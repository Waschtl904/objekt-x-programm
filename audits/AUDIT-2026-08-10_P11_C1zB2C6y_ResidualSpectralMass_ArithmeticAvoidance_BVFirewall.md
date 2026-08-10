# P11-C1z-B2-C6y — Residualspektralmasse, arithmetische Vermeidung und BV-Firewall

**Datum:** 2026-08-10  
**Programm:** P11 / C1z / B2 / C6  
**Modus:** `PASS-A ACTIVE`  
**Vorgänger:** C6x — `ExpandingPrimeMartingaleFrame_ResidualMassDistribution`  
**Scope:** genau ein atomarer Auditknoten; kein SYN, kein Seal, kein `papers/P11`.

---

## 0. Auditstatus

\[
\boxed{
\begin{aligned}
[P11\text{-}C1z\text{-}B2\text{-}C6y]
&\quad \checkmark[K/M]_{\rm part}\\
&+\checkmark[M]_{\rm pos,canonical\;zero\text{-}extension\;Fourier\;model}\\
&+\checkmark[M]_{\rm pos,mean\text{-}zero\;low\text{-}frequency\;mass\;bound}\\
&+\checkmark[M]_{\rm pos,jump\text{-}exponential\text{-}polynomial\;identity}\\
&+\checkmark[M]_{\rm pos,BV\;high\text{-}frequency\;tail\;bound}\\
&+\checkmark[M]_{\rm pos,actual\text{-}breakpoint\;spacing\Rightarrow TV/L^2\;reduction}\\
&+\checkmark[M]_{\rm corr,Dirichlet\;cost\;is\;upper\text{-}not\text{-}lower\;frequency\;bound}\\
&+\checkmark[M]_{\rm neg,breakpoint\;provenance\;alone\not\Rightarrow spectral\;avoidance}\\
&+\checkmark[M]_{\rm neg,current\;data\;give\;no\;uniform\;TV/L^2\;control}\\
&+\checkmark[M]_{\rm neg,current\;data\;give\;no\;quantitative\;quasi\text{-}null\;location}\\
&+\checkmark[M]_{\rm neg,current\;data\;give\;no\;windowed\;midband\;lower\;transfer}\\
&+\checkmark[M]_{\rm pos,residual\text{-}specific\;blocker\;localized}\\
&+?[O]_{\rm actual\;jump\text{-}coefficient\;exponential\text{-}sum\;estimate}\\
&+?[O]_{\rm q_{r,T}\;asymptotic}\\
&+?[O]_{\rm a_{R,T}^{(2)}\neq0}.
\end{aligned}
}
\]

**Kernurteil.** C6x schloss die reine ambiente Frame-Route. C6y prüft deshalb die letzte noch zulässige positive Idee: Kann die konkrete arithmetische Struktur des Residualvektors

\[
\boxed{r_T=h_T-\lambda_TA_T\mathbf1_T}
\]

seine Fouriermasse quantitativ von den C6w/C6x-Quasi-Nullregionen fernhalten?

Die Antwort aus den vorhandenen Daten ist **teilweise positiv, aber nicht hinreichend**.

Erstens liefert die exakte Mittelwertnullheit

\[
\langle r_T,\mathbf1_T\rangle=0
\]

eine echte relative Niederfrequenzschranke. Zweitens liefert die stückweise konstante Breakpointstruktur nach Nullfortsetzung eine exakte Darstellung der Fouriertransformierten durch ein endliches Sprung-Exponentialpolynom und damit einen `1/|\xi|`-Tail.

Aber beide Informationen schließen die C6-Lücke noch nicht. Die Hochfrequenzschranke hängt vom dimensionslosen Quotienten

\[
\Gamma_T:=\frac{\operatorname{TV}(\widetilde r_T)}{\|r_T\|_2},
\]

für den aktuell keine uniforme oder hinreichend quantitative Obergrenze vorliegt. Außerdem ist die in C6x verwendete Dirichlet-Schranke eine **Existenz-Obergrenze** für einen Approximationsnenner, keine Untergrenze für die erste schlechte Frequenz. Aus „der konstruierte Approximant kann astronomisch groß sein“ darf daher nicht geschlossen werden, dass alle Quasi-Nullfrequenzen erst astronomisch hoch beginnen.

Damit ist der residualspezifische Blocker jetzt präzise lokalisiert: Es fehlt ein koeffizientenempfindlicher Satz, der entweder die tatsächliche Sprungvariation relativ zu `||r_T||` kontrolliert und zugleich die schlechte Symbolmenge quantitativ lokalisiert, oder direkt die gewichteten Sprung-Exponentialsumme von `r_T` von den Quasi-Nullregionen fernhält.

---

# 1. Verbindliche Eingaben und Firewalls

Wir verwenden aus C6s/C6u/C6v/C6w/C6x nur bereits auditierten Input.

\[
A_T=I+R_T^*R_T,
\qquad
h_T=H_T^*H_T\mathbf1_T,
\]

\[
\lambda_T
=
\frac{\langle\mathbf1_T,h_T\rangle}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle},
\]

