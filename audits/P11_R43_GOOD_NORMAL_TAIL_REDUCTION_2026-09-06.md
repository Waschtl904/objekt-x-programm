# P11 / R43 — good-normal exponential tail and two-hard-channel reduction

**Date:** 2026-09-06  
**Status:** exact/local quantitative reduction; `B-METINC-COND` and Strong Terminal remain OPEN  
**Stack base:** PR #57 head `4a28bde4d02e983d32ba9e2c28c0110445a7685b`

## 0. Scope

This note continues the geometric-mean resolvent reduction from PR #57.  It does not modify PR #55, #56, or #57.

The PR-#57 target is

\[
\mathfrak L_{U,V}^{\rm res}(f)
=(I+S^*S)^{-1/2}P_{\mathcal N}A_V\iota x_{U,V}(f),
\qquad
x_{U,V}(f):=\mathcal Q_{U,V}H_U^*E_{X,U}f,
\tag{GN0}
\]

where

\[
A_V=R_V^*R_V,
\qquad
S^*M=P_{\mathcal N}A_V\iota,
\]

and `\mathcal Q_{U,V}` is the positive geometric-mean contraction from PR #57.

The purpose here is to resolve the prime-power normal operator into translation-sign branches and prove that **all branches except two primitive diagonal sum channels** satisfy a horizon-uniform collar-plus-exponential-tail estimate.

No estimate on the two remaining hard channels is proved here.  No terminal decay of the full leakage is claimed.

---

## 1. Exact prime-sector normal expansion

For a prime `p` and `k\ge1`, write

\[
a_p:=\frac12\log p,
\qquad
D_{p,k}:=D_{k\log p}=U_{ka_p}-U_{-ka_p},
\qquad
b_{p,k}:=\sqrt{\log p}\,p^{-k/4}.
\tag{GN1}
\]

At horizon `V`, put

\[
q_{p,k;V}(u):=\mathsf Q_V(u)\eta_{p,k}.
\]

Different prime sectors are orthogonal.  Therefore, after expanding the target inner product,

\[
\boxed{
A_V
=\sum_p\sum_{k,l\ge1}
E_V^*D_{p,k}^*\,
M_{\alpha_{p;k,l}^{V}}\,
D_{p,l}E_V,
}
\tag{GN2}
\]

where `M_\alpha` is multiplication by

\[
\alpha_{p;k,l}^{V}(u)
:=b_{p,k}b_{p,l}
\langle q_{p,k;V}(u),q_{p,l;V}(u)\rangle.
\tag{GN3}
\]

The two-prime R43 audit already proved the exact projected-mark Gram formula

\[
\langle q_{p,k}^{(J)},q_{p,l}^{(J)}\rangle
=p^{-(k+l)/2}(p^m-1),
\qquad
m=\min\{J,k,l\}.
\tag{GN4}
\]

Thus, with `m_0:=\min\{k,l\}`,

\[
\boxed{
\|\alpha_{p;k,l}^{V}\|_{L^\infty}
\le
(\log p)\,p^{-3(k+l)/4+m_0}.
}
\tag{GN5}
\]

Writing

\[
k=m_0+d,\quad l=m_0
\qquad\text{or vice versa},
\qquad d=|k-l|,
\]

this becomes

\[
\boxed{
\|\alpha_{p;k,l}^{V}\|_\infty
\le
(\log p)\,p^{-m_0/2}\,p^{-3d/4}.
}
\tag{GN6}
\]

The bound is independent of `V`.

Each `D_{p,k}^*M_\alpha D_{p,l}` contains four translation-sign terms.  Multiplication does not change spatial support, so every such sign term has one of the two net displacement magnitudes

\[
\boxed{
|k-l|a_p
\qquad\text{or}\qquad
(k+l)a_p.
}
\tag{GN7}
\]

Each individual sign term has operator norm at most `\|\alpha_{p;k,l}^V\|_\infty`; endpoints and zero extension do not increase this norm.

### Local booking

```text
R43-COND-NORMAL-SIGN-BRANCH-EXPANSION ✓[M]
```

---

## 2. Which branches are absolutely summable?

### 2.1 Nonzero difference branches

For the difference branch one has `d=|k-l|\ge1`.  From GN6,

\[
\sum_{m_0\ge1}\sum_{d\ge1}
(\log p)p^{-m_0/2}p^{-3d/4}
<\infty
\]

for every `p`, and after summing over primes the smallest exponent occurs at `m_0=d=1`:

\[
p^{-1/2}p^{-3/4}=p^{-5/4}.
\]

Hence the entire nonzero-difference branch is absolutely summable in operator norm, uniformly in `V`.

### 2.2 Sum branches

The sum displacement is

\[
(k+l)a_p=(2m_0+d)a_p.
\]

If `d\ge1`, the smallest coefficient again has exponent `5/4`, so every off-diagonal sum branch is uniformly absolutely summable.

For diagonal sum branches `k=l=m_0`, GN6 reduces to

\[
(\log p)p^{-m_0/2}.
\tag{GN8}
\]

The sum over primes is absolutely convergent for every `m_0\ge3`, but not by this crude absolute estimate for `m_0=1,2`.

Thus the only nonzero-displacement sign branches not belonging to a horizon-uniform absolutely summable family are precisely

\[
\boxed{k=l=1\quad\text{and}\quad k=l=2}
\tag{GN9}
\]

in the **sum-sign** part.

For `k=l`, the other two sign terms have zero net displacement.  Such a zero-shift multiplication term maps the old source space into itself and hence is killed exactly by `P_{\mathcal N}` after old-source embedding:

\[
\boxed{
P_{\mathcal N}\,T_{\rm zero}\,\iota=0.
}
\tag{GN10}
\]

Define `A_V^{\rm hard}` to be exactly the two diagonal sum-sign families in GN9, summed over primes.  Let `A_V^{\rm good}` contain all remaining nonzero-displacement sign branches.  Then on the old-to-new block,

\[
\boxed{
P_{\mathcal N}A_V\iota
=P_{\mathcal N}A_V^{\rm hard}\iota
+P_{\mathcal N}A_V^{\rm good}\iota.
}
\tag{GN11}
\]

### Local booking

```text
R43-COND-TWO-HARD-DIAGONAL-NORMAL-CHANNELS ✓[M]
```

This is a structural reduction only; it does not say that the two hard channels are large after saturation.

---

## 3. Exponential moment for the good branch

We now prove more than absolute summability: the good branch has a finite exponential displacement moment.

For a sign term `T`, write `\delta(T)` for its net displacement magnitude.

### 3.1 Difference terms

Choose any

\[
0<\beta<\frac12.
\]

For a difference term with parameters `(p,m_0,d)`, `d\ge1`,

\[
\delta=d a_p=\frac d2\log p.
\]

Multiplying GN6 by `e^{\beta\delta}` gives

\[
(\log p)
 p^{-m_0/2}
 p^{-d(3/4-\beta/2)}.
\tag{GN12}
\]

At `m_0=d=1` the total exponent is

\[
\frac12+\frac34-\frac\beta2
=\frac54-\frac\beta2>1.
\]

The geometric sums over `m_0,d` are uniformly bounded for `p\ge2`, and the prime sum is bounded by the corresponding integer sum.  Therefore

\[
\sum_{T\in\mathscr G_{\rm diff}}
 e^{\beta\delta(T)}\|T\|<\infty.
\tag{GN13}
\]

### 3.2 Off-diagonal sum terms

Choose

\[
0<\beta<\frac16.
\]

For `d\ge1`,

\[
\delta=(2m_0+d)a_p
=\left(m_0+\frac d2\right)\log p.
\]

The exponentially weighted GN6 coefficient is

\[
(\log p)
 p^{-m_0(1/2-\beta)}
 p^{-d(3/4-\beta/2)}.
\tag{GN14}
\]

At `m_0=d=1` the exponent is

\[
\left(\frac12-\beta\right)
+\left(\frac34-\frac\beta2\right)
=\frac54-\frac{3\beta}{2}>1.
\]

Hence the off-diagonal sum family has finite `\beta`-exponential displacement moment.

### 3.3 Diagonal sum terms with `m_0\ge3`

Here

\[
\delta=2m_0a_p=m_0\log p,
\]

and the weighted coefficient is

\[
(\log p)p^{-m_0(1/2-\beta)}.
\tag{GN15}
\]

For every `\beta<1/6` and `m_0\ge3`,

\[
m_0(1/2-\beta)>1.
\]

Thus this family also has finite exponential moment.

Taking for definiteness

\[
\boxed{\beta_*:=\frac18,}
\tag{GN16}
\]

all good branches satisfy one common bound

\[
\boxed{
\sum_{T\in\mathscr G}
 e^{\beta_*\delta(T)}\|T\|
\le C_*<\infty,
}
\tag{GN17}
\]

