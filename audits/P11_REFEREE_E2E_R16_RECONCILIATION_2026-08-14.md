# P11 End-to-End Referee R16 — reconciliation

Date: 2026-08-14

## Final paper state

R16 is paper-internal in

`papers/P11_sections/P11_O3o_TC1_NearNull_Remainder_Collapse.tex`

and included through

`papers/P11_sections/P11_O3j_Reconciliation.tex`.

Paper module creation commit:

`aebfdd4e1d75bda8fb5734ad9d1b88009b94f018`

Integration commit:

`7a4ba5d5e9e29a80088872f906d021529ee93f22`

R16 audit commit:

`b1397c79bc7783e088559d285b32845292a877a0`

## Canonical conclusions

\[
\boxed{[R16\text{-}A]\ \checkmark[M]}
\]
The full Theorem 6.1 signed future-edge/full-rest dual certificate can be uniformized on the bounded family
\[
z_U=f_m-\frac{\ell_U(f_m)}{\ell_U(f_0)}f_0
\]
inside the fixed two-dimensional smooth odd space `span{f_0,f_m}`.

\[
\boxed{[R16\text{-}B]\ \checkmark[M]}
\]
Exact constant-mode cancellation `ell_U(z_U)=0` forces
\[
D_U(z_U,z_U)=\sigma_U(Jz_U,Jz_U)=O(1).
\]

\[
\boxed{[R16\text{-}C]\ \checkmark[M]_{\rm neg}}
\]
Every exponential-times-polynomial lower scale for the TC1 near-null remainder is false. For every fixed `N>0`,
\[
D_U(z_U,z_U)=o(e^U/U^N).
\]
In particular there are no fixed `c>0`, `alpha>0` with
\[
D_U(z_U,z_U)\ge c\,e^U/U^{2m+2+\alpha}
\]
for all sufficiently large `U`.

\[
\boxed{[R16\text{-}D]\ \checkmark[M]}
\]
The full P11 graph metric does not collapse on this direction. Gamma compatibility and `C_{Gamma,R}>=I` give
\[
q_U^X(Jz_U)=\mathfrak c_{\Gamma,R}[z_U]+D_U(z_U,z_U)\asymp1.
\]
Thus the bounded near-null Schur scale sits on top of a fixed positive archimedean floor.

\[
\boxed{[R16\text{-}E]\ \checkmark[M]}
\]
The same exact near-null direction upgrades R7 to an exponential conditioning witness:
\[
\boxed{\kappa(A_{T_0,U}^{R,-})\ge c\,e^U/U^2.}
\]
The old statement `U^{-N} kappa -> infinity for every N` remains true but is substantially weaker.

\[
\boxed{[R16\text{-}F]\ ?[O]}
\]
The bounded-scale asymptotic of `D_U(z_U,z_U)` remains unknown: convergence to a positive constant, decay to zero, or bounded oscillation are not distinguished.

\[
\boxed{[R16\text{-}G]\ ?[O]}
\]
No gauge or cross-terminal convergence follows. In particular
\[
\Gamma_U\to I,
\qquad
K_{R,S}^{T_0,U}\to I,
\qquad
W_{R,S,-}^{[U]}\ \text{strong Cauchy}
\]
remain open.

## Structural interpretation

R15 identified `D_U(z_U,z_U)` as the first positive quantity left after exact rank-one cancellation. R16 shows that this remainder is not a smaller exponential jet term at all: the entire future exponential scale can be absorbed by the signed future-edge/full-rest certificate once the exact constant mode is cancelled.

The remaining Schur energy is bounded. Consequently, after normalization by the leading `e^U` scale, the small finite-jet directions live beyond every polynomial order. The fixed Gamma form is then of the same absolute order as the surviving Schur core and cannot be dropped from any square-root analysis.

This changes the next frontier. The immediate problem is no longer to find an exponent `alpha` in a polynomial correction. It is to identify the **bounded core operator** after certificate removal and compare it between source levels `R` and `S`.

## CI

The integrated R16 paper commit

`7a4ba5d5e9e29a80088872f906d021529ee93f22`

was checked by the permanent workflow

`P11 LaTeX check`, run `31812206124`.

Result: **SUCCESS**.

Both P11 LaTeX passes and the unresolved/multiply-defined reference check completed successfully.

## Scope firewall

R16 is an absolute-scale refinement of the finite-jet/conditioning analysis. It does not prove a bounded-core limit, a polar-gauge limit, strong terminal transport, a global Object X, Seal, or RH.