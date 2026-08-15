# P11 End-to-End Referee R22 — strong-gauge angle defect and moving-gauge firewall

Date: 2026-08-15

## Target

Audit the proposed R22 shift from operator-norm witnesses to fixed-vector / strong-topology diagnostics after R21.  The initial candidate was
\[
D_U:=(Z_U-W)^*(Z_U-W),
\qquad
Z_U=U_S^*WU_R,
\]
with the hope that fixed-vector control of \(D_U\) would directly decide the R15 strong gauge gate.

The audit must distinguish the three related operators
\[
V_U:=U_SWU_R^*,
\qquad
\mathfrak P_U:=U_SW-WU_R,
\qquad
Z_U:=U_S^*WU_R,
\]
and must respect the O3t warning that \(U_R\) depends on the terminal parameter \(U\).

## Verdict

The fixed-vector strategy is correct, but the **primary R22 angle defect must be built from the R15 gauge isometry \(V_U\), not from \(Z_U\)**.

Define
\[
\boxed{
\mathscr G_U:=(V_U-W)^*(V_U-W).
}
\]
Since \(V_U\) and \(W\) are isometries and \(\Gamma_U=W^*V_U\),
\[
\boxed{
\mathscr G_U=2I-\Gamma_U-\Gamma_U^*.
}
\]
Thus
\[
\boxed{
\langle \mathscr G_U f,f\rangle
=\|(V_U-W)f\|^2.
}
\]
This is the correct fixed-vector diagnostic for the R15 strong gate
\[
\Gamma_U\xrightarrow[s]{}I
\iff
V_U\xrightarrow[s]{}W.
\]
Moreover \(0\le \mathscr G_U\le4I\), so convergence of this quadratic form on any fixed dense source core is sufficient and necessary for strong gauge convergence on the whole source space.

The initially proposed operator
\[
D_U:=(Z_U-W)^*(Z_U-W)
\]
is still exact and useful, but it measures the same norm geometry in a **moving source gauge**:
\[
\boxed{
D_U=\mathfrak P_U^*\mathfrak P_U
=U_R^*\mathscr G_UU_R
=2I-\Omega_U-\Omega_U^*,
}
\]
where \(\Omega_U=U_R^*\Gamma_UU_R\).  Hence \(D_U\) and \(\mathscr G_U\) have identical operator norms and spectra at each fixed \(U\), but their fixed-vector strong asymptotics are not equivalent without additional control of the moving unitary \(U_R\).

This is exactly the strong-topology version of the O3t \(\Omega_U\)-firewall.

## Canonical statuses

- [R22-A] true R15 strong-gauge angle defect
  \[
  \mathscr G_U=(V_U-W)^*(V_U-W)=2I-\Gamma_U-\Gamma_U^*
  \]
  with \(0\le\mathscr G_U\le4I\): **✓[M]**;

- [R22-B] fixed-vector and dense-core criterion for the R15 strong gauge gate: **✓[M]**;

- [R22-C] moving-gauge defect
  \[
  D_U=(Z_U-W)^*(Z_U-W)=\mathfrak P_U^*\mathfrak P_U
  =U_R^*\mathscr G_UU_R
  \]
  and \(\|D_U\|=\|\mathscr G_U\|=\|\mathfrak P_U\|^2\): **✓[M]**;

- [R22-D] fixed-vector convergence of \(D_U\) is equivalent to fixed-vector convergence of \(\mathscr G_U\) by abstract unitary conjugacy: **✓[M]_neg**;

- [R22-E] metric-only representation of \(\Gamma_U\) / \(\mathscr G_U\) still contains the unresolved inverse-square-root orientation: **✓[M]** as an identity/firewall;

- [R22-F] concrete P11 asymptotics of
  \[
  \langle\mathscr G_Uf,f\rangle
  \]
  for fixed smooth odd source vectors \(f\): **?[O]**.

No conclusion about the full future transport, strong Cauchy convergence, or a global Object X follows.

---

## 1. Exact positive angle defect for the R15 gate

