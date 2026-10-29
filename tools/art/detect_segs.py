#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import sys

def segments(name):
    im = Image.open('tools/art/xian/' + name).convert('RGB')
    a = np.array(im)
    r, g, b = a[:, :, 0].astype(int), a[:, :, 1].astype(int), a[:, :, 2].astype(int)
    bg = (r > 210) & (g > 200) & (b > 180) & (np.abs(r - g) < 35) & (np.abs(g - b) < 45)
    fg = ~bg
    col = fg.sum(axis=0)
    active = col > 5
    segs = []
    inS = False
    for x, v in enumerate(active):
        if v and not inS:
            start = x
            inS = True
        elif not v and inS:
            segs.append((start, x))
            inS = False
    if inS:
        segs.append((start, len(active)))
    # 合并间隔过小的段（同一角色被误分）
    merged = []
    for s in segs:
        if merged and s[0] - merged[-1][1] < 20:
            merged[-1] = (merged[-1][0], s[1])
        else:
            merged.append(list(s))
    print(name, im.size)
    for i, (x0, x1) in enumerate(merged):
        sub = fg[:, x0:x1]
        rows = np.where(sub.sum(axis=1) > 2)[0]
        print('  char', i, 'x', x0, x1, 'y', rows.min(), rows.max())
    return merged

if __name__ == '__main__':
    segments('_run_hi.png')
    segments('_atk_hi.png')
