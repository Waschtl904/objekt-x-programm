# Direktaudit NEU-207 — Bewertungsgitter, Primschalentransport und Ketten-No-go

**Gesamtstatus:** `✓[M]_part`

---

## 1. Auditumfang

Geprüft: NEU-207 vollständig; Transportformeln und Charakterkernschalen aus NEU-206; dyadische Vergleichskonstruktion aus NEU-204; NEU-208 hinsichtlich seiner Revisionsaussage zu [O-207-5a/5b]; aktuelle Ordnerliste.

---

## 2. Kernergebnis

NEU-207 ersetzt die eindimensionale Teilbarkeitskette durch das Bewertungsgitter
$$\Lambda = \mathbb{N}_0^{(\mathcal{P})}$$
und beweist exakte Transportformeln für Prim- und Rechteckschalen. Der anschließende Vorschlag $c(\alpha)=\log(2+|\alpha|_1)$ ist auf jedem festen endlichen Gitter translationsflach, aber **nicht stabil**, wenn neue Primkoordinaten hinzukommen. Dieser Fehler wird in NEU-208 nachgewiesen.

---

## 3. DAG-Knoten

| Knoten | Aussage | Status |
|---|---|---|
| [O-207-1] | Exakt transportgeschlossene totale Teilbarkeitskette für ≥2 Primrichtungen | `✓[M]_neg` |
| [O-207-2] | Bewertungsgitter Λ als exakter Transportindex | `✓[M]` |
| [O-207-3a] | Primschalen q_{p,a}: exakte Transportformeln | `✓[M]` |
| [O-207-3b] | Rechteckschalen Q_{F,α}: exakte Transportformeln bei festem F | `✓[M]` |
| [O-207-partition] | Endliche gesättigte Gitterpartitionen | `✓[M]` |
| [O-207-4a] | Charakterkerne als obere Mengen auf exakten Rechteckschalen | `✓[M]` |
| [O-207-4b] | Charakterkernkontrolle auf Tailatomen | `✓[K/M]` |
| [O-207-5a-fixed] | c(α)=log(2+|α|₁): unbeschränkt und auf festem Gitter translationsflach | `✓[M]` |
| [O-207-5a-ref] | Radiale Funktion unter F↑Primzahlen refinementstabil | `✓[M]_neg` |
| [O-207-5b-radial] | Radiale gesättigte Architektur besitzt normstabile Randterme | `✓[M]_neg` |
| [O-207-5b-general] | Alternative Koeffizientenarchitektur mit Tail- und Refinementkontrolle | `?[O]` |
| [O-207-5c-analytic] | Geladene äußere Derivation A_alg→A_C* | `?[O]` |
| [O-207-5c-algebraic] | Geladene äußere Derivation A_alg→A_alg | `?[O]` |
| [O-207-HH4] | Cup-Aufstieg und geladener Dualzyklus im korrekten Zielmodul | `?[O]` |
| [O-207-op] | Operator-/Weil-Form-Brücke | `✓[M]_neg,Quelle` |

---

## 4. Ersetzte Aussagen

- `[O-207-2] ✓[K]` → `✓[M]`
- `[O-207-5a] ✓[K]` → aufgespalten in `[O-207-5a-fixed] ✓[M]` und `[O-207-5a-ref] ✓[M]_neg`
- „Nur noch die Randtermkontrolle ist offen" → **falsch**; radiale Koeffizientenarchitektur scheitert bereits an Refinementstabilität
- „Direkter Objekt-X-Kandidat bereits nach [O-207-5b]" → `⚠[M]` (programmatisch, nicht mathematisch belastbar)

---

## 5. Beitrag zu Objekt X

Belastbar:
- Korrekte Indexgeometrie: **Bewertungsgitter**, nicht totale Kette
- Exakte Transportformeln für Prim- und Rechteckschalen
- Charakterkerne als obere Mengen im selben Gitter

Nicht tragfähig:
- Behaupteter Abschluss des Koeffizientenproblems
- $c(\alpha)=\log(2+|\alpha|_1)$ scheitert beim Übergang zu wachsenden Primzahlmengen

**Nächster Auditknoten:** NEU-208 — Separierbare Primpotentiale und Refinementstabilität
