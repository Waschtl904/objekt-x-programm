# P11 End-to-End Referee R26 — near-null survival of the concrete relative resolvents

Date: 2026-08-15

## Target

Test whether the R17 exact near-null construction implies a concrete statement about the relative resolvents appearing in R24/R25.

The potentially tempting route after R24 is to hope that the divergence of every fixed nonzero smooth odd source vector in the absolute terminal metric forces the relative resolvents or inverse roots to vanish strongly.  R26 audits this implication directly for the actual P11 family.

Fix
\[
0<R<S<T_0<U
\]
and work on the odd sector.  Write
\[
B_R:=G_{R,T_0}^-,\qquad C_R(U):=G_{R,U}^-,
\]
\[
A_R(U):=B_R^{-1/2}C_R(U)B_R^{-1/2}.
\]
Similarly define \(B_S,C_S(U),A_S(U)\).  Let
\[
W:=B_S^{1/2}J_{R,S}B_R^{-1/2}
\]
be the normalized baseline isometry.

## Verdict

The strong-resolvent-extinction route is false for the concrete P11 odd family.

Let \(f\in C_c^\infty((-R,R))_{\rm odd}\setminus\{0\}\) satisfy
\[
\beta_R^{(0)}(f)=0.
\]
By completeness of the odd boundary jet, \(f\) has a finite first nonzero jet order \(m>0\).  Choose a fixed smooth odd \(f_0\) with first jet order \(0\), and let
\[
z_U=f-\frac{\ell_U(f)}{\ell_U(f_0)}f_0.
\]
R17 gives
\[
z_U\to f
\]
in the fixed source graph space and
\[
q_U^X(J_{R,U}z_U)\to \gamma_f:=\mathfrak c_{\Gamma,R}[f]>0.
\]

Put
\[
x_f:=B_R^{1/2}f,\qquad y_U:=B_R^{1/2}z_U.
\]
Then
\[
y_U\to x_f,
\qquad
\langle A_R(U)y_U,y_U\rangle_{X,R}
=q_U^X(J_{R,U}z_U)\to\gamma_f,
\]
and
\[
\|x_f\|_{X,R}^2=q_{T_0}^X(J_{R,T_0}f)=:b_f>0.
\]
For every fixed \(t\ge0\), the variational identity for a positive invertible operator gives
\[
\langle(A_R(U)+tI)^{-1}x_f,x_f\rangle
=\sup_{y\ne0}
\frac{|\langle x_f,y\rangle|^2}
{\langle A_R(U)y,y\rangle+t\|y\|^2}.
\]
Testing with \(y=y_U\) yields
\[
\boxed{
\liminf_{U\to\infty}
\langle(A_R(U)+tI)^{-1}x_f,x_f\rangle
\ge
\frac{b_f^2}{\gamma_f+t b_f}>0.
}
\]
The same estimate holds at level \(S\) on the fixed vector \(Wx_f\):
\[
\boxed{
\liminf_{U\to\infty}
\langle(A_S(U)+tI)^{-1}Wx_f,Wx_f\rangle
\ge
\frac{b_f^2}{\gamma_f+t b_f}>0.
}
\]

At \(t=0\),
\[
\boxed{
\liminf_{U\to\infty}\|A_R(U)^{-1/2}x_f\|^2
\ge\frac{b_f^2}{\gamma_f}>0,
}
\]
and likewise for \(A_S(U)^{-1/2}Wx_f\).

Thus the concrete P11 relative inverse metrics retain nonzero mass on every fixed smooth higher-jet direction, despite the absolute terminal divergence
\[
q_U^X(J_{R,U}f)\to\infty.
\]
This is a genuine nonuniformity phenomenon: the moving near-null vector \(z_U=f+O(U^{-m})f_0\) converges to the fixed higher-jet vector while cancelling the dominant boundary channel.

## Canonical statuses

