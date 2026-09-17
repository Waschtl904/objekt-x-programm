# X-C1-CONNECTED-WAXING-193/500 — rational closure below the third-mode crossing

**Datum:** 17. September 2026.  
**Status:** neue analytische Autorenableitung; externe Prüfung offen.  
**Elternstand:** `X-C1-CONNECTED-19/50` auf PR #137.  
**Auditimpuls:** der eingegangene Delta-Audit identifiziert `a=193/500` als letzten sinnvollen rationalen Testpunkt knapp unter der Nullstelle der skalarisierten Mode 2.  
**Scope:** gesamte Klasse
\[
\mathcal W_{193/500}
=
H^1_0(-193/500,193/500;\mathbb C)\cap\ker E_+\cap\ker E_-.
\]

Kein A1-Import, keine numerische Matrix, keine zusätzliche Mellinbedingung.

## 0. Ergebnis

Setze
\[
a=\frac{193}{500}=0.386,\qquad L=2a=\frac{193}{250}=0.772.
\]
Dann ist Prime 2 aktiv und Prime 3 noch inaktiv. Auf der gesamten verbundenen NULLPOL-Klasse existiert dieselbe vorwärts definierte positive Auswertung wie in den beiden vorherigen Connected-Fenstern. Insbesondere
\[
\boxed{
Q_W[u]\ge
\frac{1193}{5002000}\|u\|_2^2
>
\frac1{5000}\|u\|_2^2
\qquad
(u\in\mathcal W_{193/500}).
}
\tag{W0}
\]

Der Schritt vergrößert den rigoros geschlossenen zusammenhängenden Bereich
\[
\frac38\longrightarrow\frac{19}{50}\longrightarrow\frac{193}{500}.
\]

Die Zahl `0.3869` bleibt nur eine Warnschwelle der konkret skalarisierten Unterform. Dieses Dokument behauptet keinen Weil-No-Go oder C1-No-Go jenseits davon.

## 1. Ausgangsform und Kanalregime

Es gelten unverändert
\[
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},\qquad
\kappa_*=\log(8\pi)+\gamma+\frac\pi2.
\]
Der exakte Kanten-/Knotenansatz des Connected-Elternbeweises liefert
\[
Q_W[u]
=
\int_{x<y\in I}h(y-x)|u(y)-u(x)|^2\,dx\,dy
+
w_2\int_{-a}^{a-\log2}|u(x+\log2)-u(x)|^2\,dx
+
\int_I\rho_a(x)|u(x)|^2\,dx,
\tag{W1}
\]
für \(I=(-a,a)\), \(w_2=\log2/\sqrt2\).

Mit der klassischen Reihe
\[
\log2=2\sum_{n\ge0}\frac{3^{-(2n+1)}}{2n+1}
\]
und einem geometrischen Rest erhält man rational
\[
\frac{6931}{10000}<\log2<\frac{6932}{10000}<\frac{193}{250}.
\]
Außerdem ist \(\log3>1>193/250\), etwa weil \(e<11/4<3\). Damit ist genau der Shift \(\log2\) aktiv.

## 2. Schärferer Kernsplit auf dem ganzen Abstand \(0<t\le193/250\)

Für den neuen Endpunkt genügt der folgende stärkere Vergleich:
\[
\boxed{
\frac1{2t}+\frac14-\frac{t}{16}
<
h(t)
<
\frac1{2t}+\frac14-\frac{t}{50}
\qquad
(0<t\le193/250).
}
\tag{W2}
\]

### 2.1 Untere Schranke

Da
\[
h(t)=\frac{e^{t/2}}{2\sinh t},
\]
ist die untere Schranke äquivalent zu
\[
e^{t/2}>
\left(1+\frac t2-\frac{t^2}{8}\right)\frac{\sinh t}{t}.
\]
Für \(t<4/5\) gilt
\[
\frac{\sinh t}{t}
\le
1+\frac{t^2}{6(1-t^2/20)},
\]
weil nach dem \(t^2/6\)-Term das Verhältnis aufeinanderfolgender positiver Terme höchstens \(t^2/20\) ist. Andererseits
\[
e^{t/2}>1+\frac t2+\frac{t^2}{8}.
\]
Die Differenz dieser beiden rationalen Schranken ist
\[
-\frac{t^2(t^2-10t+10)}{6(t^2-20)}>0
\qquad(0<t\le4/5),
\]
da \(t^2-10t+10>0\) und \(t^2-20<0\).

