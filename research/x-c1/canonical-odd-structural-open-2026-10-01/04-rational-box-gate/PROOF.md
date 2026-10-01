# Rationaler Boxtest für die ungerade Maximiererrichtung

30. September 2026 · A9 nach A11 · lokaler Forschungsblock

**STRUCTURAL OPEN · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

Ausgangspunkt: `main@689ff6266b5e4d58700f82eae3016951a023e353`.

## Ergebnis

Der angeforderte rationale Branch-and-Bound-Prüfer ist umgesetzt. Er
teilt zuerst Y₅₈, danach Y₆₈ und bezahlt die vollständigen übrigen
Eintragsunsicherheiten. Nach **7 geprüften Knoten und 4 terminalen
Teilboxen** ist die Frage für die vorliegende Relaxation entschieden:

\[
\boxed{\text{STRUCTURAL OPEN}.}
\]

Zwei verschiedene überlebende Teilboxen enthalten jeweils eine vollständig
zertifizierte zulässige Vervollständigung. Beide erfüllen die gemeinsame
Transportordnung, alle geerbten ausdrücklich geprüften Momentbedingungen
und die Eigenwert-/Gapgrenzen. Ihre maximalen physischen inversen
Antwortrichtungen liegen mindestens **89.987266 Grad** auseinander.

Damit kann auch ein feineres Aufteilen dieser Familie keinen engen,
alle zulässigen Daten umfassenden Winkelkorridor erzwingen. Um irgendeine
feste Referenzgerade braucht ein solcher Kegel mindestens **44.993633 Grad
Halbwinkel**. Dies betrifft die geprüfte Relaxation; die tatsächliche
ungerade Maximiererrichtung ist damit weiterhin nicht lokalisiert.

Der im Auftrag genannte Zwischenstand UNRESOLVED wurde durch die zuvor
fertiggestellten korrigierten Transportbeispiele überholt. Die neue
Transportbedingung bleibt wirksam: Sie schließt die früheren unmodifizierten
Beispiele aus. Ihre Wirkung genügt jedoch nicht, die korrigierten Beispiele
mit unverändertem Projektor auszuschließen.

## Daten und Normalisierung

Der Prüfer verwendet unverändert

\[
\widetilde B_B=G_B+L_B/17,\qquad
X=\widetilde B_B^{-1}Y^*.
\]

Dies ist exakt dieselbe Konvention wie X=17(L_B+17G_B)^{-1}Y*.
Ein unabhängiger rationaler Test prüft den Faktor 17 an
nichtkommutierenden Gram- und Energiematrizen.

Die vier Verzweigungsvariablen sind

\[
(Y_{57},Y_{58},Y_{67},Y_{68}).
\]

Die übrigen Einträge von Y sowie die vollständigen Matrizen G_A,L_A,G_B,L_B
und Z_B bleiben in ihren zertifizierten Hüllen. Die Hüllen beider geerbter
Präzisionsquittungen werden geschnitten. Eine unabhängige Wahl der
Mittelpunktmatrizen wird nicht als gemeinsame Realisierung verwendet.

Intervallrechnung vergrößert die zulässige Menge dort, wo sie Abhängigkeiten
nicht vollständig ausdrücken kann. Ein Ausschluss auf dieser größeren
Menge ist sicher; bloßes Überleben einer Box beweist keine Zulässigkeit.
Die Existenzbeweise stammen aus den erneut vollständig abgespielten
gemeinsamen rationalen Konstruktionen des Vorgängerpakets.

## Sichere Ausschlussregeln

Für jede Box werden aus demselben Y und denselben Matrixhüllen gebildet:

\[
H_0=G_A-X^*G_BX,\quad H_1=L_A-X^*L_BX,\quad H_\nu=H_1-\nu_BH_0.
\]

Die Einschließung von H_ν wird zusätzlich mit der algebraisch gleichen Form

\[
H_\nu=L_A-\nu_BG_A+X^*(\nu_BG_B-L_B)X
\]

geschnitten. Es gilt ν_B=0.070769.

