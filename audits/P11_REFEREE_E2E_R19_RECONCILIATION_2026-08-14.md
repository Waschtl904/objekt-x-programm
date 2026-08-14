# P11 End-to-End Referee R19 — reconciliation

Date: 2026-08-14

## Final paper state

R19 is paper-internal in

`papers/P11_sections/P11_O3r_SquareRoot_OffBlock_Witness.tex`

and included through

`papers/P11_sections/P11_O3j_Reconciliation.tex`.

Paper module commit:

`a32bd3e278f0d232d845d3e9a69e4ec9b7eccd6b`

Audit commit:

`b205d31ba6b055dccdebbb3c55ae3b32c368659a`

Integration commit:

`1f9ed759fc0ca436e2879db5729dc82d0735d093`

## Canonical conclusions

\[
\boxed{[R19\text{-}A]\ \checkmark[M]}
\]
With
\[
\mathscr B_U=(I-P)A_SW,
\qquad
\mathscr C_U=(I-P)A_S^{1/2}W,
\]
there is an exact block factorization
\[
\mathscr B_U=\mathscr C_UD_U+E_U\mathscr C_U,
\]
where
\[
D_U=W^*A_S^{1/2}W,
\qquad
E_U=(I-P)A_S^{1/2}(I-P)|_{\operatorname{Ran}W^\perp}.
\]
Hence
\[
\|\mathscr C_U\|
\ge
\frac{\|\mathscr B_U\|}
{\sqrt{\|A_R\|}+\sqrt{\|A_S\|}}.
\]

\[
\boxed{[R19\text{-}B]\ \checkmark[M]}
\]
Using R13's explicit complement witness and the relative-metric norm upper bound,
\[
\boxed{
\|\mathscr C_U\|
\gtrsim
\frac{e^{U/2}}{U^{m_h+3/2}}.
}
\]
Thus the square-root off-block diverges in operator norm.

\[
\boxed{[R19\text{-}C]\ \checkmark[M]}
\]
For the modulus leakage
\[
\mathscr N_U=(I-P)Q,
\qquad
Q=A_S^{1/2}WA_R^{-1/2},
\]
one has exactly
\[
\mathscr C_U=\mathscr N_UA_R^{1/2}
\]
and therefore
\[
\boxed{\|\mathscr N_U\|\gtrsim U^{-m_h-1}.}
\]

\[
\boxed{[R19\text{-}D]\ \checkmark[M]}
\]
Since
\[
Q-W=-W\mathscr K+\mathscr N_U
\]
is an orthogonal range decomposition,
\[
\boxed{\|Q-W\|\gtrsim U^{-m_h-1}.}
\]
This is a direct lower bound on the modulus-isometry defect itself.  It does not rule out `Q -> W`; it rules out norm convergence faster than the displayed polynomial scale.

\[
\boxed{[R19\text{-}E]\ \checkmark[M]_{\rm neg}}
\]
There is no abstract implication from large second-moment or square-root leakage to polar leakage `(I-P)U_SW`.  The canonical inclusion model
\[
W:\mathbb C\hookrightarrow\mathbb C^2,
\qquad
Wz=(z,0),
\]
with identity base metrics and future metric
\[
t^2\begin{pmatrix}2&1\\1&2\end{pmatrix}
\]
has arbitrarily large `B_U` and `C_U` while the polar factor satisfies `U_S=I` and hence `(I-P)U_SW=0` identically.

\[
\boxed{[R19\text{-}F]\ ?[O]}
\]
The concrete P11 polar-gauge problem remains open.  In particular no conclusion follows about
\[
\Gamma_U\to I,
\qquad
K_{R,S}^{T_0,U}\to I,
\qquad
W_{R,S,-}^{[U]}\text{ strong Cauchy}.
\]

## Structural interpretation

R18 forced the unresolved transport information out of every finite source-compatible Gram block and into the off-block coupling before functional calculus.  R19 now proves that this off-block survives the positive square root: the actual P11 square-root off-block diverges, and after canonical source normalization it produces a polynomially nontrivial modulus leakage.

Thus the remaining frontier is no longer whether the square root erases the complement coupling. It does not. The unresolved step is specifically the polar reorientation of that modulus leakage by the concrete P11 metric pairs.  Abstract compression algebra cannot perform this promotion.

## CI

The integrated R19 paper commit

`1f9ed759fc0ca436e2879db5729dc82d0735d093`

was checked by the permanent workflow

`P11 LaTeX check`, run `31826771081`.

Result: **SUCCESS**.

Both P11 LaTeX passes and the unresolved/multiply-defined reference check completed successfully.

## Scope firewall

R19 is a square-root/modulus result, not a polar-gauge theorem.  It does not prove nonconvergence of `Q`, does not give a lower bound for `(I-P)U_SW`, and does not prove strong terminal transport, a global Object X, Seal, or RH.