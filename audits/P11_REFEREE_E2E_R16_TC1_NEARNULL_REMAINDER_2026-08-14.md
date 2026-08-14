# P11 End-to-End Referee R16 — TC1 near-null remainder collapse

Date: 2026-08-14

Target: determine the first available quantitative scale of the positive TC1 Gram remainder
\[
D_U(z_U,z_U)
\]
on the exact near-null direction from R15,
\[
z_U=f_m-\frac{\ell_U(f_m)}{\ell_U(f_0)}f_0,
\qquad \ell_U(z_U)=0.
\]

## Verdict

The current P11 proof package does **not** determine a nonzero leading constant or a limit for `D_U(z_U,z_U)`.  However, re-running the full Theorem 6.1 dual certificate **uniformly on the fixed two-dimensional space**
\[
E_m=\operatorname{span}\{f_0,f_m\}
\]
gives a much stronger absolute estimate than the R15 little-o bound:
\[
\boxed{D_U(z_U,z_U)=O(1).}
\]
Hence for every fixed `N>0`,
\[
\boxed{D_U(z_U,z_U)=o(e^U/U^N).}
\]
In particular, no lower bound of the form
\[
D_U(z_U,z_U)\ge c\,e^U/U^{2m+2+\alpha}
\]
with fixed `c>0`, `alpha>0` can hold for all sufficiently large `U`.

The full P11 graph energy on this direction does not collapse because the terminal-compatible Gamma form supplies a fixed positive floor:
\[
q_U^X(J_{R,U}z_U)=\mathfrak c_{\Gamma,R}[z_U]+D_U(z_U,z_U)\asymp1.
\]
Consequently the same fixed two-jet block already yields an exponential conditioning witness
\[
\boxed{\kappa(A_{T_0,U}^{R,-})\gtrsim e^U/U^2.}
\]
This strengthens R7's beyond-all-polynomial lower bound.

Canonical statuses:

- [R16-A] uniformization of the R1 dual certificate on a fixed finite-dimensional smooth odd block: **✓[M]**;
- [R16-B] `D_U(z_U,z_U)=O(1)`: **✓[M]**;
- [R16-C] every exponential-times-polynomial lower scale for `D_U(z_U,z_U)` is impossible: **✓[M]_neg**;
- [R16-D] full graph energy on `z_U` is `Theta(1)` because of the Gamma floor: **✓[M]**;
- [R16-E] exponential conditioning witness `kappa(A_{T_0,U}^{R,-}) >= c e^U/U^2`: **✓[M]**;
- [R16-F] actual bounded-scale asymptotic/limit of `D_U(z_U,z_U)`: **?[O]**;
- [R16-G] gauge/cross-terminal convergence: **?[O]**.

---

## 1. Uniform finite-dimensional setup

Fix smooth odd `f_0,f_m` with first nonzero integral-jet orders `0` and `m>0`.  By the TC1 boundary formula,
\[
\ell_U(f_0)
=-\sqrt2\,c_0\beta_R^{(0)}(f_0)\frac{e^{U/2}}{U^{1/2}}(1+O(U^{-1})),
\]
\[
\ell_U(f_m)
=-\sqrt2\,c_m\beta_R^{(m)}(f_m)\frac{e^{U/2}}{U^{m+1/2}}(1+O(U^{-1})).
\]
Thus
\[
a_U:=\frac{\ell_U(f_m)}{\ell_U(f_0)}=O(U^{-m}),
\qquad
z_U=f_m-a_Uf_0.
\]
Therefore `z_U -> f_m` in every fixed smooth seminorm.  In particular the family `{z_U}` has a common compact support strictly inside `(-R,R)` and uniformly bounded `C^1` and `L^2` norms.

Every estimate in Steps 2--6 of the full proof of Theorem 6.1 is linear/quadratic in finitely many such fixed seminorms.  Hence the constants can be chosen uniformly on bounded subsets of the finite-dimensional space `E_m`.

