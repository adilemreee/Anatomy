"""Helpers for the Turkish part dictionary (Anatomy/Content/terms.json).

Every 3D part and model group gets a Turkish name, a corrected Latin name
where Z-Anatomy's is misspelled, and a short Turkish description:

    T("Femur", "Uyluk kemiği", "Os femoris", "Vücudun en uzun ...")

`la=None` keeps the Latin from the glossary (TA2 via Z-Anatomy).
"""

TERMS = {}


def T(en, tr, la=None, d=""):
    key = en.lower()
    assert key not in TERMS or TERMS[key]["tr"] == tr, f"duplicate term with a different name: {en}"
    entry = {"tr": tr}
    if la:
        entry["la"] = la
    if d:
        entry["d"] = d
    TERMS[key] = entry


ORD_EN = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
ORD_TR = ["1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.", "11.", "12."]
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
FINGER_TR = ["başparmak", "işaret parmağı", "orta parmak", "yüzük parmağı", "serçe parmak"]
TOE_TR = ["başparmak", "2. parmak", "3. parmak", "4. parmak", "serçe parmak"]
