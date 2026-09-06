# P11 / R43 — primitive martingale-level peeling for structured COND

**Date:** 2026-09-06  
**Status:** exact/local scalar-conditioning reduction; Strong Terminal remains OPEN  
**Parent:** `P11_R43_HARD11_LEVEL0_SATURATION_REDUCTION_2026-09-06.md` on the same branch

## 0. Purpose

The preceding hard11 note shows that the primitive `(1,1)` divergence is the leading part of the positive martingale level `a=0` channel.  A direct bound by the horizon-`V` old diagonal energy `X_0` is correct but potentially too strong, because increasing the terminal horizon resolves new level-0 residual coordinates even inside the old spatial window.

This note keeps the **exact negative residual increment** in the conditioning identity instead of discarding it.  The result is a channel-peeling inequality:

> an entire positive martingale level can be removed from the leakage denominator at the cost of only its already-existing horizon-`U` diagonal energy.

Applying the lemma to `a=0` removes hard11 from the remaining leakage problem. Applying it once more to `a=1` removes the primitive hard22 level.  The residual subsystem `a\ge2` has a uniform `\beta=1/8` exponential displacement moment.

This does not prove decay of the charged low-level old energy and does not close structured COND.

---

## 1. Exact martingale-level support sets and horizon nesting

P11 defines

\[
J_{p,R}(u)
=
\max\left\{0,
\left\lfloor\frac{2(R-|u|)_+}{\log p}\right\rfloor
\right\}
\]

and retains the martingale coordinate `\psi_{p,a}` exactly when

\[
a<J_{p,R}(u).
\]

With

\[
a_p:=\frac12\log p,
\]

this is, up to boundary null sets,

\[
\boxed{
\Omega_{p,a,R}
=
\{u:\ |u|+(a+1)a_p\le R\}.
}
\tag{PL1}
\]

Hence for `U<V`,

\[
\boxed{
\Omega_{p,a,U}\subseteq\Omega_{p,a,V}.
}
\tag{PL2}
\]

For each `a\ge0` define the positive channel

\[
B_{a,R}:=
\sum_pT_{p,a;R}^*T_{p,a;R},
\tag{PL3}
\]

with the PR #56 factor

\[
T_{p,a;R}
=
\sqrt{(\log p)(p-1)p^a}\,
1_{\Omega_{p,a,R}}
\sum_{k\ge a+1}p^{-3k/4}K_{p,k;R}.
\tag{PL4}
\]

Then

\[
A_R=R_R^*R_R=\sum_{a\ge0}B_{a,R}.
\tag{PL5}
\]

Fix `U<V` and embed the old source by `\iota`. Since

\[
E_V\iota=E_U,
\]

the ambient translated function occurring in (PL4) is the same for horizon `U` and for horizon `V`; only the allowed output set grows according to (PL2). Therefore

\[
\boxed{
D_{a;U,V}
:=
\iota^*B_{a,V}\iota-B_{a,U}
\succeq0.
}
\tag{PL6}
\]

Summing over `a` and using the frozen nesting identity

\[
\iota^*A_V\iota-A_U=C^*C,
\]

gives

\[
\boxed{
C^*C=\sum_{a\ge0}D_{a;U,V}.
}
\tag{PL7}
\]

This is precisely why the horizon-`V` old diagonal energy must not be silently replaced by its horizon-`U` counterpart: their difference is a genuine positive part of `C^*C`.

### Local draft booking

```text
R43-COND-MARTINGALE-LEVEL-HORIZON-NESTING ✓[M]
```

---

## 2. Abstract two-channel leakage peeling lemma

Let a positive normal operator on the old/new source decomposition be split into two positive pieces

\[
A=A_0+A_1,
\qquad
A_j\succeq0,
\]

with blocks

\[
A_j=
\begin{pmatrix}
X_j&Y_j^*\\
Y_j&Z_j
\end{pmatrix}.
\tag{PL8}
\]

Put

\[
Y=Y_0+Y_1,
\qquad
Z=Z_0+Z_1.
\]

Then for every old vector `x`,

\[
\boxed{
\langle Yx,(I+Z)^{-1}Yx\rangle
\le
\langle x,X_0x\rangle
+
\langle Y_1x,(I+Z_1)^{-1}Y_1x\rangle.
}
\tag{PL9}
\]

### Proof

Fix `0<\varepsilon<1` and set

\[
D_0:=\varepsilon I+Z_0,
\qquad
D_1:=(1-\varepsilon)I+Z_1.
\]

Then

\[
D_0+D_1=I+Z.
\]

The operator Cauchy/infimal-convolution inequality gives

\[
\langle u+v,(D_0+D_1)^{-1}(u+v)\rangle
\le
\langle u,D_0^{-1}u\rangle
+
\langle v,D_1^{-1}v\rangle.
\tag{PL10}
\]

