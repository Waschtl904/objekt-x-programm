#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exact dyadic matrix builder / positivity gate for frozen A1 C-even.

The exact dyadic finite block is

    A_q = 0.1 I + sum_s alpha_q,s b_q,s b_q,s^T + 2 a_q a_q^T,

with 160 fractional bits for alpha, b and a.  Positivity above the stronger
shift 1.005e-35 is equivalent, after multiplying by 10^38*2^480, to
positivity of the exact integer symmetric matrix

    S = 10^38 K_int
        + 10^38 * 2^161 M M^T
        + (10^37 - 1005) * 2^480 I.

Modes:
  --smoke      : few-panel backend/API smoke only;
  --build-only : build all 155120 nodes and fingerprint the complete S;
  --full       : rebuild complete S and attempt rigorous Arb positivity.

The split is deliberate: the expensive exact matrix construction gets its own
stable checkpoint before any large spectral calculation.
"""

import argparse
import hashlib
import os
from time import perf_counter

from flint import arb, arb_mat, ctx, fmpz_mat

ctx.prec = 3072
ctx.threads = 2
os.environ["A1_PREC_BITS"] = "3072"

from check_a1_c_even_engine_preflight_arb import (  # noqa: E402
    A, GAUSS_N, MAX_DEGREE, OMEGA, PI,
    downward_from_direct_turning_anchors, gauss_node, moment_coeff,
    r_on_real_ball, turning_indices, upward_vector,
)

DIM = 1075
PANEL_COUNT = 3878
DYAD_BITS = 160
HALF_ULP = A(2) ** (-(DYAD_BITS + 1))
BLOCK_ROWS = 256
DEC38 = 10 ** 38
TWO161 = 1 << 161
TWO480 = 1 << 480
DIAG_INTEGER = (10 ** 37 - 1005) * TWO480
EIG_PREC_LADDER = (512, 768, 1024, 1536, 2048, 3072)
EIG_SCALE_POW = 600


def matrix_trace_int(m: fmpz_mat) -> int:
    return sum(int(m[i, i]) for i in range(min(m.nrows(), m.ncols())))


def matrix_sha256(m: fmpz_mat) -> str:
    """Deterministic row-major hash, independent of Python object encoding."""
    h = hashlib.sha256()
    h.update(f"fmpz-matrix-v1:{m.nrows()}:{m.ncols()}\n".encode("ascii"))
    for i in range(m.nrows()):
        for j in range(m.ncols()):
            z = int(m[i, j])
            sign = b"-" if z < 0 else b"+"
            a = abs(z)
            raw = a.to_bytes(max(1, (a.bit_length() + 7) // 8), "big")
            h.update(sign)
            h.update(len(raw).to_bytes(4, "big"))
            h.update(raw)
    return h.hexdigest()


def sharp_even_head(z: arb):
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
    a_int = quantize_exact_target(A(alpha_ball.mid()), f"alpha[{panel},{node_index}]")
    b_int = [0] * DIM
    for n, jball in sharp_even_head(x):
        phase = -1 if ((n // 2) & 1) else 1
        coeff = (2 * A(2 * n + 1) / PI).sqrt()
        target = phase * coeff * A(jball.mid())
        b_int[n // 2] = quantize_exact_target(target, f"b[{panel},{node_index},{n}]")
    return a_int, b_int


def quantized_moment_vector():
    out = []
    for k in range(DIM):
        n = 2 * k
        out.append(quantize_exact_target(moment_coeff(n), f"moment[{n}]"))
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
            alpha_rows.append(aa); b_rows.append(bb); node_count += 1
            if len(alpha_rows) >= BLOCK_ROWS:
                k_int = flush_block(k_int, alpha_rows, b_rows)
                alpha_rows.clear(); b_rows.clear()
        if (panel + 1) % 128 == 0 or panel + 1 == panel_limit:
            now = perf_counter()
            print(
                f"assembly_progress panels={panel+1}/{panel_limit} nodes={node_count} "
                f"elapsed={now-t0:.3f}s delta={now-last:.3f}s", flush=True
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
    n = 12
    lead = fmpz_mat(n, n, [s[i, j] for i in range(n) for j in range(n)])
    if lead != lead.transpose():
        raise RuntimeError("smoke leading block is not symmetric")
    if any(int(lead[i, i]) == 0 for i in range(n)):
        raise RuntimeError("smoke leading block has zero diagonal")
    print(f"SMOKE: leading12_trace_bits={abs(matrix_trace_int(lead)).bit_length()}")
    # Exercise the exact integer -> Arb matrix API used later, without making a
    # positivity claim about this truncated four-panel smoke matrix.
    ctx.prec = 512
    a = arb_mat.convert(lead) * A((1, -EIG_SCALE_POW))
    vals = a.eig(multiple=True)
    if len(vals) != n:
        raise RuntimeError(f"smoke Arb eig returned {len(vals)} values instead of {n}")
    print("SMOKE: arb_mat.convert/eig API passed")
    print("CERTIFIED: exact signed weighted-Gram and common integer scaling smoke passed")
    print("FIREWALL: smoke mode is not full C-even positivity")


def certify_positive_by_arb_eigenvalues(s: fmpz_mat):
    for prec in EIG_PREC_LADDER:
        ctx.prec = prec
        print(f"===== EIG_PRECISION {prec} =====", flush=True)
        t0 = perf_counter()
        a = arb_mat.convert(s) * A((1, -EIG_SCALE_POW))
        try:
            vals = a.eig(multiple=True)
        except Exception as exc:
            print(f"eig_failed precision={prec}: {type(exc).__name__}: {exc}", flush=True)
            continue
        if len(vals) != DIM:
            print(f"eig_wrong_count precision={prec}: {len(vals)}", flush=True)
            continue
        ok = True
        min_val = None
        min_mid = None
        for z in vals:
            re = z.real
            midpoint = re.mid()
            if min_mid is None or midpoint < min_mid:
                min_mid = midpoint; min_val = z
            if not (re > 0):
                ok = False
        print(
            f"eig_done precision={prec} elapsed={perf_counter()-t0:.3f}s min_ball={min_val}",
            flush=True,
        )
        if ok:
            min_re = vals[0].real
            for z in vals[1:]:
                re = z.real
                if re.lower() < min_re.lower():
                    min_re = re
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
    parser.add_argument("--build-only", action="store_true")
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--smoke-panels", type=int, default=4)
    args = parser.parse_args()
    if sum((args.smoke, args.build_only, args.full)) != 1:
        raise SystemExit("choose exactly one of --smoke, --build-only or --full")

    panel_limit = args.smoke_panels if args.smoke else PANEL_COUNT
    if not (1 <= panel_limit <= PANEL_COUNT):
        raise RuntimeError("invalid panel limit")
    mode = "smoke" if args.smoke else ("build-only" if args.build_only else "full")
    print("A1 C-even exact dyadic matrix gate")
    print(f"mode={mode}")
    print(f"prec_bits={ctx.prec} threads={ctx.threads}")
    print(f"dim={DIM} panels={panel_limit} gauss_order={GAUSS_N} dyad_bits={DYAD_BITS}")
    print(f"block_rows={BLOCK_ROWS}")

    k_int, node_count, t_assembly = build_k_int(panel_limit)
    print(f"K_int_complete nodes={node_count} elapsed={t_assembly:.3f}s", flush=True)
    s, t_finish = build_shifted_integer_matrix(k_int)
    print(f"shifted_matrix_complete elapsed={t_finish:.3f}s", flush=True)
    print(f"shifted_trace_bits={abs(matrix_trace_int(s)).bit_length()}", flush=True)

    if args.smoke:
        smoke_checks(s, node_count)
        return

    expected_nodes = PANEL_COUNT * GAUSS_N
    if node_count != expected_nodes:
        raise RuntimeError(f"full build node count mismatch: {node_count} != {expected_nodes}")
    digest = matrix_sha256(s)
    print(f"MATRIX_SHA256={digest}", flush=True)
    print("CERTIFIED: full exact integer 1075x1075 matrix assembly completed")
    print("CERTIFIED: epsilon_gemm = epsilon_storage = 0 for the exact dyadic matrix")

    if args.build_only:
        print("FIREWALL: exact matrix build is not yet the C-even positivity certificate")
        return

    if not certify_positive_by_arb_eigenvalues(s):
        raise RuntimeError(
            "full exact matrix assembled, but Arb eigenvalue positivity remained undecided on frozen precision ladder"
        )


if __name__ == "__main__":
    main()
