# P11 Audit — Stopped-OU interior norm rate and Strong-Terminal boundary mechanism

**Datum:** 15. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** theorem-level Konvergenzfolge der gestoppten OU-Filtration.  
**Registry:** unveraendert.  
**Nonclaim:** keine neue globale P11-/Weil-Konvergenz ueber bereits dokumentierte Firewall hinaus; die Aussage betrifft den Kanal-Gram und erklaert den Strong-vs-Norm-Mechanismus.

---

## 0. Kurzurteil

Der gestoppte normalisierte AR(1)-Kern konvergiert mit wachsender Innovationstiefe **stark, aber nicht in Operatornorm** zum vollen AR(1)-Kern. Die fehlende Kovarianz ist lediglich in immer hoehere Kanalindizes verschoben und behaelt ihre Norm.

Nach Einsetzen der echten Weilgewichte aendert sich die Lage im festen Innenraum: der physikalische Prime-Kanal-Gram konvergiert dort sogar exponentiell in Operatornorm. Gleichmaessig ueber alle Primzahlen gilt fuer eine sichtbare kontinuierliche Tiefe `L>=2`

```math
\boxed{
\sup_p
\|C_p-C_p^{(m_p(L))}\|
\le
C_0 L e^{-L/2},
}
```

mit dem expliziten universellen Faktor

```math
C_0=\frac{1+2^{-1/2}}{1-2^{-1/2}}.
```

Auf dem gesamten wachsenden Raum kann trotzdem keine solche Normkonvergenz aus diesem Argument folgen, weil die bewegte Fensterrandzone stets Punkte mit Stopptiefe `L_R(x) approx 0` enthaelt. Fuer jeden festen kompakten Source-Vektor wandert diese schlechte Zone dagegen nach aussen. Genau dies ist der geometrische Mechanismus hinter **Strong-Terminal statt globaler Operatornorm-Konvergenz**.

Status:

```text
normalized stopped AR1 -> full AR1 strongly             ✓[M]
normalized operator-norm convergence                     ×[M]
weighted fixed-depth prime Gram norm rate                ✓[M]
uniform-in-prime interior rate O(L e^{-L/2})             ✓[M]
boundary layer obstructs global sup-norm mechanism       ✓[M]
compatibility with Strong-Terminal architecture          ✓[M]_part
```

---

# 1. Normalized covariance tail

Recall

```math
R_q(j,k)=q^{|j-k|},
```

and the stopped covariance

```math
R_q^{(m)}(j,k)
=q^{j+k-2\min(j,k,m)}.
```

The innovation vectors are

```math
(d_r)_j
=\sqrt{1-q^2}q^{j-r}\mathbf1_{j>=r}.
```

Hence

```math
\boxed{
R_q-R_q^{(m)}
=\sum_{r>m}d_rd_r^*\succeq0.
}
```

For `m=0`,

```math
R_q-R_q^{(0)}
=R_q-uu^*
=T_q^*T_q.
```

For general `m`, the nonzero tail block is obtained from the `m=0` block by the unilateral shift isometry. Therefore

```math
\boxed{
\|R_q-R_q^{(m)}\|
=\|T_q\|^2.
}
```

Since

```math
T_q=\sqrt{1-q^2}(I-qS^*)^{-1},
```

we have

```math
\|T_q\|
=\frac{\sqrt{1-q^2}}{1-q}
=\sqrt{\frac{1+q}{1-q}}.
```

Thus

```math
\boxed{
\|R_q-R_q^{(m)}\|
=\frac{1+q}{1-q}
}
```

for every `m`.

So normalized operator-norm convergence is impossible.

---

# 2. Strong convergence

Let `P_{>m}` be the projection onto channel indices `j>m`. Then

```math
R_q-R_q^{(m)}
=P_{>m}(R_q-R_q^{(m)})P_{>m}.
```

The operators are uniformly bounded in `m`, while

```math
P_{>m}x\to0
```

