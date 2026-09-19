# A-gauge high-tail contraction and finite low reduction on the full shell interval

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Anchor: `8f5b711145b28b6dbfc8280d8e51625f3d2f1532` on
`research/x-c1-inherited-resonance-shell-schur-2026-09-18`.
This note is append-only. It does not change `main`, open a PR, or merge anything.

Put
\[
 B={\log5\over2},\qquad 0<h=b-B\le10^{-20},\qquad L=\log(2/h).
\]
All physical core products are in `L2((-B,B),dx)`, linear in the first argument.
The A-gauge spaces, form `a_A`, full shell form `d`, coupling `C_A`, and fixed
near-null coordinate `f_A` are those of the anchor.

This package proves two pieces of the WIDTH-AMPLIFICATION program:

1. it binds the previously quoted `0.7194486...` tail floor to its exact
   endpoint space and converts it to a physical A-core tail floor;
2. it proves a complete infinite-dimensional high-tail shell contraction
   on the whole interval `0<h<=10^-20`.

It does **not** close the remaining finite low block or the full even gate at
`h=10^-20`.

## 1. Exact provenance of the endpoint tail floor

Use the reference Hilbert space
\[
 \mathscr H=L^2((-1,1),d\xi/2),
 \qquad (U_Bu)(\xi)=\sqrt{2B}\,u(B\xi).
\]
`U_B` is an L2 isometry. In the even sector put
\[
 X=P_0^\perp,
 \qquad L_0=\operatorname{span}\{P_2,P_4,\ldots,P_{62}\},
 \qquad Y=\overline{\operatorname{span}\{P_{64},P_{66},\ldots\}}.
\]
Thus `X=L_0 direct-sum Y` and `dim L_0=31`.

Let `m(ξ)=cosh(Bξ/2)` and let the endpoint Mellin reconstruction be
\[
 \mathcal Mx=x- {\langle x,m\rangle\over\langle P_0,m\rangle}P_0.
\tag{1}
\]
The endpoint package `prime-power-segment-4-2026-09-18` proves that the
actual constrained tail block of `M* q_B M` on **all of Y** satisfies
\[
 q_B[U_B^{-1}\mathcal My]\ge\delta_H\|y\|_{\mathscr H}^2,
 \qquad y\in Y\cap\operatorname{Dom}(q_B\circ\mathcal M),
\tag{2}
\]
with the directed stored lower endpoint
\[
 \delta_H>0.719448628450052179181039.
\tag{3}
\]
This is the quantity stored as `even_tail_floor`; it is not a sampled or
finite-tail eigenvalue. The same package proves globally
\[
 \|\mathcal Mx\|^2\le(1+\beta_0)\|x\|^2,
 \qquad \beta_0<0.006732787914843592696179.
\tag{4}
\]
Consequently, on the physical tail image
\[
 \mathscr T:=U_B^{-1}\mathcal M Y,
\]
we have, on its form domain,
\[
 \boxed{a[f]=q_B[f]> {7\over10}\|f\|_2^2.}
\tag{5}
\]
Indeed the checker verifies directly from the pinned rational endpoints that
`delta_H/(1+beta_0)>7/10`.

The space `T` is closed in physical L2: on Y the correction in (1) is in the
orthogonal P0 direction, hence `||M y||>=||y||`. The form-domain version is
closed in the energy norm because the finitely many omitted low Legendre
coordinate functionals are L2-bounded and `a>=10^-13 I` on the ambient core.

For `b>B`, physical zero extension preserves the core energy exactly by the
established window identity, so (5) is the same core estimate used in the
shell problem.

## 2. The A-high tail and a genuinely finite remainder

Let
\[
 F_A=F_{B,A}^0=\{f\in F_B:a(f,\psi)=0\}
\]
be the complete A-gauge core form domain, and let
\[
 \mathscr T_A:=F_A\cap\mathscr T.
\tag{6}
\]
The inverse Mellin coordinate followed by projection to `L_0` gives a bounded
map from `F_A` into the 31-dimensional space `L_0`. Its kernel is exactly
`T_A`. Therefore
\[
 \boxed{\operatorname{codim}_{F_A}\mathscr T_A\le31.}
\tag{7}
\]

Normalize the fixed near-null A-coordinate only in the core energy:
\[
 v_A={f_A\over\sqrt{a_A[f_A]}},\qquad a_A[v_A]=1.
\]
Define
\[
 H_A:=\mathscr T_A\cap v_A^{\perp_{a_A}},
 \qquad
 L_A:=\bigl(\operatorname{span}\{v_A\}\oplus_{a_A}H_A\bigr)^{\perp_{a_A}}.
\tag{8}
\]
Then all spaces are closed in the core energy Hilbert space and
\[
 \boxed{
 F_A=\operatorname{span}\{v_A\}\oplus_{a_A}L_A\oplus_{a_A}H_A,
 \qquad \dim L_A\le31.
 }
\tag{9}
\]
Thus the remaining WIDTH problem can be organized with an explicitly finite
low block. The high block `H_A` still contains the entire infinite tail.

## 3. Sharpened complete core-shell coupling on the tail

For `f in T_A` and `z=(t,s) in F_D`, put
\[
 p=\|s\|_{L^2(B,b)},\qquad
 Y_s=-m_s\chi+S_s,
 \qquad m_s=\int_B^b s(x)\cosh(x/2)\,dx.
\]
The exact A-gauge block identity from the anchor gives
\[
 c_A(f,z)=q_b(Jf,Y_s),
\tag{10}
\]
so the trace coordinate `t` does not enter the forcing.

