# X-C1 INHERITED RESONANCE — orthogonal shell coordinates and a surjective nonorthogonal shell lift

**Date:** 2026-09-18  
**Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`  
**Research branch:** `research/x-c1-inherited-resonance-shell-schur-2026-09-18`  
**Base:** consolidated PR #137 milestone `21fade97f35089617d07a111ab64082404084319`.  
**Scope:** structural source-space geometry to the right of `B=log(5)/2`. No new positivity endpoint and no claim at `log(7)/2` or `a=1`.

The consolidation audit at `8074d14508873e09068222b9703b1f34e8607fc6` correctly observes that the naive identity

\[
\mathcal W_b^{\rm even}=E_{B,b}\oplus
(\mathcal W_b^{\rm even}\cap E_{B,b}^{\perp_{L^2}})
\]

is not justified in the `H^1_0` source topology: `E_{B,b}` is not closed in the ambient `L^2` topology and an `L^2` projection onto its closure need not preserve `H^1`. The present note keeps the useful orthogonal subspace, proves its exact structure, and then constructs a different **nonorthogonal but surjective** complement of the old core.

---

## 1. Source spaces and the old core

Put

\[
B=\frac{\log 5}{2},\qquad H(x)=\cosh(x/2),\qquad B<b\le1,
\qquad h=b-B.
\]

In the even sector the two Mellin conditions reduce to the single condition against `H`; the odd moment vanishes by parity. Write

\[
\mathcal W_a^{\rm e}
=\left\{u\in H_0^1((-a,a)):\ u(-x)=u(x),\ 
\int_{-a}^a u(x)H(x)\,dx=0\right\}.
\]

Let

\[
E_{B,b}=J_{B,b}\mathcal W_B^{\rm e}\subset \mathcal W_b^{\rm e}
\]

be physical zero extension of the old even source space.

The exact window law already proved on the frozen milestone gives

\[
Q_b[J_{B,b}w]=Q_B[w],\qquad \|J_{B,b}w\|_2=\|w\|_2.
\tag{1}
\]

---

## 2. The `L^2` closure of the old core

Let

\[
\mathscr K_B=
\left\{f\in L^2_{\rm even}(-B,B):
\int_{-B}^B f(x)H(x)\,dx=0\right\}.
\]

### Lemma 2.1

\[
\overline{\mathcal W_B^{\rm e}}^{\,L^2(-B,B)}=\mathscr K_B.
\tag{2}
\]

### Proof

The inclusion from left to right is immediate because the moment functional is continuous on `L^2(-B,B)`.

Conversely let `f in K_B`. Approximate `f` in `L^2` by even functions `g_n in C_c^infty(-B,B)`. Fix one even `chi in C_c^infty(-B,B)` with `<chi,H> != 0`. Since `<g_n,H> -> <f,H>=0`,

\[
\widetilde g_n
=g_n-\frac{\langle g_n,H\rangle}{\langle\chi,H\rangle}\chi
\]

belongs to `W_B^e` and converges to `f` in `L^2`. This proves (2). `square`

After zero extension to `(-b,b)`, the closure of `E_{B,b}` consists exactly of the even `L^2` functions supported in `[-B,B]` whose `H`-moment on the core vanishes.

---

## 3. Exact orthogonal shell subspace

Define

\[
Z_b=\mathcal W_b^{\rm e}\cap E_{B,b}^{\perp_{L^2(-b,b)}}.
\tag{3}
\]

Put

\[
H_B=H(B),\qquad
A_B=\int_0^B H(x)^2\,dx
=\frac{B+\sinh B}{2}>0,
\tag{4}
\]

and on the right shell `(B,b)`

\[
\ell_h(x)=\frac{b-x}{h},\qquad \ell_h(B)=1,\quad \ell_h(b)=0.
\tag{5}
\]

### Theorem 3.1 — orthogonal-shell coordinate lemma

For every `z in Z_b` there is a unique `r in H_0^1(B,b)` such that, on the positive half interval,

\[
z(x)=
\begin{cases}
\alpha(r)H(x),&0<x<B,\\[1mm]
\alpha(r)H_B\ell_h(x)+r(x),&B<x<b,
\end{cases}
\tag{6}
\]

and `z` is obtained on the negative half by even reflection. Here

\[
\boxed{
\alpha(r)=
-\frac{\displaystyle\int_B^b r(x)H(x)\,dx}
{\displaystyle A_B+H_B\int_B^b\ell_h(x)H(x)\,dx}.
}
\tag{7}
\]

Conversely, every `r in H_0^1(B,b)` inserted into (6)-(7) produces an element of `Z_b`. Thus for every fixed `b>B`,

\[
\boxed{H_0^1(B,b)\ \cong\ Z_b}
\tag{8}
\]

as Hilbert spaces with their `H^1` topologies.

### Proof

Let `z in Z_b`. For every `w in W_B^e`, orthogonality to `J_{B,b}w` gives

\[
\int_{-B}^B z(x)\overline{w(x)}\,dx=0.
\]

By Lemma 2.1 the restriction `z|_{(-B,B)}` is orthogonal to the codimension-one kernel `K_B`. Its orthogonal complement inside the even core `L^2` space is `span{H}`. Hence

\[
z(x)=\alpha H(x)\quad(|x|<B)
\tag{9}
\]

for a unique scalar `alpha`.

An `H^1` function on an interval has a continuous representative. Therefore the right-shell trace satisfies `z(B+)=z(B-)=alpha H_B`, and `z(b)=0`. Hence

\[
r(x):=z(x)-\alpha H_B\ell_h(x)\in H_0^1(B,b).
\tag{10}
\]

The even Mellin condition for `z`, divided by the common factor two, is

\[
0=\alpha A_B+\alpha H_B\int_B^b\ell_hH
+\int_B^b rH,
\]

which is exactly (7). The denominator is strictly positive because every term is nonnegative and `A_B>0`.

Conversely define `z` by (6)-(7). Core and shell traces agree at `B`, the outer trace at `b` vanishes, and even reflection gives an element of `H_0^1(-b,b)`. Equation (7) makes its even Mellin moment zero; odd moment vanishes by parity. For every old core vector `w`, the shell contributes zero and the core pairing is `alpha <H,w>=0`; hence `z in Z_b`.

Injectivity and surjectivity of `r -> z_r` follow from (10). Boundedness for fixed `b` follows from the one-dimensional trace theorem and the explicit formulas; boundedness of the inverse follows from (9)-(10). `square`

---

## 4. Small-shell scale of the orthogonal correction

For `r in H_0^1(B,b)`, the sharp interval Poincare inequality gives

\[
\|r\|_{L^2(B,b)}\le\frac h\pi\|r'\|_{L^2(B,b)}.
\tag{11}
\]

Since `b<=1`, `H(x)<=cosh(1/2)` on the shell. Therefore

\[
\left|\int_B^b rH\right|
\le \frac{\cosh(1/2)}\pi h^{3/2}\|r'\|_2.
\tag{12}
\]

The denominator in (7) is at least `A_B`, so

\[
\boxed{
|\alpha(r)|\le
C_\alpha h^{3/2}\|r'\|_2,
\qquad
C_\alpha=\frac{\cosh(1/2)}{\pi A_B}.
}
\tag{13}
\]

Thus the forced old-core amplitude of an **orthogonal** shell vector is `O(h^(3/2))` in derivative scale.

For later use,

\[
\|\ell_h\|_{H^1(B,b)}^2=\frac h3+\frac1h,
\tag{14}
\]

so the affine shell trace correction in (6) has derivative-scale size `O(h)`, while the core term `alpha H` has `H^1` size `O(h^(3/2))`.

---

## 5. A complete nonorthogonal shell lift

The orthogonal space `Z_b` is not asserted to be an `H^1` complement of the old core. To coordinatize **all** of `W_b^e`, define

\[
\mathcal S_{B,b}=\{s\in H^1(B,b):s(b)=0\}.
\tag{15}
\]

Choose fixed core functions

\[
\phi_T(x)=\frac{H(x)}{H_B},\qquad
\phi_M(x)=1-\frac{x}{B}.
\tag{16}
\]

Then

\[
\phi_T(B)=1,\qquad \phi_M(B)=0,
\]

and their core Mellin masses are

\[
A_T:=\int_0^B\phi_T(x)H(x)\,dx=\frac{A_B}{H_B},
\tag{17}
\]

\[
\boxed{
M_B:=\int_0^B\phi_M(x)H(x)\,dx
=\frac4B\bigl(H_B-1\bigr)>0.
}
\tag{18}
\]

For `s in S_(B,b)` set

\[
t=s(B),\qquad m_s=\int_B^b s(x)H(x)\,dx,
\tag{19}
\]

\[
\boxed{
\gamma(s)=-\frac{m_s+tA_T}{M_B}.
}
\tag{20}
\]

Define `L_(B,b)s` on the positive half interval by

\[
(L_{B,b}s)(x)=
\begin{cases}
t\phi_T(x)+\gamma(s)\phi_M(x),&0<x<B,\\
s(x),&B<x<b,
\end{cases}
\tag{21}
\]

and extend evenly to `(-b,b)`.

### Theorem 5.1 — complete shell-lift lemma

`L_(B,b)` is a bounded linear map

\[
L_{B,b}:\mathcal S_{B,b}\longrightarrow\mathcal W_b^{\rm e}.
\tag{22}
\]

Moreover

\[
\boxed{
\Phi_b:\mathcal W_B^{\rm e}\oplus\mathcal S_{B,b}
\longrightarrow\mathcal W_b^{\rm e},
\qquad
\Phi_b(w,s)=J_{B,b}w+L_{B,b}s
}
\tag{23}
\]

is a linear topological isomorphism for the `H^1` topologies. In particular

\[
\boxed{
\mathcal W_b^{\rm e}
=E_{B,b}\ \dotplus\ L_{B,b}\mathcal S_{B,b}
}
\tag{24}
\]

as a **nonorthogonal** direct sum.

### Proof

For `s in S_(B,b)`, equation (21) has matching trace at `B` because `phi_T(B)=1` and `phi_M(B)=0`; it has zero trace at `b`. Piecewise `H^1` gluing therefore gives an `H_0^1` even function. Its positive-half Mellin moment is

\[
tA_T+\gamma(s)M_B+m_s=0
\]

by (20), so `L_(B,b)s in W_b^e`.

For surjectivity take `u in W_b^e` and let `s=u|_(B,b)`. Then `s in S_(B,b)`. Put

\[
w=(u-L_{B,b}s)|_{(-B,B)}.
\]

The shell of `u-Ls` is zero. Its trace at `B` is zero because both `u` and `Ls` have trace `s(B)`. Hence `w in H_0^1(-B,B)`. Both `u` and `Ls` have zero Mellin moment, so `w` has zero core Mellin moment and is even. Thus `w in W_B^e`, proving surjectivity.

If `Jw+Ls=0`, restriction to the shell gives `s=0`; then `Jw=0`, so `w=0`. Hence the sum is direct and the coordinates are unique.

The inverse is explicit:

\[
s=u|_{(B,b)},\qquad
w=(u-L_{B,b}s)|_{(-B,B)}.
\tag{25}
\]

The trace theorem and the explicit scalar functional (20) imply boundedness of `L`; (25) then gives boundedness of the inverse for fixed `b`. `square`

---

## 6. Uniform small-shell norm bounds for the complete lift

The complete lift necessarily has a larger core correction than the orthogonal subspace because the shell trace is free.

Since `s(b)=0`,

\[
|t|=|s(B)|\le \sqrt h\,\|s'\|_2,
\tag{26}
\]

and

\[
\|s\|_2\le\frac h{\sqrt2}\|s'\|_2.
\tag{27}
\]

Hence, with `H_max=cosh(1/2)`,

\[
|m_s|\le \frac{H_{\max}}{\sqrt2}h^{3/2}\|s'\|_2.
\tag{28}
\]

For `0<h<=1-B`, (20) yields

\[
\boxed{
|\gamma(s)|\le C_\gamma\sqrt h\,\|s'\|_2,
\qquad
C_\gamma=
\frac{A_T+H_{\max}(1-B)/\sqrt2}{M_B}.
}
\tag{29}
\]

The fixed core norms have closed forms

\[
\|\phi_T\|_{H^1(0,B)}^2
=\frac{3B+5\sinh B}{8H_B^2},
\qquad
\|\phi_M\|_{H^1(0,B)}^2
=\frac B3+\frac1B.
\tag{30}
\]

Therefore, with

\[
C_L=\|\phi_T\|_{H^1(0,B)}+C_\gamma\|\phi_M\|_{H^1(0,B)},
\tag{31}
\]

one has the uniform positive-half estimate

\[
\boxed{
\|t\phi_T+\gamma(s)\phi_M\|_{H^1(0,B)}
\le C_L\sqrt h\,\|s'\|_2.
}
\tag{32}
\]

Thus the complete lift's core correction is `O(h^(1/2))` in derivative scale, whereas the orthogonal `Z_b` core amplitude is `O(h^(3/2))`.

Equations (26)-(32) give uniform boundedness of `Phi_b` and its inverse on every right interval `B<b<=1` when the shell is equipped with its `H^1` norm. They also quantify the conditioning that must be paid when a future Schur estimate is converted back to the physical source norm.

---

## 7. Correct full-space block form

The complete source-space coordinates are now `(w,s) in W_B^e direct-sum S_(B,b)`, not `(w,z)` with `z in Z_b`.

Pull the actual form back by `Phi_b`:

\[
\mathfrak F_b((w,s),(w',s'))
=Q_b(\Phi_b(w,s),\Phi_b(w',s')).
\tag{33}
\]

Its blocks are

\[
A_B(w,w')=Q_B(w,w')
\tag{34}
\]

exactly, by window functoriality,

\[
C_b(w,s)=Q_b(J_{B,b}w,L_{B,b}s),
\tag{35}
\]

and

\[
D_b(s,s')=Q_b(L_{B,b}s,L_{B,b}s').
\tag{36}
\]

Thus

\[
\mathfrak F_b=
\begin{pmatrix}
A_B&C_b^*\\
C_b&D_b
\end{pmatrix}
\tag{37}
\]

on a coordinate system that is **surjective onto the whole even source space**.

If a future analysis realizes `D_b` as a strictly positive invertible form/operator on an appropriate shell Hilbert realization, the corresponding Schur expression

\[
A_B-C_b^*D_b^{-1}C_b
\tag{38}
\]

is then the correct all-source object. Because the coordinates are not `L^2` orthogonal, a quantitative `L^2` coercivity constant must additionally pay the norm conditioning of `Phi_b`; positivity alone is invariant under the bijective coordinate change.

The cleaner orthogonal space `Z_b` remains useful for **directed tests**, especially coupling to the inherited near-null source, but a Schur estimate on `E_{B,b}+Z_b` alone does not prove positivity on all of `W_b^e`.

---

## 8. Scope firewall and next gate

This package proves only source-space geometry:

1. the exact orthogonal characterization `Z_b ~= H_0^1(B,b)`;
2. the complete nonorthogonal topological direct sum `W_b^e = E_(B,b) dotplus L_(B,b) S_(B,b)`;
3. uniform small-shell norm bounds for the lift.

It does **not** prove `D_b>0`, does not bound the actual shell coupling, and does not establish positivity at any new endpoint.

The next mathematical gate is now well posed:

- lower-bound the full lifted-shell block `D_b`;
- compute the actual coupling `C_b` to the inherited near-null sector;
- prove positivity of the Schur form (38) on the entire old core;
- include the coordinate norm conditioning when extracting an `L^2` gap.

A failed comparison bound is not a negative Weil vector. C15 is not forced by these coordinate lemmas.
