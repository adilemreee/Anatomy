"""Checks the App Store listing in tools/i18n/appstore.md against the
App Store Connect limits.

    python3 tools/i18n/check_appstore.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIMITS = {"Name": 30, "Subtitle": 30, "Promotional text": 170, "Keywords": 100, "Description": 4000, "What's New": 4000}


def main():
    text = open(os.path.join(HERE, "appstore.md"), encoding="utf-8").read()
    problems = 0
    for block in re.split(r"\n## ", text)[1:]:
        lang = block.splitlines()[0].strip()
        fields = dict(re.findall(r"### (.+?)\n(.*?)(?=\n### |\n---|\Z)", block, re.S))
        for field, limit in LIMITS.items():
            value = fields.get(field, "").strip()
            mark = "ok" if 0 < len(value) <= limit else "PROBLEM"
            if field == "Keywords" and (", " in value or " ," in value):
                mark = "PROBLEM (spaces after commas)"
            if mark != "ok":
                problems += 1
            print(f"{lang:28} {field:17} {len(value):5}/{limit:<5} {mark}")
    print("problems:", problems)
    return problems


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
