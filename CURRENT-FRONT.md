# CURRENT FRONT — Objekt X / OX-GEN

> **Operative Kopfschicht — zuerst lesen.**
> **Redaktioneller Stand:** 13. September 2026; keine Registry-Promotion.
> **Konsolidierungsquellen:** [AR(1)/Weil-Tail/OX-GRAM-Audit](audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md) und [Gate-2/OX-GEN-Audit](audits/P11_OX_GRAM_GATE2_AND_OX_GEN_2026-09-12.md).
> **Strategie:** [kanonische Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md).
> **Suchgegenstand:** [Objekt-X-Arbeitsdefinition](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md).
> **Buchungen:** [Theorem-/Review-Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).

Diese Datei ordnet die Arbeit; sie beweist nichts. Der aktuelle `main`-Head und PR-Zustände werden live aus GitHub gelesen. Bei Konflikten ist die kanonische mathematische Quelle im benannten Scope maßgeblich.

## 1. Erreichter Meilenstein

Der integrierte positive Wurzelanker plus R42.51 liefert Strong Terminal/C6 für jedes **feste** `0<R<S` im **ungeraden P11-Graphraum**.

**Scope:** keine Radienuniformität, keine Operatornormkonvergenz, kein gerader Gesamtsektor, keine vollständige Objekt-X-Realisierung und keine RH-Folgerung.

Diese C6-Front wird nicht erneut geöffnet, solange kein tatsächlicher Eingang fällt.

## 2. Belastbare Prime-Power-Struktur

Seit PR #98 ist auf `main` dokumentiert:

```math
C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4},
\qquad
C_{kk}^{(p)}=(\log p)p^{-k/2}.
```

