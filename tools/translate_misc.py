#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate ResultDescriptions, Journal, Challenges."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PD = os.path.join(ROOT, "src", "com", "watabou", "pixeldungeon")

T = {
    "ResultDescriptions.java": {
        "Killed by %s on level %d": "在第%d层被%s击杀",
        "Killed by the %s on level %d": "在第%d层被%s击杀",
        "Killed by your own %s on level %d": "在第%d层被自己的%s击杀",
        "Killed by an explosion of a bomb on level %d": "在第%d层被炸弹爆炸击杀",
        "Killed by discharge of %s on level %d": "在第%d层被%s的放电击杀",
        "Burned to death on level %d": "在第%d层被烧死",
        "Starved to death on level %d": "在第%d层饿死",
        "Died from poison on level %d": "在第%d层中毒而死",
        "Died from toxic gas on level %d": "在第%d层死于毒气",
        "Bled to death on level %d": "在第%d层流血而死",
        "Killed by a caustic ooze on level %d": "在第%d层被腐蚀性软泥击杀",
        "Fell to death on level %d": "在第%d层坠落而死",
        "Obtained the Amulet of Yendor": "获得延多护符",
    },
    "Journal.java": {
        "Well of Health": "生命之井",
        "Well of Awareness": "感知之井",
        "Well of Transmutation": "嬗变之井",
        "Sacrificial chamber": "献祭室",
        "Alchemy pot": "炼金釜",
        "Animated statue": "活化雕像",
        "Sad ghost": "悲伤幽魂",
        "Old wandmaker": "老法杖匠",
        "Troll blacksmith": "巨魔铁匠",
        "Ambitious imp": "野心小恶魔",
    },
    "Challenges.java": {
        "On diet": "节食",
        "Faith is my armor": "信念即护甲",
        "Barren land": "贫瘠之地",
        "Swarm intelligence": "群体智慧",
        "Into darkness": "深入黑暗",
        "Forbidden runes": "禁忌符文",
    },
}


def main():
    for f, mapping in T.items():
        path = os.path.join(PD, f)
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()
        for k, v in mapping.items():
            content = content.replace('"%s"' % k, '"%s"' % v)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
    print("misc files translated")


if __name__ == "__main__":
    sys.exit(main())
