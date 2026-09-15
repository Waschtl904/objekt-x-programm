# P11 Audit — NULLPOL prime-discrepancy cancellation and OU root-trace bridge

**Datum:** 15. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** theorem-level Umformung der NULLPOL-Weilform nach dem Hard Audit.  
**Registry:** unverändert.  
**Nonclaim:** kein Positivitäts-, Object-X-, RH- oder Publikationsneuheitsclaim.

---

## 0. Kurzurteil

Auf NULLPOL kann der exponentiell wachsende glatte Hauptterm der Prime-Power-Maßes **exakt** gegen den Grundmodus `mu_0=1/2` der Gamma-/Green-Schicht eliminiert werden.

Definiere die lokal endliche Prime-Power-Maßstruktur

```math
\nu_P
:=
\sum_{n=p^k\ge2}
\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}
```

und ihre polbereinigte Diskrepanz

```math
\boxed{
\Delta
:=
\nu_P-e^{t/2}\,dt.
}
```

Weiter setze

```math
h_1(t)
:=
h(t)-e^{-t/2}
=
\frac{e^{-5t/2}}{1-e^{-2t}}.
```

Dann gilt fuer jede kompakt getragene NULLPOL-Testfunktion `v` exakt

```math
\boxed{
Q_W(v)
=
\int_0^\infty h_1(t)\|K_tv\|_2^2dt
-(\kappa_*-4)\|v\|_2^2
-
\int_0^\infty
\bigl(f_v(t)+f_v(-t)\bigr)\,d\Delta(t),
}
```

wobei

```math
f_v=v*\widetilde v,
\qquad
K_t=T_{t/2}-T_{-t/2}.
```

Die Darstellung ist **fensterfrei**: fuer kompakt getragenes `v` ist der atomare Anteil automatisch lokal endlich. Der wachsende Fenster-Skalar

```math
2\sum_{\log n\le2a}\Lambda(n)/\sqrt n
```

tritt nicht mehr auf. Die gesamte radiusabhaengige arithmetische Schwierigkeit sitzt stattdessen in der signierten Diskrepanz `Delta`.

Zusaetzlich besitzt `Delta` eine exakte OU-/P11-Rootspurinterpretation. In der normierten OU-Familie mit Rootkorrelation `e^{-sigma t}` gilt fuer `sigma>1/4`

```math
\boxed{
\operatorname{tr}H_{P}^{(\sigma)}
-
\operatorname{tr}H_{0}^{(\sigma)}
=
-\frac{\zeta'}{\zeta}\left(\frac12+2\sigma\right)
-
\frac1{2\sigma-1/2}
=
\mathcal L\Delta(2\sigma).
}
```

Bei der P11-/Critical-half-Skala `sigma=1/2` ist dies

```math
-\zeta'/\zeta(3/2)-2.
```

Das ist eine exakte Bruecke zwischen dem P11-Root und der neuen Diskrepanznormalform. Sie ist **noch keine positive Differenz- oder Schur-Komplement-Realisierung**.

Status:

```text
NULLPOL growing/decaying correlation identity            ✓[M]
prime-main / Gamma-ground cancellation                    ✓[M]
window-free discrepancy normal form                       ✓[M]
Laplace transform of Delta                                ✓[M]
OU/P11 root-trace identity for Delta                      ✓[M]
polynomial cumulative Delta bound <=> RH-scale PNT error  ✓[M] (standard equivalence route)
positive Schur/dilation realization of Delta              ?[O]
full Object X / RH                                        ?[O]
publication novelty                                       ?[O]
```

---

# 1. Starting point: the additive explicit formula

Use the same normalization as `P11_NP_COMMON_JUMP_GRAM_2026-09-13.md`.
For

```math
f_v=v*\widetilde v,
\qquad
\widetilde v(x)=\overline{v(-x)},
```

write

```math
F_v(t):=f_v(t)+f_v(-t).
```

The explicit formula reads

```math
\begin{aligned}
Q_W(v)
={}&
\int_{\mathbb R}f_v(x)(e^{x/2}+e^{-x/2})dx\\
&-
\int_0^\infty F_v(t)\,d\nu_P(t)\\
&-(\log4\pi+\gamma)f_v(0)\\
&-
\int_0^\infty
\{F_v(t)-2e^{-t/2}f_v(0)\}h(t)dt,
\end{aligned}
```

where

```math
h(t)=\frac{e^{-t/2}}{1-e^{-2t}}.
```

For compactly supported `v`, the `nu_P` integral is a finite sum.

---

# 2. NULLPOL turns the growing exponential correlation into the decaying one

Define

```math
E_+(v)=\int e^{x/2}v(x)dx,
\qquad
E_-(v)=\int e^{-x/2}v(x)dx.
```

On NULLPOL,

```math
E_+(v)=E_-(v)=0.
```

By Fubini,

