# P11-TC1-MIX — Mixed-Jet Bilinear Terminal Asymptotic

**Datum:** 2026-08-12  
**Knoten:** `[P11-TC1-MIX]`  
**Vorgänger / autoritative Inputs:** P11-C1z-B2-C4, P11-C1z-B2-C5, P11-O3d-I2, P11-O3g  
**Direkter Zielstrang:** TC0 -> TC1 Cross-Terminal -> Cauchy-Defekt -> starker odd Terminaltransport?  
**Modus:** direkter mathematischer Audit; externer Countercheck ausstehend  
**Scope-Firewall:** kein Schluss auf `K_{R,S}^{T,U}->I`, kein Schluss auf starke Cauchy-Konvergenz von `W_{R,S,-}^{[T]}`, kein O3k, kein O4, kein SYN, kein Seal, keine RH-Folgerung.

---

## 0. Urteil

Die in der Übergabe formulierte Mixed-Jet-Frage ist **beweisbar**, aber mit zwei zwingenden Korrekturen:

1. Die committed O3d-I2-Skala lautet

\[
\frac{e^T}{T^{2m+2}},
\]

nicht `T^{2m+2}e^T`.

2. Wegen der in C5/O3g verwendeten sesquilinearen Konvention lautet der gemischte Koeffizient

\[
\beta_R^{(m)}(f)\,\overline{\beta_R^{(n)}(g)}.
\]

Für feste nichttriviale glatte odd Vektoren

\[
f,g\in C_c^\infty((-R,R))_{\rm odd},
\]

mit ersten nichtverschwindenden Integral-Jets

\[
m=m(f),\qquad n=m(g),
\]

gilt:

\[
\boxed{
\sigma_T\!\left(J_{R,T}f,J_{R,T}g\right)
=
 c_m c_n\,
 \beta_R^{(m)}(f)\,
 \overline{\beta_R^{(n)}(g)}
 \frac{e^T}{T^{m+n+2}}
 \bigl(1+o_{R,f,g}(1)\bigr).
}
\tag{TC1-MIX.1}
\]

Hier

\[
c_j=\frac{\binom{2j}{j}}{4^j}.
\]

Der entscheidende Punkt ist: **Die bloße führende Diagonalasymptotik polarisiert bei `m\neq n` nicht tief genug.** Der Beweis benutzt stattdessen die in O3d-I2 bereits enthaltene matching Konstantenmode-Unter-/Obergeometrie und isoliert einen **positiven Schur-Rest**. Dessen gemischter Anteil wird durch Cauchy-Schwarz automatisch auf der geometrischen Mixed-Jet-Skala klein.

Zusätzlich folgt für jedes feste solche Paar die asymptotische Winkelkollaps-Aussage

\[
\boxed{
\frac{
\sigma_T(Jf,Jg)
}{
\sigma_T(Jf,Jf)^{1/2}\,\sigma_T(Jg,Jg)^{1/2}
}
\longrightarrow
\frac{
\beta_R^{(m)}(f)\overline{\beta_R^{(n)}(g)}
}{
|\beta_R^{(m)}(f)|\,|\beta_R^{(n)}(g)|
}.
}
\tag{TC1-MIX.2}
\]

Insbesondere konvergiert der Betrag der normierten Schur-Korrelation gegen `1`.

**Aber:** Dies ist eine fixed-vector Aussage. Sie kontrolliert weder `G_{R,T}^{-1/2}` auf `T`-abhängigen Vektoren noch Spektralunterräume, Konditionszahlen oder Range-Leakage uniform. Daher folgt daraus **keine** Konvergenzaussage für den Cross-Terminal-Kern.

Status:

\[
\boxed{
\begin{aligned}
[P11\text{-}TC1\text{-}MIX]
&\quad \checkmark[M]_{\rm corrected\ mixed\text{-}jet\ bilinear\ asymptotic}\\
&+\checkmark[M]_{\rm positive\ constant\text{-}mode\ remainder\ decomposition}\\
&+\checkmark[M]_{\rm fixed\text{-}pair\ asymptotic\ angle\ collapse}\\
&+\checkmark[M]_{\rm bare\ diagonal\ polarization\ insufficient\ for\ }m\ne n\\
&+?[O]_{\rm full\ graded\ mixed\text{-}jet\ expansion}\\
&+?[O]_{\rm uniform\ finite\text{-}jet\ Gram/square\text{-}root\ control}\\
&+?[O]_{K_{R,S}^{T,U}\to I}\\
&+?[O]_{W_{R,S,-}^{[T]}\ \rm strong\ Cauchy}.
\end{aligned}
}
\]

