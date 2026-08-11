# P11-O3g — Future-Cross-Gram-Witness und Smooth-Complement-Gate

**Datum:** 2026-08-11  
**Knoten:** `[P11-O3g]`  
**Vorgänger:** O3d-I2, O3e, O3f  
**Direkte Schnittstellen:** C4, C5, C5c, O3d-I2, O3f  
**Modus:** `PASS-A ACTIVE`  
**Scope-Firewall:** kein O4, kein tatsächlicher Polynomial-Witness für `nu_2`, kein Theta-No-Go, kein starker odd Terminaltransport, kein SYN, kein Seal.

---

## 0. Urteil

O3f hat den bisherigen O3-Produktkanal auf den dimensionslosen Second-Moment-Witness

\[
\nu_{2;R,S}^{T_0,U}
=
\frac{
\|W^*A_S^2W-A_R^2\|
}{
\|A_R\|\,\|A_S\|
}
=
\frac{\|\mathscr B\|^2}{\|A_R\|\,\|A_S\|}
\]

reduziert, wobei

\[
\mathscr B=(I-WW^*)A_SW.
\]

Der vorliegende Knoten reduziert `||mathscr B||` exakt auf einen **skalaren Future-Cross-Gram zwischen dem alten Raum und dem `T_0`-Gram-Komplement**.

Fixiere

\[
0<R<S<T_0<U
\]

und arbeite auf den odd Sektoren. Definiere das rohe `T_0`-Gram-Komplement

\[
\boxed{
\mathcal C^-_{S,T_0}(R)
:=
\ker\!\left(J_{R,S}^*G_{S,T_0}\right)
\cap \mathcal K^-_{X,S}.
}
\tag{O3g.1}
\]

Dann gilt exakt

\[
\boxed{
\|\mathscr B\|
=
\sup_{\substack{0\ne f\in\mathcal K^-_{X,R}\\
0\ne g\in\mathcal C^-_{S,T_0}(R)}}
\frac{
\left|
\left\langle
(G_{S,U}-G_{S,T_0})J_{R,S}f,
 g
\right\rangle
\right|
}{
\langle G_{R,T_0}f,f\rangle^{1/2}
\langle G_{S,T_0}g,g\rangle^{1/2}
}.
}
\tag{O3g.2}
\]

Außerdem besitzt die relative Zukunftsmetrik für feste Basen eine sehr grobe, aber ausreichende globale Operatornormabschätzung

\[
\boxed{
\|A_R\|+\|A_S\|
\le C_{R,S,T_0}\,Ue^U
\qquad(U\gg1).
}
\tag{O3g.3}
\]

Daraus folgt ein scharfer **konditionaler Abschlussmechanismus**.

Falls ein fester nichttrivialer glatter odd Vektor

\[
0\ne g
\in
\mathcal C^-_{S,T_0}(R)
\cap C_c^\infty((-S,S))
\]

existiert und sein erster nichtverschwindender Boundary-Jet Ordnung `m` besitzt, dann kann man nach C4/C5 einen festen glatten alten odd Vektor `f` mit demselben ersten Jet `m` wählen. Die Polarisation von O3d-I2 liefert dann

\[
\boxed{
\left\langle
(G_{S,U}-G_{S,T_0})J_{R,S}f,
 g
\right\rangle
=
C_{f,g}
\frac{e^U}{U^{2m+2}}
\bigl(1+o(1)\bigr),
\qquad C_{f,g}\ne0.
}
\tag{O3g.4}
\]

Damit

\[
\boxed{
\|\mathscr B\|
\gtrsim_{f,g}
\frac{e^U}{U^{2m+2}},
}
\tag{O3g.5}
\]

und aus (O3g.3)

\[
\boxed{
\nu_{2;R,S}^{T_0,U}
\gtrsim_{f,g}
U^{-(4m+6)}.
}
\tag{O3g.6}
\]

O3f würde dann sofort liefern

\[
\boxed{
\chi^{R,-}_{T_0,U}
\|\Theta^-_{T_0,U}\|
\longrightarrow +\infty,
}
\tag{O3g.7}
\]

also das Scheitern des bisherigen O3-Produktkanals.

**Aber:** Der aktuelle Repo-Stand beweist noch nicht die benötigte Regularitätsaussage

