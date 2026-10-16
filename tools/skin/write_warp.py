"""Writes the female warp field for the app (WarpField.swift).

    python3 write_warp.py <warp.npz from warp_field.py> <Anatomy/Resources/Models/warp-female.bin>

"WRP2", grid count u32, then per grid: origin f32×3, cell size f32, dims
u32×3 and the displacement of every cell as float16 xyz, index
(i * ny + j) * nz + k. The first grid covers the body, the others (hands,
feet) are finer and blended in over it. Raw deflate like the mesh packs.
"""
import struct
import sys
import zlib

import numpy as np

src, dst = sys.argv[1:3]
w = np.load(src)
grids = [(w['lo'], float(w['h']), w['dims'].astype(int), w['D'])]
for k in range(len(w['sub_lo']) if 'sub_lo' in w.files else 0):
    grids.append((w['sub_lo'][k], float(w['hs']), w['sub_dims'][k].astype(int), w[f'sub{k}']))
blob = bytearray(b'WRP2' + struct.pack('<I', len(grids)))
for lo, h, dims, D in grids:
    assert D.shape == (dims[0], dims[1], dims[2], 3)
    blob += struct.pack('<4f', *np.asarray(lo, np.float32), h) + struct.pack('<3I', *dims) + D.astype('<f2').tobytes()
comp = zlib.compressobj(9, zlib.DEFLATED, -15)
data = comp.compress(bytes(blob)) + comp.flush()
open(dst, 'wb').write(data)
print(f'warp: {len(grids)} grids ({", ".join(f"{d.tolist()} at {h * 1000:.0f} mm" for _, h, d, _ in grids)}), {len(data) / 1e6:.2f} MB')
