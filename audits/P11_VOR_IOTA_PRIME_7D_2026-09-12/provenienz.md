# Provenienz -- Vor-iota' Zug 7D bounded-transform cross-bridge

This chronology records the errors and repairs that led to the 7D certificate.  It is part of the mathematical provenance; superseded numerical values are not promoted by being recorded here.

## P1 -- PR #96 leaves the relevant class open

Merged PR #96 proves d-exact failure only for the native Rest Gram and the native Feshbach/Schur Gram at `R=1`.  Its nonclaims explicitly leave open nontrivial mediators and pre-Schur nonorthogonal Hub/Rest cross terms.

Therefore a later result for a canonical cross bridge is new information, not a restatement of PR #96.

## P2 -- 7A type firewall

The naive expression `<H_R f, R_R g>` was rejected: the Hub output and full-rest analysis output do not naturally live in the same Hilbert space.

This prevented a repetition of the earlier `H_A/E_A/Pi_A` placeholder error class.

## P3 -- Polar and graph bridges

The polar partial isometry of `T=\widetilde R_R` is canonical, but on same-source vectors the orientation collapses through

```math
U^*T=(T^*T)^{1/2}.
```

The canonical graph bridge `B T^*` is also well-defined and yields a positive block metric, but its same-source Prime-2 cross term vanishes by parity for the odd PR-#91 witness.

The parity interpretation was corrected during review: the witness `a,b` is odd, not even.

## P4 -- 7D bridge

To obtain a canonical parity-compatible bridge without fitting a scalar, the two canonical bounded transforms were composed:

```math
M_7D = H(I+H^*H)^{-1}(I+A)^{-1}T^*.
```

Its norm is at most `1/4`, so the associated block metric is at least `3/4 I`.

The same-source cross correction reduces to the anticommutator of the two resolvent defects

```math
P_H = H^*H/(I+H^*H),
P_R = A/(I+A).
```

No Weil coefficient is inserted into this definition.

## P5 -- First CG value withdrawn as a certificate

An initial Dictionary/CG computation gave approximately

```text
X_7D(a,b) = -0.070736.
```

That value had the correct sign and order of magnitude, but the computation was **not certified**:

- with bump half-width `epsilon=1e-4`, repeated `H^*H` applications generate distinct nonzero lobes whose centres overlap;
- already at `(H^*H)^3 a` a centre gap around `1.143e-4` is below `2*epsilon`;
- the exploratory CG implementation also pruned small amplitudes without a complete error bound.

The 7D d-exact status was reset to OPEN.

## P6 -- Tool change: tuple DP plus Chebyshev

The resolvent was replaced by a finite Chebyshev approximation.  Exact half-log exponent tuples are accumulated after every shift, so the representation tracks reachable centres rather than a branching path tree.

For `r(t)=1/(1+t)` on `[0,L]`, the explicit Chebyshev tail gives a priori control.  Conservative spectral boxes `L_H=16` and `L_R=32` are derived from operator norm majorants rather than fitted from numerics.

At degree `N=13`, the central calculation is already accurate enough to separate the Prime-2 target.

## P7 -- Width firewall repaired

The hardened run uses bump half-width

```text
epsilon = 1e-8.
```

The finite Chebyshev support is checked directly:

- every source/window cutoff decision must certify the entire lobe strictly inside or outside;
- final distinct lobe centres must be more than `2*epsilon` apart before tuplewise orthogonality is used.

No small-amplitude pruning is used in the certificate.

## P8 -- Arb hardening

The final certificate uses `flint.arb` at precision `200` bits for:

- logarithms;
- square roots;
- prime-power weights;
- Chebyshev coefficients;
- finite tuple-DP arithmetic;
- spectral-bound comparisons;
- target and separation comparison.

Reported hardened values include

```text
X_13  = -0.07161580220284683...     (ball radius < 3e-56)
Delta =  0.01951899370897315...
X_req = -0.11727646455338526...
X_lo - X_req = +0.02614166864156528... > 0
```

The large positive reserve makes the d-exact failure insensitive to display rounding.

## P9 -- Interpretation firewall

The exploratory ratio `X_7D/X_req approximately 0.603` is **not** interpreted as `3/5`, `1/e` or any other constant.  No PSLQ inference is part of the result.

The only promoted local conclusion of this package is:

```text
7D d-exact FAIL in the stated R=1 Prime-2 scope.
```

There is no universal cross-term, Object-X or RH no-go.

## P10 -- Governance

This local package was prepared against `main@5280471a550f2ce2b8a0e55d8a07646d82baff34` after the PR #96 merge.

At preparation time:

- no GitHub branch was created;
- no file was pushed;
- no PR was opened;
- no Registry entry was changed;
- no merge was performed.

Before any future push, the current `main` head and the exact package bytes must be rechecked.  Push requires explicit user authorization.
