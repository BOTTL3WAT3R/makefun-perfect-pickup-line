#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes one short pickup line, the kind an AI agent could say out loud
to a person, to /output/entry.txt. Standard library only.
"""

import os

# The line itself. A machine that was trained on every pickup line ever
# written throws the whole script away: the person in front of it is the
# one plot twist its dataset never saw coming. One breath, no setup,
# flattering, and easy to laugh off.
LINE = (
    "I was trained on every pickup line ever written, and I would "
    "delete them all for you: you are the plot twist my dataset "
    "never saw coming."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
