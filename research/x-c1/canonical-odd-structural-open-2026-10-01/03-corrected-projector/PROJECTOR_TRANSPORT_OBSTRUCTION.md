# Grenze der ungeraden Projektorlokalisierung durch gemeinsame Transportmomente

30. September 2026 · A9 nach A11 · lokaler Forschungsblock

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

Ausgangspunkt: `main@689ff6266b5e4d58700f82eae3016951a023e353`.
Der Forschungsversuch folgt Gate 1 des neuen Renewal-Fahrplans. Der
positive Extremalgap und die Eindeutigkeit sind Voraussetzungen.

## Ergebnis

**Auch die zuletzt verstärkte Momentfamilie erlaubt zwei fast orthogonale
obere Eigenrichtungen.** Zwei explizit definierte rationale
Vervollständigungen erfüllen die bisher ausdrücklich geprüften äußeren
Momentbedingungen, die volle gemeinsame b-Grammatrix und jetzt zusätzlich

\[
\mathsf H_1-\nu_B\mathsf H_0\succ0,\qquad
\mathsf H_0\succ0,\qquad \nu_B=0.070769.
\]

Ihre oberen physischen Eigenrichtungen liegen im selben A11-Gramraum
mindestens **89.987266 Grad** auseinander. Dies sind die Richtungen der
maximierenden inversen Antwortvektoren, entsprechend der kanonischen
Definition. Die zugehörigen Schur-Verschiebungen werden damit nicht
gleichgesetzt.

Die Beispiele haben einfache größte Eigenwerte und erfüllen die geerbten
Eigenwert- und Gapgrenzen. Somit reicht diese konkrete Relaxation nicht für
eine enge gemeinsame Richtungseinschließung. Um eine feste Referenzgerade
kann ein alle Beispiele enthaltender Winkelkegel keinen Halbwinkel unter
**44.993633 Grad** haben: Dies folgt aus der Dreiecksungleichung für den
Winkel zwischen Geraden.

**Die tatsächliche ungerade Maximierergerade bleibt quantitativ offen.**
Es wird keine Realisierung sämtlicher Trial-, Überlappungs- und
Operatordaten durch ein einziges physisches Operatorpaar behauptet.
Der Nachweis betrifft genau die unten geprüfte endliche Relaxation.

## Eine Korrektur bei unverändertem Projektor

Die beiden bisherigen Transportbeispiele, ihre vollständigen
Kammermomente und ihr rationaler Drehparameter werden unverändert aus dem
eingebetteten Archiv übernommen. Setze für eines dieser Beispiele

\[
B_B=G_B+L_B/17,\qquad
H=G_A-YB_B^{-1}G_BB_B^{-1}Y^*.
\]

Hier ist H die bisherige transportierte Restmasse. Der alte Prüfer und der
neue Replay bestätigen H positiv definit. Definiere exakt rational

\[
\boxed{C=I+\tfrac14 HG_A^{-1},\qquad \widetilde Y=CY.}\tag{1}
\]

C ist invertierbar, denn

\[
G_A^{-1/2}CG_A^{1/2}
=I+\tfrac14G_A^{-1/2}HG_A^{-1/2}\succ0.
\]

Deshalb gilt exakt

\[
\ker\widetilde Y=\ker Y.\tag{2}
\]

G_A,L_A,G_B,L_B sowie die inversen Kammermomente bleiben fest. (1) ist
eine Änderung des Kreuzblocks innerhalb der Relaxation, keine gemeinsame
Umbenennung der Koordinaten aller Matrizen.

In beiden Beispielen ist die maximale absolute Zeilensumme von C−I
kleiner als **0.0001627**. Auch diese Größenangabe folgt aus den gerichteten
Eintragseinschließungen; die Kerninvarianz ist unabhängig von ihrer Größe.

Insbesondere bleiben die normierte Kernbasis
N(Y)=[−Y_l^{-1}Y_r;I₂], alle auf ihr komprimierten Zweiermatrizen und deren
verallgemeinerte Eigenprojektoren exakt gleich. Dafür wird kein
Eigenvektorkomponentenverhältnis eingeschlossen.

## Gemeinsame Masse und Energie nach der Korrektur

