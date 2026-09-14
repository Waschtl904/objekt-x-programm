# -*- coding: utf-8 -*-
"""Sharded rigorous node-evaluation certificate for frozen A1 C-odd.

Each shard checks a disjoint round-robin subset of the 3878 Gauss panels.
At every node it proves the odd Legendre-Fourier midpoint proposal has l2
error < 1e-43.  The proof uses the same rigorous direct-turning-anchor Bessel
engine as C-even and the exact odd spherical-Bessel energy identity

    sum_{n odd} 2(2n+1)/pi * j_n(x)^2 = (1-j_0(2x))/pi.

It also accumulates the scalar-alpha part of the rank-one perturbation bound.
All 32 shards together imply scalar-alpha contribution < 1e-39.
"""

import os
from flint import arb, ctx

ctx.prec = 3072
os.environ["A1_PREC_BITS"] = "3072"

from check_a1_c_even_engine_preflight_arb import (  # noqa: E402
    A, GAUSS_N, MAX_DEGREE, OMEGA, PI,
    downward_from_direct_turning_anchors, elementary_j0, gauss_node,
    lower_abs_point, r_on_real_ball, turning_indices, upper_point,
    upward_vector,
)

PANEL_COUNT = 3878
SHARD_COUNT = int(os.environ.get("A1_SHARD_COUNT", "32"))
SHARD_INDEX = int(os.environ["A1_SHARD_INDEX"])
E_B_TARGET = A("1e-43")
SCALAR_TOTAL_TARGET = A("1e-39")
SCALAR_SHARD_TARGET = SCALAR_TOTAL_TARGET / SHARD_COUNT
BMAX = (2 / PI).sqrt()  # uniform upper bound for either parity vector
B0_BOUND = BMAX + E_B_TARGET
SCALAR_FACTOR = (B0_BOUND + E_B_TARGET) ** 2

if SHARD_COUNT != 32:
    raise RuntimeError("frozen C-odd shard count is 32")
if not (0 <= SHARD_INDEX < SHARD_COUNT):
    raise RuntimeError("invalid shard index")


def sharp_odd_head(z: arb):
    """Return rigorous sharp odd j_n intervals through the direct high anchor."""
    low, high = turning_indices(z, MAX_DEGREE)
    up = upward_vector(z, low + 12)
    down = downward_from_direct_turning_anchors(z, high, max(2, low - 12))
    overlap_low = max(2, low - 8)
    overlap_high = min(low + 12, len(up) - 1, high)

    out = []
    for n in range(1, high + 1, 2):
        if n < overlap_low:
            v = up[n]
        elif n <= overlap_high:
            v = up[n].intersection(down[n])
            if v is None:
                raise RuntimeError(f"up/down overlap failed at n={n}")
        else:
            v = down[n]
        if not v.is_finite():
            raise RuntimeError(f"non-finite sharp odd Bessel interval at n={n}")
        out.append((n, v))
    return out, low, high


def vector_error_bound(z: arb, head) -> arb:
    """l2 error of exact-scaled midpoint odd head plus zero unresolved tail."""
    head_rad2_upper = A(0)
    head_energy_lower = A(0)

    for n, v in head:
        c2 = 2 * A(2 * n + 1) / PI
        c2_upper = upper_point(c2)
        c2_lower = A(c2.mid()) - A(c2.rad())
        if c2_lower < 0:
            c2_lower = A(0)
        rad = A(v.rad())
        lb = lower_abs_point(v)
        head_rad2_upper += c2_upper * rad * rad
        head_energy_lower += c2_lower * lb * lb

    # Addition theorem split by parity.
    total_odd_energy = (1 - elementary_j0(2 * z)) / PI
    if not total_odd_energy.is_finite() or not head_energy_lower.is_finite():
        raise RuntimeError("non-finite shard odd-energy components")

    total_upper = upper_point(total_odd_energy)
    head_lower = A(head_energy_lower.mid()) - A(head_energy_lower.rad())
    if head_lower < 0:
        head_lower = A(0)
    tail_upper = total_upper - head_lower
    if tail_upper < 0:
        tail_upper = A(0)

    head_rad2_upper = upper_point(head_rad2_upper)
    if head_rad2_upper < 0:
        head_rad2_upper = A(0)

    eb2 = tail_upper + head_rad2_upper
    if not eb2.is_finite() or eb2 < 0:
        raise RuntimeError(
            f"invalid odd node vector error square: total={total_upper}, head={head_lower}, "
            f"tail={tail_upper}, head_rad2={head_rad2_upper}"
        )
    eb = eb2.sqrt()
    if not eb.is_finite():
        raise RuntimeError(f"non-finite odd node vector error sqrt: eb2={eb2}")
    return eb


def main() -> None:
    scalar_sum = A(0)
    max_eb = A(0)
    max_eb_panel = -1
    max_eb_node = -1
    node_count = 0
    panel_count = 0

    for panel in range(SHARD_INDEX, PANEL_COUNT, SHARD_COUNT):
        panel_count += 1
        for node_index in range(GAUSS_N):
            x, w = gauss_node(panel, node_index)
            if not (x > 0 and x < A(OMEGA)):
                raise RuntimeError("Gauss node outside open frozen band")

            alpha = w * r_on_real_ball(x)
            if not alpha.is_finite():
                raise RuntimeError("non-finite alpha interval")

            head, _, _ = sharp_odd_head(x)
            eb = vector_error_bound(x, head)
            if not (eb < E_B_TARGET):
                raise RuntimeError(
                    f"odd node e_b target failed: shard={SHARD_INDEX}, panel={panel}, "
                    f"node={node_index}, e_b={eb}"
                )
            if eb > max_eb:
                max_eb = eb
                max_eb_panel = panel
                max_eb_node = node_index

            scalar_sum += A(alpha.rad()) * SCALAR_FACTOR
            node_count += 1

    if not (scalar_sum < SCALAR_SHARD_TARGET):
        raise RuntimeError(
            f"scalar-alpha shard budget failed: shard={SHARD_INDEX}, "
            f"sum={scalar_sum}, target={SCALAR_SHARD_TARGET}"
        )

    print("A1 C-odd evaluation shard certificate")
    print(f"prec_bits              = {ctx.prec}")
    print(f"shard                  = {SHARD_INDEX}/{SHARD_COUNT}")
    print(f"panels_checked         = {panel_count}")
    print(f"nodes_checked          = {node_count}")
    print(f"max_e_b                = {max_eb.str(40)}")
    print(f"max_e_b_location       = panel {max_eb_panel}, node {max_eb_node}")
    print(f"scalar_alpha_sum_upper = {scalar_sum.str(50)}")
    print(f"scalar_shard_target    = {SCALAR_SHARD_TARGET.str(30, radius=False)}")
    print("CERTIFIED: every node in this shard has C-odd vector error e_b < 1e-43")
    print("CERTIFIED: C-odd scalar-alpha perturbation contribution is below 1e-39/32")
    print("FIREWALL: C-odd shard success is not finite matrix positivity")


if __name__ == "__main__":
    main()
