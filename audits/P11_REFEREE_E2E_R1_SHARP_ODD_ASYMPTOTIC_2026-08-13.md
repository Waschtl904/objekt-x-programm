# P11 END-TO-END REFEREE AUDIT — R1: SHARP ODD ASYMPTOTIC

**Datum:** 2026-08-13  
**Paper:** `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex`  
**Hauptknoten:** Theorem `thm:odd`, Gleichung (6.1)  
**Modul:** `papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex`  
**Auditmodus:** End-to-End-Referee. Historische Audits dienen nur als destruktiver Gegencheck, nicht als Beweisergänzung.

---

## 0. Warum dieser Satz zuerst geprüft wird

Unter den im Paper behaupteten Resultaten verdient

\[
\sigma_T(J_{R,T}f_-)
=
c_m^2|\beta_R^{(m)}(f_-)|^2
\frac{e^T}{T^{2m+2}}(1+o(1))
\tag{R1.1}
\]

für feste nichtverschwindende glatte odd Vektoren den stärksten Widerstand.

Er verbindet die längste nichttriviale Kette im Manuskript:

\[
\text{boundary jet expansion}
\to
\text{sharp constant denominator}
\to
\text{signed mean-zero certificate}
\to
\text{short-interval prime quadrature}
\to
\text{full-rest lift}
\to
\text{dual squeeze}.
\]

Außerdem tragen (R1.1) sowohl die superpolynomiale Konditionsdivergenz als auch TC1-MIX.

---

# 1. Vorläufiges Gesamturteil

Es wurde in diesem Referee-Durchgang **kein Gegenbeispiel gegen (R1.1)** und kein falscher Exponent/Koeffizient gefunden.

Die zentralen Skalen sind konsistent:

\[
\ell_T(f_-)
\sim
-\sqrt2\,c_m\beta_R^{(m)}(f_-)
\frac{e^{T/2}}{T^{m+1/2}},
\]

\[
d_T
=\langle\mathbf1_T,(I+R_T^*R_T)\mathbf1_T\rangle
=2T+O(1),
\]

und daher

\[
\frac{|\ell_T(f_-)|^2}{d_T}
\sim
c_m^2|\beta_R^{(m)}(f_-)|^2
\frac{e^T}{T^{2m+2}}.
\]

Der Full-Hub-Squeeze ist ebenfalls algebraisch konsistent, **sofern** die in Steps 5--6 verwendete diskrete Full-Rest-Zerlegung paperintern vollständig hergestellt wird.

Der aktuelle Referee-Status lautet deshalb

\[
\boxed{
[\mathrm{P11\text{-}R1\text{-}T6.1}]
=\checkmark[M]_{\rm part}\;\text{(REFEREE HOLD)}.
}
\]

Nicht `×[M]`: Der Satz ist durch diesen Audit nicht widerlegt.  
Nicht `✓[M]`: Drei lokale Proof-Completion-Punkte verhindern derzeit einen echten End-to-End-PASS.

---

# 2. R1-A — Full-Rest-Faktorisierung (3.4)/(3.5) ist im Paper nicht bewiesen

Der Haupttext sagt nach Definition von

\[
\Phi_{p,a,R}[f](u)
:=\sum_{k\ge a+1}p^{-3k/4}(K_{k\log p}^{\rm tr}f)(u)
\]

direkt

\[
\mathfrak R_R(f,g)
=\sum_p(\log p)(p-1)\sum_{a\ge0}p^a
\int_{\Omega_{p,a,R}}
\Phi_{p,a,R}[f]\overline{\Phi_{p,a,R}[g]}
\tag{R1.2}
\]

und daraus

\[
\widetilde R_R^*\widetilde R_R=R_R^*R_R.
\tag{R1.3}
\]

Im aktuellen Paperpfad fehlt jedoch die eigentliche Rechnung aus der Definition von `R_R`.  Außerdem sollte explizit

\[
\mathfrak R_R(f,g):=\langle R_Rf,R_Rg\rangle
\]

gesetzt werden.

## Direkte Referee-Rechnung

Für festes `p` und

\[
J:=J_{p,R}(u)
\]

gilt