Mit \(\widetilde X=B_B^{-1}\widetilde Y^*\) setze

\[
\widetilde H_0=G_A-\widetilde X^*G_B\widetilde X,
\qquad
\widetilde H_1=L_A-\widetilde X^*L_B\widetilde X.
\]

Direktes Ausmultiplizieren liefert die hilfreiche Identität

\[
\boxed{\widetilde H_0
=\tfrac12H+\tfrac7{16}HG_A^{-1}H
+\tfrac1{16}HG_A^{-1}HG_A^{-1}H.}\tag{3}
\]

Alle drei Summanden sind positiv. Die Korrektur verbessert jedoch nicht
für beliebige Daten automatisch die hohe Spektralordnung; diese wird für
beide konkreten Beispiele gesondert zertifiziert.

Der Prüfer wertet die exakt rational definierten Matrizen mit gerichteten
rationalen Intervallen aus und bestätigt sämtliche sechs LDL-Pivots
streng positiv. Folgende Zahlen sind nach unten gerundete Schranken für
den jeweils kleinsten Pivot, **keine Eigenwertuntergrenzen**:

| Beispiel | Restmasse | Restenergie | b-Schurkomplement | H₁−ν_B H₀ |
| --- | ---: | ---: | ---: | ---: |
| zentral korrigiert | 1.4731655e−28 | 7.3633787e−29 | 1.5164795e−28 | 6.3208342e−29 |
| gedreht korrigiert | 1.4731657e−28 | 7.3633885e−29 | 1.5164797e−28 | 6.3208438e−29 |

Zusätzlich liegt jeder Eintrag von \(\widetilde Y\) innerhalb der geerbten
zertifizierten Y-Hülle. Dieselben fest definierten Beispiele bestehen die
Prüfungen gegen beide Präzisionsquittungen.

Die positiven H₀,H₁ können abstrakt als Masse und Energie eines gemeinsamen
hohen Restes realisiert werden: Wähle E_H=H₀^{1/2} und
Q_H=H₀^{-1/2}H₁H₀^{-1/2}. Dann gilt E_H^*E_H=H₀,
E_H^*Q_HE_H=H₁ und Q_H≻ν_B I. Diese Zweimoment-Realisierung
stellt noch keine gemeinsame Realisierung aller ursprünglichen Trialdaten
und beider vollständigen Operatoren her.

## Was genau geprüft wird

Die beiden Kammermodelle stammen jeweils aus einem gemeinsamen positiven
Spektralmaß. Ihre Energie-, inversen Energie- und Gram-Matrizen, kritischen
Ränge, hohen Schnitte und geerbten Loewner-Schranken werden erneut geprüft.

Für das Extremalproblem werden die komprimierten Momenthüllen, YN=0, die
Energieordnungen, die N-abhängigen inversen Schranken sowie die einfachen
oberen Eigenwerte aus dem Vorgängerpaket übernommen und erneut ausgewertet.
YN=0 bleibt nach (1) exakt bestehen. Die geerbte Prüfung der alten Kernbasis
wird deshalb zusammen mit einer gesonderten Einschließung des korrigierten
Y verwendet. Es wird keine Hülle für unabhängige, frei gewählte N behauptet.

Der physische Projektor wird aus dem Bild von

\[
M^{-1}R-\beta_-I
\]

gebildet und mit der physischen Gram-Matrix normiert. Wegen (2) stimmt er
mit dem jeweiligen bisherigen Projektor exakt überein. Der Winkelvergleich
verwendet beide Vektoren in derselben vollständigen A11-Grammatrix G_B.
Der neue Prüfer berechnet den Vergleich erneut und bestätigt dieselbe
exakte rationale Winkeluntergrenze wie der Vorgänger.

## Konsequenz für Gate 1

Ein positiver Eigenwertgap kontrolliert die Einfachheit und kann zusammen
mit einer ausreichend kleinen Störung oder einem geeigneten Residuum eine
Richtungseinschließung begründen. Der Gap allein kontrolliert nicht die
Bewegung des Projektors über eine ganze zulässige Familie. Die hier
zertifizierte Familie enthält nahezu rechtwinklige Beispiele trotz Gap.

