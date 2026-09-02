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

## 5A. Intrinsic Gamma formula and strict nested ratio

The constant \(\gamma_X\) introduced in R41 is in fact independent of the chosen baseline
terminal \(T_0\).

Indeed, under the fixed whitening map
\[
x=B_X^{1/2}f,
\]
one has
\[
x\in V_X
\iff
\beta_X^{(0)}(f)=0,
\]
while
\[
\ell_{1,X}(x)=\beta_X^{(1)}(f),
\qquad
\widetilde{\mathfrak c}_{\Gamma,X}[x]
=
\mathfrak c_{\Gamma,X}[f].
\]
Therefore
\[
\boxed{
\gamma_X
=
\sup_{\substack{0\ne f\in\mathcal K_{X,X}^{-}\\
\beta_X^{(0)}(f)=0}}
\frac{|\beta_X^{(1)}(f)|^2}
{\mathfrak c_{\Gamma,X}[f]}.
}
\tag{R42.26a}
\]
Thus \(\gamma_X\) is an intrinsic Gamma/jet invariant of the source radius \(X\), not of
\(T_0\).  Consequently the R41 ratio limit is really
\[
\boxed{
\theta_{R,S}
=
\sqrt{\frac{\gamma_R}{\gamma_S}},
}
\tag{R42.26b}
\]
independent of the baseline terminal.

### Strict monotonicity for every strict source inclusion

Let
\[
mathcal H_X^0
:=
\{f\in\mathcal K_{X,X}^{-}:\beta_X^{(0)}(f)=0\}
\]
with Gamma inner product \(\mathfrak c_{\Gamma,X}\), and let \(g_X\in\mathcal H_X^0\) be
the Gamma-Riesz vector of \(\beta_X^{(1)}|_{\mathcal H_X^0}\):
\[
\mathfrak c_{\Gamma,X}[f,g_X]
=
\beta_X^{(1)}(f)
\qquad(f\in\mathcal H_X^0).
\tag{R42.26c}
\]
Then
\[
\gamma_X=\|g_X\|_{\Gamma,X}^2.
\tag{R42.26d}
\]

For \(0<R<S\), zero extension is an isometric embedding
\[
J_{R,S}:\mathcal H_R^0\hookrightarrow\mathcal H_S^0
\]
for the Gamma inner products, and the first jet is compatible with zero extension.
Hence the Gamma-orthogonal projection of \(g_S\) onto
\(J_{R,S}\mathcal H_R^0\) is \(J_{R,S}g_R\).  Therefore
\[
\gamma_R\le\gamma_S,
\]
with equality iff
\[
g_S\in J_{R,S}\mathcal H_R^0,
\tag{R42.26e}
\]
i.e. iff \(g_S\) is supported in \([-R,R]\).

We now rule out (R42.26e) for every strict \(R<S\).

Assume for contradiction that
\[
\operatorname{ess\,supp}g_S\subset[-R,R].
\tag{R42.26f}
\]
Let
\[
\phi_m(u):=\operatorname{sgn}(u)I_m(|u|),
\]
so that
\[
\beta_S^{(m)}(f)=\langle f,\phi_m\rangle_{L^2(-S,S)}.
\]
Since (R42.26c) holds on the codimension-one kernel of \(\beta_S^{(0)}\), there is
a scalar \(\lambda\in\mathbb C\) such that on the full Gamma form domain
\[
\mathfrak c_{\Gamma,S}[f,g_S]
=
\langle f,\phi_1+\lambda\phi_0\rangle.
\tag{R42.26g}
\]
The right side is represented by an \(L^2\) vector, so the form representation theorem
places \(g_S\) in the operator domain and gives
\[
C_{\Gamma,S}g_S
=
\phi_1+\lambda\phi_0.
\tag{R42.26h}
\]

