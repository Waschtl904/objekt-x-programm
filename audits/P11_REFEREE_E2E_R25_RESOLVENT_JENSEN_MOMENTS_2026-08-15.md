# P11 End-to-End Referee R25 — positive resolvent Jensen kernel and inverse-root fixed-vector criterion

Date: 2026-08-15

## Target

Continue the R24-F analysis for the concrete odd P11 relative metrics at fixed
\[
0<R<S<T_0<U.
\]
Retain
\[
A_R:=A_{T_0,U}^{R,-},\qquad
A_S:=A_{T_0,U}^{S,-},\qquad
W:=W_{R,S,-}^{[T_0]},\qquad
P:=WW^*,
\]
with
\[
W^*A_SW=A_R,
\]
and the O3l/O3r off-block
\[
\mathscr B_U:=(I-P)A_SW=A_SW-WA_R.
\]
R24 proved the uniform P11 coercivity
\[
a_0I\le A_R,A_S,
\qquad
a_0=(1+\|H_{T_0}\|^2)^{-1}>0,
\]
and the inverse-root resolvent bridge
\[
A_S^{-1/2}W-WA_R^{-1/2}
=-\frac1\pi\int_0^\infty t^{-1/2}
(A_S+tI)^{-1}\mathscr B_U(A_R+tI)^{-1}\,dt.
\]
The R25 question is whether the vector-valued integral admits a positive source-space reformulation that removes cancellation in the spectral parameter and gives a fixed-vector criterion suitable for strong convergence.

## Verdict

Yes.  The source compression of the resolvent quasi-commutator has an exact positive Gram factorization.  Put
\[
R_R(t):=(A_R+tI)^{-1},\qquad
R_S(t):=(A_S+tI)^{-1}.
\]
Then
\[
\boxed{
\mathscr E_U(t)
:=W^*R_S(t)W-R_R(t)
=R_R(t)\mathscr B_U^*R_S(t)\mathscr B_U R_R(t)\ge0.
}
\]
Thus three previously separate functional-calculus defects are moments of one and the same positive operator-valued kernel:
\[
\boxed{
A_R^{1/2}-W^*A_S^{1/2}W
=\frac1\pi\int_0^\infty t^{1/2}\mathscr E_U(t)\,dt,
}
\]
\[
\boxed{
\mathscr L_U
:=\log A_R-W^*(\log A_S)W
=\int_0^\infty\mathscr E_U(t)\,dt\ge0,
}
\]
\[
\boxed{
\mathscr I_U
:=W^*A_S^{-1/2}W-A_R^{-1/2}
=\frac1\pi\int_0^\infty t^{-1/2}\mathscr E_U(t)\,dt\ge0.
}
\]
For every fixed source vector \(f\), the R24 inverse-root intertwining defect
\[
D_U^-:=A_S^{-1/2}W-WA_R^{-1/2}
\]
satisfies
\[
\boxed{
\|D_U^-f\|^2
\le a_0^{-1/2}\langle\mathscr I_Uf,f\rangle,
\qquad
\mathscr I_U=W^*D_U^-.
}
\]
Hence
\[
\boxed{
D_U^-f\to0
\iff
\langle\mathscr I_Uf,f\rangle\to0
}
\]
for every fixed \(f\).  Since \(\|D_U^-\|\le2a_0^{-1/2}\) uniformly, convergence on a fixed dense core is equivalent to strong inverse-root compatibility.

The logarithmic defect \(\mathscr L_U\) is intrinsically scale-invariant under common rescaling \((A_R,A_S)\mapsto(cA_R,cA_S)\).  Moreover
\[
\mathscr L_U=0\iff \mathscr B_U=0\iff Q=W,
\]
so it is an exact modulus-layer defect.  The actual P11 O3l witness implies the new quantitative bound
\[
\boxed{
\|\mathscr L_U\|\gtrsim U^{-2m_h-2}.
}
\]
This is a scale-invariant polynomial lower witness for a resolvent/logarithmic modulus defect.