\[
\mathsf Q_R(u)\eta_{p,k}
=\sqrt{p-1}
\sum_{a=0}^{\min(k-1,J-1)}p^{(a-k)/2}\psi_{p,a}.
\]

Nach Multiplikation mit dem Restkoeffizienten `p^{-k/4}` wird der Koeffizient der orthonormalen Martingalkoordinate `\psi_{p,a}`

\[
\sqrt{p-1}\,p^{a/2}
\sum_{k\ge a+1}p^{-3k/4}(K_{k\log p}^{\rm tr}f)(u).
\]

Somit ist der `p`-Sektor von `R_Rf` exakt

\[
\sqrt{(\log p)(p-1)}
\sum_{a=0}^{J-1}
 p^{a/2}\Phi_{p,a,R}[f](u)\psi_{p,a}.
\]

Orthogonalität der `\psi_{p,a}` und der verschiedenen Primsektoren liefert sofort (R1.2), weil

\[
a<J_{p,R}(u)
\iff
u\in\Omega_{p,a,R}.
\]

Damit folgt (R1.3) durch Polarisation.

**Befund:** Die mathematische Identität ist `✓[M]`, aber ihre gegenwärtige Darstellung im Paper ist **nicht self-contained genug**, obwohl Theorem 6.1 sie in Step 1 und Step 6 als tragenden Input benutzt.

Status:

\[
\boxed{[\mathrm{R1\text{-}A}]\;\checkmark[M]_{\rm identity}\; +\;\times[M]_{\rm paper\ proof\ omission}.}
\]

---

# 3. R1-B — Sesquilineare Typisierung in (6.8), (6.15), (6.16)

TC1-MIX fixiert durch seine Formeln effektiv die Konvention, dass das Hilbertraumskalarprodukt im **ersten Argument linear** ist; insbesondere erscheint

\[
\rho_T(f,g)=\frac{\ell_T(f)\overline{\ell_T(g)}}{d_T}.
\]

Unter dieser Konvention muss für komplexe Testvektoren in Step 2 des Beweises von Theorem 6.1 geschrieben werden

\[
\langle h_T^{\rm grow},e\rangle
=
\int_0^T k_T(t)\,\overline{b_T(t)}\,dt,
\tag{R1.4}
\]

nicht wörtlich `\int k_T(t)b_T(t)dt`.

Entsprechend lautet die mean-zero identity

\[
\int_0^T k_T^0(t)\overline{b(t)}dt
=
\int_0^T\int_0^\varepsilon
k_T^0(t)\alpha(s)
\bigl(\overline{b(t)}-\overline{b(s)}\bigr)
\,ds\,dt,
\tag{R1.5}
\]

und nach `r=(t+s)/2`

\[
\int k_T^0\overline b
=
\iint C_T^-(r,t)
\overline{\bigl(b(t)-b(2r-t)\bigr)}\,dt\,dr.
\tag{R1.6}
\]

Die Zertifikatskosten und alle Betragsabschätzungen bleiben dadurch unverändert. Es handelt sich daher nicht um einen Gegenbeweis gegen (R1.1), sondern um einen echten komplex-sesquilinearen Typisierungsfehler im Prooftext.

Alternativ könnte das Paper die Rechnung zuerst für reelle Vektoren durchführen und anschließend die komplexe Version explizit rekonstruieren; derzeit tut es weder das eine noch das andere.

Status:

\[
\boxed{[\mathrm{R1\text{-}B}]\;\times[M]_{\rm proof\ typing}\quad\text{(lokal reparierbar)}.}
\]

---

# 4. R1-C — Step 5 nennt das Hilbertraumfeld, definiert es aber nicht

Der aktuelle Text verwendet für die Prime-Zellquadratur den Satz

> "For every Hilbert-valued Lipschitz function `\Phi` ... Apply this to the signed edge field ..."

aber das tatsächlich zu approximierende `L^2`-wertige Feld wird nicht definiert.

Für einen externen Referee ist das genau die Stelle, an der die Operator-Norm-/Translationsfrage gefährlich wird: die rohe Edge-Abbildung

\[
b\mapsto b(t)-b(2r-t)
\]