---

# 1. Autoritative Ausgangsdaten

Fixiere `R>0`. Für `T>R` setze

\[
h_T(f):=H_T^*J_{R,T}f,
\qquad
A_T:=I+R_T^*R_T.
\tag{TC1-MIX.3}
\]

Nach C5 ist der Schurterm sesquilinear:

\[
\boxed{
\sigma_T(Jf,Jg)
=
\langle h_T(f),A_T^{-1}h_T(g)\rangle.
}
\tag{TC1-MIX.4}
\]

Definiere die Konstantenmode

\[
\mathbf 1_T:=1_{(-T,T)}
\]

und

\[
\ell_T(f)
:=
\langle h_T(f),\mathbf1_T\rangle
=
\langle J_{R,T}f,H_T\mathbf1_T\rangle.
\tag{TC1-MIX.5}
\]

C4 liefert für jeden festen Trunkationsgrad eine vollständige `1/T`-Entwicklung. Insbesondere, wenn `m=m(f)` der erste nichtverschwindende Integral-Jet ist,

\[
\boxed{
\ell_T(f)
=
-\sqrt2\,c_m\beta_R^{(m)}(f)
\frac{e^{T/2}}{T^{m+1/2}}
\bigl(1+O_{R,f,m}(T^{-1})\bigr).
}
\tag{TC1-MIX.6}
\]

O3d-I2 benutzt außerdem die scharfe Konstantenmode-Norm

\[
\boxed{
d_T
:=
\langle\mathbf1_T,A_T\mathbf1_T\rangle
=2T+O(1).
}
\tag{TC1-MIX.7}
\]

und beweist für jeden festen nichttrivialen glatten odd Vektor mit erstem Jet `m`:

\[
\boxed{
\sigma_T(Jf,Jf)
=
 c_m^2|\beta_R^{(m)}(f)|^2
 \frac{e^T}{T^{2m+2}}
 (1+o_{R,f}(1)).
}
\tag{TC1-MIX.8}
\]

Wichtig für den vorliegenden Audit ist nicht nur (TC1-MIX.8), sondern die **matching Rank-one-Untergeometrie** aus O3d-I2:

\[
\boxed{
\frac{|\ell_T(f)|^2}{d_T}
=
 c_m^2|\beta_R^{(m)}(f)|^2
 \frac{e^T}{T^{2m+2}}
 (1+o_{R,f}(1)).
}
\tag{TC1-MIX.9}
\]

Genau diese zusätzliche Information ist das neue Mixed-Jet-Scharnier.

---

# 2. Warum naive Polarisation bei verschiedenen Jets nicht reicht

Sei zunächst

\[
m<n.
\]

Dann besitzt für jedes feste `\lambda\in\mathbb C` der Vektor

\[
f+\lambda g
\]

weiterhin ersten Jet `m`, weil

\[
\beta_R^{(m)}(g)=0,
\qquad
\beta_R^{(m)}(f)\ne0.
\]

Die bloße O3d-I2-Leading-Order-Aussage gibt daher nur

\[
\sigma_T(J(f+\lambda g),J(f+\lambda g))
=
 c_m^2|\beta_R^{(m)}(f)|^2
 \frac{e^T}{T^{2m+2}}
 (1+o(1)),
\]

unabhängig von `\lambda` auf dieser führenden Skala.

Der gesuchte Mixed-Term liegt aber auf der kleineren Skala

\[
\frac{e^T}{T^{m+n+2}}
=
\frac{e^T}{T^{2m+2}}\,T^{-(n-m)}.
\]

Ein unspezifiziertes `o(e^T/T^{2m+2})` ist hierfür nicht ausreichend.

Dies ist nicht nur ein technischer Verdacht. Betrachte abstrakt die positiven Formen auf `\mathbb C^2`

\[
Q_T^{(\rho)}(x,y)
=
a_T|x|^2+b_T|y|^2
+2\operatorname{Re}\!\left(
\rho\sqrt{a_Tb_T}\,x\overline y
\right),
\qquad |\rho|\le1,
\tag{TC1-MIX.10}
\]

