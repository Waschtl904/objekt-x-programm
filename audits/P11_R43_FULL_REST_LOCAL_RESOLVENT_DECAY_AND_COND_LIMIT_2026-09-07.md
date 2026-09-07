# P11 / R43 — Volle Restresolvente: lokaler Normzerfall und exakter COND-Grenzwert

Datum: 2026-09-07. Definitionsbasis: `main` auf
`55a3a1617513cc5d82c47d0cfd606c6b0894c984`.

**Status:** neuer analytischer Kandidat mit vollständiger Herleitung und
Autorengegencheck. Kein unabhängiger Exact-Head-Review, keine Registry-Promotion,
kein numerisches Zertifikat und kein Strong-Terminal-/RH-Abschluss.
Die schon integrierten LOCAL-O1-, Orientierungs- und festen-U-COND-Sätze werden
nicht erneut als offene lokale Aufgaben geführt.

## 0. Ergebnis, Nutzen und offene Grenze

Für die tatsächliche vollständige P11-Restresolvente
`B_V=(I+R_V^*R_V)^{-1}` gilt für jedes feste räumliche Fenster `r>0`

```math
\|E_{r,V}^*B_VE_{r,V}\|_{L^2(-r,r)\to L^2(-r,r)}=O_r(V^{-1}).
\tag{RL1}
```

Dies ist Operatornormzerfall auf dem ganzen alten L2-Fenster, nicht bloß
Konvergenz auf einer Testquelle oder nach einer kompakten Graphraumeinbettung.
Die volle Umgebungsraumresolvente konvergiert stark gegen null, aber nicht in
Operatornorm. Für festes altes `U` folgt mit Rate `O_U(V^{-1})`

```math
G_{X,\mathrm{cond}}^{U,V}\longrightarrow\Gamma_X
\quad\text{in Operatornorm},\qquad X=R,S.
\tag{RL2}
```

Damit wird der bisher nur normpräkompakte feste-U-COND-Horizontweg bis zu seinem
konkreten Grenzwert bestimmt. Auch die kanonische Reverse-Quelle und ihr
Reverse-Stretch erhalten einen exakten iterierten Grenzwert, siehe §7.

Die neue quantitative Aussage RL1 gilt im Fernzukunftsbereich relativ zum
festen Eingabefenster. Ihr Beweis liefert **keine** brauchbare Schranke bei
`r=U` und `U<V<=2U`: Dort fehlen die benötigten getrennten räumlichen Kopien.
BR39 und das tatsächliche globale Flagbudget bleiben offen. Eine
Normpräkompaktheit des vollständigen wachsenden Terminaltransports wird nicht
behauptet. Ein Grenzwert bei festem U darf nicht entlang U->infinity eingesetzt
werden, ohne die U-Abhängigkeit zu kontrollieren.

Die quantitative Zählung verwendet nur den gewöhnlichen, unbedingten
Primzahlsatz. Eine zusätzliche qualitative Herleitung des starken Nullgrenzwerts
in §9 benötigt nicht einmal diesen, sondern nur die Divergenz der
Primzahlreziprokensumme. Keine Nullstellenhypothese wird benutzt.

## 1. Exakte volle Restzeilen im gemeinsamen L2-Raum

Schreibe `H=L^2(R)`, `M_V=1_{(-V,V)}`, und benutze
`(U_t f)(u)=f(u-t)` sowie `D_s=U_{s/2}-U_{-s/2}`.
Die Einbettung und Restriktion heißen `E_V` und `P_V=E_V^*`.
`E_{r,V}:L^2(-r,r)->L^2(-V,V)` ist Nullerweiterung.

Die P11-Martingalzeile `(p,a)` im Umgebungsraum lautet genau

```math
(\widehat R_Vx)_{p,a}
 =c_{p,a}M_{p,a}(V)\sum_{k\ge a+1}p^{-3k/4}D_{k\log p}M_Vx,
\quad c_{p,a}=\sqrt{(\log p)(p-1)p^a},
\tag{RL3}
```

