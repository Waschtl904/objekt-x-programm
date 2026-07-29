# GPT-Audit-Zwischenbilanz

**Stand: 29. Juli 2026 — nach vollständiger Auswertung der Ordner 00, 01, 02, 03 + DAG-Audit NEU-123–127 + Audit NEU-128A/B/130/131 + Audit NEU-132–136 + Audit NEU-137–140 + Audit NEU-141–145 + Audit NEU-146–150 (offen, Mellinfehler) + Audit NEU-151–155**

Dieses Dokument sichert den Gesprächsstand des laufenden GPT-Auditdurchlaufs
für die Verwendung in einem neuen Chat-Kontext. Es wird am Ende des Gesamtdurchlaufs
zu einem vollständigen Übergabe-Prompt zusammengefasst.

---

## Repo-Koordinaten

- **Repository:** `Waschtl904/objekt-x-programm`
- **Kanonisches Kontrollblatt:** `00-grundlegung/ebene-XVI-objekt-x.md`
  — Revision 2, Stand NEU-221e (26. Juli 2026)
- **Navigationskarte:** `KARTE.md` im Root
  — vollständig API-verifiziert, alle 8 Ordner, 348 Dateien total

---

## Verifikationsstand KARTE.md

| Ordner | Inhalt | Dateizahl | Verifikation |
|--------|--------|-----------|-------------|
| 00-grundlegung | Axiome, Ebenendokumente, p1-Testreihe | 20 | ✅ 2026-07-28 |
| 01-primkanten-werkzeuge | NEU-003–056, NEU-223–249 | 86 | ✅ 2026-07-28 |
| 02-jacobi-limes | NEU-058–090 | 34 | ✅ 2026-07-28 |
| 03-weil-form-statistik | NEU-091–120 | 31 | ✅ 2026-07-28 |
| 04-grenzoperator-renormierung | NEU-121–150 + Varianten | 42 | ✅ 2026-07-28 |
| 05-primkanal-fourierladung | NEU-151–173 + Varianten | 34 | ✅ 2026-07-28 |
| 06-hochschild-bc-algebra | NEU-174–222 + a–z-Varianten | 66 | ✅ 2026-07-28 |
| 07-weil-explizitformel | NEU-220–221e, NEU-242–246 | 35 | ✅ 2026-07-28 |
| **Gesamt** | | **348** | **alle ✅** |

**Hinweis (03):** NEU-118 liegt doppelt vor (`Bombieri_Normalisierung` und `X_Rigiditaet_R1_Nachweis`)
— beide als separate Dateien in KARTE.md eingetragen. Thematisches Duplikat mit NEU-113 vermerkt.

---

## GPT-Audit-Fortschritt

### Bereits vollständig ausgewertet

#### 00-grundlegung
Referenz- und Kontrollordner — kein Forschungsinhalt, nur verbindliche Karte.
Maßgeblich: `ebene-XVI-objekt-x.md` (Revision 2). Trennung der drei logischen
Ebenen (intrinsische Axiome / Brückenarchitektur / Realisierungsbedingungen)
sowie Gültigkeitsetiketten (`global`, `bridge`, `spectral`, `Feshbach`, `HH`,
`route-conditional`) und Konstruktionspfade P0–P5 sind hier kanonisch definiert.

#### 01-primkanten-werkzeuge (86 Dateien, NEU-003–056 + NEU-223–249)