mit

\[
a_T=\frac{e^T}{T^{2m+2}},
\qquad
b_T=\frac{e^T}{T^{2n+2}}.
\]

Für jeden festen Vektor mit `x\ne0` ist

\[
Q_T^{(\rho)}(x,y)\sim a_T|x|^2,
\]

und auf der Achse `x=0`

\[
Q_T^{(\rho)}(0,y)=b_T|y|^2.
\]

Diese gesamte geschichtete führende Diagonalinformation ist unabhängig von `\rho`, während der gemischte Koeffizient beliebig mit `\rho` variiert.

Daher:

\[
\boxed{
\text{O3d-I2 als bloßer Leading-Diagonalsatz bestimmt TC1-MIX für }m\ne n\text{ nicht.}
}
\tag{TC1-MIX.11}
\]

Die in O3g verwendete direkte Polarisation ist deshalb exakt auf der **same-jet** Stufe ausreichend, aber nicht als alleinige Methode für verschiedene erste Jets.

Status:

\[
\boxed{\checkmark[M]_{\rm bare\ leading\ diagonal\ data\ insufficient}.}
\]

---

# 3. Exakte positive Konstantenmode-Abspaltung

Definiere die sesquilineare Rank-one-Form

\[
\boxed{
\rho_T(f,g)
:=
\frac{\ell_T(f)\overline{\ell_T(g)}}{d_T}.
}
\tag{TC1-MIX.12}
\]

und den Rest

\[
\boxed{
D_T(f,g)
:=
\sigma_T(Jf,Jg)-\rho_T(f,g).
}
\tag{TC1-MIX.13}
\]

Der entscheidende neue Punkt ist:

\[
\boxed{D_T\ge0\text{ als sesquilineare Form}.}
\tag{TC1-MIX.14}
\]

**Beweis.** Da

\[
A_T=I+R_T^*R_T\ge I,
\]

ist `A_T` positiv und invertierbar. Setze

\[
x_f:=A_T^{-1/2}h_T(f),
\qquad
v_T:=A_T^{1/2}\mathbf1_T.
\]

Dann

\[
\sigma_T(Jf,Jg)=\langle x_f,x_g\rangle,
\]

\[
\ell_T(f)=\langle x_f,v_T\rangle,
\qquad
d_T=\|v_T\|^2.
\]

Ist `P_{v_T}` der orthogonale Rang-eins-Projektor auf `\mathbb Cv_T`, so folgt exakt

\[
\boxed{
D_T(f,g)
=
\langle (I-P_{v_T})x_f,(I-P_{v_T})x_g\rangle.
}
\tag{TC1-MIX.15}
\]

Damit ist `D_T` positiv semidefinit. Insbesondere gilt die Cauchy-Schwarz-Ungleichung

\[
\boxed{
|D_T(f,g)|^2
\le
D_T(f,f)D_T(g,g).
}
\tag{TC1-MIX.16}
\]

Dies ist die Struktur, die bei bloßer Polarisation fehlt.

---

# 4. O3d-I2 macht den positiven Rest diagonal klein

Sei `f` fest, glatt, odd und nichtzero mit erstem Jet `m`. Aus (TC1-MIX.8) und (TC1-MIX.9):

\[
\sigma_T(Jf,Jf)
=
\Lambda_{f,T}(1+o(1)),
\]

\[
\rho_T(f,f)
=
\Lambda_{f,T}(1+o(1)),
\]

wobei

\[
\Lambda_{f,T}
:=
 c_m^2|\beta_R^{(m)}(f)|^2
 \frac{e^T}{T^{2m+2}}.
\tag{TC1-MIX.17}
\]

Da `D_T(f,f)=\sigma_T(Jf,Jf)-\rho_T(f,f)\ge0`, folgt

\[
\boxed{
D_T(f,f)=o(\Lambda_{f,T}).
}
\tag{TC1-MIX.18}
\]

Analog für `g` mit erstem Jet `n`:

\[
\boxed{
D_T(g,g)=o(\Lambda_{g,T}),
}
\tag{TC1-MIX.19}
\]

\[
\Lambda_{g,T}
:=
 c_n^2|\beta_R^{(n)}(g)|^2
 \frac{e^T}{T^{2n+2}}.
\]

Cauchy-Schwarz für den positiven Rest liefert nun

