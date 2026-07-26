# NEU-175 — Gewichtraumkomplex und geladener Kettenprojektor der BC-Zeitwirkung

## Vorbemerkung: Drei Korrekturen an NEU-174

Vor Konstruktion des Gewichtraumkomplexes sind drei Präzisierungen aus der Durchsicht von NEU-174 einzuarbeiten.

### K1 — B₃ ist Modellwahl, keine Identifikation

Der Status [O-174-1] ✓[K] ist korrekt, sofern [K] "neu konstruiert" bedeutet. Daraus folgt jedoch nicht B₃^ursprünglich = A_Q. Die präzise Aussage lautet:

> **B₃^mod := A_Q** liefert einen wohldefinierten Modellkomplex.

Alle Konstruktionen in NEU-174 und diesem Dokument beziehen sich auf **B₃^mod**, nicht auf ein unabhängig verifiziertes "ursprüngliches" B₃. Offen bleibt:

> **[O-174-1c]** ?[O]: Realisiert B₃^mod das ursprünglich mit [L₃] gemeinte Objekt?

Insbesondere ist noch keine Verbindung zur früheren Filtrationsnotation F³A_BC^an hergestellt. Der Komplex ist mathematisch legitim; seine Herkunftstreue bleibt offen und wird nicht in diesem Dokument entschieden.

### K2 — Terminologiekorrektur: reguläres statt symmetrisches Bimodul

Für M_untw = B₃ mit a·m = am, m·a = ma ist die korrekte Bezeichnung das **reguläre Bimodul** (Links- und Rechtswirkung durch die Algebramultiplikation selbst gegeben). "Symmetrisches Bimodul" würde a·m = m·a für alle a, m implizieren, was bei nichtkommutativem B₃ im Allgemeinen falsch ist. Diese Korrektur ist rein terminologisch und ändert keine Konstruktion aus NEU-174.

### K3 — Zusätzliche Kommutationsbedingung für die verdrehte Zeitwirkung

Für M_σ = _id B_{3,σ} muss α_t^M mit der verdrehten Rechtswirkung verträglich sein:

```
α_t^M(m · a) = α_t^M(m) · α_t(a)
```

Setzt man α_t^M = α_t, ergibt die linke Seite α_t(mσ(a)) = α_t(m)·α_t(σ(a)), während die rechte Seite α_t(m)·σ(α_t(a)) liefert. Daraus folgt die notwendige Bedingung:

> **α_t ∘ σ = σ ∘ α_t**

Ohne diese Bedingung ist α_t^C auf dem verdrehten Komplex **nicht notwendig wohldefiniert**. Falls σ = α_{iβ} (analytische Fortsetzung der Zeitwirkung, KMS-artig) gemeint ist, ist die Kommutation formal plausibel, muss aber inklusive Definitionsbereich separat festgehalten werden.

**Neuer Unterknoten:**

> **[O-174-4σ]:** α_t σ = σ α_t.

Dieser Knoten ist Voraussetzung für [O-174-4] im verdrehten Fall M_σ und wird hier als offen bzw. modellabhängig zu prüfen geführt: **?[O]** (sofern σ nicht explizit als α_{iβ} mit gesichertem Definitionsbereich festgelegt wird).

---

## Korrigierter Status von [O-174-4] bis [O-174-6]

Die in NEU-174 behauptete volle Fourierzerlegung von C• folgt **nicht** allein aus bα_t^C = α_t^C b. Die BC-Zeitentwicklung ist eine R-Wirkung (keine periodische Kreiswirkung); ihre natürlichen Frequenzen sind typischerweise log n bzw. Kombinationen solcher Werte. Für eine direkte Fourierzerlegung fehlen zunächst: Topologie, Stetigkeit, Spektralbegriff, Abschlusskonvention.

**Korrigierte Statustabelle:**

| Knoten | Status |
|---|---|
| [O-174-4] | ✓[K] unter den Modulkompatibilitäten (inkl. [O-174-4σ] im verdrehten Fall) |
| [O-174-5] | ✓[K] |
| [O-174-6] | ?[O] bzw. ✓[K]_fin auf einem expliziten Modalkomplex — **nicht** vollständig aus [O-174-5] ableitbar |

### Drei mögliche Konstruktionsrouten für [O-174-6]

1. **Algebraische Gewichtraumroute:** B_{3,λ} = {a ∈ B₃ : α_t(a) = e^{itλ}a}; liefert echten Unterkomplex (C_λ•, b), aber offen bleibt, ob alle Kochains endliche Summen solcher Eigenkochains sind.
2. **Spektrale Route:** Nach Hilbert-/Banach-Vervollständigung via Stone- bzw. Arveson-Spektraltheorie; liefert i.A. kein diskretes direktes Summensystem, sondern Spektralunterräume oder ein Projektionsmaß.
3. **Formale Fourierroute (gewählt in diesem Dokument):** Beschränkung auf C_fin• = span{homogene Eigenkochains}, worauf P^ch algebraisch wohldefiniert ist.

Dieses Dokument verfolgt Route 3 als kleinste kontrollierbare Konstruktion.

---

## Konstruktion des Gewichtraumkomplexes

### [O-175-1] — C_fin• als algebraischer Eigenkochainkomplex

Für λ ∈ R definieren wir den Eigenraum:

```
C^n_λ := { φ ∈ C^n(B₃^mod, M) : α_t^C φ = e^{itλ} φ  für alle t }
```

und den algebraischen Gewichtraumkomplex als endliche direkte Summe:

```
C_fin^n := ⊕_{λ ∈ Λ} C^n_λ
```