None of these statements promotes to the polar gauge.  R14 already has \(Q=W\) (hence \(\mathscr B_U=\mathscr L_U=\mathscr I_U=0\)) with nontrivial polar gauge, while R19/R20 provide modulus-active models with zero relative polar defect.  Therefore R25 improves the R24 modulus/inverse-root analysis but does not settle R22-F.

## Canonical statuses

- [R25-A] exact positive resolvent compression factorization: **✓[M]**.
- [R25-B] square-root, logarithmic, and inverse-root Jensen defects are three moments of the same positive kernel: **✓[M]**.
- [R25-C] fixed-vector/dense-core criterion for inverse-root compatibility via \(\mathscr I_U\): **✓[M]**.
- [R25-D] scale-invariant logarithmic defect and concrete P11 polynomial norm lower bound: **✓[M]**.
- [R25-E] promotion of these modulus/Jensen defects to the relative polar gauge: **✓[M]_neg** by the existing R14/R19/R20 countermodels.
- [R25-F] concrete fixed-vector asymptotics of \(\langle\mathscr I_Uf,f\rangle\) and the spectral distribution of the positive resolvent defect measure: **?[O]**.

No conclusion about \(\Gamma_U\to I\), the cross-terminal kernel, strong terminal transport, or a global Object X follows.

---

## 1. Exact positive resolvent compression factorization

The resolvent quasi-commutator follows from
\[
(A_S+tI)W-W(A_R+tI)=\mathscr B_U:
\]
\[
\boxed{
R_S(t)W-WR_R(t)
=-R_S(t)\mathscr B_UR_R(t).
}
\tag{R25.1}
\]
Taking adjoints gives
\[
W^*R_S(t)-R_R(t)W^*
=-R_R(t)\mathscr B_U^*R_S(t).
\tag{R25.2}
\]
Define
\[
\mathscr E_U(t):=W^*R_S(t)W-R_R(t).
\]
From (R25.2),
\[
\mathscr E_U(t)
=-R_R(t)\mathscr B_U^*R_S(t)W.
\]
Now substitute (R25.1):
\[
R_S(t)W
=WR_R(t)-R_S(t)\mathscr B_UR_R(t).
\]
Since \(\mathscr B_U^*W=0\),
\[
\boxed{
\mathscr E_U(t)
=R_R(t)\mathscr B_U^*R_S(t)\mathscr B_UR_R(t).
}
\tag{R25.3}
\]
Equivalently
\[
\boxed{
\mathscr E_U(t)
=\bigl(R_S(t)^{1/2}\mathscr B_UR_R(t)\bigr)^*
 \bigl(R_S(t)^{1/2}\mathscr B_UR_R(t)\bigr)
\ge0.
}
\tag{R25.4}
\]
This is the exact Jensen resolvent defect for the isometric compression \(W^*(\cdot)W\).

---

## 2. Three moments of one positive kernel

For positive invertible \(A\), norm-convergent functional-calculus formulas give
\[
A^{-1/2}
=\frac1\pi\int_0^\infty t^{-1/2}(A+tI)^{-1}\,dt,
\]
\[
A^{1/2}
=\frac1\pi\int_0^\infty t^{-1/2}A(A+tI)^{-1}\,dt,
\]
and, after cancellation of the scalar term,
\[
\log A
=\int_0^\infty\left(\frac1{1+t}I-(A+tI)^{-1}\right)dt.
\]
Using (R25.3) yields
\[
\boxed{
\mathscr J_U
:=A_R^{1/2}-W^*A_S^{1/2}W
=\frac1\pi\int_0^\infty t^{1/2}\mathscr E_U(t)\,dt\ge0.
}
\tag{R25.5}
\]
This is exactly the raw square-root Jensen gap underlying the existing normalized \(\Theta\).

