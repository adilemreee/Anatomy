"""Builds the launch animation's images from the icon renders
(tools/icon/render_layers.py, frame "body"):

    SplashSkin      the whole figure as a white silhouette
    SplashAnatomy   the right half of the figure, muscles over the skeleton

both cropped to the same box, into Anatomy/Assets.xcassets.

    <venv python> tools/icon/make_splash.py <renders of the body frame>
"""
import json
import os
import sys

import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ASSETS = os.path.join(ROOT, 'Anatomy', 'Assets.xcassets')
HEIGHT = 1400


def imageset(name, img):
    d = os.path.join(ASSETS, f'{name}.imageset')
    os.makedirs(d, exist_ok=True)
    img.save(os.path.join(d, f'{name}.png'), optimize=True)
    json.dump({'images': [{'filename': f'{name}.png', 'idiom': 'universal'}],
               'info': {'author': 'xcode', 'version': 1}}, open(os.path.join(d, 'Contents.json'), 'w'), indent=2)


def main(renders):
    skin = np.array(Image.open(os.path.join(renders, 'skin.png')).convert('RGBA'))
    anat = np.array(Image.open(os.path.join(renders, 'anatomy.png')).convert('RGBA'))
    W = skin.shape[1]
    anat[:, :W // 2, 3] = 0
    alpha = np.maximum(skin[..., 3], anat[..., 3])
    ys, xs = np.nonzero(alpha > 8)
    # symmetric about the midline, so the split stays in the middle of the image
    half = max(W // 2 - xs.min(), xs.max() - W // 2) + 8
    box = (W // 2 - half, ys.min() - 8, W // 2 + half, ys.max() + 8)
    scale = HEIGHT / (box[3] - box[1])
    size = (int(round((box[2] - box[0]) * scale)), HEIGHT)
    for name, a in (('SplashSkin', skin), ('SplashAnatomy', anat)):
        imageset(name, Image.fromarray(a).crop(box).resize(size, Image.LANCZOS))
    print('splash images', size)


if __name__ == '__main__':
    main(sys.argv[1])
