# X-C1 ACTIVE-SET SEGMENT-SCHUR — prime-label-independent tail Gram and endpoint transfer

**Date:** 2026-09-18  
**Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`  
**Parent:** PR #137 head `213edfd33d77b57c7ca272696be41339bf703f67`.  
**Scope:** the connected two-Mellin NULLPOL family on bounded windows. This is a reusable sufficient-condition theorem for arbitrary finite active prime-power sets. It does **not** assert a new positive endpoint beyond `a=log(2)` by itself.

## 1. Universal active-set family

On
\[
H=L^2((-1,1),d\mu),\qquad d\mu=d\xi/2,
\]
write
\[
D_HP_n=H_nP_n,\qquad V(\xi)=-\frac12\log(1-\xi^2),
\]
\[
q_0(a)=-\log(2\pi a)-\gamma,
\qquad
(K_af)(\xi)=2a\int_{-1}^1g(a|\xi-\eta|)f(\eta)d\mu(\eta).
\]
For a prime power `q=p^k`, put
\[
w_q=\frac{\Lambda(q)}{\sqrt q}=\frac{\log p}{p^{k/2}},
\qquad d_q(a)=\frac{\log q}{a},
\]
and, for every `0<d<2`, define the zero-extended partial translation
\[
(T_df)(\xi)=f(\xi+d)1_{\xi<1-d}+f(\xi-d)1_{\xi>-1+d}.
\tag{1}
\]
At `d=2` the overlap has measure zero and the operator is zero.

For a bounded endpoint `B`, let
\[
\mathcal A_B=\{q=p^k:\log q<2B\}.
\]
The connected nonpole form is exactly
\[
\boxed{
q_B=D_H+V+q_0(B)I-K_B-S_B,
\qquad
S_B=\sum_{q\in\mathcal A_B}w_qT_{d_q(B)}.
}
\tag{2}
\]
This is the same prime-label-independent family already isolated in the parent package. The point of the present theorem is that the **full infinite-tail Gram of (2)** can be assembled without any assumption `d_q>=1` and without deriving a new architecture when a new prime power enters.

## 2. Exact band-intersection calculus for arbitrary shifts

For `sigma in {+1,-1}` define
\[
I_\sigma(d)=\{x\in(-1,1):-1<x+\sigma d<1\}.
\]
Thus
\[
I_+(d)=(-1,1-d),\qquad I_-(d)=(-1+d,1).
\]
For Legendre polynomials `P_i,P_j`, linearity of (1) gives
\[
\boxed{
\langle P_i,T_dP_j\rangle
=\frac12\sum_{\sigma=\pm1}
\int_{I_\sigma(d)}P_i(x)P_j(x+\sigma d)\,dx.
}
\tag{3}
\]
No disjoint-band hypothesis is used. In particular (3) remains valid for `0<d<1`, where both translated branches are simultaneously active on a central region.

For two arbitrary shifts `0<d,e<2`, the complete mixed translation Gram is
\[
\boxed{
\langle T_dP_i,T_eP_j\rangle
=\frac12\sum_{\sigma,\tau=\pm1}
\int_{I_\sigma(d)\cap I_\tau(e)}
P_i(x+\sigma d)P_j(x+\tau e)\,dx.
}
\tag{4}
\]
Each nonempty intersection is an interval whose endpoints belong to
\[
\{-1,1,1-d,-1+d,1-e,-1+e\}.
\]
The integrand is a polynomial. Therefore every term in (3)--(4) is an exact algebraic expression in the shift parameters. With rational interval enclosures for the logarithms, outward `Fraction` arithmetic gives rigorous enclosures. This treats self terms and every mixed prime-power term by one formula.

For the weighted active set,
\[
S_{ij}=\langle P_i,S_BP_j\rangle
=\sum_{q\in\mathcal A_B}w_q\langle P_i,T_{d_q}P_j\rangle,
\tag{5}
\]
\[
(S^2)_{ij}
=\sum_{q,r\in\mathcal A_B}w_qw_r
\langle T_{d_q}P_i,T_{d_r}P_j\rangle.
\tag{6}
\]
Hence mixed-prime interference is retained before any tail estimate.

## 3. Exact logarithmic/shift cross terms

Let
\[
V(x)=-\tfrac12[\log(1-x)+\log(1+x)].
\]
Then
\[
\boxed{
\langle VP_i,T_dP_j\rangle
=\frac12\sum_{\sigma=\pm1}
\int_{I_\sigma(d)}V(x)P_i(x)P_j(x+\sigma d)\,dx.
}
\tag{7}
\]
After expanding the polynomial product, only moments of
`x^n log(1-x)` and `x^n log(1+x)` remain. The following antiderivatives are elementary and valid on `(-1,1)`:
\[
A_n^-(x)=
\frac{x^{n+1}-1}{n+1}\log(1-x)
-\frac1{n+1}\sum_{k=1}^{n+1}\frac{x^k}{k},
\tag{8}
\]
\[
A_n^+(x)=
\frac{x^{n+1}}{n+1}\log(1+x)
-\frac1{n+1}
\left[
\sum_{k=0}^{n}(-1)^k\frac{x^{n-k+1}}{n-k+1}
+(-1)^{n+1}\log(1+x)
\right].
\tag{9}
\]
Direct differentiation gives
\[
(A_n^-)'=x^n\log(1-x),\qquad
(A_n^+)'=x^n\log(1+x).
\]
Thus (7) is an exact finite expression at the band endpoints. The formula covers negative lower endpoints, which are unavoidable once a channel has `d<1`.

## 4. Complete tail Gram for a finite active set

Let `K_B^p` be a polynomial-kernel approximation to the bounded regular Gamma operator with a rigorous operator error. Put
\[
B_{\rm op}=V-K_B^p,
\qquad C_{\rm op}=B_{\rm op}-S_B.
\]
Fix a parity. Let `Z` contain all modes of that parity through a finite cutoff `N`, including the moment carrier `j=0` or `j=1`, and let `Y=Z^\perp` in that parity.

For low indices `i,l`, Parseval gives the **entire**, not truncated, tail matrices
\[
E^B_{il}=\langle P_YB_{\rm op}P_i,P_YB_{\rm op}P_l\rangle,
\tag{10}
\]
\[
E^S_{il}=\langle P_YS_BP_i,P_YS_BP_l\rangle
=(S^2)_{il}-\sum_{k\in Z}(2k+1)S_{ik}S_{kl},
\tag{11}
\]
\[
E^{BS}_{il}=\langle P_YB_{\rm op}P_i,P_YS_BP_l\rangle.
\tag{12}
\]
For (12), the `V-S` term is obtained from (7), while the `K^p-S` correction has finite Legendre support because `K^pP_i` is a polynomial of finite degree. Therefore no infinite series is discarded.

The complete active-set coupling Gram is
\[
\boxed{
E^C=E^B+E^S-E^{BS}-(E^{BS})^*.
}
\tag{13}
\]
This is exactly the Gram matrix of the full tail coupling
\[
P_Y(V-K_B^p-S_B)P_Z.
\]
Equations (3)--(13) are independent of the number, primality label, or ordering of the active shifts.

## 5. Two Mellin conditions and the abstract Schur certificate

For parity `j=0,1`, let
\[
m_0(x)=\cosh(Bx/2),\qquad m_1(x)=\sinh(Bx/2),
\]
and on the complement of `P_j` define the exact moment map
\[
\mathcal Mx=x-\frac{\langle x,m_j\rangle}{\langle P_j,m_j\rangle}P_j.
\tag{14}
\]
This imposes exactly one condition per parity and hence exactly the original two Mellin conditions in total.

Let `M^0` be the finite low-mode realization of (14), equal to the identity on `Y`, and suppose a rigorous form-error estimate gives
\[
\|\mathcal M^*q_B\mathcal M-(\mathcal M^0)^*q_B^p\mathcal M^0\|\le e.
\tag{15}
\]
Write the actual constrained form in low/tail blocks
\[
F=\begin{pmatrix}A&C^*\\C&D\end{pmatrix},
\qquad D\succeq\delta I>0.
\]
Let `A^0` be the finite low block of the model and let `G` be (13) after applying the finite moment congruence to both indices. If `t>0`, then
\[
C^*C\preceq G^{\rm act}:=(1+t)G+(1+t^{-1})e^2J,
\tag{16}
\]
where `J` is the low-basis Gram matrix.

Consequently
\[
A-C^*D^{-1}C
\succeq A^0-eJ-\delta^{-1}G^{\rm act}.
\tag{17}
\]
Assume an outward-rational LDL certificate proves
\[
\boxed{
A^0-eJ-\delta^{-1}G^{\rm act}-\sigma J\succ0
}
\tag{18}
\]
for some `sigma>0` in each parity. Then the **actual infinite-dimensional Schur complement** is at least `sigma` in the source norm of the low coordinates.

If in addition
\[
R^2\ge\|D^{-1}C\|^2,
\tag{19}
\]
then the inverse triangular shear has norm at most `1+R`, and square completion gives
\[
F[x]\ge\frac{\min\{\sigma,\delta\}}{(1+R)^2}\|x\|^2.
\tag{20}
\]
Finally, if the exact Mellin map satisfies
\[
\|\mathcal Mx\|^2\le(1+\beta_j)\|x\|^2,
\tag{21}
\]
then on the physical parity kernel
\[
\boxed{
q_B[u]\ge
\frac{\min\{\sigma,\delta\}}
{(1+R)^2(1+\beta_j)}\|u\|^2.
}
\tag{22}
\]
No `beta` subtraction is hidden: the complete low-mode moment congruence is already inside `A^0,G`; (21) is only the final norm conversion.

## 6. Segment transfer from one endpoint

For `0<a<=B`, let `J_{a,B}` be physical zero extension written on the reference space:
\[
(J_{a,B}f)(\xi)=\sqrt{B/a}\,f((B/a)\xi)1_{|\xi|<a/B}.
\tag{23}
\]
It preserves `H^1_0`, scales both Mellin moments by `sqrt(a/B)`, and satisfies the exact form identity
\[
q_B[J_{a,B}f]=q_a[f].
\tag{24}
\]
Therefore any endpoint gap from (22) transfers **with the same constant** to every smaller window:
\[
\boxed{
q_a[u]\ge\varepsilon_B\|u\|^2
\quad(0<a\le B),
\qquad
\varepsilon_B=
\min_{j=0,1}
\frac{\min\{\sigma_j,\delta_j\}}
{(1+R_j)^2(1+\beta_j)}.
}
\tag{25}
\]
There is no parameter grid and no Lipschitz-width loss. Lipschitz control remains useful for diagnostics and perturbation arguments but is not the continuum-transfer mechanism.

## 7. Meaning for the next prime-power segment

At
\[
B=\frac{\log5}{2}
\]
the active set is exactly
\[
\mathcal A_B=\{2,3,4\},
\]
while `5` has zero-measure overlap. Here
\[
d_2=\frac{2\log2}{\log5}<1,
\]
so the Prime-2 channel has overlapping left/right active bands. This is precisely the regime excluded by the old `d>=1` shortcut but included by (3)--(13).

Thus the next endpoint certificate requires **no new operator architecture**. It requires only:

1. interval enclosures of `d_2,d_3,d_4` and their weights;
2. the generic band-intersection matrices (3)--(7);
3. the same Gamma-polynomial, moment, tail, Schur, shear, and final norm steps;
4. an LDL proof of (18).

## 8. Scope firewall

This theorem proves a reusable exact **certificate architecture** and segment-transfer theorem. It does not prove that condition (18) holds at `B=log(5)/2`, `B=log(7)/2`, or `B=1`. Failure of a chosen cutoff, polynomial degree, or tail bound is only failure of that certificate instance, not a negative Weil vector and not a C15 necessity.

Likewise, the theorem is not full C1-GEOM, Object X, or RH. What it removes is the need for a prime-specific derivation of the tail Gram every time a new prime power enters.
