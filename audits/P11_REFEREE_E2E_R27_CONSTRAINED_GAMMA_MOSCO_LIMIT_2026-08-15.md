# P11 End-to-End Referee R27 — constrained Gamma Mosco limit and fixed-window resolvent reduction

Date: 2026-08-15

## Target

Exploit the R17/R26 near-null geometry together with the uniform first boundary profile to determine whether the concrete odd terminal forms possess an extended variational limit even though the terminal metric operators diverge on every fixed nonzero smooth odd vector.

The target is Object-X terminal geometry, not RH.  No polar-gauge promotion is allowed.

## Verdict

For each fixed source level \(X\in\{R,S\}\), the pulled-back odd terminal quadratic forms
\[
a_{X,U}(f):=q_U^X(J_{X,U}f)
\]
on the fixed Hilbert space \(\mathcal K_{X,X}^-\) Mosco-converge to the closed extended quadratic form
\[
\boxed{
a_{X,\infty}(f)=
\begin{cases}
\mathfrak c_{\Gamma,X}[f],&\beta_X^{(0)}(f)=0,\\
+\infty,&\beta_X^{(0)}(f)\ne0.
\end{cases}}
\]
Thus the first boundary functional becomes a hard asymptotic constraint, while on its kernel the Schur contribution can be removed by the R17 moving near-null recovery sequence.

After whitening at the fixed baseline \(T_0\), the relative metric forms
\[
\widetilde a_{X,U}(x)=\langle A_X(U)x,x\rangle
\]
Mosco-converge to the transported Gamma form on the closed hyperplane
\[
V_X:=G_{X,T_0}^{1/2}\ker\beta_X^{(0)}.
\]
Consequently, for every fixed \(t\ge0\),
\[
\boxed{
(A_X(U)+tI)^{-1}\xrightarrow[s]{}\mathcal R_{X,\infty}(t),
}
\]
where \(\mathcal R_{X,\infty}(t)\) is the constrained Gamma Riesz resolvent on \(V_X\).  The case \(t=0\) is included because the limit form is uniformly coercive.

The inverse square roots also have strong limits:
\[
\boxed{
A_X(U)^{-1/2}\xrightarrow[s]{}T_{X,\infty}
:=\frac1\pi\int_0^\infty t^{-1/2}\mathcal R_{X,\infty}(t)\,dt.
}
\]
Therefore the R24 inverse-root intertwining defect and the R25 positive inverse-root compression defect possess strong limits:
\[
D_U^-:=A_S(U)^{-1/2}W-WA_R(U)^{-1/2}
\xrightarrow[s]{}
D_\infty^-:=T_{S,\infty}W-WT_{R,\infty},
\]
\[
\mathscr I_U=W^*D_U^-\xrightarrow[s]{}\mathscr I_\infty:=W^*D_\infty^-\ge0.
\]
Hence the R24/R25 asymptotic-existence problem is solved: the remaining issue is whether this fixed limit is zero.

On the higher-jet effective domain the zero question is equivalent to a fixed-window Gamma block-orthogonality condition.  Put
\[
V_0:=WV_R\subset V_S,
\qquad
K:=V_S\cap V_0^\perp
\]
with orthogonality in the baseline-whitened Hilbert metric.  Then, restricted to \(V_R\),
\[
W^*\mathcal R_{S,\infty}(t)W-\mathcal R_{R,\infty}(t)=0
\]
for one (equivalently every) \(t\ge0\) iff
\[
\boxed{
\widetilde{\mathfrak c}_{\Gamma,S}(Wx,k)=0
\quad\forall x\in V_R,\ k\in K.
}
\]
In original source variables this is a fixed \(T_0\) Gamma-cross-term question between canonically nested \(\beta^{(0)}=0\) profiles and their baseline-orthogonal complement.

