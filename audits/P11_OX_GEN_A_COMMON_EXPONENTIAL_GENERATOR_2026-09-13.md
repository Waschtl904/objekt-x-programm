# P11 / OX-GEN-A — gemeinsamer Exponentialgenerator der Prime- und r0-Geometrie

> **Stand:** 13. September 2026  
> **Rolle:** theorem-level interner Audit; keine Registry-Promotion, kein Object-X-/RH-Abschluss.  
> **Scope:** kompakt getragene Testfunktionen, insbesondere Nullfortsetzungen aus `H_0^1(-a,a)`; der Befund betrifft Suzukis `r_0`-Teil. `r_1` und `c_a I` bleiben offen.

## 1. Definitionen

Für `t in R` sei

```math
(T_t v)(x)=v(x+t).
```

Für `n>=2` setze

```math
c_n=\frac12\log n,
\qquad
K_n=T_{c_n}-T_{-c_n},
\qquad
\lambda_n=n^{1/4}-n^{-1/4}>0.
```

Auf kompakt getragenen `v` definieren wir die beiden Exponentialmomente

```math
E_+(v)=\int_{\mathbb R}e^{x/2}v(x)\,dx,
\qquad
E_-(v)=\int_{\mathbb R}e^{-x/2}v(x)\,dx,
```

und die Quotientenabbildung

```math
\mathcal E v=(E_+(v),E_-(v))\in\mathbb C^2.
```

Auf jedem festen Fenster `H_0^1(-a,a)` sind `E_+` und `E_-` stetige Funktionale. Die Funktionen `e^{\pm x/2}` selbst müssen dafür **nicht** in `H_0^1(-a,a)` liegen.

## 2. OX-GEN-A1 — exakte Translationrepräsentation `✓[M]`

Substitution liefert für jede kompakt getragene Testfunktion

```math
E_+(T_t v)=e^{-t/2}E_+(v),
\qquad
E_-(T_t v)=e^{t/2}E_-(v).
```

Damit

```math
\boxed{
\mathcal E T_t=\rho(t)\mathcal E,
\qquad
\rho(t)=
\begin{pmatrix}
e^{-t/2}&0\\
0&e^{t/2}
\end{pmatrix}.}
```

Insbesondere

```math
\boxed{
\mathcal E K_n=D_n\mathcal E,
\qquad
D_n=\rho(c_n)-\rho(-c_n)
=\lambda_n
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}.}
```

Äquivalent, auf den exponentiellen Generatorfunktionen selbst,

```math
\boxed{K_n e^{\pm x/2}=\pm\lambda_n e^{\pm x/2}.}
```

Dies ist fensterunabhängig. Für Nullfortsetzungen aus `H_0^1(-a,a)` entsteht **kein Randterm**:

```math
\boxed{E_\pm(K_n v)=\mp\lambda_nE_\pm(v).}
```

Damit ist `ker \mathcal E` für jedes `K_n` invariant.

## 3. OX-GEN-A2 — `r_0` ist die Charakterform derselben Darstellung `✓[M]`

Suzukis elementarer Teil ist

```math
r_0(t)=-4\left(e^{t/2}+e^{-t/2}-2\right).
```

Da

```math
\operatorname{tr}\rho(t)=e^{-t/2}+e^{t/2}=2\cosh(t/2),
```

folgt exakt

```math
\boxed{r_0(t)=-4\bigl(\operatorname{tr}\rho(t)-\operatorname{tr}\rho(0)\bigr),}
```

und daher

```math
\boxed{r_0''(t)=-\operatorname{tr}\rho(t)=-2\cosh(t/2).}
```

Prime-Kanäle und archimedischer `r_0`-Term sind somit **zwei Funktoren derselben zweidimensionalen Translationrepräsentation**: `K_n` ist eine ungerade endliche Differenz von `\rho`, während `r_0''` ihr negatives Charakter ist.

Ein direkter diskreter Anschluss lautet

