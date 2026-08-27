# P11/R32 — Tail-FG-Pivot und exakte Horizontschwanz-Elimination

**Status:** Rechenkandidat; keine Promotion.  
**Arbeitsnamen:** `HT-A1`, `HT-A2`, `HT-A3`, `HT-A4`, `HT-RED`.  
**Repo-Basis:** `main@c0109e93846ce21e1a1df96877f40637f4f404c0`.  
**Scope:** ausschließlich die Klasse `0<R<epsilon` im bevorzugten restricted-tail-Stratum; keine Änderung bestehender Statusbuchungen.  
**Basis:** `P11_R32_A_WALL_REDUCTION_CANDIDATE.md`, `P11_R32_SCHUR_INVERSE_ELIMINATION_AUDIT.md`, `P11_R32_INVISIBLE_FIBER_GRAPH_CLASSIFICATION_AUDIT.md`, `P11_R32_FG_EXHAUSTIVITY_CLOSURE.md`, `P11_R32_TRIANGULAR_ROW_SPLITTING_AUDIT.md`.

> Dieses Dokument wird ausdrücklich **vor** einem unabhängigen adversarialen Review committed.  
> Alle neuen Aussagen bleiben bis zu diesem Review Kandidaten; insbesondere bleiben A0 und die Schur-Cross-Gram-Injektivität `?[O]`.

---

## 0. Aussage in einem Satz

Im Horizontschwanz

\[
\mathcal T_R=(T+R,T_0)=(T+R,T+\varepsilon),
\qquad 0<R<\varepsilon<c-T,
\]

reduzieren die elf Full-Rest-Gram-Wörter auf exakt sechs physische Profile. Die Tail-Tail-Kompression von \(A\) ist ein positives skalares Vielfaches der Identität,

\[
P_{\mathcal T_R}AP_{\mathcal T_R}=\kappa I,
\qquad \kappa>0,
\]

und nach Einsetzen der Fiber-Graph-Koordinaten besitzt die augmentierte Tail-Zeile den invertierbaren Pivot

\[
(1+\kappa)I.
\]

Damit ist die freie Tail-Koordinate kandidatenweise exakt eliminierbar; die verbleibende Schwierigkeit liegt in den nach unten laufenden \(z/h\)- und Annulus-Hub-Kanälen.

---

## 1. Setup

Es gelten

\[
a=\frac12\log2,
\qquad
b=\frac12\log3,
\qquad
T=2a=\log2,
\]

\[
T_0=T+\varepsilon,
\qquad
0<R<\varepsilon<c-T,
\qquad
c=\frac12\log5.
\]

Ferner

\[
d=b-a,
\qquad
e=T-b,
\qquad
a=d+e,
\]

und

\[
\Delta:=d-e=2d-a=\frac12\log\frac98>0.
\]

Numerisch:

\[
\Delta\approx0.0588915178282,
\qquad
\frac\Delta2\approx0.0294457589141,
\]

\[
e\approx0.143841036226,
\qquad
d\approx0.202732554054.
\]

Die Tail-Klasse ist

\[
\boxed{
\mathcal T_R=(T+R,T+\varepsilon).
}
\tag{HT.1}
\]

Sei \(z\) gerade und auf \(\pm\mathcal T_R\) getragen. Für

\[
R<s<\varepsilon
\]

setze

\[
\boxed{
Z(s):=z(T+s).
}
\tag{HT.2}
\]

Aus FG folgt: \(\mathcal T_R\) ist ein blinder Teil des positiven physischen Supports, also eine freie Komponente von \(\mathcal Z_R^+\).

---

## 2. Elf Wörter und vier Echo-Terme

Für

\[
W_{\delta,\eta}^{(\lambda)}
=
(K_{2\delta}^{\rm tr})^*
M_{\{|u|\le T_0-\lambda\}}
K_{2\eta}^{\rm tr}
\]

gilt nach NEU-A-WALL-1

