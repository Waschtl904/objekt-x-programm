# X-C1-CONNECTED-REST-SCHUR — a=49/125: variable Knotenreserve rettet Mode 2

**Datum:** 17. September 2026.  
**Status:** neue analytische Autorenableitung; externe Prüfung offen.  
**Elternstand:** Connected-Faktorisierung, Crossing `a=387/1000` und analytische Waxing-Funktion auf PR #137.  
**Scope:** gesamte verbundene Klasse
\[
\mathcal W_a=H^1_0((-a,a);\mathbb C)\cap\ker E_+\cap\ker E_-,
\qquad a=\frac{49}{125}=0.392.
\]
**Nicht verwendet:** A1, numerische Eigenwerte, Quadratur als Beweis, dritte Momentbedingung.

## 0. Ergebnis

Der Punkt `a=49/125` liegt rigoros jenseits der konstant-floor-Schwelle
`a_cf in (0.3916683,0.3916684)`. Der maximal konstante Gamma-Boden allein besitzt dort eine negative Mode-2-Richtung. Trotzdem ist C15 noch nicht nötig.

Die exakte Kanten-/Knotenzerlegung enthält eine variable positive Knotenreserve `V_a`. Auf den äußeren Hälften der beiden aktiven Prime-2-Endbänder gilt unabhängig

```math
V_a(x)>\frac3{10}.
```

Diese Reserve erzeugt auf dem even-Hochmodenraum einen echten unendlichdimensionalen Schur-Block. Seine Schur-Untergrenze bleibt nach Transport der einzigen even-Mellinbedingung strikt positiv. Der odd-Sektor bleibt bereits ohne diesen Zusatz stark positiv.

Damit gilt auf der gesamten verbundenen NULLPOL-Klasse

```math
\boxed{
Q_W[u] > \frac1{100000}\|u\|_2^2
\qquad(0\ne u\in\mathcal W_{49/125}).
}                                                    \tag{RS0}
```

Der nichtkonstante positive Gamma-Rest `r_a(t)=g(t)-g(2a)` und die Prime-2-Differenzenergie bleiben im Beweis sogar unbenutzt positiv. Das ist daher stärker als der zunächst geplante Test, ob gerade `r_a` Mode 2 retten kann: bereits die zuvor ausgelagerte **variable Knotenenergie** genügt.

**Firewall:** Dies ist kein Einheitsfenster, kein all-window Resultat, kein Objekt-X-/RH-Satz und keine Aussage, dass C15 niemals nötig wird.

---

## 1. Exakte Ausgangsform

Setze

```math
I_a=(-a,a),\qquad L=2a=\frac{98}{125},
```

```math
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},\qquad
g(t)=h(t)-\frac1{2t},
```

```math
\ell=\log2,\qquad w=\frac{\log2}{\sqrt2},\qquad
\kappa_*=\log(8\pi)+\gamma+\frac\pi2,
```

und

```math
H(s)=\int_s^\infty h(t)\,dt.
```

Weil `L<log3`, ist nur Prime 2 aktiv. Auf NULLPOL gilt die bereits eingefrorene gemeinsame Kantenidentität

```math
Q_W[u]
=\int_{x<y\in I_a}h(y-x)|u(y)-u(x)|^2\,dx\,dy
+w\int_{-a}^{a-\ell}|u(x+\ell)-u(x)|^2\,dx
+\int_{I_a}\rho_a(x)|u(x)|^2\,dx,                 \tag{RS1}
```

mit

```math
W_a(x)=H(a+x)+H(a-x),
```

```math
d_P(x)=w\{1_{I_a}(x-\ell)+1_{I_a}(x+\ell)\},
\qquad
\rho_a=W_a-\kappa_*-d_P.
```

Alle inneren Nähte sind bereits in der ersten positiven Differenzenergie enthalten.

---

## 2. Maximaler konstanter Gamma-Boden und exakter Knotenboden

Aus dem analytischen Waxing-Gate gilt auf allen hier vorkommenden Abständen

```math
g'(t)<0\qquad(0<t\le L<2).
```

Also ist

```math
c_a=g(L)=\inf_{0<t\le L}g(t),
\qquad
r_a(t)=g(t)-c_a\ge0.                               \tag{RS2}
```

Schreibe

```math
h(t)=\frac1{2t}+c_a+r_a(t).
```

Für die normierte Legendrebasis

