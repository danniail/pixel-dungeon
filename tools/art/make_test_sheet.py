#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""装配 24x30 测试 sprite sheet（504x240，8 tier 行）。"""
from PIL import Image
import numpy as np
import sys
sys.path.insert(0, 'tools/art')
from clean_base import is_bg, strip_white_border, block_avg

FW, FH = 24, 30
COLS, ROWS = 21, 8
SHEET_W, SHEET_H = COLS * FW, ROWS * FH  # 504 x 240


def get_frames(img_path, xsegs):
    src = Image.open(img_path).convert('RGBA')
    arr = np.array(src.convert('RGB'))
    r, g, b = arr[:, :, 0].astype(int), arr[:, :, 1].astype(int), arr[:, :, 2].astype(int)
    bg = (r > 205) & (g > 195) & (b > 175) & (np.abs(r - g) < 38) & (np.abs(g - b) < 48)
    out = []
    for x0, x1 in xsegs:
        fg = ~bg[:, x0:x1]
        rows = np.where(fg.sum(axis=1) > 1)[0]
        y0, y1 = rows.min(), rows.max()
        sub = src.crop((x0, y0, x1 + 1, y1 + 1))
        a = np.array(sub)
        rgb = np.array(sub.convert('RGB'))
        a[is_bg(rgb), 3] = 0
        sub = strip_white_border(Image.fromarray(a))
        ba = block_avg(sub, FW, FH)
        im = Image.fromarray(np.clip(ba, 0, 255).astype(np.uint8))
        out.append(im)
    return out


run = get_frames('tools/art/xian/_run_q.png',
                 [(43, 573), (604, 1114), (1143, 1596), (1613, 2092), (2077, 2567), (2577, 3054)])
atk = get_frames('tools/art/xian/_atk_q.png', [(117, 840), (973, 1940), (2099, 2684)])

idle = run[0]  # 临时用接触位当 idle（仅测试大小）

sheet = Image.new('RGBA', (SHEET_W, SHEET_H), (0, 0, 0, 0))


def place(frame_idx, im):
    x = frame_idx * FW
    sheet.paste(im, (x, 0), im)


# tier0 行（其余 tier 行复制 tier0，便于看换甲）
for tier in range(ROWS):
    y = tier * FH
    # idle 0,1
    sheet.paste(idle, (0 * FW, y), idle)
    sheet.paste(idle, (1 * FW, y), idle)
    # run 2-7
    for i in range(6):
        sheet.paste(run[i], ((2 + i) * FW, y), run[i])
    # die 8-12 临时用 idle
    for i in range(8, 13):
        sheet.paste(idle, (i * FW, y), idle)
    # attack 13-15
    for i in range(3):
        sheet.paste(atk[i], ((13 + i) * FW, y), atk[i])
    # 16-20 用 idle
    for i in range(16, 21):
        sheet.paste(idle, (i * FW, y), idle)

sheet.save('tools/art/xian/_test_sheet.png')
print('saved', sheet.size)
