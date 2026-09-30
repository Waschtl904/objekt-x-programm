# Positiver gemeinsamer Diskriminant für die kanonischen Maximierer

30. September 2026 · **JOINT GENERALIZED DISCRIMINANT**

Wissenschaftlicher Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Lokales Prüfpaket; noch nicht im Repository integriert.

## 1 Ergebnis

Für den Übergang A9 nach A11 ist der Diskriminant des tatsächlichen
zweidimensionalen verallgemeinerten Eigenproblems **in beiden Paritäten
streng positiv**. Die Schranken gelten uniform für die unten angegebene
gemeinsame Zertifikatsfamilie und damit insbesondere für die wirklichen
kanonischen Operatorgrößen.

| Parität | \(\beta_+-\beta_-\) mindestens | \((\beta_+-\beta_-)^2\) mindestens | \(b^2-4ac\) mindestens |
| --- | ---: | ---: | ---: |
| gerade | \(2.2718906\cdot10^{14}\) | \(5.1614873\cdot10^{28}\) | \(7.0392785\cdot10^{67}\) |
| ungerade | \(4.2806927\cdot10^{11}\) | \(1.8324330\cdot10^{23}\) | \(2.0884369\cdot10^{55}\) |

Alle Tabellenwerte sind nach außen gerundet und werden getrennt mit den
gebundenen Quittungen aus 1024 und 1280 Bit bestätigt. Der endgültige neue
Prüfer rechnet ausschließlich rational.

Damit ist der größte verallgemeinerte Eigenwert jeweils einfach. Für jeden
der beiden tatsächlichen Operatorfälle gibt es genau eine maximierende
Gerade. **Gerade** wird zusätzlich ein physischer Winkelbereich von

\[
[-0.850296^\circ,\ 0.381324^\circ]
\]

zur zweiten unten definierten orthonormalen kanonischen Basisachse
zertifiziert. **Ungerade** ist eine entsprechende gemeinsame Projektivkarte
noch nicht zertifiziert. Der positive Gap und die Eindeutigkeit der
maximierenden Geraden sind davon unabhängig bereits bewiesen.

Die Zahlen betreffen den verallgemeinerten Schur-Pencil. Sie sind keine
Abstände zwischen Eigenwerten des ursprünglichen Energieoperators (Q).

## 2 Pencil und Bedeutung des Diskriminanten

Es gelten dieselben tatsächlichen kanonischen Räume und dieselbe Rohbasis
wie in den vorherigen Paketen:

\[
Y=\frac1{17}b_B(JP_AU_A,P_BU_B),\qquad
N=\begin{bmatrix}-Y_l^{-1}Y_r\\I_2\end{bmatrix},\qquad
V_0=P_BU_BN.
\]

Schreibe (G=V_0^*V_0), (L=V_0^*Q_BV_0) und
(Z=V_0^*Q_B^{-1}V_0). Dann

\[
B=L+17G,\quad
R=L+34G+289Z,\quad
M=BL^{-1}B\succ0.
\tag{1}
\]

Für reelle symmetrische Matrizen der Größe zwei gilt exakt

\[
\det(R-\beta M)=a\beta^2-b\beta+c,
\]

\[
a=\det M,\quad
b=R_{11}M_{22}+R_{22}M_{11}-2R_{12}M_{12},\quad
c=\det R.
\tag{2}
\]

Mit (t=\operatorname{tr}(M^{-1}R)=b/a) und
(d=\det(M^{-1}R)=c/a) folgt

\[
\Delta=b^2-4ac=a^2(\beta_+-\beta_-)^2.
\tag{3}
\]

Eine Normierungspräzisierung ist wichtig: Unter gemeinsamer Kongruenz
(R\mapsto H^*RH, M\mapsto H^*MH) multipliziert sich (\Delta) mit
((\det H)^4). **Das Vorzeichen ist invariant; vollständig basisunabhängig
ist (\Delta/a^2).** Die Rohbasis ist hier durch den unteren Identitätsblock
von (N) festgelegt. Eine zusätzliche uniforme Untergrenze für (a)
macht auch die letzte Tabellenspalte zu einer positiven uniformen Schranke.

## 3 Die gemeinsam zugelassene Familie

