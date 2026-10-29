#!/usr/bin/env python3
"""Build the remaining M1 cultivation-theme visual resources.

All sprite sheet dimensions and item/tile indexes are preserved.
Run from the project root: python3 tools/art/build_m1_visuals.py
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"
FONT = ROOT / "build" / "tooling" / "HiraginoSansGB.ttc"


def save(image, name):
    image.save(ASSETS / name, optimize=True)
    print("wrote", name)


def centered_text(draw, box, text, size, fill, stroke=1):
    font = ImageFont.truetype(str(FONT), size)
    x0, y0, x1, y1 = box
    bounds = draw.multiline_textbbox((0, 0), text, font=font, spacing=1, align="center")
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    x = x0 + (x1 - x0 - width) / 2 - bounds[0]
    y = y0 + (y1 - y0 - height) / 2 - bounds[1]
    draw.multiline_text(
        (x, y), text, font=font, fill=fill, spacing=1, align="center",
        stroke_width=stroke, stroke_fill="#101817",
    )


def build_banners():
    image = Image.new("RGBA", (128, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    centered_text(draw, (0, 0, 128, 70), "修仙秘境", 25, "#ffe3a1")
    centered_text(draw, (0, 70, 128, 105), "妖王伏诛", 22, "#ffe3a1")
    centered_text(draw, (0, 105, 128, 140), "道途终止", 22, "#e88772")
    centered_text(draw, (0, 140, 128, 161), "选择修士", 16, "#f2eee0")
    centered_text(draw, (0, 161, 128, 218), "修仙\n秘境", 23, "#8fcfd0")
    save(image, "banners.png")


def tint_sheet(name, dark, mid, light):
    path = ASSETS / name
    with Image.open(path) as source:
        source = source.convert("RGBA")
        alpha = source.getchannel("A")
        gray = ImageOps.grayscale(source)
        colored = ImageOps.colorize(gray, black=dark, mid=mid, white=light).convert("RGBA")
        colored.putalpha(alpha)
        return colored


def build_ui():
    for name in ("chrome.png", "dashboard.png", "status_pane.png", "toolbar.png"):
        save(tint_sheet(name, "#102b2a", "#42665d", "#e2c473"), name)
    for name in ("arcs1.png", "arcs2.png"):
        save(tint_sheet(name, "#071716", "#203b37", "#648076"), name)


def scroll_icon(rune):
    image = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle((3, 1, 12, 14), fill="#382b18", outline="#101818")
    draw.rectangle((4, 2, 11, 13), fill="#e7d28a")
    draw.line((5, 4, 10, 4), fill="#9b7a38")
    draw.line((6, 6, 9, 6, 7, 8, 10, 8, 7, 10, 9, 10, 7, 12), fill=rune, width=1)
    return image


def pill_icon(color):
    image = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((3, 3, 12, 12), fill="#151d1b", outline="#080d0c")
    draw.ellipse((4, 4, 11, 11), fill=color)
    draw.point((6, 6), fill="#fff2c2")
    draw.line((4, 13, 11, 13), fill="#6f5a34")
    return image


def artifact_icon(color):
    image = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.line((2, 13, 12, 3), fill="#101817", width=3)
    draw.line((3, 12, 12, 3), fill="#d8d9c8", width=1)
    draw.point((12, 2), fill=color)
    draw.line((4, 9, 7, 12), fill=color, width=2)
    draw.line((2, 12, 4, 14), fill="#8b6534", width=2)
    draw.point((13, 4), fill="#fff0b0")
    return image


def crystal_icon():
    image = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.polygon((3, 12, 5, 5, 8, 2, 9, 11), fill="#4ea8b5", outline="#153a42")
    draw.polygon((7, 13, 9, 7, 12, 4, 13, 12), fill="#83d6cf", outline="#153a42")
    draw.line((6, 6, 7, 9), fill="#d2fff1")
    return image


def amulet_icon():
    image = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle((3, 2, 12, 13), fill="#b4832f", outline="#30200c")
    draw.rectangle((5, 4, 10, 11), fill="#e8c96a")
    draw.rectangle((6, 5, 9, 10), fill="#7d2824")
    draw.point((7, 6), fill="#ffe8a3")
    return image


def build_items():
    path = ASSETS / "items.png"
    with Image.open(path) as source:
        image = source.convert("RGBA")

    scrolls = [40, 41, 42, 43, 44, 45, 46, 47, 76, 77, 78, 79, 117]
    runes = ["#9e2d27", "#a33b78", "#773b9e", "#315d9e", "#247d68", "#a64d24"]
    for i, index in enumerate(scrolls):
        x, y = (index % 8) * 16, (index // 8) * 16
        image.paste(scroll_icon(runes[i % len(runes)]), (x, y))

    potion_colors = [
        "#42c6bd", "#d84b43", "#4c8fd0", "#58a66b", "#e0b846", "#c456a4",
        "#4b514f", "#e4ded0", "#d9913c", "#79502e", "#5256a3", "#b9c4c8",
    ]
    for i, index in enumerate(range(56, 68)):
        x, y = (index % 8) * 16, (index // 8) * 16
        image.paste(pill_icon(potion_colors[i]), (x, y))

    wand_colors = ["#8fcfd0", "#d99c48", "#a56fd0", "#78b86a"]
    wands = [3, 48, 49, 50, 51, 52, 53, 54, 55, 68, 69, 70, 71]
    for i, index in enumerate(wands):
        x, y = (index % 8) * 16, (index // 8) * 16
        image.paste(artifact_icon(wand_colors[i % len(wand_colors)]), (x, y))

    for index, icon in ((14, crystal_icon()), (87, amulet_icon())):
        x, y = (index % 8) * 16, (index // 8) * 16
        image.paste(icon, (x, y))

    save(image, "items.png")


REGIONS = [
    {
        "dark": "#10251c", "mid": "#527057", "light": "#b5c49a",
        "water_dark": "#0b2c26", "water_mid": "#327a66", "water_light": "#91c7a4",
        "accent": "#8fc46b", "kind": "herb",
    },
    {
        "dark": "#111f2a", "mid": "#4f6875", "light": "#c1d0ce",
        "water_dark": "#102d3c", "water_mid": "#396c83", "water_light": "#a0d0d4",
        "accent": "#d5b661", "kind": "rune",
    },
    {
        "dark": "#211716", "mid": "#685047", "light": "#c49b7a",
        "water_dark": "#3b1309", "water_mid": "#b44b19", "water_light": "#ffb54a",
        "accent": "#f17b32", "kind": "ember",
    },
    {
        "dark": "#142a2c", "mid": "#63898a", "light": "#d1e0d5",
        "water_dark": "#102a3b", "water_mid": "#397b91", "water_light": "#a8e1df",
        "accent": "#e0c675", "kind": "jade",
    },
    {
        "dark": "#160f22", "mid": "#4c355d", "light": "#a889b3",
        "water_dark": "#250c31", "water_mid": "#6d2780", "water_light": "#c45bc4",
        "accent": "#c259bc", "kind": "demon",
    },
]


def add_region_motif(image, kind, color):
    draw = ImageDraw.Draw(image)
    positions = ((1, 0), (4, 0), (7, 1), (10, 2), (13, 3), (15, 1))
    for tx, ty in positions:
        cx, cy = tx * 16 + 8, ty * 16 + 8
        if kind == "herb":
            draw.line((cx, cy + 3, cx, cy - 3), fill=color)
            draw.line((cx, cy, cx - 3, cy - 2), fill=color)
            draw.line((cx, cy + 1, cx + 3, cy - 1), fill=color)
        elif kind in ("rune", "demon"):
            draw.line((cx, cy - 4, cx, cy + 4), fill=color)
            draw.line((cx - 3, cy - 1, cx + 3, cy - 1), fill=color)
            draw.point((cx - 2, cy + 3), fill=color)
            draw.point((cx + 2, cy - 3), fill=color)
        elif kind == "ember":
            draw.line((cx - 4, cy + 3, cx - 1, cy, cx + 1, cy + 1, cx + 4, cy - 3), fill=color)
        elif kind == "jade":
            draw.rectangle((cx - 3, cy - 3, cx + 3, cy + 3), outline=color)
            draw.point((cx, cy), fill=color)


def build_regions():
    for index, region in enumerate(REGIONS):
        tiles = tint_sheet(
            f"tiles{index}.png", region["dark"], region["mid"], region["light"]
        )
        add_region_motif(tiles, region["kind"], region["accent"])
        save(tiles, f"tiles{index}.png")
        water = tint_sheet(
            f"water{index}.png", region["water_dark"], region["water_mid"], region["water_light"]
        )
        save(water, f"water{index}.png")


def main():
    if not FONT.is_file():
        raise SystemExit(f"missing font: {FONT}")
    build_banners()
    build_ui()
    build_items()
    build_regions()


if __name__ == "__main__":
    main()
