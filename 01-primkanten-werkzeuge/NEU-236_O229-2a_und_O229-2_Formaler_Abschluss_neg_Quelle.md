# NEU-236: Formaler Abschluss [O-229-2a] und [O-229-2]

> Datum: 27. Juli 2026 | Status: ✓[M]_neg,Quelle — alle auditierten Pfade geschlossen; Quantor auf gegenwärtigen Primärquellenbestand beschränkt

---

## 1. Abschluss des Symmetrie-Elternknotens [O-229-2a]

Knoten: **[O-229-2a-canonical-vector-from-existing-symmetries]**

Gesucht war: Eine bereits vorhandene Symmetrie- oder Graduierungsstruktur, die einen
kanonischen, nichtverschwindenden Randvektor

```
b_p ∈ Ran T_p^raw‾
```

auswählt. Drei Pfade wurden vollständig auditiert:

### Pfad i — Modulare / KMS-Symmetrie

NEU-014 konstruiert das C*-dynamische System (A, φ_β, σ_t) quellengemäß.
Keine quellendefinierte Abbildung

```
J_p : Y_p = Ran T_p^raw‾  ⟶  H_{φ_β}
```

existiert in NEU-014. Damit sind weder eine modulare Wirkung auf Y_p noch ein
Fixraum Y_p^{σ^φ} typisiert. Der GNS-/modulare Fixvektorpfad kann nicht auf
den Randvektorraum übertragen werden.

```
[O-229-2a-i]   ✓[M]_neg,Quelle    (NEU-235)
```

### Pfad ii — Wres-/Hochschild-Äquivarianz

Die N×-Wirkung aus NEU-017 lebt auf dem Hochschild-Korrekturmodul M = ker∂,
nicht auf Y_p. Innerhalb des invarianten Sektors gilt:

```
(M_1)^{N×} ⊆ ker Wres_BC^{(2,0)}
```

Die N×-invariante Hochschild-Struktur zeichnet keine nichttriviale doppelte
Wres-Klasse aus. NEU-041 liefert keine typkorrekte, äquivariante und
hebungsunabhängige Brücke M_1 ↔ Y_p. Der kanonische Kopplungsoperator

```
C_p : ℂε_p ⟶ H_{J,N}
```

ist über den gewählten Lift ε̂_p definiert; seine Hebungsunabhängigkeit im
Wres-Quotienten bleibt eine offene Voraussetzung, die er nicht selbst begründen kann.

```
[O-229-2a-ii]  ✓[M]_neg,Quelle    (NEU-231, NEU-232)
```

### Pfad iii — Ladungsgraduierung

Die vorhandene Ladungszerlegung auf dem Hochschild-/Kochankomplex definiert
keinen Hilbertraumprojektor P_ch → Y_p. Nicht quellenmäßig konstruiert:
- P_ch Y_p
- P_ch N_{Wres,rel} ⊆ N_{Wres,rel}
- Multiplizität eines geladenen Quotientensektors
- Kanonische Norm- und Phasenwahl in einem solchen Sektor

```
[O-229-2a-iii] ✓[M]_neg,Quelle    (NEU-234)
```

### Befund [O-229-2a]

