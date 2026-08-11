# P11-O3d-I2 — Signed Mean-Zero Future-Edges, scharfe Odd-Schur-Asymptotik und odd Konditionsdivergenz

**Datum:** 2026-08-11  
**Knoten:** `[P11-O3d-I2]`  
**Vorgänger:** O3d-I1  
**Direkte Schnittstellen:** C4, C5, C5c, O3c, O3d-I1  
**Modus:** `PASS-A ACTIVE`  
**Scope-Firewall:** kein O4, keine Aussage über `Theta_- -> 0`, kein Schluss auf `chi_- ||Theta_-|| -> 0`, kein starker odd Terminaltransport, kein SYN, kein Seal.

---

## 0. Urteil

O3c beweist für einen festen glatten ungeraden alten/source Testvektor `f_-` mit erstem nichtverschwindendem Boundary-Jet `m` bereits

\[
\sigma_T(J_{R,T}f_-)
\gtrsim
\frac{e^T}{T^{2m+2}}.
\]

O3d-I2 zeigt, dass die C4/O3c-Konstantenmode asymptotisch nicht nur ein Lower-Bound-Zeuge, sondern der **führende vollständige Schurmechanismus auf jeder festen ungeraden Test­richtung** ist.

Genauer gilt:

\[
\boxed{
\sigma_T(J_{R,T}f_-)
=
c_m^2\,|\beta_R^{(m)}(f_-)|^2
\frac{e^T}{T^{2m+2}}
\bigl(1+o_{R,f_-}(1)\bigr).
}
\tag{I2.1}
\]

Hier

\[
c_m=\frac{\binom{2m}{m}}{4^m}.
\]

Damit ist insbesondere

\[
\boxed{
\sigma_T(J_{R,T}f_-)
\asymp_{R,f_-}
\frac{e^T}{T^{2m+2}}.
}
\tag{I2.2}
\]

Die offene O3a-Frage nach der odd Konditionierung ist dadurch entschieden: Für jedes feste `R<T_0` gilt

\[
\boxed{
\kappa(A_{T_0,U}^{R,-})\longrightarrow\infty
\qquad(U\to\infty).
}
\tag{I2.3}
\]

Sogar stärker: für jedes feste `N>0`

\[
\boxed{
U^{-N}\,\kappa(A_{T_0,U}^{R,-})\longrightarrow\infty.
}
\tag{I2.4}
\]

und daher ebenso für

\[
\chi_{T_0,U}^{R,-}=\kappa(A_{T_0,U}^{R,-})^{1/4}:
\]

\[
\boxed{
\forall N>0:\quad
U^{-N}\chi_{T_0,U}^{R,-}\longrightarrow\infty.
}
\tag{I2.5}
\]

Dies ist eine **fixed-base-terminal** Aussage. Es wird keine gemeinsame `T_0,U->infty`-Asymptotik behauptet.

Status:

\[
\boxed{
\begin{aligned}
[P11\text{-}O3d\text{-}I2]
&\quad \checkmark[M]_{\rm even\;hub\;mean\text{-}zero\;decomposition}\\
&+\checkmark[M]_{\rm signed\;future\text{-}edge\;geometry}\\
&+\checkmark[M]_{\rm signed\;continuous\;dual\;identity}\\
&+\checkmark[M]_{\rm signed\;future\text{-}prime\;quadrature}\\
&+\checkmark[M]_{\rm full\text{-}rest\;lift\;via\;I1}\\
&+\checkmark[M]_{\rm sharp\;odd\;Schur\;asymptotic}\\
&+\checkmark[M]_{\rm odd\;conditioning\;divergence}\\
&+\checkmark[M]_{\rm odd\;conditioning\;superpolynomial}\\
&+?[O]_{\Theta^-_{T_0,U}\to0}\\
&+?[O]_{\chi^{R,-}_{T_0,U}\|\Theta^-_{T_0,U}\|\to0}\\
&+?[O]_{W_{R,S,-}^{[T]}\;\rm strong\;Cauchy}.
\end{aligned}
}
\]

---

# 1. Verbindliche Ausgangsdaten

Fixiere `R>0` und

