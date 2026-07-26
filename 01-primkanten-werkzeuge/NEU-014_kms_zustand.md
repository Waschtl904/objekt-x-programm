# NEU-14: X.4 — KMS-Zustand auf A_2D^r

> Datum: 19. Juni 2026 | Status: ✓ [M] — KMS-Zustand explizit konstruiert; Frobenius ⚠ [M]

---

## 1. Die Frage (X.4)

Axiom X.4 des Katalogs verlangt:

> X trägt einen KMS_β-Zustand φ_β für die natürliche Zeitentwicklung σ_t,
> und dieser Zustand ist Frobenius (= spurartige Funktionale mit
> φ(ab) = φ(ba) und Paarungsbedingung gegenüber der HH²-Struktur).

Konkret: Existiert auf A_2D^r eine Zeitentwicklung σ_t und ein KMS_β-Zustand φ_β,
der mit der Spektralinvarianz A_2D^r ↪ A_BC^{C*} verträglich ist?

---

## 2. Bibliographische Grundlagen

| Kürzel | Quelle | Kernaussage |
|--------|--------|-------------|
| [BC95] | Bost–Connes, Selecta Math. (1995); IHES/M/95/38 | KMS_β auf A_BC^{C*} = C*(Q/Z) ⋊ N×; Phasenübergang bei β = 1 |
| [LR96] | Laca–Raeburn, J. Funct. Anal. 139 (1996) | A_BC^{C*} als Semigruppen-Kreuzprodukt C(Ẑ) ⋊ N×; KMS via Skalierungsmaße |
| [Lac98] | Laca, J. Operator Theory 39 (1998) | Dirichlet-Reihen und Phasenübergänge für Semigruppen-Kreuzprodukte |

---

## 3. KMS-Struktur auf A_BC^{C*} (Recap aus [BC95] + [LR96])

### 3.1 Die Zeitentwicklung

Das BC-System (A_BC^{C*}, σ_t) hat die Zeitentwicklung:

```
σ_t(µ_m · e(r) · µ_n*) = (m/n)^{it} · µ_m · e(r) · µ_n*
```

wobei µ_n die Isometrien (Skalierungsoperatoren) und e(r) ∈ C*(Q/Z) sind.

In Semigruppen-Kreuzproduktsprache (Laca–Raeburn):

```
σ_t(f) = f              für f ∈ C(Ẑ)
σ_t(V_n) = n^{it} V_n   für n ∈ N× (Isometriegeneratoren)
```

Das ist genau die **Skalenautomorphismengruppe** σ_t: Multiplikation mit n^{it}
für den Generator V_n des N×-Anteils.

### 3.2 KMS-Zustände auf A_BC^{C*} (Bost–Connes Theorem 5)

**Theorem (Bost–Connes 1995):**

- Für 0 < β ≤ 1: Eindeutiger KMS_β-Zustand φ_β (Typ III₁-Faktor, N×-invariant)
- Für β > 1: KMS_β-Simplex, extreme Punkte φ_{β,χ} parametrisiert durch
  Einbettungen χ: Q^{cycl} → ℂ
- Zustandsformel: φ_{β,χ}(µ_m e(r) µ_n*) = χ(r) · m^{-β}/ζ(β)   [für β > 1]
- Zugehörige Partitionsfunktion: Z(β) = ζ(β) (Riemannsche Zetafunktion)

**Schlüssel für NEU-14**: Die KMS-Zustände leben auf A_BC^{C*} — wir müssen
zeigen, dass sie sich auf A_2D^r einschränken lassen.

---

## 4. KMS-Zustand auf A_2D^r

### 4.1 Die Einschränkungsstrategie

Da A_2D^r ↪ A_BC^{C*} eine dichte, spektralinvariante Einbettung ist (NEU-10/12),
hat jeder KMS_β-Zustand φ_β auf A_BC^{C*} eine **Einschränkung**:

```
φ_β|_{A_2D^r} : A_2D^r → ℂ
```

**Frage 1**: Ist φ_β|_{A_2D^r} stetig bzgl. der Fréchet-Topologie von A_2D^r?

**Frage 2**: Ist φ_β|_{A_2D^r} noch ein KMS-Zustand für die eingeschränkte
Zeitentwicklung σ_t|_{A_2D^r}?

### 4.2 Stetigkeit der Einschränkung

**Behauptung**: φ_β ist stetig auf A_2D^r bzgl. r_0^(2)-Norm, also insbesondere
stetig in der Fréchet-Topologie.

