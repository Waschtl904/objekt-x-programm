# Neubewertung der Schalenrichtungssuche nach gemeinsamem k-Transport

17. Oktober 2026. **EXPLORATORY / EXTERNAL_REVIEW_OPEN.**
Die Matrizen und Optimierungen dieses Pakets sind ungerichtet. Die gerichteten
Einzelzertifikate #231, #233–#235 und ihre Voraussetzungen bleiben unverändert.
Insbesondere wird der in #235 entschiedene gerade Kandidat nicht erneut optimiert
oder zertifiziert. Seine Daten dienen nur als Kontrolle des neuen Suchmodells.

## 1. Abnahme vor der Suche

Eine weitere teure Einzelzertifizierung wird erst vorgeschlagen, wenn die
numerische Ausschlussmarge

\[
M(c)=|I_0(c)|-R_{common}(c)-\tau(c)
\]

mindestens 1 Prozent der Schwelle beträgt, bei beiden Auflösungen positiv
bleibt und zehnmal größer als die beobachtete skalare Kontrollabweichung ist.
Das ist ein Auswahlkriterium, keine gerichtete Fehlergrenze. Kandidatenauswahl
und gerichtete Prüfung bleiben getrennt. Dieses Paket startet keine neue
Zertifizierung und friert keinen neuen Kandidaten als Zertifikatsinput ein.

Die physische Basis und G_W-Norm aus #232 bleiben erhalten. Wir bewerten alle
58 alten Suchläufe je Parität neu; die damalige Rangliste enthält zwei
verschiedene gerade und einen ungeraden Kandidaten. Danach folgen 73 gerade
und 72 ungerade deterministische Starts mit dem neuen Suchmodell.

## 2. Numerischer K_P-Gram des ganzen Grad-11-Raums

Für die zwölf physischen Lifts u_j sei

\[
C_{ij}(r)=\int_{\mathbb R}u_i(x)u_j(x+r)\,dx,\qquad
D_{ij}(r)=\int_{\mathbb R}(u_i(x+r)-u_i(x))(u_j(x+r)-u_j(x))\,dx.
\]

Alle u_j besitzen dieselbe Parität. Daher ist C(r) symmetrisch und
\(D(r)=2(G_W-C(r))\). Die numerische Energie wird aus den Differenzen
gebildet, um die Subtraktion fast gleicher Autokorrelationen nahe r=0 zu
vermeiden. Alle Schnittstellen der drei physischen Stücke und ihrer Translation
werden in der inneren Integration getrennt. Die äußeren Trennstellen sind
0, b−a, 2a, a+b, 2b; nahe null verwenden wir 48 dyadische Zellen.

Mit dem geerbten Kernel k und der geerbten Konstante kappa ergibt sich

\[
A_{shell}=\int_0^{2b}k(r)D(r)\,dr+2\Theta(2b)G_W
-\kappa G_W-2\sum_{q=p^m\le9}\frac{\log p}{\sqrt q}C(\log q),
\]

\[
K_{model}=A_{shell}-\widehat F^*S_0\widehat F,\quad
S_0=X_{fix}+X_{fix}^*-X_{fix}^*A_{12,model}X_{fix}.
\]

X_fix und A_12 stammen aus dem bestehenden Antwortarchiv. Die endliche
Korrektur wird mit Arb bei 600 Bit aufgebaut, die gespeicherten Fhat-Doublewerte
bleiben aber ungerichtete Eingangsdaten. Die übrige Quadratur verwendet
`numpy.longdouble`; innere/äußere Auflösung 24/64 und 40/128.
Der positive, ausgelassene Bereich unter \((b-a)2^{-48}\) erhält für die
Suchschwelle eine numerisch ausgewertete W-Einheitsmajorante aus dem vorhandenen
Ableitungs-/Sprungbudget. Der gebundene K-Modellfehler wird zusätzlich bezahlt.
Die verbleibenden Quadratur- und Rundungsfehler werden hier **nicht** gerichtet
eingeschlossen. K_model ist keine zertifizierte Gesamtmatrix.

Kontrollen:

* C(0) reproduziert den physischen G_W-Gram.
* Beide bisher fest eingefrorenen Richtungen werden gegen ihre gerichteten
  tatsächlichen K_P-Intervalle aus #234 verglichen.
* Die Differenz der zwei numerischen K-Matrizen in W-Koordinaten hat Norm
  etwa 1.049e-12 je Parität.
* Beim alten geraden Kandidaten beträgt die Abweichung zum gerichteten
  K_P-Mittelpunkt etwa −1.6463e-11, ungerade bei hoher Auflösung −3.29e-14.