\[
0\ne f_-
\in C_c^\infty((-R,R)),
\qquad
f_-(-u)=-f_-(u).
\]

Sei

\[
m=m(f_-)
:=
\min\{j\ge0:\beta_R^{(j)}(f_-)\ne0\}.
\]

Nach C5 ist `m<infty` für jeden nichttrivialen glatten ungeraden Testvektor.

Setze auf Terminallevel `T>R`

\[
h_T:=H_T^*J_{R,T}f_-.
\tag{I2.6}
\]

C5 zeigt, dass `H_T^*` die Parität wechselt. Daher ist

\[
\boxed{h_T\text{ gerade}.}
\tag{I2.7}
\]

Der Schurterm lautet nach C4/O3d-I1

\[
\boxed{
\sigma_T(J_{R,T}f_-)
=
\langle h_T,A_T^{-1}h_T\rangle,
\qquad
A_T=I+R_T^*R_T
=I+\widetilde R_T^*\widetilde R_T.
}
\tag{I2.8}
\]

O3d-I1 liefert die exakte Full-Rest-Dualform

\[
\boxed{
\sigma_T(J_{R,T}f_-)
=
\inf_{Y\in\mathscr Z_T}
\bigl(
\|h_T-\widetilde R_T^*Y\|_2^2
+
\|Y\|_{\mathscr Z_T}^2
\bigr).
}
\tag{I2.9}
\]

C4 liefert für

\[
\ell_T(f_-):=
\langle h_T,\mathbf1_T\rangle
=
\langle J_{R,T}f_-,H_T\mathbf1_T\rangle
\]

die asymptotische Entwicklung

\[
\boxed{
\ell_T(f_-)
=
-\sqrt2\,c_m\beta_R^{(m)}(f_-)
\frac{e^{T/2}}{T^{m+1/2}}
\bigl(1+O_{R,f_-,m}(T^{-1})\bigr).
}
\tag{I2.10}
\]

O3c beweist

\[
\boxed{
\langle\mathbf1_T,A_T\mathbf1_T\rangle
=2T+O(1).
}
\tag{I2.11}
\]

Daher bereits

\[
\sigma_T(Jf_-)
\ge
\frac{|\ell_T(f_-)|^2}{2T+O(1)}
=
c_m^2|\beta_R^{(m)}(f_-)|^2
\frac{e^T}{T^{2m+2}}
(1+O(T^{-1})).
\tag{I2.12}
\]

Für (I2.1) fehlt nur eine asymptotisch matching Full-Rest-Dual-Upper-Bound.

---

# 2. Zerlegung des Hubs: wachsender primitiver Block plus harmloser Rest

Wähle wie in C5c

\[
\rho_f<R,
\qquad
\operatorname{supp}f_-\subset(-\rho_f,\rho_f),
\]

sowie festes

\[
a_*>\rho_f+2\varepsilon
\]

für die C5c-Anchorreserve.

Für primitive Primzahlen setze

\[
a_p:=\frac12\log p,
\qquad
c_p:=\sqrt{\log p}\,p^{-3/4},
\qquad
d_p:=T-a_p.
\]

Definiere den wachsenden primitiven Hub

\[
\boxed{
h_T^{\rm grow}
:=
\sum_{p:\,a_*\le a_p\le T}
 c_pD_{\log p}^*J_{R,T}f_-.
}
\tag{I2.13}
\]

und den Rest

\[
\boxed{h_T^{\rm rem}:=h_T-h_T^{\rm grow}.}
\tag{I2.14}
\]

`h_T^{rem}` besteht aus

1. dem festen endlichen primitiven Small-Prime-Block `a_p<a_*`;
2. allen höheren Prime-Powers `k>=2`.

Für den Small-Prime-Block ist die `L^2`-Norm offensichtlich `O_{R,f}(1)`.

Für `k>=2` gilt wegen `||D_s||<=2`

\[
\begin{aligned}
\|h_T^{(\ge2)}\|_2
&\le
2\|f_-\|_2
\sum_p\sum_{k\ge2}
\sqrt{\log p}\,p^{-3k/4}\\
&<\infty,
\end{aligned}
\]

