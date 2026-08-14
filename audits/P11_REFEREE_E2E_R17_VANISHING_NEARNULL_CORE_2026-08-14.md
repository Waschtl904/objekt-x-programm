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

The R16 bounded Schur core is not a nonzero second asymptotic layer.  The exact residual left after the first future-edge certificate is itself mean zero and uniformly smooth/bounded, so the signed future-edge/full-rest construction can be applied a second time.  Consequently
\[
\boxed{D_U(z_U,z_U)\to0.}
\]
The full graph energy therefore converges to the fixed Gamma floor
\[
\boxed{q_U^X(J_{R,U}z_U)\to\mathfrak c_{\Gamma,R}[f_m]>0.}
\]

Moreover, for canonically compatible vectors under `R -> S` zero extension, the terminal near-null vector and its scalar TC1 remainder are literally the same terminal object.  Thus the proposed scalar comparison of `D_U` at the two source levels cannot encode the gauge commutator; that route is false as stated.

Canonical statuses:

- [R17-A] global bounded hub-remainder operator / convergence: **✓[M]**;
- [R17-B] second mean-zero future-edge absorption: **✓[M]**;
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
Since translations preserve `L^2`, `L^1`, and the fixed smooth seminorms, the second series converges absolutely in operator norm on `L^2`, and on the fixed smooth source core also in the corresponding `L^1/C^1` bounds.

After zero extension of the terminal remainder to the ambient line, dominated convergence over this absolutely summable coefficient family gives
\[
E_U h_U^{\rm rem}(z_U)
\longrightarrow
\mathcal H_{\rm rem,\infty}^*f_m
\qquad\text{in }L^2(\mathbb R),
\tag{R17.2}
\]
because `z_U -> f_m` in every fixed smooth seminorm.  In fact the same argument gives `L^1` convergence.  Every full-line translation difference has zero integral, hence
\[
\int_{\mathbb R}\mathcal H_{\rm rem,\infty}^*f_m=0.
\tag{R17.3}
\]
Thus Stage 1 of the proposed R17 program is positive: the bounded hub remainder itself has a canonical global limit.

Important: this does not yet identify the Schur energy, because the terminal denominator `A_U=I+R_U^*R_U` continues to change with `U`.

---

## 2. Exact residual after the first R16 certificate

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
Define the bounded residual
\[
r_U:=\mu_U1_U+h_U^{\rm rem}(z_U).
\tag{R17.6}
\]
Because `ell_U(z_U)=<h_U,1_U>=0` and `K_U=<h_U^grow,1_U>`, one has exactly
\[
\boxed{\langle r_U,1_U\rangle=0.}
\tag{R17.7}
\]
R16 gives `||mu_U1_U||_2=O(1)`, and the absolute higher-prime-power summability above gives uniform `L^2` and interior `C^1` bounds for `h_U^rem(z_U)`.  Hence `r_U` is an even, mean-zero, uniformly bounded smooth terminal profile.

---

## 3. A second future-edge certificate absorbs the bounded residual

For an even terminal test vector `e`, put as in the proof of Theorem 6.1
\[
b_U(t)=e(U-t),\qquad 0<t<U,
\]
and define for the residual
\[
k_U^{\rm rem}(t):=2r_U(U-t).
\tag{R17.8}
\]
Equation (R17.7) gives
\[
\int_0^U k_U^{\rm rem}(t)\,dt=0.
\]
Therefore the same anchor identity used in (6.15)--(6.16) applies verbatim:
\[
\int_0^U k_U^{\rm rem}(t)\overline{b_U(t)}dt
=
\iint C_{U,\rm rem}^-(r,t)
\overline{\bigl(b_U(t)-b_U(2r-t)\bigr)}\,dt\,dr,
\]
with
\[
C_{U,\rm rem}^-(r,t)=2k_U^{\rm rem}(t)\alpha(2r-t).
\tag{R17.9}
\]
The continuous primitive certificate cost now tends to zero absolutely.  Indeed,
\[
e^{-U}\int_0^U e^{t/2}|k_U^{\rm rem}(t)|^2dt
\le
 e^{-U/2}\|k_U^{\rm rem}\|_2^2
=O(e^{-U/2}).
\tag{R17.10}
\]

