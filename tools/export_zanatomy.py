"""Exports the Z-Anatomy Blender scene into compact per-system mesh packs.

Run headless:
    Blender -b Startup.blend --python tools/export_zanatomy.py -- <out_dir>

For every body system collection it writes
    mesh-<system>.bin   raw-deflate compressed geometry (see format below)
    mesh-<system>.json  part manifest (names, hierarchy, bounds, material
                        segments) plus the system's material name table

Each part's triangles are sorted by material so that the manifest can
describe them as runs ("seg": [[material, triangleCount], ...]); this keeps
Z-Anatomy's tendon / muscle belly, bone shade and brain lobe distinctions.
tools/bake_ao.swift later appends per-vertex ambient occlusion ("ANT2").

Binary layout (little endian, after inflating):
    "ANT1"                      magic
    u32 partCount
    f32x3 boundsMin, f32x3 boundsMax      quantisation box for positions
    partCount × (u32 vertexCount, u32 indexCount)
    then for each part:
        vertexCount × u16x3   positions, quantised inside the box
        vertexCount × i8x3    normals (snorm)
        indexCount  × u16|u32 triangle indices (u32 when vertexCount > 65535)

Coordinates are converted to Y-up with the body facing +Z, in metres.
Z-Anatomy is licensed CC BY-SA 4.0 (models derived from BodyParts3D).
"""
import bpy
import json
import re
import struct
import sys
import time
import zlib

import numpy as np

OUT = sys.argv[sys.argv.index("--") + 1]

# collection name -> (system id, triangle budget)
SYSTEMS = {
    "1: Skeletal system": ("skeletal", 900000),
    "2: Muscular insertions": ("insertions", 120000),
    "3: Joints": ("joints", 260000),
    "4: Muscular system": ("muscular", 1500000),
    "5: Cardiovascular system": ("cardiovascular", 650000),
    "6: Lymphoid organs": ("lymphoid", 140000),
    "7: Nervous system & Sense organs": ("nervous", 950000),
    "8: Visceral systems": ("visceral", 400000),
    "9: Regions of human body": ("regions", 150000),
}
HELPER_SUFFIX = (".g", ".t", ".j", ".i", ".s")
SIDE_RE = re.compile(r"\.(?:(o|e)(\d*))?([lr])$")
FASCIA_RE = re.compile(r"fascia|aponeurosis|retinacul|septum|membrane|sheath|bursa", re.I)


def clean(name):
    name = re.sub(r"\.(g|t|j|i|s)$", "", name)
    return name


def split_side(name):
    m = SIDE_RE.search(name)
    if not m:
        return name, None, None
    base = name[: m.start()]
    kind = {"o": "origin", "e": "insertion"}.get(m.group(1))
    return base, m.group(3), kind


def ancestry(obj):
    out = []
    p = obj.parent
    while p is not None:
        n = clean(p.name)
        base, _, _ = split_side(n)
        if not out or out[-1] != base:
            out.append(base)
        p = p.parent
    out.reverse()
    return out


def hexcolor(obj):
    mat = obj.active_material
    c = None
    if mat is not None:
        c = mat.diffuse_color
    elif obj.color[3] > 0:
        c = obj.color
    if c is None:
        return None
    return "%02x%02x%02x" % tuple(int(max(0, min(1, v)) ** (1 / 2.2) * 255) for v in c[:3])


MATERIALS = {}


def material_id(sid, name):
    table = MATERIALS.setdefault(sid, [])
    name = re.sub(r"\.\d+$", "", name or "Default")
    if name not in table:
        table.append(name)
    return table.index(name)


def log(t0, msg):
    print(f"[{time.time()-t0:.0f}s] {msg}", flush=True)


def walk(lc):
    yield lc
    for ch in lc.children:
        yield from walk(ch)


