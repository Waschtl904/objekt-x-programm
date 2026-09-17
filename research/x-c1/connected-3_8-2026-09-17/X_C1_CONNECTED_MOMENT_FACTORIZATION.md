# X-C1-CONNECTED-3/8 — Gamma-Nahtenergie, globale Momente und positiver Output

**Datum:** 17. September 2026.  
**Status:** neue analytische Autorenableitung; externe Prüfung offen.  
**Reichweite:** gesamte H¹₀-NULLPOL-Klasse im zusammenhängenden Intervall `I=(-3/8,3/8)`; kein gesamtes Einheitsfenster.  
**Nicht verwendet:** A1, numerische Eigenwerte, vorausgesetzte Weil-Positivität, getrennte lokale Mellinbedingungen.  
**Diese Ausführung:** lokale Mathematik/Dateien, keine Repository-Änderung oder Statuspromotion.

## 0. Ergebnis

Setze `a=3/8`, `L=2a=3/4` und

```math
\mathcal W_I=H^1_0(I;\mathbb C)\cap\ker E_+\cap\ker E_-,
\qquad E_\pm(u)=\int_Ie^{\pm x/2}u(x)\,dx.
```

Es wird eine vorwärts definierte lineare Auswertung `T_conn` in einen positiven Hilbertraum konstruiert mit

```math
\boxed{\|T_{\rm conn}u\|^2=Q_W[u],\qquad
Q_W[u]>\frac{487}{20008}\|u\|_2^2>\frac1{50}\|u\|_2^2\quad(u\ne0).} \tag{C0}
```

Auf glatten kompakten Quellen ist dies die eingefrorene Weil-Form. Auf H¹₀ wird ihre stetige Formfortsetzung verwendet. Es gibt keine inneren Zellrandbedingungen, keine verbotenen Lücken im Quellenträger und nur ZWEI globale Momente.

Die Intervalllänge 3/4 übersteigt log2. Der Prime-2-Kanal ist daher tatsächlich aktiv und wird exakt erhalten. log3 ist größer als 3/4; andere Primport-Korrelationen verschwinden durch die Trägergeometrie, nicht durch eine Approximation. Der bisherige feste Prime-2-Buckeltest liegt vollständig in I. Die dritte Zelle bei log3-log2/2 liegt NICHT in I: dies ist keine über die Trägermenge behauptete Erweiterung des gesamten Dreizellensatzes.

Die Beweisidee ist eine globale, nahtverträgliche Normalisierung der singulären Gammaenergie. Ihr exakt diagonalisierbarer positiver `1/(2|x-y|)`-Anteil wird nirgends an Zellnähten abgeschnitten. Die beiden negativen niedrigen Moden der resultierenden Unterform werden durch die zwei tatsächlichen Mellinbedingungen aus höheren Moden rekonstruiert. Der dafür benötigte Rang-zwei-Operator wird vor jeder Quadratwurzelbildung rigoros als Kontraktion abgeschätzt.

Dies ist kein Neuheitsanspruch für Kleinfensterpositivität, Legendrepolynome, logarithmische Energie oder Binomial-/Schurmethoden. Der Beitrag ist die unten ausgeschriebene konkrete Auswertung und ihre Quellen-/Naht-/Momentkontrolle im bestehenden Projektmodell.

## 1. Ausgangsform und exakte Kantenbuchhaltung

Alle Skalarprodukte sind linear im ersten Argument. Quellen außerhalb I werden nullfortgesetzt. Die importierten Projektkonventionen sind

```math
h(t)=\frac{e^{-t/2}}{1-e^{-2t}}=\frac{e^{t/2}}{2\sinh t},
\quad \kappa_* =\log(8\pi)+\gamma+\frac\pi2,
\quad t_2=\log2,\quad w_2=\frac{\log2}{\sqrt2}.
```

Auf NULLPOL gilt

```math
Q_W[u]=\int_0^\infty h(t)\|K_tu\|_2^2dt-\kappa_*\|u\|_2^2
-2w_2\operatorname{Re}\int u(x-t_2)\overline{u(x)}dx. \tag{C1}
```

Schreibe `H(s)=integral_s^infinity h(t)dt`. Für x in I sei

