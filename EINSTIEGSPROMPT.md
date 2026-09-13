# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**
> Dieser Text ist der operative Einstieg für eine neue Session. Ältere Stände sind über Git erhalten und nicht als heutige Arbeitsanweisung zu verwenden.

## Kopierbarer Arbeitskontext

Ich arbeite am Forschungsprogramm **Objekt X** zur Riemannschen Hypothese im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor und Research Assistant. Prüfe zu Beginn den aktuellen `main`-Stand direkt im Repository. Verwende kanonische mathematische Quellen vor älteren Navigations- oder Archivdokumenten. Keine Behauptung darf durch einen Merge oder einen positiven numerischen Test still promotet werden.

### Kanonische operative Quellen

Lies in dieser Reihenfolge:

1. `CURRENT-FRONT.md`
2. `00-uebersicht/AKTUELLER_STAND.md`
3. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md`
4. `00-uebersicht/DAG.md`
5. `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md`
6. `00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`

Für den aktuellen mathematischen Strang zusätzlich:

- `audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md`
- `audits/P11_OX_GRAM_GATE2_AND_OX_GEN_2026-09-12.md`

### Governance

Für **Objekt X** übernimmt ChatGPT sämtliche GitHub-/Repository-Arbeiten: Dateien ändern, Branches, Commits/Pushes, PRs, Kommentare und Merges. Perplexity dient ausschließlich als externer Reviewer/Auditor und nimmt keine Repo-Mutationen vor.

Statusmarker strikt trennen: `✓[M]`, `✓[K/M]`, `✓[M]_part`, `✓[M]_neg`, `×[M]`, `?[O]`. Reviewer-/Governance-Status erzeugen keine automatische mathematische Promotion.

---

## Aktueller mathematischer Stand

### 1. Strong Terminal / C6

Für jedes feste `0<R<S` gilt im **ungeraden P11-Graphraum** der fixed-pair Strong-Terminal/C6-Abschluss aus positivem Wurzelanker plus R42.51.

Scope-Firewall: keine Radienuniformität, keine Operatornormkonvergenz, kein vollständiger gerader Sektor, keine Object-X- oder RH-Folgerung.

### 2. Prime-Power-AR(1)-Struktur

Exakt:

```math
C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4},
\qquad
C_{kk}^{(p)}=(\log p)p^{-k/2}.
```

Der Exponent `3/4` ist durch Martingalmultiplizität plus Weil-Diagonale erzwungen.

Mit `q_p=p^{-1/2}`:

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}q_p^{|j-k|}.
```

Tail/Root:

```math
T_q^*T_q=R_q-uu^*,
\qquad
T_q^*T_q+uu^*=R_q.
```

P11-Restseite:

```math
R_R^*R_R=\sum_{p,k}w_{p,k}Z_{p,k,R}^*Z_{p,k,R}.
```

Cross-prime Root-Gram ist fensterloser Bulk, kein Boundaryterm.

### 3. Endliche OX-GRAM-Normalform

Für `a<=1`:

```math
Q_{B_a}=G_a^+-N_a,
\qquad
N_a=c_aI+C_a.
```

`G_a^+` besteht aus positiven Prime-Kanal-, Log-Multiplikator- und logarithmischen `log|D|`-Formen.

Die bloße Existenz eines kontraktiven Faktors ist **kein** nichtzirkulärer Object-X-Gate: Bei bereits bekannter lokaler Positivität kann er rückwärts aus `Q_{B_a}` konstruiert werden. Diese Existenzfront ist geschlossen; offen ist **Kanonizität**.

### 4. CERT-HARDEN

Die endlichen Gate-1/Gate-2-Checker wurden vor Merge von PR #98 gehärtet und liefen auf demselben Exact Head GREEN:

- Normalisierung Realraum/Fourier für `a=0.5,0.8,1.0`, fail-closed Residualbälle;
- explizite Bernoulli- und `sinc`-Restbälle;
- Arb-sichere Prime-Power-Cutoffs und Endpunktfehler;
- Gate 2: Arb 512 Bit, Dirichletbasis `N<=14`, beide Paritäten, drei Radien, **42/42** strikt positive Cholesky-Blöcke.

