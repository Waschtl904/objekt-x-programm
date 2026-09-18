# Prime-3 transition and continuation to log(2)

2026-09-18 — **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

For every `0 < a <= log(2)` and every nonzero function in the complete
connected `H1_0(-a,a)` class with exactly the two Mellin conditions,

**`Q_W[u] > ||u||_2^2 / 100000000000`.**

The proof certifies the exact endpoint `a=log(2)` with both shifts
`log(2)` and `log(3)`, then uses exact zero extension for the entire
interval. Prime-Power 4 has zero overlap at the endpoint. No local
crossing or split-parameter optimization is performed.

The new ingredient is the complete joint tail Gram: mixed Prime-2 /
Prime-3 terms and the logarithmic / Gamma / prime cross terms are
integrated analytically before bounding the actual Schur complement.
Two 15-dimensional low blocks retain their complete infinite tails.
The actual tail, actual shear, full two-moment correction, and final
division by `1+beta` are all certified by rational interval arithmetic.

The package also proves the correct new Node-band geometry, quadratic
H1-form activation at the Prime-3 entrance, and a common-space
Lipschitz constant 13 on `[3/8,log(2)]`. The interval gap follows from
an exact isometry, not a Lipschitz extrapolation across parameter boxes.

The general prime-power representation and window law are formulated
without dependence on a particular prime label. A positive reserve
uniform across all prime segments is **not** proved.

Files: `PROOF.md`, `check_prime3.py`, `prime3_checks.log`,
`prime3_results.json`, this README, and `SHA256SUMS`.

```text
python check_prime3.py --verify
```

This recomputes all 23 check groups, reproduces the JSON and log exactly,
and verifies the five payload hashes. Only Python's standard library
is needed; allow several minutes. The default run is read-only;
`--write` regenerates results and the manifest. No binary floats,
quadrature, numerical eigensolvers, A1, or third moment are used.

The preceding `eea8ff64...` theorem and this new theorem remain author
derivations awaiting independent external audit. This deposit is not
such an audit or a status promotion. The global channel geometry,
the unit window, Object X, and RH remain open. Keep PR #137 Draft and
unmerged; preserve all historical proof packages.
