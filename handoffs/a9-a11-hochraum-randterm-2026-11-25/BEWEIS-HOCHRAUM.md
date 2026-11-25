# Objekt X · Der direkte Term der ungeraden Hochraumkopplung

**25. November 2026.** Projektinterne Herleitung zu Commit `9a21e089f65fe69367439819bd02b56fcb9c6508`. Unter den dortigen physischen Form- und Quellenidentifikationen. Eigenständige Gegenrechnung der Randterme. Externe Prüfung offen.

Für beide festen Tests ist der direkte Anteil des Kopplungsfunktionals auf dem ganzen $Y_o$ bis auf **einen expliziten inneren Randlogarithmus** eingeschlossen. Die Wechselwirkung dieses Logarithmus mit der alten Antwort steht aus. Das Ergebnis betrifft einen Teil von Punkt 4.

## 1. Welche Größe der Prüfer einschließt

Setze $a=\log3$, $b=\tfrac12\log11$, $h=b-a$, $u=(x-a)/h$. Die unitäre Darstellung des rechten Flügels ist $q_i(u)=\sqrt{2h}\,p_i(a+hu)$ mit Maß $du$ für den physisch normierten äußeren Test $p_i$. Derselbe Maßwechsel gilt für Hilbertvertreter und Testvektoren. Bei ungerader Fortsetzung ist $m(t)=\sinh(t/2)$. Auf dem alten Intervall $(-a,a)$ trägt der physische direkte Test den Wert $-\lambda_i m/\mu$ mit $\mu=(4/3-a)/2$ und $\lambda_i=\int_a^b p_i m$. In denselben Einheiten schreibe $B_i=-\sqrt{2h}\lambda_i/\mu$ und
\[
J_i=q_i(0)-B_i m(a),\qquad L_i(u)=-\tfrac12 J_i\log u .
\]
$L_i$ bezeichnet sowohl den Vektor als auch sein Funktional durch das $L^2(du)$-Skalarprodukt. Sei $D_i$ der Vertreter der direkten Wirkung des gehobenen Tests gegen einen **rohen**, auf die neuen Flügel beschränkten ungeraden Test. Auf $Y_o$ stimmt die Paarung mit $d[i,y]$ überein, weil $\lambda_n(y)=0$. Der rohe Projektor $E_N$ auf die neuen Legendregrade $n\ge N=4096$ ist explizit. Es gilt $Y_o\subseteq\operatorname{ran}E_N$.

| Schranke | $e_o$ | $s$ |
|---|---:|---:|
| $\|E_N L_i\|$ | $[0.000359874518341,0.000359874518342]$ | $[0.000736228301353,0.000736228301354]$ |
| $\|E_N(D_i-L_i)\|$ höchstens | $0.000000052456104$ | $0.000008816611755$ |
| $\|E_N D_i\|$ mindestens | $0.000359822062237$ | $0.000727411689598$ |
| $\|E_N D_i\|$ höchstens | $0.000359926974445$ | $0.000745044913108$ |

Die Untergrenzen in der dritten Zeile betreffen den größeren rohen Legendre-Rest. Die Einschränkung auf $Y_o$ liefert aus der zweiten und vierten Zeile Obergrenzen. Die gesamte Rechnung arbeitet mit der ganzen unendlichen Reihe.

## 2. Herleitung des Randterms

Die physische Gammawirkung am rechten Flügel ist das Integral von $k(v)[2f(x)-f(x+v)-f(x-v)]$ über $v>0$ mit $k(v)=e^{v/2}/(2\sinh v)$. Setze $r(v)=k(v)-1/(2v)$. Für die beidseits nullfortgesetzte Funktion auf dem rechten Flügel entsteht auf diesem Flügel
\[
 \int_a^b k(|x-t|)(p_i(x)-p_i(t))\,dt
 +p_i(x)\left[\int_{x-a}^\infty k(v)\,dv+\int_{b-x}^\infty k(v)\,dv\right].
\]
Der Anteil des inneren Differenzenintegrals mit $1/(2|x-t|)$ ist ein Polynom. Dies folgt durch Polynomdivision und getrennte Integration links und rechts von $x$. Die beiden äußeren Integrale liefern $-q_i(u)(\log u+\log(1-u))/2$, eine Konstante mal $q_i$ und die zu $r$ gehörenden Integrale. Die letzteren heben die Integrale mit $r(|x-t|)p_i(x)$ auf. Die verbleibende Faltung mit $r$ wird unten approximiert. Der gespiegelte neue Flügel ist auf positivem Abstand.

