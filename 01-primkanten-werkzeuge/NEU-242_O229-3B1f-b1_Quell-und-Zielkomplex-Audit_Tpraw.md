# NEU-242: [O-229-3B.1f-b.1] Quell- und Zielkomplex-Audit für T_p^raw

> Datum: 27. Juli 2026 | Status: **?[O] — Zwischenstand nach NEU-155/157/158/166a/168**

---

## 1. Einordnung

NEU-241 hat den Mapping-Cone-Pfad an die richtige logische Schwelle gebunden:
T_p^raw muss nicht nur als einzelner linearer Operator, sondern als relevante
Komponente einer quellenmäßig definierten Kettenabbildung zwischen zwei
kompatiblen Komplexen typisiert sein, bevor ein Mapping Cone konstruiert werden darf.

Dieser Knoten prüft ausschließlich die Teilfrage

```
[O-229-3B.1f-b.1]
```

und noch **nicht** die Konstruktion eines Mapping Cone.

Leitmaxime:

> Bloße gemeinsame kohomologische Herkunft genügt nicht.
> Quell- und Zielraum von T_p^raw müssen selbst als kompatible Gradstücke
> definierter Komplexe auftreten.

Nicht behauptet werden darf, dass T_p^raw grundsätzlich nicht zu einer
Kettenabbildung erweiterbar sei. Der korrekte negative Befund lautet:

> Im auditierten Quellenbestand ist T_p^raw nicht als Komponente einer
> Kettenabbildung typisiert.

---

## 2. Auditprogramm für b.1

### b.1a — Primärtyp von T_p^raw

Aus den Definitionsquellen vollständig zu extrahieren:

```
Dom T_p^raw,   Codom T_p^raw,
```

Insbesondere: algebraischer oder abgeschlossener Definitionsbereich,
verwendete Topologie, eventuelle Quotienten, Abhängigkeit von
\widehat\varepsilon_p, L_3^\circ oder Projektionen, Linearität und
mögliche Unbeschränktheit.

Besonders zu klären: ob

```
T_p^raw : D(a_p) ⟶ Y_p
```

Primärdefinition oder spätere Abstraktion ist.

**Statuslogik:** Gewöhnlicher Operator- oder Formtyp sauber extrahierbar
aber noch keine Komplexstruktur belegt:

```
[O-229-3B.1f-b.1a]   ✓[M]_part
```

---

### b.1b — Existiert ein Quellkomplex?

Gesucht ist eine tatsächlich definierte Differentialstruktur

```
d_lift : C_{p,lift}^n ⟶ C_{p,lift}^{n+1},
```

mit D(a_p) ⊆ C_{p,lift}^r.

Nicht ausreichend: bloße Fouriergraduierung, affine Liftfaser,
Projektorkern K_p, Hochschild-Komplex ohne typisierte K_p-Einbettung.

**Negativer Abschluss:**

```
[O-229-3B.1f-b.1b]   ✓[M]_{neg,Quelle}   (für NEU-155/157/158/166a/168)
```

---

### b.1c — Existiert ein Zielkomplex?

Gesucht ist eine Differentialstruktur

```
d_tar : C_{p,tar}^n ⟶ C_{p,tar}^{n+1},
```

mit Ran T_p^raw ⊆ C_{p,tar}^{r+s}.

Ein Hilbertraum, Symbolraum oder Wres-Quotient ist nicht automatisch
ein Komplex. Ein Differential muss ausdrücklich definiert sein.

**Negativer Abschluss:**

```
[O-229-3B.1f-b.1c]   ✓[M]_{neg,Quelle}   (für NEU-155/157/158/166a/168)
```

---

### b.1d — Gemeinsame Gradzuweisung

Selbst wenn beide Komplexe existierten, müsste belegt werden:

```
T_p^raw : C_{p,lift}^r ⟶ C_{p,tar}^{r+s}.
```

Bei fehlendem Quell- und Zielkomplex ist b.1d nicht nur "blockiert", sondern
die Behauptung einer quellengegebenen gemeinsamen Gradzuweisung ist ebenfalls
negativ geschlossen.

