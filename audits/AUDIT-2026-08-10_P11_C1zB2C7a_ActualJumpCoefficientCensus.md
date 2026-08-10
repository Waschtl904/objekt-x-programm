# P11-C1z-B2-C7a — Actual Jump Coefficient Census und integrierte R3-Observability

**Datum:** 2026-08-10  
**Programm:** P11 / C1z / B2 / C7  
**Knoten:** `[P11-C1z-B2-C7a]`  
**Vorgänger:** C6z — `C6Closure_ResidualSpectralBlocker_CompletionDecision`  
**Block:** `ResidualArithmeticObservability_WindowedExponentialSums`  
**Modus:** `PASS-A ACTIVE`  
**Scope:** erster C7-Knoten; exakter Zensus der tatsächlichen Sprungkoeffizienten des Residualvektors, keine SYN-, Seal- oder Paper-Aktion.

---

## 0. Auditstatus

\[
\boxed{
\begin{aligned}
[P11\text{-}C1z\text{-}B2\text{-}C7a]
&\quad \checkmark[K/M]_{\rm part}\\
&+\checkmark[M]_{\rm pos,exact\text{-}residual\text{-}jump\text{-}census}\\
&+\checkmark[M]_{\rm pos,exact\text{-}hub\text{-}integer\text{-}kernel}\\
&+\checkmark[M]_{\rm pos,exact\text{-}rest\text{-}layer\text{-}coefficients}\\
&+\checkmark[M]_{\rm pos,actual\text{-}vs\text{-}candidate\text{-}breakpoint\text{-}test}\\
&+\checkmark[M]_{\rm pos,protected\text{-}lambda\text{-}free\text{-}residual\text{-}jump\text{-}pair}\\
&+\checkmark[M]_{\rm pos,fixed\text{-}T\text{-}integrated\text{-}R3\text{-}mean}\\
&+\checkmark[M]_{\rm neg,single\text{-}protected\text{-}pair\not\Rightarrow pointwise\text{-}R3}\\
&+\checkmark[M]_{\rm neg,global\text{-}pointwise\text{-}P\text{-}lower\text{-}bound}\\
&+\checkmark[M]_{\rm corr,log\text{-}form\text{-}location\not\Rightarrow coefficient\text{-}observability}\\
&+?[O]_{\rm quantitative\text{-}integrated\text{-}R3\text{-}on\text{-}relevant\text{-}band}\\
&+?[O]_{\rm second\text{-}protected\text{-}pair\;or\;offdiagonal\text{-}Gram\text{-}control}\\
&+?[O]_{\rm window\text{-}lower\text{-}transfer}\\
&+?[O]_{\rm q_{r,T}\;asymptotic}\\
&+?[O]_{\rm a_{R,T}^{(2)}\neq0}.
\end{aligned}
}
\]

### Kernurteil

C7a erreicht den geplanten **ActualJumpCoefficientCensus** in einer exakten, endlichen Form.

Für die Nullfortsetzung des Residualvektors

\[
\widetilde r_T
=\widetilde h_T
-\lambda_T\widetilde{\mathbf1_T}
-\lambda_T\widetilde g_T,
\qquad
 g_T:=R_T^*R_T\mathbf1_T,
\]

werden die tatsächlichen Sprungkoeffizienten

\[
J_T(\beta):=\operatorname{Jump}_\beta\widetilde r_T
\]

nicht länger nur durch Kandidatenlagen beschrieben, sondern durch die exakte Aggregationsformel

\[
\boxed{
J_T(\beta)
=J_{h,T}(\beta)
-\lambda_TJ_{1,T}(\beta)
-\lambda_TJ_{g,T}(\beta).
}
\tag{C1zB2C7a.1}
\]

Die Hubkoeffizienten besitzen einen exakten endlichen ganzzahligen Shift-Kernel; die Restkoeffizienten besitzen nach C6hs p-Tiefenzerlegung exakte layerweise skalare Koeffizienten und einen exakten Rücktransport. Dadurch ist erstmals sauber getrennt zwischen

\[
\text{Kandidatenlage}
\quad\text{und}\quad
\text{tatsächlichem nichtverschwindendem Residualsprung}.
\]

C6i liefert außerdem ein geschütztes symmetrisches Sprungpaar

\[
\boxed{
\pm x_T,
\qquad
|J_T(x_T)|\ge j_*>0,
\qquad
J_T(-x_T)=-J_T(x_T),
}
\tag{C1zB2C7a.2}
\]

bei dem die Rest- und Identitätskoeffizienten exakt verschwinden. Dieses Paar ist also **lambda-frei**.

Ein einzelnes geschütztes Paar liefert aber keine punktweise Observability von

\[
P_T(\xi)=\sum_\beta J_T(\beta)e^{-i\xi\beta}.
\]

Stattdessen ergibt C7a einen neuen exakten integrierten Satz:

\[
\boxed{
\lim_{X\to\infty}
\frac1{2X}
\int_{-X}^{X}|P_T(\xi)|^2\,d\xi
=
\sum_{\beta\in\mathcal B_T^{\rm act}}|J_T(\beta)|^2
\ge 2j_*^2
}
\tag{C1zB2C7a.3}
\]

für jedes hinreichend große **feste** `T`.

Dies ist eine echte finite-horizon R3-Observability auf Koeffizientenebene. Was noch fehlt, ist eine quantitative, in `T` kontrollierte Version auf dem C6z-relevanten endlichen Frequenzband sowie der Transfer zurück zu den komprimierten Martingalkanälen.

---

# 1. Verbindliche Daten aus C6z

Wir arbeiten auf

\[
\mathscr H_T=L^2(-T,T)
\]

mit

\[
A_T=I+R_T^*R_T,
\]

\[
h_T=H_T^*H_T\mathbf1_T,
\]

\[
\lambda_T
=\frac{\langle\mathbf1_T,h_T\rangle}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle},
\]