\[
\boxed{r_T=h_T-\lambda_TA_T\mathbf1_T.}
\tag{C1zB2C6y.1}
\]

Die einzige hier verwendete exakte Krylov-Orthogonalität ist

\[
\boxed{\langle r_T,\mathbf1_T\rangle=0.}
\tag{C1zB2C6y.2}
\]

Der Restquotient bleibt

\[
\boxed{
q_{r,T}
=
\frac{\|R_Tr_T\|_2^2}{\|r_T\|_2^2}.
}
\tag{C1zB2C6y.3}
\]

C6s gibt exakt

\[
\boxed{
\|R_Tf\|_2^2
=
\sum_{(p,a)\in\mathcal I_T}\mathcal E_{p,a,T}(f),
\qquad
\mathcal E_{p,a,T}(f)\ge0.
}
\tag{C1zB2C6y.4}
\]

C6x beweist dagegen auf dem ambienten mittelwertfreien Raum

\[
\inf_{f\perp\mathbf1_T}
\frac{\|R_Tf\|_2^2}{\|f\|_2^2}
\longrightarrow0.
\tag{C1zB2C6y.5}
\]

Damit ist eine positive Untergrenze nur noch über **zusätzliche Struktur des konkreten `r_T`** zulässig.

Persistente Firewalls:

- keine unbewiesene Asymptotik `\lambda_T\asymp Te^T`;
- keine Folgerung `q_{r,T}\not\to0` aus einer Untergrenze, die selbst gegen null geht;
- Kandidaten-Breakpoints sind nicht automatisch tatsächliche Breakpoints;
- Breakpoint-Lage ist nicht dasselbe wie Sprungkoeffizient;
- ambiente Quasimoden sind kein Modellbeweis für das konkrete `r_T`.

---

# 2. Eine kanonische Fourierdarstellung des Residuals

Für den Frequenztest brauchen wir keine abstrakte „Fouriertransformation auf dem Intervall“. Wir wählen eine explizite Darstellung.

Identifiziere `r_T` mit seiner Nullfortsetzung

\[
\boxed{
\widetilde r_T(u)
:=
\begin{cases}
r_T(u),&|u|\le T,\\
0,&|u|>T.
\end{cases}
}
\tag{C1zB2C6y.6}
\]

und definiere

\[
\boxed{
\widehat r_T(\xi)
:=
\int_{\mathbb R}\widetilde r_T(u)e^{-i\xi u}\,du.
}
\tag{C1zB2C6y.7}
\]

Da `r_T\in L^2([-T,T])` und kompakt getragen ist, liegt die Nullfortsetzung auch in `L^1(\mathbb R)`.

Mit dieser Konvention gilt Plancherel

\[
\boxed{
\|r_T\|_2^2
=
\frac1{2\pi}
\int_{\mathbb R}|\widehat r_T(\xi)|^2\,d\xi.
}
\tag{C1zB2C6y.8}
\]

Die Mittelwertnullheit (C1zB2C6y.2) ist exakt

\[
\boxed{
\widehat r_T(0)=0.
}
\tag{C1zB2C6y.9}
\]

Damit ist die unvermeidliche gemeinsame Symbolnullstelle bei `\xi=0` für den konkreten Residualvektor nicht völlig unkontrolliert.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,canonical\text{-}zero\text{-}extension\text{-}Fourier\text{-}model}.
}
\]

---

# 3. Exakte relative Niederfrequenzschranke aus der Mittelwertnullheit

Aus `\widehat r_T(0)=0` folgt

\[
\widehat r_T(\xi)
=
\int_{-T}^{T}
r_T(u)\bigl(e^{-i\xi u}-1\bigr)\,du.
\tag{C1zB2C6y.10}
\]

Mit

\[
|e^{-ix}-1|\le|x|
\]

erhält man

\[
|\widehat r_T(\xi)|
\le
|\xi|
\int_{-T}^{T}|u|\,|r_T(u)|\,du.
\tag{C1zB2C6y.11}
\]

Cauchy-Schwarz liefert exakt

\[
\int_{-T}^{T}|u|\,|r_T(u)|\,du
\le
\left(\int_{-T}^{T}u^2\,du\right)^{1/2}\|r_T\|_2
=
\sqrt{\frac{2T^3}{3}}\,\|r_T\|_2.
\]

Also

\[
\boxed{
|\widehat r_T(\xi)|^2
\le
\frac{2T^3}{3}\,\xi^2\,\|r_T\|_2^2.
}
\tag{C1zB2C6y.12}
\]

Integration über `|\xi|\le\delta` ergibt

\[
\begin{aligned}
\frac1{2\pi}
\int_{|\xi|\le\delta}
|\widehat r_T(\xi)|^2\,d\xi
&\le
\frac1{2\pi}
\frac{2T^3}{3}\|r_T\|_2^2
\int_{-\delta}^{\delta}\xi^2\,d\xi\\
&=
\boxed{
\frac{2}{9\pi}T^3\delta^3\|r_T\|_2^2.
}
\end{aligned}
\tag{C1zB2C6y.13}
\]

