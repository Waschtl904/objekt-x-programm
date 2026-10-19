# Antwortmatrix-Vorprüfung: Daten, fairer Vergleich und begrenzte Entscheidung

18. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Gebundene Operator-, Domänen-, Quellen- und Modellvoraussetzungen werden
übernommen, nicht unabhängig erneut bewiesen. Quelle ist der unveränderte
#238-Tree des Commits `19d27b12c06500e2b1266e560a13f67974991f1d`.

## 1. Umfang und vorab begrenzte Abnahme

Fest bleiben W9, die zwölf Antwortfunktionen Phi12, die physische Schale,
die beiden eingefrorenen Richtungen aus #238 und die Quellenmodelle. Geprüft
werden X0, die exakte rationale Inverse des A12-Mittelpunkts, das vorhandene
Hüllenmittel S und die beiden Skalen 99/100 und 101/100 von X0.

Pflichtprüfungen: Hashbindungen; exakte rationale Matrixauswahl; gemeinsame
Änderung von Residuum und K_P; gerichtete Fehlerpreise; Kontrolle des
unveränderten X0 gegen #238; exakte algebraische Gegenkontrollen; bytegleicher
Replay dieses kleinen Programms; Registry und erzeugte Ansichten.
Es gibt keine Quadratur, keine adaptive Auswahl, keine R_L-Auswertung und
keinen erneuten großen #238-Replay. Ein unentschiedener Transfer wird nicht
zum Ausschluss oder zur Verbesserung umgedeutet.

## 2. Wiederverwendbare Daten und konkrete Lücken

Schreibe D=A9 Phi12, F=Phi12* C, und bezeichne das gebundene Modell der
neuen Kopplung mit Fhat. Die Antwortregel lautet P_X=Phi12 X Fhat,
T_X=X Fhat und R_X=C-D T_X. Alle Adjunkte benutzen die physischen Metriken.

| Bestand | Wiederverwendung | Grenze |
|---|---|---|
| Analytischer neuer Schalenquellterm C | In `residuals.py` sind Schalen-, Moment-, Gamma- und Primanteile getrennt vom D-T-Abzug konstruiert. | Kein gespeicherter vollständiger gewichteter C-Gram. Beim Refactoring müssen C und D ausdrücklich getrennt bleiben. |
| Zwölf D-Funktionen | `FUNCTIONS12.json`: Polynomial-, V-, Moment- und aktive Primverschiebungsanteile, volle Operatorfehler. | Nicht mit den alten zwölf Quellen F_o verwechseln. |
| Fhat und physischer G_W | Gerichtete 12×12-Matrizen in PAIRS beider Paritäten; unabhängig von X. | T und T_enclosure derselben Dateien gehören bereits zu X0. |
| PAIRS/ENERGY aus #238 | Ganze Grame und lineare Features von R0; vollständige hohe Projektion, 84 Basisfunktionen. | Kein gewichteter Gram von D und kein Kreuzgram D/R0. Aus R0-Gramen lassen sie sich nicht zurückgewinnen. |
| Festes W9 | C8, delta, rho, K, P_upper, alte Quellen- und Fehlergrame bleiben unverändert. | Die vier berechneten Features bilden nur W_partial. Der positive R_L-Anteil fehlt weiterhin. |
| Direkte Schalenform d | `K_P_even/odd.direct_form` ist für genau die eingefrorene Richtung wiederverwendbar. | Keine gerichtete ganze d-Matrix für beliebige neue Schalenrichtungen. |
| A12 und Fehler | Rationaler Mittelpunkt A0, Loewner-Radius delta_A; F/D-Fehler delta_F, delta_D. | X0-Preise müssen für jedes neue X mittransportiert werden. |
| Ganzer Antwortgram G0 | G0 >= (X0 Fhat)(X0 Fhat)* gilt auf der vollständigen Schale. | Für X folgt eine neue Kongruenz; die alte Zahl wird nicht unverändert übernommen. |

Für beliebige neue Matrizen fehlen mindestens

    B_D = D* W_partial D,
    H_D0 = D* W_partial R0,

