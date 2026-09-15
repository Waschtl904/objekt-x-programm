# P11 Audit — RP2 source-conditioned Green filtration

**Datum:** 15. September 2026  
**Basis:** P11 source-conditioning filtration + RP2 transverse-kernel bridge at `ac574089215767f3b353fd6d6af0649b4ded454c`.  
**Rolle:** theorem-level kontinuierliche Green-/Shorting-Interpretation der realen P11-Radiusfiltration und ihr kanonischer RP2-Lift.  
**Registry:** unveraendert.  
**Nonclaim:** keine zentrierte Weil-Positivitaet, kein Object-X-Abschluss, kein NP-GAP/RH-Beweis, keine Publikationsneuheit.

---

## 0. Kurzurteil

Die P11 source conditioning ist nicht nur eine diskrete finite-adische Martingalprojektion. Sie ist exakt die Grundzustandskompression eines **kontinuierlichen gestoppten Green-/OU-Featureprozesses**.

Mit

```math
P=\sqrt{\Delta_{RP^2}+1/4}
```

und dem bereits bewiesenen operatorwertigen Sternfeature

```math
V_xh
=(2P)^{-1/2}e^{-Px}h
\oplus
[1_{[0,x]}(s)e^{-P(x-s)}h]
```

definiere fuer eine Stopptiefe `L>=0`

```math
\boxed{
V_x^{(L)}h
:=(2P)^{-1/2}e^{-Px}h
\oplus
[1_{[0,\min(x,L)]}(s)e^{-P(x-s)}h].
}
```

Dann ist der same-branch Gramoperator

```math
\boxed{
\mathcal K_L(x,y)
=(V_x^{(L)})^*V_y^{(L)}
=(2P)^{-1}
 e^{-P[x+y-2\min(x,y,L)]}.
}
```

Fuer den konstanten RP2-Grundzustand `e_0`, `Pe_0=1/2 e_0`, folgt

```math
\boxed{
\langle e_0,\mathcal K_L(x,y)e_0\rangle
=e^{\min(x,y,L)-(x+y)/2}.
}
```

Setzt man

```math
x=j\log p,
\qquad y=k\log p,
\qquad
L=J_{p,R}(u)\log p,
```

erhaelt man exakt den bereits bewiesenen source-conditioned P11-Gram

```math
\boxed{
p^{\min(j,k,J_{p,R}(u))-(j+k)/2}.}
```

Damit ist die reale P11-Radius-/Boundary-Geometrie eine **Grundzustandskompression einer kanonischen RP2-wertigen Green-Filtration**.

Status:

```text
continuous stopped OU/Green feature identity                 ✓[M]
P11 conditioned Gram = ground-state compression              ✓[M]
full-overlap limit recovers RP2/P11 kernel                    ✓[M]
J=0 boundary degeneration = root-only kernel                  ✓[M]
monotone stopping depth gives positive operator increments    ✓[M]
exact layer increments reproduce P11 innovation filtration    ✓[M]
canonical RP2 lift of source conditioning                     ✓[M]
transverse trace gives conditioned Gamma-like kernel          ✓[M]
correct finite-part/global Weil coupling                       ?[O]
noncommuting point-Weyl mixer compatible with filtration       ?[O]
Object X / NP-GAP / RH                                         ?[O]
```

---

# 1. Windowless operator-valued feature

Let

```math
\mathcal H_Y=L^2(RP^2),
\qquad
P=\sqrt{\Delta_Y+1/4}\ge1/2.
```

The RP2 kernel audit constructs on one prime branch the feature map

```math
V_x:\mathcal H_Y
\to
\mathcal H_Y\oplus L^2(\mathbb R_+;\mathcal H_Y)
```

by

```math
V_xh
=(2P)^{-1/2}e^{-Px}h
\oplus
[1_{[0,x]}(s)e^{-P(x-s)}h].
```

Direct functional calculus gives

```math
V_x^*V_y
=(2P)^{-1}e^{-P|x-y|}.
```

For different prime branches only the common root coordinate overlaps, producing

```math
(2P)^{-1}e^{-P(x+y)}.
```

