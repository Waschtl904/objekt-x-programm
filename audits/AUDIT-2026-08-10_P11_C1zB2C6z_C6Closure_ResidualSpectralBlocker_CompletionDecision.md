# P11-C1z-B2-C6z — C6-Abschlussaudit, residualspektraler Blocker und Completion-Entscheid

**Datum:** 2026-08-10  
**Programm:** P11 / C1z / B2 / C6  
**Modus:** `PASS-A ACTIVE`  
**Vorgänger:** C6y — `ResidualSpectralMass_ArithmeticAvoidance_BVFirewall`  
**Scope:** lokaler Abschlussaudit des C6-Strangs; genau ein atomarer Auditknoten; kein SYN, kein Seal, kein `papers/P11`.

---

## 0. Auditstatus

\[
\boxed{
\begin{aligned}
[P11\text{-}C1z\text{-}B2\text{-}C6z]
&\quad \checkmark[K/M]_{\rm closure}\\
&+\checkmark[M]_{\rm pos,C6\text{-}inventory\text{-}complete}\\
&+\checkmark[M]_{\rm corr,R1\text{-}denominator\text{-}not\text{-}fully\text{-}uncontrolled}\\
&+\checkmark[M]_{\rm pos,weak\text{-}global\text{-}BV\text{-}majorant}\\
&+\checkmark[M]_{\rm pos,weak\text{-}explicit\text{-}\Gamma_T\text{-}bound}\\
&+\checkmark[M]_{\rm neg,weak\text{-}R1\text{-}bound\text{-}not\text{-}uniformly\text{-}useful}\\
&+\checkmark[M]_{\rm neg,R2\text{-}requires\text{-}new\text{-}quantitative\text{-}nonapproximation}\\
&+\checkmark[M]_{\rm neg,R3\text{-}requires\text{-}new\text{-}coefficient\text{-}observability}\\
&+\checkmark[M]_{\rm neg,window\text{-}lower\text{-}transfer\text{-}missing}\\
&+\checkmark[M]_{\rm pos,pure\text{-}ambient\text{-}route\text{-}closed}\\
&+\checkmark[M]_{\rm pos,C6\text{-}locally\text{-}closed\text{-}with\text{-}exported\text{-}blocker}\\
&+?[O]_{\rm q_{r,T}\;asymptotic}\\
&+?[O]_{\rm a_{R,T}^{(2)}\neq0}.
\end{aligned}
}
\]

**Kernurteil.** C6 kann nach C6z **lokal abgeschlossen** werden, aber ausdrücklich nicht als Lösung des übergeordneten Rest-Nichtverschwindungsproblems. Der Strang hat seine eigene Mechanismenklasse vollständig ausgereizt:

- lokale Cross-Prime-Separation und positive Residual-/Kanalmasse wurden bewiesen;
- finite Jet-, einzelne Prime-, finite mixed-prime und schließlich volle ambiente Frame-Routen wurden geprüft und dort, wo sie scheitern, mit expliziten No-Gos geschlossen;
- C6y hat die verbleibende positive Möglichkeit auf die konkrete Fourier-/Sprungstruktur des Residualvektors reduziert.

C6z führt noch den letzten kurzen Koeffizientencheck durch. Dabei entsteht eine neue Präzisierung: Die in C6y definierte relative Sprungkomplexität

\[
\Gamma_T
=\frac{\operatorname{TV}(\widetilde r_T)}{\|r_T\|_2}
\]

ist nicht völlig ohne explizite Schranke. Aus bereits auditierten C6i/C6g/C6h/C6u-Daten lässt sich grob

\[
\boxed{
\Gamma_T
\le C T^{5/2}e^{9T/2}
}
\tag{C1zB2C6z.1}
\]

ableiten.

Das schließt **R1 in einer schwachen Finite-Horizon-Version**. Diese Schranke ist jedoch viel zu groß, um zusammen mit den vorhandenen Symbolinformationen eine uniforme Untergrenze für

\[
q_{r,T}
=\frac{\|R_Tr_T\|^2}{\|r_T\|^2}
\]

zu liefern. Die verbleibende Hürde ist qualitativ neu: quantitative Nichtapproximation auf einem expandierenden Frequenzband und/oder direkte Observability des tatsächlichen Sprung-Exponentialpolynoms, zusätzlich gekoppelt mit einem unteren Fenstertransfer.

Daher lautet die Abschlussentscheidung:

\[
\boxed{
\text{C6 = lokal geschlossen mit explizit exportiertem residualspektralem Blocker.}
}
\tag{C1zB2C6z.2}
\]

und zugleich

\[
\boxed{
P11=\texttt{PASS-A ACTIVE}.
}
\tag{C1zB2C6z.3}
\]

