# P11-C1z-B2-C6o — Supporttrennung, Feshbach-Sektormischung und erzwungene Erstmode-Kompensation

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6o]`  
**Direkte Voraussetzungen:** C1z-B, C1z-B2-C3, C1z-B2-C6h, C1z-B2-C6m, C1z-B2-C6n  
**Strukturelle Schnittstellen:** C1z-B2-C4, C1z-B2-C6d, C1z-B2-C6e, C1z-B2-C6f, C1z-B2-C6g, C1z-B2-C6i, C1z-B2-C6j, C1z-B2-C6k, C1z-B2-C6l  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d `orthogonality != jet alignment`, C1z-B2-C6k `current data != Wronskian nonzero`, C1z-B2-C6l `C4 constant-mode mechanism does not transfer`, C1z-B2-C6m `A-orthogonality != bulk cancellation`, C1z-B2-C6n `positivity != alignment`.  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6o]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm corr,bare\text{-}hub\not= pure\text{-}cross\text{-}prime}
+
\checkmark[M]_{\rm corr,screening\not= arithmetically\text{-}prime\text{-}pure}
+
\checkmark[M]_{\rm pos,push\text{-}through\text{-}sector\text{-}formula}
+
\checkmark[M]_{\rm pos,forced\text{-}first\text{-}mode\text{-}compensation}
+
\checkmark[M]_{\rm pos,residual\text{-}bare\text{-}vs\text{-}screened\text{-}reduction}
+
\checkmark[M]_{\rm pos,screening\text{-}Cauchy\text{-}criterion}
+
\checkmark[M]_{\rm neg,target\text{-}sector\text{-}orthogonality\not\Rightarrow RR^*\text{-}block\text{-}diagonal}
+
\checkmark[M]_{\rm neg,support\text{-}separation\text{-}route}
+
?[O]_{\rm residual\text{-}bare\text{-}vs\text{-}screened\text{-}separation}
+
?[O]_{\rm residual\text{-}angle>0}
+
?[O]_{\rm quantitative\text{-}s_{min}}
}
\]

C6n reduzierte die offene `2x2`-Alignmentfrage auf die konkrete Feshbach-Korrelation

\[
\boxed{
\sqrt{\Delta_T^{(1)}}\,a_{R,T}^{(2)}
=
\mathcal U_{R,T}-\mathcal C_{R,T},
}
\tag{C1zB2C6o.1}
\]

mit

\[
\boxed{
\mathcal U_{R,T}
:=
\langle b_{R,T},h_T\rangle,
}
\tag{C1zB2C6o.2}
\]

und

\[
\boxed{
\mathcal C_{R,T}
:=
\left\langle
R_Tb_{R,T},
(I+R_TR_T^*)^{-1}R_Th_T
\right\rangle.
}
\tag{C1zB2C6o.3}
\]

Hier

\[
 b_{R,T}:=H_T^*J_{R,T}g_{R,T},
\qquad
 h_T:=H_T^*H_T\mathbf1_T.
\tag{C1zB2C6o.4}
\]

Die natürliche Vorüberlegung war, `U` als cross-prime und `C` als prime-pure zu trennen und daraus die Unmöglichkeit einer exakten Kompensation abzuleiten.

C6o entscheidet diese Route **negativ**.

Der Grund ist nicht bloß, dass am Ende zwei Skalare verglichen werden. Die behauptete Supporttrennung geht bereits auf Operatorebene in der relevanten zusammengesetzten Korrelation verloren:

1. `U` ist keine reine Cross-Prime-Korrelation, sondern eine Drei-Label-Hubkorrelation mit diagonalem und gemischtem Anteil.
2. `R_T^*R_T` ist zwar eine Summe prime-sektoraler Gramoperatoren, aber daraus folgt weder, dass `R_TR_T^*` blockdiagonal ist, noch dass `(I+R_TR_T^*)^{-1}` die Zielprimsektoren separat behandelt.
3. Selbst nach einer exakten Push-through-Reduktion auf eine Summe über äußere Restprimen enthält jeder Summand bereits die Hub-Mischung aus `b_{R,T}` und `A_T^{-1}h_T`.
4. Ein kompletter Erstmode-Anteil von `U` und `C` ist sogar **algebraisch identisch** und muss sich exakt wegheben. Eine rohe Supportdifferenz wäre daher ohnehin nicht die richtige Vergleichsebene.

Der richtige neue Vergleich ist residual:

\[
\boxed{
\mathcal U_{R,T}^{\perp}
:=
\langle b_{R,T},r_T\rangle,
}
\tag{C1zB2C6o.5}
\]

gegen

\[
\boxed{
\mathcal C_{R,T}^{\perp}
:=
\langle b_{R,T},(I-A_T^{-1})r_T\rangle,
}
\tag{C1zB2C6o.6}
\]

wobei

\[
\boxed{
 r_T:=h_T-\lambda_TA_T\mathbf1_T.
}
\tag{C1zB2C6o.7}
\]

Dann gilt exakt

\[
\boxed{
\sqrt{\Delta_T^{(1)}}\,a_{R,T}^{(2)}
=
\mathcal U_{R,T}^{\perp}
-
\mathcal C_{R,T}^{\perp}.
}
\tag{C1zB2C6o.8}
\]

Damit ist der nächste zulässige Schritt nicht mehr eine globale `cross-prime vs prime-pure`-Supportbehauptung, sondern eine quantitative oder arithmetische Trennung genau dieser beiden residualen Skalare.

---

# 0. Verbindliche Daten und Notation

Fixiere `R>0` und großes `T`.

Aus C6m stammt der First-Observation-Nullvektor

\[
\boxed{
 g_{R,T}
=
 f_{R,1}
-
\frac{\ell_{R,1}(T)}{\ell_{R,0}(T)}f_{R,0},
}
\tag{C1zB2C6o.9}
\]

mit

\[
\boxed{
\langle J_{R,T}g_{R,T},H_T\mathbf1_T\rangle=0.
}
\tag{C1zB2C6o.10}
\]

Setze

\[
\boxed{
 b_{R,T}:=H_T^*J_{R,T}g_{R,T}.
}
\tag{C1zB2C6o.11}
\]

Dann ist

\[
\boxed{
\langle b_{R,T},\mathbf1_T\rangle=0.
}
\tag{C1zB2C6o.12}
\]

Ferner

\[
\boxed{
 h_T:=H_T^*H_T\mathbf1_T,
}
\tag{C1zB2C6o.13}
\]

und

\[
 A_T:=I+R_T^*R_T\ge I.
\tag{C1zB2C6o.14}
\]

Wie in C6n:

\[
\lambda_T
:=
\frac{\mu_{T,1}}{\mu_{T,0}},
\qquad
r_T
:=
h_T-\lambda_TA_T\mathbf1_T.
\tag{C1zB2C6o.15}
\]

Dann

\[
\boxed{
\langle r_T,\mathbf1_T\rangle=0
}
\tag{C1zB2C6o.16}
\]

und

\[
\boxed{
\langle r_T,A_T^{-1}r_T\rangle
=
\Delta_T^{(1)}.
}
\tag{C1zB2C6o.17}
\]

C6n zeigt

\[
\boxed{
\sqrt{\Delta_T^{(1)}}\,a_{R,T}^{(2)}
=
\langle b_{R,T},A_T^{-1}h_T\rangle.
}
\tag{C1zB2C6o.18}
\]

Da

\[
A_T^{-1}h_T
=
\lambda_T\mathbf1_T+A_T^{-1}r_T
\]

und `b_{R,T}\perp\mathbf1_T`, ist äquivalent

\[
\boxed{
\sqrt{\Delta_T^{(1)}}\,a_{R,T}^{(2)}
=
\langle b_{R,T},A_T^{-1}r_T\rangle.
}
\tag{C1zB2C6o.19}
\]

Diese residuale Form ist für C6o die verbindliche Zielgröße.

---

# 1. Korrektur I — die nackte Hubkorrelation ist nicht „rein cross-prime“

C6e/C6g isolierten echte Cross-Prime-Sprungstellen des Vektors

\[
h_T=H_T^*H_T\mathbf1_T.
\]

Das bedeutet aber nicht, dass jede spätere skalare Hubkorrelation mit `h_T` rein cross-prime wäre.

Für das feste Terminal `T` ist die aktive Prime-Power-Menge endlich. Schreibe

\[
\boxed{
H_T
=
\sum_{n=p^k\in\mathcal N_T}
\alpha_nK_n,
\qquad
\alpha_{p^k}
:=
\sqrt{\log p}\,p^{-3k/4},
}
\tag{C1zB2C6o.20}
\]

wobei

\[
K_n:=K_{\log n}=P_TD_{\log n}E_T.
\]

**Korrektur zur informellen Vorüberlegung:** Der Hubkoeffizient ist `sqrt(log p) p^{-3k/4}`, nicht `log p p^{-3k/4}`. Logarithmische Produkte entstehen erst nach Multiplikation mehrerer Hubkoeffizienten.

Dann

\[
\boxed{
 b_{R,T}
=
\sum_{a\in\mathcal N_T}
\alpha_aK_a^*J_{R,T}g_{R,T}.
}
\tag{C1zB2C6o.21}
\]

Weiter

\[
\boxed{
 h_T
=
\sum_{m,n\in\mathcal N_T}
\alpha_m\alpha_nK_m^*K_n\mathbf1_T.
}
\tag{C1zB2C6o.22}
\]

Daher

\[
\boxed{
\mathcal U_{R,T}
=
\sum_{a,m,n\in\mathcal N_T}
\alpha_a\alpha_m\alpha_n
\left\langle
K_a^*J_{R,T}g_{R,T},
K_m^*K_n\mathbf1_T
\right\rangle.
}
\tag{C1zB2C6o.23}
\]

Dies ist eine **Drei-Label-Hubkorrelation**.

Die Indizes `a,m,n` dürfen

- zur selben Primzahl gehören;
- zu zwei verschiedenen Primzahlen gehören;
- zu drei verschiedenen Primzahlen gehören.

Die Cross-Prime-Jumpstruktur aus C6e beweist das Vorhandensein bestimmter gemischter Beiträge in `h_T`. Sie eliminiert aber nicht die diagonal-prime Beiträge in (C1zB2C6o.23).

Insbesondere ist die Aussage

\[
\boxed{
\mathcal U_{R,T}
\text{ ist rein cross-prime}
}
\]

nicht durch die bestehende P11-Kette gedeckt.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,bare\text{-}hub\not= pure\text{-}cross\text{-}prime}.
}
\]

### First-Observation-Nullheit ändert dies nicht

Aus C6m

\[
\sum_n
\alpha_n
\langle Jg_{R,T},K_n\mathbf1_T\rangle
=0.
\tag{C1zB2C6o.24}
\]

Dies ist eine einzige lineare Relation der **ersten** Hubobservation.

Sie annihiliert nicht termweise die Drei-Label-Summe (C1zB2C6o.23). Insbesondere folgt daraus weder das Verschwinden aller same-prime Tripletts noch eine reine Cross-Prime-Reduktion.

---

# 2. Restsektoren: was wirklich prime-pure ist

C1z-B/C6h definieren

\[
\boxed{
R_Tf
=
\bigoplus_pR_{p,T}f
}
\tag{C1zB2C6o.25}
\]

mit paarweise orthogonalen **Targetsektoren** für verschiedene Primzahlen.

Daraus folgt exakt

\[
\boxed{
R_T^*R_T
=
\sum_pR_{p,T}^*R_{p,T}.
}
\tag{C1zB2C6o.26}
\]

Dies ist die prime-pure Gramstruktur der Restmetrik, die C6h entscheidend benutzt.

Aber (C1zB2C6o.26) ist eine Aussage auf dem **Source-Raum** nach Rücktransport aus den orthogonalen Targetsektoren.

Sie darf nicht mit einer Blockdiagonalität von `R_TR_T^*` auf dem Targetraum verwechselt werden.

---

# 3. Korrektur II — Targetsektor-Orthogonalität impliziert keine Blockdiagonalität von `RR^*`

Schreibe

\[
\mathscr Y_T
=
\bigoplus_p\mathscr Y_{p,T},
\qquad
R_Tf=(R_{p,T}f)_p.
\tag{C1zB2C6o.27}
\]

Für

\[
y=(y_q)_q\in\mathscr Y_T
\]

gilt

\[
R_T^*y
=
\sum_qR_{q,T}^*y_q.
\tag{C1zB2C6o.28}
\]

Damit lautet die `p`-te Komponente von `R_TR_T^*y`

\[
\boxed{
(R_TR_T^*y)_p
=
\sum_qR_{p,T}R_{q,T}^*y_q.
}
\tag{C1zB2C6o.29}
\]

Also besitzt `R_TR_T^*` die Blockmatrix

\[
\boxed{
(R_TR_T^*)_{p,q}
=
R_{p,T}R_{q,T}^*.
}
\tag{C1zB2C6o.30}
\]

Die Orthogonalität der Räume `\mathscr Y_{p,T}` bedeutet nicht

\[
R_{p,T}R_{q,T}^*=0
\qquad(p\ne q).
\]

Ein solcher Satz wäre eine zusätzliche source-seitige Orthogonalität der Rückbilder und ist in C1z-B/C6h nicht bewiesen.

Folglich ist auch

\[
\boxed{
(I+R_TR_T^*)^{-1}
\text{ ist prime-sektor-blockdiagonal}
}
\]

mit den derzeitigen Daten **nicht** zulässig.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,target\text{-}sector\text{-}orthogonality\not\Rightarrow RR^*\text{-}block\text{-}diagonal}.
}
\]

## 3.1 Minimaler abstrakter Daten-Separator

Dieser Punkt ist reine lineare Algebra und benötigt keine P11-Spezialität.

Nehme

\[
\mathscr H=\mathbb C,
\qquad
\mathscr Y_p=\mathbb C,
\qquad
\mathscr Y_q=\mathbb C,
\]

und

\[
R_px=x,
\qquad
R_qx=x.
\]

Dann

\[
R:\mathbb C\to\mathbb C\oplus\mathbb C,
\qquad
Rx=(x,x).
\]

Die beiden Targetkoordinaten sind orthogonal. Trotzdem

\[
R^*R=2I
=R_p^*R_p+R_q^*R_q,
\]

während

\[
\boxed{
RR^*
=
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
}
\tag{C1zB2C6o.31}
\]

Somit

\[
\boxed{
(I+RR^*)^{-1}
=
\frac13
\begin{pmatrix}
2&-1\\
-1&2
\end{pmatrix},
}
\tag{C1zB2C6o.32}
\]

also mit echten Off-Diagonalblöcken.

Dies ist **kein P11-Gegenbeispiel**. Es zeigt nur logisch scharf, dass die in der Vorüberlegung verwendete Schlussrichtung aus Targetsektor-Orthogonalität nicht gilt.

---

# 4. Exakte Push-through-Identität

Die fehlende Blockdiagonalität ist für die Algebra von `C` kein Hindernis, weil es eine exakte Push-through-Formel gibt.

Setze

\[
B_T
:=(I+R_TR_T^*)^{-1}.
\tag{C1zB2C6o.33}
\]

Dann

\[
(I+R_TR_T^*)R_T
=
R_T(I+R_T^*R_T)
=
R_TA_T.
\]

Multiplikation mit den Inversen ergibt

\[
\boxed{
B_TR_T
=
R_TA_T^{-1}.
}
\tag{C1zB2C6o.34}
\]

Analog

\[
\boxed{
R_T^*B_T
=
A_T^{-1}R_T^*.
}
\tag{C1zB2C6o.35}
\]

Daher

\[
\begin{aligned}
\mathcal C_{R,T}
&=
\langle R_Tb_{R,T},B_TR_Th_T\rangle\\
&=
\langle R_Tb_{R,T},R_TA_T^{-1}h_T\rangle\\
&=
\langle b_{R,T},R_T^*R_TA_T^{-1}h_T\rangle.
\end{aligned}
\]

Mit

\[
R_T^*R_T=A_T-I
\]

folgt

\[
\boxed{
\mathcal C_{R,T}
=
\langle b_{R,T},(I-A_T^{-1})h_T\rangle.
}
\tag{C1zB2C6o.36}
\]

Dies reproduziert C6ns Woodbury-Zerlegung in einer source-seitigen Form.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,push\text{-}through\text{-}sector\text{-}formula}.
}
\]

---

# 5. Exakte äußere Prime-Sektorzerlegung von `C`

Aus (C1zB2C6o.34) und der direkten Summe folgt

\[
\begin{aligned}
\mathcal C_{R,T}
&=
\langle R_Tb_{R,T},R_TA_T^{-1}h_T\rangle\\
&=
\sum_p
\langle
R_{p,T}b_{R,T},
R_{p,T}A_T^{-1}h_T
\rangle_{\mathscr Y_{p,T}}.
\end{aligned}
\]

Also

\[
\boxed{
\mathcal C_{R,T}
=
\sum_p\mathcal C_{R,T}^{[p]},
\qquad
\mathcal C_{R,T}^{[p]}
:=
\langle R_{p,T}b_{R,T},R_{p,T}A_T^{-1}h_T\rangle.
}
\tag{C1zB2C6o.37}
\]

Dies ist eine echte und nützliche Sektorzerlegung.

Aber ihre Bedeutung muss exakt typisiert werden:

\[
\boxed{
\text{`C^[p]` hat einen äußeren Restsektor }p,
\text{ ist aber nicht arithmetisch nur aus }p\text{-Labels aufgebaut.}
}
\tag{C1zB2C6o.38}
\]

Warum?

- `b_{R,T}=H_T^*Jg` enthält Hublabels sämtlicher Primzahlen;
- `h_T=H_T^*H_T1_T` enthält bereits zwei Hublabels;
- `A_T^{-1}` ist die inverse Funktion des gesamten Operators
  \[
  A_T=I+\sum_qR_{q,T}^*R_{q,T}
  \]
  und besitzt keine bewiesene Zerlegung in unabhängig wirkende Einzelprime-Inversen;
- anschließend wirkt `R_{p,T}` auf diese bereits global gemischten Sourcevektoren.

Somit bewirkt die äußere Sektororthogonalität nur, dass es im **letzten Target-Skalarprodukt** keine Paarung zwischen verschiedenen äußeren `p`-Koordinaten gibt.

Sie entfernt nicht die inneren Hub- und Screening-Labels.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,screening\not= arithmetically\text{-}prime\text{-}pure}.
}
\]

---

# 6. Konkrete Labelmischung schon in `R_p b`

Die vorige Aussage ist nicht nur abstrakte Funktionalkalkülwarnung.

C6h schreibt

\[
R_{p,T}f(u)
=
\sum_{k\ge1}
\beta_{p,k}
K_{p^k}f(u)
\,q_{p,k,T}(u),
\tag{C1zB2C6o.39}
\]

mit

\[
\beta_{p,k}
=
\sqrt{\log p}\,p^{-k/4}.
\]

Setzt man

\[
b_{R,T}
=
\sum_a\alpha_aK_a^*Jg_{R,T}
\]

ein, erhält man formal und wegen des endlichen aktiven Terminalcutoffs exakt

\[
\boxed{
R_{p,T}b_{R,T}(u)
=
\sum_{k\ge1}
\sum_{a\in\mathcal N_T}
\beta_{p,k}\alpha_a
K_{p^k}K_a^*Jg_{R,T}(u)
\,q_{p,k,T}(u).
}
\tag{C1zB2C6o.40}
\]

Der äußere Restprime ist `p`, aber das innere Hublabel `a` läuft über **alle** Primzahlpotenzen.

Schon die linke Hälfte eines einzelnen `C^[p]` ist daher arithmetisch gemischt.

Für die rechte Hälfte

\[
R_{p,T}A_T^{-1}h_T
\]

ist die Mischung mindestens ebenso stark.

Daraus folgt:

\[
\boxed{
\text{Die Cross-Prime-Arithmetik von }b,h
\text{ wird durch äußere Restsektorierung nicht gelöscht.}
}
\tag{C1zB2C6o.41}
\]

---

# 7. Firewall: primitiver Restkollaps auf `1_T` hilft hier nicht direkt

C3/C6d beweisen für den primitiven konditionierten Rest

\[
\boxed{
R_T^{(1)}\mathbf1_T=0.
}
\tag{C1zB2C6o.42}
\]

Diese Identität ist wichtig für die erste Konstantenmode.

In `C` treten aber die Restoperatoren auf

\[
R_Tb_{R,T}
\]

und

\[
R_TA_T^{-1}h_T,
\]

nicht auf `R_T1_T` allein.

Aus

\[
R_T^{(1)}1_T=0
\]

folgt weder

\[
R_T^{(1)}b_{R,T}=0
\]

noch

\[
R_T^{(1)}A_T^{-1}h_T=0.
\]

Der primitive Restkanal darf daher in C6o **nicht** aus der Screening-Korrelation gestrichen werden.

Dies ist dieselbe strukturelle Vorsicht, die C6h beim Rücktransport durch `R_p^*` bereits verlangte.

---

# 8. Hauptsatz I — ein kompletter Erstmode-Anteil von `U` und `C` ist identisch

Die rohe Frage

\[
\mathcal U_{R,T}
\stackrel?=\mathcal C_{R,T}
\]

enthält einen Anteil, der sich **zwangsläufig** kompensiert.

Erinnere

\[
h_T
=
\lambda_TA_T\mathbf1_T+r_T.
\tag{C1zB2C6o.43}
\]

Weil

\[
\langle b_{R,T},\mathbf1_T\rangle=0,
\]

gilt

\[
\begin{aligned}
\mathcal U_{R,T}
&=
\langle b_{R,T},h_T\rangle\\
&=
\lambda_T\langle b_{R,T},A_T\mathbf1_T\rangle
+
\langle b_{R,T},r_T\rangle.
\end{aligned}
\]

Nun

\[
A_T\mathbf1_T
=
\mathbf1_T+R_T^*R_T\mathbf1_T,
\]

also

\[
\langle b_{R,T},A_T\mathbf1_T\rangle
=
\langle R_Tb_{R,T},R_T\mathbf1_T\rangle.
\]

Damit

\[
\boxed{
\mathcal U_{R,T}
=
\lambda_T
\langle R_Tb_{R,T},R_T\mathbf1_T\rangle
+
\mathcal U_{R,T}^{\perp},
}
\tag{C1zB2C6o.44}
\]

wobei

\[
\boxed{
\mathcal U_{R,T}^{\perp}
:=
\langle b_{R,T},r_T\rangle.
}
\tag{C1zB2C6o.45}
\]

Für `C` benutze (C1zB2C6o.36):

\[
\mathcal C_{R,T}
=
\langle b_{R,T},(I-A_T^{-1})h_T\rangle.
\]

Setze wieder

\[
h_T=\lambda_TA_T1_T+r_T.
\]

Dann

\[
(I-A_T^{-1})A_T1_T
=
A_T1_T-1_T
=
R_T^*R_T1_T.
\]

Folglich

\[
\boxed{
\mathcal C_{R,T}
=
\lambda_T
\langle R_Tb_{R,T},R_T\mathbf1_T\rangle
+
\mathcal C_{R,T}^{\perp},
}
\tag{C1zB2C6o.46}
\]

mit

\[
\boxed{
\mathcal C_{R,T}^{\perp}
:=
\langle b_{R,T},(I-A_T^{-1})r_T\rangle.
}
\tag{C1zB2C6o.47}
\]

Damit ist bewiesen:

\[
\boxed{
\text{Der gesamte }\lambda_T\text{-Erstmode-Screeninganteil ist in }U\text{ und }C\text{ exakt identisch.}
}
\tag{C1zB2C6o.48}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,forced\text{-}first\text{-}mode\text{-}compensation}.
}
\]

### Interpretation

Ein Teil der Gleichheit von `U` und `C` ist nicht arithmetisch „zufällig“, sondern **durch die Feshbach-Zerlegung erzwungen**.

Darum ist es methodisch ungeeignet, die rohen Terme `U` und `C` über grobe Supportklassen vollständig voneinander trennen zu wollen.

Die relevante Frage beginnt erst nach Abzug des gemeinsamen Erstmodeanteils.

---

# 9. Hauptsatz II — residuale Bare-vs-Screened-Form

Subtrahiere (C1zB2C6o.46) von (C1zB2C6o.44).

Dann

\[
\boxed{
\mathcal U_{R,T}-\mathcal C_{R,T}
=
\mathcal U_{R,T}^{\perp}
-
\mathcal C_{R,T}^{\perp}.
}
\tag{C1zB2C6o.49}
\]

Andererseits

\[
\mathcal U_{R,T}^{\perp}
-
\mathcal C_{R,T}^{\perp}
=
\langle b_{R,T},A_T^{-1}r_T\rangle.
\]

Also exakt

\[
\boxed{
\sqrt{\Delta_T^{(1)}}\,a_{R,T}^{(2)}
=
\langle b_{R,T},r_T\rangle
-
\langle b_{R,T},(I-A_T^{-1})r_T\rangle.
}
\tag{C1zB2C6o.50}
\]

Dies ist die korrekte `bare residual correlation minus residual screening`-Form.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,residual\text{-}bare\text{-}vs\text{-}screened\text{-}reduction}.
}
\]

---

# 10. Der residuale Screeningoperator ist positiv

Definiere

\[
\boxed{
S_T
:=
I-A_T^{-1}.
}
\tag{C1zB2C6o.51}
\]

Da

\[
A_T\ge I,
\]

gilt durch positiven Funktionalkalkül

\[
\boxed{
0\le S_T<I.
}
\tag{C1zB2C6o.52}
\]

Außerdem folgt aus der Push-through-Formel

\[
\boxed{
S_T
=
R_T^*(I+R_TR_T^*)^{-1}R_T.
}
\tag{C1zB2C6o.53}
\]

Damit

\[
\boxed{
\mathcal C_{R,T}^{\perp}
=
\langle b_{R,T},S_Tr_T\rangle
=
\langle S_T^{1/2}b_{R,T},S_T^{1/2}r_T\rangle.
}
\tag{C1zB2C6o.54}
\]

Dies liefert eine exakte positive Geometrie für die Screening-Korrektur, obwohl ihr Vorzeichen als gemischte Paarung nicht festliegt.

---

# 11. Screening-Cauchy-Schwarz und ein exaktes hinreichendes Nichtkompensationskriterium

Aus (C1zB2C6o.54) folgt

\[
\boxed{
|\mathcal C_{R,T}^{\perp}|
\le
\sqrt{
\langle b_{R,T},S_Tb_{R,T}\rangle
}
\sqrt{
\langle r_T,S_Tr_T\rangle
}.
}
\tag{C1zB2C6o.55}
\]

Definiere die beiden residualen Screeningenergien

\[
\boxed{
\varepsilon_{b,T}^{\rm scr}
:=
\langle b_{R,T},S_Tb_{R,T}\rangle,
}
\tag{C1zB2C6o.56}
\]

und

\[
\boxed{
\varepsilon_{r,T}^{\rm scr}
:=
\langle r_T,S_Tr_T\rangle.
}
\tag{C1zB2C6o.57}
\]

Dann

\[
\boxed{
|\mathcal C_{R,T}^{\perp}|
\le
\sqrt{arepsilon_{b,T}^{\rm scr}\varepsilon_{r,T}^{\rm scr}}.
}
\tag{C1zB2C6o.58}
\]

Somit gilt das vollständig explizite hinreichende Kriterium

\[
\boxed{
|\mathcal U_{R,T}^{\perp}|
>
\sqrt{arepsilon_{b,T}^{\rm scr}\varepsilon_{r,T}^{\rm scr}}
\quad\Longrightarrow\quad
a_{R,T}^{(2)}\ne0.
}
\tag{C1zB2C6o.59}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,screening\text{-}Cauchy\text{-}criterion}.
}
\]

### Alternative source-seitige Formeln

Weil

\[
S_T=I-A_T^{-1},
\]

ist

\[
\boxed{
\varepsilon_{b,T}^{\rm scr}
=
\|b_{R,T}\|^2
-
\langle b_{R,T},A_T^{-1}b_{R,T}\rangle.
}
\tag{C1zB2C6o.60}
\]

C6n identifiziert

\[
\langle b_{R,T},A_T^{-1}b_{R,T}\rangle
=
\sigma_T(J_{R,T}g_{R,T}).
\]

Daher

\[
\boxed{
\varepsilon_{b,T}^{\rm scr}
=
\|b_{R,T}\|^2
-
\sigma_T(J_{R,T}g_{R,T}).
}
\tag{C1zB2C6o.61}
\]

Analog

\[
\boxed{
\varepsilon_{r,T}^{\rm scr}
=
\|r_T\|^2
-
\Delta_T^{(1)}.
}
\tag{C1zB2C6o.62}
\]

Somit kann (C1zB2C6o.59) auch geschrieben werden als

\[
\boxed{
|\langle b_{R,T},r_T\rangle|
>
\sqrt{
(\|b_{R,T}\|^2-\sigma_T(Jg_{R,T}))
(\|r_T\|^2-\Delta_T^{(1)})
}
\Rightarrow
a_{R,T}^{(2)}\ne0.
}
\tag{C1zB2C6o.63}
\]

Diese Ungleichung ist derzeit nicht bewiesen. Sie isoliert aber eine quantitativ saubere nächste Route.

---

# 12. Warum allgemeine Supporttrennung die Kompensation nicht ausschließt

Die Vorüberlegung hoffte sinngemäß auf

\[
\text{Cross-Prime-Support von }U
\quad\perp\quad
\text{prime-pure Support von }C.
\]

C6o zeigt, dass beide Prämissen in der relevanten zusammengesetzten Form falsch typisiert sind:

1. `U` enthält same-prime und cross-prime Hubtripletts.
2. `C` besitzt zwar eine äußere Prime-Sektorzerlegung, aber jeder Sektorterm enthält innerlich alle Hublabels und globales Feshbach-Screening.
3. Der Targetresolvent muss nicht prime-blockdiagonal sein.
4. Ein kompletter Erstmodeanteil ist in `U` und `C` sogar algebraisch identisch.

Daher folgt aus den bisherigen Supportbefunden **keine** Unmöglichkeit

\[
\mathcal U_{R,T}=\mathcal C_{R,T}.
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,support\text{-}separation\text{-}route}.
}
\]

Diese Negativaussage ist eng zu lesen:

\[
\boxed{
\text{Sie widerlegt nicht }a_{R,T}^{(2)}\ne0.
}
\]

Sie widerlegt nur den Versuch, Nichtverschwindung allein aus einer groben Klassifikation `Hub=cross-prime`, `Rest=prime-pure` abzuleiten.

---

# 13. Was von der Cross-Prime-Struktur weiterhin nutzbar bleibt

C6e-C6j bleiben vollständig gültig.

Insbesondere existieren echte, quantitativ isolierbare Cross-Prime-Kanten in

\[
h_T=H_T^*H_T1_T,
\]

und die Restmetrik `A_T1_T` besitzt dort eine fundamental andere lokale Sprunggeometrie.

C6o sagt lediglich:

\[
\boxed{
\text{Nach Anwendung von }H_T^*,\ R_T,\ A_T^{-1}
\text{ ist diese lokale Supportasymmetrie nicht automatisch eine skalare Orthogonalität.}
}
\tag{C1zB2C6o.64}
\]

Die Cross-Prime-Struktur kann also weiterhin ein positiver Input für einen späteren quantitativen Korrelationsbeweis sein.

Aber sie muss **durch die konkrete residuale Paarung** transportiert werden.

---

# 14. Parität bleibt kompatibel, trennt aber ebenfalls nicht

Aus C6l/C6n:

- `g_{R,T}` liegt im ungeraden Source-Jetsektor;
- `J_{R,T}g_{R,T}` ist ungerade;
- `H_T^*` vertauscht die Parität, daher ist `b_{R,T}` gerade;
- `h_T`, `A_T1_T` und somit `r_T` sind gerade.

Also ist

\[
\boxed{
\langle b_{R,T},A_T^{-1}r_T\rangle
}
\]

paritätsmäßig zulässig.

Es gibt keine gerade/ungerade Orthogonalität, die den Alignment-Skalar automatisch null oder nichtnull macht.

Dies ist konsistent mit C6ns Vorzeichen-Firewall.

---

# 15. Reconciliation mit C6n: Winkel- und Screening-Sprache sind äquivalent

C6n definierte den Residualwinkel

\[
\rho_{R,T}^{(2)}
=
\frac{
|\langle b_{R,T},r_T\rangle_{A_T^{-1}}|^2
}{
\|b_{R,T}\|_{A_T^{-1}}^2
\|r_T\|_{A_T^{-1}}^2
}.
\]

C6o schreibt denselben Zähler als

\[
\langle b_{R,T},A_T^{-1}r_T\rangle
=
\langle b_{R,T},r_T\rangle
-
\langle b_{R,T},S_Tr_T\rangle.
\]

Damit ist

\[
\boxed{
\text{Residualwinkel}>0
\iff
\text{bare residuale Korrelation}
\ne
\text{residuale Screening-Korrelation}.
}
\tag{C1zB2C6o.65}
\]

Die beiden Sprachen beschreiben also exakt denselben offenen Punkt:

- C6n: geometrischer Winkel im `A_T^{-1}`-Hilbertraum;
- C6o: konkrete Nichtkompensation zwischen barem und gescreentem Residualkanal.

---

# 16. Was C6o nicht beweist

C6o beweist **nicht**

\[
a_{R,T}^{(2)}\ne0.
\]

Es beweist auch nicht

\[
\rho_{R,T}^{(2)}>0,
\]

keine untere Schranke für

\[
|\mathcal U_{R,T}^{\perp}|,
\]

und keine obere Schranke für

\[
\varepsilon_{b,T}^{\rm scr},
\qquad
\varepsilon_{r,T}^{\rm scr}.
\]

Insbesondere wird nicht behauptet, dass der Rest-Screeningterm asymptotisch kleiner als der bare Hubterm ist.

Diese Größen sind jetzt die echte quantitative Front.

---

# 17. No-Go-Persistenz

C6o supersediert keinen früheren Negativbefund.

Insbesondere bleiben bestehen:

- C1y: translationinvariante positive Regulatoren lösen den Hub/Rest-Konflikt nicht;
- C1z-B2-A: Gamma-Preconditioning liefert keinen fehlenden endlichen Schattenmechanismus;
- C1z-B2-B: naive Haar-L2-/Normresolvent-Route bleibt strukturell unzureichend;
- C4: unendliche Boundary-Jet-Hierarchie, kein fixer endlicher Jet stabilisiert die rohe Terminalgeometrie;
- C6: keine faithful vollständige Odd-Faktorisierung durch einen festen endlichen Jetquotienten;
- C6a: Self-Grams/Kompressionen bestimmen Cross-Terms nicht;
- C6b: C2-Flachheit allein kontrolliert keine principal-angle Cauchy-Geometrie;
- C6c: Triangularität/Rank-one-Daten erzwingen keine Tailkontrolle;
- C6d: Probeorthogonalität ist kein Jet-Alignment;
- C6k: vorhandene Daten erzwingen den Wronskian nicht;
- C6l: C4-Konstantenmode-Mechanismus überträgt sich nicht auf den Krylov-Residualbulk;
- C6m: `A_T`-Orthogonalität ist keine Bulk-Cancellation;
- C6n: Positivität und Rang 2 erzwingen keinen positiven Residualwinkel.

Neu hinzu kommt nur die engere Firewall:

\[
\boxed{
\text{grobe Hub/Rest-Supportklassifikation}
\not\Rightarrow
\text{Nichtkompensation im C6n-Skalar}.
}
\tag{C1zB2C6o.66}
\]

---

# 18. Gesamturteil

Die C6o-Vorüberlegung enthielt eine attraktive, aber zu starke Dichotomie:

\[
\mathcal U=\text{cross-prime},
\qquad
\mathcal C=\text{prime-pure}.
\]

Diese Dichotomie ist in der tatsächlichen Feshbach-Korrelation nicht korrekt.

Der präzise Befund lautet stattdessen:

\[
\boxed{
\begin{array}{c}
R_T^*R_T\text{ besitzt eine prime-sektorale Gramzerlegung},\\[1mm]
\text{aber }R_TR_T^*\text{ und }A_T^{-1}\text{ müssen nicht prime-sektoral entkoppeln},\\[1mm]
\text{und die eingesetzten Vektoren }b_{R,T},h_T\text{ sind bereits Hub-gemischt}.
\end{array}
}
\tag{C1zB2C6o.67}
\]

Gleichzeitig wird die offene Kompensationsfrage kleiner:

\[
\boxed{
\mathcal U_{R,T}
=
\underbrace{\lambda_T\langle Rb,R1\rangle}_{\text{erzwungen gemeinsam}}
+
\mathcal U_{R,T}^{\perp},
}
\]

\[
\boxed{
\mathcal C_{R,T}
=
\underbrace{\lambda_T\langle Rb,R1\rangle}_{\text{erzwungen gemeinsam}}
+
\mathcal C_{R,T}^{\perp}.
}
\]

Daher

\[
\boxed{
 a_{R,T}^{(2)}\ne0
\iff
\mathcal U_{R,T}^{\perp}
e\mathcal C_{R,T}^{\perp}.
}
\tag{C1zB2C6o.68}
\]

Und ein konkretes hinreichendes Kriterium ist

\[
\boxed{
|\mathcal U_{R,T}^{\perp}|
>
\sqrt{\varepsilon_{b,T}^{\rm scr}\varepsilon_{r,T}^{\rm scr}}.
}
\tag{C1zB2C6o.69}
\]

Dies ist die richtige quantitative Zielscheibe nach C6o.

---

# 19. Nächster atomarer Knoten

Der nächste zulässige Knoten sollte nicht noch einmal die rohe Supporttrennung von `U` und `C` versuchen.

Die natürliche Fortsetzung ist

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6p]
:
\text{Residual Bare-vs-Screened Separation.}
}
\]

Arbeitsauftrag:

1. Untersuche
   \[
   \mathcal U_{R,T}^{\perp}=\langle b_{R,T},r_T\rangle
   \]
   direkt in der konkreten Hubgeometrie.
2. Untersuche die Screeningenergien
   \[
   \varepsilon_{b,T}^{\rm scr}
   =\langle b,S_Tb\rangle,
   \qquad
   \varepsilon_{r,T}^{\rm scr}
   =\langle r,S_Tr\rangle.
   \]
3. Prüfe, ob C6e-C6j-Cross-Prime-Separation eine **untere** Schranke für die residuale Bare-Korrelation liefern kann, nachdem der erzwungene Erstmodeanteil entfernt wurde.
4. Prüfe unabhängig, ob die source-gekoppelte Resttiefe aus C6h/C6j eine **obere** Schranke für mindestens eine der Screeningenergien liefert.
5. Nur wenn
   \[
   |\mathcal U_{R,T}^{\perp}|
   >
   \sqrt{\varepsilon_{b,T}^{\rm scr}\varepsilon_{r,T}^{\rm scr}}
   \]
   eventual bewiesen werden kann, darf daraus `a_{R,T}^{(2)} != 0` geschlossen werden.

Bis dahin bleibt

\[
\boxed{
?[O]_{\rm residual\ angle>0}
}
\]

vollständig offen.

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.
