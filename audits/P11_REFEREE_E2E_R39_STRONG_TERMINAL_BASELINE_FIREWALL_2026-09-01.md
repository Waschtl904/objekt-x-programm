# P11 End-to-End Referee R39 — Strong-Terminal versus baseline-stabilization firewall

Date: 2026-09-01

## Purpose

Correct the operative formulation of Roadmap B.

For fixed \(0<R<S\), the actual Strong-Terminal question is

\[
\boxed{
W_{R,S}^{[U]}
\quad\text{has a strong limit as }U\to\infty?
}
\tag{R39.1}
\]

Equivalently, because the \(W_{R,S}^{[U]}\) are isometries,

\[
\boxed{
(W_{R,S}^{[U]}f)_{U>S}
\text{ is Cauchy for every fixed source }f.
}
\tag{R39.2}
\]

R14/R15/R22 instead introduce, after choosing a fixed baseline terminal \(T_0\),

\[
W:=W_{R,S}^{[T_0]},
\]

the polar-gauge factorization

\[
W_{R,S}^{[U]}
=
U_S(U)\,Q_U\,U_R(U)^*,
\tag{R39.3}
\]

and the pure gauge isometry

\[
V_U:=U_S(U)WU_R(U)^*.
\tag{R39.4}
\]

R22-F asks whether

\[
V_U\to W
\quad\text{strongly},
\tag{R39.5}
\]

equivalently whether its positive angle defect tends to zero.

The point of R39 is:

\[
\boxed{
\text{R39.5 is not the Strong-Terminal question R39.1.}
}
\]

It is a baseline-return condition.

---

## 1. Exact Strong-Terminal criterion

R5 gives, for \(T,U>S\),

\[
K_{R,S}^{T,U}
=
(W_{R,S}^{[T]})^*W_{R,S}^{[U]},
\]

and

\[
\boxed{
\|(W^{[U]}-W^{[T]})f\|^2
=
2\|f\|^2
-
2\operatorname{Re}
\langle f,K_{R,S}^{T,U}f\rangle.
}
\tag{R39.6}
\]

Therefore

\[
\boxed{
W_{R,S}^{[U]}
\text{ is strongly Cauchy}
}
\]

iff for every fixed \(f\),

\[
\boxed{
\operatorname{Re}
\langle f,K_{R,S}^{T,U}f\rangle
\longrightarrow
\|f\|^2
\qquad(T,U\to\infty).
}
\tag{R39.7}
\]

This is the exact Roadmap-B gate.

No fixed baseline terminal occurs in R39.7.

---

## 2. What the fixed-baseline polar decomposition tests

Fix \(T_0>S\). R14 gives

\[
W_U:=W_{R,S}^{[U]}
=
U_SQ_UU_R^*.
\]

It also defines

\[
V_U:=U_SWU_R^*,
\qquad W=W_{R,S}^{[T_0]}.
\]

Thus

\[
W_U-V_U
=
U_S(Q_U-W)U_R^*.
\tag{R39.8}
\]

Consequently

\[
\|W_U-V_U\|
=
\|Q_U-W\|.
\tag{R39.9}
\]

If both

\[
Q_U\to W
\quad\text{strongly in the relevant moving-gauge sense}
\]

and

\[
V_U\to W
\quad\text{strongly},
\]

then indeed

\[
W_U\to W.
\]

That is a sufficient **baseline stabilization** route.

But Strong Terminal only asks for some limit

\[
W_U\to W_\infty,
\]

and \(W_\infty\) need not equal \(W\).

---

## 3. R23 is already an exact counterexample to necessity of R22-F

R23 constructs a continuous canonical-inclusion family with

\[
Q_t=W
\]

for every \(t\), while the actual future transport satisfies

\[
\boxed{
W_t\to v_\infty\ne W.
}
\tag{R39.10}
\]

In that model the source polar factor is \(U_R=I\), so

\[
W_t=V_t.
\]

Hence

\[
\boxed{
V_t\not\to W,
}
\]

and the R22 angle defect tends to the explicit positive constant

\[
\delta^2>0.
\]

Nevertheless \(W_t\) has a perfectly good strong limit \(v_\infty\).

