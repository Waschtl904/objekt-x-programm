# P11 End-to-End Referee R28 — fixed Gamma crossblock and constraint-normal mismatch

Date: 2026-08-15

## Target

Continue R27 at fixed \(0<R<S<T_0\).  The terminal parameter has been removed from the R24/R25 inverse-functional-calculus branch.  Determine exactly what vanishing of the limiting inverse-root defect means at the fixed baseline.

No polar-gauge promotion is permitted.

## Verdict

There are two fixed geometric obstructions:

1. a tangential constrained-Gamma offblock on the effective higher-jet hyperplane;
2. a one-dimensional mismatch of the Riesz normals of the hard constraints \(\beta^{(0)}=0\).

On the effective higher-jet domain,
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
s_{R,S,T_0}=0.
}
\]
If \(s\ne0\),
\[
\boxed{
\|D_\infty^-\|
\ge
\frac{\|s\|}{\|r_S\|}>0.
}
\]
The tangential nullity and the normal-matching question remain open for the concrete fixed P11 baseline.

## Canonical statuses

- [R28-A] exact graph description of the constrained complement \(K\): **✓[M]**.
- [R28-B] exact prescribed-rank-one criterion for \(\mathscr C_\Gamma=0\): **✓[M]**.
- [R28-C] higher-jet equivalence \(D_\infty^-|_{V_R}=0\iff\mathscr C_\Gamma=0\): **✓[M]**.
- [R28-D] full-space equivalence \(D_\infty^-=0\iff(\mathscr C_\Gamma=0\ \&\ s=0)\): **✓[M]**.
- [R28-E] quantitative lower bound from the constraint-normal mismatch: **✓[M]**.
- [R28-F] decide \(\mathscr C_\Gamma\) and \(s\) for the concrete fixed P11 baseline: **?[O]**.

No conclusion about the R22 polar angle, strong terminal transport, or a global Object X follows.

---

## 1. Standardized constraint normals

For \(X\in\{R,S\}\), put
\[
B_X:=G_{X,T_0}^-.
\]
In baseline-whitened coordinates the normalized inclusion
\[
W:=B_S^{1/2}J_{R,S}B_R^{-1/2}
\]
is an isometry.  Define
\[
\widehat\beta_X(x):=\beta_X^{(0)}(B_X^{-1/2}x)
\]
and let \(r_X\) be its Riesz vector:
\[
\widehat\beta_X(x)=\langle x,r_X\rangle_X.
\]
Then
\[
V_X=r_X^\perp.
\tag{R28.1}
\]
Pullback compatibility gives
\[
W^*r_S=r_R.
\tag{R28.2}
\]
Let
\[
N:=\operatorname{Ran}W,
\qquad
G:=N^\perp,
\qquad
s:=(I-WW^*)r_S.
\tag{R28.3}
\]
Then
\[
\boxed{r_S=Wr_R+s,\qquad Wr_R\perp s,}
\tag{R28.4}
\]
so
\[
\|r_S\|^2=\|r_R\|^2+\|s\|^2.
\tag{R28.5}
\]

## 2. Exact graph complement

Set
\[
M:=WV_R,
\qquad
K:=V_S\cap M^\perp.
\]
Since
\[
N=M\oplus\mathbb C Wr_R,
\qquad
M^\perp=\mathbb C Wr_R\oplus G,
\]
every \(k\in K\) is uniquely of the form
\[
\boxed{
Tg
:=g-
\frac{\langle g,s\rangle}{\|r_R\|^2}Wr_R,
\qquad g\in G.
}
\tag{R28.6}
\]
Thus \(K=T(G)\) is a bounded graph over the ordinary full-range baseline complement \(G\).

## 3. Prescribed rank-one criterion

