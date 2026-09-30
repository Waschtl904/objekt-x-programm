# Gemeinsame Spektralmomente schärfen die projizierten Überlappungen

30. September 2026 · Lokaler Forschungsblock · **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

## 1 Ergebnis

Die gemeinsame Herkunft der Energie und der inversen Energie aus demselben
positiven Spektralmaß liefert eine zusätzliche Projektorschranke. Damit lassen
sich für den Übergang A9 nach A11 **beide fest konstruierten `axis_one`
Alternativen und die ungerade `double` Alternative streng ausschließen**.
Der rationale Prüfer bestätigt jeden Ausschluss getrennt mit den gebundenen
Resolventenquittungen aus 1024 und 1280 Bit.

Das im Auftrag verlangte Mindestziel des Blocks
**CERTIFIED PROJECTED OVERLAP / JOINT SPECTRAL MOMENTS** ist damit erreicht.
Die tatsächlichen Projektoren wurden dabei über gemeinsame Momente enger
eingeschlossen. Ihre vollständige direkte Berechnung und die Isolierung der
tatsächlichen Extremalrichtung bleiben offen. Insbesondere folgt aus dem
Ausschluss dieser drei festen Alternativen noch kein positiver tatsächlicher
Extremalgap und kein Ausschluss aller anderen entarteten Vervollständigungen.

Für dieses Ergebnis genügt eine neue Auswertung der bereits zertifizierten
vollständigen Resolventenmomente. Der vorgeschlagene verschobene rationale
Spektralfilter bleibt eine mögliche weitere Verbesserung.

## 2 Unveränderte Operatoren und Quellen

Es gelten die bisherigen physischen Quellenräume und die positive terminale
Form (Q) am endlichen Horizont bis A11. Mit

\[
\mathcal A=Q(Q+17I)^{-1},\qquad
P=1_{(0,10^{-4})}(\mathcal A),\qquad R=I-P
\]

ist (P) der echte kritische Spektralprojektor. Die gebundenen Rangnachweise
liefern Rang 6 auf A9 und Rang 8 auf A11, jeweils pro Parität. Auf dem
Komplement gilt (Q|_{\operatorname{ran}R}\succeq\nu I).

| Terminal | Parität | Exakter Komplementboden \(\nu\) |
| --- | --- | ---: |
| A9 | gerade | 0.003761 |
| A9 | ungerade | 0.065841 |
| A11 | gerade | 0.003755 |
| A11 | ungerade | 0.070769 |

Die physisch orthonormalen Trialspalten (U) sind unverändert. Setze

\[
S=U^*QU,\qquad T=U^*Q^{-1}U,\qquad T^-\preceq T\preceq T^+.
\]

Die Matrizen (T^\pm) sind die bereits zertifizierten Schranken mit bezahlter
vollständiger hoher Antwort. Sie sind keine Inversen einer als vollständig
ausgegebenen Trunkierung. Die bestehende Terminalpositivität bleibt eine
Voraussetzung; ihr kleiner globaler Boden wird hier nicht numerisch invertiert.

`input_bindings.json` bindet fünf unveränderte Dateien. Die ursprünglichen
25 Repository-Inputs wurden erneut gegen Git-Commit
`8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b` geprüft. Die fünf übernommenen
Paketdateien stimmen zusätzlich bytegenau mit dem veröffentlichten Forschungshead
`b5dc05f7fcc133ab2aeb3132d4bce0fa74f55a5d` überein.
`source_audit.json` enthält Pfade, Hashes und Prüfstatus.

Der Integrationsstand zu Beginn dieses Blocks ist
`c53856b453564621a06124b7ec4f85a27acfa727`. Er ändert keine älteren Beweisanker.
Der vorliegende Block ist lokal und noch nicht in das Repository integriert.

## 3 Ein gemeinsames Residuum aus Energie und Resolvente

Definiere

\[
C=(T^+)^{-1},\qquad
\mathcal D=Q^{1/2}U-Q^{-1/2}UC.
\]

Alle Spalten sind wohldefiniert: (U) liegt in der Formdomäne und die geerbte
strikte Positivität macht (Q^{-1/2}) beschränkt. Aus (U^*U=I) folgt exakt

\[
\mathcal D^*\mathcal D
=S-2C+CTC
\preceq S-2C+CT^+C
=S-C=:E.
\tag{1}
\]