On the right annulus \(R<x<S\), the local multiplier constant contributes no off-support
term.  By the concrete Gamma kernel from R31/R33,
\[
(C_{\Gamma,S}g_S)(x)
=
-\sum_{n=0}^{\infty}
e^{-\lambda_nx}M_n(g_S),
\qquad
\lambda_n=2n+\frac12,
\tag{R42.26i}
\]
where
\[
M_n(g_S)
=
\int_{-R}^{R}g_S(y)e^{\lambda_ny}\,dy.
\]
The series is normally convergent on every half-plane
\(\operatorname{Re}x\ge R+\delta\), hence the left side of (R42.26h) is real analytic
for \(x>R\).

On \(x>0\),
\[
\phi_0(x)
=
I_0(x)
=
2(1-e^{-x/2}),
\]
\[
\phi_1(x)
=
I_1(x)
=
4-2(x+2)e^{-x/2}.
\tag{R42.26j}
\]
Thus equality on the nonempty interval \((R,S)\) extends analytically to all \(x>R\).
Letting \(x\to\infty\) in (R42.26h) forces
\[
4+2\lambda=0,
\qquad
\lambda=-2.
\]
Then the right side becomes
\[
\phi_1(x)-2\phi_0(x)
=
-2xe^{-x/2}.
\tag{R42.26k}
\]
Multiplying (R42.26i) by \(e^{x/2}\) gives
\[
-\sum_{n=0}^{\infty}M_n(g_S)e^{-2nx},
\]
which tends to the finite limit \(-M_0(g_S)\) as \(x\to\infty\).  But
(R42.26k), multiplied by \(e^{x/2}\), equals \(-2x\), which is unbounded.
Contradiction.

Therefore
\[
\boxed{
\gamma_R<\gamma_S
\qquad
\text{for every }0<R<S.
}
\tag{R42.26l}
\]
Equivalently,
\[
\boxed{
0<\theta_{R,S}<1
\qquad
\text{for every strict source inclusion }R<S.
}
\tag{R42.26m}
\]

This strictness is unconditional and uses only the concrete Gamma symbol and jet compatibility;
there is no R37/G4c input.

### Small-radius quantitative check

Since \(m_\Gamma\ge1\),
\[
\mathfrak c_{\Gamma,R}[f]\ge\|f\|_2^2.
\]
Moreover
\[
I_1(r)
=
\int_0^r se^{-s/2}\,ds
\le\frac{r^2}{2}.
\]
Hence
\[
\boxed{
\gamma_R
\le
\|\phi_1\|_{L^2(-R,R)}^2
\le
\frac{R^5}{10}.
}
\tag{R42.26n}
\]
For every fixed \(S>0\), jet independence gives \(\gamma_S>0\), so
\[
\boxed{
\theta_{R,S}
\le
\frac{R^{5/2}}{\sqrt{10\gamma_S}}
\longrightarrow0
\qquad(R\downarrow0).
}
\tag{R42.26o}
\]
Thus the asymptotic moving-angle defect tends to its maximal value as the old source radius
shrinks.

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

The vector \(\tau_{X,U}\) has an intrinsic future-metric interpretation.  Let
\[
C_X(U):=G_{X,U}^-,
\qquad
B_X:=G_{X,T_0}^-,
\]
and let \(\rho_{X,T_0}=B_X^{-1/2}r_X\) be the baseline Riesz representative.  Define the
future Riesz representative \(\rho_{X,U}^{\rm fut}\) by
\[
\beta_X^{(0)}(f)
=
\langle C_X(U)f,\rho_{X,U}^{\rm fut}\rangle.
\]
Since the same functional is represented at baseline by \(B_X\rho_{X,T_0}\),
\[
C_X(U)\rho_{X,U}^{\rm fut}
=
B_X\rho_{X,T_0}
=
B_X^{1/2}r_X.
\]
Therefore
\[
C_X(U)^{1/2}\rho_{X,U}^{\rm fut}
=
C_X(U)^{-1/2}B_X^{1/2}r_X
=
X_X(U)^{-*}r_X.
\]
Hence
\[
\boxed{
\tau_{X,U}
=
\frac{C_X(U)^{1/2}\rho_{X,U}^{\rm fut}}
{\|C_X(U)^{1/2}\rho_{X,U}^{\rm fut}\|}.
}
\tag{R42.31a}
\]
Thus \(\tau_{X,U}\) is exactly the normalized first-boundary Riesz normal in the actual
future metric, expressed in future-whitened coordinates.

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

