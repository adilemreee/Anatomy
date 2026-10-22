"""Translated content: atlas entries, the question bank, the 3D part
dictionary and the bone landmarks, built from the Turkish originals and the
translation files in tools/i18n/content/<lang>/.

    python3 tools/i18n/content.py source atlas skeletal 0 12   # Turkish text to translate
    python3 tools/i18n/content.py build                       # writes Anatomy/Content/*.<lang>.json
    python3 tools/i18n/content.py status                      # what is still missing

Translation files (JSON, any number per kind, merged by id):
  atlas-<system>*.json     {id: {"tr", "summary", "facts": [values…], "sections": [[title, body]…],
                                 "clinical": […], "tus": […], "aliases": […]}}
  extra-<system>*.json     {id: {"facts", "sections", "clinical", "tus", "aliases"}}: items added
                           to an entry after it was translated, appended in file order
  questions-<system>*.json {id: {"stem", "options": [5, in file order], "explanation", "notes": [5]}}
  terms*.json              {english key: [name, description]}
  shared.json              {"labels": {fact label: …}, "groups": {group: …},
                            "systems": {id: {"tr", "summary", "intro"}}}
The "tr" field keeps its name in translated files and holds the name in that language.
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CONTENT = os.path.join(ROOT, "Anatomy", "Content")
SOURCES = os.path.join(HERE, "content")
LANGS = ["en", "fr", "de", "es"]
SYSTEMS = ["skeletal", "articular", "muscular", "cardiovascular"]
MODELS = os.path.join(ROOT, "Anatomy", "Resources", "Models")


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save(path, data):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)


def merged(lang, pattern):
    out = {}
    for path in sorted(glob.glob(os.path.join(SOURCES, lang, pattern))):
        out.update(load(path))
    return out


def shared(lang):
    path = os.path.join(SOURCES, lang, "shared.json")
    return load(path) if os.path.exists(path) else {"labels": {}, "groups": {}, "systems": {}}


def used_terms():
    """English keys of the 3D parts, groups and bone labels in scope."""
    names = set()
    for layer in ["skeletal", "joints", "muscular", "insertions", "cardiovascular"]:
        for p in load(os.path.join(MODELS, f"mesh-{layer}.json"))["parts"]:
            names.add(p["base"].lower())
            names.update(x.lower() for x in p["path"])
    for label in load(os.path.join(MODELS, "labels.json"))["labels"]:
        if label["system"] == "skeletal":
            n = label["name"].strip()
            if n.startswith("(") and n.endswith(")"):
                n = n[1:-1].strip()
            names.add(n.lower())
    terms = load(os.path.join(CONTENT, "terms.json"))
    return [k for k in sorted(terms) if k in names]


# MARK: source dumps for translating

def source(kind, system, start, count):
    if kind == "atlas":
        entries = load(os.path.join(CONTENT, f"atlas-{system}.json"))["entries"][start:start + count]
        for e in entries:
            print(f"## {e['id']} | {e['tr']} | {e['la']} | {e['en']}")
            print("S:", e["summary"])
            for label, value in e["facts"]:
                print(f"F: {label} = {value}")
            for title, body in e["sections"]:
                print(f"SEC: {title} :: {body}")
            for c in e["clinical"]:
                print("C:", c)
            for t in e["tus"]:
                print("T:", t)
            if e["aliases"]:
                print("A:", " | ".join(e["aliases"]))
    elif kind == "questions":
        qs = load(os.path.join(CONTENT, f"questions-{system}.json"))["questions"][start:start + count]
        for q in qs:
            print(f"## {q['id']} [{q['group']}]")
            print("Q:", q["stem"])
            for i, o in enumerate(q["options"]):
                print(f"O{i}{'*' if i == q['answer'] else ''}: {o}")
            print("E:", q["explanation"])
            for i, n in enumerate(q.get("notes", [])):
                if n:
                    print(f"N{i}: {n}")
    elif kind == "terms":
        terms = load(os.path.join(CONTENT, "terms.json"))
        for key in used_terms()[start:start + count]:
            t = terms[key]
            print(f"{key} | {t['tr']} | {t.get('la') or ''} | {t.get('d') or ''}")


# MARK: build

def build_atlas(lang, report):
    tr = merged(lang, "atlas-*.json")
    for path in sorted(glob.glob(os.path.join(SOURCES, lang, "extra-*.json"))):
        for id_, add in load(path).items():
            if id_ not in tr:
                report.append(f"{lang} extra for untranslated {id_}")
                continue
            t = tr[id_] = dict(tr[id_])
            for key in ("facts", "sections", "clinical", "tus", "aliases"):
                t[key] = t.get(key, []) + add.get(key, [])
    common = shared(lang)
    labels, groups, systems = common["labels"], common["groups"], common["systems"]
    for system in SYSTEMS:
        base = load(os.path.join(CONTENT, f"atlas-{system}.json"))
        out = []
        for e in base["entries"]:
            t = tr.get(e["id"])
            if not t:
                report.append(f"{lang} atlas {system}: missing {e['id']}")
                continue
            item = dict(e)
            item["tr"] = t["tr"]
            item["summary"] = t["summary"]
            item["group"] = groups.get(e["group"], e["group"])
            if e["group"] not in groups:
                report.append(f"{lang}: group {e['group']!r}")
            values = t.get("facts", [])
            if len(values) != len(e["facts"]):
                report.append(f"{lang} atlas {e['id']}: {len(values)} facts for {len(e['facts'])}")
            item["facts"] = [[label, values[i] if i < len(values) else value, labels.get(label, label)]
                             for i, (label, value) in enumerate(e["facts"])]
            for label, _ in e["facts"]:
                if label not in labels:
                    report.append(f"{lang}: label {label!r}")
            for key in ("sections", "clinical", "tus"):
                item[key] = t.get(key, [])
                if len(item[key]) != len(e[key]):
                    report.append(f"{lang} atlas {e['id']}: {len(item[key])} {key} for {len(e[key])}")
            item["aliases"] = t.get("aliases", [])
            out.append(item)
        if out:
            save(os.path.join(CONTENT, f"atlas-{system}.{lang}.json"), {"system": system, "entries": out})

    base = load(os.path.join(CONTENT, "atlas-systems.json"))
    out = []
    for s in base:
        item = dict(s)
        t = systems.get(s["id"])
        if t:
            item.update({k: t[k] for k in ("tr", "summary", "intro") if k in t})
        elif s["id"] in SYSTEMS:
            report.append(f"{lang}: system {s['id']}")
        item["groups"] = [groups.get(g, g) for g in s["groups"]]
        out.append(item)
    save(os.path.join(CONTENT, f"atlas-systems.{lang}.json"), out)


def build_questions(lang, report):
    tr = merged(lang, "questions-*.json")
    groups = shared(lang)["groups"]
    for system in SYSTEMS:
        base = load(os.path.join(CONTENT, f"questions-{system}.json"))
        out = []
        for q in base["questions"]:
            t = tr.get(q["id"])
            if not t:
                report.append(f"{lang} questions {system}: missing {q['id']}")
                continue
            item = dict(q)
            item["group"] = groups.get(q["group"], q["group"])
            item["stem"] = t["stem"]
            item["options"] = t["options"]
            item["explanation"] = t["explanation"]
            if len(t["options"]) != len(q["options"]):
                report.append(f"{lang} {q['id']}: options")
            if "notes" in q:
                item["notes"] = t.get("notes") or ["" for _ in q["notes"]]
            out.append(item)
        if out:
            save(os.path.join(CONTENT, f"questions-{system}.{lang}.json"), {"system": system, "questions": out})


def build_terms(lang, report):
    tr = merged(lang, "terms*.json")
    base = load(os.path.join(CONTENT, "terms.json"))
    out = {}
    for key, t in base.items():
        if key in tr:
            name, desc = tr[key]
            out[key] = {"tr": name, "la": t.get("la"), "d": desc or None}
        else:
            # Out of scope parts keep their English name; never Turkish.
            out[key] = {"tr": key[:1].upper() + key[1:], "la": t.get("la"), "d": None}
    missing = [k for k in used_terms() if k not in tr]
    if missing:
        report.append(f"{lang} terms: {len(missing)} missing, first {missing[:3]}")
    save(os.path.join(CONTENT, f"terms.{lang}.json"), out)

    # Landmarks: the same list with the translated names and descriptions.
    landmarks = load(os.path.join(CONTENT, "landmarks.json"))
    for item in landmarks:
        t = out.get(item["name"].lower())
        if t:
            item["tr"] = t["tr"]
            item["d"] = t["d"] or ""
    save(os.path.join(CONTENT, f"landmarks.{lang}.json"), landmarks)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "source":
        kind, system = sys.argv[2], sys.argv[3]
        start, count = int(sys.argv[4]), int(sys.argv[5]) if len(sys.argv) > 5 else 10
        source(kind, system, start, count)
        return
    report = []
    for lang in LANGS:
        os.makedirs(os.path.join(SOURCES, lang), exist_ok=True)
        build_atlas(lang, report)
        build_questions(lang, report)
        build_terms(lang, report)
    status_only = len(sys.argv) > 1 and sys.argv[1] == "status"
    seen = set()
    for line in report:
        if line not in seen:
            seen.add(line)
            if not status_only or "missing" not in line:
                print(line)
    for lang in LANGS:
        n = sum(1 for line in seen if line.startswith(lang) and "missing" in line)
        print(f"{lang}: {n} missing lines")


if __name__ == "__main__":
    main()
