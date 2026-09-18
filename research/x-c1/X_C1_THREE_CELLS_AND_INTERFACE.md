# X-C1 — Drei Quellenzellen, vollständige Schur-Kopplung und Gamma-Naht

**Datum:** 16. September 2026.  
**Rolle:** neue analytische Autorenableitung; kein unabhängiges externes Review.  
**Quellanker:** C0 bei `d7b32ccfb9d0d90f19d4a7a5b0fbd19b0928f257`; Endpunkt-Green-Rechnung bei `708542fb8a6a230b2e1ae4b8d44d51a7aa1e393d`.  
**Scope:** exakt festgelegte drei getrennte Quellenintervalle; kein gesamtes Einheitsfenster.  
**Keine Verwendung von A1-COMP.** Kein C0-/A1-Replay, keine Repoänderung, keine CI-Ausführung, keine Neuheitsbehauptung.

## 0. Zwei Resultate

1. Auf der unten definierten unendlichdimensionalen Dreizellen-NULLPOL-Klasse gibt es eine ausdrücklich konstruierte lineare Ausgabe `T_triple` mit

```math
\|T_{\rm triple}u\|^2=Q_W[u],\qquad
Q_W[u]>\frac{53}{100}\|u\|_2^2\quad(u\ne0).
```

Die Kopplung enthält Prime 2, Prime 3 und den vollständigen Gamma-Kernel, einschließlich der durch die erste Schur-Elimination erzeugten neuen Blattkopplung. Die dritte Schur-Untergrenze des beschränkten Restblocks ist strikt größer als `95749/90545 > 21/20`.

2. Bei aneinanderstoßenden Zellen hat der Gamma-Kreuzoperator einen Carleman-Anteil mit wesentlicher Norm `pi/2`. Bei der hier fixierten Breite `1/50` ist das größer als die reine skalare Reserve `c_delta`. Die für getrennte Zellen erfolgreiche Behandlung »kleine Gamma-Kreuzkopplung gegen skalare Reserve« lässt sich somit nicht unverändert auf diese Naht übertragen. Das ist kein negativer Weil-Zeuge: die noch vorhandene kurze Gamma-Energie darf dort nicht weggelassen werden.

## 1. Exakte Klasse und Normierung

Alle Skalarprodukte sind linear im ersten Argument. `U_t f(x)=f(x-t)`, `K_t=U_{t/2}-U_{-t/2}`, Nullfortsetzungen werden explizit verwendet. Definiere

```math
\ell_2=\log2,\quad \ell_3=\log3,\quad
\varepsilon=1/100,\quad \delta=2\varepsilon=1/50,
```

```math
x_1=-\ell_2/2,\quad x_2=\ell_2/2,\quad x_3=\ell_3-\ell_2/2,
\qquad J_i=(x_i-\varepsilon,x_i+\varepsilon).
```

Damit bleibt das bisherige Quellenpaar unverändert; nur die dritte Zelle wird als `J_1+log3` hinzugefügt. Alle Zellen liegen in `(-1,1)`. Ihre Abstände der Mittelpunkte sind `log2`, `log3`, `log(3/2)`.

Setze `H_i=L2(J_i)` und `H=H_1 direct-sum H_2 direct-sum H_3`. Der im Beweis unmittelbar benutzte Hilbert-Quellenraum ist

```math
\mathcal V_3=\bigoplus_{i=1}^3 H^1_0(J_i),\qquad
\mathcal W_3=\{(u_i)\in\mathcal V_3:
E_+(\sum_i u_i)=E_-(\sum_i u_i)=0\}.
```

`W_3` hat die H1-Topologie, nicht bloß die L2-Topologie. Das ist ein abgeschlossener, unendlichdimensionaler Unterraum von `V_3`. Die beiden Momente werden nur GLOBAL gefordert. Keine Forderung `E_+(u_i)=E_-(u_i)=0` für jeden Summanden wird eingeführt.

Die Aussagen beginnen auf glatten kompakten Quellen. Sie setzen sich durch H1-Dichte auf W_3 fort. Die zwei globalen Momentbedingungen lassen sich bei Approximation durch zwei feste kompakte Testfunktionen mit invertierbarer Momentmatrix exakt wiederherstellen; ihre Koeffizienten gehen mit den Momentfehlern gegen null.

