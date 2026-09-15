# P11 Audit — RP2 point-Weyl mixer versus source-conditioned Green filtration

**Datum:** 15. September 2026  
**Inputs:** Point-Weyl/zonal mixer at `c06500b9f09571bc40536ebe81157fbb0e741ae9`; source-conditioned RP2 Green filtration at `23849b3dbd4345d771721c201d7214212fa93ccb`.  
**Rolle:** theorem-level Kompatibilitaetstest zweier bereits separat bewiesener Forward-Bausteine.  
**Registry:** unveraendert.  
**Nonclaim:** keine Weil-/Feshbach-Identitaet, kein NP-GAP, kein Object-X-Abschluss, kein RH-Beweis, keine Publikationsneuheit.

---

## 0. Kurzurteil

Der nichtkommutierende transversale Point-Weyl-Mixer und die source-dependent P11-Radiusfiltration sind **exakt kompatibel**.

Die source conditioning schneidet nur die logarithmische Ast-/Innovationskoordinate ab. Der Mixer wirkt nur in der transversalen `RP^2`-Komponente. Daher kommutieren beide Operationen.

Sei

```math
\mathcal H_Y=L^2(RP^2),
\qquad
M_y=|g_y\rangle\langle g_y|\succeq0,
```

und auf dem operatorwertigen P11-Feature-Raum

```math
\mathscr K_Y
=\mathcal H_Y
\oplus
\bigoplus_pL^2(\mathbb R_+;\mathcal H_Y)
```

definiere

```math
\boxed{
\mathbf M_y
:=M_y
\oplus
\bigoplus_p(I\otimes M_y).
}
```

Fuer eine Familie von Stopptiefen `L_p>=0` sei

```math
Q_{\mathbf L}
=I_{root}
\oplus
\bigoplus_p
(M_{1_{[0,L_p]}}\otimes I_{\mathcal H_Y}).
```

Dann exakt

```math
\boxed{[Q_{\mathbf L},\mathbf M_y]=0.}
```

Sind `L_p<=L'_p` fuer alle `p`, so

```math
\boxed{
Q_{\mathbf L}\mathbf M_yQ_{\mathbf L}
\preceq
Q_{\mathbf L'}\mathbf M_yQ_{\mathbf L'}.
}
```

Damit liefert der Point-Weyl-Kanal eine **positive, nicht-P-diagonale und radiusmonotone Zusatzgeometrie** auf genau derselben source-conditioned Feature-Filtration wie P11.

Status:

```text
transverse lifted mixer Mbold_y bounded/positive              ✓[M]
source stop commutes with transverse mixer                     ✓[M]
nested stops preserve positive mixed-feature increments        ✓[M]
noncommuting P-mode mixing and radius monotonicity coexist      ✓[M]
source-dependent P11 depths can be inserted pointwise           ✓[M]
no new radius defect from the transverse mixer                  ✓[M]
mixed channel reproduces Weil finite-part/Feshbach residual     ?[O]
canonical coefficient/normalization in final Object X           ?[O]
NP-GAP / Object X / RH                                          ?[O]
```

---

# 1. Feature-space separation of variables

The operator-valued P11/RP2 feature space has the product form

```math
\mathscr K_Y
=\mathcal H_Y
\oplus
\bigoplus_pL^2(\mathbb R_+,ds;\mathcal H_Y).
```

The first summand is the common root coordinate. On each prime branch the variable

```math
s\in\mathbb R_+
```

is logarithmic Green/innovation depth, while `H_Y` carries the transverse Gamma modes.

Thus there are two genuinely different coordinates:

```text
longitudinal innovation depth s,
transverse spectral coordinate in RP2.
```

This separation is exactly what makes the compatibility theorem possible.

---

# 2. Source conditioning acts only in `s`

For a stop depth `L_p` on branch `p`, define

```math
Q_{L_p}^{(p)}
=M_{1_{[0,L_p]}}\otimes I_{\mathcal H_Y}.
```

Globally

```math
Q_{\mathbf L}
=I_{root}\oplus\bigoplus_pQ_{L_p}^{(p)}.
```

This is an orthogonal projection.

For nested stop data

```math
L_p\le L'_p
\quad\forall p,
```

one has

```math
\boxed{
Q_{\mathbf L}Q_{\mathbf L'}
=Q_{\mathbf L'}Q_{\mathbf L}
=Q_{\mathbf L}.
}
```

Hence

```math
Q_{\mathbf L}\preceq Q_{\mathbf L'}.
```

This is the continuous version of the P11 source-conditioning filtration.

---

# 3. The Point-Weyl mixer acts only transversally

From the Point-Weyl audit,

```math
g_y=P^{-2}\delta_y\in\mathcal H_Y
```

and

```math
M_y=|g_y\rangle\langle g_y|\succeq0
```

is bounded rank one.

Lift it identically to every root/innovation fibre:

```math
\boxed{
\mathbf M_y
=M_y\oplus\bigoplus_p(I\otimes M_y).
}
```

Then `Mbold_y` is bounded and positive on `K_Y`, with

```math
\|\mathbf M_y\|=\|M_y\|.
```

Because `M_y` does not commute with

```math
P=\sqrt{\Delta_{RP^2}+1/4},
```

the lifted mixer remains genuinely non-diagonal in the Gamma-mode decomposition.

---

# 4. Exact commutation theorem

On every branch,

```math
Q_{L_p}^{(p)}
=M_{1_{[0,L_p]}}\otimes I,
```

while

```math
\mathbf M_y^{(p)}
=I\otimes M_y.
```

