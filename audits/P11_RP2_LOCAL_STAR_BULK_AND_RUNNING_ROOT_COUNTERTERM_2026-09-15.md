# P11 Audit — local RP2 star bulk and the running root counterterm

**Datum:** 15. September 2026  
**Basis:** RP2 transverse-kernel/P11-ground-mode bridge at `ac574089215767f3b353fd6d6af0649b4ded454c`.  
**Rolle:** theorem-level lokale Differentialoperator-Realisierung des operatorwertigen P11/RP2-Sternkerns.  
**Registry:** unveraendert.  
**Nonclaim:** kein unendlicher Prime-Graph, kein Object-X-Abschluss, kein NP-GAP/RH-Beweis, keine Publikationsneuheit.

---

## 0. Kurzurteil

Der operatorwertige Sternbaum-Kern

```math
\mathcal K(\alpha,\beta)
=(2P)^{-1}e^{-P d_T(\alpha,\beta)},
\qquad
P=\sqrt{\Delta_{RP^2}+1/4},
```

ist nicht nur ein abstrakter positiver Kolmogorov-Kern. Fuer jede **endliche** Anzahl `N` von Prime-Aesten ist er exakt der Zero-energy-Resolventenkern eines lokalen positiven Differentialoperators auf einem metrischen `N`-Stern mit `RP^2`-Transversalraum.

Auf jedem Ast wirkt

```math
-\partial_x^2+P^2.
```

Am gemeinsamen Root gelten Kontinuitaet und die operatorwertige Delta-Bedingung

```math
\boxed{
\sum_{j=1}^N f_j'(0)
=(2-N)P f(0).
}
```

Diese Rootbedingung ist innerhalb der permutation-symmetrischen Delta-Klasse **eindeutig** durch den geforderten P11/RP2-Kern bestimmt.

Der resultierende Resolventenkern ist fuer alte Aeste unabhaengig von `N`. Beim Hinzufuegen eines neuen Astes laeuft nur der Root-Counterterm:

```math
\boxed{
A_{N+1}-A_N=-P,
\qquad
A_N:=(2-N)P,
}
```

waehrend

```math
\boxed{NP+A_N=2P}
```

invariant bleibt.

Dies liefert eine exakte lokale **branch-addition covariance**:

```math
\boxed{
J_N^*\mathcal H_{N+1}^{-1}J_N
=\mathcal H_N^{-1}.
}
```

Status:

```text
scalar delta-star Green formula                         classical / ✓[M]
unique alpha_N=(2-N)mu for target kernel               ✓[M]
strict positivity of shifted scalar star               ✓[M]
RP2 operator-valued direct-sum realization             ✓[M]
local kernel = (2P)^-1 exp(-P d_T)                     ✓[M]
P11 = transverse ground-state compression              ✓[M]
Gamma h(d) = transverse trace of same local kernel     ✓[M]
root running law A_{N+1}=A_N-P                         ✓[M]
old-edge resolvent consistency under branch addition   ✓[M]
infinite-prime renormalized vertex operator             ?[O]
source/radius-conditioned P11 realization               ?[O]
Object X / NP-GAP / RH                                  ?[O]
```

---

# 1. Scalar `N`-star with Delta coupling

Let `T_N` be a metric star with edges `R_+`, parametrized outward from the common vertex.

For `mu>0` consider on

```math
\bigoplus_{j=1}^N L^2(\mathbb R_+)
```

the differential expression

```math
-\partial_x^2+\mu^2.
```

The standard permutation-symmetric Delta vertex condition is

```math
f_1(0)=\cdots=f_N(0)=:f(0),
```

and

```math
\boxed{
\sum_{j=1}^N f_j'(0)=\alpha f(0),
\qquad \alpha\in\mathbb R.
}
```

Such Delta couplings are standard self-adjoint quantum-graph boundary conditions. The project does not claim novelty for this framework.

---

# 2. Exact Green kernel for general `alpha`

Fix a source at `y>0` on edge `k`. Away from the source, every square-integrable homogeneous solution is proportional to `e^{-mu x}`.

Use the ansatz

```math
G_{jk}^{(\alpha)}(x,y)
=
\delta_{jk}\frac1{2\mu}e^{-\mu|x-y|}
+
C_{jk}\,e^{-\mu(x+y)}.
```

Vertex continuity forces one common boundary value. Writing

```math
A:=\frac1{N\mu+\alpha},
```

a direct boundary calculation gives

```math
\boxed{
G_{jk}^{(\alpha)}(x,y)
=
\begin{cases}
\dfrac1{2\mu}e^{-\mu|x-y|}
+\left(A-\dfrac1{2\mu}\right)e^{-\mu(x+y)}, & j=k,\\[3mm]
A e^{-\mu(x+y)}, & j\ne k.
\end{cases}
}
```

Indeed the common vertex value is `A e^{-mu y}` and

```math
\sum_j\partial_xG_{jk}^{(\alpha)}(0+,y)
=\alpha A e^{-\mu y}.
```

---

# 3. Exact P11 kernel uniquely fixes the vertex coupling

