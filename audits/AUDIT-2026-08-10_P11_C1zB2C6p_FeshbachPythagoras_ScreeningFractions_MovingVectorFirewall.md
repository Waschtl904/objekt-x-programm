# P11-C1z-B2-C6p — Feshbach-Pythagoras, dimensionslose Screening-Fraktionen und Moving-Vector-Firewall

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6p]`  
**Direkte Voraussetzungen:** C1z-B2-C6a, C1z-B2-C6h, C1z-B2-C6j, C1z-B2-C6m, C1z-B2-C6n, C1z-B2-C6o  
**Strukturelle Schnittstellen:** C1z-B, C1z-B2-C3, C1z-B2-C4, C1z-B2-C6c, C1z-B2-C6d, C1z-B2-C6e, C1z-B2-C6f, C1z-B2-C6g, C1z-B2-C6i, C1z-B2-C6k, C1z-B2-C6l  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d `orthogonality != jet alignment`, C1z-B2-C6k `current data != Wronskian nonzero`, C1z-B2-C6l `C4 constant-mode mechanism does not transfer`, C1z-B2-C6m `A-orthogonality != bulk cancellation`, C1z-B2-C6n `positivity != alignment`, C1z-B2-C6o `raw support separation route fails`.  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6p]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm corr,screening\text{-}energy\text{-}formula}
+
\checkmark[M]_{\rm pos,Feshbach\text{-}Pythagoras\text{-}isometry}
+
\checkmark[M]_{\rm pos,dimensionless\text{-}screening\text{-}criterion}
+
\checkmark[M]_{\rm pos,Jensen\text{-}rest\text{-}loading\text{-}bound}
+
\checkmark[M]_{\rm pos,quantitative\text{-}residual\text{-}angle\text{-}lower\text{-}bound}
+
\checkmark[M]_{\rm neg,global\text{-}rest\text{-}norm\text{-}insufficient}
+
\checkmark[M]_{\rm neg,C6h/C6j\text{-}vector\text{-}transfer\text{-}unproved}
+
\checkmark[M]_{\rm neg,fixed\text{-}vector\text{-}divergence\not\Rightarrow moving\text{-}g_T\text{-}divergence}
+
?[O]_{\rm bare\text{-}residual\text{-}angle\text{-}lower\text{-}bound}
+
?[O]_{\rm vector\text{-}specific\text{-}screening\text{-}fractions}
+
?[O]_{\rm second\text{-}alignment\text{-}scalar\neq0}
+
?[O]_{\rm quantitative\text{-}s_{min}}
}
\]

C6o isolierte das hinreichende Nichtkompensationskriterium

\[
|\mathcal U_{R,T}^{\perp}|
>
\sqrt{\varepsilon_{b,T}^{\rm scr}\varepsilon_{r,T}^{\rm scr}}
\quad\Longrightarrow\quad
a_{R,T}^{(2)}\ne0,
\]

mit

\[
\mathcal U_{R,T}^{\perp}=\langle b_{R,T},r_T\rangle,
\]

\[
\varepsilon_{b,T}^{\rm scr}=\langle b_{R,T},S_Tb_{R,T}\rangle,
\qquad
\varepsilon_{r,T}^{\rm scr}=\langle r_T,S_Tr_T\rangle,
\]

und

\[
S_T=I-A_T^{-1}
=R_T^*(I+R_TR_T^*)^{-1}R_T.
\]

C6p klärt nun drei Punkte:

1. Die informelle Quotientenformel für die Screening-Energie wird korrigiert.
2. Das gesamte Kriterium wird als exakte zweikanalige Pythagoras-Geometrie formuliert und dimensionslos normalisiert.
3. Es wird geprüft, welche früheren C6-Schätzungen die neuen Größen tatsächlich kontrollieren. Das Ergebnis ist negativ für einen direkten Transfer: Weder C6h/C6j noch C6a liefern bereits die benötigten vektorspezifischen Screening- oder Bare-Winkel-Bounds für `b_{R,T}` und `r_T`.

Der positive Gewinn ist eine quantitativ scharfe Reduktion auf drei dimensionslose Parameter:

\[
\boxed{
\beta_{R,T},\quad s_{b,T},\quad s_{r,T}.
}
\]

---

# 0. Verbindliche Daten aus C6m–C6o

Fixiere `R>0` und großes `T`.

Aus C6m stammt

\[
 g_{R,T}
 =
 f_{R,1}
 -
 \frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}f_{R,0},
\]

mit

\[
\boxed{
\langle J_{R,T}g_{R,T},H_T\mathbf1_T\rangle=0.
}
\tag{C1zB2C6p.1}
\]

Setze wie C6n/C6o

\[
\boxed{
 b_{R,T}
 :=
 H_T^*J_{R,T}g_{R,T},
}
\tag{C1zB2C6p.2}
\]

\[
\boxed{
 h_T:=H_T^*H_T\mathbf1_T,
}
\tag{C1zB2C6p.3}
\]

\[
\boxed{
 A_T:=I+R_T^*R_T\ge I,
}
\tag{C1zB2C6p.4}
\]

\[
\lambda_T:=\frac{\mu_{T,1}}{\mu_{T,0}},
\]

und

\[
\boxed{
 r_T:=h_T-\lambda_TA_T\mathbf1_T.
}
\tag{C1zB2C6p.5}
\]

Dann

\[
\langle b_{R,T},\mathbf1_T\rangle=0,
\qquad
\langle r_T,\mathbf1_T\rangle=0.
\tag{C1zB2C6p.6}
\]

C6l/C6n geben

\[
\boxed{
\Delta_T^{(1)}
=
\langle r_T,A_T^{-1}r_T\rangle>0
}
\tag{C1zB2C6p.7}
\]

eventual, und C6m/C6n geben

\[
\boxed{
\sigma_T(J_{R,T}g_{R,T})
=
\langle b_{R,T},A_T^{-1}b_{R,T}\rangle.
}
\tag{C1zB2C6p.8}
\]

Der zweite Alignment-Skalar ist

\[
\boxed{
 a_{R,T}^{(2)}
 =
 \frac{
 \langle b_{R,T},A_T^{-1}r_T\rangle
 }{
 \sqrt{\Delta_T^{(1)}}
 }.
}
\tag{C1zB2C6p.9}
\]

C6o schrieb äquivalent

\[
\boxed{
\sqrt{\Delta_T^{(1)}}a_{R,T}^{(2)}
=
\mathcal U_{R,T}^{\perp}
-
\mathcal C_{R,T}^{\perp},
}
\tag{C1zB2C6p.10}
\]

mit

\[
\mathcal U_{R,T}^{\perp}
=
\langle b_{R,T},r_T\rangle,
\]

\[
\mathcal C_{R,T}^{\perp}
=
\langle b_{R,T},(I-A_T^{-1})r_T\rangle.
\]

---

# 1. Korrektur: Screening-Energie ist ein quadratisches Resolventenfunktional, kein Normquotient

Setze

\[
\boxed{
Q_T:=(I+R_TR_T^*)^{-1/2}.
}
\tag{C1zB2C6p.11}
\]

Dann ist

\[
S_T
=
R_T^*Q_T^2R_T.
\tag{C1zB2C6p.12}
\]

Für jeden Sourcevektor `v` gilt daher exakt

\[
\boxed{
\varepsilon_T^{\rm scr}(v)
:=
\langle v,S_Tv\rangle
=
\langle R_Tv,(I+R_TR_T^*)^{-1}R_Tv\rangle
=
\|Q_TR_Tv\|^2.
}
\tag{C1zB2C6p.13}
\]

Insbesondere

\[
\varepsilon_{b,T}^{\rm scr}
=
\|Q_TR_Tb_{R,T}\|^2,
\]

und

\[
\varepsilon_{r,T}^{\rm scr}
=
\|Q_TR_Tr_T\|^2.
\]

Die informelle Schreibweise

\[
\varepsilon_{r,T}^{\rm scr}
\stackrel?=
\frac{\|R_Tr_T\|^2}{\|I+R_TR_T^*\|}
\]

ist im Allgemeinen falsch.

Da

\[
I
\le
I+R_TR_T^*
\le
(1+\|R_T\|^2)I,
\]

folgt

\[
\frac1{1+\|R_T\|^2}I
\le
(I+R_TR_T^*)^{-1}
\le
I.
\]

Daher gilt für jedes `v`

\[
\boxed{
\frac{\|R_Tv\|^2}{1+\|R_T\|^2}
\le
\varepsilon_T^{\rm scr}(v)
\le
\|R_Tv\|^2.
}
\tag{C1zB2C6p.14}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,screening\text{-}energy\text{-}formula}.
}
\]

---

# 2. Exakte Feshbach-Pythagoras-Isometrie

Aus der Woodbury-/Push-through-Identität folgt

\[
A_T^{-1}
=
I-R_T^*(I+R_TR_T^*)^{-1}R_T.
\]

Also

\[
\boxed{
A_T^{-1}+S_T=I.
}
\tag{C1zB2C6p.15}
\]

Definiere den zweikanaligen Operator

\[
\boxed{
\mathfrak D_T:
\mathscr H_T
\longrightarrow
\mathscr H_T\oplus\mathscr Y_T,
\qquad
\mathfrak D_Tv
:=
A_T^{-1/2}v
\oplus
Q_TR_Tv.
}
\tag{C1zB2C6p.16}
\]

Dann gilt für jedes `v`

\[
\begin{aligned}
\|\mathfrak D_Tv\|^2
&=
\|A_T^{-1/2}v\|^2
+
\|Q_TR_Tv\|^2\\
&=
\langle v,A_T^{-1}v\rangle
+
\langle v,S_Tv\rangle\\
&=
\|v\|^2.
\end{aligned}
\]

Somit

\[
\boxed{
\mathfrak D_T^*\mathfrak D_T=I.
}
\tag{C1zB2C6p.17}
\]

`mathfrak D_T` ist eine kanonische Isometrie, die jeden Sourcevektor in zwei orthogonale Informationskanäle zerlegt:

1. **überlebender Feshbach-Kanal** `A_T^{-1/2}v`;
2. **Screening-Kanal** `Q_TR_Tv`.

Für zwei Vektoren `u,v` erhält man durch Polarisation exakt

\[
\boxed{
\langle u,v\rangle
=
\langle A_T^{-1/2}u,A_T^{-1/2}v\rangle
+
\langle Q_TR_Tu,Q_TR_Tv\rangle.
}
\tag{C1zB2C6p.18}
\]

Für `u=b_{R,T}`, `v=r_T` ist dies genau C6os Residualzerlegung:

\[
\boxed{
\mathcal U_{R,T}^{\perp}
=
\sqrt{\Delta_T^{(1)}}a_{R,T}^{(2)}
+
\mathcal C_{R,T}^{\perp}.
}
\tag{C1zB2C6p.19}
\]

Der Alignment-Zähler ist also der Anteil der bare correlation, der im **überlebenden** Feshbach-Kanal verbleibt.

Die Screening-Korrektur ist der Anteil derselben bare correlation, der in den **abgeschirmten** Kanal ausgelagert wird.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,Feshbach\text{-}Pythagoras\text{-}isometry}.
}
\]

---

# 3. Pythagoreische Energiezerlegung für `b` und `r`

Aus (C1zB2C6p.15) folgt

\[
\boxed{
\|b_{R,T}\|^2
=
\sigma_T(Jg_{R,T})
+
\varepsilon_{b,T}^{\rm scr}.
}
\tag{C1zB2C6p.20}
\]

Ebenso

\[
\boxed{
\|r_T\|^2
=
\Delta_T^{(1)}
+
\varepsilon_{r,T}^{\rm scr}.
}
\tag{C1zB2C6p.21}
\]

Damit messen die Screening-Energien exakt die Differenz zwischen der nackten `L^2`-Energie und der Feshbach-überlebenden Energie.

Insbesondere

\[
\boxed{
\varepsilon_{b,T}^{\rm scr}
=
\|b_{R,T}\|^2-\sigma_T(Jg_{R,T}),
}
\tag{C1zB2C6p.22}
\]

\[
\boxed{
\varepsilon_{r,T}^{\rm scr}
=
\|r_T\|^2-\Delta_T^{(1)}.
}
\tag{C1zB2C6p.23}
\]

Das zeigt erneut, warum C6js Untergrenze

\[
\Delta_T^{(1)}\gtrsim e^{-5T}
\]

allein keine Screening-Kleinheit liefert: Ohne eine passende obere Kontrolle von `||r_T||^2` kann der Quotient

\[
\Delta_T^{(1)}/\|r_T\|^2
\]

beliebig klein sein.

---

# 4. Dimensionslose Screening-Fraktionen

Angenommen zunächst `b_{R,T}\ne0`; andernfalls ist

\[
a_{R,T}^{(2)}=0
\]

und es gibt kein `2x2`-Alignment.

Da `Delta_T^(1)>0` eventual ist, gilt `r_T\ne0` eventual.

Definiere

\[
\boxed{
 s_{b,T}
 :=
 \frac{\varepsilon_{b,T}^{\rm scr}}{\|b_{R,T}\|^2}
 =
 1-
 \frac{\sigma_T(Jg_{R,T})}{\|b_{R,T}\|^2},
}
\tag{C1zB2C6p.24}
\]

und

\[
\boxed{
 s_{r,T}
 :=
 \frac{\varepsilon_{r,T}^{\rm scr}}{\|r_T\|^2}
 =
 1-
 \frac{\Delta_T^{(1)}}{\|r_T\|^2}.
}
\tag{C1zB2C6p.25}
\]

Da `0<A_T^{-1}\le I` für jedes feste `T`, gilt

\[
\boxed{
0\le s_{b,T}<1,
\qquad
0\le s_{r,T}<1.
}
\tag{C1zB2C6p.26}
\]

Die komplementären Fraktionen

\[
1-s_{b,T}
=
\frac{\sigma_T(Jg_{R,T})}{\|b_{R,T}\|^2},
\]

\[
1-s_{r,T}
=
\frac{\Delta_T^{(1)}}{\|r_T\|^2}
\]

sind die **überlebenden Feshbach-Anteile**.

---

# 5. Bare Residualwinkel

Definiere den dimensionslosen bare angle

\[
\boxed{
\beta_{R,T}
:=
\frac{
|\langle b_{R,T},r_T\rangle|
}{
\|b_{R,T}\|\,\|r_T\|
}.
}
\tag{C1zB2C6p.27}
\]

Dann

\[
0\le\beta_{R,T}\le1.
\]

C6os hinreichendes Kriterium

\[
|\langle b,r\rangle|
>
\sqrt{\varepsilon_b^{\rm scr}\varepsilon_r^{\rm scr}}
\]

ist exakt äquivalent zu

\[
\boxed{
\beta_{R,T}
>
\sqrt{s_{b,T}s_{r,T}}.
}
\tag{C1zB2C6p.28}
\]

Damit ist die qualitative Nichtkompensationsfrage vollständig dimensionslos formuliert.

Interpretation:

- `beta_{R,T}` misst die nackte Korrelation der beiden Residuen;
- `sqrt(s_b s_r)` ist die maximal mögliche normierte Korrelation, die allein durch den Screening-Kanal getragen werden kann.

Wenn die nackte Korrelation größer ist als die maximale Screening-Kapazität, muss ein nichtverschwindender Anteil im Feshbach-Kanal übrig bleiben.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,dimensionless\text{-}screening\text{-}criterion}.
}
\]

---

# 6. Exakte Zweikanal-Winkelzerlegung

Definiere, sofern die Nenner nichtnull sind,

\[
\gamma_{R,T}^{\rm surv}
:=
\frac{
\langle A_T^{-1/2}b_{R,T},A_T^{-1/2}r_T\rangle
}{
\sqrt{\sigma_T(Jg_{R,T})}\sqrt{\Delta_T^{(1)}}
},
\]

und

\[
\gamma_{R,T}^{\rm scr}
:=
\frac{
\langle Q_TR_Tb_{R,T},Q_TR_Tr_T\rangle
}{
\sqrt{\varepsilon_{b,T}^{\rm scr}}\sqrt{\varepsilon_{r,T}^{\rm scr}}
}.
\]

Dann

\[
|\gamma_{R,T}^{\rm surv}|\le1,
\qquad
|\gamma_{R,T}^{\rm scr}|\le1.
\]

Außerdem ist nach C6n

\[
\boxed{
|\gamma_{R,T}^{\rm surv}|^2
=
\rho_{R,T}^{(2)}.
}
\tag{C1zB2C6p.29}
\]

Denn

\[
\langle A_T^{-1/2}b,A_T^{-1/2}r\rangle
=
\sqrt{\Delta_T^{(1)}}a_{R,T}^{(2)}.
\]

Normiert man (C1zB2C6p.18) durch `||b|| ||r||`, erhält man die exakte komplexe Zweikanalzerlegung

\[
\boxed{
\frac{\langle b_{R,T},r_T\rangle}
{\|b_{R,T}\|\,\|r_T\|}
=
\sqrt{(1-s_{b,T})(1-s_{r,T})}
\,\gamma_{R,T}^{\rm surv}
+
\sqrt{s_{b,T}s_{r,T}}
\,\gamma_{R,T}^{\rm scr}.
}
\tag{C1zB2C6p.30}
\]

Diese Identität ist die präziseste geometrische Form des C6o-Problems.

Falls

\[
\gamma_{R,T}^{\rm surv}=0,
\]

also genau falls das gewünschte zweite Alignment verschwindet, dann muss die gesamte bare Korrelation durch den Screening-Kanal getragen werden und daher

\[
\boxed{
\beta_{R,T}
\le
\sqrt{s_{b,T}s_{r,T}}.
}
\tag{C1zB2C6p.31}
\]

Das ist exakt die Kontraposition von (C1zB2C6p.28).

---

# 7. Quantitative Untergrenze für den Residualwinkel

Aus (C1zB2C6p.30) und `|gamma_scr|<=1` folgt per Dreiecksungleichung

\[
\sqrt{(1-s_b)(1-s_r)}
|\gamma^{\rm surv}|
\ge
\left(
\beta-\sqrt{s_bs_r}
\right)_+,
\]

wobei

\[
(x)_+:=\max\{x,0\}.
\]

Also

\[
\boxed{
\sqrt{\rho_{R,T}^{(2)}}
\ge
\frac{
\left(
\beta_{R,T}-\sqrt{s_{b,T}s_{r,T}}
\right)_+
}{
\sqrt{(1-s_{b,T})(1-s_{r,T})}
}.
}
\tag{C1zB2C6p.32}
\]

und damit

\[
\boxed{
\rho_{R,T}^{(2)}
\ge
\frac{
\left(
\beta_{R,T}-\sqrt{s_{b,T}s_{r,T}}
\right)_+^2
}{
(1-s_{b,T})(1-s_{r,T})
}.
}
\tag{C1zB2C6p.33}
\]

Dies ist stärker als das bloße Ja/Nein-Kriterium aus C6o.

Sobald man eine quantitative Lücke

\[
\beta_{R,T}
-
\sqrt{s_{b,T}s_{r,T}}
\ge
\delta_{R,T}>0
\]

beweist, erhält man unmittelbar eine quantitative Untergrenze für den C6n-Residualwinkel.

Da

\[
|a_{R,T}^{(2)}|^2
=
\sigma_T(Jg_{R,T})\rho_{R,T}^{(2)},
\]

folgt zugleich

\[
\boxed{
|a_{R,T}^{(2)}|
\ge
\frac{\|b_{R,T}\|}{\sqrt{1-s_{r,T}}}
\left(
\beta_{R,T}-\sqrt{s_{b,T}s_{r,T}}
\right)_+.
}
\tag{C1zB2C6p.34}
\]

Hier wurde

\[
\sqrt{\sigma_T(Jg)}
=
\|b\|\sqrt{1-s_b}
\]

verwendet.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,quantitative\text{-}residual\text{-}angle\text{-}lower\text{-}bound}.
}
\]

---

# 8. Vektorspezifische rohe Restbelastung

Definiere für jeden nichtnulligen Sourcevektor `v`

\[
\boxed{
q_T(v)
:=
\frac{\|R_Tv\|^2}{\|v\|^2}.
}
\tag{C1zB2C6p.35}
\]

Insbesondere

\[
q_{b,T}:=q_T(b_{R,T}),
\qquad
q_{r,T}:=q_T(r_T).
\]

Setze

\[
B_T:=R_T^*R_T\ge0.
\]

Dann

\[
S_T
=
B_T(I+B_T)^{-1}.
\]

Für einen normierten Vektor `v/||v||` sei `mu_v` sein Spektralmaß bezüglich `B_T`.

Dann

\[
s_T(v)
=
\int_0^\infty
\frac{\lambda}{1+\lambda}
\,d\mu_v(\lambda),
\]

und

\[
q_T(v)
=
\int_0^\infty
\lambda\,d\mu_v(\lambda).
\]

Die Funktion

\[
f(\lambda)=\frac{\lambda}{1+\lambda}
\]

ist auf `[0,infty)` wachsend und konkav.

Jensen liefert daher

\[
\boxed{
s_T(v)
\le
\frac{q_T(v)}{1+q_T(v)}.
}
\tag{C1zB2C6p.36}
\]

Außerdem, da `lambda<=||R_T||^2` auf dem Spektrum von `B_T`, gilt

\[
\frac{\lambda}{1+\lambda}
\ge
\frac{\lambda}{1+\|R_T\|^2},
\]

also

\[
\boxed{
\frac{q_T(v)}{1+\|R_T\|^2}
\le
s_T(v)
\le
\frac{q_T(v)}{1+q_T(v)}.
}
\tag{C1zB2C6p.37}
\]

Für `b,r` folgt

\[
\boxed{
 s_{b,T}
 \le
 \frac{q_{b,T}}{1+q_{b,T}},
\qquad
 s_{r,T}
 \le
 \frac{q_{r,T}}{1+q_{r,T}}.
}
\tag{C1zB2C6p.38}
\]

Damit erhält man ein zweites hinreichendes Alignment-Kriterium:

\[
\boxed{
\beta_{R,T}
>
\sqrt{
\frac{q_{b,T}q_{r,T}}
{(1+q_{b,T})(1+q_{r,T})}
}
\quad\Longrightarrow\quad
a_{R,T}^{(2)}\ne0.
}
\tag{C1zB2C6p.39}
\]

Dieses Kriterium ist besonders nützlich, falls man zeigen kann, dass die beiden spezifischen Residualvektoren in einem schwach gescreenten Spektralbereich von `R_T^*R_T` liegen.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,Jensen\text{-}rest\text{-}loading\text{-}bound}.
}
\]

---

# 9. Warum der globale Restoperator-Bound C6f/C6j hier nicht reicht

C6f/C6j liefern global

\[
\|R_T\|^2
\le
C_RT e^T
\]

für großes `T`.

Daraus folgt nur

\[
q_{b,T},q_{r,T}
\le
C_RT e^T.
\]

Über (C1zB2C6p.36) ergibt dies höchstens

\[
s_{b,T},s_{r,T}
\le
\frac{C_RT e^T}{1+C_RT e^T}
=
1-O((Te^T)^{-1}).
\]

Diese obere Schranke nähert sich `1`.

Sie zeigt also gerade **keine** kleine Screening-Fraktion.

Das dimensionslose Kriterium degeneriert damit auf eine Forderung nahe

\[
\beta_{R,T}>1,
\]

und ist so nicht anwendbar.

Daher gilt:

\[
\boxed{
\text{Der globale Operatorbound }\|R_T\|^2\lesssim Te^T
\text{ kann C6os Screening-Kriterium nicht schließen.}
}
\tag{C1zB2C6p.40}
\]

Benötigt werden vektorspezifische Schätzungen für `b_{R,T}` und `r_T`.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,global\text{-}rest\text{-}norm\text{-}insufficient}.
}
\]

---

# 10. C6h kontrolliert nicht `R_Tr_T`

C6h analysierte die spezielle Restgeometrie der Konstantenmode und bewies insbesondere lokale BV-Kontrolle für

\[
A_T\mathbf1_T
=
\mathbf1_T+R_T^*R_T\mathbf1_T
\]

in exponentiell kleinen Fenstern um die Cross-Prime-Orte `x_q(T)`.

Diese Rechnung benutzt wesentlich die exakte p-Tiefenlagenformel für

\[
R_{p,T}\mathbf1_T.
\]

Der neue Vektor

\[
r_T
=
h_T-\lambda_TA_T\mathbf1_T
\]

ist dagegen keine Konstantenmode und keine bereits in C6h analysierte Tiefenlage.

Insbesondere ist

\[
R_Tr_T
=
R_Th_T
-
\lambda_TR_TA_T\mathbf1_T.
\]

Beide Terme enthalten zusätzliche Hub- beziehungsweise Restpropagation, für die C6h keine lokale `L^2`-Energieformel liefert.

C6hs lokale Sprungabschätzung für `A_T1_T` impliziert daher weder

\[
\|R_Tr_T\|=o(\|r_T\|)
\]

noch

\[
s_{r,T}\to0.
\]

Die informelle Erwartung

\[
\text{„C6h-artige lokale Restenergie sollte }r_T\text{ kontrollieren“}
\]

ist als Forschungsrichtung zulässig, aber **noch kein bestehender Transfer**.

---

# 11. C6j kontrolliert den lokalen Separator, nicht die Residualvektoren

C6j bewies für den exakten Haarseparator `v_T` auf Radius `r_T\asymp e^{-4T}`

\[
\|R_Tv_T\|^2
\lesssim
e^{-3T}.
\]

Dies ist eine starke vektorspezifische Aussage.

Aber die C6p-Vektoren sind

\[
b_{R,T}=H_T^*Jg_{R,T}
\]

und

\[
r_T=h_T-\lambda_TA_T\mathbf1_T.
\]

Es gibt derzeit keine Darstellung

\[
b_{R,T}=c_Tv_T+\text{kontrollierter Fehler}
\]

oder

\[
r_T=d_Tv_T+\text{kontrollierter Fehler}
\]

in einer Norm, die für `R_T` stabil genug wäre.

Daher kann C6js Schätzung nicht direkt auf `q_{b,T}` oder `q_{r,T}` übertragen werden.

Zusammen mit §10 ergibt sich die Firewall

\[
\boxed{
\text{C6h/C6j liefern noch keine vektorspezifischen Screening-Fraktionen für }b_{R,T},r_T.
}
\tag{C1zB2C6p.41}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,C6h/C6j\text{-}vector\text{-}transfer\text{-}unproved}.
}
\]

---

# 12. Moving-Vector-Firewall: C6a darf nicht auf `g_{R,T}` extrapoliert werden

C6a bewies für jeden **festen** nichtnulligen ungeraden Vektor `f` auf einem festen Sourcelevel:

\[
\langle G^-_{R,T}f,f\rangle_{X,R}
\longrightarrow
+\infty.
\]

Insbesondere liefert C4/C6a für einen festen Vektor mit erstem nichtverschwindendem Jet `m` eine Untergrenze der Form

\[
\sigma_T(J_{R,T}f)
\gtrsim
\frac{e^T}{T^{2m+3}}.
\]

Der C6m-Vektor

\[
 g_{R,T}
 =
 f_{R,1}
 -
 c_{R,T}f_{R,0},
\qquad
 c_{R,T}
 =
 \frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}
 \asymp
 \frac1T,
\]

ist jedoch **nicht fest**.

Er hängt gerade so von `T` ab, dass

\[
\boxed{
\langle J_{R,T}g_{R,T},H_T\mathbf1_T\rangle=0
}
\]

für jeden großen Horizont exakt gilt.

Obwohl

\[
g_{R,T}\to f_{R,1}
\]

im festen Source-Raum, folgt daraus nicht

\[
\sigma_T(Jg_{R,T})
\sim
\sigma_T(Jf_{R,1})
\]

oder auch nur

\[
\sigma_T(Jg_{R,T})\to\infty.
\]

Der Grund ist, dass die Terminaloperatoren selbst unbeschränkt mit `T` wachsen.

Der scheinbar kleine Anteil

\[
-c_{R,T}f_{R,0}
=O(T^{-1})f_{R,0}
\]

wird durch die führende C4-Skala des `m=0`-Jets um einen zusätzlichen Faktor `T` stärker verstärkt als der `m=1`-Jet von `f_{R,1}`.

Genau deshalb liegen beide Beiträge in

\[
\langle Jg_{R,T},H_T\mathbf1_T\rangle
\]

auf derselben Größenordnung

\[
e^{T/2}T^{-3/2}
\]

und können sich per Definition von `c_{R,T}` exakt kompensieren.

Damit ist eine naive Stetigkeitsübertragung

\[
g_{R,T}\to f_{R,1}
\quad\Rightarrow\quad
\text{gleiche Terminaldivergenz}
\]

nicht zulässig.

Es bleibt offen, ob die **volle** Response-Energie `sigma_T(Jg_{R,T})` dennoch divergiert; dies erfordert einen neuen, mindestens zweiproben- oder transversalen Nachweis.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,fixed\text{-}vector\text{-}divergence\not\Rightarrow moving\text{-}g_T\text{-}divergence}.
}
\]

---

# 13. Was für `s_b` tatsächlich bewiesen werden müsste

Aus

\[
s_{b,T}
=
1-
\frac{\sigma_T(Jg_{R,T})}{\|b_{R,T}\|^2}
\]

folgt:

Eine kleine Screening-Fraktion `s_b` verlangt nicht bloß positive oder divergente Response-Energie.

Man braucht eine **relative** Aussage

\[
\boxed{
\sigma_T(Jg_{R,T})
\ge
(1-\delta_{b,T})
\|H_T^*Jg_{R,T}\|^2
}
\tag{C1zB2C6p.42}
\]

mit kontrolliertem `delta_{b,T}<1`, idealerweise `delta_{b,T}->0`.

Äquivalent genügt eine rohe Restbelastung

\[
q_{b,T}
=
\frac{\|R_TH_T^*Jg_{R,T}\|^2}
{\|H_T^*Jg_{R,T}\|^2}
\]

mit geeignetem oberen Bound.

Keine bisherige C6-Datei liefert diese Relation.

---

# 14. Was für `s_r` tatsächlich bewiesen werden müsste

Ebenso

\[
s_{r,T}
=
1-
\frac{\Delta_T^{(1)}}{\|r_T\|^2}.
\]

Kleine Screening-Fraktion `s_r` bedeutet

\[
\boxed{
\Delta_T^{(1)}
\ge
(1-\delta_{r,T})
\|r_T\|^2.
}
\tag{C1zB2C6p.43}
\]

C6j liefert nur

\[
\Delta_T^{(1)}
\gtrsim
e^{-5T}.
\]

Ohne eine obere Schranke gleicher oder vergleichbarer Skala für `||r_T||^2` folgt daraus keinerlei positive Kontrolle von

\[
1-s_{r,T}
=
\Delta_T^{(1)}/\|r_T\|^2.
\]

Alternativ genügt wieder ein Bound für

\[
q_{r,T}
=
\frac{\|R_Tr_T\|^2}{\|r_T\|^2}.
\]

Auch dieser ist offen.

---

# 15. Bare-Winkel-Seite

Selbst wenn beide Screening-Fraktionen klein wären, müsste zusätzlich eine bare correlation gezeigt werden:

\[
\beta_{R,T}
=
\frac{|\langle b_{R,T},r_T\rangle|}
{\|b_{R,T}\|\,\|r_T\|}.
\]

C6e–C6j zeigen lokale Cross-Prime-Struktur in `h_T` und konstruieren einen lokalen Separator für den zweiten Krylov-Residualmechanismus.

C6o zeigte jedoch bereits, dass diese lokale Supportstruktur nach Bildung der zusammengesetzten skalaren Korrelation nicht automatisch eine globale Nichtorthogonalität liefert.

Daher existiert derzeit kein bewiesener Bound

\[
\beta_{R,T}\ge c_R>0
\]

oder auch nur eventual

\[
\beta_{R,T}>0.
\]

Die bare angle-Seite ist somit ein eigenständiger offener Parameter.

Status:

\[
\boxed{
?[O]_{\rm bare\text{-}residual\text{-}angle\text{-}lower\text{-}bound}.
}
\]

---

# 16. Drei exakt getrennte offene Mechanismen

Nach C6p lässt sich die `2x2`-Alignmentfrage in drei unabhängige Aufgaben zerlegen:

## A. Bare correlation

\[
\boxed{
\beta_{R,T}
=
\frac{|\langle b_{R,T},r_T\rangle|}
{\|b_{R,T}\|\,\|r_T\|}.
}
\]

Gesucht: eventuale Nichtnullheit oder quantitative Untergrenze.

## B. Screening von `b`

\[
\boxed{
s_{b,T}
=
1-
\frac{\sigma_T(Jg_{R,T})}{\|b_{R,T}\|^2}.
}
\]

Gesucht: obere Schranke, idealerweise `s_b=o(1)` oder wenigstens `s_b<=1-delta_b`.

## C. Screening von `r`

\[
\boxed{
s_{r,T}
=
1-
\frac{\Delta_T^{(1)}}{\|r_T\|^2}.
}
\]

Gesucht: obere Schranke, idealerweise `s_r=o(1)` oder wenigstens `s_r<=1-delta_r`.

Sobald

\[
\boxed{
\beta_{R,T}
>
\sqrt{s_{b,T}s_{r,T}}
}
\]

gilt, ist

\[
a_{R,T}^{(2)}\ne0
\]

und damit nach C6m die `2x2`-Probe-Matrix invertierbar.

---

# 17. Konsequenz für die Strategie

C6p entscheidet nicht das Alignment.

Es zeigt jedoch, dass die C6o-Route jetzt mathematisch sauber in zwei Arten von Information zerfällt:

\[
\boxed{
\text{arithmetische/Hub-Korrelation}
\quad+
\text{vektorspezifische Rest-Spektrallokalisierung}.
}
\]

Die globale Restnorm ist dafür zu grob.

Die lokale Restanalyse von `1_T` beziehungsweise `v_T` kann nicht ohne neuen Beweis auf `b_{R,T}` oder `r_T` übertragen werden.

Und die Fixed-Vector-Divergenz aus C6a kann wegen der terminal-adaptierten Nullvektorkonstruktion nicht auf `g_{R,T}` extrapoliert werden.

Damit ist die nächste zulässige Arbeit nicht ein weiterer abstrakter Operatortrick, sondern ein **vektorspezifischer Audit**.

Der naheliegende nächste Knoten ist:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6q]
\quad
\text{Bare residual angle / vector-specific Rest loading.}
}
\]

Priorität sollte zunächst die Frage haben, welche der drei Größen

\[
\beta_{R,T},\quad q_{b,T},\quad q_{r,T}
\]

mit der bereits vorhandenen source-gekoppelten Prime-Power-Struktur überhaupt direkt zugänglich ist.

---

# 18. Was C6p ausdrücklich **nicht** beweist

C6p beweist nicht

\[
\beta_{R,T}>0,
\]

nicht

\[
s_{b,T}\to0,
\]

nicht

\[
s_{r,T}\to0,
\]

nicht

\[
\sigma_T(Jg_{R,T})\to\infty,
\]

nicht

\[
a_{R,T}^{(2)}\ne0,
\]

und daher nicht die `2x2`-Invertibilität.

Insbesondere bleibt

\[
\boxed{
?[O]_{\rm second\text{-}alignment\text{-}scalar\neq0}.
}
\]

Ebenso bleibt der quantitative `s_min`-Schritt offen.

---

# 19. Persistenz der früheren No-Gos

C6p supersediert keinen der persistenten No-Gos.

Insbesondere bleiben unverändert:

- C1y: translationinvariante positive Regulatoren lösen den Hub/Rest-Feshbach-Konflikt nicht;
- C1z-B2-A: Gamma-Preconditioning liefert keinen fehlenden endlichen Schattenmechanismus;
- C1z-B2-B: naiver Haar-`L^2`-/Normresolventenweg bleibt strukturell unzureichend;
- C4: kein fester endlicher Jet stabilisiert die rohe Terminalgeometrie;
- C6: keine treue volle Odd-Geometrie faktorisiert durch einen festen endlichen Jetquotienten;
- C6d: Orthogonalität zur ersten Probe ist kein Jet-Alignment;
- C6n: Positivität und Krylov-Rang `2` erzwingen keinen positiven Residualwinkel;
- C6o: rohe `cross-prime vs prime-pure`-Supporttrennung schließt die Feshbach-Kompensation nicht aus.

C6p fügt hinzu:

\[
\boxed{
\text{Globaler Restnorm-Bound und Fixed-Vector-Divergenz reichen nicht für die neuen moving residual vectors.}
}
\]

---

# 20. Endurteil

Die C6o-Ungleichung wird in C6p nicht bloß wiederholt, sondern in die natürliche zweikanalige Feshbach-Geometrie eingebettet.

Der Kern ist die Isometrie

\[
\boxed{
\mathfrak D_Tv
=
A_T^{-1/2}v
\oplus
(I+R_TR_T^*)^{-1/2}R_Tv,
\qquad
\|\mathfrak D_Tv\|=\|v\|.
}
\]

Daraus folgen exakt die Screening-Fraktionen

\[
\boxed{
 s_{b,T}
 =1-\frac{\sigma_T(Jg_{R,T})}{\|b_{R,T}\|^2},
\qquad
 s_{r,T}
 =1-\frac{\Delta_T^{(1)}}{\|r_T\|^2},
}
\]

und das dimensionslose Alignment-Kriterium

\[
\boxed{
\beta_{R,T}
>
\sqrt{s_{b,T}s_{r,T}}
\Longrightarrow
a_{R,T}^{(2)}\ne0.
}
\]

Noch stärker:

\[
\boxed{
\rho_{R,T}^{(2)}
\ge
\frac{
(\beta_{R,T}-\sqrt{s_{b,T}s_{r,T}})_+^2
}{
(1-s_{b,T})(1-s_{r,T})
}.
}
\]

Die Reststruktur kann über die rohen vektorspezifischen Belastungen

\[
q_{b,T}
=
\frac{\|R_Tb_{R,T}\|^2}{\|b_{R,T}\|^2},
\qquad
q_{r,T}
=
\frac{\|R_Tr_T\|^2}{\|r_T\|^2}
\]

kontrolliert werden, denn

\[
\boxed{
 s_{v,T}
 \le
 \frac{q_T(v)}{1+q_T(v)}.
}
\]

Aber keine bestehende C6-Schätzung kontrolliert `q_{b,T}` oder `q_{r,T}` bereits ausreichend.

Damit endet C6p als sauberer Reduktions- und Firewall-Knoten:

\[
\boxed{
\text{Alignment ist jetzt genau eine Frage von Bare-Winkel gegen vektorspezifisches Screening.}
}
\]

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.
