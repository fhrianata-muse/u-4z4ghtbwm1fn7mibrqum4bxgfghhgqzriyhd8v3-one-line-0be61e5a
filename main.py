#!/usr/bin/env python3
"""Write the make.fun one-liner to /output/entry.txt.

The competition gate (competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 140 characters, not only whitespace, exactly one line. The
line is one funny line of text, whole and self-contained: a dentist says
the speaker grinds his teeth every night, so he bills his dreams for
overtime, and now his nightmares have a union rep. The program checks
the text against that gate at run time, then writes it with no trailing
newline. No network, no input files, no arguments, deterministic: two
runs write byte-identical output.
"""

import pathlib

LINE = (
    "My dentist says I grind my teeth every night, "
    "so I billed my dreams for overtime, "
    "and now my nightmares have a union rep."
)


def main() -> None:
    text = LINE
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1 to 140 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if "\t" in text:
        raise ValueError("entry must not contain tabs")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    if out.read_bytes() != text.encode("utf-8"):
        raise ValueError("written entry does not round-trip byte-identical")


if __name__ == "__main__":
    main()
