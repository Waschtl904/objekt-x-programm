# Abhängigkeitsgraph (DAG) — Objekt X / A1-SCHUR

> **Stand:** 13. September 2026; Registry und Arbeitsdefinition unverändert.

## 1. Completion basis

```text
COMMON-JUMP / Q0 ✓[M]
        |
D_NP(a)=ker E
        |
q_a=X_a^*X_a-Gamma_a I
        |
rank-2 completion / Morse / parity ✓[M]
        |
canonical lambda=1 ✓[M]
```

## 2. Exact `a=1` Fourier edge

```text
q_1 on time-limited functions
        |
whole-line Plancherel
        v
q_1(v)=integral m_1(xi)|vhat(xi)|^2 dxi    ✓[M]
```

with active prime powers `{2,3,4,5,7}` and no additional window remainder.

## 3. High-frequency edge

```text
DLMF digamma series
 + monotone integral tail
 + cos(theta)<=1
        |
        v
m_1(xi)>0.04 for |xi|>=2300                ✓[K/M]
```

Also globally `m_1>=-Gamma_1`.

## 4. Prolate concentration edge

```text
C_2300=P[-1,1] B[-2300,2300] P[-1,1]
        |
PSWF eigenvalues lambda_k
        |
Karnik-Romberg-Davenport Cor. 3
        |
        v
lambda_1490(c=2300)<0.0035                  ✓[K/M]
```

Therefore for `T_1490=span{psi_0,...,psi_1489}^perp`:

```text
band mass <= lambda_1490
        +
high-frequency m_1>0.04
        +
global m_1>=-Gamma_1
        |
        v
q_1 > 0.01 I on T_1490                       ✓[K/M]
```

The infinite tail is closed.

## 5. Parity edge

```text
PSWF reflection symmetry
        |
first 1490 modes = 745 even + 745 odd
        |
        v
compatible with 2-channel parity completion ✓[M]
```

## 6. Remaining A1-SCHUR edge

For

```math
A_1=q_1+E^*E
```

and decomposition `R_1490 + T_1490`:

```text
A_TT > 0.01 I                                ✓[K/M]
        |
        +--> certify A_RR on 1490 modes       ?[O]
        +--> certify ||A_RT||                  ?[O]
        |
        v
A_RR-A_RT A_TT^{-1} A_TR >=0                 ?[O]
        |
        v
certified a=1 completion                      ?[O]
```

## 7. Global path

```text
A1-SCHUR
   |
fixed-window a=1 completion
   |
structural scaling / further windows
   |
all-a NP-GAP
   |
restricted Weil criterion
   |
RH
```

## 8. Firewalls

- PSWF basis diagonalizes concentration, not `q_1`.
- Positive tail does not imply positive full operator.
- Earlier finite Dirichlet Ritz values remain non-certified.
- Resolved PSD without crossblock bound is not a theorem.