**Negativer Abschluss:**

```
[O-229-3B.1f-b.1d]   ✓[M]_{neg,Quelle}   (für NEU-155/157/158/166a/168)
```

---

## 3. Quellenreihenfolge

```
NEU-155 → NEU-157/158 → NEU-166a/168 → NEU-221e → NEU-226/227 → NEU-229.
```

Gesucht werden tatsächliche Daten:

```
(C^•, d),    d^2 = 0,
D(a_p) ↪ C^r,
Ran T_p^raw ↪ C^{r+s}.
```

---

## 4. Zwischenstand nach Quellenaudit

> **Datiert: 27. Juli 2026**

### b.1a — Primärtyp (endgültig)

NEU-155 (Formel (41.6)) definiert den Primtyp:

```
T_p : B_3^adm ⟶ H_{J,N},
T_p(x) = Π_{J,N} \tildeω_2(x, L_3°).
```

Die Bezeichnung T_p^raw sowie der Typ

```
T_p^raw : D(a_p) ⟶ Y_p
```

sind **keine Primärnotationen** aus NEU-155. Sie gehören zu einer späteren
Abstraktionsschicht.

Wichtige Präzisierung zur Liftabhängigkeit: Die Definition von T_p hängt
nicht von der Auswahl eines einzelnen Lifts ab. Die ausgewertete Kopplung
T_p(\widehat\varepsilon_p) hängt jedoch im Allgemeinen von der gewählten
Hebung ab. Dies darf nicht mit der stärkeren Quotientenunabhängigkeit
T_p(\widehat\varepsilon_p + k_1) ~ T_p(\widehat\varepsilon_p + k_2) verwechselt
werden, die nicht bewiesen ist.

NEU-158 definiert den abgeschlossenen Bildraum:

```
Q_p := ̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅T_p(E_p^lin,ch) ⊆ H_{J,N}
```

mit einer unitären G_p-Darstellung — aber **ohne Differential** und ohne
Gradierung. Q_p ist ein Hilbertraum-Unterraum, kein Kokettenkomplex.

Die Auswertungsdomäne (aus NEU-157) ist die exakte Zulasssigkeitsmenge:

```
A_p^adm(\varepsilon_p^0) := {k ∈ K_p : Q_p(k) = 0, F_p(k) = 0}.
```

Diese Menge ist wegen der Normierungsquadrik Q_p(k) **im Allgemeinen kein
Vektorraum**. T_p^raw bezeichnet daher nicht einen Operator zwischen
linearen Räumen auf A_p^adm, sondern die Auswertung von T_p auf zulässigen
Liftänderungen. Eine lineare Restriktion ist nur auf tatsächlich linearen
Vorbereichen wie K_p, K_p^hom oder E_p^lin,ch möglich.

Fehlende Angaben:
- Beschränktheit/Stetigkeit bezogen auf einen quellenmäßig ausgezeichneten
  Normraum auf der Eingabeseite
- Isometrie \iota_{J,N} nicht belegt
- D(a_p) und Y_p sind keine Primärobjekte aus den bisher gelesenen Quellen

```
[O-229-3B.1f-b.1a]   ✓[M]_part   (endgültig)
```

---

### b.1b — Quellkomplex (Zwischenstatus nach NEU-155/157/158/166a/168)

NEU-157 unterscheidet K_p = ker(\pi_prim), homogen-lineare Nebenbedingungen,
affin-lineare Bedingungen und die nichtlineare W_res-Normierungsquadrik
(157.C.3). Kein Differential d_lift mit d^2 = 0 wird auf K_p, K_p^hom,
E_p^ch oder der Zulässigkeitsmenge definiert.

NEU-166a formuliert eine vollständige Hierarchie

```
T_p : K_p ⟶ Z_p,
T_p : L_p^adm ⟶ Z_p,
T_p : K_p/N_p ⟶ Z_p
```

