# Begrenzte Vorprüfung einer schärferen Inversmajorante

18. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Ausgangspunkt: veröffentlichter Commit
`5e5462d478cf700797de80dd0a77f7e7d0f20ad7`, mit den unveränderten
#238-Zertifikaten aus `19d27b12c06500e2b1266e560a13f67974991f1d`.
Alle Aussagen bleiben bedingt auf die dort gebundenen Operator-,
Domänen-, Quellenmodell- und Integrationsvoraussetzungen.

## Ergebnis und Umfang

Eine echte Verkleinerung der bisherigen Inversmajorante ist möglich:
Der vollständige Dualanteil behält seinen Faktor 11/10; der Faktor des
endlichen P-Anteils sinkt auf ungefähr 1.045472 gerade bzw. 1.082998 ungerade.
Für diese Variante gilt auf dem ganzen physischen A9-Raum

\[
A_9^{-1}\preceq W_{\rm neu}\preceq W_9.
\]

Der gerichtete Teilenergievergleich scheitert trotzdem in beiden festgefrorenen
Richtungen. Noch stärker: Bei unveränderten übrigen Bausteinen scheitert
gerade die gesamte unten definierte Familie skalarer Young-Gewichtungen.
Auch eine weitere Verbesserung allein des Gesamtresidualpreises kann diese
Familie nicht retten. Das ist **keine** Aussage über alle zulässigen Majoranten,
andere Antwortmatrizen oder eine negative tatsächliche Weil-Richtung.

Eine zusätzliche zulässige Umverteilung besteht ungerade den Teiltest, erhöht
aber den offenen vollständigen Dualanteil und scheitert weiterhin gerade.
Sie ist deshalb kein Anlass für eine vollständige neue Rechnung.
Meilenstein 4, N12 insgesamt und Objekt X bleiben offen.

## 1. Festgehaltene Daten

Unverändert bleiben X0, beide rational festgefrorenen #238-Richtungen, ihre
physische W-Normierung, die gemeinsamen Residuen, sämtliche Paarungen,
K, P_upper, U8, beta, a_fin und die tatsächlichen K_P-Intervalle.
Insbesondere wird die vorangegangene Matrixsuche nicht fortgesetzt.
Die 0.99-X0- und 1.01-X0-Varianten bleiben unentschieden.

`INPUT_BINDINGS.json` bindet die verwendeten Dateien. Der Prüfer liest jede
gebundene Datei einmal und benutzt ausschließlich diese geprüften Bytes.
Die übernommenen 36 Dateien und 20 Archivmitglieder des #238-Eingangsbestands
werden ebenfalls hashgeprüft. Die Kandidaten-, Paarungs- und Budgetbindungen
werden explizit gegengeprüft. Der Digest der unveränderten Antwortmatrix
steht zusätzlich im Ergebnis.

Neu ist nur eine gerichtete skalare Umgewichtung bereits zertifizierter
Energiekomponenten und ihrer Fehler. Keine neuen Quadraturen, keine erneuten
gemeinsamen Integrationen, kein R_L-Lauf, keine adaptive Richtungssuche.

## 2. Die vermeidbare Überschätzung

Die [Inversherleitung, Abschnitt 2](../a9-inverse-renewal-2026-10-13/original/HERLEITUNG.txt)
setzt E=D-M_upper, Z=J X_ans und R=A_force* - S Z. Aus den vollständigen
Restschranken folgt

\[
\Delta\succeq(1-c)E,\qquad
R^*S^{-1}R\preceq cE.
\]

Für ein Formdual-Funktional nu und
x²=<nu,S^-1 nu>, z²=(Z*nu)*E^-1(Z*nu) liefert Woodbury

\[
\langle\nu,H_*^{-1}\nu\rangle
\le\frac{x^2+z^2+2\sqrt c\,xz}{1-c}.
\tag{1}
\]