Recall
\[
V_U:=U_SWU_R^*,
\qquad
\Gamma_U:=W^*V_U.
\]
Both \(V_U\) and \(W\) are isometries. Therefore
\[
\begin{aligned}
\mathscr G_U
&:=(V_U-W)^*(V_U-W)\\
&=V_U^*V_U-V_U^*W-W^*V_U+W^*W\\
&=2I-\Gamma_U^*-\Gamma_U.
\end{aligned}
\]
Thus
\[
\boxed{
\mathscr G_U=2I-\Gamma_U-\Gamma_U^*.
}
\]
It is positive by construction, and
\[
\|V_U-W\|\le2
\]
gives
\[
\boxed{0\le\mathscr G_U\le4I.}
\]
For every fixed source vector \(f\),
\[
\boxed{
\langle\mathscr G_Uf,f\rangle
=\|(V_U-W)f\|^2.
}
\]

This is the intrinsic positive Gram/angle defect of the R15 strong gauge criterion.

---

## 2. Dense-core criterion

Let \(\mathcal C\) be any fixed dense subspace of the R-source Hilbert space, for example the smooth odd source core used throughout the O3 branch.

Then
\[
\boxed{
\Gamma_U\xrightarrow[s]{}I
\iff
\langle\mathscr G_Uf,f\rangle\to0
\quad\text{for every }f\in\mathcal C.
}
\]

Proof: R15 gives
\[
\Gamma_U\xrightarrow[s]{}I
\iff
V_U\xrightarrow[s]{}W.
\]
The forward implication to the quadratic form is immediate.  Conversely, if the quadratic form tends to zero on \(\mathcal C\), then
\[
\|(V_U-W)f\|\to0
\qquad(f\in\mathcal C).
\]
Since
\[
\|V_U-W\|\le2
\]
uniformly, for arbitrary \(x\) and \(f\in\mathcal C\),
\[
\|(V_U-W)x\|
\le2\|x-f\|+\|(V_U-W)f\|.
\]
Taking \(U\to\infty\) and then \(f\to x\) proves strong convergence on the whole source space.

Consequently, failure of strong gauge convergence is witnessed by one **fixed** source vector and one subsequence:
\[
\exists f,\ U_n\to\infty:
\qquad
\limsup_{n\to\infty}
\langle\mathscr G_{U_n}f,f\rangle>0.
\]
A positive operator-norm lower bound with \(U\)-dependent maximizing vectors does not supply such a witness.

---

## 3. Relation to the R21 cross-polar defect

O3t defines
\[
Z_U=U_S^*WU_R,
\qquad
Z_U-W=-U_S^*\mathfrak P_U,
\qquad
\mathfrak P_U:=U_SW-WU_R.
\]
Hence
\[
\boxed{
D_U:=(Z_U-W)^*(Z_U-W)
=\mathfrak P_U^*\mathfrak P_U.
}
\]
On the other hand
\[
V_U-W=\mathfrak P_UU_R^*,
\]
so
\[
\mathscr G_U
=(V_U-W)^*(V_U-W)
=U_R\mathfrak P_U^*\mathfrak P_UU_R^*.
\]
Equivalently,
\[
\boxed{
D_U=U_R^*\mathscr G_UU_R.
}
\]
Using \(\Omega_U=U_R^*\Gamma_UU_R\) from O3t gives
\[
\boxed{
D_U=2I-\Omega_U-\Omega_U^*
=U_R^*(2I-\Gamma_U-\Gamma_U^*)U_R.
}
\]
Thus
\[
\boxed{
\|D_U\|=\|\mathscr G_U\|=\|\mathfrak P_U\|^2
=\|V_U-W\|^2.
}
\]
At the operator-norm level nothing is lost.  At the fixed-vector / strong level the moving conjugation by \(U_R\) is decisive.

