# P11-C1z-B2-C6w — Mixed-Prime-First-Channel-Frame-Test und residualspezifische Spektralvermeidung

**Datum:** 2026-08-10  
**Programm:** P11 / C1z / B2 / C6  
**Modus:** `PASS-A ACTIVE`  
**Vorgänger:** C6v — `RelativeTwoAdicChannelMass_TransportedBreakpointSeparation`  
**Scope:** genau ein atomarer Auditknoten; kein SYN, kein Seal, kein `papers/P11`.

---

## 0. Auditstatus

\[
\boxed{
\begin{aligned}
[P11\text{-}C1z\text{-}B2\text{-}C6w]
&\quad \checkmark[K/M]_{\rm part}\\
&+\checkmark[M]_{\rm pos,no\text{-}common\text{-}exact\text{-}zero\;(2,3)}\\
&+\checkmark[M]_{\rm neg,fixed\;two\text{-}prime\;ambient\;coercivity}\\
&+\checkmark[M]_{\rm neg,fixed\;finite\;prime\;ambient\;coercivity}\\
&+\checkmark[M]_{\rm neg,fixed\;finite\;prime\text{-}depth\;subframe}\\
&+\checkmark[M]_{\rm pos,growing\text{-}family\;or\;residual\text{-}spectral\text{-}avoidance\;necessary}\\
&+?[O]_{\rm expanding\;mixed\text{-}prime\;frame}\\
&+?[O]_{\rm residual\text{-}specific\;spectral\;avoidance}\\
&+?[O]_{\rm q_{r,T}\;asymptotic}\\
&+?[O]_{\rm a_{R,T}^{(2)}\neq0}.
\end{aligned}
}
\]

**Kernurteil.** Der in C6v vorgeschlagene kleinste mixed-prime Test

\[
\mathcal E_{2,0,T}(r_T)+\mathcal E_{3,0,T}(r_T)
\]

ist strukturell sinnvoll, aber als **ambienter uniformer Frame-Mechanismus** nicht ausreichend. Obwohl die beiden Vollraum-Bulksymbole außer bei `\xi=0` keine gemeinsame exakte Nullstelle besitzen, haben sie aufgrund diophantischer Approximation gemeinsame **Quasi-Nullfrequenzen** beliebig hoher Ordnung. Daraus entstehen mittelwertfreie endliche-Fenster-Quasimoden, für die die relative Energie jedes festen endlichen mixed-prime Subframes gegen null geht.

Damit ist die nächste zulässige Alternative scharf eingegrenzt:

1. eine mit `T` wachsende mixed-prime / prime-depth Beobachtungsfamilie; oder
2. ein neuer Satz, der beweist, dass der konkrete Residualvektor `r_T` seine Masse nicht auf solchen gemeinsamen Quasi-Nullmoden konzentrieren kann.

C6w beweist **keine** dieser beiden positiven Alternativen.

---

# 1. Eingaben und persistente Firewalls

Wir übernehmen aus C6s/C6t/C6v nur die bereits geprüften Strukturen.

Für jede Primzahl `p` ist der erste Hubkanal

\[
H_{p,T}
=
\sqrt{\log p}\sum_{k\ge1}p^{-3k/4}K_{k\log p},
\]

mit erster Martingalenergie

\[
\boxed{
\mathcal E_{p,0,T}(f)
=(p-1)\int_{\Omega_{p,0,T}}|H_{p,T}f(u)|^2\,du.
}
\tag{C1zB2C6w.1}
\]

Die volle aktive Martingalfamilie erfüllt exakt

\[
\boxed{
\|R_Tf\|^2
=
\sum_{(p,a)\in\mathcal I_T}\mathcal E_{p,a,T}(f).
}
\tag{C1zB2C6w.2}
\]

Für das Residuum

\[
r_T=h_T-\lambda_TA_T1_T
\]

gilt exakt nur die bereits etablierte Orthogonalität

\[
\boxed{\langle r_T,1_T\rangle=0.}
\tag{C1zB2C6w.3}
\]

Wir verwenden insbesondere **nicht**

\[
\lambda_T\asymp Te^T,
\]

und wir folgern aus keiner gegen null gehenden Untergrenze eine Asymptotik von `q_{r,T}`.