mit `M_{p,a}(V)=1_{|u|<V-(a+1)log(p)/2}`; ein nichtpositiver Radius
bedeutet die Nullmaske. Dies ist (3.4)/(3.5) von P11. Der gemeinsame Zielraum
kann als abzählbare orthogonale Summe vollständiger L2-Zeilen gewählt werden.
An jedem endlichen V sind nur endlich viele Zeilen und effektiv endlich viele
k aktiv; die sichere Restobergrenze ist `p^k<=exp(4V)`, nicht der Hub-Cutoff.
Die formal unendliche k-Summe jeder einzelnen Zeile konvergiert zudem absolut
in Operatornorm, da `||D_s||<=2`.

Verschiedene `(p,a)`-Zeilen sind orthogonal. Verschiedene k **innerhalb einer
Zeile sind nicht orthogonal**. Diese k-Summe wird im folgenden Beweis nicht
wegprojiziert oder durch eine unbewiesene primitive Formdominierung ersetzt.

Die exakte Energie und die Umgebungsraumresolvente sind

```math
\mathcal E_V(x)=\|\widehat R_Vx\|^2,
\qquad
\widehat B_V=(I+\widehat R_V^*\widehat R_V)^{-1}
 =E_VB_VP_V+(I-M_V),\quad 0<\widehat B_V\le I.
\tag{RL4}
```

Der äußere Identitätssummand wird überall beibehalten. Auf Eingängen in
`(-r,r)` mit `r<V` trägt er nicht bei.

## 2. Höhere Primzahlpotenzen: uniformer summierbarer Rest statt falscher Dominierung

Nur die vollständigen Zeilen `a=0` werden als Untermenge der orthogonalen
Restzeilen verwendet. Setze `s_p=log p`,

```math
w_p=(\log p)(p-1)p^{-3/2},\qquad
A_{p,V}=\sqrt{w_p}M_{p,0}(V)D_{s_p}M_V+T_{p,V},
\tag{RL5}
```

wobei `A_{p,V}x=(Rhat_Vx)_{p,0}` und

```math
T_{p,V}=\sqrt{(\log p)(p-1)}M_{p,0}(V)
           \sum_{k\ge2}p^{-3k/4}D_{k\log p}M_V.
```

Die kohärente Tail-Summe erfüllt für alle V

```math
\|T_{p,V}\|\le t_p
 :=\frac{2\sqrt{(\log p)(p-1)}p^{-3/2}}{1-p^{-3/4}}.
\tag{RL6}
```

Für `p>=256`, also `p^{-3/4}<=1/64`, folgt

```math
\sum_{p\ge256}t_p^2
 \le4\left(\frac{64}{63}\right)^2
       \sum_{n\ge256}\frac{\log n}{n^2}
 \le4\left(\frac{64}{63}\right)^2\frac{\log255+1}{255}
 <\frac{114688}{1012095}<\frac12.
\tag{RL7}
```

Hier wurde nur die abnehmende Funktion `log x/x^2` durch ihr Integral ab 255
majorisiert und `log255<6` benutzt. Die rationale letzte Schranke ist exakt.
Bezeichne die tatsächliche Summe links mit `C_tail`, so `C_tail<1/2`.

Für jede endliche Primzahlmenge mit p>=256 und Gewichte `0<=alpha_p<=1` gilt
folglich

```math
\sum_p\alpha_p\|T_{p,V}x\|^2\le C_{\rm tail}\|x\|^2.
\tag{RL8}
```

Dieser Fehler bleibt beim Vergrößern der Primzahlmenge beschränkt. Er wird
später explizit von der Identitätsenergie `||x||^2` aufgenommen.
Es wird nirgends `R_V^*R_V >= (R_V^(1))^*R_V^(1)` angenommen.

## 3. Lemma: viele getrennte Vergleichsfenster kontrollieren ein altes Fenster

Fixiere r>0. Wähle M disjunkte logarithmische Primzahlbänder
`[s_j,s_j+1)`, `j=0,...,M-1`, mit

```math
s_j\ge\log256,\qquad s_j>2r,\qquad s_j+1\le V-r,
\tag{RL9}
```

so dass auch die räumlichen Hüllen

```math
J_j=[s_j-r,s_j+1+r]
```

paarweise disjunkt sind. Vorausgesetzt sei für jedes Band

```math
W_j:=\sum_{s_j\le\log p<s_j+1}w_p\ge1.
\tag{RL10}
```

Setze für p im Band j
`alpha_p=1/W_j<=1` und `beta_p=w_p/W_j`, also
`sum_{p in j} beta_p=1`. Das sind ausschließlich Testgewichte in einer
Ungleichung; **der P11-Operator selbst wird nicht renormiert**.

