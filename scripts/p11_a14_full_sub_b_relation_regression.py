#!/usr/bin/env python3
"""Independent regression certificate for P11 R36-A14.2h.

Checks the full sub-b source-chart relation directly against the original
folded operator at u=b-y.  It does not call the A14 typed cell-closure helper.

The analytic theorem is in the audit note; this script certifies branch signs,
arguments, indicator domains, and the two geometric proof regimes on a fixed
set of regression anchors plus a deterministic parameter grid.
"""

from __future__ import annotations

from math import log, sqrt

EPS = 1.0e-11
A = 0.5 * log(2.0)
B = 0.5 * log(3.0)
D = B - A
C = A + B
ELL = 0.5 * C
C2 = sqrt(log(2.0)) * 2.0 ** (-0.75)
C3 = sqrt(log(3.0)) * 3.0 ** (-0.75)


def close(x, y):
    return abs(x - y) <= EPS


def active_original_terms(y, R, S, T0):
    """Active Lh terms at the actual source point u=B-y."""

    u = B - y
    assert 0.0 < u < T0

    terms = []
    for shift, tau, weight in (("2", A, C2), ("3", B, C3)):
        folded = abs(u - tau)
        if R < folded < S:
            sign = -1.0 if u < tau else 1.0
            terms.append((shift, "fold", sign * weight, folded))

        forward = u + tau
        if R < forward < S:
            terms.append((shift, "forward", -weight, forward))

    return terms


def expected_full_sub_b_terms(y, R, S):
    """Expected Lh coefficients before multiplying the equation by -1."""

    terms = [("3", "fold", -C3, y)]

    folded = abs(y - D)
    if R < folded < S:
        # u-a=D-y, so the original a-fold sign is sign(D-y).
        coeff = C2 if y < D else -C2
        terms.append(("2", "fold", coeff, folded))

    reflected = C - y
    if R < reflected < S:
        terms.append(("2", "forward", -C2, reflected))

    return terms


def same_terms(actual, expected):
    def key(term):
        return term[0], term[1], term[3]

    actual = sorted(actual, key=key)
    expected = sorted(expected, key=key)
    assert len(actual) == len(expected), (actual, expected)

    for left, right in zip(actual, expected):
        assert left[0] == right[0]
        assert left[1] == right[1]
        assert close(left[2], right[2])
        assert close(left[3], right[3])


def relation_partition(R, S):
    """All y-breakpoints at which a sign or indicator may change."""

    points = {R, S}
    candidates = (
        D,
        D - S,
        D - R,
        D + R,
        D + S,
        C - S,
        C - R,
        ELL,
    )
    for x in candidates:
        if R < x < S:
            points.add(x)
    return sorted(points)


def assert_relation_survives(R, S, T0=0.56):
    assert 0.0 < R < S < B
    assert B < T0 < 2.0 * A

    # The source chart parametrizes the entire annulus when S<b.
    assert B - S > 0.0
    assert B - R < T0

    points = relation_partition(R, S)
    for lo, hi in zip(points, points[1:]):
        if hi - lo <= EPS:
            continue
        y = 0.5 * (lo + hi)
        same_terms(
            active_original_terms(y, R, S, T0),
            expected_full_sub_b_terms(y, R, S),
        )


def assert_low_r_geometry(R, S):
    """Check the exact inequalities used in the new R<d proof."""

    assert 0.0 < R < D
    assert R < S < B

    if S <= ELL + EPS:
        # Reflection p(y)=C-y is invisible on the whole annulus.
        assert C - S >= S - EPS
        return "folded descent only"

    boundary = C - S
    assert R < D < A < boundary < S

    # The lower interval is closed under the folded predecessor whenever the
    # predecessor is active.
    test_points = (
        R + 0.25 * (boundary - R),
        R + 0.75 * (boundary - R),
    )
    for y in test_points:
        folded = abs(y - D)
        if R < folded < S:
            assert folded < boundary + EPS

    # Every predecessor from the upper reflection block is already below it.
    assert S - D < boundary
    assert close(C - boundary, S)
    assert close(C - S, boundary)
    return "folded descent + weighted reflection"


def run_case(R, S, T0=0.56):
    assert_relation_survives(R, S, T0)
    if R < D:
        regime = assert_low_r_geometry(R, S)
    else:
        regime = "A14.2g super-d specialization"
    print(f"PASS R={R:.12g} S={S:.12g}: {regime}")


if __name__ == "__main__":
    # Formerly difficult small-R cases.
    anchors = (
        (0.02, 0.08),
        (0.02, 0.25),
        (0.05, 0.40),
        (0.10, 0.44),
        (0.02, 0.46),
        (0.10, 0.50),
        (0.19, 0.54),
        # Phase boundary and super-d checks retained as subsumed cases.
        (D, 0.30),
        (D, 0.50),
        (0.25, 0.50),
        (0.40, 0.50),
        (0.53, 0.54),
    )
    for R, S in anchors:
        run_case(R, S)

    # Deterministic grid across the complete 0<R<S<b parameter triangle.
    for i in range(1, 25):
        R = B * i / 30.0
        for j in range(i + 1, 30):
            S = B * j / 30.0
            if not (R < S < B):
                continue
            assert_relation_survives(R, S)
            if R < D:
                assert_low_r_geometry(R, S)

    assert A > D
    assert abs((C2 / C3) ** 2 - 1.0) > EPS
    assert abs((C3 / C2) ** 2 - 1.0) > EPS

    print("PASS: A14.2h full sub-b relation and geometry regression")
