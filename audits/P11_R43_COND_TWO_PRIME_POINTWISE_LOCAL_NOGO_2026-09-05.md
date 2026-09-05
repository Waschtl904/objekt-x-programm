# P11 / R43 — two-prime pointwise-local COND PSD no-go

**Date:** 2026-09-05  
**Status:** theorem-level local negative strengthening of the arbitrary-source COND Loewner route; `B-METINC-COND`, partition-selective PSD, epsilon-relaxed control, structured-vector COND, Strong Terminal/C6 remain OPEN.

## 0. Scope

This note strengthens the merged `p=2` kernel-witness theorem without changing its scope firewall.

The old theorem showed

\[
\forall U_*,h_*>0\ \exists U\ge U_*\ \exists h\in(0,h_*):
K_{U,U+h}^{\rm Schur}\not\succeq0.
\]

The strict referee suggested a stronger "co-countable in `U`, all `h>0`" form.  That proposed form is **not** justified by the old fine-step proof: the dead-layer and one-new-martingale-layer arguments require a genuinely small terminal increment.  The correct strengthening is different and stronger in the terminal variable:

\[
\boxed{
\exists U_0>0\ \forall U\ge U_0\ \exists h_0(U)>0\ \forall h\in(0,h_0(U)):
K_{U,U+h}^{\rm Schur}\not\succeq0.
}
\tag{TP0}
\]

Thus **every sufficiently late terminal has a right-hand punctured neighbourhood consisting entirely of non-PSD canonical COND steps**.  The radius `h_0(U)` is allowed to depend on `U` and may tend to zero.

This still does not exclude a specially selected cofinal partition whose steps stay above the local forbidden radius.

---

## 1. Frozen mark formula and exact Gram identity

P11 fixes

\[
\eta_{p,k}
=\sqrt{p-1}\sum_{j=0}^{k-1}p^{(j-k)/2}\psi_{p,j},
\]

and, at martingale depth `J`, the source projection keeps exactly the levels `j<J`.  Hence with

\[
q_{p,k}^{(J)}:=Q_J\eta_{p,k}
\]

and

\[
m:=\min\{J,k,l\},
\]

one has exactly

\[
\begin{aligned}
\langle q_{p,k}^{(J)},q_{p,l}^{(J)}\rangle
&=(p-1)p^{-(k+l)/2}\sum_{j=0}^{m-1}p^j\\
&=p^{-(k+l)/2}(p^m-1).
\end{aligned}
\tag{TP1}
\]

In particular, for `J=2`, `k=1`, `l=2`,

\[
\boxed{
\langle q_{p,1}^{(2)},q_{p,2}^{(2)}\rangle
=(p-1)p^{-3/2}>0.
}
\tag{TP2}
\]

This gives, after multiplying the two frozen residual coefficients

\[
\sqrt{\log p}\,p^{-1/4},
\qquad
\sqrt{\log p}\,p^{-1/2},
\]

the exact first adjacent-overlap weight

\[
\boxed{
(\log p)(p-1)p^{-9/4}>0.
}
\tag{TP3}
\]

For `p=2` this is the previously used `(\log2)2^{-9/4}`.

### Mark-Gram convention check against the older `F_K` witness

There is no sign or exponent inconsistency with the older source-separation `2a_2=\log2` construction.

There the outer `F_0` term uses `k=l=1`, terminal depth `J=1`, hence

\[
\langle q_{2,1}^{(1)},q_{2,1}^{(1)}\rangle=\frac12.
\]

Multiplying the two residual weights gives `2^{-1/2}`, and the **opposite translation signs** give

\[
-2^{-1/2}\cdot\frac12=-2^{-3/2}.
\]

By contrast, the present adjacent witness has the **Gram factor itself** equal to `+2^{-3/2}` before multiplying the residual weights.  The repeated numerical magnitude comes from different factors in two different geometries.

Book locally:

```text
R43-COND-MARK-GRAM-CONVENTION-CONSISTENCY ✓[M]
```

---

## 2. Prime-`p` adjacent source geometry

Put

\[
a_r:=\frac12\log r
\]

for every prime `r`, and let

\[
\Lambda:=\{n a_r:\ r\text{ prime},\ n\ge2\}.
\tag{TP4}
\]

Fix a witness prime `p` and a terminal `U`.  Define the exceptional set

\[
E_p:=\{U>0:\ 2U-a_p\in\Lambda\}.
\tag{TP5}
\]

If `U\notin E_p`, local finiteness of `\Lambda` gives

\[
\rho_{p,U}:=\operatorname{dist}(2U-a_p,\Lambda)>0.
\tag{TP6}
\]

For a fine step `V=U+h`, set `\varepsilon=h/2` and choose a sufficiently short interval

\[
I_Q\subset(U,V)
\]

centred at `U+\varepsilon`, then put