und

\[
\boxed{
r_T=h_T-\lambda_TA_T\mathbf1_T.}
\tag{C1zB2C7a.4}
\]

Also exakt

\[
\boxed{
r_T
=h_T-\lambda_T\mathbf1_T
-\lambda_TR_T^*R_T\mathbf1_T.}
\tag{C1zB2C7a.5}
\]

Setze

\[
\boxed{g_T:=R_T^*R_T\mathbf1_T.}
\tag{C1zB2C7a.6}
\]

C6y/C6z verwenden die Nullfortsetzung auf ganz `R`. Diese Konvention wird hier beibehalten.

Für jede stückweise konstante Nullfortsetzung `f` schreiben wir

\[
\boxed{
J_f(\beta)
:=f(\beta+)-f(\beta-).
}
\tag{C1zB2C7a.7}
\]

Die Menge ihrer tatsächlichen Breakpoints ist

\[
\boxed{
\mathcal B^{\rm act}(f)
:=\{\beta\in\mathbb R:J_f(\beta)\ne0\}.
}
\tag{C1zB2C7a.8}
\]

Insbesondere

\[
\mathcal B_T^{\rm act}
:=\mathcal B^{\rm act}(\widetilde r_T).
\]

C6y liefert exakt

\[
D\widetilde r_T
=\sum_{\beta\in\mathcal B_T^{\rm act}}
J_T(\beta)\delta_\beta,
\]

mit

\[
J_T(\beta):=J_{\widetilde r_T}(\beta),
\]

und

\[
\boxed{
i\xi\widehat r_T(\xi)
=P_T(\xi)
:=\sum_{\beta\in\mathcal B_T^{\rm act}}
J_T(\beta)e^{-i\xi\beta}.}
\tag{C1zB2C7a.9}
\]

C7a bestimmt nun die Koeffizienten in (C1zB2C7a.9) konstruktiv.

---

# 2. Exakter Residual-Koeffizientenzensus

Die Sprungabbildung ist linear. Aus (C1zB2C7a.5) folgt deshalb für jedes `beta in R`

\[
\boxed{
J_T(\beta)
=J_{h,T}(\beta)
-\lambda_TJ_{1,T}(\beta)
-\lambda_TJ_{g,T}(\beta),
}
\tag{C1zB2C7a.10}
\]

wobei

\[
J_{h,T}(\beta):=J_{\widetilde h_T}(\beta),
\qquad
J_{g,T}(\beta):=J_{\widetilde g_T}(\beta).
\]

Für die Nullfortsetzung von

\[
\mathbf1_T=1_{(-T,T)}
\]

gilt exakt

\[
\boxed{
J_{1,T}(-T)=1,
\qquad
J_{1,T}(T)=-1,
\qquad
J_{1,T}(\beta)=0\quad(\beta\ne\pm T).
}
\tag{C1zB2C7a.11}
\]

Damit folgt die erste vollständige Fallunterscheidung.

## 2.1 Innere Punkte außerhalb der Reststütze

Für

\[
\beta\in(-T,T),
\qquad
J_{g,T}(\beta)=0,
\]

gilt

\[
\boxed{J_T(\beta)=J_{h,T}(\beta).}
\tag{C1zB2C7a.12}
\]

## 2.2 Innere Hub-Rest-Kollisionspunkte

Für

\[
\beta\in(-T,T),
\qquad
J_{g,T}(\beta)\ne0,
\]

gilt

\[
\boxed{
J_T(\beta)
=J_{h,T}(\beta)-\lambda_TJ_{g,T}(\beta).
}
\tag{C1zB2C7a.13}
\]

Genau hier kann eine **echte residuale Cancellation** stattfinden.

## 2.3 Randpunkte

Am linken Rand gilt

\[
\boxed{
J_T(-T)
=J_{h,T}(-T)
-\lambda_T
-\lambda_TJ_{g,T}(-T).
}
\tag{C1zB2C7a.14}
\]

Am rechten Rand

\[
\boxed{
J_T(T)
=J_{h,T}(T)
+\lambda_T
-\lambda_TJ_{g,T}(T).
}
\tag{C1zB2C7a.15}
\]

Diese beiden Randkoeffizienten dürfen in einem globalen Zensus nicht vergessen werden.

### C7a-Firewall 1 — Kandidat ist nicht tatsächlicher Breakpoint

Eine Lage `beta` gehört genau dann zur tatsächlichen Residual-Breakpointmenge, wenn

\[
\boxed{J_T(\beta)\ne0.}
\tag{C1zB2C7a.16}
\]

Die Vereinigung der Hub- und Rest-Kandidatenmengen liefert daher nur eine **Obermenge** von `B_T^act`.

Insbesondere darf aus einer arithmetisch isolierten Kandidatenlage allein nicht auf einen tatsächlichen Residualsprung geschlossen werden. Die aggregierten Koeffizienten in (C1zB2C7a.10) sind entscheidend.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,exact\text{-}residual\text{-}jump\text{-}census}.}
\]

---

# 3. Parität und Reduktion auf positive Breakpoints

Aus dem C6-Strang gilt:

- `h_T` ist reell und gerade;
- `g_T=R_T^*R_T1_T` ist reell und gerade;
- `1_T` ist reell und gerade.

Daher ist

\[
\boxed{r_T\text{ reell und gerade}.}
\tag{C1zB2C7a.17}
\]

Für die Nullfortsetzung einer geraden Stufenfunktion gilt

\[
\boxed{
J_T(-\beta)=-J_T(\beta).
}
\tag{C1zB2C7a.18}
\]

Somit kann das Exponentialpolynom paarweise geschrieben werden als

\[
\begin{aligned}
P_T(\xi)
&=\sum_{\beta>0}
\left[
J_T(\beta)e^{-i\xi\beta}
+J_T(-\beta)e^{i\xi\beta}
\right]\\
&=-2i\sum_{\beta>0}J_T(\beta)\sin(\xi\beta).
\end{aligned}
\]