This is a genuine reduction of the U->infinity inverse-root problem to a fixed-window operator block.  It still does not decide the polar factors \(U_R,U_S\), \(\Gamma_U\), or strong terminal transport.

## Canonical statuses

- [R27-A] odd pulled-back terminal forms Mosco-converge to Gamma with hard \(\beta^{(0)}=0\) constraint: **✓[M]**.
- [R27-B] baseline-whitened relative forms have the corresponding constrained Gamma Mosco limit: **✓[M]**.
- [R27-C] concrete relative resolvents \((A_X(U)+tI)^{-1}\) have strong constrained-Gamma limits for every fixed \(t\ge0\): **✓[M]**.
- [R27-D] concrete inverse square roots have strong limits; R24/R25 inverse-root defects therefore have strong limits: **✓[M]**.
- [R27-E] higher-jet zero-defect question is equivalent to a fixed-window Gamma block-orthogonality criterion: **✓[M]**.
- [R27-F] decide that fixed Gamma block for the concrete P11 baseline and then reconnect, separately, to the relative polar gauge: **?[O]**.

No global Object X is constructed here.

---

## 1. Fixed source Hilbert space and the candidate limit form

Fix \(X>0\) and work on
\[
\mathcal H_X:=\mathcal K_{X,X}^-.
\]
For \(U>X\), define
\[
 a_{X,U}(f):=q_U^X(J_{X,U}f).
\]
At every finite \(U\) this is a bounded positive quadratic form on \(\mathcal H_X\), represented by the terminal metric \(G_{X,U}^-\).

Let
\[
H_X^0:=\ker\beta_X^{(0)}\cap\mathcal H_X.
\]
The functional \(\beta_X^{(0)}\) is continuous on \(\mathcal H_X\): it is an \(L^2\) pairing with a fixed bounded kernel, while the graph norm dominates \(L^2\).  Thus \(H_X^0\) is a closed hyperplane.

Define the extended form
\[
\boxed{
 a_{X,\infty}(f)=
 \begin{cases}
 \mathfrak c_{\Gamma,X}[f],&f\in H_X^0,\\
 +\infty,&f\notin H_X^0.
 \end{cases}}
\tag{R27.1}
\]
At fixed \(X\), the Gamma graph norm and the \(X\)-graph norm are equivalent, so \(\mathfrak c_{\Gamma,X}\) is a continuous coercive quadratic form on \(\mathcal H_X\).  Therefore (R27.1) is a proper closed extended quadratic form.

---

## 2. Uniform first-boundary functional

On the old source window, the direct terminal bridge gives
\[
H_U\mathbf1_U(u)=-\operatorname{sgn}(u)\Phi_U(|u|)
\]
and
\[
\Phi_U(r)
=\sqrt2\,e^{U/2}U^{-1/2}
\int_0^r e^{-s/2}(1-s/U)^{-1/2}\,ds
+O_X(e^{U/2}e^{-c\sqrt U})
\]
uniformly for \(0\le r\le X\).  Hence, in \(L^2(-X,X)\),
\[
\boxed{
e^{-U/2}U^{1/2}H_U\mathbf1_U|_{(-X,X)}
\longrightarrow
-\sqrt2\,\operatorname{sgn}(u)I_0(|u|).
}
\tag{R27.2}
\]
Equivalently the normalized terminal functionals
\[
\lambda_{X,U}(f):=e^{-U/2}U^{1/2}\ell_U(f)
\]
converge in \(\mathcal H_X^*\)-norm to
\[
\boxed{
\lambda_{X,\infty}(f)=-\sqrt2\,\beta_X^{(0)}(f).
}
\tag{R27.3}
\]
The later sharp constant-mode calculation gives
\[
d_U=2U+O(1).
\tag{R27.4}
\]
For every source vector the elementary variational inequality gives
\[
\boxed{
a_{X,U}(f)
\ge\sigma_U(J_{X,U}f)
\ge\frac{|\ell_U(f)|^2}{d_U}.
}
\tag{R27.5}
\]

