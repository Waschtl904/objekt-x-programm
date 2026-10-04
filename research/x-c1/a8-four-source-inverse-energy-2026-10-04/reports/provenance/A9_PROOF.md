# Zweite Kammer: neuer vollständiger Tail und Reduktion am Terminal A₉

27. September 2026 · **Lokale Herleitung / EXTERNAL_REVIEW_OPEN**

Forschungsgate: **SECOND-CHAMBER TERMINAL POSITIVITY**.
Terminal `A9=log(3)`. Die volle Terminalpositivität bleibt offen.

## Ergebnis

Für die konkrete gekoppelte C1a-Familie, die ursprünglichen zwei
Mellinbedingungen und

\[
A_8=\tfrac12\log8\le A\le A_9=\log3
\]

besitzt der unten definierte **vollständige hohe Formraum** in beiden
Paritäten die physische Reserve

\[
\boxed{q_A[u]\ge\tfrac23\|u\|_2^2.}
\tag{1}
\]

Seine Kodimension im vollständigen Quellenformraum beträgt **296 je Parität**.
Die hohen rohen Legendregrade beginnen bei 594 bzw. 595. Diese Zahl folgt aus
den neuen Verlustschranken; eine minimale notwendige Dimension wird nicht
behauptet. Im hohen T-Bildraum liefert (1) die Defektreserve **1/19**.

Die bisherigen 191 Koordinaten erlauben mit derselben neu gerechneten
Abschätzung immerhin einen hohen physischen Boden **1/5**. Der alte Boden
2/3 ist damit für diesen unveränderten Schnitt nicht erneut bewiesen.
Ein kleinerer hinreichender Boden ist kein negativer Formbefund.

Noch offen sind die beiden niedrigen Schurreste am Terminal A9 einschließlich
der vollständigen hohen Antwort. Es wurde keine positive volle Terminalreserve
bei A9 berechnet oder aus O8 übernommen.

## 1. Eingaben und neue Kammerdaten