Setzt man

\[
\delta=\frac\kappa T,
\]

so folgt die dimensionslose relative Form

\[
\boxed{
\frac{
\frac1{2\pi}\int_{|\xi|\le\kappa/T}|\widehat r_T(\xi)|^2\,d\xi
}{\|r_T\|_2^2}
\le
\frac{2\kappa^3}{9\pi}.
}
\tag{C1zB2C6y.14}
\]

Zum Beispiel liegt für `\kappa=1` höchstens

\[
\frac{2}{9\pi}\approx0.0708
\]

der gesamten `L^2`-Masse in der Zone `|\xi|\le1/T`.

Das ist ein echter residualspezifischer Positivbefund: Die exakte Nullstelle `\xi=0` kann nicht einen beliebig großen Anteil der Residualnorm in einer **hinreichend schmalen `1/T`-Zone** verstecken.

Aber daraus folgt noch kein uniformer Symbolgap. Außerhalb `|\xi|\le\kappa/T` beginnen die Prime-Symbole zunächst weiterhin klein, und weiter außen treten die C6w/C6x-Quasi-Nullregionen auf.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,mean\text{-}zero\text{-}low\text{-}frequency\text{-}relative\text{-}mass\text{-}bound}.
}
\tag{C1zB2C6y.15}
\]

---

# 4. Stückkonstanz und das tatsächliche Sprungmaß

Die C6-Breakpointanalyse zeigt: Bei festem `T` entstehen `h_T`, `A_T\mathbf1_T` und damit `r_T` aus endlich vielen abgeschnittenen Shift-/Reststrukturen. Somit ist `r_T` bei festem `T` stückweise konstant mit endlich vielen tatsächlichen Breakpoints.

Wichtig ist hier das Wort **tatsächlich**. Wir definieren nicht die rohe Kandidatenmenge, sondern die nach allen Koeffizientencancellations verbleibende Sprungmenge der Nullfortsetzung:

\[
\boxed{
\mathcal B_T^{\rm act}
:=
\{\beta\in\mathbb R:
J_T(\beta):=
\widetilde r_T(\beta+)-\widetilde r_T(\beta-)\ne0\}.
}
\tag{C1zB2C6y.16}
\]

Die Endpunkte `\pm T` sind dabei eingeschlossen, sofern dort ein Sprung gegen null entsteht.

Das distributionelle Ableitungsmaß lautet exakt

\[
\boxed{
D\widetilde r_T
=
\sum_{\beta\in\mathcal B_T^{\rm act}}
J_T(\beta)\,\delta_\beta.
}
\tag{C1zB2C6y.17}
\]

Definiere die totale Sprungvariation

\[
\boxed{
V_T
:=
|D\widetilde r_T|(\mathbb R)
=
\sum_{\beta\in\mathcal B_T^{\rm act}}
|J_T(\beta)|.
}
\tag{C1zB2C6y.18}
\]

Bei festem `T` ist `V_T<\infty`.

---

# 5. Exaktes Sprung-Exponentialpolynom

Fouriertransformation von (C1zB2C6y.17) gibt für `\xi\in\mathbb R`

\[
\widehat{D\widetilde r_T}(\xi)
=
\sum_{\beta\in\mathcal B_T^{\rm act}}
J_T(\beta)e^{-i\xi\beta}.
\]

Andererseits gilt distributionell

\[
\widehat{D\widetilde r_T}(\xi)
=i\xi\widehat r_T(\xi).
\]

Definiere daher das endliche Sprung-Exponentialpolynom

\[
\boxed{
P_T(\xi)
:=
\sum_{\beta\in\mathcal B_T^{\rm act}}
J_T(\beta)e^{-i\xi\beta}.
}
\tag{C1zB2C6y.19}
\]

Dann gilt exakt

\[
\boxed{
i\xi\widehat r_T(\xi)=P_T(\xi).
}
\tag{C1zB2C6y.20}
\]

Für `\xi\ne0` also

\[
\boxed{
\widehat r_T(\xi)
=
\frac{P_T(\xi)}{i\xi}.
}
\tag{C1zB2C6y.21}
\]

Diese Formel trennt zum ersten Mal die zwei Ebenen, die in einem reinen Breakpointargument leicht vermischt werden:

1. die arithmetische **Lage** der Punkte `\beta`;
2. die tatsächlichen **Sprungkoeffizienten** `J_T(\beta)`.

Nur die gewichtete Kombination `P_T(\xi)` bestimmt die Fouriermasse.

Zwei exakte Summenregeln folgen sofort. Da `\widetilde r_T` kompakt getragen ist,

\[
\boxed{
P_T(0)=\sum_\beta J_T(\beta)=0.
}
\tag{C1zB2C6y.22}
\]

Da zusätzlich `\widehat r_T(0)=0`, ist

\[
P_T(\xi)=i\xi\widehat r_T(\xi)=O(\xi^2)
\qquad(\xi\to0),
\]

also auch

\[
\boxed{
P_T'(0)
=-i\sum_\beta\beta J_T(\beta)=0.
}
\tag{C1zB2C6y.23}
\]

