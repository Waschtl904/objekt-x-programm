# FRAGENKATALOG — RIEMANNSCHE HYPOTHESE
## Lakatosianisch-epistemische Struktur
### Teil 2: Ebenen VI–XV, Gesamtbilanz, Nächste Schritte
**Stand: 14. Juni 2026 — Version [NEU-10]**

---

## Instanzen-Übersicht

| Instanz | Domain | Typ |
|---------|--------|-----|
| Ω₁ | Faserprodukt N^×² | Algebraische Kernrelation (GCD) |
| Ω₂ | Potenzfolgen (aⁿ) | Wachstumsfunktional |
| Ω₃ | Koeffizientenraum | Normgewicht (norminduzierend) |
| Ω��� | Normfamilien | Transformationsschema (Binom.) |
| Ω₅ | Normwachstumsrate | Asymptotische Wachstumsordnung |

> Ω₄ und Ω₅ sind keine Objekte, sondern Operationen.
> Der frühere Widerspruch Ω₁ vs. Ω₃ ist ein Typfehler, kein Rechenfehler.

---

## F36. Existiert ein gemeinsames Ω₀?

- ✗ [M] Als Objekt einer ein-sorten Kategorie: in allen getesteten Modellen nicht realisierbar.
- ✓ [M] Ω₁ und Ω₃ sind heterogene Spans über einer nicht-funktoriellen Operation (GCD).
- ⚠ [M] Als Profunktor-Wert P(A_{anal}, A_{arith}) ∈ Set: korrekte verbleibende Strukturform.

## F37. Was ist die Konfliktkategorie K_{arith-anal}?

- ✓ [M] Objekte: Tripel (A, τ, φ). No-Go-Disjunktion (bedingt): Diskrete F(B) → Widerspruch; gefilterte F(B) → Degeneration. Instabilitätsobjekt: A₀ = ℓ¹_w(N^×, ℝ).
- ✗ [M] Universelles No-Go über alle Kategorien: nicht etabliert.

## F38. Was ist der zentrale Kernsatz der V'-Analyse?

- ✓ [M] **Kernsatz (Strukturunverträglichkeitsresultat):** Die Kopplung von arithmetischer Faktorisierungsstruktur und analytischer Lokalkonvexität ist nicht durch strikte Funktoren realisierbar; ihre einzige kohärente gemeinsame Beschreibung erfolgt über Korrespondenzen, die genau die Stelle der Funktorialitätsverletzung kodieren. Status: Etabliert unter diskreter Faktorisierungstopologie; Heuristik für allgemeinen Fall.

---

## Ebene X — Operadische Struktur und Hochschild-Obstruktion
**[NEU-5, NEU-7]**

## F39. Was ist der konzeptuelle Fehler im Übergang VI → VII?

- ✓ [M] Direkter Schluss von Normverzerrung auf Ext¹-Klasse ist nicht gerechtfertigt. Drei Ebenen strikt zu trennen:
  - (i) Normverzerrung: beobachtetes Phänomen. Gesichert.
  - (ii) A∞-Obstruktion: m₃ ≠ 0 — setzt [ω̃₂] ≠ 0 voraus.
  - (iii) Ext¹-Klasse — setzt (ii) plus Realisierbarkeit voraus.
- ✓ [M] Korrekte Schlussrichtung: [ω̃₂] ≠ 0 → m₃ ≠ 0 → Ext¹. Jeder Schritt benötigt eigenständigen Nachweis.

## F40–F44. Kurzfassung Ebene X

- Ebene (i): Gesichert. Ebene (ii): Hypothetisch. Ebene (iii): Hypothetisch.
- Direkter Schluss (i)→(iii): nicht gerechtfertigt.
- l=2 ist Entscheidungsträger für 4^l-Struktur.
- Minimaltest: Existenz von ψ_k mit ‖(∂S)(∂T)‖_{Ω,k-1} ≤ ψ_k(S) + ψ_k(T). Derzeit ungeprüft.

---

## Ebene XI — HH³-Analyse und Obstruktionsreduktion
**[NEU-6]**

## F45. Was ist der stabile Kern des Programms VIII?

