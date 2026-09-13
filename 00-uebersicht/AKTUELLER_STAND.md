# Aktueller Stand — Objekt X / A1-FINITE-1212

> **Stand:** 13. September 2026; Registry und Objekt-X-Arbeitsdefinition unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [A1 Omega1551](../audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md), [A1 bounded Schur remainder](../audits/P11_A1_SCHUR_BOUNDED_REMAINDER_2026-09-13.md).

## 1. Gesicherte A1-Basis

Rank-2 Completion, Morse/Parity, exakte Fourierform sowie die Prolate-Schur-Reduktion sind geschlossen.

Der neue Exact-Head-Arb-Gate verschärft die Hochfrequenzschranke zu

```math
\boxed{m_1(\xi)>0.1\quad(|\xi|\ge1551).}
```

## 2. Reduced bounded operator

Mit

```math
c=0.1,
\qquad
r=(m_1-c)\mathbf1_{[-1551,1551]},
```

```math
K=P_I\mathcal F^{-1}M_r\mathcal F P_I
```

gilt

```math
A_1=q_1+E^*E\succeq L_1:=0.1I+K+E^*E.
```

Arb zertifiziert

```math
\|r\|_\infty<12.
```

## 3. Moment-augmented Prolate split

Für

```math
R_N=\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\}
+\operatorname{span}\{e^{x/2},e^{-x/2}\},
\qquad
T_N=R_N^\perp,
```

gilt `E|T_N=0` und

```math
\|(L_1)_{RT}\|\le\|r\|_\infty\sqrt{\lambda_N}.
```

## 4. Certified N=1210 reduction `✓[K/M]`

Für `c_PSWF=1551` liefert KRD plus Arb

```math
\boxed{\lambda_{1210}<1.5\times10^{-42}.}
```

Weiter:

```math
\tau_{1210}>0.099,
```

```math
\boxed{\text{Schur penalty}<2.2\times10^{-39}.}
```

Der tatsächliche Exact-Head-Upper-Bound ist etwa `2.11526e-39`.

## 5. Einziges offenes a=1-Ziel

Es genügt nun

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I.}
```

auf einem augmented resolved Raum von höchstens

```text
1212 total = 606 even + 606 odd.
```

Der Threshold `3e-39` wurde vor jeder resolved-space Rechnung festgelegt und ist kein beobachteter Eigenwert.

## 6. Status

```text
completion / Morse / parity                  ✓[M]
exact a=1 multiplier                         ✓[M]
Omega1551 high-frequency floor               ✓[K/M]
N=1210 Prolate / Schur constants             ✓[K/M]
1212-dimensional finite reduction            ✓[K/M]
resolved lower bound >=3e-39                 ?[O]
certified a=1 completion                     ?[O]
all-a NP-GAP                                 ?[O]
forward Object-X architecture                ✓[M]_part
full positive Object-X / RH                  ?[O]
```
