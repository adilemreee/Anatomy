"""Evaluates the female warp (warp_field.py output) like WarpField.swift."""
import numpy as np


class Warp:
    def __init__(self, path):
        w = np.load(path)
        self.grids = [(w['lo'], float(w['h']), w['D'].astype(np.float64))]
        for k in range(len(w['sub_lo']) if 'sub_lo' in w.files else 0):
            self.grids.append((w['sub_lo'][k], float(w['hs']), w[f'sub{k}'].astype(np.float64)))

    @staticmethod
    def _tri(g, p):
        lo, h, D = g
        dims = np.array(D.shape[:3])
        q = np.clip((p - lo) / h, 0, dims - 1.001)
        i = q.astype(int); f = q - i
        r = 0
        for dx in (0, 1):
            for dy in (0, 1):
                for dz in (0, 1):
                    wt = (f[:, 0] if dx else 1 - f[:, 0]) * (f[:, 1] if dy else 1 - f[:, 1]) * (f[:, 2] if dz else 1 - f[:, 2])
                    r = r + D[i[:, 0] + dx, i[:, 1] + dy, i[:, 2] + dz] * wt[:, None]
        return r

    def disp(self, p):
        p = np.asarray(p, np.float64)
        d = self._tri(self.grids[0], p)
        for g in self.grids[1:]:
            lo, h, D = g
            up = lo + (np.array(D.shape[:3]) - 1) * h
            t = np.clip(np.minimum((p - lo) / 0.012, (up - p) / 0.012).min(1), 0, 1)
            t = t * t * (3 - 2 * t)
            sel = t > 0
            if sel.any():
                d[sel] += (self._tri(g, p[sel]) - d[sel]) * t[sel, None]
        return d
