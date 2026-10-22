#!/usr/bin/env python3
"""Checks the atlas content: unknown related ids and model names that do not
match any 3D part (by base name or ancestor group)."""
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
content = os.path.join(ROOT, "Anatomy", "Content")
models = os.path.join(ROOT, "Anatomy", "Resources", "Models")

names = set()
for p in glob.glob(os.path.join(models, "mesh-*.json")):
    for part in json.load(open(p, encoding="utf-8"))["parts"]:
        names.add(part["base"].lower())
        names.update(n.lower() for n in part["path"])

systems = {s["id"] for s in json.load(open(os.path.join(content, "atlas-systems.json"), encoding="utf-8"))}
entries = {}
for p in sorted(glob.glob(os.path.join(content, "atlas-*.json"))):
    if p.endswith("atlas-systems.json") or os.path.basename(p).count(".") > 1:
        continue  # the systems list and translations
    data = json.load(open(p, encoding="utf-8"))
    assert data["system"] in systems, p
    for e in data["entries"]:
        if e["id"] in entries:
            print("DUPLICATE", e["id"], p)
        entries[e["id"]] = (data["system"], e)

bad_models, bad_related, no_model = [], [], 0
for eid, (sys_, e) in entries.items():
    for m in e["models"]:
        if m.lower() not in names:
            bad_models.append((eid, m))
    if not e["models"]:
        no_model += 1
    for r in e["related"]:
        if r not in entries:
            bad_related.append((eid, r))

print(f"{len(entries)} entries, {no_model} without 3D model")
for k, v in sorted({s for s, _ in entries.values()}.__iter__().__class__.__mro__ and [] or []):
    pass
by = {}
for s, _ in entries.values():
    by[s] = by.get(s, 0) + 1
print(by)
if bad_models:
    print("UNKNOWN MODELS:")
    for x in bad_models:
        print("  ", x)
if bad_related and "--related" in sys.argv:
    print("UNKNOWN RELATED:")
    for x in bad_related:
        print("  ", x)
else:
    print(f"{len(bad_related)} unknown related ids (use --related)")
