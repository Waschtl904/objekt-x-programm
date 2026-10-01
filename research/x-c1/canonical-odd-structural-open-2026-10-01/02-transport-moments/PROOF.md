# Gemeinsame Transportmomente für die ungerade Maximiererfrage

30. September 2026 · A9 nach A11 · lokaler Forschungsblock

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

Ausgangspunkt: `main@689ff6266b5e4d58700f82eae3016951a023e353`.
Positiver generalisierter Extremalgap und Eindeutigkeit in beiden Paritäten
sind abgeschlossene Voraussetzungen dieses Blocks.

## Ergebnis

**Die vollständige gemeinsame b-Grammatrix allein lokalisiert die ungerade
Maximierergerade noch nicht eng.** Zwei neue exakt rationale Beispiele
erfüllen die bisherigen ausdrücklich geprüften Momentbedingungen und nun
auch diese Grammatrix. Ihre oberen physischen Eigenrichtungen liegen im
selben A11-Raum mindestens **89.987266 Grad** auseinander. Die Eigenwerte bleiben einfach
und innerhalb der geerbten Einschließungen.

Eine stärkere notwendige Bedingung aus dem bestehenden Transportlemma
schließt jedoch **beide** Beispiele aus. Sie koppelt die verbleibende Masse
und Energie des übertragenen A9-Raums an den hohen A11-Spektralschnitt.
Die getrennten Restmatrizen sind positiv. Erst ihre gemeinsame spektrale
Ordnungsrelation scheitert, und zwar in einer gemischten Matrixrichtung.
Sogar sämtliche Diagonaleinträge der verletzten Matrix sind positiv.

Damit ist weder ein Gegenmodell zum tatsächlichen Operatorpaar noch ein
tatsächlicher ungerader Winkelbereich bewiesen. Der Block benennt und
prüft eine konkretere fehlende Kopplung. Die bandweisen Momente des
tatsächlichen Maximierers bleiben anschließend offen.

## Vollständige kritische Koordinaten

Für die vollständigen projizierten Trialbasen setze

\[
V_A=P_AU_A,\quad V_B=P_BU_B,\quad
G_A=V_A^*V_A,\quad L_A=V_A^*Q_AV_A,
\quad G_B=V_B^*V_B,\quad L_B=V_B^*Q_BV_B.
\]

Diese Matrizen haben Größen sechs bzw. acht; es sind nicht die Zweiermatrizen
des Extremalproblems. Positive Gram-Matrizen und die zertifizierten Ränge
stellen sicher, dass V_B den gesamten kritischen A11-Raum aufspannt. Definiere

\[
B_A=G_A+L_A/17,\qquad B_B=G_B+L_B/17,
\qquad Y=\frac1{17}b_B(JV_A,V_B).
\]

Die bisher zusätzlich geforderte gemeinsame Bedingung ist

\[
\begin{pmatrix}B_A&Y\\Y^*&B_B\end{pmatrix}\succeq0.\tag{1}
\]

Formnaturality und physische Nullfortsetzung liefern exakt

\[
J^*J=I,\qquad q_B(Ju,Jv)=q_A(u,v).\tag{2}
\]

Die unveränderten Beweistexte `inputs/TRANSPORT_LEMMA.md` und
`inputs/SPECTRAL_RANKS.md` binden diese Voraussetzungen an den kanonischen
Stand. (2) ist eine Identität der Formen, keine Vertauschungsbehauptung
über die vollständigen Operatoren oder deren Inversen.

## Die gemeinsame Spektralbedingung

Die Spektralprojektion ist auch b-orthogonal. Weil V_B den gesamten
kritischen Raum aufspannt, folgt aus den Gram-Koordinaten exakt

\[
\boxed{P_BJV_A=V_B B_B^{-1}Y^*.}\tag{3}
\]

Denn die b-Grammatrix von V_B ist 17 B_B und der Kreuzblock ist 17 Y*.
Für den hohen Rest H=(I−P_B)JV_A ergeben (2), (3) und spektrale Orthogonalität

\[
\boxed{\mathsf H_0=H^*H
=G_A-YB_B^{-1}G_BB_B^{-1}Y^*,}\tag{4}
\]

\[
\boxed{\mathsf H_1=H^*Q_BH
=L_A-YB_B^{-1}L_BB_B^{-1}Y^*.}\tag{5}
\]

Der geerbte physische Schnitt auf dem vollständigen hohen A11-Raum ist
ν_B=0.070769. Deshalb gilt notwendig

\[
\boxed{\mathsf H_1\succeq\nu_B\mathsf H_0\succeq0.}\tag{6}
\]

Dies ist die matrixielle Auswertung des vorhandenen Transportarguments.
Außerdem folgt exakt

\[
\mathsf H_1+17\mathsf H_0
=17(B_A-YB_B^{-1}Y^*).\tag{7}
\]

(1) kontrolliert diese Summe. (6) fordert zusätzlich das richtige
Verhältnis von Energie und Masse auf demselben hohen Spektralrest.
Die neuen Matrizen betreffen **übertragene alte kritische Vektoren**;
sie sind nicht die bisherigen hohen Trialmomente von U_B.

## Zwei neue Beispiele in der schwächeren Familie

Die gemeinsamen Kammermomente entstehen wie im vorigen lokalen Paket aus
symmetrisierten rationalen Mittelpunkten S,T und dem geerbten Schnitt ν:

\[
A=\nu I-S,\quad K=\nu^2T-2\nu I+S,\quad L_P=AK^{-1}A,
\quad G_P=(L_P+A)/\nu,\quad Z_P=T-(I-G_P)/\nu.
\]