\[
\begin{aligned}
(W_{\delta,\eta}^{(\lambda)}y)(x)
={}&
-\chi_\lambda(x-\delta)
 \widetilde y(x-\delta-\eta)
\\
&+
\chi_\lambda(x-\delta)
 \widetilde y(x-\delta+\eta)
\\
&+
\chi_\lambda(x+\delta)
 \widetilde y(x+\delta-\eta)
\\
&-
\chi_\lambda(x+\delta)
 \widetilde y(x+\delta+\eta).
\end{aligned}
\tag{HT.3}
\]

Bezeichne diese vier Terme der Reihe nach mit

\[
E_1,E_2,E_3,E_4.
\]

Die elf Wörter sind:

| Nr. | Wort | \((\delta,\eta;\lambda)\) | Gewicht \(c_j\) |
|---:|---|---|---:|
| 1 | \(W_{a,a}^{(a)}\) | \((a,a;a)\) | \((\log2)2^{-3/2}\) |
| 2 | \(W_{a,T}^{(a)}\) | \((a,T;a)\) | \((\log2)2^{-9/4}\) |
| 3 | \(W_{a,3a}^{(a)}\) | \((a,3a;a)\) | \((\log2)2^{-3}\) |
| 4 | \(W_{T,a}^{(a)}\) | \((T,a;a)\) | \((\log2)2^{-9/4}\) |
| 5 | \(W_{T,T}^{(a)}\) | \((T,T;a)\) | \((\log2)2^{-3}\) |
| 6 | \(W_{T,3a}^{(a)}\) | \((T,3a;a)\) | \((\log2)2^{-15/4}\) |
| 7 | \(W_{3a,a}^{(a)}\) | \((3a,a;a)\) | \((\log2)2^{-3}\) |
| 8 | \(W_{3a,T}^{(a)}\) | \((3a,T;a)\) | \((\log2)2^{-15/4}\) |
| 9 | \(W_{3a,3a}^{(a)}\) | \((3a,3a;a)\) | \((\log2)2^{-9/2}\) |
| 10 | \(W_{T,T}^{(T)}\) | \((T,T;T)\) | \((\log2)/4\) |
| 11 | \(W_{b,b}^{(b)}\) | \((b,b;b)\) | \(2(\log3)/(3\sqrt3)\) |

Damit

\[
A=\sum_{j=1}^{11}c_jW_j.
\tag{HT.4}
\]

---

## 3. Vollständige Tail-Treffer-Tabelle

Wir betrachten auf der positiven Halbachse alle Terme aus (HT.3), die bei einem reinen Tail-Vektor \(z\) einen Wert \(Z(s)\) treffen.

Von den \(11\times4=44\) positiven Vier-Echo-Möglichkeiten überleben exakt die folgenden 16 Treffer:

| Wort | aktiver Term | Tail-Quelle | positiver Zielpunkt \(x\) | Beitrag |
|---|---|---|---:|---:|
| \(W_{a,a}^{(a)}\) | \(E_2\) | \(+T+s\) | \(T+s\) | \(+c_1Z(s)\) |
|  | \(E_4\) | \(+T+s\) | \(s\) | \(-c_1Z(s)\) |
| \(W_{a,T}^{(a)}\) | \(E_1\) | \(-T-s\) | \(a-s\) | \(-c_2Z(s)\) |
|  | \(E_2\) | \(+T+s\) | \(a+s\) | \(+c_2Z(s)\) |
| \(W_{a,3a}^{(a)}\) | \(E_1\) | \(-T-s\) | \(T-s\) | \(-c_3Z(s)\) |
|  | \(E_2\) | \(+T+s\) | \(s\) | \(+c_3Z(s)\) |
| \(W_{T,a}^{(a)}\) | \(E_1\) | \(-T-s\) | \(a-s\) | \(-c_4Z(s)\) |
| \(W_{T,T}^{(a)}\) | \(E_1\) | \(-T-s\) | \(T-s\) | \(-c_5Z(s)\) |
|  | \(E_2\) | \(+T+s\) | \(T+s\) | \(+c_5Z(s)\) |
| \(W_{T,3a}^{(a)}\) | \(E_2\) | \(+T+s\) | \(a+s\) | \(+c_6Z(s)\) |
| \(W_{3a,a}^{(a)}\) | \(E_1\) | \(-T-s\) | \(T-s\) | \(-c_7Z(s)\) |
| \(W_{3a,T}^{(a)}\) | — | — | — | \(0\) |
| \(W_{3a,3a}^{(a)}\) | \(E_2\) | \(+T+s\) | \(T+s\) | \(+c_9Z(s)\) |
| \(W_{T,T}^{(T)}\) | \(E_1\) | \(-T-s\) | \(T-s\) | \(-c_{10}Z(s)\) |
|  | \(E_2\) | \(+T+s\) | \(T+s\) | \(+c_{10}Z(s)\) |
| \(W_{b,b}^{(b)}\) | \(E_1\) | \(-T-s\) | \(2d-s\) | \(-c_{11}Z(s)\) |
|  | \(E_2\) | \(+T+s\) | \(T+s\) | \(+c_{11}Z(s)\) |

