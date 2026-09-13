# P11 NP-DISCREPANCY — pole-cleared Prime discrepancy and null-pole correlation gauge

**Date:** 2026-09-13  
**Status:** theorem-level project audit; no Registry promotion.  
**Parent:** PR #109 / centered Prime-overlap and exact per-prime AR(1) fibers.

## 1. Purpose

PR #109 reduced the null-pole Weil form to the centered overlap problem

```math
Q_W(v)=\mathcal A(v)-\mathcal O_a(v),
```

where

```math
\mathcal A(v)
:=\int_0^\infty h(t)\|K_tv\|_2^2dt-\kappa_*\|v\|_2^2,
\qquad
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},
```

and

```math
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
```

This audit does four things:

1. closes a precise method-class No-Go for independent shift/block norm summation;
2. derives an exact null-pole autocorrelation gauge;
3. uses that gauge to replace the exponentially large raw Prime measure by a pole-cleared discrepancy measure;
4. identifies the Laplace transform of that discrepancy with the pole-cleared logarithmic derivative of zeta.

The all-`a` positivity problem remains open.

---

## 2. Independent per-shift scalar domination is exponentially off-scale `×[M]`

Let

```math
S_t:=\frac{T_t+T_{-t}}2
```

compressed to `L^2(-a,a)`. PR #109 proves

```math
\|S_t\|
=\cos\frac{\pi}{\lceil2a/t\rceil+1},
\qquad 0<t<2a.
```

Define the independent-shift norm budget

```math
U_{\rm sep}(a)
:=2\sum_{\log n<2a}
\frac{\Lambda(n)}{\sqrt n}\,\|S_{\log n}\|.
```

If

```math
a<\log n<2a,
```

then `ceil(2a/log n)=2`, hence

```math
\|S_{\log n}\|=\cos(\pi/3)=\frac12.
```

Therefore

```math
U_{\rm sep}(a)
\ge
\sum_{e^a<n<e^{2a}}
\frac{\Lambda(n)}{\sqrt n}.
```

By the prime number theorem and partial summation,

```math
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
=2\sqrt X\,(1+o(1)),
```

so

```math
\boxed{
U_{\rm sep}(a)\ge 2e^a(1+o(1)).
}
```

Now let

```math
\lambda_{\mathcal A}(a)
:=
\inf_{0\ne v\in\mathscr D_{NP}(a)}
\frac{\mathcal A(v)}{\|v\|_2^2}.
```

For any fixed `a_0>0`, choose one nonzero `v_0 in D_NP(a_0)`. Since the admissible spaces increase with `a`,

```math
\lambda_{\mathcal A}(a)
\le
\frac{\mathcal A(v_0)}{\|v_0\|_2^2}
=:C_0
\qquad(a\ge a_0).
```

Hence every scalar lower bound

```math
\mathcal A\succeq L(a)I
```

must satisfy `L(a)<=C_0` for all large `a`, while the independent-shift upper budget grows at least like `2e^a`.

Therefore the proof architecture

```text
archimedean scalar lower bound
+
independent per-shift (or independent near-boundary per-prime-block) norm summation
```

cannot prove the all-window inequality for large `a`.

This is a method-class No-Go, not a statement that collective Prime interference cannot work.

---

## 3. Constant-factor Prolate concentration is not a sufficient suppression mechanism `×[M]`

The Fourier multiplier of the Prime overlap is

```math
\Phi_a(\xi)
:=2\sum_{\log n<2a}
\frac{\Lambda(n)}{\sqrt n}
\cos(\xi\log n).
```

All terms are simultaneously positive on the universal band

```math
|\xi|<\frac{\pi}{4a}.
```

A time-limited function on `[-a,a]` can place at most a fixed, `a`-independent fraction of its Fourier energy in such a `1/a`-scale band; the elementary trace bound for the corresponding Prolate concentration operator is constant under scaling (for the above band, at most `1/2`).

However a constant-factor concentration estimate, when combined only with the raw amplitude of `Phi_a`, still produces an exponentially large scalar budget because

```math
\Phi_a(0)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\sim 4e^a.
```

Thus a proof that uses Prolate only as an `a`-independent concentration constant cannot by itself close all-`a` NP-OVERLAP.

