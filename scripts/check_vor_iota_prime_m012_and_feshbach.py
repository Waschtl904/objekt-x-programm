#!/usr/bin/env python3
"""Reproduce the R=1 Vor-iota' moment and Feshbach firewall diagnostics.

This is a finite symbolic-position / floating-coefficient checker.  It is NOT
an interval certificate.  The actual separation proof used by the audit is the
rational implication in check_vor_iota_prime_rational_certificate.py, applied
to the coarse moment bounds reproduced here.

Conventions follow P11 (3.4)/(3.5):
  K_s^tr = P_1 D_s E_1,
  Phi_{p,a,1} = sum_{k>=a+1} p^(-3k/4) K_{k log p}^tr,
  A = R_1^* R_1 = - sum_{p,a} (log p)(p-1)p^a Phi^*Phi,
where K_s^*=-K_s.  Exact lobe positions are stored as exponent tuples in
(1/2)(n2 log2+n3 log3+n5 log5+n7 log7).
"""
from collections import defaultdict
import math

PRIMES = (2, 3, 5, 7)
IDX = {p: i for i, p in enumerate(PRIMES)}
ACTIVE_H = ((2, 1), (2, 2), (3, 1), (5, 1), (7, 1))
SECTORS = ((2, 0), (2, 1), (3, 0), (5, 0), (7, 0))
TOL = 2e-12


def key_float(key):
    return sum(key[i] * math.log(PRIMES[i]) for i in range(4)) / 2.0


def e_shift(p, k):
    out = [0, 0, 0, 0]
    out[IDX[p]] = k
    return tuple(out)


def add_key(a, b, sign=1):
    return tuple(a[i] + sign * b[i] for i in range(4))


def clean(d, tol=1e-13):
    return {k: v for k, v in d.items() if abs(v) > tol}


def apply_P1(d):
    return {k: v for k, v in d.items() if abs(key_float(k)) < 1.0 - 1e-10}


def combine(a, b, sign):
    out = defaultdict(float)
    for k, v in a.items():
        out[k] += v
    for k, v in b.items():
        out[k] += sign * v
    return clean(out)


def norm2(d):
    return sum(v * v for v in d.values())


def inner(a, b):
    return sum(v * b.get(k, 0.0) for k, v in a.items())


def hub_weight(p, k):
    return math.sqrt(math.log(p)) * p ** (-3.0 * k / 4.0)


def build_Hstar(source_centers):
    """H_1^*=-H_1 applied to lobe centers.

    source_centers: iterable of (tuple, amplitude).  The source amplitudes
    already include 1/sqrt(2).  Equal positions are accumulated BEFORE norms.
    """
    out = defaultdict(float)
    for center, source_amp in source_centers:
        for p, k in ACTIVE_H:
            sh = e_shift(p, k)
            w = hub_weight(p, k)
            for sigma in (+1, -1):
                out[add_key(center, sh, sigma)] += -sigma * w * source_amp
    return clean(apply_P1(out))


def phi_map(v, p, a, k_max=12, collect=None):
    omega = 1.0 - (a + 1) * math.log(p) / 2.0
    if omega <= 0:
        return {}
    out = defaultdict(float)
    for k in range(a + 1, k_max + 1):
        sh = e_shift(p, k)
        coeff = p ** (-3.0 * k / 4.0)
        for pos, amp in v.items():
            out[add_key(pos, sh, +1)] += coeff * amp
            out[add_key(pos, sh, -1)] -= coeff * amp
    out = clean(out)
    out = {q: amp for q, amp in out.items() if abs(key_float(q)) <= omega + 1e-10}
    if collect is not None:
        collect.update(out)
    return out


def K_apply(w, p, k):
    """K_{k log p}^tr=P_1D_{k log p}E_1 on a lobe dictionary."""
    sh = e_shift(p, k)
    out = defaultdict(float)
    for pos, amp in w.items():
        out[add_key(pos, sh, +1)] += amp
        out[add_key(pos, sh, -1)] -= amp
    return clean(apply_P1(out))


def m1(v):
    total = 0.0
    pieces = {}
    for p, a in SECTORS:
        ph = phi_map(v, p, a)
        val = math.log(p) * (p - 1) * p**a * norm2(ph)
        pieces[(p, a)] = val
        total += val
    return total, pieces


