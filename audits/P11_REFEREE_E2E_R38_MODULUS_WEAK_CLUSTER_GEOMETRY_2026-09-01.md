# P11 End-to-End Referee R38 — weak cluster geometry of the modulus isometries

Date: 2026-09-01

## Purpose / firewall

Continue the Strong-Terminal modulus analysis after R27/R28/R37 without assuming an
operator-norm rank-one asymptotic that the current P11 theory does not prove.

For fixed

\[
0<R<S<T_0
\]

write

\[
Q_U:=A_S(U)^{1/2}WA_R(U)^{-1/2},
\qquad U>T_0,
\]

where \(Q_U\) is the modulus isometry:

\[
Q_U^*Q_U=I.
\]

R27 gives strong limits

\[
A_X(U)^{-1/2}\xrightarrow[s]{}T_{X,\infty}
=
L_X^{-1/2}P_{V_X},
\qquad X=R,S,
\]

with

\[
V_X=r_X^\perp
\]

the baseline-whitened hard-constraint hyperplane and \(L_X\) the bounded coercive
constrained-Gamma operator on \(V_X\).

The target is to characterize possible weak cluster points of \(Q_Ux\) for fixed source vectors.

No claim of strong convergence is made.

---

## 1. Exact inverse-root intertwining identity

By definition of \(Q_U\),

\[
\boxed{
A_S(U)^{-1/2}Q_U
=
WA_R(U)^{-1/2}.
}
\tag{R38.1}
\]

This is exact for every \(U>T_0\).

There is also the dual-normal identity

\[
\boxed{
Q_U^*A_S(U)^{-1/2}r_S
=
A_R(U)^{-1/2}r_R,
}
\tag{R38.2}
\]

by R28.2: pullback compatibility of the baseline-whitened boundary functional gives
\[
W^*r_S=r_R.
\]
Thus (R38.2) uses the canonical R28 constraint-normal compatibility, not an additional
asymptotic assumption.

Equation (R38.2) identifies a potentially useful next-order scalar channel, but R38 does not
assume any rate or normalized limit for these two shrinking vectors.

---

## 2. Weak cluster equation

Fix \(x\) in the R-source baseline-whitened Hilbert space.

Since \(Q_U\) is an isometry,

\[
\|Q_Ux\|=\|x\|,
\]

so every sequence \(U_n\to\infty\) has weakly convergent subnets, and in the separable
P11 Hilbert spaces one may extract weakly convergent subsequences.

Suppose

\[
Q_{U_n}x\rightharpoonup y.
\tag{R38.3}
\]

Then

\[
\boxed{
T_{S,\infty}y
=
WT_{R,\infty}x.
}
\tag{R38.4}
\]

### Proof

For any fixed target vector \(z\),

\[
\begin{aligned}
\langle A_S(U_n)^{-1/2}Q_{U_n}x,z\rangle
&=
\langle Q_{U_n}x,A_S(U_n)^{-1/2}z\rangle.
\end{aligned}
\]

R27 gives

\[
A_S(U_n)^{-1/2}z\to T_{S,\infty}z
\]

strongly.  Together with (R38.3), the left side therefore converges to

\[
\langle y,T_{S,\infty}z\rangle
=
\langle T_{S,\infty}y,z\rangle,
\]

because \(T_{S,\infty}\) is selfadjoint.

On the other hand, by (R38.1),

\[
A_S(U_n)^{-1/2}Q_{U_n}x
=
WA_R(U_n)^{-1/2}x
\to
WT_{R,\infty}x
\]

strongly.

Comparing limits proves (R38.4).
\(\square\)

Status: **AI-GREEN candidate**.

---

## 3. Unique tangential component

Since

\[
T_{S,\infty}=L_S^{-1/2}P_{V_S},
\]

equation (R38.4) gives

\[
L_S^{-1/2}P_{V_S}y
=
WL_R^{-1/2}P_{V_R}x.
\]

Therefore

\[
\boxed{
P_{V_S}y
=
Y_{R,S}P_{V_R}x,
}
\tag{R38.5}
\]

where

\[
\boxed{
Y_{R,S}
:=
L_S^{1/2}W L_R^{-1/2}
:
V_R\to V_S.
}
\tag{R38.6}
\]

Gamma compatibility gives

\[
W^*L_SW=L_R
\quad\text{on }V_R,
\]

hence

\[
Y_{R,S}^*Y_{R,S}=I_{V_R}.
\]

Thus \(Y_{R,S}\) is an isometry.

Consequently every weak cluster point has the form

\[
\boxed{
y
=
Y_{R,S}P_{V_R}x
+
\eta(x)e_S,
}
\tag{R38.7}
\]

where

\[
e_S:=r_S/\|r_S\|
\]