Nicht behauptet wird, dass die unbeschränkte Gamma-Energie auf jedem Element von ganz H endlich ist. Alternativ kann man jede kleine Gamma-Abbildung auf `C_c^infinity(J_i)` abschließen und ihre Graphnorm-Vervollständigung verwenden. Die Konstruktion der beschränkten Kopplung und der Schur-Pivots bleibt auf dem ganzen H gültig. Eine Erweiterung des ursprünglichen C0-Liftings auf jede solche größere Formdomain wird hier nicht behauptet.

## 2. Kleine Gamma-Energie und skalare Reserve

Die feste archimedische Dichte und Schwelle sind

```math
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},\quad
\kappa_*=\log(8\pi)+\gamma+\pi/2,
\qquad c=c_\delta=2\int_\delta^\infty h(t)\,dt-\kappa_*.
```

Definiere für die Nullfortsetzung `E_i f`

```math
(\mathcal G_i f)(t,x)=K_tE_i f(x),\quad 0<t<\delta,
```

mit Zielraum `Y=L2((0,delta),h(t)dt;L2(R))`. Für f in H1_0 gilt

```math
\|\mathcal G_i f\|_Y^2\le
\|f'\|_2^2\int_0^\delta t^2h(t)\,dt<\infty.
```

Der vollständige Integrand ist für glatte f nahe null O(t), die Dichte allein O(1/t).

Für t>=delta sind die Selbstkorrelationen eines einzelnen Zellenvektors null. Daraus folgt die exakte Gamma-Diagonalform

```math
q_{\gamma,i}[f]=\|\mathcal G_i f\|^2+c\|f\|^2.
```

### 2.1 Neue elementare Reserveabschätzung

Aus der bereits im Quelltext hergeleiteten Integralformel folgt, mit z=delta/4=1/200,

```math
c=\log\coth z-\log(8\pi)-\gamma-2\arctan(\tanh z).
```

Es gelten `coth z>1/z`, `atan(tanh z)<z`, `pi<22/7` sowie `gamma<H_20-log20`. Damit

```math
c>\log(1750/11)-H_{20}-1/100>29/20.                (T1)
```

Die zweite Ungleichung wird mit einer expliziten rationalen unteren Logarithmussumme überprüft. Für `x>0` wird der Logarithmus nach Potenzen von 2 auf `[1,2]` reduziert und dann

```math
\log x=2\sum_{n=0}^{N-1}\frac{q^{2n+1}}{2n+1}+R_N,
\quad q=(x-1)/(x+1),\quad
0\le R_N\le\frac{2q^{2N+1}}{(2N+1)(1-q^2)}
```

benutzt (N=48). Dies ist eine elementare exakte Abschätzung, keine numerische Quadratur.

Für die spätere Nahtanalyse gilt außerdem `coth z<1/z+z`, `pi>157/50` und `gamma>H_20-log21>11/20`. Daher

```math
c<\log8-11/20<31/20<\pi/2.                       (T2)
```

Der letzte Schritt benutzt log2<7/10. Der Checker überprüft sämtliche rationalen Enclosures. Der Beweis von `coth z<1/z+z` folgt aus der positiven Ableitung von `(1+z^2)sinh z-z cosh z`; es wird keine asymptotische Ersetzung benutzt.

## 3. Alle Kopplungsoperatoren — kein weggelassener Gamma-Rest

Für i<j definiere

```math
(H_{ji}f)(y)=\int_{J_i}h(y-x)f(x)\,dx,\qquad y\in J_j.
```

Die beiden Shiftoperatoren `V_2:H_1->H_2`, `V_3:H_1->H_3` sind

```math
V_2f(y)=f(y-\ell_2),\qquad V_3f(y)=f(y-\ell_3).
```

Beide sind unitär zwischen den gleich langen Zellen. Setze

```math
A=w_2V_2+H_{21},\quad B=w_3V_3+H_{31},\quad C=H_{32},
\qquad w_2=\log2/\sqrt2,\quad w_3=\log3/\sqrt3.
```

