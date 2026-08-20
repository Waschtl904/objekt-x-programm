#!/usr/bin/env python3
"""Conservative typed regression helper for P11 R36-A14.2.

Rules used:
  1. one surviving term -> kill its chart image;
  2. exactly two surviving terms with the same image interval -> compute the
     induced affine transition;
  3. invariant involution with multiplier square != 1 -> kill that interval;
  4. re-evaluate complete cell constraints after every new kill.

The helper deliberately never forms pairwise edges from a cell with three or
more surviving terms.  It is a regression certificate, not a global
pseudogroup termination proof.
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


def print_case(R, S, T0):
    cells, killed, events = typed_closure(R, S, T0)
    print(f"case R={R:.12g}, S={S:.12g}, T0={T0:.12g}")
    print(f"  cells={len(cells)} q_domain={q_domain(R, S)}")
    for event in events:
        print(" ", event)
    print("  killed=", killed)


if __name__ == "__main__":
    cells, killed, _ = typed_closure(0.10, 0.50, 0.56)
    assert len(cells) == 8
    assert len(killed) == 1
    assert abs(killed[0][0] - 0.10) <= EPS
    assert abs(killed[0][1] - 0.50) <= EPS

    q = q_domain(0.10, 0.50)
    assert q is not None
    assert abs(q[0] - 0.10) <= EPS
    assert abs(q[1] - (D - 0.10)) <= EPS

    # R=0.15 is the A14.2d regression: q is absent, but the full annulus is
    # still killed.  The right remainder must be killed by a genuine weighted
    # involution, so this case is explicitly NOT a nilpotent-DAG certificate.
    cells15, killed15, events15 = typed_closure(0.15, 0.50, 0.56)
    assert len(cells15) == 8
    assert q_domain(0.15, 0.50) is None
    assert len(killed15) == 1
    assert abs(killed15[0][0] - 0.15) <= EPS
    assert abs(killed15[0][1] - 0.50) <= EPS

    h15 = (TAU2 + TAU3 - 0.50, 0.50)
    assert any(
        event[1] == "weighted involution kill"
        and abs(event[2][0] - h15[0]) <= EPS
        and abs(event[2][1] - h15[1]) <= EPS
        for event in events15
    )

    # Requested qualitative regression cases.
    print_case(0.10, 0.50, 0.56)
    print_case(0.05, 0.50, 0.56)
    print_case(0.15, 0.50, 0.56)
    print_case(0.02, 0.08, 0.56)

    print("PASS: A14.2b/A14.2d typed regressions and auxiliary cases")