Also

\[
\boxed{
P_T(\xi)
=-2i\sum_{\beta>0}J_T(\beta)\sin(\xi\beta).
}
\tag{C1zB2C7a.19}
\]

Insbesondere ist `P_T` rein imaginär und ungerade.

C6y liefert zusätzlich

\[
P_T(0)=0,
\qquad
P_T'(0)=0.
\]

Aus

\[
P_T'(0)
=-i\sum_\beta\beta J_T(\beta)
\]

folgt die zweite exakte Koeffizienten-Summenregel

\[
\boxed{
\sum_\beta \beta J_T(\beta)=0.
}
\tag{C1zB2C7a.20}
\]

Zusammen mit der Antisymmetrie folgt auch

\[
\sum_\beta J_T(\beta)=0.
\]

Diese Relationen sind für jede spätere Observability-Schätzung verbindlich: Beiträge einzelner geschützter Sprünge müssen global durch andere Koeffizienten so ergänzt werden, dass (C1zB2C7a.20) erhalten bleibt.

---

# 4. Exakter Hub-Koeffizientenkernel

C6g schreibt

\[
\boxed{
H_T
=\sum_{n\in\mathcal N_T}a_nK_{\log n},
\qquad
\mathcal N_T=\{p^k:p^k\le e^{2T}\},
}
\tag{C1zB2C7a.21}
\]

mit

\[
\boxed{
a_{p^k}=\sqrt{\log p}\,p^{-3k/4}.}
\tag{C1zB2C7a.22}
\]

Ferner

\[
K_s=P_TD_sE_T,
\qquad
D_sf(u)=f(u+s/2)-f(u-s/2),
\]

und

\[
K_s^*=-K_s.
\]

Daher

\[
\boxed{
h_T
=\sum_{n,m\in\mathcal N_T}
a_na_m
K_{\log n}^*K_{\log m}\mathbf1_T.}
\tag{C1zB2C7a.23}
\]

Für `a,b>0` setze

\[
\boxed{
G_{a,b,T}
:=K_a^*K_b\mathbf1_T.}
\tag{C1zB2C7a.24}
\]

und definiere den **globalen tatsächlichen Integer-Kernel**

\[
\boxed{
\kappa_{a,b,T}(\beta)
:=J_{\widetilde G_{a,b,T}}(\beta).
}
\tag{C1zB2C7a.25}
\]

Da `K_b1_T` nur die Werte `-1,0,1` annimmt und `K_a^*` eine Differenz zweier Translationen mit Fensterkompression ist,

\[
\boxed{
\kappa_{a,b,T}(\beta)\in\mathbb Z
}
\tag{C1zB2C7a.26}
\]

und für festes `a,b,T` ist nur eine endliche Zahl dieser Koeffizienten ungleich null.

Die Hubkoeffizienten sind daher exakt

\[
\boxed{
J_{h,T}(\beta)
=\sum_{n,m\in\mathcal N_T}
a_na_m
\kappa_{\log n,\log m,T}(\beta).
}
\tag{C1zB2C7a.27}
\]

Dies ist bereits ein vollständiger endlicher Hub-Zensus: Koinzidierende Shift-Paare werden an derselben `beta` **vor** dem Nichtverschwindungstest addiert.

## 4.1 Explizite innere Kernel-Formel

Setze

\[
g_{b,T}(u):=K_b\mathbf1_T(u).
\]

Dann

\[
\boxed{
g_{b,T}
=1_{(-T,-T+b/2)}-1_{(T-b/2,T)}.}
\tag{C1zB2C7a.28}
\]

Seine vier Randpunkte sind

\[
E_{b,T}
=\{-T,-T+b/2,T-b/2,T\}.
\]

Mit unserer Rechts-minus-links-Konvention lauten die zugehörigen Sprungvorzeichen

\[
\sigma_{b,T}(-T)=+1,
\qquad
\sigma_{b,T}(-T+b/2)=-1,
\]

\[
\sigma_{b,T}(T-b/2)=-1,
\qquad
\sigma_{b,T}(T)=+1.
\]

Im Inneren `beta in (-T,T)` erzeugt

\[
G_{a,b,T}(u)
=-g_{b,T}(u+a/2)+g_{b,T}(u-a/2)
\]

die exakte Formel

\[
\boxed{
\kappa_{a,b,T}(\beta)
=
\sum_{e\in E_{b,T}}
\sigma_{b,T}(e)
\left[
1_{\{\beta=e+a/2\}}
-
1_{\{\beta=e-a/2\}}
\right].
}
\tag{C1zB2C7a.29}
\]

Mehrfachtreffer werden algebraisch summiert.

### C7a-Firewall 2 — Randkompression separat

Formel (C1zB2C7a.29) wird nur für innere Punkte verwendet. An `beta=+-T` kann die äußere Fensterkompression selbst einen Sprung erzeugen. Genau deshalb wurde der globale Kernel in (C1zB2C7a.25) über den **tatsächlichen** Nullfortsetzungs-Sprung definiert.

Es wird keine unzulässige Innenformel auf die Randpunkte übertragen.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,exact\text{-}hub\text{-}integer\text{-}kernel}.}
\]

---

# 5. Exakte p-Tiefenkoeffizienten des Restterms

C6h zerlegt

\[
R_T
=\bigoplus_pR_{p,T},
\]

so dass wegen der orthogonalen Prime-Sektoren

\[
\boxed{
g_T
=R_T^*R_T\mathbf1_T
=\sum_p g_{p,T},
\qquad
g_{p,T}:=R_{p,T}^*R_{p,T}\mathbf1_T.}
\tag{C1zB2C7a.30}
\]

Es gibt auf der Restseite keine Cross-Prime-Gramterme.

Für festes `p` gilt