Typen: A:H1->H2; B:H1->H3; C:H2->H3. C enthält keinen Primport, aber die Gamma-Kopplung ist nicht null.

Die Supportausschlüsse gelten für alle Quellen, nicht nur für einen gewählten Buckel: `log(3/2)>2/5`, `log(4/3)>2/7`, beide weit größer als delta. Somit verbindet nur log2 die erste und zweite Zelle, nur log3 die erste und dritte; kein log(n), n>=2, verbindet die zweite und dritte. Innerhalb einer Zelle ist delta<log2.

Auf der globalen NULLPOL-Klasse verschwindet der gesamte gekreuzte Polblock. Die explizite Weil-Form ist exakt

```math
Q_W[u]=\sum_{i=1}^3\|\mathcal G_i u_i\|^2
+c\sum_{i=1}^3\|u_i\|^2
-2\operatorname{Re}\{\langle Au_1,u_2\rangle+
\langle Bu_1,u_3\rangle+\langle Cu_2,u_3\rangle\}. (T3)
```

Alle nicht koppelfähigen aktiven Prime-Power-Diagonalen heben sich exakt gegen die jeweilige Schwellenbuchung auf. Dies benutzt für n=p^k das Gewicht `Lambda(n)/sqrt(n)=(log p)/p^(k/2)`.

## 4. Gemeinsame Reserve statt unabhängiger Paarbudgets

Weil h fällt und `h(t)<=1+1/(2t)`, ergibt die Schur-Abschätzung mit den Zellenlängen delta

```math
\|H_{ji}\|\le\delta h(x_j-x_i-\delta).
```

Die folgenden rationalen Schranken sind ausreichend:

```math
\|H_{21}\|<86/2425,\qquad
\|H_{31}\|<37/1225,\qquad
\|H_{32}\|<22/475.
```

Mit `w_2<1/2` und `w_3<11/17` folgt

```math
\|A\|<\alpha=27/50,\quad
\|B\|<\beta=17/25,\quad
\|C\|<\eta=1/20.                                  (T4)
```

Die obere Schranke `w_3<11/17` folgt aus log3<11/10 und sqrt3>17/10. Das sind keine nach Testvektoren angepassten Koeffizienten: Die tatsächlichen Operatoren A,B,C sind bereits definiert; nur ihre konservativen Obergrenzen werden angegeben.

Der gesamte beschränkte Kopplungsoperator ist

```math
\mathcal R_3=\begin{pmatrix}0&A^*&B^*\\A&0&C^*\\B&C&0\end{pmatrix}.
```

Der Sternteil besitzt Norm `||(A,B)^T||`, also höchstens `sqrt(||A||^2+||B||^2)`. Daher

```math
\|\mathcal R_3\|<\sqrt{\alpha^2+\beta^2}+\eta
<87/100+1/20=92/100.                              (T5)
```

Die ganze skalare Diagonalreserve wird damit EINMAL gebucht:

```math
M_3:=cI-\mathcal R_3\succ(53/100)I.               (T6)
```

Dies beweist bereits `Q_W[u]>(53/100)||u||^2` für nichtverschwindende u in W3. Keine destruktive Prime-Interferenz wird dafür vorausgesetzt oder als entdeckt ausgegeben. Die gemeinsame Stern-Normabschätzung genügt in dieser getrennten Geometrie.

## 5. Exakte Operator-LDL-Kaskade

Wir behalten die drei kleinen Gamma-Energien als positive separate Ausgänge und faktorisieren den BESCHRÄNKTEN Rest M3. Die folgenden Delta_k sind also seine Pivots, nicht stillschweigend die Pivots eines anderen unbeschränkten Operators.

```math
\Delta_1=cI_{H_1},\qquad
\Delta_2=cI_{H_2}-c^{-1}AA^*,
```

```math
\widehat C=C+c^{-1}BA^*:H_2\longrightarrow H_3,
```

```math
\Delta_3=cI_{H_3}-c^{-1}BB^*
-\widehat C\Delta_2^{-1}\widehat C^*.              (T7)
```