Diese Zertifikate sind endlich und kein RH-/unendlichdimensionaler Positivitätsbeweis.

### 5. Aktuelle Hauptfront OX-GEN

Suzukis Kernteil liefert exakt

```math
R_0(v,v)
=-2\left(\int\cosh\frac x2\,v\right)^2
+2\left(\int\sinh\frac x2\,v\right)^2.
```

Damit ist `R_0` höchstens Rang 2; gerade Parität liefert die negative `cosh`-Rang-1-Richtung, ungerade Parität die positive `sinh`-Rang-1-Richtung.

Dieselbe Exponentialfamilie erscheint auf der Primseite:

```math
p^{-1/2}=e^{-\log p/2},
\qquad
R_p(j,k)=p^{-|j-k|/2},
\qquad
w_{p,k}=\log p\,p^{-k/2}.
```

**OX-GEN:** Ist `R_0` ein intrinsischer Rand-/Defektterm derselben Exponentialstruktur, die die Prime-Power-Geometrie normiert? Gesucht ist eine explizite, vorwärts konstruierte Geometrie ohne Verwendung der fertigen Weilform, `B_a^{1/2}`, eines unbekannten Forminfimums oder RH.

`R_1` und der Skalarblock `c_aI` bleiben offen.

---

## Nächste Default-Arbeitsfolge

1. **OX-GEN-A:** bei `a=0.5` die `cosh/sinh`-Momentfunktionale innerhalb der Prime-/`log|D|`-Featuregeometrie isolieren.
2. **GENERATOR-CLASS:** eine natürliche Generator-Klasse vor einem möglichen No-Go festschreiben, sodass positive und negative Ausgänge beide vorab logisch möglich sind.
3. **OX-GEN-B:** expliziten Intertwiner/Defektmechanismus konstruieren oder die definierte Klasse ausschließen.
4. Parallel die AR(1)/Martingal-Faktorisierung als eigenständigen RH-unabhängigen Satz verschriftlichen; ausdrücklich nicht als Objekt X.

---

## Nicht reaktivieren

Folgende Deutungen sind zurückgezogen oder gesperrt:

- PR91-Zeugenmatrix sei Rang 1;
- `3/4` sei bloße Dämpfung;
- Vier-Boundary-Erklärung der Interior/Baseline-Differenz;
- cross-prime sei Fensterrand;
- „Nichtunitarität = genau Hub“;
- matched cutoff als Object-X-Mechanismus;
- OX-REN/OX-REN' als Hauptfront;
- Radiusvariation durch bloßes Ersetzen von `R=1` im PR97-Checker;
- klassische `H^{1/2}`-/Douglas-Terminologie für den Kernel `1/|x-y|`;
- globaler Kollaps von `||I-W^*W||`;
- `0.603`-Koeffizientenratio als Konstante;
- weitere reine OX-GRAM-Existenztests ohne nichtzirkulären Mechanismus.

---

## Offene Nebenfronten

- PR #91: analytischer Draft, kein übertragener unabhängiger Exact-Head-GREEN.
- PR #49 / SW1 salvage: Candidate-only Nebenfront, kein stiller Merge.
- R37/G4c: separat offen, Beziehung zu OX-GEN/Object X unresolved.
- Historische R43-COND-/FD23-/Flagfragen: eigene offene Quantoren, aber nicht aktuelle Default-Aufgabe.

---

## Arbeitsregel

Ein Schritt zählt als Object-X-Hauptfront-Fortschritt nur, wenn er einen expliziten Geometrieteil konstruiert, eine vorab definierte Architekturklasse ausschließt, eine notwendige gemeinsame Generatorstruktur beweist oder eine tatsächlich benötigte mathematische Lücke schließt.

Ein Falsifikationsgate zählt nur, wenn **beide Ausgänge vorab logisch möglich** sind.

Es gibt weiterhin **keine vollständige Object-X-Realisierung und keinen RH-Beweis**.
