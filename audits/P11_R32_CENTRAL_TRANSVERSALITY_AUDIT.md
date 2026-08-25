# P11/R32 — zentrale Schur-Transversalität im Fenster a/2 <= R < S < a

**Status:** Kandidat; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Voraussetzung:** Drei-Shift-Fenster
\[
2a<T_0<c:=\frac12\log5,
\qquad a=\frac12\log2,
\quad b=\frac12\log3,
\quad T=2a.
\]

Dieser Audit verstärkt den zentralen Unsichtbarkeitsbefund: obwohl der innere Unsichtbarkeitsraum für `R<a` einen unendlichdimensionalen Zentralraum enthält, kann dieser Zentralraum in einem konkreten offenen Parametersektor **nicht** die Quelle eines Schur-Annihilators sein.

## 1. Parametersektor und Zentralraum

Fixiere
\[
\boxed{\frac a2\le R<S<a.}
\tag{CT.1}
\]
Setze
\[
d_R:=a-R\le\frac a2
\]
und
\[
\mathcal C_R^+
:=\{y\in L^2(-T_0,T_0)^+:
\operatorname{ess\,supp}y\subset[-d_R,d_R]\}.
\]

Sei
\[
I=(-R,R),
\qquad
\mathcal A=(-S,-R)\cup(R,S).
\]
Der augmentierte SE-Block ist
\[
\mathcal K_{I,A}(y,w)
=\bigl((I+A)y+HE_{\mathcal A}w,\ E_I^*Hy\bigr),
\qquad A=R_{T_0}^*R_{T_0}.
\]
Für `y in C_R^+` ist die zweite Gleichung automatisch erfüllt (CI-1). Entscheidend ist daher die erste Gleichung.

## 2. Lemma CT-1a — Restkollaps auf dem Zentralraum

Schreibe
\[
K:=K_{\log2}^{\rm tr}=P_{T_0}D_{\log2}E_{T_0},
\qquad
\lambda:=(\log2)2^{-3/2}>0,
\]
und
\[
M_{20}:=1_{\Omega_{2,0,T_0}}.
\]
Dann gilt auf `C_R^+` exakt
\[
\boxed{
Ay=\lambda K^*M_{20}Ky.
}
\tag{CT.2}
\]

### Beweis

Aus der Full-Rest-Zerlegung bestehen im Drei-Shift-Fenster nur die Blöcke `(2,0),(2,1),(3,0)`.

Auf `Omega_(2,0)` gilt
\[
|u|<T_0-a<c-a.
\]
Für den `k=2`-Shift mit Halbshift `T=2a` folgt
\[
|u\pm T|>3a-c>\frac a2\ge d_R,
\]
weil
\[
3a-c>\frac a2
\iff 5a>2c
\iff 2^5>5^2.
\]
Der `k=3`-Shift liegt noch weiter außen. Somit verschwinden auf `C_R^+` die `k=2,3`-Anteile von `Phi_(2,0)` nach Multiplikation mit `M_(2,0)`.

Auf `Omega_(2,1)` gilt `|u|<T0-2a<c-2a`; der einzige effektive `k=2`-Term erfüllt
\[
|u\pm2a|>4a-c>\frac a2\ge d_R,
\]
also verschwindet der ganze `(2,1)`-Block.

Auf `Omega_(3,0)` gilt `|u|<T0-b<c-b`; für den `k=1`-Halbshift `b` gilt
\[
|u\pm b|>2b-c>\frac a2\ge d_R,
\]
weil
\[
2b-c>\frac a2
\iff 81>50.
\]
Also verschwindet auch der `(3,0)`-Block.

Im `(2,0)`-Block bleibt nur
\[
\Phi_{2,0}=2^{-3/4}K
\]
übrig. Mit dem Blockvorfaktor `log 2` folgt (CT.2).

## 3. Lemma CT-1b — exakte primitive Wirkung

Setze
\[
\varepsilon:=T_0-T>0.
\]
Für `y in C_R^+` und fast jedes `0<t<d_R` gilt
\[
\boxed{
(Ay)(t)
=\lambda\bigl(1+1_{(0,\varepsilon)}(t)\bigr)y(t).
}
\tag{CT.3}
\]

Für jedes `x in (R,S)` und `t=a-x in (a-S,a-R)` gilt außerdem
\[
\boxed{
(Ay)(a+x)=-\lambda y(t).
}
\tag{CT.4}
\]

### Beweis

Setze `g=M20 K y`. Da `y` gerade und in `[-d_R,d_R]` getragen ist, liegt `Ky` auf den beiden Schalen um `+-a`.

Für `0<t<d_R`:
\[
g(t-a)=-y(t),
\]
weil `|t-a|=a-t<T0-a`, während
\[
g(t+a)=1_{t<\varepsilon}y(t)
\]
wegen der oberen Maskengrenze `a+t<T0-a iff t<epsilon`.
Da `K^*=-K`, ergibt sich (CT.3).

