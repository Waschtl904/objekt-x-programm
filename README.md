# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

Gesucht wird eine gemeinsame arithmetisch-analytische Hilbert-/Gram-Geometrie, in der Primzahlpotenz- und archimedische Beiträge der vollständigen Weil-Form aus demselben Mechanismus hervorgehen. Arbeitsname: **Objekt X**.

> **Redaktioneller Stand: 13. September 2026.**  
> Eine vollständige Objekt-X-Realisierung und ein Beweis der Riemannschen Hypothese liegen nicht vor.

## Hier beginnen

1. **[Aktueller Arbeitsstand](CURRENT-FRONT.md)**
2. **[Aktueller Stand](00-uebersicht/AKTUELLER_STAND.md)**
3. **[Forschungsroadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)**
4. **[DAG](00-uebersicht/DAG.md)**
5. **[Objekt-X-Arbeitsdefinition](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)**

Aktuelle Audits:

- [OX-GEN-A](audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md)
- [POS-DIL-1 Prime-moment Hilbertization](audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md)
- [POS-DIL-2A Unit-Gain No-Go](audits/P11_POS_DIL_2_UNIT_GAIN_FEATURE_SHORTING_NOGO_2026-09-13.md)
- [POS-DIL-2B erster äußerer Prime-Shell](audits/P11_POS_DIL_2B_FIRST_EXTERIOR_PRIME_SHELL_2026-09-13.md)
- [POS-DIL-2C Radius `0<a<=1`](audits/P11_POS_DIL_2C_EXTERIOR_SHELL_RADIUS_0_1_2026-09-13.md)
- [POS-DIL-2C exakte Shell-Gauge und `R_0`-Absorption](audits/P11_POS_DIL_2C_EXACT_SHELL_GAUGE_R0_ABSORPTION_2026-09-13.md)

## Forschungsstand

### Gemeinsame Generator-Ebene

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E,
```

```math
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Die Prime-moment-Abbildung realisiert die minimale Rang-2-Masse und denselben `R_0`-Block in einem positiven Zielraum.

### Außen-Prime-Kanäle als exakte Cutoff-Gauge

Für jeden Prime-Power-Kanal mit `c_n>a` sind die beiden verschobenen Fenster disjunkt. Deshalb gilt polarisiert

```math
w_n\langle K_nv,K_nw\rangle
=2w_n\langle v,w\rangle.
```

Für jede endliche Außenkanalmenge `J` folgt

```math
H_{a,J}=b_JI,
\qquad
b_J=2\sum_{n\in J}\frac{\Lambda(n)}{\sqrt n}.
```

Damit ist die Transformation

```math
G_a^+\mapsto G_a^++H_{a,J},
\qquad
c_a\mapsto c_a+b_J
```

eine **exakte Prime-cutoff-Gauge** der lokalisierten Weilform:

```math
Q_{B_a}
=(G_a^++H_{a,J})-(c_a+b_J)I-R_0-R_1.
```

Für den ersten geometrischen Außenshell `a<c_n<=2a` lautet das Skalarinkrement

```math
A_{e^{4a}}-A_{e^{2a}}.
```

Der isolierte `c_a`-Wert ist damit nicht ohne Gauge-Fixierung kanonisch.

### Positive Absorption des elementaren archimedischen `R_0`-Layers

Für den ersten Außenshell setze

```math
A_a^{out}=G_a^++H_a^{out}.
```

Auf dem gesamten lokalen Bereich `0<a<=1` gilt

```math
A_a^{out}\succeq\mathcal E^*\mathcal E.
```

Definiere

```math
D_a^{out}=A_a^{out}-\mathcal E^*\mathcal E\succeq0
```

und

```math
L_+=E_++E_-.
```

Dann exakt

```math
\mathcal E^*\mathcal E-R_0=L_+^*L_+,
```

also

```math
\boxed{
P_a^{(0)}:=A_a^{out}-R_0
=D_a^{out}+L_+^*L_+\succeq0.
}
```

Die vollständige lokalisierte Form wird damit, ohne ihren Wert zu verändern,

```math
\boxed{
Q_{B_a}=P_a^{(0)}-c_a^{out}I-R_1,
\qquad0<a\le1.
}
```

Der elementare `r_0`-/`R_0`-Block ist somit exakt in einen positiven gemeinsamen Prime-/archimedischen Block absorbiert.

## Aktuelle Front: OX-GEN-B / `R_1` und gaugeinvarianter Skalarrest

Übrig bleibt der exakte Rest

```math
c_a^{out}I+R_1.
```

Die nächste Arbeit konzentriert sich auf die Struktur von `R_1` und eine gaugeinvariante Behandlung des skalaren Ledgers. Der nackte Wert `c_a` wird nicht mehr als kanonisches Einzelobjekt vorausgesetzt.

Zu prüfen sind insbesondere Kernel, Parität, Translation-/Reflexionssymmetrien und eine mögliche gemeinsame Generator-/Feature-Realisierung von `R_1` plus Skalarrest.

Es gibt weiterhin keine vollständige Weil-Gram-Identität, keine Object-X-Realisierung und keinen RH-Beweis.

## Nachweise und Orientierung

Ausarbeitungen: [papers/](papers/) · Prüfberichte: [audits/](audits/) · Theorem-/Reviewstatus: [Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md). Ein Merge oder erfolgreicher Test ist keine mathematische Promotion.

Für neue Arbeitssitzungen: [Einstiegsprompt](EINSTIEGSPROMPT.md).

Lizenz: [CC BY 4.0](LICENSE) · Zitierangaben: [CITATION.cff](CITATION.cff).
