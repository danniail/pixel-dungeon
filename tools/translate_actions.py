#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate item action constants (AC_*), which are both button labels and
the action identifiers compared in execute()."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")

VAL = {
    "DROP": "丢弃",
    "THROW": "投掷",
    "EQUIP": "装备",
    "UNEQUIP": "卸下",
    "SHATTER": "打碎",
    "APPLY": "使用",
    "EAT": "食用",
    "READ": "阅读",
    "OPEN": "打开",
    "LIGHT": "点燃",
    "MINE": "开采",
    "REFORGE": "重铸",
    "SET": "设置",
    "RETURN": "返回",
    "DISENCHANT": "分解",
    "DRINK": "饮用",
}

AC_RE = re.compile(r'(AC_[A-Z_]+\s*=\s*)"([A-Z_]+)"')


def repl(m):
    name, val = m.group(1), m.group(2)
    if val in VAL:
        return '%s"%s"' % (name, VAL[val])
    return m.group(0)


def main():
    files = 0
    for root, _, fl in os.walk(SRC):
        for f in fl:
            if not f.endswith(".java"):
                continue
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            new = AC_RE.sub(repl, content)
            if new != content:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new)
                files += 1
    print("action files updated: %d" % files)


if __name__ == "__main__":
    sys.exit(main())