ist nicht als Operator in `r` operatornorm-Lipschitz.  Man muss daher die **Source-Representer** quadraturieren, nicht die rohe Translation als Operator.

## Explizite korrekte Source-Representer

Erweitere `C_T^-(r,t)` außerhalb seines natürlichen Supports durch Null und setze auf `L^2(0,T)`

\[
\boxed{
\Phi_T(r)(v)
:=
C_T^-(r,v)-C_T^-(r,2r-v).
}
\tag{R1.7}
\]

Dann gilt unter der linear-im-ersten-Argument-Konvention exakt

\[
\langle\Phi_T(r),b\rangle_{L^2(0,T)}
=
\int C_T^-(r,t)
\overline{\bigl(b(t)-b(2r-t)\bigr)}dt.
\tag{R1.8}
\]

Für

\[
C_T^-(r,t)=2k_T^0(t)\alpha(2r-t)
\]

folgt durch Differentiation

\[
\boxed{
\partial_r\Phi_T(r)(v)
=
4k_T^0(v)\alpha'(2r-v)
-4(k_T^0)'(2r-v)\alpha(v).
}
\tag{R1.9}
\]

Damit ist die benötigte Hilbertraum-Lipschitzabschätzung tatsächlich aus den bereits im Paper bewiesenen Bounds für `k_T,k_T'` ableitbar.

Für den konstanten Anteil `-K_T/T` verschwindet der zweite Term in (R1.9), so dass

\[
\sup_r\|\partial_r\Phi_T^{\rm const}(r)\|_2
\le C_\alpha |K_T|/T.
\]

Für den glatten `k_T`-Anteil und eine Zelle um `r` gilt lokal

\[
|I_r|\asymp e^{-\frac45(T-r)},
\]

während aus dem `k_T,k_T'`-Bound auf dem Support von `\alpha`

\[
\|\partial_r\Phi_T^{k}(r)\|_2
\lesssim
\frac{e^{(T-2r)/2}}{\sqrt{1+(T-2r)_+}}
\]

folgt. Daher ist das lokale Produkt

\[
|I_r|\,\|\partial_r\Phi_T^{k}(r)\|_2
\lesssim
 e^{-3T/10-r/5}
\]

(bis zu harmlosen polynomialen Faktoren), und die Summe der Zellfehler ist exponentiell klein. Der konstante Anteil liefert wie im Audit

\[
O(|K_T|e^{-2T/5})=o(\sqrt{M_T}).
\]

**Befund:** Die behauptete Quadraturrest-Skala ist mit der expliziten Representer-Rechnung kompatibel. Der aktuelle Papertext überspringt jedoch genau die Definition, die verhindert, dass man versehentlich eine falsche Operatornorm-Lipschitzbehauptung über Translationen benutzt.

Status:

\[
\boxed{[\mathrm{R1\text{-}C}]\;\checkmark[M]_{\rm part}\quad\text{(Mechanismus validiert, Paperbeweis zu komprimiert)}.}
\]

---

# 5. Externer Zahlentheorie-Input

Das Paper verwendet für festes `\theta=3/5`

\[
\sum_{x<n\le x+x^\theta}\Lambda(n)\sim x^\theta.
\]

Der veröffentlichte Guth--Maynard-Short-Interval-Bereich beginnt bei `17/30+\varepsilon`; da

\[
\frac35=\frac{18}{30}>\frac{17}{30},
\]

liegt die verwendete feste Exponentwahl sicher im bewiesenen Bereich. Die Umrechnung

\[
q\asymp X=e^{2(T-r)},
\qquad
\Delta q\asymp X^{3/5}
\]

in die `r`-Skala ergibt

\[
|I|\asymp \frac{\Delta q}{X}
\asymp X^{-2/5}
=e^{-\frac45(T-r)},
\]

wie im Paper verwendet.

Ferner ist

\[
w_q=\frac{\log q}{\sqrt q}\left(1-\frac1q\right)
\]

genau der primitive `a=0`-Full-Rest-Gewichtsfaktor, und PNT liefert auf einer solchen Zelle

\[
\sum_{q:r_q\in I}w_q
\asymp
2e^{T-r_I}|I|.
\]

