# X-C1-CONNECTED-WAXING-19/50 — erster kontrollierter Fensterschritt

**Datum:** 17. September 2026.  
**Status:** neue analytische Autorenableitung; externe Prüfung offen.  
**Elternstand:** `X-C1-CONNECTED-3/8` auf PR #137.  
**Scope:** gesamte Klasse

```math
\mathcal W_{19/50}=H^1_0(-19/50,19/50;\mathbb C)\cap\ker E_+\cap\ker E_-.
```

Kein A1-Import, keine numerische Matrix, keine zusätzliche Mellinbedingung.

## 0. Ergebnis

Auf `I=(-19/50,19/50)` existiert dieselbe Art vorwärts definierter positiver Auswertung wie im `3/8`-Fenster. Insbesondere

```math
\boxed{Q_W[u]\ge \frac{67}{50020}\|u\|_2^2>\frac1{1000}\|u\|_2^2\qquad(u\in\mathcal W_{19/50}).}
```

Prime 2 ist aktiv, Prime 3 noch nicht. Wegen Inklusion gilt derselbe Positivitätssatz automatisch für jede kleinere zusammenhängende NULLPOL-Quellenklasse.

Dieses Resultat ist ein **kontrollierter Window-Waxing-Schritt** von Halbbreite `3/8=0.375` auf `19/50=0.38`. Es bleibt deutlich vor dem vollen Einheitsfenster.

## 1. Was aus dem neuen Audit übernommen wird — und was nicht

Der Audit modelliert für die skalarisierte Unterform

```math
\lambda_n(a)=\mathsf H_n+\frac{2a}{5}\mathbf 1_{n\ge1}+2H(a)-\kappa_*.
```

Die numerische Nullstelle von `lambda_2` liegt bei etwa `0.386942674`. Das ist eine nützliche Diagnose der **konkret skalarisierten Unterform**, aber kein allgemeiner No-Go für die vollständige Connected-Geometrie: positive Teile des Restkernels, die variable Knotenenergie und Prime-Differenzenergie wurden in dieser Skalarisierung teilweise nur als nichtnegative Ausgänge behalten. Ein Vorzeichenwechsel von `lambda_2` beweist daher weder eine negative Weil-Richtung noch, dass C15 die einzig mögliche Fortsetzung ist.

Außerdem absorbiert die zentrale Reserve den Prime-2-Knotengrad nur bis zu einer separaten Leakage-Schwelle. Für größere Fenster müssen diese beiden Grenzen getrennt geführt werden. Am hier gewählten rationalen Zielpunkt `19/50` sind beide Bedingungen mit deutlicher rationaler Reserve erfüllt.

Die Aktivierung des Prime-3-Shifts auf einem **vollen verbundenen Intervall** geschieht bei `2a>log 3`, also bei `a>log(3)/2`; dies ist von der früheren Frage zu unterscheiden, wann eine speziell platzierte dritte Testzelle vollständig im Fenster liegt.

## 2. Exakte Kantenform

Setze

```math
a=\frac{19}{50},\qquad L=2a=\frac{19}{25},\qquad
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},\qquad
\kappa_*=\log(8\pi)+\gamma+\frac\pi2.
```

Da

```math
\log2<L<\log3,
```

ist genau der Prime-2-Shift aktiv. Wie im Elternnachweis gilt auf NULLPOL exakt

```math
Q_W[u]=\int_{x<y\in I}h(y-x)|u(y)-u(x)|^2dxdy
+w_2\int_{-a}^{a-\log2}|u(x+\log2)-u(x)|^2dx
+\int_I\rho_a(x)|u(x)|^2dx,
```

mit `w_2=log2/sqrt2` und der exakten äußeren Knotenbilanz `rho_a`.

## 3. Uniformer Kernsplit bis Länge 19/25

Auf `0<t<=19/25` gilt weiterhin

```math
\frac1{2t}+\frac15<h(t)<\frac1{2t}+\frac13.
```

Der elementare Taylorbeweis des `3/8`-Dokuments bleibt gültig; der Begleitprüfer überprüft, dass sein Polynomrest auch am neuen rechten Endpunkt strikt positiv bleibt.

Die singuläre Energie

```math
\mathcal E_0[u]=\int_{x<y\in I}\frac{|u(y)-u(x)|^2}{2(y-x)}dxdy
```

wird auf dem **ganzen** verbundenen Intervall erhalten. Mit der normierten Legendrebasis gilt skaleninvariant

```math
\mathcal E_0[u]=\sum_{n\ge0}\mathsf H_n|u_n|^2.
```

Die konstante `1/5`-Energie liefert jetzt

```math
\frac L5\sum_{n\ge1}|u_n|^2=\frac{19}{125}\sum_{n\ge1}|u_n|^2.
```

## 4. Neue Knotenreserve

Für das Zentrum genügt

```math
2H(a)-\kappa_*>-\frac{33}{20}.
```

Ein vollständig rationaler Beweis folgt aus

