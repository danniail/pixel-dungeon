#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""玩家/怪物/NPC 精灵图与帧尺寸权威配置。
sprite 名 -> (asset 文件, 原帧宽, 原帧高)。
高清化：帧尺寸 x2、sheet x2、MobSprite scale 0.5，帧索引不变。
"""

# 玩家（HeroSprite，统一 24x30，已在 HeroSprite 处理）
HERO_SHEETS = ['warrior.png', 'mage.png', 'rogue.png', 'ranger.png']

# 怪物 / NPC：sprite -> (asset, fw, fh)
MOBS = {
    'Rat':        ('rat.png', 16, 15),
    'Albino':     ('rat.png', 16, 15),
    'FetidRat':   ('rat.png', 16, 15),
    'Gnoll':      ('gnoll.png', 12, 15),
    'Crab':       ('crab.png', 16, 16),
    'Goo':        ('goo.png', 20, 14),
    'Swarm':      ('swarm.png', 16, 16),
    'Skeleton':   ('skeleton.png', 12, 15),
    'Shaman':     ('shaman.png', 12, 15),
    'Thief':      ('thief.png', 12, 13),
    'Bandit':     ('thief.png', 12, 13),
    'Tengu':      ('tengu.png', 14, 16),
    'Sheep':      ('sheep.png', 16, 15),
    'Shopkeeper': ('shopkeeper.png', 14, 14),
    'Bat':        ('bat.png', 15, 15),
    'Brute':      ('brute.png', 12, 16),
    'Shielded':   ('brute.png', 12, 16),
    'Spinner':    ('spinner.png', 16, 16),
    'DM300':      ('dm300.png', 22, 20),
    'Wraith':     ('wraith.png', 14, 15),
    'CursePersonification': ('wraith.png', 14, 15),
    'Elemental':  ('elemental.png', 12, 14),
    'Monk':       ('monk.png', 15, 14),
    'Senior':     ('monk.png', 15, 14),
    'Warlock':    ('warlock.png', 12, 15),
    'Golem':      ('golem.png', 16, 16),
    'Undead':     ('undead.png', 12, 16),
    'King':       ('king.png', 16, 16),
    'Statue':     ('statue.png', 12, 15),
    'Piranha':    ('piranha.png', 12, 16),
    'Eye':        ('eye.png', 16, 18),
    'Succubus':   ('succubus.png', 12, 15),
    'Scorpio':    ('scorpio.png', 18, 17),
    'Acidic':     ('scorpio.png', 18, 17),
    'RottingFist': ('rotting_fist.png', 24, 17),
    'BurningFist': ('burning_fist.png', 24, 17),
    'Yog':        ('yog.png', 20, 19),
    'Larva':      ('larva.png', 12, 8),
    'Ghost':      ('ghost.png', 14, 15),
    'Wandmaker':  ('wandmaker.png', 12, 14),
    'Blacksmith': ('blacksmith.png', 13, 16),
    'Imp':        ('demon.png', 12, 14),
    'RatKing':    ('ratking.png', 16, 16),
    'Bee':        ('bee.png', 16, 16),
    'Mimic':     ('mimic.png', 16, 16),
}

# 唯一需要翻倍的 asset 文件
MOB_SHEETS = sorted({v[0] for v in MOBS.values()})
