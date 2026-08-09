# P11-C1z-B2-A — Schattenprofil des Gamma-präkonditionierten Hub-Schurterms

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1z-B2-A]`  
**Vorgänger:** C1d, C1q-CORR, C1z-B, C1z-B1  
**Leitfrage:** Liegt der in C1z-B1 konstruierte kompakte Schurterm `S_R` in `S_4` (oder wenigstens in irgendeiner endlichen Schattenklasse)?  

**Status:**

\[
\boxed{[P11\text{-}C1z\text{-}B2\text{-}A]\quad\checkmark[K/M]_{\rm part}\;\text{mit}\;\checkmark[M]_{\rm neg,Schatten}}
\]

---

## 0. Urteil

Der finite-level Kompaktheitsgewinn aus C1z-B1 ist echt, aber **logarithmisch zu schwach für jede endliche Schattenklasse**.

Für jedes nichttriviale Source-Level

\[
R>\frac12\log2
\]

gilt für den C1z-B1-Schurterm

\[
\boxed{
S_R
=
K_R(I+R_R^*R_R)^{-1}K_R^*
\in\mathcal K,
}
\]

aber zugleich

\[
\boxed{
S_R\notin\mathcal S_p
\qquad\text{für jedes endliche }1\le p<\infty.
}
\tag{C1zB2A.1}
\]

Insbesondere

\[
\boxed{S_R\notin\mathcal S_4,\qquad S_R\notin\mathcal S_2.}
\tag{C1zB2A.2}
\]

Auch die kompakte Inverse des effektiven Huboperators erfüllt auf festem `R`

\[
\boxed{
(F_R^{\rm hub})^{-1}\in\mathcal K
\setminus\bigcup_{1\le p<\infty}\mathcal S_p.
}
\tag{C1zB2A.3}
\]

Damit kann die konkrete C1z-B1-Brücke **P10-O07 nicht über den gewünschten `S_4/S_2`-Mechanismus schließen**.

Dies ist kein No-Go gegen O07 allgemein und kein No-Go gegen Objekt X. Es ist ein präziser No-Go gegen die Unterklasse

\[
\boxed{
\text{source-windowed Gamma-Präkonditionierung}
+\text{ C1z-B-Rest-Feshbach}
}
\]

als Quelle einer endlichen Schattenordnung.

Der positive Befund aus C1z-B1 bleibt vollständig bestehen:

\[
\boxed{
\text{kompakte Resolvente ja; endliche Schattenklasse nein.}
}
\]

---

# 1. Verbindliche C1z-B1-Operatoren

Für festes `R>0` sei

\[
\mathscr H_R=L^2(-R,R).
\]

C1z-B1 konstruiert den positiven Gamma-Source-Operator

\[
C_{\Gamma,R}\ge I
\]

über die geschlossene Form

\[
q_{\Gamma,R}(f)
=
\|f\|_2^2
+
\int_{\mathbb R}
 g_\infty(\xi)
 |\widehat{E_Rf}(\xi)|^2\,\frac{d\xi}{2\pi},
\]

wobei

\[
\boxed{
g_\infty(\xi)=A_\infty(\xi)-A_\infty(0)\ge0.}
\tag{C1zB2A.4}
\]

Ferner:

\[
H_R:
\mathscr H_R\to\mathscr H_R
\]

ist der source-windowed neutrale Huboperator,

\[
R_R:
\mathscr H_R\to\mathscr Y_R^0
\]

der finite-adisch konditionierte Restoperator aus C1z-B.

Setze

\[
\boxed{K_R:=C_{\Gamma,R}^{-1/2}H_R.}
\tag{C1zB2A.5}
\]

und

\[
\boxed{
B_R:=(I+R_R^*R_R)^{-1}.
}
\tag{C1zB2A.6}
\]

Dann

\[
0<B_R\le I.
\]

Da `R_R` auf jedem festen Source-Level beschränkt ist,

\[
\boxed{
B_R\ge \beta_R I,
\qquad
\beta_R:=\frac1{1+\|R_R\|^2}>0.
}
\tag{C1zB2A.7}
\]

Der normalisierte Schurterm lautet

\[
\boxed{
S_R=K_RB_RK_R^*\ge0.
}
\tag{C1zB2A.8}
\]

C1z-B1 beweist `K_R` kompakt und damit `S_R` kompakt.

---

# 2. Exaktes Hochfrequenzprofil des Gamma-Symbols

C1d/C1z-B1 geben mit

\[
a_j=j+\frac14,
\qquad x:=\frac{|\xi|}{2}
\]

die positive Reihe

\[
\boxed{
g_\infty(\xi)
=
\sum_{j=0}^{\infty}
\frac{x^2}{a_j(a_j^2+x^2)}.}
\tag{C1zB2A.9}
\]

Wir benötigen nun nicht nur `g_\infty(\xi)\to\infty`, sondern die Größenordnung.

## Lemma C1zB2A.1 — logarithmische Zweitseitenabschätzung

Es existieren Konstanten `c,C>0` mit

\[
\boxed{
c\log(2+|\xi|)
\le
1+g_\infty(\xi)
\le
C\log(2+|\xi|)
\qquad(\xi\in\mathbb R).}
\tag{C1zB2A.10}
\]

### Beweis — obere Schranke

Für `a_j\le x` gilt

\[
\frac{x^2}{a_j(a_j^2+x^2)}
\le\frac1{a_j}.
\]

Für `a_j>x` gilt

\[
\frac{x^2}{a_j(a_j^2+x^2)}
\le\frac{x^2}{a_j^3}.
\]

Daher

\[
g_\infty(\xi)
\le
\sum_{a_j\le x}\frac1{a_j}
+
x^2\sum_{a_j>x}\frac1{a_j^3}.
\]

Der erste Term ist `O(log(2+x))`, der zweite `O(1)`.

### Beweis — untere Schranke

Für `a_j\le x` ist

\[
a_j^2+x^2\le2x^2,
\]

also

\[
\frac{x^2}{a_j(a_j^2+x^2)}
\ge\frac1{2a_j}.
\]

Somit

\[
g_\infty(\xi)
\ge
\frac12\sum_{a_j\le x}\frac1{a_j}
\gtrsim\log(2+x).
\]

Damit folgt (C1zB2A.10). `□`

### Konsequenz

Die Source-Gamma-Geometrie besitzt im Hochfrequenzbereich nur die Symbolordnung

\[
\boxed{C_{\Gamma,R}\sim\log(2+|D|).}
\tag{C1zB2A.11}
\]

Dies ist wesentlich schwächer als jede positive Potenz `|D|^\alpha`.

---

# 3. Lokalisierte orthonormale Hochfrequenzfamilie

Fixiere ein nichtleeres offenes Intervall

\[
I=(u_0,u_0+L)\Subset(-R,R).
\]

Auf `I` definiere

\[
\boxed{
e_m(u)
:=
L^{-1/2}
1_I(u)
\exp\!\left(\frac{2\pi i m(u-u_0)}{L}\right),
\qquad m\in\mathbb N.}
\tag{C1zB2A.12}
\]

Dann ist `(e_m)` eine orthonormale Familie in `\mathscr H_R`.

Die Nullfortsetzung besitzt Fourierprofil

\[
|\widehat{E_Re_m}(\xi)|
=
|\widehat{L^{-1/2}1_I}(\xi-2\pi m/L)|.
\]

Da die Fouriertransformierte eines Intervallindikators quadratisch integrierbar mit Tail `O(|\eta|^{-1})` ist, gilt mit (C1zB2A.10)

\[
\boxed{
q_{\Gamma,R}(e_m)
\le C_{R,I}\log(2+m).
}
\tag{C1zB2A.13}
\]

Die logarithmische Gewichtung ist trotz der Sprungstellen von `1_I` endlich, denn

\[
\int_{|\eta|>1}
\frac{\log(2+|\eta|)}{\eta^2}\,d\eta<\infty.
\]

---

# 4. Die Gamma-Resolvente ist in keiner endlichen Schattenklasse

Für jeden positiven selbstadjungierten Operator `C\ge I` und jeden `f` in seiner Formdomäne gilt die Cauchy-Schwarz-Ungleichung

\[
\boxed{
\langle C^{-1}f,f\rangle
\,\langle Cf,f\rangle
\ge
\|f\|^4.}
\tag{C1zB2A.14}
\]

Mit `C=C_{\Gamma,R}`, `f=e_m` und `\|e_m\|=1` folgt aus (C1zB2A.13)

\[
\boxed{
\|C_{\Gamma,R}^{-1/2}e_m\|^2
\ge
\frac{c_{R,I}}{\log(2+m)}.}
\tag{C1zB2A.15}
\]

Sei `q\ge2`. Für einen Operator `T\in\mathcal S_q` und jede orthonormale Familie `(e_m)` gilt

\[
\sum_m\|Te_m\|^q<\infty
\]

(angewandt auf die Diagonale von `(T^*T)^{q/2}`).

Für

\[
T=C_{\Gamma,R}^{-1/2}
\]

liefert (C1zB2A.15) aber

\[
\sum_m
\|Te_m\|^q
\ge
c\sum_m
\frac1{(\log(2+m))^{q/2}}
=\infty.
\]

Also

\[
\boxed{
C_{\Gamma,R}^{-1/2}
\notin\mathcal S_q
\qquad\forall q<\infty.}
\tag{C1zB2A.16}
\]

Für `q<2` folgt dies zusätzlich aus

\[
\mathcal S_q\subset\mathcal S_2.
\]

Äquivalent:

\[
\boxed{
C_{\Gamma,R}^{-1}
\notin\mathcal S_p
\qquad\forall p<\infty.}
\tag{C1zB2A.17}
\]

Dies schärft C1z-B1:

\[
\boxed{
C_{\Gamma,R}^{-1}\text{ ist kompakt, aber logarithmisch zu langsam für jede }\mathcal S_p.
}
\]

---

# 5. Der Huboperator liefert keine zusätzliche Hochfrequenzglättung

Um das Schattenprofil von `K_R=C_{\Gamma,R}^{-1/2}H_R` zu bestimmen, muss ausgeschlossen werden, dass `H_R` gerade die problematischen Hochfrequenzen vernichtet.

Für

\[
R>\frac12\log2
\]

ist das primitive Label `n=2` aktiv.

Der Huboperator ist eine **endliche** Summe partieller Translationen:

\[
H_R
=
\sum_{n\in\mathcal N_R}
 c_n P_RD_{\log n}E_R,
\qquad
c_n:=\sqrt{\Lambda(n)}n^{-3/4}>0.
\tag{C1zB2A.18}
\]

Da die endlich vielen Translationszentren

\[
\left\{\pm\frac12\log n:n\in\mathcal N_R\right\}
\]

paarweise verschieden sind, kann ein kleines Intervall

\[
I_R\Subset(-R,R)
\]

so gewählt werden, dass mindestens eine `n=2`-Translationskopie

\[
J_R=I_R\mp\frac12\log2
\]

vollständig in `(-R,R)` liegt und von allen anderen überlebenden Translationskopien disjunkt ist.

Sei `P_{J_R}` die Multiplikation mit `1_{J_R}`. Dann gilt für jedes `f\in L^2(I_R)` exakt

\[
\boxed{
P_{J_R}H_Rf
=
\pm c_2\,U_{\pm\frac12\log2}f,
\qquad
c_2=\sqrt{\log2}\,2^{-3/4}>0.}
\tag{C1zB2A.19}
\]

Daher

\[
\boxed{
\|H_Rf\|_2\ge c_2\|f\|_2
\qquad(f\in L^2(I_R)).}
\tag{C1zB2A.20}
\]

Wähle nun die orthonormale Fourierfamilie `(e_m)` aus §3 auf diesem `I_R`.

Da `H_R` nur aus endlich vielen vollständigen Translationen dieser `e_m` besteht, gilt erneut mit (C1zB2A.10)

\[
\boxed{
q_{\Gamma,R}(H_Re_m)
\le C_R\log(2+m).}
\tag{C1zB2A.21}
\]

Gleichzeitig liefert (C1zB2A.20)

\[
\|H_Re_m\|\ge c_2.
\]

Mit (C1zB2A.14), jetzt für `f=H_Re_m`, folgt

\[
\begin{aligned}
\|K_Re_m\|^2
&=
\langle C_{\Gamma,R}^{-1}H_Re_m,H_Re_m\rangle\\
&\ge
\frac{\|H_Re_m\|^4}
{q_{\Gamma,R}(H_Re_m)}\\
&\ge
\boxed{
\frac{c_R}{\log(2+m)}.}
\end{aligned}
\tag{C1zB2A.22}
\]

Daraus folgt exakt wie in §4:

\[
\boxed{
K_R\notin\mathcal S_q
\qquad\forall q<\infty.}
\tag{C1zB2A.23}
\]

### Interpretation

Der source-windowed Huboperator ist im Hochfrequenzbereich **kein Smoother**. Er ist lokal eine endliche direkte Kombination von Translationen und trägt deshalb keine zusätzliche Frequenzordnung, die die logarithmische Gamma-Glättung verbessern könnte.

---

# 6. Der Feshbach-Nenner verbessert die Schattenordnung nicht

Aus (C1zB2A.7):

\[
\beta_R I\le B_R\le I.
\]

Daher als positive Operatoren

\[
\boxed{
\beta_R K_RK_R^*
\le
S_R
\le
K_RK_R^*.}
\tag{C1zB2A.24}
\]

Angenommen, für ein endliches `p\ge1` wäre

\[
S_R\in\mathcal S_p.
\]

Die Schattenideale positiver Operatoren sind unter positiver Dominierung erblich. Aus

\[
0\le\beta_RK_RK_R^*\le S_R
\]

würde folgen

\[
K_RK_R^*\in\mathcal S_p.
\]

Dies ist äquivalent zu

\[
K_R\in\mathcal S_{2p},
\]

im Widerspruch zu (C1zB2A.23).

Somit ist der Hauptsatz bewiesen:

## Satz C1zB2A.2 — kein endliches Schattenprofil

Für jedes feste

\[
R>\frac12\log2
\]

gilt

\[
\boxed{
S_R\in\mathcal K
\quad\text{aber}\quad
S_R\notin\mathcal S_p
\;\forall p<\infty.}
\tag{C1zB2A.25}
\]

Insbesondere

\[
\boxed{S_R\notin\mathcal S_4.}
\]

Status: `✓[K/M]_{neg,Schatten}` im C1z-B1-Scope.

---

# 7. Auch die effektive Hub-Resolvente besitzt keine endliche Schattenordnung

C1z-B1 liefert

\[
\boxed{
(F_R^{\rm hub})^{-1}
=
C_{\Gamma,R}^{-1/2}
(I+S_R)^{-1}
C_{\Gamma,R}^{-1/2}.}
\tag{C1zB2A.26}
\]

Da `S_R\ge0` kompakt und beschränkt ist,

\[
\boxed{
\frac1{1+\|S_R\|}I
\le
(I+S_R)^{-1}
\le I.}
\tag{C1zB2A.27}
\]

Somit

\[
\boxed{
\frac1{1+\|S_R\|}C_{\Gamma,R}^{-1}
\le
(F_R^{\rm hub})^{-1}
\le
C_{\Gamma,R}^{-1}.}
\tag{C1zB2A.28}
\]

Wegen (C1zB2A.17) folgt:

\[
\boxed{
(F_R^{\rm hub})^{-1}
\notin\mathcal S_p
\qquad\forall p<\infty.}
\tag{C1zB2A.29}
\]

C1z-B1 hat also eine **compact-resolvent bridge**, aber keine finite-Schatten-resolvent bridge konstruiert.

---

# 8. Warum der Befund strukturell unvermeidlich ist

Die Ursache sitzt nicht primär in den Primgewichten, sondern in der archimedischen Hochfrequenzordnung:

\[
\boxed{
g_\infty(\xi)\asymp\log|\xi|.}
\]

Auf einem eindimensionalen beschränkten Source-Intervall hat ein Operator mit Eigenwertwachstum nur von logarithmischer Größenordnung inverse Eigenwerte ungefähr auf der Skala

\[
\frac1{\log n}.
\]

Die Reihe

\[
\sum_n\frac1{(\log n)^p}
\]

divergiert für jedes endliche `p`.

Der Beweis oben benutzt diese Heuristik **nicht als Annahme**, sondern realisiert sie durch die expliziten lokalisierten orthonormalen Hochfrequenzpakete `(e_m)`.

---

# 9. Konsequenz für P10-O07

P10-O07 bleibt als globaler Forschungsknoten OPEN.

Aber die konkrete C1z-B1-Unterroute

\[
\boxed{
\text{Gamma-Source-Resolvente}
\to
\text{Hub-Präkonditionierung}
\to
\text{C1z-B-Feshbach}
}
\]

kann den verlangten finite-Schatten-Kanal nicht liefern, denn bereits auf jedem festen nichttrivialen Source-Level

\[
S_R\notin\mathcal S_4.
\]

Daher:

\[
\boxed{
\text{C1z-B1 schließt O07 nicht; sein Kompaktheitsmechanismus ist für O07 zu schwach.}
}
\tag{C1zB2A.30}
\]

**Firewall:** Daraus folgt nicht, dass keine andere source-relative Geometrie, kein anderer Kompressor oder keine andere Operatorfunktion eine `S_4\setminus S_2`-Struktur erzeugen kann.

---

# 10. Was positiv erhalten bleibt

Trotz des Schatten-No-Gos bleiben die folgenden C1z-B/B1-Befunde gültig und nützlich:

1. finite-adische BC-Marks werden auf dem Weil-Korrelationsträger source-kanonisch erhalten;
2. p-adische Martingalreste werden auf jedem festen Source-Level endlich lokalisiert;
3. volle Translationinvarianz wird gebrochen;
4. der Gamma-Source-Operator besitzt kompakte Resolvente;
5. der effektive Hub-Schurterm ist `I + kompakt`;
6. der konditionierte Rest sitzt kanonisch im Feshbach-Nenner;
7. die Konstruktion ist RH-frei.

Der neue Negativbefund betrifft nur die **Geschwindigkeit der Kompaktheit**.

---

# 11. Statusmatrix

| Aussage | Status |
|---|---|
| `1+g_infty(xi) ~ log(2+|xi|)` zweiseitig | `✓[K/M]` |
| `C_{Gamma,R}^{-1}` kompakt | `✓[K/M]` aus C1z-B1 |
| `C_{Gamma,R}^{-1}` in einer endlichen `S_p` | `×[M]` |
| `K_R=C_{Gamma,R}^{-1/2}H_R` kompakt | `✓[K/M]` aus C1z-B1 |
| `K_R` in einer endlichen `S_q` | `×[M]` |
| Feshbach-Nenner `B_R=(I+R_R^*R_R)^{-1}` positiv/invertibel auf festem `R` | `✓[K/M]` |
| `S_R=K_RB_RK_R^*` kompakt | `✓[K/M]` |
| `S_R in S_4` | `×[M]` |
| `S_R in S_2` | `×[M]` |
| `S_R` in irgendeiner endlichen Schattenklasse | `×[M]` |
| `(F_R^hub)^{-1}` kompakt | `✓[K/M]` |
| `(F_R^hub)^{-1}` in irgendeiner endlichen Schattenklasse | `×[M]` |
| C1z-B1 schließt P10-O07 | `×[M]` für diese konkrete Unterroute |
| P10-O07 allgemein | `?[O]` |
| Large-`R` Mosco-/Resolventenfrage | `?[O]` |

---

# 12. Nächster atomarer Schritt

Da der `S_4`-Test bereits **auf jedem festen Source-Level negativ** ist, kann ein bloßer `R\to\infty`-Grenzübergang diese konkrete Schatteneigenschaft nicht nachträglich erzeugen.

Für P11 ergeben sich deshalb zwei getrennte Anschlussfragen:

### B2-B — Large-`R` trotz fehlender Schattenordnung

Prüfe, ob die compact-resolvent Geometrien

\[
(F_R^{\rm hub})^{-1}
\]

unter geeigneten kanonischen Einbettungen überhaupt einen Mosco-/starken-Resolventen-Grenzpfad besitzen. Dies bleibt für Objekt X relevant, auch ohne O07.

### B2-C — stärkere source-relative Ordnung für O07

Falls O07 weiter aktiv angegriffen werden soll, muss eine zusätzliche Struktur echte **polynomiale** Hochfrequenzordnung erzeugen. Die reine Gamma-Inzidenz liefert nur `log|xi|` und kann durch keine bloße endliche Schattenbuchhaltung in `S_4` verwandelt werden.

Mögliche zulässige Quellen hierfür wären nur neu zu konstruierende source-relative/Rand-/Graphoperatoren; sie dürfen nicht rückwärts so gewählt werden, dass eine gewünschte Schattenklasse erzwungen wird.

Arbeitsentscheidung:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}B]
\quad
\text{Large-}R\text{-Kompatibilität der compact-resolvent Hubgeometrien}
}
\]

ist der natürliche nächste Schritt, während O07 für die **reine Gamma-präkonditionierte B1-Route** als negativ entschieden gilt.

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal.
