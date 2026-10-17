"""Undirected whole degree-11 K_P model using translation differences.

Inner and outer Gauss checks are diagnostics, not analytic remainder bounds.
No old candidate or directed certificate is changed.
"""
import hashlib
import io
import json
import sys
import zipfile
from fractions import Fraction
from pathlib import Path

import numpy as np
from flint import arb, arb_mat, ctx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DATA = HERE / 'data'
LD = np.longdouble


def bound(name):
    bindings = json.loads((HERE / 'INPUT_BINDINGS.json').read_text())['repository_files']
    raw = (ROOT / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == bindings[name], name
    return raw


def q(s):
    f = Fraction(s)
    return arb(f.numerator) / f.denominator


def ldarb(value):
    f = Fraction(str(value.mid().fmpq()))
    return LD(str(f.numerator)) / LD(str(f.denominator))


def member(z, suffix):
    names = [n for n in z.namelist() if n.endswith('/' + suffix)]
    assert len(names) == 1
    return z.read(names[0])


def build(par, outer=64, inner=24, depth=48):
    ctx.prec = 600
    d = json.loads(bound(f'research/x-c1/shell-polynomial-direction-search-2026-10-17/data/MAPS_{par}_512.json'))
    eps = 1 if par == 'even' else -1
    a, b = np.log(LD(3)), np.log(LD(11)) / 2
    h = b - a
    mu = (eps * a + np.sinh(a)) / 2
    degrees = np.arange(12, dtype=LD)
    scale = np.sqrt((2 * degrees + 1) / (2 * h))
    m = np.cosh if eps == 1 else np.sinh
    def shell(x):
        return np.polynomial.legendre.legvander(2 * (x - a) / h - 1, 11) * scale
    x64, w64 = [np.asarray(v, dtype=LD) for v in np.polynomial.legendre.leggauss(64)]
    points = (a + b) / 2 + h * x64 / 2
    lam = h / 2 * ((w64 * m(points / 2)) @ shell(points))
    Ac = -lam / mu
    G = np.eye(12, dtype=LD) + 2 * np.outer(lam, lam) / mu
    assert np.max(abs(G - np.asarray(d['G_W'], dtype=LD))) < LD('1e-13')
    def values(x):
        x = np.asarray(x, dtype=LD)
        ans = np.zeros((len(x), 12), dtype=LD)
        core = abs(x) < a
        pos = (x > a) & (x < b)
        neg = (x < -a) & (x > -b)
        ans[core] = m(x[core, None] / 2) * Ac
        ans[pos] = shell(x[pos])
        ans[neg] = eps * shell(-x[neg])
        return ans
    xn, wn = [np.asarray(v, dtype=LD) for v in np.polynomial.legendre.leggauss(inner)]
    endpoints = np.array([-b, -a, a, b], dtype=LD)
    def pairing(r, difference):
        cuts = np.unique(np.concatenate((endpoints, endpoints - r)))
        result = np.zeros((12, 12), dtype=LD)
        for lo, hi in zip(cuts[:-1], cuts[1:]):
            mid, half = (lo + hi) / 2, (hi - lo) / 2
            x = mid + half * xn
            u, v = values(x), values(x + r)
            if difference:
                diff = v - u
                result += diff.T @ (half * wn[:, None] * diff)
            else:
                result += u.T @ (half * wn[:, None] * v)
        return (result + result.T) / 2
    zero = pairing(LD(0), False)
    assert np.max(abs(zero - G)) < LD('1e-13')
    xo, wo = [np.asarray(v, dtype=LD) for v in np.polynomial.legendre.leggauss(outer)]
    panels = [(h * LD(2)**(-k), h * LD(2)**(-k+1)) for k in range(depth, 0, -1)]
    for left, right in ((h, 2*a), (2*a, a+b), (a+b, 2*b)):
        lo = left
        while 2*lo < right:
            panels.append((lo, 2*lo))
            lo *= 2
        panels.append((lo, right))
    energy = np.zeros((12, 12), dtype=LD)
    for idx, (lo, hi) in enumerate(panels):
        for x, w in zip(xo, wo):
            r = (lo+hi)/2 + (hi-lo)*x/2
            kernel = np.exp(-r/2) / (-np.expm1(-2*r))
            energy += (hi-lo)*w/2 * kernel * pairing(r, True)
        if idx % 16 == 0:
            print(par, outer, 'translation panels', idx, flush=True)
    theta = np.arctanh(np.exp(-b)) + np.arctan(np.exp(-b))
    energy += 2*theta*G
    primes = np.zeros((12,12), dtype=LD)
    for n,p in ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)):
        primes += 2*np.log(LD(p))/np.sqrt(LD(n))*pairing(np.log(LD(n)),False)
    kappa = np.log(8*ldarb(arb.pi())) + ldarb(arb.const_euler()) + ldarb(arb.pi())/2
    direct = energy - kappa*G - primes
    archive = bound('research/x-c1/a9-a11-whole-response-gram-2026-10-15/archives/Objekt-X-Vollstaendiger-Antwortgram-und-Scharfer-Modellfehler-2026-10-15.zip')
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        fresh = json.loads(member(z,'inputs/FRESH_A12.json'))
        fixed = json.loads(member(z,'inputs/FROZEN_RESPONSE12.json'))
    assert fixed['rule_id'] == 'A9_A11_N12_MIDPOINT_INVERSE_60_V1'
    A = arb_mat([[q(v) for v in row] for row in fresh['parities'][par]['midpoint']])
    X = arb_mat([[q(v) for v in row] for row in fixed['parities'][par]['X']])
    F = arb_mat([[q(str(v)) for v in row] for row in d['Fhat']])
    correction = F.transpose()*(X+X.transpose()-X.transpose()*A*X)*F
    correction = np.array([[ldarb(correction[i,j]) for j in range(12)] for i in range(12)])
    KP = direct-correction
    # Analytic near-zero inequality evaluated numerically for a W-unit majorant.
    W = np.linalg.inv(np.linalg.cholesky(np.array(G,dtype=float))).T
    maxA = np.linalg.eigvalsh(W.T@np.array(d['derivative_gram'])@W)[-1]
    maxJ = np.linalg.eigvalsh(W.T@np.array(d['jump_gram'])@W)[-1]
    t = float(h*LD(2)**(-depth))
    near = maxA*(t**3/3+t*t/4)+2*np.sqrt(maxA*maxJ)*(2*t**2.5/5+t**1.5/3)+maxJ*(t*t/2+t/2)
    checks = {}
    for case in ('even','odd'):
        if case != par: continue
        f = json.loads(bound(f'research/x-c1/shell-polynomial-direction-search-2026-10-17/data/FROZEN_{par}.json'))
        c = np.array([LD(str(Fraction(v).numerator))/LD(str(Fraction(v).denominator)) for v in f['raw_exact_rational_coefficients']])
        c /= np.sqrt(c@G@c)
        cert = json.loads(bound(f'research/x-c1/sharp-kp-frozen-directions-2026-10-17/expected/SHARP_K_{par}.json'))
        ref = sum(float(Fraction(v)) for v in cert['actual_K_P_interval'])/2
        checks['frozen_K_model'] = float(c@KP@c)
        checks['frozen_directed_K_midpoint'] = ref
        checks['frozen_K_difference'] = float(c@KP@c)-ref
        assert abs(checks['frozen_K_difference']) < 1e-9
    out={'status':'EXPLORATORY_NOT_DIRECTED','parity':par,'G_W':np.array(G,dtype=float).tolist(),
         'direct_form':np.array(direct,dtype=float).tolist(),'finite_response_correction':np.array(correction,dtype=float).tolist(),
         'K_P_model':np.array(KP,dtype=float).tolist(),'near_zero_W_unit_majorant_diagnostic':near,
         'outer_nodes':outer,'inner_nodes':inner,'dyadic_depth':depth,'panels':len(panels),'checks':checks,
         'longdouble_epsilon':str(np.finfo(LD).eps),'new_directed_certificate':False}
    DATA.mkdir(parents=True,exist_ok=True)
    (DATA/f'K_MAP_{par}_{outer}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(par,outer,'K eig',np.linalg.eigvalsh(np.array(KP,dtype=float)),checks,flush=True)
    return out

if __name__=='__main__':
    build(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
