# P11 End-to-End Referee R41 — second-order hard-constraint Gamma boundary layer

Date: 2026-09-01

## Purpose

Upgrade R40 from the scale

\[
\langle r_X,A_X(U)^{-1}r_X\rangle=\Theta(U^{-2})
\]

to an exact next-order limit.

The result is a second asymptotic layer below R27's hard-constraint Mosco limit.

Fix source level \(X\) and baseline terminal \(T_0>X\).  In baseline-whitened coordinates let

\[
A_X(U)=A_{T_0,U}^{X,-},
\qquad
\widehat\beta_X^{(m)}(x)
=
\beta_X^{(m)}(B_X^{-1/2}x),
\]

\[
B_X=G_{X,T_0}^-,
\]

and let \(r_X\) be the Riesz vector of \(\widehat\beta_X^{(0)}\).

Put

\[
V_X=\ker\widehat\beta_X^{(0)}=r_X^\perp.
\]

R27's constrained-Gamma limit on \(V_X\) is represented by

\[
\widetilde{\mathfrak c}_{\Gamma,X}[y]
=
\langle L_Xy,y\rangle,
\qquad
a_0I\le L_X\le I.
\]

Define the first residual jet functional

\[
\ell_{1,X}
:=
\left.\widehat\beta_X^{(1)}\right|_{V_X}.
\]

Jet independence implies \(\ell_{1,X}\ne0\).

Let

\[
\boxed{
\gamma_X
:=
\|\ell_{1,X}\|_{(V_X,\widetilde{\mathfrak c}_{\Gamma,X})^*}^2
>0.
}
\tag{R41.1}
\]

Then the candidate theorem is

\[
\boxed{
U^2
\langle r_X,A_X(U)^{-1}r_X\rangle
\longrightarrow
\frac{\gamma_X}{4}.
}
\tag{R41.2}
\]

Equivalently, for

\[
v_{X,U}:=A_X(U)^{-1/2}r_X,
\]

\[
\boxed{
U\|v_{X,U}\|
\longrightarrow
\frac{\sqrt{\gamma_X}}{2}.
}
\tag{R41.3}
\]

Status: **AI-GREEN candidate**, no promotion.

---

## 1. Scaled variational problem

Define

\[
m_X(U)
:=
\inf\left\{
\langle A_X(U)x,x\rangle:
\widehat\beta_X^{(0)}(x)=1
\right\}.
\tag{R41.4}
\]

As in R40,

\[
m_X(U)
=
\langle r_X,A_X(U)^{-1}r_X\rangle^{-1}.
\tag{R41.5}
\]

Put \(x=Uy\).  By quadratic homogeneity,

\[
\boxed{
\frac{m_X(U)}{U^2}
=
\inf\left\{
\langle A_X(U)y,y\rangle:
\widehat\beta_X^{(0)}(y)=\frac1U
\right\}.
}
\tag{R41.6}
\]

R40 gives

\[
0<c\le \frac{m_X(U)}{U^2}\le C
\tag{R41.7}
\]

for all large \(U\).

---

## 2. First-order boundary-functional expansion

R40 gives in fixed baseline dual norm

\[
\widehat\mu_{X,U}
:=
e^{-U/2}U^{1/2}\ell_U\circ B_X^{-1/2}
\]

with

\[
\boxed{
\widehat\mu_{X,U}(y)
=
-\sqrt2
\left[
\widehat\beta_X^{(0)}(y)
+
\frac1{2U}\widehat\beta_X^{(1)}(y)
+
\mathcal E_{X,U}(y)
\right],
}
\tag{R41.8}
\]

where

\[
\|\mathcal E_{X,U}\|
\le CU^{-2}.
\tag{R41.9}
\]

Also

\[
d_U=2U+O(1)
\]

and

\[
\langle A_X(U)y,y\rangle
\ge
\frac{|\ell_U(B_X^{-1/2}y)|^2}{d_U}.
\tag{R41.10}
\]

---

## 3. Liminf: emergence of the affine first-jet constraint

Let \(U_n\to\infty\), and choose exact minimizers \(y_n\) in R41.6.  Such minimizers exist because
\(A_X(U_n)\) is boundedly invertible and the affine constraint is closed.

By R41.7 and R24 coercivity,

\[
\|y_n\|\le C.
\]

After passing to a subsequence,

\[
y_n\rightharpoonup y.
\tag{R41.11}
\]

The affine constraint gives

\[
\widehat\beta_X^{(0)}(y_n)=U_n^{-1}\to0,
\]