Die Krylov-Mittelwertnullheit wird damit zu einer **ersten Momentrelation der tatsächlichen Sprünge**.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,jump\text{-}exponential\text{-}polynomial\text{-}identity}.
}
\]

---

# 6. Hochfrequenz-Tail aus BV

Aus (C1zB2C6y.19) folgt trivial

\[
|P_T(\xi)|
\le
\sum_\beta|J_T(\beta)|
=V_T.
\]

Daher

\[
\boxed{
|\widehat r_T(\xi)|
\le
\frac{V_T}{|\xi|}
\qquad(\xi\ne0).
}
\tag{C1zB2C6y.24}
\]

Für `X>0` ergibt sich

\[
\begin{aligned}
\frac1{2\pi}
\int_{|\xi|\ge X}
|\widehat r_T(\xi)|^2\,d\xi
&\le
\frac1{2\pi}
2V_T^2\int_X^\infty\frac{d\xi}{\xi^2}\\
&=
\boxed{
\frac{V_T^2}{\pi X}.
}
\end{aligned}
\tag{C1zB2C6y.25}
\]

Für `r_T\ne0` definiere

\[
\boxed{
\Gamma_T
:=
\frac{V_T}{\|r_T\|_2}.
}
\tag{C1zB2C6y.26}
\]

Dann lautet die relative Tail-Schranke

\[
\boxed{
\frac{
\frac1{2\pi}\int_{|\xi|\ge X}|\widehat r_T(\xi)|^2\,d\xi
}{\|r_T\|_2^2}
\le
\frac{\Gamma_T^2}{\pi X}.
}
\tag{C1zB2C6y.27}
\]

Dies bestätigt den Kern der C6y-Vorüberlegung: **hohe Frequenz kann für das konkrete stückweise Residuum tatsächlich ein Verbündeter sein.**

Aber der korrekte Skalenparameter ist nicht bloß `X`, sondern `X/\Gamma_T^2`.

Ohne quantitative Kontrolle von `\Gamma_T` ist die Aussage nicht uniform.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,BV\text{-}high\text{-}frequency\text{-}tail\text{-}bound}.
}
\]

---

# 7. Eine exakte relative Spektralband-Reduktion

Kombiniere (C1zB2C6y.14) und (C1zB2C6y.27).

Für `\kappa>0` und `M>0` setze

\[
\delta_T:=\frac\kappa T,
\qquad
X_T:=M\Gamma_T^2.
\]

Dann liegt der relative Niederfrequenzanteil unter

\[
\frac{2\kappa^3}{9\pi},
\]

und der relative Hochfrequenzanteil unter

\[
\frac1{\pi M}.
\]

Daher trägt das Zwischenband

\[
\boxed{
\mathcal A_T(\kappa,M)
:=
\left\{
\frac\kappa T<|\xi|<M\Gamma_T^2
\right\}
}
\tag{C1zB2C6y.28}
\]

mindestens den Anteil

\[
\boxed{
\frac{
\frac1{2\pi}\int_{\mathcal A_T(\kappa,M)}
|\widehat r_T(\xi)|^2\,d\xi
}{\|r_T\|_2^2}
\ge
1-
\frac{2\kappa^3}{9\pi}
-
\frac1{\pi M}.
}
\tag{C1zB2C6y.29}
\]

sofern das Band nicht leer ist; ist es leer, erzwingen die beiden Außenabschätzungen bereits die entsprechende triviale Konsistenzbedingung.

Beispielsweise ergeben `\kappa=1`, `M=10` formal mehr als `0.89` der Residualmasse im Band

\[
T^{-1}<|\xi|<10\Gamma_T^2.
\]

C6y reduziert die Spektralfrage somit tatsächlich auf ein **endliches, aber `T`-abhängiges Zwischenband**.

Der Preis ist exakt sichtbar: sein oberes Ende hängt von `\Gamma_T^2` ab.

---

# 8. Breakpoint-Abstände würden `\Gamma_T` kontrollieren — aber nur für tatsächliche Breakpoints

Schreibe die Nullfortsetzung auf ihren tatsächlichen konstanten Intervallen als

\[
\widetilde r_T
=
\sum_{j=1}^{N_T}c_{j,T}\,1_{I_{j,T}},
\]

wobei die Intervalle `I_{j,T}` paarweise disjunkt sind und positive Längen

\[
\ell_{j,T}:=|I_{j,T}|>0
\]

haben.

Für die totale Variation einschließlich der Randübergänge nach null gilt

\[
V_T
\le
2\sum_{j=1}^{N_T}|c_{j,T}|.
\tag{C1zB2C6y.30}
\]

Gewichtetes Cauchy-Schwarz liefert

\[
\sum_j|c_{j,T}|
\le
\left(\sum_j\ell_{j,T}|c_{j,T}|^2\right)^{1/2}
\left(\sum_j\ell_{j,T}^{-1}\right)^{1/2}.
\]

Also

\[
\boxed{
\Gamma_T
\le
2
\left(\sum_{j=1}^{N_T}\ell_{j,T}^{-1}\right)^{1/2}.
}
\tag{C1zB2C6y.31}
\]

