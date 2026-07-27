# NEU-237: Eröffnung [O-229-3-minimal-additional-boundary-datum]

> Datum: 27. Juli 2026 | Status: ?[O] — neuer Folgeknoten nach Quellen-No-Go [O-229-2]

---

## 1. Motivation und Übergang

Nach dem formalen Abschluss von [O-229-2] als `✓[M]_neg,Quelle` (NEU-236) ist die
nächste Frage nicht mehr, welche vorhandene Symmetrie b_p auswählt. Die Audits
zeigen, dass hierfür zusätzliche Struktur nötig wäre, die im gegenwärtigen
Primärquellenbestand nicht vorhanden ist.

Die neue Leitfrage lautet:

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Welches minimale zusätzliche, intrinsische Randdatum  𝔟_p              │
│  würde einen nichtverschwindenden kontraktiven Vektor                   │
│      b_p ∈ Ran T_p^raw‾                                                │
│  bestimmen, ohne:                                                       │
│  (i)  nachträglich an eine gewünschte Ξ-Identität angepasst zu werden; │
│  (ii) eine bestimmte Liftwahl vorauszusetzen;                           │
│  (iii) aus dem noch nicht wohldefinierten Feshbach-Transfer rückwärts  │
│        definiert zu werden;                                             │
│  (iv) den Wres-Nullraum zu ignorieren;                                  │
│  (v)  eine nicht vorhandene Primkanalorthogonalität vorauszusetzen?     │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Zulässigkeitsbedingungen für ein Randdatum 𝔟_p

Ein Kandidat 𝔟_p ist als zulässig anzusehen, wenn er folgende Bedingungen
erfüllt, bevor ein Lift oder Feshbach-Transfer postuliert wird:

### 2.1 Typkorrektheit

```
b_p ∈ Ran T_p^raw‾   (nicht nur in der Algebra A oder im GNS-Raum)
```

### 2.2 Nichttrivialität

```
0 < |b_p| ≤ 1
b_p ∉ N_{Wres,rel}   (Wres-nichttrivial)
```

### 2.3 Liftunabhängigkeit

Die Auswahl von b_p darf nicht von einer Wahl ε̂_p ∈ Dom T_p^raw abhängen,
deren Quotientenunabhängigkeit erst noch nachzuweisen wäre.

### 2.4 Quotientenverträglichkeit des Mischblocks

Das Mischfunktional

```
β_p(k) = √α_p · ⟨b_p, T_p^raw k⟩
```

muss im Wres-Quotienten wohldefiniert sein:

```
k ∈ N_{Wres,rel}  ⟹  β_p(k) = 0.
```

### 2.5 Keine Ξ-Rückwärtsdefinition

Die gewünschte spektrale Identität (Ξ-Formel) darf nicht als implizite
Definition von b_p verwendet werden.

---

## 3. Mögliche Ergebnistypen

| Code | Bedeutung |
|---|---|
| `✓[K/M]` | Kanonisches Randdatum konstruiert |
| `✓[M]_part` | Eindeutigkeit nur unter zusätzlichen intrinsischen Axiomen |
| `✓[M]_neg` | Jedes zulässige Randdatum fällt in den Wres-Nullraum (mit Umfangsklausel) |
| `✓[M]_neg,Quelle` | Primärdefinition fehlt weiterhin |
| `?[O]` | Konkrete Restfrage, Pfad noch offen |

---

## 4. Erste Strukturüberlegungen (nicht abgeschlossen)

Folgende Kandidatentypen sind a priori denkbar; keiner ist im gegenwärtigen
Quellenbestand ausreichend definiert:

**Typ A — Spektraler Randterm**
Ein aus dem Spektrum von D_rel (oder einer Regularisierung davon) gewonnenes
Funktional auf Ran T_p^raw. Voraussetzung: D_rel ist als selbstadjungierter
Operator auf einem Hilbertraum mit explizit konstruiertem Y_p bereits vorhanden.

**Typ B — Kohomologisches Randdatum**
Ein kanonischer Kozyklus in einer Randkohomologie, der einen Vektor in
Ran T_p^raw‾ auszeichnet. Voraussetzung: Eine Randkohomologie mit Werten in
Y_p (nicht nur im Kochankomplex) muss definiert werden.

**Typ C — Varietäts- oder Fixpunktdatum**
Ein Fixpunkt einer kontrahierenden Abbildung auf der konvexen Menge
{b ∈ Ran T_p^raw‾ : |b| ≤ 1, b ∉ N_{Wres,rel}}.
Voraussetzung: Eine solche Abbildung wäre erst zu konstruieren.

**Typ D — Externes Axiom**
Ein zusätzliches intrinsisches Axiom für Objekt X, das explizit einen
Randvektor postuliert (im Geiste eines Axioms X.7 o.ä.).
Nachteil: Verschiebt das Problem auf die Rechtfertigung des Axioms.

---

## 5. Arbeitsstatus

```
┌─────────────────────────────────────────────────────────────────────────┐
│  [O-229-3-minimal-additional-boundary-datum]                            │
│                                                                         │
│  ?[O]                                                                   │
│                                                                         │
│  Keine der denkbaren Kandidatenstrukturen ist im gegenwärtigen          │
│  Quellenbestand ausreichend definiert. Der Knoten ist offen.            │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Abhängigkeiten

| Vorgänger | Status |
|---|---|
| [O-229-2] | `✓[M]_neg,Quelle` (NEU-236) |
| [O-229-2a] | `✓[M]_neg,Quelle` (NEU-236) |

| Nachfolger (potentiell) | Bedingung |
|---|---|
| [O-229-3a] — Typ-A-Audit (spektral) | Setzt explizites Y_p ↪ H_{D_rel} voraus |
| [O-229-3b] — Typ-B-Audit (kohomologisch) | Setzt Randkohomologie auf Y_p voraus |
| [O-229-4] — Feshbach-Wohldefiniertheit | Setzt zulässiges 𝔟_p aus [O-229-3] voraus |

---

*Datei: `NEU-237_O229-3_Minimales_Randdatum_Eroeffnung.md` | Erstellt: 27. Juli 2026*
