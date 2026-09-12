#!/usr/bin/env python3
"""Arb-ball certificate for the R=1 Vor-iota' 7D cross-bridge firewall.

Scope
-----
This checker treats only the PR-#91 odd Prime-2 calibration witness at R=1.
It certifies the Chebyshev degree-N enclosure for the canonical bounded-transform
cross bridge

    M = H (I+H*H)^(-1) (I+A)^(-1) T*,
    T = \\widetilde R_1,  A = T*T = R_1*R_1,

whose same-source cross correction is

    X_7D(a,b) = <P_H a, P_R b> + <P_R a, P_H b>,
    P_H = H*H (I+H*H)^(-1),
    P_R = A (I+A)^(-1).

The code uses exact exponent tuples for lobe centres and python-flint Arb balls
for every coefficient, logarithm, square root and Prime-power weight.  It does
not prune small amplitudes.  Cutoff decisions are accepted only when the whole
bump support is rigorously on one side of the relevant boundary.  Before the
final tuplewise inner products, all distinct output lobe centres are certified
more than 2*EPS apart.

This is a finite-window / finite-degree certificate, not an Object-X or RH
certificate and not a universal no-go for cross-term geometries.

Dependency: python-flint (tested design target: flint.arb, precision 200 bits).
"""
from __future__ import annotations

from collections import defaultdict
import math

try:
    from flint import arb, ctx
except ImportError as exc:  # pragma: no cover - explicit dependency firewall
    raise SystemExit(
        "python-flint is required: install a version providing `from flint import arb, ctx`"
    ) from exc

ctx.prec = 200

PRIMES = (2, 3, 5, 7)
IDX = {p: i for i, p in enumerate(PRIMES)}
ACTIVE_H = ((2, 1), (2, 2), (3, 1), (5, 1), (7, 1))
SECTORS = ((2, 0), (2, 1), (3, 0), (5, 0), (7, 0))
K_MAX = 12  # safely beyond every possible R=1 translated overlap
N = 13
L_H = 16
L_R = 32
EPS = arb("1e-8")
ZERO = arb(0)
ONE = arb(1)
TWO = arb(2)
LOG = {p: arb(p).log() for p in PRIMES}


def pos(x: arb) -> bool:
    """True only if the Arb comparison proves x>0."""
    return bool(x > ZERO)


def key_float(key: tuple[int, ...]) -> float:
    """Ordering aid only.  Every adjacent order/gap is re-certified with Arb."""
    return sum(key[i] * math.log(PRIMES[i]) for i in range(4)) / 2.0


def key_ball(key: tuple[int, ...]) -> arb:
    out = arb(0)
    for i, p in enumerate(PRIMES):
        out += arb(key[i]) * LOG[p] / 2
    return out


def e_shift(p: int, k: int) -> tuple[int, ...]:
    out = [0, 0, 0, 0]
    out[IDX[p]] = k
    return tuple(out)


def add_key(a: tuple[int, ...], b: tuple[int, ...], sign: int = 1) -> tuple[int, ...]:
    return tuple(a[i] + sign * b[i] for i in range(4))


def add_scaled(out: dict, v: dict, scale: arb) -> None:
    for k, x in v.items():
        out[k] += scale * x


def lincomb(*terms: tuple[arb, dict]) -> dict:
    out = defaultdict(lambda: arb(0))
    for scale, v in terms:
        add_scaled(out, v, scale)
    # Deliberately no numerical pruning: balls containing zero are retained.
    return dict(out)


CUTOFF_DECISIONS = 0


def cut_dict(d: dict, bound: arb, label: str) -> dict:
    """Restrict a lobe dictionary to |u|<bound with rigorous support decisions.

    A normalized lobe centred at c has support in [c-EPS,c+EPS].  It is kept only
    if abs(c)+EPS < bound is proved; it is discarded only if abs(c)-EPS > bound
    is proved.  Any unresolved/straddling case aborts the certificate.
    """
    global CUTOFF_DECISIONS
    out = {}
    for k, coeff in d.items():
        cabs = abs(key_ball(k))
        inside = bound - (cabs + EPS)
        outside = (cabs - EPS) - bound
        if pos(inside):
            out[k] = coeff
        elif pos(outside):
            pass
        else:
            raise AssertionError(
                f"Uncertified cutoff/straddle at {label}: key={k}, center={key_ball(k)}, bound={bound}"
            )
        CUTOFF_DECISIONS += 1
    return out