---

## 3. Mosco liminf

Let \(U_n\to\infty\) and \(f_n\rightharpoonup f\) weakly in \(\mathcal H_X\).

### Case 1: \(\beta_X^{(0)}(f)\ne0\)

The weakly convergent sequence is bounded.  By the dual-norm convergence (R27.3),
\[
\lambda_{X,U_n}(f_n)\to-\sqrt2\,\beta_X^{(0)}(f)\ne0.
\]
Thus for all large \(n\),
\[
|\ell_{U_n}(f_n)|\ge c_f e^{U_n/2}U_n^{-1/2}.
\]
Equations (R27.4)--(R27.5) give
\[
a_{X,U_n}(f_n)\ge c_f'\frac{e^{U_n}}{U_n^2}\to\infty.
\]
Hence
\[
\liminf_n a_{X,U_n}(f_n)=+\infty=a_{X,\infty}(f).
\]

### Case 2: \(\beta_X^{(0)}(f)=0\)

Exact Gamma compatibility and positivity of the Schur term give
\[
a_{X,U_n}(f_n)\ge\mathfrak c_{\Gamma,X}[f_n].
\]
The fixed Gamma norm is equivalent to the \(X\)-graph norm, hence its quadratic form is weakly lower semicontinuous on \(\mathcal H_X\). Therefore
\[
\liminf_n a_{X,U_n}(f_n)
\ge\mathfrak c_{\Gamma,X}[f]
=a_{X,\infty}(f).
\]

This proves the Mosco weak-liminf condition.

---

## 4. Strong recovery sequence

It suffices to construct recovery sequences for \(f\in H_X^0\).

First suppose
\[
f\in C_c^\infty((-X,X))_{\rm odd}\cap H_X^0.
\]
If \(f\ne0\), completeness of the odd jet gives a finite first nonzero order \(m>0\).  Choose a fixed smooth odd \(f_0\) with first jet order zero and define the R17 vector
\[
z_U(f):=f-\frac{\ell_U(f)}{\ell_U(f_0)}f_0.
\]
Then
\[
z_U(f)\to f
\quad\text{in }\mathcal H_X
\]
and R17 gives
\[
a_{X,U}(z_U(f))	o\mathfrak c_{\Gamma,X}[f].
\tag{R27.6}
\]
For \(f=0\), take the zero sequence.

Now let arbitrary \(f\in H_X^0\).  By the smooth odd core theorem choose smooth odd \(g_n\to f\) in \(\mathcal H_X\).  Fix smooth \(f_0\) with \(\beta_X^{(0)}(f_0)\ne0\) and put
\[
h_n:=g_n-
\frac{\beta_X^{(0)}(g_n)}{\beta_X^{(0)}(f_0)}f_0.
\]
Then \(h_n\in C_c^\infty\cap H_X^0\) and \(h_n\to f\).  Apply (R27.6) to each \(h_n\), and choose increasing thresholds \(U_n\) such that for all \(U\ge U_n\),
\[
\|z_U(h_n)-h_n\|_{X,X}<1/n,
\qquad
|a_{X,U}(z_U(h_n))-\mathfrak c_{\Gamma,X}[h_n]|<1/n.
\]
Let \(n(U)\to\infty\) sufficiently slowly and define
\[
f_U:=z_U(h_{n(U)}).
\]
Then
\[
f_U\to f,
\qquad
a_{X,U}(f_U)\to\mathfrak c_{\Gamma,X}[f].
\]
This is the Mosco strong-recovery condition.

Therefore
\[
\boxed{a_{X,U}\xrightarrow[M]{U\to\infty}a_{X,\infty}.}
\tag{R27.7}
\]

---

## 5. Baseline whitening and relative forms

