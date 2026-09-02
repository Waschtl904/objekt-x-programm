# P11 End-to-End Referee R42 — dual-normal direction limit and second-order eta-blindness

Date: 2026-09-02

## Purpose

Continue the independently verified R41 second-order hard-constraint Gamma layer without
touching R37/G4c.

R41 determines the norm scale
\[
U\|v_{X,U}\|\to \frac{\sqrt{\gamma_X}}2,
\qquad
v_{X,U}:=A_X(U)^{-1/2}r_X,
\]
but deliberately leaves the direction of \(\widehat v_{X,U}\) open.

R42 shows that the direction is in fact already forced by the same unique constrained-Gamma
minimizer.  The normalized future dual normal converges strongly to a fixed **tangential**
first-residual-jet direction.

This has two consequences:

1. the R41 ratio invariant acquires an exact fixed-vector range-projection geometry;
2. the complete second-order dual-normal layer is **blind** to the R38 normal cluster scalar
   \(a_U=\langle Q_Ue_R,e_S\rangle\).  Hence no direct
   \(\gamma_R/\gamma_S\Rightarrow a_U\) bridge can be extracted from this order alone.

A separate exact identity rewrites the same ratio inside the **actual future transport**
\(W_{R,S}^{[U]}\), exposing the next B-POL/C6 target as the motion of future-whitened dual-normal
directions.

Status: **AI-GREEN internal candidate only**, no freeze and no canonical promotion.

---

## 1. Fixed Gamma first-residual-jet vectors

Use the frozen R41 notation.  On
\[
V_X=r_X^\perp
\]
let
\[
\ell_{1,X}
=
\widehat\beta_X^{(1)}|_{V_X},
\]
and let \(b_{1,X}\in V_X\) be its Riesz vector in the fixed baseline Hilbert norm:
\[
\ell_{1,X}(y)=\langle y,b_{1,X}\rangle.
\]

The constrained Gamma operator is
\[
\widetilde{\mathfrak c}_{\Gamma,X}[y]
=
\langle L_Xy,y\rangle,
\qquad
a_0I\le L_X\le I.
\]

Define
\[
u_{1,X}:=L_X^{-1}b_{1,X},
\qquad
q_{1,X}:=L_X^{-1/2}b_{1,X}.
\tag{R42.1}
\]
Then
\[
\gamma_X
=
\langle b_{1,X},L_X^{-1}b_{1,X}\rangle
=
\|q_{1,X}\|^2.
\tag{R42.2}
\]

R41's unique affine Gamma minimizer is
\[
y_{*,X}
=
-\frac{2}{\gamma_X}u_{1,X}.
\tag{R42.3}
\]

---

## 2. Strong convergence of the exact rescaled minimizers

Put
\[
\delta_X(U)
:=
\langle r_X,A_X(U)^{-1}r_X\rangle,
\qquad
m_X(U)=\delta_X(U)^{-1}.
\]
The unique minimizer of
\[
\langle A_X(U)x,x\rangle
\quad\text{subject to}\quad
\widehat\beta_X^{(0)}(x)=1
\]
is
\[
x_{X,U}
=
\frac{A_X(U)^{-1}r_X}{\delta_X(U)}.
\tag{R42.4}
\]
Define the R41-scaled minimizer
\[
y_{X,U}:=\frac{x_{X,U}}{U}.
\tag{R42.5}
\]
Then
\[
\widehat\beta_X^{(0)}(y_{X,U})=\frac1U,
\qquad
\langle A_X(U)y_{X,U},y_{X,U}\rangle
=
\frac{m_X(U)}{U^2}.
\tag{R42.6}
\]

R41 proves
\[
\frac{m_X(U)}{U^2}
\longrightarrow
M_X
=
\frac4{\gamma_X}.
\tag{R42.7}
\]

We claim the **full** strong limit
\[
\boxed{
y_{X,U}
\longrightarrow
y_{*,X}
=
-\frac{2}{\gamma_X}u_{1,X}
}
\tag{R42.8}
\]
in the fixed Gamma norm, hence also in the baseline Hilbert norm.

### Proof

