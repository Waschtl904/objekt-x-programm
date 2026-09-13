# -*- coding: utf-8 -*-
"""Rigorous Arb certificate for the short-window NP-GAP threshold.

This script certifies the unique root a_* of

    B(a) = kappa_*

where

    B(a) = 4*pi^2/(pi^2+a^2)
           + sum_{m>=1} (2/alpha_m) exp(-alpha_m a),
    alpha_m = 2*m + 1/2,
    kappa_* = log(8*pi) + gamma + pi/2.

The infinite tail is enclosed rigorously by a geometric majorant.  No float
conversion is used in any acceptance test.
"""

from flint import arb, ctx

ctx.prec = 256

PI = arb.pi()
GAMMA = arb.const_euler()
KAPPA = (8 * PI).log() + GAMMA + PI / 2


def alpha(m: int) -> arb:
    return arb(2 * m) + arb(1) / 2


def B_ball(a: arb, M: int = 700) -> arb:
    """Rigorous enclosure of B(a) using M higher channels plus a tail ball."""
    first = 4 * PI * PI / (PI * PI + a * a)
    s = arb(0)
    for m in range(1, M + 1):
        al = alpha(m)
        s += (2 / al) * (-al * a).exp()

    al_next = alpha(M + 1)
    q = (-2 * a).exp()
    tail_upper = (2 / al_next) * (-al_next * a).exp() / (1 - q)

    # The true positive tail lies in [0, tail_upper].
    tail_ball = tail_upper / 2 + arb(0, tail_upper / 2)
    return first + s + tail_ball


def main() -> None:
    # 1e-13-wide rational-decimal bracket around the root.
    lo = arb("0.1033784517534")
    hi = arb("0.1033784517535")

    Blo = B_ball(lo)
    Bhi = B_ball(hi)

    if not (Blo > KAPPA):
        raise RuntimeError(f"lower endpoint not certified above kappa: B(lo)={Blo}, kappa={KAPPA}")
    if not (Bhi < KAPPA):
        raise RuntimeError(f"upper endpoint not certified below kappa: B(hi)={Bhi}, kappa={KAPPA}")

    half_log2 = arb(2).log() / 2
    if not (hi < half_log2):
        raise RuntimeError(f"root bracket does not lie below log(2)/2: hi={hi}, log2/2={half_log2}")

    print("NP-GAP short-window Arb certificate")
    print(f"prec_bits = {ctx.prec}")
    print(f"kappa_*   = {KAPPA.str(40)}")
    print(f"B(lo)     = {Blo.str(40)}")
    print(f"B(hi)     = {Bhi.str(40)}")
    print(f"a_* in    = [{lo.str(20, radius=False)}, {hi.str(20, radius=False)}]")
    print(f"log(2)/2  = {half_log2.str(40)}")
    print("CERTIFIED: unique root a_* lies in the bracket and a_* < log(2)/2")


if __name__ == "__main__":
    main()