einschließlich gewichteter Modell- und Integrationsfehler. Dann wäre für
DeltaT=(X-X0)Fhat rein algebraisch

    R_X* W_partial R_X
      = R0* W_partial R0 - H_D0* DeltaT - DeltaT* H_D0
        + DeltaT* B_D DeltaT.

Einmalige gemeinsame D-Features und diese Kreuzgrame würden viele spätere
Matrixvarianten ohne jeweils neue Funktionsintegration erlauben. Für eine
komponentenweise Fehleranalyse sind die entsprechenden vier Einzelblöcke
aufzubewahren. Die vorliegenden R0-Grame allein reichen dazu nicht.

## 3. Budget und Residuum gemeinsam ändern

Für einen W-normierten festen Schalenvektor z setze fhat=Fhat z und t=X fhat.
Das tatsächliche Budget ist

    K_X[z] = d[z] - 2 Re <F z,t> + <t,A12 t>.

Der vorhandene gerichtete d-Wert wird unverändert wiederverwendet. Mit A0
und fhat entsteht der Mittelpunkt-/Modellausdruck

    Khat_X[z] = d[z] - 2 Re <fhat,t> + <t,A0 t>.

Sein kompletter zusätzlicher Quellen-/A12-Preis ist

    e_K(X,z) = 2 delta_F ||t|| + delta_A ||t||².

Fhat, z-Normierung und t bleiben dabei gerichtete Intervalle; ihre
Arithmetik wird nicht ein zweites Mal als unabhängiger Modellpreis addiert.
Die d-Integrationsreste bleiben im übernommenen d-Intervall enthalten.
So gilt K_X[z] in Khat_X[z]+[-e_K,e_K]. Die alte K_P-Zahl wird für keine
neue Matrix festgehalten.

Für die ganze Schale sei M=X X0^-1. X0 ist als rationale Matrix invertierbar.
Dann gilt exakt T_X=M T0 und deshalb

    G_X=M G0 M* >= T_X T_X*.

Damit erhält jede Variante zugleich die uniformen Preise

    ||T_X|| <= sqrt(tr G_X),
    e_K(X) <= 2 delta_F sqrt(tr G_X)+delta_A tr G_X,
    e_D,partial(X) <= sqrt(w_partial) delta_D sqrt(tr G_X).

Das Programm gibt diese Preise neben den richtungsbezogenen Preisen aus.
Sie sind keine Kontrolle des fehlenden R_L-Anteils.

## 4. Günstiger gerichteter Transfer ohne neue Paarungen

Die schon zertifizierte tatsächliche Teilenergie von R0 z sei [E0-,E0+].
Aus R_X z-R0 z=-D (X-X0)fhat folgt

    e_Delta <= sqrt(w_partial) ||D|| ||(X-X0)fhat||,

    E_X in [(max(0,sqrt(E0-)-e_Delta))²,
             (sqrt(E0+)+e_Delta)²].

Die ganze alte Fehlerbilanz bleibt in [E0-,E0+] erhalten. Die zusätzliche
Differenz benutzt das tatsächliche D, nicht nur sein Modell. Somit werden
die alten Fehler nicht versehentlich entfernt oder zweimal separat gezählt.

Eine neue, billige D-Normschranke vermeidet die sehr grobe Summe sämtlicher
Monomkoeffizienten. Mit t=x/a haben die Modellspalten die Form

    Dhat_j = Pi_a [p_j(t)+v_j(t)V(t)+c_j m(at)
                    +sum I_shift(t) p_j,shift(t)] / sqrt(2a).

Die physische Paritätsnorm reduziert sich auf L2(0,1); Pi_a ist kontraktiv.
Für V(t)=-log(1-t²)/2 gilt
0<=V(t)<=-log(1-t)/2, also ||V||_2<=1/sqrt(2).
Die Koeffizienten v_j,n in v_j=sum v_j,n P_n werden durch
Polynom-Stammfunktionen eingeschlossen. Aus |P_n(t)|<=1 folgt

    ||Dhat_j|| <= sqrt(int_0^1 p_j²)
       + sum_n |v_j,n|/sqrt(2) + |c_j| exp(a/2)
       + sum_shift sqrt(int_active p_j,shift²).

