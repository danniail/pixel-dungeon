#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate plant names, descriptions and seed names."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "src", "com", "watabou", "pixeldungeon", "plants")

PLANT_NAME = {
    "Dreamweed": "幻梦草",
    "Earthroot": "地根草",
    "Fadeleaf": "隐叶",
    "Firebloom": "火焰花",
    "Icecap": "冰冠草",
    "Rotberry": "腐莓",
    "Sorrowmoss": "悲苔",
    "Sungrass": "阳草",
}

# English description -> Chinese (single-line literals).
DESC = {
    "Upon touching a Dreamweed it secretes a glittering cloud of confusing gas.":
        "触碰幻梦草时，它会分泌出一团闪烁的、令人迷惑的气体。",
    "When a creature touches an Earthroot, its roots ":
        "当生物触碰地根草时，它的根须",
    "create a kind of natural armor around it.":
        "会在生物周围形成一层天然护甲。",
    "Touching a Fadeleaf will teleport any creature ":
        "触碰隐叶会把任意生物",
    "to a random place on the current level.":
        "传送到当前层的随机位置。",
    "When something touches a Firebloom, it bursts into flames.":
        "当有东西触碰火焰花时，它会爆成火焰。",
    "Upon touching an Icecap excretes a pollen, which freezes everything in its vicinity.":
        "触碰冰冠草时，它会释放花粉，冻结附近的一切。",
    "Berries of this shrub taste like sweet, sweet death.":
        "这种灌木的浆果尝起来像甜蜜的死亡。",
    "A Sorrowmoss is a flower (not a moss) with razor-sharp petals, coated with a deadly venom.":
        "悲苔是一种花（不是苔藓），花瓣锋利如刀，涂着致命的毒液。",
    "Sungrass is renowned for its sap's healing properties.":
        "阳草以其汁液的治愈功效闻名。",
}

EXTRA = {
    "Herbal armor": "草药护甲",
    "Herbal healing": "草药治愈",
    "The seed emits a roar that echoes throughout the dungeon!":
        "种子发出一声怒吼，响彻整个地牢！",
}

SEED_NAME_RE = re.compile(r'name\s*=\s*"seed of "\s*\+\s*plantName')


def main():
    files = 0
    for f in sorted(os.listdir(BASE)):
        if not f.endswith(".java") or f == "Plant.java":
            continue
        bn = f[:-5]
        path = os.path.join(BASE, f)
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()
        original = content

        if bn in PLANT_NAME:
            content = content.replace(
                'plantName = "%s"' % bn,
                'plantName = "%s"' % PLANT_NAME[bn])
        for k, v in DESC.items():
            content = content.replace('"%s"' % k, '"%s"' % v)
        for k, v in EXTRA.items():
            content = content.replace('"%s"' % k, '"%s"' % v)
        content = SEED_NAME_RE.sub('name = plantName + "种子"', content)

        if content != original:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
            files += 1
    print("plant files updated: %d" % files)


if __name__ == "__main__":
    sys.exit(main())
