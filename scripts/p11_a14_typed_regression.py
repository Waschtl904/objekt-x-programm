#!/usr/bin/env python3
"""Conservative typed regression helper for P11 R36-A14.2.

Core closure rules:
  1. one surviving term -> kill its chart image;
  2. exactly two surviving terms with the same image interval -> compute the
     induced affine transition;
  3. invariant involution with multiplier square != 1 -> kill that interval;
  4. re-evaluate complete cell constraints after every new kill.

The core helper deliberately never forms pairwise edges from a cell with three
or more surviving terms.  It is a regression certificate, not a global
pseudogroup termination proof.

A14.2f adds one separate exact certificate for the right cell-order flank
S>2*tau2-R.  There two adjacent cells carry the two halves of the same p_2
reflection relation.  The certificate checks those cells and their domains
explicitly; it does not weaken the conservative core rules.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log, sqrt

EPS = 1.0e-11
TAU2 = 0.5 * log(2.0)
TAU3 = 0.5 * log(3.0)
D = TAU3 - TAU2
C2 = sqrt(log(2.0)) * 2.0 ** (-0.75)
C3 = sqrt(log(3.0)) * 3.0 ** (-0.75)


@dataclass(frozen=True)
class Term:
    shift: str
    kind: str
    coeff: float
    alpha: float
    beta: float
    image: tuple[float, float]


@dataclass(frozen=True)
class Cell:
    lo: float
    hi: float
    terms: tuple[Term, ...]


def merge(intervals):
    data = sorted((a, b) for a, b in intervals if b - a > EPS)
    out = []
    for lo, hi in data:
        if not out or lo > out[-1][1] + EPS:
            out.append([lo, hi])
        else:
            out[-1][1] = max(out[-1][1], hi)
    return [(lo, hi) for lo, hi in out]


def covered(interval, killed):
    lo, hi = interval
    cursor = lo
    for left, right in merge(killed):
        if right <= cursor + EPS:
            continue
        if left > cursor + EPS:
            return False
        cursor = max(cursor, right)
        if cursor >= hi - EPS:
            return True
    return cursor >= hi - EPS


def same_interval(a, b):
    return abs(a[0] - b[0]) <= EPS and abs(a[1] - b[1]) <= EPS


def close_interval(interval, target):
    return same_interval(interval, target)


def enumerate_cells(R, S, T0):
    if not (0.0 < R < S < T0):
        raise ValueError("Require 0 < R < S < T0")

    shifts = (("2", TAU2, C2), ("3", TAU3, C3))
    breakpoints = {0.0, T0}
    for _, tau, _ in shifts:
        for x in (
            tau - R,
            tau + R,
            tau - S,
            tau + S,
            tau,
            R - tau,
            S - tau,
        ):
            if 0.0 < x < T0:
                breakpoints.add(x)

    points = sorted(breakpoints)
    cells = []
    for lo, hi in zip(points, points[1:]):
        if hi - lo <= EPS:
            continue
        u = 0.5 * (lo + hi)
        terms = []
        for name, tau, weight in shifts:
            folded = abs(u - tau)
            if R < folded < S:
                if u < tau:
                    alpha, beta, sign = -1.0, tau, -1.0
                else:
                    alpha, beta, sign = 1.0, -tau, 1.0
                endpoints = (alpha * lo + beta, alpha * hi + beta)
                terms.append(
                    Term(
                        name,
                        "fold",
                        sign * weight,
                        alpha,
                        beta,
                        (min(endpoints), max(endpoints)),
                    )
                )

            forward = u + tau
            if R < forward < S:
                terms.append(
                    Term(name, "forward", -weight, 1.0, tau, (lo + tau, hi + tau))
                )
        cells.append(Cell(lo, hi, tuple(terms)))
    return cells


def induced_transition(first, second):
    # x1 = alpha1*u+beta1, x2 = alpha2*u+beta2
    # -> x2 = slope*x1+intercept
    slope = second.alpha / first.alpha
    intercept = second.beta - slope * first.beta
    multiplier = -first.coeff / second.coeff
    return slope, intercept, multiplier


def typed_closure(R, S, T0):
    cells = enumerate_cells(R, S, T0)
    killed = []
    events = []

    changed = True
    while changed:
        changed = False
        for index, cell in enumerate(cells, start=1):
            surviving = [term for term in cell.terms if not covered(term.image, killed)]

            if len(surviving) == 1:
                image = surviving[0].image
                before = merge(killed)
                killed = merge([*killed, image])
                if killed != before:
                    events.append((index, "one-term kill", image))
                    changed = True
                continue

            # Firewall: do not infer pairwise transitions from >=3 terms.
            if len(surviving) != 2:
                continue

            first, second = surviving
            if not same_interval(first.image, second.image):
                continue

            slope, intercept, multiplier = induced_transition(first, second)
            if abs(slope + 1.0) > EPS:
                continue
            if abs(multiplier * multiplier - 1.0) <= EPS:
                continue

            image = first.image
            before = merge(killed)
            killed = merge([*killed, image])
            if killed != before:
                events.append(
                    (
                        index,
                        "weighted involution kill",
                        image,
                        (slope, intercept),
                        multiplier,
                    )
                )
                changed = True

    return cells, merge(killed), events


def q_domain(R, S):
    lo = max(R, D - S)
    hi = min(S, D - R)
    return (lo, hi) if lo < hi else None


def middle_wedge_upper(R):
    return min(2.0 * D + R, 2.0 * TAU2 - R)


def unified_strip_lower(R):
    return max(0.5 * (TAU2 + TAU3), 2.0 * TAU2 - D - R)


def assert_full_core_kill(R, S, T0=0.56):
    cells, killed, events = typed_closure(R, S, T0)
    assert len(killed) == 1
    assert abs(killed[0][0] - R) <= EPS
    assert abs(killed[0][1] - S) <= EPS
    return cells, events


def find_cell(cells, lo, hi):
    for cell in cells:
        if abs(cell.lo - lo) <= EPS and abs(cell.hi - hi) <= EPS:
            return cell
    raise AssertionError(f"cell ({lo}, {hi}) not found")


def find_term(cell, shift, kind):
    matches = [term for term in cell.terms if term.shift == shift and term.kind == kind]
    assert len(matches) == 1, (cell, shift, kind, matches)
    return matches[0]


def assert_right_flank_assembled_p2(R, S, T0=0.56):
    """Exact A14.2f Case IV certificate for S>2*tau2-R.

    The conservative core closure intentionally stops because the two high
    images on the three-term cell differ.  This function checks the exact
    adjacent-cell decomposition whose relation domains union to the invariant
    p_2 interval H=(tau2+tau3-S,S).
    """

    assert D / 2.0 < R < D
    assert 0.5 * (TAU2 + TAU3) < S < TAU3
    assert S > 2.0 * TAU2 - R
    assert TAU3 < T0 < 2.0 * TAU2

    A = TAU2 + TAU3 - S
    B = 2.0 * TAU2 - R
    C = D + R
    assert R < D < A < S
    assert A < C
    assert B < S
    assert S - D < A

    cells = enumerate_cells(R, S, T0)

    # One-term block: (S-a,a) -> (d,A), (a,b-R) -> (R,d).
    left = find_cell(cells, S - TAU2, TAU2)
    assert len(left.terms) == 1
    left_b = find_term(left, "3", "fold")
    assert close_interval(left_b.image, (D, A))

    mid = find_cell(cells, TAU2, TAU3 - R)
    assert len(mid.terms) == 1
    mid_b = find_term(mid, "3", "fold")
    assert close_interval(mid_b.image, (R, D))

    # Three-term cell: low image is already in (R,A); the two high images
    # encode p_2 on z in (A,B).
    three = find_cell(cells, TAU3 - S, TAU2 - R)
    assert len(three.terms) == 3
    low = find_term(three, "2", "fold")
    fwd = find_term(three, "2", "forward")
    bfold = find_term(three, "3", "fold")
    assert close_interval(low.image, (R, S - D))
    assert close_interval(fwd.image, (A, B))
    assert close_interval(bfold.image, (C, S))
    assert low.image[1] < A + EPS

    # Adjacent two-term cell supplies the same p_2 relation on z in (B,S).
    two = find_cell(cells, TAU2 - R, S - TAU2)
    assert len(two.terms) == 2
    fwd2 = find_term(two, "2", "forward")
    bfold2 = find_term(two, "3", "fold")
    assert close_interval(fwd2.image, (B, S))
    assert close_interval(bfold2.image, (A, C))

    # Domain union and partner-image union are both exactly H=(A,S), up to
    # endpoints.  On both cells the relation is c2*h(z)+c3*h(p_2(z))=0.
    assert close_interval((fwd.image[0], fwd2.image[1]), (A, S))
    assert close_interval((bfold2.image[0], bfold.image[1]), (A, S))
    assert abs((C2 / C3) ** 2 - 1.0) > EPS

    return (A, S)


def assert_middle_wedge_case(R, T0=0.56):
    lower = 0.5 * (TAU2 + TAU3)
    upper = middle_wedge_upper(R)
    assert D / 2.0 < R < D
    assert lower < upper

    S = 0.5 * (lower + upper)
    assert TAU3 < T0 < 2.0 * TAU2
    assert lower < S < upper < T0
    assert q_domain(R, S) is None

    cells, events = assert_full_core_kill(R, S, T0)
    assert len(cells) == 8

    h = (TAU2 + TAU3 - S, S)
    assert any(
        event[1] == "weighted involution kill"
        and abs(event[2][0] - h[0]) <= EPS
        and abs(event[2][1] - h[1]) <= EPS
        for event in events
    )
    return S


def print_case(R, S, T0):
    cells, killed, events = typed_closure(R, S, T0)
    print(f"case R={R:.12g}, S={S:.12g}, T0={T0:.12g}")
    print(f"  cells={len(cells)} q_domain={q_domain(R, S)}")
    for event in events:
        print(" ", event)
    print("  killed=", killed)


if __name__ == "__main__":
    cells, _ = assert_full_core_kill(0.10, 0.50, 0.56)
    assert len(cells) == 8

    q = q_domain(0.10, 0.50)
    assert q is not None
    assert abs(q[0] - 0.10) <= EPS
    assert abs(q[1] - (D - 0.10)) <= EPS

    # R=0.15 is the A14.2d regression: q is absent, but the full annulus is
    # still killed.  The right remainder must be killed by a genuine weighted
    # involution, so this case is explicitly NOT a nilpotent-DAG certificate.
    cells15, events15 = assert_full_core_kill(0.15, 0.50, 0.56)
    assert len(cells15) == 8
    assert q_domain(0.15, 0.50) is None

    h15 = (TAU2 + TAU3 - 0.50, 0.50)
    assert any(
        event[1] == "weighted involution kill"
        and abs(event[2][0] - h15[0]) <= EPS
        and abs(event[2][1] - h15[1]) <= EPS
        for event in events15
    )

    # A14.2e sweep: points on both sides of R=a-d=2a-b.
    wedge_cases = (0.105, 0.12, 0.14, 0.15, 0.18, 0.20)
    wedge_s = [(R, assert_middle_wedge_case(R)) for R in wedge_cases]

    # A14.2f: small-R q anchor above the slanted lower bound.
    assert 0.50 > unified_strip_lower(0.01)
    assert_full_core_kill(0.01, 0.50, 0.56)

    # A14.2f: strict point beyond the old left A14.2e flank.
    assert 0.53 > 2.0 * D + 0.12
    assert 0.53 < TAU3
    assert_full_core_kill(0.12, 0.53, 0.56)

    # A14.2f: strict points beyond the old right A14.2e flank.  The core
    # helper is allowed to stop; the exact adjacent-cell certificate closes H.
    for S in (0.515, 0.54):
        assert S > 2.0 * TAU2 - 0.18
        assert_right_flank_assembled_p2(0.18, S, 0.56)

    # A second right-flank point close to R=d.
    assert_right_flank_assembled_p2(0.20, 0.54, 0.56)

    # Requested qualitative regression cases.
    print_case(0.10, 0.50, 0.56)
    print_case(0.05, 0.50, 0.56)
    print_case(0.15, 0.50, 0.56)
    print_case(0.02, 0.08, 0.56)
    print_case(0.12, 0.53, 0.56)
    print_case(0.18, 0.515, 0.56)
    for R, S in wedge_s:
        print_case(R, S, 0.56)

    print("PASS: A14.2b/A14.2d/A14.2e/A14.2f typed regressions and flank certificates")
