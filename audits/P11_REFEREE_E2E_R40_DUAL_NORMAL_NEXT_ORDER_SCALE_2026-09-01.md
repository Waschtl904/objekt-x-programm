# P11 End-to-End Referee R40 — first next-order scale of the hard-constraint dual normals

Date: 2026-09-01

## Purpose

Continue R38's future-dual-normal gate.

For fixed source level \(X\) and baseline terminal \(T_0>X\), let

\[
A_X(U)=A_{T_0,U}^{X,-},
\qquad U>T_0,
\]

be the baseline-whitened odd relative metric, and let \(r_X\) be the R28 Riesz vector of

\[
\widehat\beta_X(x)
=
\beta_X^{(0)}(B_X^{-1/2}x),
\qquad B_X=G_{X,T_0}^-.
\]

Define

\[
v_{X,U}:=A_X(U)^{-1/2}r_X.
\]

R27 proves \(v_{X,U}\to0\), but no rate.

R40 identifies the first robust scale:

\[
\boxed{
\|v_{X,U}\|\asymp U^{-1}.
}
\tag{R40.1}
\]

Equivalently,

\[
\boxed{
\langle r_X,A_X(U)^{-1}r_X\rangle
\asymp U^{-2}.
}
\tag{R40.2}
\]

Status: **AI-GREEN candidate**.

No limit constant is claimed.

---

## 1. Variational meaning

Because \(A_X(U)>0\),

\[
\|v_{X,U}\|^2
=
\langle r_X,A_X(U)^{-1}r_X\rangle.
\]

This is the squared dual norm of \(\widehat\beta_X\) in the future relative metric.

Equivalently,

\[
\boxed{
\|v_{X,U}\|^{-2}
=
\inf\left\{
\langle A_X(U)x,x\rangle:
\widehat\beta_X(x)=1
\right\}.
}
\tag{R40.3}
\]

Thus R40.1 is equivalent to proving that the minimum future energy under the fixed constraint
\(\widehat\beta_X=1\) is of order \(U^2\).

---

## 2. Uniform first-order tilt of the terminal boundary functional

The direct terminal bridge gives, uniformly on the fixed source interval,

\[
\Phi_U(r)
=
\sqrt2e^{U/2}U^{-1/2}
\int_0^r
e^{-s/2}(1-s/U)^{-1/2}\,ds
+
O_X(e^{U/2}e^{-c\sqrt U}).
\]

Using

\[
(1-z)^{-1/2}
=
1+\frac12z+O(z^2)
\]

uniformly for \(0\le s\le X\), one obtains in the dual norm of the fixed source graph space

\[
\boxed{
\mu_{X,U}
:=
e^{-U/2}U^{1/2}\ell_U
=
-\sqrt2
\left(
\beta_X^{(0)}
+
\frac1{2U}\beta_X^{(1)}
+
\mathcal E_{X,U}
\right),
}
\tag{R40.4}
\]

with

\[
\boxed{
\|\mathcal E_{X,U}\|_{\mathcal H_X^*}
\le
\frac{C_X}{U^2}
}
\tag{R40.5}
\]

for all sufficiently large \(U\).

After baseline whitening the same statement is

\[
\widehat\mu_{X,U}(x)
=
-\sqrt2
\left(
\widehat\beta_X^{(0)}(x)
+
\frac1{2U}\widehat\beta_X^{(1)}(x)
+
\widehat{\mathcal E}_{X,U}(x)
\right),
\tag{R40.6}
\]

with an \(O(U^{-2})\) operator-norm remainder.

R27 also gives

\[
d_U=2U+O(1)
\tag{R40.7}
\]

and the exact rank-one lower bound

\[
\langle A_X(U)x,x\rangle
\ge
\frac{|\ell_U(B_X^{-1/2}x)|^2}{d_U}.
\tag{R40.8}
\]

---

## 3. Lower bound on the constrained energy

Let

\[
\widehat\beta_X^{(0)}(x)=1
\]

and put \(t=\|x\|\) in the fixed baseline-whitened Hilbert norm.

Since \(\widehat\beta_X^{(1)}\) is a fixed continuous functional, R40.6 gives

