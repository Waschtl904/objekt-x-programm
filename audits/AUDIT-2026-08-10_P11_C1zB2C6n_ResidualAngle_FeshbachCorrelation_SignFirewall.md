# P11-C1z-B2-C6n — Residualwinkel, Feshbach-Korrelationsformel und Vorzeichen-Firewall

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6n]`  
**Direkte Voraussetzungen:** C1z-B2-C6d, C1z-B2-C6j, C1z-B2-C6k, C1z-B2-C6l, C1z-B2-C6m  
**Strukturelle Schnittstellen:** C1z-B, C1z-B2-C3, C1z-B2-C4, C1z-B2-C6a, C1z-B2-C6b, C1z-B2-C6c, C1z-B2-C6e, C1z-B2-C6f, C1z-B2-C6g, C1z-B2-C6h, C1z-B2-C6i  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d `orthogonality != jet alignment`, C1z-B2-C6k `current data != Wronskian nonzero`, C1z-B2-C6l `C4 constant-mode mechanism does not transfer`, C1z-B2-C6m `A-orthogonality != bulk cancellation`.  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6n]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm pos,residual\text{-}A^{-1}\text{-}correlation}
+
\checkmark[M]_{\rm pos,energy\times angle\text{-}factorization}
+
\checkmark[M]_{\rm pos,determinant\text{-}three\text{-}factor\text{-}formula}
+
\checkmark[M]_{\rm pos,Feshbach\text{-}bare\text{-}minus\text{-}screened\text{-}identity}
+
\checkmark[M]_{\rm pos,parity\text{-}compatibility}
+
\checkmark[M]_{\rm neg,positivity\text{-}does\text{-}not\text{-}force\text{-}alignment}
+
\checkmark[M]_{\rm neg,sign\text{-}argument\text{-}from\text{-}S_T\ge0}
+
?[O]_{\rm residual\text{-}angle>0}
+
?[O]_{\rm bare\text{-}hub\text{-}vs\text{-}screening\text{-}separation}
+
?[O]_{\rm quantitative\text{-}s_{min}}
}
\]

C6m reduzierte die vollständige `2x2`-Alignmentfrage auf den einzigen normierten Skalar

\[
\boxed{
 a_{R,T}^{(2)}
 :=
 \left\langle
 \xi_{R,g_T}^{(T)},
 \widehat\psi_{T,1}
 \right\rangle.
}
\tag{C1zB2C6n.1}
\]

C6n beantwortet nun die Frage, ob allgemeine Positivität, eine bilineare Identität oder die bereits bekannte Nichtdegeneration der zweiten Krylov-Probe dieses Skalarprodukt automatisch von null trennt.

Das Ergebnis ist zweigeteilt:

1. Es gibt eine **exakte kanonische Korrelationsformel** im `A_T^{-1}`-Hilbertraum. Dadurch zerfällt das Alignmentproblem in Response-Energie und einen dimensionslosen Residualwinkel.
2. Weder `\mathfrak S_T\ge0` noch `\Delta_T^{(1)}>0` noch positive Response-Energie erzwingen einen positiven Residualwinkel. Ein abstraktes dreidimensionales Modell zeigt dies scharf.

Zusätzlich besitzt der noch offene Korrelationszähler eine konkrete P11-spezifische Feshbach-Zerlegung

\[
\boxed{
\text{bare Hub-Korrelation}
-
\text{Rest-Screening-Korrektur}.
}
\]

Damit ist C6n kein Alignment-Durchbruch, aber die bisher schärfste Formulierung dessen, **welche konkrete Kompensation ausgeschlossen werden muss**.

---

# 0. Verbindliche Daten aus C6m

Fixiere `R>0` und großes `T`.

C6m definiert

\[
 c_{R,T}
 :=
 \frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}
\]

und

\[
\boxed{
 g_{R,T}
 :=
 f_{R,1}-c_{R,T}f_{R,0}.
}
\tag{C1zB2C6n.2}
\]

Dann gilt exakt

\[
\boxed{
\langle J_{R,T}g_{R,T},H_T\mathbf1_T\rangle=0.
}
\tag{C1zB2C6n.3}
\]

Der zugehörige gescreente Response-Vektor ist

\[
\boxed{
\xi_{R,g_T}^{(T)}
:=
A_T^{-1/2}H_T^*J_{R,T}g_{R,T}.
}
\tag{C1zB2C6n.4}
\]

Er ist orthogonal zur ersten Probe

\[
\widehat\psi_{T,0}
=
\frac{\zeta_T}{\sqrt{\mu_{T,0}}},
\qquad
\zeta_T=A_T^{1/2}\mathbf1_T.
\]

Die zweite normierte Krylov-Probe ist eventual durch C6e-C6j wohldefiniert und lautet

\[
\boxed{
\widehat\psi_{T,1}
=
\frac{
\mathfrak S_T\zeta_T-\lambda_T\zeta_T
}{
\sqrt{\Delta_T^{(1)}}
}.
}
\tag{C1zB2C6n.5}
\]

C6m beweist die determinantenerhaltende Triangularisierung

\[
\boxed{
\det\mathcal P_T^{(1)}
=
\frac{\ell_{R,0}(T)}{\sqrt{\mu_{T,0}}}
\,a_{R,T}^{(2)}.
}
\tag{C1zB2C6n.6}
\]

Damit gilt eventual

\[
\boxed{
\mathcal P_T^{(1)}\text{ invertierbar}
\iff
 a_{R,T}^{(2)}\ne0.
}
\tag{C1zB2C6n.7}
\]

Der erste Faktor in (C1zB2C6n.6) ist durch C4 quantitativ stark und nicht der Engpass.

---

# 1. Zwei source-seitige Residualvektoren

Setze

\[
\boxed{
 b_{R,T}
 :=
 H_T^*J_{R,T}g_{R,T}.
}
\tag{C1zB2C6n.8}
\]

Dann ist

\[
\xi_{R,g_T}^{(T)}
=A_T^{-1/2}b_{R,T}.
\]

Weiter setze wie C6l

\[
 h_T:=H_T^*H_T\mathbf1_T,
\]

\[
 \lambda_T:=\frac{\mu_{T,1}}{\mu_{T,0}},
\]

und den source-seitigen zweiten Krylov-Residualvektor

\[
\boxed{
 r_T
 :=
 h_T-\lambda_TA_T\mathbf1_T.
}
\tag{C1zB2C6n.9}
\]

Dann ist

\[
 y_T=A_T^{-1}r_T
\]

und

\[
\widehat\psi_{T,1}
=
\frac{A_T^{-1/2}r_T}{\sqrt{\Delta_T^{(1)}}}.
\tag{C1zB2C6n.10}
\]

Denn C6l zeigte äquivalent

\[
A_T^{1/2}y_T=A_T^{-1/2}r_T.
\]

Damit steht die zweite Alignment-Paarung vollständig source-seitig zur Verfügung.

---

# 2. Der natürliche `A_T^{-1}`-Hilbertraum

Da `A_T=I+R_T^*R_T\ge I` für jedes feste `T` positiv und invertierbar ist, definiere

\[
\boxed{
\langle u,v\rangle_{A_T^{-1}}
:=
\langle u,A_T^{-1}v\rangle.
}
\tag{C1zB2C6n.11}
\]

Die zugehörige Norm ist

\[
\|u\|_{A_T^{-1}}^2
=
\langle u,A_T^{-1}u\rangle.
\]

Diese Geometrie ist nicht extern eingeführt; sie ist genau die bereits vorhandene Feshbach-Geometrie hinter `sigma_T`.

Für `b_{R,T}` gilt

\[
\boxed{
\|b_{R,T}\|_{A_T^{-1}}^2
=
\langle b_{R,T},A_T^{-1}b_{R,T}\rangle
=
\sigma_T(J_{R,T}g_{R,T}).
}
\tag{C1zB2C6n.12}
\]

Für `r_T` gilt aus C6l

\[
\boxed{
\|r_T\|_{A_T^{-1}}^2
=
\Delta_T^{(1)}.
}
\tag{C1zB2C6n.13}
\]

Damit haben beide für das Alignment relevanten Größen eine direkte geometrische Bedeutung in **derselben** positiven Form.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,residual\text{-}A^{-1}\text{-}correlation}.
}
\]

---

# 3. Beide Residuen liegen im selben First-Observation-Orthogonalkomplement

Der ausgezeichnete erste Source-Vektor in der `A_T^{-1}`-Geometrie ist

\[
A_T\mathbf1_T.
\]

Für `b_{R,T}` gilt wegen C6ms exakter Nullbedingung

\[
\begin{aligned}
\langle b_{R,T},A_T\mathbf1_T\rangle_{A_T^{-1}}
&=
\langle b_{R,T},\mathbf1_T\rangle\\
&=
\langle H_T^*J_{R,T}g_{R,T},\mathbf1_T\rangle\\
&=
\langle J_{R,T}g_{R,T},H_T\mathbf1_T\rangle\\
&=0.
\end{aligned}
\tag{C1zB2C6n.14}
\]

Für `r_T` gilt

\[
\begin{aligned}
\langle r_T,A_T\mathbf1_T\rangle_{A_T^{-1}}
&=
\langle r_T,\mathbf1_T\rangle\\
&=
\langle h_T,\mathbf1_T\rangle
-
\lambda_T\langle A_T\mathbf1_T,\mathbf1_T\rangle\\
&=
\mu_{T,1}-\frac{\mu_{T,1}}{\mu_{T,0}}\mu_{T,0}\\
&=0.
\end{aligned}
\tag{C1zB2C6n.15}
\]

Also liegen

\[
\boxed{
 b_{R,T},r_T
\in
(A_T\mathbf1_T)^{\perp_{A_T^{-1}}}.
}
\tag{C1zB2C6n.16}
\]

Dies ist die source-seitige Version der Tatsache, dass sowohl `xi_{R,g_T}` als auch die zweite Krylov-Probe im Targetraum orthogonal zur ersten Probe liegen.

Aber genau wie C6d/C6m warnten:

\[
\boxed{
\text{gemeinsame Orthogonalität zur ersten Richtung}
\not\Rightarrow
\text{Nichtorthogonalität untereinander}.
}
\tag{C1zB2C6n.17}
\]

---

# 4. Exakte Korrelationsformel für den Alignment-Skalar

Aus (C1zB2C6n.4) und (C1zB2C6n.10) folgt

\[
\begin{aligned}
 a_{R,T}^{(2)}
&=
\left\langle
A_T^{-1/2}b_{R,T},
\frac{A_T^{-1/2}r_T}{\sqrt{\Delta_T^{(1)}}}
\right\rangle\\
&=
\boxed{
\frac{
\langle b_{R,T},r_T\rangle_{A_T^{-1}}
}{
\sqrt{\Delta_T^{(1)}}
}.
}
\end{aligned}
\tag{C1zB2C6n.18}
\]

Da

\[
\sqrt{\Delta_T^{(1)}}=\|r_T\|_{A_T^{-1}},
\]

ist dies noch transparenter:

\[
\boxed{
 a_{R,T}^{(2)}
=
\frac{
\langle b_{R,T},r_T\rangle_{A_T^{-1}}
}{
\|r_T\|_{A_T^{-1}}
}.
}
\tag{C1zB2C6n.19}
\]

Damit ist `a_{R,T}^{(2)}` die skalare Projektion des first-observation-blinden Source-Responses auf die normierte zweite Krylov-Residualrichtung.

Insbesondere

\[
\boxed{
 a_{R,T}^{(2)}=0
\iff
 b_{R,T}\perp_{A_T^{-1}}r_T.
}
\tag{C1zB2C6n.20}
\]

Das ist der exakte source-seitige Ja/Nein-Test.

---

# 5. Energie mal Winkel — der fehlende dimensionslose Faktor

Falls

\[
\sigma_T(Jg_{R,T})>0,
\]

definiere

\[
\boxed{
\rho_{R,T}^{(2)}
:=
\frac{
|\langle b_{R,T},r_T\rangle_{A_T^{-1}}|^2
}{
\|b_{R,T}\|_{A_T^{-1}}^2
\|r_T\|_{A_T^{-1}}^2
}.
}
\tag{C1zB2C6n.21}
\]

Nach Cauchy-Schwarz gilt

\[
\boxed{0\le\rho_{R,T}^{(2)}\le1.}
\tag{C1zB2C6n.22}
\]

Geometrisch ist `rho` das Quadrat des Kosinus des Winkels zwischen `b_{R,T}` und `r_T` in der Feshbach-Geometrie `A_T^{-1}`.

Falls `sigma_T(Jg_{R,T})=0`, setze kanonisch

\[
\rho_{R,T}^{(2)}:=0.
\]

Dann gilt in allen Fällen exakt

\[
\boxed{
|a_{R,T}^{(2)}|^2
=
\sigma_T(J_{R,T}g_{R,T})
\,\rho_{R,T}^{(2)}.
}
\tag{C1zB2C6n.23}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,energy\times angle\text{-}factorization}.
}
\]

### Interpretation

Die zweite Alignmentfrage zerfällt damit **exakt** in zwei logisch unabhängige Komponenten:

1. **Residual-Response-Energie**
   \[
   \sigma_T(Jg_{R,T});
   \]
2. **Residual-Observability-Winkel**
   \[
   \rho_{R,T}^{(2)}.
   \]

C6m hatte bereits gezeigt, dass Response-Energie allein nicht genügt. C6n identifiziert nun präzise den fehlenden dimensionslosen Faktor.

Die qualitative Invertibilität ist äquivalent zu

\[
\boxed{
\rho_{R,T}^{(2)}>0.
}
\tag{C1zB2C6n.24}
\]

wobei `rho>0` automatisch `sigma>0` einschließt.

---

# 6. Dreifaktorformel für den `2x2`-Determinanten

C6m liefert

\[
\det\mathcal P_T^{(1)}
=
\frac{\ell_{R,0}}{\sqrt{\mu_{T,0}}}
a_{R,T}^{(2)}.
\]

Quadriert man den Betrag und benutzt (C1zB2C6n.23), folgt

\[
\boxed{
|\det\mathcal P_T^{(1)}|^2
=
\frac{|\ell_{R,0}(T)|^2}{\mu_{T,0}}
\,
\sigma_T(J_{R,T}g_{R,T})
\,
\rho_{R,T}^{(2)}.
}
\tag{C1zB2C6n.25}
\]

Dies ist die bisher vollständigste faktorielle Form des ersten echten `2x2`-Alignmentdeterminanten.

Die drei Faktoren haben getrennte Bedeutungen:

- erster C4-Kanal;
- Response-Energie des exakt first-observation-blinden Sourcevektors;
- geometrischer Alignment-Winkel zur zweiten Krylov-Richtung.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,determinant\text{-}three\text{-}factor\text{-}formula}.
}
\]

### Konsequenz für spätere `s_min`-Arbeit

Allgemein gilt für eine `2x2`-Matrix

\[
 s_{\min}(\mathcal P)
=
\frac{|\det\mathcal P|}{s_{\max}(\mathcal P)}
\ge
\frac{|\det\mathcal P|}{\|\mathcal P\|_F}.
\]

Für einen quantitativen `s_min`-Satz braucht P11 daher nun getrennt:

1. einen unteren Bound für `rho`;
2. einen unteren/geeigneten Bound für `sigma_T(Jg)`;
3. eine obere Kontrolle von `||P||_F`.

C6n behauptet keinen dieser noch offenen Bounds.

---

# 7. Warum `mathfrak S_T >= 0` kein Vorzeichenargument liefert

Die C6n-Vorüberlegung fragte, ob die Positivität

\[
\mathfrak S_T
=
A_T^{-1/2}H_T^*H_TA_T^{-1/2}
\ge0
\]

ein Vorzeichen für

\[
 a_{R,T}^{(2)}
\]

erzwingen könnte.

Die Antwort ist **nein**.

Positivität eines Operators kontrolliert quadratische Formen

\[
\langle x,\mathfrak S_Tx\rangle\ge0,
\]

aber keine feste Off-Diagonalpaarung

\[
\langle x,\mathfrak S_Ty\rangle.
\]

C6ms First-Observation-Nullbedingung entfernt zwar die erste Krylov-Komponente, macht die zweite Off-Diagonalpaarung aber nicht zu einer quadratischen Form.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,sign\text{-}argument\text{-}from\text{-}S_T\ge0}.
}
\]

---

# 8. Scharfes abstraktes Dreidimensional-Modell

Um den logischen Scope exakt zu trennen, betrachte den abstrakten Response-Raum

\[
\mathbb C^3
\]

mit Standardbasis `e_1,e_2,e_3`.

Setze

\[
\zeta=e_1
\]

und für ein festes `0<|t|<1`

\[
\boxed{
\mathfrak S
=
\begin{pmatrix}
1&t&0\\
t&1&0\\
0&0&1
\end{pmatrix}.
}
\tag{C1zB2C6n.26}
\]

Dann ist

\[
\mathfrak S>0.
\]

Weiter

\[
\mathfrak S\zeta=e_1+t e_2.
\]

Der Rayleighquotient der ersten Richtung ist

\[
\lambda=1,
\]

und der zweite Krylov-Residualvektor ist

\[
\mathfrak S\zeta-\lambda\zeta=t e_2.
\]

Also

\[
\Delta=|t|^2>0.
\]

Die zweite Krylov-Probe existiert damit strikt.

Wähle nun einen first-observation-blinden Response-Vektor

\[
\xi_g=e_3.
\]

Dann

\[
\langle\xi_g,\zeta\rangle=0
\]

und dennoch

\[
\boxed{
\langle\xi_g,\widehat\psi_1\rangle=0.
}
\tag{C1zB2C6n.27}
\]

Gleichzeitig ist

\[
\|\xi_g\|^2=1>0.
\]

Damit können gleichzeitig gelten:

- positiver Operator `S`;
- nichtdegenerierte zweite Krylov-Probe;
- positive Response-Energie;
- exakte First-Observation-Nullheit;
- aber **Null-Alignment** zur zweiten Probe.

Wählt man statt `e_3` die Vektoren `e_2`, `-e_2` oder `e^{i\theta}e_2`, kann die zweite Paarung positives, negatives beziehungsweise beliebiges komplexes Vorzeichen/Phase besitzen.

Dies ist **kein P11-Gegenbeispiel**. Es ist ein logisches Daten-No-Go:

\[
\boxed{
\mathfrak S_T\ge0
+
\Delta_T^{(1)}>0
+
\sigma_T(Jg)>0
+
\langle\xi_g,\zeta_T\rangle=0
\not\Rightarrow
 a_{R,T}^{(2)}\ne0.
}
\tag{C1zB2C6n.28}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,positivity\text{-}does\text{-}not\text{-}force\text{-}alignment}.
}
\]

---

# 9. P11-spezifische Vereinfachung des Korrelationszählers

Aus (C1zB2C6n.18) gilt

\[
\sqrt{\Delta_T^{(1)}}\,a_{R,T}^{(2)}
=
\langle b_{R,T},A_T^{-1}r_T\rangle.
\]

Mit

\[
 r_T=h_T-\lambda_TA_T\mathbf1_T
\]

folgt

\[
 A_T^{-1}r_T
=
A_T^{-1}h_T-\lambda_T\mathbf1_T.
\]

Wegen

\[
\langle b_{R,T},\mathbf1_T\rangle=0
\]

verschwindet der `lambda_T`-Term exakt. Somit

\[
\boxed{
\sqrt{\Delta_T^{(1)}}\,a_{R,T}^{(2)}
=
\langle b_{R,T},A_T^{-1}h_T\rangle.
}
\tag{C1zB2C6n.29}
\]

Explizit:

\[
\boxed{
\sqrt{\Delta_T^{(1)}}\,a_{R,T}^{(2)}
=
\left\langle
H_T^*J_{R,T}g_{R,T},
A_T^{-1}H_T^*H_T\mathbf1_T
\right\rangle.
}
\tag{C1zB2C6n.30}
\]

Diese Formel ist äquivalent zu C6ms Profilpaarung, aber jetzt als symmetrische Feshbach-Korrelation zweier source-seitiger Responses geschrieben.

---

# 10. Exakte Feshbach-Resolventenidentität

Für jeden beschränkten `R_T` gilt die Standardidentität

\[
\boxed{
(I+R_T^*R_T)^{-1}
=
I
-
R_T^*(I+R_TR_T^*)^{-1}R_T.
}
\tag{C1zB2C6n.31}
\]

Da

\[
A_T=I+R_T^*R_T,
\]

folgt aus (C1zB2C6n.29):

\[
\begin{aligned}
\sqrt{\Delta_T^{(1)}}\,a_{R,T}^{(2)}
&=
\langle b_{R,T},h_T\rangle\\
&\quad-
\left\langle
b_{R,T},
R_T^*(I+R_TR_T^*)^{-1}R_Th_T
\right\rangle.
\end{aligned}
\]

Also

\[
\boxed{
\sqrt{\Delta_T^{(1)}}\,a_{R,T}^{(2)}
=
\mathcal U_{R,T}
-
\mathcal C_{R,T},
}
\tag{C1zB2C6n.32}
\]

mit

\[
\boxed{
\mathcal U_{R,T}
:=
\langle b_{R,T},h_T\rangle
}
\tag{C1zB2C6n.33}
\]

und

\[
\boxed{
\mathcal C_{R,T}
:=
\left\langle
R_Tb_{R,T},
(I+R_TR_T^*)^{-1}R_Th_T
\right\rangle.
}
\tag{C1zB2C6n.34}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,Feshbach\text{-}bare\text{-}minus\text{-}screened\text{-}identity}.
}
\]

### Interpretation

`mathcal U_{R,T}` ist die **ungescreente gemischte Hub-Korrelation** zwischen

\[
H_T^*Jg_{R,T}
\]

und

\[
H_T^*H_T\mathbf1_T.
\]

`mathcal C_{R,T}` ist die konkrete Rest-Feshbach-Korrektur derselben Korrelation.

Daher lautet die qualitative Alignmentfrage exakt

\[
\boxed{
 a_{R,T}^{(2)}\ne0
\iff
\mathcal U_{R,T}\ne\mathcal C_{R,T}.
}
\tag{C1zB2C6n.35}
\]

Das ist die bisher P11-nächste Formulierung des offenen Problems.

---

# 11. Warum die Resolventenzerlegung noch kein Vorzeichen liefert

Obwohl

\[
(I+R_TR_T^*)^{-1}\ge0,
\]

ist

\[
\mathcal C_{R,T}
=
\langle R_Tb_{R,T},B_TR_Th_T\rangle
\]

mit

\[
B_T:=(I+R_TR_T^*)^{-1}\ge0
\]

weiterhin eine Off-Diagonalpaarung zwischen zwei verschiedenen Vektoren.

Daher besitzt `mathcal C_{R,T}` aus Positivität allein kein festes Vorzeichen.

Ebenso ist

\[
\mathcal U_{R,T}=\langle b_{R,T},h_T\rangle
\]

keine quadratische Form.

Somit darf aus

\[
A_T^{-1}\ge0,
\qquad
\mathfrak S_T\ge0
\]

nicht auf

\[
\mathcal U_{R,T}-\mathcal C_{R,T}>0
\]

oder auch nur auf Nichtverschwindung geschlossen werden.

Der nächste positive Satz muss P11-spezifisch mindestens eine der folgenden Aussagen beweisen:

1. `mathcal U_{R,T}` besitzt einen asymptotisch dominanten expliziten Hauptterm;
2. `mathcal C_{R,T}=o(mathcal U_{R,T})`;
3. `mathcal U_{R,T}` und `mathcal C_{R,T}` besitzen strukturell verschiedene arithmetische Supports, die exakte Kompensation ausschließen;
4. eine andere P11-spezifische Identität erzwingt `rho_{R,T}^{(2)}>0`.

Keine dieser Aussagen wird in C6n postuliert.

---

# 12. Parität ist kompatibel, aber wiederum nicht entscheidend

Aus C6a/C6l liegen

\[
 f_{R,0},f_{R,1}
\]

im ungeraden Source-Sektor. Daher ist auch

\[
 g_{R,T}
\]

ungerade.

Da `H_T` mit der Source-Reflexion antikommutiert, ist

\[
 b_{R,T}=H_T^*Jg_{R,T}
\]

gerade.

C6l zeigte bereits, dass

\[
 h_T,
\quad
A_T\mathbf1_T,
\quad
r_T
\]

ebenfalls gerade sind.

Also liegen die beiden Korrelationsvektoren

\[
 b_{R,T},r_T
\]

im selben geraden Sektor.

Somit gibt es **keine Paritätsobstruktion** gegen Alignment.

Aber wie schon C6d/C6l:

\[
\boxed{
\text{gleiche Parität}
\not\Rightarrow
\rho_{R,T}^{(2)}>0.
}
\tag{C1zB2C6n.36}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,parity\text{-}compatibility}.
}
\]

---

# 13. Reconciliation mit C6e-C6m

## C6e-C6j

Diese Knoten sichern eventual die Existenz der zweiten Krylov-Probe und liefern

\[
\Delta_T^{(1)}>0
\]

sowie die explizite Untergrenze

\[
\Delta_T^{(1)}\gtrsim e^{-5T}.
\]

C6n nutzt dies nur, um `widehat psi_{T,1}` sicher zu definieren. Die Untergrenze selbst erzwingt keinen positiven Residualwinkel.

## C6k

C6k reduzierte die `2x2`-Invertibilität auf den Response-Wronskian.

C6n ersetzt den Wronskian endgültig durch den geometrischen Winkel `rho_{R,T}^{(2)}`.

## C6l

C6l isolierte den echten Residualprofilanteil `H_Ty_T` und zeigte den Bulk/Shell-Engpass.

C6n umgeht die vollständige Profilasymptotik erneut und schreibt dieselbe Information als `A_T^{-1}`-Korrelation von `b_{R,T}` und `r_T`.

## C6m

C6m triangularisierte die Probe-Matrix und isolierte `a_{R,T}^{(2)}`.

C6n faktorisiert nun

\[
|a_{R,T}^{(2)}|^2
=
\sigma_T(Jg_{R,T})\rho_{R,T}^{(2)}.
\]

Damit ist exakt sichtbar, warum Response-Energie und Alignment zwei verschiedene Aufgaben sind.

Kein früherer No-Go wird supersediert.

---

# 14. No-Go-Persistenzmatrix

| Früherer Knoten | Gesiegelter Befund | Wirkung in C6n |
|---|---|---|
| C1y | translationsinvariante Regulatoren lösen Hub/Rest-Konflikt nicht im C1y-Scope | unverändert |
| B2-A | Gamma-Präkonditionierung erzeugt keinen fehlenden Schattenmechanismus | unverändert |
| B2-B | naiver Haar-`L^2`-Endpunkt reicht nicht | unverändert |
| C4 | unendliche Boundary-Jet-Hierarchie; kein fester endlicher Jet stabilisiert roh | unverändert |
| C6 | kein voller Odd-Transport durch festen endlichen Jetquotienten | unverändert |
| C6a | Self-Grams/Kompression reichen nicht | unverändert |
| C6b | C2-Flachheit allein reicht nicht | unverändert |
| C6c | Triangularität / Rang-eins reicht nicht | unverändert |
| C6d | Orthogonalität der Probes ist kein Jet-Alignment | durch Residualwinkel präzisiert |
| C6e-C6j | zweite Probe eventual nichtdegeneriert | positiv übernommen |
| C6k | aktuelle Daten erzwingen Wronskian `!=0` nicht | bestätigt |
| C6l | C4-Konstantenmechanismus transferiert nicht auf `y_T` | unverändert |
| C6m | `A_T`-Orthogonalität erzeugt keinen Bulk-Kollaps | bestätigt |

---

# 15. Was C6n ausdrücklich nicht beweist

Nicht bewiesen sind:

- `a_{R,T}^{(2)} != 0` für alle großen `T`;
- `rho_{R,T}^{(2)}>0` eventual;
- ein unterer Bound für `rho_{R,T}^{(2)}`;
- ein unterer oder oberer geeigneter Bound für `sigma_T(Jg_{R,T})`;
- Dominanz von `mathcal U_{R,T}` über `mathcal C_{R,T}`;
- ein Vorzeichen von `mathcal U_{R,T}`;
- ein Vorzeichen von `mathcal C_{R,T}`;
- eine arithmetische Supporttrennung zwischen beiden Termen;
- eine asymptotische Klassifikation von `Delta_T^(1)`;
- ein quantitativer `s_min`-Bound;
- `tau_T(E_{R,1}) -> 0`;
- `Theta_{T,U}^{E_{R,1}} -> I`;
- starker Odd-Gauge-Limes.

Insbesondere gilt weiterhin logisch:

\[
\boxed{
\rho_{R,T}^{(2)}=0
}
\]

ist mit allen bisher gesiegelten allgemeinen Operatorinformationen vereinbar.

Ein Ausschluss dieses Falls muss neue P11-spezifische Arithmetik verwenden.

---

# 16. Exakter nächster Arbeitsauftrag C6o

C6n reduziert die qualitative Alignmentfrage auf

\[
\boxed{
\mathcal U_{R,T}\ne\mathcal C_{R,T}.
}
\]

Daher sollte der nächste Knoten **nicht** erneut abstrakte Positivität, Krylov-Rang oder `Delta` untersuchen.

Der nächste Arbeitsauftrag lautet:

\[
\boxed{
\text{C6o: nackte Hub-Korrelation versus Rest-Screening-Korrektur.}
}
\tag{C1zB2C6n.37}
\]

Konkret:

1. Berechne/zerlege
   \[
   \mathcal U_{R,T}
   =
   \langle H_T^*Jg_{R,T},H_T^*H_T\mathbf1_T\rangle.
   \]
2. Isoliere darin primitive, Cross-Prime- und höhere Prime-Power-Komponenten.
3. Schreibe
   \[
   \mathcal C_{R,T}
   =
   \langle R_TH_T^*Jg_{R,T},
   (I+R_TR_T^*)^{-1}R_TH_T^*H_T\mathbf1_T\rangle
   \]
   in derselben Primsektorzerlegung.
4. Prüfe zuerst, ob beide Terme überhaupt denselben führenden arithmetischen Support besitzen.
5. Nur falls ja, sind quantitative Größenvergleiche nötig; falls nein, könnte die Supportgeometrie bereits exakte Kompensation ausschließen.

### Firewall für C6o

Nicht zulässig sind die Abkürzungen

\[
\mathfrak S_T\ge0
\Rightarrow a_{R,T}^{(2)}>0,
\]

oder

\[
\Delta_T^{(1)}>0
\Rightarrow\rho_{R,T}^{(2)}>0.
\]

Der nächste Fortschritt muss aus der konkreten P11-Primzahl-/Reststruktur kommen.

---

# 17. Endurteil

C6n beantwortet die bilineare Identitätssuche vollständig auf der abstrakten Feshbach-Ebene.

Der zweite Alignment-Skalar ist exakt

\[
 a_{R,T}^{(2)}
=
\frac{
\langle b_{R,T},r_T\rangle_{A_T^{-1}}
}{
\|r_T\|_{A_T^{-1}}
},
\]

mit

\[
\|b_{R,T}\|_{A_T^{-1}}^2
=
\sigma_T(Jg_{R,T}),
\qquad
\|r_T\|_{A_T^{-1}}^2
=
\Delta_T^{(1)}.
\]

Daraus folgt die exakte Energie-Winkel-Zerlegung

\[
\boxed{
|a_{R,T}^{(2)}|^2
=
\sigma_T(Jg_{R,T})\rho_{R,T}^{(2)}.
}
\]

und für den vollständigen `2x2`-Determinanten

\[
\boxed{
|\det\mathcal P_T^{(1)}|^2
=
\frac{|\ell_{R,0}(T)|^2}{\mu_{T,0}}
\sigma_T(Jg_{R,T})
\rho_{R,T}^{(2)}.
}
\]

Damit ist mathematisch präzise getrennt:

\[
\boxed{
\text{Energie} \neq \text{Alignment}.
}
\]

Allgemeine Positivität kann den fehlenden Winkel nicht liefern. Das abstrakte `3D`-Modell zeigt, dass selbst bei positiver `S`, `Delta>0`, positiver Response-Energie und First-Observation-Nullheit das zweite Alignment exakt null sein kann.

P11-spezifisch bleibt jedoch die exakte Identität

\[
\boxed{
\sqrt{\Delta_T^{(1)}}\,a_{R,T}^{(2)}
=
\mathcal U_{R,T}-\mathcal C_{R,T},
}
\]

also

\[
\boxed{
\text{bare Hub-Korrelation}
-
\text{Rest-Feshbach-Screening}.
}
\]

Damit ist der nächste offene mathematische Schritt nicht mehr diffus: Es muss gezeigt werden, dass diese beiden konkreten P11-Terme die zweite Residualrichtung nicht exakt auslöschen.