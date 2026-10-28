#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate mob names and descriptions."""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RETURN_RE = re.compile(
    r'return\s+((?:"(?:[^"\\]|\\.)*"\s*(?:\+\s*)?)+);', re.DOTALL)
LIT_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')
NAME_RE = re.compile(r'(name\s*=\s*)"((?:[^"\\]|\\.)*)"')

NAMES = {
    "acidic scorpio": "酸性巨蝎",
    "albino rat": "白化巨鼠",
    "crazy bandit": "疯狂强盗",
    "vampire bat": "吸血蝙蝠",
    "gnoll brute": "豺狼蛮兵",
    "sewer crab": "下水道螃蟹",
    "curse personification": "诅咒化身",
    "fire elemental": "火焰元素",
    "evil eye": "邪眼",
    "fetid rat": "恶臭巨鼠",
    "gnoll scout": "豺狼斥候",
    "golem": "石魔像",
    "undead dwarf": "亡灵矮人",
    "mimic": "拟形怪",
    "dwarf monk": "矮人武僧",
    "giant piranha": "巨型食人鱼",
    "marsupial rat": "有袋巨鼠",
    "scorpio": "巨蝎",
    "senior monk": "资深武僧",
    "gnoll shaman": "豺狼萨满",
    "shielded brute": "持盾蛮兵",
    "skeleton": "骷髅",
    "cave spinner": "洞穴织网蛛",
    "animated statue": "活化雕像",
    "succubus": "魅魔",
    "swarm of flies": "苍蝇群",
    "crazy thief": "疯狂盗贼",
    "dwarf warlock": "矮人术士",
    "wraith": "幽魂",
    "rotting fist": "腐烂之拳",
    "burning fist": "燃烧之拳",
    "golden bee": "金色蜜蜂",
    "troll blacksmith": "巨魔铁匠",
    "sad ghost": "悲伤幽魂",
    "ambitious imp": "野心小恶魔",
    "mirror image": "镜像",
    "rat king": "鼠王",
    "shopkeeper": "店主",
    "old wandmaker": "老法杖匠",
}