```math
e_n(x)=\sqrt{\frac{2n+1}{2a}}P_n(x/a)
```

liefert der erste Anteil den harmonischen Faktor `H_n`, der konstante Anteil `c_a L` auf allen nichtkonstanten Moden.

### 2.1 Wo liegt das Minimum von rho?

Setze

```math
d=L-\ell>0.
```

Im prime-inaktiven Zentrum ist `rho=W_a-kappa_*`; da `W_a` gerade und für `x>0` steigend ist, liegt dessen Minimum bei `x=0`.

Im aktiven rechten Endband `x in [\ell-a,a]` ist `d_P=w` konstant und `W_a` steigend. Das Minimum des aktiven Bandes liegt daher bei `x=\ell-a` und lautet

```math
H(d)+H(\ell)-\kappa_*-w.
```

Der exakte rationale Intervallprüfer zeigt zusätzlich, dass dieser Wert unter dem Mittelpunktwert liegt. Daher ist der globale Knotenboden exakt

```math
-C_a=H(d)+H(\ell)-\kappa_*-w,
```

also

```math
\boxed{
C_a=\kappa_*+w-H(d)-H(\ell)>0.
}                                                    \tag{RS3}
```

und

```math
V_a(x):=\rho_a(x)+C_a\ge0.                         \tag{RS4}
```

Der Prüfer schließt rigoros

```math
C_a<\frac{1711}{1000}.                              \tag{RS5}
```

---

## 3. Die entscheidende neue Reserve sitzt auf den äußeren Endbandhälften

Definiere die symmetrische Menge

```math
J_a=\{x\in I_a:\ |x|\ge\ell/2\}.
```

Da `2a>ell`, liegt `J_a` vollständig in den beiden Prime-2-Endbändern. Dort ist `V_a` mit `|x|` steigend. Sein Minimum auf `J_a` liegt bei `x=ell/2`.

Aus (RS3) folgt dort die kappa- und w-freie Identität

```math
V_a(\ell/2)
=H\!\left(\frac{L+\ell}{2}\right)
 +H\!\left(\frac{L-\ell}{2}\right)
 -H(L-\ell)-H(\ell).                               \tag{RS6}
```

Die rein rationale Intervallrechnung liefert

```math
\boxed{V_a(x)>\frac3{10}\quad(x\in J_a).}          \tag{RS7}
```

Damit zerfällt die Knotenenergie exakt als

```math
\int V_a|u|^2
=\frac3{10}\int_{J_a}|u|^2
 +\int\left(V_a-\frac3{10}1_{J_a}\right)|u|^2,    \tag{RS8}
```

wobei der zweite Term positiv ist.

Der positive Restkernel `r_a` und die Prime-Differenzenergie aus (RS1) bleiben ebenfalls vollständig positiv erhalten. Für die folgende Untergrenje werden beide nicht benötigt.

---

## 4. Skalare Legendre-Bilanz

Nach (RS2)--(RS4) lautet der skalare Teil

```math
-C_a|u_0|^2+\sum_{n\ge1}\lambda_n|u_n|^2,
```

mit

```math
\lambda_n=\mathsf H_n+Lc_a-C_a,\qquad n\ge1.       \tag{RS9}
```

Da `Lc_a=Lh(L)-1/2`, kann Mode 2 auch geschrieben werden als

```math
\lambda_2=1+Lh(L)-C_a.
```

Der exakte Prüfer beweist

```math
\boxed{\lambda_2>-\frac{21}{500}.}                 \tag{RS10}
```

Weil

```math
\mathsf H_4-\mathsf H_2=\frac7{12},
```

folgt für alle even-Moden `n>=4`

```math
\lambda_n>\frac{27}{50}.                           \tag{RS11}
```

Analog

```math
\lambda_n>\frac{437}{1500}\quad(n\ge3,\ n\text{ odd}), \tag{RS12}
```

und

```math
-\lambda_1<\frac{271}{500}.                        \tag{RS13}
```

---

## 5. Der echte even Rest-Schur-Block

NULLPOL zerfällt nach Parität in genau die beiden bekannten Momentbedingungen. Im even-Sektor schreibe

```math
u_{\rm even}=u_0e_0+x,
\qquad
x=\alpha e_2+y,
\qquad y\in Y_{\rm even}:=\overline{\operatorname{span}}\{e_4,e_6,\ldots\}.
```

