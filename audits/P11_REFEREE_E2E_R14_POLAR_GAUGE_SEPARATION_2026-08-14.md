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

However, the modulus/Jensen data do **not** determine the actual future transport.  There is a finite-dimensional exact countermodel with the **fixed canonical coordinate inclusion**
\[
J:\mathbb C\hookrightarrow\mathbb C^2,
\qquad Jz=(z,0),
\]
(the finite-dimensional analogue of zero extension) satisfying the terminal pullback and relative-metric identities for which
\[
Q=W,\qquad \Theta=0
\]
identically, while
\[
W^{[U]}\ne W,\qquad K^{T_0,U}\ne I.
\]
There is even a fixed-baseline sequence with the same inclusion `J`, with `Q=W` and `Theta=0` at every future step, while the actual future transports alternate between two distinct isometries and hence are not Cauchy.

Therefore:

- [R14-A] exact polar-gauge identity: **✓[M]**;
- [R14-B] uniqueness of `U_R,U_S`: **✓[M]**;
- [R14-C] exact gauge/modulus separation formula for the cross kernel: **✓[M]**;
- [R14-D] implication `modulus/Jensen control => actual terminal convergence` from the current pullback/relative/polar algebra, even with canonical inclusion: **✓[M]_neg**;
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

## 3. Canonical-inclusion countermodel

Take source space `C`, target space `C^2`, and fix once and for all
\[
Jz=ze_1,
\qquad e_1=(1,0)^T.
\]
Define the positive matrix
\[
P=\begin{pmatrix}
\sqrt3/2&1/2\\
1/2&1
\end{pmatrix}>0,
\]
and
\[
w:=Pe_1=(\sqrt3/2,1/2)^T.
\]
Then `||w||=1`.

Set the base metrics
\[
G_{R,T_0}=1,
\qquad
G_{S,T_0}=P^2.
\]
The pullback identity holds because
\[
J^*G_{S,T_0}J=e_1^*P^2e_1=\|Pe_1\|^2=1=G_{R,T_0}.
\]
The normalized base transport is therefore
\[
W=G_{S,T_0}^{1/2}JG_{R,T_0}^{-1/2}=Pe_1=w.
\]

Now put
\[
A:=I+3ww^*
=\begin{pmatrix}
13/4&3\sqrt3/4\\
3\sqrt3/4&7/4
\end{pmatrix},
\]
so that `Aw=4w`.  At the future horizon define
\[
G_{R,U}=4,
\qquad
G_{S,U}=PAP.
\]
Then
\[
J^*G_{S,U}J=e_1^*PAPe_1=w^*Aw=4=G_{R,U},
\]
so the future pullback identity also holds.

The relative metrics are
\[
A_R=4,
\qquad
A_S=P^{-1}(PAP)P^{-1}=A.
\]
Therefore
\[
Q=A_S^{1/2}WA_R^{-1/2}
=\frac12A^{1/2}w
=w
=W.
\]
Also
\[
W^*A_S^{1/2}W=w^*A^{1/2}w=2=A_R^{1/2},
\]
so
\[
\Theta=0.
\]
Thus the modulus/Jensen data are ideal.

The actual future normalized transport is
\[
V:=W^{[U]}=\frac12(PAP)^{1/2}e_1.
\tag{R14.3}
\]
We claim `V != w`.  In polar notation `U_R=1` and
\[
X_S=(PAP)^{1/2}P^{-1}=U_SA^{1/2}.
\]
All matrices are real and `det U_S=+1`.  If `V=w`, then from `W^{[U]}=U_SQ` and `Q=w` we obtain `U_Sw=w`.  An orientation-preserving orthogonal operator on `R^2` fixing a nonzero vector is the identity, so `U_S=I`.  Hence
\[
(PAP)^{1/2}=A^{1/2}P.
\]
The left side is selfadjoint, forcing `A^{1/2}P` to be selfadjoint and therefore `A^{1/2}` to commute with `P`.  Hence `A` would commute with `P`.

But direct multiplication gives
\[
PA-AP=
\begin{pmatrix}
0&3/8-3\sqrt3/4\\
-3/8+3\sqrt3/4&0
\end{pmatrix}\ne0.
\]
Contradiction.  Thus
\[
Q=W,\quad\Theta=0,
\qquad\text{but}\qquad
W^{[U]}=V\ne W.
\]
Since `W,V` are unit vectors, `K^{T_0,U}=W^*V != 1` as well.

This is stronger than the earlier arbitrary-map toy model: the transition is already the canonical coordinate inclusion.

---

## 4. Non-Cauchy sequence with fixed canonical inclusion and perfect modulus data

Keep the same fixed baseline `P,J`.  Let the scalar source future metric alternate between
\[
a_n=1
\qquad\text{and}\qquad
a_n=4.
\]
Put
\[
A_n:=I+(a_n-1)ww^*,
\]
\[
G_{R,U_n}=a_n,
\qquad
G_{S,U_n}=PA_nP.
\]
At every step `w` is an eigenvector of `A_n` with eigenvalue `a_n`, so
\[
Q_n=W,
\qquad
\Theta_n=0.
\]
When `a_n=1`, the future metrics equal the baseline metrics and `W^{[U_n]}=W`.  When `a_n=4`, the future transport is the fixed distinct vector `V` from (R14.3).

Hence the future normalized transports alternate between two distinct isometries and are not Cauchy despite perfect modulus/Jensen data at every step.

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
4. the pullback/relative/polar algebra plus canonical-inclusion structure still cannot supply that missing control, because the countermodel has `Theta=0` identically and nontrivial/non-Cauchy future transport.

The next genuine mathematical target is therefore no longer a Jensen estimate.  It is an **actual-family gauge theorem**, for example a bound derived from the concrete P11 metric generators, commutators, or source arithmetic that forces
\[
W^*U_SWU_R^*\to I
\]
or directly controls the true cross-terminal kernel.

No strong-terminal, Object-X, Seal, or RH conclusion follows from R14.