Weiterhin bleibt

\[
\boxed{
q_{r,T}
=
\frac{\|R_Tr_T\|^2}{\|r_T\|^2}
=
\frac{\sum_{p,a}\mathcal E_{p,a,T}(r_T)}{\|r_T\|^2}.
}
\tag{C1zB2C6w.4}
\]

---

# 2. Exakte Vollraum-Bulksymbole der ersten Primkanäle

Setze

\[
r_p:=p^{-3/4},
\qquad
\theta_p(\xi):=\frac{\xi\log p}{2}.
\]

Für den Vollraum-Differenzoperator

\[
D_sf(u):=f(u+s/2)-f(u-s/2)
\]

ist der Fouriermultiplikator

\[
2i\sin(\xi s/2).
\]

Daher besitzt der erste `p`-Hub im Bulk das Symbol

\[
\begin{aligned}
m_p(\xi)
&=
2i\sqrt{\log p}
\sum_{k\ge1}r_p^k\sin(k\theta_p(\xi))\\
&=
\boxed{
2i\sqrt{\log p}
\frac{r_p\sin\theta_p(\xi)}
{1-2r_p\cos\theta_p(\xi)+r_p^2}
}.
\end{aligned}
\tag{C1zB2C6w.5}
\]

Da

\[
1-2r_p\cos\theta+r_p^2
\ge(1-r_p)^2>0,
\]

sind die Nullstellen exakt durch den Sinus bestimmt:

\[
\boxed{
m_p(\xi)=0
\iff
\xi\in\frac{2\pi}{\log p}\mathbb Z.}
\tag{C1zB2C6w.6}
\]

Für `p=2,3` also

\[
\mathcal Z_2=\frac{2\pi}{\log2}\mathbb Z,
\qquad
\mathcal Z_3=\frac{2\pi}{\log3}\mathbb Z.
\]

---

# 3. Positiver Befund: keine gemeinsame nichttriviale exakte Nullstelle für 2 und 3

Angenommen

\[
\xi\ne0,
\qquad
m_2(\xi)=m_3(\xi)=0.
\]

Dann existieren `m,n\in\mathbb Z\setminus\{0\}` mit

\[
\xi=\frac{2\pi m}{\log2}
=\frac{2\pi n}{\log3}.
\]

Somit

\[
\frac{\log3}{\log2}=\frac{n}{m}\in\mathbb Q.
\]

Nach Potenzieren ergäbe dies für geeignete positive ganze Exponenten

\[
3^{|m|}=2^{|n|},
\]

im Widerspruch zur eindeutigen Primfaktorzerlegung.

Also

\[
\boxed{
\mathcal Z_2\cap\mathcal Z_3=\{0\}.
}
\tag{C1zB2C6w.7}
\]

Das bestätigt die C6v-Intuition:

> Der 3-adische Kanal sieht jede **exakte** nichttriviale 2-adische Bulk-Nullmode.

Aber dies ist noch keine quantitative Frame-Aussage.

---

# 4. Die entscheidende Lücke: „keine gemeinsame Nullstelle“ ist nicht „uniform von null getrennt“

Für eine uniforme Zweiprime-Coercivity im Vollraum bräuchte man mindestens eine Symboluntergrenze der Form

\[
\boxed{
|m_2(\xi)|^2+|m_3(\xi)|^2\ge c>0
\qquad(\xi\ne0)
}
\tag{C1zB2C6w.8}
\]

in einem für die mittelwertfreien Vektoren relevanten Sinn.

C6w zeigt nun, dass eine solche Aussage falsch ist.

Setze

\[
\alpha:=\frac{\log3}{\log2}.
\]

Da `\alpha` irrational ist, liefert die elementare Dirichlet-Approximation unendlich viele Paare positiver ganzer Zahlen `(n,m)` mit

\[
\boxed{
|n\alpha-m|\to0.
}
\tag{C1zB2C6w.9}
\]

Sogar die übliche quantitative Form

\[
|n\alpha-m|<\frac1n
\]

tritt für unendlich viele geeignete Nenner auf; für den No-Go genügt bereits die Konvergenz gegen null.

Wähle dazu die exakt 2-adischen Nullfrequenzen

\[
\boxed{
\xi_n:=\frac{2\pi n}{\log2}.
}
\tag{C1zB2C6w.10}
\]