R24 coercivity and (R42.7) make \(y_{X,U}\) bounded.  Let a subsequence converge weakly,
\[
y_{X,U_n}\rightharpoonup y.
\]
The frozen R41 liminf argument applies to these exact minimizers and gives
\[
y\in V_X,
\qquad
\widehat\beta_X^{(1)}(y)=-2.
\tag{R42.9}
\]
Moreover positivity of the Schur part gives
\[
\widetilde{\mathfrak c}_{\Gamma,X}[y_{X,U_n}]
\le
\langle A_X(U_n)y_{X,U_n},y_{X,U_n}\rangle
\to
M_X.
\]
Weak lower semicontinuity yields
\[
M_X
\le
\widetilde{\mathfrak c}_{\Gamma,X}[y]
\le
\liminf_n
\widetilde{\mathfrak c}_{\Gamma,X}[y_{X,U_n}]
\le M_X.
\]
Thus \(y\) is the unique affine Gamma minimizer, so \(y=y_{*,X}\), and the Gamma norms
converge.  Weak convergence plus convergence of the Gamma norms gives strong Gamma convergence.

Every weakly convergent subsequence has the same strong limit, hence (R42.8) holds for the full
family.
\(\square\)

---

## 3. Strong first-order direction of \(A_X(U)^{-1}r_X\)

From (R42.4)--(R42.5),
\[
A_X(U)^{-1}r_X
=
\delta_X(U)\,U y_{X,U}.
\]
R41 gives
\[
U^2\delta_X(U)\to\frac{\gamma_X}{4}.
\]
Using (R42.8),
\[
\boxed{
U A_X(U)^{-1}r_X
\longrightarrow
-\frac12u_{1,X}
}
\tag{R42.10}
\]
strongly.

This is already stronger than the scalar R41 norm limit: it identifies the full first-order
vector asymptotic of the inverse-normal channel.

---

## 4. Strong first-order direction of the inverse-square-root dual normal

Set
\[
w_{X,U}:=U v_{X,U}
=
U A_X(U)^{-1/2}r_X.
\tag{R42.11}
\]
R41 gives
\[
\|w_{X,U}\|
\to
\frac{\sqrt{\gamma_X}}2.
\tag{R42.12}
\]
Hence \(w_{X,U}\) is bounded.

R27 gives
\[
A_X(U)^{-1/2}
\xrightarrow[s]{}
T_{X,\infty}
=
L_X^{-1/2}P_{V_X}.
\tag{R42.13}
\]

Let \(w_{X,U_n}\rightharpoonup w\).  Since the operators in (R42.13) converge strongly and
the vectors are bounded,
\[
A_X(U_n)^{-1/2}w_{X,U_n}
\rightharpoonup
T_{X,\infty}w.
\]
But
\[
A_X(U)^{-1/2}w_{X,U}
=
U A_X(U)^{-1}r_X
\to
-\frac12u_{1,X}
\]
strongly by (R42.10).  Therefore
\[
L_X^{-1/2}P_{V_X}w
=
-\frac12u_{1,X},
\]
hence
\[
P_{V_X}w
=
-\frac12L_X^{1/2}u_{1,X}
=
-\frac12q_{1,X}.
\tag{R42.14}
\]
By (R42.2),
\[
\left\|P_{V_X}w\right\|
=
\frac{\sqrt{\gamma_X}}2.
\]
This already equals the limiting norm in (R42.12).  Thus \(w\) has no component in
\(V_X^\perp=\mathbb Ce_X\), and equality of weak-limit and sequence norms forces strong
convergence.

Therefore
\[
\boxed{
U A_X(U)^{-1/2}r_X
\longrightarrow
-\frac12q_{1,X}
=
-\frac12L_X^{-1/2}b_{1,X}
}
\tag{R42.15}
\]
strongly.

In particular the normalized future dual normal has the fixed direction
\[
\boxed{
\widehat v_{X,U}
:=
\frac{v_{X,U}}{\|v_{X,U}\|}
\longrightarrow
\zeta_X
:=
-\frac{q_{1,X}}{\sqrt{\gamma_X}}
}
\tag{R42.16}
\]
strongly, where
\[
\zeta_X\in V_X,
\qquad
\|\zeta_X\|=1.
\]