\[
R_{p,T}f(u)
=\sum_{k\ge1}b_{p,k}
K_{k\log p}f(u)\,q_{p,k,T}(u),
\]

mit

\[
\boxed{b_{p,k}=\sqrt{\log p}\,p^{-k/4},}
\tag{C1zB2C7a.31}
\]

und

\[
\boxed{
q_{p,k,T}(u)
=\sqrt{p-1}
\sum_{a=0}^{\min(k-1,J_{p,T}(u)-1)}
p^{(a-k)/2}\psi_{p,a}.}
\tag{C1zB2C7a.32}
\]

## 5.1 Rechte Tiefenlayer

Für `j>=0` setze wie in C6h

\[
\boxed{
I^+_{p,j,T}
=
\left(
T-\frac{j+1}{2}\log p,
T-\frac j2\log p
\right).
}
\tag{C1zB2C7a.33}
\]

Auf diesem Intervall ist

\[
J_{p,T}(u)=j.
\]

Für `j=0` gilt

\[
R_{p,T}\mathbf1_T=0.
\]

Für `j>=1` definiere den endlichen geometrischen Tail

\[
\boxed{
S_{p,j,T}
:=\sum_{\ell=j+1}^{K_p(T)}p^{-3\ell/4},
}
\tag{C1zB2C7a.34}
\]

wobei `K_p(T)` der bereits in C6h verwendete endliche aktive Trunkationsindex ist.

Dann gilt auf `I^+_{p,j,T}` exakt

\[
\boxed{
R_{p,T}\mathbf1_T(u)
=-\sqrt{(p-1)\log p}\,S_{p,j,T}
\sum_{a=0}^{j-1}p^{a/2}\psi_{p,a}.}
\tag{C1zB2C7a.35}
\]

## 5.2 Der skalare Rücktransportkoeffizient

Setze

\[
\boxed{
F_{p,k,T}(u)
:=\left\langle
q_{p,k,T}(u),
R_{p,T}\mathbf1_T(u)
\right\rangle.}
\tag{C1zB2C7a.36}
\]

Auf dem rechten Layer `I^+_{p,j,T}` mit `j>=1` ist `F_{p,k,T}` konstant.

Mit

\[
m=\min(k-1,j-1)
\]

liefert die Orthonormalität der `psi_{p,a}`

\[
\begin{aligned}
F_{p,k,T}^{+}(j)
&=-(p-1)\sqrt{\log p}\,S_{p,j,T}
\sum_{a=0}^{m}p^{(a-k)/2}p^{a/2}\\
&=-(p-1)\sqrt{\log p}\,S_{p,j,T}
 p^{-k/2}\sum_{a=0}^{m}p^a\\
&=-\sqrt{\log p}\,S_{p,j,T}
 p^{-k/2}\left(p^{m+1}-1\right).
\end{aligned}
\]

Da

\[
m+1=\min(k,j),
\]

folgt die exakte geschlossene Formel

\[
\boxed{
F_{p,k,T}^{+}(j)
=-\sqrt{\log p}\,S_{p,j,T}
 p^{-k/2}
\left(p^{\min(k,j)}-1\right),
\qquad j\ge1.
}
\tag{C1zB2C7a.37}
\]

Für `j=0` gilt

\[
\boxed{F_{p,k,T}^{+}(0)=0.}
\tag{C1zB2C7a.38}
\]

Dies ist stärker als eine bloße Sprungmajorante: Die tatsächlichen Layerwerte sind explizit.

Da `q_{p,k,T}` nur von `|u|` abhängt und `R_{p,T}1_T` ungerade ist, ist

\[
\boxed{F_{p,k,T}\text{ ungerade}.}
\tag{C1zB2C7a.39}
\]

Die linken Layerwerte sind daher durch Spiegelung exakt festgelegt.

## 5.3 Exakte Tiefensprünge von F

An der rechten inneren Tiefenmarke

\[
\gamma^+_{p,j,T}
:=T-\frac j2\log p,
\qquad j\ge1,
\]

liegt links der Layer `j` und rechts der Layer `j-1`. Daher

\[
\boxed{
J_{F_{p,k,T}}(\gamma^+_{p,j,T})
=F^+_{p,k,T}(j-1)-F^+_{p,k,T}(j).
}
\tag{C1zB2C7a.40}
\]

Die linken Koeffizienten folgen aus der Ungeradheit.

Damit sind auch die inneren tatsächlichen Sprünge der skalaren Rücktransportfelder explizit aus (C1zB2C7a.37) berechenbar.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,exact\text{-}rest\text{-}layer\text{-}coefficients}.}
\]

---

# 6. Exakter Rücktransport zu den Rest-Sprungkoeffizienten

C6h liefert

\[
\boxed{
g_{p,T}
=\sum_{k\ge1}b_{p,k}
K_{k\log p}^*F_{p,k,T}.}
\tag{C1zB2C7a.41}
\]

Für eine nullfortgesetzte skalare Stufenfunktion `F` definiere global

\[
\boxed{
\tau_{s,T}[F](\beta)
:=J_{\widetilde{K_s^*F}}(\beta).
}
\tag{C1zB2C7a.42}
\]

Dann gilt ohne jede Kandidatenapproximation

\[
\boxed{
J_{g_p,T}(\beta)
=\sum_{k\ge1}b_{p,k}
\tau_{k\log p,T}[F_{p,k,T}](\beta).
}
\tag{C1zB2C7a.43}
\]

und insgesamt

\[
\boxed{
J_{g,T}(\beta)
=\sum_pJ_{g_p,T}(\beta).}
\tag{C1zB2C7a.44}
\]

Die Summen sind bei festem `T` endlich auf aktiven Indizes.

## 6.1 Innere Transportformel

Für `beta in (-T,T)` und eine Sprungstelle `gamma` von `F` gilt wegen

\[
K_s^*F
=-F(\cdot+s/2)+F(\cdot-s/2)
\]

die innere Transportregel