Operators acting on separate tensor factors commute. Therefore

```math
Q_{L_p}^{(p)}\mathbf M_y^{(p)}
=\mathbf M_y^{(p)}Q_{L_p}^{(p)}.
```

The root projection is the identity, so globally

```math
\boxed{
[Q_{\mathbf L},\mathbf M_y]=0.
}
```

No spectral approximation or asymptotic argument is used.

---

# 5. Positive mixed-feature kernels

Let

```math
V_\alpha:\mathcal H_Y\to\mathscr K_Y
```

be any of the already constructed operator-valued P11/RP2 tree features.

Define the mixed stopped Gram kernel

```math
\boxed{
\mathcal M_{\mathbf L}(\alpha,\beta)
:=
V_\alpha^*
Q_{\mathbf L}\mathbf M_yQ_{\mathbf L}
V_\beta.
}
```

Since `Mbold_y>=0`, this is positive in the Gram sense:

```math
\sum_{i,j}
\langle h_i,
\mathcal M_{\mathbf L}(\alpha_i,\alpha_j)h_j\rangle
=
\left\|
\mathbf M_y^{1/2}Q_{\mathbf L}
\sum_iV_{\alpha_i}h_i
\right\|^2
\ge0.
```

Thus the mixer can be inserted as an additional manifestly positive feature channel.

---

# 6. Radius monotonicity survives the mixer

Assume

```math
Q_{\mathbf L}\preceq Q_{\mathbf L'}.
```

Because the projections commute with `Mbold_y`, write

```math
Q_{\mathbf L'}
=Q_{\mathbf L}+E,
```

with

```math
E\succeq0,
\qquad
EQ_{\mathbf L}=0,
\qquad
[E,\mathbf M_y]=0.
```

Then

```math
\begin{aligned}
Q_{\mathbf L'}\mathbf M_yQ_{\mathbf L'}
-Q_{\mathbf L}\mathbf M_yQ_{\mathbf L}
&=E\mathbf M_yE\\
&\succeq0.
\end{aligned}
```

Therefore

```math
\boxed{
\mathcal M_{\mathbf L'}-
\mathcal M_{\mathbf L}
\succeq_{Gram}0.
}
```

A genuinely noncommuting transverse mixer is therefore compatible with the same positive radius-filtration mechanism as the original P11 innovations.

---

# 7. Source-dependent P11 insertion

At source point `u` and window radius `R`, use the existing stop depths

```math
L_{p,R}(u)
=J_{p,R}(u)\log p.
```

For `R<S` and every old source point `|u|<R`, the P11 filtration proves

```math
J_{p,R}(u)\le J_{p,S}(u),
```

hence

```math
L_{p,R}(u)\le L_{p,S}(u).
```

Thus

```math
Q_{R,u}\preceq Q_{S,u}
```

and by §6

```math
\boxed{
\mathcal M_{R,u}
\preceq_{Gram}
\mathcal M_{S,u}.
}
```

The mixed channel introduces no new reversal of the source-radius order.

---

# 8. Noncommutativity is retained

The compatibility is not achieved by diagonalizing the mixer.

The stopped Green features contain factors

```math
e^{-Ps}.
```

Since

```math
[M_y,P]\ne0,
```

generically

```math
M_ye^{-Ps}\ne e^{-Ps}M_y.
```

Consequently the mixed Gram matrices have off-diagonal Gamma-mode entries.

In the zonal basis they inherit the strictly nonzero matrix elements of `M_y`, and hence the source stopping does **not** restore Gamma-mode superselection.

This proves simultaneous compatibility of

```text
P-mode mixing,
positive Gram structure,
source-radius monotonicity.
```

---

# 9. No new radius variable

The point `y`, the vector `g_y` and the operator `M_y` are fixed independently of `R`.

All radius dependence remains in the already existing stop data

```math
L_{p,R}(u).
```

Thus the transverse mixer does not introduce an independent running parameter.

Different point choices are still related by RP2 isometries as proved in the Point-Weyl audit.

---

# 10. What the theorem does NOT prove

The mixed kernel `M_L` is an additional positive feature family. Nothing in the commutation/monotonicity theorem identifies its coefficient in the physical Weil form.

In particular it is **not** proved that

```math
\text{mixed feature energy}
=
\text{missing centered Weil residual}.
```

Nor is it proved that adding this channel to the existing P11 Feshbach block produces the total Boundary-Weyl self-energy `Omega_R`.

Doing so by choosing a coefficient after looking at the target residual would be circular.

---

# 11. Sharp next gate

The previous open question

```text
Can noncommuting Gamma-mode mixing coexist with the real P11 source filtration?
```

is now answered:

```math
\boxed{\text{Yes.}}
```

The remaining question is narrower and harder:

```math
\boxed{
\text{Does the existing source-conditioned P11/Feshbach geometry}
\atop
\text{fix the mixed channel and its normalization so that the}
\text{total finite-part Boundary-Weyl residual is exactly recovered?}
}
```

This is now the appropriate Forward Object-X gate.

---

# 12. Forschungsurteil

The RP2 route now contains simultaneously:

```text
- exact P11 ground-state channel,
- full Gamma transverse ladder,
- source-conditioned radius filtration,
- a concrete bounded positive noncommuting mixer,
- and exact compatibility of that mixer with the radius filtration.
```

This removes a substantial structural obstruction.

But the central theorem still missing is an **identity**, not an existence statement: why this positive mixed geometry should have exactly the coefficient/shorting/finite-part required by the centered Weil form.

Until that identity is derived independently, NP-GAP and Object X remain open.
