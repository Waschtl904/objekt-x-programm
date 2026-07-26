# NEU-58 — Skalenbilanz-Lemma und Obstruktionssatz

**Status:** Gesicherter Obstruktionssatz ✗[M] für Weg A; Weg B strukturell erzwungen ✓[M]  
**Datum:** 2026-06-29  
**Aufbaut auf:** NEU-56 (γ_N-Widerlegung), NEU-57 (singuläre Werte, Weg-B-Formulierung)

---

## Kontext und Fragestellung

Aus NEU-56 ist bekannt: Ein skalares γ_N, das gleichzeitig
- **Kommutator-Schur** (Nelson-Beschränktheit) und
- **Konfinement** (kompakter Resolvent über L-Abschätzung)

kontrolliert, existiert nicht. NEU-58 präzisiert **warum** durch explizite Berechnung der
Skalenverhältnisse A_N und B_N aus der Θ_N-Matrixstruktur.

---

## Schritt 1: Δ_N(a,n) aus der Θ_N-Geometrie

Basisindex: `a = (p, m, r, u)`, Zielindex unter Θ_N: `b = (p', m, r+n, u')` mit `n | m`.

Nelson-Energiefunktional:
```
ℓ(a) ≍ 1 + |r|·log(2+m) + |u|·log(p) + Ω(m)
```

Da m bei der Transition konstant bleibt, fallen Ω(m)-Terme und log(2+m)-Koeffizienten
**nicht** heraus beim Differenzieren:

```
Δ_N(a,n) := |ℓ(b) - ℓ(a)| ≍ |r+n|·log(2+m) - |r|·log(2+m) = n·log(2+m)
```

**Ergebnis:** Δ_N(a,n) ~ n·log(m) ✓[M]

Dies bestätigt GPTs Annahme (NEU-58-Vorbesprechung) und ist der entscheidende Eingabewert
für die B_N-Berechnung.

---

## Schritt 2: A_N^basis — Konfinement-Skala

Mit |Θ̃_ba| ≍ |r|·log(n) (unrenormiert, γ_N = 1):

```
‖J̃_N⁻ η_a‖² = Σ_{n|m} |Θ̃_ba|² ≍ r²·Σ_{n|m} log²(n)
```

Daher:
```
A_N^basis = inf_a  ‖J̃_N⁻ η_a‖ / ℓ(a)
           ≍ inf_a  |r|·(Σ_{n|m} log²n)^{1/2} / (|r|·log m)
           = inf_a  (Σ_{n|m} log²n)^{1/2} / log(m)
```

**Infimum wird an Primzahlen angenommen:** Für m = p prim gilt
```
Σ_{n|p} log²n = log²(1) + log²(p) = log²(p) = log²(m)
```
also:
```
A_N^basis|_{m=p} = log(m)/log(m) = 1
```

**Ergebnis:**
```
A_N^basis ≍ 1     (auf dem N-effektiven Sektor: m ≥ 2, m ≤ N, r ≠ 0)
```
✓[M]

**Hinweis:** Triviale Randfälle m=1 sind vom N-effektiven Sektor auszuschließen, da dort
kein nichttrivialer Divisor beiträgt (A_N = 0 wäre artifiziell).

---

## Schritt 3: B_N^basis — Kommutator-Schur-Skala

Mit Δ_N(a,n) ≍ n·log(m) und |Θ̃_ba| ≍ |r|·log(n):

```
B_N^basis ≍ sup_a  (1/ℓ(a))·Σ_{n|m} |ℓ(b)-ℓ(a)|·|r|·log(n)
           ≍ sup_{m≤N}  (1/(|r|·log m))·Σ_{n|m} n·log(m)·|r|·log(n)
           = sup_{m≤N}  Σ_{n|m} n·log(n)
```

Das log(m) und |r| **kürzen sich vollständig heraus** — B_N ist unabhängig von r. ✓[M]

### Schranken für Σ_{n|m} n·log(n)

**Untere Schranke** (Top-Divisor n=m, m=p Primzahl nahe N):
```
Σ_{n|p} n·log(n) = p·log(p)  →  B_N ≥ c·N·log(N)
```

**Obere Schranke** (via σ₁-Maximalordnung):
```
Σ_{n|m} n·log(n) ≤ log(m)·Σ_{n|m} n = log(m)·σ₁(m)
```
Mit der klassischen Maximalordnung σ₁(m) = O(m·log(log(m))):
```
Σ_{n|m} n·log(n) ≤ C·m·log(m)·log(log(m))
```

**Ergebnis:**
```
N·log(N)  ≲  B_N^basis  ≲  N·log(N)·log(log(N))
```
Oder kompakt:
```
B_N^basis = N·log(N)·(log(log(N)))^{O(1)}
```
✓[M] / ⚠[M] (Untere Schranke gesichert; exakte Maximalordnung bis log(log(N))-Faktor offen)

---

## Satz NEU-58.1 — Skalenbilanz-Obstruktion ✗[M]

