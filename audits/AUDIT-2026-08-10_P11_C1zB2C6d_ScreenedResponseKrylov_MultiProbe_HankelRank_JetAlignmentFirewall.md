# P11-C1z-B2-C6d — Screened-Response-Krylov-Probes, Hankel-Rangtest und Jet-Alignment-Firewall

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6d]`  
**Direkte Voraussetzungen:** C1z-B1, C1z-B2-C3, C1z-B2-C4, C1z-B2-C5, C1z-B2-C6, C1z-B2-C6a, C1z-B2-C6b, C1z-B2-C6c  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6d]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm corr,C4\text{-}jets\neq multi\text{-}probes}
+
\checkmark[M]_{\rm pos,screened\text{-}response\text{-}Krylov}
+
\checkmark[M]_{\rm pos,Hankel\text{-}rank\text{-}criterion}
+
\checkmark[M]_{\rm pos,second\text{-}probe\text{-}defect}
+
\checkmark[M]_{\rm pos,multi\text{-}probe\text{-}Gram\text{-}decomposition}
+
\checkmark[M]_{\rm neg,Krylov\text{-}rank\text{-}unproved}
+
\checkmark[M]_{\rm neg,orthogonality\not\Rightarrow jet\text{-}alignment}
+
\checkmark[M]_{\rm neg,primitive\text{-}screening\text{-}Krylov\text{-}collapse}
}
\]

C6d beantwortet die Multi-Probe-Frage in einer präzisen Mischform.

1. Die unendliche C4-Jetentwicklung erzeugt **keine** unendliche Familie terminaler Probes. Alle Jetkoeffizienten stammen aus derselben skalaren Beobachtung durch die eine Konstantenmode `\mathbf1_T` beziehungsweise deren gescreentes Bild `\zeta_T`.
2. Aus der vorhandenen Feshbach-Kolligation existiert dennoch eine kanonische echte Multi-Probe-Kandidatenfamilie: der Krylov-Flag des positiven gescreenten Huboperators
   \[
   \mathfrak S_T=A_T^{-1/2}H_T^*H_TA_T^{-1/2}
   \]
   ausgehend von `\zeta_T=A_T^{1/2}\mathbf1_T`.
3. Die lineare Unabhängigkeit der ersten `N+1` Probes ist exakt äquivalent zur Positivität einer expliziten Hankel-Momentmatrix. Es wird keine abstrakte Vollständigkeit postuliert.
4. Für die zweite Probe entsteht ein vollständig expliziter Nichtdegenerationsdefekt `\Delta_T^{(1)}`. Seine Positivität ist genau die Bedingung, dass überhaupt eine zweite kanonische Feshbach-Probe existiert.
5. Falls ein voller `N+1`-Probe-Frame existiert, zerlegt er die endliche Feshbach-Response-Grammatrix exakt in beobachteten Probe-Anteil plus transversalen Rest. Eine quantitative invertierbare Probe-Matrix würde daher echte finite-window Coercivity liefern.
6. Weder der Krylov-Rang noch die jet-trianguläre Ausrichtung dieses Frames folgen aus den bisherigen Knoten. Insbesondere erzwingt exakte Orthogonalität der Probes keine Triangularität ihrer Response-Matrix.
7. Der naheliegende alternative Krylov-Flag aus `A_T` allein kollabiert im primitiven Restmodell auf Rang eins, weil C3 den primitiven Rest auf `\mathbf1_T` exakt annihiliert. Jede zusätzliche `A_T`-Krylov-Richtung muss daher aus höheren Prime-Powers des Restes stammen.

Nicht bewiesen werden weiterhin

\[
\tau_T(E_{R,N})\to0,
\qquad
\Theta_{T,U}^{E_{R,N}}\to I,
\]

und damit auch nicht

\[
W_{R,S,-}^{[T]}\to W_{R,S,-}^{[\infty]}
\quad\text{stark}.
\]

---

# 0. Methodische Verkettung

C6d erbt nichts implizit.

## 0.1 Aus C1z-B1/C3

Auf dem Terminal-Source-Raum

\[
\mathscr H_T=L^2(-T,T)
\]

stehen die beschränkten Operatoren

\[
H_T:\mathscr H_T\to\mathscr H_T,
\qquad
R_T:\mathscr H_T\to\mathscr Y_T^0
\]

zur Verfügung.

Setze

\[
\boxed{
A_T:=I+R_T^*R_T\ge I.
}
\tag{C1zB2C6d.1}
\]

Damit sind für jedes feste `T`

\[
A_T^{\pm1/2}
\]

beschränkt und kanonisch definiert.

Die terminale Konstantenmode ist

\[
\mathbf1_T:=1_{(-T,T)}.
\]

C3 beweist für den **primitiven** konditionierten Restkanal exakt

\[
\boxed{
R_T^{(1)}\mathbf1_T=0,
}
\tag{C1zB2C6d.2}
\]

während die höheren Prime-Powers `k\ge2` nur durch eine polynomiale obere Restenergieschranke kontrolliert werden.

## 0.2 Aus C4

Für `F=\mathfrak B_Rf` gilt mit der Konstantenmode

\[
\langle J_{R,T}f,H_T\mathbf1_T\rangle
=
-\sqrt2\,e^{T/2}T^{-1/2}
\sum_{m=0}^{M}\frac{c_m}{T^m}\beta_R^{(m)}(f)
+
O_{R,M,f}(e^{T/2}T^{-M-3/2}).
\tag{C1zB2C6d.3}
\]

Die Jets `\beta_R^{(m)}` sind vollständig auf dem ungeraden Sektor.

## 0.3 Aus C6c

Der gescreente Feshbach-Response-Operator ist

\[
\boxed{
\mathcal X_{R,T}
:=
A_T^{-1/2}H_T^*J_{R,T}\mathfrak B_R^{-1}
:
\mathscr A_R^-\to\mathscr H_T.
}
\tag{C1zB2C6d.4}
\]

Für die kanonische Jet-ONB `(e_{R,m})` aus C6a setzen wir

\[
\xi_{R,m}^{(T)}
:=
\mathcal X_{R,T}e_{R,m}.
\tag{C1zB2C6d.5}
\]

Die terminale Feshbach-Response-Grammatrix auf

\[
E_{R,N}=\operatorname{span}\{e_{R,0},\ldots,e_{R,N}\}
\]

ist

\[
\bigl(
\langle\xi_{R,i}^{(T)},\xi_{R,j}^{(T)}\rangle
\bigr)_{0\le i,j\le N}.
\]

C6c identifizierte die C4-Probe als

\[
\boxed{
\zeta_T
:=
A_T^{1/2}\mathbf1_T.
}
\tag{C1zB2C6d.6}
\]

Dann gilt exakt

\[
\boxed{
\langle\mathcal X_{R,T}F,\zeta_T\rangle
=
\langle J_{R,T}f,H_T\mathbf1_T\rangle.
}
\tag{C1zB2C6d.7}
\]

---

# 1. Reconciliation — C4s unendlicher Jet ist keine terminale Multi-Probe-Familie

Die Expansion (C1zB2C6d.3) besitzt unendlich viele Koeffizienten

\[
\beta_R^{(0)},\beta_R^{(1)},\beta_R^{(2)},\ldots
\]

Diese Koeffizienten sind jedoch asymptotische Koeffizienten **einer einzigen skalaren Beobachtung**

\[
\boxed{
\ell_T(F)
:=
\langle\mathcal X_{R,T}F,\zeta_T\rangle.
}
\tag{C1zB2C6d.8}
\]

Für jedes feste `T` besitzt diese Beobachtung targetseitig Rang höchstens eins:

\[
F
\longmapsto
P_{\zeta_T}\mathcal X_{R,T}F.
\]

Daraus folgt ein wichtiger Scope-Schutz.

## Satz C1zB2C6d.1 — asymptotische Koeffizienten sind keine neuen Probes

Die Kenntnis beliebig vieler Koeffizienten der `1/T`-Entwicklung von `\ell_T(F)` erzeugt für ein festes Terminal `T` keine zusätzlichen linear unabhängigen Richtungen in `\mathscr H_T`.

Insbesondere darf aus

\[
\ell_T(F)
\sim
\sum_{m\ge0}a_m(T)\beta_R^{(m)}(F)
\]

nicht auf die Existenz von targetseitigen Probes

\[
\psi_{T,0},\psi_{T,1},\ldots
\]

mit entsprechendem Rang geschlossen werden.

Status:

\[
\boxed{\checkmark[M]_{\rm corr,C4\text{-}jets\neq multi\text{-}probes}.}
\]

### Konsequenz

Die C4-Jet-Hierarchie ist eine **Source-Hierarchie** innerhalb einer einzigen terminalen Observation.

Eine echte Multi-Probe-Theorie muss zusätzliche Vektoren in `\mathscr H_T` aus der Kolligation konstruieren.

---

# 2. Kanonischer gescreenter Huboperator im Response-Raum

Die vorhandenen Operatoren liefern einen natürlichen positiven terminalen Operator

\[
\boxed{
\mathfrak S_T
:=
A_T^{-1/2}H_T^*H_TA_T^{-1/2}
:
\mathscr H_T\to\mathscr H_T.
}
\tag{C1zB2C6d.9}
\]

Da

\[
\mathfrak S_T
=
(H_TA_T^{-1/2})^*(H_TA_T^{-1/2}),
\]

ist

\[
\boxed{
\mathfrak S_T\ge0.
}
\tag{C1zB2C6d.10}
\]

Für jedes feste `T` ist `\mathfrak S_T` beschränkt.

Diese Konstruktion benutzt ausschließlich bereits vorhandene P11-Daten:

- `H_T`;
- `R_T` über `A_T=I+R_T^*R_T`;
- positive Funktionalkalkülbildung `A_T^{-1/2}`.

Es wird keine neue Norm, kein externer Basisraum und keine Kompaktheitsannahme eingeführt.

---

# 3. Hauptsatz I — kanonischer Screened-Response-Krylov-Flag

Definiere die rohen Response-Probes

\[
\boxed{
\psi_{T,j}^{\rm raw}
:=
\mathfrak S_T^j\zeta_T,
\qquad j\ge0.
}
\tag{C1zB2C6d.11}
\]

Dann ist

\[
\psi_{T,0}^{\rm raw}=\zeta_T,
\]

also reproduziert die erste Probe exakt C4.

Für `N\ge0` setze

\[
\boxed{
\mathscr K_{T,N}^{\rm resp}
:=
\operatorname{span}
\{\zeta_T,\mathfrak S_T\zeta_T,\ldots,\mathfrak S_T^N\zeta_T\}.
}
\tag{C1zB2C6d.12}
\]

Dies ist ein vollständig kanonischer endlicher Krylov-Raum der konkreten Feshbach-Kolligation.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,screened\text{-}response\text{-}Krylov}.}
\]

### Firewall

C6d behauptet noch nicht

\[
\dim\mathscr K_{T,N}^{\rm resp}=N+1.
\]

Ein Krylov-Breakdown ist möglich und muss P11-spezifisch ausgeschlossen werden.

---

# 4. Hankel-Momentmatrix und exakter Rangtest

Definiere die Momente

\[
\boxed{
\mu_{T,k}
:=
\langle\zeta_T,\mathfrak S_T^k\zeta_T\rangle,
\qquad k\ge0.
}
\tag{C1zB2C6d.13}
\]

Da `\mathfrak S_T` selbstadjungiert ist,

\[
\begin{aligned}
\langle
\psi_{T,i}^{\rm raw},
\psi_{T,j}^{\rm raw}
\rangle
&=
\langle
\mathfrak S_T^i\zeta_T,
\mathfrak S_T^j\zeta_T
\rangle\\
&=
\langle
\zeta_T,
\mathfrak S_T^{i+j}\zeta_T
\rangle\\
&=
\mu_{T,i+j}.
\end{aligned}
\]

Die Gram-Matrix der ersten `N+1` rohen Probes ist daher die Hankelmatrix

\[
\boxed{
\mathbf K_{T}^{(N)}
:=
(\mu_{T,i+j})_{0\le i,j\le N}.
}
\tag{C1zB2C6d.14}
\]

Sie ist positiv semidefinit.

## Satz C1zB2C6d.2 — Krylov-Rangtest

Es gilt exakt

\[
\boxed{
\dim\mathscr K_{T,N}^{\rm resp}=N+1
\iff
\mathbf K_T^{(N)}>0
\iff
\det\mathbf K_T^{(N)}>0.
}
\tag{C1zB2C6d.15}
\]

### Beweis

`\mathbf K_T^{(N)}` ist die Gram-Matrix der Vektoren

\[
\psi_{T,0}^{\rm raw},\ldots,\psi_{T,N}^{\rm raw}.
\]

Eine endliche Gram-Matrix ist genau dann positiv definit, wenn die zugrunde liegenden Vektoren linear unabhängig sind. `□`

Status:

\[
\boxed{\checkmark[M]_{\rm pos,Hankel\text{-}rank\text{-}criterion}.}
\]

Dies verwandelt die abstrakte Frage „existieren höhere Probes?“ in einen konkreten P11-Test von endlich vielen terminalen Momenten.

---

# 5. Exakte Orthogonalisierung ohne Vollständigkeitsannahme

Angenommen für ein festes `N` gilt

\[
\mathbf K_T^{(N)}>0.
\]

Sei

\[
\mathbf K_T^{(N)}
=
L_T^{(N)}(L_T^{(N)})^*
\]

die eindeutige Cholesky-Zerlegung mit unterer Dreiecksmatrix und positiver Diagonale.

Definiere den rohen Syntheseoperator

\[
\Psi_T^{(N)}:
\mathbb C^{N+1}\to\mathscr H_T,
\qquad
\Psi_T^{(N)}e_j
=
\psi_{T,j}^{\rm raw}.
\]

Dann setze

\[
\boxed{
\widehat\Psi_T^{(N)}
:=
\Psi_T^{(N)}
\bigl((L_T^{(N)})^*\bigr)^{-1}.
}
\tag{C1zB2C6d.16}
\]

Es gilt

\[
(\widehat\Psi_T^{(N)})^*\widehat\Psi_T^{(N)}
=I_{N+1}.
\tag{C1zB2C6d.17}
\]

Die Spalten

\[
\widehat\psi_{T,0},\ldots,\widehat\psi_{T,N}
\]

sind daher exakt orthonormal.

Weil `((L_T^{(N)})^*)^{-1}` obere Dreiecksgestalt besitzt, liegt die `j`-te orthogonalisierte Probe im Flag

\[
\operatorname{span}
\{\zeta_T,\mathfrak S_T\zeta_T,\ldots,\mathfrak S_T^j\zeta_T\}.
\]

Dies ist die finite Cholesky-/Lanczos-Form der kanonischen Multi-Probe-Konstruktion.

### Antwort auf die Orthogonalitätsfrage

Falls kein Krylov-Breakdown eintritt, können die höheren Probes **exakt** orthogonal zu allen Vorgängern gewählt werden, nicht nur asymptotisch in `T`.

Aber diese Orthogonalität ist eine Hilbertgeometrie-Aussage im Response-Raum. Sie sagt noch nichts darüber, welchen Boundary-Jet jede Probe detektiert.

---

# 6. Die zweite Probe: vollständig expliziter Nichtdegenerationsdefekt

Der erste rohe höhere Krylov-Vektor ist

\[
\mathfrak S_T\zeta_T
=
A_T^{-1/2}H_T^*H_T\mathbf1_T.
\tag{C1zB2C6d.18}
\]

Die ersten drei Momente besitzen daher explizite Formen.

Zunächst

\[
\boxed{
\mu_{T,0}
=
\|\zeta_T\|^2
=
\langle\mathbf1_T,A_T\mathbf1_T\rangle
=
2T+\|R_T\mathbf1_T\|^2.
}
\tag{C1zB2C6d.19}
\]

Ferner

\[
\begin{aligned}
\mu_{T,1}
&=
\langle
A_T^{1/2}\mathbf1_T,
A_T^{-1/2}H_T^*H_T\mathbf1_T
\rangle\\
&=
\langle\mathbf1_T,H_T^*H_T\mathbf1_T\rangle\\
&=
\boxed{\|H_T\mathbf1_T\|^2.}
\end{aligned}
\tag{C1zB2C6d.20}
\]

Und

\[
\boxed{
\mu_{T,2}
=
\langle
H_T^*H_T\mathbf1_T,
A_T^{-1}H_T^*H_T\mathbf1_T
\rangle.
}
\tag{C1zB2C6d.21}
\]

Die `2x2`-Hankeldeterminante lautet

\[
\det\mathbf K_T^{(1)}
=
\mu_{T,0}\mu_{T,2}-\mu_{T,1}^2.
\]

Definiere

\[
\boxed{
\Delta_T^{(1)}
:=
\mu_{T,2}
-
\frac{\mu_{T,1}^2}{\mu_{T,0}}.
}
\tag{C1zB2C6d.22}
\]

Also explizit

\[
\boxed{
\Delta_T^{(1)}
=
\langle H_T^*H_T\mathbf1_T,
A_T^{-1}H_T^*H_T\mathbf1_T\rangle
-
\frac{\|H_T\mathbf1_T\|^4}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}.
}
\tag{C1zB2C6d.23}
\]

Durch Cauchy-Schwarz in der `A_T`-Geometrie gilt

\[
\boxed{\Delta_T^{(1)}\ge0.}
\tag{C1zB2C6d.24}
\]

Der erste orthogonale Residualvektor kann als

\[
\boxed{
r_{T,1}^{\rm probe}
:=
\mathfrak S_T\zeta_T
-
\frac{\mu_{T,1}}{\mu_{T,0}}\zeta_T
}
\tag{C1zB2C6d.25}
\]

geschrieben werden.

Er erfüllt

\[
\langle r_{T,1}^{\rm probe},\zeta_T\rangle=0
\]

und

\[
\boxed{
\|r_{T,1}^{\rm probe}\|^2
=
\Delta_T^{(1)}.
}
\tag{C1zB2C6d.26}
\]

## Satz C1zB2C6d.3 — exakter Zweitprobe-Test

Es existiert genau dann eine nichttriviale zweite Krylov-Probe, wenn

\[
\boxed{
\Delta_T^{(1)}>0.
}
\tag{C1zB2C6d.27}
\]

Äquivalent:

\[
\boxed{
H_T^*H_T\mathbf1_T
\notin
\mathbb C\,A_T\mathbf1_T.
}
\tag{C1zB2C6d.28}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm pos,second\text{-}probe\text{-}defect}.}
\]

### Wichtige Firewall

Die bisherigen Knoten beweisen **noch nicht** eine uniforme oder auch nur eventuale Untergrenze

\[
\Delta_T^{(1)}\ge c_T>0.
\]

Insbesondere wird nicht behauptet, dass der zweite Krylov-Vektor für alle großen `T` nichtverschwindet.

---

# 7. Multi-Probe-Response-Matrix

Fixiere nun `R`, `N` und nehme an, dass

\[
\mathbf K_T^{(N)}>0.
\]

Die orthonormalen Probes aus §5 definieren die Analyseabbildung

\[
U_{T,N}^*:
\mathscr H_T\to\mathbb C^{N+1},
\]

wobei

\[
U_{T,N}e_j=\widehat\psi_{T,j}.
\]

Auf dem kanonischen Jetfenster

\[
E_{R,N}
=
\operatorname{span}\{e_{R,0},\ldots,e_{R,N}\}
\]

definiere

\[
\boxed{
\mathcal P_T^{(N)}
:=
U_{T,N}^*
\mathcal X_{R,T}|_{E_{R,N}}.
}
\tag{C1zB2C6d.29}
\]

In den kanonischen Basen lautet dies

\[
\boxed{
(\mathcal P_T^{(N)})_{j,m}
=
\langle
\xi_{R,m}^{(T)},
\widehat\psi_{T,j}
\rangle.
}
\tag{C1zB2C6d.30}
\]

Dies ist die echte finite Multi-Probe-Matrix, die C6c gesucht hatte.

### C4 ist nur die erste rohe Zeile

Vor der Krylov-Orthogonalisierung ist `j=0` exakt

\[
\langle\xi_{R,m}^{(T)},\zeta_T\rangle
=
\langle J_{R,T}f_{R,m},H_T\mathbf1_T\rangle,
\]

mit

\[
f_{R,m}:=\mathfrak B_R^{-1}e_{R,m}.
\]

Da `e_{R,m}` im `m`-ten Jetlayer liegt,

\[
\beta_R^{(0)}(f_{R,m})
=
\cdots
=
\beta_R^{(m-1)}(f_{R,m})
=0,
\]

aber

\[
\beta_R^{(m)}(f_{R,m})>0
\]

nach der Phasenfixierung von C6a.

C4 liefert daher für jedes feste `m`

\[
\boxed{
\langle\xi_{R,m}^{(T)},\zeta_T\rangle
=
-\sqrt2\,c_m\beta_R^{(m)}(f_{R,m})
\frac{e^{T/2}}{T^{m+1/2}}
\bigl(1+O_{R,m}(T^{-1})\bigr).
}
\tag{C1zB2C6d.31}
\]

Damit isoliert die erste Probe die Jetlagen bereits durch verschiedene asymptotische Skalen, aber sie liefert targetseitig weiterhin nur eine Zeile.

---

# 8. Hauptsatz II — exakte Probe-/Transversal-Zerlegung der Response-Grammatrix

Setze

\[
X_{T,N}
:=
\mathcal X_{R,T}|_{E_{R,N}}
:
E_{R,N}\to\mathscr H_T.
\]

Sei

\[
\Pi_{T,N}
:=
U_{T,N}U_{T,N}^*
\]

die orthogonale Projektion auf den Multi-Probe-Raum

\[
\operatorname{Ran}U_{T,N}
=
\mathscr K_{T,N}^{\rm resp}.
\]

Dann gilt exakt

\[
\begin{aligned}
X_{T,N}^*X_{T,N}
&=
X_{T,N}^*\Pi_{T,N}X_{T,N}
+
X_{T,N}^*(I-\Pi_{T,N})X_{T,N}\\
&=
(\mathcal P_T^{(N)})^*\mathcal P_T^{(N)}
+
\mathcal R_{T,N}^{\rm trans},
\end{aligned}
\]

mit

\[
\boxed{
\mathcal R_{T,N}^{\rm trans}
:=
X_{T,N}^*(I-\Pi_{T,N})X_{T,N}
\ge0.
}
\tag{C1zB2C6d.32}
\]

Also

\[
\boxed{
X_{T,N}^*X_{T,N}
=
(\mathcal P_T^{(N)})^*\mathcal P_T^{(N)}
+
\mathcal R_{T,N}^{\rm trans}.
}
\tag{C1zB2C6d.33}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm pos,multi\text{-}probe\text{-}Gram\text{-}decomposition}.}
\]

### Konsequenz: finite-window Lower-Bound-Kriterium

Da

\[
\mathcal R_{T,N}^{\rm trans}\ge0,
\]

gilt

\[
\boxed{
X_{T,N}^*X_{T,N}
\ge
(\mathcal P_T^{(N)})^*\mathcal P_T^{(N)}.
}
\tag{C1zB2C6d.34}
\]

Somit

\[
\boxed{
\lambda_{\min}(X_{T,N}^*X_{T,N})
\ge
s_{\min}(\mathcal P_T^{(N)})^2.
}
\tag{C1zB2C6d.35}
\]

Wenn also P11-spezifisch gezeigt werden könnte, dass

\[
s_{\min}(\mathcal P_T^{(N)})\to\infty
\]

für jedes feste `N`, dann wäre die in C6c fehlende **uniforme finite-window Response-Coercivity** bewiesen.

Dies ist ein echtes zweiseitiges Verbesserungspotential gegenüber der C4-Rang-eins-Untergrenze.

**Aber:** C6d beweist diese Singularwertasymptotik noch nicht.

---

# 9. Whitened Probe-Observability-Defekt

Die Probe-Matrix kontrolliert nur die Projektion der Response auf

\[
\mathscr K_{T,N}^{\rm resp}.
\]

Um zu messen, ob sie asymptotisch die gesamte Response des festen Jetfensters erfasst, definiere mit

\[
C_{R,T}^{(N)}
:=
P_{R,N}M_{R,T}P_{R,N}|_{E_{R,N}}>0
\]

den dimensionslosen Defekt

\[
\boxed{
\varepsilon_T^{\rm probe}(R,N)
:=
\left\|
(I-\Pi_{T,N})
X_{T,N}
(C_{R,T}^{(N)})^{-1/2}
\right\|.
}
\tag{C1zB2C6d.36}
\]

Dann

\[
\boxed{
\left\|
(C_{R,T}^{(N)})^{-1/2}
\mathcal R_{T,N}^{\rm trans}
(C_{R,T}^{(N)})^{-1/2}
\right\|
=
\bigl(\varepsilon_T^{\rm probe}(R,N)\bigr)^2.
}
\tag{C1zB2C6d.37}
\]

Damit würde

\[
\varepsilon_T^{\rm probe}(R,N)\to0
\]

bedeuten, dass der kanonische Krylov-Probe-Frame die gescreente Response des festen Jetfensters nach natürlichem Whitening asymptotisch vollständig beobachtet.

### Firewall

Auch

\[
\varepsilon_T^{\rm probe}(R,N)\to0
\]

ist **nicht** identisch mit dem C6c-Jet-Tail

\[
\tau_T(E_{R,N})\to0.
\]

Der Probe-Defekt lebt im terminalen Response-Raum `\mathscr H_T`; `\tau` misst dagegen den Off-Window-Block von `M_{R,T}^{1/2}` im Profilraum. Eine Brücke zwischen beiden wäre ein neuer Satz über die Blockstruktur der vollen Feshbach-Metrik.

---

# 10. No-Go — Krylov-Rang folgt nicht aus Positivität oder Feshbach-Form allein

Der Operator

\[
\mathfrak S_T\ge0
\]

und der Startvektor

\[
\zeta_T
\]

sind kanonisch.

Daraus folgt aber nicht, dass `\zeta_T` zyklisch oder auch nur zweistufig nichtdegeneriert ist.

Wenn beispielsweise

\[
\mathfrak S_T\zeta_T
=
\lambda_T\zeta_T,
\]

dann gilt für jedes `j`

\[
\mathfrak S_T^j\zeta_T
=
\lambda_T^j\zeta_T
\]

und somit

\[
\dim\mathscr K_{T,N}^{\rm resp}=1
\]

für alle `N`.

Die abstrakte Positivität von `\mathfrak S_T` verhindert diesen Fall nicht.

Die bisherigen P11-Knoten enthalten keine Schätzung, die

\[
\Delta_T^{(1)}>0
\]

für alle hinreichend großen `T` beweist, geschweige denn

\[
\det\mathbf K_T^{(N)}>0
\]

für beliebiges festes `N`.

Status:

\[
\boxed{\checkmark[M]_{\rm neg,Krylov\text{-}rank\text{-}unproved}.}
\]

**Scope:** Dies ist kein No-Go gegen den konkreten P11-Krylov-Frame. Es ist die Aussage, dass sein Rang ein neuer P11-spezifischer analytischer Test ist und nicht aus allgemeiner Operatorgeometrie folgt.

---

# 11. No-Go — Orthogonalität der Probes erzwingt keine Jet-Triangularität

Selbst wenn

\[
\widehat\psi_{T,0},\ldots,\widehat\psi_{T,N}
\]

exakt orthonormal sind, folgt daraus keinerlei Nullstruktur für

\[
(\mathcal P_T^{(N)})_{j,m}
=
\langle\xi_{R,m}^{(T)},\widehat\psi_{T,j}\rangle.
\]

Tatsächlich sei in einem beliebigen Hilbertraum ein orthonormales System

\[
\psi_0,\ldots,\psi_N
\]

gegeben. Für jede beliebige komplexe Matrix

\[
B=(b_{j,m})_{0\le j,m\le N}
\]

kann man Vektoren

\[
\xi_m
:=
\sum_{j=0}^{N}b_{j,m}\psi_j
\]

wählen. Dann ist

\[
\langle\xi_m,\psi_j\rangle=b_{j,m}.
\]

Also kann die Probe-Matrix trotz exakter Probe-Orthogonalität beliebig dicht besetzt sein.

Damit:

\[
\boxed{
\text{Probe-Orthogonalität}
\not\Rightarrow
\text{Jet-Triangularität der Response-Matrix}.
}
\tag{C1zB2C6d.38}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm neg,orthogonality\not\Rightarrow jet\text{-}alignment}.}
\]

### Konsequenz

Die vom Nutzer vorgeschlagene Idee „höhere Randmoden orthogonal zu `\zeta_T`“ ist als **Konstruktion** realisierbar; die Orthogonalität kann via Krylov-Cholesky sogar exakt gemacht werden.

Was zusätzlich bewiesen werden muss, ist die **Jet-Ausrichtung**:

\[
\boxed{
\text{Welche Jetlagen werden von welcher orthogonalen Probe in welcher }T\text{-Skala gesehen?}
}
\tag{C1zB2C6d.39}
\]

Das ist eine neue Feshbach-/Boundary-Asymptotik, keine Folge der Orthogonalisierung.

---

# 12. Alternative `A_T`-Krylov-Probes und der primitive Kollaps

Es gibt eine zweite, noch direkter auf C3 bezogene kanonische Kandidatenfamilie.

Definiere im Source-Raum

\[
\phi_{T,j}:=A_T^j\mathbf1_T
\]

und im Response-Raum

\[
\boxed{
\chi_{T,j}:=A_T^{1/2}\phi_{T,j}
=A_T^{j+1/2}\mathbf1_T.
}
\tag{C1zB2C6d.40}
\]

Dann gilt exakt

\[
\boxed{
\langle\mathcal X_{R,T}F,\chi_{T,j}\rangle
=
\langle J_{R,T}f,H_TA_T^j\mathbf1_T\rangle.
}
\tag{C1zB2C6d.41}
\]

Diese Familie hat den Vorteil einer sehr transparenten Source-Darstellung.

Nun betrachte jedoch nur den primitiven konditionierten Rest

\[
R_T^{(1)}.
\]

C3 beweist exakt

\[
R_T^{(1)}\mathbf1_T=0.
\]

Setze

\[
A_T^{(1)}
:=
I+(R_T^{(1)})^*R_T^{(1)}.
\]

Dann

\[
A_T^{(1)}\mathbf1_T
=
\mathbf1_T
\]

und folglich für alle `j\ge0`

\[
\boxed{
(A_T^{(1)})^j\mathbf1_T
=
\mathbf1_T.
}
\tag{C1zB2C6d.42}
\]

Der primitive `A_T`-Krylov-Raum ist daher exakt rang eins.

## Satz C1zB2C6d.4 — primitive Screening-Krylov-Kollaps

Im nur-primitiven konditionierten Restmodell erzeugt der `A_T`-Krylov-Ansatz **keine** zweite Probe.

Jede zusätzliche Richtung des vollen `A_T`-Krylov-Flags muss aus den höheren Prime-Power-Restkanälen `k\ge2` stammen.

Status:

\[
\boxed{\checkmark[M]_{\rm neg,primitive\text{-}screening\text{-}Krylov\text{-}collapse}.}
\]

### Strukturelle Bedeutung

Dies ist bemerkenswert, weil C4s führende Boundary-Jet-Asymptotik gerade vom **primitiven Hub** stammt; höhere Prime-Powers im Hub sind dort exponentiell kleiner.

Damit gibt es im naiven `A_T`-Krylov-Ansatz eine Quellenasymmetrie:

- die zu trennenden Boundary-Jets werden führend vom primitiven Hub erzeugt;
- zusätzliche Screening-Krylov-Richtungen entstehen erst durch höhere Prime-Power-Restdaten.

Das beweist keinen No-Go gegen den vollen `A_T`-Krylov-Ansatz. Es zeigt aber, dass eine jet-adaptierte Multi-Probe-Struktur daraus **nicht automatisch** folgt.

Aus diesem Grund ist der gescreente Hub-Krylov-Operator `\mathfrak S_T` aus §2 der strukturell passendere Kandidat für C6d/C6e.

---

# 13. Was ein positiver Multi-Probe-Satz tatsächlich beweisen müsste

Für jedes feste `N` wären drei getrennte Schritte nötig.

## Schritt A — kein Krylov-Breakdown

Zeige für hinreichend große `T`

\[
\boxed{
\det\mathbf K_T^{(N)}>0.
}
\tag{C1zB2C6d.43}
\]

Bereits für `N=1` ist dies äquivalent zu

\[
\Delta_T^{(1)}>0.
\]

## Schritt B — quantitative Jet-Ausrichtung

Zeige eine explizite asymptotische Struktur der Matrix

\[
\mathcal P_T^{(N)}.
\]

Eine mögliche, derzeit **nicht bewiesene** Form wäre eine nach kanonischen `T`-Skalen renormierte Dreiecksgrenze mit nichtverschwindender Diagonale.

Entscheidend ist nicht das Wort „triangulär“, sondern eine quantitative Untergrenze

\[
\boxed{
s_{\min}(\mathcal P_T^{(N)})
\ge a_{R,N}(T)>0}
\tag{C1zB2C6d.44}
\]

mit kontrollierter asymptotischer Größe.

## Schritt C — transversale Response kontrollieren

Zeige zusätzlich, falls für den weiteren Tail-Schritt benötigt,

\[
\boxed{
\varepsilon_T^{\rm probe}(R,N)\to0.
}
\tag{C1zB2C6d.45}
\]

Erst dann wäre der endliche Krylov-Frame asymptotisch ein vollständiges Feshbach-Observability-System für das feste Jetfenster.

### Firewall

Keine dieser drei Aussagen folgt aus Kompaktheit oder Schattenklassenzugehörigkeit. Sie müssen aus expliziten terminalen Momenten beziehungsweise Boundary-/Prime-Power-Asymptotiken hergeleitet werden.

---

# 14. Was C6d bereits gegenüber C6c verbessert

C6c formulierte abstrakt den Wunsch nach `N+1` terminalen Probes.

C6d ersetzt diese unspezifizierte Forderung durch einen konkreten kanonischen Kandidaten:

\[
\boxed{
\zeta_T,
\mathfrak S_T\zeta_T,
\ldots,
\mathfrak S_T^N\zeta_T,
\qquad
\mathfrak S_T=A_T^{-1/2}H_T^*H_TA_T^{-1/2}.
}
\tag{C1zB2C6d.46}
\]

Außerdem wird die Frage „gibt es genügend Probes?“ auf die endlichen Determinanten

\[
\boxed{
\det(\mu_{T,i+j})_{0\le i,j\le N}
}
\tag{C1zB2C6d.47}
\]

reduziert.

Und die Frage „reichen sie zur Response-Kontrolle?“ wird auf

\[
s_{\min}(\mathcal P_T^{(N)})
\]

und

\[
\varepsilon_T^{\rm probe}(R,N)
\]

reduziert.

Dies ist ein echter Fortschritt in der Typisierung: Die bisher abstrakten „höheren Randmoden“ sind nun durch konkrete P11-Operatorausdrücke ersetzt.

---

# 15. No-Go-Persistenzmatrix

| Früherer Knoten | Gesiegelter Befund | Wirkung in C6d |
|---|---|---|
| C1y | translationsinvariante Regulatoren lösen den Hub/Rest-Konflikt im C1y-Scope nicht | unverändert; `\mathfrak S_T` lebt auf source-windowed Terminalräumen |
| B2-A | kein endlicher Schattenklassenabschluss durch Gamma-Präkonditionierung | unverändert; keine Kompaktheits-/Schattenroute |
| B2-B | naiver Haar-`L^2`-Grenzendpunkt reicht nicht | unverändert |
| C4 | unendliche Jet-Hierarchie; kein fixer endlicher Jet reicht global | unverändert; `N` bleibt fest und fensterabhängig |
| C5/C6a | totale Odd-Divergenz | unverändert |
| C6 | kein voller Transport durch festen endlichen Jetquotienten | unverändert |
| C6a | kanonische Jet-ONB und trianguläre native Transitionen | direkte Domain-Struktur der Probe-Matrix; keine analytische Rate importiert |
| C6a | Selbst-Grams allein reichen nicht | unverändert |
| C6b | C2-Flachheit allein reicht nicht | unverändert |
| C6c | `tau=>kappa` auf festen Fenstern | unverändert; C6d löst `tau` noch nicht |
| C6c | Triangularität allein reicht nicht | unverändert; deshalb wird Jet-Ausrichtung der **Response-Probes** separat verlangt |
| C6c | C4 ist nur rank-one Response-Information | präzisiert: C4-Jetkoeffizienten sind nicht zusätzliche targetseitige Probes |
| C5e | gerader Gamma-Gauge konvergiert stark | nur Vergleich; kein Import in Odd |

---

# 16. Was C6d supersediert — und was ausdrücklich nicht

C6d supersediert ausschließlich die unscharfe Hoffnung

\[
\text{„Die höheren C4-Boundary-Jets liefern automatisch höhere terminale Randprobes.“}
\]

Korrekt ist

\[
\boxed{
\text{C4 liefert viele Source-Koeffizienten einer einzigen targetseitigen Probe.}
}
\tag{C1zB2C6d.48}
\]

Als konkrete neue Probe-Kandidaten treten stattdessen die Krylov-Vektoren des gescreenten Huboperators `\mathfrak S_T` auf.

Nicht supersediert werden:

- C4s Jet-Hierarchie;
- C6a-Triangularität;
- C6b/C6c-Tail-/Cross-Frame-Kriterien;
- C6c `tau=>kappa`;
- sämtliche älteren No-Gos.

Insbesondere wird **kein** Multi-Probe-Rang oder Odd-Gauge-Grenzwert behauptet.

---

# 17. Exakter nächster Arbeitsauftrag C6e

C6d zeigt, dass der minimalste nächste Test nicht sofort bei beliebigem `N` beginnen sollte.

Der atomare erste Fall ist

\[
\boxed{N=1.}
\]

Zu untersuchen ist der explizite Defekt

\[
\boxed{
\Delta_T^{(1)}
=
\langle H_T^*H_T\mathbf1_T,
A_T^{-1}H_T^*H_T\mathbf1_T\rangle
-
\frac{\|H_T\mathbf1_T\|^4}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}.
}
\tag{C1zB2C6d.49}
\]

Die Fragen sind in dieser Reihenfolge:

1. Gilt für alle hinreichend großen `T`
   \[
   \Delta_T^{(1)}>0\ ?
   \]
   Damit wäre die Existenz einer echten zweiten Feshbach-Probe bewiesen.
2. Gibt es eine quantitative Untergrenze für `\Delta_T^{(1)}` relativ zu den natürlichen C3/C4-Skalen?
3. Für die normierte zweite Probe
   \[
   \widehat\psi_{T,1}
   =
   r_{T,1}^{\rm probe}/\sqrt{\Delta_T^{(1)}}
   \]
   welche Asymptotik besitzt
   \[
   \langle\xi_{R,m}^{(T)},\widehat\psi_{T,1}\rangle
   \]
   für `m=0,1`?
4. Entsteht zusammen mit der C4-Probe eine `2x2`-Response-Matrix mit kontrollierter kleinster Singularzahl?

Ein positiver `N=1`-Satz wäre der erste echte Beleg, dass die Feshbach-Kolligation selbst mehr als den C4-Rang-eins-Kanal sichtbar macht.

Ein negativer Satz

\[
\Delta_T^{(1)}=0
\]

oder eine asymptotische Degeneration wäre ebenso wertvoll: Dann wäre die naheliegendste kanonische Multi-Probe-Route geschlossen und C6 müsste zu direkten Off-Diagonal-Schätzungen zurückkehren.

**Firewall für C6e:** Keine Behauptung höherer Krylov-Ränge, bevor bereits der `N=1`-Defekt kontrolliert ist.

---

# 18. Endurteil

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6d]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm corr,C4\text{-}jets\neq multi\text{-}probes}
+
\checkmark[M]_{\rm pos,screened\text{-}response\text{-}Krylov}
+
\checkmark[M]_{\rm pos,Hankel\text{-}rank\text{-}criterion}
+
\checkmark[M]_{\rm pos,second\text{-}probe\text{-}defect}
+
\checkmark[M]_{\rm pos,multi\text{-}probe\text{-}Gram\text{-}decomposition}
+
\checkmark[M]_{\rm neg,Krylov\text{-}rank\text{-}unproved}
+
\checkmark[M]_{\rm neg,orthogonality\not\Rightarrow jet\text{-}alignment}
+
\checkmark[M]_{\rm neg,primitive\text{-}screening\text{-}Krylov\text{-}collapse}
}
\]

Der wesentliche Fortschritt ist, dass „höhere Randprobes“ nicht mehr als informelle Hoffnung im Raum stehen. Es gibt jetzt einen konkreten, vollständig aus der P11-Feshbach-Kolligation gebauten Kandidaten und einen exakten endlichen Rangtest.

Der erste wirklich neue analytische Engpass ist dadurch auf eine einzelne skalare Größe reduziert:

\[
\boxed{\Delta_T^{(1)}.}
\]

Er entscheidet, ob die konkrete Kolligation überhaupt eine zweite kanonische, zur C4-Konstantenprobe orthogonale Response-Richtung erzeugt.