```math
\lambda_n^2
=n^{1/2}+n^{-1/2}-2
=\operatorname{tr}\rho(\log n)-2,
```

also

```math
\boxed{r_0(\log n)=-4\lambda_n^2.}
```

Dies ist eine exakte Prime/Archimedean-Brücke auf der Generator-Ebene.

## 4. Polarisierte Rang-2-Form und Parität `✓[M]`

Mit Standard-Skalarprodukt auf `\mathbb C^2` (linear im ersten Argument) und dem Austauschoperator

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}
```

gilt für den polarisierten `r_0''`-Korrektor

```math
\boxed{
R_0(v,w)
=-E_+(v)\overline{E_-(w)}
-E_-(v)\overline{E_+(w)}
=\langle\mathcal E v,-P\mathcal E w\rangle_{\mathbb C^2}.}
```

Für reelle `v` folgt

```math
\boxed{R_0(v,v)=-2E_+(v)E_-(v).}
```

Die räumliche Spiegelung `(\Pi v)(x)=v(-x)` erfüllt

```math
\mathcal E\Pi=P\mathcal E.
```

Daher ist `-P` die kanonische Fundamentalform dieses Quotienten. Für gerade `v` ist `E_+=E_-` und `R_0<=0`; für ungerade `v` ist `E_+=-E_-` und `R_0>=0`. Die bekannte Paritätssignatur ist also unmittelbares Korollar der Austauschgeometrie.

## 5. Anti-Kovarianz unter allen Prime-Kanälen `✓[M]`

Sei

```math
S=\begin{pmatrix}-1&0\\0&1\end{pmatrix},
\qquad D_n=\lambda_nS.
```

Da

```math
SPS=-P,
```

gilt mit `J=-P`

```math
D_n^*JD_n=-\lambda_n^2J.
```

Somit für alle zulässigen `v,w`

```math
\boxed{R_0(K_nv,K_nw)=-\lambda_n^2R_0(v,w).}
```

Insbesondere wechselt die indefinite `R_0`-Form unter jedem nichttrivialen Kanal das Vorzeichen. Das ist eine exakte Anti-Kovarianz, keine positive Kontraktionsidentität.

## 6. Gewichtete Generatoridentität `✓[M]`

Mit

```math
w_n=\frac{\Lambda(n)}{\sqrt n}
```

gilt termweise

```math
w_n\lambda_n^2
=\Lambda(n)-2\frac{\Lambda(n)}{\sqrt n}+\frac{\Lambda(n)}n.
```

Daher für jeden endlichen Cutoff `X`

```math
\boxed{
\sum_{n\le X}w_n\lambda_n^2
=\psi(X)-A_X+\sum_{n\le X}\frac{\Lambda(n)}n,
\qquad
A_X=2\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}.}
```

Im absoluten Konvergenzgebiet besitzt die unendliche Reihe die Dirichletdarstellung

```math
\boxed{
\sum_{n\ge2}\Lambda(n)n^{-s}\lambda_n^2
=-\frac{\zeta'}\zeta\!\left(s-\frac12\right)
+2\frac{\zeta'}\zeta(s)
-\frac{\zeta'}\zeta\!\left(s+\frac12\right).}
```

## 7. Wichtige Korrektur am vorgeschlagenen Prime-only-A2

### 7.1 Die volle Prime-Gram-Form descendiert nicht auf `\mathcal E`

Die positive Prime-Form

```math
\mathfrak P_X(v,w)=\sum_{n\le X}w_n\langle K_nv,K_nw\rangle_{L^2}
```

ist **keine** Form auf dem Quotienten `v -> \mathcal E v`.

Zwar ist `ker \mathcal E` unter jedem `K_n` invariant, aber es liegt nicht im Radikal von `\mathfrak P_X`. Tatsächlich besitzt `ker \mathcal E` unendlich viele von Null verschiedene kompakt getragene Vektoren. Für einen solchen `h!=0` gilt `K_nh!=0`: aus `K_nh=0` folgte Periodizität mit Periode `2c_n`; eine kompakt getragene periodische Funktion ist Null. Also

```math
\mathfrak P_X(h,h)>0
```

sobald der Cutoff mindestens einen Kanal enthält.

Damit ist eine „Prime-Gram-Form auf dem Rang-2-Quotienten“ ohne zusätzliche Quotientennorm, Schur-Komplement-Wahl oder Komplementauswahl **nicht wohldefiniert**.

### 7.2 Die diskreten Spektraldaten `{w_n,lambda_n}` fixieren den Maßstab nicht `×[M]`

Nehme eine Hermiteform `H` auf `\mathbb C^2`, die dieselbe Anti-Kovarianz erfüllen soll:

```math
D_n^*HD_n=-\lambda_n^2H.
```

Da `D_n=\lambda_nS`, ist dies äquivalent zu

```math
SHS=-H.
```

Für

```math
H=\begin{pmatrix}a&b\\\bar b&d\end{pmatrix}
```

folgt exakt

```math
a=d=0,
\qquad
H=\begin{pmatrix}0&b\\\bar b&0\end{pmatrix}.
```

Die Kanalwirkung bestimmt also nur die off-diagonale Formklasse; der absolute Maßstab `b` bleibt frei. Die Gewichte `w_n` ändern daran nichts, da sie die Kovarianz nur mit dem Skalar `\sum w_n\lambda_n^2` multiplizieren.

**No-Go im engen Scope:** Der absolute Koeffizient `2` in `R_0(v,v)=-2E_+(v)E_-(v)` kann **nicht allein** aus den diskreten Daten `{w_n,\lambda_n}` und ihrer Anti-Kovarianz hergeleitet werden.

Der Koeffizient wird dagegen kanonisch, sobald die vollständige Translation-/Spiegelstruktur einbezogen wird: die normalisierten Funktionale `E_\pm`, der Austausch `P` und

```math
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle
```

fixieren die Form.

## 8. Forschungsstatus

### Geschlossen

- `OX-GEN-A / gemeinsame Generator-Ebene`: `✓[M]`.
- Fensterkovarianz ohne Randterm: `✓[M]`.
- Charakteridentität `r_0''=-tr rho`: `✓[M]`.
- `r_0(log n)=-4 lambda_n^2`: `✓[M]`.
- Rang-2-Faktorisierung `R_0=E^*(-P)E`: `✓[M]`.
- Prime-only-A2 aus `{w_n,lambda_n}` allein: `×[M]` im oben exakt definierten Scope.

### Offen

Der nächste nichtzirkuläre Gate ist nicht mehr die Existenz einer beliebigen Rang-2-Form, sondern:

> **OX-GEN-A2' / POSITIVE-DILATION:** Lässt sich die kanonische Translation-/Reflexions-Geometrie `(\mathbb C^2,\rho,P,\mathcal E)` intrinsisch in die positive Prime-/`log|D|`-Featuregeometrie einbetten oder als Schur-/Defektterm einer positiven Erweiterung realisieren, ohne `Q_{B_a}`, RH oder eine rückwärts definierte Positivitätswurzel zu verwenden?

Das ist die erste Stelle, an der eine positive Antwort tatsächlich einen expliziten gemeinsamen Prime-/Archimedean-Baustein konstruieren würde. Ein negatives Resultat muss eine vorab definierte natürliche Dilatations-/Intertwinerklasse ausschließen.

## 9. Firewalls

- Kein `W_a` konstruiert.
- Keine positive Hilbertfaktorisierung von `R_0`; `-P` ist indefinit.
- `r_1` und `c_aI` bleiben offen.
- Keine Aussage, dass die Generator-Ebene den dominanten Skalar erklärt.
- Keine Object-X-Realisierung und keine RH-Folgerung.
- Die numerischen Arb-Treffer des externen Reviews sind unabhängige Konsistenzchecks; die Sätze oben folgen elementar exakt und benötigen sie nicht als Beweisinput.