\[
|\widehat\mu_{X,U}(x)|
\ge
\sqrt2
\left(
1-\frac{C_1t}{U}
\right)
\tag{R40.9}
\]

after enlarging \(C_1\) and taking \(U\) large.

Split into two cases.

### Case A: \(t\le U/(2C_1)\)

Then

\[
|\widehat\mu_{X,U}(x)|
\ge \frac1{\sqrt2}.
\]

Hence

\[
|\ell_U(B_X^{-1/2}x)|^2
\ge
\frac12\,\frac{e^U}{U}.
\]

Using \(d_U\asymp U\),

\[
\langle A_X(U)x,x\rangle
\ge
c\frac{e^U}{U^2}.
\]

In particular, for all sufficiently large \(U\),

\[
\langle A_X(U)x,x\rangle
\ge cU^2.
\tag{R40.10}
\]

### Case B: \(t>U/(2C_1)\)

R24 gives the uniform coercivity

\[
A_X(U)\ge a_0I,
\qquad
a_0>0.
\]

Therefore

\[
\langle A_X(U)x,x\rangle
\ge
a_0t^2
\ge
\frac{a_0}{4C_1^2}U^2.
\tag{R40.11}
\]

Combining the two cases,

\[
\boxed{
\inf_{\widehat\beta_X^{(0)}(x)=1}
\langle A_X(U)x,x\rangle
\ge
c_XU^2.
}
\tag{R40.12}
\]

By R40.3,

\[
\boxed{
\|v_{X,U}\|^2
\le
C_XU^{-2}.
}
\tag{R40.13}
\]

---

## 4. Matching upper bound via the exact R16 near-null direction

Choose fixed smooth odd vectors \(f_0,f_1\) with

\[
\beta_X^{(0)}(f_0)\ne0,
\]

\[
\beta_X^{(0)}(f_1)=0,
\qquad
\beta_X^{(1)}(f_1)\ne0.
\]

R16 defines

\[
z_U
=
f_1
-
a_Uf_0,
\qquad
a_U
=
\frac{\ell_U(f_1)}{\ell_U(f_0)},
\tag{R40.14}
\]

so that

\[
\ell_U(z_U)=0.
\]

The boundary expansion gives

\[
a_U
=
\frac{
\frac12\beta_X^{(1)}(f_1)
}{
\beta_X^{(0)}(f_0)
}
\,U^{-1}
+
O(U^{-2}),
\tag{R40.15}
\]

hence

\[
|a_U|\asymp U^{-1}.
\tag{R40.16}
\]

Since \(\beta_X^{(0)}(f_1)=0\),

\[
\beta_X^{(0)}(z_U)
=
-a_U\beta_X^{(0)}(f_0),
\]

so

\[
|\beta_X^{(0)}(z_U)|
\asymp U^{-1}.
\tag{R40.17}
\]

Define

\[
x_U
:=
\frac{B_X^{1/2}z_U}
{\beta_X^{(0)}(z_U)}.
\tag{R40.18}
\]

Then

\[
\widehat\beta_X^{(0)}(x_U)=1
\]

and

\[
\|x_U\|=O(U).
\tag{R40.19}
\]

Because \(\ell_U(z_U)=0\), the rank-one TC1 term vanishes exactly.

R16 proves

\[
D_U(z_U,z_U)=O(1),
\]

while the fixed Gamma contribution is \(O(1)\) because \(z_U\to f_1\) in the fixed
two-dimensional smooth block.

Therefore

\[
q_U^X(J_{X,U}z_U)=O(1).
\tag{R40.20}
\]

Scaling by R40.17,

\[
\boxed{
\langle A_X(U)x_U,x_U\rangle
=O(U^2).
}
\tag{R40.21}
\]

Hence

\[
\inf_{\widehat\beta_X^{(0)}(x)=1}
\langle A_X(U)x,x\rangle
\le C_XU^2.
\tag{R40.22}
\]

By R40.3,

\[
\boxed{
\|v_{X,U}\|^2
\ge
c_XU^{-2}.
}
\tag{R40.23}
\]

Together with R40.13 this proves R40.1--R40.2.

---

## 5. Nested R/S consequence

For fixed \(0<R<S<T_0\), R38 gives the exact identity

