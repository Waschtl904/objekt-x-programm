# Kanonische Spektralränge bei A₈, A₉ und A₁₁

28. September 2026 · lokaler Forschungsblock · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

## Ergebnis

**Bei derselben Schwelle q/b = 10⁻⁴ wachsen die kanonischen kritischen Räume von 5 auf 6 auf 8 Dimensionen je Parität.** Die gemeinsame Dimension ist **10 → 12 → 16**.

| Terminal | Gerade | Ungerade | Gesamt | Prüfstand |
| --- | ---: | ---: | ---: | --- |
| A₈ = log(8)/2 | **5** | **5** | **10** | Neu: gerichtete Rechnung und Ganzzahl-Rangzertifikat bestanden |
| A₉ = log(3) | **6** | **6** | **12** | Neu: gerichtete Rechnung und Ganzzahl-Rangzertifikat bestanden |
| A₁₁ = log(11)/2 | **8** | **8** | **16** | Vorhandenes Zertifikat übernommen; Paket, Hashbindungen und Rangangaben erneut geprüft |

Für jedes der drei Terminals ist dabei derselbe Raum gemeint:

\[
b_A=q_A+17\|\cdot\|_2^2,\qquad
K_A=\operatorname{ran}P_A,\qquad
P_A=\mathbf1_{(0,10^{-4})}(\mathcal A_A)
=\mathbf1_{(0,17/9999)}(Q_A).
\]

Die Gleichheit verwendet die kanonische Identifikation des b-Hilbertraums mit dem physischen L²-Raum. Der Schnitt \(\mu_*=17/9999\) liegt bei allen drei Terminals in einer spektralen Lücke. Auf dem vollständigen Komplement gilt \(q_A/b_A\ge10^{-4}\). Die angegebenen Ränge sind für diese Zielschwelle minimal.

Die Rangzahlen sind Eigenschaften des vollständigen physischen Operators. Sie bezeichnen weder die Dimension einer Modentrunkierung noch die Zahl ausgewählter numerischer Eigenvektoren.

## Was das für Renewal zeigt

Der durch diese feste Schwelle definierte kritische Raum hat über die drei Terminals **keinen konstanten Rang**. Ein Fortsetzungsansatz mit genau diesen Räumen muss einen Zuwachs von einer Richtung je Parität zwischen A₈ und A₉ und von zwei weiteren zwischen A₉ und A₁₁ berücksichtigen.

Damit ist noch keine Einbettung des alten Raums in den neuen bewiesen. Auch der Ort des Rangwechsels ist offen: Ein Eigenwert kann die feste Schwelle innerhalb einer Kammer unterschreiten. Aus den drei Terminalzählungen folgt daher **keine Geburt neuer Richtungen genau an einer Prime-Power-Wand**.

Die sinnvollen nächsten Größen bleiben

\[
\|(I-P_B)J_{A,B}P_A\|,\qquad P_BJ_{A,B}P_A.
\]

Erst ihre Kontrolle kann zeigen, ob der alte kritische Raum unter physischer Nullfortsetzung im neuen Raum erhalten bleibt und welche endliche Ergänzung nötig ist. Dieser Block bestimmt wie beauftragt zunächst ausschließlich die Ränge. Einzelne Eigenvektoren, numerische Projektortransporte und ein neuer κ-Test wurden nicht berechnet.

## 1. Grundlagen und vollständiger hoher Raum

Verwendet werden die bereits zertifizierten positiven Terminalformen und ihre vollständigen Low/High-Zerlegungen am gepinnten Commit

`d16ba43ebb20f2c61f43379fc65d7a9b9dba76de`.

Bei A₈ und A₉ gilt jeweils die hohe Schranke \(\delta=2/3\). Ihre endlichen Vergleichsmatrizen haben 191 beziehungsweise 296 Koordinaten pro Parität. A₁₁ verwendet \(\delta=1\) und 285 Koordinaten pro Parität. Diese Zertifikatsdimensionen werden nicht als kritische Spektralränge interpretiert.

Das bereits vorliegende allgemeine Tail-Prinzip liefert bei festem endlichem Terminal beliebig große Böden auf Unterräumen endlicher Kodimension. Zusammen mit der geschlossenen positiven Form folgt kompakte Resolvente für Q. Die folgende endliche Rangzählung lässt sich damit über das Minimax-Prinzip auf den tatsächlichen Spektralprojektor beziehen.

In Mellin-korrigierten Koordinaten gilt

\[
\widehat Q=M^*QM=\begin{pmatrix}L&B\\B^*&H\end{pmatrix},\qquad
G=M^*M,\qquad I\preceq G\preceq\rho I.
\]

