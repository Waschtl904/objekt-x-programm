# Prime-power 4: uniform segment through log(5)/2

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.**

The fixed endpoint with all active channels 2,3,4 closes:

`Q_W[u] > 10^-13 ||u||_2^2` for every `0 < a <= log(5)/2`
and every nonzero `u in H1_0(-a,a) intersect ker E+ intersect ker E-`.

This includes the complete new segment `[log(2), log(5)/2]`.
Channel 4 has weight log(2)/2; channel 5 has zero overlap at the
right endpoint. Prime-2 central overlap and every mixed shift term
are included in the complete infinite-tail Gram.

PROOF.md gives a conditional finite-channel segment theorem, its
exact zero-extension law, the endpoint proof, and a reserve-loss
ledger. The checker uses 31 low modes per parity and controls the
entire tails from degrees 64 and 65. Its Gamma polynomial has
degree 64 with an analytic uniform remainder. Finite Schur bounds
come from an interval inverse trace, not a chosen tiny target.
Actual H1_0 two-Mellin trial sources provide upper diagnostics for
the optimal endpoint gap; they are not numerical eigenvalue proofs.

Run with standard-library Python:

```text
python check_segment.py --verify
```

Default execution recomputes without writing. `--write` explicitly
regenerates JSON, log and SHA256SUMS. Verification requires identical
JSON/log bytes and checks all five payload SHA-256 hashes. The
manifest does not hash itself. All arithmetic uses integers and
Fractions with outward rounding on a 10^-200 grid. No quadrature,
binary floating-point decision, A1 or third Mellin condition is used.

The reusable routines generate prime-power weights and integrate
an entire finite group of signed shifts before forming its Gram.
The deposited configuration is fixed at endpoint 5. A later
configuration must also certify its band arrangement, Gamma range,
moment errors, tail and Schur reserve; it is not certified merely
by reusing the engine. Exact coincident band endpoints need to be
identified algebraically before a future arrangement is certified.

Calculation base: `213edfd33d77b57c7ca272696be41339bf703f67`.
Publication base: `28351975097ed024ffa6a65145bc4a4d9b63d827`.
Both intervening structural packages are preserved: the active-set
theorem at `a18f90a8...` and the universal family at `28351975...`.
The active-set theorem is instantiated here at log(5)/2.
Append-only six-file addition to PR #137 on
`research/x-c0-common-memory-2026-09-16`; no merge, main or Registry
change. The preceding packages retain their review-open status.

Still open: independent external audit, later prime-power segments,
the unit window, a canonical positive reserve for all segments,
C1-GEOM, Object X and RH.