Für y in `(-r,r)` liegt `u=y+s_p/2` innerhalb der tatsächlichen
`(p,0)`-Ausgabemaske, denn
`|u|+s_p/2<=r+s_p<=V`. Beide Eingabepunkte y und `y+s_p` liegen im Fenster V.
Deshalb gilt auf dieser gemessenen Zeile exakt

```math
\ell_p(y):=\sqrt{w_p}\,[x(y)-x(y+s_p)]
 =A_{p,V}x(y+s_p/2)-T_{p,V}x(y+s_p/2).
\tag{RL11}
```

Es wurde die tatsächliche Halbverschiebung verwendet; s_p ist die Distanz
zwischen den beiden Eingabepräbildern, nicht die Halbverschiebung selbst.
Restriktion auf die angegebene Ausgabezelle kann L2-Normen nur verkleinern.

Aus `||a-b||^2<=2||a||^2+2||b||^2`, Zeilenorthogonalität,
`alpha_p<=1` und RL8 folgt

```math
\sum_p\alpha_p\|\ell_p\|_{L^2(-r,r)}^2
 \le2\mathcal E_V(x)+2C_{\rm tail}\|x\|^2.
\tag{RL12}
```

Andererseits ist `x(y)=[x(y)-x(y+s_p)]+x(y+s_p)`. Die gleiche elementare
Quadratabschätzung, mit beta_p gemittelt und über die M Bänder addiert, ergibt

```math
M\|P_rx\|^2
 \le2\sum_p\alpha_p\|\ell_p\|^2
      +2\sum_p\beta_p\int_{-r}^r|x(y+s_p)|^2\,dy.
\tag{RL13}
```

Im Band j liegen die übersetzten Fenster in J_j. Da die beta_p eine
Wahrscheinlichkeitsgewichtung sind, ist ihr gemittelter Indikator höchstens
`1_{J_j}`. Die J_j sind disjunkt, also ist der letzte Summenausdruck ohne
Faktor 2 höchstens `||x||^2`, **nicht** M mal `||x||^2`.

Einsetzen in RL13 und RL12 liefert

```math
M\|P_rx\|^2
 \le4\mathcal E_V(x)+(4C_{\rm tail}+2)\|x\|^2
 \le4\bigl(\mathcal E_V(x)+\|x\|^2\bigr).
\tag{RL14}
```

RL14 gilt für jedes komplexe x im gesamten Umgebungsraum H; insbesondere
wird der spätere Resolventenvektor nicht als altfenstergetragen angenommen.
Seine fernen Werte werden gerade durch die disjunkten Vergleichsfenster
bilanziert. Weitere Restzeilen dürfen die rechte Energie nur erhöhen.

## 4. Existenz linear vieler nutzbarer Bänder

Der gewöhnliche Primzahlsatz `pi(x)~x/log x` liefert

```math
\pi(e^{s+1})-\pi(e^s)\sim(e-1)e^s/s\qquad(s\to\infty).
```

Im Band gilt
`w_p>=s(1-e^{-s})e^{-(s+1)/2}`. Daher wächst die Bandmasse W(s) mindestens
wie eine positive Konstante mal `e^{s/2}` und ist für alle hinreichend großen
reellen s mindestens 1. Ein möglicherweise enthaltenes einzelnes
Randprimzahlglied ändert diese Schlussfolgerung nicht.

Fixiere einmal eine Konstante `a_*>=log256`, so dass `W(s)>=1` für jedes
`s>=a_*`. Ihre numerische Größe wird nicht behauptet. Es wird keine effektive
Primzahlfehlerkonstante und keine kurze additive Intervallhypothese benötigt.
Die Bänder haben feste **logarithmische** Breite, also festes Verhältnis e
zwischen den Grenzen.

Wähle jetzt

```math
s_j=a_*+2r+1+j(2r+2),\qquad j=0,1,2,... .
```

Die räumlichen Hüllen J_j haben Länge `2r+1`, ihre Startpunkte Abstand
`2r+2`; sie sind daher mit positiver Lücke disjunkt. Die Bedingungen RL9
und RL10 gelten für genau die ersten

```math
M(r,V)=\max\left\{0,\ 1+
 \left\lfloor\frac{V-a_*-3r-2}{2r+2}\right\rfloor\right\}
\tag{RL15}
```

