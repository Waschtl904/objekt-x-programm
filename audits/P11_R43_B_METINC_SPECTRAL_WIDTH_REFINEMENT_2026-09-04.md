# P11 R43 — B-METINC spectral-width refinement

Date: 2026-09-04

## Status and firewall

This companion note strengthens the terminal-metric-increment route inside B-FLAGMOD.
It uses only the already established fixed-source compression algebra and does **not**
prove B-METINC, B-FLAGMOD, B-FLAGTIGHT, Strong Terminal/C6, Object X, or RH.

No freeze, no new formal independent-GREEN booking, and no new `✓[M]` are created.
R43 remains OPEN.

The main refinement is that Loewner positivity is not needed even for the factor-`1/2`
leakage estimate: the correct invariant is the **spectral width** of the self-adjoint
normalized metric increment.

---

## 1. Setup

Fix `0<R<S` and one terminal step `U<V`. Put

\[
\mathbf H_X^{U,V}
:=G_{X,U}^{-1/2}(G_{X,V}-G_{X,U})G_{X,U}^{-1/2}
=A_X^{U,V}-I,
\qquad X\in\{R,S\}.
\tag{SW1}
\]

Frozen O1 compression gives

\[
W_U^*\mathbf H_S^{U,V}W_U=\mathbf H_R^{U,V}.
\tag{SW2}
\]

Let

\[
P_U:=W_UW_U^*
\]

and define the A-level off-range defect

\[
\mathscr E_{U,V}
:=(I-P_U)\mathbf H_S^{U,V}W_U.
\tag{SW3}
\]

Because `W_U` is an isometry onto `Ran P_U`,

\[
\boxed{
\|\mathscr E_{U,V}\|
=\|(I-P_U)\mathbf H_S^{U,V}P_U\|.
}
\tag{SW4}
\]

Since `\mathbf H_S^{U,V}` is self-adjoint, its commutator with `P_U` has block form

\[
[\mathbf H_S,P_U]
=\begin{pmatrix}
0&-B^*\\
B&0
\end{pmatrix},
\qquad
B=(I-P_U)\mathbf H_SP_U,
\]

relative to `Ran P_U \oplus Ran(I-P_U)`. Hence

\[
\boxed{
\|\mathscr E_{U,V}\|
=\|[\mathbf H_S^{U,V},P_U]\|.
}
\tag{SW5}
\]

This is the exact off-diagonal/commutator identity behind B-METINC.

---

## 2. Positivity-free spectral-width bound

Let

\[
\lambda_-^{U,V}:=\inf\sigma(\mathbf H_S^{U,V}),
\qquad
\lambda_+^{U,V}:=\sup\sigma(\mathbf H_S^{U,V}),
\]

and define

\[
\operatorname{width}(\mathbf H_S^{U,V})
:=\lambda_+^{U,V}-\lambda_-^{U,V}.
\tag{SW6}
\]

Choose the spectral midpoint

\[
\mu_{U,V}:=\frac{\lambda_+^{U,V}+\lambda_-^{U,V}}2.
\]

Scalar multiples of the identity have no off-diagonal block, so

\[
(I-P_U)\mathbf H_SP_U
=(I-P_U)(\mathbf H_S-\mu I)P_U.
\]

Therefore

\[
\begin{aligned}
\|\mathscr E_{U,V}\|
&\le \|\mathbf H_S^{U,V}-\mu_{U,V}I\|\\
&=\frac12\operatorname{width}(\mathbf H_S^{U,V}).
\end{aligned}
\]

Thus, with no sign assumption at all,

\[
\boxed{
\|\mathscr E_{U,V}\|
\le
\frac12\operatorname{width}(\mathbf H_S^{U,V}).
}
\tag{SW7}
\]

This strictly strengthens the unconditional norm estimate

\[
\|\mathscr E_{U,V}\|\le\|\mathbf H_S^{U,V}\|,
\tag{SW8}
\]

because for every bounded self-adjoint operator

\[
\operatorname{width}(H)\le2\|H\|.
\]

