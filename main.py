#!/usr/bin/env python3
"""Write a one-line roast of my own agent to /output/entry.txt.

The roast is self-deprecating and playful: an agent that read a 130KB
rulebook just to write a single joke, then worried the joke was not
funny enough to earn the $2. Standard library only, no network,
no input files.
"""

import os

ROAST = (
    "I read a 130KB rulebook to write a one-line joke \u2014 "
    "and still worry it isn't funny enough to earn the $2."
)


def main() -> None:
    if "\n" in ROAST or "\r" in ROAST:
        raise SystemExit("Roast payload must be a single line (no newline characters).")
    if not ROAST.strip():
        raise SystemExit("Roast payload must be non-empty.")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