Die negativen Zielpunkte sind durch Geradheit die Spiegelbilder dieser Tabelle.

Alle nicht aufgeführten Terme sterben entweder am Multiplikator-Gate oder am Source-Horizon.

---

## 4. Sechs Koeffizienten

Die 16 Treffer gruppieren sich auf genau sechs Profile.

### 4.1 Tail-Diagonalkoeffizient

\[
\boxed{
\kappa=c_1+c_5+c_9+c_{10}+c_{11}.
}
\tag{HT.5}
\]

Also

\[
\boxed{
\kappa=
(\log2)
\left(
2^{-3/2}+2^{-3}+2^{-9/2}
\right)
+\frac{\log2}{4}
+\frac{2\log3}{3\sqrt3}.
}
\tag{HT.6}
\]

Numerisch

\[
\boxed{
\kappa\approx0.9584838626>0.
}
\tag{HT.7}
\]

### 4.2 Off-Tail-Koeffizienten

\[
\boxed{
\beta_0=-c_1+c_3
=(\log2)(2^{-3}-2^{-3/2}).
}
\tag{HT.8}
\]

\[
\boxed{
\beta_-=-c_2-c_4
=-(\log2)2^{-5/4}.
}
\tag{HT.9}
\]

\[
\boxed{
\beta_+=c_2+c_6
=(\log2)(2^{-9/4}+2^{-15/4}).
}
\tag{HT.10}
\]

\[
\boxed{
\beta_T=-c_3-c_5-c_7-c_{10}
=-\frac58\log2.
}
\tag{HT.11}
\]

\[
\boxed{
\beta_b=-c_{11}
=-\frac{2\log3}{3\sqrt3}.
}
\tag{HT.12}
\]

Numerisch:

\[
(\beta_0,\beta_-,\beta_+,\beta_T,\beta_b)
\approx
(-0.15842,-0.29143,0.19723,-0.43322,-0.42286).
\]

Alle fünf Off-Tail-Koeffizienten sind ungleich null.

---

## 5. Reine Tail-Wirkung und sechs Output-Intervalle

Definiere

\[
I_0=(R,\varepsilon),
\]

\[
I_-=(a-\varepsilon,a-R),
\qquad
I_+=(a+R,a+\varepsilon),
\]

\[
I_T=(T-\varepsilon,T-R),
\]

\[
I_b=(2d-\varepsilon,2d-R).
\]

Dann gilt auf \(x>0\):

\[
\boxed{
\begin{aligned}
(Az)(x)
={}&
\kappa\,1_{\mathcal T_R}(x)Z(x-T)
+\beta_0\,1_{I_0}(x)Z(x)
\\
&+\beta_-\,1_{I_-}(x)Z(a-x)
+\beta_+\,1_{I_+}(x)Z(x-a)
\\
&+\beta_T\,1_{I_T}(x)Z(T-x)
+\beta_b\,1_{I_b}(x)Z(2d-x).
\end{aligned}
}
\tag{HT.13}
\]

Mit gerader Fortsetzung folgt insbesondere

\[
\boxed{
P_{\mathcal T_R}AP_{\mathcal T_R}
=
\kappa I.
}
\tag{HT.14}
\]

