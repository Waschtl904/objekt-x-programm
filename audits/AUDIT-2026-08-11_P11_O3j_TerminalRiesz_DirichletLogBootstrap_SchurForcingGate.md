# P11-O3j — Terminal-Riesz-Projektion, Dirichlet-Log-Bootstrap und Schur-Forcing-Gate

**Datum:** 2026-08-11  
**Knoten:** `[P11-O3j]`  
**Vorgaenger:** O3g, O3h, O3i  
**Direkte Schnittstellen:** C1z-B1, C1z-B2-C, C1z-B2-C1, C1z-B2-C2, O1, O2, O3g, O3h, O3i  
**Modus:** `PASS-A ACTIVE`  
**Scope-Firewall:** kein O4, kein tatsaechlicher polynomialer `nu_2`-Witness, kein O3-Produkt-No-Go, kein starker odd Terminaltransport, kein SYN, kein Seal.

---

## 0. Urteil

O3i reduzierte den noch offenen polynomialen Second-Moment-Witness auf eine endliche logarithmische Regularitaetsfrage fuer den expliziten rough complement witness

\[
g_h=(I-\Pi^{\rm raw})h,
\qquad
\Pi^{\rm raw}=J(G_R^0)^{-1}J^*G_S^0,
\]

wobei `h` ein glatter odd Annulus-Vektor ist und

\[
G_R^0:=G_{R,T_0},\qquad
G_S^0:=G_{S,T_0},\qquad
0<R<S<T_0.
\]

Der vorliegende Knoten typisiert den bisher abstrakten Korrekturterm

\[
u_h:=(G_R^0)^{-1}J^*G_S^0h
\]

exakt.

Der zentrale neue Befund lautet:

\[
\boxed{
J_{R,T_0}u_h
\text{ ist die }\mathcal K_{X,T_0}\text{-orthogonale Projektion von }
J_{S,T_0}h
\text{ auf }\operatorname{Ran}J_{R,T_0}.
}
\]

Auf der rohen Source-Ebene ist `u_h` daher die eindeutige Loesung einer festen finite-horizon Dirichlet-/Riesz-Gleichung

\[
\boxed{
q_{T_0}^X(E_Ru_h,E_Rv)
=
q_{T_0}^X(E_Sh,E_Rv)
\qquad
\forall v\in\mathcal K_{X,R}.
}
\tag{O3j.1}
\]

Hier bezeichnet `E_R=J_{R,T_0}` beziehungsweise `E_S=J_{S,T_0}` die rohe Nullfortsetzung in das gemeinsame Terminalfenster.

Da `h` glatt und strikt innerhalb `(-S,S)` getragen ist, ist die rechte Seite von (O3j.1) sogar durch einen festen `L^2(-R,R)`-Vektor darstellbar. Die eingeschraenkte Terminalform besitzt die Gestalt

\[
q_{T_0}^X(E_Ru,E_Rv)
=
q_{\Gamma,R}(u,v)
+
\langle \Sigma_R^{[T_0]}u,v\rangle_{L^2(-R,R)},
\]

mit einem beschraenkten positiven Operator `Sigma_R^[T0]`. Somit ist

\[
\boxed{
u_h
=\bigl(C_{\Gamma,R}+\Sigma_R^{[T_0]}\bigr)^{-1}r_h
\in\mathcal D(C_{\Gamma,R}).
}
\tag{O3j.2}
\]

Dies ist ein echter **Operator-Domain-Gewinn** gegenueber einem beliebigen Vektor des Gamma-Formraums

\[
\mathcal D(q_{\Gamma,R}).
\]

Aber: Aus dem bisher committed Material folgt **nicht**

\[
E_Ru_h\in\mathscr H_{\log}^{m_h+3/2},
\]

und auch nicht einmal die allgemeine Identifikation

\[
\mathcal D(C_{\Gamma,R})
\stackrel?\subset
\mathscr H_{\log}^{1}(\mathbb R)
\]

fuer die Nullfortsetzung. Die Source-Kompression ist eine echte Dirichlet-Realisierung des logarithmischen Symbols und darf nicht mit dem globalen Fouriermultiplikator invertiert werden.

Noch schaerfer laesst sich die forcing side zerlegen:

\[
\boxed{
r_h=r_{\Gamma,h}+r_{\sigma,h}.}
\tag{O3j.3}
\]

