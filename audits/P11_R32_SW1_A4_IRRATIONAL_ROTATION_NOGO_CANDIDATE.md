# P11/R32 — SW1-A4 Irrational-Rotation Point-Orbit No-Go Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-a3-free-coordinate-gram@82559ac41961c7c306ae564fa17d6b842838bc39  
> **Status:** ?[O] — exakter Negativkandidat hergeleitet; Zertifikat/Re-Review offen; keine Promotion.  
> **Scope:** ausschließlich No-Go gegen eine exhaustive Zerlegung des oberen SW1-Chambers in endlich große physische Punktorbits. Keine Aussage gegen Operatorinjektivität.

---

## 0. Motivation

A0/A1 liefern endlich viele räumliche Zellen, aber A1 warnt ausdrücklich:

\[
\text{finite cells}
\not\Rightarrow
\text{finite point orbits}.
\]

A4 entscheidet diese Frage im oberen A-Wall-Chamber

\[
\boxed{
\frac{\Delta}{2}<\varepsilon<\Delta-R.
}
\tag{A4.1}
\]

Das Ergebnis ist negativ: ein konkreter aktiver Echo-Teilgraph enthält eine irrationale Kreisrotation.

---

## 1. Das Rotationsintervall

Setze

\[
\boxed{
A_\varepsilon:=2d-\varepsilon
=
a+\Delta-\varepsilon,
}
\tag{A4.2}
\]

\[
\boxed{
B_\varepsilon:=T-\varepsilon
=
2a-\varepsilon.
}
\tag{A4.3}
\]

Dann

\[
A_\varepsilon>a
\]
wegen \(\varepsilon<\Delta\), und
\[
B_\varepsilon<T.
\]

Definiere

\[
\boxed{
I_\varepsilon
:=
(A_\varepsilon,B_\varepsilon).
}
\tag{A4.4}
\]

Seine Länge ist parameterunabhängig:

\[
\boxed{
L
:=
B_\varepsilon-A_\varepsilon
=
a-\Delta
=
2e.
}
\tag{A4.5}
\]

Ferner setze den Schnittpunkt

\[
\boxed{
C_\varepsilon
:=
B_\varepsilon-\Delta
=
2a-\varepsilon-\Delta.
}
\tag{A4.6}
\]

Dann

\[
C_\varepsilon-A_\varepsilon
=
a-2\Delta
>0,
\tag{A4.7}
\]

und

\[
B_\varepsilon-C_\varepsilon
=
\Delta.
\tag{A4.8}
\]

Also

\[
I_\varepsilon
=
I_-\dot\cup I_+
\quad\text{a.e.},
\]
mit

\[
I_-:=(A_\varepsilon,C_\varepsilon),
\qquad
I_+:=(C_\varepsilon,B_\varepsilon).
\tag{A4.9}
\]

Da \(I_\varepsilon\subset(a,T)\), liegt auf diesem ganzen Intervall kein abhängiger linker KNF-\(a\)-Branch. Jeder physische Punkt ist dort entweder eine freie Blindkoordinate oder eine freie rechte Samplekoordinate.

---

## 2. Aktive Echo-Isometrien

Schreibe

\[
r_c(x):=c-x.
\]

Aus den A1-Archetypen sind auf den im Folgenden verwendeten Zellen die drei Reflexionen

\[
r_{3a},
\qquad
r_{2b},
\qquad
r_{4a}
\tag{A4.10}
\]

mit den Koeffizienten

\[
\beta_-,
\qquad
\beta_b,
\qquad
\beta_T
\tag{A4.11}
\]

aktiv.

Alle drei Koeffizienten sind strikt nichtzero:

\[
\beta_-=-2c_2<0,
\qquad
\beta_b=-c_{11}<0,
\qquad
\beta_T=-\frac58\log2<0.
\tag{A4.12}
\]

Damit sind die folgenden Pfade echte Kantenpfade des A-/Free-Coordinate-Graphen und keine formalen Nullkopplungen.

---

## 3. Unterer Zweig: Translation um \(+\Delta\)

Sei

\[
x\in I_-.
\]

Der erste Echo-Schritt ist

\[
x_1:=r_{3a}(x)=3a-x.
\tag{A4.13}
\]

Für \(x\in I_-\) gilt

\[
a+\varepsilon+\Delta
<
x_1
<
T-\Delta+\varepsilon.
\tag{A4.14}
\]

Insbesondere

\[
x_1>a+\varepsilon>2d-\varepsilon
\]
im oberen Chamber, und

\[
x_1<T.
\]

Damit liegt \(x_1\) vollständig in A1-Zonen, in denen der Wort-11-Echo
\[
r_{2b}
\]
aktiv ist.

Der zweite Schritt liefert

\[
\begin{aligned}
x_2
&:=r_{2b}(x_1)\\
&=2b-(3a-x)\\
&=x+(2b-3a).
\end{aligned}
\]

Da

\[
2b-3a
=
2d-a
=
\Delta,
\]
folgt