| Schicht | Endurteil |
|---|---|
| A₂Dʳ als analytischer Träger | substanziell entwickelt |
| BC-KMS/Skalierung | stark als Hintergrundstruktur |
| [ω̃₂] ≠ 0, [L₃] ≠ 0 — frühe Beweise | **nicht tragfähig** |
| Roher Shift / direkter Hilbert–Pólya-Operator | **negativ ausgeräumt** |
| D_rel kompakter Resolvent | **strukturell ausgeschlossen** (Transportgenerator, NEU-225) |
| Graphische Primreinheit | strukturell stark |
| Kantendiagonalität | extrinsische Annahme, nicht hergeleitet |
| Feshbach-Transfer K(z) = V*(D_rel−z)⁻¹V | ernsthafte Arbeitshypothese, **offen** |
| Intrinsische positive Primkopplung | **zentraler Hauptengpass** |
| Mapping-Cone-Pfad | quellenmäßig **blockiert** (NEU-242 in 07) |
| B₃ᵃᵈᵐ-Provenienz | **ungeklärt** — darf nicht mit Kettenraum identifiziert werden |

**Präzisester Engpass (NEU-229):**
Gesucht ist eine intrinsische Quelle für Λ_p oder b_p — keine der vorhandenen
KMS-, Hochschild-, Wres- oder Ladungsstrukturen liefert dies. Formale
Positivitätsklassifikation: h_p ≥ 0 ⟺ a_p ≥ 0 und |β_p(k)|² ≤ a_p(k,k).
Die Rohkopplung liefert β_p = 0 (weil T_p^raw · e_p = 0). Mischblock fehlt.

**Aktueller konstruktiver Pfad (NEU-243–249):**
Koszul-Kandidat d_K = Σ_q Δ_q ⊗ (e_q ∧ ·) aus kommutierenden Bewertungsderivationen.
Blockiert an Typbarriere: δ_p wirkt auf A_alg, aber Liftbereich liegt in
noch nicht vollständig provenienzgeklärtem B₃ᵃᵈᵐ. NEU-249 legt verbindlich
fest: 𝔅 := A_Q, C₃^HH(𝔅) = 𝔅^⊗4, Bd₃^HH(𝔅) = im b₄.

#### 02-jacobi-limes (34 Dateien, NEU-058–090)

| Teilpfad | Endurteil |
|---|---|
| Direkter Jacobi-Limes A_N → D_rel | durch NEU-224/225 **überholt** |
| Starker Mangoldt-Limes auf festen Vektoren | **null** |
| Reiner Vorwärtsshift | nilpotent — Spur und Determinante **trivial** |
| Additive/modulare Periodisierung | **negativ ausgeschlossen** |
| BC-Zeit als Quelle von log p | **strukturell stark** |
| Jacobi-Schließung B_N^Λ | nichttrivial, aber quadratisch in Λ² |
| Relative Resolventdeterminante | kontrollierbarer Modellkandidat |
| NEU-090-Konstantengrenzwert T_N(z) → γ²/2 | **falsch** (tatsächlich → 0) |
| Direkter ξ-Determinantenanschluss | **nicht erreicht** |

#### 03-weil-form-statistik (31 Dateien, NEU-091–120)

| Teilpfad | Endurteil |
|---|---|
| Weil-Positivitätsstrategie | **zentrales Leitprinzip** — Ordner etabliert Gram-Priorität |
| Normalisierung nach Bombieri (NEU-113/118) | sorgfältig ausgearbeitet, kanonisch |
| Statistische Formapproximationen | tragfähig als Schätzrahmen |
| R1-Rigiditätsnachweis (NEU-118b) | **offen** — Typbarriere analog zu Koszul-Problem |
| Skalenkorrektur √N → √(N/log N) | kritische Korrektur, Klasse-B-Rücksetzung erzwungen |
| Weil-Explizitformel-Anschluss | strukturell vorbereitet, aber nicht vollzogen |

#### 04-grenzoperator-renormierung — Teilergebnis: NEU-128A/B, NEU-130, NEU-131

