# NEU-238: [O-229-3B] Kohomologisches Randdatum und [O-229-3B.1] Quellenaudit Transgression

> Datum: 27. Juli 2026 | Status: ?[O] — Typ B logisch vorrangig; [O-229-3B.1] als erster Quellenaudit geöffnet

---

## 1. Begründung der Typ-B-Priorisierung

### 1.1 Warum Typ A nachrangig ist

Ein spektraler Randterm (Typ A) benötigt als Vorannahmen:

```
J_p : Y_p ↪ H_{D_rel}        (quellenseitig nicht konstruiert, NEU-235)
D_rel-verträgliche Struktur auf J_p(Y_p)
kanonischen Grenzwert / Randwertoperation
Rücktransport nach Y_p
```

Zusätzliche bekannte Barrieren:
- Y_p ↪ H_{D_rel} quellenseitig nicht konstruiert (NEU-235)
- D_rel besitzt rein absolut kontinuierliche Primsektoren — weder Eigenvektor
  noch Nullmodus noch diskrete spektrale Auswahl sind als kanonischer Randvektor
  verwendbar
- Ein bloßes Spektralmaß zeichnet keinen einzelnen Vektor b_p aus
- D_rel fungiert in der Übergabearchitektur als Transport- und Streugenerator,
  nicht als direkter kompakter HP-2-Operator

Typ A müsste zunächst eine neue Hilbertraumeinbettung konstruieren, bevor die
eigentliche Randdatumsfrage beginnt.

### 1.2 Warum Typ B logisch früher liegt

Ein kohomologischer Kandidat kann auf einem algebraischen gemeinsamen
Definitionsbereich formuliert werden:

```
D_p^lift,   K_p^alg,   D(a_p)
```

vor einer Hilbertraumvervollständigung und ohne spektrale Einbettung in H_{D_rel}.

Gesucht ist nicht unmittelbar ein Vektor, sondern ein kanonisches lineares Funktional

```
β_p : D(a_p) ⟶ ℂ.
```

Erst nach dem Positivitätsnachweis

```
|β_p(k)|^2 ≤ a_p(k,k)
```

liefert der Riesz-Satz einen kontraktiven Vektor b_p ∈ H_{a,p}. Das entspricht
genau der bereits bewiesenen Positivitätsklassifikation und vermeidet, b_p von
Anfang an in einen noch nicht verbundenen Hilbertraum einzusetzen.

### 1.3 Strategische Reihenfolge

```
Typ B zuerst  ⟶  Typ A nur bei negativem oder unvollständigem B-Befund.
```

Typ B prüft, ob die bereits vorhandene singuläre HH-Struktur überhaupt ein
Randfunktional auf dem Liftkern erzeugen kann. Typ A folgt nur, wenn entweder
- eine konkrete Einbettung Y_p ↪ H_{D_rel} konstruiert wird, oder
- Typ B ein Funktional liefert, dessen analytische Realisierung durch einen
  spektralen Randwert untersucht werden soll.

---

## 2. Struktur des Knotens [O-229-3B]

### B.1 — Exakter kohomologischer Quelltyp

Gesucht: ein tatsächlich definierter Komplex

```
(C_p^•, ∂_p)
```

mit einem Rand-, Transgressions- oder Verbindungsmechanismus, der ein Funktional
auf dem Liftkern liefern könnte. Minimal erforderlich:

```
τ_p : H_p^boundary  ⟶  D(a_p)*
```

quellenseitig definiert und nicht allein aus dem Wort „Randklasse“ oder der
Existenz einer HH-Klasse abgeleitet.

```
[O-229-3B.1]   ?[O]   ← erster Quellenaudit (NEU-238)
```

### B.2 — Typkorrekte Kontraktion mit dem Liftkern

Für ein ausgezeichnetes Randdatum b_p ∈ H_p^boundary müsste gelten:

```
β_p(k) := τ_p(b_p)(k)
```

Zu prüfen:
- k ↦ β_p(k) linear
- β_p unabhängig von Hilfsrepräsentanten
- Genaue Beziehung zu L_3^∘, T_p^raw oder dem primitiven Quotienten

### B.3 — Hermitizität und Positivitätskontrolle

Eine kohomologische Paarung allein genügt nicht. Erforderlich:

```
|β_p(k)|^2 ≤ a_p(k,k)   ∀ k ∈ D(a_p)
```

Für den Rohkernblock:

```
|β_p(k)|^2 ≤ α_p · ||T_p^raw k||^2
```

