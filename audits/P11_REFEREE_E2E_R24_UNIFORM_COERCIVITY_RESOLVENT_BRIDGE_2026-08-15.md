# P11 End-to-End Referee R24 — uniform coercivity and the inverse-root resolvent bridge

Date: 2026-08-15

## Target

After R22/R23 the remaining gauge obstruction was described as an inverse-square-root
orientation problem for the concrete relative metrics
\[
A_X(U):=A_{T_0,U}^{X,-},\qquad X\in\{R,S\}.
\]
R15 had also used an abstract rank-one model in which the smallest eigenvalue can
collapse and the inverse square root can blow up.  R24 checks whether such small-spectrum
behavior can actually occur for the P11 relative metrics at fixed base terminal
\(T_0\), and then rewrites the nested inverse-square-root orientation exactly in terms
of the already existing second-moment off-block.

## Verdict

There is a **uniform P11 lower spectral bound**:
\[
\boxed{
A_X(U)\ge a_0 I,
\qquad
a_0:=\frac1{1+\|H_{T_0}\|^2}>0,
}
\]
for every \(U>T_0\) and \(X=R,S\).  Consequently
\[
\boxed{
\|A_X(U)^{-1/2}\|\le a_0^{-1/2}
=\sqrt{1+\|H_{T_0}\|^2}
}
\]
uniformly in the future terminal.

Thus the concrete P11 inverse-square-root gate is **not** a small-eigenvalue/norm-blowup
problem.  The unresolved information is the orientation of the inverse square roots
across the nested source levels.

That orientation has an exact resolvent representation.  If
\[
A_R=W^*A_SW,
\qquad
P=WW^*,
\qquad
\mathscr B_U:=(I-P)A_SW=A_SW-WA_R,
\]
then
\[
\boxed{
A_S^{-1/2}W-WA_R^{-1/2}
=-\frac1\pi\int_0^\infty
 t^{-1/2}(A_S+tI)^{-1}\mathscr B_U(A_R+tI)^{-1}\,dt.
}
\]
The integral converges in operator norm.  The corresponding square-root bridge is
\[
\boxed{
A_S^{1/2}W-WA_R^{1/2}
=\frac1\pi\int_0^\infty
 t^{1/2}(A_S+tI)^{-1}\mathscr B_U(A_R+tI)^{-1}\,dt.
}
\]
Hence the positive and inverse-square-root orientation defects are two different
resolvent weightings of the **same** off-block \(\mathscr B_U\).

This is a genuine new reduction for the R22/R23 gate.  R19 controls the raw off-block at
one scale; R24 identifies the exact resolvent-weighted quantity that must be controlled
to reach the inverse-root orientation.

## Canonical statuses

- [R24-A] uniform lower spectral bound for the concrete P11 relative metrics:
  **✓[M]**;
- [R24-B] uniform inverse-square-root norm bound: **✓[M]**;
- [R24-C] the abstract possibility of future-terminal inverse-root norm blow-up as the
  concrete P11 obstruction: **✓[M]_neg**;
- [R24-D] exact inverse-root resolvent intertwining formula: **✓[M]**;
- [R24-E] exact square-root resolvent intertwining formula and common off-block source:
  **✓[M]**;
- [R24-F] concrete asymptotics of the resolvent-weighted off-block on fixed source
  vectors: **?[O]**.

No strong terminal-transport conclusion, Object X construction, Seal, or RH claim is
made.

---

## 1. Uniform coercivity of the actual relative metrics

Fix \(X\in\{R,S\}\), a base terminal \(T_0>X\), and a future terminal \(U>T_0\).
The Rayleigh quotient of the relative metric is, as used already in O3l,
\[
\frac{\langle A_X(U)z,z\rangle_{X,T_0}}{\|z\|_{X,T_0}^2}
=
\frac{q_U^X(E_{X,U}z)}{q_{T_0}^X(E_{X,T_0}z)}.
\]
Exact Gamma compatibility and positivity of the Schur term give
\[
q_U^X(E_{X,U}z)\ge \mathfrak c_{\Gamma,X}[z].
\]
At the fixed baseline, the graph-norm equivalence gives
\[
q_{T_0}^X(E_{X,T_0}z)
\le
(1+\|H_{T_0}\|^2)\mathfrak c_{\Gamma,X}[z].
\]
Therefore for every nonzero \(z\),
\[
\frac{q_U^X(E_{X,U}z)}{q_{T_0}^X(E_{X,T_0}z)}
\ge
\frac1{1+\|H_{T_0}\|^2}.
\]
Thus
\[
\boxed{
A_X(U)\ge a_0I,
\qquad
a_0=(1+\|H_{T_0}\|^2)^{-1}.
}
\tag{R24.1}
\]

Combined with O3l,
\[
A_X(U)\le (1+\|H_U\|^2)I
\ll \frac{e^U}{U}I.
\]
So the growth of the condition number comes from the upper spectral edge; the lower
edge remains uniformly separated from zero.

Functional calculus immediately yields
\[
\boxed{
\|A_X(U)^{-1/2}\|\le a_0^{-1/2}.
}
\tag{R24.2}
\]

This does not determine the inverse-square-root orientation, but it removes a false
candidate mechanism: concrete P11 inverse roots do not become large because
\(\lambda_{\min}(A_X(U))\to0\).

---

## 2. Nested off-block identity

Keep the P11 relative compression identity
\[
A_R=W^*A_SW
\]
and put
\[
P:=WW^*.
\]
Then
\[
WA_R=WW^*A_SW=PA_SW.
\]
Hence
\[
\boxed{
A_SW-WA_R=(I-P)A_SW=:\mathscr B_U.
}
\tag{R24.3}
\]
This is exactly the second-moment off-block used in O3l/O3r.

