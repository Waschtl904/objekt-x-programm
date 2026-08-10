# P11-C1z-B2-C6j — Lokale Separatorenergie, Prime-Power-Disjunktheit und Chebyshev-Verbesserung

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6j]`  
**Direkte Voraussetzungen:** C1z-B, C1z-B2-C3, C1z-B2-C6f, C1z-B2-C6g, C1z-B2-C6h, C1z-B2-C6i  
**Strukturelle Schnittstellen:** C1z-B2-C4, C1z-B2-C6a, C1z-B2-C6b, C1z-B2-C6c, C1z-B2-C6d  
**Neues arithmetisches Werkzeug:** elementare Chebyshev-Schranke `psi(X) << X`; **kein PNT**, keine Siebtheorie  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d Jet-Alignment-Firewall  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6j]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm corr,boundary\text{-}layer\text{-}geometry}
+
\checkmark[M]_{\rm pos,right\text{-}translate\text{-}killed}
+
\checkmark[M]_{\rm pos,k\text{-}pulse\text{-}disjointness}
+
\checkmark[M]_{\rm pos,local\text{-}rest\text{-}energy}
+
\checkmark[M]_{\rm pos,Chebyshev\text{-}scope}
+
\checkmark[M]_{\rm pos,improved\text{-}\Delta\text{-}lower\text{-}bound}
+
?[O]_{\rm asymptotic\text{-}\Delta\text{-}classification}
+
?[O]_{\rm second\text{-}probe\text{-}jet\text{-}alignment}
}
\]

C6j verbessert den C6i-Nenner exakt in der vom Gegenprüfer vorgeschlagenen Richtung.

Für den exakten C6i-Separator

\[
\boxed{
v_T
=
1_{(x_T-r_T,x_T)}
-
1_{(x_T,x_T+r_T)},
\qquad
r_T=c_0e^{-4T},
}
\tag{C1zB2C6j.1}
\]

mit

\[
x_T=x_{q_T}(T),
\qquad q_T\in\{3,5\},
\]

gilt nicht nur die globale C6f-Schranke

\[
\langle v_T,A_Tv_T\rangle
\lesssim
T e^{-3T},
\]

sondern die lokale Verbesserung

\[
\boxed{
\langle v_T,A_Tv_T\rangle
\le
C_Ae^{-3T}.
}
\tag{C1zB2C6j.2}
\]

Damit verschwindet der bisherige Polynomfaktor `T`.

Zusammen mit C6is exakter Orthogonalität

\[
\langle v_T,A_T\mathbf1_T\rangle=0
\]

und der robusten Hubpaarung

\[
|\langle v_T,h_T\rangle|
\ge c_he^{-4T},
\qquad h_T=H_T^*H_T\mathbf1_T,
\]

folgt die verbesserte explizite Untergrenze

\[
\boxed{
\Delta_T^{(1)}
\ge
c_\Delta e^{-5T}
\qquad(T\gg1).
}
\tag{C1zB2C6j.3}
\]

und damit

\[
\boxed{
\det\mathbf K_T^{(1)}
\ge
c_K T e^{-5T}.
}
\tag{C1zB2C6j.4}
\]

Die Untergrenze (C1zB2C6j.3) tendiert weiterhin gegen null. C6j beweist daher **nicht** `Delta_T^(1) -> 0` und auch keine asymptotische Äquivalenz.

Der neue Mechanismus ist strukturell wichtig:

- der C6i-Haarvektor liegt in einer festen rechten **Randlage** `T-O(1)`;
- nach Anwendung von `D_{k log p}` entstehen zwei verschobene Pulse;
- die source-gekoppelte Conditional Expectation tötet den nach rechts verschobenen Puls vollständig;
- die nach links verschobenen `k`-Pulse sind für festes `p` wegen `r_T << log 2` disjunkt;
- damit entfällt genau der `K_p(T)`-Cauchy-Schwarz-Verlust aus C6f;
- die verbleibende Prime-Power-Summe ist eine gewichtete von-Mangoldt-Summe und wird durch die elementare Chebyshev-Schranke `psi(X) << X` kontrolliert.

---

# 0. Reconciliation und Scope

## 0.1 Korrektur: `x_T` liegt in einer festen Randlage

Für

\[
q\in\{3,5\}
\]

setze

\[
c_q:=\frac12\log(q/2)>0.
\]

Dann

\[
\boxed{x_q(T)=T-c_q.}
\tag{C1zB2C6j.5}
\]

Der Separator liegt daher **nicht** weit im Inneren des Terminalfensters. Sein Abstand vom rechten Rand ist die feste Konstante `c_q`.

Was lokal ist, ist seine Breite

\[
2r_T\asymp e^{-4T}.
\]

Status:

\[
\boxed{\checkmark[M]_{\rm corr,boundary\text{-}layer\text{-}geometry}.}
\]

Diese Korrektur ist wichtig, weil `R_Tv_T` nicht durch die Tiefe am Mittelpunkt `x_T` allein kontrolliert werden darf: die Differenzen `D_{k log p}` verschieben den Puls über große Distanzen.

## 0.2 Verbindlicher Restoperator

Wie in C6h:

\[
R_T
=
\bigoplus_pR_{p,T},
\]

mit

\[
\boxed{
R_{p,T}f(u)
=
\sum_{k\ge1}
 b_{p,k}
 D_{k\log p}E_Tf(u)
\,q_{p,k,T}(u),
\qquad
b_{p,k}=\sqrt{\log p}\,p^{-k/4}.
}
\tag{C1zB2C6j.6}
\]

Die Restmarke ist

\[
q_{p,k,T}(u)
=
\sqrt{p-1}
\sum_{a=0}^{\min(k-1,J_{p,T}(u)-1)}
 p^{(a-k)/2}\psi_{p,a},
\]

mit

\[
J_{p,T}(u)
=
\max\left\{0,
\left\lfloor
\frac{2(T-|u|)_+}{\log p}
\right\rfloor
\right\}.
\tag{C1zB2C6j.7}
\]

Für `J:=J_{p,T}(u)` gilt daher exakt

\[
\|q_{p,k,T}(u)\|^2
=
\begin{cases}
0,&J=0,\\[1mm]
1-p^{-k},&J\ge k,\\[1mm]
p^{J-k}-p^{-k},&1\le J<k.
\end{cases}
\tag{C1zB2C6j.8}
\]

Insbesondere

\[
\boxed{
\|q_{p,k,T}(u)\|^2
\le
\min\{1,p^{J-k}\}.
}
\tag{C1zB2C6j.9}
\]

## 0.3 Neues Werkzeug: Chebyshev, nicht PNT

C6j benutzt erstmals die klassische elementare Schranke

\[
\boxed{
\psi(X)
:=
\sum_{n\le X}\Lambda(n)
\le
C_\psi X
\qquad(X\ge2).
}
\tag{C1zB2C6j.10}
\]

Hier ist

\[
\Lambda(p^k)=\log p
\]

und `Lambda(n)=0` sonst.

Dies ist die Chebyshev-Schranke und deutlich schwächer als der Primzahlsatz. C6j deklariert sie ausdrücklich als **neues arithmetisches Input**.

Es wird nicht benutzt:

\[
\psi(X)\sim X,
\qquad
\pi(X)\sim\frac X{\log X},
\]

oder irgendeine Siebabschätzung.

---

# 1. Geometrie der beiden verschobenen Pulse

Fixiere vorübergehend eines der beiden `q in {3,5}` und setze

\[
x=T-c_q.
\]

Sei

\[
v=v_{T,q,r}
=
1_{(x-r,x)}-1_{(x,x+r)},
\qquad
0<r\le r_T.
\]

Dann

\[
\|v\|_2^2=2r.
\tag{C1zB2C6j.11}
\]

Für

\[
s=k\log p
\]

ist

\[
D_sE_Tv(u)
=
v(u+s/2)-v(u-s/2).
\tag{C1zB2C6j.12}
\]

Die beiden möglichen Träger liegen daher um

\[
\boxed{
u^-_{p,k}=x-\frac{k}{2}\log p}
\tag{C1zB2C6j.13}
\]

und

\[
\boxed{
u^+_{p,k}=x+\frac{k}{2}\log p.}
\tag{C1zB2C6j.14}
\]

Jeder Puls besitzt Länge `2r`.

---

# 2. Der nach rechts verschobene Puls wird exakt ausgelöscht

Dies ist der erste lokale Gewinn.

## Lemma C1zB2C6j.1 — right-translate kill

Für alle hinreichend großen `T`, alle `q in {3,5}`, alle Primzahlen `p` und alle `k>=1` gilt auf dem rechten Translationspuls

\[
q_{p,k,T}(u)=0.
\]

Soweit der Puls überhaupt das Terminalfenster schneidet, trägt also

\[
v(u-k\log p/2)
\]

nicht zu `R_{p,T}v` bei.

### Beweis

Sei `u` im Träger des nach rechts verschobenen Pulses. Dann

\[
T-u
\le
c_q-rac{k}{2}\log p+r.
\tag{C1zB2C6j.15}
\]

Falls `q_{p,k,T}(u) != 0`, muss mindestens

\[
J_{p,T}(u)\ge1
\]

gelten.

Da ein im Terminalfenster liegender rechter Puls für großes `T` nahe `+T` liegt, ist `u>0`, und damit folgt notwendig

\[
T-u\ge\frac12\log p.
\]

Zusammen mit (C1zB2C6j.15):

\[
c_q+r
\ge
\frac{k+1}{2}\log p
\ge
\log2.
\tag{C1zB2C6j.16}
\]

Aber

\[
\max\{c_3,c_5\}
=
\frac12\log(5/2)
<
\log2.
\]

Da `r_T -> 0`, ist (C1zB2C6j.16) für großes `T` unmöglich.

Also `q_{p,k,T}(u)=0`. `□`

Status:

\[
\boxed{\checkmark[M]_{\rm pos,right\text{-}translate\text{-}killed}.}
\]

Damit bleibt in `R_{p,T}v` nur der nach links verschobene Puls um `u^-_{p,k}`.

---

# 3. Verschiedene `k`-Pulse sind innerhalb eines Primsektors disjunkt

Für festes `p` unterscheiden sich die Mittelpunkte zweier benachbarter Linkspulse um

\[
\frac12\log p
\ge
\frac12\log2.
\]

Da

\[
r_T=c_0e^{-4T},
\]

gilt für großes `T`

\[
2r_T<\frac14\log2.
\]

Daher sind die Träger

\[
\operatorname{supp}
\left(v(\,\cdot+k\log p/2)\right)
\]

für verschiedene `k` paarweise disjunkt.

Somit gibt es **keine** `k != l`-Kreuzterme in der `L^2`-Norm von `R_{p,T}v`.

Dies ist genau der Punkt, an dem der globale C6f-Beweis zu grob war: Dort musste innerhalb eines Primsektors mit

\[
\left\|\sum_k y_{p,k}\right\|^2
\le
K_p(T)
\sum_k\|y_{p,k}\|^2
\]

gearbeitet werden. Für den C6i-Separator ist dieser Faktor nicht vorhanden.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,k\text{-}pulse\text{-}disjointness}.}
\]

---

# 4. Uniforme Markschranke auf dem Linkspuls

Sei `u` im Linkspuls um

\[
u^-_{p,k}=T-c_q-\frac{k}{2}\log p.
\]

Wir zeigen

\[
\boxed{
\|q_{p,k,T}(u)\|^2
\le
\min\left\{
1,
C_qe^{4T}p^{-2k}
\right\}.
}
\tag{C1zB2C6j.17}
\]

## 4.1 Linkspuls noch auf der rechten Terminalhälfte

Falls `u>=0`, gilt

\[
T-u
=
c_q+rac{k}{2}\log p+O(r_T).
\]

Da `c_q-r_T>0`, folgt

\[
J_{p,T}(u)\ge k.
\]

Damit ist die Marke vollständig erhalten:

\[
\|q_{p,k,T}(u)\|^2
=1-p^{-k}
\le1.
\tag{C1zB2C6j.18}
\]

Dies ist die lokale Manifestation des C1z-B-Korrelationserhaltungssatzes: Auf dem geometrisch zulässigen Korrelationspuls wird die finite-adische Markierung nicht künstlich gedämpft.

## 4.2 Linkspuls nach Überschreiten der Mittellinie

Falls `u<0`, ist

\[
T-|u|
=T+u
=
2T-c_q-rac{k}{2}\log p+O(r_T).
\]

Also

\[
J_{p,T}(u)
\le
\frac{4T-2c_q-k\log p+2r_T}{\log p}.
\]

Mit (C1zB2C6j.9) folgt

\[
\begin{aligned}
\|q_{p,k,T}(u)\|^2
&\le
p^{J_{p,T}(u)-k}\\
&\le
\exp(4T-2c_q+2r_T)p^{-2k}\\
&\le
C_qe^{4T}p^{-2k}.
\end{aligned}
\tag{C1zB2C6j.19}
\]

Zusammen mit der trivialen Kontraktionsschranke `<=1` ergibt dies (C1zB2C6j.17).

---

# 5. Exakte Reduktion der lokalen Restenergie auf eine Prime-Power-Summe

Wegen §§2–4 gilt für festes `p`:

\[
\begin{aligned}
\|R_{p,T}v\|^2
&=
\sum_{k\ge1}
 b_{p,k}^2
\int_{\operatorname{supp}(v(\cdot+k\log p/2))}
|v(u+k\log p/2)|^2
\|q_{p,k,T}(u)\|^2du\\
&\le
\|v\|^2
\sum_{k\ge1}
\log p\,p^{-k/2}
\min\{1,C_qe^{4T}p^{-2k}\}.
\end{aligned}
\tag{C1zB2C6j.20}
\]

Die Primsektoren sind orthogonal, also

\[
\boxed{
\|R_Tv\|^2
\le
\|v\|^2 S_T,
}
\tag{C1zB2C6j.21}
\]

mit

\[
\boxed{
S_T
:=
\sum_p\sum_{k\ge1}
\log p\,p^{-k/2}
\min\{1,C_0e^{4T}p^{-2k}\}.
}
\tag{C1zB2C6j.22}
\]

Hier kann `C_0` als gemeinsame Konstante für `q=3,5` gewählt werden.

Der gesamte analytische Nenner ist damit auf eine skalare Prime-Power-Summe reduziert.

---

# 6. Chebyshev-Summation

Setze

\[
Y_T:=\sqrt{C_0}\,e^{2T}.
\]

Für ein Prime-Power-Label

\[
n=p^k
\]

gilt

\[
\Lambda(n)=\log p.
\]

Wir zerlegen

\[
S_T=S_T^{\le Y}+S_T^{>Y}.
\]

## 6.1 Niedrige Prime Powers

Für `n<=Y_T` wird nur die triviale Schranke `min <=1` benutzt:

\[
S_T^{\le Y}
\le
\sum_{n\le Y_T}
\frac{\Lambda(n)}{\sqrt n}.
\tag{C1zB2C6j.23}
\]

Partielle Summation mit `psi(x) <= C_psi x` liefert

\[
\begin{aligned}
\sum_{n\le Y}
\frac{\Lambda(n)}{\sqrt n}
&=
\frac{\psi(Y)}{\sqrt Y}
+
\frac12
\int_{1}^{Y}
\frac{\psi(t)}{t^{3/2}}dt\\
&\le
C\sqrt Y.
\end{aligned}
\tag{C1zB2C6j.24}
\]

Für `Y=Y_T` daher

\[
\boxed{
S_T^{\le Y}
\le
C e^T.
}
\tag{C1zB2C6j.25}
\]

## 6.2 Hohe Prime Powers

Für `n>Y_T` benutzen wir den zweiten Faktor in (C1zB2C6j.22):

\[
S_T^{>Y}
\le
C_0e^{4T}
\sum_{n>Y_T}
\Lambda(n)n^{-5/2}.
\tag{C1zB2C6j.26}
\]

Erneute partielle Summation und `psi(t) <= C_psi t` ergeben

\[
\sum_{n>Y}
\Lambda(n)n^{-5/2}
\le
C Y^{-3/2}.
\tag{C1zB2C6j.27}
\]

Also

\[
S_T^{>Y}
\le
C e^{4T}Y_T^{-3/2}
\le
C e^T.
\tag{C1zB2C6j.28}
\]

Zusammen:

## Lemma C1zB2C6j.2 — lokale Prime-Power-Summe

\[
\boxed{
S_T\le C_Se^T.
}
\tag{C1zB2C6j.29}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm pos,Chebyshev\text{-}scope}.}
\]

### Vergleich mit C6f

C6f erhielt global

\[
\|R_T\|^2\le CTe^T.
\]

Der zusätzliche Faktor `T` kam aus dem groben innerhalb-prime Cauchy-Schwarz-Faktor `K_p(T)`.

C6j zeigt für **diesen speziellen lokalen Separator**, dass die verschobenen `k`-Pulse räumlich disjunkt sind. Dadurch fällt `K_p(T)` weg und die natürliche Summe ist nur noch

\[
\sum_{n\lesssim e^{2T}}
\frac{\Lambda(n)}{\sqrt n},
\]

die bereits durch Chebyshev `O(e^T)` ist.

---

# 7. Hauptsatz — lokale `A_T`-Energie des exakten C6i-Separators

## Satz C1zB2C6j.3

Sei `v_T` der in C6i gewählte exakte Separator mit

\[
r_T=c_0e^{-4T}.
\]

Dann existiert `C_A<infty` mit

\[
\boxed{
\langle v_T,A_Tv_T\rangle
\le
C_Ae^{-3T}
\qquad(T\gg1).
}
\tag{C1zB2C6j.30}
\]

### Beweis

Nach (C1zB2C6j.11):

\[
\|v_T\|^2=2r_T
\asymp e^{-4T}.
\]

Aus (C1zB2C6j.21) und Lemma C1zB2C6j.2:

\[
\|R_Tv_T\|^2
\le
C e^T\|v_T\|^2
\le
C'e^{-3T}.
\]

Da

\[
A_T=I+R_T^*R_T,
\]

folgt

\[
\begin{aligned}
\langle v_T,A_Tv_T\rangle
&=
\|v_T\|^2+
\|R_Tv_T\|^2\\
&\le
C_Ae^{-3T}.
\end{aligned}
\]

`□`

Status:

\[
\boxed{\checkmark[M]_{\rm pos,local\text{-}rest\text{-}energy}.}
\]

Damit war der globale C6f-Bound für diesen Separator tatsächlich um mindestens einen Faktor `T` zu grob.

**Firewall:** C6j beweist nicht

\[
\langle v_T,A_Tv_T\rangle
\asymp e^{-3T}.
\]

Nur die obere Schranke ist bewiesen. Die tatsächliche Energie kann kleiner sein.

---

# 8. Verbesserte quantitative Zweitprobe

C6i liefert exakt

\[
\boxed{
\langle v_T,A_T\mathbf1_T\rangle=0.
}
\tag{C1zB2C6j.31}
\]

C6g+C6i liefern auf dem `e^{-4T}`-Fenster

\[
\boxed{
|\langle v_T,h_T\rangle|
\ge
c_he^{-4T}.
}
\tag{C1zB2C6j.32}
\]

Mit dem C6e-Variationszertifikat

\[
\Delta_T^{(1)}
\ge
\frac{|\langle v_T,h_T\rangle|^2}
{\langle v_T,A_Tv_T\rangle}
\]

und Satz C1zB2C6j.3 folgt

\[
\Delta_T^{(1)}
\ge
\frac{c_h^2e^{-8T}}
{C_Ae^{-3T}}
=
\frac{c_h^2}{C_A}e^{-5T}.
\]

Also:

## Korollar C1zB2C6j.4

\[
\boxed{
\Delta_T^{(1)}
\ge
c_\Delta e^{-5T}
\qquad(T\gg1).
}
\tag{C1zB2C6j.33}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm pos,improved\text{-}\Delta\text{-}lower\text{-}bound}.}
\]

C6i hatte nur

\[
\Delta_T^{(1)}
\gtrsim
\frac{e^{-5T}}T.
\]

C6j entfernt somit exakt den noch vom globalen Restnormbound stammenden Faktor `1/T`.

---

# 9. Hankel-Determinante

Wie in C6d–C6i:

\[
\det\mathbf K_T^{(1)}
=
\mu_{T,0}\Delta_T^{(1)},
\qquad
\mu_{T,0}
=
\langle\mathbf1_T,A_T\mathbf1_T\rangle.
\]

Da

\[
A_T\ge I,
\]

gilt

\[
\mu_{T,0}\ge2T.
\]

Daher aus (C1zB2C6j.33):

\[
\boxed{
\det\mathbf K_T^{(1)}
\ge
c_KT e^{-5T}.
}
\tag{C1zB2C6j.34}
\]

Dies verbessert C6is expliziten Bound

\[
\det\mathbf K_T^{(1)}
\gtrsim e^{-5T}
\]

um denselben Faktor `T`.

---

# 10. Was C6j über die normierte zweite Probe sagt — und was nicht

Die zweite orthogonale Krylov-Richtung besitzt Normquadrat

\[
\Delta_T^{(1)}.
\]

C6j liefert daher nur die einseitige Nichtdegenerationsreserve

\[
\sqrt{\Delta_T^{(1)}}
\ge
c e^{-5T/2}.
\tag{C1zB2C6j.35}
\]

Für die normierte Probe

\[
\widehat\psi_{T,1}
=
\frac{r_{T,1}^{probe}}
{\sqrt{\Delta_T^{(1)}}}
\]

bedeutet dies, dass eine spätere obere Abschätzung unnormierter Pairings höchstens einen bekannten möglichen Normalisierungsverlust von Ordnung

\[
e^{5T/2}
\]

kompensieren muss.

Aber C6j beweist nicht:

\[
\Delta_T^{(1)}\asymp e^{-5T}
\]

oder

\[
\Delta_T^{(1)}\to0.
\]

Die tatsächliche `Delta`-Skala kann größer sein.

---

# 11. Reconciliation mit C6f–C6i

## C6f

C6f bewies den globalen Operatorbound

\[
\|R_T\|^2\le CTe^T.
\]

C6j widerspricht dem nicht. Es beweist nur, dass dieser Bound auf dem speziellen C6i-Haarseparator nicht scharf genug ist.

## C6g

C6g kontrolliert die Hub-Crowding-Masse zunächst auf dem größeren Radius

\[
e^{-T}/T.
\]

Da der C6i/C6j-Radius

\[
e^{-4T}
\]

kleiner ist, folgt die robuste Hubpaarung durch Monotonie weiter.

## C6h

C6h kontrolliert `R_T^*R_T\mathbf1_T` lokal. C6j behandelt eine andere Größe:

\[
\|R_Tv_T\|^2.
\]

Die beiden Resultate sind kompatibel, aber keines folgt formal aus dem anderen.

## C6i

C6i liefert die exakte `A_T\mathbf1_T`-Orthogonalität und den `e^{-4T}`-Radius.

C6j verbessert ausschließlich den Energie-Nenner:

\[
T e^{-3T}
\quad\leadsto\quad
e^{-3T}.
\]

Damit wird

\[
\frac{e^{-5T}}T
\quad\leadsto\quad
e^{-5T}.
\]

---

# 12. No-Go-Persistenzmatrix

| Früherer Knoten | Gesiegelter Befund | Wirkung in C6j |
|---|---|---|
| C1y | translationsinvariante Regulatoren lösen den Hub/Rest-Konflikt nicht | unverändert; `Q_T(u)` bleibt source-windowed |
| B2-A | kein fehlender finite Schattenmechanismus durch Gamma-Präkonditionierung | unverändert |
| B2-B | naiver Haar-`L^2`-Endpunkt reicht nicht | unverändert |
| C4 | unendliche Boundary-Jet-Hierarchie | unverändert |
| C6 | kein voller Odd-Transport durch festen endlichen Jetquotienten | unverändert |
| C6a | Self-Grams allein reichen nicht | unverändert |
| C6b | C2-Flachheit allein reicht nicht | unverändert |
| C6c | `tau=>kappa` nur unter zusätzlicher Kontrolle | unverändert |
| C6d | C4-Jets sind keine automatischen Multi-Probes | unverändert |
| C6e | eventualer Krylov-Rang 2 | bleibt positiv gesiegelt |
| C6f | global `||R_T||^2 <= CTe^T` | bleibt korrekt; lokal für `v_T` verbessert |
| C6g | Hub-Crowding auf `e^{-T}/T` | weiter benutzt |
| C6h | Rest-Crowding für `A_T1_T` | unverändert |
| C6i | exakter `e^{-4T}`-Separator | direkt benutzt |
| C6i | `lambda_T`-Asymptotik unbewiesen | unverändert; C6j braucht `lambda_T` nicht |

Alle älteren No-Gos bleiben erhalten.

---

# 13. Was C6j ausdrücklich nicht beweist

Nicht bewiesen sind:

- eine asymptotische Äquivalenz für `\langle v_T,A_Tv_T\rangle`;
- eine untere Schranke `\langle v_T,A_Tv_T\rangle \gtrsim e^{-3T}`;
- eine optimale Separatorskala;
- eine bessere als `e^{-4T}` quantitative Zwei-Paar-Isolation;
- `\Delta_T^{(1)}\to0`;
- `\inf_T\Delta_T^{(1)}>0`;
- `\Delta_T^{(1)}\to\infty`;
- eine scharfe Asymptotik für `\Delta_T^{(1)}`;
- eine obere Schranke für `\Delta_T^{(1)}`;
- Jet-Alignment der normierten zweiten Probe;
- eine Untergrenze für `s_min(P_T^(1))`;
- `epsilon_T^{probe}(R,1)->0`;
- `tau_T(E_{R,1})->0`;
- `Theta_{T,U}^{E_{R,1}}->I`;
- Krylov-Rang `N>=2`.

Insbesondere bleibt die C6f-Degenerationsmöglichkeit logisch offen:

\[
\Delta_T^{(1)}\to0
\]

ist mit dem aktuellen Stand vereinbar, aber nicht bewiesen.

---

# 14. Exakter nächster Arbeitsauftrag

Nach C6j ist die reine Energieverbesserung des exakten Separators bis auf den exponentiellen Isolationsradius ausgeschöpft:

\[
\boxed{
\langle v_T,A_Tv_T\rangle
\lesssim e^{-3T},
\qquad
|\langle v_T,h_T\rangle|
\gtrsim e^{-4T},
}
\]

also

\[
\boxed{
\Delta_T^{(1)}\gtrsim e^{-5T}.
}
\]

Der nächste sinnvolle Knoten sollte deshalb **nicht** erneut nur die globale Restnorm verbessern.

Es gibt zwei echte nächste Richtungen:

1. **C6k-A — Exponent des exakten Isolationsradius:** Kann die rein arithmetische `e^{-4T}`-Skala verbessert werden, ohne Transzendenztheorie? Jede Verbesserung geht quadratisch in den `Delta`-Zähler ein.
2. **C6k-B — zweite Probe gegen die ersten beiden Jet-Responses:** Nutze die nun explizite Normalisierungsreserve `sqrt(Delta_T^(1)) >= c e^{-5T/2}` und untersuche erstmals
   \[
   \langle\xi_{R,m}^{(T)},\widehat\psi_{T,1}\rangle,
   \qquad m=0,1.
   \]

Strategisch ist nach C6e–C6j **C6k-B** der informativere nächste Schritt: Die Existenz und quantitative Nichtdegeneration der zweiten Probe sind jetzt ausreichend kontrolliert, um den seit C6d offenen Jet-Alignment-Test endlich direkt anzugreifen.

---

# 15. Endurteil

C6j entscheidet die vom Gegenprüfer formulierte Alternative positiv: Der globale C6f-Bound war für den exakten C6i-Haarseparator tatsächlich verschwenderisch.

Der Grund ist nicht bloß die kleine Trägerlänge. Entscheidend ist die konkrete source-gekoppelte Geometrie:

\[
\boxed{
\text{rechter Translationspuls wird konditionell getötet}
+
\text{linke }k\text{-Pulse sind disjunkt}.
}
\]

Dadurch reduziert sich die Restenergie auf

\[
S_T
=
\sum_{p,k}
\log p\,p^{-k/2}
\min\{1,C e^{4T}p^{-2k}\}.
\]

Mit dem ausdrücklich neu eingeführten, aber elementaren Chebyshev-Input

\[
\psi(X)\ll X
\]

folgt

\[
S_T\ll e^T.
\]

Da

\[
\|v_T\|^2\asymp e^{-4T},
\]

ergibt sich

\[
\boxed{
\langle v_T,A_Tv_T\rangle
\lesssim e^{-3T}.
}
\]

C6is quantitative Zweitprobe verbessert sich damit auf

\[
\boxed{
\Delta_T^{(1)}
\gtrsim e^{-5T},
\qquad
\det\mathbf K_T^{(1)}
\gtrsim T e^{-5T}.
}
\]

Dies ist ein echter quantitativer Fortschritt, aber weiterhin **keine** asymptotische Klassifikation von `Delta_T^(1)`.
