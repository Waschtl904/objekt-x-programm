#!/usr/bin/env python3
"""Unabhaengiger Gegencheck des vollstaendigen Antwortgrams per direkter Quadratur.

Nicht Teil der CI (benoetigt mpmath). Statt der Reihenentwicklungen und
Momentintegrale des Originals werden die zwoelf zusammengesetzten
Antwortfunktionen t_i(y) = [P_i(v) + L_i(v) log((v+1)/(v-1)) + c_i m(y)] / sqrt(2a),
v = y/a, direkt auf der Schale (a, b) integriert: gradiertes Gauss-Legendre
(40 Punkte je Panel, dyadische Panels bis 2^-150 an den logarithmischen Rand),
55 Dezimalstellen. Verglichen werden
  (1) der X-Gram <t_i,t_j>_X mit s * G_0 (rationale Referenz des Originals),
  (2) die Ordnung TT*_W <= G_T (zertifizierte Obermatrix) ueber die Eigenwerte der Differenz,
  (3) ||T||_W numerisch gegen sqrt(tr G_T).
Ergebnis in reports/INDEPENDENT_QUADRATURE.json.
"""
import json, sys, zipfile, io, argparse
from fractions import Fraction as Q
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
ARCHIVE = HERE/'archives/Objekt-X-Vollstaendiger-Antwortgram-und-Scharfer-Modellfehler-2026-10-15.zip'
ROOT = 'Objekt-X-Vollstaendiger-Antwortgram-und-Scharfer-Modellfehler-2026-10-15/'


def qf(x):
    x = Q(x); return mp.mpf(x.numerator)/x.denominator


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--dps', type=int, default=55); ap.add_argument('--points', type=int, default=40); ap.add_argument('--panels', type=int, default=150)
    ap.add_argument('--out', type=Path, default=HERE/'reports/INDEPENDENT_QUADRATURE.json')
    a_ = ap.parse_args(); mp.mp.dps = a_.dps
    z = zipfile.ZipFile(ARCHIVE)
    fs = json.loads(z.read(ROOT+'inputs/FUNCTIONS12.json')); xs = json.loads(z.read(ROOT+'inputs/FROZEN_RESPONSE12.json')); en = json.loads(z.read(ROOT+'RESPONSE_ENERGY.json'))
    a = mp.log(3); b = mp.log(11)/2; h = b-a; s = h/a
    n = a_.points
    import numpy as np
    xs0 = np.polynomial.legendre.leggauss(n)[0]
    xm = [mp.findroot(lambda t: mp.legendre(n, t), mp.mpf(float(x))) for x in xs0]
    wm = [2/((1-x**2)*mp.diff(lambda t: mp.legendre(n, t), x)**2) for x in xm]
    nodes, weights = [], []
    for k in range(1, a_.panels):
        lo = mp.mpf(2)**(-k); hi = mp.mpf(2)**(-(k-1))
        for x, w in zip(xm, wm):
            nodes.append(lo+(hi-lo)*(x+1)/2); weights.append((hi-lo)/2*w)
    report = {'dps': a_.dps, 'points_per_panel': n, 'panels': a_.panels, 'h': mp.nstr(h, 20), 'h_below_101_over_1000': bool(h < mp.mpf('0.101')), 's': mp.nstr(s, 20), 'parities': {}}
    for parity, p in (('even', 0), ('odd', 1)):
        mfun = (lambda y: mp.cosh(y/2)) if p == 0 else (lambda y: mp.sinh(y/2))
        mu = a/2+mp.mpf(2)/3 if p == 0 else -a/2+mp.mpf(2)/3
        funcs = fs['parities'][parity]['functions']
        X = [[qf(v) for v in row] for row in xs['parities'][parity]['X']]
        P = [[qf(c) for c in f['F']['polynomial']] for f in funcs]; L = [[qf(c) for c in f['F']['log_ratio_multiplier']] for f in funcs]; C = [qf(f['F']['physical_W_moment_multiplier']) for f in funcs]
        def comb(i, arrs):
            m = max(len(x) for x in arrs); out = [mp.mpf(0)]*m
            for j in range(12):
                for k, c in enumerate(arrs[j]): out[k] += X[i][j]*c
            return out
        Pi = [comb(i, P) for i in range(12)]; Li = [comb(i, L) for i in range(12)]; Ci = [sum(X[i][j]*C[j] for j in range(12)) for i in range(12)]
        def ev(coef, v):
            r = mp.mpf(0)
            for c in reversed(coef): r = r*v+c
            return r
        T = [[None]*len(nodes) for _ in range(12)]; M = [None]*len(nodes)
        for k, u in enumerate(nodes):
            v = 1+s*u; y = a*v; lg = mp.log((2+s*u)/(s*u)); mm = mfun(y); M[k] = mm
            for i in range(12): T[i][k] = (ev(Pi[i], v)+ev(Li[i], v)*lg+Ci[i]*mm)/mp.sqrt(2*a)
        def ipX(F, G): return 2*h*sum(w*F[k]*G[k] for k, w in enumerate(weights))
        lam = [ipX(T[i], M) for i in range(12)]
        G = mp.matrix(12, 12); GX = mp.matrix(12, 12)
        for i in range(12):
            for j in range(i, 12):
                GX[i, j] = GX[j, i] = ipX(T[i], T[j]); G[i, j] = G[j, i] = GX[i, j]+lam[i]*lam[j]/(2*mu)
        fx = en['parities'][parity]['fixed_X']
        U = mp.matrix([[qf(v) for v in row] for row in fx['physical_TT_adjoint_upper']])
        ref = mp.matrix([[qf(v) for v in row] for row in fx['rational_whole_reference_Gram']])
        relerr = max(abs(GX[i, j]-s*ref[i, j])/max(abs(s*ref[i, j]), mp.mpf('1e-30')) for i in range(12) for j in range(12))
        evD = sorted(mp.eigsy(U-G, eigvals_only=True)); evG = sorted(mp.eigsy(G, eigvals_only=True))
        trU = sum(U[i, i] for i in range(12)); trG = sum(G[i, i] for i in range(12))
        report['parities'][parity] = {
            'max_rel_diff_XGram_vs_s_G0': mp.nstr(relerr, 3),
            'min_eig_G_T_minus_TTstar_numeric': mp.nstr(evD[0], 6),
            'order_TTstar_le_G_T_numerically_confirmed': bool(evD[0] >= 0),
            'T_norm_W_numeric': mp.nstr(mp.sqrt(evG[-1]), 10), 'certified_sqrt_tr_G_T': mp.nstr(mp.sqrt(trU), 10),
            'tr_TTstar_W_numeric': mp.nstr(trG, 12), 'tr_G_T_certified': mp.nstr(trU, 12),
            'TTstar_W_smallest_eigenvalue': mp.nstr(evG[0], 6), 'TTstar_W_condition_number': mp.nstr(evG[-1]/evG[0], 4),
            'max_abs_moment_lambda_i': mp.nstr(max(abs(x) for x in lam), 4),
            'metric_factor_g': mp.nstr(qf(fx['physical_metric_factor_upper'])/s, 12)}
        print(parity, report['parities'][parity])
    a_.out.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    sys.exit(main())
