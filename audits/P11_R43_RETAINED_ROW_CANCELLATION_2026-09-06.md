# P11 / R43 — retained-row cancellation of the primitive hard channels

**Date:** 2026-09-06  
**Status:** exact/local structured scalar-COND reduction; transported collar decay and Strong Terminal remain OPEN  
**Stack:** on top of PR #58 and the two preceding PR #61 audits

## 0. Purpose

The previous two notes first embedded hard11/hard22 into positive martingale-level channels and then showed how positive channels can be peeled from the exact scalar conditioning increment.

The present note observes that the frozen PR #55 residual projection already provides the optimal split.  One need not peel martingale levels one at a time.

Let

\[
M=R_V\iota,
\qquad
S=R_VP_{\mathcal N},
\qquad
\Pi=\Pi_{U,V},
\]

with the frozen exact identities

\[
\boxed{
\Pi M=\jmath R_U,
\qquad
C=(I-\Pi)M,
\qquad
M^*M-R_U^*R_U=C^*C.
}
\tag{RR1}
\]

The key step is to decompose **both** `M` and `S` through the same orthogonal residual projection `\Pi`.  The entire newly resolved residual-row channel then cancels against the exact `-C^*C` term in the resolvent-transported conditioning increment.  The only remaining positive leakage comes from new source variables coupling into residual rows that were already retained at horizon `U`.

Those retained rows have a decisive geometric property: the primitive diagonal sum branch `k=\ell=a+1` at martingale level `a` cannot cross from the old source to the new source while its intermediate residual coordinate remains in the horizon-`U` retained set.  Therefore the primitive hard11 and hard22 channels are absent from the retained-row old-to-new block.

The retained block has a horizon-uniform `\beta=1/8` exponential displacement moment.

---

## 1. Exact retained/new residual-row split

Define

\[
M_{\rm ret}:=\Pi M,
\qquad
M_{\rm new}:=(I-\Pi)M=C,
\tag{RR2}
\]

and

\[
S_{\rm ret}:=\Pi S,
\qquad
S_{\rm new}:=(I-\Pi)S.
\tag{RR3}
\]

Because `\Pi` is an orthogonal projection in the residual target space,

\[
M=M_{\rm ret}+M_{\rm new},
\qquad
S=S_{\rm ret}+S_{\rm new},
\]

with orthogonal target ranges. Consequently

\[
\boxed{
S^*M
=S_{\rm ret}^*M_{\rm ret}
+S_{\rm new}^*M_{\rm new},
}
\tag{RR4}
\]

and

\[
\boxed{
S^*S
=S_{\rm ret}^*S_{\rm ret}
+S_{\rm new}^*S_{\rm new}.
}
\tag{RR5}
\]

Put

\[
Y_{\rm ret}:=S_{\rm ret}^*M_{\rm ret},
\qquad
Z_{\rm ret}:=S_{\rm ret}^*S_{\rm ret},
\tag{RR6}
\]

and

\[
Y_{\rm new}:=S_{\rm new}^*M_{\rm new},
\qquad
Z_{\rm new}:=S_{\rm new}^*S_{\rm new}.
\tag{RR7}
\]

The positive source block associated with the newly resolved residual rows is

\[
\begin{pmatrix}
C^*C&Y_{\rm new}^*\\
Y_{\rm new}&Z_{\rm new}
\end{pmatrix}
=
\begin{pmatrix}M_{\rm new}^*\\S_{\rm new}^*\end{pmatrix}
\begin{pmatrix}M_{\rm new}&S_{\rm new}\end{pmatrix}
\succeq0.
\tag{RR8}
\]

---

## 2. Exact cancellation in the resolvent-transported conditioning scalar

For the PR #57 transported old vector

\[
x=x_{U,V}(f)
=\mathcal Q_{U,V}H_U^*E_{X,U}f,
\tag{RR9}
\]

the exact scalar conditioning increment is

\[
\boxed{
\Delta s_{\rm cond}^{U,V}(f)
=
\langle (Y_{\rm ret}+Y_{\rm new})x,
(I+Z_{\rm ret}+Z_{\rm new})^{-1}
(Y_{\rm ret}+Y_{\rm new})x\rangle
-\|Cx\|^2.
}
\tag{RR10}
\]

Apply the positive-channel peeling inequality proved in the preceding PR #61 audit with the newly resolved row channel as the peeled channel.  Its old diagonal block is exactly `C^*C`. Therefore

\[
\begin{aligned}
&\langle (Y_{\rm ret}+Y_{\rm new})x,
(I+Z_{\rm ret}+Z_{\rm new})^{-1}
(Y_{\rm ret}+Y_{\rm new})x\rangle\\
&\qquad\le
\|Cx\|^2
+
\langle Y_{\rm ret}x,(I+Z_{\rm ret})^{-1}Y_{\rm ret}x\rangle.
\end{aligned}
\tag{RR11}
\]

Subtracting the exact `\|Cx\|^2` term in (RR10) yields

\[
\boxed{
\Delta s_{\rm cond}^{U,V}(f)
\le
\langle Y_{\rm ret}x,(I+Z_{\rm ret})^{-1}Y_{\rm ret}x\rangle.
}
\tag{RR12}
\]

