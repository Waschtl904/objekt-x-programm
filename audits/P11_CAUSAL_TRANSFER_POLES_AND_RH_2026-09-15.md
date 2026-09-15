# P11 Audit — Causal transfer poles and the RH boundary

**Datum:** 15. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** theorem-level Spektral-/Systeminterpretation des Volterra-Kerns `J_Delta`.  
**Registry:** unveraendert.  
**Nonclaim:** dies ist eine RH-aequivalente Reformulierung, kein RH-Beweis und kein Neuheitsclaim.

---

## 0. Kurzurteil

Der im Critical-half-Finite-Part-Audit abgeleitete kausale Kern

```math
J_\Delta(L)
=e^{L/2}
\left(
L-\gamma-
\sum_{\log n<L}\frac{\Lambda(n)}{n}
\right)
```

hat fuer `Re s>1/2` die Laplacetransformierte

```math
\boxed{
\widehat J_\Delta(s)
=
\frac{
\displaystyle
\frac{d}{ds}\log\left((s-\tfrac12)\zeta(s+\tfrac12)\right)
-\gamma
}{s-\tfrac12}.
}
```

Der scheinbare Punkt `s=1/2` ist entfernbar. Die nichttrivialen Pole der meromorphen Fortsetzung liegen genau bei

```math
\boxed{s=\rho-\frac12}
```

mit `rho` einer nichttrivialen Nullstelle von zeta, unter Beibehaltung der Multiplizitaet.

Daher

```math
\boxed{
RH
\iff
\widehat J_\Delta^{\rm mer}(s)
\text{ hat keine Pole in }\Re s>0.
}
```

Unter RH gilt sogar der Standardweg

```math
J_\Delta(L)=O(L^2)
```

und damit existiert die echte Laplacetransformierte fuer jedes `Re s>0`. Umgekehrt wuerde eine vorwaerts konstruierte passive/stabile Realisierung des arithmetischen Volterra-Transfers auf der offenen rechten Halbebene die unerwuenschten Pole ausschliessen und damit RH liefern.

Das ist die praezise Systembedeutung des aktuellen Object-X-Gates:

```text
constructive positivity/passivity -> no unstable transfer poles -> RH.
```

Status:

```text
Laplace-transform formula                              ✓[M]
removability at s=1/2                                  ✓[M]
nontrivial poles = shifted zeta zeros                   ✓[M]
RH <=> no poles in open right half-plane                ✓[M]
RH => polynomial J_Delta via standard PNT error         ✓[M] (standard consequence)
passive positive realization of V_J                     ?[O]
```

---

# 1. Laplace transform from the Stieltjes inversion

For `Re s>1/2`, the unconditional growth of `J_Delta` is harmless and

```math
\widehat J_\Delta(s)
:=\int_0^\infty e^{-sL}J_\Delta(L)dL
```

converges.

The discrepancy transform is

```math
\mathcal L\Delta(s)
=-\frac{\zeta'}{\zeta}(s+1/2)
-\frac1{s-1/2}.
```

The Stieltjes identity is

```math
d\Delta
=\frac12J_\Delta dL-dJ_\Delta.
```

Taking the Laplace transform gives

```math
\begin{aligned}
\mathcal L\Delta(s)
&=\frac12\widehat J_\Delta(s)
-\int_0^\infty e^{-sL}dJ_\Delta(L)\\
&=\frac12\widehat J_\Delta(s)
+J_\Delta(0)-s\widehat J_\Delta(s)\\
&=J_\Delta(0)-(s-\tfrac12)\widehat J_\Delta(s).
\end{aligned}
```

Since

```math
J_\Delta(0)=-\gamma,
```

we obtain

```math
\boxed{
\widehat J_\Delta(s)
=\frac{-\gamma-\mathcal L\Delta(s)}{s-1/2}.
}
```

Substitution yields

```math
\boxed{
\widehat J_\Delta(s)
=
\frac{
-\gamma
+\zeta'/\zeta(s+1/2)
+1/(s-1/2)
}{s-1/2}.
}
```

---

# 2. Relative determinant notation

Define the pole-removed relative factor

```math
\boxed{
\mathcal D_{\rm rel}(s)
=(s-\tfrac12)\zeta(s+\tfrac12).
}
```

