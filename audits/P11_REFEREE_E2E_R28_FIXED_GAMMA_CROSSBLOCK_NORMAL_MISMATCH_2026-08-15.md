# P11 End-to-End Referee R28 — fixed Gamma crossblock and constraint-normal mismatch

Date: 2026-08-15

## Target

Continue R27 at fixed \(0<R<S<T_0\).  The terminal parameter has been removed from the R24/R25 inverse-functional-calculus branch.  The remaining task is to understand the fixed constrained-Gamma geometry and to determine exactly what vanishing of the limiting inverse-root defect means.

No polar-gauge promotion is permitted.

## Verdict

There are **two** fixed geometric obstructions, not one:

1. a tangential constrained-Gamma offblock on the effective higher-jet hyperplane;
2. a one-dimensional mismatch of the Riesz normals of the hard constraints \(\beta^{(0)}=0\).

On the effective higher-jet domain the converse left open after R27 is now proved:
\[
\boxed{
D_\infty^-|_{V_R}=0
\iff
\mathscr C_\Gamma^{R,S,T_0}=0.
}
\]
On the full standardized source space,
\[
\boxed{
D_\infty^-=0
\iff
\mathscr C_\Gamma^{R,S,T_0}=0
\quad\text{and}\quad
s_{R,S,T_0}=0,
}
\]
where \(s_{R,S,T_0}\) is the component of the target constraint normal orthogonal to the normalized baseline range.

If this normal mismatch is nonzero, it already gives the quantitative lower bound
\[
\boxed{
\|D_\infty^-\|
\ge
\frac{\|s_{R,S,T_0}\|}{\|r_S\|}>0.
}
\]
Thus the full R27 inverse-root limit can fail to intertwine even if the tangential Gamma offblock vanishes.

The tangential nullity itself remains open for the concrete P11 baseline.  R28 reduces it further to a prescribed rank-one identity for a fixed Gamma crossoperator from the full baseline complement.

## Canonical statuses

- [R28-A] exact graph description of the constrained complement \(K\): **✓[M]**.
- [R28-B] exact prescribed-rank-one criterion for \(\mathscr C_\Gamma=0\): **✓[M]**.
- [R28-C] higher-jet equivalence \(D_\infty^-|_{V_R}=0\iff\mathscr C_\Gamma=0\): **✓[M]**.
- [R28-D] full-space equivalence \(D_\infty^-=0\iff(\mathscr C_\Gamma=0\ \&\ s=0)\): **✓[M]**.
- [R28-E] quantitative lower bound from the constraint-normal mismatch: **✓[M]**.
- [R28-F] decide \(\mathscr C_\Gamma\) and \(s\) for the concrete fixed P11 baseline: **?[O]**.

No conclusion about the R22 polar angle, strong terminal transport, or a global Object X follows.

---

## 1. Standardized fixed-baseline notation

For \(X\in\{R,S\}\), put
\[
B_X:=G_{X,T_0}^-,
\]
and work in the baseline-whitened source Hilbert space.  Thus the normalized inclusion
\[
W:=B_S^{1/2}J_{R,S}B_R^{-1/2}
\]
is an isometry.

Transport the first boundary functional to standardized coordinates:
\[
\widehat\beta_X(x):=\beta_X^{(0)}(B_X^{-1/2}x).
\]
Let \(r_X\) be its Riesz vector:
\[
\widehat\beta_X(x)=\langle x,r_X\rangle_X.
\]
Then the R27 effective hyperplane is
\[
\boxed{V_X=r_X^\perp.}
\tag{R28.1}
\]
Pullback compatibility of \(\beta^{(0)}\) gives
\[
\widehat\beta_S(Wx)=\widehat\beta_R(x),
\]
hence
\[
\boxed{W^*r_S=r_R.}
\tag{R28.2}
\]

Put
\[
N:=\operatorname{Ran}W,
\qquad
G:=N^\perp,
\qquad
s:=(I-WW^*)r_S\in G.
\tag{R28.3}
\]
Then
\[
\boxed{r_S=Wr_R+s,\qquad Wr_R\perp s.}
\tag{R28.4}
\]
In particular
\[
\|r_S\|^2=\|r_R\|^2+\|s\|^2.
\tag{R28.5}
\]
The vector \(s=s_{R,S,T_0}\) is the **constraint-normal mismatch**.

