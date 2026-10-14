"""Builds Anatomy/Content/terms.json, the Turkish dictionary of every 3D part
and model group, and reports parts that are still missing.

    python3 tools/content/terms/build.py [--strict]
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, HERE)

from common import TERMS  # noqa: E402
import skeletal, joints, muscular, insertions, visceral, lymphoid, regions, nervous, cardiovascular  # noqa: E402,F401
import groups  # noqa: E402,F401
import features  # noqa: E402,F401
import extras  # noqa: E402,F401
import fixes  # noqa: E402,F401
import features_desc  # noqa: E402,F401

missing = []
for path in sorted(glob.glob(os.path.join(ROOT, "Anatomy", "Resources", "Models", "mesh-*.json"))):
    manifest = json.load(open(path))
    for part in manifest["parts"]:
        for name in [part["base"]] + part["path"]:
            if name.lower() not in TERMS:
                missing.append((manifest["system"], name))
missing = sorted(set(missing))
if missing:
    print(f"{len(missing)} names without a Turkish term:")
    for system, name in missing:
        print(f"  {system:15s} {name}")
    if "--strict" in sys.argv:
        sys.exit(1)

out = os.path.join(ROOT, "Anatomy", "Content", "terms.json")
with open(out, "w", encoding="utf-8") as fh:
    json.dump(dict(sorted(TERMS.items())), fh, ensure_ascii=False, separators=(",", ":"))
print(f"wrote {len(TERMS)} terms to {os.path.relpath(out, ROOT)}")