Insbesondere enthält `C_hat` die bei der ersten Elimination induzierte Kopplung `BA*/c`. Sie fehlt im nackten arithmetischen 2--3-Port, entsteht aber zwangsläufig im Schur-Komplement. Sie wegzulassen würde die gemeinsame Quellreserve zweimal vergeben.

Mit c0=29/20 gibt (T4)

```math
\Delta_2\succ d_2I,\qquad
 d_2=c_0-\alpha^2/c_0=18109/14500>6/5.
```

Weiter gilt

```math
\|\widehat C\|<\eta+\alpha\beta/c_0=4397/14500,
```

und damit

```math
\Delta_3\succ d_3I,\qquad
 d_3=c_0-\beta^2/c_0-
 (\eta+\alpha\beta/c_0)^2/d_2
 =95749/90545>21/20.                              (T8)
```

Alle Inversen sind daher auf ihren benannten L2-Räumen wohldefiniert und beschränkt. Die Schranken hängen nicht von Dimension, Basiswahl oder einzelnen Quellen ab.

### 5.1 Konstruktive Quadratwurzeln, ohne Weil-Positivität zu importieren

Schreibe

```math
M_2=c^{-2}AA^*,\qquad
M_{(3)}=c^{-2}BB^*+c^{-1}\widehat C\Delta_2^{-1}\widehat C^*.
```

Beide sind positiv. Die obigen Schranken liefern

```math
\|M_2\|<7/50,\qquad \|M_{(3)}\|<7/25.
```

Damit konstruiert die Neumannreihe `Delta2^-1=c^-1 sum M2^n` die Inverse. Die Binomialreihe konstruiert

```math
\Delta_j^{1/2}=\sqrt c\sum_{n=0}^\infty
(-1)^n\binom{1/2}{n}M_{(j)}^n,\quad j=2,3.
```

Diese Reihen konvergieren in Operatornorm aufgrund der VORHER bewiesenen Schranken. Beispielsweise ist der Normfehler eines nach Grad m abgeschnittenen Wurzelpolynoms höchstens `sqrt(c) q^(m+1)/(1-q)` für die jeweilige Obergrenze q, da die Beträge der Binomialkoeffizienten höchstens eins sind. Es werden keine Eigenwerte der Ziel-Weilform zum Definieren eines Operators vorausgesetzt.

### 5.2 Tatsächlicher Output, mit korrekter Dreiecksrichtung

```math
T_{\rm triple}u=\begin{pmatrix}
\mathcal G_1u_1\\\mathcal G_2u_2\\\mathcal G_3u_3\\
\sqrt c\,(u_1-c^{-1}A^*u_2-c^{-1}B^*u_3)\\
\Delta_2^{1/2}(u_2-\Delta_2^{-1}\widehat C^*u_3)\\
\Delta_3^{1/2}u_3
\end{pmatrix}.                                    (T9)
```

Der Zielraum ist `Y direct-sum Y direct-sum Y direct-sum H1 direct-sum H2 direct-sum H3`. Vollständiges Ausmultiplizieren ergibt

```math
\|T_{\rm triple}u\|^2=Q_W[u]\quad(u\in W_3).       (T10)
```

Die polarisierte Identität folgt für alle komplexen Quellen in W3. In der Standardnotation `M3=L Delta L*` lautet der Output `Delta^(1/2)L* u`, nicht `Delta^(1/2)L u` und nicht das Vorzeichen-umgedrehte untere Dreieck. Dies erklärt die obere Dreiecksrichtung in (T9).

Auf dem tatsächlichen C0-Feld lautet die Auswertung: Randquelle `R_0H` lesen, ihre drei Zellenkomponenten nehmen, (T9) anwenden. Sie ist auf genau den physischen Zuständen des angegebenen Quellenraums definiert. Die Polports bleiben erhalten; ihre gemeinsame Paarung ist auf der benannten Klasse null.

Auf dem alten Zweizellen-Unterraum reproduziert T_triple exakt dieselbe Form wie T_pair. Die beiden Ausgaben brauchen nicht koordinatenweise gleich zu sein; die Zuordnung auf erzeugten Bildräumen ist aufgrund der gemeinsamen Gramidentität isometrisch. Daraus folgt keine globale Fensterrealisierung auf Quellen außerhalb dieser drei Zellen.