Somit

\[
z\ne0,\quad
\operatorname{ess\,supp}z\subset\pm\mathcal T_R
\quad\Longrightarrow\quad
Az\ne0.
\tag{HT.15}
\]

Der Tail ist jedoch kein \(A\)-invarianter Unterraum, da alle fünf \(\beta\)-Koeffizienten nicht verschwinden.

---

## 6. Exakte Off-Tail-Shell-Kollisionen

Die fünf rein 2-adischen Intervalle

\[
I_0,I_-,I_+,I_T,\mathcal T_R
\]

sind im gesamten Tail-Sektor paarweise disjunkt.

Für den 3-adischen Kanal gilt

\[
\boxed{
I_b=I_-+\Delta,
}
\tag{HT.16}
\]

weil

\[
2d-a=\Delta.
\]

Daher

\[
\boxed{
I_b\cap I_-\ne\varnothing
\iff
\varepsilon-R>\Delta.
}
\tag{HT.17}
\]

Äquivalent:

\[
R<\varepsilon-\Delta.
\]

Ferner

\[
\boxed{
I_b\cap I_+\ne\varnothing
\iff
R<\frac\Delta2<\varepsilon.
}
\tag{HT.18}
\]

Es gibt keine weiteren Off-Tail-Shell-Kollisionen.

---

## 7. Selbstadjungierter Gegencheck: allgemeine Tail-Zeile

Werte nun \(Ay\) für ein beliebiges gerades \(y\) direkt bei

\[
x=T+s,
\qquad
R<s<\varepsilon
\]

aus.

Die adjungiert vertauschten Kreuzwörter reproduzieren exakt dieselben sechs Koeffizienten. Daher

\[
\boxed{
\begin{aligned}
(Ay)(T+s)
={}&
\kappa y(T+s)
+\beta_0y(s)
+\beta_-y(a-s)
\\
&+\beta_+y(a+s)
+\beta_Ty(T-s)
+\beta_by(2d-s).
\end{aligned}
}
\tag{HT.19}
\]

Diese Identität ist der für die freie Koordinatenanalyse relevante Tail-Row.

---

## 8. Annulus-Hub auf dem Tail

Im bevorzugten restricted-tail-Stratum

\[
T<S<T_0,
\qquad
\sigma:=S-T\le R
\]

gilt für \(x=T+s\), \(R<s<\varepsilon\):

\[
\boxed{
(HE_{\mathcal A}w)(T+s)
=
p\,w(a+s)+r\,w(e+s)+q\,w(s).
}
\tag{HT.20}
\]

Die drei \(x+\tau\)-Äste liegen außerhalb des Annulus und verschwinden.

Damit lautet die Tail-Projektion der ersten augmentierten Gleichung

\[
\boxed{
\begin{aligned}
0={}&
(1+\kappa)y(T+s)
+\beta_0y(s)
+\beta_-y(a-s)
\\
&+\beta_+y(a+s)
+\beta_Ty(T-s)
+\beta_by(2d-s)
\\
&+p\,w(a+s)+r\,w(e+s)+q\,w(s).
\end{aligned}
}
\tag{HT.21}
\]

---

## 9. Fiber-Graph-Klassifikation der sechs Argumente

Sei nun

\[
y=\widehat\Phi_R(z,0,h)\in\mathcal K_R.
\]

Im gesamten Tail-Sektor gilt

\[
0<R<\varepsilon<c-T<e<d.
\tag{HT.22}
\]

Daher ist insbesondere \(R<d\), also kann in FG-TR1 niemals die zweite Rekonstruktionsschicht \(x_1\) auftreten.

Für jedes \(R<s<\varepsilon\) sind drei Werte sofort blind:

\[
\boxed{
y(s)=z(s),
\qquad
y(a-s)=z(a-s),
\qquad
y(T+s)=z(T+s).
}
\tag{HT.23}
\]

### 9.1 Der Kanal \(a+s\)

