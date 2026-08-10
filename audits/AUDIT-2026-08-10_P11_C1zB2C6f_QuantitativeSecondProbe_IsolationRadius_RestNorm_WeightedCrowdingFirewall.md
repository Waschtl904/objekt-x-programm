# P11-C1z-B2-C6f — Quantitative Zweitprobe: Isolationsradius, Restnorm und gewichtete Crowding-Firewall

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6f]`  
**Direkte Voraussetzungen:** C1z-B, C1z-B2-C3, C1z-B2-C4, C1z-B2-C6d, C1z-B2-C6e  
**Strukturelle Schnittstellen:** C1z-B2-C6a, C1z-B2-C6b, C1z-B2-C6c  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d Jet-Alignment-Firewall  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6f]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm pos,rest\text{-}operator\text{-}bound}
+
\checkmark[M]_{\rm pos,quantitative\text{-}reduction\text{-}to\text{-}isolation\text{-}radius}
+
\checkmark[M]_{\rm neg,breakpoint\text{-}support\text{-}alone\not\Rightarrow uniform\text{-}scale}
+
?[O]_{\rm asymptotic\text{-}\Delta\text{-}classification}
+
?[O]_{\rm weighted\text{-}local\text{-}crowding}
+
?[O]_{\rm second\text{-}probe\text{-}jet\text{-}alignment}
}
\]

C6f beantwortet die in C6e offen gelassene Skalenfrage **teilweise, aber nicht vollständig**.

Der positive neue Satz lautet:

\[
\boxed{
\Delta_T^{(1)}
\ge
c_*
\frac{\rho_T}{1+C_*Te^T}
\qquad(T\gg1),
}
\tag{C1zB2C6f.1}
\]

wobei `\rho_T>0` der konkrete Isolationsradius der in C6e gewählten Cross-Prime-Sprungkante ist.

Damit ist die quantitative Zweitprobe nicht mehr von zwei unspezifizierten Größen `\varepsilon_T` und `\langle v_T,A_Tv_T\rangle` abhängig. Die gesamte noch fehlende Information wird auf eine einzige geometrische Größe reduziert:

\[
\boxed{\rho_T.}
\tag{C1zB2C6f.2}
\]

Die negative Hälfte von C6f ist ebenso wichtig:

\[
\boxed{
\text{Die reine Breakpoint-Supportgeometrie aus C6e liefert keine uniforme positive Untergrenze für }\rho_T.
}
\tag{C1zB2C6f.3}
\]

Insbesondere folgt aus C6e+C6f **weder**

\[
\Delta_T^{(1)}\to0,
\]

**noch**

\[
\inf_{T\gg1}\Delta_T^{(1)}>0,
\]

**noch** eine Wachstumsordnung.

Die Frage „wächst, bleibt beschränkt oder degeneriert `\Delta_T^{(1)}`?“ bleibt offen. C6f zeigt jedoch exakt, **welche zusätzliche Mathematik sie entscheiden muss**: nicht bloße Punktseparation, sondern eine gewichtete Kontrolle der lokalen Sprungmasse um die Cross-Prime-Kante.

---

# 0. Voraussetzungsverkettung und Supersession-Scope

C6f erbt nichts implizit.

## 0.1 Aus C1z-B

Auf dem Terminalfenster

\[
\mathscr H_T=L^2(-T,T)
\]

steht der konditionierte Restoperator in der Form

\[
R_Tf(u)
=
\sum_p\sum_{k\ge1}
 b_{p,k}
 D_{k\log p}E_Tf(u)
\otimes q_{p,k,T}(u),
\tag{C1zB2C6f.4}
\]

mit

\[
\boxed{
b_{p,k}=\sqrt{\log p}\,p^{-k/4}}
\tag{C1zB2C6f.5}
\]

und

\[
q_{p,k,T}(u)
=
\mathsf Q_T(u)\eta_{p,k}.
\tag{C1zB2C6f.6}
\]

Die finite-adischen Restsektoren verschiedener Primzahlen sind orthogonal:

\[
K_p^0\perp K_q^0
\qquad(p\ne q).
\tag{C1zB2C6f.7}
\]

Außerdem ist `\mathsf Q_T(u)` eine orthogonale Conditional Expectation, also eine Kontraktion.

Für die Restvektoren gilt aus der Martingaldarstellung

\[
\eta_{p,k}
=\sqrt{p-1}
\sum_{j=0}^{k-1}p^{(j-k)/2}\psi_{p,j},
\]

wobei die `\psi_{p,j}` orthonormal sind. Daher

\[
\begin{aligned}
\|\eta_{p,k}\|^2
&=(p-1)\sum_{j=0}^{k-1}p^{j-k}\\
&=(p-1)p^{-k}\frac{p^k-1}{p-1}\\
&=1-p^{-k}<1.
\end{aligned}
\tag{C1zB2C6f.8}
\]

Somit

\[
\boxed{
\|q_{p,k,T}(u)\|\le1.
}
\tag{C1zB2C6f.9}
\]

C1z-B beweist ferner für nichtverschwindende Restbeiträge auf dem Terminalfenster:

\[
p\le e^{2T},
\qquad
p^k\le e^{4T}.
\tag{C1zB2C6f.10}
\]

## 0.2 Aus C3

Setze

\[
\boxed{A_T=I+R_T^*R_T\ge I.}
\tag{C1zB2C6f.11}
\]

Damit

\[
\langle f,A_Tf\rangle
=\|f\|^2+\|R_Tf\|^2.
\tag{C1zB2C6f.12}
\]

## 0.3 Aus C6d/C6e

Mit

\[
h_T:=H_T^*H_T\mathbf1_T
\]

und

\[
\lambda_T
=
\frac{\|H_T\mathbf1_T\|^2}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}
\]

ist

\[
r_T=h_T-\lambda_TA_T\mathbf1_T
\]

und

\[
\boxed{
\Delta_T^{(1)}
=\langle r_T,A_T^{-1}r_T\rangle.
}
\tag{C1zB2C6f.13}
\]

Für jeden Separator `v` mit

\[
\langle v,A_T\mathbf1_T\rangle=0
\]

gilt die Variationsabschätzung

\[
\boxed{
\Delta_T^{(1)}
\ge
\frac{|\langle v,h_T\rangle|^2}
{\langle v,A_Tv\rangle}.
}
\tag{C1zB2C6f.14}
\]

C6e konstruiert eventual eine Cross-Prime-Kante

\[
x_T=x_{q_T}(T),
\qquad q_T\in\{3,5\},
\tag{C1zB2C6f.15}
\]

mit

\[
x_q(T)=T-\frac12\log(q/2)
\tag{C1zB2C6f.16}
\]

und

\[
\boxed{
|J_T|
:=
|\operatorname{Jump}_{x_T}h_T|
\ge
j_*
:=
\frac12\min\{a_2a_3,a_2a_5\}
>0
}
\tag{C1zB2C6f.17}
\]

für alle hinreichend großen `T`.

Zugleich ist

\[
x_T\notin\mathscr L_T^A,
\tag{C1zB2C6f.18}
\]

also `A_T\mathbf1_T` besitzt **genau an diesem Punkt** keinen Sprung.

C6e folgert daraus qualitativ

\[
\Delta_T^{(1)}>0
\qquad(T\gg1).
\tag{C1zB2C6f.19}
\]

C6f quantifiziert nun exakt, wie weit dieser Beweis reicht.

---

# 1. Kanonischer Isolationsradius der C6e-Kante

Seien

\[
\mathcal B_T^h
\]

und

\[
\mathcal B_T^A
\]

die endlichen Mengen der Sprungstellen der stückweise konstanten Repräsentanten von

\[
h_T
\qquad\text{bzw.}\qquad
A_T\mathbf1_T.
\]

C6e liefert

\[
x_T\in\mathcal B_T^h,
\qquad
x_T\notin\mathcal B_T^A.
\]

Definiere

\[
\boxed{
\rho_T
:=
\frac12
\operatorname{dist}
\left(
 x_T,
 (\mathcal B_T^h\cup\mathcal B_T^A)\setminus\{x_T\}
\right).
}
\tag{C1zB2C6f.20}
\]

Falls es außer `x_T` keine weitere Sprungstelle gäbe, setzen wir konventionsgemäß `\rho_T=T/4`; dieser Sonderfall spielt asymptotisch keine Rolle.

Da die Breakpoint-Mengen für jedes feste `T` endlich sind,

\[
\boxed{\rho_T>0}
\tag{C1zB2C6f.21}
\]

für jedes hinreichend große `T`.

Auf

\[
(x_T-\rho_T,x_T)
\quad\text{und}\quad
(x_T,x_T+\rho_T)
\]

liegen keine weiteren Sprungstellen von `h_T` oder `A_T\mathbf1_T`.

Daher kann C6es Separator kanonisch mit

\[
\boxed{
\varepsilon_T=\rho_T
}
\tag{C1zB2C6f.22}
\]

gewählt werden:

\[
\boxed{
v_T
=
1_{(x_T-\rho_T,x_T)}
-
1_{(x_T,x_T+\rho_T)}.
}
\tag{C1zB2C6f.23}
\]

Dann

\[
\|v_T\|^2=2\rho_T,
\tag{C1zB2C6f.24}
\]

und exakt

\[
\boxed{
\langle v_T,A_T\mathbf1_T\rangle=0,
}
\tag{C1zB2C6f.25}
\]

sowie

\[
\boxed{
|\langle v_T,h_T\rangle|
=\rho_T|J_T|
\ge j_*\rho_T.
}
\tag{C1zB2C6f.26}
\]

Damit ist der Zähler vollständig kontrolliert. Es bleibt die `A_T`-Energie des Separators.

---

# 2. Globaler Restoperator-Bound

Der folgende Bound ist grob, aber für C6f ausreichend und benutzt keine Kompaktheit.

## Lemma C1zB2C6f.1 — Restnorm

Es existiert eine absolute Konstante `C_R<\infty`, so dass für alle hinreichend großen `T`

\[
\boxed{
\|R_T\|^2
\le
C_R T e^T.
}
\tag{C1zB2C6f.27}
\]

### Beweis

Für eine feste Primzahl `p` können wegen

\[
p^k\le e^{4T}
\]

höchstens

\[
K_p(T)
:=
\left\lfloor\frac{4T}{\log p}\right\rfloor
\tag{C1zB2C6f.28}
\]

Exponenten `k` auftreten.

Wegen der Orthogonalität verschiedener Primsektoren genügt es, innerhalb eines festen `p` grob mit Cauchy-Schwarz über `k` abzuschätzen.

Setze

\[
y_{p,k}(u)
=
b_{p,k}D_{k\log p}E_Tf(u)\,q_{p,k,T}(u).
\]

Dann

\[
\left\|\sum_{k=1}^{K_p}y_{p,k}(u)\right\|^2
\le
K_p
\sum_{k=1}^{K_p}\|y_{p,k}(u)\|^2.
\tag{C1zB2C6f.29}
\]

Mit `\|q_{p,k,T}(u)\|\le1` folgt nach Integration

\[
\|R_Tf\|^2
\le
\sum_{p\le e^{2T}}
K_p(T)
\sum_{k=1}^{K_p(T)}
 b_{p,k}^2
\|D_{k\log p}E_Tf\|_2^2.
\tag{C1zB2C6f.30}
\]

Für zentrierte Differenzen gilt

\[
\|D_sE_Tf\|_2\le2\|f\|_2.
\tag{C1zB2C6f.31}
\]

Außerdem

\[
b_{p,k}^2
=\log p\,p^{-k/2}.
\]

Daher

\[
\|R_Tf\|^2
\le
4\|f\|^2
\sum_{p\le e^{2T}}
K_p(T)\log p
\sum_{k\ge1}p^{-k/2}.
\tag{C1zB2C6f.32}
\]

Nun

\[
\sum_{k\ge1}p^{-k/2}
=
\frac{p^{-1/2}}{1-p^{-1/2}}
\le
C_0p^{-1/2}
\tag{C1zB2C6f.33}
\]

mit einer absoluten Konstante `C_0`, und

\[
K_p(T)\log p\le4T.
\tag{C1zB2C6f.34}
\]

Somit

\[
\|R_Tf\|^2
\le
C_1T\|f\|^2
\sum_{p\le e^{2T}}p^{-1/2}.
\tag{C1zB2C6f.35}
\]

Wir brauchen nicht einmal den Primzahlsatz. Die grobe Ganzzahlschranke liefert

\[
\sum_{p\le X}p^{-1/2}
\le
\sum_{n\le X}n^{-1/2}
\le2\sqrt X.
\tag{C1zB2C6f.36}
\]

Für `X=e^{2T}` folgt

\[
\|R_Tf\|^2
\le
C_RTe^T\|f\|^2.
\]

Also

\[
\boxed{\|R_T\|^2\le C_RTe^T.}
\]

`□`

### Scope

Der Bound ist absichtlich grob. Er behauptet **keine** optimale Restnorm-Asymptotik.

Er benutzt insbesondere nicht:

- Schattenklassigkeit;
- Kompaktheit;
- einen Grenzoperator;
- einen translationinvarianten Regulator;
- ein verstecktes PNT-Summationsargument.

Damit verletzt er weder B2-A noch B2-B noch C1y.

---

# 3. Separatorenergie

Aus

\[
A_T=I+R_T^*R_T
\]

und Lemma C1zB2C6f.1 folgt als Operatorungleichung

\[
A_T
\le
(1+C_RTe^T)I.
\tag{C1zB2C6f.37}
\]

Für den Separator (C1zB2C6f.23) also

\[
\begin{aligned}
\langle v_T,A_Tv_T\rangle
&\le
(1+C_RTe^T)\|v_T\|^2\\
&=
2\rho_T(1+C_RTe^T).
\end{aligned}
\tag{C1zB2C6f.38}
\]

Damit sind nun beide Größen des C6e-Variationszertifikats explizit kontrolliert.

---

# 4. Hauptsatz — quantitative Reduktion auf den Isolationsradius

## Satz C1zB2C6f.2

Es existieren Konstanten `T_0,C_*,c_*>0`, so dass für alle `T\ge T_0`

\[
\boxed{
\Delta_T^{(1)}
\ge
c_*
\frac{\rho_T}{1+C_*Te^T}.
}
\tag{C1zB2C6f.39}
\]

Insbesondere kann man

\[
c_*=rac{j_*^2}{2}
\]

wählen, wobei

\[
j_*
=
\frac12\min\{a_2a_3,a_2a_5\}>0.
\]

### Beweis

Aus C6es Variationsprinzip

\[
\Delta_T^{(1)}
\ge
\frac{|\langle v_T,h_T\rangle|^2}
{\langle v_T,A_Tv_T\rangle}
\]

und (C1zB2C6f.26), (C1zB2C6f.38) folgt

\[
\begin{aligned}
\Delta_T^{(1)}
&\ge
\frac{j_*^2\rho_T^2}
{2\rho_T(1+C_RTe^T)}\\
&=
\frac{j_*^2}{2}
\frac{\rho_T}{1+C_RTe^T}.
\end{aligned}
\]

`□`

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,quantitative\text{-}reduction\text{-}to\text{-}isolation\text{-}radius}.
}
\]

Für großes `T` kann grob auch geschrieben werden

\[
\boxed{
\Delta_T^{(1)}
\gtrsim
\rho_T\,T^{-1}e^{-T}.
}
\tag{C1zB2C6f.40}
\]

**Firewall:** Dies ist nur dann eine echte asymptotische Untergrenze, wenn `\rho_T` selbst quantitativ kontrolliert wird.

---

# 5. Konsequenz für den Hankel-Determinantenrang

C6d/C6e geben

\[
\det\mathbf K_T^{(1)}
=
\mu_{T,0}\Delta_T^{(1)},
\qquad
\mu_{T,0}=\langle\mathbf1_T,A_T\mathbf1_T\rangle.
\tag{C1zB2C6f.41}
\]

Da `A_T\ge I`, gilt

\[
\mu_{T,0}
\ge
\|\mathbf1_T\|^2
=2T.
\tag{C1zB2C6f.42}
\]

Daher folgt aus Satz C1zB2C6f.2

\[
\boxed{
\det\mathbf K_T^{(1)}
\ge
2Tc_*
\frac{\rho_T}{1+C_*Te^T}.
}
\tag{C1zB2C6f.43}
\]

und somit grob

\[
\boxed{
\det\mathbf K_T^{(1)}
\gtrsim
\rho_Te^{-T}.
}
\tag{C1zB2C6f.44}
\]

Auch hier bleibt `\rho_T` der einzige neue quantitative Engpass.

---

# 6. Warum C6es Zwei-Paar-Trick keine uniforme Breite liefert

C6e beweist exakt:

Für jedes hinreichend große `T` ist mindestens eine der beiden Kanten

\[
x_3(T),\qquad x_5(T)
\]

**kein exakter** Rest-Breakpoint.

Das ist eine Nullstellenaussage über exakte Koinzidenz.

Sie ist nicht dasselbe wie eine quantitative Distanzabschätzung.

Für ein gegenüberliegendes prime-pures Gitter gilt

\[
x_q(T)
-
\left(-T+\frac m2\log r\right)
=
2T-rac12\log\left(\frac q2r^m\right).
\]

Also

\[
\boxed{
\left|
 x_q(T)+T-\frac m2\log r
\right|
=
\frac12
\left|
\log
\frac{e^{4T}}{(q/2)r^m}
\right|.
}
\tag{C1zB2C6f.45}
\]

Für jedes feste Tripel `(q,r,m)` und jedes `\eta>0` kann man `T` beliebig nahe, aber ungleich, an

\[
T_{q,r,m}
=
\frac14\log\left(\frac q2r^m\right)
\tag{C1zB2C6f.46}
\]

wählen. Dann ist die rechte Seite von (C1zB2C6f.45) beliebig klein, obwohl **keine exakte Kollision** vorliegt.

Damit folgt rein logisch:

\[
\boxed{
\text{exakte Nichtkoinzidenz}
\not\Rightarrow
\text{uniformer Abstand}.}
\tag{C1zB2C6f.47}
\]

Das ist bereits innerhalb der tatsächlichen C6e-Gitterformeln sichtbar; es ist kein abstraktes topologisches Argument.

### Wichtige Scope-Firewall

Aus (C1zB2C6f.45) wird **nicht** behauptet, dass jeder erlaubte Gitterpunkt tatsächlich ein nichtverschwindender Breakpoint von `A_T\mathbf1_T` ist.

C6e beweist nur die Supportinklusion

\[
\mathcal B_T^A
\subseteq
\bigcup_r\mathscr L_{r,T}.
\]

Daher beweist §6 genau den richtigen negativen Satz:

\[
\boxed{
\text{Die Supportinklusion allein kann keine uniforme Untergrenze für }\rho_T\text{ liefern.}
}
\tag{C1zB2C6f.48}
\]

Ob die **tatsächlich nichtverschwindenden** Rest-Breakpoints wesentlich dünner sind, ist neue Mathematik und bleibt offen.

---

# 7. Dasselbe Hindernis auf der Hubseite

Auch die gegenüberliegenden Hub-Summenkanten besitzen die Lage

\[
-T+\frac12(\log n+\log m).
\]

Der Abstand zur Cross-Prime-Kante ist daher

\[
\boxed{
\left|
 x_q(T)
-\left(-T+\frac12\log(nm)\right)
\right|
=
\frac12
\left|
\log
\frac{e^{4T}2/q}{nm}
\right|.
}
\tag{C1zB2C6f.49}
\]

C6e kontrolliert die **exakt kollidierenden** Paare `nm=e^{4T}2/q` und zeigt, dass ihre gesamte Sprungmasse

\[
O_q(T^2e^{-3T})
\]

beträgt. Das schützt den Hauptsprung **am Punkt `x_q(T)`**.

Für C6f reicht dies noch nicht.

Nahe, aber nicht exakt kollidierende Produkte `nm` erzeugen eigene Breakpoints in beliebig kleiner Umgebung von `x_q(T)`. C6e enthält noch keine Summationsabschätzung für die **gesamte gewichtete Sprungmasse in einer Umgebung**.

Genau deshalb ist die nächste Frage nicht mehr nur

\[
\operatorname{Jump}_{x_T}h_T\ne0,
\]

sondern eine lokale Variationsfrage.

---

# 8. Breakpoint-only-No-Go für die Skalenfrage

C6e+C6f kennen bisher über die gewählte Kante:

1. einen festen Hauptsprung
   \[
   |J_T|\ge j_*>0;
   \]
2. exakte Nichtkoinzidenz mit `A_T\mathbf1_T` am selben Punkt;
3. endliche Breakpoint-Mengen für jedes feste `T`;
4. den groben Restnormbound
   \[
   \|R_T\|^2\le CTe^T.
   \]

Diese Daten erzwingen **keine** der drei asymptotischen Alternativen

\[
\Delta_T^{(1)}\to0,
\qquad
\Delta_T^{(1)}\asymp1,
\qquad
\Delta_T^{(1)}\to\infty.
\]

Denn Satz C1zB2C6f.2 enthält weiterhin `\rho_T`, und aus den aktuellen Supportinformationen gibt es keinen uniformen unteren Bound dafür.

Formal kann `\rho_T` innerhalb der derzeit erlaubten Information schneller gegen null gehen als jede vorgegebene Skala; ebenso ist ein uniform positiver `\rho_T` durch die bisherigen Sätze nicht ausgeschlossen.

Daher:

\[
\boxed{
[C6e\text{ qualitative jump data}]
+
[C6f\text{ global rest norm}]
\not\Rightarrow
[\text{asymptotic class of }\Delta_T^{(1)}].
}
\tag{C1zB2C6f.50}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,breakpoint\text{-}support\text{-}alone\not\Rightarrow uniform\text{-}scale}.
}
\]

Dies ist ein **Scope-No-Go**, kein No-Go gegen die zweite Probe selbst.

C6es eventualer Rang-2-Satz bleibt vollständig bestehen.

---

# 9. Warum ein bloßer Mindestabstand vermutlich der falsche nächste Invariant ist

Der Isolationsradius `\rho_T` ist für den Beweis bequem, aber analytisch sehr hart: Schon ein winziger zusätzlicher Breakpoint mit extrem kleinem Koeffizienten zwingt `\rho_T` nach unten, obwohl er die Cross-Prime-Trennung praktisch kaum beeinflusst.

Daher wäre eine reine Abschätzung

\[
\rho_T\ge c>0
\]

unnötig stark.

Die robustere Größe ist die **gewichtete lokale Sprungmasse**.

Für eine stückweise konstante Funktion `g_T` und Radius `r>0` definiere

\[
\boxed{
\mathcal V_T(g;x_T,r)
:=
\sum_{\substack{y\in\mathcal B(g)\\0<|y-x_T|<r}}
|\operatorname{Jump}_y g|.
}
\tag{C1zB2C6f.51}
\]

Für den Hub schreiben wir

\[
\mathcal V_T^h(r)
:=
\mathcal V_T(h_T;x_T,r),
\]

und für die Restmetrik

\[
\mathcal V_T^A(r)
:=
\mathcal V_T(A_T\mathbf1_T;x_T,r).
\]

Eine starke, aber wesentlich realistischere C6g-Zielbedingung wäre die Existenz einer expliziten Radiusfolge `r_T` mit

\[
\boxed{
\mathcal V_T^h(r_T)
\le
\frac14j_*
}
\tag{C1zB2C6f.52}
\]

und einer kompatiblen Kontrolle der lokalen Variation von `A_T\mathbf1_T`.

Dann dürften innerhalb des Intervalls durchaus viele zusätzliche Sprünge liegen, solange ihre **Gesamtmasse** klein genug bleibt.

Das würde die harte geometrische Forderung „keine weitere Kante“ durch eine gewichtete analytische Forderung ersetzen.

---

# 10. Quantitatives Korrekturprinzip für nichtkonstante Restseite

C6f hält hier bewusst die nächste Tür offen.

Sei

\[
w_{T,r}
=
1_{(x_T-r,x_T)}
-
1_{(x_T,x_T+r)}.
\tag{C1zB2C6f.53}
\]

Falls `A_T\mathbf1_T` innerhalb dieses Intervalls nicht konstant ist, gilt im Allgemeinen

\[
\langle w_{T,r},A_T\mathbf1_T\rangle\ne0.
\]

Man kann jedoch formal gegen einen zweiten lokalen Vektor `z_{T,r}` korrigieren:

\[
\widetilde v_{T,r}
=
w_{T,r}
-
\frac{
\langle w_{T,r},A_T\mathbf1_T\rangle
}{
\langle z_{T,r},A_T\mathbf1_T\rangle
}
z_{T,r},
\tag{C1zB2C6f.54}
\]

sofern der Nenner nicht verschwindet.

Dann exakt

\[
\langle\widetilde v_{T,r},A_T\mathbf1_T\rangle=0.
\tag{C1zB2C6f.55}
\]

Dies ist noch **kein** C6f-Satz, weil eine kanonische Wahl von `z_{T,r}` und quantitative Kontrolle des Korrekturfaktors fehlen.

Es zeigt aber, warum C6g nicht zwingend einen echten leeren Breakpoint-Spalt benötigt. Kleine gewichtete Restvariation könnte genügen.

**Firewall:** C6f behauptet keine solche Korrekturabschätzung ohne Beweis.

---

# 11. Was C6f über die normierte zweite Probe sagt

C6e definiert eventual

\[
\widehat\psi_{T,1}
=
\frac{
\mathfrak S_T\zeta_T
-(\mu_{T,1}/\mu_{T,0})\zeta_T
}{\sqrt{\Delta_T^{(1)}}}.
\tag{C1zB2C6f.56}
\]

C6f zeigt:

Die mögliche quantitative Instabilität dieser Normalisierung ist vollständig an die noch offene Skala von

\[
\Delta_T^{(1)}
\]

gebunden.

Der neue Bound (C1zB2C6f.39) liefert zwar

\[
\frac1{\sqrt{\Delta_T^{(1)}}}
\lesssim
\sqrt{
\frac{1+Te^T}{\rho_T}
},
\tag{C1zB2C6f.57}
\]

aber ohne `\rho_T`-Kontrolle ist dies keine uniforme Probe-Schranke.

Daher bleibt ausdrücklich möglich, dass

\[
\Delta_T^{(1)}\downarrow0
\]

entlang einer Folge, obwohl

\[
\Delta_T^{(1)}>0
\]

für jedes hinreichend große `T` gilt.

Ebenso bleibt möglich, dass `\Delta_T^{(1)}` uniform positiv oder wachsend ist.

C6f entscheidet diese Alternativen nicht.

---

# 12. Verhältnis zur C4-Skala

C4 liefert für einen festen alten Sourcevektor mit erstem aktiven Jet `m`

\[
\sigma_T(J_{R,T}f)
\gtrsim
\frac{e^T}{T^{2m+3}}.
\tag{C1zB2C6f.58}
\]

Diese Divergenzskala darf **nicht** auf `\Delta_T^{(1)}` übertragen werden.

Die Größen messen verschiedene Dinge:

- C4: absolute Response-Energie eines festen Sourcevektors gegen die Konstantenprobe;
- C6e/C6f: orthogonaler Krylov-Defekt der zweiten targetseitigen Response-Richtung.

Insbesondere folgt aus

\[
\sigma_T(J_{R,T}f)\to\infty
\]

nicht

\[
\Delta_T^{(1)}\to\infty.
\]

Diese Trennung ist wichtig für die spätere Jet-Alignment-Frage.

---

# 13. Reconciliation mit C6d und C6e

## C6d

C6d reduzierte den ersten Multi-Probe-Test auf

\[
\Delta_T^{(1)}.
\]

C6f ändert daran nichts.

## C6e

C6e beweist

\[
\exists T_0\ \forall T\ge T_0:
\Delta_T^{(1)}>0.
\]

C6f supersediert **nicht** diesen Satz.

C6f supersediert ausschließlich die noch unscharfe quantitative Formulierung

\[
\text{„offen sind }\varepsilon_T
\text{ und }\langle v_T,A_Tv_T\rangle\text{“}.
\]

Nach C6f ist die Situation präziser:

1. die Separatorenergie besitzt den globalen Bound
   \[
   \langle v_T,A_Tv_T\rangle
   \le
   2\rho_T(1+C_RTe^T);
   \]
2. der Sprungbetrag ist uniform von null getrennt;
3. der einzige verbleibende Parameter dieses Beweiswegs ist `\rho_T`.

Damit lautet die korrigierte quantitative Firewall:

\[
\boxed{
\text{Nicht die Restenergie, sondern lokale Breakpoint-Crowding ist jetzt der erste Engpass.}
}
\tag{C1zB2C6f.59}
\]

---

# 14. No-Go-Persistenzmatrix

| Früherer Knoten | Gesiegelter Befund | Wirkung in C6f |
|---|---|---|
| C1y | translationsinvariante Regulatoren lösen den Hub/Rest-Konflikt im C1y-Scope nicht | unverändert; `R_T` bleibt source-windowed und nichttranslationinvariant |
| B2-A | Gamma-Präkonditionierung liefert keinen fehlenden finite Schattenmechanismus | unverändert; Restnormbound ist reine Operatornormabschätzung |
| B2-B | naiver Haar-`L^2`-Endpunkt reicht nicht | unverändert |
| C4 | unendliche Boundary-Jet-Hierarchie; kein fixer endlicher Jet reicht global | unverändert |
| C5/C6a | totale Odd-Divergenz für jeden nichtnull Odd-Graphvektor | unverändert |
| C6 | kein voller Odd-Transport durch festen endlichen Jetquotienten | unverändert |
| C6a | kanonische Jet-ONB / trianguläre Transitionen | unverändert; keine Rate importiert |
| C6a | Self-Grams allein bestimmen Cross-Terminal-Geometrie nicht | unverändert |
| C6b | C2-Flachheit allein reicht nicht | unverändert |
| C6c | `tau=>kappa` auf festem Fenster | unverändert |
| C6c | Triangularität allein reicht nicht | unverändert |
| C6d | C4-Jets sind keine automatischen Multi-Probes | unverändert |
| C6d | primitive `A_T`-Krylovquelle kollabiert | unverändert |
| C6e | eventualer Krylov-Rang 2 | **bleibt positiv gesiegelt** |
| C6e | keine uniforme `Delta`-Skala | präzisiert: auf `rho_T` reduziert |

---

# 15. Was C6f ausdrücklich nicht beweist

Nicht bewiesen sind:

- eine uniforme positive Untergrenze für `\rho_T`;
- eine optimale oder auch nur scharfe Asymptotik von `\|R_T\|`;
- `\Delta_T^{(1)}\to0`;
- `\inf_T\Delta_T^{(1)}>0`;
- `\Delta_T^{(1)}\to\infty`;
- eine natürliche C3/C4-Skala für `\Delta_T^{(1)}`;
- eine uniforme Normschranke für `\widehat\psi_{T,1}`;
- Jet-Alignment der zweiten Probe;
- eine Untergrenze für `s_{\min}(\mathcal P_T^{(1)})`;
- `\varepsilon_T^{\rm probe}(R,1)\to0`;
- `\tau_T(E_{R,1})\to0`;
- `\Theta_{T,U}^{E_{R,1}}\to I`;
- Krylov-Rang `N\ge2`;
- ein Odd-Gauge-Grenzwert.

Insbesondere wird die vom Gegenprüfer geforderte negative Möglichkeit ausdrücklich offen gehalten:

\[
\boxed{
\Delta_T^{(1)}\to0
\text{ ist mit dem aktuellen Stand vereinbar.}
}
\tag{C1zB2C6f.60}
\]

Falls sie später bewiesen wird, muss sie als eigener asymptotischer Degenerations-No-Go gesiegelt werden.

---

# 16. Exakter nächster Arbeitsauftrag C6g

C6f zeigt, dass ein weiterer reiner Mindestabstands-Audit wahrscheinlich zu stark und methodisch ungeschickt wäre.

Der nächste natürliche Knoten ist:

\[
\boxed{
\text{C6g: gewichtete lokale Breakpoint-Crowding-Schätzung um die Cross-Prime-Kante.}
}
\tag{C1zB2C6f.61}
\]

Der Arbeitsauftrag lautet:

## A. Hub-Crowding

Für

\[
x_T=x_{q_T}(T)
\]

schätze die gesamte Sprungmasse aller **anderen** Hubkanten in

\[
(x_T-r,x_T+r).
\]

Ziel wäre eine explizite Folge `r_T` mit

\[
\mathcal V_T^h(r_T)
\le
\theta j_*,
\qquad
\theta<1.
\tag{C1zB2C6f.62}
\]

## B. Rest-Crowding

Kontrolliere die lokale Variation von

\[
A_T\mathbf1_T
\]

im selben Fenster quantitativ, nicht nur ihre Sprungorte.

## C. Korrigierter Separator

Konstruiere gegebenenfalls einen lokalen Separator `\widetilde v_{T,r_T}`, der

\[
\langle\widetilde v_{T,r_T},A_T\mathbf1_T\rangle=0
\]

exakt erfüllt, ohne einen vollständig leeren Breakpoint-Spalt zu verlangen.

## D. Quantitative Zweitprobe

Leite daraus eine echte Untergrenze für

\[
\Delta_T^{(1)}
\]

ab und entscheide erst dann, ob die normierte zweite Probe asymptotisch stabil ist.

### Harte Firewall für C6g

Ein Resultat der Form

\[
\text{„die Breakpoints sind diskret“}
\]

reicht nicht mehr.

Benötigt wird eine **gewichtete** lokale Abschätzung der tatsächlich nichtverschwindenden Sprungkoeffizienten.

Ebenso darf aus eventualem Rang 2 nicht auf quantitative Jet-Ausrichtung geschlossen werden.

---

# 17. Endurteil

C6f liefert zwei echte Fortschritte und einen klaren No-Go im richtigen Scope.

Erstens besitzt der konditionierte Restoperator die grobe globale Schranke

\[
\boxed{
\|R_T\|^2\le C_RTe^T.
}
\]

Zweitens wird C6es Variationszertifikat auf eine einzige geometrische Größe reduziert:

\[
\boxed{
\Delta_T^{(1)}
\ge
c_*
\frac{\rho_T}{1+C_*Te^T}.
}
\]

Drittens reicht die bisherige Breakpoint-Supportgeometrie **nicht**, um `\rho_T` uniform zu kontrollieren. Exakte Nichtkoinzidenz ist qualitativ stark genug für Rang 2, aber quantitativ zu schwach für die Stabilität der zweiten Probe.

Damit lautet der neue Engpass nicht mehr

\[
\text{„existiert eine zweite Probe?“}
\]

— das ist durch C6e positiv entschieden — sondern

\[
\boxed{
\text{„bleibt der Cross-Prime-Sprung gegenüber der gewichteten lokalen Breakpoint-Masse quantitativ sichtbar?“}
}
\tag{C1zB2C6f.63}
\]

Genau diese Frage muss C6g beantworten, bevor ein sinnvoller `2\times2`-Jet-Alignment-Audit begonnen wird.