\[
\boxed{
\mathcal C^-_{S,T_0}(R)
\cap C_c^\infty((-S,S))
\ne\{0\}.
}
\tag{O3g.8}
\]

Das rohe Komplement selbst ist nichttrivial und sogar unendlichdimensional; offen ist die Existenz eines **I2-zulässigen glatten fixed complement witness**.

Status:

\[
\boxed{
\begin{aligned}
[P11\text{-}O3g]
&\quad \checkmark[M]_{\rm exact\ future\text{-}cross\text{-}Gram\ witness}\\
&+\checkmark[M]_{\rm crude\ global\ relative\ metric\ upper\ bound}\\
&+\checkmark[M]_{\rm I2\ same\text{-}jet\ polarization}\\
&+\checkmark[M]_{\rm smooth\ complement\ witness\Rightarrow polynomial\ nu_2}\\
&+?[O]_{\rm smooth\ odd\ T_0\text{-}Gram\ complement\ witness}\\
&+?[O]_{\nu_2\ \rm polynomial\ lower\ witness}\\
&+?[O]_{\chi_-\|\Theta_-\|\to0}\\
&+?[O]_{W_{R,S,-}^{[T]}\ \rm strong\ Cauchy}.
\end{aligned}
}
\]

---

# 1. Verbindliche Daten aus O3/O3f

Schreibe

\[
G_R^0:=G_{R,T_0},
\qquad
G_S^0:=G_{S,T_0},
\]

\[
A_R=(G_R^0)^{-1/2}G_{R,U}(G_R^0)^{-1/2},
\]

\[
A_S=(G_S^0)^{-1/2}G_{S,U}(G_S^0)^{-1/2},
\]

und

\[
W=(G_S^0)^{1/2}J_{R,S}(G_R^0)^{-1/2}.
\tag{O3g.9}
\]

O3/O3f liefern

\[
W^*W=I,
\qquad
P:=WW^*,
\tag{O3g.10}
\]

sowie

\[
\boxed{
\mathscr B:=(I-P)A_SW.
}
\tag{O3g.11}
\]

Da `W` isometrisch ist, ist `P` der orthogonale Projektor auf

\[
\mathcal M:=\operatorname{Ran}W.
\]

---

# 2. Das rohe `T_0`-Gram-Komplement

Da `(G_S^0)^{1/2}` beschränkt invertierbar ist und `(G_R^0)^{-1/2}` surjektiv ist,

\[
\mathcal M
=
(G_S^0)^{1/2}J_{R,S}\mathcal K^-_{X,R}.
\tag{O3g.12}
\]

Für `g\in\mathcal K^-_{X,S}` setze

\[
z=(G_S^0)^{1/2}g.
\]

Dann gilt für jedes `f\in\mathcal K^-_{X,R}`:

\[
\begin{aligned}
\left\langle
z,
(G_S^0)^{1/2}J_{R,S}f
\right\rangle
&=
\left\langle
G_S^0g,
J_{R,S}f
\right\rangle\\
&=
\left\langle
J_{R,S}^*G_S^0g,
f
\right\rangle.
\end{aligned}
\tag{O3g.13}
\]

Daher

\[
\boxed{
z\in\mathcal M^\perp
\iff
J_{R,S}^*G_S^0g=0.}
\tag{O3g.14}
\]

Also bildet

\[
(G_S^0)^{1/2}:
\mathcal C^-_{S,T_0}(R)
\longrightarrow
\mathcal M^\perp
\]

bijektiv ab.

Ferner

\[
\|z\|^2
=
\langle G_S^0g,g\rangle.
\tag{O3g.15}
\]

---

# 3. Exakte Future-Cross-Gram-Darstellung von `||mathscr B||`

Sei

\[
y=(G_R^0)^{1/2}f.
\]

Dann läuft `y` bijektiv durch den odd Source-Raum und

\[
\|y\|^2
=
\langle G_R^0f,f\rangle.
\tag{O3g.16}
\]

Außerdem

\[
Wy=(G_S^0)^{1/2}J_{R,S}f.
\tag{O3g.17}
\]

Daher

\[
\begin{aligned}
A_SWy
&=
(G_S^0)^{-1/2}
G_{S,U}
(G_S^0)^{-1/2}
(G_S^0)^{1/2}J_{R,S}f\\
&=
(G_S^0)^{-1/2}G_{S,U}J_{R,S}f.
\end{aligned}
\tag{O3g.18}
\]

