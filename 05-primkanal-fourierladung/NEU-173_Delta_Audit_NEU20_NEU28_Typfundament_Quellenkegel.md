# NEU-173 — Delta-Audit NEU-20/NEU-28 und Abschluss des Typfundament-Quellenkegels

## Vorbemerkung: Drei Präzisierungen gegenüber NEU-172

Vor Beginn des eigentlichen Delta-Audits sind drei epistemische und typologische Korrekturen gegenüber dem in NEU-172 festgehaltenen Befund einzuarbeiten.

---

### P1 — Fallkorrektur: Der Quellenbefund entspricht C_src-neg, nicht C₂

Nach der in NEU-171 festgelegten Matrix bezeichnete **C₂** den Fall, dass sämtliche Typfragen lediglich offen bzw. importabhängig bleiben. Der tatsächliche Befund aus NEU-72 und NEU-170b ist stärker:

| Knoten | Quellenbefund NEU-72 / NEU-170b |
|---|---|
| [O-171-1] | ✓[M]_neg |
| [O-171-2] | ✓[M]_neg |
| [O-171-3] | ✓[M]_neg |
| [O-171-5] | ✓[M]_neg |

Für Knoten [O-171-4] ist eine Zweiteilung vorzunehmen:

**[O-171-4-audit]** ✓[M]_neg  
> NEU-72 und NEU-170b bestimmen keinen typisierten Repräsentanten L₃.

**[O-171-4-exist]** ?[O]  
> Lässt sich ein typkorrekter Kochain oder Operator L₃ neu konstruieren?

Diese beiden Teilfragen sind logisch voneinander unabhängig. Der Quellenbefund schließt die erste negativ ab, lässt die zweite jedoch vollständig offen.

**Schlussfolgerung:** Der Gesamtbefund entspricht Fall **C_src-neg** (alle auditierten Quellenknoten negativ geschlossen, Existenzfrage mathematisch offen), nicht C₂.

---

### P2 — Typologische Präzisierung: δ_BC ≠ d ist zu schwach formuliert

Die in NEU-172 verwendete Formulierung „δ_BC ≠ d" unterschätzt den strukturellen Unterschied. Die beiden Abbildungen haben bereits unterschiedliche **Typen**:

```
δ_BC : A_Q → A_Q,   δ_BC(a) = [H, a]       (Algebraableitung)
b    : Cⁿ(B₃, M) → Cⁿ⁺¹(B₃, M)             (Hochschild-Kodifferential)
```

Sie sind als Abbildungen nicht unmittelbar vergleichbar.

**Präziserer Befund:**
> δ_BC ist eine Algebraableitung und kein in NEU-72 definierter Hochschild-Korandoperator.

Um Notationskollisionen zu vermeiden, verwendet NEU-173 (und alle Folgedokumente) **b** statt d für das Hochschild-Kodifferential:

```
(bφ)(a₁, …, a_{n+1})
  = a₁ · φ(a₂, …, a_{n+1})
  + Σᵢ₌₁ⁿ (−1)ⁱ φ(a₁, …, aᵢaᵢ₊₁, …, a_{n+1})
  + (−1)ⁿ⁺¹ φ(a₁, …, aₙ) · a_{n+1}
```

Für dieses **b** gilt die Komplexbedingung b² = 0.

Die BC-Ableitung δ_BC könnte später eine Zeitwirkung oder infinitesimale Gewichtswirkung auf Kochains induzieren, ersetzt b jedoch nicht.

---

### P3 — Titelkorrektur: NEU-173 ist ein Delta-Audit, kein Vollaudit

NEU-20 und NEU-28 wurden in NEU-170c bereits auf die konkrete Konstruktion und Normierung von L₃ auditiert. Ein vollständiger erneuter Audit würde bereits negativ geschlossene Arbeit wiederholen.

NEU-173 prüft daher **ausschließlich** die bislang noch nicht explizit tabellierten Typfragen.

