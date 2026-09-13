# Offene Probleme — NP-DUAL-COMP

> **Stand:** 13. September 2026.  
> Operative Quelle: [NP-DUAL-COMP-Audit](audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md).

## Neu geschlossen

### `[SCREW-REDUNDANCY]` `✓[M]`

Die pole-cleared Diskrepanz aus PR #110 ist der bekannte Prime+Polar-Ableitungsblock der Suzuki-Screw-Funktion:

```math
D=(g_0+r_0)'.
```

Neuheitsclaim `D` als neues arithmetisches Objekt: `×[M]`.

### `[AUTOCORR-GAUGES]` `✓[M]`

Nullpol erzeugt die notwendigen linearen Bedingungen

```math
L_0(C)=0,
\qquad L_1(C)=0.
```

### `[TURAN-EXACTNESS]` `×[M]`

Weder eine noch beide skalaren Momentbedingungen charakterisieren `E_+=E_-=0` exakt auf Faktorebene. Scalar-Turán ist nur eine äußere Relaxation.

### `[RANK2-COMPLETION]` `✓[M]`

Strict:

```math
q_a\ge\delta I\text{ on ker E}
\Longrightarrow
\exists\lambda>0:\ q_a+\lambda E^*E\succeq0.
```

Semidefinite exact:

```math
q_a\ge0\text{ on ker E}
\iff
\forall\varepsilon>0\ \exists\lambda_\varepsilon>0:
q_a+\varepsilon I+\lambda_\varepsilon E^*E\succeq0.
```

---

## Priorität 0 — `[DUAL-CERT-1.0]` `?[O]`

Baue einen **rigorosen** fixed-window Completion-Certificate bei

```text
a=1.0
```

oder einem vorab festgelegten Wert `>0.8`.

Pflichten:

1. Basis/Trunkierung vor Ergebnis festlegen;
2. exact/Arb Momentmatrix für `E_±`;
3. Hermiteschen `2x2` Completionblock `H` oder scalar `lambda` optimieren;
4. resolved PSD zertifizieren;
5. unresolved tail rigoros kontrollieren;
6. keine Promotion aus einem bloßen finite Ritz/SDP value.

Literaturbenchmark: volle fixed-window Positivität ist bereits bis `a=0.8` zertifiziert.

---

## Priorität 1 — `[COMPLETION-STRUCTURE]` `?[O]`

Suche eine analytische Regel für `H_a` oder `lambda_a`, die mit `a` skaliert und nicht auf jedem Fenster neu numerisch gefittet wird.

Besonders prüfen:

- Verbindung von `H_a` zum klassischen Poleblock `P`;
- Q0-Transport und COMMON-JUMP;
- signed discrepancy / AR(1) nur als Mechanismen zur Tailkontrolle;
- mögliche Monotonie/Schur-Komplement-Kovarianz in `a`.

---

## Priorität 2 — `[TURAN-RELAX]`

Scalar-Turán/positive-definite SDP darf als sufficient relaxation getestet werden. Ein positives Zertifikat dort beweist mehr als nötig; ein negativer Relaxationszeuge falsifiziert NP-GAP **nicht**.

---

## Firewalls

- `D` nicht als neue arithmetische Größe verkaufen;
- scalar autocorrelation nicht mit factor-level null-pole verwechseln;
- finite matrix PSD ohne tail != theorem;
- fixed-window positivity != RH;
- all-a completion bleibt RH-hart;
- Object X / RH offen.