with `C_*` absolute and independent of `U,V`.

In particular, for the subfamily with `\delta(T)>r`,

\[
\boxed{
\left\|
\sum_{\substack{T\in\mathscr G\\\delta(T)>r}}T
\right\|
\le C_*e^{-r/8}.
}
\tag{GN18}
\]

### Local booking

```text
R43-COND-GOOD-NORMAL-EXPONENTIAL-DISPLACEMENT-MOMENT ✓[M]
```

---

## 4. Short displacement forces an old-source collar

For `0<r<U`, let

\[
\chi_{U,r}
:=1_{\{U-r<|u|<U\}}
\tag{GN19}
\]

on the old source space `L^2(-U,U)`.

Let `T` be any translation-multiplication-translation sign term with net displacement magnitude at most `r`.  If its output lies in the new-source summand

\[
\mathcal N=L^2((-V,V)\setminus(-U,U)),
\]

while its input is old-supported in `(-U,U)`, then the input point must lie within distance `r` of one of the old boundaries.  Therefore

\[
\boxed{
P_{\mathcal N}T\iota
=P_{\mathcal N}T\iota\,\chi_{U,r}
\qquad(\delta(T)\le r).
}
\tag{GN20}
\]

This is a pure support statement and remains valid with the source-dependent scalar multipliers `\alpha^V_{p;k,l}`.

Split

\[
A_V^{\rm good}
=A_{V,\le r}^{\rm good}+A_{V,>r}^{\rm good}
\]

by net displacement.  GN17 gives

\[
\|A_{V,\le r}^{\rm good}\|\le C_*,
\qquad
\|A_{V,>r}^{\rm good}\|\le C_*e^{-r/8}.
\]

Combining with GN20 yields the horizon-uniform bound

\[
\boxed{
\|P_{\mathcal N}A_V^{\rm good}\iota x\|
\le
C_*\|\chi_{U,r}x\|
+C_*e^{-r/8}\|x\|.
}
\tag{GN21}
\]

Since `(I+S^*S)^{-1/2}` is a contraction, the same estimate holds after saturation:

\[
\boxed{
\|(I+S^*S)^{-1/2}
P_{\mathcal N}A_V^{\rm good}\iota x\|
\le
C_*\bigl(
\|\chi_{U,r}x\|+e^{-r/8}\|x\|
\bigr).
}
\tag{GN22}
\]

### Local booking

```text
R43-COND-GOOD-NORMAL-COLLAR-PLUS-TAIL ✓[M]
```

---

## 5. Exact normalized geometric-mean contraction

The PR-#57 geometric-mean transport satisfies

\[
\mathcal Q\,\mathscr G\,\mathcal Q=B_U,
\qquad
\mathscr G=I+M^*(I+SS^*)^{-1}M\succeq I.
\tag{GN23}
\]

Therefore

\[
\boxed{
\mathcal Q^2\preceq B_U.
}
\tag{GN24}
\]

For the structured hub vector

\[
v_U(f)=H_U^*E_{X,U}f,
\]

this gives

\[
\boxed{
\|\mathcal Qv_U(f)\|^2
\le
\langle v_U(f),B_Uv_U(f)\rangle
=s_U(f)
\le q_U^X(E_{X,U}f).
}
\tag{GN25}
\]

Thus for a source vector normalized in the actual terminal graph metric,

\[
q_U^X(E_{X,U}f)=1,
\]

one has the uniform contraction

\[
\boxed{
\|x_{U,V}(f)\|
=\|\mathcal Q_{U,V}H_U^*E_{X,U}f\|
\le1.
}
\tag{GN26}
\]

No support preservation is inferred.

### Local booking

```text
R43-COND-NORMALIZED-GEOMETRIC-TRANSPORT-CONTRACTION ✓[M]
```

---

## 6. Quantitative reduction of normalized transported leakage

Put

\[
x:=x_{U,V}(f)=\mathcal Q_{U,V}v_U(f).
\]

By GN11 and the triangle inequality,

\[
\begin{aligned}
\|(I+S^*S)^{-1/2}P_{\mathcal N}A_V\iota x\|
\le{}&
\|(I+S^*S)^{-1/2}P_{\mathcal N}A_V^{\rm hard}\iota x\|\\
&+C_*\|\chi_{U,r}x\|
+C_*e^{-r/8}\|x\|.
\end{aligned}
\tag{GN27}
\]