## 6. Was im Vollfenster-Vorschlag korrigiert werden muss

### 6.1 Globale Momente statt künstlicher Zellmomente

Die Forderung `E_±(u_j)=0` für jede von N Zellen ist im L2-Ambientraum von Kodimension 2N. Global NULLPOL besitzt nur Kodimension zwei. Der erstere Raum ist nicht dicht im letzteren. Ein Vollfenster-Beweis darf also die restlichen 2N-2 Momentfreiheitsgrade nicht eliminieren, ohne ihre Rückführung zu beweisen.

Bei einer zusammenhängenden Zerlegung ist außerdem die scharfe Zellenrestriktion einer globalen H1-Funktion gewöhnlich nicht H1_0 in jeder Zelle. Entweder benötigt man die natürliche, schwächere Gamma-Formdomain oder eine kontrollierte glatte Lokalisierung. Das ist ein anderes Problem als die hier gewählte getrennte H1_0-Klasse.

### 6.2 Prime-power-Gewicht

Für n=4 ist `Lambda(4)=log2`, nicht log4. Deshalb liegt die korrekte aktive Gewichtssumme für a=1 rigoros in `(2.92623,2.92624)`, nicht bei 3.272. Außerdem ist eine globale Summe aller aktiven Gewichte keine automatisch bewiesene untere Schranke einer konkreten Zellenzeile: beide Shift-Richtungen, Trägerüberlappungen und die Randlage müssen mitgezählt werden.

### 6.3 Schur-Residuum ist nicht automatisch Speichertransfer

Eine Quellenblock-Elimination und eine Transport-/Speicheridentität sind unterschiedliche mathematische Konstruktionen. Ein Identifikationssatz benötigt explizite Zustandsabbildungen, Domains, Randbedingungen und Eliminationsregeln. Die vorhandene Flussidentität allein beweist keine Positivität der nacheinander auftretenden Schur-Pivots.

## 7. Neue Nahtanalyse: angrenzende Zellen sind nicht kleine kompakte Gamma-Kopplungen

Nimm benachbarte Zellen `(-delta,0)` und `(0,delta)`. In Grenzabständen s=-x und t=y lautet der Gamma-Kreuzoperator auf L2(0,delta)

```math
(H_\delta f)(t)=\int_0^\delta h(s+t)f(s)ds.
```

Nahe null gilt durch Taylorentwicklung exakt

```math
h(r)=\frac1{2r}+\frac14+O(r).
```

Somit

```math
H_\delta=\tfrac12 C_\delta+K_\delta,\qquad
(C_\delta f)(t)=\int_0^\delta\frac{f(s)}{s+t}ds,
```

wobei K_delta einen auf dem abgeschlossenen Quadrat stetigen Kernel besitzt, also Hilbert-Schmidt und kompakt ist. C_delta ist beschränkt, aber nicht kompakt.

### 7.1 Eigenständiger Nachweis der wesentlichen Norm

Die unitäre logarithmische Koordinate `t=delta exp(-x)`, x>0, bildet C_delta auf die Halbgeradenkompression der Faltung mit

```math
k(x-y)=\frac1{2\cosh((x-y)/2)}
```

ab. Es gilt `integral_R k=pi`; Youngs Ungleichung liefert Norm höchstens pi.
Für `g_L=L^(-1/2) 1_[L,2L]` gilt `||g_L||=1`, `g_L` konvergiert schwach gegen null, und

```math
\langle g_L,\widetilde C_\delta g_L\rangle
=\int_{-L}^L(1-|t|/L)k(t)dt\longrightarrow\pi.
```

Daher hat C_delta sowohl Norm als auch wesentliche Norm pi. Da kompakte Störungen die wesentliche Norm nicht verändern,

```math
\boxed{\|H_\delta\|_{ess}=\pi/2.}                (I1)
```