Definiert man

\[
\ell_{T}^{\min}
:=
\min_j\ell_{j,T},
\]

folgt insbesondere

\[
\boxed{
\Gamma_T
\le
2\sqrt{\frac{N_T}{\ell_T^{\min}}}.
}
\tag{C1zB2C6y.32}
\]

Das ist eine wichtige Brücke zurück zu C6v:

> Eine quantitative **tatsächliche** Breakpoint-Separation plus eine Kontrolle der Anzahl tatsächlicher Intervalle würde automatisch eine quantitative `TV/L^2`-Schranke und damit einen Fourier-Tail-Cutoff liefern.

Aber C6v zeigte gerade, dass rohe transportierte Kandidaten-Separation nicht genügt. Synchronized Near-Collisions können auf Kandidatenebene arbiträr klein werden, und nur eine koeffizientenempfindliche Analyse entscheidet, welche Breakpoints in `r_T` beziehungsweise seinen Filtern tatsächlich überleben.

Daher darf (C1zB2C6y.32) nicht mit einer unbewiesenen Kandidatenradius-Schranke gefüttert werden.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,actual\text{-}breakpoint\text{-}spacing\Rightarrow TV/L^2\text{-}reduction}.
}
\]

---

# 9. Korrektur der „astronomischen Dirichlet-Frequenz“-Hoffnung

C6x verwendete für die volle bei festem `T` endliche Primfamilie simultane Dirichlet-Approximation. In Dimension `d_T` liefert die Standardaussage zu einer Güte `1/Q` einen Nenner mit

\[
1\le n\le Q^{d_T}.
\tag{C1zB2C6y.33}
\]

Diese Aussage ist eine **Obergrenze auf einen Nenner, dessen Existenz garantiert wird**.

Sie ist keine Untergrenze der Form

\[
n\ge Q^{c d_T}
\]

und erst recht keine Aussage, dass alle guten gemeinsamen Approximationen unterhalb einer astronomischen Frequenz ausgeschlossen sind.

Daher ist der Schluss

\[
\text{„viele aktive Primes“}
\Longrightarrow
\text{„jede Quasi-Nullfrequenz liegt extrem hoch“}
\]

mit den bisherigen Daten nicht bewiesen.

Um die BV-Tailschranke positiv gegen die Quasi-Nullmenge einzusetzen, bräuchte man stattdessen eine **Nichtapproximationsschranke**: Für einen kontrollierten Bereich `|\xi|\le X_T` müsste gezeigt werden, dass wenigstens ein gewichtsstarker aktiver Kanal quantitativ von seiner Nullwinkellattice getrennt bleibt.

Das ist arithmetisch eine andere Richtung als Dirichlets Existenzsatz.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,Dirichlet\text{-}upper\text{-}bound\text{-}not\text{-}quasinull\text{-}frequency\text{-}lower\text{-}bound}.
}
\tag{C1zB2C6y.34}
\]

---

# 10. Breakpoint-Provenienz ist noch keine Spektralvermeidung

Aus den C6g/C6h-Typisierungen stammen Breakpointlabels aus log-arithmetischen Familien; im Hubsektor schematisch

\[
\pm T+
\frac12
(\varepsilon_1\log n+\varepsilon_2\log m),
\qquad
\varepsilon_i\in\{-1,0,1\},
\]

und im Restsektor zusätzlich die bereits auditierten prime-puren Familien.

Setzt man solche tatsächlichen Punkte in (C1zB2C6y.19) ein, erhält man Phasen

\[
e^{-i\xi\beta}
\]

mit expliziter logarithmischer Arithmetik.

Aber die Fouriertransformierte hängt von

\[
\boxed{
P_T(\xi)
=
\sum_{\beta}J_T(\beta)e^{-i\xi\beta}
}
\]

ab, nicht von der ungewichteten Menge `\{\beta\}`.

Zwei Funktionen können dieselbe Breakpointmenge besitzen und völlig verschiedene Fouriermasse haben, wenn ihre Sprungkoeffizienten verschieden sind.

C6v hat dieselbe Firewall bereits im transportierten Kanal aufgedeckt: Kandidaten-Breakpoints können durch Koeffizientencancellation verschwinden.

Für C6y folgt deshalb:

\[
\boxed{
\text{arithmetische Breakpoint-Lage allein}
\not\Rightarrow
\text{residualspezifische Spektralvermeidung}.
}
\tag{C1zB2C6y.35}
\]

Der fehlende Gegenstand ist ein **gewichteter Exponentialsummentest für die tatsächlichen `J_T(\beta)`**.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,breakpoint\text{-}provenance\text{-}alone\text{-}insufficient}.
}
\]

---

# 11. Was die bestehende Normschranke aus C6u nicht liefert

C6u beweist die `\lambda_T`-freie Obergrenze

\[
\boxed{
\|r_T\|_2^2
\le C_rT^4e^{3T}.
}
\tag{C1zB2C6y.36}
\]

Diese Schranke kontrolliert jedoch nicht

