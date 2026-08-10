# P11-C1z-B2-C6h — Prime-pure Restlagen, lokale BV-Masse und exponentielles Fenster

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6h]`  
**Direkte Voraussetzungen:** C1z-B, C1z-B2-C3, C1z-B2-C6e, C1z-B2-C6f, C1z-B2-C6g  
**Strukturelle Schnittstellen:** C1z-B2-C6a, C1z-B2-C6b, C1z-B2-C6c, C1z-B2-C6d  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d Jet-Alignment-Firewall  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6h]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm corr,exact\text{-}rest\text{-}mark}
+
\checkmark[M]_{\rm pos,exact\text{-}p\text{-}depth\text{-}layer\text{-}formula}
+
\checkmark[M]_{\rm pos,prime\text{-}pure\text{-}jump\text{-}weight}
+
\checkmark[M]_{\rm pos,elementary\text{-}rest\text{-}crowding}
+
\checkmark[M]_{\rm pos,approximate\text{-}A\mathbf1\text{-}annihilation}
+
\checkmark[M]_{\rm neg,irrationality\text{-}input\text{-}unnecessary}
+
?[O]_{\rm corrected\text{-}separator}
+
?[O]_{\rm asymptotic\text{-}\Delta\text{-}classification}
+
?[O]_{\rm second\text{-}probe\text{-}jet\text{-}alignment}
}
\]

C6h schließt die in C6g offen gebliebene **gewichtete Rest-Crowding-Seite** auf derselben elementaren Ebene wie C6g.

Der zentrale neue Satz lautet:

Für jeden festen `c>0`, insbesondere für den C6g-Radius

\[
\boxed{
r_T=c\frac{e^{-T}}{T},}
\tag{C1zB2C6h.1}
\]

und für beide kanonischen Cross-Prime-Orte

\[
\boxed{
x_q(T)=T-\frac12\log(q/2),\qquad q\in\{3,5\},}
\tag{C1zB2C6h.2}
\]

gilt für die lokale Sprungmasse der Restmetrik

\[
A_T\mathbf1_T
=\mathbf1_T+R_T^*R_T\mathbf1_T
\]

die elementare Schranke

\[
\boxed{
\mathcal V^A_{T,q}(r_T)
\le
C_c\,T^2e^{-T}
\longrightarrow0.
}
\tag{C1zB2C6h.3}
\]

Dabei zählt `\mathcal V^A_{T,q}(r)` die absolute Masse aller tatsächlich nichtverschwindenden Sprünge von `A_T\mathbf1_T` im `r`-Fenster um `x_q(T)`; der konstante Identitätsanteil erzeugt keinen Sprung.

Der Beweis braucht **keine** quantitative Irrationalitätsabschätzung für

\[
\frac{\log p}{\log q}.
\]

Er benutzt stattdessen die exakte source-gekoppelte Martingalformel und erhält einen zusätzlichen geometrischen Dämpfungsfaktor im Sprungkoeffizienten. Konkret gilt für die gegenüberliegende prime-pure Kante

\[
y_{p,m}(T)
=-T+\frac m2\log p
\]

die blockweise Abschätzung

\[
\boxed{
\left|
\operatorname{Jump}_{y_{p,m}(T)}
\bigl(R_{p,T}^*R_{p,T}\mathbf1_T\bigr)
\right|
\le
C\,m\log p\,p^{-(m+2)/4}.
}
\tag{C1zB2C6h.4}
\]

Das ist die entscheidende Restanalogie zu C6gs Hub-Gewichtssummation. Die Restseite ist sogar günstiger: Sie bleibt prime-pure und besitzt zusätzlich den Faktor `p^{-1/2}` relativ zur bloßen Terminalskala `p^{-m/4}`.

Als direkte Konsequenz für den C6g-Haarwavelet

\[
w_{T,q,r}
=
1_{(x_q(T)-r,x_q(T))}
-
1_{(x_q(T),x_q(T)+r)}
\]
folgt

\[
\boxed{
|\langle w_{T,q,r_T},A_T\mathbf1_T\rangle|
\le
C_c\,T e^{-2T}.
}
\tag{C1zB2C6h.5}
\]

Damit ist die Restseite des robusten lokalen Separators **quantitativ fast annihiliert**, aber noch nicht exakt annihiliert. Der exakte korrigierte Separator bleibt deshalb bewusst der nächste atomare Schritt.

---

# 0. Reconciliation und exakte Ausgangsdaten

## 0.1 Korrektur der Restmarke

Die exakte Formel aus C1z-B lautet

\[
\boxed{
q_{p,k,T}(u)
:=
\mathsf Q_T(u)\eta_{p,k}
=
\sqrt{p-1}
\sum_{a=0}^{\min(k-1,J_{p,T}(u)-1)}
 p^{(a-k)/2}\psi_{p,a}.
}
\tag{C1zB2C6h.6}
\]

Der Vorfaktor ist also `\sqrt{p-1}`. Eine informelle Schreibweise mit einem Faktor `p^{-1}` wäre hier nicht die C1z-B-Formel.

Die source-gekoppelte Tiefe ist

\[
\boxed{
J_{p,T}(u)
=
\max\left\{0,
\left\lfloor
\frac{2(T-|u|)_+}{\log p}
\right\rfloor
\right\}.
}
\tag{C1zB2C6h.7}
\]

Die Martingalvektoren `\psi_{p,a}` sind orthonormal.

## 0.2 Restoperator

Wie in C6f schreiben wir

\[
\boxed{
R_Tf
=
\bigoplus_pR_{p,T}f,
}
\tag{C1zB2C6h.8}
\]

mit

\[
\boxed{
R_{p,T}f(u)
=
\sum_{k\ge1}
 b_{p,k}
 K_{k\log p}f(u)
\,q_{p,k,T}(u),
\qquad
b_{p,k}=\sqrt{\log p}\,p^{-k/4},
}
\tag{C1zB2C6h.9}
\]

wobei

\[
K_s=P_TD_sE_T.
\]

Da die Range-Sektoren `K_p^0` für verschiedene Primzahlen orthogonal sind,

\[
\boxed{
R_T^*R_T
=
\sum_pR_{p,T}^*R_{p,T}.
}
\tag{C1zB2C6h.10}
\]

Es entstehen auf der Restseite also **keine Cross-Prime-Gramterme**.

## 0.3 C6g-Radius

C6g beweist für jede feste Zielkonstante `0<\theta<1`, dass

\[
r_T=c_\theta\frac{e^{-T}}{T}
\]

die gesamte andere Hub-Sprungmasse um `x_q(T)` quantitativ klein macht.

C6h untersucht exakt denselben Radius auf der Restseite.

---

# 1. Rechte p-Tiefenlagen

Fixiere eine Primzahl `p`. Auf der rechten Terminalhälfte definiere für `j\ge0`

\[
\boxed{
I^+_{p,j,T}
:=
\left(
T-\frac{j+1}{2}\log p,
T-\frac j2\log p
\right).
}
\tag{C1zB2C6h.11}
\]

Für `u\in I^+_{p,j,T}` gilt exakt

\[
\boxed{J_{p,T}(u)=j.}
\tag{C1zB2C6h.12}
\]

Randpunkte sind maßtheoretisch irrelevant und können durch halb-offene Intervalle festgelegt werden.

Für die Konstantenfunktion `\mathbf1_T` gilt auf der rechten Hälfte

\[
K_{k\log p}\mathbf1_T(u)
=
-1
\]

genau dann, wenn

\[
T-u<\frac k2\log p.
\]

Auf `I^+_{p,j,T}` ist dies äquivalent zu

\[
\boxed{k\ge j+1.}
\tag{C1zB2C6h.13}
\]

Andererseits ist nach (C1zB2C6h.6) für `j=0`

\[
q_{p,k,T}(u)=0
\qquad\forall k.
\]

Daher

\[
\boxed{
R_{p,T}\mathbf1_T(u)=0
\qquad(u\in I^+_{p,0,T}).
}
\tag{C1zB2C6h.14}
\]

Dies ist der genaue lokale Inhalt der „flachen Tiefe“. Wichtig ist die Firewall:

\[
R_{p,T}\mathbf1_T=0
\text{ auf der äußersten Lage}
\not\Rightarrow
R_{p,T}^*R_{p,T}\mathbf1_T=0
\text{ dort},
\]

weil `R_{p,T}^*` verschobene innere Lagen zurück an den Rand transportiert.

Damit wird eine mögliche zu starke lokale Kollapsbehauptung ausdrücklich vermieden.

---

# 2. Exakte Formel für `R_{p,T}\mathbf1_T` auf einer Tiefe

Sei nun `j\ge1` und `u\in I^+_{p,j,T}`.

Für alle in (C1zB2C6h.13) aktiven `k\ge j+1` gilt

\[
\min(k-1,j-1)=j-1.
\]

Mit (C1zB2C6h.6) und (C1zB2C6h.9) folgt daher exakt

\[
\begin{aligned}
R_{p,T}\mathbf1_T(u)
&=
-
\sum_{k\ge j+1}
\sqrt{\log p}\,p^{-k/4}
\sqrt{p-1}
\sum_{a=0}^{j-1}p^{(a-k)/2}\psi_{p,a}\\
&=
-\sqrt{(p-1)\log p}
\left(
\sum_{k\ge j+1}^{K_p(T)}p^{-3k/4}
\right)
\sum_{a=0}^{j-1}p^{a/2}\psi_{p,a}.
\end{aligned}
\tag{C1zB2C6h.15}
\]

Hier kann

\[
K_p(T)
\le
\left\lfloor\frac{4T}{\log p}\right\rfloor
\]

genommen werden, da größere Verschiebungen auf `[-T,T]` keinen Restbeitrag mehr erzeugen. Für die folgenden oberen Schranken kann der endliche geometrische Tail nach oben durch den unendlichen ersetzt werden.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,exact\text{-}p\text{-}depth\text{-}layer\text{-}formula}.}
\]

---

# 3. Geometrische Normabnahme in der Tiefe

Aus

\[
\sum_{k\ge j+1}p^{-3k/4}
\le
\frac{p^{-3(j+1)/4}}{1-p^{-3/4}}
\le
C_0p^{-3(j+1)/4}
\]

und der Orthonormalität der `\psi_{p,a}` folgt

\[
\left\|
\sum_{a=0}^{j-1}p^{a/2}\psi_{p,a}
\right\|^2
=
\sum_{a=0}^{j-1}p^a
=
\frac{p^j-1}{p-1}.
\]

Also erhält man aus (C1zB2C6h.15)

\[
\begin{aligned}
\|R_{p,T}\mathbf1_T(u)\|
&\le
C_0\sqrt{(p-1)\log p}
 p^{-3(j+1)/4}
\sqrt{\frac{p^j-1}{p-1}}\\
&\le
C_0\sqrt{\log p}
 p^{-3(j+1)/4}p^{j/2}.
\end{aligned}
\]

Somit:

\[
\boxed{
\|R_{p,T}\mathbf1_T(u)\|
\le
C_0\sqrt{\log p}\,p^{-(j+3)/4}
\qquad(u\in I^+_{p,j,T},\ j\ge1).
}
\tag{C1zB2C6h.16}
\]

Die linke Terminalhälfte erfüllt wegen Parität dieselbe Normschranke.

Diese Abschätzung ist stärker als die globale C6f-Schranke `\|q_{p,k,T}(u)\|\le1`: Sie benutzt die **tatsächliche lokale p-Tiefe**.

---

# 4. Rücktransport durch `R_{p,T}^*`

Definiere für jedes `k\ge1`

\[
\boxed{
F_{p,k,T}(u)
:=
\left\langle
q_{p,k,T}(u),
R_{p,T}\mathbf1_T(u)
\right\rangle_{K_p^0}.
}
\tag{C1zB2C6h.17}
\]

Dann ist

\[
\boxed{
R_{p,T}^*R_{p,T}\mathbf1_T
=
\sum_{k\ge1}
 b_{p,k}K_{k\log p}^*F_{p,k,T}.
}
\tag{C1zB2C6h.18}
\]

Da `K_s^*=-K_s`, ändert das Vorzeichen für absolute Sprungabschätzungen nichts.

Auf `I^+_{p,j,T}` ist `F_{p,k,T}` konstant. Mit

\[
\|q_{p,k,T}(u)\|\le1
\]

und (C1zB2C6h.16) gilt

\[
\boxed{
|F_{p,k,T}(u)|
\le
C_0\sqrt{\log p}\,p^{-(j+3)/4}.
}
\tag{C1zB2C6h.19}
\]

Die Sprungstelle zwischen den Tiefen `j-1` und `j` liegt bei

\[
T-\frac j2\log p.
\]

Für `j\ge2` ist der größere der beiden benachbarten Bounds derjenige der flacheren Lage `j-1`; für `j=1` ist die äußere Lage exakt null. Einheitlich dürfen wir daher gröber schreiben

\[
\boxed{
\left|
\operatorname{Jump}_{T-j\log p/2}F_{p,k,T}
\right|
\le
C_1\sqrt{\log p}\,p^{-(j+2)/4}
\qquad(j\ge1).
}
\tag{C1zB2C6h.20}
\]

Für `j=1` ist der tatsächliche Bound sogar `O(\sqrt{\log p}\,p^{-1})`; die gröbere einheitliche Form genügt.

---

# 5. Prime-pure Sprungkoeffizient nach äußerer Verschiebung

Wendet man `K_{k\log p}^*` auf eine Stufenfunktion mit Sprung bei

\[
\pm\left(T-\frac j2\log p\right)
\]

an, entstehen verschobene Sprungkanten ausschließlich auf dem einzelnen p-Gitter.

Die für die Nähe zu `x_q(T)=T-O(1)` relevante **gegenüberliegende** Kante ist

\[
\boxed{
y_{p,m}(T)
=-T+\frac m2\log p,}
\tag{C1zB2C6h.21}
\]

wobei

\[
\boxed{m=j+k\ge2.}
\tag{C1zB2C6h.22}
\]

Für ein festes Paar `(j,k)` liefert (C1zB2C6h.20) zusammen mit

\[
b_{p,k}=\sqrt{\log p}\,p^{-k/4}
\]

die Sprungabschätzung

\[
C_1\log p\,p^{-(j+k+2)/4}
=
C_1\log p\,p^{-(m+2)/4}.
\tag{C1zB2C6h.23}
\]

Zu festem `m` gibt es höchstens `m-1` Paare positiver ganzer Zahlen `(j,k)` mit `j+k=m`. Eventuelle Koinzidenzen der daraus entstehenden Sprünge werden absolut majorisiert.

Daher:

## Lemma C1zB2C6h.1 — prime-pure Gegenkanten-Gewicht

Für jedes `p,m,T` gilt

\[
\boxed{
\left|
\operatorname{Jump}_{y_{p,m}(T)}
\bigl(R_{p,T}^*R_{p,T}\mathbf1_T\bigr)
\right|
\le
C_2m\log p\,p^{-(m+2)/4}.
}
\tag{C1zB2C6h.24}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm pos,prime\text{-}pure\text{-}jump\text{-}weight}.}
\]

### Primitive-Kollaps-Reconciliation

Der Befund

\[
R_T^{(1)}\mathbf1_T=0
\]

ist in (C1zB2C6h.15) bereits sichtbar: Auf Tiefe `j` beginnt die innere Summe bei `k=j+1`, also insbesondere nie mit einem alleinigen primitiven `k=1`-Beitrag.

Nach Anwendung von `R_T^*` kann der äußere Index zwar `k=1` sein. Deshalb beginnen die gegenüberliegenden `R_T^*R_T`-Gitter grundsätzlich schon bei `m=2`; C6h behauptet **nicht** fälschlich `m\ge3`.

Der primitive Kollaps wirkt stattdessen über die zusätzliche Tiefendämpfung in (C1zB2C6h.24).

---

# 6. Rechtsseitige prime-pure Gitter sind uniform fern von `x_3,x_5`

Neben (C1zB2C6h.21) können prime-pure Restkanten auf der rechten Seite die Form

\[
T-\frac m2\log p
\]

besitzen.

Nähe zu

\[
x_q(T)=T-\frac12\log(q/2)
\]

würde

\[
\left|
\log\frac{p^m}{q/2}
\right|<2r
\tag{C1zB2C6h.25}
\]

verlangen.

Für `q=3` ist `q/2=3/2`; jede Primzahlpotenz `p^m\ge2`, und der nächste mögliche Wert ist `2`, also besitzt man den festen logarithmischen Abstand

\[
\log(4/3).
\]

Für `q=5` ist `q/2=5/2`; die nächsten Primzahlpotenzen sind `2` und `3`, also ist der kleinste logarithmische Abstand mindestens

\[
\log(6/5).
\]

Wähle daher beispielsweise

\[
\boxed{
r_0:=\frac14\log(6/5)>0.}
\tag{C1zB2C6h.26}
\]

Dann gibt es für `0<r\le r_0` **keine rechtsseitige prime-pure Restkante** im `r`-Fenster um `x_3(T)` oder `x_5(T)`.

Diese Aussage ist vollständig elementar; keine Irrationalität von Logarithmen wird benutzt.

---

# 7. Gegenüberliegende Gitter als kurze Primzahlpotenzfenster

Für die Kante (C1zB2C6h.21) gilt

\[
|y_{p,m}(T)-x_q(T)|<r
\]

genau dann, wenn

\[
\boxed{
X_{q,T}e^{-2r}
<
p^m
<
X_{q,T}e^{2r},
\qquad
X_{q,T}:=e^{4T}\frac2q.
}
\tag{C1zB2C6h.27}
\]

Setze

\[
P_{m,T}:=X_{q,T}^{1/m}.
\]

Für `r\le r_0` liegen alle Kandidaten `p` in einem festen Multiplikativfaktor um `P_{m,T}`. Elementar gilt daher

\[
\boxed{
\sum_{\substack{p\ \mathrm{prim}\\X_{q,T}e^{-2r}<p^m<X_{q,T}e^{2r}}}
p^{-1/2}
\le
C_3
\left(
\frac r m P_{m,T}^{1/2}
+
P_{m,T}^{-1/2}
\right).
}
\tag{C1zB2C6h.28}
\]

### Beweis

Das p-Intervall besitzt Länge

\[
P_{m,T}(e^{2r/m}-e^{-2r/m})
\le
C\frac r mP_{m,T}.
\]

Die Zahl der Primzahlen darin ist höchstens die Zahl der ganzen Zahlen, also

\[
\le C\left(1+\frac r mP_{m,T}\right).
\]

Auf dem Intervall gilt `p\asymp P_{m,T}`, somit `p^{-1/2}\le CP_{m,T}^{-1/2}`. Multiplikation liefert (C1zB2C6h.28). `□`

Es wird wiederum **kein PNT** benutzt.

---

# 8. Elementare Summation der lokalen Rest-Sprungmasse

Unter der Bedingung (C1zB2C6h.27) gilt

\[
p^{-m/4}
\asymp
X_{q,T}^{-1/4}
\asymp_q e^{-T}
\]

und

\[
m\log p
=\log(p^m)
=4T+O_q(1+r).
\]

Lemma C1zB2C6h.1 liefert daher für jeden Kandidaten

\[
\boxed{
|\operatorname{Jump}|
\le
C_qT e^{-T}p^{-1/2}.
}
\tag{C1zB2C6h.29}
\]

Summiert man mit (C1zB2C6h.28) über alle möglichen `m`, erhält man

\[
\mathcal V^A_{T,q}(r)
\le
C_qT e^{-T}
\sum_{m=2}^{M_T}
\left(
\frac r mP_{m,T}^{1/2}
+
P_{m,T}^{-1/2}
\right),
\tag{C1zB2C6h.30}
\]

wobei

\[
M_T\le C T
\]

folgt aus `p\ge2` und `p^m\asymp e^{4T}`.

Da

\[
P_{m,T}^{1/2}
\asymp_q e^{2T/m},
\qquad
P_{m,T}^{-1/2}
\asymp_q e^{-2T/m},
\]

wird

\[
\boxed{
\mathcal V^A_{T,q}(r)
\le
C_qT e^{-T}
\left[
 r\sum_{m=2}^{M_T}\frac{e^{2T/m}}m
+
\sum_{m=2}^{M_T}e^{-2T/m}
\right].
}
\tag{C1zB2C6h.31}
\]

Für den ersten Summanden isolieren wir `m=2`:

\[
\sum_{m=2}^{M_T}\frac{e^{2T/m}}m
\le
\frac12e^T
+
C T e^{2T/3}.
\tag{C1zB2C6h.32}
\]

Für den zweiten genügt grob

\[
\sum_{m=2}^{M_T}e^{-2T/m}
\le
M_T
\le
CT.
\tag{C1zB2C6h.33}
\]

Setze nun

\[
r_T=c\frac{e^{-T}}T.
\]

Dann folgt aus (C1zB2C6h.31)–(C1zB2C6h.33)

\[
\begin{aligned}
\mathcal V^A_{T,q}(r_T)
&\le
C_{q,c}T e^{-T}
\left[
\frac{e^{-T}}T e^T
+
\frac{e^{-T}}T\,T e^{2T/3}
+
T
\right]\\
&\le
C_{q,c}
\left[
e^{-T}+Te^{-4T/3}+T^2e^{-T}\right].
\end{aligned}
\]

Somit:

## Satz C1zB2C6h.2 — elementares Rest-Crowding

Für jedes feste `c>0` existieren `C_c,T_c<\infty`, so dass für `q\in\{3,5\}` und

\[
r_T=c\frac{e^{-T}}T
\]

gilt

\[
\boxed{
\mathcal V^A_{T,q}(r_T)
\le
C_cT^2e^{-T}
\qquad(T\ge T_c).
}
\tag{C1zB2C6h.34}
\]

Insbesondere

\[
\boxed{
\mathcal V^A_{T,q}(r_T)\to0.
}
\tag{C1zB2C6h.35}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm pos,elementary\text{-}rest\text{-}crowding}.}
\]

### Scope-Firewall

Die Schranke ist bewusst nicht als scharfe Asymptotik behauptet. Sie genügt nur, um die lokale Restvariation am C6g-Radius gegen null zu drücken.

Es wird weder PNT noch Siebtheorie noch eine quantitative Irrationalitätsabschätzung verwendet.

---

# 9. Warum die Irrationalitätsroute nicht benötigt wird

Für verschiedene Primzahlen gilt zwar

\[
\frac{\log p}{\log q}\notin\mathbb Q,
\]

weil eine rationale Relation `a\log p=b\log q` zu `p^a=q^b` und damit zum Widerspruch mit eindeutiger Primfaktorzerlegung führen würde.

Diese qualitative Irrationalität liefert aber **keine** für C6h geeignete uniforme quantitative Diophantik.

C6h benutzt sie daher nicht.

Die gewichtete Summationsroute ist stärker für den aktuellen Zweck:

- rechtsseitige kleine prime-pure Gitter werden durch elementare Ganzzahldiskretheit ausgeschlossen;
- gegenüberliegende hohe Gitter dürfen beliebig dicht werden;
- ihre tatsächlichen Sprungkoeffizienten werden mit (C1zB2C6h.24) summiert.

Daher:

\[
\boxed{
\text{C6h benötigt keine quantitative Kontrolle von }\log p/\log q.
}
\tag{C1zB2C6h.36}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm neg,irrationality\text{-}input\text{-}unnecessary}.}
\]

Dies ist kein No-Go gegen transzendenztheoretische Methoden allgemein; sie sind für diesen lokalen Rest-Crowding-Schritt schlicht unnötig.

---

# 10. Haarwavelet-Paarung mit der Restmetrik

Setze wie in C6g

\[
\boxed{
w_{T,q,r}
=
1_{(x_q(T)-r,x_q(T))}
-
1_{(x_q(T),x_q(T)+r)}.
}
\tag{C1zB2C6h.37}
\]

Der Identitätsanteil von `A_T\mathbf1_T` ist konstant und verschwindet daher in dieser Paarung exakt.

Für eine Stufenfunktion `g` gilt allgemein

\[
\left|
\int_{x-r}^{x}g(u)du
-
\int_x^{x+r}g(u)du
\right|
\le
r\,\operatorname{Var}_{(x-r,x+r)}(g),
\tag{C1zB2C6h.38}
\]

wobei für Stufenfunktionen die Variation die Summe der absoluten Sprungbeträge ist. Eine mögliche Sprungkante genau bei `x` darf dabei mitgezählt werden.

Mit Satz C1zB2C6h.2 folgt deshalb

\[
\boxed{
|\langle w_{T,q,r_T},A_T\mathbf1_T\rangle|
\le
r_T\mathcal V^A_{T,q}(r_T)
\le
C_cT e^{-2T}.
}
\tag{C1zB2C6h.39}
\]

Für das in C6e ausgewählte `q_T`, bei dem `x_{q_T}(T)` selbst kein `A_T\mathbf1_T`-Breakpoint ist, gilt dieselbe Schranke natürlich erst recht.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,approximate\text{-}A\mathbf1\text{-}annihilation}.}
\]

---

# 11. Kombination mit C6g — lokale geometrische Trennung

Wähle in C6g `\theta=1/4` und denselben Radius

\[
r_T=c_*\frac{e^{-T}}T.
\]

Dann liefert C6g für den Hub

\[
\boxed{
|\langle w_{T,q,r_T},h_T\rangle|
\ge
\frac34j_*r_T
\asymp
\frac{e^{-T}}T.
}
\tag{C1zB2C6h.40}
\]

C6h liefert gleichzeitig

\[
\boxed{
|\langle w_{T,q,r_T},A_T\mathbf1_T\rangle|
\le
C T e^{-2T}.
}
\tag{C1zB2C6h.41}
\]

Somit ist auf demselben expliziten lokalen Testvektor das Verhältnis

\[
\boxed{
\frac{
|\langle w_{T,q,r_T},A_T\mathbf1_T\rangle|
}{
|\langle w_{T,q,r_T},h_T\rangle|
}
\le
C T^2e^{-T}
\longrightarrow0.
}
\tag{C1zB2C6h.42}
\]

Dies ist eine echte quantitative lokale Trennung der beiden Vektoren.

### Aber: noch kein `\Delta`-Skalensatz

Für

\[
r_T^{\rm Krylov}
:=
h_T-\lambda_TA_T\mathbf1_T,
\qquad
\lambda_T
=
\frac{\|H_T\mathbf1_T\|^2}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle},
\]

muss

\[
\langle w_{T,q,r_T},r_T^{\rm Krylov}\rangle
=
\langle w_{T,q,r_T},h_T\rangle
-
\lambda_T
\langle w_{T,q,r_T},A_T\mathbf1_T\rangle
\]

kontrolliert werden.

Aus C6h allein folgt **keine hinreichend scharfe obere Schranke für `\lambda_T`**, um den zweiten Term gegenüber (C1zB2C6h.40) zu vernachlässigen.

Deshalb wird ausdrücklich **nicht** behauptet, dass (C1zB2C6h.42) bereits eine asymptotische Untergrenze für `\Delta_T^{(1)}` liefert.

Genau hier bleibt der exakte korrigierte Separator notwendig.

---

# 12. Korrigierter Separator bleibt ein eigener Knoten

C6f skizzierte formal eine Korrektur

\[
\widetilde v
=
w-
\frac{\langle w,A_T\mathbf1_T\rangle}
{\langle z,A_T\mathbf1_T\rangle}z.
\]

C6h liefert jetzt erstmals einen exponentiell kleinen Zähler

\[
\boxed{
|\langle w,A_T\mathbf1_T\rangle|
\le
CTe^{-2T}.
}
\tag{C1zB2C6h.43}
\]

Es fehlt jedoch weiterhin eine kanonische Wahl von `z=z_T`, für die gleichzeitig

1. `|\langle z,A_T\mathbf1_T\rangle|` quantitativ von null getrennt ist;
2. die Korrektur die robuste Hubpaarung aus C6g nicht zerstört;
3. `\langle\widetilde v,A_T\widetilde v\rangle` kontrollierbar bleibt.

Diese drei Bedingungen sind neue Mathematik und werden nicht durch den kleinen Fehlerterm allein ersetzt.

Daher bleibt

\[
\boxed{?[O]_{\rm corrected\text{-}separator}.}
\tag{C1zB2C6h.44}
\]

---

# 13. Reconciliation mit C6e, C6f und C6g

## C6e

Der eventuale Rang-2-Satz

\[
\Delta_T^{(1)}>0
\qquad(T\gg1)
\]

bleibt unverändert positiv gesiegelt.

C6h liefert einen zweiten, quantitativen Blick auf dieselbe Trennung, ersetzt aber den exakten C6e-Separator nicht.

## C6f

C6f reduzierte den isolierten-Intervall-Beweis auf `\rho_T` und zeigte, dass bloße Supportgeometrie keine uniforme `\rho_T`-Skala liefert.

C6h umgeht `\rho_T` auf der Restseite genauso wie C6g auf der Hubseite: zusätzliche Breakpoints dürfen im Fenster liegen, solange ihre **gewichtete Gesamtvariation** klein ist.

## C6g

C6g schloss

\[
\text{Hub-Crowding}
\]

für

\[
r_T\asymp e^{-T}/T.
\]

C6h schließt nun auf demselben Radius

\[
\text{Rest-Crowding}.
\]

Damit sind beide gewichteten lokalen BV-Aufgaben aus C6f analytisch kontrolliert.

Offen bleibt nicht mehr die lokale Crowding-Masse selbst, sondern die **exakte Korrektur zur `A_T\mathbf1_T`-Orthogonalität**.

---

# 14. No-Go-Persistenzmatrix

| Früherer Knoten | Gesiegelter Befund | Wirkung in C6h |
|---|---|---|
| C1y | translationsinvariante Regulatoren lösen den Hub/Rest-Konflikt im C1y-Scope nicht | unverändert; Restkonditionierung bleibt source-windowed |
| B2-A | Gamma-Präkonditionierung liefert keinen finite Schattenmechanismus | unverändert; keine Kompaktheit/Schattenklasse |
| B2-B | naiver Haar-`L^2`-Endpunkt reicht nicht | unverändert |
| C4 | unendliche Boundary-Jet-Hierarchie | unverändert |
| C5/C6a | totale Odd-Divergenz | unverändert |
| C6 | kein voller Odd-Transport durch festen endlichen Jetquotienten | unverändert |
| C6a | Self-Grams allein reichen nicht | unverändert |
| C6b | C2-Flachheit allein reicht nicht | unverändert |
| C6c | `tau=>kappa` auf festem Fenster | unverändert |
| C6c | Triangularität allein reicht nicht | unverändert |
| C6d | C4-Jets sind keine automatischen Multi-Probes | unverändert |
| C6e | eventualer Krylov-Rang 2 | bleibt positiv gesiegelt |
| C6f | Breakpoint-Support allein reicht nicht für uniforme Skala | unverändert; C6h benutzt Gewichte statt Mindestabstände |
| C6g | elementares Hub-Crowding auf `e^{-T}/T`-Fenster | direkt ergänzt durch Rest-Crowding |
| C6g | globale Restnorm impliziert keine lokale BV-Kontrolle | bestätigt: C6h benötigt die konkrete Martingalstruktur |

---

# 15. Was C6h ausdrücklich nicht beweist

Nicht bewiesen sind:

- eine scharfe Asymptotik von `\mathcal V^A_{T,q}(r_T)`;
- eine optimale Wahl des Radius `r_T`;
- ein PNT-verbesserter Radius;
- ein exakt `A_T\mathbf1_T`-orthogonaler korrigierter lokaler Separator;
- eine asymptotische Klassifikation von `\Delta_T^{(1)}`;
- `\inf_T\Delta_T^{(1)}>0`;
- `\Delta_T^{(1)}\to0`;
- `\Delta_T^{(1)}\to\infty`;
- eine uniforme Stabilität von `\widehat\psi_{T,1}`;
- Jet-Alignment der zweiten Probe;
- eine Untergrenze für `s_{\min}(\mathcal P_T^{(1)})`;
- `\tau_T(E_{R,1})\to0`;
- `\Theta_{T,U}^{E_{R,1}}\to I`;
- Krylov-Rang `N\ge2`.

Insbesondere bleibt die in C6f formulierte Degenerationsmöglichkeit

\[
\boxed{
\Delta_T^{(1)}\to0
}
\]

weiterhin logisch offen.

---

# 16. Exakter nächster Arbeitsauftrag C6i

Nach C6g und C6h sind beide lokalen Crowding-Seiten kontrolliert:

\[
|\langle w_T,h_T\rangle|
\gtrsim
\frac{e^{-T}}T,
\]

während

\[
|\langle w_T,A_T\mathbf1_T\rangle|
\lesssim
Te^{-2T}.
\]

Der nächste Knoten sollte deshalb **nicht** erneut die Breakpoint-Masse schätzen.

Er lautet:

\[
\boxed{
\text{C6i: exakter korrigierter Separator aus der kleinen Restpaarung.}
}
\tag{C1zB2C6h.45}
\]

Arbeitsauftrag:

1. Konstruiere einen kanonischen Korrekturvektor `z_T` mit
   \[
   |\langle z_T,A_T\mathbf1_T\rangle|
   \]
   quantitativ kontrolliert von null weg.
2. Setze
   \[
   \widetilde v_T
   =w_T-
   \frac{\langle w_T,A_T\mathbf1_T\rangle}
   {\langle z_T,A_T\mathbf1_T\rangle}z_T.
   \]
3. Beweise exakt
   \[
   \langle\widetilde v_T,A_T\mathbf1_T\rangle=0.
   \]
4. Zeige, dass die Korrektur die C6g-Hubpaarung nur um `o(e^{-T}/T)` verändert.
5. Kontrolliere
   \[
   \langle\widetilde v_T,A_T\widetilde v_T\rangle
   \]
   und leite daraus erstmals eine echte quantitative Untergrenze für `\Delta_T^{(1)}` ab.

### Firewall für C6i

Die Kleinheit

\[
\langle w_T,A_T\mathbf1_T\rangle=o(\langle w_T,h_T\rangle)
\]

allein reicht **nicht**, weil in

\[
h_T-\lambda_TA_T\mathbf1_T
\]

der Faktor `\lambda_T` noch nicht scharf genug kontrolliert ist.

C6i muss daher entweder wirklich exakt korrigieren oder eine neue ausreichend starke Schranke für `\lambda_T` beweisen.

---

# 17. Endurteil

C6h schließt die gewichtete Rest-Crowding-Frage positiv und elementar.

Die entscheidende neue Struktur ist die exakte p-Tiefenformel

\[
R_{p,T}\mathbf1_T(u)
=
-\sqrt{(p-1)\log p}
\left(\sum_{k\ge j+1}p^{-3k/4}\right)
\sum_{a=0}^{j-1}p^{a/2}\psi_{p,a},
\]

die den geometrischen Bound

\[
\|R_{p,T}\mathbf1_T(u)\|
\lesssim
\sqrt{\log p}\,p^{-(j+3)/4}
\]

erzwingt.

Nach Rücktransport durch `R_{p,T}^*` folgt die prime-pure Sprungschranke

\[
\left|
\operatorname{Jump}_{-T+m\log p/2}
(R_{p,T}^*R_{p,T}\mathbf1_T)
\right|
\lesssim
m\log p\,p^{-(m+2)/4}.
\]

Damit gilt auf genau dem C6g-Fenster

\[
\boxed{
\mathcal V^A_{T,q}(c e^{-T}/T)
\lesssim
T^2e^{-T}	o0.
}
\]

Die lokale Restpaarung des C6g-Testvektors ist folglich exponentiell kleiner als seine robuste Hubpaarung:

\[
\boxed{
\frac{|\langle w_T,A_T\mathbf1_T\rangle|}
{|\langle w_T,h_T\rangle|}
\lesssim
T^2e^{-T}	o0.
}
\]

Das ist ein echter Fortschritt gegenüber C6f/C6g. Der quantitative Zweitprobe-Engpass ist jetzt nicht mehr Hub-Crowding und nicht mehr Rest-Crowding, sondern die **exakte Orthogonalisierung des lokalen Separators** ohne Verlust der Hubkopplung.
