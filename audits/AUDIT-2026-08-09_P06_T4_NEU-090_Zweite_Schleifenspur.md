# P06 G-T4 — Targeted-Reaudit NEU-090

**Datum:** 9. August 2026  
**SYN-Ziel:** P06 — Jacobi–Feshbach + Divisorgraph  
**Quellknoten:** `02-jacobi-limes/NEU-090_Zweite_Schleifenspur_z_Rigiditaet.md`  
**Vergleichsknoten:** NEU-084, NEU-088, NEU-089  
**Auditanker:** `ZWISCHENBILANZ_2026-07-29.md`  
**Prüfart:** `TARGETED-REAUDIT`  
**Status:** **G-T4 COMPLETE — NEU-090 HAUPTGRENZWERT `×[M]`; korrigiert auf $T_N(z)\to0$**

---

## 0. Prüfauftrag

Geprüft wurde ausschließlich:

1. der behauptete Grenzwert
   $$T_N(z)\to\gamma^2/2;$$
2. die dafür verwendete angeblich gleichmäßige Abschätzung der inneren Mangoldt-Quadratsumme;
3. die Rolle der Skala $M_N=N/\log N$ gegenüber der strengeren Operatorskala aus NEU-084;
4. die Folgen für $z$-Rigidität und die relative Determinante.

---

## 1. Ausgangsformel

NEU-090 setzt $h_r=r$ und

$$
T_N(z)
=
\frac{2\gamma^2}{N^2}
\sum_{r\le M_N}r^2
\sum_{n\le N-r}
\frac{\Lambda(n)^2}{(r-z)(r+n-z)}.
$$

Für festes $z$ und große $r$ ist

$$
\frac{r^2}{(r-z)(r+n-z)}
\asymp_z
\frac{r}{r+n}.
$$

Der zu prüfende Hauptterm ist daher

$$
\frac1{N^2}
\sum_{r\le M_N}r
\sum_{n\le N-r}\frac{\Lambda(n)^2}{r+n}.
$$

---

## 2. Der Fehler in NEU-090.1

NEU-090 behauptet gleichmäßig für

$$
r\le \frac{N}{\log N}
$$

die Asymptotik

$$
\sum_{n\le N-r}\frac{\Lambda(n)^2}{r+n}
\sim \frac12(\log N)^2.
$$

Diese Gleichmäßigkeit ist falsch.

Für $r$ nahe $N/\log N$ schneidet der Nenner $r+n$ gerade den Bereich ab, der bei $r$ klein die volle $\frac12\log^2N$-Masse erzeugt. Heuristisch bzw. per partieller Summation ist dort nur die Größenordnung

$$
O(\log N\,\log\log N)
$$

relevant. Da die äußere Summe mit dem Faktor $r$ gerade große $r$ stark gewichtet, darf man die $r=O(1)$-Asymptotik nicht gleichmäßig bis $N/\log N$ einsetzen.

Damit bricht genau der Schritt zusammen, der in NEU-090 die beiden Faktoren $(\log N)^2$ wegkürzt.

**Status:** behauptete uniforme Asymptotik `×[M]`.

---

## 3. Rigide obere Abschätzung auf der pathwise Skala

Es genügt die unbedingte Standardabschätzung

$$
A(x):=\sum_{n\le x}\Lambda(n)^2=O(x\log x).
$$

Für festes $z$ können endlich viele kleine $r$ separat behandelt werden. Für alle hinreichend großen $r$ gilt mit einer von $z$ abhängigen Konstante

$$
\left|\frac{r^2}{(r-z)(r+n-z)}\right|
\le C_z\frac{r}{r+n}.
$$

Setze

$$
M:=\frac{N}{\log N},
\qquad L:=\log N.
$$

Vertausche die Summen und benutze

$$
\sum_{r\le M}\frac{r}{r+n}
\le
\begin{cases}
M,& n\le M,\\[1mm]
\dfrac{M^2}{2n},& n>M.
\end{cases}
$$

Dann

$$
|T_N(z)|
\ll_z
\frac1{N^2}
\left(
M\sum_{n\le M}\Lambda(n)^2
+
M^2\sum_{M<n\le N}\frac{\Lambda(n)^2}{n}
\right)
+o(1).
$$

Der erste Term erfüllt

$$
\frac{M}{N^2}A(M)
=O\!\left(\frac{M^2\log M}{N^2}\right)
=O\!\left(\frac1{\log N}\right).
$$

Partielle Summation mit $A(x)=O(x\log x)$ liefert

$$
\sum_{M<n\le N}\frac{\Lambda(n)^2}{n}
=O\!\bigl(\log^2N-\log^2M+\log N\bigr)
=O(\log N\,\log\log N).
$$

Somit

$$
\frac{M^2}{N^2}
\sum_{M<n\le N}\frac{\Lambda(n)^2}{n}
=
O\!\left(\frac{\log\log N}{\log N}\right).
$$

Daher für jedes feste zulässige $z$:

$$
\boxed{
T_N(z)
=O_z\!\left(\frac{\log\log N}{\log N}\right)
\longrightarrow0.
}
$$

Damit ist der alte Grenzwert $\gamma^2/2$ widerlegt.