\[
V_T=\operatorname{TV}(\widetilde r_T)
\]

und damit nicht

\[
\Gamma_T=V_T/\|r_T\|_2.
\]

Eine reine Obergrenze für den Nennervektor `\|r_T\|` ist hier sogar in der falschen Richtung: Für die relative Hochfrequenzschranke braucht man `V_T` **relativ** zu `\|r_T\|`.

Ebenso liefert der feste lokale gefilterte Sprung aus C6t nur eine positive lokale Struktur und keine globale obere Schranke für die gesamte Variation.

Daher ist derzeit nicht bewiesen, dass

\[
\Gamma_T\le e^{CT},
\qquad
\Gamma_T\le T^C,
\]

oder irgendeine andere brauchbare uniforme Wachstumsform gilt.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,current\text{-}data\text{-}no\text{-}relative\text{-}TV\text{-}control}.
}
\tag{C1zB2C6y.37}
\]

---

# 12. Der Zwischenband-Blocker

C6y hat nun einen großen Teil der Residualmasse in das Band (C1zB2C6y.28) gezwungen. Um daraus eine positive Restuntergrenze zu gewinnen, müsste dieses Band von den aktiven Kanälen quantitativ gesehen werden.

Auf Vollraum-Bulkebene besitzt jeder Prime-/Tiefenkanal ein trigonometrisches Symbol. Da bereits die ersten `p=2`- und `p=3`-Symbole keine gemeinsame nichttriviale exakte Nullstelle besitzen, ist für jedes **feste kompakte** Intervall

\[
0<\delta\le|\xi|\le X<\infty
\]

die Summe ihrer Symbolquadrate stetig und strikt positiv. Daher existiert formal ein kompakter Symbolgap

\[
\boxed{
g_{23}(\delta,X)>0.}
\tag{C1zB2C6y.38}
\]

Aber C6w zeigt zugleich

\[
\inf_{\xi\ne0}
\bigl(|m_2(\xi)|^2+|m_3(\xi)|^2\bigr)=0.
\]

Somit kann `g_{23}(\delta,X)` beim Wachsen von `X` beliebig klein werden. Außerdem geht in C6y

\[
\delta_T=\kappa/T\to0.
\]

Für das tatsächlich benötigte Band

\[
\frac\kappa T<|\xi|<M\Gamma_T^2
\]

liegt daher aus den aktuellen Daten **keine uniforme positive Untergrenze** des Bulk-Symbols vor.

Noch wichtiger: Die C6s-Energie ist eine Summe von **komprimierten endlichen-Fenster-Kanälen** auf `\Omega_{p,a,T}`. Sie ist nicht bereits als exaktes Vollraum-Fouriermultiplikatorintegral

\[
\int \Sigma_T(\xi)|\widehat r_T(\xi)|^2d\xi
\]

identifiziert.

C6x benötigte für seine Quasimoden nur eine **obere** Bulk-plus-Rand-Abschätzung. Für einen positiven C6y-Beweis bräuchte man die umgekehrte Richtung: einen unteren Fenster-zu-Bulk-Transfer auf dem konkreten `r_T`, bei dem Randverluste nicht die gesamte relevante Energie aufnehmen können.

Ein solcher Lower-Transfer-Satz ist in C6s–C6x nicht bewiesen.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,current\text{-}data\text{-}no\text{-}midband\text{-}symbol\text{-}gap\text{-}and\text{-}window\text{-}lower\text{-}transfer}.
}
\tag{C1zB2C6y.39}
\]

---

# 13. Drei präzise fehlende Bausteine

Nach den exakten Reduktionen dieses Knotens ist der residualspezifische Blocker nicht mehr vage. Mindestens eine erfolgreiche Route muss quantitativ neue Information eines der folgenden Typen liefern:

### R1 — Relative Sprungkomplexität

Eine Schranke

\[
\boxed{
\Gamma_T
=
\frac{\operatorname{TV}(\widetilde r_T)}{\|r_T\|_2}
\le G_T
}
\tag{C1zB2C6y.40}
\]

mit explizit kontrolliertem `G_T`.

Eine mögliche Quelle wäre eine koeffizientenempfindliche tatsächliche Breakpoint-Separation über (C1zB2C6y.32).

### R2 — Quantitative Quasi-Null-Nichtapproximation

Für den dadurch relevanten Frequenzbereich bis etwa `G_T^2` eine Aussage, dass die gewichtsstarken aktiven Prime-Winkel nicht alle zugleich zu nahe bei `\pi\mathbb Z` liegen.

Äquivalent: eine explizite Untergrenze für die schlechte bulk-spektrologische Funktion auf dem tatsächlich relevanten Zwischenband.

### R3 — Direkte Sprungkoeffizienten-Observability

Ein Satz über

\[
P_T(\xi)
=
\sum_\beta J_T(\beta)e^{-i\xi\beta}
\]

oder direkt über die Kanalbilder `\Phi_{p,a,T}[r_T]`, der die konkrete arithmetische Koeffizientenstruktur nutzt und eine relative Untergrenze

