# A9 → A11 · Der vollständige Schurvergleich auf einem Teilraum endlicher Kodimension

23. November 2026. Analytische Herleitung zur Gegenprüfung für die festgelegte Majorante \(U_9=W_9\) und die Zwölferantwort \(P\) am GitHub-Stand c0b7a59d7943383047d83399697d2cf5c195241e. Die Schranken gelten in jeder der beiden Paritäten. Verwendet werden die projektinternen Domänen- und Hilbertquellenidentifikationen, die A9-Inversformel (6.1)–(6.5) und der direkte rohe Schalenboden \(\sigma>0{,}51839\). Die A11-Terminalpositivität wird nicht eingesetzt.

## Aussage

Es gibt im rohen neuen Schalenraum \(X=L^2((a,b),2\,dx)\) einen unten explizit als gemeinsamen Kern linearer Abbildungen definierten abgeschlossenen Teilraum \(Y_p\) mit Kodimension höchstens 8942. Für jeden \(s\in Y_p\) in der Formdomäne gilt
\[
 (K_P-R^*W_9R)[s]\ \ge\ 0{,}58\,W[s].
\]
Auf \(Y_p\) stimmen \(W\) und die rohe Metrik überein. Die Aussage betrifft die vollständige Vergleichsform in diesen Richtungen. Sie umfasst den ganzen alten \(R_L\)-Term. Die Kompression auf \(Y_p\) besitzt einen auswertbaren skalaren Inversvergleich \(A_Y^{-1}\preceq(1/0{,}58)I_Y\). Die übrigen Richtungen und ihr Schurpreis sind offen. Weder eine numerische Basis des endlichen Quotienten noch dessen Dimension oder Positivität wurden bestimmt.

## 1. Drei paarweise Kopplungen

Schreibe \(c=\tfrac32\log2,\ a=\log3,\ b=\tfrac12\log11,\ g=a-c,\ h=b-a\). Indizes \(c,o,n\) bezeichnen die rechten Halbintervalle \((0,c),(c,a),(a,b)\), jeweils mit Maß \(2\,dx\) und Paritätsfortsetzung. \(B_{ij}\) sei die rohe gemischte Form als Operator von \(j\) nach \(i\); für disjunkte Träger ist \(B_{ij}=-(G_{ij}+D_{ij})\), wobei \(G\) die Gammakopplung und \(D\) die Summe der Primtranslationen mit Originalgewichten ist. Die Paritätszeichen gehen in die gefalteten Operatoren ein. Diagonale und \(-\kappa I\) tragen zu diesen gemischten Operatoren nichts bei.

Am Kontakt der beiden Schalen ist der gleichseitige Kern \(k(u+v)\), \(0<u<g,\ 0<v<h\). Für die hier auftretenden Abstände \(0<t\le a<3\) gilt
\[
0\le k(t)-1/(2t)\le e^{t/2}/4.
\]
Für die linke Seite verwende \(\sinh(t)/t\le e^{t^2/6}\le e^{t/2}\), für die rechte \(\sinh(t)\ge t\) und \(e^{t/2}-1\le (t/2)e^{t/2}\). Der singuläre Kern \(1/[2(u+v)]\) hat Norm höchstens \(\pi/2\) durch den beidseitigen Schurtest mit \(u^{-1/2},v^{-1/2}\). Der Spiegelkern hat absoluten Wert höchstens \(k(a+c)\). Die beschränkten Kerne kosten höchstens das jeweilige Supremum mal \(\sqrt{gh}\). Analog beim Kontakt des A8-Kerns und der alten Schale erhält man
\[
 M_{on}=\pi/2+\sqrt{gh}\,(e^{(g+h)/2}/4+k(a+c))<1{,}619,\qquad
 M_{co}=\pi/2+\sqrt{cg}\,(e^{a/2}/4+k(c))<1{,}847 .
\]
Diese Größen majorisieren \(\|G_{on}\|,\|G_{co}\|\). Es wird keine Hilbert–Schmidt-Norm des singulären Randkerns angesetzt.