There is also an exact future-tangential invariance.  Put
\[
\mathcal V_{X,U}^{\rm fut}:=\tau_{X,U}^{\perp}.
\]
If \(x\in\mathcal V_{R,U}^{\rm fut}\), then by (R42.32)
\[
\langle W_Ux,\tau_{S,U}\rangle
=
\langle x,W_U^*\tau_{S,U}\rangle
=
\theta_U\langle x,\tau_{R,U}\rangle
=0.
\]
Therefore
\[
\boxed{
W_U\mathcal V_{R,U}^{\rm fut}
\subset
\mathcal V_{S,U}^{\rm fut}.
}
\tag{R42.33a}
\]
So the full future transport respects the moving hard-constraint hyperplanes exactly.

This is the first direct placement of the R41 invariant inside the **actual** future transport,
rather than only the modulus isometry.

There is also an exact moving-angle decomposition.  Since \(W_U\) and \(\tau_{X,U}\) are
isometric/unit vectors and (R42.33) is real positive,
\[
\boxed{
W_U\tau_{R,U}
=
\theta_U\tau_{S,U}
+
\rho_{S,U},
\qquad
\rho_{S,U}\perp\tau_{S,U},
\qquad
\|\rho_{S,U}\|^2=1-\theta_U^2.
}
\tag{R42.34}
\]
Thus if \(\gamma_R<\gamma_S\), the actual future transport carries a persistent positive
moving-angle residual of asymptotic squared norm
\[
1-\frac{\gamma_R}{\gamma_S}.
\]
This still does not contradict Strong Terminal because both the source/target normals and the
orthogonal residual are terminal-dependent.

The strong direction theorem (R42.16) converts the moving target into a fixed-vector polar
observable:
\[
\boxed{
\|\tau_{X,U}-U_X(U)\zeta_X\|
=
\|\widehat v_{X,U}-\zeta_X\|
\longrightarrow0.
}
\tag{R42.35}
\]
Therefore
\[
\boxed{
\tau_{X,U}\text{ is strongly convergent/Cauchy}
\iff
U_X(U)\zeta_X\text{ is strongly convergent/Cauchy}.
}
\tag{R42.36}
\]
So the first-residual-jet direction
\[
\zeta_X=-q_{1,X}/\sqrt{\gamma_X}
\]
is a **fixed vector on which B-POL can now be tested directly**.

However (R42.35)--(R42.36) concern \(U_X\), while the exact future transport contains
\(U_R^*\) on its fixed source input.  Hence they do not by themselves bypass the R22/R39
moving-adjoint firewall.

Accordingly (R42.32)--(R42.36) do **not** decide the fixed-vector C6 criterion of R39.7.  They
sharpen the next B-POL target to:

\[
\boxed{
\text{control }U_X(U)\zeta_X
\text{ and then connect that one-sided polar control to the adjoint/cross-terminal action.}
}
\tag{R42.37}
\]

---

## 7A. Tangential polar collapse and codimension-one C6 reduction

This section is new relative to the independently reviewed blob
`16745c2b8e9d892059cff637021d89858158fe45`.
It is therefore **AI-GREEN internal candidate only** until a separate independent review.

### 7A.1 Unwhitened constrained inverse-root limit

Let
\[
\mathcal H_X:=\mathcal K_{X,X}^{-},
\qquad
H_X^0:=\ker\beta_X^{(0)}\subset\mathcal H_X,
\]
and let
\[
C_X(U):=G_{X,U}^{-}
\]
be the unwhitened terminal metric represented in the fixed source Hilbert space
\(\mathcal H_X\).

