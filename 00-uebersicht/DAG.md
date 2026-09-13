# Abhängigkeitsgraph (DAG) — Objekt X / A1-FINITE-1212

> **Stand:** 13. September 2026; Registry und Arbeitsdefinition unverändert.

## 1. Closed base

```text
COMMON-JUMP / Q0 ✓[M]
        |
rank-2 completion / Morse / parity ✓[M]
        |
canonical lambda=1 ✓[M]
        |
exact a=1 Fourier multiplier ✓[M]
```

## 2. Sharpened frequency gate

```text
DLMF positive digamma series
 + rigorous derivative bound
 + 0.02 Arb grid on [1551,2500]
 + far-field monotonicity
        |
        v
m_1(xi)>0.1 for |xi|>=1551                 ✓[K/M]
```

## 3. Reduced bounded operator

```text
c=0.1
r=(m_1-c)1_{|xi|<=1551}
s=(m_1-c)1_{|xi|>1551} >=0
        |
        v
q_1 >= cI+K                                  ✓[M]
```

Arb also certifies `||r||<12`. `✓[K/M]`.

## 4. Moment-augmented Prolate split

```text
R_N^0 = first N PSWFs
M = span{e^{x/2},e^{-x/2}}
R_N=R_N^0+M
T_N=R_N^perp
        |
        +--> E|T_N=0
        +--> band mass on T_N <= lambda_N
```

Thus the completion term has no tail/crossblock. `✓[M]`.

## 5. Bounded Schur theorem

```math
\|L_{RT}\|\le\|r\|_\infty\sqrt{\lambda_N},
```

```math
L_{TT}\succeq
[c-(\Gamma_1+c)\lambda_N]I.
```

Hence

```math
L_{RR}\succeq\mu_RI,
\qquad
\mu_R\ge
\frac{\|r\|_\infty^2\lambda_N}
{c-(\Gamma_1+c)\lambda_N}
```

is sufficient. `✓[M]`.

## 6. Certified N=1210 constants

```text
lambda_1210(c=1551)<1.5e-42
||r||<12
tau_1210>0.099
        |
        v
Schur penalty <2.2e-39                       ✓[K/M]
```

## 7. Final a=1 edge

```text
R_1210 dimension <=1212
  = <=606 even + <=606 odd
        |
        v
certify L_RR >=3e-39 I                       ?[O]
        |
        v
canonical a=1 completion                     ?[O]
```

No separate infinite-dimensional tail or crossblock theorem remains.

## 8. Global path

```text
A1-FINITE-1212
   |
fixed-window a=1 completion
   |
further windows / structural scaling
   |
all-a NP-GAP
   |
restricted Weil criterion
   |
RH
```

## 9. Firewalls

- `3e-39` is a predeclared sufficient threshold, not a measured eigenvalue.
- The older `2300/1680` certificate remains valid but is superseded quantitatively.
- Resolved lower bound remains open.
- Fixed-window a=1 and RH are not proved.
