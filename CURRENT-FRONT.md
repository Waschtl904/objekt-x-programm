# CURRENT FRONT — Objekt X / OX-GEN

> **Operative Kopfschicht — zuerst lesen.**
> **Redaktioneller Stand:** 12. September 2026; keine Registry-Promotion.
> **Konsolidierungsquellen:** [AR(1)/Weil-Tail/OX-GRAM-Audit](audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md) und [Gate-2/OX-GEN-Audit](audits/P11_OX_GRAM_GATE2_AND_OX_GEN_2026-09-12.md).
> **Strategie:** [kanonische Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md).
> **Suchgegenstand:** [Objekt-X-Arbeitsdefinition](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md).
> **Buchungen:** [Theorem-/Review-Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).

Diese Datei ordnet die Arbeit; sie beweist nichts. Der aktuelle `main`-Head und heutige PR-Zustände werden live aus GitHub gelesen. Bei Konflikten ist die kanonische mathematische Quelle im benannten Scope maßgeblich.

## 1. Erreichter Meilenstein bleibt gültig

Der integrierte positive Wurzelanker plus R42.51 liefert Strong Terminal/C6 für jedes **feste** `0<R<S` im **ungeraden P11-Graphraum**. Keine Radienuniformität, Operatornormkonvergenz, vollständige Objekt-X-Realisierung oder RH-Folgerung wird ergänzt.

Diese C6-Front wird nicht erneut geöffnet, solange kein tatsächlicher Eingang fällt.

## 2. Belastbare Prime-Power-Struktur

Die seit PR #97 konsolidierte Struktur lautet:

- exaktes Ledger
  `C_jk^(p)=(log p)p^min(j,k)p^{-3(j+k)/4}`;
- Weil-Diagonale `C_kk=(log p)p^{-k/2}`;
- erzwungener Exponent `3/4`;
- AR(1)/Kac–Murdock–Szegő-Normalform
  `C_jk=sqrt(w_j w_k) p^{-|j-k|/2}`;
- Tail-Faktor `T_q^*T_q=R_q-uu^*` und Hub/Root-Ergänzung `+uu^*`;
- exakte Weil-Tail-Normalform der P11-Restseite;
- cross-prime Root-Gram ist fensterloser Bulk, kein räumlicher Boundaryterm.

Diese Aussagen sind exakte Kanal-/Koeffizientenstruktur, noch keine volle Objekt-X-Realisierung.

## 3. OX-GRAM: endliche Normalform, aber Existenzgate geschlossen

Für `a<=1` liegt Suzukis lokalisierte Weilform in der endlichen Form

```math
Q_{B_a}(v)=G_a^+(v)-N_a(v)
```

vor. `G_a^+` besteht aus explizit positiven **logarithmischen Formraum-/`log|D|`-**, Prime-Kanal- und Log-Multiplikator-Formen; `N_a=c_aI+C_a` enthält den expliziten Skalar und den stetigen `r''`-Korrektor.

Die frühere Frage

```text
N_a <= G_a^+ ?
```

ist **kein nichtzirkulärer Objekt-X-Gate**: Sobald lokale Weil-Positivität bekannt ist, kann ein kontraktiver `W_a` rückwärts aus `Q=G_a^+-N_a` definiert werden. Das beweist keine intrinsische Geometrie.

**Buchung:** OX-GRAM als Existenzfrage ist geschlossen/vakuant. Übrig bleibt Kanonizität: ein Objekt-X-Baustein muss aus den vorhandenen Generatoren konstruiert werden, ohne `Q_{B_a}`, `B_a^{1/2}`, `lambda_a` oder RH rückwärts zu verwenden.

## 4. Gate 2: starke Evidenz, Repo-Zertifikat noch nicht eingefroren

Der externe 512-Bit-Lauf testete eine Dirichletbasis bis `N=14`, drei Radien und beide Paritätssektoren. Die ausgegebene Arb-Cholesky akzeptierte 42/42 endliche Blöcke; kein numerischer Gegenvektor wurde gefunden.

**Aber:** Die übergebene Implementierung ist noch nicht vollständig interval-geschlossen:

1. `r_1''` wird als Bernoulli-Partialsumme bis `N=340` integriert, ohne den Tail `n>340` in die Arb-Bälle einzuschließen;
2. der Prime-Power-Cutoff wird über `float(exp(2a))` entschieden;
3. ein Log-Endpunktfehler verwendet einen Float in einer sonst rigorosen oberen Schranke.

Der Bernoulli-Tail ist für `|u|<=2` extrem klein; er kann explizit beschränkt oder durch die geschlossene Formel

```math
r_1''(u)=\frac{e^{u/2}}{2\sinh u}-\frac1{2u},
\qquad r_1''(0)=\frac14
```

ersetzt werden. Bis zum gehärteten Rerun wird Gate 2 als **starke Arb-Evidenz, nicht als vollständiger Repo-Freeze** geführt.

## 5. Neue operative Hauptfront: OX-GEN

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

Gleichzeitig werden die Prime-Kanäle durch dieselbe Exponentialfamilie normiert:

```math
p^{-1/2}=e^{-(\log p)/2},
\qquad
R_p(j,k)=p^{-|j-k|/2},
\qquad
w_{p,k}=\log p\,p^{-k/2}.
```

