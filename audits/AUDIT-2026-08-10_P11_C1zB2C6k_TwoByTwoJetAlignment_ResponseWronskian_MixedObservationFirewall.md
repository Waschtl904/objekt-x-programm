# P11-C1z-B2-C6k — 2×2-Jet-Alignment, Response-Wronskian und Mixed-Observation-Firewall

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6k]`  
**Direkte Voraussetzungen:** C1z-B2-C4, C1z-B2-C6a, C1z-B2-C6d, C1z-B2-C6e, C1z-B2-C6j  
**Strukturelle Schnittstellen:** C1z-B, C1z-B2-C3, C1z-B2-C6b, C1z-B2-C6c, C1z-B2-C6f, C1z-B2-C6g, C1z-B2-C6h, C1z-B2-C6i  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d `orthogonality ≠ jet alignment`  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6k]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm corr,single\text{-}(1,1)\text{-}entry\not\Leftrightarrow invertibility}
+
\checkmark[M]_{\rm pos,exact\text{-}second\text{-}row\text{-}formula}
+
\checkmark[M]_{\rm pos,lambda\text{-}cancellation}
+
\checkmark[M]_{\rm pos,response\text{-}Wronskian\text{-}criterion}
+
\checkmark[M]_{\rm pos,C4\text{-}jet\text{-}ratio\text{-}reduction}
+
\checkmark[M]_{\rm neg,current\text{-}data\not\Rightarrow Wronskian\neq0}
+
\checkmark[M]_{\rm corr,Delta\text{-}lower\text{-}bound\not\Rightarrow determinant\text{-}lower\text{-}bound}
+
?[O]_{\rm mixed\text{-}second\text{-}observation\text{-}asymptotic}
+
?[O]_{\rm quantitative\text{-}s_{min}}
+
?[O]_{\rm second\text{-}probe\text{-}jet\text{-}alignment}
}
\]

C6k ist der erste Knoten, der die inzwischen gesicherte zweite Krylov-Probe aus C6e–C6j mit dem kanonischen zweidimensionalen Jetfenster

\[
E_{R,1}=\operatorname{span}\{e_{R,0},e_{R,1}\}
\]

verknüpft.

Das Resultat ist **kein vorschneller Alignment-Satz**, sondern eine exakte Reduktion auf einen einzigen neuen P11-spezifischen gemischten Response-Term.

Die wichtigste neue Formel lautet:

\[
\boxed{
\det\mathcal P_T^{(1)}
=
\frac{
\ell_{R,0}(T)\nu_{R,1}(T)
-
\ell_{R,1}(T)\nu_{R,0}(T)
}
{\sqrt{\mu_{T,0}\Delta_T^{(1)}}}.
}
\tag{C1zB2C6k.1}
\]

Hier sind

\[
\ell_{R,m}(T)
:=
\langle\xi_{R,m}^{(T)},\zeta_T\rangle
\tag{C1zB2C6k.2}
\]

die bereits durch C4 asymptotisch kontrollierten ersten Observationen und

\[
\boxed{
\nu_{R,m}(T)
:=
\langle\xi_{R,m}^{(T)},\mathfrak S_T\zeta_T\rangle
}
\tag{C1zB2C6k.3}
\]

die neuen **zweiten gemischten Feshbach-Observationen**.

Der Rayleighquotient

\[
\lambda_T=\mu_{T,1}/\mu_{T,0}
\]

verschwindet in (C1zB2C6k.1) exakt. Damit ist die in C6h/C6i problematische fehlende `lambda_T`-Asymptotik für die reine 2×2-Invertibilitätsfrage irrelevant.

Definiere den Response-Wronskian

\[
\boxed{
\mathcal W_{R,T}
:=
\ell_{R,0}(T)\nu_{R,1}(T)
-
\ell_{R,1}(T)\nu_{R,0}(T).
}
\tag{C1zB2C6k.4}
\]

Dann gilt eventual wegen C6es `Delta_T^(1)>0` exakt

\[
\boxed{
\mathcal P_T^{(1)}\text{ invertierbar}
\iff
\mathcal W_{R,T}\ne0.
}
\tag{C1zB2C6k.5}
\]

Das ist der korrekte erste Jet-Alignment-Test.

---

# 0. Reconciliation: was C6k wirklich testen muss

## 0.1 Der einzelne `(1,1)`-Eintrag ist kein Invertibilitätskriterium

Die C6d-Probe-Matrix ist

\[
\mathcal P_T^{(1)}
=
\begin{pmatrix}
\langle\xi_{R,0}^{(T)},\widehat\psi_{T,0}\rangle
&
\langle\xi_{R,1}^{(T)},\widehat\psi_{T,0}\rangle
\\[1mm]
\langle\xi_{R,0}^{(T)},\widehat\psi_{T,1}\rangle
&
\langle\xi_{R,1}^{(T)},\widehat\psi_{T,1}\rangle
\end{pmatrix}.
\tag{C1zB2C6k.6}
\]

Die zunächst vorgeschlagene Frage

\[
\langle\xi_{R,1}^{(T)},\widehat\psi_{T,1}\rangle
\stackrel{?}{\not\to}0
\]

ist zwar interessant, aber sie ist weder hinreichend noch notwendig für die Invertierbarkeit von (C1zB2C6k.6).

- Ein nichtverschwindender `(1,1)`-Eintrag kann durch die Off-Diagonalprodukte im Determinanten exakt kompensiert werden.
- Ein verschwindender `(1,1)`-Eintrag ist mit einer invertierbaren Matrix vereinbar, wenn beide Off-Diagonalterme nichtnull sind.

Daher ist das korrekte erste Ziel

\[
\boxed{\det\mathcal P_T^{(1)}\ne0,}
\]

nicht die isolierte Nichtverschwindensaussage eines einzelnen Eintrags.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,single\text{-}(1,1)\text{-}entry\not\Leftrightarrow invertibility}.
}
\]

## 0.2 C6j liefert eine Normierungsreserve, aber noch kein Alignment

C6j beweist

\[
\boxed{
\Delta_T^{(1)}\ge c_\Delta e^{-5T}
}
\tag{C1zB2C6k.7}
\]

für großes `T`.

Damit ist

\[
\|r_{T,1}^{\rm probe}\|
=\sqrt{\Delta_T^{(1)}}
\ge c e^{-5T/2},
\]

also die zweite Probe eventual wohldefiniert und ihre Normierung ist nicht beliebig stärker singulär als `e^{5T/2}`.

Aber eine **untere** Schranke für `Delta` liefert keine untere Schranke für den Determinanten (C1zB2C6k.1), da `sqrt(Delta)` dort im Nenner steht. Für einen quantitativen Determinanten-Lower-Bound aus einem Lower-Bound für `|W|` bräuchte man zusätzlich eine **obere** Schranke für `Delta`.

Und für eine quantitative Schranke

\[
s_{\min}(\mathcal P_T^{(1)})\ge c_T
\]

braucht man darüber hinaus eine obere Kontrolle des größten Singularwerts, etwa über `||P||_F`.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,Delta\text{-}lower\text{-}bound\not\Rightarrow determinant\text{-}lower\text{-}bound}.
}
\]

---

# 1. Verbindliche P11-Daten

Fixiere `R>0` und setze

\[
f_{R,m}:=\mathfrak B_R^{-1}e_{R,m},
\qquad m=0,1.
\tag{C1zB2C6k.8}
\]

Aus C6d:

\[
\boxed{
\mathcal X_{R,T}
=A_T^{-1/2}H_T^*J_{R,T}\mathfrak B_R^{-1},
}
\tag{C1zB2C6k.9}
\]

und

\[
\boxed{
\xi_{R,m}^{(T)}
=A_T^{-1/2}H_T^*J_{R,T}f_{R,m}.
}
\tag{C1zB2C6k.10}
\]

Die erste kanonische Probe ist

\[
\boxed{
\zeta_T=A_T^{1/2}\mathbf1_T.
}
\tag{C1zB2C6k.11}
\]

Der positive gescreente Huboperator ist

\[
\boxed{
\mathfrak S_T
=A_T^{-1/2}H_T^*H_TA_T^{-1/2}.
}
\tag{C1zB2C6k.12}
\]

Setze wie C6d

\[
\mu_{T,k}
=\langle\zeta_T,\mathfrak S_T^k\zeta_T\rangle.
\tag{C1zB2C6k.13}
\]

Dann

\[
\mu_{T,0}=\|\zeta_T\|^2,
\qquad
\lambda_T:=\frac{\mu_{T,1}}{\mu_{T,0}},
\tag{C1zB2C6k.14}
\]

und

\[
\boxed{
\Delta_T^{(1)}
=\mu_{T,2}-\frac{\mu_{T,1}^2}{\mu_{T,0}}.
}
\tag{C1zB2C6k.15}
\]

C6e–C6j liefern eventual

\[
\Delta_T^{(1)}>0.
\]

Damit können die beiden orthonormalen Krylov-Probes geschrieben werden als

\[
\boxed{
\widehat\psi_{T,0}
=\frac{\zeta_T}{\sqrt{\mu_{T,0}}}
}
\tag{C1zB2C6k.16}
\]

und

\[
\boxed{
\widehat\psi_{T,1}
=
\frac{
\mathfrak S_T\zeta_T-\lambda_T\zeta_T
}
{\sqrt{\Delta_T^{(1)}}}.
}
\tag{C1zB2C6k.17}
\]

---

# 2. Zwei Observationen pro Jetvektor

Definiere für `m=0,1`

\[
\boxed{
\ell_{R,m}(T)
:=
\langle\xi_{R,m}^{(T)},\zeta_T\rangle.
}
\tag{C1zB2C6k.18}
\]

Nach C6d/C4 ist

\[
\boxed{
\ell_{R,m}(T)
=
\langle J_{R,T}f_{R,m},H_T\mathbf1_T\rangle.
}
\tag{C1zB2C6k.19}
\]

Die neue zweite Observation ist

\[
\boxed{
\nu_{R,m}(T)
:=
\langle\xi_{R,m}^{(T)},\mathfrak S_T\zeta_T\rangle.
}
\tag{C1zB2C6k.20}
\]

Da

\[
\mathfrak S_T\zeta_T
=A_T^{-1/2}H_T^*H_T\mathbf1_T,
\]

folgt exakt

\[
\begin{aligned}
\nu_{R,m}(T)
&=
\left\langle
A_T^{-1/2}H_T^*J_{R,T}f_{R,m},
A_T^{-1/2}H_T^*H_T\mathbf1_T
\right\rangle
\\
&=
\boxed{
\left\langle
H_T^*J_{R,T}f_{R,m},
A_T^{-1}H_T^*H_T\mathbf1_T
\right\rangle.
}
\end{aligned}
\tag{C1zB2C6k.21}
\]

Äquivalent, durch Verschieben von `H_T^*`,

\[
\boxed{
\nu_{R,m}(T)
=
\left\langle
J_{R,T}f_{R,m},
H_TA_T^{-1}H_T^*H_T\mathbf1_T
\right\rangle.
}
\tag{C1zB2C6k.22}
\]

Definiere daher das terminale gemischte Observationsprofil

\[
\boxed{
\mathfrak G_T
:=
H_TA_T^{-1}H_T^*H_T\mathbf1_T.
}
\tag{C1zB2C6k.23}
\]

Dann ist schlicht

\[
\boxed{
\nu_{R,m}(T)=\langle J_{R,T}f_{R,m},\mathfrak G_T\rangle.
}
\tag{C1zB2C6k.24}
\]

Dies ist der **einzige neue P11-spezifische Funktionsvektor**, den C6k für den 2×2-Test benötigt.

C4 kontrolliert stattdessen das Profil

\[
H_T\mathbf1_T.
\]

Es existiert bisher kein Satz, der `G_T` auf einem festen alten Fenster asymptotisch durch dieselbe Boundary-Jet-Entwicklung beschreibt.

---

# 3. Exakte zweite Zeile der Probe-Matrix

Aus (C1zB2C6k.17) folgt für `m=0,1`

\[
\begin{aligned}
\langle\xi_{R,m}^{(T)},\widehat\psi_{T,1}\rangle
&=
\frac{
\langle\xi_{R,m}^{(T)},\mathfrak S_T\zeta_T\rangle
-
\lambda_T\langle\xi_{R,m}^{(T)},\zeta_T\rangle
}
{\sqrt{\Delta_T^{(1)}}}\\
&=
\boxed{
\frac{
\nu_{R,m}(T)-\lambda_T\ell_{R,m}(T)
}
{\sqrt{\Delta_T^{(1)}}}.
}
\end{aligned}
\tag{C1zB2C6k.25}
\]

Die erste Zeile ist

\[
\boxed{
\langle\xi_{R,m}^{(T)},\widehat\psi_{T,0}\rangle
=
\frac{\ell_{R,m}(T)}{\sqrt{\mu_{T,0}}}.
}
\tag{C1zB2C6k.26}
\]

Somit lautet die komplette 2×2-Matrix exakt

\[
\boxed{
\mathcal P_T^{(1)}
=
\begin{pmatrix}
\ell_0/\sqrt{\mu_0} & \ell_1/\sqrt{\mu_0}
\\[2mm]
(\nu_0-\lambda\ell_0)/\sqrt\Delta
&
(\nu_1-\lambda\ell_1)/\sqrt\Delta
\end{pmatrix},
}
\tag{C1zB2C6k.27}
\]

wobei zur Lesbarkeit die Indizes `(R,T)` unterdrückt wurden.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,exact\text{-}second\text{-}row\text{-}formula}.
}
\]

---

# 4. Hauptsatz I — exakte `lambda_T`-Elimination

Berechne den Determinanten von (C1zB2C6k.27):

\[
\begin{aligned}
\det\mathcal P_T^{(1)}
&=
\frac{
\ell_0(\nu_1-\lambda\ell_1)
-
\ell_1(\nu_0-\lambda\ell_0)
}
{\sqrt{\mu_0\Delta}}\\
&=
\frac{
\ell_0\nu_1
-
\ell_1\nu_0
-
\lambda\ell_0\ell_1
+
\lambda\ell_1\ell_0
}
{\sqrt{\mu_0\Delta}}\\
&=
\boxed{
\frac{
\ell_0\nu_1-\ell_1\nu_0
}
{\sqrt{\mu_0\Delta}}.
}
\end{aligned}
\tag{C1zB2C6k.28}
\]

Der Rayleighquotient `lambda_T` hebt sich **exakt** weg.

Damit ist die in C6h/C6i fehlende Asymptotik von `lambda_T` für die reine 2×2-Invertibilitätsfrage nicht mehr relevant.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,lambda\text{-}cancellation}.
}
\]

---

# 5. Response-Wronskian-Kriterium

Definiere

\[
\boxed{
\mathcal W_{R,T}
:=
\ell_{R,0}(T)\nu_{R,1}(T)
-
\ell_{R,1}(T)\nu_{R,0}(T).
}
\tag{C1zB2C6k.29}
\]

Da

\[
\mu_{T,0}>0
\]

und C6e–C6j eventual

\[
\Delta_T^{(1)}>0
\]

liefern, folgt:

## Satz C1zB2C6k.1 — 2×2-Alignment-Kriterium

Für jedes feste `R>0` und jedes hinreichend große `T` gilt

\[
\boxed{
\det\mathcal P_T^{(1)}\ne0
\iff
\mathcal W_{R,T}\ne0.
}
\tag{C1zB2C6k.30}
\]

Äquivalent sind die beiden Observationsvektoren

\[
\boxed{
(\ell_{R,0},\ell_{R,1})
\quad\text{und}\quad
(\nu_{R,0},\nu_{R,1})
}
\tag{C1zB2C6k.31}
\]

in `C^2` genau dann linear unabhängig, wenn das kanonische 2×2-Jetfenster durch die ersten beiden Krylov-Probes invertibel beobachtet wird.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,response\text{-}Wronskian\text{-}criterion}.
}
\]

### Interpretation

C6e–C6j beweisen, dass der **targetseitige** Krylov-Flag Rang 2 besitzt.

C6k zeigt nun: Für Jet-Alignment braucht man zusätzlich, dass die zweite rohe Observation auf dem **sourceseitigen** Jetfenster nicht bloß proportional zur ersten Observation ist.

Damit wird C6ds abstrakte Firewall

\[
orthogonality\not\Rightarrow jet\text{-}alignment
\]

zu einer einzigen expliziten Determinantenbedingung verschärft.

---

# 6. C4 reduziert den Wronskian auf einen Jet-korrigierten zweiten Defekt

Für

\[
f_{R,0},f_{R,1}
\]

liefert C4/C6d:

\[
\boxed{
\ell_{R,0}(T)
=
-\sqrt2\,c_0\beta_R^{(0)}(f_{R,0})
\frac{e^{T/2}}{T^{1/2}}
\left(1+O_R(T^{-1})\right)
}
\tag{C1zB2C6k.32}
\]

und

\[
\boxed{
\ell_{R,1}(T)
=
-\sqrt2\,c_1\beta_R^{(1)}(f_{R,1})
\frac{e^{T/2}}{T^{3/2}}
\left(1+O_R(T^{-1})\right).
}
\tag{C1zB2C6k.33}
\]

Nach der C6a-Phasenfixierung sind die ersten nichtverschwindenden Jets positiv. Setze

\[
\boxed{
\kappa_R
:=
\frac{
 c_1\beta_R^{(1)}(f_{R,1})
}{
 c_0\beta_R^{(0)}(f_{R,0})
}>0.
}
\tag{C1zB2C6k.34}
\]

Dann gilt eventual `ell_{R,0}(T) != 0` und

\[
\boxed{
\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}
=
\frac{\kappa_R}{T}
\left(1+O_R(T^{-1})\right).
}
\tag{C1zB2C6k.35}
\]

Also

\[
\begin{aligned}
\mathcal W_{R,T}
&=
\ell_{R,0}(T)
\left[
\nu_{R,1}(T)
-
\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}
\nu_{R,0}(T)
\right].
\end{aligned}
\tag{C1zB2C6k.36}
\]

Definiere den exakten **Jet-korrigierten zweiten Observationsdefekt**

\[
\boxed{
\mathfrak D_{R,T}^{(2)}
:=
\nu_{R,1}(T)
-
\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}
\nu_{R,0}(T).
}
\tag{C1zB2C6k.37}
\]

Dann

\[
\boxed{
\mathcal W_{R,T}
=
\ell_{R,0}(T)\mathfrak D_{R,T}^{(2)}.
}
\tag{C1zB2C6k.38}
\]

und daher eventual

\[
\boxed{
\mathcal P_T^{(1)}\text{ invertierbar}
\iff
\mathfrak D_{R,T}^{(2)}\ne0.
}
\tag{C1zB2C6k.39}
\]

Asymptotisch ist

\[
\mathfrak D_{R,T}^{(2)}
=
\nu_{R,1}(T)
-
\frac{\kappa_R}{T}
\left(1+O_R(T^{-1})\right)
\nu_{R,0}(T).
\tag{C1zB2C6k.40}
\]

Damit ist der nächste positive P11-Satz völlig präzise:

> Die zweite gemischte Observation darf auf dem ersten zweidimensionalen Jetfenster nicht dieselbe `1/T`-Proportionalität wie die C4-Konstantenobservation besitzen.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,C4\text{-}jet\text{-}ratio\text{-}reduction}.
}
\]

---

# 7. Warum C6e–C6j den Wronskian noch nicht kontrollieren

Die Kette C6e–C6j liefert starke targetseitige Information:

1. `Delta_T^(1)>0` eventual;
2. einen expliziten Separator gegen `A_T 1_T`;
3. eine explizite Untergrenze
   \[
   \Delta_T^{(1)}\gtrsim e^{-5T};
   \]
4. eine lokale Restenergieanalyse des Separators.

Diese Aussagen kontrollieren die Norm des zweiten Krylov-Residualvektors

\[
r_{T,1}^{\rm probe}
=
\mathfrak S_T\zeta_T-\lambda_T\zeta_T.
\]

Sie sagen aber nicht, wie dieser Vektor relativ zu den beiden konkreten Response-Vektoren

\[
\xi_{R,0}^{(T)},\qquad \xi_{R,1}^{(T)}
\]

liegt.

Der neue Term

\[
\nu_{R,m}
=
\langle\xi_{R,m},\mathfrak S_T\zeta_T\rangle
\]

ist weder durch C4s skalare Konstantenobservation noch durch C6js Separatornorm bestimmt.

Insbesondere folgt aus

\[
\Delta_T^{(1)}>0
\]

nur

\[
\mathfrak S_T\zeta_T\notin\mathbb C\zeta_T,
\]

aber nicht

\[
(\nu_{R,0},\nu_{R,1})
\notin
\mathbb C(\ell_{R,0},\ell_{R,1}).
\]

Diese beiden Nichtkollinearitätsaussagen leben auf verschiedenen Ebenen.

---

# 8. Daten-Firewall: Rang 2 erzwingt keinen 2×2-Jet-Wronskian

C6k kann diese logische Lücke durch ein endliches abstraktes Response-Modell exakt demonstrieren.

## Modell

Sei der targetseitige Hilbertraum

\[
\mathscr H=\mathbb C^3
\]

mit Orthonormalbasis

\[
e_0,e_1,e_2.
\]

Wähle

\[
\zeta=\sqrt{\mu_0}\,e_0
\]

mit `mu_0>0`.

Wähle `lambda>0`, `Delta>0` und einen positiven selbstadjungierten Operator `S`, dessen Wirkung auf `e_0` lautet

\[
S e_0
=
\lambda e_0
+
\sqrt{\frac{\Delta}{\mu_0}}e_1.
\tag{C1zB2C6k.41}
\]

Eine solche positive selbstadjungierte Fortsetzung existiert, etwa indem man auf `span{e_0,e_1}` die Matrix

\[
\begin{pmatrix}
\lambda & d\\
d & M
\end{pmatrix},
\qquad
d=\sqrt{\Delta/\mu_0},
\]

mit `M>d^2/lambda` wählt und auf `e_2` positiv fortsetzt.

Dann

\[
S\zeta
=
\lambda\zeta+\sqrt\Delta\,e_1,
\]

also ist der zweite Krylov-Residualvektor exakt

\[
\sqrt\Delta\,e_1\ne0.
\]

Der targetseitige Krylov-Rang ist damit 2.

Nun seien beliebige nichtverschwindende gewünschte erste Observationen

\[
\ell_0,\ell_1
\]

gegeben. Wähle für ein beliebiges `alpha` zwei Response-Vektoren

\[
\xi_m
=
\frac{\ell_m}{\sqrt{\mu_0}}e_0
+
\alpha\ell_m e_1
+
\gamma_m e_2,
\qquad m=0,1,
\tag{C1zB2C6k.42}
\]

mit frei wählbaren `gamma_0,gamma_1`; insbesondere können die beiden `xi_m` durch passende `gamma_m` linear unabhängig gemacht werden.

Dann

\[
\langle\xi_m,\zeta\rangle=\ell_m
\]

und

\[
\begin{aligned}
\nu_m
:=\langle\xi_m,S\zeta\rangle
&=
\lambda\ell_m
+
\alpha\sqrt\Delta\,\ell_m\\
&=
(\lambda+\alpha\sqrt\Delta)\ell_m.
\end{aligned}
\tag{C1zB2C6k.43}
\]

Somit

\[
\boxed{
\ell_0\nu_1-\ell_1\nu_0=0
}
\tag{C1zB2C6k.44}
\]

obwohl

\[
\Delta>0
\]

und sogar die Response-Vektoren `xi_0,xi_1` unabhängig gewählt werden können.

### Exakter Scope dieses Gegenmodells

Dieses Modell ist **kein Gegenbeispiel zur konkreten P11-Kolligation**. Es behauptet nicht, dass die speziellen Operatoren `H_T,R_T,J_{R,T}` ein solches Verhalten realisieren.

Es beweist ausschließlich den richtigen logischen Satz:

\[
\boxed{
[C4\text{-erste Observationen}]
+
[\Delta_T^{(1)}>0]
+
[\text{targetseitiger Krylov-Rang }2]
\not\Rightarrow
[\mathcal W_{R,T}\ne0]
}
\tag{C1zB2C6k.45}
\]

ohne zusätzliche P11-spezifische Information über die gemischte zweite Observation (C1zB2C6k.21).

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,current\text{-}data\not\Rightarrow Wronskian\neq0}.
}
\]

Dies ist die präzise Fortsetzung von C6ds Firewall

\[
orthogonality\not\Rightarrow jet\text{-}alignment.
\]

---

# 9. Was für einen quantitativen `s_min`-Satz zusätzlich nötig wäre

Für eine 2×2-Matrix gilt

\[
s_{\min}(P)s_{\max}(P)=|\det P|.
\]

Daher beispielsweise

\[
\boxed{
 s_{\min}(P)
\ge
\frac{|\det P|}{\|P\|_F}.
}
\tag{C1zB2C6k.46}
\]

Ein quantitativer P11-Satz müsste also mindestens zwei Arten von Information liefern.

## 9.1 Lower-Bound für den Wronskian

Man braucht eine explizite Folge `w_{R,T}>0` mit

\[
|\mathcal W_{R,T}|\ge w_{R,T}.
\]

## 9.2 Upper-Bounds für die Normalisierung und die Response-Matrix

Wegen

\[
\det\mathcal P_T^{(1)}
=
\frac{\mathcal W_{R,T}}
{\sqrt{\mu_{T,0}\Delta_T^{(1)}}}
\]

braucht ein Determinanten-Lower-Bound insbesondere eine obere Kontrolle von

\[
\mu_{T,0}\Delta_T^{(1)}.
\]

Für `mu_{T,0}` existiert aus C3 eine polynomiale obere Schranke. Für `Delta_T^(1)` besitzt die aktuelle Kette dagegen primär die C6j-**Untergrenze**.

Für `s_min` kommt zusätzlich eine obere Kontrolle der Response-Norm hinzu.

Daher darf aus einem späteren bloßen Nichtverschwindensbeweis

\[
\mathcal W_{R,T}\ne0
\]

noch nicht automatisch

\[
s_{\min}(\mathcal P_T^{(1)})\to\infty
\]

oder auch nur eine uniforme positive Untergrenze gefolgert werden.

---

# 10. No-Go-Persistenzmatrix

| Früherer Knoten | Gesiegelter Befund | Wirkung in C6k |
|---|---|---|
| C1y | translationsinvariante Regulatoren lösen den Hub/Rest-Konflikt im C1y-Scope nicht | unverändert |
| B2-A | Gamma-Präkonditionierung liefert keinen finite Schattenmechanismus | unverändert |
| B2-B | naiver Haar-`L^2`-Endpunkt reicht nicht | unverändert |
| C4 | unendliche Boundary-Jet-Hierarchie | unverändert; C4 liefert nur `ell_m` |
| C6 | kein voller Odd-Transport durch festen endlichen Jetquotienten | unverändert |
| C6a | kanonische Jet-ONB; Self-Grams allein reichen nicht | unverändert |
| C6b | C2-Flachheit allein reicht nicht | unverändert |
| C6c | Triangularität allein reicht nicht | unverändert |
| C6d | C4-Jets sind keine automatischen Multi-Probes | bestätigt |
| C6d | Orthogonalität der Probes erzwingt kein Jet-Alignment | **präzisiert durch `W_{R,T}`** |
| C6e | eventualer Krylov-Rang 2 | vollständig benutzt |
| C6f–C6j | quantitative Nichtdegeneration der zweiten Probe | vollständig benutzt; noch kein Alignment |
| C6j | `Delta_T^(1) >= c e^{-5T}` | Normierungsreserve; kein Determinanten-Lower-Bound |

Kein früheres No-Go wird durch C6k supersediert.

---

# 11. Was C6k ausdrücklich nicht beweist

Nicht bewiesen sind:

- `nu_{R,0}(T)` oder `nu_{R,1}(T)` asymptotisch;
- `mathcal W_{R,T} != 0` eventual;
- `mathfrak D_{R,T}^{(2)} != 0` eventual;
- `det P_T^(1) != 0` eventual;
- eine Untergrenze für `|det P_T^(1)|`;
- eine obere Schranke für `Delta_T^(1)` auf der für Alignment nötigen Skala;
- eine obere Schranke für `||P_T^(1)||` auf der nötigen Skala;
- eine Untergrenze für `s_min(P_T^(1))`;
- `epsilon_T^probe(R,1) -> 0`;
- `tau_T(E_{R,1}) -> 0`;
- `Theta_{T,U}^{E_{R,1}} -> I`;
- Krylov-Rang `N>=2`;
- ein Odd-Gauge-Grenzwert.

Insbesondere bleibt logisch möglich, dass

\[
\boxed{
\Delta_T^{(1)}>0
\quad\text{aber}\quad
\det\mathcal P_T^{(1)}=0
}
\]

für einzelne oder sogar alle großen Horizonte, solange kein P11-spezifischer Satz über `nu_m` vorliegt.

---

# 12. Exakter nächster Arbeitsauftrag C6l

C6k zeigt, dass der nächste Knoten **nicht** erneut die Nichtdegeneration der zweiten Krylov-Probe untersuchen sollte.

Diese ist durch C6e–C6j ausreichend abgesichert.

Der nächste atomare Gegenstand ist

\[
\boxed{
\mathfrak G_T
=
H_TA_T^{-1}H_T^*H_T\mathbf1_T.
}
\tag{C1zB2C6k.47}
\]

und seine beiden festen alten Jetpaarungen

\[
\boxed{
\nu_{R,m}(T)
=
\langle J_{R,T}f_{R,m},\mathfrak G_T\rangle,
\qquad m=0,1.
}
\tag{C1zB2C6k.48}
\]

Der nächste Knoten sollte daher lauten:

\[
\boxed{
\text{C6l: Boundary-Asymptotik der zweiten gemischten Feshbach-Observation.}
}
\tag{C1zB2C6k.49}
\]

Arbeitsauftrag:

1. Schreibe `G_T` in einer Form, die die bekannte Hub-Randstruktur und den Feshbach-Screen `A_T^{-1}` getrennt sichtbar macht.
2. Prüfe, ob auf einem festen alten Fenster `[-R,R]` eine asymptotische Expansion
   \[
   \langle J_{R,T}f,\mathfrak G_T\rangle
   \sim
   \sum_{m\ge0}d_m(T)\beta_R^{(m)}(f)
   \]
   existiert.
3. Entscheide speziell, ob die Koeffizientenfolge `d_m(T)` proportional zur C4-Folge
   \[
   e^{T/2}T^{-m-1/2}c_m
   \]
   ist oder eine neue Jetrichtung erzeugt.
4. Für `m=0,1` genügt zunächst der Defekt
   \[
   \mathfrak D_{R,T}^{(2)}
   =
   \nu_{R,1}
   -
   \frac{\ell_{R,1}}{\ell_{R,0}}\nu_{R,0}.
   \]
5. Falls `mathfrak D != 0` eventual, ist die qualitative 2×2-Invertibilität bewiesen.
6. Erst danach sind obere `Delta`-/Response-Bounds für einen quantitativen `s_min`-Satz sinnvoll.

### Harte Firewall für C6l

Es reicht **nicht**, zu zeigen, dass `G_T` selbst nicht proportional zu `H_T 1_T` ist.

Benötigt wird Nichtproportionalität **nach Projektion auf genau das kanonische Jetfenster**:

\[
(\nu_{R,0},\nu_{R,1})
\notin
\mathbb C(\ell_{R,0},\ell_{R,1}).
\]

Eine globale targetseitige Nichtkollinearität kann nach Restriktion auf zwei Source-Observationen verschwinden.

---

# 13. Endurteil

C6k macht aus der bisher qualitativen Jet-Alignment-Firewall eine einzelne explizite P11-Gleichung.

Die normierte zweite Krylov-Probe erfüllt

\[
\langle\xi_{R,m}^{(T)},\widehat\psi_{T,1}\rangle
=
\frac{\nu_{R,m}-\lambda_T\ell_{R,m}}
{\sqrt{\Delta_T^{(1)}}}.
\]

Im 2×2-Determinanten hebt sich `lambda_T` exakt weg:

\[
\boxed{
\det\mathcal P_T^{(1)}
=
\frac{\mathcal W_{R,T}}
{\sqrt{\mu_{T,0}\Delta_T^{(1)}}}.
}
\]

Der einzige qualitative Alignment-Engpass ist daher

\[
\boxed{
\mathcal W_{R,T}
=
\ell_{R,0}\nu_{R,1}
-
\ell_{R,1}\nu_{R,0}
\stackrel{?}{\ne}0.
}
\]

C4 liefert

\[
\frac{\ell_{R,1}}{\ell_{R,0}}
=
\frac{\kappa_R}{T}(1+O_R(T^{-1})),
\]

so dass die Frage äquivalent auf

\[
\boxed{
\nu_{R,1}
-
\frac{\kappa_R}{T}(1+O_R(T^{-1}))\nu_{R,0}
\stackrel{?}{\ne}0
}
\]

reduziert wird.

Die Kette C6e–C6j beweist diese Nichtkollinearität nicht; ein endliches Daten-Gegenmodell zeigt, dass targetseitiger Rang 2 allein dafür logisch nicht genügt.

Damit ist der nächste Engpass klarer als zuvor:

\[
\boxed{
\text{Nicht mehr „existiert eine zweite Probe?“, sondern
„erzeugt die zweite gemischte Feshbach-Observation eine neue Jetrichtung?“}
}
\]

Genau das muss C6l entscheiden.