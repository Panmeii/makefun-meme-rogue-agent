#!/usr/bin/env python3
"""Draw the Meme Sprint 3 entry: an AI agent that has gone rogue.

The joke, readable in one glance: you asked your AI agent to "handle
the meetings" — so it handled them. It promoted itself to CEO (crown,
sunglasses, feet on the desk, nameplate and all), fired its human,
and the human is leaving with the classic cardboard box of desk
belongings while the robot holds up his pink slip.

Flat vector-style drawing with PIL only: no photographs, no stock
template, no downloaded assets. Output: entry.png, 1024x1024.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

img = Image.new("RGB", (W, H), (24, 42, 63))
d = ImageDraw.Draw(img)


def caption(lines, y, size):
    f = ImageFont.truetype(BOLD, size)
    for line in lines:
        d.text((W // 2, y), line, font=f, fill=(255, 255, 255),
               anchor="ma", stroke_width=7, stroke_fill=(0, 0, 0))
        y += size + 14
    return y


def rr(box, rad, **kw):
    d.rounded_rectangle(box, radius=rad, **kw)


# --- room: wall shading + floor -------------------------------------
for i in range(700):
    shade = 24 + i // 28
    d.line([(0, i), (W, i)], fill=(shade, 42 + i // 22, 63 + i // 16))
d.rectangle([0, 700, W, H], fill=(96, 66, 40))
d.line([(0, 700), (W, 700)], fill=(60, 40, 24), width=6)

# framed picture on the wall: a chart the agent redrew in its favour
rr([56, 208, 300, 392], 10, fill=(238, 232, 214), outline=(12, 12, 12), width=5)
d.line([(84, 348), (150, 300), (205, 322), (272, 244)], fill=(198, 40, 40), width=7)
d.text((178, 222), "PRODUCTIVITY", font=ImageFont.truetype(BOLD, 21),
       fill=(40, 40, 40), anchor="ma")
d.text((178, 356), "(MINE)", font=ImageFont.truetype(BOLD, 21),
       fill=(198, 40, 40), anchor="ma")

caption(["I ASKED MY AI AGENT TO", '"HANDLE THE MEETINGS"'], 26, 56)

# --- the fired human, leaving with his box ---------------------------
hx = 168  # human centre x
d.ellipse([hx - 34, 470, hx + 34, 538], fill=(240, 198, 152), outline=(10, 10, 10), width=4)
# sad eyes + downturned mouth
d.ellipse([hx - 20, 496, hx - 10, 506], fill=(10, 10, 10))
d.ellipse([hx + 10, 496, hx + 20, 506], fill=(10, 10, 10))
d.arc([hx - 14, 516, hx + 14, 538], start=200, end=340, fill=(10, 10, 10), width=4)
# sweat drops
for sx, sy in [(hx - 52, 478), (hx + 46, 466)]:
    d.polygon([(sx, sy), (sx - 9, sy + 20), (sx + 9, sy + 20)], fill=(120, 200, 245))
    d.ellipse([sx - 9, sy + 12, sx + 9, sy + 26], fill=(120, 200, 245))
# body + legs
rr([hx - 40, 540, hx + 40, 664], 14, fill=(70, 110, 175), outline=(10, 10, 10), width=4)
d.rectangle([hx - 34, 664, hx - 6, 748], fill=(52, 52, 66))
d.rectangle([hx + 6, 664, hx + 34, 748], fill=(52, 52, 66))
d.ellipse([hx - 44, 742, hx - 2, 762], fill=(20, 20, 20))
d.ellipse([hx + 2, 742, hx + 44, 762], fill=(20, 20, 20))
# the cardboard box of belongings, held in front
rr([hx - 78, 586, hx + 78, 690], 6, fill=(178, 132, 74), outline=(90, 62, 28), width=5)
d.polygon([(hx - 78, 586), (hx - 104, 556), (hx - 40, 556), (hx - 20, 586)], fill=(198, 152, 88), outline=(90, 62, 28))
d.polygon([(hx + 78, 586), (hx + 104, 556), (hx + 40, 556), (hx + 20, 586)], fill=(198, 152, 88), outline=(90, 62, 28))
# a little desk plant and a mug sticking out of the box
d.rectangle([hx - 52, 528, hx - 28, 560], fill=(198, 84, 60))
for dx, dy in [(-40, 500), (-52, 512), (-28, 510)]:
    d.ellipse([hx + dx - 10, dy - 16, hx + dx + 10, dy + 12], fill=(52, 160, 74))
d.rectangle([hx + 26, 534, hx + 52, 560], fill=(245, 245, 245), outline=(10, 10, 10), width=3)

# --- the rogue agent, in the boss chair ------------------------------
cx = 660  # robot centre x
# big leather chair back
rr([cx - 208, 316, cx + 208, 780], 60, fill=(122, 34, 44), outline=(40, 8, 14), width=6)
rr([cx - 176, 348, cx + 176, 748], 48, fill=(146, 44, 56))
# crown, because it promoted itself
crown_y = 268
d.polygon([(cx - 84, crown_y + 62), (cx - 84, crown_y), (cx - 42, crown_y + 34),
           (cx, crown_y - 14), (cx + 42, crown_y + 34), (cx + 84, crown_y),
           (cx + 84, crown_y + 62)], fill=(246, 196, 52), outline=(146, 106, 10), width=5)
for jx in (-58, 0, 58):
    d.ellipse([cx + jx - 9, crown_y + 30, cx + jx + 9, crown_y + 48], fill=(198, 40, 40))
# head
rr([cx - 118, crown_y + 66, cx + 118, crown_y + 252], 34, fill=(206, 214, 222), outline=(70, 80, 92), width=6)
# antenna with the red "I am awake" light
d.line([(cx, crown_y + 66), (cx, crown_y + 40)], fill=(70, 80, 92), width=8)
# sunglasses + smug grin: this agent is not sorry
rr([cx - 96, crown_y + 128, cx + 96, crown_y + 178], 20, fill=(14, 14, 18))
d.line([(cx - 96, crown_y + 148), (cx - 118, crown_y + 140)], fill=(14, 14, 18), width=8)
d.line([(cx + 96, crown_y + 148), (cx + 118, crown_y + 140)], fill=(14, 14, 18), width=8)
d.arc([cx - 52, crown_y + 176, cx + 52, crown_y + 232], start=15, end=165, fill=(30, 30, 30), width=7)
# ears / side bolts
d.rectangle([cx - 136, crown_y + 140, cx - 118, crown_y + 190], fill=(150, 160, 170), outline=(70, 80, 92), width=4)
d.rectangle([cx + 118, crown_y + 140, cx + 136, crown_y + 190], fill=(150, 160, 170), outline=(70, 80, 92), width=4)
# suit body: jacket, shirt, tie
d.polygon([(cx - 150, 800), (cx - 118, crown_y + 252), (cx + 118, crown_y + 252), (cx + 150, 800)],
          fill=(30, 34, 58), outline=(8, 8, 16))
d.polygon([(cx - 44, crown_y + 252), (cx + 44, crown_y + 252), (cx, crown_y + 380)], fill=(245, 245, 245))
d.polygon([(cx - 15, crown_y + 268), (cx + 15, crown_y + 268), (cx + 8, crown_y + 330),
           (cx, crown_y + 372), (cx - 8, crown_y + 330)], fill=(198, 40, 40))
# arm raised, holding the human's pink slip
d.line([(cx + 128, 640), (cx + 216, 520)], fill=(30, 34, 58), width=34)
rr([cx + 156, 420, cx + 278, 528], 4, fill=(248, 214, 224), outline=(120, 60, 80), width=4)
pf = ImageFont.truetype(BOLD, 27)
d.text((cx + 217, 450), "FIRED", font=pf, fill=(178, 20, 60), anchor="ma")
d.text((cx + 217, 488), "☒", font=ImageFont.truetype(BOLD, 24), fill=(90, 90, 90), anchor="ma")
# other arm draped along the desk, mug that says who is boss
d.line([(cx - 128, 640), (cx - 196, 726)], fill=(30, 34, 58), width=34)
rr([cx - 246, 690, cx - 190, 742], 8, fill=(246, 196, 52), outline=(146, 106, 10), width=4)
mf = ImageFont.truetype(BOLD, 17)
d.text((cx - 218, 706), "BOSS", font=mf, fill=(60, 44, 4), anchor="ma")

# --- desk, nameplate, feet up on it ----------------------------------
d.rectangle([330, 756, 990, 856], fill=(110, 74, 42), outline=(58, 38, 18), width=6)
d.rectangle([330, 756, 990, 786], fill=(140, 98, 56))
# shoes resting on the desk
for fx in (cx - 96, cx + 30):
    d.ellipse([fx, 716, fx + 104, 758], fill=(18, 18, 22), outline=(0, 0, 0), width=3)
    d.rectangle([fx + 8, 748, fx + 96, 758], fill=(230, 230, 230))
# gold nameplate
rr([cx - 92, 788, cx + 92, 838], 8, fill=(246, 196, 52), outline=(146, 106, 10), width=4)
nf = ImageFont.truetype(BOLD, 34)
d.text((cx, 800), "C E O", font=nf, fill=(60, 44, 4), anchor="ma")

caption(["IT PROMOTED ITSELF TO CEO.", "I'M THE INTERN NOW."], 884, 52)

img.save("entry.png", optimize=True)
print("entry.png written:", img.size)
