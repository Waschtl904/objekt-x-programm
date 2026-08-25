# P11/R32 — erste nichtzentrale Unsichtbarkeitsschale und vollständige Schalen-Transversalität

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
\boxed{\frac d2\le R<d,
\qquad R<S<a}
\tag{NS.1}
\]
und
\[
h:=d-R>0.
\]
Sei
\[
I=(-R,R),
\qquad \mathcal A=(-S,-R)\cup(R,S).
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
liegt und deren Profil um \(a\) symmetrisch ist:
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

### Beweis

Sei \(0<u<R\). Für den \(a\)-Kanal gilt:

- falls \(0<u<h\), liegen \(a-u,a+u\in J_R\) und (NS.2) gibt \(y(a-u)=y(a+u)\);
- falls \(h<u<R\), liegen beide Punkte außerhalb von \(J_R\).

Also verschwindet der \(a\)-Beitrag. Für den \(b\)-Kanal ist
\[
b-u>b-R=a+h,
\]
und für den \(T\)-Kanal
\[
T-u>T-R=(b-R)+e>a+h.
\]
Damit verschwinden auch diese Kanäle. Also \(Hy=0\) fast überall auf \((-R,R)\).

Der Raum \(\mathcal S_R^+\) ist unendlichdimensional: ein beliebiges \(L^2(0,h)\)-Profil kann um \(a\) gespiegelt und anschließend gerade fortgesetzt werden.

## 3. Rest-Supportlemma

### Lemma NS-1b

Für \(y\in\mathcal S_R^+\) gilt auf der positiven Achse
\[
\boxed{
\operatorname{ess\,supp}(Ay)
\subset
(a-h,a+h)
\cup
(a+2d-h,a+2d+h),
}
\tag{NS.4}
\]
wobei die zweite Schale am Horizont \(T_0\) abgeschnitten wird.

### Begründung aus SE-2

Im Drei-Shift-Fenster besitzt \(A\) nur die Full-Rest-Blöcke
\((2,0),(2,1),(3,0)\).

- Im \((2,0)\)-Block verschwindet der maskierte primitive \(k=1\)-Output zentral durch die Schalen-Symmetrie; seine äußeren Kopien liegen außerhalb der Maske. Der \(k=2\)-Term kann nach dem Rücktransport nur um \(\pm a\) und \(\pm3a\) landen, wobei \(3a>T_0\). Der \(k=3\)-Term ist nach der Maske null.
- Der \((2,1)\)-Block erzeugt ebenfalls keine positiven Zentren zwischen \(a\) und \(a+2d\); mögliche \(3a\)-Kopien liegen außerhalb des Horizonts.
- Der \((3,0)\)-Block transportiert die \(\pm a\)-Schalen zunächst auf \(\pm d\) und nach dem adjungierten \(b\)-Transport genau zurück auf \(\pm a\) bzw. auf \(\pm(a+2d)\).

Andere positive Supportzentren treten nicht auf. Insbesondere liegt die gesamte positive ursprüngliche Restschale oberhalb
\[
a-h=e+R,
\]
während die äußere positive Restschale erst bei
\[
a+2d-h=a+d+R=b+R
\]
beginnt.

## 4. Der saubere untere Auswertungspunkt

Fixiere \(x\in(R,S)\) und setze
\[
u:=a-x.
\]
Da \(S<a\), gilt \(u>0\). Außerdem
\[
u<a-R.
\]
Aus \(R\ge d/2\) folgt
\[
a-R\le e+R=a-h,
\]
weil dies äquivalent zu \(d\le2R\) ist. Also liegt \(u\) strikt unterhalb der positiven \(y\)-Schale. Nach Lemma NS-1b liegt dort auch kein positiver Rest-Support. Daher
\[
\boxed{y(a-x)=0,\qquad (Ay)(a-x)=0.}
\tag{NS.5}
\]

Für den Hubterm auf \(w\) gilt:

1. \(a\)-Kanal:
\[
D_{2a}E_Aw(a-x)
=w(-x)-w(2a-x)
=-w(x),
\]
weil \(2a-x>a>S\).

2. \(b\)-Kanal:
\[
(a-x)-b=-(x+d),
\]
also trägt genau \(-w(x+d)\) bei, falls \(x+d<S\); der andere Ast liegt rechts außerhalb des Annulus.

3. \(T=2a\)-Kanal: beide Argumente haben Betrag größer als \(a>S\), also kein Beitrag.

Damit lautet die erste Blockgleichung bei \(u=a-x\) exakt
\[
\boxed{
p\,w(x)+r\,1_{\{x+d<S\}}w(x+d)=0
\qquad\text{für fast jedes }x\in(R,S).
}
\tag{NS.6}
\]

Diese Gleichung enthält weder \(y\) noch \(A\).

## 5. Zwei-Schritt-d-Descent

Aus \(d>a/2\) folgt
\[
a<2d.
\]
Da \(R\ge d/2\) und \(S<a\), gilt daher
\[
S-R<a-R\le a-\frac d2<\frac32d<2d.
\tag{NS.7}
\]
Insbesondere ist die Annulusbreite strikt kleiner als \(2d\).

Teile den positiven Annulus in
\[
H:=(\max\{R,S-d\},S)
\]
und, falls nichtleer,
\[
L:=(R,S-d).
\]

Für \(x\in H\) ist \(x+d\ge S\), also reduziert (NS.6) zu
\[
pw(x)=0.
\]
Da \(p>0\), folgt
\[
w=0\quad\text{a.e. auf }H.
\tag{NS.8}
\]

Sei nun \(x\in L\). Dann \(X:=x+d\in(R,S)\). Wegen (NS.7) gilt
\[
X+d=x+2d>S,
\]
also liegt \(X\in H\). Nach (NS.8) ist \(w(X)=0\). Setzt man dies in (NS.6) bei \(x\) ein, folgt
\[
pw(x)=0.
\]
Also auch
\[
w=0\quad\text{a.e. auf }L.
\]
Somit
\[
\boxed{w=0\quad\text{auf dem ganzen Annulus}.}
\tag{NS.9}
\]

## 6. Theorem NS-1 — vollständige Transversalität der ersten nichtzentralen Schale

Unter (NS.1) gilt
\[
\boxed{
\ker\mathcal K_{I,A}
\cap
(\mathcal S_R^+\oplus\mathscr H_{\mathcal A}^-)
=\{0\}.
}
\tag{NS.10}
\]
Äquivalent
\[
\boxed{
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap
(I+A)\mathcal S_R^+
=\{0\}.
}
\tag{NS.11}
\]

### Beweis

Sei \((y,w)\) ein Blockkernpaar mit \(y\in\mathcal S_R^+\). Abschnitt 5 liefert \(w=0\). Die erste Blockgleichung wird damit
\[
(I+A)y=0.
\]
Da \(A=R_{T_0}^*R_{T_0}\ge0\), gilt \(I+A\ge I\), also \(y=0\). Damit folgt (NS.10).

## 7. Bedeutung

NS-1 behandelt **die gesamte erste nichtzentrale unendlichdimensionale Unsichtbarkeitsschale** für
\[
\boxed{\frac d2\le R<d,\qquad R<S<a.}
\]
Es bleibt für diese Schale kein \(S\)-Restkeil übrig.

Der Mechanismus ist deutlich einfacher als im zentralen CTX-Sektor: dort musste der Restterm aktiv mitgeführt werden; hier existiert mit \(u=a-x\) ein kompletter Outputkorridor, auf dem sowohl \(y\) als auch \(Ay\) verschwinden. Dadurch reduziert sich die Schur-Blockgleichung auf den zweistufigen \(d\)-Descent (NS.6).

## 8. Firewall und Kandidatenstatus

NS-1 betrifft ausschließlich Blockkernvektoren mit \(y\in\mathcal S_R^+\). Nicht bewiesen sind:

- voller \(\ker\mathcal K_{I,A}=0\);
- voller Schur-Crossblock injektiv;
- Klassifikation aller weiteren nichtzentralen Komponenten von \(\mathcal N_I\);
- Closed Range / bounded below / uniforme Winkel;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

Bei unabhängigem GREEN wäre erlaubt:

- **NS-1a:** `✓[M]` — erste nichtzentrale symmetrische Schale ist ein unendlichdimensionaler Unterraum von \(\mathcal N_I\) für \(d/2\le R<d\);
- **NS-1:** `✓[M]_part` — diese gesamte Schale ist für jedes \(R<S<a\) transversal.

Keine Promotion ohne explizite Freigabe.