\[
\boxed{
\tau_{s,T}[F](\beta)
=
\sum_{\gamma}J_F(\gamma)
\left[
1_{\{\beta=\gamma+s/2\}}
-
1_{\{\beta=\gamma-s/2\}}
\right].
}
\tag{C1zB2C7a.45}
\]

Für `s=k log p` und die p-Tiefenmarken

\[
\gamma=\pm T+\frac j2\log p
\]

bleibt deshalb jede transportierte innere Restlage in der prime-puren Familie

\[
\boxed{
\pm T+\frac m2\log p.
}
\tag{C1zB2C7a.46}
\]

Dies reproduziert C6hs prime-pure Supportklassifikation, jetzt aber auf **Koeffizientenebene**.

### C7a-Firewall 3 — Prime-pure Support ist kein Koeffizientensatz

Formel (C1zB2C7a.46) sagt nur, wo ein Restkoeffizient liegen kann.

Ob er tatsächlich ungleich null ist, entscheidet erst die aggregierte Summe

\[
\sum_k b_{p,k}\tau_{k\log p,T}[F_{p,k,T}](\beta),
\]

und bei einer Kollision verschiedener Prime-Blöcke anschließend zusätzlich die Summe über `p` in (C1zB2C7a.44).

Genau diese Aggregation ist Teil des ActualJumpCoefficientCensus.

---

# 7. Die vollständige konstruktive C7a-Formel

Setzt man die Hubformel (C1zB2C7a.27) und die Restformel (C1zB2C7a.44) in den Residualzensus (C1zB2C7a.10) ein, erhält man für jedes `beta`:

\[
\boxed{
\begin{aligned}
J_T(\beta)
={}&
\sum_{n,m\in\mathcal N_T}
a_na_m
\kappa_{\log n,\log m,T}(\beta)\\
&-\lambda_TJ_{1,T}(\beta)\\
&-\lambda_T
\sum_p\sum_{k\ge1}
b_{p,k}
\tau_{k\log p,T}[F_{p,k,T}](\beta),
\end{aligned}
}
\tag{C1zB2C7a.47}
\]

wobei die skalaren Layerwerte von `F_{p,k,T}` durch (C1zB2C7a.37) exakt gegeben sind.

Alle Größen auf der rechten Seite sind für festes `T` endliche, explizite Daten des bereits definierten Operatorsystems.

Damit ist die tatsächliche Breakpointmenge konstruktiv

\[
\boxed{
\mathcal B_T^{\rm act}
=
\{\beta:J_T(\beta)\ne0\},
}
\tag{C1zB2C7a.48}
\]

und nicht mehr bloß eine Kandidatenvereinigung.

### Was „Zensus“ hier mathematisch bedeutet

C7a behauptet nicht, eine geschlossene Einzeilenformel für jede einzelne Kollision aller Prime-Power-Paare gefunden zu haben.

Der Zensus ist vielmehr **algorithmisch-exakt**:

1. endliche aktive Labelmengen bestimmen;
2. Hub-Integerkernel `kappa` auswerten;
3. p-Tiefenlayer und die expliziten Werte (C1zB2C7a.37) auswerten;
4. Rücktransportkernel `tau` auswerten;
5. alle Beiträge an identischem `beta` addieren;
6. den Residualkoeffizienten (C1zB2C7a.47) bilden;
7. erst dann `J_T(beta) != 0` testen.

Damit sind **alle Cancellations typisiert und an der richtigen Stelle der Rechnung lokalisiert**.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,actual\text{-}vs\text{-}candidate\text{-}breakpoint\text{-}test}.}
\]

---

# 8. Ein geschütztes lambda-freies tatsächliches Residualsprungpaar

C6i liefert für jedes hinreichend große `T` mindestens ein

\[
q_T\in\{3,5\}
\]

mit

\[
\boxed{
x_T
:=T-\frac12\log(q_T/2)}
\tag{C1zB2C7a.49}
\]

und einem positiven `A_T1_T`-freien Radius um `x_T`.

Da `x_T` strikt im Inneren `(-T,T)` liegt,

\[
J_{1,T}(x_T)=0.
\]

Da

\[
A_T\mathbf1_T
=\mathbf1_T+g_T
\]

in einer ganzen Umgebung von `x_T` keinen Breakpoint besitzt, folgt zugleich

\[
\boxed{J_{g,T}(x_T)=0.}
\tag{C1zB2C7a.50}
\]

Damit kollabiert die vollständige Residualformel an dieser Stelle exakt zu

\[
\boxed{
J_T(x_T)=J_{h,T}(x_T).
}
\tag{C1zB2C7a.51}
\]

C6e/C6g/C6i liefern für den tatsächlichen Hubsprung eventual eine T-unabhängige positive Untergrenze

\[
\boxed{
|J_T(x_T)|
=|J_{h,T}(x_T)|
\ge j_*>0.
}
\tag{C1zB2C7a.52}
\]

Wegen der Geradheit von `r_T`

\[
\boxed{
J_T(-x_T)=-J_T(x_T),
\qquad
|J_T(-x_T)|\ge j_*.
}
\tag{C1zB2C7a.53}
\]

Dies ist der erste vollständig geschützte Koeffizientenbefund des C7-Strangs:

\[
\boxed{
\text{Das Paar }\pm x_T\text{ überlebt alle Hub-Rest- und Identitätscancellations.}
}
\tag{C1zB2C7a.54}
\]

### C7a-Firewall 4 — keine falsche primitive Exaktheit

Es wird **nicht** behauptet, dass

\[
J_{h,T}(x_T)
\]

genau nur aus dem primitiven Labelpaar `(2,q_T)` besteht.

Andere Hubpaare können bei speziellen Horizonten dieselbe Kandidatenlage treffen. Die korrekte Größe ist die vollständig aggregierte Hubsumme (C1zB2C7a.27).

