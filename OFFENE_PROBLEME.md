# Offene Probleme — aktuelle OX-GEN-Priorität

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [AKTUELLER_STAND](00-uebersicht/AKTUELLER_STAND.md), [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](00-uebersicht/DAG.md), [Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).
>
> **Wichtige Korrektur gegenüber älteren Fassungen:** fixed-pair Strong Terminal/C6 ist im ausgewiesenen ungeraden P11-Scope nicht mehr offen. Historische R43-/NEU-Probleme bleiben Provenienz und Nebenfragen, nicht heutige Default-Priorität.

---

## Priorität 0 — OX-GEN-A

### `[OX-GEN-A]` Gemeinsamen Exponentialgenerator lokalisieren `?[O]`

Für `a=0.5` die beiden Funktionale

```math
v\mapsto\int\cosh(x/2)v(x)\,dx,
\qquad
v\mapsto\int\sinh(x/2)v(x)\,dx
```

innerhalb der vorhandenen Prime-/`log|D|`-Featuregeometrie isolieren.

Motivation: Suzukis exakter Rang-2-Term

```math
R_0(v,v)
=-2\left(\int\cosh\frac x2\,v\right)^2
+2\left(\int\sinh\frac x2\,v\right)^2
```

verwendet dieselbe Exponentialfamilie wie

```math
p^{-1/2}=e^{-\log p/2},
\qquad
R_p(j,k)=p^{-|j-k|/2},
\qquad
w_{p,k}=\log p\,p^{-k/2}.
```

**Erfolgskriterium:** eine explizite vorwärts konstruierte Relation, nicht aus der fertigen Weilform rückwärts definiert.

**Firewall:** Ein bloßer numerischer Wertabgleich oder eine GNS-/Quadratwurzel-Faktorisierung von bereits bekannter Positivität zählt nicht.

---

## Priorität 1 — GENERATOR-CLASS

### `[GENERATOR-CLASS]` Natürliche zulässige Klasse definieren `?[O]`

Vor einem No-Go ist eine enge, mathematisch natürliche Klasse von Generatorabbildungen festzuschreiben, gebaut aus Daten wie

```text
e^{+x/2}, e^{-x/2}, K_n, Prime-AR(1), log|D|-Geometrie.
```

Die Klasse darf nicht post hoc auf ein gewünschtes Ergebnis zugeschnitten werden.

**Gate-Regel:** Positive Konstruktion und negativer Ausgang müssen vorab beide logisch möglich sein.

---

## Priorität 2 — OX-GEN-B

### `[OX-GEN-B]` Konstruktion oder Klassen-No-Go `?[O]`

Nach Festlegung der Generator-Klasse:

- entweder einen expliziten nichtzirkulären Intertwiner/Defektmechanismus konstruieren, der den `R_0`-Term intrinsisch erklärt;
- oder die gesamte definierte Klasse ausschließen.

Eine positive Antwort wäre ein **echter geometrischer Teilbaustein** in Richtung Objekt X, aber noch keine vollständige Realisierung.

---

## Priorität 3 — verbleibende archimedische Teile

### `[OX-R1]` Regulärer Korrektor `R_1` `?[O]`

Wie wird der verbleibende reguläre `r_1''`-Block in eine gemeinsame Prime-/Archimedean-Geometrie eingebettet?

### `[OX-SCALAR]` Skalarblock `c_a I` `?[O]`

Wie entsteht der explizite Skalarblock intrinsisch aus derselben Geometrie, statt als nachträglich abgezogene Konstante?

Diese Fragen werden erst dann Hauptfront, wenn OX-GEN-A/B eine tragfähige Generatorstruktur liefert oder deren Klasse ausschließt.

---

## Priorität 4 — vollständiger Objekt-X-Pfad

### `[OX-CANDIDATE]` Genuine X candidate `?[O]`

