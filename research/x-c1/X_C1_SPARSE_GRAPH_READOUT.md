# X-C1-SPARSE-GRAPH — positiver Teilmediator und explizite Isometrien

**Datum:** 16. September 2026. **Spur:** Draft PR #137.
**Eingangsanker:** `708542fb8a6a230b2e1ae4b8d44d51a7aa1e393d`.
**Status:** analytische Autorenherleitung; externe Prüfung OFFEN; keine Neuheitsbehauptung.

## 0. Ergebnis und feste Reichweite

Es wird ein tatsächlich definierter positiver Readout auf einer **unendlichdimensionalen, aber trägerbeschränkten** Teilklasse konstruiert. Er gilt nicht nur für skalare Linearkombinationen eines Bumps. Für sechs unten festgelegte Intervalle und jede nichtleere Teilvereinigung S gilt

```math
Q_W[u]=\|C_S T_a^0u\|_{\mathcal K_S}^2
\ge\frac1{25}\|u\|_2^2
\qquad
\left(u\in H^1_0(S),\ E_+(u)=E_-(u)=0\right).       \tag{SG0}
```

Für glatte Quellen ist Q_W die vorhandene Weil-Form. Auf H1 wird ihre bekannte kontinuierliche Formfortsetzung benutzt. Das Quellenfenster I_a muss S enthalten. Die Momente werden nur GLOBAL verlangt, nicht separat in jedem Intervall. S wird pro Raum festgelegt, nicht pro Testfunktion nachoptimiert.

Der Readout ist die gemeinsame Differenzabbildung `u -> (u(x)-u(y),u(x))` in einem vorwärts definierten gewichteten Kanten-/Knotenraum. Kein Matrix-/Operatorquadratwurzelverfahren, keine GNS-Norm und kein angepasster Koeffizient werden benutzt. Isometrische Verbindungsabbildungen für S subset T werden ausdrücklich auf den gesamten Zielräumen angegeben und erfüllen ein exaktes Kokzyklusgesetz.

**Nicht erreicht:** voller C1-GEOM auf W_a, beliebige Träger, eine beliebig lange dyadische Kette oder Objekt X/RH. Die Zahl sechs benennt die hier bewiesene ausreichende Geometrie, keine behauptete optimale oder fundamentale Grenze. A1, die C0-Dateien, C1-STORAGE und ENDPOINT-GREEN werden weder verändert noch erneut geprüft. Keine Registry-Promotion, kein Merge, kein CI-green-Anspruch.

## 1. Importierte Form und gemeinsame Kanten

Die festgelegten Daten bleiben

```math
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},\quad
w_n=\frac{\Lambda(n)}{\sqrt n},\quad t_n=\log n,
\qquad\kappa_* =\log(8\pi)+\gamma+\frac\pi2.
```

Auf NULLPOL gilt nach der vorhandenen COMMON-JUMP-Identität

```math
Q_W[u]=\int_0^\infty h(t)\|K_tu\|_2^2dt
-\kappa_*\|u\|_2^2
-2\operatorname{Re}\sum_n w_n
 \int u(x-t_n)\overline{u(x)}dx.                    \tag{SG1}
```

Die Primzahlsumme ist hier exakt endlich: Es tragen nur Verschiebungen bis zum Durchmesser des kompakten Quellenträgers bei. Größere Verschiebungen haben null Korrelation. Es werden weder zwei divergente Normen subtrahiert noch unendliche Prime-/Continuum-Speicher getrennt kritisch verstärkt.

Sei S eine endliche Vereinigung beschränkter offener Intervalle. Orientiere die Kanten durch x>y und setze

```math
\mathcal E_S=\{(x,y)\in S^2:x>y\},\qquad
(D_Su)(x,y)=u(x)-u(y).
```

Auf derselben Kantenmenge definiere ein einziges positives Maß

```math
\nu_S=\nu_{\Gamma,S}+\nu_{P,S},
\qquad d\nu_{\Gamma,S}(x,y)=h(x-y)dxdy,
```

```math
\int F\,d\nu_{P,S}
=\sum_n w_n\int_{S\cap(S+t_n)}F(x,x-t_n)dx.        \tag{SG2}
```