Likewise
\[
\boxed{
\mathscr L_U
:=\log A_R-W^*(\log A_S)W
=\int_0^\infty\mathscr E_U(t)\,dt\ge0,
}
\tag{R25.6}
\]
and
\[
\boxed{
\mathscr I_U
:=W^*A_S^{-1/2}W-A_R^{-1/2}
=\frac1\pi\int_0^\infty t^{-1/2}\mathscr E_U(t)\,dt\ge0.
}
\tag{R25.7}
\]
All integrals converge in operator norm because \(A_R,A_S\ge a_0I\) and, for large \(t\), the Gram kernel is \(O(t^{-3})\) in norm.

For each fixed \(f\), define the positive scalar measure
\[
d\mu_{U,f}(t):=\langle\mathscr E_U(t)f,f\rangle\,dt.
\]
Then
\[
\langle\mathscr J_Uf,f\rangle
=\frac1\pi\int t^{1/2}d\mu_{U,f}(t),
\]
\[
\langle\mathscr L_Uf,f\rangle
=\int d\mu_{U,f}(t),
\]
\[
\langle\mathscr I_Uf,f\rangle
=\frac1\pi\int t^{-1/2}d\mu_{U,f}(t).
\]
In particular Cauchy--Schwarz gives the scalar moment interpolation
\[
\boxed{
\langle\mathscr L_Uf,f\rangle^2
\le
\pi^2\langle\mathscr J_Uf,f\rangle
       \langle\mathscr I_Uf,f\rangle.
}
\tag{R25.8}
\]
No converse asymptotic implication is asserted without spectral localization of \(\mu_{U,f}\).

---

## 3. Positive fixed-vector criterion for R24-F

Put
\[
D_U^-:=A_S^{-1/2}W-WA_R^{-1/2}.
\]
R24 gives
\[
D_U^-
=-\frac1\pi\int_0^\infty t^{-1/2}
R_S(t)\mathscr B_UR_R(t)\,dt.
\tag{R25.9}
\]
For a fixed \(f\), (R25.4) and \(R_S(t)^2\le(a_0+t)^{-1}R_S(t)\) imply
\[
\|R_S(t)\mathscr B_UR_R(t)f\|^2
\le
(a_0+t)^{-1}\langle\mathscr E_U(t)f,f\rangle.
\]
Cauchy--Schwarz in the \(t\)-integral gives
\[
\begin{aligned}
\|D_U^-f\|^2
&\le
\frac1{\pi^2}
\left(\int_0^\infty t^{-1/2}
\langle\mathscr E_U(t)f,f\rangle\,dt\right)
\left(\int_0^\infty\frac{t^{-1/2}}{a_0+t}\,dt\right)\\
&=
\boxed{a_0^{-1/2}\langle\mathscr I_Uf,f\rangle}.
\end{aligned}
\tag{R25.10}
\]
On the other hand, directly
\[
\boxed{
\mathscr I_U=W^*D_U^-.
}
\tag{R25.11}
\]
Therefore for every fixed source vector
\[
\boxed{
D_U^-f\to0
\iff
\langle\mathscr I_Uf,f\rangle\to0.
}
\tag{R25.12}
\]
Indeed the reverse implication follows from (R25.10); the forward implication follows from
\[
|\langle\mathscr I_Uf,f\rangle|
=|\langle D_U^-f,Wf\rangle|
\le\|D_U^-f\|\,\|f\|.
\]
Furthermore
\[
\|D_U^-\|
\le\|A_S^{-1/2}\|+\|A_R^{-1/2}\|
\le2a_0^{-1/2}
\]
uniformly in \(U\).  Hence if (R25.12) holds on any fixed dense source core, then \(D_U^-\to0\) strongly on the entire source Hilbert space.

This is strictly better suited to R24-F than the original vector integral: the positive scalar quantity \(\langle\mathscr I_Uf,f\rangle\) contains no cancellation in the spectral parameter.

---

## 4. Scale-invariant logarithmic defect