Then

```math
\frac{\mathcal D_{\rm rel}'(s)}{\mathcal D_{\rm rel}(s)}
=
\frac1{s-1/2}
+\frac{\zeta'}{\zeta}(s+1/2).
```

Hence

```math
\boxed{
\widehat J_\Delta(s)
=
\frac{
\mathcal D_{\rm rel}'(s)/\mathcal D_{\rm rel}(s)-\gamma
}{s-1/2}.
}
```

At `s=1/2`, the Laurent expansion

```math
\zeta(1+\varepsilon)
=\frac1\varepsilon+\gamma+O(\varepsilon)
```

shows

```math
\mathcal D_{\rm rel}(1/2+\varepsilon)
=1+\gamma\varepsilon+O(\varepsilon^2).
```

Thus

```math
\mathcal D_{\rm rel}'/\mathcal D_{\rm rel}-\gamma
=O(s-1/2),
```

so the apparent singularity of `Jhat` at `s=1/2` is removable.

---

# 3. Pole set

Away from `s=1/2`, poles of

```math
\mathcal D_{\rm rel}'/\mathcal D_{\rm rel}
```

occur exactly at zeros and poles of `D_rel`.

The zeta pole at `1` has been removed by the factor `(s-1/2)`. The trivial zeta zeros produce poles only at

```math
s=-2m-\frac12,
\qquad m>=1,
```

strictly in the left half-plane.

Every nontrivial zero `rho` gives a pole at

```math
\boxed{s=rho-1/2.}
```

Its residue equals the zero multiplicity; division by `s-1/2` does not remove such a pole because no nontrivial zero is `rho=1`.

---

# 4. RH equivalence

All nontrivial zeta zeros lie in the critical strip

```math
0<Re rho<1.
```

Therefore

```math
\widehat J_\Delta^{mer}
\text{ has no pole in }Re s>0
```

if and only if zeta has no zero with

```math
Re rho>1/2.
```

By the functional equation / symmetry of nontrivial zeros under

```math
rho -> 1-rho,
```

absence of zeros to the right of `1/2` is equivalent to every nontrivial zero lying on `Re rho=1/2`.

Hence

```math
\boxed{
RH
\iff
\widehat J_\Delta^{mer}
\text{ is pole-free in the open right half-plane}.
}
```

---

# 5. Actual Laplace convergence under RH

The classical RH consequence

```math
\psi(x)=x+O(\sqrt x\log^2x)
```

implies by partial summation

```math
\sum_{n<x}\frac{\Lambda(n)}n
=\log x-\gamma
+O(x^{-1/2}\log^2x).
```

With `x=e^L`, the closed formula for `J_Delta` gives

```math
\boxed{J_\Delta(L)=O(L^2).}
```

Thus, assuming RH, the defining Laplace integral for `Jhat_Delta` converges for every `Re s>0`, not merely by meromorphic continuation.

No converse growth theorem is needed for the pole-set equivalence in Section 4.

---

# 6. System-theoretic meaning and firewall

A causal passive or conservative transfer function produced by a well-posed positive state-space realization is analytic in its open stability half-plane. Therefore a **forward**, noncircular passive realization of the already-derived kernel `J_Delta` on `Re s>0` would force the pole-free property above and hence RH.

This explains why the missing positive realization is exactly as hard as it should be.

However it is forbidden to argue backwards:

```text
RH-equivalent analytic function
-> invoke a generic realization theorem
-> call the resulting storage space Object X.
```

Such a realization would merely encode the desired analyticity as an assumption.

The admissible Object-X task remains:

```text
construct the passive/conservative state space directly from
- the P11 stopped OU filtration,
- the continuous pole compensator,
- the higher Gamma filter bank,
- and the overlap-cone boundary geometry,
without assuming pole-freeness or Weil positivity.
```

---

# 7. Strategic endpoint

The research front can now be stated in one sentence:

```math
\boxed{
\text{Can the concrete stopped-OU/Gamma geometry furnish a positive storage}
\atop
\text{realization of the causal arithmetic kernel }J_\Delta
\text{ whose transfer is automatically analytic for }Re s>0?
}
```

A PASS would imply RH. A natural-class FAIL would be a meaningful Object-X no-go.
