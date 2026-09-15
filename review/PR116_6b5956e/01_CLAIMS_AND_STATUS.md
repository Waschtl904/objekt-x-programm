# PR #116 — Claims and status ledger

Frozen source head for every frozen-source row unless stated otherwise:

`6b5956e69dfcb8124e8e31083613fd89c5f35fb3`

Immutable review base:

`freeze/pr116-6b5956e`

Status vocabulary:

- `✓[M]` — theorem-level mathematical claim on the stated scope;
- `✓[M]_part` — meaningful partial implementation/reduction, but the advertised terminal certificate is not closed;
- `?[O]` — open / not established here;
- `corrected` — frozen wording was too strong, with a later exact correction recorded below.

| ID | Claim | Status | Exact source | Dependencies / firewall |
|---|---|---|---|---|
| C01 | `D_NP,a = L_{1/2} C_c^∞(-a,a)` with `L_{1/2}=-∂_x^2+1/4` | `✓[M]` | `audits/P11_CRITICAL_HALF_GREEN_TREE_BRIDGE_2026-09-13.md`, §2 | Compact smooth test class. The two Mellin-null conditions kill the two exponential Green tails. |
| C02 | Whole-line Green kernel of `L_{1/2}` is `e^{-|x-y|/2}` | `✓[M]` | same, §1 | Distributional identity on `R`. |
| C03 | Sampling on one prime ray gives `p^{-|j-k|/2}`; explicit star-tree features reproduce the windowless P11 prime-index Gram ledger including cross-prime hub terms | `✓[M]` | same, §§3–6 | **Ledger only.** Does not identify the full spatial/windowed P11 operator with the tree Gram. |
| C04 | Gamma ladder has `μ_m=2m+1/2`; `μ_0=1/2` gives the same base resolvent | `✓[M]` | Green/tree + harmonic bridge audits | Structural identity, not by itself positivity. |
| C05 | Direct pointwise scattering multiplier positivity fails: `τ_a(0)<0` and `τ_a(z)` becomes positive for large `|z|` | `✓[M]` | `audits/P11_SCATTERING_POINTWISE_POSITIVITY_NOGO_2026-09-13.md` | Narrow no-go against pointwise Gram factorization of the multiplier. |
| C06 | NULLPOL in `PW_a` is `F(±i/2)=0`; reproducing kernel is exact rank-2 shorting `K_NP=K-k*G^{-1}k`, `G=(1/π)[[sinh a,a],[a,sinh a]]` | `✓[M]` | `audits/P11_NP_GAP_PROLATE_COMPRESSION_2026-09-13.md`, §4 | Do not promote `(z²+1/4)PW_a` to an unrestricted closed-space equality without an operator domain. |
| C07 | Compressed negative multiplier block is positive trace class with exact trace `∫τ_{a,-}(z)K_NP,a(z,z)dz` | `✓[M]` | same, §5 | Compact negative-frequency support plus locally bounded diagonal kernel. |
| C08 | Trace-minus-Ritz: `λ1(D) ≤ tr D - Σ_{j=2}^m θ_j` for positive trace-class `D` | `✓[M]` | `audits/P11_NP_PROLATE_TRACE_RITZ_CERTIFICATE_2026-09-13.md`, §2 | Min-max + positivity + trace class. |
| C09 | Parity splits rank-2 NULLPOL shorting into one rank-1 constraint in each even/odd sector | `✓[M]` | same, §3 | Positive-half-line doubled-kernel normalization was independently checked; no factor-2 defect found. |
| C10 | Frozen `check_np_prolate_1_arb.py` implements the intended rigorous route | `✓[M]_part` | checker blob `b73ab9858cbc19626fb19794ab4ce4a0a7d3dbd8` | Static inequality directions check out. Exact run #3 reached `verify_partition` in both sectors but stopped before trace/Ritz because root brackets were too narrow. |
| C11 | `NP-PROLATE-1`, `a=1/2`, even sector certified PASS | `?[O]` | workflow/checker | First rigorous run failed at the root-partition enclosure, not at the final spectral inequality. Separate certificate-repair PR #126 is experimental and does not alter this frozen status. |
| C12 | `NP-PROLATE-1`, `a=1/2`, odd sector certified PASS | `?[O]` | workflow/checker | Same. |
| C13 | Frozen orbit-chain formula `N=floor(L/t)+1` is exact for every `t` | `corrected` | frozen prolate audit; correction at post-snapshot commit `524bc5f...` | Exact essential maximum for an open interval is `N=ceil(L/t)`. Frozen lower-frame bound remains conservative at integer `L/t`, but the old exactness claim is false there. |
| C14 | Critical-half Schur bound `⟨v,D²(D²+μ²)^{-1}v⟩ ≥ e^{-μa}||v||²` for support in `[-a,a]` | `✓[M]` | `audits/P11_CRITICAL_HALF_RIGIDITY_AND_SCHUR_GAP_2026-09-13.md`, §§6–7 | Direct Schur test on the full-line resolvent. |
| C15 | Strict local NP-GAP from the Critical-half Gamma ladder for every `0<a≤1/16` | `✓[M]` | same, §8 | No prime atom is active because `2a<log2`; elementary comparison `S(1/16)>κ_*`. Not a novelty/record claim. |
| C16 | Absolute-envelope treatment of the large-window prime comb has a sufficient tail cutoff of doubly-exponential scale `exp((4+o(1))e^a)` | `✓[M]` (method-specific) | post-snapshot hard audit `524bc5f...`, with review correction | This is a sufficient cutoff for the crude absolute envelope `|P_a|≤A_a`. |
| C17 | The actual last negative frequency, or every possible pointwise method, necessarily has that doubly-exponential scale | `?[O]` | — | Qualitative Kronecker recurrence does not provide the quantitative recurrence time needed for such a lower barrier. |
| C18 | Fixed-window `a=1/2` positivity implies all-window NP-GAP / Object X / RH | `?[O]` / **not claimed** | — | No such implication. |
| C19 | Publication novelty of the Critical-half synthesis | `?[O]` | — | Prolate/time-band limiting, Paley-Wiener windows, ±1/2 moment conditions and compression methods have substantial prior art. Any novelty must be narrower. |

