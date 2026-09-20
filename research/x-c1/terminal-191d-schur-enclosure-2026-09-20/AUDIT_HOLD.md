# AUDIT HOLD — terminal 191D Schur enclosure

20.09.2026. **NO STATUS PROMOTION.**

The payload in this directory reports an author-derived candidate certificate
for strict positivity of the terminal even/odd 191D Schur matrices. The
operative registry correctly keeps the package at
`PENDING_STATUS_REVIEW` and keeps
`TERMINAL-191D-DEFECT-SCHUR-A1` **OPEN**.

This hold is not a mathematical refutation of the candidate result.

## Why promotion is blocked

The current package does not document the required **same-engine endpoint
calibration at**
[
B=rac{log 5}{2},
]
before interpreting the `a=1` sign. The 64 normalization checks are useful,
but they are not a full reproduction of the known positive endpoint with the
same directed assembly, complete High response and sign-certification path.

In addition, this audit environment could not independently execute
`python-flint==0.9.0`; therefore the stored Arb artifacts and the
`STRICT_POSITIVE_BOTH_PARITIES` log have not been independently replayed in
this review.

## Analytic points checked so far

The following parts are consistent with the inherited architecture and show no
immediate contradiction:

- the 191 low coordinates per parity are the bridge coordinates;
- the physical Schur route is legitimate because the bridge proves positive-Gram
  congruence with the C1 defect Schur rest;
- a sharper terminal High estimate may exploit the raw High space's mean-zero
  property to subtract the constant Gamma kernel component;
- at `a=1`, the Prime-2 partial translation has a three-vertex chain and the
  other active shifts are in the disjoint two-vertex regime;
- the complete coupling Gram construction follows the Active-Set tail-Gram
  architecture rather than sampling finitely many High modes;
- a fixed rational triangular preconditioner is only an untrusted witness if
  its congruence and all directed rows/pivots are recomputed by the checker.

These observations do **not** promote the terminal sign.

## Mandatory release gates

Before this package can be promoted from pending status:

1. The same directed assembly engine must be parameterized or replayed at
   `B=log(5)/2` and reproduce the already-known positive endpoint, including
   the complete High response and a rigorous positive sign certificate.
2. The calibration must be stronger than midpoint positivity: the directed
   enclosure itself must stay on the positive side.
3. The terminal checker must be run in the pinned
   `python-flint==0.9.0` environment with `--verify`; the matrix
   regeneration path must also be replayed (`--recompute` or an independently
   regenerated model) and match every stored A/G enclosure.
4. The derivation of the terminal High floor, the direction
   [
   A-eJ-delta^{-1}G^{act}
   ]
   and the Mellin-coordinate norm/error conversion must receive an independent
   analytic review.
5. Only after 1–4 pass may the candidate
   `STRICT_POSITIVE_BOTH_PARITIES` result be considered for registry
   promotion.

If the same-engine B calibration fails, the `a=1` sign is **UNDECIDED** and
must not be interpreted as positive or negative.

## Scope firewall

Until promotion, none of the following is claimed by the canonical state:

- (|R_1|le1);
- positivity through (a=1);
- a negative Weil source;
- full C1-GEOM;
- Objekt X;
- global Weil positivity;
- RH.


## Audit update — Same-Engine-B calibration PASSED

Commit `2374340f1bad3888d56c0be7cc93a1c939d22a3e`, workflow run
`35518951368`, executed the new Arb/Legendre assembly at
(B=log(5)/2) in the pinned `python-flint==0.9.0` environment.

The calibration passed in both parities. Entry-by-entry against the frozen
Fraction endpoint engine:

[
A_{m nonoverlap}=0,qquad
G_{m act,nonoverlap}=0,qquad
delta	ext{-overlap}=mathrm{true},qquad
L_{m nonoverlap}=0.
]

All 31 endpoint LDL pivots per parity were directed positive. The resulting
physical lower gaps are (>1.0423892675	imes10^{-13}) (even) and
(>2.3831654	imes10^{-11}) (odd).

Therefore release gate **1 (same-engine B calibration)** is now CLOSED.

The audit hold itself remains active. Still required before terminal promotion:

- pinned full terminal `check_terminal.py --verify --recompute` replay;
- independent analytic review of the terminal (7/10) High floor, enclosure
  direction and Mellin/physical norm conversion;
- explicit review that the stored rational preconditioners are only verified
  congruence witnesses and introduce no sign assumption.

The canonical terminal gate remains OPEN until these remaining items are
closed.