Prime und Gamma lesen somit dieselbe Differenz desselben Quellenfeldes. Das ist keine Identifikation des zeitlichen Verzögerungsgraphen mit dem andersartigen adelischen P11-Tree-Gram.

## 2. Die negative Diagonale wird ausdrücklich bilanziert

Definiere für x in S

```math
W_S(x)=\int_{\mathbb R\setminus S}h(|x-y|)dy,
\qquad d_{P,S}(x)=\sum_nw_n
 \left(1_S(x-t_n)+1_S(x+t_n)\right),
```

```math
\boxed{\rho_S(x)=W_S(x)-\kappa_*-d_{P,S}(x).}      \tag{SG3}
```

W_S ist im Inneren von S endlich; seine logarithmische Randsingularität wird nicht wegdefiniert. Die Summe in d_P ist endlich.

Die Gammaenergie zerfällt nach den Endpunkten ihrer Kanten. Die Kanten zwischen S und seinem Komplement liefern genau W_S|u|². Für jede Primkante gilt

```math
-2\operatorname{Re}(u(x)\overline{u(y)})
=|u(x)-u(y)|^2-|u(x)|^2-|u(y)|^2.
```

Damit folgt auf glatten kompakten Quellen durch Tonelli für die positiven Gammaanteile und endliche Primzahlsummen die **exakte** Identität

```math
\boxed{
q_{\rm NP}[u]=\int_{\mathcal E_S}|D_Su|^2d\nu_S
 +\int_S\rho_S(x)|u(x)|^2dx.
}                                                        \tag{SG4}
```

Hier ist q_NP die rechte Seite von SG1 auch ohne Momentbedingungen. Auf NULLPOL ist q_NP=Q_W; für allgemeine Quellen ist der Polbeitrag nicht automatisch null. Der Faktor 1/2 fehlt in SG4 absichtlich: Jede Kante wird durch x>y genau einmal gezählt.

**Ausreichendes geometrisches Kriterium:** Ist rho_S>=c>0, so definiert

```math
\mathcal K_S=L^2(\mathcal E_S,\nu_S)
 \oplus L^2(S,\rho_S(x)dx),\qquad
\mathcal C_Su=(D_Su,u)                             \tag{SG5}
```

einen positiven Readout, ohne Positivität von Q_W vorauszusetzen. Seine Maße wurden vor der Normidentität aus h, w_n und der Trägermenge angegeben; die Positivität von rho wird nachfolgend unabhängig nachgewiesen.

## 3. Die neue sechsintervallige Klasse enthält den alten Witness unverändert

Setze

```math
\ell=\log2,\quad\varepsilon=1/100,\quad\delta=2\varepsilon=1/50,
\qquad I_j=((j-1/2)\ell-\varepsilon,(j-1/2)\ell+\varepsilon),
\quad j=0,\ldots,5.
```

Für jede nichtleere Menge A subset {0,...,5} setze S_A=union_{j in A} I_j. Es gibt 63 solche Trägermengen; jede zugehörige Quellenklasse ist unendlichdimensional. Die ursprünglichen f und g aus C0 §10.2 sind unverändert in den Abschlüssen von I_0 und I_1 getragen und gehören zu H1_0(S_{0,1}). Die gesamte neue Familie liegt z.B. in I_4=(-4,4). Kleinere passende Quellenfenster bleiben zulässig.

### 3.1 Sämtliche anderen Primzahlen sind exakt ausgeschlossen

Zwischen I_i und I_j liegt die Mittelpunktdifferenz k log2, 1<=k<=5. Eine ganzzahlige Verschiebung log n kann die Intervalle nur verbinden, wenn

```math
|\log n-\log(2^k)|<\delta.
```

Die jeweils nächsten anderen ganzen Zahlen liegen weiter entfernt: Aus log(1+x)>x/(1+x) folgt

```math
\log\frac{2^k+1}{2^k}>\frac1{2^k+1}\ge\frac1{33}>\frac1{50},
\qquad
\log\frac{2^k}{2^k-1}>\frac1{2^k}\ge\frac1{32}>\frac1{50}.
```

Daher bleiben genau n=2^k. Innerhalb eines einzelnen Intervalls gibt es wegen delta<log2 keine Primkante. Dies ist kein numerischer Cutoff und keine Ersetzung der gesamten Arithmetik durch ein dyadisches Modell.