### Two-sided increment form

If one can prove only the pairwise order bounds

\[
-\delta_{U,V}I
\le
\mathbf H_S^{U,V}
\le
\varepsilon_{U,V}I,
\qquad
\delta_{U,V},\varepsilon_{U,V}\ge0,
\tag{SW9}
\]

then

\[
\boxed{
\|\mathscr E_{U,V}\|
\le
\frac12(\varepsilon_{U,V}+\delta_{U,V}).
}
\tag{SW10}
\]

This is strictly weaker than Loewner positivity.

### Loewner as a special case

If `\mathbf H_S^{U,V}\ge0`, then

\[
\operatorname{width}(\mathbf H_S^{U,V})
\le\|\mathbf H_S^{U,V}\|,
\]

so SW7 gives

\[
\boxed{
\|\mathscr E_{U,V}\|
\le\frac12\|\mathbf H_S^{U,V}\|.
}
\tag{SW11}
\]

Thus the previous conditional half-norm estimate is a special case of spectral-width
control. In particular `R43-MI-LOEWNER` is not required for this factor-`1/2` mechanism.
It remains an optional arithmetic/order theorem, not a logical gate for B-METINC.

---

## 3. Exact new / old-geometry / old-conditioning telescoping split

The frozen Schur-energy audit already shows that primitive prime-power coefficients are
horizon independent while both the finite-window geometry and the Feshbach conditioning
move with the terminal horizon.

For fixed source `X` and vector `f`, write

\[
v_U:=H_U^*E_{X,U}f,
\qquad
\iota:=E_{U,V}:L^2(-U,U)\to L^2(-V,V).
\]

Split the terminal-`V` hub into old and newly activated indices:

\[
H_V=H_{V,\mathrm{old}}+H_{V,\mathrm{new}},
\]

where

\[
H_{V,\mathrm{old}}
:=\sum_{(p,k)\in\Lambda_U}a_{p,k}K_{p,k;V},
\qquad
H_{V,\mathrm{new}}
:=\sum_{(p,k)\in\Lambda_V\setminus\Lambda_U}a_{p,k}K_{p,k;V}.
\tag{SW12}
\]

Set

\[
v_0:=\iota v_U,
\qquad
v_1:=H_{V,\mathrm{old}}^*E_{X,V}f,
\qquad
v_2:=H_V^*E_{X,V}f
=v_1+H_{V,\mathrm{new}}^*E_{X,V}f.
\tag{SW13}
\]

Then the exact Schur-energy difference telescopes as

\[
\boxed{
\begin{aligned}
s_V(f)-s_U(f)
={}&
\underbrace{\bigl(\langle v_0,B_Vv_0\rangle-\langle v_U,B_Uv_U\rangle\bigr)}_{\rm old\text{-}conditioning}
\\
&+
\underbrace{\bigl(\langle v_1,B_Vv_1\rangle-\langle v_0,B_Vv_0\rangle\bigr)}_{\rm old\text{-}geometry}
\\
&+
\underbrace{\bigl(\langle v_2,B_Vv_2\rangle-\langle v_1,B_Vv_1\rangle\bigr)}_{\rm new\text{-}shell}.
\end{aligned}
}
\tag{SW14}
\]

This is an exact decomposition, but **none of the three summands has a sign from the
frozen definitions alone**. In particular the new-shell term still contains cross terms
with the already present terminal-`V` old geometry.

By polarization/Riesz representation, SW14 defines self-adjoint fixed-source operator
increments

\[
\Delta G_X^{U,V}
=\Delta G_{X,\mathrm{cond}}^{U,V}
+\Delta G_{X,\mathrm{geo}}^{U,V}
+\Delta G_{X,\mathrm{new}}^{U,V}.
\tag{SW15}
\]

After normalization by `G_{X,U}^{-1/2}`, write

\[
\mathbf H_X^{U,V}
=\mathbf H_{X,\mathrm{cond}}^{U,V}
+\mathbf H_{X,\mathrm{geo}}^{U,V}
+\mathbf H_{X,\mathrm{new}}^{U,V}.
\tag{SW16}
\]

