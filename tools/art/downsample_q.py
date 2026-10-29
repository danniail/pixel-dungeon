#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Q版 run cycle 降采样到 12x15：统一比例、脚对齐地面、块平均、量化。"""
from PIL import Image
import numpy as np
import sys
sys.path.insert(0, 'tools/art')
from xian_frames import PAL

# 角色本体边界（x0,x1,y0,y1），已排除阴影
CHARS = [
    (43, 573, 253, 1254),
    (604, 1114, 311, 1248),
    (1143, 1596, 227, 1250),
    (1613, 2092, 78, 1169),
    (2077, 2567, 207, 1225),
    (2577, 3054, 207, 1248),
]
GROUND_Y = 1250
REF_H = 1000
TW, TH = 12, 15


def is_bg(a):
    r, g, b = a[:, :, 0].astype(int), a[:, :, 1].astype(int), a[:, :, 2].astype(int)
    return (r > 210) & (g > 200) & (b > 180) & (np.abs(r - g) < 35) & (np.abs(g - b) < 45)


def quantize(im):
    arr = np.array(im).astype(int)
    out = np.zeros((TH, TW, 4), dtype=np.uint8)
    keys = list(PAL.keys())
    pal = np.array([PAL[k] for k in keys])
    for y in range(TH):
        for x in range(TW):
            r, g, b, a = arr[y, x]
            if a < 110:
                continue
            d = ((pal[:, 0] - r) ** 2 + (pal[:, 1] - g) ** 2 + (pal[:, 2] - b) ** 2)
            k = keys[d.argmin()]
            out[y, x] = np.array(PAL[k] + (255,))
    return Image.fromarray(out)


def build():
    src = Image.open('tools/art/xian/_run_q.png').convert('RGBA')
    scale = TH / REF_H
    frames = []
    for (x0, x1, y0, y1) in CHARS:
        sub = src.crop((x0, y0, x1 + 1, y1 + 1))
        w, h = sub.size
        nw = max(1, round(w * scale))
        nh = max(1, round(h * scale))
        small = sub.resize((nw, nh), Image.LANCZOS)
        canvas = Image.new('RGBA', (TW, TH), (0, 0, 0, 0))
        # 脚对齐：脚 y1 相对 GROUND
        foot_y = y1
        paste_y = TH - round((GROUND_Y - foot_y) * scale) - nh
        paste_x = (TW - nw) // 2
        canvas.paste(small, (paste_x, paste_y), small)
        frames.append(quantize(canvas))
    return frames


if __name__ == '__main__':
    frames = build()
    s = 16
    W = len(frames) * (12 * s + 6)
    row = Image.new('RGBA', (W, 15 * s), (90, 82, 64, 255))
    for i, f in enumerate(frames):
        z = f.resize((12 * s, 15 * s), Image.NEAREST)
        row.paste(z, (i * (12 * s + 6), 0), z)
    row.save('tools/art/xian/_run_q_ds.png')
    print('saved')