Auf x in I_i ist somit

```math
d_{P,S_A}(x)=\sum_{j\in A,\ j\ne i}
 \frac{\log2}{2^{|i-j|/2}}.                        \tag{SG6}
```

Schreibe hier omega_k:=w_{2^k}=(log2)2^{-k/2}, um k nicht mit dem ganzzahligen Index n in w_n zu verwechseln. Die maximal belasteten Zellen der vollen Sechserkette sind i=2,3 mit Abständen 1,1,2,2,3. Mit log2<7/10 und sqrt2>7/5 folgen die strikten Obergrenzen

```math
(\omega_1,\omega_2,\omega_3,\omega_4,\omega_5)
<(1/2,7/20,1/4,7/40,1/8),\qquad
 d_{P,S_A}(x)<39/20.                              \tag{SG7}
```

### 3.2 Gamma-Leckage nach außen liefert die Reserve

Schreibe H(s)=integral_s^infinity h(t)dt. Weil h positiv und fallend ist, ist H konvex. Für x in einer einzelnen delta-breiten Zelle gilt deshalb

```math
W_{I_i}(x)=H(x-\inf I_i)+H(\sup I_i-x)
\ge2H(\delta/2).
```

Von dieser Leckage müssen beim Hinzufügen anderer Zellen deren Gamma-Verbindungen abgezogen werden. Für j!=i gilt

```math
\int_{I_j}h(|x-y|)dy
\le\delta h(|i-j|\ell-\delta)
<g_{|i-j|},
\qquad g_k:=\delta\left(1+\frac1{2(2k/3-\delta)}\right).  \tag{SG8}
```

Benutzt werden log2>2/3 und h(t)<=1+1/(2t). Die letztere Schranke folgt aus e^(2t)-1>=2t. Die g_k fallen; deshalb ist die größte Gesamtlast höchstens

```math
2g_1+2g_2+g_3
=\frac{1430258}{9458955}.                         \tag{SG9}
```

Die lokale Reserve kann elementar und ohne Quadratur geschätzt werden. Mit

```math
H(s)=\operatorname{atanh}(e^{-s/2})+\arctan(e^{-s/2})
```

folgt

```math
2H(\delta/2)-\kappa_*
=\log\coth(\delta/8)-\log(8\pi)-\gamma
 -2\arctan\tanh(\delta/8)
>\log(175/11)-\gamma-1/200>429/200.                \tag{SG10}
```

Hier wurden coth z>1/z, arctan(tanh z)<z und pi<22/7 verwendet. Die letzten beiden Konstantenbudgets werden exakt rational bewiesen:

```math
\log(175/11)
>2\sum_{r=0}^{14}\frac{(82/93)^{2r+1}}{2r+1}>11/4,
```

```math
\gamma<H_{32}-\log32
<H_{32}-10\sum_{r=0}^{4}\frac{(1/3)^{2r+1}}{2r+1}<3/5.
```

H_32 bezeichnet hier die harmonische Zahl, nicht die Tailfunktion H(s). Der erste Vergleich für gamma folgt aus der fallenden Folge H_n-log n. Die benutzte Logarithmusreihe ergibt sich durch Integration der geometrischen Reihe. Pi<22/7 folgt z.B. aus dem positiven Integral integral_0^1 x^4(1-x)^4/(1+x²)dx=22/7-pi, bereits im vorigen Paket behandelt. Log2<7/10 folgt aus 1+7/10+(7/10)²/2+(7/10)³/6>2.

Aus SG7--SG10 folgt für jede der 63 Mengen und fast jedes x in S_A

```math
\boxed{
\rho_{S_A}(x)>
\frac{429}{200}-\frac{39}{20}-\frac{1430258}{9458955}
=\frac{16569529}{378358200}
=\frac1{25}+\frac{1435201}{378358200}
>\frac1{25}.
}                                                        \tag{SG11}
```

Damit ist das geometrische Kriterium auf einer unendlichdimensionalen Quellenklasse bewiesen; es wurde nicht aus Stichproben-Eigenwerten erschlossen.

