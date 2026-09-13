# P11 NP-GAP — review correction, certified short-window threshold, and Prime-overlap front

**Date:** 2026-09-13  
**Status:** theorem-level project correction/addendum; no Registry promotion.  
**Parents:** PR #107 COMMON-JUMP; PR #108 Q0 first-channel / short-window coercivity.

## 1. Purpose

This addendum incorporates the external review of PR #108 and separates three issues that must not be conflated:

1. the mathematics of the `Q_0`/first-channel intertwining;
2. the novelty/status of the resulting short-window positivity statement;
3. the actual all-window obstruction after COMMON-JUMP centering.

The first survives unchanged.  The second is corrected.  The third becomes the new default front.

---

## 2. `e^{-alpha a}` higher-channel bound is rigorously valid `✓[M]`

For

```math
A_\alpha
=\frac{2}{\alpha}\left(I-\alpha^2R_\alpha\right),
\qquad
R_\alpha=(-\partial_x^2+\alpha^2)^{-1},
```

the whole-line resolvent kernel is

```math
R_\alpha(x,y)=\frac{1}{2\alpha}e^{-\alpha|x-y|}.
```

Compress to `I_a=(-a,a)`.  The Schur row integral is maximal at `x=0` and equals

```math
\sup_{|x|<a}\int_{-a}^a\frac{e^{-\alpha|x-y|}}{2\alpha}\,dy
=\frac{1-e^{-\alpha a}}{\alpha^2}.
```

Therefore

```math
\|1_{I_a}R_\alpha1_{I_a}\|
\le \frac{1-e^{-\alpha a}}{\alpha^2}
```

and hence, for every `v` supported in `(-a,a)`,

```math
\boxed{
\langle v,A_\alpha v\rangle
\ge \frac{2}{\alpha}e^{-\alpha a}\|v\|_2^2.
}
```

Thus the weaker elementary `e^{-2\alpha a}` estimate is unnecessary.  The PR #108 exponent is mathematically justified.

---

## 3. Short-window novelty correction

The short-window positivity consequence from PR #108 is **not a new theorem about the Weil form in the absolute literature sense**.

Suzuki, Theorem 1.4 in *Weil's quadratic form via the screw function* (2026), proves unconditionally that for sufficiently small `a>0` the lowest eigenvalue of the localized Weil operator is positive (indeed positive and simple), with the asymptotic

```math
\lambda_a
=\log(1/a)+\mu_1-\log(2\pi)+\psi(2)-1+O(a).
```

This theorem is on the full local class, so it is stronger than positivity restricted to `D_NP(a)`.

### Correct project booking

```text
short-window positivity as a new Weil-form theorem        ×[M]
COMMON-JUMP/Q0 internal derivation of short-window gap     ✓[M]_part
Q0/first-channel intertwining itself                       ✓[M]
```

The value of PR #108 is therefore structural: it derives a known qualitative small-window positivity phenomenon **inside the new COMMON-JUMP architecture**, rather than importing the positivity theorem as an input.

No claim of publication novelty is made.

---

## 4. Closed form of the PR #108 lower bound

Let

```math
\alpha_m=2m+\frac12,
\qquad
x=e^{-a/2}.
```

The higher-channel series in PR #108 satisfies

```math
\sum_{m=1}^\infty\frac{2}{\alpha_m}e^{-\alpha_ma}
=\log\frac{1+x}{1-x}+2\arctan x-4x.
```

Hence

```math
\boxed{
B(a)
=\frac{4\pi^2}{\pi^2+a^2}
+\log\frac{1+e^{-a/2}}{1-e^{-a/2}}
+2\arctan(e^{-a/2})
-4e^{-a/2}.
}
```

In particular,

```math
B(a)=\log(1/a)+O(1)
\qquad(a\downarrow0),
```

which reproduces the leading logarithmic scale in Suzuki's small-window theorem.  This is a consistency statement about the architecture, not a novelty claim.

`B(a)` is strictly decreasing, so the equation

```math
B(a_*)=\kappa_*,
\qquad
\kappa_*=\log(8\pi)+\gamma+\pi/2,
```

has a unique positive solution.

---

## 5. Arb certificate for `a_*`

The new exact-head script

```text
scripts/check_np_gap_short_window_arb.py
```

uses Arb arithmetic and a rigorous positive geometric tail enclosure for the infinite higher-channel sum.  The associated workflow is

```text
.github/workflows/np-gap-short-window-arb.yml
```

and certifies

```math
\boxed{
0.1033784517534<a_*<0.1033784517535.
}
```

It also certifies

```math
\boxed{a_*<\frac12\log2.}
```

Consequently the formal minimum in PR #108 can be sharpened to the actual short-window range

```math
\boxed{0<a\le a_*}
```

(the endpoint is allowed because the target inequality is non-strict).

The certificate is numerical only for the decimal enclosure of `a_*`; the existence, uniqueness, and short-window theorem are analytic.

---

## 6. Exact centered Prime-overlap decomposition `✓[M]`

COMMON-JUMP gives on the null-pole class

```math
Q_W(v)
=\|X_av\|^2-\Gamma_a\|v\|^2.
```

For `t>0`,

```math
\|K_tv\|^2
=2\|v\|^2-2\operatorname{Re}\langle T_tv,v\rangle.
```