```math
W_I(x)=H(a+x)+H(a-x),
\quad d_P(x)=w_2\{1_I(x-t_2)+1_I(x+t_2)\},
\quad \rho(x)=W_I(x)-\kappa_*-d_P(x).
```

Durch Zerlegen der Gamma-Kanten nach inneren/äußeren Endpunkten und durch
`-2Re(u(x)conj(u(y)))=|u(x)-u(y)|²-|u(x)|²-|u(y)|²` folgt exakt

```math
Q_W[u]=\int_{x<y,\ x,y\in I}h(y-x)|u(y)-u(x)|^2dxdy
+w_2\int_{-a}^{a-t_2}|u(x+t_2)-u(x)|^2dx
+\int_I\rho(x)|u(x)|^2dx.                         \tag{C2}
```

Dies ist die bereits bewiesene Kanten-/Knotenidentität, nun auf einem verbundenen Träger. Jede Kante wird einmal gezählt. Eine Quellenrestriktion auf Teilzellen oder eine Behauptung positiver rho wird hier NICHT vorweggenommen.

## 2. Zwei elementare Kernelvergleiche auf dem ganzen relevanten Abstand

Für `0<t<=3/4` gilt

```math
\boxed{\frac1{2t}+\frac15<h(t)<\frac1{2t}+\frac13.} \tag{C3}
```

### Untere Schranke

Die Reihe für sinh liefert

```math
\frac{\sinh t}{t}\le1+b t^2,
\qquad b=\frac{1}{6(1-(3/4)^2/20)}=\frac{160}{933}.
```

Denn ab dem t²/6-Term ist das Verhältnis aufeinanderfolgender positiver Terme höchstens t²/20. Andererseits ist `exp(t/2)>=1+t/2+t²/8`. Die Differenz zwischen dieser unteren Schranke und `(1+2t/5)(1+b t²)` ist

```math
t\{\tfrac1{10}-(b-\tfrac18)t-\tfrac25 b t^2\}
\ge t\,\frac{1321}{49760}>0.
```

Damit `exp(t/2)>(1+2t/5)sinh(t)/t`, was die linke Seite von C3 ergibt.

### Obere Schranke

Aus `sinh t>=t`, Konvexität der Exponentialfunktion und `exp(3/8)<3/2` folgt auf [0,3/4]

```math
e^{t/2}\le1+\frac{e^{3/8}-1}{3/4}t<1+\frac23t.
```

Division durch 2t gibt die rechte Seite von C3. Alle skalaren Endpunktungleichungen werden im Begleitprüfer rational eingeschlossen.

Definiere deshalb den nichtnegativen, am Ursprung stetig fortsetzbaren Restkernel

```math
r(t)=h(t)-\frac1{2t}-\frac15,\qquad r(0)=\frac1{20}.
```

Die Singularität 1/(2t) wird NICHT verworfen. Sie wird in §4 auf dem gesamten Intervall exakt behandelt.

## 3. Der negative Knotenanteil hat eine explizite globale Untergrenze

Es gilt

```math
\boxed{\rho(x)>-\frac{3249}{2000}>-\frac{13}{8}\quad\text{für fast alle }x\in I.} \tag{C4}
```

### 3.1 Mittelpunkt ohne Primport-Abzug

h ist positiv und fallend; H ist konvex. Daher `W_I(x)>=2H(a)`. Die exakte Stammfunktionsformel

```math
H(s)=\operatorname{atanh}(e^{-s/2})+\arctan(e^{-s/2})
```

liefert mit z=a/4=3/32

```math
2H(a)-\kappa_*
=\log\coth z-\log(8\pi)-\gamma-2\arctan(\tanh z)
>\log\frac{14}{33}-\gamma-\frac3{16}.
```

Verwendet sind `coth z>1/z`, `atan(tanh z)<z` und `pi<22/7`. Die Grenzen

```math
\log(33/14)<429/500,\qquad
\gamma<H_{400}-\log400<579/1000
```

geben

```math
2H(a)-\kappa_*>-429/500-579/1000-3/16=-3249/2000.
```

Hier ist H_400 die harmonische ZAHL, nicht die oben definierte Tailfunktion H(s). Die klassische Schranke `gamma<H_n-log n` folgt aus der monoton fallenden Harmonischen-Logarithmus-Folge. Die Grenze pi<22/7 folgt etwa aus dem positiven Integral `integral_0^1 x^4(1-x)^4/(1+x²)dx=22/7-pi`.