Nimm nun `g\in\mathcal C^-_{S,T_0}(R)` und

\[
z=(G_S^0)^{1/2}g\in\mathcal M^\perp.
\]

Da `(I-P)z=z`:

\[
\begin{aligned}
\langle\mathscr By,z\rangle
&=
\langle(I-P)A_SWy,z\rangle\\
&=
\langle A_SWy,z\rangle\\
&=
\left\langle
(G_S^0)^{-1/2}G_{S,U}Jf,
(G_S^0)^{1/2}g
\right\rangle\\
&=
\boxed{
\langle G_{S,U}Jf,g\rangle.
}
\end{aligned}
\tag{O3g.19}
\]

Wegen `g\in ker(J^*G_S^0)` gilt zugleich

\[
\langle G_S^0Jf,g\rangle=0.
\tag{O3g.20}
\]

Also exakt

\[
\boxed{
\langle\mathscr By,z\rangle
=
\left\langle
(G_{S,U}-G_{S,T_0})Jf,g
\right\rangle.
}
\tag{O3g.21}
\]

Da `y` und `z` über die obigen Transformationen alle Vektoren des Source-Raums beziehungsweise von `M^perp` durchlaufen, folgt durch die übliche bilineare Operatornormcharakterisierung

\[
\boxed{
\|\mathscr B\|
=
\sup_{f,g}
\frac{
|\langle(G_{S,U}-G_{S,T_0})Jf,g\rangle|
}{
\langle G_R^0f,f\rangle^{1/2}
\langle G_S^0g,g\rangle^{1/2}
},
}
\tag{O3g.22}
\]

wobei das Supremum genau über

\[
0\ne f\in\mathcal K^-_{X,R},
\qquad
0\ne g\in\mathcal C^-_{S,T_0}(R)
\]

läuft.

Dies beweist (O3g.2).

Status:

\[
\boxed{\checkmark[M]_{\rm exact\ future\text{-}cross\text{-}Gram\ witness}.}
\]

---

# 4. Das rohe Komplement ist groß — Regularität ist die offene Stelle

Die unnormierte alte Einbettungsrange

\[
J_{R,S}\mathcal K^-_{X,R}
\subset
\mathcal K^-_{X,S}
\]

hat bei `R<S` unendliche Kodimension: bereits im zugrundeliegenden odd `L^2(-S,S)` liefert der äußere Annulus

\[
(-S,-R)\cup(R,S)
\]

einen unendlichdimensionalen komplementären Freiheitsraum.

Beschränkt invertierbare Gram-Transformationen ändern die Kodimension nicht. Daher ist

\[
\boxed{
\dim\mathcal C^-_{S,T_0}(R)=\infty.
}
\tag{O3g.23}
\]

Insbesondere existieren viele nichttriviale odd Komplementvektoren.

C5 beweist auf dem gesamten odd Source-Sektor die Vollständigkeit des Boundary-Jets:

\[
\bigcap_{m\ge0}\ker\beta_S^{(m)}
=
\mathcal K^+_{X,S}.
\tag{O3g.24}
\]

Daher besitzt jeder nichtzero odd `g\in\mathcal C^-_{S,T_0}(R)` irgendeinen endlichen ersten nichtverschwindenden Jet.

**Aber:** O3d-I2 wurde bislang für feste glatte odd Testvektoren bewiesen. Aus der bloßen Nichttrivialität von `mathcal C^-` folgt nicht automatisch

\[
\mathcal C^-_{S,T_0}(R)\cap C_c^\infty((-S,S))\ne\{0\}.
\]

Ein dichter glatter Unterraum kann abstrakt einen gegebenen abgeschlossenen Unterraum schlecht schneiden; hierzu braucht es einen eigenen Regularitätssatz für die feste `T_0`-Gram-Projektion.

Ein natürlicher roher `T_0`-Gram-Projektor auf die alte Einbettungsrange ist

\[
\boxed{
\Pi^{\rm raw}_{R,S;T_0}
:=
J_{R,S}
G_{R,T_0}^{-1}
J_{R,S}^*
G_{S,T_0}.
}
\tag{O3g.25}
\]

Aus der Cocycle-/Gramidentität

\[
J_{R,S}^*G_{S,T_0}J_{R,S}=G_{R,T_0}
\]

folgt