Die größere gerade Kalibrierungsabweichung wird ausdrücklich nicht durch die
kleinere Auflösungsdifferenz ersetzt. Weder Zahl ist eine uniforme gerichtete
Fehlerschranke. Die kleinsten numerischen K-Eigenwerte liegen ungefähr bei
4.94e-7 und 7.76e-7; die physische Normierung bleibt gut konditioniert.

## 3. Gemeinsamer k-Transport auf allen zwölf Schalenkoordinaten

Die Herleitung von #235 wird mit den vorhandenen 384-/512-Knoten-Maps auf
alle Schalenkoordinaten angewendet. Gespeichert waren CP=C*Phi*h8 und b_F.
Phi*h8 wird mit Arb bei 800 Bit aus C*Phi*h8 rekonstruiert; alle 2292
Rekonstruktionsresiduen enthalten null. Diese algebraische Kontrolle beseitigt
keine Unsicherheit der ursprünglich ungerichteten Quadraturdaten.

Mit den Bezeichnungen aus #235 werden numerische quadratische Matrizen für

\[
\|G_p^{1/2}(b_F-C_{F0}^*\ell)\|^2,\qquad
\nu^2=\gamma_M\|h_8\|^2-\|\ell\|^2,\qquad
\|C^*\ell\|^2
\]

gebildet. Vollständige hohe Quellen-/Kopplungsgrame und deren gebundene
Fehlerkonstanten geben

\[
R_{common}(c)=\sqrt{c^*A_kc}
+a_h\sqrt{c^*H_hc}+a_f\sqrt{c^*H_fc}.
\]

Hier enthält a_h sowohl den festen hohen Beitrag als auch den hohen gemeinsamen
k-Support einschließlich Quellen-/Kopplungsfehler; a_f enthält den festen
Featurefehler und seinen Anteil im gemeinsamen k-Ellipsoid. Alte getrennte
psi-k-/Antwort-k-Budgets werden nicht zusätzlich addiert. Numerisch ist
\(a_h\) ungefähr 49.283 gerade und 17.066 ungerade.

Die gerichteten Konstanten machen die ungerichteten Gram-Matrizen nicht zu
Zertifikaten. Kleine negative Eigenwerte auf Rundungsniveau werden nur im
Suchmodell gekappt und protokolliert; materielle Negativität stoppt den Lauf.
Der gesamte neue Raum besitzt noch keine gerichteten Integrationsreste.

Der unveränderte gerade Kandidat reproduziert den Radius von #235 bis etwa
6.25e-11. Die I_0-Kontrollen weichen um weniger als 3e-14 von den gebundenen
Einzelzertifikaten ab. Das sind Konsistenzdiagnosen, keine neue Zertifizierung.

## 4. Suchergebnis und Neubewertung

Optimiert wird auf der physischen W-Einheitssphäre mittels Cholesky-Whitening.
Starts: alte eingefrorene Richtung, alte unterschiedliche Kandidaten, duale
I_0-Richtung, K-inverse I_0-Richtung, zwölf K- und zwölf hohe-Gram-Eigenrichtungen,
zwölf Koordinatenrichtungen sowie 32 Zufallsstarts mit gebundenem Seed.
Alle 145 Optimiererläufe melden Konvergenz. Dies beweist keine globale
Optimalität des nichtlinearen Fehlerbudgets.

| numerische Richtung | I_0 | Radius | Schwelle | Marge |
|---|---:|---:|---:|---:|
| eingefroren gerade, neue Diagnose | 1.493637 | 0.255177 | 3.314249 | −2.075789 |
| beste neue Marge gerade | 0.241675 | 0.019904 | 0.290216 | −0.068445 |
| eingefroren ungerade, neue Diagnose | 152.528516 | 11.388441 | 182.550051 | −41.409976 |
| beste neue Marge ungerade | 0.092474 | 0.006378 | 0.131749 | −0.045654 |

**Kein alter oder neuer Kandidat erfüllt das Auswahlkriterium.** Kleinere
negative absolute Margen sind hier teilweise eine Folge kleinerer K_P-Energien;
sie sind keine positiven Ausschlussmargen. Alle alten 116 Läufe und die neuen
145 Läufe sind mit Koeffizienten, Ergebnissen und Kontrollabweichungen gespeichert.
Die größte skalare Auflösungsabweichung der neuen Kandidaten liegt bei
4.09e-9 gerade und 1.19e-9 ungerade. Der alte zweite gerade Kandidat ist nach
Neubewertung ebenfalls schlechter als der eingefrorene erste Kandidat.

## 5. Schranken für das numerische Suchmodell

Für die I_0-Zeile l und alpha=10q/11 ist im positiven numerischen K-Modell

\[
\sup_{c\ne0}\frac{|lc|}{\sqrt{\alpha c^*Kc}}
=\sqrt{lK^{-1}l^*/\alpha}.
\]

