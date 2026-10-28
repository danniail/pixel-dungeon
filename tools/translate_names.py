#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch-translate item names (the `name = "..."` assignments) for the
Simplified Chinese build.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")

NAMES = {
    # Potions
    "Potion of Healing": "治疗药水",
    "Potion of Experience": "经验药水",
    "Potion of Frost": "冰霜药水",
    "Potion of Invisibility": "隐形药水",
    "Potion of Levitation": "漂浮药水",
    "Potion of Liquid Flame": "液态火焰药水",
    "Potion of Might": "威能药水",
    "Potion of Mind Vision": "心灵视界药水",
    "Potion of Paralytic Gas": "麻痹气体药水",
    "Potion of Purification": "净化药水",
    "Potion of Strength": "力量药水",
    "Potion of Toxic Gas": "毒气药水",
    # Scrolls
    "Scroll of Challenge": "挑战卷轴",
    "Scroll of Enchantment": "附魔卷轴",
    "Scroll of Identify": "鉴定卷轴",
    "Scroll of Lullaby": "摇篮曲卷轴",
    "Scroll of Magic Mapping": "魔法地图卷轴",
    "Scroll of Mirror Image": "镜像卷轴",
    "Scroll of Psionic Blast": "灵能冲击卷轴",
    "Scroll of Recharging": "充能卷轴",
    "Scroll of Remove Curse": "驱魔卷轴",
    "Scroll of Teleportation": "传送卷轴",
    "Scroll of Terror": "恐惧卷轴",
    "Scroll of Upgrade": "升级卷轴",
    "Scroll of Wipe Out": "湮灭卷轴",
    # Rings
    "Ring of Accuracy": "精准之戒",
    "Ring of Detection": "侦测之戒",
    "Ring of Elements": "元素之戒",
    "Ring of Evasion": "闪避之戒",
    "Ring of Haggler": "议价之戒",
    "Ring of Haste": "急速之戒",
    "Ring of Herbalism": "草药之戒",
    "Ring of Mending": "修复之戒",
    "Ring of Power": "能量之戒",
    "Ring of Satiety": "饱食之戒",
    "Ring of Shadows": "暗影之戒",
    "Ring of Thorns": "荆棘之戒",
    # Wands
    "Wand of Amok": "狂乱法杖",
    "Wand of Avalanche": "雪崩法杖",
    "Wand of Blink": "闪烁法杖",
    "Wand of Disintegration": "分解法杖",
    "Wand of Firebolt": "火焰法杖",
    "Wand of Flock": "羊群法杖",
    "Wand of Lightning": "闪电法杖",
    "Wand of Magic Missile": "魔法飞弹法杖",
    "Wand of Poison": "剧毒法杖",
    "Wand of Reach": "延伸法杖",
    "Wand of Regrowth": "再生法杖",
    "Wand of Slowness": "减速法杖",
    "Wand of Teleportation": "传送法杖",
    "sheep": "绵羊",
    # Armor
    "cloth armor": "布甲",
    "leather armor": "皮甲",
    "mail armor": "锁子甲",
    "scale armor": "鳞甲",
    "plate armor": "板甲",
    "mage robe": "法师长袍",
    "warrior suit of armor": "战士铠甲",
    "rogue garb": "盗贼装束",
    "huntress cloak": "猎手斗篷",
    # Melee
    "dagger": "匕首",
    "knuckleduster": "指虎",
    "short sword": "短剑",
    "sword": "铁剑",
    "longsword": "长剑",
    "mace": "钉头锤",
    "quarterstaff": "长棍",
    "spear": "长矛",
    "battle axe": "战斧",
    "war hammer": "战锤",
    "glaive": "关刀",
    # Missiles
    "dart": "飞镖",
    "curare dart": "箭毒飞镖",
    "incendiary dart": "燃烧飞镖",
    "shuriken": "手里剑",
    "javelin": "标枪",
    "tomahawk": "投掷斧",
    "boomerang": "回旋镖",
    # Food
    "ration of food": "口粮",
    "overpriced food ration": "高价口粮",
    "mystery meat": "神秘肉",
    "chargrilled meat": "烤肉",
    "frozen carpaccio": "冻生肉片",
    "pasty": "馅饼",
    # Keys
    "golden key": "金钥匙",
    "iron key": "铁钥匙",
    "skeleton key": "万能钥匙",
    # Bags
    "key ring": "钥匙环",
    "scroll holder": "卷轴筒",
    "seed pouch": "种子袋",
    "wand holster": "法杖套",
    # Misc
    "dewdrop": "露珠",
    "dew vial": "露珠瓶",
    "bomb": "炸弹",
    "honeypot": "蜜罐",
    "torch": "火把",
    "gold": "金币",
    "armor kit": "护甲套件",
    "weightstone": "磨刀石",
    "Amulet of Yendor": "延多护符",
    "Ankh": "安卡",
    "lloyd's beacon": "劳埃德信标",
    "phantom fish": "幻影鱼",
    "dried rose": "干枯玫瑰",
    "dwarf token": "矮人信物",
    "pickaxe": "镐",
    "dark gold ore": "暗金矿石",
    "giant rat skull": "巨鼠头骨",
    "corpse dust": "尸尘",
}


def main():
    changed = 0
    for dirpath, _dirs, files in os.walk(SRC):
        for name in files:
            if not name.endswith(".java"):
                continue
            path = os.path.join(dirpath, name)
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            original = content
            for eng, cn in NAMES.items():
                content = content.replace('name = "%s"' % eng, 'name = "%s"' % cn)
            if content != original:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(content)
                changed += 1
    print("files updated: %d" % changed)


if __name__ == "__main__":
    sys.exit(main())
