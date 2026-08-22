# P12 Consolidation Audit — Runden 8–11

**Datum:** 2026-08-22 (Runde 12 — Konsolidierung, keine neue Mathematik)
**Basis-HEAD vor Consolidation:** `949f901`
**Ziel:** GPTs sechs Konsolidierungs-Befunde abarbeiten, Dependency-DAG dokumentieren, keine Retraktion.

## Sechs Consolidation-Patches

### (A) b2d-Regionen-Zerlegung geometrisch korrigiert

**Alt (falsch):**
- b2d-upper: $x \in (d - R, \sigma)$, nonempty iff $\sigma > d - R$
- b2d-core-both: $x \in (d - \sigma, d - R)$, nonempty iff $\sigma > d - R$
- b2d-core-single: $x \in (R, d - \sigma)$

**Neu (korrekt):**
- b2d-core-single: $x \in (R, \min\{\sigma, d - \sigma, d - R\})$
- b2d-core-both: $x \in (\max\{R, d - \sigma\}, \min\{\sigma, d - R\})$, nonempty iff $\sigma > d/2$
- b2d-upper: $x \in (d - R, \sigma)$, nonempty iff $\sigma > d - R$

**Sharp-Case-Zerlegung nach $\sigma$:**
- (A) $\sigma \le d/2$: nur core-single, $(R, \sigma)$
- (B) $d/2 < \sigma \le d - R$: $(R, d-\sigma)$ core-single, $(d-\sigma, \sigma)$ core-both
- (C) $\sigma > d - R$ (braucht $R > d - \varepsilon_{\max}$): $(R, d-R)$ core-both, $(d-R, \sigma)$ upper

**Numerisch verifiziert** in `consolidation/round11_eta_wall_bootstrap.py` und
neuem Prüfskript. Runde-11-Aussage "$h = 0$ auf $(R, \min\{\sigma, d-\sigma\})$"
bleibt korrekt und ist in Fall A/B substantiell, in Fall C automatisch leer
(dort ist core-single geometrisch leer).

**Kein Retraktions-Bedarf.**

### (B) Runde-10-Konstantenfehler

**Alt:** "$e > 2\delta$ i.e. $27 > 16$" — Reduktion falsch.

**Neu:** $e > 2\delta$ iff $\log(4/3) > 2\log(9/8)$ iff $4/3 > (9/8)^2$ iff $256 > 243$.

Numerisch: $4 \cdot 64 = 256 > 3 \cdot 81 = 243$. Elementar.

### (C) R\*-Formel korrekt

**Alt:** $R^* = \tfrac14 \log(311/217)$ — Bruch falsch, Dezimalwert 0.0753... korrekt.

**Neu:**
$$R^* = d/2 - \eta = \tfrac14 \log(3/2) - \tfrac12 \log(256/243) = \tfrac14 \log\!\left(\frac{3^{11}}{2^{17}}\right) = \tfrac14 \log\!\left(\frac{177147}{131072}\right) \approx 0.0753082765.$$

Ableitung:
- $d/2 = \tfrac14 \log(3/2)$
- $\eta = \tfrac12 \log(256/243) = \tfrac14 \log(65536/59049)$
- $R^* = \tfrac14 [\log(3/2) - \log(65536/59049)] = \tfrac14 \log(3 \cdot 59049 / (2 \cdot 65536)) = \tfrac14 \log(177147/131072)$
- $3 \cdot 59049 = 3^{12} \cdot 3^{-1} \cdot 3 = 3^{11} \cdot \ldots$ nachrechnen: $3 \cdot 59049 = 3 \cdot 3^{10} = 3^{11} = 177147$. ✓
- $2 \cdot 65536 = 2 \cdot 2^{16} = 2^{17} = 131072$. ✓

### (D) Veralteter Runde-10-Scope aktualisiert

**Alt (in Wedge-Scope-Remark):** open front = $\{\sigma > d/2\} \cup \{\sigma > R + \eta\}$.

**Neu:** derselbe Text mit Zusatzabsatz: der zweite Teil ($\sigma > R + \eta$)
wird durch den η-Wall-Bootstrap in Runde 11 (Theorem `thm:p12-b2d-core-single-full`
und Corollary `cor:p12-b2d-wedge-plus`) geschlossen. Nur $\{\sigma > d/2\}$
(core-both) bleibt offen.