- [R26-A] higher-jet fixed-vector resolvent lower bound at source level \(R\): **✓[M]**.
- [R26-B] same lower bound at the canonically nested level \(S\): **✓[M]**.
- [R26-C] concrete strong-resolvent-extinction route \((A_X(U)+tI)^{-1}\to0\) on the odd sector is false: **✓[M]_neg**.
- [R26-D] concrete inverse-root survival \(A_X(U)^{-1/2}\not\to0\) strongly on higher-jet directions: **✓[M]**.
- [R26-E] absolute fixed-vector metric divergence does not imply inverse-metric extinction for the concrete P11 family: **✓[M]_neg**.
- [R26-F] the R25 positive resolvent difference
  \[
  \mathscr E_U(t)=W^*(A_S+tI)^{-1}W-(A_R+tI)^{-1}
  \]
  on fixed vectors remains **?[O]**.  R26 proves that both terms can survive; it does not decide their difference.

No conclusion about the polar gauge, strong terminal transport, or a global Object X follows.

---

## 1. Genericity of the higher-jet input

Let
\[
f\in C_c^\infty((-R,R))_{\rm odd}\setminus\{0\},
\qquad \beta_R^{(0)}(f)=0.
\]
The completeness theorem for the integral jets implies that there is a finite
\[
m=m(f)\ge1
\]
with
\[
\beta_R^{(0)}(f)=\cdots=\beta_R^{(m-1)}(f)=0,
\qquad
\beta_R^{(m)}(f)\ne0.
\]
Choose once and for all a smooth odd \(f_0\) with \(\beta_R^{(0)}(f_0)\ne0\).  The hypotheses of Proposition O3N (exact TC1 near-null direction) and Theorem O3P (vanishing near-null Schur core) therefore apply with \(f_m=f\).

They give
\[
z_U=f-\frac{\ell_U(f)}{\ell_U(f_0)}f_0,
\qquad
\frac{\ell_U(f)}{\ell_U(f_0)}=O(U^{-m}),
\]
so
\[
\boxed{z_U\to f}
\]
in the fixed finite-dimensional smooth source span, hence in the fixed \(X\)-graph norm.

R17 further gives
\[
\boxed{
q_U^X(J_{R,U}z_U)	o\gamma_f:=\mathfrak c_{\Gamma,R}[f]>0.
}
\tag{R26.1}
\]

---

## 2. Base-standardized coordinates

Put
\[
B_R:=G_{R,T_0}^-,\qquad C_R(U):=G_{R,U}^-,
\qquad A_R(U):=B_R^{-1/2}C_R(U)B_R^{-1/2}.
\]
For
\[
x_f:=B_R^{1/2}f,
\qquad
y_U:=B_R^{1/2}z_U,
\]
one has
\[
\boxed{y_U\to x_f.}
\tag{R26.2}
\]
Moreover, directly from the definition of the terminal metric,
\[
\begin{aligned}
\langle A_R(U)y_U,y_U\rangle_{X,R}
&=\langle C_R(U)z_U,z_U\rangle_{X,R}\\
&=q_U^X(J_{R,U}z_U)
\longrightarrow\gamma_f.
\end{aligned}
\tag{R26.3}
\]
At the fixed baseline
\[
\boxed{
\|x_f\|_{X,R}^2
=\langle B_Rf,f\rangle_{X,R}
=q_{T_0}^X(J_{R,T_0}f)
=:b_f>0.
}
\tag{R26.4}
\]
Hence
\[
\langle x_f,y_U\rangle\to b_f,
\qquad
\|y_U\|^2\to b_f.
\tag{R26.5}
\]

---

## 3. Fixed-vector resolvent survival

For every positive invertible operator \(A\), every \(t\ge0\), and every vector \(x\),
\[
\boxed{
\langle(A+tI)^{-1}x,x\rangle
=\sup_{y\ne0}
\frac{|\langle x,y\rangle|^2}
{\langle Ay,y\rangle+t\|y\|^2}.
}
\tag{R26.6}
\]
This is the standard variational formula obtained by writing the quotient as Cauchy--Schwarz after applying \((A+tI)^{\pm1/2}\), with equality at \(y=(A+tI)^{-1}x\).

Apply (R26.6) to \(A=A_R(U)\), \(x=x_f\), and use the admissible test vector \(y=y_U\).  Equations (R26.3)--(R26.5) give
\[
\begin{aligned}
\liminf_{U\to\infty}
\langle(A_R(U)+tI)^{-1}x_f,x_f\rangle
&\ge
\lim_{U\to\infty}
\frac{|\langle x_f,y_U\rangle|^2}
{\langle A_R(U)y_U,y_U\rangle+t\|y_U\|^2}\\
&=
\boxed{
\frac{b_f^2}{\gamma_f+t b_f}>0.
}
\end{aligned}
\tag{R26.7}
\]
This holds for every fixed \(t\ge0\).

