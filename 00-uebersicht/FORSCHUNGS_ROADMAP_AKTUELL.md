# Objekt X — kanonische Forschungsroadmap v2.9

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Operative Front: [CURRENT-FRONT](../CURRENT-FRONT.md).  
> **Strategische Korrektur:** POS-DIL bleibt mathematisch erhalten, ist aber nach Identifikation der Polfunktionale keine Default-Hauptfront mehr.

---

## 1. Gesicherte Basis

- fixed-pair Strong Terminal/C6 im dokumentierten ungeraden P11-Scope;
- Prime-Power-AR(1)/Weil-Tail;
- lokale Suzuki-Normalform
  ```math
  Q_{B_a}=G_a^+-c_aI-R_0-R_1;
  ```
- OX-GEN-A und POS-DIL #101--#105 als exakte full-class Pole-layer-Struktur.

---

## 2. Nullpol-Reduktion `✓[M]` + importierter Weil-Scope

```math
M(v)(s)=\int v(x)e^{(s-1/2)x}\,dx,
```

```math
\boxed{E_-=M(v)(0),\qquad E_+=M(v)(1).}
```

Daher auf

```math
\mathscr D_{NP}=\ker M(0)\cap\ker M(1)
```

```math
\boxed{R_0=0,\qquad\mathcal E=0.}
```

Connes–Consani Proposition C.1: Die globale Weil-Vorzeichenbedingung bleibt nach Vorgabe einer endlichen Nullstellenmenge `F superset {0,1}`, `F cap Z = empty`, RH-äquivalent.

**Firewall:** keine Behauptung einer fixed-`a`-RH-Äquivalenz.

---

## 3. Neue Forschungsregel — NULLPOL-CORE

Ein Object-X-Hauptfront-Schritt muss mindestens eines leisten:

1. konstruiert einen nichttrivialen gemeinsamen Prime-/archimedischen Mechanismus auf `\mathscr D_{NP}`;
2. schließt eine vorab definierte Architekturklasse **auch nach** Nullpolrestriktion aus;
3. beweist eine notwendige Struktur von `R_1` oder des skalaren/gaugeinvarianten Restes auf Nullpol;
4. schließt eine Domain-/Konvergenz-/Normalisierungslücke, die für diesen Nullpolpfad tatsächlich benötigt wird.

Ein Schritt, dessen gesamter Zielterm auf `\mathscr D_{NP}` verschwindet, ist auxiliary und bekommt keine automatische Hauptfront-Kante.

---

## 4. OX-GEN-A / POS-DIL — neue Rolle

### Mathematischer Status

Unverändert gültig:

- gemeinsame `rho/P/E`-Generatorstruktur;
- Prime-moment Hilbertization;
- unit-gain full-class No-Go;
- Außen-Prime-Shell;
- Radiusdomination `0<a<=1`;
- exakte Prime-cutoff-Gauge;
- positive `R_0`-Absorption.

### Strategischer Status

```text
AUX-POS-DIL / full-class pole-layer route
```

Diese Route bleibt wertvoll für eine spätere volle Testklassenrealisierung, ist aber kein notwendiger Engpass für einen RH-äquivalenten Nullpolpfad.

---

## 5. Default-Priorität A — NP-R1

Rekonstruiere `R_1` aus der kanonischen Suzuki-/OX-GRAM-Quelle **vor** jeder neuen Architekturidee.

Zu bestimmen:

- polarisierter Kernel;
- geschlossene Formel für `r_1''` und hebbare Singularitäten;
- Parität und Spiegelung;
- Translation-/Faltungsstruktur;
- Verhalten unter `M(v)(0)=M(v)(1)=0`;
- natürliche positive/indefinite Generatorfamilie oder ein vorab definierter No-Go.

Ein positiver Kandidat zählt nur, wenn er auf Nullpol nicht trivialisiert.

---

## 6. Default-Priorität B — NP-SCALAR

Im kanonischen Suzuki-Gauge bleibt

```math
c_aI
```

auf Nullpol bestehen.

PR #105 zeigt zugleich die cutoff-gauge-Abhängigkeit des isolierten Skalarlagers. Daher zwei parallele, aber kompatible Wege:

1. **canonical-Suzuki gauge:** Gauge explizit fixieren und die Herkunft von `c_a` dort untersuchen;
2. **gauge-invariant route:** eine Kombination aus Skalarledger und positiver Featureenergie/R1 finden, die unter exakten Außen-Prime-Gauges invariant ist.

Kein künstliches `tI` als Lösung.

---

## 7. Default-Priorität C — NP-COMMON

Nach NP-R1/NP-SCALAR prüfen:

> Entstehen `R_1` und der skalare Rest aus demselben Prime-/archimedischen Mechanismus?

Bevorzugt werden:

- echte Features/Intertwiner;
- relative Operator- oder Spurklassenstrukturen;
- Schur-/Shorting-Mechanismen mit vorwärts definierten Daten;
- semilokale/`log|D|`-Strukturen, sofern sie auf Nullpol nichttrivial bleiben.

Nicht bevorzugt: getrennte post-hoc Gegenbuchungen.

---

## 8. Danach: genuine X candidate

```text
NULLPOL-CORE geometry
        |
        | requires nontrivial NP-R1 + NP-SCALAR mechanism
        v
genuine X candidate ?[O]
        |
        | separate exact proof
        v
full Weil-Gram identity on RH-equivalent test class ?[O]
        |
        v
Object-X realization ?[O]
        |
        | criterion-scope verification
        v
RH
```

Die Rückbindung muss ausdrücklich prüfen, dass die realisierte Testklasse exakt im Connes–Consani/Weil-Scope liegt.

---

## 9. Separate / auxiliary routes

### AUX-POS-DIL

Vollklassen-Pole-layer-Geometrie #101--#105. Kein Widerruf, keine Default-Priorität.

### AR1-WRITEUP

Prime-Power-AR(1)/Martingal-Faktorisierung als eigenständige RH-unabhängige Mathematik.

### Weitere

- R37/G4c separat;
- PR #91 analytischer Draft;
- PR #49 Candidate-only.

---

## 10. Firewalls

- `R_0=0` auf Nullpol bedeutet nicht, dass die volle Weilform positiv ist.
- Die globale RH-Äquivalenz der Nullpolklasse bedeutet nicht fixed-`a`-Äquivalenz.
- `c_a` ist ohne Gaugewahl kein isoliertes kanonisches Object-X-Objekt.
- POS-DIL ist nicht mathematisch widerlegt; nur strategisch zurückgestuft.
- Keine Registry-Promotion durch diese Roadmap.

---

## 11. Explizit offen

```text
NP-R1
NP-SCALAR / gauge-invariant scalar remainder
NP-COMMON
genuine X candidate
exact full Weil-Gram identity on RH-equivalent null-pole scope
Object-X realization
criterion-scope verification
RH
R37/G4c [separate]
```
