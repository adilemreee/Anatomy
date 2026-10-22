"""Bone landmarks for the questions and flashcards.

Reads the specimen viewer's feature labels (Resources/Models/labels.json),
resolves each label's bone to the atlas entry that describes it (the most
specific entry listing the part, else its closest ancestor group, the same
rule as AtlasStore) and writes Anatomy/Content/landmarks.json with the
Turkish name, Latin name and description from terms.json.

    python3 tools/content/landmarks.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTENT = os.path.join(ROOT, "Anatomy", "Content")
MODELS = os.path.join(ROOT, "Anatomy", "Resources", "Models")
SYSTEMS = ["skeletal", "articular", "muscular"]

# Features every vertebra (or every bone of a series) has: the labels sit on
# one sample bone, so "which bone is it on" would have several answers.
GENERIC = {
    "Annular epiphysis", "Inferior articular facet of vertebra", "Inferior vertebral notch", "Intervertebral foramen",
    "Intervertebral surface", "Lamina of vertebral arch", "Pedicle of vertebral arch", "Spinous process",
    "Superior articular facet of vertebra", "Superior articular process of vertebra", "Superior vertebral notch",
    "Transverse process", "Lateral part of transverse process", "Vertebra", "Vertebral arch", "Vertebral body",
    "Vertebral foramen", "Pars interarticularis of vertebral arch", "Cervical vertebra", "Thoracic vertebra", "Rib",
    "Uncinate process of first thoracic vertebra",
}

# Features the label puts on one bone although neighbouring bones share them
# (the groove of the middle meningeal artery runs over four skull bones):
# kept for the cards, left out of "which bone" questions.
SHARED = {
    "Groove for middle meningeal artery", "Groove for transverse sinus", "Groove for sigmoid sinus",
    "Groove for superior sagittal sinus", "Superior temporal line", "Inferior temporal line", "Temporal line",
}


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    entries = [e for s in SYSTEMS for e in load(os.path.join(CONTENT, f"atlas-{s}.json"))["entries"]]
    owner = {}
    for e in entries:
        for m in e["models"]:
            key = m.lower()
            if key not in owner or len(e["models"]) < len(owner[key]["models"]):
                owner[key] = e
    paths = {p["base"]: p["path"] for p in load(os.path.join(MODELS, "mesh-skeletal.json"))["parts"]}
    terms = load(os.path.join(CONTENT, "terms.json"))
    glossary = load(os.path.join(ROOT, "Anatomy", "Resources", "glossary.json"))

    def entry_for(base):
        for name in [base] + list(reversed(paths.get(base, []))):
            if name.lower() in owner:
                return owner[name.lower()]
        return None

    out, skipped = [], []
    for label in load(os.path.join(MODELS, "labels.json"))["labels"]:
        if label["system"] != "skeletal":
            continue
        name = label["name"].strip()
        # "(Third trochanter)": features that are not always present
        if name.startswith("(") and name.endswith(")"):
            name = name[1:-1].strip()
        base = label["owner"].removesuffix(".r").removesuffix(".l")
        entry = entry_for(base)
        term = terms.get(name.lower())
        # the bone's own label ("Femur" on the femur) is not a landmark
        if not entry or not term or not term.get("tr") or name.lower() == base.lower() or name in GENERIC:
            skipped.append((name, base))
            continue
        out.append({
            "name": name,
            "tr": term["tr"],
            "la": term.get("la") or (glossary.get(name.lower()) or {}).get("la") or "",
            "d": term.get("d") or "",
            "entry": entry["id"],
            "part": base,
            "shared": name in SHARED,
        })
    # How often the atlas and the question bank mention a landmark: the
    # specimen viewer labels the frequently mentioned ones first.
    texts = []
    for e in entries:
        texts += [e["summary"]] + [v for _, v in e["facts"]] + [b for _, b in e["sections"]] + e["tus"] + e["clinical"]
    for system in SYSTEMS:
        for q in load(os.path.join(CONTENT, f"questions-{system}.json"))["questions"]:
            texts += [q["stem"], q["explanation"]] + q["options"]
    corpus = "\n".join(texts).casefold()
    for item in out:
        # the Latin name and the Turkish name without its bracketed note
        # ("trochlea" alone would count the orbit's trochlea too)
        names = {item["la"].casefold(), item["tr"].split("(")[0].strip().casefold()}
        item["rank"] = sum(corpus.count(n) for n in names if len(n) >= 6)
    with open(os.path.join(CONTENT, "landmarks.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print(f"landmarks: {len(out)} written, {len(skipped)} skipped")
    for s in skipped:
        print("   skipped", s)


if __name__ == "__main__":
    main()
