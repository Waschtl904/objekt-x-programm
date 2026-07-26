# NEU-177 — Direkter Kozykeltest und gewichteter Dualzyklus für L₃,λ

## Vorbemerkung: Statuskorrektur zu NEU-176

Da [O-176-1] von einer Modellannahme über Eigenvektoren in B₃^mod = A_Q abhängt, wird der Status präzisiert:

> **[O-176-1]** ✓[K] | [H-176-1]

wobei [H-176-1] die explizite Hypothese "A_Q besitzt genügend α_t-Eigenvektoren zu nichttrivialen Gewichten, die sich zu λ ≠ 0 im Grad 4 summieren" bezeichnet.

**Korrigierte Statustabelle nach NEU-176:**

| Knoten | Status |
|---|---|
| [O-176-1] | ✓[K] \| [H-176-1] |
| [O-176-2] | ?[O] |
| [O-176-3] | ?[O] |
| [O-176-4] | gesperrt durch [O-176-2/3] |
| [O-176-5] | gesperrt durch [O-176-4] |
| [O-176-orig] | ?[O] |

### Vorläufige Architektur mit gestrichelten Kanten

```
(C_fin^•, b) ⟶ [P^ch] ⇢ [L₃^mod]_ch ≠ 0 ⇢ ρ_op(L₃^mod)
```

Die erste gestrichelte Kante hängt an [O-176-2/3]; die zweite hängt zusätzlich an der späteren Operatorrealisierung (NEU-178). Die Operatorrealisierung **darf nicht** als eigenständiger Knoten NEU-177 beginnen, solange weder bL_{3,λ}=0 noch [L_{3,λ}]≠0 bewiesen ist.

---

## Typisierung des Dualzeugen

Ein bloßes "Spurfunktional" reicht nicht. Die natürliche duale Struktur für L_{3,λ} ∈ C⁴(B₃^mod, M) ist der Hochschild-**Kettenkomplex** mit Koeffizienten im algebraischen Dual

```
M^∨ := Hom_C(M, C)
```

mit dualer Bimodulwirkung:

```
(a · f · b)(m) := f(b · m · a)
```

### Definition des Kettenkomplexes

```
C_4(B₃^mod, M^∨) := M^∨ ⊗ (B₃^mod)^{⊗4}
```

mit Randoperator ∂: C_n(B₃^mod, M^∨) → C_{n-1}(B₃^mod, M^∨), definiert dual zu b über die Standard-Hochschild-Randformel auf Ketten.

### Paarung

```
⟨φ, f⊗a₁⊗⋯⊗a₄⟩ := f(φ(a₁,…,a₄))
```

### Adjungiertheitsidentität

> **⟨bψ, z⟩ = ⟨ψ, ∂z⟩**

Diese Identität muss mit konsistenten Vorzeichenkonventionen bewiesen werden (Standard-Dualität von Kochain- und Kettenkomplex).

**Konsequenz:** Ist ∂z = 0, so folgt für jeden Korand bψ: ⟨bψ, z⟩ = ⟨ψ, ∂z⟩ = 0. Findet man zugleich ⟨L_{3,λ}, z⟩ ≠ 0, folgt streng L_{3,λ} ∉ bC³_{fin,λ} — der gesuchte Nicht-Korand-Beweis.

---

## Gewichtsbedingung des Zeugen

Der Zeuge kann nicht beliebig gewählt werden. Ist die Paarung unter der BC-Zeitwirkung invariant und besitzt L_{3,λ} Gewicht λ ≠ 0, so gilt für einen Zeugen z_μ vom Gewicht μ:

```
⟨L_{3,λ}, z_μ⟩ = e^{it(λ+μ)} ⟨L_{3,λ}, z_μ⟩   für alle t
```

Daher kann die Paarung nur bei λ + μ = 0 von null verschieden sein. Der Zeuge muss also das **entgegengesetzte Gewicht** tragen:

```
z ∈ C_{4,-λ}(B₃^mod, M^∨)
```

> **Ein BC-invarianter Zeuge vom Gewicht 0 annihiliert typischerweise eine geladene Klasse.**

