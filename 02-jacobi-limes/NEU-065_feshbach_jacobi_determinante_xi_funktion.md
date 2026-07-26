# NEU-65 — Feshbach-/Jacobi-Determinante und endliche ξ_N-Funktion

**Status:** Strukturrahmen ⚠[M]; Spurklassifikation ⚠[M]; Hypothese Z_N→ξ ❓[O]  
**Datum:** 2026-06-29 (korrigiert: Spur = geschlossene Pfade; kein direkter Λ-Vergleich; Feshbach-Fokus)  
**Aufbaut auf:** NEU-64 (Log-Derivat-Hypothese), NEU-63 (Zwei-Seiten-Strategie)

---

## Zentralfrage

```
det_rel(A_N^{Jac,-} - z)  =?  endliches arithmetisches Z_N(1/2+iz)
```

sodass im Limes N -> ∞:

```
Z_N(s) -> ξ(s),    m_{Ω,N}(z) = -∂_z log Z_N(z) -> -iξ'/ξ(1/2+iz).
```

**Warnung:** NEU-65.H ist extrem stark — näher am Endproblem als an einer technischen Hilfshypothese (Abschnitt unten). ⚠[M]

---

## Korrektur 1: Spur = geschlossene Pfade, nicht Λ-Summen ⚠[M]

Für einen endlichen Operator gilt:

```
Tr(A_N^k) = Σ_{geschlossene Pfade a_0->a_1->...->a_k=a_0}  Θ_{a_1,a_0} Θ_{a_2,a_1} ... Θ_{a_0,a_{k-1}}
```

Das ist eine **Weg-Summe im Divisorgraphen**, nicht eine offene Divisorsumme.

Konsequenzen:

- Tr(A_N) = 0, falls keine Diagonalterme vorhanden sind (A_N rein off-diagonal). ✓[M]
- Tr(A_N^2) = Σ_{a,b} |Θ_{ba}|^2 = Σ_{a,n|m(a)} r^2 log^2(n)  (Hin-und-zurück-Kanten) ⚠[M]
- Tr(A_N^3) = Dreieckszyklus-Summen; falls Divisorgraph bipartit/graduiert:
  Tr(A_N^{2j+1}) = 0  (keine ungeraden Zyklen). ⚠[M]

**Korrekte Interpretation von Tr(A_N^2):** ⚠[M]

```
Tr(A_N^2) = Σ_{a=(p,m,r,u), n|m} r^2 log^2(n)
           = (Divisor-Energie, quadratisch in r und log n)
           ≠ Σ_{n≤N} Λ(n)     [Λ-Summe ist linear!]
           ~ Σ_{n≤N} Λ(n)^2  [quadratisch -- passender, aber immer noch verschieden]
```

Der Vergleich mit Σ_n Λ(n) ist daher **nicht der erste passende Test**.
Passender: gewichtete Divisorsumme Σ_a Σ_{n|m(a)} w(a,n) log^2(n). ⚠[M]

---

## Korrektur 2: Log-Det-Entwicklung über geschlossene Pfade ⚠[M]

Die formale Entwicklung für großes |z|:

```
log Z_N(z) = log det(A_N - z) = -Σ_{k≥1} (1/k) Tr(A_N^k) / z^k + N log(-z)
```

liefert die Log-Det als erzeugende Funktion der **Spurkoeffizienten**
(= geschlossene Pfadsummen). Der arithmetische Inhalt liegt in:

```
Tr(A_N^k)  <--->  Primorbit-/Mangoldt-Koeffizienten?
```

Das ist **nicht automatisch** der Fall. Erst wenn die geschlossenen Pfade
die richtige Primzahl-/Mangoldt-Struktur tragen (NEU-66), wird der
Determinantenlimes Z_N -> ξ realistisch.

---

## Korrektur 3: Feshbach-Determinante als natürlicher Fokus ⚠[M]

Die volle Determinante det(A_N - z) enthält alle Eigenräume, auch
spektral irrelevante Nebenkomponenten. Der natürlichere Zugang ist
ein **Feshbach-Determinant relativ zum arithmetischen Testsektor P**:

```
Z_N^{Fesh}(z) := det( P(A_N-z)P - P A_N Q (QA_NQ-z)^{-1} Q A_N P )
```

wobei P die Projektion auf den arithmetisch relevanten Unterraum und
Q = I - P. Vorteile:

- Reduziert auf den spektralen Sektor, der m_Ω kontrolliert
- Unterdrückt irrelevante Nebenblöcke
- Natürliche Verbindung zur Weyl-Funktion: m_{Ω,N}(z) = -∂_z log Z_N^{Fesh}(z)

Status: ⚠[M] (strukturell klar, arithmetischer Inhalt offen)

---

## Hypothese NEU-65.H (Hauptbrücke) ❓[O]

**Hypothese:** Es existiert ein Feshbach-Testsektor P und eine Normierung, sodass

```
Z_N^{Fesh}(s) = det( Feshbach von A_N^{Jac,-} bei s=1/2+iz )  ->  C · ξ(s)
```

**Warum diese Hypothese extrem stark ist:**

Wenn Z_N(1/2+iz) aus einem endlichen selbstadjungierten Jacobi-Operator
kommt, hat Z_N in der z-Variablen **nur reelle Nullstellen** (Eigenwerte
von A_N^{Jac,-} sind reell). Falls lokal uniforme Konvergenz

```
Z_N(1/2+iz) -> C ξ(1/2+iz)
```

gilt, erzwingt **Hurwitz** (Grenzwert holomorpher Funktionen mit reellen
Nullstellen hat nur reelle Nullstellen) fast unmittelbar:

```
ξ(1/2+iz) hat nur reelle Nullstellen  <=>  alle γ_ρ ∈ ℝ  <=>  RH.
```

**Fazit:** NEU-65.H ist **äquivalent-nahe am Endproblem**, nicht nur eine
technische Hilfshypothese. Sie sollte als **Hauptbrücke** markiert werden. ❓[O]

---

## Testfolge (revidiert)

### Test 65.1 — Spurklassifikation (-> NEU-66)

Bestimme Tr(A_N), Tr(A_N^2), Tr(A_N^3) als geschlossene-Weg-Summen
(nicht nur numerisch). Klassifiziere die Divisorgraph-Zyklen. ⚠[M]

### Test 65.2 — Log-Det-Expansion

```
log Z_N(z) = -Σ_{k≥1} Tr(A_N^k) / (k z^k)  ->  Vergleich mit log ξ'/ξ
```

Prüfe: Tr(A_N^k) <-> Primorbit-/Mangoldt-Koeffizienten? ❓[O]

### Test 65.3 — Feshbach-Determinante

Berechne Z_N^{Fesh}(s) für kleine N (I_N mit m ≤ 4) explizit.
Vergleiche Nullstellen mit γ_1 ≈ 14.13, γ_2 ≈ 21.02. ❓[O]

---

## Status NEU-65

| Objekt | Status |
|---|---|
| Log-Det = Tr-Entwicklung (abstrakt) | ✓[M] |
| Tr(A_N) = 0 (off-diagonal) | ✓[M] |
| Tr(A_N^2) als Divisor-Energie (quadratisch) | ⚠[M] |
| Tr(A_N^2) ≠ ΣΛ(n) direkt | ✓[M] (Warnung) |
| Implikation NEU-65.H + Hurwitz => RH | ⚠[M] |
| Feshbach-Determinante als nat. Fokus | ⚠[M] |
| Graphische Spurklassifikation | ⚠[M] -> NEU-66 |
| Hypothese Z_N -> ξ | ❓[O] Hauptbrücke |

---

## Literatur

- Simon, B.: *Trace Ideals*, AMS 2005, Kap. 3–4 (Fredholm-Det, Log-Derivate)
- Teschl, G.: *Jacobi Operators*, AMS 2000 (Weyl-Funktion, Kettenbruch)
- Hurwitz, A.: Theorem über Grenzwerte meromorpher Funktionen (in Reed-Simon II)
- Connes, A.: Selecta Math. 5 (1999) (Spurformel, geschlossene Orbits)
- Titchmarsh, E.C.: *Riemann Zeta-Function*, Kap. 3 (Hadamard-Produkt, ξ)