Let \(\Lambda_X\) be the full baseline-whitened Gamma Riesz operator,
\[
\langle\Lambda_Xx,y\rangle
=\widetilde{\mathfrak c}_{\Gamma,X}[x,y].
\]
The convention is the one used throughout P11: the form and Hilbert inner product are linear in the first argument.  Thus
\[
0<\Lambda_X\le I,
\qquad
W^*\Lambda_SW=\Lambda_R.
\tag{R28.7}
\]
Define
\[
\mathcal A_\Gamma
:=P_{V_R}W^*\Lambda_S|_G:G\to V_R,
\qquad
a_\Gamma:=P_{V_R}\Lambda_Rr_R.
\tag{R28.8}
\]
For \(f\in V_R\), \(g\in G\), sesquilinearity and (R28.6) give
\[
\boxed{
\widetilde{\mathfrak c}_{\Gamma,S}[Wf,Tg]
=\langle f,\mathcal A_\Gamma g\rangle
-
\frac{\langle s,g\rangle}{\|r_R\|^2}
\langle f,a_\Gamma\rangle.
}
\tag{R28.9}
\]
Equivalently,
\[
\boxed{
\mathscr C_\Gamma^{R,S,T_0}=0
\iff
\mathcal A_\Gamma g
=
\frac{\langle g,s\rangle}{\|r_R\|^2}a_\Gamma
\quad\forall g\in G.
}
\tag{R28.10}
\]
The two displayed coefficients are consistent because the second slot is conjugate-linear.  Thus nullity forces a prescribed rank-at-most-one crossoperator.  If \(s=0\),
\[
\mathscr C_\Gamma=0\iff\mathcal A_\Gamma=0.
\tag{R28.11}
\]

## 4. Tangential inverse-root equivalence

Let \(L_X\) be the constrained Gamma operator on \(V_X\):
\[
\langle L_Xx,y\rangle
=\widetilde{\mathfrak c}_{\Gamma,X}[x,y],
\qquad
a_0I\le L_X\le I.
\]
With respect to \(V_S=M\oplus K\),
\[
\boxed{
L_S=
\begin{pmatrix}
WL_RW^*&\mathscr C_\Gamma^*\\
\mathscr C_\Gamma&D
\end{pmatrix}.
}
\tag{R28.12}
\]
R27 gives, on the full standardized spaces,
\[
T_{X,\infty}=L_X^{-1/2}P_{V_X},
\qquad
D_\infty^-=T_{S,\infty}W-WT_{R,\infty}.
\tag{R28.13}
\]

If \(\mathscr C_\Gamma=0\), then \(L_SW=WL_R\) on \(V_R\), so functional calculus gives
\[
L_S^{-1/2}W=WL_R^{-1/2}.
\]
Conversely, if this inverse-root intertwining holds on \(V_R\), apply it to \(L_R^{1/2}x\), multiply by \(L_S^{1/2}\), and then once more by \(L_S^{1/2}\).  One obtains
\[
L_SWx=WL_Rx.
\]
Thus \(M\) is invariant under the selfadjoint \(L_S\), hence reducing, so its offblock vanishes.  Therefore
\[
\boxed{
D_\infty^-|_{V_R}=0
\iff
\mathscr C_\Gamma=0.
}
\tag{R28.14}
\]
This closes the converse that was not part of O3Z.14.

## 5. Full-space normal mismatch

Let
\[
e_R:=r_R/\|r_R\|.
\]
Then \(T_{R,\infty}e_R=0\), hence
\[
D_\infty^-e_R=L_S^{-1/2}P_{V_S}We_R.
\tag{R28.15}
\]
Because \(L_S\le I\), \(L_S^{-1/2}\ge I\).  Also
\[
\left|
\left\langle We_R,\frac{r_S}{\|r_S\|}\right\rangle
\right|
=\frac{\|r_R\|}{\|r_S\|},
\]
so
\[
\boxed{
\|P_{V_S}We_R\|^2
=1-\frac{\|r_R\|^2}{\|r_S\|^2}
=\frac{\|s\|^2}{\|r_S\|^2}.
}
\tag{R28.16}
\]
Therefore
\[
\boxed{
\|D_\infty^-e_R\|
\ge\frac{\|s\|}{\|r_S\|}.
}
\tag{R28.17}
\]
Thus \(D_\infty^-e_R=0\iff s=0\).  Combining with (R28.14),
\[
\boxed{
D_\infty^-=0
\iff
\mathscr C_\Gamma=0
\text{ and }s=0.
}
\tag{R28.18}
\]

## 6. Remaining concrete fixed problem

The R27 residue has split into two terminal-independent questions:

1. **tangential Gamma block**
   \[
   \mathcal A_\Gamma
   \stackrel{?}{=}
   \frac{a_\Gamma\otimes s^*}{\|r_R\|^2};
   \]
2. **constraint-normal matching**
   \[
   s=(I-WW^*)r_S\stackrel{?}{=}0.
   \]

Either nonvanishing result yields a persistent inverse-functional-calculus defect.  R14 still forbids promotion of such a modulus-layer result to the polar gauge without separate analysis.