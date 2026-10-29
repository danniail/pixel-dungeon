#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Draw the xianxia (cultivator) hero sprite sheet, replacing the European mage.

Output: assets/mage.png  (256x128, 21 frames of 12x15 per tier, 8 tiers)
Frames (see HeroSprite.java):
  0,1 idle ; 2..7 run ; 8..12 die (kept as skull) ; 13..15 attack/zap ;
  16,17 operate ; 18 fly ; 19,20 read.

Each frame is a 12x15 grid of material codes. Per-tier only the robe
palette (C/L/c) changes; head, skin, inner collar, belt and shoes are shared.
"""
from PIL import Image
import os

# ---- shared material codes (non-robe) ----
# K = topknot, h = topknot highlight, H = hair, f = face, e = eye,
# w = white inner collar, b = belt, s = shoes, n = bare hand/skin,
# C/L/c = robe main/light/dark,  . = transparent
HEAD = [
    ".....KK.....",
    "...bKhhKb...",   # hairpin (b) crosses the topknot
    "...HHHHHH...",
    "..HHHHHHHH..",
    "..HfffffH...",
    "..HfefefH...",
    "..HfffffH...",   # chin
]

# Full body frames. Each pose is 8 rows describing the body from the shoulders
# (y7) to the feet (y14); the shared HEAD (topknot, hairpin, face) is injected
# on top by render_frame. An empty first row marks the airborne run pose.

F = {}

# 0 idle
F[0] = [
    ".wwffffww...",
    "wCwffffwCw..",
    "wCCwffwCCw..",
    "wCC.ww.CCw..",
    ".nnC..Cnn...",
    "..bCCCCb....",
    "..CC..CC....",
    "..ss..ss....",
]
# 1 idle alt (subtle breathing)
F[1] = [r for r in F[0]]

# 2 run: right leg forward, right arm forward
F[2] = [
    ".wwffffwn...",
    "wCwffffwCn..",
    "wCCwffwCCw..",
    "wCC.ww.CCw..",
    ".nC....Cn...",
    ".bbCCCCbb...",
    "..CC...Cn...",
    "..ss..sss...",
]
# 3 run: passing pose, feet together
F[3] = [
    ".wwffffww...",
    "wCwffffwCw..",
    "wCCwffwCCw..",
    "wCC.ww.CCw..",
    ".nC....Cn...",
    ".bbCCCCbb...",
    "..CCCCCC....",
    "..ssssss....",
]
# 4 run: airborne, whole figure drops 1px
F[4] = [
    "............",
    ".wwffffww...",
    "wCwffffwCw..",
    "wCCwffwCCw..",
    "wCC.ww.CCw..",
    ".bbCCCCbb...",
    ".sCCCCCCs...",
    "............",
]
# 5 run: left leg forward (mirror of 2)
F[5] = [
    "...nffffww..",
    "..nCwffffwCw",
    "wCCwffwCCw..",
    "wCC.ww.CCw..",
    ".nC....Cn...",
    ".bbCCCCbb...",
    "..nC...CC...",
    "..sss..ss...",
]
# 6 run: passing pose
F[6] = [
    ".wwffffww...",
    "wCwffffwCw..",
    "wCCwffwCCw..",
    "wCC.ww.CCw..",
    ".nC....Cn...",
    ".bbCCCCbb...",
    "..CCCCCC....",
    "..ssssss....",
]
# 7 run: airborne
F[7] = [
    "............",
    ".wwffffww...",
    "wCwffffwCw..",
    "wCCwffwCCw..",
    "wCC.ww.CCw..",
    ".bbCCCCbb...",
    "...sCCCCCs..",
    "............",
]

# 13 attack/zap: raise hand
F[13] = [
    ".wwffffwn...",
    "wCwffffwCn..",
    "wCCwffwCCw..",
    "wCC.ww.CCw..",
    ".nC....Cn...",
    ".bbCCCCbb...",
    "..CC..CC....",
    "..ss..ss....",
]
# 14 attack/zap: hand thrust forward
F[14] = [
    ".wwffffwnn..",
    "wCwffffwCnn.",
    "wCCwffwCCw..",
    "wCC.ww.CCw..",
    ".nC....Cn...",
    ".bbCCCCbb...",
    "..CC..CC....",
    "..ss..ss....",
]
# 15 attack: recover
F[15] = [r for r in F[0]]

# 16 operate: bend down, hands low
F[16] = [
    ".wwffffww...",
    "wCwffffwCw..",
    "wCCwffwCCw..",
    "wCC.ww.CCw..",
    ".nC....Cn...",
    "..nCCCCn....",
    "..CC..CC....",
    "..ss..ss....",
]
# 17 operate
F[17] = [r for r in F[16]]

# 18 fly (sword-riding): upright, legs together
F[18] = [
    ".wwffffww...",
    "wCwffffwCw..",
    "wCCwffwCCw..",
    "wCC.ww.CCw..",
    ".nC....Cn...",
    ".bbCCCCbb...",
    "..CCCCCC....",
    "..ssssss....",
]

# 19 read: hands raised to chest
F[19] = [
    ".wwffffww...",
    "wCnnnnnnCw..",
    "wCCwffwCCw..",
    "wCC.ww.CCw..",
    ".nC....Cn...",
    ".bbCCCCbb...",
    "..CC..CC....",
    "..ss..ss....",
]
# 20 read: holding a talisman
F[20] = [r for r in F[19]]

# ---- per-tier robe palettes: (main C, light L, dark c) ----
# classic cultivator robe colors
TIERS = [
    ((150, 140, 120), (182, 172, 152), (110, 100, 84)),  # 0 no armor: plain hemp
    ((72, 118, 94), (108, 156, 128), (48, 84, 68)),      # 1 cloth: Han Li teal-green
    ((96, 110, 130), (138, 150, 168), (64, 76, 96)),     # 2 leather: slate blue-grey
    ((120, 96, 64), (158, 132, 92), (86, 68, 44)),       # 3 mail: ochre / hemp
    ((96, 130, 120), (138, 170, 158), (64, 92, 84)),     # 4 scale: pale jade
    ((150, 60, 56), (192, 102, 92), (106, 40, 40)),      # 5 plate: cinnabar red
    ((120, 54, 40), (162, 86, 60), (84, 38, 28)),        # 6 heavy: deep crimson
    ((70, 84, 120), (110, 126, 160), (46, 58, 88)),      # 7 class robe: dark indigo
]

SHARED = {
    'K': (30, 23, 20), 'h': (74, 58, 48), 'H': (46, 36, 30),
    'f': (226, 186, 152), 'e': (26, 20, 16),
    'w': (242, 242, 232), 'b': (120, 86, 52),
    's': (38, 30, 24), 'n': (206, 160, 124),
}


def render_frame(mat, tier):
    # mat is 8 rows: the body from the shoulders (y7) down to the feet (y14).
    # An empty first row marks the airborne (run) pose: the whole figure drops
    # one pixel, so the head is shifted down and the last body row is clipped.
    drop = 1 if mat[0].strip('.') == '' else 0
    C, L, c = TIERS[tier]
    pal = dict(SHARED)
    pal['C'] = C; pal['L'] = L; pal['c'] = c
    out = Image.new('RGBA', (12, 15), (0, 0, 0, 0))
    # shared head (topknot, hairpin, face)
    for y, row in enumerate(HEAD):
        hy = y + drop
        for x, code in enumerate(row):
            if code != '.':
                out.putpixel((x, hy), pal[code] + (255,))
    # pose-specific body
    for by, row in enumerate(mat):
        y = by + 7 + drop
        if y >= 15:
            break
        for x, code in enumerate(row):
            if code != '.':
                out.putpixel((x, y), pal[code] + (255,))
    return out


# ---- class-selection avatar (24x28, side view facing right) ----
_AVATAR_ROWS = [
    "............KK", "...........KhhK", "..........KhhhKK",
    ".........HHHHHHHH", "........HHHHHHHHHH", ".......HHHHHHHHHHHH",
    ".......HHHfffffHHH", ".......HHffffffffHH", ".......Hffffffffffn",
    ".......Hfefefffffn", "........Hffffffffn", "........HHfffffnn",
    ".........HHffff", "..........ffff", "........wwwwwwww",
    ".......wCwffffwCw", "......cCwCCffwCCw", "......cLCCCCCCCLc",
    "......cLCCCCCCCLc", "......cCCCCCCCCc", "......bbCCCCCCbb",
    "......cCCCCCCCCc", "......cCCCCCCCCc", "......cCCCCCCCCc",
    "......cCCCCCCCCc", "......cCCCCCCCCc", "......ssCCCCCCss", "",
]
AVATAR = [r.ljust(24, '.')[:24] for r in _AVATAR_ROWS]


def render_avatar():
    # the class-selection avatar always wears the signature Han Li teal robe
    C, L, c = (72, 118, 94), (108, 156, 128), (48, 84, 68)
    pal = dict(SHARED)
    pal['C'] = C; pal['L'] = L; pal['c'] = c
    out = Image.new('RGBA', (24, 28), (0, 0, 0, 0))
    for y, row in enumerate(AVATAR):
        for x, code in enumerate(row):
            if code != '.':
                out.putpixel((x, y), pal[code] + (255,))
    return out


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    sheet = Image.new('RGBA', (256, 128), (0, 0, 0, 0))

    # keep the original die frames (8..12) from the existing sheet
    old = Image.open(os.path.join(root, 'assets', 'mage.png')).convert('RGBA')

    for tier in range(8):
        for f in range(21):
            if 8 <= f <= 12:
                # copy skull frames from old sheet
                fr = old.crop((f * 12, tier * 15, f * 12 + 12, tier * 15 + 15))
            else:
                fr = render_frame(F[f], tier)
            sheet.paste(fr, (f * 12, tier * 15))

    out = os.path.join(root, 'assets', 'mage.png')
    sheet.save(out)
    print('wrote', out, sheet.size)

    # replace the mage avatar (2nd slot) in the class-selection sheet
    av_path = os.path.join(root, 'assets', 'avatars.png')
    avatars = Image.open(av_path).convert('RGBA')
    blank = Image.new('RGBA', (24, 28), (0, 0, 0, 0))
    avatars.paste(blank, (24, 0))          # clear the old slot first
    avatars.paste(render_avatar(), (24, 0))
    avatars.save(av_path)
    print('wrote', av_path, avatars.size)


if __name__ == '__main__':
    main()