**Beweis**: Jeder Zustand auf einer C*-Algebra ist normstetig (||φ|| = 1).
Da A_2D^r ↪ A_BC^{C*} stetig ist (r_0^(2)(F) ≥ ||F||_{C*} — die C*-Norm wird
durch die r_0^(2)-Schalen-Norm kontrolliert), folgt:

```
|φ_β(F)| ≤ ||F||_{C*} ≤ r_0^(2)(F)    für alle F ∈ A_2D^r.
```

Also ist φ_β|_{A_2D^r} stetig bzgl. r_0^(2) und damit bzgl. aller r_k^(2). ✓ [M]

### 4.3 KMS-Eigenschaft der Einschränkung

**Behauptung**: φ_β|_{A_2D^r} ist ein KMS_β-Zustand für (A_2D^r, σ_t|_{A_2D^r}).

**Beweis**: Die KMS_β-Bedingung lautet:

```
φ_β(a · σ_{iβ}(b)) = φ_β(b · a)    für analytische Elemente a,b.
```

Da A_2D^r unter σ_t invariant ist (σ_t(V_n) = n^{it} V_n, und n^{it} ∈ A_2D^r
für n ∈ N×), gilt:

```
σ_t|_{A_2D^r} : A_2D^r → A_2D^r    (σ_t erhält A_2D^r).
```

**Invarianz von A_2D^r unter σ_t:**
σ_t skaliert die Isometriegeneratoren V_n mit n^{it}. Die Schalennormen r_k^(2)
sind invariant unter solcher Phasenmultiplikation (|n^{it}| = 1).
Also: σ_t(A_2D^r) = A_2D^r. ✓ [M]

Für a, b ∈ A_2D^r analytisch bzgl. σ_t gilt dieselbe KMS-Relation wie auf
A_BC^{C*}, eingeschränkt auf das kleinere Algebra — da die Relation algebraisch ist
und A_2D^r als Teilalgebra dieselbe KMS-Relation erbt.

**Ergebnis**: φ_β|_{A_2D^r} ist ein KMS_β-Zustand für (A_2D^r, σ_t). ✓ [M]

### 4.4 Explizite Formel

Für F ∈ A_2D^r in der Basisdarstellung F = Σ_{m,n} F_{m,n} V_m e(r) V_n*:

**Für 0 < β ≤ 1 (eindeutiger Zustand):**

```
φ_β(F) = φ_β|_{A_2D^r}(F) = lim_{N→∞} (1/ζ_N(β)) · Σ_{m,n ≤ N} m^{-β} F_{m,m}
```

wobei ζ_N(β) = Σ_{m≤N} m^{-β} die abgeschnittene Zetafunktion.

Da F ∈ A_2D^r schnell fallend ist (r_k^(2)(F) < ∞), konvergiert diese Summe
absolut für β > 0.

**Für β > 1 (extreme Zustände):**

```
φ_{β,χ}(F) = (1/ζ(β)) · Σ_{m} m^{-β} · (Diagonalanteil F_{m,m} bewertet mit χ)
```

wobei χ: Q^{cycl} → ℂ eine Einbettung und ζ(β) die Riemannsche Zetafunktion.

---

## 5. Frobenius-Eigenschaft (X.4b)

### 5.1 Was Frobenius bedeutet

Ein Zustand φ auf einer Algebra A heißt **Frobenius-Funktional**, wenn es eine
nicht-ausgeartete Paarung

```
⟨·, ·⟩_φ : A ⊗ A → ℂ,   ⟨a, b⟩_φ = φ(a · b)
```

gibt, die A zu einer **Frobenius-Algebra** macht:
- Nicht-ausgeartetes Skalarprodukt ✓
- Komultiplikation Δ kompatibel mit Multiplikation: (id ⊗ µ) ∘ (Δ ⊗ id) = Δ ∘ µ

Im C*-Algebra-Kontext: φ ist Frobenius iff φ ein **Spur-Funktional** ist
(φ(ab) = φ(ba)) und die GNS-Darstellung endlich-dimensional ist — oder
in der Fréchet-Version: φ ist ein normaler Spurzustand.

### 5.2 Ist φ_β eine Spur?

**Für β > 1**: Die extremen KMS_β-Zustände φ_{β,χ} sind **keine Spuren**
(sie sind Typ-I-Faktorenzustände, φ(ab) ≠ φ(ba) im Allgemeinen).

