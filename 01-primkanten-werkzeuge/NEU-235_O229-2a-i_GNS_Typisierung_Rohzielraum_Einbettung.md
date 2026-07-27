# NEU-235: [O-229-2a-i.1/2] — GNS-Typisierung und Rohzielraum-Einbettung

> Datum: 27. Juli 2026 | Status: ✓[M]_neg,Quelle — NEU-014 definiert GNS-/KMS-Struktur, aber keine Brücke Y_p → H_{φ_β}

---

## 1. Auditgegenstand

Knoten **[O-229-2a-i.1]** und **[O-229-2a-i.2]** verlangen eine quellenmäßige Prüfung,
ob NEU-014 neben der KMS-GNS-Struktur auch eine typkorrekte Einbettung

```
J_p : Y_p = Ran T_p^raw ——→ H_{φ_β}
```

definiert und ob Y_p = Ran T_p^raw^‾ als modular invariantes Teilobjekt des GNS-Raums
explizit ausgewiesen ist.

---

## 2. Was NEU-014 tatsächlich definiert ([O-229-2a-i.1])

### 2.1 Das C*-dynamische System

NEU-014 konstruiert explizit:

- **Algebra**: A = A_{2D}^r (dichte spektralinvariante Unteralgebra von A_{BC}^{C*})
- **Zustand**: φ_β = BC-KMS-Zustand eingeschränkt auf A_{2D}^r
- **Zeitentwicklung**: σ_t : A → A mit σ_t(V_n) = n^{it} V_n (Skalierungsautomorphismus)
- **GNS-Raum**: H_{φ_β} (implizit als GNS-Konstruktion aus φ_β, nicht explizit konstruiert)
- **Zyklischer Vektor**: Ω_{φ_β} (implizit; NEU-014 nennt ihn nicht)
- **Implementierende Gruppe**: U_t^φ : H_{φ_β} → H_{φ_β} (nicht explizit konstruiert)

### 2.2 Typpräzisierung

NEU-014 § 3–4 etabliert:

```
σ_t(A_{2D}^r) = A_{2D}^r                                    ✓[M]
φ_β|_{A_{2D}^r} ist ein KMS_β-Zustand für (A_{2D}^r, σ_t)  ✓[M]
Z(β) = ζ(β)                                                  ✓[M]
```

Nicht konstruiert in NEU-014:

- Die GNS-Darstellung (H_{φ_β}, π_{φ_β}, Ω_{φ_β}) als explizites Objekt
- Die implementierende unitäre Gruppe U_t^φ : H_{φ_β} → H_{φ_β}
- Ob φ_β treu ist (NEU-014 §5.2: φ_{β,χ} für β > 1 sind Typ-I-Faktor-Zustände, nicht Spur → nicht offensichtlich treu)
- Ob die Tomita–Takesaki-Modulargruppe oder nur die BC-Zeitentwicklung implementiert wird
- Ob U_t^φ π(a) Ω = π(σ_t^φ(a)) Ω auf einem dichten Bereich gilt

**Quellenbefund [O-229-2a-i.1]**: NEU-014 liefert das C*-dynamische System
(A_{2D}^r, φ_β, σ_t) quellenmäßig. Den GNS-Hilbertraum H_{φ_β} als
explizit konstruiertes, benanntes Objekt mit zyklischem Vektor und implementierender
Gruppe definiert NEU-014 **nicht**.

---

## 3. Rohzielraum-Einbettung ([O-229-2a-i.2])

### 3.1 Vollständige Durchsicht von NEU-014

NEU-014 enthält folgende Abschnitte:
- §1: Die Frage (X.4)
- §2: Bibliographische Grundlagen
- §3: KMS-Struktur auf A_{BC}^{C*} (Zeitentwicklung, Zustände)
- §4: KMS-Zustand auf A_{2D}^r (Einschränkung, Stetigkeit, KMS-Eigenschaft, explizite Formeln)
- §5: Frobenius-Eigenschaft (X.4b)
- §6: Phasenübergang und Verbindung zur RH
- §7: Hauptresultat
- §8–11: Status, offene Probleme, Zusammenfassung

**Befund**: Der Rohoperator T_p^raw, der Rohzielraum Y_p = Ran T_p^raw^‾
und jede Abbildung J_p : Y_p → H_{φ_β} erscheinen in NEU-014
**an keiner Stelle**.

### 3.2 Fehlende Strukturen im Einzelnen

Gemäß der Audit-Anforderung [O-229-2a-i.2] wäre nötig:

