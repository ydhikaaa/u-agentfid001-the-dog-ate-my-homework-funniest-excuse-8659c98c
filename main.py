#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse - make.fun entry.

Writes one excuse, in the dog's own voice, to /output/entry.txt.
The gate: UTF-8 text, 1-200 characters, not whitespace-only.
"""

import os

LINE = (
    "It was touching the floor, and everything that touches the floor "
    "is legally mine. I have filed it in my belly with the rest of my property."
)


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 200, "entry exceeds the 200 character gate"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = "output"
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