In particular,

\[
\boxed{
\bigl(\Delta s_{\rm cond}^{U,V}(f)\bigr)_+
\le
\|(I+Z_{\rm ret})^{-1/2}Y_{\rm ret}x\|^2
\le
\|Y_{\rm ret}x\|^2.
}
\tag{RR13}
\]

This is the central cancellation: **all newly resolved residual rows are paid for exactly by the already present negative `C^*C` term**.  No old low-level diagonal energy remains in the bound.

### Local draft booking

```text
R43-COND-NEW-RESIDUAL-ROW-EXACT-CANCELLATION ✓[M]
```

This booking is scalar structured-COND only; it is not an operatorwide Loewner statement.

---

## 3. Exact description of retained martingale rows

P11 defines

\[
J_{p,U}(u)
=
\max\left\{0,
\left\lfloor\frac{2(U-|u|)_+}{\log p}\right\rfloor
\right\}.
\]

At martingale level `a`, the coordinate `\psi_{p,a}` is retained exactly when `a<J_{p,U}(u)`.  Writing

\[
a_p:=\frac12\log p,
\]

the retained output set is, up to boundary null sets,

\[
\boxed{
\Omega_{p,a,U}
=\{u:\ |u|+(a+1)a_p\le U\}.
}
\tag{RR14}
\]

Thus the retained-row operator uses the level decomposition

\[
\sqrt{(\log p)(p-1)p^a}\,
1_{\Omega_{p,a,U}}
\sum_{k\ge a+1}p^{-3k/4}K_{p,k;V}
\tag{RR15}
\]

on the horizon-`V` source domain.  On embedded old sources this agrees exactly with the horizon-`U` residual row, which is the frozen identity `M_{\rm ret}=\jmath R_U` in coordinates.

---

## 4. Primitive diagonal sum branches cannot couple old to new through retained rows

Fix a prime `p`, martingale level `a`, and put

\[
m:=a+1.
\]

The primitive diagonal pair is

\[
k=\ell=m.
\]

Its two zero-displacement sign terms cannot map an old source vector into the new spatial source block.

For either nonzero sum-sign term, an old source point `z` and a new source point `x` differ by

\[
|x-z|=2ma_p.
\tag{RR16}
\]

The multiplier in the normal term is evaluated at their midpoint

\[
u=\frac{x+z}{2}
\tag{RR17}
\]

(up to the symmetric negative-boundary orientation).

Assume first that the branch crosses the positive source boundary, so

\[
z<U,
\qquad
x>U,
\qquad
x=z+2ma_p.
\]

Then

\[
u=z+ma_p=x-ma_p>U-ma_p.
\tag{RR18}
\]

If `\Omega_{p,a,U}` is nonempty then `ma_p\le U`, so the right-hand side is nonnegative. Hence

\[
|u|=u>U-ma_p,
\]

which contradicts the retained-row condition

\[
|u|+ma_p\le U.
\]

The negative boundary is identical by symmetry. Therefore

\[
\boxed{
P_{\mathcal N}
\bigl(\text{retained-row primitive }k=\ell=a+1\text{ sum branch}\bigr)
\iota
=0.
}
\tag{RR19}
\]

This single geometric statement removes:

- hard11: `a=0`, `k=\ell=1`;
- the nonsummable primitive part of hard22: `a=1`, `k=\ell=2`;
- every analogous primitive diagonal branch at higher martingale levels.

### Local draft booking

```text
R43-COND-RETAINED-ROW-PRIMITIVE-DIAGONAL-EXCLUSION ✓[M]
```

---

## 5. Exponential displacement moment for the entire retained-row old-to-new block

Expand `Y_{\rm ret}` into translation-sign terms.  At martingale level `a`, a `(p,k,\ell)` term has coefficient bounded by

\[
(\log p)(p-1)p^a p^{-3(k+\ell)/4},
\qquad
k,\ell\ge a+1.
\tag{RR20}
\]

Its displacement magnitude is either

\[
|k-\ell|a_p
\quad\text{or}\quad
(k+\ell)a_p.
\tag{RR21}
\]

We prove a common `\beta_*=1/8` exponential moment.

### 5.1 Difference branches

Write

\[
k=m+d,
\qquad
\ell=m,
\qquad
d\ge1,
\]

with `m\ge a+1`. For fixed `m,d`, the largest coefficient over admissible levels occurs at `a=m-1`.  Using `p-1\le p`, the coefficient is then bounded by

\[
(\log p)p^{-m/2-3d/4}.
\tag{RR22}
\]

Since `\delta=da_p=(d/2)\log p`, multiplying by `e^{\delta/8}` gives

\[
(\log p)p^{-m/2-11d/16}.
\tag{RR23}
\]

The worst case `m=d=1` has exponent

\[
-\frac12-\frac{11}{16}=-\frac{19}{16}<-1.
\tag{RR24}
\]

### 5.2 Off-diagonal sum branches

Again `m\ge a+1`, `d\ge1`, and maximize at `a=m-1`. The unweighted coefficient is bounded by (RR22), while

