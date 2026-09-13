# P11 NP-GAP — Q0 first-channel intertwining and unconditional short-window gap

**Date:** 2026-09-13  
**Status:** theorem-level project audit; no Registry promotion.  
**Parent:** PR #107 / COMMON-JUMP exact Prime–archimedean jump-Gram geometry.  

## 1. Purpose

PR #107 reduced the null-pole Weil form to

```math
Q_W(v,w)=\langle \mathcal X_av,\mathcal X_aw\rangle-\Gamma_a\langle v,w\rangle
```

on

```math
\mathscr D_{NP}(a)
=\{v\in C_c^\infty(-a,a):E_+(v)=E_-(v)=0\}.
```

The remaining problem is the sharp lower-frame inequality. This audit proves two unconditional structural facts:

1. the first archimedean resolvent channel `alpha_0=1/2` is exactly intertwined with the support-preserving null-pole operator
   `Q_0=-d^2/dx^2+1/4`;
2. the resulting local coercivity plus elementary bounds for all higher archimedean channels proves NP-GAP on a nonempty interval of sufficiently short windows.

No statement for all `a>0` is made.

---

## 2. Setup

Let `T_t` be the unitary translation group on `L^2(R)` and

```math
K_t:=T_{t/2}-T_{-t/2}.
```

Write

```math
L:=-\partial_x^2\ge0,
\qquad
Q_0:=L+\frac14.
```

The archimedean density from COMMON-JUMP is

```math
h(t)=\frac{e^{-t/2}}{1-e^{-2t}}
=\sum_{m=0}^\infty e^{-\alpha_m t},
\qquad
\alpha_m:=2m+\frac12.
```

For `alpha>0` define the positive bounded channel operator

```math
A_\alpha
:=\int_0^\infty e^{-\alpha t}K_t^*K_t\,dt.
```

Then the full archimedean jump operator is the positive quadratic-form sum

```math
A_\infty=\sum_{m=0}^\infty A_{\alpha_m}.
```

---

## 3. Exact Fourier multiplier of one channel `✓[M]`

Since

```math
K_t^*K_t=2I-T_t-T_{-t},
```

its Fourier multiplier is

```math
4\sin^2(\xi t/2)=2-2\cos(\xi t).
```

Therefore

```math
\begin{aligned}
\widehat A_\alpha(\xi)
&=\int_0^\infty e^{-\alpha t}(2-2\cos(\xi t))\,dt\\
&=\frac{2\xi^2}{\alpha(\xi^2+\alpha^2)}.
\end{aligned}
```

Equivalently,

```math
\boxed{
A_\alpha
=\frac{2}{\alpha}
L(L+\alpha^2)^{-1}.
}
```

This is an exact positive-resolvent representation of every archimedean channel.

---

## 4. First-channel cancellation with the null-pole operator `✓[M]`

For the first channel `alpha_0=1/2`,

```math
A_{1/2}
=4L(L+1/4)^{-1}
=4I-Q_0^{-1}.
```

Hence on `C_c^\infty(R)`,

```math
\boxed{
A_{1/2}Q_0
=4L
=-4\partial_x^2.
}
```

This is the explicit intertwining/factorization identity that was previously only a structural hint.

### Uniqueness of the cancellation

For general `alpha>0`,

```math
A_\alpha Q_0
=\frac{2}{\alpha}L(L+1/4)(L+\alpha^2)^{-1}.
```

The resolvent denominator cancels as a polynomial in `L` only when

```math
\alpha^2=\frac14,
```

hence only for `alpha=1/2` among positive channels.

Therefore the first Gamma/Digamma channel is genuinely distinguished by the null-pole operator; this is not merely a numerical scale coincidence.

---

## 5. Support-preserving null-pole parametrization `✓[M]`

The Green kernel of `Q_0^{-1}` on the line is

```math
G_0(x)=e^{-|x|/2},
```

so

```math
(Q_0^{-1}v)(x)
=\int_{\mathbb R}e^{-|x-y|/2}v(y)\,dy.
```

Assume `supp(v) subset (-a,a)`. For `x>a`,

```math
(Q_0^{-1}v)(x)
=e^{-x/2}\int e^{y/2}v(y)\,dy
=e^{-x/2}E_+(v).
```

For `x<-a`,

```math
(Q_0^{-1}v)(x)
=e^{x/2}\int e^{-y/2}v(y)\,dy
=e^{x/2}E_-(v).
```

Thus if `v` is null-pole, both tails vanish and `u:=Q_0^{-1}v` has the same compact-support window.

Conversely, if `u in C_c^\infty(-a,a)` and `v=Q_0u`, integration by parts against the two homogeneous solutions `e^{\pm x/2}` gives

```math
E_+(v)=E_-(v)=0.
```

Since `Q_0` has no nonzero compactly supported kernel,

```math
\boxed{
Q_0:C_c^\infty(-a,a)
\xrightarrow{\cong}
\mathscr D_{NP}(a)
}
```

is a support-preserving bijection.

This gives a direct proof of the local null-pole parametrization needed here; no RH input is used.

---

## 6. First-channel local Sobolev energy `✓[M]`

Write `v=Q_0u` with `u in C_c^\infty(-a,a)`. Then

```math
\begin{aligned}
\langle v,A_{1/2}v\rangle
&=\langle Q_0u,4Lu\rangle\\
&=4\|u''\|_2^2+\|u'\|_2^2.
\end{aligned}
```

Hence

```math
\boxed{
\int_0^\infty e^{-t/2}\|K_tv\|_2^2\,dt
=4\|u''\|_2^2+\|u'\|_2^2.
}
```