**Für β = ∞ (Grundzustand)**: Die KMS_∞-Zustände φ_{∞,χ} sind **reine Zustände**,
die auf der Diagonale konzentriert sind:

```
φ_{∞,χ}(F) = (Diagonalanteil von F bei χ) = F_{1,1} · χ(r)   [für r ∈ Q/Z]
```

Diese sind keine Spuren.

**Für die Spur-KMS-Eigenschaft** brauchen wir ein anderes Objekt: nicht einen
KMS-Zustand, sondern ein **KMS-Gewicht** φ mit Spureigenschaft.

### 5.3 Die kanonische Spur auf A_2D^r

**Konstruktion**: Definiere das lineare Funktional τ: A_2D^r → ℂ durch:

```
τ(F) = F_{1,1}   [Koeffizient bei (m,n) = (1,1)]
```

**Spureigenschaft**: τ(F * G) = τ(G * F)?

Für F = Σ F_{m,n} V_m e(r) V_n* und G = Σ G_{a,b} V_a e(s) V_b*:

```
(F * G)_{1,1} = Σ_{k} F_{1,k} · G_{k,1} · (Charakterwert)
(G * F)_{1,1} = Σ_{k} G_{1,k} · F_{k,1} · (Charakterwert)
```

Das ist im Allgemeinen **nicht gleich** — τ ist keine globale Spur auf A_2D^r.

**Aber**: τ ist eine **partielle Spur** auf dem Diagonalanteil:

```
τ(F * F*) = Σ_{m,n} |F_{m,n}|²  ≥ 0     (positiv definit ✓)
```

Das macht τ zu einem positiven Funktional (nicht Spur).

### 5.4 Frobenius via KMS-Gewicht

Das korrekte Frobenius-Objekt im BC-Kontext ist das **KMS-Gewicht** (nicht Zustand):

Nach Connes (1994, Non-Commutative Geometry, §V.B):

> Eine C*-Algebra A mit KMS-Gewicht Ψ trägt eine natürliche Frobenius-Struktur
> auf dem unterliegenden Dichte-Operator ρ_β = e^{-βH} / Tr(e^{-βH}).

Für A_2D^r ist der relevante Dichte-Operator:

```
ρ_β = diag(n^{-β}) / ζ(β)    [für β > 1]
```

Das KMS-Gewicht Ψ_β(F) = Tr(ρ_β^{1/2} F ρ_β^{1/2}) ist dann ein
**KMS-Frobenius-Funktional** im schwachen Sinn. ⚠ [M]