for every `x in ell^2`. Hence

```math
\boxed{
(R_q-R_q^{(m)})x\to0
}
```

for every fixed `x`.

Therefore

```math
\boxed{R_q^{(m)}\to R_q\quad\text{strongly but not in norm}.}
```

---

# 3. Weil-weighted physical channel Gram

For fixed prime `p`, put

```math
h=\log p,
\qquad
q=p^{-1/2}.
```

The Weil channel weights satisfy

```math
w_{p,j}=hq^j.
```

Let

```math
D_p=\operatorname{diag}_{j>=1}(\sqrt h\,q^{j/2}).
```

Then the physical weighted Gram is

```math
C_p=D_pR_qD_p,
```

and the stopped physical Gram is

```math
C_p^{(m)}=D_pR_q^{(m)}D_p.
```

Therefore

```math
C_p-C_p^{(m)}
=D_p(R_q-R_q^{(m)})D_p.
```

On the tail `j=m+r`,

```math
D_p
=\sqrt h\,q^{m/2}
\operatorname{diag}_{r>=1}(q^{r/2}).
```

Using the normalized tail norm from Section 1,

```math
\begin{aligned}
\|C_p-C_p^{(m)}\|
&\le
hq^m
\left\|\operatorname{diag}(q^{r/2})\right\|^2
\frac{1+q}{1-q}\\
&=
\boxed{
hq^{m+1}\frac{1+q}{1-q}.}
\end{aligned}
```

---

# 4. Continuous boundary depth

For continuous visible depth `L`, the P11 mask gives

```math
m_p(L)=\left\lfloor\frac Lh\right\rfloor.
```

If `h<=L`, then

```math
(m_p(L)+1)h>L,
```

so

```math
q^{m_p(L)+1}
=e^{-(m_p(L)+1)h/2}
<e^{-L/2}.
```

Therefore

```math
\|C_p-C_p^{(m_p(L))}\|
\le
h e^{-L/2}\frac{1+q}{1-q}
\le
L e^{-L/2}C_0,
```

where

```math
C_0
=\frac{1+2^{-1/2}}{1-2^{-1/2}}.
```

If `h>L>=2`, then `m_p(L)=0` and

```math
hq^{m+1}=he^{-h/2}.
```

The function `h e^{-h/2}` is decreasing for `h>=2`, hence

```math
he^{-h/2}
\le
Le^{-L/2}.
```

Thus for every `L>=2`, uniformly over all primes,

```math
\boxed{
\sup_p
\|C_p-C_p^{(m_p(L))}\|
\le
C_0Le^{-L/2}.
}
```

---

# 5. Why this does not give global moving-window norm convergence

In the spatial P11 system the depth is not a fixed `L`; it is

```math
L_R(x)=2(R-|x|).
```

For every radius `R`, points arbitrarily close to the moving boundary have

```math
L_R(x)\approx0.
```

Therefore a global multiplication/direct-integral operator norm, which takes an essential supremum over the spatial fibre, cannot use the large-`L` estimate uniformly across the whole moving window.

By contrast, for a fixed compactly supported source and `R->infty`, every spatial point in the fixed source region satisfies

```math
L_R(x)\to\infty.
```

The local weighted Gram error there decays exponentially. This is precisely the geometry expected for strong convergence on fixed vectors.

---

# 6. Relation to the existing Strong-Terminal front

Earlier P11 research had already identified strong convergence, rather than global operator-norm convergence, as the natural terminal topology for moving-window objects.

The present stopped-OU calculation gives a direct channel-geometric reason:

```text
normalized covariance tail: norm is merely shifted, never shrinks;
Weil weights: interior tail becomes exponentially small;
moving physical boundary: always regenerates a fresh shallow-depth fibre.
```

Thus the stopped-OU interpretation is compatible with, and conceptually explains, the existing Strong-Terminal architecture. It does not by itself prove any additional full spatial intertwining theorem beyond the stated channel-Gram estimates.
