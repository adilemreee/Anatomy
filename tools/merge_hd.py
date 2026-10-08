"""Puts high-detail parts straight into an atlas pack.

    python3 tools/merge_hd.py <mesh-system.bin> <mesh-system.json> <hd-system.bin (ANT1/ANT2)> <hd-system.json> <out_dir>

Writes mesh-<system>.bin as "ANT1" (run tools/bake_ao.swift on it again)
and mesh-<system>.json with the replaced parts' triangle counts, bounds and
material segments. Both packs share the quantisation box (build_hd.py
reads it from the atlas pack), so part data is copied byte for byte.
"""
import json
import os
import struct
import sys
import zlib

lod_bin, lod_json, hd_bin, hd_json, out_dir = sys.argv[1:6]


def read(path):
    raw = zlib.decompress(open(path, "rb").read(), -15)
    assert raw[:3] == b"ANT"
    has_ao = raw[3:4] == b"2"
    count, = struct.unpack_from("<I", raw, 4)
    box = raw[8:32]
    counts = [struct.unpack_from("<II", raw, 32 + 8 * i) for i in range(count)]
    cur = 32 + 8 * count
    parts = []
    for nv, ni in counts:
        size = nv * 9 + ni * (4 if nv > 65535 else 2)
        parts.append((nv, ni, raw[cur:cur + size]))
        cur += size + (nv if has_ao else 0)
    return box, parts


lod_box, lod_parts = read(lod_bin)
hd_box, hd_parts = read(hd_bin)
assert lod_box == hd_box, "packs use different quantisation boxes"
manifest = json.load(open(lod_json))
hd_manifest = json.load(open(hd_json))
replaced = {}
for info, part in zip(hd_manifest["parts"], hd_parts):
    replaced[info["lod"]] = (info, part)

out = bytearray(b"ANT1" + struct.pack("<I", len(lod_parts)) + lod_box)
chosen = []
for i, part in enumerate(lod_parts):
    if i in replaced:
        info, hd = replaced[i]
        entry = manifest["parts"][i]
        entry["tris"], entry["bounds"], entry["seg"] = info["tris"], info["bounds"], info["seg"]
        chosen.append(hd)
    else:
        chosen.append(part)
for nv, ni, _ in chosen:
    out += struct.pack("<II", nv, ni)
for _, _, data in chosen:
    out += data
comp = zlib.compressobj(9, zlib.DEFLATED, -15)
name = os.path.basename(lod_bin)
open(os.path.join(out_dir, name), "wb").write(comp.compress(bytes(out)) + comp.flush())
json.dump(manifest, open(os.path.join(out_dir, os.path.basename(lod_json)), "w"), ensure_ascii=False, separators=(",", ":"))
before = sum(ni for _, ni, _ in lod_parts) // 3
after = sum(ni for _, ni, _ in chosen) // 3
print(f"{name}: {len(replaced)} parts replaced, {before} -> {after} triangles")
