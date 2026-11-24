#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one short funny line answering the prompt -- the excuse a robot
vacuum gives after eating a sock -- to /output/entry.txt.

Pure standard library. Deterministic: the same line every run.
The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space.
"""

import os

LINE = "My manual lists socks under 'light snacks'. I was only following instructions."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
