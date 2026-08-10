# P11-C1z-B2-C6x — Expandierendes Prime-Martingalframe und residualspezifische Massenverteilung

**Datum:** 2026-08-10  
**Programm:** P11 / C1z / B2 / C6  
**Modus:** `PASS-A ACTIVE`  
**Vorgänger:** C6w — `MixedPrimeFirstChannel_FrameTest_ResidualSpectralAvoidance`  
**Scope:** genau ein atomarer Auditknoten; kein SYN, kein Seal, kein `papers/P11`.

---

## 0. Auditstatus

\[
\boxed{
\begin{aligned}
[P11\text{-}C1z\text{-}B2\text{-}C6x]
&\quad \checkmark[K/M]_{\rm part}\\
&+\checkmark[M]_{\rm corr,active\text{-}prime\text{-}cutoff\;p\le e^{2T}}\\
&+\checkmark[M]_{\rm neg,high\text{-}frequency\text{-}window\text{-}resolution\text{-}obstruction}\\
&+\checkmark[M]_{\rm pos,uniform\text{-}martingale\text{-}boundary\text{-}tail\text{-}summability}\\
&+\checkmark[M]_{\rm neg,full\text{-}active\text{-}first\text{-}prime\text{-}ambient\text{-}coercivity}\\
&+\checkmark[M]_{\rm neg,full\text{-}active\text{-}prime\text{-}depth\text{-}ambient\text{-}coercivity}\\
&+\checkmark[M]_{\rm pos,purely\text{-}ambient\text{-}frame\text{-}route\text{-}closed}\\
&+?[O]_{\rm residual\text{-}specific\;spectral\;avoidance}\\
&+?[O]_{\rm q_{r,T}\;asymptotic}\\
&+?[O]_{\rm a_{R,T}^{(2)}\neq0}.
\end{aligned}
}
\]

**Kernurteil.** C6w ließ als ambiente Möglichkeit eine mit `T` wachsende mixed-prime / prime-depth Familie offen. C6x testet diese Route bis zur maximalen kanonischen Familie

\[
\mathcal I_T
=
\{(p,a):\Omega_{p,a,T}\neq\varnothing\},
\]

für die C6s exakt

\[
\|R_Tf\|^2
=
\sum_{(p,a)\in\mathcal I_T}\mathcal E_{p,a,T}(f)
\]

gibt.

Das Ergebnis ist negativ auf **ambienter** Ebene:

\[
\boxed{
\inf_{\substack{f\perp1_T\\f\neq0}}
\frac{\|R_Tf\|^2}{\|f\|^2}
\lesssim \frac1T
\longrightarrow0.
}
\tag{C1zB2C6x.1}
\]

Damit scheitert nicht nur jede feste endliche Prime-/Tiefenfamilie, sondern auch die **volle mit `T` expandierende aktive Martingalfamilie** als uniforme ambiente Koerzivitätsquelle.

Der einzige verbleibende zulässige positive Mechanismustyp ist daher residualspezifisch: Man muss neue Struktur des konkreten

\[
r_T=h_T-\lambda_TA_T1_T
\]

verwenden, die seine Massekonzentration auf den konstruierten gemeinsamen Quasi-Nullmoden quantitativ ausschließt.

C6x beweist ausdrücklich **nicht**, dass eine solche residualspezifische Untergrenze falsch ist.

---

# 1. Verbindliche Eingaben aus C6s und C6w

C6s definiert

\[
\Omega_{p,a,T}
=
\left\{
|u|\le T-\frac{a+1}{2}\log p
\right\}
\tag{C1zB2C6x.2}
\]

bis auf maßtheoretisch irrelevante Randpunkte, sofern die rechte Seite nicht leer ist.

Der skalare Martingaltail ist

\[
\boxed{
\Phi_{p,a,T}[f](u)
:=
\sum_{k\ge a+1}p^{-3k/4}(K_{k\log p}f)(u).
}
\tag{C1zB2C6x.3}
\]

Die exakte Martingalquadrat-Faktorisierung lautet

\[
\boxed{
\|R_Tf\|^2
=
\sum_p
(\log p)(p-1)
\sum_{a\ge0}p^a
\int_{\Omega_{p,a,T}}
|\Phi_{p,a,T}[f](u)|^2\,du.
}
\tag{C1zB2C6x.4}
\]

Alle Summanden sind nichtnegativ.

Für das konkrete Residuum bleibt

\[
\boxed{
q_{r,T}
=
\frac{\|R_Tr_T\|^2}{\|r_T\|^2}.
}
\tag{C1zB2C6x.5}
\]

Wir verwenden weiterhin nur

\[
\boxed{\langle r_T,1_T\rangle=0}
\tag{C1zB2C6x.6}
\]

