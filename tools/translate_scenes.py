#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate scenes by exact literal replacement."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "src", "com", "watabou", "pixeldungeon", "scenes")

T = {
    # AboutScene
    "Code & graphics: Watabou\\n": "代码与美术：Watabou\\n",
    "Music: Cube_Code\\n\\n": "音乐：Cube_Code\\n\\n",
    "This game is inspired by Brian Walker's Brogue. ":
        "本游戏灵感来自 Brian Walker 的《Brogue》。",
    "Try it on Windows, Mac OS or Linux - it's awesome! ;)\\n\\n":
        "可以在 Windows、Mac OS 或 Linux 上试试，非常棒！;)\\n\\n",
    "Please visit official website for additional info:":
        "请访问官方网站了解更多信息：",
    # AmuletScene
    "Let's call it a day": "今天就到此为止",
    "I'm not done yet": "我还没结束",
    "You finally hold it in your hands, the Amulet of Yendor. Using its power ":
        "你终于把延多护符握在手中。借助它的力量，",
    "you can take over the world or bring peace and prosperity to people or whatever. ":
        "你可以统治世界，或为人们带来和平与繁荣，等等。",
    "Anyway, your life will change forever and this game will end here. ":
        "无论如何，你的人生将永远改变，游戏也将在此结束。",
    "Or you can stay a mere mortal a little longer.":
        "或者，你可以再多做一会儿凡人。",
    # BadgesScene
    "Your Badges": "你的徽章",
    # GameScene
    "Welcome to the level %d of Pixel Dungeon!":
        "欢迎来到像素地牢第%d层！",
    "Welcome back to the level %d of Pixel Dungeon!":
        "欢迎回到像素地牢第%d层！",
    "Be cautious, since the dungeon is even more dangerous at night!":
        "小心，夜晚的地牢更加危险！",
    "Your steps echo across the dungeon.":
        "你的脚步声在地牢中回荡。",
    "You hear the water splashing around you.":
        "你听见周围水花飞溅。",
    "The smell of vegetation is thick in the air.":
        "空气中弥漫着浓重的草木气息。",
    "The atmosphere hints that this floor hides many secrets.":
        "气氛暗示这一层藏着许多秘密。",
    # InterlevelScene
    "File not found. For some reason.": "文件未找到，原因不明。",
    "Something went wrong...": "出了点问题……",
    # IntroScene
    "Many heroes of all kinds ventured into the Dungeon before you. Some of them have returned with treasures and magical ":
        "在你之前，形形色色的英雄都曾踏入地牢。有些人带着宝藏和魔法",
    "artifacts, most have never been heard of since. But none have succeeded in retrieving the Amulet of Yendor, ":
        "神器归来，大多数人从此杳无音信。但没有人成功取回延多护符，",
    "which is told to be hidden in the depths of the Dungeon.\\n\\n":
        "传说它藏在地牢的最深处。\\n\\n",
    "You consider yourself ready for the challenge, but most importantly, you feel that fortune smiles on you. ":
        "你认为自己已准备好迎接挑战，最重要的是，你感到幸运女神在向你微笑。",
    "It's time to start your own adventure!":
        "是时候开始你自己的冒险了！",
    # RankingsScene
    "Top Rankings": "排行榜",
    "Games played: ": "游戏场次：",
    "No games have been played yet.": "还没有进行过游戏。",
    "No additional information": "无更多信息",
    # SurfaceScene
    "Game Over": "游戏结束",
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
    print("scene files updated: %d" % files)


if __name__ == "__main__":
    sys.exit(main())
