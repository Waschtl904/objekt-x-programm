# P11 Audit — Universal stopped OU kernel and critical-half precision duality

**Datum:** 15. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** theorem-level Verdichtung der gestoppten P11-Filtration.  
**Registry:** unveraendert.  
**Nonclaim:** kein Object-X-/Weil-/RH-Abschluss; Whitening allein ist kein Fortschritt.

---

## 0. Kurzurteil

Die gestoppte P11-Kovarianz ist die exakte Gitterabtastung eines **universellen**, primzahlunabhaengigen Critical-half-OU-Kerns

```math
\boxed{
G_L(s,t)
=
\exp\left(-\frac{s+t}{2}+\min(s,t,L)\right),
\qquad s,t,L\ge0.
}
```

Seine Entwicklung in der Stopptiefe `L` ist positiv Rang eins:

```math
\boxed{
\partial_LG_L(s,t)
=
\mathbf1_{L<\min(s,t)}
 e^{-(s-L)/2}e^{-(t-L)/2}.
}
```

P11 entsteht exakt durch

```math
s=j\log p,
\qquad
t=k\log p,
\qquad
L=m\log p.
```

Raeumlich ist die Stopptiefe

```math
L=2(R-|x|).
```

Damit ist die P11-Fensterentwicklung eine diskrete Abtastung eines kontinuierlichen positiven Hamiltonianflusses.

Zusaetzlich ist der inverse Kovarianz-/Praezisionsoperator des ungestoppten Kerns erneut

```math
-\partial_t^2+1/4.
```

Dieselbe Critical-half-Masse `1/2` wirkt daher in zwei Variablen:

```text
source variable x:  NULLPOL = Range(-d_x^2+1/4),
channel depth t:    OU covariance precision = -d_t^2+1/4.
```

Der diskrete P11-Innovationsoperator ist die exponentielle Gitterversion des zugehoerigen first-order Faktors.

Status:

```text
universal stopped kernel G_L                          ✓[M]
rank-one positive L-flow                              ✓[M]
P11 exact lattice sampling                            ✓[M]
critical-half precision in channel variable           ✓[M]
discrete-to-continuous first-order precision bridge   ✓[M]
precision metric as Object X                          not claimed
```

---

# 1. Feature realization of the stopped kernel

Let `e_0` be a root vector and let `L^2(0,L)` be the innovation line. Define

```math
\boxed{
\Phi_t^{[L]}
=
e^{-t/2}e_0
\oplus
\left[
\mathbf1_{[0,\min(t,L)]}(u)e^{-(t-u)/2}
\right].
}
```

Then

```math
\begin{aligned}
\langle\Phi_s^{[L]},\Phi_t^{[L]}\rangle
&=e^{-(s+t)/2}
+\int_0^{\min(s,t,L)}e^{-(s-u)/2}e^{-(t-u)/2}du\\
&=e^{-(s+t)/2+\min(s,t,L)}.
\end{aligned}
```

Thus

```math
\boxed{
\langle\Phi_s^{[L]},\Phi_t^{[L]}\rangle=G_L(s,t).
}
```

For `L>=min(s,t)`,

```math
G_L(s,t)=e^{-|s-t|/2},
```

the full critical-half OU/Green kernel.

For `s,t>L`,

```math
G_L(s,t)=e^{-(s-L)/2}e^{-(t-L)/2},
```

which is exactly the covariance of the conditional expectations of the future states given the stopped state at depth `L`.

---

# 2. Positive Hamiltonian flow in L

From the feature formula,

```math
G_{L_2}-G_{L_1}
=
\int_{L_1}^{L_2}
\left[e^{-(s-u)/2}\mathbf1_{u<s}\right]
\left[e^{-(t-u)/2}\mathbf1_{u<t}\right]du
```

for `L_2>L_1`. Hence

```math
\boxed{
G_{L_2}-G_{L_1}\succeq0.
}
```

Differentiating away from the null boundary surfaces gives

```math
\boxed{
\partial_LG_L
=g_Lg_L^*,
\qquad
 g_L(s)=e^{-(s-L)/2}\mathbf1_{s>L}.
}
```

Thus the continuous depth evolution is rank-one positive at every `L`.

This is the continuous counterpart of the discrete P11 identity

```math
R_q^{(m+1)}-R_q^{(m)}=d_{m+1}d_{m+1}^*.
```

---

# 3. Exact P11 sampling

Fix `p`, put

```math
h=\log p,
\qquad
q=e^{-h/2}=p^{-1/2}.
```

At lattice nodes

```math
s=jh,
\qquad
t=kh,
\qquad
L=mh,
```

one gets

```math
\begin{aligned}
G_{mh}(jh,kh)
&=
\exp\left(
-\frac{(j+k)h}{2}+h\min(j,k,m)
\right)\\
&=q^{j+k-2\min(j,k,m)}\\
&=R_q^{(m)}(j,k).
\end{aligned}
```

Therefore

```math
\boxed{
R_q^{(m)}(j,k)=G_{m\log p}(j\log p,k\log p).
}
```

The finite-window P11 prime branch is not merely analogous to a stopped OU process: it is its exact logarithmic lattice sample.

---