Dies gilt für jede delta>0. Es gibt also keine gegen null gehende L2-Norm der Gamma-Nahtkopplung beim Verfeinern der Zellen. Die skalare Reserve c_delta selbst ändert sich mit delta; daraus folgt kein universelles Verfeinerungs-No-Go.

Bei der hier fixierten Breite delta=1/50 folgt aus (T2)

```math
c_\delta<31/20<\pi/2\le\|H_\delta\|.             (I2)
```

Der ZWEIZELLEN-REST, der die kurze Gamma-Energie weglässt, kann somit nicht durch bloße Kontraktivität `||H_delta||<c_delta` positiv faktorisiert werden. Konkret besitzen symmetrische, am Nahtpunkt konzentrierte Carleman-Folgen negative Werte für diesen bloßen Rest. Wegen der schwachen Nullkonvergenz verschwinden die zwei globalen Momente asymptotisch; eine feste endlichrangige Momentkorrektur ändert diesen Befund nicht. Glatte Näherungen liefern bei Bedarf tatsächliche Formkern-Vektoren für den REST.

**Firewall:** Die vollständige Gamma-/Weil-Form enthält zusätzlich die kurzen Gamma-Energien. (I2) ist keine negative Weil-Testfunktion und widerspricht weder dem Dreizellensatz noch A1. Es widerlegt nur das Weglassen der kurzen Gamma-Energie in genau dieser skalaren Naht-Abschätzung.

### 7.2 Die richtige positive Nahtenergie ist bereits explizit

Die archimedische Sprungenergie besitzt die exakte Darstellung

```math
\int_0^\infty h(t)\|K_tu\|^2dt
=\int_{x<y}h(y-x)|u(y)-u(x)|^2dxdy.               (I3)
```

Für zwei aneinanderstoßende Zellen ist deren INTERFACE-Anteil daher genau

```math
\int_{J_j}\int_{J_k}h(y-x)|u_k(y)-u_j(x)|^2dxdy\ge0. (I4)
```

Diese positive Differenzenergie muss zusammen mit den zugehörigen lokalen Diagonalmassen erhalten werden. Sie getrennt in »volle lokale Reserve« und »kleine kompakte Kreuzkopplung« zu zerlegen ist an der Naht die falsche Abschätzung.

(I3)--(I4) lösen die Subtraktion der gesamten kappa-/Prime-Schwelle nicht. Sie geben aber den konkreten nächsten Lokalisierungsbaustein vor und vermeiden eine nachweislich ungeeignete Normannahme.


### 7.3 Der negative Rest ist reparierbar: echte positive Auswertung der verbundenen Doppelzelle

Dass (I2) kein Weil-No-Go ist, lässt sich hier sogar konstruktiv zeigen. Vereine die zwei benachbarten Zellen zu einem Intervall der Breite `2delta=1/25`. Für diesen verbundenen Träger sind weiterhin alle Primport-Selbstkorrelationen null, denn `2delta<log2`. Mit

```math
c_{2\delta}=2\int_{2\delta}^\infty h(t)dt-\kappa_*
```

liefert dieselbe elementare Rechnung

```math
c_{2\delta}>\log(875/11)-H_{20}-1/50>3/4.          (I4a)
```

Für jede global NULLPOL-Quelle u auf dieser verbundenen Doppelzelle ist somit

```math
u\longmapsto
\left([t\mapsto K_tu]_{0<t<2\delta},\sqrt{c_{2\delta}}u\right)
```

in das entsprechende positive Gamma-Ausgabeprodukt eine exakte Weil-Faktorisierung mit unterer Schranke `3/4`. Dies ist klassische kleine-Träger-Positivität in expliziter Form. Sie schließt kein Einheitsfenster, zeigt aber unmittelbar, dass das Wegwerfen der Gamma-Nahtenergie — nicht die Naht selbst — den negativen Rest verursacht.

## 8. Zwangsbedingter Schur-Schritt: die globalen Momente im Eliminationsterm behalten

Ein zusätzlicher allgemeiner algebraischer Baustein ist ohne Weil-Positivitätsannahme verfügbar. Seien D ein beschränkter strikt positiver Operator auf H0, R:H0->Hrest, E ein hermitescher Restoperator. Betrachte

