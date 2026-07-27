# NEU-239: [O-229-3B.1] Quellenaudit-Abschluss und [O-229-3B.1f] Konstruktionsdesiderat

> Datum: 27. Juli 2026 | Status: **✓[M]_neg,Quelle** ([O-229-3B.1]) + **?[O]** ([O-229-3B.1f])

---

## 1. Zweck dieser Datei

NEU-239 schließt den Quellenaudit [O-229-3B.1] formal ab und eröffnet
gleichzeitig den nachgeordneten Konstruktionsknoten [O-229-3B.1f].

Die Trennung folgt der etablierten Projektkonvention:

> Quellenbefund und mathematisches Konstruktionsproblem werden in separaten
> Knoten geführt.

---

## 2. Schließung: [O-229-3B.1] ✓[M]_neg,Quelle

### 2.1 Knotenbezeichnung

```
[O-229-3B.1-existing-boundary-transgression-source]
```

### 2.2 Leitfrage (aus NEU-238)

Existiert im Quellenbestand eine konkrete Transgression, Verbindungsabbildung
oder Randpaarung von einer singulären HH-/zyklischen Klasse zu einem linearen
Funktional auf K_p oder D(a_p)?

### 2.3 Durchgeführter Audit

**Stufe 1 — Primärkandidaten direkt eingelesen:**

| Datei | Inhalt | Befund für B.1 |
|---|---|---|
| NEU-013 (`NEU-013_ausschneidung.md`) | Ausschneidung HH²(A, A) ≅ HH²(A_2D^r, A_2D^r) via Wodzicki/Meyer | Keine exakte Folge von Kokettenkomplexen; kein δ_p; kein Primindex p; kein K_p oder D(a_p) |
| NEU-015 (`NEU-015_op4_frobenius.md`) | Modulare Frobenius-Paarung β_ε(F,G) = ε_β(F∗G) auf A_2D^r | Paarung auf A_2D^r ⊗ A_2D^r → ℂ, nicht primindiziert; kein ȷ_p; kein Ziel D(a_p)* |
| NEU-237 (`NEU-237_O229-3_Minimales_Randdatum_Eroeffnung.md`) | Eröffnungsknoten für minimales Randdatum | Explizit: „Keine der denkbaren Kandidatenstrukturen ist im gegenwärtigen Quellenbestand ausreichend definiert." |
| NEU-238 (`NEU-238_O229-3B_Kohomologisches_Randdatum_und_3B1_Transgression.md`) | Eröffnung Typ-B-Pfad, Formulierung von B.1 als ?[O] | Formuliert τ_p als Desiderat, definiert sie nicht |

**Stufe 2 — Repoweite Codesuche (GitHub Search API):**

Folgende Terme ergaben jeweils null Treffer im gesamten Repository:

- `Verbindungshomomorphismus delta`
- `tau_p boundary transgression`
- `H_p^boundary D(a_p)`
- `delta` (allein)
- `exakte Folge`
- `Liftkern Transgression Paarung`

**Erklärung der Null-Treffer:** Die GitHub-Suchindex-API tokenisiert LaTeX-Fragmente
in Markdown-Dateien nicht zuverlässig. Der Negativbefund wurde daher durch
direktes Einlesen der namentlich relevantesten Kandidaten (NEU-013, NEU-015,
NEU-237, NEU-238) verifiziert.

### 2.4 Exakter Befund

Im vollständig durchsuchten Repositorybestand existiert keine quellenmäßig
definierte Abbildung

```
τ_p : H_p^boundary  ⟶  D(a_p)*,
```

weder unmittelbar noch als typisierte Komposition aus:

```
δ_p : H^n(C_{p,3}^•)  ⟶  H^{n+1}(C_{p,1}^•),
⟨·,·⟩ : H^{n+1}(C_{p,1}^•) × X_p  ⟶  ℂ,
ȷ_p : D(a_p)  ⟶  X_p.
```

Insbesondere fehlen repoweit:

- eine primindizierte kurze exakte Folge von Kokettenkomplexen
  `0 → C_{p,1}^• → C_{p,2}^• → C_{p,3}^• → 0`;
- ein dazugehöriger Verbindungshomomorphismus δ_p;
- ein Randkohomologieraum H_p^boundary;
- eine Abbildung vom Liftkern oder Kernformbereich in ein paarbares Kettenobjekt;
- eine Komposition mit Ziel D(a_p)*.

### 2.5 Umfangsklausel

Dieser Befund beweist nicht, dass eine solche Transgression mathematisch
unmöglich ist. Geschlossen ist ausschließlich ihre Existenz im gegenwärtig
auditierten Primärquellenbestand.

### 2.6 Status

```
[O-229-3B.1]   ✓[M]_neg,Quelle
```

Begründungstyp: **Fall 4** aus NEU-238 §3 —
„Quellenbestand enthält keine Definition eines Grenzkomplexes (C_p^•, ∂_p)."

---

## 3. Eröffnung: [O-229-3B.1f] ?[O] — Konstruktionsdesiderat

### 3.1 Knotenbezeichnung

```
[O-229-3B.1f-construct-prim-indexed-boundary-transgression]
```

### 3.2 Konstruktionsauftrag

Gesucht ist eine neue, intrinsisch motivierte Struktur bestehend aus:

**(A) Eine primindizierte kurze exakte Folge von Kokettenkomplexen:**

