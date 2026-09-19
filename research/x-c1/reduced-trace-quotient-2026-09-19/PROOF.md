# X-C1 INHERITED RESONANCE — reduced trace quotient coordinates

**Date:** 2026-09-19  
**Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`  
**Research branch:** `research/x-c1-inherited-resonance-shell-schur-2026-09-18`  
**Parent:** `6f24422ee8e074d387e9656e5307b607edb6c809`.  
**Scope:** exact quotient removal of the duplicated trace mode and an inverse-free reduced Schur gate. No new positive interval theorem.

## 1. Input from the full-shell pivot package

Put
\[
B=\frac{\log 5}{2},\qquad 0<h=b-B\le10^{-20}.
\]
The parent package supplies:

1. an inherited even core Hilbert space `K_B`, carrying a densely defined closed form `A` with
   \[
   A[w]\ge \varepsilon\|w\|_2^2,\qquad \varepsilon=10^{-13};
   \tag{1}
   \]
2. the shell Hilbert space
   \[
   X=\mathbb C\oplus L^2(B,b),\qquad \|(t,s)\|_X^2=|t|^2+\|s\|_2^2,
   \tag{2}
   \]
   carrying a densely defined closed form `D` with
   \[
   D[z]\ge \delta\|z\|_X^2,
   \qquad \delta=\frac1{32\cdot10^{13}};
   \tag{3}
   \]
3. a bounded physical coordinate map
   \[
   \Phi:K_B\oplus X\to\mathcal K_b,
   \tag{4}
   \]
   whose exact kernel is
   \[
   \ker\Phi=\operatorname{span}\{(-\psi,e)\},
   \qquad e=(1,0)\in X,
   \tag{5}
   \]
   and with
   \[
   \widetilde L e=\psi.
   \tag{6}
   \]
   Here `psi` is the moment-corrected **trace mode** with `psi(B)=1`; it is not the previously constructed fast-null source.
4. `psi` lies in the core form domain and `e` lies in the shell operator domain. Thus gauge shifts by multiples of `(-psi,e)` preserve the completed form domain.
5. the completed full pullback form is
   \[
   \mathfrak F((w,z))=A[w]+2\operatorname{Re}C(w,z)+D[z].
   \tag{7}
   \]

The parent proves that the unreduced strict relative estimate cannot hold because the coordinate null direction (5) forces the relative quotient to approach one.

## 2. The `L^2` projection and the gauge map

All orthogonality in this package is with respect to the physical core `L^2` inner product. Put
\[
K_B^0:=K_B\cap\psi^{\perp_{L^2}},
\tag{8}
\]
let
\[
c(w):=\frac{\langle w,\psi\rangle_{L^2}}{\|\psi\|_2^2},
\qquad
P_0w:=w-c(w)\psi,
\tag{9}
\]
and define
\[
\boxed{
G(w,z):=\bigl(P_0w,\ z+c(w)e\bigr).
}
\tag{10}
\]
Since `P_0` is the orthogonal projection onto the closed codimension-one subspace `K_B^0`, `G` is bounded from `K_B direct-sum X` to `K_B^0 direct-sum X`.

### Theorem 2.1 — exact quotient coordinate theorem

The map `G` has the following properties.

1. **Physical invariance.** If
   \[
   \Phi_0(w_0,z):=Jw_0+\widetilde Lz,
   \qquad w_0\in K_B^0,
   \tag{11}
   \]
   then
   \[
   \boxed{\Phi=\Phi_0\circ G.}
   \tag{12}
   \]
2. **Exact kernel.**
   \[
   \boxed{\ker G=\ker\Phi=\operatorname{span}\{(-\psi,e)\}.}
   \tag{13}
   \]
3. **Unique reduced representative.** Every affine gauge class
   \[
   (w,z)+\operatorname{span}\{(-\psi,e)\}
   \tag{14}
   \]
   contains exactly one element of `K_B^0 direct-sum X`, namely `G(w,z)`.
4. **Quotient isomorphism.** `G` induces a bounded linear topological isomorphism
   \[
   \boxed{
   \overline G:
   (K_B\oplus X)/\operatorname{span}\{(-\psi,e)\}
   \xrightarrow{\ \cong\ }
   K_B^0\oplus X.
   }
   \tag{15}
   \]
5. **Form-domain compatibility.** Let `D(A)` and `D(D)` denote the form domains. Then
   \[
   P_0\mathcal D(A)=\mathcal D(A)\cap K_B^0,
   \tag{16}
   \]
   and
   \[
   G\bigl(\mathcal D(A)\oplus\mathcal D(D)\bigr)
   =\bigl(\mathcal D(A)\cap K_B^0\bigr)\oplus\mathcal D(D).
   \tag{17}
   \]
   Hence quotient removal does not leave the completed form domain.

### Proof

Write `w=P_0w+c(w)psi`. Using `J psi=L_tilde e`,
\[
\Phi(w,z)
=JP_0w+c(w)J\psi+\widetilde Lz
=JP_0w+\widetilde L(z+c(w)e)
=\Phi_0(G(w,z)),
\]
which proves (12).

If `G(w,z)=0`, then `P_0w=0`, hence `w=c psi`. The second component gives `z=-c e`. Thus `(w,z)=c(psi,-e)`, which spans the same line as `(-psi,e)`. Conversely `G(-psi,e)=0`. Together with the parent's exact kernel formula for `Phi`, this proves (13).

For any `(w,z)`, equation (10) already gives a representative in `K_B^0 direct-sum X`. If another representative in the same gauge class also has core part orthogonal to `psi`, their difference is `lambda(-psi,e)` and its core part `-lambda psi` is orthogonal to `psi`; hence `lambda=0`. This proves uniqueness.

The induced map (15) is therefore a bounded linear bijection. Since both sides are Hilbert/Banach spaces, the open mapping theorem gives a bounded inverse.

Finally `psi in D(A)`, so subtracting `c(w)psi` preserves `D(A)`. Since `e in D(D)`, adding `c(w)e` preserves `D(D)`. Conversely every reduced pair is fixed by `G`. This proves (16)-(17). `square`

## 3. Reduced physical coordinate map and norm conditioning

The parent package proves that
\[
\Phi_0:K_B^0\oplus X\to\mathcal K_b
\tag{18}
\]
is a bounded bijection onto the complete even physical moment kernel and satisfies
\[
\boxed{
\frac1{32}\bigl(\|w\|_2^2+\|z\|_X^2\bigr)
\le \|\Phi_0(w,z)\|_2^2
\le65\bigl(\|w\|_2^2+\|z\|_X^2\bigr).
}
\tag{19}
\]
Thus the reduced coordinate condition `w perpendicular psi` is **not an additional physical constraint**. The removed core coordinate is present unchanged as the shell trace coordinate along `e`.

Equivalently, (15) identifies the physical completion with the quotient of the redundant coordinates and then chooses the `L^2`-orthogonal gauge slice `K_B^0 direct-sum X`.

## 4. Reduced block form

Let
\[
\mathcal D(A_0)=\mathcal D(A)\cap K_B^0,
\qquad A_0=A|_{K_B^0},
\tag{20}
\]
and let `C_0` be the cross form `C` restricted in its core variable to `K_B^0`. On the reduced form domain
\[
\mathcal D(A_0)\oplus\mathcal D(D)
\tag{21}
\]
the physical quadratic form is exactly
\[
\boxed{
\mathfrak F_0((w,z))
=A_0[w]+2\operatorname{Re}C_0(w,z)+D[z].
}
\tag{22}
\]
No source is removed and no Mellin condition is added.

The inherited and shell lower bounds remain
\[
A_0[w]\ge\varepsilon\|w\|_2^2,
\qquad
D[z]\ge\delta\|z\|_X^2,
\tag{23}
\]
with
\[
\varepsilon=10^{-13},
\qquad
\delta=\frac1{32\cdot10^{13}}.
\tag{24}
\]
The old core bound is inherited unchanged because `K_B^0 subset K_B`.

## 5. The exact reduced coupling target

Define the reduced relative coupling number
\[
\boxed{
\Theta_0(b)
:=
\sup_{\substack{0\ne w\in\mathcal D(A_0)\\0\ne z\in\mathcal D(D)}}
\frac{|C_0(w,z)|^2}{A_0[w]D[z]}.
}
\tag{25}
\]
The denominators are strictly positive by (23). The entire remaining **even** all-source gate on the already certified shell interval is therefore the strict inequality
\[
\boxed{\Theta_0(b)<1.}
\tag{26}
\]
This formulation is inverse-free. If associated operators are used legitimately, (25) agrees with the squared norm of the normalized coupling `D^(-1/2) C_0 A_0^(-1/2)`, but no operator inverse is required for the theorem below.

### Theorem 5.1 — reduced inverse-free continuation criterion

Assume
\[
\Theta_0(b)\le\theta_0<1.
\tag{27}
\]
Then every even physical source `u=Phi_0(w,z)` satisfies
\[
Q_b[u]
\ge(1-\sqrt{\theta_0})\bigl(A_0[w]+D[z]\bigr)
\tag{28}
\]
and consequently
\[
\boxed{
Q_b[u]
\ge
\frac{1-\sqrt{\theta_0}}{65}
\min\{\varepsilon,\delta\}\,\|u\|_2^2.
}
\tag{29}
\]
Since `delta<epsilon`, this becomes
\[
\boxed{
Q_b[u]
\ge
\frac{1-\sqrt{\theta_0}}{2080\cdot10^{13}}\,\|u\|_2^2.
}
\tag{30}
\]

### Proof

By (25)-(27),
\[
2|C_0(w,z)|
\le2\sqrt{\theta_0}\sqrt{A_0[w]D[z]}.
\]
Therefore
\[
\begin{aligned}
\mathfrak F_0
&\ge A_0+D-2\sqrt{\theta_0}\sqrt{A_0D}\\
&\ge(1-\sqrt{\theta_0})(A_0+D),
\end{aligned}
\]
using `2 sqrt(A_0 D)<=A_0+D`. This gives (28). Equations (19) and (23) give
\[
A_0+D
\ge\min(\varepsilon,\delta)(\|w\|_2^2+\|z\|_X^2)
\ge\frac{\min(\varepsilon,\delta)}{65}\|u\|_2^2,
\]
proving (29). Equation (30) is the exact simplification of the constants. `square`

## 6. The fast-null source in the reduced gauge

Let `v_B` denote the explicit previously constructed even fast-null source. Do **not** identify it with the trace mode `psi`. Define
\[
c_v=\frac{\langle v_B,\psi\rangle}{\|\psi\|_2^2},
\qquad
w_v=P_0v_B.
\tag{31}
\]
Then its inherited zero-extension has the exact reduced representation
\[
\boxed{
J_{B,b}v_B=\Phi_0(w_v,c_v e).
}
\tag{32}
\]
Thus the known near-null direction is retained exactly after quotienting. It supplies a sharp diagnostic pair `(w_v,c_v e)` for the reduced coupling, but its Rayleigh quotient is an upper bound on the physical infimum, not a uniform lower reserve for `A_0`.

The next numerical/analytic audit should therefore record separately
\[
A_0[w_v],\qquad D[c_v e],\qquad C_0(w_v,c_v e),
\tag{33}
\]
and compare the resulting directional relative quotient with one. This is a diagnostic for (26), not a replacement for the required supremum over the entire reduced core.

## 7. Scope firewall and next gate

This package removes exactly the coordinate redundancy identified by the parent and proves the reduced inverse-free criterion. It does **not** prove `Theta_0(b)<1`.

No new positive endpoint, no all-parity interval, and no claim at `log(7)/2` or `a=1` follows. The odd sector remains a separate obligation even if (26) is eventually proved.

The next even-sector research gate is now uniquely defined:

\[
\boxed{
\text{certify }\Theta_0(b)<1
\text{ on a nontrivial right interval.}
}
\]

Only after that should the physical even gap (30) be combined with a new odd-sector continuation.
