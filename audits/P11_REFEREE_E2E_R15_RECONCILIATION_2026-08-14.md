# P11 End-to-End Referee R15 — reconciliation

Date: 2026-08-14

## Final paper state

R15 is paper-internal in

`papers/P11_sections/P11_O3n_GaugeIntertwining_Criterion.tex`

and is included through

`papers/P11_sections/P11_O3j_Reconciliation.tex`.

Final paper commit containing the exact TC1 near-null reduction:

`65e743d4d33c00ab0efd42528be4e6ccbba48118`

Final R15 audit commit:

`9b04e7415fea5f95cf9832957b5dbd4913a00f94`

## Canonical conclusions

\[
\boxed{[R15\text{-}A]\ \checkmark[M]}
\]
The pure gauge compression
\[
\Gamma_U=W^*U_SWU_R^*
\]
has the exact transported-isometry criterion
\[
\Gamma_U\xrightarrow[s]{}I
\iff
U_SWU_R^*\xrightarrow[s]{}W.
\]
In operator norm this is equivalent to
\[
\|U_SW-WU_R\|\to0.
\]

\[
\boxed{[R15\text{-}B]\ \checkmark[M]}
\]
The square-root products satisfy
\[
X_SW-WX_R
=\bigl[U_S(Q-W)+(U_SW-WU_R)\bigr]A_R^{1/2}.
\]
After the canonical normalization,
\[
\mathcal E_U:=(X_SW-WX_R)A_R^{-1/2},
\]
one has
\[
\mathcal E_UU_R^*=W_{R,S,-}^{[U]}-W_{R,S,-}^{[T_0]}.
\]
Hence normalized `X` coherence is exactly the original norm transport defect, not a simpler independent gate.

\[
\boxed{[R15\text{-}C]\ \checkmark[M]}
\]
For each level `X=R,S`, the individual polar factor satisfies
\[
U_X=I
\iff
[G_{X,T_0}^-,G_{X,U}^-]=0.
\]
Thus the gauge records genuine metric noncommutativity; it is not a choice ambiguity.

\[
\boxed{[R15\text{-}D]\ \checkmark[M]_{\rm neg}}
\]
The present fixed-pair mixed-jet `1+o(1)` asymptotics do not determine inverse-square-root scale. The explicit positive model
\[
M_\varepsilon^{(a)}
=\begin{pmatrix}
1&\varepsilon\\
\varepsilon&\varepsilon^2+\varepsilon^a
\end{pmatrix},\qquad a>2,
\]
has the same rank-one entrywise leading data for every `a`, but
\[
\lambda_{\min}(M_\varepsilon^{(a)})\sim\varepsilon^a,
\qquad
\|(M_\varepsilon^{(a)})^{-1/2}\|\sim\varepsilon^{-a/2}.
\]
Thus the leading fixed-pair package is mathematically insufficient for the finite-jet inverse-square-root/gauge step.

\[
\boxed{[R15\text{-}E]\ \checkmark[M]}
\]
The exact TC1 near-null direction is explicit. For fixed smooth odd vectors `f_0,f_m` with first jet orders `0,m>0`, define
\[
z_U=f_m-\frac{\ell_U(f_m)}{\ell_U(f_0)}f_0.
\]
Then
\[
\rho_U(z_U,z_U)=0,
\qquad
\sigma_U(Jz_U,Jz_U)=D_U(z_U,z_U),
\]
and the current theory gives only
\[
D_U(z_U,z_U)=o(e^U/U^{2m+2}).
\]
No matching positive lower asymptotic or polynomial scale is presently proved.

\[
\boxed{[R15\text{-}F]\ ?[O]}
\]
The actual P11 limits
\[
\Gamma_U\to I,
\qquad
K_{R,S}^{T_0,U}\to I,
\]
and strong terminal Cauchy convergence remain open.

## Structural consequence

R15 shows that the next frontier is not merely a sharper prime-counting exponent. The known leading Gram term is rank one, so it cancels exactly on the `U`-dependent near-null jet direction `z_U`. The missing datum is the first non-rank-one positive Gram scale.

At the two-jet level the sharp next target is therefore a quantitative asymptotic or two-sided bound for
\[
D_U(z_U,z_U),
\]
including compatibility between the `R`- and `S`-level finite-jet blocks. This is the concrete first subproblem inside Open Problem `open:finite-jet-sqrt`.

## CI

The final paper commit `65e743d4d33c00ab0efd42528be4e6ccbba48118` was checked by the permanent workflow

`P11 LaTeX check`, run `31797931917`.

Result: **SUCCESS**.

The run completed both P11 LaTeX passes and the unresolved/multiply-defined reference check.

## Scope firewall

R15 is an exact reduction plus an information-insufficiency theorem for the current asymptotic package. It is not a counterexample to the actual P11 prime/Gamma metric family and gives no strong-terminal, Object-X, Seal, or RH conclusion.
