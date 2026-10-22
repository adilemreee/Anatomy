"""Builds the app icon, an Icon Composer document (Anatomy/AppIcon.icon).

A human bust on a deep blue field, split down the middle: the left half the
skin as Liquid Glass, the right half the muscles over the skeleton (rendered
from the atlas itself by tools/icon/render_layers.py), a soft blue glow
behind. To rebuild:

    Blender -b --python tools/icon/render_layers.py -- Anatomy/Resources/Models <renders> bust
    <venv python with numpy and Pillow> tools/icon/make_icon.py <renders>
    ictool Anatomy/AppIcon.icon --export-image --output-file icon.png \\
        --platform iOS --rendition Default --width 1024 --height 1024 --scale 1
"""
import json
import os
import sys

import numpy as np
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'Anatomy', 'AppIcon.icon')
S = 1024
# the figure a little smaller than the canvas and lower, so the head has room
POS = {'scale': 0.94, 'translation-in-points': [0, 26]}


def half(img, side, feather=0):
    """The left or right half of a render, at icon size; the split a crisp
    vertical line."""
    a = np.array(img.convert('RGBA').resize((S, S), Image.LANCZOS)).astype(np.float32)
    x = np.arange(S)[None, :]
    keep = (x < S / 2) if side == 'left' else (x >= S / 2)
    a[..., 3] *= keep
    return Image.fromarray(a.clip(0, 255).astype(np.uint8))


def glow():
    """A soft round glow behind the figure's chest."""
    y, x = np.mgrid[0:S, 0:S].astype(np.float32)
    r = np.hypot((x - S / 2) / 360, (y - S * 0.56) / 400)
    a = np.clip(1 - r, 0, 1) ** 1.8 * 150
    img = np.zeros((S, S, 4), np.uint8)
    img[..., 0], img[..., 1], img[..., 2] = 95, 184, 255
    img[..., 3] = a.astype(np.uint8)
    return Image.fromarray(img).filter(ImageFilter.GaussianBlur(8))


def write(renders):
    assets = os.path.join(OUT, 'Assets')
    os.makedirs(assets, exist_ok=True)
    for f in os.listdir(assets):
        os.remove(os.path.join(assets, f))
    half(Image.open(os.path.join(renders, 'skin.png')), 'left').save(os.path.join(assets, 'skin.png'))
    half(Image.open(os.path.join(renders, 'anatomy.png')), 'right').save(os.path.join(assets, 'anatomy.png'))
    glow().save(os.path.join(assets, 'glow.png'))
    doc = {
        'fill': {'linear-gradient': ['display-p3:0.10588,0.23529,0.58039,1.00000',
                                     'display-p3:0.01961,0.03922,0.12157,1.00000']},
        'groups': [
            {'layers': [{'image-name': 'skin.png', 'name': 'skin', 'glass': True, 'position': POS}],
             'shadow': {'kind': 'neutral', 'opacity': 0.5},
             'translucency': {'enabled': True, 'value': 0.5},
             'specular': True},
            {'layers': [{'image-name': 'anatomy.png', 'name': 'anatomy', 'glass': False, 'position': POS}],
             'shadow': {'kind': 'neutral', 'opacity': 0.45},
             'translucency': {'enabled': False, 'value': 0},
             'specular': True},
            {'layers': [{'image-name': 'glow.png', 'name': 'glow', 'glass': False}],
             'shadow': {'kind': 'none', 'opacity': 0},
             'translucency': {'enabled': False, 'value': 0},
             'specular': False},
        ],
        'supported-platforms': {'squares': ['iOS']},
    }
    json.dump(doc, open(os.path.join(OUT, 'icon.json'), 'w'), indent=2)
    print('wrote', OUT)


if __name__ == '__main__':
    write(sys.argv[1])
