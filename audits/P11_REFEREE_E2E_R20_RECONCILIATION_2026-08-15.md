# P11 End-to-End Referee R20 — reconciliation

Date: 2026-08-15

## Final paper state

R20 is paper-internal in

`papers/P11_sections/P11_O3s_Relative_Polar_Incompatibility.tex`

and included through

`papers/P11_sections/P11_O3j_Reconciliation.tex`.

Paper module commit:

`f70e45296580685112a4c11b770733e52ea49b01`

Audit commit:

`c4e6fb50f648fe5a668f870491d05b4777e25324`

Integration commit:

`76957cfb384a962849244dfdc57388394ac63b47`

## Canonical conclusions

\[
\boxed{[R20\text{-}A]\ \checkmark[M]}
\]
For one positive metric pair `(B,C)`, the scale-normalized square-root commutator gives
\[
\|U-I\|
\ge
\frac{
\|B^{-1/2}[B^{1/2},C^{1/2}]B^{-1/2}\|
}{
2\|(B^{-1/2}CB^{-1/2})^{1/2}\|
}.
\]
Thus normalized noncommutativity detects individual polar activity.

\[
\boxed{[R20\text{-}B]\ \checkmark[M]}
\]
The true relative polar defect has the exact orthogonal decomposition
\[
U_SW-WU_R
=(I-WW^*)U_SW+W(\Gamma_U-I)U_R.
\]
Hence target polar leakage is a sufficient genuine component of relative gauge failure, but individual `U_X-I` is not.

\[
\boxed{[R20\text{-}C]\ \checkmark[M]_{\rm neg}}
\]
Large raw metric-pair commutators do not algebraically force target polar leakage.

\[
\boxed{[R20\text{-}D]\ \checkmark[M]_{\rm neg}}
\]
Even nontrivial source and target polar factors produced by noncommuting metric pairs do not force a relative gauge defect: in a canonical nested direct-sum model one has
\[
U_S=U_R\oplus1,
\qquad
U_SW=WU_R
\]
exactly while the raw commutator norms can be arbitrarily large.

\[
\boxed{[R20\text{-}E]\ \checkmark[M]_{\rm neg}}
\]
Adding genuine R19-type modulus leakage does not repair this abstract implication.  A stronger canonical direct-sum model simultaneously has nonzero `(I-P)Q`, arbitrarily large square-root off-block, arbitrarily large individual metric commutators, and nevertheless
\[
(I-P)U_SW=0,
\qquad
U_SW-WU_R=0.
\]

\[
\boxed{[R20\text{-}F]\ ?[O]}
\]
The concrete P11 relative polar incompatibility remains open.  The needed object is not a pair of separate commutator estimates but a criterion that compares the source and target polar rotations across `W`.

## Structural interpretation

R19 proved that the concrete P11 future relative metric has genuine off-block information even after positive square-root functional calculus, and obtained a direct polynomial lower bound on the modulus defect `Q-W`.  R20 shows that the remaining promotion cannot be achieved by merely proving that the two base/future metric pairs are individually noncommuting, no matter how large their raw commutators are.

The correct distinction is:

- **individual polar activity:** whether `U_X` differs from the identity, quantitatively detectable by a normalized square-root commutator;
- **relative polar incompatibility:** whether `U_S W` differs from `W U_R`, which is the actual gauge obstruction.

Matched nontrivial polar rotations can cancel perfectly under the inclusion.  Therefore any successful P11 commutator route must be intrinsically relative across the nested source levels.

## CI

The integrated R20 paper commit

`76957cfb384a962849244dfdc57388394ac63b47`

was checked by the permanent workflow

`P11 LaTeX check`, run `31866988153`.

Result: **SUCCESS**.

Both P11 LaTeX passes and the unresolved/multiply-defined reference check completed successfully.

## Scope firewall

R20 does not prove a lower bound for `(I-P)U_SW` in the actual P11 family and does not prove or disprove
\[
\Gamma_U\to I,
\qquad
K_{R,S}^{T_0,U}\to I,
\qquad
W_{R,S,-}^{[U]}\text{ strong Cauchy}.
\]
No global Object X, Seal, or RH conclusion follows.