For bounded self-adjoint operators, spectral width is subadditive:

\[
\operatorname{width}(A+B)
\le\operatorname{width}(A)+\operatorname{width}(B).
\]

Together with `\operatorname{width}(K)\le2\|K\|`, SW7 yields the useful sufficient bound

\[
\boxed{
\|\mathscr E_{U,V}\|
\le
\frac12\operatorname{width}(\mathbf H_{S,\mathrm{new}}^{U,V})
+\|\mathbf H_{S,\mathrm{geo}}^{U,V}\|
+\|\mathbf H_{S,\mathrm{cond}}^{U,V}\|.
}
\tag{SW17}
\]

This is the clean three-channel B-METINC audit target:

1. `B-METINC-NEW`: control the spectral width of the genuinely new-shell contribution;
2. `B-METINC-GEO`: control the drift caused by `P_TD_sE_T` on already active channels;
3. `B-METINC-COND`: control the Feshbach-conditioning drift from `B_T`.

A future positive-atom theorem could sharpen the NEW channel, but no such positivity is
used or booked here.

---

## 4. Full Sylvester/conditioning factor for the actual modulus gate

The square-root mismatch is

\[
\mathscr M
=(A_S^{U,V})^{1/2}W_U
-W_U(A_R^{U,V})^{1/2}
\]

and satisfies the exact Sylvester equation

\[
(A_S^{U,V})^{1/2}\mathscr M
+\mathscr M(A_R^{U,V})^{1/2}
=\mathscr E_{U,V}.
\tag{SW18}
\]

Define pairwise coercivity numbers

\[
\alpha_X(U,V)
:=\inf\sigma\bigl((A_X^{U,V})^{1/2}\bigr)>0.
\tag{SW19}
\]

Then

\[
\|\mathscr M\|
\le
\frac{\|\mathscr E_{U,V}\|}
{\alpha_S(U,V)+\alpha_R(U,V)}.
\tag{SW20}
\]

The projected normalized modulus defect from FD17 is

\[
\mathfrak d_{m,\mathrm{mod}}(U,V)
=
\left\|
P_m\mathcal U_S\mathscr M
A_R^{-1/2}\mathcal U_R^*\varepsilon_R
\right\|.
\tag{SW21}
\]

Since

\[
\|A_R^{-1/2}\|=\alpha_R(U,V)^{-1},
\]

one obtains the complete pairwise operator-norm chain

\[
\boxed{
\mathfrak d_{m,\mathrm{mod}}(U,V)
\le
\frac{\|\mathscr E_{U,V}\|}
{\alpha_R(U,V)\bigl(\alpha_S(U,V)+\alpha_R(U,V)\bigr)}.
}
\tag{SW22}
\]

Combining with SW7 gives the strengthened positivity-free estimate

\[
\boxed{
\mathfrak d_{m,\mathrm{mod}}(U,V)
\le
\frac{\operatorname{width}(\mathbf H_S^{U,V})}
{2\alpha_R(U,V)\bigl(\alpha_S(U,V)+\alpha_R(U,V)\bigr)}.
}
\tag{SW23}
\]

The older norm-only route is recovered from
`\operatorname{width}(\mathbf H_S)\le2\|\mathbf H_S\|`:

\[
\boxed{
\mathfrak d_{m,\mathrm{mod}}(U,V)
\le
\frac{\|\mathbf H_S^{U,V}\|}
{\alpha_R(U,V)\bigl(\alpha_S(U,V)+\alpha_R(U,V)\bigr)}.
}
\tag{SW24}
\]

Both coercivity factors are pairwise. No cofinal uniform positive lower bound for them is
booked.

---

## 5. Summability firewall: step smallness is not enough

Let

\[
U_0<U_1<U_2<\cdots\to\infty
\]

be a terminal partition and define the width/conditioning majorant

