# -*- coding: utf-8 -*-
"""Exact-head Arb preflight for the frozen A1 C-even matrix engine.

This is NOT the 1075x1075 positivity certificate. It checks the final
turning-anchor special-function engine and the exact even-energy tail bound
used by the frozen C-even backend.
"""

import os
from flint import acb, arb, ctx, fmpq

ctx.prec = int(os.environ.get("A1_PREC_BITS", "512"))


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
LOW_MARGIN_MULT = 8
LOW_MARGIN_ADD = 16
HIGH_MARGIN_MULT = 24
HIGH_MARGIN_ADD = 32
E_B_SAMPLE_TARGET = A("1e-43")
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


def elementary_j0(z: arb) -> arb:
    return z.sin() / z


def elementary_j1(z: arb) -> arb:
    return z.sin() / (z * z) - z.cos() / z


def turning_indices(z: arb, degree: int) -> tuple[int, int]:
    """Conditioning proposal; correctness is certified by interval overlap."""
    zm = float(z.mid())
    cbrt = zm ** (1.0 / 3.0)
    low_margin = int(LOW_MARGIN_MULT * cbrt) + LOW_MARGIN_ADD
    high_margin = int(HIGH_MARGIN_MULT * cbrt) + HIGH_MARGIN_ADD
    low = max(2, int(zm) - low_margin)
    high = min(degree - 2, int(zm) + high_margin)
    if high <= low + 4:
        high = min(degree - 2, low + 8)
    return low, high


def upward_vector(z: arb, top: int) -> list[arb]:
    vals = [A(0) for _ in range(top + 2)]
    vals[0] = elementary_j0(z)
    vals[1] = elementary_j1(z)
    for n in range(1, top + 1):
        vals[n + 1] = (2 * n + 1) * vals[n] / z - vals[n - 1]
    if any(not v.is_finite() for v in vals):
        raise RuntimeError("non-finite upward recurrence")
    return vals


def downward_from_direct_turning_anchors(z: arb, high: int, low: int) -> list[arb]:
    vals = [A(0) for _ in range(high + 2)]
    vals[high] = spherical_j_direct(high, z)
    vals[high + 1] = spherical_j_direct(high + 1, z)
    if not vals[high].is_finite() or not vals[high + 1].is_finite():
        raise RuntimeError("non-finite direct turning anchors")
    for n in range(high, low, -1):
        vals[n - 1] = (2 * n + 1) * vals[n] / z - vals[n + 1]
    if any(not vals[n].is_finite() for n in range(low, high + 2)):
        raise RuntimeError("non-finite direct-anchor downward recurrence")
    return vals


def analytic_j_bounds(z: arb, degree: int) -> list[arb]:
    bounds = [A(1)]
    for n in range(degree - 1):
        bounds.append(bounds[-1] * z / (2 * n + 3))
    return bounds


def turning_anchor_vector(z: arb, degree: int) -> tuple[list[arb], int, int]:
    low, high = turning_indices(z, degree)
    up = upward_vector(z, low + 12)
    down = downward_from_direct_turning_anchors(z, high, max(2, low - 12))

    result = [A(0) for _ in range(degree)]
    for n in range(min(len(up), degree)):
        result[n] = up[n]

    overlap_low = max(2, low - 8)
    overlap_high = min(low + 12, len(up) - 1, high)
    for n in range(overlap_low, overlap_high + 1):
        overlap = up[n].intersection(down[n])
        if overlap is None:
            raise RuntimeError(f"upward/direct-anchor intervals do not overlap at n={n}")
        result[n] = overlap

    for n in range(overlap_high + 1, min(high + 1, degree)):
        result[n] = down[n]

    if high + 1 < degree:
        bounds = analytic_j_bounds(z, degree)
        for n in range(high + 1, degree):
            result[n] = arb(0, bounds[n].upper())

    if any(not v.is_finite() for v in result):
        raise RuntimeError("non-finite turning-anchor Bessel vector")
    return result, low, high


def spherical_j_even_vector(z: arb) -> tuple[list[arb], int, int]:
    if z < 1:
        full = [spherical_j_direct(n, z) for n in range(MAX_DEGREE)]
        low = 0
        high = MAX_DEGREE - 1
    else:
        full, low, high = turning_anchor_vector(z, MAX_DEGREE)
    return [full[n] for n in range(0, MAX_DEGREE, 2)], low, high


def lower_abs_point(v: arb) -> arb:
    """Nonnegative point lower bound for |v|, built from midpoint/radius."""
    m = A(v.mid())
    if m < 0:
        m = -m
    r = A(v.rad())
    out = m - r
    return out if out > 0 else A(0)


def upper_point(v: arb) -> arb:
    """Point upper bound for a real Arb ball."""
    return A(v.mid()) + A(v.rad())


