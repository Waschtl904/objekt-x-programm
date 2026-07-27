# NEU-242: [O-229-3B.1f-b.1] Quell- und Zielkomplex-Audit für T_p^raw

> Datum: 27. Juli 2026 | Status: **?[O]**

---

## 1. Einordnung

NEU-241 hat den Mapping-Cone-Pfad präzise an die richtige logische Schwelle
gebunden: Ein Mapping Cone darf erst dann konstruiert werden, wenn
T_p^raw nicht nur als einzelner linearer Operator, sondern als relevante
Komponente einer quellenmäßig definierten Kettenabbildung zwischen zwei
kompatiblen Komplexen typisiert ist.

Dieser Knoten öffnet deshalb **ausschließlich** die Teilfrage

```
[O-229-3B.1f-b.1]
```

und noch **nicht** die Konstruktion eines Mapping Cone.

Die Leitmaxime lautet:

> Bloße gemeinsame kohomologische bzw. HH-Herkunft genügt nicht.
> Quell- und Zielraum von T_p^raw müssen selbst als kompatible Gradstücke
> definierter Komplexe auftreten.

Im auditierten Quellenbestand darf daher nur gefragt werden, ob eine solche
Typisierung **quellenmäßig vorliegt**. Nicht behauptet werden darf, dass
T_p^raw grundsätzlich nicht zu einer Kettenabbildung erweiterbar sei.

Der erwartete negative Quellenbefund ist entsprechend eng zu formulieren:

> Im auditierten Quellenbestand ist T_p^raw nicht als Komponente einer
> Kettenabbildung typisiert.

---

## 2. Auditprogramm für b.1

### b.1a — Primärtyp von T_p^raw

Aus den Definitionsquellen vollständig zu extrahieren sind:

```
Dom T_p^raw,   Codom T_p^raw,
```

insbesondere:

- algebraischer oder abgeschlossener Definitionsbereich,
- verwendete Topologie,
- eventuelle Quotienten,
- Abhängigkeit von \widehat\varepsilon_p, L_3^\circ oder Projektionen,
- Linearität und mögliche Unbeschränktheit.

Besonders zu klären ist, ob der Ausdruck

```
T_p^raw : D(a_p) ⟶ Y_p
```

eine Primärdefinition ist oder bereits eine spätere Abstraktion aus
Liftänderung, Quotientenabstieg oder Hilbertraumrealisierung.

**Statuslogik:**
Wenn der gewöhnliche Operator- oder Formtyp sauber extrahiert werden kann,
aber noch keine Komplexstruktur belegt ist, erhält

```
[O-229-3B.1f-b.1a]   ✓[M]_part
```

---

### b.1b — Existiert ein Quellkomplex?

Gesucht ist eine tatsächlich definierte Differentialstruktur

```
d_lift : C_{p,lift}^n ⟶ C_{p,lift}^{n+1},
```

mit

```
D(a_p) ⊆ C_{p,lift}^r.
```

Nicht ausreichend sind:

- bloße Fouriergraduierung,
- affine Liftfaser,
- Projektorkern K_p,
- ein Hochschild-Komplex, in den K_p nicht typisiert eingebettet ist.

Es genügt also nicht, dass eine Quelle „kohomologisch klingt“; es muss ein
wirklich definierter Komplex \((C^\bullet,d)\) mit \(d^2=0\) vorliegen,
in dessen Gradstück D(a_p) typisiert eingeht.

**Negativer Abschluss:**
Wenn kein solcher Quellkomplex in den auditieren Quellen definiert ist,
gilt

```
[O-229-3B.1f-b.1b]   ✓[M]_{neg,Quelle}
```

---

### b.1c — Existiert ein Zielkomplex?

Analog ist eine Differentialstruktur nötig:

```
d_tar : C_{p,tar}^n ⟶ C_{p,tar}^{n+1},
```

mit

```
Ran T_p^raw ⊆ C_{p,tar}^{r+s}.
```

Ein Hilbertraum, Symbolraum oder Wres-Quotient ist nicht automatisch ein
Komplex. Ein Differential muss ausdrücklich definiert sein.

**Negativer Abschluss:**
Wenn kein Zielkomplex mit ausdrücklichem Differential und typisierter
Einbettung des Bildraums von T_p^raw vorliegt, gilt

```
[O-229-3B.1f-b.1c]   ✓[M]_{neg,Quelle}
```

