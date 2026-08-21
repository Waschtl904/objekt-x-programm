# P12 End-to-End Referee — A15.1 injectivity beyond the two-shift boundary

**Date:** 2026-08-21
**Repository:** `Waschtl904/objekt-x-programm`
**Papers head at audit start:** `f88c960` (P11 frozen)
**New paper introduced:** `papers/P12_Adelic_Hub_Injectivity_Program.tex`

## Purpose and firewall

P12 opens the arithmetic chamber `2a < T_0 < c := (log 5)/2`, in which
the third shift `2a` becomes active.  This audit records the four new
injectivity theorems A15.1b0/b1/b2a/b2b and isolates the exact
remaining Sub-wedge B (`0 < R < e/2`) as `?[O]`.

No polar-gauge, terminal-transport, Object-X, or RH consequence is drawn.
The R14 firewall from P11 remains unchanged.  Even a full closure of
Sub-wedge B would decide only the localized-hub kernel triviality in the
three-shift chamber; by R36-A1 (P11) this is equivalent to dense range
of the annular hub projection `P_A H_{T_0}`, a modulus-layer statement.

## Setup verified against the P11 freeze record

- `T := 2a = log 2 ≈ 0.6931`.
- `d := b - a = (log 3 - log 2)/2 ≈ 0.2027`.
- `e := a - d = 2a - b ≈ 0.1438`.
- `δ := d - e = 2b - 3a ≈ 0.0589`.
- `p := c_{2,1} = √(log 2) · 2^{-3/4} ≈ 0.4950`.
- `r := c_{3,1} = √(log 3) · 3^{-3/4} ≈ 0.4598`.
- `q := c_{2,2} = √(log 2) · 2^{-3/2} ≈ 0.2944`.
- `p² - q² ≈ 0.1584`.
- `α := pr / (p² - q²) ≈ 1.4368`, `α² - 1 ≈ 1.0645 ≠ 0`.
- `(p/q)² = 2^{3/2} ≠ 1` (this is the A14.3a transcendence input).

## 1. A15.1b0 — pure-tail injectivity (S < T)

Statement: `S < T ⟹ ker L_{R,S,T_0}^{{a,b,2a}} = {0}`.

Verdict:
```
✓[M]
```

Verification: proof is a direct persistence of A14.3a in the pure-source
region.  The additional `2a`-shift is inactive on the E-family
`u = a + x`, `0 < x < a`:
- fold branch `g(u + 2a) = g(3a + x)` has argument `3a + x > 3a > T_0`
  (using `T_0 < c ≈ 0.8047 < 3a ≈ 1.0397`), deleted by `P_{T_0}`;
- forward branch `g(u - 2a) = g(x - a) = -g(a - x)` (oddness) is
  absorbed into the existing `q`-reflection term of A14.3a.
The A14.3a apparatus applies verbatim.

## 2. A15.1b1 — horizon-open S = T endpoint

Statement: `T < T_0 < c, 0 < R < T, S = T ⟹ ker L = {0}`.

Verdict:
```
✓[M]
```

Structural check of the four proof steps:

- **Step 1 (lower-half kill):** the repaired A14.3a lower-circle argument
  gives `h = 0` on `(R, a)`.  The support hypothesis `S = T` makes the
  fold branch `g(2a + x) = 0` on `x > 0`, exactly as A14.3a expects.
- **Step 2 (H-source):** for `u = T + t`, `0 < t < ε`, the equation
  `q h(t) + r h(e + t) + p h(a + t) = 0` reduces to `p h(a + t) = 0`
  because `t < ε < e < a` places `t` and `e + t` in the killed region
  `(R, a)` (or outside support if `t < R`).  So `h = 0` on
  `(a, a + ε)`.  Structural check `✓[M]`.
- **Step 3 (high reflection transport):** with `l(z) := h(T - z)`, the
  new gap is `l(z) = 0` on `(a - ε, a)`.  The A14.3a identity
  `q l(z) + p l(a - z) = 0` is proved on `d < z < a`; the gap lies in
  that region because `a - ε > d ⇔ ε < e ⇔ T_0 < T + e = 2a + a - d
  = 3a - d`, and `3a - d ≈ 0.8412 > c ≈ 0.8047`, so `T_0 < c < 3a - d`.
  ✓.  Transport delivers `l(w) = 0` on `(0, ε)`.