Dann gilt exakt

\[
m_2(\xi_n)=0.
\]

Für den 3-adischen Winkel erhält man

\[
\theta_3(\xi_n)
=
\frac{\xi_n\log3}{2}
=
\pi n\alpha.
\]

Ist `m` die zugehörige ganze Zahl aus (C1zB2C6w.9), so

\[
|\sin\theta_3(\xi_n)|
=
|\sin(\pi(n\alpha-m))|
\le
\pi|n\alpha-m|.
\]

Da der Nenner des Symbols gleichmäßig von null getrennt ist,

\[
|m_3(\xi_n)|
\le
C_3|n\alpha-m|
\to0.
\]

Folglich

\[
\boxed{
\inf_{\xi\ne0}
\left(|m_2(\xi)|^2+|m_3(\xi)|^2\right)=0.
}
\tag{C1zB2C6w.11}
\]

Dies ist der zentrale mixed-prime Symbol-No-Go.

**Wichtig:** Es gibt keine gemeinsame nichttriviale exakte Nullstelle, aber es gibt gemeinsame **Quasi-Nullstellen** beliebig hoher Frequenz.

---

# 5. Endliche-Fenster-Quasimoden für den Zweiprime-Test

Die Vollraum-Symbolaussage muss auf den tatsächlichen endlichen Fensterraum übertragen werden.

Für eine Frequenz `\xi>0` setze

\[
\boxed{
f_{T,\xi}(u):=1_{[-T/2,T/2]}(u)\sin(\xi u).}
\tag{C1zB2C6w.12}
\]

Da die Funktion ungerade und das Intervall symmetrisch ist,

\[
\boxed{\langle f_{T,\xi},1_T\rangle=0.}
\tag{C1zB2C6w.13}
\]

Außerdem

\[
\|f_{T,\xi}\|_2^2
=
\frac T2-rac{\sin(\xi T)}{2\xi}.
\]

Für die hier verwendeten Frequenzen `\xi\ge2\pi/\log2` folgt daher uniform für große `T`

\[
\boxed{\|f_{T,\xi}\|_2^2\asymp T.}
\tag{C1zB2C6w.14}
\]

## 5.1 Randfehler eines einzelnen Shift-Differenzterms

Auf dem Teil des Fensters, auf dem beide Verschiebungen des Sinus innerhalb des Trägerintervalls bleiben, wirkt

\[
D_{k\log p}
\]

exakt mit dem Multiplikator

\[
2i\sin(k\theta_p(\xi)).
\]

Die Abweichung von dieser Bulkform ist auf Randstreifen von Gesamtmaß `O(k\log p)` getragen und punktweise beschränkt. Daher existiert für jedes feste `p` eine Konstante `C_p` mit

\[
\left\|
D_{k\log p}f_{T,\xi}
-
2i\sin(k\theta_p(\xi))f_{T,\xi}
\right\|_2
\le
C_p\sqrt{k},
\tag{C1zB2C6w.15}
\]

wobei die rechte Seite von `T` und `\xi` unabhängig ist.

Mit dem geometrischen Gewicht `r_p^k=p^{-3k/4}` ist

\[
\sum_{k\ge1}r_p^k\sqrt{k}<\infty.
\]

Damit summieren sich die Randfehler zu einer `T`- und `\xi`-unabhängigen Konstante. Die endliche Aktivitätsabschneidung der tatsächlich auf `[-T,T]` vorkommenden `k` erzeugt nur einen geometrischen Tailfehler, der für große `T` ebenfalls gleichmäßig harmlos ist.

Somit

\[
\boxed{
\|H_{p,T}f_{T,\xi}\|_2
\le
|m_p(\xi)|\,\|f_{T,\xi}\|_2+C_p.
}
\tag{C1zB2C6w.16}
\]

Die Einschränkung auf `\Omega_{p,0,T}` kann die Norm nur verkleinern.

Daraus folgt

\[
\frac{\mathcal E_{p,0,T}(f_{T,\xi})}{\|f_{T,\xi}\|_2^2}
\le
C_p'
\left(
|m_p(\xi)|^2
+
\frac{|m_p(\xi)|}{\sqrt T}
+
\frac1T
\right).
\tag{C1zB2C6w.17}
\]

