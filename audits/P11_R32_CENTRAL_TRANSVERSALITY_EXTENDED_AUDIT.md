# P11/R32 — horizon-adaptive zentrale Schur-Transversalität

**Status:** Kandidat; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Basis:** CT-1 / SE-1 / SE-2 Kandidatenkette. Dieser Audit ersetzt die gröbere uniforme CTX-Fassung vor deren Review.

## 1. Setup und adaptive Schwelle

Im Drei-Shift-Fenster
\[
2a<T_0<c:=\tfrac12\log5,
\qquad a=\tfrac12\log2,
\quad b=\tfrac12\log3,
\quad T=2a,
\]
setze
\[
d:=b-a,\qquad e:=a-d=2a-b,
\qquad \varepsilon:=T_0-T=T_0-2a.
\]
Fixiere
\[
\boxed{
R\ge \max\left\{\varepsilon,\frac d2\right\},
\qquad R<S<a.
}
\tag{CTX.1}
\]
Sei
\[
\mathcal C_R^+
:=\{y=y_{\rm even}:\operatorname{ess\,supp}y\subset[-(a-R),a-R]\}.
\]
Wie in SE-1 sei
\[
\mathcal K_{I,A}(y,w)
=\bigl((I+A)y+HE_{\mathcal A}w,\ E_I^*Hy\bigr),
\quad A=R_{T_0}^*R_{T_0},
\]
mit
\[
I=(-R,R),\qquad \mathcal A=(-S,-R)\cup(R,S).
\]
CI-1 gibt `E_I^*Hy=0` für jedes `y in C_R^+`. Es bleibt die erste Blockgleichung.

## 2. Restkollaps braucht nur R >= epsilon

Schreibe
\[
K:=K_{\log2}^{\rm tr},\qquad
\lambda:=(\log2)2^{-3/2}>0,
\qquad M_{20}:=1_{\Omega_{2,0,T_0}}.
\]
Dann gilt unter (CTX.1) exakt
\[
\boxed{Ay=\lambda K^*M_{20}Ky\qquad(y\in\mathcal C_R^+).}
\tag{CTX.2}
\]

Die zentrale Halbbreite ist
\[
D_R:=a-R\le a-\varepsilon.
\]
Für die drei Full-Rest-Blöcke aus SE-2:

1. Auf `Omega_(2,0)` ist die Maskenhalbbreite `T0-a=a+epsilon`. Beim `k=2`-Halbshift `2a` ist der kleinste Abstand zum Ursprung
   \[
   2a-(a+\varepsilon)=a-\varepsilon\ge D_R.
   \]
   Daher verschwindet der `k=2`-Term a.e. auf `C_R^+`; `k=3` liegt noch weiter außen.

2. Auf `Omega_(2,1)` ist die Maskenhalbbreite `epsilon`. Beim einzigen `k=2`-Halbshift ist der Abstand mindestens `2a-epsilon>D_R`, also verschwindet der ganze Block.

3. Auf `Omega_(3,0)` ist die Maskenhalbbreite
   \[
   T_0-b=e+\varepsilon.
   \]
   Beim `b`-Halbshift ist der kleinste Abstand
   \[
   b-(e+\varepsilon)=2d-\varepsilon.
   \]
   Wegen `d>a/2` (äquivalent `9>8`) gilt
   \[
   2d-\varepsilon>a-\varepsilon\ge D_R,
   \]
   also verschwindet auch `(3,0)`.

Somit bleibt nur `(2,0),k=1`.

Insbesondere gelten für `0<t<D_R`
\[
\boxed{(Ay)(t)=\lambda(1+1_{t<\varepsilon})y(t),}
\tag{CTX.3}
\]
und für `x in (R,S)`, `t=a-x`,
\[
\boxed{(Ay)(a+x)=-\lambda y(t).}
\tag{CTX.4}
\]

Da jeder Annuluspunkt `x>R>=epsilon` erfüllt, verschwinden alle epsilon-Indikatoren an Annulus- bzw. reflektierten Annuluspunkten; nur innere Punkte unterhalb `R` können den Indikator tragen.

## 3. Primitive Koeffizientenlücke

Setze
\[
C:=1+\lambda.
\]
Wir benötigen
\[
\boxed{G:=p^2-q^2C^2>0.}
\tag{CTX.5}
\]
Da
\[
\frac{q^2}{p^2}=2^{-3/2}=:\beta^2,
\]
genügt `beta^2 C^2<1`.