### 3.2 Die tatsächlichen Prime-2-Endbänder besitzen zusätzliche Reserve

Es gelten `69/100<t_2<7/10`, `3/4<2t_2` und `w_2<1/2`. Deshalb ist d_P entweder null oder genau w_2. Im zweiten Fall ist `|x|>=t_2-a`.

W_I wächst mit |x|. Mit d=L-t_2 liegt sein Minimum auf den aktiven Endbändern somit bei

```math
W_I(t_2-a)=H(d)+H(t_2).
```

Aus C3 folgt

```math
W_I(t_2-a)-2H(a)
=\int_d^a h(s)ds-\int_a^{t_2}h(s)ds
>\frac12\log\frac{a^2}{d t_2}-\frac2{15}(t_2-a).
```

Nun `d<3/50`, `t_2<7/10`, also `a²/(d t_2)>375/112`, und
`log(375/112)>6/5`. Ferner `t_2-a<13/40`. Folglich

```math
W_I(t_2-a)-2H(a)>3/5-(2/15)(13/40)=167/300>1/2>w_2.
```

Der Primport-Knotengrad wird daher exakt durch die zusätzliche äußere Gamma-Leckage der aktiven Endbänder absorbiert. Im gesamten Intervall gilt sogar `rho(x)>2H(a)-kappa_*` auf den aktiven Bändern und `rho(x)>=2H(a)-kappa_*` sonst. Das beweist C4.

Setze

```math
V(x)=\rho(x)+\frac{13}{8}>\frac1{2000}.           \tag{C5}
```

V ist ein aus den festen h-, Prime- und Trägerdaten DEFINIERTES positives Gewicht. Es wurde nicht aus einer getesteten Zielmatrix rückgerechnet. Seine logarithmischen Singularitäten an den äußeren Endpunkten sind integrierbar.

## 4. Die gesamte singuläre Nahtenergie wird diagonalisiert, nicht abgeschnitten

Definiere die regionale Energie

```math
\mathcal E_0[u]=\int_{x<y\in I}\frac{|u(y)-u(x)|^2}{2(y-x)}dxdy.
```

Sei

```math
e_n(x)=\sqrt{\frac{2n+1}{2a}}P_n(x/a),\quad
u_n=\langle u,e_n\rangle,
\quad \mathsf H_n=\sum_{k=1}^n\frac1k,\quad\mathsf H_0=0.
```

Dann gilt auf H¹(I) exakt

```math
\boxed{\mathcal E_0[u]=\sum_{n\ge0}\mathsf H_n|\nu_n|^2.} \tag{C6}
```

### Vollständiger Beweis des Spektralfaktors

Nach Skalierung genügt [-1,1]. Der zugehörige positive Operator auf Polynomen ist

```math
(A_0f)(x)=\frac12\int_{-1}^1\frac{f(x)-f(y)}{|x-y|}dy.
```

Auf Monomen ergibt direkte Integration

```math
A_0x^n=\mathsf H_n x^n-
\sum_{\substack{1\le k<n\\k\ \mathrm{ungerade}}}\frac{x^{n-1-k}}{k+1}.
```

A_0 erhält die Räume von Polynomen bis zu jedem Grad. Seine symmetrische Form ist E_0. Daher ist A_0 P_n orthogonal zu jedem Polynom von Grad<n. Der Leitkoeffizient liefert `A_0P_n=H_nP_n`. Die klassische vollständige Legendre-Orthogonalität ergibt C6 zunächst für Polynome.

Polynome sind dicht in H¹(I): die Ableitung durch Polynome approximieren und integrieren. Außerdem `E_0[u]<=L²||u'||²/4`. Daher konvergieren diese Approximationen in der E_0-Formnorm. Die bereits für Polynome exakte gewichtete Koeffizientenisometrie erweitert sich auf H¹; die Grenzkoeffizienten sind wegen L²-Konvergenz genau nu_n. Dies beweist C6 ohne einen endlichen Spektralcutoff.