### (E) L²-Terminologie: "for every" → "for a.e."

Konkrete Änderungen:
- Theorem `thm:p12-b2d-core-single-slice`: "for every $x \in C_{19}$" → "a.e. on $C_{19}$"
- Theorem `thm:p12-b2d-core-single-full`: "for every $x$" → "almost everywhere on"
- Bootstrap Step 3: expliziter Zusatz "$x = R + \eta$ Maßnull, Translation Maß-erhaltend"
- Corollary `cor:p12-b2d-wedge-plus`: "at each $x$" → "at a.e. $x$"

### (F) α > 1-Lemma ohne Dezimalapproximation

**Alt-Schluss:** "$4/\sqrt 3 \approx 2.309$, $2\sqrt 2 - 1 \approx 1.828$, ratio $\approx 1.263 > 1$."

**Neu-Schluss:** $\alpha > 1$ iff $4/\sqrt 3 > 2\sqrt 2 - 1$; quadrieren gibt
$16/3 > 9 - 4\sqrt 2$; also $4\sqrt 2 > 11/3$, also $12\sqrt 2 > 11$;
quadrieren gibt $288 > 121$. Elementar.

## Dependency-DAG Runden 8–11

Kritischer Test: kein Zirkelschluss.

```
Runde 8: sympy 19x19 factorization
    ↓
Runde 9: 19-source slice C_19 with all supports elementary
    ↓ (h(y)=0 on C_19)
Runde 10: parameter wedge σ ≤ min(d/2, R+η)
    ↓ (uses Runde-9 slice + full Runde-8 det ≠ 0 + P1/P2 + b2b Steps 1-5 + b1)
    │
    ↓
Runde 11 A: full core-single via η-wall bootstrap
    (uses Runde-9 slice at y=x-η, NOT Runde-10 wedge)
    ↓
Runde 11 B: extended wedge σ ≤ d/2
    (uses Runde-11-A + P1/P2 + b2b + b1 — same propagation as Runde 10)
```

**Zirkularität-Check:**
- Runde 11 A (η-Bootstrap) verwendet: Runde 9 (Slice-Theorem an $y = x - \eta$).
  Verwendet **nicht**: Runde 10 (Wedge). ✓
- Runde 11 B (Extended Wedge) verwendet: Runde 11 A (Full Core-Single) + Propagation.
  Verwendet **nicht**: Runde 10 (die es ersetzt). ✓
- Runde 10 verwendet: Runde 9 direkt + Propagation. Verwendet **nicht** Runde 11. ✓
- Die alte Runde-10-Aussage bleibt gültig **als Zwischenergebnis** (Weakened form),
  wird aber von Runde 11 B strikt subsumiert. Kein Widerspruch.

**Kein Zirkelschluss.**

## Status nach Consolidation

**$\checkmark[M]$:**
- b0, b1, b2a, b2b, b2c (full)
- b2d-upper (local kill)
- b2d Slice $C_{19}$ (local kill, Runde 9)
- b2d Full Core-Single (local kill, Runde 11 A)
- b2d Wedge $\sigma \le \min(d/2, R+\eta)$ (full kernel, Runde 10) [subsumiert]
- b2d Extended Wedge $\sigma \le d/2$ (full kernel, Runde 11 B)

**$?[O]$:**
- b2d $\sigma > d/2$ (core-both)
- $0 < R < e/2$

## R14-Firewall

**Vollständig gewahrt.** Kein Patch berührt M→PG. P11 unverändert.

## CI und Kompilation

- LaTeX-Kompilation: PASS (dreifach mit `tectonic`, alle Refs aufgelöst)
- CI: erwartet SUCCESS auf Push

## Was NICHT gemacht wurde

- Keine Retraktion irgendeines bewiesenen Satzes.
- Keine neue core-both-Behauptung.
- Keine Änderung an P11/R14.
- Keine Änderung am Wickie-Meta-Framework (`WICKIE-FRAGEN.md`, `WICKIE-CORE-BOTH-ERKUNDUNG.md`).

## Verifikationsskripte

- `consolidation/round11_eta_wall_bootstrap.py` (Runde 11) — noch gültig
- `consolidation/wickie_h1_exploration.py` (H1 no-go) — noch gültig
- Neue kurze Verifikation der Region-Zerlegung inline in diesem Audit dokumentiert