Aus der `atanh`-Reihe mit `z=1/3` folgt
\[
\log2
=2\sum_{n\ge0}\frac{3^{-(2n+1)}}{2n+1}
<2\left(\frac13+\frac1{72}\right)=\frac{25}{36}.
\]
Außerdem
\[
2^{-3/2}<\frac9{25}\quad(625<648),
\]
also
\[
\lambda<\frac14.
\]
Und
\[
2^{-3/2}<\frac38\quad(16<18).
\]
Daher
\[
\beta^2(1+\lambda)^2
<\frac38\left(\frac54\right)^2
=\frac{75}{128}<1,
\]
also (CTX.5).

## 4. Geometrische Grundschranke R >= d/2

Aus
\[
R\ge\frac d2
\]
folgen die drei geometrischen Fakten, die die Orbitstruktur endlich machen:

- `d<2R`, also kann ein rückwärtiger `b`-Ast nahe der Annulusmitte in das innere Fenster fallen;
- `e<d<=2R`, weil `d-e=\frac12\log(9/8)>0`;
- `S-R<a-d/2<2d`, denn `d>a/2` impliziert `a<2d<5d/2`.

Damit können die `d`-verschobenen Low-/High-Schalen niemals mehrfach hintereinander im Annulus liegen.

## 5. b-freie Reflexionsorbits

Für `x in (R,S)` setze `t=a-x`.

Falls
\[
x+d>S,
\qquad |x-d|<R,
\tag{CTX.6}
\]
sind beide `b`-Äste aus dem Annulus entfernt. Dann lauten die relevanten Punktgleichungen
\[
C_t y(t)-p w(x)=0,
\tag{CTX.7}
\]
\[
D_t y(t)-q\,1_{(R,S)}(t)w(t)=0,
\tag{CTX.8}
\]
mit
\[
C_t=1+\lambda(1+1_{t<\varepsilon}),
\qquad D_t=1+\lambda1_{t<\varepsilon}.
\]

Ist `t` nicht im Annulus, erzwingt (CTX.8) direkt `y(t)=0`, dann (CTX.7) `w(x)=0`.

Ist `t in (R,S)`, so gilt wegen `t,x>R>=epsilon`
\[
C_t=C_x=C=1+\lambda,
\qquad D_t=D_x=1.
\]
Die vier Gleichungen für das Reflexionspaar `x <-> t=a-x` haben Matrix
\[
M_4=
\begin{pmatrix}
C&0&-p&0\\
1&0&0&-q\\
0&C&0&-p\\
0&1&-q&0
\end{pmatrix}
\]
in den Variablen `(y(t),y(x),w(x),w(t))`. Es gilt
\[
\boxed{\det M_4=q^2C^2-p^2=-G\ne0.}
\tag{CTX.9}
\]
Also stirbt jedes b-freie Reflexionsorbit.

## 6. Der einzige b-gekoppelte Keil

Falls `S<=R+d`, ist jeder Annuluspunkt b-frei: `x+d>S`; und wegen `R>=d/2`, `x<S<=R+d` folgt auch `|x-d|<R`. Abschnitt 5 genügt dann vollständig.

Nehme nun
\[
S>R+d.
\tag{CTX.10}
\]
Definiere
\[
L:=(R,S-d),\qquad
H:=(R+d,S),\qquad
M:=(S-d,R+d).
\tag{CTX.11}
\]
Wegen `S-R<2d` sind `L` und `H` disjunkt und `M` liegt dazwischen. Die Abbildung
\[
x\mapsto X:=x+d
\]
ist eine Bijektion `L -> H`.

### 6.1 Low-High-Orbit

Fixiere `x in L` und setze
\[
X:=x+d\in H,
\qquad t:=a-x,
\qquad h:=a-X=e-x.
\]
Weil `L` nichtleer ist, gilt `x<S-d<e`, also `h>0`. Ferner `e<2R`, also `h<R`.

Aus `S>R+d` und `d>a/2` folgt
\[
R+S>2R+d\ge2d>a,
\]
also `t<S`. Andererseits ergibt `R+S<a+d=b` (aus `R<e` im Low-Fall und `S<a`) die Schranke `t>R`. Genauer liegt
\[
\boxed{t\in M\subset(R,S),\qquad 0<h<R.}
\tag{CTX.12}
\]
Die Mittelschale ist b-frei; beim High-Punkt `X` bleibt genau der rückwärtige `b`-Ast `w(X-d)=w(x)`.

