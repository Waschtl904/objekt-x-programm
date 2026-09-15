# P11 Audit — Boundary-tail shorting and universal prime-lattice sampling

**Datum:** 15. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** theorem-level Randzustandsidentitaet fuer die gestoppte OU/P11-Praezision.  
**Registry:** unveraendert.  
**Nonclaim:** kein Object-X-/Weil-/RH-Abschluss; keine Publikationsneuheit.

---

## 0. Kurzurteil

Die endliche Praezisionsform eines gestoppten P11-AR(1)-Astes rekonstruiert **alle inneren nackten Weil-Jump-Kanaele exakt** und komprimiert den gesamten unsichtbaren Aussentail in einen einzigen kontraktiven exponentiellen Randzustand.

Diskret, fuer `q in (0,1)` und

```math
Y_m=\sqrt{1-q^2}\sum_{k\ge m}q^{k-m}X_k,
```

gilt fuer die sichtbaren Zustaende `Y_1,...,Y_m`

```math
\boxed{
\mathfrak p_m(Y)
=
\sum_{r=1}^{m-1}
\frac{\|Y_r-qY_{r+1}\|^2}{1-q^2}
+\|Y_m\|^2
=
\sum_{r<m}\|X_r\|^2+\|Y_m\|^2.
}
```

Dabei

```math
\boxed{
0\le
\sum_{k\ge m}\|X_k\|^2-\|Y_m\|^2.
}
```

Kontinuierlich, fuer

```math
Y(u)=\int_u^\infty e^{-(t-u)/2}X(t)dt,
```

gilt auf `[0,L]`

```math
\boxed{
\mathfrak p_L(Y)
=
\int_0^L\left\|Y'(u)-\frac12Y(u)\right\|^2du
+\|Y(L)\|^2
=
\int_0^L\|X(u)\|^2du+\|Y(L)\|^2,
}
```

und

```math
\boxed{
0\le
\int_L^\infty\|X(t)\|^2dt-\|Y(L)\|^2.
}
```

Der diskrete Randvektor und der kontinuierliche Randvektor sind beide exakt normiert.

Mit dem universellen Feld

```math
\boxed{X_v(t)=e^{-t/4}K_tv}
```

ist jeder Prime-Power-Weilkanal nur eine Gitterabtastung:

```math
\boxed{
\sqrt{w_{p,k}}K_{k\log p}v
=\sqrt{\log p}\,X_v(k\log p).
}
```

Somit sind die P11-Primaste verschiedene logarithmische Gitter desselben kontinuierlichen Critical-half-Jump-Feldes.

Status:

```text
discrete stopped precision/boundary identity            ✓[M]
discrete exterior-tail defect positive                  ✓[M]
continuous stopped precision/boundary identity          ✓[M]
continuous exterior-tail defect positive                ✓[M]
normalized discrete/continuous boundary modes           ✓[M]
all prime branches sample one universal X_v(t)           ✓[M]
prime discrepancy as weighted lattice-count discrepancy ✓[M]
Object-X boundary coupling                               ?[O]
```

---

# 1. Discrete tail transform and its inverse orientation

For a Hilbert-valued square-summable sequence `X=(X_k)_{k>=1}`, define

```math
\boxed{
Y_m
=(T_qX)_m
=\sqrt{1-q^2}\sum_{k\ge m}q^{k-m}X_k.
}
```

Then

```math
Y_m-qY_{m+1}
=\sqrt{1-q^2}X_m,
```

so the correct inverse orientation is

```math
\boxed{
X_m
=\frac{Y_m-qY_{m+1}}{\sqrt{1-q^2}}.
}
```

This orientation matters at a finite stopping boundary.

---

# 2. Natural finite precision and the boundary state

The covariance of the visible vector `(Y_1,...,Y_m)` is the finite Kac--Murdock--Szego matrix

```math
R_q^{[m]}=(q^{|j-k|})_{1<=j,k<=m}.
```

Its inverse quadratic form is

```math
\boxed{
\mathfrak p_m(Y)
=
\sum_{r=1}^{m-1}
\frac{\|Y_r-qY_{r+1}\|^2}{1-q^2}
+\|Y_m\|^2.
}
```

Indeed, expansion gives the standard tridiagonal inverse with endpoint diagonal `1/(1-q^2)` and interior diagonal `(1+q^2)/(1-q^2)`.

Using the inverse tail relation,

```math
\boxed{
\mathfrak p_m(Y)
=
\sum_{r=1}^{m-1}\|X_r\|^2+\|Y_m\|^2.
}
```

Thus every visible interior bare channel is recovered exactly. Only the unobserved tail `X_m,X_{m+1},...` is replaced by one boundary state `Y_m`.

---

# 3. Boundary compression is contractive

The coefficient vector of the boundary tail is

```math
b_m(k)
=\sqrt{1-q^2}\,q^{k-m}\mathbf1_{k>=m}.
```

It has exact norm

```math
\sum_{k>=m}|b_m(k)|^2
=(1-q^2)\sum_{r>=0}q^{2r}=1.
```

Therefore Cauchy--Schwarz gives

```math
\boxed{
\|Y_m\|^2
\le
\sum_{k>=m}\|X_k\|^2.
}
```

Equivalently the missing exterior energy

```math
\boxed{
\mathcal D_m(X)
:=
\sum_{k>=m}\|X_k\|^2-\|Y_m\|^2
\ge0
}
```

