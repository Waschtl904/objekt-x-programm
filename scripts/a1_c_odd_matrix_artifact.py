#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic binary codec for the frozen A1 C-odd exact integer matrix.

Only the upper triangle is stored.  This first-stage codec deliberately does
not hard-code the matrix fingerprint: the full exact build discovers it once.
A follow-up hash-freeze commit must pin that value before positivity promotion.
"""

import argparse
import struct
from pathlib import Path

from flint import fmpz_mat

from certify_a1_c_odd_exact_dyadic_matrix import (
    DIM, PANEL_COUNT, build_k_int, build_shifted_integer_matrix, matrix_sha256,
)

MAGIC = b"A1CODD01"


def _write_int(f, z: int) -> None:
    sign = 1 if z < 0 else 0
    a = abs(z)
    raw = a.to_bytes(max(1, (a.bit_length() + 7) // 8), "big")
    if len(raw) >= 65536:
        raise RuntimeError("integer magnitude too large for frozen C-odd codec")
    f.write(bytes((sign,)))
    f.write(struct.pack(">H", len(raw)))
    f.write(raw)


def _read_int(f) -> int:
    head = f.read(3)
    if len(head) != 3:
        raise RuntimeError("truncated C-odd integer header")
    sign = head[0]
    if sign not in (0, 1):
        raise RuntimeError("invalid C-odd integer sign byte")
    n = struct.unpack(">H", head[1:])[0]
    if n == 0:
        raise RuntimeError("zero-length C-odd integer magnitude")
    raw = f.read(n)
    if len(raw) != n:
        raise RuntimeError("truncated C-odd integer magnitude")
    a = int.from_bytes(raw, "big")
    if sign and a == 0:
        raise RuntimeError("negative zero in C-odd artifact")
    return -a if sign else a


def write_symmetric_matrix(path: str, m: fmpz_mat) -> None:
    if m.nrows() != DIM or m.ncols() != DIM or m != m.transpose():
        raise RuntimeError("C-odd artifact writer requires symmetric 1075x1075 matrix")
    with Path(path).open("wb") as f:
        f.write(MAGIC)
        f.write(struct.pack(">I", DIM))
        for i in range(DIM):
            for j in range(i, DIM):
                _write_int(f, int(m[i, j]))


def read_symmetric_matrix(path: str, expected_sha: str | None = None) -> fmpz_mat:
    with Path(path).open("rb") as f:
        if f.read(len(MAGIC)) != MAGIC:
            raise RuntimeError("C-odd matrix artifact magic mismatch")
        raw_dim = f.read(4)
        if len(raw_dim) != 4 or struct.unpack(">I", raw_dim)[0] != DIM:
            raise RuntimeError("C-odd matrix artifact dimension mismatch")
        data = [0] * (DIM * DIM)
        for i in range(DIM):
            for j in range(i, DIM):
                z = _read_int(f)
                data[i * DIM + j] = z
                data[j * DIM + i] = z
        if f.read(1) != b"":
            raise RuntimeError("C-odd matrix artifact has trailing bytes")

    m = fmpz_mat(DIM, DIM, data)
    if m != m.transpose():
        raise RuntimeError("decoded C-odd matrix is not symmetric")
    digest = matrix_sha256(m)
    if expected_sha is not None and digest != expected_sha:
        raise RuntimeError(f"C-odd matrix artifact SHA256 mismatch: {digest}")
    return m


def build_artifact(path: str) -> None:
    k_int, node_count, elapsed = build_k_int(PANEL_COUNT)
    if node_count != PANEL_COUNT * 40:
        raise RuntimeError("full C-odd build node count mismatch")
    s, finish = build_shifted_integer_matrix(k_int)
    digest = matrix_sha256(s)
    write_symmetric_matrix(path, s)
    s2 = read_symmetric_matrix(path)
    digest2 = matrix_sha256(s2)
    if digest2 != digest:
        raise RuntimeError("C-odd round-trip fingerprint mismatch")
    print(f"build_elapsed={elapsed:.3f}s finish_elapsed={finish:.3f}s")
    print(f"artifact_bytes={Path(path).stat().st_size}")
    print(f"MATRIX_SHA256={digest2}")
    print("CERTIFIED: exact C-odd integer matrix artifact round-trip matches fresh fingerprint")
    print("FIREWALL: fingerprint must be frozen in a follow-up commit before positivity promotion")


def verify_artifact(path: str, expected_sha: str) -> None:
    m = read_symmetric_matrix(path, expected_sha)
    print(f"artifact_bytes={Path(path).stat().st_size}")
    print(f"MATRIX_SHA256={matrix_sha256(m)}")
    print("CERTIFIED: loaded C-odd integer matrix matches frozen fingerprint")


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--build", action="store_true")
    mode.add_argument("--verify", action="store_true")
    parser.add_argument("--path", required=True)
    parser.add_argument("--expect-sha")
    args = parser.parse_args()

    if args.build:
        if args.expect_sha is not None:
            raise RuntimeError("first-stage C-odd build must not predeclare an unknown hash")
        build_artifact(args.path)
    else:
        if not args.expect_sha:
            raise RuntimeError("C-odd verify requires --expect-sha")
        verify_artifact(args.path, args.expect_sha)


if __name__ == "__main__":
    main()
