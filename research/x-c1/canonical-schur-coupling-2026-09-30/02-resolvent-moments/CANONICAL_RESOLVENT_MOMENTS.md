# Energie und inverse Energie der kanonischen Ergänzungen

29. September 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

Kanonische Basis: [`main@8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b`](https://github.com/Waschtl904/objekt-x-programm/tree/8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b).

## Ergebnis

**Für alle vier echten kanonischen Ergänzungsräume liegen jetzt beidseitige Resolventen- und κ-Einschließungen vor. Die kanonische relative Kopplung ist tatsächlich nahe eins.** Die Rechnung verwendet die vollständige Low-/High-Antwort und keinen globalen Ansatz Q_B⁻¹≤c_B⁻¹I.

Maßgeblich ist weiterhin die quadrierte Kopplungsnorm κ. Die folgende Tabelle zeigt den verbleibenden relativen Schurrest **1−κ**; beide Grenzen sind nach außen gerundet:

| Übergang | Parität | dim E | Untergrenze für 1−κ | Obergrenze für 1−κ |
| --- | --- | ---: | ---: | ---: |
| A₈ → A₉ | gerade | 1 | **3.2619·10⁻⁹** | **2.1432·10⁻⁷** |
| A₈ → A₉ | ungerade | 1 | **2.0081·10⁻⁹** | **3.1340·10⁻⁵** |
| A₉ → A₁₁ | gerade | 2 | **5.2319·10⁻¹⁷** | **3.0103·10⁻¹²** |
| A₉ → A₁₁ | ungerade | 2 | **3.1660·10⁻¹⁷** | **3.5804·10⁻¹¹** |

Damit sind komfortable Werte wie 1−κ≈10⁻² oder 10⁻⁴ für diese vier Zerlegungen ausgeschlossen. Beim zweiten Übergang ist der tatsächliche Rest nachweislich kleiner als beim ersten: **mindestens um Faktor 1000 für gerade und um Faktor 50 für ungerade Quellen**, aus den jeweiligen oberen und unteren Grenzen.

Die Intervalle sind teils mehrere Größenordnungen breit. Insbesondere wird weder 10⁻¹⁵ noch eine andere einzelne Größenordnung als tatsächlicher Wert des zweiten Übergangs behauptet. Die neuen **oberen** Grenzen zeigen jedoch erstmals für diese echten kanonischen Räume, dass die starke relative Kopplung nicht allein aus dem früher eingesetzten globalen Inversenbound stammt.

Diese Aussage betrifft den relativen Schurverlust in der festgelegten Zerlegung. Sie berechnet nicht sämtliche Ursachen der absoluten Terminalreserven. Die Rechnung bleibt retrospektiv und benutzt die bereits positive Kette bis A₁₁; ein unabhängiger vorwärts gerichteter Renewal-Satz bleibt offen.

## 1. Räume, Basis und benötigte Momente

Es gelten die veröffentlichten Definitionen

\[
b_A=q_A+17\|\cdot\|_2^2,\quad
K_A=\operatorname{ran}\mathbf1_{(0,10^{-4})}(\mathcal A_A),
\]

\[
W=P_BJ_{A,B}K_A,\qquad E=K_B\ominus_{b_B}W.
\]

Die echten kritischen Ränge sind 5, 6 und 8 je Parität. Die vollständigen Komplement-Gaps und die Injektivität des Transports sind gebundene Voraussetzungen. K_B^{⊥b} koppelt exakt nicht an K_B.

Dieser Block wählt eine neue, exakt definierte Basis desselben E. Ihre Koordinaten müssen nicht mit der Polarprojektionsbasis des Außenmassenberichts übereinstimmen. κ ist davon unabhängig.

Seien U_A und U_B die bereits festgelegten **L²-orthonormalen physischen polynomialen Hilfsbasen**, einschließlich Mellinkorrektur. Die gespeicherten Ritzmatrizen seien S_A=U_A*Q_AU_A und S_B=U_B*Q_BU_B. Diese Hilfsräume sind keine echten Spektralräume. Aus ihren oberen Rayleighgrenzen unter dem vollständigen Komplement-Gap und der richtigen Rangzahl folgt jedoch: P_AU_A und P_BU_B sind Basen von K_A bzw. K_B.

Definiere die exakte kleine Matrix

\[
Y=\frac1{17}b_B(JP_AU_A,P_BU_B).
\]

Ihre ersten r_A Spalten bilden Y_l, die übrigen Y_r. Die Rechnung zertifiziert die Invertierbarkeit von Y_l und setzt

\[
N=\begin{pmatrix}-Y_l^{-1}Y_r\\I_d\end{pmatrix},
\quad V_0=P_BU_BN,\quad G_0=V_0^*V_0.
\tag{1}
\]

Dann bilden die Spalten von V₀ **den echten kanonischen Ergänzungsraum**: YN=0 ist genau dessen b-Orthogonalitätsbedingung. Mit der unteren Cholesky-Matrix C_G von G₀ ist

\[
V=V_0C_G^{-T}
\]

eine exakt definierte L²-orthonormale Basis von E. Sämtliche physischen Momentmatrizen dieses Pakets beziehen sich auf diese Basis:

\[
L=V^*Q_BV,\qquad Z=V^*Q_B^{-1}V.
\]

In den Rohkoordinaten V₀ heißen diese Matrizen L₀ und Z₀. Die Gram-Matrix G₀ wird mitgeführt und nicht durch die Einheitsmatrix ersetzt.

## 2. Richtungsweise Einschließung des echten kanonischen Raums

Setze R_A=(I−P_A)U_A, R_B=(I−P_B)U_B und M=(JU_A)*U_B. Für die vollständigen physischen Komplement-Gaps ν_A,ν_B gelten

\[
R_A^*R_A\preceq S_A/\nu_A,\qquad
R_B^*R_B\preceq S_B/\nu_B.
\]

Schreibe a_i=(S_A)_{ii}, b_j=(S_B)_{jj},

\[
\eta_i=\sqrt{a_i/\nu_A},\qquad
\delta_j=\sqrt{1-\sum_k|M_{kj}|^2}.
\]

Die Rechnung verwendet jeweils sichere obere Intervallgrenzen. Dann

\[
\boxed{|Y_{ij}-M_{ij}|\le
\eta_i\left(\sum_k\eta_k|M_{kj}|+\delta_j\right)
+\sqrt{a_i b_j}\left(\frac1{\nu_B}+\frac1{17}\right).}
\tag{2}
\]

**Begründung.** Die L²-Differenz ist

\[
M-(JP_AU_A)^*P_BU_B
=(JR_A)^*U_B+(JP_AU_A)^*R_B.
\]

Für den ersten Term zerlege U_B entlang JU_A und dessen L²-Komplement. Es gilt R_A*U_A=R_A*R_A; seine Einträge sind durch η_iη_k begrenzt. Der verbleibende Anteil der j-ten neuen Trialquelle hat Norm δ_j. Für den zweiten Term können beide Faktoren auf das neue hohe Spektralkomplement projiziert werden. Ihre Normen sind höchstens √(a_i/ν_B) bzw. √(b_j/ν_B), weil J die Form erhält. Die q-Komponente von Y ist durch Cauchy–Schwarz für die bereits positive Form höchstens √(a_i b_j)/17. Das ergibt (2).

Für eine feste Koeffizientenspalte w gilt dieselbe Abschätzung mit Mw, der Norm ‖w‖ und der Energie w*S_Bw anstelle der j-ten Spalte. Insbesondere ersetzt

\[
\delta_j\quad\text{durch}\quad
\sqrt{\|w\|^2-\|Mw\|^2}
\]

die entsprechende Restnorm. Diese richtungsweise Version vermeidet einen einzigen groben Fehler für alle alten Richtungen.

### Einschluss der Kernkoeffizienten

Ein exakter dyadischer Mittelpunkt M_c der linken Überlappungsmatrix und eine feste vorgeschlagene Kernmatrix W₀=[N₀;I] werden nur als Rechenhilfen benutzt. Mit einer eintragsweisen Schranke Δ für Y_l−M_c setzt der Prüfer

\[
C\ge|M_c^{-1}|\Delta,\qquad \|C\|_\infty<1.
\]

Die richtungsweise Fassung von (2) begrenzt |YW₀| durch R. Für

\[
\rho\ge(I-C)^{-1}|M_c^{-1}|R
\]

folgt |N_l−N₀|≤ρ. Das ist ein Neumann-Einschluss der echten Lösung, kein Ersetzen von Y durch M. Der unabhängige rationale Prüfer kontrolliert (2), die Kontraktion und die komponentenweisen Residuenungleichungen erneut. Er prüft auch die exakten letzten d Einheitskoordinaten von N.

## 3. Vollständige Resolventenantwort auf dem neuen Trialraum

Zunächst wird T=U_B*Q_B⁻¹U_B eingeschlossen. Die vorhandene Mellin-korrigierte Low-/High-Darstellung liefert einen niedrigen Block \(\mathsf L\), eine Kopplung \(\mathsf B\) und den **gesamten** hohen Block \(\mathsf H\), mit

\[
\mathsf H\succeq\delta I,\quad
\mathsf B\mathsf B^*\preceq H^{up},\quad
F\preceq\mathsf L-\delta^{-1}\mathsf B\mathsf B^*,\quad F>0.
\]

Dabei sind δ=2/3 bei A₉ und δ=1 bei A₁₁. Der niedrige obere Formblock ist \(L^+=L_{model}+e_LI\). Diese Matrizen und Fehler stammen aus den vollständigen Terminalzertifikaten.

Der duale Vektor einer physischen Trialquelle hat einen niedrigen Anteil a und einen vollständigen hohen Anteil h. Seine hohe Gram-Matrix G_h=h*h enthält die gesamte Mellin-Tailkorrektur. Konkret: Bei U_B=MellinMap·V_c, niedrigem Momentvektor t_l und Carrier c=−t_l*V_c ist

\[
a=V_c-t_lc,\qquad
G_h=\|t_h\|^2 c^*c,
\quad\|t_h\|^2=\rho-1-\|t_l\|^2.
\]

ρ ist die analytisch bekannte vollständige Momentnorm. Auch die Rundungsunsicherheit der sehr kleinen Differenz wird nach oben eingeschlossen.

Mit γ≥tr(F⁻¹H^{up}) und dem festen Young-Parameter s=10⁻²⁰ gelten

\[
T_-:=a^*(L^+)^{-1}a\preceq T,
\]

\[
\boxed{T\preceq T_+:=
(1+s)a^*F^{-1}a+
\left((1+s^{-1})\frac\gamma{\delta^2}+\frac1\delta\right)G_h.}
\tag{3}
\]

Die Untergrenze folgt aus der Variationsformel, eingeschränkt auf niedrige Testquellen. Für die Obergrenze eliminiert man den gesamten hohen Block. Der Schurterm ist mindestens F. Im verschobenen niedrigen dualen Vektor wird der hohe Anteil mit Young und
\(\|F^{-1/2}\mathsf B\|^2\le\gamma\), \(\|\mathsf H^{-1}\|\le1/\delta\) bezahlt.

Die Rechnung löst für die sechs bzw. acht Trial-Rechtsseiten sowie für die H^{up}-Spurbindung. Sie benötigt keinen explizit aufgebauten unendlichen inversen Operator. Die vorhandenen 296-/285-dimensionalen Vergleichsmatrizen bleiben Hilfsmittel zur vollständigen Resolventenkontrolle; der abschließende kanonische Test ist 1-/2-dimensional.

## 4. Übertragung auf die echte Ergänzung

Mit E_N=N*S_BN gilt

\[
G_0=N^*(I-R_B^*R_B)N.
\]

Der Verlust gegenüber N*N wird eintragsweise durch
√((E_N)_{ii}(E_N)_{jj})/ν_B begrenzt. Damit ist G₀ strikt positiv eingeschlossen.

Da Q_B und P_B kommutieren, zerfällt das inverse Moment spektral. Auf dem Komplement ist Q_B⁻¹≤ν_B⁻¹I. Daher

\[
\boxed{N^*T_-N-\nu_B^{-2}E_N
\preceq Z_0\preceq N^*T_+N.}
\tag{4}
\]

Der subtrahierte Term bezahlt gerade den hohen Spektralanteil der Trialquelle. Die großen inversen Momente des niedrigen Raums werden vollständig behalten.

### Eine positive untere Energiegrenze ohne globalen Terminalboden

Die obere Energiegrenze lautet L₀≤E_N. Für eine untere Grenze werden feste polynomielle duale Proben U_BW gewählt. W ist ein festgehaltener dyadischer Vorschlag aus T_+ und N. Für den tatsächlichen Überlappungsblock

\[
A=(U_BW)^*V_0=W^*N-W^*R_B^*R_BN
\]

werden die Fehler durch √(q[U_BW_i](E_N)_{jj})/ν_B bezahlt. Die Variationsformel für die positive Form ergibt

\[
\boxed{L_0\succeq A^*(W^*T_+W)^{-1}A.}
\tag{5}
\]

Eine gerichtete diagonale Skalierung, Symmetrisierung und Zeilenfehlerabschätzung verwandelt die Intervallfamilie rechts in eine feste positive Loewner-Untergrenze L_−. Analog wird eine obere Grenze L_+ gebildet. Positive Cholesky-Pivots bestätigen L_−>0. Der globale winzige Boden c_B wird in (3)–(5) nicht eingesetzt.

## 5. Auswertung der relativen Kopplung

In b-orthonormalen Koordinaten W⊕E sei der niedrige Operator

\[
\mathscr A=\begin{pmatrix}S&C\\C^*&D\end{pmatrix},\qquad
\kappa=\|S^{-1/2}CD^{-1}C^*S^{-1/2}\|.
\]

Die Kompression der Inversen auf E ist H=(D−C*S⁻¹C)⁻¹. Die Gleichheit der nichtverschwindenden Kopplungseigenwerte auf beiden Blockseiten liefert

\[
1-\kappa=\frac1{\lambda_{max}(D^{1/2}HD^{1/2})}.
\]

Für die L²-Momente sind B_E=L+17I, R=L+34I+289Z und

\[
1-\kappa=\frac1\beta,\qquad
\beta=\lambda_{max}(R B_E^{-1}L B_E^{-1}).
\tag{6}
\]

H wird ausdrücklich nicht mit D⁻¹ identifiziert.

Um bei den breiten Momentfamilien unnötige Auslöschung zu vermeiden, wird

\[
\Phi=\lambda_{max}(Z^{1/2}LZ^{1/2})
\]

über gewichtete Spuren begrenzt. Mit den Faktoren T_−=F_−*F_−, T_+=F_+*F_+ und L_−=C_−C_−*, L_+=C_+C_+* gilt

\[
t_-=
\|F_-NG_0^{-1}C_-\|_F^2
-\nu_B^{-2}\operatorname{tr}(G_0^{-1}L_-G_0^{-1}E_N),
\]

\[
t_+=\|F_+NG_0^{-1}C_+\|_F^2,
\qquad t_-/d\le\Phi\le t_+.
\tag{7}
\]

Diese Schlüsse verwenden die Monotonie der Spur gegen positive Faktoren, (4) und (5). Die unteren und oberen Normquadrate werden aus rationalen Intervallendpunkten berechnet; bei einem Intervall durch null ist die untere Quadratschätzung null.

Der veröffentlichte kritische obere physische Spektralwert Θ_B gibt 0<L≤Θ_BI. Für f(L)=L(L+17I)⁻² folgt

\[
\frac{L}{(17+\Theta_B)^2}\preceq f(L)\preceq\frac L{289}.
\]

Da R=L+34I+289Z,

\[
\frac{289}{(17+\Theta_B)^2}\Phi
\le\beta\le\Phi+\frac{(\Theta_B+34)\Theta_B}{289}.
\tag{8}
\]

Die Kombination von (7) und (8) liefert die Ergebnistabelle. Die d=2-Spurabschätzung kostet höchstens einen zusätzlichen Faktor zwei auf dieser Auswertungsstufe. Ein größerer Teil der Intervallbreite kommt aus der Einschließung des wahren kanonischen Raums, den vollständigen Resolventenvergleichen und Intervallabhängigkeiten.

## 6. Die Momentmatrizen selbst

`primary.json` und `crosscheck.json` enthalten die vollständigen gerichteten Matrixfamilien für G₀, L₀, Z₀ sowie Eintragsintervalle von L und Z in der definierten L²-Basis. Aus einer Loewner-Einschließung A≤X≤B wird ein Eintrag um (A+B)/2 mit Radius √((B−A)_{ii}(B−A)_{jj})/2 eingeschlossen. Diese Umrechnung kann breite, auch negative Diagonaluntergrenzen erzeugen; daraus folgt keine negative Energie.

Zusätzlich bestehen positive Loewner-Böden für die tatsächlichen physischen Matrizen:

\[
L\succeq\ell I>0,\qquad Z\succeq\Theta_B^{-1}I>0.
\]

Die Zahl ℓ folgt aus L_− und G₀. Für Z verfeinert der rationale Prüfer außerdem jede Diagonale direkt als positives Normquadrat, einschließlich der Projektion auf den vollständigen hohen Rest.

Für die eindimensionalen Ergänzungen sind L und Z selbst Skalare. Sichere, zusätzlich nach außen gerundete Anzeigen sind:

| Übergang A₈→A₉ | L=q_B[v] bei ‖v‖₂=1 | Z=⟨v,Q_B⁻¹v⟩ |
| --- | --- | --- |
| gerade | [2.06·10⁻⁶, 2.23·10⁻⁶] | [2.25·10¹², 1.38·10¹⁴] |
| ungerade | [1.09·10⁻⁴, 1.47·10⁻⁴] | [2.89·10⁸, 3.41·10¹²] |

Die zweidimensionalen Fälle enthalten auch die vollen Kreuzterme. Ihre ersten inversen Diagonalmomente liegen sicher in [1.17·10²¹,1.84·10²²] bzw. [2.84·10¹⁸,3.70·10²⁰]. Die zweite Diagonale ist deutlich breiter eingeschlossen. Diese Angaben sind basisabhängig; der κ-Schluss nutzt die vollständige gemeinsame Matrixrechnung und ist basisunabhängig.

## 7. Prüfung, Korrektur und Grenzen

- **25 Repository-Eingaben** wurden byteweise gegen den festgelegten Main-Commit und die historischen SHA-Bindungen geprüft.
- Die vollständige neue Resolventenrechnung wurde bei **1024 und 1280 Bit** mit python-flint 0.9.0 ausgeführt. Die relevanten Matrixintervalle überlappen. Die ursprünglichen Terminalintegrale wurden dabei nicht neu aufgebaut.
- Der unabhängige Standardbibliothek-Prüfer berechnet mit exakten rationalen Zahlen für beide Läufe erneut die kanonischen Annihilatorfehler, die Neumann-Residuen und die kleinen gewichteten Norm-/Spur- und κ-Schlüsse. Er prüft positive kleine Gram-/Energiegrenzen und die Quellenbindungen. Die großen gerichteten Resolventenlösungen und ihre Cholesky-Faktoren bleiben Arb-Eingaben; es wird kein zweiter unabhängiger vollständiger 296-/285-Matrixsolver behauptet.
- `verification.json` ist für die Ergebnistabelle maßgeblich. Seine rationalen Schlussintervalle können enger oder weiter als die Arb-Anzeige ausfallen, weil dieselben gerichteten Eingaben mit anderer Intervallauswertung verarbeitet werden. Die Tabelle nimmt die äußere Vereinigung beider geprüfter Läufe.
- Ein früher Entwicklungsversuch behandelte einen unbestimmten Zwischenwert fälschlich als null und lieferte ein zu enges vorläufiges Intervall. Dieses Ergebnis wurde verworfen. Die Endrechnung benutzt explizite Quadratschranken und bricht bei nichtendlichen Größen ab. Fünf gezielte Prüfungen dieser Randfälle bestehen. Das verworfene Ergebnis ist kein Paketbeleg.

Die analytischen Argumente (1)–(8) gehören zum Nachweis; der Code ist kein formales Beweisassistenzsystem. Externer mathematischer Review bleibt offen.

**Forschungsfolge:** Die echte kanonische Zerlegung macht die letzte Rechnung klein, beseitigt aber die starke relative Kopplung nicht. Ein künftiger Renewal-Satz muss mit dieser tatsächlich nachgewiesenen Nähe zu eins umgehen oder eine andere energiegerechte Darstellung rechtfertigen. Es wäre voreilig, daraus ein allgemeines Scheitern der Fortsetzung abzuleiten.

Main, Registry, historische Quellen und PR #187 wurden in diesem lokalen Block nicht verändert. Es wird keine vierte Kammer, kein allgemeiner Renewal-Satz, keine kofinale Positivität und kein globales Objekt X behauptet.
