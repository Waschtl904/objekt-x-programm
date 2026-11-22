# Objekt X – lokale Faktoren, positive Gramformen und isometrische Fortsetzung

22. November 2026 · Die Abschnitte 1–2 behandeln Zwei-Moment-Tests. Ab Abschnitt 3 gelten die lokalen Gramidentitäten der konkreten Nichtpolform für alle glatten Tests auf den jeweils angegebenen Trägern. Die Aussagen beziehen sich auf die Nichtpolform $q_t^{\rm np}$ mit der unitären Fourier-Konvention $\exp(-i\xi x)$ und antilinearem ersten Argument. Für die Identifikation mit der arithmetischen Weil-Form gelten die zwei Momentbedingungen und Voraussetzung H0 des Projekts. [Formdefinition (1.1)–(1.3)](https://github.com/Waschtl904/objekt-x-programm/blob/ffc81439b73d27929777819b4374a26f6d998181/handoffs/ritz-rest-2026-11-21/belege/DOMAIN_HERLEITUNG.txt)

## 1. Eine explizite Theta-Abbildung mit unendlichem Rang

Aus der Gaußfunktion und dem Gitter der ganzen Zahlen bilde das Profil
$$
g(x)=e^{x/2}\sum_{n\ge1}\exp(-\pi n^2 e^{2x}),\qquad
(\Theta u)(X)=\int_{\mathbb R}u(y)g(X-y)\,dy .
$$
Als Zielraum verwenden wir $L^2(\mathbb R,dX)$ mit seinem gewöhnlichen Skalarprodukt. Das ist eine konkrete Wahl von Kern und Metrik. Die Jacobi-Transformation der Thetareihe ergibt
$$
g(x)-g(-x)=\tfrac12(e^{-x/2}-e^{x/2}).
$$
Für $x\to+\infty$ fällt $g(x)$ schneller als jede Exponentialfunktion. [Jacobi-Transformation, DLMF (20.7.32)](https://dlmf.nist.gov/20.7.E32)

**Lokale Kompaktheit.** Sei $I$ ein beschränktes Intervall und $V_I$ der Raum seiner glatten, kompakt getragenen Tests mit $\int e^{\pm y/2}u(y)\,dy=0$. Für diese Tests lässt sich derselbe Operator mit dem Kern
$$
G_I(X,y)=
\begin{cases}
g(X-y),&X\ge0,\\
g(y-X),&X<0
\end{cases}
\qquad(y\in I)
$$
schreiben. Denn die Differenz auf $X<0$ integriert sich durch die zwei Nullmomente zu null. Beide Enden des Kerns fallen gleichmäßig für $y\in I$ ab. Also gehört $G_I$ zu $L^2(\mathbb R\times I)$ und $\Theta$ setzt sich auf $H_I=\overline{V_I}^{L^2(I)}$ zu einem kompakten Hilbert-Schmidt-Operator $\Theta_I$ fort.

**Injektivität.** Für reelles $\sigma>1/2$ ist $c(\sigma)=\int e^{\sigma X}g(X)\,dX$ endlich und strikt positiv. Am linken Ende folgt die Integrierbarkeit aus der Jacobi-Transformation. Da $u$ kompakten Träger hat, ist Fubini auch mit Absolutbeträgen zulässig und liefert
$$
\int e^{\sigma X}(\Theta u)(X)\,dX=c(\sigma)\int e^{\sigma y}u(y)\,dy .
$$
Aus $\Theta u=0$ folgt das Verschwinden der gesamten Laplacetransformierten von $u$ auf $(1/2,\infty)$, nach dem Identitätssatz ebenso auf der imaginären Achse. Die Eindeutigkeit der Fouriertransformation gibt $u=0$. Das Bild der glatten Zwei-Moment-Tests ist somit unendlichdimensional.

**Entscheidung am ersten Primkanal.** Setze $h=\log 2$, $|I|=h/4$ und wähle das Fenster so, dass auch $I+h$ hineinpasst. Wegen $\Theta\tau_h=\tau_h\Theta$ ist der gemischte Gramoperator $\Theta_I^*\tau_h\Theta_I$ kompakt. Die Projektform verlangt auf genau diesem Raum den Operator $B_I=-a\,\mathrm{Id}+K_I$ mit $a=h/\sqrt2$ und kompaktem $K_I$ (Beweis in der Rangnotiz). Es folgt
$$
\|B_I-\Theta_I^*\tau_h\Theta_I\|_{H_I\to H_I}\ \ge\ a .
$$
Bereits auf glatten Tests scheitert daher die exakte Gramidentität für diese Jacobi-Faltung mit der genannten Zielmetrik. Diese Prüfung betrifft die hier definierte Abbildung. Die Anwendung auf einen bestimmten automorphen Lift würde eine Identifikation seiner Testabbildung und Zielmetrik erfordern. Das Injektivitätsargument bezieht sich auf die glatten Tests. Für jede beschränkte positive Umgewichtung $A$ auf dem Ziel-$L^2$ ist auch $\Theta_I^*A\tau_h\Theta_I$ kompakt, unabhängig davon, ob $A$ mit Translationen kommutiert. Die gleiche Fehlerschranke gilt. Für die essentielle Norm wird keine Selbstadjungiertheit des gemischten Blocks benötigt.

## 2. Euler- und Gammawirkung aus derselben Operation

Die folgenden Eingangsdaten hängen weder von Nullstellen noch von Ritz-Vektoren ab. An einer Primstelle verwende die Indikatorfunktion von $\mathbb Z_p$, an der reellen Stelle die Gaußfunktion $e^{-\pi x^2}$. Beide sind bei den üblichen selbstdualen additiven Maßen und Standardcharakteren Fourier-invariant. Ihre lokalen Mellinintegrale sind für $\operatorname{Re}s>0$
$$
\begin{aligned}
L_p(s)&=\int_{\mathbb Q_p^\times}{\bf1}_{\mathbb Z_p}(x)|x|_p^s\,d^\times x
=\sum_{j\ge0}p^{-js}=(1-p^{-s})^{-1},\\
L_\infty(s)&=\int_{\mathbb R^\times}e^{-\pi x^2}|x|^s\,\frac{dx}{|x|}
=\pi^{-s/2}\Gamma(s/2).
\end{aligned}
$$
Hier hat $\mathbb Z_p^\times$ multiplikatives Maß eins. Die erste Rechnung zerlegt nach Bewertungen, die zweite substituiert $\pi x^2$. Burnol gibt im unramifizierten Sektor ausdrücklich $H_{ij}=-(\log p)p^{-|i-j|/2}$ für $i\ne j$ und $H_{ii}=0$ an. An der reellen Stelle bestimmt er im geraden Sektor das Minimum $-\log(8\pi)-\gamma-\pi/2$. Die folgende Phasenrechnung gleicht diese bekannten Spektralfunktionen mit der Projektnormierung ab. Die Orientierung des Quotienten im Folgenden legt das Vorzeichen fest. [Burnol, *The Explicit Formula and the conductor operator*, Abschnitte F, H und I](https://arxiv.org/pdf/math/9902080)

Für $s=\tfrac12+i\xi$ sei $U_v$ der Multiplikationsoperator mit $L_v(s)/L_v(1-s)$ auf dem gemeinsamen Frequenzraum $L^2(\mathbb R,d\xi)$. Der Nenner ist der komplex konjugierte Zähler und beide sind von null verschieden. Also ist $U_v$ unitär. Für $D=-i\,d/d\xi$ mit Domäne $H^1(\mathbb R)$ liefert die Produktregel auf Fouriertransformierten glatter kompakt getragener Tests
$$
U_v^*DU_v-D=M_{m_v},\qquad
m_v(\xi)=\frac{U_v(\xi)^{-1}U_v'(\xi)}{i}
=2\,\operatorname{Re}\frac{L_v'}{L_v}(\tfrac12+i\xi).
$$
Hier steht $M_m$ für Multiplikation mit $m$. Die Ableitung der Phase ist für festes $p$ beschränkt und wächst an der reellen Stelle höchstens logarithmisch. Deshalb liegen auch die mit diesen Phasen multiplizierten Testtransformierten in der Domäne von $D$. An der reellen Stelle ergibt sich das logarithmische Wachstum direkt aus der folgenden Reihe durch Teilung bei $\alpha_n=1+|\xi|$.

**Primstelle.** Die geometrische Reihe und ihre konjugierte Kopie geben
$$
m_p(\xi)=-2\log p\sum_{j\ge1}p^{-j/2}\cos(j\xi\log p).
$$
Auf der logarithmischen Ortsachse entspricht das genau $-\sum_{j\ge1}(\log p)p^{-j/2}(\tau_{j\log p}+\tau_{-j\log p})$. Für Tests im Fenster $(-t,t)$ fallen Paare mit $j\log p\ge 2t$ durch fehlende Trägerüberlappung weg.

**Reelle Stelle.** Schreibe $\psi=\Gamma'/\Gamma$ und $\alpha_n=2n+1/2$. Dann folgt aus der Digammareihe sowie Spiegelungs- und Verdopplungsformel
$$
\begin{aligned}
m_\infty(\xi)
&=-\log\pi+\operatorname{Re}\psi(\tfrac14+i\xi/2)\\
&=-\kappa+2\sum_{n\ge0}
\frac{\xi^2}{\alpha_n(\alpha_n^2+\xi^2)},\\
\kappa&=\log(8\pi)+\gamma+\pi/2 .
\end{aligned}
$$
Der konstante Term folgt aus $\psi(1/4)=-\gamma-3\log2-\pi/2$. Die Differenz zu $\xi=0$ erhält man durch Subtraktion der Digammareihe bei $1/4$. Nach (1.2) des Projekts ist die Reihe genau der Multiplikator der Gamma-Differenzform $E$. [Digammareihe](https://dlmf.nist.gov/5.7.E6) · [Spiegelung und Verdopplung](https://dlmf.nist.gov/5.5)

**Gemeinsame Identität auf einem festen Fenster.** Das endliche Produkt $\mathcal U_t=U_\infty\prod_{p\le e^{2t}}U_p$ ist unitär. Die logarithmischen Ableitungen addieren sich. Mit der Nullfortsetzung der Tests und Plancherel folgt für alle $u,w\in D_t$
$$
q_t^{\rm np}(u,w)=
\langle\mathcal U_t\widehat u,D\mathcal U_t\widehat w\rangle
-\langle\widehat u,D\widehat w\rangle . \tag{1}
$$
Die endliche Ortskompression übernimmt dabei die Abschneidung der Primzahlpotenzen. Für $u,w\in V_I$ und das zweite Argument $\tau_hw$ liefert (1) den Block
$$
-\frac{\log 2}{\sqrt2}\langle u,w\rangle
-\int_{I\times I} k(h+y-x)\overline{u(x)}w(y)\,dx\,dy,\qquad
k(s)=\frac{e^{-s/2}}{1-e^{-2s}}.
$$
Nur eine der beiden Richtungen bei $p=2$, $j=1$ überlappt. Der zweite Summand ist die Kopplung der getrennten Träger durch den Gamma-Kern. Damit stimmt der gesamte Kurzträgertest mit der Projektform überein.

**Offene Konstruktionsfrage.** Die Abbildung $u\mapsto\mathcal U_t\widehat u$ hat unendlichen Rang. Ihr gewöhnliches Zielskalarprodukt ergibt wegen Unitarität $\langle u,w\rangle$. Gleichung (1) gibt die gesuchte Form als *Differenz* zweier Ausdrücke mit $D$. Für Objekt X fehlt eine aus denselben arithmetischen Daten gebaute positive Zielmetrik samt Testabbildung, deren gewöhnliches Gramprodukt (1) ergibt und beim Übergang zu größeren Fenstern verträglich bleibt. Die lokale Jacobi-Prüfung zeigt, welchen persistenten Primbeitrag diese Konstruktion bereits im ersten Fenster erhalten muss. Die Domänenaussage zu (1) gilt auf dem angegebenen gemeinsamen Testbereich. Die logarithmisch wachsende Ableitung liefert keine Invarianz des ganzen $H^1$ unter $U_\infty$. Für $t'>t$ stimmen die komprimierten Formen auf alten Tests überein. Die Vektoren $\mathcal U_{t'}\widehat u$ können sich weiterhin von $\mathcal U_t\widehat u$ unterscheiden.

## 3. Positive Gramform auf zwei kurzen Intervallen im Abstand $\log 2$

**Zusätzliche Struktur aus der Literatur.** Bei Connes und Consani führt die Multiplikation mit $1-p^{-z}$ von einem semilokalen Sonin-Raum in den um $p$ erweiterten Raum. Satz 5.3 liefert Injektivität und ein induktives System. Wir verwenden unten den konkreten Multiplikator auf der kritischen Linie im gewöhnlichen Rand-$L^2$. Eine Zuordnung der Projekttests zu den Sonin-Räumen ist dafür entbehrlich und wird hier nicht hergeleitet. Eine andere Wahl aus derselben Arbeit lässt sich sofort entscheiden. Für das vollständige endliche Phasenprodukt $U$ einschließlich der reellen Stelle ist $(1-P)UP$ bezüglich der Hardy-Projektion auf die linke Halbebene kompakt. Ein Testbild, das mit beschränkten Abbildungen durch diesen Block faktorisiert, hat einen kompakten gemischten Gramblock. Der Ausschluss aus der Rangnotiz betrifft genau diese Wahl. [Connes–Consani, *Quasi-inner functions and local factors*, Einleitung und Satz 5.3](https://arxiv.org/abs/2008.10974)

**Der Primfaktor.** Setze $h=\log2$, $r=2^{-1/2}$ und $D_2=1-r\tau_h$. Das ist im Ortsraum der Multiplikator $1-2^{-1/2-i\xi}$. Mit dem aus Burnols erstem Primgewicht bestimmten Vorfaktor $h$ ergibt sich
$$
hD_2^*D_2=h(1+r^2)\mathrm{Id}-hr(\tau_h+\tau_{-h}).
\tag{2}
$$
Der Primblock ist damit exakt. Der zusätzliche Diagonalbetrag ist $3h/2$. Zusammen mit dem Diagonalabzug der Nichtpolform ist $C=\kappa+3h/2$ zu berücksichtigen.

**Satz.** Es gibt eine eindeutig durch die folgenden skalaren Daten bestimmte Breite $d_*$ mit $0{,}02802<d_*<0{,}02804$. Sei $I$ ein Intervall mit Länge $d\le d_*$, $\Omega=I\cup(I+h)$ und $t$ ein Horizont mit $\Omega\subset(-t,t)$. Für alle $f,g\in C_c^\infty(\Omega)$ gibt es die unten explizit angegebene Abbildung $T$ in einen positiven Hilbertraum mit
$$
q_t^{\rm np}(f,g)=\langle Tf,Tg\rangle .
\tag{3}
$$
Die Identität verwendet die durch (1.1) definierte Nichtpolform auf allen glatten Tests dieses Trägers. Auf dem Zwei-Moment-Teilraum liefert H0 den Anschluss an die arithmetische Weil-Form. Die Nullfortsetzung der Eingaben und die Auswertung beider Zielkomponenten auf der ganzen reellen Ortsachse gehören zur Konstruktion. Der Operator $T$ und der Zielraum sind für diese Träger bei jedem größeren Horizont dieselben.

**Bestimmung der Breite.** Für $0<d\le h/4$ seien
$$
J_d=(d,h-d)\cup(h+d,\infty),\qquad
M(d)=2\int_{J_d}k(s)\,ds.
$$
Für $s\in J_d$ überlappen $\Omega$ und $\Omega+s$ nicht. Somit ist
$\langle\tau_s f-f,\tau_s g-g\rangle=2\langle f,g\rangle$ auf diesen Verschiebungen. Setzt man $R=e^{-s/2}$, ergibt eine elementare Integration
$$
F(s)=\int_s^\infty k(v)\,dv=\operatorname{artanh} R+\arctan R,\qquad
M(d)=2\{F(d)-F(h-d)+F(h+d)\}.
$$
$M$ ist stetig und streng fallend, da $J_d$ mit $d$ schrumpft und $k>0$ ist. Direkt gilt $M'(d)=-2\{k(d)+k(h-d)+k(h+d)\}<0$. Für $d\downarrow0$ wächst $M(d)$ über jede Grenze. Definiere $d_*$ durch $M(d_*)=C$. Die folgenden nach außen gerundeten Intervalle belegen Existenz im angegebenen Bereich und die Vorzeichen an beiden Vergleichsbreiten.

| Breite $d$ | Einschließung von $M(d)-C$ |
|---|---|
| $h/32$ | $(0{,}28485,\ 0{,}28496)$ |
| $0{,}02802$ | $(0{,}00026,\ 0{,}00037)$ |
| $0{,}02804$ | $(-0{,}00054,\ -0{,}00043)$ |
| $h/4$ | $(-2{,}45215,\ -2{,}45204)$ |

Zur Reproduktion genügt $H_{10000}-\log(10001)<\gamma<H_{10000}-\log(10000)$ mit $H_n=\sum_{j=1}^n1/j$. Für $z=(1-R)/(1+R)$ verwendet man $F=-\tfrac12\log z+\pi/4-\arctan z$ und $\pi=16\arctan(1/5)-4\arctan(1/239)$. Für die hier benötigten Argumente $0\le z<0{,}3$ schließen 38 Terme der alternierenden Arkustangensreihe und der erste ausgelassene Term den Wert ein. Die übrigen Rechenoperationen wurden mit nach außen eingeschlossenen Dezimalwerten ausgewertet.

**Testabbildung und Beweis.** Setze $A_*=(0,\infty)\setminus J_{d_*}$ und $\Delta_s f=\tau_s f-f$. Verwende
$$
T f=\big((\Delta_s f)_{s\in A_*},\,\sqrt h\,D_2 f\big),\qquad
\mathcal K=L^2(A_*\times\mathbb R,k(s)\,ds\,dx)\ \oplus\ L^2(\mathbb R,dx).
$$
Glätte sichert $\|\Delta_s f\|_2\le s\|f'\|_2$ bei null. Der Gammaanteil hat daher endliche Norm. Aus $d\le d_*$ folgt $J_{d_*}\subset J_d$. Genau über $J_{d_*}$ ist die Gammaenergie in der Paarung gleich $C\langle f,g\rangle$. Auf $\Omega$ kann unter den Primzahlpotenzen ausschließlich die Verschiebung $\pm h$ wirken, denn $h+d<\log3$. Folglich liefert (2)
$$
\begin{aligned}
\langle Tf,Tg\rangle
&=E[f,g]-C\langle f,g\rangle+h\langle D_2 f,D_2 g\rangle\\
&=E[f,g]-\kappa\langle f,g\rangle
-hr\langle f,(\tau_h+\tau_{-h})g\rangle
=q_t^{\rm np}(f,g).
\end{aligned}
$$
Insbesondere ist für $u,w$ im linken Intervall der gemischte Anteil des Primfaktors bei den Tests $u,\tau_h w$ genau $-h/\sqrt2\,\langle u,w\rangle$. Die verbleibende Gamma-Paarung ist die vollständige glatte Kopplung aus der Rangnotiz. Die Diagonalformen und alle Kreuzterme auf dem Trägerpaar folgen aus derselben Identität (3).

**Lokaler Boden.** Schreibe $f=u+\tau_h v$ mit $u,v$ auf $I$. Die drei Teile $u,\tau_h(v-ru),-r\tau_{2h}v$ von $D_2f$ haben paarweise getrennte Träger. Also gilt $\|D_2f\|^2=(1+r^2)(\|u\|^2+\|v\|^2)-2r\operatorname{Re}\langle u,v\rangle\ge(1+r^2-r)\|f\|^2$. Aus (3) folgt $q_t^{\rm np}(f,f)\ge h(3/2-1/\sqrt2)\|f\|^2$. Die Konstante für den $D_2$-Anteil wird bei $u=v$ erreicht. Die Gammaenergie kann den Boden der Gesamtform weiter erhöhen.

**Reichweite.** Die beiden Komponenten des Zielraums sind orthogonal. Ihre bekannte Normalisierung und die Trägergeometrie ermöglichen zusammen den exakten Ausgleich des Diagonalterms. Die beiden Maße und die lokalen Gewichte sind bereits als Eingangsdaten vorgegeben. Ein gemeinsamer intrinsischer Ursprung im Sinn der Arbeitsdefinition von Objekt X bleibt offen. Ein größeres Fenster darf weitere Tests enthalten, auf denen (3) bisher unbewiesen ist. Für $d=h/4$ reicht selbst der gesamte Betrag $M(d)$ aus den Verschiebungen ohne Überlappung für diesen Ausgleich nicht. Die Breite $d_*$ ist die Grenze dieser speziellen Wahl von $D_2$, Zielnorm und Abzug ausschließlich aus solchen Verschiebungen. Die Identifikation der Nichtpolform mit der arithmetischen Weil-Form erfordert weiterhin H0. [Arbeitsdefinition, Abschnitte 1–1.3](https://github.com/Waschtl904/objekt-x-programm/blob/f84e357322c57e03d26daabcce03a3280d83be72/00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)

**Prüfung des direkten Produkts bei der nächsten Primstelle.** Für $D_p=1-p^{-1/2}\tau_{\log p}$ erzeugt das unveränderte Produkt $D_2D_3$ in seiner gewöhnlichen Gramform einen Term mit Koeffizient $+1/\sqrt6$ bei jeder der Verschiebungen $\pm\log(3/2)$, außerdem bei $\pm\log6$. Dies folgt durch Multiplikation der beiden Ausdrücke $D_p^*D_p$. Weder $3/2$ noch $6$ ist eine Primzahlpotenz. Bei zwei hinreichend kurzen Intervallen im Abstand $\log(3/2)$ hat die Projektform einen glatten Gamma-Kern als einzigen gemischten Beitrag. Das Produkt erzeugt dort zusätzlich ein nichtkompaktes Vielfaches der Identität. Ein Diagonalabzug oder ein kompakter gemischter Korrekturterm kann es nicht entfernen. Für einen Ansatz mit diesem Produkt muss die Konstruktion also insbesondere eine exakte Aufhebung dieses falschen Verschiebungsgewichts erklären. Der Befund betrifft die gewöhnliche Gramform des Produktmultiplikators, nicht die Übergangssätze über Sonin-Räume.

## 4. Eine positive Gramform auf wachsenden Trägermengen

**Fragestellung.** In Abschnitt 3 wurde der Diagonalterm durch dieselbe Menge von Verschiebungen für jeden Punkt des Trägers ausgeglichen. Für mehrere Intervalle bestimmen wir stattdessen an jedem Ort $x$ die Gammaenergie, die durch Nullfortsetzung außerhalb des Trägers entsteht. Beim Hinzufügen eines Intervalls kann man exakt angeben, welcher Teil dieser Energie in neue innere Differenzen übergeht.

Sei $\Omega$ eine beschränkte offene endliche Vereinigung von Intervallen. Für $q=p^j$, $j\ge1$, schreibe $h_q=\log q$ und $a_q=(\log p)/\sqrt q$, wobei jede Primzahlpotenz einmal zählt. Setze für $x\in\Omega$
$$
\begin{aligned}
V_\Omega(x)&=\int_{\mathbb R\setminus\Omega}k(|x-y|)\,dy,\\
d_\Omega(x)&=\sum_{q=p^j}a_q\bigl({\bf1}_\Omega(x+h_q)+{\bf1}_\Omega(x-h_q)\bigr),\\
b_\Omega(x)&=V_\Omega(x)-\kappa-d_\Omega(x).
\end{aligned}
$$
$V_\Omega(x)$ ist an jedem inneren Punkt endlich. In $d_\Omega$ können nur Potenzen mit $h_q\le\operatorname{diam}(\Omega)$ beitragen. Definiere das Maß auf Paaren $x<y$ mit beiden Enden in $\Omega$ durch
$$
d\mu_\Omega(x,y)={\bf1}_{\{x,y\in\Omega,\ x<y\}}\,
dx\left[k(y-x)\,dy+\sum_{q=p^j}a_q\,\delta_{x+h_q}(dy)\right].
$$
Für $f,g\in C_c^\infty(\Omega)$, $\nabla f(x,y)=f(y)-f(x)$ und jeden Trägerhorizont $t$ gilt exakt
$$
q_t^{\rm np}(f,g)=
\int\overline{\nabla f}\,\nabla g\,d\mu_\Omega+
\int_\Omega b_\Omega(x)\overline{f(x)}g(x)\,dx. \tag{4}
$$
**Beweis.** In der Vollgeraden-Gammaenergie setzt man $y=x+s$. Für zwei innere Enden entsteht der stetige Teil des ersten Integrals. Liegt genau ein Ende in $\Omega$, entsteht nach Nullfortsetzung $V_\Omega(x)\overline{f(x)}g(x)$ am inneren Ende. Man zählt jedes Paar einmal. Bei den diskreten Paaren liefert das Ausmultiplizieren für jede aktive Verschiebung die beiden negativen Primkreuzterme. Die beiden dabei erzeugten Diagonalen ergeben zusammen $d_\Omega(x)$ und werden im zweiten Integral abgezogen. Glatte kompakte Tests rechtfertigen die Identitäten durch die integrablen Translationsdifferenzen. Die Polarisation gilt auch für komplexe Tests. Die Struktur aus gewichteten Differenzen und einem örtlichen Restterm ist aus der Theorie der Energieformen bekannt. [Keller–Lenz–Wojciechowski, *Graphs and Discrete Dirichlet Spaces*, Kap. 0](https://www.math.uni-potsdam.de/fileadmin/user_upload/Prof-GraphTh/Keller/KellerLenzWojciechowski_GraphsAndDiscreteDirichletSpaces_personal.pdf)

Schon $b_\Omega\ge0$ fast überall liefert einen positiven Zielraum
$$
\mathcal K_\Omega=L^2(\mu_\Omega)\oplus L^2(\Omega,b_\Omega\,dx),\qquad T_\Omega f=(\nabla f,f).
$$
Gilt $b_\Omega\ge c>0$, so folgt $q_t^{\rm np}(f,f)\ge c\|f\|_2^2$. Im Unterschied zum Faktor $D_2$ in Abschnitt 3 werden in (4) genau die Primkanten innerhalb der tatsächlichen Trägermenge angesetzt. Ihr Diagonalbetrag hängt von $x$ ab. Beide Maße werden aus den vorgegebenen Gewichten der Projektform gebildet.

**Isometrische Übergänge.** Für $\Omega\subset\Omega'$ sei $N=\Omega'\setminus\Omega$. Bis auf Nullmengen gilt auf $\Omega$
$$
b_\Omega(x)-b_{\Omega'}(x)=
\int_N k(|x-y|)\,dy+
\sum_{q=p^j} a_q\bigl({\bf1}_N(x+h_q)+{\bf1}_N(x-h_q)\bigr). \tag{5}
$$
Seien die Restterme beider Stufen nichtnegativ. Für ein beliebiges Zielpaar $(e,v)\in\mathcal K_\Omega$ wird die isometrische Einbettung $J_{\Omega,\Omega'}$ wie folgt definiert. Die alten Kantenwerte $e$ werden übernommen. Der Ortswert bleibt $v$ auf $\Omega$ und ist null auf $N$. Auf einer Kante zwischen $\Omega$ und $N$ setzt man $-v(x)$, wenn das alte Ende $x$ links liegt, und $+v(x)$, wenn es rechts liegt. Auf Kanten innerhalb von $N$ steht null. Nach (5) ist die Summe der neuen quadrierten Kantennormen genau $\int_\Omega(b_\Omega-b_{\Omega'})|v|^2dx$. Das beweist die Isometrie einschließlich Wohldefiniertheit auf Äquivalenzklassen. Bei drei geschachtelten Trägern stimmen direkte und zusammengesetzte Einbettung auf jeder Kante und an jedem Ortswert überein. Für die durch null fortgesetzte Eingabe gilt
$$
J_{\Omega,\Omega'}T_\Omega f=T_{\Omega'}f .
$$
Die größere Stufe definiert die Gramform zugleich für neue Tests und ihre Kreuzpaarungen mit alten Tests.

## 5. Die Kanäle 2, 3 und 4 auf vier Intervallen

Setze $d=1/32$, $I=(0,d)$, $I_m=I+\log m$ und $\Omega_j=\bigcup_{m=1}^j I_m$ für $j=2,3,4$. Ein beliebiger Horizont, der die jeweilige Menge enthält, ist zulässig. In $\Omega_4$ wirken genau diese diskreten Kanten, jeweils bei gleicher innerer Intervallkoordinate:

| Aktive Potenz | Intervallpaare | Gewicht je Kante |
|---|---|---|
| $2$ | $1$–$2$, $2$–$4$ | $\log2/\sqrt2$ |
| $3$ | $1$–$3$ | $\log3/\sqrt3$ |
| $4=2^2$ | $1$–$4$ | $\log2/2$ |

Die möglichen positiven Verhältnisse der Zentren sind $4/3,3/2,2,3,4$. Ihre logarithmischen Abstände zu abweichenden Primzahlpotenzen sind, wo relevant, mindestens $\log(5/4)>d$ (und $d<\log2$ innerhalb jedes Einzelintervalls). Deshalb hat etwa das Paar $I_2,I_3$ nur die stetige Gamma-Kopplung. Die größte Summe inzidenter Primgewichte wird auf $I_1$ erreicht und beträgt $D_{\max}=a_2+a_3+a_4$.

**Uniformer Boden.** Die Entfernung benachbarter Intervallzentren beträgt mindestens $\delta=\log(4/3)$. Für $x$ in einem Teilintervall mit Endpunktabständen $\ell,d-\ell$ liefert das Äußere dieses Einzelintervalls zunächst $F(\ell)+F(d-\ell)\ge2F(d/2)$, denn $F'=-k$ und $k$ fällt. Für die übrigen drei Intervalle werden jeweils höchstens $d\,k(\delta-d)$ abgezogen. Somit gilt
$$
b_{\Omega_4}(x)\ge
L:=2F(d/2)-3d\,k(\delta-d)-\kappa-D_{\max}>0{,}0594. \tag{6}
$$
Die gerichtete Rechnung ergibt $0{,}05940303<L<0{,}05950303$ für diese Unterabschätzung. Verwendet wurden wie in Abschnitt 3 das harmonische Intervall für $\gamma$, die Machin-Formel und die alternierende Arkustangensreihe. Für $z=(1-e^{-d/4})/(1+e^{-d/4})$ wurde $2F(d/2)=-\log z+\pi/2-2\arctan z$ eingesetzt. Zur Gegenprüfung sind die Einzelwerte $2F(d/2)\in(7{,}10816,7{,}10817)$, $3d\,k(\delta-d)\in(0{,}20554,0{,}20555)$, $\kappa\in(5{,}37213,5{,}37224)$ und $D_{\max}\in(1{,}47098,1{,}47099)$. Aus (5) gilt derselbe untere Boden für $\Omega_2$ und $\Omega_3$. Die Breite $1/32$ liegt über der Schwelle $d_*$ von Abschnitt 3; die verwendete Testabbildung hat sich geändert.

**Beliebige endliche Zentren.** Für $m\ge2$ verschiedene feste Zentren mit Mindestabstand $\delta>0$ ist für genügend kleine gemeinsame Breite $d$ der Außenbeitrag mindestens $2F(d/2)-(m-1)d\,k(\delta-d)$. Dieser Ausdruck wächst für $d\downarrow0$ über jede Grenze. Die Primgrade bleiben durch die endliche Summe der Gewichte bis zum maximalen Durchmesser beschränkt. Also besitzt jede vorgegebene endliche Zentrenmenge eine positive gemeinsame Breite, für die (4)–(5) auf allen Teilmengen gelten. Die Breite kann von der Zentrenmenge abhängen.

## 6. Unendlich viele echte Primkanäle auf einem dünnen Träger

Auch bei einem Aufbau ohne nachträgliches Schrumpfen der alten Intervalle kann man (4)–(5) fortsetzen. Beginne mit $\Omega_4$ aus Abschnitt 5. In Schritt $n\ge1$ sei $\Omega$ die bisherige Menge, $B=\sup\Omega$ und $\varepsilon_n=2^{-n}/100$. Wir fügen ein Intervall $I_P=(R,R+\eta)$ mit $R=\log P$ für eine neue Primzahl $P$ hinzu.

1. Wähle $P$ so groß, dass für $G=R-B>2$ die Ungleichung $k(G)+G e^{-G/2}<\varepsilon_n$ gilt. Solche Primzahlen existieren, weil beide Terme gegen null gehen.
2. Wähle $0<\eta\le d\,2^{-n}$ mit $P(e^\eta-1)<1$. Für eine alte Stelle $x\ge0$ muss jede neu verbundene Primzahlpotenz im Intervall $(e^{R-x},e^{R+\eta-x})$ liegen. Seine Länge ist kleiner als eins. Daher kann bei $x$ höchstens ein neues Primgewicht hinzukommen. Dessen Größe ist höchstens $G e^{-G/2}$, da $s e^{-s/2}$ für $s>2$ fällt. Der Verlust an Gamma-Außenbeitrag ist höchstens $\eta k(G)\le k(G)$. Nach (5) verliert somit jeder alte Punkt weniger als $\varepsilon_n$.
3. Für $x\in I_P$ ist der Gamma-Außenbeitrag mindestens $2F(\eta/2)-|\Omega|\,k(G)$, wobei $|\Omega|$ die Gesamtlänge des alten Trägers bezeichnet. Alle möglichen Primnachbarn auf der neuen Gesamtmenge liegen bei Potenzen $q\le eP$. Der Grad ist insbesondere durch $2\lceil eP\rceil$ beschränkt, denn $(\log p)/\sqrt q\le(\log q)/\sqrt q<1$. Halte $P$ fest und verkleinere ausschließlich $\eta$, bis $2F(\eta/2)>|\Omega|\,k(G)+\kappa+2\lceil eP\rceil+1/20$. Das ist wegen $F(0+)=\infty$ möglich. Der neue Restterm liegt dann auf dem gesamten neuen Intervall über $1/20$.

Jeder Punkt startet mit einem Restbetrag von mindestens $1/20$. Seine späteren Verluste summieren sich auf höchstens $1/100$. **Damit gilt auf jeder Stufe $b_\Omega\ge1/25$.** Der neue Kanal $P$ wirkt wirklich: Die Translation um $\log P$ verbindet $(0,\eta)\subset I_1$ mit $I_P$. Sämtliche weiteren aktiven Kanäle sind in (4) automatisch enthalten.

Die Zielräume bilden mit den expliziten Isometrien aus (5) ein induktives System. Ihr Hilbertraum-Limes und die verträglichen $T_\Omega$ liefern eine einzige positive Gramdarstellung auf $C_c^\infty(\Omega_\infty)$, wobei $\Omega_\infty$ die Vereinigung aller so gebauten Träger ist. Jeder kompakte Test und jedes Testpaar darin liegen in einer endlichen Stufe. Auf dieser Stufe wird die Nichtpolform in einem hinreichend großen Fenster ausgewertet. Der Boden $1/25$ gilt auf dem gesamten so definierten Testraum. In dieser Fortsetzung ist die Existenz jedes weiteren Intervalls analytisch bewiesen; die konkrete numerische Einschließung (6) betrifft die vier Startintervalle.

**Warum die Trägerbeschränkung wesentlich ist.** Die Träger entweichen nach rechts, lassen offene Zwischenräume und haben sogar endliche Gesamtlänge. Tests in einem solchen Zwischenraum liegen außerhalb des Limes. Für die Nichtpolform auf *allen* glatten Tests ist eine positive Fortsetzung über ganze beliebig große Fenster unmöglich. Wähle $0\ne\phi\ge0$ in $C_c^\infty((-1,1))$ und $f_t(x)=t^{-1/2}\phi(x/t)$. Dann ist $\|f_t\|=\|\phi\|$. Wegen $\|\tau_s f_t-f_t\|\le (s/t)\|\phi'\|$ und $C_k=\int_0^\infty s^2k(s)\,ds<\infty$ gilt $E[f_t]\le C_k t^{-2}\|\phi'\|^2$. Alle Primkorrelationen sind für $f_t\ge0$ nichtnegativ und werden in (1.1) subtrahiert. Somit
$$
q_t^{\rm np}(f_t,f_t)\le C_k t^{-2}\|\phi'\|^2-\kappa\|\phi\|^2<0
\qquad\text{für hinreichend großes }t .
$$
Beide Mellinmomente dieses Gegenbeispiels sind strikt positiv. Für eine Fortsetzung auf den vollständigen Zwei-Moment-Raum muss erklärt werden, wie seine Einschränkung die ausgeschlossenen Richtungen kontrolliert. Die Konstruktion auf $\Omega_\infty$ nutzt die schon vorgegebenen arithmetischen und archimedischen Kantengewichte. Sie erklärt deren gemeinsamen intrinsischen Ursprung noch nicht. H0 bleibt Voraussetzung für den arithmetischen Anschluss; eine Folgerung über den Ritz-Schalenrest wird nicht benötigt.