weil bereits die `k=2`-Hülle

\[
\sum_p\sqrt{\log p}\,p^{-3/2}
\]

konvergiert.

Somit

\[
\boxed{
\sup_T\|h_T^{\rm rem}\|_2<\infty.
}
\tag{I2.15}
\]

Daher auch

\[
\boxed{
|\langle h_T^{\rm rem},\mathbf1_T\rangle|
=O_{R,f}(\sqrt T).
}
\tag{I2.16}
\]

---

# 3. Boundary-Kern des wachsenden primitiven odd Hubs

Sei

\[
e\in\mathscr H_T^+
\]

gerade und definiere auf der positiven Hälfte

\[
\boxed{
b_T(t):=e(T-t),\qquad0<t<T.}
\tag{I2.17}
\]

Für `a_p>=rho_f` und `u>0` gilt bei geradem `e` exakt

\[
D_{\log p}E_Te(u)
=
1_{\{u\le d_p\}}b_T(d_p-u)
-
b_T(d_p+u).
\tag{I2.18}
\]

Da `f_-` ungerade ist, folgt nach denselben Variablentransformationen wie in C5c, aber mit umgekehrtem Vorzeichen:

\[
\boxed{
\langle f_-,D_{\log p}E_Te\rangle
=
-2\int_0^T f_-(t-d_p)b_T(t)\,dt.
}
\tag{I2.19}
\]

Damit

\[
\boxed{
\langle h_T^{\rm grow},e\rangle
=
\int_0^T k_T(t)b_T(t)\,dt
}
\tag{I2.20}
\]

mit

\[
\boxed{
k_T(t)
:=-2
\sum_{p:\,a_*\le a_p\le T}
 c_pf_-(t-d_p).
}
\tag{I2.21}
\]

Der einzige Unterschied zur C5c-Kernformel ist ein globales Minuszeichen und die Parität des festen Tests. Alle absoluten PNT-/Glattheitsabschätzungen aus C5c §7 bleiben daher unverändert.

Insbesondere, mit

\[
A:=T-t,
\]

gilt

\[
\boxed{
|k_T(t)|+|k_T'(t)|
\le
C_{R,f_-}
\frac{e^{A/2}}{\sqrt{1+A}}.
}
\tag{I2.22}
\]

Daraus wie in C5c:

\[
\boxed{
 e^{-T}
\int_0^T e^{t/2}|k_T(t)|^2dt
=O_{R,f_-}(T^{-1})+O(e^{-T/4}).
}
\tag{I2.23}
\]

---

# 4. Exakte Mittelwertabspaltung

Setze

\[
\boxed{
K_T:=\int_0^Tk_T(t)dt
=
\langle h_T^{\rm grow},\mathbf1_T\rangle.
}
\tag{I2.24}
\]

Aus (I2.10) und (I2.16):

\[
\ell_T(f_-)
=K_T+O(\sqrt T).
\tag{I2.25}
\]

Da `ell_T` exponentiell groß ist, folgt

\[
\boxed{
K_T
=
-\sqrt2\,c_m\beta_R^{(m)}(f_-)
\frac{e^{T/2}}{T^{m+1/2}}
(1+O(T^{-1})+o(1)).
}
\tag{I2.26}
\]

Insbesondere

\[
|K_T|\to\infty.
\]

Definiere

\[
\boxed{
\mu_T:=\frac{K_T}{2T},
\qquad
 g_T^{\rm grow}:=h_T^{\rm grow}-\mu_T\mathbf1_T.
}
\tag{I2.27}
\]

Dann ist `g_T^{grow}` gerade und exakt mittelwertfrei:

\[
\boxed{
\langle g_T^{\rm grow},\mathbf1_T\rangle=0.
}
\tag{I2.28}
\]

Auf Boundary-Ebene entspricht dies

\[
\boxed{
k_T^0(t):=k_T(t)-\frac{K_T}{T}}
\tag{I2.29}
\]

mit

\[
\boxed{
\int_0^Tk_T^0(t)dt=0.
}
\tag{I2.30}
\]

Der euklidische Preis der abgespaltenen Konstantenmode ist

