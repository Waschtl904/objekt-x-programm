# CURRENT FRONT — Objekt X / A1-FINITE

> **Stand:** 13. September 2026; Registry und Objekt-X-Arbeitsdefinition unverändert.  
> **Hauptaudits:** [NP-DUAL-COMP](audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md) · [A1-TAIL](audits/P11_A1_HIGHFREQ_PROLATE_TAIL_2026-09-13.md) · [A1 bounded Schur remainder](audits/P11_A1_SCHUR_BOUNDED_REMAINDER_2026-09-13.md).

## 1. Gesicherte Completion-Architektur `✓[M]`

Mit

```math
q_a=X_a^*X_a-\Gamma_aI,
\qquad
\mathcal E=(E_+,E_-),
```

ist `D_NP(a)=ker E`. Rank-2 Completion-Dualität, Morse-Index-Filter, Reflection/Parity-Reduktion und die kanonische Completion `lambda=1` sind geschlossen.

## 2. A1-TAIL ist geschlossen `✓[M] / ✓[K/M]`

Bei `a=1` gilt exakt

```math
q_1(v)=\int_{\mathbb R}m_1(\xi)|\widehat v(\xi)|^2d\xi
```

mit

```math
m_1(\xi)=
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
```

Exact-head Arb zertifiziert

```math
m_1(\xi)>0.04\qquad(|\xi|\ge2300).
```

Karnik--Romberg--Davenport plus Arb liefert

```math
\lambda_{1490}(2300)<0.0035,
```

und damit auf dem vollständigen orthogonalen Prolate-Tail

```math
q_1>0.01I.
```

Der unendlichdimensionale Tail selbst ist also kein offener Gate mehr.

## 3. Bounded-band lower operator `✓[M]`

Setze

```math
c=0.04,
\qquad
r(\xi)=(m_1(\xi)-c)\mathbf1_{|\xi|\le2300},
```

und

```math
K=P_I\mathcal F^{-1}M_r\mathcal F P_I,
\qquad I=(-1,1).
```

Der Hochfrequenzrest

```math
s(\xi)=(m_1(\xi)-c)\mathbf1_{|\xi|>2300}
```

ist positiv. Daher

```math
\boxed{q_1\succeq cI+K.}
```

Für die kanonische Completion

```math
A_1=q_1+\mathcal E^*\mathcal E
```

genügt deshalb der bounded lower operator

```math
\boxed{L_1=cI+K+\mathcal E^*\mathcal E.}
```

## 4. Moment-augmented Prolate split `✓[M]`

Sei

```math
R_N^0=\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\}
```

der resolved PSWF-Raum und

```math
\mathcal M
=\operatorname{span}\{e^{x/2},e^{-x/2}\}
```

die Riesz-Range des Momentoperators.

Definiere

```math
\boxed{R_N=R_N^0+\mathcal M,\qquad T_N=R_N^\perp.}
```

Dann gilt gleichzeitig

```math
T_N\subset(R_N^0)^\perp,
\qquad
\mathcal E|_{T_N}=0.
```

Also besitzt der Completionterm `E^*E` **keinen Tailblock und keinen resolved--tail Crossblock**.

## 5. Explicit bounded crossblock `✓[M]`

Für `u in R_N`, `t in T_N` ist

```math
\langle u,L_1t\rangle=\langle u,Kt\rangle.
```

Da `r` bandbegrenzt ist,

```math
\boxed{
\|(L_1)_{RT}\|
\le\|r\|_\infty\sqrt{\lambda_N}.
}
```

Auf dem Tail gilt zugleich

```math
\boxed{
(L_1)_{TT}\succeq
\tau_N I,
\qquad
\tau_N=c-(\Gamma_1+c)\lambda_N.
}
```

Daher reicht für den Schurabschluss

```math
\boxed{
(L_1)_{RR}\succeq\mu_RI,
\qquad
\mu_R\ge
\frac{\|r\|_\infty^2\lambda_N}{\tau_N}.
}
```

## 6. Predeclared `N=1680` certificate target — exact-head CI pending

Der neue Arb-Gate ist vorab auf

```text
Omega = 2300,
c = 0.04,
N = 1680
```

fixiert und soll zertifizieren:

```math
\|r\|_\infty<12,
```

```math
\lambda_{1680}(2300)<1.1\times10^{-39},
```

```math
\tau_{1680}>0.039,
```

```math
\frac{\|r\|_\infty^2\lambda_{1680}}{\tau_{1680}}
<4.1\times10^{-36}.
```

Diese vier numerischen Aussagen bleiben bis zum grünen Exact-Head-Lauf **candidate `✓[K/M]`**.

Wenn der Gate grün wird, genügt anschließend die einzige finite Aussage

```math
\boxed{
(L_1)_{RR}\succeq5\times10^{-36}I.
}
```

Der resolved Raum hat Dimension höchstens `1682`, parity-getrennt höchstens `841+841`.

## 7. Neue Default-Front — A1-FINITE `?[O]`

Nach erfolgreichem Cross-Gate besteht der gesamte offene `a=1`-Satz nur noch aus dem finite resolved lower bound

```math
(L_1)_{RR}\succeq5\times10^{-36}I.
```

Es bleibt kein separates unendlichdimensionales Tail- oder Crossblockproblem.

## 8. Status

```text
COMMON-JUMP / Q0                                      ✓[M]
rank-2 completion / Morse / parity                    ✓[M]
exact a=1 Fourier multiplier                          ✓[M]
full infinite Prolate tail positivity                 ✓[K/M]
bounded-band lower operator                           ✓[M]
moment-augmented split                                ✓[M]
abstract bounded crossblock / Schur criterion         ✓[M]
||r||<12, lambda_1680<1.1e-39                         candidate ✓[K/M]
tau_1680>0.039                                        candidate ✓[K/M]
Schur penalty <4.1e-36                                candidate ✓[K/M]
resolved lower bound >=5e-36                          ?[O]
certified a=1 completion                              ?[O]
all-a NP-GAP                                          ?[O]
forward Object-X candidate architecture               ✓[M]_part
full positive Object-X / RH                           ?[O]
```

## 9. Firewalls

Do not claim:

- the new numerical Schur constants are certified before exact-head CI;
- the resolved `5e-36` lower bound has been proved;
- the PSWF basis diagonalizes `q_1` or `K`;
- fixed-window `a=1`, all-window NP-GAP, Object X, or RH is solved.