R27.7 already proves the Mosco limit
\[
\langle C_X(U)f,f\rangle
\ \xrightarrow[M]{}\
\begin{cases}
\mathfrak c_{\Gamma,X}[f],&f\in H_X^0,\\
+\infty,&f\notin H_X^0.
\end{cases}
\tag{R42.38}
\]
At the fixed source level \(X\),
\[
q_X^X(f)
\le
(1+\|H_X\|^2)\mathfrak c_{\Gamma,X}[f],
\]
hence
\[
\mathfrak c_{\Gamma,X}[f]
\ge
a_X\|f\|_{X,X}^2,
\qquad
a_X:=(1+\|H_X\|^2)^{-1}>0.
\]
Therefore
\[
C_X(U)\ge a_XI
\]
uniformly in \(U\).

Let \(\Lambda_X:H_X^0\to H_X^0\) be the bounded positive coercive operator representing
the constrained Gamma form in the fixed source Hilbert metric:
\[
\mathfrak c_{\Gamma,X}[f,g]
=
\langle \Lambda_Xf,g\rangle_{X,X},
\qquad f,g\in H_X^0.
\tag{R42.39}
\]
We now spell out the resolvent step, rather than importing it only by analogy with R27.

Fix \(t\ge0\) and \(g\in\mathcal H_X\).  Put
\[
z_U:=(C_X(U)+tI)^{-1}g.
\]
Equivalently, \(z_U\) is the unique minimizer of
\[
F_{U,g,t}(z)
:=
\langle C_X(U)z,z\rangle
+t\|z\|_{X,X}^2
-2\operatorname{Re}\langle g,z\rangle_{X,X}.
\tag{R42.39a}
\]
On the limit hyperplane \(H_X^0\), define
\[
F_{\infty,g,t}(z)
:=
\mathfrak c_{\Gamma,X}[z]
+t\|z\|_{X,X}^2
-2\operatorname{Re}\langle g,z\rangle_{X,X},
\qquad z\in H_X^0,
\tag{R42.39b}
\]
and \(F_{\infty,g,t}(z)=+\infty\) for \(z\notin H_X^0\).

Because \(\Lambda_X\ge a_XI\) on \(H_X^0\), the unique minimizer of
\(F_{\infty,g,t}\) is
\[
z_\infty
=
(\Lambda_X+tI_{H_X^0})^{-1}P_{H_X^0}g.
\tag{R42.39c}
\]

The family \(z_U\) is bounded.  Indeed, minimality against \(0\) gives
\[
0\ge F_{U,g,t}(z_U)
\ge
(a_X+t)\|z_U\|^2
-2\|g\|\,\|z_U\|,
\]
so
\[
\|z_U\|
\le
\frac{2\|g\|}{a_X+t}.
\tag{R42.39d}
\]

Let \(U_n\to\infty\) and \(z_{U_n}\rightharpoonup z\).  By the Mosco liminf in
(R42.38), weak lower semicontinuity of the norm, and weak continuity of the linear term,
\[
F_{\infty,g,t}(z)
\le
\liminf_{n\to\infty}F_{U_n,g,t}(z_{U_n}).
\tag{R42.39e}
\]
Conversely, Mosco recovery for the unique limit minimizer gives vectors
\[
w_U\to z_\infty
\quad\text{strongly}
\]
such that
\[
\langle C_X(U)w_U,w_U\rangle
\to
\mathfrak c_{\Gamma,X}[z_\infty].
\]
Hence
\[
F_{U,g,t}(w_U)\to F_{\infty,g,t}(z_\infty).
\tag{R42.39f}
\]
By minimality of \(z_U\),
\[
F_{U,g,t}(z_U)\le F_{U,g,t}(w_U).
\]
Combining this with (R42.39e)--(R42.39f) shows that every weak cluster of \(z_U\) minimizes
\(F_{\infty,g,t}\).  By uniqueness,
\[
z_U\rightharpoonup z_\infty
\]
for the full family, and the minimum values converge:
\[
F_{U,g,t}(z_U)\to F_{\infty,g,t}(z_\infty).
\tag{R42.39g}
\]

