# P11/R32 — erweiterte zentrale Schur-Transversalität für E <= R < S < a

**Status:** Kandidat; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Basis:** CT-1 / SE-1 / SE-2 Kandidatenkette; dieser Audit ist stärker als CT-1 und soll unabhängig geprüft werden.

## 1. Setup

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
\qquad E:=c-2a=\tfrac12\log\frac54.
\]
Fixiere
\[
\boxed{E\le R<S<a.}
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
CI-1 gibt bereits `E_I^* H y=0` für jedes `y in C_R^+`. Es bleibt also die erste Blockgleichung.

## 2. Exakte Restschwelle ist E, nicht a/2

Schreibe
\[
K:=K_{\log2}^{\rm tr},\qquad
\lambda:=(\log2)2^{-3/2}>0,
\qquad M_{20}:=1_{\Omega_{2,0,T_0}}.
\]
Dann gilt unter (CTX.1) weiterhin exakt
\[
\boxed{Ay=\lambda K^*M_{20}Ky\qquad(y\in\mathcal C_R^+).}
\tag{CTX.2}
\]

Grund: Die zentrale Halbbreite ist `a-R`. Für den `(2,0),k=2`-Term ist auf `Omega_(2,0)` der kleinste Abstand eines `2a`-Shiftarguments vom Ursprung strikt größer als
\[
3a-c.
\]
Wegen `R>=E=c-2a` gilt
\[
a-R\le a-E=3a-c,
\]
und wegen `T0<c` ist der tatsächliche Abstand strikt größer. Daher verschwinden die `k=2,3`-Anteile des `(2,0)`-Blocks. Der `(2,1)`-Block verschwindet noch deutlicher. Für `(3,0)` genügt
\[
a-R<2b-c,
\]
was bereits aus `R>=E` folgt, denn
\[
E-(a-2b+c)=\frac14\log\frac{25}{24}>0.
\]
Somit bleibt wieder nur der primitive `(2,0),k=1`-Term.

Insbesondere gelten die CT-1-Wirkungsformeln nun für ganz (CTX.1): Für `0<t<a-R`,
\[
\boxed{(Ay)(t)=\lambda(1+1_{t<\varepsilon})y(t),\qquad \varepsilon:=T_0-T<E,}
\tag{CTX.3}
\]
und für `x in (R,S)`, `t=a-x`,
\[
\boxed{(Ay)(a+x)=-\lambda y(t).}
\tag{CTX.4}
\]

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

Eine rein rationale Schranke ist möglich. Aus
\[
\log2
=2\sum_{n\ge0}\frac{3^{-(2n+1)}}{2n+1}
<\frac{25}{36}
\]
und
\[
2^{-3/2}<\frac9{25}
\quad(625<648)
\]
folgt
\[
\lambda=(\log2)2^{-3/2}<\frac14.
\]
Außerdem
\[
2^{-3/2}<\frac38
\quad(16<18).
\]
Daher
\[
\beta^2(1+\lambda)^2
<\frac38\left(\frac54\right)^2
=\frac{75}{128}<1,
\]
also (CTX.5).

## 4. B-freie Punkte und q-Reflexion

Für `x in (R,S)` setze `t=a-x`.

Falls
\[
x+d>S,
\qquad |x-d|<R,
\tag{CTX.6}
\]
sind beide `b`-Äste aus dem Annulus entfernt. Dann lauten die zwei relevanten ersten Blockgleichungen
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
\qquad D_t=1+\lambda 1_{t<\varepsilon}.
\]

Ist `t` nicht im Annulus, erzwingt (CTX.8) direkt `y(t)=0`, dann (CTX.7) `w(x)=0`.

Ist `t in (R,S)`, so gilt wegen `R>=E>epsilon`
\[
C_t=C_x=C=1+\lambda,\qquad D_t=D_x=1.
\]
Die vier Gleichungen für das Reflexionspaar `x <-> t=a-x` haben Matrix
\[
\begin{pmatrix}
C&0&-p&0\\
1&0&0&-q\\
0&C&0&-p\\
0&1&-q&0
\end{pmatrix}
\]
in den Variablen `(y(t),y(x),w(x),w(t))`. Ihre Determinante ist
\[
q^2C^2-p^2=-G\ne0.
\tag{CTX.9}
\]
Also stirbt jedes b-freie Reflexionsorbit.

## 5. Der einzige b-gekoppelte Keil