als Ebenen eines Operatorabstiegs. Auch hier: kein Differential, keine
Gradstücke, keine Komplex-Typisierung.

NEU-168 reduziert die Zeugenfrage auf zwei konkrete mathematische Aufgaben
(Nullraumanalyse von B_p und Schnitt der Normierungsquadrik). Es werden
keinerlei Differentiale auf dem Liftbereich eingeführt.

NEU-155/157/158/166a/168 **definieren keinen Quellkomplex** (C_{p,lift}^•, d_lift)
mit einer typisierten Inklusion D(a_p) ⊆ C_{p,lift}^r.

```
[O-229-3B.1f-b.1b]   ✓[M]_{neg,Quelle}   für NEU-155/157/158/166a/168
```

---

### b.1c — Zielkomplex (Zwischenstatus nach NEU-155/157/158/166a/168)

Der Bildabschluss Q_p ⊆ H_{J,N} trägt in NEU-158 eine Hilbertraum- und
Symmetriestruktur (unitäre Darstellung \pi: G_p ⟶ U(Q_p),
Kommutantenkriterium). Es wird jedoch weder eine Graduierung

```
Q_p = ⊕_n Q_p^n
```

noch ein Differential

```
d_tar : Q_p^n ⟶ Q_p^{n+1},   d_tar^2 = 0
```

definiert.

NEU-166a führt Quotientennorm und Hausdorff-Abstieg ein (§166a.E), aber
ausschließlich als Operatorabstieg auf normierten Räumen — ohne
Kettenstruktur.

NEU-155/157/158/166a/168 **definieren keinen Zielkomplex** (C_{p,tar}^•, d_tar)
mit Ran T_p ⊆ C_{p,tar}^{r+s}.

```
[O-229-3B.1f-b.1c]   ✓[M]_{neg,Quelle}   für NEU-155/157/158/166a/168
```

---

### b.1d — Gemeinsame Gradzuweisung (Zwischenstatus)

Da weder Quell- noch Zielkomplex in den bisher auditierten Quellen definiert
wird, ist die Behauptung einer quellengegebenen gemeinsamen Gradzuweisung
negativ geschlossen.

```
[O-229-3B.1f-b.1d]   ✓[M]_{neg,Quelle}   für NEU-155/157/158/166a/168
```

---

### Vorläufiges Gesamturteil

Für den bisher auditierten Quellenbestand (NEU-155, NEU-157, NEU-158,
NEU-166a, NEU-168) gilt:

```
T_p ist als linearer Operator zwischen algebraischem Eingabebereich
und Hilbertraum definiert, aber nicht als Komponente einer Kettenabbildung.
```

Der Gesamtstatus von b.1b, b.1c und b.1d wird erst nach Prüfung der
restlichen festgelegten Quellen endgültig gesetzt:

```
NEU-221e → NEU-226/227 → NEU-229.
```

---

## 5. Architekturtrennung

Explizit gewährt: Liftkern, Rohkopplung, Wres-Quotient und
Hilbertraumrealisierung werden nicht stillschweigend zu einem einzigen
Komplex identifiziert.

---

## 6. Arbeitsstatus

```
[O-229-3B.1f-b.1]   ?[O]   (Zwischenstand, verbleibend: NEU-221e, NEU-226/227, NEU-229)
```

Nächste Auditschritte:
1. NEU-221e lesen: Gibt es dort erstmals ein Differential auf Lift- oder
   Rohzielraum?
2. NEU-226/227 lesen: Wird der Wres-Nullraum als Unterkomplex typisiert?
3. NEU-229 lesen: Wird T_p als gradierte Abbildung zwischen definierten
   Komplexen typisiert?
4. Erst danach Gesamtstatus [O-229-3B.1f-b.1] endgültig setzen.

---

*Datei: `NEU-242_O229-3B1f-b1_Quell-und-Zielkomplex-Audit_Tpraw.md`*
*Erstellt: 27. Juli 2026 | Letzter Zwischenstand: 27. Juli 2026 (nach NEU-166a/168)*
