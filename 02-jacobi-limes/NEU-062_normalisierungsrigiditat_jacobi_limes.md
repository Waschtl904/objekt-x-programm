# NEU-62 — Normalisierungsrigidität des Jacobi-Limes

**Status:** Fallunterscheidung gesichert ✓[M]; Strukturentscheidung ❓[O]  
**Datum:** 2026-06-29  
**Aufbaut auf:** NEU-61 (Core-Konvergenz hängt an γ_∞ > 0)

---

## Zentralfrage

Die analytische Kette NEU-60 → NEU-61 → Weg B ist vollständig geschlossen **genau dann**,
wenn γ_N einen positiven Grenzwert besitzt. NEU-62 analysiert, ob und warum das gilt.

---

## Fallunterscheidung ✓[M]

| Fall | Konsequenz für Weg B |
|---|---|
| γ_N ≡ 1 (oder const > 0) | Lemma 61.1 gilt exakt (eventual equality der Koeffizienten); Weg B steht sofort ✓[M] |
| γ_N → γ_∞ ∈ (0, ∞) | Core-Konvergenz gilt (Satz NEU-61.1); Weg B steht mit Skalenfaktor γ_∞ ⚠[M] |
| γ_N → 0 | D_rel = 0 (Nulloperator); Core-Konvergenz trivial, aber spektral wertlos ❓[O] |
| γ_N oszilliert / divergiert | Core-Konvergenz kann scheitern ❓[O] |

**Entscheidend:**

- Fall 1 und 2 sichern Weg B.
- Fall 3 und 4 zerstören das Programm spektral.
- NEU-58 hat γ_N = C/log N als **unverträglich** mit uniformem Konfinement gezeigt;
  das schliesst Fall 3 nicht aus, sondern macht ihn nur spektral wertlos.

---

## Satz NEU-62.1 — Normalisierungsfreiheit ✓[M]

**Behauptung:** Wenn γ_N ein frei wählbarer Renormierungsparameter ist (nicht durch
externe Normierung der Jacobi-Modelle fixiert), dann kann man
```
γ_N ≡ 1
```
setzen. Dann gilt:
- Θ_{ba}^(N) = |r| log(n) (N-unabhängig für alle a, b)
- Lemma 61.1 gilt mit eventual equality
- Satz NEU-61.1 gilt
- Weg B ist geschlossen. ✓[M]

**Kompatibilität mit NEU-58:** NEU-58 zeigt, dass γ_N = 1 die uniforme
Nelson-Kommutator-Kontrolle (Schur-Test) zerstört (B_N ~ N log N divergiert).
Das ist konsistent: Weg A ist geschlossen (✗[M]), Weg B braucht diese Kontrolle nicht.

**Fazit:** γ_N ≡ 1 ist intern widerspruchsfrei für Weg B. ✓[M]

---

## Satz NEU-62.2 — Externe Normierung (strukturelle Frage) ❓[O]

Wenn γ_N aus einer externen Normierung der endlichen Jacobi-Matrizen A_N^{Jac,-}
stammt (z.B. aus spektraler Normierung, Tr-Normierung, oder Wachstumskontrolle
der Eigenwerte), dann ist zu zeigen:
```
lim_{N→∞} γ_N = γ_∞ > 0.
```

Mögliche Quellen für γ_N-Konvergenz:

**Quelle A: Spektrale Normierung**
```
γ_N := 1 / λ_{max}(A_N)    (λ_{max} = größter Eigenwert)
```
Wenn λ_{max}(A_N) ~ C (beschränkt), dann γ_N ~ 1/C > 0. ⚠[M]
Wenn λ_{max}(A_N) → ∞, dann γ_N → 0 (Fall 3). ❓[O]

**Quelle B: Tr-Normierung**
```
γ_N := C / Tr(A_N^{Jac,-})^{1/2}
```
Hängt vom Wachstum der Spur ab; aus der Matrixstruktur berechenbar. ❓[O]