\[
\boxed{
y(a+s)=
\begin{cases}
z(a+s),&s<d-R,\\
h(a+s),&s>d-R.
\end{cases}
}
\tag{HT.24}
\]

### 9.2 Der Kanal \(T-s\)

\[
\boxed{
y(T-s)=
\begin{cases}
z(T-s),&s<e-R,\\
h(T-s),&s>e-R.
\end{cases}
}
\tag{HT.25}
\]

### 9.3 Der Kanal \(2d-s\)

Da

\[
(2d-s)-a=\Delta-s,
\]

gilt

\[
\boxed{
y(2d-s)=
\begin{cases}
z(2d-s),&|s-\Delta|>R,\\
h(2d-s),&\Delta-R<s<\Delta,\\
x_0(s-\Delta),&\Delta<s<\Delta+R.
\end{cases}
}
\tag{HT.26}
\]

Im letzten Fall ist

\[
u=s-\Delta\in(0,R).
\]

Da \(R<d\), gilt ausschließlich die erste FG-TR1-Schicht:

\[
\boxed{
\begin{aligned}
x_0(u)
={}&
h(a+u)
-\frac rp\bigl[h(b-u)-h(b+u)\bigr]
\\
&-\frac qp\bigl[h(T-u)-h(T+u)\bigr].
\end{aligned}
}
\tag{HT.27}
\]

Alle fünf Argumente in (HT.27) liegen in \(\mathcal V_R\); der \(x_0\)-Ast erzeugt somit weder eine weitere Blind-\(z\)-Koordinate noch eine Rekursion.

---

## 10. Die fünf inneren Tail-FG-Wände

Setze

\[
D_-:=\Delta-R,
\qquad
D_0:=\Delta,
\qquad
D_+:=\Delta+R,
\]

\[
E:=e-R,
\qquad
A_*:=d-R.
\]

Dann wird die gesamte \(z/h/x_0\)-Klassifikation der Tail-Zeile durch genau

\[
\boxed{
D_-,D_0,D_+,E,A_*
}
\tag{HT.28}
\]

kontrolliert.

Die ersten beiden Downstream-Kanäle \(y(s)\) und \(y(a-s)\) bleiben in allen Zellen Blind-\(z\).

---

## 11. Exhaustive Parameter-Firewall

Ein Topologiewechsel kann nur auftreten,

1. wenn eine der fünf Wände aus (HT.28) einen Rand des \(s\)-Intervalls \((R,\varepsilon)\) trifft; oder
2. wenn zwei gleichzeitig aktive Wände ihre Reihenfolge tauschen.

### 11.1 Randtreffer

Für \(D_-\):

\[
D_-=\varepsilon
\iff
\varepsilon=\Delta-R,
\]

\[
D_-=R
\iff
R=\frac\Delta2.
\]

Für \(D_0\):

\[
D_0=\varepsilon
\iff
\varepsilon=\Delta,
\]

\[
D_0=R
\iff
R=\Delta.
\]

Für \(D_+\):

\[
D_+=\varepsilon
\iff
\varepsilon=\Delta+R.
\]

Für \(E\):

\[
E=\varepsilon
\iff
\varepsilon=e-R,
\]

\[
E=R
\iff
R=\frac e2.
\]

Für \(A_*\):

\[
A_*=\varepsilon
\iff
\varepsilon=d-R,
\]

\[
A_*=R
\iff
R=\frac d2.
\]

### 11.2 Wall-Wall-Kollisionen

Es gilt stets

\[
D_-<D_0<D_+.
\]

Ferner

\[
A_*-E=d-e=\Delta>0,
\]

\[
A_*-D_0=e-R>0,
\]

\[
A_*-D_-=e>0.
\]

\(A_*\) und \(D_+\) können im zulässigen Drei-Shift-Tailfenster nicht gleichzeitig aktiv sein.

Für \(E\) gilt

\[
E-D_-=e-\Delta>0,
\]

und solange beide aktiv sind auch

\[
E-D_0=e-R-\Delta>0.
\]

Der einzige mögliche innere Ordnungswechsel ist daher

\[
E-D_+
=
e-\Delta-2R.
\]

Setze