Falls `S<=R+d`, ist jeder Annuluspunkt b-frei, denn `x+d>S` und, da
\[
E>\frac d2
\iff \left(\frac54\right)^2>\frac32
\iff25>24,
\]
auch `|x-d|<R`. Dann ist Abschnitt 4 bereits vollständig.

Nehme nun
\[
S>R+d.
\tag{CTX.10}
\]
Definiere die drei offenen Schalen
\[
L:=(R,S-d),\qquad
H:=(R+d,S),\qquad
M:=(S-d,R+d).
\tag{CTX.11}
\]
Da
\[
S-R<a-E<2d
\]
(`2d-(a-E)=(2b-3a)+E>0`, und `2b-3a=\frac12\log(9/8)>0`), sind `L` und `H` disjunkt und `M` liegt dazwischen. Die Abbildung
\[
x\mapsto X:=x+d
\]
ist eine Bijektion `L -> H`.

### 5.1 Geometrie eines Low-High-Paars

Fixiere `x in L` und setze
\[
X:=x+d\in H,
\qquad t:=a-x,
\qquad h:=a-X=e-x.
\]
Aus `S>R+d`, `S<a`, `R>=E` und `2E>e` (äquivalent `75>64`) folgt
\[
t\in M\subset(R,S),
\qquad 0<h<R.
\tag{CTX.12}
\]
Außerdem sind für den Mittelwert `t` beide b-Äste außerhalb des Annulus; für `X` bleibt genau der rückwärtige b-Ast `w(X-d)=w(x)`.

Da `x,t,X` im Annulus liegen, sind ihre epsilon-Indikatoren null (`R>=E>epsilon`). Nur `h` kann `h<epsilon` oder `h>epsilon` erfüllen. Setze
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
Alle Faktoren in der Klammer sind strikt positiv und `G=p^2-q^2C^2>0`. Daher
\[
\det M_6<0.
\]
Somit verschwinden auf jedem Low-High-Orbit alle sechs Variablen.

### 5.2 Rest der Mittelschale

Für `z in M` sind beide b-Äste außerhalb/innerhalb des Annulus:
\[
z+d\ge S,
\]
und aus `R>d/2` sowie `S>R+d` folgt auch `|z-d|<R`.

Falls `a-z` außerhalb des Annulus liegt, greift die zweizeilige Elimination aus Abschnitt 4. Falls `a-z` im Annulus liegt und nicht in `L`, kann es nicht in `H` liegen: Das Reflexionsbild von `H` liegt wegen `e<2R` vollständig unterhalb `R`. Also liegt `a-z` ebenfalls in `M`, und der invertible Reflexionsblock (CTX.9) greift. Die Punkte in `a-L` sind bereits Bestandteil der sechsvariabligen Low-High-Orbits aus 5.1.

Damit ist der gesamte Annulus erschöpft.

## 6. Tiefer Zentralbereich

Für
\[
0<t<a-S
\]
liegt jeder Hubshift des Annulus außerhalb der Unterstützung, also
\[
(HE_Aw)(t)=0.
\]
Mit (CTX.3) folgt
\[
\bigl[1+\lambda(1+1_{t<\varepsilon})\bigr]y(t)=0,
\]
also `y(t)=0`. Zusammen mit den Orbits aus Abschnitt 4/5 wird damit ganz `(0,a-R)` getötet, und wegen Geradheit ganz `C_R^+`.

## 7. Theorem CTX-1 — erweiterte zentrale Transversalität

Für jedes
\[
\boxed{E\le R<S<a}
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

Dies subsumiert CT-1 (`a/2<=R<S<a`) und schiebt die zentrale Transversalitätsschwelle auf
\[
E=\frac12\log\frac54\approx0.111571775657105.
\]

## 8. Firewall

CTX-1 ist weiterhin nur ein Satz über Blockkernvektoren mit `y in C_R^+`. Nicht bewiesen sind:

- `ker K_{I,A}=0` für allgemeines `y in N_I`;
- voller Schur-Crossblock injektiv;
- bounded below / closed range / uniforme Winkel;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

Bei unabhängigem vollständigem GREEN wäre zulässig:

- **CTX-1:** `✓[M]_part` — der gesamte unendlichdimensionale zentrale Unsichtbarkeitssektor trägt für `E<=R<S<a` keinen augmentierten Schur-Kernvektor.

Keine Promotion ohne explizite Freigabe.