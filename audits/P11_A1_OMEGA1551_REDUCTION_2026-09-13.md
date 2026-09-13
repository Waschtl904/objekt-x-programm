# P11 A1-OMEGA1551 — rigorous band shrink and 1212-dimensional finite target

**Date:** 2026-09-13  
**Status:** theorem-level / exact-head Arb-certified project audit; no Registry promotion.  
**Parent main:** `c03c1f3aa43416fe8f2951002614988e2aa03d59` / PR #114.

## 1. Purpose

PR #114 reduced the full `a=1` canonical completion to a finite resolved lower-bound problem of dimension at most `1682`, using the deliberately coarse high-frequency threshold `Omega=2300`.

This audit sharpens that quantitative reduction without changing the proof architecture. A new interval-rigorous grid/Lipschitz certificate proves

```math
\boxed{m_1(\xi)>0.1\qquad(|\xi|\ge1551).}
```

Combining the smaller band with the same Karnik--Romberg--Davenport PSWF estimate reduces the sufficient resolved space to at most `1212` dimensions and the Schur penalty to approximately `2.12e-39`.

The remaining sufficient finite target becomes

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I.}
```

No resolved lower bound and no `a=1` positivity theorem is proved here.

---

## 2. Exact multiplier imported from A1-TAIL

For zero-extended `v` supported in `(-1,1)`,

```math
q_1(v)=\int_{\mathbb R}m_1(\xi)|\widehat v(\xi)|^2d\xi,
```

where

```math
m_1(\xi)=
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
```

The symbol is even.

---

## 3. Pointwise digamma lower bound

For `x>0`, DLMF 5.7.6 gives

```math
\operatorname{Re}\psi(x+iy)-\psi(x)
=
\sum_{k=0}^{\infty}
\frac{y^2}{(k+x)((k+x)^2+y^2)}.
```

With

```math
f_y(u)=\frac{y^2}{u(u^2+y^2)},
```

`f_y` is positive and decreasing, hence

```math
\sum_{k=N}^{\infty}f_y(k+x)
\ge
\int_N^\infty f_y(t+x)dt
=
\frac12\log\left(1+\frac{y^2}{(N+x)^2}\right).
```

The checker uses `N=64` and the exact value

```math
\psi(1/4)=-\gamma-\pi/2-3\log2.
```

---

## 4. Rigorous derivative bound `✓[M]`

For `z=x+iy`,

```math
\psi'(z)=\sum_{k=0}^{\infty}\frac1{(k+z)^2}.
```

Therefore

```math
|\psi'(x+iy)|
\le
\sum_{k=0}^{\infty}\frac1{(k+x)^2+y^2}.
```

Since the summand is decreasing,

```math
\sum_{k=0}^{\infty}\frac1{(k+x)^2+y^2}
\le
\frac1{x^2+y^2}
+
\int_0^\infty\frac{dt}{(t+x)^2+y^2}.
```

Thus

```math
\left|\frac d{d\xi}
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)
\right|
\le
\frac12\left[
\frac1{(1/4)^2+y^2}
+
\frac{\pi/2-\arctan((1/4)/y)}{y}
\right],
\quad y=|\xi|/2.
```

The Prime-Power part contributes at most

```math
2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\log n.
```

At `|xi|>=1551`, the exact-head Arb gate certifies

```math
\boxed{|m_1'(\xi)|<8.214249<8.22.}
```

---

## 5. Compact interval certificate `[1551,2500]` `✓[K/M]`

Use the exact rational grid

```text
xi_j = 1551 + j/50,
```

so the spacing is `0.02`. Every point of `[1551,2500]` is within `0.01` of a grid point.

At every grid point the checker evaluates a rigorous lower bound using:

- the 64-term positive digamma sum;
- the rigorous integral tail;
- Arb cosine evaluations at the five active prime powers.

The exact-head job found the smallest certified grid lower enclosure to be

```math
>0.23157640090649.
```

The proof gate itself requires only `>0.19`. Combining this floor with the certified Lipschitz cap gives, everywhere on the compact interval,

```math
m_1(\xi)
>
0.19-8.22\times0.01
=
0.1078.
```

Hence

```math
\boxed{m_1(\xi)>0.1\quad(1551\le|\xi|\le2500).}
```

---

## 6. Far field `[2500,infinity)` `✓[K/M]`

For `|xi|>=2500`, every positive digamma summand is increasing in `|xi|`, while each cosine is at most one. Therefore

```math
m_1(\xi)
\ge
\operatorname{Re}\psi\left(\frac14+1250i\right)
-\log\pi-2W_1
```

using the same rigorous finite-sum plus integral-tail lower bound.

The exact-head Arb value is

```math
>0.12591873862820.
```

Thus together with Section 5:

```math
\boxed{m_1(\xi)>0.1\qquad(|\xi|\ge1551).}
```

This supersedes the coarser `0.04` / `2300` high-frequency gate for the purpose of finite reduction, while the older theorem remains valid.

---

## 7. Smaller bounded-band lower operator

Set

```math
c=0.1,
\qquad
\Omega=1551,
```

and

```math
r(\xi)=(m_1(\xi)-c)\mathbf1_{[-\Omega,\Omega]}(\xi).
```

As in PR #114,

```math
q_1\succeq cI+K,
\qquad
K=P_I\mathcal F^{-1}M_r\mathcal F P_I.
```

The global lower bound `m_1>=-Gamma_1` gives the lower side of `r`. A finite-sum-plus-integral upper digamma bound at `|xi|=1551` plus the worst prime sign gives the upper side.

The exact-head Arb checker certifies

```math
\boxed{\|r\|_\infty<12.}
```

The actual certified upper-side enclosure was

```math
m_1(\xi)-0.1<11.26895516983277
\qquad(|\xi|\le1551).
```

---

## 8. KRD reduction at `c_PSWF=1551` `✓[K/M]`

For the time interval `[-1,1]`, the continuous PSWF parameter equals the band edge:

```math
c_{PSWF}=1551.
```

The exact-head gate certifies

```math
987<\frac{2c_{PSWF}}\pi<988,
```

so

```math
\lceil2c_{PSWF}/\pi\rceil=988.
```

Applying Karnik--Romberg--Davenport Corollary 3 at

```text
N=1210
```

gives the certified upper bound

```math
\boxed{
\lambda_{1210}(1551)
<1.5\times10^{-42}.
}
```

The actual exact-head enclosure was

```math
<1.468930504452317\times10^{-42}.
```

---

## 9. Explicit Schur penalty `✓[K/M]`

Use the same moment-augmented split as PR #114:

```math
R_N=
\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\}
+\operatorname{span}\{e^{x/2},e^{-x/2}\},
\qquad
T_N=R_N^\perp.
```

Then `E|T_N=0` and

```math
\|L_{RT}\|
\le\|r\|_\infty\sqrt{\lambda_N}.
```

The tail floor is

```math
\tau_N=c-(\Gamma_1+c)\lambda_N.
```

At `N=1210`, Arb certifies

```math
\tau_{1210}
>0.09999999999999999999999999999999999999998.
```

Using the conservative `||r||<12`, the Schur penalty satisfies

```math
\boxed{
\frac{\|r\|_\infty^2\lambda_{1210}}
{\tau_{1210}}
<2.2\times10^{-39}.
}
```

The actual exact-head upper enclosure is

```math
2.115259926411337\times10^{-39}.
```

---

## 10. New finite target

Choose before any resolved-space computation

```math
\boxed{\mu_R=3\times10^{-39}.}
```

Since this strictly dominates the certified Schur penalty, it is sufficient to prove

```math
\boxed{
(L_1)_{RR}\succeq3\times10^{-39}I.
}
```

The first `1210` PSWF modes split into

```text
605 even + 605 odd.
```

Moment augmentation adds at most one independent even and one independent odd vector. Thus the resolved dimension is at most

```text
1212 total = 606 even + 606 odd.
```

This improves PR #114's `1682`-dimensional `5e-36` target to a `1212`-dimensional `3e-39` target.

The threshold `3e-39` is not a measured eigenvalue and is not fitted to a resolved computation; it is chosen only to dominate the certified Schur penalty.

---

## 11. Remaining theorem

After this audit, the `a=1` canonical completion reduces to exactly one open finite statement:

```math
\boxed{
(L_1)_{RR}\succeq3\times10^{-39}I
\quad\text{on }R_{1210}.
}
```

No separate infinite-dimensional tail theorem or resolved--tail crossblock estimate remains.

---

## 12. Status

```text
exact a=1 Fourier multiplier                          ✓[M]
Omega=1551 global high-frequency floor m_1>0.1       ✓[K/M]
rigorous Lipschitz/grid certificate                   ✓[K/M]
||r||_infty<12 on reduced band                       ✓[K/M]
KRD lambda_1210(c=1551)<1.5e-42                      ✓[K/M]
tau_1210>0.099                                       ✓[K/M]
Schur penalty <2.2e-39                               ✓[K/M]
1212-dimensional resolved reduction                  ✓[K/M]
resolved lower bound >=3e-39                         ?[O]
certified a=1 completion                             ?[O]
all-a NP-GAP / Object X / RH                         ?[O]
```

Registry and Object-X working definition remain unchanged.

## 13. Firewalls

Do not claim:

- the resolved lower bound has been proved;
- `3e-39` is an observed or fitted eigenvalue;
- the older `2300/1680` certificate was wrong (it remains valid but coarser);
- fixed-window `a=1`, all-window NP-GAP, Object X, or RH is solved.