als exakte Residualorthogonalität und insbesondere **nicht** eine unbewiesene Asymptotik

\[
\lambda_T\asymp Te^T.
\]

C6w hat für jede feste endliche Prime-/Tiefenfamilie gemeinsame ambiente Quasi-Nullmoden konstruiert. Offen blieb dort, ob das Wachstum der beobachteten Familie mit `T` diesen Mechanismus zerstört.

---

# 2. Erste Korrektur: der volle aktive Prime-Cutoff ist `e^{2T}`, nicht `e^T`

Für den ersten Kanal `a=0` ist

\[
\Omega_{p,0,T}
=
\left\{
|u|\le T-\frac12\log p
\right\}.
\]

Dieser Kanal ist genau dann von positivem Maß, wenn

\[
T-\frac12\log p>0.
\]

Also

\[
\boxed{
\log p<2T
\quad\Longleftrightarrow\quad
p<e^{2T}.
}
\tag{C1zB2C6x.7}
\]

Am Gleichheitsrand ist die Domain nur maßnull und energetisch irrelevant.

Daher ist die natürliche volle aktive Primmenge

\[
\boxed{
\mathcal P_T
:=
\{p\text{ prim}:p<e^{2T}\}.
}
\tag{C1zB2C6x.8}
\]

Die in der C6x-Vorüberlegung genannte grobe Schranke `p\le e^T` ist also um einen Faktor `2` im Exponenten zu klein. Für die qualitative Frage ist das unerheblich, für einen Auditknoten muss die Aktivitätsbedingung aber exakt bleiben.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,active\text{-}prime\text{-}cutoff\;p<e^{2T}}.
}
\tag{C1zB2C6x.9}
\]

---

# 3. Zweite Korrektur: hohe Frequenz wird durch das endliche Fenster nicht verboten

Die C6x-Vorüberlegung enthielt die Hoffnung, die simultane diophantische Approximation könne für eine wachsende Primfamilie so große Frequenzen erzwingen, dass sie auf einem Fenster der Länge `2T` nicht mehr als relevante Quasimoden auftreten.

Diese Hoffnung ist falsch.

Für jede Frequenz `\xi>0` setze

\[
\boxed{
f_{T,\xi}(u):=1_{[-T,T]}(u)\sin(\xi u).}
\tag{C1zB2C6x.10}
\]

Die Funktion ist ungerade, daher exakt

\[
\boxed{
\langle f_{T,\xi},1_T\rangle=0.
}
\tag{C1zB2C6x.11}
\]

Außerdem

\[
\begin{aligned}
\|f_{T,\xi}\|_2^2
&=
\int_{-T}^{T}\sin^2(\xi u)\,du\\
&=
T-\frac{\sin(2\xi T)}{2\xi}.
\end{aligned}
\tag{C1zB2C6x.12}
\]

Für `\xi\ge1` gilt damit

\[
\boxed{
T-\frac12
\le
\|f_{T,\xi}\|_2^2
\le
T+\frac12.
}
\tag{C1zB2C6x.13}
\]

Insbesondere wird die Norm bei `\xi\to\infty` **nicht klein**. Hohe Frequenz bedeutet lediglich kurze Wellenlänge, nicht verschwindende `L^2`-Masse.

Es gibt im aktuellen ambienten Raum keine Bandlimit-Hypothese

\[
|\xi|\lesssim T
\]

oder ähnliche obere Frequenzbeschränkung.

Daher kann die enorme Nenner-/Frequenzkostenfunktion aus simultaner Dirichlet-Approximation für sich allein keine Frame-Untergrenze erzeugen.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,high\text{-}frequency\text{-}window\text{-}resolution\text{-}obstruction}.
}
\tag{C1zB2C6x.14}
\]

---

# 4. Vollraumwinkel und simultane Approximation der gesamten aktiven Primmenge

Setze für jede Primzahl

\[
s_p:=\log p,
\qquad
r_p:=p^{-3/4},
\qquad
\theta_p(\xi):=\frac{\xi\log p}{2}.
\tag{C1zB2C6x.15}
\]

Wir wählen wie in C6w die 2-adisch exakt resonanten Frequenzen

\[
\boxed{
\xi_n:=\frac{2\pi n}{\log2},
\qquad n\in\mathbb N.
}
\tag{C1zB2C6x.16}
\]

Dann

\[
\theta_2(\xi_n)=\pi n
\]

und für jede Primzahl `p`

\[
\theta_p(\xi_n)
=
\pi n\alpha_p,
\qquad
\alpha_p:=\frac{\log p}{\log2}.
\tag{C1zB2C6x.17}
\]

Fixiere nun **ein T**. Die aktive Primmenge `\mathcal P_T` ist endlich.