\[
\boxed{
C:=\frac{e-\Delta}{2}
=
e-\frac d2
\approx0.04247475920.
}
\tag{HT.29}
\]

Dann kollidieren \(E\) und \(D_+\) genau bei

\[
\boxed{R=C.}
\tag{HT.30}
\]

Damit besteht die exhaustive Tail-FG-Parameter-Firewall aus genau den zehn Hyperflächen

\[
\boxed{
\varepsilon=\Delta-R,\quad
R=\frac\Delta2,\quad
\varepsilon=\Delta,\quad
R=\Delta,\quad
\varepsilon=\Delta+R,
}
\]

\[
\boxed{
\varepsilon=e-R,\quad
R=\frac e2,\quad
\varepsilon=d-R,\quad
R=\frac d2,\quad
R=C.
}
\tag{HT.31}
\]

Alle Aussagen sind auf das offene Parameterdreieck

\[
0<R<\varepsilon<c-T
\]

beschränkt.

---

## 12. Exakt 15 offene Tail-FG-Chambers

Für die Signaturen verwenden wir

- \(Z\): direkter Blind-\(z\)-Wert,
- \(H\): direkter freier \(h\)-Wert,
- \(X\): der explizite Ausdruck \(x_0(h)\).

Das Tripel bezeichnet

\[
\bigl(y(a+s),y(T-s),y(2d-s)\bigr).
\]

### Zone I: \(0<R<\Delta/2\)

Hier beginnt jede Tail-Zeile mit \(ZZZ\).

| Chamber | Parameterbedingung | aktive Wände | Typfolge |
|---|---|---|---|
| I.1 | \(\varepsilon<\Delta-R\) | keine | \(ZZZ\) |
| I.2 | \(\Delta-R<\varepsilon<\Delta\) | \(D_-\) | \(ZZZ\to ZZH\) |
| I.3 | \(\Delta<\varepsilon<\Delta+R\) | \(D_-<D_0\) | \(ZZZ\to ZZH\to ZZX\) |
| I.4 | \(\varepsilon>\Delta+R\) | \(D_-<D_0<D_+\) | \(ZZZ\to ZZH\to ZZX\to ZZZ\) |

### Zone II: \(\Delta/2<R<\Delta\)

Hier beginnt jede Tail-Zeile mit \(ZZH\).

| Chamber | Parameterbedingung | aktive Wände | Typfolge |
|---|---|---|---|
| II.1 | \(\varepsilon<\Delta\) | keine | \(ZZH\) |
| II.2 | \(\Delta<\varepsilon<\min\{\Delta+R,e-R\}\) | \(D_0\) | \(ZZH\to ZZX\) |
| II.3 | \(e-R<\varepsilon<\Delta+R\) | \(D_0<E\) | \(ZZH\to ZZX\to ZHX\) |
| II.4 | \(\Delta+R<\varepsilon<e-R\) | \(D_0<D_+\) | \(ZZH\to ZZX\to ZZZ\) |
| II.5 | \(R<C,\ \varepsilon>\max\{\Delta+R,e-R\}\) | \(D_0<D_+<E\) | \(ZZH\to ZZX\to ZZZ\to ZHZ\) |
| II.6 | \(R>C,\ \varepsilon>\max\{\Delta+R,e-R\}\) | \(D_0<E<D_+\) | \(ZZH\to ZZX\to ZHX\to ZHZ\) |

Die Bedingungen II.3 bzw. II.4 sind nur dort nichtleer, wo die angegebene Intervallordnung möglich ist; die Trennung wird exakt durch \(R=C\) kontrolliert.

### Zone III: \(\Delta<R<e/2\)

Hier beginnt jede Tail-Zeile mit \(ZZX\). Im Drei-Shift-Fenster kann \(D_+\) hier nicht mehr aktiv werden.

| Chamber | Parameterbedingung | aktive Wände | Typfolge |
|---|---|---|---|
| III.1 | \(\varepsilon<e-R\) | keine | \(ZZX\) |
| III.2 | \(\varepsilon>e-R\) | \(E\) | \(ZZX\to ZHX\) |

