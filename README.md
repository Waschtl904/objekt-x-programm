# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

Gesucht wird eine gemeinsame arithmetisch-analytische Hilbert-/Gram-Geometrie,
in der Primzahlpotenz- und archimedische Beiträge der vollständigen Weil-Form
aus demselben Mechanismus hervorgehen. Arbeitsname: **Objekt X**.

> **Redaktioneller Stand: 13. September 2026.**
> Eine vollständige Objekt-X-Realisierung und ein Beweis der Riemannschen
> Hypothese liegen nicht vor.

## Hier beginnen

1. **[Aktueller Arbeitsstand](CURRENT-FRONT.md)** — operative OX-GEN-Front und nächster Gate.
2. **[Aktueller Stand](00-uebersicht/AKTUELLER_STAND.md)** — kurze Zusammenfassung für neue Sessions.
3. **[Forschungsroadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)** — Strategie und Nebenfronten.
4. **[Abhängigkeitsgraph](00-uebersicht/DAG.md)** — kompakte logische/strategische Kanten.
5. **[Objekt-X-Arbeitsdefinition](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)** — was eine vollständige Realisierung leisten muss.

Zentrale Quellen des aktuellen Strangs:

- [AR(1)/Weil-Tail/OX-GRAM-Konsolidierung](audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md)
- [Gate 2 / OX-GEN](audits/P11_OX_GRAM_GATE2_AND_OX_GEN_2026-09-12.md)
- [OX-GEN-A gemeinsamer Exponentialgenerator](audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md)

## Erreichter Meilenstein

Der integrierte [positive Wurzelanker-Beweis](audits/P11_R43_POSITIVE_ROOT_ANCHOR_STRONG_TERMINAL_2026-09-07.md)
liefert den starken Normalenlimes. Zusammen mit dem ausdrücklich übernommenen
Tangentialsatz **R42.51** folgt **Strong Terminal/C6 für jedes feste
`0 < R < S` im ungeraden P11-Graphraum**.

Dieser Satz beansprucht weder Uniformität über alle Radien noch
Operatornormkonvergenz, den geraden Gesamtsektor oder die vollständige Objekt-X-Realisierung.

## Aktuelle Forschungsaufgabe

Die Prime-Power-Seite besitzt eine exakte Weil-dekorierte AR(1)/Martingalstruktur. Für `a<=1` kann die lokalisierte Suzuki-/Weilform als

```math
Q_{B_a}=G_a^+-N_a
```

mit explizit positiver Featureform `G_a^+` und explizitem Defekt `N_a` geschrieben werden. Die bloße Existenz eines kontraktiven Faktors ist jedoch kein nichtzirkulärer Objekt-X-Gate, weil sie bei bekannter Positivität rückwärts aus `Q_{B_a}` konstruiert werden kann.

**OX-GEN-A ist inzwischen positiv geschlossen.** Mit

```math
E_\pm(v)=\int e^{\pm x/2}v(x)\,dx,
\qquad
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2})
```

gilt exakt

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=\lambda_n\operatorname{diag}(-1,1)\mathcal E,
```

und Suzukis elementarer archimedischer Anteil ist das negative Charakter derselben Darstellung:

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
r_0(\log n)=-4\lambda_n^2.
```

Mit der Spiegelung `P(E_+,E_-)=(E_-,E_+)` gilt

```math
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Damit ist erstmals eine exakte gemeinsame Prime-/Archimedean-Generatorgeometrie isoliert. Sie ist jedoch indefinit und noch **keine** positive Object-X-Realisierung.

Die engere Idee, den absoluten `R_0`-Koeffizienten allein aus den diskreten Daten `{w_n,lambda_n}` zu gewinnen, ist negativ entschieden: die volle Prime-Gram-Form descendiert nicht auf den Rang-2-Quotienten, und die Quotientenkovarianz lässt den Maßstab frei.

Der nächste Gate ist daher **OX-GEN-A2' / POSITIVE-DILATION**: Kann die kanonische Translation-/Reflexions-Geometrie intrinsisch in die positive Prime-/`log|D|`-Featuregeometrie eingebettet oder als Schur-/Defektterm einer positiven Erweiterung realisiert werden?

`r_1` und der dominante Skalar `c_aI` bleiben offen.

Parallel wird die exakte Prime-Power-AR(1)/Martingal-Faktorisierung als eigenständige, RH-unabhängige Mathematik verschriftlicht — ausdrücklich **nicht** als Objekt X.

## Nachweise und Orientierung

Ausarbeitungen: [papers/](papers/) · Prüfberichte: [audits/](audits/).
Theorem- und Reviewbuchungen stehen in der
[Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).
Ein Merge oder erfolgreicher Test ist keine mathematische Promotion.

Für neue Arbeitssitzungen: [Einstiegsprompt](EINSTIEGSPROMPT.md).
Das ältere Forschungsjournal bleibt über den [Gesamtindex](INDEX.md) erreichbar;
historische Statusangaben sind keine aktuelle Arbeitsanweisung.

Lizenz: [CC BY 4.0](LICENSE) · Zitierangaben: [CITATION.cff](CITATION.cff).

## Attribution & Priorität

Dieses Repository ist unter [CC-BY-4.0](LICENSE) veröffentlicht. Nutzung erfordert Namensnennung.

- Attributionsakte und Zitiervorlage: [`ATTRIBUTION.md`](ATTRIBUTION.md)
- Maschinenlesbare Zitationsdaten: [`CITATION.cff`](CITATION.cff)
- Kanarienvogel und Herkunftsmarker: [`/.canary`](.canary), [`SECURITY.md`](SECURITY.md)
- Automatisch aktualisierter Hashbaum der Kernddateien: [`INTEGRITY.md`](INTEGRITY.md)
