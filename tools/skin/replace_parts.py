"""Copies parts by name from one pack into another of the same system: the
breast placed again by fit_breast.py goes into the pack the later steps
(fit_inside.py, fit_bronchi.py) have made, which leave it alone.

    python3 tools/skin/replace_parts.py <from dir> <into dir> <system> <name prefix> [...]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from packedit import load, save  # noqa: E402

src, dst, system, *prefixes = sys.argv[1:]
_, fresh, _, _ = load(src, system)
by_name = {p['info']['name']: p for p in fresh}
manifest, parts, lo, hi = load(dst, system)
replaced = 0
for i, p in enumerate(parts):
    name = p['info']['name']
    if name.startswith(tuple(prefixes)) and name in by_name:
        parts[i] = by_name[name]
        replaced += 1
save(dst, system, manifest, parts, lo, hi)
print(f'{system}: {replaced} parts replaced', flush=True)
