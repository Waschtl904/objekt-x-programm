#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exact dyadic matrix builder for frozen A1 C-odd.

Odd degrees are 1,3,...,2149 (dimension 1075).  The exact dyadic block is

    A_q = 0.1 I + sum_s alpha_q,s b_q,s b_q,s^T + 2 a_q a_q^T.

As in C-even, positivity above 1.005e-35 is equivalent after multiplication by
10^38*2^480 to positivity of

    S = 10^38 K_int + 10^38*2^161 M M^T
        + (10^37-1005)*2^480 I.

This script builds/fingerprints S.  Positivity is a separate hash-fixed gate.
"""

import argparse
from time import perf_counter

from flint import fmpz_mat

from check_a1_c_even_engine_preflight_arb import (
    A, GAUSS_N, MAX_DEGREE, OMEGA, PI,
    downward_from_direct_turning_anchors, gauss_node, moment_coeff,
    r_on_real_ball, turning_indices, upward_vector,
)
from certify_a1_c_even_exact_dyadic_matrix import (
    DIM, PANEL_COUNT, DYAD_BITS, BLOCK_ROWS, DEC38, TWO161, TWO480,
    DIAG_INTEGER, HALF_ULP, matrix_sha256, matrix_trace_int,
    round_binary_mid_to_dyadic_int, dyadic_point, flush_block,
)


def sharp_odd_head(z):
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
                raise RuntimeError(f"odd up/down overlap failed at n={n}")
        else:
            v = down[n]
        if not v.is_finite():
            raise RuntimeError(f"non-finite sharp odd Bessel interval at n={n}")
        out.append((n, v))
    return out


def quantize_exact_target(target, label: str) -> int:
    if not target.is_finite():
        raise RuntimeError(f"non-finite quantization target: {label}")
    q = round_binary_mid_to_dyadic_int(target)
    err = abs(target - dyadic_point(q))
    if not (err <= HALF_ULP):
        raise RuntimeError(
            f"nearest-dyadic half-ulp check failed for {label}: err={err}, half_ulp={HALF_ULP}"
        )
    return q


def quantized_node(panel: int, node_index: int):
    x, w = gauss_node(panel, node_index)
    if not (x > 0 and x < A(OMEGA)):
        raise RuntimeError(f"Gauss node outside band at panel={panel}, node={node_index}")

    alpha_ball = w * r_on_real_ball(x)
    alpha_int = quantize_exact_target(A(alpha_ball.mid()), f"alpha[{panel},{node_index}]")
    b_int = [0] * DIM

    for n, jball in sharp_odd_head(x):
        # Real representative of the odd Fourier phase after removing the
        # common factor -i.  Any common global sign cancels in b b^T.
        phase = -1 if (((n - 1) // 2) & 1) else 1
        coeff = (2 * A(2 * n + 1) / PI).sqrt()
        target = phase * coeff * A(jball.mid())
        b_int[(n - 1) // 2] = quantize_exact_target(
            target, f"b_odd[{panel},{node_index},{n}]"
        )
    return alpha_int, b_int


def quantized_moment_vector():
    out = []
    for k in range(DIM):
        n = 2 * k + 1
        out.append(quantize_exact_target(moment_coeff(n), f"moment_odd[{n}]"))
    return out


def build_k_int(panel_limit: int):
    k_int = fmpz_mat(DIM, DIM)
    alpha_rows = []
    b_rows = []
    node_count = 0
    t0 = perf_counter()
    last = t0

    for panel in range(panel_limit):
        for node_index in range(GAUSS_N):
            aa, bb = quantized_node(panel, node_index)
            alpha_rows.append(aa)
            b_rows.append(bb)
            node_count += 1
            if len(alpha_rows) >= BLOCK_ROWS:
                k_int = flush_block(k_int, alpha_rows, b_rows)
                alpha_rows.clear()
                b_rows.clear()

        if (panel + 1) % 128 == 0 or panel + 1 == panel_limit:
            now = perf_counter()
            print(
                f"odd_assembly_progress panels={panel+1}/{panel_limit} nodes={node_count} "
                f"elapsed={now-t0:.3f}s delta={now-last:.3f}s",
                flush=True,
            )
            last = now

    k_int = flush_block(k_int, alpha_rows, b_rows)
    if k_int != k_int.transpose():
        raise RuntimeError("complete C-odd K_int is not symmetric")
    return k_int, node_count, perf_counter() - t0


def build_shifted_integer_matrix(k_int: fmpz_mat):
    t0 = perf_counter()
    m = quantized_moment_vector()
    mrow = fmpz_mat(1, DIM, m)
    mm = mrow.transpose() * mrow
    s = k_int * DEC38
    s = s + mm * (DEC38 * TWO161)
    for i in range(DIM):
        s[i, i] += DIAG_INTEGER
    if s != s.transpose():
        raise RuntimeError("shifted exact C-odd integer matrix is not symmetric")
    return s, perf_counter() - t0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--build-only", action="store_true")
    parser.add_argument("--smoke-panels", type=int, default=4)
    args = parser.parse_args()
    if args.smoke == args.build_only:
        raise SystemExit("choose exactly one of --smoke or --build-only")

    panel_limit = args.smoke_panels if args.smoke else PANEL_COUNT
    if not (1 <= panel_limit <= PANEL_COUNT):
        raise RuntimeError("invalid panel limit")

    print("A1 C-odd exact dyadic matrix builder")
    print(f"mode={'smoke' if args.smoke else 'build-only'}")
    print(f"dim={DIM} panels={panel_limit} gauss_order={GAUSS_N} dyad_bits={DYAD_BITS}")
    print(f"odd_degrees=1,3,...,2149 block_rows={BLOCK_ROWS}")

    k_int, node_count, t_assembly = build_k_int(panel_limit)
    print(f"K_int_complete nodes={node_count} elapsed={t_assembly:.3f}s", flush=True)
    s, t_finish = build_shifted_integer_matrix(k_int)
    print(f"shifted_matrix_complete elapsed={t_finish:.3f}s", flush=True)
    print(f"shifted_trace_bits={abs(matrix_trace_int(s)).bit_length()}", flush=True)

    if args.smoke:
        n = 12
        lead = fmpz_mat(n, n, [s[i, j] for i in range(n) for j in range(n)])
        if lead != lead.transpose():
            raise RuntimeError("C-odd smoke leading block is not symmetric")
        if any(int(lead[i, i]) == 0 for i in range(n)):
            raise RuntimeError("C-odd smoke leading block has zero diagonal")
        print("CERTIFIED: C-odd exact signed weighted-Gram/common-scaling smoke passed")
        print("FIREWALL: smoke mode is not full C-odd positivity")
        return

    expected_nodes = PANEL_COUNT * GAUSS_N
    if node_count != expected_nodes:
        raise RuntimeError(f"full C-odd build node count mismatch: {node_count} != {expected_nodes}")
    digest = matrix_sha256(s)
    print(f"MATRIX_SHA256={digest}", flush=True)
    print("CERTIFIED: full exact C-odd integer 1075x1075 matrix assembly completed")
    print("CERTIFIED: C-odd epsilon_gemm = epsilon_storage = 0 for exact dyadic matrix")
    print("FIREWALL: exact C-odd matrix build is not yet the positivity certificate")


if __name__ == "__main__":
    main()