nutzbaren Bänder. Insbesondere wächst `M(r,V)~V/(2r+2)` bei festem r.
Der Primzahlsatz wird nur für diese Zählung gebraucht; das Energielemma
RL14 selbst ist eine exakte Aussage über jede geeignete endliche Bänderauswahl.

## 5. Normzerfall der echten komprimierten Resolvente

Sei `g in L^2(-r,r)` und `x=Bhat_V E_r g`. Aus der resolventen Gleichung folgt

```math
\|x\|^2+\mathcal E_V(x)
 =\operatorname{Re}\langle E_rg,x\rangle
 =\operatorname{Re}\langle g,P_rx\rangle.
\tag{RL16}
```

Für `M(r,V)>=1` gibt RL14

```math
M(r,V)\|P_rx\|^2\le4\|g\|\|P_rx\|.
```

Der Fall `P_rx=0` ist trivial; andernfalls Division durch seine Norm. Damit

```math
\boxed{\|E_{r,V}^*B_VE_{r,V}\|
       \le\eta(r,V):=\min\{1,4/M(r,V)\}.}
\tag{RL17}
```

Für M=0 wird `eta(r,V)=1` definiert. Die zusätzliche Schranke 1 folgt aus
der positiven Kontraktionseigenschaft der wirklichen Resolvente.

Für `V>a_*+3r+2` folgt insbesondere die glatte Majorante

```math
\eta(r,V)\le
\min\left\{1,\frac{8(r+1)}{V-a_*-3r-2}\right\}.
\tag{RL18}
```

Bei `V>=2(a_*+3r+2)` erhält man `eta(r,V)<=16(r+1)/V`.
Das beweist RL1 mit ausdrücklich angegebener Fensterabhängigkeit.

Aus `Bhat_V^2<=Bhat_V` folgt außerdem

```math
\|\widehat B_V E_r\|^2\le\eta(r,V),\qquad
\|\widehat B_V^{1/2}E_r\|^2
 =\|E_r^*\widehat B_VE_r\|\le\eta(r,V).
\tag{RL19}
```

Die Energie des tatsächlichen Resolventenvektors in RL16 ist ebenfalls
höchstens `eta(r,V)||g||^2`.

Kompakt getragene L2-Eingänge sind dicht, und `||Bhat_V||<=1`. Deshalb

```math
\boxed{\widehat B_V\xrightarrow[V\to\infty]{\rm strong}0.}
\tag{RL20}
```

Gleichzeitig ist `||Bhat_V||=1` für jedes endliche V, weil sie außerhalb
`(-V,V)` die Identität ist. RL20 ist keine Normkonvergenz auf dem gesamten
Umgebungsraum und wird nicht als Resolvente eines dicht definierten globalen
Operators mit Inverswert null interpretiert.

## 6. Konkreter Gamma-Grenzwert des festen-U-Conditioning-Wegs

Fixiere `0<R<S<U`. Im festen Quellgraphraum sei `j_X` die kanonische
Einbettung nach H und `Gamma_X` der Darstellungsoperator der Gamma-Form.
Nach LOCAL-O1 gilt `c_X I<=Gamma_X<=I`, mit festem `c_X>0`.

Setze wie im integrierten COND-Satz

```math
K_{X,U}=\widehat H(U)^*j_X,\qquad
G_{X,\mathrm{cond}}^{U,V}
 =\Gamma_X+K_{X,U}^*\widehat B_VK_{X,U}.
\tag{RL21}
```

K_X,U ist fest und in `(-U,U)` getragen. RL17 mit r=U liefert die
operatorwertige Abschätzung

```math
0\preceq G_{X,\mathrm{cond}}^{U,V}-\Gamma_X
 \preceq\eta(U,V)K_{X,U}^*K_{X,U},
```

folglich

```math
\boxed{\|G_{X,\mathrm{cond}}^{U,V}-\Gamma_X\|
 \le\eta(U,V)\|K_{X,U}\|^2=O_U(V^{-1}).}
\tag{RL22}
```

Für diese neue Normkonvergenz braucht man nicht einmal die Kompaktheit von
K_X,U: seine Beschränktheit und sein fester räumlicher Träger genügen.
Der vorhandene kompakte-Sandwich-Satz bleibt unabhängig davon gültig und
liefert bereits Uniformität auf dem ganzen offenen Horizontbereich.