Kein SYN, kein Seal, kein `papers/P11`.

---

# 1. Zweck des Abschlussaudits

C6z ist bewusst **kein weiterer Mechanismusknoten**.

Nach C6y gibt es drei typisierte Restaufgaben:

\[
\text{R1: relative Sprungkomplexität},
\]

\[
\text{R2: quantitative Quasi-Null-Nichtapproximation},
\]

\[
\text{R3: direkte Sprungkoeffizienten-/Kanal-Observability}.
\]

C6z stellt deshalb nur drei Fragen:

1. Lässt sich R1 noch mit einem kurzen, bereits in C6 angelegten Koeffizientenargument quantitativ schließen?
2. Sind R2/R3 noch Fortsetzungen desselben C6-Mechanismus oder verlangen sie eine neue Theoremklasse?
3. Darf C6 danach lokal geschlossen werden, ohne das offene P11-Ziel fälschlich als gelöst zu markieren?

Die Antwort wird in §§3–12 formalisiert.

---

# 2. Inventur C6–C6y

Der C6-Strang lässt sich rückblickend in sechs funktionale Phasen gliedern.

## Phase I — finite Jets, Winkel und Krylov-Reduktionen

Die frühen Knoten C6–C6d prüfen, ob die benötigte zweite Richtung aus endlichen Jets, Gramwinkeln, Rank-one-/Feshbach-Reduktionen oder einer automatischen Multi-Probe-Struktur folgt.

Die positiven Strukturteile bleiben erhalten; die automatischen Schlussfolgerungen werden durch die jeweiligen Firewalls ausgeschlossen.

Insbesondere ist der spätere Residualvektor nicht durch eine endliche Jet-Triangularität bereits kontrolliert.

## Phase II — Cross-Prime-Separation und lokale quantitative Positivität

C6e–C6j identifizieren echte Cross-Prime-Hubkanten, kontrollieren lokales Hub- und Rest-Crowding und konstruieren schließlich einen exakten lokalen Separator.

Der quantitative Höhepunkt dieser Phase ist C6i:

\[
\boxed{
\Delta_T^{(1)}
\ge
c_\Delta\frac{e^{-5T}}{T}
\qquad(T\gg1).
}
\tag{C1zB2C6z.4}
\]

Diese Untergrenze ist positiv, aber selbst verschwindend. Sie ist deshalb ein echter Rang-/Nichtverschwindensbefund auf endlichem Horizont, keine asymptotische Stabilitätsklassifikation.

## Phase III — 2×2-/Feshbach-/Residual-Firewalls

C6k–C6r testen verschiedene Versuche, lokale Positivität in eine globale zweite Alignment- oder Restquotienten-Aussage zu übersetzen.

Die wiederkehrende Trennung lautet:

\[
\text{lokale Nichtverschwindung}
\not\Rightarrow
\text{uniforme relative Restmasse}.
\]

Insbesondere dürfen Orthogonalität, Positivität, Support-Provenienz und Momentinformationen nicht mit dem benötigten zweiten Alignment-Skalar gleichgesetzt werden.

## Phase IV — exakte Martingalquadrate und lokaler 2-adischer Kanal

C6s etabliert die positive Kanalzerlegung

\[
\boxed{
\|R_Tf\|_2^2
=
\sum_{(p,a)\in\mathcal I_T}
\mathcal E_{p,a,T}(f),
\qquad
\mathcal E_{p,a,T}(f)\ge0.
}
\tag{C1zB2C6z.5}
\]

C6t identifiziert einen festen nichtverschwindenden gefilterten Sprung im ersten 2-adischen Kanal; C6u macht daraus eine quantitative absolute Kanalenergie.

Gleichzeitig zeigt C6u bereits die zentrale Firewall:

\[
\text{fixer Sprung}
\not\Rightarrow
q_{r,T}\not\to0.
\]

## Phase V — Schließung der ambienten Frame-Route

C6v zeigt den single-prime Bulk-Nullstellenmechanismus. C6w erweitert ihn auf feste mixed-prime Familien. C6x geht bis zur vollen aktiven Prime-/Tiefenfamilie und beweist

\[
\boxed{
\inf_{f\perp\mathbf1_T}
\frac{\|R_Tf\|_2^2}{\|f\|_2^2}
\longrightarrow0.
}
\tag{C1zB2C6z.6}
\]

Damit ist die **pure ambiente Frame-Route geschlossen**.

## Phase VI — residualspezifische Fourierstruktur

C6y wechselt deshalb korrekt vom ambienten Raum zum konkreten

\[
r_T=h_T-\lambda_TA_T\mathbf1_T.
\]

Die Nullfortsetzung liefert

\[
\widehat r_T(0)=0,
\]

sowie die relative Niederfrequenzschranke