### 2.2 Obere Schranke

Aus \(\sinh t/t\ge1+t^2/6\) und \(t/2<2/5\) folgt
\[
e^{t/2}
<
1+\frac t2+\frac{t^2}{8}+\frac{t^3}{40}.
\]
Für den Exponentialrest genügt
\[
\sum_{k\ge3}\frac{x^k}{k!}
\le
\frac{x^3/6}{1-x/4}
<
\frac{x^3}{5},
\qquad x=t/2<2/5.
\]
Weiter ist
\[
\left(1+\frac t2-\frac{t^2}{25}\right)
\left(1+\frac{t^2}{6}\right)
-
\left(1+\frac t2+\frac{t^2}{8}+\frac{t^3}{40}\right)
=
-\frac{t^2(4t^2-35t-1)}{600}>0.
\]
Damit folgt die rechte Seite von (W2).

Insbesondere bleibt der bereits benutzte schwächere Split
\[
h(t)=\frac1{2t}+\frac15+r(t),\qquad r(t)\ge0
\tag{W3}
\]
auf dem gesamten neuen Intervall gültig.

## 3. Rationaler Zentrumsnachweis

Schreibe
\[
H(s)=\int_s^\infty h(t)\,dt,
\qquad
z=\frac a4=\frac{193}{2000}.
\]
Dann
\[
2H(a)-\kappa_*
=
\log\coth z-\log(8\pi)-\gamma
-2\arctan(\tanh z).
\tag{W4}
\]

Wir zeigen
\[
\boxed{
2H(a)-\kappa_*>-\frac{3307}{2000}.
}
\tag{W5}
\]

### 3.1 Drei elementare Verbesserungen

Erstens gilt für jedes \(z>0\)
\[
\coth z>
\frac1z+\frac z3-\frac{z^3}{45}.
\tag{W6}
\]
Nach Multiplikation mit \(z\sinh z>0\) ist die Differenz
\[
z\cosh z-
\left(1+\frac{z^2}{3}-\frac{z^4}{45}\right)\sinh z,
\]
deren Potenzreihenkoeffizient bei \(z^{2m+1}\), mit \((2m+1)!\) multipliziert, gleich
\[
\frac{16}{45}m(m-1)(m-2)(m+2)
\]
ist. Er verschwindet für \(m=0,1,2\) und ist danach positiv.

Zweitens
\[
\arctan(\tanh z)
=
\int_0^z\operatorname{sech}(2s)\,ds
\le z-\frac{z^3}{2}.
\tag{W7}
\]
Denn für \(s^2\le1/6\),
\[
\cosh(2s)\ge1+2s^2\ge\frac1{1-\frac32s^2},
\]
also \(\operatorname{sech}(2s)\le1-\frac32s^2\).

Drittens benutzen wir
\[
\pi<\frac{22}{7},
\qquad
\gamma<\frac{5773}{10000}.
\tag{W8}
\]
Die Gamma-Schranke wird ohne Gleitkomma aus
\[
\gamma<H_{10000}-\log10000
\]
gewonnen. Für \(\log10000\) wird
\[
\log x
=
2\sum_{n=0}^{N-1}\frac{q^{2n+1}}{2n+1}+R_N,
\qquad
q=\frac{x-1}{x+1},
\]
nach dyadischer Reduktion verwendet, mit
\[
0<R_N<
\frac{2q^{2N+1}}{(2N+1)(1-q^2)}.
\]
Der Begleitprüfer führt die komplette rationale Rechnung aus.

### 3.2 Abschluss

Setze
\[
C_z=\frac1z+\frac z3-\frac{z^3}{45},
\qquad
X=C_z\frac7{176}.
\]
Aus derselben rationalen Logarithmusreihe folgt
\[
\log X>-\frac{8833}{10000}.
\]
Mit (W7)--(W8):
\[
\begin{aligned}
2H(a)-\kappa_*
&>
-\frac{8833}{10000}
-\frac{5773}{10000}
-\left(2z-z^3\right)\\
&>-\frac{3307}{2000}.
\end{aligned}
\]
Dies beweist (W5).

