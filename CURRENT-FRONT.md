# CURRENT FRONT — Objekt X / NP-DUAL-COMP

> **Stand:** 13. September 2026; Registry und Objekt-X-Arbeitsdefinition unverändert.  
> **Hauptaudit:** [NP-DUAL-COMP / Screw audit](audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md).

## 1. Gesicherte Architektur

COMMON-JUMP und `Q_0` bleiben `✓[M]`. Für

```math
\mathcal Ev=(E_+(v),E_-(v))^T,
\qquad
q_a(v)=\|X_av\|^2-\Gamma_a\|v\|^2,
```

gilt

```math
D_{NP}(a)=\ker\mathcal E,
```

und die volle lokale Weilform ist exakt

```math
\boxed{
Q_W^a(v)=q_a(v)+\langle P\mathcal Ev,\mathcal Ev\rangle,
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
}
```

## 2. Screw-Redundanzaudit

Die in PR #110 definierte pole-cleared Diskrepanz ist algebraisch korrekt, aber kein literatur-neues arithmetisches Objekt. Für den Prime-/Polar-Teil von Suzukis Screw-Funktion gilt auf `t>0`

```math
\boxed{
\mathfrak D(t)=\frac d{dt}(g_0(t)+r_0(t)),
}
```

mit

```math
g_0(t)=\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n),
\qquad
r_0(t)=-4(e^{t/2}+e^{-t/2}-2).
```

Daher:

```text
prime/polar discrepancy identity                  ✓[M]
D as literature-new arithmetic object              ×[M]
null-pole gauge/use                                 ✓[M]
publication novelty of the architecture/use         ?[O]
```

## 3. Autokorrelation: Turán ja, aber nur als Relaxation

Für

```math
C_v(t)=\langle T_tv,v\rangle
```

gilt bilateral

```math
\int_{\mathbb R}e^{st}C_v(t)dt
=E_s(v)\overline{E_{-s}(v)}.
```

Nullpol erzeugt daher bei `s=1/2` mindestens eine doppelte Nullstelle. Für reelle `v` folgen zwei lineare Bedingungen

```math
\boxed{
L_0(C_v)=\int_0^{2a}C_v(t)\cosh(t/2)dt=0,
}
```

```math
\boxed{
L_1(C_v)=\int_0^{2a}tC_v(t)\sinh(t/2)dt=0.
}
```

Aber selbst `L_0=L_1=0` charakterisiert Nullpol **nicht**: die zwei Nullstellen können vollständig in nur einem Spektralfaktor liegen. Deshalb

```text
one-moment Turan = exact null-pole class           ×[M]
two scalar moments = exact null-pole class          ×[M]
L0,L1 as necessary dual gauges                      ✓[M]
```

Ein skalare positive-definite Turán-SDP ist damit eine **äußere Relaxation**: ein Positivitätszertifikat genügt, ein Gegenbeispiel falsifiziert NP-GAP nicht.

## 4. Exakte Hauptfront — rank-2 completion `✓[M]`

Sei `q_a` die geschlossene, nach unten beschränkte COMMON-JUMP-Form und `E` der zweikomponentige Momentoperator.

### Strikte Version

Falls

```math
q_a(k)\ge\delta\|k\|^2
\qquad(k\in\ker\mathcal E)
```

für ein `delta>0`, dann existiert `lambda_a>0` mit

```math
\boxed{
q_a+\lambda_a\mathcal E^*\mathcal E\succeq0
}
```

auf der vollen Formdomäne. Umgekehrt impliziert jede solche Completion Positivität auf `ker E`.

### Semidefinite exakte Version

```math
\boxed{
q_a\ge0\text{ auf }\ker\mathcal E
\iff
\forall\varepsilon>0\ \exists\lambda_{a,\varepsilon}>0:
q_a+\varepsilon I+\lambda_{a,\varepsilon}\mathcal E^*\mathcal E\succeq0.
}
```

Damit ist fixed-window NP-GAP exakt ein **Rang-2-Finite-Completion-Problem**.

## 5. Verbindung zur echten Polschicht

Die klassische Weil-Polschicht selbst ist

```math
\mathcal E^*P\mathcal E.
```

`H=P` als positive Completion wäre daher bereits volle fixed-window Weil-Positivität. NP-GAP verlangt nur die Existenz irgendeiner geeigneten Completion; sie muss nicht `P` sein.

Das verhindert eine Überpromotion: die Dualcompletion ist ein Zertifikatsmechanismus, noch keine vollständige positive Objekt-X-Realisierung.

## 6. Computational gate

Ein endliches SDP ist **nicht automatisch exakt**. Für einen theorematischen fixed-window-Nachweis braucht es:

1. vorab festgelegte Basis und Trunkierung;
2. exakte/Intervall-Momentzeilen für `E_±`;
3. Optimierung eines Hermiteschen `2x2`-Completionblocks oder eines skalaren `lambda`;
4. Arb-PSD des aufgelösten Blocks;
5. rigorose Tail-/Schur-Komplement-Untergrenze.

Zhu zertifiziert volle Weil-Positivität bereits bis `a=0.8`; ein potentiell neues fixed-window-Ziel muss daher `a>0.8` wählen. `a=1.0` ist der natürliche Stresspunkt.

## 7. Landau--Widom / Falsifikationsrolle

Die winzigen Gaps sind mit der Landau--Widom-Plunge-Skala kompatibel. Prolate-/Landau--Widom-Strukturen bleiben Kalibrierungs- und Falsifikationswerkzeuge; ein konstanter Konzentrationsfaktor ist kein all-window-Beweis.

## 8. Status

```text
COMMON-JUMP / Q0                                      ✓[M]
prime/polar discrepancy identity                      ✓[M]
D as literature-new object                            ×[M]
Suzuki screw redundancy                               ✓[M]
L0,L1 necessary autocorrelation gauges                ✓[M]
scalar Turan moments = exact null-pole class           ×[M]
strict rank-2 completion equivalence                  ✓[M]
semidefinite epsilon-completion equivalence            ✓[M]
finite exact SDP certificate beyond a=0.8             ?[O]
all-a NP-GAP / completion                             ?[O]
forward Object-X candidate architecture               ✓[M]_part
full positive Object-X / RH                           ?[O]
```
