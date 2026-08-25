# P11/R32 — ST-1 lokaler 11-Wort- und Hub-Gegencheck

**Status:** Kandidat; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Ziel:** die beiden von der unabhängigen Prüfung markierten Restunsicherheiten in ST-1 explizit schließen: (i) vollständige lokale 11-Wort-Bilanz an `x1=e-u` und `x2=a-u`; (ii) vollständige Hub-Ast-Isolation an denselben Punkten.

## 1. Setup und rechte maskierte Kanäle

Wir arbeiten im ST-1-Sektor
\[
\frac d2\le R<e,\qquad R<S<a,
\]
mit
\[
\ell=e-R,\qquad 0<u<\ell,
\]
und der zweiten Schale
\[
y=U_Rf,
\qquad y(b+u)=f(u),
\qquad y(T-u)=\rho f(u),
\qquad \rho=r/q.
\]

Im `(2,0)`-Block schreibe
\[
W_{jk}=K_j^*M_{20}K_k,\qquad j,k\in\{1,2,3\},
\]
mit Halbverschiebungen
\[
K_1:\ a,\qquad K_2:\ T=2a,\qquad K_3:\ 3a.
\]
Setze
\[
g_k:=M_{20}K_ky.
\]
Da `y` gerade ist, sind die `g_k` ungerade. Auf der positiven Achse lauten ihre vollständigen relevanten Profilkanäle:

\[
\begin{array}{c|c|c}
\text{Kanal}&\text{Punkt}&\text{Wert}\\\hline
 g_1&d+u&-f(u)\\
 g_1&a-u&-\rho f(u)\\\hline
 g_2&u&\rho f(u)\\
 g_2&e-u&f(u)\\\hline
 g_3&a+u&\rho f(u)\,1_{\{u<\varepsilon\}}\\
 g_3&a+e-u&f(u)\,1_{\{u>e-\varepsilon\}}
\end{array}
\tag{LL.1}
\]

Ferner
\[
K_j^*=-K_j,
\]
also für einen ungeraden maskierten Output `g`
\[
(K_j^*g)(x)=-g(x-ja)+g(x+ja).
\tag{LL.2}
\]
Dies erlaubt eine vollständige lokale Wortbilanz ohne bloße Endformelannahme.

## 2. Vollständiges 11-Wort-Ledger bei x1=e-u

Setze
\[
x_1=e-u\in(R,e).
\]

### Zeile j=1

Es gilt
\[
x_1-a=-(d+u),
\qquad
x_1+a=a+e-u.
\tag{LL.3}
\]
Daher:

- `W11`: `g1(d+u)=-f(u)` ist aktiv; `g1(a+e-u)=0`. Also
  \[
  W_{11}y(x_1)=-f(u).
  \]
  Mit Gewicht `(log2) alpha1^2=p^2` ergibt dies `-p^2 f(u)`.

- `W12`: weder `g2(d+u)` noch `g2(a+e-u)` liegt in den `g2`-Kanälen `(0,ell)` bzw. `(R,e)`. Also `W12=0` an `x1`.

- `W13`: `g3(d+u)=0`; dagegen ist
  \[
  g_3(a+e-u)=f(u)1_{\{u>e-\varepsilon\}}.
  \]
  Also
  \[
  W_{13}y(x_1)=f(u)1_{\{u>e-\varepsilon\}}.
  \]
  Mit Gewicht
  \[
  (\log2)\alpha_1\alpha_3=(\log2)2^{-3}=q^2
  \]
  ergibt dies den positiven Zusatz `+q^2 1_{u>e-epsilon} f(u)`.

### Zeile j=2

Es gilt
\[
x_1-T=-(b+u),
\qquad
x_1+T=T+e-u.
\tag{LL.4}
\]
Beide Beträge liegen außerhalb sämtlicher in (LL.1) auftretender Kanäle; insbesondere ist `b>a` und `T+e-u>T`. Also
\[
W_{21}=W_{22}=W_{23}=0
\]
an `x1`.

### Zeile j=3