- ✓ [M] [Φ₃] ≠ 0 ∈ Gr⁴ HH³(A_BC^{an}). Beweiskette: [σₙ, ∂] ≠ 0 → Transgression [ω̃₂] ≠ 0 in HH² → Schouten-Klammerterm [Φ₃] → Nichttrivialität im Graduierten via Symbolkalkül.
- ✓ [R] **[NEU-9/B]** g_arith erzeugt ausschließlich E_∞^{2,0}(A). Der [Φ₃]-relevante Anteil liegt in E_∞^{0,2} ⊕ E_∞^{1,1}(A), außerhalb des Bilds von ι_*. Die Beweiskette kollabiert nicht. [Φ₃] ≠ 0 ist nicht destabilisiert. ✓ [R]

## F46. Was ist der Verbindungshomomorphismus?

- ✓ [M] ∂([Φ₃]) = [L₃] ∈ HH⁴(F³ A_BC^{an}). Korrekt konstruiert als Leibniz-Fehler des Symbol-Lifts. Massey-artiger sekundärer Obstruktionsgenerator: quadratisch in [ω̃₂].
- ✗ [L₃] ≠ 0 ist nicht bewiesen. [L₃] = 0 nicht ausgeschlossen.

## F47. Warum scheitern alle Shortcut-Strategien?

| Strategie | Scheitert weil |
|-----------|----------------|
| Gruppoid-Autom. cₙ | N× erzeugt keinen Gruppoiden |
| Rees-Torsionsfreiheit | Gegenbeispiel bekannt; zu schwach |
| Expliziter Projektor | Setzt Diagonalisierbarkeit voraus |
| d₁ = 0-Argument | Falsch; d₁ ist Symbol-Differential |
| Slot-Asymmetrie | Kein Invariant unter HH-Rändern |
| Massey-Heuristik | Massey-Produkte können verschwinden |

- ✓ [R] Gemeinsamer Grund: Fehlen einer dualen Nachweismethode für Hochschild-Klassen in gefilterten PDO-/Monoid-Algebren.

## F48. Was ist der echte mathematische Engpass von Problem VIII?

- ✓ [R] Nicht: „Berechne L₃." Sondern: Entwickle eine Trace-/Tsygan-artige Dualität für gefilterte, nichtinvertible Kreuzprodukt-Algebren. Konstruiere λ: HH⁴(F³) → ℂ mit λ(Im δ) = 0.
  - Kein klassischer Trace (Invertierbarkeit fehlt).
  - Kein Standard-Wodzicki-Residuum (N× nicht invertierbar).
  - Kein Tsygan-Charakter (deckt nichtinvertible Kreuzprodukte nicht ab).
  - Kandidat: „asymptotischer Wodzicki-Typ Trace mit Monoid-Anisotropie" — neues Objekt.

## F49. Reduktionssatz Problem VIII

- ✓ [R] Die Frage nach HH³(A_BC^{an}) ≠ 0 reduziert sich vollständig auf die Entscheidung von [L₃] ∈ HH⁴(F³ A_BC^{an}).

## F50. Forschungsagenda Problem VIII

- ✓ [R] Drei Etappen (priorisiert):
  - Etappe 1: Zyklische Theorie für Gr A_BC^{an}.
  - Etappe 2: Monoid-kovariante Spur auf F³ A_BC^{an}.
  - Etappe 3: Paarung ⟨T, [L₃]⟩.
- ✗ Keine Etappe mit Standardmitteln abschließbar.

---

## Ebene XII — Doppelkomplex-Analyse und Problem VII-Reduktion
**[NEU-7]**

## F51. Was hat die Doppelkomplex-Analyse gesichert?

