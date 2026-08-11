# P11-O3i — Exaktes logarithmisches Translationsmodul-Gate und endliche Log-Regularitätsschwelle

**Datum:** 2026-08-11  
**Knoten:** `[P11-O3i]`  
**Vorgänger:** O3g, O3h  
**Direkte Schnittstellen:** C4, C5, C5c, O3d-I2, O3f, O3g, O3h  
**Modus:** `PASS-A ACTIVE`  
**Scope-Firewall:** kein O4, kein tatsächlicher polynomialer `nu_2`-Witness, kein Theta-No-Go, kein starker odd Terminaltransport, kein SYN, kein Seal.

---

## 0. Urteil

O3h reduzierte den früheren Smooth-Complement-Gate bereits auf zwei schwächere Möglichkeiten:

1. ein positiver Sobolev-Witness im festen odd Gram-Komplement;
2. eine rough/logarithmische Prime-Quadratur für den bereits explizit konstruierten compact rough complement witness.

Der vorliegende Knoten zeigt, dass selbst **positive Sobolev-Regularität weiterhin unnötig stark** ist.

Aus der robusten O3h-Zellfehlerabschätzung folgt für einen festen kompakt getragenen odd Vektor `f` mit erstem nichtverschwindendem Boundary-Jet `m` die exakt ausreichende Bedingung

\[
\boxed{
\omega_f(2\delta_T)
=o(T^{-m-3/2}),
\qquad
\delta_T:=\max_I|I|\lesssim e^{-2T/5}.
}
\tag{O3i.1}
\]

Hier ist

\[
\omega_f(h):=\|\tau_hE_Sf-E_Sf\|_{L^2(\mathbb R)}.
\]

Unter (O3i.1) schließt die derivative-freie Prime-Quadratur und der vollständige I2-Squeeze bleibt gültig:

\[
\boxed{
\sigma_T(J_{S,T}f)
=
c_m^2|\beta_S^{(m)}(f)|^2
\frac{e^T}{T^{2m+2}}
(1+o(1)).
}
\tag{O3i.2}
\]

Damit ist der wirkliche Regularitätsbedarf **logarithmisch**.

Definiere für `alpha>=0` die endliche Log-Regularitätsklasse

\[
\boxed{
\mathscr H_{\log}^{\alpha}(\mathbb R)
:=
\left\{F\in L^2(\mathbb R):
\int_{\mathbb R}
L(\xi)^{2\alpha}|\widehat F(\xi)|^2d\xi<\infty
\right\},
\quad
L(\xi):=\log(2+|\xi|).
}
\tag{O3i.3}
\]

Dann gilt:

\[
\boxed{
F\in\mathscr H_{\log}^{\alpha}
\Longrightarrow
\|\tau_hF-F\|_2
=o\bigl((\log(1/h))^{-\alpha}\bigr).
}
\tag{O3i.4}
\]

Daher genügt für einen Vektor mit erstem Jet `m` bereits

\[
\boxed{
E_Sf\in\mathscr H_{\log}^{\alpha}
\quad\text{für irgendein}\quad
\alpha\ge m+\frac32.
}
\tag{O3i.5}
\]

Die native Gammaform aus C1z-B1/O3h besitzt wegen

\[
1+g_\infty(\xi)\asymp\log(2+|\xi|)
\]

nur die Basisschwelle

\[
\boxed{
\mathcal D_{\Gamma,S}
=\mathscr H_{\log}^{1/2}
\quad\text{bis auf äquivalente Normen auf dem festen Source-Fenster}.
}
\tag{O3i.6}
\]

Somit fehlen für einen ersten Jet `m` nicht positive Ableitungen, sondern nur endlich viele zusätzliche logarithmische Regularitätsordnungen:

\[
\boxed{
\Delta\alpha=m+1.
}
\tag{O3i.7}
\]

Der O3g/O3h-Gate wird daher weiter reduziert auf

\[
\boxed{
?[O]\quad
\exists\;0\ne g\in\mathcal C^-_{S,T_0}(R)
\text{ kompakt getragen, erster Jet }m,
\text{ mit }
E_Sg\in\mathscr H_{\log}^{m+3/2}.
}
\tag{O3i.8}
\]

oder äquivalent auf eine noch schärfere Prime-Quadratur, die (O3i.1) direkt für einen rough complement witness beweist.

Status:

