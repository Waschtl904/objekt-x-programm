# A11: vollständiger Tail mit gemeinsamer Shift-/Potentialabschätzung

27. September 2026 · Lokale Herleitung · **EXTERNAL_REVIEW_OPEN**

Dieses Dokument beweist den neuen vollständigen High-Floor und formuliert
die hinreichende Terminalrechnung. Ihr tatsächliches Rechenergebnis steht
separat in den Ergebnisquittungen und im abschließenden README.

## 1. Festgelegte Form und Quellen

Wir verwenden dieselbe konkrete C1a-Familie, die in SOURCE_BINDINGS.json
commitgebunden ist. Der Terminal ist A11=log(11)/2. Auf dem Referenzraum
H=L²((-1,1),dx/2) mit U_Au(x)=sqrt(2A)u(Ax) gilt

\[
Q_A=D_H+V+q_0(A)I-K_A-S_A,
\quad D_He_n=H_ne_n,\quad e_n=\sqrt{2n+1}P_n,
\]
\[
V(x)=-\tfrac12\log(1-x^2),\qquad q_0(A)=-\log(2\pi A)-\gamma,
\]
\[
K_A f(x)=2A\int k_{reg}(A|x-y|)f(y)\,d\mu(y),\quad
k_{reg}(t)=\frac{e^{-t/2}}{1-e^{-2t}}-\frac1{2t}.
\]

S_A ist die Summe der beiden nullfortgesetzten Translationen um ±log(q)/A,
jeweils mit Gewicht w_q=log(p)/sqrt(q) für q=p^k. Am Terminal sind genau
2,3,4,5,7,8,9 aktiv. q=11 bleibt am Kontakt inaktiv. Auf A9≤A≤A11 kann
q=9 mitgeführt werden, weil sein Shift bei A9 fast überall null ist.

Die zwei ursprünglichen Mellinbedingungen lauten E_±u=∫e^(±t/2)u(t)dt=0.
Es wird kein zusätzlicher oder geänderter Quellenraum eingeführt.
Auf rohen Vektoren vor der Momentkorrektur bezeichnet Q_A die dargestellte
poltermfreie Form auf der Referenzdomäne. Sie stimmt auf den zulässigen
Zwei-Mellin-Quellen mit der physischen Form überein. Insbesondere beziehen
sich q_A(y,e_p) und Q_Ae_p unten auf diese ausdrücklich festgelegte Erweiterung.
Die Legendre-Normierung entspricht [DLMF 18.3](https://dlmf.nist.gov/18.3).

## 2. Ein allgemeiner gemeinsamer Formbound für V und alle Shifts

Für beliebige positive Gewichte und nullfortgesetzte Funktionen gilt

\[
\langle f,S_Af\rangle\le\int r_A(x)|f(x)|^2d\mu(x),\qquad
r_A(x)=\sum_q w_q\bigl(1_{(-1,1)}(x+d_q)+1_{(-1,1)}(x-d_q)\bigr).
\tag{1}
\]

Denn für jeden Shift wird 2 Re(conj(f(x))f(x+d)) durch
|f(x)|²+|f(x+d)|² beschränkt; nach Variablentausch ergibt sich genau (1).
Genauer gilt die nichtnegative Differenzidentität

\[
\int r_A|f|^2d\mu-\langle f,S_Af\rangle
=\sum_q w_q\int_{-1}^{1-d_q}|f(x+d_q)-f(x)|^2d\mu(x),
\]

wobei ein leeres Überlappungsintervall den Beitrag null liefert.
Dies gilt für komplexe Funktionen, beide Paritäten und den gesamten L²-Raum.
Somit gilt auf der V-Formdomäne

\[
\langle f,(S_A-V)f\rangle\le
\operatorname*{ess\,sup}_{|x|<1}(r_A(x)-V(x))\,\|f\|^2.
\tag{2}
\]

Für x≥0 nimmt die Aktivität jeder der zwei Translationen mit wachsendem
A zu: Die Bedingungen lauten d_q<1-x beziehungsweise d_q<1+x.
Daher r_A≤r_A11 für A≤A11. V ist unverändert. Es genügt die Berechnung
am rechten Terminal; sie ist zugleich ein kammerweiter Formbound.

### Acht exakte Zellen bei A11

Mit d_q=2log(q)/log(11) sind die positiven Grenzen in dieser Reihenfolge

\[
0,\ 1-d_3,\ d_4-1,\ d_5-1,\ 1-d_2,\ d_7-1,\ d_8-1,\ d_9-1,\ 1.
\tag{3}
\]

Alle Ungleichungen werden durch rationale Logarithmuseinschließungen
streng geprüft. Die aktiven Shiftzahlen auf den acht offenen Zellen sind:

| Zelle | Nichtverschwindende Anzahlen pro Kanal |
| --- | --- |
| 1 | 2:2, 3:2 |
| 2 | 2:2, 3:1 |
| 3 | 2:2, 3:1, 4:1 |
| 4 | 2:2, 3:1, 4:1, 5:1 |
| 5 | 2:1, 3:1, 4:1, 5:1 |
| 6 | 2:1, 3:1, 4:1, 5:1, 7:1 |
| 7 | 2:1, 3:1, 4:1, 5:1, 7:1, 8:1 |
| 8 | 2:1, 3:1, 4:1, 5:1, 7:1, 8:1, 9:1 |

Auf jeder Zelle ist r konstant und V auf [0,1) monoton zunehmend.
Ihr Verlustmaximum liegt deshalb am linken Rand. Rationale obere Gewichte,
untere Randeinschließungen b und die untere Logarithmuseinschließung
V(b)=log(1/(1-b²))/2 beweisen in allen acht Fällen

\[
\boxed{S_A-V\ \preceq\ 59/20\,I\quad(A_9\le A\le A_{11}).}
\tag{4}
\]

Der größte ausgewiesene Zellbound ist kleiner als 2.946612<2.95.
Es wird die ganze Zelle analytisch kontrolliert; die Zellmitte im Prüfer
dient nur zur Bestimmung der konstanten Shiftaktivität. Sämtliche
Schaltgrenzen sind in (3) enthalten und streng getrennt.

Die separaten Operatornormen bleiben zusätzlich nötig für Momentträger:
q=2 hat höchstens vier Knoten mit Norm φ, q=3 drei mit Norm sqrt(2),
q=4,5,7,8,9 jeweils höchstens zwei mit Norm 1. Die direkte Integralzerlegung
nach Restklassen modulo log(q), wie im bytegebundenen A9-Beweis, gibt

\[
\|S_A\|\le\varphi w_2+\sqrt2w_3+w_4+w_5+w_7+w_8+w_9<33/8.
\tag{5}
\]

(4) ist eine obere Formschranke, keine Behauptung einer Operatornorm von
S_A−V. Die positive unbeschränkte Randfunktion wird vollständig mitbezahlt.

## 3. Neuer Gamma-, Konstanten- und Mellinverlust

Setze r=6/5>A11 und z0=r/2=3/5. Die exakte Identität
k_reg(2z)=(sech z+csch z−1/z)/4 liefert  k_reg≤1/4.
Für die untere Schranke verwenden wir

\[
B_r=\sum_{j=0}^{20}\frac{r^{2j}}{(2j+3)!}
 +\frac{r^{42}}{45!(1-r^2/(46\cdot47))},
\]

eine rationale Tayloroberschranke C_r für cosh(r), und die Monotonie von
z/(1+z²/6) für z²<6. Dann gilt auf 0≤z≤r

\[
k_{reg}(2z)\ge\tfrac14(C_r^{-1}-rB_r/(1+r^2/6))>47/500.
\]

Somit ||K_A||≤r/2=3/5. Auf y⊥e0 verschwindet der konstante Kern 1/4;
der Schurtest liefert dort den schärferen Formbetrag

\[
|\langle y,K_Ay\rangle|\le2r(1/4-47/500)\|y\|^2
=234/625\,\|y\|^2.
\tag{6}
\]

Mit pi<22/7 und γ<H8192−13log2<5773/10000 folgt
log(2πA)+γ<13/5. Aus (4) und (6) folgt für alle rohen Formvektoren
mit Graden mindestens N≥2

\[
q_A[y]\ge(H_N-14811/2500)\|y\|^2,
\quad14811/2500=13/5+234/625+59/20.
\tag{7}
\]

Für Parität p=0,1 sei m_p=cosh(Ax/2) bzw. sinh(Ax/2) und
M_py=y−e_p⟨m_p,y⟩/⟨m_p,e_p⟩ auf e_p⊥. Auf rohen hohen Graden
N+p,N+p+2,... beträgt die vollständige Korrekturoperatornorm höchstens

\[
\epsilon_{p,N}=\frac{z_0^{N+p}}{(N+p)!\,[1-z_0^2/((N+p+1)(N+p+2))]}
\begin{cases}1&p=0,\\4&p=1.\end{cases}
\tag{8}
\]

Begründung: Orthogonalität annulliert alle niedrigeren Taylorgrade der
Momentfunktion; die verbleibende Reihe hat den angegebenen geometrischen
Fakultätsrest. Der gerade Nenner ist ≥1, der ungerade ≥(A/2)/sqrt3 und
sein Kehrwert <4, weil A>1.

||Ve_p||<2 folgt wie zuvor aus V≤−log(1−x)/2 und ||V||²≤1/2.
Mit (5), (6) auf dem ganzen Raum und dem Konstantenbound gilt

\[
|q_A(y,e_p)|<7\|y\|,\qquad\|Q_Ae_p\|<11.
\]

D_H- und q0-Mischterme verschwinden durch Orthogonalität. Daher

\[
q_A[M_py]\ge(H_N-14811/2500-14\epsilon-11\epsilon^2)\|y\|^2,
\quad\|M_py\|^2\le(1+\epsilon^2)\|y\|^2.
\tag{9}
\]

Für N=572 ist H572>6927/1000 und beide ε<10^−6. Exakt gilt
6927/1000−14811/2500−14·10^−6−11·10^−12>1+10^−12. Somit

\[
\boxed{q_A[u]\ge\|u\|^2\quad\hbox{auf dem vollständigen hohen Raum}.}
\tag{10}
\]

Zusätzlich geprüfte Schnitte: N=410 mit δ=2/3 (204 niedrige Koordinaten),
N=484 mit δ=5/6 (241). Gewählt ist N=572 mit δ=1 (285 Koordinaten).
Eine notwendige minimale Dimension wird nicht behauptet.

## 4. Vollständigkeit und exakte Kodimension

Das allgemeine Wandpaket beweist auf jedem endlichen Horizont

\[
\mathcal F_A=\{u:\int(1+g)|\widehat u|^2<\infty,
\ \operatorname{supp}u\subset[-A,A],\ E_+u=E_-u=0\}.
\]

Insbesondere s_A<13 und q_A+17||.||² ist zur vollen Gamma-Norm äquivalent.
Die Dichte erfolgt durch Trägerschrumpfung, zwei glatte Momentkorrekturen
und Faltung; die Gamma-Reihe kontrolliert die Dilatationen und die
Faltung erhält die Nullmomente. Die konkrete Abschlussargumentation steht
bytegleich in inputs/GENERAL_WALL_PROOF.md §3 und inputs/A9_PROOF.md §5.
Sie gilt auf dem hier neu kontrollierten endlichen Horizont unverändert.

D_H und V sind nichtnegative geschlossene Formanteile, K und S beschränkt;
die physische Integralidentität erstreckt sich durch Formabschluss.
Nullfortgesetzte Polynome gehören zur Formdomäne: Ihre L²-Translations-
inkremente haben Normquadrat O(min(t,1)); der Gamma-Kern ist nahe Null
O(1/t), im Fernbereich integrierbar. Qe_n ist ebenfalls L².

Die niedrigen Indizes sind {2,4,...,570} und {3,5,...,571}, jeweils 285.
Diese stetigen L²-Koordinaten sind auf F_A^p surjektiv, weil die Vertreter
M_pe_n die Einheits-Koordinatenmatrix besitzen. Ihr abgeschlossener Kern
hat daher genau Kodimension 285. Jeder Vektor im Kern ist eindeutig M_py
mit rohen Graden mindestens 572 bzw. 573. Endliche Subtraktion von e_p
erhält die Formdomäne. Damit gilt (10) auf dem gesamten unendlichen Kern.

Der allgemeine q9-Satz gibt ||T_Au||²≥36/355||u||² und ||D_Au||²≤13||u||²,
also T als Isomorphismus auf seinen vollständigen geschlossenen Carrier.
Aus (10) folgt im hohen T-Bild G_A≥1/14. Dieser Raum ist abgeschlossen
und hat ebenfalls Kodimension 285. Der tatsächliche Defekt-Schurrest
I−α−β*(I−K)^−1β enthält die gesamte hohe Antwort.

## 5. Vollständige physische Schur-Untergrenze und neues Fehlerbudget

Die vollständige Mellinkorrektur erfüllt ||M_p||≤2: Für z≤3/5 genügen
cosh(z)−1 bzw. z²/[3(1−z²/20)] als Quotientenbounds der orthogonalen
Momentanteile; jeweils 1 plus deren Quadrat ist kleiner als 4.

Schreibe u=U_A^−1 M_p(Ec+y), L=E*M_p*Q_A M_pE und
B=E*M_p*Q_A M_p|_Y. Dann ist B in der hohen L²-Norm beschränkt und

\[
q_A[u]\ge c^*Lc+2\operatorname{Re}\langle c,By\rangle+\|y\|^2.
\tag{11}
\]

Das Gamma-Modellpolynom vom Grad M=416 wird aus den exakten inversen
Reihen von cosh z und sinh(z)/z gebildet. Die endlichen Residuen und die
Fakultätsreste werden auf r=6/5 neu ausgewertet. Das sinh-Residuum wird
vor der Majorisierung durch z dividiert. Beide Nenner sind ≥1.
Sei ε_K der exakte rationale Kernelbound in CHECK_RESULTS.json und
γ_K=(12/5)ε_K der Operatorbound. Setze Q^P als entsprechende Modellform,
L0=E*M_p*Q^P M_pE, B0=E*M_p*Q^P|_Y und G0=B0B0*. Dann

\[
\|L-L_0\|\le e_L=4\gamma_K,\qquad
\|B-B_0\|\le e_{B,p}=2\gamma_K+22\epsilon_{p,572}.
\tag{12}
\]

Der Faktor 22 bezahlt ||M||·||Qe_p|| für die hohe Momentkorrektur.
Alle niedrigen Momente und Integrale werden in gerichteten Intervallen
neu eingeschlossen. Young mit τ=1/1000 liefert

\[
BB^*\preceq H^{up}=\tfrac{1001}{1000}G_0+1001e_B^2I,
\qquad F=L_0-e_LI-H^{up}.
\tag{13}
\]

Eine strikt positive gerichtete LDL-Zerlegung von F liefert
σ=1/tr(F^−1)>0 als unteren Eigenwertbound. Mit b²=tr(Hup) als oberem
Kopplungsnormquadrat ergibt die vollständige Schurquadratergänzung

\[
q_A[u]\ge c_{phys}\|u\|^2,\qquad
c_{phys}=\frac{\min(\sigma,1)}{4(1+b)^2}>0,\qquad
G_A\succeq\frac{c_{phys}}{c_{phys}+13}I.
\tag{14}
\]

Hier wird ||u||≤2||(c,y)|| und die inverse Scherabbildung mit Norm ≤1+b
bezahlt. Der vollständige hohe Operator hat eine beschränkte Inverse
dank (10); dieselbe Abschätzung gilt daher für die tatsächliche
Graph-Schur-Elimination. Die detaillierte Identifikation mit dem
Defekt-Schurrest steht in inputs/A9_SCHUR_AND_TRANSPORT.md; dort werden
δ und ||Qe_p|| durch die hier neu bewiesenen Werte ersetzt.

### Vollständige Gram-Berechnung

Die Engine benötigt rohe Grade 0,...,571. Der Gamma-Modellsupport reicht
bis höchstens 571+416+1=988. Nur dieser polynomiale Anteil hat endlichen
Support. G0 wird aus den ganzen V²-, S²-, VS/SV- und Gamma-Kreuzintegralen
mit Parseval-Abzug aller niedrigen rohen Grade gebildet. V² wird analytisch
integriert. Alle Shiftintegrale sind Polynom-Gaussintegrale auf den acht
Zellen (3), alle logarithmischen Kreuzintegrale benutzen exakte Primitive.
Es wird keine endliche hohe Modentrunkierung als vollständige Antwort benutzt.

Die neuen exakten Shiftrelationen sind d4=2d2, d8=3d2, d9=2d3.
Die frühere Relation d3=1 gilt hier nicht. Ein eigener Aufbau bei N=15,
M=16 vergleicht die zusammengesetzte Engine mit direkter Integration der
vollständigen Modellfunktionen vor dem Parseval-Abzug.

## 6. Bedingter positiver Abschluss über beide Wände

Erst positive Ergebnisse in beiden Paritäten von (13) ergeben den gemeinsamen
Terminalboden c>0. Die bereits bewiesene Formnaturality der physischen
Nullfortsetzung überträgt ihn auf alle 1≤A≤A11. Mit s_A<13 folgt dort
G_A≥c/(c+13)I. Das allgemeine Wandlemma liefert dann

\[
U^X_{A,B}=G_B^{1/2}M^T_{A,B}G_A^{-1/2}
\]

als isometrische Einbettungen mit Cocycle für alle 1≤A≤B≤C≤A11,
einschließlich der q8- und q9-Wand. Dies bleibt ein endlicher Horizont.
Externe analytische Abnahme, unbeschränkte positive Fortsetzung,
vollständiges Objekt X und globale Weil-/RH-Aussagen bleiben offen.

Die gemeinsame Abschätzung (1)–(2) ist allgemein. Ihr numerisch günstiger
Wert 59/20 ist bisher nur für den hier gebundenen Horizont bewiesen.
Eine beliebig oft erneuerbare Terminalreserve folgt daraus nicht.
