# P11-C1z-B2-C5 — Paritätszerlegung, Vollständigkeit des Boundary-Jets und exakter Cauchy-Kern des relativen Terminaltransports

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C5]`  
**Vorgänger:** C1z-B2-C4  
**Schnittstellen:** C1z-B/B1; C1z-B2-C2/C3/C4; P03-Haar-L2-Firewall  

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C5]
\quad
\checkmark[K/M]_{\rm part}
\;+
\checkmark[M]_{\rm neg,odd\text{-}terminal}
}
\]

mit fünf getrennten Befunden:

\[
\boxed{
\mathcal K_{X,R}
=
\mathcal K_{X,R}^{+}\oplus\mathcal K_{X,R}^{-}
\text{ ist eine exakte orthogonale Paritätszerlegung,}
}
\]

\[
\boxed{
J_{R,S},\ G_{R,T},\ G_{R,T}^{\pm1/2},\ V_{R,T},\ W_{R,S}^{[T]}
\text{ respektieren die Parität,}
}
\]

\[
\boxed{
\bigcap_{m\ge0}\ker\beta_R^{(m)}
=
\mathcal K_{X,R}^{+},
}
\]

also: der vollständige kanonische Boundary-Jet trennt exakt den gesamten ungeraden Source-Sektor,

\[
\boxed{
0\ne f\in C_c^\infty((-R,R)),\ f(-u)=-f(u)
\Longrightarrow
\langle G_{R,T}f,f\rangle_{X,R}\to+\infty,
}
\]

und schließlich

\[
\boxed{
W_{R,S}^{[T]}\xrightarrow[T\to\infty]{\rm strong}?W_{R,S}^{[\infty]}
}
\]

bleibt offen, ist aber nun exakt auf einen **Cross-Terminal-Cauchy-Kern** beziehungsweise einen **relativen Gauge-Intertwining-Defekt** reduziert.

Der Knoten schließt also den relativen Transport noch nicht. Er zeigt aber, dass die C4-Randhierarchie kein kleiner Boundary-Sektor ist: Sie ist eine vollständige analytische Kodierung des ungeraden Source-Profils. Der verbleibende Transporttest zerfällt kanonisch in einen geraden und einen ungeraden Kanal.

---

# 0. Urteil

C1z-B2-C4 hatte die unendliche Rand-Jet-Hierarchie

\[
\beta_R^{(m)}(f)
=
\int_{-R}^{R}
\operatorname{sgn}(u)I_m(|u|)f(u)\,du,
\]

\[
I_m(r)=\int_0^r s^m e^{-s/2}\,ds,
\]

isoliert und gezeigt:

Wenn

\[
\beta_R^{(0)}(f)=\cdots=\beta_R^{(m-1)}(f)=0,
\qquad
\beta_R^{(m)}(f)\ne0,
\]

so gilt

\[
\sigma_T(J_{R,T}f)
\gtrsim
\frac{e^T}{T^{2m+3}}
\to\infty.
\]

Außerdem ist jeder Jetkoeffizient exakt transition-kompatibel:

\[
\beta_S^{(m)}J_{R,S}=\beta_R^{(m)}.
\]

Offen blieb, wie groß der durch alle Jetkoeffizienten erfasste Teil des Source-Raums wirklich ist und wie die vollständige Jetgeometrie in den relativen isometrischen Transport

\[
W_{R,S}^{[T]}
=G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}
\]

eingeht.

C5 beantwortet den ersten Punkt vollständig:

\[
\boxed{
\text{Der volle Boundary-Jet ist auf dem ungeraden Source-Sektor vollständig.}
}
\]

Es gibt also **keinen** nichttrivialen ungeraden Unterraum, der von allen `beta_R^{(m)}` unsichtbar wäre.

Damit folgt aus C4 unmittelbar:

\[
\boxed{
\text{Jeder nichtzero ungerade glatte Testvektor divergiert absolut in der Terminalmetrik.}
}
\]

Dies ist stärker als der finite-Jet-No-Go aus C4.

Gleichzeitig zeigt die exakte Paritätssymmetrie der gesamten C1z-B/B1-Geometrie, dass der relative Cauchy-Test in zwei orthogonale Probleme zerfällt:

\[
W_{R,S}^{[T]}
=
W_{R,S,+}^{[T]}
\oplus
W_{R,S,-}^{[T]}.
\]

Der ungerade Kanal trägt den vollständigen Boundary-Jet; der gerade Kanal wird von diesem Jet exakt nicht gesehen. Für den geraden Kanal folgt daraus **keine** terminale Beschränktheit — er ist lediglich durch die bisherige Konstantenmode nicht getestet.

Der relative Grenzwert bleibt offen, wird aber auf einen einzigen exakten Operator reduziert:

\[
\boxed{
\mathscr K_{R,S}^{T,U}
:=(W_{R,S}^{[T]})^*W_{R,S}^{[U]}.
}
\]

Für alle `f` gilt

\[
\boxed{
\|(W_{R,S}^{[U]}-W_{R,S}^{[T]})f\|_{X,S}^2
=2\|f\|_{X,R}^2
-2\operatorname{Re}\langle f,\mathscr K_{R,S}^{T,U}f\rangle_{X,R}.
}
\]

Damit ist der starke Cauchy-Test äquivalent zur asymptotischen Identität dieses Cross-Terminal-Kerns.

---

# 1. Reflexion auf dem Source-Raum

Für jedes `R>0` definiere die Reflexion

\[
\boxed{
(\mathsf P_Rf)(u):=f(-u),
\qquad |u|<R.
}
\tag{C1zB2C5.1}
\]

Dann

\[
\mathsf P_R^2=I,
\qquad
\mathsf P_R^*=\mathsf P_R
\]

auf `L^2(-R,R)`.

Die orthogonalen Haar-`L^2`-Paritätsprojektoren sind

\[
\boxed{
\Pi_R^\pm:=\frac12(I\pm\mathsf P_R).
}
\tag{C1zB2C5.2}
\]

Der gerade und ungerade Source-Unterraum lauten

\[
L_R^+:=\operatorname{Ran}\Pi_R^+,
\qquad
L_R^-:=\operatorname{Ran}\Pi_R^-.
\]

Die Frage ist, ob diese Zerlegung auch von der vollständigen C1z-Graphgeometrie respektiert wird.

---

# 2. Der Translationsdifferenzoperator wechselt die Parität

Für

\[
D_s=U_{s/2}-U_{-s/2}
\]

gilt wegen

\[
\mathsf P U_t=U_{-t}\mathsf P
\]

exakt

\[
\boxed{
\mathsf P D_s=-D_s\mathsf P.
}
\tag{C1zB2C5.3}
\]

Also:

- `D_s` bildet gerade Funktionen in ungerade ab;
- `D_s` bildet ungerade Funktionen in gerade ab.

Die Nullfortsetzung

\[
E_R:L^2(-R,R)\to L^2(\mathbb R)
\]

und die Restriktion

\[
P_R:L^2(\mathbb R)\to L^2(-R,R)
\]

intertwinen die jeweiligen Reflexionen.

Daher gilt für den Huboperator aus C1z-B1

\[
H_R
=P_R\sum_{p^k\le e^{2R}}
\sqrt{\log p}\,p^{-3k/4}D_{k\log p}E_R
\]

exakt

\[
\boxed{
H_R\mathsf P_R
=-\mathsf P_RH_R.
}
\tag{C1zB2C5.4}
\]

Ebenso

\[
\boxed{
H_R^*\mathsf P_R
=-\mathsf P_RH_R^*.
}
\tag{C1zB2C5.5}
\]

---

# 3. Parität des source-gekoppelten Restoperators

Der C1z-B-Projektor besitzt die Faserform

\[
\mathsf Q_R(u)\psi_{p,j}
=
1_{\{j<J_{p,R}(u)\}}\psi_{p,j},
\]

mit

\[
J_{p,R}(u)
=\max\left\{0,
\left\lfloor\frac{2(R-|u|)_+}{\log p}\right\rfloor
\right\}.
\]

Da `J_{p,R}(u)` nur von `|u|` abhängt,

\[
\boxed{
\mathsf Q_R(-u)=\mathsf Q_R(u).
}
\tag{C1zB2C5.6}
\]

Auf dem Restzielraum

\[
\mathscr Y_R^0
\subset
L^2((-R,R);K^0)
\]

definiere die Source-Reflexion

\[
(\widetilde{\mathsf P}_RF)(u):=F(-u).
\]

Für den konditionierten Restoperator

\[
R_Ra(u)
=
\sum_{p,k}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_Ra(u)
\otimes
\mathsf Q_R(u)\eta_{p,k}
\]

folgt aus (C1zB2C5.3) und (C1zB2C5.6):

\[
\boxed{
R_R\mathsf P_R
=-\widetilde{\mathsf P}_RR_R.
}
\tag{C1zB2C5.7}
\]

Daher

\[
\boxed{
\mathsf P_RR_R^*R_R
=R_R^*R_R\mathsf P_R.
}
\tag{C1zB2C5.8}
\]

Somit kommutiert auch

\[
B_R=(I+R_R^*R_R)^{-1}
\]

mit der Reflexion:

\[
\boxed{
[B_R,\mathsf P_R]=0.
}
\tag{C1zB2C5.9}
\]

Status: `✓[K/M]`.

---

# 4. Die Feshbach-Schurform ist paritätsinvariant

Der positive Schurterm lautet

\[
\sigma_R(f,g)
=
\langle H_R^*f,B_RH_R^*g\rangle.
\]

Mit (C1zB2C5.5) und (C1zB2C5.9):

\[
\begin{aligned}
\sigma_R(\mathsf P_Rf,\mathsf P_Rg)
&=
\langle -\mathsf P_RH_R^*f,
B_R(-\mathsf P_RH_R^*g)\rangle\\
&=
\langle H_R^*f,B_RH_R^*g\rangle.
\end{aligned}
\]

Also

\[
\boxed{
\sigma_R(\mathsf P_Rf,\mathsf P_Rg)
=\sigma_R(f,g).
}
\tag{C1zB2C5.10}
\]

Insbesondere verschwinden die gemischten Paritätsterme:

\[
\boxed{
\sigma_R(f_+,f_-)=0
\qquad
(f_+\in L_R^+,\ f_-\in L_R^-).
}
\tag{C1zB2C5.11}
\]

Denn aus Paritätsinvarianz folgt

\[
\sigma_R(f_+,f_-)
=
\sigma_R(f_+,-f_-)
=-\sigma_R(f_+,f_-).
\]

---

# 5. Auch der Gamma-Backbone ist paritätsinvariant

Der source-windowed Gammaformteil lautet

\[
q_{\Gamma,R}(f,g)
=
\langle f,g\rangle
+
\int_0^\infty
\omega_\infty(s)
\langle D_sE_Rf,D_sE_Rg\rangle\,ds.
\]

Da `D_s` die Parität wechselt, aber die `L^2`-Paarung dieselbe Parität verlangt,

\[
\boxed{
q_{\Gamma,R}(\mathsf P_Rf,\mathsf P_Rg)
=q_{\Gamma,R}(f,g).
}
\tag{C1zB2C5.12}
\]

und

\[
\boxed{
q_{\Gamma,R}(f_+,f_-)=0.
}
\tag{C1zB2C5.13}
\]

Damit ist auch die volle finite-level Form

\[
q_R^X=q_{\Gamma,R}+\sigma_R
\]

paritätsinvariant und orthogonal gespalten.

---

# 6. Exakte orthogonale Paritätszerlegung der Graphräume

Definiere

\[
\mathcal K_{X,R}^\pm
:=
\{f\in\mathcal K_{X,R}:\mathsf P_Rf=\pm f\}.
\]

Da `mathsf P_R` bezüglich `q_R^X` unitär ist, sind beide Unterräume geschlossen und

\[
\boxed{
\mathcal K_{X,R}
=
\mathcal K_{X,R}^{+}
\oplus^{\perp_X}
\mathcal K_{X,R}^{-}.
}
\tag{C1zB2C5.14}
\]

Die Projektoren `Pi_R^pm` sind daher nicht nur Haar-`L^2`-orthogonal, sondern auch orthogonal bezüglich des `X`-Graphskalarprodukts.

Status:

\[
\boxed{\checkmark[K/M].}
\]

Diese Zerlegung war in C4 nur als Beobachtung der `beta`-Funktionale sichtbar; sie ist tatsächlich eine Symmetrie der gesamten C1z-B/B1-Geometrie.

---

# 7. Nullfortsetzungen intertwinen die Parität

Für `R<S` gilt für die native Nullfortsetzung

\[
J_{R,S}f=E_{R,S}f
\]

exakt

\[
\boxed{
J_{R,S}\mathsf P_R
=\mathsf P_SJ_{R,S}.
}
\tag{C1zB2C5.15}
\]

Da `mathsf P_R` und `mathsf P_S` unitär bezüglich der jeweiligen `X`-Skalarprodukte sind, folgt für den Adjungierten

\[
\boxed{
J_{R,S}^*\mathsf P_S
=\mathsf P_RJ_{R,S}^*.
}
\tag{C1zB2C5.16}
\]

Daher kommutiert der Metrikoperator

\[
G_{R,S}=J_{R,S}^*J_{R,S}
\]

mit der Reflexion:

\[
\boxed{
[G_{R,S},\mathsf P_R]=0.
}
\tag{C1zB2C5.17}
\]

Durch stetige Funktionalkalkül folgt ebenso

\[
\boxed{
[G_{R,S}^{\pm1/2},\mathsf P_R]=0.
}
\tag{C1zB2C5.18}
\]

---

# 8. Polar- und Terminal-Gauge-Isometrien sind paritätsverträglich

Für

\[
V_{R,S}=J_{R,S}G_{R,S}^{-1/2}
\]

gilt aus (C1zB2C5.15) und (C1zB2C5.18):

\[
\boxed{
V_{R,S}\mathsf P_R
=\mathsf P_SV_{R,S}.
}
\tag{C1zB2C5.19}
\]

Ebenso für jedes `T>=S`:

\[
W_{R,S}^{[T]}
=G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}
\]

und daher

\[
\boxed{
W_{R,S}^{[T]}\mathsf P_R
=\mathsf P_SW_{R,S}^{[T]}.
}
\tag{C1zB2C5.20}
\]

Somit zerfällt

\[
\boxed{
W_{R,S}^{[T]}
=
W_{R,S,+}^{[T]}
\oplus
W_{R,S,-}^{[T]}
}
\tag{C1zB2C5.21}
\]

in zwei isometrische Paritätskanäle

\[
W_{R,S,\pm}^{[T]}:
\mathcal K_{X,R}^{\pm}
\to
\mathcal K_{X,S}^{\pm}.
\]

Damit ist der relative Terminal-Cauchy-Test exakt in zwei unabhängige Probleme zerlegt.

---

# 9. Der Boundary-Jet sieht exakt nur den ungeraden Anteil

Aus C4:

\[
\beta_R^{(m)}(f)
=
\int_{-R}^{R}
\operatorname{sgn}(u)I_m(|u|)f(u)\,du.
\]

Da der Kern

\[
\operatorname{sgn}(u)I_m(|u|)
\]

ungerade ist,

\[
\boxed{
\beta_R^{(m)}(f_+)=0
\qquad
\forall f_+\in\mathcal K_{X,R}^{+}.
}
\tag{C1zB2C5.22}
\]

Für `f_-` ungerade gilt dagegen

\[
\boxed{
\beta_R^{(m)}(f_-)
=2\int_0^R I_m(r)f_-(r)\,dr.
}
\tag{C1zB2C5.23}
\]

Die C4-Hierarchie ist also ein reines ungerades Randdatum.

---

# 10. Vollständigkeitssatz des Boundary-Jets auf dem ungeraden Sektor

## Satz C1zB2C5.1

Sei

\[
f\in L^2(-R,R),
\qquad
f(-u)=-f(u).
\]

Falls

\[
\beta_R^{(m)}(f)=0
\qquad\forall m\ge0,
\]

dann

\[
\boxed{f=0.}
\tag{C1zB2C5.24}
\]

### Beweis

Auf `(0,R)` setze

\[
g(r):=f(r).
\]

Nach (C1zB2C5.23) ist für alle `m>=0`

\[
0
=\int_0^R I_m(r)g(r)\,dr.
\]

Mit

\[
I_m(r)=\int_0^r s^m e^{-s/2}\,ds
\]

und Fubini:

\[
\begin{aligned}
0
&=\int_0^R\int_0^r s^m e^{-s/2}g(r)\,ds\,dr\\
&=\int_0^R
s^m e^{-s/2}
\left(\int_s^R g(r)\,dr\right)ds.
\end{aligned}
\]

Definiere

\[
F(s):=\int_s^R g(r)\,dr.
\]

Da `g in L^2(0,R)`, ist `F` absolut stetig und insbesondere in `L^2(0,R)`.

Somit gilt für alle `m>=0`

\[
\int_0^R s^m F(s)e^{-s/2}\,ds=0.
\]

Polynome sind dicht in

\[
L^2((0,R),e^{-s/2}ds),
\]

also

\[
F(s)=0
\]

fast überall.

Da `F` absolut stetig ist,

\[
F'(s)=-g(s)=0
\]

fast überall. Also `g=0` und wegen Ungeradheit `f=0`. `□`

Status:

\[
\boxed{\checkmark[M].}
\]

---

# 11. Exakte Identifikation des gemeinsamen Jetkerns

Jedes `beta_R^{(m)}` ist auf `K_{X,R}` stetig.

Denn auf dem endlichen Intervall ist sein Kern beschränkt, also

\[
|\beta_R^{(m)}(f)|
\le C_{R,m}\|f\|_2
\le C_{R,m}\|f\|_{X,R}.
\]

Daher sind die Kerne abgeschlossen.

Aus (C1zB2C5.22) folgt

\[
\mathcal K_{X,R}^{+}
\subseteq
\bigcap_{m\ge0}\ker\beta_R^{(m)}.
\]

Sei umgekehrt

\[
f\in\bigcap_{m\ge0}\ker\beta_R^{(m)}.
\]

Schreibe

\[
f=f_++f_-.
\]

Da alle `beta` den geraden Anteil vernichten,

\[
\beta_R^{(m)}(f_-)=0
\qquad\forall m.
\]

Nach Satz C1zB2C5.1 ist `f_-=0` als `L^2`-Funktion.

Somit

\[
\boxed{
\bigcap_{m\ge0}\ker\beta_R^{(m)}
=
\mathcal K_{X,R}^{+}.
}
\tag{C1zB2C5.25}
\]

Dies ist die präzise Bedeutung von **vollständigem Boundary-Jet**.

Der unendliche Jet quotientiert nicht nur einen kleinen Randsektor. Würde man sämtliche Jetfunktionale auf null setzen, bliebe exakt nur die gerade Source-Geometrie übrig.

---

# 12. Der Boundary-Jet als eine einzige kanonische ganze Funktion

Die unendliche Folge kann kanonisch zu einer analytischen Randtransformierten resummiert werden.

Definiere für `z in C`

\[
\boxed{
\mathfrak B_R(z;f)
:=
\int_{-R}^{R}
\operatorname{sgn}(u)
\left(
\int_0^{|u|}e^{(z-1/2)s}\,ds
\right)
f(u)\,du.
}
\tag{C1zB2C5.26}
\]

Da `|u|<=R`, ist `mathfrak B_R(z;f)` eine ganze Funktion von `z`.

Ableiten unter dem Integral liefert

\[
\boxed{
\frac{d^m}{dz^m}\mathfrak B_R(0;f)
=\beta_R^{(m)}(f).
}
\tag{C1zB2C5.27}
\]

Für `z != 1/2` kann der innere Kern explizit geschrieben werden als

\[
\boxed{
\int_0^{|u|}e^{(z-1/2)s}\,ds
=
\frac{e^{(z-1/2)|u|}-1}{z-1/2}.
}
\tag{C1zB2C5.28}
\]

und bei `z=1/2` als `|u|`.

Damit gilt:

\[
\boxed{
\mathfrak B_R(\cdot;f)\equiv0
\iff
f\in\mathcal K_{X,R}^{+}.
}
\tag{C1zB2C5.29}
\]

Der vollständige Boundary-Jet ist also äquivalent zu einer einzigen kanonischen analytischen Source-Randtransformierten.

**Firewall:** Es wird keine Hilbertnorm auf dem Raum dieser ganzen Funktionen eingeführt. Eine solche Norm wäre eine neue Struktur und müsste source-kanonisch hergeleitet werden.

---

# 13. Exakte Transition-Kompatibilität der analytischen Randtransformierten

C4 bewies

\[
\beta_S^{(m)}J_{R,S}=\beta_R^{(m)}.
\]

Direkt aus Nullfortsetzung folgt sogar für die resummierte Form:

\[
\boxed{
\mathfrak B_S(z;J_{R,S}f)
=
\mathfrak B_R(z;f)
\qquad
\forall z\in\mathbb C.
}
\tag{C1zB2C5.30}
\]

Damit ist die vollständige ungerade Randtransformierte exakt kontravariant konstant entlang der nativen Source-Transitionen.

Dies ist stärker als die komponentenweise Aussage der einzelnen Jetkoeffizienten, aber logisch äquivalent zu ihr.

---

# 14. Konsequenz aus C4 + Jetvollständigkeit: jeder nichtzero ungerade Testvektor divergiert

Sei

\[
0\ne f\in C_c^\infty((-R,R)),
\qquad
f(-u)=-f(u).
\]

Nach Satz C1zB2C5.1 können nicht alle

\[
\beta_R^{(m)}(f)
\]

verschwinden.

Da die natürlichen Zahlen wohlgeordnet sind, existiert ein kleinster Index

\[
\boxed{
m(f):=\min\{m\ge0:\beta_R^{(m)}(f)\ne0\}.
}
\tag{C1zB2C5.31}
\]

Dann gelten

\[
\beta_R^{(0)}(f)=\cdots=\beta_R^{(m(f)-1)}(f)=0
\]

und

\[
\beta_R^{(m(f))}(f)\ne0.
\]

C4 liefert daher

\[
\boxed{
\sigma_T(J_{R,T}f)
\ge
c_f\frac{e^T}{T^{2m(f)+3}}
\longrightarrow+\infty.
}
\tag{C1zB2C5.32}
\]

Somit

\[
\boxed{
\langle G_{R,T}f,f\rangle_{X,R}
\to+\infty.
}
\tag{C1zB2C5.33}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm neg,odd\text{-}terminal}.}
\]

**Scope-Firewall:** Der Satz ist hier auf dem glatten kompakten ungeraden Testkern bewiesen, weil dort die C4-Asymptotik vorliegt. Er wird nicht ohne zusätzliche uniforme Abschätzung auf jeden Vektor der abgeschlossenen ungeraden Graphhälfte hochgestuft.

---

# 15. Der ungerade divergente Testkern ist dicht

C1z-B2-B bewies, dass `C_c^infty(-R,R)` ein Formkern für die source-windowed Gammaform ist.

Da

\[
q_R^X
\]

und

\[
q_{\Gamma,R}
\]

auf festem `R` äquivalente Graphnormen besitzen, ist `C_c^infty(-R,R)` auch dicht in `K_{X,R}`.

Die Paritätsprojektion

\[
\Pi_R^-f=\frac12(f-\mathsf P_Rf)
\]

erhält `C_c^infty`.

Daher ist

\[
\boxed{
C_{c,\rm odd}^\infty((-R,R))
\text{ dicht in }
\mathcal K_{X,R}^-.
}
\tag{C1zB2C5.34}
\]

Damit divergiert die absolute Zukunftsmetrik auf einem dichten Testkern des gesamten ungeraden Graphsektors.

Dies beweist noch keine gleichmäßige Operatoruntergrenze auf `K_{X,R}^-`, aber es schließt jede Interpretation aus, nach der die C3/C4-Randdivergenz nur eine dünne außergewöhnliche Menge ungerader Richtungen beträfe.

---

# 16. Der gerade Sektor bleibt eigenständig offen

Für

\[
f_+\in\mathcal K_{X,R}^+
\]

gilt

\[
\beta_R^{(m)}(f_+)=0
\qquad\forall m.
\]

Daraus folgt **nicht**

\[
\sup_T\langle G_{R,T}f_+,f_+\rangle<\infty.
\]

Warum nicht: Die gesamte C3/C4-Hierarchie wurde mit dem Variationsvektor

\[
\mathbf1_T
\]

extrahiert. Dieser erzeugt über den paritätswechselnden Hub einen ungeraden Source-Randterm.

Ein anderer Variationsvektor kann den geraden Source-Sektor testen und eine andere Divergenzhierarchie erzeugen.

Daher bleibt verbindlich:

\[
\boxed{
\text{Terminalverhalten von }G_{R,T}|_{\mathcal K_{X,R}^{+}}
\text{ ist }?[O].
}
\tag{C1zB2C5.35}
\]

Es wäre insbesondere falsch, die Gleichheit (C1zB2C5.25) als Beschränktheitssatz für den geraden Sektor zu lesen.

---

# 17. Der relative Transport als relative Lage verschachtelter Polarbildräume

Für `R<T` sei wie in C1/C2

\[
V_{R,T}
:=J_{R,T}G_{R,T}^{-1/2}
:\mathcal K_{X,R}\to\mathcal K_{X,T}.
\]

Dies ist eine Isometrie mit

\[
\operatorname{Ran}V_{R,T}
=
\operatorname{Ran}J_{R,T}.
\]

Für `R<S<T` gilt wegen

\[
J_{R,T}=J_{S,T}J_{R,S}
\]

die Bildrauminklusion

\[
\boxed{
\operatorname{Ran}V_{R,T}
\subseteq
\operatorname{Ran}V_{S,T}.
}
\tag{C1zB2C5.36}
\]

Nun berechnen wir:

\[
\begin{aligned}
V_{S,T}^*V_{R,T}
&=
G_{S,T}^{-1/2}
J_{S,T}^*J_{R,T}
G_{R,T}^{-1/2}\\
&=
G_{S,T}^{-1/2}
J_{S,T}^*J_{S,T}J_{R,S}
G_{R,T}^{-1/2}\\
&=
G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}.
\end{aligned}
\]

Also

\[
\boxed{
W_{R,S}^{[T]}
=V_{S,T}^*V_{R,T}.
}
\tag{C1zB2C5.37}
\]

Da `Ran V_{R,T}` in `Ran V_{S,T}` liegt,

\[
V_{S,T}V_{S,T}^*V_{R,T}=V_{R,T},
\]

und damit

\[
\boxed{
V_{R,T}
=V_{S,T}W_{R,S}^{[T]}.
}
\tag{C1zB2C5.38}
\]

**Interpretation.** `W_{R,S}^{[T]}` ist die eindeutige isometrische Koordinatenabbildung, die den kleineren Polarbildraum im gemeinsamen Terminalraum `K_{X,T}` relativ zum größeren Polarbildraum beschreibt.

Der relative Transport ist damit keine künstliche Quadratwurzelkombination, sondern eine exakte geometrische Winkel-/Koordinatenabbildung zwischen verschachtelten Terminalbildern.

Status: `✓[M]`.

---

# 18. Cross-Terminal-Cauchy-Kern

Fixiere

\[
R<S
\]

und zwei Terminalhorizonte

\[
U,T>S.
\]

Definiere

\[
\boxed{
\mathscr K_{R,S}^{T,U}
:=(W_{R,S}^{[T]})^*W_{R,S}^{[U]}
\in\mathcal B(\mathcal K_{X,R}).
}
\tag{C1zB2C5.39}
\]

Da beide `W` Isometrien sind,

\[
\boxed{
\|\mathscr K_{R,S}^{T,U}\|\le1.
}
\tag{C1zB2C5.40}
\]

Setzt man die explizite Terminal-Gauge-Formel ein, erhält man

\[
\boxed{
\mathscr K_{R,S}^{T,U}
=
G_{R,T}^{-1/2}
J_{R,S}^*
G_{S,T}^{1/2}G_{S,U}^{1/2}
J_{R,S}
G_{R,U}^{-1/2}.
}
\tag{C1zB2C5.41}
\]

Diese Formel enthält exakt die nichtkommutative Cross-Terminal-Information, die weder aus den einzelnen quadratischen Formen `G_{R,T}` noch aus den einzelnen Boundary-Jet-Untergrenzen sichtbar ist.

---

# 19. Exakte Cauchy-Identität

Für jedes

\[
f\in\mathcal K_{X,R}
\]

gilt wegen der Isometrie beider `W`:

\[
\begin{aligned}
\|(W^{[U]}-W^{[T]})f\|_{X,S}^2
={}&
\|W^{[U]}f\|^2
+\|W^{[T]}f\|^2\\
&-2\operatorname{Re}\langle W^{[T]}f,W^{[U]}f\rangle\\
={}&
2\|f\|_{X,R}^2
-2\operatorname{Re}\langle f,
\mathscr K_{R,S}^{T,U}f\rangle_{X,R}.
\end{aligned}
\]

Also

\[
\boxed{
\|(W_{R,S}^{[U]}-W_{R,S}^{[T]})f\|_{X,S}^2
=
2\|f\|_{X,R}^2
-2\operatorname{Re}\langle f,
\mathscr K_{R,S}^{T,U}f\rangle_{X,R}.
}
\tag{C1zB2C5.42}
\]

Damit ist starke Cauchy-Konvergenz exakt äquivalent zu

\[
\boxed{
\operatorname{Re}\langle f,
\mathscr K_{R,S}^{T,U}f\rangle_{X,R}
\longrightarrow
\|f\|_{X,R}^2
}
\tag{C1zB2C5.43}
\]

für alle `f` in einem dichten Core, wenn `T,U->infty`.

Da alle `W` Norm `1` besitzen, genügt ein dichter Core: Cauchy-Konvergenz dort erweitert sich durch die uniforme Operatornorm automatisch auf ganz `K_{X,R}`.

Dies ist der schärfste bisherige C5-Test.

---

# 20. Parität des Cross-Terminal-Kerns

Aus (C1zB2C5.20) folgt

\[
W_{R,S}^{[T]}\mathsf P_R
=\mathsf P_SW_{R,S}^{[T]},
\]

und daher

\[
\boxed{
[\mathscr K_{R,S}^{T,U},\mathsf P_R]=0.
}
\tag{C1zB2C5.44}
\]

Somit

\[
\boxed{
\mathscr K_{R,S}^{T,U}
=
\mathscr K_{R,S,+}^{T,U}
\oplus
\mathscr K_{R,S,-}^{T,U}.
}
\tag{C1zB2C5.45}
\]

Der Cauchy-Test (C1zB2C5.43) kann und soll daher getrennt auf

\[
C_{c,\rm even}^\infty((-R,R))
\]

und

\[
C_{c,\rm odd}^\infty((-R,R))
\]

geführt werden.

Das ist nicht nur organisatorisch: Im ungeraden Kanal ist die vollständige absolute Divergenz bereits durch `mathfrak B_R` parametrisiert, im geraden Kanal existiert bisher keine entsprechende Randtransformierte.

---

# 21. Exakte Gauge-Wechsel-Formel

C2 definierte für `T<U`

\[
\boxed{
C_R^{T\to U}
:=
G_{R,U}^{1/2}G_{R,T}^{-1/2}.
}
\tag{C1zB2C5.46}
\]

Dann gilt exakt

\[
\boxed{
W_{R,S}^{[U]}
=
C_S^{T\to U}
W_{R,S}^{[T]}
(C_R^{T\to U})^{-1}.
}
\tag{C1zB2C5.47}
\]

Dies ist eine Ähnlichkeit, keine unitäre Konjugation im Allgemeinen.

Um die relative Aufhebung zu isolieren, definiere den Gauge-Intertwining-Defekt

\[
\boxed{
\mathscr E_{R,S}^{T,U}
:=
C_S^{T\to U}W_{R,S}^{[T]}
-
W_{R,S}^{[T]}C_R^{T\to U}.
}
\tag{C1zB2C5.48}
\]

Dann folgt unmittelbar aus (C1zB2C5.47):

\[
\boxed{
W_{R,S}^{[U]}-W_{R,S}^{[T]}
=
\mathscr E_{R,S}^{T,U}
(C_R^{T\to U})^{-1}.
}
\tag{C1zB2C5.49}
\]

Damit ist die gewünschte relative Cancellation mathematisch präzise formuliert:

Nicht die einzelnen Gauge-Inkremente

\[
C_R^{T\to U}
\]

müssen gegen `I` gehen — C3/C4 zeigen gerade, dass absolute Metrikfaktoren stark wachsen können.

Benötigt wird nur, dass die **Source- und Target-Gauge-Inkremente nach Transport asymptotisch miteinander intertwinen**.

Das ist die korrekte relative Form des C5-Problems.

---

# 22. Boundary-Jet-Kompatibilität ist notwendige Struktur, aber noch kein Cauchy-Beweis

Die gesamte analytische Randtransformierte erfüllt

\[
\mathfrak B_S(z;J_{R,S}f)
=
\mathfrak B_R(z;f).
\]

Dies zeigt, dass der bekannte divergente ungerade Source-Inhalt auf den Levels `R` und `S` exakt dieselben Randdaten trägt.

Das ist genau die Art von Kompatibilität, die eine relative Cancellation in

\[
G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}
\]

möglich macht.

Aber die C3/C4-Befunde sind bislang im Wesentlichen **skalare Variationsuntergrenzen** für

\[
\langle G_{R,T}f,f\rangle.
\]

Sie liefern noch keine operatorwertige asymptotische Entwicklung für

\[
G_{R,T}^{1/2}
\]

oder den Cross-Term

\[
G_{S,T}^{1/2}G_{S,U}^{1/2}.
\]

Daher folgt aus der Jet-Kompatibilität allein nicht

\[
\mathscr K_{R,S}^{T,U}\to I.
\]

Status:

\[
\boxed{?[O].}
\]

---

# 23. Abstrakte Firewall: finite-horizon Flachheit erzwingt keinen Terminalgrenzwert

Es ist wichtig, C2 nicht stärker zu lesen als bewiesen.

Ein abstraktes Hilbertbeispiel zeigt, dass

1. exakter Kokyklus der `J`;
2. positive invertierbare Metriken `G`;
3. exakte finite-horizon Terminal-Gauges;
4. Isometrie aller `W^{[T]}`;

allein **keine** Konvergenz von `W^{[T]}` erzwingen.

Nimm

\[
H_R=\mathbb C,
\qquad
H_S=\mathbb C^2,
\]

und die feste Inklusion

\[
jz=ze_1.
\]

Für eine Folge terminaler Horizonte `T_n` wähle positive invertierbare Matrizen

\[
A_n
=U_n
\begin{pmatrix}n^2&0\\0&1\end{pmatrix}
U_n^*,
\]

wobei `U_n` etwa zwischen `I` und einer festen Rotation um `pi/4` alterniert.

Setze

\[
L_n=A_n^{1/2},
\qquad
J_{S,T_n}=L_n,
\]

und für `m>n`

\[
J_{T_n,T_m}:=L_mL_n^{-1}.
\]

Dann ist der Kokyklus exakt.

Ferner

\[
G_{S,T_n}=A_n,
\qquad
G_{R,T_n}=j^*A_nj.
\]

Der Terminaltransport lautet

\[
W_{R,S}^{[T_n]}
=
A_n^{1/2}j(j^*A_nj)^{-1/2}.
\]

Dies ist jeweils eine Isometrie `C -> C^2`, aber ihre Bildrichtung alterniert asymptotisch zwischen verschiedenen Richtungen und besitzt daher keinen Grenzwert.

Damit:

\[
\boxed{
\text{C2-Flachheit allein}\not\Rightarrow
W^{[T]}\text{-Konvergenz}.
}
\tag{C1zB2C5.50}
\]

**Scope-Firewall:** Dies ist kein Gegenbeispiel gegen das konkrete C1z-System. Es zeigt nur, dass für C5 zwingend die konkrete source-/prime-/Feshbach-Asymptotik benutzt werden muss. Formale Hilbert-Kokyklusidentitäten reichen nicht.

---

# 24. Was C5 jetzt positiv abgeschlossen hat

Verbindlich bewiesen sind:

1. `q_R^X` ist exakt paritätsinvariant;
2. `K_{X,R}=K_{X,R}^+ \oplus K_{X,R}^-` orthogonal;
3. `J`, `G`, Quadratwurzeln, `V` und `W` intertwinen Parität;
4. der vollständige Boundary-Jet ist auf dem ungeraden Sektor vollständig;
5. gemeinsamer Jetkern = gerader Graphsektor;
6. der Jet besitzt die kanonische ganze Erzeugerfunktion `mathfrak B_R(z;f)`;
7. `mathfrak B_R` ist exakt transition-kompatibel;
8. jeder nichtzero ungerade glatte Testvektor divergiert absolut terminal;
9. `W^{[T]}=V_{S,T}^*V_{R,T}` und `V_{R,T}=V_{S,T}W^{[T]}`;
10. der starke Cauchy-Test ist exakt auf `mathscr K_{R,S}^{T,U}` reduziert;
11. äquivalent kann er als asymptotisches Intertwining der Gauge-Inkremente `C_R^{T->U}` formuliert werden.

Das ist ein substantieller Fortschritt, obwohl der eigentliche relative Grenzwert noch nicht geschlossen ist.

---

# 25. Was ausdrücklich offen bleibt

Nicht bewiesen sind:

1. starke Konvergenz von `W_{R,S,+}^{[T]}`;
2. starke Konvergenz von `W_{R,S,-}^{[T]}`;
3. irgendeine terminale Beschränktheit des geraden Sektors;
4. eine operatorwertige asymptotische Expansion von `G_{R,T}`;
5. ein Grenzwert des Cross-Terminal-Kerns `mathscr K`;
6. asymptotisches Verschwinden von `mathscr E`;
7. eine kanonische Hilbertnorm auf der analytischen Boundary-Transformierten `mathfrak B_R`;
8. eine Identifikation des relativen Transportlimes mit Objekt X;
9. exakte Weil-Realisierung;
10. P10-O07;
11. P04/Suzuki-Identifikation;
12. RH.

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal.

---

# 26. Strukturelle Interpretation

Die C1z-Grenzfrage besitzt jetzt drei klar getrennte Ebenen.

## Ebene I — absolute Metrik

Auf dem ungeraden Testkern:

\[
\boxed{
G_{R,T}\text{ bläst jede nichtzero glatte ungerade Richtung aus.}
}
\]

Die Divergenz ist nicht endlich-rangig, sondern durch eine vollständige analytische Randtransformierte parametrisiert.

## Ebene II — finite-horizon relative Geometrie

Für jedes endliche `T`:

\[
\boxed{
W_{R,S}^{[T]}
\text{ ist isometrisch und kokzyklisch.}
}
\]

## Ebene III — unendlicher relativer Horizont

Offen ist nur noch:

\[
\boxed{
\mathscr K_{R,S}^{T,U}\to I
\quad\text{beziehungsweise}\quad
W_{R,S}^{[T]}\text{ Cauchy?}
}
\]

Die bekannte Boundary-Divergenz ist dafür strukturell kompatibel, aber noch nicht operatoriell genug kontrolliert.

Die richtige Leitformel lautet daher nicht mehr

\[
G_{R,T}\to G_{R,\infty},
\]

sondern

\[
\boxed{
G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}
\stackrel{T\to\infty}{?}
W_{R,S}^{[\infty]}.
}
\]

---

# 27. Nächster atomarer Knoten

Der nächste Schritt darf nicht noch einen skalaren Divergenzzeugen suchen. C3/C4/C5 haben gezeigt, dass der ungerade absolute Rand bereits vollständig parametrisiert ist.

Erforderlich ist nun eine **operatorwertige** oder wenigstens **bilineare Cross-Terminal-Asymptotik**.

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C5a]
\quad
\text{Cross-Terminal-Overlap / relative Gauge defect auf dem Paritätscore}.
}
\]

Zu prüfen ist in dieser Reihenfolge:

### C5a-A — gerader Kanal

Für

\[
f,g\in C_{c,\rm even}^\infty((-R,R))
\]

untersuche direkt

\[
\langle f,\mathscr K_{R,S,+}^{T,U}g\rangle.
\]

Da der bekannte Boundary-Jet hier exakt verschwindet, ist dies der sauberste Test auf eine zweite, bisher unsichtbare Randhierarchie.

### C5a-B — ungerader Kanal

Für

\[
f,g\in C_{c,\rm odd}^\infty((-R,R))
\]

muss die vollständige analytische Randtransformierte `mathfrak B_R` in **Source und Target gleichzeitig** verfolgt werden. Ziel ist keine absolute Beschränktheit, sondern Cancellation im normalisierten Cross-Term.

### C5a-C — Gauge-Intertwining

Alternativ beziehungsweise äquivalent teste

\[
\boxed{
\mathscr E_{R,S}^{T,U}
(C_R^{T\to U})^{-1}
\stackrel?\longrightarrow0
}
\]

stark auf dem Paritätscore.

Ein positiver Nachweis auf beiden Paritätskernen würde wegen `||W||=1` automatisch auf den gesamten Graphraum fortsetzen und einen echten isometrischen Grenztransport liefern.

Damit ist der verbleibende Beweisbedarf für den relativen Objekt-X-Transport nun exakt lokalisiert:

\[
\boxed{
\text{Nicht mehr absolute Terminalmetrik, sondern Cross-Terminal-Overlap.}
}
\]
