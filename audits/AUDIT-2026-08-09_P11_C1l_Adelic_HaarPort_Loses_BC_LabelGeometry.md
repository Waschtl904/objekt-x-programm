# P11-C1l — Adelischer Haar-Port verliert die BC-Labelgeometrie

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1l]`  
**Vorgänger:** P11-C1k2  
**Primärquellen:** P02 (`P_Haar`, `R_PW`, expliziter Surjektivitätslift), `KONVENTIONEN.md` (`E_n=1_{n\widehat{\mathbb Z}}`)  

**Urteil:**

\[
\boxed{[P11-C1l]\quad\checkmark[M]_{\rm neg,Port}\;\text{und}\;\checkmark[M]_{\rm part}}
\]

Der aktuelle P02-Haar-Port

\[
R_{PW}:\mathcal S_{adel}^{amp}\twoheadrightarrow\mathcal A_{PW}
\]

behält die endliche BC-Rangeprojektionsgeometrie **nicht** intrinsisch. Zwei adelische Amplituden können dasselbe Portbild `a` besitzen, aber verschiedene `E_n`-Momente und damit verschiedene Prime-Power-Labelinformationen tragen.

Daher kann die in C1k2 konstruierte BC-GCD-Labelgeometrie nicht allein aus dem bereits kollabierten reellen Portbild `a=R_{PW}F` zurückgewonnen werden. Für die Archimedes–Prime-Kopplung muss P11 entweder die adelische Quelle vor der Haarprojektion verfeinert behalten oder eine zusätzliche kanonische Sektion/Quotientenstruktur konstruieren.

Dies ist kein No-Go gegen eine adelische Objekt-X-Kopplung; nur gegen ihre Rekonstruktion **aus `R_PW(F)` allein**.

---

## 1. P02-Haar-Port

Für

\[
F\in\mathcal S(\mathbb A_\mathbb Q)
\]

definiert P02

\[
(P_{Haar}F)(x)
:=
\int_{\mathbb A_{\mathbb Q,f}}F(x,y)\,dy,
\]

mit

\[
\operatorname{vol}(\widehat{\mathbb Z})=1.
\]

Danach

\[
(R_{PW}F)(u)
=e^{u/2}(P_{Haar}F)(e^u).
\]

Der Port sieht also vom endlichen adelischen Anteil nur dessen **totales Haarintegral**.

---

## 2. BC-Rangeprojektionsdaten

Nach den verbindlichen BC-Konventionen

\[
E_n
=1_{n\widehat{\mathbb Z}}.
\]

Mit normiertem Haarmaß gilt

\[
\int_{\mathbb A_f}E_n(y)\,dy
=\frac1n.
\]

C1k2 benutzt die normierten Vektoren

\[
\zeta_n=\sqrt n\,E_n
\]

und erhält

\[
\langle\zeta_n,\zeta_m\rangle
=
\frac{\gcd(n,m)}{\sqrt{nm}}.
\]

Diese Information hängt von **Schnitten der Rangebereiche** ab, nicht nur von ihrem totalen Integral.

---

## 3. Explizite Haar-Nullrichtung mit nichttrivialem `E_n`-Moment

Fixiere `n>1` und setze

\[
\boxed{
\phi_n
:=
E_n-\frac1nE_1.
}
\]

Da `E_1=1_{\widehat{\mathbb Z}}` und `\operatorname{vol}(\widehat{\mathbb Z})=1`, gilt

\[
\int\phi_n(y)\,dy
=
\frac1n-rac1n
=0.
\]

Also ist `\phi_n` für die totale Haarprojektion unsichtbar.

Aber

\[
E_nE_1=E_n,
\qquad
E_n^2=E_n,
\]

somit

\[
\begin{aligned}
\int\phi_n(y)E_n(y)\,dy
&=
\int E_n(y)\,dy
-
\frac1n\int E_n(y)\,dy\\
&=
\frac1n-rac1{n^2}\\
&=
\boxed{\frac{n-1}{n^2}\neq0.}
\end{aligned}
\]

Damit ist die `E_n`-Information nicht durch das totale Haarintegral bestimmt.

Status: `✓[M]`.

---

## 4. Zwei adelische Lifts mit demselben Portbild

Sei

\[
a\in\mathcal A_{PW}
\]

und der in P02 benutzte explizite Lift

\[
F_a^{(0)}(x,y)
=h_a(x)E_1(y),
\qquad
h_a(x)=x^{-1/2}a(\log x)
\]

für `x>0`.

Wähle zusätzlich ein beliebiges

\[
k\in C_c^\infty((0,\infty))
\]

und setze

\[
K_n(x,y):=k(x)\phi_n(y).
\]

Da

\[
P_{Haar}K_n=0,
\]

gilt

\[
\boxed{
R_{PW}(F_a^{(0)}+K_n)
=R_{PW}(F_a^{(0)})
=a.
}
\]

Die beiden adelischen Amplituden besitzen also dasselbe reelle Portbild.

---

## 5. Aber ihre BC-Labelmomente unterscheiden sich

Definiere für festes `n` den endlichen-adischen Momentkanal

\[
M_nF(x)
:=
\int_{\mathbb A_f}F(x,y)E_n(y)\,dy.
\]

Dann

\[
M_nK_n(x)
=
k(x)\frac{n-1}{n^2},
\]

also im Allgemeinen

\[
\boxed{
M_n(F_a^{(0)}+K_n)
\neq
M_n(F_a^{(0)}).
}
\]

Damit faktorisiert `M_n` nicht durch `R_{PW}`.

Äquivalent existiert kein wohldefinierter Operator `\widetilde M_n` auf `\mathcal A_{PW}` mit

\[
M_n=\widetilde M_n\circ R_{PW}
\]

auf dem gesamten adelischen Amplitudenraum.

Status:

\[
\boxed{\checkmark[M]_{neg,Port}.}
\]

---

## 6. Konsequenz für die GCD-Labelgeometrie

Die BC-Gramwerte

\[
\langle\zeta_n,\zeta_m\rangle
\]

sind im finite-adischen Sektor intrinsisch definiert.

Aber das Portbild

\[
a=R_{PW}F
\]

bestimmt **nicht**, wie ein gegebener Lift `F` in den Richtungen `E_n` liegt.

Daher ist die kombinierte C1k2-Vorgeometrie

\[
V_n^{an}a\otimes\zeta_n
\]

eine kanonische Produktkonstruktion aus zwei getrennten verankerten Strukturen, aber noch nicht als **Abstieg eines einzigen adelischen Analyseoperators durch `R_{PW}`** bewiesen.

Diese Typtrennung ist bindend.

---

## 7. Der P02-Standardlift und der neutrale BC-Vektor

P02 beweist die Surjektivität mit

\[
F_a^{(0)}(x,y)=h_a(x)E_1(y).
\]

Damit ist innerhalb **dieser expliziten Sektion** der endliche adelische Ausgangsvektor

\[
\boxed{E_1=1_{\widehat{\mathbb Z}}}
\]

ausgezeichnet.

C1k2 liefert

\[
\langle E_1,\zeta_n\rangle
=
\frac1{\sqrt n}.
\]

Daher entsteht relativ zu dieser Sektion ein sehr natürlicher Archimedes–Prime-Labelkoeffizient

\[
\boxed{c_{\infty,n}^{(0)}=n^{-1/2}.}
\]

**Aber:** P02 beweist nicht, dass `F_a^{(0)}` die einzigartige oder unter allen relevanten adelischen Symmetrien kanonische Sektion ist. C1l zeigt explizit, dass andere Lifts mit demselben Portbild andere finite-adische Momente besitzen.

Status von `c_{\infty,n}^{(0)}`:

\[
\boxed{?[O]\text{ als intrinsischer Objekt-X-Koeffizient; }\checkmark[M]\text{ relativ zur P02-Standardsektion}.}
\]

---

## 8. Drei zulässige Reparaturwege

### Weg A — Verfeinerter adelischer Port

Ersetze die totale Haarprojektion durch eine vektorwertige Analyse, die neben

\[
M_1F=P_{Haar}F
\]

auch genügend BC-Momente

\[
M_nF
\]

behält.

### Weg B — Kanonische Sektion

Konstruiere eine ausgezeichnete lineare Sektion

\[
S_{can}:\mathcal A_{PW}\to\mathcal S_{adel}^{amp},
\qquad
R_{PW}S_{can}=I,
\]

und beweise ihre Kanonizität aus adelischen/BC-Daten.

### Weg C — Quotient mit zusätzlicher Relation

Quotientiere den Kern von `R_{PW}` nicht vollständig, sondern nur nach einem feineren Radikal, das die für die Labelgeometrie relevanten Momente erhält.

Alle drei Wege sind offen.

---

## 9. Warum Weg A besonders natürlich ist

Die Familie der Rangeprojektionen `(E_n)` besitzt bereits eine verschachtelte multiplikative Schnittgeometrie.

Ein vektorwertiger Port der Form

\[
\boxed{
\mathcal R_{BC}F
:=
(M_nF)_{n\in\mathcal P^*\cup\{1\}}
}
\]

würde die finite-adische Labelinformation vor dem Kollaps speichern.

Dafür müssen jedoch geklärt werden:

1. Zielraum / Gewichtung der Folge `(M_nF)`;
2. Redundanzen aus Divisibilität;
3. Beschränktheit / Fréchet-Stetigkeit;
4. source-induced Cutoffs;
5. Rückgewinnung des bisherigen `R_{PW}` als neutrale Komponente;
6. Kompatibilität mit der Gamma-Inzidenzstruktur.

Noch keine dieser Aussagen wird hier als abgeschlossen gebucht.

---

## 10. Statusmatrix

| Aussage | Status |
|---|---|
| `R_PW` sieht nur totales finite-adisches Haarintegral | `✓[K/M]` |
| `phi_n=E_n-n^{-1}E_1` liegt im Haar-Nullraum | `✓[M]` |
| `E_n`-Moment von `phi_n` ist `(n-1)/n^2` | `✓[M]` |
| `M_n` faktorisiert durch `R_PW` | `×[M]` |
| BC-GCD-Labelgeometrie aus `a=R_PW F` allein rekonstruierbar | `×[M]` |
| P02-Standardsektion selektiert `E_1` | `✓[M]` relativ zu dieser Sektion |
| `c_{infty,n}=n^{-1/2}` intrinsisch kanonisch | `?[O]` |
| verfeinerter BC-wertiger adelischer Port | `?[O]` |
| kanonische Sektion | `?[O]` |
| feinerer Quotient/Radikal | `?[O]` |

---

## 11. Wichtigster P11-Befund

C1k2 hat die Prime-Power-Labelgeometrie direkt in der BC-Algebra gefunden.

C1l zeigt jetzt, warum sie im bisherigen P02-Paper noch **nicht automatisch mit dem archimedischen Kanal verheiratet ist**:

\[
\boxed{
\text{Der bisherige Haar-Port kollabiert genau die finite-adische Information, die C1k2 für die Labelkopplung benötigt.}
}
\]

Damit ist die nächste Objekt-X-Frage nicht mehr diffus „woher kommt die Kopplung?“, sondern konkret:

\[
\boxed{
\text{Welcher verfeinerte adelische Analyseport erhält gleichzeitig die reelle Weil-Amplitude und die BC-Rangegeometrie?}
}
\]

---

## 12. Nächster Knoten

\[
\boxed{[P11\text{-}C1m]\quad\text{Minimaler BC-wertiger adelischer Port und Redundanzanalyse der }E_n\text{-Momente}.}
\]

Erster Test: Statt alle Momente `M_n` unabhängig zu speichern, prüfe, ob die normierten Projektionen `\zeta_n=\sqrt n E_n` eine kanonische Hilbertanalyse

\[
F(x,\cdot)\mapsto
\bigl(\langle F(x,\cdot),\zeta_n\rangle\bigr)_n
\]

auf den source-induced endlichen Prime-Power-Mengen `F_R` liefern und ob deren Gramoperator exakt der GCD-Kern `C_R` ist.
