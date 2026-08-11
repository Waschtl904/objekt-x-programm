# P11-O3h — Rough-Complement-Witness, derivative-freie I2-Kosten und Prime-Quadrature-Regularitaetsgate

**Datum:** 2026-08-11  
**Knoten:** `[P11-O3h]`  
**Vorgaenger:** O3d-I2, O3g  
**Direkte Schnittstellen:** C1z-B1, C4, C5, C5c, O3d-I2, O3g  
**Modus:** `PASS-A ACTIVE`  
**Scope-Firewall:** kein O4, kein tatsaechlicher polynomialer `nu_2`-Witness, kein Theta-No-Go, kein starker odd Terminaltransport, kein SYN, kein Seal.

---

## 0. Urteil

O3g reduzierte den polynomialen Second-Moment-Witness auf die Existenz eines festen glatten odd Vektors im `T_0`-Gram-Komplement

\[
\mathcal C^-_{S,T_0}(R)
=
\ker(J_{R,S}^*G_{S,T_0})\cap\mathcal K^-_{X,S}.
\]

Der vorliegende Knoten zeigt, dass die dort verlangte `C_c^\infty`-Regularitaet deutlich zu stark ist.

Erstens existiert bereits **explizit** ein nichttrivialer kompakt getragener odd Komplementvektor, ohne irgendeine Regularitaet der Gram-Inversen vorauszusetzen.

Zweitens benoetigen die C4-Mittelwertasymptotik und die kontinuierlichen signed Future-Edge-Zertifikatskosten keine Ableitungen des Testvektors.

Drittens kann der C5c/I2-Prime-Quadraturschritt fuer jeden kompakt getragenen odd Vektor mit irgendeiner positiven Sobolev-Regularitaet

\[
E_Sg\in H^s(\mathbb R),\qquad s>0,
\]

durch eine derivative-freie Oszillationsabschaetzung geschlossen werden. Damit erweitert sich die scharfe I2-Asymptotik von `C_c^\infty` auf jeden festen kompakt getragenen odd `H^s`-Vektor, `s>0`.

Andererseits liefert die bereits committed Gamma-Graphrregularitaet aus C1z-B1 nur logarithmisches Frequenzwachstum:

\[
\boxed{
 g_\infty(\xi)\asymp \log(2+|\xi|).
}
\]

Daraus folgt **keine** automatische Einbettung der gesamten Gamma-Formdomaene in irgendein festes `H^s`, `s>0`.

Der O3g-Gate reduziert sich daher auf die wesentlich schwaechere, aber weiterhin echte Regularitaetsfrage

\[
\boxed{
\exists s>0:\quad
\mathcal C^-_{S,T_0}(R)
\cap H^s_c((-S,S))
\ne\{0\}
\ ?
}
\]

oder alternativ auf einen noch staerkeren rough-Prime-Quadratursatz, der ganz ohne positive Sobolev-Regularitaet auskommt.

Status:

\[
\boxed{
\begin{aligned}
[P11\text{-}O3h]
&\quad \checkmark[M]_{\rm explicit\ compact\ rough\ complement\ witness}\\
&+\checkmark[M]_{\rm C4\ boundary\ mean\ extends\ to\ compact\ L^2}\\
&+\checkmark[M]_{\rm derivative\text{-}free\ continuous\ signed\ certificate\ cost}\\
&+\checkmark[M]_{\rm oscillation\text{-}form\ prime\ quadrature}\\
&+\checkmark[M]_{\rm I2\ extends\ to\ compact\ H^s,\ s>0}\\
&+\checkmark[M]_{\rm Gamma\ symbol\ logarithmic\ growth}\\
&+\checkmark[M]_{\rm Gamma\ graph\ does\ not\ force\ positive\ Sobolev\ gain}\\
&+?[O]_{\rm positive\ Sobolev\ complement\ witness}\\
&+?[O]_{\rm rough\ L^2/log\text{-}graph\ prime\ quadrature}\\
&+?[O]_{\nu_2\ \rm polynomial\ lower\ witness}\\
&+?[O]_{\chi_-\|\Theta_-\|\to0}\\
&+?[O]_{W_{R,S,-}^{[T]}\ \rm strong\ Cauchy}.
\end{aligned}
}
\]

