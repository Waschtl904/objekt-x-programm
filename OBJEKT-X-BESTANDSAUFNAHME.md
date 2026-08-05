# Objekt X — Bestandsaufnahme und Steckbrief

**Stand: 5. August 2026 (nach NEU-219-Finalaudit, NEU-220c und Abgleich mit NEU-223/225/227)**

Eine Inventur nach 324+ Dokumenten: Was wissen wir über Objekt X, was ist ausgeschlossen,
wo bricht die Konstruktion, und welche Grabungsschnitte sind als nächste sinnvoll.

**Neue verbindliche Resultate seit der letzten Fassung:**
- $[D_g^{\mathrm{corr}}]\smile[\Theta^\wedge]\neq 0$.
- $t\Phi_0\neq C\Phi_0$ für alle $C\in\mathbb C$.
- $\operatorname{ind}_-(Q_\infty)=\operatorname{ind}_+(Q_\infty)=\infty$.
- Der alte Vergleichsoperatorpfad NEU-56(VI) / „NEU-57“ ist durch NEU-223 zusammen mit den Spektralbefunden aus NEU-225/227 **negativ geschlossen**.

Grundlage: systematische Auswertung von `00-grundlegung/` (Soll-Profil), 22 No-Go-Dokumenten,
späteren Direkt- und Revisionsaudits sowie der Konstruktionskette NEU-42 bis NEU-221e,
ergänzt um die Positivitätsklassifikation des archimedischen Kanals aus NEU-220c.

---

## 0. Schichtenverschiebung nach NEU-223/225/227 und NEU-220c

Die bisherige Erwartung, der relative Jacobi-Operator $D_{\mathrm{rel}}=\overline{iJ^-}$ könne
selbst die kompakte Hilbert–Pólya-Schicht liefern, ist **endgültig zurückgenommen**.

NEU-223 zeigt: Jeder zulässige Vergleichsoperator für den alten Schur-/Konfinement-Pfad
reduziert sich auf dieselbe Graphnormklasse wie $|D_{\mathrm{rel}}|$. Die Suche nach einem
„anderen Vergleichsoperator“ kollabiert damit auf dieselbe Kompaktheitsfrage des reduzierten
$D_{\mathrm{rel}}$ selbst.

NEU-225/227 liefern den Spektralbefund: Auf jeder primären Transportkette ist
$D_{\mathrm{rel}}$ unitär auf einen translationsartigen Differentialoperator zurückführbar;
bereits ein solcher Sektor besitzt absolutstetigen Spektraltyp. Zusätzlich enthält der volle
relative Raum eine unendlichdimensionale Nullfaser. $D_{\mathrm{rel}}$ besitzt daher weder auf
dem vollen Raum noch auf dem kernreduzierten Primsektor einen kompakten Resolventen.

$$\boxed{D_{\mathrm{rel}} \text{ ist nicht der kompakte Hilbert–Pólya-Operator von Objekt X.}}$$

Das ist **kein** Scheitern des Jacobi- oder RH-Kanals: Selbstadjungiertheit genügt für die
RH-Hinrichtung; der kompakte Resolvent betrifft den gewünschten Spektraltyp des HP-Modells.
Was wegfällt, ist nur der **lokale Vergleichsoperatorpfad** innerhalb der Graphnormklasse von
$D_{\mathrm{rel}}$.

Gleichzeitig zeigt NEU-220c: Der exakt normalisierte archimedische Weil-Term besitzt einen
unendlichdimensionalen negativen und positiven Index,
$$\boxed{\operatorname{ind}_-(Q_\infty)=\operatorname{ind}_+(Q_\infty)=\infty,}$$
und weder der Polterm noch irgendeine endlich-rangige Korrektur kann diesen negativen Sektor
beseitigen.

**Revidierte Objekt-X-Hauptlinie:**

$$\text{lokale Primkanäle} + W_\infty \longrightarrow \text{globale Kopplungsform} \longrightarrow \text{positive Vervollständigung} \longrightarrow H_X$$

Die bisherige Linie
$$\text{singuläre HH-Struktur} \to D_{\mathrm{rel}} \text{ (Transport/Streuung)} \to K(z) \to \det\nolimits_2 \to \Xi$$
bleibt als **Transfer-/Streuungsunterpfad** erhalten, ist aber noch kein Abguss von Objekt X.

---

## 1. Die Kernbeobachtung: Wir haben den Abdruck, nicht das Objekt

### 1.1 Das Axiomenregister ist weiter veraltet, aber der Steckbrief ist schärfer