Die cosh-Bedingung liefert wie im Connected-Elternsatz

```math
|u_0|^2<\frac1{2500}\|x\|_2^2.                    \tag{RS14}
```

### 5.1 Wie viel P2-Masse liegt in J_a?

Sei `P_J` die Multiplikation mit `1_{J_a}` und

```math
p=\langle e_2,P_Je_2\rangle.
```

Mit `z_0=ell/L` folgt exakt

```math
p
=5\int_{z_0}^1P_2(z)^2dz
1-\frac94z_0^5+\frac52z_0^3-\frac54z_0.           \tag{RS15}
```

Die rationale `log2`-Einschließung liefert

```math
\boxed{p>\frac25.}                                  \tag{RS16}
```

### 5.2 Die u0-Korrektur kostet nur eine kontrollierte Menge

Punktweise gilt für komplexe Zahlen

```math
|A+B|^2\ge\frac12|A|^2-|B|^2.
```

Mit (RS7) erhält man daher

```math
\frac3{10}\int_{J_a}|x+u_0e_0|^2
\ge
\frac3{20}\langle x,P_Jx\rangle
-\frac3{10}|u_0|^2.                                \tag{RS17}
```

Setze

```math
\mu=\frac3{20},\qquad \delta=\frac{27}{50}.
```

Nach Weglassen aller übrigen positiven Outputs ist der Hochmodenblock von unten durch

```math
F_e[x]
=\lambda_2|\alpha|^2+\delta\|y\|^2
 +\mu\langle x,P_Jx\rangle                         \tag{RS18}
```

kontrolliert.

Relativ zu `C e_2 direct-sum Y_even` hat dieser Block

```math
D=\delta I+\mu P_Y P_JP_Y\succeq\delta I,
```

```math
b=\mu P_YP_Je_2,
\qquad
A_{22}=\lambda_2+\mu p.
```

Das Schur-Komplement erfüllt

```math
A_{22}-\langle b,D^{-1}b\rangle
\ge
\lambda_2+\mu p-\frac{\mu^2}{\delta}
 \|P_YP_Je_2\|^2.
```

Wegen

```math
\|P_YP_Je_2\|^2\le\|P_Je_2\|^2=p
```

folgt aus (RS10), (RS16)

```math
\begin{aligned}
A_{22}-\langle b,D^{-1}b\rangle
&> -\frac{21}{500}
 +\frac3{20}\frac25
 \left(1-\frac{(3/20)}{(27/50)}\right)\\
&=\boxed{\frac1{750}}>0.                           \tag{RS19}
\end{aligned}
```

**Damit ist das vom Audit verlangte unendlichdimensionale Schur-Kriterium tatsächlich positiv.**

### 5.3 Vom Schur-Koordinatensystem zurück zur L2-Norm

Ferner

```math
\|D^{-1}b\|\le\frac\mu\delta=\frac5{18}.
```

Die obere Dreieckstransformation der Quadratvervollständigung hat daher Norm höchstens

```math
1+\frac5{18}=\frac{23}{18}.
```

Aus (RS19) und `D>=delta I` folgt

```math
F_e[x]\ge\frac{54}{66125}\|x\|^2.                 \tag{RS20}
```

Die negative konstante Mode und der Verlust in (RS17) kosten zusammen höchstens

```math
\left(C_a+\frac3{10}\right)|u_0|^2
<\frac{2011}{2500000}\|x\|^2.                     \tag{RS21}
```

Somit

```math
Q_{W,\rm even}[u]
>\frac{16181}{1322500000}\|x\|^2.
```

Da nach (RS14)

```math
\|u_{\rm even}\|^2
<\left(1+\frac1{2500}\right)\|x\|^2,
```

ergibt sich

```math
\boxed{
Q_{W,\rm even}[u]
>\frac{16181}{1323029000}\|u_{\rm even}\|^2
>\frac1{100000}\|u_{\rm even}\|^2.
}                                                    \tag{RS22}
```

---

## 6. Odd-Sektor

Schreibe

```math
u_{\rm odd}=u_1e_1+z,
\qquad z\in\overline{\operatorname{span}}\{e_3,e_5,\ldots\}.
```

Die sinh-Bedingung liefert

```math
|u_1|^2<\frac1{22500}\|z\|^2.                     \tag{RS23}
```

Wir benötigen hier nicht einmal die Knotenreserve. Aus (RS12)--(RS13) folgt direkt