\[
\boxed{
\frac{
\frac1{2\pi}\int_{|\xi|\le\kappa/T}
|\widehat r_T(\xi)|^2d\xi
}{\|r_T\|_2^2}
\le
\frac{2\kappa^3}{9\pi}.
}
\tag{C1zB2C6z.7}
\]

Für das tatsächliche Sprungmaß

\[
D\widetilde r_T
=
\sum_\beta J_T(\beta)\delta_\beta
\]

gilt exakt

\[
\boxed{
i\xi\widehat r_T(\xi)
=P_T(\xi)
:=
\sum_\beta J_T(\beta)e^{-i\xi\beta}.}
\tag{C1zB2C6z.8}
\]

Mit

\[
V_T:=\sum_\beta|J_T(\beta)|,
\qquad
\Gamma_T:=\frac{V_T}{\|r_T\|_2}
\]

folgt der relative BV-Tail

\[
\boxed{
\frac{
\frac1{2\pi}\int_{|\xi|\ge X}
|\widehat r_T(\xi)|^2d\xi
}{\|r_T\|_2^2}
\le
\frac{\Gamma_T^2}{\pi X}.}
\tag{C1zB2C6z.9}
\]

C6z setzt genau hier an.

---

# 3. Korrektur/Präzisierung: der Nenner von \(\Gamma_T\) besitzt bereits eine explizite Untergrenze

C6y formulierte korrekt, dass aus der dort verwendeten **Obergrenze** für `||r_T||` keine relative TV-Kontrolle folgt.

Für den Abschlussaudit muss aber zusätzlich C6i mit C6us exakter Defektidentität kombiniert werden.

C6u verwendet

\[
\boxed{
\Delta_T^{(1)}
=
\langle r_T,A_T^{-1}r_T\rangle.}
\tag{C1zB2C6z.10}
\]

Da

\[
A_T=I+R_T^*R_T\ge I,
\]

gilt

\[
0<A_T^{-1}\le I.
\]

Somit

\[
\boxed{
\Delta_T^{(1)}
\le
\|r_T\|_2^2.}
\tag{C1zB2C6z.11}
\]

Mit C6i, Gleichung (C1zB2C6z.4), folgt daher sofort

\[
\boxed{
\|r_T\|_2^2
\ge
c_\Delta\frac{e^{-5T}}{T}.}
\tag{C1zB2C6z.12}
\]

beziehungsweise

\[
\boxed{
\|r_T\|_2
\ge
c_0T^{-1/2}e^{-5T/2}.}
\tag{C1zB2C6z.13}
\]

mit `c_0=\sqrt{c_\Delta}>0`.

Dies ist sehr schwach, aber wichtig für die Buchhaltung:

\[
\boxed{
\text{Der Nenner von }\Gamma_T\text{ ist nicht völlig skalenfrei.}}
\]

Die C6y-Firewall bleibt trotzdem inhaltlich richtig: Es fehlte dort eine **brauchbare relative** TV-Schranke. C6z ergänzt nun die bisher nicht kombinierte schwache Defektuntergrenze.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,R1\text{-}denominator\text{-}not\text{-}fully\text{-}uncontrolled}.}
\tag{C1zB2C6z.14}
\]

---

# 4. Eine zulässige obere Schranke für \(\lambda_T\)

Wir benötigen keine Asymptotik von `lambda_T`.

Aus

\[
\lambda_T
=
\frac{\langle\mathbf1_T,h_T\rangle}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}
\]

und `A_T>=I` folgt

\[
\langle\mathbf1_T,A_T\mathbf1_T\rangle
\ge
\|\mathbf1_T\|_2^2
=2T.
\]

Cauchy-Schwarz liefert

\[
|\langle\mathbf1_T,h_T\rangle|
\le
\sqrt{2T}\,\|h_T\|_2.
\]

C6u beweist die grobe Hubnormschranke

\[
\|h_T\|_2
\le
C_hT^{3/2}e^T.
\]

Daher

\[
\boxed{
0\le\lambda_T
\le
C_\lambda T e^T.}
\tag{C1zB2C6z.15}
\]

Dies ist nur eine obere Schranke.

Insbesondere wird weiterhin **nicht** behauptet

\[
\lambda_T\asymp Te^T.
\]

---

# 5. Globale BV-Majorante für den Hubteil

C6g schreibt

\[
h_T
=
\sum_{n,m\in\mathcal N_T}
 a_na_m
 K_{\log n}^*K_{\log m}\mathbf1_T,
\]

mit

\[
a_{p^k}
=\sqrt{\log p}\,p^{-3k/4}.
\]

C6u beweist elementar

\[
\boxed{
\sum_{n\in\mathcal N_T}a_n
\le
C_a\sqrt T\,e^{T/2}.}
\tag{C1zB2C6z.16}
\]

