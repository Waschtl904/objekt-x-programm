# P11-C1z-B2-C5a — Gerader Terminalkanal: primitive Restkoerzivität, Variationsreduktion und Prime-Frame-Engpass

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C5a]`  
**Vorgänger:** C1z-B2-C5  
**Schnittstellen:** C1z-B/B1; C1z-B2-C3/C4/C5; P03-Haar-L2-Firewall  

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C5a]
\quad
\checkmark[K/M]_{\rm part}
\;+
\checkmark[M]_{\rm neg,finite\text{-}prime\text{-}coercivity}
}
\]

mit fünf getrennten Befunden:

\[
\boxed{
\text{der C3/C4-Boundary-Jet koppelt ausschließlich an den ungeraden Source-Sektor,}
}
\]

\[
\boxed{
\ker R_T^{(1)}\cap \mathscr H_T^-=\{0\}
\quad\text{für genügend großes }T,
}
\]

also besitzt der primitive konditionierte Rest **keine** nichttriviale ungerade Nullmode,

\[
\boxed{
\text{der kanonische Test }e_T=\operatorname{sgn}(u)
\text{ wird im geraden Kanal mit Rayleigh-Quotient }O(T^{-1})\text{ gescreent,}
}
\]

\[
\boxed{
\text{kein fester endlicher Primblock liefert eine quantitative Rest-Koerzivität auf }\mathscr H_T^-,
}
\]

und

\[
\boxed{
\text{die uniforme gerade Terminalkontrolle reduziert sich auf eine explizite wachsende Prime-Frame-/Large-Sieve-Ungleichung.}
}
\]

Der Knoten beweist **noch nicht**

\[
\sup_{T>R}\|G_{R,T}|_{\mathcal K_{X,R}^+}\|<\infty
\]

und auch noch nicht die starke Konvergenz des geraden relativen Transports. Er lokalisiert aber den fehlenden Satz vollständig: Nach Paritätsreduktion, Entfernung des global harmlosen höheren Prime-Power-Hubs und Ausschluss einer primitiven Restnullmode bleibt nur eine quantitative Frameabschätzung für die wachsende Familie primitiver Primtranslationen.

---

# 0. Urteil

C1z-B2-C5 hatte die exakte Paritätszerlegung

\[
\mathcal K_{X,R}=\mathcal K_{X,R}^+\oplus\mathcal K_{X,R}^-
\]

konstruiert und gezeigt, dass der vollständige Boundary-Jet

\[
(\beta_R^{(0)},\beta_R^{(1)},\ldots)
\]

den ungeraden Source-Sektor vollständig trennt.

Für den geraden Source-Sektor gilt dagegen

\[
\beta_R^{(m)}(f)=0
\qquad
\forall m\ge0,
\qquad
f\in\mathcal K_{X,R}^+.
\]

Damit verschwindet der gesamte bislang identifizierte C3/C4-Randmechanismus dort identisch.

Das allein beweist jedoch keine Terminalbeschränktheit. Der richtige Test ist die Feshbach-Variationsformel. Für gerades `f` ist

\[
h_T:=H_T^*J_{R,T}f
\]

ungerade. Daher darf im Variationsproblem ausschließlich gegen ungerade Source-Vektoren getestet werden.

Der entscheidende Unterschied zum ungeraden Source-Sektor ist:

- im ungeraden Source-Sektor war `h_T` gerade und koppelte an die konstante Mode `1_T`, auf der der primitive Rest exakt verschwindet;
- im geraden Source-Sektor ist `h_T` ungerade, also orthogonal zu `1_T`; jede relevante Variationsmode ist ungerade;
- der primitive Rest besitzt auf dem ungeraden Source-Raum keine nichttriviale exakte Nullmode.

Damit ist der C3-Divergenzmechanismus im geraden Kanal strukturell ausgeschlossen.

Was offen bleibt, ist eine **quantitative** Version dieser Aussage: Reicht die wachsende Familie primitiver Primkanäle aus, um die gesamte ungerade Variationsfamilie uniform zu screenen?

---

# 1. Paritätsnotation

Auf

\[
\mathscr H_T=L^2(-T,T)
\]

sei

\[
(\mathcal P_Te)(u):=e(-u).
\]

Setze

\[
\mathscr H_T^+:=\ker(\mathcal P_T-I),
\qquad
\mathscr H_T^-:=\ker(\mathcal P_T+I).
\]

Für den Kantenoperator

\[
D_s=U_{s/2}-U_{-s/2}
\]

gilt exakt

\[
\boxed{
\mathcal P_TD_s=-D_s\mathcal P_T
}
\tag{C1zB2C5a.1}
\]

auf dem source-windowed Scope, also

\[
D_s:\mathscr H_T^+\to\mathscr H_T^-,
\qquad
D_s:\mathscr H_T^-\to\mathscr H_T^+.
\]

Da die source-gekoppelte Konditionierung `Q_T(u)` nur von `|u|` abhängt, respektiert auch der Restoperator die entsprechende Paritätsumschaltung in der Source-Koordinate. Folglich kommutieren

\[
R_T^*R_T,
\qquad
A_T:=I+R_T^*R_T,
\qquad
A_T^{-1}
\]

mit `P_T`.

Dies ist die finite-level Version der in C5 bewiesenen Paritätszerlegung der Graphgeometrien.

---

# 2. Exakte Variationsformel im geraden Source-Kanal

Fixiere

\[
R>0,
\qquad
f\in\mathcal K_{X,R}^+,
\qquad
T>R.
\]

Wie in C3/C4:

\[
\sigma_T(J_{R,T}f)
=
\langle h_T,A_T^{-1}h_T\rangle,
\qquad
h_T:=H_T^*J_{R,T}f.
\]

Da `H_T` die Parität wechselt,

\[
\boxed{h_T\in\mathscr H_T^-.}
\tag{C1zB2C5a.2}
\]

Für jeden positiven invertierbaren Operator `A` gilt

\[
\langle h,A^{-1}h\rangle
=
\sup_{0\ne e}
\frac{|\langle h,e\rangle|^2}{\langle e,Ae\rangle}.
\]

Da `A_T` die Parität respektiert und `h_T` ungerade ist, genügt der ungerade Sektor:

\[
\boxed{
\sigma_T(J_{R,T}f)
=
\sup_{0\ne e\in\mathscr H_T^-}
\frac{|\langle J_{R,T}f,H_Te\rangle|^2}
{\|e\|_2^2+\|R_Te\|^2}.
}
\tag{C1zB2C5a.3}
\]

Dies ist die verbindliche Form des geraden Terminalproblems.

**Interpretation.** Um den geraden Kanal uniform zu kontrollieren, muss man keinen Operatorgrenzwert direkt erraten. Man muss nur zeigen, dass die linearen Funktionale

\[
e\longmapsto\langle J_{R,T}f,H_Te\rangle
\]

auf dem ungeraden Rest-Graphraum

\[
\bigl(\mathscr H_T^-,\ \|e\|_2^2+\|R_Te\|^2\bigr)
\]

uniform in `T` beschränkt sind.

---

# 3. Warum die C3-Konstantenmode im geraden Source-Kanal exakt verschwindet

C3 benutzte

\[
\mathbf1_T=1_{(-T,T)}\in\mathscr H_T^+.
\]

Für gerades `f` ist `h_T` ungerade. Daher

\[
\boxed{
\langle h_T,\mathbf1_T\rangle=0.
}
\tag{C1zB2C5a.4}
\]

Äquivalent:

\[
\boxed{
\langle J_{R,T}f,H_T\mathbf1_T\rangle=0
\qquad
(f\text{ gerade}).
}
\tag{C1zB2C5a.5}
\]

Damit ist der gesamte C3/C4-Variationskanal, der die exponentielle Boundary-Jet-Divergenz erzeugt hat, im geraden Source-Sektor **identisch blind**.

Dies ist stärker als die Aussage `beta_R^{(m)}(f)=0`: Es gilt bereits auf finite-level Operatorniveau durch Parität.

---

# 4. Zerlegung des Hubs: höhere Prime-Powers sind global harmlos

Schreibe

\[
H_T=H_T^{(1)}+H_T^{(\ge2)},
\]

wobei

\[
H_T^{(1)}
=P_T\sum_{p\le e^{2T}}
\sqrt{\log p}\,p^{-3/4}D_{\log p}E_T
\]

der primitive Hub ist und `H_T^{(>=2)}` die Kanäle `p^k`, `k>=2`, enthält.

Da

\[
\|D_s\|\le2
\]

und

\[
\sum_p\sum_{k\ge2}
\sqrt{\log p}\,p^{-3k/4}
=
\sum_p
\sqrt{\log p}\,
\frac{p^{-3/2}}{1-p^{-3/4}}
<\infty,
\]

gibt es eine absolute Konstante `C_hp<infty` mit

\[
\boxed{
\sup_T\|H_T^{(\ge2)}\|\le C_{\rm hp}<\infty.
}
\tag{C1zB2C5a.6}
\]

Da `0<A_T^{-1}<=I`, folgt für den höheren-Power-Anteil

\[
\boxed{
\langle (H_T^{(\ge2)})^*Jf,
A_T^{-1}(H_T^{(\ge2)})^*Jf\rangle
\le
C_{\rm hp}^2\|f\|_2^2.
}
\tag{C1zB2C5a.7}
\]

Mit

\[
\|x+y\|^2\le2\|x\|^2+2\|y\|^2
\]

reduziert sich die Frage nach wachsender Terminalenergie daher auf den **primitiven Hub** `H_T^{(1)}`.

Das ist wichtig: C5a benötigt keine neue Regularisierung der höheren Prime-Powers.

---

# 5. Der primitive Restoperator explizit

Für `p` setze

\[
a_p:=\frac12\log p.
\]

Aus C1z-B gilt

\[
\mathsf Q_T(u)\eta_{p,1}
=
1_{\{|u|\le T-a_p\}}\eta_{p,1}
\]

und

\[
\|\eta_{p,1}\|^2=1-\frac1p.
\]

Der primitive Restteil lautet daher

\[
R_T^{(1)}e
=
\bigoplus_{p\le e^{2T}}
\sqrt{\log p}\,p^{-1/4}
\,1_{\{|u|\le T-a_p\}}
D_{\log p}E_Te
\otimes\eta_{p,1}.
\]

Wegen der Orthogonalität verschiedener `K_p^0`-Sektoren:

\[
\boxed{
\|R_T^{(1)}e\|^2
=
\sum_{p\le e^{2T}}
\frac{\log p}{\sqrt p}
\left(1-\frac1p\right)
\left\|
1_{\{|u|\le T-a_p\}}D_{\log p}E_Te
\right\|_2^2.
}
\tag{C1zB2C5a.8}
\]

Diese Formel ist die natürliche positive Frameenergie, gegen die der primitive Hub getestet werden muss.

---

# 6. Satz C5a.1 — keine primitive Restnullmode im ungeraden Sektor

## Aussage

Sei

\[
T>\frac12(\log2+\log3).
\]

Dann gilt

\[
\boxed{
\ker R_T^{(1)}\cap\mathscr H_T^-\ =\ \{0\}.
}
\tag{C1zB2C5a.9}
\]

Mehr noch: Auf dem gesamten Source-Raum besteht die primitive Restnullmenge nur aus konstanten Funktionen:

\[
\boxed{
\ker R_T^{(1)}=\mathbb C\mathbf1_T.
}
\tag{C1zB2C5a.10}
\]

## Beweis

Sei `R_T^{(1)}e=0`. Wegen der orthogonalen Primsektoren muss jeder einzelne primitive Kanal verschwinden.

Insbesondere für `p=2`:

\[
D_{\log2}E_Te(u)=0
\quad\text{für }|u|\le T-\tfrac12\log2.
\]

Mit `x=u-\tfrac12\log2` folgt

\[
\boxed{
e(x+\log2)=e(x)
\quad\text{für fast alle }x\in(-T,T-\log2).
}
\tag{C1zB2C5a.11}
\]

Somit ist `e` auf `(-T,T)` die Restriktion einer `log2`-periodischen messbaren Funktion `g` auf `R`.

Analog liefert `p=3`

\[
\boxed{
e(x+\log3)=e(x)
\quad\text{für fast alle }x\in(-T,T-\log3).
}
\tag{C1zB2C5a.12}
\]

Das Intervall `(-T,T-log3)` besitzt nach der angenommenen Schranke Länge größer als `log2`. Daher enthält es ein volles `log2`-Periodenintervall. Da sowohl

\[
x\mapsto g(x)
\]

als auch

\[
x\mapsto g(x+\log3)
\]

`log2`-periodisch sind und auf einem vollen Periodenintervall übereinstimmen, gilt

\[
g(x+\log3)=g(x)
\qquad\text{für fast alle }x\in\mathbb R.
\]

Also besitzt `g` die beiden Perioden

\[
\log2,\qquad\log3.
\]

Da

\[
\frac{\log2}{\log3}\notin\mathbb Q
\]

(`2^m=3^n` ist für positive ganze `m,n` unmöglich), erzeugen diese Perioden eine dichte additive Untergruppe von `R`. Durch Stetigkeit der Translationen in `L^2_{loc}` folgt, dass `g` unter **allen** reellen Translationen invariant ist. Also ist `g` fast überall konstant.

Damit ist `e` auf `(-T,T)` konstant. Ist `e` zusätzlich ungerade, muss diese Konstante null sein. `□`

## Interpretation

Dies ist die exakte Paritätsgegenhälfte von C3:

\[
\boxed{
\text{gerade Variationsmode }\mathbf1_T
\text{ ist primitive Restnullmode;}
}
\]

aber

\[
\boxed{
\text{im ungeraden Variationsraum existiert keine nichttriviale primitive Restnullmode.}
}
\]

Der C3-Mechanismus kann daher nicht einfach mit einer ungeraden Ersatzmode wiederholt werden.

Status: `✓[M]`.

---

# 7. Ein kanonischer ungerader Test wird tatsächlich stark gescreent

Der natürlichste ungerade Gegenpart zu `1_T` ist

\[
\boxed{
s_T(u):=\operatorname{sgn}(u),\qquad |u|<T.}
\tag{C1zB2C5a.13}
\]

Wir zeigen, dass dieser Test **keine** gerade Source-Divergenz erzeugt.

Fixiere

\[
0<r_0<r_1<\infty.
\]

Für Primzahlen mit

\[
T-r_1\le a_p\le T-r_0
\]

ist

\[
r_p:=T-a_p\in[r_0,r_1].
\]

Für großes `T` gilt `a_p>r_1`. Auf dem primitiven Overlapbereich

\[
|u|\le r_p
\]

liegen dann `u+a_p>0` und `u-a_p<0`. Also

\[
D_{\log p}E_Ts_T(u)=2
\]

bis auf die irrelevante Vorzeichenkonvention von `D_s`; für die Norm gilt jedenfalls

\[
\left\|1_{|u|\le r_p}D_{\log p}E_Ts_T\right\|_2^2
=8r_p
\ge8r_0.
\]

Aus (C1zB2C5a.8):

\[
\|R_T^{(1)}s_T\|^2
\ge
8r_0
\sum_{e^{2(T-r_1)}\le p\le e^{2(T-r_0)}}
\frac{\log p}{\sqrt p}
\left(1-\frac1p\right).
\]

Mit PNT/partieller Summation:

\[
\sum_{A<p\le B}\frac{\log p}{\sqrt p}
\asymp 2(\sqrt B-\sqrt A)
\]

für die hier festen multiplikativen Fenster. Daher existiert `c_{r_0,r_1}>0` mit

\[
\boxed{
\|R_T^{(1)}s_T\|^2
\ge c_{r_0,r_1}e^T
\qquad(T\gg1).
}
\tag{C1zB2C5a.14}
\]

Andererseits gilt für festes `f in L^1(-R,R)`:

\[
|\langle J_{R,T}f,H_T^{(1)}s_T\rangle|
\le
2\|f\|_1
\sum_{p\le e^{2T}}
\sqrt{\log p}\,p^{-3/4}.
\]

PNT/partielle Summation liefert

\[
\boxed{
\sum_{p\le e^{2T}}
\sqrt{\log p}\,p^{-3/4}
=O\!\left(\frac{e^{T/2}}{\sqrt T}\right).
}
\tag{C1zB2C5a.15}
\]

Somit

\[
|\langle Jf,H_T^{(1)}s_T\rangle|^2
=O_f\!\left(\frac{e^T}{T}\right).
\]

Da

\[
\|s_T\|_2^2+\|R_Ts_T\|^2
\ge\|R_T^{(1)}s_T\|^2
\gtrsim e^T,
\]

folgt für den zu `s_T` gehörigen Variationsquotienten

\[
\boxed{
\frac{|\langle Jf,H_Ts_T\rangle|^2}
{\|s_T\|_2^2+\|R_Ts_T\|^2}
=O_f(T^{-1})+O_f(e^{-T})
\longrightarrow0.
}
\tag{C1zB2C5a.16}
\]

Der `O(e^{-T})`-Zusatz steht nur für den global beschränkten höheren-Power-Hub aus §4.

### Bedeutung

Die kanonische ungerade Mode `sgn(u)` ist **nicht** der gerade Analogon-Zeuge zu `1_T`.

Sie wird durch die primitive Restgeometrie exponentiell stark gesehen und nach Feshbach-Elimination asymptotisch vollständig gescreent.

Status: `✓[M]` für diesen Testvektor.

**Firewall:** Ein einzelner gescreenter Variationsvektor beweist noch keine uniforme Kontrolle des Suprema in (C1zB2C5a.3).

---

# 8. Warum qualitative Injektivität noch keine uniforme Koerzivität ist

Satz C5a.1 zeigt

\[
R_T^{(1)}|_{\mathscr H_T^-}
\text{ ist injektiv}.
\]

Daraus folgt **nicht** automatisch eine Schranke

\[
\|e\|_2^2
\le C\|R_T^{(1)}e\|^2
\qquad(e\in\mathscr H_T^-).
\]

Tatsächlich kann kein fester endlicher Primblock eine solche Koerzivität liefern.

---

# 9. Satz C5a.2 — kein fester endlicher Primblock ist koerziv

Sei

\[
F=\{p_1,\ldots,p_N\}
\]

eine feste endliche Primmenge und `T` so groß, dass alle ihre Overlapintervalle nichtleer sind.

Definiere die endliche primitive Rest-Seminorm

\[
\mathcal E_{F,T}(e)
:=
\sum_{p\in F}
\frac{\log p}{\sqrt p}
\left(1-\frac1p\right)
\left\|
1_{|u|\le T-a_p}D_{\log p}e
\right\|_2^2.
\]

Dann existiert eine Folge ungerader Funktionen

\[
e_n(u)=\sin(\xi_nu)
\]

mit

\[
\|e_n\|_{L^2(-T,T)}\asymp_T1
\]

und

\[
\boxed{
\mathcal E_{F,T}(e_n)\longrightarrow0.
}
\tag{C1zB2C5a.17}
\]

## Beweis

Für jedes `p in F` gilt auf dem Overlapbereich

\[
D_{\log p}e_n(u)
=
2\cos(\xi_nu)
\sin\!\left(\frac{\xi_n\log p}{2}\right)
\]

bis auf die Konvention der Translationen. Daher

\[
\left\|1_{|u|\le T-a_p}D_{\log p}e_n\right\|_2
\le
C_T
\left|
\sin\!\left(\frac{\xi_n\log p}{2}\right)
\right|.
\]

Durch simultane Dirichlet-Approximation der endlich vielen reellen Zahlen

\[
\frac{\log p_j}{2\pi}
\]

existiert eine Folge `xi_n -> infinity`, für die

\[
\operatorname{dist}\!\left(
\frac{\xi_n\log p_j}{2\pi},\mathbb Z
\right)\to0
\qquad(j=1,\ldots,N).
\]

Also gehen alle Sinusfaktoren gleichzeitig gegen null. Damit folgt (C1zB2C5a.17). `□`

### Konsequenz

Die quantitative Kontrolle des geraden Kanals kann nicht aus `p=2,3` oder irgendeiner anderen **festen endlichen** Familie stammen.

Die Inkommensurabilität von `log2` und `log3` beseitigt nur den exakten Nullraum. Für eine quantitative Feshbach-Schranke muss die **mit `T` wachsende Gesamtfamilie der Primtranslationen** benutzt werden.

Status:

\[
\boxed{\checkmark[M]_{\rm neg,finite\text{-}prime\text{-}coercivity}.}
\]

---

# 10. Der exakte noch fehlende Satz: Prime-Frame-Ungleichung

Für gerades festes

\[
f\in\mathcal K_{X,R}^+
\]

definiere das primitive Hubfunktional auf dem ungeraden Terminalraum:

\[
\boxed{
\mathcal L_{T,f}^{\rm prim}(e)
:=
\langle J_{R,T}f,H_T^{(1)}e\rangle,
\qquad e\in\mathscr H_T^-.
}
\tag{C1zB2C5a.18}
\]

Nach §4 genügt für uniforme Terminalbeschränktheit des geraden Kanals eine `T`-unabhängige Schranke

\[
\boxed{
|\mathcal L_{T,f}^{\rm prim}(e)|^2
\le
C_{R,f}
\left(
\|e\|_2^2+\|R_T^{(1)}e\|^2
\right)
}
\tag{C1zB2C5a.19}
\]

für alle

\[
T>R,
\qquad
e\in\mathscr H_T^-.
\]

Denn dann liefert (C1zB2C5a.3) zusammen mit dem höheren-Power-Bound

\[
\sup_{T>R}\sigma_T(J_{R,T}f)<\infty.
\]

Die linke Seite ist explizit

\[
\mathcal L_{T,f}^{\rm prim}(e)
=
\sum_{p\le e^{2T}}
\sqrt{\log p}\,p^{-3/4}
\left\langle J_{R,T}f,
P_TD_{\log p}E_Te
\right\rangle.
\tag{C1zB2C5a.20}
\]

Die rechte positive Prime-Frame-Energie ist exakt (C1zB2C5a.8).

Damit ist der fehlende Satz keine abstrakte „Koerzivität“ mehr, sondern die konkrete gewichtete Frameabschätzung

\[
\boxed{
\left|
\sum_{p\le e^{2T}}
\sqrt{\log p}\,p^{-3/4}
\langle Jf,D_{\log p}e\rangle
\right|^2
\ \lesssim_{R,f}\ 
\|e\|_2^2
+
\sum_{p\le e^{2T}}
\frac{\log p}{\sqrt p}
\left(1-\frac1p\right)
\left\|1_{|u|\le T-a_p}D_{\log p}e\right\|_2^2
}
\tag{C1zB2C5a.21}
\]

für **ungerade** `e`.

Diese Ungleichung ist source-windowed, nichttranslationinvariant und verwendet genau die bereits kanonischen Weil-/BC-Gewichte. Es wird kein neuer Regulator eingeführt.

---

# 11. Warum die triviale primweise Cauchy-Schwarz-Schranke nicht reicht

Auf Primzahlen, deren Overlapbereich den festen Träger von `f` vollständig enthält, kann man primweise

\[
|\langle f,D_{\log p}e\rangle|
\le
\|f\|_2
\left\|1_{|u|\le T-a_p}D_{\log p}e\right\|_2
\]

verwenden.

Das Verhältnis zwischen Hub- und Restgewicht ist

\[
\frac{
\sqrt{\log p}\,p^{-3/4}
}{
\sqrt{\log p}\,p^{-1/4}\sqrt{1-1/p}
}
=
\frac{p^{-1/2}}{\sqrt{1-1/p}}.
\]

Eine Cauchy-Schwarz-Summe über die Primzahlen produziert daher

\[
\sum_{p\le X}\frac1p,
\]

also logarithmisches Mertens-Wachstum.

Damit liefert die reine kanalweise Abschätzung höchstens einen wachsenden Framekonstanten-Kandidaten und **nicht** (C1zB2C5a.21) mit uniformem `C_{R,f}`.

Die noch benötigte Information muss also die gemeinsame Source-Geometrie der Translationen benutzen, nicht nur die Orthogonalität der p-adischen Zielsektoren.

---

# 12. Boundary-Shell-Skalierung erklärt, warum eine positive Ungleichung plausibel bleibt

Dieser Abschnitt ist eine strukturelle Skalierungsdiagnose, kein Ersatz für den fehlenden Beweis.

Parametrisiere große primitive Primzahlen durch

\[
a_p=T-r,
\qquad
r=T-\frac12\log p.
\]

Für festes `r=O(1)` entspricht dies

\[
p\asymp e^{2(T-r)}.
\]

Unter PNT besitzt die Hubsumme in einer festen `r`-Schale die Größenordnung

\[
\sqrt{\log p}\,p^{-3/4}\,d\pi(p)
\sim
\frac{e^{T/2}}{\sqrt T}e^{-r/2}\,dr,
\]

während die primitive Restenergie in derselben Schale die Größenordnung

\[
\frac{\log p}{\sqrt p}\,d\pi(p)
\sim
2e^Te^{-r}\,dr
\]

trägt.

Quadratisch besitzt die Hubskala daher relativ zur Restskala einen zusätzlichen Faktor

\[
\boxed{T^{-1}.}
\]

Genau dieses Verhältnis wurde im expliziten `sgn`-Test aus §7 sichtbar.

Das spricht dafür, dass terminale primitive Randkanäle im geraden Source-Sektor stark screenbar sein **könnten**. Aber um daraus eine uniforme Aussage über das Supremum in (C1zB2C5a.3) zu machen, braucht man eine echte diskrete Prime-Frame-/Large-Sieve-Abschätzung; reine PNT-Skalierung genügt nicht.

**Firewall:** Aus dieser Skalierungsdiagnose wird kein positiver Status für (C1zB2C5a.21) gebucht.

---

# 13. Konsequenz für die absolute gerade Terminalmetrik

Aus den bisherigen Sätzen folgt verbindlich:

1. der bekannte Boundary-Jet erzeugt im geraden Source-Sektor keinen Beitrag;
2. die einzige exakte primitive Restnullmode ist konstant und liegt im **geraden Variationsraum**, nicht im für gerades `f` relevanten ungeraden Variationsraum;
3. der natürlichste ungerade globale Test `sgn` wird asymptotisch vollständig gescreent;
4. höhere Prime-Powers sind uniform beschränkt;
5. eine feste endliche Primfamilie kann die notwendige quantitative Kontrolle nicht liefern.

Nicht entschieden ist:

\[
\boxed{
\sup_{T>R}
\langle G_{R,T}f,f\rangle_{X,R}<\infty
\qquad
\forall f\in\mathcal K_{X,R}^+.
}
\tag{C1zB2C5a.22}
\]

Diese Aussage ist äquivalent zu einer uniformen Kontrolle der Graphdualnormen in (C1zB2C5a.3); (C1zB2C5a.21) ist ein konkreter hinreichender und source-kanonischer Weg dazu.

---

# 14. Konsequenz für den relativen Terminaltransport

C5 hatte

\[
W_{R,S}^{[T]}=V_{S,T}^*V_{R,T}
\]

und den Cross-Terminal-Kern

\[
\mathscr K_{R,S}^{T,U}
=(W_{R,S}^{[T]})^*W_{R,S}^{[U]}
\]

isoliert.

Da alle beteiligten Operatoren die Parität respektieren,

\[
\boxed{
\mathscr K_{R,S}^{T,U}
=
\mathscr K_{R,S,+}^{T,U}
\oplus
\mathscr K_{R,S,-}^{T,U}.
}
\tag{C1zB2C5a.23}
\]

C5a zeigt nun, dass der gerade Kanal nicht durch den C3/C4-Boundary-Jet kontrolliert werden muss. Sein fehlender Input ist stattdessen die quantitative primitive Prime-Frame-Geometrie.

Falls (C1zB2C5a.21) in einer ausreichend starken tail-stabilen Form bewiesen wird und daraus für festes `R` ein positiver Grenzoperator

\[
G_{R,\infty}^+
\]

auf dem geraden Sektor folgt, dann ergibt sich der gerade relative Transport unmittelbar als

\[
W_{R,S,+}^{[\infty]}
=(G_{S,\infty}^+)^{1/2}
J_{R,S}^+
(G_{R,\infty}^+)^{-1/2}.
\]

Dies ist nur ein **konditionaler** Schluss. C5a behauptet den Grenzoperator noch nicht.

---

# 15. Statusmatrix

| Aussage | Status |
|---|---|
| Paritätsreduktion des Variationsproblems | `✓[M]` |
| `1_T` koppelt an gerades `f` | `×[M]` — exakt null |
| höhere Prime-Power-Hubanteile uniform beschränkt | `✓[M]` |
| explizite primitive Restenergie (Frameform) | `✓[M]` |
| `ker R_T^(1)=C 1_T` für genügend großes `T` | `✓[M]` |
| primitive Restnullmode im ungeraden Variationsraum | `×[M]` |
| `sgn` erzeugt gerade Terminaldivergenz | `×[M]` — Rayleighquotient `O(1/T)` |
| fester endlicher Primblock quantitativ koerziv | `×[M]` |
| wachsende Prime-Frame-Ungleichung (C1zB2C5a.21) | `?[O]` |
| absolute gerade Terminalmetrik uniform beschränkt | `?[O]` |
| gerader Cross-Terminal-Kern `->I` | `?[O]` |
| gerader relativer Transportlimes | `?[O]` |
| ungerader relativer Transportlimes | `?[O]` aus C5 |
| Objekt X / exakte Weil-Geometrie | `?[O]` |

---

# 16. Scope-Firewalls

C5a beweist **nicht**:

1. dass der gerade Terminalkanal beschränkt ist;
2. dass `G_{R,T}^+` konvergiert;
3. dass der relative Transport auf dem geraden Kanal konvergiert;
4. dass der ungerade Boundary-Jet im relativen Transport vollständig cancelt;
5. eine Large-Sieve-Ungleichung für Primlogarithmen;
6. eine Suzuki-/P04-Identifikation;
7. P10-O07;
8. Objekt X;
9. RH.

Der Knoten schließt nur falsche Kurzschlüsse aus und isoliert den exakten quantitativen Satz, der als nächstes benötigt wird.

---

# 17. Nächster atomarer Knoten

Der nächste Test ist nun erzwungen:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C5b]
\quad
\text{Prime-Frame / source-windowed Large-Sieve Audit}.
}
\]

Zu prüfen ist primär (C1zB2C5a.21), zunächst auf einem dichten geraden Testcore.

Eine sinnvolle Zerlegung ist:

### C5b-A — Bulk

Primzahlen mit

\[
\frac12\log p\le T-R,
\]

für die der gesamte Träger des alten Tests `f` im primitiven Overlapbereich liegt.

Hier ist die Schwierigkeit ausschließlich die gemeinsame Translationgeometrie; es gibt keinen Source-Randverlust.

### C5b-B — Boundary shell

Primzahlen mit

\[
T-R<\frac12\log p\le T.
\]

Hier muss die Source-Randgeometrie explizit benutzt werden. Die Skalierung aus §12 sagt einen relativen `1/T`-Gewinn voraus, beweist ihn aber noch nicht uniform.

### C5b-C — quantitative Frameentscheidung

Entweder:

\[
|\mathcal L_{T,f}^{prim}(e)|^2
\le C_{R,f}(\|e\|^2+\|R_T^{(1)}e\|^2)
\]

uniform in `T`, dann ist die absolute gerade Terminalenergie beschränkt;

oder es existiert eine explizite ungerade Quasi-Nullfolge `e_T`, die trotz der **wachsenden** Primfamilie das Hubfunktional groß hält. Dann wäre auch der gerade absolute Terminalkanal negativ entschieden.

In beiden Fällen wäre der nächste strukturelle Schritt scharf.

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal.
