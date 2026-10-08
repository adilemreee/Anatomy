"""Splits a baked high-detail pack into individually compressed parts.

    python3 tools/pack_hd.py <hd-system.bin (ANT2)> <out_dir>

The app opens one structure at a time in the specimen viewer, so each part
is stored on its own and can be inflated without touching the others:

    "ANH1"  u32 partCount
    partCount x (u32 offset, u32 length)     from the start of the file
    then, per part, a raw-deflated single-part "ANT2" pack (same layout as
    the mesh packs, with partCount 1)

The manifest (hd-<system>.json) is copied next to it unchanged.
"""
import os
import shutil
import struct
import sys
import zlib

src, out_dir = sys.argv[1], sys.argv[2]
raw = zlib.decompress(open(src, "rb").read(), -15)
assert raw[:4] == b"ANT2", "run tools/bake_ao.swift first"
count, = struct.unpack_from("<I", raw, 4)
box = raw[8:32]
counts = [struct.unpack_from("<II", raw, 32 + 8 * i) for i in range(count)]
cur = 32 + 8 * count
blobs = []
for nv, ni in counts:
    size = nv * 6 + nv * 3 + ni * (4 if nv > 65535 else 2) + nv
    part = b"ANT2" + struct.pack("<I", 1) + box + struct.pack("<II", nv, ni) + raw[cur:cur + size]
    cur += size
    comp = zlib.compressobj(9, zlib.DEFLATED, -15)
    blobs.append(comp.compress(part) + comp.flush())
assert cur == len(raw), "unexpected trailing data"

header = 8 + 8 * count
table, offset = b"", header
for b in blobs:
    table += struct.pack("<II", offset, len(b))
    offset += len(b)
name = os.path.basename(src)
with open(os.path.join(out_dir, name), "wb") as fh:
    fh.write(b"ANH1" + struct.pack("<I", count) + table + b"".join(blobs))
manifest = os.path.splitext(src)[0] + ".json"
if os.path.abspath(os.path.dirname(manifest)) != os.path.abspath(out_dir):
    shutil.copy(manifest, out_dir)
print(f"{name}: {count} parts, {offset / 1e6:.1f} MB")
