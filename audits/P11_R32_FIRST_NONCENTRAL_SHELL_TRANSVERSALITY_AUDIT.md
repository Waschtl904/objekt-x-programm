# P11/R32 — erste nichtzentrale Unsichtbarkeitsschale und Schur-Transversalität

**Status:** Kandidat; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Basis:** SE-1/SE-2/CI-1/CTX-1 Kandidatenkette.

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
d:=b-a,
\qquad e:=a-d=2a-b.
\]
Fixiere
\[
\boxed{\frac d2\le R<d}
\tag{NS.1}
\]
und
\[
h:=d-R>0.
\]
Sei
\[
I=(-R,R),
\qquad \mathcal A=(-S,-R)\cup(R,S),
\qquad R<S<a.
\]

Der augmentierte SE-Block ist
\[
\mathcal K_{I,A}(y,w)
=\bigl((I+A)y+HE_{\mathcal A}w,\ E_I^*Hy\bigr),
\qquad A=R_{T_0}^*R_{T_0}.
\]

## 2. Die erste nichtzentrale unsichtbare Schale

Definiere \(\mathcal S_R^+\) als den Raum aller geraden \(y\in L^2(-T_0,T_0)^+\), deren positiver Träger in
\[
J_R:=(a-h,a+h)=(e+R,b-R)
\]
liegt und deren positives Profil um \(a\) symmetrisch ist:
\[
\boxed{
y(a-s)=y(a+s)\quad\text{für fast jedes }|s|<h.
}
\tag{NS.2}
\]
Wegen Geradheit liegt der volle Träger in \(J_R\cup(-J_R)\).

### Lemma NS-1a — Unsichtbarkeit

\[
\boxed{\mathcal S_R^+\subset\mathcal N_I:=\ker(E_I^*H|_+).}
\tag{NS.3}
\]

#### Beweis

Sei \(0<u<R\). Für den \(a\)-Kanal gilt:

- falls \(0<u<h\), liegen \(a-u,a+u\in J_R\) und (NS.2) gibt
  \(y(a-u)=y(a+u)\);
- falls \(h<u<R\), liegen beide Punkte außerhalb von \(J_R\), denn
  \(a-u<a-h\) und \(a+u>a+h\).

Also verschwindet der \(a\)-Beitrag auf \(I\).

Für den \(b\)-Kanal ist
\[
b-u>b-R=a+h,
\]
und der andere Ast liegt noch weiter außen. Für den \(T\)-Kanal ist
\[
T-u>T-R=(b-R)+e>a+h.
\]
Damit verschwinden auch diese beiden Kanäle. Also \(Hy=0\) fast überall auf \((-R,R)\).

Der Raum \(\mathcal S_R^+\) ist unendlichdimensional: ein beliebiges \(L^2(0,h)\)-Profil kann durch Spiegelung um \(a\) und anschließend durch Geradheit fortgesetzt werden.

## 3. Rest-Supportlemma für die Schale

### Lemma NS-1b — wo \(Ay\) liegen kann

Für \(y\in\mathcal S_R^+\) gilt auf der positiven Achse:
\[
\operatorname{ess\,supp}(Ay)
\subset
(a-h,a+h)
\cup
(a+2d-h,a+2d+h),
\tag{NS.4}
\]
wobei die zweite Schale zusätzlich am Horizont \(T_0\) abgeschnitten wird.
Insbesondere beginnt die äußere positive Restschale erst bei
\[
a+2d-h=a+d+R=b+R=a+(d+R).
\tag{NS.5}
\]

#### Beweis aus SE-2

Im Drei-Shift-Fenster besitzt \(A\) nur die Full-Rest-Blöcke
\((2,0),(2,1),(3,0)\).

1. Im \((2,0)\)-Block verschwindet der primitive \(k=1\)-Term nach der \(\Omega_{2,0}\)-Maske: sein zentraler Output hebt sich wegen (NS.2) exakt auf, während seine äußeren Outputs um \(\pm2a\) außerhalb der Maske liegen. Der \(k=2\)-Term kann nach Rücktransport nur auf die ursprünglichen Schalen um \(\pm a\) und auf Schalen um \(\pm3a\) zurückwirken; \(3a>T_0\), also bleiben nur die ursprünglichen Schalen. Der \(k=3\)-Term ist nach der Maske null.

2. Der \((2,1)\)-Block enthält nur den \(k=2\)-Term. Sein maskierter Output liegt um \(\pm a\); nach Adjungiertentransport entstehen wieder nur \(\pm a\) bzw. \(\pm3a\), und die letzteren liegen außerhalb des Horizonts. (Je nach Parameter kann der gesamte Block bereits vorher verschwinden; für (NS.4) genügt die Supportaussage.)

3. Der \((3,0)\)-Block transportiert die Schalen um \(\pm a\) zunächst auf Schalen um \(\pm d\). Nach dem adjungierten \(b\)-Transport entstehen genau die ursprünglichen Schalen um \(\pm a\) sowie äußere Schalen um
\[
\pm(a+2d).
\]

Andere positive Supportzentren treten nicht auf. Dies ergibt (NS.4). Die linke Kante der äußeren positiven Schale ist
\[
a+2d-h=a+2d-(d-R)=a+d+R=b+R,
\]
also (NS.5).

## 4. Theorem NS-1 — erste nichtzentrale Schale transversal für S <= R+d

Zusätzlich zu (NS.1) gelte
\[
\boxed{R<S<a,\qquad S\le R+d.}
\tag{NS.6}
\]
Dann
\[
\boxed{
\ker\mathcal K_{I,A}
\cap
(\mathcal S_R^+\oplus\mathscr H_{\mathcal A}^-)
=\{0\}.
}
\tag{NS.7}
\]
Äquivalent
\[
\boxed{
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap
(I+A)\mathcal S_R^+
=\{0\}.
}
\tag{NS.8}
\]