C6 umfasst ausdrücklich auch jedes Integral über zwei angrenzende Teilintervalle. Das Carleman-Kreuzstück wird nie isoliert gegen eine skalare Reserve getestet. Es bleibt innerhalb der positiven Differenzenergie E_0.

Der konstante Kernel besitzt ebenfalls eine exakte globale Form:

```math
\frac15\int_{x<y\in I}|u(y)-u(x)|^2dxdy
=\frac L5\sum_{n\ge1}|\nu_n|^2
=\frac3{20}\sum_{n\ge1}|\nu_n|^2.                 \tag{C7}
```

## 5. Nur zwei negative Moden — und genau die zwei tatsächlichen Momente

Auf der gemeinsamen Kantenmenge `x<y` in I definiere das positive Maß

```math
d\nu_*(x,y)=r(y-x)dxdy+d\nu_P(x,y),
\quad \int Fd\nu_P=w_2\int_{-a}^{a-t_2}F(x,x+t_2)dx.
```

Setze `D_Iu(x,y)=u(y)-u(x)`. Aus C2, C5, C6 und C7 folgt die EXAKTE Bilanz

```math
Q_W[u]=\|D_Iu\|_{L^2(\nu_*)}^2+\|u\|_{L^2(Vdx)}^2
+\sum_{n\ge2} a_n|\nu_n|^2
-\frac{13}{8}|\nu_0|^2-\frac{19}{40}|\nu_1|^2,
\qquad a_n=\mathsf H_n-\frac{59}{40}\ge\frac1{40}. \tag{C8}
```

Keine endliche Approximation der Gammaenergie ist in C8 enthalten. Der gesamte unendliche harmonische Faktor bleibt vorhanden.

Nun seien `c(x)=cosh(x/2)`, `s(x)=sinh(x/2)` und
`c_n=<c,e_n>`, `s_n=<s,e_n>`. c_n verschwindet für ungerade n, s_n für gerade n. Es gilt c_0>0, s_1>0. NULLPOL ist genau

```math
\nu_0=-c_0^{-1}\sum_{n\ge2}c_n\nu_n,
\qquad
\nu_1=-s_1^{-1}\sum_{n\ge2}s_n\nu_n.             \tag{C9}
```

Dies sind ZWEI globale Gleichungen. Es wird kein Mittelwert und kein Mellinmoment pro Zelle auf null gesetzt.

### 5.1 Explizite Kontrolle der Momentrekonstruktion

Auf |x|<=3/8 geben positive Taylorreihen

```math
0\le\cosh(x/2)-1<1/50,
\qquad
\left|\sinh(x/2)-x/2\right|<(1/150)|x|/2.
```

Zum Nachweis, mit z=3/16, genügen

```math
\cosh z-1\le\frac{z^2}{2(1-z^2/12)}<1/50,
\quad
\frac{\sinh z}{z}-1\le\frac{z^2}{6(1-z^2/20)}<1/150.
```

Für die orthogonalen Reste `c_perp=c-c_0e_0`, `s_perp=s-s_1e_1` gilt deshalb

```math
\frac{\|c_\perp\|}{c_0}<\frac1{50},\qquad
\frac{\|s_\perp\|}{s_1}<\frac1{150}.              \tag{C10}
```

Begründung: c_0>=sqrt(L), der beste konstante Approximationsfehler ist höchstens ||c-1||. Ebenso s_1>=||x||/2 und der beste lineare Approximationsfehler höchstens ||s-x/2||. Die Paritätsräume sind orthogonal.

Setze `z_n=sqrt(a_n)nu_n`, n>=2, also z in l², und DEFINIERE den festen Rang-zwei-Operator

```math
Bz=\begin{pmatrix}
\displaystyle\frac{\sqrt{13/8}}{c_0}\sum_{n\ge2}\frac{c_n}{\sqrt{a_n}}z_n\\[2mm]
\displaystyle\frac{\sqrt{19/40}}{s_1}\sum_{n\ge2}\frac{s_n}{\sqrt{a_n}}z_n
\end{pmatrix}.                                    \tag{C11}
```

Die Reihen konvergieren durch Cauchy-Schwarz. Beide Zeilen liegen auf orthogonalen Paritätskoordinaten. Aus C10 und a_n>=1/40 folgt

