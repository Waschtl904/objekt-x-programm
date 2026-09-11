#!/usr/bin/env python3
"""Support-separation diagnostic for the epsilon-refined PR91 witness.

Exact positions are encoded by prime-exponent tuples; floats are used only to
measure positive geometric margins.  The generated post-cancellation position
set for m0/m1/m2 has minimum pair separation ~0.00222717.  Choosing epsilon
below one quarter of this margin keeps distinct bump supports disjoint.
"""
from collections import defaultdict
import math

P = (2, 3, 5, 7)
IDX = {p: i for i, p in enumerate(P)}
ACTIVE_H = ((2, 1), (2, 2), (3, 1), (5, 1), (7, 1))
SECTORS = ((2, 0), (2, 1), (3, 0), (5, 0), (7, 0))


def key_float(k):
    return sum(k[i] * math.log(P[i]) for i in range(4)) / 2.0


def eshift(p, k):
    x = [0, 0, 0, 0]
    x[IDX[p]] = k
    return tuple(x)


def add(a, b, s=1):
    return tuple(a[i] + s * b[i] for i in range(4))


def clean(d):
    return {k: v for k, v in d.items() if abs(v) > 1e-13}


def P1(d):
    return {k: v for k, v in d.items() if abs(key_float(k)) < 1 - 1e-10}


def build_H(cs):
    d = defaultdict(float)
    for c, coef in cs:
        for p, k in ACTIVE_H:
            w = math.sqrt(math.log(p)) * p ** (-3*k/4)
            sh = eshift(p, k)
            for sig in (+1, -1):
                d[add(c, sh, sig)] += -sig * w * coef
    return clean(P1(d))


def combine(a, b, s):
    d = defaultdict(float)
    for k, v in a.items(): d[k] += v
    for k, v in b.items(): d[k] += s*v
    return clean(d)


def phi(v, p, a, kmax=12):
    omega = 1 - (a+1)*math.log(p)/2
    if omega <= 0: return {}
    d = defaultdict(float)
    for k in range(a+1, kmax+1):
        co = p**(-3*k/4)
        sh = eshift(p, k)
        for q, A in v.items():
            d[add(q, sh, +1)] += co*A
            d[add(q, sh, -1)] -= co*A
    d = clean(d)
    return {q:A for q,A in d.items() if abs(key_float(q)) <= omega + 1e-10}


def K(w, p, k):
    d = defaultdict(float)
    sh = eshift(p, k)
    for q, A in w.items():
        d[add(q, sh, +1)] += A
        d[add(q, sh, -1)] -= A
    return clean(P1(d))


def A_positions(v):
    out = defaultdict(float)
    phipos = set()
    for p, a in SECTORS:
        ph = phi(v, p, a)
        phipos.update(ph)
        pref = math.log(p)*(p-1)*p**a
        for k in range(a+1, 13):
            co = p**(-3*k/4)
            for q, A in K(ph, p, k).items():
                out[q] += -pref*co*A
    return phipos, set(clean(out))


def main():
    r2 = math.sqrt(2)
    ac = [((0,0,1,0),1/r2),((0,0,-1,0),1/r2)]
    bc = [((-2,0,1,0),1/r2),((2,0,-1,0),1/r2)]
    x,y = build_H(ac),build_H(bc)
    vp,vm = combine(x,y,+1),combine(x,y,-1)

    relevant = set(vp) | set(vm)
    for v in (vp, vm):
        pp, aa = A_positions(v)
        relevant |= pp | aa

    vals = sorted((key_float(k), k) for k in relevant)
    min_sep = min(vals[i+1][0] - vals[i][0] for i in range(len(vals)-1))
    eps_max = min_sep / 4.0

    print(f"distinct post-cancellation relevant positions: {len(relevant)}")
    print(f"minimum pair separation: {min_sep:.15f}")
    print(f"epsilon_max=min_sep/4:  {eps_max:.15e}")

    for eps in (1e-4, 1e-5, 1e-6, 1e-8, 1e-10):
        ok = eps < eps_max
        print(f"epsilon={eps:.0e}: {'PASS' if ok else 'FAIL'}")
        if not ok: raise SystemExit(1)

    # The Cloud package used the same limiting value (~5.57e-4).  The count
    # here is explicitly the post-cancellation generated set (103), not a
    # claim that every bookkeeping convention must count the same raw nodes.
    assert min_sep > 0.00222
    assert eps_max > 5.5e-4
    print("PASS: support combinatorics stable throughout the tested epsilon range.")


if __name__ == '__main__':
    main()
