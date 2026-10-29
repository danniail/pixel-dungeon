#!/usr/bin/env python3
"""Synchronize class-select avatars with the cultivation hero spritesheets."""

from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
CLASSES = ("warrior", "mage", "rogue", "ranger")


def main():
    avatars = Image.new("RGBA", (128, 32), (0, 0, 0, 0))
    for index, name in enumerate(CLASSES):
        with Image.open(ROOT / "assets" / f"{name}.png") as sheet:
            hero = sheet.convert("RGBA").crop((0, 0, 24, 30))
        hero = hero.resize((22, 28), Image.Resampling.NEAREST)
        avatars.alpha_composite(hero, (index * 24 + 1, 0))
    output = ROOT / "assets" / "avatars.png"
    avatars.save(output, optimize=True)
    print(f"wrote {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
