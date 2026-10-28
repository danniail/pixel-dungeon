#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate remaining UI labels, terrain names, and residual fragments.
Only exact, case-sensitive UI literals are touched; save keys are lowercase
and therefore unaffected."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PD = os.path.join(ROOT, "src", "com", "watabou", "pixeldungeon")

# Global exact replacements (literal content -> Chinese).
GLOBAL = {
    # window tabs / labels
    "Buffs": "状态",
    "Catalogus": "图鉴",
    "Experience": "经验",
    "Health": "生命",
    "Journal": "日志",
    "Stats": "属性",
    "Strength": "力量",
    "Badges": "徽章",
    "Challenges": "挑战",
    "Items": "物品",
    "Potions": "药水",
    "Scrolls": "卷轴",
    "Mastery": "精通",
    "ERROR": "错误",
    "Chest": "宝箱",
    "Tomb": "坟墓",
    # terrain names
    "Barricade": "栅栏",
    "Bookshelf": "书架",
    "Chasm": "深渊",
    "Embers": "余烬",
    "Floor": "地板",
    "Grass": "草地",
    "Pedestal": "基座",
    "Sign": "告示牌",
    "Statue": "雕像",
    "Wall": "墙壁",
    "Water": "水",
    "Well": "井",
    # halls decoration names
    "Emberfungi": "余烬真菌",
    "Embermoss": "余烬苔藓",
    "Pillar": "柱子",
    # journal feature
    "Garden": "花园",
    # challenge name
    "Pharmacophobia": "药水恐惧",
    # residual fragments
    "The scroll utters a soothing melody and the ":
        "卷轴奏出舒缓的旋律，",
    "The scroll emits a brilliant flash of red light and the ":
        "卷轴发出一道耀眼的红光，",
    "your %s glows in the dark": "你的%s在黑暗中发光",
}

# Special: " teleported " (with surrounding spaces) -> " 传送了 "
SPECIAL = [(" teleported ", " 传送了 ")]


def main():
    files = 0
    for root, _, fl in os.walk(PD):
        for f in fl:
            if not f.endswith(".java"):
                continue
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            original = content
            for k, v in GLOBAL.items():
                content = content.replace('"%s"' % k, '"%s"' % v)
            for old, new in SPECIAL:
                content = content.replace('"%s"' % old, '"%s"' % new)
            if content != original:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(content)
                files += 1
    print("ui files updated: %d" % files)


if __name__ == "__main__":
    sys.exit(main())
