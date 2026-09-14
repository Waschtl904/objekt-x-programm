#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exact dyadic full-matrix gate for the frozen A1 C-even certificate.

This script uses exactly the C-even proposal architecture already certified on
this branch:

* 3878 panels, Gauss-Legendre order 40, Omega=1551;
* direct turning-anchor even spherical-Bessel head, zero unresolved tail;
* nearest dyadic quantization with 160 fractional bits for alpha, b and moment;
* exact FLINT integer accumulation of B^T diag(A) B in row blocks.

Let alpha_q=A_s/2^160, b_q=B_s/2^160 and a_q=M/2^160.  The exact dyadic
finite block is

    A_q = 0.1 I + sum_s alpha_q,s b_q,s b_q,s^T + 2 a_q a_q^T.

Positivity above the already frozen stronger shift 1.005e-35 is equivalent,
after multiplication by the positive scale 10^38 * 2^480, to positivity of

    S = 10^38 K_int
        + 10^38 * 2^161 M M^T
        + (10^37 - 1005) * 2^480 I,

where K_int=sum_s A_s B_s B_s^T is an exact integer symmetric matrix.

The script has two modes:

  --smoke : build only a few panels and verify the dyadic/Gram machinery;
  --full  : build the complete 1075x1075 integer matrix and attempt a rigorous
            Arb eigenvalue positivity certificate on a fixed precision ladder.

