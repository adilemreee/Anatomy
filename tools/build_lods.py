"""Adds levels of detail to every atlas pack (see tools/lod/lodgen.cpp).

    python3 tools/build_lods.py <meshoptimizer checkout> [--models DIR] [system ...]

Builds the lodgen tool against meshoptimizer (MIT, github.com/zeux/meshoptimizer),
writes each pack's material runs from its manifest and rewrites the packs in
Anatomy/Resources/Models as "ANT3". Run it after tools/bake_ao.swift.
"""
import glob
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS = os.path.join(ROOT, "Anatomy", "Resources", "Models")
MESHOPT = os.path.abspath(sys.argv[1])
rest = sys.argv[2:]
if rest[:1] == ["--models"]:
    MODELS = os.path.abspath(rest[1])
    rest = rest[2:]
SYSTEMS = rest or [os.path.basename(p)[5:-5] for p in sorted(glob.glob(os.path.join(MODELS, "mesh-*.json")))]

work = tempfile.mkdtemp(prefix="lodgen-")
tool = os.path.join(work, "lodgen")
sources = sorted(glob.glob(os.path.join(MESHOPT, "src", "*.cpp")))
subprocess.check_call(["clang++", "-std=c++17", "-O2", os.path.join(ROOT, "tools", "lod", "lodgen.cpp"), *sources,
                       "-I", os.path.join(MESHOPT, "src"), "-lz", "-o", tool])

args = []
for system in SYSTEMS:
    manifest = json.load(open(os.path.join(MODELS, f"mesh-{system}.json")))
    seg = os.path.join(work, f"{system}.seg")
    with open(seg, "w") as fh:
        for part in manifest["parts"]:
            runs = part.get("seg") or [[0, part["tris"]]]
            fh.write(" ".join(str(n) for _, n in runs) + "\n")
    args += [os.path.join(MODELS, f"mesh-{system}.bin"), seg]
subprocess.check_call([tool, *args])
