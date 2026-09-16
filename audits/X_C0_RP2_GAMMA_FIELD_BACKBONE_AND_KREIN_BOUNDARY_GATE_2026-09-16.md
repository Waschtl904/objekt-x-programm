# X-C0 — RP2 gamma-field backbone and Krein-boundary gate

**Datum:** 16. September 2026  
**Basis:** X-C0 Draft-PR #137 plus stacked Cancel-first audit #138; RP2 point-Weyl/mixer #129 and mixer-filtration #136 are read-only inputs.  
**Rolle:** destruktiver C1 placement audit.  
**Registry:** unverändert.  
**Nonclaim:** kein positiver C1-Readout, kein Object-X-/NP-GAP-/RH-Abschluss, kein Publikationsneuheitsclaim.

---

## 0. Kurzurteil

Der kanonische RP2-Punktmischer

```math
M_y=|g_y\rangle\langle g_y|,
\qquad
g_y=P^{-2}\delta_y,
\qquad
P=\sqrt{\Delta_{RP^2}+1/4},
```

ist **kein zusaetzlicher positiver C1-Kanal**, der zur bereits exakten X-C0-Gammaenergie addiert werden darf.

Er ist der zero-energy Tangentialbaustein einer exakten positiven Zerlegung der **bereits vorhandenen** Gamma-Backbone.

Fuer `lambda>=0` setze

```math
\boxed{
g_{y,\lambda}
:=(P^2+\lambda)^{-1}\delta_y,
\qquad
M_{y,\lambda}
:=|g_{y,\lambda}\rangle\langle g_{y,\lambda}|.
}
```

Dann gilt schwach auf `L^2(RP^2)`

```math
\boxed{
\int_{RP^2}M_{y,\lambda}\,dy
=(P^2+\lambda)^{-2}.
}
```

und daher fuer reelles `z`

```math
\boxed{
P^{-2}-(P^2+z^2)^{-1}
=
\int_0^{z^2}\int_{RP^2}
M_{y,\lambda}\,dy\,d\lambda.
}
```

Nach Spur/Homogenitaet:

```math
\boxed{
\Phi_\infty(z)
=
\int_0^{z^2}\int_{RP^2}
\|g_{y,\lambda}\|^2\,dy\,d\lambda
=
2\pi\int_0^{z^2}\|g_{y_0,\lambda}\|^2d\lambda.
}
```

Insbesondere ist

```math
M_y=M_{y,0}.
```

Damit ist der Point-Weyl-Mixer als **interne Gamma-field/Feshbach-Geometrie** kanonisch, aber nicht als neue Energie neben `G`.

Der C1-Gate wird dadurch enger:

```text
KEEP the exact X-C0 Prime and Gamma ports.
DO NOT add M_y as an independent energy channel.
USE the gamma-field/mixer only inside a quotient/Feshbach/boundary completion
that redistributes the already existing energy and explains the threshold.
```

Status:

```text
integrated gamma-field Gram = full positive Gamma backbone        ✓[M]
M_y = zero-energy tangent of that existing backbone               ✓[M]
additive M_y with all C0 ports unchanged                          ×[M]
source-stop compatibility of internal mixer (input #136)          ✓[M]
Krein-von-Neumann M(0) boundary principle                         classical / imported
identification of final C1 threshold with a full boundary triple  ?[O]
positive C1 readout / Object X / RH                                ?[O]
```

---

# 1. Gamma fields at every spectral parameter

Let

```math
Y=RP^2,
\qquad
A:=P^2=\Delta_Y+1/4>0.
```

For `lambda>=0` and `y in Y` define

```math
\gamma_y(\lambda):\mathbb C\to L^2(Y),
\qquad
\gamma_y(\lambda)c
=c(A+\lambda)^{-1}\delta_y.
```

The point-Weyl audit already proves square-integrability. Spectrally,

```math
\|\gamma_y(\lambda)1\|^2
=
\sum_{m\ge0}
\frac{d_m/(2\pi)}{(\mu_m^2+\lambda)^2}
<\infty,
```

where

```math
\mu_m=2m+1/2,
\qquad d_m=4m+1=2\mu_m.
```

Set

```math
M_{y,\lambda}
:=\gamma_y(\lambda)\gamma_y(\lambda)^*
=|g_{y,\lambda}\rangle\langle g_{y,\lambda}|.
```

Each `M_(y,lambda)` is bounded, positive and rank one.

At zero:

```math
\boxed{
M_{y,0}=M_y.
}
```

No coefficient has been introduced.

---

# 2. Exact point-resolution identity

For `f,h in L^2(Y)`, using self-adjointness of `(A+lambda)^-1`,

