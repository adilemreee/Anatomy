"""High-yield exam notes ("TUS notları") for the atlas entries, keyed by
entry id. They are kept in tus_<system>.py files and merged into the
entries by common.write()."""
import glob
import importlib
import os

NOTES = {}
_here = os.path.dirname(os.path.abspath(__file__))
for _path in sorted(glob.glob(os.path.join(_here, "tus_*.py"))):
    _name = os.path.splitext(os.path.basename(_path))[0]
    if _name == "tus_notes":
        continue
    for _id, _notes in importlib.import_module(_name).T.items():
        NOTES.setdefault(_id, []).extend(_notes)
