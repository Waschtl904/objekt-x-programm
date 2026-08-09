# P11-C1r — Kanonische p-adische Martingalbasis der primspezifischen BC-Restsektoren

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1r]`  
**Vorgänger:** P11-C1n, C1q  
**Primärbasis:** BC-Rangeprojektionen `E_{p^k}=1_{p^k\widehat{\mathbb Z}}` und normiertes Haarmaß  

**Urteil:**

\[
\boxed{[P11-C1r]\quad\checkmark[K/M]}
\]

Jeder primspezifische Restsektor `K_p^0` besitzt eine kanonische orthonormale p-adische Martingal-/Differenzbasis, die ausschließlich aus den verschachtelten BC-Rangeprojektionen erzeugt wird. Damit ist die Exponenthierarchie innerhalb eines Primkanals nun intrinsisch und ohne die in C1i supersedierte globale Graphorthogonalitätsannahme typisiert.

Die Martingalzerlegung löst jedoch die Hochprimdivergenz aus C1o nicht: Sie lokalisiert sie lediglich auf konkrete niedrige p-adische Martingalstufen. Ein cross-prime/source-induzierter Regulator bleibt erforderlich.

---

## 1. Verschachtelte BC-Rangeprojektionen

Für eine feste Primzahl `p` gilt

\[
E_{p^0}=E_1,
\qquad
E_{p^{j+1}}\le E_{p^j},
\qquad
j\ge0,
\]

mit

\[
E_{p^j}=1_{p^j\widehat{\mathbb Z}}.
\]

Die Haarmaße lauten

\[
\boxed{
\int E_{p^j}\,dm_{\rm Haar}=p^{-j}.}
\]

---

## 2. Kanonische Mittelnull-Differenzen

Definiere für `j\ge0`

\[
\boxed{
d_{p,j}
:=
E_{p^{j+1}}-\frac1pE_{p^j}.}
\]

Dann

\[
\int d_{p,j}\,dm_{\rm Haar}
=p^{-(j+1)}-p^{-1}p^{-j}=0.
\]

Also

\[
\boxed{d_{p,j}\perp E_1.}
\]

Status: `✓[K/M]`.

---

## 3. Orthogonalität verschiedener Martingalstufen

Seien `0\le j<k`. Wegen der Verschachtelung gilt

\[
E_{p^{j+1}}E_{p^{k+1}}=E_{p^{k+1}},
\]

\[
E_{p^{j+1}}E_{p^k}=E_{p^k},
\]

\[
E_{p^j}E_{p^{k+1}}=E_{p^{k+1}},
\]

und

\[
E_{p^j}E_{p^k}=E_{p^k}.
\]

Daher

\[
\begin{aligned}
\langle d_{p,j},d_{p,k}\rangle
={}&p^{-(k+1)}
-p^{-1}p^{-k}
-p^{-1}p^{-(k+1)}
+p^{-2}p^{-k}\\
={}&0.
\end{aligned}
\]

Somit

\[
\boxed{
d_{p,j}\perp d_{p,k}
\qquad(j\neq k).}
\]

Status: `✓[K/M]`.

---

## 4. Normen und orthonormale Basis

Für jedes `j\ge0`:

\[
\begin{aligned}
\|d_{p,j}\|^2
&=p^{-(j+1)}
-2p^{-1}p^{-(j+1)}
+p^{-2}p^{-j}\\
&=p^{-(j+1)}-p^{-(j+2)}\\
&=\boxed{\frac{p-1}{p^{j+2}}.}
\end{aligned}
\]

Definiere daher

\[
\boxed{
\psi_{p,j}
:=
\sqrt{\frac{p^{j+2}}{p-1}}
\left(E_{p^{j+1}}-\frac1pE_{p^j}\right).}
\]

Dann

\[
\boxed{
\langle\psi_{p,j},\psi_{p,k}\rangle=\delta_{jk}.}
\]

---

## 5. Verbindung zu den C1n-Restvektoren

C1n definiert

\[
\eta_{p,k}
=
\zeta_{p^k}-p^{-k/2}\zeta_1
=
p^{k/2}E_{p^k}-p^{-k/2}E_1.
\]

Aus der Rekursion

\[
E_{p^{j+1}}
=
\frac1pE_{p^j}+d_{p,j}
\]

folgt iterativ

\[
E_{p^k}
=p^{-k}E_1
+
\sum_{j=0}^{k-1}p^{-(k-1-j)}d_{p,j}.
\]

Nach Multiplikation mit `p^{k/2}`:

\[
\eta_{p,k}
=
\sum_{j=0}^{k-1}
p^{j+1-k/2}d_{p,j}.
\]

In der orthonormalen Basis `\psi_{p,j}` ergibt sich die besonders einfache Formel

\[
\boxed{
\eta_{p,k}
=
\sqrt{p-1}
\sum_{j=0}^{k-1}
p^{(j-k)/2}\psi_{p,j}.}
\]

Status: `✓[K/M]`.

---

## 6. Normkontrolle als Konsistenztest

Aus der orthonormalen Entwicklung:

\[
\begin{aligned}
\|\eta_{p,k}\|^2
&=(p-1)
\sum_{j=0}^{k-1}p^{j-k}\\
&=(p-1)p^{-k}
\frac{p^k-1}{p-1}\\
&=\boxed{1-p^{-k}.}
\end{aligned}
\]

Dies stimmt exakt mit C1n überein.

---

## 7. Die Martingalbasis spannt exakt `K_p^0`

Für jedes `k` liegt `\eta_{p,k}` in

\[
\operatorname{span}\{\psi_{p,0},\ldots,\psi_{p,k-1}\}.
\]

Umgekehrt ist die Koeffizientenmatrix zwischen

\[
(\eta_{p,1},\ldots,\eta_{p,k})
\]

und

\[
(\psi_{p,0},\ldots,\psi_{p,k-1})
\]

unterdreieckig mit nichtverschwindender Diagonale. Daher besitzen beide endlichen Familien denselben Spann.

Somit

\[
\boxed{
K_p^0
=
\overline{\operatorname{span}\{\psi_{p,j}:j\ge0\}}.}
\]

Die `\psi_{p,j}` bilden eine kanonische ONB von `K_p^0`.

Status: `✓[K/M]`.

---

## 8. Kreuzprimorthogonalität

Aus der C1n-Sternzerlegung folgt bereits

\[
K_p^0\perp K_q^0
\qquad(p\neq q).
\]

Daher

\[
\boxed{
\langle\psi_{p,j},\psi_{q,k}\rangle=0
\qquad(p\neq q).}
\]

Die Gesamtheit

\[
\{\zeta_1\}\cup\{\psi_{p,j}:p\text{ prim},j\ge0\}
\]

ist somit eine orthonormale Familie im von den Prime-Power-Rangevektoren erzeugten BC-Unterraum.

---

## 9. Exakte Prime-Power-Labelentwicklung

Da

\[
\zeta_{p^k}
=p^{-k/2}\zeta_1+\eta_{p,k},
\]

folgt

\[
\boxed{
\zeta_{p^k}
=
p^{-k/2}\zeta_1
+
\sqrt{p-1}
\sum_{j=0}^{k-1}p^{(j-k)/2}\psi_{p,j}.}
\]

Damit ist der gesamte GCD-Gramkern in einer **expliziten orthonormalen BC-Koordinate** dargestellt.

Die Kreuzprimblöcke entstehen nur aus `\zeta_1`; die Exponenthierarchie innerhalb eines Primkanals liegt in den Martingalstufen `\psi_{p,j}`.

---

## 10. Reconciliation mit C1i

C1i hatte vor dem Targeted-Reaudit eine gleichgewichtete graphische Kettenbasis angenommen. Diese war wegen der zurückgerollten globalen Graphorthogonalität nicht kanonisch.

C1r liefert nun eine echte Ersatzstruktur:

\[
\boxed{
\text{Exponenthierarchie aus verschachtelten BC-Rangeprojektionen statt aus angenommener Graphorthogonalität.}}
\]

Die `\psi_{p,j}` sind nicht die historischen relativen Kantenvektoren. Sie leben im BC-Rangeprojektionsraum und dürfen nicht mit der Wres-Graphbasis identifiziert werden.

---

## 11. Wirkung auf die Prime-Hub-Synthese

Die primspezifische Komponente der C1o-Synthese lautet für festes `p`

\[
\mathcal T_{R,p}^0a
=
\sum_{k:\,p^k\le e^{2R}}
\sqrt{\frac{\log p}{p^{k/2}}}
D_{k\log p}a\otimes\eta_{p,k}.
\]

Mit §5:

\[
\boxed{
\mathcal T_{R,p}^0a
=
\sum_{j\ge0}
A_{p,j}^{(R)}a\otimes\psi_{p,j},}
\]

wobei

\[
\boxed{
A_{p,j}^{(R)}a
=
\sqrt{\log p}\sqrt{p-1}\,p^{j/2}
\sum_{\substack{k>j\\p^k\le e^{2R}}}
p^{-3k/4}D_{k\log p}a.}
\]

Damit

\[
\boxed{
\|\mathcal T_{R,p}^0a\|^2
=
\sum_{j\ge0}\|A_{p,j}^{(R)}a\|_2^2.}
\]

Die Divergenzfrage ist nun auf explizite orthogonale p-adische Martingalstufen reduziert.

---

## 12. Niedrige Martingalstufen zeigen, warum noch kein Regulator gewonnen ist

Der erste Level `j=0` erhält als führenden `k=1`-Beitrag

\[
A_{p,0}^{(R)}a
\supset
\sqrt{\log p}\sqrt{p-1}\,p^{-3/4}D_{\log p}a.
\]

Sein quadratischer Größenfaktor ist asymptotisch

\[
\boxed{\frac{\log p}{\sqrt p}.}
\]

Genau diese Hochprimskala verursachte C1o.

Die Martingalorthogonalisierung beseitigt sie daher nicht; sie zeigt nur exakt, **wo** sie sitzt.

Auch höhere niedrige Stufen können separate Summierbarkeitsprobleme tragen. Eine vollständige Stufenanalyse wird nicht benötigt, um festzustellen:

\[
\boxed{
\text{BC-Martingalisierung ist eine Kanonisierung der Exponentgeometrie, kein Hochprimregulator.}}
\]

---

## 13. Was C1r positiv erreicht

C1r löst drei frühere Unsicherheiten:

1. **Exponenthierarchie:** kanonisch durch p-adische Verschachtelung;
2. **Orthogonalisierung:** exakt innerhalb `K_p^0`, ohne Wres-Annahme;
3. **Koordinaten der Divergenz:** explizite Martingalstufen.

Offen bleibt die Regulierung über die Primzahlrichtung `p`.

---

## 14. Statusmatrix

| Aussage | Status |
|---|---|
| `d_{p,j}=E_{p^{j+1}}-p^{-1}E_{p^j}` hat Haarmittel null | `✓[K/M]` |
| `d_{p,j}` orthogonal für verschiedene `j` | `✓[K/M]` |
| normierte `psi_{p,j}` ONB von `K_p^0` | `✓[K/M]` |
| explizite Expansion von `eta_{p,k}` in `psi_{p,j}` | `✓[K/M]` |
| BC-Martingalbasis ersetzt supersedierte C1i-Graphorthogonalität | `✓[K/M]` als neue BC-Struktur |
| Martingalbasis = historische Wres-Graphbasis | `×[M]` als Identifikation |
| Martingalisierung kontrolliert automatisch Hochprimdivergenz | `×[M]` |
| first-level Hochprimskala `~log p/sqrt p` bleibt sichtbar | `✓[M]` |
| source-induzierter cross-prime Regulator | `?[O]` |

---

## 15. Wichtigster Befund

Der primspezifische BC-Restsektor besitzt jetzt eine vollständig kanonische interne Geometrie:

\[
\boxed{
K_p^0
\cong
\ell^2(\mathbb N_0)
\quad\text{via}\quad
\psi_{p,j}.}
\]

Damit ist die offene Regulatorfrage endgültig von der Exponentrichtung getrennt:

\[
\boxed{
\text{Exponentrichtung }k\text{: kanonisch aufgelöst}
\qquad
\text{Primrichtung }p\text{: regulatorisch offen}.}
\]

---

## 16. Nächster Knoten

\[
\boxed{[P11\text{-}C1s]\quad\text{Cross-prime Regulator: kann die BC/KMS- oder adelische Struktur die Martingalebenen }\psi_{p,j}\text{ mit einem kanonischen p-Gewicht versehen?}}
\]

Zu prüfen ist insbesondere, ob der KMS-/Rangeprojektionsrahmen bereits eine positive Energieform auf den Martingalstufen liefert, deren `p`-Abfall stärker ist als die C1o-Skala, ohne das Weil-Halbgewicht rückwärts einzubauen.
