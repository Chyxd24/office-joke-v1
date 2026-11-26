#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Competition: u-suzy-one-line-office-joke-laugh-off-f574ac73
Writes one original one-line office joke to /output/entry.txt.
Gate: UTF-8, 1..200 chars, not only whitespace.
Judge brief: one-line office joke, sharp surprising punchline,
clear on one read, fresh (no cliche), tight wording.
"""
import os
import sys

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")
MIN_LEN = 1
MAX_LEN = 200

JOKE = (
    "I told my boss exactly what I think of him. "
    "He said 'great, see you at 3pm' and updated the calendar."
)


def build_line() -> str:
    """Return the entry joke, stripped and gate-checked."""
    line = JOKE.strip()
    if not (MIN_LEN <= len(line) <= MAX_LEN):
        raise SystemExit(f"joke out of gate range: {len(line)} chars")
    return line


def write_entry(line: str) -> str:
    """Persist the line to /output/entry.txt and read it back."""
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    with open(OUT_FILE, "r", encoding="utf-8") as f:
        back = f.read().strip()
    assert back == line, "readback mismatch against /output/entry.txt"
    return back


def main() -> int:
    """Entry point: build, write, readback-assert, report."""
    line = build_line()
    back = write_entry(line)
    print(f"OK len={len(back)} -> {OUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