Thus the R41 firewall item “no limit direction for \(\widehat v_{X,U}\)” is closed by R42;
R41 itself remains frozen and is not retroactively edited.

---

## 5. Nested fixed-vector range geometry

Fix
\[
0<R<S<T_0.
\]
The frozen R38 identity is
\[
Q_U^*v_{S,U}=v_{R,U}.
\tag{R42.17}
\]
Multiplying by \(U\) and using (R42.15) gives
\[
\boxed{
Q_U^*q_{1,S}
\longrightarrow
q_{1,R}
}
\tag{R42.18}
\]
strongly.

Because \(q_{1,R}\in V_R\), frozen R38.12 also gives
\[
Q_Uq_{1,R}
\longrightarrow
Y_{R,S}q_{1,R}
\tag{R42.19}
\]
strongly.

Let
\[
P_U:=Q_UQ_U^*
\]
be the orthogonal projection onto \(\operatorname{Ran}Q_U\).  Combining
(R42.18)--(R42.19),
\[
\boxed{
P_Uq_{1,S}
\longrightarrow
Y_{R,S}q_{1,R}
}
\tag{R42.20}
\]
strongly, and therefore
\[
\boxed{
(I-P_U)q_{1,S}
\longrightarrow
q_{1,S}-Y_{R,S}q_{1,R}
}
\tag{R42.21}
\]
strongly.

Consequently
\[
Y_{R,S}^*q_{1,S}=q_{1,R}
\tag{R42.22}
\]
and
\[
\boxed{
\|q_{1,S}-Y_{R,S}q_{1,R}\|^2
=
\gamma_S-\gamma_R.
}
\tag{R42.23}
\]

In normalized form, with
\[
\theta
=
\sqrt{\frac{\gamma_R}{\gamma_S}},
\]
one gets
\[
\boxed{
Q_U^*\zeta_S
\longrightarrow
\theta\zeta_R,
}
\tag{R42.24}
\]
\[
\boxed{
P_U\zeta_S
\longrightarrow
\theta Y_{R,S}\zeta_R,
}
\tag{R42.25}
\]
and
\[
\boxed{
(I-P_U)\zeta_S
\longrightarrow
\zeta_S-\theta Y_{R,S}\zeta_R,
\qquad
\left\|\zeta_S-\theta Y_{R,S}\zeta_R\right\|^2
=
1-\theta^2.
}
\tag{R42.26}
\]

Thus the R41 asymptotic angle defect is not merely a norm number: its defect vector converges
strongly to a fixed tangential Gamma direction.

---

## 6. Second-order eta-blindness

Recall frozen R38:
every WOT cluster of \(Q_U\) has the form
\[
Q_\eta(v+\alpha e_R)
=
Y_{R,S}v+\alpha\eta e_S,
\qquad
\eta\in\overline{\mathbb D}.
\tag{R42.27}
\]
The unknown scalar \(\eta\) is exactly the cluster value of
\[
a_U=\langle Q_Ue_R,e_S\rangle.
\]

But
\[
q_{1,R}\in V_R,
\qquad
q_{1,S}\in V_S.
\]
Hence for every \(\eta\),
\[
Q_\eta^*q_{1,S}
=
Y_{R,S}^*q_{1,S}
=
q_{1,R},
\tag{R42.28}
\]
independently of \(\eta\).

Therefore the complete second-order dual-normal limit
\[
\gamma_R,\gamma_S,\theta,
\zeta_R,\zeta_S,
q_{1,S}-Yq_{1,R}
\]
lives entirely in the tangential Gamma geometry and contains **no occurrence of the normal
cluster scalar \(\eta\)**.

Accordingly:
\[
\boxed{
\text{R41/R42 second-order dual-normal data do not algebraically determine }a_U
\text{ or its WOT cluster parameter }\eta.
}
\tag{R42.29}
\]

This is an information firewall, not a claim that the concrete P11 family admits arbitrary
\(\eta\).  A relation could still arise from additional higher-order or polar information.
It simply does not arise from the verified second-order identities themselves.