Für den alten Lift schreibe $M(t)=B_i m(t)$. Seine rohe Wirkung in der Einheitskoordinate enthält $-\int_{-a}^a k(x-t)M(t)\,dt$. Beim singulären Kern liefert Polynomdivision für ein Polynom $M$
\[
 -\tfrac12 M(x)\log((x+a)/(x-a))
 +\tfrac12\int_{-a}^a\frac{M(x)-M(t)}{x-t}\,dt.
\]
Damit ist der linke Logarithmus insgesamt $-[q_i(u)-M(a+hu)]\log u/2$. Rechts bleibt $-q_i(u)\log(1-u)/2$. Die Primkanäle $q=2,3,4,5,7,8,9$ treffen mit $x-\log q$ den alten Lift auf dem ganzen offenen rechten Flügel. Kein Kanal hat positive Überlappung der beiden neuen Flügel miteinander oder eines neuen Flügels mit sich selbst. Insbesondere hat $q=11$ nur Endpunktkontakt. Für einen polynomialen alten Lift sind alle verbleibenden Primaktionen Polynome. Auch der skalare Diagonalterm verschwindet nach $E_N$.

**Gerichteter Preis der glatten Anteile.** Ersetze $m$ durch sein um $a$ entwickeltes Taylorpolynom vom Grad 47. Auf $[-a,b]$ kostet dies bei $|B_i|<1$ punktweise höchstens $6(1.1)^{48}/48!$. Auf dem alten Intervall ist der Fehler der Kontaktabbildung in $L^2(du)$ einschließlich der Primkanäle höchstens das 400-Fache davon. Tatsächlich ist $|r|\le125$ auf $[0,2.4]$ nach der folgenden Kreisschranke. Der Carleman-Anteil kostet punktweise höchstens $\tfrac12\log((x+a)/(x-a))$ mal den gleichmäßigen Fehler. Für $x=a+hu$ ist der Logarithmus höchstens $3.2+|\log u|$, dessen Norm kleiner als 5 ist. Die sieben Primgewichte sind je kleiner als eins.

Auf $|z|=2.5$ gilt $|\sinh z|\ge1/2$. Für $|\operatorname{Re}z|\ge1/2$ folgt dies direkt aus $|\sinh z|^2=\sinh^2(\operatorname{Re}z)+\sin^2(\operatorname{Im}z)$. Andernfalls liegt $|\operatorname{Im}z|$ zwischen $\sqrt6$ und $2.5$. Der an null hebbare Rest $r$ hat auf diesem Kreis Betrag kleiner als 5. Sein Taylorpolynom vom Grad 2048 hat auf $[0,2.4]$ Fehler höchstens $5(24/25)^{2049}/(1-24/25)$. Jeder $r$-Faltungsterm mit dem polynomialen Test auf jedem Flügel ist nach dieser Ersetzung ein Polynom vom Grad höchstens 2060 in $x$. Auf dem eigenen Flügel zerlegt man die Integration bei $x$. Beim Integral über das alte Intervall bleiben beide Grenzen fest. In den normierten Werten gilt $\sup|q_i|\le12$ durch Cauchy–Schwarz in der Zwölferbasis, und der alte approximierte Lift hat dort Betrag unter 2. Die Summe der Längen mal Amplituden in den drei Faltungen ist kleiner als 50.

Für den regulären Faktor $\log(x+a)$ genügt die Reihe um $2a$. Für den verbleibenden reziproken Kern des gespiegelten Flügels genügt die geometrische Reihe um $a+b$ für $x+t$, $a<t<b$. Beide Entwicklungsquotienten liegen unter $0.051$. Beide Reihen werden nach Grad 64 abgeschnitten. Mit den obigen Amplituden liegt der Gesamtfehler unter $100(0.051)^{65}/(1-0.051)$. Sämtliche so erhaltenen Polynome haben Grad unter 4096. Der Prüfer bestätigt mit rationalen Zahlen, dass die drei genannten Fehler zusammen weniger als $10^{-30}$ kosten. Am Entwicklungspunkt $a$ hat der polynomiale Momentlift denselben Wert wie der exakte Lift.