```math
Q_{W,\rm odd}[u]
>\left(\frac{437}{1500}
 -\frac{271}{500}\frac1{22500}\right)\|z\|^2.
```

Nach Rückrechnung auf die volle odd-Norm ergibt der exakte Bruchcheck

```math
\boxed{Q_{W,\rm odd}[u]>\frac14\|u_{\rm odd}\|^2.} \tag{RS24}
```

---

## 7. Gesamtsatz und positive Auswertung

Alle verwendeten Kern-, Knoten- und Shiftoperatoren sind spiegelinvariant; even und odd sind daher orthogonale Formsektoren. Aus (RS22)--(RS24) folgt (RS0).

Die exakte Form lässt sich dabei als Summe folgender vorwärts definierter Bestandteile lesen:

1. positive Rest-Gamma-Kanten mit Dichte `r_a(t)`;
2. positive Prime-2-Differenzkanten;
3. positives Knotengewicht `V_a-(3/10)1_{J_a}`;
4. der explizite even-Block aus (RS9) plus `(3/10)P_J`, nach der cosh-Momentparametrisierung;
5. der explizite odd-Block aus (RS9), nach der sinh-Momentparametrisierung;
6. optional der positive odd-Anteil von `(3/10)P_J` als eigener Output.

Die Blöcke 4 und 5 sind durch (RS19)--(RS24) geschlossene strikt positive Formen auf ihren angegebnen Formdomains. Ihre positiven Formquadratwurzeln sind daher nach dem unabhängigen Schur-Nachweis wohldefiniert. Es wird nicht `Q_W^1/2` aus voraussgesetzter Weil-Positivität definiert; die Positivität der benannten Bausteine wurde vorher aus Träger-, Kernel-, Moment- und Schurabschätzungen bewiesen.

Dies liefert eine exakte positive Gram-Auswertung auf genau `W_{49/125}`. Eine konkrete Port-Naturalisierung dieser beiden Formquadratwurzeln als zusätzliche C0-Zustandsports wird hier nicht behauptet.

---

## 8. Warum dies den geplanten Rest-Schur-Gate entscheidet

Der Audit hatte für `a=49/125` gefordert, die nach Überschreiten der konstant-floor-Schwelle noch vorhandene positive Energie nicht vollständig wegzuwerfen. Das Ergebnis ist endeutiger als erwartet:

- `lambda_2<0` der maximal konstant skalarisierten Unterform bleibt ein echter Methoden-Crossing;
- der nichtkonstante Gamma-Rest `r_a` ist positiv, wird aber für den Rettungsbeweis nicht benötigt;
- die Prime-Differenzenergie ist positiv, wird ebenfalls nicht benötigt;
- **allein die variable Knotenreserve** liefert einen Schur-Pivot `>1/750`;
- die beiden echten Mellinbedingungen reichen weiterhin; keine dritte Nebenbedingung wird eingeführt;
- C15 muss bei `a=0.392` noch nicht als neuer Restfreiheitsgrad-Mechanismus aktiviert werden.

Das ist kein allgemeiner Satz, dass die Knotenreserve für beliebige Fenster genügt. Der nächste strukturelle Grenztest muss bestimmen, wie weit diese konkrete äußere Reserve-Schur-Architektur in `a` trägt und wo erstmals auch `r_a`, Prime-Differenzenergie oder C15 tatsächlich benötigt werden.

---

## 9. Checks und Status

`check_x_c1_rest_schur_49_125.py` verwendet für alle PASS-Entscheidungen ausschließlich exakte `Fraction`-Arithmetik und rationale Restabschätzungen der transzendenten Reihen. Der gespeicherte Lauf liefert **18/18 PASS**.

Geprüft werden insbesondere:

- exakter globaler Knotenboden und `C_a<1711/1000`;
- Endbandboden liegt unter dem Mittelpunktboden;
- `V_a>3/10` auf den äußeren Endbandhälften;
- `lambda_2>-21/500` und die even/odd-Tailfloors;
- `P_2`-Masse auf `J_a` größer als `2/5`;
- beide Mellin-Rekonstruktionsbudgets;
- Schur-Pivot `1/750`, Rücktransformationsbudget und endgültiger Gap `>1/100000`.

**Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`.

Kein A1-Replay, keine CI-GREEN-Behauptung, keine Registry-Promotion, kein Merge, kein Einheitsfenster- oder RH-Claim.
