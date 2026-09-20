#!/usr/bin/env python3
"""Rigorous-ball diagnostic for the terminal 191D Schur gate.

This script constructs a dyadic finite-head lower-Weil model from the frozen
hash-fixed A1 Legendre artifacts. It is diagnostic only: it does not pay the
exact-moment, finite-model or infinite-tail comparison required for the
terminal theorem.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path
import sys
from time import perf_counter

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from flint import arb, arb_mat, ctx, fmpz_mat  # noqa: E402

EVEN_SHA = "97b761e9f89517303f557d3c18061cc1b232c821e5804fcf9071298e17e60183"
ODD_SHA = "6cff5e4710f0f23c4b43503e5b398525898e0a034e61c25791526ad94f17e295"
MODEL_SCALE = (10 ** 38) * (1 << 480)
SHIFT_INT = 1005 * (1 << 480)
LOW_DIM = 191
SOURCE_DIM = 1074
HIGH_DIM = SOURCE_DIM - LOW_DIM


def load_artifact(parity: str, path: Path):
    if parity == "even":
        import a1_c_even_matrix_artifact as codec
        m = codec.read_symmetric_matrix(str(path))
        digest = codec.matrix_sha256(m)
        expected = EVEN_SHA
    else:
        import a1_c_odd_matrix_artifact as codec
        m = codec.read_symmetric_matrix(str(path), ODD_SHA)
        digest = codec.matrix_sha256(m)
        expected = ODD_SHA
    if digest != expected:
        raise RuntimeError(f"logical matrix SHA256 mismatch: {digest} != {expected}")
    return m, digest


def moment_vector(parity: str):
    if parity == "even":
        import certify_a1_c_even_exact_dyadic_matrix as builder
    else:
        import certify_a1_c_odd_exact_dyadic_matrix as builder
    m = [int(x) for x in builder.quantized_moment_vector()]
    if len(m) != SOURCE_DIM + 1 or m[0] == 0:
        raise RuntimeError("unexpected frozen moment vector")
    return m


def source_entry(S, moment, i: int, j: int) -> int:
    """Exact y_i^T (S + SHIFT_INT I) y_j for source indices i,j>=1."""
    m0 = moment[0]
    mi = moment[i]
    mj = moment[j]
    qij = int(S[i, j]) + (SHIFT_INT if i == j else 0)
    q00 = int(S[0, 0]) + SHIFT_INT
    return (
        m0 * m0 * qij
        - m0 * mj * int(S[i, 0])
        - mi * m0 * int(S[0, j])
        + mi * mj * q00
    )


def exact_blocks(S, moment):
    t0 = perf_counter()
    low = list(range(1, LOW_DIM + 1))
    high = list(range(LOW_DIM + 1, SOURCE_DIM + 1))

    aflat = [source_entry(S, moment, i, j) for i in low for j in low]
    bflat = [source_entry(S, moment, i, j) for i in high for j in low]
    hflat = [source_entry(S, moment, i, j) for i in high for j in high]

    A = fmpz_mat(LOW_DIM, LOW_DIM, aflat)
    B = fmpz_mat(HIGH_DIM, LOW_DIM, bflat)
    H = fmpz_mat(HIGH_DIM, HIGH_DIM, hflat)
    if A != A.transpose() or H != H.transpose():
        raise RuntimeError("exact source block lost symmetry")
    return A, B, H, perf_counter() - t0


def scaled_ball_matrix(Z, denominator: int):
    return arb_mat.convert(Z) / arb(denominator)


def write_symmetric_integer_artifact(path: Path, M: fmpz_mat) -> str:
    if M.nrows() != M.ncols() or M != M.transpose():
        raise RuntimeError("integer artifact requires a symmetric square matrix")
    magic = b"T191HIGH1"
    h = hashlib.sha256()
    with path.open("wb") as f:
        f.write(magic)
        f.write(struct.pack(">I", M.nrows()))
        for i in range(M.nrows()):
            for j in range(i, M.ncols()):
                z = int(M[i, j])
                sign = 1 if z < 0 else 0
                raw = abs(z).to_bytes(max(1, (abs(z).bit_length() + 7) // 8), "big")
                if len(raw) >= 65536:
                    raise RuntimeError("integer magnitude too large")
                record = bytes((sign,)) + struct.pack(">H", len(raw)) + raw
                f.write(record)
                h.update(record)
    return h.hexdigest()


def interval_tsv(M: arb_mat) -> bytes:
    rows = []
    for i in range(M.nrows()):
        rows.append("\t".join(M[i, j].str(28, radius=True) for j in range(M.ncols())))
    return ("\n".join(rows) + "\n").encode("utf-8")


def classify_eigenvalues(vals):
    negative = []
    undecided = []
    positive = []
    for idx, z in enumerate(vals):
        r = z.real
        if r < 0:
            negative.append(idx)
        elif r > 0:
            positive.append(idx)
        else:
            undecided.append(idx)
    if negative:
        verdict = "NEGATIVE_DIAGNOSTIC"
    elif not undecided:
        verdict = "POSITIVE_DIAGNOSTIC"
    else:
        verdict = "UNDECIDED_DIAGNOSTIC"
    return verdict, negative, undecided, positive


def run(parity: str, artifact: Path, precisions, output_prefix: Path):
    S_art, digest = load_artifact(parity, artifact)
    moment = moment_vector(parity)
    Aint, Bint, Hint, assembly_seconds = exact_blocks(S_art, moment)

    m0 = moment[0]
    denominator = MODEL_SCALE * m0 * m0
    source_degrees = (
        list(range(2, 2150, 2)) if parity == "even"
        else list(range(3, 2151, 2))
    )
    if len(source_degrees) != SOURCE_DIM:
        raise RuntimeError("source degree count mismatch")
    if source_degrees[LOW_DIM - 1] not in (382, 383):
        raise RuntimeError("low-coordinate boundary mismatch")
    if source_degrees[LOW_DIM] not in (384, 385):
        raise RuntimeError("high-coordinate boundary mismatch")

    attempts = []
    final = None
    for prec in precisions:
        ctx.prec = prec
        t0 = perf_counter()
        A = scaled_ball_matrix(Aint, denominator)
        B = scaled_ball_matrix(Bint, denominator)
        H = scaled_ball_matrix(Hint, denominator)

        high_floor_artifact = None
        high_floor_sha256 = None
        b_frobenius_upper = None
        if prec == precisions[0]:
            b_sq = sum(int(Bint[i, j]) ** 2
                       for i in range(Bint.nrows())
                       for j in range(Bint.ncols()))
            b_frobenius_upper = (arb(b_sq).sqrt() / arb(denominator)).str(40, radius=True)

            shifted_high = Hint * 1000
            for i in range(HIGH_DIM):
                shifted_high[i, i] -= denominator
            high_floor_artifact = output_prefix.with_name(
                output_prefix.name + f"_{parity}_high_minus_1e-3.bin"
            )
            high_floor_sha256 = write_symmetric_integer_artifact(
                high_floor_artifact, shifted_high
            )

        try:
            X = H.solve(B, algorithm="precond")
        except ZeroDivisionError as exc:
            attempts.append({
                "precision_bits": prec,
                "status": "HIGH_SOLVE_UNDECIDED",
                "error": str(exc),
                "seconds": perf_counter() - t0,
            })
            continue

        Schur = A - B.transpose() * X
        Schur = (Schur + Schur.transpose()) / 2
        solve_seconds = perf_counter() - t0

        t1 = perf_counter()
        vals = Schur.eig(multiple=True)
        eig_seconds = perf_counter() - t1
        if len(vals) != LOW_DIM:
            raise RuntimeError(f"eigenvalue count mismatch: {len(vals)}")
        vals = sorted(vals, key=lambda z: float(z.real.mid()))
        verdict, negative, undecided, positive = classify_eigenvalues(vals)
        min_ball = vals[0].real
        max_ball = vals[-1].real

        raw = interval_tsv(Schur)
        matrix_path = output_prefix.with_name(
            output_prefix.name + f"_{parity}_{prec}bit_schur.tsv"
        )
        matrix_path.write_bytes(raw)
        matrix_hash = hashlib.sha256(raw).hexdigest()

        attempt = {
            "precision_bits": prec,
            "status": verdict,
            "negative_eigenvalue_balls": len(negative),
            "zero_meeting_eigenvalue_balls": len(undecided),
            "positive_eigenvalue_balls": len(positive),
            "minimum_eigenvalue_ball": min_ball.str(50, radius=True),
            "maximum_eigenvalue_ball": max_ball.str(30, radius=True),
            "matrix_tsv": matrix_path.name,
            "matrix_tsv_sha256": matrix_hash,
            "solve_seconds": solve_seconds,
            "eig_seconds": eig_seconds,
            "finite_high_floor_target": "1e-3",
            "finite_high_shifted_artifact": (
                None if high_floor_artifact is None else high_floor_artifact.name
            ),
            "finite_high_shifted_artifact_sha256": high_floor_sha256,
            "mixed_block_frobenius_upper": b_frobenius_upper,
        }
        attempts.append(attempt)
        final = (verdict, vals, matrix_path)
        if verdict != "UNDECIDED_DIAGNOSTIC":
            break

    overall = "HIGH_SOLVE_UNDECIDED" if final is None else final[0]

    result = {
        "status": "DIAGNOSTIC / NO STATUS PROMOTION",
        "parity": parity,
        "artifact": artifact.name,
        "logical_matrix_sha256": digest,
        "source_dimension": SOURCE_DIM,
        "low_dimension": LOW_DIM,
        "finite_high_dimension": HIGH_DIM,
        "low_degrees": [source_degrees[0], source_degrees[LOW_DIM - 1]],
        "finite_high_degrees": [source_degrees[LOW_DIM], source_degrees[-1]],
        "moment_carrier_degree": 0 if parity == "even" else 1,
        "exact_dyadic_moment_neutrality": True,
        "assembly_seconds": assembly_seconds,
        "attempts": attempts,
        "verdict": overall,
        "theorem_promotion": False,
        "hardening_gaps": [
            "exact physical moments versus dyadic moments",
            "exact bounded multiplier versus dyadic finite model",
            "infinite Legendre tail and omitted positive high-frequency contribution",
        ],
    }
    out_json = output_prefix.with_name(output_prefix.name + f"_{parity}_result.json")
    out_json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8", newline="\n")

    print(f"PARITY={parity}")
    print(f"LOGICAL_MATRIX_SHA256={digest}")
    print(f"LOW_DIM={LOW_DIM} FINITE_HIGH_DIM={HIGH_DIM}")
    print(f"ASSEMBLY_SECONDS={assembly_seconds:.3f}")
    for attempt in attempts:
        print("ATTEMPT", json.dumps(attempt, sort_keys=True))
    print(f"VERDICT={overall}")
    print("FIREWALL: diagnostic dyadic finite-head Schur model only; no exact terminal positivity claim")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parity", choices=("even", "odd"), required=True)
    ap.add_argument("--artifact", type=Path, required=True)
    ap.add_argument("--precisions", default="256,384,512")
    ap.add_argument("--output-prefix", type=Path, default=HERE / "terminal")
    args = ap.parse_args()
    precisions = [int(x) for x in args.precisions.split(",") if x.strip()]
    if not precisions or any(p < 128 for p in precisions):
        raise SystemExit("precision ladder must contain integers >=128")
    run(args.parity, args.artifact.resolve(), precisions, args.output_prefix.resolve())


if __name__ == "__main__":
    main()