\[
(\Pi^{\rm raw})^2=\Pi^{\rm raw}.
\tag{O3g.26}
\]

Für jedes `h\in\mathcal K^-_{X,S}` ist

\[
\boxed{
g:=(I-\Pi^{\rm raw})h
\in
\mathcal C^-_{S,T_0}(R).
}
\tag{O3g.27}
\]

Damit wäre (O3g.8) insbesondere bewiesen, falls man für wenigstens ein glattes odd `h` außerhalb der alten Range zeigen kann, dass

\[
\Pi^{\rm raw}_{R,S;T_0}h
\]

wieder glatt ist.

Der aktuelle Repo-Stand enthält keinen solchen Smooth-Core-/Inverse-Metrik-Erhaltungssatz.

Status:

\[
\boxed{?[O]_{\rm smooth\ odd\ T_0\text{-}Gram\ complement\ witness}.}
\]

---

# 5. Grobe globale Operatornorm von `A_R` und `A_S`

Dieser Teil benötigt keine feine Primzahlsatz-Asymptotik.

Für Terminallevel `U` ist der Hub

\[
H_U
=
P_U
\sum_{p^k\le e^{2U}}
\sqrt{\log p}\,p^{-3k/4}
D_{k\log p}E_U.
\tag{O3g.28}
\]

Da

\[
\|P_U\|,\|E_U\|\le1,
\qquad
\|D_s\|\le2,
\]

folgt

\[
\|H_U\|
\le
2
\sum_{p^k\le e^{2U}}
\sqrt{\log p}\,p^{-3k/4}.
\tag{O3g.29}
\]

Setze `X=e^{2U}`.

Für `k=1` grob über alle ganzen Zahlen:

\[
\begin{aligned}
\sum_{p\le X}\sqrt{\log p}\,p^{-3/4}
&\le
\sqrt{\log X}
\sum_{2\le n\le X}n^{-3/4}\\
&\le
C\sqrt{\log X}\,X^{1/4}\\
&\le
C'\sqrt U\,e^{U/2}.
\end{aligned}
\tag{O3g.30}
\]

Für `k\ge2`:

\[
\sum_p\sum_{k\ge2}
\sqrt{\log p}\,p^{-3k/4}
\le
\sum_{n\ge2}
\sqrt{\log n}
\frac{n^{-3/2}}{1-n^{-3/4}}
<\infty.
\tag{O3g.31}
\]

Somit

\[
\boxed{
\|H_U\|
\le C\sqrt U\,e^{U/2}.
}
\tag{O3g.32}
\]

Der Schurterm besitzt

\[
\sigma_U(h)
=
\langle H_U^*h,(I+R_U^*R_U)^{-1}H_U^*h\rangle
\]

und wegen

\[
0\le(I+R_U^*R_U)^{-1}\le I
\]

folgt

\[
\sigma_U(h)
\le
\|H_U^*h\|^2
\le
\|H_U\|^2\|h\|^2.
\tag{O3g.33}
\]

Auf einer festen alten Basis `B\in\{R,S\}` ist der Gamma-Backbone ein fester beschränkter Formoperator; die feste Nullfortsetzung von `B` nach `U` hat ebenfalls eine basisabhängige, aber `U`-unabhängige Normkonstante. Daher

\[
\boxed{
\|G_{B,U}\|
\le C_{B}\,(1+Ue^U)
\le C_B' Ue^U.
}
\tag{O3g.34}
\]

Für

\[
A_B
=G_{B,T_0}^{-1/2}G_{B,U}G_{B,T_0}^{-1/2}
\]

und festes `T_0` folgt

\[
\boxed{
\|A_B\|
\le
\|G_{B,T_0}^{-1/2}\|^2\|G_{B,U}\|
\le
C_{B,T_0}Ue^U.
}
\tag{O3g.35}
\]

Damit (O3g.3).

Status:

\[
\boxed{\checkmark[M]_{\rm crude\ global\ relative\ metric\ upper\ bound}.}
\]

---

# 6. Polarisation der scharfen I2-Asymptotik auf gleicher Jetstufe

Seien

\[
a,b\in C_c^\infty((-S,S))\cap\mathcal K^-_{X,S}
\]

feste Vektoren mit

\[
\beta_S^{(j)}(a)=\beta_S^{(j)}(b)=0
\qquad(0\le j<m),
\tag{O3g.36}
\]

und

