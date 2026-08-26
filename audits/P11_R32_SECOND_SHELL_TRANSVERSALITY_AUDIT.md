# P11/R32 — zweite nichtzentrale Schale: ambient Zwei-Punkt-Transversalität

**Status:** Kandidat; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Basis:** SE-1/SE-2, SS-1a, SS-L, SP-1 sowie die P11↔P12 Odd-Fold-Rückbindung.  
**Ziel:** die zweite nichtzentrale Rand-Schale aus `P11_R32_SECOND_NONCENTRAL_SHELL_LEDGER_AUDIT.md` im echten augmentierten Blockkern ausschließen. Der Beweis verwendet zwei **ambient Punktgleichungen** und nicht die bloße Profilkompression.

## 1. Setup

Im Drei-Shift-Fenster
\[
2a<T_0<c=\tfrac12\log5,
\qquad a=\tfrac12\log2,
\quad b=\tfrac12\log3,
\quad T=2a,
\]
setze
\[
d=b-a,
\qquad e=T-b,
\qquad \varepsilon=T_0-T.
\]
Fixiere
\[
\boxed{\frac d2\le R<e,
\qquad R<S<a.}
\tag{ST.1}
\]
Dann
\[
\ell:=e-R\in(0,R),
\qquad
\rho:=\frac rq>0.
\]

Die zweite Schale wird durch ein Profil `f in L^2(0,ell)` parametrisiert:
\[
y=U_Rf,
\]
\[
y(b+u)=f(u),
\qquad
y(T-u)=\rho f(u),
\qquad0<u<\ell,
\]
mit gerader Fortsetzung. Nach SS-1a liegt diese Schale in
\[
\mathcal K_R=\ker(E_I^*H|_+).
\]

Der augmentierte SE-Block lautet
\[
\mathcal K_{I,A}(y,w)
=\bigl((I+A)y+HE_{\mathcal A}w,\ E_I^*Hy\bigr),
\qquad A=R_{T_0}^*R_{T_0}.
\]
Sei im Folgenden `(U_Rf,w)` ein Blockkernpaar.

Schreibe
\[
p=\sqrt{\log2}\,2^{-3/4},
\quad
q=\sqrt{\log2}\,2^{-3/2},
\quad
r=\sqrt{\log3}\,3^{-3/4},
\]
und
\[
\gamma:=(\log2)2^{-9/4}>0,
\qquad
\beta:=2^{-3/2}>0.
\]

## 2. Erste ambient Auswertung: x_1=e-u

Fixiere fast jedes `0<u<ell` und setze
\[
x_1:=e-u\in(R,e).
\]
Da `x_1<a<b`, liegt `y(x_1)=0`.

### 2.1 Lokales 11-Wort-Ledger bei x_1

Im `(2,0)`-Block
\[
W_{jk}:=K_j^*M_{20}K_k,
\qquad j,k\in\{1,2,3\}.
\]
Von allen elf Full-Rest-Wörtern erreichen `x_1` exakt zwei:

1. `W_11` erreicht über den rechten `K1`-Kanal bei `d+u` den Punkt `x_1=e-u` nach dem linken `K1^*`-Rücktransport und liefert
   \[
   -p^2f(u).
   \]

2. `W_13` erreicht `x_1` genau dann, wenn der rechte `K3`-Kanal bei
   \[
   a+e-u
   \]
   die `Omega20`-Maske überlebt, also
   \[
   e-u<\varepsilon
   \iff
   u>e-\varepsilon.
   \]
   Sein Koeffizient ist
   \[
   (\log2)\alpha_1\alpha_3
   =(\log2)2^{-3}
   =q^2,
   \]
   und das Vorzeichen ist positiv.

Alle übrigen sieben `(2,0)`-Wörter, der `(2,1)`-Selbstterm und der `(3,0)`-Selbstterm besitzen bei `x_1` keinen Support. Somit
\[
\boxed{
(AU_Rf)(e-u)
=\left[-p^2+q^2 1_{\{u>e-\varepsilon\}}\right]f(u).
}
\tag{ST.2}
\]

### 2.2 Hubterm bei x_1

Für ungerades Annulus-`w` gilt
\[
(e-u)-a=-(d+u).
\]
Alle anderen `a,b,T`-Äste liegen entweder im inneren Loch oder außerhalb `(-S,S)`. Daher
\[
\boxed{
(HE_{\mathcal A}w)(e-u)
=-p\,1_{\{d+u<S\}}w(d+u).
}
\tag{ST.3}
\]

Die erste Blockgleichung liefert
\[
\boxed{
\left[-p^2+q^2 1_{\{u>e-\varepsilon\}}\right]f(u)
-p\,1_{\{d+u<S\}}w(d+u)=0.
}
\tag{ST.4}
\]

## 3. Zweite ambient Auswertung: x_2=a-u

Setze
\[
x_2:=a-u\in(a-\ell,a)=(d+R,a).
\]
Auch hier ist `y(x_2)=0`, denn die positive Schale beginnt erst bei `b>a`.

### 3.1 Lokales 11-Wort-Ledger bei x_2

Bei `x_2=a-u` erreichen von allen elf Wörtern exakt zwei den Punkt:

1. `W_12=K_1^*M20K_2` liefert
   \[
   \gamma\rho f(u).
   \]
   Hier kommt der rechte `K2`-Kanal bei `u` nach dem linken `K1^*`-Rücktransport zu `a-u`.

