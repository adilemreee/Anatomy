#!/bin/sh
# Regenerates every Anatomy/Content/atlas-*.json and questions-*.json file and validates them.
set -e
cd "$(dirname "$0")"
python3 skeletal.py && python3 articular.py && python3 muscular.py && python3 nervous.py && python3 cardiovascular.py && python3 viscera.py && python3 others.py
python3 validate.py --related
cd questions
for f in q_*.py; do python3 "$f"; done
python3 validate.py
