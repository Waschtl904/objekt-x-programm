# P11-C1z-B2-C7b — Protected Jump Pair / Off-Diagonal Gram / Integrated Observability Test

**Datum:** 2026-08-10  
**Programm:** P11 / C1z / B2 / C7  
**Knoten:** `[P11-C1z-B2-C7b]`  
**Vorgänger:** C7a — `ActualJumpCoefficientCensus`  
**Block:** `ResidualArithmeticObservability_WindowedExponentialSums`  
**Modus:** `PASS-A ACTIVE`  
**Scope:** Direktaudit der in C7a isolierten Offdiagonalgröße; keine SYN-, Seal- oder Paper-Aktion.

---

## 0. Auditstatus

\[
\boxed{
\begin{aligned}
[P11\text{-}C1z\text{-}B2\text{-}C7b]
&\quad \checkmark[K/M]_{\rm part}\\
&+\checkmark[M]_{\rm pos,exact\text{-}finite\text{-}X\text{-}Gram\text{-}identity}\\
&+\checkmark[M]_{\rm pos,protected\text{-}pair\text{-}self\text{-}energy}\\
&+\checkmark[M]_{\rm pos,\mathfrak G_T/X\text{-}sufficient}\\
&+\checkmark[M]_{\rm pos,TV\text{-}min\text{-}gap\text{-}conditional}\\
&+\checkmark[M]_{\rm neg,TV\text{-}and\text{-}moments\not\Rightarrow\mathfrak G_T\text{-}control}\\
&+\checkmark[M]_{\rm neg,candidate\text{-}gap\text{-}route}\\
&+\checkmark[M]_{\rm neg,protected\text{-}pair\text{-}alone\not\Rightarrow full\text{-}Gram\text{-}lower\text{-}bound}\\
&+\checkmark[M]_{\rm corr,\mathfrak G_T/X\text{-}envelope\text{-}not\text{-}necessary}\\
&+\checkmark[M]_{\rm pos,scale\text{-}adapted\text{-}sinc\text{-}envelope}\\
&+\checkmark[M]_{\rm neg,absolute\text{-}offdiagonal\text{-}route\text{-}from\text{-}current\text{-}data}\\
&+?[O]_{\rm signed\text{-}or\text{-}clustered\text{-}Gram\text{-}control}\\
&+?[O]_{\rm actual\text{-}\mathfrak G_T/X_T\text{-}asymptotic}\\
&+?[O]_{\rm window\text{-}lower\text{-}transfer}\\
&+?[O]_{\rm q_{r,T}\;asymptotic}\\
&+?[O]_{\rm a_{R,T}^{(2)}\neq0}.
\end{aligned}
}
\]

### Kernurteil

C7b beantwortet die in C7a formulierte Kernfrage in zwei Ebenen.

**Erstens:** Für das tatsächliche Residual-Sprungpolynom

\[
P_T(\xi)=\sum_{\beta\in\mathcal B_T^{\rm act}}J_T(\beta)e^{-i\xi\beta}
\]

ist die finite-horizon Gramform exakt

\[
\boxed{
\frac1{2X}\int_{-X}^{X}|P_T(\xi)|^2\,d\xi
=
\sum_\beta |J_T(\beta)|^2
+
\sum_{\beta\ne\gamma}
J_T(\beta)\overline{J_T(\gamma)}
\frac{\sin(X(\beta-\gamma))}{X(\beta-\gamma)}.
}
\tag{C1zB2C7b.1}
\]

Damit ist

\[
\mathfrak G_T
:=
\sum_{\beta\ne\gamma}
\frac{|J_T(\beta)J_T(\gamma)|}{|\beta-\gamma|}
\]

nur eine **hinreichende absolute Hülle** für den Offdiagonalterm:

\[
\left|\operatorname{OffDiag}_T(X)\right|
\le \frac{\mathfrak G_T}{X}.
\]

**Zweitens:** Aus den bisher bewiesenen C6/C7a-Daten lässt sich keine hinreichende asymptotische Kontrolle von \(\mathfrak G_T/X_T\) auf der C6z-relevanten Skala ableiten. Die Route

\[
\text{Protected Pair}+TV+\text{Momente}+\text{Kandidatenabstände}
\Longrightarrow
\mathfrak G_T=o(X_T)
\]

ist nicht verfügbar. Mehr noch: Ein abstrakter Stufenfunktions-Gegenbau zeigt, dass Protected Pair, Mittelwertnullheit und eine uniforme TV-Schranke **logisch nicht genügen**, um \(\mathfrak G_T\) zu kontrollieren.