Es gilt
\[
x_1-3a<-(3a-e),
\qquad
x_1+3a>3a.
\]
Die maskierten `g_k` liegen in `|x|<a+epsilon`, während
\[
3a-e= a+b > a+\varepsilon
\]
wegen `epsilon<E<b`. Daher
\[
W_{31}=W_{32}=W_{33}=0
\]
an `x1`.

### (2,1)-Selbstterm

Der `(2,1)`-Term ist `K_2^*M_{21}K_2`. Sein maskierter rechter Output liegt in `|x|<epsilon`. Die Rücktransportpunkte sind erneut `-(b+u)` und `T+e-u`, beide mit Betrag `>epsilon`. Also ist der `(2,1)`-Selbstterm an `x1` null.

### (3,0)-Selbstterm

Mit Halbverschiebung `b` sind die beiden Rücktransportpunkte
\[
x_1-b=-(2d+u),
\qquad
x_1+b=T-u.
\tag{LL.5}
\]
Der maskierte `(3,0)`-Output der zweiten Schale liegt nur in den zentralen Profilintervallen `(0,ell)` und `(R,e)` (plus ungerade Spiegelung). Wegen
\[
2d+u>2d>a>e,
\qquad
T-u>T-\ell=b+R>e,
\]
trifft keiner der beiden Punkte diesen Support. Also ist auch der `(3,0)`-Selbstterm an `x1` null.

Damit ist das lokale Ledger vollständig:
\[
\boxed{
\text{an }x_1=e-u\text{ tragen exakt }W_{11},W_{13}.
}
\tag{LL.6}
\]
Folglich
\[
\boxed{
(AU_Rf)(e-u)
=\left[-p^2+q^2 1_{\{u>e-\varepsilon\}}\right]f(u).
}
\tag{LL.7}
\]

## 3. Vollständiges 11-Wort-Ledger bei x2=a-u

Setze
\[
x_2=a-u\in(a-\ell,a).
\]

### Zeile j=1

Es gilt
\[
x_2-a=-u,
\qquad
x_2+a=T-u.
\tag{LL.8}
\]
Nach Ungeradheit ist der erste Rücktransportwert `+g_k(u)`.

- `W11`: `g1(u)=0`, `g1(T-u)=0`; also null.
- `W12`: `g2(u)=rho f(u)`, während `g2(T-u)=0`; also aktiv. Mit Gewicht
  \[
  (\log2)\alpha_1\alpha_2=(\log2)2^{-9/4}=\gamma
  \]
  ergibt sich
  \[
  +\gamma\rho f(u).
  \]
- `W13`: `g3(u)=g3(T-u)=0`; also null.

### Zeile j=2

Es gilt
\[
x_2-T=-(a+u),
\qquad
x_2+T=3a-u.
\tag{LL.9}
\]
Somit wird der erste Rücktransportwert zu `+g_k(a+u)`.

- `W21`: `g1(a+u)=0`; auch `g1(3a-u)=0`; also null.
- `W22`: `g2(a+u)=0`; auch `g2(3a-u)=0`; also null.
- `W23`: 
  \[
  g_3(a+u)=\rho f(u)1_{\{u<\varepsilon\}},
  \]
  während `g3(3a-u)=0`. Also aktiv. Sein Gewicht ist
  \[
  (\log2)\alpha_2\alpha_3
  =\gamma\,2^{-3/2}
  =\gamma\beta.
  \]
  Daher liefert `W23`
  \[
  +\gamma\rho\beta\,1_{\{u<\varepsilon\}}f(u).
  \]

### Zeile j=3

Die Rücktransportpunkte haben Beträge mindestens `T+u` beziehungsweise liegen rechts von `4a-u`; beide liegen außerhalb der maskierten `g_k`-Supports. Also
\[
W_{31}=W_{32}=W_{33}=0
\]
an `x2`.

### (2,1)-Selbstterm

Die Rücktransportpunkte des `K2^*` sind `-(a+u)` und `3a-u`, beide mit Betrag `>a>epsilon`; der maskierte `(2,1)`-Output liegt in `|x|<epsilon`. Also ist dieser Term an `x2` null.

### (3,0)-Selbstterm

