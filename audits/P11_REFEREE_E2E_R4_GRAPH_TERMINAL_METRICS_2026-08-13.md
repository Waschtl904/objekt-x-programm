# P11 END-TO-END REFEREE AUDIT — R4: GRAPH TRANSITIONS / TERMINAL METRICS

**Datum:** 2026-08-13  
**Paper:** `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex`  
**Knoten:** `thm:graph-transition`, `prop:pullback`, `thm:terminal-isometry`, `thm:relative-compression`, `cor:modulus`  
**Auditmodus:** End-to-End-Referee.

---

## 0. Typisierung

Für jedes `R` ist

\[
\mathcal K_{X,R}
=(\mathcal D(q_R^X),\langle\cdot,\cdot\rangle_{X,R})
\]

der Hilbertraum der Graphform. Alle Adjungierten

\[
J_{R,S}^*
\]

in diesem Abschnitt müssen und können daher ausschließlich als Hilbertraumadjungierte

\[
J_{R,S}^*: \mathcal K_{X,S}\to\mathcal K_{X,R}
\]

verstanden werden. Sie sind **nicht** mit dem L2-Restriktionsoperator `P_R` zu verwechseln.

Mit dieser Typisierung sind die nachfolgenden Produkte wohldefiniert.

Status:

\[
\boxed{[\mathrm{R4\text{-}TYPE}]\;\checkmark[M].}
\]

---

# 1. Bounded graph transitions

Für `0<R<S` gilt wegen

\[
E_SE_{R,S}f=E_Rf
\]

exakt

\[
\mathfrak c_{\Gamma,S}[E_{R,S}f]
=\mathfrak c_{\Gamma,R}[f].
\]

Der positive Schurterm erfüllt

\[
0\le
\langle\Sigma_SE_{R,S}f,E_{R,S}f\rangle
\le
\|H_S\|^2\|f\|_2^2
\le
\|H_S\|^2q_R^X(f).
\]

Somit

\[
q_S^X(E_{R,S}f)
\le
(1+\|H_S\|^2)q_R^X(f).
\]

Zero extension ist injektiv und erfüllt den offensichtlichen Cocycle.

\[
\boxed{[\mathrm{R4\text{-}J}]\;\checkmark[M].}
\]

---

# 2. Fixed-source lower bound und Invertibilität von `G_{R,T}`

Positivität des terminalen Schurterms liefert

\[
q_T^X(E_{R,T}f)
\ge
\mathfrak c_{\Gamma,T}[E_{R,T}f]
=
\mathfrak c_{\Gamma,R}[f].
\]

Aus

\[
q_R^X(f)
\le
(1+\|H_R\|^2)\mathfrak c_{\Gamma,R}[f]
\]

folgt

\[
\|J_{R,T}f\|_{X,T}^2
\ge
(1+\|H_R\|^2)^{-1}\|f\|_{X,R}^2.
\]

Daher ist `J_{R,T}` bounded below. Für

\[
G_{R,T}:=J_{R,T}^*J_{R,T}
\]

gilt im Graph-Hilbertraum

\[
G_{R,T}\ge(1+\|H_R\|^2)^{-1}I,
\]

also ist `G_{R,T}` positiv und boundedly invertible.

\[
\boxed{[\mathrm{R4\text{-}G}]\;\checkmark[M].}
\]

---

# 3. Pullback identity

Aus

\[
J_{S,T}J_{R,S}=J_{R,T}
\]

folgt exakt

\[
\begin{aligned}
J_{R,S}^*G_{S,T}J_{R,S}
&=J_{R,S}^*J_{S,T}^*J_{S,T}J_{R,S}\\
&=(J_{S,T}J_{R,S})^*(J_{S,T}J_{R,S})\\
&=J_{R,T}^*J_{R,T}\\
&=G_{R,T}.
\end{aligned}
\]

\[
\boxed{[\mathrm{R4\text{-}PULLBACK}]\;\checkmark[M].}
\]