\[
\boxed{
\|R_Tr_T\|_2^2
\ge c\|r_T\|_2^2
}
\tag{C1zB2C6y.41}
\]

liefert.

R3 könnte R1/R2 umgehen; ohne eine solche direkte Struktur müssen R1 und R2 zusätzlich mit einem unteren Fenstertransfer gekoppelt werden.

Keine dieser quantitativ hinreichenden Aussagen folgt aus den bislang auditierten C6-Daten.

---

# 14. Warum BV allein die ambienten C6x-Quasimoden nicht ausschließt

Es wäre falsch, aus „`r_T` ist BV/stückweise“ bereits auf eine besondere Spektralvermeidung zu schließen.

Die C6x-Idee kann durch kompakt getragene hochfrequente Funktionen realisiert und in der früheren C6-Argumentation auch durch stückweise konstante Funktionen approximiert werden. Hohe Oszillation ist mit BV vereinbar; sie bezahlt lediglich durch große Variation.

Genau deshalb ist nicht die qualitative Aussage

\[
r_T\in BV
\]

entscheidend, sondern die **relative quantitative** Aussage

\[
\operatorname{TV}(r_T)
\ll
\text{kontrollierte Funktion}\times\|r_T\|_2.
\]

Ohne diese Größenrelation kann der `1/|\xi|`-Abfall erst bei einer Frequenz wirksam werden, die selbst weit jenseits aller bisher kontrollierten Skalen liegt.

Somit:

\[
\boxed{
\text{piecewise constant / BV alone}
\not\Rightarrow
\text{residual spectral avoidance}.
}
\tag{C1zB2C6y.42}
\]

---

# 15. Konsequenz für `q_{r,T}`

C6y liefert zwei echte relative Fouriermassenschranken und eine exakte Exponentialpolynomdarstellung, aber keine uniforme Restenergie-Untergrenze.

Daher bleibt weiterhin offen:

\[
q_{r,T}\to0,
\]

und ebenso

\[
q_{r,T}\not\to0.
\]

Insbesondere darf die positive Niederfrequenzschranke (C1zB2C6y.14) nicht mit einer noch fehlenden Zwischenband-Observability verwechselt werden.

Ebenso darf der BV-Tail (C1zB2C6y.27) nicht als uniforme Tail-Kontrolle gelesen werden, solange `\Gamma_T` nicht kontrolliert ist.

Die korrekte Statusaussage lautet

\[
\boxed{
\text{Residualspezifische Fouriervermeidung ist strukturell möglich, aber aus den aktuellen C6-Daten nicht bewiesen.}
}
\tag{C1zB2C6y.43}
\]

---

# 16. Konsequenz für `a_{R,T}^{(2)}`

Das übergeordnete Ziel

\[
a_{R,T}^{(2)}\ne0
\]

beziehungsweise die echte 2×2-Invertibilitätsfrage bleibt offen.

C6y schließt diese Möglichkeit nicht aus. Der Knoten zeigt jedoch, welche Information ein Beweis jetzt zwingend zusätzlich enthalten muss: tatsächliche Sprungkoeffizienten-/Spektralstruktur des konkreten Residuals, nicht nur ambiente Operatorgeometrie oder Breakpointlabels.

Damit bleibt

\[
\boxed{?[O]_{a_{R,T}^{(2)}\neq0}.}
\]

---

# 17. Gegenprüfer-Checkliste C6y

## Test 1 — Ist die Fourierdarstellung kanonisch genug für den Audit?

**Ja.** Die Nullfortsetzung nach `\mathbb R` ist explizit festgelegt; Plancherel und die Sprungformel sind damit eindeutig typisiert.

## Test 2 — Liefert `\langle r_T,1_T\rangle=0` mehr als nur einen Punktwert bei `\xi=0`?

**Ja.** Sie liefert die relative Massenschranke

\[
\frac1{2\pi}\int_{|\xi|\le\kappa/T}|\widehat r_T|^2
\le
\frac{2\kappa^3}{9\pi}\|r_T\|^2.
\]

## Test 3 — Hat die stückweise Struktur einen echten Hochfrequenznutzen?

**Ja.** Für die tatsächliche Sprungvariation gilt

\[
\frac1{2\pi}\int_{|\xi|\ge X}|\widehat r_T|^2
\le
\frac{V_T^2}{\pi X}.
\]

## Test 4 — Ist das bereits uniform relativ?

**Nein.** Dafür müsste `\Gamma_T=V_T/\|r_T\|` quantitativ kontrolliert werden.

## Test 5 — Liefert die astronomische Dirichlet-Kostenfunktion eine untere Schranke für schlechte Frequenzen?

**Nein.** `n\le Q^{d_T}` ist eine Existenz-Obergrenze, keine Nichtapproximations-Untergrenze.

## Test 6 — Reicht die bekannte arithmetische Breakpointmenge?

**Nein.** Fouriermasse hängt von den tatsächlichen Sprungkoeffizienten `J_T(\beta)` ab. Kandidaten können canceln.

## Test 7 — Gibt es wenigstens eine Brücke von tatsächlicher Separation zu Spektraltail?