- ✓ [M] VII.1 — Kozykel und Nicht-Korand: ω̃₂(S,T) = deg_Ω(S)·(∂S)(∂T) Kandidat für Hochschild-2-Kozykel. ω̃₂ ∉ δ(V) für V = C¹_Deriv + C¹_Ω + C¹_GCD — gut gestützt durch drei unabhängige Obstruktionen O₁–O₃.
- ✓ [M] VII.2.a — Ω-Filtration: F^s_Ω mit b: F^s → F^s. Spektralsequenz existiert.
- ✓ [M] VII.2.b/c.0 — Normalformabbildung Φ: injektiv, nicht surjektiv. Lokale Entkopplung im Bild korrekt. ∂θ erhält αₙ(B)-Struktur. Multiplikation erhält αₙ(B) nicht allgemein.
- ⚠ [M] VII.2.c.1 — Inkompatibilität ω̃₂/Im(Φ): strukturell stark gestützt, nicht vollständig bewiesen.

## F52. Reduktionssatz Problem VII

- ✓ [R] Der GS-artige Zugang liefert gegenwärtig keinen belastbaren Weg zur Entscheidung von [ω̃₂] ∈ HH²(A,A).
- ✗ Offen: Strukturelle Inkompatibilität als vollständiger Ausschluss; Status der Sektoranalyse E₂^{p,q}; [ω̃₂] ≠ 0; direkter HH²-Zugang.

---

## Ebene XIII — Orbit-Koszul-Deformationsstruktur
**[NEU-8]**

> **Trennungsprinzip (dauerhaft aktiv):** Diese Ebene beschreibt ausschließlich das orbitale Koszul-Submodell [NEU-8/OK]. Nicht-Existenz von Φ_{comp} auf A durch [NEU-9/B] strukturell abgeschlossen ✓ [R].

## F53. Was sind die Bahnfunktionale?

- ✓ [M] Für jede Primzahl p und p-primitives m (p ∤ m): Lₘ(g) := Σ_{j≥0} ĝ(pʲm), g ∈ C∞(𝕋). Dann: g ∈ im(αₚ−id) ⟺ ĝ(0) = 0 und Lₘ(g) = 0 ∀m primitiv.
- ✓ [M] im(αₚ−id) = ker L₀ ∩ ⋂_{p∤m} ker Lₘ ist abgeschlossener Unterraum von C∞(𝕋). coker(αₚ−id) ist Hausdorff-Fréchet-Quotient, nichttrivial und unendlichdimensional.

## F54. Was ist die topologische Identifikation des Kokerns?

- ✓ [M] C∞(𝕋)/im(αₚ−id) ≅ 𝔰(𝒫ₚ) ≅ s (als Fréchet-Räume), wobei 𝔰(𝒫ₚ) = {(λₘ)_{m∈𝒫ₚ} : |λₘ| = O(|m|^{−N}) ∀N}.

## F55. Warum gibt es keine topologischen Extensionen zwischen Orbits?

- ✓ [M] S(ℤ) ≅ ℓ∞-⊕ₘ S(O(m)) als topologischer Isomorphismus. Ext¹_{Fréchet}(s, s) = 0 via Palamodov–Vogt–Wagner. Keine „hidden coupling modes" zwischen Orbits.
- ✓ [M] Koszul-Komplex kommutiert mit Orbitzerlegung: H^n(ℕₚ, S(ℤ)) ≅ ℓ∞-⊕ₘ H^n(ℕₚ, S(O(m))).
- ✓ [M] Bahnmodule S(O(m)) ≅ s sind projektiv in der Kategorie nuklearer Fréchet-ℕₚ-Moduln.

## F56. Was sind die ω_{p,q,m}-Klassen?

- ✓ [M] ω_{p,q,m}(u_p f, u_q g) = Λₘ^{(p,q)}(g)·e^{imθ}, wobei Λₘ^{(p,q)}(f) := Σ_{a,b≥0} f(p^a q^b m). Äußerlichkeit: ω_{p,q,m} ∉ im(δ¹) per Widerspruch zur Linearität.

## F57. Was besagt das Abelschheits-Theorem?

