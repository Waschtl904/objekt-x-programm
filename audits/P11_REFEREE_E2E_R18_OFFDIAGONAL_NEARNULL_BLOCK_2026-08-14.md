# P11 End-to-End Referee R18 — off-diagonal near-null block and source-compatible block firewall

Date: 2026-08-14

## Target

Audit the proposed gauge diagnostic
\[
\sigma_U(J_{R,U}f_0,J_{R,U}z_U),
\qquad
z_U=f_m-\frac{\ell_U(f_m)}{\ell_U(f_0)}f_0,
\qquad \ell_U(z_U)=0,
\]
where `f_0,f_m` are fixed smooth odd source vectors with first integral-jet orders `0` and `m>0`.

The questions are:

1. What is the sharp scale currently forced for the mixed TC1 entry on `(f_0,z_U)`?
2. Does the corresponding full two-vector Gram block retain a nontrivial future angle?
3. Can this off-diagonal scalar, or more generally any finite source-compatible Gram block, carry an `R/S` polar-gauge difference?

# Verdict

The mixed TC1 entry is smaller than the geometric mean scale suggested by the leading rank-one boundary mode:
\[
\boxed{
\sigma_U(Jf_0,Jz_U)
=o\!\left(\frac{e^{U/2}}{U}\right).
}
\]
In the full P11 form the fixed Gamma term is only `O(1)`, hence the normalized future angle satisfies
\[
\boxed{
\frac{q_U^X(Jf_0,Jz_U)}
{q_U^X(Jf_0)^{1/2}q_U^X(Jz_U)^{1/2}}
\to0.
}
\]
Thus after exact boundary-mode cancellation the full two-vector future Gram block is asymptotically orthogonal after diagonal normalization.

However, the proposed use of this mixed entry as an `R/S` gauge diagnostic is false.  The cocycle preserves **every** matrix element of the terminal form on a canonically nested source block, not merely diagonal Rayleigh quotients.  In fact, for any finite family at level `R`, the complete pair of finite Gram matrices at terminals `T_0` and `U` is identical to the pair obtained after zero extension to level `S`.  Therefore no scalar or finite matrix quantity built only from such source-compatible terminal pairings can measure the polar-gauge difference.

The remaining gauge information is necessarily off-block: it lives in the interaction of the nested source image with its `T_0`-orthogonal complement before the full operator square root/polar factor is taken.

Canonical statuses:

- [R18-A] exact mixed rank-one cancellation `rho_U(f_0,z_U)=0`: **✓[M]**;
- [R18-B] mixed TC1 suppression `sigma_U(f_0,z_U)=o(e^{U/2}/U)`: **✓[M]**;
- [R18-C] normalized full-Gram angle tends to zero: **✓[M]**;
- [R18-D] complete finite source-compatible Gram-pair cocycle invariance: **✓[M]**;
- [R18-E] proposed `(f_0,z_U)` off-diagonal `R/S` gauge diagnostic: **✓[M]_neg**;
- [R18-F] promotion from internal finite-block square roots to the full polar gauges: **?[O]**.

---

## 1. Exact cancellation of the mixed rank-one term

Recall the TC1 decomposition
\[
\sigma_U(Jf,Jg)=\rho_U(f,g)+D_U(f,g),
\qquad
\rho_U(f,g)=\frac{\ell_U(f)\overline{\ell_U(g)}}{d_U},
\]
with `D_U` positive semidefinite.  Since `ell_U(z_U)=0` exactly,
\[
\boxed{
\rho_U(f_0,z_U)=0,
\qquad
\sigma_U(Jf_0,Jz_U)=D_U(f_0,z_U).
}
\tag{R18.1}
\]
This is stronger than merely cancelling the diagonal rank-one energy on `z_U`: the entire rank-one row/column involving `z_U` vanishes.

---

## 2. Mixed TC1 suppression

Positivity of the TC1 remainder gives the exact Gram Cauchy--Schwarz inequality
\[
|D_U(f_0,z_U)|^2
\le D_U(f_0,f_0)D_U(z_U,z_U).
\tag{R18.2}
\]
For the fixed first-jet-zero vector `f_0`, the mixed-jet proof gives
\[
D_U(f_0,f_0)=o\!\left(\frac{e^U}{U^2}\right).
\tag{R18.3}
\]
R17 gives the much stronger exact-near-null conclusion
\[
D_U(z_U,z_U)\to0.
\tag{R18.4}
\]
Combining (R18.1)--(R18.4),
\[
|\sigma_U(Jf_0,Jz_U)|^2
=o\!\left(\frac{e^U}{U^2}\right),
\]
and therefore
\[
\boxed{
\sigma_U(Jf_0,Jz_U)
=o\!\left(\frac{e^{U/2}}{U}\right).
}
\tag{R18.5}
\]
No absolute `o(1)` conclusion is claimed.  The present proof package still allows the mixed Schur entry to grow subcritically relative to `e^{U/2}/U`.

---

## 3. Full future Gram angle collapses to zero

Write
\[
L_U:=\frac{e^U}{U^2}.
\]
For the fixed vector `f_0`, Theorem 6.1 gives
\[
q_U^X(Jf_0)=a_0L_U(1+o(1))
\qquad(a_0>0),
\tag{R18.6}
\]
because the fixed Gamma contribution is only `O(1)`.

