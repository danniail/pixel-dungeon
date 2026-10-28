#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract every desc()/info() English paragraph from item sources."""
import os
import re
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")

METHOD_RE = re.compile(
    r"(?:public|protected)?\s*String\s+(?:desc|info)\s*\(\s*\)\s*\{")
LIT_RE = re.compile(r'"((?:[^"\\\n]|\\.)*)"')


def method_body(content, brace_idx):
    depth = 0
    i = brace_idx
    while i < len(content):
        ch = content[i]
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return content[brace_idx:i + 1]
        i += 1
    return content[brace_idx:]


def main():
    entries = []
    seen = {}
    for dirpath, _dirs, files in os.walk(SRC):
        for name in sorted(files):
            if not name.endswith(".java"):
                continue
            path = os.path.join(dirpath, name)
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            for m in METHOD_RE.finditer(content):
                body = method_body(content, m.end() - 1)
                lits = LIT_RE.findall(body)
                if not lits:
                    continue
                text = "".join(lits)
                if not text.strip():
                    continue
                rel = os.path.relpath(path, ROOT)
                if text not in seen:
                    seen[text] = len(entries)
                    entries.append({"id": len(entries), "file": rel, "text": text})
    out = os.path.join(ROOT, "tools", "desc_extract.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(entries, fh, ensure_ascii=False, indent=1)
    print("unique paragraphs: %d -> %s" % (len(entries), out))


if __name__ == "__main__":
    main()
