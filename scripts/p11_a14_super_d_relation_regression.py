#!/usr/bin/env python3
"""Independent regression certificate for P11 R36-A14.2g.

This script checks the super-d relation directly against the original folded
operator branches on the source chart u=b-y.  It does not call the conservative
A14.2 cell-closure helper and does not infer pairwise edges from multi-term
cells.

The theorem itself is analytic; the numerical cases below are regression
anchors spanning every proof regime, not a substitute for the proof.
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
    """Return active terms of Lh(u) at u=B-y from the original definition.

    Each term is represented as (shift, kind, coefficient, argument).
    """

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


def expected_super_d_terms(y, R, S):
    """Expected terms from A14.2g.3, written with Lh coefficients."""

    terms = [("3", "fold", -C3, y)]

    predecessor = y - D
    if R < predecessor < S:
        terms.append(("2", "fold", -C2, predecessor))

    reflected = C - y
    if R < reflected < S:
        terms.append(("2", "forward", -C2, reflected))

    return terms


def same_terms(actual, expected):
    def key(term):
        return term[0], term[1], round(term[3], 12)

    actual = sorted(actual, key=key)
    expected = sorted(expected, key=key)
    assert len(actual) == len(expected), (actual, expected)

    for left, right in zip(actual, expected):
        assert left[0] == right[0]
        assert left[1] == right[1]
        assert close(left[2], right[2])
        assert close(left[3], right[3])


def relation_partition(R, S):
    """Partition y-space at every indicator change relevant to A14.2g.3."""

    points = {R, S}
    for x in (R + D, S + D, C - R, C - S, ELL):
        if R < x < S:
            points.add(x)
    return sorted(points)


def assert_relation_survives(R, S, T0=0.56):
    assert D - EPS <= R < S < B
    assert B < T0 < 2.0 * A

    # The complete b-fold source chart is on the u<=a side once R>=d.
    assert B - S > 0.0
    assert B - R <= A + EPS

    points = relation_partition(R, S)
    for lo, hi in zip(points, points[1:]):
        if hi - lo <= EPS:
            continue
        y = 0.5 * (lo + hi)
        same_terms(
            active_original_terms(y, R, S, T0),
            expected_super_d_terms(y, R, S),
        )


def assert_proof_regime(R, S):
    """Check the interval inequalities used by the analytic A14.2g proof."""

    assert D - EPS <= R < S < B

    if S <= ELL + EPS:
        # Case I: p(y)=C-y is outside on the upper side.
        assert C - S >= S - EPS
        return "I: triangular below center"

    if R >= ELL - EPS:
        # Case II: p(y)=C-y is outside on the lower side.
        assert C - R <= R + EPS
        return "II: triangular above center"

    lower_reflection_edge = C - S
    upper_reflection_edge = C - R

    if R <= lower_reflection_edge + EPS:
        # Case IIIa: kill the lower tail first, then the invariant H=(A,S).
        assert lower_reflection_edge > A  # because S<B
        assert S - D < A + EPS
        assert C - lower_reflection_edge == S
        return "IIIa: lower tail + weighted reflection"

    # Case IIIb: R>A implies R>a, hence the whole annulus has width <d.
    assert lower_reflection_edge > A
    assert R > A
    assert S - R < D + EPS
    assert R < upper_reflection_edge < S
    return "IIIb: weighted reflection + upper tail"


def run_case(R, S, T0=0.56):
    assert_relation_survives(R, S, T0)
    regime = assert_proof_regime(R, S)
    print(f"PASS R={R:.12g} S={S:.12g}: {regime}")


if __name__ == "__main__":
    # Exact phase boundary R=d, both below and across the reflection center.
    run_case(D, 0.30)
    run_case(D, 0.46)
    run_case(D, 0.50)

    # R>d: triangular-below-center and cross-center with R<=C-S.
    run_case(0.25, 0.40)
    run_case(0.25, 0.50)

    # Cross-center with R>C-S: invariant reflection first, then upper tail.
    run_case(0.40, 0.50)

    # Above the reflection center: pure triangular recurrence again.
    run_case(0.46, 0.52)
    run_case(0.53, 0.54)

    assert abs((C3 / C2) ** 2 - 1.0) > EPS
    print("PASS: A14.2g super-d relation survival across all proof regimes")
