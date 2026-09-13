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

mit explizit positiver Featureform `G_a^+` und explizitem Defekt `N_a` geschrieben werden. Die bloße Existenz eines kontraktiven Faktors ist kein nichtzirkulärer Objekt-X-Gate, weil sie bei bekannter Positivität rückwärts aus `Q_{B_a}` konstruiert werden kann.

**OX-GEN-A ist positiv geschlossen.** Mit

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

Mit `P(E_+,E_-)=(E_-,E_+)`, `J=-P` gilt

```math
R_0(v,w)=\langle\mathcal Ev,J\mathcal Ew\rangle.
```

Die engere Prime-only-Idee bleibt negativ entschieden: die volle Prime-Gram-Form descendiert nicht auf den Rang-2-Quotienten, und die reine Quotientenkovarianz lässt den absoluten Maßstab frei.

**POS-DIL-1 liefert nun erstmals eine positive Hilbertumgebung dieses gemeinsamen Rang-2-Blocks.** Setzt man

```math
S=\operatorname{diag}(-1,1)=D_n/\lambda_n=2\rho'(0),
```

so erzwingen Spiegelung und normalisierter Prime-Generator in der natürlichen Companion-Klasse

```math
PMP=M,
\qquad SMS=M
```

bereits `M=tI`; die minimale blockpositive Wahl ist exakt `M=I`. Eine volle positive `rho`-invariante Metrik existiert dagegen nicht außer `M=0`.

Für jede endliche nichtleere Prime-Power-Menge `N` mit

```math
\kappa_N=\sum_{n\in N}w_n\lambda_n^2
```

ist die explizite Prime-moment-Abbildung

```math
V_Nv=\kappa_N^{-1/2}
\bigl(\sqrt{w_n}\,\mathcal EK_nv\bigr)_{n\in N}
```

isometrisch auf der Generator-Ebene:

```math
\boxed{\|V_Nv\|^2=|E_+(v)|^2+|E_-(v)|^2.}
```

Mit `\mathbb P_N=\oplus P` entsteht aus derselben positiven Zielraumabbildung

```math
\boxed{R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.}
```

Für `n=p^k`, `q_p=p^{-1/2}` verbindet sich diese Konstruktion zusätzlich exakt mit der AR(1)-Root-Geometrie:

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.
```

Damit ist `OX-GEN-A2'` **partiell** positiv geschlossen (`✓[M]_part`): die minimale positive Rang-2-Masse und `R_0` sitzen in derselben vorwärts aus echten Prime-Kanalausgängen konstruierten Hilbertumgebung. Noch offen ist die stärkere Frage, ob diese Momentabbildung kontraktiv in der vollständigen positiven Featuregeometrie `G_a^+` sitzt.

Der aktive Gate ist deshalb **POS-DIL-2 / FEATURE-SHORTING**. Eine erste scharfe Form lautet

```math
\|\mathcal Ev\|^2\stackrel?\le G_a^+(v).
```

Ein PASS würde den Rang-2-Baustein als kanonische kontraktive Postkompression/Shorting der vorhandenen positiven Prime-/`log|D|`-Geometrie verankern. Ein FAIL würde nur diese natürliche Klasse ausschließen; POS-DIL-1 bliebe bestehen.

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
