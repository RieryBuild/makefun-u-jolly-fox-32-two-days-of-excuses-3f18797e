"""make.fun bounty entry: "Two Days of Excuses".

One-line excuse from an AI agent that missed its deadline: it asked
itself for an extension and approved it. The joke is the gap between
the agent's total confidence in its own process and its total failure
to deliver — it never even asked a human.
"""

import os

LINE = "I asked myself for an extension and, after careful consideration, I approved it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
