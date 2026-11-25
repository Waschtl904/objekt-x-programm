# Zwei ungerade Richtungen zusammen mit dem ganzen Hochraum

Auf der Basis von [36d6fec](https://github.com/Waschtl904/objekt-x-programm/tree/36d6fec7966a802ee6a2084a66a8224f48247093) gilt unter den geerbten Form- und Quellenidentifikationen für die dortige Vergleichsform
\[
  \mathfrak S_* >0\quad\text{auf}\quad \operatorname{span}\{e_o,s\}+Y_o .
\]
Der Schurrest nach Elimination von **ganz** \(Y_o\) hat in den zwei veröffentlichten Testkoordinaten eine Determinante größer als \(2.97146\,10^{-11}\). Dies ist eine Autorenherleitung. Der vorliegende Nachweis betrifft diesen Summenraum.

## Physische Kernkoordinaten

Wir verwenden die Intervalle \((0,c),(c,a),(a,b)\), \(c=3\log(2)/2,\ a=\log3,\ b=\log(11)/2,\ g=a-c,\ h=b-a\), mit physischer Norm für \(2\,dx\) und ungerader Fortsetzung. \(y\in Y_o,\ \|y\|=1\). Auf diesem Raum ist \(W[y]=1\). Alle Nullbedingungen stehen in [§3 des Hochblockbeweises](../../research/x-c1/a9-a11-hochblock-2026-11-23/A9-A11-Randkopplung-und-Hochblock-2026-11-23.md). Schreibe \(h_y=B_{cn}y,\ \delta=1.8219,\ d=1.84298\). Es gilt \(\|h_y\|<2,\ U_8 h_y=h_y/\delta\). Für \(z=B_{on}y-\delta^{-1}B_{co}^*h_y\) gilt \(\|z\|<2.726,\ z\perp\mathcal P_{4095}(c,a)\). Ebenso gilt \(y\perp\mathcal P_{4095}(a,b)\).

Auf dem alten Kern lautet die physische Momentkarte in orthonormalen Legendrekoordinaten \(M(u,v)=(-c_L^*u-c_H^*v,u,v)\). Hier bezeichnet die erste Stelle den Träger Grad 1, die zweite die Grade 3 bis 383, die dritte alle höheren ungeraden Grade. Die \(c\)-Vektoren sind die Momentkoeffizienten geteilt durch den Trägerkoeffizienten. Für den alten Inversvergleich gilt \(U_8=M A_{\mathrm{eff},0}^{-1}M^*\); für die stärkere Kernunterform gilt entsprechend \(U_*=M A_*^{-1} M^*\). Die Koordinatenblöcke haben denselben tatsächlichen Kreuzblock \(B\) und hohe Diagonalen \(\delta I,dI\). [Kernvergleich](../a9-a11-ungerader-kernvergleich-2026-11-25/README.md) · [Momentkarte und ganze Kopplung](../../research/x-c1/first-chamber-o8-o9-2026-09-27/o8-rechenstand/PROOF.md)

Für den physischen Vektor \(h_y=(k,u,v)=M(u,v)\) ergibt Multiplikation von \(U_8 h_y=h_y/\delta\) mit den Koordinatenabbildungen \(A_{\mathrm{eff},0}(u,v)=\delta M^*h_y\). Also \(B^*u=-\delta c_H k\). Für \(\phi=M(u,0)\) ist \(B^*u\) die hohe Koeffizientenfolge der rohen Kernwirkung \(Q_c\phi\) abzüglich des Beitrags ihres Trägers mal \(c_H\). Somit stimmen alle hohen Koeffizienten von \(Q_c\phi\) mit denen eines Vielfachen von \(m(t)=\sinh(t/2)\) überein. Das würde \(Q_c\phi\) als Summe aus einem Polynom vom Grad höchstens 383 und einem Vielfachen von \(m\) darstellen. Am rechten Rand ist die rohe Wirkung aber eine reell analytische Funktion plus \(-\phi(t)\log(c-t)/2\). Das folgt aus Polynomdivision beim singulären Differenzenintegral. Der reguläre Kern lässt sich nach Teilung der Integration bei \(t\) analytisch bis zum Rand fortsetzen. Alle Primtranslationen sind auf dem letzten offenen Teilintervall Polynome. Jede endliche Nullstellenordnung eines nichtverschwindenden \(\phi\) hinterlässt eine logarithmisch divergierende Ableitung. Folglich \(\phi=0,\ u=0\). Weil \(m\) kein Polynom ist, ist \(c_H\ne0\), also \(k=0\). Die niedrige Blockgleichung liefert \(Bv=0\), und die Momentgleichung liefert \(c_H^*v=0\).

Es folgen drei exakte Eigenschaften. \(h_y\) annihiliert alle ungeraden Polynome bis Grad 383, es annihiliert \(Q_c M(u',0)\) für jedes \(u'\), und \(U_*h_y=h_y/d\). Die zusätzliche Paarung mit \(Q_cm\) ist durch die definierende \(u_m\)-Bedingung null. Für die in der [Randtermnotiz, §4](../a9-a11-hochraum-randterm-2026-11-25/) festgelegten Antworten folgt daher
\[
 T_i(y)=d^{-1}\langle h_y,h_i\rangle+
 (1-\delta/d)\langle Ry,V_{\mathrm{Schale},i}\rangle .
\]
Hier bezeichnet \(V_{\mathrm{Schale},i}\) den physischen alten Test zu den eingefrorenen 96 Koordinaten mit freier Kernkoordinate null. Denn aus \(v(y)=J^*\nu(y)=0\) folgt \(\langle Ry,V_{\mathrm{Schale},i}\rangle=\delta^{-1}\langle h_y,g v_i\rangle\). Insbesondere muss man am Kern zwischen Momentkarte, Adjungierter und inverser Koordinatenabbildung unterscheiden.

## Der Kontaktlogarithmus auf dem eingeschränkten Raum

Setze \(u=(x-a)/h,\ \theta=h/a\). Der Projektor auf die neuen Grade ab \(N=4096\) heißt \(E_N\). Die geerbte Antwort ist \(P=\Phi X\widehat F\). Die Spalten von \(\Phi\) sind unabhängig, der Prüfer invertiert \(X\) exakt im Sinne eines Determinantentests. Also \(\widehat F y=0\). Die zwölf Modellzeilen haben in der physischen Paarung die Gestalt Polynom vom Grad höchstens 320 plus Momentterm plus
\[
 \ell_j(1+\theta u)\big[-\log u+\log(2/\theta)+\log(1+\theta u/2)\big]
\]
mit einem gemeinsamen, von null verschiedenen Normierungsfaktor. Die Paarungen von Polynom und Moment sind null. Die zwölf rationalen Polynome \(\ell_j\) stammen aus dem Feld log_ratio_multiplier. Die ersten zwölf Taylorzeilen von \(\ell_j(1+t)\) bilden eine invertierbare rationale Matrix. Nach Multiplikation mit ihrer Inversen sind die ersten zwölf Zeilen die Einheitsmatrix. Die weiteren Zeilen \(B_{rk}\) werden vollständig mitgeführt. [Funktionen und physische Metrik](../../research/x-c1/a9-inverse-spike-calibration-2026-10-15/)

Für ein Polynom \(p(u)=\sum a_k u^k\) kann man damit seine ersten zwölf Taylorstellen im Faktor vor \(\log u\) entfernen. Der Betrag des neuen Koeffizienten in Grad \(r\ge12\) ist höchstens \(|a_r|+\sum_{k<12}|a_k B_{rk}|\theta^{r-k}\). Für den analytischen Zusatz \(\log(1+\theta u/2)\) genügt das Taylorpolynom vom Grad 3999, sein Rest ist kleiner als \(19^{-4000}\). Alle Polynomprodukte bleiben unter Grad 4096. Für den logarithmischen Rest gilt nach der vollständigen Legendre-Rechnung des Elternbelegs
\[
 \|E_N(u^k\log u)\|\le N^{-1}\prod_{j=1}^k j^2/[(N-j)(N+1+j)] .
\]
Für jedes alte Schalenpolynom \(w\) vom Grad höchstens 95 und physischer Norm eins erfüllt \(p(u)=\sqrt{2h}\,w(a+hu)\) die Schranke
\[
 |a_k|\le3000 {95\choose k}{95+k\choose k}(12/7)^k .
\]
Dies folgt aus der Entwicklung verschobener Legendrepolynome um das rechte Ende der alten Schale, aus \(h/g<12/7\) und Cauchy–Schwarz für die normierten Koeffizienten. Der Vorfaktor 3000 übersteigt \(\sqrt{h/g}\,96\). Der rationale Test summiert alle Beiträge. Die eingeschränkten Normen von \(p\log u\) und \(\log u\) liegen unter \(2.968\,10^{-37}\) und \(2.461\,10^{-80}\). Die beiden Sprunghöhen des Elternbelegs haben Betrag kleiner als 7.

## Der Schnitt beim neunten Primkanal

Der getrennte Gammaoperator \(G_{cn}\) erfüllt \(\|G_{cn}y\|<10^{-990}\). Als Funktion der neuen Variablen ist der Kern auf dem Kreis um \((a+b)/2\) vom Radius \(0.09\) holomorph. Dort haben beide Argumente des Kerns Realteil größer als \(0.018\). Aus \(k(t)=e^{-t/2}/(1-e^{-2t})\) folgt \(|k|<30\). Das Taylorpolynom vom Grad 4095 verschwindet in der Paarung mit \(y\); der Quotient ist kleiner als \(0.57\). Intervalllängen, zwei Flügel und geometrischer Rest sind durch \(200(0.57)^{4096}/(1-0.57)\) gedeckt. In umgekehrter Variablenrichtung hat \(G_{cn}i\) auf \([-c,c]\) eine ungerade Chebyshevnäherung vom Grad 383 mit physischem Fehler unter \(10^{-39}\). Auf der Bernsteinellipse \(\rho=1.3\) ist der Abstand in Realteil größer als \(0.02\); die geometrische Summe der ausgelassenen Koeffizienten ist kleiner als \(400\rho^{-384}/(1-\rho^{-1})\). Es gilt \(\|i\|_{\rm roh}\le1\).

Schreibe \(r=2a-b\). Betrachte auf \([r,c]\) entweder \(f(t)=\sqrt{2h}\,w(t)\) oder \(f(t)=q_i((a-t)/h)\), \(q_i(u)=\sqrt{2h}\,i(a+hu)\). Es gibt ein ungerades Polynom \(p\) vom Grad höchstens 383 mit \(\sup_{[r,c]}|f-p|<10^{-63}\), \(\sup_{[0,c]}|p|<10^{210}\). Entwickle \(f(\sqrt z)/\sqrt z\) um \(z_0=(c^2+r^2)/2\) bis Grad 191, setze \(z=t^2\) ein und multipliziere mit \(t\). Auf dem Kreis \(R=0.9\) gilt \(|\sqrt z|>0.3,\ |\sqrt z-c|<0.94\). Beide Legendreargumente haben Betrag unter 34. Für das neue Argument ist dies unmittelbar aus \(2(g+0.94)/h+1\) ersichtlich. Die Legendre-Rekursion gibt \(|P_j(\zeta)|\le(2|\zeta|+1)^j\). Mit \(\sqrt{h/g}\,96<3000\) liegt das Kreissupremum unter \(10^{185}\). Auf \([r,c]\) ist der Taylorquotient kleiner als 0.05, auf \([0,c]\) kleiner als 1.2. Die beiden geometrischen Grenzen werden gerichtet geprüft.

Wegen \(\langle h_y,p\rangle=0\) folgt \(|\langle D_{cn}y,p\rangle|\le\|p\|\|G_{cn}y\|\). Die ersten sechs Primtranslationen eines solchen Kernpolynoms bedecken den ganzen neuen Flügel. Ihre Paarungen verschwinden, weil die übersetzten ungeraden Polynome dort Grad höchstens 383 haben. Der einzige verbleibende Term ist die Reflexion \(t=2a-x\) des Kanals \(q=9\) auf \(r<t<c\) mit Gewicht \(\log(3)/3>0.3\). Nach Rückkehr zum Maß \(du\) sind alle konstanten Umrechnungsfaktoren kleiner als 10. Ersetzen von \(p\) durch \(f\) bezahlt die obige uniforme Näherung. Das abgeschnittene \(f(2a-x)\) kostet deshalb in der eingeschränkten Dualnorm weniger als \(10^{-60}\). Das komplementäre Stück hat dieselbe Schranke, da die vollständige Fortsetzung ein Polynom ist. Dies behandelt sowohl die alte Schalenreflexion als auch die gekappte Diagonale im Primgram.

## Beiträge der alten Antwort

Für alte Schalenpolynome vom Grad höchstens 95 gilt \(|\langle B_{on}y,w\rangle|<10^{-35}\|w\|\). Der einzige Primkanal steht im vorigen Abschnitt. Der singuläre Gammaanteil ist nach Polynomdivision ein Polynom plus \(w(x)\log((x-c)/(x-a))/2\) bis auf das gemeinsame Vorzeichen. Die Schranke für \(w(x)\log u\) steht oben. Für \(\log(x-c)\) hat die Reihe um die Mitte Quotient kleiner als \(0.47\). Grad 3999 genügt selbst nach Multiplikation mit dem fortgesetzten Polynom, dessen normiertes Supremum unter \(5\,10^{91}\) liegt. Beim regulären Kern \(k(t)-1/(2t)\) und beim Spiegelkern genügt Taylorentwicklung in der neuen Variablen mit Radius 0.2. Die Argumente des regulären Kerns liegen im Kreis \(|t|<0.5\), dort ist der an null hebbare Rest kleiner als 5 (auf \(|t|=0.5\) gilt \(|\sinh t|\ge 0.5-(\sinh(0.5)-0.5)\)). Der Spiegelkern hat Realteil des Arguments größer als 1. Der Fehler in der Paarung ist kleiner als \(100(0.26)^{4096}/(1-0.26)\). Hier wird das alte Polynom auf seiner eigenen Schale integriert.

Ein alter, stückweiser Test \(v=(v_c,v_o)\) aus den folgenden Konstruktionen hat auf dem Kern die Gestalt Polynom von Grad höchstens 25 plus Vielfaches von \(m\) und auf der Schale Polynom von Grad höchstens 95 plus Vielfaches von \(m\). Für seinen Kernanteil gilt \(\langle h_y,Q_c v_c\rangle=0\) bis auf einen explizit beliebig klein kontrollierbaren Momentpolynomrest. Der reine \(m\)-Term verschwindet exakt. Für den polynomialen Teil \(w_c\) subtrahiere \(k m_{383}\), das ungerade Taylorpolynom von \(m\) bis Grad 383, mit \(k=\langle m,w_c\rangle/\langle m,m_{383}\rangle\). Das verbleibende Polynom ist momentfrei und gehört zu \(M(u',0)\). Es gilt \(|k|<100\|w_c\|\), denn \(\|m\|_{2dx}>0.2\) und der Taylorfehler ist kleiner als \(10^{-800}\). Für den graphischen Fehler gilt ebenfalls \(\|Q_c(m-m_{383})\|<10^{-795}\). Tatsächlich sind Funktions- und Ableitungsfehler kleiner als \(5/380!\) auf dem ganzen Intervall; das singuläre Differenzenintegral ist durch Länge mal Ableitungsfehler beschränkt. Das Randpotential hat endliche \(L^2\)-Norm kleiner als 10, die übrigen beschränkten Integral-, Diagonal- und Translationsanteile kosten zusammen weniger als 100 mal die beiden Supremumsfehler. Dieselbe Taylorersetzung auf der alten Schale kann für den \(m\)-Term dort durch Grad 95 vorgenommen werden (Funktionsfehler kleiner als \(5/95!<10^{-146}\)). Die Grad-95-Schranke gilt auch für dieses Polynom.

Für die alte Schalenaktion gilt exakt \(\langle h_y,B_{co}v_o\rangle=\delta\langle B_{on}y-z,v_o\rangle\). Der polynomiale Anteil der \(z\)-Paarung ist null. Die Quelle \(h_i\) des tatsächlichen \(Ri\) ist in Paarung mit \(h_y\) somit \(B_{cn}i+Q_c v_c+B_{co}v_o\), wobei \(v\) der alte Anteil des Momentlifts minus \(Pi\) ist. Orthogonale Momentprojektionen der Quelle tragen nichts bei. Für \(V_{\mathrm{Schale},i}\) genügt die direkte Darstellung \(\langle Ry,V_{\mathrm{Schale},i}\rangle=\langle h_y,v_c\rangle+\langle B_{on}y,v_o\rangle\). Die Kernpaarung ist bei Polynomen und \(m\) null.

Für die Größen dieser festen Tests genügt die großzügige Schranke \(10^{18}\) je Polynomnorm und Momentkoeffizient. Für \(Pi\) folgt sie schon aus \(\|\Phi\|<20,\ \|X\|<4.4\,10^{11},\ \|\widehat F\|\le150\|\Phi\|+1\). Der erste Wert folgt aus orthonormalen Legendrekoordinaten und der Momentkarte mit Norm kleiner als 2. Der physische direkte Momentlift des normierten \(i\) hat Norm höchstens eins. Für die 96er-Tests liegt die euklidische Koeffizientennorm unter \(2.7\,10^8\). Die vier globalen momentkorrigierten Legendreprofile niedrigen Grades haben Norm unter 2, die 92 Schalenpolynome ebenfalls je Norm unter 2. Die Momentlifte dividieren durch \(\int_0^c m^2>0.02\). Diese Werte erlauben auch nach Cauchy–Schwarz in den 96 Koordinaten den genannten Betrag. [Definition der 96 alten Tests](../../research/x-c1/a8-a9-global-closure-2026-10-13/packages/objekt-x-direkte-restform-und-positiver-96er-block-2026-10-11/HERLEITUNG.txt)

## Verbleibende Reflexion und Abnahme

In \(\langle B_{cn}y,B_{cn}i\rangle\) kosten die Beiträge mit \(G_{cn}y\) oder \(\langle h_y,G_{cn}i\rangle\) zusammen weniger als \(10^{-38}\), weil \(h_y\) das ungerade Chebyshevpolynom annihiliert. Für \(D_{cn}^*D_{cn}i\) gilt die exakte Primgramformel des [Arbeitsauftrags, Phase D](../../research/x-c1/a9-a11-certificate-calibration-2026-10-15/WORK_ORDER.md). Die konstante Diagonale verschwindet, die gekappte Diagonale wurde oben begrenzt. Es verbleibt nach Division durch \(d\) das Gewicht \(2\log(2)\log(5)/(d\sqrt{10})\) mal die Reflexion \(\mathbf1_{x>\log(10)-b}i(\log(10)-x)\). Die Summe aller bisher geschätzten Fehler in \(L_i-T_i\) ist kleiner als \(10^{-14}\), auch nach Multiplikation mit den angegebenen Normen der alten Tests.

Der Prüfer berechnet die unendliche Restnorm dieser Reflexion auf dem rohen hohen Raum als Differenz ihrer vollen quadratischen Norm und der 4096 niedrigen Energien. Die Integrationsgrenze ist \(\xi=(\log(10)-b-a)/h\). Auf \(\xi<u<1\) steht \(q_i(1+\xi-u)\), denn \(\log(10)=a+b+h\xi\). Die volle Norm folgt durch Integration von \(q_i^2\) auf \([\xi,1]\). Für die endlichen Momente verwendet die Rechnung die exakte integrierte Legendre-Rekursion und die Dreitermrekursion für Multiplikation mit \(2u-1\). Alle Auswertungen einschließlich der Subtraktion erfolgen mit Arb-Kugeln bei 8192 Bit. Die physischen Normierungsuntergrenzen stammen aus dem Elternbeleg.

| Größe | \(e_o\) | \(s\) |
|---|---:|---:|
| Reflexionsrest vor Gewicht | \(<1.766810\,10^{-6}\) | \(<2.97270\,10^{-4}\) |
| \(\|L_i-T_i\|_{Y_o^*}\) | \(<6.77\,10^{-7}\) | \(<1.14\,10^{-4}\) |
| \(G^Y_{ii}\) einschließlich Antwortfehler | \(<1.23\,10^{-10}\) | \(<9.1\,10^{-6}\) |

Die letzte Zeile benutzt \((\|L_i-T_i\|+\|E_N(D_i-L_i)\|+2.183\,10^{-26}+\sqrt{8.833\,d_i})^2/0.58\). Die beiden \(d_i\) sind die geerbten vollständigen alten Restenergien. Mit \(|G^Y_{es}|\le\sqrt{G^Y_{ee}G^Y_{ss}}\) gilt für die korrigierte erste Diagonale \(a-h_e>0\), für die Determinante \((a-h_e)(b-h_s)-(z+\sqrt{h_eh_s})^2>2.97146\,10^{-11}\). Quadratische Ergänzung mit dem positiven Hochblock beweist die Aussage.

## Reproduktion

Python 3 mit python-flint 0.9.0. Im Handoff-Ordner ausführen:

    python hochraum.py ../a9-a11-ungerader-kernvergleich-2026-11-25/ENERGIE.json

Die Option `--full-inputs ORDNER` vergleicht zusätzlich die zwölf Logpolynome und die Antwortmatrix mit den Originalen FUNCTIONS12.json und FROZEN_RESPONSE12.json einschließlich SHA-256. Beide Laufarten wurden geprüft. JETDATEN.json enthält den kompakten Auszug. Der Code prüft die rationalen und gerichteten Zahlenvergleiche. Die Identifikationen der Operatoren und die analytischen Reduktionen stehen im Text. Die Ursprungsintegrationen der Vorstufen sind übernommene Eingaben. Für Punkt 4 auf dem ganzen Raum sind weitere Richtungen und die physische Ausgabe erforderlich.