For every \(w\in\mathcal H_X\), the quadratic Euler identity at the minimizer gives
\[
F_{U,g,t}(w)-F_{U,g,t}(z_U)
=
\langle (C_X(U)+tI)(w-z_U),w-z_U\rangle.
\]
Therefore
\[
F_{U,g,t}(w)-F_{U,g,t}(z_U)
\ge
(a_X+t)\|w-z_U\|^2.
\tag{R42.39h}
\]
Applying this to the recovery sequence \(w_U\), and using
(R42.39f)--(R42.39g), yields
\[
\|w_U-z_U\|\to0.
\]
Since \(w_U\to z_\infty\) strongly,
\[
\boxed{
(C_X(U)+tI)^{-1}g
\longrightarrow
(\Lambda_X+tI_{H_X^0})^{-1}P_{H_X^0}g
}
\tag{R42.39i}
\]
strongly for every fixed \(g\in\mathcal H_X\) and every \(t\ge0\).

Finally, \(C_X(U)\ge a_XI\), so
\[
C_X(U)^{-1/2}
=
\frac1\pi
\int_0^\infty
t^{-1/2}(C_X(U)+tI)^{-1}\,dt
\tag{R42.39j}
\]
with the uniform operator bound
\[
\left\|
t^{-1/2}(C_X(U)+tI)^{-1}
\right\|
\le
\frac{t^{-1/2}}{a_X+t},
\]
whose scalar majorant is integrable on \((0,\infty)\).  Dominated convergence applied
vectorwise to (R42.39i) gives
\[
C_X(U)^{-1/2}
\xrightarrow[s]{}
\frac1\pi
\int_0^\infty
t^{-1/2}
(\Lambda_X+tI_{H_X^0})^{-1}P_{H_X^0}\,dt.
\]
By the spectral calculus of the bounded positive coercive operator \(\Lambda_X\), the
right side equals \(\Lambda_X^{-1/2}P_{H_X^0}\).  Hence
\[
\boxed{
C_X(U)^{-1/2}
\xrightarrow[s]{}
S_{X,\infty}
:=
\Lambda_X^{-1/2}P_{H_X^0}.
}
\tag{R42.40}
\]

Thus R42.40 is now proved directly in the unwhitened Hilbert space.  No new compactness input
is used; only R27.7 Mosco convergence, the uniform coercive lower bound, uniqueness of the
limit minimizer, and the standard inverse-square-root integral formula enter.

### 7A.2 Canonical Gamma isometry between the two hard-constraint realizations

Retain
\[
B_X:=G_{X,T_0}^{-},
\qquad
A_X(U):=B_X^{-1/2}C_X(U)B_X^{-1/2},
\qquad
V_X:=B_X^{1/2}H_X^0,
\]
and let \(L_X:V_X\to V_X\) represent the transported constrained Gamma form:
\[
\widetilde{\mathfrak c}_{\Gamma,X}[x,y]
=
\langle L_Xx,y\rangle.
\]
R27 gives
\[
A_X(U)^{-1/2}
\xrightarrow[s]{}
L_X^{-1/2}P_{V_X}.
\tag{R42.41}
\]

Define
\[
\boxed{
\mathcal J_X^\Gamma
:=
L_X^{1/2}B_X^{1/2}\Lambda_X^{-1/2}
:
H_X^0\longrightarrow V_X.
}
\tag{R42.42}
\]
For \(h,k\in H_X^0\),
\[
\langle L_XB_X^{1/2}h,B_X^{1/2}k\rangle
=
\mathfrak c_{\Gamma,X}[h,k]
=
\langle\Lambda_Xh,k\rangle.
\tag{R42.43}
\]
Hence
\[
\|\mathcal J_X^\Gamma f\|=\|f\|_{X,X}.
\]
Every factor in (R42.42) is boundedly invertible between the displayed spaces, so
\[
\boxed{
\mathcal J_X^\Gamma:H_X^0\to V_X
\text{ is unitary onto }V_X.
}
\tag{R42.44}
\]

