#!/usr/bin/env python3
"""Independent regression certificate for P11 R36-A14.2i.

This script checks three ingredients directly against the original two-shift
operator:

1. the symmetric b-chart relation across S=b;
2. the high-R (R>=a) source-chart geometry;
3. the explicit four-chart infinite-dimensional kernel construction for
   R<a<b<S.

It does not call the earlier typed-cell closure helper.  The theorem is
analytic; these checks are regression anchors and domain/sign firewalls.
"""

from __future__ import annotations

from math import log, sqrt

EPS = 1.0e-10
A = 0.5 * log(2.0)
B = 0.5 * log(3.0)
D = B - A
C = A + B
ELL = 0.5 * C
M = A - 0.5 * D
E = 2.0 * A - B  # A-D
C2 = sqrt(log(2.0)) * 2.0 ** (-0.75)
C3 = sqrt(log(3.0)) * 3.0 ** (-0.75)
RHO = C3 / C2


def close(x, y, tol=EPS):
    return abs(x - y) <= tol


def active_original_terms(u, R, S, T0):
    """Return active original L-terms as (coefficient, argument, label)."""
    assert 0.0 < u < T0
    out = []
    for label, tau, weight in (("2", A, C2), ("3", B, C3)):
        folded = abs(u - tau)
        if R < folded < S:
            sign = -1.0 if u < tau else 1.0
            out.append((sign * weight, folded, f"{label}-fold"))

        forward = u + tau
        if R < forward < S:
            out.append((-weight, forward, f"{label}-forward"))
    return out


def combine_terms(terms):
    """Combine terms with equal arguments, ignoring branch labels."""
    data = []
    for coeff, arg, _ in terms:
        found = False
        for item in data:
            if close(item[1], arg):
                item[0] += coeff
                found = True
                break
        if not found:
            data.append([coeff, arg])
    data = [item for item in data if abs(item[0]) > EPS]
    data.sort(key=lambda item: item[1])
    return data


def same_combined_terms(left, right):
    left = combine_terms(left)
    right = combine_terms(right)
    assert len(left) == len(right), (left, right)
    for (cl, xl), (cr, xr) in zip(left, right):
        assert close(cl, cr), (left, right)
        assert close(xl, xr), (left, right)


def symmetric_expected_raw(y, R, S):
    """Raw L-terms corresponding to minus the displayed A14.2i relation."""
    out = [(-C3, y, "self")]

    rb = 2.0 * B - y
    if R < rb < S:
        out.append((-C3, rb, "rb"))

    folded = abs(y - D)
    if R < folded < S:
        sign = 1.0 if y > D else -1.0
        out.append((-C2 * sign, folded, "tent"))

    p = C - y
    if R < p < S:
        out.append((-C2, p, "p"))

    return out


def symmetric_breakpoints(R, S):
    points = {R, S}
    for x in (
        B,
        D,
        2.0 * B - R,
        2.0 * B - S,
        D - R,
        D + R,
        D - S,
        D + S,
        C - R,
        C - S,
    ):
        if R < x < S:
            points.add(x)
    return sorted(points)


def assert_symmetric_relation(R, S, T0):
    assert 0.0 < R < S < T0
    assert B < T0 < 2.0 * A

    for lo, hi in zip(symmetric_breakpoints(R, S), symmetric_breakpoints(R, S)[1:]):
        if hi - lo <= EPS:
            continue
        for theta in (0.25, 0.5, 0.75):
            y = lo + theta * (hi - lo)
            u = abs(B - y)
            assert u > 0.0
            same_combined_terms(
                active_original_terms(u, R, S, T0),
                symmetric_expected_raw(y, R, S),
            )


def high_expected_raw(y, R, S):
    """Raw L-terms on u=y-a after the a-fold has dropped below R."""
    out = [(-C2, y, "self")]
    p = C - y
    if R < p < S:
        out.append((-C3, p, "p"))
    succ = y + D
    if R < succ < S:
        out.append((-C3, succ, "up"))
    return out


def assert_high_R_geometry(R, S, T0):
    assert A <= R < S < T0
    assert B <= S
    assert B < T0 < 2.0 * A

    points = {R, S}
    for x in (C - R, C - S, S - D, R - D, ELL):
        if R < x < S:
            points.add(x)
    points = sorted(points)

    for lo, hi in zip(points, points[1:]):
        if hi - lo <= EPS:
            continue
        y = 0.5 * (lo + hi)
        u = y - A
        same_combined_terms(
            active_original_terms(u, R, S, T0),
            high_expected_raw(y, R, S),
        )

    if R >= ELL - EPS:
        assert C - R <= R + EPS
    else:
        P = C - R
        assert R < P + EPS
        assert P <= B + EPS
        assert B <= S + EPS
        assert R + D >= P - EPS


def interval_contains(interval, x):
    return interval[0] < x < interval[1]


def kernel_lambda(R, S, T0):
    lam = max(R, T0 - A, C - S, M)
    assert lam < A - EPS, (R, S, T0, lam, A)
    return lam


def kernel_intervals(R, S, T0):
    lam = kernel_lambda(R, S, T0)
    J0 = (lam, A)
    J1 = (A, 2.0 * A - lam)
    J2 = (lam + D, B)
    J3 = (B, C - lam)
    return lam, (J0, J1, J2, J3)


