# Aktueller Stand — Objekt X / NP-DUAL-COMP

> **Stand:** 13. September 2026; Registry unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [NP-DUAL-COMP-Audit](../audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md).

## 1. COMMON-JUMP bleibt die gesicherte Basis

Für

```math
q_a(v)=\|X_av\|^2-\Gamma_a\|v\|^2,
\qquad
\mathcal Ev=(E_+(v),E_-(v))^T,
```

ist

```math
D_{NP}(a)=\ker\mathcal E,
```

und

```math
Q_W^a(v)=q_a(v)+\langle P\mathcal Ev,\mathcal Ev\rangle.
```

## 2. Literaturkorrektur

Die pole-cleared Diskrepanz aus PR #110 ist exakt der Ableitungsblock des Prime+Polar-Teils von Suzukis Screw-Funktion:

```math
\mathfrak D=(g_0+r_0)'.
```

Also:

```text
identity / null-pole gauge              ✓[M]
D as literature-new arithmetic object   ×[M]
```

## 3. Turán-Scope korrigiert

Nullpol-Autokorrelationen erfüllen zwei lineare notwendige Bedingungen

```math
L_0(C)=0,
\qquad L_1(C)=0,
```

mit Gewichten `cosh(t/2)` und `t sinh(t/2)`. Diese Bedingungen sind aber nicht hinreichend, um beide Faktorbedingungen `E_+=E_-=0` zu rekonstruieren.

Daher ist ein scalar-Turán-SDP eine äußere Relaxation, nicht die exakte Hauptfront.

## 4. Exakte fixed-window Dualität

Strikte Nullpol-Coercivity

```math
q_a(k)\ge\delta\|k\|^2
\quad(k\in\ker E)
```

impliziert und ist durch eine finite-rank Completion zertifizierbar:

```math
q_a+\lambda_aE^*E\succeq0.
```

Für Semidefinitheit exakt:

```math
q_a\ge0\text{ auf }\ker E
\iff
\forall\varepsilon>0\ \exists\lambda_{a,\varepsilon}>0:
q_a+\varepsilon I+\lambda_{a,\varepsilon}E^*E\succeq0.
```

Der duale Defekt hat also Rang höchstens zwei.

## 5. Nächster Gate

Ein theorematisches numerisches Zertifikat muss die unendliche Restdomäne kontrollieren. Finite PSD allein reicht nicht.

Benchmark: aktuelle Literatur zertifiziert volle fixed-window Weil-Positivität bis `a=0.8`; ein neuer fixed-window-Test sollte `a>0.8` wählen, bevorzugt `a=1.0`.

## 6. Status

```text
COMMON-JUMP / Q0                           ✓[M]
Suzuki screw redundancy of D              ✓[M]
D as new arithmetic object                ×[M]
necessary autocorrelation gauges          ✓[M]
scalar Turan exactness                     ×[M]
rank-2 completion duality                 ✓[M]
certified completion beyond a=0.8         ?[O]
all-a NP-GAP                              ?[O]
forward Object-X architecture             ✓[M]_part
full positive Object-X / RH               ?[O]
```