**Quelle C: Intrinsische Definition ohne Normierung**
Wenn J^- und H_rel durch arithmetische Struktur absolut definiert sind
(ohne N-abhängige Renormierung), dann ist γ_N = 1 strukturell erzwungen. ✓[M]

---

## Entscheidungsprinzip für NEU-63+

Die Entscheidung zwischen den Fällen hängt an einer einzigen Frage:

```
Ist γ_N ein interner (frei wählbarer) Parameter von J^-,
oder kommt er aus einer externen Normierung der Jacobi-Trunkierungen?
```

Drei Szenarien:

**Szenario I: γ_N intrinsisch = 1**
```
J_N^- = (1/2i)(Θ_N - Θ_N^{Wres}),  Θ_N(e_r V_n) = -r log(n) e_{r+n} V_n
(ohne zusätzlichen γ_N-Faktor in der Grunddefinition)
```
Dann ist γ_N = 1, Weg B steht. ✓[M]

**Szenario II: γ_N aus Schur-Kontrolle gewählt**
```
γ_N = C / log N  (aus Nelson/Schur-Anforderungen)
```
Dann γ_N → 0, D_rel = 0, Weg B spektral wertlos. ❓[O]
Aber: NEU-58 hat gezeigt, dass diese Wahl Konfinement sowieso nicht sichert.
Keine Motivation, γ_N = C/log N für Weg B zu verwenden.

**Szenario III: γ_N aus Jacobi-Limes-Normierung**
Externe Bedingung; muss gesondert analysiert werden. ❓[O]

---

## Empfehlung

Für den weiteren Programmaufbau:

1. **Setze γ_N ≡ 1** als strukturelle Normalisierung (keine externe Renormierung).
2. Dann ist Satz NEU-61.1 mit eventual equality gültig. ✓[M]
3. Weg B ist analytisch vollständig (NEU-58 → NEU-59 → NEU-60 → NEU-61 → NEU-62).
4. Der einzige verbleibende offene Schritt ist die **arithmetische Identifikation**
   Spec(D_rel) ↔ Nullstellen ζ.  ❓[O] → NEU-63

---

## Aktualisierter kritischer Pfad

```
[NEU-58]  B_N/A_N → ∞: Weg A ausgeschlossen         ✗[M]
           ↓
[NEU-62]  γ_N ≡ 1 (strukturell): Normalisierung gewählt  ✓[M]*
           ↓
[NEU-61]  A_N η_a → D_rel η_a (eventual equality)     ✓[M]*
           ↓
[NEU-60.1] Starke Resolventenkonvergenz                ✓[M]*
           ↓
[NEU-59.1] μ_{N,ξ,η} ⇒ μ_{ξ,η}                         ⚠[M]
           ↓
[NEU-59]   supp(μ_ξ) ⊂ Spec(D_rel) ⊂ ℝ               ✓[M]
           ↓
[NEU-63]   Arithmetische Identifikation                ❓[O]  ← Hauptproblem
           ↓
           RH

* unter γ_N ≡ 1
```

Mit der Normalisierungsentscheidung γ_N ≡ 1 ist die analytische Kette
**vollständig geschlossen bis auf die arithmetische Identifikation**.

---

## Status NEU-62

| Objekt | Status |
|---|---|
| Fallunterscheidung (γ_N-Szenarien) | ✓[M] |
| γ_N ≡ 1: Weg B sofort | ✓[M] |
| γ_N → γ_∞ > 0: Weg B mit Skalierung | ⚠[M] |
| γ_N → 0: spektral wertlos | ❓[O] |
| Externe Normierungsquelle | ❓[O] |
| Analytische Kette (unter γ_N = 1) geschlossen | ✓[M] |

---

## Literatur

- Reed, M. & Simon, B.: Bd. II, §X.6 (Jacobi-Operatoren)
- Akhiezer, N.I.: *The Classical Moment Problem*, Oliver & Boyd 1965
  (Normierungsfragen bei Jacobi-Matrizen)
- Simon, B.: *Szegő's Theorem*, AMS 2011, Kap. 2 (Weyl-Funktionen und Normierung)