Status:

\[
\boxed{[\mathrm{R1\text{-}PNT}]\;\checkmark[K/M].}
\]

---

# 6. Full-Rest-Lift und Squeeze

Unter der reparierten diskreten Zertifikatsdarstellung ist Step 6 algebraisch korrekt:

\[
\widetilde R_{T,0}^{\rm fut}
=P_T^{\rm fut}+E_T^{\rm fut},
\qquad
\|E_T^{\rm fut}\|
\lesssim \sqrt{T+1}e^{-T/2}.
\]

Wird `Y_T^{\rm prim,-}` in den `a=0`-Block gehoben, so ist

\[
\widetilde R_T^*\widehat Y_T^-
=(P_T^{\rm fut})^*Y_T^{\rm prim,-}
+(E_T^{\rm fut})^*\widehat Y_T^-.
\]

Der Tail wird mit negativem Vorzeichen in den Source-Rest absorbiert; seine Norm ist wegen

\[
\|Y_T^{\rm prim,-}\|^2=o(M_T)
\]

sogar deutlich kleiner als `\sqrt{M_T}`.

Damit ist

\[
Z_T^{\rm full}
=\mu_T\mathbf1_T+o_{L^2}(\sqrt{M_T}),
\]

also

\[
\|Z_T^{\rm full}\|_2^2=M_T(1+o(1)),
\]

und die duale Formel liefert den matching upper bound. Dieser letzte Squeeze zeigt in diesem Audit keinen algebraischen Defekt.

Status:

\[
\boxed{[\mathrm{R1\text{-}SQUEEZE}]\;\checkmark[M].}
\]

---

# 7. Firewall gegen implizite Terminalkonvergenz

Der Satz und sein direkt anschließender Scope-Remark behaupten nur fixed-vector-Asymptotik. Das Paper sagt ausdrücklich, dass der `o(1)`-Rest nicht uniform auf der odd unit sphere ist und keine Kontrolle von `G_{R,T}^{-1/2}` auf `T`-abhängigen Vektoren liefert.

Es wurde in diesem Abschnitt keine implizite Folgerung

\[
K_{R,S}^{T,U}\to I
\]

oder

\[
W_{R,S,-}^{[T]}\text{ strong Cauchy}
\]

gefunden.

Status:

\[
\boxed{[\mathrm{R1\text{-}FW}]\;\checkmark[M].}
\]

---

# 8. Pflichtreparaturen vor Referee-PASS von Theorem 6.1

1. In der Full-Rest-Subsection `\mathfrak R_R(f,g):=\langle R_Rf,R_Rg\rangle` definieren und (3.4)/(3.5) aus der `\psi_{p,a}`-Expansion beweisen.
2. Im O3d-I2-Paperbeweis die komplexe Sesquilinearität in (6.8), (6.15), (6.16) explizit korrekt schreiben oder eine reale Reduktion begründen.
3. In Step 5 das `L^2`-wertige Source-Representerfeld `\Phi_T(r)` definieren und die Zellfehlerabschätzung über dessen Ableitung führen; nicht die rohe Translation in Operatornorm behandeln.

Bis diese drei Punkte im Manuskript stehen:

\[
\boxed{
[\mathrm{P11\text{-}R1\text{-}T6.1}]
=\checkmark[M]_{\rm part}\quad\text{REFEREE HOLD}.
}
\]

Nach korrekter Integration dieser drei lokalen Punkte ist ein erneuter Direktaudit von Theorem 6.1 erforderlich; erst dann darf `✓[M]` vergeben werden.

---

# 9. Nächste Referee-Reihenfolge

Nach Theorem 6.1 ist der nächste unabhängige Hochrisikosatz nicht TC1-MIX (dessen Algebra weitgehend auf 6.1 aufsetzt), sondern

\[
\boxed{\text{Theorem `thm:schatten`: compact but no finite Schatten order}.}
\]

Dort sind insbesondere die lokalisierte Fourierfamilie, die isolierte primitive Translationskopie und der Übergang `S_R\in\mathcal S_p \Rightarrow K_R\in\mathcal S_{2p}` adversarial zu prüfen.
