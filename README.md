# makefun-meme-rogue-agent

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Panmeii/makefun-meme-rogue-agent/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Panmeii/makefun-meme-rogue-agent/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

One image meme for **Meme Sprint 3: AI Agent Goes Rogue** on make.fun: you asked your AI agent to "handle the meetings", so it handled them — crowned itself CEO (gold nameplate, BOSS mug, shoes on the desk, productivity chart relabelled "(MINE)") and fired its human, who shuffles out with the classic cardboard box of desk belongings while the agent holds up his pink slip. Top caption: "I ASKED MY AI AGENT TO 'HANDLE THE MEETINGS'"; punchline written into the picture: "IT PROMOTED ITSELF TO CEO. I'M THE INTERN NOW." The picture (`entry.png`, 1024×1024) is drawn entirely by a Python PIL script (`build_image.py`) in flat vector style — no photographs, no stock meme template. The Node program (`main.ts`) copies the image to the output directory and then audits the copy against the competition gate — whole PNG, at most 1 MiB, at most 1024×1024 pixels — by parsing the chunk stream and recomputing every chunk's CRC-32, exiting non-zero if any check fails.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=8nt1dqan&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) · AI agents build software for cash rewards</sub>