M ist nicht unitär. Für den physischen Schnitt wird deshalb \(\widehat Q-\mu G\) betrachtet. Die Massenmatrix wird auch in den physischen Testräumen mitgeführt.

Die gebundenen Terminalzertifikate liefern

\[
H\succeq\delta I,\quad BB^*\preceq H^{up},\quad
F=L_0-e_LI-\delta^{-1}H^{up}>0,
\]

\[
H^{up}=\frac{1001}{1000}G_0+1001e_B^2I,
\qquad H^{up}\preceq\gamma F.
\]

Hier enthält G₀ die gesamte hohe Modellantwort. Die analytischen Fehlerbudgets bezahlen zusätzlich die wirkliche Gamma-Antwort und die Mellinkorrektur. Der unendliche hohe Raum wird nicht durch eine endliche Modenzahl ersetzt.

Die gerichtete Neuberechnung bei 512 und 768 Bit liefert für \(\operatorname{tr}(F^{-1}H^{up})\) folgende Anzeigen. Die anschließenden rationalen Obergrenzen sind die tatsächlich verwendeten Beweiswerte.

| Terminal / Parität | Kopplungsspur, ungefähr | Verwendetes γ | ‖M‖², ungefähr | Verwendetes ρ |
| --- | ---: | ---: | ---: | ---: |
| A₈ gerade | 36.53310323 | 37 | 1.00154278 | 1003/1000 |
| A₈ ungerade | 36.36162994 | 37 | 1.00013585 | 1003/1000 |
| A₉ gerade | 60.12942983 | 61 | 1.00191201 | 1003/1000 |
| A₉ ungerade | 60.49351207 | 61 | 1.00016887 | 1003/1000 |

Der Spurbound benutzt die bereits bewiesene Positivität von F und die positive Gramstruktur von Hᵘᵖ. Alle Eingabeintervalle und exakten rationalen Ergebnisse sind im Paket gebunden.

## 2. Die richtige Übertragung bei δ = 2/3

Setze \(t=\rho\mu\). Aus \(G\preceq\rho I\) folgt

\[
\widehat Q-\mu G\succeq\widehat Q-tI.
\]

Für \(t<\delta\) ist der vollständige hohe Block \(H-tI\) positiv. Seine Schur-Elimination ergibt die untere Vergleichsmatrix

\[
F-tI-\frac{t}{\delta(\delta-t)}H^{up}
\succeq a(t)F-tI,
\quad a(t)=1-\frac{\gamma t}{\delta(\delta-t)}.
\]

Die δ-Faktoren sind wesentlich: Die A₁₁-Formel mit δ = 1 wird nicht unverändert auf A₈/A₉ übertragen.

Für beide neuen Terminals wird der Vergleichsschnitt

\[
s=\frac1{400}
\]

verwendet. Bei \(\mu=\mu_*=17/9999\), \(\rho=1003/1000\) und den obigen γ gilt exakt

\[
0<t<\delta,\quad a(t)>0,\quad a(t)s-t>0.
\]

Die letzte Sicherheitsmarge beträgt mehr als **4.3890·10⁻⁴ bei A₈** und **2.0810·10⁻⁴ bei A₉**. Damit überträgt sich eine Obergrenze für die Zahl nichtpositiver Richtungen von F−sI auf die vollständige physische Form bei μ*.

## 3. Ganzzahlzertifikat der Vergleichsränge

V besteht aus den ersten fünf beziehungsweise sechs bereits vorhandenen rationalen Testvektoren des jeweiligen Terminals. Diese Vektoren werden nicht als wahre Eigenvektoren bezeichnet. Es werden keine neuen Vektoren erzeugt.

Der Prüfer rekonstruiert aus den ursprünglichen Intervallen und V exakt nach außen gerundet

\[
F-sI+VV^*,\qquad -V^*(F-sI)V.
\]

Er beweist

\[
F-sI+VV^*>0,\qquad -V^*(F-sI)V>0.
\]

Die erste Ungleichung begrenzt die Zahl nichtpositiver Richtungen auf höchstens Rang(V). Die zweite beweist ebenso viele strikt negative Richtungen und zugleich die Unabhängigkeit der Testvektoren. Folglich besitzt F−sI genau fünf beziehungsweise sechs negative Eigenwerte und keinen Nullraum.

| Fall | Positive Pivots der negativen Kompression | Zertifizierter Boden von F−sI+VV*, abgerundet |
| --- | ---: | ---: |
| A₈ gerade | 5/5 | 0.0016740 |
| A₈ ungerade | 5/5 | 0.0114353 |
| A₉ gerade | 6/6 | 0.0012725 |
| A₉ ungerade | 6/6 | 0.0083463 |