Die neuen Intervalle für (Y,N,G) kommen aus dem Projektor-/Momentenblock.
Insbesondere bleibt die exakte Beziehung (YN=0) erhalten. Die hohen
Momentverluste und die projizierten Matrizen gehören weiterhin zu demselben
positiven Spektralmaß, mit

\[
G=N^*G_PN,\quad L=N^*L_PN,\quad Z=N^*Z_PN,
\]

\[
G_P=I-D_0,\quad L_P=S_B-D_1,\quad Z_P=T-D_{-1},
\]

\[
D_1\succeq\nu D_0\succeq\nu^2D_{-1}\succeq0,
\quad
\begin{pmatrix}D_1&D_0\\D_0&D_{-1}\end{pmatrix}\succeq0,
\quad
\begin{pmatrix}L_P&G_P\\G_P&Z_P\end{pmatrix}\succeq0.
\tag{4}
\]

Der Beweis benötigt folgende bereits zertifizierte Konsequenzen:

\[
L_-\preceq L\preceq L_+,\quad L\preceq E_N:=N^*S_BN,
\quad L\preceq\theta G,
\tag{5}
\]

\[
N^*T^-N-E_N/\nu^2\preceq Z\preceq N^*T^+N,
\quad Z\succeq GL^{-1}G.
\tag{6}
\]

Hier sind (\nu>0) der geerbte Komplementboden, (\theta>0) die geerbte
kritische Energieobergrenze und (T^\pm) die vollständigen
Trialresolventenschranken. Die geerbten Faktoren erfüllen

\[
T^\pm=F_\pm^*F_\pm,\qquad
L_-=C_-C_-^*,\qquad L_+=C_+C_+^*.
\tag{7}
\]

Die Aussage gilt bereits für die größere äußere Familie mit den neuen
(Y,N,G)-Intervallen, der exakten Annullatorbeziehung und (5) bis (7).
Weitere gemeinsame Bedingungen aus (4) verkleinern diese Familie und
können die bewiesene uniforme Untergrenze nicht verschlechtern. Es werden
keine voneinander unabhängig gewählten Einträge einer transformierten
Matrix (K) als zulässige Operatorgrößen ausgegeben.

## 4 Gemeinsame Einschließung der Linearkombinationen von N

Die direkte Multiplikation einer Eintragshülle für (N) mit (F_\pm)
verliert wichtige Korrelationen. Für eine beliebige festgelegte Matrix
(F=[F_l\ F_r]) gilt dagegen exakt

\[
FN=F_r-HY_r,\qquad H=F_lY_l^{-1}.
\tag{8}
\]

Sei (M_c) die geerbte feste Zentralmatrix für (Y_l). Setze

\[
E_Y=Y_l-M_c,\quad A=E_YM_c^{-1},\quad H_0=F_lM_c^{-1}.
\]

Aus (H Y_l=F_l) folgt

\[
H(I+A)=H_0,\qquad
H-H_0=-H_0A-(H-H_0)A.
\tag{9}
\]

Für eine nichtnegative obere Eintragsmatrix (A_{abs}\ge |A|) prüft der
Certifier (\|A_{abs}\|_\infty<1). Für jede Zeile wird anschließend eine
rationale positive Überschranke (e) mit

\[
e_j>|(H_0A)_j|+\sum_k e_k(A_{abs})_{kj}
\tag{10}
\]

exakt verifiziert. Die nichtnegative Neumann-Reihe liefert daraus
(|H-H_0|\le e). (8) wird mit dieser gemeinsamen Einschließung ausgewertet
und mit der direkten Hülle (FN) geschnitten.

Die zertifizierten oberen Kontraktionszahlen sind

\[
0.0017038549\quad\text{gerade},\qquad
0.0092214770\quad\text{ungerade}.
\]

Die Zwischenmatrizen und die strikt positiven rationalen Margen von (10)
stehen in `verification.json`. Der gleiche Vorgang wird für (F_-),
(F_+) und die unten beschriebene Restmatrix ausgeführt.

## 5 Untergrenze für die Summe der Eigenwerte

Zum Beweis, ohne numerische Transformation des Pencils, verwende die
physischen orthonormalen Koordinaten

\[
\ell=G^{-1/2}LG^{-1/2},\qquad z=G^{-1/2}ZG^{-1/2}.
\]

Dann ist (0\prec\ell\preceq\theta I), und für
(f(s)=s/(s+17)^2) gilt

