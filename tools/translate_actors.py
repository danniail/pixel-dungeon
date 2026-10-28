#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate remaining actors: combat messages, NPC dialogue, blobs, hero, subclasses."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "src", "com", "watabou", "pixeldungeon", "actors")

T = {
    # Char
    "%s hit %s": "%s 命中了 %s",
    "%s killed you...": "%s 杀死了你……",
    "%s defeated %s": "%s 击败了 %s",
    "%s %s your attack": "%s %s了你的攻击",
    "%s %s %s's attack": "%s %s了 %s 的攻击",
    "The pain snapped %s out of paralysis": "疼痛让 %s 从麻痹中惊醒",
    # mob death messages
    "%s's lightning bolt killed you...": "%s 的闪电击中了你……",
    "%s's deathgaze killed you...": "%s 的死亡凝视杀死了你……",
    "god's larva": "神之幼虫",
    "You were killed by the explosion of bones...": "你被骨爆杀死了……",
    "%s has knocked the %s from your hands!": "%s 把你手中的 %s 打落了！",
    "%s's shadow bolt killed you...": "%s 的暗影飞弹杀死了你……",
    # DM300
    "DM-300 repairs itself!": "DM-300 开始自我修复！",
    "Mission failed. Shutting down.": "任务失败，正在关机。",
    "Unauthorised personnel detected.": "检测到未授权人员。",
    # Brute
    "%s becomes enraged!": "%s 狂暴了！",
    # Mob
    "You hear something died in the distance": "你听见远处有什么东西死了",
    "echo of ": "回声：",
    "%+dEXP": "%+d经验",
    '%s: "%s" ': "%s：“%s”",
    "This %s is sleeping": "这只 %s 正在睡觉",
    "This %s is wandering": "这只 %s 正在游荡",
    "This %s is hunting": "这只 %s 正在狩猎",
    "This %s is fleeing": "这只 %s 正在逃跑",
    "This %s is passive": "这只 %s 很被动",
    # King
    "King of Dwarves": "矮人国王",
    "undead King of Dwarves": "亡灵矮人国王",
    "You cannot kill me, ": "你杀不死我，",
    "... I am... immortal...": "……我是……不朽的……",
    "Arise, slaves!": "起来吧，奴隶们！",
    "How dare you!": "你好大的胆子！",
    "These undead dwarves, risen by the will of the King of Dwarves, were members of his court. ":
        "这些亡灵矮人受矮人国王的意志复活，曾是他的宫廷成员。",
    "They appear as skeletons with a stunning amount of facial hair.":
        "它们看起来是骷髅，却有着惊人的浓密胡须。",
    # Tengu
    "Free at last...": "终于自由了……",
    "Gotcha, ": "抓到你了，",
    # Goo
    "Goo is pumping itself up!": "胶泥正在膨胀！",
    "glurp... glurp...": "咕噜……咕噜……",
    "GLURP-GLURP!": "咕噜——咕噜！",
    # Thief
    "%s stole %s from you!": "%s 偷了你的 %s！",
    "\n\n%s is carrying a _%s_. Stolen obviously.":
        "\n\n%s 带着 _%s_，显然是偷来的。",
    # Ghost description
    "The ghost is barely visible. It looks like a shapeless ":
        "幽魂几乎看不见，它看起来像一团没有形状的",
    "spot of faint light with a sorrowful face.":
        "微光，带着悲伤的面容。",
    # Ghost rose quest
    "Hello adventurer... Once I was like you - strong and confident... ":
        "你好，冒险者……我曾和你一样——强壮而自信……",
    "And now I'm dead... But I can't leave this place... Not until I have my _dried rose_... ":
        "现在我死了……但我无法离开这里……除非我找回我的 _干枯玫瑰_……",
    "It's very important to me... Some monster stole it from my body...":
        "它对我很重要……有怪物从我身上偷走了它……",
    "Please... Help me... _Find the rose_...":
        "求求你……帮帮我……_找到那朵玫瑰_……",
    "Yes! Yes!!! This is it! Please give it to me! ":
        "对！就是它！请把它给我！",
    "And you can take one of these items, maybe they ":
        "你可以从这些物品中选一件，也许它们",
    "will be useful to you in your journey...":
        "会在你的旅途中派上用场……",
    # Ghost revenge quest
    "And now I'm dead... But I can't leave this place... Not until I have my revenge... ":
        "现在我死了……但我无法离开这里……除非我能复仇……",
    "Slay the _fetid rat_, that has taken my life...":
        "杀死那只夺走我生命的 _恶臭巨鼠_……",
    "Please... Help me... _Slay the abomination_...":
        "求求你……帮帮我……_杀死那个怪物_……",
    "Yes! The ugly creature is slain and I can finally rest... ":
        "太好了！那丑陋的怪物已被杀死，我终于可以安息了……",
    "Please take one of these items, maybe they ":
        "请从这些物品中选一件，也许它们",
    # Ghost curse quest
    "And now I'm dead... But I can't leave this place, as I am bound by a horrid curse... ":
        "现在我死了……但我无法离开这里，因为我被可怕的诅咒束缚……",
    "Please... Help me... _Destroy the curse_...":
        "求求你……帮帮我……_破除诅咒_……",
    "Thank you, %s! The curse is broken and I can finally rest... ":
        "谢谢你，%s！诅咒已被破除，我终于可以安息了……",
    "Yes, I will do it for you": "好，我愿意帮你",
    "No, I can't help you": "不，我帮不了你",
    # Blacksmith
    "Hey human! Wanna be useful, eh? Take dis pickaxe and mine me some _dark gold ore_, _15 pieces_ should be enough. ":
        "嘿，人类！想帮个忙吗？拿上这把镐，给我挖点 _暗金矿石_，_15块_ 就够了。",
    "What do you mean, how am I gonna pay? You greedy...\n":
        "你什么意思，我怎么付钱？你这贪心的……\n",
    "Ok, ok, I don't have money to pay, but I can do some smithin' for you. Consider yourself lucky, ":
        "好吧，好吧，我没钱付你，但我可以给你打铁。算你走运，",
    "I'm the only blacksmith around.": "我是这附近唯一的铁匠。",
    "Hey human! Wanna be useful, eh? Take dis pickaxe and _kill a bat_ wit' it, I need its blood on the head. ":
        "嘿，人类！想帮个忙吗？拿上这把镐，用它 _杀一只蝙蝠_，我需要镐头沾它的血。",
    "Are you kiddin' me? Where is my pickaxe?!": "你在开玩笑吗？我的镐呢？！",
    "Dark gold ore. 15 pieces. Seriously, is it dat hard?":
        "暗金矿石，15块。说真的，有那么难吗？",
    "I said I need bat blood on the pickaxe. Chop chop!":
        "我说了镐上要沾蝙蝠血。快点！",
    "Oh, you have returned... Better late dan never.":
        "哦，你回来了……晚到总比不到好。",
    "I'm busy. Get lost!": "我忙着呢，走开！",
    "your %s certainly looks better now": "你的 %s 看起来确实好多了",
    "Select 2 items of the same type!": "选择两件同类型的物品！",
    "I need to know what I'm working with, identify them first!":
        "我得知道自己在处理什么，先鉴定它们！",
    "I don't work with cursed items!": "我不碰被诅咒的物品！",
    "It's a junk, the quality is too poor!": "这是废品，质量太差了！",
    "I can't reforge these items!": "我无法重铸这些物品！",
    "This troll blacksmith looks like all trolls look: he is tall and lean, and his skin resembles stone ":
        "这个巨魔铁匠和所有巨魔一样：又高又瘦，皮肤的颜色和质地都像石头。",
    "in both color and texture. The troll blacksmith is tinkering with unproportionally small tools.":
        "他正摆弄着小得不成比例的工具。",
    # Shopkeepers
    "Hello, friend!": "你好，朋友！",
    "Select an item to sell": "选择要出售的物品",
    "I'm not sleeping!": "我没在睡觉！",
    "What is it? I have no time for this nonsense. My kingdom won't rule itself!":
        "什么事？我没时间胡闹，我的王国可不会自己统治自己！",
    # Imp
    "Are you an adventurer? I love adventurers! You can always rely on them ":
        "你是冒险者吗？我喜欢冒险者！你总能指望他们",
    "if something needs to be killed. Am I right? For a bounty, of course ;)\n":
        "去杀掉该杀的东西。对吧？当然是为了赏金;)\n",
    "In my case this is _golems_ who need to be killed. You see, I'm going to start a ":
        "我这边呢，需要杀掉的是 _石魔像_。你看，我打算在这儿",
    "little business here, but these stupid golems are bad for business! ":
        "做点小生意，但这些蠢石魔像对生意没好处！",
    "It's very hard to negotiate with wandering lumps of granite, damn them! ":
        "跟游荡的花岗岩块可没法谈判，该死的！",
    "So please, kill... let's say _6 of them_ and a reward is yours.":
        "所以拜托，杀掉……就 _6个_ 吧，赏金就是你的。",
    "In my case this is _monks_ who need to be killed. You see, I'm going to start a ":
        "我这边呢，需要杀掉的是 _武僧_。你看，我打算在这儿",
    "little business here, but these lunatics don't buy anything themselves and ":
        "做点小生意，但这些疯子自己什么都不买，还",
    "will scare away other customers. ": "会吓跑其他顾客。",
    "So please, kill... let's say _8 of them_ and a reward is yours.":
        "所以拜托，杀掉……就 _8个_ 吧，赏金就是你的。",
    "How is your golem safari going?": "你的石魔像狩猎进展如何？",
    "Oh, you are still alive! I knew that your kung-fu is stronger ;) ":
        "哦，你还活着！我就知道你功夫更厉害;) ",
    "Just don't forget to grab these monks' tokens.":
        "别忘了拿这些武僧的信物。",
    "See you, %s!": "再见，%s！",
    "Psst, %s!": "嘘，%s！",
    "Imps are lesser demons. They are notable for neither their strength nor their magic talent, ":
        "小恶魔是低等恶魔。它们既不以力量著称，也不以魔法天赋闻名，",
    "but they are quite smart and sociable. Many imps prefer to live among non-demons.":
        "但相当聪明、善于交际。许多小恶魔喜欢生活在非恶魔之中。",
    # Wandmaker description
    "This old but hale gentleman wears a slightly confused ":
        "这位年迈却矍铄的绅士，脸上带着一丝困惑，",
    "expression. He is protected by a magic shield.":
        "他被一面魔法护盾保护着。",
    "Oh, what a pleasant surprise to meet a decent person in such place! I came here for a rare ingredient - ":
        "哦，在这种地方遇到正派人，真是惊喜！我来这儿是为了一种稀有材料——",
    "a _Rotberry seed_. Being a magic user, I'm quite able to defend myself against local monsters, ":
        "一颗 _腐烂浆果种子_。作为施法者，我完全能对付这里的怪物，",
    "but I'm getting lost in no time, it's very embarrassing. Probably you could help me? I would be ":
        "但我很快就会迷路，这很尴尬。也许你能帮我？我很乐意",
    "happy to pay for your service with one of my best wands.":
        "用我最好的法杖之一来支付你的酬劳。",
    "Any luck with a _Rotberry seed_, %s? No? Don't worry, I'm not in a hurry.":
        "找到 _腐烂浆果种子_ 了吗，%s？没有？别担心，我不急。",
    "_corpse dust_. It can be gathered from skeletal remains and there is an ample number of them in the dungeon. ":
        "_尸尘_。可以从骸骨残骸中收集，地牢里有大量这种东西。",
    "Being a magic user, I'm quite able to defend myself against local monsters, but I'm getting lost in no time, ":
        "作为施法者，我完全能对付这里的怪物，但我很快就会迷路，",
    "it's very embarrassing. Probably you could help me? I would be happy to pay for your service with one of my best wands.":
        "这很尴尬。也许你能帮我？我很乐意用我最好的法杖之一来支付你的酬劳。",
    "Any luck with _corpse dust_, %s? Bone piles are the most obvious places to look.":
        "找到 _尸尘_ 了吗，%s？骨堆是最明显的寻找地点。",
    "Oh, what a pleasant surprise to meet a decent person in such place! I came here for a rare ingredient: ":
        "哦，在这种地方遇到正派人，真是惊喜！我来这儿是为了一种稀有材料：",
    "a _phantom fish_. You can catch it with your bare hands, but it's very hard to notice in the water. ":
        "一条 _幻影鱼_。你可以徒手抓住它，但它在水里很难被发现。",
    "Any luck with a _phantom fish_, %s? You may want to try searching for it in one of the local pools.":
        "抓到 _幻影鱼_ 了吗，%s？你可以试试在附近的水池里找找。",
    # blobs
    "A greenish cloud of toxic gas is swirling here.":
        "一团绿色的毒气在这里盘旋。",
    "You died from a toxic gas..": "你死于毒气……",
    "As you take a sip, you feel the knowledge pours into your mind. ":
        "你啜饮一口，感到知识涌入脑海。",
    "Now you know everything about your equipped items. Also you sense ":
        "现在你了解了所有已装备物品的信息，还能感知到",
    "all items on the level and know all its secrets.":
        "本层的所有物品，并知晓它的全部秘密。",
    "Power of knowledge radiates from the water of this well. ":
        "这口井的水散发着知识的力量。",
    "Take a sip from it to reveal all secrets of equipped items.":
        "啜饮一口，揭示已装备物品的全部秘密。",
    "A cloud of paralytic gas is swirling here.":
        "一团麻痹气体在这里盘旋。",
    "Shafts of light pierce the gloom of the underground garden.":
        "道道光线穿透地下花园的幽暗。",
    "As you take a sip, you feel your wounds heal completely.":
        "你啜饮一口，感到伤口完全愈合。",
    "Power of health radiates from the water of this well. ":
        "这口井的水散发着生命的力量。",
    "Take a sip from it to heal your wounds and satisfy hunger.":
        "啜饮一口，治愈伤口并缓解饥饿。",
    "A cloud of confusion gas is swirling here.":
        "一团混乱气体在这里盘旋。",
    "Everything is covered with a thick web here.":
        "这里的一切都覆盖着厚厚的蛛网。",
    "Power of change radiates from the water of this well. ":
        "这口井的水散发着变化的力量。",
    "Throw an item into the well to turn it into something else.":
        "把物品扔进井里，它会变成别的东西。",
    "A fire is raging here.": "这里烈火熊熊。",
    '"Your sacrifice is worthy..." ': "“你的献祭有价值……”",
    '"Your sacrifice is unworthy..." ': "“你的献祭毫无价值……”",
    '"Your sacrifice is worthy and so you are!" ':
        "“你的献祭有价值，你也一样！”",
    "Sacrificial fire burns here. Every creature touched by this fire is marked as an offering for the spirits of the dungeon.":
        "献祭之火在这里燃烧。被这火触碰的生物，会被标记为献给地牢怨灵的祭品。",
    "Marked for sacrifice": "被标记为祭品",
    # Hero
    "One does not simply leave Pixel Dungeon.":
        "一个人可不能轻易离开像素地牢。",
    "level up!": "升级了！",
    "Welcome to level %d! Now you are healthier and more focused. ":
        "欢迎来到第%d级！现在你更健康、更专注。",
    "It's easier for you to hit enemies and dodge their attacks.":
        "你更容易命中敌人，也更容易闪避他们的攻击。",
    "You now have %s": "你现在拥有 %s",
    "There is something else here": "这里还有别的东西",
    "This chest is locked and you don't have matching key":
        "这只箱子锁着，你没有匹配的钥匙",
    "You don't have a matching key": "你没有匹配的钥匙",
    "You noticed something": "你注意到了什么",
    "You catch fire!": "你着火了！",
    "You are paralysed!": "你被麻痹了！",
    "You are poisoned!": "你中毒了！",
    "Caustic ooze eats your flesh. Wash away it!":
        "腐蚀性软泥在啃噬你的血肉，快把它洗掉！",
    "You can't move!": "你无法移动！",
    "You feel weakened!": "你感到虚弱！",
    "You are blinded!": "你失明了！",
    "You become furious!": "你狂暴了！",
    "You are charmed!": "你被魅惑了！",
    "You are crippled!": "你残废了！",
    "You are bleeding!": "你在流血！",
    "Everything is spinning around you!": "周围的一切都在旋转！",
    # HeroSubClass
    "A successful attack with a melee weapon allows the _Gladiator_ to start a combo, ":
        "用近战武器成功攻击后，_角斗士_ 可以发起连击，",
    "in which every next successful hit inflicts more damage.":
        "每一次成功命中都会造成更多伤害。",
    "When severely wounded, the _Berserker_ enters a state of wild fury ":
        "当身负重伤时，_狂战士_ 会进入狂野的暴怒状态，",
    "significantly increasing his damage output.":
        "显著提升伤害输出。",
    "After killing an enemy the _Warlock_ consumes its soul. ":
        "杀死敌人后，_术士_ 会吞噬它的灵魂，",
    "It heals his wounds and satisfies his hunger.":
        "治愈他的伤口并缓解饥饿。",
    "When fighting with a wand in his hands, the _Battlemage_ inflicts additional damage depending ":
        "手持法杖战斗时，_战斗法师_ 会根据当前充能数造成额外伤害，",
    "on the current number of charges. Every successful hit restores 1 charge to this wand.":
        "每次成功命中会为该法杖恢复1点充能。",
    "When performing a surprise attack, the _Assassin_ inflicts additional damage to his target.":
        "进行突袭时，_刺客_ 会对目标造成额外伤害。",
    "The _Freerunner_ can move almost twice faster, than most of the monsters. When he ":
        "_疾行者_ 的移动速度几乎是大多数怪物的两倍。奔跑时，",
    "is running, the Freerunner is much harder to hit. For that he must be unencumbered and not starving.":
        "疾行者更难被击中。为此他必须身无负重、且不处于饥饿状态。",
    "_Snipers_ are able to detect weak points in an enemy's armor, ":
        "_狙击手_ 能发现敌人护甲的弱点，",
    "effectively ignoring it when using a missile weapon.":
        "使用远程武器时能有效无视护甲。",
    "Having a strong connection with forces of nature gives _Wardens_ an ability to gather dewdrops and ":
        "与自然之力的强烈联系，让 _守望者_ 能从植物中收集露珠和种子。",
    "seeds from plants. Also trampling a high grass grants them a temporary armor buff.":
        "此外，踩踏高草会给予他们临时的护甲增益。",
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
    print("actor files updated: %d" % files)


if __name__ == "__main__":
    sys.exit(main())