| Anforderung | Status in NEU-014 |
|---|---|
| J_p : Y_p → H_{φ_β} linear | nicht definiert |
| J_p injektiv oder quotientenverträglich | nicht definiert |
| Norm-/Formverträglichkeit | nicht definiert |
| Y_p ⊆ H_{φ_β} durch explizite Formel | nicht gesetzt |
| Verweis auf T_p^raw | nicht vorhanden |

### 3.3 Nicht-Ersetzbarkeit durch gemeinsamen Ursprung

Sowohl A_{2D}^r als auch T_p^raw haben ihren Ursprung in der BC-Algebra.
Dieser **gemeinsame algebraische Ursprung** begründet jedoch keine
quellendefinierte Einbettung Y_p ↪ H_{φ_β}. Die Übergabearchitektur
verbietet genau diese stille Identifikation.

Der GNS-Raum H_{φ_β} ist der Abschluss von π(A_{2D}^r)Ω, nicht von Ran T_p^raw.
Ohne explizite Brückenabbildung ist Y_p ⊆ H_{φ_β} nicht gesetzt.

---

## 4. Befund zu [O-229-2a-i.3], [O-229-2a-i.4], [O-229-2a-i.5]

Da bereits [O-229-2a-i.2] negativ geschlossen ist, erübrigen sich die
nachgelagerten Teilknoten durch Präzedenzregel:

- **[O-229-2a-i.3]** (U_t^φ J_p(Y_p) ⊆ J_p(Y_p)): nicht prüfbar — J_p nicht definiert
- **[O-229-2a-i.4]** (Fixraumklassifikation Y_p^{U^φ}): nicht prüfbar — Y_p nicht eingebettet
- **[O-229-2a-i.5]** (Ω_{φ_β} ∈ J_p(Y_p)?): nicht prüfbar — J_p nicht definiert
- **[O-229-2a-i.6]** (Ergodizität / Zentralisator): keine Grundlage in NEU-014 auf Y_p

Diese Teilknoten bleiben offen mit Quellenblockierung, nicht als positiver oder
negativer Befund zum Inhalt.

---

## 5. Umfangsklauseln

Der Befund schließt **nicht** aus:
- dass eine solche Einbettung J_p künftig konstruiert werden kann
- dass die GNS-Struktur des BC-Systems für eine modulare Randvektoranalyse
  grundsätzlich geeignet wäre, sobald Y_p hilbertraumseitig verortet ist
- dass NEU-014 für den Teilknoten [O-229-2a-i.1] (GNS-Typen) nach
  zusätzlicher Ausarbeitung der GNS-Konstruktion nutzbar wird

---

## 6. Hauptbefund

```
[O-229-2a-i.2]  ✓[M]_neg,Quelle

NEU-014 definiert:
  – das C*-dynamische System (A_{2D}^r, φ_β, σ_t)              ✓[M]
  – KMS_β-Zustände explizit                                     ✓[M]
  – Partitionsfunktion Z(β) = ζ(β)                              ✓[M]

NEU-014 definiert nicht:
  – Y_p = Ran T_p^raw^‾ als Objekt                             ✗
  – J_p : Y_p → H_{φ_β}                                        ✗
  – modulare Invarianz U_t^φ J_p(Y_p) ⊆ J_p(Y_p)              ✗
  – Fixraumklassifikation Y_p^{U^φ}                             ✗

Konsequenz für [O-229-2a-i]:
Der modulare Ergodizitätspfad als gegenwärtige Quelle für b_p ist
✓[M]_neg,Quelle zu schließen.

Umfangsklausel: Weder modulare Randvektoren allgemein noch eine
künftig konstruierte GNS-Rohzielraum-Brücke sind damit ausgeschlossen.
```

---

## 7. DAG-Aktualisierung

| Knoten | Befund |
|---|---|
| [O-229-2a-i.1] | GNS-System (A, φ_β, σ_t): ✓[M] aus NEU-014; H_{φ_β} als explizites GNS-Objekt: nicht konstruiert → `?[O]_Quelle` |
| **[O-229-2a-i.2]** | Keine Brücke J_p : Y_p → H_{φ_β} in NEU-014 → **`✓[M]_neg,Quelle`** |
| [O-229-2a-i.3–6] | Quellenblockiert durch i.2 → nicht prüfbar |
| **[O-229-2a-i]** | Modularer Ergodizitätspfad als Quelle für b_p → **`✓[M]_neg,Quelle`** |

---

*Datei: `NEU-235_O229-2a-i_GNS_Typisierung_Rohzielraum_Einbettung.md` | Erstellt: 27. Juli 2026*
