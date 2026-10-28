#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix defenseVerb methods and correctly translate description methods."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "src", "com", "watabou", "pixeldungeon", "actors", "mobs")

# basename -> defense verb (Chinese)
DEF_VERB = {
    "Bat": "闪避", "Crab": "格挡", "FetidRat": "闪避", "Golem": "抵挡",
    "King": "格挡", "Monk": "格挡", "Shielded": "抵挡", "Skeleton": "抵挡",
    "Swarm": "闪避", "Wraith": "闪避", "Ghost": "闪避", "Imp": "闪避",
    "Wandmaker": "吸收",
}

# basename -> description (Chinese). Reuse the canonical descriptions.
DESC = {
    "Bat": "这些轻快而顽强的洞穴穹顶居民，能靠每次成功攻击恢复生命，击败比自己大得多的对手。",
    "Swarm": "致命的苍蝇群愤怒地嗡嗡作响。每次非魔法攻击都会把它分裂成两个更小却同样危险的蝇群。",
    "Crab": "这些巨大的螃蟹位于下水道食物链顶端。它们速度极快，厚实的外骨骼能承受重击。",
    "Skeleton": "骷髅由不幸的冒险者和地牢居民的尸骨构成，被深处散发的邪恶魔力驱动。受到足够伤害后，它们会在一阵骨爆中碎裂。",
    "Monk": "这些武僧是狂热者，致力于保护城市秘密，不让任何外来者知晓。他们不使用任何护甲或武器，完全依靠徒手格斗之术。",
    "Wraith": "幽魂是坟墓或墓穴被惊扰的罪人所化的复仇之灵。作为虚体存在，普通武器很难击中它。",
    "King": "矮人的末代国王深谙生死之道。他说服宫廷成员参加一个本应赐予他们永恒青春的仪式。最终只有他得到了永生——还附赠了一支亡灵大军。",
    "Golem": "矮人试图将机械知识与新掌握的元素束缚之力结合。他们用大地之灵作为石魔像机械躯体的“灵魂”，认为这是最可控的。尽管如此，仪式中最微小的失误也可能引发失控。",
    "Thief": "地牢更深处一直是各种罪犯的藏身之处。在远离阳光的漫长岁月里，并非所有人都能保持清醒。很久以前，这些疯狂的盗贼和强盗就忘记了自己是谁、为何而偷。",
    "FetidRat": "这只有袋巨鼠比普通巨鼠大得多，周身笼罩着恶臭的云雾。",
}


def method_span(src, sig):
    i = src.find(sig)
    if i < 0:
        return None
    j = src.find("{", i)
    depth = 0
    for k in range(j, len(src)):
        if src[k] == "{":
            depth += 1
        elif src[k] == "}":
            depth -= 1
            if depth == 0:
                return (j, k)
    return None


def set_method_body(src, sig, new_body):
    sp = method_span(src, sig)
    if not sp:
        return src
    j, k = sp
    return src[:j + 1] + new_body + src[k:]


def main():
    fixed = 0
    for root, _, files in os.walk(BASE):
        for f in sorted(files):
            if not f.endswith(".java"):
                continue
            bn = f[:-5]
            if bn not in DEF_VERB and bn not in DESC:
                continue
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as fh:
                src = fh.read()
            original = src
            if bn in DEF_VERB:
                src = set_method_body(
                    src, "String defenseVerb()",
                    '\n\t\treturn "%s";\n\t' % DEF_VERB[bn])
            if bn in DESC:
                src = set_method_body(
                    src, "String description()",
                    '\n\t\treturn "%s";\n\t' % DESC[bn])
            if src != original:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(src)
                fixed += 1
    print("mobs fixed: %d" % fixed)


if __name__ == "__main__":
    sys.exit(main())