Der Gamma-Anteil des glatten Annulus-Witness besitzt beliebig hohe endliche Log-Regularitaet. Der einzige aus den committed Operatoren **nicht** hoeher regularisierte forcing-Anteil ist

\[
\boxed{
r_{\sigma,h}
=P_R\Sigma_{T_0}E_Sh,}
\tag{O3j.4}
\]

der finite-horizon Schur/Feshbach-Beitrag.

Damit wird O3is Log-Gate auf zwei konkrete analytische Teilfragen reduziert:

1. **Schur-Forcing-Regularitaet:** welche endliche Log-Regularitaet besitzt `r_{sigma,h}` fuer glattes Annulus-`h`?
2. **Dirichlet-Log-Resolvent-Bootstrap:** welche Log-Regularitaet uebertraegt die Inverse von
   \[
   C_{\Gamma,R}+\Sigma_R^{[T_0]}
   \]
   auf die Nullfortsetzung der Loesung?

Status:

\[
\boxed{
\begin{aligned}
[P11\text{-}O3j]
&\quad \checkmark[M]_{\rm terminal\text{-}Riesz\ projection}\\
&+\checkmark[M]_{\rm raw\ Dirichlet\ variational\ equation}\\
&+\checkmark[M]_{\rm restricted\ terminal\ Schur\ bounded}\\
&+\checkmark[M]_{\rm smooth\ exterior\ RHS\ is\ L^2\text{-}representable}\\
&+\checkmark[M]_{u_h\in\mathcal D(C_{\Gamma,R})}\\
&+\checkmark[M]_{\rm Gamma\ forcing\ has\ arbitrary\ finite\ log\ regularity}\\
&+?[O]_{\rm Schur\ forcing\ higher\ log\ regularity}\\
&+?[O]_{\rm Dirichlet\ log\ resolvent\ bootstrap}\\
&+?[O]_{E_Rg_h\in\mathscr H_{\log}^{m_h+3/2}}\\
&+?[O]_{\nu_2\ \rm polynomial\ lower\ witness}\\
&+?[O]_{\chi_-\|\Theta_-\|\to0}\\
&+?[O]_{W_{R,S,-}^{[T]}\ \rm strong\ Cauchy}.
\end{aligned}
}
\]

---

# 1. Typ-Firewall: `G_{R,T_0}` ist kein globaler Fouriermultiplikator

C1z-B2-C2 definiert auf dem nativen Objekt-X-Graphrraum

\[
\mathcal K_{X,R}
=
\bigl(\mathcal D(q_{\Gamma,R}),\|\cdot\|_{X,R}\bigr)
\]

den Terminalmetrikoperator

\[
\boxed{
G_{R,T_0}
:=J_{R,T_0}^*J_{R,T_0}
\in\mathcal B(\mathcal K_{X,R}).
}
\tag{O3j.5}
\]

Er ist positiv und beschraenkt invertierbar.

Insbesondere ist

\[
(G_R^0)^{-1}
\]

ein beschraenkter Operator auf `K_{X,R}`.

Dies darf **nicht** mit der Inversen des globalen Gamma-Fouriermultiplikators

\[
(1+g_\infty(\xi))^{-1}
\]

identifiziert werden.

Der Grund ist doppelt:

1. `G_R^0` ist ein Riesz-/Metrikoperator relativ zum bereits vollstaendigen finite-level Graphskalarprodukt `q_R^X`;
2. seine Definition enthaelt den Pullback der gesamten `T_0`-Geometrie, insbesondere den Feshbach-Schurterm.

Firewall:

\[
\boxed{
G_R^0\neq C_{\Gamma,R}
\quad\text{und}\quad
(G_R^0)^{-1}\neq C_{\Gamma,R}^{-1}
\text{ als behauptete Identitaeten.}
}
\tag{O3j.6}
\]

Status: `checkmark[M]` Typ-Praezisierung.

---

# 2. Exakte Terminal-Riesz-Projektion

Setze

\[
J:=J_{R,S},
\qquad
J_R:=J_{R,T_0},
\qquad
J_S:=J_{S,T_0}.
\]

Aus dem exakten Transition-Kokyklus gilt

\[
\boxed{
J_SJ=J_R.
}
\tag{O3j.7}
\]

Ferner

\[
G_R^0=J_R^*J_R,
\qquad
G_S^0=J_S^*J_S.
\]

Definiere

\[
\boxed{
u_h:=(G_R^0)^{-1}J^*G_S^0h.}
\tag{O3j.8}
\]

Dann

