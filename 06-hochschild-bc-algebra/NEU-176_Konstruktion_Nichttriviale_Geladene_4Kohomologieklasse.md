# NEU-176 — Konstruktion einer nichttrivialen geladenen 4-Kohomologieklasse

## Vorbemerkung: Drei Reichweitenpräzisierungen zu NEU-175

### R1 — Die Konstruktion in NEU-175 gilt modulweise getrennt

Für das reguläre Bimodul M_untw = B₃^mod ist die induzierte Zeitwirkung unmittelbar kompatibel, sofern α_t eine Algebraautomorphismengruppe ist. Für M_σ = _id B_{3,σ} bleibt [O-174-4σ]: α_tσ = σα_t hingegen offen. Die Statusaussagen von NEU-175 werden daher getrennt:

```
[O-175-1–5]_untw   ✓[K]
[O-175-1–5]_σ      ✓[K] | [O-174-4σ]     (bedingt auf ungelöstem Unterknoten)
```

Alle Konstruktionen dieses Dokuments (NEU-176) werden — sofern nicht anders vermerkt — für das **unverdrehte Modul M_untw** durchgeführt, um die Abhängigkeit von [O-174-4σ] zu vermeiden. Eine Ausdehnung auf M_σ bleibt an [O-174-4σ] gekoppelt.

### R2 — Eindeutigkeit der Gewichtszerlegung als Definitionsbestandteil

Damit P_λ und P^ch = Σ_{λ≠0} P_λ wirklich wohldefiniert sind, muss jedes Element von C_fin• eine **eindeutige** endliche Darstellung φ = Σ_{λ∈F} φ_λ, φ_λ ∈ C^•_λ, besitzen.

**Beweis der Eindeutigkeit:** Seien λ₁, …, λ_r paarweise verschieden und Σ_{j=1}^r e^{itλ_j}φ_j = 0 für alle t ∈ R. Die Funktionen t ↦ e^{itλ_j} sind als Charaktere der Gruppe (R, +) linear unabhängig (Vandermonde-Argument bzw. Eindeutigkeit der Fourier-Exponentialentwicklung fastperiodischer Funktionen). Also folgt φ_j = 0 für alle j.

Damit ist

```
C_fin^• = ⊕^alg_{λ∈R} C_λ^•
```

eine echte algebraische direkte Summe (nicht nur eine lineare Hülle). Dieser Punkt gilt als Ergänzung zu NEU-175 hiermit als geschlossen: **✓[K]**.

### R3 — [P^ch] existiert, aber Nichtverschwinden ist nicht automatisch

Aus NEU-175 folgt die wohldefinierte Abbildung [P^ch]: H•(C_fin) → H•(C_fin). Daraus folgt jedoch **nicht** im[P^ch] ≠ 0, und erst recht nicht [P^ch]([L₃]) ≠ 0 für ein beliebiges L₃. Es könnte z.B. jeder geladene Kozykel ein Rand sein: Z⁴_λ = bC³_λ für alle λ ≠ 0.

Die präzise Zerlegung lautet:

```
H^n(C_fin) ≅ ⊕^alg_λ H^n(C_λ^•)
```

wobei [P^ch] die Summe der Komponenten mit λ ≠ 0 projiziert. Offen bleibt, ob mindestens eine Komponente im Grad 4 nichttrivial ist — genau dies ist der Gegenstand dieses Dokuments.

---

## Ziel von NEU-176

Der nächste Knoten ist **nicht** ρ_op. Noch fehlt überhaupt eine konkrete geladene Kohomologieklasse, die realisiert werden könnte. NEU-176 konstruiert daher zuerst einen Kandidaten und entscheidet, ob er eine nichttriviale Klasse definiert.

---

## Atomare Knoten

### [O-176-1] — Existenz eines geladenen 4-Kozykel-Kandidaten

> ∃ λ ≠ 0, L_{3,λ} ∈ C^4_{fin,λ}

**Konstruktion:** Wir wählen ein konkretes λ ≠ 0 und definieren L_{3,λ} ∈ C^4(B₃^mod, M_untw) als multilineare Abbildung

```
L_{3,λ}(a₁, a₂, a₃, a₄) := Σ_k c_k · f_k(a₁)f_k(a₂)f_k(a₃)f_k(a₄)
```

wobei f_k Eigenvektoren der dualen Wirkung α_{-t} auf B₃^mod* mit passenden Eigenwerten sind, so gewählt, dass α_t^C L_{3,λ} = e^{itλ}L_{3,λ} gilt (Gewichtsadditivität λ = λ₁+λ₂+λ₃+λ₄ der Faktoren).

**Status:** ✓[K] — Existenz ist konstruktiv sichergestellt, sofern B₃^mod nichttriviale Eigenvektoren zu mindestens vier (nicht notwendig verschiedenen) von-Null-verschiedenen Gewichten besitzt, die sich zu λ ≠ 0 summieren. Dies ist eine Modellannahme über B₃^mod = A_Q, die explizit zu verifizieren bleibt: **[O-176-1a] ?[O]**: Besitzt A_Q genügend viele α_t-Eigenvektoren zu nichttrivialen Gewichten?

### [O-176-2] — Kozykelbedingung

> b L_{3,λ} = 0

**Vorgehen:** Direkte Berechnung von (bL_{3,λ})(a₁,…,a₅) mittels der Hochschild-Formel aus NEU-174.C. Für die spezielle Produktform aus [O-176-1] muss die Summe der fünf Terme (einer Randterm, drei innere Multiplikationsterme, ein weiterer Randterm) explizit verschwinden. Dies ist im Allgemeinen eine **nichttriviale algebraische Bedingung** an die Koeffizienten c_k und die Wahl der f_k — sie folgt nicht automatisch aus der Gewichtseigenschaft allein.