R17 gives
\[
q_U^X(Jz_U)\to
\gamma_m:=\mathfrak c_{\Gamma,R}[f_m]>0.
\tag{R18.7}
\]
For the mixed full form,
\[
q_U^X(Jf_0,Jz_U)
=\mathfrak c_{\Gamma,R}[f_0,z_U]
 +\sigma_U(Jf_0,Jz_U).
\]
Since `z_U -> f_m` in the fixed smooth source space,
\[
\mathfrak c_{\Gamma,R}[f_0,z_U]
\to\mathfrak c_{\Gamma,R}[f_0,f_m],
\]
so the Gamma mixed term is `O(1)`.  Equation (R18.5) therefore gives
\[
q_U^X(Jf_0,Jz_U)=o(L_U^{1/2}).
\tag{R18.8}
\]
Consequently
\[
\boxed{
\frac{q_U^X(Jf_0,Jz_U)}
{q_U^X(Jf_0)^{1/2}q_U^X(Jz_U)^{1/2}}
\to0.
}
\tag{R18.9}
\]

Equivalently, if
\[
M_U:=
\begin{pmatrix}
q_U^X(Jf_0) & q_U^X(Jf_0,Jz_U)\\
q_U^X(Jz_U,Jf_0) & q_U^X(Jz_U)
\end{pmatrix}
\]
and
\[
S_U:=\operatorname{diag}
\bigl(q_U^X(Jf_0)^{-1/2},q_U^X(Jz_U)^{-1/2}\bigr),
\]
then
\[
\boxed{S_UM_US_U\to I_2.}
\tag{R18.10}
\]
In particular
\[
\det M_U
\sim a_0\gamma_m L_U.
\tag{R18.11}
\]
Thus the pure-Gamma second scalar layer found in R17 is not destroyed by the mixed entry.

This is an internal two-vector Gram statement.  It is **not** an identity for the compression of the full operator square root.

---

## 4. Finite source-compatible blocks are cocycle-invariant as complete form pairs

Let `0<R<S<T` and let `e_1,...,e_n` be any finite family in the source graph space at level `R`.  Put
\[
e_i^S:=J_{R,S}e_i.
\]
For every terminal `T>S`, the graph cocycle gives
\[
J_{S,T}e_i^S=J_{R,T}e_i.
\]
Hence, using `G_{X,T}=J_{X,T}^*J_{X,T}` with the graph-Hilbert adjoints,
\[
\boxed{
\langle G_{S,T}e_i^S,e_j^S\rangle_{X,S}
=
\langle G_{R,T}e_i,e_j\rangle_{X,R}
}
\tag{R18.12}
\]
for every `i,j`.

Apply this first with `T=T_0` and then with the future terminal `T=U`.  The complete finite matrix pair
\[
\left(
[\langle G_{R,T_0}e_i,e_j\rangle],
[\langle G_{R,U}e_i,e_j\rangle]
\right)
\]
is therefore exactly identical to the corresponding pair at level `S` after canonical source inclusion.

This remains true for `U`-dependent finite families, pointwise in `U`, provided the `S`-level vectors are the canonical images of the `R`-level vectors.  In particular it applies to `(f_0,z_U)`.

Therefore all quantities computed solely from this finite pair of matrices --- entries, determinants, finite generalized eigenvalues, internal Ritz metrics, or matrix functions of that finite generalized problem --- are source-compatible and cannot themselves produce an `R/S` difference.

---

## 5. Why this does not trivialize the actual polar gauge

The full polar gauges are formed from the full positive operators
\[
X_R=(G_{R,U})^{1/2}(G_{R,T_0})^{-1/2},
\qquad
X_S=(G_{S,U})^{1/2}(G_{S,T_0})^{-1/2}.
\]
Finite compression does not commute with functional calculus in general:
\[
P_EA^{1/2}P_E
\ne
(P_EAP_E)^{1/2}.
\tag{R18.13}
\]
R14 already supplied a canonical-inclusion countermodel showing that perfect internal modulus data can coexist with nontrivial future transport.  Thus (R18.12) is fully compatible with a nontrivial polar gauge.

The missing information is precisely the off-block coupling between the nested source image and its complement before the square root is taken.  In the `T_0`-orthogonal decomposition
\[
\operatorname{Ran}W\oplus(\operatorname{Ran}W)^\perp,
\]
this is represented by quantities such as
\[
(I-WW^*)A_SW,
\]
whose nontrivial size was already detected in R13.  What remains open is how such off-block information propagates through the **square root and polar factor**, not the internal source-compatible Gram block.

---

## 6. Updated frontier

The proposed R18 mixed scalar has now been quantified, but it does not open a new scalar route to the gauge:
\[
\sigma_U(Jf_0,Jz_U)
=o(e^{U/2}/U),
\qquad
\operatorname{corr}_{q_U}(f_0,z_U)\to0.
\]
The entire finite source-compatible `(T_0,U)` Gram pair is already cocycle-invariant between `R` and `S`.

Hence the next genuine gauge attack must retain complement information.  A natural next target is an operator/square-root off-block quantity, for example the relation between
\[
(I-WW^*)A_SW
\quad\text{and}\quad
(I-WW^*)A_S^{1/2}W,
\]
or directly the polar leakage
\[
(I-WW^*)U_SW.
\]
No conclusion about `Gamma_U -> I`, `K_{R,S}^{T_0,U} -> I`, strong terminal transport, Object X, Seal, or RH follows from R18.