\[
\boxed{
M_T
:=
\|\mu_T\mathbf1_T\|_2^2
=
\frac{|K_T|^2}{2T}.
}
\tag{I2.31}
\]

Mit (I2.26):

\[
\boxed{
M_T
=
c_m^2|\beta_R^{(m)}(f_-)|^2
\frac{e^T}{T^{2m+2}}
(1+o(1)).
}
\tag{I2.32}
\]

---

# 5. Signed Future-Edge-Geometrie für gerade Terminalvektoren

Betrachte eine primitive Future-Primzahl `q` und setze

\[
a_q=\frac12\log q,
\qquad
r_q=T-a_q.
\]

Auf dem primitiven Overlap `|u|<=r_q` setze

\[
t=r_q-u,
\qquad
s=r_q+u.
\]

Dann

\[
T-t=a_q+u,
\qquad
T-s=a_q-u.
\]

Da `e` gerade ist,

\[
e(u-a_q)=e(a_q-u).
\]

Daher gilt exakt

\[
\boxed{
D_{\log q}E_Te(u)
=
b_T(t)-b_T(s)
=
b_T(t)-b_T(2r_q-t).
}
\tag{I2.33}
\]

Der odd-Source/even-Hub-Kanal erzeugt somit **signed reflection edges**

\[
\boxed{
\mathsf E_r^-b(t)
:=
b(t)-b(2r-t).
}
\tag{I2.34}
\]

im Gegensatz zu den signless edges des C5c-even-Source-Kanals.

---

# 6. Exakte kontinuierliche Mean-Zero-Identität

Wähle dieselbe feste Anchor-Dichte wie C5c:

\[
\alpha\in C_c^\infty((0,\varepsilon)),
\qquad
\int_0^\varepsilon\alpha(s)ds=1.
\]

Wegen (I2.30) gilt für jedes `b` exakt

\[
\begin{aligned}
\int_0^Tk_T^0(t)b(t)dt
&=
\int_0^T\int_0^\varepsilon
k_T^0(t)\alpha(s)
[b(t)-b(s)]\,ds\,dt.
\end{aligned}
\]

Also

\[
\boxed{
\int k_T^0b
=
\iint k_T^0(t)\alpha(s)
[b(t)-b(s)]\,ds\,dt.
}
\tag{I2.35}
\]

Es ist **kein Anchor-Anchor-Korrekturterm** nötig: genau die Mean-Zero-Bedingung entfernt ihn.

Setze

\[
r=\frac{t+s}{2},
\qquad
s=2r-t.
\]

Dann

\[
\boxed{
C_T^-(r,t)
:=2k_T^0(t)\alpha(2r-t)
}
\tag{I2.36}
\]

und

\[
\boxed{
\int k_T^0b
=
\iint
C_T^-(r,t)
[b(t)-b(2r-t)]\,dt\,dr.
}
\tag{I2.37}
\]

Da `0<t<T` und `0<s<epsilon`, gilt auf dem Support

\[
0<r<\frac{T+\varepsilon}{2}.
\]

Somit gehören alle benötigten Primzahlen zur Future-Skala

\[
\boxed{
a_q=T-r\ge T/2-O(1).}
\tag{I2.38}
\]

---

# 7. Kontinuierliche Zertifikatskosten

Wie in C5c ist die kontinuierliche primitive Restmassendichte

\[
m_T(r)=2e^{T-r}.
\]

Definiere

\[
Y_T^{\rm cont,-}(r,t)
:=
\frac{C_T^-(r,t)}{\sqrt{m_T(r)}}.
\]

Dann erzeugt das kontinuierliche signed Edge-Adjungierte exakt `k_T^0`.

Für die Norm gilt nach `s=2r-t`, `dr=ds/2`:

\[
\boxed{
\|Y_T^{\rm cont,-}\|^2
\le
C_\alpha e^{-T}
\int_0^Te^{t/2}|k_T^0(t)|^2dt.
}
\tag{I2.39}
\]

Mit

\[
|k_T^0|^2
\le2|k_T|^2+2|K_T|^2/T^2
\]

und (I2.23):

