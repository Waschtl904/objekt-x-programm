# P11 End-to-End Referee R17 — vanishing near-null Schur core

Date: 2026-08-14

Target: the bounded TC1 near-null remainder left open by R16,
\[
D_U(z_U,z_U)=O(1),
\qquad
z_U=f_m-\frac{\ell_U(f_m)}{\ell_U(f_0)}f_0,
\qquad \ell_U(z_U)=0.
\]

## Referee questions

1. Does the bounded hub remainder `h_U^rem(z_U)` possess a genuine large-terminal limit?
2. Is the R16 `O(1)` scale sharp, or can the remaining bounded source be absorbed once more by the future primitive/full-rest channel?
3. Can scalar bounded-core differences between the `R` and `S` levels encode the polar-gauge commutator?

# Verdict

The R16 bounded Schur core is not a nonzero second asymptotic layer.  The terminal hub remainder converges in `L^1 cap L^2` to an absolutely convergent global translation-difference remainder of zero integral.  Consequently the residual constant in the R16 certificate tends to zero.  Finite smooth mean-zero partial sums of that global remainder can then be absorbed by the same signed future-edge/full-rest construction at vanishing cost, while the `L^2` tail is controlled directly.  Hence
\[
\boxed{D_U(z_U,z_U)\to0.}
\]
The full graph energy therefore converges to the fixed Gamma floor
\[
\boxed{q_U^X(J_{R,U}z_U)\to\mathfrak c_{\Gamma,R}[f_m]>0.}
\]

Moreover, for canonically compatible vectors under `R -> S` zero extension, the terminal near-null vector and its scalar TC1 remainder are literally the same terminal object.  Thus the proposed scalar comparison of `D_U` at the two source levels cannot encode the gauge commutator; that route is false as stated.

Canonical statuses:

- [R17-A] global bounded hub-remainder operator / `L^1 cap L^2` convergence: **✓[M]**;
- [R17-B] second mean-zero future-edge absorption by fixed finite approximants: **✓[M]**;
- [R17-C] bounded near-null Schur core has zero limit: **✓[M]**;
- [R17-D] full near-null graph energy converges to the Gamma floor: **✓[M]**;
- [R17-E] scalar `R`/`S` bounded-core difference as a gauge diagnostic: **✓[M]_neg**;
- [R17-F] actual polar-gauge / cross-terminal convergence: **?[O]**.

---

## 1. The hub remainder has a genuine global limit

Keep the fixed cutoff `a_*` from the proof of Theorem 6.1.  The terminal hub remainder consists of the finite primitive block `a_p<a_*` together with all higher prime powers `k>=2` admitted by the terminal cutoff.  Define on the ambient line
\[
\mathcal H_{\rm rem,\infty}^* f
:=
\sum_{p:\,\frac12\log p<a_*}
\sqrt{\log p}\,p^{-3/4}D_{\log p}^*E_Rf
+
\sum_p\sum_{k\ge2}
\sqrt{\log p}\,p^{-3k/4}D_{k\log p}^*E_Rf.
\tag{R17.1}
\]
The primitive part is finite and
\[
\sum_p\sum_{k\ge2}\sqrt{\log p}\,p^{-3k/4}<\infty.
\]
Translations preserve `L^2` and `L^1`, so the higher-prime-power series converges absolutely in operator norm on both spaces; on the fixed smooth source core it also converges absolutely in each fixed translated `C^j` seminorm.

After zero extension of the terminal remainder to the ambient line, dominated convergence over this absolutely summable coefficient family gives
\[
\boxed{
E_U h_U^{\rm rem}(z_U)
\longrightarrow
h_{\rm rem,\infty}:=\mathcal H_{\rm rem,\infty}^*f_m
\quad\text{in }L^1(\mathbb R)\cap L^2(\mathbb R).
}
\tag{R17.2}
\]
Here the terminal cutoffs disappear termwise for every fixed `(p,k)`, the omitted coefficient tail is uniformly small by absolute summability, and `z_U -> f_m` in the fixed smooth source space.

Every full-line translation difference has zero integral.  Absolute `L^1` convergence therefore gives
\[
\boxed{\int_{\mathbb R}h_{\rm rem,\infty}=0.}
\tag{R17.3}
\]
Thus Stage 1 of the proposed R17 program is positive: the bounded hub remainder itself has a canonical global limit.

Important: this does not identify the Schur energy, because the terminal denominator `A_U=I+R_U^*R_U` continues to change with `U`.

---

## 2. The R16 residual converges to the global mean-zero remainder