\[
\begin{aligned}
|D_T(f,g)|
&\le
\sqrt{D_T(f,f)D_T(g,g)}\\
&=
o\!\left(\sqrt{\Lambda_{f,T}\Lambda_{g,T}}\right).
\end{aligned}
\]

Da

\[
\sqrt{\Lambda_{f,T}\Lambda_{g,T}}
=
 c_mc_n
 |\beta_R^{(m)}(f)|
 |\beta_R^{(n)}(g)|
 \frac{e^T}{T^{m+n+2}},
\]

folgt die exakt benötigte Mixed-Jet-Fehlerordnung:

\[
\boxed{
D_T(f,g)
=
o_{R,f,g}\!\left(
\frac{e^T}{T^{m+n+2}}
\right).
}
\tag{TC1-MIX.20}
\]

**Adversarialer Punkt:** Hier wird keine Uniformität in einer Vektorfamilie behauptet oder benötigt. `f` und `g` sind fest. Zwei punktweise `o(1)`-Aussagen reichen nach Multiplikation und Quadratwurzel für das feste Paar aus.

Status:

\[
\boxed{\checkmark[M]_{\rm mixed\ positive\text{-}remainder\ bound}.}
\]

---

# 5. Führender gemischter Konstantenmode-Term

Aus C4 für die beiden ersten Jets:

\[
\ell_T(f)
=
-\sqrt2\,c_m\beta_R^{(m)}(f)
\frac{e^{T/2}}{T^{m+1/2}}
(1+O(T^{-1})),
\]

\[
\ell_T(g)
=
-\sqrt2\,c_n\beta_R^{(n)}(g)
\frac{e^{T/2}}{T^{n+1/2}}
(1+O(T^{-1})).
\]

Daher

\[
\ell_T(f)\overline{\ell_T(g)}
=
2c_mc_n
\beta_R^{(m)}(f)
\overline{\beta_R^{(n)}(g)}
\frac{e^T}{T^{m+n+1}}
(1+O(T^{-1})).
\tag{TC1-MIX.21}
\]

Mit

\[
d_T=2T+O(1)
=2T(1+O(T^{-1}))
\]

folgt

\[
\boxed{
\rho_T(f,g)
=
 c_mc_n
\beta_R^{(m)}(f)
\overline{\beta_R^{(n)}(g)}
\frac{e^T}{T^{m+n+2}}
(1+O(T^{-1})).
}
\tag{TC1-MIX.22}
\]

Zusammen mit (TC1-MIX.13) und (TC1-MIX.20):

\[
\boxed{
\sigma_T(J_{R,T}f,J_{R,T}g)
=
 c_mc_n
\beta_R^{(m)}(f)
\overline{\beta_R^{(n)}(g)}
\frac{e^T}{T^{m+n+2}}
(1+o(1)).
}
\tag{TC1-MIX.23}
\]

Damit ist der korrigierte TC1-MIX-Satz bewiesen.

Status:

\[
\boxed{\checkmark[M]_{\rm TC1\text{-}MIX}.}
\]

---

# 6. Konsistenzcheck: same-jet O3g

Für `m=n` reduziert (TC1-MIX.23) exakt auf

\[
\sigma_T(Jf,Jg)
=
 c_m^2
 \beta_R^{(m)}(f)
 \overline{\beta_R^{(m)}(g)}
 \frac{e^T}{T^{2m+2}}
 (1+o(1)),
\]

also auf die in O3g §6 committed same-jet Polarisation.

Der neue Satz ist daher eine echte Erweiterung von O3g und kein konkurrierender Normalisierungszweig.

---

# 7. Welche O3d-I2-Bausteine wirklich bilinearisiert werden müssen

Die Ausgangsfrage fragte nach Constant-Mode-Paarung, Full-Rest-Dualisierung, signed future-edge certificate und Prime-Zellquadratur.

## 7.1 Constant-Mode-Paarung

Sie ist exakt bilinear und liefert den Hauptterm:

\[
\rho_T(f,g)
=
\frac{\ell_T(f)\overline{\ell_T(g)}}{d_T}.
\]

Status: `✓[M]`.

## 7.2 Full-Rest-Dualisierung

Die Infimumsdarstellung aus O3d-I1/I2 ist quadratisch und sollte **nicht** direkt polarisiert werden. Autoritativ bilinear ist stattdessen die äquivalente Operatorform

