# P11-C1z-B2-C6r — Residuale Restladung, Momentorthogonalität und Fourier-Firewall

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6r]`  
**Direkte Voraussetzungen:** C1z-B, C1z-B2-C3, C1z-B2-C6h, C1z-B2-C6i, C1z-B2-C6j, C1z-B2-C6l, C1z-B2-C6m, C1z-B2-C6n, C1z-B2-C6o, C1z-B2-C6p, C1z-B2-C6q  
**Strukturelle Schnittstellen:** C1z-B2-C4, C1z-B2-C6a, C1z-B2-C6c, C1z-B2-C6d, C1z-B2-C6e, C1z-B2-C6f, C1z-B2-C6g, C1z-B2-C6k  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d `orthogonality != jet alignment`, C1z-B2-C6k `current data != Wronskian nonzero`, C1z-B2-C6l `C4 constant-mode mechanism does not transfer`, C1z-B2-C6m `A-orthogonality != bulk cancellation`, C1z-B2-C6n `positivity != alignment`, C1z-B2-C6o `raw support separation route fails`, C1z-B2-C6p `fixed-vector divergence != moving-vector control`, C1z-B2-C6q `cross-prime provenance != rest smallness`.  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6r]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm corr,residual\text{-}orthogonality}
+
\checkmark[M]_{\rm corr,source/target\text{-}typing}
+
\checkmark[M]_{\rm pos,exact\text{-}Rr\text{-}factorization}
+
\checkmark[M]_{\rm pos,arbitrary\text{-}rest\text{-}loading\text{-}data\text{-}separator}
+
\checkmark[M]_{\rm neg,moment\text{-}orthogonality\not\Rightarrow q_r\text{-}small}
+
\checkmark[M]_{\rm neg,Fourier\text{-}grid\text{-}route\text{-}without\text{-}translation\text{-}invariance}
+
\checkmark[M]_{\rm neg,C6h\text{-}local\text{-}rest\text{-}formula\not\Rightarrow r_T\text{-}rest\text{-}smallness}
+
\checkmark[M]_{\rm neg,componentwise\text{-}bounds\text{-}may\text{-}destroy\text{-}residual\text{-}cancellation}
+
?[O]_{\rm q_r\text{-}asymptotic}
+
?[O]_{\rm joint\text{-}Gramkernel\text{-}cancellation}
+
?[O]_{\rm bare\text{-}angle\text{-}lower\text{-}bound}
+
?[O]_{\rm second\text{-}alignment\text{-}scalar\neq0}
}
\]

C6q isolierte als nächsten asymptotischen Kandidaten

\[
\boxed{
q_{r,T}
:=
\frac{\|R_Tr_T\|^2}{\|r_T\|^2},
}
\]

mit

\[
\boxed{
r_T
=
h_T-\lambda_TA_T\mathbf1_T,
\qquad
h_T:=H_T^*H_T\mathbf1_T,
\qquad
A_T:=I+R_T^*R_T.
}
\]

C6r prüft nun die konkrete Vorüberlegung, ob die Residualorthogonalität von `r_T` oder eine daraus abgeleitete Fourier-/Momentenbedingung `q_{r,T}` klein machen könnte.

Das Ergebnis ist in dieser Form **negativ**.

Es gibt zwei notwendige Korrekturen:

1. Die exakte Residualorthogonalität lautet

\[
\boxed{
\langle r_T,\mathbf1_T\rangle=0,
}
\]

nicht `\langle r_T,A_T\mathbf1_T\rangle=0`.

2. Die typkorrekte Restidentität lautet

\[
\boxed{
R_Tr_T
=
R_Th_T
-
\lambda_T(I+R_TR_T^*)R_T\mathbf1_T.
}
\]

Eine Schreibweise `A_TR_T\mathbf1_T` ist typwidrig, weil `A_T` auf dem Source-Hilbertraum wirkt, während `R_T\mathbf1_T` im Rest-Targetraum liegt.

Noch schärfer zeigt ein zweidimensionales Datenmodell: Selbst wenn man die volle abstrakte Krylov-Struktur

\[
h=H^*H\mathbf1,
\qquad
r=h-\lambda A\mathbf1,
\qquad
\lambda=\frac{\langle h,\mathbf1\rangle}{\langle A\mathbf1,\mathbf1\rangle},
\qquad
r\perp\mathbf1
\]

erhält, kann

\[
q_r=\frac{\|Rr\|^2}{\|r\|^2}
\]
**beliebig vorgegeben** werden.

Damit folgt aus der Momentorthogonalität allein weder `q_r=o(1)` noch `q_r<1` noch irgendeine universelle Rest-Smallness.

Die explizite C6q-Gramkernel-Route bleibt dennoch vollständig offen: `q_{r,T}` ist bei festem `T` endlich und exakt berechenbar. C6r schließt nur die heuristische Abkürzung über globale Moment-/Fourierargumente.

---

# 0. Verbindliche Notation

Fixiere `R>0` und großes `T`.

Aus C6m–C6q:

\[
\boxed{
A_T
:=
I+R_T^*R_T
\ge I.
}
\tag{C1zB2C6r.1}
\]

\[
\boxed{
\mu_{T,0}
=
\langle\mathbf1_T,A_T\mathbf1_T\rangle,
\qquad
\mu_{T,1}
=
\langle\mathbf1_T,h_T\rangle
=
\|H_T\mathbf1_T\|^2.
}
\tag{C1zB2C6r.2}
\]

\[
\boxed{
\lambda_T
:=
\frac{\mu_{T,1}}{\mu_{T,0}}.
}
\tag{C1zB2C6r.3}
\]

\[
\boxed{
h_T
:=
H_T^*H_T\mathbf1_T.
}
\tag{C1zB2C6r.4}
\]

\[
\boxed{
r_T
:=
h_T-\lambda_TA_T\mathbf1_T.
}
\tag{C1zB2C6r.5}
\]

Der C6q-Restquotient ist

\[
\boxed{
q_{r,T}
=
\frac{\|R_Tr_T\|^2}{\|r_T\|^2}.
}
\tag{C1zB2C6r.6}
\]

C6q beweist bereits

\[
\boxed{
\|r_T\|^2\gtrsim e^{-4T}
}
\tag{C1zB2C6r.7}
\]

über den exakten C6i-Separator.

Diese Untergrenze trennt den Nenner quantitativ von null, sagt aber noch nichts über die Größe des Quotienten, solange `\|R_Tr_T\|` nicht kontrolliert ist.

---

# 1. Korrektur I — welche Orthogonalität gilt wirklich?

Aus der Definition von `lambda_T` folgt

\[
\begin{aligned}
\langle r_T,\mathbf1_T\rangle
&=
\langle h_T,\mathbf1_T\rangle
-
\lambda_T
\langle A_T\mathbf1_T,\mathbf1_T\rangle\\
&=
\mu_{T,1}
-
\frac{\mu_{T,1}}{\mu_{T,0}}\mu_{T,0}\\
&=0.
\end{aligned}
\]

Somit gilt exakt

\[
\boxed{
\langle r_T,\mathbf1_T\rangle=0.
}
\tag{C1zB2C6r.8}
\]

Dies ist die gewöhnliche `L^2`-Orthogonalität des Krylov-Residualvektors zur Konstantenmode.

Dagegen ist im Allgemeinen **nicht** bewiesen:

\[
\boxed{
\langle r_T,A_T\mathbf1_T\rangle=0.
}
\tag{C1zB2C6r.9}
\]

Die in C6l bewiesene `A_T`-Orthogonalität betrifft vielmehr

\[
\boxed{
y_T:=A_T^{-1}r_T.
}
\tag{C1zB2C6r.10}
\]

Für diesen Vektor gilt

\[
\boxed{
\langle y_T,A_T\mathbf1_T\rangle
=
\langle r_T,\mathbf1_T\rangle
=0.
}
\tag{C1zB2C6r.11}
\]

Äquivalent dazu ist `r_T` im `A_T^{-1}`-Skalarprodukt orthogonal zu `A_T\mathbf1_T`:

\[
\boxed{
\langle r_T,A_T\mathbf1_T\rangle_{A_T^{-1}}
:=
\langle r_T,A_T^{-1}A_T\mathbf1_T\rangle
=
0.
}
\tag{C1zB2C6r.12}
\]

Damit ist die in der Vorüberlegung verwendete gewöhnliche Orthogonalität

\[
\langle r_T,A_T\mathbf1_T\rangle=0
\]

zu stark und darf nicht als Ausgangspunkt einer Fourier- oder Rest-Smallness-Analyse verwendet werden.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,residual\text{-}orthogonality}.
}
\]

---

# 2. Korrektur II — typkorrekte Formel für `R_Tr_T`

Aus (C1zB2C6r.5):

\[
R_Tr_T
=
R_Th_T
-
\lambda_TR_TA_T\mathbf1_T.
\tag{C1zB2C6r.13}
\]

Da

\[
A_T
=
I+R_T^*R_T,
\]

folgt

\[
R_TA_T
=
R_T+R_TR_T^*R_T
=
(I+R_TR_T^*)R_T.
\tag{C1zB2C6r.14}
\]

Somit

\[
\boxed{
R_Tr_T
=
R_Th_T
-
\lambda_T(I+R_TR_T^*)R_T\mathbf1_T.
}
\tag{C1zB2C6r.15}
\]

Äquivalent:

\[
\boxed{
R_Tr_T
=
R_Th_T
-
\lambda_TR_T\mathbf1_T
-
\lambda_TR_TR_T^*R_T\mathbf1_T.
}
\tag{C1zB2C6r.16}
\]

Diese Formel ist vollständig **resolventenfrei**.

Wichtig ist aber die Typisierung:

- `A_T` wirkt auf dem Source-Hilbertraum;
- `R_T\mathbf1_T` liegt im Rest-Targetraum;
- daher ist `A_TR_T\mathbf1_T` nicht definiert;
- im Targetraum steht stattdessen `I+R_TR_T^*`.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,source/target\text{-}typing}
+
\checkmark[M]_{\rm pos,exact\text{-}Rr\text{-}factorization}.
}
\]

---

# 3. Exakte Quadratform für den Restquotienten

Da

\[
R_T^*R_T
=
A_T-I,
\]

gilt

\[
\boxed{
q_{r,T}
=
\frac{\langle r_T,(A_T-I)r_T\rangle}
{\|r_T\|^2}.
}
\tag{C1zB2C6r.17}
\]

Dies ist der Rayleigh-Quotient des positiven Operators `R_T^*R_T` auf dem einzelnen moving vector `r_T`.

Die Orthogonalität (C1zB2C6r.8) sagt lediglich, dass `r_T` im Hyperraum

\[
\mathbf1_T^\perp
\]

liegt.

Um daraus eine obere Schranke für `q_{r,T}` abzuleiten, bräuchte man eine zusätzliche Spektralaussage über `R_T^*R_T` auf genau diesem Hyperraum, zum Beispiel

\[
\sup\sigma\left((R_T^*R_T)|_{\mathbf1_T^\perp}\right)
=o(1),
\]

oder wenigstens eine vektorspezifische schwächere Variante.

Eine solche Aussage ist in der bisherigen C6-Kette nicht bewiesen.

Im Gegenteil ist der globale Operatorbound aus C6f/C6p

\[
\|R_T\|^2\lesssim Te^T
\]

für diese Richtung viel zu grob.

---

# 4. Eine einzige Momentbedingung kontrolliert keine Restladung

Die Bedingung

\[
\langle r_T,\mathbf1_T\rangle=0
\]

ist genau eine skalare Nullmomentbedingung.

Falls man auf `[-T,T]` eine Fouriertransformierte verwendet, impliziert sie höchstens die Nullheit der Nullfrequenz:

\[
\widehat r_T(0)=0
\]

unter der entsprechenden Fourierkonvention.

Sie sagt ohne weitere Struktur nichts über

\[
\widehat r_T(\xi)
\]

für nichtverschwindende Frequenzen `xi`, insbesondere nicht für logarithmische Prime-Power-Skalen.

Noch fundamentaler: Der P11-Restoperator ist durch die source-gekoppelte Tiefe

\[
J_{p,T}(u)
=
\max\left\{0,
\left\lfloor\frac{2(T-|u|)_+}{\log p}\right\rfloor
\right\}
\]

explizit `u`-abhängig.

Die Markvektoren

\[
q_{p,k,T}(u)
\]

hängen daher nicht nur vom Translationslabel `k\log p`, sondern auch vom Sourceort `u` ab.

Folglich ist

\[
R_T^*R_T
\]

kein translationskommutierender Fourier-Multiplikator.

Damit ist eine Aussage der Form

\[
q_{r,T}
\stackrel?=\
\text{gewichtete Fouriermasse von }r_T
\text{ an prime-pure Gitterpunkten}
\]

nicht aus der vorhandenen P11-Struktur ableitbar.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,moment\text{-}orthogonality\not\Rightarrow q_r\text{-}small}
+
\checkmark[M]_{\rm neg,Fourier\text{-}grid\text{-}route\text{-}without\text{-}translation\text{-}invariance}.
}
\]

Diese Firewall ist konsistent mit C1y: Gerade die source-gekoppelte Konditionierung wurde eingeführt, um die zu starre volle logarithmische Translationinvarianz zu brechen.

---

# 5. Scharfes Daten-No-Go: `q_r` kann beliebig sein

Die vorige Aussage lässt sich abstrakt scharf machen.

Das folgende Modell ist **kein P11-Gegenbeispiel**. Es zeigt nur, dass die algebraischen Konsequenzen

\[
A=I+R^*R,
\qquad
h=H^*H\mathbf1,
\qquad
r=h-\lambda A\mathbf1,
\qquad
r\perp\mathbf1,
\]

allein keine obere Schranke für

\[
q_r=\frac{\|Rr\|^2}{\|r\|^2}
\]

erzwingen.

Sei

\[
\mathscr H=\mathbb C^2
\]

mit Orthonormalbasis `e_0,e_1` und

\[
\mathbf1:=e_0.
\]

Fixiere einen beliebigen Parameter

\[
q\ge0.
\]

Definiere

\[
R_qe_0:=0,
\qquad
R_qe_1:=\sqrt q\,e_1.
\tag{C1zB2C6r.18}
\]

Dann

\[
R_q^*R_q
=
\begin{pmatrix}
0&0\\
0&q
\end{pmatrix},
\]

also

\[
\boxed{
A_q
:=
I+R_q^*R_q
=
\begin{pmatrix}
1&0\\
0&1+q
\end{pmatrix}.
}
\tag{C1zB2C6r.19}
\]

Fixiere ferner `lambda>0` und setze

\[
B_\lambda
:=
\begin{pmatrix}
\lambda&1\\
1&1+\lambda^{-1}
\end{pmatrix}.
\tag{C1zB2C6r.20}
\]

Dann

\[
\det B_\lambda
=
\lambda>0
\]

und `B_lambda>0`.

Es existiert daher ein Operator

\[
H_\lambda:=B_\lambda^{1/2}
\]

mit

\[
H_\lambda^*H_\lambda=B_\lambda.
\]

Nun ist

\[
\boxed{
h
:=
H_\lambda^*H_\lambda\mathbf1
=
B_\lambda e_0
=
\lambda e_0+e_1.
}
\tag{C1zB2C6r.21}
\]

Ferner

\[
\mu_0
:=
\langle\mathbf1,A_q\mathbf1\rangle
=1,
\]

und

\[
\mu_1
:=
\langle\mathbf1,h\rangle
=\lambda.
\]

Damit ist der Krylov-Koeffizient exakt

\[
\frac{\mu_1}{\mu_0}=\lambda.
\]

Der Residualvektor lautet

\[
\begin{aligned}
r
&=
h-\lambda A_q\mathbf1\\
&=
(\lambda e_0+e_1)-\lambda e_0\\
&=
\boxed{e_1}.
\end{aligned}
\tag{C1zB2C6r.22}
\]

Also

\[
\langle r,\mathbf1\rangle=0
\]

und zugleich

\[
\boxed{
q_r
=
\frac{\|R_qr\|^2}{\|r\|^2}
=q.
}
\tag{C1zB2C6r.23}
\]

Da `q>=0` beliebig war, kann der Restquotient in diesem Datenmodell

- null sein;
- zwischen null und eins liegen;
- gleich eins sein;
- beliebig groß sein.

Auch die Feshbach-Residualenergie bleibt positiv:

\[
\Delta
=
\langle r,A_q^{-1}r\rangle
=
\frac1{1+q}>0.
\tag{C1zB2C6r.24}
\]

Somit gelten gleichzeitig

\[
A=I+R^*R,
\qquad
h=H^*H\mathbf1,
\qquad
\lambda=\mu_1/\mu_0,
\qquad
r=h-\lambda A\mathbf1,
\qquad
r\perp\mathbf1,
\qquad
\Delta>0,
\]

während `q_r` völlig frei bleibt.

Daraus folgt die logische Firewall:

\[
\boxed{
\text{Krylov-Residualstruktur + Momentorthogonalität}
\not\Rightarrow
q_r\text{ klein}.
}
\tag{C1zB2C6r.25}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,arbitrary\text{-}rest\text{-}loading\text{-}data\text{-}separator}.
}
\]

---

# 6. Warum C6hs `1_T`-Mechanismus nicht überträgt

C6h konnte `R_T\mathbf1_T` und `R_T^*R_T\mathbf1_T` deshalb scharf kontrollieren, weil die Konstantenmode auf jeder vollständig im Fenster liegenden Translation exakt verschwindende Differenzen besitzt:

\[
K_{k\log p}\mathbf1_T(u)=0
\]

im inneren Bulkbereich.

Die verbleibenden Restbeiträge wurden dadurch auf source-gekoppelte Tiefenlagen reduziert und geometrisch summierbar.

Für `r_T` gibt es keine analoge Identität.

Die einzige globale Bedingung

\[
\int_{-T}^{T}r_T(u)\,du=0
\]

erzwingt nicht

\[
r_T(u+s)-r_T(u-s)=0.
\]

Daher bleibt im allgemeinen C6q-Gramkernel für `f=r_T` der volle Bulk erhalten:

\[
(K_{k\log p}r_T)(u)
=
r_T(u+k\log p/2)-r_T(u-k\log p/2)
\]

wann immer beide Punkte im Fenster liegen.

Die Cross-Prime-Breakpoint-Geometrie von `r_T` ändert daran nichts. Wie C6q bereits versiegelt hat, sieht `R_T` nach Einsetzen des skalaren Sourceprofils nicht mehr die Provenienz eines Sprungs.

Damit gilt weiterhin:

\[
\boxed{
\text{C6h-Spezialformel für }\mathbf1_T
\not\Rightarrow
\text{Rest-Smallness für }r_T.
}
\tag{C1zB2C6r.26}
\]

---

# 7. Explizite residuelle Restzerlegung — aber mit möglicher großer Cancellation

Aus (C1zB2C6r.16) folgt

\[
R_Tr_T
=
R_Th_T
-
\lambda_TR_T\mathbf1_T
-
\lambda_TR_TR_T^*R_T\mathbf1_T.
\]

Setze

\[
X_T:=R_Th_T,
\qquad
Y_T:=\lambda_TR_T\mathbf1_T,
\qquad
Z_T:=\lambda_TR_TR_T^*R_T\mathbf1_T.
\]

Dann

\[
\boxed{
R_Tr_T=X_T-Y_T-Z_T.
}
\tag{C1zB2C6r.27}
\]

Somit

\[
\boxed{
\begin{aligned}
\|R_Tr_T\|^2
&=
\|X_T\|^2+\|Y_T\|^2+\|Z_T\|^2\\
&\quad
-2\Re\langle X_T,Y_T\rangle
-2\Re\langle X_T,Z_T\rangle
+2\Re\langle Y_T,Z_T\rangle.
\end{aligned}
}
\tag{C1zB2C6r.28}
\]

Dies ist vollständig resolventenfrei.

Aber genau hier erscheint eine neue Firewall:

`r_T` ist per Konstruktion ein Residuum. Es ist daher möglich, dass einzelne Summanden `X_T,Y_T,Z_T` groß sind, während ihre Kombination klein ist.

Eine rein komponentenweise Dreiecksabschätzung

\[
\|R_Tr_T\|
\le
\|X_T\|+\|Y_T\|+\|Z_T\|
\]

kann diese Cancellation vollständig zerstören und deshalb für einen Smallness-Beweis strukturell zu grob sein.

Der richtige asymptotische Gegenstand ist die **gemeinsame Gramstruktur** der drei Terme in (C1zB2C6r.28), nicht nur ihre getrennten Normen.

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,componentwise\text{-}bounds\text{-}may\text{-}destroy\text{-}residual\text{-}cancellation}.
}
\]

---

# 8. Was die C6q-Gramkernel-Formel tatsächlich leistet

C6q beweist für jeden Sourcevektor `f` exakt

\[
\begin{aligned}
\|R_Tf\|^2
&=
\sum_p
\int_{-T}^{T}
\sum_{k,\ell\ge1}
(\log p)
 p^{-3(k+\ell)/4}
\left(
 p^{d_{p,T}(u;k,\ell)}-1
\right)\\
&\qquad\qquad\qquad\times
(K_{k\log p}f)(u)
\overline{(K_{\ell\log p}f)(u)}
\,du,
\end{aligned}
\tag{C1zB2C6r.29}
\]

mit

\[
d_{p,T}(u;k,\ell)
=
\min\{k,\ell,J_{p,T}(u)\}.
\]

Für `f=r_T` ist dies eine **exakte endliche Formel** für den Zähler von `q_{r,T}`.

C6r zeigt nicht, dass diese Formel asymptotisch unzugänglich wäre. Im Gegenteil: sie ist jetzt die verbindliche Route.

Was C6r ausschließt, ist nur die Behauptung, dass die Formel aufgrund einer globalen Orthogonalitäts- oder Fourierbedingung automatisch klein sein müsse.

Die verbleibende Aufgabe ist daher wirklich arithmetisch-analytisch:

1. `r_T` stückweise explizit darstellen;
2. die Translationen `K_{k\log p}r_T` in den Tiefenlagen des Gramkernels einsetzen;
3. die Kreuzterme des Residuals **gemeinsam** summieren;
4. erst danach entscheiden, ob

\[
q_{r,T}=o(1),
\]

`O(1)`, divergent oder oszillierend ist.

---

# 9. Konsequenz für das Alignmentprogramm

C6p gab das hinreichende Kriterium

\[
\beta_{R,T}
>
\sqrt{
\frac{q_{b,T}q_{r,T}}
{(1+q_{b,T})(1+q_{r,T})}
}
\quad\Longrightarrow\quad
 a_{R,T}^{(2)}\ne0.
\tag{C1zB2C6r.30}
\]

Die Hoffnung war, `q_{r,T}` vielleicht aus der Krylov-Residualorthogonalität fast kostenlos klein zu bekommen.

C6r schließt genau diese Hoffnung aus:

\[
\boxed{
\text{Residualorthogonalität allein liefert keinen kleinen }q_{r,T}.
}
\tag{C1zB2C6r.31}
\]

Damit bleibt `q_r` zwar der **am explizitesten zugängliche** der drei Parameter, aber nicht der bereits kontrollierte.

Die praktische Reihenfolge bleibt deshalb:

\[
\boxed{
q_{r,T}
\longrightarrow
\beta_{R,T}
\longrightarrow
q_{b,T},
}
\]

mit einer entscheidenden Präzisierung:

`q_r` muss aus der vollen C6q-Prime-Power-Quadratform gewonnen werden, nicht aus einem allgemeinen Moment- oder Fourierargument.

---

# 10. Status und nächster Knoten

C6r versiegelt:

\[
\boxed{
\begin{aligned}
&\checkmark[M]_{\rm corr,residual\text{-}orthogonality}\\
+{}&\checkmark[M]_{\rm corr,source/target\text{-}typing}\\
+{}&\checkmark[M]_{\rm pos,exact\text{-}Rr\text{-}factorization}\\
+{}&\checkmark[M]_{\rm pos,arbitrary\text{-}rest\text{-}loading\text{-}data\text{-}separator}\\
+{}&\checkmark[M]_{\rm neg,moment\text{-}orthogonality\not\Rightarrow q_r\text{-}small}\\
+{}&\checkmark[M]_{\rm neg,Fourier\text{-}grid\text{-}route\text{-}without\text{-}translation\text{-}invariance}\\
+{}&\checkmark[M]_{\rm neg,C6h\text{-}local\text{-}formula\not\Rightarrow r_T\text{-}smallness}\\
+{}&\checkmark[M]_{\rm neg,componentwise\text{-}bounds\text{-}may\text{-}destroy\text{-}residual\text{-}cancellation}.
\end{aligned}
}
\]

Offen bleiben:

\[
?[O]_{q_r\text{-}asymptotic},
\qquad
?[O]_{joint\text{-}Gramkernel\text{-}cancellation},
\qquad
?[O]_{bare\text{-}angle\text{-}lower\text{-}bound},
\qquad
?[O]_{second\text{-}alignment\text{-}scalar\neq0}.
\]

Der nächste zulässige Knoten ist deshalb

\[
\boxed{
\text{C6s: Joint Residual Gramkernel Expansion.}
}
\]

Nicht mehr fragen, ob eine abstrakte Orthogonalität `q_r` klein macht. Stattdessen soll C6s die drei Komponenten

\[
R_Th_T,
\qquad
\lambda_TR_T\mathbf1_T,
\qquad
\lambda_TR_TR_T^*R_T\mathbf1_T
\]

im **selben** Prime-Power-Gramkernel entwickeln und nach den tatsächlich überlebenden Haupttermen bzw. Cancellations klassifizieren.

Nur daraus kann eine belastbare Asymptotik von `q_{r,T}` entstehen.