Gamma-Pullback gibt `J^*Gamma_S J=Gamma_R`. Daher ist

```math
W_\Gamma:=\Gamma_S^{1/2}J\Gamma_R^{-1/2}
```

eine feste Isometrie und

```math
W_{\mathrm{cond}}(U,V)\longrightarrow W_\Gamma
\quad\text{in Operatornorm bei festem U}.
\tag{RL23}
```

Der Grenzoperator ist unabhängig von dem festgehaltenen alten U. Um den
Transfer ohne wachsenden Metrikfaktor zu kontrollieren, setze
`D_X=(G_(X,cond)^(U,V))^(1/2) Gamma_X^(-1/2)`.
Die exakte Pullback-Algebra ergibt

```math
W_{\mathrm{cond}}-W_\Gamma
 =(D_S-I)W_\Gamma-W_{\mathrm{cond}}(D_R-I).
```

Die Wurzeldifferenzabschätzung bei Untergrenze c_X und die beiden
Isometrien liefern damit die feste-U-Rate

```math
\|W_{\mathrm{cond}}(U,V)-W_\Gamma\|
 \le\eta(U,V)\left(
 \frac{\|K_{S,U}\|^2}{2c_S}
 +\frac{\|K_{R,U}\|^2}{2c_R}\right).
\tag{RL24}
```

Auch die Conditioning-Polarfaktoren haben konkrete Normgrenzen:
mit `C_X^infty=Gamma_X^(1/2)G_(X,U)^(-1/2)` sei
`U_X^infty=polar(C_X^infty)`. Die festen-U-Spektrallücken bleiben positiv.
Dann konvergieren die beiden vollständigen Defekte CF6 in Norm gegen

```math
\mathcal T_{\rm mod}^{\rm cond}(U,\infty)
 =W_\Gamma-\mathcal U_S^\infty W_U(\mathcal U_R^\infty)^*,
\qquad
\mathcal T_{\rm ph}^{\rm cond}(U,\infty)
 =\mathcal U_S^\infty W_U(\mathcal U_R^\infty)^*-W_U.
\tag{RL25}
```

Diese Grenzdefekte werden nicht als null behauptet. Normpräkompaktheit und
Flag-Uniformität bedeuten nicht, dass die ungeprojizierte Bewegung verschwindet.

## 7. Der wirkliche kanonische Reverse-Eingang und sein iterierter Grenzwert

Benutze unverändert RE6/BR29–BR30:

```math
f_{R;U,V}^{\rm rev}
 =(G_{R,\mathrm{cond}}^{U,V})^{-1/2}\varepsilon_R.
```

RL22 und die feste Untergrenze c_R geben

```math
f_{R;U,V}^{\rm rev}\longrightarrow
f_R^\Gamma:=\Gamma_R^{-1/2}\varepsilon_R
\quad\text{in der festen Graphnorm bei festem U}.
\tag{RL26}
```

Dies ist exakt die vorgeschriebene inverse Quadratwurzelquelle, kein
`G^{-1}`-Minimierer und keine frei gewählte Ersatzquelle.
Da `q_(R,cond)(f_rev)=1`, ist

```math
\rho^{\rm rev}_{R;U,V}
 =\bigl(\langle f_{R;U,V}^{\rm rev},G_{R,U}f_{R;U,V}^{\rm rev}\rangle-1\bigr)_+.
```

Mit `G_(R,U)-Gamma_R=K_(R,U)^* Bhat_U K_(R,U)>=0` folgt genau

```math
\boxed{\lim_{V\to\infty}\rho^{\rm rev}_{R;U,V}
 =\langle f_R^\Gamma,(G_{R,U}-\Gamma_R)f_R^\Gamma\rangle
 =\|\widehat B_U^{1/2}K_{R,U}f_R^\Gamma\|^2=:r_R^\infty(U).}
\tag{RL27}
```

Die positive-Teil-Klammer entfällt nur beim Grenzwert, weil diese spezielle
Grenzform nichtnegativ ist. Es wird weder `r_R^infty(U)>0` für alle U noch ein
Abfall oder Wachstum dieses skalaren Ausdrucks bei U->infinity behauptet.
Insbesondere gilt `sup_(V>U) rho_rev >= r_R^infty(U)`, aber RL27 ist kein
Gegenbeweis zu BR39 auf dem beschränkten Verhältnisfenster V<=2U.

