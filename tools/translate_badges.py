#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate Badges names and messages."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "src", "com", "watabou", "pixeldungeon", "Badges.java")

T = {
    "10 enemies slain": "击杀10个敌人",
    "50 enemies slain": "击杀50个敌人",
    "150 enemies slain": "击杀150个敌人",
    "250 enemies slain": "击杀250个敌人",
    "100 gold collected": "收集100金币",
    "500 gold collected": "收集500金币",
    "2500 gold collected": "收集2500金币",
    "7500 gold collected": "收集7500金币",
    "Level 6 reached": "达到6级",
    "Level 12 reached": "达到12级",
    "Level 18 reached": "达到18级",
    "Level 24 reached": "达到24级",
    "All potions identified": "鉴定全部药水",
    "All scrolls identified": "鉴定全部卷轴",
    "All rings identified": "鉴定全部戒指",
    "All wands identified": "鉴定全部法杖",
    "All potions, scrolls, rings & wands identified":
        "鉴定全部药水、卷轴、戒指和法杖",
    "All bags bought": "买下全部背包",
    "Death from fire": "死于火焰",
    "Death from poison": "死于剧毒",
    "Death from toxic gas": "死于毒气",
    "Death from hunger": "死于饥饿",
    "Death from an enchantment": "死于附魔",
    "Death from falling down": "坠落而死",
    "Death from fire, poison, toxic gas & hunger":
        "死于火焰、剧毒、毒气和饥饿",
    "1st boss slain": "击杀第1个BOSS",
    "2nd boss slain": "击杀第2个BOSS",
    "3rd boss slain": "击杀第3个BOSS",
    "4th boss slain": "击杀第4个BOSS",
    "1st boss slain by Warrior, Mage, Rogue & Huntress":
        "战士、法师、盗贼和女猎手各击杀第1个BOSS",
    "3rd boss slain by Gladiator, Berserker, Warlock, Battlemage, Freerunner, Assassin, Sniper & Warden":
        "角斗士、狂战士、战斗法师、术士、疾行者、刺客、狙击手和守望者各击杀第3个BOSS",
    "Ring of Haggler obtained": "获得议价之戒",
    "Ring of Thorns obtained": "获得荆棘之戒",
    "13 points of Strength attained": "力量达到13点",
    "15 points of Strength attained": "力量达到15点",
    "17 points of Strength attained": "力量达到17点",
    "19 points of Strength attained": "力量达到19点",
    "10 pieces of food eaten": "进食10次",
    "20 pieces of food eaten": "进食20次",
    "30 pieces of food eaten": "进食30次",
    "40 pieces of food eaten": "进食40次",
    "Item of level 3 acquired": "获得3级物品",
    "Item of level 6 acquired": "获得6级物品",
    "Item of level 9 acquired": "获得9级物品",
    "Item of level 12 acquired": "获得12级物品",
    "All rare monsters slain": "击杀全部稀有怪物",
    "Amulet of Yendor obtained": "获得延多护符",
    "Amulet of Yendor obtained by Warrior, Mage, Rogue & Huntress":
        "战士、法师、盗贼和女猎手各获得延多护符",
    "7-hit combo": "7连击",
    "3 potions cooked": "酿造3瓶药水",
    "6 potions cooked": "酿造6瓶药水",
    "9 potions cooked": "酿造9瓶药水",
    "12 potions cooked": "酿造12瓶药水",
    "Level completed without killing any monsters": "不杀任何怪物通关",
    "Monster killed by a Grim weapon": "用死神之镰击杀怪物",
    "6 piranhas killed": "击杀6条食人鱼",
    "15 monsters killed at nighttime": "夜间击杀15个怪物",
    "10 games played": "进行10场游戏",
    "100 games played": "进行100场游戏",
    "500 games played": "进行500场游戏",
    "2000 games played": "进行2000场游戏",
    "Happy end": "圆满结局",
    "Challenge won": "挑战胜利",
    "Thanks for your support!": "感谢你的支持！",
    "Badge endorsed: %s": "徽章已获得：%s",
    "New super badge: %s": "新超级徽章：%s",
    "New badge: %s": "新徽章：%s",
}


def main():
    with open(PATH, "r", encoding="utf-8") as fh:
        content = fh.read()
    for k, v in T.items():
        content = content.replace('"%s"' % k, '"%s"' % v)
    with open(PATH, "w", encoding="utf-8") as fh:
        fh.write(content)
    print("Badges translated")


if __name__ == "__main__":
    sys.exit(main())
