# Lokaler Unendlich-Rang-Nachweis der konkreten Prim-/Gamma-Form auf glatten Zwei-Moment-Tests

**Objekt X · mathematische Arbeitsnotiz · 22. November 2026**  
Bezug ist die Nichtpolform am Commit `ffc81439b73d27929777819b4374a26f6d998181`. Abschnitt 1 enthält den eigenständig lesbaren Satz. Abschnitt 2 gibt die genaue Folgerung für Approximationen an. Abschnitt 3 prüft eine aus lokalen Mellin-Daten gebildete Testabbildung.

## 1. Satz auf einem festen Fenster

Setze \(h=\log 2\), \(d=h/4\), \(c=h/\sqrt2\). Das Fenster \((-t,t)\) enthalte ein offenes Intervall \(I\) der Länge \(d\) und seine Verschiebung \(I+h\). Es sei \(D_t\) der Raum der \(f\in C_c^\infty((-t,t);\mathbb C)\) mit \(\int e^{\pm x/2}f(x)\,dx=0\), und \(V_I\) der Teilraum dieser Tests mit kompaktem Träger in \(I\). Wir setzen Funktionen durch null fort, verwenden \(\tau_s f(x)=f(x-s)\) und nehmen das Skalarprodukt antilinear im ersten Argument.

Die konkrete Form aus (1.1) ist
\[
\begin{aligned}
q_t^{\rm np}(f,g)
 &= E(f,g)-\kappa\langle f,g\rangle
 -\!\!\sum_{p^j\le e^{2t},\,j\ge1}\frac{\log p}{p^{j/2}}
   \langle f,(\tau_{j\log p}+\tau_{-j\log p})g\rangle,\\
E(f,g)&=\int_0^\infty k(s)
  \langle \tau_s f-f,\tau_s g-g\rangle\,ds,\qquad
k(s)=\frac{e^{-s/2}}{1-e^{-2s}},\qquad
\kappa=\log(8\pi)+\gamma+\frac{\pi}{2},
\end{aligned}
\]
wobei \(p\) die Primzahlen durchläuft und \(\gamma\) die Euler-Konstante bezeichnet.

**Satz.** Für jedes \(u\in V_I\) gilt
\[
 \operatorname{Re}q_t^{\rm np}(u,\tau_hu)
 \le -h(1/\sqrt2-1/2)\|u\|_2^2.
\]
Die Form hat auf \(D_t\) unendlichen Rang. Insbesondere kann keine lineare Abbildung von \(D_t\) in einen festen endlichdimensionalen Hilbertraum alle ihre Paarungen darstellen.

**Beweis.** Verschieben multipliziert die beiden Momente mit \(e^{\pm h/2}\), also liegt \(\tau_h u\) in \(D_t\). Für \(u,w\in V_I\) gilt die bilineare Version der Kernrechnung (über \(\mathbb C\) sesquilinear)
\[
 q_t^{\rm np}(u,\tau_hw)
 =-c\langle u,w\rangle
   -\int_I\int_I \overline{u(x)}\,k(h+y-x)\,w(y)\,dy\,dx. \tag{1}
\]
Tatsächlich trifft in der Primsumme nur \(\tau_{-h}\tau_hw=w\). Für jede Primzahlpotenz ab 3 gilt \(\log(p^j)-h\ge\log(3/2)>d\). Die beiden unverschobenen Träger sind disjunkt. Beim Ausmultiplizieren von \(E\) überlebt für \(s>0\) nur der Kreuzterm, der den linken Träger nach rechts verschiebt. Mit \(s=h+y-x\) ergibt sich das Integral in (1) mit Koeffizient \(-1\).

Sein Betrag ist höchstens \(d\,k(h-d)\|u\|_2\|w\|_2\). Für die fallende Funktion \(k\) gilt \(k(h-d)<k(h/2)=2^{3/4}<2\). Einsetzen von \(w=u\) gibt die Behauptung. Für jedes \(\phi\in C_c^\infty(I)\) liegt \(\phi''-\phi/4\) nach zweimaliger partieller Integration in \(V_I\). Diese Zuordnung ist injektiv, denn eine kompakt getragene Linearkombination von \(e^{x/2}\) und \(e^{-x/2}\) ist null. Somit ist \(V_I\) unendlichdimensional. Die Abbildung \(u\mapsto q_t^{\rm np}(u,\cdot)\) ist auf \(V_I\) injektiv, wie die Auswertung an \(\tau_hu\) zeigt. Das beweist den Rangsatz. Für eine endlichrangige Gram-Abbildung \(T\) ergäbe jedes \(0\ne u\in\ker(T|_{V_I})\) den Widerspruch \(q_t^{\rm np}(u,\tau_hu)=0\). ∎