Eine zusätzliche Prüfung verhindert eine irreführende Normschlussfolgerung.
Seien `A_U=I+R_U^*R_U`, `Btilde=E_(U,V)^*B_V E_(U,V)` und
`Q=B_U # Btilde` wie in RE2/RE3. Dann `Q A_U Q=Btilde` und

```math
\|A_U^{1/2}QH_U^*E_{R,U}f_{R;U,V}^{\rm rev}\|^2
 \le\eta(U,V)c_R^{-1}\|K_{R,U}\|^2\longrightarrow0
\quad(U\text{ fest}).
\tag{RL28}
```

Trotzdem hat die exakte Schurform an diesem transportierten Vektor den
Reverse-Stretch-Grenzwert RL27. Ohne Kontrolle der mit V variierenden
Schurform ist die kleine Vektornorm allein kein Argument für kleine Kosten.
Dies ist eine präzise Konsequenz der bereits vorhandenen RE-Identitäten;
es wird kein von null verschiedener Grenzwert ohne zusätzliche Hypothese
über `r_R^infty(U)` behauptet.

## 8. Anwendung auf die tatsächliche normalisierte volle Geometrie

Hier wird nicht die vollständige Terminalmetrik durch COND ersetzt.
Fixiere vielmehr einen beliebigen alten Hubhorizont L>X und lass V>L wachsen.
Schreibe `K_(X,V)=Hhat(V)^*j_X` und benutze die wirkliche Metrik
`G_(X,V)=Gamma_X+K_(X,V)^*Bhat_V K_(X,V)`.

Der volle normalisierte Schurfaktor

```math
F_V=\widehat B_V^{1/2}K_{X,V}G_{X,V}^{-1/2}
```

ist eine Kontraktion. Für den eingefrorenen alten Beitrag gilt dagegen

```math
F_{L,V}^{\rm old}=\widehat B_V^{1/2}K_{X,L}G_{X,V}^{-1/2},
\qquad
\|F_{L,V}^{\rm old}\|
 \le c_X^{-1/2}\|K_{X,L}\|\sqrt{\eta(L,V)}=:e_{L,V}\to0.
\tag{RL29}
```

Diese Aussage erlaubt bereits den tatsächlich mit V veränderlichen
kanonisch normalisierten Eingang `G_(X,V)^(-1/2) epsilon_X`: Die feste
Quellkoerzivität kontrolliert ihn, ohne ihn gegen eine Testfunktion zu tauschen.

Für den vollständigen Rest `F_V-F_(L,V)^old` erhält man

```math
\|F_V^*F_V-(F_V-F_{L,V}^{\rm old})^*(F_V-F_{L,V}^{\rm old})\|
 \le2e_{L,V}+e_{L,V}^2\longrightarrow0.
\tag{RL30}
```

Jeder festgehaltene alte Hubanteil verschwindet also selbst in der echten
normalisierten Schurenergie. Der Rest enthält **sämtliche** Änderungen von
`Hhat(V)-Hhat(L)`, einschließlich räumlicher Geometrie und neuer Indizes;
er wird nicht stillschweigend mit dem reinen NEW-Kanal identifiziert.

RL29/RL30 lokalisieren eine verbleibende Schwierigkeit: Der volle Transport
muss den mit dem Horizont wandernden Beitrag kontrollieren. Einen festen
kompakten Außenfaktor einzufrieren und dann V->infinity zu schicken bestimmt
zwar einen anderen Grenzweg, aber nicht den vollständigen Normalbahn-Grenzwert.

## 9. Qualitativer Gegencheck ohne Primzahlsatz

Dieser zweite Beweis bestätigt RL20 ohne die quantitative Bandzählung. Es ist
eine andere Autorennachrechnung, **kein unabhängiger externer Review**.

Für jede feste Primzahl p konvergiert die ganze Zeile RL5 stark-* gegen

```math
A_p=\sqrt{(\log p)(p-1)}\sum_{k\ge1}p^{-3k/4}D_{k\log p}.
```

Die Masken gehen stark gegen I; die k-Summe ist operatornormabsolut
konvergent. Die adjungierte Formel mit umgekehrter Produktreihenfolge
liefert die starke Konvergenz der Adjunktionen. Die unendlich vielen
Primzahlen werden hier **nicht** gleichzeitig im Grenzübergang bewegt.