Das ergibt bei beiden Auflösungen stabil etwa **0.91895162 gerade** und
**0.86389038 ungerade**. Schon ohne Fehlerabzug kann dieses Mittelpunktmodell
keine positive Ausschlussmarge liefern. Das ist keine Aussage über alle exakten
Residualskalare mit einem noch unbestimmten hohen Mittelpunkt.

Eine zusätzliche Diagnose berücksichtigt auch den gesamten oben definierten
Support. In K-Koordinaten setzen wir
\(v=lK^{-1/2}/\sqrt\alpha\) und
\(B=a_h^2K^{-1/2}H_hK^{-1/2}/\alpha\).
Für jedes t>0 gilt

\[
(|v y|+\sqrt{y^*By})^2
\le y^*[(1+t)v^*v+(1+t^{-1})B]y.
\]

Die größte Eigenwertwurzel, plus den Operatornormpreisen der beiden übrigen
Supportterme und des Antwortmodellfehlers epsilon_D, majorisiert deshalb das
Verhältnis des numerischen absoluten Mittelpunktes **plus** vorhandenen
Supports zur Energieschwelle. t wird als positive rationale Zahl festgehalten;
seine numerische Wahl muss nicht exakt optimal sein. Der geerbte direkte
K-Modellfehler wird im Nenner subtrahiert.

| Diagnose | gerade | ungerade |
|---|---:|---:|
| volle Supportmajorante / Energieschwelle | 0.998543224 | 0.926109431 |
| Reserve zu 1 | 0.001456776 | 0.073890569 |
| zusätzlicher Empfindlichkeitstest K→K−10⁻¹⁰G_W | 0.998545586 | 0.926109433 |

Der letzte Test ist eine frei gewählte Störung, **keine bewiesene
Quadraturfehlerschranke**. Gerade beträgt die nominelle Reserve nur 0.15 Prozent.
Die ungerichteten Matrizen erlauben keine Statuspromotion zu einem Satz über
den ganzen Raum. Die Zahlen sprechen jedoch dagegen, teure Einzelskalare
innerhalb desselben Tests weiter zu verengen oder nur ihren hohen Mittelpunkt
neu auszuwerten.

## 6. Entscheidung und nächster Arbeitsumfang

Der abgeschlossene Kandidat bleibt archiviert. Kein weiterer Kandidat wird
zertifiziert. Weitere Starts mit demselben Mittelpunkt-/Supportmodell werden
zurückgestellt. N12 und die feste Antwortregel bleiben offen.

Die sinnvolle nächste Arbeitsstufe ist eine **explorative Feature- und
Datenbilanz des vollständigen W9-Residualenergievergleichs**. Der gebundene
Anschluss in `a9-a11-whole-response-gram-2026-10-15/PROOF.md`, §5b, lautet

\[
\langle f,W_9f\rangle
=\langle f_8,U_8f_8\rangle+v_{12}^*K^{-1}v_{12}
+\frac{11}{10}\left[\beta^{-1}\langle\nu,R_L\nu\rangle
+(J^*\nu)^*P_{upper}(J^*\nu)\right].
\]

Der bisherige Skalar kontrolliert nur eine Rang-eins-Untergrenze des letzten
Terms. Für die zwölf neuen Residuen sind die vollständigen U8-, v12- und
Nu-Featureabbildungen zu inventarisieren; gespeicherte b_F- oder C*Phi*h8-Maps
allein stellen sie nicht dar. Der Vergleich wäre
\(K_P-R^*W_9R\), zunächst diagnostisch auf demselben Grad-11-Raum.
Die vorliegende Rechnung hat diese Matrix nicht berechnet.

Vor einer gerichteten Energiebestätigung benötigt man außerdem einen
gewichteten Modellfehler, etwa
\(Q_D\succeq(D-\widehat D)^*W_9(D-\widehat D)\), oder eine gültige obere
W9-Normschranke. Der bezahlte Rang-eins-Skalarfehler ersetzt das nicht.
Eine Untergrenze für die W9-Norm darf hier weiterhin nicht als Obergrenze dienen.

## 7. Reproduktion und Status

Pflichtprüfungen: Eigen-/Eingabebindungen, beide K-Auflösungen, beide geerbten
Residualauflösungen, feste z-Kontrollen, Gram-/Whiteningprüfungen, alte/neue
Suchläufe, Modellmajoranten und Replay innerhalb dokumentierter numerischer
Toleranzen. Plattformabhängige BLAS-/Optimizerwerte werden nicht als
byteidentische Mathematik versprochen. Hashes binden die publizierten Dateien.

Kein neues gerichtetes Zertifikat, keine externe mathematische Prüfung,
keine Regelbestätigung, kein N12-Abschluss und keine Aussage über Objekt X oder RH.