| Datei | Hauptaussage | Tragfähiger Kern | Problem / Lücke | Status |
|---|---|---|---|---|
| NEU-128A | Primkanal-Operator C_p^rel (erster Entwurf) | Basisnotation korrekt | Nichtentartung und T2 noch nicht definiert | ✓[M]_part |
| NEU-128B | Überarbeitung mit explizitem c_p | c_p-Notation eingeführt | Herkunft von c_p aus X nicht gezeigt | ✓[M]_part |
| NEU-130 | Spurklassenabschätzung Σ_rel^ren ∈ S₁ (Re β > 0) | S₁-Mitgliedschaft für Re β > 0 korrekt | Abhängig von offener |c_p|²-Schranke | ✓[K/M] |
| NEU-131 | Spurformel Tr(Σ_rel^ren) = −ζ'/ζ für Re β > 1 | Algebraisch korrekte Gleichung | Identität wird durch Zielgewicht R_p definiert, nicht hergeleitet | ✓[M]_part |

**Offene DAG-Knoten nach NEU-128–131:**
- J-123-Komplex (9 Knoten): 5 Korrekturen eingetragen, 3 neg. Befunde gesichert
- W-124/125/127: Skalakorrektur + Klasse-B-Rücksetzung + Typanforderung NEU-128ff.
- Nichtentartung c_p ≠ 0 für alle Primzahlen: **?[O]** — nach NEU-152 ausgelagert
- T2-Orthogonalitätsbeweis: **?[O]** — nach NEU-141ff. ausgelagert

#### 04-grenzoperator-renormierung — Teilergebnis: NEU-132–136

| Datei | Hauptaussage | Tragfähiger Kern | Problem / Lücke | Status |
|---|---|---|---|---|
| NEU-132 | H1/H2/H3-Relationen, PSWF, Abel-Primkantenraum | Motivische Primkanten-Struktur | Kein orthogonaler Hilbertraum ⊕_(m,p)^⊥ H_{m→pm} definiert | ✓[M]_part |
| NEU-133 | Primschalen, Abel-Lemma, relativer Graphraum | Kanalnormen und Schalenkonstruktion | Keine formale orthogonale Direktsumme über Kantenlabels | ✓[M]_part |
| NEU-134 | Nichtentartungsschranke |c_p|² = (log p)²·B_p | Formale Faktorisierung | B_p > 0 nicht bewiesen; B_p = O(1/p) offener Knoten | ?[O] |
| NEU-135D | Obere Schranke |c_p|² = O((log p)²/p) | Konditionale obere Schranke korrekt | Quellprovenienz offen; nur bedingt aus NEU-134 | ✓[K/M] |
| NEU-136 | Verbindung Jacobi-Limes → Grenzoperator | Übergangsdokument | Überholt durch NEU-224/225 | ✓[M]_neg |

**Offene DAG-Knoten nach NEU-132–136:**
- B_p > 0 (untere Schranke, Nichtentartung): **?[O]** → NEU-152
- B_p = O(1/p) (obere Schranke): konditional aus NEU-134/135D, kein Neubeweis
- Edge-Label-Direktsumme ⊕_(m,p)^⊥: in NEU-132/133 **nicht** formal definiert → ✓[M]_neg,Quelle

#### 04-grenzoperator-renormierung — Teilergebnis: NEU-137–140

| Datei | Hauptaussage | Tragfähiger Kern | Problem / Lücke | Status |
|---|---|---|---|---|
| NEU-137 | Absolutkonvergenz Σ_rel^ren für Re β > 0 | S₁-Mitgliedschaft korrekt belegt | Konditional auf |c_p|²-Schranken | ✓[K/M] |
| NEU-138 | Spurformel vorbereitend, Kanalnormierung | c_p-Normierung expliziert | Identität mit −ζ'/ζ noch nicht vollzogen | ✓[M]_part |
| NEU-139 | Konvergenzabgrenzung Re β = 1 als kritische Linie | Halbebenenstruktur S₁ ↔ Re β > 1 korrekt | Abhängig von offener Schranke | ✓[K/M] |
| NEU-140 | Vorbereitende Aggregation für Diagonaloperator R | Überblick über Spurhierarchie | Noch kein R-Operator; Vorbereitung zu NEU-141 | ✓[M]_part |

---