Schreibe `A_p=L_p+T_p` mit `L_p=sqrt(w_p)D_(log p)`.
Die gleiche Abschätzung wie RL6 zeigt `sum_p ||T_p||^2<infinity`, auch nach
Hinzufügen der endlich vielen kleinen Primzahlen.

Für jedes feste nichtnull f in L2 gilt
`<U_s f,f>->0` bei |s|->infinity: Approximiere f in L2 durch eine kompakt
getragene Funktion, deren weit verschobene Kopie disjunkten Träger hat.
Cauchy-Schwarz kontrolliert den Approximationsfehler uniform in s.
Somit `||D_(log p)f||^2->2||f||^2` bei p->infinity.

Ferner divergiert `sum_p w_p`, da `w_p>=1/p` für p>=5 und
`sum_p 1/p=infinity`. Letzteres folgt elementar: Wäre die Summe endlich,
wären die endlichen Produkte `product_(p<=N)(1-1/p)^(-1)` wegen
`-log(1-1/p)<=2/p` beschränkt. Jedes Produkt ist aber mindestens
`sum_(n<=N)1/n`, weil alle Primfaktoren dieser n höchstens N sind.
Die harmonischen Summen divergieren. Es wird kein Eulerprodukt am Rand
seines absoluten Konvergenzbereichs als endliche Gleichheit vorausgesetzt.

Daher ist `sum_p ||L_p f||^2=infinity`. Wegen
`||L_p f||^2<=2||A_p f||^2+2||T_p f||^2` folgt

```math
\sum_p\|A_p f\|^2=\infty\qquad(f\ne0).
\tag{RL31}
```

Betrachte jetzt irgendeine Folge `V_n->infinity` und
`x_n=Bhat_(V_n)g`. Die Energieidentität RL16 (mit beliebigem ambientem g)
gibt uniforme Beschränktheit von `||x_n||^2+E_(V_n)(x_n)`.
Für eine schwach konvergente Teilfolge `x_n weak->x` konvergiert jede feste
Zeile schwach: `A_(p,V_n)x_n weak->A_p x`, wegen der starken Konvergenz der
Adjunktionen. Für jede endliche Primzahlmenge F folgt durch schwache untere
Halbstetigkeit

```math
\sum_{p\in F}\|A_p x\|^2\le\sup_n\mathcal E_{V_n}(x_n)<\infty.
```

Erst jetzt F auf alle Primzahlen erweitern. RL31 erzwingt x=0.
Jede schwache Teilgrenze ist somit null, also `x_n weak->0`.
Schließlich `||x_n||^2<=Re<g,x_n>->0`, was RL20 beweist.

Dieser Beweis erklärt zugleich, warum keine gemeinsame nichttriviale
globale endliche Residualenergie-Domäne konstruiert wurde: Schon die
limitierten a=0-Zeilen haben für jeden nichtnull L2-Vektor unendliche
Gesamtenergie. Das ist eine Aussage über diesen **unnormalisierten Rest**,
nicht ein No-Go für normalisierten Terminaltransport oder Objekt X.

## 10. Direkter Autorengegencheck und neue Grenzen

| Möglicher Fehler | Kontrolle |
|---|---|
| Primzahlpotenzen als orthogonale Kanäle behandelt | Ganze a=0-Zeile verwendet; k>=2 bleibt als kohärenter Tail erhalten |
| Unbewiesene primitive Formdominierung | RL12 benutzt eine Quadratabschätzung mit explizitem uniformem Fehler RL8 |
| Resolventenvektor als altfenstergetragen angenommen | RL14 gilt für beliebiges x; seine fernen Werte werden in J_j mitgezählt |
| Überbelegung der fernen Vergleichsfenster | Positive Gewichte summieren je Band zu 1; räumliche Hüllen sind disjunkt |
| Falsches Half-Shift-Präbild oder inaktive Restmaske | RL11 prüft u=y+log(p)/2 und |u|+log(p)/2<=V explizit |
| Graphgewichte im Problem verändert | alpha/beta sind nur Testgewichte <=1 in einer Ungleichung |
| PNT für zu kurze Intervalle verlangt | Primzahlbänder haben festes Verhältnis e; gewöhnliche PNT reicht |
| Operatornormstetigkeit der Rohmasken vorausgesetzt | Quantitativer Beweis benutzt keine; qualitativer Gegencheck nur starke-* Grenzen |
| Fehlende äußere Identität der inversen Kompression | RL4 führt I-M_V mit; genau sie verbietet globale Operatornormkonvergenz |
| COND als volle Terminalmetrik ausgegeben | RL21 friert den alten Hub ausdrücklich ein; §8 behandelt den vollen Faktor getrennt |
| Falsche kanonische Reverse-Quelle | RL26 verwendet weiterhin inverse Quadratwurzel im festen Graphraum |
| V->infinity bei festem U mit BR39 verwechselt | RL15 liefert M(U,V)=0 für U<V<=2U; keine dyadische Kleinheit gewonnen |
| Globales Flagbudget aus kleinem Residualvektor gefolgert | Keine solche Folgerung; RL27/RL28 warnen vor unkontrollierter Schurform |