Insbesondere muss gelten:

```
T_p^raw k = 0  ⟹  β_p(k) = 0
```

Erst dann faktorisiert das Funktional durch den Rohkopplungsraum und erzeugt
einen Riesz-Vektor.

### B.4 — Wres-Abstieg

Zu prüfen:

```
β_p(k) = 0   für alle k ∈ Rad(a_p)
```

bzw. bei Wres-relativer Definition:

```
T_p^raw k ∈ N_{Wres,rel}  ⟹  β_p(k) = 0
```

Ohne diesen Schritt wäre das Randdatum repräsentantenabhängig.

### B.5 — Kanonizität und Nichttrivialität

Selbst bei Existenz einer Randklasse muss geklärt werden:

```
dim H_p^boundary = 1  ?
```

oder ob eine andere intrinsische Bedingung b_p auszeichnet. Zudem muss ein
konkreter Zeuge k existieren mit:

```
β_p(k) ≠ 0,   T_p^raw k ∉ N_{Wres,rel}
```

Andernfalls ist die Randklasse entweder wirkungslos oder im relevanten Quotienten
trivial.

---

## 3. Erster Quellenaudit: [O-229-3B.1]

### Knotenformulierung

```
[O-229-3B.1-existing-boundary-transgression-source]

Leitfrage:
Existiert im Quellenbestand eine konkrete Transgression, Verbindungsabbildung
oder Randpaarung von einer singulären HH-/zyklischen Klasse zu einem linearen
Funktional auf K_p oder D(a_p)?

Status: ?[O]
```

### Zu prüfende Quellen

Die folgenden Dokumente sind primär relevant für eine Transgressions- oder
Verbindungsabbildung in Richtung Liftkern:

| Quelle | Inhalt | Relevanz für B.1 |
|---|---|---|
| NEU-013 | Ausschneidung | Randsequenz, Verbindungshomomorphismus |
| NEU-015 | Frobenius / op4 | HH-Paarung, Spurstruktur |
| NEU-016 | Monoidladung / modulare Spur | Graduierung, Spurklassen |
| NEU-018 | λ-Modifikation | Deformierte Zyklen |
| NEU-019 | Wodzicki | Wres auf Zyklen |
| NEU-229 | Intrinsische verbundene Form | Mischblock-Gram-Geometrie |
| NEU-230 | Symmetrieklassifikation O-229-2a | HH-Fixsektoren |

### Erwartete Entscheidungsstruktur

Nach vollständigem B.1-Audit sind folgende Ausgänge möglich:

**Fall 1**: Eine quellenmäßig definierte Transgression
τ_p : H_p^boundary → D(a_p)* existiert → weiter zu B.2.

**Fall 2**: Eine HH-Klasse existiert, aber keine Abbildung in D(a_p)* →
`✓[M]_neg,Quelle` mit Umfangsklausel.

**Fall 3**: Jede kandidatenfähige Randklasse liegt im Wres-Nullraum →
`✓[M]_neg` (stärker: modellunabhängig negativ).

**Fall 4**: Quellenbestand enthält keine Definition eines Grenzkomplexes
(C_p^•, ∂_p) → `✓[M]_neg,Quelle`.

---

## 4. Abhängigkeiten

| Vorgänger | Status |
|---|---|
| [O-229-2] | `✓[M]_neg,Quelle` (NEU-236) |
| [O-229-3] | `?[O]` (NEU-237) |

| Nachfolger | Bedingung |
|---|---|
| [O-229-3B.2] Kontraktion mit Liftkern | Setzt positiven B.1-Befund voraus |
| [O-229-3B.3] Positivitätskontrolle | Setzt β_p aus B.2 voraus |
| [O-229-3B.4] Wres-Abstieg | Setzt β_p aus B.3 voraus |
| [O-229-3B.5] Kanonizität | Setzt alle vorherigen B-Knoten voraus |
| [O-229-3A] Spektraler Randterm | Nur bei negativem oder unvollständigem B-Befund |

---

## 5. Arbeitsstatus

```
[O-229-3B]    ?[O]   (Typ-B-Pfad geöffnet)
[O-229-3B.1]  ?[O]   (erster Quellenaudit: Transgression/Verbindung)
```

Noch nicht zu entscheiden: B.2–B.5 (blockiert bis B.1 abgeschlossen).

---

*Datei: `NEU-238_O229-3B_Kohomologisches_Randdatum_und_3B1_Transgression.md` | Erstellt: 27. Juli 2026*