## 5.2 Wahl einer gemeinsamen Quasi-Nullfrequenz

Für jedes große `T` wählen wir einen Dirichlet-Approximanten aus §4 so weit in der Folge, dass

\[
|m_3(\xi_T)|\le T^{-1/2},
\qquad
m_2(\xi_T)=0.
\]

Dann folgt aus (C1zB2C6w.17)

\[
\boxed{
\frac{
\mathcal E_{2,0,T}(f_{T,\xi_T})
+
\mathcal E_{3,0,T}(f_{T,\xi_T})
}{
\|f_{T,\xi_T}\|_2^2
}
\longrightarrow0.
}
\tag{C1zB2C6w.18}
\]

Zusammen mit (C1zB2C6w.13) ist dies ein echter ambienter Zweiprime-No-Go:

\[
\boxed{
\not\exists c>0:\quad
\mathcal E_{2,0,T}(f)+\mathcal E_{3,0,T}(f)
\ge c\|f\|_2^2
\quad
\forall f\perp1_T,
\ \forall T\gg1.
}
\tag{C1zB2C6w.19}
\]

---

# 6. Allgemeiner Satz: jede feste endliche Primfamilie besitzt gemeinsame Quasi-Nullmoden

Der Zweiprime-Befund ist kein Sonderfall von `2` und `3`.

Sei

\[
P=\{p_1,\dots,p_d\}
\]

eine feste endliche Primmenge. Wir wählen `p_1` als Referenz und setzen

\[
\alpha_j:=\frac{\log p_j}{\log p_1}
\qquad(j=2,\dots,d).
\]

Nach dem simultanen Dirichlet-Approximationssatz gilt für jedes `Q\ge1`: Es existiert eine positive ganze Zahl `n` und ganze Zahlen `m_2,\dots,m_d` mit

\[
1\le n\le Q^{d-1}
\]

und

\[
\boxed{
|n\alpha_j-m_j|\le\frac1Q
\qquad(j=2,\dots,d).
}
\tag{C1zB2C6w.20}
\]

Setze

\[
\xi_Q:=\frac{2\pi n}{\log p_1}.
\]

Dann

\[
m_{p_1}(\xi_Q)=0,
\]

und für `j\ge2`

\[
|\sin\theta_{p_j}(\xi_Q)|
\le\frac{\pi}{Q}.
\]

Da für die feste Primmenge alle Symbolnenner uniform positiv sind,

\[
\boxed{
\max_{p\in P}|m_p(\xi_Q)|
\le\frac{C_P}{Q}.
}
\tag{C1zB2C6w.21}
\]

Folglich

\[
\boxed{
\inf_{\xi\ne0}
\sum_{p\in P}|m_p(\xi)|^2=0
\qquad
(P\text{ fest und endlich}).
}
\tag{C1zB2C6w.22}
\]

Mit demselben Fensterargument wie in §5 erhält man für jede feste endliche Primmenge `P` mittelwertfreie Vektoren `f_T` mit

\[
\boxed{
\frac{
\sum_{p\in P}\mathcal E_{p,0,T}(f_T)
}{\|f_T\|_2^2}
\longrightarrow0.
}
\tag{C1zB2C6w.23}
\]

Damit ist nicht nur `(2,0)+(3,0)`, sondern **jede feste endliche Familie erster Primkanäle** als uniforme ambiente Coercivity-Quelle ausgeschlossen.

---

# 7. Auch eine feste endliche Prime-/Tiefenfamilie rettet die ambienten Quasi-Nullmoden nicht

C6v zeigte bereits, dass für einen festen Prime `p` alle Tiefen dieselbe exakte Bulk-Nullstellenlattice teilen. C6w erweitert dies auf jede feste endliche Prime-/Tiefenfamilie.

Für Tiefe `a\ge0` hat der ungewichtete Martingaltail im Bulk die trigonometrische Reihe

\[
\boxed{
\mu_{p,a}(\xi)
:=
2i\sum_{k\ge a+1}p^{-3k/4}\sin(k\theta_p(\xi)).
}
\tag{C1zB2C6w.24}
\]

Die zugehörige Energie trägt nur den festen positiven Faktor

\[
(\log p)(p-1)p^a.
\]

