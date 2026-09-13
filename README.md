# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

Gesucht wird eine gemeinsame arithmetisch-analytische Hilbert-/Gram-Geometrie, in der Primzahlpotenz- und archimedische Beiträge der vollständigen Weil-Form aus demselben Mechanismus hervorgehen. Arbeitsname: **Objekt X**.

> **Redaktioneller Stand: 13. September 2026.**  
> Eine vollständige Objekt-X-Realisierung und ein Beweis der Riemannschen Hypothese liegen nicht vor.

## Hier beginnen

1. **[Aktueller Arbeitsstand](CURRENT-FRONT.md)** — operative POS-DIL-Front.
2. **[Aktueller Stand](00-uebersicht/AKTUELLER_STAND.md)** — kurze Zusammenfassung.
3. **[Forschungsroadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)** — Strategie.
4. **[DAG](00-uebersicht/DAG.md)** — Abhängigkeiten und Firewalls.
5. **[Objekt-X-Arbeitsdefinition](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)**.

Aktuelle Audits:

- [AR(1)/Weil-Tail/OX-GRAM](audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md)
- [OX-GEN-A](audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md)
- [POS-DIL-1 Prime-moment Hilbertization](audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md)
- [POS-DIL-2A unit-gain No-Go](audits/P11_POS_DIL_2_UNIT_GAIN_FEATURE_SHORTING_NOGO_2026-09-13.md)
- [POS-DIL-2B erster äußerer Prime-Shell](audits/P11_POS_DIL_2B_FIRST_EXTERIOR_PRIME_SHELL_2026-09-13.md)

## Forschungsstand

### Gemeinsame Generator-Ebene

Mit

```math
\mathcal Ev=(E_+(v),E_-(v)),
\qquad
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2})
```

gilt

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E.
```

Suzukis `r_0` ist dieselbe Darstellung auf der archimedischen Seite:

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

### POS-DIL-1

Die natürliche Companion-Klasse liefert den minimalen positiven Begleiter `M=I`; eine volle positive `rho`-invariante Same-space-Metrik existiert nur trivial.

Die Prime-moment-Abbildung

```math
V_Nv=\kappa_N^{-1/2}(\sqrt{w_n}\,\mathcal EK_nv)_{n\in N}
```

realisiert

```math
\|V_Nv\|^2=\|\mathcal Ev\|^2,
\qquad
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.
```

### POS-DIL-2A: bestehende positive Featuremasse reicht nicht

Bei `a=1/2` ist

```math
\|\mathcal Ev\|^2\le G_{1/2}^+(v)
```

falsch; eine explizite Plateaufolge liefert einen notwendigen positiven Massendefekt `delta_0>5/32`. Damit ist unit-gain Shorting innerhalb der unveränderten lokalen `G_{1/2}^+`-Feature-Norm ausgeschlossen.

### POS-DIL-2B: intrinsische positive Reparatur durch den ersten äußeren Prime-Shell

Definiere ohne Anpassung an `delta_0`

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\},
\qquad c_n=\frac12\log n.
```

Für jeden solchen äußeren Kanal sind die beiden verschobenen Fenster disjunkt, daher exakt

```math
\boxed{\|K_nv\|^2=2\|v\|^2.}
```

Die Shellform

```math
H_a^{out}(v,w)=\sum_{n\in\mathscr S_a^{out}}
\frac{\Lambda(n)}{\sqrt n}\langle K_nv,K_nw\rangle
```

liefert somit echte positive lokale Prime-Masse.

Bei `a=1/2` enthält der erste Shell insbesondere `3,4,5`. Zusammen mit dem bereits vorhandenen Log-Multiplikator erhält man uniform

```math
G_{1/2}^+(v)+H_{1/2}^{out}(v)>\frac83\|v\|^2,
```

während

```math
\|\mathcal Ev\|^2<\frac83\|v\|^2.
```

Folglich

```math
\boxed{
\|\mathcal Ev\|^2
\le G_{1/2}^+(v)+H_{1/2}^{out}(v)
}
```

für alle Testfunktionen. Die augmentierte positive Form trägt `R_0` kontraktiv und liefert einen positiven Schurblock.

Das ist der erste positive Reparaturbaustein nach dem POS-DIL-2A-No-Go, dessen Zusatzmasse vollständig aus bereits vorhandenen echten Prime-Kanälen und ihren Weilgewichten stammt.

## Aktuelle Front: POS-DIL-2C / SHELL-BOOKING-AND-RADIUS

Der zentrale Engpass ist jetzt **Buchung statt bloßer Positivität**. Die Außenkanalenergie ist real, darf aber nicht einfach zusätzlich zur lokalisierten Weilform addiert werden.

Zu klären sind:

1. **Shell-Buchung:** Gibt es eine kanonische Gegenbuchung, Teleskopierung oder AR(1)-Root/Hub-Zerlegung, die den positiven Außenshell in einer exakten gemeinsamen Geometrie erscheinen lässt, ohne die volle Weilform zu verändern?
2. **Radius:** Für welche `0<a<=1` dominiert derselbe geometrische Shell die Momentmasse?

Die Shellmasse wird ausdrücklich nicht mit `c_aI` identifiziert. `r_1`, `c_aI`, eine volle Weil-Gram-Identität, Object X und RH bleiben offen.

## Nachweise und Orientierung

Ausarbeitungen: [papers/](papers/) · Prüfberichte: [audits/](audits/).  
Theorem- und Reviewbuchungen: [Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md). Ein Merge oder erfolgreicher Test ist keine mathematische Promotion.

Für neue Arbeitssitzungen: [Einstiegsprompt](EINSTIEGSPROMPT.md).

Lizenz: [CC BY 4.0](LICENSE) · Zitierangaben: [CITATION.cff](CITATION.cff).

## Attribution & Priorität

Dieses Repository ist unter [CC-BY-4.0](LICENSE) veröffentlicht. Nutzung erfordert Namensnennung.

- [`ATTRIBUTION.md`](ATTRIBUTION.md)
- [`CITATION.cff`](CITATION.cff)
- [`.canary`](.canary), [`SECURITY.md`](SECURITY.md)
- [`INTEGRITY.md`](INTEGRITY.md)