```math
\boxed{\|B\|^2<\max\{(13/8)40/2500,(19/40)40/22500\}
=\frac{13}{500}<\frac1{36}.}                     \tag{C12}
```

Insbesondere ||B||<1/6. Auf den durch C9 bestimmten Quellen gilt

```math
\|Bz\|^2=(13/8)|\nu_0|^2+(19/40)|\nu_1|^2.
```

Die negative niedrige Energie ist dadurch konkret und quantitativ an positive höhere Energie gebunden. Das ist keine Annahme von Q_W>=0.

## 6. Der tatsächliche positive Output

Auf l²(n>=2) definiere

```math
S=(I-B^*B)^{1/2}
=\sum_{k=0}^\infty(-1)^k\binom{1/2}{k}(B^*B)^k. \tag{C13}
```

C12 beweist Operatornormkonvergenz vor jeder Verwendung der Zielidentität. Der Fehler nach Grad m ist höchstens q^(m+1)/(1-q), q=13/500. Außerdem ist S-I von Rang höchstens zwei. Es wird nicht die Quadratwurzel der unbekannt positiven Weil-Form gebildet, sondern die eines bereits unabhängig kontrollierten zweimodigen Defektoperators.

Setze

```math
\mathcal K_*=L^2(\mathcal E_I,\nu_*)\oplus L^2(I,Vdx)\oplus\ell^2(\{2,3,\ldots\}),
\qquad
\boxed{T_{\rm conn}u=(D_Iu,u,Sz(u)).}             \tag{C14}
```

Aus C8--C13 folgt unmittelbar `||T_conn u||²=Q_W[u]`. Alle Bestandteile sind linear, der gemeinsame Testbereich ist ein komplexer linearer Raum, daher gilt durch Polarisation auch

```math
\langle T_{\rm conn}u,T_{\rm conn}v\rangle=Q_W(u,v).
```

### 6.1 Quantitativer Abstand

C9--C10 geben unter Nutzung der orthogonalen Paritäten

```math
\|u\|^2\le(1+1/2500)\sum_{n\ge2}|\nu_n|^2.
```

Deshalb

```math
\|Sz\|^2\ge(1-13/500)\|z\|^2
\ge\frac{487}{20000}\sum_{n\ge2}|\nu_n|^2
\ge\frac{487}{20008}\|u\|^2>\frac1{50}\|u\|^2.
```

Zusätzlich ist die Knotenenergie wegen V>1/2000 strikt positiv für nichtverschwindendes u. Dies beweist C0. Keine gemessene kleinste Eigenzahl wird behauptet.

### 6.2 Domain und Anschluss an C0

Auf H¹₀(I) sind alle drei Outputs wohldefiniert. r ist beschränkt; die Prime-Summe ist endlich. V hat nur integrierbare logarithmische äußere Randsingularitäten; H¹-Funktionen sind beschränkt. Der Koeffizientenoutput wird durch die regionale Energie E_0 kontrolliert, die auf H¹ stetig ist. Somit ist T_conn ein beschränkter Operator von W_I mit der H¹-Norm in K_*.

Die Form C1 ist auf H¹₀ stetig: für t<=1 benutze ||K_tu||<=t||u'||, für t>=1 benutze 2||u||, und die Prime-Translationen sind beschränkt. Glatte kompakte NULLPOL-Quellen sind in W_I dicht, indem man nach H¹-Approximation zwei kleine globale Momentfehler durch zwei fest gewählte kompakte Tests mit invertierbarer Momentmatrix beseitigt. Daher sind die Identitäten auf dem gesamten angegebenen Hilbert-Quellenraum gültig.

Auf dem bisherigen Vormediator gilt die konkrete Formel

```math
C_{\rm conn}(T_a^0u)=T_{\rm conn}u,
```

realisiert durch Auslesen von u=R_0H und die Komponenten C14. Sie ist auf den physischen Zuständen mit Quellen in W_I beschränkt, weil die C0-Norm `2||u'||²+(9/8)||u||²` zur H¹-Norm äquivalent ist. Eine Ausdehnung dieser H¹-Aussage auf beliebiges L² oder eine beliebige Quelle im gesamten Einheitsfenster wird nicht behauptet.

## 7. Naht- und Fensterverträglichkeit

