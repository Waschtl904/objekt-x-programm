# NEU-64 — Endliche Weyl-Funktionen und Determinantenquotienten-Struktur

**Status:** J-Bruch-Rahmen ✓[M]; Log-Derivat-Hypothese ⚠[M]; Block-Fall ❓[O]  
**Datum:** 2026-06-29 (korrigiert: Log-Derivat statt Euler-Produkt; Block-J-Bruch)  
**Aufbaut auf:** NEU-63 (Zwei-Seiten-Strategie), NEU-61/62 (Core-Konvergenz)

---

## Ziel

Berechne die endlichen Weyl-Funktionen

```
m_{Ω,N}(z) := ⟨Ω_N, (A_N^{Jac,-} - z)^{-1} Ω_N⟩
```

explizit und identifiziere sie als logarithmische Ableitung eines endlichen
arithmetischen Determinantenobjekts:

```
m_{Ω,N}(z) = -∂_z log Z_N(z) + R_N(z)
```

wobei Z_N(s) -> ξ(s) im Limes N -> ∞. Daraus folgt (via NEU-63.B):

```
m_Ω(z) = m_arith(z) = -i ξ'/ξ(1/2+iz).    ❓[O]
```

---

## Korrektur 1: Kein Euler-Produkt, sondern Log-Derivat ⚠[M]

**Frühere Formulierung (zu stark):**
```
m_{Ω,N}(z) ~ Π_{p ≤ P(N)} f_p(z)    [Euler-Produkt-Hypothese]
```

Diese Hypothese ist zu grob. Für endliche Jacobi-Operatoren gilt typischerweise:

```
m_{Ω,N}(z) = -Q_N(z) / P_N(z)    (Quotient charakteristischer Polynome)
```

Das ist ein **Quotient von Polynomen**, kein Produkt. In speziellen Spur-/
zyklischen Situationen gilt zusätzlich:

```
m_{Ω,N}(z) = ∂_z log P_N(z)
```

(logarithmische Ableitung des charakteristischen Polynoms), aber nicht
allgemein.

**Korrekte Hypothese:** ⚠[M]

```
m_{Ω,N}(z) ist ein logarithmisches Derivat eines endlichen arithmetischen
Determinantenobjekts Z_N, nicht ein Euler-Produkt selbst.
```

Die Verbindung zur Zielgröße

```
m_arith(z) = -i ξ'/ξ(1/2+iz)
```

ist natürlich, weil ξ'/ξ selbst ein **logarithmisches Derivat** ist. ⚠[M]

---

## Korrektur 2: Block-J-Bruch als Hauptform ❓[O]

Wenn D_rel nach m-Sektoren, Primzahl-Typen oder Divisorkomponenten
blockartig gekoppelt ist (nicht irreduzibel tridiagonal), lautet die
endliche Weyl-Struktur als **Block-Schur-Komplement**:

```
M_N(z) = ( A_{00} - z - B_0^* (A_{11} - z - ...)^{-1} B_0 )^{-1}
```

Das ist eine **Matrix-Herglotz-Funktion** (nicht skalare Weyl-Funktion).

Der skalare J-Bruch

```
m_N(z) = 1 / (a_1 - z - b_1^2/(a_2 - z - ...))
```

bleibt als Spezialfall korrekt (wenn D_rel auf einem Sektor eindimensional-
Jacobi agiert), aber der Block-Fall ist die allgemeine Form.

**Konsequenz für NEU-65:** Die relevante Determinante ist wahrscheinlich
eine **Block-Determinante** (Schur-Komplement-Determinante), nicht die
skalare charakteristische Determinante. ❓[O]

---

## Satz NEU-64.1 — Log-Derivat-Darstellung ⚠[M]

**Behauptung (Zielform):**

```
m_{Ω,N}(z) = -∂_z log Z_N(z) + R_N(z)
```

wobei:
- Z_N(z) ein endliches arithmetisches Determinantenobjekt ist (-> NEU-65)
- R_N(z) ein kontrollierter regulärer Term (Herglotz-neutral oder explizit)

Im Limes:
```
Z_N(s) -> ξ(s)    (geeignete Hadamard-/Euler-/Feshbach-Regularisierung)
     ⇓
m_{Ω,N}(z) -> -i ξ'/ξ(1/2+iz) + R(z) = m_arith(z) + R(z)
```

Der Regularisierungsterm R(z) muss Herglotz-neutral sein (reell für z ∈ ℝ,
oder explizit identifizierbar). ⚠[M]

---

## Satz NEU-64.2 — J-Bruch-Konvergenz (Spezialfall) ✓[M]

Im skalaren Fall (D_rel tridiagonal auf einem Sektor):

```
m_{Ω,N}(z) = [a_1, b_1^2; a_2, b_2^2; ...; a_N, 0](z)    (J-Bruch)
```

Konvergenz m_{Ω,N}(z) -> m_Ω(z) via NEU-60/61 (starke Resolventenkonvergenz
= Kettenbruch-Konvergenz; Teschl, Thm. 2.8). ✓[M]

---

## Arithmetische Struktur der Momente ⚠[M]

Die Momente m_k := <Ω, A_N^k Ω> sind Divisor-Pfadsummen:

```
m_k = Σ_{n_1|m,...,n_k|m}  (Produkt der Θ-Koeffizienten entlang Pfad)
    = Σ |r||r+n_1|...|r+n_1+...+n_{k-1}| · log(n_1)...log(n_k) · |⟨...,Ω⟩|^2
```

Diese sind **Dirichlet-artige Summen mit Von-Mangoldt-Gewichten** log(n_j). ⚠[M]

---

## Hauptaufgabe NEU-64 (präzisiert)

```
Identifiziere m_{Ω,N}(z) bzw. M_N(z) als logarithmische Ableitung eines
endlichen arithmetischen Determinantenquotienten Z_N(s) bei s = 1/2+iz.
```

Konkret:
```
det_rel(A_N^{Jac,-} - z)  =?  endliches arithmetisches Z_N(1/2+iz)    -> NEU-65
```

---

## Status NEU-64

| Objekt | Status |
|---|---|
| J-Bruch-Darstellung (skalarer Fall) | ✓[M] |
| Kettenbruch-Konvergenz via NEU-60/61 | ✓[M] |
| Log-Derivat-Hypothese m = -∂ log Z | ⚠[M] |
| Block-J-Bruch (Matrix-Fall) | ❓[O] |
| Momente als Divisor-Pfadsummen | ⚠[M] |
| Euler-Produkt-Hypothese | **aufgegeben** (zu grob) |
| Z_N(s) -> ξ(s) (Determinantenlimes) | ❓[O] -> NEU-65 |
| m_arith = -iξ'/ξ(1/2+iz) reguliert | ⚠[M] |

---

## Literatur

- Teschl, G.: *Jacobi Operators*, AMS 2000, Thm. 2.8 (Kettenbruch-Konvergenz)
- Simon, B.: *Szegő's Theorem*, AMS 2011, Kap. 2 (Herglotz, Log-Derivat)
- Gesztesy, F. & Tsekanovskii, E.: Math. Nachr. 218 (2000) (Matrix-Herglotz)
- Titchmarsh, E.C.: *Riemann Zeta-Function*, Kap. 3 (ξ'/ξ als Log-Derivat)
- Simon, B.: *Trace Ideals*, AMS 2005 (Fredholm-Determinanten, Log-Derivate)
- Forman, R.: *Functional Determinants and Geometry*, Invent. Math. 88 (1987)
  (Feshbach-/Schur-Komplement-Determinanten)