#### 04-grenzoperator-renormierung — Teilergebnis: NEU-141–145

**Zentraler Befund des Blocks:**

> T2 und R werden nicht quellentreu hergeleitet, sondern durch eine spätere
> Edge-Label-Rekonstruktion ermöglicht. Die gewöhnliche Identität mit −ζ'/ζ
> für Re s > 1 ist algebraisch korrekt, aber zielwertgesteuert. NEU-145
> definiert die „regulierte Spur" im kritischen Streifen schlicht als
> analytische Fortsetzung von −ζ'/ζ; die Nullstellen und damit die RH werden
> importiert, nicht operatoriell hergeleitet.

| Datei | Hauptaussage | Tragfähiger Kern | Problem / Lücke | Status |
|---|---|---|---|---|
| NEU-141 | Unbeschränktes R stellt Mangoldt-Gewichte wieder her | Drei Spurebenen richtig unterschieden; R·Σ ∈ S₁ ⟺ Re s > 1 konditional korrekt | T2, c_p ≠ 0 und obere Schranke offen; Mangoldt-Gewicht per Definition eingebaut | ✓[M]_part |
| NEU-142 | Edge-Labels implizieren T2 | Abstraktes Hilbertsummenlemma und Zielkollisionsdiagnose korrekt | Tatsächliches Labeling nicht entschieden; RG=Λ nicht hergeleitet | ✓[M]_part |
| NEU-143 | T2-Abschluss im Edge-Fall | Orthogonalität folgt unter orthogonaler Kantensumme | Voraussetzung nur angenommen; P_p fälschlich Projektor genannt | ✓[K/M] |
| NEU-144 | R als selbstadjungierter primdiagonaler Operator | Korrigierte Diagonalkonstruktion möglich; gewöhnliche Spur für Re s > 1 korrekt | T2 überbewertet; Nichtentartung offen; Domain falsch gewichtet; Unbeschränktheit nur bedingt | ✓[M]_part |
| NEU-145 | Regulierte Spur := meromorphe Fortsetzung von −ζ'/ζ | Gewöhnliche gegen regulierte Spur klar getrennt; R·Σ im krit. Streifen nicht spurklassig korrekt festgestellt | Zirkuläre Definition; Nullstellen importiert; kein Operatorbezug; Residuen-, Cutoff- und Wärmeskalenfehler | ✓[M]_part |

**Aktualisierte DAG-Knoten nach NEU-141–145:**

| Knoten | Aussage | Status |
|---|---|---|
| [T2-142-1] | Edge-Label ⟹ T2 | ✓[M] |
| [T2-142-2] | Edge-Label intrinsisch in alten Quellen | ✓[M]_neg,Quelle |
| [T2-143] | T2 im rekonstruierten Edge-Modell | ✓[K/M] |
| [R-144-1] | c_p ≠ 0 für alle Primzahlen | ?[O] |
| [R-144-2] | R positiver selbstadjungierter Diagonaloperator | ✓[K/M] unter T2 + Nichtentartung |
| [R-144-3] | R unbeschränkt | ✓[K/M] unter offener oberer Schranke für |c_p|² |
| [R-144-4] | R·Σ(s) ∈ 𝒦 (Re s > 0) | ✓[K/M] |
| [R-144-5] | R·Σ(s) ∈ S₁ ⟺ Re s > 1 | ✓[K/M] |
| [R-144-6] | Tr(R·Σ) = −ζ'/ζ als intrinsische Herleitung | ×[M] |
| [Reg-145-1] | Tr_reg := −ζ'/ζ als Definition | ✓[K/M] |
| [Reg-145-2] | Operatorielle Realisierung der Regularisierung | ?[O] |
| [Reg-145-3] | RH aus Polgeometrie der definierten Spur | ⚠[M] — tautologische Umformulierung |
| [Reg-145-4] | (R+ε)⁻¹R-Regularisierung | ✓[M]_neg |

