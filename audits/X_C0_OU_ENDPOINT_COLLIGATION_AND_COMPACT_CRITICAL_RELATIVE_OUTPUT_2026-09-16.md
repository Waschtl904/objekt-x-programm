# X-C0 — OU endpoint colligation and compact Critical-half relative output

**Datum:** 16. September 2026  
**Basis:** X-C0 #137 / stacked audit #138; stopped RP2 Green filtration #135; safe prime-base transport cells from the earlier stacked audit.  
**Registry:** unverändert.  
**Nonclaim:** noch keine Identitaet dieses Outputs mit dem centered Weil-Readout; kein C1-/Object-X-/NP-GAP-/RH-Abschluss.

---

## 0. Kurzurteil

Der bisher nur als Leitregel formulierte Mechanismus

```text
RELATIVE CANCELLATION FIRST;
CRITICAL-HALF OUTPUT SECOND
```

besitzt jetzt eine **kanonische positive 2-Port-Realisierung** und einen echten funktionalanalytischen PASS.

Der gestoppte Critical-half-OU-Prozess wird an Root und bewegtem Stop-Endpunkt als positive 2-Port-Kolligation geschrieben. Zwei Stop-Tiefen `h` und `L` koennen ihren Endpunkt **vor** der Elimination gemeinsam benutzen. Das positive Shorting erzeugt dann coefficient-free die relative Rootenergie

```math
\boxed{
R_P(h,L)
=
2P\,
[2-e^{-2Ph}-e^{-2PL}]^{-1}
(e^{-Ph}-e^{-PL})^2
\succeq0.
}
```

Auf dem Critical-half-Grundmodus wird die gefaehrliche getrennte Verstärkung

```math
e^{h/2}e^{-h/2},\qquad e^{L/2}e^{-L/2}
```

nicht ausgefuehrt. Zuerst entsteht

```math
e^{-h/2}-e^{-L/2},
```

und erst danach der kritische Output

```math
\boxed{
e^{L/2}(e^{-h/2}-e^{-L/2})
=e^{(L-h)/2}-1.
}
```

Fuer die kanonischen Prime-base-Massentransportzellen

```math
h_p=\log p,
\qquad
I_p=[s_{p^-},s_p),
\qquad
|I_p|=a_p=\frac{\log p}{p-1},
```

mit

```math
\delta_p:=\sup_{L\in I_p}|L-h_p|\to0,
```

folgt daher ein **beschraenkter kompakter Critical-half-Relativoperator**.

Noch staerker gilt dies operatorwertig fuer

```math
P=\sqrt{\Delta_{RP^2}+1/4}\ge1/2:
```

```math
\boxed{
C_{p,L}
:=e^{L/2}(e^{-Ph_p}-e^{-PL})
}
```

definiert zellweise einen kompakten Operator

```math
\boxed{
\mathcal C_{crit}:
\ell^2(a_p;L^2(RP^2))
\longrightarrow
L^2((\gamma,\infty),dL;L^2(RP^2)).
}
```

Damit ist die fruehere Unbeschraenktheits-Firewall **nicht** das Ende der Architektur: sie gilt nur fuer getrennte diagonale Critical-half-Lifts. Nach der kanonischen OU-Endpunkt-Ausloeschung wird der Critical-half-Output sogar kompakt.

Status:

```text
OU Root/stop-endpoint 2-port precision                  ✓[M]
common-endpoint positive relative Shorting              ✓[M]
coefficient-free relative root energy R_P(h,L)           ✓[M]
ground Critical-half relative lift bounded/compact       ✓[K/M]
full RP2 transverse Critical relative lift compact       ✓[K/M]
identity with J_Delta / exact Weil residual              ?[O]
Prime-2 quartet reproduction by final readout            ?[O]
positive C1 / Object X / RH                               ?[O]
```

---

# 1. Exact OU endpoint precision

Fix first a scalar mass `mu>0` and an interval `[0,L]`.

For boundary values

```math
a=f(0),
\qquad b=f(L),
```

the minimizer of

```math
\int_0^L(|f'|^2+\mu^2|f|^2)dx
```

