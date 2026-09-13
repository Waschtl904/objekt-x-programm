# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

Gesucht wird eine gemeinsame arithmetisch-analytische Hilbert-/Gram-Geometrie,
in der Primzahlpotenz- und archimedische Beiträge der vollständigen Weil-Form
aus demselben Mechanismus hervorgehen. Arbeitsname: **Objekt X**.

> **Redaktioneller Stand: 13. September 2026.**
> Eine vollständige Objekt-X-Realisierung und ein Beweis der Riemannschen
> Hypothese liegen nicht vor.

## Hier beginnen

1. **[Aktueller Arbeitsstand](CURRENT-FRONT.md)** — operative OX-GEN-Front, geschlossene Zertifikationsgates und gesperrte alte Deutungen.
2. **[Aktueller Stand](00-uebersicht/AKTUELLER_STAND.md)** — kurze Zusammenfassung für neue Sessions.
3. **[Forschungsroadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)** — aktuelle Strategie und Nebenfronten.
4. **[Abhängigkeitsgraph](00-uebersicht/DAG.md)** — kompakte logische/strategische Kanten.
5. **[Objekt-X-Arbeitsdefinition](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)** — was eine vollständige Realisierung leisten muss.

Zentrale Konsolidierungsquellen des aktuellen Strangs:

- [AR(1)/Weil-Tail/OX-GRAM-Konsolidierung](audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md)
- [Gate 2 / OX-GEN](audits/P11_OX_GRAM_GATE2_AND_OX_GEN_2026-09-12.md)

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

Die operative Hauptfrage ist daher **OX-GEN**: Suzukis `r_0''` besitzt eine exakte Rang-2-Zerlegung über `cosh(x/2)` und `sinh(x/2)`, während dieselbe Exponentialfamilie in `p^{-1/2}=e^{-\log p/2}`, der AR(1)-Korrelation und den Weilgewichten erscheint. Gesucht ist ein **expliziter, nichtzirkulärer gemeinsamer Generator-/Defektmechanismus**.

Die endlichen Normalisierungs- und Gate-2-Zertifikate wurden vor Merge von PR #98 gehärtet und waren auf dem geprüften Exact Head GREEN. Das nächste aktive Gate ist deshalb **OX-GEN-A bei `a=0.5`**, nicht weitere Zertifikationshärtung.

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
