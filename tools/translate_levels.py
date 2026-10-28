#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate levels (decorations, terrain descriptions, signs, traps)."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "src", "com", "watabou", "pixeldungeon", "levels")

T = {
    # Caves
    "Fluorescent moss": "荧光苔藓",
    "Fluorescent mushrooms": "荧光蘑菇",
    "Freezing cold water.": "冰冷刺骨的水。",
    "The ladder leads up to the upper depth.": "梯子通向上一层。",
    "The ladder leads down to the lower depth.": "梯子通向下一层。",
    "Huge mushrooms block the view.": "巨大的蘑菇挡住了视线。",
    "A vein of some ore is visible on the wall. Gold?":
        "墙上能看见一条矿脉。是金子吗？",
    "Who would need a bookshelf in a cave?": "谁会在洞穴里需要书架？",
    # City
    "Suspiciously colored water": "颜色可疑的水",
    "High blooming flowers": "盛开的高花",
    "A ramp leads up to the upper depth.": "坡道通向上一层。",
    "A ramp leads down to the lower depth.": "坡道通向下一层。",
    "A ramp leads down to the Inferno.": "坡道通向炼狱。",
    "Several tiles are missing here.": "这里缺了几块地砖。",
    "Thick carpet covers the floor.": "厚厚的地毯铺在地上。",
    "The statue depicts some dwarf standing in a heroic stance.":
        "雕像刻画了一个摆出英勇姿态的矮人。",
    "The rows of books on different disciplines fill the bookshelf.":
        "书架上摆满了各门学科的书籍。",
    # Halls
    "Cold lava": "冰冷的熔岩",
    "It looks like lava, but it's cold and probably safe to touch.":
        "看起来像熔岩，但它是冷的，触碰也许安全。",
    "The pillar is made of real humanoid skulls. Awesome.":
        "柱子由真正的类人生物头骨堆成，令人惊叹。",
    "Books in ancient languages smoulder in the bookshelf.":
        "书架上用古老语言写成的书在阴燃。",
    # Level.java
    "A hidden pressure plate clicks!": "一块隐藏的压力板咔哒作响！",
    "Closed door": "关闭的门",
    "Open door": "敞开的门",
    "Depth entrance": "本层入口",
    "Depth exit": "本层出口",
    "Locked door": "上锁的门",
    "High grass": "高草",
    "Locked depth exit": "上锁的本层出口",
    "Unlocked depth exit": "未锁的本层出口",
    "Empty well": "空井",
    "Toxic gas trap": "毒气陷阱",
    "Fire trap": "火焰陷阱",
    "Paralytic gas trap": "麻痹气体陷阱",
    "Poison dart trap": "毒镖陷阱",
    "Alarm trap": "警报陷阱",
    "Lightning trap": "闪电陷阱",
    "Gripping trap": "夹持陷阱",
    "Summoning trap": "召唤陷阱",
    "Triggered trap": "已触发的陷阱",
    "Alchemy pot": "炼金釜",
    "You can't see the bottom.": "你看不见底。",
    "In case of burning step into the water to extinguish the fire.":
        "如果着火，踏进水里灭火。",
    "Stairs lead up to the upper depth.": "楼梯通向上一层。",
    "Stairs lead down to the lower depth.": "楼梯通向下一层。",
    "Embers cover the floor.": "余烬铺满地面。",
    "Dense vegetation blocks the view.": "茂密的植被挡住了视线。",
    "This door is locked, you need a matching key to unlock it.":
        "这扇门锁着，你需要匹配的钥匙才能打开。",
    "Heavy bars block the stairs leading down.":
        "沉重的铁栏挡住了向下的楼梯。",
    "The wooden barricade is firmly set but has dried over the years. Might it burn?":
        "木栅栏很牢固，但岁月已让它干枯。它会燃烧吗？",
    "You can't read the text from here.": "你从这里看不清文字。",
    "Stepping onto a hidden pressure plate will activate the trap.":
        "踩到隐藏的压力板会触发陷阱。",
    "The trap has been triggered before and it's not dangerous anymore.":
        "这个陷阱之前已被触发，不再危险。",
    "Someone wanted to adorn this place, but failed, obviously.":
        "有人想装饰这个地方，但显然失败了。",
    "Drop some seeds here to cook a potion.":
        "把种子扔到这里，酿造药水。",
    "The well has run dry.": "井已经干涸。",
    # Prison
    "Dark cold water.": "冰冷的黑水。",
    "There are old blood stains on the floor.": "地上有陈旧的血迹。",
    "This is probably a vestige of a prison library. Might it burn?":
        "这也许是监狱图书馆的遗迹。它会燃烧吗？",
    # Sewer
    "Murky water": "浑浊的水",
    "Wet yellowish moss covers the floor.": "潮湿发黄的苔藓铺满地面。",
    "The bookshelf is packed with cheap useless books. Might it burn?":
        "书架上塞满了廉价无用的书。它会燃烧吗？",
    # features
    "Select a seed to throw": "选择要扔的种子",
    "Yes, I know what I'm doing": "是，我知道自己在做什么",
    "No, I changed my mind": "否，我改主意了",
    "Do you really want to jump into the chasm? You can probably die.":
        "你真的想跳进深渊吗？你可能会死。",
    "You fell to death...": "你坠落而死……",
    # Sign
    "What are you doing here?!": "你在这里做什么？！",
    "Don't overestimate your strength, use weapons and armor you can handle.":
        "别高估自己的力量，使用你能驾驭的武器和护甲。",
    "Not all doors in the dungeon are visible at first sight. If you are stuck, search for hidden doors.":
        "地牢里并非所有门都一眼可见。如果你卡住了，搜索暗门。",
    "Remember, that raising your strength is not the only way to access better equipment. You can go ":
        "记住，提升力量并非获得更好装备的唯一途径。你可以",
    "the other way, lowering its strength requirement with Scrolls of Upgrade.":
        "反其道而行，用升级卷轴降低装备的力量需求。",
    "You can spend your gold in shops on deeper levels of the dungeon. The first one is on the 6th level.":
        "你可以在地牢更深处的商店花金币。第一家商店在第6层。",
    "Beware of Goo!": "小心胶泥！",
    "Pixel-Mart - all you need for successful adventure!":
        "像素超市——成功冒险所需的一切！",
    "Identify your potions and scrolls as soon as possible. Don't put it off to the moment ":
        "尽快鉴定你的药水和卷轴。别拖到",
    "when you actually need them.": "真正需要它们的时候。",
    "Being hungry doesn't hurt, but starving does hurt.":
        "饥饿不碍事，但极度饥饿会受伤。",
    "Surprise attack has a better chance to hit. For example, you can ambush your enemy behind ":
        "突袭命中几率更高。比如，你可以",
    "a closed door when you know it is approaching.":
        "知道敌人接近时，躲在关闭的门后伏击。",
    "Don't let The Tengu out!": "别让天狗出来！",
    "Pixel-Mart. Spend money. Live longer.": "像素超市。花钱，活得更久。",
    "When you're attacked by several monsters at the same time, try to retreat behind a door.":
        "当你同时被多个怪物攻击时，试着退到门后。",
    "If you are burning, you can't put out the fire in the water while levitating.":
        "如果你着火，漂浮时无法在水里灭火。",
    "There is no sense in possessing more than one Ankh at the same time, because you will lose them upon resurrecting.":
        "同时拥有多个安卡没有意义，复活时你会失去它们。",
    "DANGER! Heavy machinery can cause injury, loss of limbs or death!":
        "危险！重型机械可能造成伤害、断肢或死亡！",
    "Pixel-Mart. A safer life in dungeon.": "像素超市。地牢里更安全的生活。",
    "When you upgrade an enchanted weapon, there is a chance to destroy that enchantment.":
        "升级附魔武器时，有可能破坏该附魔。",
    "Weapons and armors deteriorate faster than wands and rings, but there are more ways to fix them.":
        "武器和护甲比法杖、戒指损耗更快，但修复方法也更多。",
    "The only way to obtain a Scroll of Wipe Out is to receive it as a gift from the dungeon spirits.":
        "获得湮灭卷轴的唯一途径，是地牢怨灵的馈赠。",
    "No weapons allowed in the presence of His Majesty!":
        "国王陛下在场，禁止携带武器！",
    "Pixel-Mart. Special prices for demon hunters!":
        "像素超市。恶魔猎手专享价！",
    "As you try to read the sign it bursts into greenish flames.":
        "你试图读告示牌时，它爆成绿色的火焰。",
    # traps
    "The trap emits a piercing sound that echoes throughout the dungeon!":
        "陷阱发出刺耳的声音，响彻整个地牢！",
    "lightning trap": "闪电陷阱",
    "You were killed by a discharge of a lightning trap...":
        "你被闪电陷阱的放电杀死了……",
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
    print("level files updated: %d" % files)


if __name__ == "__main__":
    sys.exit(main())