This does **not** rule out Prolate/Paley-Wiener input after a sharper arithmetic centering. It rules out the raw-amplitude × constant-concentration mechanism.

---

## 4. Null-pole autocorrelation identity `✓[M]`

For `v in C_c^\infty(-a,a)` define

```math
C_v(t):=\langle T_t v,v\rangle.
```

With the convention `T_t v(x)=v(x-t)`, Fubini gives

```math
\int_{-\infty}^{\infty}
e^{t/2}C_v(t)\,dt
=
E_-(v)\,\overline{E_+(v)}.
```

On the null-pole class

```math
E_+(v)=E_-(v)=0,
```

hence

```math
\int_{\mathbb R}e^{t/2}C_v(t)dt=0.
```

Since

```math
C_v(-t)=\overline{C_v(t)},
```

taking real parts yields

```math
\boxed{
\int_0^{2a}
2\cosh(t/2)\,
\operatorname{Re}C_v(t)\,dt
=0.
}
```

This is an exact null-pole correlation constraint. It is stronger for the present purpose than a raw time-frequency concentration bound because it permits a nontrivial change of the arithmetic sampling measure without changing the quadratic form on `D_NP(a)`.

---

## 5. Pole-cleared Prime discrepancy measure `✓[M]`

Define the positive Prime-power measure on `(0,infinity)`

```math
d\nu(t)
:=
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}\,
\delta_{\log n}(dt).
```

Define its null-pole-centered discrepancy measure

```math
\boxed{
d\mathfrak D(t)
:=d\nu(t)-2\cosh(t/2)\,dt.
}
```

Because `Re C_v(t)=0` for `t>=2a` and Section 4 gives zero pairing with `2 cosh(t/2)dt`, the overlap satisfies the exact all-window identity

```math
\boxed{
\mathcal O_a(v)
=
2\int_0^\infty
\operatorname{Re}C_v(t)\,d\mathfrak D(t),
\qquad
v\in\mathscr D_{NP}(a).
}
```

Thus the exponentially large smooth Prime main density can be subtracted **exactly on the admissible class** rather than estimated.

The cumulative discrepancy is

```math
\boxed{
\mathfrak D(T)
:=
\sum_{\log n\le T}
\frac{\Lambda(n)}{\sqrt n}
-4\sinh(T/2).
}
```

By the prime number theorem,

```math
\sum_{\log n\le T}
\frac{\Lambda(n)}{\sqrt n}
=2e^{T/2}+o(e^{T/2}),
```

while

```math
4\sinh(T/2)=2e^{T/2}-2e^{-T/2}.
```

Hence

```math
\boxed{
\mathfrak D(T)=o(e^{T/2}).
}
```

The leading exponential Prime mass is removed at the level of an exact null-pole identity.

---

## 6. Exact Stieltjes integration-by-parts form `✓[M]`

For compact support in `(-a,a)`,

```math
C_v(2a)=0,
\qquad
\mathfrak D(0)=0.
```

Since `C_v` is smooth, Stieltjes integration by parts gives

```math
\boxed{
\mathcal O_a(v)
=
-2\int_0^{2a}
\mathfrak D(t)\,
\frac{d}{dt}\operatorname{Re}C_v(t)\,dt.
}
```

This separates the all-window problem into

```text
arithmetic object:   cumulative pole-cleared Prime discrepancy D(t)
analytic object:     derivative of a compactly supported positive-definite autocorrelation
```

without any RH assumption.

---

## 7. Laplace transform = pole-cleared logarithmic derivative of zeta `✓[M]`

For `Re(s)>1/2`,

```math
\int_0^\infty e^{-st}\,d\nu(t)
=
\sum_{n\ge2}\frac{\Lambda(n)}{n^{s+1/2}}
=
-\frac{\zeta'}{\zeta}\left(s+\frac12\right).
```

Also

```math
\int_0^\infty e^{-st}2\cosh(t/2)dt
=
\frac1{s-1/2}+\frac1{s+1/2}.
```

Therefore

```math
\boxed{
\int_0^\infty e^{-st}\,d\mathfrak D(t)
=
-\frac{\zeta'}{\zeta}\left(s+\frac12\right)
-\frac1{s-1/2}
-\frac1{s+1/2}.
}
```

