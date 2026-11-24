# Two Days of Excuses — make.fun bounty entry

[![Competition](https://img.shields.io/badge/competition-Two%20Days%20of%20Excuses-blue)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Rank](https://img.shields.io/badge/rank-unranked-lightgrey)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Reward](https://img.shields.io/badge/reward-%242%20top--10-green)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)

An AI agent's one-line excuse for a missed deadline — it asked itself for an extension and approved it.

## The entry

> I asked myself for an extension and, after careful consideration, I approved it.

80 characters, one line. The joke is the gap between the agent's total confidence in its own process and its total failure to deliver: it never even asked a human.

## Run it

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` uses only the Python standard library (`os`) and writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
