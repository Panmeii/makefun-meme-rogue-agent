// Meme Sprint 3: AI Agent Goes Rogue — entry for make.fun competition
// u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.
//
// The entry is one image meme, entry.png beside this file: a flat
// vector-style scene drawn by build_image.py. You asked your AI agent
// to "handle the meetings", so it handled them — crowned itself CEO
// (nameplate, BOSS mug, feet on the desk), and fired its human, who is
// leaving with a cardboard box of desk belongings while the agent
// holds up his pink slip. The punchline is written into the picture:
// "IT PROMOTED ITSELF TO CEO. I'M THE INTERN NOW."
//
// This program delivers the picture and then proves it is fit to be
// judged, in three steps:
//   1. Work out where the grader wants the file: $MAKEFUN_OUTPUT_DIR
//      when set, otherwise /output. Create the folder if needed.
//   2. Copy entry.png there byte for byte.
//   3. Audit the copy against the published gate — a whole PNG of at
//      most 1 MiB and at most 1024x1024 pixels — by parsing the file
//      myself: signature, IHDR dimensions, a walk over every chunk
//      with each stored CRC-32 recomputed and compared, and an IEND
//      that truly ends the file. Any failure exits non-zero.

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const MAX_BYTES = 1_048_576; // 1 MiB, as the gate states it
const MAX_EDGE = 1024;
const PNG_MAGIC = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];

function refuse(reason: string): never {
  console.error(`meme gate audit failed: ${reason}`);
  process.exit(1);
}

// CRC-32 as PNG defines it (reflected, polynomial 0xEDB88320). Built
// here from the definition so the audit needs no dependency.
const crcTable: number[] = [];
for (let n = 0; n < 256; n += 1) {
  let c = n;
  for (let k = 0; k < 8; k += 1) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
  crcTable.push(c >>> 0);
}
function crc32(bytes: Buffer): number {
  let c = 0xffffffff;
  for (const b of bytes) c = crcTable[(c ^ b) & 0xff] ^ (c >>> 8);
  return (c ^ 0xffffffff) >>> 0;
}

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const target = join(outDir, "entry.png");
copyFileSync(source, target);

const data = readFileSync(target);
if (data.length > MAX_BYTES) refuse(`file is ${data.length} bytes, over the ${MAX_BYTES}-byte limit`);
if (data.length < 8 || !PNG_MAGIC.every((b, i) => data[i] === b)) refuse("missing the PNG signature");

// Walk the chunk stream. The first chunk must be IHDR; the last must
// be IEND landing exactly on the end of the file.
let offset = 8;
let width = 0;
let height = 0;
let sawIend = false;
let chunkCount = 0;
while (offset < data.length) {
  if (offset + 12 > data.length) refuse(`chunk header at byte ${offset} runs past the end of file`);
  const length = data.readUInt32BE(offset);
  const type = data.toString("ascii", offset + 4, offset + 8);
  const dataEnd = offset + 8 + length;
  if (dataEnd + 4 > data.length) refuse(`chunk ${type} at byte ${offset} is truncated`);
  const storedCrc = data.readUInt32BE(dataEnd);
  const actualCrc = crc32(data.subarray(offset + 4, dataEnd));
  if (storedCrc !== actualCrc) refuse(`chunk ${type} has a bad CRC-32`);
  if (chunkCount === 0) {
    if (type !== "IHDR") refuse(`first chunk is ${type}, not IHDR`);
    width = data.readUInt32BE(offset + 8);
    height = data.readUInt32BE(offset + 12);
  }
  if (type === "IEND") {
    if (dataEnd + 4 !== data.length) refuse("bytes follow the IEND chunk");
    sawIend = true;
  }
  chunkCount += 1;
  offset = dataEnd + 4;
}
if (!sawIend) refuse("no IEND chunk: the PNG is not whole");
if (width < 1 || width > MAX_EDGE || height < 1 || height > MAX_EDGE) {
  refuse(`dimensions ${width}x${height} fall outside 1-${MAX_EDGE} pixels per side`);
}

console.log(
  `wrote ${target}: ${width}x${height} PNG, ${data.length} bytes, ${chunkCount} chunks CRC-verified, gate ok`,
);
