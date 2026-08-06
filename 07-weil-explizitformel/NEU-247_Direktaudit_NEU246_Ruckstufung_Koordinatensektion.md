# NEU-247 — Direktaudit NEU-246: Rückstufung auf konditionale Koordinatensektion

**Kennung:** NEU-247  
**Ordner:** `07-weil-explizitformel/`  
**Datum:** 2026-08-06  
**Auditgegenstand:** `07-weil-explizitformel/NEU-246_Relative-Ziel-Transport-Bruecke.md`, Commit `ab442b1`  
**Vorgänger:** NEU-246 — Relative-Ziel–Transport-Brücke  
**Nachfolger:** \([O\text{-}246/0\mathrm{corr}]\) — Gewichteter Kollisionsoperator und kanonisches Rechtsinverses

---

## 0 — Auditgegenstand und Quellenstand

Geprüft wurde NEU-246 im Ordner `07-weil-explizitformel/`, Commit `ab442b1`. Eine andere Datei mit der Nummer NEU-246 existiert zusätzlich im Ordner `01-primkanten-werkzeuge`; die Nummer ist repositoryweit **nicht eindeutig**. Im Folgenden bezeichnet „NEU-246“ ausschließlich die hier geauditete Datei in `07-weil-explizitformel/`.

Eine Datei `NEU-245g` war unter diesem Identifier im erwarteten Pfad nicht auffindbar und konnte daher nicht als Quelle verwendet werden.

Der Auftrag verlangt die Entscheidung, ob \(\iota_{p,N}^{(1)}\) eine bewiesene intrinsische Wres-Hilbertbrücke oder lediglich eine konditionale Modellsektion ist.

---

## 1 — Gesamturteil

\[
\boxed{\text{NEU-246 insgesamt: }\checkmark[M]_{\mathrm{part}}}
\]

NEU-246 enthält eine brauchbare arithmetische Reindexierung des Primsektors und trennt den Fall \(m=1\) zutreffend vom zusammengesetzten Fall. Es erkennt selbst, dass ein echter Operatornachweis fehlt.

Die zentrale Behauptung ist **nicht bewiesen**:

\[
\boxed{
\text{„}\iota_{p,N}^{(1)}\text{ ist eine intrinsische Wres-Hilbertbrücke“}
\quad
\checkmark[M]_{\mathrm{neg,Quelle}}
}
\]

Der tatsächlich erreichte Stand ist höchstens:

\[
\boxed{
\iota_{p,N}^{(1)}\text{ ist eine gewählte, konditionale Koordinatensektion}
\quad
\checkmark[K/M]
}
\]

und auch das erst nach Korrektur der Indexkonvention und der Normierung.

Die Quellen liefern derzeit weder eine explizite positive Wres-Grammatrix noch ein bestimmtes Wres-Radikal, noch einen bewiesenen positiven Hilbertquotienten, noch ein Operator-Intertwining. NEU-221e definiert lediglich einen algebraischen Rohzielraum, ein formal bezeichnetes Radikal und einen erst nach zusätzlicher Positivitätskonstruktion zu vervollständigenden Quotienten. Sie warnt ausdrücklich davor, Primkantendiagonalität oder Intrinsizität der relativen Wres-Paarung vorauszusetzen.

---

## 2 — Prüfung der sechs behaupteten Bedingungen

| Bedingung | Korrigierter Status | Auditbefund |
|---|---|---|
| 1. Indexübereinstimmung | \(\warning[M]\) | Die euklidische Zerlegung \(r=a+pk\) ist korrekt. Ihre Identifikation mit den ursprünglichen \((s,u)\)-Indizes der \(\eta\)-Familie ist nicht bewiesen und erscheint in der geschriebenen Formel vertauscht. |
| 2. Wres-Radikalverträglichkeit | Behauptet \(\times[M]\); tatsächlich \(?[O]\) | Aus nichtverschwindenden Diagonalwerten folgt kein triviales Radikal. Die vollständige Wres-Grammatrix fehlt. |
| 3. Abstieg auf positiven Hilbertraum | Behauptet \(\times[M]\); tatsächlich \(?[O]\) | Positivität, Diagonalität, Quotientenabstieg und Normierung sind nicht bewiesen. Der Faktor \(1/\sqrt{w_{p,r}}\) ist für die behauptete Isometrie falsch. |
| 4. Intertwining mit Transportoperator | \(?[O]\) | Auf dem Ausgangsraum ist kein abgeschlossener Operator mit Domäne definiert. Eine Koordinatenidentifikation ist kein Operatorintertwiner. |
| 5. Zusammengesetzte Zielsektoren | \(?[O]\) | Es wird nur eine Hilbertisierung postuliert. Kopplung, Quotient, \(u\)-Mischung und Operatortransport bleiben offen. |
| 6. Transportmittelwert auf Quotient | \(?[O]\) | Der Mittelwert steigt nur ab, wenn er auf dem tatsächlichen Radikal verschwindet. Dieses Radikal ist unbekannt. |