Apply this with

\[
u=Y_0x,\qquad v=Y_1x.
\]

Because

\[
\begin{pmatrix}
X_0&Y_0^*\\
Y_0&Z_0
\end{pmatrix}\succeq0,
\]

adding `\varepsilon I` to the lower-right block and taking the Schur complement yields

\[
Y_0^*(\varepsilon I+Z_0)^{-1}Y_0\preceq X_0.
\tag{PL11}
\]

Thus

\[
\langle Yx,(I+Z)^{-1}Yx\rangle
\le
\langle x,X_0x\rangle
+
\langle Y_1x,((1-\varepsilon)I+Z_1)^{-1}Y_1x\rangle.
\]

Letting `\varepsilon\downarrow0`, the second term decreases strongly to the `(I+Z_1)^{-1}` term, proving (PL9).
\(\square\)

### Local draft booking

```text
R43-COND-POSITIVE-CHANNEL-LEAKAGE-PEELING ✓[M]
```

This lemma is finite-pair operator algebra.  No asymptotic statement is contained in it.

---

## 3. Exact scalar conditioning identity and cancellation of the new diagonal increment

For the actual PR #57 transported old vector

\[
x=x_{U,V}(f)
=\mathcal Q_{U,V}H_U^*E_{X,U}f,
\]

the exact conditioning increment is

\[
\boxed{
\Delta s_{\rm cond}^{U,V}(f)
=
\langle Yx,(I+Z)^{-1}Yx\rangle
-
\langle x,C^*Cx\rangle,
}
\tag{PL12}
\]

where

\[
Y=P_{\mathcal N}A_V\iota,
\qquad
Z=P_{\mathcal N}A_VP_{\mathcal N}=S^*S.
\]

Peel martingale level `a=0`:

\[
A_0=B_{0,V},
\qquad
A_1=A_V-B_{0,V}.
\]

Write

\[
D_0=\iota^*B_{0,V}\iota-B_{0,U},
\qquad
D_{\ge1}=C^*C-D_0.
\]

Combining (PL9), (PL12), and

\[
X_0-D_0=B_{0,U}
\]

gives the exact one-sided reduction

\[
\boxed{
\Delta s_{\rm cond}^{U,V}(f)
\le
\langle x,B_{0,U}x\rangle
+
\Delta_{\ge1}^{U,V}(x),
}
\tag{PL13}
\]

where

\[
\Delta_{\ge1}^{U,V}(x)
:=
\langle Y_{\ge1}x,(I+Z_{\ge1})^{-1}Y_{\ge1}x\rangle
-
\langle x,D_{\ge1}x\rangle.
\tag{PL14}
\]

Thus the **newly resolved horizon-`V` level-0 diagonal energy cancels against its matching part of `C^*C`**. Only the level-0 energy already present at horizon `U` is charged.

Since the complete hard11 family lies at `a=0`, no hard11 term remains in `\Delta_{\ge1}`.

### Local draft booking

```text
R43-COND-HARD11-LEVEL0-SCALAR-PEELING ✓[M]
```

This is stronger than merely bounding hard11 leakage by the horizon-`V` diagonal energy.

---

## 4. Peeling martingale level a=1 removes the primitive hard22 level

Apply the same lemma inside the `a\ge1` subsystem, now splitting

\[
B_{1,V}
\quad\text{from}\quad
\sum_{a\ge2}B_{a,V}.
\]

The level-1 factor has `k,\ell\ge2`.  Its primitive diagonal pair is

\[
(k,\ell)=(2,2),
\]

with coefficient

\[
(\log p)(p-1)p\,p^{-3}
=(\log p)(p-1)p^{-2}
\asymp(\log p)p^{-1},
\tag{PL15}
\]

which is exactly the nonsummable hard22 scale isolated by PR #58.

All other level-1 pairs have `k+\ell\ge5` and are already exponentially summable by the same argument used below for the high-level remainder.

A second application of (PL9) therefore gives

\[
\boxed{
\Delta s_{\rm cond}^{U,V}(f)
\le
\langle x,(B_{0,U}+B_{1,U})x\rangle
+
\Delta_{\ge2}^{U,V}(x).
}
\tag{PL16}
\]

No hard11 or hard22 primitive channel remains in `\Delta_{\ge2}`.

### Local draft booking

```text
R43-COND-HARD22-LEVEL1-SCALAR-PEELING ✓[M]
```

Again, this is a scalar structured-COND reduction, not an operatorwide `B-METINC-COND` theorem.

---

## 5. The a>=2 subsystem has a beta=1/8 exponential displacement moment

At fixed martingale level `a`, the coefficient of a `(p,k,\ell)` sign term is bounded by

