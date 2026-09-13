# Offene Probleme — aktuelle NULLPOL-CORE-Priorität

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [Nullpol-Audit](audits/P11_NULLPOLE_STRATEGIC_RECLASSIFICATION_2026-09-13.md), [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](00-uebersicht/DAG.md), [Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).

## Neu geschlossen / geklärt

### `[NP-POLES]` Polfunktionale `✓[M]`

```math
E_-=M(v)(0),\qquad E_+=M(v)(1).
```

Auf

```math
\mathscr D_{NP}=\ker M(0)\cap\ker M(1)
```

gilt

```math
R_0=0,\qquad\|\mathcal Ev\|^2=0.
```

### `[NP-WEIL-SCOPE]` globaler restricted Weil-Scope `✓[K/M]`

Connes–Consani Proposition C.1: RH bleibt äquivalent zur globalen Weil-Vorzeichenbedingung nach Vorgabe einer endlichen Nullstellenmenge `F superset {0,1}`, solange `F` keine nichttriviale Zeta-Nullstelle enthält.

**Firewall:** keine fixed-`a`-Äquivalenz behauptet.

### `[OX-GEN-A]`

Mathematik bleibt `✓[M]`; strategisch als Pole-layer auxiliary reklassifiziert. Kein notwendiger Klassenschnitt auf der Nullpolroute.

### `[AUX-POS-DIL]`

PR #101--#105 bleiben vollständig mathematisch gültig, werden aber als auxiliary full-class route geführt.

---

## Priorität 0 — `[NP-R1]` `?[O]`

Bestimme `R_1` auf der Nullpolklasse.

Pflichtfragen:

1. exakter polarisierter Kernel;
2. geschlossene Form von `r_1''` einschließlich hebbarer Singularität;
3. Paritäts- und Spiegelungssymmetrien;
4. Translation-/Faltungs-/Spektraldarstellung;
5. bleibt eine natürliche Generator- oder Featureklasse nach Nullpol nichttrivial?
6. falls nein: enger vorab definierter Klassen-No-Go.

Ein Ergebnis, das nur außerhalb `\mathscr D_{NP}` wirkt, zählt nicht als Hauptfront-Fortschritt.

---

## Priorität 1 — `[NP-SCALAR]` `?[O]`

Im canonical-Suzuki-Gauge bleibt auf Nullpol

```math
c_a\|v\|^2
```

als nichtannihilierbarer Skalarledger bestehen.

Zu klären:

- intrinsische Herkunft im fixierten Suzuki-Gauge;
- Verhalten unter den exakten Außen-Prime-cutoff-Gauges aus PR #105;
- Existenz einer gaugeinvarianten Skalar-Restgröße;
- Zusammenhang mit `R_1` statt isolierter post-hoc Gegenmasse.

**Nicht erlaubt:** beliebiges `tI` als Lösung.

---

## Priorität 2 — `[NP-COMMON]` `?[O]`

Gesucht ist ein gemeinsamer Mechanismus für `R_1` plus Skalarrest, der auf `\mathscr D_{NP}` nichttrivial ist.

Beidseitig offenes Gate vor jedem Test:

> Verkleinert oder konstruiert der Mechanismus die zulässige Geometrie noch nach `M(v)(0)=M(v)(1)=0`?

Nur bei **ja** zählt er als Object-X-Hauptfront.

---

## Priorität 3 — vollständiger Object-X-Pfad

- `[OX-CANDIDATE]` genuine X candidate `?[O]`;
- `[OX-WEIL-GRAM]` exakte volle Weil-Gram-Identität auf einer RH-äquivalenten Nullpol-Testklasse `?[O]`;
- `[OX-REALIZATION]` Object-X-Realisierung `?[O]`;
- `[OX-WEIL-SCOPE]` exakte Rückbindung an das klassische/restricted Weil-Kriterium `?[O]`;
- RH `?[O]`.

---

## Auxiliary / separate

### AUX-POS-DIL

Full-class Pole-layer-Geometrie #101--#105; korrekt, aber nicht Default-Priorität.

### AR1-WRITEUP

Prime-Power-AR(1)/Martingal-Faktorisierung als eigenständige RH-unabhängige Mathematik.

### Separat

- R37/G4c;
- PR #91;
- PR #49.

---

## Präzisierungen, die nicht erneut verloren gehen dürfen

- komplex:
  ```math
  R_0(v,v)=-2\operatorname{Re}(E_+(v)\overline{E_-(v)});
  ```
- Companion-Block semidefinit genau für `t>=1`, strikt positiv für `t>1`;
- Anti-Kovarianzform hat freien `b in C`, nicht nur einen reellen Parameter;
- numerischer alte POS-DIL-No-Go sitzt in der externen Sektorauswertung im geraden Sektor;
- `c_a` ist unter Außen-Prime-cutoff-Gauge nicht isoliert invariant.

---

## Gesperrte Überdehnungen

Nicht behaupten:

- Nullpolklasse löse bereits den Skalar- oder `R_1`-Term;
- globale Nullpol-RH-Äquivalenz gelte automatisch für jedes feste Fenster;
- OX-GEN-A/POS-DIL seien falsch;
- POS-DIL sei weiterhin notwendiger Hauptengpass;
- `c_a` sei ohne Gaugewahl kanonisch;
- Object X oder RH seien bewiesen.