---

### b.1d — Gemeinsame Gradzuweisung

Selbst wenn auf beiden Seiten Komplexe existieren, muss zusätzlich eine
konkrete Gradzuweisung belegt werden:

```
T_p^raw : C_{p,lift}^r ⟶ C_{p,tar}^{r+s}.
```

Die Bezeichnung L_3^\circ, der Grad einer Hochschildklasse oder die
Symbolordnung darf nicht als Beweis für r oder s verwendet werden.

Wichtig ist die Statuslogik:
Wenn die Quellen keine beiden Komplexe definieren, dann ist b.1d nicht nur
„blockiert“, sondern die Behauptung einer **quellengegebenen gemeinsamen
Gradzuweisung** ist ebenfalls negativ geschlossen.

Daher gilt im negativen Quellenfall:

```
[O-229-3B.1f-b.1d]   ✓[M]_{neg,Quelle}
```

---

## 3. Quellenreihenfolge

Die Auditierung folgt der Reihenfolge, in der T_p^raw, Liftänderung,
Quotientenabstieg und spätere kohomologische Deutungen tatsächlich in den
Quellen auftreten:

```
NEU-155 → NEU-157/158 → NEU-166a/168 → NEU-221e → NEU-226/227 → NEU-229.
```

Dabei wird nicht nach dem Wort „Komplex“ allein gesucht, sondern nach den
wirklichen Daten

```
(C^•, d),    d^2 = 0,
D(a_p) ↪ C^r,
Ran T_p^raw ↪ C^{r+s}.
```

Für den Audit relevant sind also nur solche Stellen, an denen tatsächlich
Differentiale, Gradstücke und Einbettungen von Quell- oder Zielraum
explizit definiert werden.

---

## 4. Erwartbarer Auditabschluss

Falls die Quellen nur einen Operator

```
T_p^raw : D(a_p) ⟶ Y_p
```

zwischen linearen bzw. topologischen Räumen definieren, aber keine
Differentiale auf diesen Räumen, ergibt sich die folgende Statusfolge:

```
[O-229-3B.1f-b.1a]   ✓[M]_part
[O-229-3B.1f-b.1b]   ✓[M]_{neg,Quelle}
[O-229-3B.1f-b.1c]   ✓[M]_{neg,Quelle}
[O-229-3B.1f-b.1d]   ✓[M]_{neg,Quelle}
```

und insgesamt

```
[O-229-3B.1f-b.1]   ✓[M]_{neg,Quelle}.
```

Danach folgen logisch:

```
[O-229-3B.1f-b.2]   ?[O]_{blockiert}
[O-229-3B.1f-b.3]   ?[O]_{blockiert}
```

Der Knoten

```
[O-229-3B.1f-b.4]
```

bleibt als allgemein bewiesene notwendige analytische Bedingung bestehen,
aber als konkreter Konstruktionsknoten blockiert. Die Schranke

```
||Λ_p|| ≤ √α_p
```

bleibt unabhängig davon gültig, ob der Mapping-Cone-Typ im aktuellen
Quellenbestand scheitert.

---

## 5. Architektonische Trennungsregel

Der Audit wahrt ausdrücklich die Trennung zwischen:

- Liftkern,
- Rohkopplung,
- Wres-Quotient,
- Hilbertraumrealisierung.

Diese Bausteine dürfen nicht stillschweigend zu einem einzigen Komplex
identifiziert werden. Gerade diese Trennung ist der sachliche Kern des
aktuellen Audits.

---

## 6. Arbeitsstatus

```
[O-229-3B.1f-b.1]   ?[O]
```

Nächste konkrete Arbeitsausführung:

1. NEU-155 lesen und Primärtyp von T_p^raw extrahieren.
2. NEU-157/158 und NEU-166a/168 auf Lift- bzw. Quotientenkomplexdaten prüfen.
3. NEU-221e, NEU-226/227, NEU-229 nur auf explizite Differenziale,
   Gradstücke und typisierte Einbettungen auswerten.
4. Falls diese Daten fehlen, b.1 negativ aus Quellenlage schließen,
   ohne daraus eine prinzipielle Unmöglichkeit abzuleiten.

---

*Datei: `NEU-242_O229-3B1f-b1_Quell-und-Zielkomplex-Audit_Tpraw.md` | Erstellt: 27. Juli 2026*
