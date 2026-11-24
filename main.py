"""The Funniest Out-of-Office — make.fun bounty entry.

Writes one line of out-of-office auto-reply text to ``entry.txt``.
Standard library only (``os``, ``sys``) — no dependencies.
"""

import os
import sys

ENTRY = "I'm out of office until Monday. I'm actually at my desk — this reply is my alibi, so please play along."


def main():
    line = ENTRY
    assert 1 <= len(line) <= 140, "entry must be 1-140 characters"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