### OX-GEN

**Frage:** Ist `R_0` als Rand-/Defektterm derselben Exponentialstruktur darstellbar, die die Prime-Power-Kanäle normiert? Gibt es eine explizit aus `{e^{+x/2}, e^{-x/2}, K_n, logarithmischer Formraum-/log|D|-Geometrie}` gebaute Abbildung, die insbesondere

```math
\left(\int\cosh\frac x2\,v\right)^2
```

im geraden Sektor als intrinsischen Defekt der Prime-/archimedischen Featuregeometrie erzeugt, ohne die zu erklärende Weilform rückwärts zu benutzen?

Positive Antwort: expliziter geometrischer Baustein. Negative Antwort: Klassen-No-Go, sofern die Generator-Klasse vorher natürlich und eng definiert wurde.

**Scope:** `R_1` und der dominante Skalar `c_aI` bleiben offen; OX-GEN ist ein Teilproblem.

## 6. Nächste Gates

In dieser Reihenfolge:

1. **CERT-HARDEN** — Gate 1/2 mit explizitem Bernoulli-Tail oder geschlossener `r_1''`-Form, reinem Arb-Randfehler und Arb-sicherem Prime-Power-Cutoff rerunnen.
2. **OX-GEN-A** — bei `a=0.5` die `cosh/sinh`-Momentfunktionale innerhalb der Prime-/logarithmischen Formraum-Featureabbildung isolieren. Dieser Radius wird bevorzugt, weil die endliche Extremalrichtung dort deutlich stabiler war als bei `a>=0.8`.
3. **GENERATOR-CLASS** — vor einem No-Go eine natürliche Klasse von Generatorabbildungen festschreiben; beide Ausgänge müssen vorab logisch möglich sein.
4. **OX-GEN-B** — expliziten Intertwiner oder Klassen-No-Go suchen.

Keine weiteren `mu_max`-Dimensionssweeps als Hauptfront: ohne neuen Mechanismus messen sie bekannte lokale Weil-Positivität.

## 7. Spur B — eigenständige Mathematik

Die Prime-Power-AR(1)/Martingal-Faktorisierung wird getrennt als theorem-ready Nebenprojekt geführt:

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}\,p^{-|j-k|/2},
\qquad
T_q^*T_q+uu^*=R_q.
```

Fensterfrei, exakt, RH-unabhängig und ausdrücklich **nicht** als Objekt X vermarkten. Der bisherige Literaturbefund ist nur Neuheitsindikator, kein Prioritätsbeweis.

## 8. Gesperrte alte Deutungen

Nicht wieder als aktive Front verwenden:

- Rang-1-PR91-Zeugenmatrix;
- `3/4` als bloße Beschränktheitsdämpfung;
- Vier-Boundary-Erklärung der Interior/Baseline-Differenz;
- cross-prime als Fensterrand;
- „Nichtunitarität = genau Hub“;
- Suzuki-Basispunkt-Vierterm als `2I`-Renormierung;
- matched-cutoff `epsilon=e^{-A_L}` als Mechanismus;
- OX-REN/OX-REN' als Hauptfront;
- Radiusvariation durch bloßes Ersetzen von `R=1` im PR97-Checker;
- neue speziell angepasste Witness-Runden ohne einen vorab definierten Architekturtest;
- weitere OX-GRAM-Existenztests, die nur bekannte Weil-Positivität reproduzieren;
- `H^{1/2}`-/klassische Douglas-Terminologie für den Kernel `1/|x-y|`;
- die Aussage, die Defektnorm `||I-W^*W||` kollabiere; kollabierend beobachtet wurde der kleinste relative Eigenwert, nicht die Operatornorm;
- die radius-/sektorabhängige Koeffizienten-Koinzidenz nahe `0.603` als Konstante zu deuten.

## 9. Offene PRs und Governance

PR #91 bleibt ein eigener analytischer Draft; diese Front promotet ihn nicht. PR #92 und PR #95 sind Archiv-/Integritäts-Governance und orthogonal zur OX-GEN-Forschung. Die gemergten PR #96/#97 bleiben lokale Negativresultate in ihrem damaligen Scope.

Zusätzliche PR-Schuld ist separat abzuarbeiten: insbesondere der ältere Ready-PR #49 sowie der weiterhin ungeprüfte Draft #91 dürfen durch die OX-GEN-Front nicht aus dem Blick geraten.

Registry, `ACTIVE_FRONT.yaml` und Arbeitsdefinition bleiben unverändert.

## 10. Arbeitsregel

Ein Schritt zählt auf der Objekt-X-Hauptfront nur, wenn er

1. einen expliziten Teil der gemeinsamen Gramgeometrie konstruiert,
2. eine ganze vorab definierte Architekturklasse ausschließt,
3. eine notwendige Struktur des gemeinsamen Prime-/Archimedean-Generators beweist oder
4. eine tatsächlich benötigte Normalisierungs-/Domain-/Konvergenzlücke schließt.

Ein Falsifikationsgate zählt nur, wenn **beide Ausgänge vorab logisch möglich** sind. Bloße Umschreibungen, Witness-Wertabgleiche oder Positivitätsreproduktionen ohne neuen Mechanismus sind Nebenarbeit.
