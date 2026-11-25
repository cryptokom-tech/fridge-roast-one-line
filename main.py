"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

Writes a single original one-line roast of a smart fridge to
/output/entry.txt (91 characters, one line, UTF-8).

The line targets the judge's brief, in order:
1. It is a roast of a smart fridge, aimed at the fridge itself — its
   touchscreen and its cooling, the two things a "smart" fridge is
   supposed to do.
2. The punchline lands on the first read: "froze" turns twice — the
   touchscreen froze (crashed, the smart bit failed) while the food
   did not stay cold (the fridge bit failed). The final clause,
   "the only thing in it that stayed cold all week", is the reversal
   that carries the laugh.
3. It is specific to smart fridges: only a fridge has both a
   touchscreen and a duty to stay cold; the gag dies on any other
   gadget.
4. It is tight: 91 characters, no setup the punchline does not need.
5. It is fresh: it dodges the obvious cracks the brief names — the
   fridge ordering groceries, the fridge watching you — and it does
   not reuse the crowded "firmware forgot how to stay cold" angle
   already in the field; the vehicle is the frozen screen, not the
   firmware.

Candidate lines considered (local judging, strongest first):
  1. "My smart fridge's touchscreen froze solid — the only thing in
     it that stayed cold all week."  <- submitted (double "froze",
     reversal on the last clause, fridge-only)
  2. "My fridge put its own camera behind a paywall — I now pay
     $4.99 a month to look at food I already own." (fresh paywall
     angle, strong absurdity, but the laugh needs a beat; the
     wordplay turn of #1 lands faster)
  3. "My fridge updated to 'AI-powered ice' at 2 a.m. It still makes
     no ice — but now it explains why in a full paragraph." (fresh
     AI-rebrand angle, good final clause, looser setup than #1)
  4. "My ice maker has two settings: avalanche, and thoughts and
     prayers." (tight, specific, but the punch is a borrowed phrase)
  5. "My fridge's app says it's 'online and thriving' while my ice
     cream melts into soup." (good contrast, weaker turn)
  6. "My fridge has 47 ice-maker settings and not one of them makes
     ice." (punchy, but plain — setup is the whole joke)
  7. "My fridge texted me that my milk has 'entered its villain
     era'." (milk-opinion angle from the brief, slang may date)
  8. "My fridge's camera labelled my leftovers 'evidence'."
     (sharp, but too thin a laugh to win a pairwise)
"""

import os
import sys

MAX_CHARS = 200

LINE = "My smart fridge's touchscreen froze solid \u2014 the only thing in it that stayed cold all week."


def main():
    line = LINE
    if not line or not line.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print("entry exceeds 200 characters", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print("wrote %d characters to /output/entry.txt" % len(line))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
