# Abhängigkeitsgraph (DAG) — Objekt X / NP-DUAL-COMP

> **Stand:** 13. September 2026; Registry unverändert.

## 1. Base geometry

```text
COMMON-JUMP ✓[M]
   |
E=(E_+,E_-)
   |
D_NP(a)=ker E
   |
q_a=X_a^*X_a-Gamma_a I
   |
Q_W^a=q_a+E^*PE
```

## 2. Screw literature edge

```text
prime/polar discrepancy D
   |
   | exact identity
   v
D=(g0+r0)' in Suzuki screw decomposition       ✓[M]
   |
   v
D as literature-new object                      ×[M]
```

## 3. Autocorrelation edge

```text
v in ker E
   |
C_v(t)=<T_t v,v>
   |
H_v(s)=E_s(v) overline(E_-s(v))
   |
   +--> L0(C_v)=0                              ✓[M]
   +--> L1(C_v)=0                              ✓[M]
```

But:

```text
L0=L1=0 on scalar C
   |
   X
exact reconstruction E_+=E_-=0                 ×[M]
```

Hence scalar Turan is an outer relaxation.

## 4. Exact dual edge

```text
q_a >= delta I on ker E
   |
   v
exists lambda: q_a+lambda E^*E >=0              ✓[M]
```

Semidefinite closure:

```text
q_a >=0 on ker E
   |
   <=>
forall eps>0 exists lambda_eps:
q_a+eps I+lambda_eps E^*E >=0                    ✓[M]
```

This is the exact fixed-window rank-2 completion node.

## 5. Pole matrix edge

```text
arbitrary completion H          exact Weil pole P
         |                             |
         v                             v
null-pole certificate          full fixed-window Weil positivity
```

`H=P` is much stronger than existence of some `H`.

## 6. Computational edge

```text
finite basis + 2x2 completion optimization
        |
        +--> Arb PSD on resolved block
        +--> rigorous tail / Schur complement
        |
        v
certified fixed-window completion ?[O]
```

Without the tail edge, finite PSD is only diagnostic.

## 7. Baseline / barrier

```text
literature full-class positivity through a=0.8
Landau-Widom tiny-gap scale
pointwise-envelope doubly-exponential barrier
```

Therefore the first potentially new fixed-window target is `a>0.8`, naturally `a=1.0`.

## 8. Main path

```text
rank-2 completion theorem ✓[M]
   |
rigorous fixed-a completion beyond 0.8 ?[O]
   |
structural completion for every a ?[O]
   |
all-a NP-GAP ?[O]
   |
RH
```

Registry and working definition unchanged.
