# NEU-59 — Jacobi-Limes und Spektralmaß-Topologie

**Status:** Weg-B-Architektur, Kerngerüst ⚠[M]; Arithmetische Identifikation ❓[O]  
**Datum:** 2026-06-29 (korrigiert nach GPT-Präzisierung)  
**Aufbaut auf:** NEU-58 (Weg A strukturell ausgeschlossen), NEU-57 (Selbstadjungiertheit)

---

## Programmwechsel

Nach NEU-58 ist der Nelson-Konfinement-Weg (Weg A) strukturell geschlossen:
```
(J_N^-)^* J_N^- + 1 ≥ c² L²    ← nicht mehr Ziel
```
Der neue Hauptpfad (Weg B) operiert mit:
```
m_{a,b}^(N)(z) := ⟨η_a, (A_N^{Jac,-} - z)^{-1} η_b⟩    (Weyl-/Stieltjes-Funktionen)
```
**Nicht das Spektrum direkt konvergieren lassen, sondern die Weyl-/Stieltjes-Funktionen.**

---

## Korrektur 1: Norm-Resolventenkonvergenz

Die Aussage aus der ursprünglichen NEU-59-Version muss präzisiert werden:

> ~~Norm-Resolventen-Konvergenz ist nach NEU-58 nicht erreichbar~~

**Korrekte Formulierung:** ✓[M]
```
Norm-Resolventenkonvergenz der finite-rank Trunkierungen A_N^{Jac,-}
→ D_rel ist ausgeschlossen.
```

**Begründung:** Die A_N^{Jac,-} sind endlich-rangige (finite-rank) Jacobi-Trunkierungen,
also hat (A_N - z)^{-1} endlichen Rang und ist insbesondere kompakt. Ein
Operatornorm-Limes kompakter Operatoren ist wieder kompakt (Reed–Simon I, Thm. VI.12).
Also wäre (D_rel - z)^{-1} kompakt — genau das hat NEU-58 strukturell ausgeschlossen.

**Einschränkung:** Diese Aussage gilt spezifisch für die finite-rank Einbettungsstrategie.
Andere Approximationsstrategien (nicht-finite-rank) sind nicht ausgeschlossen, aber
auch nicht im aktuellen Programmrahmen definiert. ⚠[M]

---

## Korrektur 2: Spektralinklusion

Der Schritt
```
Spec(lim A_N) ⊂ Spec(D_rel) ⊂ ℝ
```
ist in dieser Globalform **nicht** aus bloßer schwacher Spektralmaßkonvergenz ableitbar.

**Korrekte Aussage:** ✓[M]

Aus μ_{N,ξ,η} ⇒ μ_{ξ,η} folgt zunächst nur:
```
supp(μ_ξ) ⊂ Spec(D_rel)    für jeden Testvektor ξ ∈ D_test.
```

Um daraus die **volle** Spektralinformation zu gewinnen, braucht man zusätzlich:
```
Zyklizitäts-/Totalitätsbedingung:
  span{ f(D_rel)ξ : ξ ∈ D_test, f ∈ C_c(ℝ) }  dicht in H.
```
Ohne diese Bedingung sieht Weg B nur einen Spektralanteil — die Grenzmaße könnten
einen echten Teilraum von Spec(D_rel) abdecken. ❓[O]

---

## Topologie-Hierarchie

```
(1) Norm-Resolvent:      ‖(A_N-z)^{-1} - (D_rel-z)^{-1}‖ → 0
       ↓ (impliziert)
(2) Starke Resolvent:    ‖(A_N-z)^{-1}ξ - (D_rel-z)^{-1}ξ‖ → 0  ∀ξ ∈ H
       ↓ (impliziert)
(3) Schwach auf D_test:  ⟨ξ,(A_N-z)^{-1}η⟩ → ⟨ξ,(D_rel-z)^{-1}η⟩
       ↓ (via Stieltjes-Inversion)
(4) Vage Spektralmaße:   μ_{N,ξ,η} ⇒ μ_{ξ,η}
```

