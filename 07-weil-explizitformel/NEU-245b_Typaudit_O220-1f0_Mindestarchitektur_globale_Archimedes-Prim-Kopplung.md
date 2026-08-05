# NEU-245b — Typaudit [O-220-1f₀]: Mindestarchitektur und globale Archimedes-Prim-Kopplung

**Journalnummer:** NEU-245b  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-05  
**Anschlussknotenpunkt:** NEU-245 ([c.2a] Operatortypaudit NEU-195/NEU-216), NEU-220c (Repositoryaudit, Weil-Normierung und Gamma-Vorfaktor)  
**Status:** ✓[O] Eröffnet

---

## 1. Kontext und Problemstellung

NEU-220c hat mit dem Abschluss des Weil-Normierungs- und Gamma-Vorfaktoraudits den Hauptknoten
**[O-220-1f₀]** eröffnet: Existiert eine globale Mindestarchitektur für den Weil-Operator, die
def archimedischen und nichtarchimedischen (endlichen Primpotenz-)Anteile in einem gemeinsamen
Quellenbild kohärent koppelt, ohne die in NEU-220e und NEU-220t festgestellten Voll­block-
und Additiv-Kreuzterm-No-Gos zu verletzen?

NEU-245 ([c.2a]) hat gezeigt, dass der Koszul-Kandidat über `NEU-195/NEU-216` den
Operatortyptest nur in der reinen Bewertungsderivations-Route besteht, nicht aber als
Kreuzterm-Additiv-Erweiterung. Damit bleibt die zulässige Architektur auf das **gemeinsame
Quellenbild** (gemeinsamer Definitionsbereich, separierter Block pro Primstelle) beschränkt.

Dieses Dokument typisiert den Hauptknoten [O-220-1f₀] und klärt, welche Mindestanforderungen
an eine globale Archimedes-Prim-Kopplung aus den Negativbefunden ableitbar sind.

---

## 2. Eingabebefunde (Negativseite)

### 2.1 Vollblock-No-Go (NEU-220t)

Ein Vollblock-Ansatz
\[
W = \begin{pmatrix} W_{\infty\infty} & W_{\infty p} \\ W_{p\infty} & W_{pp} \end{pmatrix}
\]
scheitert: Die Off-Axis-Blöcke `K^off ≠ 0` erzeugen im Krein-Raum eine indefinite
Sektorstruktur, die mit der Weil-Positivitätsbedingung (NEU-220l) nicht vereinbar ist.
**Status: ✗[O-220-1f₀/Voll]**

### 2.2 Additiv-Kreuzterm-No-Go (NEU-245, [c.2a])

Ein additiver Ansatz der Form
\[
W = W^{\mathrm{arch}} + W^{\mathrm{Koszul}}
\]
mit `W^{Koszul}` aus dem Koszul-Kandidaten über die Bewertungsderivationen scheitert am
Typtest: Der Koszul-Kandidat lebt in `HH¹(B_log)`, nicht in `HH¹(B_val)`; der Kreuzterm
bricht die Typ-Homogenitätsbedingung (NEU-195, 195.7).
**Status: ✗[O-220-1f₀/Add]**

---

## 3. Ableitung der Mindestbedingungen

Aus 2.1 und 2.2 folgen drei notwendige Bedingungen für jede zulässige Architektur:

**M1 (Blockseparation):**  
Der Operator W muss blockdiagonal über archimedischem und endlichem Sektor sein:
\[
W = W_{\infty} \oplus \bigoplus_p W_p
\]
Jede Kopplung zwischen den Blöcken muss über das gemeinsame Quellenbild (Testfunktionsraum)
vermittelt werden, nicht über Off-Axis-Einträge im Operator selbst.

**M2 (Typ-Homogenität):**  
Der endliche Block `W_p` muss vollständig im Typ `B_val` (Bewertungsderivations-Typ, NEU-195)
liegen. Ein Koszul-Additiv aus `B_log` ist nicht zulässig.

**M3 (gemeinsames Quellenbild):**  
Die Kopplung zwischen archimedischem und p-adischem Sektor erfolgt ausschließlich über den
gemeinsamen analytischen Testfunktionsraum (NEU-220j). Die adelische Momentquelle (NEU-221)
muss diesen Raum als Quellenbild verwenden; eine direkte Operatorkopplung ist nicht zulässig.

---

## 4. Positivseite: Zulässige Mindestarchitektur

Unter M1–M3 ist die folgende Mindestarchitektur zulässig:

```
Testfunktionsraum S_adel  (gemeinsames Quellenbild, NEU-220j)
        |
        ├── W_∞ : archimedischer Weil-Operator (Gamma-Vorfaktor, NEU-220a/b)
        │         → Mellin-normierter Beitrag zur Explizitformel
        │
        └── ⊕_p W_p : p-adischer Block (Bewertungsderivations-Typ, NEU-195)
                    → Koszul-freier, rein valutiver Summand
```

Die globale Weil-Explizitformel entsteht dann als Summe der Spurformeln der Einzelblöcke
über den gemeinsamen Testfunktionsraum, nicht als Spur eines gekoppelten Gesamtoperators.

---

## 5. Offene Folgefrage

**[O-245b/1]** Reicht M3 (gemeinsames Quellenbild) aus, um die Hankel-Positivitätshierarchie
(NEU-220v/w) im Grenzübergang zu reproduzieren, oder erfordert die Positivitätskontrolle
einen zusätzlichen Kopplungsterm, der mit M1 vereinbar ist?

Klärung verwiesen an den Feshbach-Weyl-Kandidaten in NEU-221c.

---

## Querverweise

- NEU-220a/b: Mellin-Normierung und Gamma-Vorfaktor
- NEU-220c: Repositoryaudit Weil-Normierung — Eröffnung von [O-220-1f₀]
- NEU-220e: Operatorischer Ursprung, Semifinite Spur, Hilbertspur-NoGo
- NEU-220j: Analytischer Weil-Testfunktionsraum und Konturtransport
- NEU-220l: Weil-Quadratik, Autokorrelation und positiver Kegel
- NEU-220t: Metrikblock-Klassifikation, OffAxis-Trägheit und Similarity-NoGo
- NEU-221: Adelische Momentquelle für den positiven Weil-Operator
- NEU-221c: Zyklischer Feshbach-Weyl-Kandidat und quadratische Resolvente
- NEU-245: [c.2a] Operatortypaudit NEU-195/NEU-216, Koszul-Kandidat
- NEU-195: Bewertungsderivationen, Reduktion HH¹
- NEU-216: Log-Koeffiziententyp B-log
