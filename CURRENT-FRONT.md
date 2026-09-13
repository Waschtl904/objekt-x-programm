# CURRENT FRONT — Objekt X / OX-GEN

> **Operative Kopfschicht — zuerst lesen.**
> **Redaktioneller Stand:** 13. September 2026; keine Registry-Promotion.
> **Konsolidierungsquellen:** [AR(1)/Weil-Tail/OX-GRAM](audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md), [Gate-2/OX-GEN](audits/P11_OX_GRAM_GATE2_AND_OX_GEN_2026-09-12.md), [OX-GEN-A gemeinsamer Exponentialgenerator](audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md).
> **Strategie:** [kanonische Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md).
> **Suchgegenstand:** [Objekt-X-Arbeitsdefinition](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md).
> **Buchungen:** [Theorem-/Review-Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).

Diese Datei ordnet die Arbeit; sie beweist nichts. Der aktuelle `main`-Head und PR-Zustände werden live aus GitHub gelesen. Bei Konflikten ist die kanonische mathematische Quelle im benannten Scope maßgeblich.

## 1. Erreichter Meilenstein

Der integrierte positive Wurzelanker plus R42.51 liefert Strong Terminal/C6 für jedes **feste** `0<R<S` im **ungeraden P11-Graphraum**.

**Scope:** keine Radienuniformität, keine Operatornormkonvergenz, kein gerader Gesamtsektor, keine vollständige Objekt-X-Realisierung und keine RH-Folgerung.

## 2. Belastbare Prime-Power-Struktur

Seit PR #98 ist dokumentiert:

```math
C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4},
\qquad
C_{kk}^{(p)}=(\log p)p^{-k/2}.
```

`3/4` ist durch Weil-Diagonale plus Martingalmultiplizität erzwungen. Nach Weil-Diagonalnormalisierung:

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}\,p^{-|j-k|/2},
\qquad q_p=p^{-1/2}.
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

**Spur B:** theorem-ready, RH-unabhängig, ausdrücklich noch nicht Objekt X.

## 3. Endliche Suzuki-/OX-GRAM-Normalform

Für `a<=1`:

```math
Q_{B_a}(v)=G_a^+(v)-N_a(v),
\qquad
N_a=c_aI+C_a.
```

`G_a^+` besteht aus positiven Prime-Kanal-, Log-Multiplikator- und logarithmischen `log|D|`-Formen. Die reine Existenzfrage `N_a<=G_a^+?` ist als Objekt-X-Gate geschlossen: bei bereits bekannter lokaler Weil-Positivität kann ein Kontraktor rückwärts aus `Q` gebaut werden. Das ist zirkulär.

**Übrig bleibt Kanonizität.**

## 4. CERT-HARDEN — geschlossen im dokumentierten endlichen Scope

PR #98 enthält gehärtete read-only Zertifikatswege.

- Gate 1: Realraum/Fourier-Normalisierung bei `a in {0.5,0.8,1.0}`, mit Bernoulli-Tailball, Arb-Cutoff, Arb-Endpunktfehler, `sinc`-Rest und fail-closed Null-Einschluss.
- Gate 2: Arb 512 Bit, Dirichletbasis bis `N=14`, drei Radien, beide Paritäten, **42/42** strikt positive Arb-Cholesky-Blöcke.

**Firewall:** endlichdimensionales Zertifikat, kein globaler Weil-Positivitäts- oder RH-Beweis.

## 5. OX-GEN-A — gemeinsamer Exponentialgenerator geschlossen `✓[M]`

Für kompakt getragene Testfunktionen setze

```math
E_\pm(v)=\int e^{\pm x/2}v(x)\,dx,
\qquad
\mathcal Ev=(E_+(v),E_-(v)).
```

Für Translationen `(T_t v)(x)=v(x+t)` gilt exakt

```math
\boxed{\mathcal ET_t=\rho(t)\mathcal E,\qquad
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2}).}
```

Mit

```math
K_n=T_{\frac12\log n}-T_{-\frac12\log n},
\qquad
\lambda_n=n^{1/4}-n^{-1/4}
```

folgt

```math
\boxed{\mathcal EK_n
=\lambda_n\operatorname{diag}(-1,1)\mathcal E,}
```

also

```math
E_\pm(K_nv)=\mp\lambda_nE_\pm(v)
```

**ohne Fensterrandterm**. Die Funktionen `e^{\pm x/2}` müssen selbst nicht im Fensterraum liegen.

Suzukis elementarer Anteil erfüllt zugleich

```math
\boxed{r_0''(t)=-\operatorname{tr}\rho(t)=-2\cosh(t/2),}
```

sogar

```math
\boxed{r_0(t)=-4\bigl(\operatorname{tr}\rho(t)-2\bigr),
\qquad r_0(\log n)=-4\lambda_n^2.}
```

