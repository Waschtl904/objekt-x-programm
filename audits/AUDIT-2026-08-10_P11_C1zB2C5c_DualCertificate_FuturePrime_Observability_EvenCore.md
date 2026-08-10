# P11-C1z-B2-C5c — Dualzertifikat für Future-Prime-Observability auf dem geraden Testcore

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C5c]`  
**Vorgänger:** C1z-B2-C5b  
**Schnittstellen:** C1z-B/B1; C1z-B2-C3/C4/C5/C5a/C5b; P03-Haar-L2-Firewall  

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C5c]
\quad
\checkmark[K/M]_{\rm part}
\;+
\checkmark[M]_{\rm pos,even\text{-}core\text{-}observability}
\;+
\checkmark[M]_{\rm neg,prime\text{-}micro\text{-}witness\text{-}on\text{-}core}
}
\]

mit dem neuen Hauptsatz:

> Für jedes feste gerade
> \[
> f\in C_c^\infty((-R,R))
> \]
> existiert eine Konstante `C_{R,f}<\infty`, unabhängig vom Terminalhorizont `T`, so dass für alle genügend großen `T` und alle ungeraden
> \[
> e\in\mathscr H_T^-
> \]
> gilt
> \[
> \boxed{
> |\mathcal L_{T,f}^{\rm prim}(e)|^2
> \le
> C_{R,f}
> \bigl(\|e\|_2^2+\|R_T^{(1)}e\|^2\bigr).
> }
> \tag{C1zB2C5c.1}
> \]

Damit ist die in C5a/C5b isolierte source-windowed Lower-Prime-Frame-/Observability-Ungleichung **auf dem glatten geraden Testcore positiv entschieden**.

Insbesondere kann keine `T`-abhängige Prime-Mikrostruktur-Quasi-Nullfolge die primitive Hubfunktionalform eines festen glatten geraden Tests aufblasen.

Der Beweis benötigt **keine** uniforme Lower-Frame-Ungleichung für alle Source-Vektoren. Stattdessen wird die Feshbach-Variationsform dualisiert und ein explizites Rest-Dualzertifikat gebaut.

Die einzige externe analytisch-zahlentheoretische Eingabe ist eine unbedingte PNT-in-short-intervals-Massenschranke auf komfortabler Skala `x^{3/5}`. Guth–Maynard beweisen asymptotische Primzahlverteilung in Intervallen der Länge `x^{17/30+o(1)}`; insbesondere ist `3/5>17/30` zulässig. Siehe Larry Guth, James Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics 203 (2026), DOI `10.4007/annals.2026.203.2.6`, sowie die explizite All-`x`-Formulierung in A. Gafni / T. Tao, arXiv:2505.24017, Theorem 1.1 und Einleitung.

**Firewall:** C5c beweist noch nicht

1. eine uniforme Operatornormschranke von `G_{R,T}^+` auf der gesamten vervollständigten Graphhälfte `\mathcal K_{X,R}^+`;
2. Konvergenz von `G_{R,T}^+`;
3. den Cauchy-Limes von `W_{R,S,+}^{[T]}`;
4. irgendeine Aussage über den ungeraden Boundary-Jet-Transport;
5. Objekt X oder RH.

Der positive Satz ist exakt auf dem dichten glatten geraden Testcore gebucht.

---

# 0. Warum C5b nicht mit einer Lower-Frame-Ungleichung beendet werden muss

C5b formulierte den binären Endtest:

\[
\text{Future-Layer-Observability}
\quad\text{oder}\quad
\text{Prime-Mikrostruktur-Quasi-Nullfolge}.
\]

Die direkte Form war

\[
\mathcal L_{T,f}^{\rm prim}(e)
=
\langle J_{R,T}f,H_T^{(1)}e\rangle,
\]

und gesucht wurde eine uniforme Schranke gegen

\[
\|e\|^2+\|R_T^{(1)}e\|^2.
\]

C5c benutzt nun die **duale Feshbach-Seite**.

Für einen beschränkten Operator

\[
R:H\to Y
\]

und `h in H` gilt

\[
\boxed{
\langle h,(I+R^*R)^{-1}h\rangle
=
\inf_{y\in Y}
\left(
\|h-R^*y\|^2+\|y\|^2
\right).
}
\tag{C1zB2C5c.2}
\]

Damit genügt es, für

\[
h_{T,f}^{(1)}:=(H_T^{(1)})^*J_{R,T}f
\]

einen Vektor `y_T` im primitiven Restzielraum und einen Source-Rest `z_T` zu konstruieren mit

\[
\boxed{
h_{T,f}^{(1)}=(R_T^{(1)})^*y_T+z_T}
\tag{C1zB2C5c.3}
\]

und

\[
\boxed{
\sup_T
\bigl(\|y_T\|^2+\|z_T\|^2\bigr)<\infty.
}
\tag{C1zB2C5c.4}
\]

Dann folgt für alle `e` sofort

\[
|\langle h_{T,f}^{(1)},e\rangle|
\le
\bigl(\|y_T\|^2+\|z_T\|^2\bigr)^{1/2}
\bigl(\|R_T^{(1)}e\|^2+\|e\|^2\bigr)^{1/2}.
\]

Das ist genau (C1zB2C5c.1).

**Konzeptioneller Wechsel:**

C5b fragte, ob jede mögliche Mikrostruktur durch die Primfamilie beobachtet wird.

C5c muss das nicht beweisen. Es zeigt stattdessen, dass **das eine konkrete glatte Hubfunktional, das wir brauchen**, bereits im Graphdual des Restoperators liegt — mit `T`-uniformer Norm.

---

# 1. Variations-/Minimierungslemma

## Lemma C5c.1

Sei `R:H->Y` beschränkt. Dann gilt (C1zB2C5c.2).

### Beweis

Setze

\[
F(y)=\|h-R^*y\|^2+\|y\|^2.
\]

Die Euler-Gleichung lautet

\[
(I+RR^*)y=Rh.
\]

Der Minimierer ist daher

\[
y_0=(I+RR^*)^{-1}Rh.
\]

Mit der Standardidentität

\[
I-R^*(I+RR^*)^{-1}R
=(I+R^*R)^{-1}
\]

folgt

\[
\inf_yF(y)
=
\langle h,(I+R^*R)^{-1}h\rangle.
\]

`□`

Dieses Lemma wird mit

\[
R=R_T^{(1)}
\]

angewandt.

---

# 2. Fixierter glatter gerader Test und endlicher Small-Prime-Block

Fixiere

\[
0\ne f\in C_c^\infty((-R,R)),
\qquad f(-u)=f(u).
\]

Wähle eine Zahl

\[
\rho_f<R
\]

mit

\[
\operatorname{supp}f\subset(-\rho_f,\rho_f).
\]

Fixiere ferner

\[
0<\varepsilon<\min\{1,\tfrac12\log2\}
\]

und eine nichtnegative Anchor-Dichte

\[
\alpha\in C_c^\infty((0,\varepsilon)),
\qquad
\int_0^\varepsilon\alpha(s)\,ds=1.
\]

Wähle

\[
a_*>\rho_f+2\varepsilon.
\]

Die primitiven Primzahlen werden zerlegt in

\[
\mathcal P_{\rm small}
:=\{p:\tfrac12\log p<a_*\}
\]

und den wachsenden Block

\[
\mathcal P_{\rm grow}(T)
:=\{p:a_*\le\tfrac12\log p\le T\}.
\]

`P_small` ist endlich und unabhängig von `T`.

Für `T` groß genug enthält der primitive Rest-Overlap jedes `p in P_small` den vollständigen Träger von `f`. Daher kann der zugehörige Hubterm **direkt im gleichen Primkanal** faktorisiert werden.

Mit

\[
c_p:=\sqrt{\log p}\,p^{-3/4},
\qquad
w_p:=\frac{\log p}{\sqrt p}\left(1-\frac1p\right)
\]

ist

\[
\frac{c_p^2}{w_p}
=\frac1{p(1-1/p)}.
\]

Definiere im `p`-Restzielkanal

\[
y_{p,\rm small}:=\frac{c_p}{\sqrt{w_p}}f.
\]

Dann

\[
(R_{T,p}^{(1)})^*y_{p,\rm small}
=
c_pD_{\log p}^*f
\]

und

\[
\boxed{
\sum_{p\in\mathcal P_{\rm small}}
\|y_{p,\rm small}\|^2
=
\|f\|_2^2
\sum_{p\in\mathcal P_{\rm small}}
\frac1{p(1-1/p)}
<\infty.
}
\tag{C1zB2C5c.5}
\]

Der einzige schwierige Teil ist daher der wachsende Primblock.

---

# 3. Boundary-Koordinate für den geraden Source-Test

Sei

\[
e\in\mathscr H_T^-
\]

ungerade.

Auf der positiven Source-Hälfte definiere

\[
\boxed{
b_T(t):=e(T-t),\qquad 0<t<T.}
\tag{C1zB2C5c.6}
\]

Für eine primitive Primzahl `p` setze

\[
a_p:=\tfrac12\log p,
\qquad
d_p:=T-a_p.
\]

Für `a_p>=rho_f` gilt durch Oddness von `e` und Evenness von `f` exakt

\[
\boxed{
\langle f,D_{\log p}E_Te\rangle
=
2\int_0^T f(t-d_p)b_T(t)\,dt.
}
\tag{C1zB2C5c.7}
\]

Der Beweis ist nur die Aufspaltung der beiden Fälle `u<=d_p` und `u>d_p`:

\[
D_{\log p}E_Te(u)
=
1_{\{u\le d_p\}}b_T(d_p-u)+b_T(d_p+u)
\]

für `0<u<rho_f`.

Nach den Variablentransformationen `t=d_p-u` und `t=d_p+u` vereinigen sich beide Beiträge wegen `f(-u)=f(u)` zu (C1zB2C5c.7).

Damit ist das gesamte wachsende primitive Hubfunktional

\[
\boxed{
\mathcal L_{T,f}^{\rm grow}(e)
=
\int_0^T k_T(t)b_T(t)\,dt
}
\tag{C1zB2C5c.8}
\]

mit dem **glatten Boundary-Hubkern**

\[
\boxed{
k_T(t)
:=
2\sum_{p\in\mathcal P_{\rm grow}(T)}
 c_p f(t-d_p).
}
\tag{C1zB2C5c.9}
\]

Wegen `a_*>rho_f+2epsilon` gilt

\[
\operatorname{supp}k_T
\subset
[0,T-2\varepsilon].
\tag{C1zB2C5c.10}
\]

für die gewählte technische Reserve nach Vergrößerung von `a_*` um eine feste Konstante, falls nötig.

Das ist wichtig: Für jedes `t in supp k_T` und jedes `s in supp alpha` gilt

\[
t+s<T.
\]

Damit liegt der Mittelpunkt

\[
r=\frac{t+s}{2}
\]

im **Future-Prime-Bereich**

\[
0<r<T/2.
\]

---

# 4. Primitive Future-Restkanäle als signless reflection edges

Betrachte nun eine primitive Primzahl `q` mit

\[
a_q:=\tfrac12\log q\ge T/2.
\]

Setze ihre Boundary-Distanz

\[
\boxed{r_q:=T-a_q\in[0,T/2].}
\tag{C1zB2C5c.11}
\]

Auf dem primitiven Rest-Overlap `|u|<=r_q` liegen beide positiven Endpunkte innerhalb `(0,T)`.

Mit

\[
t=r_q-u
\]

folgt exakt

\[
D_{\log q}E_Te(u)
=
b_T(t)+b_T(2r_q-t).
\]

Daher enthält die primitive Restenergie den positiven Future-Teil

\[
\boxed{
\mathcal E_{T,\rm fut}^{(1)}[b_T]
:=
\sum_{q:\,a_q\ge T/2}
 w_q
\int_0^{2r_q}
|b_T(t)+b_T(2r_q-t)|^2\,dt
\le
\|R_T^{(1)}e\|^2.
}
\tag{C1zB2C5c.12}
\]

Jeder Future-Prime liefert somit eine **signless reflection edge**

\[
\boxed{
\mathsf E_r b(t):=b(t)+b(2r-t).
}
\tag{C1zB2C5c.13}
\]

Dies ist die diskrete Source-Geometrie, die C5b nur auf Skalierungsebene als Transfer `d->d/2` identifiziert hatte.

---

# 5. Exakte kontinuierliche Dreiecksidentität

Der neue algebraische Kern ist unabhängig von Primzahlen.

Da

\[
\int\alpha=1,
\]

gilt für jedes `b` und jedes `t` exakt

\[
\boxed{
\begin{aligned}
b(t)
={}&
\int_0^\varepsilon
\alpha(s)\,[b(t)+b(s)]\,ds
\\
&-
\frac12
\int_0^\varepsilon\int_0^\varepsilon
\alpha(s)\alpha(s')\,[b(s)+b(s')]\,ds\,ds'.
\end{aligned}
}
\tag{C1zB2C5c.14}
\]

Denn die erste Zeile ist

\[
b(t)+m_\alpha(b),
\qquad
m_\alpha(b):=\int\alpha(s)b(s)ds,
\]

und die zweite Doppelintegration ist exakt `m_alpha(b)`.

Dies ist eine **signless triangle identity**:

- zwei Kanten verbinden den Targetwert `b(t)` mit dem Anchor;
- der reine Anchor-Kantenterm entfernt den eingeführten Anchor-Mittelwert exakt.

Multipliziere (C1zB2C5c.14) mit `k_T(t)` und integriere in `t`.

Setze

\[
K_T:=\int_0^T k_T(t)\,dt.
\]

Dann

\[
\boxed{
\begin{aligned}
\int k_T(t)b(t)dt
={}&
\iint k_T(t)\alpha(s)[b(t)+b(s)]\,dt\,ds
\\
&-
\frac{K_T}{2}
\iint\alpha(s)\alpha(s')[b(s)+b(s')]\,ds\,ds'.
\end{aligned}
}
\tag{C1zB2C5c.15}
\]

Jedes Paar `(t,s)` in der ersten Zeile besitzt Mittelpunkt

\[
r=\frac{t+s}{2}<T/2,
\]

also exakt die Geometrie eines Future-Restkanals.

Dasselbe gilt für die Anchor-Anchor-Paare.

Damit ist das Hubfunktional bereits **kontinuierlich exakt** als Kombination von Future-Restkanten dargestellt.

---

# 6. Kontinuierliches Future-Restmaß und Zertifikatsnorm

Die PNT-Skalierung aus C5b legt auf der Boundary-Distanz `r` das positive Gewicht

\[
\boxed{m_T(r):=2e^{T-r}}
\tag{C1zB2C5c.16}
\]

nahe.

Unter

\[
s=2r-t,
\qquad ds=2dr,
\]

kann (C1zB2C5c.15) als

\[
\int_0^{T/2}\int_0^{2r}
C_T(r,t)\,[b(t)+b(2r-t)]\,dt\,dr
\]

geschrieben werden, wobei

\[
\boxed{
C_T(r,t)
=
\alpha(2r-t)
\bigl(2k_T(t)-K_T\alpha(t)\bigr).
}
\tag{C1zB2C5c.17}
\]

Alle Funktionen werden außerhalb ihrer natürlichen Träger als null verstanden.

Definiere das kontinuierliche Analysefeld

\[
(A_T^{\rm cont}b)(r,t)
:=
\sqrt{m_T(r)}\,[b(t)+b(2r-t)].
\]

Das zu (C1zB2C5c.17) gehörige Dualzertifikat ist

\[
\boxed{
Y_T^{\rm cont}(r,t)
:=
\frac{C_T(r,t)}{\sqrt{m_T(r)}}.
}
\tag{C1zB2C5c.18}
\]

Dann gilt exakt

\[
\boxed{
(A_T^{\rm cont})^*Y_T^{\rm cont}=k_T.
}
\tag{C1zB2C5c.19}
\]

in der Boundary-Source-Darstellung.

Seine Norm erfüllt

\[
\|Y_T^{\rm cont}\|^2
=
\int\frac{|C_T(r,t)|^2}{m_T(r)}\,dt\,dr.
\]

Mit `r=(t+s)/2` und der kompakten Anchor-Dichte folgt

\[
\boxed{
\|Y_T^{\rm cont}\|^2
\le
C_\alpha e^{-T}
\left(
\int_0^T e^{t/2}|k_T(t)|^2dt
+|K_T|^2
\right).
}
\tag{C1zB2C5c.20}
\]

Damit ist die Future-Screening-Skala auf der Dualseite explizit.

---

# 7. Wachstumsabschätzungen des glatten Hubkerns

Für

\[
A:=T-t
\]

liegen in (C1zB2C5c.9) nur Primzahlen mit

\[
\tfrac12\log p=A+O_{\rho_f}(1)
\]

vor.

PNT + partielle Summation auf festen multiplikativen Primintervallen liefern

\[
\boxed{
|k_T(t)|+|k_T'(t)|
\le
C_f
\frac{e^{A/2}}{\sqrt{1+A}}
}
\tag{C1zB2C5c.21}
\]

für `A` außerhalb eines festen kompakten Anfangsbereichs; dort wird die rechte Seite nach Vergrößerung von `C_f` ebenfalls gültig.

Ferner

\[
\boxed{
|K_T|
\le
C_f\frac{e^{T/2}}{\sqrt{1+T}}.
}
\tag{C1zB2C5c.22}
\]

Daraus folgt

\[
\begin{aligned}
e^{-T}
\int_0^T e^{t/2}|k_T(t)|^2dt
&\le
C_f e^{-T}
\int_0^T
\frac{e^{T-t}e^{t/2}}{1+T-t}\,dt
\\
&=
C_f
\int_0^T
\frac{e^{-t/2}}{1+T-t}\,dt
\\
&=O_f(T^{-1})+O_f(e^{-T/4}).
\end{aligned}
\]

Ebenso

\[
e^{-T}|K_T|^2=O_f(T^{-1}).
\]

Somit

\[
\boxed{
\|Y_T^{\rm cont}\|^2
\le
\frac{C_f}{T}
+O_f(e^{-T/4}).
}
\tag{C1zB2C5c.23}
\]

Dies ist genau der in C5b vorhergesagte Future-Screening-Gewinn — jetzt als explizite Dualzertifikatsnorm.

---

# 8. Externe unbedingte Primzahleingabe: Short-interval PNT auf `x^{3/5}`

Wir brauchen nun nur noch genügend **Prime-Masse** in sehr kleinen Future-Zellen.

Die moderne unbedingte PNT-in-short-intervals-Aussage lautet: Für jedes feste

\[
\theta>17/30
\]

gilt für alle hinreichend großen `x`

\[
\sum_{x<n\le x+x^\theta}\Lambda(n)
\sim x^\theta.
\]

Wir wählen komfortabel

\[
\boxed{\theta=3/5.}
\tag{C1zB2C5c.24}
\]

Diese Wahl liegt strikt oberhalb `17/30`.

Für eine Future-Prime-Skala

\[
q\asymp X=e^{2a},
\qquad a=T-r\ge T/2,
\]

entspricht ein Intervall der Länge

\[
X^{3/5}
\]

einer `r`-Zelle der Breite

\[
\boxed{
|I|\asymp X^{-2/5}
=e^{-\frac45 a}.
}
\tag{C1zB2C5c.25}
\]

In einer solchen Zelle ist die gesamte primitive Restmasse

\[
W_I
:=
\sum_{q:\,r_q\in I}w_q.
\]

Da

\[
w_q
=\frac{\log q}{\sqrt q}(1+o(1)),
\]

liefert die Short-interval PNT

\[
\boxed{
W_I
\asymp
X^{1/10}
\asymp
2e^{T-r_I}|I|
=m_T(r_I)|I|,
}
\tag{C1zB2C5c.26}
\]

uniform für die verwendeten Future-Zellen und große `T`.

Wichtig: C5c benötigt **keinen Fehlerterm mit exponentieller relativer Genauigkeit**. Es wird nur die untere/obere Vergleichbarkeit (C1zB2C5c.26) verwendet.

---

# 9. Zellnormalisierte Prime-Quadratur

Dies ist der Schritt, der die diskrete Prime-Mikrostruktur vollständig neutralisiert.

Sei `I` eine Future-Zelle und

\[
W_I=\sum_{q:r_q\in I}w_q.
\]

Definiere für jede Primzahl in der Zelle

\[
\boxed{
\lambda_q^{(I)}
:=
|I|\frac{w_q}{W_I}.
}
\tag{C1zB2C5c.27}
\]

Dann gilt **exakt**

\[
\boxed{
\sum_{q:r_q\in I}\lambda_q^{(I)}=|I|.
}
\tag{C1zB2C5c.28}
\]

Die Primzahlen werden also nicht als punktweise Approximation eines Kontinuums benutzt. Stattdessen wird jede Zelle mit ihrer **tatsächlich vorhandenen kanonischen Restmasse** normalisiert.

Für eine Hilbertraum-wertige Lipschitzfunktion `Phi(r)` gilt daher

\[
\boxed{
\left\|
\sum_{q:r_q\in I}
\lambda_q^{(I)}\Phi(r_q)
-
\int_I\Phi(r)dr
\right\|
\le
2|I|^2
\sup_{r\in I}\|\Phi'(r)\|.
}
\tag{C1zB2C5c.29}
\]

Der Beweis ist elementar: Sowohl die diskrete Summe als auch das Integral sind Mittelwerte mit derselben Gesamtmasse `|I|`; beide liegen innerhalb der Oszillation von `Phi` auf `I`.

Außerdem gilt die exakte Zertifikatskostenidentität

\[
\boxed{
\sum_{q:r_q\in I}
\frac{|\lambda_q^{(I)}|^2}{w_q}
=
\frac{|I|^2}{W_I}
\lesssim
\frac{|I|}{m_T(r_I)}.
}
\tag{C1zB2C5c.30}
\]

nach (C1zB2C5c.26).

Dies ist die entscheidende Diskretisierungsformel.

Sie zeigt zugleich, warum eine hochoszillatorische Source-Mikrostruktur `e_T` irrelevant wird: Die Quadratur wird **auf dem glatten Dualzertifikat** ausgeführt, nicht auf `e_T`.

---

# 10. Diskretes Future-Prime-Dualzertifikat

Für jede Future-Zelle `I` und jede darin liegende Primzahl `q` definiere im `q`-Restkanal

\[
\boxed{
Y_{T,q}(t)
:=
\frac{\lambda_q^{(I)}}{\sqrt{w_q}}
C_T(r_q,t).
}
\tag{C1zB2C5c.31}
\]

über die Boundary-Koordinatenidentifikation des primitiven `q`-Kanals.

Alle `q`-Kanäle liegen in orthogonalen `K_q^0`-Sektoren. Daher

\[
\|Y_T\|^2
=
\sum_q\|Y_{T,q}\|_2^2.
\]

Mit (C1zB2C5c.30) und der Glattheit von `C_T` folgt zellenweise

\[
\|Y_T\|^2
\le
C
\int_0^{T/2}\int
\frac{|C_T(r,t)|^2}{m_T(r)}\,dt\,dr
+o(1).
\]

Also aus (C1zB2C5c.23):

\[
\boxed{
\|Y_T\|^2
\le
\frac{C_f}{T}
+O_f(e^{-cT})
}
\tag{C1zB2C5c.32}
\]

für den wachsenden Primblock und ein absolutes `c>0`.

Der kleine endliche Primblock aus §2 wird orthogonal hinzugefügt und kostet nur die feste Konstante (C1zB2C5c.5).

---

# 11. Diskretisierungsfehler ist exponentiell klein

Es bleibt zu zeigen, dass die diskrete Prime-Quadratur nicht nur die Zertifikatsnorm kontrolliert, sondern auch den kontinuierlich exakt erzeugten Hubkern in Source-Norm approximiert.

Sei

\[
\Phi_T(r)
\]

der Source-Vektor, dessen Pairing mit `b` gleich

\[
\int C_T(r,t)[b(t)+b(2r-t)]dt
\]

ist.

Dann

\[
k_T
=
\int_0^{T/2}\Phi_T(r)dr
\]

nach (C1zB2C5c.15)--(C1zB2C5c.19), während

\[
(R_T^{(1)})^*Y_T
=
\sum_I\sum_{q:r_q\in I}
\lambda_q^{(I)}\Phi_T(r_q).
\]

Nach (C1zB2C5c.29):

\[
\boxed{
\left\|
 k_T-(R_T^{(1)})^*Y_T
\right\|_2
\le
2\sum_I
|I|^2
\sup_{r\in I}\|\Phi_T'(r)\|_2.
}
\tag{C1zB2C5c.33}
\]

Die Ableitung `Phi_T'` enthält ausschließlich `k_T`, `k_T'`, `K_T` sowie feste Ableitungen der Anchor-Dichte `alpha`.

Auf dem Support der Target-Anchor-Kante gilt

\[
t=2r-s,
\qquad s\in\operatorname{supp}\alpha,
\]

also

\[
A:=T-t
=T-2r+O_\alpha(1).
\]

Die Future-Prime-Skala der betreffenden Zelle ist

\[
a_q=T-r
=\frac{T+A}{2}+O_\alpha(1).
\]

Nach (C1zB2C5c.25) besitzt die Zellweite daher

\[
|I|
\ll
\exp\!\left(-\frac45a_q\right)
\ll
\exp\!\left(-\frac25(T+A)\right).
\]

Andererseits wächst nach (C1zB2C5c.21)

\[
|k_T|+|k_T'|
\ll_f
\exp(A/2)(1+A)^{-1/2}.
\]

Das Produkt besitzt somit die exponentielle Skala

\[
\exp\!\left(-\frac25T+\frac1{10}A\right)
\le
\exp(-3T/10)
\]

weil `0<=A<=T+O(1)`.

Der Anchor-Anchor-Term ist noch günstiger: Dort `r=O(1)`, also

\[
|I|\ll e^{-4T/5},
\]

während

\[
|K_T|\ll_f e^{T/2}/\sqrt T.
\]

Daher gibt es `c>0` mit

\[
\boxed{
\left\|
 k_T-(R_T^{(1)})^*Y_T
\right\|_2
\le
C_f e^{-cT}.
}
\tag{C1zB2C5c.34}
\]

Für die konkrete Wahl `theta=3/5` kann im groben Exponentenvergleich jedes feste

\[
0<c<3/10
\]

nach Vergrößerung des Startwerts verwendet werden; die genaue Optimierung ist irrelevant.

Dies ist der Punkt, an dem die `T`-abhängige Prime-Mikrostruktur endgültig aus dem Beweis verschwindet.

---

# 12. Hauptsatz C5c.1 — uniforme primitive Observability auf dem glatten geraden Core

Füge zusammen:

1. das endliche Same-Prime-Zertifikat aus §2;
2. das diskrete Future-Prime-Zertifikat aus §10;
3. den exponentiell kleinen Source-Rest aus §11.

Es existieren also

\[
y_T\in\mathscr Y_{T,\rm prim}^0,
\qquad
z_T\in\mathscr H_T^-
\]

mit

\[
\boxed{
 h_{T,f}^{(1)}
=(R_T^{(1)})^*y_T+z_T
}
\tag{C1zB2C5c.35}
\]

und

\[
\boxed{
\sup_{T>R}
\bigl(\|y_T\|^2+\|z_T\|^2\bigr)
\le
C_{R,f}<\infty.
}
\tag{C1zB2C5c.36}
\]

Genauer trägt der wachsende Primblock nur

\[
O_f(T^{-1})+O_f(e^{-cT})
\]

zur Zertifikatsnorm bei; der `T`-unabhängige konstante Anteil stammt lediglich aus dem absichtlich separat behandelten endlichen Small-Prime-Block.

Damit folgt für jedes ungerade `e`:

\[
\begin{aligned}
|\mathcal L_{T,f}^{\rm prim}(e)|
&=|\langle h_{T,f}^{(1)},e\rangle|\\
&\le
\|y_T\|\,\|R_T^{(1)}e\|
+\|z_T\|\,\|e\|.
\end{aligned}
\]

Cauchy--Schwarz in der direkten Summe liefert

\[
\boxed{
|\mathcal L_{T,f}^{\rm prim}(e)|^2
\le
C_{R,f}
\bigl(\|e\|^2+\|R_T^{(1)}e\|^2\bigr).
}
\tag{C1zB2C5c.37}
\]

Dies ist exakt die in C5a als `(C1zB2C5a.21)` offen gelassene Prime-Frame-/Observability-Ungleichung — jetzt bewiesen auf dem glatten geraden Testcore.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,even\text{-}core\text{-}observability}.
}
\]

---

# 13. Feshbach-Konsequenz: primitive gerade Terminalenergie ist punktweise uniform beschränkt

Setze

\[
h=h_{T,f}^{(1)},
\qquad
R=R_T^{(1)}.
\]

Aus Lemma C5c.1 und (C1zB2C5c.35)--(C1zB2C5c.36):

\[
\boxed{
\langle h,(I+(R_T^{(1)})^*R_T^{(1)})^{-1}h\rangle
\le
C_{R,f}.
}
\tag{C1zB2C5c.38}
\]

Da der vollständige Restoperator zusätzliche positive Kanäle enthält,

\[
I+R_T^*R_T
\ge
I+(R_T^{(1)})^*R_T^{(1)}
\]

und daher

\[
(I+R_T^*R_T)^{-1}
\le
(I+(R_T^{(1)})^*R_T^{(1)})^{-1}.
\]

Somit ist auch der primitive Beitrag im **vollen** Feshbach-Nenner uniform kontrolliert.

---

# 14. Höhere Prime-Powers bleiben uniform harmlos

C5a bewies bereits

\[
\sup_T\|H_T^{(\ge2)}\|<\infty.
\]

Schreibe

\[
h_T=h_T^{(1)}+h_T^{(\ge2)}.
\]

Da

\[
0<(I+R_T^*R_T)^{-1}\le I,
\]

folgt

\[
\begin{aligned}
\sigma_T(J_{R,T}f)
&=
\|(I+R_T^*R_T)^{-1/2}h_T\|^2\\
&\le
2\|(I+R_T^*R_T)^{-1/2}h_T^{(1)}\|^2
+2\|h_T^{(\ge2)}\|^2.
\end{aligned}
\]

Daher:

\[
\boxed{
\sup_{T>R}
\sigma_T(J_{R,T}f)
<\infty
\qquad
\forall f\in C_c^\infty((-R,R))\cap\mathcal K_{X,R}^+.
}
\tag{C1zB2C5c.39}
\]

Und damit

\[
\boxed{
\sup_{T>R}
\langle G_{R,T}f,f\rangle_{X,R}
<\infty
}
\tag{C1zB2C5c.40}
\]

für jeden festen glatten geraden Testvektor.

Dies ist der erste vollständige positive Terminal-Beschränktheitssatz für einen gesamten **dichten Paritäts-Testcore** im C1z-Strang.

---

# 15. Der Prime-Mikrostruktur-Ausgang ist auf diesem Core geschlossen

C5b ließ als negativen Ausgang eine Folge

\[
e_T\in\mathscr H_T^-
\]

mit normalisiertem Restgraphen und wachsendem Hubfunktional offen.

Nach (C1zB2C5c.37) ist dies für einen festen glatten geraden Test `f` unmöglich.

Ist

\[
\|e_T\|^2+\|R_T^{(1)}e_T\|^2=1,
\]

dann gilt automatisch

\[
\boxed{
|\mathcal L_{T,f}^{\rm prim}(e_T)|
\le
\sqrt{C_{R,f}}
\qquad\forall T.
}
\tag{C1zB2C5c.41}
\]

Dabei gibt es **keine** Regularitätsannahme an `e_T`.

Die Folge darf

- beliebig hochoszillatorisch sein;
- von den diskreten Primepunkten abhängen;
- ihre Mikroskala mit `T` beliebig schnell verkleinern;
- gleichzeitig viele Primreflexionen nahezu neutralisieren.

Sie kann dennoch das feste glatte Hubfunktional nicht aufblasen, weil die Kontrolle vollständig auf der **Dualseite** erfolgt.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,prime\text{-}micro\text{-}witness\text{-}on\text{-}core}.
}
\]

---

# 16. Warum dies C5a.2 nicht widerspricht

C5a.2 zeigte:

\[
\text{kein fester endlicher Primblock ist quantitativ koerziv.}
\]

Dieser Satz bleibt vollständig richtig.

C5c beweist **keine** Koerzivität eines endlichen Blocks und auch keine globale Lower-Frame-Schranke

\[
\|e\|^2\lesssim\|R_T^{(1)}e\|^2.
\]

Stattdessen benutzt C5c die exponentiell große **Gesamtmasse vieler Future-Primes** in jedem short-interval Zellblock und verteilt das benötigte Dualzertifikat über diese orthogonalen Restkanäle.

Die Kosten pro Zelle sind

\[
\frac{|I|^2}{W_I},
\]

nicht die Inverse eines einzelnen Kanalgewichts.

Genau dadurch entsteht der C5b-Future-Screening-Gewinn.

---

# 17. Warum kein Standard-Large-Sieve-Satz importiert wurde

Der Beweis verwendet zwar eine moderne PNT-in-short-intervals-Eingabe, aber **keinen Standard-Large-Sieve-Satz** als Black Box für unsere Operatorungleichung.

Die Schritte sind stattdessen:

1. exakte Feshbach-Dualisierung;
2. exakte signless triangle identity;
3. explizite kontinuierliche Future-Zertifikatsnorm;
4. short-interval PNT nur als positive Massenuntergrenze für Prime-Zellen;
5. exakt massennormalisierte Quadratur mit den tatsächlichen `w_q`;
6. exponentiell kleine Diskretisierungsfehler aufgrund der glatten Dualdaten.

Damit ist die Beweisrichtung kompatibel mit der C5b-Firewall:

\[
\boxed{
\text{keine schwache Primmaßkonvergenz }\Rightarrow\text{ Operatornorm-Liminf wird behauptet.}
}
\]

Die diskrete Source-Mikrostruktur wird nie durch einen falschen Kontinuumsübergang ersetzt.

---

# 18. Was genau jetzt positiv geschlossen ist

Für jedes feste `R` und jedes feste gerade

\[
f\in C_c^\infty((-R,R))
\]

gilt:

### Primitive Hubfunktionalform

\[
\boxed{
|\mathcal L_{T,f}^{\rm prim}(e)|^2
\le
C_{R,f}
(\|e\|^2+\|R_T^{(1)}e\|^2)
}
\]

uniform in `T` und für **alle** ungeraden `e`.

### Primitive Feshbachenergie

\[
\boxed{
\sup_T
\langle h_{T,f}^{(1)},
(I+R_T^*R_T)^{-1}h_{T,f}^{(1)}\rangle
<\infty.
}
\]

### Vollständige Hub-Feshbachenergie

\[
\boxed{
\sup_T\sigma_T(J_{R,T}f)<\infty.
}
\]

### Zukunftsmetrik auf dem glatten even core

\[
\boxed{
\sup_T
\langle G_{R,T}f,f\rangle_{X,R}<\infty.
}
\]

Damit ist der **C5b-Binärtest auf dem glatten geraden Testcore positiv entschieden**.

---

# 19. Was noch nicht folgt

Die folgenden stärkeren Aussagen bleiben offen:

## 19.1 Keine automatische uniforme Operatornorm auf der Graphvervollständigung

Der konstante Faktor

\[
C_{R,f}
\]

wird im Diskretisierungsbeweis über glatte Normen von `f` kontrolliert.

Noch nicht bewiesen ist eine Schranke der Form

\[
C_{R,f}
\le
C_R\|f\|_{X,R}^2.
\]

Daher folgt aus C5c **noch nicht**

\[
\sup_T
\|G_{R,T}|_{\mathcal K_{X,R}^+}\|<\infty.
\]

Dichte des glatten Cores allein reicht hierfür nicht.

## 19.2 Beschränktheit ist noch keine Konvergenz

C5c beweist

\[
\sup_T\sigma_T(Jf)<\infty,
\]

nicht

\[
\sigma_T(Jf)\to L_f.
\]

Die Screening- und Source-Annulus-Effekte aus C1z-B2-C sind weiterhin nicht monoton.

## 19.3 Der relative Transport bleibt offen

Insbesondere ist noch nicht bewiesen

\[
\mathscr K_{R,S,+}^{T,U}\to I
\]

oder

\[
W_{R,S,+}^{[T]}\to W_{R,S,+}^{[\infty]}.
\]

C5c entfernt aber den bisher einzigen quantitativen Engpass für **Punktbeschränktheit** des geraden glatten Cores.

---

# 20. Statusmatrix

| Aussage | Status |
|---|---|
| Feshbach-Minimierungsformel (Dualzertifikat) | `✓[M]` |
| glatter Boundary-Hubkern `k_T` | `✓[M]` |
| Future-Prime-Rest = signless reflection edges | `✓[M]` |
| signless triangle identity | `✓[M]` |
| kontinuierliches Future-Dualzertifikat | `✓[M]` |
| Zertifikatsnorm `O_f(1/T)` für wachsenden Primblock | `✓[M]` |
| PNT in allen `x^{3/5}`-Intervallen | externer unbedingter Satz (Guth–Maynard) |
| Prime-Zellmasse `W_I asymp m_T(r_I)|I|` | `✓[M]` aus Short-interval PNT |
| massennormalisierte Quadratur | `✓[M]` |
| diskretes Future-Prime-Zertifikat | `✓[M]` |
| Diskretisierungsrest exponentiell klein | `✓[M]` auf glattem Core |
| C5a-Prime-Frame-Ungleichung auf glattem even core | `✓[M]` |
| T-abhängige Prime-Mikrostruktur als Divergenzzeuge für festes glattes gerades `f` | `×[M]` |
| vollständige even-core Terminalenergie punktweise beschränkt | `✓[M]` |
| uniforme Operatornorm auf `K_{X,R}^+` | `?[O]` |
| Konvergenz von `G_{R,T}^+` | `?[O]` |
| gerader Cross-Terminal-Kern `->I` | `?[O]` |
| gerader relativer Transportlimes | `?[O]` |
| ungerader relativer Transportlimes | `?[O]` |
| Objekt X / RH | `?[O]` |

---

# 21. Strukturelle Bedeutung

Die C5a/C5b-Kette hatte den Eindruck erzeugt, dass Objekt X an einer schwierigen globalen Lower-Frame-Ungleichung für die gesamte wachsende Primfamilie hängen könnte.

C5c zeigt, dass dies für den eigentlichen Feshbachzweck **zu stark formuliert war**.

Gesucht ist nicht

\[
R_T^{(1)}\text{ koerziv auf ganz }\mathscr H_T^-.
\]

Gesucht ist nur

\[
h_{T,f}^{(1)}
\in
\operatorname{Dom}\bigl((I+(R_T^{(1)})^*R_T^{(1)})^{-1/2}\bigr)
\]

mit uniformer Dualnorm für den konkreten glatten Hubvektor.

Und genau dies wird durch das Future-Prime-Dualzertifikat erreicht.

Die strukturelle Kette lautet nun:

\[
\boxed{
\begin{array}{c}
\text{gerader Source-Test}\\
\downarrow\\
\text{ungerader Hubvektor}\\
\downarrow\\
\text{keine primitive Restnullmode}\\
\downarrow\\
\text{same-prime CS verliert }\log T\\
\downarrow\\
\text{Future-Screening }d\mapsto d/2\\
\downarrow\\
\text{signless triangle identity}\\
\downarrow\\
\text{explizites kontinuierliches Dualzertifikat}\\
\downarrow\\
\text{short-interval Prime-Masse + exakt normalisierte Zellquadratur}\\
\downarrow\\
\textbf{uniforme primitive Observability auf dem glatten even core.}
\end{array}}
\]

Damit ist erstmals ein kompletter positiver Kontrollsatz für einen dichten Paritäts-Testcore erreicht, ohne einen neuen Regulator und ohne RH-Annahme.

---

# 22. Nächster atomarer Knoten

C5c beantwortet **Beschränktheit**, noch nicht **Cauchy-Konvergenz**.

Der nächste Knoten soll deshalb nicht nochmals eine Prime-Frame-Ungleichung beweisen.

Er lautet:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C5d]
\quad
\text{Even-core terminal Cauchy / completion audit}.
}
\]

Die scharfen Fragen sind:

### C5d-A — Tail-Dualzertifikat

Kann die C5c-Konstruktion für die **Differenz zweier Terminalhorizonte** `U>T` so gewählt werden, dass

\[
\boxed{
\|y_{T,U}\|^2+\|z_{T,U}\|^2\to0
}
\]

für jedes feste glatte gerade `f`?

Das wäre stärker als bloße Punktbeschränktheit und würde die Schurenergien Cauchy machen.

### C5d-B — Form-Cauchy auf dem even core

Prüfe

\[
\sigma_U(J_{R,U}f,J_{R,U}g)
-
\sigma_T(J_{R,T}f,J_{R,T}g)
\to0
\]

für glatte gerade `f,g`.

### C5d-C — Relative Gauge

Falls die even-core Zukunftsformen einen positiven Grenzwert besitzen, teste daraus direkt

\[
\mathscr K_{R,S,+}^{T,U}\to I
\]

beziehungsweise

\[
W_{R,S,+}^{[T]}\to W_{R,S,+}^{[\infty]}.
\]

Die neue Leitfrage lautet daher nicht mehr

\[
\text{„screenen die Primkanäle den geraden Hub überhaupt?“}
\]

sondern

\[
\boxed{
\text{„ist das jetzt bewiesene Screening auch terminal-tail-stabil?“}
}
\]

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal.