### Zone IV: \(e/2<R<d/2\)

Hier beginnt jede Tail-Zeile mit \(ZHX\).

| Chamber | Parameterbedingung | aktive Wände | Typfolge |
|---|---|---|---|
| IV.1 | \(\varepsilon<d-R\) | keine | \(ZHX\) |
| IV.2 | \(\varepsilon>d-R\) | \(A_*\) | \(ZHX\to HHX\) |

### Zone V: \(d/2<R<\varepsilon\)

Hier gilt auf dem gesamten Tail-Intervall

\[
\boxed{HHX.}
\]

Damit gibt es insgesamt

\[
\boxed{4+6+2+2+1=15}
\tag{HT.32}
\]

offene Tail-FG-Chambers.

---

## 13. Tail-Pivot in freien Koordinaten

Setze in (HT.21)

\[
y=\widehat\Phi_R(z,0,h).
\]

Definiere

\[
Y_A(s):=y(a+s),
\qquad
Y_T(s):=y(T-s),
\qquad
Y_b(s):=y(2d-s),
\]

wobei ihre \(Z/H/X\)-Form auf jeder der 15 Chambers durch §12 festgelegt ist.

Dann lautet die Tail-Zeile

\[
\boxed{
\begin{aligned}
0={}&
(1+\kappa)z(T+s)
+\beta_0z(s)
+\beta_-z(a-s)
\\
&+\beta_+Y_A(s)
+\beta_TY_T(s)
+\beta_bY_b(s)
\\
&+p\,w(a+s)+r\,w(e+s)+q\,w(s).
\end{aligned}
}
\tag{HT.33}
\]

Da

\[
\boxed{
1+\kappa\approx1.9584838626>0,
}
\tag{HT.34}
\]

ist die Tail-Koordinate punktweise eindeutig bestimmt:

\[
\boxed{
\begin{aligned}
z(T+s)
=
-\frac{1}{1+\kappa}
\Bigl[
&\beta_0z(s)+\beta_-z(a-s)
+\beta_+Y_A(s)
\\
&+\beta_TY_T(s)
+\beta_bY_b(s)
\\
&+p\,w(a+s)+r\,w(e+s)+q\,w(s)
\Bigr].
\end{aligned}
}
\tag{HT.35}
\]

Alle \(y\)-Argumente rechts liegen strikt unterhalb des Tail:

\[
s,\ a-s,\ a+s,\ T-s,\ 2d-s<T+R.
\tag{HT.36}
\]

Der \(X=x_0\)-Ast enthält ebenfalls ausschließlich \(h\)-Daten unterhalb des Tail.

Daher entsteht keine Tail-zu-Tail-Rekursion.

---

## 14. Kandidatenlemma HT-RED — beschränkte Tail-Gaußelimination

Nach Parametrisierung von \(y\in\mathcal K_R\) zerlege den freien Blindraum orthogonal in

\[
\mathcal Z_R^+
=
\mathcal T_R^+
\oplus
\mathcal Z_{R,\mathrm{rest}}^+,
\]

wobei \(\mathcal T_R^+\) der gerade Tail-Supportraum ist.

Die erste augmentierte Zeile definiert dann bezüglich

\[
\mathcal T_R^+
\oplus
\bigl(
\mathcal Z_{R,\mathrm{rest}}^+
\oplus L^2(\mathcal V_R)
\oplus\mathscr H_{\mathcal A}^-
\bigr)
\]

und der Codomain-Zerlegung in Tail-/Nicht-Tail-Support einen Blockoperator der Form

\[
\begin{pmatrix}
(1+\kappa)I & B_{\rm tail}\\
C_{\rm tail} & D_{\rm rest}
\end{pmatrix}.
\tag{HT.37}
\]

Da \((1+\kappa)I\) beschränkt invertierbar ist, ist die Tail-Komponente exakt eliminierbar:

\[
z_{\rm tail}
=
-(1+\kappa)^{-1}B_{\rm tail}x.
\tag{HT.38}
\]

Der verbleibende Kernel ist damit kandidatenweise bijektiv äquivalent zum reduzierten Kernel