Fix \(T_0>X\) and put
\[
B_X:=G_{X,T_0}^->0,
\qquad
A_X(U):=B_X^{-1/2}G_{X,U}^-B_X^{-1/2}.
\]
The fixed boundedly invertible map \(B_X^{1/2}\) is a strong and weak Hilbert-space homeomorphism.  Hence Mosco convergence is preserved under the change of variables
\[
x=B_X^{1/2}f.
\]
Put
\[
V_X:=B_X^{1/2}H_X^0
\]
and define
\[
\widetilde{\mathfrak c}_{\Gamma,X}[x,y]
:=\mathfrak c_{\Gamma,X}[B_X^{-1/2}x,B_X^{-1/2}y].
\]
Then
\[
\boxed{
\langle A_X(U)x,x\rangle
\xrightarrow[M]{}
\widetilde a_{X,\infty}(x)
:=
\begin{cases}
\widetilde{\mathfrak c}_{\Gamma,X}[x],&x\in V_X,\\
+\infty,&x\notin V_X.
\end{cases}}
\tag{R27.8}
\]
The fixed-baseline graph inequality gives
\[
\widetilde{\mathfrak c}_{\Gamma,X}[x]\ge a_0\|x\|^2,
\qquad
a_0=(1+\|H_{T_0}\|^2)^{-1},
\tag{R27.9}
\]
consistent with R24.

---

## 6. Strong limit of the concrete relative resolvents

For \(t\ge0\) and \(x\) in the standardized Hilbert space, let
\[
y_U:=(A_X(U)+tI)^{-1}x.
\]
It is the unique minimizer of
\[
F_{U,x,t}(y)
:=\langle A_X(U)y,y\rangle+t\|y\|^2-2\operatorname{Re}\langle x,y\rangle.
\]
Define \(\mathcal R_{X,\infty}(t)x\in V_X\) as the unique minimizer of
\[
F_{\infty,x,t}(y)
:=\widetilde{\mathfrak c}_{\Gamma,X}[y]
+t\|y\|^2-2\operatorname{Re}\langle x,y\rangle
\qquad(y\in V_X).
\]
Equivalently it is characterized by
\[
\boxed{
\widetilde{\mathfrak c}_{\Gamma,X}[\mathcal R_{X,\infty}(t)x,v]
+t\langle\mathcal R_{X,\infty}(t)x,v\rangle
=\langle x,v\rangle
\quad(v\in V_X).
}
\tag{R27.10}
\]
Coercivity (R27.9) gives uniqueness also at \(t=0\) and
\[
\|\mathcal R_{X,\infty}(t)\|\le(a_0+t)^{-1}.
\]

Mosco liminf plus a recovery sequence for the limiting minimizer gives convergence of minimum values.  Since every finite-U functional is uniformly \((a_0+t)\)-strongly convex,
\[
F_{U,x,t}(y)-F_{U,x,t}(y_U)
\ge(a_0+t)\|y-y_U\|^2.
\]
Applying this to a recovery sequence for the unique limiting minimizer proves
\[
\boxed{
(A_X(U)+tI)^{-1}x
\longrightarrow
\mathcal R_{X,\infty}(t)x
\quad\text{strongly for every fixed }x,\ t\ge0.
}
\tag{R27.11}
\]
This is a strong limit of the concrete resolvent family.  Because the effective limit form has the proper closed hyperplane \(V_X\) as its domain, we do not rebrand it as the resolvent of a densely defined selfadjoint operator on the whole standardized Hilbert space; (R27.10) is the canonical constrained-Riesz formulation.

---

## 7. Strong inverse-square-root limit

