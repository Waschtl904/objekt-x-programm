# P11 Audit — Lagarias transfer decomposition of the causal normal form

**Datum:** 15. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** theorem-level Identifikation der neuen kausalen Normalform mit dem klassischen positive-real RH-Objekt.  
**Registry:** unveraendert.  
**Nonclaim:** das positive-real-Kriterium ist klassisch (Lagarias); kein Neuheits- oder RH-Beweis.

---

## 0. Kurzurteil

Die neue Volterra-/Gamma-Normalform setzt sich im Laplace-Bereich exakt zur verschobenen logarithmischen Ableitung der Riemann-Xi-Funktion zusammen.

Definiere

```math
\boxed{
G(s)
:=\frac{\xi'}{\xi}\left(\frac12+s\right).
}
```

Mit

```math
\mu_m=2m+\frac12,
\qquad
c_*=\log(8\pi)+\frac\pi2-4-\gamma,
```

und der Laplacetransformierten des arithmetischen Volterra-Kerns gilt fuer den zunaechst absolut konvergenten Bereich und danach meromorph fortgesetzt:

```math
\boxed{
G(s)
=
(s-\tfrac12)\widehat J_\Delta(s)
+
\sum_{m=1}^\infty
\frac{s}{\mu_m(s+\mu_m)}
-
\frac{c_*}{2}.
}
```

Der Term

```math
\frac{s}{\mu_m(s+\mu_m)}
```

ist die Laplace-/positive-real-Version genau desselben stabilen Gamma-Filters, dessen Zeitbereichsdissipation in der Weilform als

```math
\frac2{\mu_m}\|y_m'\|^2
```

auftritt.

Das klassische Kriterium von Lagarias lautet, in dieser verschobenen Variable,

```math
\boxed{
RH
\iff
\operatorname{Re}G(s)>0
\quad\text{fuer alle }\operatorname{Re}s>0.
}
```

Damit ist die aktuelle Object-X-Frage **kein neues RH-Kriterium**. Sie ist die wesentlich engere konstruktive Frage, ob die bereits unabhaengig gefundene P11/stopped-OU/overlap-cone-Geometrie eine vorwaerts definierte passive Realisierung genau dieser bekannten positive-real-Funktion liefert.

Status:

```text
exact transfer decomposition into J_Delta + Gamma bank  ✓[M]
mu_0 + pole collapse to the constant 2                   ✓[M]
constant equals -c_*/2 after assembly                    ✓[M]
Lagarias positive-real RH criterion                       known/classical
P11/OU constructive passive realization                  ?[O]
```

---

# 1. Completed logarithmic derivative

For

```math
z=\frac12+s,
```

the completed function is

```math
\xi(z)
=\frac12z(z-1)\pi^{-z/2}\Gamma(z/2)\zeta(z).
```

Therefore

```math
\begin{aligned}
G(s)
&=\frac1{s+1/2}
 +\frac1{s-1/2}
 -\frac12\log\pi\\
&\quad+
\frac12\psi\left(\frac14+\frac s2\right)
+\frac{\zeta'}{\zeta}\left(\frac12+s\right).
\end{aligned}
```

---

# 2. Arithmetic relative-determinant term

From the previous causal-transfer audit,

```math
\widehat J_\Delta(s)
=
\frac{
-\gamma
+\zeta'/\zeta(s+1/2)
+1/(s-1/2)
}{s-1/2}.
```

Hence

```math
\boxed{
\frac1{s-1/2}
+\frac{\zeta'}{\zeta}(s+1/2)
=
\gamma+(s-1/2)\widehat J_\Delta(s).
}
```

This is the prime/pole part of the completed logarithmic derivative.

---

# 3. Gamma ladder in positive-real form

The digamma partial fraction expansion gives

```math
\frac12
\left[
\psi\left(\frac14+\frac s2\right)-\psi(1/4)
\right]
=
\sum_{m=0}^\infty
\left(
\frac1{\mu_m}-\frac1{s+\mu_m}
\right),
```

where

```math
\mu_m=2m+\frac12.
```

Equivalently,

```math
\boxed{
\frac12
\left[
\psi\left(\frac14+\frac s2\right)-\psi(1/4)
\right]
=
\sum_{m=0}^\infty
\frac{s}{\mu_m(s+\mu_m)}.
}
```

Since

```math
\kappa_*=\log\pi-\psi(1/4),
```

we get

```math
\boxed{
-\frac12\log\pi
+\frac12\psi\left(\frac14+\frac s2\right)
=
-\frac{\kappa_*}{2}
+
\sum_{m=0}^\infty
\frac{s}{\mu_m(s+\mu_m)}.
}
```