\[
\beta_S^{(m)}(a)\ne0,
\qquad
\beta_S^{(m)}(b)\ne0.
\tag{O3g.37}
\]

O3d-I2 liefert für jeden festen glatten odd Vektor `v` mit erstem Jet `r(v)`:

\[
\sigma_U(v,v)
=
 c_{r(v)}^2
 |\beta_S^{(r(v))}(v)|^2
 \frac{e^U}{U^{2r(v)+2}}
 (1+o_v(1)).
\tag{O3g.38}
\]

Wende die komplexe Polarisation auf

\[
a+b,\quad a-b,\quad a+ib,\quad a-ib
\]

an.

Falls bei einer dieser Kombinationen der `m`-te Jet zufällig verschwindet, liegt ihr erster Jet strikt oberhalb von `m`; dann ist ihr Diagonalterm

\[
o\!\left(\frac{e^U}{U^{2m+2}}\right).
\]

Daher erhält man unabhängig von solchen einzelnen Cancellation-Fällen

\[
\boxed{
\sigma_U(a,b)
=
 c_m^2
 \beta_S^{(m)}(a)
 \overline{\beta_S^{(m)}(b)}
 \frac{e^U}{U^{2m+2}}
 +
 o_{a,b}\!\left(\frac{e^U}{U^{2m+2}}\right).
}
\tag{O3g.39}
\]

Da der Gamma-Term terminalunabhängig und `G_{S,T_0}` fest ist,

\[
\boxed{
\left\langle
(G_{S,U}-G_{S,T_0})a,b
\right\rangle
=
 c_m^2
 \beta_S^{(m)}(a)
 \overline{\beta_S^{(m)}(b)}
 \frac{e^U}{U^{2m+2}}
 +o\!\left(\frac{e^U}{U^{2m+2}}\right).
}
\tag{O3g.40}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm I2\ same\text{-}jet\ polarization}.}
\]

---

# 7. Konditionaler polynomialer `nu_2`-Witness

Nehme nun zusätzlich an, es existiere

\[
0\ne g
\in
\mathcal C^-_{S,T_0}(R)
\cap C_c^\infty((-S,S)).
\tag{O3g.41}
\]

Nach C5 besitzt `g` einen endlichen ersten nichtverschwindenden Jet

\[
m=m(g).
\]

C4/C5 liefern einen festen

\[
f\in C_c^\infty((-R,R))\cap\mathcal K^-_{X,R}
\]

mit

\[
\beta_R^{(j)}(f)=0\;(j<m),
\qquad
\beta_R^{(m)}(f)\ne0.
\tag{O3g.42}
\]

Wegen Jet-Transition

\[
\beta_S^{(j)}(J_{R,S}f)=\beta_R^{(j)}(f),
\tag{O3g.43}
\]

haben `Jf` und `g` denselben ersten Jet `m`.

Aus (O3g.40):

\[
\left\langle
(G_{S,U}-G_{S,T_0})Jf,g
\right\rangle
=
C_{f,g}
\frac{e^U}{U^{2m+2}}
(1+o(1)),
\tag{O3g.44}
\]

mit

\[
C_{f,g}
=
 c_m^2
 \beta_R^{(m)}(f)
 \overline{\beta_S^{(m)}(g)}
\ne0.
\tag{O3g.45}
\]

Die beiden Nenner in (O3g.22) sind feste positive Konstanten. Also

\[
\boxed{
\|\mathscr B\|
\ge
c_{f,g}\frac{e^U}{U^{2m+2}}
}
\tag{O3g.46}
\]

für hinreichend großes `U`.

Damit

\[
\|\mathscr B\|^2
\gtrsim
\frac{e^{2U}}{U^{4m+4}}.
\tag{O3g.47}
\]

Aus (O3g.35):

\[
\|A_R\|\,\|A_S\|
\lesssim
U^2e^{2U}.
\tag{O3g.48}
\]

Folglich

\[
\boxed{
\nu_{2;R,S}^{T_0,U}
=
\frac{\|\mathscr B\|^2}{\|A_R\|\,\|A_S\|}
\gtrsim
U^{-(4m+6)}.
}
\tag{O3g.49}
\]

Dies ist ein tatsächlicher polynomialer Witness im Sinn von O3f.

Daher würde O3f/O3d-I2 dann sogar liefern