\[
\boxed{
\|Y_T^{\rm cont,-}\|^2
\le
\frac{C_{R,f}}{T}
+
C_{R,f}\frac{|K_T|^2e^{-T/2}}{T^2}
+O(e^{-T/4}).
}
\tag{I2.40}
\]

Verglichen mit `M_T=|K_T|^2/(2T)` gilt daher

\[
\boxed{
\|Y_T^{\rm cont,-}\|^2=o(M_T).
}
\tag{I2.41}
\]

Denn

\[
\frac{T^{-1}}{M_T}
\ll e^{-T}T^{2m+1}	o0
\]

und

\[
\frac{|K_T|^2e^{-T/2}/T^2}{M_T}
\ll e^{-T/2}/T	o0.
\]

---

# 8. Diskrete Future-Prime-Quadratur für signed edges

Die C5c-Short-interval-PNT- und Zellnormalisierungsarchitektur ist vorzeichenblind.

Für jede Future-Zelle `I` mit

\[
W_I=\sum_{q:r_q\in I}w_q
\]

verwende wie C5c

\[
\lambda_q^{(I)}
:=
|I|\frac{w_q}{W_I},
\qquad
\sum_{q:r_q\in I}\lambda_q^{(I)}=|I|.
\tag{I2.42}
\]

Die Kostenidentität bleibt exakt

\[
\boxed{
\sum_{q:r_q\in I}
\frac{|\lambda_q^{(I)}|^2}{w_q}
=
\frac{|I|^2}{W_I}
\lesssim
\frac{|I|}{m_T(r_I)}.
}
\tag{I2.43}
\]

Definiere im primitiven Future-`q`-Kanal das signed Zertifikat durch denselben Koeffizienten `C_T^-` statt des C5c-signless Koeffizienten.

Da Kosten nur Quadrate der Koeffizienten sehen, folgt aus (I2.39)--(I2.43):

\[
\boxed{
\|Y_T^{\rm prim,-}\|^2
\le
\frac{C_{R,f}}{T}
+
C_{R,f}\frac{|K_T|^2e^{-T/2}}{T^2}
+o(M_T).
}
\tag{I2.44}
\]

Insbesondere

\[
\boxed{
\|Y_T^{\rm prim,-}\|^2=o(M_T).
}
\tag{I2.45}
\]

## 8.1 Quadraturrest

Für den ursprünglichen Kern `k_T` gilt nach dem C5c-Zellargument unverändert ein exponentiell kleiner Source-Quadraturrest, da (I2.22) dieselbe absolute Glattheit besitzt wie C5c.

Der neue konstante Kernanteil `-K_T/T` hat Ableitung null. In der Hilbertraum-wertigen `r`-Darstellung kommt die `r`-Ableitung nur aus der festen Anchor-Funktion und der Reflection-Translation. Daher

\[
\sup_r\|\partial_r\Phi^{\rm const}_T(r)\|_2
\le
C_\alpha\frac{|K_T|}{T}.
\tag{I2.46}
\]

Alle verwendeten Zellen erfüllen wegen (I2.38) und C5c

\[
\boxed{
\max_I|I|
\le
C e^{-2T/5}.
}
\tag{I2.47}
\]

Außerdem ist die Gesamtlänge des `r`-Bereichs `O(T)`. Daher

\[
\sum_I|I|^2
\le
(\max_I|I|)\sum_I|I|
\le
CTe^{-2T/5}.
\tag{I2.48}
\]

Mit der C5c-Quadraturfehlerform folgt für den konstanten Anteil

\[
\boxed{
\|Z_T^{\rm quad,const}\|_2
\le
C|K_T|e^{-2T/5}.
}
\tag{I2.49}
\]

Zusammen mit dem ursprünglichen glatten Anteil:

\[
\boxed{
\|Z_T^{\rm quad}\|_2
\le
C_{R,f}e^{-cT}
+C_{R,f}|K_T|e^{-2T/5}.
}
\tag{I2.50}
\]

Da

\[
\sqrt{M_T}=\frac{|K_T|}{\sqrt{2T}},
\]

folgt

\[
\boxed{
\|Z_T^{\rm quad}\|_2=o(\sqrt{M_T}).
}
\tag{I2.51}
\]

