"""Dumps the Z-Anatomy reference texts (one per structure) to JSON.

    Blender -b Startup.blend --python tools/dump_zanatomy_texts.py -- texts.json
"""
import bpy
import json
import sys

out = sys.argv[sys.argv.index("--") + 1]
json.dump({t.name: t.as_string() for t in bpy.data.texts}, open(out, "w"), ensure_ascii=False)
