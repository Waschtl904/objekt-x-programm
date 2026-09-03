# P11 R43 GC-AC hardening review and final `b_U` reduction

Date: 2026-09-03

## Scope and exact reviewed head

This is an internal destructive review of PR #53 on branch
`research/r43-gcac-hardening`.

Exact branch / PR head reviewed before this audit commit:

`f02f2c1d18e46e81c6f94801340b750581a4603f`

The immediately preceding mathematical-content head recorded by R43 is
`b0338d78f09017e8a72ece49b7af7514445acd62`; commit `f02f2c1d...` is a ledger reconciliation
on top of that content.  This review therefore does **not** silently promote any older external
review to the current head.

Status of this document: **internal AI review / hardening only**.  It creates no
`independent GREEN`, no freeze, no `✓[M]`, no Strong-Terminal promotion, and no R37/G4c
conclusion.

---

## 1. Verdict on the GC-AC hardening

### 1.1 Real-form complexification

The repaired analyticity convention in R43.10z0 is mathematically the right one.  The
Hermitian Hilbert-Riesz identification must not itself be analytically continued as a
complex-linear holomorphic family.  Passing to the underlying real symmetric Gamma form,
complexifying it bilinearly, and using the resulting complex-linear operator

\[
A(Q):\mathscr V_{Q_0}^{\mathbb C}\to(\mathscr V_{Q_0}^{\mathbb C})'
\]

removes that conjugate-linearity hazard.  On the positive real axis the constructed vectors
are real, so the bilinear continuation restricts to the genuine real Riesz problem, and the
identity

\[
\gamma_m(Q)=b_{m,Q}(\widetilde g_{m,Q})=\|g_{m,Q}\|_{\Gamma,Q}^2
\]

is used only there.  No off-real Hilbert-norm interpretation is needed.

**Verdict:** GREEN at internal-review level.

### 1.2 Arbitrary fixed jet order

For each fixed integer \(m\ge1\),

\[
I_m(z)=\int_0^z s^m e^{-s/2}\,ds
\]

is entire.  On a fixed complex disk about \(Q_0>0\), a holomorphic branch of \(Q^{1/2}\)
exists and every \(Q\)-derivative of
\(Q^{1/2}\operatorname{sgn}(y)I_m(Q|y|)\) is uniformly bounded for \(|y|\le1\).
Together with the fixed-domain embedding into \(L^2(-1,1)\), this gives the claimed
holomorphic dual-valued map \(Q\mapsto b_{m,Q}\).  Holomorphic inversion of \(A(Q)\) then
gives real analyticity of \(\gamma_m\) on \((0,\infty)\).

Since \(\gamma_m(Q)=\|P_Q^\Gamma g_{m,S}\|^2\) is nondecreasing, its Stieltjes measure is
locally

\[
d\gamma_m(Q)=\gamma_m'(Q)\,dQ.
\]