Das ist aber **kein Gegenbeweis gegen das tatsächliche Residual** \(r_T\). C7b widerlegt nicht

\[
\mathfrak G_T/X_T\to0
\]

für die echten Koeffizienten. Es zeigt vielmehr, dass diese Aussage nicht aus den bisher inventarisierten Grobdaten folgt und dass \(\mathfrak G_T\) selbst den exakten Gramkern bei Nahkollisionen unnötig singularisiert.

Die korrekte finite-scale Größe ist daher zunächst

\[
\boxed{
\mathfrak C_T(X)
:=
\sum_{\beta\ne\gamma}
|J_T(\beta)J_T(\gamma)|
\min\left\{1,\frac1{X|\beta-\gamma|}\right\},
}
\tag{C1zB2C7b.2}
\]

oder noch besser der **signierte exakte** Offdiagonalterm selbst.

Daher lautet das C7b-Endurteil:

\[
\boxed{
\text{Die absolute }\mathfrak G_T/X\text{-Route ist als derzeitiger R3-Beweisweg BLOCKIERT/ÜBERSTARK.}
}
\]

C7c `Window-Lower-Transfer` wird durch C7b **nicht freigeschaltet**.

---

# 1. Verbindliche Eingaben aus C7a

C7a arbeitet mit der Nullfortsetzung des Residualvektors

\[
\widetilde r_T
=
\widetilde h_T
-\lambda_T\widetilde{\mathbf1_T}
-\lambda_T\widetilde g_T,
\qquad
 g_T:=R_T^*R_T\mathbf1_T,
\]

und den tatsächlichen Sprüngen

\[
J_T(\beta)
:=\operatorname{Jump}_\beta\widetilde r_T.
\]

Der exakte Residual-Zensus lautet

\[
\boxed{
J_T(\beta)
=
J_{h,T}(\beta)
-\lambda_TJ_{1,T}(\beta)
-\lambda_TJ_{g,T}(\beta).
}
\tag{C1zB2C7b.3}
\]

Ein Kandidatenpunkt ist genau dann tatsächlicher Residual-Breakpoint, wenn

\[
J_T(\beta)\ne0.
\]

Da \(r_T\) reell und gerade ist,

\[
\boxed{J_T(-\beta)=-J_T(\beta).}
\tag{C1zB2C7b.4}
\]

C7a/C6i liefern für große \(T\) das geschützte Paar

\[
\boxed{
\pm x_T,
\qquad
x_T=T-\frac12\log(q_T/2),
\qquad
q_T\in\{3,5\},
}
\tag{C1zB2C7b.5}
\]

mit

\[
\boxed{
|J_T(x_T)|\ge j_*>0,
\qquad
J_T(-x_T)=-J_T(x_T),
}
\tag{C1zB2C7b.6}
\]

und dort verschwinden Identitäts- und Restbeitrag exakt. Das Paar ist also \(\lambda_T\)-frei.

C7a liefert außerdem für jedes feste große \(T\)

\[
\boxed{
\lim_{X\to\infty}
\frac1{2X}\int_{-X}^{X}|P_T(\xi)|^2\,d\xi
=
\sum_{\beta\in\mathcal B_T^{\rm act}}|J_T(\beta)|^2
\ge 2j_*^2.
}
\tag{C1zB2C7b.7}
\]

Die offene Frage ist die quantitative \(T\)-Skala dieser Konvergenz.

---

# 2. Exakte finite-\(X\)-Gramidentität

Setze

\[
K_X(t)
:=
\begin{cases}
\dfrac{\sin(Xt)}{Xt},&t\ne0,\\[1ex]
1,&t=0.
\end{cases}
\tag{C1zB2C7b.8}
\]

Dann gilt für jedes Paar \(\beta,\gamma\)

\[
\frac1{2X}
\int_{-X}^{X}
e^{-i\xi(\beta-\gamma)}\,d\xi
=K_X(\beta-\gamma).
\]

Da \(\mathcal B_T^{\rm act}\) für festes \(T\) endlich ist, darf die Summe ohne Grenzproblem in das Integral gezogen werden. Daher

\[
\begin{aligned}
\frac1{2X}\int_{-X}^{X}|P_T(\xi)|^2\,d\xi
&=
\sum_{\beta,\gamma}
J_T(\beta)\overline{J_T(\gamma)}K_X(\beta-\gamma)\\
&=
D_T+S_T(X),
\end{aligned}
\]

mit

\[
\boxed{D_T:=\sum_\beta|J_T(\beta)|^2}
\tag{C1zB2C7b.9}
\]

und