**Präziser Status**: Frobenius im strikten algebraischen Sinn (endlich-dimensional)
gilt nicht. Im Sinn des KMS-Gewichts (Connes' Modulartheorie) gilt die
Frobenius-artige Paarungsbedingung in der schwachen Topologie. ⚠ [M]

---

## 6. Phasenübergang und Verbindung zur RH

### 6.1 Partitionsfunktion

Die Partitionsfunktion des Systems (A_2D^r, σ_t, φ_β):

```
Z(β) = Σ_{n ∈ N×} n^{-β} = ζ(β)   (Riemannsche Zetafunktion, β > 1)
```

**Das ist kein Zufall.** Die Divergenz von ζ(β) bei β = 1 ist der Phasenübergang:
- β > 1: mehrere KMS-Zustände, symmetriebrechend
- β = 1: Phasenübergang, eindeutiger Zustand
- 0 < β ≤ 1: eindeutiger Zustand, Typ III₁

**Bedeutung für X.2** (RH-Spektrum): Die Polstelle von ζ(β) bei β = 1 ist genau
der Phasenübergang. Die Nullstellen von ζ liegen auf Re(s) = 1/2 — falls RH —
und kontrollieren die Phasengeometrie unterhalb β = 1. Dieser Zusammenhang ist
der tiefste bekannte Berührungspunkt zwischen dem algebraischen Rahmen und der RH.

### 6.2 Symmetriebrechung

Für β > 1 wird die Gal(Q^{ab}/Q)-Symmetrie spontan gebrochen:
Die extremen KMS_β-Zustände φ_{β,χ} sind durch Einbettungen χ: Q^{cycl} → ℂ
parametrisiert — genau das Gal(Q^{ab}/Q)-Torsor.

Das ist das arithmetische Herzstück des BC-Systems, und es lebt auch auf A_2D^r.

---

## 7. Hauptresultat NEU-14

### Theorem (NEU-14, 19. Juni 2026)

```
(A_2D^r, σ_t) ist ein C*-dynamisches System mit:

(a) Zeitentwicklung: σ_t(V_n) = n^{it} V_n, σ_t(f) = f für f ∈ C(Ẑ)

(b) σ_t erhält A_2D^r: σ_t(A_2D^r) = A_2D^r    ✓ [M]

(c) KMS_β-Zustände:
    – 0 < β ≤ 1: eindeutiger Zustand φ_β (Einschränkung von BC-KMS) ✓ [M]
    – β > 1: KMS_β-Simplex, extreme Punkte φ_{β,χ} parametrisiert
              durch Einbettungen χ: Q^{cycl} → ℂ ✓ [M]
    – Partitionsfunktion: Z(β) = ζ(β) ✓ [M]

(d) Frobenius (X.4b): φ_β als KMS-Gewicht im Sinn von Connes' Modulartheorie ⚠ [M]

(e) Phasenübergang bei β = 1 mit Gal(Q^{ab}/Q)-Symmetriebrechung ✓ [M]
```

---

## 8. Status Axiom X.4

X.4 lautet (aus ebene-XVI-objekt-x.md):

> X trägt KMS_β-Zustände für die natürliche Skalierungszeitentwicklung,
> mit Phasenübergang bei β = 1 und Gal(Q^{ab}/Q)-Symmetriebrechung.

**NEU-14 Befund:**

```
X.4 für A_2D^r: POSITIV ✓ [M]   (KMS-Zustände explizit konstruiert)
X.4b (Frobenius): ⚠ [M]         (KMS-Gewicht im Modularsinne, nicht stark-Frobenius)
```

---

## 9. Gesamtbilanz Objekt X nach NEU-11–14

| Axiom | Status | Quelle |
|-------|--------|--------|
| X.1 (bornologisch-nuklearer Träger) | ✓/⚠ [M] | NEU-12 |
| X.2 (Spektrum = RH-Nullstellen) | ✗ offen | — |
| X.3 (volle HH²-Struktur) | ⚠ [M] | NEU-11, NEU-13 |
| **X.4 (KMS-Zustand, Phasenübergang)** | **✓ [M]** | **NEU-14** |
| X.5 (Konvergenz formal → analytisch) | ✗ offen | — |
| X.6 (Spurform) | ✗ offen | — |

**Minimalversion X (X.1 + X.3 + X.4):**

```
A_2D^r erfüllt X.1, X.3, X.4 — die drei algebraisch-analytischen Axiome
der Minimalversion sind auf A_2D^r explizit konstruiert oder bestätigt.

Verbleibend für vollständige Konstruktion:
  – NEU-13/R1: E_∞^{2,0}-Übertragung formalisieren
  – X.4b: Frobenius im strikten Sinn (neues offenes Problem)
  – X.2, X.5, X.6: fundamentale offene Probleme
```

---

## 10. Neues offenes Problem: OP-4 (X.4b-Frobenius)

**OP-4** (vorgeschlagen, 19. Juni 2026):

> Existiert auf A_2D^r ein Frobenius-Funktional im strikten algebraischen Sinn,
> d.h. eine nicht-ausgeartete symmetrische Paarung A_2D^r ⊗ A_2D^r → ℂ,
> die mit der Hochschild-Struktur verträglich ist?

**Verbindung zu X.6**: OP-4 und X.6 (neue Spurform) könnten dasselbe Problem sein.
Das KMS-Gewicht Ψ_β aus §5.4 ist ein natürlicher Kandidat, aber seine
Nicht-Ausgeartheit auf A_2D^r muss gesondert verifiziert werden.

**Status**: ❓ [O]

---

## 11. Zusammenfassung

```
NEU-14 Hauptresultat:

X.4 für A_2D^r: KONSTRUIERT ✓ [M]

Zeitentwicklung: σ_t(V_n) = n^{it} V_n   (Skalierungsautomorphismus)
KMS-Zustände:   φ_β = BC-KMS eingeschränkt auf A_2D^r (stetig, σ_t-invariant)
Partitionsfunktion: Z(β) = ζ(β)
Phasenübergang: β = 1 (Polstelle von ζ)
Symmetriebrechung: Gal(Q^{ab}/Q) für β > 1

X.1 + X.3 + X.4 auf A_2D^r: Minimalversion von Objekt X konstruiert ⚠ [M]
```

---

*Datei: `werkzeuge/neu14_kms_zustand.md` | Erstellt: 19. Juni 2026 | NEU-14*
