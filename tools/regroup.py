"""Groups Z-Anatomy leaves out of its hierarchy.

Z-Anatomy files the bones of the hand straight under "Bones of free part of
upper limb" (the foot has "Bones of foot" with tarsal, metatarsal bones and
phalanges). The atlas needs the hand as one structure too (parts browser,
search, selection levels), so its bones get the same three groups:

    ... / Bones of free part of upper limb / Bones of hand / Carpal bones
                                                           / Metacarpal bones
                                                           / Phalanges of hand

export_zanatomy.py applies this to every part; run on its own it patches the
shipped manifests in place (it is idempotent):

    python3 tools/regroup.py
"""
import json
import os
import re

CARPALS = {"Scaphoid bone", "Lunate bone", "Triquetrum bone", "Pisiform bone",
           "Trapezium bone", "Trapezoid bone", "Capitate bone", "Hamate bone"}
LIMB = "Bones of free part of upper limb"


def hand_group(name):
    if name in CARPALS:
        return "Carpal bones"
    if name.endswith("metacarpal bone"):
        return "Metacarpal bones"
    if re.fullmatch(r"(Distal|Middle|Proximal) phalanx of \w+ finger of hand", name):
        return "Phalanges of hand"
    return None


def regroup(base, path):
    """The path of a part named `base`; attachment patches carry their bone
    as the last path element."""
    if LIMB not in path or "Bones of hand" in path:
        return path
    group = next((g for g in map(hand_group, [base] + path[::-1]) if g), None)
    if group is None:
        return path
    k = path.index(LIMB) + 1
    return path[:k] + ["Bones of hand", group] + path[k:]


if __name__ == "__main__":
    models = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Anatomy", "Resources", "Models")
    for system in ("skeletal", "insertions"):
        fn = os.path.join(models, f"mesh-{system}.json")
        manifest = json.load(open(fn))
        changed = 0
        for part in manifest["parts"]:
            path = regroup(part["base"], part["path"])
            if path != part["path"]:
                part["path"] = path
                changed += 1
        with open(fn, "w", encoding="utf-8") as fh:
            json.dump(manifest, fh, ensure_ascii=False, separators=(",", ":"))
        print(f"{system}: {changed} parts regrouped")