Damit sind Prime-Kanäle und archimedischer `r_0`-Term **zwei exakte Funktoren derselben zweidimensionalen Translationrepräsentation**.

### Rang-2-Form / Spiegelung

Mit Austauschoperator

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}
```

gilt polarisiert

```math
\boxed{R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle_{\mathbb C^2}.}
```

Für reelle `v`:

```math
R_0(v,v)=-2E_+(v)E_-(v).
```

Die Spiegelung `v(x)->v(-x)` induziert genau `P`; damit folgt die bekannte Paritätssignatur intrinsisch.

Unter jedem Kanal:

```math
\boxed{R_0(K_nv,K_nw)=-\lambda_n^2R_0(v,w).}
```

Das ist Anti-Kovarianz einer indefiniten Rang-2-Form, **keine** positive Kontraktionsidentität.

## 6. Prime-only-A2 aus `{w_n,lambda_n}` geschlossen `×[M]`

Der zunächst vorgeschlagene Test „Prime-Gram direkt auf dem Rang-2-Quotienten“ ist nicht wohldefiniert:

- `ker \mathcal E` ist zwar unter jedem `K_n` invariant;
- die positive Form `\sum w_n||K_n v||^2` verschwindet dort aber nicht;
- sie descendiert daher ohne zusätzliche Quotientennorm/Schur-Komplement/Komplementwahl nicht auf `v -> (E_+,E_-)`.

Auch die reine Quotienten-Kovarianz fixiert den Maßstab nicht. Für eine Hermiteform `H` mit

```math
D_n^*HD_n=-\lambda_n^2H,
\qquad D_n=\lambda_n\operatorname{diag}(-1,1),
```

folgt lediglich

```math
H=\begin{pmatrix}0&b\\\bar b&0\end{pmatrix};
```

der Skalar `b` bleibt frei. Die Gewichte `w_n` ändern daran nichts.

**Enges No-Go:** Der absolute Koeffizient `2` in `R_0=-2E_+E_-` kann nicht allein aus den diskreten Daten `{w_n,lambda_n}` plus Anti-Kovarianz bestimmt werden.

Mit der vollen Translation-/Spiegelstruktur ist die Normierung dagegen kanonisch: `R_0=\mathcal E^*(-P)\mathcal E`.

## 7. Neue operative Hauptfrage: OX-GEN-A2' / POSITIVE-DILATION

Gesucht ist jetzt nicht mehr irgendeine Rang-2-Form, sondern:

> **Kann die kanonische Translation-/Reflexions-Geometrie `(C^2,rho,P,E)` intrinsisch in die positive Prime-/`log|D|`-Featuregeometrie eingebettet oder als Schur-/Defektterm einer positiven Erweiterung realisiert werden — ohne `Q_{B_a}`, RH oder eine rückwärts definierte Positivitätswurzel?**

Positive Antwort: erster expliziter gemeinsamer Prime-/Archimedean-Baustein mit positiver Umgebung.

Negative Antwort: nur dann Klassen-No-Go, wenn die natürliche Dilatations-/Intertwinerklasse vorher festgeschrieben ist.

**Scope:** `r_1` und `c_aI` bleiben offen. Die Rang-2-Geometrie allein ist noch kein Objekt X.

## 8. Nächste Gates

1. **GENERATOR-CLASS / POSITIVE-DILATION-CLASS** — natürliche positive Erweiterungs-/Intertwinerklasse definieren.
2. **OX-GEN-A2'** — explizite positive Dilatation/Schur-Realisierung oder Klassen-No-Go.
3. **OX-GEN-B** — erst danach `r_1` und/oder den dominanten Skalar `c_aI` in dieselbe gemeinsame Geometrie einbeziehen.
4. **Spur B parallel:** AR(1)/Martingal-Faktorisierung theorem-ready verschriftlichen.

## 9. Gesperrte Deutungen

Nicht wieder aktivieren:

- Rang-1-PR91-Zeugenmatrix;
- Vier-Boundary-Erklärung;
- cross-prime als Fensterrand;
- „Nichtunitarität = genau Hub“;
- matched-cutoff als Mechanismus;
- OX-REN/OX-REN' als Hauptfront;
- `H^{1/2}`-/klassische Douglas-Terminologie für `1/|x-y|`;
- Kollaps von `||I-W^*W||`;
- `0.603` als Konstante;
- Prime-only-Rang-2-Gram ohne zusätzliche Quotientenstruktur;
- Behauptung, die Generator-Ebene erkläre bereits `c_aI`.

## 10. Governance

- PR #91 bleibt analytischer Draft ohne übertragenes unabhängiges Exact-Head-GREEN.
- PR #49 ist formal Ready, inhaltlich aber weiterhin `candidate only; no merge requested yet`.
- Registry, `ACTIVE_FRONT.yaml` und Arbeitsdefinition werden durch diese Front nicht automatisch geändert.
- Kein Object-X- oder RH-Abschluss.