## 4. Definitionsbereich, Beschränktheit auf C0 und keine versteckte Wurzel

Für S=S_A ist die maximale Differenzabbildung SG5 auf dem natürlichen Bereich

```math
\mathcal D_S=\{u\in L^2(S):D_Su\in L^2(\nu_S),\quad
 u\in L^2(S,\rho_Sdx)\}
```

als Operator L2(S)->K_S geschlossen. Beweis: Bei u_n->u in L2 und C_Su_n->F wähle eine fast überall konvergente Teilfolge. Auf dem Gamma-Kantenmaß konvergieren die Differenzen außerhalb einer Produkt-Nullmenge; auf jeder der endlich vielen Primgeraden gilt dies nach Translation ebenfalls. Auf dem Knotenmaß gilt derselbe Schluss, da rho endlich fast überall ist. Eine weitere fast überall konvergente Teilfolge der Outputs identifiziert F mit (D_Su,u). Das Argument verwendet keine Punktauswertung als L2-beschränktes Funktional.

Für H1_0(S), mit Nullfortsetzung auf R, ist die Energie endlich: nahe t=0 gilt ||K_tu||<=t||u'||, im Tail ||K_tu||<=2||u||. Die logarithmische Randsingularität ist mit der H1-Spurkontrolle integrierbar. Alternativ liefert SG4 direkt die vorhandene H1-stetige Form.

Die geometrischen Summen erlauben sogar die explizite obere Abschätzung

```math
\|\mathcal C_Su\|^2=q_{NP}[u]
\le\frac7{12}\|u'\|_2^2+\frac{74}{5}\|u\|_2^2.
```

Denn integral_0^1 t²h<=7/12, integral_1^infinity h<3 und sum_{k=1}^5omega_k<7/5; die negative kappa-Diagonale darf für den Oberbound entfallen. Aus der unveränderten C0-Norm folgt

```math
\|C_ST_a^0u\|^2\le\frac{592}{45}\|T_a^0u\|_{\mathfrak M}^2,
\qquad \|C_S\|<4,                                \tag{SG12}
```

auf dem geschlossenen physischen C0-Teilraum

```math
\mathcal K^0_{a,S}=T_a^0
 (H^1_0(S)\cap\ker E_+\cap\ker E_-),
\qquad C_SH:=\mathcal C_S(R_0H).
```

Setze W_S=C_c^infinity(S) intersect ker E_+ intersect ker E_-. Diese glatten momentfreien Quellen sind dort dicht: Man approximiert in H1_0(S) und korrigiert die zwei kleinen Momentfehler mit zwei festen glatten Bumps an verschiedenen Punkten von S; deren 2x2-Momentmatrix ist invertierbar. Hierdurch werden keine Readout-Parameter angepasst.

**Nicht ersetzt:** Die ganze C0-Geometrie bleibt M mit ihren vollständigen Gedächtnisschwänzen. Der Readout benutzt deren Quellenrandspur. Die Green-Potentiale phi=G*u dürfen in Lücken von S ungleich null sein; nirgendwo wird supp phi subset S angenommen.

Auf der tatsächlichen NULLPOL-Klasse folgt nun durch Polarisation

```math
\langle C_ST_a^0u,C_ST_a^0v\rangle_{\mathcal K_S}
=Q_W(u,v).                                       \tag{SG13}
```

Nach ENDPOINT-GREEN, EG6, ist dies zugleich eine positive Faktorisierung der **integrierten** konkreten Randpaarung 2 Re(conj(phi) LB_aL phi) auf genau diesem Teilraum. Eine punktweise positive Residualdichte oder ein nichtnegativer kausaler Original-Gauge-Speicher wird damit nicht behauptet.

## 5. Explizite Isometrien — nicht nur aus einer Normgleichheit postuliert

Seien S=S_A subset T=S_B innerhalb der bewiesenen Familie. Für x in S gilt genau

```math
\rho_S(x)-\rho_T(x)=
\underbrace{\int_{T\setminus S}h(|x-y|)dy}_{b_{\Gamma,S,T}(x)}
+\underbrace{\sum_nw_n[1_{T\setminus S}(x-t_n)
 +1_{T\setminus S}(x+t_n)]}_{b_{P,S,T}(x)}.        \tag{SG14}
```

