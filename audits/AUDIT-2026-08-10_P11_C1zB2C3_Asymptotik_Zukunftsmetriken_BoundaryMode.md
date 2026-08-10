# P11-C1z-B2-C3 — Asymptotikaudit der Zukunftsmetriken: kanonische Source-Randmode erzwingt Divergenz

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C3]`  
**Vorgänger:** C1z-B2-C2  
**Schnittstellen:** C1z-B, C1z-B1, C1z-B2-B/C/C1/C2; P03-Haar-L2-Firewall  

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C3]
\quad
\checkmark[K/M]_{\rm part}
\;+
\checkmark[M]_{\rm neg,naive\text{-}terminal}
}
\]

mit dem neuen harten Befund

\[
\boxed{
\forall R>0\;\exists f\in C_c^\infty((0,R)),\ f\ne0:
\quad
\sigma_T(J_{R,T}f)\longrightarrow+\infty
\qquad(T\to\infty).
}
\]

Genauer existiert für geeignete nichtnegative einseitige Testfunktionen eine Konstante `c_f>0` mit

\[
\boxed{
\sigma_T(J_{R,T}f)
\ge
c_f\frac{e^T}{T^3}
\qquad(T\gg1).
}
\tag{C1zB2C3.1}
\]

Daraus folgt

\[
\boxed{
\langle G_{R,T}f,f\rangle_{X,R}\to+\infty,
\qquad
\|G_{R,T}\|\to\infty
}
\tag{C1zB2C3.2}
\]

für jedes feste `R>0` entlang geeigneter Vektoren des alten Levels.

Damit existiert **kein** beschränkter positiver Terminaloperator

\[
G_{R,\infty}\in\mathcal B(\mathcal K_{X,R})
\]

mit

\[
G_{R,T}\to G_{R,\infty}
\]

stark, schwach oder in Norm auf dem gesamten `\mathcal K_{X,R}`.

Der endliche Terminal-Gauge-Satz aus C2 bleibt vollständig korrekt. Negativ entschieden ist nur der naiv erwartete **bounded terminal-metric limit**.

Der Mechanismus ist source-geometrisch präzise: Die Rest-Feshbach-Geometrie screenet die globale Prime-Inzidenz stark, aber ein Rand-/Konstanten-Testvektor wächst im Hub exponentiell, während seine Restenergie nur polynomial wächst. Die Variationsungleichung für `(I+R_T^*R_T)^{-1}` überträgt diesen Mismatch direkt in `sigma_T`.

---

# 0. Urteil und strukturelle Bedeutung

C1z-B2-C2 hatte gezeigt, dass jeder endliche Terminalhorizont `T` eine kanonische kohärente isometrische Gauge besitzt:

\[
W_{R,S}^{[T]}
=G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}.
\]

Der damals verbleibende offene Punkt war:

\[
\boxed{
G_{R,T}\stackrel{T\to\infty}{?}G_{R,\infty}
}
\]

für festes `R`.

C3 entscheidet diese Frage für die **unrenormierte bounded-terminal Variante negativ**.

Die Divergenz kommt nicht aus einer erneuten C1q-artigen Hilbertnormschätzung des Hubs allein. Der Feshbach-Nenner

\[
B_T=(I+R_T^*R_T)^{-1}
\]

wird vollständig berücksichtigt.

Der neue Schlüssel ist die allgemeine Ungleichung

\[
\boxed{
\langle h,B_Th\rangle
\ge
\frac{|\langle h,e\rangle|^2}
{\langle e,(I+R_T^*R_T)e\rangle}
}
\tag{C1zB2C3.3}
\]

für jeden Testvektor `e`.

Wir wählen als `e` die konstante Source-Mode

\[
\mathbf 1_T:=1_{(-T,T)}.
\]

Für diese Mode gilt:

1. der source-windowed Hub koppelt an ein festes altes einseitiges `f` mit Größe `\gtrsim e^{T/2}/\sqrt T`;
2. der konditionierte Rest besitzt auf `\mathbf 1_T` nur `O(T^2)` Energie;
3. daher bleibt nach Feshbach-Elimination mindestens `\gtrsim e^T/T^3` effektive Hubenergie übrig.

Dies isoliert erstmals eine konkrete **Source-Randmode**, die den naiven Terminalmetrik-Limes blockiert.

---

# 1. Verbindliche Zukunftsmetrik aus C2

Fixiere `R>0`. Für `T>R` ist

\[
J_{R,T}:\mathcal K_{X,R}\to\mathcal K_{X,T}
\]

die kanonische Nullfortsetzungs-Transition.

Der Zukunftsmetrikoperator ist

\[
\boxed{
G_{R,T}:=J_{R,T}^*J_{R,T}.
}
\tag{C1zB2C3.4}
\]

Für `f\in\mathcal K_{X,R}` gilt

\[
\boxed{
\langle G_{R,T}f,f\rangle_{X,R}
=q_T^X(J_{R,T}f).
}
\tag{C1zB2C3.5}
\]

Aus C1z-B2-C:

\[
q_T^X(g)
=q_{\Gamma,T}(g)+\sigma_T(g),
\]

mit

\[
\boxed{
\sigma_T(g)
=
\langle H_T^*g,
(I+R_T^*R_T)^{-1}H_T^*g\rangle.
}
\tag{C1zB2C3.6}
\]

Der Gammaanteil ist unter Nullfortsetzung exakt invariant:

\[
q_{\Gamma,T}(J_{R,T}f)=q_{\Gamma,R}(f).
\]

Damit lautet die gesamte Terminalfrage:

\[
\boxed{
\langle G_{R,T}f,f\rangle_{X,R}
=q_{\Gamma,R}(f)+\sigma_T(J_{R,T}f).
}
\tag{C1zB2C3.7}
\]

C3 untersucht deshalb nur `sigma_T`.

---

# 2. Verbindlicher Hub- und Restoperator

Für das Terminallevel `T` ist

\[
\mathscr H_T=L^2(-T,T).
\]

Setze

\[
\mathcal N_T=\{p^k:p^k\le e^{2T}\}.
\]

Der source-windowed neutrale Hub ist

\[
\boxed{
H_T
=
P_T\sum_{p^k\in\mathcal N_T}
\sqrt{\log p}\,p^{-3k/4}
D_{k\log p}E_T.
}
\tag{C1zB2C3.8}
\]

Der konditionierte Rest aus C1z-B lautet formal

\[
\boxed{
R_Ta(u)
=
\sum_p\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_Ta(u)
\otimes
\mathsf Q_T(u)\eta_{p,k}.
}
\tag{C1zB2C3.9}
\]

Für festes `T` ist dies ein endlicher effektiver Operator; verschiedene Primsektoren `K_p^0` sind orthogonal.

Aus C1z-B:

\[
\mathsf Q_T(u)\eta_{p,1}
=
1_{\{|u|\le T-\frac12\log p\}}\eta_{p,1}.
\tag{C1zB2C3.10}
\]

Ferner

\[
\|\mathsf Q_T(u)\eta_{p,k}\|
\le\|\eta_{p,k}\|\le1.
\tag{C1zB2C3.11}
\]

---

# 3. Variationslemma für den Feshbach-Nenner

## Lemma C1zB2C3.1

Sei `A>=I` positiv selbstadjungiert mit beschränkter Inverser. Dann gilt für alle `h` und alle `e` in der Formdomäne von `A`:

\[
\boxed{
\langle h,A^{-1}h\rangle
\ge
\frac{|\langle h,e\rangle|^2}
{\langle e,Ae\rangle}.
}
\tag{C1zB2C3.12}
\]

### Beweis

Cauchy-Schwarz für `A^{-1/2}h` und `A^{1/2}e` liefert

\[
|\langle h,e\rangle|^2
=|\langle A^{-1/2}h,A^{1/2}e\rangle|^2
\le
\langle h,A^{-1}h\rangle\langle e,Ae\rangle.
\]

`□`

Für

\[
A_T:=I+R_T^*R_T,
\qquad
h_T:=H_T^*J_{R,T}f
\]

folgt

\[
\boxed{
\sigma_T(J_{R,T}f)
\ge
\frac{|\langle h_T,e\rangle|^2}
{\|e\|^2+\|R_Te\|^2}.
}
\tag{C1zB2C3.13}
\]

Wir setzen nun `e=\mathbf1_T`.

---

# 4. Der primitive Rest verschwindet exakt auf der Konstantenmode

Sei

\[
\mathbf1_T(u)=1
\qquad(|u|<T).
\]

Fixiere eine Primzahl `p` und

\[
a_p:=\frac12\log p.
\]

Auf dem Träger des primitiven konditionierten Restlabels gilt nach (C1zB2C3.10)

\[
|u|\le T-a_p.
\]

Dann liegen beide Punkte

\[
u\pm a_p
\]

in `[-T,T]`. Daher

\[
D_{\log p}E_T\mathbf1_T(u)
=
1-1=0.
\]

Somit gilt exakt

\[
\boxed{
\sqrt{\log p}\,p^{-1/4}
D_{\log p}E_T\mathbf1_T(u)
\otimes\mathsf Q_T(u)\eta_{p,1}
=0
}
\tag{C1zB2C3.14}
\]

für jeden primitiven Restkanal.

**Interpretation.** Die dominante primitive Restmasse, die in C1w den Fourier-Hub screenet, sieht die konstante Source-Mode nach der source-gekoppelten Overlap-Konditionierung exakt nicht.

Das ist der neue Unterschied zur rein translationsinvarianten C1w-Geometrie.

---

# 5. Polynomiale obere Schranke für die Restenergie der Konstantenmode

Für `k>=2` gilt punktweise

\[
|D_{k\log p}E_T\mathbf1_T(u)|\le1
\]

fast überall.

Für einen festen Primsektor `p` setzen wir

\[
F_{p,T}(u)
:=
\sum_{k\ge2}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_T\mathbf1_T(u)
\mathsf Q_T(u)\eta_{p,k}.
\]

Mit (C1zB2C3.11):

\[
\begin{aligned}
\|F_{p,T}(u)\|
&\le
\sqrt{\log p}
\sum_{k\ge2}p^{-k/4}\\
&=
\sqrt{\log p}
\frac{p^{-1/2}}{1-p^{-1/4}}\\
&\le
C\frac{\sqrt{\log p}}{\sqrt p},
\end{aligned}
\tag{C1zB2C3.15}
\]

mit universellem `C`, da `p>=2`.

Falls irgendein konditionierter Restbeitrag im `p`-Sektor nichtverschwindend ist, muss mindestens `J_{p,T}(u)>=1` für ein `u` gelten; insbesondere

\[
p\le e^{2T}.
\]

Da der Source-Raum Länge `2T` besitzt,

\[
\|F_{p,T}\|_{L^2}^2
\le
C_1T\frac{\log p}{p}.
\tag{C1zB2C3.16}
\]

Die Räume `K_p^0` sind für verschiedene Primzahlen orthogonal. Deshalb

\[
\|R_T\mathbf1_T\|^2
=
\sum_{p\le e^{2T}}\|F_{p,T}\|^2
\le
C_1T
\sum_{p\le e^{2T}}
\frac{\log p}{p}.
\]

Mit PNT/partieller Summation

\[
\sum_{p\le X}\frac{\log p}{p}=O(\log X)
\]

folgt

\[
\boxed{
\|R_T\mathbf1_T\|^2
=O(T^2).
}
\tag{C1zB2C3.17}
\]

Da

\[
\|\mathbf1_T\|^2=2T,
\]

gilt damit

\[
\boxed{
\langle\mathbf1_T,A_T\mathbf1_T\rangle
=2T+\|R_T\mathbf1_T\|^2
=O(T^2).
}
\tag{C1zB2C3.18}
\]

Dies ist die entscheidende **nur polynomiale Screening-Schranke** für die gewählte Randmode.

---

# 6. Exponentielle Hubkopplung an ein festes altes einseitiges Testsignal

Fixiere nun

\[
0<a<b<R
\]

und wähle

\[
\boxed{
0\ne f\in C_c^\infty((a,b)),
\qquad f\ge0.
}
\tag{C1zB2C3.19}
\]

Wir betrachten

\[
h_T:=H_T^*J_{R,T}f.
\]

Da

\[
|\langle h_T,\mathbf1_T\rangle|
=|\langle J_{R,T}f,H_T\mathbf1_T\rangle|,
\]

genügt eine untere Schranke für `H_T\mathbf1_T` auf `(a,b)`.

Fixiere `u\in[a,b]`. Für eine primitive Primzahl `p` mit

\[
\boxed{
e^{2(T-a)}<p\le e^{2T}}
\tag{C1zB2C3.20}
\]

ist

\[
a_p=\frac12\log p>T-a\ge T-u.
\]

Da zugleich `a_p<=T`, gilt für `u>0`:

\[
u+a_p>T,
\qquad
u-a_p>-T.
\]

Somit

\[
D_{\log p}E_T\mathbf1_T(u)
=-1.
\tag{C1zB2C3.21}
\]

Alle diese primitiven Beiträge besitzen auf `(a,b)` dasselbe Vorzeichen. Daher

\[
|\langle J_{R,T}f,H_T\mathbf1_T\rangle|
\ge
\left(\int_a^bf(u)\,du\right)
S_T(a),
\tag{C1zB2C3.22}
\]

wobei

\[
\boxed{
S_T(a)
:=
\sum_{e^{2(T-a)}<p\le e^{2T}}
\sqrt{\log p}\,p^{-3/4}.
}
\tag{C1zB2C3.23}
\]

PNT + partielle Summation liefern für jedes feste `a>0`

\[
\boxed{
S_T(a)
\asymp_a
\frac{e^{T/2}}{\sqrt T}.
}
\tag{C1zB2C3.24}
\]

Genauer ist der primitive Hauptterm

\[
S_T(a)
\sim
2\sqrt2\,(1-e^{-a/2})
\frac{e^{T/2}}{\sqrt T}.
\tag{C1zB2C3.25}
\]

Für den Divergenzsatz wird nur die untere Schranke benötigt. Setze

\[
m_f:=\int_a^bf(u)\,du>0.
\]

Dann existiert `c_{a,f}>0` mit

\[
\boxed{
|\langle h_T,\mathbf1_T\rangle|
\ge
c_{a,f}\frac{e^{T/2}}{\sqrt T}
\qquad(T\gg1).
}
\tag{C1zB2C3.26}
\]

Die höheren Prime-Powers werden für diese Untergrenze nicht benötigt; primitive Primzahlen allein genügen.

---

# 7. Hauptsatz: `sigma_T` divergiert trotz Feshbach-Screening

Setze in (C1zB2C3.13)

\[
e=\mathbf1_T.
\]

Aus (C1zB2C3.18) und (C1zB2C3.26):

\[
\begin{aligned}
\sigma_T(J_{R,T}f)
&\ge
\frac{|\langle h_T,\mathbf1_T\rangle|^2}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}\\
&\ge
\frac{c_{a,f}^2e^T/T}
{C T^2}.
\end{aligned}
\]

Also:

\[
\boxed{
\sigma_T(J_{R,T}f)
\ge
c_f\frac{e^T}{T^3}
\longrightarrow+\infty.
}
\tag{C1zB2C3.27}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm neg,naive\text{-}terminal}.}
\]

Dies ist ein Feshbach-stabiler Divergenzbefund: Der Nenner `(I+R_T^*R_T)^{-1}` wurde nicht verworfen oder durch `I` ersetzt.

---

# 8. Konsequenz für die Zukunftsmetriken `G_{R,T}`

Nach (C1zB2C3.7):

\[
\langle G_{R,T}f,f\rangle_{X,R}
=q_{\Gamma,R}(f)+\sigma_T(J_{R,T}f).
\]

Der Gammaanteil ist fest und endlich. Daher

\[
\boxed{
\langle G_{R,T}f,f\rangle_{X,R}
\to+\infty.
}
\tag{C1zB2C3.28}
\]

Für den normierten Vektor

\[
\widetilde f=f/\|f\|_{X,R}
\]

folgt

\[
\|G_{R,T}\|
\ge
\langle G_{R,T}\widetilde f,\widetilde f\rangle_{X,R}
\to+\infty.
\]

Also

\[
\boxed{
\sup_{T>R}\|G_{R,T}\|=\infty.
}
\tag{C1zB2C3.29}
\]

Damit kann `G_{R,T}` nicht in irgendeiner der üblichen Operator-Topologien zu einem **beschränkten** Operator auf `\mathcal K_{X,R}` konvergieren:

- keine Normkonvergenz;
- keine starke Operatorkonvergenz zu einem beschränkten Operator;
- keine schwache Operatorkonvergenz zu einem beschränkten Operator.

Die letzten beiden Aussagen folgen auch aus dem Uniform-Boundedness-Prinzip; hier liegt sogar ein einzelner fester Divergenzzeuge vor.

---

# 9. Die Untergrenze aus C2 bleibt richtig — aber die Oberseite scheitert maximal

C1/C2 hatten für festes `R` die terminalunabhängige Untergrenze

\[
G_{R,T}
\ge
\frac1{1+\|H_R\|^2}I
\qquad(T>R)
\]

bewiesen.

C3 zeigt nun:

\[
\boxed{
\text{keine Degeneration nach unten}
\quad\text{aber}\quad
\text{unbeschränkte Expansion nach oben}.}
\tag{C1zB2C3.30}
\]

Das Terminalproblem ist damit nicht ein Kollaps der Metrik, sondern eine **source-induzierte Ausblasung einzelner Richtungen**.

---

# 10. Warum dies C1w nicht widerspricht

C1w arbeitete global translationsinvariant und faserweise im Fourierbild. Für jedes feste `xi!=0` galt dort

\[
\frac{|h_T(\xi)|^2}{1+\rho_T(\xi)}\to0.
\]

C3 benutzt dagegen den source-windowed, nichttranslationinvarianten C1z-B/B1-Aufbau.

Der entscheidende neue Effekt ist (C1zB2C3.14):

\[
\boxed{
\text{primitive konditionierte Restkanäle verschwinden exakt auf }\mathbf1_T,
}
\]

während der source-windowed Hub `H_T\mathbf1_T` gerade aus den Randabbrüchen der Translationen wächst.

Somit ist die C3-Randmode im C1w-Fouriermodell nicht als feste nichtzero Frequenz vorhanden. Die beiden Aussagen liegen in verschiedenen, korrekt getrennten Scopes.

C1w wird nicht korrigiert und nicht widerlegt.

---

# 11. Kanonische asymptotische Randfunktion

Die Rechnung aus §6 identifiziert mehr als nur einen Divergenzzeugen.

Für festes `u>0` ist der primitive Randhub

\[
S_T(u)
:=
\sum_{e^{2(T-u)}<p\le e^{2T}}
\sqrt{\log p}\,p^{-3/4}.
\]

PNT/partielle Summation geben

\[
\boxed{
\sqrt T\,e^{-T/2}S_T(u)
\longrightarrow
2\sqrt2\,(1-e^{-u/2}).
}
\tag{C1zB2C3.31}
\]

Für `u<0` tritt wegen der Orientierung von `D_s` das entgegengesetzte Vorzeichen auf.

Dies motiviert auf jedem festen alten Source-Level die kanonische lineare Randfunktionalform

\[
\boxed{
\beta_R(f)
:=
\int_{-R}^{R}
\operatorname{sgn}(u)
\bigl(1-e^{-|u|/2}\bigr)
 f(u)\,du.
}
\tag{C1zB2C3.32}
\]

Bis auf die feste Konstante `2\sqrt2` beschreibt `beta_R` die führende primitive Hubkopplung an `\mathbf1_T`.

Für die in §6 gewählten positiven einseitigen Tests gilt

\[
\beta_R(f)>0.
\]

**Firewall:** Aus C3 folgt noch nicht, dass die gesamte Divergenz von `G_{R,T}` asymptotisch rang eins ist oder exakt durch `|\beta_R\rangle\langle\beta_R|` beschrieben wird. Bewiesen ist nur, dass `beta_R` eine kanonische divergente Richtung detektiert.

---

# 12. Was jetzt negativ entschieden ist

Der folgende in C2 formulierte direkte Kandidat ist geschlossen:

\[
\boxed{
G_{R,T}\to G_{R,\infty}
\quad\text{in }\mathcal B(\mathcal K_{X,R})
}
\]

für einen positiven beschränkten invertierbaren Terminaloperator.

Insbesondere kann die `T=\infty`-Gauge **nicht** einfach durch Einsetzen eines bounded Grenzwerts in

\[
W_{R,S}^{[\infty]}
=G_{S,\infty}^{1/2}J_{R,S}G_{R,\infty}^{-1/2}
\]

gewonnen werden.

Status:

\[
\boxed{\checkmark[M]_{\rm neg,naive\text{-}terminal}.}
\]

Dies ist kein No-Go gegen eine renormierte, relative, quotientierte oder unbeschränkte Terminalmetrik.

---

# 13. Was weiterhin offen bleibt

C3 entscheidet ausdrücklich **nicht**:

1. ob eine kanonisch renormierte Familie `\widetilde G_{R,T}` konvergiert;
2. ob die Divergenz endlich-rangig ist;
3. ob `ker(beta_R)` eine terminal beschränkte Untergeometrie trägt;
4. ob ein quotientierter Randmodus einen positiven Grenzoperator erzeugt;
5. ob die finite-horizon Isometrien `W_{R,S}^{[T]}` selbst trotz divergenter `G_{R,T}` einen starken Grenzwert besitzen;
6. ob eine unbeschränkte positive Terminalmetrik sinnvoll als geschlossene Form existiert;
7. ob ein solcher Grenzträger die exakte Weilform realisiert;
8. P10-O07;
9. P04/Suzuki-Identifikation;
10. RH oder Objekt X.

Insbesondere bleibt die finite-horizon Trivialisierung aus C2 vollständig intakt.

---

# 14. Neue strukturelle Interpretation

Die C1z-Kette lautet nun:

\[
\boxed{
\begin{array}{c}
\text{source-gekoppelte finite-adische Restkonditionierung}\\
\downarrow\\
\text{finite-level Gamma-Hub-Feshbach mit kompakter Resolvente}\\
\downarrow\\
\text{keine endliche Schattenklasse}\\
\downarrow\\
\text{Gamma-Kompaktheit entweicht bei }R\to\infty\\
\downarrow\\
\text{Graphräume + bounded injective Transitionen}\\
\downarrow\\
\text{paarweise Polar-Isometrien + signierte Colligation}\\
\downarrow\\
\text{finite-horizon Metrik-Kokyklus exakt trivial}\\
\downarrow\\
\textbf{naive bounded Terminalmetrik divergiert in einer Source-Randmode.}
\end{array}}
\]

Der Grenzträger muss daher nicht nur die Haar-Geometrie verlassen, sondern auch die **unrenormierte Terminal-Pullback-Metrik**.

Die positive neue Information ist, dass der erste Divergenzkanal nicht anonym ist:

\[
\boxed{
\text{er wird durch die kanonische Randfunktion }\beta_R\text{ detektiert}.}
\]

Das macht einen kontrollierten nächsten Test möglich.

---

# 15. Nächster atomarer Knoten

Der nächste Schritt soll **keinen** Gegenfaktor rückwärts wählen.

Die durch C3 selbst erzwungene Frage lautet:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C4]
\quad
\text{Boundary-mode extraction / relative terminal metric}.
}
\]

In dieser Reihenfolge:

## C4-A — Rangtest der Divergenz

Prüfe, ob für festes `R`

\[
\sup_{T>R}
\langle G_{R,T}f,f\rangle_{X,R}<\infty
\]

für alle

\[
f\in\ker\beta_R
\]

gilt.

Falls ja, ist die C3-Divergenz tatsächlich in erster Ordnung ein kanonischer Rang-eins-Randkanal.

## C4-B — source-kanonische Relative/Quotient-Geometrie

Nur falls C4-A positiv ausfällt, teste den von `beta_R` bestimmten Quotienten beziehungsweise die orthogonale Relativebene. Kein frei gewählter Counterterm.

## C4-C — finite-horizon Gauge-Limes direkt

Unabhängig davon prüfe, ob

\[
W_{R,S}^{[T]}
\]

für feste `R<S` konvergiert, obwohl die einzelnen Terminalmetriken `G_{R,T}` divergieren. Ein gemeinsamer divergenter Gaugefaktor könnte sich in

\[
G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}
\]

wegheben.

Damit lautet die neue Leitfrage:

\[
\boxed{
\text{Ist die Terminaldivergenz nur ein kanonischer Rand-Gaugekanal,}
\text{ der im relativen/isometrischen Transport verschwindet?}
}
\]

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal.