Sei \(w_q=(\log r)/\sqrt q\) für \(q=r^j\), und \(s_6=\sum_{q=2,3,4,5,7,8}w_q^2\). Es gelten
\[
 \|D_{cn}\|\le p_*=\sqrt{\delta\,1{,}458639},\quad
 \|D_{co}\|=\sqrt{s_6},\quad \|D_{on}\|\le w_9,\quad
 \|D_{co}^*D_{cn}\|\le w_7w_8+w_8w_9+w_3^2 .
\]
Die erste Ungleichung folgt aus \(D_{cn}^*D_{cn}=\delta T_p\). Für \(D_{co}\) treffen die sechs Kanäle den Kern auf dem ganzen alten Flügel. Verschiedene gleichgerichtete Bilder sind getrennt, denn \(\log(8/7)>g\); für gespiegelte Bilder müsste eine ganze Zahl strikt zwischen \(8\) und \(9\) liegen. In \(D_{on}\) tritt nur die Reflexion mit \(q=9\) auf. Für das Produkt \(D_{co}^*D_{cn}\) müssen sich zwei Bilder auf dem A8-Kern treffen. Gleichgerichtet verlangt das \(1<q/r<e^{b-c}\) für einen neuen Kanal \(q\) und einen alten Kanal \(r\); es bleiben \((8,7),(9,8)\). Gespiegelt verlangt es \(e^{a+c}<qr<e^{a+b}\); es bleibt \((3,3)\). Jeder Beitrag auf den mit \(2dx\) normierten Halbintervallen ist eine komprimierte Translation oder Reflexion mit Norm höchstens eins. Mit \(D_{cn,\ne9}\) für die ersten sechs Kanäle gilt auch \(\|D_{cn,\ne9}\|\le p_*\), da der neunte Kanal zum Primgram nur eine positive Diagonale beiträgt.

## 2. Abgeschnittene Gammaoperatoren bei positivem Abstand

Der Kern \(k(t)=\sum_{j\ge0}e^{-(2j+1/2)t}\) hat bei \(t\ge g\) nach 128 Summanden einen Punktrest von höchstens \(L=e^{-(256+1/2)g}/(1-e^{-2g})\). Sei \(F_1\) die entsprechende Näherung von \(G_{cn}\). Sei \(F_2\) die Näherung des Produkts \(G_{co}^*D_{cn,\ne9}\), bei der nur der Gammakern abgeschnitten wird. Die ersten sechs neuen Primkanäle haben im A8-Kern Träger in \([-c+g,c-g]\); deshalb gilt die Abstandsschranke auch für \(F_2\). Für \(q=9\) besteht dort Randkontakt und dieser Beitrag wird separat mit \(M_{co}w_9\) bezahlt. Je Parität hat jeder Summand der beiden Reihen höchstens Rang eins: auf dem äußeren Flügel trennt sich \(e^{-\alpha x}\), auf dem inneren Flügel die entsprechende Paritätskombination \(e^{\alpha y}+(-1)^p e^{-\alpha y}\), bei der umgekehrten Abbildung entsprechend adjungiert. Damit
\[
 \|G_{cn}-F_1\|\le e_1=2\sqrt{ch}\,L<1{,}61\cdot10^{-6},\qquad
 \|G_{co}^*D_{cn,\ne9}-F_2\|\le e_2=2\sqrt{cg}\,L p_*<2{,}1\cdot10^{-6}.
\]

## 3. Der Teilraum und die tatsächliche gemeinsame Quelle

Verwende für die alte Schale die Buchstaben der Quellen: \(F_o,\Lambda_T,g_o,g_F,K,a_{\rm fin},J\) sind die alten W9-Karten, \(g_o\) bezeichnet den dort \(g\) genannten Quellenoperator. Für \(f=C_ps\) seien \(h_c=J_{\rm old}^* f\), \(v=F_o^*f-g_F^*U_8 h_c\), \(\nu=\Lambda_T^*f-g_o^*U_8h_c-a_{\rm fin}^*K^{-1}v\). Schreibe \(m_c\) für das alte Momentprofil auf dem Kern und \(u_m\) für den auf den Kern eingeschränkten rohen Hilbertvertreter der Formwirkung des nullfortgesetzten \(m_c\). Dieser Vertreter existiert nach dem Domänenbeweis für die stückweise glatten Profile mit logarithmischen Endpunkten.

Setze auf dem gesamten rohen Schalenraum
\[
 z(s)=B_{on}s-\delta^{-1}B_{co}^*B_{cn}s .
\]
\(Q^i_{<N}\) bezeichnet die rohe orthogonale Legendreprojektion auf Grade \(0,\ldots,N-1\) des Intervalls \(i\). Definiere \(Y_p\) durch folgende gleichzeitig verlangten Nullbedingungen mit \(N=4096\). Die rechte Spalte gibt obere Ränge an.

| Zu null gesetzte Größen | Rang höchstens |
|---|---:|
| Neues Schalenmoment \(\lambda_n(s)\), Antwort \(Ps\) | \(1+12\) |
| Altes Kernmoment \(\langle m_c,B_{cn}s\rangle\), Kernliftpaarung \(\langle u_m,h_c\rangle\) | \(1+1\) |
| \((U_8-\delta^{-1}I)h_c\) | 383 |
| \(v,\ J^*\nu\) | \(12+84\) |
| \(F_1s,\ F_2s\) | \(128+128\) |
| \(Q^n_{<N}s,\ Q^o_{<N}z(s)\) | \(4096+4096\) |