Die bisherige Abschätzung benutzt 2xz<=x²+z² und rundet den gemeinsamen
Faktor 1/(1-sqrt(c)) nach oben auf 11/10. Dieser Faktor war zulässig;
er wird hier nicht als früherer Fehler bezeichnet. Die unnötige Reserve
liegt in der gleichen Gewichtung und anschließenden Aufrundung.

Wir benutzen zusätzlich die bereits gebundenen besseren **vollständigen**
Restpreise des [globalen Abschlusses](../a8-a9-global-closure-2026-10-13/PROOF.md):

\[
c_e=1977/500000,\qquad c_o=6967/1000000.
\]

Das sind die Gesamtpreise aller 203 Kräfte relativ zu beta E, keine isolierten
Quadraturpreise. Der zugehörige Abnahmebericht und seine Provenienz sind
gebunden. Der kleine neue Prüfer kontrolliert die rationalen Gesamtgrenzen
gegen diese Caps und die ältere Inversherleitung. Er wiederholt deren
große Integrationsbeweise nicht. Es bleibt
beta=20209999981781/182190000000000.

## 3. Zulässige Familie und echte Verkleinerung

Seien a,b positive skalare Gewichte. Die Ungleichung

\[
\frac{x^2+z^2+2\sqrt c\,xz}{1-c}\le ax^2+bz^2
\tag{2}
\]

folgt aus der positiven Semidefinitheit der 2x2-Matrix mit Diagonalen
a(1-c)-1, b(1-c)-1 und Nebendiagonale -sqrt(c). Somit genügen genau

\[
a(1-c)\ge1,\quad b(1-c)\ge1,\quad
[a(1-c)-1][b(1-c)-1]\ge c.
\tag{3}
\]

Für c>0 sind die ersten beiden Ungleichungen bei Zulässigkeit strikt.
Mit x²<=beta^-1<nu,R_L nu> und
z²<=(J*nu)*P_upper(J*nu) folgt aus der unveränderten vollständigen
Quadratergänzung der Inversherleitung

\[
\begin{split}
\langle f,W_{a,b}f\rangle={}&
\langle h,U_8h\rangle+v^*K^{-1}v\\
&+\frac a\beta\langle\nu,R_L\nu\rangle
+b(J^*\nu)^*P_{\rm upper}(J^*\nu),\\
A_9^{-1}\preceq{}&W_{a,b}.
\end{split}
\tag{4}
\]

h,v,nu sind exakt die gemeinsamen tatsächlichen linearen Funktionen aus
Abschnitt 6 der alten Herleitung. Die Domänen, die volle R_L-Inverse und
sämtliche Kreuzterme bleiben erhalten. Dies ist eine Operatoraussage,
keine Extrapolation aus den zwei geprüften Richtungen.

Bei festem a=11/10 minimiert auf dem Rand von (3)

\[
b=\frac{a-1}{a(1-c)-1}=\frac1{1-11c}.
\tag{5}
\]

Beide Faktoren sind <=11/10. Also ist (4) tatsächlich <=W9; die Differenz
ist der positive Operator mit Energie (11/10-b)(J*nu)*P_upper(J*nu).
Dies ist die kleinste P-Gewichtung dieser Familie bei unverändertem
Dualgewicht. Eine mögliche Abhängigkeit der beiden tatsächlichen Features
wird damit nicht optimiert.

## 4. Angepasster gerichteter Fehlertransport

Schreibe die vier alten Modellkomponenten als E_i und ihre gemeinsam
hergeleiteten Featurefehler als e_i. Nur die P-Komponente ändert sich,
mit s²=b/(11/10). Deshalb gelten für die neue Modellenergie und deren Fehler

\[
E_{\rm mod}(b)=\sum_{i\ne P}E_i+s^2E_P,\qquad
e_{\rm feat}(b)^2=\sum_{i\ne P}e_i^2+s^2e_P^2.
\]