\[
I_P:=I_Q-a_p,
\qquad
f:=1_{I_P},
\qquad
g:=1_{I_Q}.
\tag{TP7}
\]

The source separation is exactly `a_p`.

---

## 3. Why the simple kernel mechanism works precisely for `p=2,3`

Assume the global fine-step condition

\[
0<h<a_2.
\tag{TP8}
\]

Then the new outer spatial strip has martingale depth zero for every prime, and every old spatial row gains at most one martingale level.

For a new layer in prime sector `r`, with new level index `j\ge1`, the scalar amplitude sees only translation indices `k\ge j`.

Let

\[
d_p:=a_p-\varepsilon
\]

be the distance of `I_P` from the old right boundary.

### 3.1 Near same-side translation

A hit of `I_P` from a positive depth-increment row with the translation directed toward the boundary would force, up to the `h`/support tolerances,

\[
d_p\approx(j-k)a_r\le0,
\]

which is impossible because `d_p>0`.

### 3.2 Far same-side translation

The opposite translation sign would force

\[
d_p\approx(j+k)a_r.
\]

Because `r` is prime, `r\ge2`, and because `j,k\ge1`, one has the explicit uniform floor

\[
(j+k)a_r\ge2a_2,
\]

with equality only at `r=2`, `j=k=1`. Therefore this direction is automatically excluded whenever

\[
a_p<2a_2
\]

and the fine-step/support tolerances are chosen below the fixed margin

\[
\delta_p:=2a_2-a_p>0.
\tag{TP9}
\]

Exactly the two smallest primes satisfy this:

\[
\delta_2=a_2>0,
\qquad
\delta_3=2a_2-a_3
=\frac12\log\frac43>0.
\tag{TP10}
\]

For `p=5`, already `a_5>2a_2`, so the simple support argument can be hit by a lower-prime same-side layer.  Thus the referee suggestion to continue mechanically with `p=5` is not type-safe without a new cancellation argument.

This is why the exact strengthening below uses the natural pair `p=2,3`.

---

## 4. Exact kernel statement for `p=2` or `p=3`

Fix `p\in\{2,3\}` and `U\notin E_p`.  Put

\[
\delta_p:=2a_2-a_p>0.
\]

Choose

\[
0<h<
\min\left\{
\frac{a_2}{8},
\frac{\delta_p}{16},
\frac{\rho_{p,U}}{64}
\right\}
\tag{TP11}
\]

and then choose the interval length `\ell=|I_Q|` so that

\[
0<\ell<
\min\left\{
\frac h4,
\frac{\delta_p}{64},
\frac{\rho_{p,U}}{64}
\right\}.
\tag{TP12}
\]

After `(TP11)`--`(TP12)`, shrink `\ell` once more if necessary by the finite non-exact-overlap gap `(H4)` from

`audits/P11_R43_COND_TWO_PRIME_NONEXACT_OVERLAP_HARDENING_2026-09-05.md`.

This additional condition depends on `(U,h,p)` and only decreases `\ell`; it does **not** alter the already chosen step `h` or any terminal-radius estimate below.

The same-side alternatives are excluded by Sections 3.1--3.2.

For a negative depth-increment row, the only possible hit of the positive interval `I_P` is an opposite-boundary translation.  Combining the depth band with a translation index `k\ge j` gives

\[
\left|
2U-a_p+\varepsilon-(j+k)a_r
\right|<h+\ell.
\tag{TP13}
\]

Since `j+k\ge2`, the quantity `(j+k)a_r` lies in `\Lambda`.  By (TP11)--(TP12),

\[
\operatorname{dist}(2U-a_p+\varepsilon,\Lambda)
\ge \rho_{p,U}-\varepsilon
\]

is much larger than `h+\ell`.  Thus (TP13) is impossible.

Hence every newly exposed residual component vanishes:

\[
\boxed{C_{U,U+h}f=0.}
\tag{TP14}
\]

This is a full-operator statement over all prime sectors.

---

## 5. The strip coupling is strictly nonzero for the same witness

At fixed `V=U+h`, only finitely many translated source packets can participate. The hardening condition `(H4)` excludes every non-exact shift mismatch. Consequently an actual surviving overlap between an `f`-translate and a `g`-translate in a prime sector `r` must satisfy one of the exact relations

\[
|k-l|a_r=a_p
\quad\text{or}\quad
(k+l)a_r=a_p.
\tag{TP15}
\]

The second alternative is impossible because `k+l\ge2`, `r\ge2`, and therefore

\[
(k+l)a_r\ge2a_2>a_p
\]

for the witness primes `p\in\{2,3\}`.  The first gives

\[
r^{|k-l|}=p.
\]

Since `p` is prime, necessarily

\[
\boxed{r=p,\qquad |k-l|=1.}
\tag{TP16}
\]