### 7A.3 Strong tangential convergence of the individual polar adjoints

Recall
\[
X_X(U)
=
C_X(U)^{1/2}B_X^{-1/2}
=
U_X(U)A_X(U)^{1/2}.
\]
Taking inverses gives
\[
\boxed{
A_X(U)^{-1/2}U_X(U)^*
=
B_X^{1/2}C_X(U)^{-1/2}.
}
\tag{R42.45}
\]

Fix \(f\in H_X^0\).  Along any subsequence with
\[
U_X(U_n)^*f\rightharpoonup y,
\]
the right side of (R42.45) converges strongly by (R42.40), while the left side converges
weakly by (R42.41).  Therefore
\[
P_{V_X}y
=
L_X^{1/2}B_X^{1/2}\Lambda_X^{-1/2}f
=
\mathcal J_X^\Gamma f.
\tag{R42.46}
\]
By (R42.44),
\[
\|P_{V_X}y\|=\|f\|.
\]
Since \(\|U_X(U_n)^*f\|=\|f\|\), weak lower semicontinuity gives \(\|y\|\le\|f\|\).
Thus (R42.46) exhausts the whole possible norm and
\[
y=\mathcal J_X^\Gamma f.
\]
The weak cluster is unique and has the same norm as the sequence, hence
\[
\boxed{
U_X(U)^*f
\longrightarrow
\mathcal J_X^\Gamma f
\quad\text{strongly for every }f\in H_X^0.
}
\tag{R42.47}
\]

Because \(\mathcal J_X^\Gamma\) is unitary onto \(V_X\), if
\(v=\mathcal J_X^\Gamma f\in V_X\), then
\[
\|U_X(U)v-f\|
=
\|v-U_X(U)^*f\|
\to0.
\]
Therefore
\[
\boxed{
U_X(U)v
\longrightarrow
(\mathcal J_X^\Gamma)^*v
\quad\text{strongly for every }v\in V_X.
}
\tag{R42.48}
\]

Thus B-POL is already strongly convergent on the full tangential hard-constraint block.
Only its normal channel remains open.

### 7A.4 The future-gauge normals actually converge

R42.16 gives
\[
\widehat v_{X,U}\to\zeta_X
\]
strongly, with \(\zeta_X\in V_X\).  Combining this with (R42.48),
\[
\boxed{
\tau_{X,U}
=
U_X(U)\widehat v_{X,U}
\longrightarrow
\tau_{X,\infty}
:=
(\mathcal J_X^\Gamma)^*\zeta_X
\in H_X^0
}
\tag{R42.49}
\]
strongly.

The exact identity R42.32 then yields
\[
\boxed{
W_U^*\tau_{S,\infty}
\longrightarrow
\theta_{R,S}\tau_{R,\infty}
}
\tag{R42.50}
\]
strongly.

### 7A.5 Strong convergence of the actual future transport on the hard-constraint hyperplane

Fix \(0<R<S<T_0\) and abbreviate
\[
\mathcal J_R:=\mathcal J_R^\Gamma,
\qquad
\mathcal J_S:=\mathcal J_S^\Gamma.
\]
For \(f\in H_R^0\), (R42.47) gives
\[
U_R^*f\to\mathcal J_Rf.
\]
Frozen R38.12 and the isometry of \(Q_U\) then give
\[
Q_UU_R^*f
\longrightarrow
Y_{R,S}\mathcal J_Rf.
\]
The limit lies in \(V_S\), so (R42.48) at level \(S\) gives
\[
\boxed{
W_{R,S}^{[U]}f
\longrightarrow
W_{R,S}^{(0)}f
:=
\mathcal J_S^*Y_{R,S}\mathcal J_Rf
\quad\text{strongly for every }f\in H_R^0.
}
\tag{R42.51}
\]
Thus
\[
\boxed{
W_{R,S}^{(0)}
=
\mathcal J_S^*Y_{R,S}\mathcal J_R
:
H_R^0\to H_S^0
}
\tag{R42.52}
\]
is an isometry.