Der gemeinsame a_fin-Fehler steckt bereits einmal in e_P und wird weder
weggelassen noch nochmals addiert. Alle Auslöschungen bleiben in den
übernommenen gemeinsamen Modellkomponenten erhalten. Für den Fehler des
gesamten Residualmodells genügt

\[
e_{\rm res}(b)\le\max(1,s)e_{\rm res}(11/10),
\]

denn die neue **Teil**gewichtung ist höchstens max(1,s²) mal die alte.
Damit werden die tatsächlichen Teilenergien eingeschlossen durch

\[
\left[
\max(0,\sqrt{E_{\rm mod,lo}}-e_{\rm feat}-e_{\rm res})^2,
(\sqrt{E_{\rm mod,hi}}+e_{\rm feat}+e_{\rm res})^2
\right].
\]

Die Intervallrechnung benutzt 800 Bit und äußere rationale Rundung.
Die Entscheidung erfolgt an den veröffentlichten rationalen Endpunkten.
Die winzige zusätzliche Aufweitung beim erneuten Einlesen alter Intervalle
ist enthalten. K_P bleibt unverändert; eine Änderung der Majorante ändert
bei festem X0 weder Residuum noch K_P.

| Variante | Gerade Teilenergie | Ungerade Teilenergie | Entscheidung |
|---|---:|---:|---|
| bisher, a=b=1.1 | [6.048190,6.071310]e-5 | [5.396321,5.397977]e-6 | beide ausgeschlossen |
| (5), gleiches Dualgewicht | [5.825076,5.847726]e-5 | [5.360129,5.361784]e-6 | beide ausgeschlossen |
| b=1.02, angepasstes a | [5.720853,5.743284]e-5 | [5.226026,5.227680]e-6 | gerade ausgeschlossen; ungerade Teiltest bestanden |
| nur Hilfsuntervergleich b=1 | [5.639018,5.661277]e-5 | [5.183452,5.185106]e-6 | gerade ausgeschlossen |

Die Tabelle rundet nach außen. Die unveränderten Budgets liegen in
[5.4117169360,5.4117169380]e-5 bzw. [5.2807764351,5.2807764506]e-6.
Für (5) bleiben gerichtete Abstände >4.13359e-6 bzw. >7.93525e-8.

## 5. Grenze der ganzen Gewichtungsfamilie

Jede Gewichtung aus (3) hat b>=1/(1-c)>=1. Also dominiert ihre Teilenergie
den Hilfsuntervergleich mit b=1 und ohne R_L. Dieser Hilfsoperator wird
**nicht** als zulässige Inversmajorante ausgegeben. Seine Energie liegt
gerade schon um >2.27301e-6 über der tatsächlichen Budgetobergrenze.

Folglich scheitert der feste Vergleich gerade für alle Gewichte aus (3),
bei unveränderten U8,K,P_upper und tatsächlichen Quellenabbildungen. Das
gilt sogar für jeden hypothetisch verbesserten Gesamtpreis 0<=c'<1, soweit
die gleiche Familie benutzt wird. Es ist keine Behauptung, eine tatsächlich
bessere Matrix- oder Operatorabschätzung müsse ebenfalls scheitern.

Die zusätzliche Variante b=51/50 benutzt
a=(b-1)/(b(1-c)-1), ungefähr 1.252590 gerade und 1.551150 ungerade.
Sie ist zulässig, aber wegen des höheren Dualgewichts **nicht nachgewiesen
kleiner als W9**. Ungerade lässt sie eine gerichtete Restreserve >5.30967e-8.
Ein hinreichender Anschluss für genau diese Richtung wäre eine vollständige,
fehlerbezahlte obere Schranke

\[
\langle\nu,R_L\nu\rangle\le3.7971\cdot10^{-9}.
\]

