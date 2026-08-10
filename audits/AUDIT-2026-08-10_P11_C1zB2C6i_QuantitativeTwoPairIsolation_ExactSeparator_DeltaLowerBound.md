# P11-C1z-B2-C6i — Quantitativer Zwei-Paar-Isolationssatz, exakter Separator und explizite Δ-Untergrenze

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6i]`  
**Direkte Voraussetzungen:** C1z-B2-C3, C1z-B2-C6e, C1z-B2-C6f, C1z-B2-C6g, C1z-B2-C6h  
**Strukturelle Schnittstellen:** C1z-B, C1z-B2-C4, C1z-B2-C6a, C1z-B2-C6b, C1z-B2-C6c, C1z-B2-C6d  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d Jet-Alignment-Firewall  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6i]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm corr,rest/hub\text{-}ratio}
+
\checkmark[M]_{\rm corr,\lambda_T\text{-}asymptotic\text{-}unproved}
+
\checkmark[M]_{\rm neg,opposite\text{-}boundary\text{-}hub\text{-}smallness}
+
\checkmark[M]_{\rm pos,quantitative\text{-}two\text{-}pair\text{-}isolation}
+
\checkmark[M]_{\rm pos,exact\text{-}local\text{-}separator}
+
\checkmark[M]_{\rm pos,explicit\text{-}\Delta\text{-}lower\text{-}bound}
+
?[O]_{\rm asymptotic\text{-}\Delta\text{-}classification}
+
?[O]_{\rm second\text{-}probe\text{-}jet\text{-}alignment}
}
\]

C6i löst den in C6h offen gelassenen **exakten Separator-Schritt**, aber auf einem anderen und einfacheren Weg als der zunächst vorgeschlagene Korrekturvektor

\[
\widetilde v_T
=w_T-
\frac{\langle w_T,A_T\mathbf1_T\rangle}
{\langle z_T,A_T\mathbf1_T\rangle}z_T.
\]

Ein zusätzlicher Vektor `z_T` ist nicht nötig.

Der neue Kern ist, den bereits in C6e verwendeten Zwei-Paar-Trick `(2,3)/(2,5)` **quantitativ** auszuwerten. Für jedes hinreichend große `T` besitzt mindestens eine der beiden kanonischen Cross-Prime-Kanten

\[
x_3(T)=T-\frac12\log(3/2),
\qquad
x_5(T)=T-\frac12\log(5/2)
\]

einen echten `A_T\mathbf1_T`-freien Radius von Größe

\[
\boxed{
\rho_T^A\ge c_A e^{-4T}.
}
\tag{C1zB2C6i.1}
\]

Auf diesem kleineren Fenster kann der ursprüngliche Haarseparator exakt benutzt werden:

\[
\boxed{
v_T
=
1_{(x_T-r_T,x_T)}
-
1_{(x_T,x_T+r_T)},
\qquad
r_T=c e^{-4T},
}
\tag{C1zB2C6i.2}
\]

mit

\[
\boxed{
\langle v_T,A_T\mathbf1_T\rangle=0.
}
\tag{C1zB2C6i.3}
\]

C6g garantiert wegen Monotonie der gewichteten Hub-Crowding-Masse zugleich

\[
\boxed{
|\langle v_T,h_T\rangle|
\ge c_h e^{-4T},
\qquad
h_T:=H_T^*H_T\mathbf1_T.
}
\tag{C1zB2C6i.4}
\]

Mit C6fs globalem Operatorbound

\[
\|R_T\|^2\le C_RTe^T
\]

folgt schließlich die erste vollständig explizite quantitative Untergrenze für den zweiten Krylov-Defekt:

\[
\boxed{
\Delta_T^{(1)}
\ge
c_\Delta\frac{e^{-5T}}{T}
\qquad(T\gg1).
}
\tag{C1zB2C6i.5}
\]

Diese Untergrenze tendiert selbst gegen null. Sie beweist daher **nicht**, dass die zweite Probe asymptotisch uniform stabil ist. Sie klassifiziert `\Delta_T^{(1)}` auch nicht. Sie ist aber eine echte, horizontexplizite Verbesserung gegenüber C6es rein qualitativer Positivität und C6fs `\rho_T`-abhängiger Schranke.

---

# 0. Reconciliation: zwei Korrekturen vor dem Beweis

## 0.1 Das C6h-Verhältnis war in der Gegenprüfer-Vorüberlegung invertiert

C6h beweist

\[
\boxed{
\frac{
|\langle w_T,A_T\mathbf1_T\rangle|
}{
|\langle w_T,h_T\rangle|
}
\le
CT^2e^{-T}
\to0.
}
\tag{C1zB2C6i.6}
\]

Die operative Aussage lautet also

\[
\boxed{
\text{Rest/Hub}\to0,
}
\]

nicht `Hub/Rest -> 0`.

Die konzeptuelle Interpretation aus C6h — der Hub dominiert auf der Cross-Prime-Kante die Restmetrik — bleibt damit unverändert richtig.

Status:

\[
\boxed{\checkmark[M]_{\rm corr,rest/hub\text{-}ratio}.}
\]

## 0.2 `\lambda_T\asymp Te^T` ist aus dem bisherigen Strang nicht bewiesen

C6h definiert

\[
\lambda_T
=
\frac{\|H_T\mathbf1_T\|^2}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}.
\tag{C1zB2C6i.7}
\]

Die totale Odd-Divergenz aus C5/C6a betrifft dagegen die Zukunftsmetrik auf **festen alten Odd-Sourcevektoren**. Sie liefert keine Asymptotik für den terminalen Rayleighquotienten (C1zB2C6i.7).

C3 beweist für die Konstantenmode nur insbesondere

\[
\langle\mathbf1_T,A_T\mathbf1_T\rangle=O(T^2),
\]

und benutzt ihre Hubkopplung an feste alte Sourcevektoren. Daraus folgt nicht

\[
\lambda_T\asymp Te^T.
\]

C6i verwendet deshalb **keine** solche Asymptotik.

Status:

\[
\boxed{\checkmark[M]_{\rm corr,\lambda_T\text{-}asymptotic\text{-}unproved}.}
\]

## 0.3 Warum ein Korrekturvektor nahe `-T` nicht automatisch hubarm ist

Aus der Paritätsstruktur von C6e gilt

\[
H_T\mathbf1_T\text{ ungerade},
\qquad
h_T=H_T^*H_T\mathbf1_T\text{ gerade}.
\]

Daher besitzt die linke Terminalseite keine durch Parität erzwungene kleinere `h_T`-Struktur als die rechte.

Insbesondere ist der heuristische Schluss

\[
\text{„}z_T\text{ liegt nahe }-T
\Rightarrow
\langle z_T,h_T\rangle\text{ klein“}
\]

nicht zulässig.

Dies ist kein No-Go gegen jede denkbare linke Randkorrektur. Negativ ist nur genau dieses Distanz-/Paritätsargument.

Status:

\[
\boxed{\checkmark[M]_{\rm neg,opposite\text{-}boundary\text{-}hub\text{-}smallness}.}
\]

---

# 1. Verbindliche Daten aus C6e–C6h

Setze

\[
A_T:=I+R_T^*R_T,
\qquad
h_T:=H_T^*H_T\mathbf1_T.
\]

C6e liefert für

\[
q\in\{3,5\}
\]

die beiden kanonischen Hubkanten

\[
\boxed{
x_q(T)=T-\frac12\log(q/2).}
\tag{C1zB2C6i.8}
\]

Für beide gilt eventual

\[
\boxed{
|\operatorname{Jump}_{x_q(T)}h_T|
\ge j_*>0.
}
\tag{C1zB2C6i.9}
\]

C6g verbessert dies robust: Für jede feste `0<theta<1` existiert

\[
R_T^{\rm hub}=c_\theta\frac{e^{-T}}T
\]

mit

\[
\boxed{
\mathcal V^{h,\mathrm{off}}_{T,q}(R_T^{\rm hub})
\le\theta j_*
}
\tag{C1zB2C6i.10}
\]

für beide `q=3,5` und großes `T`.

C6h typisiert die Rest-Breakpoints. Sämtliche Sprungstellen von

\[
A_T\mathbf1_T
=\mathbf1_T+R_T^*R_T\mathbf1_T
\]

liegen in der prime-puren Menge

\[
\boxed{
\mathcal B_T^A
\subseteq
\bigcup_p
\left\{
\pm T+\frac m2\log p:m\in\mathbb Z
\right\}\cap(-T,T).
}
\tag{C1zB2C6i.11}
\]

Rechtsseitige prime-pure Gitter besitzen um `x_3,x_5` sogar einen festen Abstand. Für einen exponentiell kleinen Radius muss deshalb nur die gegenüberliegende Familie

\[
\boxed{
y_{p,m}(T)=-T+\frac m2\log p}
\tag{C1zB2C6i.12}
\]

betrachtet werden.

---

# 2. Quantitative Zwei-Paar-Separation

Definiere

\[
X_{q,T}:=\frac2q e^{4T}.
\tag{C1zB2C6i.13}
\]

Für einen gegenüberliegenden prime-puren Gitterpunkt

\[
y_{p,m}(T)=-T+\frac m2\log p
\]

gilt exakt

\[
\begin{aligned}
|x_q(T)-y_{p,m}(T)|
&=
\left|
2T-\frac12\log\left(\frac q2p^m\right)
\right|\\
&=
\frac12
\left|
\log\frac{X_{q,T}}{p^m}
\right|.
\end{aligned}
\tag{C1zB2C6i.14}
\]

Der qualitative C6e-Zwei-Paar-Trick schloss nur die **gleichzeitige exakte** Koinzidenz für `q=3` und `q=5` aus.

C6i quantifiziert nun denselben Mechanismus.

## Lemma C1zB2C6i.1 — quantitative Zwei-Paar-Separation

Es existieren `T_0<infty` und `c_A>0`, so dass für jedes `T>=T_0` mindestens eines der beiden `q in {3,5}` die Eigenschaft besitzt:

\[
\boxed{
\operatorname{dist}
\left(
 x_q(T),
 \bigcup_{p,m\ge1}
 \left\{-T+\frac m2\log p\right\}
\right)
\ge
c_Ae^{-4T}.
}
\tag{C1zB2C6i.15}
\]

### Beweis

Angenommen, beide Distanzen seien kleiner als ein Radius `r`, der später gewählt wird.

Dann existieren Prime Powers

\[
a=p^m,
\qquad
b=s^n
\]

mit

\[
\left|\log\frac{X_{3,T}}a\right|<2r,
\qquad
\left|\log\frac{X_{5,T}}b\right|<2r.
\tag{C1zB2C6i.16}
\]

Also kann man schreiben

\[
a=X_{3,T}e^{\alpha},
\qquad
b=X_{5,T}e^{\beta},
\qquad
|\alpha|,|\beta|<2r.
\]

Da

\[
\frac{X_{3,T}}{X_{5,T}}=\frac53,
\]

folgt

\[
\boxed{
\frac ab
=\frac53e^{\eta},
\qquad
\eta:=\alpha-\beta,
\qquad
|\eta|<4r.
}
\tag{C1zB2C6i.17}
\]

Damit

\[
3a=5be^{\eta}.
\]

Falls

\[
3a=5b,
\]

liefert eindeutige Primfaktorzerlegung wie in C6e

\[
a=5,
\qquad
b=3.
\]

Für großes `T` ist dies mit (C1zB2C6i.16) unmöglich, weil

\[
X_{3,T},X_{5,T}\to\infty.
\]

Also gilt für großes `T`

\[
3a-5b\in\mathbb Z\setminus\{0\}
\]

und daher

\[
1\le|3a-5b|
=5b|e^{\eta}-1|.
\tag{C1zB2C6i.18}
\]

Für `r<=1/8` ist `|\eta|<=1/2`, also

\[
|e^{\eta}-1|\le2|\eta|\le8r.
\]

Somit

\[
1\le40br.
\tag{C1zB2C6i.19}
\]

Andererseits folgt aus (C1zB2C6i.16)

\[
b\le e^{2r}X_{5,T}
\le2X_{5,T}
=\frac45e^{4T}
\]

für großes `T` und kleines `r`.

Daher

\[
1\le32e^{4T}r.
\]

Also muss

\[
\boxed{
r\ge\frac1{32}e^{-4T}.}
\tag{C1zB2C6i.20}
\]

Wählt man etwa

\[
c_A:=\frac1{64},
\]

können nicht **beide** Distanzen kleiner als `c_Ae^{-4T}` sein.

Damit besitzt mindestens eines der beiden `q` die behauptete Separation. `□`

### Scope

Der Beweis benutzt keine quantitative Irrationalität von Logarithmen, keinen PNT und keinen Siebsatz.

Er benutzt nur:

1. die exakten prime-puren Gitter aus C6h;
2. den C6e-Zwei-Paar-Ansatz;
3. eindeutige Primfaktorzerlegung;
4. die triviale Ganzzahllücke
   \[
   |3a-5b|\ge1.
   \]

Status:

\[
\boxed{\checkmark[M]_{\rm pos,quantitative\text{-}two\text{-}pair\text{-}isolation}.}
\]

---

# 3. Auswahl der quantitativ isolierten kanonischen Kante

Für jedes hinreichend große `T` wähle

\[
q_T\in\{3,5\}
\]

so, dass Lemma C1zB2C6i.1 gilt, und setze

\[
\boxed{x_T:=x_{q_T}(T).}
\tag{C1zB2C6i.21}
\]

C6h zeigt zusätzlich, dass rechtsseitige prime-pure Gitter einen festen Abstand von beiden `x_q(T)` besitzen. Daher kann nach eventueller Verkleinerung von `c_A` aus (C1zB2C6i.15) auf die **gesamte tatsächliche Rest-Breakpoint-Menge** geschlossen werden:

\[
\boxed{
\operatorname{dist}(x_T,\mathcal B_T^A)
\ge c_Ae^{-4T}.
}
\tag{C1zB2C6i.22}
\]

Definiere

\[
\boxed{
r_T:=\frac{c_A}{2}e^{-4T}.}
\tag{C1zB2C6i.23}
\]

Dann besitzt

\[
A_T\mathbf1_T
\]

auf dem gesamten Intervall

\[
(x_T-r_T,x_T+r_T)
\]

keinen Sprung und ist dort als Stufenfunktion konstant.

Wichtig: Es wird **nicht** behauptet, dass `A_T\mathbf1_T` dort verschwindet oder positiv ist. Für den Haarseparator genügt die Konstanz.

---

# 4. Der ursprüngliche Haarseparator ist wieder exakt

Setze

\[
\boxed{
v_T
:=
1_{(x_T-r_T,x_T)}
-
1_{(x_T,x_T+r_T)}.
}
\tag{C1zB2C6i.24}
\]

Dann

\[
\boxed{\|v_T\|^2=2r_T.}
\tag{C1zB2C6i.25}
\]

Da `A_T\mathbf1_T` auf beiden gleich langen Halbintervallen denselben konstanten Wert besitzt,

\[
\boxed{
\langle v_T,A_T\mathbf1_T\rangle=0.
}
\tag{C1zB2C6i.26}
\]

Damit ist der in C6h geforderte exakte Korrekturschritt geschlossen — nicht durch Addition eines `z_T`, sondern durch einen quantitativ isolierten Radius.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,exact\text{-}local\text{-}separator}.}
\]

---

# 5. Die Hubpaarung bleibt auf dem kleineren Fenster robust

Wähle in C6g beispielsweise

\[
\theta=\frac14.
\]

Dann existiert

\[
R_T^{\rm hub}=c_h'\frac{e^{-T}}T
\]

so dass für beide `q=3,5`

\[
\mathcal V^{h,\mathrm{off}}_{T,q}(R_T^{\rm hub})
\le\frac14j_*.
\tag{C1zB2C6i.27}
\]

Da

\[
r_T\asymp e^{-4T}
\ll
\frac{e^{-T}}T,
\]

gilt für großes `T`

\[
r_T<R_T^{\rm hub}.
\]

Die lokale Sprungmasse ist monoton im Radius. Also

\[
\boxed{
\mathcal V^{h,\mathrm{off}}_{T,q_T}(r_T)
\le\frac14j_*.
}
\tag{C1zB2C6i.28}
\]

C6gs robuste Haarpaarungsungleichung liefert damit

\[
\begin{aligned}
|\langle v_T,h_T\rangle|
&\ge
r_T
\left(
|\operatorname{Jump}_{x_T}h_T|
-
\mathcal V^{h,\mathrm{off}}_{T,q_T}(r_T)
\right)\\
&\ge
r_T\left(j_*-\frac14j_*\right).
\end{aligned}
\]

Somit

\[
\boxed{
|\langle v_T,h_T\rangle|
\ge
\frac34j_*r_T
\ge
c_h e^{-4T}.
}
\tag{C1zB2C6i.29}
\]

Kein `\lambda_T` tritt auf, weil (C1zB2C6i.26) exakt gilt.

---

# 6. Kontrolle der `A_T`-Energie

C6f beweist

\[
\boxed{
\|R_T\|^2\le C_RTe^T.
}
\tag{C1zB2C6i.30}
\]

Daher als Operatorungleichung

\[
A_T
=I+R_T^*R_T
\le
(1+C_RTe^T)I.
\tag{C1zB2C6i.31}
\]

Für `v_T` folgt

\[
\begin{aligned}
\langle v_T,A_Tv_T\rangle
&\le
(1+C_RTe^T)\|v_T\|^2\\
&=
2r_T(1+C_RTe^T).
\end{aligned}
\tag{C1zB2C6i.32}
\]

Da

\[
r_T\asymp e^{-4T},
\]

gilt insbesondere

\[
\boxed{
\langle v_T,A_Tv_T\rangle
\le
C_E T e^{-3T}
}
\tag{C1zB2C6i.33}
\]

für großes `T`.

Diese Energieabschätzung ist grob, aber ausreichend. Es wird keine lokale Verbesserung von `\|R_T\|` importiert.

---

# 7. Hauptsatz — explizite Untergrenze für `\Delta_T^{(1)}`

C6d/C6e definieren

\[
\Delta_T^{(1)}
=
\langle H_T^*H_T\mathbf1_T,
A_T^{-1}H_T^*H_T\mathbf1_T\rangle
-
\frac{\|H_T\mathbf1_T\|^4}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}.
\tag{C1zB2C6i.34}
\]

C6e beweist für jeden Vektor `v` mit

\[
\langle v,A_T\mathbf1_T\rangle=0
\]

die Variationsuntergrenze

\[
\boxed{
\Delta_T^{(1)}
\ge
\frac{|\langle v,h_T\rangle|^2}
{\langle v,A_Tv\rangle}.
}
\tag{C1zB2C6i.35}
\]

Setze `v=v_T` aus (C1zB2C6i.24).

Nach (C1zB2C6i.29) ist der Zähler mindestens

\[
c_h^2e^{-8T}.
\]

Nach (C1zB2C6i.33) ist der Nenner höchstens

\[
C_ETe^{-3T}.
\]

Folglich:

## Satz C1zB2C6i.2 — quantitative Zweitprobe-Nichtdegeneration

Es existieren `T_1<infty` und `c_\Delta>0`, so dass für alle `T>=T_1`

\[
\boxed{
\Delta_T^{(1)}
\ge
c_\Delta\frac{e^{-5T}}T.
}
\tag{C1zB2C6i.36}
\]

`□`

Status:

\[
\boxed{\checkmark[M]_{\rm pos,explicit\text{-}\Delta\text{-}lower\text{-}bound}.}
\]

---

# 8. Konsequenz für den `N=1`-Hankeldeterminanten

C6d/C6e geben

\[
\det\mathbf K_T^{(1)}
=\mu_{T,0}\Delta_T^{(1)},
\qquad
\mu_{T,0}
=\langle\mathbf1_T,A_T\mathbf1_T\rangle.
\tag{C1zB2C6i.37}
\]

Da

\[
A_T\ge I,
\]

gilt

\[
\mu_{T,0}\ge\|\mathbf1_T\|^2=2T.
\]

Mit Satz C1zB2C6i.2 folgt daher

\[
\boxed{
\det\mathbf K_T^{(1)}
\ge
c_K e^{-5T}
}
\tag{C1zB2C6i.38}
\]

für großes `T`.

Dies ist die erste vollständig horizontexplizite Determinantenuntergrenze im `N=1`-Krylov-Scope.

---

# 9. Was die neue Untergrenze bedeutet — und was nicht

Der Satz

\[
\Delta_T^{(1)}
\ge c_\Delta e^{-5T}/T
\]

ist quantitativ echt, aber bewusst schwach.

Er zeigt:

1. Der C6e-Rang-2-Befund besitzt eine explizite horizonabhängige Nichtdegenerationsreserve.
2. Die Reserve kommt aus einer rein arithmetisch-geometrischen Separation, nicht aus Generizität.
3. Der bislang abstrakte Isolationsradius aus C6f kann im Zwei-Kandidaten-Scope explizit durch `e^{-4T}` ersetzt werden.

Er zeigt **nicht**:

\[
\inf_{T\gg1}\Delta_T^{(1)}>0.
\]

Er zeigt auch nicht

\[
\Delta_T^{(1)}\to0.
\]

Eine untere Schranke, die selbst gegen null geht, klassifiziert die tatsächliche Asymptotik nicht.

Ebenso folgt daraus keine uniforme Stabilität des normierten zweiten Krylov-Vektors

\[
\widehat\psi_{T,1}.
\]

Die in C6f formulierte Degenerationsmöglichkeit bleibt logisch offen.

---

# 10. Verhältnis zu C6f–C6h

## C6f

C6f zeigte

\[
\Delta_T^{(1)}
\ge
c_*\frac{\rho_T}{1+C_*Te^T}
\]

für einen punktweisen Isolationsradius `\rho_T`, konnte diesen aber aus einer einzelnen Kante nicht quantitativ kontrollieren.

C6i präzisiert diesen Befund:

- für **eine fest vorgegebene** Kante `x_3` oder `x_5` bleibt ein uniformer quantitativer Abstand weiterhin nicht bewiesen;
- im **adaptiven Zwei-Kandidaten-Scope** erzwingt die Ganzzahllücke `|3a-5b|>=1` jedoch
  \[
  \max\{\rho_{T,3}^A,\rho_{T,5}^A\}
  \gtrsim e^{-4T}.
  \]

Dies widerspricht C6f nicht. C6f schloss nur einen uniform positiven Radius bzw. eine Kontrolle aus bloßer Einzel-Support-Nichtkoinzidenz aus.

## C6g

C6g kontrolliert Hub-Crowding auf dem größeren Radius

\[
e^{-T}/T.
\]

C6i benutzt lediglich die Monotonie dieser Kontrolle auf dem kleineren Radius

\[
e^{-4T}.
\]

Es wird keine neue Hub-Summation benötigt.

## C6h

C6h schloss die gewichtete Rest-Crowding-Seite und zeigte approximate `A_T\mathbf1_T`-Annihilation auf `e^{-T}/T`.

C6i benötigt für den exakten Separator nicht einmal diese quantitative Rest-BV-Schranke. Es benutzt aus C6h stattdessen die **prime-pure Typisierung der Rest-Breakpoints** und den festen Abstand der rechtsseitigen Gitter.

Damit besitzt C6h zwei bleibende Rollen:

1. strukturell: Restseite ist prime-pure und exakt typisiert;
2. analytisch: auf dem größeren C6g-Fenster ist Rest/Hub asymptotisch klein.

C6i ergänzt diese Aussagen um einen kleineren, aber exakt breakpointfreien Zwei-Kandidaten-Radius.

---

# 11. Supersession-Scope

C6i supersediert in C6h den offenen Punkt

\[
?[O]_{\rm corrected\text{-}separator}
\]

im folgenden präzisen Sinn:

\[
\boxed{
\text{Ein exakt }A_T\mathbf1_T\text{-orthogonaler lokaler Separator existiert mit explizitem Radius }r_T\asymp e^{-4T}.
}
\tag{C1zB2C6i.39}
\]

Es wird **nicht** bewiesen, dass der ursprünglich vorgeschlagene additive Korrekturvektor `z_T` mit Radius `e^{-T}/T` funktioniert.

Der größere robuste C6g/C6h-Radius bleibt analytisch interessant, insbesondere für eine spätere Verbesserung der `\Delta`-Skala.

---

# 12. No-Go-Persistenzmatrix

| Früherer Knoten | Gesiegelter Befund | Wirkung in C6i |
|---|---|---|
| C1y | translationsinvariante Regulatoren lösen den Hub/Rest-Konflikt im C1y-Scope nicht | unverändert |
| B2-A | Gamma-Präkonditionierung liefert keinen finite Schattenmechanismus | unverändert |
| B2-B | naiver Haar-`L^2`-Endpunkt reicht nicht | unverändert |
| C4 | unendliche Boundary-Jet-Hierarchie | unverändert |
| C5/C6a | totale Odd-Divergenz | unverändert; keine `lambda_T`-Asymptotik daraus abgeleitet |
| C6 | kein voller Odd-Transport durch festen endlichen Jetquotienten | unverändert |
| C6a | Self-Grams allein reichen nicht | unverändert |
| C6b | C2-Flachheit allein reicht nicht | unverändert |
| C6c | `tau=>kappa` auf festem Fenster | unverändert |
| C6c | Triangularität allein reicht nicht | unverändert |
| C6d | C4-Jets sind keine automatischen Multi-Probes | unverändert |
| C6e | eventualer Krylov-Rang 2 | quantitativ verstärkt |
| C6f | Einzel-Breakpoint-Support allein liefert keinen uniform positiven Radius | unverändert; C6i benutzt zwei Kandidaten + Ganzzahllücke |
| C6g | elementares Hub-Crowding | direkt benutzt |
| C6h | elementares Rest-Crowding / Rest-Hub-Trennung | bleibt positiv; Separator-Open wird im kleineren Radius geschlossen |

---

# 13. Was C6i ausdrücklich nicht beweist

Nicht bewiesen sind:

- eine scharfe Asymptotik von `\Delta_T^{(1)}`;
- `\Delta_T^{(1)}\to0`;
- `\inf_T\Delta_T^{(1)}>0`;
- `\Delta_T^{(1)}\to\infty`;
- eine optimale exponentielle Rate in der Untergrenze;
- eine lokale Verbesserung des C6f-Bounds `\|R_T\|^2<=CTe^T` auf `v_T`;
- Funktionieren des additiven `z_T`-Korrektors auf dem größeren Radius `e^{-T}/T`;
- eine bewiesene Asymptotik für `\lambda_T`;
- uniforme Stabilität von `\widehat\psi_{T,1}`;
- Jet-Alignment der zweiten Probe;
- eine Untergrenze für `s_{\min}(\mathcal P_T^{(1)})`;
- `\varepsilon_T^{\rm probe}(R,1)\to0`;
- `\tau_T(E_{R,1})\to0`;
- `\Theta_{T,U}^{E_{R,1}}\to I`;
- Krylov-Rang `N>=2`.

---

# 14. Exakter nächster Arbeitsauftrag C6j

Nach C6i ist die Existenz eines quantitativ expliziten exakten Separators im `N=1`-Scope erledigt.

Der nächste sinnvolle Knoten sollte **nicht** erneut die Existenz der zweiten Probe untersuchen.

Es gibt zwei mögliche Richtungen; die atomarere ist:

\[
\boxed{
\text{C6j: lokale Energieverbesserung des exakten }e^{-4T}\text{-Separators.}
}
\tag{C1zB2C6i.40}
\]

Der aktuelle Nenner verwendet nur den globalen C6f-Bound

\[
\langle v_T,A_Tv_T\rangle
\le
(1+CTe^T)\|v_T\|^2.
\]

Dieser ist wahrscheinlich sehr grob für einen extrem randnahen, sehr kurzen Haarvektor.

C6j sollte daher direkt die konkrete konditionierte Restformel auf `v_T` auswerten und prüfen, ob

\[
\|R_Tv_T\|^2
\]

deutlich kleiner als

\[
CTe^T\|v_T\|^2
\]

ist.

Jede Verbesserung

\[
\langle v_T,A_Tv_T\rangle
\le E_T
\]

verbessert unmittelbar

\[
\Delta_T^{(1)}
\ge
c e^{-8T}/E_T.
\]

Erst danach sollte entschieden werden, ob der größere C6g/C6h-Radius `e^{-T}/T` mit einem echten Korrekturvektor nochmals verfolgt wird oder ob bereits der `2x2`-Jet-Alignment-Test sinnvoll wird.

### Firewall für C6j

Die globale Normschranke `||R_T||^2<=CTe^T` darf nicht als lokale Asymptotik interpretiert werden.

Eine Verbesserung muss aus der tatsächlichen source-gekoppelten Restformel auf dem konkreten `v_T` folgen.

---

# 15. Endurteil

C6i schließt den exakten Separator-Engpass im `N=1`-Scope durch eine quantitative Version des C6e-Zwei-Paar-Tricks.

Der arithmetische Kern ist:

\[
\boxed{
|3a-5b|\ge1
}
\]

für die beiden nahe den Zielwerten

\[
a\approx\frac23e^{4T},
\qquad
b\approx\frac25e^{4T}
\]

liegenden Prime Powers, sofern nicht die für großes `T` ausgeschlossene exakte C6e-Kollision vorliegt.

Dadurch gilt adaptiv für mindestens eine der beiden Kanten

\[
\boxed{
\operatorname{dist}(x_{q_T}(T),\mathcal B_T^A)
\gtrsim e^{-4T}.
}
\]

Auf diesem Radius ist der Haarseparator exakt `A_T\mathbf1_T`-orthogonal, während C6gs Hub-Crowding-Kontrolle wegen Radiusmonotonie erhalten bleibt.

Zusammen mit C6fs globaler Restnorm ergibt sich

\[
\boxed{
\Delta_T^{(1)}
\ge
c_\Delta\frac{e^{-5T}}T.
}
\]

Damit ist C6es qualitative eventuale Rang-2-Aussage erstmals mit einer vollständig expliziten horizonabhängigen Nichtdegenerationsreserve versehen.

Die tatsächliche asymptotische Stabilität der zweiten Probe bleibt offen.