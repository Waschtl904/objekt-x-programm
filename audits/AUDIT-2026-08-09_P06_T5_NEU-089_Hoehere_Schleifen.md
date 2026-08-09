# P06 G-T5 — Targeted-Reaudit NEU-089

**Datum:** 9. August 2026  
**SYN-Ziel:** P06 — Jacobi–Feshbach + Divisorgraph  
**Quellknoten:** `02-jacobi-limes/NEU-089_Hoehere_Schleifen_Asymptotische_Quadratisierung.md`  
**Vergleichsknoten:** NEU-088, NEU-090; P06 G-T4 (`AUDIT-2026-08-09_P06_T4_NEU-090_Zweite_Schleifenspur.md`)  
**Prüfart:** `TARGETED-REAUDIT` — während G-T4 neu entdeckter konkreter Typ-/Normkonflikt  
**Status:** **G-T5 COMPLETE — NEU-089 `SUPERSEDED_part / korrigierte HS-Kontrolle`**

---

## 0. Neu entdeckter Konflikt

NEU-089 definiert

$$
C_N(z):=R_N(z)^{1/2}B_N^\Lambda R_N(z)^{1/2},
\qquad R_N(z)=(H_N-z)^{-1},
$$

und behauptet für komplexes $z$ sinngemäß:

1. $C_N(z)$ sei selbstadjungiert/symmetrisch;
2. deshalb
   $$\|C_N(z)\|_{HS}^2=\operatorname{Tr}(C_N(z)^2).$$

Für $z\notin\mathbb R$ ist $R_N(z)^{1/2}$ im Allgemeinen nicht selbstadjungiert. Auch bei selbstadjungiertem $B_N^\Lambda$ folgt daher nicht

$$
C_N(z)^*=C_N(z).
$$

Damit ist die Gleichsetzung

$$
\|C_N(z)\|_{HS}^2=\operatorname{Tr}(C_N(z)^2)
$$

für komplexes $z$ im Allgemeinen falsch; korrekt ist

$$
\boxed{\|C_N(z)\|_{HS}^2=\operatorname{Tr}(C_N(z)^*C_N(z)).}
$$

**Status:** historische Selbstadjungiertheits-/HS-Gleichsetzung `×[M]` im komplexen Resolventenregime.

---

## 1. Was trotzdem gültig bleibt: zyklische Trace-Identität

Im endlichen Modell und für einen konsistent gewählten diagonalen Quadratwurzelzweig gilt algebraisch

$$
(BR)^k
\quad\text{und}\quad
C^k=(R^{1/2}BR^{1/2})^k
$$

unter der Spur zyklisch äquivalent. Insbesondere

$$
\operatorname{Tr}((B_NR_N(z))^k)
=
\operatorname{Tr}(C_N(z)^k).
$$

Dafür ist Selbstadjungiertheit von $C_N(z)$ nicht erforderlich.

**Status:** `✓[M]` im endlichen Matrixmodell.

---

## 2. Korrigierte Hilbert–Schmidt-Abschätzung

Mit $h_r=r$ und den NEU-088-Matrixelementen gilt betragsmäßig für festes zulässiges $z$ und große Indizes

$$
|(C_N(z))_{r,r+n}|^2
\ll_z
\frac{\gamma^2}{N^2}\Lambda(n)^2\frac{r}{r+n}.
$$

Daher

$$
\|C_N(z)\|_{HS}^2
\ll_z
\frac1{N^2}
\sum_{r\le M_N}r
\sum_{n\le N-r}\frac{\Lambda(n)^2}{r+n}
+o(1).
$$

Dies ist dieselbe **betragspositive** Doppelsumme, die im G-T4-Reaudit von NEU-090 kontrolliert wurde.

Auf der pathwise Skala

$$
M_N=\frac{N}{\log N}
$$

ergibt die dort bewiesene Splitabschätzung

$$
\boxed{
\|C_N(z)\|_{HS}^2
=O_z\!\left(\frac{\log\log N}{\log N}\right)
\longrightarrow0.
}
$$

Damit folgt sogar

$$
\boxed{\|C_N(z)\|\le\|C_N(z)\|_{HS}\longrightarrow0.}
$$

Die historische NEU-089-Buchung „HS-Norm nur $O(1)$, Operatornorm separat via Schur $O(1/\sqrt{\log N})$“ ist somit nicht der schärfste Endstand.

**Status:** korrigierte HS- und Operatornormkontrolle `✓[M]` im NEU-88–90-Modellscope ($h_r=r$, festes zulässiges $z$, $M_N=N/\log N$).

---

## 3. Höhere Schleifen — Beweis ohne Selbstadjungiertheit

Für jeden festen $k\ge3$ gilt für beliebige endliche Matrizen mit $C_N\in\mathcal S_2$:

