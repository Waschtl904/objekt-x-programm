# PR #116 — Claims and status ledger

Frozen source head for every row unless stated otherwise:

`6b5956e69dfcb8124e8e31083613fd89c5f35fb3`

Status vocabulary:

- `✓[M]` — theorem-level mathematical claim on the stated scope;
- `✓[M]_part` — mathematically meaningful partial implementation/reduction, but the advertised terminal certificate has not yet been independently closed;
- `?[O]` — open / not established here.

| ID | Claim | Status | Exact source | Dependencies / firewall |
|---|---|---|---|---|
| C01 | `D_NP,a = L_{1/2} C_c^∞(-a,a)` with `L_{1/2}=-∂_x^2+1/4` | `✓[M]` | `audits/P11_CRITICAL_HALF_GREEN_TREE_BRIDGE_2026-09-13.md`, §2 | Compact smooth test class. Uses the two Mellin-null conditions to kill the two exponential Green tails. |
| C02 | Whole-line Green kernel of `L_{1/2}` is `e^{-|x-y|/2}` | `✓[M]` | same, §1 | Distributional identity on `R`. |
| C03 | Sampling on one prime ray gives `p^{-|j-k|/2}`; explicit star-tree features reproduce the windowless P11 prime-index Gram ledger including cross-prime hub terms | `✓[M]` | same, §§3–6 | **Ledger only.** Does not identify the full spatial/windowed P11 operator with the tree Gram. |
| C04 | Gamma ground ladder begins at `μ_m=2m+1/2`; `μ_0=1/2` gives the same base resolvent kernel | `✓[M]` | `audits/P11_PRIME_AR1_POISSON_GAMMA_HARMONIC_BRIDGE_2026-09-13.md` and bridge audit | Structural identity, not by itself a positivity theorem. |
| C05 | Direct pointwise scattering multiplier positivity fails: `τ_a(0)<0`, while the archimedean term grows logarithmically and finite prime sums remain bounded, so `τ_a` changes sign | `✓[M]` | `audits/P11_SCATTERING_POINTWISE_POSITIVITY_NOGO_2026-09-13.md` | Narrow no-go against a pointwise Gram factorization of the multiplier. |
| C06 | NULLPOL in `PW_a` is the codimension-2 subspace `F(±i/2)=0`; its reproducing kernel is the exact rank-2 shorting `K_NP=K-k*G^{-1}k` with `G=(1/π)[[sinh a,a],[a,sinh a]]` | `✓[M]` | `audits/P11_NP_GAP_PROLATE_COMPRESSION_2026-09-13.md`, §4 | Do not upgrade `(z²+1/4)PW_a` to an unrestricted closed-space equality without declaring the multiplication domain. |
| C07 | The compressed negative multiplier block is positive trace class with exact trace `∫ τ_{a,-}(z)K_NP,a(z,z) dz` | `✓[M]` | same, §5 | Compact negative-frequency support plus locally bounded diagonal kernel. |
| C08 | Trace-minus-Ritz certificate: `λ1(D) ≤ tr D - Σ_{j=2}^m θ_j` for positive trace-class `D` | `✓[M]` | `audits/P11_NP_PROLATE_TRACE_RITZ_CERTIFICATE_2026-09-13.md`, §2 | Min-max + positivity + trace class. No Galerkin convergence theorem needed for this inequality. |
| C09 | Parity splits the rank-2 NULLPOL shorting into one rank-1 constraint in each even/odd sector | `✓[M]` | same, §3 | Audit factor-of-2 conventions carefully. |
| C10 | `check_np_prolate_1_arb.py` implements a rigorous interval route using sign partition, root-bracket trace booking, certified Gram/Cholesky, and `D_inner ≤ D` logic | `✓[M]_part` | `scripts/check_np_prolate_1_arb.py` | Code-path correctness still requires exact-head execution and log audit. Presence of code is not a PASS. |
| C11 | `NP-PROLATE-1`, `a=1/2`, even sector certified PASS | `?[O]` | workflow + checker | Not promoted until an exact-head workflow/job log exists and is checked. |
| C12 | `NP-PROLATE-1`, `a=1/2`, odd sector certified PASS | `?[O]` | workflow + checker | Same. |
| C13 | Fixed-window `a=1/2` positivity implies all-window NP-GAP | `?[O]` / **not claimed** | — | No such implication is established. |
| C14 | PR #116 proves Object X or RH | `?[O]` / **not claimed** | — | Explicit firewall. |
| C15 | Publication novelty of the Critical-half synthesis | `?[O]` | — | Prolate/shorting/scattering/local-L-factor/operator themes have substantial prior art. Novelty must be formulated narrowly and independently researched. |

## Domain firewall

The review uses these two statements separately:

```math
\mathscr D_{NP,a}=L_{1/2}C_c^\infty(-a,a)
```

and

```math
\mathcal N_a=\{F\in PW_a:F(i/2)=F(-i/2)=0\}.
```

Any statement involving multiplication by `z^2+1/4` on `PW_a` must declare the operator domain needed to retain `L^2(R)`.

## P11 firewall

The exact tree theorem concerns the **fensterlose Kanalindex-Ledger**. It does not silently remove window projections or prove equality with the complete spatial P11 operator geometry.

## Numerical firewall

Floating/Nyström values in the source audits are diagnostic only. The only acceptable promotion path for `NP-PROLATE-1` is an independently inspectable rigorous execution of the frozen checker or an equivalent proof certificate.