# P11 End-to-End Referee R14 — reconciliation

Date: 2026-08-14

## Final paper state

R14 is paper-internal in

`papers/P11_sections/P11_O3m_PolarGauge_Separation.tex`

and is included through

`papers/P11_sections/P11_O3j_Reconciliation.tex`.

Final strengthened paper commit:

`1f06c35f61bbc0028b957254b21408087c6f02af`

The final countermodel uses the fixed canonical coordinate inclusion
\[
J:\mathbb C\hookrightarrow\mathbb C^2,
\qquad Jz=(z,0),
\]
so the non-promotion result is not an artifact of allowing an arbitrary transition map.

## Canonical R14 conclusions

\[
\boxed{[R14\text{-}A]\ \checkmark[M]}
\]
The polar-gauge identity is exact.

\[
\boxed{[R14\text{-}B]\ \checkmark[M]}
\]
The polar factors `U_R,U_S` are unique; the word “gauge” does not denote a choice ambiguity.

\[
\boxed{[R14\text{-}C]\ \checkmark[M]}
\]
The true cross-terminal kernel admits the exact decomposition
\[
K_{R,S}^{T_0,U}
=\left[W^*U_SW(I-\mathscr K)+W^*U_S\mathscr N\right]U_R^*,
\]
and, with
\[
\Gamma_U=W^*U_SWU_R^*,
\]
\[
\|K_{R,S}^{T_0,U}-\Gamma_U\|
\le 2\|Q-W\|.
\]
Thus even hypothetical modulus convergence `Q-W -> 0` leaves a separate gauge-compression condition `Gamma_U -> I`.

\[
\boxed{[R14\text{-}D]\ \checkmark[M]_{\rm neg}}
\]
Promotion from modulus/Jensen information to actual terminal convergence is false from the current pullback/relative/polar algebra alone.  The canonical-inclusion countermodel has
\[
Q=W,\qquad \Theta=0
\]
exactly, but
\[
W^{[U]}\ne W,
\qquad
K^{T_0,U}\ne I.
\]
A fixed-baseline sequence has `Q_n=W` and `Theta_n=0` for every `n` while the actual future transports are not Cauchy.

\[
\boxed{[R14\text{-}E]\ ?[O]}
\]
The actual P11 asymptotics of the unique polar factors and of
\[
K_{R,S}^{T_0,U}
\]
remain open.  Additional concrete P11 structure may constrain the gauges in a way absent from the abstract countermodel.

## Interaction with R13

R13 proves
\[
\chi\|\Theta\|\to\infty
\]
for the actual P11 O3 diagnostic.  R14 clarifies that this kills only the auxiliary sufficient Jensen-product route.  It does **not** imply
\[
Q-W\not\to0
\]
and does not imply
\[
K_{R,S}^{T_0,U}\not\to I.
\]

## CI

The final strengthened paper commit `1f06c35f...` was checked by the permanent workflow

`P11 LaTeX check`, run `31769871893`.

Result: **SUCCESS**.

The run completed the real two-pass P11 LaTeX build and the unresolved/multiply-defined reference check.

## Scope firewall

R14 is a logical/algebraic non-promotion theorem, not a counterexample to the actual P11 prime/Gamma family.  It supplies no strong-terminal, Object-X, Seal, or RH conclusion.

The next genuine target is an actual-family gauge theorem or a direct estimate for the true cross-terminal kernel, not another Jensen-only estimate.