```math
q(x,y)=\langle x,Dx\rangle-2Re\langle Rx,y\rangle+\langle y,Ey\rangle,
\qquad Mx+Ny=0,
```

mit surjektivem M:H0->C2. Setze

```math
G=MD^{-1}M^*>0,\qquad T=N+MD^{-1}R^*.
```

Nach dem Quadratabzug `z=x-D^{-1}R^*y` ist die Bedingung `Mz=-Ty`. Ihre minimale D-Energie beträgt `⟨Ty,G^{-1}Ty⟩`. Daher ist das EXAKTE constrained Schur-Residuum

```math
E-RD^{-1}R^*+T^*G^{-1}T.                          (I5)
```

Der positive Rang-zwei-Zusatz in (I5) entsteht aus den vorgeschriebenen globalen Momenten, nicht aus gefitteten Koeffizienten. Er ist kein endlichrangiger Ersatz für die unendlichdimensionale Schwellenmasse. Für unbeschränkte D sind Domain-/Formversionen gesondert auszuführen; hier wird nur der benannte beschränkte Fall bewiesen.

Ein verbundenes Fensterprogramm muss diese Nebenbedingungen oder eine äquivalente Parametrisierung mitführen. Jede Zelle einzeln NULLPOL zu machen würde gerade diese Kopplungsinformation verlieren.

## 9. Checks, Status und nächste mathematische Grenze

Der beigefügte Standardbibliothek-Prüfer wurde lokal ausgeführt. Er prüft 35 exakte rationale beziehungsweise skalare algebraische Beziehungen, darunter die vollständigen Schur-Budgets, die durch Elimination erzeugte Blattkopplung und den Reservevergleich an der Gamma-Naht. Die kleinen skalaren Matrixidentitäten sind nur Algebraregressionen; die Operatorbeweise stehen oben. Keine diskretisierte Matrix wird als Ersatz des unendlichdimensionalen Beweises ausgegeben.

Erreicht: explizite positive Auswertung auf der getrennten Dreizellenklasse, einschließlich beider konkurrierender Primports und aller Gamma-Kreuzterme.

Offen: positive Auswertung auf allen Quellen im zusammenhängenden Einheitsfenster. Der nächste sinnvolle Schritt ist eine Naht-/Lokalisierung mit der vollen positiven Energie (I4) und globalen Momentbedingungen (I5), nicht nur ein weiteres getrenntes Zellpaar oder eine größere normweise Zeilensumme.

Kein Ergebnis dieses Dokuments promoviert C1-GEOM insgesamt, A1, Registry, all-window NP-GAP, Objekt X oder RH.

## Quellen

- Exakte Ausgangsnormalisierung: [COMMON-JUMP, fester main-Modellanker](https://github.com/Waschtl904/objekt-x-programm/blob/ac164bbbd2c46623aa64e567d21f813f41f164b0/audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md).
- [C0-Spezifikation, unveränderter Quellanker](https://github.com/Waschtl904/objekt-x-programm/blob/d7b32ccfb9d0d90f19d4a7a5b0fbd19b0928f257/X_CANDIDATE_C0_SPEC.md).
- [Endpunkt-Green-Rechnung und Zweiquellen-Budgets](https://github.com/Waschtl904/objekt-x-programm/blob/708542fb8a6a230b2e1ae4b8d44d51a7aa1e393d/research/x-c1/X_C1_ENDPOINT_GREEN_BRIDGE.md), insbesondere Abschnitte 5--6.
- [DLMF 27.2.14](https://dlmf.nist.gov/27.2#E14): von-Mangoldt-Gewichte.
- [DLMF 4.6.7](https://dlmf.nist.gov/4.6#E7): klassische Binomialreihe.
- [D. R. Yafaev, Spectral and scattering theory for perturbations of the Carleman operator, arXiv:1210.5709](https://arxiv.org/abs/1210.5709): klassischer Carleman-Kontext. Die hier benötigte halbintervallbezogene Normrechnung wurde in §7.1 selbst angegeben; die Literatur wird nicht als Prüfung dieses Projektresultats ausgegeben.
