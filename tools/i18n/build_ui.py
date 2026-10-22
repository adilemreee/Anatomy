"""Fills Anatomy/Localizable.xcstrings and InfoPlist.xcstrings from the
interface translations in tools/i18n/ui/<lang>.py.

Each module defines T = {Turkish key: translation}; a translation may be a
dict of plural forms ({"one": …, "other": …}) for a key with one number.

    python3 tools/i18n/build_ui.py        # writes the catalogs, reports gaps
"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CATALOG = os.path.join(ROOT, "Anatomy", "Localizable.xcstrings")
INFOPLIST = os.path.join(ROOT, "Anatomy", "InfoPlist.xcstrings")
LANGS = ["en", "fr", "de", "es"]

# Keys that are identifiers rather than Turkish text, used where one Turkish
# word has two meanings (defaultValue in the code); their Turkish text.
TURKISH = {
    "flashcard.again": "Tekrar",
    "view.front": "Ön",
    "view.left": "Sol",
    "view.back": "Arka",
    "view.right": "Sağ",
    "streak.oneDay": "gün seri",
}

# App name on the home screen, per language.
DISPLAY_NAME = {"tr": "Anatomi Atlası", "en": "Anatomy Atlas", "fr": "Atlas Anatomie", "de": "Anatomie Atlas", "es": "Atlas Anatomía"}


def load(lang):
    path = os.path.join(HERE, "ui", f"{lang}.py")
    spec = importlib.util.spec_from_file_location(f"ui_{lang}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.T


SPEC = re.compile(r"%(?:\d+\$)?(@|lld|ld|d|f|\.\d+f|%)")


def specs(text):
    """Placeholder types in order of their position numbers."""
    found = []
    auto = 0
    for m in re.finditer(r"%(?:(\d+)\$)?(@|lld|ld|d|\.\d+f|f|%)", text):
        if m.group(2) == "%":
            continue
        if m.group(1):
            found.append((int(m.group(1)), m.group(2)))
        else:
            auto += 1
            found.append((auto, m.group(2)))
    return sorted(found)


def unit(value):
    return {"stringUnit": {"state": "translated", "value": value}}


def main():
    catalog = json.load(open(CATALOG, encoding="utf-8"))
    strings = catalog["strings"]
    problems = 0
    for lang in LANGS:
        table = load(lang)
        unknown = [k for k in table if k not in strings]
        missing = [k for k in strings if k and k not in table]
        for k in unknown:
            print(f"{lang}: unknown key {k!r}")
        for k in missing:
            print(f"{lang}: missing {k!r}")
        problems += len(unknown) + len(missing)
        for key, value in table.items():
            if key not in strings:
                continue
            if isinstance(value, dict) and len(specs(key)) != 1:
                print(f"{lang}: plural forms need exactly one placeholder: {key!r}")
                problems += 1
            forms = value if isinstance(value, dict) else {"other": value}
            for form in forms.values():
                if specs(form) != specs(key) and not (len(specs(key)) == 1 and form == ""):
                    print(f"{lang}: placeholders differ in {key!r} → {form!r}")
                    problems += 1
            entry = strings[key].setdefault("localizations", {})
            if isinstance(value, dict):
                entry[lang] = {"variations": {"plural": {f: unit(v) for f, v in value.items()}}}
            else:
                entry[lang] = unit(value)
    # Turkish is the source, but English is the fallback for other device
    # languages (CFBundleDevelopmentRegion), so Turkish is written out too.
    for key, item in strings.items():
        if key:
            item.setdefault("localizations", {})["tr"] = unit(TURKISH.get(key, key))
    with open(CATALOG, "w", encoding="utf-8") as fh:
        json.dump(catalog, fh, ensure_ascii=False, indent=2, separators=(",", " : "))
        fh.write("\n")

    info = {"sourceLanguage": "tr", "strings": {}, "version": "1.0"}
    for key in ("CFBundleDisplayName", "CFBundleName"):
        info["strings"][key] = {"comment": "App name on the home screen", "extractionState": "manual",
                                "localizations": {lang: unit(name) for lang, name in DISPLAY_NAME.items()}}
    with open(INFOPLIST, "w", encoding="utf-8") as fh:
        json.dump(info, fh, ensure_ascii=False, indent=2, separators=(",", " : "))
        fh.write("\n")
    print("problems:", problems)
    return problems


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
