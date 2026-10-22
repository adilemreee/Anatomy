"""Helpers for authoring the atlas content files.

Each system module calls `E(...)` for every entry and `write(system, entries)`
at the end. The output is Anatomy/Content/atlas-<system>.json.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "Anatomy", "Content")


def E(id, tr, la, en, group, region, summary, facts=(), sections=(), clinical=(), related=(), models=(), aliases=(), tus=()):
    return {
        "id": id, "tr": tr, "la": la, "en": en, "group": group, "region": region,
        "summary": summary.strip(),
        "facts": [list(f) for f in facts],
        "sections": [list(s) for s in sections],
        "clinical": list(clinical),
        "tus": list(tus),
        "related": list(related),
        "models": list(models),
        "aliases": list(aliases),
    }


def write(system, entries, extra=None):
    """`extra` maps an entry id to more facts, sections, clinical and exam
    notes for it; they go after everything else so the translations of the
    earlier items keep their positions."""
    from tus_notes import NOTES
    for e in entries:
        for note in NOTES.get(e["id"], []):
            if note not in e["tus"]:
                e["tus"].append(note)
    by_id = {e["id"]: e for e in entries}
    for id_, add in (extra or {}).items():
        assert id_ in by_id, f"extra for unknown entry {id_}"
        e = by_id[id_]
        e["facts"] += [list(f) for f in add.get("facts", ())]
        e["sections"] += [list(s) for s in add.get("sections", ())]
        for key in ("clinical", "tus", "aliases"):
            e[key] += list(add.get(key, ()))
    ids = [e["id"] for e in entries]
    dup = {i for i in ids if ids.count(i) > 1}
    assert not dup, f"duplicate ids: {dup}"
    path = os.path.join(OUT, f"atlas-{system}.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"system": system, "entries": entries}, fh, ensure_ascii=False, indent=1)
    print(f"{system}: {len(entries)} entries")