Die einzige systematische Beschreibung von Objekt X — [`ebene-XVI-objekt-x.md`](00-grundlegung/ebene-XVI-objekt-x.md)
mit den Positivbedingungen X.1–X.10 und den Ausschlussbedingungen X.neg.1–X.neg.7 — trägt
den Stand NEU-114. Das zweite Axiomensystem, [`objekt_x_minimalaxiome.md`](00-grundlegung/objekt_x_minimalaxiome.md),
steht weiterhin auf `✗[H]`. Beide Register sind veraltet.

**Neu ist aber:** Der Steckbrief von X ist inzwischen wesentlich schärfer. Neben den 22 No-Go-
Resultaten liegen jetzt zwei weitere strukturelle Sperren vor:
- der Abschluss des lokalen Vergleichsoperatorpfads durch NEU-223/225/227,
- die Negativitätsklassifikation des archimedischen Kanals durch NEU-220c.

### 1.2 Die Drift ist bestätigt, aber die Antworten liegen inzwischen vor

Nach NEU-56 brach die direkte X-Arbeit weitgehend ab; gearbeitet wurde an Spektralschatten,
BC-Kohomologie und Weil-Form. Die vier Rückbindungstests aus NEU-114 wurden formal nie
weitergeführt.

Viele Antworten liegen aber inzwischen **implizit** vor und müssen nur verbucht werden:
- Test 114.2 ist durch den 06-Strang negativ beantwortet (Zyklizitätsblockade).
- Test 114.3 ist durch den Vierschichtensatz NEU-116 und den externen Faktor
  $\Theta_{1/2}$ teilweise beantwortet.
- Der archimedische Teil ist mit NEU-220a/b/c nicht positiv lokal realisierbar; der offene
  Pfad ist daher **global gekoppelt**, nicht lokal getrennt.

---

## 2. Der Steckbrief: Was X sein muss

Der eigentliche Ertrag der No-Go- und Auditkette ist ein positives Fahndungsbild. Zusammen mit
den neueren Befunden ergibt sich jetzt:

| # | Eigenschaft, die X haben MUSS | Erzwungen durch |
|---|---|---|
| **S1** | **Nichtverschwindender Off-Diagonal-Anteil** $K^{\mathrm{off}}\neq 0$; kein nichttrivial entkoppelter Block im Primkopplungsgraph. | NEU-50, 207, 209 |
| **S2** | **Mehrdimensionales Bewertungsgitter** mit gemeinsamer, punktkonzentrierter Singularität statt separierbarer Koordinatenstruktur. | NEU-207, 209 |
| **S3** | **Gradierte, nicht skalare Normierung** — eine Diagonalmatrix $D_N$, kein Skalar $\kappa_N$. | NEU-78, 82, 83, 123.H |
| **S4** | **Dichte Trägerstruktur** ($\kappa_N\asymp N$), nicht dünn/rein primzahlindiziert. | NEU-82, 83 |
| **S5** | **Nicht-naive Topologie**: X wird erst durch Zusatzstruktur sichtbar, nicht als gewöhnlicher starker Limes. | NEU-85 |
| **S6** | **Semifinite statt gewöhnlicher Spur**; **Carleman-Determinante $\det_2$** statt Fredholm-Determinante; Schattenklasse $\mathcal S_2\setminus\mathcal S_1$. | NEU-86, 220e, 220u |
| **S7** | **Vermittlung über echte Zwischenobjekte** $\Pi_\gamma$ und $W_\xi$; X ist strukturell höherstufig als jede Projektion. | NEU-114, 115, 116 |
| **S8** | **Keine zentralen Cup-Faktoren, keine globalen Bimodul-Retraktionen**. | NEU-182, 183, 215 |
| **S9** | **Echte Singularität bei 0**: $H\in\mathrm{LC}(\hat{\mathbb Z}\setminus\{0\})\setminus\mathrm{LC}(\hat{\mathbb Z})$. | NEU-196, 200 |
| **S10** | **Getwistete/parazyklische Kohomologie** oder Orbitshift $\kappa\neq 0$; naive Cup-mit-KMS-Form ausgeschlossen. | NEU-219u |
| **S11** | **Unbeschränkte Operatoren und regulierte Spuren** im RH-relevanten Bereich $0<\Re\beta\le 1$. | NEU-140, 141, 220t |
| **S12** | **Global gekoppelte Positivität.** Der archimedische Weil-Term besitzt einen unendlichdimensionalen negativen Spektralsektor. Weder der Polterm noch irgendeine endlich-rangige Korrektur kann ihn positiv machen. Objekt X darf daher keine orthogonale direkte Summe isoliert positiver lokaler Kanäle sein; erforderlich ist eine echte nichtdiagonale Archimedes–Prim-Kopplung $B_{\infty,\mathrm{pr}}$, gegebenenfalls zusammen mit nichttrivialen $B_{pq}$. | NEU-220a, 220c |