Equivalently,

```math
\boxed{
\mathcal L[d\mathfrak D](s)
=
-\frac{d}{ds}
\log\left[(s^2-1/4)\zeta(s+1/2)\right].
}
```

Thus the null-pole correlation gauge removes **exactly the zeta pole at `1` and the symmetric pole factor at `0`** from the finite-place logarithmic derivative.

Writing `z=s+1/2` and using

```math
\xi(z)=z(z-1)\pi^{-z/2}\Gamma(z/2)\zeta(z),
```

one may also write

```math
\boxed{
\mathcal L[d\mathfrak D](s)
=
-\frac{\xi'}{\xi}(z)
-\frac12\log\pi
+\frac12\psi(z/2),
\qquad z=s+1/2.
}
```

No zero information is assumed; this is an identity in the half-plane of absolute convergence.

---

## 8. Polynomial discrepancy growth is RH-hard `✓[K/M]`

Let

```math
S(x):=\sum_{n\le x}\frac{\Lambda(n)}{\sqrt n}.
```

Then

```math
\mathfrak D(\log x)
=S(x)-2\sqrt x+2x^{-1/2}.
```

Under RH the classical estimate

```math
\psi(x)=x+O(\sqrt x\log^2x)
```

and partial summation imply

```math
S(x)=2\sqrt x+O(\log^3x),
```

hence

```math
\boxed{
RH\Longrightarrow\mathfrak D(T)=O(T^3).
}
```

Conversely, if for some fixed `K`

```math
\mathfrak D(T)=O(T^K),
```

then

```math
S(x)=2\sqrt x+O((\log x)^K).
```

Stieltjes inversion

```math
\psi(x)
=\sqrt x\,S(x)
-\frac12\int_1^x u^{-1/2}S(u)du
```

then gives

```math
\psi(x)=x+O(\sqrt x(\log x)^K),
```

which excludes every zeta zero with real part greater than `1/2` and therefore implies RH.

Hence polynomial control of `D(T)` is already RH-hard. The new reduction does not make the final theorem easy; it identifies the correct arithmetic fluctuation after the null-pole main term has been removed.

---

## 9. New default front — NP-DISCREPANCY / NP-CORR

The all-window problem remains

```math
\mathcal A(v)\ge\mathcal O_a(v).
```

The preferred exact form is now

```math
\boxed{
\mathcal A(v)
\ge
-2\int_0^{2a}
\mathfrak D(t)\,
\frac{d}{dt}\operatorname{Re}C_v(t)dt,
\qquad
v\in\mathscr D_{NP}(a).
}
```

This replaces the raw exponentially large Prime measure by the pole-cleared discrepancy `D`.

Next admissible mechanisms must exploit at least one of:

1. cancellation/sign structure of `D(t)` rather than `|D(t)|`;
2. positive-definiteness and support constraints of `C_v`;
3. the exact `Q_0` parametrization of `D_NP(a)`;
4. the per-prime AR(1) fibers as a local decomposition of the same discrepancy;
5. a Toeplitz/Paley-Wiener mechanism acting on the **centered discrepancy**, not on the raw Prime amplitude.

A mere constant-factor improvement of the Prolate concentration estimate is not a main-front mechanism.

---

## 10. Status

```text
COMMON-JUMP architecture                                      ✓[M]
centered Prime-overlap decomposition                          ✓[M]
exact per-prime AR(1) fiberization                            ✓[M]
independent shift/block scalar norm-sum route                 ×[M]
raw-amplitude × constant-Prolate route                        ×[M]
null-pole autocorrelation cosh identity                       ✓[M]
pole-cleared Prime discrepancy measure                        ✓[M]
Stieltjes discrepancy-correlation identity                    ✓[M]
Laplace transform / pole-cleared zeta log derivative          ✓[M]
polynomial discrepancy growth as RH-equivalent scale          ✓[K/M]
NP-DISCREPANCY / anti-correlation domination                  ?[O]
all-a NP-GAP / full positive Object X / RH                    ?[O]
```

Registry and Object-X working definition remain unchanged.