Für jedes feste Paar `(n,m)` ist

\[
K_{\log n}^*K_{\log m}\mathbf1_T
\]

eine zweifach gebildete komprimierte Differenz einer Intervallindikatorfunktion. Eine einzelne Differenz erzeugt nur universell viele Sprungkanten mit universell beschränkten ganzzahligen Koeffizienten; die zweite Differenz sowie die Nullfortsetzung vermehren diese Zahl nur um einen absoluten Faktor.

Daher existiert eine absolute Konstante `C_{BV,h}` mit

\[
\boxed{
\operatorname{TV}
\left(
\widetilde{K_{\log n}^*K_{\log m}\mathbf1_T}
\right)
\le C_{BV,h}}
\tag{C1zB2C6z.17}
\]

für alle aktiven `n,m,T`.

Mit der Dreiecksungleichung für totale Variation folgt

\[
\begin{aligned}
\operatorname{TV}(\widetilde h_T)
&\le
C_{BV,h}
\sum_{n,m}a_na_m\\
&=
C_{BV,h}
\left(\sum_na_n\right)^2.
\end{aligned}
\]

Also nach (C1zB2C6z.16)

\[
\boxed{
\operatorname{TV}(\widetilde h_T)
\le
C_h^{BV}T e^T.}
\tag{C1zB2C6z.18}
\]

Diese Schranke ist absichtlich grob. Sie benutzt keine Cancellation zwischen Hubpaaren.

---

# 6. Globale BV-Majorante für \(A_T\mathbf1_T\)

Die schwierige Seite ist

\[
A_T\mathbf1_T
=
\mathbf1_T+R_T^*R_T\mathbf1_T.
\]

C6g warnte korrekt:

\[
\|R_T\|\text{-Kontrolle allein}
\not\Rightarrow
\text{lokale BV-Kontrolle}.
\]

C6h liefert jedoch danach die konkret benötigten prime-puren **Sprungkoeffizienten**. Für eine Restkante

\[
y_{p,m}(T)
=-T+\frac m2\log p
\]

gilt blockweise

\[
\boxed{
\left|
\operatorname{Jump}_{y_{p,m}(T)}
(R_{p,T}^*R_{p,T}\mathbf1_T)
\right|
\le
C\,m\log p\,p^{-(m+2)/4}.}
\tag{C1zB2C6z.19}
\]

Die Spiegelkante erfüllt dieselbe absolute Schranke. Da die Restseite prime-pure ist, genügt für eine globale Majorante die Summe der rechten Seite über aktive `(p,m)`.

Aktivität erzwingt grob

\[
m\log p\le4T.
\]

Wir zerlegen nach `m=1` und `m>=2`.

## 6.1 Tiefe \(m=1\)

Hier ist

\[
m\log p\,p^{-(m+2)/4}
=(\log p)p^{-3/4}.
\]

Mit `p<=e^{4T}` und der Majorisierung durch alle ganzen Zahlen folgt elementar

\[
\begin{aligned}
\sum_{p\le e^{4T}}
(\log p)p^{-3/4}
&\le
\sum_{2\le n\le e^{4T}}
(\log n)n^{-3/4}\\
&\le
C T e^T.
\end{aligned}
\tag{C1zB2C6z.20}
\]

## 6.2 Tiefen \(m\ge2\)

Für jedes `p>=2` gilt wegen geometrischer Summation

\[
\sum_{m\ge2}
m p^{-(m+2)/4}
\le
C p^{-1}.
\tag{C1zB2C6z.21}
\]

Daher

\[
\begin{aligned}
\sum_{p}
\sum_{m\ge2}
 m(\log p)p^{-(m+2)/4}
&\le
C\sum_{p\le e^{2T}}
\frac{\log p}{p}\\
&\le
C\sum_{2\le n\le e^{2T}}
\frac{\log n}{n}\\
&\le
C T^2.
\end{aligned}
\tag{C1zB2C6z.22}
\]

Damit dominiert der `m=1`-Teil und wir erhalten einschließlich der universell vielen Rand-/Spiegelbeiträge

\[
\boxed{
\operatorname{TV}
\left(
\widetilde{R_T^*R_T\mathbf1_T}
\right)
\le
C_R^{BV}T e^T.}
\tag{C1zB2C6z.23}
\]

Da

\[
\operatorname{TV}(\widetilde{\mathbf1_T})=2,
\]

folgt

\[
\boxed{
\operatorname{TV}
\left(
\widetilde{A_T\mathbf1_T}
\right)
\le
C_A^{BV}T e^T.}
\tag{C1zB2C6z.24}
\]