\[
\boxed{
S_T(X)
:=
\sum_{\beta\ne\gamma}
J_T(\beta)\overline{J_T(\gamma)}K_X(\beta-\gamma).
}
\tag{C1zB2C7b.10}
\]

Somit folgt exakt (C1zB2C7b.1).

Aus dem Protected Pair folgt

\[
\boxed{D_T\ge2j_*^2.}
\tag{C1zB2C7b.11}
\]

### Firewall C7b-A — Diagonale ist nicht finite-band Observability

Die positive Diagonale allein liefert **keine** finite-band Untergrenze, weil \(S_T(X)\) negativ sein kann.

Die gesamte Gramform ist zwar nichtnegativ,

\[
D_T+S_T(X)\ge0,
\]

aber für eine uniforme quantitative Untergrenze muss die negative Offdiagonalinterferenz kontrolliert werden.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,exact\text{-}finite\text{-}X\text{-}Gram\text{-}identity}.}
\]

---

# 3. Exakte Eigenenergie des Protected Pair

Schreibe

\[
j_T:=J_T(x_T).
\]

Der alleinige Beitrag des geschützten Paares ist

\[
P_T^{\rm prot}(\xi)
=
j_Te^{-i\xi x_T}-j_Te^{i\xi x_T}
=-2ij_T\sin(\xi x_T).
\tag{C1zB2C7b.12}
\]

Daher

\[
\begin{aligned}
\frac1{2X}
\int_{-X}^{X}|P_T^{\rm prot}(\xi)|^2\,d\xi
&=
\frac{4j_T^2}{2X}
\int_{-X}^{X}\sin^2(\xi x_T)\,d\xi\\
&=
2j_T^2
\left(
1-
\frac{\sin(2Xx_T)}{2Xx_T}
\right).
\end{aligned}
\]

Also

\[
\boxed{
\frac1{2X}
\int_{-X}^{X}|P_T^{\rm prot}(\xi)|^2\,d\xi
=
2j_T^2
\left(
1-
\frac{\sin(2Xx_T)}{2Xx_T}
\right).
}
\tag{C1zB2C7b.13}
\]

Für festes \(T\) und \(X\to\infty\) geht dies gegen

\[
2j_T^2\ge2j_*^2.
\]

Das bestätigt: Das Protected Pair besitzt selbst eine robuste integrierte Eigenenergie.

### Firewall C7b-B — Protected Pair ist kein orthogonaler Summand

Schreibe

\[
P_T=P_T^{\rm prot}+P_T^{\rm rest}.
\]

Dann

\[
\|P_T\|_{L^2(-X,X)}^2
=
\|P_T^{\rm prot}\|^2
+
\|P_T^{\rm rest}\|^2
+2\Re\langle P_T^{\rm prot},P_T^{\rm rest}\rangle.
\]

Der Kreuzterm kann negativ sein. Deshalb folgt aus (C1zB2C7b.13) **nicht**

\[
\frac1{2X}\int|P_T|^2\ge c>0
\]

uniform in \(T\), solange keine Kreuztermkontrolle vorliegt.

Status:

\[
\boxed{\checkmark[M]_{\rm neg,protected\text{-}pair\text{-}alone\not\Rightarrow full\text{-}Gram\text{-}lower\text{-}bound}.}
\]

---

# 4. Die C7a-Größe \(\mathfrak G_T\): exakt hinreichend

Aus

\[
|\sin y|\le1
\]

folgt für \(t\ne0\)

\[
|K_X(t)|
\le
\frac1{X|t|}.
\]

Daher

\[
|S_T(X)|
\le
\frac1X
\sum_{\beta\ne\gamma}
\frac{|J_T(\beta)J_T(\gamma)|}{|\beta-\gamma|}.
\]

Definiere wie C7a

\[
\boxed{
\mathfrak G_T
:=
\sum_{\beta\ne\gamma}
\frac{|J_T(\beta)J_T(\gamma)|}{|\beta-\gamma|}.
}
\tag{C1zB2C7b.14}
\]

Dann

\[
\boxed{|S_T(X)|\le\frac{\mathfrak G_T}{X}.}
\tag{C1zB2C7b.15}
\]

und wegen \(D_T\ge2j_*^2\)

\[
\boxed{
\frac1{2X}\int_{-X}^{X}|P_T(\xi)|^2\,d\xi
\ge
2j_*^2-rac{\mathfrak G_T}{X}.
}
\tag{C1zB2C7b.16}
\]

Somit wäre jede Skala \(X_T\) mit

\[
\boxed{\mathfrak G_T=o(X_T)}
\tag{C1zB2C7b.17}
\]