\[
Q_U^*v_{S,U}=v_{R,U}.
\tag{R40.24}
\]

Therefore

\[
\|v_{R,U}\|\le\|v_{S,U}\|.
\]

R40 now upgrades the qualitative vanishing to

\[
\boxed{
0<c_{R,S,T_0}
\le
\frac{\|v_{R,U}\|}{\|v_{S,U}\|}
\le1
}
\tag{R40.25}
\]

for all sufficiently large \(U\).

Thus the normalized target future-dual normal cannot become asymptotically orthogonal to
\(\operatorname{Ran}Q_U\).

Indeed, with

\[
\widehat v_{X,U}
=
\frac{v_{X,U}}{\|v_{X,U}\|},
\qquad
\theta_U
=
\frac{\|v_{R,U}\|}{\|v_{S,U}\|},
\]

one has

\[
Q_U^*\widehat v_{S,U}
=
\theta_U\widehat v_{R,U}.
\tag{R40.26}
\]

Hence

\[
\|Q_UQ_U^*\widehat v_{S,U}\|
=
\theta_U
\ge c_{R,S,T_0}>0.
\tag{R40.27}
\]

The exact limit of \(\theta_U\) remains open.

---

## 6. Why no limit constant is claimed

To obtain

\[
U^2\|v_{X,U}\|^2\to\gamma_X
\]

one would need the first nontrivial scaled limit of the R16/R17 boundary-null remainder after
multiplication by \(U^2\), or an equivalent second-order Mosco/Schur-complement theorem.

R17 proves only

\[
D_U(z_U,z_U)\to0
\]

with no rate.  After the \(U\)-rescaling in R40.18 this is not enough to identify a constant.

Therefore R40 stops at the two-sided scale

\[
\Theta(U^{-2})
\]

for the squared dual norm.

This is the correct current scope.

---

## 7. Audit ledger and freeze

### Dependency source-check

As of 2026-09-02, the R40 dependency chain has been rechecked directly against the committed
canonical sources on the same research lineage:

- R5-JET: the fixed-window boundary expansion and the first-order coefficient used in
  (R40.4)--(R40.6) are source-verified; the separate R5 smooth-core self-containment issue is
  not used by R40;
- R16-B/D: the exact near-null vector satisfies \(\ell_U(z_U)=0\),
  \(D_U(z_U,z_U)=O(1)\), and bounded full graph energy;
- R17-C/D: the same near-null Schur core in fact satisfies \(D_U(z_U,z_U)\to0\), but with no
  quantitative rate; this supports the R40 firewall against claiming a limit constant;
- R24-A: \(A_X(U)\ge a_0I\) uniformly, exactly as used in Case B;
- R27: \(d_U=2U+O(1)\), the rank-one variational lower bound, and the hard-constraint
  inverse-root framework are source-verified;
- frozen R38: \(Q_U^*v_{S,U}=v_{R,U}\) is exactly (R38.9).

The variational identity (R40.3), the two-case lower bound (R40.9)--(R40.13), the normalized
R16 recovery vector (R40.14)--(R40.23), and the nested ratio estimate (R40.24)--(R40.27) were
also independently rederived against these definitions.  No R37/G4c input is used anywhere
in R40.

### Independent reviewer verification

An independent reviewer read the exact R40 blob
`7984fae11ab553cb19951ae9b5c0af08098d616a` on parent head
`0af33a6024d74e0e7a8f65bf8668c0d906d6cc86` and reported GREEN for R40.1--R40.25,
including both constrained-energy bounds and the uniform positive lower bound for the
R/S dual-normal ratio.

Accordingly R40 is now **FROZEN as independently verified AI-GREEN** on this research
lineage.  This is a governance/reviewer freeze only; it is **not** a canonical
\(\checkmark[M]\) promotion.

---

## 8. Strong-Terminal firewall

R40 does not prove:

- a limit for \(\widehat v_{X,U}\);
- a limit for \(\theta_U\);
- a strong limit for \(Q_U\);
- a strong limit for the actual future transport;
- any R22 baseline-gauge stabilization;
- Object X;
- RH.

It supplies the first quantitative next-order scale beneath the hard-constraint Mosco limit.