At \(t=0\),
\[
\langle A_R(U)^{-1}x_f,x_f\rangle
=\|A_R(U)^{-1/2}x_f\|^2,
\]
so
\[
\boxed{
\liminf_{U\to\infty}
\|A_R(U)^{-1/2}x_f\|^2
\ge\frac{b_f^2}{\gamma_f}>0.
}
\tag{R26.8}
\]

---

## 4. Canonically nested target level

Let
\[
x_f^S:=B_S^{1/2}J_{R,S}f.
\]
The normalized baseline transition is
\[
W=B_S^{1/2}J_{R,S}B_R^{-1/2},
\]
hence
\[
\boxed{x_f^S=Wx_f.}
\tag{R26.9}
\]
By R17 source compatibility,
\[
z_U^S=J_{R,S}z_U^R.
\]
Therefore the corresponding standardized moving vector is
\[
y_U^S=B_S^{1/2}z_U^S=Wy_U.
\]
Since \(W\) is an isometry,
\[
\langle x_f^S,y_U^S\rangle\to b_f,
\qquad
\|y_U^S\|^2\to b_f.
\]
The terminal cocycle gives the same terminal vector at level \(U\), so
\[
\langle A_S(U)y_U^S,y_U^S\rangle
=q_U^X(J_{S,U}z_U^S)
=q_U^X(J_{R,U}z_U)
\to\gamma_f.
\]
The same variational argument yields
\[
\boxed{
\liminf_{U\to\infty}
\langle(A_S(U)+tI)^{-1}Wx_f,Wx_f\rangle
\ge\frac{b_f^2}{\gamma_f+t b_f}>0.
}
\tag{R26.10}
\]
and at \(t=0\)
\[
\boxed{
\liminf_{U\to\infty}
\|A_S(U)^{-1/2}Wx_f\|^2
\ge\frac{b_f^2}{\gamma_f}>0.
}
\tag{R26.11}
\]

---

## 5. Concrete nonuniformity: direct metric divergence versus inverse survival

For the same fixed nonzero smooth odd \(f\), the sharp odd terminal asymptotic gives
\[
q_U^X(J_{R,U}f)\asymp_f\frac{e^U}{U^{2m+2}}\to\infty.
\]
Equivalently,
\[
\langle A_R(U)x_f,x_f\rangle\to\infty.
\]
Nevertheless (R26.7)--(R26.8) show that
\[
(A_R(U)+tI)^{-1}x_f
\not\to0
\]
strongly for every fixed \(t\ge0\), and
\[
A_R(U)^{-1/2}x_f\not\to0.
\]
The same statement holds at level \(S\) on \(Wx_f\).

There is no contradiction: \(z_U=f+O(U^{-m})f_0\) is a moving direction that approaches \(f\) in the fixed source norm while exactly cancelling the dominant constant-mode boundary functional.  The future quadratic forms are therefore highly nonuniform in direction.  Pointwise divergence on fixed vectors does not control the inverse functional calculus.

This is an actual P11 result, not an abstract countermodel.

---

## 6. R25 firewall and remaining problem

R25 introduced
\[
\mathscr E_U(t)
=W^*(A_S(U)+tI)^{-1}W-(A_R(U)+tI)^{-1}\ge0.
\]
R26 shows that, on every fixed higher-jet vector \(x_f\), both terms in this difference have positive liminf.  Therefore R25-F cannot be resolved by a crude argument that each resolvent factor vanishes on the fixed smooth odd core.

But R26 does **not** determine the difference.  In particular it proves neither
\[
\langle\mathscr E_U(t)x_f,x_f\rangle\to0
\]
nor a positive limsup.  The genuine question is now a relative one: how much additional inverse-metric relaxation is gained by passing from the nested source range \(\Ran W\) to its complement inside the level-\(S\) future metric?

No statement about \(\Gamma_U\), \(\mathfrak P_U\), the R22 angle defect, strong terminal transport, or a global Object X is made.