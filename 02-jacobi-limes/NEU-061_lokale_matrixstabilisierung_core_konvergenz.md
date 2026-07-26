# NEU-61 — Lokale Matrixstabilisierung und Core-Konvergenz

**Status:** Lemma 61.2 gesichert ✓[M]; Satz 61.1 gesichert unter γ_N → γ_∞ > 0 ⚠[M]  
**Datum:** 2026-06-29 (korrigiert: eventual equality → Konvergenz; Einbettungspräzisierung)  
**Aufbaut auf:** NEU-60 (Core-Konvergenz-Kriterium), NEU-58 (Weg A geschlossen)

---

## Struktureller Gewinn gegenüber NEU-58

```
NEU-58 scheitert an:  sup_{m ≤ N} Σ_{n|m} n log n ~ N log N  (uniform, divergent)

NEU-61 braucht nur:   Σ_{n|m} n log n  für FESTES m  (endliche Divisorenmenge!)
```

Für festes m ist {n : n | m} endlich (genau d(m) Elemente). Das ist die lokale
Endlichkeit, die Weg B rettet: NEU-58 scheitert uniform in m ≤ N, NEU-61
funktioniert punktweise auf dem Core.

---

## Zielsetzung

Für jeden festen Basisvektor η_a mit a = (p, m, r, u) zeige:
```
A_N^{Jac,-} η_a  →  D_rel η_a    in H-Norm  (N → ∞).
```

Diese Konvergenz zerfällt:
```
‖A_N η_a - D_rel η_a‖²
  = Σ_{b ∈ I_N}  |Θ_{ba}^(N) - Θ_{ba}^(∞)|²    [Koeffizienten-Stabilisierung]
  + Σ_{b ∉ I_N}  |Θ_{ba}^(∞)|²              [Tail-Kontrolle: Lemma 61.2]
  → 0.
```

---

## Lemma 61.2 — Tail-Kontrolle ✓[M]

**Behauptung:** Für festes a = (p, m, r, u) und N > N_0(a):
```
Σ_{b ∉ I_N} |Θ_{ba}^(∞)|² = 0.
```

**Beweis:** Da m fest ist, ist {n : n | m} endlich. Für alle hinreichend großen N
sind alle Zielindizes b = (p', m, r+n, u') mit n | m in I_N enthalten.
Der Tail ist **eventual exakt Null**. ✓[M]

**Präzisierung:** Support-Stabilisierung ist eventual exakt; das ist
ein strukturelles Ergebnis, kein asymptotisches.

---

## Lemma 61.1 — Koeffizienten-Stabilisierung ⚠[M]

**Behauptung:** Für festes a = (p, m, r, u) und γ_N → γ_∞ ∈ (0, ∞):
```
Σ_{b ∈ I_N} |Θ_{ba}^(N) - Θ_{ba}^(∞)|²  →  0    (N → ∞).
```

**Wichtige Präzisierung (gegenüber früherer Version):**

Aus γ_N → γ_∞ > 0 folgt im Allgemeinen **nicht** eventual equality
Θ_{ba}^(N) = Θ_{ba}^(∞) für große N, sondern nur Konvergenz:
```
Θ_{ba}^(N) = γ_N · |r| · log(n)  →  γ_∞ · |r| · log(n) = Θ_{ba}^(∞).
```

Eventual equality gilt nur bei exakt konstanten γ_N ≡ γ.

**Explizite Normabschätzung:**
```
‖A_N η_a - D_rel η_a‖²
  = |γ_N - γ_∞|² · r² · Σ_{n|m} log²(n)  →  0,
```
weil:
(1) |γ_N - γ_∞|² → 0 (Voraussetzung),
(2) r² · Σ_{n|m} log²(n) < ∞ für festes a (endliche Divisorenmenge). ✓[M]

**Zusammenfassung:**
```
Support-Stabilisierung:    eventual exakt Null     ✓[M]
Koeffizienten-Stabilisierung:  nur konvergent      ⚠[M]
```
Beides zusammen reicht vollständig für NEU-60.1. ⚠[M]

---

## Satz NEU-61.1 — Core-Konvergenz auf Basisvektoren ⚠[M]

**Voraussetzung:** γ_N → γ_∞ ∈ (0, ∞).

**Behauptung:**
```
A_N^{Jac,-} η_a  →  D_rel η_a    für jeden Basisvektor η_a ∈ D_test.
```

**Beweis:** Aus Lemma 61.2 (Tail = 0 für N > N_0(a)) und Lemma 61.1
(Koeffizienten γ_N → γ_∞, endlich viele Terme):
```
‖A_N η_a - D_rel η_a‖² = |γ_N - γ_∞|² · r² · Σ_{n|m} log²(n) + 0  →  0. □
```

**Korollar (via NEU-60.1):** Starke Resolventenkonvergenz:
```
(A_N - z)^{-1} ξ  →  (D_rel - z)^{-1} ξ    für alle ξ ∈ H, z ∈ ℂ\ℝ.
```
⚠[M]

---

## Technische Warnung: Einbettung von A_N in H

**(GPT-Korrektur übernommen)**

Die Aussage über Norm-Resolventenkonvergenz hängt **entscheidend** von der
Einbettungsstrategie ab:

**Fall 1: A_N lebt nur auf H_N** (natürlicher Fall)
Dann ist Norm-Resolventenkonvergenz A_N → D_rel nicht direkt definiert
(verschiedene Hilberträume). Der robuste Weg ist starke Resolventenkonvergenz
über Core-Konvergenz. ✓[M]

**Fall 2: A_N als P_N A_N P_N + 0 auf H_N^perp eingebettet**
Dann gilt:
```
(A_N - z)^{-1} = (A_N|_{H_N} - z)^{-1} P_N + (-z)^{-1} (I - P_N)
```
Diese Resolvente ist **nicht** endlich-rangig und **nicht** kompakt
(wegen des (-z)^{-1}(I-P_N)-Terms). Der Kompaktheitswiderspruch aus NEU-59
gilt nur für die finite-rank Einbettung ohne (-z)^{-1}-Korrektur.

**Konsequenz für NEU-59:**
Der Ausschluss der Norm-Resolventenkonvergenz in NEU-59 bleibt gültig,
aber nur für die reine P_N A_N P_N-Einbettung ohne Korrekturterm. Die
sichere Formulierung lautet:
```
Norm-Resolventenkonvergenz ist nicht der natürliche Weg;
der robuste Weg ist starke Resolventenkonvergenz über Core-Konvergenz.
```
✓[M]

---

## Status NEU-61

| Objekt | Status |
|---|---|
| Tail-Kontrolle (Lemma 61.2) | ✓[M] |
| Koeffizienten-Konvergenz (γ_N → γ_∞ > 0) | ⚠[M] |
| Satz NEU-61.1 (Core-Konvergenz) | ⚠[M] |
| Starke Resolventenkonvergenz (via NEU-60.1) | ⚠[M] |
| Einbettungswarnung (Kompaktheit) | ✓[M] |
| γ_∞ > 0 (Voraussetzung) | ❓[O] → NEU-62 |

---

## Literatur

- Kato, T.: *Perturbation Theory for Linear Operators*, Springer 1995, §VIII.1
- Reed, M. & Simon, B.: Bd. I, Thm. VIII.25; Bd. II, §X.6
- Akhiezer, N.I. & Glazman, I.M.: *Theory of Linear Operators in Hilbert Space*, Kap. 7
