# Aktueller Stand — Objekt X / A1-FINITE

> **Stand:** 13. September 2026; Registry und Objekt-X-Arbeitsdefinition unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [A1-TAIL](../audits/P11_A1_HIGHFREQ_PROLATE_TAIL_2026-09-13.md), [A1 bounded Schur remainder](../audits/P11_A1_SCHUR_BOUNDED_REMAINDER_2026-09-13.md).

## 1. Gesicherte `a=1`-Basis

Rank-2 Completion, Morse-/Parity-Reduktion, exakte Fourierform und der vollständige Prolate-Tail sind geschlossen. Insbesondere

```math
m_1(\xi)>0.04\quad(|\xi|\ge2300)
```

und

```math
q_1>0.01I
```

auf dem orthogonalen Tail nach den ersten `1490` PSWF-Moden.

## 2. Bounded lower operator `✓[M]`

Mit

```math
c=0.04,
\qquad
r=(m_1-c)\mathbf1_{[-2300,2300]},
```

und

```math
K=P_I\mathcal F^{-1}M_r\mathcal F P_I
```

gilt für die kanonische Completion

```math
A_1=q_1+\mathcal E^*\mathcal E
\succeq
L_1:=cI+K+\mathcal E^*\mathcal E.
```

Der unbeschränkte positive Hochfrequenzanteil ist damit vollständig aus der Schur-Rechnung entfernt.

## 3. Moment-augmented Prolate split `✓[M]`

Für

```math
R_N^0=\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\},
\qquad
\mathcal M=\operatorname{span}\{e^{x/2},e^{-x/2}\},
```

setze

```math
R_N=R_N^0+\mathcal M,
\qquad
T_N=R_N^\perp.
```

Dann `E|_{T_N}=0`; der Completionterm besitzt weder Tail- noch Crossblock. Für den bounded band operator gilt

```math
\|(L_1)_{RT}\|\le\|r\|_\infty\sqrt{\lambda_N},
```

und

```math
(L_1)_{TT}\succeq
\left[0.04-(\Gamma_1+0.04)\lambda_N\right]I.
```

## 4. Predeclared N=1680 gate — CI pending

Der neue Exact-Head-Arb-Gate soll ohne nachträgliches Tuning zertifizieren:

```math
\|r\|_\infty<12,
```

```math
\lambda_{1680}(2300)<1.1\times10^{-39},
```

```math
\tau_{1680}>0.039,
```

und Schur-Penalty

```math
<4.1\times10^{-36}.
```

Bis zum grünen Exact-Head-Lauf bleiben diese Zahlen candidate `✓[K/M]`.

## 5. Endliches Restziel

Nach erfolgreichem Gate genügt als vollständiger `a=1`-Abschluss die einzelne finite Aussage

```math
\boxed{
(L_1)_{RR}\succeq5\times10^{-36}I.
}
```

`R_1680` hat Dimension höchstens `1682`, parity-getrennt höchstens `841+841`.

Damit wären Tail und Crossblock bereits quantitativ absorbiert.

## 6. Status

```text
completion / Morse / parity                         ✓[M]
exact a=1 multiplier                                ✓[M]
full infinite Prolate tail                          ✓[K/M]
bounded-band lower operator                         ✓[M]
moment-augmented Schur reduction                    ✓[M]
explicit N=1680 Schur constants                     candidate ✓[K/M]
resolved lower bound >=5e-36                        ?[O]
certified a=1 completion                            ?[O]
all-a NP-GAP                                        ?[O]
forward Object-X architecture                       ✓[M]_part
full positive Object-X / RH                         ?[O]
```
