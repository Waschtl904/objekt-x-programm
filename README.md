# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

Gesucht wird eine gemeinsame arithmetisch-analytische Hilbert-/Gram-Geometrie, in der Primzahlpotenz- und archimedische Beiträge der vollständigen Weil-Form aus demselben Mechanismus hervorgehen. Arbeitsname: **Objekt X**.

> **Redaktioneller Stand: 13. September 2026.**  
> Eine vollständige Objekt-X-Realisierung und ein Beweis der Riemannschen Hypothese liegen nicht vor.

## Hier beginnen

1. **[Aktueller Arbeitsstand](CURRENT-FRONT.md)**
2. **[Nullpol-Reklassifikation](audits/P11_NULLPOLE_STRATEGIC_RECLASSIFICATION_2026-09-13.md)**
3. **[Aktueller Stand](00-uebersicht/AKTUELLER_STAND.md)**
4. **[Forschungsroadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)**
5. **[DAG](00-uebersicht/DAG.md)**
6. **[Objekt-X-Arbeitsdefinition](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)**

## Aktueller Schlüsselfund: die OX-GEN-A-Ebene ist die Pol-Ebene

Für

```math
M(v)(s)=\int_{\mathbb R}v(x)e^{(s-1/2)x}\,dx
```

gilt exakt

```math
\boxed{E_-(v)=M(v)(0),\qquad E_+(v)=M(v)(1).}
```

Die beiden OX-GEN-A-Funktionale sind damit die zwei Polfunktionale der expliziten Formel.

Auf der Nullpolklasse

```math
\mathscr D_{NP}=\{v:M(v)(0)=M(v)(1)=0\}
```

verschwinden exakt

```math
R_0(v,w),
\qquad
\|\mathcal Ev\|^2.
```

Connes–Consani Proposition C.1 zeigt zugleich, dass die **globale** Weil-Vorzeichenbedingung nach Vorgabe einer endlichen Nullstellenmenge `F superset {0,1}` ohne nichttriviale Zeta-Nullstelle RH-äquivalent bleibt.

Damit ist die Nullpolrestriktion logisch mit dem globalen RH-Scope verträglich.

## Strategische Korrektur

OX-GEN-A bleibt mathematisch `✓[M]`: Prime-Kanäle und `R_0` besitzen weiterhin die exakte gemeinsame Translation-/Reflexions-Generatorstruktur.

Die Schlussfolgerung, diese Rang-2-Struktur sei ein **notwendiger** Object-X-Hauptengpass, wird jedoch zurückgezogen: Auf der global RH-äquivalenten Nullpolklasse ist ihr gesamter Zielterm identisch Null.

Dasselbe gilt strategisch für die auf OX-GEN-A aufbauende POS-DIL-Kette PR #101--#105. Ihre Mathematik bleibt erhalten und bildet künftig die

```text
AUX-POS-DIL / full-class pole-layer route.
```

Sie ist nützlich für eine vollständige Testklassenrealisierung, aber nicht mehr Default-Priorität.

## Neue Hauptfront: NULLPOL-CORE

Für `0<a<=1` gilt lokal im kanonischen Suzuki-Gauge

```math
Q_{B_a}=G_a^+-c_aI-R_0-R_1.
```

Auf der lokalen Nullpol-Unterklasse reduziert sich dies exakt zu

```math
\boxed{
Q_{B_a}(v)
=G_a^+(v)-c_a\|v\|_2^2-R_1(v,v).
}
```

Die Hauptfront liegt damit bei:

1. **NP-R1:** exakter Kernel, Parität, Translation-/Generatorstruktur von `R_1` auf Nullpol;
2. **NP-SCALAR:** Skalarledger im explizit fixierten Suzuki-Gauge beziehungsweise gaugeinvariante Reststruktur;
3. **NP-COMMON:** ein gemeinsamer Prime-/archimedischer Mechanismus für `R_1` plus Skalarrest, der auf Nullpol nichttrivial bleibt.

### Verbindliche Gate-Regel

Ein neuer Object-X-Hauptfront-Schritt zählt nur dann als Klassenschnitt oder Konstruktionsfortschritt, wenn er nach

```math
M(v)(0)=M(v)(1)=0
```

noch nichttrivial wirkt.

## Was aus POS-DIL erhalten bleibt

Die folgenden Sätze bleiben vollständig gültig:

- [OX-GEN-A](audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md)
- [POS-DIL-1](audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md)
- [POS-DIL-2A](audits/P11_POS_DIL_2_UNIT_GAIN_FEATURE_SHORTING_NOGO_2026-09-13.md)
- [erster äußerer Prime-Shell](audits/P11_POS_DIL_2B_FIRST_EXTERIOR_PRIME_SHELL_2026-09-13.md)
- [Radius `0<a<=1`](audits/P11_POS_DIL_2C_EXTERIOR_SHELL_RADIUS_0_1_2026-09-13.md)
- [exakte Shell-Gauge / positive `R_0`-Absorption](audits/P11_POS_DIL_2C_EXACT_SHELL_GAUGE_R0_ABSORPTION_2026-09-13.md)

Sie werden nicht widerrufen, sondern strategisch als auxiliary klassifiziert.

## Wichtige Firewalls

- Die globale RH-Äquivalenz der Nullpolklasse ist keine fixed-`a`-Äquivalenz.
- Das Verschwinden von `R_0` löst weder `R_1` noch den Skalarledger.
- Der nackte Wert `c_a` ist unter der exakten Außen-Prime-cutoff-Gauge nicht isoliert invariant; eine Gaugewahl oder gaugeinvariante Formulierung bleibt nötig.
- Es gibt keine vollständige Weil-Gram-Identität, keine Object-X-Realisierung und keinen RH-Beweis.

## Nachweise und Orientierung

Ausarbeitungen: [papers/](papers/) · Prüfberichte: [audits/](audits/) · Theorem-/Reviewstatus: [Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md). Ein Merge oder erfolgreicher Test ist keine mathematische Promotion.

Für neue Arbeitssitzungen: [Einstiegsprompt](EINSTIEGSPROMPT.md).

Lizenz: [CC BY 4.0](LICENSE) · Zitierangaben: [CITATION.cff](CITATION.cff).