---

## Delta-Audit: NEU-20 und NEU-28

### Auditierte Quellen

- **NEU-20**: Konstruktion und Normierung von L₃ (erste explizite Definition)
- **NEU-28**: Verwendung von L₃ in einer Spurformel für Algebraelemente

### Auditknotenliste [O-173-1] – [O-173-5]

| Knoten | Frage | Erwarteter Befund |
|---|---|---|
| [O-173-1] | Definiert NEU-20 oder NEU-28 eine Algebra B₃? | ✓[M]_neg |
| [O-173-2] | Definiert eine Quelle ein B₃-Bimodul M? | ✓[M]_neg |
| [O-173-3] | Definiert eine Quelle C•(B₃, M) und b? | ✓[M]_neg |
| [O-173-4] | Typisiert eine Quelle L₃ ∈ Z⁴(B₃, M)? | ✓[M]_neg |
| [O-173-5] | Definiert eine Quelle eine Realisierung ρ_op : Z⁴(B₃, M) → A_BC^an oder End(H)? | ✓[M]_neg |

### Begründung zu [O-173-5]

Knoten [O-173-5] ist entscheidend: Selbst ein korrekt definierter Hochschild-Kozykel L₃ ∈ Z⁴(B₃, M) liefert noch nicht die in NEU-28 verwendete Einsetzung a = L₃ in eine Spurformel für Algebraelemente. Dafür wäre eine zusätzliche **Typbrücke**

```
ρ_op : Z⁴(B₃, M) → A_BC^an   oder   ρ_op : Z⁴(B₃, M) → End(H)
```

erforderlich, die in keiner der auditierten Quellen konstruiert wird.

---

## Abschluss des Typfundament-Quellenkegels

### Gesamtergebnis

> **Im Quellenkegel NEU-15–17, NEU-20, NEU-28, NEU-72 und NEU-170b ist kein vollständiges Tupel (B₃, M, C•, b, L₃, ρ_op) konstruiert.**

**Status:**

- ✓[M]_neg — als Quellenbefund (alle sechs Komponenten des Tupels fehlen in allen auditierten Quellen)
- ?[O] — als mathematische Konstruktionsfrage (die Existenz eines typkorrekten L₃ bleibt offen)

### Konsequenz für den Fortgang

Ein weiterer Quellenaudit ist nur bei einer **konkret neu identifizierten Ursprungsquelle** sinnvoll. Andernfalls schließt NEU-173 den Quellenaudit-Zyklus vollständig ab.

---

## Ausblick: NEU-174

NEU-174 setzt erstmals **konstruktiv** an:

**NEU-174 — Minimaler Hochschild-Komplex und induzierte BC-Zeitwirkung**

Schrittfolge:
1. Explizite Festlegung von B₃, M, C•(B₃, M), b
2. Verifikation b² = 0
3. Konstruktion eines Kandidaten L₃ ∈ Z⁴(B₃, M)
4. Definition einer induzierten Zeitwirkung αₜᶜ mit der Kommutierungseigenschaft:

```
b αₜᶜ = αₜᶜ b
```

Damit wird die Grenze zwischen Quellenaudit und neuer mathematischer Konstruktion erstmals vollständig sichtbar.

---

## Statusübersicht

| Phase | Dokument | Status |
|---|---|---|
| Typfundament-Definition | NEU-171 | ✓ abgeschlossen |
| Direktaudit NEU-72 / NEU-170b | NEU-172 | ✓ abgeschlossen |
| Delta-Audit NEU-20 / NEU-28 | NEU-173 (dieses Dokument) | ✓ abgeschlossen |
| Konstruktionsphase | NEU-174 | ?[O] offen |

**Fallbezeichnung des Gesamtbefunds:** C_src-neg  
**Offene mathematische Frage:** ?[O] — Existenz eines typkorrekten Tupels (B₃, M, C•, b, L₃, ρ_op)
