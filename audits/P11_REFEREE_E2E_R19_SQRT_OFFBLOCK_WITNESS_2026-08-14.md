# P11 End-to-End Referee R19 — square-root off-block witness

Date: 2026-08-14

## Target

Pass from the already proved second-moment off-block
\[
\mathscr B_U=(I-WW^*)A_SW
\]
through the positive square root and determine what follows for
\[
\mathscr C_U=(I-WW^*)A_S^{1/2}W,
\]
the modulus leakage `(I-WW*)Q`, and the polar leakage `(I-WW*)U_SW`.

## Verdict

The passage through the square root is positive at the modulus level and negative at the polar-promotion level.

The block identity already implicit in the proof of the O3f second-moment estimate gives
\[
\mathscr B_U=\mathscr C_UD_U+E_U\mathscr C_U,
\]
with
\[
\|D_U\|\le\sqrt{\|A_R\|},\qquad
\|E_U\|\le\sqrt{\|A_S\|}.
\]
Hence R13's lower bound for `B_U`, together with the crude relative-metric norm upper bound, yields
\[
\boxed{
\|\mathscr C_U\|\gtrsim \frac{e^{U/2}}{U^{m_h+3/2}}.
}
\]
Thus the square-root off-block diverges.

Since
\[
\mathscr N_U:=(I-WW^*)Q,
\qquad
\mathscr C_U=\mathscr N_UA_R^{1/2},
\]
one obtains the first direct lower bound on the actual modulus leakage,
\[
\boxed{\|\mathscr N_U\|\gtrsim U^{-m_h-1},}
\]
and therefore
\[
\boxed{\|Q-W\|\gtrsim U^{-m_h-1}.}
\]
This does not exclude `Q -> W`; it excludes only faster operator-norm convergence.

A canonical inclusion countermodel shows that no algebraic promotion to the polar leakage is valid.  One can have arbitrarily large `B_U` and `C_U` while `(I-WW*)U_SW=0` identically.

## Canonical statuses

- [R19-A] exact square-root block factorization: **✓[M]**;
- [R19-B] P11 square-root off-block lower witness: **✓[M]**;
- [R19-C] polynomial modulus-leakage lower bound: **✓[M]**;
- [R19-D] direct lower bound `||Q-W|| >= c U^{-m_h-1}`: **✓[M]**;
- [R19-E] promotion from square-root/modulus leakage to polar leakage by abstract compression algebra: **✓[M]_neg**;
- [R19-F] concrete P11 polar-gauge / cross-terminal convergence: **?[O]**.

## 1. Exact square-root block algebra

Write
\[
P=WW^*,\qquad S_U=A_S^{1/2},
\]
and define
\[
D_U=W^*S_UW,
\qquad
E_U=(I-P)S_U(I-P)|_{\operatorname{Ran}W^\perp},
\]
\[
\mathscr C_U=(I-P)S_UW.
\]
Then
\[
(I-P)S_U^2W
=(I-P)S_UPS_UW+(I-P)S_U(I-P)S_UW,
\]
so
\[
\boxed{\mathscr B_U=\mathscr C_UD_U+E_U\mathscr C_U.}
\]
Operator Jensen gives
\[
0\le D_U\le A_R^{1/2},
\]
while `E_U` is a compression of `S_U`. Hence
\[
\|\mathscr B_U\|
\le
(\sqrt{\|A_R\|}+\sqrt{\|A_S\|})\|\mathscr C_U\|.
\]
Therefore
\[
\boxed{
\|\mathscr C_U\|
\ge
\frac{\|\mathscr B_U\|}
{\sqrt{\|A_R\|}+\sqrt{\|A_S\|}}.
}
\]

## 2. Insert the actual P11 asymptotics

R13 proves, for the fixed complement witness of first jet order `m_h`,
\[
\|\mathscr B_U\|
\gtrsim
\frac{e^U}{U^{m_h+2}}.
\]
The relative-metric norm estimate gives
\[
\|A_R\|,\|A_S\|\ll\frac{e^U}{U}.
\]
Thus
\[
\boxed{
\|\mathscr C_U\|
\gtrsim
\frac{e^{U/2}}{U^{m_h+3/2}}.
}
\]
This is the first direct P11 witness after applying the positive square root to the future relative metric.

## 3. Modulus leakage

Recall
\[
Q=A_S^{1/2}WA_R^{-1/2},
\qquad
\mathscr N_U=(I-P)Q.
\]
Then exactly
\[
\mathscr C_U=\mathscr N_UA_R^{1/2}.
\]
Hence
\[
\|\mathscr N_U\|
\ge
\frac{\|\mathscr C_U\|}{\sqrt{\|A_R\|}}
\gtrsim U^{-m_h-1}.
\]
The orthogonal decomposition
\[
Q-W=-W\mathscr K+\mathscr N_U
\]
gives
\[
\boxed{\|Q-W\|\ge\|\mathscr N_U\|\gtrsim U^{-m_h-1}.}
\]
This is stronger and logically different from R13's obstruction of the sufficient Jensen-product condition: it is a direct lower bound on the modulus-isometry defect itself.

## 4. No promotion to polar leakage

Take source `C`, target `C^2`, and the canonical inclusion
\[
Wz=(z,0).
\]
Let the base metrics be
\[
G_{R,T_0}=1,
\qquad
G_{S,T_0}=I_2.
\]
For `t>0` choose
\[
A_0=\begin{pmatrix}2&1\\1&2\end{pmatrix},
\qquad
G_{S,U}=t^2A_0,
\qquad
G_{R,U}=2t^2.
\]
Then
\[
A_S=t^2A_0,
\qquad
A_R=2t^2,
\qquad
W^*A_SW=A_R.
\]
But
\[
X_S=tA_0^{1/2},
\qquad
X_R=\sqrt2\,t
\]
are positive, so the polar factors are
\[
U_S=I_2,
\qquad
U_R=1.
\]
Therefore
\[
(I-WW^*)U_SW=0
\]
identically, while
\[
\|(I-WW^*)A_SW\|\asymp t^2,
\qquad
\|(I-WW^*)A_S^{1/2}W\|\asymp t.
\]
Thus large second-moment and square-root leakage do not algebraically force polar leakage.

This is an abstract non-promotion model, not a counterexample to the actual P11 family.

## Structural interpretation

R18 showed that all finite source-compatible Gram blocks are cocycle-invariant, so the unresolved information must be off-block before full functional calculus.  R19 now proves that the actual P11 second-moment off-block survives the positive square root strongly enough to produce a divergent square-root off-block and a polynomial lower bound on modulus leakage.

The remaining gap is sharper than before: it is no longer whether there is off-block square-root information. There is. The gap is how the concrete polar factors `U_R,U_S` reorganize that modulus leakage. Abstract compression algebra alone cannot answer this.

## Scope firewall

R19 does not prove nonconvergence of `Q`, does not give a lower bound for `(I-WW*)U_SW`, and does not prove or disprove
\[
\Gamma_U\to I,
\qquad
K_{R,S}^{T_0,U}\to I,
\qquad
W_{R,S,-}^{[U]}\text{ strong Cauchy}.
\]
No global Object X, Seal, or RH conclusion follows.