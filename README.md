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
- [POS-DIL-2C Radius 0<a<=1](audits/P11_POS_DIL_2C_EXTERIOR_SHELL_RADIUS_0_1_2026-09-13.md)

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

Die Prime-moment-Abbildung realisiert die minimale positive Rang-2-Masse

```math
\|V_Nv\|^2=\|\mathcal Ev\|^2
```

und denselben `R_0`-Block über eine Zielraum-Involution.

### Außenshell als intrinsische positive Prime-Masse

Definiere

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\},
\qquad c_n=\frac12\log n.
```

Für jeden Kanal in diesem geometrisch definierten ersten Außenshell sind die beiden verschobenen Fenster disjunkt. Daher

```math
\boxed{\|K_nv\|^2=2\|v\|^2.}
```

Die positive Shellform

```math
H_a^{out}(v,w)=\sum_{n\in\mathscr S_a^{out}}
\frac{\Lambda(n)}{\sqrt n}\langle K_nv,K_nw\rangle
```

ist somit echte Prime-Kanalenergie und keine beliebige Diagonalergänzung.

### Vollständige Radiusfortsetzung im lokalen Scope

Für `0<a<=1` liefert der vorhandene Log-Multiplikator

```math
G_a^+(v)\ge(-\log a)\|v\|^2,
```

während

```math
\|\mathcal Ev\|^2\le4\sinh(a)\|v\|^2.
```

Eine rein elementare siebenintervallige Prime-Power-Abschätzung beweist

```math
\boxed{-\log a+2B_a^{out}>4\sinh a
\qquad(0<a\le1).}
```

Daher gilt auf dem gesamten dokumentierten Radiusbereich

```math
\boxed{
\|\mathcal Ev\|^2
\le G_a^+(v)+H_a^{out}(v).
}
```

Damit trägt die augmentierte positive Form `R_0` kontraktiv:

```math
\boxed{
\begin{pmatrix}
G_a^++H_a^{out}&R_0\\
R_0&G_a^++H_a^{out}
\end{pmatrix}\succeq0,
\qquad0<a\le1.
}
```

Die **Radiusfrage ist damit geschlossen**. Der verbliebene Engpass ist nicht mehr positive Masse, sondern ihre exakte Buchung.

## Aktuelle Front: EXACT-SHELL-BOOKING

Die Außenkanalenergie darf nicht einfach zusätzlich zur Weilform addiert werden. Gesucht ist eine kanonische Bilanz, die die volle Form unverändert lässt.

Priorisierte Fragen:

- Wo sitzt die Außenkanal-Identitätsmasse vor der lokalen Cutoff-Umschreibung?
- Teleskopieren Differenzen benachbarter Shiftshells?
- Liefert
  ```math
  T_q^*T_q+uu^*=R_q
  ```
  die notwendige Root-/Hub-Gegenbuchung?
- Ist die POS-DIL-1-Amplitude `1-u_k` der richtige Buchungsindikator?

Erst nach einer exakten Antwort darf eine Verbindung zum offenen `c_aI`- oder `r_1`-Block behauptet werden.

Es gibt weiterhin keine vollständige Weil-Gram-Identität, keine Object-X-Realisierung und keinen RH-Beweis.

## Nachweise und Orientierung

Ausarbeitungen: [papers/](papers/) · Prüfberichte: [audits/](audits/) · Theorem-/Reviewstatus: [Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md). Ein Merge oder erfolgreicher Test ist keine mathematische Promotion.

Für neue Arbeitssitzungen: [Einstiegsprompt](EINSTIEGSPROMPT.md).

Lizenz: [CC BY 4.0](LICENSE) · Zitierangaben: [CITATION.cff](CITATION.cff).
