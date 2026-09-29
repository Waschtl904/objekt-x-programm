# A₁₁: zertifizierter niedriger Spektralraum

28. September 2026 · lokaler Forschungsblock · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

## Ergebnis

**Am Terminal A₁₁ genügt ein echter kritischer Spektralraum von acht Dimensionen pro Parität für einen Komplement-Gap q/b ≥ 10⁻⁴. Dieser Rang ist für diese Zielschwelle minimal.** Im gemeinsamen geraden und ungeraden Raum beträgt die kanonische Dimension damit **16**.

Die Schwelle 10⁻⁴ ist eine ausdrücklich gewählte quantitative Bedeutung von „robust“ für diesen Vergleich. Ein schwellenunabhängiger optimaler Rang wird nicht behauptet.

Mit b = q + 17‖·‖² und dem durch q im b-Hilbertraum dargestellten Operator \(\mathcal A\) ist der Raum exakt definiert durch

\[
\boxed{K=\operatorname{ran}\mathbf1_{(0,10^{-4})}(\mathcal A)
=\operatorname{ran}\mathbf1_{(0,17/9999)}(Q).}
\]

Die Dimension, die spektrale Trennung und der Gap des vollständigen Komplements sind zertifiziert. Zusätzlich ist die Lage dieses echten Raums relativ zu expliziten alten Testräumen eingeschlossen. **Es wurden noch keine numerischen Koordinaten einer echten Eigenbasis ausgegeben.** Die alten Testvektoren werden nicht zu Eigenvektoren umbenannt.

| Parität | Optimaler Gap nach sieben Richtungen: Obergrenze | Optimaler Gap nach acht Richtungen: Einschließung |
| --- | ---: | ---: |
| gerade | 1.995·10⁻⁷ | [1.884·10⁻⁴, 2.464·10⁻⁴] |
| ungerade | 1.014·10⁻⁵ | [8.069·10⁻⁴, 5.188·10⁻³] |

Damit ist die frühere Raumwahlfrage für diese Schwelle entschieden: Die untersuchten F-Diagnoseräume ließen selbst bei Rang 20 im geraden Komplement Quellen mit q/b ≤ 1.967·10⁻³⁸ zu. Der **echte** Spektralraum hat schon bei Rang acht einen Gap von mindestens 1.884·10⁻⁴. Beide Aussagen betreffen dieselbe tatsächliche Terminalform.

Dieser Block führt den ausdrücklich vorgeschlagenen ersten Schritt bei A₁₁ aus. Die analogen kanonischen Räume bei A₈ und A₉, ihre numerischen physischen Transporte und ein erneuter κ-Test mit den echten Räumen sind noch nicht berechnet. Main, Registry und bestehende Beweise bleiben unverändert.

## 1. Die optimale Raumwahl und ihre Voraussetzungen

Am festen positiven Terminal ist Q der positive selbstadjungierte Operator der geschlossenen Form im Mellin-nulligen physischen L²-Raum. Die Form b gehört zu Q + 17I. Auf ihrem Formraum gilt

\[
\mathcal A=I-17(Q+17I)^{-1}.
\]

Unter der kanonischen Identifikation des b-Hilbertraums mit L² ist dies der beschränkte Operator Q(Q + 17I)⁻¹. Der bereits positive Terminalboden macht \(\mathcal A\) beschränkt invertierbar.

Für jeden endlichen Quellenraum K gilt

\[
u\perp_qK\iff u\perp_b\mathcal A K.
\]

Weil \(\mathcal A\) invertierbar ist, durchläuft \(\mathcal A K\) alle Räume derselben endlichen Dimension. Das Minimax-Prinzip ergibt deshalb

\[
\sup_{\dim K=r}\inf_{0\ne u\perp_qK}\frac{q[u]}{b[u]}
=\lambda_{r+1}(\mathcal A)
=\frac{\mu_{r+1}(Q)}{\mu_{r+1}(Q)+17}.
\]

Die benötigte diskrete Spektralstruktur folgt hier aus dem bereits vorliegenden allgemeinen Tail-Prinzip: Für jeden endlichen Boden existiert am festen Terminal ein Teilraum endlicher Kodimension mit mindestens diesem Boden. Jeder beschränkte Spektralbereich von Q ist damit endlichdimensional; Q hat kompakte Resolvente. Die Eigenwerte von \(\mathcal A\) können sich bei 1 häufen. Sie werden nicht mit den Eigenwerten einer endlichen F-Matrix identifiziert.

Ein durch eine echte Spektralschwelle definierter Raum ist invariant unter Q. Sein q-orthogonales Komplement stimmt mit seinem L²- und b-orthogonalen Komplement überein. Genau deshalb entfernt diese Raumwahl die niedrigen spektralen Richtungen auch energetisch.

## 2. Die korrekte vollständige Schurformel

Die gespeicherten Koordinaten sind Mellin-korrigierte Quellen

\[
u=M(Ec+y).
\]

Diese Abbildung ist nicht unitär. Deshalb ist die gespeicherte Blockform \(\widehat Q=M^*QM\) zusammen mit ihrer **Massenmatrix** zu betrachten:

\[
\widehat Q=\begin{pmatrix}L&B\\B^*&H\end{pmatrix},\qquad
G=M^*M=\begin{pmatrix}G_{LL}&G_{LH}\\G_{HL}&G_{HH}\end{pmatrix}.
\]

Auf dem trägerfreien Referenzraum hat M die Form Mz = z − e⟨t,z⟩. Daher gilt G = I + tt*, insbesondere

\[
I\preceq G\preceq\rho I,\qquad
\rho=\frac{\|m\|^2}{|\langle m,e\rangle|^2}<\frac{1003}{1000}
\]

in beiden Paritäten. Im vorhandenen vollständigen hohen Raum gilt q[My] ≥ ‖My‖². Somit ist H − μG_HH für 0 ≤ μ < 1 positiv invertierbar.

Der tatsächliche parameterabhängige Schurrest lautet

\[
\boxed{\mathscr S(\mu)=L-\mu G_{LL}
-(B-\mu G_{LH})(H-\mu G_{HH})^{-1}(B^*-\mu G_{HL}).}
\]

Sein Kern entspricht genau den Eigenquellen von Q zum Eigenwert μ. Für

\[
Y_\mu=\begin{pmatrix}I\\-(H-\mu G_{HH})^{-1}(B^*-\mu G_{HL})\end{pmatrix}
\]

gilt

\[
\boxed{\mathscr S'(\mu)=-Y_\mu^*G Y_\mu\preceq-I.}
\]

Die strenge Monotonie bleibt erhalten. In einer orthonormalen physischen Blockbasis reduziert sich diese Formel auf die im Prüfauftrag genannte Form. Die Massenmatrix in den vorhandenen Koordinaten einfach durch I zu ersetzen wäre dagegen falsch.

## 3. Vollständige spektrale Untergrenzen ohne hohe Trunkierung

Aus den gebundenen Terminaldaten gelten

\[
H\succeq I,\quad BB^*\preceq H^{up},\quad
L\succeq L_0-e_LI,\quad F=L_0-e_LI-H^{up}>0.
\]

Die gerichtete Rechnung liefert

\[
H^{up}\preceq\gamma F,\qquad
\gamma\le\operatorname{tr}(F^{-1}H^{up})<60.
\]

Die berechneten Spurgrenzen liegen bei etwa 58.98951 (gerade) und 58.82239 (ungerade). Das ist eine Abschätzung der vollständigen hohen Kopplung.

Setze t = ρμ. Für t < 1 wird zunächst q − μ‖·‖² durch die Referenzform q − t‖(c,y)‖² nach unten abgeschätzt. Nach vollständiger hoher Elimination folgt

\[
\mathscr S_{\rm Vergleich}(\mu)
\succeq F-tI-\frac{t}{1-t}H^{up}
\succeq a(t)F-tI,
\quad a(t)=1-\frac{\gamma t}{1-t}.
\]

Ist fⱼ eine positive Untergrenze des j-ten Eigenwerts der endlichen Vergleichsmatrix F und gilt a(t)fⱼ ≥ t mit a(t) > 0, dann hat die vollständige Form q − μ‖·‖² höchstens j−1 negative Richtungen. Folglich ist μⱼ(Q) ≥ μ. Die verwendete Wurzel ist

\[
t(f)=\frac{2f}{1+(1+\gamma)f+
\sqrt{[1+(1+\gamma)f]^2-4f}},\qquad
\mu_j(Q)\ge\frac{t(f_j)}{\rho}.
\]

Die abschließende Prüfung setzt die ausgegebenen rationalen Untergrenzen wieder exakt in a(t)f ≥ t ein. Es wird keine hohe Modenzahl als Ersatz für die ganze Antwort gewählt.

Für die Obergrenze dient ein tatsächlicher j-dimensionaler physischer Testraum. Sind Sⱼ seine Form-Grammatrix und Gⱼ seine L²-Grammatrix, dann liefert Rayleigh–Ritz

\[
\mu_j(Q)\le\max_{x\ne0}\frac{x^*S_jx}{x^*G_jx}
\le\frac{\text{Gershgorin-Obergrenze}(S_j)}{
\text{positive Gershgorin-Untergrenze}(G_j)}.
\]

Die alten Richtungen werden hierfür ausschließlich als Testquellen eingesetzt. Die Unter- und Obergrenzen beziehen sich anschließend auf die **echten** Eigenwerte des unendlichen Operators.

## 4. Die ersten neun physischen Eigenwerte

Die Anzeigen sind nach außen gerundet. Maßgeblich sind die rationalen Endpunkte in `verification.json`.

| j | μⱼ gerade: Untergrenze | μⱼ gerade: Obergrenze | μⱼ ungerade: Untergrenze | μⱼ ungerade: Obergrenze |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 9.455·10⁻⁴² | 1.081·10⁻⁴¹ | 1.209·10⁻³⁸ | 1.557·10⁻³⁸ |
| 2 | 5.013·10⁻³⁵ | 6.038·10⁻³⁵ | 4.996·10⁻³² | 6.002·10⁻³² |
| 3 | 5.123·10⁻²⁹ | 6.274·10⁻²⁹ | 1.840·10⁻²⁶ | 2.093·10⁻²⁶ |
| 4 | 1.108·10⁻²³ | 1.434·10⁻²³ | 5.256·10⁻²¹ | 5.821·10⁻²¹ |
| 5 | 1.484·10⁻¹⁸ | 1.831·10⁻¹⁸ | 1.933·10⁻¹⁶ | 2.149·10⁻¹⁶ |
| 6 | 4.055·10⁻¹⁴ | 4.886·10⁻¹⁴ | 6.028·10⁻¹² | 6.940·10⁻¹² |
| 7 | 6.480·10⁻¹⁰ | 7.392·10⁻¹⁰ | 4.577·10⁻⁸ | 5.420·10⁻⁸ |
| 8 | 3.105·10⁻⁶ | 3.392·10⁻⁶ | 1.447·10⁻⁴ | 1.723·10⁻⁴ |
| 9 | 3.203·10⁻³ | 4.190·10⁻³ | 1.372·10⁻² | 8.866·10⁻² |

Diese neun Intervalle sind innerhalb jeder Parität voneinander getrennt. Für die ersten 21 Eigenwerte wurden ebenfalls Schranken erzeugt; die späteren Untergrenzen werden wegen der konservativen hohen Vergleichsabschätzung wesentlich breiter. Daraus werden keine engen späteren Eigenwertlagen abgeleitet.

Der Sprung zwischen μ₈ und μ₉ beantwortet die Rangfrage für die gewählte Zielreserve. Da

\[
\frac{\mu}{\mu+17}<10^{-4}\iff\mu<\frac{17}{9999},
\]

liegen genau acht Eigenwerte je Parität unter dieser Schwelle. Der Rest ist spektral davon getrennt. Auf dem vollständigen Komplement des gemeinsamen 16-dimensionalen Raums gilt insbesondere q/b ≥ 1.884·10⁻⁴.

## 5. Unabhängige Rangzählung

Die zentrale Dimension wurde zusätzlich ohne Benutzung der berechneten F-Eigenwerte geprüft. Sei s = 1/500 und V die Matrix aus acht festgehaltenen alten Koeffizientenvektoren. Aus den ursprünglichen vollständigen F-Intervallen wurde mit Ganzzahlintervallen bewiesen:

\[
F-sI+VV^*>0,\qquad -V^*(F-sI)V>0.
\]

Die erste Aussage beschränkt die Zahl nichtpositiver Richtungen auf höchstens acht; die zweite liefert acht negative Richtungen. Damit hat F−sI **genau acht negative Eigenwerte und keinen Nullraum**.

Gleitkommarechnungen schlagen dafür lediglich rationale Dreiecksfaktoren R und T vor. Der unabhängige Prüfer rekonstruiert die reparierte Matrix aus F und den rationalen Vektoren. Er berechnet exakt nach außen gerundet

\[
\eta\ge\|I-RT\|,\quad \rho_T\ge\|T\|^2,\quad
\epsilon\ge\|F-sI+VV^*-R^*R\|.
\]

Das geprüfte Kriterium

\[
\frac{(1-\eta)^2}{\rho_T}-\epsilon>0
\]

beweist die Positivität der reparierten Matrix. Acht positive Intervall-LDL-Pivots prüfen die negative Kompression.

Mit den separat gerichteten vollständigen Grenzen γ < 60 und ρ < 1003/1000 wird die Aussage exakt auf den physischen Schnitt μ = 17/9999 übertragen: Für t = (1003/1000)μ gilt a(t)s−t > 0. Die physischen acht Testquellen liefern gleichzeitig acht Eigenwerte unter diesem Schnitt.

**Unabhängigkeit:** Diese Rangzählung verwendet nicht den numerischen Eigenwertalgorithmus. Die Kopplungsspurgrenze und der Massenbound bleiben Ergebnisse der separaten gerichteten Arb-Rechnung. Eine zweite unabhängige Neuerzeugung der ursprünglichen Terminalintegrale wird nicht behauptet.

## 6. Einschließung des echten Raums und verbleibende Rechenarbeit

Sei P der oben definierte echte Spektralprojektor. Sei U eine L²-orthonormierte Darstellung des expliziten alten acht-dimensionalen Testraums. Aus der spektralen Lücke und dessen maximalem Rayleighquotienten folgt

\[
\|(I-P)Ux\|_2^2\le
\frac{U_8}{\underline\mu_9}\|x\|^2.
\]

Die gerichteten Schranken ergeben

\[
\|(I-P)U\|\le0.033\quad\text{gerade},\qquad
\|(I-P)U\|\le0.113\quad\text{ungerade}.
\]

Beide Werte liegen unter 1. Deshalb ist P auf dem Testraum injektiv und bildet ihn auf den gesamten echten acht-dimensionalen Spektralraum ab. Insbesondere sind die mathematisch exakt definierten Quellen PU₁,…,PU₈ eine Basis dieses Raums. Ihre Gram-Matrix besitzt den Boden 1−‖(I−P)U‖².

Das ist eine zertifizierte Lageeinschließung des tatsächlichen Spektralraums. Für die frühere extrem empfindliche κ-Rechnung ist sie noch zu grob, um die Testquellen durch die projizierten Quellen zu ersetzen. Die Komponenten von PUᵢ oder eine entsprechend genaue hohe Resolventenantwort wurden noch nicht numerisch eingeschlossen.

Die gespeicherte vollständige Gram-Matrix BB* und ein hoher Boden bestimmen (H−μG_HH)⁻¹ nicht eindeutig. Sie reichen für die obigen spektralen Schranken und Rangzertifikate. Für eine numerische echte Eigenbasis und den anschließenden Transport-/Kopplungstest muss die hohe Antwort genauer ausgewertet werden. Diese nächste Aufgabe wird durch die neuen Ergebnisse auf einen klar bestimmten kritischen Raum begrenzt.

## 7. Ausgeführte Prüfungen und Status

- Gerichtete Einschließung aller 285 Vergleichseigenwerte je Parität mit 512 Bit und erneut mit 768 Bit.
- Physische Unter- und Obergrenzen für jeweils 21 Eigenwerte, einschließlich des vollständigen hohen Raums und der Massenmatrix.
- Unabhängige Ganzzahl-Rangzählung aus den ursprünglichen Intervallmatrizen und rationalen Quellenkoeffizienten.
- Exakte rationale Kontrolle der Übertragung auf den physischen Schnitt, der Minimax-Untergrenzen und der Lageeinschließung des echten Spektralraums.
- Exakte Tests der verallgemeinerten Schur-Determinantenidentität und ihrer Ableitung bei nichttrivialer Massenmatrix.
- Bytevergleich der verwendeten Repository-Quellen und der beiden analytischen Beweisdateien gegen den Commit [`d16ba43ebb20f2c61f43379fc65d7a9b9dba76de`](https://github.com/Waschtl904/objekt-x-programm/tree/d16ba43ebb20f2c61f43379fc65d7a9b9dba76de).

Die Aussagen bleiben an die vorhandenen analytischen Terminal- und Tail-Bindungen gebunden. Der ursprüngliche Aufbau der Integrale wurde in diesem Block nicht wiederholt. Die neuen Ableitungen und Zertifikate behaupten keinen externen Review.

**Abgeschlossen ist der erste A₁₁-Spektralblock: kanonische Raumdefinition, exakte Dimension, minimaler Rang für die gewählte Zielreserve, vollständiger Komplement-Gap und Lageeinschließung.** Noch offen sind eine numerische echte Eigenbasis, die entsprechenden A₈-/A₉-Räume und der erneute κ-Test nach physischem Transport. Ein allgemeiner Renewal-Satz folgt daraus noch nicht.