### 3.1 Gamma plus arithmetic shell term

The all-core proof gives for arbitrary even L2 core `f`
\[
 |q_\Gamma(Jf,S_s)|
 \le \sqrt2\left({\pi\over2}+{5\over4}\sqrt{Bh}\right)\|f\|p.
\tag{11}
\]
At `h<=10^-20`, the inherited directed constants imply
\[
 \sqrt2<1.415,\quad \pi<{22\over7},\quad B<1,
\]
and hence the coefficient in (11) is `<2.224`.

For the four active prime-power channels `q=2,3,4,5`, the exact nonpole
weights are
\[
 w_q={\Lambda(q)\over\sqrt q},
\tag{12}
\]
with `w_4=log(2)/2`. The checker proves, by the pinned directed logarithm
and radical arithmetic,
\[
 w_2<0.491,\quad w_3<0.635,\quad w_4<0.347,\quad w_5<0.721.
\tag{13}
\]
Each reflected core-shell translation contributes at most `2 w_q ||f|| p`.
Therefore the arithmetic coefficient is `<4.388`, and (11)-(13) give
\[
 \boxed{|q_b(Jf,S_s)|<{331\over50}\|f\|p.}
\tag{14}
\]
The bound `331/50=6.62` is deliberately rounded upward. It includes all
four channels and the full Carleman singularity; no shrinking-translation
operator norm is used.

### 3.2 Moment correction

Write `E=a[f]`. By (5), `E>(7/10)||f||^2`. Since the non-Gamma remainder
has L2 operator norm at most 14,
\[
 \mathcal E[f]\le E+14\|f\|^2<21E.
\]
The inherited bounds `E[chi]<=106` and `||chi||^2<=18` then imply
\[
 |q_B(f,\chi)|
 \le\sqrt{106\cdot21}\sqrt E
       +14\sqrt{18\cdot{10\over7}}\sqrt E
 <132\sqrt E.
\tag{15}
\]
Also
\[
 |m_s|\le{6\over5}\sqrt h\,p\le {6\over5\cdot10^{10}}p.
\]
Consequently
\[
 |m_s q_B(f,\chi)|<{1\over100}\sqrt E\,p.
\tag{16}
\]
This is vastly nonsharp but already negligible at the required scale.

From (5) and (14),
\[
 |q_b(Jf,S_s)|
 <{331\over50}\sqrt{10\over7}\sqrt E\,p
 <{792\over100}\sqrt E\,p.
\]
Combining with (16) gives the convenient complete bound
\[
 \boxed{|c_A(f,z)|<{793\over100}\sqrt{a_A[f]}\,p,}
\tag{17}
\]
and `(793/100)^2<63`.

## 4. Full high-tail Riesz contraction on 0<h<=10^-20

The logarithmic shell estimate already proved in `04bc246...` is, on the
complete shell form domain,
\[
 d[(t,s)]\ge\delta|t|^2+(2L-19)p^2.
\tag{18}
\]
For `0<h<=10^-20`, `L=log(2/h)>46`, so
\[
 d[(t,s)]>73p^2.
\tag{19}
\]
If `p=0`, the numerator in (17) is zero. Otherwise (17)-(19) give
\[
 { |c_A(f,z)|^2\over a_A[f]d[z]}<{63\over73}.
\]
Taking the full shell supremum therefore proves
\[
 \boxed{
 \|D^{-1/2}C_Af\|_X^2\le {63\over73}a_A[f]
 \qquad(f\in\mathscr T_A).
 }
\tag{20}
\]
No finite shell basis or coretail cutoff enters this estimate.

In particular, for the high space in (8), if
`B_h=D^{-1/2}C_A A_A^{-1/2}` denotes the normalized A-core-to-shell map,
then
\[
 \boxed{G_{HH}=B_H^*B_H\preceq {63\over73}I.}
\tag{21}
\]
This closes the infinite High-Tail block on the **full** previous structural
interval `0<h<=10^-20`.

The inherited near-null block satisfies
\[
 G_{vv}<\nu I,\qquad \nu={151\over20000000}.
\tag{22}
\]
Because the full Gram operator is positive, the Near/High mixed block is
already controlled without a separate truncation:
\[
 \boxed{\|G_{vH}\|^2\le {151\over20000000}{63\over73}.}
\tag{23}
\]
This does not close the remaining Low interactions.

## 5. What remains for WIDTH AMPLIFICATION

Equations (9), (21), and (23) reduce the still-open full-width problem to a
finite-dimensional low block and its interactions. On
\[
 F_A=\operatorname{span}\{v_A\}\oplus_{a_A}L_A\oplus_{a_A}H_A,
 \qquad \dim L_A\le31,
\]
the remaining unproved data are

- the rigorous finite block `G_LL`;
- the Near/Low block `G_vL`;
- the Low/High block `G_LH`;
- a directed norm enclosure of the resulting complete 3-by-3 block operator
  strictly below one.

The separate facts `G_vv<1` and `G_HH<1` do not by themselves imply that
full norm bound. In particular `G_LH` cannot be discarded.

This package does not extend the existing Even-All-Source theorem beyond
`h<=2^(-10^16)`, does not certify the full interval `h<=10^-20`, and does
not touch the odd sector, `log(7)/2`, `a=1`, C1-GEOM, Objekt X, or RH.