For `Re s>0`, each Gamma summand has positive real part:

```math
\operatorname{Re}
\frac{s}{\mu(s+\mu)}
=
\frac{
\operatorname{Re}(s)(\operatorname{Re}(s)+\mu)
+(\operatorname{Im}s)^2
}{
\mu|s+\mu|^2
}
>0.
```

---

# 4. Ground-mode / pole collapse

The ground Gamma mass is

```math
\mu_0=\frac12.
```

Its term is

```math
\frac{s}{(1/2)(s+1/2)}
=\frac{2s}{s+1/2}.
```

Together with the remaining completed-zeta pole factor,

```math
\frac1{s+1/2},
```

one gets the exact constant

```math
\boxed{
\frac1{s+1/2}
+
\frac{2s}{s+1/2}
=2.
}
```

Thus no `s`-dependence from this pair remains.

---

# 5. Final assembly

Combining Sections 1--4 gives

```math
G(s)
=
(s-1/2)\widehat J_\Delta(s)
+
\sum_{m=1}^\infty\frac{s}{\mu_m(s+\mu_m)}
+
2+\gamma-\frac{\kappa_*}{2}.
```

But

```math
c_*=\kappa_*-4-2\gamma,
```

so

```math
2+\gamma-\frac{\kappa_*}{2}
=-\frac{c_*}{2}.
```

Therefore

```math
\boxed{
G(s)
=
(s-\tfrac12)\widehat J_\Delta(s)
+
\sum_{m=1}^\infty\frac{s}{\mu_m(s+\mu_m)}
-
\frac{c_*}{2}.
}
```

This is exactly the frequency/Laplace counterpart of the causal dissipation-feedback decomposition of the Weil quadratic form.

---

# 6. Collision with the classical Lagarias criterion

Jeffrey Lagarias proved/studied the classical positivity characterization

```math
RH
\iff
\operatorname{Re}\frac{\xi'}{\xi}(z)>0
\quad\text{for }\operatorname{Re}z>1/2.
```

After `z=1/2+s`, this is

```math
\boxed{
RH
\iff
\operatorname{Re}G(s)>0
\quad(\operatorname{Re}s>0).
}
```

Thus the abstract statement

```text
"find a passive realization of G"
```

is not itself new; it is another expression of a known positive-real RH criterion.

The project-specific content of the present chain is the exact decomposition of `G` into components that arose independently from the finite-window/P11 analysis:

```text
arithmetic channel:   (s-1/2) Jhat_Delta(s)
higher Gamma bank:    sum_{m>=1} s/[mu_m(s+mu_m)]
fixed leakage:        -c_*/2
```

and the fact that the same arithmetic channel was obtained geometrically from the stopped OU boundary-depth system.

---

# 7. Boundary Herglotz interpretation under RH

If RH holds, the nontrivial zeros are

```math
\rho=\frac12+i\gamma.
```

The Hadamard/logarithmic-derivative representation then has the schematic positive-real form

```math
G(s)
=\sum_\gamma \frac{m_\gamma}{s-i\gamma}
```

with the standard symmetric regularization. For `Re s>0`, every summand has positive real part.

Its boundary real part as `Re s downarrow 0` is, distributionally, a positive measure supported at the ordinates `gamma`. This is the same zero-side positivity that underlies Weil's quadratic criterion.

This observation is classical/Herglotz in nature; it is recorded only to show why a successful passive state-space realization would be the correct kind of Object X.

---

# 8. Updated novelty firewall

Known / not claimed as project novelty:

```text
- RH as positivity of Re(xi'/xi) in the right half-strip;
- positive-real/Herglotz interpretation;
- zeta-related transfer-system viewpoints in general;
- causal-system reformulations by themselves.
```

Potentially project-specific and still requiring independent literature audit:

```text
- derivation of the arithmetic impulse kernel J_Delta from the P11 stopped-OU
  boundary geometry;
- exact universal boundary-tail shorting of the P11 masked filtration;
- the time-domain decomposition matching the higher Gamma filter bank and
  fixed leakage constant with no fitted coefficients.
```

No novelty is asserted yet.

---

# 9. Sharpened research gate

The only version of the passivity route that would be substantive is:

```math
\boxed{
\text{derive a positive storage realization directly from the concrete}
\atop
\text{P11 stopped-OU / overlap-cone geometry, and then verify that its}
\text{transfer is }G(s),\text{ without assuming Lagarias positivity.}
}
```

Invoking a generic Herglotz/passive realization theorem would be circular, because the required positive-real property is already equivalent to RH.