\[
t=\operatorname{tr}\bigl(f(\ell)(\ell+34I+289z)\bigr)
\ge\frac{289}{(17+\theta)^2}\operatorname{tr}(G^{-1}LG^{-1}Z).
\tag{11}
\]

Die Positivität von (Z), (5) und (6) ergeben

\[
\operatorname{tr}(G^{-1}LG^{-1}Z)
\ge
\|F_-NG^{-1}C_-\|_F^2
-\frac{\operatorname{tr}(G^{-1}L_-G^{-1}E_N)}{\nu^2}.
\tag{12}
\]

Die Norm wird mit der gemeinsamen Einschließung aus (8) berechnet. Ein
Intervall, das null enthält, trägt zur unteren Quadratsumme null bei.
Kein Vorzeichen oder nichtendlicher Wert wird als positives Quadrat
behandelt. Die vollständig bezahlte hohe Korrektur bleibt in (12) enthalten.
Damit entsteht die rationale Untergrenze (t\ge t_0>0).

## 6 Obergrenze für den kleineren Eigenwert

Wähle einen festen rationalen Spaltenvektor (\alpha\in\mathbb R^8)
mit (\alpha_1=1), und definiere

\[
f=e_1^*F_+,\qquad D=F_+-\alpha f.
\tag{13}
\]

Die verwendeten Zahlen stehen in `rank_one_parameters.json`. Sie sind
reine Hilfsparameter. Jeder rationale Vektor mit (\alpha_1=1) wäre
zulässig; ein günstiger Vektor macht nur die Restschranke kleiner. Der
Prüfer übernimmt keinen numerischen Optimierungserfolg als Beweis.

Der Kern der Zeile (fN) enthält einen von null verschiedenen Vektor.
Für jeden Vektor (x) in diesem Kern gilt

\[
F_+Nx=DNx,\qquad x^*Zx\le\|DNx\|^2.
\tag{14}
\]

Weiter liefert die skalare Funktion (f(\ell))

\[
M^{-1}\preceq\frac1{289}G^{-1}L_+G^{-1},
\qquad
L+34G\preceq\epsilon M,
\quad \epsilon=\frac{\theta(\theta+34)}{289}.
\tag{15}
\]

Aus der Minimumeigenschaft des kleineren verallgemeinerten Eigenwerts,
(14), (15) und der Spurabschätzung einer positiven Matrix folgt

\[
\boxed{\beta_-\le
\epsilon+\|DNG^{-1}C_+\|_F^2=:u.}
\tag{16}
\]