Sei

\[
d_p(\xi):=\operatorname{dist}(\theta_p(\xi),\pi\mathbb Z).
\]

Mit

\[
|\sin(k\theta)|
\le k\,\operatorname{dist}(\theta,\pi\mathbb Z)
\]

folgt

\[
|\mu_{p,a}(\xi)|
\le
2d_p(\xi)
\sum_{k\ge a+1}k p^{-3k/4}.
\tag{C1zB2C6w.25}
\]

Für jede feste Tiefe `a` ist die Summe endlich.

Sei nun

\[
J\subset\{(p,a):p\text{ prim},\ a\ge0\}
\]

eine feste endliche Indexmenge und `P(J)` die dazugehörige endliche Primmenge. Wähle die simultanen Dirichlet-Frequenzen aus §6. Dann gehen für alle `p\in P(J)` die Abstände `d_p(\xi_Q)` simultan gegen null. Daher

\[
\boxed{
\max_{(p,a)\in J}|\mu_{p,a}(\xi_Q)|\to0.
}
\tag{C1zB2C6w.26}
\]

Das Fensterargument lässt sich kanalweise wiederholen; wegen der Endlichkeit von `J` bleiben alle Randkonstanten summierbar. Somit existieren mittelwertfreie `f_T` mit

\[
\boxed{
\frac{
\sum_{(p,a)\in J}\mathcal E_{p,a,T}(f_T)
}{\|f_T\|_2^2}
\longrightarrow0.
}
\tag{C1zB2C6w.27}
\]

**Satz C6w-Finite-Subframe-No-Go.** Für keine feste endliche Prime-/Tiefenindexmenge `J` kann aus der aktuellen Hub-/Martingalstruktur eine uniforme ambiente Unterframe-Ungleichung

\[
\sum_{(p,a)\in J}\mathcal E_{p,a,T}(f)
\ge c\|f\|_2^2
\qquad(f\perp1_T)
\]

mit einem von `T` unabhängigen `c>0` gelten.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,fixed\text{-}finite\text{-}prime\text{-}depth\text{-}ambient\text{-}subframe}.
}
\tag{C1zB2C6w.28}
\]

---

# 8. Was dieser No-Go für den konkreten Residualvektor `r_T` bedeutet — und was nicht

Der No-Go aus §§5–7 ist **ambient**. Er konstruiert zulässige mittelwertfreie Vektoren, die von jedem festen endlichen Subframe asymptotisch schlecht gesehen werden.

Er beweist nicht, dass der konkrete

\[
r_T=h_T-\lambda_TA_T1_T
\]

solche Quasimoden tatsächlich enthält.

Die bisher bewiesenen Eigenschaften von `r_T` reichen aber auch nicht aus, sie auszuschließen.

Insbesondere:

1. `\langle r_T,1_T\rangle=0` schließt nur die konstante Nullmode aus, nicht hochfrequente gemeinsame Quasi-Nullmoden.
2. Der in C6t bewiesene feste lokale 2-adische gefilterte Sprung erzwingt positive lokale Kanalenergie, aber keine positive **relative** Energie gegen `\|r_T\|^2`.
3. Die Stückkonstanz / Sprungstruktur allein ist keine bekannte Spektrallokalisierung, die eine Konzentration nahe den diophantischen Quasi-Nullfrequenzen verhindert.
4. C6u liefert eine obere Normschranke, aber keine spektrale Verteilung der Norm von `r_T`.

Daher ist die residualspezifische Aussage

\[
\boxed{
\mathcal E_{2,0,T}(r_T)+\mathcal E_{3,0,T}(r_T)
\ge c\|r_T\|^2
}
\tag{C1zB2C6w.29}
\]

mit festem `c>0` weiterhin **offen** als vektorspezifische Aussage, kann aber nicht aus einer ambienten Zweiprime-Frame-Ungleichung folgen, weil eine solche ambient falsch ist.

Dasselbe gilt für jedes feste endliche Subframe.

---

# 9. Die neue scharfe Dichotomie

C6w reduziert den verbleibenden Mechanismus auf zwei logisch getrennte Möglichkeiten.

## 9.1 Route A — wachsende mixed-prime Familie

Man wählt eine mit `T` wachsende Indexfamilie

