# P11/R32 — erste nichtzentrale Unsichtbarkeitsschale: reparierte Schur-Transversalität

**Status:** Kandidat; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Basis:** SE-1/SE-2/CI-1/CTX-1 Kandidatenkette.

> **Audit-Hinweis.** Eine frühere, noch unreviewte Zwischenfassung übersah die adjungierten Cross-Terme im `(2,0)`-Full-Rest-Block und behauptete deshalb fälschlich ein vollständiges Rest-Supportloch. Diese Fassung ist ersetzt. Der zentrale Cross-Term wird unten explizit mitgeführt; genau daraus entsteht eine reparierende `delta=d-e`-Rekursion.

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
\qquad e:=a-d=2a-b,
\qquad \delta:=d-e=2d-a,
\qquad \varepsilon:=T_0-T.
\]
Fixiere
\[
\boxed{\frac d2\le R<d,
\qquad R<S<a.}
\tag{NS.1}
\]
Setze
\[
h:=d-R>0,
\qquad I=(-R,R),
\qquad \mathcal A=(-S,-R)\cup(R,S).
\]

Der augmentierte SE-Block ist
\[
\mathcal K_{I,A}(y,w)
=\bigl((I+A)y+HE_{\mathcal A}w,\ E_I^*Hy\bigr),
\qquad A=R_{T_0}^*R_{T_0}.
\]

Wir verwenden die exakten Ungleichungen
\[
d>\frac a2\quad(9>8),
\qquad
e>\frac d2\quad(32>27),
\tag{NS.2}
\]
also insbesondere
\[
0<\delta=d-e<\frac d2\le R.
\tag{NS.3}
\]
Außerdem gilt im Drei-Shift-Fenster
\[
0<\varepsilon<E:=c-2a<e,
\tag{NS.4}
\]
weil `E<e` äquivalent zu `15<16` ist.

## 2. Erste nichtzentrale unsichtbare Schale

Definiere \(\mathcal S_R^+\) als den Raum aller geraden \(y\in L^2(-T_0,T_0)^+\), deren positiver Träger in
\[
J_R:=(a-h,a+h)=(e+R,b-R)
\]
liegt und deren Profil um \(a\) symmetrisch ist:
\[
\boxed{
y(a-s)=y(a+s)\quad\text{für fast jedes }|s|<h.
}
\tag{NS.5}
\]
Schreibe
\[
f(s):=y(a+s)=y(a-s),\qquad |s|<h.
\]

### Lemma NS-1a — Unsichtbarkeit

\[
\boxed{\mathcal S_R^+\subset\mathcal K_R:=\ker(E_I^*H|_+).}
\tag{NS.6}
\]

### Beweis

Für \(0<u<R\) heben sich die beiden \(a\)-Äste für \(u<h\) durch (NS.5) auf; für \(u>h\) liegen beide außerhalb der Schale. Der \(b\)-Ast beginnt erst bei
\[
b-R=a+h,
\]
und der \(T\)-Ast noch weiter außen. Also \(Hy=0\) auf \((-R,R)\). Der Raum ist unendlichdimensional, da ein beliebiges \(L^2(0,h)\)-Profil gespiegelt werden kann.

## 3. Exakte Full-Rest-Reduktion auf der Schale

Schreibe im `(2,0)`-Block
\[
\Phi_{20}=\alpha_1K_1+\alpha_2K_2+\alpha_3K_3,
\]
mit
\[
\alpha_1=2^{-3/4},
\quad \alpha_2=2^{-3/2},
\quad \alpha_3=2^{-9/4},
\]
und
\[
K_1=K_{\log2}^{tr},
\quad K_2=K_{2\log2}^{tr},
\quad K_3=K_{3\log2}^{tr}.
\]

Auf \(\mathcal S_R^+\) gilt nach der `Omega_(2,0)`-Maske exakt
\[
M_{20}K_1y=0,
\qquad
M_{20}K_3y=0.
\tag{NS.7}
\]
Beim `K1`-Term verschwindet der zentrale Output durch die Schalen-Symmetrie; die äußeren Kopien beginnen bei `2a-h>a+epsilon`. Beim `K3`-Term liegt bereits die nächste Kopie jenseits derselben Maske. Somit
\[
M_{20}\Phi_{20}y
=\alpha_2M_{20}K_2y.
\tag{NS.8}
\]

**Wichtig:** Beim Rücktransport bleiben trotzdem alle drei Adjungiertenanteile
\[
\alpha_1K_1^*,\quad\alpha_2K_2^*,\quad\alpha_3K_3^*
\]
in `Phi_20^*` erhalten. Der `K1^* M K2`-Cross-Term erzeugt den zentralen Echo unten.