Eine Box wird nur verworfen, wenn ein notwendiger PSD-Test unmöglich ist:

- Ein Diagonaleintrag von H₀ oder H_ν hat eine strikt negative Obergrenze.
- Die Determinante des Hauptminors auf den alten Richtungen 5 und 6 hat
  eine strikt negative Obergrenze.

Eine negative Untergrenze reicht nicht als Ausschluss. Ebenso wird aus
einem nicht entscheidbaren Nenner oder einem zu breiten Projektorintervall
kein Unzulässigkeitsurteil abgeleitet.

Beim vorliegenden Lauf werden **keine** der vier terminalen Boxen durch
diese äußeren Tests ausgeschlossen. Zwei enthalten nachgewiesene Zeugen;
für die beiden anderen wird keine Existenzbehauptung aufgestellt.

## Gemeinsame Kernbasis und physischer Projektor

Für jede überlebende Box wird

\[
N=\begin{pmatrix}-Y_l^{-1}Y_r\\I_2\end{pmatrix}
\]

neu eingeschlossen. Dieses eine N wird in allen Kompressionen G₀,L₀,Z₀
verwendet. Die geerbten Energieordnungen und die vom selben Y,N abhängigen
Resolventenfunktionale werden ergänzend ausgewertet.

Aus M=L₀+34G₀+289G₀L₀^{-1}G₀ und R=L₀+34G₀+289Z₀ setze

\[
T=M^{-1}R,\qquad K=T-\beta_-I.
\]

Weil der obere Eigenwert einfach ist, hat K Rang eins und sein Bild ist
die gesuchte obere Eigenrichtung. Der physische Gram-Projektor in den
Kernkoordinaten ist

\[
\Pi_G=\frac{KK^*G_0}{\operatorname{tr}(KK^*G_0)}.
\]

Dies ist ein G₀-orthogonaler Projektor. Ein Eigenvektorkomponentenquotient
wird nicht benötigt. Eine positive Untergrenze für den Nenner folgt aus

\[
\operatorname{tr}(KK^*G_0)
\ge\frac{\det G_0}{\operatorname{tr}G_0}
(\beta_+-\beta_-)^2.
\]

Der Winkelvergleich benutzt U=NK, eine feste rationale Referenz c im
vollen Achtkoordinatenraum und die physische Gram-Matrix G_B:

\[
\cos^2\theta=
\frac{\|U^*G_Bc\|^2}
{(c^*G_Bc)\operatorname{tr}(U^*G_BU)}.
\]

c ist der rationale Mittelpunkt der zweiten Spalte der bereits gebundenen
zentralen Trial-Kernbasis. Diese Wahl definiert nur die Referenzrichtung;
sie ersetzt keine unsicheren Operator- oder Momentdaten durch Mittelpunkte.

Die breiten terminalen Boxen liefern jeweils zunächst nur 0≤sin²θ≤1.
Das ist kein Lokalisierungsnachweis. Für die engen Einschließungen der
zwei ausdrücklich konstruierten Zeugen ergeben sich dagegen:

| Zeuge | Physischer Winkel zur festen Referenz |
| --- | ---: |
| zentral korrigiert | [0.95153834°, 0.95153835°] |
| gedreht korrigiert | [89.035729°, 89.035730°] |

Dies sind unorientierte Winkel zur Referenz. Der direkte Winkel zwischen
beiden Geraden wird gesondert im gemeinsamen G_B-Raum zertifiziert und
beträgt mindestens 89.987266 Grad.

## Die vier dominanten Koordinaten

Gerichtete Einschließungen der beiden zulässigen Zeugen:

| Eintrag | Zentral korrigiert | Gedreht korrigiert |
| --- | --- | --- |
| Y₅₇ | [−0.017877352, −0.017877351] | [−0.017878213, −0.017878212] |
| Y₅₈ | [0.0017811837, 0.0017811838] | [0.0020593161, 0.0020593162] |
| Y₆₇ | [−0.28947323, −0.28947322] | [−0.28940713, −0.28940712] |
| Y₆₈ | [0.055425517, 0.055425518] | [0.034108608, 0.034108609] |