(1) ist ausgeschlossen (finite-rank Argument, NEU-58). ✗[M]  
(2) ist das Ziel, erfordert Core-Konvergenz + Range-Dichte (→ NEU-60). ❓[O]  
(3)/(4) folgen aus (2) via Herglotz/Stieltjes. ✓[M] (abstrakt)

---

## Satz NEU-59.1 — Spektralmaß-Reduktion (präzisiert) ⚠[M]

**Voraussetzungen:**
- A_N^{Jac,-} selbstadjungierte finite-rank Jacobi-Trunkierungen
- D_rel selbstadjungiert auf H_rel^eff
- Für alle ξ, η ∈ D_test gilt:
  `⟨ξ, (A_N - z)^{-1} η⟩ → ⟨ξ, (D_rel - z)^{-1} η⟩` für alle z ∈ ℂ\ℝ

**Schlussfolgerung:**
```
μ_{N,ξ,η} ⇒ μ_{ξ,η}    (vage Konvergenz)
supp(μ_ξ) ⊂ Spec(D_rel) ⊂ ℝ
```

**Vollständige Spektralrekonstruktion** zusätzlich falls D_test spektral total/zyklisch. ❓[O]

**Literatur:**
- Reed–Simon Bd. I, Thm. VIII.20 (Spektralsatz + Stieltjes-Inversion)
- Simon, *Szegő's Theorem and Its Descendants*, AMS 2011, Thm. 2.3.3
- Kato, *Perturbation Theory*, §VIII.1

---

## Aktualisierte Weg-B-Architektur

```
[1]  J⁻ ≲ L (Form-Schranke)                                    ✓[M]
          ↓
[2]  D_rel selbstadjungiert, Spec(D_rel) ⊂ ℝ                   ✓[M]
          ↓
[3]  A_N^{Jac,-} ξ → D_rel ξ auf gemeinsamem Kern              ❓[O]  → NEU-60
          ↓
[4]  Range-/Core-Dichte: (D_rel - z) D_test dicht in H          ❓[O]  → NEU-60
          ↓
[5]  Schwache/starke Resolventenkonvergenz auf D_test            ❓[O]  → NEU-60
          ↓
[6]  μ_{N,ξ,η} ⇒ μ_{ξ,η}  (via Stieltjes-Inversion)           ⚠[M]
          ↓
[7]  D_test spektral total/zyklisch                              ❓[O]
          ↓
[8]  Arithmetische Identifikation: Spec(D_rel) ↔ Nullstellen ζ  ❓[O]
          ↓
[9]  RH-Kriterium                                                ❓[O]
```

Schritte [1]–[2]: gesichert ✓[M]  
Schritte [3]–[5]: Kern von NEU-60 ❓[O]  
Schritte [6]: abstrakt gesichert, konkret von NEU-60 abhängig ⚠[M]  
Schritte [7]–[9]: offen ❓[O]

---

## Status NEU-59

| Objekt | Status |
|---|---|
| Norm-Resolvent (finite-rank) ausgeschlossen | ✓[M] |
| D_rel selbstadjungiert, Spec ⊂ ℝ | ✓[M] |
| Topologie-Hierarchie (abstrakt) | ✓[M] |
| Stieltjes-Reduktion (NEU-59.1) | ⚠[M] |
| supp(μ_ξ) ⊂ Spec(D_rel) | ✓[M] |
| Zyklizitäts-/Totalitätsbedingung D_test | ❓[O] |
| Core-Konvergenz A_N ξ → D_rel ξ | ❓[O] → NEU-60 |
| Arithmetische Identifikation | ❓[O] |

---

## Literatur

- Reed, M. & Simon, B.: *Methods of Modern Mathematical Physics*, Bd. I, Thm. VI.12, VIII.20
- Kato, T.: *Perturbation Theory for Linear Operators*, Springer 1995, §VIII.1
- Simon, B.: *Szegő's Theorem and Its Descendants*, AMS 2011, Kap. 2
- Simon, B.: *Trace Ideals and Their Applications*, AMS 2005
- Connes, A.: *Trace formula in noncommutative geometry*, Selecta Math. 5 (1999)