---

# 4. Finite-terminal isometry

Definiere

\[
W_{R,S}^{[T]}
=G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}.
\]

Dann

\[
\begin{aligned}
(W_{R,S}^{[T]})^*W_{R,S}^{[T]}
&=G_{R,T}^{-1/2}J_{R,S}^*G_{S,T}J_{R,S}G_{R,T}^{-1/2}\\
&=I
\end{aligned}
\]

über die Pullbackidentität.

Für `0<R<S<U<T`:

\[
\begin{aligned}
W_{S,U}^{[T]}W_{R,S}^{[T]}
&=G_{U,T}^{1/2}J_{S,U}G_{S,T}^{-1/2}
 G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}\\
&=G_{U,T}^{1/2}J_{R,U}G_{R,T}^{-1/2}\\
&=W_{R,U}^{[T]}.
\end{aligned}
\]

Es wird keine Surjektivität von `W` benötigt oder behauptet; `W` ist eine Isometrie in den größeren Graph-Hilbertraum.

\[
\boxed{[\mathrm{R4\text{-}W}]\;\checkmark[M].}
\]

---

# 5. Relative compression

Für `T<U` setze

\[
A_R^{T,U}
=G_{R,T}^{-1/2}G_{R,U}G_{R,T}^{-1/2},
\]

analog auf `S`. Mit `W=W_{R,S}^{[T]}` gilt

\[
\begin{aligned}
W^*A_S^{T,U}W
&=G_{R,T}^{-1/2}J_{R,S}^*
 G_{S,U}J_{R,S}G_{R,T}^{-1/2}\\
&=G_{R,T}^{-1/2}G_{R,U}G_{R,T}^{-1/2}\\
&=A_R^{T,U}.
\end{aligned}
\]

Alle Quadratwurzeln und inversen Quadratwurzeln existieren durch die positive bounded invertibility der terminal metrics.

\[
\boxed{[\mathrm{R4\text{-}REL}]\;\checkmark[M].}
\]

---

# 6. Modulus isometry

Für

\[
Q=(A_S^{T,U})^{1/2}W(A_R^{T,U})^{-1/2}
\]

folgt

\[
\begin{aligned}
Q^*Q
&=(A_R^{T,U})^{-1/2}W^*A_S^{T,U}W(A_R^{T,U})^{-1/2}\\
&=I.
\end{aligned}
\]

\[
\boxed{[\mathrm{R4\text{-}Q}]\;\checkmark[M].}
\]

---

# 7. Firewall

Der Abschnitt weist unmittelbar nach der finite-terminal isometry ausdrücklich darauf hin, dass

\[
(W_{R,S}^{[T]})^*W_{R,S}^{[T]}=I
\]

keine Cauchy- oder Grenzwertaussage in `T` impliziert. Ebenso erklärt der First-power firewall, dass

\[
W^*A_SW=A_R
\]

keine Invarianz von `\operatorname{Ran}W` unter `A_S` und keine Kontrolle der komprimierten Quadratwurzel liefert.

Damit wird aus der exakten finite algebra nirgends implizit

\[
K_{R,S}^{T,U}\to I
\]

oder starker Terminaltransport gefolgert.

\[
\boxed{[\mathrm{R4\text{-}FW}]\;\checkmark[M].}
\]

---

# 8. Gesamturteil

\[
\boxed{
[\mathrm{P11\text{-}R4\text{-}TERMINAL\ ALGEBRA}]
=\checkmark[M].
}
\]

**Referee-Ergebnis:** PASS.

Kleine redaktionelle Empfehlung für den finalen Paperpass: einmal explizit sagen, dass `J^*` in §§4--5 stets das Adjungierte bezüglich der `X`-Graph-Skalarprodukte bezeichnet. Mathematisch ist die gegenwärtige Typisierung bereits eindeutig aus `G_{R,T}\in\mathcal B(\mathcal K_{X,R})` rekonstruierbar.
