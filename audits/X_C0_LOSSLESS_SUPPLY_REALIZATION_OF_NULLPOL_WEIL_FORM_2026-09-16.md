# X-C0 — Lossless supply realization of the NULLPOL Weil form

**Datum:** 16. September 2026  
**Basis:** X-C0 #137; stacked audits #138; Critical-half finite-part/Volterra normal form; exact `J_Delta` transport+P11-tail decomposition.  
**Registry:** unverändert.  
**Nonclaim:** kein Beweis `Q_W>=0`, kein positiver finaler C1-Readout, kein Object-X-/NP-GAP-/RH-Abschluss, kein Publikationsneuheitsclaim.

---

## 0. Kurzurteil

Die nach Hard Audit verbliebene signed NULLPOL-Weilform besitzt nun eine **vollstaendig vorwaerts definierte, coefficient-free lossless supply representation**.

Der arithmetische Finite-Part-Koeffizient `J_Delta(L)` ist zunaechst ein Off-Diagonal-Matrixelement eines positiven Hilbertraums, aufgebaut aus

```text
- dem symmetrischen Differenzstreifen des sicheren Prime/Continuum-Massentransports;
- den exakt ungelösten stopped-P11 OU-Boundary-Tail-Zustaenden.
```

Der Source-Faktor

```math
D_+=\partial_x+1/2
```

besitzt seinerseits eine unitäre Polarzerlegung relativ zu

```math
L_{1/2}=-\partial_x^2+1/4.
```

Beide unitären Teile tensorisieren zu einer fiberweisen lossless Scattering-Transformation. Dadurch wird der komplette signierte arithmetische Volterra-Term zur Differenz zweier positiver Portnormen.

Zusammen mit der bereits positiven hoeheren Gamma-Filterbank erhaelt man fuer jedes feste Fenster `[-a,a]` und jedes glatte NULLPOL-`v` exakt

```math
\boxed{
Q_W(v)
=
\|\mathcal O_a v\|^2
-
\|\mathcal I_a v\|^2,
}
```

mit **expliziten, vorwaerts definierten** OUT-/IN-Ports

```math
\mathcal O_av
=(\mathcal G_{\ge1}v,\Phi_-(v)),
```

```math
\mathcal I_av
=(\sqrt{c_*}\,v,\Phi_+(v)),
```

und

```math
\boxed{
c_*
=\log(8\pi)+\frac\pi2-4-\gamma
>0.
}
```

Numerisch nur zur Orientierung:

```text
c_* = 0.2177520894...
```

Somit ist der verbleibende Positivitaetsgate **genau** eine passivitaets-/bounded-real-artige Portdominanzfrage:

```math
Q_W(v)\ge0
\iff
\|\mathcal I_av\|\le\|\mathcal O_av\|
\quad(v\in\mathscr D_{NP,a}).
```

Diese Aequivalenz ist nicht als Loesung zu missverstehen. Ein Kontraktor darf nicht rueckwaerts aus der Ungleichung definiert werden. Der weitere Object-X-Gate ist jetzt vielmehr:

> Leitet die vorhandene X-C0-/stopped-OU-/RP2-Zustandsdynamik **vorwaerts** einen kausalen/geometrischen Kontraktor vom OUT- zum IN-Port her?

Status:

```text
transport defect as positive 2-port off-diagonal                 ✓[M]
P11 unresolved tails in same positive 2-port                     ✓[M]
J_Delta as Critical-half scaled lossless matrix element           ✓[M]
unitary polar factor of D_+=partial+1/2                           ✓[M]
full arithmetic Volterra term as lossless scattering supply       ✓[M]
Q_W = ||OUT||^2-||IN||^2 on fixed-window NULLPOL                 ✓[M]
forward geometric OUT->IN contraction                             ?[O]
Object X / NP-GAP / RH                                            ?[O]
```

---

# 1. Safe transport discrepancy as an Off-Diagonal Gram entry

Recall

```math
h_p=\log p,
\qquad
a_p=\frac{h_p}{p-1},
```

and, ordering the primes increasingly,

```math
s_0=\gamma,
\qquad
s_N=\gamma+\sum_{j\le N}a_{p_j}.
```

For `L>0` away from prime-power jump points let

```math
N(L)=\#\{p:h_p<L\},
```

```math
\boxed{d(L):=L-s_{N(L)}.}
```

Work in the fixed transport Hilbert space

```math
\mathscr H_{tr}=L^2(\mathbb R_+,d\lambda).
```

