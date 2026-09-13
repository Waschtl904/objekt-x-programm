# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**

Forschungsprogramm **Objekt X** im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor. ChatGPT übernimmt Repo-Arbeiten; externe Modelle sind Reviewer. Keine Promotion allein durch Merge, CI oder Numerik.

## Zuerst lesen

1. `CURRENT-FRONT.md`
2. `audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md`
3. `audits/P11_NP_DISCREPANCY_POLE_CLEARED_CORRELATION_2026-09-13.md`
4. `audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md`
5. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md`
6. Registry und Objekt-X-Arbeitsdefinition nur als unverändert gültige Governancequellen.

## Aktueller Kern

Mit

```math
q_a=X_a^*X_a-\Gamma_a I,
\qquad
\mathcal E=(E_+,E_-),
```

ist

```math
D_{NP}(a)=\ker\mathcal E
```

und

```math
Q_W^a=q_a+\mathcal E^*P\mathcal E,
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
```

### Literaturkorrektur

Die pole-cleared Diskrepanz ist nicht als neues arithmetisches Objekt zu beanspruchen; sie ist der Prime+Polar-Ableitungsblock von Suzukis Screw-Funktion.

### Autocorrelation firewall

Nullpol impliziert zwei notwendige lineare Bedingungen auf `C_v`, aber selbst beide sind nicht hinreichend, um `E_+=E_-=0` auf Faktorebene zu rekonstruieren. Scalar-Turán ist deshalb nur eine äußere Relaxation.

### Exact dual completion

Strict:

```math
q_a\ge\delta I\text{ on ker E}
\Rightarrow
\exists\lambda>0:\ q_a+\lambda E^*E\succeq0.
```

Semidefinite exact:

```math
\boxed{
q_a\ge0\text{ on ker E}
\iff
\forall\varepsilon>0\ \exists\lambda_\varepsilon>0:
q_a+\varepsilon I+\lambda_\varepsilon E^*E\succeq0.
}
```

## Default-Auftrag — DUAL-CERT-1.0

Versuche einen rigorosen Completion-Certificate bei `a=1.0`.

Pflichtreihenfolge:

1. Basis/Trunkierung **vor** Resultat festlegen.
2. Exakte/Arb `E_±`-Momentzeilen bauen.
3. Hermiteschen `2x2` Completionblock oder scalar `lambda` optimieren.
4. Finite PSD intervallzertifizieren.
5. Analytische/Arb Tail-Untergrenze für das ungelöste Komplement beweisen.
6. Nur wenn 4+5 zusammen grün sind: fixed-window theorem promoten.

### Firewalls

- finite Ritz/SDP PSD ohne tail ist kein Beweis;
- `a<=0.8` wäre keine Erweiterung des aktuellen Literaturbenchmarks;
- scalar Turán failure falsifiziert NP-GAP nicht;
- existence of arbitrary completion != Weil pole matrix `P`;
- all-a completion ist RH-hart;
- Registry/Arbeitsdefinition unverändert.

## Status

```text
COMMON-JUMP / Q0                         ✓[M]
Suzuki screw redundancy                 ✓[M]
D as new arithmetic object             ×[M]
necessary autocorrelation gauges       ✓[M]
scalar Turan exactness                  ×[M]
rank-2 completion duality              ✓[M]
certified completion at a>0.8          ?[O]
all-a NP-GAP                            ?[O]
forward Object-X architecture          ✓[M]_part
full positive Object-X / RH            ?[O]
```