Under a common rescaling
\[
(A_R,A_S)\mapsto(cA_R,cA_S),\qquad c>0,
\]
one has
\[
\log(cA_R)-W^*\log(cA_S)W
=\log A_R-W^*\log A_SW,
\]
so
\[
\boxed{\mathscr L_U\text{ is scale invariant}.}
\tag{R25.13}
\]
By (R25.6), \(\mathscr L_U=0\) iff \(\mathscr E_U(t)=0\) for all \(t\), hence iff \(\mathscr B_U=0\).  Since \(A_S\) is selfadjoint, \(\mathscr B_U=0\) means \(\Ran W\) reduces \(A_S\), and therefore
\[
A_S^{1/2}W=WA_R^{1/2},
\qquad Q=W.
\]
Conversely \(Q=W\) implies \(A_S^{1/2}W=WA_R^{1/2}\), hence \(A_SW=WA_R\), so \(\mathscr B_U=0\).  Thus
\[
\boxed{
\mathscr L_U=0
\iff
\mathscr B_U=0
\iff
Q=W.
}
\tag{R25.14}
\]
This is an exact modulus statement, not a polar statement.

---

## 5. Concrete P11 polynomial lower witness for the log defect

Let
\[
M_U:=\max(\|A_R\|,\|A_S\|)=\|A_S\|.
\]
Choose a unit vector \(f_U\) with
\[
\|\mathscr B_Uf_U\|\ge\frac12\|\mathscr B_U\|.
\]
For \(t\ge4M_U\),
\[
\|R_R(t)-t^{-1}I\|\le\frac{M_U}{t^2},
\]
so
\[
\|\mathscr B_UR_R(t)f_U\|
\ge
\frac{\|\mathscr B_U\|}{4t}.
\]
Also
\[
R_S(t)\ge(M_U+t)^{-1}I.
\]
Therefore
\[
\langle\mathscr E_U(t)f_U,f_U\rangle
\ge
\frac{\|\mathscr B_U\|^2}{16t^2(M_U+t)}.
\]
Integrating only over \([4M_U,8M_U]\) gives a universal \(c_*>0\) such that
\[
\boxed{
\|\mathscr L_U\|
\ge
c_*\frac{\|\mathscr B_U\|^2}{M_U^2}.
}
\tag{R25.15}
\]
For the actual P11 family, O3l gives
\[
\|\mathscr B_U\|
\gtrsim\frac{e^U}{U^{m_h+2}},
\]
while
\[
M_U\ll\frac{e^U}{U}.
\]
Hence
\[
\boxed{
\|\mathscr L_U\|
\gtrsim U^{-2m_h-2}.
}
\tag{R25.16}
\]
This lower scale tends to zero, so it does not rule out \(\mathscr L_U\to0\).  It rules out faster operator-norm decay and supplies a scale-invariant positive resolvent witness for the concrete P11 modulus geometry.

---

## 6. Countermodel firewall and the remaining gate

The R25 observables remain on the modulus/functional-calculus layer.

- In the R14 perfect-modulus countermodel, \(Q=W\), hence by (R25.14)
  \[
  \mathscr B_U=\mathscr E_U(t)=\mathscr L_U=\mathscr I_U=0,
  \]
  while the actual polar gauge is nontrivial.
- In the R19 modulus-active countermodel, \(\mathscr B_U\ne0\), so the new Jensen defects detect the modulus activity, while polar leakage is zero.
- The R20 combined model likewise permits nonzero modulus/Jensen defects together with zero relative polar defect.

Therefore no estimate on \(\mathscr E_U(t)\), \(\mathscr L_U\), or \(\mathscr I_U\) alone can be promoted to a theorem about
\[
\mathfrak P_U=U_SW-WU_R
\]
by abstract algebra.

The genuine next analytic question on the R24/R25 branch is now the positive fixed-vector problem
\[
\boxed{
\langle\mathscr I_Uf,f\rangle
=\frac1\pi\int_0^\infty t^{-1/2}
\|R_S(t)^{1/2}\mathscr B_UR_R(t)f\|^2dt
\stackrel{?}{\longrightarrow}0
}
\]
for each fixed smooth odd \(f\), or the construction of a fixed \(f\) and subsequence with positive limsup.

This solves no polar-gauge asymptotic and no terminal-limit problem, but it replaces the cancellation-prone R24 vector integral by a canonically positive scalar observable.