**Status:** ?[O] — abhängig von einer expliziten Wahl der f_k und c_k, die diese Kozykelbedingung erfüllt. Dies ist der erste substantielle Konstruktionsschritt, der über die reine Gewichtsbuchhaltung hinausgeht.

### [O-176-3] — Der kritische Punkt: Nichtrandbedingung

> L_{3,λ} ∉ b C^3_{fin,λ}

Dies ist der **mathematisch belastende** Punkt: der Nachweis, dass der konstruierte Kozykel kein Korand ist.

**Strategie:** Ein Standardansatz ist die Konstruktion eines dualen Zeugen — eines linearen Funktionals τ: C^4_{fin,λ} → C mit τ(bC^3_{fin,λ}) = 0, aber τ(L_{3,λ}) ≠ 0. Ein solches τ kann etwa aus einer Spurform oder einem geeigneten Paarungsintegral (falls B₃^mod eine Spurfunktion trägt) gewonnen werden. Ohne konkrete Spurstruktur auf A_Q bleibt dieser Nachweis offen.

**Status:** ?[O] — dies ist der zentrale unbewiesene Knoten dieses Dokuments. Weder aus [O-176-1] noch aus [O-176-2] folgt die Nichtrandbedingung automatisch.

### [O-176-4] — Nichttrivialität der Kohomologieklasse

> [L_{3,λ}] ≠ 0 in H⁴(C_{fin,λ})

Dies ist äquivalent zu [O-176-2] ∧ [O-176-3] (Kozykel, der kein Korand ist, definiert per Definition eine nichttriviale Klasse).

**Status:** ?[O] — abhängig vom Abschluss von [O-176-2] und [O-176-3].

### [O-176-5] — Erhaltung unter P^ch

> [P^ch]([L_{3,λ}]) = [L_{3,λ}] ≠ 0

**Beweis (bedingt):** Da λ ≠ 0 nach Konstruktion, projiziert P^ch = Σ_{μ≠0}P_μ die Klasse [L_{3,λ}] ∈ H⁴(C_{fin,λ}) unverändert auf sich selbst (P_λ wirkt als Identität auf dem λ-Summanden, alle anderen P_μ mit μ≠λ annullieren ihn). Damit ist [O-176-5] eine **direkte Konsequenz** von [O-176-4] und der Gewichtszerlegung aus R2, sofern [O-176-4] gilt.

**Status:** ✓[K] | [O-176-4] — bedingt auf dem Abschluss des vorangehenden Knotens.

---

## DAG-Knotenübersicht

| Knoten | Inhalt | Status |
|---|---|---|
| [O-176-1] | ∃ λ≠0, L_{3,λ} ∈ C⁴_{fin,λ} | ✓[K] (unter Modellannahme [O-176-1a]) |
| [O-176-1a] | Besitzt A_Q genügend Eigenvektoren zu nichttrivialen Gewichten? | ?[O] |
| [O-176-2] | b L_{3,λ} = 0 | ?[O] |
| [O-176-3] | L_{3,λ} ∉ bC³_{fin,λ} | ?[O] — zentraler unbewiesener Knoten |
| [O-176-4] | [L_{3,λ}] ≠ 0 in H⁴(C_{fin,λ}) | ?[O] (≡ [O-176-2]∧[O-176-3]) |
| [O-176-5] | [P^ch]([L_{3,λ}]) = [L_{3,λ}] ≠ 0 | ✓[K] \| [O-176-4] |

---

## Herkunftsstatus des neuen L₃

Auch bei erfolgreichem Abschluss aller Knoten muss zwischen zwei Objekten unterschieden werden:

```
[L₃^mod] ∈ H⁴(C_fin)     versus     [L₃^orig]  (historisch postulierte Klasse)
```

Ein erfolgreich konstruierter geladener Modellkozykel beweist zunächst nur:

```
∃ [L₃^mod]_ch ≠ 0
```

aber **nicht**:

```
[L₃^mod] = [L₃^orig]
```

Der Vergleichsknoten bleibt offen:

> **[O-176-orig]** ?[O]: Realisiert die Modellklasse das ursprüngliche Objekt-X-Datum?

Dieser Knoten ist strukturell analog zu [O-174-1c] (Herkunftstreue von B₃^mod) und wird nicht in NEU-176 entschieden.

---

## Korrigierte Folgearchitektur

```
B₃^mod ⟶ (C_fin^•, b) ⟶ [P^ch]
        ⟶ [L₃^mod]_ch ≠ 0 ⟶ ρ_op(L₃^mod) ⟶ C_L, P^ch(L₃^op)
```

Die Operatorrealisierung ρ_op wird auf **NEU-177** verschoben. NEU-176 muss zuerst entscheiden, ob der neu gebaute Komplex überhaupt eine nichttriviale geladene Klasse im relevanten Grad 4 trägt — diese Entscheidung ist mit [O-176-3] noch nicht gefallen.

---

## Offene Fragen (Zusammenfassung)

| Frage | Status |
|---|---|
| Ausdehnung auf verdrehtes Modul M_σ | ?[O] (gekoppelt an [O-174-4σ]) |
| Besitzt A_Q genügend Eigenvektoren zu nichttrivialen Gewichten? | ?[O] |
| Ist L_{3,λ} tatsächlich ein Kozykel? | ?[O] |
| Ist L_{3,λ} kein Korand? | ?[O] — zentrale offene Frage |
| Realisiert [L₃^mod] das ursprüngliche Objekt-X-Datum? | ?[O] |
