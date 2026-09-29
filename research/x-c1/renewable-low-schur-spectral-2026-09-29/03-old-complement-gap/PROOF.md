# Alter Komplement-Gap: Rang 1 bis 20

28. September 2026 · A₈, A₉ und A₁₁ · ausschließlich Daten des jeweiligen alten Terminals

## Ergebnis

Die gewünschte Größe

\[
\tau_A^{(r)}=
\inf_{0\ne u\perp_{q_A}K_A^{(r)}}
\frac{q_A[u]}{q_A[u]+17\|u\|_2^2}
\]

wurde für **A₈, A₉ und A₁₁, beide Paritäten und jeden Rang r = 1,…,20** nach unten und oben eingeschlossen. Das sind 120 Fälle. Der Rang gilt jeweils **pro Parität**; gemeinsam werden damit 2r Richtungen mitgeführt.

**Die bisherige Familie kritischer Diagnoseräume erzeugt auch bis Rang 20 keinen großen Komplement-Gap.** Es wurden explizite, exakt q-orthogonale Quellen mit weiterhin sehr kleiner Energie konstruiert. Diese liefern Obergrenzen für den tatsächlichen Gap des vollständigen Komplements. Der Befund beruht daher nicht bloß darauf, dass eine stärkere Untergrenze noch fehlt.

Besonders deutlich ist der gerade Sektor bei A₁₁:

\[
0<\tau_{A_{11},\mathrm{gerade}}^{(20)}
\le 1.967\cdot10^{-38}.
\]

Wegen der ineinander enthaltenen Quellenräume gilt diese Obergrenze auch für jeden kleineren untersuchten Rang. Zugleich existiert im q-orthogonalen Komplement bei Rang 20 ein Zeuge w mit

\[
\frac{\operatorname{dist}_{L^2}(w,K_{A_{11}}^{(20)})}{\|w\|_2}
\le 5\cdot10^{-19}.
\]

**Eine Quelle kann hier also räumlich fast im entfernten Raum liegen und trotzdem exakt q-orthogonal zu ihm sein.** Das ist die entscheidende Schwierigkeit dieser Raumwahl.

Der neue Block verwendet für jeden Fall ausschließlich dessen eigenes Terminalpaket. Die Positivität eines späteren Terminals, eine spätere Resolvente oder eine weitere Kammer werden nicht eingesetzt. Repository und Main wurden nicht verändert.

## 1. Welche Quellenräume untersucht wurden

Die ersten drei Richtungen jeder Parität sind exakt dieselben rationalen Dezimalkoeffizienten wie im vorherigen Kopplungspaket. Sie wurden unverändert übernommen.

Diese Räume wurden zu einer verschachtelten Familie erweitert. Weitere Richtungen werden am rationalen Mittelpunkt der alten Schur-Untergrenze F durch 32 Schritte einer blockweisen inversen Iteration erzeugt, unter Orthogonalisierung gegen die drei festgehaltenen Richtungen. Ihre ausgegebenen 90-stelligen Dezimalkoeffizienten werden anschließend als exakte rationale Zahlen fixiert. Es werden 21 Richtungen gespeichert: 20 für die Raumfamilie und eine zusätzliche Testrichtung.

Die mathematischen Schranken setzen keine Konvergenz dieser Iteration zu exakten Eigenvektoren voraus. Entscheidend sind die fixierten Quellenkoeffizienten und deren gerichtete Auswertung. Die vollständige Mellinkorrektur wird anhand der alten eingeschlossenen Momente vorgenommen.

Die so definierten Räume sind positiv und linear unabhängig. Das wurde für alle sechs 21-dimensionalen Form-Grammatrizen durch 126 positive Intervallpivots bestätigt; die L²-Grammatrizen sind ebenfalls positiv.

**Diese Räume sind weiterhin keine zertifizierten Spektralräume der tatsächlichen Form.** Untersucht wurde die natürliche Fortsetzung der bisherigen F-Diagnoseräume. Die Rechnung optimiert nicht über alle möglichen r-dimensionalen Räume und schließt eine bessere Quellenwahl nicht aus.

## 2. Wie ein exakter Komplement-Zeuge entsteht

Am festen alten Terminal schreibe Vᵣ für die ersten r physischen Quellen und v für die nächste Quelle. Definiere mit der tatsächlichen Form

\[
S_{ij}=q_A(v_i,v_j),\qquad h_i=q_A(v_i,v),
\qquad\alpha=S^{-1}h.
\]

Die Quelle

\[
\boxed{w=v-V_r\alpha}
\]

liegt exakt im q-orthogonalen Komplement, denn

\[
q_A(V_r,w)=h-S\alpha=0.
\]

Ihre Energie ist der endliche Schurrest

\[
E=q_A[v]-h^*S^{-1}h>0.
\]

Ist G die physische L²-Grammatrix von \((v_1,\ldots,v_r,v)\), dann gilt mit \(z=(-\alpha,1)\)

\[
N=\|w\|_2^2=z^*Gz>0,
\qquad
\tau_A^{(r)}\le\frac{E}{E+17N}.
\]

Die tatsächlichen Einträge von S, h und G sind durch die alten Modellintervalle einschließlich des bewiesenen Formfehlers eingeschlossen. Insbesondere wird nicht bloß am Mittelpunkt eine Orthogonalität angenommen. Die Formel definiert den Zeugen anhand der tatsächlichen Form; seine möglichen Koeffizienten und sein Quotient werden gerichtet eingeschlossen.

Mit E ≤ E₊ und N ≥ N₋ > 0 folgt die verwendete Obergrenze

\[
U_r=\frac{E_+}{E_++17N_-}.
\]

### Weshalb dies eine Aussage über das vollständige Komplement ist

Die Zeugen sind zulässige Quellen im vollständigen Formraum und erfüllen dessen exakte Orthogonalitätsbedingung. Ein einzelner solcher Zeuge genügt für eine Obergrenze des Infimums. Dass die Zeugen aus endlich vielen alten niedrigen Quellen gebildet werden, schränkt diese Aussage nicht auf eine Modentrunkierung ein.

Für die Untergrenze wird der bereits zertifizierte physische Boden **desselben Terminals** verwendet:

\[
q_A\ge c_A I
\quad\Longrightarrow\quad
\tau_A^{(r)}\ge\frac{c_A}{c_A+17}>0.
\]

Diese Untergrenze ist vom Rang unabhängig und bleibt konservativ. Eine neue, wesentlich stärkere Untergrenze für das Komplement wurde nicht hergeleitet. Die exakten Infima wurden nicht bestimmt; das neue Ergebnis sind die expliziten Obergrenzen, die einen großen Gap für diese Raumfamilie ausschließen.

## 3. Zahlen

Alle Angaben in der Tabelle sind zusätzlich nach außen gerundet. Die Untergrenze gilt für jeden untersuchten Rang der jeweiligen Zeile. Die Obergrenzen gelten für die angegebenen Ränge. Maßgeblich sind die exakten rationalen Werte in `verification.json`.

| Terminal | Parität | Untergrenze für τ | Obergrenze r = 1 | Obergrenze r = 3 | Obergrenze r = 20 |
| --- | --- | ---: | ---: | ---: | ---: |
| A₈ | gerade | 7.250·10⁻³¹ | 1.286·10⁻²⁶ | 5.403·10⁻²⁶ | 7.599·10⁻²⁵ |
| A₈ | ungerade | 5.065·10⁻²⁸ | 3.063·10⁻²³ | 1.171·10⁻²² | 6.372·10⁻²¹ |
| A₉ | gerade | 4.100·10⁻³⁶ | 8.741·10⁻³² | 3.175·10⁻³¹ | 7.117·10⁻²⁹ |
| A₉ | ungerade | 3.808·10⁻³³ | 2.847·10⁻²⁸ | 7.446·10⁻²⁸ | 3.571·10⁻²⁶ |
| A₁₁ | gerade | 3.803·10⁻⁵¹ | 4.045·10⁻⁴¹ | 2.342·10⁻⁴⁰ | 1.967·10⁻³⁸ |
| A₁₁ | ungerade | 1.565·10⁻⁴⁷ | 2.557·10⁻³⁸ | 9.663·10⁻³⁸ | 1.801·10⁻³⁴ |

Die tatsächlichen Größen τᵣ sind monoton nicht fallend: Aus Kᵣ ⊂ Kᵣ₊₁ folgt Rᵣ₊₁ ⊂ Rᵣ. Einzelne Obergrenzen aus wechselnden Testquellen müssen diese Monotonie nicht besitzen. Deshalb wurde die gültige monotone Hülle

\[
\widehat U_r=\min_{r\le j\le20}U_j
\]

verwendet. Ein Zeuge in Rⱼ liegt auch in jedem Rᵣ mit r ≤ j. In den Daten ist der jeweils verwendete Zeugenrang ausdrücklich gespeichert.

Für die veröffentlichten Uⱼ wird konservativ das Maximum der Obergrenzen aus beiden Arb-Läufen und dem unabhängigen Ganzzahl-Replay verwendet. Die Tabelle beruht somit auch auf den etwas breiteren Schranken des unabhängigen Replays.

### Räumliche Nähe trotz q-Orthogonalität

Aus w = v − Vᵣα folgt unmittelbar

\[
\frac{\operatorname{dist}_{L^2}(w,K_r)^2}{\|w\|_2^2}
\le\frac{\|v\|_2^2}{N_-}.
\]

Der Ganzzahlprüfer schließt auch diese Größe ein. Für den eigenen Rang-20-Zeugen bei A₁₁ gerade ergibt sich die oben genannte Distanzschranke 5·10⁻¹⁹. Hier wird eine Normdistanz direkt eingeschlossen; ein auf 1 gerundeter Winkelkosinus wird nicht als Beleg benutzt.

## 4. Warum eine kleine Fehlrichtung den Gap erhalten kann

Ein exakt lösbares Beispiel zeigt das Problem der q-Orthogonalität. Sei

\[
q(x,y)=\varepsilon x^2+y^2,\quad
b=q+17(x^2+y^2),\quad
K=\operatorname{span}\{(1,t)\}.
\]

Der Vektor n = (t,−ε) ist exakt q-orthogonal zu K. Im eindimensionalen Komplement beträgt der physische Quotient

\[
\mu=\frac{\varepsilon t^2+\varepsilon^2}{t^2+\varepsilon^2},
\qquad\tau=\frac{\mu}{\mu+17}.
\]

Für t = 0 ist K der exakte schwache Eigenraum, und τ = 1/18. Für t² = ε gilt dagegen

\[
\mu=\frac{2\varepsilon}{1+\varepsilon},
\]

also weiterhin ein winziger Komplement-Gap — obwohl K für kleines ε räumlich extrem nahe am richtigen Eigenraum liegt. Beispielsweise wurde ε = 10⁻³⁰, t = 10⁻¹⁵ exakt mit rationaler Arithmetik geprüft.

Die Konsequenz ist präziser als „mehr Richtungen helfen nicht“: **Die Richtungstreue muss zur winzigen Formenergie passen.** Eine gute L²-Überlappung oder die Auswahl aus einer hinreichenden Schur-Untergrenze genügt dafür nicht automatisch. Das Beispiel ist eine Erklärung des möglichen Mechanismus; es identifiziert nicht die vollständige Spektralstruktur der Terminaloperatoren.

## 5. Was von der vorgeschlagenen Dreiteilung bleibt

Für ein festes altes positives Terminal lässt sich

\[
F_A=K_A\oplus_{q_A}R_A
\]

bilden. Physische Nullfortsetzung erhält q und L² auf alten Quellen. Daher gilt nach Transport exakt

\[
q_B(JK_A,JR_A)=0.
\]

Ein geeignet gewähltes topologisches Komplement des gesamten alten Bildraums führt weiterhin zum vorgeschlagenen Block

\[
\begin{pmatrix}
S&0&C_K\\
0&R&C_R\\
C_K^*&C_R^*&D_0
\end{pmatrix}.
\]

Die Nullkopplung zwischen den beiden alten Teilen ist also korrekt. Der hier untersuchte Boden für R ist jedoch bei der bisherigen Raumwahl weiterhin winzig. Er ist positiv und ausschließlich alt begründet; seine Kleinheit macht die anschließende Abschätzung von C_R und D₀ anspruchsvoller. Sie verhindert die Fortsetzung nicht logisch.

Der nächste sinnvolle Schritt ist eine **besser an die tatsächliche Form angepasste Quellenwahl**, etwa ein zertifizierter spektraler Raum oder ein Raum mit kontrollierter vollständiger Schur-Graphkorrektur. Für einen nachgewiesenen echten Spektralraum würde die q-Orthogonalität die entsprechenden niedrigen Eigenrichtungen tatsächlich entfernen. Die bisherigen F-Richtungen besitzen diesen Nachweis nicht.

Ein optimaler Rang ist damit noch nicht bestimmt. Die Rechnung beantwortet zunächst die konkrete Frage zur vorhandenen Familie: Die getesteten Ränge 1 bis 20 liefern keinen großen Gap. Ein weiterer reiner Rangscan derselben Art ist durch diese Daten weniger aussichtsreich als eine Verbesserung der Raumwahl.

## 6. Ein verschwindender physischer Gap widerlegt Objekt X nicht

Die konzeptionelle Unterscheidung aus dem Prüfauftrag ist richtig: Sind alle endlichen Stufen positiv und die injektiven Transporte kohärent und q-isometrisch, dann definiert die gemeinsame Form auf der gerichteten Vereinigung ein positives Prä-Hilbertprodukt. Jeder von null verschiedene Vektor wird bereits auf einer endlichen Stufe positiv ausgewertet. Dafür ist kein einheitlicher positiver L²-Boden über alle Stufen nötig.

Offen bleiben damit mögliche zusätzliche Anforderungen an die Einbettung, Vervollständigung und Identifikation mit der vollständigen Weil-Testklasse. Die drei vorhandenen Terminals beweisen auch noch nicht die Positivität sämtlicher endlicher Stufen.

Die ähnliche Größenordnung früherer Reserveverluste und der gemessenen Werte 1−κ ist ein Forschungsindiz. Sie ist kein bereits bewiesenes Gesetz: Die veröffentlichten c_A sind konservative Untergrenzen, und 1−κ misst einen anderen, relativen Schurquotienten.

## 7. Ausgeführte Prüfungen und Grenzen

- 120 Fälle mit 1024-Bit-Arb-Arithmetik; Konstruktion der zusätzlichen alten Diagnoserichtungen und gerichtete Auswertung der tatsächlichen alten Quellenformen.
- Dieselben exakt fixierten Räume erneut mit 1280 Bit. Die größte relative Änderung einer Arb-Obergrenze beträgt weniger als 6·10⁻⁹; die Schlussfolgerungen und die gerundete Ergebnistabelle bleiben stabil.
- Unabhängiger Standardbibliotheksprüfer mit Ganzzahlintervallen und 220 Dezimalstellen: 120 Schurprojektions-Zeugen, 126 positive Formpivots und die L²-Grammatrizen erfolgreich geprüft.
- Exakte rationale Prüfung der Schurprojektionsidentität und des zweidimensionalen Gegenbeispiels.
- Zehn Repository-Dateien erneut byteweise gegen den Commit [`d16ba43ebb20f2c61f43379fc65d7a9b9dba76de`](https://github.com/Waschtl904/objekt-x-programm/tree/d16ba43ebb20f2c61f43379fc65d7a9b9dba76de) geprüft; unveränderte Übernahme der ersten drei alten Richtungen kontrolliert.

Der unabhängige Ganzzahlprüfer beginnt bei den von Arb erzeugten Projektions-Gramintervallen. Er baut die ursprünglichen Terminalintegrale und auch diese Projektion nicht unabhängig neu auf. Die Herkunft der Intervalle wird durch den separaten Arb-Lauf und die Eingabebindungen dokumentiert. Die ursprünglichen Terminalzertifikate bleiben Voraussetzungen dieses Blocks.

**Status:** alte, terminalgebundene Einschließungen der Komplement-Gaps und explizite Zeugen gegen einen großen Gap der bisherigen Raumfamilie. Keine neue Kammer, keine allgemeine Low-Schur-Erneuerung, keine Statusaufwertung und keine Veröffentlichung auf Main.

## Paketdateien

- `gap_bounds.json`: primäre 120 Einschließungen.
- `gap_bounds_crosscheck.json`: Wiederholung und nach außen gerundete Projektions-Gramintervalle.
- `verification.json`: unabhängiger Ganzzahl-Replay, konservative monotone Obergrenzen, Distanzschranken und Eingabebindungen.
- `fixed_vectors.json`: alle 126 fixierten Quellenkoeffizienten.
- `old_vectors.json`: unveränderte Ursprungsdatei der alten Diagnoserichtungen.
- `ALLE_RAENGE.md`: Übersicht aller Ränge, aus den geprüften rationalen Werten erzeugt.
- `old_complement_gap.py`, `verify_old_complement_gap.py`: Reproduktion.
- `REPRODUKTION.md`, `SHA256SUMS`: Aufrufe und Dateibindungen.
