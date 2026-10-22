"""Splits a translation source module into per-language JSON files.

A source module (tools/i18n/content/src/<name>.py) defines KIND ("atlas",
"extra", "questions" or "terms"), SYSTEM and E = {id: {lang: value}}. Atlas
values are [name, summary, [facts], [[section title, body]], [clinical], [tus],
[aliases]]; extra values are {"facts": [...], "sections": [...], "clinical":
[...], "tus": [...], "aliases": [...]}, the items an entry gained after it was
translated, appended in order; question values are [stem, [options],
explanation, [notes]]; term values are [name, description].

    python3 tools/i18n/content/split.py src/atlas_skeletal_00.py
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main(path):
    spec = importlib.util.spec_from_file_location("src", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    name = os.path.splitext(os.path.basename(path))[0]
    langs = {}
    for key, per in mod.E.items():
        for lang, v in per.items():
            if mod.KIND == "atlas":
                item = {"tr": v[0], "summary": v[1], "facts": v[2], "sections": v[3], "clinical": v[4], "tus": v[5],
                        "aliases": v[6] if len(v) > 6 else []}
            elif mod.KIND == "questions":
                item = {"stem": v[0], "options": v[1], "explanation": v[2], "notes": v[3] if len(v) > 3 else []}
            else:
                item = v
            langs.setdefault(lang, {})[key] = item
    prefix = {"atlas": f"atlas-{getattr(mod, 'SYSTEM', '')}", "extra": f"extra-{getattr(mod, 'SYSTEM', '')}", "questions": f"questions-{getattr(mod, 'SYSTEM', '')}", "terms": "terms"}[mod.KIND]
    for lang, items in langs.items():
        os.makedirs(os.path.join(HERE, lang), exist_ok=True)
        with open(os.path.join(HERE, lang, f"{prefix}-{name}.json"), "w", encoding="utf-8") as fh:
            json.dump(items, fh, ensure_ascii=False, indent=1)
    print(name, {lang: len(items) for lang, items in langs.items()})


if __name__ == "__main__":
    for p in sys.argv[1:]:
        main(p if os.path.isabs(p) else os.path.join(HERE, p) if not os.path.exists(p) else p)