C6e/C6g garantieren deren tatsächliches Nichtverschwinden; C7a ersetzt diesen bewiesenen aggregierten Satz nicht durch eine zu starke primitive Ein-Paar-Formel.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,protected\text{-}lambda\text{-}free\text{-}residual\text{-}jump\text{-}pair}.}
\]

---

# 9. Beitrag des geschützten Paars zum Sprungpolynom

Schreibe

\[
J_T^*:=J_T(x_T).
\]

Der Beitrag der beiden geschützten Koeffizienten zu `P_T` ist exakt

\[
\begin{aligned}
P_T^{\rm prot}(\xi)
&=J_T^*e^{-i\xi x_T}
-J_T^*e^{i\xi x_T}\\
&=-2iJ_T^*\sin(\xi x_T).
\end{aligned}
\]

Also

\[
\boxed{
P_T^{\rm prot}(\xi)
=-2iJ_T^*\sin(\xi x_T).
}
\tag{C1zB2C7a.55}
\]

Setze

\[
\boxed{
P_T(\xi)
=P_T^{\rm prot}(\xi)+P_T^{\rm rem}(\xi).
}
\tag{C1zB2C7a.56}
\]

Das geschützte Paar hat feste Koeffizientenstärke, aber es erzeugt **keine** punktweise Untergrenze für die volle Summe.

Erstens besitzt bereits der geschützte Teil die exakten Nullstellen

\[
\boxed{
\xi=\frac{k\pi}{x_T},
\qquad k\in\mathbb Z.
}
\tag{C1zB2C7a.57}
\]

Zweitens kann `P_T^rem` den geschützten Beitrag an einzelnen Frequenzen partiell oder vollständig kompensieren.

Drittens erzwingt die globale Momentrelation

\[
P_T'(0)=0
\]

gerade eine nichttriviale Koeffizientenkompensation zwischen dem geschützten Paar und dem Rest.

Damit gilt ausdrücklich

\[
\boxed{
\text{ein geschütztes tatsächliches Sprungpaar}
\not\Rightarrow
\text{punktweise R3-Observability}.
}
\tag{C1zB2C7a.58}
\]

---

# 10. Korrektur des punktweisen R3-Zieltyps

Ein naheliegender Zieltyp wäre

\[
|P_T(\xi)|
\ge c|\xi|\,\|r_T\|_2.
\tag{C1zB2C7a.59}
\]

Als **globale** Aussage kann dies jedoch nicht stimmen.

## 10.1 No-Go nahe null

C6y liefert

\[
P_T(0)=P_T'(0)=0.
\]

Da `P_T` ein endliches Exponentialpolynom ist, ist es analytisch und somit

\[
P_T(\xi)=O_T(\xi^2)
\qquad(\xi\to0).
\]

Daher

\[
\frac{|P_T(\xi)|}{|\xi|\|r_T\|_2}
\longrightarrow0
\qquad(\xi\to0)
\]

für jedes feste nichtverschwindende `r_T`.

Also existiert kein `c>0`, das (C1zB2C7a.59) in einer ganzen punktierten Nullumgebung erfüllt.

## 10.2 No-Go bei unbeschränkter Frequenz

Da

\[
P_T(\xi)=\sum_\beta J_T(\beta)e^{-i\xi\beta},
\]

gilt

\[
\boxed{|P_T(\xi)|\le V_T:=\sum_\beta|J_T(\beta)|}
\tag{C1zB2C7a.60}
\]

für alle reellen `xi`.

Die rechte Seite von (C1zB2C7a.59) wächst dagegen linear in `|xi|`.

Auch deshalb kann eine solche globale Untergrenze nicht gelten.

### Konsequenz

R3 sollte nicht als globale punktweise Untergrenze formuliert werden.

Der natürliche Zieltyp ist vielmehr eine **integrierte Observability** auf einem relevanten Frequenzband oder eine quantitative Aussage, dass ein fester Anteil der Fouriermasse nicht gleichzeitig in den Prime-Quasi-Nullregionen liegen kann.

Status:

\[
\boxed{\checkmark[M]_{\rm neg,global\text{-}pointwise\text{-}P\text{-}lower\text{-}bound}.}
\]

---

# 11. Exakte integrierte Koeffizientenenergie

Hier liefert der ActualJumpCoefficientCensus sofort einen positiven Satz.

Fixiere `T` und schreibe die **distinct actual breakpoints** als

\[
\mathcal B_T^{\rm act}
=\{\beta_1,\ldots,\beta_{N_T}\},
\]

mit

\[
J_j:=J_T(\beta_j)\ne0.
\]

Dann

\[
P_T(\xi)=\sum_{j=1}^{N_T}J_je^{-i\xi\beta_j}.
\]

Für `X>0` gilt exakt

\[
\begin{aligned}
\int_{-X}^{X}|P_T(\xi)|^2d\xi
&=\sum_{j,k}J_j\overline{J_k}
\int_{-X}^{X}e^{-i\xi(\beta_j-\beta_k)}d\xi\\
&=2X\sum_j|J_j|^2\\
&\quad+
2\sum_{j\ne k}
J_j\overline{J_k}
\frac{\sin(X(\beta_j-\beta_k))}
{\beta_j-\beta_k}.
\end{aligned}
\]

Somit

\[
\boxed{
\frac1{2X}
\int_{-X}^{X}|P_T(\xi)|^2d\xi
=
\sum_j|J_j|^2
+
\frac1X
\sum_{j\ne k}
J_j\overline{J_k}
\frac{\sin(X(\beta_j-\beta_k))}
{\beta_j-\beta_k}.
}
\tag{C1zB2C7a.61}
\]

Für festes `T` ist die Summe endlich und alle `beta_j-beta_k` mit `j!=k` sind ungleich null. Daher verschwindet jeder Offdiagonalterm nach Division durch `X` im Grenzwert.

Folglich:

\[
\boxed{
\lim_{X\to\infty}
\frac1{2X}
\int_{-X}^{X}|P_T(\xi)|^2d\xi
=
\sum_{\beta\in\mathcal B_T^{\rm act}}
|J_T(\beta)|^2.
}
\tag{C1zB2C7a.62}
\]

Dies ist eine exakte Parseval-artige Mittelwertidentität für das endliche Sprung-Exponentialpolynom.

## 11.1 Quantitative positive Diagonale aus dem geschützten Paar

C7a.52–C7a.53 liefern zwei verschiedene tatsächliche Breakpoints `+-x_T` mit Betrag mindestens `j_*`.

Daher

\[
\boxed{
\sum_{\beta\in\mathcal B_T^{\rm act}}
|J_T(\beta)|^2
\ge
2j_*^2.
}
\tag{C1zB2C7a.63}
\]

Zusammen mit (C1zB2C7a.62):

\[
\boxed{
\liminf_{X\to\infty}
\frac1{2X}
\int_{-X}^{X}|P_T(\xi)|^2d\xi
\ge2j_*^2.
}
\tag{C1zB2C7a.64}
\]

für jedes hinreichend große **feste** `T`.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,fixed\text{-}T\text{-}integrated\text{-}R3\text{-}mean}.}
\]

---

# 12. Warum dies R3 noch nicht schließt

Die Identität (C1zB2C7a.61) zeigt exakt, was für eine in `T` quantitative Version fehlt.

Definiere den Offdiagonal-Kostenparameter

\[
\boxed{
\mathfrak G_T
:=
\sum_{\substack{\beta,\gamma\in\mathcal B_T^{\rm act}\\\beta\ne\gamma}}
\frac{|J_T(\beta)J_T(\gamma)|}
{|\beta-\gamma|}.
}
\tag{C1zB2C7a.65}
\]

Dann folgt aus (C1zB2C7a.61) sofort

\[
\boxed{
\frac1{2X}
\int_{-X}^{X}|P_T(\xi)|^2d\xi
\ge
\sum_\beta|J_T(\beta)|^2
-\frac{\mathfrak G_T}{X}.
}
\tag{C1zB2C7a.66}
\]

Mit dem geschützten Paar insbesondere

\[
\boxed{
\frac1{2X}
\int_{-X}^{X}|P_T(\xi)|^2d\xi
\ge
2j_*^2
-\frac{\mathfrak G_T}{X}.
}
\tag{C1zB2C7a.67}
\]

Damit wäre eine quantitative integrierte R3-Aussage sofort verfügbar, wenn man auf einer relevanten Skala `X=X_T` zeigen könnte

\[
\boxed{
\mathfrak G_T\le cX_T
}
\tag{C1zB2C7a.68}
\]

mit `c<2j_*^2` beziehungsweise einer entsprechend skalierten Diagonalabschätzung.

Aber genau diese Kontrolle ist noch nicht vorhanden.

C6i isoliert `x_T` von den Rest-Breakpoints von `A_T1_T`; es liefert **keine globale Mindestseparation aller tatsächlichen Residualsprünge**.

C6g kontrolliert gewichtete Hub-Crowding-Masse lokal, nicht den gesamten Offdiagonalparameter (C1zB2C7a.65).

C6y/C6z kontrollieren die absolute Variation `V_T` grob, aber `V_T` allein kontrolliert wegen der Nenner `|beta-gamma|^{-1}` nicht `G_T`.

Daher gilt:

\[
\boxed{
\text{fixed-T positive mean}
\not\Rightarrow
\text{uniforme integrierte R3-Observability auf }X_T.
}
\tag{C1zB2C7a.69}
\]

Dies ist der nun präzise C7b-Eingang.

---

# 13. Beziehung zu C6ys Fourierdarstellung

C6y liefert

\[
i\xi\widehat r_T(\xi)=P_T(\xi).
\]

Also für `xi!=0`

\[
\boxed{
|\widehat r_T(\xi)|^2
=\frac{|P_T(\xi)|^2}{\xi^2}.}
\tag{C1zB2C7a.70}
\]

Die integrierte Koeffizientenenergie von `P_T` ist damit unmittelbar relevant für die Fouriermasse des Residualvektors.

Aber aus einer ungewichteten Untergrenze für

\[
\int |P_T|^2
\]

folgt wegen des Faktors `xi^{-2}` nicht automatisch die benötigte relative Untergrenze für

\[
\int |\widehat r_T|^2.
\]

Noch weniger folgt daraus unmittelbar eine Untergrenze für die komprimierte Martingalenergie

\[
\|R_Tr_T\|^2.
\]

Der in C6z exportierte **window lower transfer** bleibt daher ausdrücklich offen.

### C7a-Firewall 5

\[
\boxed{
\text{integrierte }P_T\text{-Observability}
\not\Rightarrow
q_{r,T}\not\to0
}
\tag{C1zB2C7a.71}
\]

ohne quantitative Frequenzlokalisierung und unteren Kanaltransfer.

---

# 14. Linearformen-in-Logarithmen-Firewall

Die Breakpointlagen im C6/C7-System enthalten arithmetische Kombinationen von

\[
\log p,
\quad
\log q,
\quad
\log n,
\]

sowie terminale Terme `+-T`.

Quantitative Sätze über **nichtverschwindende lineare Formen in Logarithmen algebraischer Zahlen** sind deshalb prinzipiell als Werkzeug für bestimmte Abstandsaussagen zwischen log-arithmetischen Lagen denkbar.

C7a verwendet jedoch keinen solchen Satz.

Der Grund ist strukturell:

## 14.1 Lagekontrolle ist nicht Koeffizientenobservability

Selbst eine Untergrenze

\[
|\beta-\gamma|\ge\delta_T
\]

für ausgewählte verschiedene Breakpointlagen liefert noch keine punktweise Untergrenze für

\[
P_T(\xi)=\sum_\beta J_T(\beta)e^{-i\xi\beta},
\]

