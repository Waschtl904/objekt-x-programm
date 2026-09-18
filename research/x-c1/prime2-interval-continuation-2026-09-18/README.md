# Prime-2 interval continuation

2026-09-18 — **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

For every `0 < a <= log(3)/2` and every nonzero function in the complete
connected `H1_0(-a,a)` class satisfying exactly the two Mellin conditions,

**`Q_W[u] > ||u||_2^2 / 100000`.**

This is a macroscopic interval theorem. It ends local point/crossing
optimization in this track. The endpoint includes the full Gamma and
Prime-2 terms; Prime 3 has zero overlap there.

The proof uses:

- one fixed reference space and the exact recombination of Node/Gamma
  terms into a logarithmic potential plus a bounded regular kernel;
- a quantitative Lipschitz bound on `[3/8, log(3)/2]`;
- the two exact Mellin moment corrections;
- two 15-dimensional Schur blocks with complete infinite-tail Gram
  identities, a positive actual tail, and the actual shear bound;
- the final division by `1 + beta`;
- exact isometric zero extension to certify the entire interval.

All proof decisions use rational outward interval arithmetic. The finite
matrices do not replace the infinite-dimensional operator. There is no
quadrature, numerical eigenvalue proof, A1, or third Mellin condition.

Files: `PROOF.md`, `check_interval.py`, `interval_checks.log`,
`interval_results.json`, this README, and `SHA256SUMS`.

Recompute and verify from any directory:

```text
python check_interval.py --verify
```

The default run is read-only; `--write` regenerates the deterministic
results, log, and five-payload manifest. No external Python package is
needed. The full run may take several minutes.

Source/form-level window isometries are proved. The global channel
readout geometry, the C0/C1 intertwiner, the range beyond the Prime-3
transition, a=1, Object X, and RH remain open. PR #137 remains Draft;
this append-only deposit does not merge or rewrite historical packages.