Thus the source separation isolates the witness prime exactly; different prime sectors are orthogonal anyway.

Consider the first left-going adjacent overlap with source indices

\[
l=1\quad\text{for }f,
\qquad
k=2\quad\text{for }g.
\]

It lies on the output interval `I_Q-2a_p`.  For all sufficiently late `U` this interval lies inside the old spatial window.  From `\varepsilon=h/2` and `h<a_2\le a_p`,

\[
J_{p,U}=1,
\qquad
J_{p,U+h}=2
\]

on that interval.  Therefore (TP2)--(TP3) give the exact positive contribution

\[
\boxed{
\ell(\log p)(p-1)p^{-9/4}>0.
}
\tag{TP17}
\]

Every other surviving exact overlap has equal translation signs (hence sign product `+1`) and a nonnegative projected-mark Gram coefficient by (TP1).  Hence no cancellation is possible and

\[
\boxed{
\langle Mf,Sg\rangle>0,
\qquad
S^*Mf\ne0.
}
\tag{TP18}
\]

Combining with (TP14),

\[
\boxed{
\langle f,K_{U,U+h}^{\rm Schur}f\rangle
=-\|(I+S^*S)^{-1/2}S^*Mf\|^2<0.
}
\tag{TP19}
\]

Therefore, for each `p\in\{2,3\}` and every `U\notin E_p`, one may take for example

\[
h_p(U):=
\min\left\{
\frac{a_2}{8},
\frac{\delta_p}{16},
\frac{\rho_{p,U}}{64}
\right\}>0,
\]

and every smaller positive step admits the witness after choosing `\ell` as above. Thus

\[
\boxed{
0<h<h_p(U)
\Longrightarrow
K_{U,U+h}^{\rm Schur}\not\succeq0.
}
\tag{TP20}
\]

---

## 6. The two exceptional sets are disjoint

Suppose for contradiction that

\[
U\in E_2\cap E_3.
\]

Then there exist primes `q,r` and integers `n,m\ge2` such that

\[
2U-a_2=n a_q,
\qquad
2U-a_3=m a_r.
\]

Exponentiating after multiplying by two gives

\[
\boxed{2q^n=3r^m.}
\tag{TP21}
\]

Unique prime factorization makes this impossible.

Indeed, because the right side must contain the prime `2`, one must have `r=2`; because the left side must contain the prime `3`, one must have `q=3`.  Then (TP21) reduces to

\[
2\,3^n=3\,2^m
\quad\Longrightarrow\quad
3^{n-1}=2^{m-1},
\]

impossible for `n,m\ge2`.

Hence

\[
\boxed{E_2\cap E_3=\varnothing.}
\tag{TP22}
\]

This is stronger and cheaper than a three-prime compatibility argument.

---

## 7. Breakthrough: pointwise-local non-PSD at every late terminal

Choose a fixed safe terminal threshold, for example

\[
U_0>2a_3.
\]

For every `U\ge U_0`, disjointness (TP22) implies that at least one of `U\notin E_2` or `U\notin E_3` holds.  Choose any available witness prime `p(U)\in\{2,3\}` with `U\notin E_{p(U)}` and let `h_0(U):=h_{p(U)}(U)>0` be the radius from (TP20). If both witness primes are available, either choice proves TP23; for the quantitative floor in Section 8 one may choose the available prime with the larger `\rho_{p,U}`.

Then

\[
\boxed{
\exists U_0>0\ \forall U\ge U_0\ \exists h_0(U)>0\ \forall h\in(0,h_0(U)):
K_{U,U+h}^{\rm Schur}\not\succeq0.
}
\tag{TP23}
\]

This is strictly stronger than the previously booked cofinal `\forall\forall\exists\exists` no-go.

Local booking:

```text
R43-COND-TWO-PRIME-POINTWISE-LOCAL-NOGO ✓[M]_neg
```

Interpretation: there are no late terminal points at which canonical arbitrary-source Loewner PSD persists under arbitrarily fine right refinements.

---

## 8. Quantitative universal lower scale for the forbidden radius

The two-prime argument also gives a very weak but explicit universal scale.

Write

\[
E_p=\left\{\frac14\log(pq^n):\ q\text{ prime},\ n\ge2\right\}
\]

and

\[
d_p(U):=\operatorname{dist}(U,E_p),
\qquad
\rho_{p,U}=2d_p(U).
\]

Because `E_2` and `E_3` are disjoint, nearest points `x_2\in E_2`, `x_3\in E_3` correspond to distinct positive integers

\[
N_2=e^{4x_2}=2q^n,
\qquad
N_3=e^{4x_3}=3r^m.
\]

If both nearest-point distances are below `1`, then `x_2,x_3\le U+1`, so

\[
\max(N_2,N_3)\le e^{4(U+1)}.
\]

For the two distinct positive integers put