The desired scalar specialization of the project kernel is

```math
K_{jk}(x,y)
=
\frac1{2\mu}
e^{-\mu d_T((j,x),(k,y))},
```

that is

```math
K_{jk}(x,y)
=
\begin{cases}
\dfrac1{2\mu}e^{-\mu|x-y|}, & j=k,\\[2mm]
\dfrac1{2\mu}e^{-\mu(x+y)}, & j\ne k.
\end{cases}
```

Comparison with the general Delta-star Green formula requires

```math
A=\frac1{2\mu}.
```

Since

```math
A=(N\mu+\alpha)^{-1},
```

this is equivalent to

```math
N\mu+\alpha=2\mu.
```

Hence uniquely

```math
\boxed{
\alpha_N=(2-N)\mu.
}
```

The same equality simultaneously kills the unwanted reflected term on the source edge and fixes the desired cross-edge coefficient.

Thus within the standard symmetric Delta class there is no free coupling parameter left.

---

# 4. Strict positivity of the scalar shifted star

For `N=1`, `alpha_1=mu>0`, so the Robin endpoint is repulsive and

```math
H_{1,\mu}\ge\mu^2>0.
```

For `N=2`, `alpha_2=0`; the two half-lines glue to the free full-line massive operator and again

```math
H_{2,\mu}\ge\mu^2>0.
```

For `N>2`, `alpha_N<0`. The attractive scalar Delta star has at most one symmetric bound state. Writing it as

```math
f_j(x)=c e^{-\kappa x}
```

gives

```math
-N\kappa c=\alpha_Nc,
```

hence

```math
\kappa=\frac{N-2}{N}\mu.
```

After the `+mu^2` shift its eigenvalue is

```math
\begin{aligned}
\mu^2-\kappa^2
&=\mu^2
\left[1-\frac{(N-2)^2}{N^2}\right]\\
&=\boxed{
\frac{4(N-1)}{N^2}\mu^2
}>0.
\end{aligned}
```

Therefore the scalar operator whose inverse kernel is `K` is strictly positive for every finite `N`.

---

# 5. Operator-valued RP2 lift

Let

```math
\mathcal H_Y=L^2(RP^2),
\qquad
P=\sqrt{\Delta_Y+1/4}\ge\frac12.
```

The spectral decomposition of `P` is

```math
P|_{E_m}=\mu_mI,
\qquad
\mu_m=2m+1/2.
```

Consider

```math
\mathscr H_N
=\bigoplus_{j=1}^N
L^2(\mathbb R_+;\mathcal H_Y).
```

Mode by mode in the spectral decomposition of `P`, impose the scalar Delta condition from §3. Equivalently, on the natural operator domain the root conditions are

```math
f_1(0)=\cdots=f_N(0)=:f(0)
```

and

```math
\boxed{
\sum_{j=1}^N f_j'(0)
=(2-N)P f(0).
}
```

Denote the resulting direct-sum self-adjoint operator by

```math
\mathcal H_N.
```

Because every transverse `mu_m` sector is strictly positive and `mu_m>=1/2`, `mathcal H_N` is positive and invertible.

### Domain firewall

The operator-valued boundary condition is defined spectrally/direct-sum-wise; no claim is made here about the most general abstract boundary-pair classification for unbounded operator-valued Robin data.

---

# 6. Exact operator-valued resolvent kernel

Applying the scalar formula on every `P`-eigenspace gives

```math
\boxed{
(\mathcal H_N^{-1})_{jk}(x,y)
=
\begin{cases}
(2P)^{-1}e^{-P|x-y|}, & j=k,\\[2mm]
(2P)^{-1}e^{-P(x+y)}, & j\ne k.
\end{cases}
}
```

In terms of the metric-star distance

```math
d_T((j,x),(k,y))
=
\begin{cases}
|x-y|,&j=k,\\
x+y,&j\ne k,
\end{cases}
```

this is exactly

```math
\boxed{
\mathcal H_N^{-1}(\alpha,\beta)
=(2P)^{-1}e^{-P d_T(\alpha,\beta)}.
}
```

Thus the abstract operator-valued Kolmogorov kernel from the RP2/P11 audit is the actual Green kernel of a local positive star-bulk operator.

---

# 7. P11 and Gamma remain two evaluations of the local kernel

Let `e_0` be the normalized constant RP2 mode, so

```math
Pe_0=\frac12e_0.
```

Then

```math
\boxed{
\langle e_0,
\mathcal H_N^{-1}(\alpha,\beta)e_0\rangle
=e^{-d_T(\alpha,\beta)/2},
}
```

exactly the normalized P11 OU/tree kernel.

Taking the transversale trace gives for positive distance

```math
\boxed{
\operatorname{Tr}_{RP^2}
\mathcal H_N^{-1}(\alpha,\beta)
=
\sum_{m\ge0}e^{-\mu_m d_T}
=
\frac{e^{-d_T/2}}{1-e^{-2d_T}},
}
```

exactly the Gamma COMMON-JUMP density `h(d_T)`.