Damit sind **nicht** „fünf von sechs Bedingungen“ abgeschlossen. Im strengen Sinn ist nur die zugrunde liegende euklidische Division bewiesen.

---

## 3 — Exakter Status von \(\iota_{p,N}^{(1)}\)

### 3.1 — Die arithmetische Zerlegung

Für jedes \(r\in\mathbb Z\) existieren eindeutig \(a\in\{0,\ldots,p-1\}\), \(k\in\mathbb Z\) mit \(r=a+pk\). Die Abbildung \(r\mapsto(a,k)\) ist als reine Mengenabbildung korrekt: \(\checkmark[M]\). Das beweist aber noch keine Identifikation von Wres-Vektoren, Quotientenklassen oder Operatorzuständen.

### 3.2 — Konflikt mit dem vorhandenen Koordinatenwörterbuch

Das vorhandene Wörterbuch lautet:

\[
\eta_{p;m;s,u}\longleftrightarrow e_RV_M,
\qquad M=pm,\qquad R=u+ps.
\]

Insbesondere gilt nach dieser Konvention \(\eta_{p;p;a,k}\longleftrightarrow e_{k+pa}V_{p^2}\), nicht \(e_{a+pk}V_{p^2}\).

Soll \(r=a+pk\) durch die ursprünglichen Indizes dargestellt werden, wäre formal vielmehr \(s=k\), \(u=a\), also \(\eta_{p;p;k,a}\) zu erwarten. NEU-246 schreibt dagegen \(\eta_{p;p;a,k}\).

Damit sind entweder die beiden Indexrollen vertauscht, oder NEU-246 verwendet stillschweigend eine neue, bereits transportadaptierte Notation — ohne diese sauber vom ursprünglichen \(\eta_{p;m;s,u}\)-System zu trennen. Die älteren Dateien identifizieren \(u\) außerdem als Lift- beziehungsweise Regulatorindex, nicht als bloßen Kettenindex.

Die in NEU-225 vorgenommene Transportzerlegung funktioniert anders: Dort wird \(u\) zunächst festgehalten und anschließend der verbleibende Index in Restklasse und Kettenkoordinate zerlegt. Die resultierende Kettenbasis trägt daher weiterhin einen unabhängigen festen \(u\)-Parameter. NEU-246 unterdrückt beziehungsweise vermischt diese zusätzliche Multiplizität.

\[
\boxed{\text{Indexkompatibilität mit dem Quellwörterbuch: }\warning[M]}
\]

### 3.3 — Die Abbildung ist eine Sektion, keine intrinsische Umkehrung

Aus \(R=u+ps\) folgt für jedes \(t\in\mathbb Z\): \(R=(u-pt)+p(s+t)\). Derselbe kollabierte Index \(R\) besitzt somit im unregulierten System unendlich viele Darstellungen:

\[
(s,u)\sim(s+t,u-pt).
\]

Die Wahl \(u=a\), \(s=k\) ist die euklidische Standardsektion dieser Darstellung — arithmetisch ausgezeichnet, aber nicht automatisch Wres-intrinsisch. Der zunächst formulierte nächste Knoten \([O\text{-}246/0]\) lautete deshalb: Zu prüfen sei, ob die verschiedenen Darstellungen durch eine Radikalbedingung identifiziert werden. **NEU-248 korrigiert diese Formulierung doppelt:**

1. Die dort zunächst geschriebene Formel
   \[
   \eta_{p;p;s+t,u-pt}\in\mathcal N_{\mathrm{Wres,rel}}
   \]
   ist bereits formal falsch, da sie für \(t=0\) jede einzelne Basis \(\eta_{p;p;s,u}\) ins Radikal zwingen würde.