- **Step 4 (UC2):** open seed on `(0, ε) ⊂ (0, e)` in the first
  component of the upper-circle vector `W(t)`.  UC2 return-count from
  A14.3a UC-repair (2026-08-21) applies to the same cocycle.  Delivers
  `W = 0`.

The claimed structural novelty — old support gap `(0, T-S)` replaced by
horizon-generated gap `(a, a + ε)` transported by the A14.3a high
reflection — is genuine and non-trivial.

Boundary scope note: the exact corner `T_0 = T = S` remains `?[O]`
(the proof uses `ε > 0` essentially).

## 3. A15.1b2a — mixed strip R ≥ e

Statement: `T < T_0 < c, e ≤ R < T, T < S < T_0 ⟹ ker L = {0}`.

Verdict:
```
✓[M]
```

Structural check:
- Step 1: `d < x < a` ⟹ auxiliary values `x - d`, `a - x` both in
  `(0, e) ⊆ (0, R)` ⟹ killed.  ✓
- Step 2: `R < x < d` ⟹ `h(d - x) = 0` (since `d - x < d - R ≤ δ < e
  ≤ R`); pair equations (E, E-at-`a-x`) give `(p² - q²) h(x) = 0`;
  `p² ≠ q²`.  ✓
- Step 3 (upper half): A14.3a upper source `u = 3a - t` etc. applies with
  same mechanism.
- Step 4 (tail): `H(t) = 0` because all three auxiliary values lie in
  the just-killed `(0, a)`.

Numerical cross-check performed at `R ∈ {0.144, 0.20, 0.30}`, `S = 0.5`,
`T_0 = 0.78`, `N = 200`: `σ_min ∈ [8.6e-2, 1.3e-1]`, mesh-stable.

## 4. A15.1b2b — mixed strip Sub-wedge A (e/2 ≤ R < e)

Statement: `T < T_0 < c, e/2 ≤ R < e, T < S < T_0 ⟹ ker L = {0}`.

Verdict:
```
✓[M]
```

**This is the new theorem introduced by P12.**  It uses the H-source
`u = 2a + x` for the first time in the injectivity proof.

Structural check of the six proof steps:

- **H-source identity (H\_R):** for `0 < x < min(R, ε)`, the H-source
  gives `p h(a + x) + r h(e + x) = 0`.  This is the new source input.
  Substituting `y = e + x` gives `h(y + d) = -(r/p) h(y)` on
  `(e, e + min(R, ε))`.  ✓
- **Step 1 (near a, `a - R < x < a`):** `a - x < R`, so `h(a - x) = 0`;
  `x > d` (since `a - R > d ⇔ R < e`, our regime); E-eqn gives
  `p h(x) + r h(x - d) = 0` on `(a - R, a)`.  ✓
