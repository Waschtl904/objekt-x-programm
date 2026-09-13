# Abhängigkeitsgraph (DAG) — Objekt X / A1-FINITE

> **Stand:** 13. September 2026; Registry und Arbeitsdefinition unverändert.

## 1. Closed base

```text
COMMON-JUMP / Q0 ✓[M]
        |
rank-2 completion / Morse / parity ✓[M]
        |
canonical lambda=1 ✓[M]
        |
exact a=1 multiplier ✓[M]
        |
high-frequency + full Prolate tail ✓[K/M]
```

## 2. Bounded-band reduction

```text
m_1 = c + r_band + s_out,
s_out >=0
        |
        v
q_1 >= c I + K                              ✓[M]
        |
A_1=q_1+E^*E >= L_1=cI+K+E^*E              ✓[M]
```

with `c=0.04` and `r_band=(m_1-c)1_{|xi|<=2300}`.

## 3. Moment augmentation

```text
R_N^0 = first N PSWFs
M = span{e^{x/2},e^{-x/2}}
        |
R_N=R_N^0+M
T_N=R_N^perp
        |
        +--> T_N subset (R_N^0)^perp
        +--> E|T_N=0
```

Hence the completion term has no tail/crossblock. `✓[M]`.

## 4. Bounded crossblock theorem

```text
band concentration on T_N <= lambda_N
        +
||r||_infty finite
        |
        v
||L_RT|| <= ||r|| sqrt(lambda_N)             ✓[M]
```

and

```text
L_TT >= tau_N I,
tau_N=c-(Gamma_1+c)lambda_N                    ✓[M]
```

Therefore

```math
L_{RR}\succeq\mu_RI,
\qquad
\mu_R\ge\frac{\|r\|_\infty^2\lambda_N}{\tau_N}
```

is sufficient for `L_1>=0`, hence for the canonical completion.

## 5. Explicit N=1680 gate — candidate until CI

```text
||r||<12
lambda_1680(c=2300)<1.1e-39
tau_1680>0.039
        |
        v
Schur penalty <4.1e-36
        |
        v
resolved target mu_R=5e-36 sufficient
```

All numeric constants remain candidate `✓[K/M]` until the new exact-head Arb workflow is green.

## 6. Final open edge after C5

```text
R_1680 dimension <=1682
  = <=841 even + <=841 odd
        |
        v
certify L_RR >=5e-36 I                         ?[O]
        |
        v
canonical a=1 completion                       ?[O]
```

After the new cross gate is certified, no separate infinite-dimensional tail or crossblock theorem remains.

## 7. Global path

```text
A1-FINITE
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

## 8. Firewalls

- `5e-36` is a predeclared sufficient threshold, not a measured eigenvalue.
- New Schur constants require exact-head CI before promotion.
- Resolved lower bound remains open.
- Fixed-window a=1 and RH are not proved.