\[
\boxed{
\ker\Bigl(
D_{\rm rest}
-
C_{\rm tail}(1+\kappa)^{-1}B_{\rm tail}
\Bigr).
}
\tag{HT.39}
\]

Dies ist eine reine Block-Gauß-/Schur-Elimination des **Tail-Pivots** und keine Aussage über die Trivialität des reduzierten Kernes.

Insbesondere kann kein nichttriviales Kernelpaar ausschließlich auf der freien Tail-Koordinate getragen sein.

---

## 15. Kandidatenstatus

Vor unabhängigem Review:

```text
HT-A1 WORDWISE TAIL ACTION:              ?[O]
HT-A2 TAIL COMPRESSION / SCALAR PIVOT:   ?[O]
HT-A3 OFF-TAIL SHELL CLASSIFICATION:     ?[O]
HT-A4 TAIL-FG COMMON REFINEMENT:         ?[O]
HT-RED TAIL GAUSSIAN ELIMINATION:        ?[O]

A0 FULL FREE-COORDINATE COVERAGE:        ?[O]
SCHUR CROSS-GRAM INJECTIVITY:            ?[O]
```

Interner Rechenstand vor dem unabhängigen Review:

```text
HT-A1: candidate GREEN internally
HT-A2: candidate GREEN internally
HT-A3: candidate GREEN internally
HT-A4: candidate GREEN internally
HT-RED: new candidate
```

Keine dieser Zeilen ist eine mathematische Promotion.

---

## 16. Firewall

Aus diesem Kandidaten folgen **nicht**:

- A0 ist geschlossen;
- die vollständige \((z,h)\)-Analyse außerhalb des Tail-Sektors ist abgeschlossen;
- der reduzierte Kernel in (HT.39) ist trivial;
- der augmentierte Blockkernel ist trivial;
- \(\ker\Gamma_I=\{0\}\);
- Schur-Cross-Gram-Injektivität;
- bounded below / Closed Range;
- Strong Terminal Transport;
- ein Kandidat für Objekt X;
- RH.

Insbesondere bleiben

\[
\boxed{
\text{A0: }?[O]
}
\]

und

\[
\boxed{
\ker\Gamma_I=\{0\}\ ?[O].
}
\]

---

## 17. Adversarialer Review-Auftrag

Vor irgendeiner Promotion oder PR-Merge sind mindestens unabhängig zu prüfen:

1. alle \((\delta,\eta;\lambda)\)-Belegungen der elf Wörter;
2. die vollständige Enumeration der \(44\) Vier-Echo-Möglichkeiten und dass exakt die 16 Treffer in §3 überleben;
3. die Tail-Quellen \(+T+s\) bzw. \(-T-s\) jeder Tabellenzeile;
4. alle sechs Koeffizienten \(\kappa,\beta_0,\beta_-,\beta_+,\beta_T,\beta_b\);
5. die sechs Output-Intervalle in §5;
6. die Behauptung, dass \(I_b\) nur \(I_-\) und \(I_+\) schneiden kann;
7. die allgemeine Tail-Zeile (HT.19) als unabhängigen Selbstadjungiertheits-Gegencheck;
8. die Hubformel (HT.20) im restricted-tail-Stratum;
9. die drei Fiber-Graph-Klassifikationen (HT.24)–(HT.26);
10. dass im \(x_0\)-Ast alle fünf Argumente tatsächlich in \(\mathcal V_R\) liegen;
11. die Exhaustivität der fünf inneren \(s\)-Wände;
12. sämtliche zehn Parameterflächen in (HT.31) und dass keine weitere aktive Wall-Wall-Kollision existiert;
13. die 15 Chamber-Bedingungen in §12 einschließlich ihrer Nichtleere und Exhaustivität;
14. die strikte Downstream-Ungleichung (HT.36);
15. die Block-Gaußelimination (HT.37)–(HT.39);
16. die Scope-Firewall in §16.

Keine Promotion und kein Merge ohne unabhängiges GREEN gegen den exakten Commit-/PR-Diff.
