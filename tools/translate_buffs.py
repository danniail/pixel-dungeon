#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate buff status names and messages by exact literal replacement."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "src", "com", "watabou", "pixeldungeon", "actors", "buffs")

T = {
    # toString status names
    "Amok": "狂乱",
    "Barkskin": "树皮护甲",
    "Bleeding": "流血",
    "Blinded": "失明",
    "Burning": "燃烧",
    "Charmed": "被魅惑",
    "Combo": "连击",
    "Crippled": "残废",
    "Frozen": "冰冻",
    "Fury": "狂怒",
    "Immune to gases": "气体免疫",
    "Hungry": "饥饿",
    "Starving": "极度饥饿",
    "Invisible": "隐形",
    "Levitating": "漂浮",
    "Illuminated": "照明",
    "Mind vision": "心灵视界",
    "Caustic ooze": "腐蚀性软泥",
    "Paralysed": "麻痹",
    "Poisoned": "中毒",
    "Blinded with rage": "怒不可遏",
    "Rooted": "被缠绕",
    "Shadowmelded": "暗影潜行",
    "Slowed": "减速",
    "Zeroed in": "锁定",
    "Haste": "加速",
    "Terror": "恐惧",
    "Vertigo": "眩晕",
    "Weakened": "虚弱",
    # messages
    "You bled to death...": "你流血而死……",
    "%s burns up!": "%s燃尽了！",
    "You burned to death...": "你被烧死了……",
    "%d hit combo!": "%d连击！",
    "You are hungry.": "你饿了。",
    "You are starving!": "你快饿死了！",
    "You starved to death...": "你饿死了……",
    "%s killed you...": "%s杀死了你……",
    "You died from poison...": "你中毒而死……",
}


def main():
    files = 0
    for f in sorted(os.listdir(BASE)):
        if not f.endswith(".java"):
            continue
        path = os.path.join(BASE, f)
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()
        original = content
        for k, v in T.items():
            content = content.replace('"%s"' % k, '"%s"' % v)
        if content != original:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
            files += 1
    print("buff files updated: %d" % files)


if __name__ == "__main__":
    sys.exit(main())
