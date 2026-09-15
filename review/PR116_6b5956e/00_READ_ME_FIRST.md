# PR #116 — READ ME FIRST

**Frozen research snapshot:** `6b5956e69dfcb8124e8e31083613fd89c5f35fb3`  
**Source PR:** #116 — `CRITICAL-HALF: Green/tree/scattering bridge and shorted NP prolate front`  
**Review branch:** this package only; source theorem files are not edited here.

## What this package is for

This is an adversarial review surface for the exact PR #116 snapshot above. It does **not** promote the branch, merge it, rebase it, or restate its proofs as a second source of truth.

The core question is narrow:

> Which claims at `6b5956e…` are exact theorem-level consequences, which are only partial reductions or computational implementations, and which remain open?

## Five-minute mathematical map

The safest theorem-level starting point is the compact-window range identity

```math
\mathscr D_{NP,a}
=
L_{1/2}C_c^\infty(-a,a),
\qquad
L_{1/2}=-\partial_x^2+\frac14.
```

Its whole-line Green kernel is

```math
L_{1/2}^{-1}(x,y)=e^{-|x-y|/2}.
```

On prime-power nodes `k log p`, the same kernel samples to

```math
e^{-\frac12|j-k|\log p}=p^{-|j-k|/2}.
```

The source audit constructs an explicit OU/star-tree Gram model reproducing the **windowless P11 prime-index ledger**, including cross-prime hub terms. This is a ledger statement; it is **not** permission to erase the spatial/windowed P11 operator geometry.

For the finite-window NULLPOL problem, define

```math
\mathcal N_a
=
\{F\in PW_a:F(i/2)=F(-i/2)=0\}.
```

The domain-safe statement used in this review is the definition above together with the smooth-test-class range identity. We do **not** use the shorthand

```math
\mathcal N_a=(z^2+1/4)PW_a
```

as an unrestricted Hilbert-space equality without an explicit multiplication-operator domain.

The two evaluation constraints give an exact rank-2 shorting of the Paley–Wiener reproducing kernel. The negative part of the centered multiplier is compactly supported after compression and yields a positive trace-class defect.

The trace-minus-Ritz lemma is exact:

```math
\lambda_1(D)
\le
\operatorname{tr}D-
\sum_{j=2}^{m}\theta_j,
```

for a positive trace-class `D` and Ritz values `theta_j` of any finite compression.

## What is **not** established by this package

- no all-window NP-GAP theorem;
- no RH theorem;
- no Object-X completion;
- no Registry promotion;
- no theorem-level use of floating/Nyström diagnostics;
- no publication-novelty claim;
- no promotion of `NP-PROLATE-1 / a=1/2` until an exact-head Arb run and its logs are independently checked.

## Arb gate

The frozen snapshot already contains:

- `.github/workflows/np-prolate-1-arb.yml`;
- `scripts/check_np_prolate_1_arb.py`.

The checker uses Arb interval arithmetic, explicit root-bracket error booking, certified Gram/Cholesky steps, and a trace-minus-Ritz/upper-Ritz chain. The implementation is therefore a serious theorem-certificate candidate, but **implementation present** is not the same as **certificate run audited**.

At the time this review branch was created, PR #116 itself had no workflow run recorded on exact head `6b5956e…`. PR #125 was opened with its head initially pointing exactly to that SHA in order to trigger the existing pull-request workflow before adding these review documents.

See `04_REPRODUCE.md` for the exact status and reproduction commands.

## How to review

1. Start at `01_CLAIMS_AND_STATUS.md`.
2. Follow only the exact-source permalinks in `02_CORE_PROOFS.md`.
3. Try to break the claims listed in `03_ATTACK_THIS.md`.
4. Treat `04_REPRODUCE.md` as the sole computational entrypoint.

If a claim survives, keep it. If it fails, downgrade it. No narrative is protected.