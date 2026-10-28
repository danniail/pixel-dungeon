#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix strings containing escaped quotes/newlines that were missed."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PD = os.path.join(ROOT, "src", "com", "watabou", "pixeldungeon")

# Each entry: (relative path, old literal INCLUDING outer quotes,
#              new literal INCLUDING outer quotes)
FIX = [
    ("actors/blobs/SacrificialFire.java",
     r'"\"Your sacrifice is worthy...\" "',
     '"“你的献祭有价值……” "'),
    ("actors/blobs/SacrificialFire.java",
     r'"\"Your sacrifice is unworthy...\" "',
     '"“你的献祭毫无价值……” "'),
    ("actors/blobs/SacrificialFire.java",
     r'"\"Your sacrifice is worthy and so you are!\" "',
     '"“你的献祭有价值，你也一样！” "'),
    ("actors/mobs/Mob.java",
     r'"%s: \"%s\" "',
     '"%s：“%s” "'),
    ("actors/mobs/Thief.java",
     r'"\n\n%s is carrying a _%s_. Stolen obviously."',
     r'"\n\n%s 带着 _%s_，显然是偷来的。"'),
    ("actors/mobs/npcs/Blacksmith.java",
     r'"What do you mean, how am I gonna pay? You greedy...\n"',
     r'"你什么意思，我怎么付钱？你这贪心的……\n"'),
    ("actors/mobs/npcs/Imp.java",
     r'"if something needs to be killed. Am I right? For a bounty, of course ;)\n"',
     r'"去杀掉该杀的东西。对吧？当然是为了赏金;)\n"'),
    ("items/LloydsBeacon.java",
     r'"\n\nThis beacon was set somewhere on the level %d of Pixel Dungeon."',
     r'"\n\n这个信标设置在像素地牢第%d层的某处。"'),
]


def main():
    n = 0
    for rel, old, new in FIX:
        path = os.path.join(PD, rel)
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()
        if old in content:
            content = content.replace(old, new)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
            n += 1
            print("fixed", rel)
        else:
            print("NOT FOUND", rel, old)
    print("total fixed: %d" % n)


if __name__ == "__main__":
    sys.exit(main())
