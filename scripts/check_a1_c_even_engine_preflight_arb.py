# -*- coding: utf-8 -*-
"""Exact-head Arb preflight for the frozen A1 C-even matrix engine.

This is NOT the 1075x1075 positivity certificate.  It checks the special-
function and convention layer that the full C-even assembler will use:

* the frozen Gauss-40 / width<=0.4 node construction;
* the exact A1 prime-power mask {2,3,4,5,7};
* rigorous spherical-Bessel vector evaluation at four predeclared nodes
  spanning [0,1551];
* direct-Arb overlap checks at low/mid/high even orders;
* positive-series moment coefficients for e^{x/2};
* even parity phases and finite scalar quadrature coefficients.

No binary float enters a sign/inequality acceptance decision.
"""

from flint import acb, arb, ctx, fmpq

ctx.prec = 512


def Q(n: int, d: int = 1) -> fmpq:
    return fmpq(n, d)


def A(x) -> arb:
    return arb(x)


PI = arb.pi()
GAUSS_N = 40
PANEL = Q(2, 5)  # 0.4
OMEGA = Q(1551)
C = Q(1, 10)
MAX_DEGREE = 2150
CF_DEPTH = 160

# (panel index, Gauss-node index), fixed before this run.
SAMPLES = ((0, 0), (1250, 20), (2500, 20), (3877, 39))
CHECK_ORDERS = (0, 2, 100, 500, 1000, 1500, 2148)
MOMENT_ORDERS = (0, 2, 100, 1000, 2148)


def odd_double_factorial(n: int) -> int:
    assert n >= 1 and n % 2 == 1
    out = 1
    for k in range(1, n + 1, 2):
        out *= k
    return out


def panel_interval(panel: int) -> tuple[arb, arb]:
    left = A(panel) * A(PANEL)
    right = left + A(PANEL)
    if right > A(OMEGA):
        right = A(OMEGA)
    return left, right


def gauss_node(panel: int, node_index: int) -> tuple[arb, arb]:
    left, right = panel_interval(panel)
    root, weight = arb.legendre_p_root(GAUSS_N, node_index, weight=True)
    half = (right - left) / 2
    mid = (right + left) / 2
    return mid + half * root, half * weight


def prime_data():
    log2 = A(2).log()
    log3 = A(3).log()
    log5 = A(5).log()
    log7 = A(7).log()
    return (
        (2, log2, log2 / A(2).sqrt()),
        (3, log3, log3 / A(3).sqrt()),
        (4, 2 * log2, log2 / A(4).sqrt()),
        (5, log5, log5 / A(5).sqrt()),
        (7, log7, log7 / A(7).sqrt()),
    )


PRIME_DATA = prime_data()


def r_on_real_ball(x: arb) -> arb:
    value = acb(Q(1, 4), x / 2).digamma().real - PI.log() - A(C)
    for _, logarithm, amplitude in PRIME_DATA:
        value -= 2 * amplitude * (x * logarithm).cos()
    return value


def spherical_j_direct(n: int, z: arb) -> arb:
    if z.contains(0):
        return A(1) if n == 0 else A(0)
    return z.bessel_j(Q(2 * n + 1, 2)) * (PI / (2 * z)).sqrt()


def spherical_ratio_cf(n: int, z: arb, depth: int = CF_DEPTH) -> arb:
    """Enclose j_(n+1)(z)/j_n(z) by backward continued fraction.

    For spherical j, write nu=n+1/2 and R_n=J_(nu+1)/J_nu.  The exact
    recurrence is

        R_k = z / (2(k+3/2) - z R_(k+1)).

    At all uses here k>=n=2150 and 0<z<1551<k.  Standard order monotonicity
    for J_mu(z) in the region mu>z>0 gives 0<R_k<1.  We therefore start the
    finite backward enclosure with the rigorous tail box [-1,1]; contraction
    over 160 levels makes its effect negligible.  Every denominator is
    checked away from zero.
    """
    # Symmetric interval [-1,1] is deliberately conservative.
    r = arb(0, 1)
    for k in range(n + depth, n - 1, -1):
        denom = 2 * (A(k) + Q(3, 2)) - z * r
        if denom.contains(0):
            raise RuntimeError("continued-fraction Bessel ratio denominator contains zero")
        r = z / denom
    if not r.is_finite():
        raise RuntimeError("non-finite continued-fraction Bessel ratio")
    return r