The same **local** differential operator therefore realizes both previous evaluations.

---

# 8. Running Root-Counterterm

Write the operator-valued Delta strength as

```math
\boxed{A_N=(2-N)P.}
```

Then

```math
\boxed{A_{N+1}-A_N=-P.}
```

The combination entering the scalar Green denominator is

```math
NP+A_N.
```

For the distinguished coupling:

```math
\boxed{NP+A_N=2P}
```

for every `N`.

Thus adding an edge contributes `+P` to the Dirichlet-to-Neumann load and the running root counterterm contributes exactly `-P`. The renormalized root denominator is invariant.

This is an exact finite-`N` cancellation, not an asymptotic statement.

---

# 9. Exact branch-addition covariance

Let

```math
J_N:\mathscr H_N\to\mathscr H_{N+1}
```

be the Hilbert-space embedding that places a vector on the first `N` edges and zero on the new edge.

Although `J_N` does not map the **operator domains** by zero extension because of vertex continuity, compression of the resolvent is well defined.

Since the old-old blocks of the kernel in §6 do not depend on `N`, one has exactly

```math
\boxed{
J_N^*\mathcal H_{N+1}^{-1}J_N
=\mathcal H_N^{-1}.
}
```

This is the correct projective statement: the **Green geometry seen by all old branches is unchanged** when a new branch is added and the root counterterm runs according to `A_{N+1}=A_N-P`.

### Important distinction

This branch-addition covariance is not yet the full source-window covariance `R<S` of P11. Window growth changes not only the number of active primes but also overlap depths, one-sided rest channels and source geometry. The present theorem isolates one exact part of the required radius consistency.

---

# 10. Ground-state scalar root law

Compress the operator-valued root condition to the constant RP2 mode `e_0`.

Since

```math
Pe_0=\frac12e_0,
```

the scalar P11-ground vertex strength is

```math
\boxed{
\alpha_N^{(0)}=\frac{2-N}{2}.
}
```

Thus every newly added prime branch shifts the scalar ground-root coupling by exactly

```math
-\frac12.
```

The same Critical-half mass that controls the P11 edge propagation controls the root counterterm flow.

---

# 11. Infinite-prime limit and renormalization firewall

As `N->infty`, the bare root coefficient

```math
A_N=(2-N)P
```

diverges to `-infty` on every transverse eigenspace.

The finite object is instead the renormalized combination

```math
\boxed{NP+A_N=2P.}
```

This strongly suggests an infinite-degree root must be formulated through a renormalized boundary condition / resolvent limit rather than a naive infinite sum of outward derivatives.

However:

```text
infinite-prime self-adjoint root operator        ?[O]
strong/norm resolvent convergence N->infty       ?[O]
compatibility with actual prime ordering/cutoffs ?[O]
```

No infinite-star theorem is claimed here.

---

# 12. Relation to cutoff gauge

The COMMON-JUMP cutoff gauge says that a newly entering exterior Prime channel contributes a positive diagonal amount which is exactly cancelled by the corresponding threshold shift on old source vectors.

The local star model displays an analogous exact cancellation at the common root:

```text
new branch Dirichlet-to-Neumann load  +P
running root counterterm               -P
------------------------------------------
old-branch Green denominator            unchanged.
```

This is structurally compatible with the project philosophy that new exterior channels should be pure gauge before they overlap the old source.

### Firewall

The two cancellations are not yet proved to be **the same operator identity**. The present result is a local Green/resolvent analogue and a candidate mechanism to test against the source-conditioned P11 connecting maps.

---

# 13. Literature firewall

Metric quantum graphs with Delta vertex couplings, continuity plus

```math
\sum f_j'(0)=\alpha f(0),
```

and resolvent/Green-function constructions are classical. Examples include the standard quantum-graph literature of Exner, Turek, Fulling and many others.

No novelty is claimed for Delta-star operators or their scalar resolvents.

Project-specific new-here synthesis:

```text
RP2 transverse P
+
unique running Delta strength (2-N)P
+
exact local realization of the existing P11/RP2 kernel
+
branch-addition resolvent covariance
```

is recorded for audit only. Publication novelty remains open.

---

# 14. Forschungsurteil

The P11/RP2 kernel now has three equivalent levels:

```text
1. abstract positive operator-valued kernel
   (2P)^-1 exp(-P d_T)

2. explicit Kolmogorov/tree Gram factorization

3. local positive star-bulk Green operator
   -d_x^2+P^2
   with root condition
   sum f_j'(0)=(2-N)P f(0).
```

The third level adds a genuinely new constraint on future Object-X candidates: root gluing cannot be arbitrary if it is to preserve the already proven P11/Gamma kernel. Within the symmetric Delta class the running counterterm is forced.

The next concrete test is therefore:

```math
\boxed{
\text{Does the source-conditioned P11 Feshbach transport induce precisely}
\atop
\text{this running root renormalization on the active-prime star?}
}
```

A positive answer would connect the local bulk directly to the existing radius geometry. A negative answer would give a sharp no-go for this local star realization as the full Object-X mechanism.
