# P11-C1z-B2-C6e — Zweitprobe-Nichtdegeneration durch Cross-Prime-Sprungkante

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6e]`  
**Direkte Voraussetzungen:** C1z-B, C1z-B1, C1z-B2-C3, C1z-B2-C4, C1z-B2-C6d  
**Strukturelle Schnittstellen:** C1z-B2-C6a, C1z-B2-C6b, C1z-B2-C6c  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d Jet-Alignment-Firewall  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6e]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm pos,eventual\text{-}second\text{-}probe}
+
\checkmark[M]_{\rm pos,cross\text{-}prime\text{-}jump\text{-}separator}
+
\checkmark[M]_{\rm pos,Krylov\text{-}rank\text{-}2}
+
\checkmark[M]_{\rm neg,parity\text{-}separator}
+
?[O]_{\rm quantitative\text{-}\Delta\text{-}scale}
+
?[O]_{\rm second\text{-}probe\text{-}jet\text{-}alignment}
}
\]

Der atomare C6d-Test wird positiv entschieden:

\[
\boxed{
\exists T_0<\infty\ \forall T\ge T_0:
\qquad
\Delta_T^{(1)}>0.
}
\tag{C1zB2C6e.1}
\]

Äquivalent gilt für alle hinreichend großen Terminalhorizonte

\[
\boxed{
H_T^*H_T\mathbf1_T
\notin
\mathbb C\,A_T\mathbf1_T,
\qquad
A_T=I+R_T^*R_T.
}
\tag{C1zB2C6e.2}
\]

Damit besitzt der gescreente Hub-Krylov-Flag aus C6d tatsächlich eine zweite, von der C4-Konstantenprobe linear unabhängige Response-Richtung:

\[
\boxed{
\dim
\operatorname{span}
\{\zeta_T,\mathfrak S_T\zeta_T\}
=2
\qquad(T\ge T_0),
}
\tag{C1zB2C6e.3}
\]

wobei

\[
\zeta_T=A_T^{1/2}\mathbf1_T,
\qquad
\mathfrak S_T=A_T^{-1/2}H_T^*H_TA_T^{-1/2}.
\]

Der Beweis benutzt **nicht** das Argument „Proportionalität wäre nichtgenerisch“ und auch keine bloße Größenordnung der beiden Gesamtvektoren. Er konstruiert eine explizite lokale Trennrichtung `v_T`.

Der Mechanismus ist arithmetisch:

- `R_T^*R_T` zerfällt wegen der orthogonalen Restsektoren `K_p^0` als Summe **prime-purer** Blöcke;
- deshalb können die Sprungkanten von `A_T\mathbf1_T` nur auf einzelnen logarithmischen Primgittern liegen;
- `H_T^*H_T` enthält dagegen echte **Cross-Prime**-Terme, weil alle Hublabels in denselben skalaren neutralen Hub fallen;
- eine Cross-Prime-Kante bei
  \[
  x_{p,q}(T)=T-\frac12\log(q/p)
  \]
  kann rechtsseitig von keinem einzelnen Primzahlgitter erzeugt werden;
- die einzige mögliche Gegenkollision von der gegenüberliegenden Fensterseite wird durch einen Zwei-Paar-Test `(2,3)` / `(2,5)` ausgeschaltet;
- mögliche zusätzliche Hubkollisionen durch sehr hohe Labelpaare besitzen an genau dieser lokalen Sprungkante insgesamt nur `O(T^2e^{-3T})` Gewicht und können den festen primitiven Cross-Prime-Sprung für großes `T` nicht aufheben.

Dadurch existiert für jedes hinreichend große `T` ein Punkt `x_T` und ein kleines `\varepsilon_T>0`, so dass

\[
v_T
:=
1_{(x_T-\varepsilon_T,x_T)}
-
1_{(x_T,x_T+\varepsilon_T)}
\]

erfüllt

\[
\boxed{
\langle v_T,A_T\mathbf1_T\rangle=0,
\qquad
\langle v_T,H_T^*H_T\mathbf1_T\rangle\ne0.
}
\tag{C1zB2C6e.4}
\]

Das ist der verlangte explizite Separator.

---

# 0. Voraussetzungsverkettung und Scope

C6e erbt nichts implizit.

## 0.1 Aus C1z-B / C1z-B1

Auf

\[
\mathscr H_T=L^2(-T,T)
\]

steht der source-windowed Huboperator

\[
\boxed{
H_T
=
\sum_{n\in\mathcal N_T}
a_n K_{\ell_n},
\qquad
K_s:=P_TD_sE_T,
}
\tag{C1zB2C6e.5}
\]

zur Verfügung, mit

\[
\mathcal N_T=\{p^k:p^k\le e^{2T}\},
\qquad
\ell_{p^k}=k\log p,
\qquad
\boxed{
a_{p^k}=\sqrt{\log p}\,p^{-3k/4}>0.
}
\tag{C1zB2C6e.6}
\]

Der konditionierte Restoperator zerfällt wegen

\[
K_p^0\perp K_q^0
\qquad(p\ne q)
\]

orthogonal nach Primzahlen:

\[
\boxed{
R_T=\bigoplus_pR_{p,T},
\qquad
R_T^*R_T=\sum_pR_{p,T}^*R_{p,T}.
}
\tag{C1zB2C6e.7}
\]

Die source-gekoppelte p-adische Tiefe lautet

\[
J_{p,T}(u)
=
\max\left\{0,
\left\lfloor
\frac{2(T-|u|)_+}{\log p}
\right\rfloor
\right\},
\]

und die Vektoren

\[
q_{p,k,T}(u)
:=
\mathsf Q_T(u)\eta_{p,k}
\]

sind bezüglich `u` stückweise konstant; ihre Sprungstellen liegen ausschließlich auf dem zum einzelnen `p` gehörenden Randgitter.

## 0.2 Aus C3

Setze

\[
\boxed{
A_T:=I+R_T^*R_T\ge I.
}
\tag{C1zB2C6e.8}
\]

Für jedes feste `T` ist `A_T` positiv, beschränkt und invertierbar.

C3 beweist außerdem den primitiven Restkollaps

\[
R_T^{(1)}\mathbf1_T=0,
\]

aber C6e benutzt diesen Befund **nicht** als alleinigen Nichtdegenerationsbeweis. Er bleibt nur Teil der strukturellen Einordnung.

## 0.3 Aus C4

C4 zeigt auf jedem festen alten Source-Fenster die exakte Boundary-Form

\[
H_T\mathbf1_T(u)
=-\operatorname{sgn}(u)\Phi_T(|u|)
\]

und entwickelt die eine skalare Beobachtung

\[
\langle J_{R,T}f,H_T\mathbf1_T\rangle
\]

in den vollständigen Boundary-Jet.

C6e benutzt C4 als Konsistenzschnittstelle, **nicht** als Ersatz für den neuen Zweitprobe-Beweis. Insbesondere wird aus den C4-Jetkoeffizienten keine zweite targetseitige Probe postuliert.

## 0.4 Aus C6d

C6d definiert

\[
\mathfrak S_T
=A_T^{-1/2}H_T^*H_TA_T^{-1/2},
\qquad
\zeta_T=A_T^{1/2}\mathbf1_T,
\]

und

\[
\Delta_T^{(1)}
=
\langle H_T^*H_T\mathbf1_T,
A_T^{-1}H_T^*H_T\mathbf1_T\rangle
-
\frac{\|H_T\mathbf1_T\|^4}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}.
\tag{C1zB2C6e.9}
\]

C6d beweist exakt

\[
\boxed{
\Delta_T^{(1)}>0
\iff
H_T^*H_T\mathbf1_T
\notin\mathbb C\,A_T\mathbf1_T.
}
\tag{C1zB2C6e.10}
\]

C6e entscheidet genau diese noch offene `N=1`-Frage.

---

# 1. Die Gleichheitsbedingung als Separatorproblem

Setze zur Abkürzung

\[
h_T:=H_T^*H_T\mathbf1_T.
\]

Falls

\[
h_T=\lambda_TA_T\mathbf1_T,
\]

muss durch Paarung mit `\mathbf1_T`

\[
\boxed{
\lambda_T
=
\frac{\langle\mathbf1_T,h_T\rangle}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}
=
\frac{\|H_T\mathbf1_T\|^2}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}
>0.
}
\tag{C1zB2C6e.11}
\]

Daher genügt es, einen Vektor `v_T\in\mathscr H_T` zu finden mit

\[
\boxed{
\langle v_T,A_T\mathbf1_T\rangle=0,
\qquad
\langle v_T,h_T\rangle\ne0.
}
\tag{C1zB2C6e.12}
\]

Dies ist genau die vom C6e-Gegenprüfer verlangte Form eines expliziten Trennzertifikats.

Noch stärker: Für jedes solche `v_T` folgt aus Cauchy-Schwarz in der `A_T`-Geometrie eine quantitative, wenn auch zunächst nicht asymptotisch ausgewertete Untergrenze.

Definiere

\[
r_T
:=
h_T-\lambda_TA_T\mathbf1_T.
\]

Dann ist

\[
\Delta_T^{(1)}
=
\langle r_T,A_T^{-1}r_T\rangle.
\]

Wegen `\langle v_T,A_T\mathbf1_T\rangle=0` gilt

\[
\langle v_T,r_T\rangle=\langle v_T,h_T\rangle.
\]

Also

\[
|\langle v_T,h_T\rangle|^2
\le
\langle v_T,A_Tv_T\rangle
\Delta_T^{(1)}.
\]

Somit:

\[
\boxed{
\Delta_T^{(1)}
\ge
\frac{|\langle v_T,h_T\rangle|^2}
{\langle v_T,A_Tv_T\rangle}.
}
\tag{C1zB2C6e.13}
\]

Ein einziger expliziter Separator mit nichtverschwindendem Zähler entscheidet also `\Delta_T^{(1)}>0`.

---

# 2. Paritäts-Firewall: Symmetrie trennt die beiden Vektoren nicht

Der erste naheliegende Versuch wäre eine Gerade/Ungerade-Trennung.

Für die zentrierten Differenzen gilt

\[
D_s:\text{gerade}\leftrightarrow\text{ungerade}.
\]

Da `H_T` eine reelle Linearkombination solcher zentrierten Differenzen ist,

\[
H_T\mathbf1_T
\]

ist ungerade und

\[
H_T^*H_T\mathbf1_T
\]

wieder gerade.

Die source-gekoppelte Konditionierung hängt nur von `|u|` ab. Daher respektiert `R_T^*R_T` die Paritätszerlegung, und folglich ist auch

\[
A_T\mathbf1_T
\]

gerade.

Damit liefert jeder ungerade Testvektor `v` gleichzeitig

\[
\langle v,h_T\rangle=0,
\qquad
\langle v,A_T\mathbf1_T\rangle=0.
\]

Also:

\[
\boxed{
\text{Parität allein kann }h_T
\text{ und }A_T\mathbf1_T\text{ nicht trennen.}
}
\tag{C1zB2C6e.14}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm neg,parity\text{-}separator}.}
\]

Der positive Beweis muss die arithmetische Randstruktur benutzen.

---

# 3. Exakte Randgitter der komprimierten Differenzen

Für

\[
0<s\le2T
\]

setze

\[
K_s=P_TD_sE_T.
\]

Da `D_s^*=-D_s` und `P_T=E_T^*`, gilt exakt

\[
\boxed{
K_s^*=-K_s.
}
\tag{C1zB2C6e.15}
\]

Mit der in C3/C4 verwendeten Translationskonvention ist

\[
\boxed{
K_s\mathbf1_T
=
1_{(-T,-T+s/2)}
-
1_{(T-s/2,T)}.
}
\tag{C1zB2C6e.16}
\]

Dies reproduziert die C4-Aussage, dass `H_T\mathbf1_T` auf der rechten Hälfte negativ und auf der linken Hälfte positiv ist.

Insbesondere ist `K_s\mathbf1_T` eine Stufenfunktion mit ausschließlich den vier Randpunkten

\[
-T,\quad -T+s/2,\quad T-s/2,\quad T.
\]

Wendet man ein weiteres `K_a` an, entstehen nur um `\pm a/2` verschobene Randpunkte. Daher liegen sämtliche Sprungstellen von

\[
K_a^*K_b\mathbf1_T
\]

in der endlichen Menge

\[
\boxed{
\pm T
+
\frac12(\varepsilon_1a+\varepsilon_2b),
\qquad
\varepsilon_1,\varepsilon_2\in\{-1,0,1\},
}
\tag{C1zB2C6e.17}
\]

soweit der jeweilige Punkt tatsächlich in `(-T,T)` liegt.

Für die folgenden speziellen Cross-Prime-Paare brauchen wir nur eine konkrete dieser Kanten.

---

# 4. Die primitive Cross-Prime-Kante

Seien `p<q` verschiedene Primzahlen und

\[
a:=\log p,
\qquad
b:=\log q.
\]

Nehme an, beide primitiven Labels sind aktiv:

\[
q\le e^{2T}.
\]

Definiere

\[
\boxed{
x_{p,q}(T)
:=
T-\frac{b-a}{2}
=
T-\frac12\log(q/p).
}
\tag{C1zB2C6e.18}
\]

Betrachte den geordneten Hub-Crossterm

\[
a_pa_qK_a^*K_b\mathbf1_T,
\qquad
a_p=\sqrt{\log p}\,p^{-3/4}.
\]

Aus (C1zB2C6e.16) sieht man direkt: Beim Durchgang durch `u=x_{p,q}(T)` kreuzt genau eine der beiden um `a/2` verschobenen Auswertungen von `K_b\mathbf1_T` die innere rechte Randkante

\[
T-b/2.
\]

Daher besitzt

\[
K_a^*K_b\mathbf1_T
\]

bei `x_{p,q}(T)` einen Sprung vom Betrag `1`.

Für die beiden später verwendeten Paare

\[
(p,q)=(2,3),\qquad(2,5)
\]

liegt keine der trivialen Koinzidenzen wie `b=2a` vor. Der primitive Cross-Prime-Beitrag zum Sprung von `h_T` besitzt daher den festen nichtverschwindenden Betrag

\[
\boxed{
a_2a_q
=
\sqrt{\log2\,\log q}\,(2q)^{-3/4}>0.
}
\tag{C1zB2C6e.19}
\]

Die Frage ist nur noch, ob andere Hubterme exakt an derselben Stelle springen und diesen Beitrag auslöschen könnten.

---

# 5. Eindeutige Primfaktorzerlegung isoliert die rechtsseitige Cross-Prime-Differenz

Fixiere zunächst eines der Paare `(2,q)` mit `q\in\{3,5\}` und setze

\[
d_q:=\log(q/2),
\qquad
x_q(T):=T-d_q/2.
\]

Ein anderer rechtsseitiger **Differenzrand** zweier Hublabels `n,m` könnte denselben Punkt nur erzeugen, wenn

\[
|\log m-\log n|=d_q.
\]

Also

\[
\frac mn=\frac q2
\quad\text{oder}\quad
\frac nm=\frac q2.
\]

Da `n` und `m` jeweils einzelne Primzahlpotenzen sind, erzwingt eindeutige Primfaktorzerlegung

\[
\boxed{
\{n,m\}=\{2,q\}.
}
\tag{C1zB2C6e.20}
\]

Ein rechtsseitiger Einzelrand würde

\[
\log n=d_q
\]

und damit `n=q/2` verlangen — unmöglich.

Ein rechtsseitiger Summenrand würde

\[
\log n+\log m=d_q
\]

und damit `nm=q/2` verlangen — ebenfalls unmöglich.

Somit ist die primitive `(2,q)`-Kante unter allen rechtsseitig erzeugten Hubkanten arithmetisch eindeutig.

---

# 6. Einzige mögliche Hub-Gegenkollision: sehr hohe Labels von der gegenüberliegenden Randseite

Für großes `T` können die übrigen in (C1zB2C6e.17) vorkommenden Einzel- oder Differenzkanten von der linken Fensterseite `x_q(T)` nicht erreichen: ihre logarithmische Verschiebung ist höchstens `2T`, während hierzu asymptotisch `4T-d_q` nötig wäre.

Übrig bleibt nur eine Summenkante zweier sehr hoher aktiver Labels `n,m`:

\[
-T+\frac12(\log n+\log m)
=x_q(T).
\]

Dies ist äquivalent zu

\[
\boxed{
nm
=e^{4T}\frac{2}{q}.
}
\tag{C1zB2C6e.21}
\]

Setze

\[
C_{q,T}:=e^{4T}\frac{2}{q}.
\]

Falls `C_{q,T}` kein positiver Integer ist, existiert überhaupt keine solche Kollision.

Falls `C_{q,T}` Integer ist, können `n` und `m` als einzelne Primzahlpotenzen sein Produkt nur in sehr wenigen Weisen darstellen:

- besitzt `C_{q,T}` mindestens drei verschiedene Primteiler, gibt es keine Darstellung;
- besitzt es genau zwei verschiedene Primteiler, gibt es höchstens die beiden geordneten Darstellungen;
- ist es eine reine Primzahlpotenz `r^M`, gibt es höchstens `M-1=O(T)` geordnete Aufteilungen in zwei nichttriviale Primzahlpotenzen.

Also ist die Anzahl kollidierender geordneter Paare stets

\[
O(T).
\tag{C1zB2C6e.22}
\]

Für jedes solche Paar `n=r^k`, `m=s^\ell` gilt

\[
\begin{aligned}
a_na_m
&=
\sqrt{\log r\,\log s}\,(nm)^{-3/4}\\
&\le
\frac12\log(nm)\,(nm)^{-3/4}\\
&=
O_q(T)e^{-3T}.
\end{aligned}
\tag{C1zB2C6e.23}
\]

Der Sprung eines einzelnen `K_{\log n}^*K_{\log m}\mathbf1_T` an einer solchen Kante ist durch eine universelle Konstante beschränkt. Mit (C1zB2C6e.22) folgt für die **gesamte** mögliche Gegenkollision

\[
\boxed{
J_{q,T}^{\rm opp}
=O_q(T^2e^{-3T}).
}
\tag{C1zB2C6e.24}
\]

Dagegen besitzt der feste primitive `(2,q)`-Crossterm nach (C1zB2C6e.19) einen von `T` unabhängigen nichtverschwindenden Sprungkoeffizienten.

Folglich existiert für jedes `q\in\{3,5\}` ein `T_q<\infty` mit

\[
\boxed{
\left|
\operatorname{Jump}_{x_q(T)}h_T
\right|
\ge
\frac12a_2a_q
>0
\qquad(T\ge T_q),
}
\tag{C1zB2C6e.25}
\]

sofern `x_q(T)` nicht aus einem anderen bereits identifizierten exakt gleichen rechtsseitigen Cross-Prime-Paar stammt; (C1zB2C6e.20) zeigt, dass dies nicht geschieht.

### Methodische Firewall

(C1zB2C6e.24) ist **kein** bloßes Größenordnungsargument für die Gesamtvektoren `h_T` und `A_T\mathbf1_T`.

Es ist eine lokale Nichtauslöschungsabschätzung für den Sprungkoeffizienten an einer konkret identifizierten arithmetischen Kante. Der anschließende Beweis benutzt diesen nichtverschwindenden lokalen Sprung zur Konstruktion eines tatsächlichen Separators.

---

# 7. Prime-pure Breakpoint-Theorem für `A_T\mathbf1_T`

Nun wird die Restseite typisiert.

Für eine Primzahl `r` setze

\[
\boxed{
\mathscr L_{r,T}
:=
\left\{
\pm T+\frac m2\log r:
 m\in\mathbb Z
\right\}
\cap(-T,T).
}
\tag{C1zB2C6e.26}
\]

## Lemma C1zB2C6e.1 — prime-pure Restgitter

Für jedes feste `T` besitzt `R_{r,T}^*R_{r,T}\mathbf1_T` eine stückweise konstante Repräsentante, deren sämtliche Sprungstellen in

\[
\mathscr L_{r,T}
\]

liegen.

### Beweis

Schreibe den `r`-Sektor des Restoperators als endliche Summe

\[
R_{r,T}f(u)
=
\sum_k
b_{r,k}
K_{k\log r}f(u)
\,q_{r,k,T}(u),
\]

mit

\[
b_{r,k}=\sqrt{\log r}\,r^{-k/4}
\]

und

\[
q_{r,k,T}(u)=\mathsf Q_T(u)\eta_{r,k}.
\]

Aus der exakten source-gekoppelten Tiefenformel hängt `q_{r,k,T}` nur von

\[
J_{r,T}(u)
=
\left\lfloor
\frac{2(T-|u|)_+}{\log r}
\right\rfloor
\]

ab. Seine Sprungstellen liegen deshalb in `\mathscr L_{r,T}`.

Nach (C1zB2C6e.16) ist auch

\[
K_{k\log r}\mathbf1_T
\]

eine Stufenfunktion mit Sprungstellen in demselben Gitter.

Daher ist

\[
R_{r,T}\mathbf1_T
\]

eine `K_r^0`-wertige Stufenfunktion mit ausschließlich `r`-puren Gitterkanten.

Für den Adjungierten gilt

\[
R_{r,T}^*F
=
\sum_k
b_{r,k}
K_{k\log r}^*
\left(
\langle q_{r,k,T}(\cdot),F(\cdot)\rangle_{K_r^0}
\right).
\]

Setzt man `F=R_{r,T}\mathbf1_T`, ist der skalare Ausdruck in Klammern wiederum eine Stufenfunktion mit Sprungstellen in `\mathscr L_{r,T}`. Multiplikation erzeugt keine neuen Kanten, und `K_{k\log r}^*=-K_{k\log r}` verschiebt vorhandene Kanten ausschließlich um ganzzahlige Vielfache von `\frac12\log r`.

Damit bleibt die gesamte Breakpoint-Menge in `\mathscr L_{r,T}`. `□`

Wegen der p-sektoralen Orthogonalität (C1zB2C6e.7) folgt sofort:

## Korollar C1zB2C6e.2 — Breakpoints von `A_T\mathbf1_T`

Setze

\[
\mathscr L_T^{A}
:=
\bigcup_r\mathscr L_{r,T},
\]

wobei nur die für festes `T` tatsächlich aktiven Primsektoren auftreten.

Dann ist `A_T\mathbf1_T` stückweise konstant und

\[
\boxed{
\operatorname{Break}(A_T\mathbf1_T)
\subseteq
\mathscr L_T^A.
}
\tag{C1zB2C6e.27}
\]

Insbesondere erzeugt die Restmetrik **keine** genuine Cross-Prime-Randkante.

Dies ist der strukturelle Unterschied zu `H_T^*H_T`, dessen skalare Hubsumme vor der Gram-Bildung alle Primlabels miteinander koppelt.

---

# 8. Zwei feste Cross-Prime-Paare garantieren eine restfreie Kante

Betrachte nun

\[
q=3
\qquad\text{und}\qquad
q=5
\]

mit gemeinsamem `p=2`.

Die beiden Kandidatenpunkte sind

\[
\boxed{
x_3(T)=T-\frac12\log(3/2),}
\tag{C1zB2C6e.28}
\]

und

\[
\boxed{
x_5(T)=T-\frac12\log(5/2).}
\tag{C1zB2C6e.29}
\]

Sobald

\[
T\ge\frac12\log5,
\]

sind alle drei primitiven Hublabels `2,3,5` aktiv.

Wir zeigen: **Mindestens einer der beiden Punkte liegt nicht in `\mathscr L_T^A`.**

### Rechtsseitige Gitterkollision

Angenommen

\[
x_q(T)=T+\frac m2\log r.
\]

Dann

\[
-\log(q/2)=m\log r.
\]

Da `q/2` für `q=3,5` keine ganzzahlige Primzahlpotenz und auch kein Kehrwert einer solchen mit passender eindeutiger Primfaktorzerlegung ist, ist dies unmöglich.

### Gegenüberliegende Gitterkollision

Es bleibt

\[
x_q(T)=-T+\frac m2\log r,
\]

also

\[
\boxed{
e^{4T}=\frac q2r^m.}
\tag{C1zB2C6e.30}
\]

Nehmen wir an, **beide** Kandidaten seien auf diese Weise Rest-Breakpoints. Dann gäbe es Primzahlen `r,s` und positive ganze `m,n` mit

\[
e^{4T}=\frac32r^m=\frac52s^n.
\]

Folglich

\[
3r^m=5s^n.
\]

Eindeutige Primfaktorzerlegung erzwingt

\[
\boxed{
r=5,\qquad s=3,\qquad m=n=1.}
\]

Damit müsste

\[
\boxed{e^{4T}=15/2.}
\tag{C1zB2C6e.31}
\]

gelten.

Aber für

\[
T\ge\frac12\log5
\]

ist

\[
e^{4T}\ge25>15/2.
\]

Widerspruch.

Also:

\[
\boxed{
T\ge\frac12\log5
\Longrightarrow
\bigl(x_3(T)\notin\mathscr L_T^A\bigr)
\ \text{oder}\ 
\bigl(x_5(T)\notin\mathscr L_T^A\bigr).
}
\tag{C1zB2C6e.32}
\]

Dies ist der arithmetische Kern des Separators.

---

# 9. Wahl der tatsächlichen Sprungkante

Sei nun `T` so groß, dass zugleich

1. `T\ge\frac12\log5`;
2. die Nichtauslöschungsabschätzungen (C1zB2C6e.25) für `q=3` und `q=5` gelten.

Wähle

\[
q_T\in\{3,5\}
\]

so, dass

\[
\boxed{x_T:=x_{q_T}(T)\notin\mathscr L_T^A.}
\tag{C1zB2C6e.33}
\]

Nach §6 besitzt `h_T` bei `x_T` einen echten nichtverschwindenden Sprung:

\[
\boxed{
J_T
:=
\operatorname{Jump}_{x_T}h_T
\ne0.
}
\tag{C1zB2C6e.34}
\]

Nach §7/§8 besitzt `A_T\mathbf1_T` dort dagegen **keinen** Sprung.

Da für festes `T` sowohl `h_T` als auch `A_T\mathbf1_T` endliche Stufenfunktionen sind, gibt es

\[
\varepsilon_T>0
\]

so klein, dass auf

\[
(x_T-\varepsilon_T,x_T)
\qquad\text{und}\qquad
(x_T,x_T+\varepsilon_T)
\]

keine weitere Sprungkante eines der beiden Vektoren liegt.

Insbesondere ist `A_T\mathbf1_T` auf dem gesamten Intervall

\[
(x_T-\varepsilon_T,x_T+\varepsilon_T)
\]

konstant, während `h_T` links und rechts verschiedene konstante Werte besitzt.

---

# 10. Expliziter Separator

Definiere

\[
\boxed{
v_T
:=
1_{(x_T-\varepsilon_T,x_T)}
-
1_{(x_T,x_T+\varepsilon_T)}.
}
\tag{C1zB2C6e.35}
\]

Dieser Vektor liegt in `\mathscr H_T`.

Da `A_T\mathbf1_T` in der betrachteten Umgebung konstant ist und beide Teilintervalle dieselbe Länge haben,

\[
\boxed{
\langle v_T,A_T\mathbf1_T\rangle=0.
}
\tag{C1zB2C6e.36}
\]

Seien `h_-` und `h_+` die konstanten Werte von `h_T` links bzw. rechts von `x_T`. Dann

\[
h_+-h_-=J_T\ne0.
\]

Somit

\[
\boxed{
\langle v_T,h_T\rangle
=\varepsilon_T(h_--h_+)
=-\varepsilon_TJ_T
\ne0.
}
\tag{C1zB2C6e.37}
\]

Damit ist (C1zB2C6e.12) erfüllt.

Dies ist kein abstraktes Existenzargument. `v_T` wird direkt aus einer konkret identifizierten Cross-Prime-Sprungkante konstruiert.

---

# 11. Hauptsatz — eventuale Nichtdegeneration der zweiten Krylov-Probe

## Satz C1zB2C6e.3

Es existiert `T_0<\infty`, so dass für alle `T\ge T_0`

\[
\boxed{
H_T^*H_T\mathbf1_T
\notin
\mathbb C\,A_T\mathbf1_T.
}
\tag{C1zB2C6e.38}
\]

Folglich

\[
\boxed{
\Delta_T^{(1)}>0.
}
\tag{C1zB2C6e.39}
\]

### Beweis

Wähle `x_T`, `\varepsilon_T` und `v_T` wie in §§8–10. Dann

\[
\langle v_T,A_T\mathbf1_T\rangle=0
\]

aber

\[
\langle v_T,H_T^*H_T\mathbf1_T\rangle\ne0.
\]

Die beiden Vektoren können daher nicht proportional sein. C6d Gleichung (C1zB2C6d.28) bzw. (C1zB2C6e.10) liefert

\[
\Delta_T^{(1)}>0.
\]

`□`

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,eventual\text{-}second\text{-}probe}.
}
\]

---

# 12. Explizite positive Untergrenze aus dem Separator

Aus (C1zB2C6e.13), (C1zB2C6e.36) und (C1zB2C6e.37) folgt sogar

\[
\boxed{
\Delta_T^{(1)}
\ge
\frac{
\varepsilon_T^2|J_T|^2
}{
\langle v_T,A_Tv_T\rangle
}
>0.
}
\tag{C1zB2C6e.40}
\]

Mit (C1zB2C6e.25) kann für großes `T` im Zähler zusätzlich

\[
|J_T|
\ge
\frac12
\min\{a_2a_3,a_2a_5\}
\]

gesetzt werden.

Damit besitzt C6e nicht nur ein qualitatives Widerspruchsargument, sondern ein explizites positives Variationszertifikat.

### Quantitative Firewall

(C1zB2C6e.40) ist **noch keine brauchbare asymptotische C3/C4-Skala für `\Delta_T^{(1)}`**.

Offen sind insbesondere uniforme Kontrollen von

\[
\varepsilon_T
\]

und

\[
\langle v_T,A_Tv_T\rangle.
\]

Die arithmetischen Breakpoints können mit wachsendem `T` dichter werden; aus der bloßen Endlichkeit für jedes feste `T` folgt kein uniformer Mindestabstand.

Deshalb wird hier ausdrücklich **nicht** behauptet

\[
\Delta_T^{(1)}\gtrsim e^{\alpha T}T^{-\beta}
\]

oder irgendeine andere natürliche asymptotische Größenordnung.

Status:

\[
\boxed{?[O]_{\rm quantitative\text{-}\Delta\text{-}scale}.}
\]

---

# 13. Konsequenz für den C6d-Hankelrang

C6d hatte

\[
\det\mathbf K_T^{(1)}
=
\mu_{T,0}\Delta_T^{(1)}
\]

mit

\[
\mu_{T,0}=\langle\mathbf1_T,A_T\mathbf1_T\rangle>0
\]

gezeigt.

Daher folgt aus Satz C1zB2C6e.3:

\[
\boxed{
\det\mathbf K_T^{(1)}>0
\qquad(T\ge T_0).
}
\tag{C1zB2C6e.41}
\]

Äquivalent:

\[
\boxed{
\dim\mathscr K_{T,1}^{\rm resp}=2
\qquad(T\ge T_0).
}
\tag{C1zB2C6e.42}
\]

Somit existiert für alle hinreichend großen `T` die normierte zweite Probe

\[
\boxed{
\widehat\psi_{T,1}
=
\frac{
\mathfrak S_T\zeta_T
-
(\mu_{T,1}/\mu_{T,0})\zeta_T
}{
\sqrt{\Delta_T^{(1)}}
}.
}
\tag{C1zB2C6e.43}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm pos,Krylov\text{-}rank\text{-}2}.}
\]

### Supersession-Scope

C6e supersediert damit den C6d-Befund

\[
\checkmark[M]_{\rm neg,Krylov\text{-}rank\text{-}unproved}
\]

**nur im atomaren `N=1`-Scope und nur eventual in `T`.**

Für

\[
N\ge2
\]

bleibt weiterhin offen, ob

\[
\det\mathbf K_T^{(N)}>0
\]

für alle hinreichend großen `T` gilt.

---

# 14. Warum dieser Beweis C4 nicht rückwärts überinterpretiert

C4 kontrolliert die eine skalare Beobachtung

\[
\langle\mathcal X_{R,T}F,\zeta_T\rangle
=
\langle J_{R,T}f,H_T\mathbf1_T\rangle
\]

und entwickelt sie in unendlich vielen Source-Jetkoeffizienten.

C6d stellte klar:

\[
\text{viele C4-Jets}
\ne
\text{viele targetseitige Probes}.
\]

C6e respektiert diese Firewall vollständig.

Die zweite Probe wird nicht aus einem höheren C4-Koeffizienten postuliert. Ihre Existenz wird aus einer neuen, unabhängigen Struktur bewiesen:

\[
\boxed{
\text{Cross-Prime-Gramkante des skalaren Hubs}
\quad\text{vs.}\quad
\text{prime-pure Restmetrik}.
}
\tag{C1zB2C6e.44}
\]

Das ist exakt die Art zusätzlicher Feshbach-Geometrie, die C6c/C6d verlangt hatten.

---

# 15. Was C6e noch nicht über die zweite Probe weiß

Die Existenz von `\widehat\psi_{T,1}` beantwortet nur den Rangtest.

Noch nicht bewiesen ist die Jet-Ausrichtung

\[
\langle
\xi_{R,m}^{(T)},
\widehat\psi_{T,1}
\rangle
\]

für `m=0,1`.

Insbesondere folgt aus C6e nicht, dass

\[
\mathcal P_T^{(1)}
=
\begin{pmatrix}
\langle\xi_{R,0}^{(T)},\widehat\psi_{T,0}\rangle &
\langle\xi_{R,1}^{(T)},\widehat\psi_{T,0}\rangle\\
\langle\xi_{R,0}^{(T)},\widehat\psi_{T,1}\rangle &
\langle\xi_{R,1}^{(T)},\widehat\psi_{T,1}\rangle
\end{pmatrix}
\]

eine kontrollierte kleinste Singularzahl besitzt.

Auch folgt noch nicht

\[
\varepsilon_T^{\rm probe}(R,1)\to0,
\]

und erst recht nicht

\[
\tau_T(E_{R,1})\to0
\]

oder

\[
\Theta_{T,U}^{E_{R,1}}\to I.
\]

Status:

\[
\boxed{?[O]_{\rm second\text{-}probe\text{-}jet\text{-}alignment}.}
\]

---

# 16. No-Go-Persistenzmatrix

| Früherer Knoten | Gesiegelter Befund | Wirkung in C6e |
|---|---|---|
| C1y | translationsinvariante Regulatoren lösen den Hub/Rest-Konflikt im C1y-Scope nicht | unverändert; der Separator benutzt gerade die source-windowed Randgeometrie |
| B2-A | kein endlicher Schattenklassenabschluss durch Gamma-Präkonditionierung | unverändert; keinerlei Kompaktheits-/Schattenargument |
| B2-B | naiver Haar-`L^2`-Grenzendpunkt reicht nicht | unverändert |
| C4 | unendliche Jet-Hierarchie; kein fixer endlicher Jet reicht global | unverändert |
| C5/C6a | totale Odd-Divergenz auf dichtem glattem Kern | unverändert |
| C6 | kein voller Odd-Transport durch festen endlichen Jetquotienten | unverändert |
| C6a | Triangularität der nativen Jettransitionen reicht analytisch nicht | unverändert |
| C6a | Self-Grams allein bestimmen Cross-Terminal-Geometrie nicht | unverändert |
| C6b | C2-Flachheit allein reicht nicht | unverändert |
| C6c | `tau=>kappa` auf festem Fenster | unverändert |
| C6c | Rank-one-C4-Information reicht nicht zur vollen Response-Kontrolle | unverändert; C6e beweist nur die Existenz einer zweiten Krylov-Richtung |
| C6d | C4-Jets sind keine Multi-Probes | unverändert |
| C6d | Orthogonalität impliziert keine Jet-Ausrichtung | unverändert |
| C6d | primitive `A_T`-Krylov-Familie kollabiert | unverändert |
| C6d | allgemeiner Krylov-Rang unbewiesen | präzisiert: `N=1` eventual positiv; `N>=2` offen |
| C5e | gerader Gamma-Gauge konvergiert | nur Vergleich; kein Import in Odd |

---

# 17. Was C6e supersediert — und was nicht

C6e supersediert genau die offene C6d-Frage

\[
\Delta_T^{(1)}>0\ ?
\]

für große `T`.

Das Urteil lautet nun:

\[
\boxed{
\Delta_T^{(1)}>0
\qquad(T\gg1).
}
\tag{C1zB2C6e.45}
\]

Damit ist bewiesen, dass die konkrete P11-Feshbach-Kolligation tatsächlich mehr als die eine C4-Konstantenprobe erzeugt.

Nicht supersediert werden:

- der allgemeine `N`-Krylov-Rangtest;
- die Jet-Alignment-Firewall;
- die finite-window Tailfrage `tau`;
- die Cross-Terminal-Frage `Theta`;
- die Unterscheidung `\varepsilon_T^{probe}\ne\tau_T`;
- irgendeiner der älteren strukturellen No-Gos.

---

# 18. Exakter nächster Arbeitsauftrag C6f

Nach C6e ist die Existenz der zweiten Probe kein Engpass mehr.

Der nächste atomare Punkt ist die **quantitative Nutzbarkeit** dieser Probe.

Zuerst sollte nicht sofort ein allgemeiner `N=2`-Krylov-Rang angegriffen werden. Stattdessen ist auf dem bereits gesicherten Zwei-Probe-Raum zu klären:

1. Kann die Separatoruntergrenze
   \[
   \Delta_T^{(1)}
   \ge
   \frac{\varepsilon_T^2|J_T|^2}
   {\langle v_T,A_Tv_T\rangle}
   \]
   in eine robuste natürliche `T`-Skala übersetzt werden?
2. Lässt sich der mikroskopische Breakpoint-Abstand `\varepsilon_T` durch einen gröberen, arithmetisch stabilen Testvektor ersetzen?
3. Welche Größenordnung besitzt
   \[
   \langle\xi_{R,m}^{(T)},\widehat\psi_{T,1}\rangle,
   \qquad m=0,1?
   \]
4. Ist die `2x2`-Probe-Matrix `\mathcal P_T^{(1)}` nach natürlicher Zeilenskalierung asymptotisch nichtsingulär?

Der logisch erste Unterknoten ist damit:

\[
\boxed{
\text{C6f: quantitative Cross-Prime-Separation und Skala von }\Delta_T^{(1)}.
}
\]

Erst wenn diese Skala kontrolliert ist, ist die normierte zweite Probe analytisch stabil genug für einen ernsthaften Jet-Alignment-Test.

---

# 19. Endurteil

C6e liefert erstmals einen **positiven echten Multi-Probe-Rangbefund** innerhalb des ungeraden P11-Feshbach-Strangs:

\[
\boxed{
\exists T_0<\infty\ \forall T\ge T_0:
\quad
\det\mathbf K_T^{(1)}>0,
\quad
\Delta_T^{(1)}>0,
\quad
\dim\mathscr K_{T,1}^{\rm resp}=2.
}
\tag{C1zB2C6e.46}
\]

Der Beweis beruht auf einer konkreten strukturellen Differenz:

\[
\boxed{
\text{Hub-Gram besitzt Cross-Prime-Kanten,}
\qquad
\text{Rest-Gram bleibt prime-pure.}
}
\tag{C1zB2C6e.47}
\]

Die beiden festen Paare `(2,3)` und `(2,5)` garantieren, dass für jeden hinreichend großen Terminalhorizont mindestens eine solche Hubkante keine Restkante ist. Ein lokaler Differenzindikator über dieser Kante liefert den expliziten Separator und damit `\Delta_T^{(1)}>0`.

Die offene Front verschiebt sich dadurch von der **Existenz** zur **Skala und Ausrichtung** der zweiten Probe.