weil die Koeffizienten `J_T(beta)` selbst cancellieren können.

## 14.2 Freies T muss eliminiert sein

Eine Differenz zweier Breakpointlagen, in der ein Term `+-2T` verbleibt, ist für beliebiges reelles `T` nicht automatisch eine lineare Form in Logarithmen algebraischer Zahlen.

Ein logarithmischer Abstandssatz darf daher nur auf Teilprobleme angewandt werden, in denen die terminalen `T`-Beiträge **exakt herausfallen** oder anderweitig arithmetisiert sind.

## 14.3 C7a-Ziel ist zuerst Koeffizientenzensus

Vor jeder Diophantischen Abstandstheorie muss geklärt sein, welche Kandidatenlagen nach allen Huber-, Rest- und Identitätscancellations überhaupt tatsächliche Koeffizienten tragen.

Genau dies leistet (C1zB2C7a.47)–(C1zB2C7a.48).

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,log\text{-}form\text{-}location\not\Rightarrow coefficient\text{-}observability}.
}
\]

---

# 15. Reconciliation mit dem C6-Abschluss

C6z exportierte drei qualitativ neue Aufgaben:

\[
R1:\ \Gamma_T\text{-Kontrolle},
\]

\[
R2:\ \text{quantitative Quasi-Null-Nichtapproximation},
\]

\[
R3:\ \text{direkte Koeffizientenobservability von }P_T.
\]

C6z schloss R1 schwach durch

\[
\Gamma_T\le CT^{5/2}e^{9T/2}.
\]

C7a greift R3 an und erreicht:

1. exakte tatsächliche Koeffizientenformel;
2. exakte Hub- und Rest-Unterformeln;
3. geschütztes `lambda`-freies Sprungpaar;
4. fixed-T positive integrierte Mittelwertobservability;
5. exakte Typisierung des noch fehlenden Offdiagonal-/Bandproblems.

Damit ist R3 **nicht gelöst**, aber von einer vagen Frage über Breakpointprovenienz auf die konkrete Größe

\[
\boxed{
\mathfrak G_T
=\sum_{\beta\ne\gamma}
\frac{|J_T(\beta)J_T(\gamma)|}{|\beta-\gamma|}
}
\tag{C1zB2C7a.72}
\]

beziehungsweise auf mögliche feinere, lokal gewichtete Varianten reduziert.

---

# 16. Was C7a ausdrücklich nicht beweist

C7a beweist **nicht**:

\[
q_{r,T}\not\to0.
\]

C7a beweist ebenso wenig

\[
q_{r,T}\to0.
\]

C7a beweist nicht

\[
a_{R,T}^{(2)}\ne0.
\]

C7a beweist keine uniforme punktweise Untergrenze für `P_T`.

C7a beweist keine globale Mindestseparation aller tatsächlichen Breakpoints.

C7a beweist keinen Baker-/Baker-Wuestholz-basierten Abstandssatz.

C7a überträgt die integrierte Exponentialpolynomenergie noch nicht nach unten auf die komprimierte Martingalenergie.

Insbesondere bleibt

\[
\boxed{P11=\texttt{PASS-A ACTIVE}.}
\tag{C1zB2C7a.73}
\]

Kein SYN, kein Seal, kein `papers/P11`.

---

# 17. Nächster atomarer Knoten

Nach C7a ist ein weiterer allgemeiner Koeffizientenzensus nicht nötig.

Der nächste Knoten sollte die neue integrierte Form direkt testen:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C7b]
}
\]

mit Arbeitstitel

`ProtectedJumpPair_OffDiagonalGram_IntegratedObservabilityTest`.

Der Arbeitsauftrag ist bewusst eng:

1. den Offdiagonalparameter `G_T` aus (C1zB2C7a.65) nicht global blind, sondern relativ zum geschützten Paar `+-x_T` zerlegen;
2. prüfen, ob C6gs gewichtete lokale Hub-Crowding-Schranke und C6hs Rest-Crowding genügen, um die paarbezogenen Gramterme auf einer expliziten Frequenzskala zu kontrollieren;
3. falls ein zweites geschütztes tatsächliches Sprungpaar benötigt wird, dieses explizit konstruieren oder einen No-Go protokollieren;
4. pointwise Observability nicht erneut als Standardziel verwenden;
5. logarithmische Abstandssätze nur dort einsetzen, wo die `T`-Terme exakt eliminiert sind;
6. R3 und den späteren window-lower-transfer weiterhin getrennt halten.

C7 soll damit endlich bleiben: C7a ist der Koeffizientenzensus; C7b ist der integrierte Observability-Test. Erst wenn dieser Test positiv ist, ist ein eigener kurzer Window-Transfer-Knoten gerechtfertigt.

---

# 18. Abschlussurteil C7a

Der C7a-Zensus ist positiv abgeschlossen:

\[
\boxed{
\text{actual residual jump coefficients are now explicitly and constructively typed.}
}
\]

Der wichtigste neue mathematische Inhalt ist die Kombination

\[
\boxed{
|J_T(\pm x_T)|\ge j_*>0
}
\]

mit der exakten Mittelwertidentität

\[
\boxed{
\lim_{X\to\infty}
\frac1{2X}\int_{-X}^{X}|P_T(\xi)|^2d\xi
=
\sum_\beta|J_T(\beta)|^2
\ge2j_*^2.
}
\]

Damit besitzt R3 bei jedem festen großen Horizont eine reale koeffizientengetriebene positive Diagonale.

Der verbleibende zentrale Schritt ist nun nicht mehr

\[
\text{„gibt es überhaupt tatsächliche residuale Sprünge?“},
\]

sondern

\[
\boxed{
\text{„kann die positive Diagonale gegen die Offdiagonalinterferenz
auf einer }T\text{-relevanten Frequenzskala stabilisiert werden?“}
}
\]

Genau diese Frage wird an C7b übergeben.