## 4. Rationaler Prime-2-Endbandnachweis

Auf einem Prime-2-aktiven Endband muss zusätzlich der Knotengrad \(w_2\) bezahlt werden. Setze
\[
\ell=\log2,\qquad d=2a-\ell.
\]
Dann
\[
W_I(\ell-a)-2H(a)
=
\int_d^a h(t)\,dt-\int_a^\ell h(t)\,dt.
\tag{W9}
\]

Mit (W2) erhalten wir
\[
\begin{aligned}
W_I(\ell-a)-2H(a)
>{}&
\frac12\log\frac{a^2}{d\ell}
-\frac{a^2-d^2}{32}
+\frac{\ell^2-a^2}{100}.
\end{aligned}
\tag{W10}
\]
Die konstanten \(1/4\)-Anteile löschen sich exakt, weil
\[
a-d=\ell-a.
\]

Aus
\[
\ell_-=\frac{6931}{10000}<\ell<\frac{6932}{10000}=\ell_+
\]
folgt konservativ
\[
\frac{a^2}{d\ell}
>
\frac{a^2}{\ell_-(2a-\ell_-)}.
\]
Für den negativen quadratischen Term wird \(d>2a-\ell_+\), für den positiven Term \(\ell>\ell_-\) verwendet. Eine achtgliedrige rationale atanh-Reihe liefert
\[
\log\frac{a^2}{\ell_-(2a-\ell_-)}
>
\frac{5011481639}{5000000000}.
\]
Daraus folgt exakt
\[
\boxed{
W_I(\ell-a)-2H(a)>
\frac{50001}{100000}>
\frac12>w_2.
}
\tag{W11}
\]
Somit wird der Prime-2-Knotengrad vollständig durch die zusätzliche äußere Gamma-Leckage der Endbänder bezahlt.

Aus (W5) und (W11) folgt auf dem ganzen Intervall
\[
\boxed{
\rho_a(x)>-\beta,\qquad
\beta=\frac{3307}{2000}.
}
\tag{W12}
\]
Also ist
\[
V_a(x)=\rho_a(x)+\beta>0.
\]

## 5. Globale Gamma-Moden: Mode 2 bleibt knapp positiv

Die singuläre Energie aus \(1/(2|x-y|)\) wird wie im Elternbeweis auf dem ganzen verbundenen Intervall diagonalisiert:
\[
\mathcal E_0[u]
=
\sum_{n\ge0}\mathsf H_n|u_n|^2.
\tag{W13}
\]
Der konstante Anteil \(1/5\) liefert jetzt
\[
\frac{L}{5}\sum_{n\ge1}|u_n|^2
=
\frac{193}{1250}\sum_{n\ge1}|u_n|^2.
\tag{W14}
\]

Nach Ausgliederung der positiven \(r\)-Kanten, des Prime-2-Differenzports und des positiven Knotengewichts \(V_a\) verbleibt
\[
\sum_{n\ge2}\lambda_n|u_n|^2
-\frac{3307}{2000}|u_0|^2
-\frac{4991}{10000}|u_1|^2,
\tag{W15}
\]
mit
\[
\lambda_n
=
\mathsf H_n+\frac{193}{1250}-\frac{3307}{2000}.
\]
Insbesondere
\[
\lambda_1=-\frac{4991}{10000},
\qquad
\boxed{\lambda_2=\frac9{10000}>0.}
\tag{W16}
\]
Da die harmonischen Zahlen wachsen, gilt
\[
\lambda_n\ge\frac9{10000}\qquad(n\ge2).
\]
In dieser konkreten Unterform bleiben also weiterhin genau zwei negative niedrige Moden.

## 6. Dieselben zwei globalen Mellinmomente schließen den Defekt

Auf \(|x|\le193/500\), also \(|x|/2\le193/1000\), gelten noch
\[
\frac{\|c_\perp\|}{c_0}<\frac1{50},
\qquad
\frac{\|s_\perp\|}{s_1}<\frac1{150},
\tag{W17}
\]
für \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\).

Tatsächlich genügen
\[
\cosh z-1
\le
\frac{z^2}{2(1-z^2/12)}
<\frac1{50},
\]
und
\[
\frac{\sinh z}{z}-1
\le
\frac{z^2}{6(1-z^2/20)}
<\frac1{150},
\qquad z=\frac{193}{1000}.
\]