---

# 2. Stopping the innovations at depth `L`

Fix `L>=0` and let

```math
Q_L
```

be the orthogonal projection on the feature space which preserves

```text
- the common root coordinate;
- branch innovations supported in [0,L];
```

and kills branch innovations on `(L,infty)`.

Then

```math
\boxed{V_x^{(L)}:=Q_LV_x.}
```

Explicitly

```math
V_x^{(L)}h
=(2P)^{-1/2}e^{-Px}h
\oplus
[1_{[0,\min(x,L)]}(s)e^{-P(x-s)}h].
```

Thus the source conditioning is literally a Shorting/projection in the already existing positive Green-feature space.

---

# 3. Closed operator-valued Gram formula

Let

```math
m=\min(x,y,L).
```

The root part contributes

```math
(2P)^{-1}e^{-P(x+y)}.
```

The stopped branch part contributes

```math
\begin{aligned}
\int_0^m
 e^{-P(x-s)}e^{-P(y-s)}ds
&=\int_0^m e^{-P(x+y-2s)}ds\\
&=(2P)^{-1}
\left[
 e^{-P(x+y-2m)}-e^{-P(x+y)}
\right].
\end{aligned}
```

Adding root and branch pieces gives

```math
\boxed{
\mathcal K_L(x,y)
=(2P)^{-1}
 e^{-P[x+y-2\min(x,y,L)]}.
}
```

No approximation and no finite-dimensional truncation is used.

---

# 4. Three geometric regimes

The kernel formula has an immediate geometric interpretation.

## 4.1 Both points before the stop

If

```math
x,y\le L,
```

then

```math
x+y-2\min(x,y,L)=|x-y|,
```

so

```math
\boxed{
\mathcal K_L(x,y)
=(2P)^{-1}e^{-P|x-y|}.
}
```

The full windowless Green kernel is recovered.

## 4.2 One point before, one after

If

```math
x\le L<y,
```

then `min(x,y,L)=x` and again

```math
\boxed{
\mathcal K_L(x,y)
=(2P)^{-1}e^{-P(y-x)}.
}
```

Propagation from the interior point to the exterior point is unchanged.

## 4.3 Both points after the stop

If

```math
L<x,y,
```

then

```math
\boxed{
\mathcal K_L(x,y)
=(2P)^{-1}
 e^{-P(x-L)}e^{-P(y-L)}.
}
```

Beyond the final innovation depth the kernel factorizes through the single boundary state at `L`. The tail is root-like / rank-one in the longitudinal branch coordinate.

This is the continuous Green meaning of the P11 boundary degeneration.

---

# 5. Ground-state compression reproduces P11 exactly

Let `e_0` be the normalized constant RP2 eigenvector. Then

```math
Pe_0=\frac12e_0
```

and

```math
(2P)^{-1}e_0=e_0.
```

Therefore

```math
\begin{aligned}
\langle e_0,
\mathcal K_L(x,y)e_0\rangle
&=e^{-[x+y-2\min(x,y,L)]/2}\\
&=\boxed{
e^{\min(x,y,L)-(x+y)/2}.
}
\end{aligned}
```

For a prime `p`, choose

```math
x=j\log p,
\qquad
y=k\log p,
\qquad
L=J\log p.
```

Then

```math
\begin{aligned}
\langle e_0,
\mathcal K_{J\log p}(j\log p,k\log p)e_0\rangle
&=p^{\min(j,k,J)-(j+k)/2}.
\end{aligned}
```

This is exactly the source-conditioned combined Hub+Rest Prime-Gram from P11.

---

# 6. Source-dependent stopping depth

At source coordinate `u in(-R,R)`, P11 defines

```math
J_{p,R}(u)
=\max\left\{0,
\left\lfloor
\frac{2(R-|u|)_+}{\log p}
\right\rfloor
\right\}.
```

Define the continuous stop

```math
\boxed{
L_{p,R}(u)
:=J_{p,R}(u)\log p.
}
```

Then for every pair of Prime-Power indices `j,k` the P11 conditioned Gram is the ground compression of

