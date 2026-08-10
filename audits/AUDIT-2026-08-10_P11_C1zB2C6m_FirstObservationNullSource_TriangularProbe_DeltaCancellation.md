# P11-C1z-B2-C6m — Exakter First-Observation-Nullvektor, trianguläre Probe-Matrix und Δ-Kürzung

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6m]`  
**Direkte Voraussetzungen:** C1z-B2-C4, C1z-B2-C6d, C1z-B2-C6j, C1z-B2-C6k, C1z-B2-C6l  
**Strukturelle Schnittstellen:** C1z-B2-C3, C1z-B2-C6a, C1z-B2-C6b, C1z-B2-C6c, C1z-B2-C6e, C1z-B2-C6f, C1z-B2-C6g, C1z-B2-C6h, C1z-B2-C6i  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d `orthogonality != jet alignment`, C1z-B2-C6k `current data != Wronskian nonzero`, C1z-B2-C6l `C4 constant-mode mechanism does not transfer`  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6m]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm corr,Delta\text{-}lower\text{-}bound\not\Rightarrow y\text{-}smallness}
+
\checkmark[M]_{\rm neg,A\text{-}orthogonality\not\Rightarrow bulk\text{-}cancellation}
+
\checkmark[M]_{\rm pos,exact\text{-}first\text{-}observation\text{-}null\text{-}source}
+
\checkmark[M]_{\rm pos,exact\text{-}source\text{-}column\text{-}triangularization}
+
\checkmark[M]_{\rm pos,Delta\text{-}cancellation\text{-}in\text{-}determinant}
+
\checkmark[M]_{\rm pos,canonical\text{-}second\text{-}alignment\text{-}scalar}
+
\checkmark[M]_{\rm pos,residual\text{-}A\text{-}Cauchy\text{-}Schwarz}
+
\checkmark[M]_{\rm neg,C4\text{-}rank\text{-}one\text{-}lower\text{-}bound\text{-}vanishes\text{-}on\text{-}g_T}
+
?[O]_{\rm second\text{-}alignment\text{-}scalar\neq0}
+
?[O]_{\rm residual\text{-}bulk\text{-}asymptotic}
+
?[O]_{\rm quantitative\text{-}s_{min}}
}
\]

C6m untersucht die in C6l offene Frage, ob die Orthogonalität

\[
\langle y_T,A_T\mathbf1_T\rangle=0
\]

eine versteckte Cancellation im Bulkterm von `H_Ty_T` erzeugt.

Die Antwort ist in dieser Form **negativ**: Die `A_T`-Orthogonalität liefert weder einen C4-artigen Bulk-Kollaps noch derzeit eine quantitative Kleinheit des gewöhnlichen Mittelwerts von `y_T`.

Gleichzeitig ergibt sich aber eine stärkere und sauberere Reduktion, die die punktweise Bulkfrage zunächst umgeht.

Setze

\[
\boxed{
c_{R,T}:=\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}}
\tag{C1zB2C6m.1}
\]

und definiere den terminal-adaptierten Sourcevektor

\[
\boxed{
g_{R,T}:=f_{R,1}-c_{R,T}f_{R,0}.}
\tag{C1zB2C6m.2}
\]

Dann gilt **exakt**

\[
\boxed{
\langle J_{R,T}g_{R,T},H_T\mathbf1_T\rangle=0.
}
\tag{C1zB2C6m.3}
\]

Der zweite Alignment-Defekt aus C6l ist genau

\[
\boxed{
\mathfrak E_{R,T}^{\perp}
=
\langle J_{R,T}g_{R,T},H_Ty_T\rangle.
}
\tag{C1zB2C6m.4}
\]

Auf Response-Ebene ist

\[
\boxed{
\xi_{R,g_T}^{(T)}
:=
A_T^{-1/2}H_T^*J_{R,T}g_{R,T}
}
\tag{C1zB2C6m.5}
\]

exakt orthogonal zur ersten Probe `zeta_T`.

Da aus C6l

\[
A_T^{1/2}y_T
=
\sqrt{\Delta_T^{(1)}}\,\widehat\psi_{T,1},
\]

folgt

\[
\boxed{
\mathfrak E_{R,T}^{\perp}
=
\sqrt{\Delta_T^{(1)}}
\left\langle
\xi_{R,g_T}^{(T)},
\widehat\psi_{T,1}
\right\rangle.
}
\tag{C1zB2C6m.6}
\]

Setzt man dies in C6ks Determinantenformel ein, kürzt sich `Delta_T^(1)` vollständig heraus:

\[
\boxed{
\det\mathcal P_T^{(1)}
=
\frac{\ell_{R,0}(T)}{\sqrt{\mu_{T,0}}}
\left\langle
\xi_{R,g_T}^{(T)},
\widehat\psi_{T,1}
\right\rangle.
}
\tag{C1zB2C6m.7}
\]

Dies ist die kanonische trianguläre Form der ersten echten `2x2`-Alignmentfrage.

Eventual ist der erste Faktor nach C4 ungleich null. Daher gilt exakt:

\[
\boxed{
\mathcal P_T^{(1)}\text{ invertierbar}
\iff
\left\langle
\xi_{R,g_T}^{(T)},
\widehat\psi_{T,1}
\right\rangle\ne0.
}
\tag{C1zB2C6m.8}
\]

Der neue atomare Invariant ist somit nicht mehr ein Wronskian mit vier Skalaren und auch nicht mehr ein unnormalisierter Residualdefekt, sondern eine einzige normierte Target-Paarung:

\[
\boxed{
a_{R,T}^{(2)}
:=
\left\langle
\xi_{R,g_T}^{(T)},
\widehat\psi_{T,1}
\right\rangle.
}
\tag{C1zB2C6m.9}
\]

C6m beweist **nicht**, dass `a_{R,T}^{(2)}` eventual ungleich null ist. Es isoliert aber exakt den einzigen noch fehlenden Skalar für die qualitative `2x2`-Invertibilität.

---

# 0. Reconciliation: zwei Korrekturen vor dem Hauptargument

## 0.1 Eine untere `Delta`-Schranke macht `y_T` nicht klein

C6l beweist exakt

\[
\boxed{
\langle y_T,A_Ty_T\rangle
=\Delta_T^{(1)}.
}
\tag{C1zB2C6m.10}
\]

und damit

\[
\|y_T\|^2\le\Delta_T^{(1)},
\qquad
\|R_Ty_T\|^2\le\Delta_T^{(1)}.
\]

C6j liefert jedoch nur die **untere** Schranke

\[
\Delta_T^{(1)}\ge c e^{-5T}.
\]

Daraus folgt keinerlei obere Schranke für `||y_T||` oder `||R_Ty_T||`.

Insbesondere ist der Schluss

\[
\Delta_T^{(1)}\gtrsim e^{-5T}
\Rightarrow
\|y_T\|\text{ klein}
\]

logisch falsch.

Für Kleinheit von `y_T` bräuchte man eine **obere** Schranke für `Delta_T^(1)`.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,Delta\text{-}lower\text{-}bound\not\Rightarrow y\text{-}smallness}.
}
\]

## 0.2 `A_T`-Orthogonalität ist keine Mittelwert- oder Bulk-Cancellation

C6l liefert

\[
\boxed{
\langle y_T,A_T\mathbf1_T\rangle=0.
}
\tag{C1zB2C6m.11}
\]

Da

\[
A_T=I+R_T^*R_T,
\]

ist dies äquivalent zu

\[
\boxed{
\langle y_T,\mathbf1_T\rangle
=-\langle R_Ty_T,R_T\mathbf1_T\rangle.
}
\tag{C1zB2C6m.12}
\]

Cauchy-Schwarz ergibt

\[
\boxed{
|\langle y_T,\mathbf1_T\rangle|
\le
\|R_Ty_T\|\,\|R_T\mathbf1_T\|
\le
\sqrt{\Delta_T^{(1)}}\,\|R_T\mathbf1_T\|.
}
\tag{C1zB2C6m.13}
\]

C3 beweist

\[
\|R_T\mathbf1_T\|^2=O(T^2),
\]

also

\[
|\langle y_T,\mathbf1_T\rangle|
\le O(T)\sqrt{\Delta_T^{(1)}}.
\tag{C1zB2C6m.14}
\]

Ohne obere `Delta`-Kontrolle folgt daraus derzeit **keine** quantitative Kleinheit des Mittelwerts.

Noch wichtiger: Selbst die stärkere hypothetische Aussage

\[
\langle y_T,\mathbf1_T\rangle=0
\]

würde C6ls Bulkterm

\[
\mathcal B_T[y_T](x)
=
\sum_{n\le e^{2(T-x)}}
\alpha_n
\bigl[y_T(x+s_n)-y_T(x-s_n)\bigr]
\]

nicht annihilieren.

Der Hub annihiliert **Konstantenfunktionen** durch zentrierte Differenzen. Mittelwertfreiheit ist eine globale Integralaussage und erzwingt keine punktweisen Translationsdifferenzen.

Daher gilt mit den vorhandenen Daten:

\[
\boxed{
\langle y_T,A_T\mathbf1_T\rangle=0
\not\Rightarrow
\mathcal B_T[y_T]=0
}
\tag{C1zB2C6m.15}
\]

und auch keine asymptotische Kleinheit des Bulkterms folgt allein daraus.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,A\text{-}orthogonality\not\Rightarrow bulk\text{-}cancellation}.
}
\]

---

# 1. Verbindliche Daten aus C6k/C6l

Fixiere `R>0`.

Für die ersten beiden kanonischen Jetvektoren setze

\[
f_{R,m}:=\mathfrak B_R^{-1}e_{R,m},
\qquad m=0,1.
\]

Der Response-Operator ist

\[
\mathcal X_{R,T}
=A_T^{-1/2}H_T^*J_{R,T}\mathfrak B_R^{-1}.
\]

Also

\[
\xi_{R,m}^{(T)}
=A_T^{-1/2}H_T^*J_{R,T}f_{R,m}.
\tag{C1zB2C6m.16}
\]

Die erste Probe ist

\[
\widehat\psi_{T,0}
=\frac{\zeta_T}{\sqrt{\mu_{T,0}}},
\qquad
\zeta_T=A_T^{1/2}\mathbf1_T.
\]

Die erste Observation lautet

\[
\ell_{R,m}(T)
=\langle\xi_{R,m}^{(T)},\zeta_T\rangle
=\langle J_{R,T}f_{R,m},H_T\mathbf1_T\rangle.
\tag{C1zB2C6m.17}
\]

C4/C6k geben

\[
\ell_{R,0}(T)
\sim
-C_{R,0}\frac{e^{T/2}}{T^{1/2}},
\]

\[
\ell_{R,1}(T)
\sim
-C_{R,1}\frac{e^{T/2}}{T^{3/2}},
\]

mit `C_R,0,C_R,1>0`, also

\[
\boxed{
\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}
=
\frac{\kappa_R}{T}
\left(1+O_R(T^{-1})\right),
\qquad\kappa_R>0.
}
\tag{C1zB2C6m.18}
\]

Insbesondere ist `ell_R,0(T)` für großes `T` ungleich null.

C6l definiert

\[
y_T=A_T^{-1}(h_T-\lambda_TA_T\mathbf1_T)
\]

und

\[
\eta_{R,m}(T)
=\langle J_{R,T}f_{R,m},H_Ty_T\rangle.
\tag{C1zB2C6m.19}
\]

Ferner

\[
\eta_{R,m}(T)
=
\sqrt{\Delta_T^{(1)}}
\langle\xi_{R,m}^{(T)},\widehat\psi_{T,1}\rangle.
\tag{C1zB2C6m.20}
\]

Der C6l-Residualdefekt ist

\[
\mathfrak E_{R,T}^{\perp}
=
\eta_{R,1}(T)
-
\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}\eta_{R,0}(T).
\tag{C1zB2C6m.21}
\]

---

# 2. Exakter First-Observation-Nullvektor

Definiere für großes `T`

\[
\boxed{
c_{R,T}
:=
\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}
}
\tag{C1zB2C6m.22}
\]

und

\[
\boxed{
g_{R,T}
:=
f_{R,1}-c_{R,T}f_{R,0}.
}
\tag{C1zB2C6m.23}
\]

Dann folgt durch Linearität exakt

\[
\begin{aligned}
\langle J_{R,T}g_{R,T},H_T\mathbf1_T\rangle
&=
\ell_{R,1}(T)
-c_{R,T}\ell_{R,0}(T)\\
&=0.
\end{aligned}
\]

Also

\[
\boxed{
\ell_{R,g_T}(T)=0.
}
\tag{C1zB2C6m.24}
\]

Da `c_R,T=O_R(1/T)`, gilt auf dem festen Source-Level zugleich

\[
\boxed{
g_{R,T}\to f_{R,1}}
\tag{C1zB2C6m.25}
\]

in jeder festen Norm, in der `f_R,0,f_R,1` liegen.

Dies ist bemerkenswert: `g_R,T` konvergiert source-seitig gegen den zweiten Jetvektor, ist aber für jedes große `T` **exakt unsichtbar für die erste terminale C4-Observation**.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,exact\text{-}first\text{-}observation\text{-}null\text{-}source}.
}
\]

### Jetinterpretation

Der Nullvektor ist `T`-abhängig. Er ist deshalb nicht identisch mit einem festen Quotienten durch den ersten Jet.

C4s Expansion zeigt vielmehr, dass die kleine Beimischung

\[
-c_{R,T}f_{R,0}=O_R(T^{-1})f_{R,0}
\]

gerade die terminale erste Observation von `f_R,1` kompensiert.

Dies ist eine horizonadaptive Source-Orthogonalisierung gegen die erste terminale Probe, keine neue feste Jetbasis.

---

# 3. Response-Nullstellung gegen die erste Probe

Definiere

\[
\boxed{
\xi_{R,g_T}^{(T)}
:=
A_T^{-1/2}H_T^*J_{R,T}g_{R,T}.
}
\tag{C1zB2C6m.26}
\]

Dann gilt nach (C1zB2C6m.24)

\[
\boxed{
\langle\xi_{R,g_T}^{(T)},\zeta_T\rangle=0.
}
\tag{C1zB2C6m.27}
\]

Äquivalent:

\[
\boxed{
\langle\xi_{R,g_T}^{(T)},\widehat\psi_{T,0}\rangle=0.
}
\tag{C1zB2C6m.28}
\]

Damit liegt `xi_R,g_T^(T)` exakt im Orthogonalkomplement der ersten Krylov-Probe.

C6ls zweite Probe erfüllt ebenfalls

\[
\widehat\psi_{T,1}\perp\widehat\psi_{T,0}.
\]

Wichtig ist die Firewall:

\[
\boxed{
\xi_{R,g_T}^{(T)},\widehat\psi_{T,1}\in\widehat\psi_{T,0}^{\perp}
\not\Rightarrow
\langle\xi_{R,g_T}^{(T)},\widehat\psi_{T,1}\rangle\ne0.
}
\tag{C1zB2C6m.29}
\]

Das Orthogonalkomplement ist im Allgemeinen hochdimensional.

Die frühere C6d-Firewall `orthogonality != jet alignment` bleibt damit vollständig aktiv, jetzt aber in einer exakt auf den ersten Probe-Nullraum reduzierten Form.

---

# 4. Der C6l-Residualdefekt ist eine einzige Response-Paarung

Aus Definition von `g_R,T` und `eta_R,m`:

\[
\begin{aligned}
\langle J_{R,T}g_{R,T},H_Ty_T\rangle
&=
\eta_{R,1}(T)-c_{R,T}\eta_{R,0}(T)\\
&=
\mathfrak E_{R,T}^{\perp}.
\end{aligned}
\]

Somit

\[
\boxed{
\mathfrak E_{R,T}^{\perp}
=
\langle J_{R,T}g_{R,T},H_Ty_T\rangle.
}
\tag{C1zB2C6m.30}
\]

Mit

\[
\xi_{R,g_T}^{(T)}
=A_T^{-1/2}H_T^*J_{R,T}g_{R,T}
\]

und C6ls

\[
A_T^{1/2}y_T
=
\sqrt{\Delta_T^{(1)}}\widehat\psi_{T,1}
\]

folgt exakt

\[
\begin{aligned}
\mathfrak E_{R,T}^{\perp}
&=
\langle H_T^*J_{R,T}g_{R,T},y_T\rangle\\
&=
\langle A_T^{-1/2}H_T^*J_{R,T}g_{R,T},A_T^{1/2}y_T\rangle\\
&=
\boxed{
\sqrt{\Delta_T^{(1)}}
\langle\xi_{R,g_T}^{(T)},\widehat\psi_{T,1}\rangle.
}
\end{aligned}
\tag{C1zB2C6m.31}
\]

Definiere daher

\[
\boxed{
a_{R,T}^{(2)}
:=
\langle\xi_{R,g_T}^{(T)},\widehat\psi_{T,1}\rangle.
}
\tag{C1zB2C6m.32}
\]

Dann

\[
\boxed{
\mathfrak E_{R,T}^{\perp}
=
\sqrt{\Delta_T^{(1)}}\,a_{R,T}^{(2)}.
}
\tag{C1zB2C6m.33}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,canonical\text{-}second\text{-}alignment\text{-}scalar}.
}
\]

---

# 5. Exakte trianguläre Form der `2x2`-Probe-Matrix

Die ursprüngliche C6d/C6k-Probe-Matrix in den Source-Spalten `(f_R,0,f_R,1)` lautet

\[
\mathcal P_T^{(1)}
=
\begin{pmatrix}
\ell_{R,0}/\sqrt{\mu_{T,0}}
&
\ell_{R,1}/\sqrt{\mu_{T,0}}
\\[1mm]
\eta_{R,0}/\sqrt{\Delta_T^{(1)}}
&
\eta_{R,1}/\sqrt{\Delta_T^{(1)}}
\end{pmatrix}.
\tag{C1zB2C6m.34}
\]

Hier wurde C6ls Kürzung

\[
\nu_{R,m}-\lambda_T\ell_{R,m}=\eta_{R,m}
\]

bereits eingesetzt.

Führe nun auf der Source-Seite die Spaltenoperation

\[
(f_{R,0},f_{R,1})
\mapsto
(f_{R,0},g_{R,T})
\]

durch.

Die zugehörige `2x2`-Transformationsmatrix besitzt Determinante `1`. Daher ändert sich der Determinant der Probe-Matrix nicht.

In der neuen Source-Basis erhält man exakt

\[
\boxed{
\widetilde{\mathcal P}_T^{(1)}
=
\begin{pmatrix}
\ell_{R,0}/\sqrt{\mu_{T,0}}
&0
\\[1mm]
\eta_{R,0}/\sqrt{\Delta_T^{(1)}}
&a_{R,T}^{(2)}
\end{pmatrix}.
}
\tag{C1zB2C6m.35}
\]

Denn der zweite Eintrag der ersten Zeile ist exakt null und

\[
\frac{\eta_{R,1}-c_{R,T}\eta_{R,0}}{\sqrt{\Delta_T^{(1)}}}
=a_{R,T}^{(2)}.
\]

Dies ist eine exakte trianguläre Probe-Matrix.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,exact\text{-}source\text{-}column\text{-}triangularization}.
}
\]

---

# 6. `Delta_T^(1)` kürzt sich aus dem Determinanten vollständig heraus

Aus der triangulären Matrix folgt sofort

\[
\boxed{
\det\mathcal P_T^{(1)}
=
\frac{\ell_{R,0}(T)}{\sqrt{\mu_{T,0}}}
a_{R,T}^{(2)}.
}
\tag{C1zB2C6m.36}
\]

Dies ist äquivalent zur C6k/C6l-Formel, aber konzeptuell schärfer.

Die Größe

\[
\Delta_T^{(1)}
\]

ist für die **Existenz und Normierung** der zweiten Krylov-Probe notwendig. Sobald C6e-C6j eventual `Delta_T^(1)>0` sichern, tritt `Delta_T^(1)` in der qualitativen Determinantenfrage jedoch nicht mehr separat auf.

Damit wird C6ks quantitative Firewall präzisiert:

- Eine `Delta`-Untergrenze liefert für sich keinen Determinanten-Lower-Bound.
- Aber nach Übergang zur normierten zweiten Probe ist auch keine separate `Delta`-Obergrenze nötig, wenn man `a_R,T^(2)` direkt kontrolliert.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,Delta\text{-}cancellation\text{-}in\text{-}determinant}.
}
\]

### Qualitatives Alignment-Kriterium

C4 liefert eventual

\[
\ell_{R,0}(T)\ne0,
\qquad
\mu_{T,0}>0.
\]

Daher:

\[
\boxed{
\mathcal P_T^{(1)}\text{ invertierbar}
\iff
a_{R,T}^{(2)}\ne0.
}
\tag{C1zB2C6m.37}
\]

Dies ist der bisher kleinste exakte Alignment-Invariant des C6-Strangs.

---

# 7. Größe des ersten Diagonaleintrags

C4 liefert

\[
|\ell_{R,0}(T)|
\asymp_R
\frac{e^{T/2}}{\sqrt T}.
\tag{C1zB2C6m.38}
\]

C3 liefert

\[
2T\le\mu_{T,0}\le C T^2.
\tag{C1zB2C6m.39}
\]

Daraus folgt

\[
\boxed{
 c_R\frac{e^{T/2}}{T^{3/2}}
\le
\left|
\frac{\ell_{R,0}(T)}{\sqrt{\mu_{T,0}}}
\right|
\le
C_R\frac{e^{T/2}}{T}.
}
\tag{C1zB2C6m.40}
\]

Der erste diagonale Probe-Kanal degeneriert also nicht; er wächst sogar exponentiell.

Damit ist für die **qualitative** Invertibilität wirklich nur noch `a_R,T^(2)` offen.

Für eine quantitative Untergrenze von

\[
s_{\min}(\mathcal P_T^{(1)})
\]

reicht ein Lower-Bound für `|a_R,T^(2)|` allein jedoch noch nicht, weil der untere linke Eintrag

\[
\eta_{R,0}/\sqrt{\Delta_T^{(1)}}
\]

beziehungsweise die Gesamtmatrixnorm ebenfalls kontrolliert werden muss.

Die frühere `s_min`-Firewall bleibt daher bestehen.

---

# 8. Exakter `A_T`-Cauchy-Schwarz-Bound für den neuen Defekt

Aus

\[
\mathfrak E_{R,T}^{\perp}
=
\langle H_T^*J_{R,T}g_{R,T},y_T\rangle
\]

folgt in der `A_T`-Geometrie

\[
\begin{aligned}
|\mathfrak E_{R,T}^{\perp}|
&=
\left|
\left\langle
A_T^{-1/2}H_T^*J_{R,T}g_{R,T},
A_T^{1/2}y_T
\right\rangle
\right|\\
&\le
\|\xi_{R,g_T}^{(T)}\|
\sqrt{\Delta_T^{(1)}}.
\end{aligned}
\]

Also

\[
\boxed{
|a_{R,T}^{(2)}|
\le
\|\xi_{R,g_T}^{(T)}\|.
}
\tag{C1zB2C6m.41}
\]

Und

\[
\boxed{
\|\xi_{R,g_T}^{(T)}\|^2
=
\left\langle
H_T^*J_{R,T}g_{R,T},
A_T^{-1}H_T^*J_{R,T}g_{R,T}
\right\rangle
=
\sigma_T(J_{R,T}g_{R,T}).
}
\tag{C1zB2C6m.42}
\]

Damit

\[
\boxed{
|\mathfrak E_{R,T}^{\perp}|^2
\le
\Delta_T^{(1)}\,
\sigma_T(J_{R,T}g_{R,T}).
}
\tag{C1zB2C6m.43}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,residual\text{-}A\text{-}Cauchy\text{-}Schwarz}.
}
\]

Diese Schranke ist korrekt und nutzt die natürliche Feshbach-Geometrie. Sie ist aber nur eine **obere** Schranke und beweist kein Alignment.

---

# 9. Warum C4 auf `g_R,T` absichtlich stumm ist

Die C3/C4-Variationsuntergrenze lautet für einen Sourcevektor `f`

\[
\sigma_T(J_{R,T}f)
\ge
\frac{
|\langle J_{R,T}f,H_T\mathbf1_T\rangle|^2
}{
\langle\mathbf1_T,A_T\mathbf1_T\rangle
}.
\tag{C1zB2C6m.44}
\]

Für den neuen Vektor `g_R,T` ist der Zähler nach Konstruktion exakt null:

\[
\langle J_{R,T}g_{R,T},H_T\mathbf1_T\rangle=0.
\]

Daher liefert genau der alte C4-Rang-eins-Test nur

\[
\boxed{
\sigma_T(J_{R,T}g_{R,T})\ge0,
}
\tag{C1zB2C6m.45}
\]

also keine positive Information.

Dies ist kein Defekt der Konstruktion, sondern genau ihr Zweck: `g_R,T` lebt im exakten Nullraum der ersten terminalen Observation.

Folglich kann der zweite Alignment-Schritt **nicht** erneut mit derselben Konstantenmode `1_T` bewiesen werden.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,C4\text{-}rank\text{-}one\text{-}lower\text{-}bound\text{-}vanishes\text{-}on\text{-}g_T}.
}
\]

---

# 10. Geometrische Bedeutung: Observability im ersten Probe-Komplement

Da

\[
\xi_{R,g_T}^{(T)}\perp\widehat\psi_{T,0}
\]

und

\[
\widehat\psi_{T,1}\perp\widehat\psi_{T,0},
\]

kann man innerhalb des ersten Probe-Komplements orthogonal zerlegen:

\[
\boxed{
\xi_{R,g_T}^{(T)}
=
a_{R,T}^{(2)}\widehat\psi_{T,1}
+
\xi_{R,g_T}^{\rm trans,(T)},
}
\tag{C1zB2C6m.46}
\]

mit

\[
\xi_{R,g_T}^{\rm trans,(T)}
\perp
\operatorname{span}\{\widehat\psi_{T,0},\widehat\psi_{T,1}\}.
\]

Daher

\[
\boxed{
\sigma_T(J_{R,T}g_{R,T})
=
|a_{R,T}^{(2)}|^2
+
\|\xi_{R,g_T}^{\rm trans,(T)}\|^2.
}
\tag{C1zB2C6m.47}
\]

Dies macht die C6d-Observability-Firewall exakt sichtbar:

Selbst eine große Feshbach-Response-Energie

\[
\sigma_T(Jg_{R,T})
\]

erzwingt nicht

\[
a_{R,T}^{(2)}\ne0,
\]

weil die gesamte Response transversal zum zweidimensionalen Krylov-Probe-Raum liegen könnte.

Der offene Punkt ist daher kein bloßer Response-Normbound, sondern eine echte **Richtungs-/Observability-Aussage**.

---

# 11. Reconciliation mit C6k und C6l

## C6k

C6k führte den Response-Wronskian

\[
\mathcal W_{R,T}
=
\ell_{R,0}\nu_{R,1}
-
\ell_{R,1}\nu_{R,0}
\]

ein und zeigte

\[
\det\mathcal P_T^{(1)}
=
\frac{\mathcal W_{R,T}}
{\sqrt{\mu_{T,0}\Delta_T^{(1)}}}.
\]

## C6l

C6l kürzte den gesamten C4-Anteil und erhielt

\[
\mathcal W_{R,T}
=
\ell_{R,0}\eta_{R,1}
-
\ell_{R,1}\eta_{R,0}
=
\ell_{R,0}\mathfrak E_{R,T}^{\perp}.
\]

## C6m

C6m identifiziert

\[
\mathfrak E_{R,T}^{\perp}
=
\sqrt{\Delta_T^{(1)}}a_{R,T}^{(2)}.
\]

Daher

\[
\boxed{
\mathcal W_{R,T}
=
\ell_{R,0}(T)
\sqrt{\Delta_T^{(1)}}
a_{R,T}^{(2)}
}
\tag{C1zB2C6m.48}
\]

und

\[
\boxed{
\det\mathcal P_T^{(1)}
=
\frac{\ell_{R,0}(T)}{\sqrt{\mu_{T,0}}}
a_{R,T}^{(2)}.
}
\tag{C1zB2C6m.49}
\]

Die Kette ist damit vollständig konsistent.

---

# 12. No-Go-Persistenzmatrix

| Früherer Knoten | Gesiegelter Befund | Wirkung in C6m |
|---|---|---|
| C1y | translationsinvariante Regulatoren lösen den Hub/Rest-Konflikt im C1y-Scope nicht | unverändert |
| B2-A | Gamma-Präkonditionierung liefert keinen finite Schattenmechanismus | unverändert |
| B2-B | naiver Haar-`L^2`-Endpunkt reicht nicht | unverändert |
| C4 | unendliche Boundary-Jet-Hierarchie; kein endlicher Jet stabilisiert Rohterminalmetrik | unverändert |
| C6 | kein voller Odd-Transport durch festen endlichen Jetquotienten | unverändert |
| C6a | Self-Grams allein reichen nicht | unverändert |
| C6b | C2-Flachheit allein reicht nicht | unverändert |
| C6c | Triangularität/total divergence allein reichen nicht | unverändert |
| C6d | Probe-Orthogonalität ist kein Jet-Alignment | bestätigt und auf `g_R,T` zugespitzt |
| C6e-C6j | zweite Krylov-Probe eventual existent, explizite Nichtdegenerationsreserve | vollständig erhalten |
| C6k | Wronskian ist exakter `2x2`-Test; vorhandene Daten erzwingen ihn nicht | in `a_R,T^(2)` umgeschrieben |
| C6l | C4-Konstantenmode-Mechanismus überträgt sich nicht auf `y_T`; Bulk bleibt | unverändert; Mittelwert-Abkürzung zusätzlich ausgeschlossen |

Kein früheres No-Go wird durch C6m aufgehoben.

---

# 13. Was C6m ausdrücklich nicht beweist

Nicht bewiesen sind:

- `a_{R,T}^{(2)} != 0` für alle großen `T`;
- eine asymptotische Formel für `a_{R,T}^{(2)}`;
- ein Lower-Bound für `|a_{R,T}^{(2)}|`;
- ein Lower-Bound für `s_min(P_T^(1))`;
- eine obere Schranke oder asymptotische Klassifikation von `Delta_T^(1)`;
- dass `y_T` in `L^2` klein ist;
- dass `y_T` gewöhnlich mittelwertfrei oder asymptotisch mittelwertfrei ist;
- dass der Bulkterm `B_T[y_T]` klein ist;
- dass der Shellterm den Bulkterm dominiert;
- dass `sigma_T(Jg_R,T)` die zweite Probe-Richtung kontrolliert;
- `tau_T(E_R,1) -> 0`;
- `Theta_T,U^(E_R,1) -> I`;
- Krylov-Rang `N>=2`.

Insbesondere bleibt logisch möglich

\[
\boxed{
a_{R,T}^{(2)}=0}
\]

für einzelne oder sogar unendlich viele große Horizonte, solange keine zusätzliche P11-spezifische Observability-Struktur bewiesen wird.

---

# 14. Exakter nächster Arbeitsauftrag C6n

Nach C6m ist die qualitative `2x2`-Alignmentfrage auf einen einzigen Skalar reduziert:

\[
\boxed{
a_{R,T}^{(2)}
=
\langle\xi_{R,g_T}^{(T)},\widehat\psi_{T,1}\rangle.}
\]

Der nächste Knoten sollte deshalb **nicht** erneut die volle Probe-Matrix, den Wronskian oder `Delta_T^(1)` untersuchen.

Er sollte direkt die Response des First-Observation-Nullvektors analysieren.

Arbeitsauftrag:

1. Nutze
   \[
   g_{R,T}=f_{R,1}-c_{R,T}f_{R,0},
   \qquad c_{R,T}=\kappa_R/T+O_R(T^{-2}),
   \]
   und die exakte Nullbedingung
   \[
   \langle Jg_{R,T},H_T\mathbf1_T\rangle=0.
   \]
2. Schreibe
   \[
   \xi_{R,g_T}^{(T)}
   =A_T^{-1/2}H_T^*Jg_{R,T}
   \]
   in einer Form, die die Projektion auf
   \[
   \widehat\psi_{T,1}
   \]
   direkt sichtbar macht.
3. Prüfe zuerst, ob die spezielle Sourcekombination `g_R,T` zusammen mit der expliziten Residualgleichung
   \[
   A_Ty_T=h_T-\lambda_TA_T\mathbf1_T
   \]
   eine bilineare Identität oder Vorzeichenstruktur für
   \[
   \langle H_T^*Jg_{R,T},y_T\rangle
   \]
   erzeugt.
4. Falls keine exakte Identität existiert, zerlege **diese skalare Paarung** in prime-pure und Cross-Prime Beiträge; nicht die gesamte Funktion `H_Ty_T`.
5. Ein positiver Satz muss eventual
   \[
   a_{R,T}^{(2)}\ne0
   \]
   oder quantitativ
   \[
   |a_{R,T}^{(2)}|\ge\delta_{R,T}>0
   \]
   beweisen.
6. Falls die vorhandene Operatorstruktur selbst auf dieser reduzierten Ebene kein Vorzeichen/Nichtverschwinden erzwingt, ist ein weiterer präziser Observability-No-Go zu siegeln.

### Firewall für C6n

Weder

\[
\xi_{R,g_T}^{(T)}\perp\widehat\psi_{T,0}
\]

noch

\[
\widehat\psi_{T,1}\perp\widehat\psi_{T,0}
\]

noch

\[
\sigma_T(Jg_{R,T})>0
\]

reichen für

\[
a_{R,T}^{(2)}\ne0.
\]

Der nächste positive Schritt muss eine echte P11-spezifische Richtungsinformation liefern.

---

# 15. Endurteil

C6m entscheidet die in C6l vorgeschlagene versteckte Bulk-Cancellation über `A_T`-Orthogonalität negativ und ersetzt sie durch eine deutlich stärkere geometrische Reduktion.

Die `T`-abhängige Sourcekombination

\[
\boxed{
g_{R,T}
=f_{R,1}
-
\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}f_{R,0}}
\]

liegt exakt im Nullraum der ersten terminalen C4-Observation:

\[
\boxed{
\langle Jg_{R,T},H_T\mathbf1_T\rangle=0.}
\]

Nach Feshbach-Whitening gilt

\[
\boxed{
\xi_{R,g_T}^{(T)}\perp\widehat\psi_{T,0}.}
\]

Der gesamte zweite Alignment-Invariant ist dann die eine Paarung

\[
\boxed{
a_{R,T}^{(2)}
=
\langle\xi_{R,g_T}^{(T)},\widehat\psi_{T,1}\rangle.}
\]

Und die Probe-Matrix wird durch eine determinantenerhaltende Source-Spaltenoperation exakt triangularisiert:

\[
\boxed{
\widetilde{\mathcal P}_T^{(1)}
=
\begin{pmatrix}
\ell_{R,0}/\sqrt{\mu_{T,0}}&0\\
\eta_{R,0}/\sqrt{\Delta_T^{(1)}}&a_{R,T}^{(2)}
\end{pmatrix}.}
\]

Daher

\[
\boxed{
\det\mathcal P_T^{(1)}
=
\frac{\ell_{R,0}}{\sqrt{\mu_{T,0}}}
a_{R,T}^{(2)}.}
\]

`Delta_T^(1)` kürzt sich vollständig aus der Determinantenformel heraus.

Damit ist nach C6m die erste `2x2`-Jetfrage maximal reduziert:

\[
\boxed{
\text{Sieht die zweite normierte Krylov-Probe die Response des exakt first-observation-nullten Sourcevektors }g_{R,T}?}
\]

Genau diese eine Observability-Frage bleibt für C6n offen.