This is a strong-limit theorem for the genuine P11 future transport on an
infinite-dimensional closed codimension-one subspace.

### 7A.6 Stabilization of the strict Gamma angle inside the actual strong limit

Since
\[
\tau_{R,\infty}=\mathcal J_R^*\zeta_R,
\qquad
\tau_{S,\infty}=\mathcal J_S^*\zeta_S,
\]
R42.24 gives
\[
\boxed{
(W_{R,S}^{(0)})^*\tau_{S,\infty}
=
\theta_{R,S}\tau_{R,\infty}.
}
\tag{R42.53}
\]
Hence
\[
\boxed{
\langle W_{R,S}^{(0)}\tau_{R,\infty},\tau_{S,\infty}\rangle
=
\theta_{R,S}
=
\sqrt{\frac{\gamma_R}{\gamma_S}}
\in(0,1).
}
\tag{R42.54}
\]

The residual from R42.34 also converges strongly:
\[
\boxed{
\rho_{S,U}
\longrightarrow
\rho_{S,\infty}
:=
W_{R,S}^{(0)}\tau_{R,\infty}
-
\theta_{R,S}\tau_{S,\infty},
}
\tag{R42.55}
\]
with
\[
\boxed{
\rho_{S,\infty}\perp\tau_{S,\infty},
\qquad
\|\rho_{S,\infty}\|^2
=
1-\frac{\gamma_R}{\gamma_S}
>0.
}
\tag{R42.56}
\]

Thus the strict Gamma angle is a fixed feature of the already-existing strong tangential
terminal limit, not merely a moving asymptotic diagnostic.

### 7A.7 Exact codimension-one reduction of Strong Terminal / C6

Let \(\varepsilon_R\) be the unit Riesz normal of \(\beta_R^{(0)}\) in the fixed source graph
Hilbert metric:
\[
H_R^0=\varepsilon_R^\perp,
\qquad
\|\varepsilon_R\|_{X,R}=1.
\tag{R42.57}
\]
Then
\[
\mathcal H_R=H_R^0\oplus\mathbb C\varepsilon_R.
\]

Since every \(W_{R,S}^{[U]}\) is an isometry and (R42.51) gives strong convergence on
\(H_R^0\),
\[
\boxed{
W_{R,S}^{[U]}
\text{ is strongly Cauchy on }\mathcal H_R
\iff
\bigl(W_{R,S}^{[U]}\varepsilon_R\bigr)_U
\text{ is strongly Cauchy}.
}
\tag{R42.58}
\]

By the exact R39 cross-terminal identity, this is equivalent to
\[
\boxed{
\operatorname{Re}
\langle
\varepsilon_R,
K_{R,S}^{T,U}\varepsilon_R
\rangle_{X,R}
\longrightarrow1
\qquad(T,U\to\infty).
}
\tag{R42.59}
\]

Therefore B-C6 for a fixed strict pair \(R<S\) is reduced from an operator-valued
strong-Cauchy problem to the orbit of **one fixed source normal vector**, equivalently
to **one fixed scalar matrix coefficient of the exact cross-terminal kernel**:
\[
\boxed{
\text{B-MOD: one normal scalar;}
\qquad
\text{B-POL: one normal channel;}
\qquad
\text{B-C6: one fixed normal orbit / one scalar cross-kernel coefficient.}
}
\tag{R42.60}
\]

### 7A.8 Constraints on any remaining normal-orbit cluster