hinreichend für eine asymptotische positive integrierte R3-Schranke.

Das ist eine korrekte **hinreichende** Bedingung.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,\mathfrak G_T/X\text{-}sufficient}.}
\]

---

# 5. Grobe Kontrolle durch tatsächlichen Minimalabstand und TV

Für festes \(T\) definiere den tatsächlichen Minimalabstand

\[
\boxed{
\delta_T^{\rm act}
:=
\min_{\substack{\beta,\gamma\in\mathcal B_T^{\rm act}\\\beta\ne\gamma}}
|\beta-\gamma|>0.
}
\tag{C1zB2C7b.18}
\]

Dann

\[
\mathfrak G_T
\le
\frac1{\delta_T^{\rm act}}
\sum_{\beta\ne\gamma}|J_T(\beta)J_T(\gamma)|.
\]

Für die Nullfortsetzung einer kompakten Stufenfunktion ist

\[
\sum_\beta|J_T(\beta)|
=\operatorname{TV}(\widetilde r_T).
\]

Daher

\[
\sum_{\beta\ne\gamma}|J_T(\beta)J_T(\gamma)|
\le
\left(\sum_\beta|J_T(\beta)|\right)^2
=
\operatorname{TV}(\widetilde r_T)^2.
\]

Also

\[
\boxed{
\mathfrak G_T
\le
\frac{\operatorname{TV}(\widetilde r_T)^2}{\delta_T^{\rm act}}.
}
\tag{C1zB2C7b.19}
\]

C6z liefert unter der dort ausdrücklich zugelassenen Schranke

\[
\lambda_T\le CTe^T
\]

die grobe Variation

\[
\operatorname{TV}(\widetilde r_T)
\lesssim T^2e^{2T}.
\]

Damit

\[
\boxed{
\mathfrak G_T
\lesssim
\frac{T^4e^{4T}}{\delta_T^{\rm act}}.
}
\tag{C1zB2C7b.20}
\]

C6z lokalisiert die relevante obere Fourier-Skala nur schwach auf Größenordnung

\[
X_T^{\rm C6z}\asymp T^5e^{9T}
\]

(bis zu festen Konstanten des gewählten Massenparameters). Setzt man diese Skala in die grobe G-Hülle ein, folgt konditional

\[
\boxed{
\frac{\mathfrak G_T}{X_T^{\rm C6z}}
\lesssim
\frac1{T e^{5T}\delta_T^{\rm act}}.
}
\tag{C1zB2C7b.21}
\]

Eine hinreichende Abstandsaussage wäre daher etwa

\[
\boxed{
T e^{5T}\delta_T^{\rm act}\longrightarrow\infty.
}
\tag{C1zB2C7b.22}
\]

Insbesondere würde jede Schranke deutlich stärker als

\[
\delta_T^{\rm act}\gtrsim e^{-5T}/T
\]

diese **grobe** Route schließen.

Aber genau eine solche globale tatsächliche Abstandsschranke ist im bisherigen Strang nicht bewiesen.

### Firewall C7b-C — (C1zB2C7b.22) ist nur hinreichend

Aus dem Scheitern einer Minimalabstandsschranke folgt nicht das Scheitern der integrierten Observability. Ein einzelnes enges Punktpaar kann im exakten sinc-Kern völlig harmlos sein.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,TV\text{-}min\text{-}gap\text{-}conditional}.}
\]

---

# 6. Warum die Kandidatengeometrie den nötigen Gap nicht liefert

C6v hat bereits synchronisierte Kandidatenfamilien identifiziert. In der dortigen Notation treten beispielsweise Lagen der Form

\[
b_{q,j}(T)
=
-T+rac12(j\log2-\log q),
\]

und transportierte Lagen

\[
v_{q,j,k}(T)
=
-T+rac12((j+k)\log2-\log q)
\]

auf. Gegen die beobachtete Lage

\[
u_q(T)=T-\frac12\log q
\]

entsteht die Differenz

\[
\boxed{
u_q(T)-v_{q,j,k}(T)
=
2T-rac12(j+k)\log2.
}
\tag{C1zB2C7b.23}
\]

Für \(j=k=N\) und

\[
T_N=\frac{N\log2}{2}
\]

ist diese Differenz exakt null; in beliebig kleinen Umgebungen solcher \(T_N\) entstehen beliebig kleine Kandidatenabstände.

Daraus folgt:

\[
\boxed{
\text{Die rohe Kandidatenlage besitzt keine uniforme globale Separation, die (C1zB2C7b.22) automatisch liefert.}
}
\tag{C1zB2C7b.24}
\]

