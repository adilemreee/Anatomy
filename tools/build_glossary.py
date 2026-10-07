#!/usr/bin/env python3
"""Builds Anatomy/Resources/glossary.json: Latin names (Terminologia Anatomica 2)
and the Z-Anatomy reference text for every name used by the 3D parts.

usage: tools/build_glossary.py <texts.json> <TA2.csv>
  texts.json comes from tools/dump_zanatomy_texts.py, TA2.csv from the
  Z-Anatomy repository.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS = os.path.join(ROOT, "Anatomy", "Resources", "Models")
OUT = os.path.join(ROOT, "Anatomy", "Resources", "glossary.json")
MAX_DEF = 2200


def variants(name):
    n = name.strip()
    out = [n]
    m = n.strip("()").strip()
    out.append(m)
    out.append(re.sub(r"\*", "", m).strip())
    out.append(re.sub(r"\s*\([^)]*\)\s*\*?$", "", m).strip())
    out.append(re.sub(r"\s*\([^)]*\)", "", m).replace("*", "").strip())
    seen = []
    for v in out:
        v = v.lower()
        if v and v not in seen:
            seen.append(v)
    return seen


def clean_def(text):
    text = text.replace("\r", "")
    lines = [l.strip() for l in text.split("\n")]
    # drop the upper-case title line at the top
    while lines and (not lines[0] or lines[0].isupper()):
        lines.pop(0)
    paras, cur = [], []
    for l in lines:
        h = re.match(r"^=+\s*(.*?)\s*=+$", l)
        if h:
            if cur:
                paras.append(" ".join(cur)); cur = []
            paras.append("## " + h.group(1))
        elif not l:
            if cur:
                paras.append(" ".join(cur)); cur = []
        else:
            cur.append(l)
    if cur:
        paras.append(" ".join(cur))
    out, size = [], 0
    for p in paras:
        p = re.sub(r"\(\s*[,;]\s*", "(", p)
        p = re.sub(r"\(\s*\)", "", p)
        p = re.sub(r"\s+([,.;:])", r"\1", p)
        p = re.sub(r"\s{2,}", " ", p).strip()
        if not p:
            continue
        if p.startswith("## ") and out and out[-1].startswith("## "):
            out.pop()
        if size + len(p) > MAX_DEF and out:
            break
        out.append(p); size += len(p)
    while out and out[-1].startswith("## "):
        out.pop()
    return "\n\n".join(out)


def main():
    texts = json.load(open(sys.argv[1], encoding="utf-8"))
    rows = open(sys.argv[2], encoding="utf-8-sig").read().splitlines()
    latin = {}
    for r in rows[1:]:
        f = r.strip().strip('"').split(";")
        if len(f) >= 3 and f[1].strip():
            latin.setdefault(f[1].strip().lower(), f[2].strip())
    text_by = {}
    for k, v in texts.items():
        for var in variants(k):
            text_by.setdefault(var, v)

    names = set()
    for p in glob.glob(os.path.join(MODELS, "mesh-*.json")):
        for part in json.load(open(p, encoding="utf-8"))["parts"]:
            names.add(part["base"])
            names.update(part["path"])

    out = {}
    for n in sorted(names):
        la = next((latin[v] for v in variants(n) if v in latin), None)
        tx = next((text_by[v] for v in variants(n) if v in text_by), None)
        entry = {}
        if la:
            entry["la"] = la
        if tx:
            d = clean_def(tx)
            if len(d) > 40:
                entry["def"] = d
        if entry:
            out[n.lower()] = entry
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, separators=(",", ":"))
    print(f"{len(names)} names, {sum('la' in e for e in out.values())} latin, "
          f"{sum('def' in e for e in out.values())} definitions, {os.path.getsize(OUT)/1e6:.1f} MB")


if __name__ == "__main__":
    main()