Damit ist `3/4` durch Weil-Diagonale plus Martingalmultiplizität erzwungen. Nach Weil-Diagonalnormalisierung gilt

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}\,p^{-|j-k|/2},
\qquad q_p=p^{-1/2},
```

also eine AR(1)/Kac–Murdock–Szegő-Struktur je Primast. Für den Tail-Faktor gilt

```math
T_q^*T_q=R_q-uu^*,
\qquad
T_q^*T_q+uu^*=R_q,
```

und die P11-Restseite besitzt die exakte Weil-Tail-Normalform

```math
R_R^*R_R=\sum_{p,k}w_{p,k}Z_{p,k,R}^*Z_{p,k,R}.
```

Cross-prime Root-Gram ist fensterloser Bulk, kein räumlicher Boundaryterm.

**Spur B:** Diese AR(1)/Martingal-Faktorisierung ist theorem-ready, RH-unabhängig und wird getrennt verschriftlicht. Sie ist ausdrücklich noch nicht Objekt X.

## 3. Endliche Suzuki-/OX-GRAM-Normalform

Für `a<=1` liegt die lokalisierte Weilform in der endlichen Form

```math
Q_{B_a}(v)=G_a^+(v)-N_a(v),
\qquad
N_a=c_aI+C_a,
```

vor. `G_a^+` besteht aus explizit positiven Prime-Kanal-, Log-Multiplikator- und logarithmischen `log|D|`-Formen. Der Kernel `1/|x-y|` wird **nicht** als klassische `H^{1/2}`-/Douglas-Seminorm bezeichnet.

Die reine Existenzfrage

```text
N_a <= G_a^+ ?
```

ist als Objekt-X-Gate geschlossen: Bei bereits bekannter lokaler Weil-Positivität kann ein Kontraktor rückwärts aus `Q=G_a^+-N_a` konstruiert werden. Das ist zirkulär und liefert keine intrinsische Geometrie.

**Übrig bleibt Kanonizität.**

## 4. CERT-HARDEN — geschlossen im dokumentierten endlichen Scope

PR #98 enthält zwei gehärtete read-only Zertifikatswege.

### Gate 1 / Normalisierung

Für `a in {0.5,0.8,1.0}` werden Realraum- und Fourierdarstellung mit Arb verglichen. Gehärtet sind:

- Bernoulli-Tail von `r_1''` als expliziter Restball;
- Prime-Power-Cutoff ausschließlich über Arb-Vergleiche;
- Log-Endpunktfehler ohne Float-Obergrenze;
- hebbare `sinc`-Singularität mit explizitem Taylor-Rest;
- fail-closed Null-Einschluss für alle A–F/C2-Residualbälle.

Der Exact-Head-CI vor Merge von PR #98 war GREEN für alle drei Radien.

### Gate 2 / finite OX-GRAM-Blöcke

Arb 512 Bit, Dirichletbasis bis `N=14`, drei Radien, beide Paritätssektoren: **42/42** verschachtelte Blöcke besitzen strikt positive Arb-Cholesky-Pivots; kein `Cholesky-FAIL`.

**Firewall:** Das ist ein endliches Zertifikat und kein unendlichdimensionaler Weil-Positivitäts- oder RH-Beweis.

## 5. Aktuelle Hauptfront: OX-GEN

Suzukis Teilkern

```math
r_0''(t)=-2\cosh(t/2)
```

liefert exakt

```math
R_0(v,v)
=-2\left(\int\cosh\frac x2\,v(x)\,dx\right)^2
+2\left(\int\sinh\frac x2\,v(x)\,dx\right)^2.
```

Damit ist `R_0` Rang höchstens 2; im geraden Sektor bleibt eine negative Rang-1-Richtung, im ungeraden eine positive Rang-1-Richtung.

Dieselbe Exponentialfamilie tritt auf der Primseite auf:

```math
p^{-1/2}=e^{-(\log p)/2},
\qquad
R_p(j,k)=p^{-|j-k|/2},
\qquad
w_{p,k}=\log p\,p^{-k/2}.
```

### OX-GEN

**Offene Frage:** Ist `R_0` als Rand-/Defektterm derselben Exponentialstruktur darstellbar, die die Prime-Power-Kanäle normiert? Gesucht ist eine explizite, nichtzirkuläre Konstruktion aus natürlichen Generatoren wie `{e^{+x/2},e^{-x/2},K_n,log|D|-Geometrie}`, ohne `Q_{B_a}`, `B_a^{1/2}`, das unbekannte Forminfimum oder RH rückwärts zu verwenden.

Positive Antwort: expliziter geometrischer Baustein. Negative Antwort: Klassen-No-Go, sofern die Generator-Klasse vorher natürlich und eng definiert wurde.

**Scope:** `R_1` und der Skalar `c_aI` bleiben offen; OX-GEN ist ein Teilproblem.

## 6. Nächste Gates

1. **OX-GEN-A** — bei `a=0.5` die `cosh/sinh`-Momentfunktionale innerhalb der Prime-/`log|D|`-Featureabbildung isolieren.
2. **GENERATOR-CLASS** — vor einem No-Go die natürliche Generator-Klasse festschreiben; beide Ausgänge müssen logisch möglich sein.
3. **OX-GEN-B** — expliziten Intertwiner oder Klassen-No-Go suchen.
4. **Spur B parallel:** AR(1)/Martingal-Faktorisierung theorem-ready verschriftlichen.

Keine weiteren reinen `mu_max`-Dimensionssweeps als Hauptfront: ohne neuen Mechanismus reproduzieren sie bekannte lokale Weil-Positivität.

## 7. Gesperrte Deutungen

Nicht wieder als aktive Front verwenden:

- Rang-1-PR91-Zeugenmatrix;
- `3/4` als bloße Beschränktheitsdämpfung;
- Vier-Boundary-Erklärung der Interior/Baseline-Differenz;
- cross-prime als Fensterrand;
- „Nichtunitarität = genau Hub“;
- Suzuki-Basispunkt-Vierterm als `2I`-Renormierung;
- matched cutoff `epsilon=e^{-A_L}` als Mechanismus;
- OX-REN/OX-REN' als Hauptfront;
- Radiusvariation durch bloßes Ersetzen von `R=1` im PR97-Checker;
- neue speziell angepasste Witness-Runden ohne vorab definierten Architekturtest;
- reine OX-GRAM-Existenztests, die nur bekannte Weil-Positivität reproduzieren;
- `H^{1/2}`-/klassische Douglas-Terminologie für den Kernel `1/|x-y|`;
- die Aussage, `||I-W^*W||` kollabiere; kollabierend beobachtet wurde der kleinste relative Eigenwert;
- die radius-/sektorabhängige `0.603`-Koeffizientenkoinzidenz als Konstante.

## 8. Offene PRs / Governance

- PR #91 bleibt analytischer Draft; kein unabhängiger Exact-Head-GREEN ist durch PR #98 übertragen worden.
- PR #49 ist formal Ready, bezeichnet sich inhaltlich aber weiterhin als `candidate only; no merge requested yet`; deshalb kein stiller Merge.
- PR #92/#95 und andere Governance-/Archivstränge bleiben getrennt.
- Registry, `ACTIVE_FRONT.yaml` und Arbeitsdefinition werden durch diese Front nicht automatisch geändert.

## 9. Arbeitsregel

Ein Schritt zählt auf der Objekt-X-Hauptfront nur, wenn er mindestens eines leistet:

1. konstruiert einen expliziten Teil der gemeinsamen Gramgeometrie;
2. schließt eine ganze vorab definierte Architekturklasse aus;
3. beweist eine notwendige Struktur des gemeinsamen Prime-/Archimedean-Generators;
4. schließt eine tatsächlich benötigte Domain-/Normalisierungs-/Konvergenzlücke.

Ein Falsifikationsgate zählt nur, wenn **beide Ausgänge vorab logisch möglich** sind. Bloße Umschreibungen, Witness-Wertabgleiche oder Positivitätsreproduktionen ohne neuen Mechanismus sind Nebenarbeit.
