# P11-C1z-B2-C6l — Krylov-Residualprofil, Bulk/Shell-Zerlegung und Mixed-Boundary-Firewall

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6l]`  
**Direkte Voraussetzungen:** C1z-B2-C4, C1z-B2-C6d, C1z-B2-C6e, C1z-B2-C6j, C1z-B2-C6k  
**Strukturelle Schnittstellen:** C1z-B, C1z-B2-C3, C1z-B2-C6a, C1z-B2-C6b, C1z-B2-C6c, C1z-B2-C6f, C1z-B2-C6g, C1z-B2-C6h, C1z-B2-C6i  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d `orthogonality != jet alignment`, C1z-B2-C6k `current data != Wronskian nonzero`  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6l]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm pos,Krylov\text{-}residual\text{-}decomposition}
+
\checkmark[M]_{\rm pos,exact\text{-}A\text{-}energy\text{-}identity}
+
\checkmark[M]_{\rm pos,Wronskian\text{-}residual\text{-}reduction}
+
\checkmark[M]_{\rm pos,exact\text{-}bulk\text{-}shell\text{-}formula}
+
\checkmark[M]_{\rm pos,odd\text{-}parity\text{-}compatibility}
+
\checkmark[M]_{\rm neg,C4\text{-}constant\text{-}mode\text{-}mechanism\text{-}does\text{-}not\text{-}transfer}
+
\checkmark[M]_{\rm neg,cross\text{-}prime\text{-}edge\text{-}data\not\Rightarrow mixed\text{-}jet\text{-}alignment}
+
?[O]_{\rm residual\text{-}bulk\text{-}asymptotic}
+
?[O]_{\rm response\text{-}Wronskian\neq0}
+
?[O]_{\rm quantitative\text{-}s_{min}}
}
\]

C6l untersucht die in C6k isolierte zweite gemischte Observation

\[
\nu_{R,m}(T)
=
\langle J_{R,T}f_{R,m},\mathfrak G_T\rangle,
\qquad
\mathfrak G_T
:=
H_TA_T^{-1}H_T^*H_T\mathbf1_T,
\]

aber ohne die heuristische Abkürzung

\[
\text{„Cross-Prime-Struktur in }H_T^*H_T\mathbf1_T
\Rightarrow
\text{neue Jetrichtung“.}
\]

Der Hauptbefund ist eine exakte Zerlegung, die den tatsächlich neuen Anteil sichtbar macht.

Setze

\[
h_T:=H_T^*H_T\mathbf1_T,
\qquad
\lambda_T:=\frac{\mu_{T,1}}{\mu_{T,0}},
\qquad
r_T^{\rm src}:=h_T-\lambda_TA_T\mathbf1_T,
\]

und definiere den **Krylov-Source-Korrektor**

\[
\boxed{
y_T:=A_T^{-1}r_T^{\rm src}.}
\tag{C1zB2C6l.1}
\]

Dann gilt exakt

\[
\boxed{
A_T^{-1}h_T
=
\lambda_T\mathbf1_T+y_T,
}
\tag{C1zB2C6l.2}
\]

und daher

\[
\boxed{
\mathfrak G_T
=
\lambda_TH_T\mathbf1_T
+
H_Ty_T.
}
\tag{C1zB2C6l.3}
\]

Der erste Summand besitzt genau die C4-Boundary-Jet-Struktur. Er ist aber für die 2x2-Invertibilitätsfrage **vollständig irrelevant**, weil er im Response-Wronskian exakt wegfällt.

Definiere

\[
\boxed{
\eta_{R,m}(T)
:=
\langle J_{R,T}f_{R,m},H_Ty_T\rangle.
}
\tag{C1zB2C6l.4}
\]

Dann

\[
\boxed{
\nu_{R,m}(T)
=
\lambda_T\ell_{R,m}(T)+\eta_{R,m}(T),
}
\tag{C1zB2C6l.5}
\]

und C6ks Wronskian reduziert sich weiter zu

\[
\boxed{
\mathcal W_{R,T}
=
\ell_{R,0}(T)\eta_{R,1}(T)
-
\ell_{R,1}(T)\eta_{R,0}(T).
}
\tag{C1zB2C6l.6}
\]

Damit ist nun exakt klar:

\[
\boxed{
\text{Der zweite Jet-Alignment-Test sieht ausschließlich das Boundary-Verhalten von }H_Ty_T.
}
\tag{C1zB2C6l.7}
\]

C6l zeigt zugleich, warum C4 nicht direkt auf diesen neuen Profilvektor übertragbar ist. Für die Konstantenmode `1_T` verschwinden alle inneren zentrierten Differenzen exakt. Deshalb reduzierte C4 den alten Source-Window-Ausdruck auf einen reinen terminalen Prime-Shell. Für `y_T` ist genau dieser Mechanismus nicht verfügbar.

Auf dem festen alten Sourcefenster entsteht stattdessen eine exakte **Bulk/Shell-Zerlegung**. Für `x in [0,R]`, Prime-Power-Label `n=p^k`,

\[
s_n:=\frac12\log n,
\qquad
\alpha_n:=\sqrt{\log p}\,p^{-3k/4},
\]

gilt

\[
\boxed{
(H_Ty_T)(x)
=
\sum_{\substack{n=p^k\\ n\le e^{2(T-x)}}}
\alpha_n
\bigl[y_T(x+s_n)-y_T(x-s_n)\bigr]
-
\sum_{\substack{n=p^k\\ e^{2(T-x)}<n\le e^{2T}}}
\alpha_n y_T(x-s_n).
}
\tag{C1zB2C6l.8}
\]

Der erste Term ist der neue **Bulkterm**; der zweite ist der terminale **Shellterm**.

Für `y_T=1_T` ist der Bulkterm exakt null und der Shellterm reproduziert C4. Für den echten Krylov-Korrektor `y_T` gibt es derzeit weder eine Abschätzung, die den Bulkterm gegenüber dem Shellterm vernachlässigbar macht, noch eine eigene `1/T`-Entwicklung dieses Bulkterms.

Das ist der neue präzise Engpass.

---

# 0. Reconciliation mit C6k

C6k definierte

\[
\ell_{R,m}(T)
:=
\langle\xi_{R,m}^{(T)},\zeta_T\rangle,
\]

\[
\nu_{R,m}(T)
:=
\langle\xi_{R,m}^{(T)},\mathfrak S_T\zeta_T\rangle,
\]

und den Response-Wronskian

\[
\mathcal W_{R,T}
:=
\ell_{R,0}\nu_{R,1}
-
\ell_{R,1}\nu_{R,0}.
\]

Eventual gilt wegen C6e-C6j

\[
\mathcal P_T^{(1)}\text{ invertierbar}
\iff
\mathcal W_{R,T}\ne0.
\]

C6k schrieb ferner

\[
\nu_{R,m}(T)
=
\langle J_{R,T}f_{R,m},\mathfrak G_T\rangle
\]

mit

\[
\mathfrak G_T
=H_TA_T^{-1}h_T,
\qquad
h_T=H_T^*H_T\mathbf1_T.
\]

C6l zerlegt genau diesen neuen Vektor und trennt den bereits bekannten C4-Anteil vom echten Zweitprobeanteil.

---

# 1. Source-Residual hinter der zweiten Krylov-Probe

Setze

\[
A_T:=I+R_T^*R_T\ge I,
\]

\[
\mu_{T,0}
=\langle\mathbf1_T,A_T\mathbf1_T\rangle,
\qquad
\mu_{T,1}
=\langle\mathbf1_T,h_T\rangle,
\]

und

\[
\lambda_T
:=
\frac{\mu_{T,1}}{\mu_{T,0}}.
\tag{C1zB2C6l.9}
\]

Definiere

\[
\boxed{
r_T^{\rm src}
:=
h_T-\lambda_TA_T\mathbf1_T.
}
\tag{C1zB2C6l.10}
\]

Dann ist

\[
\boxed{
\langle r_T^{\rm src},\mathbf1_T\rangle=0.
}
\tag{C1zB2C6l.11}
\]

Denn

\[
\langle h_T,\mathbf1_T\rangle
=\mu_{T,1}
\]

und

\[
\lambda_T\langle A_T\mathbf1_T,\mathbf1_T\rangle
=\frac{\mu_{T,1}}{\mu_{T,0}}\mu_{T,0}
=\mu_{T,1}.
\]

Nun setze

\[
y_T:=A_T^{-1}r_T^{\rm src}.
\]

Dann gilt sofort

\[
\boxed{
\langle y_T,A_T\mathbf1_T\rangle=0.
}
\tag{C1zB2C6l.12}
\]

Dies ist die source-seitige Form der Orthogonalität der zweiten Krylov-Probe zur ersten.

---

# 2. Exakte A-Energie des Krylov-Korrektors

C6d definiert

\[
\Delta_T^{(1)}
=
\langle h_T,A_T^{-1}h_T\rangle
-
\frac{\mu_{T,1}^2}{\mu_{T,0}}.
\]

Für `r_T^{src}=h_T-lambda_T A_T1_T` gilt

\[
\begin{aligned}
\langle r_T^{\rm src},A_T^{-1}r_T^{\rm src}\rangle
&=
\langle h_T,A_T^{-1}h_T\rangle
-2\lambda_T\langle h_T,\mathbf1_T\rangle
+\lambda_T^2\langle A_T\mathbf1_T,\mathbf1_T\rangle\\
&=
\langle h_T,A_T^{-1}h_T\rangle
-2\frac{\mu_{T,1}^2}{\mu_{T,0}}
+\frac{\mu_{T,1}^2}{\mu_{T,0}}\\
&=
\Delta_T^{(1)}.
\end{aligned}
\]

Da `y_T=A_T^{-1}r_T^{src}`,

\[
\boxed{
\langle y_T,A_Ty_T\rangle
=
\Delta_T^{(1)}.
}
\tag{C1zB2C6l.13}
\]

Insbesondere

\[
\boxed{
\|y_T\|^2\le\Delta_T^{(1)},
\qquad
\|R_Ty_T\|^2\le\Delta_T^{(1)}.
}
\tag{C1zB2C6l.14}
\]

weil

\[
\langle y_T,A_Ty_T\rangle
=\|y_T\|^2+\|R_Ty_T\|^2.
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,exact\text{-}A\text{-}energy\text{-}identity}.
}
\]

### Verbindung zur normierten zweiten Probe

Aus C6d

\[
r_{T,1}^{\rm probe}
=
\mathfrak S_T\zeta_T-\lambda_T\zeta_T.
\]

Andererseits

\[
\begin{aligned}
r_{T,1}^{\rm probe}
&=
A_T^{-1/2}h_T
-\lambda_TA_T^{1/2}\mathbf1_T\\
&=
A_T^{-1/2}(h_T-\lambda_TA_T\mathbf1_T)\\
&=
A_T^{1/2}y_T.
\end{aligned}
\tag{C1zB2C6l.15}
\]

Daher

\[
\boxed{
\widehat\psi_{T,1}
=
\frac{A_T^{1/2}y_T}{\sqrt{\Delta_T^{(1)}}}.
}
\tag{C1zB2C6l.16}
\]

Der Source-Korrektor `y_T` ist also exakt die vor dem Feshbach-Whitening liegende zweite Krylov-Richtung.

---

# 3. Exakte Zerlegung des gemischten Profilvektors

Aus

\[
r_T^{\rm src}
=h_T-\lambda_TA_T\mathbf1_T
\]

folgt

\[
h_T
=\lambda_TA_T\mathbf1_T+A_Ty_T.
\]

Nach Anwendung von `A_T^{-1}`:

\[
\boxed{
A_T^{-1}h_T
=\lambda_T\mathbf1_T+y_T.
}
\tag{C1zB2C6l.17}
\]

Somit

\[
\boxed{
\mathfrak G_T
=H_TA_T^{-1}h_T
=\lambda_TH_T\mathbf1_T+H_Ty_T.
}
\tag{C1zB2C6l.18}
\]

Definiere

\[
\boxed{
\mathfrak G_T^{\perp}
:=H_Ty_T.
}
\tag{C1zB2C6l.19}
\]

Dann ist `mathfrak G_T^perp` exakt der neue Profilanteil, der nach Abzug der ersten Krylovrichtung übrig bleibt.

Für die C6k-Observationen:

\[
\begin{aligned}
\nu_{R,m}(T)
&=\langle J_{R,T}f_{R,m},\mathfrak G_T\rangle\\
&=\lambda_T\langle J_{R,T}f_{R,m},H_T\mathbf1_T\rangle
+\langle J_{R,T}f_{R,m},H_Ty_T\rangle.
\end{aligned}
\]

Da der erste Skalar genau `ell_R,m(T)` ist,

\[
\boxed{
\nu_{R,m}(T)
=\lambda_T\ell_{R,m}(T)+\eta_{R,m}(T),
}
\tag{C1zB2C6l.20}
\]

mit

\[
\eta_{R,m}(T)
:=\langle J_{R,T}f_{R,m},H_Ty_T\rangle.
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,Krylov\text{-}residual\text{-}decomposition}.
}
\]

---

# 4. Der Response-Wronskian sieht nur den Residualanteil

Setze C6ks Definition ein:

\[
\mathcal W_{R,T}
=\ell_{R,0}\nu_{R,1}-\ell_{R,1}\nu_{R,0}.
\]

Mit

\[
\nu_{R,m}=\lambda_T\ell_{R,m}+\eta_{R,m}
\]

folgt

\[
\begin{aligned}
\mathcal W_{R,T}
&=\ell_{R,0}(\lambda_T\ell_{R,1}+\eta_{R,1})
-\ell_{R,1}(\lambda_T\ell_{R,0}+\eta_{R,0})\\
&=
\boxed{
\ell_{R,0}\eta_{R,1}
-\ell_{R,1}\eta_{R,0}.
}
\end{aligned}
\tag{C1zB2C6l.21}
\]

Der komplette bekannte C4-Anteil

\[
\lambda_TH_T\mathbf1_T
\]

verschwindet also **exakt** aus dem Alignment-Invarianten.

Dies ist stärker als die `lambda_T`-Kürzung aus C6k: Nicht nur der skalare Quotient verschwindet algebraisch im Determinanten, sondern der gesamte Profilanteil entlang der ersten C4-Boundary-Observation trägt nichts zum Wronskian bei.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,Wronskian\text{-}residual\text{-}reduction}.
}
\]

### Rückübersetzung in die Probe-Matrix

Aus (C1zB2C6l.15)-(C1zB2C6l.16) folgt

\[
\begin{aligned}
\eta_{R,m}(T)
&=\langle J_{R,T}f_{R,m},H_Ty_T\rangle\\
&=\langle A_T^{-1/2}H_T^*J_{R,T}f_{R,m},A_T^{1/2}y_T\rangle\\
&=\langle\xi_{R,m}^{(T)},r_{T,1}^{\rm probe}\rangle\\
&=\boxed{
\sqrt{\Delta_T^{(1)}}
\langle\xi_{R,m}^{(T)},\widehat\psi_{T,1}\rangle.
}
\end{aligned}
\tag{C1zB2C6l.22}
\]

Damit ist die Reduktion exakt konsistent mit C6ks zweiter Probe-Zeile.

---

# 5. Parität des Residualprofils

Sei

\[
(Pf)(u):=f(-u)
\]

die Source-Reflexion.

Für den zentrierten Differenzoperator gilt

\[
D_sP=-PD_s.
\tag{C1zB2C6l.23}
\]

Da die source-gekoppelte Restmarke `q_{p,k,T}(u)` nur über `|u|` von `u` abhängt, ist die Restgeometrie reflexionssymmetrisch. Folglich kommutiert

\[
R_T^*R_T
\]

mit `P`, also auch

\[
A_T=I+R_T^*R_T.
\]

Der Hub antikommutiert mit `P`:

\[
H_TP=-PH_T.
\tag{C1zB2C6l.24}
\]

Da `1_T` gerade ist,

\[
H_T\mathbf1_T
\]

ungerade und

\[
h_T=H_T^*H_T\mathbf1_T
\]

gerade.

Auch

\[
A_T\mathbf1_T
\]

ist gerade. Daher sind

\[
r_T^{\rm src},\qquad y_T
\]

gerade, und

\[
\boxed{
\mathfrak G_T^{\perp}=H_Ty_T
\text{ ist ungerade.}
}
\tag{C1zB2C6l.25}
\]

Damit liegt das Residualprofil genau im richtigen Paritätssektor, um die ungeraden Boundary-Jets `beta_R^(m)` zu sehen.

Aber:

\[
\boxed{
\text{ungerade Parität}
\not\Rightarrow
\text{zweite Jetrichtung}.
}
\tag{C1zB2C6l.26}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,odd\text{-}parity\text{-}compatibility}.
}
\]

---

# 6. Exakte Bulk/Shell-Zerlegung auf dem alten Sourcefenster

Fixiere `R>0`, `T>R` und `x in [0,R]`.

Für ein Prime-Power-Label

\[
n=p^k\le e^{2T}
\]

setze

\[
\boxed{
s_n:=\frac12\log n}
\tag{C1zB2C6l.27}
\]

und

\[
\boxed{
\alpha_n:=\sqrt{\log p}\,p^{-3k/4}.
}
\tag{C1zB2C6l.28}
\]

Der Hub ist

\[
H_T
=\sum_{n=p^k\le e^{2T}}\alpha_nP_TD_{\log n}E_T.
\]

Für `x in [0,R]` gilt:

- falls `s_n<=T-x`, liegen `x+s_n` und `x-s_n` beide in `[-T,T]`;
- falls `T-x<s_n<=T`, liegt `x+s_n` außerhalb rechts, während `x-s_n` weiterhin in `[-T,T]` liegt.

Daher erhält man für jedes `L^2`-repräsentierbare `y_T` zunächst fast überall, beziehungsweise nach Wahl der natürlichen stückweisen Repräsentanten auf den hier verwendeten endlichen Translationen,

\[
\boxed{
\begin{aligned}
(H_Ty_T)(x)
&=
\sum_{\substack{n=p^k\\n\le e^{2(T-x)}}}
\alpha_n
\bigl[y_T(x+s_n)-y_T(x-s_n)\bigr]\\
&\quad-
\sum_{\substack{n=p^k\\e^{2(T-x)}<n\le e^{2T}}}
\alpha_n y_T(x-s_n).
\end{aligned}
}
\tag{C1zB2C6l.29}
\]

Definiere

\[
\boxed{
\mathcal B_T[y](x)
:=
\sum_{n\le e^{2(T-x)}}
\alpha_n\bigl[y(x+s_n)-y(x-s_n)\bigr]
}
\tag{C1zB2C6l.30}
\]

und

\[
\boxed{
\mathcal S_T[y](x)
:=-
\sum_{e^{2(T-x)}<n\le e^{2T}}
\alpha_n y(x-s_n).
}
\tag{C1zB2C6l.31}
\]

Dann

\[
\boxed{
H_Ty_T|_{[0,R]}
=
\mathcal B_T[y_T]
+
\mathcal S_T[y_T].
}
\tag{C1zB2C6l.32}
\]

Dies ist die verbindliche Mixed-Boundary-Zerlegung.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,exact\text{-}bulk\text{-}shell\text{-}formula}.
}
\]

---

# 7. Warum C4 für `1_T` außergewöhnlich einfach war

Setzt man formal `y=1_T`, dann gilt für jeden Bulk-Label

\[
1_T(x+s_n)-1_T(x-s_n)=0.
\]

Also

\[
\boxed{
\mathcal B_T[\mathbf1_T](x)=0.
}
\tag{C1zB2C6l.33}
\]

und

\[
\mathcal S_T[\mathbf1_T](x)
=-
\sum_{e^{2(T-x)}<p^k\le e^{2T}}
\sqrt{\log p}\,p^{-3k/4}.
\]

Dies ist exakt C4s

\[
-H_T\mathbf1_T(x)
=\Phi_T(x)
\]

auf der positiven alten Sourcehälfte.

C4s vollständige `1/T`-Jetentwicklung beruht daher auf zwei getrennten Spezialfakten:

1. **Bulk-Annihilation**
   \[
   D_s\mathbf1_T=0
   \]
   solange beide verschobenen Punkte im Fenster liegen;
2. **konstante Shell-Amplitude**
   \[
   \mathbf1_T(x-s_n)=1
   \]
   für alle terminalen Shelllabels.

Beide Eigenschaften reduzieren den gesamten alten Source-Window-Ausdruck auf eine skalare Prime-Power-Shellsumme, die anschließend arithmetisch expandiert werden kann.

---

# 8. Warum derselbe Mechanismus für den Krylov-Korrektor nicht verfügbar ist

Für `y_T` kennen wir exakt

\[
\langle y_T,A_T\mathbf1_T\rangle=0
\]

und

\[
\|y_T\|_A^2
:=
\langle y_T,A_Ty_T\rangle
=
\Delta_T^{(1)}.
\]

Diese Informationen erzwingen aber weder

\[
y_T(x+s_n)-y_T(x-s_n)=0
\]

im Bulk noch eine konstante oder asymptotisch einfache Shell-Amplitude.

Im Gegenteil: Wegen C6es eventualer Positivität

\[
\Delta_T^{(1)}>0
\]

ist `y_T` nicht null.

Noch stärker kann `y_T` nicht proportional zur Konstantenmode sein. Denn falls

\[
y_T=c\mathbf1_T,
\]

dann würde aus

\[
0=\langle y_T,A_T\mathbf1_T\rangle
=c\langle\mathbf1_T,A_T\mathbf1_T\rangle
\]

wegen `mu_T,0>0` bereits `c=0` folgen, im Widerspruch zu `Delta_T^(1)>0`.

Also:

\[
\boxed{
\Delta_T^{(1)}>0
\Rightarrow
y_T\text{ ist keine Konstantenmode}.
}
\tag{C1zB2C6l.34}
\]

Dies beweist nicht, dass jeder einzelne Bulkterm nichtnull ist. Es beweist aber, dass der C4-Schluss

\[
\text{„Bulk verschwindet identisch aus Symmetrie/Constancy“}
\]

für den echten Zweitprobe-Korrektor nicht zur Verfügung steht.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,C4\text{-}constant\text{-}mode\text{-}mechanism\text{-}does\text{-}not\text{-}transfer}.
}
\]

---

# 9. Warum die C6e-C6j-Cross-Prime-Kante den Mixed-Wronskian noch nicht entscheidet

C6e-C6j isolieren eine genuine Cross-Prime-Struktur in

\[
h_T=H_T^*H_T\mathbf1_T
\]

nahe den terminalen Punkten

\[
x_3(T),x_5(T)=T-O(1).
\]

Diese Information war stark genug für:

- eventualen Krylov-Rang 2;
- einen exakten Separator;
- eine explizite Untergrenze für `Delta_T^(1)`;
- lokale Restenergiekontrolle des Separators.

Die C6k/C6l-Observation ist jedoch

\[
\eta_{R,m}(T)
=
\langle J_{R,T}f_{R,m},H_Ty_T\rangle,
\]

wobei `J_R,T f_R,m` auf dem **festen alten Fenster** `[-R,R]` lebt.

Formel (C1zB2C6l.29) zeigt, dass `(H_Ty_T)(x)` für festes `x=O_R(1)` nicht nur terminale Werte von `y_T` nahe einer einzelnen Cross-Prime-Kante sieht. Der Bulkterm sampelt

\[
y_T(x+s_n),
\qquad
y_T(x-s_n)
\]

für sämtliche aktiven Prime-Power-Halblängen

\[
0<s_n\le T-x.
\]

Damit werden Werte über einen großen Teil des gesamten Terminalintervalls gekoppelt.

Die bisherige Cross-Prime-Separatortheorie liefert **keinen** Satz der Form

\[
\mathcal B_T[y_T](x)
=o(\mathcal S_T[y_T](x))
\]

oder eine eigene asymptotische Entwicklung von `mathcal B_T[y_T]`.

Ebenso liefert die globale Energieidentität

\[
\|y_T\|_A^2=\Delta_T^{(1)}
\]

keine punktweise oder BV-artige Kontrolle der Werte

\[
y_T(x\pm s_n).
\]

Insbesondere darf aus den terminalen Cross-Prime-Breakpoints von `h_T` nicht ohne einen neuen Propagationssatz durch

\[
A_T^{-1}
\]

und anschließend

\[
H_T
\]

auf eine neue feste-Source-Jetrichtung geschlossen werden.

Daher:

\[
\boxed{
[\text{Cross-Prime terminal edge in }h_T]
\not\Rightarrow
[\mathcal W_{R,T}\ne0]
\quad\text{mit den aktuellen Daten.}
}
\tag{C1zB2C6l.35}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,cross\text{-}prime\text{-}edge\text{-}data\not\Rightarrow mixed\text{-}jet\text{-}alignment}.
}
\]

Dies ist ein **Daten-/Mechanismus-No-Go**, kein P11-Gegenbeispiel gegen Alignment.

---

# 10. Was die vorhandene Energieinformation positiv liefert

Die Identität

\[
\|y_T\|_A^2=\Delta_T^{(1)}
\]

ist dennoch nützlich.

Aus (C1zB2C6l.22) folgt

\[
\boxed{
|\eta_{R,m}(T)|
\le
\sqrt{\Delta_T^{(1)}}\,\|\xi_{R,m}^{(T)}\|.
}
\tag{C1zB2C6l.36}
\]

Denn

\[
\eta_{R,m}
=\langle\xi_{R,m},r_{T,1}^{\rm probe}\rangle
\]

und

\[
\|r_{T,1}^{\rm probe}\|=\sqrt{\Delta_T^{(1)}}.
\]

Daraus folgt für den Wronskian die obere Schranke

\[
\boxed{
|\mathcal W_{R,T}|
\le
\sqrt{\Delta_T^{(1)}}
\left(
|\ell_{R,0}|\,\|\xi_{R,1}\|
+|\ell_{R,1}|\,\|\xi_{R,0}\|
\right).
}
\tag{C1zB2C6l.37}
\]

Diese Schranke ist nur eine **obere** Kontrolle. Sie liefert keine Nichtverschwindensaussage.

C6js Lower-Bound

\[
\Delta_T^{(1)}\gtrsim e^{-5T}
\]

bleibt damit eine Normierungsreserve, aber kein Alignment-Satz.

---

# 11. Der richtige reduzierte Mixed-Boundary-Test

C6k hatte wegen C4

\[
\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}
=
\frac{\kappa_R}{T}
\left(1+O_R(T^{-1})\right)
\]

für eine feste `kappa_R>0`.

Nach C6ls Residualreduktion ist daher der Alignment-Defekt

\[
\boxed{
\mathfrak E_{R,T}^{\perp}
:=
\eta_{R,1}(T)
-
\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}
\eta_{R,0}(T).
}
\tag{C1zB2C6l.38}
\]

und

\[
\boxed{
\mathcal W_{R,T}
=
\ell_{R,0}(T)\,\mathfrak E_{R,T}^{\perp}.
}
\tag{C1zB2C6l.39}
\]

Da `ell_R,0(T)` eventual nichtnull ist,

\[
\boxed{
\mathcal P_T^{(1)}\text{ invertierbar}
\iff
\mathfrak E_{R,T}^{\perp}\ne0.
}
\tag{C1zB2C6l.40}
\]

Dies ist eine stärkere Reduktion als „berechne das ganze Profil `mathfrak G_T`“.

Für den nächsten positiven Schritt genügt es, die zwei skalaren Residualobservationen

\[
\eta_{R,0}(T),
\qquad
\eta_{R,1}(T)
\]

so weit asymptotisch zu kontrollieren, dass ihre Ratio nicht dieselbe C4-Ratio besitzt.

---

# 12. Conditional Alignment-Satz für eine künftige Residualasymptotik

C6l formuliert bewusst nur ein konditionales Ziel, damit der nächste Knoten keine unnötig starke volle Profilasymptotik beweisen muss.

Angenommen, es existiert eine nichtverschwindende Skala `b_T` und Konstanten `d_{R,0},d_{R,1}` mit

\[
\eta_{R,0}(T)
=b_T\left(d_{R,0}+o(1)\right),
\tag{C1zB2C6l.41}
\]

und

\[
\eta_{R,1}(T)
=\frac{b_T}{T}\left(d_{R,1}+o(1)\right).
\tag{C1zB2C6l.42}
\]

Falls

\[
\boxed{
 d_{R,1}\ne\kappa_R d_{R,0},
}
\tag{C1zB2C6l.43}
\]

folgt aus (C1zB2C6l.38)

\[
\mathfrak E_{R,T}^{\perp}
=\frac{b_T}{T}
\left(
 d_{R,1}-\kappa_Rd_{R,0}+o(1)
\right)
\ne0
\]

eventual, also

\[
\boxed{
\mathcal W_{R,T}\ne0
}
\]

und damit echte `2x2`-Jet-Invertibilität.

Dieser konditionale Satz zeigt exakt, welche Art neuer Asymptotik benötigt wird: nicht „Cross-Prime irgendwo im Terminalraum“, sondern eine **zweite, nichtproportionale feste-Source-Observation**.

---

# 13. Warum volle Punktwise-Boundary-Asymptotik unnötig stark wäre

C6ks Formulierung mit

\[
\mathfrak G_T
=H_TA_T^{-1}h_T
\]

könnte dazu verleiten, zunächst `mathfrak G_T(x)` für alle `x in [-R,R]` vollständig zu expandieren.

C6l zeigt, dass dies für den unmittelbaren `2x2`-Test nicht nötig ist.

Es reichen die zwei Zahlen

\[
\eta_{R,0}(T)
=\langle Jf_{R,0},H_Ty_T\rangle,
\]

\[
\eta_{R,1}(T)
=\langle Jf_{R,1},H_Ty_T\rangle.
\]

Der nächste Knoten sollte daher zuerst einen **skalaren Mixed-Residual-Audit** durchführen und nicht eine unnötig starke uniforme Profiltheorie postulieren.

---

# 14. No-Go-Persistenzmatrix

| Früherer Knoten | Gesiegelter Befund | Wirkung in C6l |
|---|---|---|
| C1y | translationsinvariante Regulatoren lösen Hub/Rest-Konflikt im C1y-Scope nicht | unverändert |
| B2-A | Gamma-Präkonditionierung liefert keinen finite Schattenmechanismus | unverändert |
| B2-B | naiver Haar-L2-Endpunkt reicht nicht | unverändert |
| C4 | unendliche Boundary-Jet-Hierarchie; kein fixer endlicher Jet reicht global | unverändert; C6l benutzt nur `m=0,1` als Testfenster |
| C6 | kein voller Odd-Transport durch festen endlichen Jetquotienten | unverändert |
| C6a | Self-Grams/Kompression allein reichen nicht | unverändert |
| C6b | C2-Flachheit allein reicht nicht | unverändert |
| C6c | Triangularität allein reicht nicht | unverändert |
| C6d | Orthogonalität der Probes impliziert kein Jet-Alignment | **bestätigt und verschärft** |
| C6e | eventualer Krylov-Rang 2 | unverändert positiv |
| C6j | `Delta_T^(1) >= c e^{-5T}` | liefert A-Energiereserve für `y_T`, aber keine Boundary-Ratio |
| C6k | Alignment iff Response-Wronskian nonzero | weiter reduziert auf Residual-Wronskian |
| C6k | aktuelle Daten erzwingen Wronskian nicht | strukturell erklärt durch Bulkterm |

Kein älterer No-Go wird supersediert.

---

# 15. Was C6l ausdrücklich nicht beweist

Nicht bewiesen sind:

- `mathcal B_T[y_T]=o(mathcal S_T[y_T])` auf dem alten Fenster;
- eine `1/T`-Expansion von `H_Ty_T`;
- eine Asymptotik von `eta_R,0(T)` oder `eta_R,1(T)`;
- `eta_R,0(T) != 0` eventual;
- `eta_R,1(T) != 0` eventual;
- `mathfrak E_R,T^perp != 0`;
- `mathcal W_R,T != 0`;
- Invertibilität von `mathcal P_T^(1)`;
- eine quantitative Untergrenze für `s_min(mathcal P_T^(1))`;
- eine obere Asymptotik für `Delta_T^(1)`;
- `epsilon_T^probe(R,1) -> 0`;
- `tau_T(E_R,1) -> 0`;
- einen starken Odd-Gauge-Grenzwert.

Insbesondere wird die Heuristik

\[
\text{„Cross-Prime-Struktur ist anders als prime-pure Struktur“}
\]

nicht als Beweisersatz benutzt.

---

# 16. Exakter nächster Arbeitsauftrag C6m

Nach C6l ist der nächste sinnvolle Knoten enger als eine volle Boundary-Asymptotik von `mathfrak G_T`.

\[
\boxed{
\text{C6m: Mixed-Residual-Observation auf }E_{R,1}.
}
\tag{C1zB2C6l.44}
\]

Der Arbeitsauftrag lautet:

1. Untersuche direkt
   \[
   \eta_{R,m}(T)
   =\langle J_{R,T}f_{R,m},H_Ty_T\rangle,
   \qquad m=0,1.
   \]
2. Zerlege mit (C1zB2C6l.29) in Bulk- und Shellanteil.
3. Prüfe zuerst, ob der Bulkterm durch die `A_T`-Orthogonalität
   \[
   \langle y_T,A_T\mathbf1_T\rangle=0
   \]
   oder durch die konkrete source-gekoppelte Reststruktur zusätzliche Cancellation besitzt.
4. Falls keine solche Cancellation existiert, versuche einen quantitativen Bulkbound auf genau den beiden Testvektoren `f_R,0,f_R,1`, nicht punktweise auf ganz `[-R,R]`.
5. Bestimme, ob
   \[
   \eta_{R,1}(T)
   -\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}\eta_{R,0}(T)
   \]
   eventual von null getrennt werden kann.
6. Falls die beiden Residualobservationen asymptotisch dieselbe Ratio wie C4 besitzen, siegle dies als echten `2x2`-Alignment-No-Go in diesem Krylov-Scope.

### Harte Firewall für C6m

Nicht zulässig ist der Schluss

\[
\Delta_T^{(1)}>0
\Rightarrow
\mathfrak E_{R,T}^{\perp}\ne0.
\]

`Delta_T^(1)>0` ist targetseitige Nichtdegeneration; `mathfrak E_R,T^perp` ist source-windowed Observability.

Ebenso nicht zulässig ist

\[
\text{Cross-Prime-Breakpoint von }h_T
\Rightarrow
\text{Cross-Prime-dominierte Asymptotik von }H_TA_T^{-1}r_T^{src}	ext{ auf }[-R,R].
\]

Genau diese Propagation wäre neue Mathematik.

---

# 17. Endurteil

C6l bringt die C6k-Frage auf die richtige dynamische Variable.

Die zweite gemischte Observation ist nicht als Ganzes neu. Sie zerfällt exakt in

\[
\mathfrak G_T
=\lambda_TH_T\mathbf1_T+H_Ty_T,
\]

wobei der erste Term vollständig in der alten C4-Richtung liegt und im Response-Wronskian verschwindet.

Der echte neue Anteil ist

\[
\boxed{
\mathfrak G_T^{\perp}=H_Ty_T,
\qquad
\|y_T\|_A^2=\Delta_T^{(1)},
\qquad
\langle y_T,A_T\mathbf1_T\rangle=0.
}
\]

Auf dem alten Sourcefenster besitzt dieser Anteil die exakte Zerlegung

\[
H_Ty_T
=\mathcal B_T[y_T]+\mathcal S_T[y_T].
\]

C4 war deshalb so explizit, weil für `1_T` der gesamte Bulkterm identisch verschwand. Für `y_T` ist dieser Mechanismus nicht vorhanden; vielmehr ist `y_T` wegen `Delta_T^(1)>0` gerade keine Konstantenmode.

Damit ist die nächste offene Mathematik nun sehr präzise:

\[
\boxed{
\text{Kontrolliere die zwei skalaren Bulk/Shell-Residualobservationen }\eta_{R,0},\eta_{R,1}
\text{ und entscheide ihre Ratio.}
}
\]

Erst dies kann den Response-Wronskian und damit das erste echte `2x2`-Jet-Alignment positiv oder negativ entscheiden.