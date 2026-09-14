#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic binary codec for the frozen A1 C-even exact integer matrix.

Only the upper triangle is stored.  Every entry is encoded by sign + unsigned
big-endian magnitude.  The reconstructed full matrix is fingerprinted with the
canonical row-major SHA256 used by certify_a1_c_even_exact_dyadic_matrix.py.
"""

import argparse
import struct
from pathlib import Path

from flint import fmpz_mat

from certify_a1_c_even_exact_dyadic_matrix import (
    DIM,
    PANEL_COUNT,
    build_k_int,
    build_shifted_integer_matrix,
    matrix_sha256,
)

MAGIC = b"A1CEVEN1"
EXPECTED_SHA256 = "97b761e9f89517303f557d3c18061cc1b232c821e5804fcf9071298e17e60183"


def _write_int(f, z: int) -> None:
    sign = 1 if z < 0 else 0
    a = abs(z)
    raw = a.to_bytes(max(1, (a.bit_length() + 7) // 8), "big")
    if len(raw) >= 65536:
        raise RuntimeError("integer magnitude too large for frozen codec")
    f.write(bytes((sign,)))
    f.write(struct.pack(">H", len(raw)))
    f.write(raw)


def _read_int(f) -> int:
    head = f.read(3)
    if len(head) != 3:
        raise RuntimeError("truncated integer header")
    sign = head[0]
    if sign not in (0, 1):
        raise RuntimeError("invalid integer sign byte")
    n = struct.unpack(">H", head[1:])[0]
    if n == 0:
        raise RuntimeError("zero-length integer magnitude")
    raw = f.read(n)
    if len(raw) != n:
        raise RuntimeError("truncated integer magnitude")
    a = int.from_bytes(raw, "big")
    return -a if sign else a


def write_symmetric_matrix(path: str, m: fmpz_mat) -> None:
    if m.nrows() != DIM or m.ncols() != DIM or m != m.transpose():
        raise RuntimeError("artifact writer requires frozen symmetric 1075x1075 matrix")
    p = Path(path)
    with p.open("wb") as f:
        f.write(MAGIC)
        f.write(struct.pack(">I", DIM))
        for i in range(DIM):
            for j in range(i, DIM):
                _write_int(f, int(m[i, j]))


def read_symmetric_matrix(path: str) -> fmpz_mat:
    p = Path(path)
    with p.open("rb") as f:
        if f.read(len(MAGIC)) != MAGIC:
            raise RuntimeError("matrix artifact magic mismatch")
        raw_dim = f.read(4)
        if len(raw_dim) != 4 or struct.unpack(">I", raw_dim)[0] != DIM:
            raise RuntimeError("matrix artifact dimension mismatch")
        data = [0] * (DIM * DIM)
        for i in range(DIM):
            for j in range(i, DIM):
                z = _read_int(f)
                data[i * DIM + j] = z
                data[j * DIM + i] = z
        if f.read(1) != b"":
            raise RuntimeError("matrix artifact has trailing bytes")
    m = fmpz_mat(DIM, DIM, data)
    if m != m.transpose():
        raise RuntimeError("decoded matrix is not symmetric")
    digest = matrix_sha256(m)
    if digest != EXPECTED_SHA256:
        raise RuntimeError(f"matrix artifact SHA256 mismatch: {digest}")
    return m


def build_artifact(path: str) -> None:
    k_int, node_count, elapsed = build_k_int(PANEL_COUNT)
    if node_count != PANEL_COUNT * 40:
        raise RuntimeError("full build node count mismatch")
    s, finish = build_shifted_integer_matrix(k_int)
    digest = matrix_sha256(s)
    if digest != EXPECTED_SHA256:
        raise RuntimeError(f"fresh matrix fingerprint mismatch: {digest}")
    write_symmetric_matrix(path, s)
    # Mandatory round-trip before publishing the artifact.
    s2 = read_symmetric_matrix(path)
    digest2 = matrix_sha256(s2)
    if digest2 != EXPECTED_SHA256:
        raise RuntimeError("round-trip fingerprint mismatch")
    print(f"build_elapsed={elapsed:.3f}s finish_elapsed={finish:.3f}s")
    print(f"artifact_bytes={Path(path).stat().st_size}")
    print(f"MATRIX_SHA256={digest2}")
    print("CERTIFIED: exact C-even integer matrix artifact round-trip matches frozen fingerprint")


def verify_artifact(path: str) -> None:
    m = read_symmetric_matrix(path)
    print(f"artifact_bytes={Path(path).stat().st_size}")
    print(f"MATRIX_SHA256={matrix_sha256(m)}")
    print("CERTIFIED: loaded C-even integer matrix matches frozen fingerprint")


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--build", action="store_true")
    mode.add_argument("--verify", action="store_true")
    parser.add_argument("--path", required=True)
    args = parser.parse_args()
    if args.build:
        build_artifact(args.path)
    else:
        verify_artifact(args.path)


if __name__ == "__main__":
    main()