Eine endliche Zerlegung von I verändert C14 NICHT. E_0 ist über alle inneren Kanten definiert; sowohl innere Zellkanten als auch Nahtkanten werden exakt einmal erfasst. Die Restkante D_I mit nu_* umfasst ebenfalls alle Abstandspaare, nicht nur nächste Nachbarn. Die Momentkoordinaten c_n,s_n gehören zum GANZEN I.

Weder die Quelle u noch ihre C0-Anhebung wird an einer künstlichen inneren Naht nullgesetzt. Auch eine globale H¹-Quelle, die dort von null verschieden ist, bleibt zulässig. Die frühe Bemerkung über zulässige Sprünge in schwächeren Gamma-Formräumen ist dafür nicht einmal nötig: das vorliegende Verfahren arbeitet direkt auf der unzerlegten H¹-Quelle.

Für jedes äußere Fenster mit Quellen in W_I wird dieselbe Auswertung und derselbe Zielraum K_* verwendet. Bei Nullfortsetzung aus einem kleineren Fenster bleibt u wörtlich gleich; dadurch sind die zugehörigen Zielabbildungen Identitäten auf K_*. Auf erzeugten Bildräumen entstehen die gleichen kanonischen Isometrien wie im bisherigen Gramargument. Dies ist keine Konstruktion für neue Quellen außerhalb I.

Auf den unverändert in I enthaltenen bisherigen f,g reproduziert die polarisierte Identität den kompletten Gamma- und Prime-2-Mischterm automatisch, nicht nur dessen Vorzeichen. Ein neuer Fit an f,g wird nicht vorgenommen.

## 8. Formversion der zwangsbedingten Schur-Identität

Für weitere räumliche Eliminationsschritte lässt sich I5 des Dreizellen-Dokuments korrekt auf positive GESCHLOSSENE Formräume übertragen. Das ersetzt keine noch fehlende Positivitätsabschätzung, beseitigt aber die Verwechslung unbeschränkter Operatoren mit ihren Forminversen.

Sei d eine geschlossene Form mit d>=c||.||², c>0, und X_d ihre vollständige Formdomain mit Skalarprodukt d. Sei Y ein geeigneter Rest-Formraum. Vorausgesetzt werden ein beschränktes K:Y->X_d, ein beschränktes surjektives M:X_d->C² und ein beschränktes N:Y->C². Die gemischte Form sei durch d(x,Ky) dargestellt. Die betrachtete Gesamtform lautet

```math
q(x,y)=d[x]-2Re\,d(x,Ky)+e[y],\qquad Mx+Ny=0.
```

M^dagger bezeichne das Adjunkt bezüglich d. Setze

```math
G=MM^\dagger>0,\qquad T=N+MK.
```

Jeder zulässige x besitzt eindeutig die Darstellung

```math
x=Ky-M^\dagger G^{-1}Ty+\xi,\qquad M\xi=0.
```

Der zweite Term ist d-orthogonal zu ker M. Deshalb ist die exakte Identität

```math
\boxed{q(x,y)=d[\xi]+e[y]-d[Ky]+\langle Ty,G^{-1}Ty\rangle.} \tag{C15}
```

Für beschränktes positiv invertierbares D und d[x]=<x,Dx> reduziert sich dies auf die frühere Formel. Im Formfall wird nur die wohldefinierte Rieszabbildung auf X_d benutzt. Es wird kein unzulässiges D^{-1} auf einen ungenannten Operatorbereich angewendet.

In einer Kaskade müssen die aktualisierten Momentkarten gemeinsam transportiert werden. Die zwei Koordinaten werden nicht bei jeder Zelle als neues unabhängiges Guthaben eingeführt. Wiederholte Minimierung über dieselbe gemeinsame affine Menge ist, bei den angegebenen endlichen/koerziven Minima, dieselbe Operation wie die direkte Minimierung. Das ist eine algebraische Konsistenz, kein Beweis positiver späterer Schur-Reste.

Die konkrete Konstruktion C9--C14 verwendet stattdessen eine gleichwertige globale Momentparametrisierung: sie löst die zwei Momente direkt nach den zwei niedrigen Moden auf. Dadurch entfällt in diesem Fenster eine räumliche Schur-Kaskade vollständig.

## 9. Offene Grenze, ohne neue künstliche Nebenbedingungen

