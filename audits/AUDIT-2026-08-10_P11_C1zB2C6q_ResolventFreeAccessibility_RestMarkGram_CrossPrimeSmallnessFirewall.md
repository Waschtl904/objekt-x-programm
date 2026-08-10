# P11-C1z-B2-C6q — Resolventfreie Zugänglichkeit, Rest-Mark-Gramkern und Cross-Prime-Smallness-Firewall

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6q]`  
**Direkte Voraussetzungen:** C1z-B, C1z-B2-C3, C1z-B2-C6h, C1z-B2-C6i, C1z-B2-C6j, C1z-B2-C6m, C1z-B2-C6n, C1z-B2-C6o, C1z-B2-C6p  
**Strukturelle Schnittstellen:** C1z-B2-C4, C1z-B2-C6a, C1z-B2-C6c, C1z-B2-C6d, C1z-B2-C6e, C1z-B2-C6f, C1z-B2-C6g, C1z-B2-C6k, C1z-B2-C6l  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d `orthogonality != jet alignment`, C1z-B2-C6k `current data != Wronskian nonzero`, C1z-B2-C6l `C4 constant-mode mechanism does not transfer`, C1z-B2-C6m `A-orthogonality != bulk cancellation`, C1z-B2-C6n `positivity != alignment`, C1z-B2-C6o `raw support separation route fails`, C1z-B2-C6p `fixed-vector divergence != moving-vector control`.  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6q]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm pos,exact\text{-}rest\text{-}mark\text{-}Gram\text{-}kernel}
+
\checkmark[M]_{\rm pos,resolvent\text{-}free\text{-}three\text{-}parameter\text{-}formulas}
+
\checkmark[M]_{\rm pos,fixed\text{-}T\text{-}finite\text{-}computability}
+
\checkmark[M]_{\rm pos,residual\text{-}L^2\text{-}lower\text{-}bound}
+
\checkmark[M]_{\rm pos,bare\text{-}angle\text{-}old\text{-}window\text{-}formula}
+
\checkmark[M]_{\rm corr,q_r\text{-}most\text{-}accessible\neq q_r\text{-}small}
+
\checkmark[M]_{\rm neg,cross\text{-}prime\text{-}provenance\not\Rightarrow rest\text{-}smallness}
+
\checkmark[M]_{\rm neg,C6h\text{-}special\text{-}1_T\text{-}formula\not\Rightarrow r_T\text{-}rest\text{-}bound}
+
?[O]_{\rm q_r\text{-}asymptotic}
+
?[O]_{\rm bare\text{-}angle\text{-}lower\text{-}bound}
+
?[O]_{\rm q_b\text{-}asymptotic}
+
?[O]_{\rm second\text{-}alignment\text{-}scalar\neq0}
+
?[O]_{\rm quantitative\text{-}s_{min}}
}
\]

C6p reduzierte das Alignmentproblem auf die drei dimensionslosen Größen

\[
\boxed{
\beta_{R,T},\qquad q_{b,T},\qquad q_{r,T},
}
\]

mit

\[
\beta_{R,T}
:=
\frac{|\langle b_{R,T},r_T\rangle|}
{\|b_{R,T}\|\,\|r_T\|},
\]

\[
q_{b,T}
:=
\frac{\|R_Tb_{R,T}\|^2}{\|b_{R,T}\|^2},
\qquad
q_{r,T}
:=
\frac{\|R_Tr_T\|^2}{\|r_T\|^2}.
\]

C6q führt das angekündigte Zugänglichkeitsaudit durch.

Der Hauptbefund ist zweigeteilt:

1. **Positiv:** Alle drei Größen sind bei festem `T` vollständig **resolventenfrei** und als endliche P11-interne Summen bzw. Integrale explizit zugänglich. Insbesondere liefert die source-gekoppelte Restmarke einen geschlossenen Prime-by-Prime-Gramkernel für `||R_T f||^2` bei beliebigem Sourcevektor `f`.
2. **Negativ:** Aus der Cross-Prime-Herkunft eines Sprungs von `r_T` folgt keinerlei kleine Restladung. `R_T` sieht die skalare Sourcefunktion durch Translationen; es bewahrt nicht die Provenienz „dieser Sprung kam aus zwei verschiedenen Hubprimen“. Die C6h-Prime-pure-Struktur des **Operators** ist daher keine Smallness-Aussage für einen cross-prime erzeugten **Eingabevektor**.

Der Residualvektor `r_T` bleibt dennoch der beste erste asymptotische Kandidat, aber aus einem anderen Grund: er ist bei festem `T` eine explizite stückweise Funktion, sein Nenner ist bereits quantitativ von null getrennt, und `q_{r,T}` kann direkt mit dem exakten Rest-Gramkernel untersucht werden.

---

# 0. Verbindliche Notation aus C6m–C6p

Fixiere `R>0` und großes `T`.

Aus C6m:

\[
\boxed{
 g_{R,T}
 =
 f_{R,1}
 -
 c_{R,T}f_{R,0},
\qquad
c_{R,T}:=\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}.
}
\tag{C1zB2C6q.1}
\]

Dann

\[
\boxed{
\langle J_{R,T}g_{R,T},H_T\mathbf1_T\rangle=0.
}
\tag{C1zB2C6q.2}
\]

Setze

\[
\boxed{
 b_{R,T}:=H_T^*J_{R,T}g_{R,T}.
}
\tag{C1zB2C6q.3}
\]

Ferner

\[
\boxed{
 h_T:=H_T^*H_T\mathbf1_T,
}
\tag{C1zB2C6q.4}
\]

\[
\boxed{
 A_T:=I+R_T^*R_T,
}
\tag{C1zB2C6q.5}
\]

\[
\boxed{
\lambda_T
:=
\frac{\mu_{T,1}}{\mu_{T,0}},
\qquad
r_T
:=
h_T-\lambda_TA_T\mathbf1_T.
}
\tag{C1zB2C6q.6}
\]

C6p definierte

\[
\boxed{
\beta_{R,T}
=
\frac{|\langle b_{R,T},r_T\rangle|}
{\|b_{R,T}\|\,\|r_T\|}
\in[0,1],
}
\tag{C1zB2C6q.7}
\]

und

\[
\boxed{
q_{b,T}
=
\frac{\|R_Tb_{R,T}\|^2}{\|b_{R,T}\|^2},
\qquad
q_{r,T}
=
\frac{\|R_Tr_T\|^2}{\|r_T\|^2}.
}
\tag{C1zB2C6q.8}
\]

Für die Screening-Fraktionen gilt aus C6p

\[
s_{b,T}
\le
\frac{q_{b,T}}{1+q_{b,T}},
\qquad
s_{r,T}
\le
\frac{q_{r,T}}{1+q_{r,T}},
\tag{C1zB2C6q.9}
\]

und daher das hinreichende Alignment-Kriterium

\[
\boxed{
\beta_{R,T}
>
\sqrt{
\frac{q_{b,T}q_{r,T}}
{(1+q_{b,T})(1+q_{r,T})}
}
\Longrightarrow
 a_{R,T}^{(2)}\ne0.
}
\tag{C1zB2C6q.10}
\]

C6q fragt nur, wie zugänglich diese drei nackten Größen mit der bereits vorhandenen P11-Struktur tatsächlich sind.

---

# 1. Exakte Restmarke

Für eine Primzahl `p`, Potenzindex `k>=1` und Sourcepunkt `u` ist aus C1z-B/C6h

\[
\boxed{
q_{p,k,T}(u)
=
\sqrt{p-1}
\sum_{a=0}^{\min(k-1,J_{p,T}(u)-1)}
p^{(a-k)/2}\psi_{p,a},
}
\tag{C1zB2C6q.11}
\]

mit

\[
\boxed{
J_{p,T}(u)
=
\max\left\{0,
\left\lfloor
\frac{2(T-|u|)_+}{\log p}
\right\rfloor
\right\}.
}
\tag{C1zB2C6q.12}
\]

Die `psi_{p,a}` sind orthonormal.

Der Restoperator lautet

\[
\boxed{
R_Tf
=
\bigoplus_pR_{p,T}f,
}
\tag{C1zB2C6q.13}
\]

mit

\[
\boxed{
R_{p,T}f(u)
=
\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}
K_{k\log p}f(u)
\,q_{p,k,T}(u).
}
\tag{C1zB2C6q.14}
\]

Bei festem `T` ist die aktive Summe endlich.

---

# 2. Exakter Gramkernel der source-gekoppelten Restmarken

Fixiere `p,u,k,l` und setze

\[
\boxed{
d_{p,T}(u;k,l)
:=
\min\{k,l,J_{p,T}(u)\}.
}
\tag{C1zB2C6q.15}
\]

Falls `d_{p,T}(u;k,l)=0`, ist mindestens einer der beiden Markvektoren auf diesem Sourcepunkt null und damit

\[
\langle q_{p,k,T}(u),q_{p,l,T}(u)\rangle=0.
\]

Sei nun `d:=d_{p,T}(u;k,l)>=1`. Dann teilen die beiden Markvektoren genau die Martingalstufen

\[
a=0,1,\ldots,d-1.
\]

Aus (C1zB2C6q.11) und der Orthonormalität folgt

\[
\begin{aligned}
\langle q_{p,k,T}(u),q_{p,l,T}(u)\rangle
&=
(p-1)
\sum_{a=0}^{d-1}
p^{(a-k)/2}p^{(a-l)/2}\\
&=
(p-1)p^{-(k+l)/2}
\sum_{a=0}^{d-1}p^a\\
&=
p^{-(k+l)/2}(p^d-1).
\end{aligned}
\]

Somit gilt **exakt**

\[
\boxed{
\langle q_{p,k,T}(u),q_{p,l,T}(u)\rangle
=
p^{-(k+l)/2}
\left(
p^{d_{p,T}(u;k,l)}-1
\right).
}
\tag{C1zB2C6q.16}
\]

Die Formel enthält den Diagonalfall `k=l` als Spezialfall und reproduziert insbesondere die C6j-Normformel der einzelnen Restmarke.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,exact\text{-}rest\text{-}mark\text{-}Gram\text{-}kernel}.
}
\]

---

# 3. Exakte resolventenfreie Formel für `||R_T f||^2`

Da die Prime-Targeträume für verschiedene `p` orthogonal sind,

\[
\|R_Tf\|^2
=
\sum_p\|R_{p,T}f\|^2.
\tag{C1zB2C6q.17}
\]

Setze (C1zB2C6q.14) ein und verwende (C1zB2C6q.16). Dann

\[
\boxed{
\begin{aligned}
\|R_Tf\|^2
&=
\sum_p
\int_{-T}^{T}
\sum_{k,l\ge1}
(\log p)
p^{-3(k+l)/4}
\left(
p^{d_{p,T}(u;k,l)}-1
\right)\\
&\qquad\qquad\qquad\times
(K_{k\log p}f)(u)
\overline{(K_{l\log p}f)(u)}
\,du.
\end{aligned}
}
\tag{C1zB2C6q.18}
\]

Dies ist eine positive quadratische Form, obwohl die einzelnen `k,l`-Summanden wegen der Translationsdifferenzen komplexe oder vorzeichenwechselnde Kreuzterme besitzen können.

Die Formel ist entscheidend aus zwei Gründen:

1. Sie enthält **keine Resolvente** und kein `A_T^{-1}`.
2. Sie gilt für beliebige Sourcevektoren `f`, nicht nur für `1_T` oder den C6j-Haarseparator.

Damit sind sofort

\[
\boxed{
q_{r,T}
=
\frac{\mathfrak R_T[r_T]}{\|r_T\|^2},
\qquad
q_{b,T}
=
\frac{\mathfrak R_T[b_{R,T}]}{\|b_{R,T}\|^2},
}
\tag{C1zB2C6q.19}
\]

mit der expliziten quadratischen Form `mathfrak R_T` aus (C1zB2C6q.18).

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,resolvent\text{-}free\text{-}rest\text{-}loading}.
}
\]

---

# 4. Auch `lambda_T`, `r_T`, `g_{R,T}` und `b_{R,T}` sind resolventenfrei

Der Eindruck, `r_T` trage wegen seiner Herkunft aus dem Krylov-/Feshbach-Strang noch eine versteckte Resolvente, ist falsch.

Denn

\[
\mu_{T,0}
=
\langle\mathbf1_T,A_T\mathbf1_T\rangle
=
\|\mathbf1_T\|^2+\|R_T\mathbf1_T\|^2
=
2T+\|R_T\mathbf1_T\|^2,
\tag{C1zB2C6q.20}
\]

und

\[
\mu_{T,1}
=
\langle\mathbf1_T,H_T^*H_T\mathbf1_T\rangle
=
\|H_T\mathbf1_T\|^2.
\tag{C1zB2C6q.21}
\]

Also

\[
\boxed{
\lambda_T
=
\frac{\|H_T\mathbf1_T\|^2}
{2T+\|R_T\mathbf1_T\|^2}.
}
\tag{C1zB2C6q.22}
\]

Weiter

\[
\boxed{
A_T\mathbf1_T
=
\mathbf1_T+R_T^*R_T\mathbf1_T,
}
\tag{C1zB2C6q.23}
\]

und daher

\[
\boxed{
r_T
=
H_T^*H_T\mathbf1_T
-
\lambda_T
\left(
\mathbf1_T+R_T^*R_T\mathbf1_T
\right).
}
\tag{C1zB2C6q.24}
\]

Alle Größen rechts sind bereits durch Hub, Rest und Konstantenmode definiert.

Ebenso ist

\[
c_{R,T}
=
\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)},
\qquad
\ell_{R,m}(T)
=
\langle J_{R,T}f_{R,m},H_T\mathbf1_T\rangle,
\tag{C1zB2C6q.25}
\]

also

\[
\boxed{
g_{R,T}
=
f_{R,1}
-
\frac{\langle Jf_{R,1},H_T\mathbf1_T\rangle}
{\langle Jf_{R,0},H_T\mathbf1_T\rangle}
f_{R,0}.
}
\tag{C1zB2C6q.26}
\]

Schließlich

\[
\boxed{
b_{R,T}=H_T^*J_{R,T}g_{R,T}.
}
\tag{C1zB2C6q.27}
\]

Somit sind `r_T`, `g_{R,T}` und `b_{R,T}` bei festem `T` ebenfalls explizite endliche Operatorausdrücke ohne Inversion.

---

# 5. Der bare Winkel ist ein alter-Sourcefenster-Skalar

Der Zähler von `beta_{R,T}` ist

\[
\langle b_{R,T},r_T\rangle.
\]

Mit (C1zB2C6q.3) folgt durch Adjungieren exakt

\[
\boxed{
\langle b_{R,T},r_T\rangle
=
\langle J_{R,T}g_{R,T},H_Tr_T\rangle.
}
\tag{C1zB2C6q.28}
\]

Damit ist die scheinbar globale Sourceraum-Winkelfrage wieder eine skalare Observation auf dem festen alten Sourcefenster.

Setze (C1zB2C6q.24) ein:

\[
H_Tr_T
=
H_Th_T
-
\lambda_TH_T\mathbf1_T
-
\lambda_TH_TR_T^*R_T\mathbf1_T.
\]

Wegen der exakten First-Observation-Nullheit (C1zB2C6q.2) verschwindet der mittlere Term nach Paarung mit `Jg_{R,T}`. Daher

\[
\boxed{
\langle b_{R,T},r_T\rangle
=
\langle J_{R,T}g_{R,T},H_Th_T\rangle
-
\lambda_T
\langle J_{R,T}g_{R,T},H_TR_T^*R_T\mathbf1_T\rangle.
}
\tag{C1zB2C6q.29}
\]

Der bare Korrelationszähler ist also exakt

\[
\boxed{
\text{Drei-Hub-Korrelation}
-
\text{Hub--Rest}^2\text{-Korrelation}.
}
\tag{C1zB2C6q.30}
\]

Auch hier tritt keine Resolvente auf.

Für die Norm von `b_{R,T}` gilt ebenfalls

\[
\boxed{
\|b_{R,T}\|^2
=
\|H_T^*J_{R,T}g_{R,T}\|^2
=
\langle J_{R,T}g_{R,T},H_TH_T^*J_{R,T}g_{R,T}\rangle.
}
\tag{C1zB2C6q.31}
\]

Damit ist

\[
\boxed{
\beta_{R,T}
=
\frac{
|\langle Jg_{R,T},H_Tr_T\rangle|
}{
\sqrt{\langle Jg_{R,T},H_TH_T^*Jg_{R,T}\rangle}
\,\|r_T\|
}.
}
\tag{C1zB2C6q.32}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,bare\text{-}angle\text{-}old\text{-}window\text{-}formula}.
}
\]

---

# 6. Fixed-`T`-Computability

Bei festem `T` sind alle aktiven Hub- und Rest-Prime-Power-Label endlich:

\[
p^k\le e^{O(T)}.
\]

Die Funktionen

\[
H_T\mathbf1_T,
\qquad
H_T^*H_T\mathbf1_T,
\qquad
R_T^*R_T\mathbf1_T
\]

sind durch endliche Translations-/Mark-Summen gegeben. Insbesondere sind die aus `1_T` erzeugten Profile stückweise durch die endliche Breakpoint-Geometrie aus C6e/C6h beschrieben.

Daher sind bei festem `T`

\[
\lambda_T,
\quad
r_T,
\quad
c_{R,T},
\quad
g_{R,T},
\quad
b_{R,T},
\]

und schließlich

\[
\boxed{
\beta_{R,T},\qquad q_{r,T},\qquad q_{b,T}
}
\]

prinzipiell durch endliche Summen und eindimensionale Integrale bestimmbar.

Dies ist eine **mathematische Zugänglichkeitsaussage**, keine Behauptung effizienter numerischer Komplexität. Die Zahl aktiver Labels wächst stark mit `T`; naive Enumeration ist asymptotisch keine Beweismethode.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,fixed\text{-}T\text{-}finite\text{-}computability}.
}
\]

---

# 7. `r_T` besitzt bereits eine bare `L^2`-Untergrenze

C6i konstruiert für jedes hinreichend große `T` einen der beiden Orte

\[
x_T=x_{q_T}(T),
\qquad
q_T\in\{3,5\},
\]

und einen Haarseparator

\[
\boxed{
v_T
=
\mathbf1_{(x_T-\rho_T,x_T)}
-
\mathbf1_{(x_T,x_T+\rho_T)},
\qquad
\rho_T\asymp e^{-4T},
}
\tag{C1zB2C6q.33}
\]

mit

\[
\boxed{
\langle v_T,A_T\mathbf1_T\rangle=0.
}
\tag{C1zB2C6q.34}
\]

C6g/C6i geben auf dieser Skala

\[
\boxed{
|\langle v_T,h_T\rangle|
\ge
c_h e^{-4T}
}
\tag{C1zB2C6q.35}
\]

für großes `T`.

Da

\[
r_T=h_T-\lambda_TA_T\mathbf1_T,
\]

folgt exakt

\[
\boxed{
\langle v_T,r_T\rangle
=
\langle v_T,h_T\rangle.
}
\tag{C1zB2C6q.36}
\]

Weiter

\[
\|v_T\|^2=2\rho_T\asymp e^{-4T}.
\tag{C1zB2C6q.37}
\]

Cauchy--Schwarz liefert damit

\[
\|r_T\|^2
\ge
\frac{|\langle v_T,r_T\rangle|^2}{\|v_T\|^2}
\gtrsim
\frac{e^{-8T}}{e^{-4T}}.
\]

Also

\[
\boxed{
\|r_T\|^2
\ge
c_r e^{-4T}
}
\tag{C1zB2C6q.38}
\]

für ein `c_r>0` und großes `T`.

Dies ist stärker als die bloße Folgerung

\[
\|r_T\|^2
\ge
\langle r_T,A_T^{-1}r_T\rangle
=
\Delta_T^{(1)}
\gtrsim e^{-5T}.
\]

Wichtig: (C1zB2C6q.38) ist nur eine **Nenner-Untergrenze** für `q_{r,T}`. Sie sagt nichts darüber, wie groß `||R_T r_T||` ist.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,residual\text{-}L^2\text{-}lower\text{-}bound}.
}
\]

---

# 8. Korrektur: Cross-Prime-Herkunft macht `R_T r_T` nicht klein

Auf dem in C6i gewählten kleinen Fenster ist `A_T1_T` konstant und `h_T` trägt eine robuste Cross-Prime-Hubkante. Deshalb besitzt `r_T` dort dieselbe nichtverschwindende Hubkante.

Dies ist eine wichtige lokale Strukturinformation.

Aber daraus folgt **nicht**

\[
q_{r,T}\ll1.
\]

Der Grund ist typologisch klar. Der Restoperator wirkt auf eine skalare Sourcefunktion `f` durch

\[
(K_{k\log p}f)(u)
=
(P_TD_{k\log p}E_Tf)(u)
\]

und koppelt das Ergebnis anschließend an den Prime-Targetmarkvektor `q_{p,k,T}(u)`.

Sobald `r_T` als Sourcefunktion vorliegt, trägt ein Wert oder Sprung von `r_T` **kein internes Etikett mehr**, ob er ursprünglich aus

- einem same-prime Hubpaar,
- einem cross-prime Hubpaar,
- oder einer Linearkombination vieler Hubpaare

entstanden ist.

Der Restoperator sieht nur die tatsächlichen translatierten Werte

\[
r_T(u+s)-r_T(u-s).
\]

Die äußere Prime-Sektorierung

\[
R_T=igoplus_pR_{p,T}
\]

klassifiziert den **Ausgangssektor des Restoperators**, nicht die arithmetische Provenienz eines Source-Sprungs.

Daher gilt mit den vorhandenen Daten ausdrücklich nicht

\[
\boxed{
\text{cross-prime Hubkante in }r_T
\Longrightarrow
\|R_Tr_T\|\text{ klein}.
}
\tag{C1zB2C6q.39}
\]

Dies ist dieselbe Grundwarnung wie C6o, nun auf die konkrete `q_r`-Smallness-Hoffnung angewandt.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,cross\text{-}prime\text{-}provenance\not\Rightarrow rest\text{-}smallness}.
}
\]

---

# 9. Warum C6h nicht direkt auf `r_T` übertragbar ist

C6h konnte die Restseite für `1_T` deshalb so stark kontrollieren, weil auf einer p-Tiefenlage `I^+_{p,j,T}` exakt bekannt ist,

\[
K_{k\log p}\mathbf1_T(u)
\in\{0,-1,+1\},
\]

und die aktive Bedingung lediglich von `j,k` abhängt.

Dadurch entstand die geschlossene Tiefenformel

\[
R_{p,T}\mathbf1_T(u)
=
-\sqrt{(p-1)\log p}
\left(\sum_{k\ge j+1}p^{-3k/4}\right)
\sum_{a=0}^{j-1}p^{a/2}\psi_{p,a}.
\]

Für `r_T` ist

\[
K_{k\log p}r_T(u)
=
r_T(u+k\log p/2)-r_T(u-k\log p/2)
\]

kein konstanter `0/+-1`-Wert und keine nur von der p-Tiefe abhängige Größe.

Die exakte allgemeine Ersatzformel ist daher nicht C6hs geometrischer Tail, sondern der Gramkernel (C1zB2C6q.18).

Folglich ist der direkte Schluss

\[
\text{C6h Rest-Crowding für }1_T
\Longrightarrow
q_{r,T}\lesssim e^{-T}
\]

nicht bewiesen.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,C6h\text{-}special\text{-}1_T\text{-}formula\not\Rightarrow r_T\text{-}rest\text{-}bound}.
}
\]

---

# 10. Zugänglichkeitsranking der drei Parameter

Die drei C6p-Größen sind alle resolventenfrei, aber nicht gleich schwer asymptotisch zu analysieren.

## 10.1 `q_{r,T}` — erster Kandidat

`r_T` wird ausschließlich aus der Konstantenmode durch

\[
H_T^*H_T,
\qquad
R_T^*R_T,
\qquad
\lambda_T
\]

erzeugt.

Bei festem `T` besitzt dieser Vektor die explizite Hub-/Rest-Breakpoint-Struktur aus C6e/C6h. Außerdem ist sein Nenner durch (C1zB2C6q.38) bereits quantitativ von null getrennt.

Mit (C1zB2C6q.18) ist

\[
\|R_Tr_T\|^2
\]

eine vollständig explizite Prime-by-Prime-Quadratform.

Daher ist `q_{r,T}` der **strukturell beste erste asymptotische Kandidat**.

Aber:

\[
\boxed{
\text{„am zugänglichsten“}
\ne
\text{„bereits klein“.}
}
\tag{C1zB2C6q.40}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,q_r\text{-}most\text{-}accessible\neq q_r\text{-}small}.
}
\]

## 10.2 `beta_{R,T}` — ein einzelner alter-Window-Skalar

Der Korrelationszähler ist nach (C1zB2C6q.29) ein einzelnes Skalarprodukt auf dem festen alten Sourcefenster:

\[
\langle Jg_{R,T},H_Th_T\rangle
-
\lambda_T\langle Jg_{R,T},H_TR_T^*R_T1_T\rangle.
\]

Dies ist algebraisch eine Drei-Hub- gegen eine Hub--Rest²-Korrelation. Es ist komplizierter als `q_r`, aber strukturierter als eine abstrakte Winkelanalyse im gesamten Terminalraum.

Für eine untere Schranke muss allerdings eine mögliche Kompensation dieser beiden Skalare ausgeschlossen werden; genau dafür gibt es noch keinen Satz.

## 10.3 `q_{b,T}` — moving Hubresponse durch den vollständigen Restkernel

Hier

\[
b_{R,T}=H_T^*Jg_{R,T}
\]

und

\[
\|R_Tb_{R,T}\|^2
=
\mathfrak R_T[H_T^*Jg_{R,T}].
\]

Die allgemeine Formel (C1zB2C6q.18) ist exakt, aber die Eingabe selbst ist bereits eine terminale Hubsumme des moving vectors `g_{R,T}`. Dadurch werden Hub-Label- und Rest-Label-Geometrie direkt verschachtelt.

C6ps Moving-Vector-Firewall bleibt daher hier besonders relevant.

### Arbeitsranking

Für den nächsten analytischen Schritt ist daher die Reihenfolge

\[
\boxed{
q_{r,T}
\quad\longrightarrow\quad
\beta_{R,T}
\quad\longrightarrow\quad
q_{b,T}
}
\tag{C1zB2C6q.41}
\]

die derzeit plausibelste **Zugänglichkeitsreihenfolge**.

Dies ist eine Arbeitsentscheidung, kein mathematischer Satz über die letztendliche asymptotische Schwierigkeit.

---

# 11. Eine nützliche targetseitige Formel für `R_T r_T`

Aus

\[
r_T
=
h_T-\lambda_TA_T\mathbf1_T
\]

und

\[
R_TA_T
=
R_T(I+R_T^*R_T)
=
(I+R_TR_T^*)R_T
\]

folgt exakt

\[
\boxed{
R_Tr_T
=
R_Th_T
-
\lambda_T
(I+R_TR_T^*)R_T\mathbf1_T.
}
\tag{C1zB2C6q.42}
\]

Damit

\[
\boxed{
q_{r,T}
=
\frac{
\|R_Th_T-\lambda_T(I+R_TR_T^*)R_T\mathbf1_T\|^2
}{
\|h_T-\lambda_TA_T\mathbf1_T\|^2
}.
}
\tag{C1zB2C6q.43}
\]

Auch diese Darstellung ist resolventenfrei.

Sie zeigt zugleich, warum `q_r` trotz der expliziten Struktur nicht trivial klein sein muss: Der zweite Term enthält die volle targetseitige Restgrammwirkung `R_TR_T^*` auf `R_T1_T`.

---

# 12. Was C6q nicht beweist

C6q beweist **nicht**:

\[
q_{r,T}\to0,
\]

nicht

\[
q_{r,T}\lesssim e^{-T},
\]

nicht

\[
\inf_T\beta_{R,T}>0,
\]

nicht

\[
q_{b,T}=O(1),
\]

und nicht

\[
a_{R,T}^{(2)}\ne0.
\]

Ebenso wenig wird die Cross-Prime-Geometrie aus C6e--C6j abgeschwächt. Sie bleibt für `h_T` und den exakten Separator vollständig gültig. C6q sagt ausschließlich:

\[
\boxed{
\text{arithmetische Provenienz eines Sourceprofils}
\ne
\text{Rest-Spektrallokalisierung dieses Profils}.
}
\tag{C1zB2C6q.44}
\]

Um `q_{r,T}` klein zu machen, muss die tatsächliche quadratische Form (C1zB2C6q.18) auf `r_T` kontrolliert werden.

---

# 13. Neuer atomarer Folgeauftrag

C6q zeigt, dass `q_{r,T}` als erster der drei Parameter eine eigene asymptotische Analyse verdient.

Der nächste Knoten soll daher nicht nochmals die drei Parameter gemeinsam behandeln, sondern ausschließlich

\[
\boxed{
q_{r,T}
=
\frac{\mathfrak R_T[r_T]}{\|r_T\|^2}
}
\]

untersuchen.

Die natürliche Strategie ist:

1. `r_T=h_T-\lambda_TA_T1_T` in die exakte Restquadratform (C1zB2C6q.18) einsetzen;
2. die Beiträge nach p-Tiefe und nach Hub-/Rest-Breakpointlagen organisieren;
3. prüfen, ob die C6e--C6j-Cross-Prime-Kante lediglich eine Nenner-Untergrenze liefert oder zusätzlich echte Cancellation in den Rest-Translationsdifferenzen erzwingt;
4. keinerlei Smallness aus der bloßen Bezeichnung „cross-prime“ ableiten.

Arbeitsname:

\[
\boxed{
\text{C6r: Residual Rest-Loading Asymptotic.}
}
\]

Ein positiver Ausgang wäre beispielsweise

\[
q_{r,T}=o(1)
\]

oder auch nur eine explizite Schranke `q_{r,T}<=Q_T` mit `Q_T` deutlich kleiner als der globale `O(Te^T)`-Bound.

Ein negativer Ausgang wäre ebenso wertvoll: falls die explizite Restquadratform auf `r_T` keine Smallness zeigt oder sogar eine persistente Restladung erzwingt, wäre die C6p-Route über kleines `s_{r,T}` zu versiegeln und der Hebel müsste auf `beta_{R,T}` oder `q_{b,T}` wechseln.

---

# 14. Endurteil

C6q löst das Alignmentproblem nicht, aber es verschiebt den Engpass von einer abstrakten Feshbach-Geometrie auf explizite arithmetische Quadratformen.

Die drei natürlichen C6p-Koordinaten sind nun nicht nur konzeptionell, sondern **rechnerisch typisiert**:

\[
\boxed{
\begin{array}{rcl}
q_{r,T}
&=&
\mathfrak R_T[r_T]/\|r_T\|^2,\\[1mm]
q_{b,T}
&=&
\mathfrak R_T[b_{R,T}]/\|b_{R,T}\|^2,\\[1mm]
\beta_{R,T}
&=&
|\langle Jg_{R,T},H_Tr_T\rangle|/(\|b_{R,T}\|\|r_T\|).
\end{array}
}
\tag{C1zB2C6q.45}
\]

Der Rest-Gramkernel ist exakt bekannt:

\[
\boxed{
\langle q_{p,k,T}(u),q_{p,l,T}(u)\rangle
=
p^{-(k+l)/2}
\left(p^{\min(k,l,J_{p,T}(u))}-1\right).
}
\tag{C1zB2C6q.46}
\]

Damit ist die nächste echte Mathematik nicht mehr „finde eine geeignete Darstellung“, sondern:

\[
\boxed{
\text{werte diese explizite Quadratform auf dem echten Residualvektor }r_T\text{ asymptotisch aus.}
}
\]

P11 bleibt `PASS-A ACTIVE`. Alle persistenten No-Gos bleiben erhalten. Kein SYN, kein Seal, kein `papers/P11`.