is the massive harmonic interpolant. Its Dirichlet-to-Neumann energy is

```math
\mu
\begin{pmatrix}
\coth(\mu L)&-\operatorname{csch}(\mu L)\\
-\operatorname{csch}(\mu L)&\coth(\mu L)
\end{pmatrix}.
```

The stopped OU process of PR #135 is stationary at the root and retains the full decaying tail beyond `L`. These two exterior pieces contribute respectively

```math
\mu|a|^2,
\qquad
\mu|b|^2.
```

Hence the exact two-endpoint precision is

```math
\boxed{
\Lambda_{\mu,L}
=\mu
\begin{pmatrix}
\coth(\mu L)+1&-\operatorname{csch}(\mu L)\\
-\operatorname{csch}(\mu L)&\coth(\mu L)+1
\end{pmatrix}.
}
```

Its determinant is positive and direct inversion gives

```math
\boxed{
\Lambda_{\mu,L}^{-1}
=\frac1{2\mu}
\begin{pmatrix}
1&e^{-\mu L}\\
e^{-\mu L}&1
\end{pmatrix}.
}
```

This is exactly the root/stop-endpoint covariance obtained by evaluating the stopped Green kernel from #135 at `0` and `L`.

Thus the moving stop boundary is not an ad hoc new degree of freedom: it is the minimal two-point precision representation of the already proved stopped OU covariance.

---

# 2. Conditional-transition form

Equivalently set

```math
E_L=e^{-\mu L},
\qquad
C_L=\frac{2\mu}{1-e^{-2\mu L}}.
```

Then

```math
\boxed{
\langle(a,b),\Lambda_{\mu,L}(a,b)\rangle
=2\mu|a|^2
+C_L|b-E_La|^2.
}
```

Interpretation:

```text
root prior precision                  2 mu,
OU transition root -> stop endpoint  E_L,
innovation precision                  C_L.
```

Eliminating `b` gives exactly the invariant root precision `2mu`.

This explains at precision level why the root covariance in #135 is independent of the stopping depth.

---

# 3. Two stop lengths with one common endpoint

Take two OU transitions from the **same** root value `a`, of lengths `h` and `L`, but force them to use a common endpoint variable `b`.

Do not duplicate the root prior. The positive energy is

```math
\boxed{
2\mu|a|^2
+C_h|b-E_ha|^2
+C_L|b-E_La|^2.
}
```

This is coefficient-free: all numbers are fixed by the two OU propagators.

Weighted least squares gives

```math
\begin{aligned}
&C_h|b-E_ha|^2+C_L|b-E_La|^2\\
&=(C_h+C_L)|b-\bar E a|^2
+\frac{C_hC_L}{C_h+C_L}|E_h-E_L|^2|a|^2,
\end{aligned}
```

where

```math
\bar E=\frac{C_hE_h+C_LE_L}{C_h+C_L}.
```

After Shorting/eliminating the common endpoint, the root precision becomes

```math
2\mu+R_\mu(h,L),
```

with

```math
\boxed{
R_\mu(h,L)
=\frac{C_hC_L}{C_h+C_L}
(E_h-E_L)^2.
}
```

Substituting `C_h,C_L` gives

```math
\boxed{
R_\mu(h,L)
=
\frac{2\mu\,[e^{-\mu h}-e^{-\mu L}]^2}
{2-e^{-2\mu h}-e^{-2\mu L}}
\ge0.
}
```

It vanishes iff `h=L`.

This is the exact positive storage cost of forcing two OU delays to identify **before** endpoint elimination.

That is the desired local meaning of `cancel-first`.

---

# 4. Operator-valued RP2 lift

Let

```math
P=\sqrt{\Delta_{RP^2}+1/4}\ge1/2.
```

All scalar functions above are bounded Borel functions of `P` for positive `h,L`; hence functional calculus gives

```math
E_L=e^{-PL},
```

```math
C_L=2P(I-e^{-2PL})^{-1},
```

and

