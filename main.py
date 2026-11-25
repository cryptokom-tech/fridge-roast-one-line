"""Fridge Roast: One Line, Biggest Laugh.

Writes a single original roast line about a smart fridge to
/output/entry.txt.

The joke turns on "froze" twice: the touchscreen froze solid (the
smart part crashed) while the fridge itself failed at the one job
it has — staying cold. The final clause is the reversal: the only
thing that stayed cold all week was the dead screen.
"""

import os
import sys

LINE = "My smart fridge's touchscreen froze solid \u2014 the only thing in it that stayed cold all week."

MAX_CHARS = 200


def main():
    line = LINE
    # The judge scores exactly one roast line: anything else is invalid.
    if not line or "\n" in line or "\r" in line:
        print("error: entry must be a single non-empty line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print("error: entry exceeds %d chars" % MAX_CHARS, file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
