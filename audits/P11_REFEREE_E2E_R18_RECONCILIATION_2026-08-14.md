# P11 End-to-End Referee R18 — reconciliation

Date: 2026-08-14

## Final paper state

R18 is paper-internal in

`papers/P11_sections/P11_O3q_OffDiagonal_NearNull_Block.tex`

and included through

`papers/P11_sections/P11_O3j_Reconciliation.tex`.

Audit commit:

`b209f6a355fe0e9b2cb825bfec5bb5d8cb5f367e`

Paper module commit:

`9738a172ae85be4ebdb7a01bed4b975b38e93186`

Integration commit:

`90ab1ac353a52b4419b95a2abbb5edec930239c1`

## Canonical conclusions

\[
\boxed{[R18\text{-}A]\ \checkmark[M]}
\]
The exact near-null condition `ell_U(z_U)=0` kills the complete rank-one row/column involving `z_U`:
\[
\rho_U(f_0,z_U)=0,
\qquad
\sigma_U(Jf_0,Jz_U)=D_U(f_0,z_U).
\]

\[
\boxed{[R18\text{-}B]\ \checkmark[M]}
\]
Using positivity of `D_U`, the fixed-vector estimate
\[
D_U(f_0,f_0)=o(e^U/U^2)
\]
and R17
\[
D_U(z_U,z_U)\to0,
\]
one obtains
\[
\boxed{
\sigma_U(Jf_0,Jz_U)=o(e^{U/2}/U).
}
\]
No absolute `o(1)` claim is made.

\[
\boxed{[R18\text{-}C]\ \checkmark[M]}
\]
For the full graph form,
\[
q_U^X(Jf_0)\asymp e^U/U^2,
\qquad
q_U^X(Jz_U)\to\mathfrak c_{\Gamma,R}[f_m]>0,
\]
and the mixed entry is `o(e^{U/2}/U)`. Therefore the normalized full-Gram angle tends to zero. Equivalently, the diagonally normalized two-vector correlation matrix tends to `I_2`.

\[
\boxed{[R18\text{-}D]\ \checkmark[M]}
\]
The graph cocycle preserves every terminal matrix element on a canonically nested finite source block.  For any finite family `e_i` at level `R` and `e_i^S=J_{R,S}e_i`,
\[
\langle G_{S,T}e_i^S,e_j^S\rangle_{X,S}
=
\langle G_{R,T}e_i,e_j\rangle_{X,R}
\]
for every future terminal `T`.  Hence the complete finite `(T_0,U)` Gram pair is exactly source-compatible.

\[
\boxed{[R18\text{-}E]\ \checkmark[M]_{\rm neg}}
\]
The proposed `(f_0,z_U)` off-diagonal scalar, and more generally any scalar or finite matrix quantity formed only from canonically nested source vectors, cannot carry an `R/S` polar-gauge difference.  Different jet orders do not bypass the cocycle.

\[
\boxed{[R18\text{-}F]\ ?[O]}
\]
The full polar gauge remains open because compression does not commute with positive functional calculus.  Internal finite-block matrix square roots do not determine the compression of the full operator square root.  The missing information is off-block coupling to the `T_0`-orthogonal complement.

## Structural interpretation

R15 showed that leading fixed-pair rank-one data were insufficient for inverse-square-root control.  R16 and R17 then resolved the exact smooth near-null scalar direction: the Schur remainder is bounded and in fact tends to zero, leaving a pure Gamma floor in the full metric.  R18 now shows that the corresponding mixed source-block entry is also subcritical and that the entire finite source-compatible Gram pair is cocycle-invariant between source levels.

Thus the finite source-block route is exhausted as a gauge diagnostic.  The polar-gauge obstruction is genuinely an off-block phenomenon.  A next attack must retain the splitting
\[
\operatorname{Ran}W\oplus(\operatorname{Ran}W)^\perp
\]
and study square-root or polar leakage across it, rather than more internal jet-block entries.

## CI

The integrated R18 paper commit

`90ab1ac353a52b4419b95a2abbb5edec930239c1`

was checked by the permanent workflow

`P11 LaTeX check`, run `31817848341`.

Result: **SUCCESS**.

Both P11 LaTeX passes and the unresolved/multiply-defined reference check completed successfully.

## Scope firewall

R18 does not prove `Gamma_U -> I`, `K_{R,S}^{T_0,U} -> I`, strong terminal transport, a global Object X, Seal, or RH.