\[
\boxed{
\begin{aligned}
[P11\text{-}O3i]
&\quad \checkmark[M]_{\rm exact\ modulus\ sufficient\ gate}\\
&+\checkmark[M]_{\rm finite\ log\ regularity\ translation\ lemma}\\
&+\checkmark[M]_{\rm I2\ extension\ under\ log\ threshold}\\
&+\checkmark[M]_{\rm positive\ Sobolev\ not\ necessary}\\
&+\checkmark[M]_{\rm Gamma\ baseline\ alpha=1/2}\\
&+\checkmark[M]_{\rm finite\ log\ deficit\ m+1}\\
&+?[O]_{\rm complement\ witness\ at\ alpha\ge m+3/2}\\
&+?[O]_{\rm direct\ modulus\ gate\ for\ explicit\ rough\ witness}\\
&+?[O]_{\nu_2\ \rm polynomial\ lower\ witness}\\
&+?[O]_{\chi_-\|\Theta_-\|\to0}\\
&+?[O]_{W_{R,S,-}^{[T]}\ \rm strong\ Cauchy}.
\end{aligned}
}
\]

---

# 1. Verbindliche O3h-Zellfehlerform

Fixiere

\[
0<R<S<T_0
\]

und einen festen kompakt getragenen odd Vektor

\[
0\ne f\in\mathcal K^-_{X,S}
\]

mit erstem nichtverschwindendem Jet

\[
m=m(f)<\infty.
\]

O3h beweist für die Future-Prime-Zellweite

\[
\boxed{
\delta_T:=\max_I|I|\le Ce^{-2T/5}
}
\tag{O3i.9}
\]

und für den rough signed Quadraturrest

\[
\boxed{
\|Z_T^{\rm quad,rough}\|_2
\le
Ce^{T/2}\sqrt T
\left[
\delta_T\|f\|_2+
\omega_f(2\delta_T)
\right]
+
Z_T^{\rm anchor},
}
\tag{O3i.10}
\]

mit

\[
\boxed{
\|Z_T^{\rm anchor}\|_2=o(\sqrt{M_T}).
}
\tag{O3i.11}
\]

C4/O3h geben zugleich

\[
\boxed{
\sqrt{M_T}
\asymp_f
\frac{e^{T/2}}{T^{m+1}}.
}
\tag{O3i.12}
\]

Der Zellbreitenterm ist automatisch harmlos:

\[
\frac{e^{T/2}\sqrt T\,\delta_T}
{e^{T/2}T^{-m-1}}
\lesssim
T^{m+3/2}e^{-2T/5}
\to0.
\tag{O3i.13}
\]

Damit bleibt exakt der Translationsmodulterm.

---

# 2. Satz O3i.1 — exaktes hinreichendes Modulus-Gate

Angenommen

\[
\boxed{
\omega_f(2\delta_T)
=o(T^{-m-3/2}).
}
\tag{O3i.14}
\]

Dann

\[
\begin{aligned}
 e^{T/2}\sqrt T\,
\omega_f(2\delta_T)
&=
o\!\left(
 e^{T/2}\sqrt T\,T^{-m-3/2}
\right)\\
&=
o\!\left(
\frac{e^{T/2}}{T^{m+1}}
\right)\\
&=o(\sqrt{M_T}).
\end{aligned}
\]

Mit (O3i.10)--(O3i.13):

\[
\boxed{
\|Z_T^{\rm quad,rough}\|_2=o(\sqrt{M_T}).
}
\tag{O3i.15}
\]

Alle übrigen I2-Schritte sind nach O3h bereits `L^2`-robust:

1. C4-Mittelwertasymptotik;
2. Mean-Zero-Abspaltung;
3. kontinuierliche signed Zertifikatskosten;
4. Full-Rest-Lift aus O3d-I1;
5. Lower-/Upper-Squeeze.

Daher:

## Satz O3i.1

Für jeden festen kompakt getragenen odd Vektor `f` mit erstem Jet `m`, der (O3i.14) erfüllt, gilt die scharfe I2-Asymptotik (O3i.2).

Status:

\[
\boxed{\checkmark[M]_{\rm exact\ sufficient\ modulus\ gate}.}
\]

**Firewall O3i-FW1.** Die Bedingung (O3i.14) ist hinreichend für den robusten O3h-Quadraturbeweis. Es wird nicht behauptet, dass sie für jede denkbare Prime-Quadratur notwendig ist.

---

# 3. Logarithmische Regularitätsskala

Für `alpha>=0` setze (O3i.3).

Diese Skala ist strikt schwächer als jede positive Sobolev-Regularität:

\[
H^s(\mathbb R)
\subset
\mathscr H_{\log}^{\alpha}(\mathbb R)
\qquad
(s>0,\;\alpha<\infty),
\]

aber die Umkehrung gilt für kein festes `s>0`.

O3h zeigte bereits mit Modulationstests, dass die native Gammaform nicht automatisch in irgendein positives `H^s` einbettet.

---

# 4. Satz O3i.2 — Log-Regularität impliziert den benötigten Translationsmodul

Sei

\[
F\in\mathscr H_{\log}^{\alpha}(\mathbb R),
\qquad
\alpha>0.
\]

Wir zeigen (O3i.4).

Per Plancherel:

\[
\|\tau_hF-F\|_2^2
=
\frac1{2\pi}
\int_{\mathbb R}
|e^{i\xi h}-1|^2
|\widehat F(\xi)|^2d\xi.
\tag{O3i.16}
\]

Setze

\[
M:=h^{-1/2}.
\]

## Niederfrequenzen

Für `|xi|<=M` gilt

\[
|e^{i\xi h}-1|^2
\le h^2\xi^2
\le h.
\]

Daher

\[
\int_{|\xi|\le M}
|e^{i\xi h}-1|^2|\widehat F|^2
\le
h\|F\|_2^2.
\tag{O3i.17}
\]

Für jedes feste `alpha`:

\[
h=o\!\left((\log(1/h))^{-2\alpha}\right).
\tag{O3i.18}
\]

## Hochfrequenzen

Für `|xi|>M` gilt

\[
|e^{i\xi h}-1|^2\le4.
\]

Außerdem

\[
\begin{aligned}
\int_{|\xi|>M}|\widehat F(\xi)|^2d\xi
&\le
L(M)^{-2\alpha}
\int_{|\xi|>M}
L(\xi)^{2\alpha}|\widehat F(\xi)|^2d\xi\\
&=
o\bigl(L(M)^{-2\alpha}\bigr),
\end{aligned}
\tag{O3i.19}
\]

weil der gewichtete Tail gegen null geht.

Da

\[
L(M)\asymp\log(1/h),
\]

folgt aus (O3i.16)--(O3i.19):

\[
\boxed{
\|\tau_hF-F\|_2^2
=o\bigl((\log(1/h))^{-2\alpha}\bigr)
}
\tag{O3i.20}
\]

und damit

\[
\boxed{
\|\tau_hF-F\|_2
=o\bigl((\log(1/h))^{-\alpha}\bigr).
}
\tag{O3i.21}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm finite\ log\ translation\ lemma}.}
\]

---

# 5. Korollar — endliche Log-Schwelle für einen Jet `m`

Sei nun

\[
E_Sf\in\mathscr H_{\log}^{\alpha}
\]

mit

\[
\boxed{
\alpha\ge m+\frac32.
}
\tag{O3i.22}
\]

Aus (O3i.9):

\[
\log(1/\delta_T)
\ge
\frac25T-O(1).
\]

Daher aus (O3i.21):

\[
\omega_f(2\delta_T)
=o(T^{-\alpha})
=o(T^{-m-3/2}).
\tag{O3i.23}
\]

Somit greift Satz O3i.1 und die scharfe I2-Asymptotik folgt.

Also:

\[
\boxed{
E_Sf\in\mathscr H_{\log}^{m+3/2}
\Longrightarrow
\text{I2 sharp odd asymptotic für }f.
}
\tag{O3i.24}
\]

Positive Sobolev-Regularität ist daher nur ein komfortabler, aber nicht minimaler hinreichender Spezialfall.

Status:

\[
\boxed{\checkmark[M]_{\rm finite\ log\ threshold}.}
\]

---

# 6. Native Gamma-Schwelle und exakter Regularitätsdefizit

O3h beweist aus C1z-B1

\[
\boxed{
1+g_\infty(\xi)
\asymp
\log(2+|\xi|).
}
\tag{O3i.25}
\]

Die Gammaformnorm ist daher äquivalent zu

\[
\int
L(\xi)|\widehat{E_Sf}(\xi)|^2d\xi.
\]

Dies ist exakt die Log-Klasse mit

\[
2\alpha=1,
\qquad
\boxed{\alpha=\frac12.}
\tag{O3i.26}
\]

Für einen ersten Jet `m` verlangt (O3i.22)

\[
\alpha_{\rm req}=m+\frac32.
\]

Der Abstand zur automatisch vorhandenen Gamma-Regularität beträgt somit

\[
\boxed{
\alpha_{\rm req}-\alpha_{\Gamma}
=
\left(m+\frac32\right)-\frac12
=m+1.
}
\tag{O3i.27}
\]

Das ist der exakte endliche Log-Regularitätsdefizit des robusten O3h/I2-Quadraturwegs.

**Firewall O3i-FW2.** Aus (O3i.27) folgt nicht, dass ein complement witness diese zusätzlichen Log-Ordnungen nicht besitzt. Es folgt nur, dass sie nicht aus der bisherigen Gamma-Graphnorm allein erzwungen werden.

---

# 7. Anwendung auf den O3h-rough-complement witness

O3h konstruiert für jeden glatten odd Annulus-Vektor `h` den nichttrivialen compact rough complement witness

\[
\boxed{
 g_h=(I-\Pi^{\rm raw})h
\in
\mathcal C^-_{S,T_0}(R).
}
\tag{O3i.28}
\]

C5/O3h garantieren

