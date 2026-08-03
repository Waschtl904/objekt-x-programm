# Direktaudit NEU-208 — Separierbare Primpotentiale und Refinementstabilität

**Gesamtstatus: ✓[M]_part**

---

## Kernbefunde

### Belastbare Resultate

| Knoten | Aussage | Status |
|---|---|---|
| [O-208-1] | Radiale Funktion log(2+|α|₁) unter Primrefinement nicht normstabil | ✓[M]_neg |
| [O-208-2] | Separierbare Primpotentiale X_{F,N}=Σ_{p∈F} X_{p,N_p} vollständig algebraisch konstruiert | ✓[M] |
| [O-208-3a] | Neue Primrichtung q∤k verändert [X,μ_k] nicht | ✓[M] |
| [O-208-3b] | Entsprechende Stabilität für μ_k* und e(r) | ✓[M] |
| [O-208-4a] | B_{p,a} existiert in B_{C*} mit Norm log((a+2)/2) | ✓[M] |
| [O-208-4b] | \|B_k\| = Σ_{p\|k} log((v_p(k)+2)/2) | ✓[M] |
| [O-208-4c] | D:A_alg→A_{C*} neutrale normunbeschränkte Derivation | ✓[M] |
| [O-208-HH1-analytic] | [D]≠0 in HH¹(A_alg,A_{C*})_1 — stärkster positiver Befund | ✓[M] |

### Widerlegte Resultate

| Knoten | Aussage | Status |
|---|---|---|
| [O-208-4b-old] | Verschiedene Primkanäle orthogonal; Norm von B_k ist Maximum | ×[M] |
| [O-208-algebraic] | D(A_alg)⊂A_alg für den logarithmischen Primkanal | ✓[M]_neg |
| [O-208-5a] | Naiver geladener separierbarer Sandwichansatz μ_m(Σ_p X̃_{p,N_p})μ_n* | ✓[M]_neg |

### Offene Knoten

| Knoten | Aussage | Status |
|---|---|---|
| [O-208-5b] | Gemeinsam lokalisierte geladene Architektur mit separierbaren Differenzen | ?[O] |
| [O-charged-HH1-analytic] | Geladene äußere Klasse in HH¹(A_alg,A_{C*})_g | ?[O] |
| [O-charged-HH1-algebraic] | Geladene äußere Klasse in HH¹(A_alg,A_alg)_g | ?[O] |

---

## Ersetzte Aussagen

1. **[O-208-2]** war `✓[K]` → korrigiert zu `✓[M]`.
2. **Normformel für B_k**: `max_{p|k} log((v_p(k)+2)/2)` → korrekt `Σ_{p|k} log((v_p(k)+2)/2)`; Primkanäle sind nicht orthogonal.
3. **Zieltyp**: unpräzise `"Grenzderivation auf Generatoren"` → `D:A_alg→A_{C*}` mit `[D]≠0 in HH¹(A_alg,A_{C*})_1`.
4. **[O-208-5]** aufgespalten in `[O-208-5a] ✓[M]_neg` (naiver Sandwich) und `[O-208-5b] ?[O]` (allgemeine geladene Kopplung).
5. **Überdehnte Schlussbehauptung** `"einzig verbleibender Schritt"` → `⚠[M]`; nach erfolgreicher Kopplung fehlen weiterhin: Konvergenz der e(r)-Kommutatoren, Nichtinnerheit, HH¹-Klasse, Cup-Aufstieg, Dualzyklus, Operatorbrücke.

---

## Beitrag zu Objekt X

**Positiver Kernbefund:**

> [D] ≠ 0 in HH¹(A_alg, A_{C*})₁

Damit ist ein vollständig separierbarer mehrprimiger neutraler analytischer Kanal konstruiert. Die Primfaktorzerlegung von k spiegelt sich exakt in den Kommutatorgrenzwerten:

> D(μ_k) = μ_k · Σ_{p|k} B_{p,v_p(k)}

**Verbleibende Lücken für Objekt X:**
- neutral statt geladen
- A_{C*}-wertig statt A_alg-wertig
- naiver geladener Sandwichansatz scheitert
- keine geladene HH¹-Klasse
- kein Cup-Aufstieg, kein Dualzyklus, keine Operator-/Weil-Form-Brücke

**Neuer präziser Engpass:**
> Finde eine gemeinsam lokalisierte geladene Singularität, deren Transportdifferenzen dennoch primweise separierbar bleiben.

**Nächster Auditknoten:** NEU-209 — Singulärer Träger separierbarer Primkanäle und Charakterkern-No-go
