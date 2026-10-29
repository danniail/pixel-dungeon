#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把修仙者全部动作转译到 24x30 并输出预览（统一缩放、统一基线）。"""
from PIL import Image
import numpy as np
import sys
sys.path.insert(0, 'tools/art')
from clean_base import is_bg, strip_white_border, block_avg
from scipy import ndimage

FW, FH = 24, 30
X = 'tools/art/xian/'

# 各动作的角色横向分段（x0,x1）
SEGS = {
    'idle':    [(546, 1112), (1438, 2002)],
    'run':     [(43, 573), (604, 1114), (1143, 1596), (1613, 2092), (2077, 2567), (2577, 3054)],
    'die':     [(30, 700), (700, 1340), (1340, 1960), (1960, 2560), (2560, 3170)],
    'attack':  [(117, 840), (973, 1940), (2099, 2684)],
    'operate': [(322, 1032), (1302, 2406)],
    'fly':     [(60, 1900)],
    'read':    [(448, 1102), (1544, 2236)],
}
FILES = {
    'idle': '_idle_q.png', 'run': '_run_q.png', 'die': '_die2_q.png',
    'attack': '_atk_q.png', 'operate': '_operate_q.png',
    'fly': '_fly_q.png', 'read': '_read_q.png',
}


def remove_bg_flood(im):
    """只移除与图像边缘连通的外部背景，保留角色内部的亮肤色（不被误判）。"""
    a = np.array(im.convert('RGBA'))
    h, w = a.shape[:2]
    bg = is_bg(a[:, :, :3])
    lbl, n = ndimage.label(bg)
    edge = np.zeros(n + 1, bool)
    edge[lbl[0, :]] = True
    edge[lbl[-1, :]] = True
    edge[lbl[:, 0]] = True
    edge[lbl[:, -1]] = True
    edge[0] = False
    outer = np.isin(lbl, np.where(edge)[0])
    a[outer, 3] = 0
    return Image.fromarray(a)


def enhance_eyes(im, dil=1):
    """加深/放大面部眼睛（连通块），让块平均后眼睛清晰；不向下膨胀以免和鼻子连。"""
    A = np.array(im).astype(np.uint8)
    h, w = A.shape[:2]
    dark = (A[:, :, :3].sum(axis=2) < 170) & (A[:, :, 3] > 0)
    lbl, n = ndimage.label(dark)
    eye = np.zeros_like(dark)
    for i in range(1, n + 1):
        ys, xs = np.where(lbl == i)
        area = len(ys)
        if (0.10 * h < ys.min() < 0.32 * h and 0.10 * h < ys.max() < 0.34 * h
                and 200 < area < 0.02 * h * w and (xs.max() - xs.min()) < 0.18 * w):
            eye |= (lbl == i)
    eye = ndimage.binary_fill_holes(eye)
    if dil:
        struct = np.array([[0, 1, 0], [1, 1, 1], [0, 0, 0]])
        eye = ndimage.binary_dilation(eye, structure=struct, iterations=dil)
    out = A.copy()
    add = eye & (A[:, :, 3] > 0) & (A[:, :, :3].sum(axis=2) > 100)
    out[add, :3] = 22
    out[add, 3] = 255
    return Image.fromarray(out)


def extract(file, x0, x1, eyes=True):
    src = Image.open(X + file).convert('RGBA')
    sub = remove_bg_flood(src.crop((x0, 0, x1 + 1, src.size[1])))
    sub = strip_white_border(sub, iters=14)
    aa = np.array(sub)
    ys, xs = np.where(aa[:, :, 3] > 0)
    sub = sub.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    if eyes:
        sub = enhance_eyes(sub)
    return sub


# 每个动作图的"站立等效身体高度"（原图像素，统一归一化到 27）
TARGET_H = 27
REF_H = {
    'idle': 1551,    # 站立
    'run': 1100,     # 奔跑接触位略低，估算站立等效
    'die': 1560,     # 盘腿坐化的站立等效
    'attack': 1300,  # 收剑帧
    'operate': 1510,
    'fly': 1700,
    'read': 1490,
}
SCALES = {a: TARGET_H / REF_H[a] for a in REF_H}


def to_frame(act, im):
    """块平均直接填满 24x30（之前通过的品质方案，不做调色板量化）。"""
    ba = block_avg(im, FW, FH)
    return Image.fromarray(np.clip(ba, 0, 255).astype(np.uint8))


FRAMES = {}
for act, segs in SEGS.items():
    do_eyes = act != 'die'  # 坐化骷髅无眼睛，跳过增强
    FRAMES[act] = [to_frame(act, extract(FILES[act], *s, eyes=do_eyes)) for s in segs]
    print(act, len(FRAMES[act]))

# 输出全部帧横向预览（按游戏帧顺序，共21帧）
order = [('idle', 0), ('idle', 1), ('run', 0), ('run', 1), ('run', 2), ('run', 3), ('run', 4), ('run', 5),
         ('die', 0), ('die', 1), ('die', 2), ('die', 3), ('die', 4),
         ('attack', 0), ('attack', 1), ('attack', 2),
         ('operate', 0), ('operate', 1), ('fly', 0), ('read', 0), ('read', 1)]
preview = Image.new('RGBA', (len(order) * FW, FH), (30, 30, 36, 255))
for i, (a, k) in enumerate(order):
    preview.paste(FRAMES[a][k], (i * FW, 0), FRAMES[a][k])
preview = preview.resize((len(order) * FW * 5, FH * 5), Image.NEAREST)
preview.save('/tmp/xian_full_preview.png')
print('preview saved', preview.size)

# 装配完整 504x240 sheet（8 tier 行；本阶段 8 行内容相同，护甲颜色后续再分）
COLS, ROWS = 21, 8
sheet = Image.new('RGBA', (COLS * FW, ROWS * FH), (0, 0, 0, 0))


def place_row(tier):
    y = tier * FH
    # 0,1 idle
    for k in range(2):
        sheet.paste(FRAMES['idle'][k], (k * FW, y), FRAMES['idle'][k])
    # 2-7 run
    for k in range(6):
        sheet.paste(FRAMES['run'][k], ((2 + k) * FW, y), FRAMES['run'][k])
    # 8-12 die
    for k in range(5):
        sheet.paste(FRAMES['die'][k], ((8 + k) * FW, y), FRAMES['die'][k])
    # 13-15 attack
    for k in range(3):
        sheet.paste(FRAMES['attack'][k], ((13 + k) * FW, y), FRAMES['attack'][k])
    # 16,17 operate
    for k in range(2):
        sheet.paste(FRAMES['operate'][k], ((16 + k) * FW, y), FRAMES['operate'][k])
    # 18 fly
    sheet.paste(FRAMES['fly'][0], (18 * FW, y), FRAMES['fly'][0])
    # 19,20 read
    for k in range(2):
        sheet.paste(FRAMES['read'][k], ((19 + k) * FW, y), FRAMES['read'][k])


for tier in range(ROWS):
    place_row(tier)
sheet.save('assets/mage.png')
print('sheet saved', sheet.size)