\[
J_T\subseteq\mathcal I_T,
\qquad
|P(J_T)|\to\infty,
\]

und versucht eine Untergrenze

\[
\boxed{
\sum_{(p,a)\in J_T}\mathcal E_{p,a,T}(r_T)
\ge c\|r_T\|^2
}
\tag{C1zB2C6w.30}
\]

zu beweisen.

C6w zeigt nur die **Notwendigkeit eines Wachstums**, falls man eine rein ambiente finite-Subframe-Strategie verfolgt. Es zeigt nicht, wie schnell `J_T` wachsen muss und nicht, dass irgendeine konkrete wachsende Familie bereits genügt.

Die volle aktive Familie

\[
J_T=\mathcal I_T
\]

bleibt der kanonische maximale Kandidat, weil dort exakt

\[
\sum_{(p,a)\in\mathcal I_T}\mathcal E_{p,a,T}(r_T)
=\|R_Tr_T\|^2
\]

gilt.

## 9.2 Route B — residualspezifische Spektralvermeidung

Alternativ könnte man beweisen, dass der spezielle `r_T` quantitativ wenig Fouriermasse in den gemeinsamen Quasi-Nullregionen eines kleinen Subframes trägt.

Schematisch bräuchte man für eine geeignete schlechte Frequenzmenge `\mathfrak B_T` eine Aussage der Form

\[
\boxed{
\int_{\mathfrak B_T}|\widehat r_T(\xi)|^2\,d\xi
\le(1-\eta)\|r_T\|^2
}
\tag{C1zB2C6w.31}
\]

mit `\eta>0` und gleichzeitig einer Symboluntergrenze außerhalb `\mathfrak B_T`.

Eine solche Aussage liegt in den bisherigen C6-Knoten **nicht** vor.

Außerdem muss auf dem tatsächlichen endlichen Intervall präzise festgelegt werden, welche Fourier-/Fensterdarstellung verwendet wird; (C1zB2C6w.31) ist daher nur die Form des benötigten Mechanismus, kein bereits definierter Satz über `r_T`.

---

# 10. Warum die Inkommensurabilität trotzdem nützlich war

Die Inkommensurabilität von

\[
\log2,
\qquad
\log3
\]

ist nicht nutzlos. Sie trennt zwei verschiedene Ebenen:

### Exakte Unsichtbarkeit

Für `\xi\ne0` kann kein Vollraum-Modus gleichzeitig exakt im ersten 2- und 3-Kanal verschwinden.

### Quantitative Beobachtbarkeit

Es existieren dennoch Folgen `\xi_n\to\infty`, auf denen beide Kanäle gleichzeitig beliebig klein werden.

Damit lautet die korrekte Aussage nicht

> „Zwei inkommensurable Primkanäle ergeben ein Frame.“

sondern

> „Zwei inkommensurable Primkanäle entfernen gemeinsame **exakte** nichttriviale Nullmoden, aber nicht gemeinsame **Quasi-Nullmoden**.“

Diese Unterscheidung ist ab C6w persistent.

---

# 11. Konsequenz für die C6v-Frage nach „mindestens p=3“

C6v formulierte korrekt, dass mindestens mixed-prime Information oder ein residualspezifischer Spektralsatz nötig ist.

C6w verschärft diese Aussage:

\[
\boxed{
\begin{minipage}{0.88\textwidth}
Ein einzelner zusätzlicher fester Primkanal reicht als ambienter uniformer Frame-Mechanismus nicht. Tatsächlich reicht keine feste endliche Menge von Primkanälen, und auch keine feste endliche Prime-/Tiefenfamilie. Falls der Beweis über ambiente Observability laufen soll, muss die beobachtete Primfamilie mit `T` wachsen. Ein kleines fixes Subframe kann nur dann noch genügen, wenn eine neue residualspezifische Spektralvermeidung für den konkreten `r_T` bewiesen wird.
\end{minipage}
}
\tag{C1zB2C6w.32}
\]

Das ist stärker als der C6v-Befund, ohne ihn zu überschreiben.

---

# 12. Konsequenz für `q_{r,T}`

Aus C6s gilt exakt

\[
q_{r,T}
=
\frac{\sum_{(p,a)\in\mathcal I_T}\mathcal E_{p,a,T}(r_T)}{\|r_T\|^2}.
\]