The source-representer derivative is uniformly bounded because `r_U` has a uniform interior `C^1` bound.  All cells needed in (R17.9) satisfy
\[
r\le \frac{U+\varepsilon}{2},
\]
so at the corresponding prime scale the `theta=3/5` cells of the R1 proof have maximum width
\[
\max_I|I|\ll e^{-2U/5}.
\]
The same mass-normalized prime quadrature therefore produces a discrete primitive certificate with norm tending to zero and source quadrature error tending to zero.  The full-rest `a=0` primitive-plus-tail lift again has tail norm tending to zero by (6.25).

Consequently there exist `Y_U^(2)` and `E_U^(2)` with
\[
\boxed{
r_U=\widetilde R_U^*Y_U^{(2)}+E_U^{(2)},
\qquad
\|Y_U^{(2)}\|_{\mathscr Z_U}\to0,
\qquad
\|E_U^{(2)}\|_2\to0.}
\tag{R17.11}
\]
This is not a new number-theoretic input; it is a second use of the already audited signed future-edge/full-rest construction, now on a bounded mean-zero profile.

---

## 4. The bounded TC1 core vanishes

Combine (R17.4) and (R17.11):
\[
h_U
=\widetilde R_U^*\bigl(\widehat Y_U^{(1)}+Y_U^{(2)}\bigr)
 +Z_U^{\rm quad}+Z_U^{\rm tail}+E_U^{(2)}.
\]
The exact dual formula (6.2) gives
\[
\sigma_U(J_{R,U}z_U,J_{R,U}z_U)
\le
\|\widehat Y_U^{(1)}+Y_U^{(2)}\|^2
+
\|Z_U^{\rm quad}+Z_U^{\rm tail}+E_U^{(2)}\|_2^2
\longrightarrow0.
\]
Since `ell_U(z_U)=0`, the rank-one TC1 form vanishes exactly and hence
\[
\boxed{
D_U(z_U,z_U)
=\sigma_U(J_{R,U}z_U,J_{R,U}z_U)
\longrightarrow0.}
\tag{R17.12}
\]
Thus the three R16 bounded-scale possibilities are resolved: there is no positive bounded limit and no bounded nonconvergent oscillation.  The scalar Schur core decays to zero.

No quantitative rate beyond `o(1)` is claimed here; the first certificate has squared cost `O(U^{-1})`, but the already recorded quadrature/tail remainders are only needed at `o(1)` strength for this conclusion.

---

## 5. The full near-null energy has an exact Gamma limit

Terminal Gamma compatibility gives
\[
q_U^X(J_{R,U}z_U)
=\mathfrak c_{\Gamma,R}[z_U]+D_U(z_U,z_U).
\]
Since `z_U -> f_m` in the fixed smooth source space, the Gamma form is continuous on this finite-dimensional family.  Using (R17.12),
\[
\boxed{
q_U^X(J_{R,U}z_U)
\longrightarrow
\mathfrak c_{\Gamma,R}[f_m]>0.}
\tag{R17.13}
\]
Thus after exact rank-one cancellation the second scalar layer of the **full** metric is purely archimedean: the Schur remainder disappears and the fixed Gamma floor survives.

At the fixed baseline `T_0`, similarly
\[
q_{T_0}^X(J_{R,T_0}z_U)\to q_{T_0}^X(J_{R,T_0}f_m),
\]
so the near-null relative Rayleigh quotient has the positive finite limit
\[
\rho_{T_0,U}(z_U)
\longrightarrow
\frac{\mathfrak c_{\Gamma,R}[f_m]}
{q_{T_0}^X(J_{R,T_0}f_m)}.
\tag{R17.14}
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
\tag{R17.15}
\]
But `D_U` is a terminal form built only from `H_U`, `R_U`, and `1_U`.  Therefore on this canonically compatible vector
\[
\boxed{
D_U^{(S)}(z_U^{S},z_U^{S})
=D_U^{(R)}(z_U^{R},z_U^{R})
}
\tag{R17.16}
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