---

# 9. Lift in den vollen Rest via O3d-I1

O3d-I1 identifiziert den vollen Future-`a=0`-Kanal als

\[
\widetilde R_{T,0}^{\rm fut}
=
P_T^{\rm fut}+E_T^{\rm fut}
\]

mit

\[
\boxed{
\|E_T^{\rm fut}\|
\le
C\sqrt{T+1}e^{-T/2}.
}
\tag{I2.52}
\]

Lifte `Y_T^{prim,-}` isometrisch in den `a=0`-Teil des kanonischen Full-Rest-Zielraums und nenne den Lift `\widehat Y_T^-`.

Dann

\[
\widetilde R_T^*\widehat Y_T^-
=
(P_T^{\rm fut})^*Y_T^{\rm prim,-}
+
(E_T^{\rm fut})^*\widehat Y_T^-.
\]

Absorbiere den Tail in

\[
Z_T^{\rm tail}
:=
-(E_T^{\rm fut})^*\widehat Y_T^-.
\]

Dann

\[
\|Z_T^{\rm tail}\|_2
\le
\|E_T^{\rm fut}\|\,\|Y_T^{\rm prim,-}\|.
\]

Aus (I2.45) und (I2.52):

\[
\boxed{
\|Z_T^{\rm tail}\|_2=o(\sqrt{M_T}).
}
\tag{I2.53}
\]

und

\[
\boxed{
\|\widehat Y_T^-\|^2=o(M_T).
}
\tag{I2.54}
\]

Damit existiert eine Full-Rest-Dualzerlegung

\[
\boxed{
 g_T^{\rm grow}
=
\widetilde R_T^*\widehat Y_T^-
+
Z_T^{\rm quad}
+
Z_T^{\rm tail}.
}
\tag{I2.55}
\]

---

# 10. Full-Hub-Dualzerlegung

Aus

\[
h_T
=
\mu_T\mathbf1_T
+
g_T^{\rm grow}
+
h_T^{\rm rem}
\]

und (I2.55):

\[
\boxed{
 h_T
=
\widetilde R_T^*\widehat Y_T^-
+
Z_T^{\rm full},
}
\tag{I2.56}
\]

mit

\[
\boxed{
Z_T^{\rm full}
:=
\mu_T\mathbf1_T
+
h_T^{\rm rem}
+
Z_T^{\rm quad}
+
Z_T^{\rm tail}.
}
\tag{I2.57}
\]

Nach (I2.15), (I2.51), (I2.53) und

\[
\|\mu_T\mathbf1_T\|=\sqrt{M_T}\to\infty
\]

gilt

\[
\boxed{
\|h_T^{\rm rem}+Z_T^{\rm quad}+Z_T^{\rm tail}\|_2
=o(\sqrt{M_T}).
}
\tag{I2.58}
\]

Somit

\[
\boxed{
\|Z_T^{\rm full}\|_2^2
=M_T(1+o(1)).
}
\tag{I2.59}
\]

Zusammen mit (I2.54):

\[
\boxed{
\|\widehat Y_T^-\|^2
+
\|Z_T^{\rm full}\|^2
=M_T(1+o(1)).
}
\tag{I2.60}
\]

---

# 11. Matching Upper Bound und scharfe Schur-Asymptotik

Setze (I2.56) in die Full-Rest-Dualform (I2.9) ein:

\[
\boxed{
\sigma_T(J_{R,T}f_-)
\le
M_T(1+o(1)).
}
\tag{I2.61}
\]

Andererseits liefert O3c/C4

\[
\sigma_T(J_{R,T}f_-)
\ge
\frac{|\ell_T(f_-)|^2}{2T+O(1)}.
\tag{I2.62}
\]

Aus (I2.25) und (I2.26):

\[
\frac{|\ell_T(f_-)|^2}{2T+O(1)}
=M_T(1+o(1)).
\tag{I2.63}
\]

Daher Squeeze:

\[
\boxed{
\sigma_T(J_{R,T}f_-)
=M_T(1+o(1)).
}
\tag{I2.64}
\]

Mit (I2.32):

