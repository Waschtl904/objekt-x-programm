# P11 Audit — RP2 gamma-field origin and canonical normalization of the point mixer

**Datum:** 15. September 2026  
**Basis:** RP2 point-Weyl/zonal mixer and irreducibility audits.  
**Rolle:** theorem-level Herkunft und Normalisierung des bereits konstruierten Mixers `M_y`.  
**Registry:** unveraendert.  
**Nonclaim:** kein Koeffizient im finalen Weil-/P11-Block, kein NP-GAP, kein Object-X-Abschluss, kein RH-Beweis, keine Publikationsneuheit.

---

## 0. Kurzurteil

Der positive Rang-1-Mixer

```math
M_y
=|g_y\rangle\langle g_y|,
\qquad
g_y=P^{-2}\delta_y,
```

ist nicht eine nachtraeglich ausgewaehlte Zusatzgeometrie. Er ist exakt der **Zero-energy gamma-field Gramoperator** derselben Punkt-Weyl-Geometrie, deren skalare Weyl-Funktion die archimedische Gamma-Schicht liefert.

Definiere fuer `lambda>=0`

```math
\gamma_y(\lambda)c
:=c(P^2+\lambda)^{-1}\delta_y,
\qquad c\in\mathbb C.
```

Dann

```math
\boxed{
\gamma_y(0)1=g_y
}
```

und

```math
\boxed{
M_y
=\gamma_y(0)\gamma_y(0)^*.
}
```

Fuer die regularisierte skalare Weyl-Funktion

```math
m_y(\lambda)
:=\operatorname{FP}
\langle\delta_y,(P^2+\lambda)^{-1}\delta_y\rangle
```

gilt nach Ableitung, wobei die Divergenzkonstante verschwindet,

```math
\boxed{
-m_y'(\lambda)
=\|\gamma_y(\lambda)1\|^2.
}
```

Insbesondere

```math
\boxed{
-m_y'(0)=\|g_y\|^2.
}
```

Damit sind Richtung und interne Normierung des Mixers bereits durch die Weyl-Response festgelegt. Offen bleibt nicht mehr, **welcher** transversale Rang-1-Kanal natuerlich ist, sondern ob und mit welchem strukturell erzwungenen Gewicht dieser Kanal in der finalen P11/Weil-Feshbach-Geometrie auftritt.

Status:

```text
zero-energy gamma field gamma_y(0)                       ✓[M]
M_y = gamma_y(0) gamma_y(0)^*                           ✓[M]
-Weyl derivative = gamma-field norm squared              ✓[M]
closed formula for ||g_y||^2                             ✓[M]
point/isometry covariance of gamma field                 ✓[M]
internal mixer normalization fixed by Weyl geometry      ✓[M]
coefficient in final P11/Weil block                      ?[O]
Object X / NP-GAP / RH                                   ?[O]
```

---

# 1. Spectral setup

Let

```math
Y=RP^2,
\qquad
P=\sqrt{\Delta_Y+1/4}.
```

The zonal basis at a point `y` is

```math
\zeta_{m,y},
\qquad
P\zeta_{m,y}=\mu_m\zeta_{m,y},
\qquad
\mu_m=2m+1/2.
```

The point projector weight is

```math
\|\Pi_m\delta_y\|^2
=\frac{d_m}{V},
\qquad
d_m=4m+1=2\mu_m,
\qquad
V=2\pi.
```

Hence

```math
\Pi_m\delta_y
=\sqrt{\frac{d_m}{V}}\,\zeta_{m,y}.
```

---

# 2. Gamma field

For `lambda>=0` define the rank-one response map

```math
\boxed{
\gamma_y(\lambda):\mathbb C\to L^2(Y),
\qquad
\gamma_y(\lambda)c
=c(P^2+\lambda)^{-1}\delta_y.
}
```

The vector is in `L^2(Y)` because

```math
\begin{aligned}
\|\gamma_y(\lambda)1\|^2
&=\sum_{m\ge0}
\frac{d_m/V}{(\mu_m^2+\lambda)^2}\\
&\asymp\sum_{m\ge1}m^{-3}<\infty.
\end{aligned}
```

At zero energy

```math
\boxed{
\gamma_y(0)1
=P^{-2}\delta_y
=g_y.
}
```

---

# 3. The mixer is the gamma-field Gram

The adjoint

```math
\gamma_y(0)^*:L^2(Y)\to\mathbb C
```

is

```math
\gamma_y(0)^*h
=\langle g_y,h\rangle.
```

Therefore

```math
\begin{aligned}
\gamma_y(0)\gamma_y(0)^*h
&=g_y\langle g_y,h\rangle\\
&=M_yh.
\end{aligned}
```

Thus exactly

```math
\boxed{
M_y
=\gamma_y(0)\gamma_y(0)^*.
}
```

The mixer direction and its scale are therefore inherited from the natural boundary response operator; no independent normalization has been introduced in its definition.

---

# 4. Weyl derivative identity

Use the spectrally regularized diagonal response