Der `(2,1)`-Block verschwindet auf dieser Schale vollständig, weil sein `K2`-Output um `+-a` liegt, während die Maske nur `|u|<epsilon<e<a-h` sieht. Der `(3,0)`-Block trägt lokal auf der `a`-Schale, aber nicht zum zentralen Echo bei.

## 4. Zentraler Cross-Term-Echo

Setze
\[
\gamma:=(\log2)2^{-9/4}>0.
\]
Für fast jedes
\[
0<t<h
\]
gilt exakt
\[
\boxed{
(Ay)(t)=\gamma_t f(t),
\qquad
\gamma_t:=\gamma\bigl(1+1_{\{t<\varepsilon\}}\bigr)>0.
}
\tag{NS.9}
\]

### Rechnung

Sei `g=M20 K2 y`. Für `0<t<h` gilt
\[
g(-a+t)=-f(t),
\qquad
g(a+t)=1_{\{t<\varepsilon\}}f(t).
\]
Da `K1^*=-K1`, erhält der zentrale Punkt nur aus dem Cross-Term `K1^* M20 K2` den Beitrag
\[
(\log2)\alpha_1\alpha_2
\bigl(1+1_{\{t<\varepsilon\}}\bigr)f(t),
\]
und `alpha_1 alpha_2=2^{-9/4}`. Andere Full-Rest-Blöcke besitzen dort keinen Support.

## 5. Lokale Wirkung auf dem zugehörigen Schalenpunkt

Für denselben \(0<t<h\) gilt am Punkt \(a+t\)
\[
\boxed{
((I+A)y)(a+t)=C_t f(t),
}
\tag{NS.10}
\]
mit
\[
\boxed{
C_t:=1+q^2+2r^2\,1_{\{t\ge\delta-\varepsilon\}}>0.
}
\tag{NS.11}
\]

Der `q^2`-Term ist der lokale `(2,0), k=2`-Selbstterm. Der `(2,1)`-Block ist null. Der `(3,0)`-Selbstterm trägt genau dann, wenn die `Omega_(3,0)`-Maske den rückwärtigen `b`-Output enthält, also bei `t>=delta-epsilon`.

## 6. Sauberer Bereich x <= R+e

Fixiere \(x\in(R,S)\) und setze
\[
t:=a-x.
\]
Falls
\[
x\le R+e,
\tag{NS.12}
\]
gilt
\[
t\ge a-(R+e)=d-R=h.
\]
Damit liegt `u=t` außerhalb des zentralen Echos und unterhalb der ursprünglichen Schale. Also
\[
y(t)=(Ay)(t)=0.
\]
Die erste Blockgleichung bei `u=a-x` lautet deshalb exakt
\[
\boxed{
pw(x)+r\,1_{\{x+d<S\}}w(x+d)=0.}
\tag{NS.13}
\]
Der `T`-Hubkanal liegt dort vollständig außerhalb des Annulus.

## 7. Echo-Bereich x > R+e

Nehme nun
\[
x>R+e.
\tag{NS.14}
\]
Dann
\[
0<t=a-x<h.
\]
Außerdem
\[
x+d>R+e+d=R+a>S,
\]
also ist im zentralen Hubwert kein `w(x+d)` mehr aktiv. Mit (NS.9) gibt die Blockgleichung bei `u=t`
\[
\boxed{
\gamma_t f(t)-p w(x)=0.
}
\tag{NS.15}
\]

Betrachte anschließend den zugehörigen Schalenpunkt
\[
a+t=T-x.
\]
Dort liegen der `a`-Hubast im inneren Loch und die rechten Äste außerhalb. Weil `x>R+e`, gilt
\[
x-e>R,
\]
und `x-e<S`. Daher lautet die Blockgleichung mit (NS.10)
\[
\boxed{
C_t f(t)-r w(x-e)-q w(x)=0.
}
\tag{NS.16}
\]

Elimination von `f(t)` ergibt
\[
\boxed{
A_t w(x)-r w(x-e)=0,
\qquad
A_t:=\frac{C_t p}{\gamma_t}-q.
}
\tag{NS.17}
\]

### Positivität von A_t

Es gilt `C_t>=1` und `gamma_t<=2 gamma`. Daher
\[
A_t\ge\frac{p}{2\gamma}-q.
\]
Mit
\[
\frac{p}{2\gamma}=\sqrt{\frac2{\log2}}>\sqrt2,
\qquad q<1,
\]
folgt
\[
\boxed{A_t>0.}
\tag{NS.18}
\]

