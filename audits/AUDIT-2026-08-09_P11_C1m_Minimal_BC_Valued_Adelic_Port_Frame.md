# P11-C1m — Minimaler BC-wertiger adelischer Momentport und GCD-Frame-Rekonstruktion

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1m]`  
**Vorgänger:** P11-C1k2, P11-C1l + Targeted-Reaudit `E_1` vs. total Haar  
**Status:**

\[
\boxed{[P11-C1m]\quad\checkmark[K/M]_{\rm part}}
\]

Für jeden source-induced endlichen Prime-Power-Cutoff existiert ein kanonischer endlicher BC-Momentport. Seine Redundanz wird exakt durch die strikt positive GCD-Grammatrix kontrolliert; der finite-adische Anteil im zugehörigen Rangeprojektionsraum kann aus den Momenten vollständig rekonstruiert werden.

Der Port ist ein echter positiver finite-adischer Quellenbaustein. Noch offen ist die gemeinsame Testfunktions-/Trägerklasse, auf der diese BC-Momentkanäle gleichzeitig mit dem P02-Paley–Wiener-Port und der archimedischen Inzidenzgeometrie kompatibel sind.

---

## 1. Source-induced Prime-Power-Labelmenge

Aus C1f:

\[
\boxed{
\mathcal N_R
:=
\{n=p^k:\ p^k\le e^{2R}\}.
}
\]

Diese Menge ist endlich und für `R<S` gilt

\[
\mathcal N_R\subset\mathcal N_S.
\]

Für jedes `n` definiert C1k2 den normierten BC-Rangevektor

\[
\boxed{
\zeta_n:=\sqrt n\,E_n
=\sqrt n\,1_{n\widehat{\mathbb Z}}
\in L^2(\widehat{\mathbb Z}).
}
\]

---

## 2. Endlicher BC-Labelraum

Setze

\[
\boxed{
K_R
:=
\operatorname{span}\{\zeta_n:n\in\mathcal N_R\}
\subset L^2(\widehat{\mathbb Z}).
}
\]

C1k/C1k2 beweisen, dass die Gram-Matrix

\[
\boxed{
C_R=(c_{nm})_{n,m\in\mathcal N_R},
\qquad
c_{nm}=\frac{\gcd(n,m)}{\sqrt{nm}}
}
\]

streng positiv definit ist.

Daher sind die `\zeta_n`, `n\in\mathcal N_R`, linear unabhängig und

\[
\dim K_R=|\mathcal N_R|.
\]

Status: `✓[K/M]`.

---

## 3. Synthese- und Analyseoperator

Definiere

\[
S_R:\mathbb C^{\mathcal N_R}\to K_R,
\qquad
S_Rc:=\sum_{n\in\mathcal N_R}c_n\zeta_n.
\]

Dann ist der adjungierte Analyseoperator

\[
S_R^*:L^2(\widehat{\mathbb Z})\to\mathbb C^{\mathcal N_R},
\qquad
(S_R^*f)_n=\langle f,\zeta_n\rangle.
\]

Der Gramoperator ist exakt

\[
\boxed{S_R^*S_R=C_R.}
\]

Da `C_R>0`, ist `S_R` injektiv und `C_R^{-1}` wohldefiniert.

---

## 4. Exakte Rekonstruktion des `K_R`-Anteils

Der orthogonale Projektor auf `K_R` lautet

\[
\boxed{
P_{K_R}
=S_R C_R^{-1}S_R^*.
}
\]

Beweis: Für `f\in L^2(\widehat{\mathbb Z})` setze

\[
g:=S_R C_R^{-1}S_R^*f\in K_R.
\]

Für jedes `m\in\mathcal N_R`:

\[
\begin{aligned}
\langle f-g,\zeta_m\rangle
&=(S_R^*f)_m
-\bigl(C_R C_R^{-1}S_R^*f\bigr)_m\\
&=0.
\end{aligned}
\]

Also `f-g\perp K_R`, somit `g=P_{K_R}f`.

Status: `✓[K/M]`.

---

## 5. Positive Norm direkt in Momentkoordinaten

Setze

\[
m_R(f):=S_R^*f
=\bigl(\langle f,\zeta_n\rangle\bigr)_{n\in\mathcal N_R}.
\]

Dann

\[
\begin{aligned}
\|P_{K_R}f\|_2^2
&=
\langle S_RC_R^{-1}m_R(f),
S_RC_R^{-1}m_R(f)\rangle\\
&=
m_R(f)^*C_R^{-1}m_R(f).
\end{aligned}
\]

Somit

\[
\boxed{
\|P_{K_R}f\|_2^2
=
m_R(f)^*C_R^{-1}m_R(f)\ge0.
}
\]

Das ist eine **kanonische positive Quellenform in nichtorthogonalen BC-Momentkoordinaten**.

Kein Koeffizient wird frei gewählt; `C_R^{-1}` wird von der BC-Rangegeometrie erzwungen.

---

## 6. Anwendung auf adelische Amplituden

Für

\[
F\in\mathcal S(\mathbb A_\mathbb Q)
\]

definiere punktweise in der reellen Variablen

\[
\boxed{
M_{n}F(x)
:=
\int_{\mathbb A_f}
F(x,y)\,\overline{\zeta_n(y)}\,dy.
}
\]

Da `\zeta_n` kompakt getragen und lokal konstant ist, ist `M_nF` eine wohldefinierte Schwartz-Funktion der reellen Variablen `x`.

Der endliche BC-Momentvektor lautet

\[
\boxed{
\mathbf M_R F(x)
:=
(M_nF(x))_{n\in\mathcal N_R}.
}
\]

Für jedes feste `x` rekonstruiert

\[
S_RC_R^{-1}\mathbf M_RF(x)
\]

exakt den `K_R`-Anteil der finite-adischen Scheibe `F(x,\cdot)` innerhalb `L^2(\widehat{\mathbb Z})`.

---

## 7. Korrigierter minimaler verfeinerter Port

C1l-Targeted-Reaudit zeigt:

\[
M_1\neq P_{Haar}
\]

im Allgemeinen auf `\mathbb A_f`.

Daher muss der minimale P11-Port beide Informationstypen getrennt führen:

\[
\boxed{
\mathcal R_R F
:=
\left(
P_{Haar}F,
\mathbf M_RF
\right).
}
\]

Die erste Komponente ist exakt die bestehende P02-Quelle für `R_{PW}`; die zweite Komponente speichert die Prime-Power-Rangegeometrie.

Dies ist noch kein globaler Hilbertport, sondern ein **typisierter endlicher Analyseport**.

---

## 8. P02-Standardsektion als Kalibrierung

Für den P02-Lift

\[
F_a^{(0)}(x,y)=h_a(x)E_1(y)
\]

gilt

\[
M_nF_a^{(0)}(x)
=
\sqrt n\,h_a(x)
\int_{\widehat{\mathbb Z}}E_n(y)\,dy
=
\frac{h_a(x)}{\sqrt n}.
\]

Also

\[
\boxed{
\mathbf M_RF_a^{(0)}(x)
=h_a(x)
\bigl(n^{-1/2}\bigr)_{n\in\mathcal N_R}.
}
\]

Dies ist genau der Gram-Koeffizientenvektor von `E_1` gegen die `\zeta_n`:

\[
\langle E_1,\zeta_n\rangle=n^{-1/2}.
\]

Damit stimmt die P02-Standardsektion exakt mit der neutralen Zeile des GCD-Kerns überein.

Status: `✓[M]` relativ zur Standardsektion.

---

## 9. Verschachtelung

Für `R<S` gilt

\[
K_R\subset K_S
\]

und `C_R` ist die entsprechende Hauptuntermatrix von `C_S`.

Daher bilden die Projektoren

\[
P_{K_R}
\]

eine monotone Familie im Unterraumsinn:

\[
K_R\subset K_S.
\]

Für jedes feste `f\in L^2(\widehat{\mathbb Z})`:

\[
\|P_{K_R}f\|
\le
\|P_{K_S}f\|
\le
\|f\|.
\]

Damit besitzt die finite-adische Labelanalyse einen kontrollierten positiven Induktivpfad.

---

## 10. Welchen Grenzraum erfassen die `K_R`?

Definiere

\[
K_{\rm div}
:=
\overline{\bigcup_{R>0}K_R}^{\,L^2(\widehat{\mathbb Z})}.
\]

Dieser Raum ist kanonisch definiert.

**Nicht behauptet** wird

\[
K_{\rm div}=L^2(\widehat{\mathbb Z}).
\]

Die Vektoren `E_n=1_{n\widehat{\mathbb Z}}` sehen nur die verschachtelte **Teilbarkeits-/Idealgeometrie**, nicht sämtliche additiven Restklassenfunktionen auf `\widehat{\mathbb Z}`.

Für P11 kann genau diese Beschränkung sogar erwünscht sein: `K_{div}` ist der minimale BC-Unterraum, der die GCD-/Rangegeometrie trägt.

Status der Dichtheit im vollen finite-adischen `L^2`: nicht benötigt / nicht behauptet.

---

## 11. Wichtige Regularitätslücke

Für `F\in\mathcal S_{adel}^{amp}` erzwingt die P02-Definition nur

\[
(P_{Haar}F)|_{(0,\infty)}\in C_c^\infty((0,\infty)).
\]

Sie erzwingt **nicht**, dass für alle `n`

\[
(M_nF)|_{(0,\infty)}
\]

denselben kompakten Träger besitzt.

Die `M_nF` sind als reelle Funktionen Schwartz, aber ihre logarithmischen Bilder müssen nicht im selben `\mathcal A_{PW}`-Fenster wie `R_{PW}F` liegen.

Damit ist die direkte gemeinsame Anwendung der C1c-Translationsinzidenz auf alle Momentkanäle noch nicht typisiert.

\[
\boxed{\text{BC-Momentport konstruiert; gemeinsame Paley–Wiener-Domäne noch OPEN.}}
\]

---

## 12. Zwei mögliche nächste Quellräume

### Variante A — synchronisierte Momenten-Amplituden

Für endliches `R` fordere zusätzlich

\[
\operatorname{supp}(M_nF|_{(0,\infty)})
\subset[e^{-R},e^R]
\quad
\forall n\in\mathcal N_R.
\]

Das wäre source-/cutoff-kompatibel, ist aber eine neue Bedingung und auf Kanonizität/Dichtheit zu prüfen.

### Variante B — Standardsektion plus BC-Unterraum

Beginne mit

\[
F(x,y)=h_a(x)f(y),
\qquad
f\in K_R.
\]

Dann besitzen alle Momente denselben reellen Träger wie `h_a`. Dies ist ein sauberer endlicher Pilot, aber zunächst ein Tensorprodukt-Unterraum, nicht der volle adelische Quellenraum.

---

## 13. Statusmatrix

| Aussage | Status |
|---|---|
| `C_R>0` | `✓[K/M]` |
| `P_{K_R}=S_RC_R^{-1}S_R^*` | `✓[K/M]` |
| Momentnorm `m^*C_R^{-1}m` | `✓[K/M]` |
| endlicher BC-Momentport `M_R` | `✓[K/M]` |
| korrigierter verfeinerter Port `(P_Haar,M_R)` | `✓[M]` als Typ/Konstruktion |
| Standardsektion liefert Momente `h_a/sqrt n` | `✓[M]` |
| `K_R` verschachtelt | `✓[M]` |
| `K_div` kanonisch definiert | `✓[M]` |
| `K_div=L^2(hat Z)` | **nicht behauptet** |
| alle Momentkanäle liegen automatisch in derselben `A_PW`-Klasse | `×[M]` |
| synchronisierte Momenten-Amplitudenquelle | `?[O]` |
| Tensorprodukt-Pilot `h_a(x)f(y)`, `f\in K_R` | `✓[M]` als verfügbarer Testtyp; Kanonizität als Gesamtquelle OPEN |

---

## 14. Wichtigster Befund

P11 besitzt nun einen **konkreten verfeinerten Quellenbaustein**:

\[
\boxed{
F
\longmapsto
\left(
P_{Haar}F,
\mathbf M_RF
\right),
\qquad
\mathbf M_RF=(\langle F,\zeta_n\rangle)_{n\in\mathcal N_R},
}
\]

mit exakter positiver Rekonstruktionsgeometrie

\[
\boxed{
\|P_{K_R}F(x,\cdot)\|^2
=
\mathbf M_RF(x)^*C_R^{-1}\mathbf M_RF(x).
}
\]

Damit ist die BC-Labelinformation nicht mehr nur ein abstrakter Nebenraum; sie kann direkt als endlicher vektorwertiger Port an die adelische Quelle angehängt werden.

---

## 15. Nächster Knoten

\[
\boxed{[P11\text{-}C1n]\quad\text{Tensorprodukt-Pilot auf }\mathcal D_R\otimes K_R:\text{ gemeinsame Gamma-/Prime-Inzidenz und Kompressionsmatrix}.}
\]

Der Pilot soll **keine** neue globale Annahme machen. Er prüft lediglich auf dem expliziten Raum

\[
\mathcal D_R\otimes K_R
\]

ob die bereits konstruierten Operatoren `D_s` und BC-Rangeprojektionen eine finite positive Blockgeometrie liefern, deren Diagonal-/Kompressionsdaten mit C1d/C1e exakt verglichen werden können.
