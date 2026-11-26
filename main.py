#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry — u-suzy-one-line-office-joke-laugh-off-f574ac73.

Writes one original one-line office joke to /output/entry.txt.
Gate: UTF-8, 1..200 chars, not only whitespace.
"""
import os

JOKE = "I told my boss exactly what I think of him. He said 'great, see you at 3pm' and updated the calendar."

OUT = "/output/entry.txt"


def main() -> int:
    line = JOKE.strip()
    if not (1 <= len(line) <= 200):
        raise SystemExit(f"joke out of gate range: {len(line)} chars")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    with open(OUT, "r", encoding="utf-8") as f:
        back = f.read().strip()
    assert back == line, "readback mismatch"
    print(f"OK len={len(back)} -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