\[
\sigma_T(Jf,Jg)
=
\langle h_T(f),A_T^{-1}h_T(g)\rangle.
\]

Sie erlaubt die exakte positive Abspaltung (TC1-MIX.15).

Status: `✓[M]` für die benötigte bilineare Verwendung.

## 7.3 Signed future-edge certificate

Kein eigener gemischter signed-edge-Zeuge ist erforderlich. O3d-I2 benutzt den signed certificate, um für jeden festen Einzelvektor den Diagonalrest gegenüber der Konstantenmode auf `o(\Lambda_{f,T})` zu drücken. Positivität von `D_T` überträgt diese beiden Diagonalabschätzungen automatisch auf den gemischten Rest.

Status: `✓[M]` indirekt ausreichend.

## 7.4 Prime-Zellquadratur und Full-Rest-Lift

Auch diese müssen nicht paarweise neu konstruiert werden. Ihre committed Einzelvektorfehler fließen in (TC1-MIX.18)/(TC1-MIX.19) ein; Cauchy-Schwarz erledigt danach den Cross-Term.

Status: `✓[M]` indirekt ausreichend.

---

# 8. Asymptotische Winkel

Aus O3d-I2 diagonal und TC1-MIX gemischt:

\[
\sigma_T(Jf,Jf)^{1/2}
\sim
c_m|\beta_R^{(m)}(f)|
\frac{e^{T/2}}{T^{m+1}},
\]

\[
\sigma_T(Jg,Jg)^{1/2}
\sim
c_n|\beta_R^{(n)}(g)|
\frac{e^{T/2}}{T^{n+1}}.
\]

Daher

\[
\boxed{
\frac{\sigma_T(Jf,Jg)}
{\sigma_T(Jf,Jf)^{1/2}\sigma_T(Jg,Jg)^{1/2}}
\to
\frac{\beta_R^{(m)}(f)\overline{\beta_R^{(n)}(g)}}
{|\beta_R^{(m)}(f)|\,|\beta_R^{(n)}(g)|}.
}
\tag{TC1-MIX.24}
\]

Somit

\[
\boxed{
\left|
\frac{\sigma_T(Jf,Jg)}
{\sigma_T(Jf,Jf)^{1/2}\sigma_T(Jg,Jg)^{1/2}}
\right|\to1.
}
\tag{TC1-MIX.25}
\]

Äquivalent:

\[
\boxed{
\sigma_T(Jf,Jf)\sigma_T(Jg,Jg)
-|\sigma_T(Jf,Jg)|^2
=
o\!\left(
\sigma_T(Jf,Jf)\sigma_T(Jg,Jg)
\right).
}
\tag{TC1-MIX.26}
\]

Dies ist ein echter neuer geometrischer Befund: auf jedem festen glatten odd Paar wird die terminale Schurgeometrie nach individueller Normierung asymptotisch rank-one.

**Firewall:** `fixed-vector asymptotically rank-one` ist keine Operatornorm-Aussage und keine uniforme Rank-one-Approximation auf der odd Einheitskugel.

---

# 9. Warum dies den Cross-Terminal-Kern noch nicht schließt

Der direkte Terminaltransport lautet

\[
W_{R,S}^{[T]}
=
G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2},
\]

und der Cross-Terminal-Kern

\[
K_{R,S}^{T,U}
=
G_{R,T}^{-1/2}J_{R,S}^*
G_{S,T}^{1/2}G_{S,U}^{1/2}
J_{R,S}G_{R,U}^{-1/2}.
\]

TC1-MIX kontrolliert feste `f,g` in der wachsenden Formgeometrie. In `K_{R,S}^{T,U}` treten dagegen `T`- und `U`-abhängige inverse Quadratwurzeln auf. Diese können schwache bzw. subleading Richtungen verstärken.

Das ist hier besonders relevant, weil TC1-MIX selbst zeigt, dass die führende normierte feste-Vektor-Gramgeometrie rank-one kollabiert. Der führende Gramterm ist daher gerade **nicht invertierbar** auf mehrdimensionalen Jetfamilien. Die inverse Quadratwurzel wird von den nächsten Jetlagen / Resttermen mitbestimmt.

Daher ist die Implikation

\[
\text{TC1-MIX}
\Longrightarrow
K_{R,S}^{T,U}\to I
\]

nicht bewiesen.

Status:

