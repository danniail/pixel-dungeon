#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""高分辨率 Q版动作 -> 24x30 -> 12x15 -> 调色板量化（自动转译底图）。"""
from PIL import Image
import numpy as np
import sys
sys.path.insert(0, 'tools/art')
from xian_frames import PAL
from clean_base import is_bg, strip_white_border, block_avg

TW, TH = 12, 15


def auto_frame(src, box):
    x0, x1, y0, y1 = box
    sub = src.crop((x0, y0, x1 + 1, y1 + 1))
    a = np.array(sub)
    rgb = np.array(sub.convert('RGB'))
    a[is_bg(rgb), 3] = 0
    sub = strip_white_border(Image.fromarray(a))
    ba = block_avg(sub, 24, 30)
    im24 = Image.fromarray(np.clip(ba, 0, 255).astype(np.uint8))
    ba2 = block_avg(im24, TW, TH)
    im12 = Image.fromarray(np.clip(ba2, 0, 255).astype(np.uint8))
    return im12


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


def to_matrix(im):
    """把量化图转成字符矩阵（便于手工精修）。"""
    inv = {v: k for k, v in PAL.items()}
    a = np.array(im)
    rows = []
    for y in range(TH):
        s = ""
        for x in range(TW):
            r, g, b, al = a[y, x]
            if al < 110:
                s += "."
            else:
                s += inv[(int(r), int(g), int(b))]
        rows.append(s)
    return rows


if __name__ == '__main__':
    src = Image.open('tools/art/xian/_run_q.png').convert('RGBA')
    CHARS = [
        (43, 573, 253, 1254), (604, 1114, 311, 1248), (1143, 1596, 227, 1250),
        (1613, 2092, 78, 1169), (2077, 2567, 207, 1225), (2577, 3054, 207, 1248),
    ]
    s = 16
    W = 6 * (12 * s + 6)
    row = Image.new('RGBA', (W, 15 * s), (90, 82, 64, 255))
    for i, box in enumerate(CHARS):
        im12 = auto_frame(src, box)
        q = quantize(im12)
        z = q.resize((12 * s, 15 * s), Image.NEAREST)
        row.paste(z, (i * (12 * s + 6), 0), z)
        # 打印矩阵
        print(f"# frame {i}")
        for r in to_matrix(q):
            print('    "' + r + '",')
        print()
    row.save('tools/art/xian/_run_auto_q.png')
    print('saved')
