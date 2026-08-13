# P11 End-to-End Referee Audit R8 — Mixed-jet bilinear asymptotic and rank-one scope

**Date:** 2026-08-13  
**Repository:** `Waschtl904/objekt-x-programm`  
**Branch:** `main`  
**Paper under review:** `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex`  
**Proof module:** `papers/P11_sections/P11_TC1_MixedJet.tex`

## Executive verdict

- **[R8-A] ✓[M]** — the mixed-jet bilinear asymptotic is correct, assuming the already separately audited sharp diagonal theorem and its local R1 paper repairs.
- **[R8-B] ✓[M]** — the positive rank-one remainder decomposition and the fixed-pair Cauchy--Schwarz step are correct.
- **[R8-C] ✓[M]** — the fixed-pair angle-collapse corollary is correct.
- **[R8-D] ✓[M]_part (wording only)** — the remark saying the normalized Gram geometry on “any collection” becomes rank one should be read, and preferably written, as **any fixed finite collection, entrywise (equivalently in finite-dimensional matrix norm)**. No infinite-family uniform statement follows.

**Overall R8 status:** **PASS on theorem core; minor scope wording repair recommended.**

---

## 1. Exact rank-one/remainder decomposition

For fixed smooth odd `f`, the paper sets

\[
h_T(f)=H_T^*J_{R,T}f,
\qquad
x_f=A_T^{-1/2}h_T(f),
\qquad
v_T=A_T^{1/2}\mathbf1_T,
\]

with

\[
A_T=I+R_T^*R_T.
\]

Using the paper's sesquilinear convention (linear in the first component),

\[
\sigma_T(Jf,Jg)=\langle x_f,x_g\rangle,
\qquad
\ell_T(f)=\langle x_f,v_T\rangle,
\qquad
 d_T=\|v_T\|^2.
\]

Let `P_{v_T}` be the orthogonal projection onto `C v_T`. Then

\[
\langle P_{v_T}x_f,P_{v_T}x_g\rangle
=
\frac{\ell_T(f)\overline{\ell_T(g)}}{d_T}
=:\rho_T(f,g).
\]

Therefore

\[
\boxed{
D_T(f,g):=\sigma_T(Jf,Jg)-\rho_T(f,g)
=
\langle(I-P_{v_T})x_f,(I-P_{v_T})x_g\rangle.
}
\]

This is an exact Gram representation. Hence `D_T` is positive semidefinite and

\[
|D_T(f,g)|^2\le D_T(f,f)D_T(g,g).
\]

No selfadjointness or polarization shortcut beyond this Hilbert-space identity is being smuggled in.

---

## 2. Non-circular diagonal exhaustion

If `m=m(f)` is the first nonzero jet, the boundary expansion gives independently

\[
\ell_T(f)
=-\sqrt2\,c_m\beta_R^{(m)}(f)
\frac{e^{T/2}}{T^{m+1/2}}(1+O(T^{-1})),
\]

while the constant-mode denominator is

\[
d_T=2T+O(1).
\]

Thus, before using the total sharp diagonal Schur asymptotic,

\[
\rho_T(f,f)
=c_m^2|\beta_R^{(m)}(f)|^2
\frac{e^T}{T^{2m+2}}(1+O(T^{-1})).
\]

The separately audited sharp diagonal theorem gives the same leading term for

\[
\sigma_T(Jf,Jf).
\]

Consequently

\[
D_T(f,f)
=o\!\left(\frac{e^T}{T^{2m+2}}\right).
\]

The same holds for `g` with first jet `n`. Since `f,g` are fixed, Cauchy--Schwarz yields

\[
D_T(f,g)
=o\!\left(\frac{e^T}{T^{m+n+2}}\right).
\]

No uniformity in `f,g` is required for this fixed-pair conclusion.

---

## 3. Mixed coefficient

The rank-one part satisfies

\[
\rho_T(f,g)
=c_mc_n\beta_R^{(m)}(f)\overline{\beta_R^{(n)}(g)}
\frac{e^T}{T^{m+n+2}}(1+O(T^{-1})).
\]

Adding the smaller remainder proves

\[
\boxed{
\sigma_T(J_{R,T}f,J_{R,T}g)
=c_mc_n\beta_R^{(m)}(f)\overline{\beta_R^{(n)}(g)}
\frac{e^T}{T^{m+n+2}}
(1+o_{R,f,g}(1)).
}
\]

The power `T^{m+n+2}`, coefficient, and conjugation orientation are all consistent with the paper's sesquilinear convention.

---

## 4. Fixed-pair angle collapse

Dividing the mixed asymptotic by the two sharp diagonal asymptotics gives

\[
\frac{\sigma_T(Jf,Jg)}
{\sigma_T(Jf,Jf)^{1/2}\sigma_T(Jg,Jg)^{1/2}}
\to
\frac{\beta_R^{(m)}(f)\overline{\beta_R^{(n)}(g)}}
{|\beta_R^{(m)}(f)|\,|\beta_R^{(n)}(g)|}.
\]

The limit has modulus one. This corollary is correct for every fixed nonzero smooth odd pair.

---

## 5. Exact scope of “rank one”

For a **fixed finite family** `f_1,...,f_N`, let `m_i=m(f_i)` and define the individually diagonal-normalized Gram matrix

\[
\Gamma_T(i,j)
:=
\frac{\sigma_T(Jf_i,Jf_j)}
{\sigma_T(Jf_i,Jf_i)^{1/2}\sigma_T(Jf_j,Jf_j)^{1/2}}.
\]

Put

\[
z_i:=\frac{\beta_R^{(m_i)}(f_i)}{|\beta_R^{(m_i)}(f_i)|}.
\]

Then for every `i,j`,

\[
\Gamma_T(i,j)\to z_i\overline{z_j}.
\]

Because `N` is fixed and finite, entrywise convergence is equivalent to convergence in any matrix norm. Hence

\[
\Gamma_T\to zz^*,
\]

a rank-one matrix.

This justifies the paper's fixed-pair/fixed-finite-family rank-one interpretation.

However, the phrase “on any collection of fixed smooth odd vectors” should not be read as an assertion for an infinite family in operator norm. Pairwise limits do not provide uniform control over an infinite collection, and the paper's own firewall explicitly denies such uniformity.

**Recommended wording:** replace “any collection of fixed smooth odd vectors” by

> “any fixed finite collection of smooth odd vectors, after individual diagonal normalization, converges entrywise (hence in finite-dimensional matrix norm) to a rank-one Gram matrix.”

---

## 6. Dependency and firewalls

R8 uses the sharp diagonal theorem `thm:odd`; therefore final paper-level closure of R8 inherits the local self-containment repairs already recorded in R1. R8 does not create a new defect in that theorem.

Nothing here proves:

\[
\text{uniform finite-jet Gram/square-root control},
\]

\[
K_{R,S}^{T,U}\to I,
\]

or

\[
W_{R,S,-}^{[T]}\ \text{strong Cauchy}.
\]

The rank-one leading limit is singular on multi-dimensional finite-jet spans, so inverse-square-root behavior can be governed by subleading eigendirections. That remains the genuine direct gate.

---

## Final referee disposition

\[
\boxed{
[R8\text{-}A,B,C]\ \checkmark[M],
\qquad
[R8\text{-}D]\ \checkmark[M]_{\rm part}\ \text{(scope wording only)}.
}
\]

**R8 theorem core: PASS.**
