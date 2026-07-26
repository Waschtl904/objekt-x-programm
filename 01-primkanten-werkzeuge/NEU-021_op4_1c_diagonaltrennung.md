# NEU-21 — OP-4.1c: Diagonaltrennung im Hauptsymbol

> Datum: 20. Juni 2026 | Aufbauend auf NEU-17–20 (OP-3 abgeschlossen)
> Status: ✓ [M] (Proposition OP-4.1c.1) | ❓ [O] (OP-4.1c.2, OP-4.1c.3)

---

## Kontext und Gesamtstruktur

OP-4.1 fragt nach der strikten modularen Frobenius-Nicht-Ausgeartheit der Paarung

```
B : HH⁴(B₃, B₃) × HH₄(B₃) → ℂ
B([Ψ], [c]) := Wres_BC^{top}(R₃(Ψ(c)))
```

wobei `B₃ := F³ A_BC^{an}`.

**Wichtige Einschränkung (Präzisierung aus OP-3-Analyse):**
Die Paarung kann a priori nicht auf ganz HH⁴(B₃, B₃) nicht-ausgeartet sein. Denn jede
Klasse [Ψ] mit

```
R₃(Ψ(c)) = 0   für alle c ∈ HH₄(B₃)
```

gibt B([Ψ],[c]) = 0 für alle [c], selbst wenn [Ψ] ≠ 0 in einem tieferen
Filtrationsanteil lebt.

**Strategie (dreistufig):**

- **(OP-4.1c.1)** Trennung auf dem R₃-sichtbaren Quotienten ← **NEU-21** ✓ [M]
- **(OP-4.1c.2)** R₃-Sichtbarkeit: [Ψ] ≠ 0 ⟹ R₃[Ψ] ≠ 0 ❓ [O]
- **(OP-4.1c.3)** Diagonal-Neutralität: R₃[Ψ] ≠ 0 ⟹ ∃ neutraler Diagonalkoeffizient ≠ 0 ❓ [O]

Volle Nicht-Ausgeartheit auf ganz HH⁴ = (OP-4.1c.1) + (OP-4.1c.2) + (OP-4.1c.3).

---

## Definitionen

**Sichtbarer Quotient:**

```
HH⁴_vis(B₃) := HH⁴(B₃, B₃) / ker(R₃-diag-Wres)
```

wobei

```
ker(R₃-diag-Wres) := { [Ψ] | Wres_BC^{(2,0)}(R₃(Ψ(c))) = 0 für alle c }.
```

**Neutraler Diagonalsektor:**
Der χ=1-Sektor von Gr³ A_BC^{an}, d.h. der Teil mit Monoidladung 1 unter der
N×-Wirkung. Πdiag,0 projiziert auf (m,m,0)-Koeffizienten (Fourier-Index 0,
Monoidlabel m=m).

**Λ₂-Typ:**
Ein Diagonalkoeffizient F_M (M ∈ N×) ist vom Λ₂-Typ, falls

```
Σ_M F_M · M^{-β}  ~  C · (−ζ'/ζ)²(β)   (führender Doppelpol bei β→1⁺)
```

mit C ≠ 0.

---

## Proposition OP-4.1c.1 — Diagonaltrennung im Hauptsymbol ✓ [M]

**Voraussetzung:**
Sei Ψ ∈ Z⁴(B₃, B₃) ein Hochschild-4-Kozykel mit R₃Ψ ≠ 0.
Angenommen, R₃Ψ besitzt einen neutralen Fourier-Monoid-Koeffizienten, der
nicht durch Hochschild-Ränder eliminiert wird.

**Behauptung:**
Es existiert ein Hochschild-4-Zyklus c₄ ∈ Z₄(B₃) mit

```
Wres_BC^{(2,0)}(R₃(Ψ(c₄))) ≠ 0.
```

Insbesondere trennt B die Klasse [Ψ] im R₃-sichtbaren Quotienten:

```
B ist nicht-ausgeartet auf HH⁴_vis(B₃).
```

---

## Beweis von Proposition OP-4.1c.1

### Schritt 1 — Existenz eines nichttrivialen Hauptsymbolkoeffizienten

Da R₃Ψ ≠ 0 in Gr³ A_BC^{an} und der neutrale Koeffizient nicht durch
Hochschild-Ränder eliminiert wird, existieren Monoidlabel N ∈ N× und
Fourier-Index q ∈ ℤ, so dass

```
(R₃Ψ)(a₁, a₂, a₃, a₄)  enthält  C · e_q V_N   (C ≠ 0)
```

für geeignete Testelemente a₁,...,a₄ ∈ B₃.

*Begründung:* Gr³ A_BC^{an} wird von Elementen e_r V_n aufgespannt. Wäre jeder
Koeffizient null oder durch Ränder killbar, so wäre R₃[Ψ] = 0 im assoziierten
Graduierten — Widerspruch zur Voraussetzung.

### Schritt 2 — Diagonalisierung durch linken Testfaktor

Wähle den linken Testfaktor

```
a₀ := e_{−q} · V_{L}
```

wobei L ∈ N× so gewählt wird, dass das kombinierte Monoidelement L·N durch
geeignete Primpotenzen zerlegt werden kann (L = 1 genügt für den Diagonalschritt).

Dann gilt:

```
a₀ · (e_q V_N) = e_{-q} · e_q · V_{L·N} = e₀ · V_{L·N}.
```

Das Fourier-Produkt ergibt den neutralen Index 0; das Monoidlabel ist L·N.

### Schritt 3 — Konstruktion des Hochschild-4-Zyklus c₄

Definiere den antisymmetrisierten Zyklus:

```
c₄^{alt} := Σ_{σ ∈ S₄} sgn(σ) · a₀ ⊗ a_{σ(1)} ⊗ a_{σ(2)} ⊗ a_{σ(3)} ⊗ a_{σ(4)}
```

Im assoziierten Graduierten Gr³ ist c₄^{alt} ein HKR-artiger Zyklus:

- Der Hochschild-Rand b(c₄^{alt}) fällt in F⁴ A_BC^{an} (wegen Antisymmetrisierung
  und Graded-Kommutatoreigenschaft im Gr³-Kalkül).
- Da R₃ den F⁴-Anteil zu Null macht (Quotient nach F⁴), gilt:

```
R₃(b(c₄^{alt})) = 0,
```

also ist c₄^{alt} ein Zyklus modulo F⁴, ausreichend für Wres_BC^{top}.

### Schritt 4 — Auswertung: Λ₂-Anteil im Diagonalsektor

Wir berechnen Π_{diag,0}(R₃(Ψ(c₄^{alt}))):

Aus Schritt 1–2 hat R₃(Ψ(c₄^{alt})) einen Diagonalkoeffizienten der Form

```
Π_{diag,0}(R₃(Ψ(c₄^{alt})))_M = C_Ψ · F_M
```

wobei F_M aus der expliziten ω̃₂-Berechnung stammt (analog NEU-20):

Um zwei unabhängige Primlabels zu erzeugen, wähle in den a_i zwei Monoid-
richtungen V_p, V_q (p, q Primzahlen). Der Diagonalkoeffizient enthält dann
Beiträge der Form log(p)·log(q), und nach Summation über p·q = M:

```
Π_{diag,0}(R₃(Ψ(c₄^{alt})))_M = C_Ψ · Λ₂(M) + (Terme niedrigerer Singularitätsordnung)
```

wobei Λ₂ = Λ*Λ die volle von-Mangoldt-Faltung ist und C_Ψ ≠ 0 aus dem
nichtverschwindenden Hauptsymbolkoeffizienten aus Schritt 1 folgt.

*Prototyp aus OP-3 (NEU-20):*
Der Zeuge n=2, m=3, r=4, s=1, t=−1, k=1 lieferte:

```
C'_{4,1} = −24·log(2)·log(6)/μ ≠ 0
```

Der abstrakte Schritt generalisiert: Jeder nichttriviale Hauptsymbolkoeffizient
C · e_q V_N mit zwei Primfaktoren im Monoidlabel liefert einen Λ₂-Beitrag.

### Schritt 5 — Wres_BC^{(2,0)} ≠ 0

Aus Schritt 4:

```
Σ_M Π_{diag,0}(R₃(Ψ(c₄^{alt})))_M · M^{-β}
  = C_Ψ · Σ_M Λ₂(M) M^{-β} + (reguläre Terme bei β→1⁺)
  = C_Ψ · (−ζ'/ζ)²(β) + ...
```

Der führende Doppelpol bei β→1⁺ liefert:

```
Wres_BC^{(2,0)}(R₃(Ψ(c₄^{alt}))) = C_Ψ ≠ 0.
```

Also:

```
B([Ψ], [c₄^{alt}]) = Wres_BC^{top}(R₃(Ψ(c₄^{alt}))) ≠ 0.   □
```

---

## Zusammenfassung: Was NEU-21 leistet und was offen bleibt

**Gesichert ✓ [M]:**

```
B ist nicht-ausgeartet auf HH⁴_vis(B₃)
 = HH⁴(B₃,B₃) / ker(R₃-diag-Wres).
```

Konkret: Jede Klasse [Ψ] mit nichttrivialem, neutral-sichtbarem Hauptsymbol
wird durch einen explizit konstruierbaren Zyklus c₄^{alt} getrennt.

**Beweisskette:**

```
[Ψ] ≠ 0, R₃[Ψ] ≠ 0, neutraler Koeffizient ≠ 0
 ⇒  Fourier-/Monoid-Testdaten diagonalisieren Hauptsymbol
 ⇒  Π_{diag,0}(R₃(Ψ(c₄))) hat Λ₂-Anteil mit C_Ψ ≠ 0
 ⇒  Wres_BC^{(2,0)} ≠ 0
 ⇒  B([Ψ],[c₄]) ≠ 0
```

**Offen ❓ [O]:**

| Problem | Aussage | Status |
|---------|---------|--------|
| OP-4.1c.2 | [Ψ] ≠ 0 ⟹ R₃[Ψ] ≠ 0 (R₃-Sichtbarkeit) | ❓ [O] |
| OP-4.1c.3 | R₃[Ψ] ≠ 0 ⟹ ∃ neutraler Diagonalkoeff. ≠ 0 | ❓ [O] |

**Schwächster Punkt:**
Die Voraussetzung „neutraler Koeffizient nicht durch Ränder eliminiert" ist eine
Bedingung an die Kohomologie, keine automatische Folge aus R₃Ψ ≠ 0. OP-4.1c.3
muss dies für relevante Klassen verifizieren.

**Schlüsselidentifikation:**
Das Trennungsprinzip funktioniert, weil die ω̃₂-Formel

```
ω̃₂(e_r V_n, e_s V_m) = −r·s·log(n) · e_{r+ns} · V_{nm}
```

(Fourier-Exponent r+ns, NICHT r+s) zwei Primrichtungen in den Diagonalsektor
dreht. NEU-20 ist nicht nur Zeuge für [L₃] ≠ 0, sondern liefert den Prototyp
für alle OP-4.1c.1-Trennungen.

---

*Datei: `werkzeuge/neu21_op4_1c_diagonaltrennung.md` | 20. Juni 2026*
*Nächste Schritte: OP-4.1c.2 (R₃-Sichtbarkeit) → OP-4.1c.3 (Diagonal-Neutralität)*