---

## 2. Exact mean cancellation changes the scale

For a source vector `f`, the R1 proof decomposes
\[
h_U(f)=h_U^{\rm grow}(f)+h_U^{\rm rem}(f),
\]
with
\[
\sup_U\|h_U^{\rm rem}(f)\|_2<\infty
\]
for fixed `f`.  Uniformly on the bounded family `{z_U}` this becomes
\[
\boxed{\|h_U^{\rm rem}(z_U)\|_2\le C.}
\tag{R16.1}
\]
Let
\[
K_U:=\langle h_U^{\rm grow}(z_U),\mathbf1_U\rangle.
\]
Since `ell_U(z_U)=0` exactly,
\[
K_U=-\langle h_U^{\rm rem}(z_U),\mathbf1_U\rangle.
\]
Cauchy--Schwarz and (R16.1) give
\[
\boxed{|K_U|\le C\sqrt U.}
\tag{R16.2}
\]
Define
\[
\mu_U:=\frac{K_U}{2U},
\qquad
k_U^0(t):=k_U(t)-\frac{K_U}{U}.
\]
Then
\[
\boxed{\|\mu_U\mathbf1_U\|_2^2=\frac{|K_U|^2}{2U}=O(1).}
\tag{R16.3}
\]
This is the decisive difference from a fixed source vector, where the extracted constant-mode cost is exponentially large.

---

## 3. Absolute cost of the signed future-edge certificate

The kernel estimate in Theorem 6.1 is uniform for the bounded family `{z_U}`:
\[
|k_U(t)|+|k_U'(t)|
\le C\frac{e^{(U-t)/2}}{\sqrt{1+U-t}}.
\]
Hence the already proved weighted estimate now reads absolutely
\[
\boxed{
e^{-U}\int_0^U e^{t/2}|k_U(t)|^2\,dt=O(U^{-1})+O(e^{-U/4}).
}
\tag{R16.4}
\]
The subtracted constant contributes only
\[
e^{-U}\int_0^Ue^{t/2}\frac{|K_U|^2}{U^2}\,dt
=O(e^{-U/2}/U)
\]
by (R16.2).  Therefore the signed continuous certificate has
\[
\boxed{\|Y_U^{\rm cont,-}\|^2=O(U^{-1}).}
\tag{R16.5}
\]

The prime-cell mass identity and mass-normalized coefficient identity from Step 5 transfer the same absolute scale to the primitive discrete certificate:
\[
\boxed{\|Y_U^{\rm prim,-}\|^2=O(U^{-1}).}
\tag{R16.6}
\]
The source-representer Lipschitz estimate is uniform on `{z_U}`.  Since the future-cell mesh is exponentially small, the quadrature source error satisfies
\[
\boxed{\|Z_U^{\rm quad}\|_2=o(1).}
\tag{R16.7}
\]
(The constant part contributes `O(|K_U|e^{-2U/5})=o(1)`.)

Finally the exact full-rest lift has future tail norm
\[
\|E_U^{\rm fut}\|\le C\sqrt{U+1}\,e^{-U/2}.
\]
Together with (R16.6),
\[
\boxed{\|Z_U^{\rm tail}\|_2=o(1).}
\tag{R16.8}
\]

---

## 4. Dual squeeze on the exact near-null vector