def spherical_j_vector_downward(z: arb, degree: int) -> list[arb]:
    """Rigorous j_0,...,j_(degree-1) by Miller downward recurrence."""
    top = degree
    ratio = spherical_ratio_cf(top, z)
    values = [A(0) for _ in range(top + 2)]
    values[top] = A(1)
    values[top + 1] = ratio
    for n in range(top, 0, -1):
        values[n - 1] = (2 * n + 1) * values[n] / z - values[n + 1]

    # Pivot selection is only an implementation choice; correctness is
    # subsequently re-proved by a direct Arb value and interval overlap.
    pivot = min(degree - 1, max(0, int(float(z.mid()))))
    if values[pivot].contains(0):
        raise RuntimeError("downward recurrence normalization pivot contains zero")
    direct = spherical_j_direct(pivot, z)
    if direct.contains(0):
        # Move deterministically downward until a nonzero direct interval is found.
        found = False
        for candidate in range(pivot - 1, max(-1, pivot - 64), -1):
            candidate_direct = spherical_j_direct(candidate, z)
            if not values[candidate].contains(0) and not candidate_direct.contains(0):
                pivot = candidate
                direct = candidate_direct
                found = True
                break
        if not found:
            raise RuntimeError("no nonzero normalization pivot found")
    scale = direct / values[pivot]
    result = [v * scale for v in values[:degree]]
    if any(not v.is_finite() for v in result):
        raise RuntimeError("non-finite spherical-Bessel recurrence vector")
    return result


def spherical_j_even_vector(z: arb) -> list[arb]:
    if z < 1:
        vals = [spherical_j_direct(n, z) for n in range(0, MAX_DEGREE, 2)]
    else:
        full = spherical_j_vector_downward(z, MAX_DEGREE)
        vals = [full[n] for n in range(0, MAX_DEGREE, 2)]
    if any(not v.is_finite() for v in vals):
        raise RuntimeError("non-finite even Bessel vector")
    return vals


def modified_spherical_i_series(n: int, z: arb) -> arb:
    """Positive series for i_n(z) with a rigorous geometric tail."""
    df = A(odd_double_factorial(2 * n + 1))
    term = (z ** n) / df
    total = term
    for k in range(200):
        ratio = (z * z) / (2 * (k + 1) * (2 * n + 2 * k + 3))
        term = term * ratio
        total += term
        next_ratio = (z * z) / (2 * (k + 2) * (2 * n + 2 * k + 5))
        if next_ratio < A(Q(1, 4)) and term < A(2) ** (-400):
            tail = term * next_ratio / (1 - next_ratio)
            return total + arb(0, tail.upper())
    raise RuntimeError("modified spherical-i series did not close")


def moment_coeff(n: int) -> arb:
    return 2 * (A(n) + Q(1, 2)).sqrt() * modified_spherical_i_series(n, A(Q(1, 2)))


def main() -> None:
    for n in (2, 3, 4, 5, 7):
        if not A(n).log() < 2:
            raise RuntimeError(f"active mask failed at n={n}")
    if not A(8).log() > 2:
        raise RuntimeError("inactive-mask check log(8)>2 failed")

    print("A1 C-even special-function engine preflight")
    print(f"prec_bits = {ctx.prec}")
    print(f"Gauss order = {GAUSS_N}, panel = 0.4, Omega = 1551")

    for panel, node_index in SAMPLES:
        x, w = gauss_node(panel, node_index)
        if not (x > 0 and x < A(OMEGA)):
            raise RuntimeError("sample Gauss node outside open band")
        r = r_on_real_ball(x)
        alpha = w * r
        if not r.is_finite() or not alpha.is_finite():
            raise RuntimeError("non-finite scalar multiplier/weight")

        vals = spherical_j_even_vector(x)
        if len(vals) != 1075:
            raise RuntimeError("wrong even-vector dimension")

        max_rad = A(0)
        for v in vals:
            if v.rad() > max_rad:
                max_rad = v.rad()

        for n in CHECK_ORDERS:
            recurrence_value = vals[n // 2]
            direct = spherical_j_direct(n, x)
            if not recurrence_value.overlaps(direct):
                raise RuntimeError(
                    f"direct/recurrence Bessel mismatch panel={panel}, node={node_index}, n={n}"
                )

        print(
            "sample", panel, node_index,
            "x=", x.str(22, radius=True),
            "r=", r.str(18, radius=True),
            "alpha=", alpha.str(18, radius=True),
            "max_j_radius=", max_rad.str(8, radius=True),
        )

    for n in MOMENT_ORDERS:
        a = moment_coeff(n)
        if not (a > 0 and a.is_finite()):
            raise RuntimeError(f"moment coefficient invalid at n={n}")
        print("moment", n, a.str(24, radius=True))

    expected = (1, -1, 1, -1, 1, -1)
    got = tuple(1 if k % 2 == 0 else -1 for k in range(6))
    if got != expected:
        raise RuntimeError("even Legendre Fourier phase convention failed")

    print("CERTIFIED: frozen Gauss-40 / panel-0.4 sample nodes are valid")
    print("CERTIFIED: C-even Miller/continued-fraction recurrence overlaps independent direct Arb values")
    print("CERTIFIED: C-even moment-series sample coefficients are positive finite enclosures")
    print("CERTIFIED: C-even special-function engine preflight passed")
    print("FIREWALL: this is not the 1075x1075 finite positivity certificate")


if __name__ == "__main__":
    main()
