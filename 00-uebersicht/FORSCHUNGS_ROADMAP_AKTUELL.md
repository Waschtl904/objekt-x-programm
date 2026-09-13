# Objekt X — kanonische Forschungsroadmap v3.8

> **Stand:** 13. September 2026; Registry und Arbeitsdefinition unverändert.

## Gate C0 — Completion / A1-TAIL `✓[M] / ✓[K/M]`

Geschlossen sind:

```text
COMMON-JUMP / Q0
rank-2 completion / Morse / parity
canonical lambda=1
exact a=1 Fourier multiplier
high-frequency positivity
full infinite Prolate tail
```

Insbesondere gilt `q_1>0.01I` auf dem orthogonalen Tail nach den ersten `1490` PSWF-Moden.

## Gate C1 — Bounded lower operator `✓[M]`

Mit

```math
c=0.04,
\quad
r=(m_1-c)1_{[-2300,2300]},
\quad
K=P_I\mathcal F^{-1}M_r\mathcal F P_I
```

ist

```math
q_1\succeq cI+K.
```

Für `A_1=q_1+E^*E` genügt deshalb

```math
L_1=cI+K+E^*E.
```

## Gate C2 — Moment-augmented PSWF split `✓[M]`

```math
R_N=\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\}
+\operatorname{span}\{e^{x/2},e^{-x/2}\},
\qquad
T_N=R_N^\perp.
```

Dann

```math
E|_{T_N}=0,
```

und damit besitzt der Completionterm keinen Tail- oder Crossblock.

Für den bounded band operator:

```math
\|(L_1)_{RT}\|\le\|r\|_\infty\sqrt{\lambda_N},
```

```math
(L_1)_{TT}\succeq
[c-(\Gamma_1+c)\lambda_N]I.
```

## Gate C3 — Explicit N=1680 Schur constants — candidate `✓[K/M]`

Vorab fixiert:

```text
Omega=2300,
c=0.04,
N=1680.
```

Der neue Exact-Head-Arb-Gate soll zertifizieren

```math
\|r\|_\infty<12,
\qquad
\lambda_{1680}<1.1\times10^{-39},
```

```math
\tau_{1680}>0.039,
```

und

```math
\frac{\|r\|_\infty^2\lambda_{1680}}{\tau_{1680}}
<4.1\times10^{-36}.
```

Bis CI grün ist, bleibt dieser Gate candidate.

## Gate C4 — A1-FINITE `?[O]`

Nach erfolgreichem C3 genügt der eine resolved-space Satz

```math
\boxed{
(L_1)_{RR}\succeq5\times10^{-36}I.
}
```

Resolved dimension:

```text
at most 1682 total
at most 841 even + 841 odd.
```

Das ist der gesamte verbleibende `a=1`-Beweisobligation.

## Gate C5 — certified a=1 completion `?[O]`

C4 plus der zertifizierte Schur-Penalty ergibt

```text
A_1>=0
  => q_1>=0 on ker E
  => fixed-window null-pole positivity at a=1.
```

Kein solcher Satz ist bisher bewiesen.

## Gate C6 — all-window mechanism `?[O]`

Erst nach einem `a=1`-Abschluss:

```text
finite fixed-window certificate
  |
structural scaling / further windows
  |
all-a NP-GAP
  |
RH-hard global criterion.
```

## Firewalls

- N=1680 Schurkonstanten erst nach exact-head CI promoten.
- `5e-36` ist ein vorab berechnetes sufficient target, kein beobachteter Eigenwert.
- resolved lower bound ist weiterhin offen.
- fixed-window `a=1` ist noch nicht bewiesen.
- Registry/Arbeitsdefinition unverändert.