```math
\int_{\mathbb R}f_v(t)e^{t/2}dt
=E_+(v)\overline{E_-(v)}=0,
```

and similarly

```math
\int_{\mathbb R}f_v(t)e^{-t/2}dt=0.
```

Splitting both identities at `t=0` and adding them gives

```math
\int_0^\infty
(e^{t/2}+e^{-t/2})F_v(t)dt=0.
```

Hence

```math
\boxed{
\int_0^\infty e^{t/2}F_v(t)dt
=
-\int_0^\infty e^{-t/2}F_v(t)dt.
}
```

This is exact and uses only NULLPOL. No PNT, RH or asymptotic prime information is used.

Equivalently, in the correlation notation `C_v(t)=<v,T_t v>` one has

```math
\boxed{
\Re\int_0^\infty e^{t/2}C_v(t)dt
=
-\Re\int_0^\infty e^{-t/2}C_v(t)dt.
}
```

The growing `e^{t/2}` mode is therefore conjugate, on NULLPOL, to the decaying Critical-half Green mode.

---

# 3. Exact cancellation with the Gamma ground mode

Split

```math
h(t)=e^{-t/2}+h_1(t),
\qquad
h_1(t)=\frac{e^{-5t/2}}{1-e^{-2t}}.
```

Also write

```math
\nu_P=\Delta+e^{t/2}dt.
```

The prime term becomes

```math
-\int F_v\,d\nu_P
=
-\int F_v\,d\Delta
-
\int_0^\infty e^{t/2}F_v(t)dt.
```

By the NULLPOL identity in Section 2,

```math
-\int_0^\infty e^{t/2}F_v(t)dt
=
+\int_0^\infty e^{-t/2}F_v(t)dt.
```

The `e^{-t/2}` piece of the archimedean integral is

```math
-\int_0^\infty
\{F_v(t)-2e^{-t/2}f_v(0)\}e^{-t/2}dt
=
-\int_0^\infty e^{-t/2}F_v(t)dt
+2f_v(0),
```

because `int_0^infty e^{-t}dt=1`.

The two nonlocal correlation terms cancel exactly.

Thus

```math
Q_W(v)
=
-\int F_v\,d\Delta
+(2-\log4\pi-\gamma)f_v(0)
-
\int_0^\infty
\{F_v(t)-2e^{-t/2}f_v(0)\}h_1(t)dt.
```

Using

```math
F_v(t)
=2f_v(0)-\|K_tv\|_2^2
```

gives

```math
-\int
\{F_v-2e^{-t/2}f_v(0)\}h_1dt
=
\int h_1(t)\|K_tv\|_2^2dt
-2f_v(0)\int h_1(t)(1-e^{-t/2})dt.
```

From the already proved identity

```math
\kappa_*
=
\log4\pi+\gamma
+2\int_0^\infty h(t)(1-e^{-t/2})dt
```

and

```math
2\int_0^\infty e^{-t/2}(1-e^{-t/2})dt=2
```

one gets

```math
2\int_0^\infty h_1(t)(1-e^{-t/2})dt
=
\kappa_*-(\log4\pi+\gamma)-2.
```

Therefore the scalar coefficient is

```math
4-\kappa_*.
```

This proves

```math
\boxed{
Q_W(v)
=
\int_0^\infty h_1(t)\|K_tv\|_2^2dt
-(\kappa_*-4)\|v\|_2^2
-
\int_0^\infty F_v(t)\,d\Delta(t).
}
```

Numerically only as orientation,

```math
\kappa_*-4
=1.3721834192256655\ldots
```

No numerical value is needed in the proof.

---

# 4. The arithmetic discrepancy and its Laplace transform

For `Re s>1/2`, absolute convergence gives

```math
\begin{aligned}
\mathcal L\Delta(s)
&:=\int_0^\infty e^{-st}\,d\Delta(t)\\
&=
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}n^{-s}
-
\int_0^\infty e^{-(s-1/2)t}dt\\
&=
-\frac{\zeta'}{\zeta}\left(s+\frac12\right)
-
\frac1{s-1/2}.
\end{aligned}
```

Hence

```math
\boxed{
\mathcal L\Delta(s)
=
-\frac{\zeta'}{\zeta}\left(s+\frac12\right)
-
\frac1{s-1/2}.
}
```

The continuous compensator removes exactly the pole at `s+1/2=1` from the Euler logarithmic derivative.

The cumulative discrepancy is

```math
\boxed{
D(T)
:=\Delta([0,T])
=
\sum_{n\le e^T}\frac{\Lambda(n)}{\sqrt n}
-2(e^{T/2}-1).
}
```

This is the weighted Chebyshev discrepancy in logarithmic coordinates.

---

# 5. Firewall: polynomial control of D is already RH-scale information

Let

```math
S(X)=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}.
```

Then `D(log X)=S(X)-2(sqrt(X)-1)`.

If for some fixed `B`

```math
D(T)=O(T^B),
```

then