### Beweis

Sei \((y,w)\) ein Blockkernpaar mit \(y\in\mathcal S_R^+\).

Fixiere fast jedes \(x\in(R,S)\) und betrachte den positiven Punkt
\[
u=a+x.
\]
Da \(x>R\ge d/2\), gilt
\[
h=d-R\le R<x.
\]
Somit liegt \(u=a+x\) oberhalb der ursprünglichen positiven \(y\)-Schale, also \(y(u)=0\).

Nach Lemma NS-1b beginnt die einzige mögliche äußere positive \(Ay\)-Schale erst bei Offset \(d+R\) von \(a\). Wegen
\[
x<S\le R+d
\]
liegt \(u=a+x\) strikt darunter. Daher
\[
(Ay)(a+x)=0.
\tag{NS.9}
\]

Nun berechnen wir den Hubterm auf \(w\). Der \(a\)-Ast liefert
\[
D_{2a}E_Aw(a+x)=w(x),
\]
da der zweite Ast bei \(2a+x>S\) liegt.

Für den \(b\)-Ast ist der rückwärtige Punkt \(x-d\). Aus \(R\ge d/2\) und \(x<R+d\) folgt
\[
|x-d|<R,
\]
also liegt dieser Punkt im inneren Loch des Annulus; der andere \(b\)-Ast liegt rechts außerhalb. Somit trägt der \(b\)-Kanal nichts bei.

Für den \(T=2a\)-Ast ist
\[
(a+x)-T=x-a<0.
\]
Wegen Ungeradheit von \(w\) ergibt dieser Ast
\[
-q\,1_{(R,S)}(a-x)\,w(a-x).
\]
Der zweite \(T\)-Ast liegt rechts außerhalb.

Die erste Blockgleichung bei \(u=a+x\) lautet daher exakt
\[
\boxed{
pw(x)-q\,1_{(R,S)}(a-x)w(a-x)=0.}
\tag{NS.10}
\]

Falls \(a-x\notin(R,S)\), folgt sofort \(w(x)=0\).

Falls \(x':=a-x\in(R,S)\), darf dieselbe Gleichung auf \(x'\) angewendet werden. Da \(a-x'=x\), erhalten wir
\[
pw(x)-qw(x')=0,
\qquad
pw(x')-qw(x)=0.
\tag{NS.11}
\]
Die Koeffizientenmatrix ist
\[
\begin{pmatrix}p&-q\\-q&p\end{pmatrix}
\]
mit
\[
\det=p^2-q^2
=(\log2)\left(2^{-3/2}-2^{-3}\right)>0.
\tag{NS.12}
\]
Also \(w(x)=w(x')=0\).

Damit verschwindet \(w\) fast überall auf \((R,S)\), also wegen Ungeradheit auf dem ganzen Annulus. Die erste Blockgleichung reduziert sich zu
\[
(I+A)y=0.
\]
Da \(A=R_{T_0}^*R_{T_0}\ge0\), ist \(I+A\ge I\) injektiv, also \(y=0\).
Dies beweist (NS.7).

## 5. Wichtige Reichweite

Da
\[
e=a-d,
\]
gilt für jedes \(R\ge e\)
\[
R+d\ge a.
\]
Folglich ist (NS.6) für jedes \(S<a\) automatisch erfüllt. Daher:
\[
\boxed{
e\le R<d,\quad R<S<a
\Longrightarrow
\text{NS-1 gilt für die gesamte erste nichtzentrale Schale}.}
\tag{NS.13}
\]

Der einzige durch NS-1 noch nicht behandelte Teil dieser ersten Schale ist damit der kleine Keil
\[
\boxed{
\frac d2\le R<e,
\qquad R+d<S<a.
}
\tag{NS.14}
\]

## 6. Strukturelle Beobachtung für den Restkeil

Im Restkeil (NS.14) wird am High-Teil des Annulus gleichzeitig

- der rückwärtige \(b\)-Ast \(w(x-d)\), und
- die äußere \((3,0)\)-Restschale von \(Ay\)

aktiv. Die natürliche Shell-Symmetrie induziert auf der Annuluskoordinate die Reflexion
\[
J_d(x)=2d-x,
\]
während der \(q\)-Ast an \(u=a+x\) die Reflexion
\[
J_a(x)=a-x
\]
induziert. Ihre Komposition ist die Translation
\[
\boxed{
J_d\circ J_a(x)=x+(2d-a)=x+\delta,
\qquad \delta:=2d-a=d-e.
}
\tag{NS.15}
\]
Damit entsteht im Restkeil exakt dieselbe kleine Längenskala \(\delta\), die bereits im P12-Low-Radius-Programm die Orbit-/Kammerstruktur steuert. Dies ist eine Strukturbeobachtung, noch kein Injektivitätssatz für (NS.14).

## 7. Firewall und Kandidatenstatus

NS-1 betrifft ausschließlich Blockkernvektoren mit \(y\in\mathcal S_R^+\). Nicht bewiesen sind:

- voller \(\ker\mathcal K_{I,A}=0\);
- voller Schur-Crossblock injektiv;
- Behandlung des Restkeils (NS.14);
- Closed Range / bounded below / uniforme Winkel;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

Bei unabhängigem GREEN wäre erlaubt:

- **NS-1a:** `✓[M]` — erste nichtzentrale symmetrische Schale ist ein unendlichdimensionaler Unterraum von \(\mathcal N_I\) für \(d/2\le R<d\);
- **NS-1:** `✓[M]_part` — diese gesamte Schale ist für \(S\le R+d\) transversal; insbesondere für \(e\le R<d\) und jedes \(R<S<a\).

Keine Promotion ohne explizite Freigabe.