## Exact CI evidence now available

Workflow run #3 (`34924681973`) executed the frozen checker blob under Python 3.13.15 with `python-flint==0.9.0`.

Both sectors stopped in `verify_partition()` before any trace/Ritz/Cholesky/final-gap calculation:

- even: unresolved sign interval immediately outside the first diagnostic root bracket near `13.25888014...`;
- odd: unresolved sign interval immediately outside the first diagnostic root bracket near `12.50398955...`.

Thus the first execution is evidence of a **root-enclosure defect in the certificate data**, not a mathematical failure of the trace-minus-Ritz inequality and not a certified NP-PROLATE PASS.

## Post-snapshot hard-audit evidence

The live PR #116 branch later advanced to `524bc5f08b822eeae751196eb9f8acb989bd1122`. That commit is **not part of the frozen source**, but its destructive audit is relevant evidence:

- Range/Green, sampled OU/tree, rank-2 shorting and trace-minus-Ritz survive;
- orbit-chain exactness is corrected as in C13;
- the parity factor-2 suspicion is withdrawn;
- weighted prolate is strategically demoted to a fixed-window regression gate;
- the claimed intrinsic doubly-exponential barrier must itself be weakened to the envelope-method statement C16 unless a quantitative recurrence lower bound is supplied.

## Domain firewall

Use separately:

```math
\mathscr D_{NP,a}=L_{1/2}C_c^\infty(-a,a)
```

and

```math
\mathcal N_a=\{F\in PW_a:F(i/2)=F(-i/2)=0\}.
```

Any multiplication statement involving `z²+1/4` on `PW_a` must declare the domain needed to remain in `L²(R)`.

## P11 firewall

The exact tree theorem concerns the **fensterlose Kanalindex-Ledger**. It does not remove window projections or prove equality with the complete spatial P11 operator geometry.

## Numerical firewall

Floating/Nyström diagnostics are not theorem data. A terminal `NP-PROLATE-1` promotion requires a fully rigorous run whose root partition, trace, Gram, Ritz/Cholesky and strict final interval gap all pass and whose exact proof inputs are retained.