Dazu kommt das explizite Kriterienbündel für die Spektralkomponente aus NEU-220u — jetzt mit korrigierter Lesart:

| Kriterium | Forderung | Aktueller Stand |
|---|---|---|
| **HP-1** | $H_X = H_X^*$ | `⚠[M]` — für $D_{\mathrm{rel}}$ unter Nelson-Bedingungen; für einen global gekoppelten $H_X$ offen |
| **HP-2** | $H_X$ hat kompakten Resolventen | **`✗[M]` für $D_{\mathrm{rel}}$ und alle zulässigen graphnormäquivalenten Vergleichsoperatoren**; NEU-223 reduziert die Klasse auf die Kompaktheitsfrage von $D_{\mathrm{rel}}$, NEU-225/227 schließen diese negativ. **Ein anderer global gekoppelter Operator $H_X$ bleibt `?[O]`.** |
| **HP-3** | $H_X^{-1}\in\mathcal S_2\setminus\mathcal S_1$ | `?[O]` — nicht mehr an einen lokalen Vergleichsoperatorpfad zu binden |
| **HP-4** | $N_{H_X}(T)=\frac{T}{\pi}\log\frac{T}{2\pi}-\frac{T}{\pi}+O(\log T)$ | `?[O]` |
| **HP-5** | $\det_2(I-zH_X^{-1})=\Xi(z)/\Xi(0)$ | `?[O]` |
| **HP-6** | Determinantenidentität aus Spur-/Streu-/relativer Determinantenformel | `?[O]` |
| **HP-7** | Nullstellenlagen nirgends als Eingabedaten | **verletzt** im 220s–w-Strang, dort selbst als `?[O], RH-stark` markiert |

### 2.1 Die schärfste Kollision im Katalog — revidiert

Die alte Fassung führte HP-2 und den alternativen Vergleichsoperatorpfad als noch offene
Spannung. Das ist überholt.

> **HP-2 ist für $D_{\mathrm{rel}}$ und alle zulässigen lokalen Vergleichsoperatoren negativ geschlossen.**

NEU-223 zeigt, dass jeder zulässige Vergleichsoperator auf dieselbe Graphnormklasse wie
$|D_{\mathrm{rel}}|$ zurückfällt. NEU-225/227 zeigen, dass $D_{\mathrm{rel}}$ translationsartigen,
absolutstetigen Spektraltyp besitzt und keinen kompakten reduzierten Resolventen hat.

Damit ist der alte G3-/„NEU-57“-Pfad **nicht schlafend, sondern abgeschlossen**.

**Offen bleibt nur noch die globale Version der Frage:**
> Gibt es einen anderen, global gekoppelten Operator $H_X$, dessen Konfinement nicht aus der
> Graphnorm von $D_{\mathrm{rel}}$ allein stammt und der eine echte Archimedes–Prim-Kopplung
> bereits in seiner Konstruktion enthält?

---

## 3. Der Positivbestand: Was tatsächlich gebaut ist

### 3.1 Die tragfähige Kette

```
Primkanten H_rel,N = ⊕_{p≤N} ⊕_m H_{m→pm}                        ✓[M]  NEU-44
   │  Rang-1-Struktur von C_p^rel, störungsstabil                ✓[M]  NEU-44.X/X'
   ▼
Fourier-Hebung  T_p^rel = log p                                  ✓[M]  NEU-42
   │
   ▼
D_rel = closure(iJ^-) wesentlich selbstadjungiert                ⚠[M]  NEU-53–55
   │                            (unter Nelson-Bedingungen)
   ▼
Selbstenergie Σ_rel^ren(β) konvergent, spurklassig für Re β > 0   ✓[M]  NEU-136/137
   │
   ▼
Mangoldt-Spur  Tr(R·Σ_rel^ren) = −ζ'/ζ(β)                        ✓[M]  NEU-141
   │                            NUR für Re β > 1  ◄── Bruch
   ▼
kritischer Streifen 0 < Re β ≤ 1                                 ❓[O]  [O-144-3]
```

Das bleibt die stärkste durchgehende Verbindung von der Primkantenstruktur zur Zetafunktion.
Sie ist echt — aber sie endet weiterhin genau dort, wo die RH eine Aussage macht.

### 3.2 Die revidierten Bruchstellen