**Ja.** Mit `N_T` tatsächlichen Intervallen und minimaler tatsächlicher Länge `\ell_T^{\min}` gilt

\[
\Gamma_T\le2\sqrt{N_T/\ell_T^{\min}}.
\]

Aber die dafür nötige tatsächliche quantitative Separation ist offen.

## Test 8 — Ist C6 damit mathematisch gelöst?

**Nein.** Der letzte residualspezifische Mechanismus ist jetzt präzise lokalisiert, aber nicht positiv geschlossen.

---

# 18. Persistente neue Firewalls aus C6y

## C6y-A — low-frequency firewall

\[
\boxed{
\langle r_T,1_T\rangle=0
\Rightarrow
\text{relative Kontrolle nur auf einer }O(1/T)\text{-Niederfrequenzzone, nicht globale Observability.}
}
\]

## C6y-B — BV firewall

\[
\boxed{
\operatorname{TV}(r_T)<\infty
\Rightarrow
1/|\xi|\text{-Tail, aber ohne }\operatorname{TV}(r_T)/\|r_T\|\text{-Kontrolle keine uniforme relative Aussage.}
}
\]

## C6y-C — Dirichlet-direction firewall

\[
\boxed{
\text{Dirichlet-Existenzobergrenze für Nenner}
\not\Rightarrow
\text{Untergrenze für erste Quasi-Nullfrequenz}.}
\]

## C6y-D — coefficient firewall

\[
\boxed{
\text{Breakpoint-Provenienz}
\not\Rightarrow
\text{Fouriermassenaussage ohne tatsächliche Sprungkoeffizienten}.}
\]

## C6y-E — window firewall

\[
\boxed{
\text{Vollraum-Bulk-Symbolgap}
\not\Rightarrow
\text{komprimierte Kanal-Untergrenze ohne Lower-Transfer-Satz}.}
\]

## C6y-F — q firewall

C6y liefert keine Asymptotik von `q_{r,T}`.

---

# 19. C6-Abschlusskriterium nach C6y

C6v–C6x haben die gesamte ambiente Frameklasse ausgeschlossen. C6y prüft den verbleibenden residualspezifischen Fouriermechanismus und reduziert ihn auf klar benannte neue Daten, die im bisherigen Strang fehlen.

Damit sollte der nächste Knoten **keine neue Kanalvariante** eröffnen.

Der nächste sinnvolle atomare Knoten ist

\[
\boxed{[P11\text{-}C1z\text{-}B2\text{-}C6z]}
\]

mit Arbeitstitel etwa

`C6Closure_ResidualSpectralBlocker_CompletionDecision`.

Sein Auftrag wäre nicht SYN, sondern ein lokaler C6-Abschlussaudit:

1. inventarisiere C6a–C6y und trenne positive Struktur, No-Gos und echte offene Blocker;
2. entscheide, ob der residualspezifische Blocker als sauberer **offener C6-Endpunkt** protokolliert werden kann;
3. entscheide danach, ob P11 einen neuen Arbeitsblock C7 benötigt oder ob der offene Punkt bereits außerhalb des P11-PASS-A-Scopes liegt;
4. erst nach dieser Entscheidung darf über SYN/Seal/P11-Paper gesprochen werden.

Bis dahin bleibt

\[
\boxed{P11=\texttt{PASS-A ACTIVE}.}
\]

Kein SYN, kein Seal, kein `papers/P11`.

---

# 20. Kurzfazit

C6y findet tatsächlich den in C6x fehlenden residualspezifischen Anfang: Der konkrete Residualvektor besitzt wegen seiner Mittelwertnullheit wenig Fouriermasse in einer `1/T`-Zone um null, und wegen seiner endlichen tatsächlichen Sprungvariation besitzt er einen `1/|\xi|`-Fouriertail.

Noch stärker lässt sich die gesamte Masse bis auf explizit kleine Anteile in ein Zwischenband

\[
\frac\kappa T<|\xi|<M\Gamma_T^2
\]

zwingen.

Damit wird aber gerade sichtbar, was noch fehlt. Die Größe

\[
\Gamma_T
=
\frac{\operatorname{TV}(\widetilde r_T)}{\|r_T\|_2}
\]

ist aktuell nicht kontrolliert; die Dirichlet-Kosten aus C6x lokalisieren schlechte Frequenzen nicht von unten; und die bekannte Breakpointarithmetik liefert ohne tatsächliche Sprungkoeffizienten keinen Fouriermassensatz.

Die residualspezifische Frage ist daher auf ein scharfes, koeffizientenempfindliches Problem reduziert:

\[
\boxed{
\text{Kontrolliere die tatsächlichen Sprünge von }r_T
\text{ so stark, dass seine Spektralmasse die aktive Quasi-Nullgeometrie quantitativ vermeidet.}
}
\]

Dieser Satz ist im aktuellen Repo nicht bewiesen. Genau das ist nach C6y der verbleibende C6-Blocker.

P11 bleibt `PASS-A ACTIVE` bis zum lokalen C6-Abschlussentscheid.