hence

\[
y\in V_X.
\tag{R41.12}
\]

Because the energies in R41.6 stay bounded, R41.10 implies

\[
|\widehat\mu_{X,U_n}(y_n)|
\le
C U_ne^{-U_n/2}.
\tag{R41.13}
\]

Multiply R41.8 by \(U_n\).  Since \(\|y_n\|\) is bounded,

\[
U_n\mathcal E_{X,U_n}(y_n)\to0.
\]

Using \(U_n\widehat\beta_X^{(0)}(y_n)=1\), equation R41.13 yields

\[
1+\frac12\widehat\beta_X^{(1)}(y_n)\to0.
\]

Therefore

\[
\boxed{
\widehat\beta_X^{(1)}(y)=-2.
}
\tag{R41.14}
\]

Exact Gamma compatibility and positivity of the Schur term give

\[
\langle A_X(U_n)y_n,y_n\rangle
\ge
\widetilde{\mathfrak c}_{\Gamma,X}[y_n].
\]

The fixed Gamma form is weakly lower semicontinuous, so

\[
\liminf_n
\frac{m_X(U_n)}{U_n^2}
\ge
\widetilde{\mathfrak c}_{\Gamma,X}[y].
\]

Hence

\[
\boxed{
\liminf_{U\to\infty}
\frac{m_X(U)}{U^2}
\ge
M_X,
}
\tag{R41.15}
\]

where

\[
M_X
:=
\inf\left\{
\widetilde{\mathfrak c}_{\Gamma,X}[y]:
y\in V_X,\ 
\widehat\beta_X^{(1)}(y)=-2
\right\}.
\tag{R41.16}
\]

---

## 4. Recovery sequence with the moving affine constraint

We prove the matching limsup.

First take a smooth odd

\[
y\in V_X
\]

with

\[
\widehat\beta_X^{(1)}(y)=-2.
\tag{R41.17}
\]

Choose a fixed smooth odd \(g_0\) with

\[
\widehat\beta_X^{(0)}(g_0)=1.
\]

R27/R17 define the exact boundary-null recovery

\[
z_U(y)
=
y-
\frac{\ell_U(B_X^{-1/2}y)}
{\ell_U(B_X^{-1/2}g_0)}
g_0.
\tag{R41.18}
\]

Then

\[
\ell_U(B_X^{-1/2}z_U(y))=0
\]

and

\[
z_U(y)\to y.
\]

Using R41.8 and R41.17,

\[
\frac{
\ell_U(B_X^{-1/2}y)
}{
\ell_U(B_X^{-1/2}g_0)
}
=
-\frac1U+O(U^{-2}).
\tag{R41.19}
\]

Therefore

\[
\widehat\beta_X^{(0)}(z_U(y))
=
\frac1U+O(U^{-2}).
\tag{R41.20}
\]

Set

\[
c_U
:=
\frac{U^{-1}}
{\widehat\beta_X^{(0)}(z_U(y))}.
\tag{R41.21}
\]

Then

\[
c_U\to1.
\]

Define

\[
y_U:=c_Uz_U(y).
\]

It satisfies exactly

\[
\boxed{
\widehat\beta_X^{(0)}(y_U)=U^{-1},
\qquad
\ell_U(B_X^{-1/2}y_U)=0.
}
\tag{R41.22}
\]

R27's recovery theorem gives

\[
\langle A_X(U)z_U(y),z_U(y)\rangle
\to
\widetilde{\mathfrak c}_{\Gamma,X}[y].
\]

Since \(c_U\to1\),

\[
\boxed{
\langle A_X(U)y_U,y_U\rangle
\to
\widetilde{\mathfrak c}_{\Gamma,X}[y].
}
\tag{R41.23}
\]

Thus

\[
\limsup_{U\to\infty}
\frac{m_X(U)}{U^2}
\le
\widetilde{\mathfrak c}_{\Gamma,X}[y].
\]

It remains to justify density **with the two constraints imposed exactly**.

Choose smooth odd vectors \(h_0,h_1\) such that
\[
\widehat\beta_X^{(0)}(h_0)=1,
\qquad
\widehat\beta_X^{(0)}(h_1)=0,
\qquad
\widehat\beta_X^{(1)}(h_1)=1.
\tag{R41.23a}
\]
Such a pair exists because the first two odd jet functionals are linearly independent:
on smooth odd sources they are represented by the nonproportional kernels \(I_0\) and \(I_1\).