Die verschobenen Polynome werden nur über ihre tatsächlichen aktiven
Intervalle integriert. log3/a=1 und log9/a=2 werden exakt erkannt.
Alle Integrale hier sind geschlossene Polynom-Stammfunktionen, keine neuen
numerischen Quadraturen. Dreiecksungleichung und Cauchy-Schwarz liefern
||D|| <= sqrt(sum_j n_j²)+delta_D. Die Ausgabe ergibt

    ||D_even|| < 25.755839,  ||D_odd|| < 27.820790.

Diese Schranken dienen ausschließlich dem Transfer. Aus ihren Oberwerten
werden keine unteren Aussagen über tatsächliche Fehler gewonnen.

## 5. Ergebnisse der fünf festgelegten Varianten

Alle Entscheidungen benutzen die veröffentlichten, nach außen gerundeten
rationalen Endpunkte. Die Matrixwerte werden aus den gebundenen Daten exakt
rational konstruiert und durch eigene SHA-256-Werte identifiziert.

| Variante | gerade: untere Teilenergie minus oberes neues K_P | ungerade |
|---|---:|---:|
| X0 (Kontrolle) | >6.3647e-6 | >1.15545e-7 |
| Exakte rationale A0-Inverse | >6.3647e-6 | >1.15545e-7 |
| S, Mittel der vorhandenen Invershüllen | >6.3646e-6 | >1.15545e-7 |
| (99/100)X0, (101/100)X0 | unentschieden | unentschieden |

Der Abstand von X0 zur exakten Mittelpunktinverse beträgt in Frobeniusnorm
weniger als 3.503e-60 bzw. 3.110e-60. Die Teilenergienorm-Änderung ist
kleiner als 2.285e-38 bzw. 2.252e-40. Mehr Stellen der gleichen Inverse
können den vorhandenen Ausschluss somit nicht beheben.

Für das Hüllenmittel S ist die gerichtete Energienormänderung kleiner als
7.594e-9 bzw. 8.393e-12. Auch nach dieser Änderung und neuer K_P-Rechnung
bleiben beide festen Richtungen Ausschlusszeugen. S ist keine exakte
Inverse und wird nicht als solche bezeichnet.

Bei ±1 % Skalierung wächst das neu berechnete K_P etwa auf 2.88288e-4
bzw. 1.99605e-4. Daraus folgt keine Verbesserung: Die allgemeine
Transfermajorante liefert nur Teilenergieoberwerte von ungefähr 4.51e50
bzw. 1.99e45 und eine untere Grenze null. Das ist ein Versagen dieser
Abschätzung, keine Aussage über die tatsächliche Energie. Auch Gleichheit
der K-Budgets für beide Vorzeichen macht ihre Residualenergien nicht gleich.

Es wurde weder der ganze Raum der Antwortmatrizen optimiert noch irgendeine
Variante als positiver vollständiger Vergleich zertifiziert.

## 6. Das richtige Optimierungsproblem und die fehlende Vollenergie

Für die vollständige zulässige Majorante W9>=A9^-1 gilt auf den gebundenen
Domänen exakt

    K_X - R_X*W9 R_X
      = d-C*A9^-1 C - R_X*(W9-A9^-1)R_X.

Die echte Schurform rechts ist unabhängig von X. Eine neue Antwort soll
den Überschuss der Majorante auf ihrem Residuum verkleinern. Minimierung
von ||R_X|| allein ist dafür nicht das passende Ziel.

Schreibe U=T_X-T0, H=D*W9 R0 und B=D*W9 D-A12. Dann ist die Änderung
des vollständigen Vergleichs

    2 Re U*(H+A12 T0-F) - U*B U.

Hier gilt B>=0, denn D=A9 Phi12 und W9>=A9^-1. Bei Verwendung von Fhat
muss der F-Modellfehler bezahlt werden. Sind nur Teilenergien vorhanden,
gilt B_partial=D*W_partial D-A12 im Allgemeinen nicht >=0.

