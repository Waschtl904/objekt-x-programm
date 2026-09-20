# Full shell pivot and trace quotient

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 2026-09-18.
[German research summary](STATUS_DE.md).
Separate Shell-Schur branch; coordinate anchor `0ec5276b2e0a2fe0aa700503e40b4a6a0acb65ff`.
Publication parent: `ea06f01cc40911d67955065a51ff7bd7b7c1f720`, preserving
the concurrent form-interface package.

For B=log(5)/2 and 0<b-B<=10^-20, the complete even lifted-shell block satisfies

`D_b[s] >= |s(B)|^2/(32*10^13) + 70*||s||_L2(B,b)^2`.

This is an infinite-dimensional pivot theorem using the existing core gap
10^-13, exact moments, complete Gamma leakage and all four active channels
2,3,4,5. It is NOT a new all-source positivity theorem beyond B.

The natural completed trace-plus-L2 shell space shares the direction psi
with the completed old core. The uncompressed Schur operator therefore
has an exact null direction. The proof removes this coordinate redundancy
without restricting the original sources or adding a Mellin condition.
The remaining gate is the Schur lower bound on the entire reduced core;
the odd continuation is also open. See [PROOF.md](PROOF.md), Sections 7-9.

From repository root, Python 3.10+, standard library only:

```text
python research/x-c1/full-shell-pivot-trace-quotient-2026-09-18/check_shell_pivot.py --verify
```

Do not use Python -O. `--verify` checks frozen input bindings, all directed
constant and rational ledger decisions, the saved JSON/log, and SHA256SUMS.
The general form-domain, completion and quotient arguments are analytic
proofs, not conclusions from finitely many tests. No quadrature, spectral
sampling, third Mellin condition, A1 work, main edit or merge is involved.

The width 10^-20 is an explicit conservative proof interval. It is not an
optimized estimate, and does not consume the near-null Rayleigh upper
bound as if it were a uniform reserve. Historical files remain unchanged.

Section 10 shows directly on original H1 sequences that the concurrent
unreduced inverse-free relative ratio approaches 1. Its conditional theorem
is valid, but its strict global theta<1 hypothesis requires the same
coordinate correction before it can become a feasible research gate.
