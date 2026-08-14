# P11 End-to-End Referee R14 — polar-gauge separation

Date: 2026-08-14

Target: the exact polar-gauge identity in `P11_O3_Diagnostic_Proofs_Core.tex` and the question whether the R13 information on the Jensen/modulus defect can be promoted to the actual cross-terminal kernel.

## Referee question

At fixed `0<R<S<T_0<U`, write on the odd sectors
\[
W=W_{R,S,-}^{[T_0]},\qquad
Q=A_S^{1/2}WA_R^{-1/2},
\]
\[
X_R=(G_{R,U}^-)^{1/2}(G_{R,T_0}^-)^{-1/2},\qquad
X_S=(G_{S,U}^-)^{1/2}(G_{S,T_0}^-)^{-1/2},
\]
and polar-decompose
\[
X_R=U_RA_R^{1/2},\qquad X_S=U_SA_S^{1/2}.
\]
The paper proves
\[
W_{R,S,-}^{[U]}=U_SQU_R^*.
\]
Does control of `Q`, `Theta`, or the R13 divergence `chi ||Theta|| -> infinity` determine the actual future transport or the cross-terminal kernel
\[
K_{R,S}^{T_0,U}=W^*W_{R,S,-}^{[U]}?
\]

# Verdict

The polar-gauge identity is exact and the polar factors are **unique**.  The gauge gap is therefore not a decomposition ambiguity.

However, the modulus/Jensen data do **not** determine the actual future transport.  In fact there is a finite-dimensional exact countermodel satisfying the same pullback and relative-metric algebra in which
\[
Q=W=I,\qquad \Theta=0
\]
identically, while
\[
W^{[U]}\ne W,\qquad K^{T_0,U}\ne I.
\]
There is even a fixed-baseline sequence with `Q=W=I` and `Theta=0` at every future step while the actual future transports alternate between two distinct unitaries and hence are not Cauchy.

Therefore:

- [R14-A] exact polar-gauge identity: **✓[M]**;
- [R14-B] uniqueness of `U_R,U_S`: **✓[M]**;
- [R14-C] exact gauge/modulus separation formula for the cross kernel: **✓[M]**;
- [R14-D] implication `modulus/Jensen control => actual terminal convergence` from the current algebra alone: **✓[M]_neg**;
- [R14-E] actual P11 asymptotics of `U_R,U_S` and `K_{R,S}^{T_0,U}`: **?[O]**.

Thus R14 closes the **logical promotion question** negatively but does not decide the actual P11 transport problem.

---

## 1. Polar factors are unique

Since each `X_R,X_S` is boundedly invertible,
\[
|X_R|=(X_R^*X_R)^{1/2}=A_R^{1/2},\qquad
|X_S|=A_S^{1/2}.
\]
Hence
\[
U_R=X_RA_R^{-1/2},\qquad U_S=X_SA_S^{-1/2}.
\]
There is no phase or gauge choice left after the metric pairs are fixed.

This corrects a possible misreading of the word “gauge”: the obstruction is not nonuniqueness of polar decomposition, but the presence of unitary information not encoded by the relative modulus operators alone.

---

## 2. Exact cross-kernel separation

The paper already gives
\[
W_{R,S,-}^{[U]}=U_SQU_R^*.
\]
Therefore
\[
K_{R,S}^{T_0,U}=W^*U_SQU_R^*.
\]
With
\[
\mathscr K=I-W^*Q,\qquad
\mathscr N=(I-WW^*)Q,
\]
one has
\[
Q=W(I-\mathscr K)+\mathscr N.
\]
Thus exactly
\[
\boxed{
K_{R,S}^{T_0,U}
=\left[W^*U_SW(I-\mathscr K)+W^*U_S\mathscr N\right]U_R^*.
}
\tag{R14.1}
\]
Define the pure gauge compression
\[
\Gamma_U:=W^*U_SWU_R^*.
\]
Then
\[
\boxed{
\|K_{R,S}^{T_0,U}-\Gamma_U\|
\le \|\mathscr K\|+\|\mathscr N\|
\le 2\|Q-W\|.
}
\tag{R14.2}
\]
The second inequality follows because `-W mathscr K` and `mathscr N` are orthogonal for each source vector in
\[
Q-W=-W\mathscr K+\mathscr N.
\]

Hence even if one could prove the **stronger** statement
\[
Q-W\to0,
\]
the actual cross-kernel question would reduce to the still separate requirement
\[
\Gamma_U\to I.
\]

