#!/bin/sh
# Rebuilds the visceral, lymphoid, cardiovascular, regions and nervous packs:
# the BodyParts3D organs (tools/build_organs.py) on the original Z-Anatomy
# export, the female organs from the Human Reference Atlas
# (tools/add_female.py), the structures neither source has
# (tools/add_extras.py), baked occlusion and levels of detail; then copies
# the packs into Anatomy/Resources/Models.
#
#   tools/rebuild_organs.sh <original packs dir> <bp3d obj dir> <parts_list_e.txt> <hra dir> <meshoptimizer> <work dir>
#
# <original packs dir> holds mesh-visceral/lymphoid .bin/.json as exported
# by tools/export_zanatomy.py (any of ANT1/2/3). The cardiovascular,
# regions, nervous, muscular and skeletal packs are taken from the app.
set -e
ORIG=$1 BP3D=$2 PARTS=$3 HRA=$4 MESHOPT=$5 WORK=$6
ROOT=$(cd "$(dirname "$0")/.." && pwd)
MODELS="$ROOT/Anatomy/Resources/Models"
mkdir -p "$WORK/plain" "$WORK/organs" "$WORK/female" "$WORK/final" "$WORK/bin"
for s in visceral lymphoid; do
  python3 "$ROOT/tools/strip_pack.py" "$ORIG/mesh-$s.bin" "$WORK/plain/mesh-$s.bin"
  cp "$ORIG/mesh-$s.json" "$WORK/plain/"
done
blender -b --python "$ROOT/tools/build_organs.py" -- "$BP3D" "$PARTS" "$WORK/plain" "$WORK/organs" visceral lymphoid
blender -b --python "$ROOT/tools/add_female.py" -- "$HRA" "$WORK/organs" "$WORK/female"
cp "$WORK/organs/mesh-lymphoid.bin" "$WORK/organs/mesh-lymphoid.json" "$WORK/female/"
for s in cardiovascular regions nervous muscular skeletal; do
  cp "$MODELS/mesh-$s.bin" "$MODELS/mesh-$s.json" "$WORK/female/"
done
blender -b --python "$ROOT/tools/add_extras.py" -- "$HRA" "$WORK/female" "$WORK/final"
[ -x "$WORK/bin/bake_ao" ] || swiftc -O "$ROOT/tools/bake_ao.swift" -o "$WORK/bin/bake_ao"
"$WORK/bin/bake_ao" "$WORK/final"/mesh-visceral.bin "$WORK/final"/mesh-lymphoid.bin "$WORK/final"/mesh-cardiovascular.bin "$WORK/final"/mesh-regions.bin "$WORK/final"/mesh-nervous.bin
python3 "$ROOT/tools/build_lods.py" "$MESHOPT" --models "$WORK/final" visceral lymphoid cardiovascular regions nervous
cp "$WORK/final"/mesh-*.bin "$WORK/final"/mesh-*.json "$MODELS/"