Eine gewöhnliche invariante Spur allein genügt daher **nicht**. Entweder tragen die eingesetzten Kettenelemente das Gesamtgewicht −λ, oder es wird ein entsprechend gewichtetes bzw. verdrehtes Funktional benötigt.

---

## Atomare Struktur von NEU-177

| Knoten | Inhalt |
|---|---|
| [O-177-1] | Explizite vollständige Formel für L_{3,λ}(a₁,a₂,a₃,a₄) |
| [O-177-2] | b L_{3,λ} = 0 |
| [O-177-3] | M^∨ und C_•(B₃^mod, M^∨) definieren |
| [O-177-4] | ⟨bψ, z⟩ = ⟨ψ, ∂z⟩ beweisen |
| [O-177-5] | ∃ z_{−λ}: ∂z_{−λ} = 0 |
| [O-177-6] | ⟨L_{3,λ}, z_{−λ}⟩ ≠ 0 |
| [O-177-7] | [L_{3,λ}] ≠ 0 in H⁴(C^•_{fin,λ}) |

### Status

Alle sieben Knoten sind zum Zeitpunkt dieses Dokuments **?[O]** — dies ist ein Konstruktionsprogramm, keine abgeschlossene Beweiskette. Das Dokument legt die notwendige Typstruktur (M^∨, Kettenkomplex, Adjungiertheit, Gewichtsbedingung) fest, ohne die Existenz eines konkreten z_{−λ} bereits zu behaupten.

### Schlusskette (bei Erfolg aller Knoten)

```
bL_{3,λ} = 0,
∂z_{−λ} = 0,
⟨L_{3,λ}, z_{−λ}⟩ ≠ 0
⟹ L_{3,λ} ∉ im b
⟹ [L_{3,λ}] ≠ 0
```

---

## Alternative algebraische Form

Falls der vollständige Kettenkomplex unnötig schwer wird, genügt algebraisch auch ein Funktional

```
τ_λ ∈ (C^4_{fin,λ})^∨
```

mit

```
τ_λ ∘ b = 0  auf C³_{fin,λ},   τ_λ(L_{3,λ}) ≠ 0
```

Das beweist ebenfalls den Nicht-Korand-Status. Diese Variante ist jedoch **weniger strukturell**: Die Konstruktion eines solchen Separators ist praktisch bereits äquivalent zur direkten Lösung von [O-176-3]. Der gewichtete Dualzyklus über M^∨ und den Kettenkomplex liefert deshalb den informativeren, strukturell verankerten Weg und wird in diesem Dokument als Hauptroute geführt.

---

## DAG-Knotenübersicht (konsolidiert)

| Knoten | Inhalt | Status |
|---|---|---|
| [O-176-1] | ∃ λ≠0, L_{3,λ} ∈ C⁴_{fin,λ} | ✓[K] \| [H-176-1] |
| [O-177-1] | Explizite Formel für L_{3,λ} | ?[O] |
| [O-177-2] | bL_{3,λ} = 0 | ?[O] |
| [O-177-3] | M^∨, C_•(B₃^mod,M^∨) definiert | ?[O] |
| [O-177-4] | ⟨bψ,z⟩ = ⟨ψ,∂z⟩ | ?[O] |
| [O-177-5] | ∃ z_{−λ}: ∂z_{−λ}=0 | ?[O] |
| [O-177-6] | ⟨L_{3,λ}, z_{−λ}⟩ ≠ 0 | ?[O] |
| [O-177-7] | [L_{3,λ}] ≠ 0 | ?[O], impliziert durch 177-2,5,6 |

---

## Ausblick: NEU-178

Erst nach erfolgreichem Abschluss von NEU-177 (insbesondere [O-177-7]) wird die Kette

```
[L₃^mod]_ch ≠ 0 ⟶ ρ_op(L₃^mod)
```

freigeschaltet. Die Operatorrealisierung ρ_op: Z⁴(B₃,M) → End(H) bleibt Gegenstand von **NEU-178** und wird hier nicht vorgezogen.