**Status:** `✓[M]` für den Nullgrenzwert unter der in NEU-090 gesetzten Diagonalskala $h_r=r$ und $M_N=N/\log N$.

---

## 4. Die strengere Operatorskala verstärkt den Nullbefund

NEU-084 unterscheidet korrekt:

$$
M_N^{\rm path}\lesssim\frac{N}{\log N}
$$

für einzelne Jacobi-Gewichte und

$$
M_N^{\rm op}\lesssim\sqrt{\frac{N}{\log N}}
$$

für uniforme $\ell^2$-Zeilennormkontrolle.

NEU-088 hatte bereits die grobe Schranke

$$
T_N(z)
=O\!\left(\frac{M_N^2(\log N)^2}{N^2}\right).
$$

Auf der strengeren Operatorskala folgt unmittelbar

$$
T_N(z)=O\!\left(\frac{\log N}{N}\right)\to0.
$$

Der gezielte Reaudit zeigt aber stärker: **Auch auf der größeren pathwise Skala $N/\log N$ ist der tatsächliche Grenzwert null.**

---

## 5. Korrigierte $z$-Rigidität

Die historische Aussage „der Grenzwert ist $z$-unabhängig“ trifft nur noch in der trivialen Form zu:

$$
\boxed{T_N(z)\to0\quad\text{für jedes feste zulässige }z.}
$$

Damit überlebt keine nichttriviale $z$-abhängige oder $z$-unabhängige Schleifenmasse der zweiten Ordnung.

**Status:** nichttriviale $z$-Rigidität `SUPERSEDED`; Nullgrenzwert `✓[M]` im Modellscope.

---

## 6. Folge für die relative Determinante

NEU-089 verwendet, unter seiner höheren-Schleifen-Kontrolle,

$$
\log D_N(z)=-\frac12T_N(z)+o(1).
$$

Setzt man den korrigierten Grenzwert ein, folgt **unter genau diesen NEU-089-Voraussetzungen**

$$
\log D_N(z)\to0,
\qquad
\boxed{D_N(z)\to1.}
$$

Nicht korrekt ist daher die historische Folgerung

$$
D_N(z)\to e^{-\gamma^2/4}.
$$

**Status:**

- $e^{-\gamma^2/4}$: `×[M]`;
- $D_N(z)\to1$: `CONDITIONAL` auf die in NEU-089 verwendete höhere-Schleifen-/Logdet-Kontrolle;
- ohne diese Zusatzkontrolle ist jedenfalls der behauptete zweite-Schleifen-Hauptterm $\gamma^2/2$ widerlegt.

---

## 7. Konsequenz für den direkten $\xi$-Anschluss

Die alte Begründung „konstante Determinante $e^{-\gamma^2/4}$ kann nicht $C\xi$ sein“ muss numerisch korrigiert werden. Die strukturelle Diagnose bleibt jedoch bestehen:

- unter NEU-089s Kontrollannahmen tendiert die Determinante sogar zur trivialen Konstante $1$;
- ohne diese Annahmen ist ein $\xi$-Grenzwert jedenfalls **nicht hergeleitet**;
- die relative Schleifenkonstruktion liefert in diesem Scaling keine nichttriviale Nullstellenfunktion.

Daher:

$$
\boxed{\text{Direkter }\xi\text{-Determinantenanschluss in diesem NEU-88–90-Modell: nicht erreicht.}}
$$

Dies ist kein No-Go gegen andere Feshbach-/Fredholmrealisierungen von Objekt X.

---

## 8. Reconciliierte Statusmatrix NEU-090

| Aussage | Historischer Status | P06-Endstatus |
|---|---|---|
| uniforme innere Asymptotik $\frac12\log^2N$ bis $r=N/\log N$ | ⚠[M] | `×[M]` |
| $T_N(z)\to\gamma^2/2$ | ⚠[M] | `×[M]` |
| $T_N(z)\to0$ bei $M_N=N/\log N$, $h_r=r$ | nicht erkannt | `✓[M]` |
| $T_N(z)\to0$ auf $M_N\lesssim\sqrt{N/\log N}$ | implizit aus NEU-088 | `✓[M]` |
| nichttriviale $z$-Rigidität | ⚠[M] | `SUPERSEDED` |
| $D_N(z)\to e^{-\gamma^2/4}$ | ✓/⚠[M] | `×[M]` |
| $D_N(z)\to1$ | nicht erkannt | `CONDITIONAL` auf NEU-089-Higher-Loop-Kontrolle |
| direkter $\xi$-Anschluss | No-Go im Modell | `NICHT ERREICHT`; unter Higher-Loop-Kontrolle trivialer Konstantenlimes |

---

## 9. Endurteil G-T4

$$
\boxed{\text{NEU-090: TARGETED-REAUDIT COMPLETE.}}
$$

$$
\boxed{T_N(z)\to0\ \text{statt}\ \gamma^2/2.}
$$

**Endstatus für P06:** `PATCH-RECONCILED / Hauptgrenzwert ×[M] / korrigierter Nullgrenzwert ✓[M]`.

Dieser Befund bestätigt die bereits in der Juli-Zwischenbilanz dokumentierte Korrektur und schließt den letzten offenen Targeted-Reaudit der P06-Eröffnung.