## 3. Rechnung über alle Legendregrade

Der Prüfer verwendet die Rohkoeffizienten $c_j$ aus den unten gebundenen Tests. Vor der Normierung ist $q=\sum_j c_j\sqrt{2j+1}\,P_j(2u-1)$. Für $I=\int_0^1 q(u)m(a+hu)\,du$ ist der physische Normierungsfaktor $\sqrt{\sum c_j^2+h I^2/\mu}$. $B_i$ ist $-hI/\mu$ geteilt durch diesen Faktor. Die Reihen von $a=2\operatorname{atanh}(1/2)$ und $h=\operatorname{atanh}(1/10)$ werden mit geometrischer Restschranke ausgewertet. Für die Momentintegration gilt $\int_0^1P_j(2u-1)u^k\,du=(k!)^2/((k-j)!(k+j+1)!)$ für $k\ge j$, sonst null.

Für $n>k$ gilt
\[
 \left|\int_0^1 P_n(2u-1)u^k\log u\,du\right|
 =\frac{(k!)^2(n-k-1)!}{(n+k+1)!}.
\]
Die Formel folgt aus der Ableitung nach $\alpha$ von $\int_0^1 P_n(2u-1)u^\alpha\,du=\prod_{j=0}^{n-1}(\alpha-j)/\prod_{j=1}^{n+1}(\alpha+j)$ bei $\alpha=k$. Die Ausgangsidentität folgt durch integrierte Rodriguesformel, zunächst für $\alpha>n$, dann für $\alpha>-1$ durch die rationale Identität oder analytische Fortsetzung. Bei $k=0$ teleskopiert die quadrierte Norm im orthonormalen System zu $\sum_{n=N}^\infty (2n+1)/(n^2(n+1)^2)=1/N^2$. Für $k\ge1$ ist das Verhältnis zum Betrag bei $k=0$ für alle $n\ge N$ höchstens $\prod_{j=1}^k j^2/[(N-j)(N+1+j)]$. Spiegelung am rechten Ende erhält den Betrag. Der Prüfer setzt diese Faktoren an den Einschließungen der wirklichen Polynomkoeffizienten ein. Das erfasst beide logarithmischen Ränder und den ganzen Rest ab Grad 4096.

## 4. Übertragung auf die tatsächlichen Kopplungen

Für $y\in Y_o$ gelten $Py=0$, $Ry=C_p y$ und $W[y]=\|y\|^2$. Die Modellkorrektur zu $d$ in $K_P$ verschwindet in der gemischten Stelle mit $y$. In der Projektformel enthält jeder Term der symmetrischen Modellkorrektur auf einer Seite $X\widehat F y=0$, oder er lässt sich wegen $X=X^*$ so schreiben. Hier wird benutzt, dass die Spalten von $\Phi_{12}$ unabhängig sind und $P=\Phi_{12}X\widehat F$. Der beidseitige **ungerade** Modellfehler für $K_P$ ist kleiner als $2.183\cdot10^{-26}$ in der physischen Metrik. Daher addiert sich dieser Betrag zu jeder Obergrenze für die gemischte direkte Norm bei $W[i]=1$.

Auch die gemischte Wirkung der alten 96er-Antwort lässt sich auf $Y_o$ genau reduzieren. Schreibe $v_i=(v_{F,i},w_i)$ für die eingefrorenen Schalenkoordinaten, die physisch in den F- und J-Richtungen liegen. Setze $g v_i=g_Fv_{F,i}+g_oJw_i$, $x_i=A_*^{-1}(h_i-gv_i)$ und $\delta_0=1.8219$. Für $h_y=B_{cn}y$ liefern die definierenden Nullbedingungen des Hochraums
\[
 F_o^*Ry=g_F^*U_8 h_y,\qquad
 J^*\Lambda_T^*Ry=J^*g_o^*U_8 h_y,\qquad
 U_8h_y=h_y/\delta_0.
\]
In der zweiten Identität verschwindet der alte $a_{\rm fin}$-Term wegen $v(y)=0$. Das ergibt für die tatsächliche Antwort $V_i$ einschließlich ihres Kernanteils
\[
 T_i(y):=\langle Ry,V_i\rangle
 =\langle B_{cn}y,\, x_i+\delta_0^{-1}g v_i\rangle .
\]
Alle Abbildungen stehen in den physischen Metriken des Projekts. Diese Reduktion setzt den alten hohen Nenner $\delta_0$ nur an der Hochraumquelle $h_y$ ein. Die Kernantwort $x_i$ verwendet weiterhin $A_*^{-1}$.

