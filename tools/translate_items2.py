#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate remaining item action buttons, messages, enchantment/glyph names."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "src", "com", "watabou", "pixeldungeon", "items")

T = {
    "You killed yourself with a bomb...": "你用炸弹把自己炸死了……",
    "you wince as your grip involuntarily tightens around your %s":
        "你不由得握紧了你的%s",
    "%+dHP": "%+d生命",
    "You can't read while blinded": "你不能在失明时阅读",
    "Tome of Remastery": "重修之书",
    "Tome of Mastery": "精通之书",
    "You have chosen the way of the %s!": "你选择了%s之路！",
    "Select a weapon to balance": "选择要调整的武器",
    "you balanced your %s to make it faster": "你调整了%s，让它更快",
    "you balanced your %s to make it more accurate":
        "你调整了%s，让它更精准",
    "How would you like to balance your %s?": "你想怎样调整你的%s？",
    "For speed": "提升速度",
    "For accuracy": "提升精准度",
    "Never mind": "算了",
    "The dew vial was emptied to heal your wounds.":
        "露珠瓶被倒空，用来治愈你的伤口。",
    "You collected a dewdrop into your dew vial.":
        "你把一滴露珠收集进露珠瓶。",
    "Your dew vial is full!": "你的露珠瓶满了！",
    "Your dew vial is empty!": "你的露珠瓶空了！",
    "Select an armor to upgrade": "选择要升级的护甲",
    "you applied the armor kit to upgrade your %s":
        "你使用护甲套件升级了%s",
    "This is a mimic!": "这是拟形怪！",
    "Strong magic aura of this place prevents you from using the lloyd's beacon!":
        "这里强大的魔法气场让你无法使用劳埃德信标！",
    "Psychic aura of neighbouring creatures doesn't allow you to use the lloyd's beacon at this moment.":
        "附近生物的灵能气场让你此刻无法使用劳埃德信标。",
    "The lloyd's beacon is successfully set at your current location, now you can return here anytime.":
        "劳埃德信标已成功设置在你当前位置，现在你随时可以返回这里。",
    "Lloyd's beacon is an intricate magic device, that allows you to return to a place you have already been.":
        "劳埃德信标是精巧的魔法装置，能让你返回曾经到过的地方。",
    "\n\nThis beacon was set somewhere on the level %d of Pixel Dungeon.":
        "\n\n这个信标设置在像素地牢第%d层的某处。",
    "You can't remove cursed %s!": "你无法脱下被诅咒的%s！",
    "Collect gold coins to spend them later in a shop.":
        "收集金币，日后在商店消费。",
    "A pile of %d gold coins. ": "一堆%d金币。",
    "One gold coin. ": "一枚金币。",
    "Your pack is too full for the %s": "你的背包太满，装不下%s",
    "Because of frequent use, your %s has broken.":
        "由于频繁使用，你的%s已经损坏。",
    "Because of frequent use, your %s is going to break soon.":
        "由于频繁使用，你的%s很快就要损坏。",
    "Choose direction of throw": "选择投掷方向",
    "END THE GAME": "结束游戏",
    "You are now familiar enough with your %s to identify it. It is %s.":
        "你现在对%s足够熟悉，能鉴定它了。它是%s。",
    "Interaction of different types of magic has negated the enchantment on this weapon!":
        "不同类型魔法的相互作用，抹去了这件武器上的附魔！",
    "broken %s :%d": "损坏的%s :%d",
    # enchantment names
    "venomous %s": "剧毒%s",
    "stunning %s": "眩晕%s",
    "unstable %s": "不稳定%s",
    "chilling %s": "寒冰%s",
    "vampiric %s": "吸血%s",
    "grim %s": "死神%s",
    "eldritch %s": "恐怖%s",
    "tempered %s": "淬炼%s",
    "blazing %s": "烈焰%s",
    "shocking %s": "电击%s",
    "lucky %s": "幸运%s",
    # short sword quest
    "Select a weapon to upgrade": "选择要升级的武器",
    "you reforged the short sword to upgrade your %s":
        "你重铸短剑，升级了你的%s",
    "you can't upgrade a boomerang this way":
        "你不能用这种方式升级回旋镖",
    # scrolls
    "You are now aware of the level layout.": "你现在掌握了本层布局。",
    "In a blink of an eye you were teleported to another location of the level.":
        "眨眼之间，你被传送到本层的另一处。",
    "Strong magic aura of this place prevents you from teleporting!":
        "这里强大的魔法气场让你无法传送！",
    "The scroll emits a brilliant flash of red light and the monsters flee!":
        "卷轴发出一道耀眼的红光，怪物们逃跑了！",
    " flees!": "逃跑了！",
    "The scroll emits a brilliant flash of red light":
        "卷轴发出一道耀眼的红光",
    "your %s certainly looks better now": "你的%s看起来确实好多了",
    "Select an enchantable item": "选择可附魔的物品",
    "You can't read a scroll while blinded": "你不能在失明时阅读卷轴",
    "Select an item to identify": "选择要鉴定的物品",
    "It is ": "它是",
    "The scroll utters a soothing melody and the monsters fall asleep!":
        "卷轴奏出舒缓的旋律，怪物们睡着了！",
    " falls asleep!": "睡着了！",
    "The scroll utters a soothing melody.": "卷轴奏出舒缓的旋律。",
    "Your pack glows with a cleansing light, and a malevolent energy disperses.":
        "你的背包发出净化之光，邪恶的能量消散了。",
    "Your pack glows with a cleansing light, but nothing happens.":
        "你的背包发出净化之光，但什么也没发生。",
    "The scroll emits a challenging roar that echoes throughout the dungeon!":
        "卷轴发出挑衅的怒吼，响彻整个地牢！",
    "Select an item to upgrade": "选择要升级的物品",
    "a surge of energy courses through your pack, recharging your wand":
        "一股能量涌入你的背包，为法杖充能",
    "a surge of energy courses through your pack, but nothing happens":
        "一股能量涌入你的背包，但什么也没发生",
    "Select an item": "选择物品",
    "Do you really want to cancel this scroll usage? It will be consumed anyway.":
        "你确定要取消使用这张卷轴吗？它还是会被消耗。",
    "Yes, I'm positive": "是，我确定",
    "No, I changed my mind": "否，我改主意了",
    # wands
    " to somewhere": "到某处",
    "nothing happened": "什么也没发生",
    "You have magically transported %s into your backpack":
        "你用魔法把%s移进了背包",
    "You killed yourself with your own Wand of Lightning...":
        "你用自己的闪电法杖把自己电死了……",
    "Select a wand to upgrade": "选择要升级的法杖",
    "you disenchanted the Wand of Magic Missile and used its essence to upgrade your %s":
        "你分解魔法飞弹法杖，用它的精华升级了%s",
    "You killed yourself with your own Wand of Magic Missile...":
        "你用自己的魔法飞弹法杖把自己打死了……",
    "Baa!": "咩！",
    "Baa?": "咩？",
    "This is a magic sheep. What's so magical about it? You can't kill it. ":
        "这是一只魔法绵羊。它哪里魔法？你杀不死它。",
    "It will stand there until it magcially fades away, all the while chewing cud with a blank stare.":
        "它会一直站在那里，直到魔法般消失，全程茫然地反刍。",
    "You killed yourself with your own Wand of Firebolt...":
        "你用自己的火焰法杖把自己烧死了……",
    "You killed yourself with your own Wand of Avalanche...":
        "你用自己的雪崩法杖把自己砸死了……",
    # potions
    "You float into the air!": "你飘到了空中！",
    "+1 str": "+1力量",
    "Newfound strength surges through your body.": "新生的力量涌遍全身。",
    "You see your hands turn invisible!": "你看见自己的手变隐形了！",
    "You feel uncommon freshness in the air.": "你感到空气中异常清新。",
    "You've stopped sensing any smells!": "你闻不到任何气味了！",
    "You can somehow feel the presence of other creatures' minds!":
        "你隐约能感到其他生物的心灵存在！",
    "You can somehow tell that you are alone on this level at the moment.":
        "你隐约感到此刻本层只有你一个人。",
    "Your wounds heal completely.": "你的伤口完全愈合。",
    "+1 str, +5 ht": "+1力量，+5生命",
    # class armor
    "You can only jump to an empty location in your field of view":
        "你只能跳到视野内的空位置",
    "Only rogues can use this armor!": "只有盗贼能使用这件护甲！",
    "SMOKE BOMB": "烟雾弹",
    "Choose a location to jump to": "选择要跳到的位置",
    "No enemies in sight": "视野内没有敌人",
    "Only huntresses can use this armor!": "只有女猎手能使用这件护甲！",
    "SPECTRAL BLADES": "幽灵之刃",
    "HEROIC LEAP": "英勇跳跃",
    "Only warriors can use this armor!": "只有战士能使用这件护甲！",
    "Choose direction to leap": "选择跳跃方向",
    "Your health is too low!": "你的生命值太低了！",
    "You need to be wearing this armor to use its special power!":
        "你需要穿上这件护甲才能使用它的特殊能力！",
    "MOLTEN EARTH": "熔土之术",
    "Only mages can use this armor!": "只有法师能使用这件护甲！",
    # glyphs
    "%s of bounce": "反弹%s",
    "%s of viscosity": "黏滞%s",
    "deferred %d": "延迟%d",
    "Defered damage (%d)": "延迟伤害（%d）",
    "enchantment of viscosity": "黏滞附魔",
    "The enchantment of viscosity killed you...": "黏滞附魔杀死了你……",
    "%s of multiplicity": "多重%s",
    "%s of entanglement": "缠绕%s",
    "%s of affection": "魅惑%s",
    "%s of displacement": "位移%s",
    "%s of potential": "潜能%s",
    "%s of stench": "恶臭%s",
    "%s of metabolism": "代谢%s",
    "%s of anti-entropy": "反熵%s",
    "%s of auto-repair": "自修%s",
    # pickaxe
    "There is no dark gold vein near you to mine":
        "你附近没有可开采的暗金矿脉",
    # food
    "That food tasted ok.": "这食物味道还行。",
    "You feel your skin hardens!": "你感到皮肤变硬了！",
    "Refreshing!": "神清气爽！",
    "You feel better!": "你感觉好多了！",
    "That food tasted delicious!": "这食物味道好极了！",
    "That food tasted... strange.": "这食物味道……很奇怪。",
    "Oh it's hot!": "哦，好烫！",
    "You can't feel your legs!": "你感觉不到自己的腿了！",
    "You are not feeling well.": "你感觉不太舒服。",
    "You are stuffed.": "你吃饱了。",
    # keys
    "iron key from depth %d": "第%d层的铁钥匙",
}


def main():
    files = 0
    for root, _, fl in os.walk(BASE):
        for f in fl:
            if not f.endswith(".java"):
                continue
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            original = content
            for k, v in T.items():
                content = content.replace('"%s"' % k, '"%s"' % v)
            if content != original:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(content)
                files += 1
    print("item files updated: %d" % files)


if __name__ == "__main__":
    sys.exit(main())