Wichtig: Dies widerspricht C6g nicht. C6g schloss die **unzulässige Ableitung aus einer globalen Operatornorm** aus. C6z benutzt stattdessen genau die später in C6h berechneten prime-puren Sprunggewichte.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,weak\text{-}global\text{-}BV\text{-}majorant}.}
\tag{C1zB2C6z.25}
\]

---

# 7. Schwache explizite R1-Schranke

Aus

\[
r_T
=h_T-\lambda_TA_T\mathbf1_T
\]

folgt mit (C1zB2C6z.15), (C1zB2C6z.18) und (C1zB2C6z.24)

\[
\begin{aligned}
V_T
:=\operatorname{TV}(\widetilde r_T)
&\le
\operatorname{TV}(\widetilde h_T)
+\lambda_T
\operatorname{TV}(\widetilde{A_T\mathbf1_T})\\
&\le
C T e^T
+C(T e^T)(T e^T).
\end{aligned}
\]

Somit

\[
\boxed{
V_T
\le
C_VT^2e^{2T}.}
\tag{C1zB2C6z.26}
\]

Kombiniert mit der Residualnorm-Untergrenze (C1zB2C6z.13) folgt

\[
\begin{aligned}
\Gamma_T
&=
\frac{V_T}{\|r_T\|_2}\\
&\le
C
\frac{T^2e^{2T}}
{T^{-1/2}e^{-5T/2}}.
\end{aligned}
\]

Also

\[
\boxed{
\Gamma_T
\le
C_\Gamma T^{5/2}e^{9T/2}.}
\tag{C1zB2C6z.27}
\]

und damit

\[
\boxed{
\Gamma_T^2
\le
C_\Gamma' T^5e^{9T}.}
\tag{C1zB2C6z.28}
\]

Dies ist der kurze Koeffizientencheck, den C6z vor einer Abschlussentscheidung leisten musste.

Er schließt R1 in folgender **schwacher** Bedeutung:

\[
\boxed{
\text{Für jeden Horizont existiert eine explizite C6-interne obere Skala für }\Gamma_T.}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,weak\text{-}explicit\text{-}\Gamma_T\text{-}bound}.}
\tag{C1zB2C6z.29}
\]

---

# 8. Warum die neue \(\Gamma_T\)-Schranke C6 nicht positiv abschließt

C6ys Hochfrequenz-Tail lautet

\[
\frac{
\frac1{2\pi}\int_{|\xi|\ge X}
|\widehat r_T(\xi)|^2d\xi
}{\|r_T\|_2^2}
\le
\frac{\Gamma_T^2}{\pi X}.
\]

Setzt man die explizite Majorante

\[
G_T:=C_\Gamma T^{5/2}e^{9T/2}
\]

ein und wählt

\[
X_T=M G_T^2,
\]

so erhält man weiterhin

\[
\frac{
\frac1{2\pi}\int_{|\xi|\ge X_T}
|\widehat r_T(\xi)|^2d\xi
}{\|r_T\|_2^2}
\le
\frac1{\pi M}.
\tag{C1zB2C6z.30}
\]

Zusammen mit der Niederfrequenzkontrolle liegt also ein großer Anteil der Residualmasse im nun **expliziten** Zwischenband

\[
\boxed{
\frac\kappa T
<|\xi|
<
C_M T^5e^{9T}.}
\tag{C1zB2C6z.31}
\]

Das ist eine Verbesserung der Buchhaltung, aber keine uniforme Observability-Aussage.

Denn:

1. das obere Bandende wächst extrem schnell;
2. C6w/C6x zeigen gemeinsame Quasi-Nullfrequenzen der ambienten Prime-Symbole;
3. C6y korrigiert bereits, dass Dirichlets Nenner-Obergrenze keine Untergrenze für die erste solche Frequenz ist;
4. selbst ein positiver Vollraum-Symbolgap auf jedem festen kompakten Band ist nicht uniform in dem expandierenden Band (C1zB2C6z.31);
5. die tatsächliche C6s-Energie besteht aus komprimierten Fensterkanälen, nicht aus einem bereits bewiesenen globalen Fouriermultiplikator mit positiver unterer Symbolschranke.

Daher gilt ausdrücklich nicht

\[
\Gamma_T\le C T^{5/2}e^{9T/2}
\Longrightarrow
q_{r,T}\not\to0.
\]

Die neue R1-Schranke ist eine **Finite-Horizon-Kontrolle**, keine uniforme Restkoerzivität.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,weak\text{-}R1\text{-}bound\text{-}not\text{-}uniformly\text{-}useful}.}
\tag{C1zB2C6z.32}
\]

---

# 9. R2 ist eine neue arithmetische Theoremklasse

Nach (C1zB2C6z.31) wäre ein möglicher positiver Weg eine quantitative Aussage vom Typ:

\[
\boxed{
\text{Für }
\kappa/T\le|\xi|\le C T^5e^{9T}
\text{ können die gewichtsstarken aktiven Prime-Winkel nicht alle zu nahe an }\pi\mathbb Z\text{ liegen.}
}
\tag{C1zB2C6z.33}
\]

Das ist **nicht** die in C6w/C6x verwendete simultane Dirichlet-Approximation.

Dirichlet garantiert gute Approximationen; R2 benötigt quantitative **Nichtapproximation** beziehungsweise eine kontrollierte Beschreibung der schlechten Menge auf einem `T`-abhängigen expandierenden Frequenzbereich.

Die bisherigen C6-Arithmetikwerkzeuge — eindeutige Primfaktorzerlegung, ganzzahlige Separatorargumente, elementare gewichtete Crowding-Summen — liefern eine solche Aussage nicht.

Man könnte für einen einzelnen festen Frequenzbereich triviale kompakte Positivität oder sehr schwache diskrete Separationsschranken formulieren. Das würde jedoch nur `T`-abhängige Konstanten erzeugen und die benötigte uniforme relative Untergrenze nicht schließen.

Daher lautet der Completion-Befund:

\[
\boxed{
\text{R2 ist kein fehlender Rechenschritt in C6, sondern neue quantitative Arithmetik.}
}
\tag{C1zB2C6z.34}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,R2\text{-}requires\text{-}new\text{-}quantitative\text{-}nonapproximation}.}
\]

---

# 10. R3 ist eine neue koeffizientenempfindliche Observability-Aufgabe

C6y identifiziert exakt

\[
P_T(\xi)
=
\sum_{\beta\in\mathcal B_T^{\rm act}}
J_T(\beta)e^{-i\xi\beta}.
\]

Die BV-Majorante aus C6z verwendet nur

\[
|P_T(\xi)|
\le
\sum_\beta|J_T(\beta)|
=V_T.
\]

Sie verwirft damit gerade die Phasen- und Vorzeichenstruktur, die für eine **untere** Observability-Schranke entscheidend wäre.

Eine positive R3-Aussage müsste etwa beweisen, dass die konkret aus

\[
h_T-\lambda_TA_T\mathbf1_T
\]

stammenden Koeffizienten auf den schlechten Prime-Phasen nicht gleichzeitig so cancellieren können, dass fast die gesamte Residualmasse kanalunsichtbar wird.

Das verlangt mindestens eine der folgenden neuen Informationen:

- einen vollständigen oder hinreichend strukturierten Census der **tatsächlichen** Sprungkoeffizienten `J_T(\beta)` nach Cancellations;
- eine arithmetische Untergrenze für gewichtete Exponentialsummen `P_T(\xi)` auf der relevanten schlechten Menge;
- oder eine direkte räumliche Untergrenze für die volle Martingalsumme am konkreten `r_T`, die den Fourierweg umgeht.

Keine dieser Aussagen ist in C6a–C6y vorhanden.

Daher:

\[
\boxed{
\text{R3 ist eine neue residualspezifische Koeffizienten-Observability-Aufgabe.}
}
\tag{C1zB2C6z.35}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,R3\text{-}requires\text{-}new\text{-}coefficient\text{-}observability}.}
\]

---

# 11. Unabhängiger analytischer Blocker: Fenster-Lower-Transfer

Selbst wenn R2 auf Vollraum-Symbolebene eine gute Menge identifiziert, fehlt noch ein zweiter Schritt.

Die C6s-Kanalenergie lautet exakt

\[
\|R_Tr_T\|^2
=
\sum_{p,a}
\mathcal E_{p,a,T}(r_T),
\]

wobei jeder Kanal auf seiner komprimierten Domain `\Omega_{p,a,T}` lebt.

C6x konnte für die ambienten Quasimoden eine **obere** Bulk-plus-Rand-Abschätzung aufbauen. Für einen positiven Beweis benötigt man jedoch die umgekehrte Richtung:

\[
\boxed{
\text{relevante Vollraum-/Fenster-Fouriermasse}
\Longrightarrow
\text{quantitativ positive Summe komprimierter Kanalenergien}.}
\tag{C1zB2C6z.36}
\]

Ein solcher unterer Transfer ist in C6s–C6y nicht bewiesen.

Er ist logisch von R2 zu trennen: Eine gute arithmetische Symbolschranke allein darf nicht direkt in `q_{r,T}` eingesetzt werden, solange die Fensterkompression nicht in der unteren Richtung kontrolliert ist.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,window\text{-}lower\text{-}transfer\text{-}missing}.}
\tag{C1zB2C6z.37}
\]

---

# 12. Completion-Entscheid für C6

Nach §§2–11 ist die Lage vollständig typisiert.

