# P11-C1z-B2-C5b — Prime-Frame / Reverse-Large-Sieve-Audit und Future-Screening

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C5b]`  
**Vorgänger:** C1z-B2-C5a  
**Schnittstellen:** C1z-B/B1; C1z-B2-C3/C4/C5/C5a; P03-Haar-L2-Firewall

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C5b]
\quad
\checkmark[K/M]_{\rm part}
\;+
\checkmark[M]_{\rm neg,macro\text{-}boundary\text{-}profile}
}
\]

mit fünf getrennten Befunden:

\[
\boxed{
\text{die rein primweise Cauchy--Schwarz-Route verliert exakt nur }\log T,
}
\]

\[
\boxed{
\text{der restkontrollierte Anteil der terminalen Boundary-Shell besitzt bereits einen }O(T^{-1})\text{-Gewinn},
}
\]

\[
\boxed{
\text{jede feste makroskopische Boundary-Profilfamilie wird im Shell-Feshbachquotienten mit }O(T^{-1})\text{ gescreent},
}
\]

\[
\boxed{
\text{die PNT-Gewichte zeigen einen kanonischen Future-Screening-Transfer }d\mapsto d/2
\text{ mit Faktor }e^{-d/2}/T,
}
\]

und

\[
\boxed{
\text{der volle diskrete C5a-Frame-Satz bleibt }?[O]\text{ und ist jetzt als source-windowed}\
\textbf{lower-frame / observability / reverse-large-sieve}\text{-Problem typisiert.}
}
\]

Insbesondere ist ein möglicher negativer Zeuge jetzt stark eingeschränkt: Er kann weder ein fester Boundary-Modus noch ein festes reskaliertes Randprofil sein. Er müsste eine genuin `T`-abhängige Mikrostruktur besitzen, die gleichzeitig

1. die immer dichter werdende diskrete Primreflexionsfamilie ausnutzt,
2. den positiven Restgraphen klein hält,
3. und dennoch mit dem glatten festen alten Test `f` nicht asymptotisch orthogonal wird.

Der Knoten entscheidet die volle uniforme gerade Terminalbeschränktheit noch nicht.

---

# 0. Urteil

C5a reduzierte für festes gerades

\[
f\in\mathcal K_{X,R}^{+}
\]

das gesamte wachsende Problem auf

\[
\boxed{
\left|
\sum_{p\le e^{2T}}
\sqrt{\log p}\,p^{-3/4}
\langle J_{R,T}f,D_{\log p}E_Te\rangle
\right|^2
\lesssim_{R,f}
\|e\|_2^2
+
\|R_T^{(1)}e\|^2
}
\tag{C1zB2C5b.1}
\]

für alle ungeraden

\[
e\in\mathscr H_T^{-}.
\]

Hier

\[
\boxed{
\|R_T^{(1)}e\|^2
=
\sum_{p\le e^{2T}}
\frac{\log p}{\sqrt p}
\left(1-\frac1p\right)
\left\|
1_{\{|u|\le T-a_p\}}D_{\log p}E_Te
\right\|_2^2,
\qquad
a_p=\frac12\log p.
}
\tag{C1zB2C5b.2}
\]

C5a nannte (C1zB2C5b.1) eine Prime-Frame-/Large-Sieve-Ungleichung.

C5b präzisiert die Terminologie und die tatsächliche Richtung:

- eine klassische Large-Sieve-Abschätzung ist typischerweise eine **obere** Bessel-/Sampling-Schranke;
- hier wird eine **untere** Kontrolle der relevanten Source-Moden durch eine wachsende Familie zensierter Primdifferenzen benötigt, beziehungsweise dual dazu eine uniforme Observability-Schranke für das Hubfunktional.

Die mathematisch passendere Kurzbezeichnung lautet daher

\[
\boxed{
\text{source-windowed reverse large sieve / lower prime-frame observability.}
}
\tag{C1zB2C5b.3}
\]

Der folgende Audit zeigt zugleich, dass die rohe Gewichtsskala dieses Problems günstig ist. Die verbleibende Schwierigkeit ist nicht mehr die Größe der Prime-Summen, sondern ausschließlich eine mögliche `T`-abhängige Mikrostruktur der Source-Vektoren.

---

# 1. Fixierter Testcore und Support-Marge

Für den gesamten Knoten fixieren wir

\[
0<\rho_0<\rho<R
\]

und einen geraden Test

\[
\boxed{
0\ne f\in C_c^\infty((-\rho_0,\rho_0)),
\qquad
f(-u)=f(u).
}
\tag{C1zB2C5b.4}
\]

Die zusätzliche Zahl `rho` ist nur eine technische Shell-Marge. Sie ist **kein Regulator** und verändert den Test nicht.

Für eine Primzahl `p<=e^{2T}` setzen wir weiterhin

\[
a_p=\frac12\log p,
\qquad
r_p:=T-a_p\ge0.
\tag{C1zB2C5b.5}
\]

Dann ist der primitive Rest-Overlap genau

\[
|u|\le r_p.
\]

Wir unterscheiden:

### Bulk

\[
r_p\ge\rho
\quad\Longleftrightarrow\quad
a_p\le T-\rho.
\]

Dann liegt der gesamte Träger von `f` im Rest-Overlap.

### Boundary-Shell

\[
0\le r_p<\rho.
\]

Nur dort kann ein Teil des Hubterms außerhalb des primitiven Rest-Overlaps liegen.

---

# 2. Exakte Gewichtsfaktorisierung

Schreibe

\[
c_p:=\sqrt{\log p}\,p^{-3/4}
\]

für das primitive Hubgewicht und

\[
w_p:=\frac{\log p}{\sqrt p}\left(1-\frac1p\right)
\]

für das primitive Restgewicht.

Dann gilt exakt

\[
\boxed{
\frac{c_p}{\sqrt{w_p}}
=
\frac{p^{-1/2}}{\sqrt{1-1/p}}.
}
\tag{C1zB2C5b.6}
\]

Daher

\[
\boxed{
\frac{c_p^2}{w_p}
=
\frac1{p(1-1/p)}.
}
\tag{C1zB2C5b.7}
\]

Diese Identität erklärt vollständig den logarithmischen Verlust der naiven primweisen Cauchy--Schwarz-Route.

---

# 3. C5b-A — Bulk: der naive Verlust ist exakt logarithmisch

Für `r_p>=rho` liegt `supp f` vollständig im primitiven Rest-Overlap. Daher

\[
|\langle f,D_{\log p}E_Te\rangle|
\le
\|f\|_2
\left\|
1_{\{|u|\le r_p\}}D_{\log p}E_Te
\right\|_2.
\]

Setze

\[
L_{T,f}^{\rm bulk}(e)
:=
\sum_{a_p\le T-\rho}
 c_p\langle f,D_{\log p}E_Te\rangle.
\]

Gewichtete Cauchy--Schwarz liefert mit (C1zB2C5b.7)

\[
\begin{aligned}
|L_{T,f}^{\rm bulk}(e)|^2
\le{}&
\|f\|_2^2
\left(
\sum_{p\le e^{2(T-\rho)}}
\frac1{p(1-1/p)}
\right)
\\
&\times
\left(
\sum_{p\le e^{2(T-\rho)}}
w_p
\left\|
1_{\{|u|\le r_p\}}D_{\log p}E_Te
\right\|_2^2
\right).
\end{aligned}
\tag{C1zB2C5b.8}
\]

Nun

\[
\frac1{p(1-1/p)}
=
\frac1p+O(p^{-2}),
\]

und PNT/partielle Summation geben

\[
\sum_{p\le X}\frac1p
=
\log\log X+O(1).
\]

Mit

\[
X=e^{2(T-\rho)}
\]

folgt

\[
\boxed{
\sum_{p\le e^{2(T-\rho)}}
\frac1{p(1-1/p)}
=
\log T+O_\rho(1).
}
\tag{C1zB2C5b.9}
\]

Also

\[
\boxed{
|L_{T,f}^{\rm bulk}(e)|^2
\le
\bigl(\log T+O_\rho(1)\bigr)
\|f\|_2^2
\|R_T^{(1)}e\|^2.
}
\tag{C1zB2C5b.10}
\]

### Urteil

Die naive gleiche-Primzahl-Route verfehlt die gewünschte uniforme Schranke **nur logarithmisch**.

Das ist wichtig: Nach C3/C4 gab es exponentielle absolute Divergenzen im ungeraden Source-Sektor. Im geraden Kanal ist der rohe verbliebene Verlust nur

\[
\boxed{\log T.}
\]

Dieser Faktor ist aber real in der kanalweisen Abschätzung; er darf nicht einfach als `O(1)` gebucht werden.

---

# 4. Warum der logarithmische Verlust kein Beweis einer echten Divergenz ist

(C1zB2C5b.10) behandelt die Funktionen

\[
D_{\log p}e
\]

für verschiedene Primzahlen als voneinander unabhängige Daten.

Das sind sie nicht.

Alle Kanäle stammen aus **demselben** Source-Vektor `e`. Insbesondere erzeugen zwei Prime-Reflexionen durch Komposition eine Source-Translation mit Schritt

\[
\log p-\log q.
\]

Der Nullraumbeweis aus C5a ist die qualitative Extremform davon:

\[
D_{\log2}e=0,
\qquad
D_{\log3}e=0
\]

erzwingen wegen der inkommensurablen Perioden bereits Konstanz.

C5b.10 ignoriert diese gemeinsame Source-Geometrie vollständig.

Daher gilt nur:

\[
\boxed{
\text{same-prime Cauchy--Schwarz }\Rightarrow O(\log T),
}
\]

nicht

\[
\boxed{
\text{wahre Feshbach-Energie }\sim\log T.
}
\]

Ein echter Negativsatz müsste eine `T`-abhängige Familie `e_T` konstruieren, die die gemeinsame wachsende Reflexionsgeometrie tatsächlich ausnutzt.

---

# 5. C5b-B — der restkontrollierte Boundary-Shell-Anteil besitzt bereits `1/T`

Sei nun

\[
0\le r_p<\rho.
\]

Zerlege den Source-Test in

\[
f=f_{p,\rm in}+f_{p,\rm out},
\]

wobei

\[
f_{p,\rm in}:=1_{\{|u|\le r_p\}}f,
\qquad
f_{p,\rm out}:=1_{\{r_p<|u|<\rho_0\}}f.
\]

Der innere Anteil liegt wieder vollständig im primitiven Rest-Overlap.

Definiere

\[
L_{T,f}^{\rm shell,in}(e)
:=
\sum_{T-\rho<a_p\le T}
 c_p\langle f_{p,\rm in},D_{\log p}E_Te\rangle.
\]

Wie im Bulk:

\[
|L_{T,f}^{\rm shell,in}(e)|^2
\le
\|f\|_2^2
\left(
\sum_{e^{2(T-\rho)}<p\le e^{2T}}
\frac1{p(1-1/p)}
\right)
\|R_T^{(1)}e\|^2.
\tag{C1zB2C5b.11}
\]

PNT/partielle Summation liefern für festes `rho`:

\[
\begin{aligned}
\sum_{e^{2(T-\rho)}<p\le e^{2T}}
\frac1p
&=
\log\frac{T}{T-\rho}
+O_\rho(T^{-1})
\\
&=O_\rho(T^{-1}).
\end{aligned}
\tag{C1zB2C5b.12}
\]

Der `p^{-2}`-Korrekturterm ist in dieser hohen Shell noch kleiner. Also

\[
\boxed{
|L_{T,f}^{\rm shell,in}(e)|^2
\le
\frac{C_{\rho,f}}{T}
\|R_T^{(1)}e\|^2
\qquad(T\gg1).
}
\tag{C1zB2C5b.13}
\]

### Bedeutung

Derjenige Teil der Boundary-Shell, auf dem Hub und Rest denselben Source-Overlap sehen, ist bereits **besser als nötig** kontrolliert.

Der einzige Shell-Engpass liegt im äußeren Source-Streifen

\[
|u|>r_p,
\]

wo der primitive Rest nach C1z-B die Marke source-kanonisch abschneidet, der neutrale Hub aber aufgrund der Nullfortsetzung noch einen einseitigen Randbeitrag besitzt.

Genau dieser Streifen erzeugte C3 im anderen Paritätskanal die Boundary-Divergenz.

---

# 6. Boundary-Koordinaten für den äußeren Shell-Anteil

Wir analysieren jetzt diesen Streifen ohne einen neuen Counterterm.

Fixiere `rho_0<rho` wie in §1. Für

\[
0<r<\rho,
\qquad
a=T-r,
\]

und einen ungeraden Source-Vektor `e` betrachten wir auf der positiven Source-Hälfte `u>=0`.

Schreibe den positiven terminalen Boundary-Abstand als

\[
t:=T-x.
\]

Für eine feste Profilfunktion

\[
b:(0,2\rho)\to\mathbb C
\]

definieren wir die makroskopische ungerade Boundary-Familie

\[
\boxed{
e_T^b(x)
=
\begin{cases}
 b(T-x),&T-2\rho<x<T,\\
-b(T+x),&-T<x<-T+2\rho,\\
0,&|x|\le T-2\rho.
\end{cases}}
\tag{C1zB2C5b.14}
\]

Für `b in C_c^\infty((0,2rho))` liegt dies auf dem natürlichen glatten dichten Boundary-Core nach einer beliebig kleinen Endpunktglättung; für die `L^2`-Rechnung genügt (C1zB2C5b.14) direkt.

Für eine Shell-Primzahl mit

\[
r_p=r
\]

gilt auf dem primitiven Rest-Overlap `|u|<=r`:

\[
D_{\log p}E_Te_T^b(u)
=
\begin{cases}
 b(r-u)+b(r+u),&u\ge0,\\
 b(r+u)+b(r-u),&u<0,
\end{cases}
\]

also insgesamt eine gerade Funktion.

Daher

\[
\boxed{
\left\|
1_{\{|u|\le r\}}D_{\log p}E_Te_T^b
\right\|_2^2
=
2\int_0^r
|b(r-u)+b(r+u)|^2\,du.
}
\tag{C1zB2C5b.15}
\]

Dies ist die exakte Boundary-Reflexionsform des primitiven Rests.

---

# 7. PNT-Shellmaße: Hub und Rest besitzen verschiedene natürliche Skalierungen

Für eine feste stetige Funktion `Phi` auf `[0,rho]` betrachten wir die Shellpunkte

\[
r_p=T-\frac12\log p.
\]

PNT + partielle Summation geben die beiden gewichteten schwachen Grenzformeln

\[
\boxed{
\sqrt T\,e^{-T/2}
\sum_{0<r_p<\rho}
\sqrt{\log p}\,p^{-3/4}\Phi(r_p)
\longrightarrow
\sqrt2
\int_0^\rho e^{-r/2}\Phi(r)\,dr,
}
\tag{C1zB2C5b.16}
\]

und

\[
\boxed{
e^{-T}
\sum_{0<r_p<\rho}
\frac{\log p}{\sqrt p}
\left(1-\frac1p\right)
\Phi(r_p)
\longrightarrow
2
\int_0^\rho e^{-r}\Phi(r)\,dr.
}
\tag{C1zB2C5b.17}
\]

Die Gewichtsdichten lassen sich bereits heuristikfrei aus der Variablentransformation

\[
p=e^{2(T-r)}
\]

lesen:

\[
d\pi(p)\sim\frac{dp}{\log p}
\quad\Longrightarrow\quad
\begin{cases}
 c_p\,d\pi(p)
\sim
\sqrt2\,e^{T/2}T^{-1/2}e^{-r/2}\,dr,\\[1mm]
 w_p\,d\pi(p)
\sim
2e^Te^{-r}\,dr.
\end{cases}
\tag{C1zB2C5b.18}
\]

Damit ist die schon in C5a beobachtete `1/T`-Skala nicht nur ein `sgn`-Spezialfall, sondern die natürliche Shell-Skalierung des gesamten Hub/Rest-Paares.

---

# 8. Kontinuums-Restform der Boundary-Shell

Setze für ein festes Profil `b`

\[
\boxed{
\mathcal Q_\rho[b]
:=
4\int_0^\rho
e^{-r}
\int_0^r
|b(r-u)+b(r+u)|^2\,du\,dr.
}
\tag{C1zB2C5b.19}
\]

Aus (C1zB2C5b.15) und (C1zB2C5b.17) folgt

\[
\boxed{
e^{-T}
\|R_{T,\rm shell}^{(1)}e_T^b\|^2
\longrightarrow
\mathcal Q_\rho[b].
}
\tag{C1zB2C5b.20}
\]

Hier bezeichnet `R_{T,shell}^{(1)}` nur die primitiven Primzahlen mit `0<r_p<rho`.

Die Form besitzt eine nützliche äquivalente Zweipunktdarstellung. Mit

\[
t=r-u,
\qquad
s=r+u
\]

gilt

\[
dr\,du=\frac12\,dt\,ds,
\qquad
t+s=2r.
\]

Nach Symmetrisierung erhält man exakt

\[
\boxed{
\mathcal Q_\rho[b]
=
\int_{\substack{t\ge0,\ s\ge0\\t+s\le2\rho}}
 e^{-(t+s)/2}
|b(t)+b(s)|^2\,dt\,ds.
}
\tag{C1zB2C5b.21}
\]

Dies ist eine **signless reflection graph form** auf dem terminalen Boundary-Abstand.

---

# 9. Interior-Koerzivität der Kontinuums-Boundary-Form

Die Form (C1zB2C5b.21) ist am äußersten Punkt `t=2rho` nicht uniform koerziv: Ein Profil kann sich in einer immer dünneren Schicht direkt am Endpunkt konzentrieren.

Für unseren festen alten Test ist das jedoch nicht die relevante Region.

## Lemma C5b.1

Für jedes

\[
0<\delta<2\rho
\]

gibt es eine Konstante

\[
C_{\rho,\delta}<\infty
\]

mit

\[
\boxed{
\|b\|_{L^2(0,2\rho-\delta)}^2
\le
C_{\rho,\delta}\,
\mathcal Q_\rho[b]
}
\tag{C1zB2C5b.22}
\]

für alle `b` mit endlicher rechter Seite.

### Beweis

Wähle

\[
0<\varepsilon<\delta/2
\]

und das Ankerintervall

\[
A=(0,\varepsilon).
\]

Auf `A x A` liegt stets `t+s<2rho`. Außerdem ist das Gewicht `e^{-(t+s)/2}` dort von unten positiv beschränkt.

Die elementare Identität

\[
\int_A\int_A
|b(t)+b(s)|^2\,dt\,ds
=
2|A|\int_A|b|^2
+2\left|\int_A b\right|^2
\]

liefert

\[
\int_A|b|^2
\le C_{\rho,\varepsilon}\mathcal Q_\rho[b].
\tag{C1zB2C5b.23}
\]

Fixiere nun

\[
t\in[\varepsilon,2\rho-\delta].
\]

Für jedes `s in A` gilt wegen `s<delta/2`:

\[
t+s<2\rho.
\]

Mit

\[
|b(t)|^2
\le
2|b(t)+b(s)|^2+2|b(s)|^2
\]

und Integration über `s in A`:

\[
\varepsilon|b(t)|^2
\le
2\int_A|b(t)+b(s)|^2\,ds
+2\int_A|b(s)|^2\,ds.
\]

Integration in `t` und (C1zB2C5b.23) ergeben (C1zB2C5b.22). `□`

### Konsequenz

Die einzige mögliche makroskopische Schwäche der Kontinuums-Shellform sitzt direkt am äußersten Boundary-Endpunkt `t=2rho`.

Ein fester Test mit echter Support-Marge sieht diesen Punkt nicht.

---

# 10. Kontinuums-Hubfunktional für feste Boundary-Profile

Für `r in [0,rho]` setze

\[
\boxed{
\Phi_f[b;r]
:=
2\int_0^{\rho_0}
 f(u)
\left(
 b(r+u)
+1_{\{u\le r\}}b(r-u)
\right)du.
}
\tag{C1zB2C5b.24}
\]

Dies ist exakt der primitive Hub-Pairingterm

\[
\langle f,D_{\log p}E_Te_T^b\rangle
\]

für eine Shell-Primzahl mit Boundary-Abstand `r_p=r`.

Definiere das limitierende Hubfunktional

\[
\boxed{
\Lambda_{\rho,f}[b]
:=
\sqrt2
\int_0^\rho
 e^{-r/2}
\Phi_f[b;r]\,dr.
}
\tag{C1zB2C5b.25}
\]

Aus (C1zB2C5b.16):

\[
\boxed{
\sqrt T\,e^{-T/2}
L_{T,f}^{\rm shell}(e_T^b)
\longrightarrow
\Lambda_{\rho,f}[b].
}
\tag{C1zB2C5b.26}
\]

Wichtig ist nun die Support-Geometrie von `Lambda`.

In (C1zB2C5b.24) treten nur Werte

\[
r+u\le\rho+\rho_0
\]

und

\[
|r-u|\le\rho
\]

auf.

Setze

\[
\delta_f:=\rho-\rho_0>0.
\]

Dann

\[
\rho+\rho_0
=2\rho-\delta_f.
\]

Also hängt `Lambda_{rho,f}` ausschließlich von der **interioren** Profilregion

\[
0<t\le2\rho-\delta_f
\]

ab.

Mit Lemma C5b.1 und Cauchy--Schwarz folgt daher

\[
\boxed{
|\Lambda_{\rho,f}[b]|^2
\le
C_{\rho,f}\,
\mathcal Q_\rho[b].
}
\tag{C1zB2C5b.27}
\]

für alle zulässigen Profile `b`.

Dies ist die **kontinuierliche Boundary-Observability-Ungleichung**.

---

# 11. Hauptsatz C5b.1 — kein festes makroskopisches Boundary-Profil kann divergieren

Kombiniere

\[
L_{T,f}^{\rm shell}(e_T^b)
=
\frac{e^{T/2}}{\sqrt T}
\bigl(\Lambda_{\rho,f}[b]+o(1)\bigr)
\]

mit

\[
\|R_{T,\rm shell}^{(1)}e_T^b\|^2
=
e^T\bigl(\mathcal Q_\rho[b]+o(1)\bigr).
\]

Für `b ne 0` ist `Q_rho[b]>0`: Aus (C1zB2C5b.21) würde `Q=0` bedeuten

\[
b(t)+b(s)=0
\]

für fast alle Paare mit `t+s<2rho`; drei kleine Punkte erzwingen zunächst `b=0` nahe null, und danach koppelt jeder weitere Punkt an ein solches kleines `s`.

Daher

\[
\boxed{
\frac{
|L_{T,f}^{\rm shell}(e_T^b)|^2
}{
\|e_T^b\|_2^2
+
\|R_{T,\rm shell}^{(1)}e_T^b\|^2
}
\le
\frac{C_{\rho,f,b}+o(1)}{T}.
}
\tag{C1zB2C5b.28}
\]

Mit (C1zB2C5b.27) kann die Profilabhängigkeit der führenden Dualnorm sogar entfernt werden:

\[
\boxed{
\limsup_{T\to\infty}
T\,
\frac{
|L_{T,f}^{\rm shell}(e_T^b)|^2
}{
\|e_T^b\|_2^2
+
\|R_{T,\rm shell}^{(1)}e_T^b\|^2
}
\le
C_{\rho,f}
}
\tag{C1zB2C5b.29}
\]

für jedes feste `b` im Profilcore.

### Status

\[
\boxed{
\checkmark[M]_{\rm neg,macro\text{-}boundary\text{-}profile}.
}
\]

Das bedeutet **nicht**, dass die gesamte diskrete Shell uniform kontrolliert ist. Es schließt nur die gesamte Klasse der `T`-unabhängig reskalierten makroskopischen Boundary-Profile als Divergenzmechanismus aus.

Ein negativer Zeuge müsste daher `b=b_T` mit zunehmend feiner `T`-abhängiger Struktur besitzen.

---

# 12. Warum dies genau die diskrete Mikrostruktur als Restproblem isoliert

Die Grenzformeln (C1zB2C5b.16)--(C1zB2C5b.17) gelten für **feste** Testprofile gegen die gewichteten Primmaße.

Sie liefern nicht automatisch eine uniforme untere Frame-Schranke für beliebige Folgen

\[
b_T.
\]

Der Grund ist funktionalanalytisch präzise:

- die diskreten Prime-Reflexionsoperatoren hängen von den Punkten `r_p` ab;
- Translation/Reflexion ist auf `L^2` stark, aber nicht operatornorm-stetig in der Verschiebung;
- daher folgt aus schwacher Konvergenz der Primmaße kein uniformer Operator-Liminf für beliebige hochoszillatorische `b_T`.

Genau hier sitzt die noch fehlende Reverse-Large-Sieve-Aussage.

Ein legitimer nächster Beweis muss also entweder

1. eine quantitative Kompaktheit/Observability der `T`-abhängigen Quasi-Nullfolgen beweisen,

oder

2. eine solche Quasi-Nullfolge explizit konstruieren.

Bloße PNT-Maßkonvergenz reicht für diesen letzten Schritt nicht.

---

# 13. Future-Screening: der richtige Restkanal liegt bei halber Boundary-Distanz

C5a verglich einen Hubkanal im Wesentlichen mit dem Rest desselben Prime-Levels. Das produziert die harmonische `log T`-Summe.

Die Source-Geometrie zeigt jedoch einen stärkeren Mechanismus.

Betrachte einen Hub-Layer mit Mittelpunkt

\[
a=T-d,
\qquad d>0.
\]

Seine gewichtete PNT-Hubmasse pro fester `d`-Schale besitzt nach (C1zB2C5b.18) die Skala

\[
\boxed{
M_H(T,d)
\asymp
\frac{e^{T/2}}{\sqrt T}e^{-d/2}.
}
\tag{C1zB2C5b.30}
\]

Die Source-Punkte in der Umgebung dieses Layers werden aber von größeren Primtranslationen erfasst, deren Mittelpunkt ungefähr zwischen `a` und dem Terminalrand liegt:

\[
\boxed{
b\approx\frac{T+a}{2}=T-\frac d2.}
\tag{C1zB2C5b.31}
\]

Der dazugehörige primitive Rest-Layer besitzt Gewichtsskala

\[
\boxed{
M_R\left(T,\frac d2\right)
\asymp
 e^T e^{-d/2}.
}
\tag{C1zB2C5b.32}
\]

Daher ist das reine Gewichtverhältnis

\[
\boxed{
\frac{M_H(T,d)^2}
{M_R(T,d/2)}
\asymp
\frac{e^{-d/2}}{T}.
}
\tag{C1zB2C5b.33}
\]

Dies ist der **Future-Screening-Faktor**.

Im Gegensatz zum gleichen-Level-Verhältnis ist

\[
e^{-d/2}
\]

über feste `d`-Schalen summierbar.

Damit lautet die strukturell richtige Screening-Geometrie nicht

\[
\boxed{
\text{Hub bei }d
\leftrightarrow
\text{Rest bei }d,
}
\]

sondern

\[
\boxed{
\text{Hub bei }d
\longrightarrow
\text{Future-Rest bei }d/2.
}
\tag{C1zB2C5b.34}
\]

Dieser Halbierungsmechanismus ist direkt durch die Source-Reflexion erzwungen: Eine Translation mit Mittelpunkt `T-d/2` koppelt einen Punkt in Boundary-Distanz `d` an einen Punkt näher am Terminalrand.

**Firewall:** (C1zB2C5b.33) ist eine exakte PNT-Gewichtsskalierung, aber noch keine Operatorungleichung. Die fehlende Information ist, dass die zugehörigen Reflexionskanäle die richtigen Source-Komponenten tatsächlich uniform beobachten.

---

# 14. Konditionaler Future-Screening-Satz

Die Gewichtsanalyse legt eine wesentlich schärfere hinreichende Aussage nahe als die rohe C5a-Frameform.

Zerlege den positiven Source-Halbraum in feste Boundary-Distanz-Layer

\[
\mathcal A_j(T)
:=
\{x>0:j\Delta\le T-x<(j+1)\Delta\},
\qquad j=0,1,2,\ldots
\]

mit festem `Delta>0`.

Sei `L_{T,f,j}` der primitive Hubbeitrag, dessen Translationsmittelpunkte in Boundary-Distanz `d approximately j Delta` liegen, und `E_{T,j/2}^{future}` die primitive Restenergie in einer festen Schale um Boundary-Distanz `j Delta/2`.

Falls man die source-geometrische Layer-Observability

\[
\boxed{
|L_{T,f,j}(e)|^2
\le
C_{\Delta,R,f}
\frac{e^{-j\Delta/2}}{T}
E_{T,j/2}^{\rm future}(e)
}
\tag{C1zB2C5b.35}
\]

mit kontrollierter endlicher Überlappungsmultiplizität der verwendeten Future-Schalen beweist, dann folgt nach Summation über `j`

\[
\boxed{
|\mathcal L_{T,f}^{\rm prim}(e)|^2
\le
\frac{C_{R,f}}{T}
\|R_T^{(1)}e\|^2
+C_{R,f}\|e\|^2.
}
\tag{C1zB2C5b.36}
\]

Insbesondere wäre der primitive Feshbachbeitrag auf dem geraden Testcore nicht nur beschränkt, sondern asymptotisch stark gescreent.

Die geometrische Reihe

\[
\sum_{j\ge0}e^{-j\Delta/2}<\infty
\]

ist genau das, was den `log T`-Verlust aus §3 beseitigen würde.

### Urteil

Der fehlende Satz ist jetzt noch schärfer als (C1zB2C5a.21):

\[
\boxed{
\text{Beweise die diskrete Layer-Observability für den kanonischen Transfer }d\mapsto d/2.
}
\tag{C1zB2C5b.37}
\]

---

# 15. Warum die klassische Bezeichnung „Large Sieve“ allein zu unscharf ist

Die übliche Large-Sieve-Logik kontrolliert obere Quadratsummen beziehungsweise Bessel-Konstanten für getrennte Frequenzen oder Stichproben.

Unser Problem ist anders gerichtet:

- die Primkanäle sind bereits positive Restkanäle;
- wir benötigen eine **untere** Beobachtbarkeit des relevanten Source-Anteils durch diese Kanäle;
- die Fenster

\[
|u|\le T-a_p
\]

hängen vom selben Prime-Label ab;
- die Reflection-/Translation-Familie wird mit `T` dichter;
- der problematische Scope sind gerade mögliche hochoszillatorische Quasi-Nullfolgen.

Daher darf kein Standard-Large-Sieve-Satz ohne zusätzliche Brücke als Beweis von (C1zB2C5b.1) zitiert werden.

Die präzise Aufgabe ist eine **source-windowed lower frame inequality** beziehungsweise eine **reverse-large-sieve observability**.

---

# 16. Was C5b jetzt positiv bzw. negativ entschieden hat

## Positiv

1. Exakte Hub-/Rest-Gewichtsfaktorisierung (C1zB2C5b.6)--(C1zB2C5b.7).
2. Same-prime Bulkverlust exakt `log T`, nicht exponentiell.
3. Restkontrollierter Boundary-Shell-Anteil `O(1/T)`.
4. PNT-Shellgrenzen für Hub- und Restmaße.
5. Explizite Kontinuums-Boundary-Reflexionsform `Q_rho`.
6. Interior-Koerzivität dieser Kontinuumsform.
7. Kontinuierliche Boundary-Observability für den festen alten Test.
8. Future-Screening-Gewichtsfaktor `e^{-d/2}/T`.

## Negativ im klaren Scope

\[
\boxed{
\text{Ein festes makroskopisches Boundary-Profil kann den geraden Feshbachquotienten nicht divergieren lassen.}
}
\]

Status:

\[
\checkmark[M]_{\rm neg,macro\text{-}boundary\text{-}profile}.
\]

## Weiter offen

1. uniforme diskrete Lower-Frame-Ungleichung für beliebige `e_T`;
2. Ausschluss bzw. Konstruktion hochoszillatorischer Prime-Quasi-Nullfolgen;
3. (C1zB2C5b.35) als echter Operator-/Layer-Satz;
4. absolute gerade Terminalbeschränktheit;
5. Konvergenz von `G_{R,T}^+`;
6. gerader Cross-Terminal-Kern;
7. ungerader relativer Transport;
8. Objekt X.

---

# 17. Statusmatrix

| Aussage | Status |
|---|---|
| gleiche-Primzahl-CS liefert uniformen Bulkbound | `×[M]` — Verlust `log T` |
| gleiche-Primzahl-CS-Verlust ist höchstens logarithmisch | `✓[M]` |
| restkontrollierter Shell-Anteil | `✓[M]`, sogar `O(1/T)` |
| PNT-Shellmaß für Hub | `✓[M]` |
| PNT-Shellmaß für Rest | `✓[M]` |
| Kontinuums-Boundary-Restform | `✓[M]` |
| Interior-Koerzivität von `Q_rho` | `✓[M]` |
| feste makroskopische Boundary-Profile als Divergenzzeugen | `×[M]` |
| Future-Screening-Gewicht `d -> d/2` | `✓[M]` auf Skalierungsebene |
| diskrete Future-Layer-Observability | `?[O]` |
| volle source-windowed lower Prime-Frame-Ungleichung | `?[O]` |
| absolute gerade Terminalmetrik beschränkt | `?[O]` |
| gerader relativer Transportlimes | `?[O]` |
| Objekt X / exakte Weil-Geometrie | `?[O]` |

---

# 18. Scope-Firewalls

C5b beweist **nicht**:

1. dass (C1zB2C5a.21) für alle ungeraden `e` gilt;
2. dass keine `T`-abhängige hochoszillatorische Quasi-Nullfolge existiert;
3. dass PNT-Maßkonvergenz allein eine Operatornorm- oder Mosco-Liminf-Aussage liefert;
4. dass die absolute gerade Terminalmetrik konvergiert;
5. dass `sigma_T^+(f)->0`;
6. dass der relative Transport konvergiert;
7. dass ein klassischer Standard-Large-Sieve-Satz unmittelbar auf die zensierte Primreflexionsform anwendbar ist;
8. P10-O07;
9. P04/Suzuki;
10. Objekt X oder RH.

Insbesondere bleibt P11 `PASS-A ACTIVE`; kein SYN, kein Seal.

---

# 19. Strukturelles Gesamtbild nach C5b

Der gerade Kanal hat nun die Kette

\[
\boxed{
\begin{array}{c}
\text{Boundary-Jet identisch blind}\\
\downarrow\\
\text{keine ungerade primitive Restnullmode}\\
\downarrow\\
\operatorname{sgn}\text{-Mode }O(1/T)\text{ gescreent}\\
\downarrow\\
\text{kein fester endlicher Primblock koerziv}\\
\downarrow\\
\text{same-prime Gesamtabschätzung verliert nur }\log T\\
\downarrow\\
\text{Boundary-Shell auf makroskopischen Profilen }O(1/T)\\
\downarrow\\
\text{Future-Screening }d\mapsto d/2\text{ besitzt summierbare Gewichtsskala}\\
\downarrow\\
\textbf{nur noch diskrete }T\textbf{-abhängige Mikrostruktur offen.}
\end{array}}
\]

Damit ist C5b ein echter Fortschritt trotz offenem Endsatz: Der mögliche Gegenmechanismus ist von einer allgemeinen „Large-Sieve-Lücke“ auf eine sehr spezielle hochoszillatorische diskrete Prime-Frame-Frage reduziert.

---

# 20. Nächster atomarer Knoten

Der nächste Knoten soll **nicht** wieder dieselben PNT-Skalierungen wiederholen.

Er muss die nun isolierte Mikrostruktur direkt angreifen:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C5c]
\quad
\text{Diskrete Future-Layer-Observability / Quasi-Null-Audit}.
}
\]

Zwei exklusive Ausgänge:

### C5c-A — positiver Weg

Beweise eine diskrete Version von

\[
|L_{T,f,j}(e)|^2
\lesssim
\frac{e^{-j\Delta/2}}{T}
E_{T,j/2}^{\rm future}(e)
\]

nach geeigneter endlich überlappender Layerzerlegung.

Dann folgt die volle uniforme gerade Prime-Frame-Kontrolle.

### C5c-B — negativer Weg

Konstruiere explizit

\[
e_T\in\mathscr H_T^-,
\qquad
\|e_T\|^2+\|R_T^{(1)}e_T\|^2=1,
\]

mit

\[
|\mathcal L_{T,f}^{\rm prim}(e_T)|\to\infty.
\]

Nach C5b kann eine solche Folge weder eine feste Sinus-/Boundary-Makroform noch eine `T`-unabhängige reskalierte Randmode sein. Sie müsste die diskreten Primepunkte auf immer feineren Skalen ausnutzen.

Damit ist die Alternative jetzt maximal scharf:

\[
\boxed{
\text{diskrete Future-Observability}
\quad\text{oder}\quad
\text{echte Prime-Mikrostruktur-Quasi-Nullfolge}.}
\]

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal.