The first nonlocal jump channel becomes an exactly local Sobolev energy after null-pole factorization.

---

## 7. Quantitative first-channel coercivity `✓[M]`

Let

```math
\lambda_1(a)=\frac{\pi^2}{4a^2}
```

be the first Dirichlet eigenvalue of `L=-d^2/dx^2` on `(-a,a)`.

Expanding `u` in the Dirichlet eigenbasis gives

```math
\frac{\langle v,A_{1/2}v\rangle}{\|v\|_2^2}
=\frac{\sum_k4\lambda_k(\lambda_k+1/4)|u_k|^2}
       {\sum_k(\lambda_k+1/4)^2|u_k|^2}.
```

Since

```math
\lambda\mapsto\frac{4\lambda}{\lambda+1/4}
```

is increasing and `lambda_k >= lambda_1(a)`, one obtains

```math
\boxed{
\langle v,A_{1/2}v\rangle
\ge
\frac{4\pi^2}{\pi^2+a^2}\,\|v\|_2^2,
\qquad v\in\mathscr D_{NP}(a).
}
```

This is a genuine null-pole improvement; it uses support preservation of `Q_0^{-1}`.

---

## 8. Higher-channel support bound `✓[M]`

For arbitrary `alpha>0`,

```math
A_\alpha
=\frac{2}{\alpha}\bigl(I-\alpha^2(L+\alpha^2)^{-1}\bigr).
```

The resolvent kernel is

```math
R_\alpha(x,y)
=\frac{1}{2\alpha}e^{-\alpha|x-y|}.
```

Compress it to `I_a=(-a,a)`. By the Schur test,

```math
\|1_{I_a}R_\alpha1_{I_a}\|
\le
\sup_{|x|<a}
\int_{-a}^a\frac{e^{-\alpha|x-y|}}{2\alpha}\,dy
=\frac{1-e^{-\alpha a}}{\alpha^2}.
```

Therefore every `v` supported in `(-a,a)` satisfies

```math
\boxed{
\langle v,A_\alpha v\rangle
\ge
\frac{2}{\alpha}e^{-\alpha a}\|v\|_2^2.
}
```

No null-pole condition is required for this estimate.

---

## 9. A rigorous short-window NP-GAP theorem `✓[M]_part`

Define

```math
B(a)
:=
\frac{4\pi^2}{\pi^2+a^2}
+
\sum_{m=1}^\infty
\frac{2}{\alpha_m}e^{-\alpha_m a},
\qquad
\alpha_m=2m+\frac12.
```

Equivalently,

```math
B(a)
=
\frac{4\pi^2}{\pi^2+a^2}
+e^{-a/2}
\left[
\Phi(e^{-2a},1,1/4)-4
\right],
```

where `Phi` is the Lerch transcendent.

By Sections 7 and 8,

```math
\boxed{
\langle v,A_\infty v\rangle
\ge B(a)\|v\|_2^2
\qquad
(v\in\mathscr D_{NP}(a)).
}
```

The function `B(a)` is continuous and strictly decreasing on `(0,infinity)`, with

```math
\lim_{a\downarrow0}B(a)=+\infty,
\qquad
\lim_{a\to\infty}B(a)=0.
```

Let `a_*` be the unique positive solution of

```math
B(a_*)=\kappa_* ,
\qquad
\kappa_*=\log\pi-\psi(1/4)
=\log(8\pi)+\gamma+\pi/2.
```

For

```math
0<a<\min\{a_*,\tfrac12\log2\},
```

there are no prime-power atoms in the canonical cutoff `log n <= 2a`, so

```math
\Gamma_a=\kappa_*.
```

Hence

```math
\boxed{
\|\mathcal X_av\|_2^2
\ge\Gamma_a\|v\|_2^2
\quad
\text{for every }v\in\mathscr D_{NP}(a)
}
```

throughout this nonempty short-window interval.

Equivalently,

```math
\boxed{
Q_W(v)\ge0
\quad
\text{on }\mathscr D_{NP}(a)
\text{ for all sufficiently small }a>0.
}
```

This is an unconditional partial NP-GAP theorem.

### Scope firewall

This proves only a proper short-window range. It does **not** prove the required inequality for all `a>0`, and therefore does not prove RH.

No numerical approximation to `a_*` is needed for the theorem and none is promoted here.

---

## 10. Relation to the external review correction

The external counter-audit correctly noted that the earlier phrase “the null-pole conditions hit the first resolvent channel” was only a structural hint without an explicit operator identity.

That gap is now closed by

```math
\boxed{A_{1/2}Q_0=4L.}
```

It also correctly noted that finite-dimensional Ritz minima are upper bounds for the true infimum. No finite-dimensional positive Ritz gap is used anywhere in this proof.

Thus this audit is independent of the non-certified Galerkin diagnostics reported during exploration.

---

## 11. Status

```text
COMMON-JUMP architecture                               ✓[M] imported from #107
single-channel resolvent formula A_alpha               ✓[M]
Q0 support-preserving null-pole bijection              ✓[M]
A_{1/2} Q0 = -4 d^2/dx^2                              ✓[M]
uniqueness of alpha=1/2 channel cancellation           ✓[M]
first-channel local Sobolev identity                   ✓[M]
first-channel quantitative coercivity                  ✓[M]
higher-channel Schur lower bound                       ✓[M]
NP-GAP on a nonempty sufficiently-short-window range   ✓[M]_part
NP-GAP for every a>0                                   ?[O]
full positive Object-X realization                     ?[O]
publication novelty                                    ?[O]
RH                                                     ?[O]
```

Registry unchanged.