2. Auch die differenzierte Version
   \[
   \eta_{p;p;s+t,u-pt}-\eta_{p;p;s,u}\in\mathcal N_{\mathrm{Wres,rel}}
   \]
   ist typwidrig, weil \(\mathcal N_{\mathrm{Wres,rel}}\) im \(E\)-Rohzielraum liegt, die \(\eta\)-Vektoren aber im Transporthilbertraum.

Die richtige Frage ist daher **nicht** eine Radikalidentifikation von \(\eta\)-Differenzen, sondern die Existenz und Geometrie der algebraischen Kollapsabbildung

\[
\kappa_p^{\mathrm{alg}}:\eta_{p;p;s,u}\longmapsto E^{\mathrm{rel}}_{u+ps;1\to p},
\]

ihres Kerns und eines ggf. gewichteten kanonischen Rechtsinversen. Genau dies ist der durch NEU-248 eingeführte Nachfolgeknoten \([O\text{-}246/0\mathrm{corr}]\).

\[
\boxed{\text{intrinsische Quotientenabbildung: }?[O]}
\]

---

## 4 — Status von \(w_{p,r}\)

NEU-246 verwendet formal \(\|E^{\mathrm{rel}}_{r;1\to p}\|_{\mathrm{Wres}}^2\). Diese Schreibweise setzt bereits voraus, dass eine positive Norm existiert. Die fundamentalen Wres-Quellen begründen jedoch keine positive Wres-Funktionalität und keine gewöhnliche GNS-Konstruktion; ausdrücklich wird festgehalten, dass Wres im gegebenen Kontext nicht positiv ist und eine positive Regularisierung oder andere Hilbertisierung noch konstruiert werden muss.

Vor einer Positivitätskonstruktion darf daher höchstens geschrieben werden:

\[
w_{p,r}:=h_{\mathrm{Wres,rel}}\bigl(E^{\mathrm{rel}}_{r;1\to p},E^{\mathrm{rel}}_{r;1\to p}\bigr),
\]

sofern diese Paarung auf den betreffenden Vektoren überhaupt explizit definiert ist.

| Eigenschaft von \(w_{p,r}\) | Status |
|---|---|
| als Symbol eingeführt | \(\warning[M]\) |
| durch explizite Wres-Formel definiert | \(?[O]\) |
| unabhängig von der Hebung \((s,u)\) | \(?[O]\) |
| unabhängig von der Koordinatensektion | \(?[O]\) |
| endlich | \(?[O]\) |
| reell | \(?[O]\) |
| nichtnull | \(?[O]\) |
| positiv | \(?[O]\) |
| Teil einer diagonalen positiven Grammatrix | \(?[O]\) |

Der nächste offene Punkt ist daher nicht bloß \(w_{p,r}>0\), sondern bereits:

\[
\boxed{\text{Was ist die vollständige intrinsische Wres-Grammatrix?}}
\]

---

## 5 — Wres-Radikal- und Quotientenprüfung

### 5.1 — Nichtverschwindende Diagonale impliziert kein triviales Radikal

NEU-246 argumentiert sinngemäß, nichtverschwindende Diagonalgewichte lieferten ein triviales Radikal. Das ist falsch. Bereits die Matrix

\[
G=\begin{pmatrix}1&1\\1&1\end{pmatrix}
\]