def A_apply(v, k_max=12):
    """A v = R_1^*R_1 v from the martingale decomposition.

    Phi^* = -sum_k p^(-3k/4) K_k after zero extension from Omega.
    phi_map already enforces the Omega cutoff on the intermediate vector;
    K_apply enforces P_1 on the output.
    """
    out = defaultdict(float)
    for p, a in SECTORS:
        ph = phi_map(v, p, a, k_max=k_max)
        if not ph:
            continue
        pref = math.log(p) * (p - 1) * p**a
        for k in range(a + 1, k_max + 1):
            coeff = p ** (-3.0 * k / 4.0)
            kw = K_apply(ph, p, k)
            for pos, amp in kw.items():
                out[pos] += -pref * coeff * amp
    return clean(out)


def rest_cross(a_src, b_src):
    total = 0.0
    for p, a in SECTORS:
        pa = phi_map(a_src, p, a)
        pb = phi_map(b_src, p, a)
        total += math.log(p) * (p - 1) * p**a * inner(pa, pb)
    return total


def bounds(m0, m1_, m2):
    lo = m0 * m0 / (m0 + m1_)
    hi = m0 - m1_ * m1_ / (m1_ + m2)
    return lo, hi


def close(name, got, want, tol=TOL):
    diff = abs(got - want)
    print(f"{name:<36} {got:.15f}   diff={diff:.3e}")
    if diff > tol:
        raise SystemExit(f"FAIL: {name}: {got} != {want} within {tol}")


def main():
    sq2 = math.sqrt(2.0)
    a_centers = [((0, 0, 1, 0), 1 / sq2), ((0, 0, -1, 0), 1 / sq2)]
    b_centers = [((-2, 0, 1, 0), 1 / sq2), ((2, 0, -1, 0), 1 / sq2)]
    a_src = dict(a_centers)
    b_src = dict(b_centers)

    x = build_Hstar(a_centers)
    y = build_Hstar(b_centers)
    vp = combine(x, y, +1)
    vm = combine(x, y, -1)

    m0p, m0m = norm2(vp), norm2(vm)
    m1p, sectors_p = m1(vp)
    m1m, sectors_m = m1(vm)
    Avp, Avm = A_apply(vp), A_apply(vm)
    m2p, m2m = norm2(Avp), norm2(Avm)
    adjp, adjm = inner(vp, Avp), inner(vm, Avm)

    expected = {
        "m0(v+)": 1.637322379399263,
        "m0(v-)": 2.617580522867810,
        "m1(v+)": 2.619026483293040,
        "m1(v-)": 4.413637746886540,
        "m2(v+)": 5.827373366984125,
        "m2(v-)": 10.320698292415832,
    }
    close("m0(v+)", m0p, expected["m0(v+)"])
    close("m0(v-)", m0m, expected["m0(v-)"])
    close("m1(v+)", m1p, expected["m1(v+)"])
    close("m1(v-)", m1m, expected["m1(v-)"])
    close("m2(v+)", m2p, expected["m2(v+)"])
    close("m2(v-)", m2m, expected["m2(v-)"])
    close("<v+,Av+>-m1", adjp - m1p, 0.0)
    close("<v-,Av->-m1", adjm - m1m, 0.0)

    print("\nm1 sectors:")
    for s in SECTORS:
        print(f"  {s}: v+={sectors_p[s]:.15f}  v-={sectors_m[s]:.15f}")

    rest = rest_cross(a_src, b_src)
    rest_formula = (4.0 - 7.0 * sq2) * math.log(2.0) / 32.0
    close("<R1 a,R1 b> vs Zug 6.1", rest, rest_formula)

    qplo, qphi = bounds(m0p, m1p, m2p)
    qmlo, qmhi = bounds(m0m, m1m, m2m)
    f_lo = (qplo - qmhi) / 4.0
    f_hi = (qphi - qmlo) / 4.0
    target = -math.log(2.0) / math.sqrt(2.0)

    print("\nResolvent moment bounds:")
    print(f"  Q(v+) in [{qplo:.10f}, {qphi:.10f}]")
    print(f"  Q(v-) in [{qmlo:.10f}, {qmhi:.10f}]")
    print(f"  <Sigma_1 a,b> in [{f_lo:.10f}, {f_hi:.10f}]")
    print(f"  Weil target      = {target:.10f}")
    print(f"  separation gap  = {f_lo - target:.10f}")

    if not (target < f_lo):
        raise SystemExit("FAIL: diagnostic interval does not separate the Weil target")

    # Coarse inequalities consumed by the exact rational implication certificate.
    assert m0p > 1.63
    assert m1p < 2.63
    assert m0m < 2.62
    assert m1m > 4.41
    assert m2m < 10.33

    print("\nPASS: all diagnostics and coarse moment inequalities reproduced.")
    print("NOTE: floating diagnostics are not the formal separation certificate.")


if __name__ == "__main__":
    main()
