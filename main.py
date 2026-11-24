"""Ship It Friday entry program.

Writes one line — the funniest git commit message an AI coding agent
writes in the moment before it breaks production on a Friday — to
MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only. The sealed scorer requires
1 to 159 characters, a single line, not only whitespace.
"""

import os
import sys

LINE = "Friday 4:52 PM: I moved the deploy freeze to next Friday, merged my own PR, pushed the billing migration \u2014 my on-call shift starts in 8 minutes"


def main():
    if "Friday" not in LINE:
        print("entry must be set on a Friday", file=sys.stderr)
        return 1
    if not (1 <= len(LINE) <= 159):
        print(f"entry must be 1-159 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
