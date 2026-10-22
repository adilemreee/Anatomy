"""Helpers for authoring the question bank.

Every question is original. A system module builds a list with `Q(...)` and
calls `write(system, questions)`; the output is
Anatomy/Content/questions-<system>.json.

    Q(level, group, stem, answer, wrong, explain, notes=None, e=(), m=())

level   "b" basic, "f" faculty, "t" TUS; add "v" for a clinical vignette
        ("bv", "fv", "tv")
group   one of the system's group headings (atlas-systems.json)
answer  the correct option; wrong: the four distractors
notes   optional, one short note per distractor (why it is wrong)
e       atlas entry ids the question is about; m: 3D model names to show

Options are shuffled with a seed taken from the stem, so a question keeps
its option order (and its id) between builds.
"""
import hashlib
import json
import os
import random

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(ROOT, "Anatomy", "Content")

PREFIX = {
    "skeletal": "sk", "articular": "ar", "muscular": "mu", "nervous": "ne", "cardiovascular": "cv",
    "respiratory": "re", "digestive": "di", "urinary": "ur", "reproductive": "rp", "endocrine": "en",
    "lymphatic": "ly", "integumentary": "in", "senses": "se",
}


def Q(level, group, stem, answer, wrong, explain, notes=None, e=(), m=()):
    assert level in ("b", "f", "t", "bv", "fv", "tv"), level
    assert len(wrong) == 4, (stem, wrong)
    assert notes is None or len(notes) == 4, stem
    return {
        "level": {"b": "basic", "f": "faculty", "t": "tus"}[level[0]],
        "clinical": level.endswith("v"),
        "group": group,
        "stem": " ".join(stem.split()),
        "answer": answer.strip(),
        "wrong": [w.strip() for w in wrong],
        "explanation": " ".join(explain.split()),
        "wrongNotes": [" ".join(n.split()) for n in notes] if notes else None,
        "entries": list(e),
        "models": list(m),
    }


def write(system, questions):
    systems = json.load(open(os.path.join(OUT, "atlas-systems.json"), encoding="utf-8"))
    groups = next(s["groups"] for s in systems if s["id"] == system)
    out, ids = [], set()
    for q in questions:
        assert q["group"] in groups, f"{system}: unknown group {q['group']!r}"
        opts = [q["answer"]] + q["wrong"]
        assert len({o.lower() for o in opts}) == 5, f"duplicate options: {q['stem']}"
        notes = [""] + (q["wrongNotes"] or ["", "", "", ""])
        digest = hashlib.sha1(q["stem"].encode("utf-8")).hexdigest()
        qid = f"{PREFIX[system]}-{digest[:8]}"
        assert qid not in ids, f"duplicate stem: {q['stem']}"
        ids.add(qid)
        order = list(range(5))
        random.Random(digest).shuffle(order)
        item = {
            "id": qid, "group": q["group"], "level": q["level"], "clinical": q["clinical"],
            "stem": q["stem"],
            "options": [opts[i] for i in order],
            "answer": order.index(0),
            "explanation": q["explanation"],
        }
        if q["wrongNotes"]:
            item["notes"] = [notes[i] for i in order]
        if q["entries"]:
            item["entries"] = q["entries"]
        if q["models"]:
            item["models"] = q["models"]
        out.append(item)
    path = os.path.join(OUT, f"questions-{system}.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"system": system, "questions": out}, fh, ensure_ascii=False, indent=1)
    tus = sum(1 for q in out if q["level"] == "tus")
    clinical = sum(1 for q in out if q["clinical"])
    basic = sum(1 for q in out if q["level"] == "basic")
    print(f"{system}: {len(out)} questions ({basic} basic, {tus} TUS, {clinical} clinical)")
