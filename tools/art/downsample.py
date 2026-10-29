#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把高分辨率 AI 动作图降采样到 12x15，并量化到游戏调色板。"""
from PIL import Image
import numpy as np
import sys
sys.path.insert(0, 'tools/art')
from xian_frames import PAL

# 检测到的角色边界（x0,x1）
RUN_SEGS = [(50, 569), (616, 1117), (1153, 1611), (1655, 2152), (2153, 2663), (2680, 3171)]
ATK_SEGS = [(112, 769), (940, 1828), (2031, 2690)]

TARGET_H = 15
TARGET_W = 12


def is_bg(a):
    r, g, b = a[:, :, 0].astype(int), a[:, :, 1].astype(int), a[:, :, 2].astype(int)
    return (r > 210) & (g > 200) & (b > 180) & (np.abs(r - g) < 35) & (np.abs(g - b) < 45)


def crop_char(im, x0, x1):
    region = np.array(im.convert('RGB'))[:, x0:x1]
    fg = ~is_bg(region)
    # 角色精确边界
    cols = np.where(fg.sum(axis=0) > 1)[0]
    rows = np.where(fg.sum(axis=1) > 1)[0]
    y0, y1 = rows.min(), rows.max()
    cx0, cx1 = cols.min(), cols.max()
    sub = im.convert('RGBA').crop((x0 + cx0, y0, x0 + cx1 + 1, y1 + 1))
    # 去背景 -> 透明
    arr = np.array(sub)
    bgm = is_bg(np.array(sub.convert('RGB')))
    arr[:, :, 3] = np.where(bgm, 0, 255)
    return Image.fromarray(arr)


def to_target(char_im, ref_h=None):
    """缩放到 12x15：按统一高度，脚对齐 y14，水平居中。"""
    w, h = char_im.size
    scale = TARGET_H / h
    new_w = max(1, round(w * scale))
    new_w = min(new_w, TARGET_W)
    small = char_im.resize((new_w, TARGET_H), Image.LANCZOS)
    canvas = Image.new('RGBA', (TARGET_W, TARGET_H), (0, 0, 0, 0))
    ox = (TARGET_W - new_w) // 2
    canvas.paste(small, (ox, 0), small)
    return canvas


def quantize(im):
    """量化到 PAL 调色板，保留透明。"""
    arr = np.array(im).astype(int)
    out = np.zeros((TARGET_H, TARGET_W, 4), dtype=np.uint8)
    keys = list(PAL.keys())
    pal = np.array([PAL[k] for k in keys])
    for y in range(TARGET_H):
        for x in range(TARGET_W):
            r, g, b, a = arr[y, x]
            if a < 110:
                continue
            d = ((pal[:, 0] - r) ** 2 + (pal[:, 1] - g) ** 2 + (pal[:, 2] - b) ** 2)
            k = keys[d.argmin()]
            out[y, x] = np.array(PAL[k] + (255,))
    return Image.fromarray(out)


def build(name, segs):
    im = Image.open('tools/art/xian/' + name).convert('RGB')
    frames = []
    for i, (x0, x1) in enumerate(segs):
        c = crop_char(im, x0, x1)
        t = to_target(c)
        q = quantize(t)
        frames.append(q)
    return frames


if __name__ == '__main__':
    run = build('_run_hi.png', RUN_SEGS)
    atk = build('_atk_hi.png', ATK_SEGS)
    # 放大预览
    s = 16
    rw = len(run) * (12 * s + 6)
    row = Image.new('RGBA', (rw, 15 * s), (90, 82, 64, 255))
    for i, f in enumerate(run):
        row.paste(f.resize((12 * s, 15 * s), Image.NEAREST), (i * (12 * s + 6), 0),
                  f.resize((12 * s, 15 * s), Image.NEAREST))
    row.save('tools/art/xian/_run_ds.png')
    aw = len(atk) * (12 * s + 6)
    row2 = Image.new('RGBA', (aw, 15 * s), (90, 82, 64, 255))
    for i, f in enumerate(atk):
        row2.paste(f.resize((12 * s, 15 * s), Image.NEAREST), (i * (12 * s + 6), 0),
                   f.resize((12 * s, 15 * s), Image.NEAREST))
    row2.save('tools/art/xian/_atk_ds.png')
    print('saved')
