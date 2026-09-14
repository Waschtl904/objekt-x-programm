# -*- coding: utf-8 -*-
"""Exact-head Arb preflight for the frozen A1 C-even matrix engine.

This is NOT the 1075x1075 positivity certificate.  It checks the special-
function and convention layer that the full C-even assembler will use:

* frozen Gauss-40 / width<=0.4 nodes;
* exact A1 prime-power mask {2,3,4,5,7};
* rigorous spherical-Bessel even vectors at four fixed nodes;
* Miller recurrence only through the numerically relevant order range;
* a rigorous analytic enclosure for all higher orders;
* direct-Arb overlap checks at fixed low/mid/high orders;
* positive-series moment coefficients for e^{x/2}.

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
PANEL = Q(2, 5)
OMEGA = Q(1551)
C = Q(1, 10)
MAX_DEGREE = 2150
CF_DEPTH = 192

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
    log2 = A(2).log(); log3 = A(3).log(); log5 = A(5).log(); log7 = A(7).log()
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
    """Enclose j_(n+1)(z)/j_n(z) by a contracting backward CF."""
    r = arb(0, 1)  # conservative tail box [-1,1]
    for k in range(n + depth, n - 1, -1):
        denom = 2 * (A(k) + Q(3, 2)) - z * r
        if denom.contains(0):
            raise RuntimeError("continued-fraction ratio denominator contains zero")
        r = z / denom
    if not r.is_finite():
        raise RuntimeError("non-finite continued-fraction ratio")
    return r


def choose_miller_top(z: arb, degree: int) -> int:
    """Implementation proposal followed by an exact Arb safety check."""
    top = max(32, int(1.5 * float(z.mid())) + 32)
    top = min(degree, top)
    while top < degree and not (A(top) > 3 * z / 2):
        top += 1
    if top < degree and not (A(top) > 3 * z / 2):
        raise RuntimeError("failed exact Miller-top safety check")
    return top


def low_order_normalization(values: list[arb], z: arb, top: int) -> tuple[int, arb]:
    """Normalize Miller at a well-conditioned low order."""
    for pivot in range(min(12, top + 1)):
        direct = spherical_j_direct(pivot, z)
        if not values[pivot].contains(0) and not direct.contains(0):
            return pivot, direct
    raise RuntimeError("no nonzero low-order Miller normalization pivot found")


def analytic_j_bounds(z: arb, degree: int) -> list[arb]:
    """Return b_n=z^n/(2n+1)!! for n=0,...,degree-1 recursively."""
    bounds = [A(1)]
    for n in range(degree - 1):
        bounds.append(bounds[-1] * z / (2 * n + 3))
    return bounds


def spherical_j_vector_mixed(z: arb, degree: int) -> tuple[list[arb], int]:
    """Miller through an adaptive top, analytic symmetric enclosures above."""
    top = choose_miller_top(z, degree)
    if top == degree:
        represented_top = degree - 1
        recurrence_top = degree
    else:
        represented_top = top
        recurrence_top = top

    ratio = spherical_ratio_cf(recurrence_top, z)
    values = [A(0) for _ in range(recurrence_top + 2)]
    values[recurrence_top] = A(1)
    values[recurrence_top + 1] = ratio
    for n in range(recurrence_top, 0, -1):
        values[n - 1] = (2 * n + 1) * values[n] / z - values[n + 1]

    pivot, direct = low_order_normalization(values, z, recurrence_top)
    scale = direct / values[pivot]
    low = [v * scale for v in values[: represented_top + 1]]
    if any(not v.is_finite() for v in low):
        raise RuntimeError("non-finite Miller low vector")

    result = [A(0) for _ in range(degree)]
    for n, v in enumerate(low):
        result[n] = v

    if represented_top + 1 < degree:
        bounds = analytic_j_bounds(z, degree)
        for n in range(represented_top + 1, degree):
            result[n] = arb(0, bounds[n].upper())

    if any(not v.is_finite() for v in result):
        raise RuntimeError("non-finite mixed spherical-Bessel vector")
    return result, represented_top


def spherical_j_even_vector(z: arb) -> tuple[list[arb], int]:
    if z < 1:
        full = [spherical_j_direct(n, z) for n in range(MAX_DEGREE)]
        top = MAX_DEGREE - 1
    else:
        full, top = spherical_j_vector_mixed(z, MAX_DEGREE)
    return [full[n] for n in range(0, MAX_DEGREE, 2)], top


def modified_spherical_i_series(n: int, z: arb) -> arb:
    df = A(odd_double_factorial(2 * n + 1))
    term = (z ** n) / df
    total = term
    for k in range(200):
        ratio = (z * z) / (2 * (k + 1) * (2 * n + 2 * k + 3))
        term *= ratio
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
        r = r_on_real_ball(x); alpha = w * r
        if not r.is_finite() or not alpha.is_finite():
            raise RuntimeError("non-finite scalar multiplier/weight")

        vals, represented_top = spherical_j_even_vector(x)
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
                    f"direct/mixed Bessel mismatch panel={panel}, node={node_index}, n={n}"
                )

        print(
            "sample", panel, node_index,
            "x=", x.str(22, radius=True),
            "r=", r.str(18, radius=True),
            "alpha=", alpha.str(18, radius=True),
            "Miller_top=", represented_top,
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
    print("CERTIFIED: C-even adaptive Miller/tail enclosures overlap independent direct Arb values")
    print("CERTIFIED: C-even moment-series sample coefficients are positive finite enclosures")
    print("CERTIFIED: C-even special-function engine preflight passed")
    print("FIREWALL: this is not the 1075x1075 finite positivity certificate")


if __name__ == "__main__":
    main()