Die Rangschranke 383 folgt aus den 191 Koordinaten von \(V_8\), den 191 niedrigen Koordinaten und dem einen Momentterm von \(T_h^*T_h-I\). Sämtliche Bedingungen sind beschränkte lineare Beobachtungen. Ihre gemeinsame Kodimension ist höchstens 8942, unabhängig von linearen Abhängigkeiten. Ist die Formdomäne in \(X\) dicht, ist ihr Schnitt mit diesem Kern darin dicht: Die endlichdimensionale Bildmenge der Beobachtungen ist schon mit Formvektoren erreichbar. Deren feste Urbilder korrigieren die kleinen Beobachtungsfehler einer approximierenden Folge.

Auf \(Y_p\) gilt \(Os=s,\ W[s]=\|s\|_X^2,\ R s=C_ps,\ K_P[s]=d_p[s]\). Wegen der Momentbedingungen ist \(h_c=B_{cn}s\), und \(U_8h_c=\delta^{-1}h_c\). Für jeden zulässigen Test \(t\) auf dem alten Rest \(T\) gilt dann exakt
\[
 \langle t,\nu\rangle_{W_o}=\langle t,z(s)\rangle_{X_o}.
\]
Tatsächlich ist der physische alte Test die rohe Schalenfunktion minus \(\lambda_o(t)m_c/\mu_c\). Die erste dadurch entstehende Paarung verschwindet wegen \(\langle m_c,B_{cn}s\rangle=0\). Beim Kernoperator \(g_o t\) erzeugt derselbe Lift den Zusatz \(-\lambda_o(t)u_m/\mu_c\), dessen Paarung mit \(U_8h_c\) ebenfalls null ist. Der Restterm mit \(a_{\rm fin}\) verschwindet wegen \(v=0\). Diese Identität hält die direkte Wirkung und die Rückkopplung in derselben physischen Quelle zusammen. Insbesondere ist \(z\) hier ein roher Vertreter des auf \(T\) eingeschränkten Funktionals; man setzt ihn nicht mit dem physischen Rieszvektor \(\nu\) gleich.

## 4. Rechnung für den ganzen Hochblock

Es gelten auf \(Y_p\)
\[
 \delta^{-1}\|h_c\|^2\le(p_*+e_1)^2\|s\|^2/\delta<1{,}459\|s\|^2,
 \qquad \|z(s)\|\le L_z\|s\|,\quad L_z<2{,}726 .
\]
Für den Kernpreis wurde \(F_1s=0\) benutzt. Für die Quelle genügt
\[
L_z=M_{on}+w_9+
\delta^{-1}\left[
 w_7w_8+w_8w_9+w_3^2+M_{co}w_9+e_2+
 (M_{co}+\sqrt{s_6})e_1\right].
\]
Die vier Beiträge innerhalb der Klammer kommen aus dem reinen Primprodukt, der Gammawirkung auf den neunten Kanal, dem getrennten Gamma-Primprodukt mit \(F_2s=0\) und der Wirkung von \(B_{co}^*\) auf \(G_{cn}s\). Die Dreiecksungleichung wird erst nach der exakten Reduktion auf \(Y_p\) verwendet.

In der Variationsformel für \(R_L\) erweitere die Testmenge von \(T\) auf die ganze alte Legendre-Formdomäne. Wegen \(Q^o_{<N}z=0\) gilt dann
\[
 \langle\nu,R_L\nu\rangle_{W_o}
 \le\sum_{j\ge N}\frac{|\langle\ell_j,z\rangle_{X_o}|^2}{H_j+11/10}
 \le\frac{2{,}726^2}{H_N+11/10}\|s\|^2.
\]
Wegen \(v=J^*\nu=0\) verbleiben in (6.4) genau dieser Beitrag mit Faktor \(\omega=11/(10\beta)<9{,}917\) und der obige Kernpreis. Auf der direkten Seite gilt \(d_p[s]\ge D_H[s]+\sigma\|s\|^2\ge(H_N+\sigma)\|s\|^2\), weil der neue Momentlift entfällt und \(Q^n_{<N}s=0\). Mit \(H_{4096}>8{,}895\) ergibt sich für den Boden
\[
 8{,}895+0{,}51839-1{,}459-\frac{9{,}917\,(2{,}726)^2}{8{,}895+1{,}1}
 >0{,}58130>0{,}58 .
\]
Die alte und die neue Hochprojektion betreffen unterschiedliche Objekte. Die Zahl 4096 wurde als bequemer überprüfbarer Schnitt gewählt. Eine Optimierung der Kodimension ist nicht belegt.

## 5. Ausstehende Rechnung

