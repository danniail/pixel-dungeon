#!/usr/bin/env python3
"""Validate resources needed by the Chinese cultivation build.

Uses only the Python standard library so it can run in CI or locally:
    python3 tools/validate_project.py
"""

from pathlib import Path
import re
import struct
import sys

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
SRC = ROOT / "src"
RES = ROOT / "res"


def png_size(path):
    with path.open("rb") as f:
        header = f.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError("not a valid PNG")
    return struct.unpack(">II", header[16:24])


def main():
    errors = []

    charset_path = ASSETS / "cn" / "chars.txt"
    if not charset_path.is_file():
        errors.append("missing Chinese charset: assets/cn/chars.txt")
        charset = set()
    else:
        charset = set(charset_path.read_text(encoding="utf-8"))

    used = set()
    for base in (SRC, RES):
        for path in base.rglob("*"):
            if path.suffix not in (".java", ".xml"):
                continue
            text = path.read_text(encoding="utf-8")
            used.update(re.findall(r"[\u3400-\u9fff]", text))
    missing = sorted(used - charset)
    if missing:
        errors.append("Chinese glyphs missing from assets/cn/chars.txt: " + "".join(missing))

    assets_java = SRC / "com" / "watabou" / "pixeldungeon" / "Assets.java"
    if assets_java.is_file():
        text = assets_java.read_text(encoding="utf-8")
        for value in re.findall(r'public\s+static\s+final\s+String\s+\w+\s*=\s*"([^"]+)"', text):
            if re.search(r"\.(png|ogg|mp3|txt|json)$", value) and not (ASSETS / value).is_file():
                errors.append("missing asset referenced by Assets.java: " + value)
    else:
        errors.append("missing Assets.java")

    for name in ("mage.png", "warrior.png", "rogue.png", "ranger.png"):
        path = ASSETS / name
        if not path.is_file():
            errors.append("missing hero spritesheet: assets/" + name)
            continue
        try:
            width, height = png_size(path)
        except ValueError as exc:
            errors.append(f"invalid hero spritesheet assets/{name}: {exc}")
            continue
        if width < 24 * 21 or height < 30 * 8 or width % 24 or height % 30:
            errors.append(
                f"invalid 24x30 hero layout assets/{name}: {width}x{height}; "
                "expected at least 21 columns and 8 armor tiers"
            )

    expected_sizes = {"banners.png": (128, 256), "items.png": (128, 256)}
    for index in range(5):
        expected_sizes[f"tiles{index}.png"] = (256, 64)
    for name, expected in expected_sizes.items():
        path = ASSETS / name
        if not path.is_file():
            errors.append("missing themed resource: assets/" + name)
            continue
        try:
            actual = png_size(path)
        except ValueError as exc:
            errors.append(f"invalid themed resource assets/{name}: {exc}")
            continue
        if actual != expected:
            errors.append(f"invalid dimensions assets/{name}: {actual[0]}x{actual[1]}, expected {expected[0]}x{expected[1]}")

    if errors:
        print("PROJECT VALIDATION FAILED", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
        return 1

    print(f"PROJECT VALIDATION OK: {len(used)} Chinese glyphs, referenced assets, four hero spritesheets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
