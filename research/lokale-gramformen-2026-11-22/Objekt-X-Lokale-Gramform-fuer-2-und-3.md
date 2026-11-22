# Objekt X · Eine lokale Gramform für die Primkanäle 2 und 3

22. November 2026 · Herleitung für die konkrete Nichtpolform. Alle Skalarprodukte sind antilinear im ersten Argument. Die Intervallrechnung am Ende ist reproduzierbar.

**Satz.** Sei \(I\) ein offenes Intervall der Länge \(0<d\le 0{,}02803\). Ein festes Fenster \((-t,t)\) enthalte
\[
\Omega=I\cup(I+\log 2)\cup(I+\log 3).
\]
Für alle \(f,g\in C_c^\infty(\Omega)\) gibt es eine einzige unten angegebene lineare Testabbildung \(T\) in einen positiven Hilbertraum mit
\[
q_t^{\rm np}(f,g)=\langle Tf,Tg\rangle,\qquad
q_t^{\rm np}(f,f)>0{,}0001631\,\|f\|_2^2\quad(f\ne0).
\]
Die beiden Primblöcke koppeln das erste Intervall jeweils an eines der beiden anderen. Zwischen \(I+\log 2\) und \(I+\log 3\) bleibt genau die archimedische Paarung. Die Breite umfasst das ganze zuvor zertifizierte Zweiintervall-Regime \(d\le d_*\).

## 1. Form und Referenz auf zwei Intervallen

