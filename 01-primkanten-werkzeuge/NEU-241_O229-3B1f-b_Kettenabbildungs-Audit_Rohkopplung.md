# NEU-241: [O-229-3B.1f-b] Kettenabbildungs-Audit — Erweiterung von T_p^raw zu einer Kettenabbildung

> Datum: 27. Juli 2026 | Status: **?[O]**

---

## 1. Einordnung

NEU-240 hat Typ III (Mapping-Cone-Konstruktion) als strukturell stärksten
Kandidaten für die Faktorisierungsbedingung

```
β_p = Λ_p ∘ T_p^raw
```

identifiziert. Ein Mapping Cone ist jedoch nur dann kohomologisch definiert,
wenn eine echte Kettenabbildung vorliegt. Der vorliegende Knoten

```
[O-229-3B.1f-b-chain-map-lift-of-raw-coupling]
```

klärt die logisch vorgelagerte Frage:

> Besitzt T_p^raw überhaupt eine quellenmäßig definierte Erweiterung
> zu einer Kettenabbildung zwischen zwei tatsächlich definierten Komplexen?

Dies ist die minimale Schwelle, an der sich entscheidet, ob Typ III eine
echte kohomologische Architektur oder nur eine formal attraktive Notation ist.

---

## 2. Vier atomare Teilfragen

### b.1 — Quell- und Zielkomplex

Gesucht sind explizit definierte Komplexe

```
(C_{p,lift}^•, d_lift)   und   (C_{p,tar}^•, d_tar)
```

mit:

```
D(a_p) ⊆ C_{p,lift}^r      (für einen explizit bestimmten Grad r)
Ran T_p^raw ⊆ C_{p,tar}^{r+s}   (Grad r+s, Verschiebung s explizit)
```

**Bedingungen:**
- Weder Grad r noch Verschiebung s dürfen aus der Bezeichnung L_3^∘ oder
  einer anderen bereits bekannten Notation erraten werden.
- Die Differenziale d_lift und d_tar müssen quellenmäßig definiert sein,
  nicht nur postuliert.
- D(a_p) muss als Gradstück von C_{p,lift}^• erscheinen, nicht nur als
  abstrakter Definitionsbereich.

**Entscheidungsfrage:** Existieren im Repo oder aus dem algebraischen Gerüst
(A_{2D}^r, a_p, T_p^raw, N_{Wres,rel}) natürliche Komplexkandidaten für
Quell- und Zielseite?

---

### b.2 — Erweiterung von T_p^raw zur Kettenabbildung

Gesucht ist eine Abbildung auf allen Graden

```
Τ_p^• : C_{p,lift}^•  ⟶  C_{p,tar}^{•+s}
```

deren relevante Komponente mit der Rohkopplung übereinstimmt:

```
Τ_p^r |_{D(a_p)} = T_p^raw
```

und die die Kettenrelation erfüllt:

```
d_tar ∘ Τ_p = (-1)^s Τ_p ∘ d_lift
```

**Warum die Kettenrelation unverhandelbar ist:**
Ohne sie existiert kein Mapping Cone im kohomologischen Sinn. Das Objekt

```
Cone(Τ_p)^n = C_{p,tar}^n ⊕ C_{p,lift}^{n+s+1}
```

mit dem Differential

```
D_Cone(v, w) = (d_tar v + (-1)^s Τ_p w,  -d_lift w)
```

ist nur dann ein Komplex (D_Cone^2 = 0), wenn die Kettenrelation gilt.

**Entscheidungsfrage:** Kann T_p^raw zu einer solchen Kettenabbildung auf
den natürlichen Quell- und Zielkomplexen ergänzt werden?

---

### b.3 — Wres-Quotientenverträglichkeit

Für den Quotientenkomplex

```
C_{p,tar}^• / N_{Wres,rel}^•
```

muss gelten:

**(i) N_{Wres,rel}^• ist Unterkomplex:**
```
d_tar N_{Wres,rel}^n ⊆ N_{Wres,rel}^{n+1}
```

**(ii) Τ_p steigt zum Quotienten ab:**
```
Τ_p^r(k) ∈ N_{Wres,rel}^{r+s}   für alle k ∈ Rad(a_p)
```

Dieser Punkt ist stärker als die bisher verwendete Mengeninklusion

```
T_p^raw(Rad a_p) ⊆ N_{Wres,rel}
```

weil er Differentialverträglichkeit in allen Graden verlangt, nicht nur
für die nullte Komponente.

**Entscheidungsfrage:** Trägt der Zielkomplex eine Unterkomplexstruktur
für N_{Wres,rel}?

---

### b.4 — Analytische Kontrolle: Beschränktheit von Λ_p

Selbst ein algebraisch korrekter Mapping Cone mit Kettenrelation und
Wres-Abstieg liefert noch nicht automatisch die Positivitätsschranke.
Es wird eine Kokette oder Klasse auf dem Zielkomplex benötigt, deren
Auswertung ein beschränktes Funktional

