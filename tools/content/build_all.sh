#!/bin/sh
# Regenerates every Anatomy/Content/atlas-*.json file and validates them.
cd "$(dirname "$0")" && python3 skeletal.py && python3 articular.py && python3 muscular.py && python3 nervous.py && python3 cardiovascular.py && python3 viscera.py && python3 others.py && python3 validate.py --related