Therefore the implication

\[
\boxed{
\text{Strong Terminal exists}
\Longrightarrow
\mathscr G_U\to0
}
\]

is false even in a continuous canonical-inclusion rank-one model satisfying exact pullback and perfect modulus coherence.

Equivalently:

\[
\boxed{
\text{R22-F is not a necessary condition for Roadmap B.}
}
\tag{R39.11}
\]

This does not prove anything positive or negative about the concrete P11 family. It corrects the logical role of the gate.

---

## 4. R37 modulus mismatch also does not decide Strong Terminal

R37 gives on an explicit concrete P11 two-shift region

\[
Q_U\not\to W
\quad\text{strongly}.
\]

This rules out one particular baseline-stabilization scenario.

It does **not** rule out

\[
Q_U\to Q_\infty\ne W
\]

or, more importantly,

\[
W_U=U_SQ_UU_R^*
\to W_\infty
\]

through coherent joint convergence of modulus and polar factors.

Thus:

\[
\boxed{
Q_U\not\to W
\not\Longrightarrow
W_U\text{ is not strongly convergent}.
}
\tag{R39.12}
\]

R14's algebraic countermodels already forbid such a promotion abstractly; R23 shows that convergence to a nonbaseline limit is genuinely compatible with persistent baseline angle.

---

## 5. Correct decomposition of the B-front

The operative B-front should therefore be separated into:

### B-MOD — modulus limit geometry

Determine whether the isometries

\[
Q_U=A_S(U)^{1/2}WA_R(U)^{-1/2}
\]

possess a strong/weakly rigid limit, possibly

\[
Q_\infty\ne W.
\]

R27/R28/R37/R38 are inputs here.

### B-POL — relative polar limit geometry

Determine the asymptotic behavior of the unique polar factors \(U_R(U),U_S(U)\), but **not**
only through the baseline-return condition \(V_U\to W\).

The relevant question is whether their joint action combines with \(Q_U\) to produce a limit.

### B-C6 — actual Strong-Terminal gate

Determine directly whether

\[
\boxed{
W_{R,S}^{[U]}
=
U_S(U)Q_UU_R(U)^*
}
\]

is strongly Cauchy.

The exact final observable is R39.7.

---

## 6. Correct role of R22-F

R22 remains mathematically useful.

It asks whether the pure polar gauge returns to its baseline position:

\[
V_U\to W.
\]

A positive result would simplify B-POL strongly.

A negative result would show persistent baseline polar drift.

But neither verdict alone decides whether \(V_U\) itself has a different strong limit.

Thus R22-F should be labeled

\[
\boxed{
\text{baseline polar stabilization gate},
}
\]

not

\[
\boxed{
\text{the Strong-Terminal gate}.
}
\]

---

## 7. New constructive priority

Because R27 already supplies strong inverse-root limits, R38 gives a fixed tangential weak-cluster
map for \(Q_U\), and R37 produces a concrete nonbaseline modulus defect, the next constructive
question is:

\[
\boxed{
Q_U
\text{ itself: does it converge strongly to a nonbaseline }Q_\infty?
}
\tag{R39.13}
\]

If yes, the full Roadmap-B problem becomes a cleaner polar-coherence problem around a **known
modulus limit**, instead of the artificial target \(Q_U\to W\).

If no, a fixed-vector/subsequence witness for non-Cauchy modulus behavior may already feed the
full cross-terminal Cauchy analysis.

The first next-order scalar inside R39.13 is the R38 future-dual-normal ratio

\[
\frac{\|A_R(U)^{-1/2}r_R\|}
{\|A_S(U)^{-1/2}r_S\|}.
\]

---

## 8. Status firewall

R39 is a logical/research-front reconciliation.

It does not promote:

- existence of a modulus limit;
- existence or nonexistence of Strong Terminal;
- any R22 verdict for concrete P11;
- Object X;
- RH.

Candidate status:

\[
\boxed{
\text{Strong Terminal / C6 remains }?[O],
}
\]

but its correct active target is **strong Cauchy / arbitrary strong limit**, not forced return to the baseline terminal geometry.