Da `x,t,X` Annuluspunkte sind, tragen sie keinen epsilon-Indikator. Nur `h` kann `h<epsilon` erfüllen. Setze
\[
C_h:=1+\lambda(1+\iota_h),
\qquad D_h:=1+\lambda\iota_h,
\qquad \iota_h:=1_{h<\varepsilon}.
\]

Nach elementaren Zeilenoperationen auf den sechs Punktgleichungen erhält man für
\[
(y(t),y(x),y(h),w(x),w(t),w(X))
\]
die Matrix
\[
M_6=
\begin{pmatrix}
C&0&0&-p&0&-r\\
1&0&0&0&-q&-r\\
0&C&0&0&-p&0\\
0&1&0&-q&0&0\\
0&0&C_h&0&0&-p\\
0&0&D_h&r&0&0
\end{pmatrix}.
\tag{CTX.13}
\]
Ihre Determinante faktorisiert exakt zu
\[
\boxed{
\det M_6
=-p\Big(C_h\lambda r^2+D_h\,[p^2-q^2C^2]\Big).
}
\tag{CTX.14}
\]
Alle Faktoren in der Klammer sind strikt positiv und `G>0`. Daher `det M6<0`. Somit verschwinden auf jedem Low-High-Orbit alle sechs Variablen.

### 6.2 Rest der Mittelschale

Für `z in M` gilt `z+d>=S`. Für den rückwärtigen b-Ast:

- wenn `z>=d`, dann `0<=z-d<R`;
- wenn `z<d`, dann
  \[
  d-z\le2d-S<d-R\le R.
  \]

Also ist `M` b-frei.

Falls `a-z` außerhalb des Annulus liegt, greift die zweizeilige Elimination. Falls `a-z in L`, ist `z` bereits Teil eines 6er-Orbits. Falls `a-z` im Annulus liegt und nicht in `L`, kann es nicht in `H` liegen, denn
\[
a-H=(a-S,e-R)\subset(0,R)
\]
wegen `e<2R`. Also liegt `a-z` ebenfalls in `M`, und der invertible Reflexionsblock (CTX.9) greift.

Damit ist der gesamte Annulus erschöpft.

## 7. Tiefer Zentralbereich

Für
\[
0<t<a-S
\]
liegt jeder Hubshift des Annulus außerhalb seiner Unterstützung, also
\[
(HE_Aw)(t)=0.
\]
Mit (CTX.3) folgt
\[
\bigl[1+\lambda(1+1_{t<\varepsilon})\bigr]y(t)=0,
\]
also `y(t)=0`. Zusammen mit den Orbitgleichungen wird ganz `(0,a-R)` getötet, also wegen Geradheit ganz `C_R^+`; zugleich verschwindet `w` auf dem gesamten Annulus.

## 8. Theorem CTX-1 — horizon-adaptive zentrale Transversalität

Für jedes
\[
\boxed{
R\ge\max\left\{\varepsilon,\frac d2\right\},
\qquad R<S<a
}
\]
gilt
\[
\boxed{
\ker\mathcal K_{I,A}
\cap(\mathcal C_R^+\oplus\mathscr H_A^-)
=\{0\}.
}
\tag{CTX.15}
\]
Äquivalent
\[
\boxed{
\operatorname{Ran}(HE_A|_-)
\cap(I+A)\mathcal C_R^+
=\{0\}.
}
\tag{CTX.16}
\]

Da im Drei-Shift-Fenster
\[
\varepsilon<E:=c-2a=\tfrac12\log\frac54
\]
und
\[
E>\frac d2
\iff \left(\frac54\right)^2>\frac32
\iff25>24,
\]
folgt als horizont-uniformes Korollar
\[
\boxed{E\le R<S<a.}
\]
CT-1 (`a/2<=R<S<a`) ist ein noch gröberes Teilfenster hiervon.

## 9. Firewall

CTX-1 ist weiterhin nur ein Satz über Blockkernvektoren mit `y in C_R^+`. Nicht bewiesen sind:

- `ker K_{I,A}=0` für allgemeines `y in N_I`;
- voller Schur-Crossblock injektiv;
- bounded below / closed range / uniforme Winkel;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

Bei unabhängigem vollständigem GREEN wäre zulässig:

- **CTX-1:** `✓[M]_part` — der gesamte unendlichdimensionale zentrale Unsichtbarkeitssektor trägt im horizon-adaptiven Bereich `R>=max{epsilon,d/2}`, `R<S<a` keinen augmentierten Schur-Kernvektor.

Keine Promotion ohne explizite Freigabe.