def assert_kernel_interval_geometry(R, S, T0):
    assert 0.0 < R < A < B < S < T0 < 2.0 * A
    lam, (J0, J1, J2, J3) = kernel_intervals(R, S, T0)

    for lo, hi in (J0, J1, J2, J3):
        assert R <= lo + EPS
        assert hi <= S + EPS
        assert hi > lo + EPS

    assert J0[1] <= J1[0] + EPS
    assert J1[1] <= J2[0] + EPS
    assert J2[1] <= J3[0] + EPS

    U0 = (0.0, A - lam)
    U2 = (lam - E, D)
    U1 = (D, B - lam)
    assert U0[1] <= U2[0] + EPS
    assert U2[1] <= U1[0] + EPS
    assert U1[1] < T0

    # The dangerous upper a-fold source of J0 lies beyond T0.
    assert A + lam >= T0 - EPS

    return lam, (J0, J1, J2, J3), (U0, U2, U1)


def f_base(x):
    return 1.0 + 0.37 * x


def h_kernel(y, R, S, T0):
    lam, (J0, J1, J2, J3) = kernel_intervals(R, S, T0)

    if interval_contains(J0, y):
        return f_base(y)
    if interval_contains(J1, y):
        x = 2.0 * A - y
        return -f_base(x)
    if interval_contains(J2, y):
        x = y - D
        return RHO * f_base(x)
    if interval_contains(J3, y):
        x = C - y
        return -RHO * f_base(x)
    return 0.0


def L_of_constructed_h(u, R, S, T0):
    value = 0.0
    for coeff, arg, _ in active_original_terms(u, R, S, T0):
        value += coeff * h_kernel(arg, R, S, T0)
    return value


def inverse_sources_of_value(y, T0):
    """All u in (0,T0) where an original branch can evaluate h(y)."""
    values = []
    for tau in (A, B):
        for u in (tau - y, tau + y, y - tau):
            if 0.0 < u < T0 and not any(close(u, v) for v in values):
                values.append(u)
    values.sort()
    return values


def assert_kernel_construction(R, S, T0):
    lam, _, _ = assert_kernel_interval_geometry(R, S, T0)

    for theta in (0.15, 0.35, 0.55, 0.75, 0.9):
        x = lam + theta * (A - lam)
        support_values = (x, 2.0 * A - x, x + D, C - x)

        # Aggregate every original source that can see any of the four values.
        actual_sources = []
        for y in support_values:
            for u in inverse_sources_of_value(y, T0):
                if not any(close(u, v) for v in actual_sources):
                    actual_sources.append(u)
        actual_sources.sort()

        expected_sources = sorted((A - x, x - E, B - x))
        assert len(actual_sources) == 3, (R, S, T0, x, actual_sources)
        for u, v in zip(actual_sources, expected_sources):
            assert close(u, v), (actual_sources, expected_sources)

        for u in expected_sources:
            assert abs(L_of_constructed_h(u, R, S, T0)) <= 5.0e-10

    # Check every source cell induced by the support endpoints as an extra
    # numerical firewall.  The analytic proof is the source-family argument.
    source_points = {0.0, T0}
    endpoints = [lam, A, 2.0 * A - lam, lam + D, B, C - lam]
    for y in endpoints:
        for u in inverse_sources_of_value(y, T0):
            source_points.add(u)
    source_points = sorted(source_points)

    for lo, hi in zip(source_points, source_points[1:]):
        if hi - lo <= EPS:
            continue
        for theta in (0.2, 0.5, 0.8):
            u = lo + theta * (hi - lo)
            assert abs(L_of_constructed_h(u, R, S, T0)) <= 5.0e-9, (
                R,
                S,
                T0,
                u,
                L_of_constructed_h(u, R, S, T0),
            )


if __name__ == "__main__":
    # Symmetric relation: below, at, and above S=b.
    relation_cases = (
        (0.05, 0.40, 0.56),
        (0.10, 0.50, 0.56),
        (0.10, B, 0.60),
        (0.10, 0.60, 0.68),
        (0.30, 0.65, 0.68),
        (A, 0.65, 0.68),
        (0.50, 0.65, 0.68),
    )
    for case in relation_cases:
        assert_symmetric_relation(*case)

    # Deterministic triangle sweep for the relation.
    for T0 in (0.57, 0.62, 0.68):
        if not (B < T0 < 2.0 * A):
            continue
        for i in range(1, 7):
            S = 0.04 + i * (T0 - 0.05) / 7.0
            if not (0.02 < S < T0):
                continue
            for j in range(1, 5):
                R = 0.01 + j * (S - 0.02) / 5.0
                if 0.0 < R < S:
                    assert_symmetric_relation(R, S, T0)

    # High-R zero side, including the sharp R=a boundary.
    high_cases = (
        (A, B, 0.60),
        (A, 0.60, 0.68),
        (A + 0.01, 0.65, 0.68),
        (0.40, 0.60, 0.68),
        (0.46, 0.65, 0.68),
        (0.55, 0.65, 0.68),
    )
    for case in high_cases:
        assert_high_R_geometry(*case)

    # Infinite-kernel side, including points close to all three open borders.
    kernel_cases = (
        (0.10, 0.56, 0.57),
        (0.10, 0.60, 0.68),
        (0.30, 0.65, 0.68),
        (A - 0.006, 0.56, 0.60),
        (0.01, 0.68, 0.69),
    )
    for case in kernel_cases:
        assert_kernel_construction(*case)

    # Small deterministic sweep through R<a<b<S<T0<2a.
    for T0 in (0.57, 0.62, 0.68):
        for frac_s in (0.25, 0.55, 0.85):
            S = B + frac_s * (T0 - B)
            for frac_r in (0.05, 0.45, 0.90):
                R = frac_r * A
                assert_kernel_construction(R, S, T0)

    assert abs(RHO * RHO - 1.0) > 1.0e-6
    print("PASS: A14.2i complete first two-shift classification regressions")
