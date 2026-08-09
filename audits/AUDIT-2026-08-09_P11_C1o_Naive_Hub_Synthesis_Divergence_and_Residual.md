# P11-C1o — Naive globale Hub-Synthese divergiert: exakter Rest und notwendige regulatorische Struktur

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1o]`  
**Vorgänger:** P11-C1c–C1n  

**Urteil:**

\[
\boxed{[P11-C1o]\quad\checkmark[M]_{\rm neg}\text{ für die naive unrenormierte Gesamtsynthese}.}
\]

Die kanonische BC-GCD-Labelgeometrie ist positiv und nichtorthogonal, aber die naivste globale Source-Synthese

\[
a\longmapsto
\sum_{p^k\le e^{2R}}
\sqrt{\frac{\log p}{p^{k/2}}}
D_{k\log p}a\otimes\zeta_{p^k}
\]

divergiert entlang des source-induced Cutoffs bereits für jedes feste nichttriviale kompakt getragene `a`. Daher kann sie ohne zusätzliche Regulator-/Quotienten-/Renormierungsstruktur nicht gegen die endliche Weilform konvergieren.

Dies ist kein No-Go gegen den GCD-Labelkern selbst und kein No-Go gegen Objekt X. Es lokalisiert den nächsten Engpass auf die **Synthese**, nicht auf die bereits konstruierte lokale/Label-Gramgeometrie.

---

## 1. Endliche positive Prime-Hub-Synthese

Für

\[
\mathcal N_R
=
\{n=p^k:p^k\le e^{2R}\}
\]

definiere

\[
\boxed{
\mathcal T_R^{pr}a
:=
\sum_{n=p^k\in\mathcal N_R}
\sqrt{w_n}
D_{\log n}a\otimes\zeta_n,
\qquad
w_n:=\frac{\Lambda(n)}{\sqrt n}.
}
\]

Die Summe ist endlich. Daher

\[
\boxed{
\mathfrak G_R^{pr}(a,b)
:=
\langle\mathcal T_R^{pr}a,\mathcal T_R^{pr}b\rangle
}
\]

ist eine wohldefinierte positive Form.

Explizit:

\[
\mathfrak G_R^{pr}(a,b)
=
\sum_{n,m\in\mathcal N_R}
\sqrt{w_nw_m}
\frac{\gcd(n,m)}{\sqrt{nm}}
\langle D_{\log n}a,D_{\log m}b\rangle.
\]

Status: `✓[K/M]` für jedes endliche `R`.

---

## 2. Diagonalteil und Kreuzterm

Schreibe

\[
\mathfrak G_R^{pr}
=\mathcal E_R^{diag}+X_R,
\]

mit

\[
\mathcal E_R^{diag}(a,b)
:=
\sum_{n\in\mathcal N_R}
w_n\langle D_{\log n}a,D_{\log n}b\rangle
\]

und

\[
X_R(a,b)
:=
\sum_{n\neq m}
\sqrt{w_nw_m}
\frac{\gcd(n,m)}{\sqrt{nm}}
\langle D_{\log n}a,D_{\log m}b\rangle.
\]

C1c liefert

\[
B_{fin}^{\mathcal N_R}(a,b)
=
\mathcal E_R^{diag}(a,b)
-2W_R\langle a,b\rangle,
\]

wobei

\[
W_R:=\sum_{n\in\mathcal N_R}w_n.
\]

Daher exakt

\[
\boxed{
\mathfrak G_R^{pr}-B_{fin}^{\mathcal N_R}
=
X_R+2W_R\langle\cdot,\cdot\rangle.
}
\]

Die nichtorthogonale GCD-Geometrie ersetzt also die historische Kompensation **nicht automatisch**.

---

## 3. Voller positiver Pilot inklusive Gamma-/Pol-Pluskanal

Setze

\[
\mathfrak G_R^+(a,b)
:=
\mathcal E_\infty(a,b)
+
\mathfrak G_R^{pr}(a,b)
+
P_+(a)\overline{P_+(b)}.
\]

Dann ist

\[
\mathfrak G_R^+(a,a)\ge0.
\]

C1d liefert für die wörtliche endliche Weiltrunkierung

\[
\begin{aligned}
B_W^{\mathcal N_R}(a,b)
={}&
\mathcal E_\infty(a,b)
+
\mathcal E_R^{diag}(a,b)
+
P_+(a)\overline{P_+(b)}\\
&-
\Bigl[
(2W_R-A_\infty(0))\langle a,b\rangle
+P_-(a)\overline{P_-(b)}
\Bigr].
\end{aligned}
\]

Somit

\[
\boxed{
\mathfrak G_R^+-B_W^{\mathcal N_R}
=
X_R
+(2W_R-A_\infty(0))\langle\cdot,\cdot\rangle
+P_-^*P_-.
}
\]

Dies ist der exakte Rest der naiven positiven Hubform.

---

## 4. Sternzerlegung des Prime-Hub-Raums

C1n liefert

\[
\zeta_{p^k}
=p^{-k/2}\zeta_1+\eta_{p,k},
\]

mit

\[
K_p^0:=\overline{\operatorname{span}\{\eta_{p,k}\}_k},
\qquad
K_p^0\perp K_q^0
\quad(p\neq q),
\]

und

\[
\|\eta_{p,1}\|^2=1-p^{-1}.
\]

Damit zerfällt

\[
\mathcal T_R^{pr}a
=
\mathcal T_{R,hub}^{pr}a
+
\bigoplus_p\mathcal T_{R,p}^{0}a.
\]

Insbesondere

\[
\boxed{
\|\mathcal T_R^{pr}a\|^2
\ge
\sum_p\|\mathcal T_{R,p}^{0}a\|^2.
}
\]

Diese orthogonale primspezifische Projektion liefert einen robusten Divergenztest, unabhängig von möglichen negativen Kreuztermen im neutralen Hub.

---

## 5. Große Primzahlen im source-induced Cutoff tragen nur `k=1`

Für

\[
e^R<p\le e^{2R}
\]

gilt

\[
p\le e^{2R},
\qquad
p^2>e^{2R}.
\]

Daher enthält `\mathcal N_R` in diesem Primkanal **nur** das Label `p=p^1`.

Folglich ist die `K_p^0`-Komponente exakt

\[
\sqrt{\frac{\log p}{\sqrt p}}
D_{\log p}a\otimes\eta_{p,1}.
\]

Ihr Normquadrat ist

\[
\boxed{
\frac{\log p}{\sqrt p}
(1-p^{-1})
\|D_{\log p}a\|_2^2.
}
\]

---

## 6. Für feste kompakte Quelle werden die großen Verschiebungen disjunkt

Fixiere

\[
0\neq a\in C_c^\infty([-R_0,R_0]).
\]

Für

\[
s>2R_0
\]

sind die Träger von

\[
U_{s/2}a
\quad\text{und}\quad
U_{-s/2}a
\]

disjunkt. Daher

\[
\boxed{
\|D_sa\|_2^2
=2\|a\|_2^2.
}
\]

Für `R>2R_0` und `e^R<p\le e^{2R}` ist `\log p>R>2R_0`, also

\[
\|D_{\log p}a\|_2^2=2\|a\|_2^2.
\]

---

## 7. Divergenzuntergrenze

Aus §§4–6 folgt

\[
\boxed{
\mathfrak G_R^{pr}(a,a)
\ge
2\|a\|_2^2
\sum_{e^R<p\le e^{2R}}
\frac{\log p}{\sqrt p}(1-p^{-1}).
}
\]

Mit dem Primzahlsatz und partieller Summation gilt

\[
\sum_{p\le X}\frac{\log p}{\sqrt p}
\sim2\sqrt X.
\]

Daher

\[
\sum_{e^R<p\le e^{2R}}
\frac{\log p}{\sqrt p}(1-p^{-1})
\longrightarrow\infty.
\]

Somit für jedes feste `0\neq a\in C_c^\infty`:

\[
\boxed{
\mathfrak G_R^{pr}(a,a)
\longrightarrow+\infty.
}
\]

Status: `✓[M]_{neg}` gegen den unrenormierten globalen Synthesegrenzwert.

---

## 8. Vergleich mit der exakten Weilform

Für ein festes `a,b\in\mathcal A_{PW}` ist

\[
g_{a,b}\in C_c^\infty.
\]

Daher stabilisiert der Primblock entlang des source-induced Cutoffs exakt:

\[
B_{fin}^{\mathcal N_R}(a,b)
=B_{fin}(a,b)
\]

für alle hinreichend großen `R`.

Gamma- und Polblock hängen nicht von `R` ab. Somit ist

\[
B_W^{\mathcal N_R}(a,b)
=B_W(a,b)
\]

für alle hinreichend großen `R`.

Für `a=b\neq0` ist dieser Wert endlich.

Zusammen mit §7:

\[
\boxed{
\mathfrak G_R^{pr}(a,a)\to\infty
\quad\text{während}\quad
B_W^{\mathcal N_R}(a,a)=B_W(a,a)\text{ stabilisiert}.}
\]

Damit kann die naive positive Hubform nicht die gesuchte positive Approximation mit verschwindendem Rest sein.

---

## 9. Was genau gescheitert ist

Ausgeschlossen ist die Source-Synthese

\[
\boxed{
a\mapsto\sum_{n\in\mathcal N_R}\sqrt{w_n}D_{\log n}a\otimes\zeta_n}
\]

mit **derselben skalaren Amplitude `a` in jedem Prime-Power-Kanal** und ohne zusätzliche Regulator-/Quotientenstruktur.

Nicht ausgeschlossen sind:

1. labelabhängige Quellamplituden aus dem verfeinerten BC-Momentport C1m;
2. ein kanonischer `u`-/KMS-/Dirichlet-Regulator;
3. ein Quotient, der die divergenten primspezifischen Restanteile kontrolliert;
4. eine renormierte Synthese mit separat bewiesenem Grenzwert;
5. eine Schur-/Feshbach-artige positive Oberstruktur, solange P10-Firewalls beachtet werden.

---

## 10. Wo die Divergenz sitzt

Die Divergenzuntergrenze stammt ausschließlich aus den orthogonalen primspezifischen Restsektoren

\[
K_p^0.
\]

Damit ist nicht der **gemeinsame neutrale Hub** als solcher widerlegt.

Strukturell:

\[
\boxed{
\text{GCD-Hubkopplung lebt weiter; die unregulierte Summe der primspezifischen Tails ist das Problem.}
}
\]

Dies ist wichtig für den nächsten Knoten.

---

## 11. Verbindung zum historischen `u`-Regulator

P05/NEU-226 halten fest, dass bereits im Feshbach-/Primkanalbild die Summationsreichweite über den internen Index `u` ein echter Regulator ist und über Schatten-/Definiertheitsfragen entscheidet.

C1o findet unabhängig davon einen zweiten, jetzt expliziten Regulierungsbedarf auf der **Prime-Power-Label-Synthese**.

P11 darf beide Regulatoren nicht stillschweigend gleichsetzen. Zu prüfen ist, ob eine gemeinsame adelische/KMS-Struktur sie koppelt.

---

## 12. Statusmatrix

| Aussage | Status |
|---|---|
| endliche Hub-Gramform `G_R^pr` PSD | `✓[K/M]` |
| exakter Rest zu `B_fin^N_R` | `✓[K/M]` |
| Sternzerlegung liefert orthogonale primspezifische Untergrenze | `✓[K/M]` |
| große Primkanäle `e^R<p<=e^{2R}` enthalten nur `k=1` | `✓[M]` |
| `||D_logp a||^2=2||a||^2` für große `p` bei festem kompaktem `a` | `✓[M]` |
| `G_R^pr(a,a)->infty` | `✓[M]_{neg}` |
| naive Hubform approximiert `B_W` mit Rest `->0` | `×[M]` |
| GCD-Labelkern selbst falsch/unbrauchbar | **nein; nicht widerlegt** |
| neutraler Hub selbst Divergenzursache | **nicht bewiesen; Untergrenze kommt aus `K_p^0`** |
| regulierte/quotientierte Synthese | `?[O]` |
| labelabhängige Quellamplituden aus C1m | `?[O]` |

---

## 13. Wichtigster P11-Befund

P11 hat nun erstmals die beiden Fragen sauber getrennt:

\[
\boxed{
\text{Kopplungsgeometrie: konstruiert}
\qquad\neq\qquad
\text{globaler Synthesegrenzwert: noch offen}.
}
\]

Die BC-GCD-Sterngeometrie ist kanonisch und positiv. Aber sie darf nicht mit einer unregulierten Summe identischer Quellamplituden über alle Prime-Power-Labels globalisiert werden.

---

## 14. Nächster Knoten

\[
\boxed{[P11\text{-}C1p]\quad\text{Regulatoraudit der neutralen Hub-/primspezifischen Zerlegung}.}
\]

Zu prüfen sind zunächst zwei kanonische Regulatorquellen:

1. **BC/KMS-Dirichletgewicht** `n^{-\sigma}` vor dem kritischen Grenzwert;
2. **verfeinerte adelische Momentamplituden** aus C1m.

Ziel ist nicht, einen Faktor so zu wählen, dass der Grenzwert passt. Ziel ist festzustellen, ob eine bereits vorhandene source-induzierte Gewichtung die in C1o lokalisierte Divergenz kontrolliert und dabei die exakten Prime-Power-Weilgewichte nach einer nachweisbaren Renormierung wiederherstellt.