```math
\boxed{
R_P(h,L)
=
2P[2-e^{-2Ph}-e^{-2PL}]^{-1}
(e^{-Ph}-e^{-PL})^2
\succeq0.
}
```

The operator acts only in the transverse RP2 factor and contains no fitted scalar.

The same construction therefore applies simultaneously to the P11 ground mode and all higher Gamma modes.

---

# 5. Ground-mode Critical-half cancellation

On the constant RP2 mode

```math
Pe_0=\frac12e_0.
```

The two root-to-endpoint amplitudes are

```math
e^{-h/2},
\qquad e^{-L/2}.
```

The plain separate Critical-half lift multiplies each energy by `e^{h/2}` or `e^{L/2}` and is unbounded globally; this is the previously proved firewall.

The common-endpoint colligation instead first creates the **amplitude difference**

```math
e^{-h/2}-e^{-L/2}.
```

Use `L` as the reference-output coordinate and only then apply the Critical-half amplitude factor `e^{L/2}`:

```math
\boxed{
\chi(h,L)
:=e^{L/2}
(e^{-h/2}-e^{-L/2})
=e^{(L-h)/2}-1.
}
```

Hence

```math
|\chi(h,L)|
\le e^{|L-h|/2}-1.
```

If `|L-h|->0`, the critical output goes to zero.

This is the exact cancellation mechanism missing from the diagonal lift.

---

# 6. Prime-base transport cells

From the preceding stacked audit, set

```math
h_p=\log p,
\qquad
a_p=\frac{\log p}{p-1},
```

and define monotone equal-mass cells

```math
I_p=[s_{p^-},s_p),
\qquad |I_p|=a_p,
```

with the canonical initial Euler block `[0,gamma)`.

The classical unconditional PNT input gives

```math
\delta_p
:=\sup_{L\in I_p}|L-h_p|
\longrightarrow0.
```

Indeed the stronger summability

```math
\sum_pa_p\delta_p<\infty
```

was already established on this branch.

---

# 7. Compact ground Critical-half relative output

Let

```math
\mathscr H_P^{root}
:=\ell^2(a_p)
```

with norm

```math
\|c\|^2=\sum_pa_p|c_p|^2.
```

Define

```math
(\mathcal C_0c)(L)
:=
[e^{(L-h_p)/2}-1]c_p,
\qquad L\in I_p.
```

Then

```math
\|\mathcal C_0c\|_{L^2(dL)}^2
=
\sum_p|c_p|^2
\int_{I_p}|e^{(L-h_p)/2}-1|^2dL.
```

On the p-th coordinate the squared singular value relative to the input weight is

```math
\boxed{
\sigma_p^2
=\frac1{a_p}
\int_{I_p}|e^{(L-h_p)/2}-1|^2dL.
}
```

Since

```math
\sigma_p
\le e^{\delta_p/2}-1
\longrightarrow0,
```

one obtains

```math
\boxed{
\mathcal C_0:\ell^2(a_p)\to L^2(dL)
\text{ is bounded and compact}.
}
```

The finitely many initial cells cause no difficulty; asymptotically the block singular values tend to zero.

This is the first rigorous bounded Critical-half output produced **after** the safe discrete/continuum cancellation.

---

# 8. Full RP2 transverse Critical output

Define on `L in I_p`

```math
\boxed{
C_{p,L}
:=e^{L/2}(e^{-Ph_p}-e^{-PL}).
}
```

Consider

```math
\mathcal C_{RP2}:
\ell^2(a_p;\mathcal H_Y)
\to
L^2((\gamma,\infty),dL;\mathcal H_Y),
```

```math
(\mathcal C_{RP2}c)(L)=C_{p,L}c_p,
\qquad L\in I_p.
```

We show that the cell operator norms tend to zero.

Let

```math
\delta=|L-h_p|,
\qquad m=\min(L,h_p).
```

For a spectral value `mu>=1/2` of `P`, the scalar multiplier is

```math
e^{L/2}|e^{-\mu h_p}-e^{-\mu L}|.
```

By the mean-value bound

```math
|e^{-\mu h}-e^{-\mu L}|
\le\mu\delta e^{-\mu m}.
```