Gesucht wird eine intrinsische gemeinsame Geometrie mit Hilbert-/Mediatorraum, kanonischer Abbildung, Prime-Power- und archimedischem Kanal, gemeinsamer nichtorthogonaler Kopplung, Testklasse, Normalisierung und Nicht-Zirkularität.

### `[OX-WEIL-GRAM]` Exakte volle Weil-Gram-Identität `?[O]`

Für einen konkreten Kandidaten separat zu beweisen:

```math
Q_W(f,g)=\langle T_Xf,T_Xg\rangle_{\mathcal K_X}
```

auf der richtigen vollständig normalisierten Testklasse.

### `[OX-REALIZATION]` Object-X-Realisierung `?[O]`

Erst gemeinsame intrinsische Geometrie plus exakte volle Weil-Gram-Identität bilden eine Realisierung.

### `[OX-WEIL-SCOPE]` Weil-Kriterium-Scope `?[O]`

Nach einer Realisierung ist separat zu prüfen, ob die realisierte Form/Testklasse exakt den benötigten klassischen Weil-Kriterium-Scope erfüllt.

### `RH` `?[O]`

Unverändert offen.

---

## Spur B — eigenständige Mathematik

### `[AR1-WRITEUP]` Prime-Power-AR(1)/Martingal-Faktorisierung

Die exakte Struktur

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
\qquad
T_q^*T_q+uu^*=R_q
```

ist theorem-ready und soll separat, RH-unabhängig und **nicht als Objekt X** verschriftlicht werden.

Ein Literaturbefund kann Neuheitsindikator sein, ist aber kein Prioritätsbeweis.

---

## Separate / geparkte Probleme

### R37/G4c `?[O]`

Separat offen. Beziehung zur OX-GEN-/X-Route ist unresolved; keine notwendige Kante wird behauptet.

### Historische R43-COND-/FD23-/Flagfragen

Einzelne quantitative Fragen bleiben in ihren eigenen Quantoren offen. Sie sind jedoch **keine** Voraussetzungen des abgeschlossenen fixed-pair-C6-Pfads und derzeit nicht Default-Priorität.

### PR #91 — Source descent / Weil separation

Analytischer Draft; kein unabhängiger Exact-Head-GREEN wird durch die aktuelle Front übertragen.

### PR #49 / SW1 salvage

Candidate-only Nebenfront. Kein stiller Merge und keine unbewiesene Object-X-Kante.

---

## Geschlossen / nicht erneut öffnen ohne neuen Widerspruch

### Fixed-pair Strong Terminal / C6

Im ungeraden P11-Graphraum für jedes feste `0<R<S` verfügbar aus positivem Wurzelanker plus R42.51.

### OX-GRAM-Existenzfrage

Die Frage nach der bloßen Existenz eines kontraktiven Faktors ist als Object-X-Gate geschlossen/vakuant, weil bei bekannter lokaler Positivität eine rückwärts aus `Q` definierte Faktorisierung existiert. Offen bleibt nur eine **kanonische nichtzirkuläre** Konstruktion.

### CERT-HARDEN im dokumentierten endlichen Scope

Normalisierungs- und Gate-2-Checker wurden in PR #98 interval-gehärtet und waren vor Merge auf demselben Exact Head GREEN.

---

## Gesperrte Altdeutungen

Nicht als neue offene Probleme wieder einführen:

- PR91-Zeugenmatrix Rang 1;
- `3/4` als freie Dämpfung;
- Vier-Boundary-Erklärung;
- cross-prime als Boundary;
- „Nichtunitarität = Hub“;
- matched cutoff / OX-REN;
- reiner Radius-Swap im PR97-Checker;
- klassische `H^{1/2}`-/Douglas-Deutung von `1/|x-y|`;
- globaler Defektnorm-Kollaps;
- `0.603` als Konstante;
- weitere reine OX-GRAM-Existenzsweeps ohne neuen Mechanismus.

Historische NEU-/Wres-/HH-Probleme bleiben über Git, INDEX, STATUS und die ursprünglichen Dokumente als Provenienz verfügbar.
