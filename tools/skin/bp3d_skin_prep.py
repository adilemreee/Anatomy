"""BodyParts3D's own skin (FMA7163) in the atlas frame.

The atlas bones are BodyParts3D's (tools/build_hd.py), so the skin of the same
body fits them as no other skin can. This brings the skin into the app's frame
with one similarity transform fitted on the bone centres, welds it, keeps its
outer surface (the mesh is a solid layer of skin and the fat under it, with
inner sheets), drops the small loose patches and reduces it to about
`triangles` triangles, faces wound outwards.

    Blender -b --python tools/skin/bp3d_skin_prep.py -- <BodyParts3D_3.0_obj_95.zip> <parts_list_e.txt> \\
        <skeletal pack dir> <out skin.npz> [triangles]

BodyParts3D: CC BY-SA 2.1 JP, The Database Center for Life Science.
"""
import io
import os
import sys
import zipfile

import bmesh
import bpy
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from packedit import load  # noqa: E402

args = sys.argv[sys.argv.index('--') + 1:]
ZIP, PARTS_LIST, BONES, OUT = args[:4]
TRIANGLES = int(args[4]) if len(args) > 4 else 300000

z = zipfile.ZipFile(ZIP)
files = {n.replace('\\', '/').split('/')[-1][:-4]: n for n in z.namelist() if n.endswith('.obj')}
names = {}
for line in open(PARTS_LIST, encoding='utf-8'):
    c = line.rstrip('\n').split('\t')
    if len(c) >= 2 and c[0].startswith('FMA'):
        names.setdefault(c[1].strip().lower(), c[0])


def read_obj(fma, faces=True):
    vs, fs = [], []
    for line in io.TextIOWrapper(z.open(files[fma]), encoding='utf-8', errors='ignore'):
        if line.startswith('v '):
            vs.append(line[2:].split())
        elif faces and line.startswith('f '):
            ids = [int(t.split('/')[0]) for t in line.split()[1:]]
            for k in range(1, len(ids) - 1):
                fs.append((ids[0], ids[k], ids[k + 1]))
    return np.array(vs, float), np.array(fs, np.int64) - 1


def similarity(a, b):
    """Umeyama: s, R, t minimising |s R a + t - b|."""
    ma, mb = a.mean(0), b.mean(0)
    A, B = a - ma, b - mb
    u, d, vt = np.linalg.svd(B.T @ A / len(a))
    S = np.eye(3)
    if np.linalg.det(u) * np.linalg.det(vt) < 0:
        S[2, 2] = -1
    r = u @ S @ vt
    s = np.trace(np.diag(d) @ S) / (A ** 2).sum(1).mean()
    return s, r, mb - s * r @ ma


# --- the transform, from the bones both have ----------------------------------------------------
_, parts, _, _ = load(BONES, 'skeletal')
src, dst = [], []
for p in parts:
    i = p['info']
    base = i['base'].lower()
    side = {'r': 'right ', 'l': 'left '}.get(i.get('side'), '')
    for cand in (side + base, base, side + base.replace(' bone', ''), base.replace(' bone', '')):
        f = names.get(cand)
        if f and f in files:
            src.append(read_obj(f, faces=False)[0].mean(0)); dst.append(p['co'].mean(0))
            break
src, dst = np.array(src), np.array(dst)
s, r, t = similarity(src, dst)
for _ in range(3):
    err = np.linalg.norm((s * (r @ src.T)).T + t - dst, axis=1)
    keep = err < max(np.median(err) * 3, 0.01)
    s, r, t = similarity(src[keep], dst[keep])
err = np.linalg.norm((s * (r @ src.T)).T + t - dst, axis=1)
print(f'transform from {len(src)} bones: scale {s:.6f}, median centre error {np.median(err) * 1000:.1f} mm', flush=True)

# --- the skin -------------------------------------------------------------------------------------
V, F = read_obj(names['skin'])
V = (s * (r @ V.T)).T + t
me = bpy.data.meshes.new('skin')
me.from_pydata(V.tolist(), [], F.tolist())
me.update()
bm = bmesh.new(); bm.from_mesh(me)
bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-6)
bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
bm.to_mesh(me); bm.free()
co = np.empty(len(me.vertices) * 3); me.vertices.foreach_get('co', co); co = co.reshape(-1, 3)
me.calc_loop_triangles()
tri = np.empty(len(me.loop_triangles) * 3, np.int64); me.loop_triangles.foreach_get('vertices', tri); tri = tri.reshape(-1, 3)
vol = np.einsum('ij,ij->i', co[tri[:, 0]], np.cross(co[tri[:, 1]], co[tri[:, 2]])).sum() / 6
if vol < 0:
    tri = tri[:, ::-1].copy()

# The mesh is a solid layer (skin and the fat under it, with inner sheets):
# only its outer surface is wanted. A vertex is on it when a ray from just
# off it escapes the body.
from mathutils import Vector  # noqa: E402
from mathutils.bvhtree import BVHTree  # noqa: E402
tree = BVHTree.FromPolygons([Vector(v) for v in co], [tuple(map(int, f)) for f in tri])
nrm = np.zeros_like(co)
fn = np.cross(co[tri[:, 1]] - co[tri[:, 0]], co[tri[:, 2]] - co[tri[:, 0]])
for k in range(3):
    np.add.at(nrm, tri[:, k], fn)
nrm /= np.linalg.norm(nrm, axis=1, keepdims=True).clip(1e-12)
axes = [Vector(d) for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))]
outer = np.zeros(len(co), bool)
for k, (v, n) in enumerate(zip(co, nrm)):
    o = Vector(v + n * 0.0005)
    for d in [Vector(n)] + axes:
        if tree.ray_cast(o, d, 3.0)[0] is None:
            outer[k] = True
            break
keep_f = outer[tri].all(1)
print(f'outer surface: {int(outer.sum())} of {len(co)} vertices, {int(keep_f.sum())} of {len(tri)} triangles', flush=True)
tri = tri[keep_f]

me2 = bpy.data.meshes.new('outer')
me2.from_pydata(co.tolist(), [], tri.tolist())
me2.update()
bm = bmesh.new(); bm.from_mesh(me2); bm.faces.ensure_lookup_table()
# the one large surface (small loose patches go)
seen, biggest = set(), []
for f in bm.faces:
    if f.index in seen:
        continue
    stack, comp = [f], []
    seen.add(f.index)
    while stack:
        g = stack.pop(); comp.append(g)
        for e in g.edges:
            for h in e.link_faces:
                if h.index not in seen:
                    seen.add(h.index); stack.append(h)
    if len(comp) > len(biggest):
        biggest = comp
keep = set(f.index for f in biggest)
bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.index not in keep], context='FACES')
bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_faces], context='VERTS')
bm.to_mesh(me2); bm.free()
ob = bpy.data.objects.new('outer', me2)
bpy.context.scene.collection.objects.link(ob)
mod = ob.modifiers.new('decimate', 'DECIMATE')
mod.ratio = min(1.0, TRIANGLES * 1.02 / len(me2.polygons))
mod.use_collapse_triangulate = True
dg = bpy.context.evaluated_depsgraph_get()
m3 = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
m3.calc_loop_triangles()
co = np.empty(len(m3.vertices) * 3); m3.vertices.foreach_get('co', co)
idx = np.empty(len(m3.loop_triangles) * 3, np.int64); m3.loop_triangles.foreach_get('vertices', idx)
np.savez(OUT, co=co.reshape(-1, 3), idx=idx.reshape(-1, 3))
print(f'skin: {len(co) // 3} vertices, {len(idx) // 3} triangles -> {OUT}', flush=True)
