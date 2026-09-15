# P11 Audit — Covariance/precision duality on the same OU state

**Datum:** 15. September 2026

## Result

Fix a prime `p` and put

```math
q=p^{-1/2},
\qquad s_q=\sqrt{1-q^2}.
```

For the Weil-normalized jump channels

```math
X_k
=\sqrt{\log p}\,p^{-k/4}K_{k\log p}v,
```

define the existing P11 tail state

```math
Y_m
=s_q\sum_{k\ge m}q^{k-m}X_k.
```

Then

```math
Y_m-qY_{m+1}=s_q X_m.
```

The P11 hub coordinate is

```math
\boxed{
H_p:=\sum_{k\ge1}q^kX_k
=\frac{q}{s_q}Y_1.
}
```

Therefore Hub + Rest is exactly the state norm

```math
\boxed{
\mathcal E_{P11}(Y)
=\sum_{m\ge1}\|Y_m\|^2
+\frac{q^2}{1-q^2}\|Y_1\|^2.
}
```

By the already established factorization `R_q=T_q^*T_q+uu^*`, this equals the P11 AR(1) covariance form on the channel vector `X`.

On the **same state** the canonical inverse-covariance/precision form is

```math
\boxed{
\mathcal P(Y)
=\frac1{1-q^2}
\sum_{m\ge1}\|Y_m-qY_{m+1}\|^2
=\sum_{m\ge1}\|X_m\|^2.
}
```

The final quantity is exactly the positive full p-power COMMON-JUMP/Weil channel energy.

Thus the P11 prime geometry and the positive Weil prime tower are not two unrelated feature metrics: they are the covariance and precision/Dirichlet forms of one and the same AR(1)/OU tail state.

**Status:** exact identity `✓[M]`; no lower-frame/RH conclusion.

---

## Continuous counterpart

For the universal field

```math
X_v(t)=e^{-t/4}K_tv
```

set

```math
Y(u)=\int_u^\infty e^{-(t-u)/2}X_v(t)dt.
```

Then

```math
(1/2-\partial_u)Y=X_v,
```

and the continuous precision is

```math
\boxed{
\int_0^\infty\|X_v(t)\|^2dt
=\int_0^\infty\|Y'(u)-Y(u)/2\|^2du.
}
```

The left side is exactly the Gamma ground energy.

The stationary Critical-half OU kernel on the half-line has the natural Robin root condition. The corresponding precision quadratic form can equivalently be written as the Critical-half Dirichlet form with its root boundary mass.

Hence:

```text
P11 Hub+Rest        = discrete OU covariance/state geometry
Prime jump tower    = discrete OU precision geometry
Gamma ground        = continuous OU precision geometry
NULLPOL source      = Critical-half precision/range geometry in x
```

This is an exact duality statement, not a positivity proof for the centered Weil form.

---

## Why this does not contradict the primewise contraction no-go

The earlier hard audit proved that the P11 tail transform `T_q` is neither contractive nor expansively ordered relative to the bare channel norm on the physical translation-generated range.

No contraction is asserted here. Instead the state space carries two different canonical metrics:

```math
\mathcal E_{P11}
\quad\text{and}\quad
\mathcal P.
```

The second is forced by the inverse AR(1) covariance / local difference operator. Thus the bridge is metric duality, not feature shorting.

---

## Immediate spectral bound

Since the AR(1) covariance spectrum lies in

```math
[(1-q)/(1+q),(1+q)/(1-q)],
```

one has the canonical comparison

```math
\sum_k\|X_k\|^2
\ge\frac{1-q}{1+q}\langle X,R_qX\rangle.
```

This bound is exact at the spectral level but is not by itself sharp enough to close the global Weil threshold. Its role is only to record the canonical relation between the two metrics.
