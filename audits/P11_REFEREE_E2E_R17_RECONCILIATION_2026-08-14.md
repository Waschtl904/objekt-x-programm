# P11 End-to-End Referee R17 — reconciliation

Date: 2026-08-14

## Final mathematical state

R17 is paper-internal in

`papers/P11_sections/P11_O3p_Vanishing_NearNull_Core.tex`

and is included through

`papers/P11_sections/P11_O3j_Reconciliation.tex`.

Paper module creation commit:

`979a971a83cbc9e62635b41d500d226a775b9899`

Integration commit:

`13acd5481c83482ca3510478b42f89bb3511600a`

Final repaired R17 audit commit:

`87d94e61a14a2c0fb88b33f8376a5d8a8b345fa3`

## Canonical conclusions

\[
\boxed{[R17\text{-}A]\ \checkmark[M]}
\]
For every fixed admissible R1 splitting cutoff `a_*`, the terminal hub remainder has a well-defined ambient limit
\[
E_Uh_U^{\rm rem}(z_U)\to h_{\rm rem,\infty}^{(a_*)}
\quad\text{in }L^1\cap L^2,
\]
with zero integral.  The auxiliary vector depends on the chosen splitting cutoff; it is not claimed to be a cutoff-independent canonical object.  Changing `a_*` changes it only by finitely many complete primitive translation differences, which are smooth mean-zero profiles and are asymptotically absorbed by the same R17 lemma.

\[
\boxed{[R17\text{-}B]\ \checkmark[M]}
\]
Every fixed smooth compactly supported even mean-zero profile can be represented asymptotically by the future primitive/full-rest adjoint at vanishing certificate cost and vanishing source error.

\[
\boxed{[R17\text{-}C]\ \checkmark[M]}
\]
The R16 bounded TC1 core actually vanishes:
\[
\boxed{D_U(z_U,z_U)\to0.}
\]
Thus the R16 alternatives `positive bounded limit / zero / bounded oscillation` are resolved in favor of zero.

\[
\boxed{[R17\text{-}D]\ \checkmark[M]}
\]
The full graph energy on the exact near-null direction converges to the fixed Gamma floor:
\[
\boxed{q_U^X(J_{R,U}z_U)\to\mathfrak c_{\Gamma,R}[f_m]>0.}
\]
Equivalently, at fixed baseline `T_0`,
\[
\rho_{T_0,U}(z_U)
\to
\frac{\mathfrak c_{\Gamma,R}[f_m]}
{q_{T_0}^X(J_{R,T_0}f_m)}\in(0,\infty).
\]
The exponential conditioning witness from R16 remains valid.

\[
\boxed{[R17\text{-}E]\ \checkmark[M]_{\rm neg}}
\]
The proposed comparison of scalar bounded cores at source levels `R` and `S` is not a gauge diagnostic.  For a canonically nested jet pair,
\[
z_U^S=J_{R,S}z_U^R,
\]
and since `D_U` is terminal data,
\[
D_U^{(S)}(z_U^S,z_U^S)=D_U^{(R)}(z_U^R,z_U^R)
\]
identically.  Hence no scalar `R-S` difference exists on the compatible direction from which to recover the polar commutator.

\[
\boxed{[R17\text{-}F]\ ?[O]}
\]
The actual operator-valued gauge problem remains open:
\[
\Gamma_U\to I,
\qquad
K_{R,S}^{T_0,U}\to I,
\qquad
W_{R,S,-}^{[U]}\ \text{strong Cauchy}.
\]
The next viable route must retain off-diagonal/complement information and the orientation of the full positive/inverse square roots; scalar near-null Schur energies are exhausted by R17.

## CI state at reconciliation creation

The new module itself was created at commit `979a971a...`; workflow run `31813762885` completed successfully, but at that commit the new file was not yet included by the main manuscript.

The integration commit `13acd548...` triggered permanent workflow run `31813801346`.  At the final check during this audit, that run was still `in_progress` in the TeX-dependency installation step.  Therefore this reconciliation does **not** claim a completed integrated CI pass.  The mathematics above is frozen independently of that pending build status.

## Scope firewall

R17 resolves the scalar bounded Schur core and rules out the proposed scalar `R/S` gauge comparison.  It does not prove a polar-gauge limit, cross-terminal convergence, strong terminal transport, a global Object X, Seal, or RH.