Thus every failure of the relative metrics themselves to intertwine under \(W\) is
encoded by \(\mathscr B_U\).

---

## 3. Exact inverse-square-root resolvent bridge

For every positive invertible operator \(A\),
\[
A^{-1/2}
=\frac1\pi\int_0^\infty t^{-1/2}(A+tI)^{-1}\,dt
\]
in operator norm.  Apply this to \(A_S\) and \(A_R\).  The resolvent quasi-commutator is
\[
\begin{aligned}
(A_S+tI)^{-1}W-W(A_R+tI)^{-1}
&=(A_S+tI)^{-1}
\bigl(W(A_R+tI)-(A_S+tI)W\bigr)
(A_R+tI)^{-1}\\
&=-(A_S+tI)^{-1}\mathscr B_U(A_R+tI)^{-1}.
\end{aligned}
\]
Therefore
\[
\boxed{
\begin{aligned}
A_S^{-1/2}W-WA_R^{-1/2}
={}&-\frac1\pi\int_0^\infty t^{-1/2}
(A_S+tI)^{-1}\mathscr B_U(A_R+tI)^{-1}\,dt.
\end{aligned}
}
\tag{R24.4}
\]

By (R24.1),
\[
\|(A_X+tI)^{-1}\|\le(a_0+t)^{-1},
\]
so the integrand is bounded by
\[
t^{-1/2}(a_0+t)^{-2}\|\mathscr B_U\|,
\]
which is integrable.  Hence the formula is a genuine operator-norm Bochner integral.
Moreover
\[
\boxed{
\|A_S^{-1/2}W-WA_R^{-1/2}\|
\le \frac1{2a_0^{3/2}}\|\mathscr B_U\|.
}
\tag{R24.5}
\]
Indeed
\[
\frac1\pi\int_0^\infty
\frac{t^{-1/2}}{(a_0+t)^2}\,dt
=\frac1{2a_0^{3/2}}.
\]

The crude norm bound is not expected to decide the asymptotics because O3l shows that
\(\|\mathscr B_U\|\) is large.  The value of (R24.4) is structural: it identifies the
required cancellation as a resolvent-weighted off-block problem.

---

## 4. Square-root bridge from the same off-block

Use the standard positive functional-calculus representation
\[
A^{1/2}
=\frac1\pi\int_0^\infty t^{-1/2}A(A+tI)^{-1}\,dt.
\]
Since
\[
A(A+tI)^{-1}=I-t(A+tI)^{-1},
\]
we obtain
\[
\begin{aligned}
&A_S(A_S+tI)^{-1}W
-WA_R(A_R+tI)^{-1}\\
&\qquad
=-t\bigl((A_S+tI)^{-1}W-W(A_R+tI)^{-1}\bigr)\\
&\qquad
=t(A_S+tI)^{-1}\mathscr B_U(A_R+tI)^{-1}.
\end{aligned}
\]
Therefore
\[
\boxed{
A_S^{1/2}W-WA_R^{1/2}
=\frac1\pi\int_0^\infty t^{1/2}
(A_S+tI)^{-1}\mathscr B_U(A_R+tI)^{-1}\,dt.
}
\tag{R24.6}
\]
Again the integral converges in operator norm, and
\[
\boxed{
\|A_S^{1/2}W-WA_R^{1/2}\|
\le\frac1{2\sqrt{a_0}}\|\mathscr B_U\|.
}
\tag{R24.7}
\]

Applying \(I-P\) to (R24.6) gives an exact resolvent representation of the O3r
square-root off-block
\[
\mathscr C_U=(I-P)A_S^{1/2}W.
\]
Applying \(I-P\) to (R24.4) gives the corresponding inverse-root off-block.

Thus O3r's square-root witness and R22's inverse-root orientation are not unrelated
objects: they are different spectral weightings of the same second-moment off-block.

---

## 5. Consequence for the R22/R23 firewall

The R15 abstract matrix model correctly proves that rank-one leading fixed-pair data do
not determine inverse square roots in arbitrary positive families.  R24 adds a concrete
P11 restriction that the abstract model did not impose:
\[
\lambda_{\min}(A_X(U))\ge a_0>0.
\]
Therefore the concrete P11 obstruction must not be described as an unknown blow-up of
\(\|A_X(U)^{-1/2}\|\).  That norm is uniformly bounded.

What remains unknown is the nested orientation
\[
A_S^{-1/2}W-WA_R^{-1/2},
\]
and (R24.4) shows exactly where it lives: in the resolvent-smoothed off-block
\[
(A_S+tI)^{-1}\mathscr B_U(A_R+tI)^{-1}.
\]

This is a sharper target than estimating the raw inverse square roots separately.

---

## 6. Open problem R24-F

For fixed smooth odd source vectors \(f\), estimate
\[
\boxed{
\int_0^\infty t^{-1/2}
(A_S+tI)^{-1}\mathscr B_U(A_R+tI)^{-1}f\,dt
}
\]
as \(U\to\infty\), and analogously the \(t^{1/2}\)-weighted integral.

A proof that the inverse-root integral tends to zero on a fixed dense core would give a
new concrete nested functional-calculus compatibility statement.  A fixed-vector
positive limsup would produce an inverse-root orientation obstruction.

The existing raw lower bound on \(\mathscr B_U\) does not decide either alternative,
because the large directions may be suppressed by the two resolvents.  This is exactly
the new analytic gate.