```math
\begin{aligned}
\left\langle f,
\left(\int_YM_{y,\lambda}dy\right)h
\right\rangle
&=
\int_Y
[(A+\lambda)^{-1}f](y)
\overline{[(A+\lambda)^{-1}h](y)}dy\\
&=
\langle f,(A+\lambda)^{-2}h\rangle.
\end{aligned}
```

Therefore, in the weak operator sense,

```math
\boxed{
\int_YM_{y,\lambda}\,dy
=(A+\lambda)^{-2}.
}
```

This is the parameter-dependent extension of the already proved identity

```math
\int_YM_y\,dy=P^{-4}.
```

No point choice survives the integration.

---

# 3. Integrating the mixer family gives exactly the Gamma backbone

Functional calculus gives

```math
\frac{d}{d\lambda}(A+\lambda)^{-1}
=-(A+\lambda)^{-2}.
```

Hence for real `z`

```math
\begin{aligned}
A^{-1}-(A+z^2)^{-1}
&=
\int_0^{z^2}(A+\lambda)^{-2}d\lambda\\
&=
\int_0^{z^2}\int_YM_{y,\lambda}\,dy\,d\lambda.
\end{aligned}
```

Thus

```math
\boxed{
P^{-2}-(P^2+z^2)^{-1}
=
\int_0^{z^2}\int_YM_{y,\lambda}\,dy\,d\lambda.
}
```

The RP2 audit identifies

```math
\Phi_\infty(z)
=
\operatorname{Tr}_Y
[P^{-2}-(P^2+z^2)^{-1}].
```

Consequently Tonelli/trace positivity yields

```math
\boxed{
\Phi_\infty(z)
=
\int_0^{z^2}\int_Y
\|g_{y,\lambda}\|^2dy\,d\lambda.
}
```

By RP2 homogeneity, the inner norm is independent of `y`, and `vol(Y)=2pi`. Hence

```math
\boxed{
\Phi_\infty(z)
=
2\pi\int_0^{z^2}
\|g_{y_0,\lambda}\|^2d\lambda.
}
```

Equivalently for the regularized point-Weyl scalar `m_y(lambda)`,

```math
-m_y'(\lambda)=\|g_{y,\lambda}\|^2
```

and the positive Gamma difference is the integrated Weyl derivative.

---

# 4. Placement theorem: `M_y` is internal, not additive

X-C0 already has an exact Gamma port `G` satisfying on physical states

```math
\|\mathcal GT^0v\|^2
=\langle v,\Phi_\infty(D)v\rangle.
```

Section 3 shows that this same positive energy is already the integral of the canonical gamma-field Grams `M_(y,lambda)`.

Therefore an enlarged energy of the form

```math
\|\mathcal GT^0v\|^2
+c\,\|\mathbf M_y^{1/2}\,\Xi T^0v\|^2
```

with `c>0`, while **all other X-C0 ports and threshold bookkeeping are left unchanged**, cannot still equal the same signed COMMON-JUMP/Weil identity unless the added channel vanishes identically on the physical image.

For the natural ground/source insertion it does not vanish because

```math
\langle e_0,M_ye_0\rangle
=|\langle g_y,e_0\rangle|^2
=\frac8\pi>0.
```

Hence the class

```text
existing exact X-C0 ports
+
independent additional positive point-mixer energy
+
unchanged threshold / no compensating shorting
```

is excluded.

```math
\boxed{\text{additive independent }M_y\text{ channel}\quad\times[M]}
```

This is a placement no-go, not a no-go against using `M_y` internally in a larger positive parent.

---

# 5. Prime-2 witness and why mixed calibration alone is not enough

For the X-C0 Prime-2 witness `f,g`, the existing Prime jump port already gives

```math
\langle\mathcal P_{2,1}T^0f,
\mathcal P_{2,1}T^0g\rangle
=-\frac{\log2}{\sqrt2}\|f\|^2.
```

A root-only insertion of `M_y` has mixed term proportional to

```math
\langle f,g\rangle=0,
```

so the single off-diagonal Prime-2 number would **not detect** its illegal additive diagonal energy.

This is why PR #137 correctly requires the candidate to be checked on

```text
f, g, f+g, f-g,
```

not only on the mixed coefficient.

Since

```math
\langle e_0,M_ye_0\rangle=8/\pi,
```

an uncompensated root mixer changes the diagonal energies of `f` and `g` and therefore cannot preserve the full exact identity.

Thus the fixed witness reinforces the placement conclusion:

```text
M_y may enter only through an internal redistribution/shorting whose net
boundary output leaves the already-correct C0 Prime/Gamma identities intact.
```

---

# 6. Source filtration compatibility survives in the internal role

PR #136 proves for the fibrewise lift

```math
\mathbf M_{y,0}
=M_y\oplus\bigoplus_p(I\otimes M_y)
```

and every P11 source-stop projection `Q_L` that

```math
[Q_L,\mathbf M_{y,0}]=0.
```