R13 does not prove `Q-W not -> 0`.  It proves `chi ||Theta|| -> infinity`, which only says that the sufficient bound
\[
\|\mathscr K\|\le \chi\|\Theta\|
\]
cannot close the route.  This is a one-sided estimate and cannot be inverted into a nonvanishing lower bound for `Q-W`.

---

## 3. Finite-dimensional countermodel

Work on `C^2`.  Let
\[
B=\begin{pmatrix}2&1\\1&2\end{pmatrix}>0,
\qquad
A=\begin{pmatrix}4&0\\0&1\end{pmatrix}>0.
\]
They do not commute.

Set the base-terminal metrics and transition map to
\[
G_{R,T_0}=I,\qquad
G_{S,T_0}=B,\qquad
J=B^{-1/2}.
\]
At the future horizon set
\[
G_{R,U}=A,\qquad
G_{S,U}=B^{1/2}AB^{1/2}.
\]
Then
\[
J^*G_{S,T_0}J=G_{R,T_0},\qquad
J^*G_{S,U}J=G_{R,U},
\]
so the exact pullback algebra is satisfied.

The normalized base transport is
\[
W=G_{S,T_0}^{1/2}JG_{R,T_0}^{-1/2}=I.
\]
The two relative metrics are both exactly
\[
A_R=A_S=A.
\]
Therefore
\[
Q=A_S^{1/2}WA_R^{-1/2}=I,
\qquad
\Theta=0.
\]
This is the ideal modulus/Jensen situation.

But the actual future transport is
\[
V=W^{[U]}
=(B^{1/2}AB^{1/2})^{1/2}B^{-1/2}A^{-1/2}.
\tag{R14.3}
\]
It is unitary by the pullback identity.  If `V=I`, then
\[
(B^{1/2}AB^{1/2})^{1/2}=A^{1/2}B^{1/2}.
\]
The left side is positive selfadjoint, so `A^{1/2}B^{1/2}` would be selfadjoint.  Hence `A^{1/2}` and `B^{1/2}` would commute and therefore `A` and `B` would commute, contradiction.

Thus
\[
Q=W=I,\quad \Theta=0,
\qquad\text{but}\qquad
W^{[U]}=V\ne I,
\]
and hence `K^{T_0,U}=V != I`.

This proves that even the full modulus package `(A_R,A_S,W,Q,Theta)` does not by itself determine the actual future transport: taking instead `B=I` with the same `A` gives the same relative data `A_R=A_S=A`, `W=Q=I`, `Theta=0`, but now the future transport is exactly `I`.

---

## 4. Non-Cauchy sequence with perfect modulus data

Keep the noncommuting `B` and the same fixed base data `G_{R,T_0}=I`, `G_{S,T_0}=B`, `J=B^{-1/2}`.  For a sequence of future horizons choose alternately
\[
A_n=I,
\qquad
A_n=A.
\]
Put
\[
G_{R,U_n}=A_n,
\qquad
G_{S,U_n}=B^{1/2}A_nB^{1/2}.
\]
At every step
\[
A_{R,n}=A_{S,n}=A_n,
\qquad
Q_n=W=I,
\qquad
\Theta_n=0.
\]
Yet the actual normalized future transport equals `I` when `A_n=I` and equals the fixed nonidentity unitary `V` from (R14.3) when `A_n=A`.

Therefore the future transports are not Cauchy despite perfect modulus/Jensen data at every step.

This is an algebraic model only; it is **not** asserted to arise from the actual P11 prime/Gamma metric family.

---

## 5. Consequence for the actual P11 program

R13 proves for the real P11 family
\[
\chi\|\Theta\|\to\infty.
\]
R14 shows exactly what this does and does not mean:

1. it kills the auxiliary sufficient route `chi ||Theta|| -> 0`;
2. it does **not** imply `Q-W` stays away from zero;
3. even `Q-W -> 0` would not imply `K_{R,S}^{T_0,U} -> I` without control of
   \[
   \Gamma_U=W^*U_SWU_R^*;
   \]
4. the current algebraic identities cannot supply that missing control, because the countermodel has `Theta=0` identically and still has nontrivial/non-Cauchy future transport.

The next genuine mathematical target is therefore no longer a Jensen estimate.  It is an **actual-family gauge theorem**, for example a bound derived from commutators or relative metric structure that forces
\[
W^*U_SWU_R^*\to I
\]
or directly controls the true cross-terminal kernel.

No strong-terminal, Object-X, Seal, or RH conclusion follows from R14.