Genauer: Auf dem Kern von (fN) ist der Rayleigh-Quotient höchstens
(\epsilon+289\|DNx\|^2/(x^*Mx)). Der zweite Summand ist höchstens
(289\operatorname{tr}(M^{-1}N^*D^*DN)), und (15) ergibt (16).
Das gilt auch, falls die Zeile (fN) null wäre. Die elementare
Minimax-Charakterisierung des Rayleigh-Quotienten ist beispielsweise in
[Taos Vorlesungsnotizen, Satz 2 und Bemerkung 1](https://terrytao.wordpress.com/2010/01/12/254a-notes-3a-eigenvalues-and-sums-of-hermitian-matrices/)
formuliert.

Für (16) wird **(DN) unmittelbar mit (8) eingeschlossen**. Würde man
zuerst getrennte breite Intervalle für (F_+N) und (\alpha fN) bilden
und danach subtrahieren, ginge gerade die benötigte Korrelation verloren.

## 7 Uniforme positive Diskriminantenschranke

Die entscheidende Prüfung ist

\[
\boxed{t_0-2u>0.}
\tag{17}
\]

Daraus folgen gleichzeitig

\[
\beta_+\ge t_0-u>u\ge\beta_-,\qquad
\beta_+-\beta_-\ge t_0-2u=:g_0>0.
\tag{18}
\]

Dies ist eine Aussage über denselben gemeinsamen Pencil. Es werden
keine getrennten Extremwerte aus unverträglichen Daten zu einem
scheinbaren Eigenpaar zusammengesetzt.

| Parität | Untergrenze \(t_0\) | Obergrenze \(u\) |
| --- | ---: | ---: |
| gerade | \(2.2793337\cdot10^{14}\) | \(3.7215526\cdot10^{11}\) |
| ungerade | \(1.3753124\cdot10^{12}\) | \(4.7362158\cdot10^{11}\) |

Die genaueren Zahlen in (17) sind rationale Werte der Quittung; die
gerundeten Tabellenwerte werden nicht rückwärts als Recheninputs benutzt.

Für (a=\det M) liefert (1)

\[
a=\frac{\det(L+17G)^2}{\det L}
\ge\frac{17^4\det(G)^2}{\det E_N}.
\tag{19}
\]

Der Prüfer verwendet zusätzlich die kleinere der vorhandenen oberen
Schranken für (\det E_N) und (\det L_+). Dadurch erhält er

\[
a\ge a_0,
\qquad a_0\ge
\begin{cases}
3.6929773\cdot10^{19}&\text{gerade},\\
1.0675706\cdot10^{16}&\text{ungerade}.
\end{cases}
\]

Aus (3), (18), (19) folgt die gesuchte Antwort

\[
\boxed{\inf_{\text{gemeinsam zulässige Daten}}\Delta
\ \ge\ a_0^2g_0^2\ >0.}
\tag{20}
\]

Der Wert des Infimums wird nicht exakt bestimmt. Bewiesen ist eine uniforme
positive Untergrenze. Der Code speichert auch Einschließungen für (a,b,c).
Eine erneute unabhängige Intervallauswertung von (b^2-4ac) aus diesen
äußeren Koeffizientenboxen würde Korrelationen verlieren und ist nicht der
Nachweis von (20).

Es wird keine Cholesky-Transformation von (M) berechnet. Die bereits
geerbten Faktoren in (7) dienen der gemeinsamen Normauswertung.

## 8 Eigenwerte und relative Schurreserve

Aus (Z\succeq GL^{-1}G) folgt (R\succeq M), also (\beta_-\ge1).
Für den größeren Eigenwert gilt ergänzend

\[
\beta_+\le\|F_+NG^{-1}C_+\|_F^2+\epsilon.
\tag{21}
\]

Die folgenden disjunkten Intervalle stimmen mit der positiven Wurzelwahl
in (\beta_\pm=(b\pm\sqrt\Delta)/(2a)) überein:

| Parität | \(\beta_-\) | \(\beta_+\) |
| --- | --- | --- |
| gerade | \([1,\ 3.7215526\cdot10^{11}]\) | \([2.2756122\cdot10^{14},\ 4.4631121\cdot10^{15}]\) |
| ungerade | \([1,\ 4.7362158\cdot10^{11}]\) | \([9.0169084\cdot10^{11},\ 1.0546191\cdot10^{16}]\) |

Die geerbte quadratische Konvention für \(\kappa\) bleibt unverändert.
Mit (1-\kappa=1/\beta_+) folgt als Korollar:

| Parität | Neues Intervall für \(1-\kappa\) auf A9 nach A11 |
| --- | --- |
| gerade | \([2.2405890\cdot10^{-16},\ 4.3944218\cdot10^{-15}]\) |
| ungerade | \([9.4820969\cdot10^{-17},\ 1.1090276\cdot10^{-12}]\) |

Das sind Einschließungen, keine Bestimmung eines einzelnen tatsächlichen
Exponenten. Die früheren gültigen Intervalle werden dadurch verengt.

## 9 Richtung und physischer Winkel

Erst nach der Trennung der Eigenwerte wird

\[
(R-\beta_+M)x=0
\]

ausgewertet. Gerade ist der Nenner der ersten Zeile streng von null
getrennt. Deshalb ist (x_2\ne0), und nach Wahl (x_2=1) gilt

\[
\frac{x_1}{x_2}
=\frac{\beta_+M_{12}-R_{12}}{R_{11}-\beta_+M_{11}}
=\frac{M_{12}-R_{12}/\beta_+}{R_{11}/\beta_+-M_{11}}
\in[-0.0058383588,\ 0.011976753].
\tag{22}
\]

Beide algebraisch identischen Formen werden eingeschlossen und geschnitten.
Die zweite Form verringert die wiederholte Abhängigkeit von (\beta_+).

Für den physischen Winkel sei (G=C_GC_G^*) mit positivem unteren
Cholesky-Faktor und (V=V_0C_G^{-*}). Dann ist (V) L2-orthonormal, und
der tatsächliche Antwortvektor (V_0x) hat darin Koordinaten (z=C_G^*x).
Für (r=x_1/x_2) ist

\[
\frac{z_1}{z_2}=\frac{G_{11}r+G_{12}}{\sqrt{\det G}}.
\tag{23}
\]

Der Winkel wird von der zweiten Basisachse in Richtung der ersten gemessen,
mit Orientierung (x_2>0). Gerichtete rationale Arkustangensreihen und
die Machin-Identität für (\pi) ergeben

\[
\angle_{L^2}(V_0x,V e_2)\in[-0.850296^\circ,\ 0.381324^\circ].
\tag{24}
\]

Dies ist ein physischer L2-Winkel in der ausdrücklich angegebenen Basis.
Es ist kein Winkel in den durch (M) normierten Koordinaten.

Ungerade enthält die momentan verfügbare Nennerhülle null. Der Bericht
behauptet deshalb weder (x_2\ne0) noch einen ungeraden physischen Winkel.
Aus diesem Intervallbefund folgt nicht, dass der wahre Nenner null ist.
Die einfache maximale Eigenwertgerade ist durch (20) bereits gesichert;
ihre weitere räumliche Lokalisierung bleibt der nächste offene Schritt.

Die Richtung in (22) bis (24) gehört zum maximierenden
**inversen Antwortvektor** (V_0x). Die zugehörige Schur-Verschiebung ist
(V_0L^{-1}Bx); ihr Winkel wird hier nicht mit diesem Winkel gleichgesetzt.

## 10 Prüfung und Beweisbindung

Der endgültige Prüfer verwendet Python-Standardbibliothek und gerichtete
rationale Intervalle mit 160 Dezimalstellen für die Rundung nach außen.
Er prüft beide geerbten Präzisionsquittungen vollständig. Die Hilfsparameter
aus (13) werden als feste rationale Zahlen eingelesen und im Ergebnis
zusätzlich per SHA-256 gebunden.

Die Quellenprüfung liest erneut 25 ursprüngliche Repository-Dateien am
mathematischen Beweisanker
`8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b` und vier veröffentlichte Inputs
am Forschungshead `b5dc05f7fcc133ab2aeb3132d4bce0fa74f55a5d`.
Zwei weitere Inputs werden bytegenau gegen das unveränderte lokale
Projektorarchiv mit SHA-256
`6fda15548fe850146806604ec1272f68ea5db62684b76d440f9e62aa26fa882b`
geprüft.

Die Abnahme umfasst die exakte nichtkommutierende Determinantenidentität,
ihre Kongruenztransformation, eine exakte Doppelwurzel als Negativkontrolle,
einen unabhängigen Test der gemeinsamen Funktionale, fehlgeschlagene
Kontraktion, Winkelausrichtung, Nullteiler, manipulierte Inputdatei und
ungeeignete Rang-eins-Parameter. Der zweite vollständige Replay muss
dieselbe JSON-Datei und identische LF-Bytes liefern. Berichtstabellen,
Manifest und ZIP werden separat geprüft.

Die vollständigen früheren Integral- und Operatorrechnungen bleiben
gebundene Voraussetzungen. Sie wurden nicht neu berechnet. Der aktuelle
lokale Integrationsstand bleibt
`c53856b453564621a06124b7ec4f85a27acfa727`; dieses Paket und der vorherige
Projektorblock sind weiterhin lokale neue Forschungsergebnisse.

## 11 Aussagegrenze und nächster Schritt

Der neue Ausgang ist positiv: Die verstärkte gemeinsame Familie erzwingt
einen positiven tatsächlichen verallgemeinerten Gap in beiden Paritäten.
Die bisherigen Gegenmodelle können daher innerhalb dieser Familie auch
nicht durch ein anderes exaktes Doppelmodell ersetzt werden.

Gerade ist außerdem eine Projektivkarte samt physischem Winkelbereich
zertifiziert. Ungerade bleibt die gemeinsame Richtungslokalisierung offen.
Bandweise Spektralmomente des tatsächlichen Maximierers wurden in diesem
Block noch nicht berechnet. Die bekannten Momentzeugen dürfen weiterhin
nicht ohne Nachweis als tatsächliche Maximierer bezeichnet werden.

Bestehende Terminalpositivität ist weiterhin ein Input. Vorwärts-Erneuerung,
kofinale Positivität, globales Objekt X und RH erhalten keinen neuen Status.
PR #187 und A13 gehören nicht zum vorliegenden Block.