besitzt ausschließlich nichtverschwindende Diagonaleinträge, aber ein nichttriviales Radikal \(\operatorname{span}\{(1,-1)\}\). Zur Bestimmung des Radikals benötigt man die vollständige Grammatrix \(h_{\mathrm{Wres,rel}}(E_r,E_{r'})\), nicht nur ihre Diagonale. Die Quellen warnen zusätzlich davor, bei einer möglicherweise indefiniten Form das Radikal mit der Menge isotroper Vektoren zu verwechseln.

\[
\boxed{\text{Behaupteter Beweis in NEU-246: }\times[M]}
\qquad
\boxed{\text{tatsächlicher Radikalstatus: }?[O]}
\]

### 5.2 — Notwendiges Abstiegsdiagramm

Sei \(q_{\mathrm{Wres}}:E_{\mathrm{raw}}\to E_{\mathrm{raw}}/\mathcal N_{\mathrm{Wres,rel}}\) die Quotientenabbildung. Eine auf Rohvektoren definierte Abbildung \(\widetilde\iota:E_{\mathrm{raw}}\to H_{\mathrm{tr}}\) induziert genau dann eine Abbildung auf dem Quotienten, wenn \(\mathcal N_{\mathrm{Wres,rel}}\subseteq\ker\widetilde\iota\). NEU-246 zeigt diese Inklusion nicht.

### 5.3 — Auch Diagonalpositivität würde nicht ausreichen

Selbst wenn \(h_{\mathrm{Wres,rel}}(E_r,E_r)>0\) für alle \(r\) gezeigt wäre, genügt das nicht für eine diagonale Isometrie auf orthonormale \(\eta_r\); nichtverschwindende Kreuzterme würden nicht reproduziert. Bei positiver, aber nicht diagonaler Grammatrix wäre eine Gramfaktorisierung \(G_p=B_p^*B_p\) oder ein Quadratwurzeloperator notwendig — eine punktweise Skalierung einzelner Basisvektoren reicht nicht.

---

## 6 — Der Normierungsfehler

NEU-246 definiert \(w_{p,r}=\|E_r\|_{\mathrm{Wres}}^2\) und anschließend \(E_r\mapsto\frac1{\sqrt{w_{p,r}}}\eta_r\) mit \(\|\eta_r\|=1\). Dann gilt:

\[
\left\|\frac1{\sqrt{w_{p,r}}}\eta_r\right\|^2=\frac1{w_{p,r}},
\qquad\text{während}\qquad
\|E_r\|^2=w_{p,r}.
\]

Die Abbildung ist daher nur im Sonderfall \(w_{p,r}=1\) normerhaltend. Die korrekte isometrische Formel wäre, unter allen weiteren noch unbewiesenen Diagonalitäts- und Positivitätsannahmen:

\[
E_r\longmapsto\sqrt{w_{p,r}}\,\eta_r,
\]

alternativ für normierte Ausgangsvektoren: \(E_r/\sqrt{w_{p,r}}\mapsto\eta_r\).

\[
\boxed{\text{Hilbertbrückenformel in NEU-246: }\times[M]}
\]

Dieser Fehler zieht auch die dort angegebene Formel für den Transportmittelwert in Mitleidenschaft.

---

## 7 — Intertwining- und Domänenprüfung

### 7.1 — Die \(\eta\)-Basis ist keine Eigenbasis

Die Vorgängerdateien halten fest, dass die \(\eta\)-Vektoren eine Graph- beziehungsweise Kopplungsbasis, keine Spektralbasis sind (\(D\eta_a=\sum_b J_{ba}\eta_b\)). Eine Behandlung einzelner \(\eta\)-Vektoren als „Träger-Eigenzustände“ ist ausdrücklich ausgeschlossen. Im Primsektor besitzt der Transportgenerator rein absolut kontinuierliches Spektrum und keine normalen Eigenvektoren.

\[
\boxed{\text{Eigenzustandsinterpretation in NEU-246: }\times[M]}
\]

### 7.2 — Tautologischer Pullback ist kein Quellenintertwining

Eine Definition \(D_E:=\iota^{-1}D_{\mathrm{tr}}\iota\) erfüllt \(\iota D_E=D_{\mathrm{tr}}\iota\) tautologisch — korrekt als konditionale Modellrechnung (\(\checkmark[K/M]\)), beweist aber nicht die Übereinstimmung mit einem bereits vorhandenen geometrischen oder Wres-seitigen \(D_{\mathrm{rel}}\).

### 7.3 — Fehlende Operatorbedingungen

Für ein echtes Operatorintertwining wären mindestens erforderlich: \(D_E\mathcal N_{\mathrm{Wres,rel}}\subseteq\mathcal N_{\mathrm{Wres,rel}}\), \(\iota(\operatorname{Dom}D_E)\subseteq\operatorname{Dom}D_{\mathrm{tr}}\), sowie \(D_{\mathrm{tr}}\iota\xi=\iota D_E\xi\) auf dichter gemeinsamer Kerndomäne, zusätzlich Abschluss, Symmetrie/Selbstadjungiertheit und Bilddichte. NEU-225 lässt die Kerndomänenfrage der Transportrealisierung selbst offen.

\[
\boxed{\text{Operatorintertwining: }?[O]}
\]

---

## 8 — Transportmittelwert und Quotient

Ein linearer Mittelwert \(\mathcal M\) definiert genau dann einen Mittelwert auf dem Quotienten, wenn \(\mathcal M(\nu)=0\) für alle \(\nu\in\mathcal N_{\mathrm{Wres,rel}}\). NEU-245f hatte diese Quotientenfrage offengelassen. NEU-246 erklärt den Abstieg nur, weil zuvor ein triviales Radikal behauptet wurde — dieser Nachweis ist falsch, also fällt der Mittelwertabstieg zurück auf \(?[O]\). Zusätzlich verwendet die Mittelwertformel die fehlerhafte Normierung \(1/\sqrt{w_{p,r}}\); bei korrigierter Zuordnung \(E_r\mapsto\sqrt{w_{p,r}}\eta_r\) würden sich die Gewichtsfaktoren umkehren, bei normierten Ausgangsvektoren träte kein Zusatzfaktor auf.

\[
\boxed{\text{aktuelle Mittelwertformel: keine intrinsische Quotientenformel}}
\]

---

## 9 — Zusammengesetzter Fall \(m>1\)

NEU-246 behandelt den zusammengesetzten Fall nur durch die Erklärung, der Spann könne mit einer „induzierten Wres-Norm“ hilbertisiert werden — das setzt gerade die offenen Probleme (Positivität, Radikal, Liftunabhängigkeit, Abgeschlossenheit, Operatorabstieg) voraus. Divisorensprünge können zudem \(u\)-Klassen mischen; die im Primsektor genutzte Fixierung eines einzelnen \(u\)-Kanals überträgt sich nicht automatisch. Strategie B ist damit keine Konstruktion, sondern eine konditionale Zielbeschreibung.

\[
\boxed{m>1:\quad ?[O]}
\]

---

## 10 — Quellenlage der Wres-Form

Der Verweis auf „NEU-220a“ als Quelle des Wres-Gewichts ist fehladressiert: Unter diesem Identifier findet sich nur die neuere archimedische Normalisierungsdatei, keine Wres-Quelldatei mit der benötigten Grammatrix. NEU-041 liefert ebenfalls keine explizite positive Grammatrix auf der verwendeten Basis; Liftunabhängigkeit, Projektion und Zielraumabstieg bleiben dort offen.

Die tatsächlich einschlägige Wres-Quellenkette ist eher:

\[
\text{NEU-019}\to\text{NEU-031}\to\text{NEU-039}\to\text{NEU-041}\to\text{NEU-221e}\to\text{NEU-228b/229}.
\]

Diese Kette endet gerade bei der offenen Aufgabe, die primäre Wres-Grammatrix und ihr Radikal explizit zu bestimmen.

---

## 11 — Korrigierte Statusbuchung für NEU-246

| Knoten | Status |
|---|---|
| \([O\text{-}246\text{-a}]\) Euklidische Zerlegung \(r=a+pk\) | \(\checkmark[M]\) |
| \([O\text{-}246\text{-b}]\) Kompatibilität mit \((s,u)\)-Indizes und \(u\)-Regulator | \(\warning[M]\) |
| \([O\text{-}246\text{-c}]\) Algebraische Koordinatensektion nach expliziter Hebungswahl | \(\checkmark[K/M]\) |
| \([O\text{-}246\text{-d}]\) Intrinsizität/Sektionsunabhängigkeit im Wres-Quotienten | \(?[O]\) |
| \([O\text{-}246\text{-e}]\) Trivialität des Radikals aus Diagonalwerten | \(\times[M]\) |
| \([O\text{-}246\text{-f}]\) Positiver Hilbertabstieg der geschriebenen Abbildung | \(\times[M]\) |
| \([O\text{-}246\text{-g}]\) Existenz korrigierter positiver Gramfaktorisierung | \(?[O]\) |
| \([O\text{-}246\text{-h}]\) Operatorintertwining einschließlich Domänen | \(?[O]\) |
| \([O\text{-}246\text{-i}]\) Abstieg des Transportmittelwerts | \(?[O]\) |
| \([O\text{-}246\text{-j}]\) Zusammengesetzter Fall \(m>1\) | \(?[O]\) |

Gesamturteil bleibt: \(\boxed{\text{NEU-246: }\checkmark[M]_{\mathrm{part}}}\).

---

## 12 — Konkrete Repository-Korrekturen (anzuwenden auf NEU-246)

1. **Hauptsatz zurückstufen:** „Wres-Hilbertbrücke konstruiert“ → „arithmetische Koordinatensektion vorgeschlagen; Abstieg, Liftunabhängigkeit, Isometrie und Intertwining offen“.
2. **Indizes trennen:** \(\eta_{p;p;s,u}\) und eine ggf. neue Transportnotation \(\eta^{\mathrm{tr}}_{p;a,k;u_0}\) explizit unterscheiden.
3. **\(u\)-Parameter nicht unterdrücken:** Zielvektor mindestens als \(\eta^{\mathrm{tr}}_{p;a,k;u_0}\) führen, bis Identifikation verschiedener \(u_0\) im Quotienten bewiesen ist.
4. **Normierung berichtigen:** \(E_r\mapsto\sqrt{w_{p,r}}\,\eta_r\) statt \(1/\sqrt{w_{p,r}}\), konditional zu \(G_{r,r'}=w_{p,r}\delta_{r,r'}\), \(w_{p,r}>0\).
5. **Vollständige Grammatrix statt Diagonalgewicht:** \(h_{\mathrm{Wres,rel}}(E^{\mathrm{rel}}_{u+ps;1\to p},E^{\mathrm{rel}}_{u'+ps';1\to p})\) definieren, bevor Radikal/Positivität/Gramfaktorisierung geprüft werden.
6. **Radikalargument löschen:** Folgerung „\(G_{r,r}\ne0\Rightarrow\operatorname{Rad}G=\{0\}\)“ streichen.
7. **Mittelwert nur konditional:** erst nach Nachweis \(\mathcal N_{\mathrm{Wres,rel}}\subseteq\ker\mathcal M\) als Quotientenfunktional bezeichnen.
8. **Operatorabschnitt zurückstufen:** nicht „Intertwining“, sondern „Kandidat für spätere Koordinatenidentifikation; Operatorintertwining noch nicht definiert“.
9. **Zusammengesetzten Fall offenlassen:** postulierte Hilbertisierung für \(m>1\) entfernen oder als Arbeitshypothese \(?[O]\) markieren.
10. **Quellen präzisieren:** Verweis „NEU-220a“ durch eindeutigen Pfad und konkrete Formel ersetzen; \(w_{p,r}\) nicht als bereits vorhandenes Quellenobjekt behandeln.

---

## 13 — Korrigierter Forschungs-DAG

\[
\begin{aligned}
\text{NEU-041/043/051/052} &\to \text{Rohbasis, Liftindizes, Wres-Typisierung}\\
\text{NEU-221e} &\to \text{algebraischer Rohzielraum, formaler Quotient}\\
\text{NEU-225/227} &\to \text{Primtransport, Koordinatenwörterbuch}\\
&\searrow\\
[O\text{-}246/0\mathrm{corr}] &\to \text{gewichteter Kollisionsoperator, Kern, Rechtsinverses}\\
\downarrow\\
[O\text{-}246/0\mathrm b] &\to \text{Radikal und positive Gramfaktorisierung}\\
\downarrow\\
[O\text{-}246/0\mathrm c] &\to \text{korrigierte Hilbertbrücke}\\
\downarrow\\
[O\text{-}246/0\mathrm d] &\to \text{Operatorabstieg, Domänen, Intertwining}\\
\downarrow\\
[O\text{-}246/1] &\to \text{Mittelwertabstieg und Niedrigenergiebedingung}
\end{aligned}
\]

Der zusammengesetzte Fall wird als separater Zweig geführt:

\[
[O\text{-}246/2]:\quad m>1\text{ einschließlich Divisorensprüngen und }u\text{-Mischung}.
\]

Die frühere Buchung \([O\text{-}246/1]: w_{p,r}>0\) kommt zu früh: Positivität eines noch nicht intrinsisch definierten Diagonalwerts kann den Brückenoperator nicht begründen.

---

## 14 — Nächster atomarer Forschungsauftrag

\[
\boxed{[O\text{-}246/0\mathrm{corr}]:\ \text{Gewichteter Kollisionsoperator und kanonisches Rechtsinverses}}
\]

Für festes \(p\) sind sauber zu trennen und zu prüfen:

1. die algebraische Kollapsabbildung
   \[
   \kappa_p^{\mathrm{alg}}:\eta_{p;p;s,u}\longmapsto E^{\mathrm{rel}}_{u+ps;1\to p},
   \]
2. ihr Kern, algebraisch erzeugt durch Kollisionsdifferenzen entlang der Fasern \(u+ps=R\),
3. die Obstruktion des ungewichteten Hilbertkollapses wegen unendlich großer Fasern,
4. das gewichtete Beschränktheitskriterium
   \[
   \sup_R\sum_{u+ps=R}|b_{s,u}|^2<\infty,
   \]
5. der minimale Rechtsinverse-Kandidat
   \[
   \iota_{p,b}(E_R)=\frac1{B_R}\sum_{u+ps=R}\overline{b_{s,u}}\,\eta_{p;p;s,u},
   \qquad
   B_R=\sum_{u+ps=R}|b_{s,u}|^2,
   \]
6. und schließlich die Rückbindung der Hebungsunabhängigkeit an die bereits bestehende Barriere \([O\text{-}221\text{-}1c1a]\)/\([O\text{-}153\text{-A/B}]\).

Nur wenn die Gewichte quellenseitig kanonisch und hebungsunabhängig sind, erhält man daraus eine intrinsische Sektion oder Hilbertbrücke.

---

## 15 — Endurteil

\[
\boxed{
\iota_{p,N}^{(1)}\text{ ist gegenwärtig keine bewiesene intrinsische Wres-Hilbertbrücke.}
}
\]

Sie ist im besten Fall eine konditionale, koordinatenabhängige Modellsektion. In der geschriebenen Form ist sie zusätzlich durch eine Indexvertauschung beziehungsweise ungeklärte Reindexierung und durch die falsche Normierung \(1/\sqrt{w_{p,r}}\) belastet.

Der nächste Knoten ist daher nicht die Positivität von \(w_{p,r}\), sondern die vorgelagerte und inzwischen präzisierte Frage, ob das vorhandene Koordinatenwörterbuch über einen gewichteten Kollisionsoperator intrinsisch durch den Wres-Quotienten faktorisiert.

---

## 16 — Repository-Korrekturblock

```text
AUDIT NEU-246 (Direktaudit NEU-247, korrigiert durch NEU-248)

Gesamturteil NEU-246:            checkmark[M]_part
Hauptbehauptung (Hilbertbruecke): checkmark[M]_neg,Quelle
Tatsaechlicher Stand:            konditionale Koordinatensektion, checkmark[K/M]

Korrigierte Knoten:
  [O-246-a] euklidische Zerlegung r=a+pk           checkmark[M]
  [O-246-b] Kompatibilitaet mit (s,u) und u-Regulator  warning[M]
  [O-246-c] Koordinatensektion nach Hebungswahl     checkmark[K/M]
  [O-246-d] Sektionsunabhaengigkeit im Quotienten   ?[O]
  [O-246-e] Radikaltrivialitaet aus Diagonalwerten  x[M]  (falsch, gestrichen)
  [O-246-f] positiver Hilbertabstieg                x[M]  (falsch, gestrichen)
  [O-246-g] korrigierte Gramfaktorisierung          ?[O]
  [O-246-h] Operatorintertwining inkl. Domaenen     ?[O]
  [O-246-i] Abstieg Transportmittelwert             ?[O]
  [O-246-j] zusammengesetzter Fall m>1              ?[O]

Normierungsfehler:
  falsch:   E_r |--> (1/sqrt(w_{p,r})) eta_r
  korrigiert (konditional): E_r |--> sqrt(w_{p,r}) eta_r
  oder:     E_r/sqrt(w_{p,r}) |--> eta_r

Quellenverweis korrigiert:
  "NEU-220a" als Wres-Quelle: fehladressiert.
  Tatsaechliche Kette: NEU-019 -> NEU-031 -> NEU-039 -> NEU-041
                        -> NEU-221e -> NEU-228b/229.

Naechster Knoten:
  Fruehere Formulierung (zurueckgezogen):
    [O-246/0]  Wres-Sektionsunabhaengigkeit im Primsektor.
    Formel (falsch): eta_{p;p;s+t,u-pt} in N_Wres,rel

  Korrektur durch NEU-248:
    - differenzierte Formel waere formal naeherliegend,
      aber ebenfalls typwidrig;
    - korrektes Objekt ist kappa_p^alg: eta_{p;p;s,u} |--> E_rel_{u+ps;1->p}

  Tatsaechlich naechster Knoten:
    [O-246/0corr]
    Gewichteter Kollisionsoperator und kanonisches Rechtsinverses.

Endurteil:
  iota_{p,N}^{(1)} ist keine bewiesene intrinsische Wres-Hilbertbruecke,
  sondern hoechstens eine konditionale, koordinatenabhaengige Modellsektion.
```

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung des RH-Forschungsjournals*