and \(\eta(x)\in\mathbb C\) may depend on the chosen subsequence.

This is a substantial compression: **the entire tangential cluster geometry is unique; all
remaining weak-cluster ambiguity is one complex scalar in the target constraint-normal
direction.**

Status: **AI-GREEN candidate**.

---

## 4. Constraint-normal source vector

Let

\[
e_R:=r_R/\|r_R\|.
\]

Then

\[
P_{V_R}e_R=0,
\qquad
T_{R,\infty}e_R=0.
\]

Therefore every weak cluster point of \(Q_Ue_R\) satisfies

\[
T_{S,\infty}y=0.
\]

Since

\[
\ker T_{S,\infty}
=
V_S^\perp
=
\mathbb C e_S,
\]

one obtains

\[
\boxed{
Q_{U_n}e_R\rightharpoonup y
\Longrightarrow
y=\eta e_S
\quad\text{for some }|\eta|\le1.
}
\tag{R38.8}
\]

Thus the normal source direction cannot have a weak cluster component in any fixed tangential
target direction.

The unresolved possibilities are exactly:

1. \(|\eta|=1\): no loss of norm, giving strong convergence along that subsequence to a phase
   multiple of \(e_S\);
2. \(0<|\eta|<1\): part of the unit norm escapes weakly through terminal-dependent high-energy
   tangential directions;
3. \(\eta=0\): complete weak escape.

R27 alone does not distinguish these cases.

Status: **AI-GREEN candidate**.

---

## 5. Relation to the R37 modulus no-go

On the R37 open two-shift region,

\[
0<R<a<b<S<T_0<2a,
\]

the R37 finite/algebraic argument, together with its still-open analytic Gate G4c,
gives the conditional conclusion

\[
s_{R,S,T_0}\ne0
\]

and hence

\[
Q_U\not\xrightarrow[s]{}W.
\]

This paragraph does **not** promote R37 or close G4c.  Without an independent closure of
G4c, the displayed R37 conclusion remains conditional exactly as recorded in the R37
dependency freeze.

R38 explains geometrically why this does not yet identify the actual modulus limit.

The baseline image of the source normal is

\[
We_R.
\]

But

\[
r_S=Wr_R+s
\]

with \(s\ne0\), so the target normal direction \(e_S\) is not the baseline source-normal
direction \(We_R\).

If one could prove the additional no-escape statement

\[
\|P_{V_S}Q_Ue_R\|\to0
\quad\text{and}\quad
|\langle Q_Ue_R,e_S\rangle|\to1,
\]

with a controlled phase, then \(Q_Ue_R\) would have a concrete strong limit along the target
normal.

R38 does **not** prove this.  It shows only that every weak cluster point is already forced onto
that one-dimensional normal line.

---

## 6. Exact next scalar gate: future dual normals

Define

\[
v_{X,U}:=A_X(U)^{-1/2}r_X.
\]

R27 implies

\[
v_{X,U}\to0
\]

strongly because \(r_X\perp V_X\).

Equation (R38.2) becomes

\[
\boxed{
Q_U^*v_{S,U}=v_{R,U}.
}
\tag{R38.9}
\]

Hence

\[
\|v_{R,U}\|\le\|v_{S,U}\|.
\tag{R38.10}
\]

Moreover,

\[
\|v_{X,U}\|^2
=
\langle r_X,A_X(U)^{-1}r_X\rangle
\]

is exactly the squared dual norm of the fixed first-boundary functional
\(\widehat\beta_X\) with respect to the future relative metric.

The current P11 repository proves these quantities tend to zero but does **not** provide a
common first-order asymptotic or ratio theorem.

Thus the next clean scalar target is

\[
\boxed{
\frac{\|v_{R,U}\|}{\|v_{S,U}\|}
\stackrel{?}{\longrightarrow}1
}
\tag{R38.11}
\]

(or determine its actual limit).

A ratio limit of one, combined with (R38.9), would imply that \(v_{S,U}\) becomes asymptotically
contained in \(\operatorname{Ran}Q_U\) and would strongly constrain the normal phase/escape
mechanism.

This is a **next-order hard-constraint problem**, not contained in the unscaled Mosco limit.

---

## 7. Strong-Terminal firewall

R38 does not prove:

- strong convergence of \(Q_U\);
- a phase limit for \(Q_Ue_R\);
- strong convergence of the polar gauge;
- strong convergence or Cauchy convergence of \(W_{R,S,-}^{[U]}\);
- closure or promotion of R37 Gate G4c;
- Object X;
- RH.

The result is a cluster-geometry reduction:

\[
\boxed{
\text{unknown modulus asymptotics}
\;\longrightarrow\;
\text{known tangential cluster map}
+
\text{one-dimensional normal/escape gate}.
}
\]
