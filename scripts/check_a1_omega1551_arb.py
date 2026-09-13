# -*- coding: utf-8 -*-
"""Rigorous Arb certificate reducing the a=1 dangerous frequency band to |xi|<1551.

We certify

    m_1(xi) > 0.1  for every |xi| >= 1551,

where

    m_1(xi) = Re psi(1/4+i xi/2) - log(pi)
              -2 sum_{n in {2,3,4,5,7}} Lambda(n)/sqrt(n) cos(xi log n).

Strategy:
  1. On [1551,2500], use a rational grid of spacing 1/50.  Every grid-point
     value is bounded below with the positive DLMF digamma series plus a
     rigorous integral tail.  A rigorous global derivative bound converts
     pointwise grid lower bounds into an interval bound.
  2. On [2500,infinity), use cos<=1 and monotonicity of the same digamma lower
     bound, evaluated only at xi=2500.
  3. Combine c=0.1 and Omega=1551 with the Karnik--Romberg--Davenport PSWF
     bound at N=1210, and certify an explicit Schur penalty <2.2e-39.

All acceptance predicates use Arb intervals only; no Python floats enter proof
comparisons.
"""

from flint import arb, ctx

ctx.prec = 256

PI = arb.pi()
GAMMA = arb.const_euler()
LOG2 = arb(2).log()
X0 = arb(1) / 4
PSI_QUARTER = -GAMMA - PI / 2 - 3 * LOG2

ACTIVE = ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7))


def weight(n: int, p: int) -> arb:
    return arb(p).log() / arb(n).sqrt()


WEIGHTS = tuple(weight(n, p) for n, p in ACTIVE)
W = sum(WEIGHTS, arb(0))
KAPPA = PI.log() - PSI_QUARTER
GAMMA1 = KAPPA + 2 * W

# Predeclared proof parameters.
OMEGA = arb(1551)
FAR = arb(2500)
C = arb("0.1")
GRID_DEN = 50                    # spacing 0.02
GRID_HALF = arb(1) / (2 * GRID_DEN)
GRID_POINT_FLOOR = arb("0.19")
LIPSCHITZ_CAP = arb("8.22")
SERIES_N = 64
M = arb(12)
PROLATE_N = 1210
SHANNON_CEIL = 988
LAMBDA_TARGET = arb("1.5e-42")
TAU_FLOOR = arb("0.099")
SCHUR_TARGET = arb("2.2e-39")
RESOLVED_TARGET = arb("3e-39")


def f_term(u: arb, yy: arb) -> arb:
    return yy / (u * (u * u + yy))


def digamma_increment_lower_y(y: arb) -> arb:
    yy = y * y
    s = arb(0)
    for k in range(SERIES_N):
        u = arb(k) + X0
        s += f_term(u, yy)
    u0 = arb(SERIES_N) + X0
    s += (1 + yy / (u0 * u0)).log() / 2
    return s


def digamma_increment_upper_y(y: arb) -> arb:
    yy = y * y
    s = arb(0)
    for k in range(SERIES_N):
        u = arb(k) + X0
        s += f_term(u, yy)
    u0 = arb(SERIES_N) + X0
    # decreasing tail: sum_{k=N} f(k+x) <= f(N+x)+ integral_N^inf f(t+x)dt
    s += f_term(u0, yy) + (1 + yy / (u0 * u0)).log() / 2
    return s


def point_multiplier_lower(xi: arb) -> arb:
    y = xi / 2
    arch = PSI_QUARTER + digamma_increment_lower_y(y) - PI.log()
    prime = arb(0)
    for (n, _p), w in zip(ACTIVE, WEIGHTS):
        prime += w * (xi * arb(n).log()).cos()
    return arch - 2 * prime


def derivative_bound() -> arb:
    """Uniform |m_1'| upper bound for xi>=OMEGA."""
    y = OMEGA / 2
    # |d/dxi Re psi(1/4+i xi/2)| <= 1/2 |psi'(z)|.
    # Sum 1/((k+x)^2+y^2) <= first term + integral_0^inf.
    trigamma_abs = 1 / (X0 * X0 + y * y) + (PI / 2 - (X0 / y).atan()) / y
    arch_der = trigamma_abs / 2
    prime_der = arb(0)
    for (n, _p), w in zip(ACTIVE, WEIGHTS):
        prime_der += 2 * w * arb(n).log()
    return arch_der + prime_der


def far_worst_lower() -> arb:
    y = FAR / 2
    # For xi>=FAR, the digamma increment is monotone in |xi| and every cos<=1.
    return PSI_QUARTER + digamma_increment_lower_y(y) - PI.log() - 2 * W