No floating-point BLAS result enters the exact matrix.  If the final Arb
eigenvalue stage is undecided, the exact matrix assembly remains valid but the
C-even positivity theorem remains open.
"""

import argparse
import os
from time import perf_counter

from flint import arb, arb_mat, ctx, fmpz_mat

ctx.prec = 3072
ctx.threads = 2
os.environ["A1_PREC_BITS"] = "3072"

from check_a1_c_even_engine_preflight_arb import (  # noqa: E402
    A,
    GAUSS_N,
    MAX_DEGREE,
    OMEGA,
    PI,
    downward_from_direct_turning_anchors,
    gauss_node,
    moment_coeff,
    r_on_real_ball,
    turning_indices,
    upward_vector,
)

DIM = 1075
PANEL_COUNT = 3878
DYAD_BITS = 160
HALF_ULP = A(2) ** (-(DYAD_BITS + 1))
BLOCK_ROWS = 256
DEC38 = 10 ** 38
TWO160 = 1 << 160
TWO161 = 1 << 161
TWO480 = 1 << 480
DIAG_INTEGER = (10 ** 37 - 1005) * TWO480
EIG_PREC_LADDER = (512, 768, 1024, 1536, 2048, 3072)
EIG_SCALE_POW = 600


def sharp_even_head(z: arb):
    """Same sharp-head construction used by the certified 32-shard sweep."""
    low, high = turning_indices(z, MAX_DEGREE)
    up = upward_vector(z, low + 12)
    down = downward_from_direct_turning_anchors(z, high, max(2, low - 12))
    overlap_low = max(2, low - 8)
    overlap_high = min(low + 12, len(up) - 1, high)

    out = []
    for n in range(0, high + 1, 2):
        if n < overlap_low:
            v = up[n]
        elif n <= overlap_high:
            v = up[n].intersection(down[n])
            if v is None:
                raise RuntimeError(f"up/down overlap failed at n={n}")
        else:
            v = down[n]
        if not v.is_finite():
            raise RuntimeError(f"non-finite sharp even Bessel interval at n={n}")
        out.append((n, v))
    return out


def round_binary_mid_to_dyadic_int(x: arb, bits: int = DYAD_BITS) -> int:
    """Round the exact binary midpoint of x to an integer numerator / 2^bits.

    Ties are rounded away from zero.  The returned point is deterministic.
    """
    if not x.is_finite():
        raise RuntimeError("cannot quantize non-finite ball")
    man, exp = x.mid().man_exp()
    m = int(man)
    e = int(exp) + bits
    if e >= 0:
        return m << e
    den = 1 << (-e)
    am = abs(m)
    q, rem = divmod(am, den)
    if 2 * rem >= den:
        q += 1
    return q if m >= 0 else -q


def dyadic_point(q: int, bits: int = DYAD_BITS) -> arb:
    return A((q, -bits))


def quantize_exact_target(target: arb, label: str) -> int:
    """Choose a dyadic integer and rigorously prove half-ulp proximity.

    target may be a tiny Arb enclosure of an exact irrational proposal value.
    """
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
    """Return exact integer (A_s, B_s) for one frozen Gauss node."""
    x, w = gauss_node(panel, node_index)
    if not (x > 0 and x < A(OMEGA)):
        raise RuntimeError(f"Gauss node outside band at panel={panel}, node={node_index}")

    alpha_ball = w * r_on_real_ball(x)
    # The certified alpha proposal is the exact binary midpoint of the Arb ball.
    alpha0 = A(alpha_ball.mid())
    a_int = quantize_exact_target(alpha0, f"alpha[{panel},{node_index}]")

    b_int = [0] * DIM
    head = sharp_even_head(x)
    for n, jball in head:
        phase = -1 if ((n // 2) & 1) else 1
        coeff = (2 * A(2 * n + 1) / PI).sqrt()
        # Evaluation-error certificate uses the exact normalization times the
        # exact binary midpoint of the sharp j_n enclosure.
        target = phase * coeff * A(jball.mid())
        b_int[n // 2] = quantize_exact_target(
            target, f"b[{panel},{node_index},{n}]"
        )
    return a_int, b_int


def quantized_moment_vector():
    out = []
    for k in range(DIM):
        n = 2 * k
        target = moment_coeff(n)
        out.append(quantize_exact_target(target, f"moment[{n}]"))
    return out


def flush_block(k_int: fmpz_mat, alpha_rows, b_rows):
    rows = len(alpha_rows)
    if rows == 0:
        return k_int
    flat_b = []
    flat_ab = []
    for aa, row in zip(alpha_rows, b_rows):
        flat_b.extend(row)
        flat_ab.extend(aa * x for x in row)
    bmat = fmpz_mat(rows, DIM, flat_b)
    abmat = fmpz_mat(rows, DIM, flat_ab)
    block = bmat.transpose() * abmat
    if block != block.transpose():
        raise RuntimeError("exact weighted Gram block is not symmetric")
    return k_int + block


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
                alpha_rows.clear(); b_rows.clear()
        if (panel + 1) % 128 == 0 or panel + 1 == panel_limit:
            now = perf_counter()
            print(
                f"assembly_progress panels={panel+1}/{panel_limit} nodes={node_count} "
                f"elapsed={now-t0:.3f}s delta={now-last:.3f}s",
                flush=True,
            )
            last = now

    k_int = flush_block(k_int, alpha_rows, b_rows)
    if k_int != k_int.transpose():
        raise RuntimeError("complete K_int is not symmetric")
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
        raise RuntimeError("shifted exact integer matrix is not symmetric")
    return s, perf_counter() - t0


def smoke_checks(s: fmpz_mat, node_count: int):
    if node_count <= 0:
        raise RuntimeError("smoke build produced no nodes")
    # Algebra/API smoke: exact principal block remains symmetric and finite.
    n = 12
    lead = fmpz_mat(n, n, [s[i, j] for i in range(n) for j in range(n)])
    if lead != lead.transpose():
        raise RuntimeError("smoke leading block is not symmetric")
    if any(int(lead[i, i]) == 0 for i in range(n)):
        raise RuntimeError("smoke leading block has zero diagonal")
    print(f"SMOKE: leading12_trace_bits={abs(int(lead.trace())).bit_length()}")
    print("CERTIFIED: exact signed weighted-Gram and common integer scaling smoke passed")
    print("FIREWALL: smoke mode is not full C-even positivity")


def certify_positive_by_arb_eigenvalues(s: fmpz_mat):
    """Attempt a rigorous complete eigenvalue certificate on a fixed ladder."""
    for prec in EIG_PREC_LADDER:
        ctx.prec = prec
        print(f"===== EIG_PRECISION {prec} =====", flush=True)
        t0 = perf_counter()
        # Multiplication by 2^-600 is exact dyadic scaling and only keeps
        # numerical exponents moderate.  It does not change signs.
        a = arb_mat(s) * A((1, -EIG_SCALE_POW))
        try:
            vals = a.eig(multiple=True)
        except Exception as exc:
            print(f"eig_failed precision={prec}: {type(exc).__name__}: {exc}", flush=True)
            continue
        if len(vals) != DIM:
            print(f"eig_wrong_count precision={prec}: {len(vals)}", flush=True)
            continue

        ok = True
        min_re = None
        min_val = None
        for z in vals:
            re = z.real
            if min_re is None or re < min_re:
                min_re = re; min_val = z
            if not (re > 0):
                ok = False
        print(
            f"eig_done precision={prec} elapsed={perf_counter()-t0:.3f}s "
            f"min_ball={min_val}",
            flush=True,
        )
        if ok:
            # Convert the scaled integer eigenvalue lower enclosure back to the
            # physical eigenvalue of A_q - 1.005e-35 I:
            # S = 10^38 * 2^480 * (A_q-shift), and a=S*2^-600.
            # Hence physical = a * 2^120 / 10^38.
            physical = min_re * A((1, 120)) / A(DEC38)
            if not (physical > 0):
                raise RuntimeError("positive scaled eigenvalues but physical lower bound not positive")
            print(f"min_physical_ball = {physical.str(40)}", flush=True)
            print(f"CERTIFIED_PRECISION={prec}")
            print("CERTIFIED: exact dyadic shifted 1075x1075 C-even matrix is positive definite")
            print("CERTIFIED: A_e >= 1e-35 I_1075 after the frozen finite-model ledger")
            return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--smoke-panels", type=int, default=4)
    args = parser.parse_args()
    if args.smoke == args.full:
        raise SystemExit("choose exactly one of --smoke or --full")

    panel_limit = args.smoke_panels if args.smoke else PANEL_COUNT
    if not (1 <= panel_limit <= PANEL_COUNT):
        raise RuntimeError("invalid panel limit")

    print("A1 C-even exact dyadic matrix gate")
    print(f"mode={'smoke' if args.smoke else 'full'}")
    print(f"prec_bits={ctx.prec} threads={ctx.threads}")
    print(f"dim={DIM} panels={panel_limit} gauss_order={GAUSS_N} dyad_bits={DYAD_BITS}")
    print(f"block_rows={BLOCK_ROWS}")

    k_int, node_count, t_assembly = build_k_int(panel_limit)
    print(f"K_int_complete nodes={node_count} elapsed={t_assembly:.3f}s", flush=True)
    s, t_finish = build_shifted_integer_matrix(k_int)
    print(f"shifted_matrix_complete elapsed={t_finish:.3f}s", flush=True)
    print(f"shifted_trace_bits={abs(int(s.trace())).bit_length()}", flush=True)

    if args.smoke:
        smoke_checks(s, node_count)
        return

    expected_nodes = PANEL_COUNT * GAUSS_N
    if node_count != expected_nodes:
        raise RuntimeError(f"full build node count mismatch: {node_count} != {expected_nodes}")
    print("CERTIFIED: full exact integer 1075x1075 matrix assembly completed")
    print("CERTIFIED: epsilon_gemm = epsilon_storage = 0 for the exact dyadic matrix")

    if not certify_positive_by_arb_eigenvalues(s):
        raise RuntimeError(
            "full exact matrix assembled, but Arb eigenvalue positivity remained undecided on frozen precision ladder"
        )


if __name__ == "__main__":
    main()