---

## 2. Exact graph description of the R27 complement

Inside \(V_S\), define
\[
M:=WV_R,
\qquad
K:=V_S\cap M^\perp.
\]
Since
\[
N=M\oplus\mathbb C Wr_R
\]
orthogonally, one has
\[
M^\perp=\mathbb C Wr_R\oplus G.
\]
Thus every \(k\in K\) has the form
\[
k=aWr_R+g,
\qquad g\in G.
\]
The constraint \(k\perp r_S\), together with (R28.4), gives
\[
a\|r_R\|^2+\langle g,s\rangle=0.
\]
Therefore
\[
\boxed{
K
=
\left\{
Tg:=g-
\frac{\langle g,s\rangle}{\|r_R\|^2}Wr_R
:\ g\in G
\right\}.
}
\tag{R28.6}
\]
The projection \(P_G:K\to G\) is the inverse of \(T\), so \(K\) is a bounded graph over the ordinary full-range baseline complement \(G\).  This proves [R28-A].

---

## 3. Prescribed rank-one reformulation of the Gamma offblock

Let \(\Lambda_X\) denote the bounded baseline-whitened Gamma Riesz operator on the full standardized source space:
\[
\langle\Lambda_Xx,y\rangle
=\widetilde{\mathfrak c}_{\Gamma,X}[x,y].
\]
Since the fixed baseline form is Gamma plus a positive Schur term,
\[
0<\Lambda_X\le I.
\tag{R28.7}
\]
Gamma pullback compatibility gives
\[
W^*\Lambda_SW=\Lambda_R.
\tag{R28.8}
\]

Let \(P_{V_R}\) be the orthogonal projection onto \(V_R\), and define the fixed crossoperator
\[
\boxed{
\mathcal A_\Gamma
:=P_{V_R}W^*\Lambda_S|_G:G\to V_R,
}
\tag{R28.9}
\]
and
\[
\boxed{
a_\Gamma:=P_{V_R}\Lambda_Rr_R\in V_R.}
\tag{R28.10}
\]
For \(f\in V_R\) and \(g\in G\), (R28.6) gives
\[
\begin{aligned}
\widetilde{\mathfrak c}_{\Gamma,S}[Wf,Tg]
&=\langle f,\mathcal A_\Gamma g\rangle\\
&\quad-
\frac{\langle g,s\rangle}{\|r_R\|^2}
\langle f,a_\Gamma\rangle.
\end{aligned}
\tag{R28.11}
\]
Therefore the R27 constrained-Gamma offblock vanishes iff
\[
\boxed{
\mathscr C_\Gamma^{R,S,T_0}=0
\iff
\mathcal A_\Gamma g
=
\frac{\langle g,s\rangle}{\|r_R\|^2}a_\Gamma
\quad\forall g\in G.
}
\tag{R28.12}
\]
Thus nullity forces the full Gamma crossoperator from \(G\) into the higher-jet source hyperplane to have rank at most one, with a **prescribed** right functional \(g\mapsto\langle g,s\rangle\) and prescribed range direction \(a_\Gamma\).  If \(s=0\), the criterion simplifies to
\[
\mathscr C_\Gamma=0\iff\mathcal A_\Gamma=0.
\tag{R28.13}
\]
This proves [R28-B].

---

## 4. The constrained Gamma operators

Let \(L_X\) be the bounded positive operator on \(V_X\) represented by the R27 limiting Gamma form:
\[
\langle L_Xx,y\rangle
=\widetilde{\mathfrak c}_{\Gamma,X}[x,y],
\qquad x,y\in V_X.
\]
R27 gives
\[
a_0I\le L_X\le I.
\tag{R28.14}
\]
With respect to
\[
V_S=M\oplus K,
\qquad M=WV_R,
\]
write
\[
\boxed{
L_S=
\begin{pmatrix}
WL_RW^*&\mathscr C_\Gamma^*\\
\mathscr C_\Gamma&D
\end{pmatrix}.
}
\tag{R28.15}
\]
The upper-left identity follows from Gamma compatibility.

R27 identified the strong inverse-root limits as
\[
T_{X,\infty}=L_X^{-1/2}P_{V_X}
\tag{R28.16}
\]
when viewed on the full standardized source Hilbert space.  Hence
\[
D_\infty^-=T_{S,\infty}W-WT_{R,\infty}.
\tag{R28.17}
\]

