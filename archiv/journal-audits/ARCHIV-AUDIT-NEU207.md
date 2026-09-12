# Direktaudit NEU-207 — Bewertungsgitter, Primschalentransport und Ketten-No-go

**Gesamtstatus: ✓[M]_part**

---

## Kernbefunde

### Belastbare Resultate

| Knoten | Aussage | Status |
|---|---|---|
| [O-207-1] | Exakt transportgeschlossene totale Teilbarkeitskette für ≥2 Primrichtungen unmöglich | ✓[M]_neg |
| [O-207-2] | Bewertungsgitter Λ=ℕ₀^(𝒫) als exakter Transportindex | ✓[M] |
| [O-207-3a] | Primschalen q_{p,a}: exakte Transportformeln | ✓[M] |
| [O-207-3b] | Rechteckschalen Q_{F,α}: exakte Transportformeln bei festem F | ✓[M] |
| [O-207-partition] | Endliche gesättigte Gitterpartitionen | ✓[M] |
| [O-207-4a] | Charakterkerne als obere Mengen auf exakten Rechteckschalen | ✓[M] |
| [O-207-4b] | Charakterkernkontrolle auf Tailatomen | ✓[K/M] |
| [O-207-5a-fixed] | c(α)=log(2+|α|₁): unbeschränkt und auf festem Gitter translationsflach | ✓[M] |

### Widerlegte Resultate

| Knoten | Aussage | Status |
|---|---|---|
| [O-207-5a-ref] | Radiale Funktion unter F↑𝒫 refinementstabil | ✓[M]_neg |
| [O-207-5b-radial] | Radiale gesättigte Architektur besitzt normstabile Randterme | ✓[M]_neg |

### Offene Knoten

| Knoten | Aussage | Status |
|---|---|---|
| [O-207-5b-general] | Alternative Koeffizientenarchitektur mit Tail- und Refinementkontrolle | ?[O] |
| [O-207-5c-analytic] | Geladene äußere Derivation A_alg→A_C* | ?[O] |
| [O-207-5c-algebraic] | Geladene äußere Derivation A_alg→A_alg | ?[O] |
| [O-207-HH4] | Cup-Aufstieg und geladener Dualzyklus | ?[O] |
| [O-207-op] | Operator-/Weil-Form-Brücke | ✓[M]_neg,Quelle |

---

## Ersetzte Aussagen

1. **[O-207-2]** war `✓[K]` → korrigiert zu `✓[M]`.
2. **[O-207-5a]** aufgespalten in `[O-207-5a-fixed] ✓[M]` und `[O-207-5a-ref] ✓[M]_neg`.
3. **Strukturbehauptung §207.E/F** (`neuer Flaschenhals = nur Randtermkontrolle`) → `×[M]`; korrekt ist: die radiale Koeffizientenarchitektur scheitert bereits an der Refinementstabilität.
4. **Geladener Grenzknoten** aufgespalten in `[O-207-5c-analytic]` und `[O-207-5c-algebraic]`.

---

## Beitrag zu Objekt X

- Die korrekte Indexgeometrie ist das endliche Bewertungsgitter, nicht eine totale Teilbarkeitskette.
- Exakte Transportformeln für Prim- und Rechteckschalen sind belastbar.
- Charakterkerne als obere Mengen im selben Gitter sind belastbar.
- Die radiale Koeffizientenfunktion `log(2+|α|₁` scheitert beim Übergang zu wachsenden Primzahlmengen (durch NEU-208 nachgewiesen).
- Der allgemeine Koeffizientenknoten bleibt offen.

**Nächster Auditknoten:** NEU-208 — Separierbare Primpotentiale und Refinementstabilität