\[
\boxed{
\sigma_T(J_{R,T}f_-)
=
c_m^2|\beta_R^{(m)}(f_-)|^2
\frac{e^T}{T^{2m+2}}
(1+o(1)).
}
\tag{I2.65}
\]

Dies beweist (I2.1).

**Interpretation.** Für jede feste odd Richtung ist der vollständige Feshbach-Schurterm asymptotisch bis zum führenden Koeffizienten durch die euklidische Projektion des wachsenden primitiven Hubs auf die Terminalkonstante bestimmt. Die übrige even Hubkomponente wird durch signed Future-Edges asymptotisch billiger gescreent.

---

# 12. Konsequenz für die odd Zukunftsmetrik

Die exakte Metrikzerlegung lautet

\[
\langle G_{R,T}f_-,f_-\rangle
=q_{\Gamma,R}(f_-)
+\sigma_T(J_{R,T}f_-).
\]

Der Gamma-Term ist `T`-unabhängig. Daher aus (I2.65):

\[
\boxed{
\langle G_{R,T}f_-,f_-\rangle
\sim
c_m^2|\beta_R^{(m)}(f_-)|^2
\frac{e^T}{T^{2m+2}}.
}
\tag{I2.66}
\]

Insbesondere kennen wir nun für **jede feste glatte odd Richtung** nicht nur Divergenz, sondern die exakte führende Wachstumsordnung.

---

# 13. Odd Konditionsdivergenz

Fixiere nun

\[
R<T_0.
\]

Für `U>T_0` setze wie O3a

\[
\rho_{T_0,U}(f)
:=
\frac{\langle G_{R,U}f,f\rangle}
{\langle G_{R,T_0}f,f\rangle}.
\]

O3a.3 beweist

\[
\kappa(A_{T_0,U}^{R,-})
=
\frac{\sup_{f_-\ne0}\rho_{T_0,U}(f_-)}
{\inf_{f_-\ne0}\rho_{T_0,U}(f_-)}.
\tag{I2.67}
\]

Wähle einen glatten odd Test `f_0` mit

\[
\beta_R^{(0)}(f_0)\ne0.
\]

Für jedes `M>=1` liefert die C4-Jet-Unabhängigkeit einen glatten Test mit

\[
\beta_R^{(0)}=\cdots=\beta_R^{(M-1)}=0,
\qquad
\beta_R^{(M)}\ne0.
\]

Da alle `beta_R^{(j)}` den geraden Anteil annihilieren, kann dieser Test odd projiziert werden, ohne die Jetwerte zu verändern. Nenne ihn `f_M`.

Dann aus (I2.66):

\[
\rho_{T_0,U}(f_0)
\sim
C_0\frac{e^U}{U^2},
\]

\[
\rho_{T_0,U}(f_M)
\sim
C_M\frac{e^U}{U^{2M+2}},
\]

mit festen positiven Konstanten `C_0,C_M`.

Somit

\[
\boxed{
\frac{\rho_{T_0,U}(f_0)}
{\rho_{T_0,U}(f_M)}
\sim
C_{M,R,T_0}\,U^{2M}.
}
\tag{I2.68}
\]

Daher

\[
\boxed{
\kappa(A_{T_0,U}^{R,-})
\ge
c_{M,R,T_0}U^{2M}
\qquad(U\gg1).
}
\tag{I2.69}
\]

für jedes feste `M`.

Folglich

\[
\boxed{
\forall N>0:\quad
U^{-N}\kappa(A_{T_0,U}^{R,-})\to\infty.
}
\tag{I2.70}
\]

und wegen

\[
\chi_{T_0,U}^{R,-}
=
\kappa(A_{T_0,U}^{R,-})^{1/4}
\]

gleichfalls

\[
\boxed{
\forall N>0:\quad
U^{-N}\chi_{T_0,U}^{R,-}\to\infty.
}
\tag{I2.71}
\]

Dies löst die O3a-Frage

\[
\chi_{T_0,U}^{R,-}\text{ bounded oder divergent?}
\]

für festen Basisterminalhorizont eindeutig zugunsten

\[
\boxed{\chi_{T_0,U}^{R,-}\to\infty.}
\]

---