# 4. Spatial time parameter

From the P11 masks,

```math
m_p(x)=\left\lfloor\frac{2(R-|x|)}{\log p}\right\rfloor.
```

Hence the sampled continuous stopping depth is

```math
m_p(x)\log p
\le
2(R-|x|)
<
(m_p(x)+1)\log p.
```

Thus the universal continuous depth parameter is canonically

```math
\boxed{L_R(x)=2(R-|x|).}
```

The same inequality `t<L_R(x)` is precisely the two-sided half-translation overlap condition for

```math
K_t=T_{t/2}-T_{-t/2}.
```

This identifies the stopped OU time with the COMMON-JUMP overlap-cone coordinate.

---

# 5. Critical-half precision on the channel ray

On the half-line, the full kernel

```math
G_\infty(s,t)=e^{-|s-t|/2}
```

is the Green kernel of

```math
\boxed{
L_t=-\partial_t^2+\frac14
}
```

with the natural root Robin condition

```math
u'(0)=\frac12u(0).
```

The corresponding positive precision/Cameron-Martin form is

```math
\boxed{
\mathfrak p(u)
=
\int_0^\infty
\left(|u'|^2+\frac14|u|^2\right)dt
+\frac12|u(0)|^2.
}
```

For decaying `u`, this has either first-order representation

```math
\boxed{
\mathfrak p(u)
=
|u(0)|^2+
\int_0^\infty|u'(t)+\tfrac12u(t)|^2dt
=
\int_0^\infty|u'(t)-\tfrac12u(t)|^2dt.
}
```

Thus the same operator `-d^2+1/4` that characterizes NULLPOL in the physical source variable is the inverse covariance of the P11/OU channel variable.

---

# 6. Discrete precision is the exponential-step analogue

For a stationary AR(1) branch

```math
Z_k=qZ_{k-1}+\sqrt{1-q^2}\,\varepsilon_k
```

the normalized innovations are

```math
\boxed{
\varepsilon_k
=
\frac{Z_k-qZ_{k-1}}{\sqrt{1-q^2}}.
}
```

Accordingly, the discrete precision form is local nearest-neighbor:

```math
\boxed{
|Z_0|^2
+
\sum_{k\ge1}
\frac{|Z_k-qZ_{k-1}|^2}{1-q^2}.
}
```

Set `q=e^{-h/2}` and sample a smooth channel field `Z_k=u(kh)`. Then

```math
Z_k-qZ_{k-1}
=h\left(u'(kh)+\frac12u(kh)\right)+O(h^2),
```

while

```math
1-q^2=1-e^{-h}=h+O(h^2).
```

Therefore

```math
\frac{|Z_k-qZ_{k-1}|^2}{1-q^2}
=h\left|u'+\frac12u\right|^2+O(h^2),
```

which is the Riemann-sum discretization of the continuous precision form.

This is the precise discrete/continuous critical-half bridge behind the P11 tail operator.

---

# 7. Important firewall: precision whitening is not by itself Object X

Any strictly positive covariance can formally be whitened by its inverse square root. Therefore the statement

```text
P11 covariance -> precision -> diagonal norm
```

would be vacuous if used only as a change of metric.

The present observation is potentially useful only because the precision is **local and canonical**:

```text
continuous:  -d_t^2+1/4 with a fixed Robin root condition;
discrete:    nearest-neighbor AR(1) innovation difference;
spatial:     stopping time L_R(x)=2(R-|x|).
```

A genuine Object-X step would have to show that these local precision and boundary terms reproduce the Weil/prime-discrepancy coupling with no fitted coefficients and survive the existing Prime-2 calibration witness.

---

# 8. Failed scalar-root repair

A diagnostic on the existing Prime-2 witness shows that applying the local discrete precision to the **masked** P11 Rest output moves the mixed pairing much closer to the Weil target, but not onto it:

```math
\text{masked-precision pairing}
=-\frac{7\sqrt2}{16}\log2,
```

whereas

```math
\text{Weil target}
=-\frac{8\sqrt2}{16}\log2.
```

For that one witness, adding `1/4` of the Hub pairing would fill the gap exactly. This must **not** be promoted: on other source directions the precision defect is not proportional to the Hub.

The abstract reason is already visible at fixed stopping depth `m`. The stopped inverse-tail reconstruction compresses the exterior channel tail to one geometric boundary amplitude, so the difference from the full diagonal tail contains an operator of rank larger than one. A scalar Root correction cannot repair it on all channel data.

Thus the exact `1/4` witness calibration is recorded only as a coincidence/firewall, not as a candidate theorem.

---

# 9. Sharpened next gate

The surviving nontrivial possibility is a genuinely local **boundary-tail system** on the overlap cone, not a scalar Hub patch:

```math
\boxed{
\mathcal C_R
=\{(x,t):0<t<2(R-|x|)\}.
}
```

The universal stopped kernel provides the positive depth flow; the precision operator provides the local channel derivative; the missing exterior tail is a boundary state at `t=2(R-|x|)`.

The next mathematically meaningful test is whether that boundary state can be coupled canonically to the pole-subtracted prime discrepancy / Gamma continuum so that the full Prime-2 calibration is recovered without fitting.