## 8. Die delta-Rekursion

Setze
\[
z:=x-e.
\]
Aus (NS.14) folgt `z>R`. Ferner
\[
z<x<S<a
\quad\Longrightarrow\quad
z<d.
\]
Wegen `R>=d/2>delta` gilt
\[
d<R+e,
\]
also liegt `z` im sauberen Bereich (NS.12). Gleichung (NS.13) bei `z` lautet
\[
pw(z)+r\,1_{\{z+d<S\}}w(z+d)=0.
\]
Aber
\[
z+d=x+(d-e)=x+\delta.
\]
Mit (NS.17) folgt daher:

- falls `x+delta>=S`, dann `w(z)=0` und wegen `A_t>0` auch `w(x)=0`;
- falls `x+delta<S`, dann
  \[
  \boxed{
  B_t w(x)+r w(x+\delta)=0,
  \qquad B_t:=\frac{pA_t}{r}>0.
  }
  \tag{NS.19}
  \]

Dies ist eine strikt aufwärts gerichtete `delta`-Rekursion im Echo-Bereich.

## 9. Endliche delta-Streifen-Elimination

Der Echo-Bereich ist
\[
E_R:=(R+e,S).
\]
Partitioniere ihn in endlich viele Streifen
\[
E_n:=E_R\cap(S-(n+1)\delta,S-n\delta),
\qquad n=0,1,\dots,N.
\]

Auf `E_0` gilt `x+delta>=S`, also `w=0`. Induktiv: ist `w` auf `E_0\cup\dots\cup E_{n-1}` null, so liegt für `x in E_n` der Punkt `x+delta` entweder außerhalb des Annulus oder in einem bereits getöteten höheren Streifen. (NS.19) und `B_t>0` geben dann `w(x)=0`.

Somit
\[
\boxed{w=0\quad\text{auf }E_R.}
\tag{NS.20}
\]

## 10. Rückkehr zum sauberen Bereich

Sei nun `x in (R,min(S,R+e))`. Aus (NS.13):

- wenn `x+d>=S`, folgt direkt `w(x)=0`;
- wenn `x+d<S`, dann wegen `d>e`
  \[
  x+d>R+d>R+e,
  \]
  also liegt `x+d` im bereits getöteten Echo-Bereich. Wieder folgt `w(x)=0`.

Daher
\[
\boxed{w=0\quad\text{auf dem ganzen Annulus}.}
\tag{NS.21}
\]

## 11. Theorem NS-1 — vollständige Transversalität der ersten nichtzentralen Schale

Unter (NS.1) gilt
\[
\boxed{
\ker\mathcal K_{I,A}
\cap
(\mathcal S_R^+\oplus\mathscr H_{\mathcal A}^-)
=\{0\}.
}
\tag{NS.22}
\]
Äquivalent
\[
\boxed{
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap
(I+A)\mathcal S_R^+
=\{0\}.
}
\tag{NS.23}
\]

Denn nach (NS.21) ist `w=0`; dann liefert `(I+A)y=0` und `A>=0` sofort `y=0`.

## 12. Bedeutung und Firewall

Der zentrale CTX-Sektor und die erste nichtzentrale Schale werden durch zwei verschiedene Mechanismen geschlossen:

- CTX: endliche `4x4/6x6`-Orbits;
- NS-1: ein **Full-Rest-Cross-Term erzeugt einen zentralen Echo**, der zusammen mit dem sauberen `d`-Schritt exakt die P12-Skala
  \[
  \delta=d-e
  \]
  erzeugt und eine endliche `delta`-Streifen-Elimination erlaubt.

Dies ist strukturell relevant, aber weiterhin nur ein partieller Schur-Transversalitätssatz.

Nicht bewiesen sind:

- voller `ker K_{I,A}=0`;
- voller Schur-Crossblock injektiv;
- Klassifikation sämtlicher weiterer Teile von `K_R`;
- Closed Range / bounded below / uniforme Winkel;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

Bei unabhängigem GREEN wäre erlaubt:

- **NS-1a:** `✓[M]` — erste nichtzentrale symmetrische Schale ist ein unendlichdimensionaler Unterraum von `K_R` für `d/2<=R<d`;
- **NS-1:** `✓[M]_part` — diese gesamte Schale ist für jedes `R<S<a` transversal.

Keine Promotion ohne explizite Freigabe.