Let
\[
\mathcal M_{R,S}^{(0)}
:=
\operatorname{Ran}W_{R,S}^{(0)}
\subset H_S^0.
\]
If
\[
W_{R,S}^{[U_n]}\varepsilon_R\rightharpoonup y,
\]
then orthogonality to the strongly convergent tangential images gives
\[
y\in(\mathcal M_{R,S}^{(0)})^\perp.
\tag{R42.61}
\]
Equation (R42.50) also gives
\[
\langle y,\tau_{S,\infty}\rangle=0.
\tag{R42.62}
\]

Since (R42.53) implies
\[
P_{\mathcal M_{R,S}^{(0)}}\tau_{S,\infty}
=
\theta_{R,S}
W_{R,S}^{(0)}\tau_{R,\infty},
\]
the vector
\[
d_{R,S}
:=
\tau_{S,\infty}
-
\theta_{R,S}W_{R,S}^{(0)}\tau_{R,\infty}
\in
(\mathcal M_{R,S}^{(0)})^\perp
\tag{R42.63}
\]
is nonzero and satisfies
\[
\|d_{R,S}\|^2
=
1-\theta_{R,S}^2
>0.
\]
Every weak cluster of the one remaining normal orbit lies in
\[
\boxed{
(\mathcal M_{R,S}^{(0)})^\perp
\cap
d_{R,S}^{\perp}.
}
\tag{R42.64}
\]

This does not yet force uniqueness of the normal-orbit cluster, because the complement may
remain infinite-dimensional.  It does remove one explicit nonzero complement direction from
the possible escape geometry.

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

After Section 7A, the earlier item “prove convergence of \(\tau_{X,U}\)” is closed, and
the general fixed-vector C6 problem has collapsed to the single normal vector
\(\varepsilon_R\).  The next live targets are therefore sharply separated:

1. **B-C6 normal orbit:** determine
   \[
   \operatorname{Re}\langle
   \varepsilon_R,K_{R,S}^{T,U}\varepsilon_R
   \rangle\to1
   \quad?
   \]
   This is now the exact remaining Strong-Terminal gate.
2. **B-POL normal channel:** determine the one-dimensional/escape asymptotics of the polar
   factors off \(H_X^0\) and \(V_X\); tangential polar convergence is already closed by
   R42.47--R42.48.
3. **B-MOD normal scalar:** determine the limit/no-escape behavior of
   \(a_U=\langle Q_Ue_R,e_S\rangle\).
4. **Higher-order route:** obtain a quantitative rate for the R17 exact-boundary-null Schur
   remainder if a third-order jet expansion is needed to connect the remaining normal
   channels.

For Strong Terminal itself, item 1 is now the primary target; the higher-order R17 rate is no
longer the only visible route.

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
- full-space strong convergence of the polar factors \(U_X(U)\) or \(U_X(U)^*\);
- full-space strong Cauchy convergence of \(W_{R,S}^{[U]}\);
- Object X;
- RH.

Independent review ledger:

- Blob `16745c2b8e9d892059cff637021d89858158fe45`, commit
  `0c49b76e8cfda361b58a1e0f783c2c9495ef1008`: independently reviewer-GREEN for
  R42.1--R42.37, including the strict inequality \(\gamma_R<\gamma_S\).
- Section 7A, R42.38--R42.64: independently destructively reviewed on head
  `7fa5fc7ca190eb6171f3e77d297413a1574ce3bd`; all checked conclusions were reported GREEN
  except that R42.40 was judged structurally correct but insufficiently expanded because its
  resolvent proof was only referenced by analogy to R27.
- R42.39a--R42.39j and the expanded proof of R42.40 were added after that review to close
  precisely that proof-completeness gap.  The expanded R42.40 text itself awaits the final
  independent recheck.

Current booking:
\[
\boxed{
\text{R42 core reviewer-GREEN; Section 7A reviewer-GREEN modulo final recheck of expanded R42.40.}
}
\]

No freeze and no canonical \(\checkmark[M]\) promotion before independent reviewer verification.