Erreicht ist das gesamte verbundene Fenster (-3/8,3/8) auf W_I, mit aktiver Prime-2-Kopplung. Die vorherige verbundene Doppelzelle hatte lediglich Breite 1/25. Die neue Quelle darf insbesondere alle bisherigen Lücken zwischen den beiden festen Prime-2-Buckeln ausfüllen.

Nicht erreicht sind (-1,1), die dritte Prime-3-Zelle, alle Fenster oder der vollständige intrinsische X-Abschluss. Die grobe Skalarisierung rho>=-13/8 und der nur zweimodige negative Rest sind fensterspezifisch. Bei größeren Fenstern verschlechtert sich die äußere Reserve, weitere Primporte werden aktiv, und die hier bewiesenen Konstanten dürfen nicht weiterverwendet werden.

Der nächste konkrete Hebel ist, die variable Knotenfunktion rho_I und die nahtverträgliche regionale Energie in einem größeren verbundenen Fenster gemeinsam zu behalten. Falls zusätzliche niedrige Moden einer Unterform negativ werden, dürfen sie nicht als zusätzliche NULLPOL-Bedingungen gestrichen werden. Sie müssen als tatsächliche Freiheitsgrade einschließlich ihrer Kopplung im Restproblem bleiben. C15 ist eine zulässige Schnittstelle für diese weitere Aufgabe, keine vorweggenommene Lösung.

## 10. Tatsächlich ausgeführte kleine Checks und Quellen

`check_connected_constants.py` benutzt ausschließlich Python-Standardbibliothek und exakte Brüche. Es wurden **40 skalare bzw. polynomiale Algebra-Prüfungen** ausgeführt. Darin sind 13 endliche Regressionsfälle für A_0P_n=H_nP_n (n=0,...,12); der Beweis für alle n steht in §4 und wird nicht durch diese Fälle ersetzt. Die übrigen Prüfungen sichern die rationalen Taylor-/Logarithmus-, Moment- und Reservebudgets.

Keine numerische Matrixfaktorisierung, keine A1-Dateien, kein CI-Lauf, keine externe Freigabe. Der Hilbertraum-, Domain-, unendliche Reihen- und Positivitätsnachweis ist der analytische Text, nicht allein die Checkzahl.

### Quelltrennung

**Importierte Projektdaten:**
- [COMMON-JUMP, fester Modellanker](https://github.com/Waschtl904/objekt-x-programm/blob/ac164bbbd2c46623aa64e567d21f813f41f164b0/audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md).
- [C0 und Felddefinition](https://github.com/Waschtl904/objekt-x-programm/blob/d7b32ccfb9d0d90f19d4a7a5b0fbd19b0928f257/X_CANDIDATE_C0_SPEC.md).
- [Sparse-Graph SG1--SG4, exakt gelesener Anker](https://github.com/Waschtl904/objekt-x-programm/blob/192f443b4f1a26772e6c7d9d55fbf524ff1ee728/research/x-c1/X_C1_SPARSE_GRAPH_READOUT.md).
- [Dreizellen-/Nahtquelle](https://github.com/Waschtl904/objekt-x-programm/blob/4871a5343a996be49e66a565d1e232b2ecd38f54/research/x-c1/X_C1_THREE_CELLS_AND_INTERFACE.md), insbesondere I3--I5.

**Klassischer Kontext, keine Prüfung der neuen Projektaussagen:**
- [DLMF 18.3](https://dlmf.nist.gov/18.3): Legendre-Orthogonalität/Normierung.
- [DLMF 4.6](https://dlmf.nist.gov/4.6): klassische Reihen für Logarithmus und Binomialpotenzen.
- [Chen--Weth, The Dirichlet Problem for the Logarithmic Laplacian, arXiv:1710.03416](https://arxiv.org/abs/1710.03416): logarithmische nichtlokale Energie als allgemeiner Kontext. Der regionale Operator C6 wird hier selbst hergeleitet und nicht mit dem Ganzraum-Dirichletoperator der Publikation identifiziert.

**Neue Autorenableitung dieser Runde:** C3--C15 mit den konkreten Zahlen, Domains, Output und Geltungsgrenzen. Kein externer Review oder Literatur-Neuheitsanspruch.