**Resultat:** Die global-in-V-Resolventenaussage RL17/RL20 und der exakte
feste-U-COND-Grenzwert RL22–RL27 sind ausformuliert. Die tatsächliche
Mitwachsendes-Fenster-Abschätzung, BR39, das positive Flagbudget und
B-FLAGTIGHT bleiben offen. Die bereits integrierte bedingte Orientierung
wird nicht erneut geöffnet. Kein unbedingtes C6-/Objekt-X-/RH-Ergebnis.

Zur Prüfung des nächsten Schritts ist insbesondere zu unterscheiden:
`V>>U` mit eingefrorenem Hub (jetzt kontrolliert) gegenüber
`U<V<=2U` mit der tatsächlichen kanonischen Mitbewegung (weiter offen).
Ein weiteres Experiment mit frei gewählten Bandprofilen ist hierfür kein Ersatz.

## 11. Quellen, Reviewstatus und Repositoryumfang

Die Herleitung ist neu in diesem Dokument; die folgenden Quellen liefern
Definitionen beziehungsweise den ausdrücklich bezeichneten klassischen Satz.
Der eingebundene Primzahlsatz hat keinen RH-/GC-AC-Vorbehalt.

1. [P11, volle Hub-/Rest- und Graphraumdefinitionen](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex),
   (2.5), (2.6), (3.1)–(3.5); gelesener Blob
   `6d9260d2f3e9b0f3bb463578a8530e078aa0a050`.
2. [LOCAL-O1](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md),
   gemeinsame Umgebungsraumresolvente, feste Quellkoerzivität und
   nichtkommutative Wurzelkontrolle. Der lokale Satz bleibt geprüfter Eingang.
3. [Feste-U-COND-Uniformität, CF2–CF6](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_R43_COND_FIXED_OLD_ALL_FUTURE_UNIFORMITY_2026-09-07.md),
   gelesener Blob `57ad312edcac0c9436f0ce7ca0ece109604dd0ab`.
4. [Reverse-Normal-/Schur-Reduktion, RE2–RE11](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_R43_REVERSE_NORMAL_SCHUR_EXTENSION_REDUCTION_2026-09-06.md),
   gelesener Blob `422f58613a79fd434c88c90866b82a1822f9bf9e`.
5. [Primzahlsatz, NIST DLMF §27.12](https://dlmf.nist.gov/27.12),
   ausschließlich pi(x)~x/log x für die Bandzählung in §4. Die auf derselben
   Seite getrennt dargestellten RH-äquivalenten Fehlerabschätzungen werden
   nicht verwendet.
6. [Eulerprodukte, NIST DLMF §27.4](https://dlmf.nist.gov/27.4),
   Hintergrund zur in §9 direkt bewiesenen endlichen Produktargumentation.
   Kein analytischer Eulerprodukt-Grenzübergang bei Re(s)=1 wird benötigt.

Der Autorengegencheck ist kein externer Review. Eine Markdown-/Steuerzeichen-
und Hashkontrolle oder die rationale Prüfung der Konstante in RL7 wäre nur
technische Integritätsprüfung, kein Zertifikat für die unendlichdimensionalen
Sätze. Genau eine neue Beweisdatei ist zur Draft-Aufnahme vorgesehen;
vorhandene Beweise, aktive Registry und main bleiben unverändert.