Die wirkliche Kopplung lautet $C_Y i(y)=K_P[i,y]-T_i(y)-\langle Ry,Q_*^{-1}r_i\rangle$. Nach der Inversordnung und dem Hochraumbeweis gilt $\|Ry\|_{Q_*^{-1}}^2\le8.833\,W[y]$. Damit kostet der letzte Term höchstens $\sqrt{8.833\,d_i}$ in der Dualnorm für $W$. Die $d_i$ sind die beiden publizierten oberen Restpreise.

| Offener Funktionaltest auf ganz $Y_o$ | Hinreichende Obergrenze | Dann obere Grenze für $G^Y_{ii}$ |
|---|---:|---:|
| $\|L_e-T_e\|_{Y_o^*}$ | $0.000033847$ | $0.000000002980937985$ |
| $\|L_s-T_s\|_{Y_o^*}$ | $0.0054311$ | $0.000099808787575492$ |

Die letzte Spalte verwendet den Boden $0.58\,W$ und enthält den direkten Randrest, den $K_P$-Modellfehler und die alte Restenergie. Sie ist bedingt. Eine Auswertung der beiden Normen in der ersten Spalte fehlt. Beide sind nun als ein konkreter Vergleich mit der physischen A8-Kernquelle formuliert. Punkt 4 erfordert darüber hinaus die übrigen Richtungen und $U_{11}$.

## 5. Reproduktion und Primärquellen

Im entpackten Ordner erzeugt **python pruefe_direkten_hochraum.py** die beigefügte **ENDPUNKTE.json** auf der Standardausgabe. Python ab Version 3.9 mit Standardbibliothek genügt. Die Zahlenrechnung verwendet nach außen gerundete ganzzahlige Intervallgrenzen und exakte rationale Ungleichungen. Die mathematische Identifikation der Formen und die ältere Fehlerrechnung sind Projektvoraussetzungen.

- [Rohe Testvektoren und gewählte Antworten, Felder trial_e und trial_s](https://github.com/Waschtl904/objekt-x-programm/blob/9a21e089f65fe69367439819bd02b56fcb9c6508/handoffs/a9-a11-ungerader-kernvergleich-2026-11-25/ENERGIE.json)
- [Normierung und physische direkte Form im Projektintegrator](https://github.com/Waschtl904/objekt-x-programm/blob/9a21e089f65fe69367439819bd02b56fcb9c6508/research/x-c1/w9-partial-energy-2026-10-18/certify_k.py)
- [Definition von Y und Majorante der alten Inversenergie, §§ 3–4](https://github.com/Waschtl904/objekt-x-programm/blob/9a21e089f65fe69367439819bd02b56fcb9c6508/research/x-c1/a9-a11-hochblock-2026-11-23/A9-A11-Randkopplung-und-Hochblock-2026-11-23.md)
- [Ungerader beidseitiger Modellfehler der festen N12-Regel](https://github.com/Waschtl904/objekt-x-programm/blob/9a21e089f65fe69367439819bd02b56fcb9c6508/research/x-c1/nstar-jp-spike-orthogonality-2026-10-16/original/gpt2-kp-budgets/expected/BUDGET_BOUNDS.json)
- [Vorherige Zweiraumabnahme und Restpreise](https://github.com/Waschtl904/objekt-x-programm/blob/9a21e089f65fe69367439819bd02b56fcb9c6508/handoffs/a9-a11-ungerader-kernvergleich-2026-11-25/ABSCHLUSS.json)