Y₅₇ und Y₆₇ liegen bei beiden Zeugen innerhalb der im Auftrag genannten
diagnostischen engeren Bereiche. Es besteht daher kein Widerspruch zur
beobachteten Verengung dieser beiden Koordinaten. Die weiterhin mögliche
Variation in Y₅₈,Y₆₈ genügt für die stark verschiedenen Richtungen.
Die diagnostischen Gesamtbreiten von 12 % und 28 % werden hier nicht als
uniform zertifizierte Hüllen übernommen.

Nach der ersten Halbierung von Y₅₈ liegt der zentrale Zeuge links, der
gedrehte rechts. Nach der anschließenden Halbierung von Y₆₈ liegen sie
in `rootLL` beziehungsweise `rootRL`. Sämtliche Grenzen und die exakte
Überdeckung der Ausgangsbox stehen in `verification.json`.

## Abnahmestatus und Stoppregel

Die feste GREEN-Schwelle dieses Laufs lautet sin²θ≤1/100 bezüglich
derselben Referenz, also ein Halbwinkel kleiner als 5.74 Grad. Die
Schwelle ist eine Abnahmeeinstellung, keine mathematische Behauptung.

- **GREEN:** Alle nicht ausgeschlossenen terminalen Boxen liegen im
  gemeinsamen Zielkorridor, und die Boxen überdecken den Ausgangsbereich.
- **STRUCTURAL OPEN:** Zwei vollständig zertifizierte zulässige Punkte
  liegen in verschiedenen überlebenden Boxen und überschreiten gemeinsam
  die mögliche Breite des Zielkorridors.
- **UNRESOLVED:** Die verbleibenden Einschließungen reichen nicht aus und
  es liegt kein solcher Existenznachweis vor.

Eine vollständig ausgeschlossene äußere Familie erhält einen eigenen
Fehler-/Diagnosestatus; sie wird nicht leerheitsbedingt als GREEN ausgegeben.
Die Einstellungen erlauben bis zu 12 Teilungsebenen und 255 Knoten. Weiter
geteilt wird nur bei noch unentschiedener mathematischer Frage.

Der aktuelle Stopp nach zwei Ebenen ist durch die Existenzbeweise begründet,
nicht durch ein Rechenbudget. Die Gegenzeugen schließen unabhängig von der
gewählten Referenz jeden gemeinsamen Halbwinkel unter 44.993633 Grad aus.

## Prüfung und Konsequenz

Das unveränderte letzte Projektor-/Transportarchiv ist vollständig
eingebettet. Sein Certifier und alle eingebetteten Vorgängerreplays werden
bytegleich ausgeführt. Die PSD-Ausschlussregeln werden unter anderem an
Intervallboxen geprüft, die ausdrücklich positiv definite Matrizen
enthalten und deshalb nicht verworfen werden dürfen.

Weitere unabhängige Kontrollen prüfen exakte Boxpartitionen, die
Unterscheidung der Ergebnisstatus, die physische statt euklidische
Winkelmetrik, den Faktor 17 und die Ablehnung manipulierter Archive.
Die frische Quellenprüfung umfasst erneut 25 ursprüngliche
Repository-Quellen. Große Operatorrechnungen wurden nicht gestartet.

Der nächste informative Schritt bleibt die gemeinsame Projektor- oder
Kreuzresidueninformation des tatsächlichen A9/A11-Operatorpaars. Die
vorhandene Relaxation nochmals feiner aufzuteilen kann die bereits
zertifizierten zulässigen Gegenrichtungen nicht entfernen.

Der tatsächliche ungerade Winkel, bandweise Momente tatsächlicher
Maximierer und der Forward-Renewal-Satz bleiben offen. Eine gemeinsame
Realisierung aller Trialdaten durch das vollständige physische
Operatorpaar wird für die Gegenzeugen nicht beansprucht.
Der Repository-Stand bleibt unverändert; A13/#187 wurde nicht als
Forschungsquelle verwendet.