The same proof is parameter-independent. Replacing `M_y` by

```math
M_{y,\lambda}
=|g_{y,\lambda}\rangle\langle g_{y,\lambda}|
```

still acts only in the transverse factor, hence

```math
\boxed{
[Q_L,\mathbf M_{y,\lambda}]=0
\qquad(\lambda\ge0).
}
```

Therefore the **entire integrated gamma-field decomposition** of the Gamma backbone is compatible with the real P11 stopping filtration.

This is stronger than compatibility of the single zero-energy mixer.

---

# 7. Krein-von Neumann zero-frequency boundary parameter

A standard theorem of boundary-triple extension theory states:

> for a positive symmetric operator with `0` in the resolvent of the distinguished Dirichlet/Friedrichs-type extension, the Krein-von Neumann extension is characterized by the boundary condition
>
> ```math
> \Gamma_1=M(0)\Gamma_0,
> ```
>
> where `M(lambda)` is the corresponding Weyl function.

Thus a zero-frequency Weyl value is not an arbitrary fitted Robin coefficient in a positive extension theory; it is the canonical Krein boundary parameter.

This standard theorem is used here only as an **architectural import**. The project has not yet constructed one complete boundary triple whose operator-valued Weyl function is the full Prime+RP2 `Omega_a` with all source-window and finite-part domains included.

Accordingly:

```text
zero-frequency threshold as canonical Krein-type boundary datum   ✓[K/M] architectural import
full X-C0 / total-Weyl boundary triple with this datum             ?[O]
```

### Critical firewall

The Krein principle does **not** by itself prove the centered Weil form positive.

At the scalar Weyl level, the canonical zero-frequency boundary completion explains the already known positive difference

```math
M(0)-M(z),
```

which is the analogue of the positive COMMON-JUMP backbone.

The centered Weil form contains an additional zero-frequency subtraction in the project bookkeeping. Thus one must not claim

```text
Krein extension => NP-GAP.
```

It does not. What it supplies is a canonical, non-fitted interpretation of the safe positive boundary completion around which C1 must be built.

---

# 8. Sharpened C1 gate

After the Cancel-first and current placement audits, the smallest surviving C1 problem is:

```text
1. KEEP the exact X-C0 Prime Jump/Euler ports.
2. KEEP the exact X-C0 Gamma port; its gamma-field mixer family is internal.
3. KEEP the pole ports and window embeddings.
4. Use the zero-frequency Weyl/Krein boundary datum as a canonical safe
   completion, not as a fitted coefficient.
5. Construct a source-compatible quotient/Feshbach/boundary colligation whose
   elimination changes only the boundary/threshold bookkeeping and returns
   the centered Weil residual.
6. The construction must preserve the Prime-2 coefficient and all four
   f,g,f+g,f-g tests without adding an independent positive mixer energy.
```

The point mixer is therefore **not** the missing channel. The missing object is the positive parent/quotient in which the already existing channels are glued.

This agrees with the total-Weyl formulation: the unexplained object is a noncircular positive boundary completion, not another local self-energy.

---

# 9. Recommended next destructive test

Use the finite-star RP2/P11 bulk from PR #133, whose forced root condition is

```math
\sum_{j=1}^Nf_j'(0)=(2-N)P f(0),
```

and whose running root counterterm satisfies

```math
A_{N+1}-A_N=-P,
\qquad NP+A_N=2P.
```

This is already positive and coefficient-free.

The next test should ask:

```math
\boxed{
\text{Does its forced running root/Krein boundary completion, after inserting}
\atop
\text{the source stops, induce exactly the X-C0 zero-frequency threshold}
\text{without modifying the already-correct Jump/Gamma ports?}
}
```

PASS would give a genuine C1 mechanism.

FAIL would eliminate the most natural coefficient-free RP2/P11 boundary-completion class, while leaving X-C0 and the local survivor identities intact.

---

# 10. Sources / review target

Project inputs:

```text
PR #137  X-C0 common-memory mediator
PR #138  cancel-first prime-base/raw-memory audit
PR #129  RP2 point-Weyl gamma-field mixer
PR #136  mixer/source-stop compatibility
PR #133  local positive RP2 star bulk and running root counterterm
PR #134  total Boundary-Weyl self-energy
```

External standard input:

```text
Krein-von Neumann extension in boundary-triple form:
Gamma_1=M(0)Gamma_0.
```

Destructive review should focus on:

```text
R1. weak operator integral int_Y M_(y,lambda)dy=(P^2+lambda)^-2;
R2. integration in lambda and exact recovery of the existing Gamma backbone;
R3. the scope of the additive-mixer no-go;
R4. extension of source-stop commutation from lambda=0 to lambda>=0;
R5. keeping the classical Krein boundary theorem separate from the still-open
    construction of a project-wide Prime+RP2 boundary triple.
```