**Gesamtstatus Block NEU-141–145:** ✓[M]_part

---

#### 05-primkanal-fourierladung — Teilergebnis: NEU-151–155

**Zentraler Befund des Blocks:**

> Der stärkste Fortschritt liegt in NEU-155: Rohkopplung T_p, induzierter
> Primkanaloperator C_p^[ε̂_p] und Rang-eins-Erweiterung C_p^rel[ε̂_p]
> werden erstmals sauber getrennt. Dadurch werden zentrale Konstruktionen
> aus NEU-151 und NEU-154 nachträglich typologisch ungültig.

| Datei | Hauptaussage | Tragfähiger Kern | Problem / Lücke | Status |
|---|---|---|---|---|
| NEU-151 | Rang-eins-Modell und Normaudit | Normidentitäten ‖C_p^rel‖_{S₁,S₂} = |c_p|; P_p ≠ π_p; Notationsbereinigung | Rang genau 1 offen; obere Schranke und Finite-Part falsch als bewiesen importiert | ✓[M]_part |
| NEU-152 | Gleichmäßige Nichtentartung von c_p | Reduktion auf B_p ≥ A/p; Auslöschungsanalyse; Vorrang von NEU-153 erkannt | Keine Koeffizientenwerte; keine obere oder untere Schranke; Phase von c_p nicht kanonisch | ✓[M]_part |
| NEU-153 | Hebungsunabhängigkeit und Liftgeometrie | Starke/schwache Invarianz sauber getrennt; positive und semidefinite Modellgeometrie | Quell-/Zielnorm offen; zweite Variationsformel falsch (Faktor 2); Projektionsnichtvernichtung fehlt | ✓[M]_part |
| NEU-154 | Pullback über C_p^rel auf Liftvektoren | Abstrakte Quotienten- und Reichweitenideen | Zentraler Operator wirkt auf falschem Raum; Injektivität mit Rang ≤ 1 unvereinbar; globale Skalierung unzulässig | ⚠[M], Kernpullback ×[M] |
| NEU-155 | Trennung von Rohkopplung, Primkanaloperator und Rang-eins-Erweiterung | Wesentliche Typkorrektur; Rohkopplungsquotient sinnvoll konditionalisiert | B₃ᵃᵈᵐ, Pullback und Einbettungsisometrie offen; Endformel erneut typfalsch | ✓[M]_part |

**Detailbefunde NEU-151–155:**

*Drei widerlegte Statusmarker (NEU-151):*
- Obere Schranke O((log p)²/p): von NEU-151 als gesichert übernommen, von NEU-152 selbst als unbewiesene Annahme identifiziert → **?[O]** (zurückgestuft von ✓[M])
- Skalarer Finite-Part aus NEU-148/149: NEU-148 verwechselt Primlabel-Cutoff φ(p/X) mit Primpotenzcutoff φ(p^k/X); Mellin-Integrand falsch → **×[M]**
- „Kein Import hängt an offener Hypothese": widerlegt durch obige beiden Punkte → **×[M]**

*Rang-eins-Situation nach NEU-155:*
- rang C_p^rel ≤ 1: **✓[M]** (folgt trivial aus Rang-eins-Struktur)
- rang C_p^rel = 1 für alle p: **?[O]** (erfordert c_p ≠ 0, nicht bewiesen)

*Zweite Variationsformel in NEU-153:*
- NEU-153 schreibt d²/dt²|_{t=0} |A + tB + t²C|² = 2|B|² + 2Re⟨A,C⟩
- Korrekt ist: 2|B|² + **4**Re⟨A,C⟩ → **×[M]**

*Pullback-Situation nach NEU-155:*
- Alter Pullback (NEU-154): ⟨C_p^rel x, C_p^rel y⟩ auf Liftvektoren → **×[M]** (falscher Operatortyp)
- Neuer offener Kandidat (NEU-155): q_conn(x) =? |T_p x|² bzw. ⟨T_p x, T_p y⟩ → **?[O]**
- Unter diesem Kandidat gilt T_p(v_p) = 0, also q_conn(v_p) = 0 ≠ 1: positive-definite Kugelgeometrie aus NEU-153 nicht anwendbar