\[
G_R^0u_h=J^*G_S^0h.
\]

Fuer jedes `v in K_{X,R}`:

\[
\begin{aligned}
\langle J_Ru_h,J_Rv\rangle_{X,T_0}
&=\langle G_R^0u_h,v\rangle_{X,R}\\
&=\langle J^*G_S^0h,v\rangle_{X,R}\\
&=\langle G_S^0h,Jv\rangle_{X,S}\\
&=\langle J_Sh,J_SJv\rangle_{X,T_0}\\
&=\langle J_Sh,J_Rv\rangle_{X,T_0}.
\end{aligned}
\tag{O3j.9}
\]

Damit

\[
\boxed{
J_Ru_h=P_{\operatorname{Ran}J_R}^{X,T_0}\,J_Sh,
}
\tag{O3j.10}
\]

wobei rechts die orthogonale Projektion im Hilbertraum `K_{X,T0}` steht.

C1z-B2-C1 beweist, dass `Ran J_R` geschlossen ist, also ist diese Projektion wohldefiniert.

Insbesondere

\[
\boxed{
J_Sh-J_Ru_h
\perp_{X,T_0}
\operatorname{Ran}J_R.
}
\tag{O3j.11}
\]

Unter der Identifikation

\[
g_h=h-Ju_h
\]

ist dies exakt die Gram-Komplement-Eigenschaft aus O3g/O3h.

Status:

\[
\boxed{\checkmark[M]_{\rm terminal\text{-}Riesz\ projection}.}
\]

---

# 3. Rohe Source-Variationsgleichung

Auf rohen Funktionen ist jede `J`-Abbildung die Nullfortsetzung.

Schreibe daher

\[
E_R:L^2(-R,R)\to L^2(-T_0,T_0),
\]

\[
E_S:L^2(-S,S)\to L^2(-T_0,T_0).
\]

Dann ist (O3j.9) exakt

\[
\boxed{
q_{T_0}^X(E_Ru_h,E_Rv)
=
q_{T_0}^X(E_Sh,E_Rv)
\qquad
\forall v\in\mathcal K_{X,R}.
}
\tag{O3j.12}
\]

Dies ist die verbindliche Riesz-/Dirichletform des O3i-Regularitaetsgates.

Wichtig:

Die Gleichung lebt auf einem **festen endlichen Horizont `T_0`**. Es wird in diesem Knoten kein `T_0 -> infinity`-Grenzargument verwendet.

---

# 4. Terminalform = Gammaform + beschraenkter Schuroperator

Aus C1z-B1/C1z-B2-C gilt auf jedem festen Level `T_0`

\[
q_{T_0}^X(F,G)
=
q_{\Gamma,T_0}(F,G)
+
\sigma_{T_0}(F,G).
\tag{O3j.13}
\]

Mit

\[
B_{T_0}
:=(I+R_{T_0}^*R_{T_0})^{-1},
\qquad
0<B_{T_0}\le I,
\]

ist

\[
\sigma_{T_0}(F,G)
=
\langle H_{T_0}^*F,
B_{T_0}H_{T_0}^*G\rangle.
\]

Definiere den beschraenkten positiven selbstadjungierten Source-Operator

\[
\boxed{
\Sigma_{T_0}
:=H_{T_0}B_{T_0}H_{T_0}^*.
}
\tag{O3j.14}
\]

Dann

\[
\boxed{
\sigma_{T_0}(F,G)
=
\langle \Sigma_{T_0}F,G\rangle_{L^2(-T_0,T_0)}.
}
\tag{O3j.15}
\]

und

\[
0\le\Sigma_{T_0}\le \|H_{T_0}\|^2I.
\tag{O3j.16}
\]

Komprimiere auf den alten Source-Raum:

\[
\boxed{
\Sigma_R^{[T_0]}
:=E_R^*\Sigma_{T_0}E_R
\in\mathcal B(L^2(-R,R)).
}
\tag{O3j.17}
\]

Dann ist auch

\[
\Sigma_R^{[T_0]}\ge0.
\]

Aus der exakten Gamma-Kompatibilitaet unter Nullfortsetzung:

\[
q_{\Gamma,T_0}(E_Ru,E_Rv)
=
q_{\Gamma,R}(u,v).
\tag{O3j.18}
\]

Somit

\[
\boxed{
q_{T_0}^X(E_Ru,E_Rv)
=
q_{\Gamma,R}(u,v)
+
\langle\Sigma_R^{[T_0]}u,v\rangle.
}
\tag{O3j.19}
\]