```math
S(X)=2(\sqrt X-1)+O((\log X)^B).
```

Stieltjes partial summation in the reverse direction gives

```math
\psi(X)
=\sqrt X\,S(X)
-\frac12\int_1^X S(t)t^{-1/2}dt,
```

hence

```math
\boxed{
\psi(X)=X+O(\sqrt X(\log X)^B).
}
```

Such a bound excludes nontrivial zeros with real part `>1/2`; by the functional equation it is RH-scale information.

Conversely the standard RH bound

```math
\psi(X)=X+O(\sqrt X\log^2X)
```

and partial summation imply

```math
D(T)=O(T^3)
```

(up to harmless lower-end constants).

Thus the new normal form has not made the hard arithmetic disappear: it has isolated it cleanly in `Delta`. Any easy claim that `D(T)` has polynomial growth would essentially be an RH proof and must be treated accordingly.

---

# 6. Exact OU/P11 root-trace bridge

Use the normalized OU family from the Critical-half rigidity audit:

```math
\langle\Phi^{(\sigma)}_x,\Phi^{(\sigma)}_y\rangle
=e^{-\sigma d(x,y)},
\qquad \sigma>0.
```

At a prime-power node `t_n=log n`, the weighted feature has root coordinate

```math
\sqrt{w_n}\,e^{-\sigma t_n},
\qquad
w_n=\frac{\Lambda(n)}{\sqrt n}.
```

Therefore the trace of the root projection over the prime-power channel basis is, for `sigma>1/4`,

```math
\begin{aligned}
\operatorname{tr}H_P^{(\sigma)}
&=
\sum_n w_n e^{-2\sigma t_n}\\
&=
\sum_n\Lambda(n)n^{-(1/2+2\sigma)}\\
&=
-\frac{\zeta'}{\zeta}\left(\frac12+2\sigma\right).
\end{aligned}
```

Now put on a continuous reference ray the compensator measure

```math
d\lambda_0(t)=e^{t/2}dt.
```

The same OU root coordinate has squared continuous mass

```math
\begin{aligned}
\operatorname{tr}H_0^{(\sigma)}
&=
\int_0^\infty e^{t/2}e^{-2\sigma t}dt\\
&=
\frac1{2\sigma-1/2}.
\end{aligned}
```

Consequently

```math
\boxed{
\operatorname{tr}H_P^{(\sigma)}
-
\operatorname{tr}H_0^{(\sigma)}
=
\mathcal L\Delta(2\sigma).
}
```

At the Critical-half/P11 value `sigma=1/2`,

```math
\boxed{
\operatorname{tr}H_P^{(1/2)}
-
\operatorname{tr}H_0^{(1/2)}
=
-\zeta'/\zeta(3/2)-2.
}
```

The P11 exponent `3/4` is visible here at the feature level:

```math
\sqrt{w_n}\,e^{-t_n/2}
=\sqrt{\Lambda(n)}\,n^{-3/4}.
```

For `n=p^k` this is precisely

```math
\sqrt{\log p}\,p^{-3k/4},
```

the P11 hub/root amplitude.

Thus the P11 common root is an exact discrete OU sampling of the same pole-subtracted prime-vs-continuum trace family that appears in the discrepancy normal form.

---

# 7. What this does and does not prove

What is now exact:

```text
Prime measure             nu_P
minus pole compensator    e^{t/2}dt
= arithmetic discrepancy Delta.

NULLPOL converts the compensator correlation into the decaying e^{-t/2}
Green correlation.

That Green correlation cancels exactly the mu_0=1/2 Gamma ground mode.

The P11 root trace, compared against the same continuous compensator root,
recovers the Laplace transform of Delta.
```

This is a genuine structural bridge between three previously separate project objects:

```text
NULLPOL Green exterior cancellation
Gamma ground mode
P11 OU/tree root.
```

However the decisive positivity step is still absent. In particular:

```math
\operatorname{tr}H_P^{(\sigma)}
-
\operatorname{tr}H_0^{(\sigma)}
```

is a **difference** of positive traces. No positive block matrix, contraction, Schur complement or shorting has yet been constructed whose residual quadratic form is the full `Delta` term.

A trace identity must not be promoted to an operator identity.

---

# 8. Next gate

The sharpened Object-X question is now:

```math
\boxed{
\text{Can the signed discrepancy pairing }
\int F_v\,d\Delta
\text{ be obtained as a forward Schur complement / compression}
\atop
\text{of a joint discrete-prime + continuous critical-half OU geometry?}
}
```

Required firewall:

1. the joint positive parent must be defined before using Weil positivity;
2. the continuous component must be the canonical compensator `e^{t/2}dt`, not fitted from `Delta`;
3. the construction must reproduce more than the scalar root trace — ideally the full autocorrelation pairing;
4. failure is acceptable and should become a class no-go;
5. no claim that this route is new in the literature until a dedicated audit is complete.