| # | Bruchstelle | Kern | Quelle |
|---|---|---|---|
| 1 | Primkanten-Kollaps | $T_{\mathrm{rel}}$ auf dem kollabierten Raum nicht wohldefiniert ohne Kantenmarkierung; Intrinsizität offen. | NEU-43, NEU-44.X3 |
| 2 | Nichtüberzählung | $\dim\ker(1-\mathcal K_\infty(\rho))=m_\rho$ bleibt Kern-Engpass. | NEU-49 |
| 3 | Spurklasse global | Off-Diagonal-Terme generisch; Kriterium braucht echte Spektralbasis von $D_{\mathrm{rel}}$. | NEU-51/52 |
| 4 | Lokaler Konfinementpfad | **negativ geschlossen**: kein alternativer Vergleichsoperator innerhalb der Graphnormklasse von $|D_{\mathrm{rel}}|$ kann HP-2 retten. | NEU-223, 225, 227 |
| 5 | Kritischer Streifen | Spurformel nur für $\Re\beta>1$. | NEU-141/144 |
| 6 | Primkantendiagonalität | Induzierte Wres-Paarung primkantendiagonal weiterhin offen. | NEU-144 [O-144-1] |
| 7 | Zyklisches Tripel | $(\mathcal H_N^{\mathrm{rel}},D_N^{\mathrm{rel}},\Psi_N)$ nicht vollständig typisiert. | NEU-221d |
| 8 | Abel-Lemma quantitativ | Kanalgewichte unbekannt; Kancellation nahe möglicher Nullstellenlagen gefährdet. | NEU-133 |
| 9 | RH-Tautologie | 220s–w nutzt Nullstellenliste bzw. RH-nahe Positivität; nicht als nichttautologischer Konstruktionspfad verwendbar. | NEU-220s–w |
| 10 | Archimedische Negativität | Der lokale archimedische Kanal ist nicht positiv und nicht durch endlich-rangige Defekte reparierbar. | NEU-220c |

### 3.3 Der Feshbach-Kandidat NEU-221 — Status präzisiert

Der gekoppelte Feshbach-/Birman–Schwinger-Transfer
$$K_N(z)=V_N^*(D_{\mathrm{rel}}-z)^{-1}V_N$$
bleibt ein ernstzunehmender Kandidat für die Transfer-/Streuungsschicht. Er ist jedoch
**noch kein Abguss von Objekt X**, sondern eine Arbeitshypothese mit offenen Kopplungs-,
Schattenklassen- und Rückbindungsfragen.

Wesentlich ist jetzt: Selbst eine erfolgreiche Typisierung von $K(z)$ würde den neuen Knoten
S12 / $[O\text{-}220\text{-}1f_0]$ noch nicht automatisch lösen. Denn der archimedische
Negativsektor verlangt eine **globale Positivitätsarchitektur**, nicht bloß einen lokalen
zyklischen oder streuungstheoretischen Kandidaten.

---

## 4. Die zwei ernsten Risiken

### 4.1 Die kohomologische Schicht endet an der Zyklizität, nicht an der Leere

Die alte Leere-Diagnose ist überholt. Die singuläre Route trägt bis $HH^4$ und blockiert erst
an der Zyklizität. Damit ist die kohomologische Schicht nicht leer, aber auch noch nicht in
eine positive Operatorarchitektur überführt.

Der positive Befund $[D_g^{\mathrm{corr}}]\smile[\Theta^\wedge]\neq0$ stärkt diese Schicht,
löst aber das Positivitätsproblem von S12 nicht.

### 4.2 Das Tautologieproblem bleibt scharf

NEU-220t zeigt: Eine positive, invertierbare Metrik im Kreinraum-Modell existiert genau dann,
wenn RH gilt. Jede Reparatur innerhalb dieses Modells ist damit selbst RH-tautologisch.

Der 220-Strang liefert also weiterhin **Kriteriengewinnung**, aber keinen nichttautologischen
Beweisweg. Das heutige archimedische Negativitätsresultat verschärft das noch: Selbst lokal ist
keine positive Hilbertraumrealisierung vorhanden; eine Lösung müsste global gekoppelt und
quellseitig konstruiert sein.

---

## 5. Vier aktive Grabungsschnitte

### G1 — Fundkartierung synchronisieren: Ebene XVI / Bestandsaufnahme aktualisieren

Diese Fassung selbst ist der erste Schritt: S1–S12, HP-1–HP-7 und der Abschluss des alten
Vergleichsoperatorpfads sind jetzt an einem Ort verbucht.

Nächster Unterpunkt: die kanonische Registerdatei `00-grundlegung/ebene-XVI-objekt-x.md`
entsprechend synchronisieren.

### G2 — Die vier Rückbindungstests explizit abschließen

