# P11-C1z-B2-C6t — Erster Martingalkanal, 2-adischer Hubfilter und Drei-Prim-Selektor

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6t]`  
**Direkte Voraussetzungen:** C1z-B, C1z-B2-C3, C1z-B2-C6e, C1z-B2-C6g, C1z-B2-C6h, C1z-B2-C6i, C1z-B2-C6q, C1z-B2-C6r, C1z-B2-C6s  
**Strukturelle Schnittstellen:** C1z-B2-C4, C1z-B2-C6a, C1z-B2-C6c, C1z-B2-C6d, C1z-B2-C6f, C1z-B2-C6j, C1z-B2-C6m, C1z-B2-C6n, C1z-B2-C6o, C1z-B2-C6p  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d `orthogonality != jet alignment`, C1z-B2-C6k `current data != Wronskian nonzero`, C1z-B2-C6l `C4 constant-mode mechanism does not transfer`, C1z-B2-C6m `A-orthogonality != bulk cancellation`, C1z-B2-C6n `positivity != alignment`, C1z-B2-C6o `raw support separation route fails`, C1z-B2-C6p `fixed-vector divergence != moving-vector control`, C1z-B2-C6q `cross-prime provenance != rest smallness`, C1z-B2-C6r `moment orthogonality != q_r small`, C1z-B2-C6s `same order != cancellation`.  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6t]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm pos,first\text{-}martingale\text{-}channel=prime\text{-}hub}
+
\checkmark[M]_{\rm pos,p=2\text{-}channel=restricted\text{-}two\text{-}adic\text{-}hub\text{-}energy}
+
\checkmark[M]_{\rm pos,exact\text{-}jump\text{-}transport\text{-}lattice}
+
\checkmark[M]_{\rm pos,three\text{-}odd\text{-}prime\text{-}rest\text{-}collision\text{-}selector}
+
\checkmark[M]_{\rm pos,right\text{-}hub\text{-}collision\text{-}classification}
+
\checkmark[M]_{\rm pos,eventual\text{-}nonzero\text{-}first\text{-}channel}
+
\checkmark[M]_{\rm pos,R_Tr_T\neq0\text{-}eventually}
+
\checkmark[M]_{\rm neg,nonzero\text{-}channel\not\Rightarrow q_r\not\to0}
+
\checkmark[M]_{\rm corr,pointwise\text{-}locking\text{-}question\to jump\text{-}transport\text{-}question}
+
?[O]_{\rm quantitative\text{-}first\text{-}channel/\|r_T\|^2}
+
?[O]_{\rm q_r\text{-}asymptotic}
+
?[O]_{\rm bare\text{-}angle\text{-}lower\text{-}bound}
+
?[O]_{\rm second\text{-}alignment\text{-}scalar\neq0}
}
\]

C6s faktorisierte die Restenergie in nichtnegative Martingalkanäle. C6t untersucht den flachsten Kanal `a=0`, beginnend mit `p=2`.

Der Hauptbefund ist positiv und stärker als eine bloße Zugänglichkeitsaussage:

1. Der `a=0`-Kanal einer Primzahl `p` ist exakt die auf die innere Tiefenregion eingeschränkte Energie des **p-reinen Huboperators**.
2. Für `p=2` kann eine arithmetische Drei-Prim-Auswahl `q_T in {3,5,7}` getroffen werden, so dass entlang der gesamten relevanten `2`-adischen Verschiebungslattice kein prime-purer Restbreakpoint von `A_T 1_T` kollidiert.
3. Am dazugehörigen inneren Punkt `u_{q_T}(T)=T-(1/2)log q_T` besitzt der 2-adische Hubfilter von `r_T` für alle hinreichend großen `T` einen echten Sprung.
4. Daher ist der erste Martingalkanal eventual strikt positiv:

\[
\boxed{
\mathcal E_{2,0,T}(r_T)>0,
\qquad
R_Tr_T\ne0.
}
\]

Dies entscheidet noch **nicht** `q_{r,T}\not\to0`, weil dafür eine quantitative untere Schranke relativ zu `||r_T||^2` nötig wäre. Aber die Möglichkeit, dass der gesamte Restzähler bereits im flachsten Kanal exakt verschwindet, ist ausgeschlossen.

---

# 0. Verbindliche Notation

Auf

\[
\mathscr H_T=L^2(-T,T)
\]

steht der source-windowed Huboperator

\[
\boxed{
H_T
=
\sum_{n=p^k\in\mathcal N_T}
a_nK_{\log n},
\qquad
a_{p^k}=\sqrt{\log p}\,p^{-3k/4},
}
\tag{C1zB2C6t.1}
\]

mit

\[
\boxed{
K_s=P_TD_sE_T.
}
\tag{C1zB2C6t.2}
\]

Für die zentrierte Differenz gilt auf der Nullfortsetzung

\[
(K_sf)(u)
=
(E_Tf)(u+s/2)-(E_Tf)(u-s/2),
\tag{C1zB2C6t.3}
\]

für fast alle `u in (-T,T)`.

Insbesondere

\[
K_s^*=-K_s
\]

und

\[
K_s1_T
=
1_{(-T,-T+s/2)}-1_{(T-s/2,T)}.
\tag{C1zB2C6t.4}
\]

Wie in C6s setzen wir

\[
\boxed{
A_T:=I+R_T^*R_T,
\qquad
a_T:=A_T1_T,
}
\tag{C1zB2C6t.5}
\]

\[
\boxed{
h_T:=H_T^*H_T1_T,
}
\tag{C1zB2C6t.6}
\]

\[
\boxed{
\lambda_T
:=
\frac{\langle1_T,h_T\rangle}
{\langle1_T,A_T1_T\rangle}
\ge0,
}
\tag{C1zB2C6t.7}
\]

und

\[
\boxed{
r_T:=h_T-\lambda_Ta_T.
}
\tag{C1zB2C6t.8}
\]

C6r korrigierte die exakte Residualorthogonalität zu

\[
\langle r_T,1_T\rangle=0.
\]

Der Restquotient lautet

\[
\boxed{
q_{r,T}
=
\frac{\|R_Tr_T\|^2}{\|r_T\|^2}.
}
\tag{C1zB2C6t.9}
\]

C6s zeigte die kanalweise Zerlegung von `||R_T r_T||^2`. C6t untersucht ausschließlich den ersten Kanal.

---

# 1. Der erste Martingalkanal ist exakt ein p-reiner Hub

C6s definiert für `a>=0`

\[
\Phi_{p,a,T}[f](u)
:=
\sum_{k\ge a+1}
p^{-3k/4}(K_{k\log p}f)(u),
\tag{C1zB2C6t.10}
\]

und

\[
\Omega_{p,a,T}
:=
\left\{
|u|\le T-\frac{a+1}{2}\log p
\right\}.
\tag{C1zB2C6t.11}
\]

Für `a=0` ist

\[
\boxed{
\Phi_{p,0,T}[f](u)
=
\sum_{k\ge1}
p^{-3k/4}(K_{k\log p}f)(u).
}
\tag{C1zB2C6t.12}
\]

Definiere nun den **p-reinen Huboperator**

\[
\boxed{
H_{p,T}
:=
\sum_{k\ge1}
\sqrt{\log p}\,p^{-3k/4}K_{k\log p},
}
\tag{C1zB2C6t.13}
\]

wobei wie immer nur die bei festem `T` aktiven Prime-Power-Labels beitragen.

Dann gilt exakt

\[
\boxed{
\Phi_{p,0,T}[f]
=
\frac1{\sqrt{\log p}}H_{p,T}f.
}
\tag{C1zB2C6t.14}
\]

Der C6s-Kanal besitzt das Gewicht

\[
(\log p)(p-1).
\]

Daher ist seine Energie

\[
\boxed{
\mathcal E_{p,0,T}(f)
:=
(\log p)(p-1)
\int_{\Omega_{p,0,T}}
|\Phi_{p,0,T}[f](u)|^2du
}
\]

exakt

\[
\boxed{
\mathcal E_{p,0,T}(f)
=
(p-1)
\int_{\Omega_{p,0,T}}
|H_{p,T}f(u)|^2du.
}
\tag{C1zB2C6t.15}
\]

Dies ist keine Asymptotik und keine Majorante.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,first\text{-}martingale\text{-}channel=prime\text{-}hub}.
}
\]

## 1.1 Spezialfall p=2

Für `p=2` ist `p-1=1`. Setze

\[
\delta:=\frac12\log2,
\qquad
c_k:=2^{-3k/4}.
\tag{C1zB2C6t.16}
\]

Dann

\[
\boxed{
H_{2,T}
=
\sqrt{\log2}
\sum_{k\ge1}c_kK_{k\log2}
}
\tag{C1zB2C6t.17}
\]

und

\[
\boxed{
\Omega_{2,0,T}
=
[-T+\delta,T-\delta].
}
\tag{C1zB2C6t.18}
\]

Der erste `2`-adische Restkanal des Residualvektors ist daher schlicht

\[
\boxed{
\mathcal E_{2,0,T}(r_T)
=
\int_{-T+\delta}^{T-\delta}
|H_{2,T}r_T(u)|^2du.
}
\tag{C1zB2C6t.19}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,p=2\text{-}channel=restricted\text{-}two\text{-}adic\text{-}hub\text{-}energy}.
}
\]

---

# 2. Exakte Sprungtransportformel des 2-adischen Hubfilters

Sei `f` eine der in der P11-Kette auftretenden stückweisen Funktionen. Schreibe

\[
J_f(x):=\operatorname{Jump}_xf.
\]

Aus (C1zB2C6t.3) folgt für jeden Punkt `u`, an dem die endliche aktive Summe betrachtet wird,

\[
\boxed{
\operatorname{Jump}_u(K_{k\log2}f)
=
J_f(u+k\delta)-J_f(u-k\delta),
}
\tag{C1zB2C6t.20}
\]

wobei Randpunkte der Nullfortsetzung als Sprünge der fortgesetzten Funktion mitgezählt werden.

Daher

\[
\boxed{
\operatorname{Jump}_u(H_{2,T}f)
=
\sqrt{\log2}
\sum_{k\ge1}
c_k
\bigl(
J_f(u+k\delta)-J_f(u-k\delta)
\bigr).
}
\tag{C1zB2C6t.21}
\]

Der C6t-Test ist damit keine diffuse punktweise Auswertung mehr. Er ist eine gewichtete Faltung der Sprungmaße von `f` entlang einer einzigen `delta=(log2)/2`-Lattice.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,exact\text{-}jump\text{-}transport\text{-}lattice}.
}
\]

---

# 3. Der kanonische innere Beobachtungspunkt

Für eine feste ungerade Primzahl `q` setze

\[
\boxed{
u_q(T):=T-\frac12\log q.}
\tag{C1zB2C6t.22}
\]

Da `q>2`, gilt

\[
\frac12\log q>\frac12\log2=\delta.
\]

Also liegt `u_q(T)` strikt im ersten Martingalbereich:

\[
\boxed{
u_q(T)\in\Omega_{2,0,T}.}
\tag{C1zB2C6t.23}
\]

Die verschobenen Punkte der Sprungtransportformel sind exakt

\[
\boxed{
u_q(T)+k\delta
=
T-\frac12\log\left(\frac q{2^k}\right),}
\tag{C1zB2C6t.24}
\]

und

\[
\boxed{
u_q(T)-k\delta
=
T-\frac12\log(q2^k).}
\tag{C1zB2C6t.25}
\]

Damit trifft die `2`-adische Filterlattice genau die arithmetischen Summe-/Differenzkanten der Labelpaare

\[
\{2^k,q\}.
\]

Dies ist der Grund, weshalb `p=2,a=0` strukturell aufschlussreich ist.

---

# 4. Rechte Hubkollisionen an u_q: eindeutige Primfaktorzerlegung

C6e/C6g typisieren die rechten Hubkanten von

\[
h_T=H_T^*H_T1_T
\]

als Summe-/Differenzkanten der Prime-Power-Labels.

Wir klassifizieren nun diejenigen rechten Kanten, die nach einer `2`-adischen Verschiebung genau auf `u_q(T)` transportiert werden.

## 4.1 Plus-Lattice

Ein rechter Differenzbreakpoint hat die Form

\[
T-\frac12|\log(m/n)|.
\]

Gleichheit mit `u_q+k\delta` bedeutet

\[
|\log(m/n)|
=
\log(q/2^k).
\]

Dies ist nur möglich, wenn `2^k<q`. Dann liefert eindeutige Primfaktorzerlegung bei Prime-Power-Labels exakt

\[
\boxed{
\{m,n\}=\{q,2^k\}.
}
\tag{C1zB2C6t.26}
\]

Andere rechte Prime-Power-Paare können dort nicht kollidieren.

## 4.2 Minus-Lattice

Ein rechter Summenbreakpoint hat die Form

\[
T-\frac12(\log n+\log m).
\]

Gleichheit mit `u_q-k\delta` bedeutet

\[
nm=q2^k.
\]

Da `n,m` jeweils Prime-Powers sind und `q` ungerade prim ist, folgt wiederum exakt

\[
\boxed{
\{m,n\}=\{q,2^k\}.
}
\tag{C1zB2C6t.27}
\]

Andere rechte Hubpaare kollidieren nicht.

## 4.3 Vorzeichen

Aus der exakten Formel

\[
K_s1_T
=
1_{(-T,-T+s/2)}-1_{(T-s/2,T)}
\]

folgt durch direkte Einsetzung in `K_a^*K_b1_T`:

- die rechte Summenkante des Paares `{2^k,q}` trägt im relevanten geordneten Kreuzterm ein positives Sprungvorzeichen;
- die rechte Differenzkante trägt das entgegengesetzte Sprungvorzeichen;
- im äußeren Operator `K_{k\log2}` wird die Minus-Lattice subtrahiert.

Daher erscheinen beide direkten rechten Beiträge in

\[
\operatorname{Jump}_{u_q(T)}H_{2,T}h_T
\]

mit **demselben Vorzeichen**.

Insbesondere liefert bereits das primitive Paar `{2,q}` einen festen, von `T` unabhängigen nichtverschwindenden Direktbeitrag.

Für eine bequeme positive Konstante können wir daher schreiben

\[
\boxed{
J_q^{\rm dir}>0
}
\tag{C1zB2C6t.28}
\]

so dass die Summe aller rechten direkten `{2^k,q}`-Beiträge für großes `T` Betrag mindestens `J_q^{dir}` besitzt.

Die exakte numerische Maximierung dieser Konstante wird nicht benötigt; entscheidend ist, dass sie nur von der festen Primzahl `q` abhängt und **nicht** von `T`.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,right\text{-}hub\text{-}collision\text{-}classification}.
}
\]

---

# 5. Terminale Hubkollisionen sind ein verschwindender Fehler

Neben den rechten direkten Kanten können an den Punkten

\[
u_q\pm k\delta
\]

nur noch Kanten von der gegenüberliegenden Terminalseite kollidieren.

Für große `T` sind Einzel- und Differenzkanten von der linken Seite wegen der aktiven Labelgrenze `n,m<=e^{2T}` ausgeschlossen; übrig bleiben terminale Summenkanten

\[
-T+\frac12\log(nm).
\]

Die Kollisionsgleichungen lauten

\[
\boxed{
nm
=
e^{4T}\frac{2^k}{q}}
\tag{C1zB2C6t.29}
\]

für die Plus-Lattice und

\[
\boxed{
nm
=
e^{4T}\frac1{q2^k}}
\tag{C1zB2C6t.30}
\]

für die Minus-Lattice.

Für ein solches Paar gilt elementar

\[
a_na_m
\le
\sqrt{\log n\log m}\,(nm)^{-3/4}
\le
2T\,(nm)^{-3/4}.
\tag{C1zB2C6t.31}
\]

Der äußere `2`-adische Filter liefert zusätzlich `c_k=2^{-3k/4}`.

Für (C1zB2C6t.29) ergibt sich daher der Faktor

\[
c_k(nm)^{-3/4}
=
q^{3/4}e^{-3T}2^{-3k/2}.
\tag{C1zB2C6t.32}
\]

Außerdem ist wegen `nm<=e^{4T}` nur `2^k<=q` möglich. Dies betrifft also nur endlich viele `k`, unabhängig von `T`.

Für (C1zB2C6t.30) gilt

\[
c_k(nm)^{-3/4}
=
q^{3/4}e^{-3T}.
\tag{C1zB2C6t.33}
\]

Hier gibt es höchstens `O(T)` aktive `k`.

Die Zahl geordneter Faktorisierungen eines festen Produkts `P` als Produkt zweier Prime-Powers ist elementar höchstens polynomial in `log P`: besitzt `P` einen einzigen Primteiler, gibt es `O(log P)` Exponentensplits; besitzt `P` zwei Primteiler, gibt es nur endlich viele Zuordnungen; bei mehr als zwei Primteilern gibt es keine solche Faktorisierung.

Zusammen mit dem universellen Sprungbound für `K_a^*K_b1_T` aus C6g folgt daher für jedes feste `q` eine polynomielle Konstante `C_q` mit

\[
\boxed{
\mathcal J_{q,T}^{\rm terminal}
=
O_q(T^C e^{-3T})
}
\tag{C1zB2C6t.34}
\]

für irgendeine feste absolute Potenz `C`.

Mögliche Kollisionen mit der äußeren Fensterkante selbst besitzen wegen `k\asymp T` zusätzlich den geometrischen Filterfaktor `c_k=O_q(e^{-3T})`; mit der groben elementaren Hubgewichtsmajorante bleiben auch sie `o_q(1)`.

Folglich

\[
\boxed{
\operatorname{Jump}_{u_q(T)}H_{2,T}h_T
=
\mathcal J_q^{\rm dir}(T)+o_q(1),
}
\tag{C1zB2C6t.35}
\]

mit

\[
|\mathcal J_q^{\rm dir}(T)|\ge J_q^{\rm dir}>0
\]

für alle hinreichend großen `T`.

Insbesondere existiert `T_q<infty` mit

\[
\boxed{
|\operatorname{Jump}_{u_q(T)}H_{2,T}h_T|
\ge
\frac12J_q^{\rm dir}>0
\qquad(T\ge T_q).
}
\tag{C1zB2C6t.36}
\]

---

# 6. Restbreakpoints entlang der gesamten 2-adischen Lattice

Nun betrachten wir

\[
a_T=A_T1_T=1_T+R_T^*R_T1_T.
\]

C6h typisiert die nichttrivialen Restbreakpoints prime-pure. Rechts liegen sie auf Gittern der Form

\[
T-\frac m2\log p,
\]

und von der gegenüberliegenden Seite auf

\[
-T+\frac m2\log p,
\]

neben den äußeren Fensterkanten.

Fixiere wieder eine ungerade Primzahl `q`.

## 6.1 Rechte prime-pure Breakpoints sind unmöglich

Gleichheit

\[
T-\frac m2\log p
=
u_q+k\delta
\]

würde

\[
p^m=q2^{-k}
\]

fordern, unmöglich für `k>=1`.

Gleichheit

\[
T-\frac m2\log p
=
u_q-k\delta
\]

würde

\[
p^m=q2^k
\]

fordern. Da `q` ungerade prim ist und `k>=1`, ist die rechte Seite keine Primzahlpotenz.

Somit:

\[
\boxed{
\text{Kein rechter prime-purer Restbreakpoint liegt auf }
\{u_q\pm k\delta:k\ge1\}.
}
\tag{C1zB2C6t.37}
\]

Dies ist eine exakte arithmetische Aussage.

## 6.2 Gegenüberliegende Restbreakpoints

Eine Kollision

\[
-T+\frac m2\log p
=
u_q+k\delta
\]

ist äquivalent zu

\[
\boxed{
e^{4T}=q\,2^{-k}p^m.}
\tag{C1zB2C6t.38}
\]

Eine Kollision mit `u_q-k\delta` ist äquivalent zu

\[
\boxed{
e^{4T}=q\,2^{k}p^m.}
\tag{C1zB2C6t.39}
\]

Auch eine mögliche äußere Fensterkollision ist von derselben arithmetischen Form ohne einen zusätzlichen ungeraden Primfaktor.

Damit ist ein odd-prime `q` genau dann für den C6t-Test **rest-kollisionsgefährdet**, wenn

\[
\boxed{
e^{4T}=q\,2^z p^m}
\tag{C1zB2C6t.40}
\]

für irgendein `z in Z`, irgendeine Primzahl `p` und `m>=1` gilt, wobei reine `q2^z`-Fälle als Randfall mitgemeint sind.

---

# 7. Drei-Prim-Selektor: mindestens eine gesamte Lattice ist restfrei

Betrachte die drei festen ungeraden Primzahlen

\[
\boxed{\mathcal Q:=\{3,5,7\}.}
\tag{C1zB2C6t.41}
\]

## Satz C6t.1

Für jedes `T` existiert mindestens ein

\[
\boxed{q_T\in\{3,5,7\}}
\tag{C1zB2C6t.42}
\]

so dass **keine** Gleichung der Form

\[
e^{4T}=q_T2^zp^m
\]

mit `z in Z`, `p` prim und `m>=1` gilt.

### Beweis

Falls für kein `q` eine Darstellung existiert, ist nichts zu zeigen.

Existiert eine Darstellung für irgendein `q`, so ist `e^{4T}` rational und seine ungerade Primträgerstruktur ist in dieser Darstellung in höchstens zwei ungeraden Primzahlen enthalten: in `q` und gegebenenfalls in `p`.

Nehmen wir an, alle drei `q=3,5,7` wären gefährdet. Dann müsste dieselbe positive rationale Zahl `e^{4T}` drei Darstellungen

\[
3\,2^{z_3}p_3^{m_3}
=
5\,2^{z_5}p_5^{m_5}
=
7\,2^{z_7}p_7^{m_7}
\]

besitzen.

Nach Entfernen der Zweierpotenzen erzwingt eindeutige Primfaktorzerlegung, dass der ungerade Primträger der gemeinsamen Zahl gleichzeitig `3`, `5` und `7` enthält.

Die erste Darstellung kann aber höchstens die beiden ungeraden Primzahlen `3` und `p_3` enthalten. Widerspruch.

Also sind höchstens zwei der drei Kandidaten gefährdet. `□`

Damit wählen wir für jedes `T` ein `q_T` mit

\[
\boxed{
\operatorname{Jump}_{u_{q_T}(T)}H_{2,T}a_T=0.
}
\tag{C1zB2C6t.43}
\]

Denn weder rechte prime-pure Breakpoints noch gegenüberliegende/äußere Breakpoints liegen an einem der in (C1zB2C6t.21) ausgewerteten Latticepunkte.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,three\text{-}odd\text{-}prime\text{-}rest\text{-}collision\text{-}selector}.
}
\]

**Bemerkung.** Dies ist stärker als der ursprüngliche Zwei-Paar-Selektor aus C6e für einen einzelnen Cross-Prime-Ort. Hier wird für das gewählte `q_T` die **gesamte 2-adische Verschiebungslattice** des ersten Martingalkanals restfrei gemacht.

---

# 8. Eventual nichtverschwindender erster p=2-Kanal

Für den nach Satz C6t.1 gewählten Kandidaten gilt

\[
r_T=h_T-\lambda_Ta_T.
\]

Daher

\[
\operatorname{Jump}_{u_{q_T}}H_{2,T}r_T
=
\operatorname{Jump}_{u_{q_T}}H_{2,T}h_T
-
\lambda_T
\operatorname{Jump}_{u_{q_T}}H_{2,T}a_T.
\]

Nach (C1zB2C6t.43) verschwindet der zweite Term **exakt**:

\[
\boxed{
\operatorname{Jump}_{u_{q_T}}H_{2,T}r_T
=
\operatorname{Jump}_{u_{q_T}}H_{2,T}h_T.
}
\tag{C1zB2C6t.44}
\]

Da `q_T` nur drei mögliche Werte besitzt, können wir die drei festen Schwellen aus (C1zB2C6t.36) vereinheitlichen. Es existieren also `T_0<infty` und `j_0>0` mit

\[
\boxed{
|\operatorname{Jump}_{u_{q_T}(T)}H_{2,T}r_T|
\ge j_0
\qquad(T\ge T_0).
}
\tag{C1zB2C6t.45}
\]

Außerdem liegt `u_{q_T}(T)` nach (C1zB2C6t.23) strikt im Integrationsbereich `Omega_{2,0,T}`.

Eine Funktion mit einem echten Sprung im Inneren eines Intervalls kann dort nicht fast überall null sein. Also

\[
\boxed{
\int_{\Omega_{2,0,T}}
|H_{2,T}r_T(u)|^2du
>0
\qquad(T\ge T_0).
}
\tag{C1zB2C6t.46}
\]

Mit (C1zB2C6t.19):

\[
\boxed{
\mathcal E_{2,0,T}(r_T)>0
\qquad(T\ge T_0).
}
\tag{C1zB2C6t.47}
\]

Da C6s die Gesamtenergie als Summe nichtnegativer Kanäle schreibt,

\[
\|R_Tr_T\|^2
\ge
\mathcal E_{2,0,T}(r_T),
\]

folgt insbesondere

\[
\boxed{
R_Tr_T\ne0
\qquad(T\ge T_0).
}
\tag{C1zB2C6t.48}
\]

und wegen `r_T!=0` eventual auch

\[
\boxed{
q_{r,T}>0
\qquad(T\ge T_0).
}
\tag{C1zB2C6t.49}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,eventual\text{-}nonzero\text{-}first\text{-}channel}
+
\checkmark[M]_{\rm pos,R_Tr_T\neq0\text{-}eventually}.
}
\]

---

# 9. Was C6t ausdrücklich noch nicht beweist

Der Befund

\[
\mathcal E_{2,0,T}(r_T)>0
\]

ist qualitativ, nicht relativ asymptotisch.

Ein echter Sprung von fester Höhe liefert ohne quantitative Kontrolle des Abstands zu den nächsten Breakpoints noch keine terminaluniforme untere Schranke für das `L^2`-Integral. Selbst eine absolute Schranke

\[
\mathcal E_{2,0,T}(r_T)\ge c_T>0
\]

würde für `q_{r,T}` erst dann genügen, wenn `c_T` mit einer **oberen** Schranke für `||r_T||^2` verglichen wird.

Daher ist die Schlussfolgerung

\[
\boxed{
\mathcal E_{2,0,T}(r_T)>0
\not\Rightarrow
q_{r,T}\not\to0.
}
\tag{C1zB2C6t.50}
\]

verbindlich.

C6q liefert zwar

\[
\|r_T\|^2\gtrsim e^{-4T},
\]

aber dies ist eine **Untergrenze** des Nenners und hilft für eine untere Quotientenschranke nicht.

Ebenso darf aus dem festen Sprung `j_0` nicht ohne Breakpoint-Isolation behauptet werden, dass die erste Kanalenergie eine feste positive Konstante besitzt.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,nonzero\text{-}channel\not\Rightarrow q_r\not\to0}.
}
\]

---

# 10. Einordnung gegenüber der C6t-Vorüberlegung

Die Vorüberlegung fragte, ob

\[
\Phi_{2,0,T}[h_T](u)
\approx
\lambda_T\Phi_{2,0,T}[a_T](u)
\]

punktweise auf dem gesamten ersten Martingalbereich gelten könnte.

C6t zeigt, dass dies **nicht** überall der Fall sein kann.

Denn am arithmetisch selektierten inneren Punkt `u_{q_T}(T)` besitzt die Differenz

\[
H_{2,T}h_T-\lambda_TH_{2,T}a_T
=H_{2,T}r_T
\]

einen echten Sprung, während der Restmodebeitrag dort sprungfrei ist.

Somit ist eine exakte oder fast-überall identische kanalweise Locking-Beziehung ausgeschlossen.

Die richtige verbleibende quantitative Frage lautet nicht mehr

\[
\text{„Ist der erste Kanal identisch null?“}
\]

sondern

\[
\boxed{
\text{„Wie groß ist die L2-Energie dieses nachweislich nichtverschwindenden Kanals relativ zu }\|r_T\|^2\text{?“}
}
\tag{C1zB2C6t.51}
\]

Das ist eine wesentlich schärfere Front.

---

# 11. Konsequenzen für q_r und Alignment

C6p gab

\[
s_{r,T}
\le
\frac{q_{r,T}}{1+q_{r,T}}.
\]

C6t zeigt jetzt, dass `q_{r,T}` eventual nicht durch exaktes Verschwinden des Restresiduums klein werden kann:

\[
R_Tr_T\ne0.
\]

Aber eine asymptotische Smallness

\[
q_{r,T}\to0
\]

bleibt logisch möglich, falls die nachgewiesene erste Kanalenergie gegenüber `||r_T||^2` verschwindet.

Daher ändert C6t den Status des q_r-Pfades von

\[
\text{„möglicherweise exakt restfrei“}
\]

zu

\[
\boxed{
\text{„arithmetisch erzwungen restbeladen, aber relative Ladung noch offen“.}
}
\]

Für das zweite Alignment-Skalarproblem

\[
a_{R,T}^{(2)}\ne0
\]

ist dies ein positiver Strukturbeitrag, aber noch kein Abschluss.

---

# 12. Nächster atomarer Schritt

Der nächste sinnvolle Knoten ist nicht sofort der zweite Primekanal `p=3`.

C6t hat bereits bewiesen, dass `p=2,a=0` qualitativ nichtverschwindend ist. Die knappste offene Frage ist jetzt die **relative Skala desselben Kanals**.

Vorgeschlagener Knoten:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6u]
\quad
\text{Two-Adic First-Channel Isolation and Relative Energy Scale}.
}
\]

Arbeitsauftrag:

1. konstruiere um `u_{q_T}(T)` einen expliziten breakpointfreien oder BV-kontrollierten Radius `rho_T` für `H_{2,T}r_T`;
2. leite aus dem festen Sprung `j_0` eine quantitative untere Schranke
   \[
   \mathcal E_{2,0,T}(r_T)\gtrsim j_0^2\rho_T
   \]
   ab;
3. suche parallel eine P11-spezifische obere Schranke für `||r_T||^2` auf derselben Skala;
4. entscheide erst dann, ob der erste Kanal `q_{r,T}\to0` blockiert oder nur eine verschwindende positive Restladung liefert.

Bis dahin bleibt

\[
?[O]_{q_r\text{-}asymptotic}
\]

offen.

---

# 13. Status-Firewall

C6t beweist **nicht**:

- `q_{r,T}` besitzt eine positive terminaluniforme Untergrenze;
- `q_{r,T}` konvergiert nicht gegen null;
- `s_{r,T}` ist von null getrennt;
- `beta_{R,T}>sqrt(s_{b,T}s_{r,T})`;
- `a_{R,T}^{(2)}!=0`;
- starke Konvergenz der odd terminal gauges;
- irgendeine Aussage über RH.

C6t beweist exakt:

\[
\boxed{
\text{Der flachste }(p,a)=(2,0)\text{-Martingalkanal des Krylov-Residuals ist eventual nicht null.}
}
\]

Die gesamte No-Go-Persistenz bleibt erhalten.

---

# 14. Kurzfazit

C6s schrieb den Restzähler als Summe positiver Martingalquadrate. C6t identifiziert den ersten dieser Quadrate mit dem `2`-reinen Hubfilter und nutzt dessen exakte Sprungtransportlattice.

Die arithmetische Kernidee ist ein Drei-Prim-Selektor:

\[
q_T\in\{3,5,7\},
\]

für den die gesamte Lattice

\[
\{T-\tfrac12\log q_T\pm k\tfrac12\log2:k\ge1\}
\]

frei von prime-puren Restbreakpoints ist.

Auf derselben Lattice erzwingt die Hubseite dagegen die direkten Prime-Power-Paare

\[
\{2^k,q_T\}
\]

mit gleichgerichtetem Hauptsprung; terminale Gegenkollisionen sind wegen der Hubgewichte verschwindend.

Somit

\[
\boxed{
\operatorname{Jump}_{u_{q_T}(T)}H_{2,T}r_T\ne0
}
\]

für alle hinreichend großen `T`, und daher

\[
\boxed{
\mathcal E_{2,0,T}(r_T)>0,
\qquad
R_Tr_T\ne0.
}
\]

Die q_r-Front ist damit qualitativ enger geworden: Nicht mehr die Existenz von Restladung ist offen, sondern nur noch ihre **relative terminale Skala**.