Write

```math
\mathcal A(v)
:=\int_0^\infty h(t)\|K_tv\|^2dt-\kappa_*\|v\|^2,
```

with

```math
h(t)=\frac{e^{-t/2}}{1-e^{-2t}}.
```

Then the Prime diagonal part cancels **exactly** against the Prime part of `Gamma_a`, leaving

```math
\boxed{
Q_W(v)
=\mathcal A(v)-\mathcal O_a(v),
\qquad v\in D_{NP}(a),
}
```

where

```math
\boxed{
\mathcal O_a(v)
:=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
}
```

For `log n>=2a` the shifted supports are disjoint and the correlation is zero, so there is no outer contribution to `O_a`.

Equivalently, with

```math
S_t:=\frac12(T_t+T_{-t}),
```

compressed to `L^2(-a,a)`, define the Hermitian finite overlap operator

```math
\boxed{
\mathbf O_a
:=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}S_{\log n}.
}
```

Then all-`a` NP-GAP is exactly the operator domination problem

```math
\boxed{
(A_\infty-\kappa_*I)|_{D_{NP}(a)}
\succeq
\mathbf O_a|_{D_{NP}(a)}.
}
```

This is the new canonical form of the hard remainder.

### Strategic interpretation

The exponentially large Prime diagonal ledger is **not** itself the obstruction; it cancels in the centered form.  The only arithmetic defect that remains is the weighted overlap/correlation of the finitely many shifts with `log n<2a`.

Thus the next proof attempt must attack the overlap operator rather than seek additional scalar mass.

---

## 7. `Q_0`-transport of the Prime overlap `✓[M]`

For `v=Q_0u`, `Q_0=-\partial_x^2+1/4`, translation commutes with `Q_0`.  Integration by parts gives, for every `t>0`,

```math
\boxed{
\operatorname{Re}\langle T_tv,v\rangle
=
\operatorname{Re}\langle T_tu'',u''\rangle
+\frac12\operatorname{Re}\langle T_tu',u'\rangle
+\frac1{16}\operatorname{Re}\langle T_tu,u\rangle.
}
```

Hence the Prime-overlap operator on `D_NP(a)` transports to a finite weighted sum of ordinary overlap correlations at Sobolev levels `0,1,2` on `C_c^\infty(-a,a)`.

This is an exact reformulation, not yet a domination theorem.  It identifies the natural next analytic target: control the positive spectral part of these shifted-overlap correlations by the archimedean COMMON-JUMP surplus.

---

## 8. Multi-null Gamma ladder — exact but auxiliary

For

```math
\alpha_m=2m+\frac12,
\qquad
Q_m=-\partial_x^2+\alpha_m^2,
```

one has

```math
M(Q_mu)(s)
=\left(\alpha_m^2-(s-1/2)^2\right)M(u)(s).
```

Thus `Q_m` imposes zeros at

```math
s=\frac12\pm\alpha_m=-2m,\ 2m+1.
```

For each fixed `N`, the finite set

```math
F_N=\{-2m,2m+1:0\le m<N\}
```

contains `{0,1}` and is disjoint from the **non-trivial** zeta-zero set.  The negative even points are trivial zeta zeros; this does not violate Connes--Consani Proposition C.1, whose excluded set is the non-trivial zero set.

Therefore the corresponding finite-null global Weil criterion remains RH-equivalent.

This makes the finite Gamma-channel ladder a legitimate auxiliary theorem direction, but it is **not** the new default coercivity front: it does not change the Prime-overlap operator and therefore attacks the secondary, archimedean side of the all-window inequality.

---

## 9. New default front — NP-OVERLAP

The main question is now

```math
\boxed{
\mathcal A(v)\ge\mathcal O_a(v)
\quad
\forall v\in D_{NP}(a),\ \forall a>0.
}
```

Priority order:

1. spectral structure of the finite Hermitian overlap operator `O_a` on `D_NP(a)`;
2. exact `Q_0`-transport and parity decomposition;
3. sharp support/overlap inequalities as `t` approaches `2a`;
4. interaction with the Prime-power AR(1)/Weil-tail structure already proved elsewhere in the program;
5. only then revisit multi-null Gamma ladders if they give a quantitative bound on `O_a` rather than merely a better archimedean lower bound.

A proof of the domination for all `a` remains RH-hard.

---

## 10. Corrected status

```text
COMMON-JUMP architecture                                  ✓[M]
A_alpha resolvent form                                    ✓[M]
e^{-alpha a} Schur lower bound                            ✓[M]
Q0 first-channel intertwining                             ✓[M]
Q0 support-preserving null-pole bijection                 ✓[M]
short-window coercivity derived inside COMMON-JUMP        ✓[M]_part
short-window positivity as a new literature theorem       ×[M]
Arb bracket for a_*                                       ✓[K/M] numerical certificate
exact centered Prime-overlap decomposition                ✓[M]
Q0 Sobolev transport of Prime overlaps                    ✓[M]
finite multi-null Gamma ladder                            ✓[M] structural / auxiliary
all-a NP-OVERLAP domination                               ?[O]
full positive Object-X realization                        ?[O]
publication novelty of COMMON-JUMP/Q0 architecture        ?[O]
RH                                                        ?[O]
```

Registry and Object-X working definition remain unchanged.
