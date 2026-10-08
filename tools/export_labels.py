"""Exports Z-Anatomy's feature labels (e.g. "Head of femur" on the femur).

    Blender -b Startup.blend --python tools/export_labels.py -- labels.json

Z-Anatomy pins every label with a two-vertex leader line (objects ending in
".i" or ".j") that is hooked onto the structure. This script evaluates those
lines and writes, for each label, the owning part, the point on the surface
it points at and the far end of the leader (used for the label direction).
Coordinates use the same Y-up, body-facing-+Z frame as the mesh packs.
"""
import json
import re
import sys

import bpy
import numpy as np
from mathutils.bvhtree import BVHTree

OUT = sys.argv[sys.argv.index("--") + 1]
SYSTEMS = {
    "1: Skeletal system": "skeletal", "3: Joints": "joints", "4: Muscular system": "muscular",
    "5: Cardiovascular system": "cardiovascular", "6: Lymphoid organs": "lymphoid",
    "7: Nervous system & Sense organs": "nervous", "8: Visceral systems": "visceral",
}
CONV = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]], dtype=np.float64)


def conv(v):
    return [round(float(x), 5) for x in (np.array(v) @ CONV.T)]


def walk(lc):
    yield lc
    for ch in lc.children:
        yield from walk(ch)


def main():
    for lc in walk(bpy.context.view_layer.layer_collection):
        if lc.collection.name in SYSTEMS:
            lc.hide_viewport = False
    lines = [o for o in bpy.data.objects if o.type == "MESH" and re.search(r"\.(i|j)$", o.name)]
    for o in lines:
        o.hide_set(False)
        if o.parent:
            o.parent.hide_set(False)
    dg = bpy.context.evaluated_depsgraph_get()
    dg.update()

    trees = {}

    def tree_for(obj):
        if obj.name in trees:
            return trees[obj.name]
        ev = obj.evaluated_get(dg)
        me = ev.to_mesh()
        if me is None or len(me.polygons) == 0:
            trees[obj.name] = None
            return None
        verts = [obj.matrix_world @ v.co for v in me.vertices]
        polys = [tuple(p.vertices) for p in me.polygons]
        tree = BVHTree.FromPolygons(verts, polys)
        ev.to_mesh_clear()
        trees[obj.name] = tree
        return tree

    labels = []
    for o in lines:
        label = o.parent
        if label is None:
            continue
        name = re.sub(r"\.(s|t|g)$", "", label.name)
        # owner: the nearest mesh ancestor with geometry
        owner = label.parent
        while owner is not None and not (owner.type == "MESH" and len(owner.data.polygons) > 0):
            owner = owner.parent
        if owner is None:
            continue
        system = None
        for c in owner.users_collection:
            system = SYSTEMS.get(c.name) or system
        if system is None:
            continue
        ev = o.evaluated_get(dg)
        me = ev.to_mesh()
        if me is None or len(me.vertices) < 2:
            continue
        a = ev.matrix_world @ me.vertices[0].co
        b = ev.matrix_world @ me.vertices[-1].co
        ev.to_mesh_clear()
        tree = tree_for(owner)
        if tree is not None:
            da = tree.find_nearest(a)[3]
            db = tree.find_nearest(b)[3]
            anchor, tip = (a, b) if (da or 9) <= (db or 9) else (b, a)
            dist = min(da or 9, db or 9)
        else:
            anchor, tip, dist = b, a, 0
        if dist > 0.02 or (anchor - tip).length < 1e-5:
            continue
        labels.append({
            "name": name, "owner": owner.name, "system": system,
            "anchor": conv(anchor), "tip": conv(tip),
        })
    json.dump({"labels": labels}, open(OUT, "w"), ensure_ascii=False, separators=(",", ":"))
    print(f"LABELS {len(labels)}")


main()