Let

```math
E_L
=(\min\{L,s_{N(L)}\},\max\{L,s_{N(L)}\}).
```

Define

```math
r_L=\mathbf1_{E_L},
```

and, with an arbitrary convention `sgn(0)=1`,

```math
q_L=\operatorname{sgn}(d(L))\,\mathbf1_{E_L}.
```

Then

```math
\boxed{
\|r_L\|^2
=\|q_L\|^2
=|d(L)|,
}
```

and

```math
\boxed{
\langle r_L,q_L\rangle=d(L).
}
```

This is the literal `cancel-first` form of the safe monotone transport: the common prefix of `[0,L]` and `[0,s_N]` has already been removed; only their oriented symmetric-difference strip remains.

No large common-mode energy is retained.

---

# 2. Add the unresolved stopped-P11 Boundary tails

The preceding audit constructs, for every active prime `p`, the normalized unresolved OU boundary-tail state with coefficient

```math
b_{p,J_p(L)}
=\frac{\sqrt{h_p}\,q_p^{J_p(L)+1}}
       {\sqrt{1-q_p^2}},
\qquad q_p=p^{-1/2},
```

whose squared norm is

```math
\boxed{
|b_{p,J_p(L)}|^2
=U_p(L)
=\frac{h_pp^{-J_p(L)}}{p-1}.
}
```

Put all such coefficients into a fixed Hilbert space

```math
\mathscr H_{tail}=\ell^2(\mathcal P),
```

with zero coordinate for inactive primes, and write

```math
b_L=(b_{p,J_p(L)})_p.
```

Then

```math
\boxed{
\|b_L\|^2
=T(L):=\sum_{h_p<L}U_p(L).
}
```

Set

```math
\mathscr A
=\mathscr H_{tr}\oplus\mathscr H_{tail},
```

```math
\boxed{
R_L=r_L\oplus b_L,
\qquad
S_L=q_L\oplus b_L.
}
```

Therefore

```math
\boxed{
\|R_L\|^2
=\|S_L\|^2
=|d(L)|+T(L),
}
```

and, using the exact preceding theorem

```math
 e^{-L/2}J_\Delta(L)=d(L)+T(L),
```

we obtain

```math
\boxed{
\langle R_L,S_L\rangle
=e^{-L/2}J_\Delta(L).
}
```

Thus the full safe coefficient, including all prime powers, is already an Off-Diagonal matrix element of a positive Gram pair with equal diagonal norms.

---

# 3. The auxiliary map is lossless

Define on the transport factor the multiplication operator

```math
(W_L^{tr}f)(\lambda)
=
\begin{cases}
\operatorname{sgn}(d(L))f(\lambda),&\lambda\in E_L,\\
f(\lambda),&\lambda\notin E_L,
\end{cases}
```

and on the tail factor use the identity.

Then

```math
\boxed{
W_L:=W_L^{tr}\oplus I_{tail}
}
```

is self-adjoint and unitary:

```math
W_L^*=W_L,
\qquad
W_L^2=I.
```

Moreover

```math
\boxed{S_L=W_LR_L.}
```

After the **correct** Critical-half amplitude scaling

```math
\widehat R_L=e^{L/4}R_L,
\qquad
\widehat S_L=e^{L/4}S_L,
```

one has

```math
\boxed{
\langle\widehat R_L,
W_L\widehat R_L\rangle
=J_\Delta(L).
}
```

This is coefficient-free. The factor `e^(L/4)` is the amplitude lift corresponding to the energy-scale change

```math
\Lambda(n)/n
\mapsto
\Lambda(n)/\sqrt n.
```

---

# 4. Polar decomposition of the Critical-half source port

Let

```math
D_+=\partial_x+\frac12,
\qquad
D_-=-\partial_x+\frac12.
```

Then

```math
D_-D_+
=L_{1/2}
=-\partial_x^2+\frac14.
```

Since `L_(1/2)>=1/4`, define

```math
H:=L_{1/2}^{1/2}
```

and

```math
\boxed{
U:=D_+H^{-1}.
}
```

On Fourier side the symbol of `U` is

```math
\frac{1/2+i\xi}{\sqrt{\xi^2+1/4}},
```

which has modulus one. Hence

```math
\boxed{U\text{ is unitary}.}
```

Moreover all of `U`, `H` and the translations commute as Fourier multipliers.

For real `L` and smooth `v`, put

```math
\psi_v(L)
:=H^{1/2}T_{-L/2}v
=L_{1/2}^{1/4}T_{-L/2}v.
```

