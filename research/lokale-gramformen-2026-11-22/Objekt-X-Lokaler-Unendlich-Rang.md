# Lokaler Unendlich-Rang-Nachweis für die Prim-/Gamma-Form von Objekt X

Mathematische Notiz · 22. November 2026 · Bezug auf die konkrete Nichtpolform in (1.1)–(1.3) am Commit `ffc81439`. Skalarprodukte sind antilinear im ersten Argument. Der Übergang von dieser Form zur arithmetischen Weil-Form setzt die dort so bezeichnete Identifikation H0 voraus. [Formdefinition und H0](https://github.com/Waschtl904/objekt-x-programm/blob/ffc81439b73d27929777819b4374a26f6d998181/handoffs/ritz-rest-2026-11-21/belege/DOMAIN_HERLEITUNG.txt)

## Satz

Seien $h=\log 2$, $d=h/4$ und $I$ ein offenes Intervall der Länge $d$. Ein fester Horizont $t$ enthalte $I$ und $I+h$ in $(-t,t)$. Auf der glatten Zwei-Moment-Testklasse
$$
D_t=\{f\in C_c^\infty((-t,t)):\ \int_{\mathbb R} e^{x/2}f(x)\,dx
=\int_{\mathbb R}e^{-x/2}f(x)\,dx=0\}
$$
hat die konkrete Nichtpolform $q_t^{\rm np}$ unendlichen Rang. Genauer gilt für jede von null verschiedene Funktion $u\in V_I:=D_t\cap C_c^\infty(I)$, mit $(\tau_hu)(x)=u(x-h)$,
$$
\operatorname{Re}q_t^{\rm np}(u,\tau_hu)
\le -h(2^{-1/2}-1/2)\,\|u\|_2^2<0 .
$$
Insbesondere kann keine lineare Abbildung in einen festen endlichdimensionalen Hilbertraum auf ganz $D_t$ diese Form als Gramform darstellen.

## Beweis

**1. Zulässige Tests.** Zweimalige partielle Integration zeigt für jedes $\phi\in C_c^\infty(I)$, dass $\phi''-\phi/4$ beide Momentbedingungen erfüllt. Der Operator $\phi\mapsto\phi''-\phi/4$ ist injektiv. Jede Lösung der homogenen Gleichung ist eine Linearkombination von $e^{x/2}$ und $e^{-x/2}$ und verschwindet identisch, sobald sie kompakten Träger in $I$ hat. Folglich ist $V_I$ unendlichdimensional. Für die verschobene Funktion gilt $E_\pm(\tau_hu)=e^{\pm h/2}E_\pm(u)$, also $\tau_hu\in D_t$.

**2. Exakter gemischter Block.** Setze $a=h/\sqrt2$ und $k(s)=e^{-s/2}/(1-e^{-2s})$. Für alle $u,w\in V_I$ gilt
$$
q_t^{\rm np}(u,\tau_hw)
=-a\langle u,w\rangle
-\int_I\int_I k(h+y-x)\,\overline{u(x)}\,w(y)\,dy\,dx. \tag{1}
$$
Denn $I$ und $I+h$ sind getrennt. Unter den Primverschiebungen trifft genau $\tau_{-h}$ die verschobene Kopie. Für jede andere positive Primzahlpotenz ab 3 beträgt der Abstand ihrer logarithmischen Verschiebung zu $h$ mindestens $\log(3/2)>d$. Der skalare Diagonalterm verschwindet. In der Gamma-Differenzform bleibt bei positivem Verschiebungsparameter nur die Kreuzrichtung vom linken zum rechten Träger. Die Substitution auf $I\times I$ ergibt genau den zweiten Term in (1).

**3. Vorzeichen und Rang.** Der Integralkern ist durch $k(h-d)$ beschränkt. Der Betrag des Integrals in (1) ist daher höchstens $d\,k(h-d)\|u\|_2\|w\|_2$. Aus $k(h-d)<k(h/2)=2^{3/4}<2$ folgt für $w=u$ die behauptete Schranke. Ist $u$ im linken Nullraum der gesamten Form und in $V_I$, so muss insbesondere $q_t^{\rm np}(u,\tau_hu)=0$ gelten. Die antilineare Abbildung $u\mapsto q_t^{\rm np}(u,\cdot)$ von $V_I$ in den algebraischen Dualraum von $D_t$ ist daher injektiv. Schon die Auswertung auf $\tau_h V_I$ erkennt ihren Kern. Das beweist unendlichen Rang. Eine lineare Abbildung von $V_I$ in endlich viele Dimensionen hätte einen nichttrivialen Kern. Auf einem solchen Kernvektor würde die geforderte Gramidentität der Schranke widersprechen. Eine Stetigkeitsannahme an die Testabbildung ist dafür entbehrlich. ∎

Vor der Kompression hat der gesamte Kanal $p=2$ den Multiplikator $-2h\sum_{j\ge1}2^{-j/2}\cos(jh\xi)=2\operatorname{Re}(L_2'/L_2)(1/2+i\xi)$ mit $L_2(s)=(1-2^{-s})^{-1}$. Die beiden Verschiebungsrichtungen erklären den Faktor zwei im Multiplikator. In (1) trifft genau eine Richtung bei $j=1$.

## Schärfere Folgerung für Approximationen

Sei $H_I=\overline{V_I}^{L^2(I)}$. Bezeichne mit $B_I$ den durch $\langle u,B_Iw\rangle=q_t^{\rm np}(u,\tau_hw)$ bestimmten beschränkten Operator auf $H_I$. Aus (1) folgt $B_I=-a\,\mathrm{Id}+K_I$. Der stetige Kern des zweiten Summanden auf dem beschränkten Quadrat ist quadratintegrierbar. Sein Integraloperator und seine Kompression auf $H_I$ sind kompakt.

Der Abstand von $B_I$ zu den kompakten Operatoren in der $L^2$-Operatornorm ist **exakt $a=\log(2)/\sqrt2$**. Die obere Schranke folgt durch Wahl von $K_I$. Für jeden kompakten Operator $C$ und jede Orthonormalfolge $(e_n)$ in $H_I$ gilt $\|(K_I-C)e_n\|\to0$. Also $\|(B_I-C)e_n\|\to a$. Eine Folge endlichrangiger Operatoren kann auf jedem einzelnen Test konvergieren, etwa durch Projektion auf wachsende dichte Teilräume. Ihr Fehler gegenüber diesem Block bleibt auf der ganzen $L^2$-Einheitskugel mindestens $a$. Diese Aussage betrifft die Norm des gemischten Blocks auf dem angegebenen Intervall.
