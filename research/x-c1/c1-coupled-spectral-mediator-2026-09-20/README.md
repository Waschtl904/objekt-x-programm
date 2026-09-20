# Coupled spectral C1 candidate, 2026-09-20

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**. Anchor: `f77116a`.

An explicit infinite-dimensional positive candidate target and a genuinely
nonlocal, common Prime/Gamma readout are constructed on the fixed physical
horizon `B<=a<=1`. The maps intertwine exactly under source zero extension.
The readout is defined without assuming positivity of the Weil form.

With the full Gamma symbol g, the five horizon weights (2,3,4,5,7), their
sum omega and cosine sum c, set

    s = kappa + 2 omega
    T u = (g + omega - c) / sqrt(g+s) * Fourier(u)
    D u = (kappa + omega + c) / sqrt(g+s) * Fourier(u).

Then exactly `q=<T,T>-<D,D>`. On `H_a=closure(T W_a)`, the defect transfer
`R_a(Tu)=Du` is compact, injective and of infinite rank, and satisfies
`R_b I_ab=R_a`. The candidate readout satisfies `T_b J_ab=I_ab T_a`.
Its actual Gram error is strictly negative on every nonzero diagonal;
the uncorrected T is therefore not an exact Weil-Gram readout.

The residual positivity gate is `||R_a||<=1`. It is **not** proved on new
windows. Compactness reduces possible sign obstructions to finitely many
singular values at or above one, without deciding their values. A fully
explicit finite-rank approximation bound is supplied; no numerical
eigenvalue is used as a sign certificate.

See `PROOF.md` for the analytic theorem, physical nonlocality proof,
domain completion, common channel observations, transition laws, and the
distinction between compression and operator intertwining.

Reproduce from any location using Python 3 (standard library only):

    python check_mediator.py --verify

`--write` regenerates the result, log and manifest; `--verify` requires
byte-identical JSON/log and seven matching payload hashes. The same
ledger of 53 exact checks is used in both modes. Five immutable provenance files
are bound by byte length, SHA256 and Git blob id. No prior numerical
matrix chain is replayed by this checker.

Full C1, unrestricted-horizon compatibility, Moving-191D Low/Profile,
new transport endpoints, Objekt X and RH remain open. This package closes
the construction/transition interfaces for this named candidate only.