wobei Λ ⊂ R eine (a priori beliebige, später konkret zu spezifizierende) endliche oder abzählbare Menge von Gewichten ist, für die C^n_λ ≠ 0 gilt und nur endlich viele Summanden ungleich null vorkommen.

**Status:** ✓[K]_fin — als algebraische Definition wohldefiniert, sofern man sich auf endliche Summen beschränkt. Die Frage, ob C_fin• = C• gilt (Vollständigkeit der Zerlegung), bleibt **?[O]** und wird hier nicht behauptet.

### [O-175-2] — b respektiert die Gewichträume

**Behauptung:** φ ∈ C^n_λ ⇒ bφ ∈ C^{n+1}_λ.

**Beweis:** Aus [O-174-5] (bα_t^C = α_t^C b) folgt:

```
α_t^C(bφ) = b(α_t^C φ) = b(e^{itλ}φ) = e^{itλ}(bφ)
```

Also ist bφ ebenfalls Eigenvektor zum Eigenwert e^{itλ}, d.h. bφ ∈ C^{n+1}_λ. ✓

Somit gilt b(C^n_fin,λ) ⊆ C^{n+1}_fin,λ, und (C_fin^•, b) zerfällt in eine direkte Summe von Unterkomplexen (C_λ^•, b) für λ ∈ Λ.

**Status:** ✓[K]

### [O-175-3] — Der geladene Kettenprojektor P^ch

Auf C_fin^• definieren wir die Projektion auf den Nicht-Nullgewicht-Anteil:

```
P^ch := Σ_{λ ≠ 0} P_λ
```

wobei P_λ: C_fin^• → C^•_λ ⊂ C_fin^• die kanonische Projektion auf den λ-Eigenraum ist (P_λ ist wohldefiniert, da C_fin^• nach Konstruktion eine endliche direkte Summe der C^•_λ ist).

**Status:** ✓[K] — auf C_fin^• algebraisch wohldefiniert (nicht auf dem vollen C^•, dort bliebe P^ch ?[O]).

### [O-175-4] — Kommutation von P^ch mit b

**Behauptung:** b P^ch = P^ch b (auf C_fin^•).

**Beweis:** Für φ = Σ_λ φ_λ (endliche Summe, φ_λ ∈ C^n_λ):

```
b(P^ch φ) = b(Σ_{λ≠0} φ_λ) = Σ_{λ≠0} bφ_λ
```

Nach [O-175-2] ist bφ_λ ∈ C^{n+1}_λ. Also:

```
Σ_{λ≠0} bφ_λ = P^ch(Σ_λ bφ_λ) = P^ch(bφ)
```

(da bφ_0 ∈ C^{n+1}_0 im λ=0-Anteil verbleibt und von P^ch annulliert wird). Damit b P^ch φ = P^ch b φ. ✓

**Status:** ✓[K] — direkte Konsequenz aus [O-175-2], hier vollständig auf C_fin^• bewiesen (nicht bloß postuliert wie in der ursprünglichen Sperrlogik von NEU-174 befürchtet).

### [O-175-5] — Induzierte Abbildung auf Kohomologie

Da b P^ch = P^ch b, bildet P^ch Kozykel auf Kozykel und Koränder auf Koränder ab. Damit ist die induzierte Abbildung

```
[P^ch]: H^•(C_fin) → H^•(C_fin),   [P^ch]([φ]) := [P^ch φ]
```

wohldefiniert (unabhängig vom gewählten Repräsentanten φ der Klasse [φ]).

**Status:** ✓[K]

---

## DAG-Knotenübersicht NEU-175

| Knoten | Inhalt | Status |
|---|---|---|
| [O-174-1c] | Realisiert B₃^mod das ursprünglich gemeinte Objekt? | ?[O] |
| [O-174-4σ] | α_t σ = σ α_t | ?[O] (modellabhängig) |
| [O-175-1] | C_fin• als algebraischer Eigenkochainkomplex | ✓[K]_fin |
| [O-175-2] | b(C^n_fin,λ) ⊆ C^{n+1}_fin,λ | ✓[K] |
| [O-175-3] | P^ch = Σ_{λ≠0} P_λ auf C_fin• | ✓[K] |
| [O-175-4] | b P^ch = P^ch b | ✓[K] |
| [O-175-5] | [P^ch]: H•(C_fin) → H•(C_fin) | ✓[K] |

---

## Korrigierte konstruktive Kette

```
B₃^mod ⟶ M ⟶ (C•, b) ⟶ α_t^C ⟶ C_fin• ⟶ P^ch ⟶ [L₃]_ch
```

Erst nach Abschluss dieser Kette folgt die Suche nach einem konkreten Kandidaten:

```
L₃ ∈ Z⁴(C_fin•)
```

und die Prüfung der Nichtverschwindensbedingung:

```
[P^ch]([L₃]) ≠ 0
```

Die Operatorrealisierung ρ_op: Z⁴(B₃,M) → End(H) folgt weiterhin erst **nach** dieser kohomologischen Nichtverschwindensentscheidung und ist Gegenstand eines eigenen Folgeknotens (voraussichtlich NEU-176).

---

## Zusammenfassung der offenen Fragen

| Frage | Status |
|---|---|
| Realisiert B₃^mod das ursprüngliche Objekt? | ?[O] |
| α_t ∘ σ = σ ∘ α_t im verdrehten Modell? | ?[O] |
| Ist C_fin• = C• (vollständige Zerlegung)? | ?[O] |
| Existiert L₃ ∈ Z⁴(C_fin•) mit [P^ch]([L₃]) ≠ 0? | ?[O] — Gegenstand des nächsten Konstruktionsschritts |
