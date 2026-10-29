#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 Q版角色转成干净的 12x15 块平均底图（去背景、去贴纸白边）。"""
from PIL import Image
import numpy as np

TW, TH = 12, 15


def is_bg(rgb):
    r, g, b = rgb[:, :, 0].astype(int), rgb[:, :, 1].astype(int), rgb[:, :, 2].astype(int)
    return (r > 205) & (g > 195) & (b > 175) & (np.abs(r - g) < 38) & (np.abs(g - b) < 48)


def is_white(rgb):
    r, g, b = rgb[:, :, 0].astype(int), rgb[:, :, 1].astype(int), rgb[:, :, 2].astype(int)
    return (r > 225) & (g > 225) & (b > 218)


def strip_white_border(rgba, iters=6):
    """把与透明相邻的白色像素设为透明（去贴纸白边）。"""
    a = np.array(rgba)
    h, w = a.shape[:2]
    for _ in range(iters):
        alpha = a[:, :, 3] > 0
        rgb = a[:, :, :3]
        white = is_white(rgb)
        # 与透明相邻
        border = np.zeros((h, w), bool)
        border[:-1, :] |= ~alpha[1:, :]
        border[1:, :] |= ~alpha[:-1, :]
        border[:, :-1] |= ~alpha[:, 1:]
        border[:, 1:] |= ~alpha[:, :-1]
        remove = white & border & alpha
        a[remove, 3] = 0
    return Image.fromarray(a)


def block_avg(im, nw, nh):
    """块平均缩放到 nw x nh，保留 alpha。"""
    a = np.array(im).astype(float)
    h, w = a.shape[:2]
    out = np.zeros((nh, nw, 4))
    for y in range(nh):
        sy0 = int(y * h / nh); sy1 = max(sy0 + 1, int((y + 1) * h / nh))
        for x in range(nw):
            sx0 = int(x * w / nw); sx1 = max(sx0 + 1, int((x + 1) * w / nw))
            block = a[sy0:sy1, sx0:sx1]
            al = block[:, :, 3]
            if al.sum() < 1:
                continue
            wgt = al / 255.0
            out[y, x, :3] = (block[:, :, :3] * wgt[:, :, None]).sum(axis=(0, 1)) / wgt.sum()
            out[y, x, 3] = al.mean()
    return out


if __name__ == '__main__':
    src = Image.open('tools/art/xian/_run_q.png').convert('RGBA')
    # 6 角色边界
    CHARS = [
        (43, 573, 253, 1254), (604, 1114, 311, 1248), (1143, 1596, 227, 1250),
        (1613, 2092, 78, 1169), (2077, 2567, 207, 1225), (2577, 3054, 207, 1248),
    ]
    GROUND_Y = 1250
    REF_H = 1000
    scale = TH / REF_H
    s = 16
    W = len(CHARS) * (12 * s + 6)
    row = Image.new('RGBA', (W, 15 * s), (90, 82, 64, 255))
    from PIL import ImageDraw
    d = ImageDraw.Draw(row)
    for i, (x0, x1, y0, y1) in enumerate(CHARS):
        sub = src.crop((x0, y0, x1 + 1, y1 + 1))
        rgb = np.array(sub.convert('RGB'))
        a = np.array(sub)
        a[is_bg(rgb), 3] = 0
        sub = Image.fromarray(a)
        sub = strip_white_border(sub)
        w, h = sub.size
        nw = max(1, round(w * scale)); nh = max(1, round(h * scale))
        ba = block_avg(sub, nw, nh)
        cell = Image.new('RGBA', (TW, TH), (0, 0, 0, 0))
        carr = np.array(cell)
        paste_y = TH - round((GROUND_Y - y1) * scale) - nh
        paste_x = (TW - nw) // 2
        small = Image.fromarray(np.clip(ba, 0, 255).astype(np.uint8))
        cell.paste(small, (paste_x, paste_y), small)
        z = cell.resize((12 * s, 15 * s), Image.NEAREST)
        bx = i * (12 * s + 6)
        row.paste(z, (bx, 0), z)
        for gx in range(13):
            d.line([(bx + gx * s, 0), (bx + gx * s, 15 * s)], fill=(200, 80, 80, 70))
        for gy in range(16):
            d.line([(bx, gy * s), (bx + 12 * s, gy * s)], fill=(200, 80, 80, 70))
    row.save('tools/art/xian/_run_base.png')
    print('saved')