\[
\boxed{
 m_h:=m(g_h)<\infty.
}
\tag{O3i.29}
\]

Daher ist für **jeden konkret gewählten** rough witness die noch fehlende Regularitätsforderung endlich:

\[
\boxed{
E_Sg_h\in
\mathscr H_{\log}^{m_h+3/2}
\quad ?
}
\tag{O3i.30}
\]

Es ist nicht mehr erforderlich, `g_h` als `H^s`-Vektor zu kontrollieren.

Noch schwächer genügt direkt die sequenzielle Modulusbedingung

\[
\boxed{
\omega_{g_h}(2\delta_T)
=o(T^{-m_h-3/2}).
}
\tag{O3i.31}
\]

---

# 8. Konsequenz für den konditionalen O3g-Witness

Angenommen, für einen festen Annulus-Witness `h` gilt (O3i.30), und setze

\[
g:=g_h,
\qquad
m:=m_h.
\]

Dann liefert Satz O3i.1/O3i.2 die scharfe Future-Asymptotik für `g`.

Wähle wie O3g einen glatten alten odd Vektor `f` mit demselben ersten Jet `m`.

Da `Jf` glatt und `g` in der endlichen Log-Klasse (O3i.30) liegt, liegen auch

\[
Jf\pm g,
\qquad
Jf\pm ig
\]

in derselben Log-Klasse. Ihre ersten Jets sind mindestens `m`; bei Cancellation liegt der erste Jet höher und der entsprechende Diagonalterm ist `o(e^U/U^{2m+2})`.

Daher funktioniert die O3g-Polarisation unverändert:

\[
\boxed{
\langle
(G_{S,U}-G_{S,T_0})Jf,g
\rangle
=
C_{f,g}
\frac{e^U}{U^{2m+2}}
(1+o(1)),
\qquad
C_{f,g}\ne0.
}
\tag{O3i.32}
\]

O3g liefert dann

\[
\boxed{
\|\mathscr B\|
\gtrsim
\frac{e^U}{U^{2m+2}},
}
\tag{O3i.33}
\]

und mit

\[
\|A_R\|\|A_S\|\lesssim U^2e^{2U}
\]

folgt

\[
\boxed{
\nu_2(U)
\gtrsim
U^{-(4m+6)}.
}
\tag{O3i.34}
\]

Damit würde O3f/I2 den bisherigen O3-Produktkanal ausschließen.

**Aber:** (O3i.30)/(O3i.31) ist weiterhin offen. Also ist auch (O3i.34) weiterhin nur konditional.

---

# 9. Neue atomare Gate-Formulierung

Der Regularitätsengpass ist nun nicht mehr

\[
\mathcal C^-\cap C_c^\infty\ne\{0\}
\]

und auch nicht mehr notwendig

\[
\mathcal C^-\cap H^s\ne\{0\}.
\]

Die minimal hinreichende, heute sichtbare Form lautet:

\[
\boxed{
\text{finde }0\ne g\in\mathcal C^-_{S,T_0}(R)
\text{ mit erstem Jet }m
\text{ und }
\omega_g(2\delta_T)=o(T^{-m-3/2}).
}
\tag{O3i.35}
\]

Eine komfortable statische hinreichende Form ist

\[
\boxed{
E_Sg\in\mathscr H_{\log}^{m+3/2}.
}
\tag{O3i.36}
\]

Dies ist der neue atomare Gate.

---

# 10. Externe Vergleichsfirewall

Der vorliegende Knoten benutzt **keinen** externen Regularitätssatz für den logarithmischen Laplaceoperator und identifiziert die P11-Gammaform nicht mit einem Standard-Dirichlet-Log-Laplacian.

Die gesamte Reduktion O3i.1--O3i.36 folgt ausschließlich aus den committed P11-Formeln C4/C5c/O3d-I2/O3g/O3h.

---

# 11. Endscope

Bewiesen ist jetzt:

\[
\boxed{
\text{positive Sobolev-Regularität ist für O3g nicht nötig.}
}
\]

\[
\boxed{
\text{Für ersten Jet }m\text{ genügt endliche Log-Regularität }
\alpha=m+\frac32.
}
\]

\[
\boxed{
\text{Die native Gammaform liefert nur }\alpha=\frac12.
}
\]

\[
\boxed{
\text{Der robuste Regularitätsdefizit beträgt exakt }m+1\text{ Log-Ordnungen.}
}
\]

Offen bleiben:

\[
?[O]_{\exists\ complement\ witness\ satisfying\ O3i.35/O3i.36},
\]

\[
?[O]_{\nu_2\ polynomial\ witness},
\]

\[
?[O]_{\chi_-\|\Theta_-\|\to0},
\]

\[
?[O]_{W_{R,S,-}^{[T]}\ strong\ Cauchy}.
\]

Kein O4, kein SYN, kein Seal.