Then

```math
\begin{aligned}
\langle D_+T_{-L/2}v,T_{L/2}v\rangle
&=
\left\langle
H^{1/2}T_{-L/2}v,
H^{1/2}U^*T_{L/2}v
\right\rangle\\
&=
\boxed{
\langle\psi_v(L),
U^*T_L\psi_v(L)\rangle.
}
\end{aligned}
```

Thus the two source factors in the Volterra correlation also differ by a unitary operator.

---

# 5. Fixed-window lossless scattering space

Let `v` be supported in `[-a,a]`. Its midpoint correlation vanishes for `L>2a`, so only

```math
0<L<2a
```

enters the Volterra form.

Use the fixed-window direct-integral Hilbert space

```math
\boxed{
\mathscr Z_a
:=L^2((0,2a),dL;\mathscr A\widehat\otimes L^2(\mathbb R_x)).
}
```

Define

```math
\boxed{
(\Phi_av)(L)
:=
\widehat R_L\otimes\psi_v(L).
}
```

For fixed `a` this is well defined on smooth compactly supported `v`, because all auxiliary coefficients are locally bounded in `L` and the interval is finite.

Define fiberwise

```math
\boxed{
\mathscr S_L
:=W_L\otimes U^*T_L.
}
```

Each factor is unitary, hence

```math
\mathscr S_L^*\mathscr S_L=I.
```

The direct integral

```math
\boxed{
\mathscr S_a
:=\int_0^{2a}{}^\oplus\mathscr S_LdL
}
```

is therefore unitary on `Z_a`.

---

# 6. Exact arithmetic Volterra term

Using §§3--5,

```math
\begin{aligned}
\langle\Phi_av,
\mathscr S_a\Phi_av\rangle
&=
\int_0^{2a}
J_\Delta(L)
\langle D_+T_{-L/2}v,T_{L/2}v\rangle dL.
\end{aligned}
```

The prior Critical-half finite-part theorem gives

```math
F_v'(L)+\frac12F_v(L)
=2\operatorname{Re}
\langle D_+T_{-L/2}v,T_{L/2}v\rangle,
```

where `F_v=f_v+f_v(-.)`.

Therefore

```math
\boxed{
\int_0^\infty
J_\Delta(L)
\left(F_v'(L)+\frac12F_v(L)\right)dL
=
2\operatorname{Re}
\langle\Phi_av,
\mathscr S_a\Phi_av\rangle.
}
```

The upper limit may be replaced by `2a` because the source correlation is zero outside the window difference set.

Thus the complete signed arithmetic discrepancy contribution is a lossless scattering matrix element of a positive Hilbert state built forward from the prime-base transport and stopped-P11 boundary states.

---

# 7. Lossless input/output ports

Define

```math
\boxed{
\Phi_+(v)
:=\frac{I+\mathscr S_a}{\sqrt2}\Phi_av,
\qquad
\Phi_-(v)
:=\frac{I-\mathscr S_a}{\sqrt2}\Phi_av.
}
```

Since `S_a` is unitary,

```math
\begin{aligned}
\|\Phi_-(v)\|^2
-\|\Phi_+(v)\|^2
&=-2\operatorname{Re}
\langle\Phi_av,\mathscr S_a\Phi_av\rangle.
\end{aligned}
```

Hence

```math
\boxed{
-\int J_\Delta(L)
\left(F_v'(L)+\frac12F_v(L)\right)dL
=
\|\Phi_-(v)\|^2
-\|\Phi_+(v)\|^2.
}
```

The sign is therefore carried entirely by the **supply-rate orientation** of a lossless scattering channel, not by an indefinite local energy density.

---

# 8. Add the positive higher-Gamma reservoir

The previous causal Gamma theorem defines

```math
\mu_m=2m+\frac12,
\qquad
 y_m=(\partial_x+\mu_m)^{-1}v,
\qquad m\ge1,
```

and the positive output map

```math
\boxed{
\mathcal G_{\ge1}v
:=
\left[
\sqrt{\frac2{\mu_m}}\,y_m'
\right]_{m\ge1},
}
```

with

```math
\boxed{
\|\mathcal G_{\ge1}v\|^2
=E_{\Gamma,\ge1}(v).
}
```

The exact causal NULLPOL normal form was

```math
Q_W(v)
=E_{\Gamma,\ge1}(v)
-c_*\|v\|^2
-\int J_\Delta(L)
\left(F_v'(L)+\frac12F_v(L)\right)dL,
```