Das beweist **nicht**, dass die entsprechenden Punkte beide in \(\mathcal B_T^{\rm act}\) überleben. Cancellations können Kandidaten entfernen. Aber genau diese Koeffizienteninformation ist R3 und darf nicht durch reine Lagegeometrie ersetzt werden.

Status:

\[
\boxed{\checkmark[M]_{\rm neg,candidate\text{-}gap\text{-}route}.}
\]

---

# 7. Logisches No-Go: Protected Pair + Momente + TV kontrollieren \(\mathfrak G\) nicht

Um exakt zu bestimmen, was die bisherigen Grobdaten leisten, betrachten wir eine **abstrakte** kompakt getragene gerade Stufenfunktion. Diese Konstruktion ist ausdrücklich **kein Modell des tatsächlichen** \(r_T\), sondern ein Implikations-Gegenbeispiel.

Fixiere

\[
0<x<a<T,
\qquad
j>0,
\]

und \(0<\varepsilon<T-a\). Auf der positiven Achse setze die Sprünge

\[
J(x)=j,
\qquad
J(a)=1,
\qquad
J(a+\varepsilon)=d_\varepsilon,
\]

mit

\[
\boxed{
d_\varepsilon
:=-\frac{xj+a}{a+\varepsilon}.
}
\tag{C1zB2C7b.25}
\]

Auf der negativen Achse setze antisymmetrisch

\[
J(-\beta)=-J(\beta).
\]

Dann gilt automatisch

\[
\sum_\beta J(\beta)=0.
\tag{C1zB2C7b.26}
\]

Außerdem

\[
\begin{aligned}
\sum_\beta\beta J(\beta)
&=2\left[xj+a+(a+\varepsilon)d_\varepsilon\right]\\
&=0.
\end{aligned}
\tag{C1zB2C7b.27}
\]

Damit erfüllt das zugehörige Sprungpolynom dieselben beiden Nullmomente

\[
P(0)=P'(0)=0.
\]

Das Paar \(\pm x\) bleibt geschützt mit Amplitude \(j\).

Die Gesamtvariation ist

\[
\operatorname{TV}
=2\left(j+1+|d_\varepsilon|\right),
\]

und bleibt für \(\varepsilon\downarrow0\) beschränkt, denn

\[
d_\varepsilon\to-\frac{xj+a}{a}.
\]

Aber die beiden geordneten Offdiagonalbeiträge zwischen \(a\) und \(a+\varepsilon\) liefern

\[
\boxed{
\mathfrak G
\ge
\frac{2|d_\varepsilon|}{\varepsilon}
\longrightarrow\infty.
}
\tag{C1zB2C7b.28}
\]

Die Sprungdaten definieren wegen (C1zB2C7b.26) eine kompakt getragene Stufenfunktion; die Antisymmetrie der Sprünge macht sie gerade, und (C1zB2C7b.27) entspricht Mittelwertnullheit.

Damit ist formal bewiesen:

\[
\boxed{
\text{Protected Pair}
+
P(0)=P'(0)=0
+
\operatorname{TV}\le C
\not\Rightarrow
\mathfrak G\le C'.
}
\tag{C1zB2C7b.29}
\]

### Firewall C7b-D — kein Gegenbeispiel gegen \(r_T\)

(C1zB2C7b.25)–(C1zB2C7b.29) sagen ausschließlich, dass die **bereits bewiesenen Grobinvarianten** die gewünschte G-Kontrolle logisch nicht erzwingen.

Sie sagen nicht, dass die echten arithmetischen Koeffizienten \(J_T(\beta)\) dieses Verhalten besitzen.

Status:

\[
\boxed{\checkmark[M]_{\rm neg,TV\text{-}and\text{-}moments\not\Rightarrow\mathfrak G_T\text{-}control}.}
\]

---

# 8. Der eigentliche strukturelle Fehler der absoluten \(\mathfrak G_T\)-Hülle

Für jedes \(t\) gilt nicht nur

\[
|K_X(t)|\le\frac1{X|t|},
\]

sondern die schärfere elementare Schranke

\[
\boxed{
|K_X(t)|
\le
\min\left\{1,\frac1{X|t|}\right\}.
}
\tag{C1zB2C7b.30}
\]

Das ist bei Nahkollisionen entscheidend.

Falls

\[
|\beta-\gamma|\ll X^{-1},
\]

ist

\[
K_X(\beta-\gamma)=1+O(X^2|\beta-\gamma|^2),
\]

also der echte Grambeitrag von Größenordnung

\[
J_T(\beta)\overline{J_T(\gamma)},
\]