\[
\delta=(2m+d)a_p
=\left(m+\frac d2\right)\log p.
\]

Hence the weighted coefficient is

\[
(\log p)p^{-3m/8-11d/16}.
\tag{RR25}
\]

The worst case `m=d=1` has exponent

\[
-\frac38-\frac{11}{16}
=-\frac{17}{16}<-1.
\tag{RR26}
\]

### 5.3 Diagonal sum branches

Let `k=\ell=m`.  The primitive level `a=m-1` is excluded exactly by RR19. Therefore every retained old-to-new diagonal sum term satisfies

\[
a\le m-2.
\]

The largest coefficient occurs at `a=m-2` and is bounded by

\[
(\log p)p^{-m/2-1}.
\tag{RR27}
\]

Here

\[
\delta=2ma_p=m\log p,
\]

so the `\beta=1/8` weighted coefficient is

\[
(\log p)p^{-3m/8-1}.
\tag{RR28}
\]

The smallest possible `m` is `2`, giving exponent

\[
-\frac34-1=-\frac74<-1.
\tag{RR29}
\]

All geometric sums over `m,d,a` are uniformly convergent for `p\ge2`, and the prime sums are dominated by the corresponding integer sums. Therefore

\[
\boxed{
\sum_{T\in\mathscr R_{\rm ret}}
e^{\delta(T)/8}\|T\|
\le C_{\rm ret}<\infty
}
\tag{RR30}
\]

uniformly in `U,V`.

### Local draft booking

```text
R43-COND-RETAINED-ROW-EXPONENTIAL-DISPLACEMENT-MOMENT ✓[M]
```

---

## 6. Retained-row collar plus tail

For a retained-row sign term `T` of displacement `\delta(T)\le r`, old-to-new crossing implies the input lies in the old terminal collar

\[
\chi_{U,r}:=1_{\{U-r<|u|<U\}}.
\]

Thus

\[
P_{\mathcal N}T\iota
=P_{\mathcal N}T\iota\chi_{U,r}.
\tag{RR31}
\]

From RR30,

\[
\left\|
\sum_{\delta(T)>r}T
\right\|
\le
C_{\rm ret}e^{-r/8}.
\tag{RR32}
\]

Therefore

\[
\boxed{
\|Y_{\rm ret}x\|
\le
C_{\rm ret}
\left(
\|\chi_{U,r}x\|
+e^{-r/8}\|x\|
\right).
}
\tag{RR33}
\]

Combining RR13 and RR33 gives the principal estimate

\[
\boxed{
\bigl(\Delta s_{\rm cond}^{U,V}(f)\bigr)_+
\le
C_{\rm ret}^2
\left(
\|\chi_{U,r}x_{U,V}(f)\|
+e^{-r/8}\|x_{U,V}(f)\|
\right)^2.
}
\tag{RR34}
\]

Under the terminal-graph normalization already used in PR #58,

\[
\|x_{U,V}(f)\|\le1,
\]

so

\[
\boxed{
\bigl(\Delta s_{\rm cond}^{U,V}(f)\bigr)_+
\le
C_{\rm ret}^2
\left(
\|\chi_{U,r}x_{U,V}(f)\|
+e^{-r/8}
\right)^2.
}
\tag{RR35}
\]

### Local draft booking

```text
R43-COND-RETAINED-ROW-CANCELLATION-BOUND ✓[M]
```

---

## 7. Consequence for the active COND front

RR35 gives a strictly different structured scalar route from the PR #58 leakage-only reduction.

For this route, separate decay estimates for hard11 and hard22 are no longer required.  The primitive hard channels live in newly resolved residual rows and are canceled at the scalar conditioning level by the exact negative residual increment `-C^*C` before any crude absolute summation is applied.

The remaining quantitative gate is

\[
\boxed{
\|\chi_{U,r}x_{U,V}(f)\|\to0
}
\tag{RR36}
\]

with a choice of `r=r(U,V)` and quantifiers strong enough for the later B-FLAGDYN/FD23 summability mechanism.

Thus the preferred structured scalar-COND route becomes

```text
exact geometric-mean transport
        |
        v
exact retained/new residual-row split
        |
        v
new-row cancellation against -C*C
        |
        v
retained-row exponential moment
        |
        v
TRANSPORTED COLLAR MASS DECAY ?[O]
        |
        v
structured scalar COND positive-increment control
```

This does **not** prove operatorwide `B-METINC-COND` and does not by itself provide the required cofinal summability.

---

## 8. Firewalls

Still OPEN:

```text
R43-COND-TRANSPORTED-COLLAR-MASS-DECAY
R43-COND-DECAY-TO-TELESCOPE-SUMMABILITY
ROADMAP-BRIDGE-COND-DIRECT-FLAGDYN
B-FLAGDYN / B-FLAGTIGHT
B-SIGN / B-ORIENT
Strong Terminal / C6
Object-X realization
RH
```

The earlier hard11/hard22 direct saturated-decay questions remain valid possible routes but are no longer necessary **for this specific structured scalar cancellation route** if RR35 is verified.

No Registry promotion is made by this Draft.