\[
\boxed{
\chi^{R,-}_{T_0,U}
\|\Theta^-_{T_0,U}\|
\to+\infty.
}
\tag{O3g.50}
\]

**Firewall:** Dieser Schluss ist derzeit konditional auf (O3g.41).

Status:

\[
\boxed{
\checkmark[M]_{\rm smooth\ complement\ witness\Rightarrow polynomial\ nu_2}.
}
\]

---

# 8. Der verbleibende atomare Gate

Nach O3g bleiben für diesen Route-Angriff nicht mehr mehrere asymptotische Größen offen.

Der zentrale neue Gate ist:

\[
\boxed{
\textbf{Smooth-Complement Gate:}
\qquad
\mathcal C^-_{S,T_0}(R)
\cap C_c^\infty((-S,S))
\stackrel{?}{\ne}\{0\}.
}
\tag{O3g.51}
\]

Eine hinreichende konkrete Unteraufgabe ist:

> Finde einen glatten odd Annulus-Testvektor `h` und beweise, dass der feste rohe Gram-Projektor
> \[
> \Pi^{\rm raw}_{R,S;T_0}
> =J G_{R,T_0}^{-1}J^*G_{S,T_0}
> \]
> `h` auf einen glatten alten Vektor abbildet.

Dann ist

\[
g=(I-\Pi^{\rm raw})h
\]

ein glatter odd Komplement-Witness. Weil `h` außerhalb der alten Nullfortsetzungsrange gewählt werden kann und `Pi_raw h` in der alten Range liegt, ist `g\ne0`.

Alternativ genügt jeder direkte Smooth-Core-Satz für

\[
\ker(J^*G_{S,T_0}).
\]

**Nicht zulässig:** Aus Dichtheit von `C_c^infty` allein die Existenz eines exakten glatten Komplementvektors folgern.

---

# 9. Persistente Firewalls

## O3g-FW1 — Kein tatsächlicher `nu_2`-Lower-Bound ohne Smooth-Complement-Gate

O3g beweist

\[
\text{smooth fixed complement witness}
\Longrightarrow
\nu_2\gtrsim U^{-M}.
\]

Es beweist noch nicht die linke Voraussetzung.

## O3g-FW2 — Kein Transport-No-Go

Selbst wenn der polynomial Witness geschlossen wird und

\[
\chi_-\|\Theta_-\|\not\to0,
\]

ist damit nur der bisherige hinreichende O3-Produktkanal ausgeschlossen.

Es folgt nicht automatisch

\[
W_{R,S,-}^{[T]}
\text{ konvergiert nicht stark}.
\]

## O3g-FW3 — Keine Dichtheitsabkürzung

Aus

\[
\dim\mathcal C^-_{S,T_0}(R)=\infty
\]

und der Dichtheit glatter odd Funktionen folgt abstrakt nicht ohne Zusatzstruktur

\[
\mathcal C^-_{S,T_0}(R)\cap C_c^\infty\ne\{0\}.
\]

## O3g-FW4 — Same-jet Polarisation

(O3g.39) wird nur für zwei feste glatte Vektoren verwendet, deren erster nichtverschwindender Jet dieselbe Ordnung `m` besitzt. Es wird keine allgemeine Cross-Asymptotik für unterschiedliche Jetordnungen behauptet.

---

# 10. Nächster zulässiger Arbeitsauftrag

Der nächste Primäraudit soll **nicht** erneut eine asymptotische Terminalrate untersuchen.

Er soll ausschließlich die feste finite-Horizon-Regularität von

\[
\Pi^{\rm raw}_{R,S;T_0}
=J G_{R,T_0}^{-1}J^*G_{S,T_0}
\]

auf dem glatten odd Core untersuchen.

Leitfrage:

\[
\boxed{
\exists\,0\ne h\in C_c^\infty((-S,S))\cap\mathcal K^-_{X,S}
\text{ außerhalb }J\mathcal K_{X,R}
:
\Pi^{\rm raw}_{R,S;T_0}h
\in C_c^\infty((-S,S))\ ?
}
\tag{O3g.52}
\]

Falls ja, ist Route A zum polynomialen `nu_2`-Witness im Wesentlichen geschlossen.

Falls nein oder nicht beweisbar, muss statt I2 auf glatten fixed complement witnesses eine schwächere Future-Cross-Gram-Technik für nichtglatte feste Komplementvektoren entwickelt werden.
