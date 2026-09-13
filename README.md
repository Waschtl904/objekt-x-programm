# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

> **Stand: 13. September 2026.**  
> COMMON-JUMP liefert eine gemeinsame Prime-/archimedische positive Featurearchitektur. Bei `a=1` ist der unendlichdimensionale Tail bereits rigoros positiv. Eine moment-augmentierte Prolate-Schur-Reduktion reduziert den noch offenen fixed-window Satz — vorbehaltlich des neuen Exact-Head-Arb-Gates — auf eine **einzige finite resolved-space Untergrenze**. Eine vollständige positive Objekt-X-Realisierung und RH bleiben offen.

## Hier beginnen

1. [CURRENT-FRONT](CURRENT-FRONT.md)
2. [A1 bounded Schur remainder](audits/P11_A1_SCHUR_BOUNDED_REMAINDER_2026-09-13.md)
3. [A1 high-frequency / Prolate tail](audits/P11_A1_HIGHFREQ_PROLATE_TAIL_2026-09-13.md)
4. [NP-DUAL-COMP](audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md)
5. [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)

## 1. Closed completion and tail structure

Für

```math
A_1=q_1+\mathcal E^*\mathcal E
```

sind rank-2 Completion, Morse/Parity und `lambda=1` kanonisiert. Zudem gilt exakt

```math
q_1(v)=\int m_1(\xi)|\widehat v(\xi)|^2d\xi.
```

Exact-head Arb + Karnik--Romberg--Davenport liefert bereits

```math
m_1(\xi)>0.04\quad(|\xi|\ge2300),
```

und rigorose Positivität des vollständigen unendlichdimensionalen Prolate-Tails.

## 2. Bounded-band lower operator

Setze

```math
c=0.04,
\qquad
r=(m_1-c)\mathbf1_{[-2300,2300]},
```

```math
K=P_I\mathcal F^{-1}M_r\mathcal F P_I.
```

Der verworfene Außenanteil ist positiv, also

```math
\boxed{q_1\succeq cI+K.}
```

Damit genügt für die kanonische Completion der bounded operator

```math
\boxed{L_1=cI+K+\mathcal E^*\mathcal E.}
```

## 3. Moment-augmented Prolate decomposition

Für die PSWFs `psi_k` setze

```math
R_N=
\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\}
+\operatorname{span}\{e^{x/2},e^{-x/2}\},
\qquad
T_N=R_N^\perp.
```

Dann gilt auf dem Tail exakt

```math
\mathcal E=0.
```

Der Completionterm hat damit keinen Tail- oder Crossblock. Für den bounded band operator:

```math
\boxed{\|(L_1)_{RT}\|\le\|r\|_\infty\sqrt{\lambda_N},}
```

```math
\boxed{(L_1)_{TT}\succeq[0.04-(\Gamma_1+0.04)\lambda_N]I.}
```

## 4. Explicit finite target — exact-head gate pending

Vorab festgelegt:

```text
Omega = 2300
N = 1680
```

Der neue Arb-Gate soll zertifizieren

```math
\|r\|_\infty<12,
\qquad
\lambda_{1680}(2300)<1.1\times10^{-39},
```

```math
\tau_{1680}>0.039,
```

und

```math
\text{Schur penalty}<4.1\times10^{-36}.
```

Bis Exact-Head-CI grün ist, bleiben diese Zahlen candidate `✓[K/M]`.

Wenn der Gate hält, reicht anschließend

```math
\boxed{
(L_1)_{RR}\succeq5\times10^{-36}I.
}
```

Resolved dimension höchstens:

```text
1682 total
841 even + 841 odd.
```

Das wäre der gesamte verbleibende `a=1`-Beweisobligation.

## 5. Status

```text
COMMON-JUMP / Q0                              ✓[M]
rank-2 completion / Morse / parity            ✓[M]
exact a=1 multiplier                          ✓[M]
full infinite Prolate tail                    ✓[K/M]
bounded-band lower operator                   ✓[M]
moment-augmented cross theorem                ✓[M]
explicit N=1680 Schur constants               candidate ✓[K/M]
resolved lower bound >=5e-36                  ?[O]
certified a=1 completion                      ?[O]
all-a NP-GAP                                  ?[O]
forward Object-X architecture                 ✓[M]_part
full positive Object-X / RH                   ?[O]
```

## Firewalls

- `5e-36` ist kein gemessener Eigenwert, sondern ein vorab deklarierter sufficient threshold.
- Neue N=1680 Konstanten erst nach exact-head CI promoten.
- Resolved lower bound ist noch offen.
- Fixed-window `a=1`, all-a NP-GAP, Object X und RH sind nicht bewiesen.
- Registry und Objekt-X-Arbeitsdefinition bleiben unverändert.

Lizenz: [CC BY 4.0](LICENSE).