```math
\boxed{
\mathcal K_{p,R,u}(j,k)
:=
\mathcal K_{L_{p,R}(u)}
(j\log p,k\log p).
}
```

Thus the discrete Martingal-depth variable is exactly a quantized stopping depth in logarithmic Green distance.

---

# 7. J=0 gives the root-only boundary block

At a boundary point where

```math
J_{p,R}(u)=0,
```

we have `L=0`. Therefore

```math
\mathcal K_0(x,y)
=(2P)^{-1}e^{-P(x+y)}.
```

Ground-state compression yields

```math
\boxed{
e^{-(x+y)/2}.}
```

At `x=j log p`, `y=k log p` this is

```math
p^{-(j+k)/2},
```

exactly the rank-one P11 Root-Gram at the source boundary.

The P11 loss of pointwise coercivity at `J=0` is therefore the ground-state shadow of an exact **stopped Green factorization**.

---

# 8. Full-overlap gives the complete RP2 Green kernel

If

```math
L\ge\min(x,y),
```

then

```math
\mathcal K_L(x,y)
=(2P)^{-1}e^{-P|x-y|}.
```

Thus the P11 Full-overlap gate is exactly the point where the stopped feature no longer changes the covariance of that pair.

In the discrete Prime-Power variables this condition is

```math
J_{p,R}(u)\ge\min(j,k),
```

which is precisely the already proved P11 criterion for recovery of the full AR(1) Gram.

---

# 9. Monotonicity in stopping depth

If

```math
0\le L_1\le L_2,
```

then the feature projections satisfy

```math
Q_{L_1}\preceq Q_{L_2}.
```

Hence for every finite collection `x_1,...,x_n` and transverse vectors `h_i`,

```math
\sum_{i,j}
\langle h_i,
[\mathcal K_{L_2}(x_i,x_j)-\mathcal K_{L_1}(x_i,x_j)]h_j\rangle
\ge0.
```

So the kernel increment is positive semidefinite in the Gram sense:

```math
\boxed{
\mathcal K_{L_2}-\mathcal K_{L_1}\succeq_{Gram}0.
}
```

This is the continuous operator-valued origin of the discrete positive rank-one innovation increments in P11.

---

# 10. Exact infinitesimal/layer increment

At the feature level,

```math
Q_{L_2}-Q_{L_1}
```

is simply the orthogonal projection onto innovations supported in

```math
(L_1,L_2].
```

Accordingly

```math
\begin{aligned}
&\mathcal K_{L_2}(x,y)-\mathcal K_{L_1}(x,y)\\
&\qquad=
\int_{L_1}^{L_2}
1_{\{s\le x\}}
1_{\{s\le y\}}
 e^{-P(x-s)}e^{-P(y-s)}ds.
\end{aligned}
```

This is manifestly a positive operator-valued Gram increment.

If `L_1=(ell-1)log p` and `L_2=ell log p`, ground-state sampling at `j log p,k log p` reproduces exactly the `ell`-th P11 Martingal-layer increment.

Thus the discrete rank-one vectors `v_{p,ell}` are the ground-state lattice samples of continuous Green innovations on the slab

```math
((\ell-1)\log p,\ell\log p].
```

---

# 11. Cross-prime Root coupling is untouched by source stopping

For different prime branches `p!=r`, the innovation spaces are orthogonal. Only the common root coordinate overlaps.

Therefore the operator-valued cross-prime kernel remains

```math
\boxed{
\mathcal K_{cross}(x,y)
=(2P)^{-1}e^{-P(x+y)},
}
```

independent of the stopping depths on the individual branches.

Ground compression gives

```math
e^{-(x+y)/2},
```

and at Prime-Power nodes

```math
p^{-j/2}r^{-k/2},
```

exactly the P11 cross-prime Hub-Gram.

This explains why source conditioning changes the prime-specific innovation blocks but not the universal Root correlation.

---

# 12. Transverse trace: a conditioned Gamma-like kernel

For a positive effective distance

```math
\delta_L(x,y)
:=x+y-2\min(x,y,L)>0,
```

the transverse trace is