Wir verwenden \((\tau_s f)(x)=f(x-s)\), \(\Delta_s=\tau_s-1\) und die Nullfortsetzung aller Tests auf \(\mathbb R\). Die Projektform lautet
\[
\begin{aligned}
k(s)&=\frac{e^{-s/2}}{1-e^{-2s}},\qquad
\kappa=\log(8\pi)+\gamma+\frac{\pi}{2},\\
E[f,g]&=\int_0^\infty k(s)\langle\Delta_s f,\Delta_s g\rangle\,ds,\\
q_t^{\rm np}(f,g)&=E[f,g]-\kappa\langle f,g\rangle
-\sum_{p^j\le e^{2t}}\frac{\log p}{\sqrt{p^j}}
  \langle f,(\tau_{\log(p^j)}+\tau_{-\log(p^j)})g\rangle .
\end{aligned}
\]
Für die Identifikation mit der arithmetischen Weil-Form auf der Projektklasse gelten H0 und die zwei Mellin-Nullmomente. Sämtliche folgenden lokalen Identitäten für die angegebene rechte Seite gelten ohne Momentbedingungen. [Projektform (1.1) am Commit ffc81439](https://github.com/Waschtl904/objekt-x-programm/blob/ffc81439b73d27929777819b4374a26f6d998181/handoffs/ritz-rest-2026-11-21/belege/DOMAIN_HERLEITUNG.txt)

Schreibe \(h=\log 2\), \(l=\log 3\) und \(b=l-h\). Für das ursprüngliche Paar \(I,I+h\) seien
\[
J_2(d)=(d,h-d)\cup(h+d,\infty),\qquad M_2(d)=2\int_{J_2(d)}k(s)\,ds.
\]
Die ursprüngliche Breite löst \(M_2(d_*)=\kappa+3h/2\). Für \(d\le d_*\) und Tests auf diesem Paar gilt mit \(D_2=1-2^{-1/2}\tau_h\) und \(A_2=(0,\infty)\setminus J_2(d_*)\)
\[
q_t^{\rm np}(f,g)=\int_{A_2} k(s)\langle\Delta_s f,\Delta_s g\rangle\,ds
+h\langle D_2f,D_2g\rangle .
\]
Denn auf \(J_2(d_*)\) ist die Gamma-Paarung im Integranden genau \(2\langle f,g\rangle\). Das Quadrat von \(D_2\) erzeugt den Primblock und den Diagonalbetrag \(3/2\). In den beiden Intervallkoordinaten hat die komprimierte Matrix von \(D_2^*D_2\) die Diagonale \(3/2\) und beide Nebeneinträge \(-1/\sqrt2\). Damit folgt der in der Gegenprüfung angegebene Boden \(h(3/2-1/\sqrt2)\|f\|_2^2\). [Ausgangsnotiz, Abschnitt 3](Objekt-X-Theta-und-lokale-Faktoren.md)

## 2. Die komprimierte Primwirkung auf drei Intervallen

Identifiziere \(f\) mit \(F=(f_0,f_2,f_3)\in L^2(I)^3\) durch \(f_0(x)=f(x)\), \(f_2(x)=f(x+h)\), \(f_3(x)=f(x+l)\) für \(x\in I\). Diese Identifikation erhält das Skalarprodukt. Für die geometrischen Aussagen in diesem Abschnitt genügt \(d\le0{,}03\). Die möglichen positiven Abstände liegen in \([0,d]\) und in den drei disjunkten Bändern \([x-d,x+d]\) um \(x=b,h,l\). Wegen \(l+d<\log 4\) kommen als Primzahlpotenzen nur 2 und 3 in Frage. Die Verschiebung um \(h\) verbindet exakt die erste und zweite Komponente, diejenige um \(l\) exakt die erste und dritte.

Mit \(a_2=h/\sqrt2,\ a_3=l/\sqrt3\) ist also der **abzuziehende** Primoperator in diesen Koordinaten
\[
W=\begin{pmatrix}0&a_2&a_3\\a_2&0&0\\a_3&0&0\end{pmatrix}.
\]
Die einfache additive Wahl \(h\|D_2 f\|^2+l\|D_3 f\|^2\) verlangt den skalaren Diagonalbetrag \(3h/2+4l/3\). Auf diesen Trägern genügen zwei Differenzen mit erheblich kleinerem Diagonalbetrag. Setze
\[
\rho=\sqrt{a_2^2+a_3^2},\qquad
L_i F=\frac{a_i}{\sqrt\rho}f_0-\sqrt\rho\,f_i,\quad i=2,3.
\]
Durch Ausmultiplizieren erhält man für beliebige Tripel \(F,G\)
\[
\sum_{i=2,3}\langle L_i F,L_i G\rangle
=\rho\langle F,G\rangle-\langle F,WG\rangle .
\tag{1}
\]
Der Koeffizient vor \(\langle f_0,g_0\rangle\) ist \((a_2^2+a_3^2)/\rho=\rho\). Jede der beiden anderen Komponenten erhält denselben Diagonalbetrag. Ein Produkt von \(f_2\) mit \(g_3\) kommt in keinem Quadrat vor. Unter allen Zerlegungen des **komprimierten Primteils** in positive Quadrate und einen einheitlichen Diagonalabzug ist \(\rho\) minimal. Die Eigenwerte von \(W\) sind \(0,\pm\rho\), also ist \(c\,\mathrm{Id}-W\) genau für \(c\ge\rho\) positiv semidefinit. Die beiden Kosten sind ungefähr \(2{,}50453716\) und \(0{,}80158769\).

## 3. Der Gammaanteil und die vollständige Testabbildung

Für die feste Referenzbreite \(D=0{,}02803\) seien
\[
\begin{aligned}
J_3(D)&=(0,\infty)\setminus\Big((0,D]\cup
            \bigcup_{x\in\{b,h,l\}}[x-D,x+D]\Big),\\
A_3&=(0,\infty)\setminus J_3(D),\qquad
M_3(D)=2\int_{J_3(D)}k(s)\,ds,\qquad
\varepsilon=M_3(D)-\kappa-\rho .
\end{aligned}
\]
Jedes \(0<d\le D\) verwendet dieselbe Menge \(A_3\). Für \(s\in J_3(D)\) sind \(\Omega\) und \(\Omega+s\) disjunkt. Beide gemischten Translationspaarungen verschwinden und \(\langle\Delta_s f,\Delta_s g\rangle=2\langle f,g\rangle\). Folglich ist der auf \(A_3\) verbleibende Teil von \(E\) genau \(E[f,g]-M_3(D)\langle f,g\rangle\).

Die Intervallprüfung in Abschnitt 5 ergibt \(\varepsilon>0{,}0001631\). Eine explizite Testabbildung ist
\[
T f=\big((\Delta_s f)_{s\in A_3},\ L_2F,\ L_3F,\ \sqrt{\varepsilon}\,f\big)
\]
mit Zielraum
\[
L^2(A_3\times\mathbb R,k(s)\,ds\,dx)
\ \oplus\ L^2(I)\ \oplus\ L^2(I)\ \oplus\ L^2(\mathbb R).
\]
Die Gammadifferenzen werden auf der ganzen Geraden ausgewertet. Ihre Integrierbarkeit folgt bei null aus \(\|\Delta_s f\|_2\le s\|f'\|_2\), bei großen \(s\) aus der Integrierbarkeit von \(k\). Addition der vier Gramkomponenten und (1) liefern den Skalarbeitrag \(-M_3(D)+\rho+\varepsilon=-\kappa\) und den vollständigen Primbeitrag \(-W\). Das beweist die behauptete Identität und die untere Schranke.

**Prüfpaar im Abstand \(\log(3/2)\).** Seien \(u,w\in C_c^\infty(I)\), \(f=\tau_hu\), \(g=\tau_lw\). In (1) sind alle Paarungen null. Der Diagonalterm verschwindet ebenfalls. Beim Ausmultiplizieren der Gammadifferenzen bleibt wegen der disjunkten geordneten Träger genau
\[
q_t^{\rm np}(\tau_hu,\tau_lw)
=-\int_I\int_I k(b+y-x)\,\overline{u(x)}w(y)\,dy\,dx .
\]
Der Integralkern ist glatt, da \(b-d>0\). Die Formel hält die echte archimedische Wechselwirkung zwischen den äußeren Intervallen fest. In den anderen zwei gemischten Blöcken trägt der Primteil \(-a_2\langle u,w\rangle\) bzw. \(-a_3\langle u,w\rangle\) bei.

**Kompatibilität.** Bei festem \(I\) und Referenzbreite \(D\) kann man mit Tests auf \(I\cup(I+h)\) anfangen und dann \(I+l\) hinzunehmen. Wer \(T\) von Anfang an verwendet, behält für jeden alten Test buchstäblich denselben Zielvektor, mit \(f_3=0\). Die Abbildung aus Abschnitt 1 realisiert auf alten Tests dieselbe Gramform in einem anderen Zielraum. Ein größeres Fenster lässt \(T\) auf dieser Konfiguration gleich, weil längere Verschiebungen hier keine Trägerüberlappung haben.

## 4. Wiederverwendung bei weiteren Trägern

Für ein festes endliches Muster von Intervallen \(I+x_i\) mit verschiedenen \(x_i\) kann man die Matrix \(W\) unmittelbar aus den Primverschiebungen aufbauen. Wähle die Länge \(d\) so klein, dass die Intervalle disjunkt sind und jede Primzahlpotenzverschiebung mit Überlappung zwei Intervalle genau zur Deckung bringt. Ein solches \(d>0\) existiert für jedes endliche Muster. Unterhalb seines um eins vergrößerten Durchmessers gibt es nur endlich viele Logarithmen von Primzahlpotenzen. Die positiven Abstände dieser Zahlen zu den davon verschiedenen Intervalldifferenzen haben daher bei nichtleerer Liste ein positives Minimum. Auch die Intervallbreite selbst ist kleiner als \(\log 2\) zu wählen.

Für \(i\ne j\) hat \(W_{ij}\) das Gewicht \((\log p)/\sqrt{p^m}\), wenn \(|x_j-x_i|=\log(p^m)\), sonst null. Die Diagonale ist null. Mit \(c=\lambda_{\max}(W)\) ist \(c\,\mathrm{Id}-W\) positiv semidefinit. Sein endlicher Matrixfaktor wirkt auf den Intervallindex, das Funktionsargument in \(L^2(I)\) bleibt erhalten. Damit sind auch höhere aktive Primzahlpotenzen erfasst. Dieser Schritt verwendet ausschließlich explizite Verschiebungsgewichte.

Für den Gammaanteil streiche aus \((0,\infty)\) das Band \((0,d]\) und die \(d\)-Umgebungen aller positiven Intervalldifferenzen, auch der nichtarithmetischen. Auf der übrigen Menge \(J\) ist die Gamma-Paarung ein Skalar. Für ein festes Muster und \(d\downarrow0\) wächst \(2\int_J k(s)\,ds\) unbegrenzt. Tatsächlich enthält \(J\) dann \((d,\delta/2)\) für jeden festen kleinsten Zentrenabstand \(\delta>0\), sobald \(d<\delta/2\), und \(k(s)\sim1/(2s)\). Im Fall eines einzigen Intervalls kann jede feste positive obere Grenze an die Stelle von \(\delta/2\) treten. Daher ist für jedes endliche Muster eine hinreichend kleine Referenzbreite verfügbar, die \(\kappa+c\) deckt. Die Konstruktion aus Abschnitt 3 gilt mit dem entsprechenden Matrixfaktor. Teilmuster desselben vorab festgelegten Musters lassen sich durch Nullsetzen der übrigen Komponenten mit derselben Abbildung behandeln.

**Eine feste Abbildung auch bei variierenden Intervalllagen.** Sei \(L>0\) eine obere Schranke für den Durchmesser des Trägersystems und \(\delta>0\) eine untere Schranke für den Abstand verschiedener linker Intervallenden. Lege vor der Wahl der Intervalle alle Kanäle \(q=p^j\le e^L\) fest. Setze
\[
C_L=\kappa+\sum_{p^j\le e^L}(\log p)(1+p^{-j}),\qquad
D_0=\frac{\delta}{2}\exp\big[-e^{\delta/4}(C_L+1)\big].
\]
Bei Intervallbreiten höchstens \(D_0\) liegt \(J_0=(D_0,\delta/2)\) für jedes solche System vollständig außerhalb der möglichen Trägerabstände. Auf \(J_0\) gilt \(2k(s)\ge e^{-\delta/4}/s\), weil \(1-e^{-2s}\le2s\). Also ist \(m_0=2\int_{J_0}k(s)\,ds\ge C_L+1\). Setze \(D_q=1-q^{-1/2}\tau_{\log q}\). Die feste Abbildung
\[
f\longmapsto\left((\Delta_s f)_{s\notin J_0,\ s>0},
     \ (\sqrt{\log p}\,D_{p^j}f)_{p^j\le e^L},
     \ \sqrt{m_0-C_L}\,f\right)
\]
hat die Gamma-Zielnorm aus Abschnitt 3 und gewöhnliche Vollgeraden-\(L^2\)-Normen in allen anderen Komponenten. Ihre Gramform ist die Projektform auf jedem dieser Trägersysteme. Dies folgt durch Ausmultiplizieren jedes \(D_q^*D_q\). Kanäle mit \(\log q>L\) haben dort keine Wirkung. Umgekehrt kann bei einem kleineren Fenster auch ein in der Abbildung vorgehaltener Kanal die Fenstergrenze überschreiten. In diesem Fall verschwinden seine beiden Translationspaarungen auf den Tests. Der Diagonalbetrag aller vorgehaltenen Kanäle ist bereits in \(C_L\) enthalten.

Hier dürfen sich die Intervalle verschieben und weitere Primkanäle durch teilweise Überlappung aktiv werden. Zielraum und Abbildung hängen nur von \(L,\delta\) ab. Die Identität gilt für jedes Testpaar, dessen **gemeinsamer** Träger in einem zulässigen System liegt. Beliebige Linearkombinationen aus verschiedenen Systemen können diese Voraussetzung verletzen. Die Formel für \(D_0\) ist eine hinreichende, konservative Breite. Abschnitt 3 liefert den wesentlich schärferen Befund für das konkrete feste Muster.

Beide Konstruktionen verwenden die vorgegebenen Primgewichte, den Gammakern und ein Stück Gammaenergie aus trennenden Verschiebungen. Ein intrinsischer Ursprung beider Komponenten und kompatible Abbildungen auf den **gesamten** wachsenden Formräumen bleiben offen. Zur zweiten Ritz-Restenergie enthält der Satz keine Abschätzung.

## 5. Reproduzierbare Intervallprüfung

Setze \(z=e^{-s/2}\) und \(F(s)=\tfrac12\log((1+z)/(1-z))+\arctan z\). Es gilt \(F'=-k\), \(F(\infty)=0\). Für die Abstandsmenge \(B=\{h\}\) oder \(B=\{b,h,l\}\) und die hier verwendeten disjunkten Bänder ist
\[
M_B(d)=2\left[F(d)-\sum_{x\in B}\big(F(x-d)-F(x+d)\big)\right].
\]
Diese Funktion ist streng fallend, weil die ausgeschlossenen Bänder mit \(d\) wachsen und \(k>0\). Die Tabelle gibt äußere Intervalle mit rationalen Dezimalgrenzen.

| Träger und Diagonalbetrag \(c\) | \(d\) | Einschließung von \(M_B(d)-\kappa-c\) |
|---|---:|---:|
| Zwei Intervalle, \(3h/2\) | \(0{,}02802\) | \([0{,}0002665,\ 0{,}0003666]\) |
| Zwei Intervalle, \(3h/2\) | \(0{,}02803\) | \([-0{,}0001331,\ -0{,}0000330]\) |
| Drei Intervalle, \(\rho\) | \(0{,}02803\) | \([0{,}0001631,\ 0{,}0002632]\) |
| Drei Intervalle, \(\rho\) | \(0{,}02804\) | \([-0{,}0003214,\ -0{,}0002213]\) |
| Drei Intervalle, \(3h/2+4l/3\) | \(0{,}02803\) | \([-1{,}702787,\ -1{,}702686]\) |

Die Grenze des früheren Abzugs liegt also unter \(0{,}02803\). Die entsprechende Grenze des Dreiträgerabzugs mit \(\rho\) liegt zwischen \(0{,}02803\) und \(0{,}02804\). Diese Grenzen gehören zu den jeweiligen Quadratzerlegungen. Über die größtmögliche Breite für Positivität der Form treffen sie keine Aussage.

Das folgende Python-Beispiel prüft beide Enden jeder Tabellenzeile. Eingaben erfolgen in Intervallarithmetik mit 44 Dezimalstellen. Die Konstante \(\gamma\) wird nur mit \(H_n-\log(n+1)<\gamma<H_n-\log n\) eingeschlossen, \(n=10000\).

~~~python
from mpmath import iv

iv.dps = 44
R = iv.mpf
h, l = iv.ln(R(2)), iv.ln(R(3))
rho = iv.sqrt(h*h/2 + l*l/3)
two, three = [h], [l-h, h, l]
n = 10000
harmonic = sum((1/R(j) for j in range(1, n+1)), R(0))
gamma_lo = harmonic - iv.ln(R(n+1))
gamma_hi = harmonic - iv.ln(R(n))
base = iv.ln(8*iv.pi) + iv.pi/2

def tail(s):
    z = iv.exp(-s/2)
    return iv.ln((1+z)/(1-z))/2 + iv.atan2(z, R(1))

def margin_without_gamma(d, centers, diagonal):
    loss = sum((tail(x-d)-tail(x+d) for x in centers), R(0))
    return 2*(tail(d)-loss) - base - diagonal

rows = [
    (two,   3*h/2,       '0.02802', '0.0002665',  '0.0003666'),
    (two,   3*h/2,       '0.02803', '-0.0001331', '-0.0000330'),
    (three, rho,         '0.02803', '0.0001631',  '0.0002632'),
    (three, rho,         '0.02804', '-0.0003214', '-0.0002213'),
    (three, 3*h/2+4*l/3, '0.02803', '-1.702787',  '-1.702686'),
]
for centers, diagonal, width, lo, hi in rows:
    v = margin_without_gamma(R(width), centers, diagonal)
    assert R(lo) < v - gamma_hi
    assert v - gamma_lo < R(hi)
print(f"{len(rows)} Intervalle bestätigt")
~~~