Die neue Kantenenergie wird also aus derselben alten Knotenreserve bezahlt.

Für ein BELIEBIGES Zielraumelement (F,z) in K_S, nicht nur für ein physisches Bild, definiere J_{S,T}(F,z)=(F_new,z_new) wie folgt:

```math
z_{new}=z\text{ auf }S,\qquad z_{new}=0\text{ auf }T\setminus S,
```

```math
F_{new}(x,y)=\begin{cases}
F(x,y),&x,y\in S,\\
z(x),&x\in S,\ y\in T\setminus S,\\
-z(y),&x\in T\setminus S,\ y\in S,\\
0,&x,y\in T\setminus S,
\end{cases}\qquad x>y.                           \tag{SG15}
```

Die Regel gilt sowohl auf dem kontinuierlichen Gammaanteil als auch auf den Primgeraden desselben Maßes. Sie ist auf Äquivalenzklassen wohldefiniert; die neuen Kantennormen sind durch SG14 und rho_T>=0 kontrolliert. Daher

```math
\|J_{S,T}(F,z)\|_{\mathcal K_T}^2
=\|F\|_{L^2(\nu_S)}^2
 +\int_S(\rho_T+b_\Gamma+b_P)|z|^2dx
=\|(F,z)\|_{\mathcal K_S}^2.                     \tag{SG16}
```

Es werden keine Quadratwurzeln oder inversen Operatoren benötigt: Die Gewichte liegen in den explizit vorgegebenen positiven Maßen.

Die Fallunterscheidung zeigt direkt

```math
J_{T,U}J_{S,T}=J_{S,U},\qquad
J_{S,T}\mathcal C_Su=\mathcal C_T\widetilde u,     \tag{SG17}
```

wobei tilde u die Nullfortsetzung von S nach T ist. Bereits erzeugte Kanten bleiben erhalten; spätere neue Kanten lesen dieselbe alte Knotenspur z.

Für ein festes S ist der äußere Fensterwechsel a->b wörtlich unverändert: T_b^0u=T_a^0u und C_S hat denselben Wert. Kombinierte Fenster-/Trägerinklusionen kommutieren somit mit SG15. Auf den abgeschlossenen erzeugten Räumen K_{X,S}:=closure(C_ST_a^0 W_S) beschränken sich J_{S,T} zu den gewünschten isometrischen Verbindungsabbildungen **dieser Teilklasse**.

## 6. Der eingefrorene Prime-2-Mischtest wird jetzt vom Readout reproduziert

Für die unveränderten f=L b_eps(x+ell/2), g=U_ell f aus dem vorigen Paket gilt auf S_{0,1}, ebenso auf jeder größeren S_A mit {0,1} subset A:

- Der Knoten-Mischterm ist wegen disjunkter Quellenträger null.
- Auf der verbindenden Prime-2-Kante sind die beiden Differenzausgaben -f(y) und g(y+ell)=f(y). Ihre Paarung ist exakt `-(log2/sqrt2)||f||²`.
- Der kontinuierliche Kanten-Mischterm ist `-integral integral h(x-y)f(y)g(x)dxdy=-R_gamma`, mit genau der bereits bewiesenen absolut konvergenten Gamma-Reihe. Der Grundmodus verschwindet, die höheren Moden bleiben.
- Beide Mellinmomente verschwinden, also ebenso die Polpaarung.

Somit liefert **der tatsächlich konstruierte positive Readout**, nicht nur eine Zielmatrix,

```math
\boxed{\langle C_ST_a^0f,C_ST_a^0g\rangle
=-\frac{\log2}{\sqrt2}\|f\|_2^2-R_\gamma.}         \tag{SG18}
```

Normidentität und Polarisation erfassen auch f, g, f+g und f-g. Der bereits bewiesene stärkere 9/20-Bound auf ihrem festen zweidimensionalen Span bleibt unverändert; 1/25 ist der gemeinsame konservative Bound für die wesentlich größere Sechsintervallklasse.

## 7. Die noch fehlende Erweiterung wird nicht durch Sparse-Support verdeckt