---

# 1. Verbindliche Daten aus O3g

Fixiere

\[
0<R<S<T_0.
\]

Schreibe

\[
G_R^0:=G_{R,T_0},
\qquad
G_S^0:=G_{S,T_0},
\qquad
J:=J_{R,S}.
\]

O3g definiert den rohen `T_0`-Gramprojektor

\[
\boxed{
\Pi^{\rm raw}
:=
J(G_R^0)^{-1}J^*G_S^0.
}
\tag{O3h.1}
\]

Aus der Pullback-Identitaet

\[
J^*G_S^0J=G_R^0
\]

folgt

\[
(\Pi^{\rm raw})^2=\Pi^{\rm raw}.
\]

Ferner gilt

\[
\boxed{
(I-\Pi^{\rm raw})\mathcal K^-_{X,S}
\subseteq
\mathcal C^-_{S,T_0}(R).
}
\tag{O3h.2}
\]

Alle beteiligten Operatoren respektieren die Paritaet.

---

# 2. Satz O3h.1 — expliziter kompakter rough-complement witness

Waehle einen nichttrivialen glatten odd Annulus-Vektor

\[
0\ne h\in C_c^\infty((-S,S)),
\qquad
h(-u)=-h(u),
\]

mit

\[
\operatorname{supp}h
\subset
(-S,-R-\delta)\cup(R+\delta,S)
\]

fuer ein festes `delta>0`.

Setze

\[
\boxed{
 g_h:=(I-\Pi^{\rm raw})h.
}
\tag{O3h.3}
\]

Dann gilt nach O3g

\[
\boxed{
 g_h\in\mathcal C^-_{S,T_0}(R).
}
\tag{O3h.4}
\]

Da

\[
\Pi^{\rm raw}h
\in
J\mathcal K^-_{X,R},
\]

ist `Pi^raw h` als rohe Source-Funktion in `[-R,R]` getragen. Auf dem Annulus gilt deshalb exakt

\[
g_h=h.
\]

Insbesondere

\[
\boxed{g_h\ne0.}
\tag{O3h.5}
\]

Außerdem ist

\[
\operatorname{supp}g_h
\subset
[-R,R]\cup\operatorname{supp}h
\Subset(-S,S).
\]

Somit existiert bereits ohne irgendeinen Smooth-Core-Satz ein **fester nichtzero kompakt getragener odd Gram-Komplementvektor**.

Die einzige offene Eigenschaft ist seine innere Regularitaet auf `[-R,R]`.

Nach C5 gilt auf dem gesamten odd Source-Sektor

\[
\bigcap_{m\ge0}\ker\beta_S^{(m)}
=\mathcal K^+_{X,S}.
\]

Da `g_h` odd und nichtzero ist, existiert daher ein endliches

\[
\boxed{
 m(g_h)
:=
\min\{m\ge0:\beta_S^{(m)}(g_h)\ne0\}<\infty.
}
\tag{O3h.6}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm explicit\ compact\ rough\ complement}.}
\]

---

# 3. C4-Mittelwertasymptotik benoetigt keine Glattheit

C4 beweist auf jedem festen Source-Fenster die uniforme Kernelentwicklung

\[
\Phi_T(r)
=
\sqrt2\,e^{T/2}T^{-1/2}
\sum_{j=0}^{M}\frac{c_j}{T^j}I_j(r)
+
O_{S,M}\!\left(e^{T/2}T^{-M-3/2}\right)
\]

uniform fuer `0<=r<=S`.

Die Hubkopplung lautet exakt

\[
\langle J_{S,T}f,H_T\mathbf1_T\rangle
=
-\int_{-S}^{S}\operatorname{sgn}(u)\Phi_T(|u|)f(u)\,du.
\]

Fuer jedes feste kompakt getragene `f in L^2(-S,S)` gilt

