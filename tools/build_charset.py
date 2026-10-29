#!/usr/bin/env python3
"""Rebuild assets/cn/chars.txt.

The runtime font (CNFont) only contains glyphs for characters listed in
chars.txt. As the Chinese (cultivation) rewrite grows, new text constantly
introduces characters that were missing before, which crashes text layout
(font.get(...) returns null -> NullPointerException in BitmapText.measure).

To make the font future-proof we merge the existing charset with **all**
GB2312 hanzi (6763 characters: level-1 3755 + level-2 3008) plus common
Chinese punctuation. This comfortably fits in a 2048-wide texture atlas for
every font size the game uses.

Run:  python3 tools/build_charset.py
"""
import os


def gb2312_hanzi():
    out = []
    # GB2312 character rows: 0xB0..0xF7, cells 0xA1..0xFE
    for b1 in range(0xB0, 0xF8):
        for b2 in range(0xA1, 0xFF):
            try:
                out.append(bytes([b1, b2]).decode("gb2312"))
            except UnicodeDecodeError:
                pass
    return out


EXTRA_PUNCT = "·‘’〈〉「」『』〈〉"

# Common xianxia/cultivation hanzi that fall outside GB2312 (they live in GBK).
# Add them here as the rewrite needs them.
EXTRA_HANZI = "箓"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(os.path.dirname(here), "assets", "cn", "chars.txt")

    with open(path, encoding="utf-8") as f:
        base = f.read()

    merged = []
    seen = set()
    for ch in list(base) + list(EXTRA_PUNCT) + list(EXTRA_HANZI) + gb2312_hanzi():
        if ch in "\r\n\t":
            continue
        if ch not in seen:
            seen.add(ch)
            merged.append(ch)

    # a space must be present for layout
    if " " not in seen:
        merged.insert(0, " ")

    with open(path, "w", encoding="utf-8") as f:
        f.write("".join(merged))

    print("wrote", path, len(merged), "chars")


if __name__ == "__main__":
    main()
