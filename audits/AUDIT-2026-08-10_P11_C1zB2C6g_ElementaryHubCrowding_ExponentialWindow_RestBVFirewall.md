# P11-C1z-B2-C6g — Elementares Hub-Crowding, exponentielles Lokalfenster und Rest-BV-Firewall

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6g]`  
**Direkte Voraussetzungen:** C1z-B, C1z-B2-C3, C1z-B2-C4, C1z-B2-C6e, C1z-B2-C6f  
**Strukturelle Schnittstellen:** C1z-B2-C6d, C1z-B2-C6a, C1z-B2-C6b, C1z-B2-C6c  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d Jet-Alignment-Firewall  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6g]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm pos,elementary\text{-}hub\text{-}crowding}
+
\checkmark[M]_{\rm pos,explicit\text{-}radius\text{-}e^{-T}/T}
+
\checkmark[M]_{\rm pos,robust\text{-}hub\text{-}separator\text{-}pairing}
+
\checkmark[M]_{\rm corr,raw\text{-}pair\text{-}count}
+
\checkmark[M]_{\rm neg,global\text{-}rest\text{-}norm\not\Rightarrow local\text{-}BV}
+
?[O]_{\rm weighted\text{-}rest\text{-}crowding}
+
?[O]_{\rm corrected\text{-}separator}
+
?[O]_{\rm asymptotic\text{-}\Delta\text{-}classification}
}
\]

C6g löst den ersten Teil des in C6f formulierten gewichteten Crowding-Problems **ohne** PNT, Siebmethoden oder Kompaktheit:

Für jede feste Zielkonstante `0<theta<1` gibt es `c_theta>0` und `T_theta<infty`, so dass für

\[
\boxed{
r_T=c_\theta\frac{e^{-T}}{T}}
\tag{C1zB2C6g.1}
\]

und für beide kanonischen Cross-Prime-Kanten

\[
x_q(T)=T-\frac12\log(q/2),
\qquad q\in\{3,5\},
\]

die gesamte gewichtete Sprungmasse **aller anderen Hubkanten** erfüllt

\[
\boxed{
\mathcal V^{h,\mathrm{off}}_{T,q}(r_T)
\le
\theta j_*
\qquad(T\ge T_\theta),
}
\tag{C1zB2C6g.2}
\]

wobei C6e/C6f

\[
j_*
=
\frac12\min\{a_2a_3,a_2a_5\}>0
\]

liefert.

Damit bleibt der feste Cross-Prime-Hauptsprung auch dann quantitativ sichtbar, wenn das Lokalfenster viele weitere Breakpoints enthält.

Der Beweis benutzt ausschließlich:

- die exakten Hubgewichte;
- die Prime-Power-Labelstruktur;
- eindeutige Primfaktorzerlegung für die endliche Niedriglabel-Separation;
- elementare Ganzzahlsummen für den Hochlabel-Tail.

Insbesondere wird **kein Primzahlsatz** benutzt.

Die zweite Hälfte des C6f-Arbeitsauftrags bleibt offen:

\[
\boxed{
\text{gewichtete lokale Variation von }A_T\mathbf1_T
=\mathbf1_T+R_T^*R_T\mathbf1_T.
}
\tag{C1zB2C6g.3}
\]

C6f's globaler Bound `||R_T||^2 <= C T e^T` kontrolliert diese lokale BV-Größe nicht. C6g siegelt diesen Implikationsfehler ausdrücklich und verschiebt den nächsten atomaren Angriff auf die **prime-puren konditionierten Rest-Sprungkoeffizienten**.

---

# 0. Voraussetzungen und Scope

## 0.1 Huboperator

Wie in C6e gilt auf

\[
\mathscr H_T=L^2(-T,T)
\]

\[
\boxed{
H_T
=
\sum_{n\in\mathcal N_T}
a_nK_{\log n},
\qquad
\mathcal N_T=\{p^k:p^k\le e^{2T}\},
}
\tag{C1zB2C6g.4}
\]

mit

\[
K_s=P_TD_sE_T
\]

und für `n=p^k`

\[
\boxed{
a_n=\sqrt{\log p}\,p^{-3k/4}.}
\tag{C1zB2C6g.5}
\]

Da

\[
\log p\le\log n,
\]

folgt die elementare Majorante

\[
\boxed{
a_n\le \sqrt{\log n}\,n^{-3/4}.}
\tag{C1zB2C6g.6}
\]

Setze

\[
\boxed{h_T:=H_T^*H_T\mathbf1_T.}
\tag{C1zB2C6g.7}
\]

Dann

\[
h_T
=
\sum_{n,m\in\mathcal N_T}
a_na_mK_{\log n}^*K_{\log m}\mathbf1_T.
\tag{C1zB2C6g.8}
\]

## 0.2 C6e-Hauptkanten

Für `q in {3,5}` definiere

\[
\boxed{
d_q:=\log(q/2),
\qquad
x_q(T):=T-d_q/2.}
\tag{C1zB2C6g.9}
\]

C6e beweist eventual für **beide** Kandidaten eine echte Hub-Sprungkante und insbesondere

\[
\boxed{
|\operatorname{Jump}_{x_q(T)}h_T|
\ge
j_q>0,
}
\tag{C1zB2C6g.10}
\]

mit einer gemeinsamen unteren Schranke

\[
\boxed{
j_*
:=
\frac12\min\{a_2a_3,a_2a_5\}>0.}
\tag{C1zB2C6g.11}
\]

C6e wählt anschließend abhängig von `T` eines der beiden `q`, so dass dieselbe Kante kein Breakpoint von `A_T 1_T` ist.

C6g behandelt zunächst die Hubseite für **beide** `q` gleichzeitig.

## 0.3 Gewichtete lokale Sprungmasse

C6f definierte für eine Stufenfunktion `g`

\[
\mathcal V_T(g;x,r)
=
\sum_{\substack{y\in\mathcal B(g)\\0<|y-x|<r}}
|\operatorname{Jump}_yg|.
\]

Für die C6g-Hubkante schreiben wir

\[
\boxed{
\mathcal V^{h,\mathrm{off}}_{T,q}(r)
:=
\sum_{\substack{y\in\mathcal B(h_T)\\0<|y-x_q(T)|<r}}
|\operatorname{Jump}_yh_T|.
}
\tag{C1zB2C6g.12}
\]

Der zentrale Sprung bei `x_q(T)` selbst wird ausdrücklich nicht mitgezählt.

---

# 1. Universeller Sprungbound eines einzelnen Hub-Paars

Aus C6e gilt

\[
K_s\mathbf1_T
=
1_{(-T,-T+s/2)}
-
1_{(T-s/2,T)}.
\]

`K_a^*=-K_a`, und `K_a` ist eine Differenz zweier Translationen mit anschließender Fensterkompression.

Daher ist

\[
K_a^*K_b\mathbf1_T
\]

eine endliche Linearkombination von Indikatorfunktionen mit universell beschränkten ganzzahligen Koeffizienten.

Insbesondere existiert eine absolute Konstante `C_J` mit

\[
\boxed{
|\operatorname{Jump}_y(K_a^*K_b\mathbf1_T)|
\le C_J
}
\tag{C1zB2C6g.13}
\]

für alle `a,b,T` und alle Sprungstellen `y`.

Folglich kann die tatsächliche absolute Sprungmasse von `h_T` durch die Summe der absoluten Paarbeiträge majorisiert werden:

\[
\boxed{
\mathcal V^{h,\mathrm{off}}_{T,q}(r)
\le
C_J
\sum_{(n,m)\in\mathfrak C_{T,q}(r)}
a_na_m,
}
\tag{C1zB2C6g.14}
\]

wobei `mathfrak C_{T,q}(r)` alle geordneten Labelpaare bezeichnet, die eine **andere** Sprungkante im punktierten `r`-Fenster um `x_q(T)` erzeugen.

Koinzidieren mehrere Paarbeiträge an derselben Kante, ist (C1zB2C6g.14) nur gröber, aber weiterhin korrekt.

---

# 2. Welche Kantentypen können nahe `x_q(T)` liegen?

C6e typisiert alle Paar-Sprungkanten durch

\[
\pm T
+
\frac12(\varepsilon_1\log n+\varepsilon_2\log m),
\qquad
\varepsilon_1,\varepsilon_2\in\{-1,0,1\}.
\tag{C1zB2C6g.15}
\]

Da

\[
x_q(T)=T-O(1),
\]

bleiben für einen hinreichend kleinen festen Radius `r_0>0` und großes `T` nur zwei asymptotisch relevante Familien übrig.

## 2.1 Rechtsseitige Differenzkanten

Sie haben die Form

\[
T-\frac12|\log m-\log n|.
\]

Nähe zu `x_q(T)` bedeutet

\[
\boxed{
\left|
|\log(m/n)|-d_q
\right|<2r.
}
\tag{C1zB2C6g.16}
\]

Also liegt, nach Vertauschung von `n,m` falls nötig,

\[
\boxed{
ce^{-2r}n<m<ce^{2r}n,
\qquad c=q/2>1.
}
\tag{C1zB2C6g.17}
\]

Die zentrale primitive Kante entspricht exakt

\[
\{n,m\}=\{2,q\}.
\]

## 2.2 Gegenüberliegende Summenkanten

Sie haben die Form

\[
-T+\frac12(\log n+\log m).
\]

Nähe zu `x_q(T)` bedeutet

\[
\boxed{
Xe^{-2r}<nm<Xe^{2r},
\qquad
X=X_{q,T}:=e^{4T}\frac2q.
}
\tag{C1zB2C6g.18}
\]

Das ist genau die in C6e nur am exakten Kollisionspunkt behandelte terminale Produktfamilie.

## 2.3 Die übrigen Kantentypen

Für hinreichend kleines festes `r_0` und hinreichend großes `T` sind im `r_0`-Fenster um `x_q(T)` ausgeschlossen:

- rechtsseitige Summenkanten, weil dafür `nm` nahe `q/2<3` liegen müsste, während `nm>=4`;
- rechtsseitige Einzelkanten, weil dafür ein Prime-Power-Label nahe `q/2` liegen müsste und `q/2` selbst kein ganzzahliges Label ist;
- linksseitige Einzelkanten und linksseitige Differenzkanten, weil dafür eine logarithmische Verschiebung von Größe `4T-O(1)` nötig wäre, während einzelne aktive Labelunterschiede höchstens `2T+O(1)` erreichen;
- die äußere Kante `T` selbst, die festen Abstand `d_q/2>0` von `x_q(T)` besitzt.

Damit reduziert sich das Hub-Crowding in C6g auf (C1zB2C6g.16) und (C1zB2C6g.18).

---

# 3. Arithmetische Isolation der niedrigen Ratio-Labels

Der kritische Punkt im elementaren Beweis ist die `+1`-Fehlertermstruktur beim Zählen ganzer Zahlen in einem kurzen Intervall.

Sie darf nicht über alle kleinen Labels aufsummiert werden, weil sie dann nur einen konstanten beziehungsweise polynomialen Fehler liefern würde.

Stattdessen trennt C6g niedrige und hohe Labels.

Fixiere `N>=10`.

Unter allen Prime-Power-Paaren

\[
(n,m)\ne(2,q),(q,2),
\qquad
2\le n,m\le N,
\]

kann wegen eindeutiger Primfaktorzerlegung **kein** Paar exakt

\[
m/n=q/2
\]

oder dessen Kehrwert erfüllen.

Denn aus

\[
\frac mn=\frac q2
\]

und `n,m` jeweils einzelne Primzahlpotenzen folgt notwendig

\[
n=2,
\qquad
m=q.
\]

Daher ist die endliche positive Distanz

\[
\boxed{
\delta_{q,N}
:=
\min_{\substack{n,m\in\mathcal P^*\\2\le n,m\le N\\\{n,m\}\ne\{2,q\}}}
\left|
|\log(m/n)|-d_q
\right|
>0.
}
\tag{C1zB2C6g.19}
\]

wohldefiniert.

Wähle

\[
\boxed{
r_{q,N}^{\rm low}:=\delta_{q,N}/4.}
\tag{C1zB2C6g.20}
\]

Dann erzeugt **kein** niedriges Off-Main-Paar mit `n,m<=N` eine rechtsseitige Differenzkante im `r_{q,N}^{low}`-Fenster.

Dies ist der einzige Ort, an dem C6g eine arithmetische Separationsaussage braucht.

Sie ist endlich und elementar; kein PNT tritt auf.

---

# 4. Elementare Hochlabel-Schätzung für rechtsseitige Differenzkanten

Fixiere `q in {3,5}` und `0<r<=r_0` mit `r_0` so klein, dass aus (C1zB2C6g.17)

\[
c_1n\le m\le c_2n
\tag{C1zB2C6g.21}
\]

mit festen positiven Konstanten `c_1,c_2` folgt.

Dann liefert (C1zB2C6g.6)

\[
\begin{aligned}
a_na_m
&\le
\sqrt{\log n\log m}\,(nm)^{-3/4}\\
&\le
C_q(1+\log n)n^{-3/2}.
\end{aligned}
\tag{C1zB2C6g.22}
\]

Für ein festes ganzzahliges `n` besitzt das Intervall

\[
(ce^{-2r}n,ce^{2r}n)
\]

Länge

\[
\le C_qrn.
\]

Also enthält es höchstens

\[
\boxed{C_qrn+1}
\tag{C1zB2C6g.23}
\]

ganze Zahlen — und damit erst recht höchstens so viele Prime-Power-Labels.

Wir vergessen ab jetzt sogar die Prime-Power-Bedingung und summieren über alle ganzen `n>N`.

Damit ist die gewichtete Hochlabelmasse der rechtsseitigen Differenzfamilie höchstens

\[
C_q
\sum_{N<n\le e^{2T}}
(C_qrn+1)(1+\log n)n^{-3/2}.
\tag{C1zB2C6g.24}
\]

Zerlege in den Intervalllängen- und den Rundungsterm.

Für den ersten:

\[
\begin{aligned}
r\sum_{n\le e^{2T}}(1+\log n)n^{-1/2}
&\le
C r(1+T)e^T\\
&\le
C rTe^T
\end{aligned}
\tag{C1zB2C6g.25}
\]

für großes `T`.

Für den zweiten:

\[
\sum_{n>N}(1+\log n)n^{-3/2}
\le
C\frac{1+\log N}{\sqrt N}.
\tag{C1zB2C6g.26}
\]

Somit:

\[
\boxed{
\mathcal W^{\rm diff}_{T,q}(r;N)
\le
C_q
\left(
rTe^T
+
\frac{1+\log N}{\sqrt N}
\right).
}
\tag{C1zB2C6g.27}
\]

Dies ist vollständig elementar.

### Warum die endliche Niedriglabel-Trennung unverzichtbar ist

Ohne §3 würde der `+1`-Term auch die kleinen `n` enthalten und nur einen festen, nicht beliebig kleinen Fehler liefern.

Durch die endliche arithmetische Isolation kann `N` zuerst so groß gewählt werden, dass der Tailterm beliebig klein wird; erst danach wird `r=r_T` gewählt.

Dies ist dieselbe Reihenfolge, die methodisch bereits aus C6a bekannt ist:

\[
\boxed{
N\text{ zuerst fest wählen, dann }T\to\infty.
}
\tag{C1zB2C6g.28}
\]

Hier ist `N` nur ein Hilfscutoff des Beweises, **kein** universeller Jet-Cutoff.

---

# 5. Elementare Schätzung der gegenüberliegenden terminalen Summenkanten

Nun gilt

\[
X=X_{q,T}=e^{4T}\frac2q.
\]

Für `r<=r_0` und

\[
Xe^{-2r}<nm<Xe^{2r},
\]

sowie `n,m<=e^{2T}` folgt

\[
\boxed{
c_qe^{2T}\le n,m\le e^{2T}}
\tag{C1zB2C6g.29}
\]

mit einer festen Konstante `c_q>0`.

Außerdem

\[
\begin{aligned}
a_na_m
&\le
\sqrt{\log n\log m}(nm)^{-3/4}\\
&\le
C_qT X^{-3/4}\\
&\le
C_qT e^{-3T}.
\end{aligned}
\tag{C1zB2C6g.30}
\]

Für festes `n` liegt `m` in einem Intervall der Länge

\[
\le C_qr\frac Xn.
\]

Daher gibt es höchstens

\[
C_qr\frac Xn+1
\]

ganzzahlige Kandidaten.

Wieder vergessen wir die Prime-Power-Bedingung vollständig.

Die gesamte gewichtete Produktfamilie ist daher majorisiert durch

\[
C_qTe^{-3T}
\sum_{c_qe^{2T}\le n\le e^{2T}}
\left(
C_qr\frac Xn+1
\right).
\tag{C1zB2C6g.31}
\]

Da das `n`-Intervall nur einen festen Multiplikativbereich umfasst,

\[
\sum_{c_qe^{2T}\le n\le e^{2T}}\frac1n
=O_q(1),
\tag{C1zB2C6g.32}
\]

und die Anzahl der `n` höchstens `e^{2T}` ist.

Somit

\[
\boxed{
\mathcal W^{\rm opp}_{T,q}(r)
\le
C_q
\left(
rTe^T+Te^{-T}
\right).
}
\tag{C1zB2C6g.33}
\]

Auch diese Schätzung ist rein elementar.

Für `r=0` reproduziert der `Te^{-T}`-Bound nicht die deutlich schärfere exakte C6e-Kollisionsschranke `O(T^2e^{-3T})`; C6g braucht diese Schärfe aber nicht. Hier wird ein ganzes Lokalfenster kontrolliert, nicht nur ein einzelner exakt kollidierender Produktwert.

---

# 6. Hauptsatz — elementares Hub-Crowding

## Satz C1zB2C6g.1

Fixiere `0<theta<1`.

Dann existieren

\[
c_\theta>0,
\qquad
T_\theta<\infty,
\]

so dass für beide `q in {3,5}` und alle `T>=T_theta` mit

\[
\boxed{
r_T=c_\theta\frac{e^{-T}}T}
\tag{C1zB2C6g.34}
\]

gilt:

\[
\boxed{
\mathcal V^{h,\mathrm{off}}_{T,q}(r_T)
\le
\theta j_*.
}
\tag{C1zB2C6g.35}
\]

### Beweis

Wähle zuerst `N` so groß, dass für `q=3,5`

\[
C_q\frac{1+\log N}{\sqrt N}
\le
\frac{\theta j_*}{6C_J}.
\tag{C1zB2C6g.36}
\]

Danach setze

\[
r_0
:=
\min_{q=3,5}
r_{q,N}^{\rm low}
\]

und verkleinere `r_0` gegebenenfalls weiter, so dass die Kantentypisierung aus §2 gilt.

Aus §§4–5 und dem universellen Sprungbound folgt

\[
\mathcal V^{h,\mathrm{off}}_{T,q}(r)
\le
C
\left(
rTe^T
+
Te^{-T}
+
\frac{1+\log N}{\sqrt N}
\right)
\tag{C1zB2C6g.37}
\]

für `0<r<=r_0` und großes `T`.

Wähle nun `c_theta>0` so klein, dass

\[
Cc_\theta\le\frac{\theta j_*}{3}.
\]

Für

\[
r_T=c_\theta e^{-T}/T
\]

ist

\[
r_TTe^T=c_\theta.
\]

Außerdem

\[
Te^{-T}\to0.
\]

Nach Vergrößerung von `T_theta` gilt zugleich `r_T<=r_0` und jeder der drei Terme in (C1zB2C6g.37) trägt höchstens den vorgesehenen Anteil bei.

Damit folgt (C1zB2C6g.35).

`□`

Status:

\[
\boxed{\checkmark[M]_{\rm pos,elementary\text{-}hub\text{-}crowding}.}
\]

---

# 7. Konkrete Wahl `theta=1/4`

Für die C6f-Zielbedingung genügt beispielsweise

\[
\theta=\frac14.
\]

Dann existiert `c_0>0` mit

\[
\boxed{
r_T=c_0\frac{e^{-T}}T}
\tag{C1zB2C6g.38}
\]

und

\[
\boxed{
\mathcal V^{h,\mathrm{off}}_{T,q}(r_T)
\le
\frac14j_*
}
\tag{C1zB2C6g.39}
\]

für `q=3,5` und großes `T`.

Damit ist C6f-Arbeitsauftrag A im elementaren Scope erfüllt.

---

# 8. Robuste Paarung mit dem unsymmetrisch crowdenden Hub

Definiere wie in C6f

\[
\boxed{
w_{T,q,r}
=
1_{(x_q(T)-r,x_q(T))}
-
1_{(x_q(T),x_q(T)+r)}.
}
\tag{C1zB2C6g.40}
\]

Wäre `x_q(T)` die einzige Hubkante im Intervall, wäre

\[
|\langle w_{T,q,r},h_T\rangle|
=r|J_{q,T}|.
\]

Jeder zusätzliche Sprung `J_y` im Intervall verändert diese Paarung um höchstens

\[
r|J_y|.
\]

Daher gilt allgemein

\[
\boxed{
|\langle w_{T,q,r},h_T\rangle|
\ge
r\left(
|J_{q,T}|-
\mathcal V^{h,\mathrm{off}}_{T,q}(r)
\right).
}
\tag{C1zB2C6g.41}
\]

Mit

\[
|J_{q,T}|\ge j_*
\]

und (C1zB2C6g.39) folgt für `r=r_T`:

\[
\boxed{
|\langle w_{T,q,r_T},h_T\rangle|
\ge
\frac34j_*r_T.
}
\tag{C1zB2C6g.42}
\]

Also:

\[
\boxed{
|\langle w_{T,q,r_T},h_T\rangle|
\gtrsim
\frac{e^{-T}}T.
}
\tag{C1zB2C6g.43}
\]

Dies ist ein echter Fortschritt gegenüber C6f: Der Hub-Zähler bleibt quantitativ kontrolliert, **ohne** dass das Lokalintervall breakpointfrei sein muss.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,robust\text{-}hub\text{-}separator\text{-}pairing}.}
\]

### Firewall

(C1zB2C6g.42) ist noch **kein** Variationszertifikat für `Delta_T^(1)`, weil im crowdenden Fall im Allgemeinen

\[
\langle w_{T,q,r_T},A_T\mathbf1_T\rangle\ne0.
\]

Die Restseite muss separat kontrolliert oder exakt wegkorrigiert werden.

---

# 9. Korrektur der Paarzählungsintuition

Die Vorüberlegung zu C6g vermutete, dass die Zahl der Cross-Prime-Paare nahe `x_T` bei Verwendung des PNT höchstens polynomial in `T` wachsen könnte.

Das ist für einen **festen positiven Ratiofensterradius** nicht richtig.

Nehmen wir heuristisch primitive Primzahlen `p,q` der Größe

\[
p\asymp q\asymp e^{2T}.
\]

Ein logarithmisches Ratiofenster der festen Breite `r` erlaubt für ein festes `p` ein additives `q`-Intervall der Länge

\[
\asymp r e^{2T}.
\]

PNT-Dichte `1/T` auf beiden Primvariablen würde daher heuristisch eine Paarzahl von ungefähr

\[
\asymp
\frac{r e^{4T}}{T^2}
\]

liefern — also weiterhin exponentiell in `T`.

Entscheidend ist nicht eine polynomial kleine Paarzahl, sondern das Gewicht jedes terminalen Paares:

\[
a_pa_q
\asymp
T e^{-3T}.
\]

Multiplikation ergibt heuristisch

\[
\asymp
r\frac{e^T}{T}
\]

für die **gewichtete** Masse.

Das erklärt zugleich:

- warum ein festes `r` zu groß ist;
- warum ein schrumpfendes exponentielles Fenster natürlich ist;
- warum PNT die elementare Radiusordnung zwar verbessern könnte, aber nicht notwendig ist, um überhaupt ein quantitatives Crowding-Fenster zu erhalten.

Status:

\[
\boxed{\checkmark[M]_{\rm corr,raw\text{-}pair\text{-}count}.}
\]

---

# 10. Was PNT voraussichtlich verbessern würde — aber C6g nicht benutzt

Die elementare Ganzzahlmajorante verliert die Primzahldichte vollständig.

Sie liefert

\[
\mathcal V^{h,\mathrm{off}}_{T,q}(r)
\lesssim
rTe^T+o(1).
\]

Eine PNT-basierte dyadische Abschätzung für primitive Paare würde heuristisch beziehungsweise nach sauberer partieller Summation eher auf

\[
\mathcal V^{h,\mathrm{off}}_{T,q}(r)
\lesssim
r\frac{e^T}{T}
+\text{Prime-Power-Tails}
\]

führen.

Damit wäre eine wesentlich größere natürliche Radiusordnung

\[
r_T\asymp Te^{-T}
\]

plausibel, also um etwa einen Faktor `T^2` größer als der elementare C6g-Radius.

C6g benötigt diese Verbesserung nicht.

**Scope:** Es wird hier kein PNT-Satz als bewiesene C6g-Aussage benutzt oder gesiegelt. Sollte die Radiusgröße später quantitativ entscheidend werden, wäre ein eigener deklarierter PNT-/Sieb-Knoten gerechtfertigt.

---

# 11. Warum der globale C6f-Restnormbound die Rest-Crowding-Frage nicht löst

C6f beweist

\[
\boxed{\|R_T\|^2\le CTe^T.}
\tag{C1zB2C6g.44}
\]

Damit

\[
\|A_T\mathbf1_T\|_2
\le
(1+CTe^T)\|\mathbf1_T\|_2.
\]

Dies ist eine `L^2`-/Operatornormaussage.

Die gesuchte Größe

\[
\mathcal V_T^A(r)
=
\sum_{\substack{y\in\mathcal B(A_T\mathbf1_T)\\0<|y-x_T|<r}}
|\operatorname{Jump}_y(A_T\mathbf1_T)|
\]

ist dagegen eine lokale `BV`-artige Größe.

Es gibt keine allgemeine Implikation

\[
L^2\text{-Bound}
\Longrightarrow
BV\text{-Bound}.
\]

Schon auf einem festen Intervall kann man Stufenfunktionen `g_M` mit

\[
\|g_M\|_2=1
\]

und beliebig vielen alternierenden Sprüngen konstruieren, deren totale Sprungvariation gegen unendlich geht.

Daher darf aus (C1zB2C6g.44) **nicht** geschlossen werden, dass

\[
\mathcal V_T^A(r_T)
\]

klein ist.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,global\text{-}rest\text{-}norm\not\Rightarrow local\text{-}BV}.
}
\]

### Scope-Firewall

Dies ist kein Gegenbeispiel gegen die konkrete P11-Reststruktur.

Es sagt nur:

\[
\boxed{
\text{Der bereits bewiesene globale Restnormbound allein kann C6g-B nicht liefern.}
}
\tag{C1zB2C6g.45}
\]

Die konkrete prime-pure / conditional-expectation Struktur kann sehr wohl zusätzliche lokale Variationkontrolle besitzen. Genau das ist der nächste offene Test.

---

# 12. Warum die Restseite strukturell günstiger als der Hub sein könnte

Obwohl C6g-B offen bleibt, gibt es eine wichtige P11-spezifische Asymmetrie.

Der Hub ist skalar und enthält alle Cross-Prime-Paare:

\[
H_T^*H_T
\sim
\sum_{p,q}
\text{Cross-Prime-Terme}.
\]

Der Rest zerfällt dagegen orthogonal nach Primzahlen:

\[
R_T^*R_T
=
\sum_pR_{p,T}^*R_{p,T}.
\]

Seine Breakpoints sind daher prime-pure:

\[
\mathcal B(A_T\mathbf1_T)
\subseteq
\bigcup_p
\left\{
\pm T+\frac m2\log p
\right\}.
\]

Außerdem ist die tatsächliche konditionierte Restmarke nicht nur durch `||q_{p,k,T}||<=1` beschränkt, sondern explizit

\[
q_{p,k,T}(u)
=
\sqrt{p-1}
\sum_{j=0}^{\min(k-1,J_{p,T}(u)-1)}
p^{(j-k)/2}\psi_{p,j}.
\tag{C1zB2C6g.46}
\]

Nahe der rechten Cross-Prime-Kante

\[
T-x_q(T)=\frac12\log(q/2)=O(1)
\]

ist die source-gekoppelte Tiefe `J_{p,T}(u)` klein.

Dies deutet darauf hin, dass eine scharfe Rest-Crowding-Schätzung nicht die grobe globale Normschranke aus C6f verwenden sollte, sondern direkt die **flache lokale Martingaltiefe** und den primitiven Kollaps aus C3.

Das ist nur eine Arbeitsrichtung, noch kein Resultat.

---

# 13. No-Go-Persistenzmatrix

| Früherer Knoten | Gesiegelter Befund | Wirkung in C6g |
|---|---|---|
| C1y | translationsinvariante Regulatoren lösen Hub/Rest-Konflikt im C1y-Scope nicht | unverändert; alle Fenster sind source-gebunden |
| B2-A | kein finite-Schatten-Abschluss aus Gamma-Präkonditionierung | unverändert; C6g benutzt elementare gewichtete Summen |
| B2-B | naiver Haar-`L^2`-Endpunkt reicht nicht | unverändert |
| C4 | unendliche Jet-Hierarchie / kein fixer endlicher Jet global | unverändert |
| C6 | kein voller Odd-Transport durch festen endlichen Jetquotienten | unverändert |
| C6a | Self-Gram-/Kompressions-Firewalls | unverändert |
| C6b | C2-Flachheit allein reicht nicht | unverändert |
| C6c | `tau=>kappa`; Triangularität allein reicht nicht | unverändert |
| C6d | C4-Jets sind keine automatischen Multi-Probes | unverändert |
| C6e | eventualer Krylov-Rang 2 | unverändert positiv |
| C6f | `Delta` auf Isolationsradius reduziert; Support allein kontrolliert Radius nicht | präzisiert: auf Hubseite ersetzt gewichtetes Crowding den leeren Spalt |
| C6f | `||R_T||^2<=CTe^T` | bleibt gültig, aber für lokale Rest-BV allein unzureichend |

---

# 14. Was C6g supersediert — und was nicht

C6g supersediert auf der **Hubseite** die zu starke Forderung aus dem ursprünglichen C6f-Separatorweg,

\[
\text{„das ganze Lokalintervall um }x_T\text{ muss breakpointfrei sein.“}
\]

Korrekt genügt:

\[
\boxed{
\text{Der Hauptsprung muss die gewichtete lokale Konkurrenz dominieren.}
}
\tag{C1zB2C6g.47}
\]

Und genau diese Dominanz ist für den Hub auf dem expliziten elementaren Radius

\[
r_T\asymp e^{-T}/T
\]

bewiesen.

Nicht supersediert werden:

- C6f's qualitative Aussage, dass reine Supportseparation keine uniforme Skala liefert;
- die offene Rest-Crowding-Frage;
- die offene quantitative Klassifikation von `Delta_T^(1)`;
- die offene Jet-Ausrichtung der zweiten Probe;
- `tau`, `Theta` und der Odd-Gauge-Grenzwert.

---

# 15. Exakter nächster Arbeitsauftrag C6h

Nach C6g ist der Hub-Crowding-Teil nicht mehr der erste Engpass.

Der nächste atomare Knoten sollte **nicht** PNT und **nicht** `N=2` sein.

Er lautet:

\[
\boxed{
\text{C6h: lokale prime-pure Rest-Sprungkoeffizienten nahe }x_3(T),x_5(T).
}
\tag{C1zB2C6g.48}
\]

Zu untersuchen sind direkt die tatsächlichen Koeffizienten von

\[
R_T^*R_T\mathbf1_T
\]

unter Verwendung von

1. der exakten Martingaldarstellung (C1zB2C6g.46);
2. der kleinen source-gekoppelten Tiefe nahe `T-O(1)`;
3. dem primitiven Kollaps
   \[
   R_T^{(1)}\mathbf1_T=0;
   \]
4. der prime-puren Orthogonalität.

Der erste Test sollte sein, ob für den bereits in C6e gewählten Kandidaten `q_T` eine Radiusfolge `r_T` derselben oder größerer Ordnung wie

\[
e^{-T}/T
\]

gilt mit

\[
\boxed{
\mathcal V_T^A(r_T)
\le C_A
}
\]

oder besser mit einer gegen null gehenden Schranke.

Danach kann erstmals der korrigierte Separator aus C6f quantitativ geschlossen werden.

### Firewall C6h

Keine Folgerung aus `||R_T||` auf lokale Jumpvariation.

Jeder positive Rest-Crowding-Satz muss aus den **tatsächlichen prime-puren Koeffizienten** und der Conditional-Expectation-Tiefe hergeleitet werden.

---

# 16. Endurteil

C6g beantwortet die zentrale methodische Frage aus der Vorüberlegung:

\[
\boxed{
\text{Für das Hub-Crowding ist PNT nicht notwendig.}
}
\]

Ein rein elementares Zweiskalenargument genügt.

Die entscheidende Abschätzung ist

\[
\boxed{
\mathcal V^{h,\mathrm{off}}_{T,q}(r)
\le
C
\left(
rTe^T
+Te^{-T}
+\frac{1+\log N}{\sqrt N}
\right),
}
\]

wobei `N` zuerst fest und groß gewählt wird.

Damit existiert explizit

\[
\boxed{
r_T=c_0e^{-T}/T}
\]

mit

\[
\boxed{
\mathcal V^{h,\mathrm{off}}_{T,q}(r_T)
\le\frac14j_*.
}
\]

Der C6e-Cross-Prime-Sprung bleibt also trotz lokaler Breakpoint-Dichte quantitativ sichtbar.

Die quantitative Zweitprobe ist damit jedoch noch nicht geschlossen, weil die Restseite

\[
A_T\mathbf1_T
\]

im selben Fenster noch keine gewichtete lokale Variationkontrolle besitzt.

Der neue erste Engpass ist daher scharf und P11-spezifisch:

\[
\boxed{
\text{Wie groß sind die tatsächlichen prime-puren Rest-Sprungkoeffizienten nahe der Cross-Prime-Kante?}
}
\]

Das ist C6h.