\[
\|f\|_1\le\sqrt{2S}\,\|f\|_2.
\]

Daher darf die uniforme C4-Entwicklung direkt gegen `f` integriert werden. Es folgt fuer jedes feste `M`

\[
\boxed{
\langle J_{S,T}f,H_T\mathbf1_T\rangle
=
-\sqrt2\,e^{T/2}T^{-1/2}
\sum_{j=0}^{M}
\frac{c_j}{T^j}\beta_S^{(j)}(f)
+
O_{S,M,\|f\|_2}
\!\left(e^{T/2}T^{-M-3/2}\right).
}
\tag{O3h.7}
\]

Insbesondere, falls `m=m(f)` der erste nichtverschwindende Jet ist,

\[
\boxed{
K_T(f)
\sim
-\sqrt2\,c_m\beta_S^{(m)}(f)
\frac{e^{T/2}}{T^{m+1/2}}.
}
\tag{O3h.8}
\]

Damit gilt die I2-Mittelwertskala auch fuer den rough complement witness `g_h`.

**Firewall:** (O3h.8) ist noch keine scharfe Asymptotik des vollen Schurterms. Dafuer muss der mean-zero Anteil noch diskret gescreent werden.

Status:

\[
\boxed{\checkmark[M]_{\rm rough\ C4\ mean\ asymptotic}.}
\]

---

# 4. Derivative-freie kontinuierliche signed-Zertifikatskosten

Sei nun allgemein

\[
f\in L^2(-S,S)
\]

odd und kompakt in `(-rho,rho)` getragen, `rho<S`.

Wie I2 setze fuer primitive Primzahlen

\[
a_p:=\frac12\log p,
\qquad
c_p:=\sqrt{\log p}\,p^{-3/4},
\qquad
d_p:=T-a_p,
\]

und

\[
\boxed{
 k_T(t)
:=-2\sum_{p}c_p f(t-d_p)
}
\tag{O3h.9}
\]

auf dem wachsenden Future-Block.

Setze

\[
A:=T-t.
\]

Dann

\[
k_T(T-A)
=-2\sum_pc_pf(a_p-A).
\]

Definiere

\[
F(u):=e^{u/4}f(u).
\]

Da `a_p=A+u`, gilt exakt

\[
\boxed{
 e^{-A/4}k_T(T-A)
=
-2\sum_p
\sqrt{\log p}\,p^{-7/8}
F(a_p-A).
}
\tag{O3h.10}
\]

Dies ist eine diskrete Faltung mit positiver Totalvariationsmasse

\[
S_T^{(7/8)}
:=
\sum_{p\le e^{2T}}
\sqrt{\log p}\,p^{-7/8}.
\]

Aus der elementaren Chebyshev-Schranke

\[
\pi(x)\ll \frac{x}{\log x}
\]

und partieller Summation beziehungsweise dyadischer Zerlegung folgt

\[
\boxed{
S_T^{(7/8)}
\ll
\frac{e^{T/4}}{\sqrt T}.
}
\tag{O3h.11}
\]

Youngs Ungleichung fuer endliche diskrete Masse liefert daher

\[
\begin{aligned}
\int_0^T e^{-A/2}|k_T(T-A)|^2dA
&\le
C\left(S_T^{(7/8)}\right)^2\|F\|_2^2\\
&\le
C_{S}\frac{e^{T/2}}{T}\|f\|_2^2.
\end{aligned}
\]

Da

\[
e^{-T}e^{t/2}=e^{-T/2}e^{-A/2},
\]

folgt

\[
\boxed{
 e^{-T}
\int_0^Te^{t/2}|k_T(t)|^2dt
\le
\frac{C_S}{T}\|f\|_2^2.
}
\tag{O3h.12}
\]

Dies ist dieselbe Future-Screening-Kostenskala wie I2.23, aber **ohne** `f'`, `k_T'` oder punktweise Glattheit.

Nach der Mittelwertabspaltung

\[
k_T^0=k_T-K_T/T
\]