def band_r_upper() -> arb:
    # On |xi|<=OMEGA, digamma increment increases with |xi|; prime term <= +2W.
    y = OMEGA / 2
    m_upper = PSI_QUARTER + digamma_increment_upper_y(y) - PI.log() + 2 * W
    return m_upper - C


def krd_upper(k: int) -> arb:
    denom = (2 / (PI * PI)) * (100 * OMEGA / PI + 25).log()
    exponent = -(arb(k - SHANNON_CEIL - 6)) / denom
    return 10 * exponent.exp()


def main() -> None:
    if not (arb(7).log() < 2 and arb(8).log() > 2):
        raise RuntimeError("active a=1 prime-power set not certified")

    # Rigorous derivative bound.
    lip = derivative_bound()
    if not (lip < LIPSCHITZ_CAP):
        raise RuntimeError(f"Lipschitz cap failed: {lip}")

    # Exact rational grid on [1551,2500].
    count = (2500 - 1551) * GRID_DEN
    min_seen = None
    for j in range(count + 1):
        xi = arb(1551 * GRID_DEN + j) / GRID_DEN
        lb = point_multiplier_lower(xi)
        if not (lb > GRID_POINT_FLOOR):
            raise RuntimeError(f"grid lower bound failed at j={j}, xi={xi}, lb={lb}")
        if min_seen is None or lb < min_seen:
            min_seen = lb

    # Every point in the compact interval lies within GRID_HALF of a grid point.
    compact_floor = GRID_POINT_FLOOR - LIPSCHITZ_CAP * GRID_HALF
    if not (compact_floor > C):
        raise RuntimeError(f"compact interval margin failed: {compact_floor}")

    # Monotone far-field certificate.
    far_lb = far_worst_lower()
    if not (far_lb > C):
        raise RuntimeError(f"far-field lower bound failed: {far_lb}")

    # Compact-band bound for r=(m_1-C)1_band.
    if not (GAMMA1 + C < M):
        raise RuntimeError(f"lower-side r norm bound failed: {GAMMA1+C}")
    r_upper = band_r_upper()
    if not (r_upper < M):
        raise RuntimeError(f"upper-side r norm bound failed: {r_upper}")

    # KRD PSWF bound for c=Omega=1551.
    shannon = 2 * OMEGA / PI
    if not (arb(987) < shannon and shannon < arb(988)):
        raise RuntimeError(f"failed 987 < 2c/pi < 988: {shannon}")

    lam = krd_upper(PROLATE_N)
    if not (lam < LAMBDA_TARGET):
        raise RuntimeError(f"KRD lambda_1210 bound failed: {lam}")

    tau = C - (GAMMA1 + C) * lam
    if not (tau > TAU_FLOOR):
        raise RuntimeError(f"tail floor failed: {tau}")

    cross_sq = M * M * lam
    schur = cross_sq / tau
    if not (schur < SCHUR_TARGET):
        raise RuntimeError(f"Schur penalty failed: {schur}")
    if not (RESOLVED_TARGET > SCHUR_TARGET):
        raise RuntimeError("resolved target does not dominate declared Schur target")

    print("A1 Omega=1551 reduced-band Arb certificate")
    print(f"prec_bits             = {ctx.prec}")
    print(f"Gamma_1               = {GAMMA1.str(50)}")
    print(f"Lipschitz bound       = {lip.str(50)}")
    print(f"grid point minimum    = {min_seen.str(50)}")
    print(f"compact certified lb  = {compact_floor.str(50)}")
    print(f"far-field lb @2500    = {far_lb.str(50)}")
    print(f"band r upper          = {r_upper.str(50)}")
    print(f"2c/pi                 = {shannon.str(50)}")
    print(f"PSWF index            = {PROLATE_N}")
    print(f"KRD lambda_1210 ub    = {lam.str(60)}")
    print(f"tail tau              = {tau.str(60)}")
    print(f"Schur penalty ub      = {schur.str(60)}")
    print(f"resolved target       = {RESOLVED_TARGET.str(20, radius=False)}")
    print("CERTIFIED: m_1(xi) > 0.1 for every |xi| >= 1551")
    print("CERTIFIED: ||r||_infty < 12 on |xi|<=1551")
    print("CERTIFIED: PSWF lambda_1210(c=1551) < 1.5e-42")
    print("CERTIFIED: Schur penalty < 2.2e-39")
    print("CERTIFIED: resolved lower bound 3e-39 is sufficient for A1 positivity")


if __name__ == "__main__":
    main()