The full-rest certificate therefore gives
\[
h_U(z_U)=\widetilde R_U^*\widehat Y_U^-+Z_U^{\rm full},
\]
where
\[
Z_U^{\rm full}
=\mu_U\mathbf1_U+h_U^{\rm rem}(z_U)+Z_U^{\rm quad}+Z_U^{\rm tail}.
\]
Equations (R16.1), (R16.3), (R16.7), (R16.8) imply
\[
\|Z_U^{\rm full}\|_2=O(1),
\qquad
\|\widehat Y_U^-\|^2=O(U^{-1}).
\]
Insert this admissible pair into the exact dual formula
\[
\langle h_U,A_U^{-1}h_U\rangle
=\inf_Y\bigl(\|h_U-\widetilde R_U^*Y\|_2^2+\|Y\|^2\bigr).
\]
Thus
\[
\boxed{\sigma_U(J_{R,U}z_U,J_{R,U}z_U)=O(1).}
\tag{R16.9}
\]
But `ell_U(z_U)=0`, so the TC1 rank-one form is exactly zero and
\[
D_U(z_U,z_U)=\sigma_U(Jz_U,Jz_U).
\]
Hence
\[
\boxed{D_U(z_U,z_U)=O(1).}
\tag{R16.10}
\]

For every fixed `N>0`,
\[
\frac{D_U(z_U,z_U)}{e^U/U^N}
=O(U^Ne^{-U})\to0.
\]
This proves the superpolynomial-relative collapse
\[
\boxed{D_U(z_U,z_U)=o(e^U/U^N)\quad\forall N>0.}
\tag{R16.11}
\]

---

## 5. Gamma floor and full graph scale

The actual P11 graph metric is
\[
q_U^X(J_{R,U}f)=\mathfrak c_{\Gamma,R}[f]+\sigma_U(J_{R,U}f).
\]
Gamma compatibility makes the first term independent of `U`.  Since `z_U -> f_m != 0`, positivity of the fixed Gamma form gives constants `0<c<C<infty` with
\[
c\le \mathfrak c_{\Gamma,R}[z_U]\le C
\]
for all sufficiently large `U`.  Combining this with (R16.10) and positivity of `D_U`,
\[
\boxed{q_U^X(J_{R,U}z_U)\asymp1.}
\tag{R16.12}
\]
Thus the Schur near-null direction falls to bounded scale, while the full graph metric is prevented from collapsing by the archimedean/Gamma floor.

---

## 6. Exponential conditioning witness

At baseline `T_0`, `z_U -> f_m`, so
\[
q_{T_0}^X(J_{R,T_0}z_U)\asymp1.
\]
Therefore the relative Rayleigh quotient satisfies
\[
\rho_{T_0,U}(z_U)=O(1).
\tag{R16.13}
\]
For the fixed first-jet-zero vector `f_0`, Theorem 6.1 gives
\[
\rho_{T_0,U}(f_0)\asymp e^U/U^2.
\tag{R16.14}
\]
Since the condition number is `sup rho / inf rho`,
\[
\kappa(A_{T_0,U}^{R,-})
\ge \frac{\rho_{T_0,U}(f_0)}{\rho_{T_0,U}(z_U)}
\ge c\frac{e^U}{U^2}
\]
for all sufficiently large `U`.

Hence
\[
\boxed{\kappa(A_{T_0,U}^{R,-})\gtrsim e^U/U^2.}
\tag{R16.15}
\]
This is strictly stronger than the R7 statement that the condition number beats every fixed power of `U`.

---

## 7. Firewall and next target

R16 does **not** determine the first nonzero bounded-scale asymptotic of `D_U(z_U,z_U)`.  The possibilities
\[
D_U(z_U,z_U)\to d>0,
\qquad
D_U(z_U,z_U)\to0,
\qquad
\text{or bounded oscillation}
\]
remain open.

Nor does (R16.15) decide the polar gauges.  It strengthens the conditioning information but supplies no asymptotic orientation of the positive/inverse square roots and no proof of
\[
\Gamma_U\to I,
\qquad
K_{R,S}^{T_0,U}\to I.
\]

The immediate next quantitative target is therefore the **bounded core** left after the future-edge certificate: identify whether the residual energy represented by `h_U^{rem}` and the vanishing certificate errors has a limit, a positive lower bound, or further cancellation.  Any such result must then be compared compatibly between the `R` and `S` finite-jet blocks.

No strong-terminal, Object-X, Seal, or RH conclusion follows from R16.