kommt wie in I2 nur der zusaetzliche Term

\[
C\frac{|K_T|^2e^{-T/2}}{T^2}
\]

hinzu. Gegen

\[
M_T=\frac{|K_T|^2}{2T}
\]

ist dieser exponentiell klein.

Somit bleibt die kontinuierliche signed-Zertifikatsnorm fuer jeden festen kompakt getragenen odd `L^2`-Vektor

\[
\boxed{
\|Y_T^{\rm cont,-}\|^2=o(M_T).
}
\tag{O3h.13}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm derivative\text{-}free\ continuous\ cost}.}
\]

---

# 5. Derivative-freie Zellquadratur: Oszillationsform

C5c definiert fuer jede Future-Zelle `I`

\[
\lambda_q^{(I)}
=|I|\frac{w_q}{W_I}
\]

mit der exakten Massennormalisierung

\[
\sum_{q:r_q\in I}\lambda_q^{(I)}=|I|.
\]

Sei nun `Phi:I->H` eine normstetige Hilbertraum-wertige Funktion. Fuer ein beliebiges `r_I in I` gilt

\[
\begin{aligned}
&\left\|
\sum_{q:r_q\in I}\lambda_q^{(I)}\Phi(r_q)
-\int_I\Phi(r)dr
\right\|\\
&\le
\sum_q\lambda_q^{(I)}\|\Phi(r_q)-\Phi(r_I)\|
+\int_I\|\Phi(r)-\Phi(r_I)\|dr.
\end{aligned}
\]

Daher exakt

\[
\boxed{
\left\|
\sum_{q:r_q\in I}\lambda_q^{(I)}\Phi(r_q)
-\int_I\Phi(r)dr
\right\|
\le
2|I|\,\omega_\Phi(|I|),
}
\tag{O3h.14}
\]

wobei

\[
\omega_\Phi(\delta)
:=
\sup_{|r-r'|\le\delta}\|\Phi(r)-\Phi(r')\|.
\]

Dies ist die derivative-freie Version von C5c.29.

---

# 6. Oszillation des signed Edge-Vektors

Fuer den I2-signed Koeffizienten

\[
C_T^-(r,t)=2k_T^0(t)\alpha(2r-t)
\]

ist der zugehoerige Source-Vektor explizit

\[
\boxed{
\Phi_T^-(r)(x)
=
2k_T^0(x)\alpha(2r-x)
-
2k_T^0(2r-x)\alpha(x).
}
\tag{O3h.15}
\]

Die erste Komponente variiert nur ueber die feste glatte Anchorfunktion. Fuer `|r-r'|<=delta`:

\[
\|k_T^0(\cdot)
[\alpha(2r-\cdot)-\alpha(2r'-\cdot)]\|_2
\le
C_\alpha\delta\|k_T^0\|_2.
\]

Die zweite Komponente ist eine Translation von `k_T^0`. Daher

\[
\boxed{
\omega_{\Phi_T^-}(\delta)
\le
C_\alpha
\left(
\delta\|k_T^0\|_2
+
\omega_{k_T^0}(2\delta)
\right).
}
\tag{O3h.16}
\]

Der konstante Anteil `-K_T/T` besitzt Translationsoeszillation null; seine Anchorvariation ist bereits exponentiell harmlos wie in I2.46--I2.50.

Fuer den rauen Anteil gilt mit

\[
S_T^{(3/4)}
:=
\sum_{p\le e^{2T}}\sqrt{\log p}\,p^{-3/4}
\]

analog per Chebyshev/partieller Summation

\[
\boxed{
S_T^{(3/4)}
\ll
\frac{e^{T/2}}{\sqrt T}.
}
\tag{O3h.17}
\]

Young liefert

\[
\boxed{
\|k_T\|_2
\le
C\frac{e^{T/2}}{\sqrt T}\|f\|_2,
}
\tag{O3h.18}
\]

und fuer den L2-Translationsmodul

\[
\omega_f(h):=\|\tau_hE_Sf-E_Sf\|_2
\]

auch

\[
\boxed{
\omega_{k_T}(h)
\le
C\frac{e^{T/2}}{\sqrt T}\omega_f(h).
}
\tag{O3h.19}
\]

---

# 7. Prime-Zellweite und hinreichende Regularitaet

Auf dem gesamten I2-Future-Bereich gilt aus C5c/I2

\[
\boxed{
\delta_T:=\max_I|I|
\le
Ce^{-2T/5}.
}
\tag{O3h.20}
\]

Summiert man (O3h.14) ueber die Zellen und benutzt, dass die gesamte `r`-Laenge `O(T)` ist, folgt die robuste, wenn auch nicht optimierte Schranke

\[
\boxed{
\|Z_T^{\rm quad,rough}\|_2
\le
C T\,
\omega_{\Phi_T^-}(\delta_T).
}
\tag{O3h.21}
\]

Mit (O3h.16)--(O3h.19):

\[
\boxed{
\|Z_T^{\rm quad,rough}\|_2
\le
C e^{T/2}\sqrt T
\left[
\delta_T\|f\|_2
+
\omega_f(2\delta_T)
\right]
+
\text{constant-anchor term}.
}
\tag{O3h.22}
\]

Der constant-anchor term ist nach I2 exponentiell `o(sqrt(M_T))`.

Nun sei fuer irgendein festes `s>0`

\[
E_Sf\in H^s(\mathbb R).
\]

Dann gilt die Standardtranslationsabschaetzung

\[
\boxed{
\omega_f(h)
\le
C_s|h|^{\min\{s,1\}}\|E_Sf\|_{H^s}.
}
\tag{O3h.23}
\]

Wegen (O3h.20) ist die rechte Seite exponentiell klein in `T`. Daher fuer jedes feste `L>0`

\[
\boxed{
\|Z_T^{\rm quad,rough}\|_2
=o\!\left(e^{T/2}T^{-L}\right).
}
\tag{O3h.24}
\]

Ist `m=m(f)<infty`, so

\[
\sqrt{M_T}
\asymp
\frac{e^{T/2}}{T^{m+1}}.
\]

Mit `L=m+1` folgt

\[
\boxed{
\|Z_T^{\rm quad,rough}\|_2=o(\sqrt{M_T}).
}
\tag{O3h.25}
\]

Damit funktionieren die diskrete Future-Prime-Quadratur, der Full-Rest-Lift und der I2-Squeeze unveraendert.

Folglich:

## Satz O3h.2 — I2-Hs-Erweiterung

Sei `f` ein fester nichttrivialer kompakt getragener odd Vektor mit

\[
E_Sf\in H^s(\mathbb R)
\]

fuer irgendein `s>0`, und sei `m` sein erster nichtverschwindender Boundary-Jet. Dann gilt

\[
\boxed{
\sigma_T(J_{S,T}f)
=
c_m^2|\beta_S^{(m)}(f)|^2
\frac{e^T}{T^{2m+2}}
(1+o(1)).
}
\tag{O3h.26}
\]

Damit gilt auch die same-jet Polarisation aus O3g fuer solche `H^s`-Vektoren.

Status:

\[
\boxed{\checkmark[M]_{\rm I2\ extends\ to\ compact\ H^s,\ s>0}.}
\]

---

# 8. Gamma-Symbol waechst nur logarithmisch

C1z-B1 gibt exakt

\[
\boxed{
 g_\infty(\xi)
=
\sum_{j=0}^\infty
\frac{X^2}{a_j(a_j^2+X^2)},
\qquad
X:=|\xi|/2,
\qquad
a_j=j+\frac14.
}
\tag{O3h.27}
\]

Fuer `X>=2` zerlege bei `a_j<=X` und `a_j>X`.

Falls `a_j<=X`, gilt

\[
\frac{X^2}{a_j(a_j^2+X^2)}
\ge
\frac1{2a_j},
\]

und stets

\[
\frac{X^2}{a_j(a_j^2+X^2)}
\le
\frac1{a_j}.
\]

Daher

\[
\sum_{a_j\le X}
\frac{X^2}{a_j(a_j^2+X^2)}
\asymp
\sum_{a_j\le X}\frac1{a_j}
\asymp\log X.
\]

Fuer `a_j>X`:

\[
\frac{X^2}{a_j(a_j^2+X^2)}
\le
\frac{X^2}{a_j^3},
\]

und

\[
X^2\sum_{a_j>X}a_j^{-3}=O(1).
\]

Somit

\[
\boxed{
 c\log(2+|\xi|)
\le
1+g_\infty(\xi)
\le
C\log(2+|\xi|)
}
\tag{O3h.28}
\]

fuer feste universelle positive Konstanten `c,C`.

Die Gamma-Formdomaene ist damit auf Fourierseite aequivalent zu einer **logarithmischen Sobolev-Domaene**:

\[
\int
\log(2+|\xi|)
|\widehat{E_Rf}(\xi)|^2d\xi<\infty.
\]

---

# 9. Die bestehende Gamma-Graphnorm erzwingt kein positives Sobolev-s

Fuer ein festes

\[
0\ne\varphi\in C_c^\infty((-R,R))
\]

setze

\[
f_N(u)=e^{iNu}\varphi(u).
\]

Aus (O3h.28) folgt

\[
\|f_N\|_{\Gamma,R}^2
\asymp
\log N
\]

fuer `N->infty`, waehrend fuer jedes feste `s>0`

\[
\|E_Rf_N\|_{H^s}^2
\asymp
N^{2s}.
\]

Daher kann es keine konstante Einbettungsabschaetzung

\[
\|E_Rf\|_{H^s}
\le C_s\|f\|_{\Gamma,R}
\]

auf der gesamten Gamma-Formdomaene geben.

Da die Gamma-Formdomaene ein Hilbertraum ist und die Einbettung in `L^2` stetig ist, wuerde eine set-theoretische Inklusion der **gesamten** Domaene in `H^s` per Closed-Graph-Theorem eine stetige Einbettung erzwingen. Somit folgt sogar:

\[
\boxed{
\mathcal D_{\Gamma,R}
\not\subset H^s(-R,R)
\qquad\text{fuer jedes feste }s>0.
}
\tag{O3h.29}
\]

Da

\[
\mathcal K_{X,R}
=\mathcal D(q_{\Gamma,R})
\]

mit aequivalenter Graphnorm, liefert der vorhandene finite-level Objekt-X-Graphrraum **keinen automatischen positiven Sobolev-Gewinn**.

Status:

\[
\boxed{\checkmark[M]_{\rm no\ automatic\ positive\ Sobolev\ gain}.}
\]

---

# 10. Was die Gamma-Graphnorm dennoch liefert: logarithmischer Translationsmodul

Sei

\[
f\in\mathcal D_{\Gamma,R},
\qquad F=E_Rf.
\]

Dann

\[
\|\tau_hF-F\|_2^2
=
\frac1{2\pi}
\int
|e^{i\xi h}-1|^2|\widehat F(\xi)|^2d\xi.
\]

Setze

\[
M=h^{-1/2}.
\]

Auf `|xi|<=M` gilt

\[
|e^{i\xi h}-1|^2\le h^2\xi^2\le h.
\]

Auf `|xi|>M` benutzen wir (O3h.28). Da der gewichtete Fourier-Tail gegen null geht,

\[
\int_{|\xi|>M}|\widehat F(\xi)|^2d\xi
=
o\!\left(\frac1{\log M}\right).
\]

Daher

\[
\boxed{
\|\tau_hF-F\|_2
=
o\!\left((\log(1/h))^{-1/2}\right)
\qquad(h\downarrow0).
}
\tag{O3h.30}
\]

Auf der Future-Zellskala

\[
h\asymp e^{-2T/5}
\]

folgt lediglich

\[
\boxed{
\omega_f(h)=o(T^{-1/2}).
}
\tag{O3h.31}
\]

Dies ist echte Regularitaet, reicht aber fuer die robuste Quadraturabschaetzung (O3h.22) **nicht uniform fuer beliebige endliche Jetordnung `m`** aus.

**Firewall:** Einzelne Gram-Komplementvektoren koennen wesentlich regulaerer sein. O3h beweist nur, dass die bestehende Graphraumstruktur allein keinen solchen positiven Sobolev-Gewinn erzwingt.

---

# 11. Der neue atomare Gate

O3g verlangte noch

\[
\mathcal C^-_{S,T_0}(R)
\cap C_c^\infty((-S,S))
ne\{0\}.
\]

O3h ersetzt dies durch die strikt schwaechere hinreichende Bedingung

\[
\boxed{
\exists s>0:\quad
\mathcal C^-_{S,T_0}(R)
\cap
\{g:\operatorname{supp}g\Subset(-S,S),\ E_Sg\in H^s(\mathbb R)\}
\ne\{0\}.
}
\tag{O3h.32}
\]

Denn fuer einen solchen `g` liefert Satz O3h.2 die volle I2-Asymptotik, und O3g/O3f geben danach

\[
\nu_2(U)\gtrsim U^{-M}
\]

fuer ein endliches `M` und damit

\[
\chi_-\|\Theta_-\|\to+\infty.
\]

Alternativ wuerde ein neuer rough-Quadratursatz genuegen, der (O3h.25) fuer den expliziten rough complement witness `g_h` aus Satz O3h.1 direkt beweist, ohne `H^s` vorauszusetzen.

Damit verbleiben exakt zwei Routen:

\[
\boxed{
\text{Route H1: positiver Sobolev-Komplement-Witness}
}
\]

oder

\[
\boxed{
\text{Route H2: rough/log-graph Prime-Quadrature fuer }g_h.
}
\]

Keiner dieser beiden Saetze ist aktuell committed.

---

# 12. Persistente Firewalls

## O3h-FW1 — rough complement ist noch kein I2 witness

\[
 g_h\in\mathcal C^-_{S,T_0}(R),\quad g_h\ne0
\]

impliziert nicht automatisch

\[
\sigma_U(g_h)
\sim
c_m^2|\beta_m(g_h)|^2e^U/U^{2m+2}.
\]

Dafuer fehlt H1 oder H2.

## O3h-FW2 — logarithmische Gamma-Regularitaet ist nicht positive Sobolev-Regularitaet

Die kompakte Gamma-Einbettung aus C1z-B1 darf nicht als verstecktes `H^s`-Embedding gelesen werden.

## O3h-FW3 — kein Dichtheitskurzschluss

Aus

\[
C_c^\infty\text{ dicht in }\mathcal K_{X,S}
\]

und

\[
\mathcal C^-_{S,T_0}(R)\ne\{0\}
\]

folgt weiterhin nicht

\[
C_c^\infty\cap\mathcal C^-\ne\{0\}.
\]

## O3h-FW4 — selbst H1/H2 killt nur den O3-Produktkanal

Auch wenn H1 oder H2 den polynomialen `nu_2`-Witness schliesst und

\[
\chi_-\|\Theta_-\|\not\to0
\]

beziehungsweise sogar Divergenz beweist, folgt daraus noch nicht

\[
W_{R,S,-}^{[T]}
\text{ konvergiert nicht stark}.
\]

---

# 13. Naechster zulaessiger Primäraudit

Der naechste atomare Test ist jetzt **nicht** mehr die volle Smooth-Core-Erhaltung von

\[
G_{R,T_0}^{-1}.
\]

Stattdessen ist zuerst die wesentlich schwaechere Frage zu pruefen:

\[
\boxed{
\text{Erhaelt }\Pi^{\rm raw}_{R,S;T_0}
\text{ auf wenigstens einem odd Annulus-Witness irgendein }H^s,\ s>0?
}
\]

Falls nein oder nicht zugaenglich, ist Route H2 zu testen: eine direkte Prime-Zell-Quadratur auf der logarithmischen Gamma-Graphklasse.

**Kein O4, kein SYN, kein Seal.**
