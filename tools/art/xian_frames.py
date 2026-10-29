#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修仙者 12x15 像素帧（idle/run/attack），基于已确认的设计稿。

帧表（见 HeroSprite.java / CharSprite.java）：
  0,1 idle ; 2..7 run ; 8..12 die(保留原版骷髅) ; 13..15 attack/zap ;
  16,17 operate ; 18 fly ; 19,20 read（本阶段暂保留原版）。
本模块只定义本阶段要替换的 idle/run/attack 帧。
"""
from PIL import Image

# 材质调色板
PAL = {
    'K': (28, 26, 30),     # 黑：发髻/头发/眉/眼/腰带/靴
    'p': (176, 128, 72),   # 木簪
    'f': (244, 206, 178),  # 脸
    'n': (232, 184, 150),  # 手（略深肤色）
    'C': (86, 150, 148),   # 青袍主色
    'd': (60, 118, 118),   # 青袍阴影
    'l': (128, 178, 174),  # 青袍亮
    'w': (240, 240, 232),  # 白中衣/袖口/衬里
    'g': (212, 180, 92),   # 剑格（金）
    'S': (200, 206, 214),  # 剑刃
    'D': (120, 128, 140),  # 剑刃暗
}

# ---- idle 帧0：正面站立，双手自然垂 ----
IDLE0 = [
    ".....KK.....",
    "..ppKKKKpp..",
    "...KKKKKK...",
    "..KffffffK..",
    "...KK..KK...",
    "..KfKffKfK..",
    "..KffffffK..",
    "...wffffw...",
    "..wCffffCw..",
    "..CCwffwCC..",
    "..CC.ww.CC..",
    "..KKCCCCKK..",
    ".nCCCCCCn...",
    "..wCCCCCCw..",
    "..ss....ss..",
]
# idle 帧1：呼吸（与帧0相同，循环无跳变）
IDLE1 = [r for r in IDLE0]

# ---- run 帧2：右腿前抬、右臂前摆 ----
RUN2 = [
    ".....KK.....",
    "..ppKKKKpp..",
    "...KKKKKK...",
    "..KffffffK..",
    "...KK..KK...",
    "..KfKffKfK..",
    "..KffffffK..",
    "...wffffw...",
    "..wCffffCn..",
    ".nCCwffwCCn.",
    ".nCC.ww.CC..",
    "..KKCCCCKK..",
    ".wCCCCCCww..",
    "..w......ws.",
    "..ss........",
]
# run 帧3：经过（双脚交错、身体略低、手臂交换）
RUN3 = [
    ".....KK.....",
    "..ppKKKKpp..",
    "...KKKKKK...",
    "..KffffffK..",
    "...KK..KK...",
    "..KfKffKfK..",
    "..KffffffK..",
    "...wffffw...",
    "..wCffffCw..",
    "..nCwffwCn..",
    "..CC.ww.CC..",
    ".KKCCCCCCKK.",
    ".wCCCCCCw...",
    ".....wwww...",
    ".....ss.....",
]
# run 帧4：腾空（整体下移1、右臂后左臂前、双脚前伸）
RUN4 = [
    "............",
    ".....KK.....",
    "..ppKKKKpp..",
    "...KKKKKK...",
    "..KffffffK..",
    "...KK..KK...",
    "..KfKffKfK..",
    "..KffffffK..",
    "...wffffw...",
    "..wCffffCw..",
    ".nCCwffwCCn.",
    "..CC.ww.CC..",
    ".KKCCCCCCKK.",
    ".w.ww..w....",
    "........ss..",
]
def _mirror(rows):
    return [r[::-1] for r in rows]
# run 帧5/6/7：帧2/3/4 的水平镜像
RUN5 = _mirror(RUN2)
RUN6 = _mirror(RUN3)
RUN7 = _mirror(RUN4)

# ---- attack 帧13：举剑（剑竖直在右侧） ----
ATK13 = [
    ".....KK...S.",
    "..ppKKKK..S.",
    "...KKKKKK.S.",
    "..KffffffKS.",
    "...KK..KK...",
    "..KfKffKfK..",
    "..KffffffK g.",
    "...wffffwK..",
    "..wCffffCn..",
    "..CCwffwCC..",
    "..CC.ww.CC..",
    "..KKCCCCKK..",
    "..CCCCCCCC..",
    "..wCCCCCCw..",
    "..ss....ss..",
]
# attack 帧14：横斩（剑横身前、弓步）
ATK14 = [
    ".....KK.....",
    "..ppKKKKpp..",
    "...KKKKKK...",
    "..KffffffK..",
    "...KK..KK...",
    "..KfKffKfK..",
    "..KffffffK..",
    "...wffffw...",
    "..wCffgSSSS.",
    "..CCnnKCC...",
    "..CC.ww.CC..",
    ".KKCCCCCCKK.",
    ".wCCCCCCw...",
    "..w.....ww..",
    "..ss....ss..",
]
# attack 帧15：恢复（=idle）
ATK15 = [r for r in IDLE0]

# 本阶段要替换的帧
FRAMES = {
    0: IDLE0, 1: IDLE1,
    2: RUN2, 3: RUN3, 4: RUN4, 5: RUN5, 6: RUN6, 7: RUN7,
    13: ATK13, 14: ATK14, 15: ATK15,
}


def render(rows):
    out = Image.new('RGBA', (12, 15), (0, 0, 0, 0))
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch in PAL:
                out.putpixel((x, y), PAL[ch] + (255,))
    return out


if __name__ == '__main__':
    im = render(IDLE0)
    big = im.resize((12 * 16, 15 * 16), Image.NEAREST)
    from PIL import ImageDraw
    d = ImageDraw.Draw(big)
    for x in range(13):
        d.line([(x * 16, 0), (x * 16, 15 * 16)], fill=(200, 80, 80, 120), width=1)
    for y in range(16):
        d.line([(0, y * 16), (12 * 16, y * 16)], fill=(200, 80, 80, 120), width=1)
    big.save('tools/art/xian/_idle0_preview.png')
    print('saved')