\[
N_{\max}:=\max(N_2,N_3),
\qquad
N_{\min}:=\min(N_2,N_3).
\]

Then, without any hidden ordering convention,

\[
\begin{aligned}
4|x_2-x_3|
&=\log\frac{N_{\max}}{N_{\min}}\\
&=\log\left(1+\frac{N_{\max}-N_{\min}}{N_{\min}}\right)\\
&\ge \frac{N_{\max}-N_{\min}}{N_{\max}}\\
&\ge \frac1{N_{\max}}\\
&\ge e^{-4(U+1)}.
\end{aligned}
\tag{TP24}
\]

Since

\[
|x_2-x_3|\le d_2(U)+d_3(U),
\]

we have

\[
d_2(U)+d_3(U)\ge\frac14e^{-4(U+1)}.
\]

Therefore

\[
\max\{d_2(U),d_3(U)\}
\ge\frac18e^{-4(U+1)},
\]

and because `\rho_{p,U}=2d_p(U)`, this is exactly

\[
\boxed{
\max\{\rho_{2,U},\rho_{3,U}\}
\ge \frac14 e^{-4(U+1)}.
}
\tag{TP25}
\]

This proves TP25 when both `d_2(U),d_3(U)<1`.

If instead one of the two distances, say `d_p(U)`, is at least `1`, then `\rho_{p,U}\ge2`. If this prime is available (`U\notin E_p`), TP20 gives

\[
h_p(U)\ge
\min\left\{
\frac{a_2}{8},
\frac{\delta_p}{16},
\frac{2}{64}
\right\}
=:c_p^{(0)}>0.
\]

If the prime with distance at least `1` is exceptional at `U`, its distance would be zero, so this case cannot occur; hence such a prime is automatically available. Thus in the `d_p(U)\ge1` case the forbidden radius has an absolute positive lower bound, which is certainly at least `c_*e^{-4U}` for all sufficiently large `U` after decreasing `c_*>0` once.

In the remaining case, choose among the available witness primes one with maximal `\rho_{p,U}`. By TP25 and TP20,

\[
h_0(U)\ge \frac1{64}\max\{\rho_{2,U},\rho_{3,U}\}
\]

up to the fixed positive caps `a_2/8` and `\delta_p/16`; for sufficiently large `U` the exponentially small term is below those caps. Consequently there is an absolute `c_*>0` such that, for all sufficiently large `U`,

\[
\boxed{h_0(U)\ge c_*e^{-4U}.}
\tag{TP26}
\]

No optimality is claimed. The fixed factor `e^{-4}` coming from `(U+1)` is absorbed into `c_*`.

Consequently, any terminal step that is actually canonical-PSD must obey the necessary floor

\[
\boxed{
K_{U,U+h}^{\rm Schur}\succeq0
\Longrightarrow
h\ge c_*e^{-4U}
}
\tag{TP27}
\]

for all sufficiently late `U`.

Local booking:

```text
R43-COND-PARTITION-PSD-STEP-FLOOR ✓[M]
```

This still does **not** rule out a cofinal PSD partition, because a sequence with step sizes above an exponentially small floor can still reach infinity while tending to zero.

---

## 9. What this does and does not do to the live tree

The stronger theorem upgrades the arbitrary-source operator no-go from "bad pairs occur kofinally" to "every late terminal has a whole forbidden fine-step neighbourhood".

It does **not** prove

```text
R43-COND-PARTITION-SELECTIVE-PSD ×[M]
```

because the forbidden radius depends on `U`.  A specially selected partition could, in principle, choose every used step above `h_0(U_j)` and still have `h_j->0`.

Therefore retain

```text
R43-COND-PARTITION-SELECTIVE-PSD ?[O]
R43-COND-EPSILON-RELAXED-TELESCOPE ?[O]
```

but sharpen the necessary condition for the first route by (TP27).

The theorem also does not say anything negative about the structured canonical vector

\[
v_U=H_U^*E_{X,U}f.
\]

`B-METINC-COND`, B-FLAGMOD/B-FLAGDYN, B-FLAGTIGHT, Strong Terminal/C6, Object X and RH remain OPEN.

---

## 10. Correct response to the strict referee's proposed strengthening

The referee's suggestion

```text
for co-countably many U, for all h>0: K_{U,U+h} not PSD
```

is not adopted.  The old proof's outer-dead-layer and one-new-layer structure is fine-step dependent, and for large `h` the new outer spatial strip can itself carry residual depth.

The correct replacement is the stronger-in-`U`, local-in-`h` theorem (TP23), obtained from the exact `p=2` and `p=3` pair.

Similarly, no `p=5` theorem is booked: the simple same-side support firewall ceases to be automatic once `a_p\ge2a_2`.

This is a theorem-level strengthening, not a merge or project-level promotion.  PR #54 remains Draft pending external re-review and full-diff inspection.