is exactly the norm of the component of the tail orthogonal to the normalized exponential boundary mode `b_m`.

This is the finite-dimensional/marginal Schur-shortening mechanism underlying the stopped AR(1) covariance.

---

# 4. Continuous tail transform

Let `X in L^2((0,infty);H)` and define

```math
\boxed{
Y(u)=\int_u^\infty e^{-(t-u)/2}X(t)dt.
}
```

Then in the weak sense

```math
Y'(u)
=-X(u)+\frac12Y(u),
```

hence

```math
\boxed{
X(u)=\left(\frac12-\partial_u\right)Y(u).
}
```

The covariance kernel of the transform of white input is

```math
\int_{\max(s,t)}^\infty
 e^{-(u-s)/2}e^{-(u-t)/2}du
=e^{-|s-t|/2}.
```

Thus this is the same full Critical-half OU kernel.

---

# 5. Continuous stopped precision and boundary shorting

The inverse-covariance form of `e^{-|s-t|/2}` restricted to `[0,L]` is

```math
\int_0^L
\left(\|Y'\|^2+\frac14\|Y\|^2\right)du
+\frac12\|Y(0)\|^2
+\frac12\|Y(L)\|^2.
```

Integration by parts rewrites it as

```math
\boxed{
\mathfrak p_L(Y)
=
\int_0^L
\left\|Y'(u)-\frac12Y(u)\right\|^2du
+\|Y(L)\|^2.
}
```

Using `X=(1/2-partial)Y`,

```math
\boxed{
\mathfrak p_L(Y)
=
\int_0^L\|X(u)\|^2du+\|Y(L)\|^2.
}
```

The continuous boundary mode is

```math
g_L(t)=e^{-(t-L)/2}\mathbf1_{t>=L}
```

with

```math
\|g_L\|_{L^2(dt)}^2=\int_L^\infty e^{-(t-L)}dt=1.
```

Hence

```math
\boxed{
\|Y(L)\|^2
\le
\int_L^\infty\|X(t)\|^2dt
}
```

and the exterior defect is the positive orthogonal-complement energy.

---

# 6. Exact discrete/continuous boundary correspondence

For a lattice step `h>0`, put

```math
q=e^{-h/2}.
```

The discrete boundary coefficients are

```math
\sqrt{1-e^{-h}}\,e^{-(k-m)h/2}.
```

Their `ell^2` norm is exactly one. The continuous boundary coefficient is

```math
e^{-(t-L)/2}\mathbf1_{t>=L},
```

whose `L^2` norm is exactly one.

Thus the discrete P11 boundary state and the continuous Critical-half boundary state are normalized versions of the same exponential tail mode in their respective counting/Lebesgue geometries.

---

# 7. Universal Weil-Jump field sampled by every prime

For `p` set

```math
h_p=\log p,
\qquad
q_p=e^{-h_p/2}.
```

The Weil weight is

```math
w_{p,k}
=(\log p)p^{-k/2}
=h_p e^{-kh_p/2}.
```

Define

```math
\boxed{
X_v(t)=e^{-t/4}K_tv.
}
```

Then

```math
\begin{aligned}
\sqrt{w_{p,k}}K_{kh_p}v
&=\sqrt{h_p}\,e^{-kh_p/4}K_{kh_p}v\\
&=\boxed{\sqrt{h_p}\,X_v(kh_p)}.
\end{aligned}
```

Hence all prime branches sample one and the same continuous channel field; only their logarithmic lattice spacing differs.

Applying the P11 tail transform gives

```math
\boxed{
Y_{p,m}
=
\sqrt{1-e^{-h_p}}
\sum_{k>=m}
 e^{-(k-m)h_p/2}\sqrt{h_p}\,X_v(kh_p).
}
```

This is the exact normalized exponential tail quadrature used by the P11 branch.

---

# 8. Prime measure as a weighted logarithmic lattice comb

Define the logarithmic prime-power counting measure

```math
\boxed{
d\mathcal N_P(t)
=
\sum_{p}\sum_{k>=1}(\log p)\,\delta_{k\log p}(dt).
}
```

Then

```math
\boxed{
d\nu_P(t)=e^{-t/2}d\mathcal N_P(t).}
```

Since the pole compensator is `e^{t/2}dt`, the discrepancy is

```math
\boxed{
d\Delta(t)
=e^{-t/2}\left(d\mathcal N_P(t)-e^t dt\right).}
```

Thus `Delta` is exactly the weighted discrepancy between the union of logarithmic prime lattices and its smooth exponential main density.

This formulation does not make the discrepancy easy: polynomial control is already RH-scale, as recorded in the preceding audit. Its value is geometric: the same depth coordinate `t` carries

```text
- the universal jump field X_v(t),
- every P11 prime lattice,
- the stopped OU boundary mode,
- and the pole-subtracted prime-lattice counting discrepancy.
```

---

# 9. Next gate

The remaining nontrivial construction problem can now be stated without P11-specific index notation:

```math
\boxed{
\text{Given one continuous field }X_v(t)\text{ on the overlap cone,}
\atop
\text{couple its prime-lattice stopped boundary quadratures and the continuous}
\text{Critical-half boundary state in a forward positive system whose}
\text{nonlocal boundary transfer reproduces the }\Delta\text{ pairing.}
}
```

The signed measure itself cannot be a local positive energy density. Any success must occur through a boundary/transfer/spectral-shift mechanism and must pass the exact Prime-2 mixed-pair witness.
