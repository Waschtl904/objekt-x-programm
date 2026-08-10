# P11-C1z-B2-C6u — 2-adische Kanal-Isolation, relative Energie und Residualnorm-Firewall

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6u]`  
**Direkte Voraussetzungen:** C1z-B, C1z-B2-C3, C1z-B2-C6f, C1z-B2-C6i, C1z-B2-C6q, C1z-B2-C6r, C1z-B2-C6s, C1z-B2-C6t  
**Strukturelle Schnittstellen:** C1z-B2-C4, C1z-B2-C6a, C1z-B2-C6e, C1z-B2-C6g, C1z-B2-C6h, C1z-B2-C6j, C1z-B2-C6m, C1z-B2-C6n, C1z-B2-C6o, C1z-B2-C6p  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d `orthogonality != jet alignment`, C1z-B2-C6k `current data != Wronskian nonzero`, C1z-B2-C6l `C4 constant-mode mechanism does not transfer`, C1z-B2-C6m `A-orthogonality != bulk cancellation`, C1z-B2-C6n `positivity != alignment`, C1z-B2-C6o `raw support separation route fails`, C1z-B2-C6p `fixed-vector divergence != moving-vector control`, C1z-B2-C6q `cross-prime provenance != rest smallness`, C1z-B2-C6r `moment orthogonality != q_r small`, C1z-B2-C6s `same order != cancellation`, C1z-B2-C6t `nonzero first channel != quantitative relative rest loading`.  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6u]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm pos,canonical\text{-}first\text{-}channel\text{-}isolation\text{-}radius}
+
\checkmark[M]_{\rm pos,jump\text{-}to\text{-}channel\text{-}energy\text{-}bound}
+
\checkmark[M]_{\rm pos,lambda\text{-}free\text{-}hub\text{-}operator\text{-}bound}
+
\checkmark[M]_{\rm pos,lambda\text{-}free\text{-}residual\text{-}norm\text{-}upper\text{-}bound}
+
\checkmark[M]_{\rm pos,relative\text{-}rest\text{-}loading\text{-}reduction}
+
\checkmark[M]_{\rm corr,heuristic\text{-}moment\text{-}scales\text{-}unproved}
+
\checkmark[M]_{\rm neg,fixed\text{-}jump\not\Rightarrow q_r\not\to0}
+
\checkmark[M]_{\rm neg,vanishing\text{-}lower\text{-}bound\not\Rightarrow asymptotic\text{-}classification}
+
?[O]_{\rm quantitative\text{-}two\text{-}adic\text{-}channel\text{-}isolation\text{-}radius}
+
?[O]_{\rm q_r\text{-}asymptotic}
+
?[O]_{\rm bare\text{-}angle\text{-}lower\text{-}bound}
+
?[O]_{\rm second\text{-}alignment\text{-}scalar\neq0}
}
\]

C6t bewies eventual einen festen nichtverschwindenden Sprung des ersten `p=2`-Martingalkanals:

\[
\boxed{
\left|
\operatorname{Jump}_{u_T}
H_{2,T}r_T
\right|
\ge j_0>0,
}
\tag{C1zB2C6u.1}
\]

mit

\[
 u_T=u_{q_T}(T)=T-\frac12\log q_T,
\qquad
q_T\in\{3,5,7\},
\]

und daraus

\[
\mathcal E_{2,0,T}(r_T)>0.
\]

C6u quantifiziert zunächst exakt, was ein solcher Sprung für die Kanalenergie liefert, und prüft anschließend, ob diese absolute Information bereits relativ zur Gesamtnorm `||r_T||^2` ausreicht.

Das Ergebnis ist zweigeteilt:

1. **Positiv:** Ein kanonischer Isolationsradius `rho_T^{(2)}` reduziert die absolute Kanalenergie auf
   \[
   \mathcal E_{2,0,T}(r_T)\ge \frac{j_0^2}{4}\rho_T^{(2)}.
   \]
   Zusätzlich folgt ohne jede scharfe `lambda_T`-Asymptotik die grobe, aber explizite Obergrenze
   \[
   \|r_T\|^2\lesssim T^4e^{3T}.
   \]
   Damit
   \[
   q_{r,T}\gtrsim \frac{\rho_T^{(2)}}{T^4e^{3T}}.
   \]
2. **Negativ:** Selbst eine exponentielle Untergrenze für `rho_T^{(2)}` erzeugt damit nur eine gegen null gehende Untergrenze für `q_{r,T}`. Das reicht logisch weder für `q_{r,T}\not\to0` noch gegen `q_{r,T}\to0`. Der fixe Sprung aus C6t ist also quantitativ real, aber für die asymptotische Klassifikation allein zu schwach.

Der nächste atomare Schritt wird dadurch sauber isoliert: nicht bloß `rho_T^{(2)}` quantifizieren, sondern entscheiden, ob der erste Kanal **relativ** einen nichtverschwindenden Anteil der Residualnorm trägt oder ob `||r_T||^2` auf anderen Regionen/Moden dominiert.

---

# 0. Verbindliche Notation

Wie in C6s/C6t:

\[
\boxed{
A_T:=I+R_T^*R_T\ge I,
}
\tag{C1zB2C6u.2}
\]

\[
\boxed{
h_T:=H_T^*H_T\mathbf1_T,
}
\tag{C1zB2C6u.3}
\]

\[
\boxed{
\lambda_T
:=
\frac{\langle\mathbf1_T,h_T\rangle}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}
=
\frac{\|H_T\mathbf1_T\|^2}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}
\ge0,
}
\tag{C1zB2C6u.4}
\]

\[
\boxed{
r_T:=h_T-\lambda_TA_T\mathbf1_T.
}
\tag{C1zB2C6u.5}
\]

Der Restquotient ist

\[
\boxed{
q_{r,T}
:=
\frac{\|R_Tr_T\|^2}{\|r_T\|^2}.
}
\tag{C1zB2C6u.6}
\]

Aus C6s folgt die positive Martingalzerlegung

\[
\|R_Tr_T\|^2
=
\sum_{p,a}\mathcal E_{p,a,T}(r_T),
\qquad
\mathcal E_{p,a,T}(r_T)\ge0.
\tag{C1zB2C6u.7}
\]

Insbesondere

\[
\boxed{
\|R_Tr_T\|^2
\ge
\mathcal E_{2,0,T}(r_T).
}
\tag{C1zB2C6u.8}
\]

C6t identifiziert den ersten 2-adischen Kanal exakt als

\[
\boxed{
\mathcal E_{2,0,T}(r_T)
=
\int_{\Omega_{2,0,T}}
|H_{2,T}r_T(u)|^2\,du,
}
\tag{C1zB2C6u.9}
\]

mit

\[
\Omega_{2,0,T}
=
\left[-T+\frac12\log2,
T-\frac12\log2\right].
\tag{C1zB2C6u.10}
\]

Zur Erinnerung lautet die korrekte Normalisierung aus C6t

\[
\boxed{
\Phi_{p,0,T}[f]
=
\frac1{\sqrt{\log p}}H_{p,T}f,
}
\tag{C1zB2C6u.11}
\]

nicht `1/(\log p)`.

---

# 1. Kanonischer Isolationsradius des ersten 2-adischen Kanals

Setze

\[
F_T:=H_{2,T}r_T
\qquad\text{auf }\Omega_{2,0,T}.
\tag{C1zB2C6u.12}
\]

Bei festem `T` ist `F_T` eine endliche Linearkombination verschobener stückweiser Funktionen und daher selbst stückweise konstant mit endlich vielen Breakpoints.

C6t liefert für alle hinreichend großen `T` einen Punkt

\[
\boxed{
u_T:=T-\frac12\log q_T,
\qquad q_T\in\{3,5,7\},}
\tag{C1zB2C6u.13}
\]

mit

\[
\boxed{
|J_T^{(2)}|
:=
\left|\operatorname{Jump}_{u_T}F_T\right|
\ge j_0>0.
}
\tag{C1zB2C6u.14}
\]

Definiere den kanonischen Kanal-Isolationsradius

\[
\boxed{
\rho_T^{(2)}
:=
\frac12
\operatorname{dist}
\left(
 u_T,
\bigl(\mathcal B(F_T)\cup\partial\Omega_{2,0,T}\bigr)
\setminus\{u_T\}
\right).
}
\tag{C1zB2C6u.15}
\]

Da `u_T` im Inneren von `Omega_{2,0,T}` liegt und `F_T` bei festem `T` nur endlich viele Breakpoints besitzt,

\[
\boxed{
\rho_T^{(2)}>0
}
\tag{C1zB2C6u.16}
\]

für alle hinreichend großen `T`.

Auf den beiden Intervallen

\[
I_T^-=(u_T-\rho_T^{(2)},u_T),
\qquad
I_T^+=(u_T,u_T+\rho_T^{(2)})
\tag{C1zB2C6u.17}
\]

ist `F_T` jeweils konstant.

Bezeichne diese Konstanten mit

\[
F_T^-,\qquad F_T^+.
\]

Dann

\[
F_T^+-F_T^-=J_T^{(2)}.
\tag{C1zB2C6u.18}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,canonical\text{-}first\text{-}channel\text{-}isolation\text{-}radius}.
}
\]

---

# 2. Vom festen Sprung zur absoluten Kanalenergie

Aus

\[
|F_T^+-F_T^-|
\ge j_0
\]

folgt elementar

\[
\boxed{
\max\{|F_T^-|,|F_T^+|\}
\ge \frac{j_0}{2}.
}
\tag{C1zB2C6u.19}
\]

Mindestens eines der beiden Intervalle `I_T^-`, `I_T^+` trägt daher auf voller Länge `rho_T^{(2)}` einen Betrag von mindestens `j_0/2`.

Somit

\[
\begin{aligned}
\mathcal E_{2,0,T}(r_T)
&=
\int_{\Omega_{2,0,T}}|F_T(u)|^2du\\
&\ge
\frac{j_0^2}{4}\rho_T^{(2)}.
\end{aligned}
\]

Also exakt:

\[
\boxed{
\mathcal E_{2,0,T}(r_T)
\ge
\frac{j_0^2}{4}\rho_T^{(2)}.
}
\tag{C1zB2C6u.20}
\]

Wegen (C1zB2C6u.8) folgt zugleich

\[
\boxed{
\|R_Tr_T\|^2
\ge
\frac{j_0^2}{4}\rho_T^{(2)}.
}
\tag{C1zB2C6u.21}
\]

Dies ist die gesuchte quantitative Version des qualitativen C6t-Befunds.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,jump\text{-}to\text{-}channel\text{-}energy\text{-}bound}.
}
\]

---

# 3. Firewall: C6i liefert nicht automatisch denselben Radius

C6i bewies für den dortigen Cross-Prime-Punkt `x_T` einen `A_T1_T`-freien Radius

\[
\rho_T^A\ge c_Ae^{-4T}.
\]

C6u benötigt dagegen den Abstand zu **allen Breakpoints der bereits gefilterten Funktion**

\[
F_T=H_{2,T}r_T.
\]

Nach C6ts Sprungtransportformel entstehen diese Breakpoints aus den Breakpoints von `r_T` durch alle aktiven Verschiebungen

\[
\pm\frac{k}{2}\log2.
\]

Daher gilt ohne zusätzliche Zählung nicht

\[
\rho_T^{(2)}\ge c e^{-4T}.
\]

Insbesondere muss ein C6i-artiger arithmetischer Distanzsatz nun für die **transportierte Breakpointfamilie** bewiesen werden.

Die Drei-Prim-Auswahl aus C6t schließt exakte Restkollisionen auf der relevanten Lattice aus. Sie ist aber zunächst eine qualitative Kollisionsaussage und noch keine quantitative Mindestdistanz zu sämtlichen benachbarten transportierten Breakpoints.

Deshalb bleibt

\[
\boxed{
?[O]_{\rm quantitative\text{-}two\text{-}adic\text{-}channel\text{-}isolation\text{-}radius}.
}
\tag{C1zB2C6u.22}
\]

Dies ist bewusst strenger als eine unbewiesene Übernahme der C6i-Skala `e^{-4T}`.

---

# 4. Eine λ-freie globale Huboperator-Schranke

Für den nächsten Schritt benötigen wir eine obere Schranke für `||r_T||`.

Der Huboperator lautet

\[
H_T
=
\sum_{n=p^k\le e^{2T}}
 a_nK_{\log n},
\qquad
 a_n=\sqrt{\log p}\,p^{-3k/4}.
\tag{C1zB2C6u.23}
\]

Für jede komprimierte zentrierte Differenz gilt

\[
\boxed{
\|K_s\|\le2.
}
\tag{C1zB2C6u.24}
\]

Ferner

\[
a_n
\le
\sqrt{\log n}\,n^{-3/4}.
\tag{C1zB2C6u.25}
\]

Da die Menge der Prime Powers eine Teilmenge der ganzen Zahlen `2<=n<=e^{2T}` ist,

\[
\sum_{n=p^k\le e^{2T}}a_n
\le
\sum_{2\le m\le e^{2T}}
\sqrt{\log m}\,m^{-3/4}.
\tag{C1zB2C6u.26}
\]

Elementarer Integralvergleich liefert

\[
\sum_{m\le X}
\sqrt{\log m}\,m^{-3/4}
\le C X^{1/4}\sqrt{\log X}
\qquad(X\ge3).
\tag{C1zB2C6u.27}
\]

Mit `X=e^{2T}` folgt

\[
\boxed{
\sum_{n=p^k\le e^{2T}}a_n
\le C\sqrt T\,e^{T/2}.
}
\tag{C1zB2C6u.28}
\]

und damit

\[
\boxed{
\|H_T\|
\le C_H\sqrt T\,e^{T/2}.
}
\tag{C1zB2C6u.29}
\]

Dies benutzt weder PNT noch eine `lambda_T`-Asymptotik.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,lambda\text{-}free\text{-}hub\text{-}operator\text{-}bound}.
}
\]

---

# 5. Konsequenz für h_T

Da

\[
h_T=H_T^*H_T\mathbf1_T
\]

und

\[
\|\mathbf1_T\|^2=2T,
\]

folgt aus (C1zB2C6u.29)

\[
\begin{aligned}
\|h_T\|
&\le
\|H_T\|^2\|\mathbf1_T\|\\
&\le
C T e^T\sqrt{2T}.
\end{aligned}
\]

Somit

\[
\boxed{
\|h_T\|
\le C_hT^{3/2}e^T,
}
\tag{C1zB2C6u.30}
\]

und

\[
\boxed{
\|h_T\|^2
\le C_h'T^3e^{2T}.
}
\tag{C1zB2C6u.31}
\]

Dies ist eine grobe Operatornorm-Schranke, keine asymptotische Gleichheit.

Insbesondere darf sie nicht als

\[
\|h_T\|^2\asymp T^3e^{2T}
\]

gelesen werden.

---

# 6. λ-freie Obergrenze für die Residualnorm

Setze wie C6l

\[
\boxed{
y_T:=A_T^{-1}r_T.}
\tag{C1zB2C6u.32}
\]

Dann

\[
r_T=A_Ty_T.
\tag{C1zB2C6u.33}
\]

Außerdem

\[
\boxed{
\Delta_T^{(1)}
=
\langle y_T,A_Ty_T\rangle
=
\langle r_T,A_T^{-1}r_T\rangle.
}
\tag{C1zB2C6u.34}
\]

Da `A_T` positiv ist,

\[
A_T^2
\le
\|A_T\|A_T.
\]

Daher

\[
\begin{aligned}
\|r_T\|^2
&=
\|A_Ty_T\|^2\\
&=
\langle y_T,A_T^2y_T\rangle\\
&\le
\|A_T\|\langle y_T,A_Ty_T\rangle\\
&=
\|A_T\|\Delta_T^{(1)}.
\end{aligned}
\]

Also

\[
\boxed{
\|r_T\|^2
\le
\|A_T\|\Delta_T^{(1)}.
}
\tag{C1zB2C6u.35}
\]

Nun gilt aus der Krylov-Definition

\[
\Delta_T^{(1)}
=
\langle h_T,A_T^{-1}h_T\rangle
-
\frac{|\langle\mathbf1_T,h_T\rangle|^2}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}
\le
\langle h_T,A_T^{-1}h_T\rangle.
\tag{C1zB2C6u.36}
\]

Wegen `A_T>=I` ist `A_T^{-1}<=I`, also

\[
\boxed{
\Delta_T^{(1)}
\le
\|h_T\|^2.
}
\tag{C1zB2C6u.37}
\]

C6f beweist

\[
\boxed{
\|R_T\|^2
\le C_RT e^T.
}
\tag{C1zB2C6u.38}
\]

Daher

\[
\|A_T\|
=
\|I+R_T^*R_T\|
\le
1+C_RT e^T
\le C_A T e^T
\tag{C1zB2C6u.39}
\]

für großes `T`.

Setzt man (C1zB2C6u.31), (C1zB2C6u.37) und (C1zB2C6u.39) in (C1zB2C6u.35) ein, erhält man

\[
\boxed{
\|r_T\|^2
\le
C_rT^4e^{3T}.
}
\tag{C1zB2C6u.40}
\]

Dies ist die erste hier benötigte vollständig `lambda_T`-freie globale Obergrenze für die Residualnorm.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,lambda\text{-}free\text{-}residual\text{-}norm\text{-}upper\text{-}bound}.
}
\]

---

# 7. Relative Restladung: exakte Reduktion

Aus (C1zB2C6u.21) und (C1zB2C6u.40) folgt

\[
\begin{aligned}
q_{r,T}
&=
\frac{\|R_Tr_T\|^2}{\|r_T\|^2}\\
&\ge
\frac{(j_0^2/4)\rho_T^{(2)}}{C_rT^4e^{3T}}.
\end{aligned}
\]

Also

\[
\boxed{
q_{r,T}
\ge
c_q
\frac{\rho_T^{(2)}}{T^4e^{3T}}.
}
\tag{C1zB2C6u.41}
\]

Dies ist eine echte quantitative relative Untergrenze.

Sie hängt nur noch von einer geometrischen Größe ab:

\[
\boxed{
\rho_T^{(2)}.
}
\tag{C1zB2C6u.42}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,relative\text{-}rest\text{-}loading\text{-}reduction}.
}
\]

---

# 8. Warum diese Untergrenze q_r noch nicht klassifiziert

Angenommen, ein späterer Knoten würde beispielsweise

\[
\rho_T^{(2)}
\ge
c e^{-\alpha T}T^{-B}
\]

für feste `alpha,B>=0` beweisen.

Dann liefert C6u lediglich

\[
\boxed{
q_{r,T}
\ge
c'
T^{-(B+4)}e^{-(\alpha+3)T}.
}
\tag{C1zB2C6u.43}
\]

Diese Untergrenze tendiert gegen null.

Eine gegen null gehende Untergrenze ist kompatibel mit allen folgenden Möglichkeiten:

\[
q_{r,T}\to0,
\]

\[
q_{r,T}\to c>0,
\]

\[
q_{r,T}\to\infty,
\]

oder oszillierendem Verhalten.

Daher gilt ausdrücklich

\[
\boxed{
\mathcal E_{2,0,T}(r_T)>0
\text{ und sogar }
\mathcal E_{2,0,T}(r_T)\gtrsim e^{-\alpha T}
\not\Rightarrow
q_{r,T}\not\to0.
}
\tag{C1zB2C6u.44}
\]

Ebenso folgt daraus nicht `q_{r,T}\to0`; hierfür bräuchte man eine obere Schranke für `||R_Tr_T||^2` relativ zu `||r_T||^2`.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,fixed\text{-}jump\not\Rightarrow q_r\not\to0}
+
\checkmark[M]_{\rm neg,vanishing\text{-}lower\text{-}bound\not\Rightarrow asymptotic\text{-}classification}.
}
\]

---

# 9. Reconciliation der heuristischen Skalen aus der Vorüberlegung

Die Vorüberlegung verwendete unter anderem heuristische Größen wie

\[
\lambda_T\asymp Te^T,
\]

und daraus abgeleitete Größenordnungen für `||A_T1_T||`, `||h_T||` und `||r_T||`.

C6i hat bereits ausdrücklich versiegelt:

\[
\boxed{
\lambda_T\asymp Te^T
\text{ ist im bisherigen Strang nicht bewiesen.}
}
\tag{C1zB2C6u.45}
\]

C6u benutzt diese Heuristik daher nicht.

Außerdem sind die Größen

\[
\mu_{T,0}=\langle1_T,A_T1_T\rangle,
\qquad
\mu_{T,1}=\langle1_T,h_T\rangle
\]

Skalarprodukte/Momente und dürfen nicht ohne Zusatzargument mit

\[
\|A_T1_T\|^2,
\qquad
\|h_T\|^2
\]

identifiziert werden.

Insbesondere sind Aussagen der Form

\[
\|A_T1_T\|^2\asymp\mu_{T,0}
\]

oder

\[
\|h_T\|^2\asymp\mu_{T,1}
\]

nicht aus der bisherigen Kette ableitbar.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,heuristic\text{-}moment\text{-}scales\text{-}unproved}.
}
\]

---

# 10. Was C6u tatsächlich entscheidet

C6u beweist nun gleichzeitig:

### Positiv

1. Der C6t-Hauptsprung besitzt bei festem `T` einen kanonischen positiven Kanal-Isolationsradius `rho_T^{(2)}`.
2. Dieser liefert
   \[
   \mathcal E_{2,0,T}(r_T)
   \ge
   \frac{j_0^2}{4}\rho_T^{(2)}.
   \]
3. Ohne `lambda_T`-Asymptotik gilt
   \[
   \|r_T\|^2\lesssim T^4e^{3T}.
   \]
4. Folglich
   \[
   q_{r,T}
   \gtrsim
   \frac{\rho_T^{(2)}}{T^4e^{3T}}.
   \]

### Negativ / Firewall

1. Die C6i-Skala `e^{-4T}` darf nicht automatisch auf den bereits gefilterten Kanal `H_{2,T}r_T` übertragen werden.
2. Ein fester Sprung oder eine exponentiell kleine absolute Kanalenergie klassifiziert `q_{r,T}` nicht.
3. Eine gegen null gehende Untergrenze für `q_{r,T}` beweist ausdrücklich **nicht** `q_{r,T}\not\to0`.
4. Die bisher unbewiesene Heuristik `lambda_T\asymp Te^T` wird nicht reaktiviert.

Damit ist der C6t-Befund quantitativ korrekt eingeordnet.

---

# 11. Nächster atomarer Arbeitsauftrag

Der natürliche Folgepunkt ist

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6v]
}
\]

mit dem Titel etwa

**„Transportierte Breakpoint-Separation und relative 2-adische Kanalmasse“**.

C6v sollte zwei Fragen strikt getrennt prüfen:

1. **Geometrie:** Kann die Drei-Prim-Auswahl aus C6t zusammen mit C6i/C6g zu einer expliziten Untergrenze
   \[
   \rho_T^{(2)}\ge \rho_T^{\rm explicit}
   \]
   für die transportierte Breakpointfamilie verstärkt werden?
2. **Relative Masse:** Gibt es eine stärkere, nicht bloß lokale Beziehung zwischen
   \[
   \|H_{2,T}r_T\|^2
   \]
   und
   \[
   \|r_T\|^2,
   \]
   etwa auf einem strukturell ausgezeichneten Teilraum, die einen nichtverschwindenden relativen Anteil erzwingen könnte?

Erst Frage 2 kann den Smallness-Hebel `q_{r,T}` wirklich blockieren. Frage 1 allein verbessert nur die absolute Untergrenze.

---

# 12. Endurteil

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6u]
\quad
\checkmark[K/M]_{\rm part}
}
\]

mit den versiegelten positiven Ergebnissen

\[
\boxed{
\mathcal E_{2,0,T}(r_T)
\ge
\frac{j_0^2}{4}\rho_T^{(2)},
}
\]

\[
\boxed{
\|r_T\|^2
\lesssim
T^4e^{3T},
}
\]

und

\[
\boxed{
q_{r,T}
\gtrsim
\frac{\rho_T^{(2)}}{T^4e^{3T}}.
}
\]

Die noch offene Kernfrage ist nicht mehr bloß, ob der erste 2-adische Kanal positiv ist — das ist C6t zufolge eventual bewiesen — sondern ob er **relativ zur gesamten Residualnorm** asymptotisch relevant bleibt.

P11 bleibt `PASS-A ACTIVE`. Kein SYN, kein Seal, kein `papers/P11`. Alle bisherigen No-Go-Ergebnisse bleiben unverändert in Kraft.