Dies ist eine geschlossene coercive Form auf

\[
\mathcal D(q_{\Gamma,R}).
\]

---

# 5. Der zugehoerige Dirichletoperator

Sei

\[
C_{\Gamma,R}\ge I
\]

der aus der Gammaform erzeugte positive selbstadjungierte Operator aus C1z-B1.

Da `Sigma_R^[T0]` beschraenkt selbstadjungiert ist, ist nach dem Standardtheorem ueber beschraenkte selbstadjungierte Stoerungen der zu (O3j.19) gehoerige Operator

\[
\boxed{
F_R^{[T_0]}
=C_{\Gamma,R}+\Sigma_R^{[T_0]}
}
\tag{O3j.20}
\]

mit exakt derselben Operator-Domaene

\[
\boxed{
\mathcal D(F_R^{[T_0]})
=
\mathcal D(C_{\Gamma,R}).
}
\tag{O3j.21}
\]

Außerdem

\[
F_R^{[T_0]}\ge I,
\]

also

\[
(F_R^{[T_0]})^{-1}
\in\mathcal B(L^2(-R,R)).
\tag{O3j.22}
\]

**Firewall O3j-FW1.**

(O3j.21) ist eine Aussage ueber die Operator-Domaene der **Dirichlet-/Source-komprimierten** Gamma-Realisierung. Sie identifiziert diese Domaene nicht automatisch mit der globalen Fourierklasse `H_log^1` der Nullfortsetzung.

---

# 6. Die rechte Seite fuer glattes Annulus-`h` ist ein `L^2`-Vektor

Waehle wie O3h

\[
h\in C_c^\infty((-S,S))
\]

odd und mit positivem Abstand von den Grenzen `+-S`; insbesondere ist ihre Nullfortsetzung

\[
E_Sh\in C_c^\infty((-T_0,T_0)).
\]

Daher liegt `E_S h` in der Operator-Domaene von `C_{Gamma,T0}`.

Setze

\[
\boxed{
r_{\Gamma,h}
:=E_R^*C_{\Gamma,T_0}E_Sh,}
\tag{O3j.23}
\]

\[
\boxed{
r_{\sigma,h}
:=E_R^*\Sigma_{T_0}E_Sh.}
\tag{O3j.24}
\]

Dann

\[
r_{\Gamma,h},r_{\sigma,h}\in L^2(-R,R)
\]

und

\[
\boxed{
r_h:=r_{\Gamma,h}+r_{\sigma,h}\in L^2(-R,R).}
\tag{O3j.25}
\]

Fuer jedes `v in D(q_{Gamma,R})`:

\[
\begin{aligned}
q_{T_0}^X(E_Sh,E_Rv)
&=\langle C_{\Gamma,T_0}E_Sh,E_Rv\rangle
+\langle\Sigma_{T_0}E_Sh,E_Rv\rangle\\
&=\langle r_h,v\rangle_{L^2(-R,R)}.
\end{aligned}
\tag{O3j.26}
\]

Damit wird (O3j.12) zu

\[
\boxed{
q_{\Gamma,R}(u_h,v)
+\langle\Sigma_R^{[T_0]}u_h,v\rangle
=\langle r_h,v\rangle
\quad\forall v\in\mathcal D(q_{\Gamma,R}).
}
\tag{O3j.27}
\]

Nach dem Darstellungssatz fuer geschlossene Formen:

\[
\boxed{
F_R^{[T_0]}u_h=r_h
}
\tag{O3j.28}
\]

und daher

\[
\boxed{
u_h
=(F_R^{[T_0]})^{-1}r_h
\in\mathcal D(F_R^{[T_0]})
=\mathcal D(C_{\Gamma,R}).
}
\tag{O3j.29}
\]

Dies ist der neue positive Regularitaetsbefund.

Status:

\[
\boxed{\checkmark[M]_{u_h\in\mathcal D(C_{\Gamma,R})}.}
\]

---

# 7. Gamma forcing versus Schur forcing

O3h/O3i geben

\[
1+g_\infty(\xi)
\asymp
L(\xi),
\qquad
L(\xi)=\log(2+|\xi|).
\]

Da `E_Sh` glatt kompakt getragen ist, ist seine Fouriertransformierte Schwartz.

Multiplikation mit dem langsam wachsenden Gamma-Symbol behaelt daher fuer jedes feste `alpha<infty` genuegend Fourierzerfall.