Die Identifikation mit der arithmetischen Weil-Form verwendet H0. Der Satz über \(q_t^{\rm np}\) folgt allein aus (1.1) auf dem festen Fenster. [Formdefinition, H0 und Zwei-Moment-Domäne](https://github.com/Waschtl904/objekt-x-programm/blob/ffc81439b73d27929777819b4374a26f6d998181/handoffs/ritz-rest-2026-11-21/belege/DOMAIN_HERLEITUNG.txt)

## 2. Exakter Abstand des Kreuzoperators von den kompakten Operatoren

Es sei \(H_I=\overline{V_I}^{\,L^2(I)}\). Durch (1) ist \(A\) auf \(H_I\) eindeutig definiert durch \(\langle u,Aw\rangle=q_t^{\rm np}(u,\tau_hw)\) auf den glatten Tests. Es gilt
\[
 A=-c\,\mathrm{Id}_{H_I}+K,\qquad
 \inf_{C\ {\rm kompakt}}\|A-C\|_{H_I\to H_I}=c=\frac{\log2}{\sqrt2}. \tag{2}
\]
Hier ist \(K\) der auf \(H_I\) komprimierte Integraloperator mit Kern \(-k(h+y-x)\). Der Abstand zum Pol des Kerns ist mindestens \(h-d>0\), daher ist der Kern quadratintegrierbar und \(K\) kompakt. Für jeden kompakten Operator \(C\) und jede Orthonormalfolge \((u_n)\) in \(H_I\) geht \((K-C)u_n\) in Norm gegen null. Damit geht \(\|(A-C)u_n\|\) gegen \(c\). Die Wahl \(C=K\) erreicht den Abstand. Endlichrangige Approximationen von \(K\) zeigen, dass das Infimum über beschränkte Operatoren endlichen Rangs ebenfalls \(c\) beträgt.

Ein konkreter Test für Theta-Daten folgt daraus. Ein lokaler Ansatz \(Tu=\int_I u(x)b_x\,dx\) mit stark messbaren Hilbertraumvektoren und \(\int_I\|b_x\|^2dx<\infty\) ist Hilbert-Schmidt. Hat die Synthese auf \(I+h\) eine beschränkte \(L^2\)-Fortsetzung, ist der zurückverschobene Kreuzoperator der beiden Abbildungen kompakt. Eine solche Paarung verfehlt (2) selbst bei unendlichdimensionalem Zielraum. Bei einem wirklichen Theta-Lift wären diese Voraussetzungen an den gewählten Daten zu prüfen. Für wachsende Modelle unterscheidet (2) zwischen gleichmäßiger Approximation aller normierten lokalen Tests und Konvergenz auf jedem einzelnen festen Test.

## 3. Zweierkanal und Gammaanteil aus lokalen Mellin-Daten

Als ausdrücklich gewählten Vergleich verwende man die lokalen Standardfunktionen \(\mathbf1_{\mathbb Z_p}\) und \(e^{-\pi x^2}\). Mit \(\operatorname{vol}_{d^\times x}(\mathbb Z_p^\times)=1\), \(|p|_p=p^{-1}\) und \(d^\times x=dx/|x|\) auf \(\mathbb R^\times\) lauten ihre Mellin-Integrale für \(\Re s>0\)
\[
 L_p(s)=\sum_{j\ge0}p^{-js}=(1-p^{-s})^{-1},\qquad
 L_\infty(s)=\int_{\mathbb R^\times}e^{-\pi x^2}|x|^s\,d^\times x
 =\pi^{-s/2}\Gamma(s/2).
\]
Die erste Rechnung zerlegt \(\mathbb Z_p\setminus\{0\}\) in \(p^j\mathbb Z_p^\times\). Die zweite benutzt die Substitution \(y=\pi x^2\) auf der positiven Halbachse und die Geradheit des Integranden.

Setze \(s=1/2+i\xi\), \(m_v(\xi)=L_v(s)/L_v(\bar s)\). Die Wahl des Quotienten legt das Vorzeichen der folgenden Ableitung fest. Es gilt \(|m_v|=1\) und
\[
 a_v(\xi)=-i\,m_v^{-1}\partial_\xi m_v=2\operatorname{Re}(L_v'/L_v)(s).
\]
Für \(p=2\) ergibt das die absolut und gleichmäßig konvergente Reihe
\[
 a_2(\xi)=-2h\sum_{j\ge1}2^{-j/2}\cos(jh\xi).
\]
Bei der unitären Fouriertransformation mit \(e^{-ix\xi}\) ist dies genau der Multiplikator der negativen Summe beider Translationsrichtungen. Für andere Primzahlen gilt dieselbe Rechnung mit \(h=\log p\) und \(p^{-j/2}\).

Mit \(\psi=\Gamma'/\Gamma\) und \(\alpha_n=2n+1/2\) liefert dieselbe Ableitung an der reellen Stelle
\[
\begin{aligned}
 a_\infty(\xi)&=-\log\pi+\operatorname{Re}\psi(1/4+i\xi/2)\\
 &=-\kappa+2\sum_{n\ge0}
       \frac{\xi^2}{\alpha_n(\alpha_n^2+\xi^2)}.
\end{aligned} \tag{3}
\]
Dabei gilt \(\psi(1/4)=-\gamma-\pi/2-3\log2\). Die Differenz der beiden Digammawerte folgt summandenweise aus der Partialbruchreihe für \(\psi\). So stimmt (3) einschließlich der additiven Konstante mit (1.1)–(1.2) des Projekts überein. Der Bezug zwischen logarithmischen Ableitungen lokaler Tate-Faktoren und den Beiträgen der expliziten Formel hat eine etablierte operatorentheoretische Behandlung bei Burnol. [Burnol, *Spectral Analysis of the local Conductor Operator*](https://arxiv.org/abs/math/9811040) · [DLMF, Digamma-Reihe](https://dlmf.nist.gov/5.7) · [DLMF, spezielle Werte](https://dlmf.nist.gov/5.4)

**Eine explizite Testabbildung und ihre beiden Paarungen.** Bilde für das feste Fenster das endliche Produkt \(m_t=m_\infty\prod_{p\le e^{2t}}m_p\) und setze \(T_tu=m_t\widehat u\). Diese lineare Isometrie in \(L^2(\mathbb R,d\xi)\) hat unendlichdimensionales Bild auf \(D_t\). Für \(D=-i\partial_\xi\) gilt durch die Produktregel und Plancherel für alle \(u,v\in D_t\)
\[
 q_t^{\rm np}(u,v)=
 \langle T_tu,D T_tv\rangle-\langle \widehat u,D\widehat v\rangle . \tag{4}
\]
Die Ableitung des endlichen Produkts summiert die \(a_v\). Potenzen mit \(j\log p\ge2t\) verschwinden in der komprimierten Formpaarung wegen fehlender Überlappung. Es gibt somit keinen Grenzübergang über die Primstellen. Die Fourierbilder glatter kompakter Tests liegen im Schwartzraum. Die endlichen lokalen Multiplikatoren \(a_p\) sind beschränkt, und (3) wächst höchstens logarithmisch (Reihe bei \(\alpha_n\approx1+|\xi|\) teilen). Damit liegen \(\widehat v\) und \(T_tv\) in der Domäne von \(D\).

Für \(0\ne u\in V_I\) liefert (4) die negative Kreuzpaarung aus (1). Das gewöhnliche Skalarprodukt derselben Bilder ist dagegen \(\langle T_tu,T_t\tau_hu\rangle=\langle u,\tau_hu\rangle=0\). Die Rechnung identifiziert also die richtige Wirkung in einer Differenz zweier Paarungen und entscheidet den Test für die vorgeschlagene Isometrie vollständig. Eine Zuordnung \(u\mapsto\) automorphe Theta-Daten, deren **gewöhnliches** Skalarprodukt diese Differenz realisiert, bleibt offen. Die Rallis-Paarung in (III.210) wäre an einer solchen Zuordnung auszuwerten. [Waterloo-Ausarbeitung, (III.210)](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper.pdf)