```math
\begin{aligned}
\operatorname{Tr}_{RP^2}
\mathcal K_L(x,y)
&=\sum_{m\ge0}
e^{-\mu_m\delta_L(x,y)}\\
&=\boxed{
\frac{e^{-\delta_L(x,y)/2}}
{1-e^{-2\delta_L(x,y)}}
}.
\end{aligned}
```

Thus the same source-stopping geometry canonically lifts the P11 ground channel to the full Gamma ladder.

At `delta_L=0` the transverse trace diverges, exactly as expected from the 2D diagonal singularity; operator-valued `K_L(x,x)` itself remains bounded as `(2P)^{-1}` but is not trace class.

### Firewall

This trace identity defines a natural **conditioned Gamma-like kernel**. It is not yet proved to be the actual finite-window archimedean COMMON-JUMP form. The known Gamma backbone is source-radius invariant under zero extension; any use of this conditioned trace in the final form requires a separate identity/no-go.

---

# 13. Canonical RP2 lift of the P11 radius filtration

The previous P11 filtration theorem says:

```text
R increases
 -> J_{p,R}(u) increases
 -> one new finite-adic innovation level appears at a time.
```

The current theorem gives an exact continuous lift:

```text
R increases
 -> L_{p,R}(u)=J log p increases
 -> the orthogonal Green-innovation subspace [0,L] increases.
```

Each discrete source-conditioned P11 Gram is therefore the ground-state compression of a member of one fixed positive operator-valued filtration

```math
\boxed{
\{\mathcal K_L\}_{L\ge0}.
}
```

No new radius-dependent transverse parameter is introduced.

---

# 14. Relation to the local star bulk

The windowless limit `L=infty` is the exact Green kernel of the local RP2 star-bulk operator with running root condition

```math
\sum_jf_j'(0)=(2-N)Pf(0).
```

Finite `L` does **not** correspond here to simply cutting the metric edge and imposing an ordinary local boundary condition at `L`: beyond `L` the covariance becomes a rank-one deterministic tail rather than an independent reflected Green region.

The correct interpretation is therefore

```text
local windowless star bulk
+
orthogonal Shorting of branch-innovation features beyond L.
```

This distinction prevents an unjustified local-boundary-condition claim.

---

# 15. What this solves for the RP2/P11 coupling

Before this audit the RP2 lift reproduced the windowless P11 Tree Gram, while the actual source-conditioned finite-window P11 remained a separate layer.

Now:

```math
\boxed{
\text{actual source-conditioned P11 Gram}
=
\text{ground-state compression of }\mathcal K_{L_{p,R}(u)}.
}
```

Thus the RP2 transverse geometry is compatible not only with the asymptotic/windowless ledger but with the **real finite-window radius filtration**.

This removes one important type/radius objection to the RP2 route.

---

# 16. What remains open

The lift is diagonal in the `P`-eigenbasis. Therefore it does not by itself create the noncommuting Gamma-mode mixer isolated in the Point-Weyl audit.

Open:

```text
1. whether the point-Weyl mixer M_y can be inserted compatibly with the stopped projections Q_L;
2. whether such insertion preserves the R<S direct system;
3. whether the transverse trace/finite part then reproduces the actual archimedean backbone rather than a new conditioned one;
4. whether the P11 Feshbach shorting of the lifted features has the total Boundary-Weyl self-energy as its residual form;
5. centered Weil positivity.
```

---

# 17. Forschungsurteil

The source-dependent finite-adic P11 geometry has acquired an exact continuous Green meaning:

```text
finite-adic martingale depth J
        =
logarithmic Green innovation stop L=J log p.
```

The resulting kernel

```math
(2P)^{-1}e^{-P[x+y-2min(x,y,L)]}
```

simultaneously contains

```text
P11 source-conditioned Gram  -> ground-state compression,
Gamma-mode lift              -> transverse spectrum/trace,
radius monotonicity          -> nested orthogonal feature projections.
```

This is a genuine Forward-architecture improvement.

The next sharp gate is whether the **noncommuting point-Weyl mixer** and the **source-stopped Green filtration** admit one common radius-compatible Feshbach/Shorting construction. No claim of such a construction is made here.