Mit Halbverschiebung `b`:
\[
x_2-b=-(d+u),
\qquad
x_2+b=a+b-u.
\tag{LL.10}
\]
Der `(3,0)`-Output ist nur in `(0,ell)\cup(R,e)` und Spiegelung getragen. Es gilt
\[
d+u>d>e,
\qquad
a+b-u>a>e.
\]
Also ist auch der `(3,0)`-Selbstterm an `x2` null.

Damit:
\[
\boxed{
\text{an }x_2=a-u\text{ tragen exakt }W_{12},W_{23}.
}
\tag{LL.11}
\]
und
\[
\boxed{
(AU_Rf)(a-u)
=\gamma\rho\left(1+\beta1_{\{u<\varepsilon\}}\right)f(u).
}
\tag{LL.12}
\]

## 4. Vollständige Hub-Ast-Isolation bei x1=e-u

Für
\[
H=pD_{2a}+rD_{2b}+qD_{2T}
\]
werden alle sechs Astpunkte explizit geprüft.

### a-Kanal
\[
x_1-a=-(d+u)
\]
ist der einzige potentiell annular aktive Punkt und liefert wegen Ungeradheit
\[
-p1_{\{d+u<S\}}w(d+u).
\]
Der Vorwärtsast ist
\[
x_1+a=a+e-u>a+e-\ell=a+R>a>S,
\]
also außerhalb.

### b-Kanal
\[
x_1-b=-(2d+u),
\]
und
\[
2d+u>2d>a>S
\]
weil `d>a/2`. Der Vorwärtsast ist
\[
x_1+b=T-u>T-\ell=b+R>b>a>S.
\]
Beide sind außerhalb.

### T-Kanal
\[
x_1-T=-(b+u),
\qquad |x_1-T|=b+u>b>a>S,
\]
und
\[
x_1+T=T+e-u>T>S.
\]
Beide sind außerhalb.

Somit exakt
\[
\boxed{
(HE_Aw)(e-u)=-p1_{\{d+u<S\}}w(d+u).
}
\tag{LL.13}
\]

## 5. Vollständige Hub-Ast-Isolation bei x2=a-u

### a-Kanal
\[
x_2-a=-u,
\qquad |u|<\ell<R,
\]
liegt im inneren Loch. Der Vorwärtsast
\[
x_2+a=T-u>T-\ell=b+R>b>a>S
\]
liegt außerhalb.

### b-Kanal
\[
x_2-b=-(d+u)
\]
ist der einzige potentiell annular aktive Punkt und liefert
\[
-r1_{\{d+u<S\}}w(d+u).
\]
Der Vorwärtsast erfüllt
\[
x_2+b=a+b-u>a>S
\]
weil `u<b`.

### T-Kanal
\[
x_2-T=-(a+u),
\qquad |x_2-T|=a+u>a>S,
\]
und
\[
x_2+T=3a-u>2a=T>a>S
\]
weil `u<a`. Beide sind außerhalb.

Damit exakt
\[
\boxed{
(HE_Aw)(a-u)=-r1_{\{d+u<S\}}w(d+u).
}
\tag{LL.14}
\]

## 6. Konsequenz für ST-1

Die beiden bislang extern nur teilweise nachgerechneten Voraussetzungen ST-A/ST-C und ST-B/ST-D sind damit intern vollständig auf alle elf Restwörter bzw. alle sechs Hubäste zurückgeführt.

Zusammen mit der bereits unabhängig bestätigten Vorzeichen-Elimination gilt weiterhin:
\[
P_u=p^2-q^2 1_{\{u>e-\varepsilon\}}>0,
\qquad
G_u=\gamma\rho(1+\beta1_{\{u<\varepsilon\}})>0.
\]
Die zwei ambient Gleichungen koppeln exakt denselben Annuluswert `w(d+u)` und erzwingen punktweise `f(u)=0`. Danach reduziert sich der Blockkernel auf `HE_Aw=0`; da `S<a<T`, greift das globale P12-Stratum `S<T` und liefert `w=0`.

**Interner Kandidatenstand:** ST-1 ist damit intern vollständig geschlossen.  
**Externer Status:** weiterhin kein vollständiges independent GREEN, bis gerade dieses lokale Ledger unabhängig gegengeprüft wurde.

Keine Promotion ohne explizite Freigabe.