def inner(a: dict, b: dict) -> arb:
    out = arb(0)
    for k, x in a.items():
        if k in b:
            out += x * b[k]
    return out


def p_pow_neg_3k4(p: int, k: int) -> arb:
    return (-arb(3 * k) * LOG[p] / 4).exp()


def hub_weight(p: int, k: int) -> arb:
    return LOG[p].sqrt() * p_pow_neg_3k4(p, k)


def Hstar_apply(v: dict) -> dict:
    """H_1^*=-H_1, using exactly the active R=1 hub channels."""
    out = defaultdict(lambda: arb(0))
    for center, amp in v.items():
        for p, k in ACTIVE_H:
            sh = e_shift(p, k)
            w = hub_weight(p, k)
            out[add_key(center, sh, +1)] += -w * amp
            out[add_key(center, sh, -1)] += +w * amp
    return cut_dict(dict(out), ONE, "P1/H*")


def H_apply(v: dict) -> dict:
    return {k: -x for k, x in Hstar_apply(v).items()}


def G_apply(v: dict) -> dict:
    """G=H*H."""
    return Hstar_apply(H_apply(v))


def phi_map(v: dict, p: int, a: int) -> dict:
    omega = ONE - arb(a + 1) * LOG[p] / 2
    if not pos(omega):
        return {}
    out = defaultdict(lambda: arb(0))
    for k in range(a + 1, K_MAX + 1):
        sh = e_shift(p, k)
        coeff = p_pow_neg_3k4(p, k)
        for pos_key, amp in v.items():
            out[add_key(pos_key, sh, +1)] += coeff * amp
            out[add_key(pos_key, sh, -1)] -= coeff * amp
    return cut_dict(dict(out), omega, f"Omega({p},{a})")


def K_apply(w: dict, p: int, k: int) -> dict:
    sh = e_shift(p, k)
    out = defaultdict(lambda: arb(0))
    for pos_key, amp in w.items():
        out[add_key(pos_key, sh, +1)] += amp
        out[add_key(pos_key, sh, -1)] -= amp
    return cut_dict(dict(out), ONE, f"P1/K({p},{k})")


def A_apply(v: dict) -> dict:
    """A=R_1^*R_1 from P11 (3.4)/(3.5), no sectorwise-square shortcut."""
    out = defaultdict(lambda: arb(0))
    for p, a in SECTORS:
        ph = phi_map(v, p, a)
        if not ph:
            continue
        pref = LOG[p] * arb((p - 1) * (p**a))
        for k in range(a + 1, K_MAX + 1):
            coeff = p_pow_neg_3k4(p, k)
            kw = K_apply(ph, p, k)
            for pos_key, amp in kw.items():
                out[pos_key] += -pref * coeff * amp
    return dict(out)


def cheb_resolvent_defect(v: dict, op, L: int, Ndeg: int) -> tuple[dict, arb]:
    """Degree-N Chebyshev approximation to P=op/(I+op) on spec(op) subset [0,L]."""
    Lb = arb(L)
    s = (ONE + Lb).sqrt()
    q = (s - ONE) / (s + ONE)

    # r(t)=1/(1+t)=1/s*[1+2 sum_{n>=1}(-q)^n T_n(2t/L-1)]
    t0 = v
    t1 = lincomb((TWO / Lb, op(v)), (-ONE, v))
    rN = defaultdict(lambda: arb(0))
    add_scaled(rN, t0, ONE / s)
    if Ndeg >= 1:
        add_scaled(rN, t1, (TWO / s) * (-q))

    prev, cur = t0, t1
    for n in range(1, Ndeg):
        ycur = lincomb((TWO / Lb, op(cur)), (-ONE, cur))
        nxt = lincomb((TWO, ycur), (-ONE, prev))
        add_scaled(rN, nxt, (TWO / s) * ((-q) ** (n + 1)))
        prev, cur = cur, nxt

    pN = lincomb((ONE, v), (-ONE, dict(rN)))
    eps = (TWO / s) * (q ** (Ndeg + 1)) / (ONE - q)
    return pN, eps