Für `x in (R,S)` und `t=a-x`, ist `x<a<T0-a`, also
\[
g(x)=y(t).
\]
Der zweite Wert in `K g` bei `a+x` liegt außerhalb der `+-a`-Schalen. Daher folgt (CT.4).

## 4. Lemma CT-1c — isolierte Hubwerte

Unter (CT.1) gilt für jedes `x in (R,S)` und `t=a-x`:
\[
\boxed{
(HE_Aw)(t)=-p\,w(x),
\qquad
(HE_Aw)(a+x)=+p\,w(x).
}
\tag{CT.5}
\]

Außerdem
\[
\boxed{
(HE_Aw)(t)=0
\quad\text{für }0<t<a-S.
}
\tag{CT.6}
\]

### Beweis der Branch-Isolation

Für `t=a-x` liefert der `a`-Shift die Argumente `-x` und `T-x`; wegen `S<a` liegt `T-x>S`, also bleibt nur `-w(x)`.

Für den `b`-Shift ist
\[
|t-b|=x+(b-a)>R+(b-a)>S,
\]
weil `R>=a/2`, `b-a>a/2` (äquivalent `9>8`) und `S<a`. Der andere `b`-Ast liegt noch weiter rechts. Die `T`-Äste liegen ebenfalls außerhalb des Annulus.

Bei `a+x` liefert der `a`-Shift `w(x)`. Für den `b`-Ast ist
\[
|(a+x)-b|=|x-(b-a)|<R,
\]
weil `2R>=a>b-a` und `S-(b-a)<a-(b-a)<a/2<=R`; der zweite `b`-Ast ist rechts außerhalb. Für den `T`-Ast gilt
\[
|(a+x)-T|=a-x< a-R\le R,
\]
und der andere Ast liegt rechts außerhalb. Damit bleibt nur `+p w(x)`.

Für `0<t<a-S` liegen schon die nächsten `a`-Shiftargumente außerhalb `(R,S)`; die `b`- und `T`-Argumente liegen noch weiter weg. Das ergibt (CT.6).

## 5. Theorem CT-1 — zentraler Transversalitätssatz

Im Parametersektor (CT.1) gilt
\[
\boxed{
\ker\mathcal K_{I,A}
\cap
(\mathcal C_R^+\oplus\mathscr H_A^-)
=\{0\}.
}
\tag{CT.7}
\]
Äquivalent:
\[
\boxed{
\operatorname{Ran}(HE_A|_-)
\cap
(I+A)\mathcal C_R^+
=\{0\}.
}
\tag{CT.8}
\]

### Beweis

Sei `(y,w)` ein Blockkernpaar mit `y in C_R^+`.

Zuerst sei `0<t<a-S`. Nach (CT.6) und (CT.3) reduziert die erste Blockgleichung auf
\[
\bigl[1+\lambda(1+1_{t<\varepsilon})\bigr]y(t)=0.
\]
Der Koeffizient ist strikt positiv, also
\[
y(t)=0
\quad(0<t<a-S).
\tag{CT.9}
\]

Nun sei `x in (R,S)` und `t=a-x in (a-S,a-R)`. Die erste Blockgleichung bei `u=t` gibt mit (CT.3),(CT.5)
\[
\bigl[1+\lambda(1+1_{t<\varepsilon})\bigr]y(t)-p w(x)=0.
\tag{CT.10}
\]
Bei `u=a+x` ist `y(a+x)=0`, und (CT.4),(CT.5) geben
\[
-\lambda y(t)+p w(x)=0.
\tag{CT.11}
\]
Elimination von `p w(x)` ergibt
\[
\bigl[1+\lambda 1_{t<\varepsilon}\bigr]y(t)=0.
\]
Wieder ist der Koeffizient strikt positiv, also `y(t)=0` und dann `w(x)=0`.

Wenn `x` durch `(R,S)` läuft, läuft `t=a-x` durch `(a-S,a-R)`. Zusammen mit (CT.9) folgt `y=0` fast überall auf `(0,a-R)`, also wegen Geradheit `y=0` auf ganz `C_R^+`. Gleichung (CT.11) liefert `w=0` fast überall auf `(R,S)`, und wegen Ungeradheit auf dem ganzen Annulus.

Damit folgt (CT.7); (CT.8) ist dieselbe Aussage nach Vorzeichenwechsel `w -> -w`.

## 6. Scope

CT-1 ist ein echter partieller Satz über die **wahre post-P12 SE-Transversalität**, aber nur für Blockkernvektoren, deren gerade Komponente `y` im zentralen Unsichtbarkeitsraum `C_R^+` liegt.

Nicht bewiesen sind:
- `ker K_{I,A}=0` ohne die Zusatzannahme `y in C_R^+`;
- `ker(E_I^* Sigma E_A)=0` im ganzen Parametersektor;
- irgendeine uniforme Winkel-/Coercivity-Schranke;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

Bei unabhängigem GREEN wäre erlaubt:

- **CT-1:** `✓[M]_part` — der gesamte unendlichdimensionale zentrale Unsichtbarkeitssektor kann für `a/2 <= R < S < a` keinen augmentierten Schur-Kernvektor tragen.