C6w beweist **keine** positive uniforme Untergrenze für diesen Quotienten.

Insbesondere folgt weder

\[
q_{r,T}\not\to0
\]

noch

\[
q_{r,T}\to0.
\]

Was C6w ausschließt, ist lediglich die Argumentationsroute

\[
\text{„ein fixes endliches mixed-prime Subframe ist ambient uniform koerziv“}.
\]

Eine wachsende Familie oder eine residualspezifische Aussage kann weiterhin eine positive Untergrenze liefern.

---

# 13. Konsequenz für `a_{R,T}^{(2)}` und die 2×2-Invertibilität

Der übergeordnete P11-C6-Zielmechanismus verlangt weiterhin die echte nichtverschwindende Restinformation, die im bisherigen Strang mit

\[
a_{R,T}^{(2)}\ne0
\]

beziehungsweise der entsprechenden 2×2-Invertibilitätsfrage verbunden ist.

C6w löst diesen Punkt **nicht**.

Es schließt nur eine weitere zu starke Brücke:

\[
\boxed{
\text{keine gemeinsame exakte Nullstelle}
\not\Rightarrow
\text{uniforme mixed-prime Coercivity}.
}
\tag{C1zB2C6w.33}
\]

Daher bleibt

\[
?[O]_{a_{R,T}^{(2)}\neq0}.
\]

---

# 14. Gegenprüfer-Checkliste C6w

## Test 1 — exakte Nullstellen

Sind

\[
\frac{2\pi}{\log2}\mathbb Z
\quad\text{und}\quad
\frac{2\pi}{\log3}\mathbb Z
\]

außer bei null disjunkt?

**Ja.** Eine gemeinsame nichttriviale Nullstelle würde eine rationale Relation zwischen `\log2` und `\log3` und damit `2^a=3^b` erzwingen.

## Test 2 — folgt daraus ein positiver Symbolgap?

**Nein.** Dirichlet-Approximation liefert 2-adische Nullfrequenzen, die beliebig nahe an 3-adischen Nullfrequenzen liegen.

## Test 3 — bleibt der No-Go nur formal im Vollraum?

**Nein.** Die zentral getragenen Sinus-Quasimoden auf `[-T/2,T/2]` haben nur `O(1)`-Randfehler pro festem Primkanal, während ihre Norm quadratisch wie `T` wächst. Dadurch geht der relative Fehler gegen null.

## Test 4 — helfen endlich viele weitere Primzahlen?

**Nein, ambient nicht.** Simultane Dirichlet-Approximation erzeugt gemeinsame Quasi-Nullfrequenzen jeder festen endlichen Primmenge.

## Test 5 — helfen endlich viele zusätzliche Martingaltiefen?

**Nein, ambient nicht.** Für jede feste Tiefe wird ihr Tailsymbol klein, sobald der zugehörige Prime-Winkel nahe `\pi\mathbb Z` liegt. Eine feste endliche Prime-/Tiefenfamilie besitzt deshalb denselben Quasimoden-No-Go.

## Test 6 — ist damit der konkrete Residualvektor erledigt?

**Nein.** Der No-Go betrifft den ambienten Raum. Es bleibt möglich, aber unbewiesen, dass die spezielle arithmetische Form von `r_T` eine Konzentration auf gemeinsame Quasi-Nullfrequenzen quantitativ verhindert.

## Test 7 — was ist jetzt minimal neu nötig?

Entweder

\[
|P(J_T)|\to\infty
\]

für eine wachsende beobachtete Primfamilie, oder ein neuer residualspezifischer Spektralvermeidungssatz.

---

# 15. Persistente Firewalls aus C6w

Ab diesem Knoten dürfen folgende Aussagen nicht still überschrieben werden.

## C6w-A — exact-zero / quasi-zero firewall

\[
\boxed{
\text{Keine gemeinsame exakte mixed-prime Nullstelle}
\not\Rightarrow
\text{positiver uniformer Symbolgap}.
}
\]

## C6w-B — finite-prime firewall

\[
\boxed{
\text{Jede feste endliche Primfamilie besitzt ambiente gemeinsame Quasi-Nullmoden.}
}
\]

## C6w-C — finite-depth firewall

