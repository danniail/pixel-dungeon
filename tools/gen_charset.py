#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the font character set for the Simplified Chinese build.

Scans every Java source file under src/, extracts the contents of all
string literals (handling escapes), and collects the union of characters.
The full printable ASCII set is always included. The result is written to
assets/cn/chars.txt, which CNFont reads at runtime.

Usage:
    python3 tools/gen_charset.py
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, "assets", "cn", "chars.txt")

# Matches a double-quoted string literal, including escaped characters.
STRING_RE = re.compile(r'"((?:[^"\\\n]|\\.)*)"')

ESCAPES = {
    "n": "\n", "t": "\t", "r": "\r", "b": "\b", "f": "\f",
    '"': '"', "'": "'", "\\": "\\",
}


def unescape(literal):
    out = []
    i = 0
    while i < len(literal):
        ch = literal[i]
        if ch == "\\" and i + 1 < len(literal):
            nxt = literal[i + 1]
            if nxt in ESCAPES:
                out.append(ESCAPES[nxt])
                i += 2
                continue
            if nxt == "u" and i + 5 < len(literal) + 1 and i + 6 <= len(literal):
                hexd = literal[i + 2:i + 6]
                if len(hexd) == 4:
                    try:
                        out.append(chr(int(hexd, 16)))
                        i += 6
                        continue
                    except ValueError:
                        pass
            out.append(nxt)
            i += 2
        else:
            out.append(ch)
            i += 1
    return "".join(out)


def main():
    chars = set()
    # Full printable ASCII.
    for c in range(0x20, 0x7F):
        chars.add(chr(c))

    for dirpath, _dirnames, filenames in os.walk(SRC):
        for name in filenames:
            if not name.endswith(".java"):
                continue
            path = os.path.join(dirpath, name)
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            for match in STRING_RE.finditer(content):
                for ch in unescape(match.group(1)):
                    if ch in ("\n", "\r", "\t"):
                        continue
                    chars.add(ch)

    # Order: ASCII first, then everything else by code point.
    ordered = sorted(chars, key=lambda c: (ord(c) >= 0x7F, ord(c)))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("".join(ordered))

    cjk = sum(1 for c in ordered if 0x4E00 <= ord(c) <= 0x9FFF)
    print("chars: %d total, %d CJK ideographs -> %s" % (len(ordered), cjk, OUT))


if __name__ == "__main__":
    sys.exit(main())