nicht von Größenordnung

\[
\frac{J_T(\beta)\overline{J_T(\gamma)}}{X|\beta-\gamma|}.
\]

Die Hülle \(\mathfrak G_T/X\) erzeugt bei \(|\beta-\gamma|\to0\) daher eine künstliche Singularität, die der exakte finite-band Gramkern **nicht besitzt**.

Dies erklärt, warum (C1zB2C7b.28) die Größe \(\mathfrak G\) explodieren lassen kann, ohne automatisch einen entsprechend großen exakten Gramfehler zu erzwingen.

Folglich ist

\[
\boxed{
\mathfrak G_T=o(X_T)
}
\]

eine korrekte hinreichende, aber **nicht notwendige** Zielformulierung.

Status:

\[
\boxed{\checkmark[M]_{\rm corr,\mathfrak G_T/X\text{-}envelope\text{-}not\text{-}necessary}.}
\]

---

# 9. Die skalenadaptierte absolute Hülle

Die exakte sinc-Schranke legt die finite-scale Größe

\[
\boxed{
\mathfrak C_T(X)
:=
\sum_{\beta\ne\gamma}
|J_T(\beta)J_T(\gamma)|
\min\left\{1,\frac1{X|\beta-\gamma|}\right\}.
}
\tag{C1zB2C7b.31}
\]

nahe.

Dann gilt unmittelbar

\[
\boxed{|S_T(X)|\le\mathfrak C_T(X).}
\tag{C1zB2C7b.32}
\]

und daher

\[
\boxed{
\frac1{2X}\int_{-X}^{X}|P_T(\xi)|^2\,d\xi
\ge
D_T-\mathfrak C_T(X).
}
\tag{C1zB2C7b.33}
\]

Man kann \(\mathfrak C_T\) exakt in Nah- und Fernpaare spalten:

\[
\mathfrak N_T(X)
:=
\sum_{0<|\beta-\gamma|\le X^{-1}}
|J_T(\beta)J_T(\gamma)|,
\tag{C1zB2C7b.34}
\]

\[
\mathfrak F_T(X)
:=
\frac1X
\sum_{|\beta-\gamma|>X^{-1}}
\frac{|J_T(\beta)J_T(\gamma)|}{|\beta-\gamma|}.
\tag{C1zB2C7b.35}
\]

Dann, bis auf die harmlose Wahl der Gleichheitsgrenze,

\[
\boxed{
\mathfrak C_T(X)
=
\mathfrak N_T(X)+\mathfrak F_T(X).
}
\tag{C1zB2C7b.36}
\]

Diese Größe behandelt Nahkollisionen korrekt: Ein extrem kleiner Abstand wird nicht künstlich mit \(1/|\beta-\gamma|\) bestraft.

### Aber auch \(\mathfrak C_T\) ist nur eine absolute Hülle

In (C1zB2C7b.31) wurden weiterhin alle Vorzeichen/Phasen der tatsächlichen Koeffizienten verworfen. Daher kann auch

\[
\mathfrak C_T(X)\ll D_T
\]

stärker sein als tatsächlich nötig.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,scale\text{-}adapted\text{-}sinc\text{-}envelope}.}
\]

---

# 10. Der exakte R3-Gegenstand ist signiert

Die mathematisch minimale Größe ist nicht \(\mathfrak G_T\) und auch nicht \(\mathfrak C_T\), sondern der signierte Offdiagonalterm

\[
\boxed{
S_T(X)
=
\sum_{\beta\ne\gamma}
J_T(\beta)\overline{J_T(\gamma)}
K_X(\beta-\gamma).
}
\tag{C1zB2C7b.37}
\]

Denn exakt gilt

\[
\boxed{
\mathcal O_T(X)
:=
\frac1{2X}\int_{-X}^{X}|P_T(\xi)|^2\,d\xi
=
D_T+S_T(X).
}
\tag{C1zB2C7b.38}
\]

mit

\[
D_T\ge2j_*^2.
\]

Eine ausreichende residualspezifische R3-Aussage wäre daher beispielsweise:

\[
\boxed{
S_T(X_T)\ge -(1-\eta)D_T
}
\tag{C1zB2C7b.39}
\]

für ein \(\eta>0\) auf einer P11-relevanten Skala \(X_T\). Dann

\[
\mathcal O_T(X_T)\ge\eta D_T\ge2\eta j_*^2.
\]

Alternativ kann man eine skalenadaptierte Clusterform beweisen, in der Breakpoints auf Auflösung \(X_T^{-1}\) zunächst mit ihren **signierten** Koeffizienten aggregiert werden und erst danach die Ferninteraktion kontrolliert wird.