SG11 gilt nicht automatisch beim Füllen der Lücken oder Hinzufügen beliebig vieler Zellen. Schon für den vollen Einheitsfensterträger S=(-1,1) ist die hier verwendete Knotenreserve am Mittelpunkt negativ:

```math
\rho_{(-1,1)}(0)=2H(1)-\kappa_*-2\log2/\sqrt2<0.
```

Elementar ist H(1)<16/9 (e^(1/2)>3/2, e²>4) und kappa_*>9/2, also schon 2H(1)-kappa_*<-17/18. Dies widerlegt **nur das hinreichende punktweise Reservekriterium für diesen vollen Träger**, weder Q_W>=0 noch andere Readouts. Die positiven inneren Kanten können eine negative lokale Reserve durchaus kompensieren.

Der nächste sachliche Gate lautet deshalb: Die verbleibende negative Knotenreserve auf größeren Trägern durch die vorhandene innere Differenzenergie kontrollieren und diese Kontrolle in einen positiven, mit SG17 verträglichen Readout überführen. Eine bloße weitere Verkleinerung der Bumps oder der Beweis für einen weiteren endlichen Span schließt diesen Gate nicht.

Insbesondere sind nicht bewiesen: Dichte dieser festen Sparse-Klasse in W_a; Kontrolle beliebiger Kreuzterme zwischen verschieden verschobenen Sparse-Familien; positive Readouts auf der gesamten W_a; radienuniformer NP-GAP; globale Root-CANCEL-FIRST-Admissibilität. Neue Primüberlappungen außerhalb der sechs Zellen dürfen nicht ignoriert werden.

## 8. Ausgeführte Unterstützungstests und Quellen

Der neue eigenständige Standardbibliotheksprüfer `scripts/check_x_c1_sparse_graph.py` wurde lokal ausgeführt und bestand **5229 exakte Checks**: positive rationale Konstantenbudgets, sämtliche 384 Zeilenbudgets der 63 Teilmengen, 126 Energie-/Positivitätschecks eines rationalen endlichen Graphanalogons, 665 Inklusionsisometrien, 665 Intertwining-Checks und 3367 Kokzyklusfälle; die restlichen Checks betreffen Isolations- und exakte Restbudgets. Die Modellkanten haben ausdrücklich rationale Beispielgewichte, nicht vorgetäuschte Werte des kontinuierlichen h. Keine Quadratur, kein Float-Positivitätszeugnis, keine große Matrix und kein C0-/A1-Prüfer wurden ausgeführt.

Diese endlichen Tests unterstützen die oben angegebenen universellen Algebra-/Trägerbeweise. Sie ersetzen insbesondere nicht Tonelli, die Definitionsbereichsargumente oder eine externe Prüfung. Die Anzahl der Checks wird nicht als Evidenzstärke einer unabhängigen Zertifizierung ausgegeben.

Quellenanker:

- `X_CANDIDATE_C0_SPEC.md` am Eingangsanker: COMMON-JUMP-Bilanz, T_a^0, Normierung und ursprünglicher Witness.
- `research/x-c1/X_C1_STORAGE.md` am Eingangsanker: tatsächliche Supply-/Randpaarung, kein positiver kausaler Original-Gauge-Speicher.
- `research/x-c1/X_C1_ENDPOINT_GREEN_BRIDGE.md` am Eingangsanker: integrierte Randidentität EG6 und vollständige Gamma-Mischpaarung EG10--EG11.
- NIST DLMF §§5.4, 5.9: klassische Digamma-/Gamma-Normalisierungen, https://dlmf.nist.gov/5.4 und https://dlmf.nist.gov/5.9 .
- M. Keller und D. Lenz, *Dirichlet forms and stochastic completeness of graphs and subgraphs*, arXiv:0904.2985, https://arxiv.org/abs/0904.2985 : klassischer Kontext positiver Kanten-/Knotenformen, kein importierter Objekt-X-Positivitätssatz.

Die konkrete kontinuierlich-atomare Zerlegung, das rationale Sechszellenbudget und die angegebenen Verbindungsabbildungen werden in diesem Dokument direkt bewiesen. Keine Literatur-Neuheit wird beansprucht. Forschungsstatus: **C1-SPARSE-GEOM auf Autorenebene konstruiert; voller C1-GEOM weiterhin OFFEN.**