\[
\boxed{
x_2=x+\Delta.
}
\tag{A4.15}
\]

Wegen
\[
x<C_\varepsilon=B_\varepsilon-\Delta
\]
liegt
\[
x+\Delta<B_\varepsilon.
\]
Also

\[
\boxed{
F(x):=x+\Delta
\in I_\varepsilon
\qquad(x\in I_-).
}
\tag{A4.16}
\]

Der untere Rotationszweig wird somit durch den echten Zwei-Echo-Pfad

\[
\boxed{
r_{2b}\circ r_{3a}
}
\tag{A4.17}
\]

realisiert.

---

## 4. Oberer Zweig: Wrap-around-Translation

Sei nun

\[
x\in I_+.
\]

Zunächst liegt \(I_+\) vollständig in A1-R5. Denn

\[
C_\varepsilon-(a+\varepsilon)
=
a-\Delta-2\varepsilon
=
(a-3\Delta)+2(\Delta-\varepsilon)
>0.
\tag{A4.18}
\]

Hier wurde nur
\[
a-3\Delta>0
\]
und
\[
\varepsilon<\Delta
\]
verwendet.

Setze

\[
x_1:=r_{3a}(x)=3a-x.
\tag{A4.19}
\]

Dann

\[
a+\varepsilon
<
x_1
<
a+\varepsilon+\Delta.
\tag{A4.20}
\]

Außerdem

\[
a+\varepsilon+\Delta
<
T-\varepsilon
\tag{A4.21}
\]
wegen A4.18. Somit liegt \(x_1\) vollständig in A1-R5 und \(r_{2b}\) ist aktiv.

Der zweite Schritt ist

\[
x_2:=r_{2b}(x_1)=x+\Delta.
\tag{A4.22}
\]

Da \(x\in(B_\varepsilon-\Delta,B_\varepsilon)\),

\[
T-\varepsilon
<
x_2
<
T-\varepsilon+\Delta.
\tag{A4.23}
\]

Wegen des oberen Chambers

\[
2\varepsilon>\Delta
\]
gilt

\[
T-\varepsilon+\Delta<T+\varepsilon=T_0.
\tag{A4.24}
\]

Also liegt \(x_2\) vollständig im erweiterten \(T\)-Tail A1-R6/R7, wo
\[
r_{4a}(u)=4a-u=2T-u
\]
mit Koeffizient \(\beta_T\ne0\) aktiv ist.

Setze

\[
x_3:=r_{4a}(x_2)=4a-x_2.
\tag{A4.25}
\]

Aus A4.23 folgt

\[
T+\varepsilon-\Delta
<
x_3
<
T+\varepsilon.
\tag{A4.26}
\]

Wegen \(2\varepsilon>\Delta\) ist
\[
T+\varepsilon-\Delta>T-\varepsilon,
\]
also liegt auch \(x_3\) vollständig in A1-R6/R7, wo \(r_{2b}\) aktiv ist.

Der vierte Schritt ergibt

\[
\begin{aligned}
x_4
&:=r_{2b}(x_3)\\
&=2b-\bigl(4a-(x+\Delta)\bigr)\\
&=x+2\Delta-a.
\end{aligned}
\tag{A4.27}
\]

Mit
\[
L=a-\Delta
\]
ist

\[
2\Delta-a
=
\Delta-L.
\]

Daher

\[
\boxed{
x_4
=
x+\Delta-L.
}
\tag{A4.28}
\]

Für \(x\in I_+\) gilt exakt

\[
A_\varepsilon
<
x+\Delta-L
<
A_\varepsilon+\Delta
<
B_\varepsilon.
\tag{A4.29}
\]

Somit

\[
\boxed{
F(x):=x+\Delta-L
\in I_\varepsilon
\qquad(x\in I_+).
}
\tag{A4.30}
\]

Der obere Wrap-around-Zweig wird durch den echten Vier-Echo-Pfad

\[
\boxed{
r_{2b}\circ r_{4a}\circ r_{2b}\circ r_{3a}
}
\tag{A4.31}
\]

realisiert.

---

## 5. Exakte Kreisrotation

Identifiziere

\[
I_\varepsilon
\]
mit dem Kreis

\[
\mathbb R/L\mathbb Z
\]
durch

\[
t=x-A_\varepsilon.
\]

Dann ist der Schnittpunkt

\[
C_\varepsilon-A_\varepsilon
=
L-\Delta.
\tag{A4.32}
\]

A4.16 und A4.30 werden exakt zu

\[
\boxed{
t\longmapsto t+\Delta\pmod L.
}
\tag{A4.33}
\]

Die aktive Echo-Geometrie enthält somit auf \(I_\varepsilon\) die Kreisrotation um den Winkel/Schritt \(\Delta\) bei Umfang

\[
L=a-\Delta.
\]

---

## 6. Irrationalität

Wir zeigen

\[
\boxed{
\frac{\Delta}{a-\Delta}\notin\mathbb Q.
}
\tag{A4.34}
\]