$$
|\operatorname{Tr}(C_N^k)|
\le
\|C_N^{k-2}\|\,\|C_N^2\|_1
\le
\|C_N\|^{k-2}\,\|C_N\|_{HS}^2.
$$

Da bereits $\|C_N\|_{HS}\to0$, folgt

$$
\boxed{\operatorname{Tr}(C_N(z)^k)\to0\qquad(k\ge2\text{ fest}).}
$$

Insbesondere verschwindet auch der zweite Schleifenterm, nicht nur die höheren.

**Status:** `✓[M]` im Modellscope; der historische Beweisweg über „$C_N$ selbstadjungiert“ wird ersetzt.

---

## 4. Asymptotische Quadratisierung wird zum vollständigen Schleifenkollaps

NEU-089 formuliert historisch

$$
\log D_N(z)
=-\frac12\operatorname{Tr}(C_N(z)^2)+o(1),
$$

mit potentiell nichttrivialem quadratischem Hauptterm.

Nach G-T4/G-T5 gilt dagegen

$$
\operatorname{Tr}(C_N(z)^2)\to0.
$$

Wenn die Logdet-Reihenentwicklung im dort verwendeten endlichen Modell für große $N$ angesetzt wird, ist wegen $\|C_N(z)\|\to0$ die Reihe sogar besonders stabil, und alle nichtlinearen Schleifenterme verschwinden.

Da der lineare Term wegen der off-diagonalen Struktur null ist,

$$
\operatorname{Tr}(B_NR_N(z))=0,
$$

folgt

$$
\boxed{\log D_N(z)\to0,\qquad D_N(z)\to1.}
$$

**Status:** `✓[M]` innerhalb des endlichen NEU-88–90-Modells mit $h_r=r$ und $M_N=N/\log N$; keine Aussage über andere renormierte Feshbach-/Fredholmarchitekturen.

---

## 5. Kein direkter $\xi$-Anschluss aus dieser Schleifenskala

Der korrigierte Endstand ist stärker und zugleich enger als die historische „Quadratisierung“:

$$
\boxed{\text{Auf dieser Skala kollabiert die gesamte relative Schleifen-Logdeterminante auf }0.}
$$

Daher

$$
D_N(z)\to1,
$$

eine $z$-unabhängige nullstellenfreie Konstante. Diese konkrete NEU-88–90-Konstruktion kann damit keinen nichttrivialen $C\xi(z)$-Grenzwert liefern.

Dies ist **kein** No-Go gegen:

- einen anders skalierten/renormierten relativen Determinantenansatz;
- den globalen Feshbach-Transfer $V^*(D_{rel}-z)^{-1}V$ nach intrinsischer Quellkonstruktion;
- eine $\det_2$-/Weil-Schicht in anderer Hilbertisierung.

---

## 6. Reconciliierte Statusmatrix NEU-089

| Aussage | Historischer Status | P06-Endstatus |
|---|---|---|
| $C_N(z)$ selbstadjungiert für komplexes $z$ | ✓[M] | `×[M]` |
| $\|C_N\|_{HS}^2=\operatorname{Tr}(C_N^2)$ für komplexes $z$ | ✓[M] | `×[M]` |
| zyklische Identität $\operatorname{Tr}((BR)^k)=\operatorname{Tr}(C^k)$ | ✓[M] | `✓[M]` |
| $\|C_N\|_{HS}^2=O(1)$ auf $N/\log N$ | ✓[M] | wahr, aber superseded durch `o(1)` |
| $\|C_N\|_{HS}^2\to0$ | nicht erkannt | `✓[M]` |
| $\|C_N\|\to0$ | ⚠[M] via Schur | `✓[M]` via $\|C\|\le\|C\|_{HS}$ |
| höhere Schleifen $k\ge3$ verschwinden | ✓/⚠[M] | `✓[M]` im Modellscope |
| zweiter Schleifenterm bleibt $O(1)$ nichttrivial | Zielbild | `×[M]`; tatsächlich $\to0$ |
| asymptotische Quadratisierung mit nichttrivialem Hauptterm | ✓/⚠[M] | `SUPERSEDED` |
| $D_N(z)\to1$ | nicht erkannt | `✓[M]` im Modellscope |

---

## 7. Endurteil G-T5

$$
\boxed{\text{NEU-089: TARGETED-REAUDIT COMPLETE.}}
$$

**Endstatus für P06:** `SUPERSEDED_part / korrigierte HS-Kontrolle ✓[M]`.

Der während G-T4 entdeckte Zusatzkonflikt ist damit geschlossen. Die P06-Eröffnung umfasst endgültig **fünf** Targeted-Reaudits, nicht vier.