Dies ist nur eine erforderliche weitere Lieferaufgabe für den hier gewählten
hinreichenden Test, kein vorhandenes Zertifikat und keine notwendige Schranke
für alle denkbaren Tests. Ein endlicher Galerkinwert liefert dafür zunächst
nur eine Untergrenze. Zudem bliebe der gerade Fall dieses Vergleichs gescheitert.
Ein bestandener Teiltest bestätigt weder eine ganze Antwortregel noch N12.

## 6. Entscheidung, Datenlücken und Aufwand

**Entscheidung:** Die echte Verkleinerung (5) ist analytisch zulässig, behebt
das Hindernis aber nicht. Weitere Optimierung allein der Young-Gewichte
oder des skalaren Gesamtpreises wird für diesen festen Vergleich zurückgestellt.
Der ungerade Trade rechtfertigt keinen großen vollständigen Lauf, weil die
gleiche Familie gerade bereits unabhängig vom fehlenden positiven Dualterm
ausgeschlossen ist. Eine zusätzliche R_L-Rechnung zum Nachweis dieses
Ausschlusses ist nicht nötig.

Der nächste sachliche Entscheidungspunkt ist, welche **strukturelle**
Untervergleichsreserve sich mit vorhandenen Daten verbessern lässt:
die alte U8-Ersetzung, der endliche K-Untervergleich oder die gerichtete
Schur-/Woodbury-Matrixkontrolle. In der bisherigen Kette bleiben insbesondere
S^-1<=beta^-1 R_L und Delta^-1<=[(1-c)E]^-1 grob. Ein möglicher neuer Ansatz
muss echte gemeinsame Kreuzinformation erhalten und erneut eine vollständige
Operatorordnung beweisen. Bloßes Streichen positiver Beiträge genügt nicht.

| Weiterer Ansatz | Fehlende gerichtete Daten / Begründung | Rechenumfang |
|---|---|---|
| nur ungeraden Trade vollständig prüfen | volles <nu,R_L nu> mit Normierung, Projektionsbedingungen und vollständigem Rest; obige Zielreserve | neue Dualrechnung; keine belastbare Laufzeit aus dem jetzigen Bestand ableitbar; wegen geradem No-Go nicht empfohlen |
| gemeinsame Woodbury-Auswertung | <nu,S^-1 nu>, R* S^-1 nu und eine passende Matrixeinschließung von Delta^-1 | je festem Kandidaten ein vollständiger Formsolve mit 203 gemeinsamen Residualpaarungen; voller Zwölferblock benötigt 203x12 je Parität sowie Restkontrolle; nicht nur vorhandene skalare Preise |
| U8- oder K-Untervergleich verbessern | neue zulässige gemeinsame Formuntergrenze und daraus konsistent neu hergeleitete Kräfte, Budgets und gewichtete Fehler | zuerst begrenztes Daten-/Herleitungsinventar; Aufwand einer anschließenden Integration erst danach seriös schätzbar |

Die zweite Zeile beschreibt benötigte Größen, keinen bereits verfügbaren
Solver oder freigegebenen Lauf. Der allgemeine Matrixweg bleibt ebenfalls
offen. Dieser Auftrag startet keinen dieser größeren Schritte.

## 7. Abnahme

`preflight.py --check` reproduziert `EXPECTED.json` aus gebundenen Bytes.
Exakte rationale Gegenkontrollen verwerfen eine Unterschreitung des zulässigen
P-Gewichts und das unbezahlte Weglassen des Kreuzterms. Der eigene Manifest
und alle übernommenen Inputs werden geprüft; `python -O` wird abgewiesen.
Der vorab festgelegte Abnahmeumfang steht in `ACCEPTANCE_PLAN.md`, die
tatsächlich ausgeführten Prüfungen in `ACCEPTANCE.json`.

Replay und Registry-Prüfung sind keine unabhängige mathematische Begutachtung.
Historische Zertifikate bleiben unverändert; keine Statuspromotion und kein Merge.
