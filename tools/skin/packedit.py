"""Read and write the atlas mesh packs as editable parts (every part kept).

    from packedit import load, save
    manifest, parts, lo, hi = load(models_dir, 'visceral')
    ... edit parts[i]['co'] / ['n'] / ['idx'] / ['info'] ...
    save(out_dir, 'visceral', manifest, parts, lo, hi)   # writes "ANT1"

Run bake_ao and build_lods on the written pack afterwards.
"""
import json
import os
import struct
import zlib

import numpy as np


def load(folder, system):
    raw = zlib.decompress(open(os.path.join(folder, f'mesh-{system}.bin'), 'rb').read(), -15)
    manifest = json.load(open(os.path.join(folder, f'mesh-{system}.json')))
    has_ao = raw[3:4] in (b'2', b'3')
    count, = struct.unpack_from('<I', raw, 4)
    lo = np.array(struct.unpack_from('<3f', raw, 8)); hi = np.array(struct.unpack_from('<3f', raw, 20))
    sizes = [struct.unpack_from('<II', raw, 32 + 8 * i) for i in range(count)]
    cur = 32 + 8 * count
    parts = []
    for (nv, ni), info in zip(sizes, manifest['parts']):
        co = np.frombuffer(raw, '<u2', nv * 3, cur).reshape(-1, 3).astype(np.float64) / 65535 * (hi - lo) + lo
        cur += nv * 6
        n = np.frombuffer(raw, 'i1', nv * 3, cur).reshape(-1, 3).astype(np.float64) / 127
        cur += nv * 3
        wide = nv > 65535
        idx = np.frombuffer(raw, '<u4' if wide else '<u2', ni, cur).astype(np.int64).reshape(-1, 3)
        cur += ni * (4 if wide else 2) + (nv if has_ao else 0)
        parts.append({'info': info, 'co': co, 'n': n, 'idx': idx})
    return manifest, parts, lo, hi


def vertex_normals(co, tris):
    n = np.zeros_like(co)
    fn = np.cross(co[tris[:, 1]] - co[tris[:, 0]], co[tris[:, 2]] - co[tris[:, 0]])
    for k in range(3):
        np.add.at(n, tris[:, k], fn)
    return n / np.linalg.norm(n, axis=1, keepdims=True).clip(1e-12)


def covering_box(parts, lo, hi, pad=0.002):
    """The quantisation box: `lo`/`hi`, grown to take every vertex (her breasts
    and toes reach further forward than the male body the box was made for)."""
    lo, hi = np.array(lo, float), np.array(hi, float)
    for p in parts:
        if len(p['co']):
            lo = np.minimum(lo, p['co'].min(0) - pad)
            hi = np.maximum(hi, p['co'].max(0) + pad)
    return lo, hi


def save(folder, system, manifest, parts, lo, hi):
    os.makedirs(folder, exist_ok=True)
    lo, hi = covering_box(parts, lo, hi)
    blob = bytearray(b'ANT1' + struct.pack('<I', len(parts)) + struct.pack('<3f', *lo) + struct.pack('<3f', *hi))
    for p in parts:
        blob += struct.pack('<II', len(p['co']), p['idx'].size)
    for p in parts:
        co = p['co']
        blob += np.clip(np.round((co - lo) / (hi - lo) * 65535), 0, 65535).astype('<u2').tobytes()
        blob += np.clip(np.round(p['n'] * 127), -127, 127).astype('i1').tobytes()
        blob += p['idx'].astype('<u2' if len(p['co']) <= 65535 else '<u4').tobytes()
        info = p['info']
        info['tris'] = int(len(p['idx']))
        if len(p['co']):
            info['bounds'] = [round(float(v), 4) for v in (*co.min(0), *co.max(0))]
    comp = zlib.compressobj(9, zlib.DEFLATED, -15)
    open(os.path.join(folder, f'mesh-{system}.bin'), 'wb').write(comp.compress(bytes(blob)) + comp.flush())
    manifest['parts'] = [p['info'] for p in parts]
    json.dump(manifest, open(os.path.join(folder, f'mesh-{system}.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