No pointwise strict positivity of \(\gamma_m'\) is required.

**Verdict:** GREEN at internal-review level for every fixed \(m\).

### 1.3 Scalar multiplicity is realization-independent

The intrinsic support projection nest exists before a canonical-system model is selected.
One diagonal realization is sufficient to exhibit multiplicity one because nest multiplicity
is invariant under unitary equivalence.  No uniqueness of the diagonal Hamiltonian is
required.  The atomless cumulative-measure reparameterization likewise preserves the support
nest up to null flat intervals.

**Verdict:** the revised formulation removes the earlier hidden uniqueness / determinant-
normalization assumption.

### 1.4 Measure-theoretic GC-AC step: one wording gap and its exact repair

R43.10cu--R43.10cw has the correct core idea: in a scalar nest model,

\[
d\gamma_m=|G_m|^2\,d\nu_S,
\qquad d\gamma_m\ll dQ,
\]

so every \(G_m\) vanishes on the singular part of \(\nu_S\).  Density of the countable
Riesz family then excludes a nonzero singular component.

One detail must be made explicit.  From

\[
d\nu_S=w\,dQ+d\nu_S^{\rm sc},
\qquad d\nu_S^{\rm sc}\perp dQ,
\]

choose a Borel set \(E\subset(0,S)\) with

\[
|E|=0,
\qquad
\nu_S^{\rm sc}((0,S)\setminus E)=0.
\tag{H43.1}
\]

Because \(d\gamma_m\ll dQ\),

\[
0=d\gamma_m(E)=\int_E |G_m|^2\,d\nu_S
=\int_E |G_m|^2\,d\nu_S^{\rm sc},
\]

hence

\[
G_m=0\quad\nu_S^{\rm sc}\text{-a.e. on }E
\qquad\forall m\ge1.
\tag{H43.2}
\]

If \(\nu_S^{\rm sc}\ne0\), then, because \(|E|=0\), the closed subspace

\[
\mathcal H_E:=\{F\in L^2(d\nu_S):F=0\text{ a.e. on }E^c\}
\simeq L^2(E,d\nu_S^{\rm sc})
\]

is nonzero and is orthogonal to every \(G_m\), contradicting R43.10ct.  Therefore

\[
\boxed{\nu_S^{\rm sc}=0.}
\tag{H43.3}
\]

This supplies the missing null-support sentence and makes the final contradiction literal.

**Verdict:** with H43.1--H43.3, the Section 3K.5 GC-AC argument is internally GREEN as a
candidate proof, conditional only on the already stated scalar-multiplicity input and the
higher-jet analyticity/totality stack.  It remains independently unreviewed on the exact
hardening head.

---

## 2. Source-interface review status

The published Bessonov--Denisov paper is correctly identified as Invent. Math. 234 (2023),
291--373, DOI 10.1007/s00222-023-01201-9.  The current hardening is also correctly cautious:
it does not infer determinant normalization or uniqueness of the diagonal Hamiltonian, and
it treats the stronger PW-sampling route as unavailable for the concrete Gamma measure once
unit-interval masses are unbounded.

The present internal review does **not** create an independent literature-verification
booking for the precise Szegő-to-type-clock implication.  That imported theorem interface
must remain part of the exact-head external review scope before freeze.

---

## 3. The last Strong-Terminal scalar after candidate GC-AC

Assume the candidate GC-AC conclusion and use R43.44--R43.48:

\[
w_U=W_{R,S}^{[U]}\varepsilon_R
=b_U\varepsilon_S+h_U,
\qquad
b_U\in[-1,1],
\qquad
h_U\in H_S^0,
\qquad
h_U\rightharpoonup0,
\]

with

\[
\boxed{\|h_U\|^2=1-b_U^2.}
\tag{B43.1}
\]

R43.51 is correct:

\[
\boxed{
\text{Strong Terminal}
\iff
[b_U\text{ Cauchy}]\ \&\ [b_U^2\to1].
}
\tag{B43.2}
\]

The remaining two subgates can be sharpened further without any new analytic input.

### 3.1 Exact cross-scalar identity

For any terminals \(T,U\), orthogonality of the fixed decomposition gives

\[
\boxed{
L_{R,S}^{T,U}
=
 b_T b_U
+
\operatorname{Re}\langle h_T,h_U\rangle.
}
\tag{B43.3}
\]

Indeed R43.50 and
\(\|h_X\|^2=1-b_X^2\) give this after expansion.

If B-TIGHT holds, equivalently \(b_U^2\to1\), then \(\|h_U\|\to0\), hence

\[
\boxed{
L_{R,S}^{T,U}-b_Tb_U\to0
\qquad(T,U\to\infty).
}
\tag{B43.4}
\]

Therefore under candidate GC-AC + B-TIGHT,

\[
\boxed{
\text{Strong Terminal}
\iff
b_Tb_U\to1
\qquad(T,U\to\infty).
}
\tag{B43.5}
\]

This is an exact replacement of the remaining Cauchy/sign gate by a two-terminal scalar
correlation gate.

### 3.2 Opposite-sign escape is maximally visible

Under B-TIGHT, every cofinal subsequence has \(|b_U|\to1\).  If there exist cofinal
sequences \(T_n,U_n\to\infty\) with opposite asymptotic signs, then

\[
b_{T_n}b_{U_n}\to-1,
\qquad
\langle h_{T_n},h_{U_n}\rangle\to0,
\]

so

\[
\boxed{
L_{R,S}^{T_n,U_n}\to-1,
\qquad
\|w_{U_n}-w_{T_n}\|^2\to4.
}
\tag{B43.6}
\]

Thus failure of the last sign gate is not a small residual phenomenon: after B-TIGHT it
produces asymptotically antipodal normal images.

Conversely, if there is \(U_0\) such that all sufficiently large \(b_U\) have the same sign,
then B-TIGHT gives

\[
b_U\to+1\quad\text{or}\quad b_U\to-1,
\]

and Strong Terminal follows.

Hence the live post-B-TIGHT gate can be booked as

\[
\boxed{
\textbf{B-SIGN: eventual sign coherence of }b_U.
}
\tag{B43.7}
\]

Equivalently, under B-TIGHT,

\[
\boxed{
\textbf{B-SIGN}
\iff
\liminf_{T,U\to\infty} b_Tb_U>0
\iff
b_Tb_U\to1.
}
\tag{B43.8}
\]

No terminal continuity is assumed here.

### 3.3 Priority after this review

The final fixed-pair Strong-Terminal problem is therefore ordered as follows:

1. **B-TIGHT**: exclude norm escape, i.e. prove \(b_U^2\to1\).  The canonical jet-tail
   criterion R43.57 remains exact; B-JMOM remains a sufficient route.
2. **B-SIGN**: once B-TIGHT is known, exclude asymptotically antipodal sign branches.
   By B43.5 this can be attacked directly through the cross-kernel coefficient
   \(L_{R,S}^{T,U}\), without separately proving continuity of \(U\mapsto b_U\).

The second point is the useful new reduction: the sign problem is now a scalar
**cross-terminal correlation** problem already expressed in the canonical R5/R39 observable.

---

## 4. Booking

At the exact pre-audit head `f02f2c1d18e46e81c6f94801340b750581a4603f`:

- GC-M1_scalar: candidate-GREEN, independently unreviewed on current hardening;
- GC-AC: candidate-closed; destructive internal review finds the argument sound after the
  explicit null-support repair H43.1--H43.3;
- `b_U in R`: confirmed;
- B-TIGHT: OPEN;
- B-SIGN / cross-scalar coherence: OPEN;
- Strong Terminal / C6: OPEN;
- R43 overall: OPEN;
- no freeze and no promotion.

The next mathematical attack should target B-TIGHT first, while testing whether the concrete
cross-kernel structure supplies a direct lower bound or sign-coherence mechanism for
`b_T b_U`.