For terminally normalized `f`, GN26 gives

\[
\boxed{
\|\mathfrak L_{U,V}^{\rm res}(f)\|
\le
\mathfrak H_{U,V}(f)
+C_*\|\chi_{U,r}x_{U,V}(f)\|
+C_*e^{-r/8},
}
\tag{GN28}
\]

where the **two-hard-channel saturated leakage** is

\[
\boxed{
\mathfrak H_{U,V}(f)
:=
\|(I+S^*S)^{-1/2}
P_{\mathcal N}A_V^{\rm hard}\iota
x_{U,V}(f)\|.
}
\tag{GN29}
\]

Consequently the whole quantitative COND problem has been reduced to two tasks:

1. control terminal-collar mass of the geometric-mean transported structured vector;
2. control the two primitive diagonal sum channels `k=l=1,2` after the exact saturation.

Everything else carries a uniform exponentially decaying displacement tail.

---

## 7. Why the two hard channels are genuinely special

For `k=l=1`, the full projected mark at depth at least one has squared norm

\[
1-p^{-1},
\]

so the diagonal coefficient is of order

\[
(\log p)p^{-1/2}.
\]

Its nonzero sum displacement is

\[
2a_p=\log p.
\]

For `k=l=2`, at full depth two the diagonal coefficient is of order

\[
(\log p)p^{-1},
\]

and the nonzero sum displacement is

\[
4a_p=2\log p.
\]

These two prime sums are not absolutely summable by the horizon-uniform estimate used above.  They therefore cannot be hidden inside GN17.

This does **not** imply that their saturated action is large.  The factor

\[
(I+S^*S)^{-1/2}
\]

is precisely capable of suppressing large new-source self-energy, and the geometric-mean transport `\mathcal Q` may suppress the corresponding old-source direction.  Those effects remain to be exploited rather than discarded by a crude absolute sum.

---

## 8. Firewalls

1. GN17 is an **absolute operator-tail** theorem only for the good branch; it excludes the two channels GN9.
2. GN20 is collar forcing for a projected old-to-new translation term; it does not state that the original structured vector itself is collar-supported.
3. O3k fixed-window Sobolev regularity cannot currently be used to turn `\|\chi_{U,r}x\|` into a uniform terminal rate: its positive Sobolev exponent is explicitly nonuniform in the growing horizon.
4. The older off-support hub formula does not propagate through `B_U` or `\mathcal Q`; both are nonlocal.
5. GN26 is a norm contraction after terminal normalization, not a localization theorem.
6. No estimate on `\mathfrak H_{U,V}` is proved.
7. No `B-METINC-COND`, Strong Terminal/C6, Object X, or RH promotion is made.

---

## 9. Status ledger

New local theorem-level bookings:

```text
R43-COND-NORMAL-SIGN-BRANCH-EXPANSION                 ✓[M]
R43-COND-TWO-HARD-DIAGONAL-NORMAL-CHANNELS            ✓[M]
R43-COND-GOOD-NORMAL-EXPONENTIAL-DISPLACEMENT-MOMENT  ✓[M]
R43-COND-GOOD-NORMAL-COLLAR-PLUS-TAIL                 ✓[M]
R43-COND-NORMALIZED-GEOMETRIC-TRANSPORT-CONTRACTION   ✓[M]
```

New/refined OPEN nodes:

```text
R43-COND-TRANSPORTED-COLLAR-MASS-DECAY ?[O]
R43-COND-TWO-HARD-CHANNEL-SATURATED-DECAY ?[O]
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
B-METINC-COND ?[O]
B-METINC ?[O]
B-FLAGMOD / B-FLAGDYN ?[O]
B-FLAGTIGHT ?[O]
B-SIGN / B-ORIENT ?[O]
Strong Terminal / C6 ?[O]
Object X / RH ?[O]
```

---

## 10. Next attack

The preferred next target is not another global `A_V` estimate.  It is the saturated hard block

\[
(I+S^*S)^{-1/2}P_{\mathcal N}A_V^{\rm hard}\iota,
\]

where `A_V^{\rm hard}` consists only of the `k=l=1` and `k=l=2` diagonal sum shifts.

Because `S^*S=P_{\mathcal N}A_VP_{\mathcal N}` contains the same prime-sector energy on the new source block, the next proof should keep this denominator intact and seek a channel-wise or quadratic-form comparison rather than estimate the hard numerator by its divergent unsaturated prime sum.