---

## 5. Exact converse on the higher-jet domain

### Proposition
\[
\boxed{
D_\infty^-|_{V_R}=0
\iff
\mathscr C_\Gamma^{R,S,T_0}=0.
}
\tag{R28.18}
\]

### Proof
If \(\mathscr C_\Gamma=0\), (R28.15) is block diagonal and
\[
L_S W=WL_R
\quad\text{on }V_R.
\]
Continuous functional calculus gives
\[
L_S^{-1/2}W=WL_R^{-1/2},
\]
so (R28.18) follows in one direction.

Conversely suppose
\[
L_S^{-1/2}W=WL_R^{-1/2}
\quad\text{on }V_R.
\tag{R28.19}
\]
For \(x\in V_R\), apply (R28.19) to \(L_R^{1/2}x\):
\[
L_S^{-1/2}WL_R^{1/2}x=Wx.
\]
Since \(L_S^{1/2}\) is bounded and invertible on \(V_S\),
\[
WL_R^{1/2}x=L_S^{1/2}Wx.
\]
Applying \(L_S^{1/2}\) once more gives
\[
\boxed{L_SWx=WL_Rx.}
\tag{R28.20}
\]
Thus \(M=WV_R\) is invariant under the selfadjoint \(L_S\), hence reducing, and the offblock in (R28.15) is zero.  This proves the converse and [R28-C].

This is a new theorem; it was not contained in O3Z.14, which only established the corresponding resolvent-block criterion.

---

## 6. The full source space has one additional obstruction

Let
\[
e_R:=\frac{r_R}{\|r_R\|}.
\]
Then
\[
\mathcal H_R=V_R\oplus\mathbb Ce_R.
\]
Since \(T_{R,\infty}e_R=0\),
\[
D_\infty^-e_R
=L_S^{-1/2}P_{V_S}We_R.
\tag{R28.21}
\]
Because \(L_S\le I\) on \(V_S\),
\[
L_S^{-1/2}\ge I.
\tag{R28.22}
\]
The angle between \(We_R\) and the target normal \(r_S\) is determined by (R28.2):
\[
\left|
\left\langle We_R,\frac{r_S}{\|r_S\|}\right\rangle
\right|
=\frac{\|r_R\|}{\|r_S\|}.
\]
Hence
\[
\boxed{
\|P_{V_S}We_R\|^2
=1-\frac{\|r_R\|^2}{\|r_S\|^2}
=\frac{\|s\|^2}{\|r_S\|^2}.
}
\tag{R28.23}
\]
Combining (R28.21)--(R28.23),
\[
\boxed{
\|D_\infty^-e_R\|
\ge\frac{\|s\|}{\|r_S\|}.
}
\tag{R28.24}
\]
Therefore \(D_\infty^-e_R=0\) iff \(s=0\), equivalently iff
\[
r_S=Wr_R.
\tag{R28.25}
\]

Together with (R28.18),
\[
\boxed{
D_\infty^-=0\text{ on the full standardized source space}
\iff
\mathscr C_\Gamma=0
\text{ and }
s=0.
}
\tag{R28.26}
\]
This proves [R28-D] and [R28-E].

---

## 7. Interpretation and remaining fixed problem

R28 separates the fixed R27 residue into two geometrically different layers:

- **tangential higher-jet layer:** \(\mathscr C_\Gamma\), measuring failure of the nested constrained-Gamma hyperplane to reduce the limiting Gamma operator;
- **constraint-normal layer:** \(s=(I-WW^*)r_S\), measuring whether the hard first-boundary constraint itself has compatible Riesz normals under source enlargement.

The previous shorthand “decide the Gamma crossblock” is therefore complete only for the higher-jet sector.  The full inverse-root limit intertwines iff both fixed obstructions vanish.

The remaining concrete P11 tasks are now entirely fixed-window:

1. decide whether
   \[
   \mathcal A_\Gamma
   =\frac{a_\Gamma\otimes s^*}{\|r_R\|^2};
   \]
2. decide whether
   \[
   s=(I-WW^*)r_S
   \]
   vanishes.

Either nonvanishing result gives a persistent **inverse-functional-calculus** defect.  By the R14 firewall it still does not imply a persistent relative polar defect.

No strong terminal transport or global Object-X conclusion is asserted.