Es genügt zu zeigen

\[
\frac a\Delta\notin\mathbb Q.
\]

Angenommen

\[
\frac a\Delta=\frac mn
\]
mit positiven ganzen Zahlen \(m,n\). Dann

\[
na=m\Delta.
\]

Mit

\[
a=\frac12\log2,
\qquad
\Delta=\frac12\log\frac98
\]
folgt

\[
2^n
=
\left(\frac98\right)^m
=
\frac{3^{2m}}{2^{3m}}.
\]

Also

\[
\boxed{
2^{n+3m}=3^{2m}.
}
\tag{A4.35}
\]

Dies ist wegen eindeutiger Primfaktorzerlegung für \(m,n>0\) unmöglich.

Damit ist \(a/\Delta\) irrational und folglich auch A4.34.

---

## 7. No-Go für finite Punktorbits

Eine endliche Bahn der Rotation A4.33 würde für ein \(N\ge1\) verlangen

\[
N\Delta\equiv0\pmod L,
\]
also

\[
\frac{\Delta}{L}\in\mathbb Q,
\]
im Widerspruch zu A4.34.

Daher besitzt jede Kreisbahn unendlich viele Punkte.

In der offenen Intervallrepräsentation können lediglich diejenigen Ausgangspunkte problematisch sein, deren Bahn einen der endlich vielen Branch-/Randpunkte trifft. Diese Menge ist höchstens abzählbar.

Somit gilt:

\[
\boxed{
\text{Für fast jedes }x\in I_\varepsilon
\text{ enthält der aktive Echo-Orbit unendlich viele Punkte.}
}
\tag{A4.36}
\]

Nach dem klassischen Irrational-Rotation-Satz sind diese Bahnen sogar dicht in \(I_\varepsilon\) modulo der Kreisidentifikation.

Insbesondere ist unmöglich:

\[
\boxed{
\text{eine a.e. exhaustive Zerlegung von }I_\varepsilon
\text{ in endlich große physische Echo-Punktorbits.}
}
\tag{A4.37}
\]

---

## 8. Bedeutung für \(\mathfrak G_R\)

Das Intervall

\[
I_\varepsilon\subset(a,T)
\]
besteht ausschließlich aus freien KNF-Koordinaten:

- Blindkoordinaten außerhalb der Samplefenster;
- freie \(b\)- und \(T\)-nahe Samplekoordinaten innerhalb der Samplefenster.

Der einzige abhängige KNF-Branch liegt in

\[
(a-R,a),
\]
also strikt links von \(I_\varepsilon\).

Die in A4 verwendeten Echo-Pfade besitzen nur nichtverschwindende Koeffizienten.
Daher sind sie echte Kanten des freien A1/A3-Operatorgraphen.

Folglich enthält auch der freie Gramgraph von

\[
\mathfrak G_R
=
J_R^*(I+A)J_R
\]
a.e. unendliche physische Punktorbits im oberen Chamber.

Dies widerlegt ausschließlich die Strategie

\[
\boxed{
\text{A0 finite cells}
\Rightarrow
\text{finite point-orbit matrices}.
}
\tag{A4.38}
\]

---

## 9. Was dieser No-Go NICHT sagt

A4 beweist nicht:

- dass \(\mathfrak G_R^{-1}\) nicht explizit analysierbar ist;
- dass keine endliche **Zell**darstellung existiert — A1 beweist gerade eine solche;
- dass keine funktionalanalytische oder Transferoperator-Methode funktioniert;
- dass \(\mathcal L_{\rm ann}^{\rm SW1}\) einen nichttrivialen Kern besitzt;
- dass \(\ker\Gamma_I\ne0\);
- HT-RED;
- Objekt X;
- RH.

Der Befund betrifft nur die geplante Reduktion auf endlich große **Punktorbits**.

Er steht auch nicht im Widerspruch zu Stage 10B des Δ-Descents: Dort wurden endliche Orbits einer anderen, engen **Parameterreflexionsgruppe** auf \((R,\varepsilon)\) bewiesen. A4 betrifft den physischen Echo-Graphen auf einem viel größeren \(x\)-Intervall.

---

## 10. Strategische Konsequenz

Im oberen Chamber

\[
\varepsilon>\Delta/2
\]
muss A3/A4 daher als echter unendlichdimensionaler finite-cell Operator behandelt werden.

Der nächste sinnvolle Angriff ist nicht mehr ein Punktorbit-Determinantentest, sondern beispielsweise:

1. Transfer-/Irrational-Rotations-Darstellung auf \(I_\varepsilon\);
2. Fourier-/Floquet-artige Analyse der Rotationskomponente;
3. coercive Schurkomplementabschätzungen auf Zellebene;
4. Suche nach einer gerichteten Elimination, die die Rotation nicht punktweise auflöst.

**Firewall:** A4 ist ein Strategieno-go, kein No-Go gegen die Schur-Cross-Gram-Injektivität.