Exaktes Gegenmodell: A=1, W9=2, W_partial=0, C=1, d=3/2, Antwort t=x.
Dann wächst K_x-E_partial=3/2-2x+x² unbeschränkt. Der volle Vergleich ist
aber 1/2-(1-x)² und ist bei x=3 negativ. Eine Optimierung der unvollständigen
Teilenergie könnte somit große Matrizen fälschlich attraktiv erscheinen
lassen. Der Prüfer kontrolliert dieses Beispiel und die Änderungsidentität
mit rationaler Arithmetik.

## 7. Entscheidung und Aufwand

| Weg | Nächster fehlender Nachweis | Aufwand / Entscheidung |
|---|---|---|
| Präzisere Mittelpunktinverse oder vorhandenes S | Keine neue Großrechnung sinnvoll; beide Varianten bleiben ausgeschlossen. | Abgeschlossen. |
| Strukturell andere Matrix bei gleichem W9 | D-Features und gemeinsame D/R0-Kreuzgrame, gewichtete Fehler; danach gegebenenfalls RL-Kontrolle. | Keine überzeugende Variante mit den vorhandenen Daten auswählbar. |
| Geänderte zulässige Inversmajorante | Nachweis A9^-1<=W9_neu und vollständige neue Fehler-/Energiebilanz. Ein Gewicht darf nicht bloß numerisch verkleinert werden. | Empfohlene nächste begrenzte Vorprüfung, noch keine Rechnung freigegeben. |

Für den zweiten Weg wären einmal zwölf zusätzliche Antwortkanäle pro Parität
einschließlich ihrer Kreuzblöcke nötig; anschließend sind Matrixwechsel kleine
Algebrarechnungen. Die Ausgangsfunktionen, alten Quellen und Zellzerlegung sind
wiederverwendbar. Eine neue Integration für jede einzelne Matrix wäre unnötig.

Der beobachtete #238-Lauf benötigte auf dieser Umgebung ungefähr 22–24 Minuten
Integrationszeit je Parität, zusätzlich Kontrollen und Abnahme. Das ist eine
Referenz, keine Laufzeitgarantie für die fehlenden Antwortblöcke. Deren Aufwand
ist ohne Implementierung und kurzen Pilot nicht zuverlässig zu beziffern.
Die vollständige R_L-Fehlerkontrolle ist davon getrennt und noch nicht
benchmarkfähig. Diese Vorprüfung arbeitet dagegen ausschließlich mit kleinen
Matrizen und Polynom-Stammfunktionen.

Ohne überzeugenden neuen Matrixkandidaten wird kein großer Paarungslauf
gestartet. Für einen späteren positiven Nachweis bleibt die vollständige
R_L-Kontrolle oder eine bewiesene obere Ersatzabschätzung erforderlich.
Ein negativer Teilenergietest braucht sie nicht.

## 8. Status und Aussagegrenze

Die hier bewiesenen Ausschlüsse betreffen nur drei konkret benannte
Antwortmatrizen mit derselben W9-Majorante und den zwei festgefrorenen
Richtungen. Skalierte oder beliebige weitere Matrizen bleiben unentschieden.
Keine negative Weil-Richtung, kein allgemeines N12-Scheitern, kein
A9→A11-Abschluss und keine Aussage gegen die Existenz von Objekt X.
Der allgemeine Matrixweg bleibt offen. Meilenstein 4 bleibt offen.
Externe mathematische Prüfung und spätere Integration bleiben getrennt.

Technische Abnahmekorrektur: Der erste isolierte Paketstart unter /tmp brach
vor der Rechnung ab, weil argparse den Repository-Standardpfad trotz eines
expliziten --repository-Arguments sofort auswertete. Der Standard wird jetzt
erst bei Bedarf aufgelöst. Die mathematischen Eingaben und Ergebnisdateien
blieben unverändert; der isolierte Paketstart ist Bestandteil der Abnahme.