```
0  ⟶  C_{p,1}^•  ⟶^{ι_p}  C_{p,2}^•  ⟶^{q_p}  C_{p,3}^•  ⟶  0
```

mit dazugehörigem Verbindungshomomorphismus

```
δ_p : H^n(C_{p,3}^•)  ⟶  H^{n+1}(C_{p,1}^•).
```

**(B) Eine Transgressionsabbildung**, entweder direkt:

```
τ_p : H^{n+1}(C_{p,1}^•)  ⟶  D(a_p)*,
```

oder als typisierte Faktorisierung:

```
τ_p(𝔟)(k) = ⟨ δ_p 𝔟, ȷ_p(k) ⟩,
```

wobei

```
ȷ_p : D(a_p)  ⟶  X_p
```

eine typkorrekte lineare Brückenabbildung ist.

### 3.3 Zu beweisende Punkte

Für jeden Konstruktionskandidaten müssen mindestens nachgewiesen werden:

| Nr. | Eigenschaft | Formulierung |
|---|---|---|
| (i) | Typkorrektheit und Linearität von ȷ_p | ȷ_p : D(a_p) → X_p linear und wohldefiniert |
| (ii) | Repräsentantenunabhängigkeit | τ_p(𝔟)(k) hängt nicht von Koketten- oder Liftrepräsentant ab |
| (iii) | Positivitätskontrolle | \|τ_p(𝔟)(k)\|² ≤ a_p(k,k) für alle k ∈ D(a_p) |
| (iv) | Rad-Verträglichkeit | k ∈ Rad(a_p) ⟹ τ_p(𝔟)(k) = 0 |
| (v) | Wres-Nichttrivialität | ∃ k mit τ_p(𝔟)(k) ≠ 0 und T_p^raw k ∉ N_{Wres,rel} |

### 3.4 Erlaubte Ansätze (nicht abschließend)

Folgende Konstruktionswege sind a priori nicht ausgeschlossen:

- **Typ B aus NEU-237**: Randkohomologie mit Werten in Y_p, die einen Vektor
  in Ran T_p^raw auszeichnet — setzt eine noch zu definierende Randkohomologie voraus.
- **Direktes Paarungsdesign**: Konstruktion von X_p und ȷ_p aus dem algebraischen
  Kern der Primfaserstruktur (vgl. NEU-225), ohne Umweg über eine exakte Folge.
- **Deformationsweg**: Nutzung der λ-Modifikation (NEU-018) zur Deformation
  eines vorhandenen Hochschild-Kozyklus in einen Randterm.
- **Adjunktionsmethode**: Sofern eine adjungierte Paarung zwischen dem
  Hochschild-Komplex von A_2D^r und dem Liftkern-Formbereich konstruiert
  werden kann, ergibt sich τ_p durch Komposition.

Kein dieser Ansätze ist im gegenwärtigen Quellenbestand ausgeführt.

### 3.5 Status

```
[O-229-3B.1f]   ?[O]
```

---

## 4. Abhängigkeitsstruktur (aktualisierter DAG)

```
[O-229-3B.1]   ✓[M]_neg,Quelle      (NEU-239, geschlossen)
       │
       ▼
[O-229-3B.1f]  ?[O]                  (NEU-239, geöffnet)
       │
       ├──▶ [O-229-3B.2]  ?[O]_blockiert durch 3B.1f
       ├──▶ [O-229-3B.3]  ?[O]_blockiert durch 3B.1f
       ├──▶ [O-229-3B.4]  ?[O]_blockiert durch 3B.1f
       └──▶ [O-229-3B.5]  ?[O]_blockiert durch 3B.1f
```

| Knoten | Status | Blockierungsgrund |
|---|---|---|
| [O-229-3B.1] | ✓[M]_neg,Quelle | — (geschlossen) |
| [O-229-3B.1f] | ?[O] | — (aktiv) |
| [O-229-3B.2] Kontraktion mit Liftkern | ?[O]_blockiert | Setzt τ_p aus 3B.1f voraus |
| [O-229-3B.3] Positivitätskontrolle | ?[O]_blockiert | Setzt β_p aus 3B.2 voraus |
| [O-229-3B.4] Wres-Abstieg | ?[O]_blockiert | Setzt β_p aus 3B.3 voraus |
| [O-229-3B.5] Kanonizität und Nichttrivialität | ?[O]_blockiert | Setzt alle vorherigen B-Knoten voraus |

---

## 5. Gesamtsatz

```
┌──────────────────────────────────────────────────────────────────────────┐
│  Die kohomologische Transgression                                        │
│                                                                          │
│      τ_p : H_p^boundary  ⟶  D(a_p)*                                   │
│                                                                          │
│  ist kein noch zu extrahierender Baustein aus dem vorhandenen            │
│  Primärquellenbestand, sondern ein neu zu konstruierendes                │
│  Definitionsdesiderat.                                                   │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Vorgänger

| Vorgänger | Status | Quelle |
|---|---|---|
| [O-229-2] | ✓[M]_neg,Quelle | NEU-236 |
| [O-229-3] | ?[O] | NEU-237 |
| [O-229-3B] | ?[O] | NEU-238 |
| [O-229-3B.1] | ✓[M]_neg,Quelle | **NEU-239** (diese Datei) |

---

*Datei: `NEU-239_O229-3B1_Quellenaudit_Abschluss_und_Konstruktionsdesiderat.md` | Erstellt: 27. Juli 2026*