For sufficiently large `p`, `m>=2` and `delta<=1`. Then

```math
\begin{aligned}
e^{L/2}|e^{-\mu h_p}-e^{-\mu L}|
&\le
\mu\delta
e^{-(\mu-1/2)m}e^{\delta/2}.
\end{aligned}
```

For `m>=2`, the function

```math
\mu\mapsto \mu e^{-(\mu-1/2)m}
```

is decreasing on `mu>=1/2`, hence bounded by `1/2`. Therefore

```math
\boxed{
\|C_{p,L}\|
\le\frac12e^{\delta_p/2}\delta_p
\longrightarrow0.
}
```

The finite set of cells with `m<2` has finite operator norm separately.

Thus the relative block norm

```math
\sigma_p^{RP2}
:=
\left(
\frac1{a_p}
\int_{I_p}\|C_{p,L}\|^2dL
\right)^{1/2}
```

satisfies

```math
\sigma_p^{RP2}\to0.
```

Since the cells are orthogonal in `L^2(dL)`, the operator is block diagonal across `p`; consequently

```math
\boxed{
\mathcal C_{RP2}
\text{ is bounded and compact}.
}
```

This uses only the spectral lower bound `P>=1/2` and the unconditional transport localization `delta_p->0`.

---

# 9. Relation to the positive relative Shorting energy

The intrinsic shorted root energy is `R_P(h,L)` from §4.

Its square-root output is, mode by mode,

```math
R_\mu(h,L)^{1/2}
=
\left[
\frac{2\mu}{2-e^{-2\mu h}-e^{-2\mu L}}
\right]^{1/2}
|e^{-\mu h}-e^{-\mu L}|.
```

After the same Critical-half factor `e^{L/2}`, this remains bounded and tends to zero cellwise as `p->infty`; the additional square-root prefactor grows only polynomially in `mu`, while the exponential `e^{-\mu m}` controls the transverse high modes.

Thus the compactness is not an artifact of omitting the OU innovation metric: the actual positive common-endpoint Shorting has the same cancel-first regularization mechanism.

---

# 10. What this solves — and what it does not

Solved:

```text
Can the safe root/OU discrete-continuum geometry survive the Critical-half
amplification after a canonical pre-cancellation?
```

Answer:

```math
\boxed{\text{YES, boundedly and even compactly.}}
```

This directly repairs the earlier diagonal-lift obstruction **within a new, narrower architecture**.

Not solved:

```text
- Does the compact relative endpoint output equal J_Delta or the exact
  centered Prime/Gamma transfer?
- How is the output coupled to the already-correct X-C0 Jump/Euler ports?
- Does the resulting full source-conditioned Schur complement reproduce
  Gamma_a on f,g,f+g,f-g?
- Is the full C1 parent positive on every window?
```

No such identity is inferred from compactness alone.

---

# 11. Updated minimal C1 gate

The smallest now-viable coefficient-free construction is:

```text
A. X-C0 common memory supplies the exact Jump/Gamma/pole ports.
B. Stopped RP2 OU geometry supplies a root and moving endpoint state.
C. Prime-base monotone cells pair h_p with continuum L before elimination.
D. The paired endpoints are identified inside one positive OU 2-port parent.
E. Only the resulting relative endpoint difference is Critical-half lifted.
F. The final readout must be derived from this compact relative output plus
   the existing ports, then tested on f,g,f+g,f-g.
```

The next destructive task is no longer boundedness. Boundedness/compactness has passed.

The next task is **exact coefficient identity**:

```math
\boxed{
\text{Does the canonical endpoint-relative output reproduce the required}
\quad J_\Delta / \Gamma_a\quad\text{bookkeeping?}
}
```

If not, the architecture must be closed rather than rescaled after the fact.

---

# 12. Status

```text
cancel-first Critical-half boundedness obstruction       CLOSED / PASS
exact relative endpoint-to-Weil identity                 ?[O]
Prime-2 quartet                                           ?[O]
positive C1 readout                                       ?[O]
Object X / RH                                             ?[O]
```

No Registry change.