Die zwei NULLPOL-Bedingungen rekonstruieren \(u_0,u_1\) aus den höheren Paritätsmoden genau wie im Elternbeweis. Für
\[
z_n=\sqrt{\lambda_n}\,u_n,\qquad n\ge2,
\]
erhält man einen festen Rang-zwei-Operator \(B_a\) mit
\[
\begin{aligned}
\|B_a\|^2
&<
\max\left\{
\frac{3307}{2000}\frac{1}{(9/10000)50^2},
\frac{4991}{10000}\frac{1}{(9/10000)150^2}
\right\}\\
&=
\boxed{\frac{3307}{4500}<1.}
\end{aligned}
\tag{W18}
\]

Damit ist
\[
S_a=(I-B_a^*B_a)^{1/2}
\tag{W19}
\]
durch eine normkonvergente Binomialreihe definiert, bevor die Weil-Normidentität verwendet wird.

## 7. Positiver Output und quantitative Untergrenze

Mit demselben Zielraumtyp wie im Connected-Elternbeweis setze
\[
T_a u=(D_Iu,\ u,\ S_a z(u)),
\tag{W20}
\]
wobei \(D_I\) die positive \(r\)-/Prime-Differenzausgabe und der zweite Eintrag die positive \(V_a(x)\,dx\)-Knotenausgabe bezeichnet.

Aus der exakten Bilanz folgt
\[
\boxed{
\|T_a u\|^2=Q_W[u].
}
\tag{W21}
\]
Die komplexe polarisierte Identität folgt ebenfalls.

Weiter:
\[
\|S_a z\|^2
\ge
\left(1-\frac{3307}{4500}\right)\|z\|^2
=
\frac{1193}{4500}\|z\|^2.
\]
Wegen \(\lambda_n\ge9/10000\) und
\[
\|u\|^2
\le
\left(1+\frac1{2500}\right)
\sum_{n\ge2}|u_n|^2
\]
erhalten wir exakt
\[
Q_W[u]
\ge
\frac{1193}{4500}
\frac9{10000}
\frac{2500}{2501}
\|u\|^2
=
\boxed{
\frac{1193}{5002000}\|u\|^2
>
\frac1{5000}\|u\|^2.
}
\]
Dies beweist (W0).

## 8. Bedeutung der Schwelle

Der neue Punkt liegt strikt unter
\[
0.3869
\]
und damit auch unter der numerisch diagnostizierten Nullstelle
\[
a_*\approx0.386942674
\]
der **skalarisierten** Mode 2. Der Begleitprüfer bestätigt lediglich die rationale Lage
\[
\frac{193}{500}=0.386<0.3869.
\]

Der methodische Befund lautet jetzt präzise:

- Die C9--C14-Zweimodenmethode ist rigoros bis \(a=193/500\) fortgesetzt.
- Ihr positiver Mode-2-Boden ist dort bereits nur \(9/10000\).
- Ein Vorzeichenwechsel dieses Bodens wäre eine Grenze dieser Unterform, kein negativer Weil-Zeuge.
- Jenseits des Crossings muss entweder mehr vorhandene positive Energie in den Hauptblock einbezogen oder Mode 2 als echter Restfreiheitsgrad über C15 beziehungsweise eine äquivalente Form-Schur-Struktur transportiert werden.

## 9. Checks und Nichtaussagen

Der Begleitprüfer benutzt nur Python-Standardbibliothek und exakte Brüche. Er führt **27 exakte rationale Checks** aus:

- rationales \(\log2\)-Enclosure und Kanalregime;
- Gültigkeit der beiden Kernschranken;
- \(\gamma<5773/10000\);
- rationaler Zentrumsnachweis;
- Prime-2-Endband-Leakage \(>1/2\);
- Taylorkontrolle der zwei Momentrekonstruktionen;
- exakte Modenkoeffizienten;
- Kontraktivität des Rang-zwei-Defekts;
- Enduntergrenze \(1193/5002000>1/5000\).

Nicht bewiesen: der Schwellenübertritt, Prime 3, das volle Einheitsfenster, all-window NP-GAP, vollständiges C1-GEOM, Objekt X oder RH. Kein A1-Replay und keine Neuheitsbehauptung.
