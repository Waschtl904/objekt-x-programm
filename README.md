# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

Gesucht wird eine gemeinsame arithmetisch-analytische Hilbert-/Gram-Geometrie,
in der Primzahlpotenz- und archimedische Beiträge der vollständigen Weil-Form
aus demselben Mechanismus hervorgehen. Arbeitsname: **Objekt X**.

> **Redaktioneller Stand: 13. September 2026.**
> Eine vollständige Objekt-X-Realisierung und ein Beweis der Riemannschen
> Hypothese liegen nicht vor.

## Hier beginnen

1. **[Aktueller Arbeitsstand](CURRENT-FRONT.md)** — operative POS-DIL-Front und nächster Gate.
2. **[Aktueller Stand](00-uebersicht/AKTUELLER_STAND.md)** — kurze Zusammenfassung für neue Sessions.
3. **[Forschungsroadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)** — Strategie und Nebenfronten.
4. **[Abhängigkeitsgraph](00-uebersicht/DAG.md)** — kompakte logische/strategische Kanten.
5. **[Objekt-X-Arbeitsdefinition](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)** — was eine vollständige Realisierung leisten muss.

Zentrale Quellen des aktuellen Strangs:

- [AR(1)/Weil-Tail/OX-GRAM-Konsolidierung](audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md)
- [Gate 2 / OX-GEN](audits/P11_OX_GRAM_GATE2_AND_OX_GEN_2026-09-12.md)
- [OX-GEN-A gemeinsamer Exponentialgenerator](audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md)
- [POS-DIL-1 Prime-moment Hilbertization](audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md)
- [POS-DIL-2 Unit-Gain Feature-Shorting No-Go](audits/P11_POS_DIL_2_UNIT_GAIN_FEATURE_SHORTING_NOGO_2026-09-13.md)

## Erreichter Meilenstein

Der integrierte [positive Wurzelanker-Beweis](audits/P11_R43_POSITIVE_ROOT_ANCHOR_STRONG_TERMINAL_2026-09-07.md) plus R42.51 liefert **Strong Terminal/C6 für jedes feste `0<R<S` im ungeraden P11-Graphraum**. Keine Radienuniformität, Operatornormkonvergenz, vollständige Objekt-X-Realisierung oder RH-Folgerung wird beansprucht.

## Aktuelle Forschungsaufgabe

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

Die natürliche Companion-Symmetrie erzwingt `M=tI`; der minimale blockpositive Begleiter ist `M=I`. Eine exakte positive `rho`-invariante Same-space-Hilbertmetrik existiert nur trivial.

Für jede endliche nichtleere Prime-Power-Menge `N` ist

```math
V_Nv=\kappa_N^{-1/2}
\bigl(\sqrt{w_n}\,\mathcal EK_nv\bigr)_{n\in N}
```

mit

```math
\|V_Nv\|^2=|E_+(v)|^2+|E_-(v)|^2,
```

und derselbe positive Zielraum trägt über `\mathbb P_N=\oplus P` die Form

```math
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.
```

Für `n=p^k`, `q_p=p^{-1/2}` gilt

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S,
```

also eine exakte Brücke zur AR(1)-Root-Komponente. `OX-GEN-A2'` ist damit `✓[M]_part`.

### POS-DIL-2A: unit-gain Shorting fällt

Der anschließend vorab definierte Gate

```math
\|\mathcal Ev\|^2\stackrel?\le G_a^+(v)
```

ist bereits bei `a=1/2` falsch. Eine explizite `H_0^1`-Plateaufolge erfüllt

```math
|R_0(v_\varepsilon,v_\varepsilon)|
=\|\mathcal Ev_\varepsilon\|^2
\to32\sinh^2\frac14,
```

aber

```math
G_{1/2}^+(v_\varepsilon)
\to1+\sqrt2(\log2)^2,
```

und exakt

```math
32\sinh^2\frac14>2>1+\sqrt2(\log2)^2.
```

Damit kann die vorhandene `G_{1/2}^+`-Featuremasse `R_0` nicht mit Gain `1` als kontraktive Zielraumkompression tragen. Ausgeschlossen sind sowohl `C F^+=V` mit `||C||<=1` als auch jede allgemeinere kontraktive Target-observable-Realisierung innerhalb derselben Feature-Norm.

Der notwendige Plateau-Massendefekt ist

```math
\boxed{
\delta_0
=32\sinh^2\frac14
-1-\sqrt2(\log2)^2
>\frac5{32}>0.
}
```

### Neue Front

**POS-DIL-2B / INTRINSIC-MASS-AUGMENTATION:** Welche schwächste zusätzliche positive Masse entsteht **intrinsisch** aus bereits vorhandener Prime-/AR(1)-Root/Hub-/`log|D|`-Geometrie, liefert am Plateau mindestens `delta_0` und trägt `R_0` im selben positiven Umraum?

Kandidaten wie globale Prime-Kanäle außerhalb des lokalen Suzuki-Cutoffs dürfen untersucht werden, aber ihre Buchungsrichtung muss nichtzirkulär sein. Eine beliebige Diagonalergänzung oder das bloße Umbenennen des offenen `c_aI`-Blocks zählt nicht.

`r_1` und `c_aI` bleiben offen.

## Nachweise und Orientierung

Ausarbeitungen: [papers/](papers/) · Prüfberichte: [audits/](audits/).
Theorem- und Reviewbuchungen stehen in der [Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md). Ein Merge oder erfolgreicher Test ist keine mathematische Promotion.

Für neue Arbeitssitzungen: [Einstiegsprompt](EINSTIEGSPROMPT.md). Historische Statusangaben sind keine aktuelle Arbeitsanweisung.

Lizenz: [CC BY 4.0](LICENSE) · Zitierangaben: [CITATION.cff](CITATION.cff).

## Attribution & Priorität

Dieses Repository ist unter [CC-BY-4.0](LICENSE) veröffentlicht. Nutzung erfordert Namensnennung.

- Attributionsakte und Zitiervorlage: [`ATTRIBUTION.md`](ATTRIBUTION.md)
- Maschinenlesbare Zitationsdaten: [`CITATION.cff`](CITATION.cff)
- Kanarienvogel und Herkunftsmarker: [`/.canary`](.canary), [`SECURITY.md`](SECURITY.md)
- Automatisch aktualisierter Hashbaum der Kernddateien: [`INTEGRITY.md`](INTEGRITY.md)