Diese Formulierung respektiert genau das, was C7a durch den tatsächlichen Koeffizientenzensus gewonnen hat: **Koeffizienten und Cancellations sind Teil der Struktur, nicht Störgrößen, die durch Absolutbeträge entfernt werden dürfen.**

---

# 11. Kann C7b die ursprüngliche Frage \(\mathfrak G_T/X_T\to0\) entscheiden?

Die Antwort muss zweigeteilt sein.

## 11.1 Aus den aktuellen Beweisen: nein

Die derzeit verfügbaren Daten liefern:

1. ein geschütztes Paar mit Amplitude \(\ge j_*\);
2. zwei Nullmomente des Sprungpolynoms;
3. eine grobe TV-Schranke;
4. einen exakten Koeffizientenzensus;
5. Kandidatenlagen mit logarithmischer Arithmetik;
6. aber **keine** globale quantitative Separation der tatsächlichen Breakpoints und **keine** hinreichende signierte Clusterkontrolle.

Nach §7 genügen 1–3 logisch nicht zur G-Kontrolle. Nach C6v/§6 liefert reine Kandidatengeometrie 5 ebenfalls keinen uniformen Gap.

Daher ist

\[
\boxed{?[O]_{\rm actual\text{-}\mathfrak G_T/X_T\text{-}asymptotic}.}
\]

## 11.2 Als notwendiger R3-Zieltyp: ebenfalls nein

Wegen §8 kann \(\mathfrak G_T\) durch sehr enge Punktpaare groß werden, obwohl der exakte sinc-Kern diese Paare nur mit Gewicht \(O(1)\) sieht.

Daher darf ein Scheitern von

\[
\mathfrak G_T=o(X_T)
\]

nicht als Scheitern von R3 interpretiert werden.

Das ursprüngliche C7b-Ziel wird damit **korrigiert**:

\[
\boxed{
\text{Nicht }\mathfrak G_T/X_T\to0\text{ ist fundamental, sondern eine quantitative Untergrenze für }D_T+S_T(X_T).
}
\tag{C1zB2C7b.40}
\]

---

# 12. Baker/Wüstholz: weiterhin nicht der aktuelle Engpass

Lineare-Formen-in-Logarithmen-Technik könnte später quantitative Untergrenzen für bestimmte **arithmetisch spezifizierte Lageabstände** liefern.

C7b zeigt jedoch, dass selbst perfekte Kontrolle eines einzelnen Minimalabstands nicht die konzeptionell richtige Endform sein muss:

- Nahkollisionen sind im sinc-Kern nicht singular;
- tatsächliche Cancellations entscheiden, welche Breakpoints überhaupt überleben;
- signierte Koeffizienteninterferenz ist der relevante finite-band Gegenstand.

Daher wird in C7b **kein** Baker/Wüstholz-Satz als fehlendes Standardlemma eingesetzt.

Sollte später eine konkrete Fernpaar-Separation innerhalb \(\mathfrak F_T(X)\) benötigt werden, kann diese Werkzeugklasse gezielt zurückkehren.

---

# 13. Konsequenz für C7c

Die Roadmap lässt C7c `Window-Lower-Transfer` nur bei positivem C7b-Ausgang zu.

Ein positiver C7b-Ausgang hätte eine quantitative finite-band R3-Untergrenze liefern müssen, etwa

\[
\mathcal O_T(X_T)\ge c>0
\]

oder eine äquivalente residualspezifische Observability, aus der ein unterer Transfer in die komprimierten Martingalkanäle sinnvoll angegriffen werden kann.

C7b liefert eine solche Schranke **noch nicht**. Es liefert stattdessen:

- die exakte finite-X Gramform;
- einen korrekten hinreichenden G-Test;
- ein No-Go für die Ableitung dieses Tests aus den bisherigen Grobdaten;
- und die Korrektur auf signierte/skalenadaptierte Gramkontrolle.

Daher gilt verbindlich:

\[
\boxed{
\text{C7c wird durch C7b nicht freigeschaltet.}
}
\tag{C1zB2C7b.41}
\]

Dies verhindert einen unzulässigen Window-Lower-Transfer aus einer noch offenen Observability.

---

# 14. Was genau offen bleibt

Nach C7b ist R3 enger typisiert als zuvor.

Nicht mehr offen ist die Frage, **welche** finite-band Gramform kontrolliert werden muss. Sie ist exakt (C1zB2C7b.38).

Offen ist vielmehr eine der folgenden äquivalenten/ausreichenden residualspezifischen Aussagen:

