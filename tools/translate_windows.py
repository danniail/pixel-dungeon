#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate windows by exact literal replacement."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "src", "com", "watabou", "pixeldungeon", "windows")

T = {
    # WndBlacksmith
    "Ok, a deal is a deal, dat's what I can do for you: I can reforge ":
        "好，一言为定，我能为你做的是：把",
    "2 items and turn them into one of a better quality.":
        "2件物品重铸，合二为一，品质更好。",
    "Select an item to reforge": "选择要重铸的物品",
    "Reforge them": "重铸它们",
    # WndChooseWay
    "Which way will you follow?": "你要走哪条路？",
    "I'll decide later": "我稍后再决定",
    "Do you want to respec into %s?": "你想转职为%s吗？",
    "Yes, I want to respec": "是，我要转职",
    "Maybe later": "以后再说",
    # WndGame
    "Start New Game": "开始新游戏",
    "Main Menu": "主菜单",
    "Exit Game": "退出游戏",
    "Return to Game": "返回游戏",
    # WndHero
    "Gold Collected": "收集金币",
    "Maximum Depth": "最深层数",
    # WndImp
    "Oh yes! You are my hero!\\n": "哦，太棒了！你就是我的英雄！\\n",
    "Regarding your reward, I don't have cash with me right now, but I have something better for you. ":
        "关于你的报酬，我现在身上没带钱，但我有更好的东西给你。",
    "This is my family heirloom ring: my granddad took it off a dead paladin's finger.":
        "这是我的传家戒指：我爷爷从一个死去圣骑士的手指上取下来的。",
    "Take the ring": "收下戒指",
    # WndInfoCell
    "There is nothing here.": "这里什么也没有。",
    # WndInfoItem
    "Locked chest": "上锁的箱子",
    "Crystal chest": "水晶箱",
    "Skeletal remains": "骸骨",
    "You won't know what's inside until you open it!":
        "打开之前，你不知道里面有什么！",
    " But to open it you need a golden key.":
        "但要打开它，你需要一把金钥匙。",
    "You can see %s inside, but to open the chest you need a golden key.":
        "你能看见里面的%s，但要打开箱子需要一把金钥匙。",
    "This ancient tomb may contain something useful, ":
        "这座古墓里也许有有用的东西，",
    "but its owner will most certainly object to checking.":
        "但它的主人肯定不会同意你翻找。",
    "This is all that's left from one of your predecessors. ":
        "这是你的某位前辈留下的全部东西。",
    "Maybe it's worth checking for any valuables.":
        "也许值得找找有没有值钱的东西。",
    # WndRanking
    "Unable to load additional information": "无法加载更多信息",
    "Game Duration": "游戏时长",
    "Mobs Killed": "击杀怪物",
    "Food Eaten": "进食次数",
    "Potions Cooked": "酿造药水",
    "Ankhs Used": "使用安卡",
    # WndResurrect
    "You died, but you were given another chance to win this dungeon. Will you take it?":
        "你死了，但你得到了再战地牢的机会。你要接受吗？",
    "Yes, I will fight!": "是，我要再战！",
    "No, I give up": "否，我放弃",
    # WndSadGhost
    "Ghost's weapon": "幽魂的武器",
    "Ghost's armor": "幽魂的护甲",
    "Farewell, adventurer!": "永别了，冒险者！",
    # WndSettings
    "Default Zoom": "默认缩放",
    "Scale up UI": "放大界面",
    "Immersive mode": "沉浸模式",
    "Sound FX": "音效",
    "Second quickslot": "第二快捷栏",
    "Switch to portrait": "切换到竖屏",
    "Switch to landscape": "切换到横屏",
    # WndStory
    "The Dungeon lies right beneath the City, its upper levels actually constitute the City's sewer system. ":
        "地牢就在城市正下方，它的上层实际上构成了城市的下水道系统。",
    "Being nominally a part of the City, these levels are not that dangerous. No one will call it a safe place, ":
        "名义上属于城市，这些层并不那么危险。没人会说这是个安全的地方，",
    "but at least you won't need to deal with evil magic here.":
        "但至少你不必在这里对付邪恶魔法。",
    "Many years ago an underground prison was built here for the most dangerous criminals. At the time it seemed ":
        "许多年前，这里建了一座地下监狱，关押最危险的罪犯。当时这",
    "like a very clever idea, because this place indeed was very hard to escape. But soon dark miasma started to permeate ":
        "看起来是个绝妙的主意，因为这里确实很难逃脱。但很快，黑暗的瘴气开始渗出，",
    "from below, driving prisoners and guards insane. In the end the prison was abandoned, though some convicts ":
        "让囚犯和守卫发疯。最终监狱被废弃，尽管有些囚犯",
    "were left locked up here.":
        "还被锁在这里。",
    "The caves, which stretch down under the abandoned prison, are sparcely populated. They lie too deep to be exploited ":
        "废弃监狱下方延伸的洞穴人烟稀少。它们太深，城市无法开采；",
    "by the City and they are too poor in minerals to interest the dwarves. In the past there was a trade outpost ":
        "矿物又太贫乏，矮人不感兴趣。过去，在这条商路上",
    "somewhere here on the route between these two states, but it has perished since the decline of Dwarven Metropolis. ":
        "曾有一个贸易前哨站，但自矮人城邦衰落以来，它也消亡了。",
    "Only omnipresent gnolls and subterranean animals dwell here now.":
        "如今只有无处不在的豺狼和地下动物栖息于此。",
    "Dwarven Metropolis was once the greatest of dwarven city-states. In its heyday the mechanized army of dwarves ":
        "矮人城邦曾是最伟大的矮人城邦。鼎盛时期，矮人的机械化军队",
    "has successfully repelled the invasion of the old god and his demon army. But it is said, that the returning warriors ":
        "成功击退了古神和他的恶魔大军的入侵。但据说，归来的战士",
    "have brought seeds of corruption with them, and that victory was the beginning of the end for the underground kingdom.":
        "带回了腐败的种子，那场胜利正是这个地下王国走向终结的开端。",
    "In the past these levels were the outskirts of Metropolis. After the costly victory in the war with the old god ":
        "过去这些层是城邦的郊区。在与古神的战争中付出惨重代价后，",
    "dwarves were too weakened to clear them of remaining demons. Gradually demons have tightened their grip on this place ":
        "矮人太过虚弱，无法清除残余的恶魔。恶魔逐渐收紧了对这里的控制，",
    "and now it's called Demon Halls.\\n\\n":
        "如今这里被称为恶魔大厅。\\n\\n",
    "Very few adventurers have ever descended this far...":
        "极少有冒险者能走到这么远……",
    # WndTradeItem
    "FOR SALE: %s - %dg": "出售：%s - %d金币",
    "Buy for %dg": "花%d金币购买",
    "Sell for %dg": "以%d金币卖出",
    "Sell 1 for %dg": "卖1个，得%d金币",
    "Sell all for %dg": "全部卖出，得%d金币",
    "Never mind": "算了",
    "You've sold your %s for %dg": "你以%d金币卖出了%s",
    "You've bought %s for %dg": "你以%d金币买下了%s",
    # WndWandmaker
    "Oh, I see you have succeeded! I do hope it hasn't troubled you too much. ":
        "哦，看来你成功了！希望没让你太费周折。",
    "As I promised, you can choose one of my high quality wands.":
        "正如我承诺的，你可以从我的高品质法杖中选一根。",
    "Battle wand": "战斗法杖",
    "Non-battle wand": "非战斗法杖",
    "Good luck in your quest, %s!": "祝你冒险顺利，%s！",
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
    print("window files updated: %d" % files)


if __name__ == "__main__":
    sys.exit(main())