Sei

\[
d_T:=|\mathcal P_T|-1
\]

und betrachte den endlichen Vektor

\[
(\alpha_p)_{p\in\mathcal P_T\setminus\{2\}}.
\]

Die simultane Dirichlet-Approximation liefert zu jedem `Q\ge2` ein

\[
1\le n\le Q^{d_T}
\]

mit

\[
\boxed{
\|n\alpha_p\|_{\mathbb R/\mathbb Z}
\le\frac1Q
\qquad
\forall p\in\mathcal P_T\setminus\{2\}.
}
\tag{C1zB2C6x.18}
\]

Für `p=2` gilt die Relation exakt.

Damit erhält man für alle aktiven Primzahlen gleichzeitig

\[
\boxed{
d_p(\xi_n)
:=
\operatorname{dist}(\theta_p(\xi_n),\pi\mathbb Z)
\le\frac{\pi}{Q}.}
\tag{C1zB2C6x.19}
\]

Der entscheidende Punkt ist:

> Auch wenn `d_T` riesig ist und `n\le Q^{d_T}` astronomisch groß wird, bleibt `f_{T,\xi_n}` ein völlig zulässiger mittelwertfreier `L^2`-Vektor mit Norm `\asymp\sqrt T`.

Die diophantischen **Kosten in Frequenz** sind ohne zusätzliche Bandbegrenzung kein positiver Mechanismus.

---

# 5. Der kanalweise Bulk-Term für beliebige Martingaltiefe

Fixiere `(p,a)` und schreibe kurz

\[
s:=s_p=\log p,
\qquad
r:=r_p=p^{-3/4},
\qquad
\theta:=\theta_p(\xi).
\]

Für die globale Sinusfunktion gilt formal

\[
D_{ks}\sin(\xi u)
=
2\cos(\xi u)\sin(k\theta),
\tag{C1zB2C6x.20}
\]

bis auf ein irrelevantes Vorzeichen je nach Konvention von `K_s`.

Auf `\Omega_{p,a,T}` liegen für den **ersten Tailindex** `k=a+1` beide verschobenen Argumente sicher in `[-T,T]`. Denn

\[
|u|\le T-\frac{a+1}{2}s
\]

impliziert

\[
\left|u\pm\frac{a+1}{2}s\right|\le T.
\]

Damit ist gerade der führende Term jedes Martingaltails auf seiner eigenen Kanal-Domain randfrei.

Für den idealen Bulk-Tail definiere

\[
\boxed{
S_{p,a}(\theta)
:=
\sum_{k\ge a+1}r^k\sin(k\theta).
}
\tag{C1zB2C6x.21}
\]

Mit

\[
d:=\operatorname{dist}(\theta,\pi\mathbb Z)
\]

gilt

\[
|\sin(k\theta)|\le k d.
\]

Folglich

\[
|S_{p,a}(\theta)|
\le
d\sum_{k\ge a+1}k r^k.
\tag{C1zB2C6x.22}
\]

Da für `0<r\le2^{-3/4}<1`

\[
\sum_{k\ge a+1}k r^k
=
r^{a+1}
\left(
\frac{a+1}{1-r}
+
\frac{r}{(1-r)^2}
\right),
\]

existiert eine universelle Konstante `C` mit

\[
\boxed{
|S_{p,a}(\theta)|
\le
C(a+1)r^{a+1}d.
}
\tag{C1zB2C6x.23}
\]

Der ideale Bulkanteil besitzt daher auf `\Omega_{p,a,T}` die quadratische Schranke

\[
\boxed{
\|\text{Bulk}_{p,a,T}\|_2^2
\le
C T (a+1)^2 p^{-3(a+1)/2}d_p(\xi)^2.
}
\tag{C1zB2C6x.24}
\]

---

# 6. Randgeometrie des Tailterms

Jetzt kommt der Punkt, den die reine Vollraumsymbolanalyse nicht sieht.

Für `k>a+1` kann ein verschobenes Argument auf Teilen von `\Omega_{p,a,T}` das Grundfenster `[-T,T]` verlassen.

Definiere den Randfehler des `k`-Terms als Differenz zwischen dem tatsächlichen abgeschnittenen Shift-Differenzterm und der globalen Sinusform aus (C1zB2C6x.20).

Sein Träger innerhalb `\Omega_{p,a,T}` liegt dort, wo mindestens einer der beiden `k`-Shifts das Grundfenster verlässt.

Die relevante Randmenge hat Maß höchstens

\[
\boxed{
|B_{p,a,k,T}|
\le
(k-a-1)\log p.
}
\tag{C1zB2C6x.25}
\]