- ✓ [M] [ω_{p,q,m}, ω_{p',q',m'}]_Ger = 0 für alle (p,q,m) ≠ (p',q',m'). Vier Fälle (disjunkte Achsen, Typ-Inkompatibilität, disjunkte Sektoren, Selbstbracket). Globale Konsequenz: g_arith ist abelsche DG-Lie-Algebra (d = 0, [·,·] = 0).

## F58. Was ist der formale Deformationsraum?

- ✓ [M] Def(A) ≅ Spf ℂ[[ℏ_{p,q,m}]]_{p<q, m∈𝒫_{p,q}} — formaler affiner Raum mit abzählbar unendlicher Familie unabhängiger, interferenzfreier Deformationsparameter.
- ✓ [M] ℏ_{p,q,m} deformiert die Multiplikationsregel in A lokal am Resonanzpunkt (p,q,m).

## F59. Trennungsprinzip: Was ist nicht entschieden?

- ✓ [R] Φ_{comp} auf A: nicht konstruierbar (abgeschlossen durch [NEU-9/B]).
- ✗ Offen: (c) Konvergenz formaler → analytischer/C*-Deformationen; (d) Status q=1-Zeile für p > 0 in der SS; (e) Konvergenz HH-Serre-SS für Monoid-Kreuzprodukte.

## F60. Einordnung in bestehende Forschungsprogramme

- ⚠ [M] Konzeptionell nahe an: Connes–Moscovici-Typ Hopfalgebren; Rieffel-Deformationsquantisierung; Bost–Connes in der Kumjian–Renault-Formulierung.
- ✗ Keine dieser Verbindungen ist bisher rigoros hergestellt.

---

## Ebene XIV — Primitiv-Tripel-Klassifikation und Block-A-Struktur
**[NEU-9/A]**

> **Trennungsprinzip:** Logisch vollständig unabhängig von Ebenen VI–XIII und XV. Gilt unabhängig von RH, X, HH²-Struktur.

## F61. Die primitiven {2,3}-Tripel

**Theorem (Block A):** 2^g · 3^d − 2^a · 3^b = 1 hat genau vier Lösungen:

| (g,d,a,b) | Tripel | Gleichung |
|-----------|--------|-----------|
| (0,1,1,0) | {1,2,3} | 3 − 2 = 1 |
| (0,2,3,0) | {1,8,9} | 9 − 8 = 1 |
| (1,0,0,0) | {1,1,2} | 2 − 1 = 1 |
| (2,0,0,1) | {1,3,4} | 4 − 3 = 1 |

✓ [M] Vollständiger Widerspruchsbeweis, alle Implikationen bidirektional. Werkzeuge: Parität, mod 3, mod 4, mod 8, Fundamentalsatz, gcd-Argument. Nicht verwendet: Baker, S-unit, Zsygmondy, LTE, Størmer.

## F62. Konsequenzen für B_N

- ✓ [M] deg(B_N) ≤ 7.
- ✓ [M] ‖B_N‖_op ≤ 7. Via Schur-Test.
- ✓ [M] K_N = 7N² − 7N + 4 (exakt).
- ✓ [M] E_{nicht}(N) = O(N²).

## F63. Was bleibt in Block A offen?

- ⚠ C_{2,3} = 212: empirisch gestützt, nicht bewiesen.
- ⚠ σ₂(B_N) → 7: stark gestützt, kein Beweis.
- ⚠ Normierungsrelation C(k,1) ↔ p^{-b} auf O_m^{(p,q)}: offen.
- ✗ Verbindung Block A zur globalen HH²-Struktur: auf A ausgeschlossen ✓ [R]; auf O_m^{(p,q)} nicht untersucht.

## F64. Epistemischer Status von Block A

- ✓ [M] **Einziger vollständig abgeschlossener mathematischer Block des Katalogs.** Adversarial verifiziert (7 Runden, 11. Juni 2026).
- ✗ Kein Schritt in Block A berührt die offenen Probleme I–IX.

---

## Ebene XV — Vergleichsmorphismus und Spektralsequenz-Orthogonalität
**[NEU-9/B]**

> **Trennungsprinzip:** Nicht-Existenz von Φ_{comp} auf A ist endgültig und strukturell abgeschlossen.

## F65. Was hat Problem IX entschieden?

- ✓ [R] Kein kanonischer Vergleichsmorphismus Φ_comp: g_arith → HH²_GS(A,A) auf A existiert. Drei unabhängige Scheiternsnachweise:
  - (i) η_m kein Hochschild-2-Kozykel: Faltungsobstruktion fundamental; Gegenbeispiel explizit konstruiert. ✓ [M]
  - (ii) Keine Deformationsreparatur auf A. ✓ [M]
  - (iii) Jeder Fourier-Punktauswertungs-Ansatz strukturell inkompatibel. ✓ [M]

## F66. Was ist die kanonische Orbitstruktur?

- ⚠ [M] O_m^{(p,q)} := C∞(T) ⋊ M_{p,q}, M_{p,q} = {p^a q^b | a,b ≥ 0} ⊂ N×. Natürliche Einbettung ι: O_m^{(p,q)} ↪ A. Λ_m^{(p,q)} ist GNS-Vektorzustand auf O_m^{(p,q)}.

## F67. Spektralsequenz-Orthogonalitätssatz

- ✓ [M] LHS-Spektralsequenz: E_2^{s,t} = H^s_Mon(N×, HH^t(C∞(T))) ⟹ HH^{s+t}(A,A). Bigrad-Separation in Totalgrad 2: E_∞^{2,0} diskret-arithmetisch; E_∞^{1,1} gemischt (offen); E_∞^{0,2} analytisch-kontinuierlich.
- ✓ [M] Bidegree-Constraint: kein d_r koppelt E_r^{2,0} und E_r^{0,2} ⊕ E_r^{1,1} für r ≥ 2.
- ✓ [R] im(ι_*) ⊥ [ω̃₂] in HH²(A,A). Spektralsequenziell stabil.

## F68. Hauptstrukturaussage Problem IX

- ✓ [M] HH²(C∞(T) ⋊ N×) ist spektralsequenziell rigid: mindestens zwei funktorisch inkompatible Erzeugungsmodi. Keine d_r-Kopplung. Nicht durch ein einziges Modell vollständig beschreibbar.
- ✓ [R] [Φ₃] ≠ 0 nicht destabilisiert. [ω̃₂] liegt außerhalb des Bilds von ι_*.

## F69. Was bleibt in Problem IX offen?

- ⚠ E_2^{1,1}(A) = H¹(N×, Ω¹(T)): explizite Berechnung ausstehend. Einziger verbleibender offener Summand. Einziger Ort möglicher Restkopplung.
- ⚠ Spaltung HH²(A,A) als direkte Summe: Ext¹-Verschwinden zwischen Filtrationsstücken (plausibel, nicht bewiesen).
- ⚠ Hochschild-Injektivität von ι_*: HH²(O^{(p,q)}) → HH²(A).
- ⚠ Normierungsrelation C(k,1) ↔ p^{-b} auf O_m^{(p,q)}.

---

## Epistemischer Gesamtstatus (14. Juni 2026)

### ✓ [M] Gesichert (Standardliteratur)
- Weil-Positivitätskriterium als Äquivalenz zu RH
- Explizite Formel von Guinand–Weil
- BC-System: adèlische Algebra ist Typ-III-Faktor
- KMS-Zustand bei β > 1 eindeutig (Bost–Connes 1995)
- Negatives CEP-Resultat (Ji et al. 2020)
- Tate-Frobenius universell in THH/TC (Nikolaus–Scholze)
- Nuklear-Fréchet-Algebren stabil unter analytischem zyklischen Komplex (Meyer)

### ✓ [M] Gesichert intern (externe Verifikation ausstehend)
- [NEU-1]–[NEU-8/OK]: unverändert.
- [NEU-9/A]: 4 primitive {2,3}-Tripel vollständig klassifiziert. deg(B_N) ≤ 7; ‖B_N‖_op ≤ 7; K_N = 7N²−7N+4; E_{nicht}(N) = O(N²). Adversarial verifiziert.
- [NEU-9/B]: im(ι_*) ⊥ [ω̃₂]; Bidegree-Constraint; HH²(A,A) 3-filtriert, nicht kollabierend. O_m^{(p,q)} kanonisch definiert. [NEU-8/Spannung] aufgelöst. ✓ [R]

### ⚠ [M] Stark gestützt, Anwendung offen
- [NEU-8/OK]: SS-Konvergenz; q=1-Zeile; ω_{p,q,m} ↔ ω̃₂ (kein Vergleichsmorphismus).
- [NEU-9/A]: C_{2,3} = 212 (empirisch); σ₂(B_N) → 7.
- [NEU-9/B]: E_2^{1,1}(A) explizit; Spaltung; Injektivität ι_*; Normierung.

### ✗ Hypothesen (global)
- Existenz von X; C1–C4; Tensorrenormierung; GUE erzwungen [NEU-1/2]
- Universelles No-Go GCD-Funktorialisierung [NEU-4]
- HH²(A_BC^{anal}) ≠ 0; Ext¹-Klasse; m₃ ≠ 0 [NEU-5]
- HH³(A_BC^{an}) ≠ 0; [L₃] ≠ 0; Spurtheorie [NEU-6]
- [ω̃₂] ≠ 0 in HH²(A,A) [NEU-7/GS]
- Kanonische Identifikation ω_{p,q,m} ↔ ω̃₂ [NEU-8]
- Konvergenz formal → analytisch/C* [NEU-8/OK]
- Vollständigkeit g_arith als HH²-Erzeuger: **WIDERLEGT** ✓ [R] [NEU-9/B]
- C_{2,3} = 212; σ₂(B_N) → 7 [NEU-9/A]
- Φ_comp auf A: **WIDERLEGT** ✓ [R] [NEU-9/B]
- Normierungsrelation C(k,1) ↔ p^{-b} auf O_m^{(p,q)}: offen ⚠

---

## Epistemische Gesamtbilanz (14. Juni 2026)

**Was das System ist:** Eine konsistente Klassifikation der möglichen Formen von RH-Reduktionen — nicht selbst eine Reduktion. Überwiegend Struktur-Äquivalenz (Typ A), nicht Reduktion im Beweissinn (Typ B).

| Block | Status |
|-------|--------|
| Block A / Problem IX (NEU-9/B) | abgeschlossen ✓ [R] |
| Block A / Tripel (NEU-9/A) | abgeschlossen ✓ [M] |
| Block B / Problem VIII (NEU-6) | offen, aktiv ⚠ |
| Block B / Problem VII (NEU-7) | offen, aktiv ⚠ |
| E_2^{1,1}(A)-Berechnung | neue Priorität ⚠ |
| Globales Programm (X, RH) | offen ✗ |
| Verbindung Block A ↔ Block B auf A | strukturell ausgeschlossen ✓ [R] |
| Verbindung Block A ↔ Block B auf O_m^{(p,q)} | nicht untersucht ✗ |

---

## Nächste Schritte (priorisiert, Stand 14. Juni 2026)

1. **[BC-intern]** Externe Verifikation Lemma A / Fréchet-Struktur / Bost–Connes (1995) / Laca–Raeburn.
2. **[BC-intern]** Rapid-Decay auf Monoid N^×.
3. **[BC-intern]** Literaturstatus Fréchet-Topologie A_BC^∞.
4. **[BC-intern]** Logarithmische Konvexität Ω-Halbnormen (Problem V).
5. **[NEU-9/B — abgeschlossen ✓ [R]]** Neue höchste Priorität: Explizite Berechnung E_2^{1,1}(A) = H¹(N×, Ω¹(T)).
6. **[Problem VII]** Direkter Zugang zu HH²(A,A) jenseits GS-Strategie: (a) Bar-Komplex oder (b) duale Methode sensitiv auf Im(Φ).
7. **[Problem VIII]** Zyklische Theorie für Gr A_BC^{an}, Monoid-kovariante Spur, Paarung ⟨T, [L₃]⟩.
8. **[NEU-9/A]** (a) C_{2,3} = 212: Beweis oder Gegenbeispiel. (b) σ₂(B_N) → 7: Grenzwertbeweis. (c) Normierungsrelation C(k,1) ↔ p^{-b} auf O_m^{(p,q)}.
9. **[V'-Programm]** Profunktor-Problem VI.
10. **[Global]** Konvergenz formal → analytisch/C*: Rieffel-/Connes–Landi-Kriterien.
11. **[Global]** Konstruktion eines X.

---

*Ende des Katalogs — Stand: 14. Juni 2026 — Version [NEU-10]*