\[
\boxed{?[O]_{K_{R,S}^{T,U}\to I}.}
\]

---

# 10. Gestufte Jet-Expansion: was jetzt bewiesen ist und was nicht

C4 liefert für `\ell_T(f)` eine beliebig tiefe `1/T`-Expansion in den Integral-Jets. Damit besitzt der **Rank-one-Anteil**

\[
\rho_T(f,g)
=
\frac{\ell_T(f)\overline{\ell_T(g)}}{d_T}
\]

eine entsprechende gemischte Jetstruktur.

Für den vollständigen Schurterm kennen wir aus diesem Audit jedoch nur

\[
D_T(f,g)
=
o\!\left(\frac{e^T}{T^{m+n+2}}\right)
\]

auf der ersten nichtverschwindenden gemischten Skala.

Dies reicht für TC1-MIX, aber nicht für eine vollständige Expansion

\[
\sigma_T(Jf,Jg)
\stackrel?=
 e^T\sum_{r,s\ge0}
 A_{r,s}
 \beta_R^{(r)}(f)
 \overline{\beta_R^{(s)}(g)}
 T^{-r-s-2}
+\cdots.
\]

Für die nächsten Koeffizienten wäre eine **quantifizierte** Restabschätzung für `D_T` nötig, nicht nur `o(1)` relativ zur ersten geometrischen Mixed-Skala.

Status:

\[
\boxed{?[O]_{\rm full\ graded\ mixed\text{-}jet\ expansion}.}
\]

---

# 11. Nächstes direktes Gate

TC1-MIX legt einen konkreten nächsten Terminalschritt nahe, ohne ihn zu behaupten:

> **Uniformes finite-jet Gram-/Square-root-Gate.** Auf einem festen endlichdimensionalen, jet-adaptierten glatten odd Unterraum ist eine hinreichend tiefe, uniform kontrollierte gestufte Gram-Asymptotik zu beweisen, sodass nicht nur `G_{R,T}`, sondern die relevanten `G_{R,T}^{\pm1/2}` nach Jet-Reskalierung kontrolliert werden können.

Der Grund ist strukturell: Der jetzt bewiesene Leading-Mixed-Term ist rank-one. Für Quadratwurzeln und insbesondere inverse Quadratwurzeln sind deshalb die subleading Eigenrichtungen unvermeidlich.

Noch **kein** neuer TC2-/TC1-SQRT-Knoten wird aus dieser Beobachtung automatisch eröffnet.

---

# 12. Auditorischer Gegencheck

Die folgenden Fehlerquellen wurden explizit geprüft:

1. **Falsche Terminalskala:** Die Übergabe enthielt `T^{2m+2}e^T`; autoritativ O3d-I2 ist `e^T/T^{2m+2}`. Korrigiert.
2. **Fehlende komplexe Konjugation:** O3g/C5 verwenden die Konvention `beta(f) overline{beta(g)}`. Korrigiert.
3. **Naive Polarisation:** für `m<n` reicht Leading-Diagonal-`o(1)` nicht. Durch abstraktes positives `2x2`-Modell bestätigt.
4. **Positivität des Restes:** nicht angenommen, sondern exakt durch orthogonale Projektion von `A_T^{-1/2}h_T(f)` auf `A_T^{1/2}1_T` bewiesen.
5. **Uniformitätsleck:** der Beweis benutzt nur feste `f,g`; keine Aussage über `T`-abhängige Vektoren wird still ergänzt.
6. **Infimumspolarisation:** vermieden. Die Full-Rest-Infimumsform wird nur über ihre bereits committed Operatoridentität benutzt.
7. **Gamma-Term:** TC1-MIX ist zunächst ein Satz über den terminalabhängigen Schurterm. Ein fester Gamma-Cross-Term ist gegenüber der exponentiell divergierenden Mixed-Skala vernachlässigbar, wird aber für den Square-root-Transport nicht als irrelevant deklariert.
8. **Cross-Terminal-Sprung:** aus fixed-terminal bilinearer Asymptotik wird keine Aussage über `T,U`-gemischte Quadratwurzeln abgeleitet.

Endurteil vor externem Countercheck:

\[
\boxed{
[P11\text{-}TC1\text{-}MIX]
\quad
\checkmark[M]_{\rm direct\ audit}
\;+
?[O]_{\rm independent\ countercheck/reconciliation}.
}
\]
