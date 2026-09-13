# Aktueller Stand — Objekt X / A1-SCHUR

> **Stand:** 13. September 2026; Registry und Objekt-X-Arbeitsdefinition unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [NP-DUAL-COMP](../audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md), [A1-TAIL](../audits/P11_A1_HIGHFREQ_PROLATE_TAIL_2026-09-13.md).

## 1. Completion-Architektur `✓[M]`

Für

```math
q_a=X_a^*X_a-\Gamma_aI,
\qquad \mathcal E=(E_+,E_-),
```

ist `D_NP(a)=ker E`. Fixed-window Nullpol-Coercivity besitzt die exakte rank-2 Completion-Dualität; Morse-Index-Filter und Reflection/Parity-Reduktion sind ebenfalls geschlossen.

Die kanonische skalare Completion ist

```math
q_a+\mathcal E^*\mathcal E
=Q_W^a+\mathcal E^*(I-P)\mathcal E,
```

also `lambda=1` als vorab festgelegter Kandidat.

## 2. Exakte Fourierform bei `a=1` `✓[M]`

Für zero-extended `v` mit Träger in `(-1,1)`:

```math
\boxed{
q_1(v)=\int_{\mathbb R}m_1(\xi)|\widehat v(\xi)|^2d\xi
}
```

mit

```math
m_1(\xi)=
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
```

Es gibt keinen zusätzlichen Fensterrest im quadratischen Wert.

## 3. Hochfrequenz-Gate `✓[K/M]`

Ein 256-bit-Arb-Zertifikat kombiniert eine endliche Digamma-Reihe mit einem rigorosen Integralrest und beweist

```math
\boxed{m_1(\xi)>0.04\quad(|\xi|\ge2300).}
```

Global gilt `m_1>=-Gamma_1`.

## 4. Voller Prolate-Tail `✓[K/M]`

Für den Zeit-Band-Konzentrationsoperator auf `[-1,1]` mit Band `[-2300,2300]` ist der kontinuierliche Prolate-Parameter `c=2300`.

Die nichtasymptotische Karnik--Romberg--Davenport-Schranke wird intervallrigoros ausgewertet und liefert

```math
\boxed{\lambda_{1490}(2300)<0.0035.}
```

Daher gilt auf dem orthogonalen Komplement der ersten `1490` timelimitierten PSWF-Moden

```math
\boxed{
q_1(v)>0.01\|v\|^2.
}
```

Damit ist der gesamte unendlichdimensionale Prolate-Tail rigoros coercive.

## 5. Verbleibender `a=1`-Gate

Schreibe für die kanonische Completion

```math
A_1=q_1+\mathcal E^*\mathcal E
```

bezüglich

```math
L^2(-1,1)=\mathcal R_{1490}\oplus\mathcal T_{1490}
```

als Blockoperator. Bereits geschlossen ist

```math
A_{TT}>0.01I.
```

Offen bleibt der endliche Schur-Abschluss

```math
\boxed{
A_{RR}-A_{RT}A_{TT}^{-1}A_{TR}\succeq0.
}
```

Also: finite `1490`-Mode-Arb-Matrix plus rigorose resolved--tail Kopplung.

## 6. Status

```text
COMMON-JUMP / Q0                                  ✓[M]
rank-2 completion / Morse / parity                ✓[M]
exact a=1 Fourier multiplier                       ✓[M]
high-frequency m_1>0.04 outside |xi|=2300         ✓[K/M]
KRD Prolate eigenvalue lambda_1490<0.0035          ✓[K/M]
full infinite Prolate tail q_1>0.01                ✓[K/M]
resolved 1490-mode Arb block                       ?[O]
resolved-tail crossblock / Schur                   ?[O]
certified a=1 completion                           ?[O]
all-a NP-GAP                                       ?[O]
forward Object-X architecture                      ✓[M]_part
full positive Object-X / RH                        ?[O]
```