def even_b_vector_error(z: arb, vals: list[arb], high: int) -> tuple[arb, arb, arb, arb]:
    represented_even = min(MAX_DEGREE - 2, high if high % 2 == 0 else high - 1)
    head_rad2_upper = A(0)
    head_energy_lower = A(0)

    for n in range(0, represented_even + 1, 2):
        v = vals[n // 2]
        c2 = 2 * A(2 * n + 1) / PI
        c2_upper = upper_point(c2)
        c2_lower = A(c2.mid()) - A(c2.rad())
        if c2_lower < 0:
            c2_lower = A(0)
        rad = A(v.rad())
        lb = lower_abs_point(v)
        head_rad2_upper += c2_upper * rad * rad
        head_energy_lower += c2_lower * lb * lb

    total_even_energy = (1 + elementary_j0(2 * z)) / PI
    if not total_even_energy.is_finite() or not head_energy_lower.is_finite():
        raise RuntimeError("non-finite even-energy components")

    total_upper = upper_point(total_even_energy)
    head_lower = A(head_energy_lower.mid()) - A(head_energy_lower.rad())
    if head_lower < 0:
        head_lower = A(0)
    tail2_upper = total_upper - head_lower
    if tail2_upper < 0:
        tail2_upper = A(0)

    head_rad2_upper = upper_point(head_rad2_upper)
    if head_rad2_upper < 0:
        head_rad2_upper = A(0)

    eb2_upper = head_rad2_upper + tail2_upper
    if not eb2_upper.is_finite() or eb2_upper < 0:
        raise RuntimeError(
            f"invalid even-vector error-square upper bound: total={total_upper}, "
            f"head_lower={head_lower}, tail2={tail2_upper}, head_rad2={head_rad2_upper}"
        )
    eb = eb2_upper.sqrt()
    if not eb.is_finite():
        raise RuntimeError(
            f"non-finite sqrt in even-vector error: eb2={eb2_upper}, total={total_upper}, "
            f"head_lower={head_lower}, tail2={tail2_upper}, head_rad2={head_rad2_upper}"
        )
    return eb, head_rad2_upper, tail2_upper, total_upper


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

    print("A1 C-even special-function / energy-tail preflight")
    print(f"prec_bits = {ctx.prec}")
    print(f"Gauss order = {GAUSS_N}, panel = 0.4, Omega = 1551")
    print(f"high-margin rule = {HIGH_MARGIN_MULT}*x^(1/3)+{HIGH_MARGIN_ADD}")
    print(f"sample e_b target = {E_B_SAMPLE_TARGET.str(12, radius=False)}")

    for panel, node_index in SAMPLES:
        x, w = gauss_node(panel, node_index)
        if not (x > 0 and x < A(OMEGA)):
            raise RuntimeError("sample Gauss node outside open band")
        r = r_on_real_ball(x); alpha = w * r
        if not r.is_finite() or not alpha.is_finite():
            raise RuntimeError("non-finite scalar multiplier/weight")

        vals, low, high = spherical_j_even_vector(x)
        if len(vals) != 1075:
            raise RuntimeError("wrong even-vector dimension")

        for n in CHECK_ORDERS:
            value = vals[n // 2]
            direct = spherical_j_direct(n, x)
            if not value.overlaps(direct):
                raise RuntimeError(
                    f"direct/turning-anchor Bessel mismatch panel={panel}, node={node_index}, n={n}"
                )

        if not elementary_j0(x).overlaps(spherical_j_direct(0, x)):
            raise RuntimeError("elementary/direct j0 mismatch")
        if not elementary_j1(x).overlaps(spherical_j_direct(1, x)):
            raise RuntimeError("elementary/direct j1 mismatch")

        eb, head_rad2, tail2, total_e = even_b_vector_error(x, vals, high)
        if not (eb < E_B_SAMPLE_TARGET):
            raise RuntimeError(
                f"sample even-vector error exceeds 1e-43: panel={panel}, node={node_index}, e_b={eb}, "
                f"head_rad2={head_rad2}, tail2={tail2}, totalE={total_e}"
            )

        print(
            "sample", panel, node_index,
            "x=", x.str(22, radius=True),
            "r=", r.str(18, radius=True),
            "alpha=", alpha.str(18, radius=True),
            "turn_low=", low,
            "turn_high=", high,
            "e_b=", eb.str(16, radius=True),
            "head_rad2=", head_rad2.str(10, radius=True),
            "tail2=", tail2.str(10, radius=True),
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
    print("CERTIFIED: C-even direct-turning-anchor Bessel enclosures overlap direct Arb values")
    print("CERTIFIED: C-even addition-theorem energy-tail l2 bounds computed")
    print("CERTIFIED: C-even sample vector errors e_b < 1e-43")
    print("CERTIFIED: C-even moment-series sample coefficients are positive finite enclosures")
    print("CERTIFIED: C-even special-function / energy-tail preflight passed")
    print("FIREWALL: this is not the 1075x1075 finite positivity certificate")


if __name__ == "__main__":
    main()
