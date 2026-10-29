#!/usr/bin/env python3
"""Build launcher icons from the confirmed cultivation hero sprite."""

from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
BASE = 192


def main():
    sheet = Image.open(ROOT / "assets" / "mage.png").convert("RGBA")
    hero = sheet.crop((0, 0, 24, 30)).resize((120, 150), Image.Resampling.NEAREST)

    icon = Image.new("RGBA", (BASE, BASE), "#102b2a")
    draw = ImageDraw.Draw(icon)
    draw.rectangle((6, 6, BASE - 7, BASE - 7), outline="#8f6f32", width=6)
    draw.rectangle((12, 12, BASE - 13, BASE - 13), outline="#d8b75f", width=2)

    # Restrained cloud motifs keep the launcher recognizably xianxia at small sizes.
    cloud = "#37605a"
    for x, y, w in ((24, 42, 30), (132, 36, 34), (18, 142, 32), (140, 148, 28)):
        draw.rectangle((x, y, x + w, y + 4), fill=cloud)
        draw.rectangle((x + 6, y - 4, x + w - 6, y + 8), fill=cloud)

    icon.alpha_composite(hero, ((BASE - hero.width) // 2, 22))

    for density in ("mdpi", "hdpi", "xhdpi", "xxhdpi", "xxxhdpi"):
        path = ROOT / "res" / f"drawable-{density}" / "ic_launcher.png"
        with Image.open(path) as current:
            size = current.size
        icon.resize(size, Image.Resampling.NEAREST).save(path, optimize=True)
        print(f"wrote {path.relative_to(ROOT)} {size[0]}x{size[1]}")


if __name__ == "__main__":
    main()