Insbesondere besitzt der globale Gammaoutput des glatten `h` beliebig hohe **endliche logarithmische** Fourierregularitaet.

Nach Restriktion auf `(-R,R)` und erneuter Nullfortsetzung entsteht hoechstens ein fester endlicher Randjump. Ein kompakt getragener stueckweise glatter Vektor mit endlich vielen Randjumps besitzt wegen Fourierzerfall `O(|xi|^{-1})` weiterhin

\[
\int
L(\xi)^{2\alpha}|\widehat F(\xi)|^2d\xi<\infty
\]

fuer jedes feste `alpha`.

Damit:

\[
\boxed{
E_Rr_{\Gamma,h}
\in
\bigcap_{\alpha<\infty}\mathscr H_{\log}^{\alpha}(\mathbb R).
}
\tag{O3j.30}
\]

Der Schurforcing-Anteil besitzt aus den bisher committed Operatornormen dagegen nur

\[
\boxed{
r_{\sigma,h}\in L^2(-R,R).}
\tag{O3j.31}
\]

Denn `Sigma_T0` ist zwar positiv und beschraenkt auf `L^2`, aber es liegt bisher kein Satz vor, dass

\[
\Sigma_{T_0}
\]

eine positive Log-Regularitaetsklasse erhaelt oder verbessert.

Daher:

\[
\boxed{
\text{alle derzeit unkontrollierte forcing-Rauheit sitzt im finite-horizon Schur/Feshbach-Anteil.}
}
\tag{O3j.32}
\]

**Firewall O3j-FW2.** Aus `r_{sigma,h} in L2` wird nicht gefolgert, dass dieser Anteil tatsaechlich maximal rau ist. Es wird nur festgehalten, dass keine staerkere committed Kontrolle vorliegt.

---

# 8. Warum der Operator-Domain-Gewinn O3i noch nicht schliesst

O3i benoetigt fuer den expliziten complement witness

\[
g_h=h-Ju_h
\]

mit erstem Integral-Jet `m_h` mindestens die hinreichende Bedingung

\[
E_Sg_h
\in
\mathscr H_{\log}^{m_h+3/2}
\tag{O3j.33}
\]

oder direkt

\[
\omega_{g_h}(2\delta_T)
=o(T^{-m_h-3/2}).
\tag{O3j.34}
\]

Da `h` glatt ist, liegt die gesamte Frage im alten Korrekturterm `Ju_h`.

Aus (O3j.29) wissen wir zwar

\[
u_h\in\mathcal D(C_{\Gamma,R}),
\]

aber die committed Quellen identifizieren die Dirichlet-Operator-Domaene nicht mit

\[
\mathscr H_{\log}^{1}
\]

oder einer hoeheren globalen Fourierklasse der Nullfortsetzung.

Die falsche Abkuerzung waere

\[
C_{\Gamma,R}
\stackrel{\rm falsch}{=}
\mathcal F^{-1}L(\xi)\mathcal F
\quad\text{auf dem gesamten }L^2(\mathbb R)
\]

und daraus

\[
C_{\Gamma,R}^{-1}
\stackrel{\rm falsch}{=}
\mathcal F^{-1}L(\xi)^{-1}\mathcal F.
\]

Tatsaechlich ist `C_{Gamma,R}` die durch die geschlossene Source-Form erzeugte **Dirichlet-Realisierung auf dem festen Fenster**.

Der Grenz-/Randoperator ist daher nicht durch bloße symbolweise Division auditiert.

Status:

\[
\boxed{?[O]_{\rm Dirichlet\text{-}log\ bootstrap}.}
\]

---

# 9. Exakter verbleibender Bootstrap-Gate

Der O3i-Gate kann jetzt source-kanonisch so formuliert werden.

## Gate J1 — Schur forcing

Fuer den glatten odd Annulus-Witness `h`:

\[
\boxed{
E_Rr_{\sigma,h}
\stackrel?\in
\mathscr H_{\log}^{\beta}
\quad\text{fuer eine ausreichend grosse endliche }\beta.
}
\tag{O3j.35}
\]

## Gate J2 — Dirichlet resolvent

Fuer

\[
F_R^{[T_0]}
=C_{\Gamma,R}+\Sigma_R^{[T_0]}
\]

muss ein datenabhaengiger oder operatorieller Log-Bootstrap bewiesen werden, stark genug um aus der forcing-Regularitaet die Zielschwelle