Innerhalb C6 wurden folgende Mechanismen tatsächlich geprüft:

\[
\text{finite Jets / Gramwinkel / Rank-one / Krylov},
\]

\[
\text{lokale Cross-Prime-Separation},
\]

\[
\text{Rest-/Hub-Crowding und exakter Separator},
\]

\[
\text{Martingalquadrate und einzelne Kanäle},
\]

\[
\text{finite und expandierende ambiente Frames},
\]

\[
\text{residualspezifische Fourier-/BV-Reduktion}.
\]

Die letzten noch fehlenden Aussagen R2/R3 plus Fenster-Lower-Transfer sind nicht bloß eine weitere Variante derselben getesteten C6-Mechanismen. Sie verlangen neue quantitative Theoreme über entweder

\[
\text{logarithmische simultane Nichtapproximation},
\]

oder

\[
\text{arithmetische Exponentialsummen tatsächlicher Residualsprünge},
\]

sowie gegebenenfalls einen neuen unteren Fenster-Observability-Satz.

Deshalb wäre ein weiterer alphabetischer Knoten `C6aa` inhaltlich irreführend. Er würde einen qualitativ neuen Arbeitsblock künstlich als Restrechnung von C6 erscheinen lassen.

Die korrekte lokale Abschlussmarkierung ist:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6]
=\texttt{LOCALLY CLOSED / EXPLICIT RESIDUAL-SPECTRAL BLOCKER}.}
\tag{C1zB2C6z.38}
\]

`LOCALLY CLOSED` bedeutet hier ausdrücklich **nicht**:

\[
q_{r,T}\not\to0,
\]

nicht

\[
q_{r,T}\to0,
\]

nicht

\[
a_{R,T}^{(2)}\neq0,
\]

und nicht

\[
P11\text{ abgeschlossen}.
\]

Es bedeutet nur:

> Der C6-Strang hat den aktuellen Mechanismusraum bis zu einem klar benannten neuen Theoremtyp reduziert; weitere Arbeit sollte unter einem neuen Arbeitsblock geführt werden.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,C6\text{-}locally\text{-}closed\text{-}with\text{-}exported\text{-}blocker}.}
\tag{C1zB2C6z.39}
\]

---

# 13. C7 statt B3

Der offene Gegenstand bleibt derselbe B2-Residualmechanismus:

\[
r_T,
\qquad
R_T,
\qquad
q_{r,T},
\qquad
P_T(\xi).
\]

Es wird also noch keine neue übergeordnete B-Architektur benötigt. Neu ist die **Theoremklasse**, nicht das Grundobjekt.

Daher ist die natürlichere Fortsetzung nach diesem Abschlussaudit ein neuer Geschwisterblock

\[
\boxed{[P11\text{-}C1z\text{-}B2\text{-}C7]}
\]

und nicht unmittelbar `B3`.

Ein geeigneter Arbeitstitel wäre etwa

`ResidualArithmeticObservability_WindowedExponentialSums`.

Ein solcher C7-Block sollte atomar trennen:

1. **C7a — ActualJumpCoefficientCensus:** tatsächliche `J_T(\beta)` und Cancellations aus `h_T-\lambda_TA_T1_T`;
2. **C7b — QuasiNullNonApproximation:** quantitative schlechte Prime-Phasen im expliziten C6z-Band;
3. **C7c — WindowedLowerTransfer:** untere Übertragung von spektraler Masse auf die komprimierten Martingalkanäle;
4. erst danach eine erneute Entscheidung über `q_{r,T}` beziehungsweise `a_{R,T}^{(2)}`.

Dies ist eine **Arbeitsstruktur-Empfehlung**, kein neu eröffneter Knoten in diesem Commit.

C6z erzeugt nur den Abschlussaudit C6z.

---

# 14. Gegenprüfer-Checkliste

## Test 1 — wurde aus C6is verschwindender \(\Delta\)-Untergrenze zu viel gefolgert?

Nein.

C6z benutzt nur

\[
\Delta_T^{(1)}\le\|r_T\|^2
\]

und erhält daraus eine ebenfalls sehr schwache Residualnorm-Untergrenze. Es wird keine uniforme Stabilität behauptet.

## Test 2 — wurde \(\lambda_T\asymp Te^T\) wieder eingeführt?

Nein.

Verwendet wird ausschließlich die rigorose obere Schranke

\[
\lambda_T\le CTe^T.
\]

## Test 3 — widerspricht die globale BV-Majorante C6g?

Nein.

C6g verbot die Ableitung lokaler BV-Kontrolle allein aus `||R_T||`. C6z benutzt zusätzlich die in C6h später explizit bewiesenen prime-puren Sprunggewichte und summiert deren Absolutwerte.

## Test 4 — beweist die neue \(\Gamma_T\)-Schranke Spektralvermeidung?