**Voraussetzungen:**
- |Θ̃_ba^(N)| ≍ |r|·log(n) für n|m (aus gesichertem Θ_N-Kontext)
- ℓ(a) ≍ |r|·log(2+m) (Nelson-Energiefunktional)
- Δ_N(a,n) ≍ n·log(m) (Schritt 1)

**Behauptung:**

Auf dem N-effektiven Sektor (m ≥ 2, m ≤ N, r ≠ 0) gilt:

```
A_N^basis ≍ 1
B_N^basis ≳ N·log(N)
B_N^basis / A_N^basis ≳ N·log(N) → ∞
```

**Folgerung:** Es existiert kein skalarer Parameter γ_N, der gleichzeitig erfüllt:
```
γ_N · A_N ≳ c > 0    (Konfinement-Bedingung)
γ_N · B_N ≲ C < ∞   (Nelson/Kommutator-Schur-Bedingung)
```

**Beweis der Unmöglichkeit:**

Aus A_N ≍ 1 und der Konfinement-Bedingung folgt γ_N ≳ c > 0.
Dann gilt γ_N · B_N ≳ c · N·log(N) → ∞. Widerspruch zur Kommutator-Schur-Bedingung. □

**Korollar:** Die Wahl γ_N = C/log(N) ist nicht nur unzureichend, sondern exemplarisch
für die allgemeine Unmöglichkeit: jede Wahl γ_N → 0 verletzt Konfinement, jede Wahl
γ_N ≳ c verletzt den Nelson-Kommutator. ✗[M]

---

## Satz NEU-58.2 — Weg B ist strukturell erzwungen ✓[M]

Da Weg A (kompakter Resolvent über Nelson-Konfinement mit skalarem γ_N) durch
NEU-58.1 ausgeschlossen ist, ist der einzig verbleibende Weg:

```
Selbstadjungiertheit von D_rel (braucht nur J⁻ ≲ L, nicht Konfinement)
    ↓
Spektralsatz: Spec(D_rel) ⊂ ℝ
    ↓
RH-Hinrichtung: Spec(lim A_N^{Jac,-}) ⊂ ℝ   (via Spektralmaß/Jacobi-Limes, Weg B)
```

Die RH-Hinrichtung ist vollständig formulierbar ohne kompakten Resolvent. ✓[M]

---

## Offene Punkte ❓[O]

1. **Operatorielle elliptische Untergrenze:** Der basisweise Befund
   `‖J̃_N⁻ η_a‖ ≍ ℓ(a)` ist noch keine elliptische Operatorabschätzung.
   Möbius-artige destruktive Interferenzen bei linearen Kombinationen können
   ```
   inf_{ξ ⊥ ker J_N⁻} ‖J_N⁻ ξ‖ / ‖Lξ‖
   ```
   unter die Basisnorm drücken. Für die **Obstruktion** irrelevant (kommt von B_N),
   aber für eine eventuelle zukünftige Weg-A-Variante mit anderem Vergleichsoperator
   weiterhin offen.

2. **Spektral-Limes-Topologie:** Der Schritt A_N^{Jac,-} → D_rel braucht eine
   präzise Operatortopologie-Spezifikation (Norm-Resolventenkonvergenz oder schwächeres).
   Literatur: Kato, *Perturbation Theory*, Thm. VIII.1.5.

3. **Exakte Maximalordnung von B_N:** Die Frage ob
   `B_N ≍ N·log(N)` oder `B_N ≍ N·log(N)·log(log(N))`
   ist für die Obstruktion irrelevant, aber für eine präzise Spektraltheorie
   (z.B. Zählung der Nullstellen) möglicherweise wichtig. ⚠[M]

---

## Statusübersicht

| Größe | Wert | Status |
|---|---|---|
| Δ_N(a,n) | ~ n·log(m) | ✓[M] |
| A_N^basis | ≍ 1 | ✓[M] |
| B_N^basis | ≳ N·log(N), wahrscheinlich N·log(N)·log(log(N)) | ✓[M]/⚠[M] |
| B_N/A_N → ∞ | ja, mindestens ≳ N·log(N) | ✓[M] |
| Kein skalares γ_N für Weg A | Obstruktion gesichert | ✗[M] |
| Operatorielle elliptische Untergrenze | offen (Interferenz) | ❓[O] |
| Spektral-Limes-Topologie | offen | ❓[O] |
| Weg B strukturell erzwungen | ja | ✓[M] |

---

## Literatur

- Reed, M. & Simon, B.: *Methods of Modern Mathematical Physics*, Bd. I–IV (Academic Press)
- Simon, B.: *Trace Ideals and Their Applications*, 2. Aufl., AMS (2005)
- Kato, T.: *Perturbation Theory for Linear Operators*, Springer (1995)
- Nelson, E.: *Analytic vectors*, Ann. Math. 70 (1959), 572–615
- Hardy, G.H. & Wright, E.M.: *An Introduction to the Theory of Numbers* (σ₁-Maximalordnung)
