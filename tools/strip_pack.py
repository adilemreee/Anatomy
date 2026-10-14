"""Turns a baked pack back into plain geometry so it can be edited again.

    python3 tools/strip_pack.py <mesh-system.bin> <out.bin>

Reads an "ANT2"/"ANT3" pack (baked occlusion, levels of detail) and writes
the "ANT1" layout that tools/merge_hd.py, tools/add_parts.py and
tools/bake_ao.swift expect. Run bake_ao and build_lods again afterwards.
"""
import struct
import sys
import zlib

src, dst = sys.argv[1], sys.argv[2]
raw = zlib.decompress(open(src, "rb").read(), -15)
assert raw[:3] == b"ANT", "not a mesh pack"
has_ao = raw[3:4] in (b"2", b"3")
count, = struct.unpack_from("<I", raw, 4)
counts = [struct.unpack_from("<II", raw, 32 + 8 * i) for i in range(count)]
cur = 32 + 8 * count
out = bytearray(b"ANT1" + raw[4:cur])
for nv, ni in counts:
    size = nv * 9 + ni * (4 if nv > 65535 else 2)
    out += raw[cur:cur + size]
    cur += size + (nv if has_ao else 0)
comp = zlib.compressobj(9, zlib.DEFLATED, -15)
open(dst, "wb").write(comp.compress(bytes(out)) + comp.flush())
print(f"{src}: {count} parts -> ANT1 {dst}")