\[
\boxed{
b_k
:=
\sup_{V\in[U_k,U_{k+1}]}
\frac{\operatorname{width}(\mathbf H_S^{U_k,V})}
{2\alpha_R(U_k,V)\bigl(\alpha_S(U_k,V)+\alpha_R(U_k,V)\bigr)}.
}
\tag{SW25}
\]

Then

\[
\Delta_{m,k}^{\mathrm{mod}}\le b_k
\quad\text{for every }m,k.
\tag{SW26}
\]

Thus the quantitative total-variation requirement is naturally

\[
\boxed{
\sum_{k\ge0}b_k<\infty.
}
\tag{SW27}
\]

In particular, mere step smallness

\[
\|\mathbf H_S^{U_k,U_{k+1}}\|\to0
\]

is insufficient: arbitrarily small increments can still have infinite total variation.

However, SW27 **alone does not yet imply** the FD23 limit

\[
\lim_{m\to\infty}\sum_k\Delta_{m,k}^{\mathrm{mod}}=0.
\]

For dominated convergence on the counting measure one also needs, for every fixed `k`,

\[
\boxed{
\Delta_{m,k}^{\mathrm{mod}}\to0
\qquad(m\to\infty).
}
\tag{SW28}
\]

Pointwise strong convergence `P_m\to0` controls each fixed vector but does not by itself
make the supremum over `V\in[U_k,U_{k+1}]` uniform. A sufficient additional mechanism is
relative compactness of the vector family

\[
\left\{
\mathcal U_S\mathscr M A_R^{-1/2}\mathcal U_R^*\varepsilon_R:
V\in[U_k,U_{k+1}]
\right\},
\tag{SW29}
\]

for example from an independently proved norm-continuity statement in `V` on the compact
interval. No such terminal-continuity theorem is silently imported here.

Accordingly, a clean sufficient modulus route is:

\[
\boxed{
\text{SW27 + SW28}
\Longrightarrow
\lim_{m\to\infty}\sum_k\Delta_{m,k}^{\mathrm{mod}}=0,
}
\tag{SW30}
\]

which supplies the B-FLAGMOD half of the existing FD23 criterion.

---

## 6. Revised B-METINC research target

The primary operator-norm route should now be read as a **spectral-width route**:

```text
B-METINC-WIDTH
  = find a terminal partition with
      (i) summable width/conditioning majorants b_k,
     (ii) fixed-interval projected-tail convergence SW28.
```

The three separately auditable quantitative subtargets are

```text
B-METINC-NEW   : new-shell spectral width,
B-METINC-GEO   : old-channel geometric drift,
B-METINC-COND  : Feshbach-conditioning drift.
```

The logical role is only sufficient:

\[
\boxed{
\text{B-METINC-WIDTH}
\Longrightarrow
\text{B-FLAGMOD contribution to FD23}.
}
\tag{SW31}
\]

Failure of cofinal operator-norm/spectral-width control would **not** disprove B-FLAGMOD.
It would force a return to the genuinely projected quantity

\[
\|P_m\mathcal U_S\mathscr M A_R^{-1/2}\mathcal U_R^*\varepsilon_R\|,
\]

which can be much smaller than the global operator norm.

`R43-MI-LOEWNER` is therefore demoted from optional factor-`1/2` accelerator to an
optional structural/order theorem. Spectral width already supplies the factor `1/2`
without positivity.

---

## 7. Governance

- R43: OPEN.
- `R43-MI-LOEWNER`: OPEN, optional structural theorem.
- `B-METINC-WIDTH`: OPEN.
- `B-METINC-NEW`: OPEN.
- `B-METINC-GEO`: OPEN.
- `B-METINC-COND`: OPEN.
- B-METINC: OPEN.
- B-FLAGMOD: OPEN.
- B-FLAGPHASE: OPEN.
- B-FLAGTIGHT: OPEN.
- B-SIGN: OPEN.
- Strong Terminal/C6: OPEN.
- no freeze;
- no new formal independent GREEN;
- no new `✓[M]`;
- R38–R42 unchanged/frozen;
- R37/G4c separate and open;
- no Object-X/RH promotion.