---

## 7. Exact bridge into the actual future transport

Let the polar factors be
\[
X_X(U)=U_X(U)A_X(U)^{1/2}
\]
as in R14/R39, and define the **future-gauge normalized dual normal**
\[
\tau_{X,U}
:=
U_X(U)\widehat v_{X,U}.
\tag{R42.30}
\]
Since
\[
X_X(U)^{-*}
=
U_X(U)A_X(U)^{-1/2},
\]
this can also be written without an arbitrary polar choice as
\[
\boxed{
\tau_{X,U}
=
\frac{X_X(U)^{-*}r_X}{\|v_{X,U}\|}.
}
\tag{R42.31}
\]
The polar factors are unique, so \(\tau_{X,U}\) is canonical.

For the actual future transport
\[
W_U:=W_{R,S}^{[U]}
=
U_SQ_UU_R^*,
\]
the normalized R38 identity gives **exactly**
\[
\boxed{
W_U^*\tau_{S,U}
=
\theta_U\tau_{R,U},
\qquad
\theta_U
=
\frac{\|v_{R,U}\|}{\|v_{S,U}\|}.
}
\tag{R42.32}
\]
Equivalently,
\[
\boxed{
\langle W_U\tau_{R,U},\tau_{S,U}\rangle
=
\theta_U
\longrightarrow
\sqrt{\frac{\gamma_R}{\gamma_S}}.
}
\tag{R42.33}
\]

This is the first direct placement of the R41 invariant inside the **actual** future transport,
rather than only the modulus isometry.

However the vectors \(\tau_{R,U},\tau_{S,U}\) themselves move with \(U\).  Therefore
(R42.32)--(R42.33) do **not** decide the fixed-vector C6 criterion of R39.7.  They identify
precisely the remaining B-POL issue in this channel:

\[
\boxed{
\text{control the terminal motion of }\tau_{X,U}
\text{ (or an equivalent fixed-vector surrogate).}
}
\tag{R42.34}
\]

---

## 8. Attempted next-order expansion and the present wall

The direct terminal expansion can be continued formally one order:
\[
(1-s/U)^{-1/2}
=
1+\frac{s}{2U}+\frac{3s^2}{8U^2}+O(U^{-3}),
\]
so the next boundary-functional coefficient is governed by \(\beta^{(2)}\).

To turn this into the next correction to (R42.15), however, one needs quantitative control of
the recovery energy beyond R17's
\[
D_U(z_U,z_U)\to0.
\]
R17 supplies no rate.  At the next rescaled order an unspecified \(o(1)\) Schur remainder can
compete with the desired \(U^{-1}\) correction to the affine Gamma minimizer.

Thus the current canonical inputs justify the first-order vector limits (R42.10) and (R42.15),
but do **not** yet justify a third-order expansion capable of exposing a normal component and
hence the scalar \(a_U\).

A viable next theorem would therefore be one of:

1. a quantitative rate for the R17 exact-boundary-null Schur remainder on the relevant
   finite-jet recovery family;
2. a direct compactness/convergence theorem for the future-gauge normals \(\tau_{X,U}\);
3. a direct fixed-vector estimate for the cross-terminal kernel R39.7 that bypasses both.

---

## 9. Governance / firewall

R42 uses:

- frozen R38: strong tangential modulus limit and exact dual-normal identity;
- frozen R40/R41: the \(U^{-1}\) norm scale and exact second-order Gamma limit;
- canonical R24/R27: uniform coercivity and strong inverse-root limit.

It uses no R37/G4c conclusion.

R42 does **not** prove:

- convergence of \(a_U\);
- \(|a_U|\to1\);
- strong convergence of \(Q_U\);
- convergence of the polar factors \(U_X(U)\);
- convergence of \(\tau_{X,U}\);
- strong Cauchy convergence of \(W_{R,S}^{[U]}\);
- Object X;
- RH.

Current booking:
\[
\boxed{
\text{R42 internal exploratory result: AI-GREEN candidate only.}
}
\]

No freeze and no canonical \(\checkmark[M]\) promotion before independent reviewer verification.