def certify_final_disjoint(*vectors: dict) -> None:
    keys = set()
    for v in vectors:
        keys.update(v.keys())
    ordered = sorted(keys, key=key_float)
    for left, right in zip(ordered, ordered[1:]):
        # This simultaneously certifies the float-assisted ordering and non-overlap.
        gap = key_ball(right) - key_ball(left) - TWO * EPS
        if not pos(gap):
            raise AssertionError(
                f"Final lobe separation not certified: {left} -> {right}; gap={gap}"
            )


def spectral_boxes() -> tuple[arb, arb]:
    # ||H|| <= 2 sum_{active p,k} sqrt(log p) p^(-3k/4)
    hnorm = arb(0)
    for p, k in ACTIVE_H:
        hnorm += TWO * hub_weight(p, k)
    gbound = hnorm * hnorm
    if not pos(arb(L_H) - gbound):
        raise AssertionError(f"H*H spectral box L_H={L_H} not certified; bound={gbound}")

    # ||A|| <= sum_s c_s ||Phi_s||^2, with
    # ||Phi_{p,a}|| <= 2 sum_{k>=a+1} p^(-3k/4), bounded by the infinite geometric tail.
    abound = arb(0)
    for p, a in SECTORS:
        r = p_pow_neg_3k4(p, 1)
        geom = (r ** (a + 1)) / (ONE - r)
        phi_norm = TWO * geom
        c = LOG[p] * arb((p - 1) * (p**a))
        abound += c * phi_norm * phi_norm
    if not pos(arb(L_R) - abound):
        raise AssertionError(f"A spectral box L_R={L_R} not certified; bound={abound}")
    return gbound, abound


def main() -> None:
    sq2 = arb(2).sqrt()
    amp = ONE / sq2

    # Same exact half-log tuple centres as the merged PR-#96 checker.
    a = {
        (0, 0, 1, 0): amp,
        (0, 0, -1, 0): amp,
    }
    b = {
        (-2, 0, 1, 0): amp,
        (2, 0, -1, 0): amp,
    }

    gbound, abound = spectral_boxes()

    PHa, epsH = cheb_resolvent_defect(a, G_apply, L_H, N)
    PHb, _ = cheb_resolvent_defect(b, G_apply, L_H, N)
    PRa, epsR = cheb_resolvent_defect(a, A_apply, L_R, N)
    PRb, _ = cheb_resolvent_defect(b, A_apply, L_R, N)

    # The tail bound is a scalar function of (L,N), hence source-independent.

    certify_final_disjoint(PHa, PHb, PRa, PRb)

    XN = inner(PHa, PRb) + inner(PRa, PHb)
    # ||P_H||,||P_R|| <= 1 and ||a||=||b||=1 give
    # |X-XN| <= 2(epsH+epsR+epsH epsR).
    cheb_error = TWO * (epsH + epsR + epsH * epsR)
    Xlo = XN - cheb_error
    Xhi = XN + cheb_error

    log2 = LOG[2]
    Xreq = -(arb(4) + sq2) * log2 / 32
    reserve = Xlo - Xreq
    if not pos(reserve):
        raise AssertionError(f"FAIL certificate did not separate target: reserve={reserve}")

    print("Vor-iota' 7D.1-HARDEN -- Arb certificate")
    print(f"precision_bits = {ctx.prec}")
    print(f"degree_N       = {N}")
    print(f"epsilon        = {EPS}")
    print(f"||H*H|| bound  = {gbound} < {L_H}")
    print(f"||A|| bound    = {abound} < {L_R}")
    print(f"X_N            = {XN}")
    print(f"eps_H          = {epsH}")
    print(f"eps_R          = {epsR}")
    print(f"DeltaX_cheb    = {cheb_error}")
    print(f"X_7D enclosure = [{Xlo}, {Xhi}]")
    print(f"X_req          = {Xreq}")
    print(f"Xlo-Xreq       = {reserve}")
    print(f"cutoff decisions certified = {CUTOFF_DECISIONS}")
    print(f"final support sizes: PHa={len(PHa)}, PHb={len(PHb)}, PRa={len(PRa)}, PRb={len(PRb)}")
    print("PASS: X_req < Xlo; 7D d-exact FAIL in the stated R=1 Prime-2 scope.")
    print("NONCLAIM: no universal mediator/cross-term/Object-X/RH no-go.")


if __name__ == "__main__":
    main()