There is also the exact positive decomposition inherited from R20:
\[
\mathfrak P_U
=\Lambda_U+W(\Gamma_U-I)U_R,
\qquad
\Lambda_U:=(I-WW^*)U_SW,
\]
with orthogonal ranges. Therefore
\[
\boxed{
D_U
=\Lambda_U^*\Lambda_U
+U_R^*(\Gamma_U-I)^*(\Gamma_U-I)U_R.
}
\]
This is an operator-level version of the R20 Pythagorean identity.  It does not remove the moving-\(U_R\) issue.

---

## 4. Moving-unitary strong-convergence counterexample

The implication
\[
D_U\xrightarrow[s]{}0
\Longrightarrow
\mathscr G_U\xrightarrow[s]{}0
\]
is false under abstract moving unitary conjugacy.

Let \(\mathcal H=\ell^2(\mathbb N)\), \(W=I\), and let
\[
V:=I-2P_{e_1}
\]
be the reflection in the first coordinate.  Then
\[
\mathscr G:=(V-I)^*(V-I)=4P_{e_1},
\]
which is constant and does not converge strongly to zero.

For each \(n\), choose a unitary \(U_{R,n}\) with
\[
U_{R,n}^*e_1=e_n,
\]
and put
\[
U_{S,n}:=VU_{R,n}.
\]
Then
\[
V_n=U_{S,n}WU_{R,n}^*=V
\]
for every \(n\), while
\[
\mathfrak P_n
=U_{S,n}W-WU_{R,n}
=(V-I)U_{R,n}.
\]
Hence
\[
D_n
=\mathfrak P_n^*\mathfrak P_n
=U_{R,n}^*(4P_{e_1})U_{R,n}
=4P_{e_n}
\xrightarrow[s]{}0.
\]
Thus the moving-gauge defect can converge strongly to zero while the actual R15 angle defect remains fixed and nonzero.

This is not a counterexample to the concrete P11 metric family.  It is a topology firewall: strong convergence is not invariant under conjugation by a terminal-dependent unitary sequence.

---

## 5. Metric representation and inverse-square-root firewall

Because
\[
U_S=X_SA_S^{-1/2},
\qquad
U_R^*=A_R^{-1/2}X_R^*,
\]
one has
\[
\boxed{
V_U
=X_SA_S^{-1/2}WA_R^{-1/2}X_R^*,
}
\]
and therefore
\[
\boxed{
\Gamma_U
=W^*X_SA_S^{-1/2}WA_R^{-1/2}X_R^*.
}
\]
Consequently the true fixed-vector angle defect is expressible from the metric polar products as
\[
\boxed{
\mathscr G_U
=2I-
W^*X_SA_S^{-1/2}WA_R^{-1/2}X_R^*
-
X_RA_R^{-1/2}W^*A_S^{-1/2}X_S^*W.
}
\]

This identity makes the remaining obstruction explicit: fixed-vector control of \(\mathscr G_U\) still requires the orientation of the inverse square roots \(A_R^{-1/2}\) and \(A_S^{-1/2}\).  R17/R19 do not provide this information, and O3t already records that the existing rank-one leading Gram asymptotics do not determine the inverse-square-root behavior.

Therefore R22 does not solve the gauge gate; it formulates its correct strong-topology observable.

---

## 6. Open problem R22-F

For a fixed dense smooth odd source core \(\mathcal C_R^-\), determine whether
\[
\boxed{
\langle\mathscr G_Uf,f\rangle
=\|(V_U-W)f\|^2
\longrightarrow0
}
\]
for every fixed \(f\in\mathcal C_R^-\), or construct a fixed \(f\) and subsequence \(U_n\to\infty\) with positive limsup.

Either direction requires genuinely relative inverse-square-root orientation information for the concrete P11 metric family.

Even a positive resolution \(\mathscr G_U\to0\) strongly would settle only the **polar gauge component**.  The full future transport
\[
W_{R,S,-}^{[U]}=U_SQU_R^*
\]
also contains the modulus defect \(Q-W\), whose required strong behavior on the relevant moving vectors is not established here.

Accordingly no conclusion about strong terminal transport, a global Object X, or any later global consequence is drawn.