Let \(y\in V_X\) satisfy \(\widehat\beta_X^{(1)}(y)=-2\), and choose arbitrary smooth odd
core vectors \(g_n\to y\) in the Gamma graph norm.  Define
\[
\widetilde g_n
:=
g_n
-
\widehat\beta_X^{(0)}(g_n)h_0
-
\Bigl(
\widehat\beta_X^{(1)}(g_n)
-
\widehat\beta_X^{(0)}(g_n)\widehat\beta_X^{(1)}(h_0)
+2
\Bigr)h_1.
\tag{R41.23b}
\]
Then exactly
\[
\widehat\beta_X^{(0)}(\widetilde g_n)=0,
\qquad
\widehat\beta_X^{(1)}(\widetilde g_n)=-2.
\]
Continuity of both jet functionals and \(g_n\to y\) imply that both correction
coefficients tend to zero.  Hence
\[
\widetilde g_n\to y
\]
in the Gamma graph norm.

Thus smooth odd vectors satisfying both affine constraints are indeed dense in the constrained
affine subspace.  Therefore

\[
\boxed{
\limsup_{U\to\infty}
\frac{m_X(U)}{U^2}
\le M_X.
}
\tag{R41.24}
\]

Combining R41.15 and R41.24,

\[
\boxed{
\frac{m_X(U)}{U^2}
\longrightarrow M_X.
}
\tag{R41.25}
\]

---

## 5. Evaluate the fixed Gamma minimization

Let \(b_{1,X}\in V_X\) be the baseline-Hilbert Riesz vector of
\(\ell_{1,X}\):

\[
\ell_{1,X}(y)=\langle y,b_{1,X}\rangle.
\]

The constrained-Gamma metric is represented by \(L_X\).  Therefore its Riesz vector for
\(\ell_{1,X}\) is

\[
u_{1,X}:=L_X^{-1}b_{1,X}.
\]

Its squared dual norm is

\[
\boxed{
\gamma_X
=
\langle b_{1,X},L_X^{-1}b_{1,X}\rangle
=
\ell_{1,X}(u_{1,X}).
}
\tag{R41.26}
\]

The minimum of

\[
\langle L_Xy,y\rangle
\]

under

\[
\ell_{1,X}(y)=-2
\]

is achieved at

\[
y_*=-\frac{2}{\gamma_X}u_{1,X}
\]

and equals

\[
\boxed{
M_X=\frac4{\gamma_X}.
}
\tag{R41.27}
\]

By R41.5 and R41.25,

\[
U^2
\langle r_X,A_X(U)^{-1}r_X\rangle
=
\frac{U^2}{m_X(U)}
\longrightarrow
\frac{\gamma_X}{4}.
\]

This proves R41.2.

---

## 6. Nested R/S ratio theorem

For fixed \(0<R<S<T_0\), define \(\gamma_R,\gamma_S\) as above.

R38 gives

\[
Q_U^*v_{S,U}=v_{R,U}.
\]

Therefore

\[
\|v_{R,U}\|\le\|v_{S,U}\|.
\]

R41.3 gives the exact ratio limit

\[
\boxed{
\frac{\|v_{R,U}\|}
{\|v_{S,U}\|}
\longrightarrow
\theta_{R,S,T_0}
:=
\sqrt{\frac{\gamma_R}{\gamma_S}}
\in(0,1].
}
\tag{R41.28}
\]

Consequently

\[
\boxed{
\gamma_R\le\gamma_S.
}
\tag{R41.29}
\]

The ratio \(\theta\) is a new fixed-window invariant measuring how much of the target's
next-order hard-constraint dual direction is already visible from the smaller source.

For normalized future dual normals

\[
\widehat v_{X,U}=v_{X,U}/\|v_{X,U}\|,
\]

one has exactly

\[
Q_U^*\widehat v_{S,U}
=
\theta_U\widehat v_{R,U},
\qquad
\theta_U\to\theta_{R,S,T_0}.
\tag{R41.30}
\]

Hence

\[
\|(I-Q_UQ_U^*)\widehat v_{S,U}\|^2
=
1-\theta_U^2
\longrightarrow
1-\frac{\gamma_R}{\gamma_S}.
\tag{R41.31}
\]

This gives a quantitative next-order angle between the target future-dual normal and the modulus
range.

---

## 7. Equality criterion

