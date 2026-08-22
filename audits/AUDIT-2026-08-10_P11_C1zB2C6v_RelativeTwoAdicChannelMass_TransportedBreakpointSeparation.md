# P11-C1z-B2-C6v — Relative 2-adische Kanalmasse und transportierte Breakpoint-Separation

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6v]`  
**Direkte Voraussetzungen:** C1z-B, C1z-B2-C3, C1z-B2-C6g, C1z-B2-C6h, C1z-B2-C6i, C1z-B2-C6q, C1z-B2-C6r, C1z-B2-C6s, C1z-B2-C6t, C1z-B2-C6u  
**Strukturelle Schnittstellen:** C1z-B2-C4, C1z-B2-C6a, C1z-B2-C6e, C1z-B2-C6f, C1z-B2-C6j, C1z-B2-C6m, C1z-B2-C6n, C1z-B2-C6o, C1z-B2-C6p  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d `orthogonality != jet alignment`, C1z-B2-C6k `current data != Wronskian nonzero`, C1z-B2-C6l `C4 constant-mode mechanism does not transfer`, C1z-B2-C6m `A-orthogonality != bulk cancellation`, C1z-B2-C6n `positivity != alignment`, C1z-B2-C6o `raw support separation route fails`, C1z-B2-C6p `fixed-vector divergence != moving-vector control`, C1z-B2-C6q `cross-prime provenance != rest smallness`, C1z-B2-C6r `moment orthogonality != q_r small`, C1z-B2-C6s `same order != cancellation`, C1z-B2-C6t `nonzero first channel != quantitative relative rest loading`, C1z-B2-C6u `fixed jump / vanishing lower bound != q_r asymptotic classification`.  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
\begin{aligned}
[P11\text{-}C1z\text{-}B2\text{-}C6v]
\quad&
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm corr,e^{-6T}\text{-}transport\text{-}not\text{-}automatic}
\\
&+
\checkmark[M]_{\rm neg,raw\text{-}transported\text{-}candidate\text{-}separation}
+
\checkmark[M]_{\rm pos,synchronized\text{-}two\text{-}adic\text{-}near\text{-}collision\text{-}family}
\\
&+
\checkmark[M]_{\rm neg,single\text{-}prime\text{-}ambient\text{-}coercivity}
+
\checkmark[M]_{\rm neg,fixed\text{-}jump\not\Rightarrow relative\text{-}channel\text{-}mass}
\\
&+
\checkmark[M]_{\rm pos,mixed\text{-}prime\text{-}frame\text{-}reduction}
+
\checkmark[M]_{\rm corr,same\text{-}prime\text{-}depths\text{-}share\text{-}bulk\text{-}null\text{-}lattice}
\\
&+
?[O]_{\rm actual\text{-}\rho_T^{(2)}\text{-}coefficient\text{-}separation}
+
?[O]_{\rm residual\text{-}specific\text{-}mixed\text{-}prime\text{-}observability}
\\
&+
?[O]_{\rm q_r\text{-}asymptotic}
+
?[O]_{\rm second\text{-}alignment\text{-}scalar\neq0}.
\end{aligned}
}
\]

C6v trennt die zwei in C6u bewusst offengelassenen Fragen strikt:

1. **Geometrie:** Kann der Isolationsradius des transportierten ersten 2-adischen Kanals allein aus der bekannten Breakpoint-Typisierung quantitativ nach unten beschränkt werden?
2. **Relative Masse:** Kann der einzelne Kanal `(p,a)=(2,0)` einen festen Anteil der Residualnorm tragen?

Das Ergebnis ist in beiden Richtungen restriktiver als die naheliegende Fortsetzung von C6u.

- Die zunächst vermutete Skala `e^{-6T}` folgt **nicht** durch bloßes Anhängen eines zusätzlichen `2^k`-Faktors an C6is `e^{-4T}`-Argument. Es gibt eine explizite synchronisierte Familie transportierter Hubkandidaten, die für `q=3,5,7` gleichzeitig beliebig nahe an die jeweiligen Beobachtungspunkte heranrückt. Daher kann eine quantitative Schranke für den **tatsächlichen** Radius `rho_T^{(2)}` nur noch über die tatsächlichen Sprungkoeffizienten und ihre Nichtcancellation bewiesen werden, nicht über die rohe Kandidatenmenge.
- Der einzelne 2-adische Hub besitzt auf der translationsinvarianten Bulk-Ebene eine exakte Fourier-Nullstellenlattice. Daraus folgt ein echter ambienter No-Go gegen eine uniforme Koerzivität auf `1_T^perp`. Insbesondere reichen die bisher bekannten Eigenschaften des Residualvektors — Mittelwertnullheit und ein fester lokaler gefilterter Sprung — nicht aus, um
  \[
  \mathcal E_{2,0,T}(r_T)\ge c\|r_T\|^2
  \]
  mit festem `c>0` zu erzwingen.
- Der korrekte nächste positive Zieltyp ist deshalb eine **mixed-prime Martingal-/Frame-Ungleichung auf dem konkreten Residualvektor**. Mehr 2-adische Tiefen allein beseitigen die 2-adische Bulk-Nullstellenlattice nicht; mindestens ein anderer Primkanal oder eine zusätzliche residualspezifische Spektralinformation ist erforderlich.

Keiner dieser Befunde klassifiziert `q_{r,T}` asymptotisch.

---

# 0. Verbindliche Ausgangsdaten

Auf

\[
\mathscr H_T=L^2(-T,T)
\]

stehen

\[
\boxed{
A_T:=I+R_T^*R_T,
\qquad
h_T:=H_T^*H_T\mathbf1_T,
}
\tag{C1zB2C6v.1}
\]

\[
\boxed{
\lambda_T
:=
\frac{\langle\mathbf1_T,h_T\rangle}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}
\ge0,
}
\tag{C1zB2C6v.2}
\]

und

\[
\boxed{
r_T:=h_T-\lambda_TA_T\mathbf1_T.
}
\tag{C1zB2C6v.3}
\]

Die einzige hier benutzte exakte Residualorthogonalität ist

\[
\boxed{
\langle r_T,\mathbf1_T\rangle=0.
}
\tag{C1zB2C6v.4}
\]

Es wird ausdrücklich **nicht** benutzt:

\[
\lambda_T\asymp Te^T.
\]

Diese Asymptotik ist in der bisherigen Kette nicht bewiesen.

C6s liefert

\[
\boxed{
\|R_Tr_T\|^2
=
\sum_{p,a}\mathcal E_{p,a,T}(r_T),
\qquad
\mathcal E_{p,a,T}(r_T)\ge0.
}
\tag{C1zB2C6v.5}
\]

C6t identifiziert

\[
\boxed{
\mathcal E_{2,0,T}(r_T)
=
\int_{\Omega_{2,0,T}}
|H_{2,T}r_T(u)|^2\,du,
}
\tag{C1zB2C6v.6}
\]

mit

\[
\boxed{
\Omega_{2,0,T}
=
\left[-T+\delta,T-\delta\right],
\qquad
\delta:=\frac12\log2,
}
\tag{C1zB2C6v.7}
\]

und

\[
\boxed{
H_{2,T}
=
\sqrt{\log2}
\sum_{k\ge1}
2^{-3k/4}K_{k\log2},
}
\tag{C1zB2C6v.8}
\]

wobei nur aktive Terme beitragen.

C6t liefert ferner einen Selektor

\[
q_T\in\{3,5,7\}
\]

und

\[
\boxed{
u_T:=T-\frac12\log q_T}
\tag{C1zB2C6v.9}
\]

mit eventual

\[
\boxed{
\left|
\operatorname{Jump}_{u_T}H_{2,T}r_T
\right|
\ge j_0>0.
}
\tag{C1zB2C6v.10}
\]

C6u definiert

\[
\boxed{
F_T:=H_{2,T}r_T
}
\tag{C1zB2C6v.11}
\]

und

\[
\boxed{
\rho_T^{(2)}
:=
\frac12
\operatorname{dist}
\left(
 u_T,
(\mathcal B(F_T)\cup\partial\Omega_{2,0,T})
\setminus\{u_T\}
\right).
}
\tag{C1zB2C6v.12}
\]

Für jedes feste hinreichend große `T` gilt

\[
\rho_T^{(2)}>0
\]

und

\[
\boxed{
\mathcal E_{2,0,T}(r_T)
\ge
\frac{j_0^2}{4}\rho_T^{(2)}.
}
\tag{C1zB2C6v.13}
\]

C6u beweist außerdem ohne scharfe `lambda_T`-Asymptotik

\[
\boxed{
\|r_T\|^2\lesssim T^4e^{3T}.
}
\tag{C1zB2C6v.14}
\]

Daher gilt nur

\[
\boxed{
q_{r,T}
\gtrsim
\frac{\rho_T^{(2)}}{T^4e^{3T}}.
}
\tag{C1zB2C6v.15}
\]

Eine gegen null gehende Untergrenze auf der rechten Seite klassifiziert `q_{r,T}` nicht.

---

# 1. Teil A — was C6i tatsächlich auf die transportierte Geometrie überträgt

C6i bewies an einem **untransportierten** Cross-Prime-Punkt einen Radius

\[
\rho_T^A\ge c_Ae^{-4T}
\]

gegen die prime-pure Breakpointmenge von `A_T\mathbf1_T`.

C6v benötigt dagegen Breakpoints von

\[
F_T=H_{2,T}r_T.
\]

Aus der C6t-Transportformel

\[
\operatorname{Jump}_u(K_{k\log2}f)
=
J_f(u+k\delta)-J_f(u-k\delta)
\]

folgt nur die Mengeninklusion

\[
\boxed{
\mathcal B(F_T)
\subseteq
\bigcup_{k\ {m aktiv}}
\left(
\mathcal B(r_T)-k\delta
\right)
\cup
\left(
\mathcal B(r_T)+k\delta
\right),
}
\tag{C1zB2C6v.16}
\]

wobei nach dem Summieren einzelne Kandidaten wegen Sprungcancellation verschwinden können.

C6g/C6h geben für die beiden Bestandteile des Residuals die Typisierung:

- Hubbreakpoints von `h_T` liegen in Familien
  \[
  \pm T+\frac12
  (\varepsilon_1\log n+\varepsilon_2\log m),
  \qquad
  \varepsilon_i\in\{-1,0,1\},
  \]
  mit aktiven Prime-Power-Labels `n,m`;
- Breakpoints von `A_T\mathbf1_T` sind prime-pure.

Formal erhöht der zusätzliche Faktor `2^k` die naive multiplikative Höhe. Das erklärt, warum zunächst eine Skala wie `e^{-6T}` naheliegt.

Aber genau hier liegt eine neue Firewall:

\[
\boxed{
\text{Höhenkontrolle allein ist noch keine Separation der transportierten Kandidaten.}
}
\tag{C1zB2C6v.17}
\]

Der Grund ist eine synchronisierte Familie, die im nächsten Abschnitt explizit wird.

---

# 2. Synchronisierte 2-adische Near-Collision-Familie

Fixiere zunächst eine der drei ungeraden Primzahlen

\[
q\in\{3,5,7\}.
\]

Für `j>=1` betrachte im Hub-Paarsektor die Labels

\[
2^j,\qquad q.
\]

Die C6g-Kantentypisierung erlaubt die linksseitige Differenzkante

\[
\boxed{
b_{q,j}(T)
:=-T+rac12(j\log2-\log q).
}
\tag{C1zB2C6v.18}
\]

Sie ist genau die Differenzlage des Paares `(2^j,q)`.

Wichtig ist, dass diese Lage nicht aus einer willkürlichen neuen Arithmetik stammt: sie ist bereits Teil der in C6g klassifizierten Hub-Paarfamilie. Die Ratio

\[
\frac{2^j}{q}
\]

ist cross-prime und kann nicht mit einer prime-puren Restlage

\[
p^m
\]

identifiziert werden. Insbesondere gibt es keinen automatischen `A_T\mathbf1_T`-Breakpoint mit derselben multiplikativen Marke.

Transportiere nun diese Lage im `k`-ten 2-adischen Hubterm um `+k\delta`. Es entsteht der Kandidat

\[
\boxed{
v_{q,j,k}(T)
:=
b_{q,j}(T)+k\delta
=
-T+rac12((j+k)\log2-\log q).
}
\tag{C1zB2C6v.19}
\]

Vergleiche ihn mit dem C6t-Beobachtungspunkt

\[
u_q(T)=T-rac12\log q.
\]

Dann gilt **exakt**

\[
\begin{aligned}
u_q(T)-v_{q,j,k}(T)
&=
T-rac12\log q
+
T-rac12((j+k)\log2-\log q)
\\
&=
2T-rac12(j+k)\log2.
\end{aligned}
\]

Also

\[
\boxed{
|u_q(T)-v_{q,j,k}(T)|
=
\left|
2T-rac12(j+k)\log2
\right|.
}
\tag{C1zB2C6v.20}
\]

Der entscheidende Punkt lautet:

\[
\boxed{
\text{Die rechte Seite ist vollständig unabhängig von }q.
}
\tag{C1zB2C6v.21}
\]

Der Drei-Prim-Selektor kann diese Familie daher auf bloßer Ortsgeometrie **nicht** auseinanderziehen.

## 2.1 Eine besonders scharfe Sequenz

Setze

\[
j=k=N
\]

und

\[
\boxed{
T_N:=\frac N2\log2.
}
\tag{C1zB2C6v.22}
\]

Dann gilt

\[
2T_N=N\log2
=
\frac12(j+k)\log2.
\]

Folglich

\[
\boxed{
v_{q,N,N}(T_N)=u_q(T_N)}
\tag{C1zB2C6v.23}
\]

für **alle drei** `q=3,5,7` gleichzeitig.

Die Aktivitätsbedingungen sind genau auf der zulässigen Skala:

\[
2^N=e^{2T_N}.
\]

Für

\[
T=T_N+\varepsilon,
\qquad
\varepsilon>0,
\]

bleiben sowohl das Hublabel `2^N` als auch der `N`-te 2-adische Transportterm aktiv, und

\[
\boxed{
|u_q(T)-v_{q,N,N}(T)|=2\varepsilon
}
\tag{C1zB2C6v.24}
\]

wieder gleichzeitig für `q=3,5,7`.

Da `\varepsilon` beliebig klein gewählt werden kann, besitzt die **rohe transportierte Kandidatenmenge** keine uniforme exponentielle Separation

\[
ce^{-\alpha T}
\]

für irgendein festes `\alpha>0`.

Insbesondere ist die informelle Schlusskette

\[
\text{C6i: }e^{-4T}
+
\text{ein zusätzlicher }2^k\text{-Faktor}
\Longrightarrow
\rho_T^{(2)}\gtrsim e^{-6T}
\]

nicht gültig.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,e^{-6T}\text{-}transport\text{-}not\text{-}automatic}
+
\checkmark[M]_{\rm pos,synchronized\text{-}two\text{-}adic\text{-}near\text{-}collision\text{-}family}.
}
\tag{C1zB2C6v.25}
\]

---

# 3. Präzise Firewall: Kandidaten-No-Go ist noch kein No-Go für `rho_T^{(2)}`

Hier muss die Source-/Target-Logik streng bleiben.

Definiere die rohe transportierte Kandidatenmenge

\[
\boxed{
\mathcal C_T^{\rm tr}
:=
\bigcup_{k\ {m aktiv}}
\left(
\mathcal B(r_T)-k\delta
\right)
\cup
\left(
\mathcal B(r_T)+k\delta
\right).
}
\tag{C1zB2C6v.26}
\]

Dann gilt nur

\[
\boxed{
\mathcal B(F_T)\subseteq\mathcal C_T^{\rm tr}.
}
\tag{C1zB2C6v.27}
\]

Eine Kandidatenlage kann in der gewichteten Summe

\[
H_{2,T}r_T
=
\sqrt{\log2}
\sum_k2^{-3k/4}K_{k\log2}r_T
\]

wegcancellieren.

Daher folgt aus (C1zB2C6v.24) **nicht** automatisch

\[
\rho_T^{(2)}\to0
\]

und auch nicht, dass irgendeine konkrete exponentielle Untergrenze für den tatsächlichen Radius falsch ist.

Was bewiesen ist, ist genau die methodische Negativaussage:

\[
\boxed{
\text{Eine Untergrenze für }\rho_T^{(2)}
\text{ kann nicht durch Separation der rohen transportierten Labelmenge allein bewiesen werden.}
}
\tag{C1zB2C6v.28}
\]

Der fehlende Schritt ist jetzt **koeffizientenempfindlich**:

> Man müsste auf der synchronisierten Familie (C1zB2C6v.19) den tatsächlichen Sprung
> \[
> \operatorname{Jump}_{v_{q,j,k}(T)}F_T
> \]
> auswerten und entscheiden, ob er verschwindet oder nicht.

Erst danach kann eine quantitative Aussage über den tatsächlichen Radius `rho_T^{(2)}` getroffen werden.

Damit wird die C6u-Frage A nicht positiv geschlossen, sondern schärfer lokalisiert:

\[
\boxed{
?[O]_{\rm actual\text{-}\rho_T^{(2)}\text{-}coefficient\text{-}separation}.
}
\tag{C1zB2C6v.29}
\]

Status der bloßen Kandidatenroute:

\[
\boxed{
\checkmark[M]_{\rm neg,raw\text{-}transported\text{-}candidate\text{-}separation}.
}
\tag{C1zB2C6v.30}
\]

---

# 4. Teil B — der relevante relative Kanalquotient

Definiere den ersten 2-adischen Beobachtungsoperator

\[
\boxed{
\mathcal C_{2,T}f
:=
1_{\Omega_{2,0,T}}H_{2,T}f.
}
\tag{C1zB2C6v.31}
\]

Dann ist

\[
\boxed{
\mathcal E_{2,0,T}(f)
=
\|\mathcal C_{2,T}f\|^2.
}
\tag{C1zB2C6v.32}
\]

Für das konkrete Residuum setze tautologisch

\[
\boxed{
c_T^{(2)}
:=
\frac{\mathcal E_{2,0,T}(r_T)}{\|r_T\|^2}
}
\tag{C1zB2C6v.33}
\]

sofern `r_T\ne0`.

C6t beweist eventual

\[
c_T^{(2)}>0.
\]

Die offene Frage ist aber gerade, ob

\[
\boxed{
\inf_{T\gg1}c_T^{(2)}>0
}
\tag{C1zB2C6v.34}
\]

oder wenigstens eine anderweitig hinreichend starke quantitative Untergrenze folgt.

C6v zeigt nun, dass eine solche Schranke **nicht** als ambienter Operatorbound für den einzelnen 2-adischen Kanal verfügbar ist.

---

# 5. Fourier-Symbol des unendlichen 2-adischen Bulk-Hubs

Ignoriere für diesen Abschnitt nur die Fenstergrenzen und betrachte den translationsinvarianten Vollraumoperator

\[
\boxed{
H_{2,\infty}
:=
\sqrt{\log2}
\sum_{k\ge1}2^{-3k/4}D_{k\log2}.
}
\tag{C1zB2C6v.35}
\]

Dabei ist

\[
(D_sf)(u)=f(u+s/2)-f(u-s/2).
\]

Für die Fouriermode `e^{i\xi u}` gilt

\[
D_se^{i\xi u}
=
2i\sin(\xi s/2)e^{i\xi u}.
\]

Setze

\[
r:=2^{-3/4},
\qquad
\theta:=\frac{\xi\log2}{2}.
\]

Dann ist das Symbol

\[
\begin{aligned}
m_2(\xi)
&=
2i\sqrt{\log2}
\sum_{k\ge1}r^k\sin(k\theta)
\\
&=
2i\sqrt{\log2}
\frac{r\sin\theta}
{1-2r\cos\theta+r^2}.
\end{aligned}
\]

Also exakt

\[
\boxed{
m_2(\xi)=0
\iff
\sin\left(\frac{\xi\log2}{2}\right)=0.}
\tag{C1zB2C6v.36}
\]

Damit besitzt der 2-adische Hub die nichttriviale Nullstellenlattice

\[
\boxed{
\xi_m
=
\frac{2\pi m}{\log2},
\qquad
m\in\mathbb Z.
}
\tag{C1zB2C6v.37}
\]

Nicht nur die Konstantenmode `m=0`, sondern unendlich viele **nichtkonstante** Bulk-Frequenzen werden exakt ausgelöscht.

Dies ist der zentrale ambient-spectral No-Go.

---

# 6. Endliche-Fenster-Quasimoden: keine uniforme Koerzivität auf `1_T^perp`

Wähle die erste nichttriviale Nullfrequenz

\[
\boxed{
\xi_*:=\frac{2\pi}{\log2}.
}
\tag{C1zB2C6v.38}
\]

und für großes `T` die reelle Funktion

\[
\boxed{
f_T(u)
:=
1_{[-T/2,T/2]}(u)\sin(\xi_*u).
}
\tag{C1zB2C6v.39}
\]

Wegen der Oddness gilt exakt

\[
\boxed{
\langle f_T,\mathbf1_T\rangle=0.
}
\tag{C1zB2C6v.40}
\]

Außerdem

\[
\boxed{
\|f_T\|^2\asymp T.
}
\tag{C1zB2C6v.41}
\]

Fixiere `k`. Solange beide verschobenen Punkte innerhalb des zentralen Trägerintervalls liegen,

\[
\begin{aligned}
D_{k\log2}f_T(u)
&=
\sin(\xi_*(u+k\delta))
-
\sin(\xi_*(u-k\delta))
\\
&=
2\cos(\xi_*u)\sin(k\pi)
\\
&=0.
\end{aligned}
\tag{C1zB2C6v.42}
\]

Der `k`-te Term lebt also nur in den durch die Trägerkante erzeugten Übergangsbereichen. Deren Gesamtlänge ist `O(k)`, und die Amplitude ist universell beschränkt. Daher

\[
\boxed{
\|K_{k\log2}f_T\|
\le C\sqrt{k}
}
\tag{C1zB2C6v.43}
\]

mit einer von `T,k` unabhängigen Konstante `C`; für sehr große `k` ist die triviale Fensterschranke noch kleiner als eine geeignete `C\sqrt{k}`-Majorante.

Somit

\[
\begin{aligned}
\|H_{2,T}f_T\|
&\le
\sqrt{\log2}
\sum_{k\ge1}2^{-3k/4}
\|K_{k\log2}f_T\|
\\
&\le
C\sqrt{\log2}
\sum_{k\ge1}2^{-3k/4}\sqrt{k}
\\
&\le C_2<\infty,
\end{aligned}
\tag{C1zB2C6v.44}
\]

uniform in `T`.

Da die Einschränkung auf `Omega_{2,0,T}` die Norm nur verkleinert,

\[
\boxed{
\mathcal E_{2,0,T}(f_T)
\le C_2^2.
}
\tag{C1zB2C6v.45}
\]

Zusammen mit (C1zB2C6v.41) folgt

\[
\boxed{
\frac{\mathcal E_{2,0,T}(f_T)}{\|f_T\|^2}
\lesssim
\frac1T
\longrightarrow0.
}
\tag{C1zB2C6v.46}
\]

Damit ist bewiesen:

\[
\boxed{
\not\exists c>0\ \forall T\gg1\ \forall f\perp\mathbf1_T:
\quad
\mathcal E_{2,0,T}(f)\ge c\|f\|^2.
}
\tag{C1zB2C6v.47}
\]

Die Mittelwertnullheit des echten Residuals kann also allein keine uniforme erste-Kanal-Koerzivität liefern.

Da der 2-adische Hub als Operator auf `L^2` uniform beschränkt ist, können die glatten Quasimoden außerdem in `L^2` durch stückweise konstante Funktionen approximiert werden. Die bloße Tatsache, dass die konkreten P11-Vektoren stückweise sind, entfernt diesen ambienten No-Go nicht.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,single\text{-}prime\text{-}ambient\text{-}coercivity}.
}
\tag{C1zB2C6v.48}
\]

---

# 7. Selbst der feste C6t-Sprung erzwingt keine relative Masse

C6t/C6u besitzen mehr als nur Mittelwertnullheit: für den echten Residualvektor existiert ein fester Sprung

\[
\left|\operatorname{Jump}_{u_T}\mathcal C_{2,T}r_T\right|
\ge j_0.
\]

Aber auch diese lokale Information beseitigt den ambienten Mechanismus aus §6 nicht.

Man kann zu `f_T` ein mittelwertfreies lokales Haarpaket `w_T` von **uniform beschränkter** `L^2`-Norm addieren, dessen 2-adisch gefiltertes Bild an einem vorgegebenen inneren Punkt einen nichtverschwindenden Sprung besitzt. Nach fester Reskalierung kann dieser Sprung auf eine vorgegebene positive Größe normiert werden.

Setze abstrakt

\[
g_T:=f_T+w_T.
\]

Dann kann man zugleich erreichen:

\[
\langle g_T,\mathbf1_T\rangle=0,
\]

\[
|\operatorname{Jump}_{u_T}\mathcal C_{2,T}g_T|
\ge j_*>0,
\]

aber weiterhin

\[
\|g_T\|^2\asymp T
\]

und

\[
\|\mathcal C_{2,T}g_T\|^2=O(1).
\]

Somit

\[
\boxed{
\frac{\|\mathcal C_{2,T}g_T\|^2}{\|g_T\|^2}
\to0
}
\tag{C1zB2C6v.49}
\]

bei gleichzeitig festem lokalem gefiltertem Sprung.

Diese Konstruktion ist **kein Modell des konkreten `r_T`**. Ihre Rolle ist ausschließlich die logische Firewall:

\[
\boxed{
\langle r_T,1_T\rangle=0
+
|\operatorname{Jump}_{u_T}H_{2,T}r_T|\ge j_0
\not\Rightarrow
\mathcal E_{2,0,T}(r_T)\ge c\|r_T\|^2.
}
\tag{C1zB2C6v.50}
\]

Eine positive relative Schranke muss daher zusätzliche **vektorspezifische** Information über den konkreten Krylov-Residualvektor verwenden.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,fixed\text{-}jump\not\Rightarrow relative\text{-}channel\text{-}mass}.
}
\tag{C1zB2C6v.51}
\]

---

# 8. Was für den konkreten Residualvektor weiterhin offen ist

Der No-Go aus §§5–7 ist ambient. Er beweist **nicht**

\[
c_T^{(2)}\to0
\]

für den konkreten Vektor

\[
r_T=h_T-\lambda_TA_T\mathbf1_T.
\]

Insbesondere bleibt logisch möglich, dass die spezielle arithmetische Entstehung von `r_T` seine Masse von den 2-adischen Nullmoden fernhält.

Dafür liegt bisher aber kein Satz vor.

Benötigt würde beispielsweise mindestens eine der folgenden Arten neuer Information:

1. eine residualspezifische Fourier-/Spektralkonzentrationsaussage, die Masse nahe
   \[
   \frac{2\pi}{\log2}\mathbb Z
   \]
   quantitativ ausschließt;
2. eine direkte Gram-/Frame-Untergrenze auf dem konkreten eindimensionalen Residualray `span{r_T}` mit expliziter, nichtzirkulärer Konstante;
3. eine mixed-prime Beobachtungsungleichung, in der Nullmoden eines Primkanals durch andere Primkanäle gesehen werden.

Keine dieser Aussagen folgt aus C6t/C6u.

Daher bleibt

\[
\boxed{
?[O]_{\rm residual\text{-}specific\text{-}two\text{-}adic\text{-}coercivity}.
}
\tag{C1zB2C6v.52}
\]

---

# 9. Warum zusätzliche 2-adische Tiefen die Bulk-Nullstellen nicht entfernen

C6s definiert für `a>=0`

\[
\Phi_{2,a,T}[f](u)
=
\sum_{k\ge a+1}
2^{-3k/4}(K_{k\log2}f)(u).
\]

Auf der Vollraum-Fouriermode hat der entsprechende Tail das Symbol

\[
\boxed{
m_{2,a}(\xi)
=
2i
\sum_{k\ge a+1}
2^{-3k/4}
\sin\left(k\frac{\xi\log2}{2}\right).
}
\tag{C1zB2C6v.53}
\]

Für jede Frequenz

\[
\xi_m=\frac{2\pi m}{\log2}
\]

gilt termweise

\[
\sin(km\pi)=0.
\]

Also

\[
\boxed{
m_{2,a}(\xi_m)=0
\qquad
\forall a\ge0,
\ \forall m\in\mathbb Z.
}
\tag{C1zB2C6v.54}
\]

Damit teilen **alle 2-adischen Martingaltiefen dieselbe exakte Bulk-Nullstellenlattice**.

Die korrekte Schlussfolgerung ist bewusst begrenzt:

\[
\boxed{
\text{Mehr 2-adische Tiefen allein beseitigen den Bulk-Nullmodusmechanismus nicht.}
}
\tag{C1zB2C6v.55}
\]

Dies ist noch kein No-Go gegen eine mögliche Fenster-/Randkoerzivität der gesamten 2-adischen Tiefenfamilie; deren Tiefengewichte und Randgeometrie müssten separat ausgewertet werden.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,same\text{-}prime\text{-}depths\text{-}share\text{-}bulk\text{-}null\text{-}lattice}.
}
\tag{C1zB2C6v.56}
\]

---

# 10. Ein anderer Primkanal sieht die exakte 2-adische Nullmode

Für eine Primzahl `p` besitzt der volle erste p-Hub analog das Symbol

\[
\boxed{
m_p(\xi)
=
2i\sqrt{\log p}
\frac{p^{-3/4}\sin(\xi\log p/2)}
{1-2p^{-3/4}\cos(\xi\log p/2)+p^{-3/2}}.
}
\tag{C1zB2C6v.57}
\]

Sei erneut

\[
\xi_*:=\frac{2\pi}{\log2}.
\]

Für eine ungerade Primzahl `q` wäre

\[
m_q(\xi_*)=0
\]

nur möglich, wenn

\[
\frac{\log q}{\log2}\in\mathbb Z
\]

beziehungsweise allgemeiner rational wäre. Eine rationale Relation

\[
a\log q=b\log2
\]

mit positiven ganzen `a,b` würde aber

\[
q^a=2^b
\]

erzwingen, im Widerspruch zur eindeutigen Primfaktorzerlegung.

Daher

\[
\boxed{
m_q(\xi_*)\ne0
\qquad(q\text{ ungerade Primzahl}).}
\tag{C1zB2C6v.58}
\]

Das zeigt exakt, was dem einzelnen 2-adischen Kanal fehlt:

> Ein **mixed-prime** Kanal kann die exakte nichttriviale 2-adische Bulk-Nullmode sehen.

Aber daraus darf nicht sofort die globale Frame-Ungleichung

\[
|m_2(\xi)|^2+|m_q(\xi)|^2\ge c>0
\quad\forall\xi
\]

behauptet werden. Nichtgemeinsame exakte Nullstellen schließen beliebig kleine gemeinsame Werte nicht automatisch aus, und außerdem bleiben Fenster-, Tiefen- und Residualeffekte zu kontrollieren.

Somit ist ein zweiter Primkanal **notwendig als Mechanismustyp**, aber aus den aktuellen Daten noch nicht als hinreichend bewiesen.

---

# 11. Die volle Martingalfamilie ist die kanonische relative Zielgröße

Definiere die aktive Indexfamilie

\[
\boxed{
\mathcal I_T
:=
\{(p,a):\Omega_{p,a,T}\ne\varnothing\}.
}
\tag{C1zB2C6v.59}
\]

und den Analyseoperator

\[
\boxed{
\mathcal M_Tf
:=
\left(
\sqrt{(\log p)(p-1)p^a}\,
1_{\Omega_{p,a,T}}
\Phi_{p,a,T}[f]
\right)_{(p,a)\in\mathcal I_T}.
}
\tag{C1zB2C6v.60}
\]

C6s besagt exakt

\[
\boxed{
\|\mathcal M_Tf\|^2
=
\|R_Tf\|^2.
}
\tag{C1zB2C6v.61}
\]

Für das Residuum ist daher

\[
\boxed{
q_{r,T}
=
\frac{\|\mathcal M_Tr_T\|^2}{\|r_T\|^2}.
}
\tag{C1zB2C6v.62}
\]

Die asymptotisch relevante Frage ist jetzt exakt eine residualspezifische Frame-/Observability-Frage:

\[
\boxed{
\|\mathcal M_Tr_T\|^2
\ge
c_T\|r_T\|^2.
}
\tag{C1zB2C6v.63}
\]

Ein uniformes `c_T>=c>0` wäre ein echter Durchbruch für den Restquotienten.

C6v beweist **nicht** eine solche Ungleichung. Es zeigt nur, warum die Reduktion auf den einzelnen Index `(2,0)` dafür strukturell zu schwach ist.

---

# 12. Welche zusätzliche Prime-/Tiefenfamilie ist jetzt tatsächlich notwendig?

Die Frage muss in drei Stufen beantwortet werden.

## 12.1 Was definitiv nicht genügt

Die Familie

\[
\{(2,0)\}
\]

besitzt den ambienten Fourier-No-Go aus §6.

Ebenso beseitigt das bloße Hinzufügen weiterer `p=2`-Tiefen die exakte Bulk-Nullstellenlattice nicht.

Damit ist die Route

\[
\boxed{
\text{„nur 2-adisch, nur durch mehr Tiefe“}
}
\]

als rein bulk-spektrologische Koerzivitätsstrategie blockiert.

## 12.2 Minimal notwendige neue Struktur

Mindestens ein Kanal mit

\[
\boxed{p\ne2}
\]

muss hinzukommen **oder** es muss eine neue residualspezifische Spektralaussage bewiesen werden, die die 2-adischen Nullmoden quantitativ ausschließt.

Die kleinste natürliche mixed-prime Testfamilie ist daher beispielsweise

\[
\boxed{
\mathcal I_T^{\rm test}
=
\{(2,0),(3,0)\}.
}
\tag{C1zB2C6v.64}
\]

Dies ist nur ein **nächster Test**, keine bereits bewiesene ausreichende Familie.

## 12.3 Was aus den aktuellen Daten garantiert zulässig ist

Ohne einen neuen Subframe-Satz darf kein positiver Martingalkanal verworfen werden. Die einzige bereits exakt identifizierte vollständige Familie ist deshalb

\[
\boxed{
\mathcal I_T
=
\{(p,a):\Omega_{p,a,T}\ne\varnothing\}.
}
\tag{C1zB2C6v.65}
\]

mit

\[
\sum_{(p,a)\in\mathcal I_T}
\mathcal E_{p,a,T}(r_T)
=
\|R_Tr_T\|^2.
\]

Daher lautet die gegenprüferfeste Antwort auf die C6v-Frage 5:

\[
\boxed{
\begin{minipage}{0.88\textwidth}
Der einzelne `(2,0)`-Kanal genügt aus den vorhandenen Daten nicht. Mehr `p=2`-Tiefe entfernt den Bulk-Nullmechanismus nicht. Mindestens mixed-prime Information ist erforderlich. Welche echte Unterfamilie bereits hinreichend ist, ist offen; ohne neuen Frame-Satz bleibt die volle aktive Martingalfamilie der einzige kanonisch garantierte Zielraum.
\end{minipage}
}
\tag{C1zB2C6v.66}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,mixed\text{-}prime\text{-}frame\text{-}reduction}.
}
\tag{C1zB2C6v.67}
\]

---

# 13. Antworten auf die fünf C6v-Prüffragen

## Frage 1

> Kann `||r_T||^2` überwiegend in Regionen liegen, die der erste 2-adische Kanal kaum sieht?

**Mit den aktuellen Daten: ja, dies ist nicht ausgeschlossen.**

Präziser ist die Gefahr nicht nur räumlich. Der Kanal sieht

\[
1_{\Omega_{2,0,T}}H_{2,T}r_T,
\]

also eine Kombination aus räumlicher Einschränkung und einem Differenzfilter. §6 zeigt explizite mittelwertfreie Quasimoden, deren Norm wächst wie `T^{1/2}`, während die beobachtete 2-adische Energie beschränkt bleibt.

Für den konkreten `r_T` ist eine solche Konzentration weder bewiesen noch ausgeschlossen.

## Frage 2

> Hat `H_{2,T}` auf dem konkreten Krylov-Residualraum eine vektorspezifische koerzivitätsartige Untergrenze?

Eventual gilt tautologisch

\[
\mathcal E_{2,0,T}(r_T)>0,
\]

aber eine quantitative Untergrenze relativ zu `||r_T||^2` ist **offen**.

Ambient ist eine uniforme Koerzivität falsch.

## Frage 3

> Gibt es einen Daten-No-Go für einen einzelnen Prime-Hubkanal?

Ja, auf ambienter Ebene:

\[
\boxed{
\inf_{\substack{f\perp1_T\\f\ne0}}
\frac{\mathcal E_{2,0,T}(f)}{\|f\|^2}
\not\ge c>0
\text{ uniform in }T.
}
\]

Der No-Go folgt aus der exakten 2-adischen Fourier-Nullstellenlattice und den endlichen-Fenster-Quasimoden.

Er ist ausdrücklich **kein** Beweis gegen eine residualspezifische Untergrenze für das konkrete `r_T`.

## Frage 4

> Kann die volle Martingalsumme relativ besser kontrolliert werden?

Strukturell ja: sie ist exakt die volle Restnorm und besitzt keine Cross-Channel-Cancellation.

Quantitativ ist eine relative Untergrenze aber noch offen. Die Aufgabe ist nun eine Frame-/Observability-Ungleichung für `mathcal M_T` auf `r_T`.

## Frage 5

> Welche zusätzliche Prime-/Tiefenfamilie ist notwendig?

Mindestens mixed-prime Information oder eine neue residualspezifische Spektralausschlussaussage.

Mehr 2-adische Tiefe allein beseitigt die gemeinsame 2-adische Bulk-Nullstellenlattice nicht. Eine natürliche erste mixed-prime Testfamilie ist `(2,0)+(3,0)`, aber ihre Suffizienz ist nicht bewiesen. Ohne neuen Subframe-Satz bleibt die **volle aktive `(p,a)`-Familie** die einzige exakt abgesicherte Zielgröße.

---

# 14. Persistente neue Firewalls aus C6v

C6v fügt drei Aussagen hinzu, die in späteren Knoten nicht still überschrieben werden dürfen.

## C6v-A — transportierte Kandidaten-Separation

\[
\boxed{
\text{C6is }e^{-4T}\text{-Separation überträgt sich nicht durch bloße Höhenzählung auf }F_T.
}
\]

Insbesondere ist `e^{-6T}` nicht aus der bisherigen Labelgeometrie bewiesen.

Die synchronisierte Familie (C1zB2C6v.19) zeigt, dass die rohe transportierte Kandidatenmenge für alle drei C6t-Selektorprimzahlen gleichzeitig arbiträr nahe Gegenkandidaten besitzen kann.

## C6v-B — single-prime relative coercivity

\[
\boxed{
\text{Der einzelne 2-adische erste Kanal ist auf }1_T^\perp\text{ nicht uniform koerziv.}
}
\]

Mittelwertnullheit und ein fixer lokaler gefilterter Sprung reichen nicht.

## C6v-C — same-prime depth firewall

\[
\boxed{
\text{Alle 2-adischen Martingaltiefen teilen im Bulk dieselbe exakte Fourier-Nullstellenlattice.}
}
\]

Daher darf „mehr 2-adische Tiefe“ nicht ohne zusätzlichen Rand-/Frame-Beweis als Lösung des Koerzivitätsproblems behauptet werden.

---

# 15. Was C6v ausdrücklich nicht beweist

C6v beweist **nicht**:

\[
\rho_T^{(2)}\to0,
\]

\[
\rho_T^{(2)}\not\gtrsim e^{-\alpha T},
\]

\[
c_T^{(2)}\to0,
\]

\[
q_{r,T}\to0,
\]

\[
q_{r,T}\not\to0,
\]

oder

\[
a_{R,T}^{(2)}\ne0.
\]

Der erste Teil liefert einen **No-Go für die rohe Kandidaten-Separationsmethode**, nicht für jede denkbare koeffizientenempfindliche Radiusuntergrenze.

Der zweite Teil liefert einen **ambienten** single-prime Koerzivitäts-No-Go, nicht die Asymptotik des konkreten Residualvektors.

---

# 16. Nächster atomarer Knoten

Der nächste sinnvolle Knoten ist

\[
\boxed{[P11\text{-}C1z\text{-}B2\text{-}C6w]}
\]

mit Arbeitstitel etwa

`MixedPrimeFirstChannel_FrameTest_ResidualSpectralAvoidance`.

Er soll **nicht** erneut den einzelnen 2-adischen Sprung quantifizieren, sondern die kleinste mixed-prime Beobachtung testen, beginnend mit

\[
\mathcal E_{2,0,T}(r_T)+\mathcal E_{3,0,T}(r_T).
\]

Atomarer Auftrag:

1. schreibe die beiden Vollraum-Bulksymbole `m_2,m_3` exakt;
2. prüfe, ob die fehlenden gemeinsamen exakten Nullstellen für den **konkreten** Residualvektor in eine quantitative Untergrenze übersetzt werden können;
3. falls nicht, konstruiere den entsprechenden mixed-prime Quasimoden-No-Go und entscheide, ob eine wachsende Primfamilie nötig wird;
4. halte Fenster-/Randbeiträge und Martingaltiefen strikt getrennt;
5. verwende weiterhin keine unbewiesene Asymptotik
   \[
   \lambda_T\asymp Te^T.
   \]

Bis dahin bleibt

\[
\boxed{
P11=\texttt{PASS-A ACTIVE}.
}
\]

Kein SYN, kein Seal, kein `papers/P11`.

---

# 17. Kurzfazit

C6v beantwortet die zwei C6u-Folgefragen mit zwei unterschiedlichen Firewalls.

Erstens ist die transportierte Breakpoint-Geometrie **nicht** einfach C6i plus ein weiterer Höhenfaktor. Die Familie

\[
v_{q,j,k}(T)
=
-T+rac12((j+k)\log2-\log q)
\]
liegt für `q=3,5,7` in exakt demselben Abstand vom jeweiligen

\[
u_q(T)=T-rac12\log q.
\]

Mit `j=k=N` und `T\downarrow N\log2/2` wird dieser Abstand simultan beliebig klein. Deshalb muss jede tatsächliche Untergrenze für `rho_T^{(2)}` jetzt die **Sprungkoeffizienten von `H_{2,T}r_T` selbst** auswerten.

Zweitens besitzt der einzelne 2-adische Hub die Bulk-Nullstellen

\[
\xi_m=\frac{2\pi m}{\log2}.
\]

Daraus entstehen mittelwertfreie endliche-Fenster-Quasimoden mit

\[
\frac{\mathcal E_{2,0,T}(f_T)}{\|f_T\|^2}\to0.
\]

Damit kann der erhoffte feste relative Kanalanteil nicht aus den bisher bekannten abstrakten Residualeigenschaften folgen.

Der nächste zulässige positive Mechanismus ist daher mixed-prime:

\[
\boxed{
\text{single prime}
\longrightarrow
\text{mixed-prime Martingal-/Frame-Observability}.
}
\]

Die volle aktive Martingalfamilie bleibt die einzige bereits exakt mit `||R_Tr_T||^2` identifizierte Zielgröße. Die asymptotische Klassifikation von `q_{r,T}` bleibt offen.