Nein.

Sie macht C6ys Zwischenband explizit, aber das Band wächst bis grob `T^5e^{9T}`. Darin gibt es ohne R2/R3 keine uniforme Observability.

## Test 5 — kann Dirichlet die fehlende R2-Aussage liefern?

Nein.

Dirichlet liefert Existenz guter Approximationen, nicht die für C6z benötigte Nichtapproximation.

## Test 6 — darf ein Vollraum-Symbolgap direkt auf \(R_T\) übertragen werden?

Nein.

Der untere Fenstertransfer fehlt.

## Test 7 — ist C6 damit „bewiesen“ oder P11 fertig?

Nein.

Nur der lokale Arbeitsblock C6 ist abgeschlossen und exportiert seinen präzisen Blocker.

---

# 15. Persistente Firewalls nach C6z

Die folgenden Aussagen dürfen in späteren Blöcken nicht still überschrieben werden.

## C6z-A — weak-R1 firewall

\[
\boxed{
\Gamma_T\le C T^{5/2}e^{9T/2}
\text{ ist eine explizite obere Schranke, keine asymptotische Gleichheit und keine uniforme Observability.}}
\]

## C6z-B — ambient-route firewall

\[
\boxed{
\text{Keine ambiente Frame-Untergrenze darf nach C6x erneut als Rest-Nichtverschwindensmechanismus verwendet werden.}}
\]

## C6z-C — Dirichlet-direction firewall

\[
\boxed{
\text{Approximationsexistenz}
\neq
\text{Nichtapproximation der schlechten Frequenzmenge}.}
\]

## C6z-D — coefficient firewall

\[
\boxed{
\text{Breakpoint-Provenienz}
\neq
\text{Observability des gewichteten }P_T(\xi).}
\]

## C6z-E — window firewall

\[
\boxed{
\text{Vollraum-Symbolinformation}
\not\Rightarrow
\text{untere komprimierte Kanalenergie ohne separaten Transfer.}}
\]

## C6z-F — completion firewall

\[
\boxed{
\texttt{C6 LOCALLY CLOSED}
\neq
\texttt{P11 SEALED/SYN}.
}
\]

---

# 16. Offene Ziele nach C6-Abschluss

Weiterhin offen sind insbesondere

\[
\boxed{?[O]_{q_{r,T}\to0\;\text{oder}\;q_{r,T}\not\to0}},
\]

\[
\boxed{?[O]_{a_{R,T}^{(2)}\neq0}},
\]

und damit die übergeordnete echte 2×2-Invertibilitätsfrage.

C6z liefert hierzu keinen positiven oder negativen Endsatz.

Der Fortschritt ist struktureller Natur:

\[
\boxed{
\begin{minipage}{0.88\textwidth}
Der offene Rest ist nicht mehr „irgendwo in der Frame-/Krylov-Geometrie“. Er ist auf eine neue residualspezifische Theoremklasse reduziert: tatsächliche Sprungkoeffizienten, quantitative logarithmische Nichtapproximation und untere Fenster-Observability.
\end{minipage}}
\tag{C1zB2C6z.40}
\]

---

# 17. Abschlussfazit

C6z führt keinen neuen Rettungsmechanismus ein. Es prüft nur, ob C6y noch einen kurzen internen Abschluss zulässt.

Die Antwort ist zweigeteilt.

**Ja:** R1 kann schwach explizit gemacht werden. C6i liefert die bisher ungenutzte Residualnorm-Untergrenze

\[
\|r_T\|^2\ge c e^{-5T}/T,
\]

während C6g/C6h/C6u über die tatsächlichen Gewichte eine grobe globale Variationsmajorante

\[
V_T\le C T^2e^{2T}
\]

erlauben. Daraus folgt

\[
\boxed{
\Gamma_T\le C T^{5/2}e^{9T/2}.}
\]

**Nein:** Diese Schranke ist nicht stark genug, um die residualspezifische Observability zu schließen. Das relevante Spektralband kann noch bis etwa

\[
T^5e^{9T}
\]

wachsen. Auf diesem Band fehlen sowohl eine quantitative Nichtapproximation der Prime-Quasi-Nullen als auch eine koeffizientenempfindliche Untergrenze für `P_T`; zusätzlich fehlt der untere Transfer von Vollraum-/Fenster-Fourierinformation zu den tatsächlich komprimierten Martingalkanälen.

Damit ist die korrekte Programmentscheidung:

\[
\boxed{
\text{C6 lokal schließen; residualspektralen Blocker nach C7 exportieren.}}
\]

und unverändert

\[
\boxed{
P11=\texttt{PASS-A ACTIVE}.}
\]

Kein SYN, kein Seal, kein `papers/P11`.
