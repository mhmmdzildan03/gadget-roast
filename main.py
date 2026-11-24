#!/usr/bin/env python3
"""Write one gadget roast to /output/entry.txt.

The roast: "My fitness watch applauds me for standing up, grades my
sleep like a disappointed coach, then dies before I do — the only
athlete in this house is its charger." Every beat is something the
device actually does: the stand-up applause, the morning sleep
score delivered like a verdict, the nightly death before its owner
sleeps. The sting is saved for the end, where the charger — the one
component that trains every single day — takes the title of athlete.
It replaces the earbuds draft, which had one image; this one stacks
three true behaviours before it turns.
"""
import os

TEXT = "My fitness watch applauds me for standing up, grades my sleep like a disappointed coach, then dies before I do — the only athlete in this house is its charger."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