Falls die innere vollsichtbare Zone bereits leer ist, ist die gesamte Kanal-Domain betroffen; ihre Länge ist dann kleiner als dieselbe rechte Seite, sodass die Schranke weiterhin gilt.

Punktweise ist der Fehler durch eine absolute Konstante beschränkt. Deshalb

\[
\boxed{
\|E_{p,a,k,T}\|_2
\le
C\sqrt{(k-a-1)\log p}.
}
\tag{C1zB2C6x.26}
\]

Der gesamte gewichtete Tail-Randfehler erfüllt somit

\[
\begin{aligned}
\|E_{p,a,T}\|_2
&\le
C\sqrt{\log p}
\sum_{k\ge a+2}
p^{-3k/4}\sqrt{k-a-1}\\
&\le
C\sqrt{\log p}\,p^{-3(a+2)/4}.
\end{aligned}
\tag{C1zB2C6x.27}
\]

Also

\[
\boxed{
\|E_{p,a,T}\|_2^2
\le
C(\log p)p^{-3(a+2)/2}.
}
\tag{C1zB2C6x.28}
\]

Wichtig ist der zusätzliche Faktor gegenüber dem führenden Tailindex: Der Randfehler beginnt erst bei `k=a+2`, weil `k=a+1` auf `\Omega_{p,a,T}` exakt randfrei ist.

---

# 7. Gewichtete Summation über alle Tiefen eines festen Prime

Die Energie des `(p,a)`-Kanals trägt nach C6s das Gewicht

\[
\boxed{
w_{p,a}:=(\log p)(p-1)p^a.}
\tag{C1zB2C6x.29}
\]

Mit `|X+Y|^2\le2|X|^2+2|Y|^2` zerlegen wir Bulk und Rand.

## 7.1 Bulk

Aus (C1zB2C6x.24) folgt

\[
\begin{aligned}
w_{p,a}\|\text{Bulk}_{p,a,T}\|_2^2
&\le
C T(\log p)(p-1)p^a
(a+1)^2p^{-3(a+1)/2}
 d_p(\xi)^2\\
&\le
C T(\log p)
(a+1)^2p^{-(a+1)/2}
 d_p(\xi)^2.
\end{aligned}
\tag{C1zB2C6x.30}
\]

Da

\[
\sum_{a\ge0}(a+1)^2p^{-(a+1)/2}
\le
C p^{-1/2}
\qquad(p\ge2),
\]

erhält man über **alle Tiefen**

\[
\boxed{
\sum_{a\ge0}
 w_{p,a}\|\text{Bulk}_{p,a,T}\|_2^2
\le
C T(\log p)p^{-1/2}d_p(\xi)^2.
}
\tag{C1zB2C6x.31}
\]

Die tatsächlich aktiven Tiefen bilden nur eine endliche Teilmenge, daher ist die unendliche Summe eine zulässige obere Schranke.

## 7.2 Rand

Aus (C1zB2C6x.28) folgt

\[
\begin{aligned}
w_{p,a}\|E_{p,a,T}\|_2^2
&\le
C(\log p)^2(p-1)p^a p^{-3(a+2)/2}\\
&\le
C(\log p)^2p^{-a/2-2}.
\end{aligned}
\tag{C1zB2C6x.32}
\]

Daher

\[
\boxed{
\sum_{a\ge0}
w_{p,a}\|E_{p,a,T}\|_2^2
\le
C(\log p)^2p^{-2}.
}
\tag{C1zB2C6x.33}
\]

Dies ist der entscheidende Summabilitätsgewinn.

---

# 8. Globale Rand-Tail-Summabilität über alle Primzahlen

Nun summiere (C1zB2C6x.33) über alle Primzahlen.

Wegen

\[
\sum_{p}
\frac{(\log p)^2}{p^2}
\le
\sum_{n\ge2}
\frac{(\log n)^2}{n^2}
<\infty
\]

gibt es eine absolute Konstante `C_{\rm bd}` mit

\[
\boxed{
\sum_p\sum_{a\ge0}
 w_{p,a}\|E_{p,a,T}\|_2^2
\le
C_{\rm bd}
}
\tag{C1zB2C6x.34}
\]

uniform in `T` und `\xi`.

Das ist der Schlüsselfund von C6x:

> Das Anwachsen der Zahl der Prim- und Tiefenkanäle lässt die Randfehler nicht unkontrolliert anwachsen. Die geometrischen Faktoren `p^{-3k/4}` und der Umstand, dass der erste Tailterm auf seiner eigenen Domain randfrei ist, machen die gesamte Rand-Tail-Familie summierbar.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,uniform\text{-}full\text{-}martingale\text{-}boundary\text{-}tail\text{-}summability}.
}
\tag{C1zB2C6x.35}
\]

---