Der Prüfer bestätigt alle Eingabeordnungen und exakt
Z_P=G_P L_P^−1 G_P. Die Momente stammen daher pro Kammer aus einem einzigen
positiven Spektralmaß mit den richtigen kritischen Rängen.

Sei O der feste rationale Mittelpunkt der Trialüberlappung und
N₀=[−O_l^−1 O_r;I₂]. Setze

\[
w=(0,0,0,0,3/10000,-23/1000)^T,\quad u=O^*w,\quad v=N_0e_2,
\quad K_0=uv^*-vu^*,\quad s=\|u\|^2\|v\|^2.
\]

Wegen Ov=0 ist u*v=0. Die rationale Cayley-Drehung

\[
U_t=I+\frac{t}{1+t^2s/4}K_0+
\frac{t^2}{2(1+t^2s/4)}K_0^2
\]

ist exakt orthogonal. Die neue Überlappung lautet

\[
Y_t=G_A O U_t G_B,\qquad
t=0\quad\hbox{oder}\quad t=\frac{92709707500416459487}{10^{20}}.\tag{8}
\]

Der zweite Parameter ist eine Vorschlagszahl; seine Folgen werden exakt
verifiziert. Die numerische Suche ist keine Beweisvoraussetzung.
Aus der rational geprüften Kontraktion OO*≺I, 0≺G_A,G_B⪯I und B_B⪰G_B folgt

\[
Y_tB_B^{-1}Y_t^*\preceq G_A^2\preceq G_A\preceq B_A.
\]

Damit gilt (1) analytisch; positive gerichtete LDL-Pivots bestätigen es
zusätzlich direkt. Auch (4) und (5) sind bei beiden Beispielen positiv.
Alle vorher ausdrücklich aufgelisteten Bedingungen der äußeren
Diskriminantenfamilie werden für dieselben festen Beispiele gegen beide
Präzisionsquittungen geprüft. Dazu gehören volle gemeinsame Kammermomente,
YN=0, komprimierte Momentgrenzen sowie die geerbten Eigenwert- und Gapgrenzen.

## Obere Projektoren im selben physischen Raum

Die oberen Eigenprojektoren werden aus den exakten Zweierproblemen der
Beispiele berechnet. Für jedes Y_t bezeichnet N(Y_t)=[−(Y_t)_l^−1(Y_t)_r;I₂]
die tatsächlich zugehörige Kernbasis. Der physische Vergleich benutzt
a=N(Y_0)x₀ und c=N(Y_t)x_t und dieselbe volle A11-Grammatrix G_B:

\[
\cos^2\angle(a,c)=\frac{|a^*G_Bc|^2}{(a^*G_Ba)(c^*G_Bc)}.
\]

Die gerichtete Rechnung bestätigt mindestens **89.987266 Grad**. Die exakte
rationale Untergrenze steht in `verification.json`. Dies betrifft die
explizite schwächere Familie mit (1), nicht die zusätzlich durch (6)
eingeschränkte Familie und nicht das tatsächliche Operatorpaar.

## Exakte Zeugen gegen den hohen Spektralsupport

Für D=H₁−ν_B H₀ konstruiert der Prüfer jeweils einen rationalen Vektor a
mit fünfter Koordinate eins und sechster Koordinate null. Er verifiziert
**direkt und exakt** a*Da<0. Die erste Näherung stammt aus dem Schurkomplement
des führenden Viererblocks. Nach rationaler Rundung wird die quadratische
Form vollständig neu berechnet.

| Beispiel | Gerichtetes Intervall der negativen quadratischen Form |
| --- | ---: |
| zentral | [−8.3432193e−10, −8.3432192e−10] |
| gedreht | [−2.2492497e−9, −2.2492496e−9] |

Die Vektoren sind nicht normiert. Ihre rationalen Koordinaten und die
vollständigen gerichteten Grenzen stehen in der Quittung. Alle sechs
Diagonaleinträge von D sind trotzdem positiv. Ein reiner Diagonaltest
würde die fehlende Kopplung übersehen.

Beide Beispiele sind durch (6) ausgeschlossen. Sie werden ausdrücklich
nicht als Realisierungen des vollständigen gemeinsamen Transports ausgegeben.

## Prüfung und nächster Schritt

Das Paket bindet das unveränderte vorige Projektorarchiv und reproduziert
dessen Quittung bytegleich, einschließlich der darin ausgeführten
Schurdefekt- und Diskriminantenreplays. Ein unabhängiger nichtkommutierender
endlicher Operator prüft (3) bis (7). Negative Kontrollen unterscheiden
getrennte Gram-Positivität, positive Diagonalen und die gemeinsame Ordnung (6).

Eine frische Quellenprüfung vergleicht die beiden zusätzlichen Beweistexte
mit dem kanonischen Main-Commit und prüft erneut die älteren Operatorquellen
und publizierten Eingaben. Große Integral- und Operatorrechnungen bleiben
gebundene Voraussetzungen; sie wurden nicht neu berechnet.

**Die tatsächliche ungerade Maximierergerade bleibt quantitativ offen.**
Der nächste enge Rechenschritt ist die gemeinsame Auswertung von (4) bis
(6), den bisherigen Momenten und YN=0 über die gesamte zulässige Familie.
Der Ausschluss zweier fester Beispiele beweist noch keinen uniformen
Winkelkegel für diese Familie.

Gap, Eindeutigkeit und gerade Lokalisierung bleiben unverändert. Bandweise
Momente des tatsächlichen Maximierers werden hier nicht beansprucht.
PR #187/A13, allgemeines Renewal, eine kofinale positive Familie, globales
Objekt X und RH erhalten keinen neuen Status. Das Paket bleibt lokal;
das Repository wird nicht verändert.