- **Step 2 (middle `d < x < a - R`):** `x - d < a - R - d = e - R ≤ R`
  (Sub-wedge A: `e - R ≤ e/2 ≤ R`), so `h(x - d) = 0`; E-eqn gives
  `h(x) = (q/p) h(a - x)`, with `a - x ∈ (R, e)`.  Setting `y = a - x`
  yields (5$'$): `h(a - y) = (q/p) h(y)` on `y ∈ (R, e)`.  ✓
- **Step 3 (core wedge `R < x < e`):** substitute (5$'$) into E-eqn:
  `(p² - q²) h(x) = pr h(d - x)`, `h(x) = α h(d - x)`.  Then
  (i) if `d - x < R` (i.e. `x > d - R`): direct kill; else
  (ii) iterate: `h(d - x) = α h(x)`, so `α² h(x) = h(x)`, and
  `α² ≠ 1` ⟹ `h(x) = 0`.  ✓
- **Step 4 (strip `e < x < d`):** `d - x < δ < R`, so `h(d-x) = 0`;
  and `a - x ∈ (e, d)` itself; `(p² - q²)` kill.  ✓
- **Step 5 (upper interior `d < x < a - R`):** from (5) with `h = 0`
  on `(R, e)`.  ✓
- **Step 6 (upper half and tail):** upper half by A14.3a upper source;
  tail via `H(t) = 0` reduction.

**Adversarial checks:**
- Numerical: `σ_min ∈ [8.6e-2, 1.3e-1]` for `R ∈ {0.08, 0.10, 0.12, 0.14}`,
  `S = 0.75`, `T_0 = 0.78`, `N = 200`, mesh-stable.  Consistent.
- Sub-wedge B breaking point: (5) requires `e - R ≤ R`, which is
  exactly Sub-wedge A ⇔ `R ≥ e/2`.  Sub-wedge B has `e - R > R`, and
  the reduction to a single reflection $h(x) = \alpha h(d-x)$ fails
  there.  This is the exact `?[O]` handoff point.
- Transcendence: `α² = 1` would require an algebraic relation between
  `log 2` and `log 3` beyond those excluded by Gelfond–Schneider.
  Numerically `α² - 1 ≈ 1.065`.  Since `α² = (pr)² / (p² - q²)²` with
  `p, q, r` all products of `√(log 2)` or `√(log 3)` and rational
  powers of `2` or `3`, `α² - 1 = 0` reduces to an explicit polynomial
  identity in `log 2` and `log 3`; by Gelfond–Schneider `log 2 / log 3`
  is transcendental, so any such polynomial identity is false.
  Structural check `✓[M]`.

## 5. Open Sub-wedge B

Statement: for `2a < T_0 < c`, `0 < R < e/2`, `T < S < T_0`:
decide whether `ker L = {0}`.

Verdict:
```
?[O]
```

Numerical evidence: `σ_min ∈ [6.6e-2, 9.5e-2]` for `R ∈ {0.02, 0.04,
0.06, 0.07}`, `S = 0.75`, `T_0 = 0.78`, `N = 200`, mesh-stable.
Consistent with kernel triviality, but not a proof.  Matches the
independent numerical prediction of council-member Claude Opus 5
(report `model-council-claude_opus_5_0.md`, §0.4).

## 6. Consolidated status after P12

| Item | Verdict |
|---|---|
| A15.1b0 pure-tail injectivity (S < T) | ✓[M] |
| A15.1b1 horizon-open S = T endpoint | ✓[M] |
| A15.1b2a mixed strip R ≥ e | ✓[M] |
| A15.1b2b mixed strip Sub-wedge A (e/2 ≤ R < e) | ✓[M] |
| A15.1 remaining core Sub-wedge B (0 < R < e/2) | ?[O] |
| Exact corner T_0 = T = S | ?[O] |
| Chamber wall T_0 = c (activation of shift log(5)/2) | ?[O] |

Consolidated: for `2a < T_0 < c`, `0 < R < S < T_0`, injectivity holds
on the disjoint union
```
{S < T} ∪ {S = T} ∪ {R ≥ e, T < S < T_0} ∪ {e/2 ≤ R < e, T < S < T_0}
```
with the complement in `{0 < R < S < T_0, R < T}` being exactly
`{0 < R < e/2, T < S < T_0} ∪ {T_0 = T = S}`.

## 7. Consequences (booked adversarially)

- The old R36-B annihilator route for R30-F is further eroded in the
  three-shift chamber: every A15.1 injectivity theorem removes candidate
  witnesses from the localized-hub kernel.  Sub-wedge B is now the only
  remaining candidate cell for a nontrivial R36-B witness in the
  three-shift regime.
- Scenario II ("immediate new kernel reentry above `T_0 = 2a`") is
  refuted in three of four strata, and numerically excluded in the
  fourth.
- Scenario III ("new phase boundary immediately above `T_0 = 2a`") is
  refuted in the same three strata.
- Scenario I ("right-stability of A14.3a-boundary injectivity through
  the full three-shift chamber") is confirmed except in Sub-wedge B.
- **None of the above crosses the R14 firewall.**  All statements are
  modulus-layer.  No polar-gauge, terminal-transport, Object-X or RH
  claim follows.