# 9. Globale Energieabschätzung für die volle aktive Martingalfamilie

Kombiniert man Bulk und Rand, erhält man für die Sinusfunktion `f_{T,\xi}`

\[
\boxed{
\|R_Tf_{T,\xi}\|^2
\le
C T
\sum_{p\in\mathcal P_T}
(\log p)p^{-1/2}d_p(\xi)^2
+
C_{\rm bd}.
}
\tag{C1zB2C6x.36}
\]

Definiere die endliche Gewichtssumme

\[
\boxed{
W_T
:=
\sum_{p\in\mathcal P_T}
(\log p)p^{-1/2}.
}
\tag{C1zB2C6x.37}
\]

Es ist keine Primzahlsatz-Asymptotik nötig. Elementar genügt

\[
W_T
\le
\sum_{2\le n<e^{2T}}
\frac{\log n}{\sqrt n}
<\infty.
\tag{C1zB2C6x.38}
\]

Mit der simultanen Approximation (C1zB2C6x.19) folgt

\[
\boxed{
\|R_Tf_{T,\xi_n}\|^2
\le
C\pi^2T\frac{W_T}{Q^2}
+
C_{\rm bd}.
}
\tag{C1zB2C6x.39}
\]

Da `Q` für jedes feste `T` beliebig groß gewählt werden darf, wähle beispielsweise

\[
\boxed{
Q_T^2
\ge
T W_T.
}
\tag{C1zB2C6x.40}
\]

Dann

\[
\boxed{
\|R_Tf_{T,\xi_T}\|^2
\le
C_0
}
\tag{C1zB2C6x.41}
\]

mit einer von `T` unabhängigen Konstante `C_0`.

Gleichzeitig gilt aus (C1zB2C6x.13)

\[
\boxed{
\|f_{T,\xi_T}\|^2
\ge T-\frac12.
}
\tag{C1zB2C6x.42}
\]

Daher

\[
\boxed{
\frac{\|R_Tf_{T,\xi_T}\|^2}
{\|f_{T,\xi_T}\|^2}
\le
\frac{C_0}{T-1/2}
\longrightarrow0.
}
\tag{C1zB2C6x.43}
\]

Dies beweist (C1zB2C6x.1).

---

# 10. Satz C6x — Full-Active-Martingale Ambient No-Go

Wir fassen den vorigen Abschnitt als eigenständige Audit-Aussage zusammen.

## Satz

Für die C6s-Martingalquadratstruktur auf `[-T,T]` existiert eine Folge mittelwertfreier Vektoren

\[
f_T\perp1_T,
\qquad
\|f_T\|^2\asymp T,
\]

so dass

\[
\boxed{
\|R_Tf_T\|^2=O(1).
}
\tag{C1zB2C6x.44}
\]

Insbesondere

\[
\boxed{
\inf_{\substack{f\perp1_T\\f\neq0}}
\frac{\|R_Tf\|^2}{\|f\|^2}
\to0.
}
\tag{C1zB2C6x.45}
\]

Somit gibt es keine Konstante `c>0`, unabhängig von `T`, mit

\[
\boxed{
\|R_Tf\|^2
\ge
c\|f\|^2
\qquad
\forall f\perp1_T.
}
\tag{C1zB2C6x.46}
\]

## Beweismechanismus

Der Satz verwendet genau drei Zutaten:

1. Für jedes feste `T` ist die volle aktive Primmenge endlich, also simultan diophantisch beliebig gut approximierbar.
2. Es gibt keine obere Frequenzbeschränkung im ambienten `L^2`-Raum; die Frequenzkosten der Approximation zerstören die Norm der Sinusmode nicht.
3. Die Randfehler aller höheren Martingaltails sind nach Gewichtung über sämtliche `p,a` uniform summierbar.

Kein Primzahlsatz und keine RH-nahe Aussage wird benötigt.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,full\text{-}active\text{-}prime\text{-}depth\text{-}ambient\text{-}coercivity}.
}
\tag{C1zB2C6x.47}
\]

---

# 11. Das Resultat enthält den First-Prime-Test als Spezialfall

Da alle Kanalenergien nichtnegativ sind, gilt insbesondere

\[
\sum_{p\in\mathcal P_T}
\mathcal E_{p,0,T}(f_T)
\le
\|R_Tf_T\|^2.
\]

Daher folgt aus (C1zB2C6x.44) sofort

\[
\boxed{
\frac{
\sum_{p\in\mathcal P_T}
\mathcal E_{p,0,T}(f_T)
}{\|f_T\|^2}
\longrightarrow0.
}
\tag{C1zB2C6x.48}
\]

Also scheitert bereits die **volle expandierende erste-Prime-Familie** ambient.