Because \(\ell_{1,R}\) is the restriction of \(\ell_{1,S}\) under the canonical nested inclusion
and Gamma compatibility makes
\[
W:(V_R,\widetilde{\mathfrak c}_{\Gamma,R})
\longrightarrow
(V_S,\widetilde{\mathfrak c}_{\Gamma,S})
\]
an isometric embedding, \(\gamma_R\le\gamma_S\) is the standard monotonicity of squared dual
norms under enlargement of the admissible constrained space.

Let
\[
M:=WV_R\subset V_S
\]
and let \(P_M^{\Gamma}\) denote orthogonal projection onto \(M\) in the
\(\widetilde{\mathfrak c}_{\Gamma,S}\)-inner product.  If
\[
u_{1,S}=L_S^{-1}b_{1,S},
\qquad
u_{1,R}=L_R^{-1}b_{1,R},
\]
then the Riesz property and Gamma compatibility give the exact identity
\[
\boxed{
P_M^{\Gamma}u_{1,S}=Wu_{1,R}.
}
\tag{R41.31a}
\]
Consequently
\[
\gamma_R
=
\|P_M^{\Gamma}u_{1,S}\|_{\Gamma,S}^2,
\qquad
\gamma_S
=
\|u_{1,S}\|_{\Gamma,S}^2.
\tag{R41.31b}
\]
Therefore
\[
\boxed{
\gamma_R=\gamma_S
\iff
u_{1,S}\in WV_R
\iff
u_{1,S}=Wu_{1,R}.
}
\tag{R41.31c}
\]

Equivalently, equality holds exactly when the target first-residual-jet Riesz representer has no
new constrained-Gamma component orthogonal to the nested source subspace.  This is a fixed-window
question and a natural next candidate for an explicit Gamma offblock test.

---

## 8. Interpretation

R27 says the zeroth boundary jet becomes an infinitely hard constraint.

R41 identifies the first boundary layer beneath that constraint:

\[
\boxed{
\beta^{(0)}=\frac1U
\quad\leadsto\quad
\beta^{(1)}=-2
}
\]

in the rescaled minimization.

Thus the first residual jet \(\beta^{(1)}\) controls the leading decay of the future dual normal.

This is the beginning of a possible **iterated jet boundary-layer hierarchy** beneath the
Strong-Terminal problem.

---

## 9. Internal audit ledger

As of 2026-09-02, the R41 chain has been independently rederived internally against the committed
definitions and the frozen R40/R38 inputs.

Checked points include:

- the rescaling identity (R41.6) and existence/boundedness of exact affine minimizers;
- the liminf passage from bounded rescaled energy to the forced affine first-jet condition
  \(\widehat\beta_X^{(1)}=-2\);
- the exact boundary-null recovery sequence and normalization in (R41.18)--(R41.23);
- the constrained density step, now made explicit in (R41.23a)--(R41.23b);
- evaluation of the fixed Gamma minimization, including the factor \(1/4\);
- the ratio theorem (R41.28)--(R41.31);
- the equality criterion, now expressed exactly by the Gamma-orthogonal projection
  (R41.31a)--(R41.31c).

Dependencies used are R5-JET/R17 through the R27 recovery mechanism, R24/R27 for coercivity and
hard-constraint convergence, frozen R40 for the first-order boundary expansion/scale, and frozen
R38 for the nested dual-normal identity.  R41 uses no R37/G4c conclusion.

Independent reviewer verification of the exact hardened R41 head
`f26896db27e1359c153940b35e2466f2af38b2a9` was completed on 2026-09-02.  The reviewer
checked the forced first-jet condition (R41.14), the recovery and exact two-constraint density
construction (R41.18)--(R41.23b), the factor \(1/4\) in (R41.2), the ratio limit (R41.28),
and the Gamma-projection equality criterion (R41.31a)--(R41.31c), with all checked steps
reported GREEN.  The dependency chain against frozen R38/R40 and the canonical R5/R16/R17/R24/R27
inputs was also reported source-compatible, with no use of R37/G4c.

Accordingly R41 is now **FROZEN as independently verified AI-GREEN** on this research lineage.
This freeze records the verified second-order hard-constraint Gamma boundary layer and the
scalar norm-ratio theorem only.  It is **not** a canonical \(\checkmark[M]\) promotion;
R37/G4c remains open and Strong Terminal / C6 remains \(?[O]\).

---

## 10. Strong-Terminal firewall

R41 does not prove:

- a limit direction for \(\widehat v_{X,U}\);
- a strong limit for \(Q_U\);
- a strong limit for \(W_{R,S}^{[U]}\);
- R22 baseline stabilization;
- Object X;
- RH.

It closes R38's scalar norm-ratio gate but leaves the directional/escape problem open.