```math
\coth(a/4)>4/a,\qquad \arctan(\tanh(a/4))<a/4,
```

`pi<22/7`, `gamma<579/1000` und

```math
\log(418/175)<881/1000.
```

Auf den Prime-2-Endbändern muss zusätzlich der Knotengrad `w_2` bezahlt werden. Schreibe `d=L-log2`. Aus dem Kernvergleich folgt

```math
W_I(\log2-a)-2H(a)
>\frac12\log\frac{a^2}{d\log2}-\frac{2}{15}(\log2-a).
```

Mit `69/100<log2<7/10` gilt

```math
\frac{a^2}{d\log2}>\frac{1444}{483},\qquad
\log(1444/483)>407/375,
```

und daher strikt

```math
W_I(\log2-a)-2H(a)>1/2>w_2.
```

Somit gilt auf dem ganzen Intervall

```math
\rho_a(x)>-33/20.
```

Definiere

```math
V_a(x)=\rho_a(x)+33/20>0.
```

## 5. Genau zwei negative Moden bleiben

Nach Ausgliederung der positiven `r`-/Prime-Differenzenergie und `V_a` lautet der modale Rest

```math
\sum_{n\ge2}\lambda_n|u_n|^2-\frac{33}{20}|u_0|^2-\frac{249}{500}|u_1|^2,
```

mit

```math
\lambda_n=\mathsf H_n+\frac{19}{125}-\frac{33}{20}\ge
\lambda_2=\frac1{500}.
```

Es gibt am Zielpunkt also weiterhin **genau zwei** negative Moden in dieser kontrollierten Unterform.

## 6. Dieselben zwei Mellinmomente schließen den Defekt

Auf `|x|<=19/50`, also `|x|/2<=19/100`, gelten weiterhin

```math
\frac{\|\cosh(x/2)-\Pi_0\cosh(x/2)\|}{c_0}<\frac1{50},
\qquad
\frac{\|\sinh(x/2)-\Pi_1\sinh(x/2)\|}{s_1}<\frac1{150}.
```

Die zwei NULLPOL-Bedingungen rekonstruieren daher `u_0,u_1` aus den höheren Moden. Für `z_n=sqrt(lambda_n)u_n`, `n>=2`, definiert der entsprechende Rang-zwei-Operator `B_a` die negative Niedrigmodenenergie. Seine beiden Paritätszeilen sind orthogonal und

```math
\|B_a\|^2<\max\left\{
\frac{33}{20}\frac{500}{50^2},
\frac{249}{500}\frac{500}{150^2}
\right\}
=\frac{33}{100}<1.
```

Damit ist

```math
S_a=(I-B_a^*B_a)^{1/2}
```

durch die normkonvergente Binomialreihe vorwärts definiert. Zusammen mit den positiven Kanten- und Knotenoutputs erhält man die exakte komplexe Gramidentität

```math
\|T_{19/50}u\|^2=Q_W[u].
```

Außerdem

```math
\|S_az\|^2\ge\frac{67}{100}\|z\|^2,
\qquad
\|u\|^2\le\left(1+\frac1{2500}\right)\sum_{n\ge2}|u_n|^2,
```

also

```math
Q_W[u]\ge\frac{67}{50020}\|u\|^2>\frac1{1000}\|u\|^2.
```

## 7. Bedeutung für den nächsten Gate

Der Auditbefund `a≈0.38694` wird dadurch präzisiert:

- Er ist **nicht** die Grenze des bereits bewiesenen Scopes: dieser Scope wächst jetzt rigoros bis `a=0.38`.
- Er ist eine nahe Warnschwelle der gewählten zweimodigen **skalarisierten Unterform**.
- Ein rationaler nächster Versuch kann zwischen `0.38` und dieser Warnschwelle liegen; der verfügbare Modenboden wird dort jedoch schnell klein.
- Sobald diese Unterform eine dritte negative Mode besitzt, können die zwei Mellinbedingungen allein diesen dreidimensionalen Negativraum nicht durch dieselbe C9--C14-Parametrisierung beseitigen. Dann muss entweder zusätzliche bereits vorhandene positive Energie schärfer in den Hauptblock aufgenommen oder die Mode als echter Restfreiheitsgrad über eine Form-/Schur-Schnittstelle wie C15 transportiert werden.

Das ist eine **Methodengrenze**, kein Weil-No-Go.

## 8. Checks und Nichtaussagen

Der Begleitprüfer verwendet nur Python-Standardbibliothek und exakte Brüche. Er bestätigt 22 skalare/rationale Anker einschließlich Kernelbereich, Knotenreserve, Prime-2-Leakage, Modenboden, Momentfehler, Kontraktion und endgültiger rationaler Untergrenze.

Nicht bewiesen: `a>=0.38694`, Prime-3-Aktivierung, `(-1,1)`, vollständiges C1-GEOM, all-window NP-GAP oder RH. Kein A1-Replay und keine Neuheitsbehauptung.