Die unveränderte allgemeine Formidentität stammt aus dem
[Universal-Prime-Power-Beweis](https://github.com/Waschtl904/objekt-x-programm/blob/876f9c79d555019217c745923cae3bef5da8af17/research/x-c1/universal-prime-power-family-2026-09-18/PROOF.md).
Auf `H=L²((-1,1),dx/2)` und unter `U_Au(x)=sqrt(2A)u(Ax)` lautet sie

\[
Q_A=D_H+V+q_0(A)I-K_A-S_A,
\quad D_HP_n=H_nP_n,\quad V=-\tfrac12\log(1-x^2),
\quad q_0(A)=-\log(2\pi A)-\gamma.
\tag{2}
\]

Dabei bezeichnet `H_n=sum_{j=1}^n 1/j` die harmonische Zahl,

\[
k_{\rm reg}(t)=\frac{e^{-t/2}}{1-e^{-2t}}-\frac1{2t},\qquad
(K_Af)(x)=2A\int k_{\rm reg}(A|x-y|)f(y)\,d\mu(y),
\]

und `S_A=sum_q w_q T_{log(q)/A}`, `w_{p^k}=log(p)/sqrt(p^k)`.
`T_d` ist die Summe der beiden partiellen Translationen um `+d` und `-d`.
Die normierten Legendrepolynome sind `e_n=sqrt(2n+1)P_n`; Normierung und
Orthogonalität entsprechen [DLMF §18.3](https://dlmf.nist.gov/18.3).

Bei A8 gilt noch `Q_-={2,3,4,5,7}`. Für `A8<A<=A9` gilt
`Q_+={2,3,4,5,7,8}`; bei A9 bleibt 9 inaktiv. Der sechste Summand kann am
linken Endpunkt mitgeführt werden, weil dort `T_2=0` fast überall.

Wir verwenden den rationalen Hüllradius

\[
A_9<r:=11/10,\qquad A/2\le z_0:=11/20.
\tag{3}
\]

Die C1a-Skalarbindung `5<kappa<11/2`, `10<s_-<23/2` und
`w8=log(2)/sqrt(8)<1/4` ergeben auch hier `s_A=kappa+2omega_A<12`.
Die lokalen O10-Rohtransporte sind in der bytegleich beigefügten
[O10-Herleitung](inputs/O10_PROOF.md) dokumentiert. Der Tailnachweis unten
führt seine neuen Träger-, Kernel-, Shift- und Momentabschätzungen ausdrücklich
aus. Alle verwendeten Repository-Eingaben stehen in `SOURCE_BINDINGS.json`.

## 2. Neuer Shiftverlust: q=2 hat jetzt Viererketten

In physischen Koordinaten zerlege `(-A,A)` nach den Restklassen modulo
`ell_q=log(q)`. Die Isometrie

\[
f\longmapsto \{f(-A+t+j\ell_q)\}_j,\qquad 0<t<\ell_q,
\]

mit genau den in `(-A,A)` liegenden Knoten realisiert `T_{ell_q/A}` als
direktes Integral endlicher Pfad-Adjazenzmatrizen. Die L²-Norm ist das Integral
der Summen der Knotenbeträge; Nachbarknoten werden durch die Translation
verbunden. Damit ist die Operatornorm durch die größte auftretende Pfadnorm
beschränkt.

Für q=2 gelten `3log(2)<=2A<=log(9)<4log(2)`. Die Ketten haben fast überall
höchstens vier Knoten. Bei A8 gibt es fast überall höchstens drei; für jedes
`A>A8` treten Viererketten auf einer Menge positiver Länge auf.
Die Pfadmatrizen besitzen die charakteristischen Polynome

\[
p_1(\lambda)=\lambda,\quad p_2=\lambda^2-1,\quad
p_3=\lambda^3-2\lambda,\quad p_4=\lambda^4-3\lambda^2+1.
\]

Ihre größte Norm bis zur Länge 4 ist

\[
\varphi=\sqrt{(3+\sqrt5)/2}=(1+\sqrt5)/2.
\tag{4}
\]

Die alte Dreierkettennorm `sqrt(2)` darf rechts von A8 deshalb nicht für
den q=2-Operator weiterbenutzt werden.

Für q=3 gilt `2A<=2log(3)`: fast überall höchstens zwei Knoten, auch am
Gleichheitsendpunkt A9. Für q=4,5,7,8 ist `log(q)/A>1`, also ebenfalls
Norm höchstens 1. Am linken Endpunkt ist der q=8-Operator null.
Folglich

\[
\|S_A\|\le
\varphi\frac{\log2}{\sqrt2}+
\frac{\log3}{\sqrt3}+\frac{\log2}{2}+
\frac{\log5}{\sqrt5}+\frac{\log7}{\sqrt7}+
\frac{\log2}{\sqrt8}
<\frac{139}{40}=3.475.
\tag{5}
\]

Alle sechs Gewichte und die neue Pfadnorm gehen in den rationalen Vergleich
ein. Insbesondere wird für 8 das Gewicht `log(2)/sqrt(8)` verwendet.
Es handelt sich um eine Normschranke für die Summe der tatsächlichen
Shiftoperatoren; eine positive Zerlegung in unabhängige Prime-Grams folgt
daraus nicht.

## 3. Regulärer Gamma-Kern auf dem größeren Intervall

Für `z=t/2` gilt weiterhin die exakte Identität

\[
k_{\rm reg}(2z)=\tfrac14(\operatorname{sech}z+
\operatorname{csch}z-1/z).
\tag{6}
\]

Aus `sinh(z)>=z`, `sech(z)<=1` folgt die obere Schranke 1/4.
Für die untere Schranke setze

\[
B_r=\sum_{j=0}^{20}\frac{r^{2j}}{(2j+3)!}
+\frac{r^{42}}{45!\,[1-r^2/(46\cdot47)]}.
\]

Dann gilt für `0<z<=r` mit `S(z)=sinh(z)/z`

\[
\frac{S(z)-1}{z^2}\le B_r,\quad S(z)\ge1+z^2/6,
\quad \frac1z-\operatorname{csch}z
\le\frac{zB_r}{1+z^2/6}\le\frac{rB_r}{1+r^2/6}.
\]

Der letzte Ausdruck benutzt die Monotonie von `z/(1+z²/6)` für `z²<6`.
Für eine rationale obere Taylor-Einschließung `C_r` von `cosh(r)` folgt

\[
k_{\rm reg}(2z)\ge\frac14\left(C_r^{-1}
-\frac{rB_r}{1+r^2/6}\right)>\frac{109}{1000}.
\tag{7}
\]

Bei Null ist der Grenzwert 1/4. Somit gelten die Schranken auf dem gesamten
benötigten Intervall `0<=t<=2A<=11/5`, ohne eine unbewiesene Monotonie
des regulären Gamma-Kerns zu verwenden.

Der Schurtest liefert `||K_A||<=r/2=11/20`. Für `y orthogonal P_0`
verschwindet der konstante Kern 1/4 in der quadratischen Form. Nach Abzug
dieses Rang-eins-Operators erhält man

\[
|\langle y,K_Ay\rangle|
\le2r(1/4-109/1000)\|y\|^2
=\frac{1551}{5000}\|y\|^2.
\tag{8}
\]

Der volle Gamma-Trägerbound `Gamma[u]>=4e^{-A}||u||²>=4/3||u||²`
bleibt nützlich für den T-Isomorphismus. Allein bezahlt er jedoch weder die
Prime-Verluste noch den konstanten Formterm. Für den hohen Raum wird deshalb
die harmonische Diagonale in (2) zusammen mit (5) und (8) verwendet.

## 4. Roher Tail und genaue Bezahlung der Mellinkorrektur

Rationale Reihenzeugen geben

\[
\gamma<H_{8192}-13\log2<5773/10000,\quad
\log(2\pi A)+\gamma<2511/1000.
\tag{9}
\]

Für pi genügt `pi<22/7`; für A wird (3) eingesetzt.
Da `V>=0`, folgt für jeden Formvektor y mit Legendregraden mindestens N
und `y orthogonal P_0`

\[
q_A[y]\ge\left(H_N-
\frac{2511}{1000}-\frac{1551}{5000}-\frac{139}{40}\right)\|y\|^2
=\left(H_N-\frac{31481}{5000}\right)\|y\|^2.
\tag{10}
\]

Vor der Momentkorrektur bezeichnet q dieselbe Form ohne Polterme auf dem
Referenzformraum. Die physisch zulässige Zwei-Mellin-Quelle wird jetzt
rekonstruiert.

Für die Parität p=0,1 sei `e=e_p`,
`m_0(x)=cosh(Ax/2)`, `m_1(x)=sinh(Ax/2)` und

\[
M_{p,A}y=y-e\frac{\langle m_p,y\rangle}{\langle m_p,e\rangle}
\qquad(y\perp e).
\tag{11}
\]

Die Paarung ist im zweiten Argument linear. Für hohen Anfangsgrad `n=N+p`
folgen aus der Orthogonalität zu sämtlichen niedrigeren Monomen

\[
\|M_{p,A}y-y\|\le\epsilon_{p,N}\|y\|,\quad
\epsilon_{p,N}:=
\frac{z_0^{N+p}}{(N+p)!\,[1-z_0^2/((N+p+1)(N+p+2))]}
\begin{cases}1,&p=0,\\4,&p=1.\end{cases}
\tag{12}
\]

Der gerade Trägermomentnenner ist mindestens 1. Für den normierten ungeraden
Träger ist er mindestens `z/sqrt(3)` bei `z=A/2>=1/2`; sein inverser Faktor
ist kleiner als 4. Genau die ursprünglichen Momente werden korrigiert.

Auch die Mischkosten werden neu bezahlt. Auf `[0,1)` gilt
`0<=V(x)<=-log(1-x)/2`, also `||V||²<=1/2`. Wegen `e_0=1`, `e_1=sqrt(3)x`
ist `||Ve_p||<2` für beide normierten Träger. Daraus folgen

\[
|q_A(y,e_p)|<(2+11/20+139/40)\|y\|<7\|y\|,
\]
\[
\|Q_Ae_p\|<1+2+2511/1000+11/20+139/40<10.
\tag{13}
\]

Im ersten Vergleich verschwinden die D_H- und q0-Mischterme durch
Orthogonalität. Die logarithmische Multiplikatorfunktion V wird dabei
**nur auf den beiden Trägerpolynomen** in L² abgeschätzt.

Für `epsilon=max_p epsilon_{p,N}` ergeben (10)–(13)

\[
q_A[M_{p,A}y]\ge
\left(H_N-31481/5000-14\epsilon-10\epsilon^2\right)\|y\|^2,
\quad \|M_{p,A}y\|^2\le(1+\epsilon^2)\|y\|^2.
\tag{14}
\]

Für N=594 gilt exakt `H_594>69649/10000` und
`epsilon_{p,594}<10^(-6)` in beiden Paritäten. Folglich

\[
\frac{6687}{10000}-14\cdot10^{-6}-10\cdot10^{-12}
>\frac23(1+10^{-12}).
\tag{15}
\]

Dies beweist (1). Die tatsächlichen rationalen Momentreste aus (12) sind
wesentlich kleiner als `10^(-6)`; ein späteres Schur-Fehlerbudget verwendet
diese tatsächlichen Reste, nicht die grobe Demonstrationsschranke.

### Vergleich neu geprüfter Schnitte

Die folgende Tabelle verwendet stets die neuen sechs-Kanal-Verluste.

| Hoher gerader/ungerader Anfangsgrad | Niedrige Koordinaten je Parität | Bewiesener physischer High-Floor | Hohe Defektreserve mit s<12 |
| --- | ---: | ---: | ---: |
| 384 / 385 | 191 | 1/5 | 1/61 |
| 502 / 503 | 250 | 1/2 | 1/25 |
| **594 / 595** | **296** | **2/3** | **1/19** |
| 646 / 647 | 322 | 3/4 | 1/17 |

296 ist eine hinreichende Wahl für die weitere Rechnung. Ein kleinerer
Schnitt kann bei schärferen Abschätzungen ebenfalls genügen; die Tabelle
behauptet keine notwendige spektrale Dimension und keine positiven Low-Blöcke.

## 5. Vollständige Formdomäne und Kodimension 296

Sei `G` die volle Gamma-Formdomäne mit Norm `integral(1+g)|uhat|²`.
Da `s_A<12`, sind auf dem deklarierten Quellenraum diese Norm und
`q_A+17||.||²` äquivalent. Für jedes A im betrachteten Bereich gilt

\[
F_A=\{u\in G:\operatorname{supp}u\subset[-A,A],\ E_+u=E_-u=0\}.
\tag{16}
\]

Hier wird derselbe Dichteschritt wie im gebundenen O8-Beweis erneut auf
diesem Bereich begründet. Die rechte Seite ist unter der Gamma-Norm
abgeschlossen. Für die umgekehrte Inklusion schrumpfe eine Quelle durch
`u_r(x)=r^(-1/2)u(x/r)`, `r<1`, ins Intervallinnere. Jeder Summand der
Gamma-Reihe erfüllt `g(t xi)<=max(1,t²)g(xi)`; deshalb sind diese Dilatationen
nahe 1 gleichmäßig beschränkt und konvergieren stark in G, zunächst auf
glatten kompakten Fourierfunktionen und dann durch Dichte auf ganz G.

Die Momentfehler gehen durch L²-Konvergenz auf festem kompaktem Träger gegen
null. Sie werden durch zwei feste glatte Innenfunktionen mit invertierbarer
Momentmatrix korrigiert; in einer Parität genügt eine passende Funktion.
Anschließende Faltung mit einem kleinen glatten geraden Mollifier erhält
die Nullmomente, weil `E_pm(f*rho)=E_pm(f)E_pm(rho)`, und konvergiert in G.
Die korrigierten Träger bleiben im Inneren. Damit werden wirkliche glatte
H¹₀-Quellen approximiert, ohne zusätzliche Randbedingungen zu verlangen.

Die Gamma-Zerlegung (2) gilt auf der abgeschlossenen Formdomäne: D_H und V
sind nichtnegative geschlossene Formanteile, K_A und S_A beschränkt. Die
Integralidentität erstreckt sich durch Tonelli und Formabschluss. Insbesondere
liegt jedes nullfortgesetzte Polynom in der Formdomäne, denn seine
Translationsinkremente haben Normquadrat `O(min(r,1))`; der Gamma-Kern ist
nahe Null `O(1/r)` und im Fernbereich integrierbar.

Fixiere N=594 und p=0,1. Die niedrigen Indizes sind

\[
I_0=\{2,4,\ldots,592\},\qquad I_1=\{3,5,\ldots,593\}.
\tag{17}
\]

Dies sind jeweils 296 stetige L²-Koordinaten auf `F_A^p`. Ihr gemeinsamer
Kern ist im Quellenformraum abgeschlossen. Die Vertreter
`U_A^(-1)M_{p,A}e_n`, `n in I_p`, haben die Identität als niedrige
Koordinatenmatrix; sie liegen nach (16) in `F_A^p`.
Die Koordinatenabbildung ist daher surjektiv und ihr Kern hat **genau
Kodimension 296**.

Umgekehrt ist jeder Vektor in diesem Kern eindeutig `U_A^(-1)M_{p,A}y`,
wobei y aus den rohen Graden 594,596,... bzw. 595,597,... besteht und in der
Formdomäne liegt. Dazu wird lediglich der Momentträger abgezogen; die
Mellinbedingung bestimmt seinen Koeffizienten. Endliche Subtraktionen von
Formpolynomen erhalten die Domäne. (14) gilt somit für den vollständigen
unendlichen hohen Raum, nicht nur für eine polynomiale Testklasse.

## 6. Hohe Defektreserve und noch offener Schurrest

Der Gamma-Trägerbound bis A9 liefert wie in O10
`||T_Au||²>=2/15 ||u||²` und `||D_Au||²<=12||u||²`.
Zusammen mit
`||T_Au||² <= ||u||_(A,17)² <= (257/2)||T_Au||²`
ist T ein beschränkter Isomorphismus der vollständigen Quellen auf ihren
abgeschlossenen T-Bildraum. R mit `D=RT` ist beschränkt, `||R||<=sqrt(90)`.
Diese Beschränktheit benutzt noch keine volle Formpositivität.

Auf dem hohen Quellenraum liefert (1)

\[
\|D_Au\|^2\le18q_A[u],\qquad
\|T_Au\|^2=q_A[u]+\|D_Au\|^2\le19q_A[u].
\tag{18}
\]

Der hohe T-Bildraum ist abgeschlossen und hat Kodimension 296. Für die
orthogonale Zerlegung in niedrige und hohe T-Koordinaten schreibe

\[
R_A^*R_A=\begin{pmatrix}\alpha&\beta^*\\\beta&K\end{pmatrix},
\qquad0\le K\le\tfrac{18}{19}I.
\]

Damit ist `I-K` invertierbar. Der tatsächliche noch offene niedrige Schurrest
lautet

\[
\boxed{S_A=I-\alpha-\beta^*(I-K)^{-1}\beta.}
\tag{19}
\]

Ein positiver niedriger Hauptblock allein ersetzt (19) nicht. Der Operator
enthält die gesamte unendliche hohe Antwort. Ein nachgewiesener Boden
`S_A>=sigma I>0` würde mit der hohen Defektreserve 1/19 die volle Reserve
liefern, etwa

\[
\eta_A\ge\frac{\min(\sigma,1/19)}
{(1+\|(I-K)^{-1}\beta\|)^2}>0.
\tag{20}
\]

## 7. Vorbereitung einer vollständig bezahlten physischen Schur-Untermatrix

Eine konkrete Rechnung kann erneut mit physischen Legendrekoordinaten
arbeiten, muss aber alle A9-Daten neu bilden. Setze `Z=ME`, wobei E die
296 niedrigen normierten Koordinaten einbettet, und schreibe jede Quelle als
`u=U_A^(-1)M(Ec+y)`.
Für `A/2<=11/20` gilt `||M||<=2`: im geraden Sektor genügt
`cosh(11/20)-1`, im ungeraden die Schranke

\[
\frac{z_0^2}{3(1-z_0^2/20)}
\]

für den Quotienten aus orthogonaler Momentkomponente und Trägermoment.
In beiden Fällen ist 1 plus dessen Quadrat kleiner als 4.

Definiere `L=Z*QZ` und die tatsächliche vollständige Low/High-Kopplung
`B=Z*Q M|_Y`. Aus (1) folgt

\[
q_A[u]\ge c^*Lc+2\operatorname{Re}\langle c,By\rangle+
\delta\|y\|^2,\qquad\delta=2/3.
\tag{21}
\]

Die normierten niedrigen Polynome liegen in der Operatordomäne von Q:
V mal ein Polynom ist L², D_H ist auf ihnen endlich und K_A,S_A sind
beschränkt. Daher ist B bezüglich der hohen L²-Norm beschränkt.

### Neuer Gamma-Modellradius

Die rationalen inversen Taylorpolynome von `cosh(z)` und `sinh(z)/z`
ergeben wie zuvor ein Polynom `p_M(z)` für `k_reg(2z)`.
Die endlichen Residuen werden exakt multipliziert; das Residuum von
`sinh(z)/z` wird **vor** der Majorisierung durch z dividiert. Explizite
Fakultätsreste bezahlen die abgeschnittenen Nennerreihen. Beide wirklichen
Nenner sind mindestens 1.

Die neu berechneten Majoranten auf `0<=z<=11/10` sind:

| Polynomgrad M | Kernel-Fehlerobergrenze, gerundete Anzeige | Operator-Fehlerobergrenze, gerundete Anzeige |
| --- | ---: | ---: |
| 160 | 3.063e-26 | 6.738e-26 |
| 192 | 3.427e-31 | 7.538e-31 |
| **224** | **3.833e-36** | **8.433e-36** |

Die gespeicherten exakten rationalen Werte sind maßgeblich. Für M=224 darf
bequem `epsilon_K=4/10^36` und
`gamma_K=(11/5)epsilon_K` verwendet werden. Das ist nur die Kernel-/Operator-
Approximation, noch kein vollständiges Matrixbudget oder Low-Zertifikat.

Für `Q^P=D_H+V+q0-K_A^P-S_A` setze `L0=Z*Q^P Z`,
`B0=Z*Q^P|_Y` und `G0=B0 B0*`. Dann gelten neu

\[
e_L=4\gamma_K,\qquad
\|L-L_0\|\le e_L,\qquad
\|B-B_0\|\le e_{B,p}:=2\gamma_K+20\epsilon_{p,594}.
\tag{22}
\]

Der zweite Term bezahlt die hohe Momentkorrektur mit dem tatsächlichen
`||Qe_p||<10` aus (13). Die niedrigen Momente, Integral- und Arithmetikfehler
müssen zusätzlich durch die späteren Matrixintervalle eingeschlossen werden.
Mit `tau=1/1000` folgt

\[
BB^*\le H_p^{up}:=\tfrac{1001}{1000}G_0+1001e_{B,p}^2 I,
\qquad F_p:=L_0-e_LI-\tfrac32 H_p^{up}.
\tag{23}
\]

Ein gerichteter Nachweis `F_p>=sigma_p I>0` wäre hinreichend. Mit
`b_p²>=||B||²`, etwa `b_p²=tr(H_p^{up})`, ergäbe sich dann

\[
c_{{phys},p}=\frac{\min(\sigma_p,2/3)}{4(1+3b_p/2)^2},\qquad
\eta_{A,p}\ge\frac{c_{{phys},p}}{c_{{phys},p}+12}.
\tag{24}
\]

Das ist die vollständige Norm-/Shear-Umrechnung für diesen neuen Schnitt.
Eine fehlgeschlagene Prüfung von F_p wäre zunächst ein Befund gegen diese
hinreichende Einschließung, kein Nachweis einer negativen tatsächlichen Quelle.

### Neue A9-Geometrie für die spätere Engine

Am Endpunkt gelten exakt `d3=1`, `d4=2d2`, `d8=3d2` mit `d2=log2/log3`.
Die positiven Teilungsgrenzen der Shiftaktionen sind

\[
0<d_4-1<1-d_2<d_5-1<d_7-1<d_8-1<1.
\tag{25}
\]

Ihre Reihenfolge folgt aus
`1<4/3<3/2<5/3<7/3<8/3<3` nach Anwendung von log und Division durch log3.
Es gibt **sechs** positive Zellen. Die bei A8 zusammenfallenden q=2/q=4-
Grenzen sind hier getrennt; die q=3-Grenze liegt exakt bei Null.
Die speziellen A8-Grenzbehandlungen dürfen nicht kopiert werden.

Für N=594 werden rohe Grade `0,...,593` benötigt. Mit M=224 reicht der
polynomiale Gamma-Support bis höchstens `593+224+1=818`. Dies begrenzt nur
den Modellpolynomanteil. G0 muss weiterhin über die vollständigen V²-, S²-,
V/S-, Gamma/V- und Gamma/Shift-Grams mit Parseval-Abzug des gesamten
niedrigen rohen Raums berechnet werden. Eine endliche hohe Trunkierung
ersetzt die vollständige hohe Antwort nicht.

## 8. Bedingte Konsequenz einer späteren A9-Terminalreserve

Erst wenn beide Paritäten in (23) positiv zertifiziert sind, liefert ihr
Minimum einen physischen Boden `c>0` am Terminal A9. Physische Nullfortsetzung
und die O10-Formnaturality geben dann `q_A[u]>=c||u||²` für alle
`1<=A<=A9`. Weil `s_A<12`, folgt auf jedem gesamten Carrier der Boden
`G_A>=c/(c+12) I`.

Alternativ überträgt reine G-Kompression einen gegebenen Endpunktboden
innerhalb der zweiten Kammer unverändert und links über die Wand mindestens
mit Faktor `20/21`. Über die Wand darf die rohe T-Isometrie nicht stillschweigend
benutzt werden.

Mit wirklich bewiesenen positiven invertierbaren `Delta_A=G_A^(1/2)` wäre
anschließend

\[
U^X_{A,B}=\Delta_B M^T_{A,B}\Delta_A^{-1}
\]

ein isometrischer Transport: O10 liefert
`(M^T)^*G_B M^T=G_A`, und die beiden mittleren Quadratwurzeln heben sich im
Cocycle auf. Das ist eine bedingte Folgerung, kein schon ausgeführter
positiver Abschluss der zweiten Kammer.

## 9. Status und ausgeführte Prüfungen

Der vollständige High-Floor, seine Mellinrekonstruktion und die Kodimension
296 sind lokal analytisch hergeleitet. `check_tail.py` prüft die rationalen
Konstanten, die Pfadpolynome, die Endpunktgeometrie, die Momentreste und die
Gamma-Residualbudgets mit exakter Arithmetik. Er berechnet keine niedrigen
Terminalmatrizen und entscheidet nicht über (19) oder (23).

**SECOND-CHAMBER TERMINAL POSITIVITY bleibt offen.** Externe analytische
Prüfung bleibt offen. O10 bleibt ein eigener Rohtransportsatz. Die
Repository-Registry und Main wurden durch dieses lokale Paket nicht geändert.
Ein positiver Abschluss bis A9 wäre weiterhin ein beschränkter lokaler
C1-Abschluss, keine Konstruktion des globalen Objekts X und kein RH-Beweis.