*Ebenenarchitektur (stärkster positiver Befund):*
> intrinsische Rohkopplung T_p → Hebungsauswertung → eindimensionaler Primkanal C_p^[ε̂_p] → Rang-eins-Erweiterung C_p^rel[ε̂_p]

Die Rang-eins-Struktur entsteht erst durch Kompression auf den eindimensionalen Primkanal, nicht aus einer Degeneration der ursprünglichen Kopplung.

*Interner Typfehler im Endbefund NEU-155:*
- NEU-155 schreibt C_p^rel[ε̂_p](v_p) ~ Ψ_p; v_p liegt weder in ℂε_p noch im dritten Schichtkanal → **×[M]**

**DAG-Knoten nach NEU-151–155:**

| Knoten | Aussage | Status |
|---|---|---|
| [P-151-1] | rang C_p^rel ≤ 1 | ✓[M] |
| [P-151-2] | rang C_p^rel = 1 | ?[O] |
| [P-151-3] | P_p = |c_p|²·π_p, P_p ≠ π_p allgemein | ✓[M] |
| [P-151-4] | |c_p|² = O((log p)²/p) | ?[O] — zurückgestuft |
| [P-152-1] | B_p ≥ A/p | ?[O] |
| [P-152-2] | c_p ≠ 0 für alle p | ?[O] |
| [P-153-1] | Ψ_p hebungsunabhängig (Vektor) | ?[O] |
| [P-153-2] | |Ψ_p| hebungsunabhängig (Norm) | ?[O] |
| [P-153-3] | |c_p|² intrinsisches Primgewicht | ✓[M]_neg — im derzeitigen hebungsrelativen Modell |
| [P-153-4] | zweite Variationsformel | ×[M] |
| [P-154-1] | Pullback über C_p^rel auf Liftvektoren | ×[M] |
| [P-155-1] | Drei-Operatoren-Trennung T_p / C_p^[ε̂_p] / C_p^rel[ε̂_p] | ✓[M]_part |
| [P-155-2] | q_conn(x) =? |T_p x|² | ?[O] |
| [P-155-3] | ℒ_p^ch ≠ ∅ ⟺ T_p(ℰ_p^ch) ≠ {0} | ✓[K/M] unter Rohpullback und Domänenannahmen |
| [P-155-4] | ι_{J,N} isometrisch | ?[O] |
| [P-155-5] | B₃ᵃᵈᵐ typgenau identifiziert | ?[O] |

**Stärkster positiver Satz des Blocks:**
> T_p, C_p^[ε̂_p] und C_p^rel[ε̂_p] sind drei verschiedene, klar typisierte Abbildungen.

**Stärkster negativer Satz des Blocks:**
> |c_p|² ist derzeit kein wohldefiniertes intrinsisches Primgewicht.

**Was der Block nicht erreicht:**
- Wohldefiniertheits- oder Nichtentartungsnachweis für c_p
- Intrinsische Formulierung einer skalaren Primgröße
- Rückbindung an Weil-Form oder von-Mangoldt-Summe
- q_conn = |T_p ·|² bleibt eine neue Rekonstruktion ohne Quellenbasis

**Gesamtstatus Block NEU-151–155:** ✓[M]_part

---

### Noch ausstehend in 04-grenzoperator-renormierung

NEU-146 bis NEU-150 (Abschlussblock) — **Mellinfehler aus NEU-148/149 bereits als Vorabinformation bekannt** (durch Rückbindung in NEU-151-Audit identifiziert):