Damit ist insbesondere (E\succeq0). Hier werden (S) und (T) gemeinsam
verwendet. Eine unabhängige Wahl beider Momente ohne gemeinsamen Operator würde
die Identität für das Residuum nicht rechtfertigen.

Die allgemeine Einordnung solcher Kompressionsbeziehungen liefert die
Operator-Jensen-Ungleichung; siehe Hansen und Pedersen, Satz 2.1 in
[Jensen’s Operator Inequality](https://arxiv.org/pdf/math/0204049).
Die für diesen Block benötigte Beziehung (1) ist oben unmittelbar bewiesen.

Für jede Spalte setze

\[
w_j=\|Q^{1/2}RUe_j\|.
\]

Weil (R) mit den Spektralfunktionen von (Q) kommutiert, gilt

\[
Q^{1/2}RUe_j=R\mathcal D e_j+
Q^{-1/2}RUCe_j.
\]

Auf dem hohen Raum ist

\[
\|Q^{-1/2}RUe_k\|
=\|Q^{-1}Q^{1/2}RUe_k\|
\le\nu^{-1}w_k.
\]

Mit (1) ergibt das die komponentenweise Ungleichung

\[
w_j\le\sqrt{E_{jj}}+
\sum_k\frac{|C_{kj}|}{\nu}w_k.
\tag{2}
\]

Der Prüfer bildet eine rationale nichtnegative obere Matrix (B) für

\[
B_{jk}=|C_{kj}|/\nu
\]

und prüft (\|B\|_\infty<1). Die Neumann-Reihe ist dann nichtnegativ.
Für rationale obere Zahlen (a_j\ge\sqrt{E_{jj}/\nu}) wird ein positiver
Vektor (r) berechnet und anschließend **exakt** geprüft:

\[
r_j-a_j-\sum_k B_{jk}r_k>0\quad\text{für alle }j.
\tag{3}
\]

Aus (2), (3) folgt (w_j\le\sqrt\nu\,r_j). Zusätzlich gilt direkt

\[
w_j^2\le S_{jj}.
\]

Mit nach oben gerundetem

\[
\eta_j=\min\{r_j,\sqrt{S_{jj}/\nu}\}
\]

erhalten wir gleichzeitig

\[
\boxed{
\|RUe_j\|^2\le\eta_j^2,\qquad
\|Q^{1/2}RUe_j\|^2\le\nu\eta_j^2,\qquad
\|Q^{-1/2}RUe_j\|^2\le\eta_j^2/\nu.}
\tag{4}
\]

Die zweite Aussage bleibt auch nach der Minimumsbildung gültig, weil beide
beteiligten Schranken unabhängig die hohe Energie kontrollieren.

## 4 Neue Projektorfehler und gemeinsame Momente

Die größte neue Spaltenschranke steht jeweils in der letzten Trialspalte.
Die folgenden oberen Zahlen gelten für beide Quittungen. Die Spalten aller
Matrizen und sämtliche exakten rationalen Zahlen stehen in `verification.json`.

| Terminal | Parität | Neue obere Schranke für die letzte Spalte | Obere Zeilensumme von \(B\) |
| --- | --- | ---: | ---: |
| A9 | gerade | 0.0060977804 | 0.000559125 |
| A9 | ungerade | 0.022291085 | 0.001734787 |
| A11 | gerade | 0.0084182831 | 0.000829206 |
| A11 | ungerade | 0.019123978 | 0.002062729 |

Die früheren einheitlichen Projektorfehler betrugen ungefähr 0.02443,
0.04729, 0.03002 und 0.04933. Diese Größen sind Normschranken, keine gemessenen
Winkel oder exakten Fehlerwerte. Die übrigen neuen Spaltenschranken sind
teilweise sehr viel kleiner; beispielsweise liegt die erste gerade A11-Spalte
unter (1.879\cdot10^{-20}).

Für das gemeinsame Matrixmaß

\[
\Sigma(I)=U^*E_Q(I)U
\]

definiere die drei hohen Momente

\[
D_1=\int_{\rm hoch}\lambda\,d\Sigma,\quad
D_0=\int_{\rm hoch}d\Sigma,\quad
D_{-1}=\int_{\rm hoch}\lambda^{-1}d\Sigma.
\]

Dann gelten gleichzeitig

\[
G_P=I-D_0,\qquad L_P=S-D_1,\qquad Z_P=T-D_{-1},
\tag{5}
\]

\[
D_1\succeq\nu D_0\succeq\nu^2D_{-1}\succeq0,
\qquad
\begin{pmatrix}D_1&D_0\\D_0&D_{-1}\end{pmatrix}\succeq0.
\tag{6}
\]

Die Blockpositivität folgt durch Integration der positiven äußeren Produkte
mit Faktoren (\sqrt\lambda) und (1/\sqrt\lambda). Dieselbe Argumentation
auf dem kritischen Band liefert

\[
\begin{pmatrix}L_P&G_P\\G_P&Z_P\end{pmatrix}\succeq0.
\tag{7}
\]

(4) kontrolliert die Diagonalen der drei hohen Momente. Ihre Einträge sind
durch Cauchy–Schwarz eingeschlossen:

\[
|(D_1)_{ij}|\le\nu\eta_i\eta_j,\quad
|(D_0)_{ij}|\le\eta_i\eta_j,\quad
|(D_{-1})_{ij}|\le\eta_i\eta_j/\nu.
\tag{8}
\]

Diagonal ist jeweils zusätzlich die untere Schranke null gültig. (8)
behauptet ausdrücklich keine Gleichheit (D_1=\nu D_0).
Die aus (5), (8) ausgegebenen Eintragsintervalle gehören zu derselben
Operatorfamilie; sie ersetzen die Beziehungen (5) bis (7) nicht durch frei
wählbare, voneinander unabhängige Matrizen.

Außerdem folgt

\[
G_P\succeq\left(1-\sum_j\eta_j^2\right)I\succ0.
\tag{9}
\]

Für die vier Tabellenzeilen liegen zertifizierte untere Schranken des Faktors
in (9) über 0.999962810, 0.999503024, 0.999929109 und 0.999634155.
Damit bleiben die projizierten Trialspalten voller Rang.

## 5 Engere gemeinsame Überlappungen

Für A=A9, B=A11 seien (J) die physische Nullfortsetzung und

\[
M=(JU_A)^*U_B,\quad
q_{A,i}=(S_A)_{ii},\quad q_{B,j}=(S_B)_{jj},\quad
\delta_j=\sqrt{1-\sum_k|M_{kj}|^2}.
\]

Wir verwenden dieselbe kanonische Größe wie zuvor:

\[
Y_{ij}=\frac1{17}\,b_B(JP_AU_Ae_i,P_BU_Be_j),\qquad b=q+17\langle\cdot,\cdot\rangle.
\]

Eine Zerlegung von (U_Be_j) entlang der orthonormalen Spalten (JU_A) ergibt

\[
|\langle JR_AU_Ae_i,U_Be_j\rangle|
\le\eta_{A,i}\left(\sum_k\eta_{A,k}|M_{kj}|+\delta_j\right).
\]

Dabei wurde (U_A^*R_AU_A=(R_AU_A)^*R_AU_A) benutzt. Für den zweiten
Projektionsverlust gilt aufgrund der erhaltenen Formenergie unter (J)

\[
|\langle JP_AU_Ae_i,R_BU_Be_j\rangle|
\le\sqrt{q_{A,i}/\nu_B}\,\eta_{B,j}.
\]

Schließlich bezahlt Cauchy–Schwarz in der positiven Form den (q/17)-Term
durch (\sqrt{q_{A,i}q_{B,j}}/17). Zusammen folgt

\[
\boxed{
|Y_{ij}-M_{ij}|\le
\eta_{A,i}\left(\sum_k\eta_{A,k}|M_{kj}|+\delta_j\right)
+\sqrt{q_{A,i}/\nu_B}\,\eta_{B,j}
+\frac{\sqrt{q_{A,i}q_{B,j}}}{17}.}
\tag{10}
\]

Beide Projektoren gehen jetzt mit den engeren gemeinsamen Momentenschranken
ein. Das neue Intervall wird zusätzlich mit der bisherigen Hülle geschnitten.

Die linke 6 mal 6 Untermatrix von (Y) bleibt in der rationalen Intervallrechnung
invertierbar. Damit wird erneut derselbe tatsächliche Annullator eingeschlossen:

\[
N=\begin{bmatrix}-Y_l^{-1}Y_r\\I_2\end{bmatrix},\quad
V_0=P_BU_BN,\quad
G_0=N^*G_PN,\quad L_0=N^*L_PN,\quad Z_0=N^*Z_PN.
\tag{11}
\]

`verification.json` enthält (Y,N,G_P,L_P,Z_P) und die drei mit demselben
(N) komprimierten Momentmatrizen. Eintragsintervall-Kompression kann erneut
Abhängigkeiten verlieren; sie wird hier nicht als erfolgreich isolierter
Extremalpencil ausgewiesen.

## 6 Strenger Ausschluss der festen Alternativen

Alle Angaben sind nach außen gerundet und gelten getrennt für beide Läufe.
Die Kandidateneinträge werden exakt aus den ursprünglichen rationalen
Parametern und den ursprünglichen Hüllen der 1280-Bit-Quittung rekonstruiert.
Ihre Definition wird nicht an die neuen Intervalle angepasst.

| Parität und Alternative | Eintrag | Neues zulässiges Intervall | Alter Kandidat ungefähr | Strikter Abstand mindestens |
| --- | --- | --- | ---: | ---: |
| gerade `axis_one` | \(Y_{68}\) | [0.026756918, 0.039360043] | 0.017518825 | 0.0092380932 |
| ungerade `axis_one` | \(Y_{68}\) | [0.032289945, 0.078619397] | 0.027686854 | 0.0046030914 |
| ungerade `double` | \(Y_{57}\) | [−0.018153854, −0.017598120] | −0.018443582 | 0.00028972889 |
| ungerade `double` | \(Y_{58}\) | [0.0014823381, 0.0020803756] | 0.0023757068 | 0.00029533127 |
| ungerade `double` | \(Y_{67}\) | [−0.31104081, −0.26805629] | −0.24371659 | 0.024339706 |

Die Abstände werden aus den exakten rationalen Intervallgrenzen berechnet.
Die gerundete Kandidatenspalte dient nur zur Orientierung. Jede einzelne
Zeile genügt zum Ausschluss der jeweiligen festgelegten Alternative.

Das frühere negative Extremalgate bleibt richtig: Seine ausdrücklich
definierte schwächere endliche Relaxation lässt die damaligen Alternativen
zu. Der vorliegende Block fügt eine weitere notwendige Operatorbeziehung
hinzu und schließt genau diese Alternativen damit aus.

## 7 Prüfung und Reproduktion

Der endgültige Prüfer benötigt nur die Python-Standardbibliothek. Er führt
die kleinen Matrixinversionen, Quadratwurzelobergrenzen, Neumann-Vergleiche,
Überlappungsintervalle und Kandidatenabstände mit rationaler gerichteter
Arithmetik aus. Nach elementaren Intervalloperationen wird auf ein rationales
Gitter mit 160 Dezimalstellen nach außen gerundet. Die strikten
Supersolutionsmargen in (3) werden danach nochmals exakt kontrolliert.

Die Abnahme umfasst beide geerbten Präzisionsquittungen, einen zweiten
deterministischen Replay, einen exakten nichtkommutierenden Spektraltest,
Ablehnung von Nullteilern, negativer Wurzel, vertauschtem Intervall,
singulärer Matrix und fehlender Spektraltrennung, sowie die frische
Quellenbindung. Manifest und ZIP werden separat kontrolliert.

Der nichtkommutierende Test verwendet ein wirkliches positives
vierdimensionales (Q), zwei orthonormale Trialspalten und dessen exakten
Projektor. Alle drei ausgegebenen Momenthüllen müssen die direkt
berechneten wahren Momente enthalten. Er testet damit auch die Bedeutung
der Schranken außerhalb der konkreten Forschungsdaten.

Die alten vollständigen Integral- und Operatorzertifikate bleiben gebundene
Voraussetzungen. Sie wurden für diese neue Folgerung nicht erneut berechnet.
Reproduktionsbefehle und Dateien sind in `REPRODUKTION.md` beschrieben.

## 8 Nächster mathematischer Schritt

Das neue Gate liefert die verlangte gemeinsame Verengung und den strengen
Ausschluss der drei bekannten Gegenmodelle. Eine weitere Extremalrechnung
kann jetzt die neuen Bedingungen (1), (5) bis (11) gemeinsam benutzen.
Ob sie bereits einen positiven tatsächlichen Gap erzwingen, muss gesondert
zertifiziert werden. Falls weitere Vervollständigungen übrig bleiben, ist
eine direkte Auswertung verschobener Spektralfilter ein geeigneter nächster
Ansatz.

Die Aussagen bleiben retrospektiv auf dem bestehenden positiven Horizont.
Vorwärts-Erneuerung, kofinale Positivität, globales Objekt X und RH erhalten
durch diesen Block keinen neuen Status.
