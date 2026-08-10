# P11-C1z-B2-C6s — Gemeinsamer Residual-Gramkern, Martingalquadrate und Rest-Regression

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6s]`  
**Direkte Voraussetzungen:** C1z-B, C1z-B2-C3, C1z-B2-C6h, C1z-B2-C6i, C1z-B2-C6j, C1z-B2-C6l, C1z-B2-C6m, C1z-B2-C6n, C1z-B2-C6o, C1z-B2-C6p, C1z-B2-C6q, C1z-B2-C6r  
**Strukturelle Schnittstellen:** C1z-B2-C4, C1z-B2-C6a, C1z-B2-C6c, C1z-B2-C6d, C1z-B2-C6e, C1z-B2-C6f, C1z-B2-C6g, C1z-B2-C6k  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4 Finite-Jet-No-Go, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos, C1z-B2-C6b C2-Flachheits-No-Go, C1z-B2-C6c Triangularitäts-/Rank-one-No-Gos, C1z-B2-C6d `orthogonality != jet alignment`, C1z-B2-C6k `current data != Wronskian nonzero`, C1z-B2-C6l `C4 constant-mode mechanism does not transfer`, C1z-B2-C6m `A-orthogonality != bulk cancellation`, C1z-B2-C6n `positivity != alignment`, C1z-B2-C6o `raw support separation route fails`, C1z-B2-C6p `fixed-vector divergence != moving-vector control`, C1z-B2-C6q `cross-prime provenance != rest smallness`, C1z-B2-C6r `moment orthogonality != q_r small`.  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6s]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm pos,rest\text{-}bilinear\text{-}polarization}
+
\checkmark[M]_{\rm pos,six\text{-}to\text{-}three\text{-}Gram\text{-}collapse}
+
\checkmark[M]_{\rm pos,martingale\text{-}square\text{-}factorization}
+
\checkmark[M]_{\rm pos,channelwise\text{-}residual\text{-}squares}
+
\checkmark[M]_{\rm pos,rest\text{-}regression\text{-}decomposition}
+
\checkmark[M]_{\rm pos,no\text{-}cross\text{-}channel\text{-}cancellation}
+
\checkmark[M]_{\rm corr,heuristic\text{-}size\text{-}scales\text{-}unproved}
+
\checkmark[M]_{\rm neg,same\text{-}order\not\Rightarrow cancellation}
+
\checkmark[M]_{\rm neg,separate\text{-}component\text{-}bounds\text{-}route}
+
?[O]_{\rm q_r\text{-}asymptotic}
+
?[O]_{\rm channelwise\text{-}rest\text{-}locking}
+
?[O]_{\rm bare\text{-}angle\text{-}lower\text{-}bound}
+
?[O]_{\rm second\text{-}alignment\text{-}scalar\neq0}
}
\]

C6r zeigte, dass die abstrakte Residualorthogonalität und eine Fourier-Abkürzung keine Rest-Smallness erzwingen. Der noch zulässige Weg ist die **konkrete gemeinsame Auswertung** des C6q-Rest-Gramkerns auf

\[
\boxed{
 r_T=h_T-\lambda_TA_T\mathbf1_T.
}
\]

C6s führt genau diese gemeinsame Auswertung auf struktureller Ebene durch, bevor irgendeine asymptotische Abschätzung vorgenommen wird.

Der Hauptbefund ist stärker als die naive Sechs-Term-Expansion von

\[
R_Tr_T=X_T-Y_T-Z_T.
\]

Die drei Vektoren `Y_T` und `Z_T` gehören algebraisch zusammen. Setzt man

\[
\boxed{
 a_T:=A_T\mathbf1_T
 =\mathbf1_T+R_T^*R_T\mathbf1_T,
}
\]

so gilt

\[
\boxed{
Y_T+Z_T
=\lambda_TR_Ta_T
}
\]

und daher

\[
\boxed{
R_Tr_T
=R_Th_T-\lambda_TR_Ta_T.
}
\]

Die vollständige Sechs-Term-Struktur kollabiert damit exakt auf **drei gemeinsame Rest-Grameinträge**. Noch stärker lässt sich der C6q-Gramkern in der p-adischen Martingalbasis zu einer Summe echter Quadrate faktorisieren. Für das Residuum entsteht dadurch eine kanalweise Formel

\[
\boxed{
\|R_Tr_T\|^2
=
\sum_{p,a}
\text{positives Gewicht}
\times
\|\text{Hubkanal}_{p,a}-\lambda_T\text{Restmode}_{p,a}\|_{L^2}^2.
}
\]

Somit kann es **keine Cancellation zwischen verschiedenen Primzahlen, Martingalstufen oder Tiefenlagen** geben. Alle mögliche Cancellation sitzt innerhalb desselben Kanals.

Dies ist die korrekte analytische Form des in C6r geforderten gemeinsamen Gramkernel-Ansatzes.

---

# 0. Verbindliche Notation

Fixiere `R>0` und großes `T`.

Wie in C6q/C6r:

\[
\boxed{
A_T:=I+R_T^*R_T\ge I.
}
\tag{C1zB2C6s.1}
\]

\[
\boxed{
h_T:=H_T^*H_T\mathbf1_T.
}
\tag{C1zB2C6s.2}
\]

\[
\boxed{
\lambda_T
:=
\frac{\mu_{T,1}}{\mu_{T,0}}
=
\frac{\|H_T\mathbf1_T\|^2}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}
\in[0,\infty).
}
\tag{C1zB2C6s.3}
\]

\[
\boxed{
r_T:=h_T-\lambda_TA_T\mathbf1_T.
}
\tag{C1zB2C6s.4}
\]

C6r korrigierte die exakte Orthogonalität zu

\[
\boxed{
\langle r_T,\mathbf1_T\rangle=0.
}
\tag{C1zB2C6s.5}
\]

Der zu untersuchende Restquotient ist

\[
\boxed{
q_{r,T}
:=
\frac{\|R_Tr_T\|^2}{\|r_T\|^2}.
}
\tag{C1zB2C6s.6}
\]

C6q/C6r geben bereits

\[
\boxed{
\|r_T\|^2\gtrsim e^{-4T},
}
\tag{C1zB2C6s.7}
\]

aber noch keine hinreichende obere Schranke für den Zähler.

Setze zur Abkürzung

\[
\boxed{
a_T:=A_T\mathbf1_T.
}
\tag{C1zB2C6s.8}
\]

Dann ist schlicht

\[
\boxed{
r_T=h_T-\lambda_Ta_T.
}
\tag{C1zB2C6s.9}
\]

---

# 1. Die naive Sechs-Term-Zerlegung und ihre richtige Gruppierung

C6r schrieb typkorrekt

\[
R_Tr_T
=
R_Th_T
-
\lambda_TR_T\mathbf1_T
-
\lambda_TR_TR_T^*R_T\mathbf1_T.
\tag{C1zB2C6s.10}
\]

Bezeichne informell

\[
X_T:=R_Th_T,
\]

\[
Y_T:=\lambda_TR_T\mathbf1_T,
\]

\[
Z_T:=\lambda_TR_TR_T^*R_T\mathbf1_T.
\]

Dann

\[
R_Tr_T=X_T-Y_T-Z_T.
\]

Eine direkte Normexpansion liefert sechs reelle Beiträge:

\[
\begin{aligned}
\|R_Tr_T\|^2
&=
\|X_T\|^2
+\|Y_T\|^2
+\|Z_T\|^2\\
&\quad
-2\Re\langle X_T,Y_T\rangle
-2\Re\langle X_T,Z_T\rangle
+2\Re\langle Y_T,Z_T\rangle.
\end{aligned}
\tag{C1zB2C6s.11}
\]

Diese Formel ist korrekt, aber sie ist **nicht die optimale Rechenform**.

Denn

\[
R_Ta_T
=
R_TA_T\mathbf1_T
=
R_T\mathbf1_T
+R_TR_T^*R_T\mathbf1_T.
\]

Daher

\[
\boxed{
Y_T+Z_T
=
\lambda_TR_Ta_T.
}
\tag{C1zB2C6s.12}
\]

und somit

\[
\boxed{
R_Tr_T
=R_Th_T-\lambda_TR_Ta_T.
}
\tag{C1zB2C6s.13}
\]

Diese Gruppierung ist zwingend, wenn die Residual-Cancellation nicht durch separate Dreiecks- oder Cauchy-Schranken zerstört werden soll.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,six\text{-}to\text{-}three\text{-}Gram\text{-}collapse}.
}
\]

---

# 2. Hermitesche Rest-Bilinearform

Definiere auf dem Source-Hilbertraum

\[
\boxed{
\mathfrak R_T(f,g)
:=
\langle R_Tf,R_Tg\rangle.
}
\tag{C1zB2C6s.14}
\]

Dann ist `mathfrak R_T` hermitesch und positiv semidefinit:

\[
\mathfrak R_T(g,f)
=
\overline{\mathfrak R_T(f,g)},
\]

\[
\mathfrak R_T(f,f)
=
\|R_Tf\|^2\ge0.
\]

Die C6q-Quadratform polarisiert exakt zu

\[
\boxed{
\begin{aligned}
\mathfrak R_T(f,g)
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
\overline{(K_{\ell\log p}g)(u)}
\,du,
\end{aligned}
}
\tag{C1zB2C6s.15}
\]

mit

\[
\boxed{
d_{p,T}(u;k,\ell)
:=
\min\{k,\ell,J_{p,T}(u)\}.
}
\tag{C1zB2C6s.16}
\]

Für `f=g` reproduziert (C1zB2C6s.15) exakt C6q.

Da `lambda_T` reell ist, folgt aus (C1zB2C6s.13):

\[
\boxed{
\begin{aligned}
\|R_Tr_T\|^2
&=
\mathfrak R_T(h_T,h_T)
-2\lambda_T\Re\mathfrak R_T(h_T,a_T)
+\lambda_T^2\mathfrak R_T(a_T,a_T).
\end{aligned}
}
\tag{C1zB2C6s.17}
\]

Dies sind genau die drei gemeinsamen Gramgrößen

\[
\boxed{
\mathfrak R_T(h_T,h_T),
\qquad
\Re\mathfrak R_T(h_T,a_T),
\qquad
\mathfrak R_T(a_T,a_T).
}
\tag{C1zB2C6s.18}
\]

Die sechs Terme aus (C1zB2C6s.11) sind darin vollständig enthalten; nichts wurde approximiert oder verworfen.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,rest\text{-}bilinear\text{-}polarization}.
}
\]

---

# 3. C6q-Gramkernel als Summe von Martingalquadraten

Der C6q-Gramkernel besitzt zusätzliche Struktur, die in der Doppelsummenform noch verborgen ist.

Für ganzzahliges `j>=1` gilt

\[
p^{\min(k,\ell,j)}-1
=
(p-1)
\sum_{a=0}^{j-1}
p^a
\mathbf1_{\{k\ge a+1\}}
\mathbf1_{\{\ell\ge a+1\}}.
\tag{C1zB2C6s.19}
\]

Denn die rechte Seite summiert exakt

\[
(p-1)\sum_{a=0}^{\min(k,\ell,j)-1}p^a
=
p^{\min(k,\ell,j)}-1.
\]

Definiere für jede Primzahl `p` und Martingalstufe `a>=0`

\[
\boxed{
\Omega_{p,a,T}
:=
\{u\in[-T,T]:J_{p,T}(u)\ge a+1\}.
}
\tag{C1zB2C6s.20}
\]

Aus

\[
J_{p,T}(u)
=
\max\left\{0,
\left\lfloor
\frac{2(T-|u|)_+}{\log p}
\right\rfloor
\right\}
\]

folgt bis auf maßtheoretisch irrelevante Randpunkte

\[
\boxed{
\Omega_{p,a,T}
=
\left\{
|u|
\le
T-\frac{a+1}{2}\log p
\right\},
}
\tag{C1zB2C6s.21}
\]

sofern die rechte Seite nicht leer ist.

Weiter definiere den skalaren Translations-Tail

\[
\boxed{
\Phi_{p,a,T}[f](u)
:=
\sum_{k\ge a+1}
p^{-3k/4}
(K_{k\log p}f)(u).
}
\tag{C1zB2C6s.22}
\]

Bei festem `T` ist die effektiv aktive Summe endlich.

Setzt man (C1zB2C6s.19) in (C1zB2C6s.15) ein und vertauscht die endlichen Summen, erhält man exakt

\[
\boxed{
\begin{aligned}
\mathfrak R_T(f,g)
&=
\sum_p
(\log p)(p-1)
\sum_{a\ge0}
p^a
\int_{\Omega_{p,a,T}}
\Phi_{p,a,T}[f](u)
\overline{\Phi_{p,a,T}[g](u)}
\,du.
\end{aligned}
}
\tag{C1zB2C6s.23}
\]

Insbesondere

\[
\boxed{
\|R_Tf\|^2
=
\sum_p
(\log p)(p-1)
\sum_{a\ge0}
p^a
\int_{\Omega_{p,a,T}}
|\Phi_{p,a,T}[f](u)|^2
\,du.
}
\tag{C1zB2C6s.24}
\]

Dies ist die **Martingalquadrat-Faktorisierung** des C6q-Gramkerns.

Sie ist exakt dieselbe Geometrie wie die orthonormalen Martingalvektoren `psi_{p,a}` aus C1z-B/C6h, nun jedoch vollständig auf die skalare Sourcefunktion zurücktransportiert.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,martingale\text{-}square\text{-}factorization}.
}
\]

---

# 4. Exakte gemeinsame Residualformel

Wende (C1zB2C6s.24) direkt auf

\[
r_T=h_T-\lambda_Ta_T
\]

an.

Wegen der Linearität von `Phi_{p,a,T}` gilt

\[
\Phi_{p,a,T}[r_T]
=
\Phi_{p,a,T}[h_T]
-
\lambda_T\Phi_{p,a,T}[a_T].
\tag{C1zB2C6s.25}
\]

Daher folgt die zentrale C6s-Identität:

\[
\boxed{
\begin{aligned}
\|R_Tr_T\|^2
&=
\sum_p
(\log p)(p-1)
\sum_{a\ge0}
p^a
\int_{\Omega_{p,a,T}}
\left|
\Phi_{p,a,T}[h_T](u)
-
\lambda_T\Phi_{p,a,T}[a_T](u)
\right|^2
\,du.
\end{aligned}
}
\tag{C1zB2C6s.26}
\]

Dies ist die gesuchte **gemeinsame Gramkernel-Expansion**, aber in einer stärkeren Form als eine bloße Ausmultiplizierung der sechs Kreuzterme.

Jeder einzelne Summand in (C1zB2C6s.26) ist nichtnegativ.

Damit gilt:

\[
\boxed{
\text{Cancellation kann nur innerhalb desselben }(p,a,u)\text{-Kanals auftreten.}
}
\tag{C1zB2C6s.27}
\]

Insbesondere gibt es keine Cancellation

- zwischen verschiedenen Primzahlen `p`;
- zwischen verschiedenen Martingalstufen `a`;
- zwischen disjunkten Sourcebereichen innerhalb der Integrale;
- erst recht nicht zwischen einer positiven Energie eines Primkanals und einer negativen Energie eines anderen Primkanals.

Das ist stärker als die bloße Warnung aus C6r, separate Normabschätzungen könnten Cancellation zerstören. C6s lokalisiert jetzt exakt, **wo** die zulässige Cancellation überhaupt sitzt.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,channelwise\text{-}residual\text{-}squares}
+
\checkmark[M]_{\rm pos,no\text{-}cross\text{-}channel\text{-}cancellation}.
}
\]

---

# 5. Tiefenlagenform der Quadratsumme

Alternativ kann man nach exakten Tiefenlagen zerlegen.

Definiere

\[
D_{p,j,T}
:=
\{u\in[-T,T]:J_{p,T}(u)=j\},
\qquad j\ge0.
\tag{C1zB2C6s.28}
\]

Auf `D_{p,j,T}` ist der Kernel konstant in der Tiefenvariable:

\[
G_{p,j}(k,\ell)
:=
(\log p)
p^{-3(k+\ell)/4}
\left(
p^{\min(k,\ell,j)}-1
\right).
\tag{C1zB2C6s.29}
\]

Für `j=0` verschwindet er.

Für `j>=1` ist

\[
G_{p,j}(k,\ell)
=
(\log p)(p-1)
\sum_{a=0}^{j-1}
p^a
p^{-3k/4}p^{-3\ell/4}
\mathbf1_{k\ge a+1}
\mathbf1_{\ell\ge a+1}.
\tag{C1zB2C6s.30}
\]

Der `k,ell`-Kernel auf einer Tiefe `j` hat damit Rang höchstens `j` in der Martingalzerlegung.

Für `j=1` ist er sogar Rang eins:

\[
\boxed{
G_{p,1}(k,\ell)
=
(\log p)(p-1)
p^{-3k/4}p^{-3\ell/4}.
}
\tag{C1zB2C6s.31}
\]

Das macht die erste p-adische Tiefenlage zu einem besonders natürlichen Kandidaten für einen späteren expliziten Asymptotiktest.

---

# 6. Rest-Regression: welche Cancellation wäre überhaupt nötig?

Setze im Rest-Targetraum

\[
\boxed{
U_T:=R_Th_T,
\qquad
V_T:=R_Ta_T.
}
\tag{C1zB2C6s.32}
\]

Dann

\[
\boxed{
R_Tr_T=U_T-\lambda_TV_T.
}
\tag{C1zB2C6s.33}
\]

Falls `V_T=0`, gibt es keine `a_T`-Restkompensation und

\[
\|R_Tr_T\|^2=\|U_T\|^2.
\]

Sei nun `V_T!=0`.

Da `lambda_T` reell ist, definiere den reell optimalen Rest-Regressionskoeffizienten

\[
\boxed{
\lambda_T^{\rm rest}
:=
\frac{
\Re\langle U_T,V_T\rangle
}{
\|V_T\|^2
}.
}
\tag{C1zB2C6s.34}
\]

Dieser Koeffizient minimiert

\[
c\longmapsto\|U_T-cV_T\|^2
\]

über `c in R`.

Daher gilt exakt die Pythagoras-/Least-Squares-Zerlegung

\[
\boxed{
\|U_T-\lambda_TV_T\|^2
=
\|U_T-\lambda_T^{\rm rest}V_T\|^2
+
\|V_T\|^2
(\lambda_T-\lambda_T^{\rm rest})^2.
}
\tag{C1zB2C6s.35}
\]

Definiere ferner, sofern `U_T,V_T` beide nicht null sind,

\[
\boxed{
\chi_T^{\rm rest}
:=
\frac{
\Re\langle U_T,V_T\rangle
}{
\|U_T\|\,\|V_T\|}
\in[-1,1].
}
\tag{C1zB2C6s.36}
\]

Dann

\[
\lambda_T^{\rm rest}
=
\chi_T^{\rm rest}
\frac{\|U_T\|}{\|V_T\|}
\]

und

\[
\boxed{
\|U_T-\lambda_T^{\rm rest}V_T\|^2
=
\|U_T\|^2
\left(
1-(\chi_T^{\rm rest})^2
\right).
}
\tag{C1zB2C6s.37}
\]

Somit erhält man die zweite zentrale C6s-Identität:

\[
\boxed{
\begin{aligned}
\|R_Tr_T\|^2
&=
\|R_Th_T\|^2
\left(
1-(\chi_T^{\rm rest})^2
\right)\\
&\quad+
\|R_TA_T\mathbf1_T\|^2
\left(
\lambda_T-\lambda_T^{\rm rest}
\right)^2.
\end{aligned}
}
\tag{C1zB2C6s.38}
\]

Die Formel zeigt exakt, welche zwei Bedingungen für eine kleine Restladung nötig sind:

1. **Rest-Winkel-Locking:**

\[
|\chi_T^{\rm rest}|\approx1;
\]

2. **Koeffizienten-Locking:**

\[
\lambda_T
\approx
\lambda_T^{\rm rest}.
\]

Gleiche Größenordnung von `||U_T||` und `lambda_T||V_T||` liefert keine dieser beiden Aussagen.

Status:

\[
\boxed{
\checkmark[M]_{\rm pos,rest\text{-}regression\text{-}decomposition}
+
\checkmark[M]_{\rm neg,same\text{-}order\not\Rightarrow cancellation}.
}
\]

---

# 7. Der Krylov-Koeffizient ist nicht der Rest-Regressionskoeffizient

Der Krylov-Koeffizient ist

\[
\boxed{
\lambda_T
=
\frac{
\langle h_T,\mathbf1_T\rangle
}{
\langle a_T,\mathbf1_T\rangle
}.
}
\tag{C1zB2C6s.39}
\]

Er wird also durch eine **Source-L2-Observation an der Konstantenmode** bestimmt.

Der Rest-Regressionskoeffizient ist dagegen

\[
\boxed{
\lambda_T^{\rm rest}
=
\frac{
\Re\mathfrak R_T(h_T,a_T)
}{
\mathfrak R_T(a_T,a_T)
}.
}
\tag{C1zB2C6s.40}
\]

sofern der Nenner nicht null ist.

Da

\[
\mathfrak R_T(f,g)
=
\langle f,(A_T-I)g\rangle,
\]

kann man schreiben

\[
\mathfrak R_T(h_T,a_T)
=
\langle h_T,(A_T-I)A_T\mathbf1_T\rangle
=
\langle h_T,(A_T^2-A_T)\mathbf1_T\rangle,
\tag{C1zB2C6s.41}
\]

und

\[
\mathfrak R_T(a_T,a_T)
=
\langle A_T\mathbf1_T,(A_T-I)A_T\mathbf1_T\rangle.
\tag{C1zB2C6s.42}
\]

Somit liegt zwischen `lambda_T` und `lambda_T^{rest}` keine bekannte abstrakte Identität.

Insbesondere folgt aus der Definition von `lambda_T` nicht

\[
\lambda_T=\lambda_T^{\rm rest}.
\]

Eine solche Gleichheit oder asymptotische Annäherung wäre ein neuer P11-spezifischer Satz.

---

# 8. Kanalweise Regression und die stärkere No-Cross-Cancellation-Aussage

Für jeden Kanal `(p,a)` definiere

\[
\mathcal H_{p,a,T}
:=
L^2(\Omega_{p,a,T},du)
\]

und

\[
\boxed{
U_{p,a,T}
:=
\sqrt{(\log p)(p-1)p^a}\,
\Phi_{p,a,T}[h_T],
}
\tag{C1zB2C6s.43}
\]

\[
\boxed{
V_{p,a,T}
:=
\sqrt{(\log p)(p-1)p^a}\,
\Phi_{p,a,T}[a_T].
}
\tag{C1zB2C6s.44}
\]

Dann ist

\[
\boxed{
\|R_Tr_T\|^2
=
\sum_{p,a}
\|U_{p,a,T}-\lambda_TV_{p,a,T}\|_{\mathcal H_{p,a,T}}^2.
}
\tag{C1zB2C6s.45}
\]

Für jeden Kanal mit `V_{p,a,T}!=0` kann man einen lokalen Regressionskoeffizienten definieren:

\[
\boxed{
\lambda_{p,a,T}^{\rm rest}
:=
\frac{
\Re\langle U_{p,a,T},V_{p,a,T}\rangle
}{
\|V_{p,a,T}\|^2.
}
\tag{C1zB2C6s.46}
\]

Dann

\[
\boxed{
\begin{aligned}
\|U_{p,a,T}-\lambda_TV_{p,a,T}\|^2
&=
\|U_{p,a,T}-\lambda_{p,a,T}^{\rm rest}V_{p,a,T}\|^2\\
&\quad+
\|V_{p,a,T}\|^2
(\lambda_T-\lambda_{p,a,T}^{\rm rest})^2.
\end{aligned}
}
\tag{C1zB2C6s.47}
\]

Daraus folgt eine besonders starke notwendige Bedingung für kleine Gesamt-Restladung:

\[
\boxed{
q_{r,T}\text{ klein}
\Longrightarrow
\text{alle gewichtsstarken Kanäle müssen gleichzeitig}
\begin{cases}
U_{p,a,T}\approx \lambda_{p,a,T}^{\rm rest}V_{p,a,T},\\
\lambda_{p,a,T}^{\rm rest}\approx\lambda_T
\end{cases}
\text{ erfüllen.}
}
\tag{C1zB2C6s.48}
\]

Es reicht nicht, wenn ein Primkanal eine Überkompensation und ein anderer eine Unterkompensation besitzt: die Energien addieren sich positiv.

Das ist der präzise Inhalt von

\[
\boxed{
\text{keine Cross-Prime-/Cross-Depth-Cancellation im Restzähler}.
}
\tag{C1zB2C6s.49}
\]

---

# 9. Ein einzelner Kanal kann eine Rest-Smallness widerlegen

Aus (C1zB2C6s.45) folgt für jedes feste `(p,a)` sofort

\[
\boxed{
q_{r,T}
\ge
\frac{
\|U_{p,a,T}-\lambda_TV_{p,a,T}\|^2
}{
\|r_T\|^2
}.
}
\tag{C1zB2C6s.50}
\]

Daher genügt für eine untere Schranke an `q_{r,T}` ein einziger Kanal.

Zum Beispiel würde

\[
\|U_{p,a,T}-\lambda_TV_{p,a,T}\|^2
\ge
c\,\|r_T\|^2
\]

für eine Folge großer `T` bereits

\[
q_{r,T}\ge c
\]

auf dieser Folge liefern.

Umgekehrt ist ein Beweis von

\[
q_{r,T}=o(1)
\]

strenger: Er muss die **Summe aller nichtnegativen Kanäle** kontrollieren.

Das zeigt, dass die gemeinsame Gramkernel-Form besonders gut geeignet ist, eine falsche Rest-Smallness-Hoffnung durch einen einzigen stabilen Kanal zu widerlegen.

---

# 10. Die erste Martingalstufe ist Rang eins

Für `a=0` ist

\[
\Omega_{p,0,T}
=
\left\{
|u|\le T-\frac12\log p
\right\}
\]

und

\[
\boxed{
\Phi_{p,0,T}[f](u)
=
\sum_{k\ge1}
p^{-3k/4}
K_{k\log p}f(u).
}
\tag{C1zB2C6s.51}
\]

Die zugehörige Energie ist

\[
\boxed{
\mathcal E_{p,0,T}(f)
=
(\log p)(p-1)
\int_{\Omega_{p,0,T}}
\left|
\sum_{k\ge1}
p^{-3k/4}
K_{k\log p}f(u)
\right|^2du.
}
\tag{C1zB2C6s.52}
\]

Für das Residuum:

\[
\boxed{
\begin{aligned}
\mathcal E_{p,0,T}(r_T)
&=
(\log p)(p-1)
\int_{\Omega_{p,0,T}}
\Bigg|
\sum_{k\ge1}p^{-3k/4}
K_{k\log p}h_T(u)\\
&\qquad\qquad
-\lambda_T
\sum_{k\ge1}p^{-3k/4}
K_{k\log p}a_T(u)
\Bigg|^2du.
\end{aligned}
}
\tag{C1zB2C6s.53}
\]

Dieser Kanal ist analytisch wesentlich einfacher als die vollständige Doppelsumme und daher ein natürlicher erster Kandidat für den nächsten expliziten Rechenschritt.

---

# 11. Korrektur der heuristischen Größenordnungen aus der Vorüberlegung

Die Vorüberlegung schlug heuristisch Größenordnungen der Form

\[
\|X_T\|^2\asymp T^2e^T,
\qquad
\|Y_T\|^2\asymp T^2e^T
\]

vor und motivierte daraus eine mögliche Hauptcancellation.

Diese Größenordnungen dürfen in C6s **nicht als bewiesen verwendet werden**.

Insbesondere würde eine solche Aussage eine hinreichend präzise Kontrolle von

\[
\lambda_T
=
\frac{\mu_{T,1}}{\mu_{T,0}}
\]

und der globalen Restnorm

\[
\|R_T\mathbf1_T\|^2
\]

verlangen.

Die bisherige C6-Kette enthält zwar lokale Rest-Crowding- und Separatorabschätzungen, aber keinen bereits freigegebenen Satz, der die oben eingesetzten globalen `asymp`-Skalen rechtfertigt.

Daher lautet die verbindliche Firewall:

\[
\boxed{
\text{heuristisch gleiche Größenordnung von }X_T,Y_T
\not\Rightarrow
\text{bewiesene Rest-Cancellation}.
}
\tag{C1zB2C6s.54}
\]

Noch fundamentaler zeigt (C1zB2C6s.38), dass selbst **exakt gleiche Normen**

\[
\|U_T\|=\lambda_T\|V_T\|
\]

nicht genügen. Ohne Winkel-Locking kann die Differenz groß bleiben.

Status:

\[
\boxed{
\checkmark[M]_{\rm corr,heuristic\text{-}size\text{-}scales\text{-}unproved}.
}
\]

---

# 12. Warum separate obere Schranken strukturell falsch priorisiert wären

Aus

\[
R_Tr_T=X_T-Y_T-Z_T
\]

folgt natürlich

\[
\|R_Tr_T\|
\le
\|X_T\|+\|Y_T\|+\|Z_T\|.
\]

Diese Abschätzung ist korrekt, aber für das Residualproblem potentiell maximal verschwenderisch.

Ebenso kann man jede der sechs Größen aus (C1zB2C6s.11) durch Cauchy-Schwarz kontrollieren. Auch das ist korrekt, aber es verliert genau die Information, ob

\[
U_T
\approx
\lambda_TV_T.
\]

C6s ersetzt deshalb die Strategie

\[
\boxed{
\text{sechs Terme separat majorisieren}
}
\]

durch

\[
\boxed{
\text{gemeinsame positive Quadrate exakt analysieren}.
}
\tag{C1zB2C6s.55}
\]

Status:

\[
\boxed{
\checkmark[M]_{\rm neg,separate\text{-}component\text{-}bounds\text{-}route}.
}
\]

---

# 13. Exakte Form des Restquotienten nach C6s

Kombiniert man (C1zB2C6s.26) mit der Definition von `q_{r,T}`, erhält man

\[
\boxed{
q_{r,T}
=
\frac{
\displaystyle
\sum_p
(\log p)(p-1)
\sum_{a\ge0}
p^a
\int_{\Omega_{p,a,T}}
\left|
\Phi_{p,a,T}[h_T]
-\lambda_T\Phi_{p,a,T}[a_T]
\right|^2du
}{
\|h_T-\lambda_Ta_T\|^2
}.
}
\tag{C1zB2C6s.56}
\]

Äquivalent, in globaler Rest-Regressionssprache,

\[
\boxed{
q_{r,T}
=
\frac{
\|R_Th_T\|^2(1-(\chi_T^{\rm rest})^2)
+
\|R_Ta_T\|^2
(\lambda_T-\lambda_T^{\rm rest})^2
}{
\|h_T-\lambda_Ta_T\|^2
}.
}
\tag{C1zB2C6s.57}
\]

Damit ist die offene Asymptotik vollständig auf zwei Rest-spezifische Mechanismen reduziert:

\[
\boxed{
1-(\chi_T^{\rm rest})^2
}
\]

und

\[
\boxed{
\lambda_T-\lambda_T^{\rm rest}.
}
\]

Oder, feiner, auf die Kanalfehler aus (C1zB2C6s.45).

---

# 14. Was C6s nicht beweist

C6s beweist **nicht**

\[
q_{r,T}=o(1).
\]

Es beweist auch nicht

\[
q_{r,T}\ge c>0.
\]

Es beweist nicht

\[
\lambda_T\sim Te^T
\]

oder irgendeine andere neue globale Asymptotik für `lambda_T`.

Es beweist nicht

\[
|\chi_T^{\rm rest}|\to1.
\]

Und es beweist nicht

\[
\lambda_T-\lambda_T^{\rm rest}\to0.
\]

Der Fortschritt ist strukturell und exakt:

1. die sechs Kreuzterme sind auf drei gemeinsame Gramgrößen reduziert;
2. der Gramkern ist als Martingalquadratsumme faktorisiert;
3. jede erlaubte Cancellation ist kanalweise lokalisiert;
4. die Bedingungen für kleine Restladung sind als Winkel- und Koeffizienten-Locking exakt identifiziert.

---

# 15. Verhältnis zu C6e–C6j

Die Cross-Prime-Separatorsätze aus C6e–C6j bleiben unverändert gültig.

C6s behauptet nicht, dass Cross-Prime-Struktur verschwunden sei. Sie steckt weiterhin in der konkreten Sourcefunktion

\[
h_T=H_T^*H_T\mathbf1_T
\]

und damit in

\[
\Phi_{p,a,T}[h_T].
\]

Die neue Aussage betrifft nur die **Restenergie nach Anwendung von `R_T`**:

Sobald der Vektor in den Restoperator eingespeist wurde, zerfällt seine Energie in positive äußere Prime-/Martingalkanäle. Die arithmetische Herkunft innerhalb von `h_T` kann die Werte der einzelnen `Phi` stark beeinflussen, aber Energien verschiedener Restkanäle können sich nicht gegenseitig wegheben.

Damit überschreibt C6s keinen früheren Cross-Prime-Satz.

---

# 16. Verhältnis zum Alignment-Kriterium aus C6p

C6p benötigt Kontrolle von

\[
q_{r,T},
\qquad
q_{b,T},
\qquad
\beta_{R,T}.
\]

C6s gibt für den zuerst ausgewählten Kandidaten `q_{r,T}` nun die feinste bisherige exakte Darstellung.

Falls ein späterer Knoten etwa beweist

\[
q_{r,T}\le\varepsilon_T
\to0,
\]

folgt aus C6p

\[
s_{r,T}
\le
\frac{\varepsilon_T}{1+\varepsilon_T}
\to0.
\]

Umgekehrt könnte bereits ein einzelner stabiler Restkanal zeigen, dass dieser Hebel nicht funktioniert.

C6s ist daher ein echter Entscheidungsknoten für die `q_r`-Route.

---

# 17. Nächster atomarer Knoten

Die vollständige Formel (C1zB2C6s.56) ist noch zu groß für eine globale Asymptotik in einem Schritt.

Der nächste zulässige atomare Test ist deshalb:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6t]
\quad
\text{First Martingale Channel / Shallow-Depth Residual Test}.
}
\]

Empfohlene Leitfrage:

> Was macht der einfachste Kanal `a=0` — zunächst für die kleinsten Primzahlen — mit dem Residuum `r_T`?

Konkret ist zu untersuchen

\[
\boxed{
\mathcal E_{p,0,T}(r_T)
=
(\log p)(p-1)
\int_{\Omega_{p,0,T}}
\left|
\Phi_{p,0,T}[h_T]
-\lambda_T\Phi_{p,0,T}[a_T]
\right|^2du.
}
\tag{C1zB2C6s.58}
\]

Drei mögliche Ausgänge sind sauber getrennt:

1. **Nichtverschwindender stabiler Kanal:** liefert eine untere Schranke für `q_{r,T}` und kann die Rest-Smallness-Hoffnung widerlegen.
2. **Starke kanalweise Cancellation:** liefert erstmals konkrete Evidenz für `lambda_T^{rest}`-Locking.
3. **Unentschiedene Skala:** dann muss zunächst `lambda_T` oder die beiden Tailprofile `Phi[h_T]`, `Phi[a_T]` separat asymptotisch bestimmt werden.

Bis dahin bleibt

\[
\boxed{
?[O]_{q_r\text{-}asymptotic}.
}
\]

---

# 18. Endurteil

C6s beantwortet die Frage, **wie** die in C6r geforderte gemeinsame Gramkernel-Cancellation korrekt analysiert werden muss.

Die Antwort ist nicht die rohe Sechs-Term-Expansion, sondern die exakte positive Faktorisierung

\[
\boxed{
\|R_Tr_T\|^2
=
\sum_{p,a}
(\log p)(p-1)p^a
\int_{
\Omega_{p,a,T}}
|\Phi_{p,a,T}[h_T]-\lambda_T\Phi_{p,a,T}[A_T\mathbf1_T]|^2du.
}
\]

Damit ist erstmals bewiesen:

\[
\boxed{
\text{Residual-Cancellation ist vollständig kanalweise.}
}
\]

Es gibt keine globale Cross-Prime-/Cross-Depth-Kompensation der Restenergie.

Die quantitative Frage `q_{r,T}=o(1)?` ist damit nicht gelöst, aber deutlich schärfer geworden. Sie ist jetzt eine konkrete Frage nach simultanem kanalweisem Rest-Winkel- und Koeffizienten-Locking.

**P11 bleibt `PASS-A ACTIVE`.**  
**Kein SYN. Kein Seal. Kein `papers/P11`.**