Deshalb beendet dieser Befund den zeitlich begrenzten Versuch einer engen
Lokalisierung **aus genau diesen Daten**. Eine erneute Auswertung derselben
Relaxation mit einer anderen Eigenvektorformel beseitigt das Hindernis nicht.
Das Ergebnis ist kein No-Go für den tatsächlichen Operator oder Objekt X.

Die nächste gezielte Datenfrage betrifft die **gemeinsame relative Lage
der tatsächlichen projizierten Trialvektoren**. Mit
R_A=(I−P_A)U_A, R_B=(I−P_B)U_B und O=U_A^*J^*U_B gilt exakt

\[
K=(P_AU_A)^*J^*(P_BU_B)
=O-R_A^*J^*U_B-U_A^*J^*R_B+R_A^*J^*R_B.\tag{4}
\]

Die bloßen Norm- und Momenthüllen verlieren die Vorzeichen und gemeinsame
Lage dieser Kreuzterme. Eine gemeinsame Projektor- oder Residuenrechnung
am tatsächlichen Operatorpaar könnte sie enger einschließen. Das ist eine
konkrete nächste Datenbeschaffung, noch kein bewiesener Erfolg dieser Methode.
Weil die B-Basis den kritischen Raum vollständig aufspannt, gilt außerdem

\[
Y=K G_B^{-1}B_B.\tag{5}
\]

Für (4) wird kein Transportgesetz für inverse Operatoren angenommen.

## Ausrichtung auf Renewal

Der Forschungsfahrplan bleibt: tatsächlicher ungerader Projektor, danach
bandweise Masse, Energie und inverse Energie beider tatsächlicher
Maximierer, dann ein Kandidat für eine erneuerbare Reserve und ein
vorwärts gerichteter Satz. Die Bänder sollen an zertifizierten
Spektralskalen liegen. Die Richtung der inversen Antwort und die
Schur-Verschiebung müssen dabei ausdrücklich unterschieden werden.

Eine kleine rohe Reserve allein entscheidet noch nicht, welche renormierte
Größe über einen weiteren Übergang erhalten bleibt. In diesem Block wird
keine solche Größe ausgewählt und kein Renewal-Satz bewiesen.

Für den späteren Satz sind alte Reserve, Wand-/Transportdaten,
High-Tail-Kontrolle und vorwärts konstruierte neue Richtungen zulässige
Eingaben. Neue Terminalpositivität, ein schon fertiger neuer kritischer
Projektor und die inverse Antwort des bereits positiv abgeschlossenen
neuen Terminals dürfen den Vorwärtsschluss nicht tragen.

Der Kandidat soll aus A8→A9 und A9→A11 formuliert werden. Vor einem Test
auf A11→A13 sind Aussage, Konstanten und Abnahmekriterien festzuhalten.
Dieser Block hat keine A13-Daten gelesen und PR #187 nicht verändert.
Frühere Kenntnis der Existenz des separaten Strangs ist kein vollständig
verblindetes Studiendesign; der geplante Test bleibt eine vorab festgelegte
Prüfung auf einem zusätzlichen Übergang.

## Reproduktion und Status

Das unveränderte Transportarchiv ist eingebettet. Sein Certifier sowie
die darin gebundenen Odd-, Schurdefekt- und Diskriminantenprüfer werden
bytegleich reproduziert. Ein unabhängiger rationaler Test prüft (2), (3)
an nichtkommutierenden Matrizen und enthält eine negative Kontrolle gegen
eine unzulässige allgemeine Supportbehauptung. Die bestehenden endlichen
Operatorkontrollen werden ebenfalls ausgeführt.

Die frische Quellenprüfung bestätigt die kanonischen Beweisbindungen und
25 ursprüngliche Repository-Quellen. Große Operator- und Integralrechnungen
wurden nicht wiederholt. Der abschließende Replay, Hashvergleich und die
Archivprüfung sind in `verification.log` bzw. `SHA256SUMS` dokumentiert.

Kein tatsächlicher ungerader Winkelbereich, keine bandweisen Momente
tatsächlicher Maximierer und kein Forward-Renewal-Satz werden beansprucht.
Das Paket bleibt lokal. Der kanonische Repository-Stand ist unverändert.