\[
\boxed{
E_Ru_h
\in
\mathscr H_{\log}^{m_h+3/2}
}
\tag{O3j.36}
\]

zu gewinnen.

Erst dann folgt wegen glattem `h`

\[
E_Sg_h
\in
\mathscr H_{\log}^{m_h+3/2}
\]

und O3i/O3g liefern den polynomialen `nu_2`-Witness.

---

# 10. Eine schwachere direkte Alternative

Auch O3j.36 ist weiterhin staerker als logisch notwendig.

Nach O3i genuegt direkt

\[
\boxed{
\omega_{E_Ru_h}(2\delta_T)
=o(T^{-m_h-3/2}),
\qquad
\delta_T\lesssim e^{-2T/5}.
}
\tag{O3j.37}
\]

Denn `h` ist glatt und sein Translationsmodul auf exponentiell kleinen Skalen ist exponentiell klein.

Damit lauten die zwei noch minimaleren Folgewege:

1. **Log-Space-Weg:** Beweis von (O3j.36);
2. **direkter Dirichlet-Modulus-Weg:** Beweis nur von (O3j.37).

Keiner der beiden Wege ist in O3j geschlossen.

---

# 11. Abhaengigkeiten und Firewalls

## O3j-FW3 — kein polynomialer Witness

O3j beweist nicht

\[
\nu_2(U)\gtrsim U^{-M}.
\]

## O3j-FW4 — kein O3-Produkt-No-Go

Daher wird nicht behauptet

\[
\chi_-(U)\|\Theta_-(U)\|\not\to0.
\]

## O3j-FW5 — kein Transport-No-Go

Selbst ein spaeterer Beweis des polynomialen `nu_2`-Witness wuerde nach O3f lediglich den **hinreichenden O3-Produktkanal** ausschliessen, nicht automatisch den starken odd Terminaltransport selbst.

## O3j-FW6 — kein Fourier-Inversen-Kurzschluss

Die exakte Formel

\[
1+g_\infty(\xi)\asymp\log(2+|\xi|)
\]

beschreibt die globale Gammaform und ihre Formdomäne. Sie rechtfertigt ohne eigenen Dirichlet-Regularitaetssatz keine symbolweise Formel fuer

\[
(C_{\Gamma,R}+\Sigma_R^{[T_0]})^{-1}.
\]

---

# 12. Ergebnisstatus

Verbindlich ist nun:

\[
\boxed{
\begin{aligned}
&u_h=(G_R^0)^{-1}J^*G_S^0h
\text{ ist exakt terminal-orthogonale Rieszprojektion};\\
&u_h\text{ loest eine feste Dirichletgleichung }F_R^{[T_0]}u_h=r_h;\\
&r_h\in L^2(-R,R);\\
&u_h\in\mathcal D(C_{\Gamma,R});\\
&r_{\Gamma,h}\text{ besitzt beliebig hohe endliche Log-Regularitaet};\\
&r_{\sigma,h}\text{ besitzt committed bislang nur }L^2\text{-Kontrolle};\\
&\text{die benoetigte endliche Log-Schwelle von }u_h\text{ bleibt offen}.
\end{aligned}
}
\]

Der naechste direkte mathematische Block soll daher **nicht** erneut abstrakt `G_R^{-1}` untersuchen, sondern einen der zwei konkret typisierten Gate angreifen:

\[
\boxed{
\text{O3k-A: Schur-Forcing-Logregularitaet von }r_{\sigma,h}
}
\]

oder

\[
\boxed{
\text{O3k-B: Dirichlet-Log-Resolvent/Translationsmodul fuer }F_R^{[T_0]}.
}
\]

Strategisch ist `O3k-A` zuerst zu testen, weil jede dort bewiesene Roughness- oder Regularitaetsaussage die benoetigte Staerke des Resolvent-Bootstraps unmittelbar festlegt.

---

## Schlussstatus

\[
\boxed{
[P11\text{-}O3j]
\quad
\checkmark[M]_{\rm Riesz/Dirichlet\ reduction}
+\checkmark[M]_{\rm operator\text{-}domain\ gain}
+?[O]_{\rm Schur\ forcing\ log\ regularity}
+?[O]_{\rm Dirichlet\ log\ bootstrap}
+?[O]_{\nu_2\ polynomial}
+?[O]_{\rm O3\ product\ gate}
+?[O]_{\rm strong\ odd\ terminal\ transport}.
}
\]