Use the notation of R16:
\[
K_U=\langle h_U^{\rm grow},1_U\rangle,
\qquad
\mu_U=\frac{K_U}{2U}.
\]
The first certificate gives
\[
h_U
=\widetilde R_U^*\widehat Y_U^{(1)}
 +\mu_U1_U+h_U^{\rm rem}+Z_U^{\rm quad}+Z_U^{\rm tail},
\tag{R17.4}
\]
with
\[
\|\widehat Y_U^{(1)}\|^2=O(U^{-1}),
\qquad
\|Z_U^{\rm quad}\|_2+\|Z_U^{\rm tail}\|_2=o(1).
\tag{R17.5}
\]
Because `ell_U(z_U)=0`,
\[
K_U=-\langle h_U^{\rm rem}(z_U),1_U\rangle.
\tag{R17.6}
\]
The `L^1` convergence (R17.2) and (R17.3) imply
\[
\boxed{K_U\to0.}
\tag{R17.7}
\]
Consequently
\[
\boxed{
\|\mu_U1_U\|_2^2=\frac{|K_U|^2}{2U}\to0.
}
\tag{R17.8}
\]
Define
\[
r_U:=\mu_U1_U+h_U^{\rm rem}(z_U).
\]
Then, after zero extension to the ambient line,
\[
\boxed{E_Ur_U\to h_{\rm rem,\infty}\quad\text{in }L^2(\mathbb R),}
\tag{R17.9}
\]
and both sides have zero integral in the limit; in fact `r_U` has exact terminal mean zero because
\[
\langle r_U,1_U\rangle=K_U+\langle h_U^{\rm rem},1_U\rangle=0.
\]

The point of (R17.9) is that no moving-boundary `C^1` assertion is needed for the second absorption.

---

## 3. Fixed smooth mean-zero profiles have vanishing future-rest energy

We isolate the only new lemma required.

Let `g` be a fixed even `C_c^infty(R)` function with zero integral.  Regard it as a vector in `L^2(-U,U)` for all sufficiently large `U`.  Put
\[
b_U(t)=e(U-t),\qquad
k_g^{(U)}(t)=2g(U-t),\qquad 0<t<U.
\]
Then `int_0^U k_g^(U)=0`, so the exact anchor identity (6.15)--(6.16) applies.  Its continuous future-edge certificate has cost
\[
e^{-U}\int_0^Ue^{t/2}|k_g^{(U)}(t)|^2dt
\ll_g e^{-U/2}.
\tag{R17.10}
\]
Because `g` is fixed smooth and compactly supported, the source-representer derivative is uniformly bounded.  All required cells satisfy
\[
r\le \frac{U+O(1)}2,
\]
so the `theta=3/5` prime cells used in the R1 proof have
\[
\max_I|I|\ll e^{-2U/5}.
\]
The same mass-normalized quadrature therefore has source error tending to zero.  The exact `a=0` full-rest lift has tail tending to zero by (6.25).  Hence there exist `Y_{U,g}` and `E_{U,g}` such that
\[
\boxed{
g=\widetilde R_U^*Y_{U,g}+E_{U,g},
\qquad
\|Y_{U,g}\|_{\mathscr Z_U}\to0,
\qquad
\|E_{U,g}\|_2\to0.}
\tag{R17.11}
\]
The dual formula (6.2) therefore gives
\[
\boxed{\langle g,(I+R_U^*R_U)^{-1}g\rangle\to0.}
\tag{R17.12}
\]
This is a direct reuse of the audited R1 future-edge/full-rest mechanism on a fixed mean-zero profile; no new prime-distribution theorem is invoked.

---

## 4. Approximate the global remainder by finite mean-zero translation sums

Because the series (R17.1) converges absolutely in `L^2`, for every `epsilon>0` there is a finite partial sum `g_epsilon` made from finitely many complete translation differences such that
\[
\|h_{\rm rem,\infty}-g_\varepsilon\|_2<\varepsilon.
\tag{R17.13}
\]
Each summand is smooth, compactly supported and has zero integral, hence so does `g_epsilon`.