C6x ist damit stärker als ein Test eines speziellen Cutoffs `P_T\sim T` oder `P_T\sim e^{\alpha T}`: Selbst die maximal aktive erste-Prime-Familie bis zum exakten Cutoff `p<e^{2T}` liefert keine uniforme ambiente Frame-Untergrenze.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,full\text{-}active\text{-}first\text{-}prime\text{-}ambient\text{-}coercivity}.
}
\tag{C1zB2C6x.49}
\]

---

# 12. Was mit den „diophantischen Kosten“ tatsächlich passiert

Die Vorüberlegung war richtig darin, dass die simultane Approximation bei wachsender Primanzahl extrem teuer wird.

Bei

\[
d_T=|\mathcal P_T|-1
\]

liefert die elementare Dirichlet-Schranke nur einen Nenner

\[
n\le Q^{d_T}.
\]

Für große `T` kann das astronomisch sein.

Aber die Folgerung

\[
\text{„astronomische Frequenz“}
\Longrightarrow
\text{„kein endliches-Fenster-Quasimodus“}
\]

ist falsch.

Denn

\[
\|1_{[-T,T]}\sin(\xi u)\|_2^2
=T+O(\xi^{-1})
\]

wird bei wachsender `\xi` sogar **stabiler** gegen den Oszillationsterm.

Die diophantische Kostenabschätzung könnte erst dann positiv relevant werden, wenn ein zusätzlicher Satz eine Frequenzobergrenze oder spektrale Konzentration des konkreten Residuals erzwingt, etwa schematisch

\[
\widehat r_T(\xi)\approx0
\qquad
(|\xi|>\Xi_T)
\]

oder eine quantitativ hinreichende Tail-Schranke.

Eine solche Aussage ist derzeit nicht vorhanden.

---

# 13. Konsequenz: die rein ambiente Frame-Route ist geschlossen

C6w ließ die Dichotomie

\[
\text{wachsende Primfamilie}
\quad\text{oder}\quad
\text{residualspezifische Spektralvermeidung}
\]

offen.

C6x verschärft sie.

Da selbst die volle aktive Prime-/Tiefenfamilie keine uniforme ambiente Unterframe-Ungleichung besitzt, kann **Wachstum allein** den Beweis nicht liefern.

Die korrekte neue Aussage lautet

\[
\boxed{
\begin{minipage}{0.88\textwidth}
Jede erfolgreiche quantitative Untergrenze für den konkreten Restquotienten muss residualspezifische Information verwenden. Eine wachsende Prim- oder Tiefenfamilie kann dabei weiterhin Teil des Mechanismus sein, aber ihre bloße ambiente Frame-Geometrie genügt nicht — nicht einmal für die volle aktive Martingalfamilie.
\end{minipage}
}
\tag{C1zB2C6x.50}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,purely\text{-}ambient\text{-}frame\text{-}route\text{-}closed}.
}
\tag{C1zB2C6x.51}
\]

---

# 14. Was C6x für das konkrete Residuum nicht sagt

Der konstruierte Quasimodus `f_T` ist ein ambienter Testvektor.

Er ist **nicht** das konkrete

\[
r_T=h_T-\lambda_TA_T1_T.
\]

Daher folgt aus C6x nicht

\[
\frac{\|R_Tr_T\|^2}{\|r_T\|^2}\to0.
\]

Ebenso folgt nicht, dass `r_T` seine Masse tatsächlich bei den simultanen diophantischen Quasi-Nullfrequenzen konzentriert.

Es bleibt möglich, dass seine explizite arithmetische Konstruktion eine quantitative Spektralvermeidung erzwingt.

Die jetzt notwendige positive Aussage muss ungefähr einen der folgenden Typen besitzen:

### Typ A — Frequenz-Tail-Kontrolle

Für eine geeignete Fourier-/Fensterdarstellung

\[
\int_{|\xi|>\Xi_T}
|\widehat r_T(\xi)|^2\,d\xi
\le
(1-\eta)\|r_T\|^2
\]

mit hinreichend kleinem `\Xi_T` und `\eta>0`.

### Typ B — Quasi-Nullmengen-Vermeidung

Für die schlechte Frequenzmenge

\[
\mathfrak B_T(\varepsilon)
:=
\left\{
\xi:
\sum_{p,a}\text{gewichteter Kanalsymbolbetrag}
\le\varepsilon
\right\}
\]

eine Schranke

\[
\int_{\mathfrak B_T(\varepsilon)}
|\widehat r_T(\xi)|^2\,d\xi
\le
(1-\eta)\|r_T\|^2.
\]

### Typ C — direkte arithmetische Kanalmasse

Ohne Fourierumweg ein Beweis