### R3-S — signierte Gramkontrolle

Finde eine P11-relevante Skala \(X_T\) und \(\eta>0\) mit

\[
S_T(X_T)\ge-(1-\eta)D_T.
\]

### R3-C — Clusterobservability

Aggregiere tatsächliche Sprünge auf Auflösung \(X_T^{-1}\), erhalte signierte Clusterkoeffizienten und zeige, dass genügend Clusterenergie nach den tatsächlichen Cancellations überlebt.

### R3-A — skalenadaptierte absolute Kontrolle

Die stärkere hinreichende Variante wäre

\[
\mathfrak C_T(X_T)\le(1-\eta)D_T.
\]

Keine dieser Aussagen ist im aktuellen Repo bereits bewiesen.

---

# 15. C7b-Firewalls

## C7b-FW1 — \(\mathfrak G_T/X\) nur hinreichend

Nie aus

\[
\mathfrak G_T/X\not\to0
\]

auf Scheitern von R3 schließen.

## C7b-FW2 — Nahkollisionen sind nicht singular im exakten Gramkern

Immer

\[
|K_X(t)|\le1.
\]

Die Singularität \(1/(X|t|)\) ist nur die Fernpaarhülle.

## C7b-FW3 — tatsächlicher versus Kandidatenabstand

C6v-Nahkollisionen betreffen Kandidatenlagen. Sie dürfen nicht automatisch als zwei tatsächliche Residualbreakpoints gezählt werden.

## C7b-FW4 — TV kontrolliert keine Offdiagonalgeometrie

Eine TV-Schranke kontrolliert \(\sum|J|\), nicht die paarweisen Abstände. §7 zeigt dies explizit.

## C7b-FW5 — Protected Pair ist kein orthogonaler Summand

Seine positive Eigenenergie kann durch Kreuzterme auf einem endlichen Band teilweise interferieren.

## C7b-FW6 — keine Aktivierung von C7c ohne quantitative R3-Untergrenze

Der Window-Lower-Transfer bleibt gesperrt.

## C7b-FW7 — kein q-Schluss

C7b beweist weder

\[
q_{r,T}\to0
\]

noch

\[
q_{r,T}\not\to0.
\]

## C7b-FW8 — kein Schluss zu \(a_{R,T}^{(2)}\)

Der separate offene Koeffizient

\[
a_{R,T}^{(2)}\ne0
\]

wird nicht gelöst.

---

# 16. Endurteil

Der in C7a vorgeschlagene Test

\[
\mathfrak G_T/X_T\to0
\]

war ein sinnvoller erster quantitativer Zugriff, aber C7b zeigt, dass er nicht der intrinsische R3-Gegenstand ist.

Die exakte finite-horizon Struktur ist

\[
\boxed{
\mathcal O_T(X)
=
D_T+S_T(X),
\qquad
D_T\ge2j_*^2,
}
\]

mit sinc-gewichteter signierter Offdiagonalinterferenz.

Aus den bisher bewiesenen Grobdaten kann \(\mathfrak G_T=o(X_T)\) nicht abgeleitet werden. Ein abstrakter Gegenbau zeigt sogar, dass Protected Pair, Nullmomente und TV allein keine Kontrolle von \(\mathfrak G_T\) erzwingen. Gleichzeitig ist \(\mathfrak G_T\) bei Nahkollisionen eine zu grobe Hülle, da der exakte sinc-Kern dort sättigt.

Daher:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C7b]
=\checkmark[K/M]_{\rm part}
\text{ mit }\checkmark[M]_{\rm neg,absolute\text{-}G\text{-}route}
\text{ und }?[O]_{\rm signed/clustered\text{-}R3}.
}
\]

### Abschlussentscheidung innerhalb C7

- **C7a:** DONE — tatsächliche Koeffizienten + Protected Pair + fixed-T Mean.
- **C7b:** DONE — absolute Offdiagonalroute geprüft; als derzeitiger Beweisweg blockiert/überstark; exakter signierter Zieltyp identifiziert.
- **C7c:** **NICHT GETRIGGERT**, weil quantitative R3-Untergrenze fehlt.
- **C7d:** nächster zulässiger Roadmap-Knoten ist das **Konsequenzaudit**: Welche P11-Aussage ist nach C7a/C7b tatsächlich getragen, und ist ein weiterer R3-Satz theorem-kritisch oder kann P11 schwächer geschlossen werden?
- Danach: **C7-CLOSE** und zwingendes P11-Readiness-Gate; kein automatisches C8.

---

*Audit: 2026-08-10 | P11 PASS-A ACTIVE | C7b atomic direct audit*