By (R17.9), for sufficiently large `U`,
\[
\|r_U-g_\varepsilon\|_2<2\varepsilon.
\tag{R17.14}
\]
Write the first R16 decomposition as
\[
h_U
=\widetilde R_U^*\widehat Y_U^{(1)}+r_U+Z_U^{\rm quad}+Z_U^{\rm tail}.
\]
For the fixed `g_epsilon`, use (R17.11):
\[
g_\varepsilon=\widetilde R_U^*Y_{U,\varepsilon}+E_{U,\varepsilon},
\qquad
\|Y_{U,\varepsilon}\|\to0,
\qquad
\|E_{U,\varepsilon}\|_2\to0.
\]
Thus
\[
h_U
=\widetilde R_U^*\bigl(\widehat Y_U^{(1)}+Y_{U,\varepsilon}\bigr)
 +(r_U-g_\varepsilon)
 +Z_U^{\rm quad}+Z_U^{\rm tail}+E_{U,\varepsilon}.
\]
Insert this admissible pair into the exact dual formula.  First let `U -> infinity` with `epsilon` fixed, using (R17.5), (R17.11), and (R17.14); then let `epsilon -> 0`.  One gets
\[
\boxed{
\sigma_U(J_{R,U}z_U,J_{R,U}z_U)\longrightarrow0.
}
\tag{R17.15}
\]
Since `ell_U(z_U)=0`, the rank-one TC1 form vanishes exactly.  Therefore
\[
\boxed{
D_U(z_U,z_U)\longrightarrow0.
}
\tag{R17.16}
\]

Thus the three R16 bounded-scale possibilities are resolved: there is no positive bounded limit and no bounded nonconvergent oscillation.  The scalar Schur core decays to zero.

No quantitative rate beyond `o(1)` is claimed here.

---

## 5. The full near-null energy has an exact Gamma limit

Terminal Gamma compatibility gives
\[
q_U^X(J_{R,U}z_U)
=\mathfrak c_{\Gamma,R}[z_U]+D_U(z_U,z_U).
\]
Since `z_U -> f_m` in the fixed smooth source space, the Gamma form is continuous on this finite-dimensional family.  Using (R17.16),
\[
\boxed{
q_U^X(J_{R,U}z_U)
\longrightarrow
\mathfrak c_{\Gamma,R}[f_m]>0.
}
\tag{R17.17}
\]
Thus after exact rank-one cancellation the second scalar layer of the **full** metric is purely archimedean: the Schur remainder disappears and the fixed Gamma floor survives.

At the fixed baseline `T_0`, similarly
\[
q_{T_0}^X(J_{R,T_0}z_U)\to q_{T_0}^X(J_{R,T_0}f_m),
\]
so the near-null relative Rayleigh quotient has the positive finite limit
\[
\boxed{
\rho_{T_0,U}(z_U)
\longrightarrow
\frac{\mathfrak c_{\Gamma,R}[f_m]}
{q_{T_0}^X(J_{R,T_0}f_m)}.
}
\tag{R17.18}
\]
The exponential conditioning witness of R16 remains valid.

---

## 6. The proposed scalar R/S core comparison is not a gauge diagnostic

Let `0<R<S` and choose the fixed jet pair `f_0,f_m` in `C_c^infty((-R,R))`.  View the same vectors at level `S` by zero extension.  For every terminal `U>S`, the graph cocycle gives the same terminal vector:
\[
J_{S,U}J_{R,S}f=J_{R,U}f.
\]
The terminal functional
\[
\ell_U(f)=\langle H_U^*J_{\cdot,U}f,1_U\rangle
\]
therefore has the same value whether the vector is regarded as originating at level `R` or at level `S`.  Hence the exact near-null combination is compatible:
\[
\boxed{z_U^{S}=J_{R,S}z_U^{R}.}
\tag{R17.19}
\]
But `D_U` is a terminal form built only from `H_U`, `R_U`, and `1_U`.  Therefore on this canonically compatible vector
\[
\boxed{
D_U^{(S)}(z_U^{S},z_U^{S})
=D_U^{(R)}(z_U^{R},z_U^{R})
}
\tag{R17.20}
\]
identically, not merely asymptotically.

Thus a difference of these scalar near-null Schur cores cannot carry the `R`/`S` polar-gauge commutator.  The gauge obstruction lives in the operator-valued orientation of the full base/future metric pairs and their square roots, not in this source-compatible terminal scalar.

This is a negative result about the proposed Stage 2 route, not a negative result about gauge convergence itself.

---

## 7. Updated frontier

R17 resolves the scalar bounded-core question completely:
\[
D_U(z_U,z_U)\to0,
\qquad
q_U^X(Jz_U)\to\mathfrak c_{\Gamma,R}[f_m].
\]
The remaining gauge problem is therefore no longer a scalar bounded-core problem.  A successful next step must retain operator-valued information: off-diagonal finite-jet Gram data, the interaction with the fixed Gamma matrix, and compatibility of the resulting positive/inverse square roots under `R -> S`.

No conclusion about
\[
\Gamma_U\to I,
\qquad
K_{R,S}^{T_0,U}\to I,
\qquad
W_{R,S,-}^{[U]}\text{ strong Cauchy},
\]
Object X, Seal, or RH follows from R17.