```math
m_y(\lambda)
=\operatorname{FP}
\sum_{m\ge0}
\frac{d_m/V}{\mu_m^2+\lambda}.
```

The logarithmic counterterm in the finite part is independent of `lambda`. Differentiation therefore removes the divergence and gives an absolutely convergent series:

```math
\begin{aligned}
m_y'(\lambda)
&=-\sum_{m\ge0}
\frac{d_m/V}{(\mu_m^2+\lambda)^2}\\
&=-\|\gamma_y(\lambda)1\|^2.
\end{aligned}
```

Hence

```math
\boxed{
-m_y'(\lambda)
=\gamma_y(\lambda)^*\gamma_y(\lambda)
}
```

as a scalar operator on `C`.

At `lambda=0`:

```math
\boxed{
-m_y'(0)=\|g_y\|^2.
}
```

This is the direct spectral version of the standard Weyl/gamma-field derivative relation.

---

# 5. Closed norm formula

From the previous Point-Weyl audit,

```math
\langle\zeta_{m,y},g_y\rangle
=\frac1{\sqrt\pi\,\mu_m^{3/2}}.
```

Therefore

```math
\|g_y\|^2
=\frac1\pi\sum_{m=0}^\infty\mu_m^{-3}.
```

Since

```math
\mu_m=2(m+1/4),
```

we get

```math
\|g_y\|^2
=\frac1{8\pi}\zeta(3,1/4).
```

Using

```math
\zeta(3,1/4)+\zeta(3,3/4)=56\zeta(3)
```

and

```math
\zeta(3,1/4)-\zeta(3,3/4)
=64\beta(3)=2\pi^3,
```

with

```math
\beta(3)=\pi^3/32,
```

follows

```math
\boxed{
\zeta(3,1/4)=28\zeta(3)+\pi^3.
}
```

Hence

```math
\boxed{
\|g_y\|^2
=\frac{7\zeta(3)}{2\pi}
+\frac{\pi^2}{8}.
}
```

The value is independent of `y` by homogeneity.

---

# 6. Ground-state component

For `m=0`, `mu_0=1/2`. Therefore

```math
\boxed{
|\langle e_0,g_y\rangle|^2
=\frac8\pi.
}
```

Thus the dominant component of the canonical gamma-field vector lies in the already identified P11 ground mode, while every excited zonal component remains strictly nonzero.

This quantifies rather than merely asserts the ground/excited coupling.

---

# 7. Isometry covariance

For an isometry `r` of `RP^2`, let `U_r` be its unitary action. Since `P` commutes with all isometries,

```math
U_r(P^2+\lambda)^{-1}
=(P^2+\lambda)^{-1}U_r.
```

If `ry=y'`, then

```math
\delta_{y'}=U_r\delta_y
```

distributionally, hence

```math
\boxed{
\gamma_{y'}(\lambda)
=U_r\gamma_y(\lambda).
}
```

Consequently

```math
\boxed{
M_{y'}=U_rM_yU_r^*.
}
```

Thus the gamma-field normalization introduces no point-dependent scalar data.

---

# 8. What has been fixed, and what has not

Before this audit one could object:

```text
The point-Weyl geometry gives many possible noncommuting rank-one operators;
why choose precisely M_y and with which normalization?
```

This objection is resolved internally:

```math
\boxed{
M_y=\gamma_y(0)\gamma_y(0)^*
}
```

is the canonical zero-energy Gram of the same boundary response whose Weyl function is the Gamma multiplier.

However a different question remains open:

```text
Why should the final P11/Weil Gram use this gamma-field Gram with coefficient 1
(or any other coefficient) as an additional feature energy?
```

The statement `M_y is canonically normalized as a boundary-response object` does **not** imply `M_y appears with coefficient 1 in Object X`.

That coefficient/placement must follow from the source/Feshbach/finite-part geometry, not be fitted.

---

# 9. Relation to the source-filtration compatibility theorem

The separate compatibility audit proves that the fibrewise lift of `M_y` commutes with every source stop `Q_L`.

Combining that theorem with the current one gives:

```text
canonical mixer direction/scale from RP2 Weyl geometry
+
exact source-radius compatibility from tensor-factor separation.
```

Thus the remaining ambiguity is no longer an arbitrary transverse construction. It is solely the **role of this fixed canonical response channel in the final Weil/Feshbach identity**.

---

# 10. Forschungsurteil

The chain is now:

```text
RP2 point Weyl function m_y(lambda)
        |
        +-- derivative --> ||gamma_y(lambda)||^2
        |
        +-- lambda=0 --> gamma_y(0)=g_y
                              |
                              +-- Gram --> M_y
```

and independently

```text
M_y
 -> noncommuting zonal mixing
 -> compatible with P11 source stopping.
```

Therefore the next gate is not to invent or normalize a mixer. It is to derive a **forward identity** showing whether this already canonical gamma-field channel occurs in the P11/COMMON-JUMP finite-part/Feshbach architecture.

No such identity is claimed here.
