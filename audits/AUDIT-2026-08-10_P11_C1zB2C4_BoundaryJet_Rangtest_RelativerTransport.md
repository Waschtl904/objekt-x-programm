# P11-C1z-B2-C4 — Boundary-Jet-Rangtest und relativer Terminaltransport

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C4]`  
**Vorgänger:** C1z-B2-C3  
**Schnittstellen:** C1z-B2-C2/C3; C1z-B/B1; P03-Haar-L2-Firewall  

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C4]
\quad
\checkmark[K/M]_{\rm part}
\;+
\checkmark[M]_{\rm neg,rank\text{-}one}
\;+
\checkmark[M]_{\rm neg,finite\text{-}jet}
}
\]

mit vier getrennten Befunden:

\[
\boxed{
\ker\beta_R\text{ ist nicht terminal beschränkt.}
}
\]

\[
\boxed{
\text{Die C3-Randmode }\beta_R\text{ ist nur der erste Koeffizient einer kanonischen unendlichen Rand-Jet-Hierarchie.}
}
\]

\[
\boxed{
\text{Kein endlicher Trunkat dieser kanonischen Randhierarchie stabilisiert die unrenormierte Terminalmetrik.}
}
\]

und

\[
\boxed{
W_{R,S}^{[T]}\xrightarrow[T\to\infty]{}W_{R,S}^{[\infty]}
\text{ bleibt }?[O],
}
\]

wobei die gesamte neue Rand-Jet-Hierarchie unter den nativen Nullfortsetzungen exakt pullback-kompatibel ist.

---

# 0. Urteil

C1z-B2-C3 hatte für jedes feste `R>0` eine kanonische Randfunktion

\[
\beta_R(f)
=
\int_{-R}^{R}
\operatorname{sgn}(u)
\bigl(1-e^{-|u|/2}\bigr)f(u)\,du
\]

isoliert und für geeignete `f` mit `beta_R(f)\ne0` gezeigt:

\[
\sigma_T(J_{R,T}f)
\gtrsim
\frac{e^T}{T^3}.
\]

Offen war der Rangtest:

\[
f\in\ker\beta_R
\stackrel?\Longrightarrow
\sup_{T>R}\langle G_{R,T}f,f\rangle_{X,R}<\infty.
\]

C4 entscheidet diese Frage **negativ**.

Der primitive Source-Randhub besitzt nicht nur einen führenden asymptotischen Koeffizienten, sondern auf jedem festen alten Source-Level eine vollständige asymptotische Entwicklung in Potenzen von `1/T`.

Definiere für `m>=0`

\[
\boxed{
I_m(r)
:=
\int_0^r s^m e^{-s/2}\,ds,
\qquad 0\le r\le R,
}
\tag{C1zB2C4.1}
\]

und die zugehörigen linearen Randfunktionale

\[
\boxed{
\beta_R^{(m)}(f)
:=
\int_{-R}^{R}
\operatorname{sgn}(u)
I_m(|u|)f(u)\,du.
}
\tag{C1zB2C4.2}
\]

Dann ist

\[
\beta_R^{(0)}=2\beta_R.
\]

Für jedes feste `M` besitzt die Hubkopplung an die C3-Konstantenmode `1_T` die uniforme Entwicklung

\[
\boxed{
\langle J_{R,T}f,H_T\mathbf1_T\rangle
=
-\sqrt2\,e^{T/2}T^{-1/2}
\sum_{m=0}^{M}
\frac{c_m}{T^m}\,\beta_R^{(m)}(f)
+
O_{R,M,f}\!\left(e^{T/2}T^{-M-3/2}\right),
}
\tag{C1zB2C4.3}
\]

mit

\[
\boxed{
c_m=\frac{\binom{2m}{m}}{4^m}}
\tag{C1zB2C4.4}
\]

(`c_0=1`, `c_1=1/2`, `c_2=3/8`, ...).

Daraus folgt:

Wenn

\[
\beta_R^{(0)}(f)=\cdots=\beta_R^{(m-1)}(f)=0,
\qquad
\beta_R^{(m)}(f)\ne0,
\]

so gilt

\[
\boxed{
\sigma_T(J_{R,T}f)
\ge
c_{R,f,m}\,
\frac{e^T}{T^{2m+3}}
\longrightarrow+\infty.
}
\tag{C1zB2C4.5}
\]

Insbesondere existiert `f in C_c^infty((-R,R))` mit

\[
\beta_R(f)=0
\]

aber

\[
\beta_R^{(1)}(f)\ne0,
\]

und für dieses `f`

\[
\boxed{
\sigma_T(J_{R,T}f)
\gtrsim
\frac{e^T}{T^5}
\to\infty.
}
\tag{C1zB2C4.6}
\]

Damit ist die C4-A-Hoffnung eines einzigen Rang-eins-Randkanals geschlossen.

Noch stärker: Für jedes endliche `M` gibt es Testvektoren, die die ersten `M` Randmoden auslöschen und dennoch durch die nächste Randmode exponentiell divergieren. Die Terminaldivergenz besitzt daher einen **kanonischen unendlichen asymptotischen Rand-Jet**.

Der relative finite-horizon Transport aus C2 bleibt trotzdem offen als möglicher Grenzträger. Die Rand-Jet-Funktionale erfüllen nämlich exakt

\[
\boxed{
\beta_S^{(m)}(J_{R,S}f)=\beta_R^{(m)}(f),
\qquad R<S,\ m\ge0.
}
\tag{C1zB2C4.7}
\]

Die Divergenz ist also nicht nur kanonisch, sondern bereits auf allen Source-Leveln **pullback-kompatibel**. Dies lässt eine relative Aufhebung im isometrischen Terminaltransport weiterhin zu, beweist sie aber nicht.

---

# 1. Verbindliche Daten aus C3

Fixiere `R>0` und `T>R`.

Die Zukunftsmetrik ist

\[
G_{R,T}=J_{R,T}^*J_{R,T}
\]

auf `K_{X,R}` und

\[
\boxed{
\langle G_{R,T}f,f\rangle_{X,R}
=
q_{\Gamma,R}(f)
+
\sigma_T(J_{R,T}f).
}
\tag{C1zB2C4.8}
\]

Der gesamte `T`-abhängige Anteil ist

\[
\boxed{
\sigma_T(g)
=
\langle H_T^*g,
A_T^{-1}H_T^*g\rangle,
\qquad
A_T:=I+R_T^*R_T.
}
\tag{C1zB2C4.9}
\]

C3 beweist mit

\[
\mathbf1_T:=1_{(-T,T)}
\]

die Variationsuntergrenze

\[
\boxed{
\sigma_T(J_{R,T}f)
\ge
\frac{|< J_{R,T}f,H_T\mathbf1_T\rangle|^2}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}.
}
\tag{C1zB2C4.10}
\]

Ferner gilt die terminale Screening-Schranke

\[
\boxed{
\langle\mathbf1_T,A_T\mathbf1_T\rangle
=O(T^2).
}
\tag{C1zB2C4.11}
\]

Der primitive konditionierte Rest verschwindet auf `1_T` exakt. Daher ist (C1zB2C4.11) bereits Feshbach-stabil und wird in C4 unverändert benutzt.

---

# 2. Exakte Source-Randform des Huboperators auf `1_T`

Für `u in (0,R)` und ein aktives Prime-Power-Label `n=p^k` mit

\[
p^k\le e^{2T}
\]

ist

\[
D_{\log n}E_T\mathbf1_T(u)
=
\begin{cases}
0,&\frac12\log n\le T-u,\\
-1,&T-u<\frac12\log n\le T.
\end{cases}
\]

Für `u in (-R,0)` ist das Vorzeichen umgekehrt.

Somit ist auf dem alten Source-Fenster `[-R,R]` exakt

\[
\boxed{
H_T\mathbf1_T(u)
=
-\operatorname{sgn}(u)\,
\Phi_T(|u|),
}
\tag{C1zB2C4.12}
\]

mit

\[
\boxed{
\Phi_T(r)
:=
\sum_{\substack{p^k:\\
 e^{2(T-r)}<p^k\le e^{2T}}}
\sqrt{\log p}\,p^{-3k/4},
\qquad 0\le r\le R.
}
\tag{C1zB2C4.13}
\]

Damit

\[
\boxed{
\langle J_{R,T}f,H_T\mathbf1_T\rangle
=
-\int_{-R}^{R}
\operatorname{sgn}(u)\Phi_T(|u|)f(u)\,du.
}
\tag{C1zB2C4.14}
\]

Dies zeigt bereits eine wichtige Paritätsstruktur:

\[
H_T\mathbf1_T|_{[-R,R]}
\text{ ist ungerade.}
\]

Der in C3/C4 sichtbare Boundary-Jet lebt daher zunächst im ungeraden Source-Sektor.

**Firewall:** Daraus folgt nicht, dass der gerade Sektor terminal beschränkt ist. C4 untersucht nur den durch die kanonische Konstantenmode detektierten Rand-Jet.

---

# 3. Höhere Prime-Powers sind für den Boundary-Jet exponentiell klein

Zerlege

\[
\Phi_T(r)=\Phi_T^{(1)}(r)+\Phi_T^{(\ge2)}(r),
\]

wobei

\[
\Phi_T^{(1)}(r)
=
\sum_{e^{2(T-r)}<p\le e^{2T}}
\sqrt{\log p}\,p^{-3/4}.
\]

Für `k>=2` liegt aus

\[
e^{2(T-r)}<p^k\le e^{2T}
\]

die Primzahl in einem Fenster

\[
e^{2(T-r)/k}<p\le e^{2T/k}.
\]

Schon `k=2` liefert mit PNT/partieller Summation

\[
\sum_{e^{T-r}<p\le e^T}
\sqrt{\log p}\,p^{-3/2}
=O_R\!\left(\frac{e^{-T/2}}{\sqrt T}\right).
\]

Die Beiträge `k>=3` sind noch kleiner; die endliche Zahl möglicher `k` bis `O(T)` ändert die Exponentialordnung nicht.

Daher, uniform für `0<=r<=R`,

\[
\boxed{
\Phi_T^{(\ge2)}(r)
=O_R\!\left(e^{-T/2}T^C\right)
}
\tag{C1zB2C4.15}
\]

für eine feste harmlose Potenz `C`.

Insbesondere sind höhere Prime-Powers gegenüber jeder Ordnung

\[
e^{T/2}T^{-N}
\]

des primitiven Boundary-Jets vernachlässigbar.

---

# 4. Vollständige asymptotische Entwicklung des primitiven Primrandes

Setze

\[
F(x):=x^{-3/4}(\log x)^{-1/2}.
\]

Mit der Chebyshev-Funktion

\[
\vartheta(x)=\sum_{p\le x}\log p
\]

schreibt sich

\[
\Phi_T^{(1)}(r)
=
\int_{e^{2(T-r)}}^{e^{2T}}
F(x)\,d\vartheta(x).
\]

Wir benutzen die klassische unbedingte PNT-Fehlerform

\[
\vartheta(x)
=x+O\!\left(xe^{-c\sqrt{\log x}}\right)
\]

für ein `c>0`.

Partielle Integration zeigt auf jedem festen Multiplikativfenster `r in [0,R]`:

\[
\Phi_T^{(1)}(r)
=
\int_{e^{2(T-r)}}^{e^{2T}}
\frac{x^{-3/4}}{\sqrt{\log x}}\,dx
+
O_R\!\left(e^{T/2}e^{-c'\sqrt T}\right).
\tag{C1zB2C4.16}
\]

Mit

\[
x=e^{2v},\qquad dx=2e^{2v}dv
\]

wird der Hauptterm exakt

\[
\sqrt2
\int_{T-r}^{T}
e^{v/2}v^{-1/2}\,dv.
\]

Setze `s=T-v`. Dann

\[
\boxed{
\Phi_T^{(1)}(r)
=
\sqrt2\,e^{T/2}T^{-1/2}
\int_0^r
e^{-s/2}
\left(1-\frac{s}{T}\right)^{-1/2}ds
+
O_R\!\left(e^{T/2}e^{-c'\sqrt T}\right).
}
\tag{C1zB2C4.17}
\]

Für festes `R` ist die Binomialentwicklung uniform:

\[
\left(1-\frac{s}{T}\right)^{-1/2}
=
\sum_{m=0}^{M}
\frac{c_m s^m}{T^m}
+O_{R,M}(T^{-M-1}),
\]

mit

\[
c_m=\frac{\binom{2m}{m}}{4^m}.
\]

Definiere

\[
I_m(r)=\int_0^r s^m e^{-s/2}ds.
\]

Dann folgt uniform auf `0<=r<=R`:

\[
\boxed{
\Phi_T(r)
=
\sqrt2\,e^{T/2}T^{-1/2}
\sum_{m=0}^{M}
\frac{c_m}{T^m}I_m(r)
+
O_{R,M}\!\left(e^{T/2}T^{-M-3/2}\right).
}
\tag{C1zB2C4.18}
\]

Dabei wurden (C1zB2C4.15) und der PNT-Fehler absorbiert.

Für `M=0` ist

\[
I_0(r)=2(1-e^{-r/2}),
\]

und (C1zB2C4.18) reproduziert exakt den C3-Hauptterm

\[
2\sqrt2(1-e^{-r/2})\frac{e^{T/2}}{\sqrt T}.
\]

C4 ist damit eine echte Verfeinerung, keine Änderung von C3.

---

# 5. Kanonische Boundary-Jet-Funktionale

Für `m>=0` definiere auf `K_{X,R}` zunächst auf dem Testkern

\[
\boxed{
\beta_R^{(m)}(f)
:=
\int_{-R}^{R}
\operatorname{sgn}(u)I_m(|u|)f(u)\,du.
}
\tag{C1zB2C4.19}
\]

Da die Gewichtsfunktion

\[
w_{R,m}(u)
:=\operatorname{sgn}(u)I_m(|u|)
\]

auf `[-R,R]` beschränkt ist,

\[
|\beta_R^{(m)}(f)|
\le
\|w_{R,m}\|_2\|f\|_2
\le
\|w_{R,m}\|_2\|f\|_{X,R}.
\]

Somit erweitert sich jedes `beta_R^(m)` eindeutig zu einem beschränkten linearen Funktional auf `K_{X,R}`.

Für `m=0`:

\[
I_0(r)=2(1-e^{-r/2}),
\]

also

\[
\boxed{
\beta_R^{(0)}=2\beta_R.
}
\tag{C1zB2C4.20}
\]

Die C3-Randmode ist damit exakt der **0-te Rand-Jet-Koeffizient**.

---

# 6. Asymptotische Hubkopplung als Boundary-Jet

Setzt man (C1zB2C4.18) in (C1zB2C4.14) ein, erhält man für jedes feste `M` und `f in K_{X,R}` mit zunächst `f` im Testkern:

\[
\boxed{
\langle J_{R,T}f,H_T\mathbf1_T\rangle
=
-\sqrt2\,e^{T/2}T^{-1/2}
\sum_{m=0}^{M}
\frac{c_m}{T^m}\beta_R^{(m)}(f)
+
O_{R,M}\!\left(
\|f\|_1 e^{T/2}T^{-M-3/2}
\right).
}
\tag{C1zB2C4.21}
\]

Da auf dem festen Intervall

\[
\|f\|_1\le\sqrt{2R}\|f\|_2\le\sqrt{2R}\|f\|_{X,R},
\]

ist die Fehlerkontrolle auch graphnormstetig.

---

# 7. Allgemeiner Divergenzsatz nach Auslöschung endlich vieler Randmoden

## Satz C1zB2C4.1 — Boundary-Jet-Divergenz

Sei `m>=0` und

\[
f\in\mathcal K_{X,R}
\]

mit

\[
\beta_R^{(0)}(f)=\cdots=\beta_R^{(m-1)}(f)=0,
\]

aber

\[
\beta_R^{(m)}(f)\ne0.
\]

Dann

\[
\boxed{
\langle J_{R,T}f,H_T\mathbf1_T\rangle
=
-\sqrt2\,c_m\beta_R^{(m)}(f)
\frac{e^{T/2}}{T^{m+1/2}}
\bigl(1+O_{R,f,m}(T^{-1})\bigr).
}
\tag{C1zB2C4.22}
\]

Mit der C3-Variationsungleichung und

\[
\langle\mathbf1_T,A_T\mathbf1_T\rangle=O(T^2)
\]

folgt

\[
\boxed{
\sigma_T(J_{R,T}f)
\ge
c_{R,f,m}
\frac{e^T}{T^{2m+3}}
\to+\infty.
}
\tag{C1zB2C4.23}
\]

Dies ist Feshbach-stabil, da derselbe vollständige Nenner `A_T^{-1}` wie in C3 verwendet wird.

---

# 8. C4-A negativ: `ker beta_R` ist nicht terminal beschränkt

Wir müssen nur einen Testvektor konstruieren mit

\[
\beta_R^{(0)}(f)=0,
\qquad
\beta_R^{(1)}(f)\ne0.
\]

Die beiden Gewichtsfunktionen auf `(0,R)` sind

\[
I_0(r)=2(1-e^{-r/2})
\]

und

\[
I_1(r)=\int_0^r se^{-s/2}ds.
\]

Sie sind nicht proportional. Tatsächlich:

\[
I_0'(r)=e^{-r/2},
\qquad
I_1'(r)=re^{-r/2}.
\]

Wären `I_1=lambda I_0`, so würde `r=lambda` auf einem Intervall gelten — unmöglich.

Daher existieren `0<a<b<R` mit

\[
\det
\begin{pmatrix}
I_0(a)&I_0(b)\\
I_1(a)&I_1(b)
\end{pmatrix}
\ne0.
\]

Wähle zwei nichtnegative schmale Glattbumps

\[
\varphi_a,\varphi_b\in C_c^\infty((0,R))
\]

um `a` und `b`. Für hinreichend schmale Supports bleibt die entsprechende Momentmatrix invertierbar.

Daher gibt es Koeffizienten `x,y`, nicht beide null, so dass

\[
f=x\varphi_a+y\varphi_b
\]

erfüllt

\[
\beta_R^{(0)}(f)=0
\]

aber

\[
\beta_R^{(1)}(f)\ne0.
\]

Nach Satz C1zB2C4.1 mit `m=1`:

\[
\boxed{
\sigma_T(J_{R,T}f)
\ge
c_f\frac{e^T}{T^5}
\to+\infty.
}
\tag{C1zB2C4.24}
\]

Da `beta_R^(0)=2 beta_R`, gilt

\[
\boxed{
f\in\ker\beta_R
\quad\text{aber}\quad
\sup_{T>R}\langle G_{R,T}f,f\rangle_{X,R}=\infty.
}
\tag{C1zB2C4.25}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm neg,rank\text{-}one}.}
\]

Die C3-Divergenz ist daher **nicht** durch einen einzigen Randfreiheitsgrad erschöpft.

---

# 9. Die Randhierarchie ist unendlichdimensional

Die Funktionen

\[
I_m(r)=\int_0^r s^m e^{-s/2}ds
\]

sind auf jedem Intervall `(0,R)` linear unabhängig.

Denn aus

\[
\sum_{m=0}^{M}a_mI_m(r)=0
\qquad\forall r\in(0,R)
\]

folgt nach Differentiation

\[
e^{-r/2}
\sum_{m=0}^{M}a_mr^m=0.
\]

Also ist das Polynom identisch null und

\[
a_0=\cdots=a_M=0.
\]

Somit sind auch die Funktionale

\[
\boxed{
\beta_R^{(0)},\beta_R^{(1)},\beta_R^{(2)},\ldots
}
\tag{C1zB2C4.26}
\]

auf dem ungeraden Testsektor linear unabhängig.

Für jedes `M>=1` kann man daher durch `M+1` geeignete Glattbumps ein `f_M` konstruieren mit

\[
\boxed{
\beta_R^{(0)}(f_M)=\cdots=\beta_R^{(M-1)}(f_M)=0,
\qquad
\beta_R^{(M)}(f_M)\ne0.
}
\tag{C1zB2C4.27}
\]

Nach Satz C1zB2C4.1:

\[
\boxed{
\sigma_T(J_{R,T}f_M)
\gtrsim
\frac{e^T}{T^{2M+3}}
\to+\infty.
}
\tag{C1zB2C4.28}
\]

Da die Exponentialskala `e^T` jede feste Potenz von `T` dominiert, beseitigt das Auslöschen beliebig vieler **endlich vieler** asymptotischer Randkoeffizienten die Divergenz nicht.

Status:

\[
\boxed{\checkmark[M]_{\rm neg,finite\text{-}jet}.}
\]

---

# 10. Konsequenz: kein endlicher kanonischer Boundary-Jet-Quotient genügt

Definiere für `M>=1` den natürlichen endlichen relativen Kern

\[
\boxed{
\mathcal R_{R,M}
:=
\bigcap_{m=0}^{M-1}
\ker\beta_R^{(m)}.
}
\tag{C1zB2C4.29}
\]

Dies ist ein abgeschlossener Unterraum von endlicher Kodimension in `K_{X,R}`.

Aus §9 existiert

\[
f_M\in\mathcal R_{R,M}
\]

mit

\[
\langle G_{R,T}f_M,f_M\rangle_{X,R}\to\infty.
\]

Daher

\[
\boxed{
\sup_{T>R}
\|G_{R,T}|_{\mathcal R_{R,M}}\|
=\infty
\qquad\forall M<\infty.
}
\tag{C1zB2C4.30}
\]

Somit ist nicht nur der Rang-eins-Quotient unzureichend. **Jeder endliche Trunkat der durch die Primzahlschalengeometrie selbst erzwungenen Boundary-Jet-Hierarchie ist unzureichend.**

**Scope-Firewall:** Dies ist kein No-Go gegen einen unendlichen relativen Randraum, eine unbeschränkte Terminalform oder einen relativen Transportlimes. Es sagt nur: Die C3/C4-Randdivergenz lässt sich nicht durch endlich viele dieser kanonischen asymptotischen Randmoden entfernen.

---

# 11. Exakte Pullback-Kompatibilität des gesamten Boundary-Jets

Sei `R<S` und

\[
J_{R,S}:\mathcal K_{X,R}\to\mathcal K_{X,S}
\]

die native Nullfortsetzung.

Da die Gewichtsfunktion

\[
\operatorname{sgn}(u)I_m(|u|)
\]

unabhängig vom Source-Level definiert ist, gilt für `f` auf `[-R,R]` exakt

\[
\begin{aligned}
\beta_S^{(m)}(J_{R,S}f)
&=
\int_{-S}^{S}
\operatorname{sgn}(u)I_m(|u|)
(E_{R,S}f)(u)du\\
&=
\int_{-R}^{R}
\operatorname{sgn}(u)I_m(|u|)f(u)du.
\end{aligned}
\]

Also

\[
\boxed{
\beta_S^{(m)}J_{R,S}
=\beta_R^{(m)}
\qquad\forall m\ge0.
}
\tag{C1zB2C4.31}
\]

Dies ist ein echter positiver Kohärenzbefund.

Die neue Divergenzhierarchie ist **kein Level-für-Level-Artefakt**. Sie ist bereits ein natürliches kontravariantes Randdatum des gerichteten Source-Systems.

Für die endlichen relativen Kerne folgt

\[
\boxed{
J_{R,S}(\mathcal R_{R,M})
\subseteq
\mathcal R_{S,M}.
}
\tag{C1zB2C4.32}
\]

Damit sind sogar die endlichen Boundary-Jet-Quotienten algebraisch kohärent — sie reichen analytisch nur nicht zur Terminalstabilisierung.

---

# 12. Paritätsstruktur des Boundary-Jets

Alle Gewichte

\[
w_m(u):=\operatorname{sgn}(u)I_m(|u|)
\]

sind ungerade.

Daher hängt

\[
\beta_R^{(m)}(f)
\]

nur vom ungeraden Anteil von `f` ab:

\[
\boxed{
\beta_R^{(m)}(f)
=
\int_0^R I_m(r)
\bigl(f(r)-f(-r)\bigr)dr.
}
\tag{C1zB2C4.33}
\]

Insbesondere

\[
f\text{ gerade}
\quad\Longrightarrow\quad
\beta_R^{(m)}(f)=0
\quad\forall m.
\]

**Firewall:** C4 beweist nicht, dass gerade Testfunktionen terminal beschränkt sind. Der Konstantenmode-Test `1_T` detektiert nur den ungeraden Boundary-Jet. Ein möglicher gerader Divergenzkanal müsste durch einen anderen Variationsvektor im Feshbach-Nenner untersucht werden.

Dies verhindert eine unzulässige Schlussfolgerung

\[
\bigcap_{m\ge0}\ker\beta_R^{(m)}
\stackrel?=\text{terminal beschränkter Kern}.
\]

---

# 13. Konsequenz für die ursprüngliche C4-B-Rang-eins-Idee

C3 hatte als nächsten möglichen Schritt einen von `beta_R` bestimmten Quotienten beziehungsweise eine orthogonale Relativebene vorgeschlagen — **nur falls** C4-A positiv ausfiele.

C4-A ist negativ.

Daher ist die konkrete Rang-eins-Route

\[
\mathcal K_{X,R}
\longrightarrow
\mathcal K_{X,R}/\ker\beta_R
\]

beziehungsweise das Abziehen eines einzigen `|beta_R><beta_R|`-artigen Randterms **nicht** gerechtfertigt.

Noch stärker ist auch

\[
\mathcal R_{R,M}
=
\bigcap_{m<M}\ker\beta_R^{(m)}
\]

für kein endliches `M` terminal beschränkt.

Somit lautet der korrekte neue Randgegenstand nicht

\[
\boxed{\text{eine Randmode}}
\]

sondern mindestens

\[
\boxed{\text{ein unendlicher asymptotischer Boundary-Jet}.}
\]

Es wird hier **kein** Hilbertraum für diesen unendlichen Jet rückwärts gewählt. Insbesondere werden keine willkürlichen `ell^2`-Gewichte auf die Folge `beta_R^(m)` gelegt.

---

# 14. C4-C: Relativer Terminaltransport bleibt logisch offen

Der finite-horizon Transport aus C2 ist

\[
\boxed{
W_{R,S}^{[T]}
=
G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2},
\qquad R<S<T.
}
\tag{C1zB2C4.34}
\]

Für jedes feste `T` ist `W_{R,S}^{[T]}` eine Isometrie und die Familie erfüllt den exakten finite-horizon Kokyklus.

C3/C4 zeigen

\[
\|G_{R,T}\|\to\infty
\]

und sogar eine unendliche Hierarchie divergenter Randkoeffizienten.

Daraus folgt **nicht** automatisch

\[
W_{R,S}^{[T]}\not\to W_{R,S}^{[\infty]}.
\]

Denn die Randfunktionale selbst sind pullback-kompatibel:

\[
\beta_S^{(m)}J_{R,S}=\beta_R^{(m)}.
\]

Damit bleibt mathematisch möglich, dass die divergenten Terminalmetriken auf Source- und Target-Seite dieselbe Boundary-Jet-Geometrie tragen und sich im relativen Faktor

\[
G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}
\]

aufheben.

Status:

\[
\boxed{?[O].}
\]

C4 liefert also **keinen** Negativbefund gegen den relativen Terminaltransport.

---

# 15. Konditionaler Satz: Ein starker relativer Grenzwert wäre automatisch der richtige Kokyklus

Angenommen, für alle festen `R<S` existiert

\[
\boxed{
W_{R,S}^{[T]}
\xrightarrow[T\to\infty]{\rm strong}
W_{R,S}^{[\infty]}.
}
\tag{C1zB2C4.35}
\]

Da jedes `W_{R,S}^{[T]}` isometrisch ist,

\[
\|W_{R,S}^{[T]}f\|_{X,S}=\|f\|_{X,R}.
\]

Starke Konvergenz liefert deshalb

\[
\boxed{
\|W_{R,S}^{[\infty]}f\|_{X,S}=\|f\|_{X,R},
}
\tag{C1zB2C4.36}
\]

also ist der Grenzoperator selbst isometrisch.

Für `R<S<U` gilt für jedes `T>U` exakt

\[
W_{S,U}^{[T]}W_{R,S}^{[T]}
=W_{R,U}^{[T]}.
\]

Alle Faktoren haben Norm `1`. Daher erlaubt starke Konvergenz den Produktgrenzübergang:

\[
\boxed{
W_{S,U}^{[\infty]}W_{R,S}^{[\infty]}
=W_{R,U}^{[\infty]}.
}
\tag{C1zB2C4.37}
\]

Somit wäre jeder starke relative Terminalgrenzwert **automatisch** ein kohärentes isometrisches Induktivsystem.

Der schwierige Teil ist ausschließlich die Existenz des starken Grenzwerts.

---

# 16. Schwache Teilfolgen reichen nicht

Für feste `R<S` gilt

\[
\|W_{R,S}^{[T]}\|=1.
\]

Damit besitzt die Familie im Weak-Operator-Sinn Teilgrenzwerte entlang Netzen; bei den hier separablen Hilberträumen kann man entlang geeigneter Folgen schwache Teilfolgen extrahieren.

Ein schwacher Grenzwert einer Isometrienfolge muss jedoch nur eine Kontraktion sein. Normerhalt und Kokyklus gehen daraus nicht automatisch hervor.

Daher ist

\[
\boxed{
\text{WOT-Präkompaktheit kein Ersatz für den gesuchten starken relativen Grenzwert.}
}
\tag{C1zB2C4.38}
\]

---

# 17. Was jetzt positiv konstruiert ist

Nach C4 besitzt der C1z-Strang folgende robuste Daten:

1. finite-level Graphräume `K_{X,R}`;
2. bounded injective native Transitionen `J_{R,S}`;
3. exakten nativen Kokyklus;
4. positive invertierbare Metrikoperatoren `G_{R,S}`;
5. paarweise Polar-Isometrien;
6. signierte Feshbach-Colligation;
7. exakte finite-horizon Terminal-Gauge-Isometrien `W_{R,S}^{[T]}`;
8. exakte Kohärenz zwischen verschiedenen endlichen Terminal-Gauges;
9. unbeschränkte unrenormierte Zukunftsmetriken `G_{R,T}`;
10. eine kanonische **unendliche Boundary-Jet-Hierarchie** `beta_R^(m)`;
11. exakte Pullback-Kompatibilität dieses Jets unter `J_{R,S}`.

Das ist ein deutlich strukturierterer Grenzapparat als vor C3.

---

# 18. Was negativ entschieden ist

Die folgenden Routen sind jetzt geschlossen:

### 18.1 Naive bounded Terminalmetrik

Bereits C3:

\[
G_{R,T}\not\to G_{R,\infty}
\quad\text{in }\mathcal B(\mathcal K_{X,R}).
\]

### 18.2 Ein einzelner Boundary-Mode-Quotient

C4:

\[
f\in\ker\beta_R
\not\Rightarrow
\sup_T\langle G_{R,T}f,f\rangle<\infty.
\]

### 18.3 Jeder endliche Trunkat des kanonischen Boundary-Jets

Für jedes `M<infty`:

\[
\sup_T
\|G_{R,T}|_{\mathcal R_{R,M}}\|
=\infty.
\]

Damit ist jede **finite-rank Boundary-Jet-Extraktion** dieser Route unzureichend.

---

# 19. Was ausdrücklich offen bleibt

C4 entscheidet nicht:

1. ob der vollständige unendliche Boundary-Jet eine kanonische Hilbertraumtopologie besitzt;
2. ob ein unendlicher relativer Randquotient die Terminalmetrik stabilisiert;
3. ob gerade Source-Moden weitere Divergenzkanäle tragen;
4. ob eine unbeschränkte geschlossene Terminalform existiert;
5. ob `W_{R,S}^{[T]}` stark konvergiert;
6. ob ein möglicher relativer Grenztransport die exakte Weil-Geometrie trägt;
7. P10-O07;
8. P04/Suzuki-Identifikation;
9. RH;
10. Objekt X.

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal.

---

# 20. Neue strukturelle Interpretation

Die bisherige Hoffnung

\[
\boxed{\text{ein divergenter Randfreiheitsgrad }\beta_R}
\]

muss ersetzt werden durch

\[
\boxed{
\text{einen source-kanonischen asymptotischen Rand-Jet}
\quad
(\beta_R^{(0)},\beta_R^{(1)},\beta_R^{(2)},\ldots).
}
\]

Dieser Jet ist nicht ad hoc:

- er stammt direkt aus derselben Prime-Shell-Geometrie wie C3;
- seine Koeffizienten sind durch die Binomialentwicklung des Source-Randprofils erzwungen;
- er ist auf jedem Level kontinuierlich;
- er ist unter den nativen Transitionen exakt kompatibel.

Damit verschiebt sich die Objekt-X-Frage erneut:

\[
\boxed{
\text{Nicht: Kann eine einzelne Randmode entfernt werden?}
}
\]

sondern

\[
\boxed{
\text{Kann die vollständige Boundary-Jet-Geometrie relativ transportiert werden,}
\text{ ohne sie durch willkürliche Gewichte in einen Hilbertraum zu zwingen?}
}
\]

Der finite-horizon Transport `W^[T]` ist dafür weiterhin der natürlichste vorhandene Kandidat, weil er bereits auf jedem endlichen Horizont isometrisch und kohärent ist.

---

# 21. Nächster atomarer Knoten

Der nächste Schritt sollte **nicht** versuchen, endlich viele weitere Randterme abzuziehen. C4 schließt diese Strategie in jeder endlichen Ordnung.

Der erzwungene nächste Test ist:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C5]
\quad
\text{Relativer Terminaltransport gegen den vollständigen Boundary-Jet}.
}
\]

Zwei zulässige Untertests:

## C5-A — asymptotische Intertwining-Form

Prüfe für feste `R<S`, ob die Terminalmetriken trotz Divergenz eine relative asymptotische Äquivalenz besitzen, zum Beispiel auf einem gemeinsamen Core:

\[
G_{R,T}
\stackrel?\sim
J_{R,S}^*G_{S,T}J_{R,S}
\]

ist bereits exakt als Pullbackidentität bekannt; benötigt wird nun Kontrolle der Quadratwurzeltransporte

\[
G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}.
\]

Die Boundary-Jet-Identitäten

\[
\beta_S^{(m)}J_{R,S}=\beta_R^{(m)}
\]

sind hierbei als verbindliches asymptotisches Randdatum zu verwenden.

## C5-B — direkte Cauchyfrage für `W^[T]`

Untersuche

\[
\boxed{
\|(W_{R,S}^{[U]}-W_{R,S}^{[T]})f\|_{X,S}
\stackrel?\longrightarrow0
}
\]

für `U,T->infty` zunächst auf einem dichten Core.

Ein positiver Befund würde wegen §15 automatisch einen isometrischen Kokyklus im Grenzfall liefern.

Damit lautet die neue Leitfrage:

\[
\boxed{
\text{Divergiert nur die absolute Terminalmetrik, während der relative isometrische Transport konvergiert?}
}
\]

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal.