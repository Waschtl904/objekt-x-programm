# O8 bei A₈: Formraum, vollständige Kopplung und gerichtete Untermatrix

**Lokale mathematische Herleitung. Externe analytische Prüfung offen.**

Endpunkt A=A₈=log(8)/2. Kanäle {2,3,4,5,7}; q=8 bleibt inaktiv. Physische Nullfortsetzung, feste Fourierkonvention und die ursprünglichen beiden Mellinbedingungen bleiben erhalten. Die Rechnungen beziehen sich auf die konkrete C1a-Fortführung aus O1–O7. Die nachfolgende Herleitung und der gerichtete Rechner sind getrennte Bestandteile des Nachweises.

## 1. Anbindung des vollständigen Formraums

Auf dem gemeinsamen Fourier-Raum sei 𝒢 die Gamma-Formdomäne mit Norm ∫(1+g)|û|². In der ersten Kammer ist b=g−κ−2c+17 äquivalent zu 1+g: s=κ+2ω<23/2, also b≥g+17−s>g+5 und b≤g+17+s. Die O1–O7-Vervollständigung F_A der tatsächlichen Zwei-Mellin-H¹₀-Quellen hat daher dieselbe Topologie wie der entsprechende Gamma-Abschluss.

Die Identifikation

\[
F_A=\{u\in\mathcal G:\operatorname{supp}u\subset[-A,A],\ E_+u=E_-u=0\}
\tag{1}
\]

wird hier für jedes A∈[1,A₈] begründet. Die rechte Seite ist wegen L²-Stetigkeit der Momente auf dem festen kompakten Träger und L²-Abgeschlossenheit der Trägerbedingung geschlossen. Für die Dichte:

1. Schrumpfe u durch u_r(x)=r⁻¹ᐟ²u(x/r), r<1. Nach Fouriertransformation ist die Gamma-Norm durch g(ξ/r) kontrolliert. Jeder Summand der Gamma-Reihe erfüllt g(tξ)≤max(1,t²)g(ξ). Dilatationen nahe r=1 sind deshalb gleichmäßig beschränkt auf 𝒢. Auf Funktionen mit glatter kompakter Fouriertransformierter konvergieren sie stark; deren Dichte in L²((1+g)dξ) erweitert diese Konvergenz auf ganz 𝒢.
2. Die Momentfehler von u_r gehen gegen null, denn alle Träger liegen in [-A,A]. Wähle zwei feste glatte Innenfunktionen mit invertierbarer E_±-Matrix und ziehe die entsprechenden, gegen null gehenden Korrekturen ab. Solche Funktionen erhält man aus zwei kleinen verschobenen Kopien derselben glatten positiven Funktion an verschiedenen inneren Punkten: ihre Exponentialmomente haben verschiedene Quotienten. In einer festen Parität genügt eine gerade bzw. ungerade Innenfunktion mit nichtverschwindendem verbleibendem Moment.
3. Falte anschließend mit einem glatten kompakten geraden Mollifier von hinreichend kleinem Träger. Die Quelle bleibt strikt im Intervallinneren und in ihrer Parität. Beide Nullmomente bleiben wegen E_±(u*ρ)=E_±(u)E_±(ρ) exakt null. Die Gamma-Konvergenz folgt aus Fourier-Dominanz und der gleichmäßig beschränkten Fouriertransformation des Mollifiers.

Damit liefert (1) genau den Abschluss tatsächlicher glatter Quellen; zusätzliche Randbedingungen werden nicht eingeführt.

Mit U_Au(x)=√(2A)u(Ax) wird die allgemeine, skalierte Form zu

\[
Q=D_H+V+q_0I-K_A-S_A,
\quad H=L^2((-1,1),dx/2),
\]
\[
D_HP_n=H_nP_n,\quad V=-\tfrac12\log(1-x^2),
\quad q_0=-\log(2\pi A)-\gamma.
\tag{2}
\]

Vor der Momentkorrektur verwenden wir dieselbe Form ohne Polterme auf dem noch nicht durch Mellinbedingungen eingeschränkten Raum. Die allgemeine Gamma-Zerlegung liefert (2) auch auf der geschlossenen Formdomäne: der singuläre Differenzanteil und der Randpotentialanteil sind nichtnegative Formen, der reguläre Gamma- und Prime-Anteil sind beschränkt. Die Integralzerlegung erstreckt sich durch Tonelli bzw. Formabschluss; die Legendre-Diagonalisierung des singulären Anteils ist diejenige der verwendeten universellen Formidentität. Es wird keine Konvergenz einer unkontrollierten endlichen Tail-Summe vorausgesetzt.

Nullfortgesetzte Polynome haben endliche Gamma-Energie, da ‖τ_ru−u‖²=O(min(r,1)). Das Produkt mit dem Gamma-Kern O(1/r) ist nahe null integrierbar; bei unendlich fällt der Kern exponentiell ab. Momentkorrigierte Polynome gehören nach (1) zu F_A, auch wenn sie selbst keine klassischen H¹₀-Randspuren besitzen.

## 2. Vollständige Koordinaten und hohe Reserve

Fixiere p=0 oder p=1, e_n=√(2n+1)P_n und e=e_p. Setze

\[
m_0(x)=\cosh(Ax/2),\quad m_1(x)=\sinh(Ax/2),
\quad Mx=x-e\frac{\langle m_p,x\rangle}{\langle m_p,e\rangle}
\quad(x\perp e).
\]

Die Paarung ist im zweiten Argument linear. Die Mellinbedingungen reduzieren sich durch Parität auf genau dieses eine nichtautomatische Moment.

Sei E:ℂ¹⁹¹→H die isometrische Einbettung in die Grade 2,4,…,382 bzw. 3,5,…,383; Y ist der rohe hohe Raum ab Grad 384 bzw. 385, jeweils geschnitten mit der Formdomäne. Dann hat jede zulässige Quelle eindeutig die Darstellung

\[
u=U_A^{-1}M(Ec+y),\qquad y\in Y.
\tag{3}
\]

Tatsächlich werden nur der Momentträger und die endlich vielen niedrigen Legendrekomponenten entfernt. Alle entfernten Polynome liegen in der Formdomäne; der Rest bleibt darin. Die Mellinbedingung bestimmt den Trägerkoeffizienten eindeutig. Die Vertreter MEe_j haben die Identität als niedrige Koordinatenmatrix. Somit ist der gemeinsame Kern der 191 niedrigen Koordinaten abgeschlossen und hat genau Kodimension 191. Er besteht aus allen M(Y), nicht aus einer endlichen oder zusätzlich randbeschränkten Teilklasse.

Der neue [Tail-Entwurf](../o8-vorbereitung/O8_ANALYSE.md), §§2.2–2.5, liefert auf diesem gesamten Raum

\[
q_A[U_A^{-1}My]\ge\tfrac12\|My\|^2\ge\tfrac12\|y\|^2.
\tag{4}
\]

Die zweite Ungleichung folgt aus y⊥e. Zur Einordnung: die physische hohe Reserve 1/2 entspricht der hohen T-Reserve 1/24; beide sind von einer noch zu berechnenden vollen Terminalreserve zu unterscheiden.

Für die spätere Normumrechnung gilt auf ganz e⊥, nicht nur auf dem niedrigen Block, ‖M‖≤μ=2. Denn bei z=A/2≤21/40 ist im geraden Sektor der Quotient der orthogonalen Momentkomponente durch das Trägermoment höchstens cosh(z)−1. Im ungeraden Sektor ist er höchstens

\[
\frac{\sqrt3}{z}(\sinh z-z)
\le\frac{z^2}{3(1-z^2/20)}.
\]

Hier wurden √3<2, das Trägermoment ≥z/√3 und die geometrische Majorante des sinh-Restes benutzt. In beiden Fällen ist 1 plus das Quadrat dieses Quotienten kleiner als 4. Diese rationalen Vergleiche werden im Reservechecker ausgeführt.

## 3. Tatsächliche und modellierte Kopplung

Schreibe Z=ME und definiere den tatsächlichen niedrigen Block L=Z*QZ und B:Y→ℂ¹⁹¹ durch die vollständige Formkopplung zwischen Zc und My. Die Polynome Zc liegen in der Operatordomäne des auf sie angewendeten Ausdrucks Q: VZc∈L², D_HZc ist endlich und die übrigen Terme sind beschränkt. Daher besitzt die Kopplung eine L²-beschränkte Darstellung. Mit (4) gilt

\[
q_A[u]\ge c^*Lc+2\operatorname{Re}\langle c,By\rangle+\tfrac12\|y\|^2.
\tag{5}
\]

Sei K^P_A der Grad-M-Polynomkern aus der neuen Gamma-Restabschätzung, und Q^P der entsprechende Formoperator. Die Engine bildet

\[
L_0=Z^*Q^PZ,\qquad B_0=Z^*Q^P|_Y,
\qquad G_0=B_0B_0^*.
\tag{6}
\]

M ist in L₀ und links in B₀ bereits exakt enthalten; alle niedrigen Mellinmomente werden mit einschließenden Arb-Reihen samt Rest berechnet. Die hohe Momentkorrektur rechts in B wird anschließend ausdrücklich bezahlt. Eine Gleichsetzung von B und B₀ findet nicht statt.

### Warum G₀ die unendliche Antwort enthält

Mit C=V−K^P_A−S_A und P_Z der Projektion auf alle rohen Grade bis 383 gilt

\[
G_0=Z^*C(I-P_Z)CZ.
\]

Die Engine berechnet den gesamten Gram von V−S durch die exakten Integrale V², S², VS und SV, und zieht ausschließlich die niedrige Projektion ab. S² enthält alle gemischten Prime-Kanäle und beide Translationsrichtungen. Die Gamma-Ergänzungen enthalten die vollständigen K^P/K^P-, V/K^P- und S/K^P-Terme. D_H+q₀ trägt zur Low/High-Kopplung nichts bei, weil es diagonal ist und Z im rohen niedrigen Raum liegt.

Nur K^P_AP_i besitzt endlichen Legendre-Support bis N+M+1=544 für N=383,M=160. Der V-/Shift-Rest wird durch vollständige Integrale und Parseval erfasst. Der Rest des wirklichen Gamma-Kerns wird durch die unten bewiesene Operatorfehlerschranke bezahlt. Grad 544 ist daher kein Abbruch der wirklichen hohen Antwort.

Am Endpunkt werden d₂=2/3 und d₄=4/3 algebraisch eingesetzt. Die gemeinsame positive Zellgrenze x=1/3 wird einmal angelegt; die übrigen Grenzen werden mit gerichteten Vergleichen geordnet. Dadurch entstehen fünf positive Halbraumzellen. Die Parität rekonstruiert die andere Hälfte der Integrale mit der Normierung dx/2.

## 4. Vollständige Fehlerweitergabe

Die neue rationale Gamma-Rechnung liefert |k_reg(t)−p(t/2)|≤ε auf 0≤t/2≤21/20. Der Schurtest ergibt

\[
\|K_A-K^P_A\|\le\gamma_K:=\frac{21}{10}\epsilon.
\]

Mit μ=2 folgt unmittelbar

\[
\|L-L_0\|\le e_L:=4\gamma_K.
\tag{7}
\]

Sei ε_p die bereits hergeleitete hohe Momentkorrektur: für n=384+p und z₀=21/40

\[
\epsilon_p=\frac{z_0^n}{n!\,[1-z_0^2/((n+1)(n+2))]}
\times\begin{cases}1&p=0,\\4&p=1.\end{cases}
\]

Sie begrenzt ‖M|_Y−I_Y‖. Für den normierten Träger e gilt

\[
\|Qe\|\le H_p+|q_0|+\|Ve\|+\|K_A\|+\|S_A\|
<1+\tfrac52+4+\tfrac{21}{40}+\tfrac{63}{20}<12.
\]

Damit lässt sich die Differenz der vollständigen Kopplungen exakt zerlegen in

\[
B-B_0=Z^*(Q-Q^P)|_Y+Z^*Q(M|_Y-I_Y),
\]

und daher

\[
\boxed{\|B-B_0\|\le e_{B,p}:=2\gamma_K+24\epsilon_p.}
\tag{8}
\]

In (8) sind die Gamma-Abweichung und die hohe Mellin-Korrektur getrennt begründet; der zweite Term benutzt den tatsächlichen Q-Träger, sodass kein Gamma/Moment-Kreuzterm fehlt. Niedrige Momentintervalle, Logarithmen, Integrale und Arithmetikfehler sind bereits in den gespeicherten Matrixintervallen enthalten.

Für τ=1/1000 gilt als Operatorungleichung

\[
BB^*\preceq(1+\tau)G_0+(1+\tau^{-1})e_{B,p}^2I
=\frac{1001}{1000}G_0+1001e_{B,p}^2I=:H_p^{\rm up}.
\tag{9}
\]

Dies folgt aus dem Quadrat von B=B₀+(B−B₀) und dem gewichteten Cauchy–Schwarz- beziehungsweise Young-Schritt. Es ist eine obere Gram-Abschätzung, keine Behauptung über einzelne Vorzeichen der Gram-Einträge.

Die vollständig bezahlte hinreichende Untermatrix lautet also

\[
\boxed{F_p=L_0-e_LI-2\left(\frac{1001}{1000}G_0+1001e_{B,p}^2I\right).}
\tag{10}
\]

Jeder tatsächliche Wert der modellierten Matrixeinträge liegt in den gespeicherten Intervallen. Die gerichtete LDL-Rechnung behandelt diese Unsicherheit vollständig. Die Matrix F_p liegt unter L−2BB*, unabhängig davon, ob sie selbst positiv ist.

## 5. Reservecheck und Normumrechnung

Falls alle gerichteten LDL-Pivots von F_p strikt positiv sind, ist F_p positiv definit. Für F_p=LDL* mit unterem Dreiecksfaktor L und Einsen auf dessen Diagonale ist

\[
\operatorname{tr}(F_p^{-1})=\sum_{i,k}|(L^{-1})_{ik}|^2/D_{ii},
\qquad \sigma_p:=1/\operatorname{tr}(F_p^{-1})>0
\]

ein zulässiger unterer Eigenwertboden. Die Rückrechnung erfolgt wiederum mit Intervallen. Die tatsächliche Matrix genügt dann L−2BB*≥σ_pI. Quadratische Ergänzung in (5) gibt

\[
q_A[u]\ge\sigma_p\|c\|^2+\tfrac12\|y+2B^*c\|^2.
\]

Mit b_p²≥‖B‖², beispielsweise b_p²=tr(H_p^up), und μ=2 folgt

\[
c_{{\rm phys},p}=\frac{\min(\sigma_p,1/2)}{4(1+2b_p)^2}>0,
\qquad q_A[u]\ge c_{{\rm phys},p}\|u\|_2^2.
\tag{11}
\]

Dabei wirkt die Dreieckstransformation auf ℂ¹⁹¹⊕Y; ‖u‖≤μ‖(c,y)‖ folgt direkt aus (3). Die niedrigen physischen Legendrekoordinaten werden an keiner Stelle als orthonormale niedrige T-Koordinaten behandelt.

Aus den etablierten Kammeridentitäten ‖D_Au‖²≤s‖u‖², s<23/2 und ‖T_Au‖²=q_A[u]+‖D_Au‖² folgt schließlich

\[
\boxed{\eta_{A,p}\ge\frac{c_{{\rm phys},p}}{c_{{\rm phys},p}+23/2}>0.}
\tag{12}
\]

T_A:F_A→H_A^T ist nach O5–O7 surjektiv und beschränkt invertierbar. Daher gilt (12) auf dem gesamten geschlossenen Terminalraum. Das Minimum der beiden Paritätsreserven ist ein gemeinsamer Boden. Für kleinere Terminals innerhalb der Kammer liefert die rohe isometrische Kompressionsidentität denselben Boden. O9 und das Wall-Crossing O10 werden dadurch nicht als eigene Konstruktionen erledigt.

Falls (10) nicht positiv zertifiziert werden kann, folgt keine negative tatsächliche Terminalquelle. Dann muss die hohe Eliminationsschranke oder der konkrete Rechenansatz geschärft werden.

## 6. Prüfrollen und Status

`generate_a8.py` erzeugt beide 191×191-L₀-/G₀-Intervallmatrizen. `check_a8.py` liest die tatsächlich gespeicherten Intervalle erneut ein, rekonstruiert ε, e_L und e_B, bildet (10) und prüft die Reserven. `check_normalization_a8.py` prüft am kleinen Modell N=15,M=16 die neue Endpunktskalierung und setzt den vollständigen Gram unabhängig durch Integration der gesamten Modellfunktionen mit anschließender Parseval-Subtraktion zusammen. Diese kleine Rechnung ersetzt keinen 191D-Reservecheck.

Die analytischen Aussagen über den Formraum, die universelle Formidentität, die vollständige Gram-Darstellung und (7)–(12) sind die Voraussetzung für die Bedeutung eines Rechner-PASS. Ein Rechenerfolg allein bewirkt keine Registry-Promotion. Die externen Reviewstatus der geerbten Belege bleiben unverändert. Es wurden weder GitHub-Schreibzugriffe noch CI-Läufe gestartet.

## 7. Gezielte Verschärfung nach dem ersten Reservecheck

Die Untermatrix (10) mit physischer hoher Reserve δ=1/2 wurde tatsächlich geprüft. Der gerade Sektor hat 189 positive Pivots vor einem strikt negativen Pivot, der ungerade 190. Das ist ein negativer Befund für diese hinreichende Untermatrix, nicht für die tatsächliche Terminalform. Diese ursprünglichen Ergebnisse bleiben in `reserve_results.json` erhalten; der zugehörige ursprüngliche Checker in `check_a8_half.py`.

Die danach vorgenommene Änderung betrifft ausschließlich die analytische hohe Reserve. Die gleichen L₀-/G₀-Matrizen, der gleiche Gamma-Grad und das gleiche Fehlerbudget werden weiterverwendet.

### 7.1 Neuer vollständiger physischer Floor 2/3

Setze r=26/25. Rationale Logarithmuszeugen bestätigen A₈<r. Mit S(z)=sinh(z)/z und

\[
\frac{S(z)-1}{z^2}\le b:=\sum_{k=0}^{\infty}\frac{r^{2k}}{(2k+3)!}
\]

gilt für 0<z≤r

\[
\frac1z-\operatorname{csch}z
=\frac{S(z)-1}{zS(z)}
\le\frac{zb}{1+z^2/6}
\le\frac{rb}{1+r^2/6}.
\]

Die letzte Ungleichung folgt aus r²<6. Eine obere Taylor-Einschließung C_r von cosh(r) und eine obere Einschließung von b liefern daher

\[
k_{\rm reg}(2z)\ge\frac14\left(C_r^{-1}-\frac{rb}{1+r^2/6}\right)
>\frac{59}{500}.
\]

Die Einschließung von b verwendet 21 Summanden und den expliziten positiven Rest

\[
\frac{r^{42}}{45!\,[1-r^2/(46\cdot47)]}.
\]

Dieser Grenzwert gilt zusammen mit k_reg(0)=1/4 auf dem ganzen benötigten Intervall. Es wird keine nur numerisch getestete Monotonie von k_reg benutzt.

Weitere rationale Zeugen aus `refine_tail.py`:

\[
\gamma<H_{8192}-13\log2<\frac{5773}{10000},\quad
-q_0(A)<\frac{491}{200},\quad
\|S_A\|<\frac{313}{100},\quad
H_{384}>\frac{6529}{1000}.
\]

Die Shift-Schranke verwendet dieselbe analytische Dreierkettenzerlegung für q=2 wie zuvor; nur die skalaren Logarithmus-/Wurzelzeugen werden schärfer ausgewertet. Für q₀ werden π<22/7 und A≤26/25 eingesetzt.

Nach Entfernung des konstanten Gamma-Kerns auf dem rohen hohen Raum bleibt dessen Verlust höchstens

\[
2r\left(\frac14-\frac{59}{500}\right)=\frac{858}{3125}.
\]

Der rohe hohe Floor ist damit größer als

\[
\frac{6529}{1000}-\frac{491}{200}-\frac{858}{3125}-\frac{313}{100}
=\frac{2092}{3125}=0.66944.
\]

Die Faktoren 8 und 12 für die Misch- bzw. Momentträgerabschätzung gelten weiterhin. Mit dem bisherigen sicheren ε=10⁻⁶ gilt exakt

\[
\frac{2092}{3125}-16\epsilon-12\epsilon^2
>\frac23(1+\epsilon^2).
\]

Somit gilt auf dem bereits identifizierten **vollständigen** hohen Raum

\[
\boxed{q_A[U_A^{-1}My]\ge\frac23\|My\|^2\ge\frac23\|y\|^2.}
\tag{13}
\]

Die zugehörige hohe T-Defektreserve wäre 4/73. Der folgende physische Check verwendet ausdrücklich δ=2/3. Alle elf zusätzlichen rationalen Vergleiche bestehen; ein Formraum- oder Kodimensionswechsel findet nicht statt.

### 7.2 Gerichtete Matrix und volle Reserve

Mit unverändertem H_p^up aus (9) wird statt (10) jetzt geprüft:

\[
\boxed{F_{p,\delta}=L_0-e_LI-\delta^{-1}H_p^{\rm up},\qquad\delta=2/3.}
\tag{14}
\]

Die Normumrechnung wird entsprechend geändert zu

\[
c_{{\rm phys},p}=\frac{\min(\sigma_p,\delta)}{4(1+b_p/\delta)^2},
\qquad\eta_{A,p}\ge\frac{c_{{\rm phys},p}}{c_{{\rm phys},p}+23/2}.
\tag{15}
\]

`reserve_refined.json` dokumentiert jeweils **191 strikt positive gerichtete LDL-Pivots**. Die angezeigten Werte sind Näherungsdarstellungen der dort gespeicherten gerichteten Intervalle:

| Parität | Physischer Reserveboden aus (15) | Defektreserveboden aus (15) |
|---|---:|---:|
| Gerade | 1,23256343485·10⁻²⁹ | 1,07179429117·10⁻³⁰ |
| Ungerade | 8,61066526013·10⁻²⁷ | 7,48753500881·10⁻²⁸ |

Ein gemeinsamer rationaler physischer Boden ist c_phys=12/10³⁰. Daraus folgt

\[
\eta_A\ge\frac{24}{23\cdot10^{30}+24}>10^{-30}.
\]

Diese gemeinsame Abrundung wird in `common_reserve.json` anhand der unteren Endpunkte der gespeicherten Intervalle nochmals ausschließlich rational geprüft. Die Schlussfolgerung ist ein lokaler autorenseitiger O8-Nachweis relativ zu den benannten analytischen Eingaben und der hier ausgeführten Herleitung. Ein unabhängiger analytischer Review und eine etwaige Repository-Statusänderung sind damit nicht behauptet.