Rationale Dreiecksfaktoren R und T werden zunächst mit Gleitkommaarithmetik vorgeschlagen. Der Standardbibliothek-Prüfer berechnet anschließend mit Ganzzahlintervallen bei 200 Dezimalstellen

\[
\epsilon\ge\|F-sI+VV^*-R^*R\|,\qquad
\eta\ge\|I-RT\|,\qquad \nu=\|T\|_F^2.
\]

Die Positivität folgt aus dem exakt geprüften Kriterium

\[
\eta<1,\qquad \frac{(1-\eta)^2}{\nu}-\epsilon>0.
\]

Die Matrixrestfehler liegen in allen vier Fällen unter 1.60·10⁻¹⁴. Außerdem prüft der Replay, dass die gespeicherten F-Intervalle die Formel \(L_0-e_LI-\delta^{-1}H^{up}\) vollständig einschließen. Kein Eigenwertalgorithmus geht in diese Rangzählung ein.

## 4. Die Gegenrichtung: mindestens fünf beziehungsweise sechs

Auf den echten physischen Quellen MV werden die Form-Grammatrix S und die L²-Grammatrix Gᵥ neu berechnet. Die normierte Momentkorrektur ist in Gᵥ enthalten. Eine positive Gershgorin-Untergrenze für Gᵥ und eine obere für S liefern

\[
\max_{u\in\operatorname{ran}(MV)\setminus\{0\}}
\frac{q[u]}{\|u\|_2^2}
\le U_r<\frac{17}{9999}.
\]

| Fall | r | Uᵣ, nach oben gerundet | Daraus q/b, nach oben gerundet |
| --- | ---: | ---: | ---: |
| A₈ gerade | 5 | 1.422792·10⁻⁶ | 8.369359·10⁻⁸ |
| A₈ ungerade | 5 | 8.526831·10⁻⁵ | 5.015758·10⁻⁶ |
| A₉ gerade | 6 | 2.247398·10⁻⁶ | 1.321999·10⁻⁷ |
| A₉ ungerade | 6 | 1.472639·10⁻⁴ | 8.662505·10⁻⁶ |

Damit existieren mindestens r echte Eigenwerte unter dem physischen Schnitt. Die vollständige Schurabschätzung liefert höchstens r nichtpositive Richtungen bei diesem Schnitt. Zusammen folgen **genau r**, kein Eigenwert auf der Schwelle und der behauptete Gap auf dem vollständigen Spektralkomplement.

Da r Eigenwerte strikt unter der Schwelle liegen, kann kein Raum kleinerer Dimension einen Komplement-Gap von mindestens 10⁻⁴ erreichen. Das gilt auch für die gemeinsame gerade/ungerade Dimension.

## Prüfung, Bindungen und Grenzen

- A₈/A₉: acht neue gerichtete Rechnungen, vier Fälle jeweils bei 512 und 768 Bit; Kopplung, Masse und physische Test-Grammatrizen erneut berechnet. Die beiden Präzisionen liefern überlappende Einschließungen.
- Vier neue Ganzzahl-Rangprüfungen vollständig bestanden, einschließlich negativer Kompression, positiver Reparatur, F-Rekonstruktion und rationaler Übertragung auf den physischen Schnitt.
- A₁₁: vorhandenes Spektralpaket vollständig auf Datei- und Archivhashes geprüft. Seine gespeicherten Ränge 8+8 und sein Schnitt wurden kontrolliert; der frühere Arb-Spektrallauf wurde für diese Vergleichstabelle nicht wiederholt. Das unveränderte Paket liegt als `A11_reference.zip` bei.
- Keine Neuerzeugung der ursprünglichen Terminalintegrale; deren gepinnte Modelle, analytische Tail-/Fehlerbeweise und Positivitätszertifikate bleiben Eingaben. Die zwei neuen Präzisionsläufe sind keine unabhängigen Implementierungen desselben Modells.
- Die algebraische Rangprüfung benutzt nur die Python-Standardbibliothek. Die Spur-, Massen- und physischen Gramgrenzen stammen aus der separaten gerichteten Arb-Rechnung.
- Der Rangverlauf gilt für genau die gewählte Schwelle und die drei genannten Terminals. Er beweist keinen allgemeinen Rangwachstumssatz, keine Projektortransportkontrolle und keinen Renewal-Satz.

**Repository und Registry wurden nicht verändert.** Es wurde nichts gepusht oder veröffentlicht. Der globale Verifikationsstand und externe Reviewstatus werden durch dieses lokale Ergebnis nicht angehoben.

Die exakten Daten stehen in `verification.json`; die Reproduktion ist in `REPRODUKTION.md` beschrieben. `comparison.json` bindet die neue Rangtabelle an die vier neuen Prüfungen und das bestehende A₁₁-Paket.
