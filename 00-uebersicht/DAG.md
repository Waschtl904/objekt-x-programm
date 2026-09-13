# Abhängigkeitsgraph (DAG) — Objekt X / COMMON-JUMP → NP-OVERLAP

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Aktuelle Front: [CURRENT-FRONT](../CURRENT-FRONT.md).

## 1. Nullpol und COMMON-JUMP

```text
E_-=M(0), E_+=M(1)
        |
        v
D_NP = ker M(0) ∩ ker M(1)
        |
        v
Q_W|NP = X_a^* X_a - Gamma_a I      ✓[M]
```

`X_a` wird aus derselben Familie `K_t=T_{t/2}-T_{-t/2}` mit kontinuierlichem archimedischen Maß und atomaren Prime-Power-Massen gebaut.

## 2. Q0 / Gamma channel

```text
h(t)=sum exp(-alpha_m t), alpha_m=2m+1/2
        |
        v
A_alpha=(2/alpha)L(L+alpha^2)^(-1)    ✓[M]
        |
        v
alpha=1/2, Q0=L+1/4
        |
        v
A_{1/2}Q0=4L                          ✓[M]
        |
        v
Q0 : C_c^infty(-a,a) <-> D_NP(a)      ✓[M]
```

Higher channel:

```text
Schur on compressed resolvent
        |
        v
A_alpha >= (2/alpha)e^{-alpha a} I    ✓[M]
```

## 3. Short-window correction

```text
COMMON-JUMP/Q0 channel bounds
        |
        v
internal short-window coercivity       ✓[M]_part
```

But:

```text
Suzuki Thm 1.4
full local class positive for small a
        |
        v
short-window positivity as NEW theorem   ×[M]
```

The project result is an architectural reproduction, not a novelty claim.

## 4. Exact centering exposes the arithmetic wall

For one Prime atom:

```math
w_n\|K_{\log n}v\|^2-2w_n\|v\|^2
=-2w_n\operatorname{Re}\langle T_{\log n}v,v\rangle.
```

Summing:

```text
Prime feature diagonal
        +
Prime threshold ledger
        |
        | exact cancellation
        v
only inner-shift correlations remain
```

Thus

```math
Q_W(v)=\mathcal A(v)-\mathcal O_a(v),
```

```math
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
```

Status `✓[M]`.

## 5. New main DAG

```text
COMMON-JUMP geometry ✓[M]
        |
        v
centered Prime-overlap identity ✓[M]
        |
        +--> Q0 Sobolev transport ✓[M]
        |
        +--> overlap radius delta_n=2a-log n
        |
        +--> Prime-Power AR(1) / Weil-tail input
        |
        v
(A_infty-kappa_* I)|D_NP >= O_a|D_NP ?[O]
        |
        v
global null-pole Weil positivity
        |
        v
RH
```

## 6. Q0 transport edge

For `v=Q0u`:

```math
Re<T_t v,v>
=Re<T_tu'',u''>
+\frac12Re<T_tu',u'>
+\frac1{16}Re<T_tu,u>.
```

The arithmetic defect is therefore a finite Sobolev-level shift-correlation operator.

## 7. Finite Gamma-null ladder — auxiliary

```text
Q_m=L+alpha_m^2
        |
        v
M(Q_m u)(s)=(alpha_m^2-(s-1/2)^2)M(u)(s)
        |
        v
zeros at {-2m,2m+1}
```

Finite unions are compatible with Connes--Consani Proposition C.1. Negative even points are trivial zeta zeros and do not violate the condition `F ∩ Z_nontrivial = empty`.

No main coercivity edge is granted unless this ladder controls `O_a`.

## 8. Certified short-window scalar side gate

A dedicated Arb workflow brackets the project-internal `a_*` root of `B(a)=kappa_*` in

```math
(0.1033784517534,0.1033784517535)
```

and checks it lies below `log2/2`. This is a side certificate, not the all-window proof.

## 9. Firewalls

- Prime threshold growth != centered arithmetic obstruction;
- short-window reproduction != novelty;
- Gamma ladder != all-window domination;
- positive finite Ritz gap != proof;
- global restricted criterion != fixed-window criterion;
- Registry unchanged.