2. `W_23=K_2^*M20K_3` liefert genau dann einen Zusatz, wenn der rechte `K3`-Kanal bei `a+u` die Maske überlebt, also `u<epsilon`. Sein relativer Koeffizient ist
   \[
   \frac{\alpha_2\alpha_3}{\alpha_1\alpha_2}
   =\frac{\alpha_3}{\alpha_1}
   =2^{-3/2}=\beta.
   \]

Alle übrigen sieben `(2,0)`-Wörter sowie `(2,1)` und `(3,0)` sind an `x_2` supportfrei. Daher
\[
\boxed{
(AU_Rf)(a-u)
=\gamma\rho\left[1+\beta 1_{\{u<\varepsilon\}}\right]f(u).
}
\tag{ST.5}
\]

### 3.2 Hubterm bei x_2

Es gilt
\[
(a-u)-b=-(d+u).
\]
Der `a`-Rückast liegt bei `-u` im inneren Loch, der `T`-Rückast bei `-(a+u)` außerhalb des Annulus, und alle Vorwärtsäste liegen rechts von `S<a`. Also
\[
\boxed{
(HE_{\mathcal A}w)(a-u)
=-r\,1_{\{d+u<S\}}w(d+u).
}
\tag{ST.6}
\]

Die erste Blockgleichung liefert somit
\[
\boxed{
\gamma\rho\left[1+\beta 1_{\{u<\varepsilon\}}\right]f(u)
-r\,1_{\{d+u<S\}}w(d+u)=0.
}
\tag{ST.7}
\]

## 4. Vorzeichen-Elimination

Setze
\[
\chi(u):=1_{\{d+u<S\}}.
\]
Ferner
\[
P_u:=p^2-q^2 1_{\{u>e-\varepsilon\}}>0
\tag{ST.8}
\]
weil
\[
p^2>q^2>0,
\]
und
\[
G_u:=\gamma\rho\left[1+\beta 1_{\{u<\varepsilon\}}\right]>0.
\tag{ST.9}
\]
Dann sind (ST.4) und (ST.7) genau
\[
-P_u f(u)-p\chi(u)w(d+u)=0,
\tag{ST.10}
\]
\[
G_u f(u)-r\chi(u)w(d+u)=0.
\tag{ST.11}
\]

### Fall chi(u)=0

Aus (ST.10) folgt sofort
\[
f(u)=0.
\]

### Fall chi(u)=1

Aus den beiden Gleichungen folgt
\[
w(d+u)=-\frac{P_u}{p}f(u),
\qquad
w(d+u)=\frac{G_u}{r}f(u).
\]
Daher
\[
\left(\frac{P_u}{p}+\frac{G_u}{r}\right)f(u)=0.
\]
Der Koeffizient ist strikt positiv, also wiederum
\[
f(u)=0.
\]

Somit
\[
\boxed{f=0\text{ fast überall auf }(0,\ell).}
\tag{ST.12}
\]
Also `y=U_Rf=0`.

## 5. Danach w=0

Mit `y=0` reduziert sich die erste augmentierte Blockgleichung auf
\[
HE_{\mathcal A}w=0.
\tag{ST.13}
\]
In unserem gesamten Sektor gilt
\[
S<a<T.
\]
Die bereits in P12 bewiesene globale Hub-Injektivität im Stratum `S<T`, zusammen mit der exakten P11↔P12 Odd-Fold-Identifikation
\[
\mathcal R_+H_{T_0}E_{\mathcal A}\mathcal O_{R,S}
=L_{R,S,T_0}^{\{a,b,2a\}},
\]
liefert daher
\[
\boxed{w=0.}
\tag{ST.14}
\]

## 6. Theorem ST-1 — zweite Schale transversal

Für
\[
\boxed{
\frac d2\le R<e,
\qquad R<S<a
}
\]
gilt
\[
\boxed{
\ker\mathcal K_{I,A}
\cap
(\mathcal S_{R,2}^+\oplus\mathscr H_{\mathcal A}^-)
=\{0\}.
}
\tag{ST.15}
\]
Äquivalent auf den hier ohnehin globalen P12-Hub-Injektivitätsstrata:
\[
\boxed{
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap
(I+A)\mathcal S_{R,2}^+
=\{0\}.
}
\tag{ST.16}
\]

## 7. Bedeutung

Die zweite Schale war ambient wesentlich komplizierter als NS-1:
\[
10/11
\]
Full-Rest-Wörter sind global aktiv. Trotzdem reichen für die echte Blockkernfrage zwei gezielt gewählte ambient Auswertungspunkte. An beiden Punkten koppelt derselbe Annuluswert `w(d+u)`, während die beiden Restkoeffizienten von `f(u)` strikt entgegengesetztes Vorzeichen besitzen.

Das ist stärker als die reine SP-1-Profilkompression: Die Transversalität folgt nicht aus `V_R^*AV_R`, sondern aus einer lokalen **Sign-locked two-point observation** des vollen ambient Operators.

## 8. Firewall

ST-1 beweist nur die Transversalität der zweiten expliziten nichtzentralen Schale.

Nicht bewiesen:

- Klassifikation des gesamten `K_R`;
- voller augmentierter Blockkern trivial;
- voller Schur-Crossblock injektiv;
- Closed Range / bounded below / uniforme Winkel;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

Kandidatenstatus:

- **ST-1:** `?[O]` bis unabhängiges GREEN.

Bei unabhängigem vollständigem GREEN wäre zulässig:

- **ST-1:** `✓[M]_part`.

Keine Promotion ohne explizite Freigabe.
