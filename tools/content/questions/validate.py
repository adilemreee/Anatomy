#!/usr/bin/env python3
"""Checks the question bank: entry ids exist, answers are balanced, and
prints counts per system and group."""
import collections
import glob
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
content = os.path.join(ROOT, "Anatomy", "Content")

entries = set()
for p in glob.glob(os.path.join(content, "atlas-*.json")):
    if p.endswith("atlas-systems.json") or os.path.basename(p).count(".") > 1:
        continue  # the systems list and translations
    entries.update(e["id"] for e in json.load(open(p, encoding="utf-8"))["entries"])

total, bad, positions = 0, [], collections.Counter()
for p in sorted(glob.glob(os.path.join(content, "questions-*.json"))):
    if os.path.basename(p).count(".") > 1:
        continue
    data = json.load(open(p, encoding="utf-8"))
    groups = collections.Counter(q["group"] for q in data["questions"])
    total += len(data["questions"])
    for q in data["questions"]:
        positions["ABCDE"[q["answer"]]] += 1
        for e in q.get("entries", []):
            if e not in entries:
                bad.append((q["id"], e))
    print(f"{data['system']:15} {len(data['questions']):4}  " + ", ".join(f"{g}: {n}" for g, n in groups.items()))
print("total", total, "answer positions", dict(sorted(positions.items())))
for qid, e in bad:
    print("UNKNOWN ENTRY", qid, e)