def main():
    t0 = time.time()
    scene = bpy.context.scene
    for lc in walk(bpy.context.view_layer.layer_collection):
        if lc.collection.name in SYSTEMS:
            lc.hide_viewport = False

    # Pick geometry objects and tone down subdivision / curve resolution.
    picked = {}
    for cname, (sid, _) in SYSTEMS.items():
        coll = bpy.data.collections[cname]
        objs = []
        for o in coll.objects:
            if o.type not in ("MESH", "CURVE") or o.name.endswith(HELPER_SUFFIX) or o.hide_get():
                continue
            if o.type == "MESH":
                base = sum(len(p.vertices) - 2 for p in o.data.polygons)
                for m in o.modifiers:
                    if m.type == "SUBSURF":
                        if sid == "insertions" or base >= 2500:
                            m.show_viewport = False
                        else:
                            m.levels = min(m.levels, 1)
            else:
                cu = o.data
                cu.resolution_u = min(cu.resolution_u, 6)
                if cu.bevel_mode == "ROUND":
                    cu.bevel_resolution = min(cu.bevel_resolution, 2)
                for m in o.modifiers:
                    if m.type == "SUBSURF":
                        m.show_viewport = False
            objs.append(o)
        picked[sid] = objs

    dg = bpy.context.evaluated_depsgraph_get()
    dg.update()
    log(t0, "evaluated scene")

    # Pass 1: count evaluated triangles and decide a decimation ratio per system.
    tri_counts = {}
    ratios = {}
    for cname, (sid, budget) in SYSTEMS.items():
        counts = {}
        for o in picked[sid]:
            ev = o.evaluated_get(dg)
            try:
                me = ev.to_mesh()
            except RuntimeError:
                continue
            if me is None:
                continue
            counts[o.name] = sum(len(p.vertices) - 2 for p in me.polygons)
            ev.to_mesh_clear()
        total = sum(counts.values())
        small = sum(v for v in counts.values() if v < 600)
        big = total - small
        ratio = 1.0 if total <= budget or big == 0 else max(0.06, (budget - small) / big)
        tri_counts[sid] = counts
        ratios[sid] = ratio
        log(t0, f"{sid}: {len(counts)} parts, {total} tris -> ratio {ratio:.3f}")

    # Pass 2: append a decimate modifier to the big parts and evaluate once.
    # Curves cannot be decimated directly, so they get a mesh proxy first.
    proxies = {}
    for cname, (sid, _) in SYSTEMS.items():
        ratio = ratios[sid]
        if ratio >= 0.97:
            continue
        for o in picked[sid]:
            if tri_counts[sid].get(o.name, 0) < 600:
                continue
            target = o
            if o.type == "CURVE":
                me = bpy.data.meshes.new_from_object(o.evaluated_get(dg), preserve_all_data_layers=False, depsgraph=dg)
                target = bpy.data.objects.new("__proxy", me)
                target.matrix_world = o.matrix_world.copy()
                scene.collection.objects.link(target)
                proxies[o.name] = target
            mod = target.modifiers.new("__dec", "DECIMATE")
            mod.ratio = ratio
            mod.use_collapse_triangulate = True
    dg.update()
    log(t0, "decimated")

    all_parts = {}
    gmin = np.array([1e9, 1e9, 1e9]); gmax = -gmin
    conv = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]], dtype=np.float64)  # (x,y,z) -> (x,z,-y)

    for cname, (sid, budget) in SYSTEMS.items():
        parts = []
        for o in picked[sid]:
            if o.name not in tri_counts[sid]:
                continue
            src = proxies.get(o.name, o)
            ev = src.evaluated_get(dg)
            try:
                me = ev.to_mesh()
            except RuntimeError:
                continue
            if me is None:
                continue
            me.calc_loop_triangles()
            nv = len(me.vertices)
            nt = len(me.loop_triangles)
            if nv == 0 or nt == 0:
                ev.to_mesh_clear()
                continue
            mw = np.array(src.matrix_world, dtype=np.float64)
            co = np.empty(nv * 3, dtype=np.float64)
            me.vertices.foreach_get("co", co)
            co = co.reshape(-1, 3)
            co = co @ mw[:3, :3].T + mw[:3, 3]
            co = co @ conv.T
            nrm = np.empty(nv * 3, dtype=np.float64)
            me.vertex_normals.foreach_get("vector", nrm)
            nrm = nrm.reshape(-1, 3)
            nm = np.linalg.inv(mw[:3, :3]).T
            nrm = (nrm @ nm.T) @ conv.T
            idx = np.empty(nt * 3, dtype=np.int64)
            me.loop_triangles.foreach_get("vertices", idx)
            mat_index = np.empty(nt, dtype=np.int64)
            me.loop_triangles.foreach_get("material_index", mat_index)
            slot_names = [m.name if m else "" for m in me.materials]
            if not slot_names:
                slot_names = [sl.material.name if sl.material else "" for sl in o.material_slots]
            ev.to_mesh_clear()
            # global material id per triangle, then sort triangles by it
            tri_mat = np.array([material_id(sid, slot_names[i] if 0 <= i < len(slot_names) else "")
                                for i in range(max(len(slot_names), 1))], dtype=np.int64)[np.clip(mat_index, 0, max(len(slot_names), 1) - 1)]
            order = np.argsort(tri_mat, kind="stable")
            idx = idx.reshape(-1, 3)[order].reshape(-1)
            tri_mat = tri_mat[order]
            segments = []
            if len(tri_mat):
                cuts = np.flatnonzero(np.diff(tri_mat)) + 1
                starts = np.concatenate([[0], cuts])
                ends = np.concatenate([cuts, [len(tri_mat)]])
                segments = [[int(tri_mat[a]), int(b - a)] for a, b in zip(starts, ends)]
            if np.linalg.det(mw[:3, :3]) < 0:
                # mirrored objects: keep triangles counter-clockwise when seen
                # from outside so two-sided lighting does not flip normals
                idx = idx.reshape(-1, 3)[:, ::-1].reshape(-1)
            used = np.unique(idx)
            if len(used) != nv:
                remap = np.full(nv, -1, dtype=np.int64)
                remap[used] = np.arange(len(used))
                co, nrm, idx = co[used], nrm[used], remap[idx]
            gmin = np.minimum(gmin, co.min(axis=0)); gmax = np.maximum(gmax, co.max(axis=0))
            name = o.name
            base, side, kind = split_side(name)
            parts.append({
                "name": name, "base": base, "side": side, "kind": kind,
                "path": ancestry(o), "color": hexcolor(o),
                "fascia": bool(FASCIA_RE.search(base)) and sid == "muscular",
                "co": co, "n": nrm, "idx": idx, "seg": segments,
            })
        all_parts[sid] = parts
        log(t0, f"{sid}: kept {len(parts)} parts, {sum(len(p['idx'])//3 for p in parts)} tris")

    # write
    pad = 0.002
    gmin -= pad; gmax += pad
    span = gmax - gmin
    for sid, parts in all_parts.items():
        out = bytearray()
        out += b"ANT1" + struct.pack("<I", len(parts))
        out += struct.pack("<3f", *gmin) + struct.pack("<3f", *gmax)
        for p in parts:
            out += struct.pack("<II", len(p["co"]), len(p["idx"]))
        manifest = []
        for p in parts:
            q = np.clip(np.round((p["co"] - gmin) / span * 65535), 0, 65535).astype("<u2")
            out += q.tobytes()
            n = p["n"]
            ln = np.linalg.norm(n, axis=1, keepdims=True); ln[ln == 0] = 1
            out += np.clip(np.round(n / ln * 127), -127, 127).astype("i1").tobytes()
            dt = "<u2" if len(p["co"]) <= 65535 else "<u4"
            out += p["idx"].astype(dt).tobytes()
            lo = p["co"].min(axis=0); hi = p["co"].max(axis=0)
            entry = {"name": p["name"], "base": p["base"], "path": p["path"],
                     "bounds": [round(float(v), 4) for v in (*lo, *hi)],
                     "tris": int(len(p["idx"]) // 3)}
            if p["side"]: entry["side"] = p["side"]
            if p["kind"]: entry["kind"] = p["kind"]
            if p["color"]: entry["color"] = p["color"]
            if p["fascia"]: entry["fascia"] = True
            entry["seg"] = p["seg"]
            manifest.append(entry)
        comp = zlib.compressobj(9, zlib.DEFLATED, -15)
        blob = comp.compress(bytes(out)) + comp.flush()
        with open(f"{OUT}/mesh-{sid}.bin", "wb") as fh:
            fh.write(blob)
        with open(f"{OUT}/mesh-{sid}.json", "w", encoding="utf-8") as fh:
            json.dump({"system": sid, "materials": MATERIALS.get(sid, []), "parts": manifest}, fh, ensure_ascii=False, separators=(",", ":"))
        log(t0, f"{sid}: {len(parts)} parts, {len(out)/1e6:.1f} MB raw, {len(blob)/1e6:.1f} MB deflated")
    log(t0, f"done, bounds {gmin} {gmax}")


main()