\[
\boxed{
\text{Auch jede feste endliche Prime-/Tiefenfamilie besitzt ambiente Quasi-Nullmoden.}
}
\]

## C6w-D — residual firewall

\[
\boxed{
\text{Der ambiente No-Go ist kein No-Go für eine spezielle Untergrenze am konkreten }r_T.
}
\]

## C6w-E — q-firewall

Aus C6w folgt keine Asymptotik von `q_{r,T}`.

---

# 16. Was C6w ausdrücklich nicht beweist

C6w beweist **nicht**:

\[
\sum_{(p,a)\in\mathcal I_T}\mathcal E_{p,a,T}(r_T)
\ge c\|r_T\|^2,
\]

\[
q_{r,T}\not\to0,
\]

\[
q_{r,T}\to0,
\]

\[
a_{R,T}^{(2)}\ne0,
\]

\[
\rho_T^{(2)}\to0,
\]

oder irgendeine asymptotische Formel für `\lambda_T`.

Es beweist ebenfalls nicht, dass **jede wachsende** Primfamilie koerziv ist. Wachstum ist für die ambiente Frame-Route nach dem finite-subframe No-Go notwendig, aber nicht hinreichend.

---

# 17. Nächster atomarer Knoten

Der C6-Strang sollte jetzt nicht wieder zu einem beliebigen neuen Einzelkanal zurückkehren. C6w hat die fixe-finite Subframe-Route vollständig klassifiziert.

Der nächste sinnvolle atomare Knoten ist daher

\[
\boxed{[P11\text{-}C1z\text{-}B2\text{-}C6x]}
\]

mit Arbeitstitel etwa

`ExpandingPrimeMartingaleFrame_ResidualMassDistribution`.

Er sollte genau eine der beiden verbleibenden positiven Routen testen:

1. **Expanding-family test:** Kann aus der vollen oder einer natürlich mit `T` wachsenden ersten-Prime-Familie eine quantitative Symbol-/Frame-Untergrenze gewonnen werden?
2. **Residual-mass test:** Welche zusätzliche Struktur der expliziten Form von `r_T` kontrolliert seine Masse in den gemeinsamen Quasi-Nullregionen?
3. Prime-Tiefen dürfen nur hinzugefügt werden, wenn ihr Beitrag über die bereits bekannte gemeinsame Prime-Nullgeometrie hinaus quantitativ genutzt wird.
4. Erst eine tatsächlich uniforme residualspezifische Untergrenze darf in eine Aussage über `q_{r,T}` übersetzt werden.

Bis dahin bleibt

\[
\boxed{P11=\texttt{PASS-A ACTIVE}.}
\]

Kein SYN, kein Seal, kein `papers/P11`.

---

# 18. Kurzfazit

C6w schließt den naheliegenden Hoffnungsschritt

\[
(2,0)+(3,0)
\quad\Longrightarrow\quad
\text{uniformes mixed-prime Frame}
\]

auf ambienter Ebene.

Die beiden Symbole

\[
m_2(\xi),\qquad m_3(\xi)
\]

haben zwar keine gemeinsame nichttriviale exakte Nullstelle. Aber die Irrationalität von `\log3/\log2` erzeugt gerade nicht nur Trennung, sondern via diophantischer Approximation unendlich viele hohe Frequenzen, bei denen ein 2-adischer exakter Nullpunkt arbiträr nahe an einem 3-adischen Nullpunkt liegt. Die zugehörigen Symbole werden gleichzeitig arbiträr klein.

Dieses Phänomen verallgemeinert sich durch simultane Dirichlet-Approximation auf jede feste endliche Primmenge und, wegen der gemeinsamen Prime-Winkelstruktur, auf jede feste endliche Prime-/Tiefenfamilie.

Damit ist die C6-Mechanik nun wesentlich schärfer lokalisiert:

\[
\boxed{
\text{fixed finite subframe: No-Go ambient}
}
\]

und als verbleibende Wege

\[
\boxed{
\text{growing mixed-prime family}
\quad\text{oder}\quad
\text{residual-specific spectral avoidance}.
}
\]

Genau dort muss C6 als Nächstes entscheiden, ob die volle arithmetische Martingalstruktur tatsächlich genug relative Restenergie erzwingt.