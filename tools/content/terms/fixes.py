"""Last corrections, applied after every other term module: Turkish names
that were left in English and Latin names missing from or misspelled in
the glossary."""
from common import TERMS


def fix(en, tr=None, la=None):
    entry = TERMS.setdefault(en.lower(), {"tr": tr or en})
    if tr:
        entry["tr"] = tr
    if la:
        entry["la"] = la


# Turkish names that were still the English ones.
fix("Abdominal aorta", tr="Karın aortu (aorta abdominalis)")
fix("Glenoid labrum", tr="Glenoid dudak (labrum glenoidale)")
fix("Lateral fasciculus proprius", tr="Yan özgün demet (fasciculus proprius lateralis)")
fix("Subdeltoid bursa", tr="Deltoid altı bursa")
fix("Suprapatellar bursa", tr="Patella üstü bursa")
fix("Pronator teres", tr="Yuvarlak pronator kas")
fix("Levator ani", tr="Anüs kaldırıcı kas (m. levator ani)")
fix("Glans penis", tr="Penis başı (glans penis)")
fix("Dorsal striatum", tr="Dorsal striatum (çizgili cisim)")
fix("Zona orbicularis", tr="Kalça eklemi halka bağı (zona orbicularis)")

# Latin names the glossary lacks.
fix("Superior deep lateral nodes", tr="Üst derin yan boyun lenf düğümleri",
    la="Nodi lymphoidei cervicales laterales profundi superiores")
fix("Grey matter of medulla oblongata.", tr="Medulla oblongata'nın gri cevheri", la="Substantia grisea medullae oblongatae")
fix("Grey matter of medulla oblongata", tr="Medulla oblongata'nın gri cevheri", la="Substantia grisea medullae oblongatae")
fix("Nervous system & Sense organs", tr="Sinir sistemi ve duyu organları", la="Systema nervosum et organa sensuum")
fix("Sense organs", tr="Duyu organları", la="Organa sensuum")
fix("Female genital system", tr="Kadın genital sistemi", la="Systema genitale femininum")
fix("Female internal genitalia", tr="Kadın iç genital organları", la="Organa genitalia feminina interna")

# Latin names misspelled or abbreviated in the glossary.
fix("Facet for calcaneonavicular part of bifurcate ligament", la="Facies articularis partis calcaneonavicularis ligamenti bifurcati")
fix("Lamina of thyroid cartilage", la="Lamina cartilaginis thyroideae")
fix("Medial compartment of thigh", la="Compartimentum femoris mediale")
fix("Lateral supracondylar ridge", la="Crista supracondylaris lateralis")
fix("Medial supracondylar ridge", la="Crista supracondylaris medialis")
fix("Posterior segment of liver (I)", la="Segmentum posterius hepatis (I), lobus caudatus")