R24 gives the uniform lower bound \(A_X(U)\ge a_0I\).  Hence
\[
A_X(U)^{-1/2}
=\frac1\pi\int_0^\infty t^{-1/2}(A_X(U)+tI)^{-1}\,dt
\]
with the uniform integrable domination
\[
\left\|t^{-1/2}(A_X(U)+tI)^{-1}\right\|
\le\frac{t^{-1/2}}{a_0+t}.
\]
Using (R27.11) and dominated convergence for each vector gives
\[
\boxed{
A_X(U)^{-1/2}\xrightarrow[s]{}T_{X,\infty}
:=\frac1\pi\int_0^\infty t^{-1/2}\mathcal R_{X,\infty}(t)\,dt.
}
\tag{R27.12}
\]
Thus
\[
\boxed{
D_U^-:=A_S(U)^{-1/2}W-WA_R(U)^{-1/2}
\xrightarrow[s]{}
D_\infty^-:=T_{S,\infty}W-WT_{R,\infty}.
}
\tag{R27.13}
\]
By R25,
\[
\boxed{
\mathscr I_U=W^*D_U^-
\xrightarrow[s]{}
\mathscr I_\infty:=W^*D_\infty^-\ge0.
}
\tag{R27.14}
\]
Hence the existence part of R24-F/R25-F is resolved.  The remaining issue is the value of the fixed limit.

---

## 8. Fixed-window Gamma block criterion on the effective higher-jet domain

Put
\[
V_0:=WV_R\subset V_S,
\qquad
K:=V_S\cap V_0^\perp.
\]
Transition compatibility of \(\beta^{(0)}\) gives the inclusion.  Gamma compatibility gives
\[
\widetilde{\mathfrak c}_{\Gamma,S}[Wx,Wy]
=\widetilde{\mathfrak c}_{\Gamma,R}[x,y]
\qquad(x,y\in V_R).
\tag{R27.15}
\]
Since the limit Gamma form is bounded and coercive in the baseline-whitened Hilbert norm, it is represented on \(V_S\) by a bounded positive operator.  Relative to
\[
V_S=V_0\oplus K,
\]
write its block matrix as
\[
\begin{pmatrix}
W L_R W^*&C^*\\
C&D
\end{pmatrix},
\]
where the off-block is characterized by
\[
\langle C Wx,k\rangle
=\widetilde{\mathfrak c}_{\Gamma,S}[Wx,k].
\]
For a fixed \(t\ge0\), the block inverse / Schur-complement formula shows, on inputs \(x\in V_R\),
\[
W^*\mathcal R_{S,\infty}(t)W-\mathcal R_{R,\infty}(t)\ge0
\]
and it vanishes identically on \(V_R\) iff \(C=0\).  Therefore
\[
\boxed{
\left.
\bigl(W^*\mathcal R_{S,\infty}(t)W-\mathcal R_{R,\infty}(t)\bigr)
\right|_{V_R}=0
\iff
\widetilde{\mathfrak c}_{\Gamma,S}(WV_R,K)=0.
}
\tag{R27.16}
\]
The criterion is independent of \(t\).  If the cross block is nonzero, the limiting positive resolvent defect is nonzero; if it vanishes, the constrained Gamma resolvents intertwine on the effective higher-jet domain.

In original source variables this is the fixed-window question:

For \(f\in\ker\beta_R^{(0)}\) and \(h\in\ker\beta_S^{(0)}\) whose baseline-whitened representative is orthogonal to the nested \(R\)-hyperplane, does
\[
\mathfrak c_{\Gamma,S}[J_{R,S}f,h]
\]
vanish identically?

This is now a fixed \(R,S,T_0\) Dirichlet/Riesz-Gamma block question, not a U->infinity asymptotic question.

---

## 9. Firewall

R27 resolves an asymptotic existence problem on the modulus/inverse-functional-calculus layer.  It does not control the moving polar factors.  R14 remains decisive: exact modulus compatibility can coexist with nontrivial polar drift.  Therefore even if the fixed Gamma cross block in (R27.16) vanishes, R22-F remains separately open.

Conversely, a nonzero fixed Gamma cross block would prove a persistent inverse-root/modulus orientation defect, not by itself a persistent relative polar-gauge defect.

No conclusion about strong terminal transport or a global Object X is drawn.