```
┌─────────────────────────────────────────────────────────────────────────┐
│  [O-229-2a-canonical-vector-from-existing-symmetries]                   │
│                                                                         │
│  ✓[M]_neg,Quelle                                                        │
│                                                                         │
│  Alle drei Symmetriepfade (modular/KMS, Wres-äquivariant,               │
│  ladungsgraduiert) sind im gegenwärtigen Quellenbestand geschlossen.    │
│                                                                         │
│  Umfang: Geschlossen ist nur die Konstruktion aus den gegenwärtig       │
│  definierten Symmetriestrukturen. Nicht ausgeschlossen: zusätzliche     │
│  Randdaten, neu konstruierte Brückenabbildungen, kontrollierte          │
│  Symmetriebrechung.                                                     │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Kumuliertes Ergebnis für [O-229-2]

Knoten: **[O-229-2-intrinsic-source-of-mixed-boundary-vector]**

Gesucht war eine intrinsisch ausgezeichnete Quelle für

```
b_p ∈ Ran T_p^raw‾,   |b_p| ≤ 1
```

bzw. für das Mischfunktional √α_p ⟨b_p, T_p^raw k⟩.

### A. Rohkopplung selbst

Aus T_p^raw e_p = 0 folgt:

```
B_p^raw(e_p, k) = 0   ⟹   b_p = 0,  β_p = 0.
```

Die reine Rohkopplung liefert keinen nichtverschwindenden Randvektor.

### B. Kandidatenquellen im Primärbestand

Keine Primärformel für einen nichtverschwindenden Mischblock wurde gefunden aus:
- verbundener Wres-Randpaarung
- Polarisierung einer verbundenen quadratischen Form
- KMS- oder modularem Randterm
- Kopplung mit L_3^∘
- Ableitung oder Variation der Rohkopplungsform
- Feshbach-Selbstenergie oder Weyl-Funktion
- Hochschild-/zyklischer Paarung
- Primkanalprojektion oder bedingter Erwartung

### C. Symmetriegestützte Kanonisierung

Auch eine nachträgliche kanonische Auswahl von b_p durch vorhandene Symmetrien
scheitert im gegenwärtigen Quellenbestand:
- keine modulare Wirkung auf Y_p (NEU-235)
- keine Wres-äquivariante Brücke zum Hochschild-Fixsektor (NEU-232)
- keine Hilbertraum-Ladungsprojektion auf Y_p (NEU-234)
- keine kanonische Norm- oder Phasenwahl
- keine nachgewiesene nichttriviale Wres-Klasse eines ausgezeichneten Vektors

### D. Zirkularität des Feshbach-Rückwegs

Eine Definition von b_p aus dem Feshbach-Transfer

```
V_p* (D_rel - z)^{-1} V_p
```

ist zirkulär: Der Kopplungsoperator V_p setzt eine wohldefinierte geladene
Hebung und deren Quotientenunabhängigkeit voraus. Der Feshbach-Transfer kann
nicht rückwärts die Liftgeometrie definieren, von der seine Wohldefiniertheit
abhängt.

### Auditurteil

```
┌─────────────────────────────────────────────────────────────────────────┐
│  [O-229-2-intrinsic-source-of-mixed-boundary-vector]                    │
│                                                                         │
│  ✓[M]_neg,Quelle                                                        │
│                                                                         │
│  Im vollständig auditierten Primärquellenbestand existiert gegenwärtig  │
│  keine typkorrekte und nichtzirkuläre Konstruktion eines                │
│  nichtverschwindenden intrinsischen Randvektors                         │
│      b_p ∈ Ran T_p^raw‾                                                │
│  oder eines entsprechenden Mischfunktionals                             │
│      β_p : K_p ⟶ ℂ.                                                    │
│                                                                         │
│  Quantor: Beschränkt auf die gegenwärtig vorhandene Primärarchitektur   │
│  und die vollständig auditierten Quellenpfade.                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Umfangsklausel

Dieser Befund beweist **nicht**, dass für Objekt X grundsätzlich kein
nichtverschwindender intrinsischer Mischblock existieren kann.

Quellenseitig geschlossen ist ausschließlich die Konstruktion eines solchen
Mischblocks aus der gegenwärtig vorhandenen:
- Wres-Struktur
- Hochschild-/zyklischen Struktur
- KMS-/Modularstruktur
- Ladungsgraduierung
- L_3^∘-Rohkopplung
- Primkanalprojektion
- NEU-041-Kopplungsarchitektur
- Feshbach-/Weyl-Schicht

Eine neue Primärstruktur würde den Knoten nur dann wieder öffnen, wenn sie
vor der Liftwahl definiert ist und explizit liefert:

```
b_p ∈ Ran T_p^raw‾,   0 < |b_p| ≤ 1,   b_p ∉ N_{Wres,rel},
```

sowie einen typkorrekten und quotientenverträglichen Mischblock
√α_p ⟨b_p, T_p^raw k⟩.

---

## 3. Vollständiger DAG-Stand [O-229-2]

| Knoten | Befund | Quelle |
|---|---|---|
| [O-229-2a-i] — Modular/KMS | `✓[M]_neg,Quelle` | NEU-235 |
| [O-229-2a-ii] — Wres-Äquivarianz | `✓[M]_neg,Quelle` | NEU-231/232 |
| [O-229-2a-iii] — Ladungsgraduierung | `✓[M]_neg,Quelle` | NEU-234 |
| **[O-229-2a]** — Symmetrie-Elternknoten | **`✓[M]_neg,Quelle`** | NEU-236 |
| Rohkopplung (b_p = 0) | `✓[M]` | NEU-229 |
| Kandidatenquellen (alle Pfade) | `✓[M]_neg,Quelle` | NEU-230–235 |
| Feshbach-Rückweg | zirkulär | NEU-228 |
| **[O-229-2]** — Hauptknoten | **`✓[M]_neg,Quelle`** | NEU-236 |

---

## 4. Hauptlinie nach Abschluss

| Thema | Status |
|---|---|
| Rohkopplungs-Kernblock | `✓[M]_part` |
| Positivitätsklassifikation | `✓[M]` |
| Intrinsischer Mischblock aus vorhandenen Quellen | `✓[M]_neg,Quelle` |
| Zusätzliches minimales Randdatum | `?[O]` → [O-229-3] |

Firewall gewahrt: Hebungsunabhängigkeit und Feshbach-Wohldefiniertheit dürfen
erst nach einer tatsächlich konstruierten Liftgeometrie behauptet werden.

---

*Datei: `NEU-236_O229-2a_und_O229-2_Formaler_Abschluss_neg_Quelle.md` | Erstellt: 27. Juli 2026*