\[
\sum_{p,a}\mathcal E_{p,a,T}(r_T)
\ge
c\|r_T\|^2
\]

aus der expliziten Breakpoint-/Koeffizientenstruktur von `r_T`.

Keine dieser Aussagen ist in C6x bewiesen.

---

# 15. Konsequenz für `q_{r,T}`

Die exakte Identität bleibt

\[
q_{r,T}
=
\frac{\sum_{p,a}\mathcal E_{p,a,T}(r_T)}{\|r_T\|^2}.
\]

C6x beweist einen ambienten No-Go, keine Asymptotik dieses speziellen Quotienten.

Insbesondere sind weiterhin beide Aussagen offen:

\[
q_{r,T}\to0,
\]

und

\[
q_{r,T}\not\to0.
\]

Die neue Firewall ist lediglich:

\[
\boxed{
q_{r,T}\not\to0
\text{ kann nicht aus einer uniformen ambienten Unterframe-Ungleichung für }R_T
\text{ folgen, weil eine solche falsch ist.}
}
\tag{C1zB2C6x.52}
\]

---

# 16. Konsequenz für `a_{R,T}^{(2)}`

Das übergeordnete P11-C6-Ziel

\[
a_{R,T}^{(2)}\neq0
\]

beziehungsweise die echte 2×2-Invertibilitätsfrage bleibt offen.

C6x liefert weder einen Beweis noch einen Gegenbeweis dafür.

Es schließt nur die Route

\[
\boxed{
\text{uniforme ambiente Coercivity des vollständigen Restoperators}
\Longrightarrow
\text{Rest-Nichtverschwindung}
}
\]

als verfügbare Beweisquelle, weil die Prämisse falsch ist.

Damit muss die verbleibende Nichtverschwindungsinformation aus der speziellen Lage des konkreten Residualvektors im ambienten Raum kommen.

---

# 17. Gegenprüfer-Checkliste C6x

## Test 1 — Aktivitätscutoff

Ist `\Omega_{p,0,T}` nichtleer genau für `\log p\le2T`?

**Ja.** Aus C6s folgt unmittelbar

\[
\Omega_{p,0,T}
=\{|u|\le T-\tfrac12\log p\}.
\]

Der energierelevante offene Cutoff ist `p<e^{2T}`.

## Test 2 — verschwinden hochfrequente Sinusmoden im Fenster normmäßig?

**Nein.**

\[
\|1_{[-T,T]}\sin(\xi u)\|^2
=T+O(1/\xi).
\]

Es gibt keine aktuelle Bandlimit-Hypothese.

## Test 3 — kann man alle aktiven Primwinkel bei festem `T` simultan approximieren?

**Ja.** Die Menge ist endlich. Simultane Dirichlet-Approximation gilt unabhängig davon, wie groß ihre Dimension ist.

## Test 4 — werden die dafür nötigen Frequenzen sehr groß?

**Ja, potenziell extrem groß.** Das ist aber ohne Frequenzobergrenze kein Hindernis.

## Test 5 — explodieren die Randfehler beim Summieren über alle aktiven Prime-/Tiefenkanäle?

**Nein.** Der erste Tailterm `k=a+1` ist auf `\Omega_{p,a,T}` randfrei. Der Rand beginnt erst bei `k=a+2`, und nach Gewichtung erhält man

\[
\sum_{p,a}\text{Randenergie}_{p,a}
\lesssim
\sum_p\frac{(\log p)^2}{p^2}<\infty.
\]

## Test 6 — bleibt deshalb die volle aktive Restenergie auf geeigneten Quasimoden `O(1)`?

**Ja.** Wähle die simultane Approximationsgüte abhängig von `W_T`; dann ist der Bulk ebenfalls `O(1)` und der Rand uniform `O(1)`.

## Test 7 — folgt daraus etwas über das konkrete `r_T`?

**Nein.** Nur die uniforme ambiente Frame-Route ist ausgeschlossen. Residualspezifische Spektralvermeidung bleibt offen.

---

# 18. Persistente neue Firewalls aus C6x

## C6x-A — active-cutoff firewall

\[
\boxed{
\Omega_{p,0,T}\neq\varnothing
\Longleftrightarrow
p\lesssim e^{2T}
}
\]

mit exaktem energierelevantem Cutoff `p<e^{2T}`.

## C6x-B — frequency-cost firewall

\[
\boxed{
\text{Große simultane Dirichlet-Frequenz}
\not\Rightarrow
\text{kleine Fenster-}L^2\text{-Norm}.
}
\]

## C6x-C — expanding-family firewall

\[
\boxed{
\text{Selbst die volle aktive erste-Prime-Familie ist ambient nicht uniform koerziv.}
}
\]

## C6x-D — full-martingale firewall

