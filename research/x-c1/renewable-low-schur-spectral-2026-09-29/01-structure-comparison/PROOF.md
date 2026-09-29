# Renewable Low-Schur Positivity

## Erster Strukturvergleich von A8, A9 und A11

28. September 2026 · Neue lokale Untersuchung · Externe analytische Prüfung offen

**Ergebnis:** Die drei vorhandenen Rechnungen zeigen sehr ähnliche empfindliche
Richtungen in physischen Koordinaten. Ein wiederverwendbarer kritischer Unterraum
ist deshalb ein konkreter Forschungsansatz. Eine erneuerbare Positivitätsaussage
ist damit noch nicht bewiesen. Die einfache monotone Fortsetzung der bisherigen
Zertifikatsmatrizen ist in ihren Referenzkoordinaten bereits ausgeschlossen.

Die Untersuchung liest ausschließlich den integrierten Stand
[`d16ba43`](https://github.com/Waschtl904/objekt-x-programm/tree/d16ba43ebb20f2c61f43379fc65d7a9b9dba76de).
Die zehn benutzten Eingabedateien wurden mit den Bytes dieses Commits verglichen
und zusätzlich mit SHA-256 gebunden. O8–A11, Registry und Repository wurden nicht
verändert. Es wurde keine vierte Kammer gerechnet.

## 1. Was verglichen wurde

| Terminal | Low-Dimension je Parität | Hoher Anfangsgrad gerade/ungerade | Hoher Boden δ | Gamma-Modellgrad |
|---|---:|---:|---:|---:|
| A8 = log(8)/2 | 191 | 384 / 385 | 2/3 | 160 |
| A9 = log(3) | 296 | 594 / 595 | 2/3 | 224 |
| A11 = log(11)/2 | 285 | 572 / 573 | 1 | 416 |

Bei A8 wurde die erfolgreiche **verfeinerte** Untermatrix verwendet. Die ältere
Rechnung mit δ=1/2 ist ein erhaltener Zwischenstand und keine der drei hier
verglichenen erfolgreichen Rechnungen. Bei A11 wurde die ursprüngliche
Untermatrix vor dem rationalen Basiswechsel verwendet.

Die unterschiedlichen Dimensionen sind Entscheidungen der jeweiligen
Tail-Abschätzung. Insbesondere bedeutet 296 → 285 weder das Verschwinden eines
Kanals noch eine Abnahme der wirklichen Schwierigkeit.

### Drei verschiedene Schur-Objekte

In physischen, momentkorrigierten Koordinaten sei die vollständige Form

\[
\mathcal Q=\begin{pmatrix}L&B\\B^*&H\end{pmatrix},\qquad H\succeq\delta I.
\]

Der exakte physische Schurrest ist \(S^{\rm phys}=L-BH^{-1}B^*\).
Die gespeicherten Rechner verwenden die hinreichende Untermatrix

\[
F=L_0-e_LI-\delta^{-1}H^{\rm up},\qquad
H^{\rm up}=\frac{1001}{1000}G_0+1001e_B^2I,
\quad G_0=B_0B_0^*.
\]

Somit gilt unter den veröffentlichten Fehlerabschätzungen
\(F\preceq L-\delta^{-1}BB^*\preceq S^{\rm phys}\).
Der in orthogonalen T-Koordinaten geschriebene Defekt-Schurrest ist wiederum ein
anderes Koordinatenobjekt. **Die unten untersuchten Eigenrichtungen gehören zu F.**
Sie sind nicht automatisch Eigenrichtungen des exakten physischen oder des
Defekt-Schurrests.

Grundlagen: [O8, §§2–7](https://github.com/Waschtl904/objekt-x-programm/blob/d16ba43ebb20f2c61f43379fc65d7a9b9dba76de/research/x-c1/first-chamber-o8-o9-2026-09-27/o8-rechenstand/PROOF.md),
[A9, §§6–7](https://github.com/Waschtl904/objekt-x-programm/blob/d16ba43ebb20f2c61f43379fc65d7a9b9dba76de/research/x-c1/chambers-through-a11-2026-09-28/a9/PROOF.md),
[A11, §§4–5](https://github.com/Waschtl904/objekt-x-programm/blob/d16ba43ebb20f2c61f43379fc65d7a9b9dba76de/research/x-c1/chambers-through-a11-2026-09-28/a11/PROOF.md).
Die Quellentexte enthalten bewusst erhaltene Zwischenstände; ihr integrierter
Ergebnisstatus ergibt sich aus den späteren Zertifikaten und dem Register.

## 2. Die empfindlichsten Richtungen

Auf den rationalen Mittelpunkten der sechs Intervallmatrizen wurden jeweils die
ersten drei kritischen Richtungen durch inverse Unterraumiteration mit 768 Bit
untersucht. Die Tabelle zeigt den kleinsten diagnostisch gefundenen Eigenwert.
Dies sind **Diagnosewerte**, keine neuen allgemeinen Reservebehauptungen.

| Terminal | F: gerade | F: ungerade | Grad, bis zu dem 99 % der Koordinatennorm der ersten Richtung liegen, gerade/ungerade |
|---|---:|---:|---:|
| A8 | 1,11289116 · 10⁻²⁶ | 7,79687588 · 10⁻²⁴ | 12 / 11 |
| A9 | 1,03043821 · 10⁻³¹ | 9,60207951 · 10⁻²⁹ | 12 / 13 |
| A11 | 9,48060943 · 10⁻⁴² | 1,21019965 · 10⁻³⁸ | 14 / 13 |

Die relative Eigenpaarresiduen-Norm \(\|Fv-\lambda v\|/|\lambda|\) bleibt für
alle 18 untersuchten Richtungen unter 10⁻³⁰. Die drei A11-Eigenwerte im geraden
Sektor stimmen bei 768 und 1024 Bit in allen 70 ausgegebenen signifikanten
Stellen überein. Das ist eine Stabilitätskontrolle; eine vollständige
Eigenwertisolation des Spektrums wurde nicht durchgeführt.

**Die Konzentration in niedrigen Graden rechtfertigt keine Trunkierung.**
Ein Normrest von beispielsweise einem Prozent ist gegenüber einer Reserve der
Größenordnung 10⁻⁴² riesig. Auch sehr kleine höhere Koeffizienten können für das
Vorzeichen entscheidend sein. Ebenso ist nicht bewiesen, dass drei Richtungen
den gesamten künftig kritischen Raum erfassen.

### Die Schwäche besteht schon im niedrigen physischen Block

Entlang der ersten kritischen Richtung beträgt der Schur-Kopplungsabzug relativ
zum niedrigen Modellwert:

| Terminal | Gerade | Ungerade |
|---|---:|---:|
| A8 | 29,43 % | 12,68 % |
| A9 | 31,84 % | 14,53 % |
| A11 | 12,27 % | 22,26 % |

Die extrem kleinen Werte entstehen also in diesen Richtungen nicht erst durch
eine fast vollständige Subtraktion des hohen Kopplungsabzugs. Bereits der
niedrige Modellwert ist extrem klein.

Zusätzlich wurden explizite rationale Koeffizientenvektoren aus der Diagnose
erneut mit den **vollen niedrigen Modellintervallen**, dem dokumentierten Fehler
\(\pm e_L\|v\|^2\) und der vollständigen Mellin-Normkorrektur ausgewertet.
Für die so definierten geraden physischen Quellen ergeben sich insbesondere
folgende obere Rayleigh-Schranken:

| Terminal | Gerichtete obere Schranke für q[u]/‖u‖², hier nach außen gerundet |
|---|---:|
| A8 | < 1,610 · 10⁻²⁶ |
| A9 | < 1,513 · 10⁻³¹ |
| A11 | < 1,081 · 10⁻⁴¹ |

Diese Auswertung setzt die vorhandenen analytischen Modellfehlerbindungen
voraus. Sie ist eine Aussage über konkrete Quellen, kein Beweis ihrer
Extremalität. Sie zeigt aber: Eine kleine physische Reserve ist nicht bloß ein
Artefakt der abschließenden Frobenius- oder Schur-Normschranke.

## 3. Physische Richtungen bleiben erstaunlich ähnlich

Bloßes Auffüllen von Koeffizientenlisten mit Nullen ist kein physischer
Transport. Für den Vergleich wurde aus jedem Vektor die momentkorrigierte
Legendrequelle f_A rekonstruiert und

\[
u_A(t)=(2A)^{-1/2}f_A(t/A),\qquad |t|<A,
\]

außerhalb des Trägers nullgesetzt. Für A < B wurde daher tatsächlich

\[
\langle u_A,u_B\rangle
=\frac{\sqrt{A/B}}2\int_{-1}^{1}
 f_A(x)f_B((A/B)x)\,dx
\]

ausgewertet und durch beide physischen Normen geteilt.

| Vergleich | Absoluter normierter Überlapp der ersten Richtung, gerade | Ungerade |
|---|---:|---:|
| A8 → A9 | 0,999958565 | 0,999938047 |
| A9 → A11 | 0,999915786 | 0,999882932 |
| A8 → A11 | 0,999756248 | 0,999650776 |

Auch die jeweiligen drei untersuchten Richtungen bilden ähnliche physische
Unterräume: Der kleinste Hauptwinkelkosinus benachbarter Dreier-Unterräume
beträgt 0,998448 oder mehr. Von A8 direkt zu A11 sind es mindestens 0,995462.

Diese Winkel sind gewöhnliche Gleitkomma-Diagnostik. Zwei Gaussregeln mit 640
und 704 Knoten stimmen in den Überlappmatrizen auf besser als 10⁻¹⁰ überein.
Die mathematischen Integranden sind Polynome und liegen im Exaktheitsbereich
beider Regeln; die Rechnung selbst benutzt dennoch gerundete Knoten und Werte.
In der Datendatei ebenfalls ausgewiesene extrem kleine äußere Trägermassen
liegen teilweise an der Gleitkomma-Auflösungsgrenze und werden hier nicht als
Schranken interpretiert.

**Folgerung für die Forschung:** Es lohnt sich, einen physisch mitgeführten
kritischen Unterraum zu suchen. Ähnlichkeit in L² kontrolliert jedoch noch
keinen Fehler relativ zur winzigen Formreserve.

## 4. Die naive Matrixmonotonie scheitert bereits exakt

Vergleicht man gleich benannte Legendrekoordinaten auf dem Referenzintervall
und beschränkt beide Matrizen auf ihre gemeinsame Dimension, besitzt jede
untersuchte Differenz sowohl positive als auch negative Diagonaleinträge.
Beispiele im geraden Sektor:

| Differenz der F-Matrizen | Negativer Diagonalzeuge | Positiver Diagonalzeuge |
|---|---:|---:|
| A9 − A8, gemeinsame Dimension 191 | Grad 22: −0,6014657934 | Grad 382: +0,9411753396 |
| A11 − A9, gemeinsame Dimension 285 | Grad 20: −0,9209475704 | Grad 22: +0,6278227814 |

Die Vorzeichen wurden mit ganzzahligen Intervallgrenzen direkt aus den
gebundenen Dateien nachgerechnet. Sie hängen nicht von einem approximativen
Eigenwertsolver ab. Die analogen ungeraden und nicht benachbarten Vergleiche
stehen in den Ergebnisdateien.

Damit ist in dieser Identifikation weder F_neu ≥ F_alt noch F_neu ≤ F_alt
möglich. **Dies widerlegt keinen geeigneten Vergleich unter physischem
Transport oder nach einer begründeten Basisänderung.** Endpunkt, Mellinabbildung,
Tail-Schnitt und hoher Boden ändern sich gleichzeitig. Die Differenz darf auch
nicht dem jeweils neu aktivierten Kanal allein zugeschrieben werden.

## 5. Gemeinsames Muster der Basiswechsel — mit einer Grenze

Für alle sechs Mittelpunktsmatrizen wurde dieselbe geordnete Zerlegung
F = LDL* und die diagnostische Basis P = L⁻* gebildet. Normalisierte gemeinsame
Spalten benachbarter Terminals sind ähnlich: An den untersuchten Spalten liegen
ihre absoluten Kosinuswerte zwischen ungefähr 0,981 und 0,997.

Die Normkosten wachsen jedoch stark. Im geraden Sektor ist diagnostisch

| Terminal | ‖P‖²_F |
|---|---:|
| A8 | 1,56424 · 10²⁶ |
| A9 | 1,79946 · 10³¹ |
| A11 | 2,10066 · 10⁴¹ |

P = L⁻* ist für jede positiv definite Matrix verfügbar. Das gemeinsame
Rezept allein ist deshalb noch keine vom Terminalrechner unabhängige Struktur.
Der A11-Beweis bezahlt die Normrückrechnung bereits ausdrücklich; diese
Untersuchung verändert weder seinen rationalen P noch seine zertifizierte
Reserve. Siehe [A11-Basiswechsel](https://github.com/Waschtl904/objekt-x-programm/blob/d16ba43ebb20f2c61f43379fc65d7a9b9dba76de/research/x-c1/chambers-through-a11-2026-09-28/a11/PRECONDITIONING.md).

## 6. Präzise Form eines möglichen Erneuerungsschritts

Ein geeigneter Satz muss die Änderung **relativ zur alten Formenergie**
kontrollieren. Folgendes elementare Blockkriterium formuliert ein konkretes
Beweisziel, ohne seine Voraussetzungen für die Kammerfamilie zu behaupten.

Sei S > 0 die alte, bereits gesicherte Matrix. Nach einer begründeten
Koordinatenidentifikation und vollständiger hoher Elimination habe eine
Untergrenze für den neuen Rest die Form

\[
\mathcal S_{\rm neu}\succeq
\begin{pmatrix}S+E&C\\C^*&D\end{pmatrix},\qquad D\succeq dI>0.
\]

Falls

\[
E\succeq-\varepsilon S,\qquad
CD^{-1}C^*\preceq\kappa S,\qquad
\varepsilon+\kappa<1,
\]

folgt

\[
S+E-CD^{-1}C^*\succeq(1-\varepsilon-\kappa)S>0.
\]

Der vollständige Block ist positiv: Quadratische Ergänzung schreibt seine
Form als diese positive Restform plus
\(\|D^{1/2}(y+D^{-1}C^*x)\|^2\).
Für eine quantitative Reserve in ursprünglichen Koordinaten sind zusätzlich
die Basis- und Scher-Normen zu bezahlen.

Die Forschungsaufgabe liegt darin, S, E, C und D **ohne erneute vollständige
Terminalzerlegung** zu konstruieren und die relativen Schranken zu beweisen.
Die drei erfolgreichen Datenpunkte liefern hierfür ein Motiv, noch keinen Satz.
Ein positiver Schritt für jeden endlichen Horizont wäre außerdem von einer
globalen positiven Grenzkonstruktion und ihrer Kompatibilität zu unterscheiden.

### Zwei notwendige Strukturklärungen

1. **Physische Nullfortsetzung erzeugt im Allgemeinen unendlich viele neue
   Legendrekoeffizienten.** Ein nichttriviales altes Polynom ist nach
   Nullfortsetzung auf dem größeren Intervall kein einziges Polynom. Eine
   endliche Blockerweiterung muss deshalb erst nach kontrollierter Projektion
   und vollständiger hoher Elimination begründet werden. Die alte und neue
   Low-Dimension allein definieren keinen passenden Einbettungsblock.
2. **Ein neuer Kanal ist nicht automatisch eine Störung endlichen Ranges.**
   Partielle Translationen wirken auf unendlichdimensionalen Funktionsräumen.
   Auch Formnaturality allein gibt keinen nach unten monotonen Schurrest:
   Sobald bei festgehaltenen Low-Koordinaten über mehr hohe Richtungen minimiert
   werden darf, kann das Infimum sinken. Ob die dafür nötige
   Koordinatenverträglichkeit besteht, muss zuvor gezeigt werden.

## 7. Nächster abgegrenzter Forschungsblock

1. **Transport der kritischen Quellen definieren.** Die physische
   Nullfortsetzung einschließlich ihrer neuen Low-/High-Anteile ausdrücklich
   darstellen. Die hier gefundenen Richtungen dienen als Diagnose, nicht als
   bereits analytisch erklärte Basis.
2. **Einen analytisch beschreibbaren kritischen Unterraum suchen.** Seine
   Definition soll nicht voraussetzen, dass die neue Terminalmatrix schon
   diagonalisiert wurde. Drei Richtungen sind ein Startpunkt für Experimente;
   die notwendige Dimension und eine Reserve auf dem Komplement sind offen.
3. **Die gewichteten Kopplungsgrößen messen und anschließend abschätzen.**
   Entscheidend sind Größen wie
   S⁻¹ᐟ² C D⁻¹ C* S⁻¹ᐟ² und der negative Anteil von S⁻¹ᐟ² E S⁻¹ᐟ²,
   einschließlich aller Modell- und Eliminationsfehler.
4. **Das Kriterium an A8 → A9 und A9 → A11 testen.** Erst wenn dieselbe
   Konstruktion beide Übergänge erklärt, ist eine Anwendung auf weitere
   Kammern ein sinnvoller Test eines Erneuerungsmechanismus.

Die integrierten Ergebnisse bleiben das Fundament. Der erste Vergleich liefert
eine konkrete Richtung für den neuen Block: **ähnliche schwache physische
Richtungen, kontrolliert in ihrer eigenen Formenergie**.

## Daten und Reproduktion

- [Diagnosen und Quellhashes](diagnostics.json)
- [Explizite kritische Koeffizientenvektoren](critical_vectors.json)
- [Physische Winkelvergleiche](physical_angles.json)
- [Exakte Vorzeichen- und gerichtete Formauswertung](verification.json)
- [A11-Gegenrechnung bei 1024 Bit](precision-check.json)
- [Reproduktionsanleitung](REPRODUKTION.md)

**Status:** lokaler Strukturvergleich; numerische Hinweise und ausdrücklich
begrenzte Intervallbefunde. Keine Registry-Promotion, kein allgemeiner
Low-Positivitätssatz und keine Änderung am globalen Verifikationssnapshot.