\[
(\log p)(p-1)p^a p^{-3(k+\ell)/4},
\qquad
k,\ell\ge a+1.
\tag{PL17}
\]

Its displacement obeys

\[
\delta\le\frac{k+\ell}{2}\log p.
\tag{PL18}
\]

For `\beta_*=1/8`, using `p-1\le p`,

\[
e^{\delta/8}\|T\|
\le
(\log p)
 p^{1+a-3(k+\ell)/4+(k+\ell)/16}.
\tag{PL19}
\]

For fixed `a`, the largest term occurs at

\[
k=\ell=a+1.
\]

The corresponding prime exponent is

\[
1+a-\frac{3}{2}(a+1)+\frac18(a+1)
=-\frac{3(a+1)}8.
\tag{PL20}
\]

For `a\ge2`, this is at most

\[
-\frac98<-1.
\]

The sums over the excess indices `k-(a+1)`, `\ell-(a+1)` and over `a\ge2` are geometric uniformly for `p\ge2`. Hence

\[
\boxed{
\sum_{T\in\mathscr G_{\ge2}}
e^{\delta(T)/8}\|T\|<\infty
}
\tag{PL21}
\]

uniformly in the horizon.

Therefore the old-to-new block `Y_{\ge2}` satisfies

\[
\boxed{
\|Y_{\ge2}x\|
\le
C\left(
\|\chi_{U,r}x\|+e^{-r/8}\|x\|
\right).
}
\tag{PL22}
\]

Since `((I+Z_{\ge2})^{-1/2})` is a contraction and the diagonal increment term in `\Delta_{\ge2}` is nonnegative and subtracted, (PL16) yields

\[
\boxed{
\bigl(\Delta s_{\rm cond}^{U,V}(f)\bigr)_+
\le
\langle x,(B_{0,U}+B_{1,U})x\rangle
+
C^2
\left(
\|\chi_{U,r}x\|+e^{-r/8}\|x\|
\right)^2.
}
\tag{PL23}
\]

Under the PR #58 terminal-graph normalization `\|x\|\le1`,

\[
\boxed{
\bigl(\Delta s_{\rm cond}^{U,V}(f)\bigr)_+
\le
\mathcal E_{<2;U,V}(f)
+
C^2
\left(
\|\chi_{U,r}x\|+e^{-r/8}
\right)^2,
}
\tag{PL24}
\]

where

\[
\boxed{
\mathcal E_{<2;U,V}(f)
:=
\langle x_{U,V}(f),(B_{0,U}+B_{1,U})x_{U,V}(f)\rangle.
}
\tag{PL25}
\]

### Local draft booking

```text
R43-COND-TWO-PRIMITIVE-LEVEL-PEELING-REDUCTION ✓[M]
```

This is the principal result of the note.

---

## 6. What this changes in the active COND strategy

PR #58 left two explicit hard saturated channels:

```text
(k,l)=(1,1)
(k,l)=(2,2)
```

For the **structured scalar conditioning increment**, PL24 provides a different sufficient route.  One no longer needs to prove the two primitive channel decays separately if one can prove instead:

```text
ROADMAP-COND-LOW-MARTINGALE-OLD-ENERGY-DECAY
ROADMAP-COND-TRANSPORTED-COLLAR-MASS-DECAY
```

with the quantifiers required by the later B-FLAGDYN/FD23 composition.

The low-level energy target is

\[
\boxed{
\mathcal E_{<2;U,V}(f)\to0.
}
\tag{PL26}
\]

This is only a **sufficient alternative route**.  PL24 does not prove PL26 and does not show that the earlier direct hard-channel route is unnecessary in every possible argument.

### Important firewall

The auxiliary contraction from the preceding hard11 note gives

\[
\|R_U\mathcal Q_{U,V}y\|\le\|y\|,
\]

but the relevant pre-transport vector is `H_U^*E_{X,U}f`; no currently booked theorem gives the R40/R42 `O(U^{-1})` dual-normal scale for this vector.  Therefore no decay of `\mathcal E_{<2;U,V}` is inferred here.

---

## 7. Quantifier and status firewall

PL23/PL24 are fixed-pair algebraic/quantitative reductions.  This note does not silently choose:

- relation between `U` and `V`;
- uniformity in intermediate `V`;
- pointwise versus uniform source control;
- cofinal partition;
- `r=r(U,V)`;
- order of limits.

Still OPEN:

```text
ROADMAP-COND-LOW-MARTINGALE-OLD-ENERGY-DECAY
R43-COND-TRANSPORTED-COLLAR-MASS-DECAY
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY
ROADMAP-BRIDGE-COND-DIRECT-FLAGDYN
B-FLAGDYN / B-FLAGTIGHT
Strong Terminal / C6
Object-X realization
RH
```

No Registry promotion is made by this Draft.