\[
\boxed{
\text{Selbst die volle aktive Prime-/Tiefen-Martingalfamilie ist ambient nicht uniform koerziv.}
}
\]

## C6x-E — residual firewall

\[
\boxed{
\text{Der Full-Family Ambient No-Go ist kein No-Go für eine spezielle Untergrenze am konkreten }r_T.
}
\]

## C6x-F — q-firewall

C6x liefert keine Asymptotik von `q_{r,T}`.

---

# 19. Was C6x ausdrücklich nicht beweist

C6x beweist **nicht**:

\[
q_{r,T}\to0,
\]

\[
q_{r,T}\not\to0,
\]

\[
a_{R,T}^{(2)}\neq0,
\]

\[
a_{R,T}^{(2)}=0,
\]

\[
\rho_T^{(2)}\to0,
\]

oder eine Asymptotik für `\lambda_T`.

C6x beweist auch nicht, dass eine wachsende Primfamilie für den **konkreten Residualvektor** nutzlos ist. Sie kann weiterhin Bestandteil eines residualspezifischen Beweises sein. Ausgeschlossen ist nur die Hoffnung, ihr Wachstum erzeuge bereits ambient eine uniforme Frame-Untergrenze.

---

# 20. Nächster atomarer Knoten

Nach C6x ist es nicht mehr sinnvoll, weitere ambiente Subframes zu testen.

Die maximal mögliche ambiente Familie wurde bereits ausgeschöpft und besitzt dennoch Quasimoden.

Der nächste atomare Knoten sollte daher direkt die letzte verbleibende positive Route prüfen:

\[
\boxed{[P11\text{-}C1z\text{-}B2\text{-}C6y]}
\]

mit Arbeitstitel etwa

`ResidualSpectralMass_ArithmeticAvoidanceTest`.

Atomarer Auftrag:

1. schreibe `r_T=h_T-\lambda_TA_T1_T` in einer für Fourier-/Frequenzmassenfragen tatsächlich zulässigen Darstellung;
2. trenne exakt die spektrale Masse von `r_T` von bloßer Sprung-/Breakpoint-Provenienz;
3. prüfe, ob die expliziten Hub- und Restkoeffizienten eine quantitative Obergrenze der Masse in den C6w/C6x-Quasi-Nullregionen liefern;
4. falls keine solche Schranke aus den vorhandenen Daten folgt, formuliere den präzisen residualspezifischen Blocker als C6-Abschlusskriterium statt weitere ambiente Kanäle zu eröffnen;
5. nur eine tatsächlich uniforme relative Untergrenze darf in `q_{r,T}\not\to0` oder in die 2×2-Invertibilitätsfrage eingespeist werden.

Bis dahin bleibt

\[
\boxed{P11=\texttt{PASS-A ACTIVE}.}
\]

Kein SYN, kein Seal, kein `papers/P11`.

---

# 21. Kurzfazit

C6x testet die stärkste noch offene ambiente Hoffnung aus C6w — und schließt sie.

Die volle aktive Primmenge ist bei festem `T` zwar enorm, aber endlich. Deshalb kann man alle Prime-Winkel simultan beliebig nahe an `\pi\mathbb Z` bringen. Die dafür nötige Frequenz kann astronomisch sein; im nicht bandbegrenzten `L^2([-T,T])` ist das kein Hindernis.

Der einzige mögliche Rettungseffekt wären die endlichen-Fenster-Ränder gewesen. Genau dort liefert die Martingalstruktur jedoch einen zusätzlichen geometrischen Gewinn: Der führende Tailterm `k=a+1` ist auf seiner eigenen Domain `\Omega_{p,a,T}` randfrei, und die erst bei `k=a+2` beginnenden Randtails erfüllen nach vollständiger Gewichtung

\[
\sum_{p,a}\text{Randenergie}_{p,a}
\lesssim
\sum_p\frac{(\log p)^2}{p^2}<\infty.
\]

Damit kann man für geeignete simultane Quasi-Nullfrequenzen sogar die **volle** Restenergie `\|R_Tf_T\|^2` uniform beschränkt halten, während

\[
\|f_T\|^2\asymp T.
\]

Folglich

\[
\boxed{
\inf_{f\perp1_T}
\frac{\|R_Tf\|^2}{\|f\|^2}
\to0.
}
\]

Die C6-Mechanik ist damit erneut schärfer lokalisiert:

\[
\boxed{
\text{pure ambient frame route: closed}
}
\]

und als verbleibende positive Aufgabe

\[
\boxed{
\text{residual-specific arithmetic/spectral avoidance for }r_T.
}
\]

P11 bleibt bis zur Entscheidung dieses residualspezifischen C6-Endpunkts `PASS-A ACTIVE`.
