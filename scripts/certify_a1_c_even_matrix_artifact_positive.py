#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Positivity gate for the frozen exact C-even integer matrix artifact.

This script performs no quadrature and no matrix assembly.  It accepts only the
binary artifact whose decoded row-major SHA256 equals the frozen fingerprint,
then applies the already frozen Arb precision ladder to that exact matrix.
"""

import argparse

from a1_c_even_matrix_artifact import EXPECTED_SHA256, read_symmetric_matrix
from certify_a1_c_even_exact_dyadic_matrix import (
    certify_positive_by_arb_eigenvalues,
    matrix_sha256,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    args = parser.parse_args()

    s = read_symmetric_matrix(args.path)
    digest = matrix_sha256(s)
    if digest != EXPECTED_SHA256:
        raise RuntimeError("frozen matrix fingerprint mismatch before positivity gate")
    print(f"MATRIX_SHA256={digest}", flush=True)
    print("CERTIFIED: positivity job loaded the frozen exact C-even matrix", flush=True)

    if not certify_positive_by_arb_eigenvalues(s):
        raise RuntimeError(
            "frozen exact matrix loaded correctly, but positivity remained undecided on the frozen precision ladder"
        )


if __name__ == "__main__":
    main()