Um den Quotienten zu prüfen, müssen unabhängige Nebenbedingungen und formzulässige Urbilder tatsächlich konstruiert werden. Auch wenn deren Diagonalblock positiv ist, kostet die Kopplung \(C_Y\) an den ganzen \(Y_p\)-Raum die Inversenergie \(C_Y^*A_Y^{-1}C_Y\). Der skalare Boden gibt dafür eine Schranke bei Hilbertquellen. Für reine Formdualquellen ist eine passende Energieabschätzung nötig. Der positive Schurrest des endlichen Blocks sowie die vollständige physische Inversausgabe bleiben offen. Die Komplementrechnung darf nicht die sehr großen endlichen Terme verwerfen, die auf \(Y_p\) absichtlich durch Nullbedingungen verschwinden.

[Definitionen und Zielzertifikat](https://github.com/Waschtl904/objekt-x-programm/blob/c0b7a59d7943383047d83399697d2cf5c195241e/research/x-c1/a9-a11-certificate-calibration-2026-10-15/WORK_ORDER.md) · [W9-Inversformel, §6](https://github.com/Waschtl904/objekt-x-programm/blob/c0b7a59d7943383047d83399697d2cf5c195241e/research/x-c1/a9-inverse-renewal-2026-10-13/original/HERLEITUNG.txt) · [W9-Inventar, insbesondere Gleichungen (1), (3), (5) und (6)](https://github.com/Waschtl904/objekt-x-programm/blob/c0b7a59d7943383047d83399697d2cf5c195241e/research/x-c1/w9-energy-inventory-2026-10-17/PROOF.md) · [Rohe Form, Carleman-Schranke und Momentprofile](https://github.com/Waschtl904/objekt-x-programm/blob/c0b7a59d7943383047d83399697d2cf5c195241e/handoffs/ritz-rest-2026-11-21/belege/DOMAIN_HERLEITUNG.txt)

## Intervallprüfung

Der folgende Python-Code wurde mit mpmath 1.3.0 und 44 Dezimalstellen Intervallpräzision ausgeführt. Er prüft die verwendeten skalaren Einzelfaktoren, den sicheren Boden und die angegebenen Kanalpaare. Die Hilbert- und Formraumidentitäten werden durch die Herleitung geprüft.

```python
from mpmath import iv

iv.dps = 44
R = iv.mpf
log, exp, sqrt = iv.ln, iv.exp, iv.sqrt
a, b, c = log(R(3)), log(R(11))/2, 3*log(R(2))/2
g, h = a-c, b-a
delta = R(18219)/10000
beta = R(20209999981781)/182190000000000
omega = 11/(10*beta)
tau_cap = R('1.458639')   # also checked below
sigma_floor = R('0.51839')  # bound from the direct-shell proof
powers = {2:2, 3:3, 4:2, 5:5, 7:7, 8:2, 9:3}
w = {q: log(R(p))/sqrt(R(q)) for q,p in powers.items()}
old = [2,3,4,5,7,8]
s6 = sum((w[q]**2 for q in old), R(0))
v, e = w[9]**2, 2*w[2]*w[5]
tau = (s6+v/2+sqrt(e**2+v**2/4))/delta
assert tau < tau_cap and R(0) < a-c
assert log(R(8)/7) > g and log(R(9)/8) > h
assert exp(a+c) > 8 and exp(a+b) < 10 and a+c < log(R(9)) < a+b
assert exp(b-c) < R(6)/5
pairs = {(q,r) for q in powers for r in old if q > r and log(R(q)/r) < b-c}
assert pairs == {(8,7),(9,8)}
assert b-log(R(2)) < c-g and log(R(9))-c < b
k = lambda t: exp(-t/2)/(1-exp(-2*t))
touch = iv.pi/2 + sqrt(g*h)*(exp((g+h)/2)/4+k(a+c))
inner = iv.pi/2 + sqrt(c*g)*(exp(a/2)/4+k(c))
prime_norm = sqrt(delta*tau_cap)
series = exp(-(R(256)+R(1)/2)*g)/(1-exp(-2*g))
eps1 = 2*sqrt(c*h)*series
eps2 = 2*sqrt(c*g)*series*prime_norm
product = w[7]*w[8]+w[8]*w[9]+w[3]**2
raw = (touch+w[9] + (product+inner*w[9]+eps2
                        +(sqrt(s6)+inner)*eps1)/delta)
core = (prime_norm+eps1)**2/delta
assert touch < R('1.619') and inner < R('1.847')
assert eps1 < R('0.00000161') and eps2 < R('0.0000021')
assert raw < R('2.726') and core < R('1.459') and omega < R('9.917')
H = sum((R(1)/j for j in range(1,4097)), R(0))
assert H > R('8.895')
floor = (R('8.895')+sigma_floor-R('1.459')
         - R('9.917')*R('2.726')**2/(R('8.895')+R('1.1')))
assert floor > R('0.58')
print('old/new Gamma', touch, 'joint source cap', raw, 'safe floor', floor)
```