# 14. Neue notwendige Bedingung für die Klasse-O-Route

O3 liefert auf dem odd Sektor

\[
\|Q_- -W_{T_0,-}\|^2
\le
2\chi_{T_0,U}^{R,-}
\|\Theta^-_{T_0,U}\|.
\tag{I2.72}
\]

Soll die rechte Seite gegen null gehen, so ist wegen (I2.71) notwendig:

\[
\boxed{
\forall N>0:\quad
U^N\|\Theta^-_{T_0,U}\|\longrightarrow0.
}
\tag{I2.73}
\]

Denn für jedes `N` existiert eine positive Konstante `c_N` mit

\[
\chi_{T_0,U}^{R,-}\ge c_NU^N
\]

für große `U`.

Damit wird das nächste Klasse-O-Gate stark verschärft:

\[
\boxed{
\chi_-\|\Theta_-\|\to0
\Longrightarrow
\Theta_-\text{ muss bei festem }T_0
\text{ schneller als jede Potenz in }U^{-1}\text{ zerfallen.}
}
\tag{I2.74}
\]

**Firewall:** Dies beweist nicht, dass ein solcher superschneller Zerfall unmöglich ist.

---

# 15. Firewalls

## I2-FW1 — fixed base terminal only

Alle Konditionsaussagen in §§13–14 gelten für

\[
R<T_0\text{ fest},
\qquad U\to\infty.
\]

Keine gemeinsame `T_0,U->infty`-Asymptotik wird behauptet.

## I2-FW2 — `chi_- -> infty` ist kein Transport-No-Go

\[
\boxed{
\chi_{T_0,U}^{R,-}\to\infty
\not\Rightarrow
W_{R,S,-}^{[T]}\text{ konvergiert nicht stark}.}
\]

Entscheidend bleibt

\[
\chi_-\|\Theta_-\|.
\]

## I2-FW3 — `Theta_-` bleibt offen

I2 beweist weder

\[
\Theta^-_{T_0,U}\to0
\]

noch irgendeine quantitative Unter- oder Obergrenze dafür.

## I2-FW4 — Full-Rest-Repair aus I1 bleibt die einzige verwendete Transferarchitektur

Es wird nirgends

\[
R_T^*R_T\ge(R_T^{(1)})^*R_T^{(1)}
\]

benutzt oder bewiesen.

## I2-FW5 — keine Aussage über C1z-B1 primitive Lower-Extraktion

Die alte primitive Lower-Extraktionsfrage bleibt unabhängig offen.

## I2-FW6 — kein O4, kein SYN, kein Seal

Der neue positive Endpunkt ist

\[
\boxed{
\text{scharfe odd Schur-Asymptotik}
+
\text{superpolynomiale odd relative Konditionsdivergenz}.
}
\]

Der Jensen-Defekt und der starke odd Terminaltransport bleiben offen.

---

# 16. Autoritativer Status nach I2

\[
\boxed{
\begin{array}{lll}
\text{C5d.1--C5d.3} & = & \checkmark[M]\quad\text{(durch I1 repariert)},\\
\text{O3a.1} & = & \checkmark[M]\quad\text{(durch I1 repariert)},\\
\text{O3a.2--O3a.4} & = & \checkmark[M],\\
\text{O3c} & = & \checkmark[M],\\
\text{odd matching upper bound} & = & \checkmark[M],\\
\text{sharp odd Schur asymptotic} & = & \checkmark[M],\\
\chi_{T_0,U}^{R,-}\to\infty & = & \checkmark[M]\quad(T_0\text{ fest}),\\
\Theta^-_{T_0,U}\to0 & = & ?[O],\\
\chi_{T_0,U}^{R,-}\|\Theta^-_{T_0,U}\|\to0 & = & ?[O],\\
W_{R,S,-}^{[T]}\text{ strong Cauchy} & = & ?[O].
\end{array}
}
\]

Der nächste mathematisch zulässige Angriff ist damit **nicht** mehr eine weitere Konditionsabschätzung, sondern die direkte quantitative Analyse des odd Jensen-Defekts `Theta^-_{T_0,U}` gegen die notwendige superpolynomiale Zerfallsskala (I2.73).