| Datei | Thema |
|---|---|
| NEU-146 | Cutoff-Finite-Part-Mangoldt-Spur |
| NEU-147 | Explizite Finite-Part-Struktur |
| NEU-148 | Geglättete Mellin-Finite-Part-Spur — **Mellinfehler: φ(p/X) statt φ(p^k/X)** |
| NEU-149 | Restkontrolle / Nullstellenvermeidende Kontur — abhängig von NEU-148 |
| NEU-150 | Rückbindung Mellin-Operatorspur |

---

### Noch ausstehend in 05-primkanal-fourierladung

| Dateien | Thema | Nächster Auditblock |
|---|---|---|
| NEU-156–160 | Verbundene Restspurform, Zulässigkeitsraum, invariante Formen, Dualzeuge, Rohkopplungsquotient | **als nächstes** |
| NEU-161–173 + Varianten | Weitere Primkanal-Fourierladungsstruktur | danach |

**Offene Leitfragen für NEU-156–160:**
1. Ist B₃ᵃᵈᵐ typgenau als Ketten-, Koketten- oder Formraum identifiziert?
2. Wird q_conn(x) = |T_p x|² als Rekonstruktion ausgewiesen oder als Quellenbefund ausgegeben?
3. Erfordert T_p(e_u V_p) ≠ 0 echte Projektionsnichtvernichtung, nicht nur injektive Labels?
4. Trägt der Rohquotient mehrere invariante Formen — und wird dies als Eindeutigkeitsbarriere behandelt?
5. Ist der Dualzeuge auf dem typkorrekten Zielraum von T_p definiert?

---

### Noch ausstehend (Gesamtübersicht)

| Ordner | Verbleibende Dateien | Priorität |
|---|---|---|
| 04-grenzoperator-renormierung | NEU-146–150 (5 Dateien) | parallel ausstehend |
| 05-primkanal-fourierladung | NEU-156–173 + Varianten (ca. 29 Dateien) | **als nächstes** |
| 06-hochschild-bc-algebra | NEU-174–222 + a–z (66 Dateien) | danach |
| 07-weil-explizitformel | NEU-220–221e, NEU-242–246 (35 Dateien) | abschließend |

---

## Persistente offene Knoten (ordnerübergreifend)

| Knoten | Beschreibung | Zuletzt aktiv |
|---|---|---|
| Intrinsische positive Primkopplung | Hauptengpass: keine Quelle für Λ_p oder b_p in KMS/HH/Wres | NEU-229 (01) |
| B₃ᵃᵈᵐ-Provenienz | Koszul-Lift typgeblockt; jetzt auch in 05 als [P-155-5] offen | NEU-243–249 (01), NEU-155 (05) |
| Nichtentartung c_p ≠ 0 | B_p > 0 nicht bewiesen; obere Schranke ebenfalls zurückgestuft auf ?[O] | NEU-134, NEU-152 |
| Edge-Label-Direktsumme | In NEU-132/133 nicht formal definiert; nur in rekonstruiertem NEU-44 | NEU-142/143/144 (04) |
| R-Cutoff ↔ Primzahlcutoff | Einseitige Schranke R_p ≳ p/log p reicht nicht für Äquivalenz | NEU-145; → NEU-146–150 |
| Operatorielle Regularisierung Tr_reg | Kein unabhängiger Cutoff/Wärme/Finite-Part-Satz bewiesen | NEU-145; → NEU-146–150 |
| Mellinfehler NEU-148/149 | φ(p/X) statt φ(p^k/X); betrifft alle Importe aus NEU-148/149 | NEU-151 (05) via Rückbindung |
| Feshbach-Transfer K(z) | Arbeitshypothese, nicht geschlossen | NEU-229 (01) |
| Rohkopplungs-Pullback q_conn = |T_p·|² | Neue Rekonstruktion, kein Quellenbefund; Wohldefiniertheit offen | NEU-155 (05) |
| Hebungsunabhängigkeit |c_p|² | Kein intrinsisches Primgewicht solange Norminvarianz offen | NEU-153 (05) |