where

```math
\boxed{
c_*
=\log(8\pi)+\frac\pi2-4-\gamma
>0.
}
```

Substitution of §7 yields

```math
\boxed{
Q_W(v)
=\|\mathcal G_{\ge1}v\|^2
+\|\Phi_-(v)\|^2
-\|\Phi_+(v)\|^2
-c_*\|v\|^2.
}
```

---

# 9. Exact IN/OUT normal form

Define positive Hilbert-valued source maps

```math
\boxed{
\mathcal O_av
:=
(\mathcal G_{\ge1}v,\Phi_-(v)),
}
```

and

```math
\boxed{
\mathcal I_av
:=
(\sqrt{c_*}\,v,\Phi_+(v)).
}
```

Then for every smooth compactly supported NULLPOL source in the fixed window,

```math
\boxed{
Q_W(v)
=\|\mathcal O_av\|^2
-\|\mathcal I_av\|^2.
}
```

Thus

```math
\boxed{
Q_W(v)\ge0
\iff
\|\mathcal I_av\|
\le
\|\mathcal O_av\|.
}
```

For the family of all windows this is another exact form of the remaining RH-equivalent positivity gate.

### Circularity firewall

One must **not** now define

```math
C_a\mathcal O_av:=\mathcal I_av
```

and call `C_a` contractive because `Q_W>=0` is desired. That would merely restate the unknown inequality.

A valid Object-X step must derive a forward map between these ports from the pre-existing X-C0 common memory / stopped OU / RP2 dynamics, before using the sign of `Q_W`.

---

# 10. Optional symmetric/antisymmetric reading

The two lossless ports are the symmetric and antisymmetric combinations of the same positive state and its unitary scatter:

```math
\Phi_+
=\frac{\Phi+\mathscr S\Phi}{\sqrt2},
```

```math
\Phi_-
=\frac{\Phi-\mathscr S\Phi}{\sqrt2}.
```

Thus the complete NULLPOL form reads

```text
OUT:
  higher Gamma dissipation
  + antisymmetric relative transport/P11 scattering port

IN:
  fixed leakage sqrt(c_*) * identity
  + symmetric relative transport/P11 scattering port.
```

This is a supply-rate / bounded-real formulation, not a positivity theorem.

It is materially stronger than the earlier pointwise-scattering attempt: the unitary scatter now lives in a **source-conditioned auxiliary Hilbert space** built from the safe mass transport and stopped P11 boundary states. It is not multiplication by the sign-changing scalar Weil symbol.

---

# 11. Prime-2 calibration

No new coefficient was chosen from the Prime-2 witness.

The IN/OUT identity is derived from the already exact global finite-part/Volterra formula and therefore applies automatically to the predeclared Prime-2 quartet `f,g,f+g,f-g` once their NULLPOL/support hypotheses hold.

In particular, the existing X-C0 Jump port retains the exact mixed arithmetic coefficient

```math
-\frac{\log2}{\sqrt2}.
```

The new transport/scattering representation does not replace that channel; it is a reorganization of the already exact total discrepancy coefficient `J_Delta`.

This is why the earlier raw-memory replacement no-go is not violated.

---

# 12. The remaining single gate

All scalar arithmetic coefficients and their signs have now been placed in forward geometric objects:

```text
prime-power jumps            -> stopped P11 boundary tails,
prime-base discrepancy       -> oriented transport strip,
Critical-half factor         -> amplitude e^(L/4),
source first-order port      -> unitary polar factor U,
higher Gamma energy          -> stable positive filter bank,
fixed finite-part leakage    -> c_* > 0.
```

The only remaining nontrivial question on this branch is:

```math
\boxed{
\text{Does the X-C0 / stopped-OU / RP2 state dynamics furnish a forward}
\atop
\text{geometric contraction/intertwiner from OUT to IN?}
}
```

Equivalently: can the above lossless supply balance be embedded into a genuinely passive/conservative positive parent **without defining the contraction from the desired Weil inequality itself**?

A PASS would be a substantive C1/Object-X mechanism.

A FAIL for the natural X-C0 state-equation class should close this architecture while preserving the exact supply representation as independent mathematics.

---

# 13. Status

```text
all arithmetic coefficient placement                      CLOSED
lossless source-conditioned supply realization             ✓[M]
fixed-window IN/OUT identity                               ✓[M]
forward C1 contraction                                     ?[O]
Object X / NP-GAP / RH                                    ?[O]
```

No Registry change.