# Description by file name (basename).
DESC = {
    "Bat": "这些轻快而顽强的洞穴穹顶居民，能靠每次成功攻击恢复生命，击败比自己大得多的对手。",
    "Brute": "蛮兵是豺狼中体型最大、最强壮、最坚韧的。受重伤时它们会陷入狂暴，对敌人造成更多伤害。",
    "Crab": "这些巨大的螃蟹位于下水道食物链顶端。它们速度极快，厚实的外骨骼能承受重击。",
    "CursePersonification": "这个生物形似悲伤幽魂，却被黑暗缠绕。它的脸上带着绝望的神情。",
    "DM300": "这台机器是几个世纪前由矮人制造的。后来矮人开始用石魔像、元素甚至恶魔取代机器，最终导致文明衰落。DM-300及类似机器通常用于建筑和采矿，有时也用于城市防御。",
    "Elemental": "游荡的火焰元素是召唤强大存在时的副产品。它们天性混乱，即使是最强大的恶魔学家也无法控制。",
    "Eye": "这个恶魔的另一个名字是“仇恨之球”，因为它一看到敌人就会肆无忌惮地施放死亡凝视，常常误伤盟友。",
    "FetidRat": "这只有袋巨鼠比普通巨鼠大得多，周身笼罩着恶臭的云雾。",
    "Gnoll": "豺狼是形似鬣狗的类人生物。它们栖息在下水道和地牢中，偶尔上到地面劫掠。豺狼斥候是狼群中的普通成员，不如蛮兵强壮，也不如萨满聪明。",
    "Golem": "矮人试图将机械知识与新掌握的元素束缚之力结合。他们用大地之灵作为石魔像机械躯体的“灵魂”，认为这是最可控的。尽管如此，仪式中最微小的失误也可能引发失控。",
    "Goo": "关于胶泥，人们所知甚少。它很可能根本不是生物，而是下水道中各种物质的聚合体，只是获得了初步的自由意志。",
    "King": "矮人的末代国王深谙生死之道。他说服宫廷成员参加一个本应赐予他们永恒青春的仪式。最终只有他得到了永生——还附赠了一支亡灵大军。",
    "Mimic": "拟形怪是能随心所欲变化形态的魔法生物。在地牢中它们几乎总是选择宝箱的形状，因为它们知道如何引诱冒险者。",
    "Mob": "真正的描述即将推出！",
    "Monk": "这些武僧是狂热者，致力于保护城市秘密，不让任何外来者知晓。他们不使用任何护甲或武器，完全依靠徒手格斗之术。",
    "Piranha": "这些食肉鱼并非地下水池的天然居民，而是专门为守护被水淹没的宝藏库而培育的。",
    "Rat": "有袋巨鼠是下水道中好斗却相当弱小的居民。只有数量庞大时它们才会构成威胁。",
    "Scorpio": "这些巨大的、形似蛛形纲的恶魔生物竭力避免近战，从远处发射致残的锯齿尖刺。",
    "Shaman": "最聪明的豺狼能掌握萨满魔法。豺狼萨满偏爱战斗法术以弥补力量不足，对那些质疑它们在部落中地位的人毫不留情。",
    "Skeleton": "骷髅由不幸的冒险者和地牢居民的尸骨构成，被深处散发的邪恶魔力驱动。受到足够伤害后，它们会在一阵骨爆中碎裂。",
    "Spinner": "这些毛茸茸的绿色洞穴蜘蛛尽量避免正面战斗，更愿意在远处等待，被它吐出的蛛网缠住的猎物会慢慢死于它的毒咬。",
    "Succubus": "魅魔是外表（略带哥特风）妖艳的女恶魔。魅魔能用魔法魅惑英雄，让他在魅惑解除前无法攻击任何东西。",
    "Swarm": "致命的苍蝇群愤怒地嗡嗡作响。每次非魔法攻击都会把它分裂成两个更小却同样危险的蝇群。",
    "Tengu": "天狗是古老刺客一族的成员，该族也叫天狗。这些刺客以大量使用手里剑和陷阱著称。",
    "Thief": "地牢更深处一直是各种罪犯的藏身之处。在远离阳光的漫长岁月里，并非所有人都能保持清醒。很久以前，这些疯狂的盗贼和强盗就忘记了自己是谁、为何而偷。",
    "Warlock": "当矮人的兴趣从工程转向奥术，术士开始在城市掌权。他们从元素魔法起步，但很快转向恶魔学和死灵术。",
    "Wraith": "幽魂是坟墓或墓穴被惊扰的罪人所化的复仇之灵。作为虚体存在，普通武器很难击中它。",
    "Bee": "尽管体型微小，金色蜜蜂却会勇猛保护主人。不过它们寿命不长。",
    "Blacksmith": "这个巨魔铁匠和所有巨魔一样：又高又瘦，皮肤的颜色和质地都像石头。巨魔铁匠正摆弄着小得不成比例的工具。",
    "Ghost": "幽魂几乎看不见。它像一团模糊的光点，没有形状，只有一张悲伤的脸。",
    "Imp": "小恶魔是低级恶魔。它们既不以力量著称，也不以魔法天赋闻名，但相当聪明、善于交际。许多小恶魔更喜欢生活在非恶魔之中。",
    "ImpShopkeeper": "小恶魔是低级恶魔。它们既不以力量著称，也不以魔法天赋闻名，但相当聪明、善于交际，许多小恶魔更喜欢在非恶魔之中生活和做生意。",
    "MirrorImage": "这个幻象与你极为相似，但更苍白，还会微微抽搐。",
    "RatKing": "这只老鼠比普通有袋巨鼠稍大一点，头上还戴着一顶小皇冠。",
    "Shopkeeper": "这个矮胖的家伙更适合大城市的商业区，而不是地牢。他的定价解释了他为什么更喜欢在这里做生意。",
    "Wandmaker": "这位年迈却精神矍铄的先生，脸上带着一丝困惑。他被一面魔法护盾保护着。",
}


def main():
    base = os.path.join(ROOT, "src", "com", "watabou", "pixeldungeon",
                       "actors", "mobs")
    n_name = n_desc = 0
    for root, _, files in os.walk(base):
        for f in sorted(files):
            if not f.endswith(".java"):
                continue
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            original = content

            def name_repl(m):
                key = m.group(2)
                if key in NAMES:
                    return m.group(1) + '"%s"' % NAMES[key]
                return m.group(0)

            content = NAME_RE.sub(name_repl, content)
            if content != original:
                n_name += 1

            bn = f[:-5]
            if bn in DESC:
                target = DESC[bn]

                def desc_repl(m):
                    return 'return "%s";' % target

                new_content = RETURN_RE.sub(
                    desc_repl, content, count=1)
                if new_content != content:
                    content = new_content
                    n_desc += 1

            if content != original:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(content)
    print("name files: %d, desc files: %d" % (n_name, n_desc))


if __name__ == "__main__":
    sys.exit(main())