| Test | Was inzwischen vorliegt | Restaufgabe |
|---|---|---|
| 114.1 HH² → Herglotz | wenig | offen halten |
| 114.2 HH⁴ → Obstruktion | O-219-No-Go + spätere Korrekturen | negativ/teilpositiv sauber verbuchen |
| 114.3 Wres → Q_Weil | Vierschichtensatz, externer $\Theta_{1/2}$, archimedischer No-Go | neue globale Kopplungsfrage eintragen |
| 114.4 Primkanten → Λ | hängt an T2-Orthogonalität | mit [O-144-1] zusammenlegen |

### G3 — Alter Vergleichsoperatorpfad abgeschlossen, neuer Operatorpfad offen

**Nicht mehr:** „NEU-57 wieder öffnen“.  
**Sondern:**

> NEU-223 reduziert alle zulässigen Vergleichsoperatoren auf die Graphnormklasse von
> $|D_{\mathrm{rel}}|$. Da $D_{\mathrm{rel}}$ translationsartigen, absolutstetigen
> Spektraltyp und keinen kompakten reduzierten Resolventen besitzt, ist dieser Weg negativ
> geschlossen.

**Neuer Nachfolgeknoten:**
> Existiert ein anderer, global gekoppelter Operator $H_X$, dessen Konfinement nicht aus der
> Graphnorm von $D_{\mathrm{rel}}$ allein stammt?

### G4 — Neuer Hauptknoten: $[O\text{-}220\text{-}1f_0]$

$$\boxed{[O\text{-}220\text{-}1f_0]\quad \text{Existiert eine kanonische Kopplung }B_{\infty,\mathrm{pr}},\text{ durch welche die vollständige globale Blockform positiv wird?}}$$

Arbeitsnormalform:
$$
\mathcal Q_X = \begin{pmatrix}A_\infty & B_{\infty,\mathrm{pr}}\\ B_{\infty,\mathrm{pr}}^* & A_{\mathrm{pr}}\end{pmatrix},
$$
mit ausdrücklich festzuhaltendem Negativbefund
$$A_\infty\ngeq0,\qquad A_\infty+R\ngeq0 \text{ für jede endlich-rangige Korrektur }R.$$

Dies ist jetzt der **aktive Hauptknoten** der positiven Konstruktion.

### G5 — Numerischer Kopplungspilot als nächste Sonde

Sobald $[O\text{-}220\text{-}1f_0]$ typisiert ist, sollte ein numerischer Pilot folgen:
endliche Blockmodelle
$$\mathcal Q_{S,N}=\begin{pmatrix}A_{\infty,N} & B_{\infty,S,N}\\ B_{\infty,S,N}^* & A_{S,N}\end{pmatrix}$$
prüfen, um zu testen, ob echte Primkopplungen negative archimedische Eigenrichtungen anheben
können. Das ersetzt keinen Beweis, entscheidet aber früh, ob die globale Kopplungsidee in die
richtige Richtung weist.

---

## 6. Antwort auf die Ausgangsfrage — revidiert

**Können wir Aussagen über X treffen?** Ja, deutlich schärfer als zuvor. Zwölf erzwungene
Struktureigenschaften S1–S12 plus HP-1–HP-7 liefern heute ein präzises Fahndungsbild.

**Können wir es konstruieren?** Noch nicht. Der alte lokale Vergleichsoperatorpfad ist
negativ geschlossen, und der isolierte archimedische Kanal ist lokal nicht positiv.

**Können wir es eingrenzen?** Ja — stärker als je zuvor. Der Raum möglicher Kandidaten ist
nicht nur kleiner geworden; seine verbleibende Form ist jetzt wesentlich präziser:
Objekt X muss global gekoppelt, nichtdiagonal und positiv nur auf der Ebene der vollständigen
Blockform sein.

**Die archäologische Analogie gilt weiter, aber präziser.** Wir haben nicht nur den Hohlraum
freigelegt, sondern jetzt auch eine weitere harte Wand entdeckt: der archimedische Kanal ist
lokal indefinit. Ein Abguss kann deshalb nicht aus lokal passenden Einzelstücken bestehen,
sondern nur aus einer globalen, miteinander verriegelten Form.

---

*Grundlagendokumente dieser Fassung: Soll-Profil aus `00-grundlegung/`, Negativbild aus den
No-Go-Dokumenten, Positivbestand aus NEU-42 bis NEU-221e, Vergleichsoperatorabschluss aus
NEU-223/225/227, archimedische Positivitätsklassifikation aus NEU-220c. Alle Statusmarken
wurden gegenüber der Vorfassung bewusst revidiert, wo spätere Audits die frühere Diagnose
überholt haben.*