```
Λ_p : Ran T_p^raw̅  ⟶  ℂ,   ||Λ_p|| ≤ √α_p
```

erzeugt. Dann gilt automatisch:

```
|β_p(k)|² = |Λ_p(T_p^raw k)|² ≤ α_p ||T_p^raw k||² = a_p(k,k).
```

**Warum Beschränktheit nicht aus der Kettenstruktur folgt:**
Eine Kohomologieklasse [z] ∈ H^n(C_{p,tar}^•) ist eine algebraische Klasse.
Die Auswertung [z](v) für v ∈ Ran T_p^raw ist ein lineares Funktional,
aber ohne zusätzliche topologische Kontrolle nicht notwendig beschränkt.
Die Schranke ||Λ_p|| ≤ √α_p erfordert entweder:
- eine Hilbertraum- oder Banachraum-Norm auf C_{p,tar}^{r+s} mit expliziter
  Abschätzung, oder
- eine kanonische Auswahl von z, die geometrisch/analytisch normkontrolliert ist.

**Entscheidungsfrage:** Gibt es eine natürliche Norm oder inneres Produkt
auf C_{p,tar}^{r+s}, das die Beschränktheitsschranke liefert?

---

## 3. Logischer Ablauf des Mapping-Cone-Pfades

```
 T_p^raw : D(a_p) ⟶ Y_p
       ↓  b.1: Quell- und Zielkomplex identifizieren
 (Τ_p^r)|_{D(a_p)} = T_p^raw
       ↓  b.2: Kettenrelation d_tar ∘ Τ_p = (-1)^s Τ_p ∘ d_lift
 Cone(Τ_p)^n = C_{p,tar}^n ⊕ C_{p,lift}^{n+s+1}
       ↓  b.3: Wres-Abstieg und Quotientenkomplex
 lange exakte Folge ⇒ Randklasse oder relative Klasse
       ↓  b.4: Beschränktheit von Λ_p
 β_p(k) = Λ_p(T_p^raw k),   |β_p(k)|² ≤ a_p(k,k)
```

---

## 4. Entscheidungsfälle

| Fall | Befund | Status |
|---|---|---|
| Kein Quell-/Zielkomplex und kein Differential für T_p^raw vorhanden | Mapping-Cone-Pfad aus vorhandener Architektur nicht zugänglich | `✓[M]_neg,Quelle` |
| Komplexe vorhanden, aber T_p^raw erfüllt Kettenrelation nicht | Mapping Cone dieser Rohkopplung ausgeschlossen (mit Umfangsklausel) | `✓[M]_neg` |
| Kettenabbildung konstruiert, aber Beschränktheit und/oder Wres-Abstieg offen | Teilresultat | `✓[M]_part` |
| Alle vier Stufen b.1–b.4 geschlossen | Mapping-Cone-Transgression vollständig | `✓[K/M]` |

---

## 5. Abhängigkeitsstruktur (aktualisierter DAG)

```
[O-229-3B.1]       ✓[M]_neg,Quelle       (NEU-239)
       │
       ▼
[O-229-3B.1f]      ?[O]                  (NEU-239)
       │
       ▼
[O-229-3B.1f-a]    ?[O]                  (NEU-240)
       │
       ▼
[O-229-3B.1f-b]    ?[O]                  (NEU-241, aktiv)
   ├─ b.1: Quell-/Zielkomplex
   ├─ b.2: Kettenabbildung Τ_p^•
   ├─ b.3: Wres-Unterkomplex und Abstieg
   └─ b.4: Beschränktheit Λ_p
       │
       ▼  (nach positivem Abschluss)
[O-229-3B.1f-b-Cone]  Cone(Τ_p) und lange exakte Folge  (noch nicht geöffnet)
```

| Knoten | Status |
|---|---|
| [O-229-3B.1f-a] | ?[O] aktiv (NEU-240) |
| [O-229-3B.1f-b] | ?[O] aktiv (NEU-241) |
| Typ-II-, Typ-I-, Typ-IV-Konstruktionen | ?[O]_blockiert bis 3B.1f-a Minimalitätsentscheid |
| [O-229-3B.2]–[O-229-3B.5] | ?[O]_blockiert bis 3B.1f positiv abgeschlossen |

---

## 6. Arbeitsstatus

```
[O-229-3B.1f-b]   ?[O]

Nächste Aufgabe: Primus-Audit der vier Teilfragen b.1–b.4.
Startpunkt: Existenz natürlicher Komplexkandidaten für
(C_{p,lift}^•, d_lift) und (C_{p,tar}^•, d_tar) aus dem
algebraischen Gerüst (A_{2D}^r, a_p, T_p^raw, N_{Wres,rel}).
```

---

*Datei: `NEU-241_O229-3B1f-b_Kettenabbildungs-Audit_Rohkopplung.md` | Erstellt: 27. Juli 2026*
