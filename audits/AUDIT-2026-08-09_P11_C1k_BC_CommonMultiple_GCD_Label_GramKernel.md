# P11-C1k — BC/Common-Multiple-Mediator und kanonischer GCD-Label-Gramkern

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1k]`  
**Vorgänger:** P11-C1g–C1j + Targeted-Reaudit C1i/C1j  
**Quellenbasis:** multiplikative Halbgruppe `\mathbb N^\times`, BC-Dirichlet-/KMS-Gewicht `\zeta(\beta)` für `\beta>1` (P01/NEU-250g), Prime-Power-Labels `n=p^k`  

**Urteil:**

\[
\boxed{[P11-C1k]\quad\checkmark[K/M]_{\rm part}}
\]

Es existiert RH-frei und ohne frei angepasste Matrix ein kanonischer positiver Label-Gramkern auf allen natürlichen Labels:

\[
\boxed{
c(n,m):=\frac{\gcd(n,m)}{\sqrt{nm}}.
}
\]

Er entsteht als kritischer `\beta\downarrow1`-Grenzwert eines normalisierten BC-/Dirichlet-Common-Multiple-Gramkerns und besitzt zugleich eine direkte endliche Divisor-Inzidenzrealisierung. Auf jeder endlichen Menge verschiedener Labels ist die Gram-Matrix **streng positiv definit**. Für verschiedene Prime-Power-Labels ist der Kreuzblock nichtnull.

Damit ist erstmals im P11-Strang ein kanonischer, cutoff-kompatibler, markierungserhaltender und nichtorthogonaler **arithmetischer Label-Gramkern** konstruiert.

Nicht bewiesen ist, dass genau dieser Kern die endgültige Objekt-X-Kopplung ist oder dass seine Kombination mit der analytischen Inzidenzgeometrie die vollständige Weilform positiv realisiert.

---

## 1. Motivation aus C1j: Mischsektor nur als Mediator

Für `p\neq q` liegt eine direkte Kollisionsgleichheit

\[
pm_p=qm_q=M
\]

notwendig auf einem gemischt zusammengesetzten Ziel `M` mit `\Lambda(M)=0`.

Daher darf der Mischsektor keinen zusätzlichen **diagonalen** Weilkoeffizienten erhalten. Er kann aber als gemeinsamer Ziel-/Mediatorraum für verschiedene Prime-Power-Labels dienen.

Die natürliche multiplikative Relation ist:

\[
\boxed{n\longmapsto nr,\qquad r\in\mathbb N^\times.}
\]

Für zwei Labels `n,m` überlappen ihre Multiplikationsorbits genau auf den gemeinsamen Vielfachen.

---

## 2. Dirichlet-gewichtete Common-Multiple-Vektoren

Sei

\[
\mathcal H_{\rm cm}:=\ell^2(\mathbb N_{\ge1})
\]

mit kanonischer Basis `(e_M)_{M\ge1}`.

Für `\beta>1` und jedes `n\ge1` definiere

\[
\boxed{
\xi_n^{(\beta)}
:=
\frac1{\sqrt{\zeta(\beta)}}
\sum_{r\ge1}r^{-\beta/2}e_{nr}.
}
\]

Die Reihe liegt in `\ell^2`, weil

\[
\sum_{r\ge1}r^{-\beta}=\zeta(\beta)<\infty.
\]

Außerdem

\[
\boxed{\|\xi_n^{(\beta)}\|^2=1.}
\]

Die Definition benutzt nur:

1. die multiplikative Halbgruppe;
2. die Dirichletgewichte `r^{-\beta}`;
3. die BC-/KMS-Normalisierung `\zeta(\beta)`.

Keine Nullstellendaten und keine RH-Annahme treten auf.

---

## 3. Exakte Berechnung des Gramkerns

Seien

\[
g:=\gcd(n,m),
\qquad
n=ga,
\qquad
m=gb,
\qquad
(a,b)=1.
\]

Ein gemeinsamer Basisvektor tritt genau dann auf, wenn

\[
nr=ms.
\]

Dies ist äquivalent zu

\[
ar=bs.
\]

Wegen `(a,b)=1` existiert eindeutig `t\ge1` mit

\[
r=bt,
\qquad
s=at.
\]

Daher

\[
\begin{aligned}
\left\langle\xi_n^{(\beta)},\xi_m^{(\beta)}\right\rangle
&=
\frac1{\zeta(\beta)}
\sum_{t\ge1}(bt)^{-\beta/2}(at)^{-\beta/2}\\
&=
(ab)^{-\beta/2}.
\end{aligned}
\]

Da

\[
ab=\frac{nm}{g^2},
\]

folgt

\[
\boxed{
\left\langle\xi_n^{(\beta)},\xi_m^{(\beta)}\right\rangle
=
\left(
\frac{\gcd(n,m)}{\sqrt{nm}}
\right)^\beta.
}
\]

Status: `✓[K/M]`.

---

## 4. Prime-Power-Spezialisierung

Für

\[
n=p^k,
\qquad
m=q^\ell
\]

ergibt sich:

### Verschiedene Primzahlen `p\neq q`

\[
\gcd(p^k,q^\ell)=1,
\]

also

\[
\boxed{
c_\beta((p,k),(q,\ell))
=p^{-k\beta/2}q^{-\ell\beta/2}>0.}
\]

### Gleiche Primzahl `p=q`

\[
\gcd(p^k,p^\ell)=p^{\min(k,\ell)},
\]

also

\[
\boxed{
c_\beta((p,k),(p,\ell))
=p^{-\beta|k-\ell|/2}.}
\]

### Diagonale

\[
\boxed{c_\beta((p,k),(p,k))=1.}
\]

Damit ist die Labelgeometrie weder orthogonal noch rang-eins-kollabiert.

---

## 5. Kritischer Grenzwert `\beta\downarrow1`

Für jedes feste Paar `n,m` existiert der Grenzwert

\[
\boxed{
\lim_{\beta\downarrow1}
\left\langle\xi_n^{(\beta)},\xi_m^{(\beta)}\right\rangle
=
\frac{\gcd(n,m)}{\sqrt{nm}}.
}
\]

Definiere daher

\[
\boxed{
c(n,m):=\frac{\gcd(n,m)}{\sqrt{nm}}.}
\]

Für jede endliche Labelmenge ist die Matrix `C=(c(n_i,n_j))` als Grenzwert positiver Gram-Matrizen positiv semidefinit.

**Firewall:** Die Vektoren `\xi_n^{(\beta)}` besitzen bei `\beta=1` nicht einfach einen starken Grenzwert in derselben `\ell^2`-Realisierung; die Normierungsquelle `\zeta(\beta)` divergiert. Der **Gramkern** besitzt jedoch einen wohldefinierten endlichen Grenzwert.

---

## 6. Direkte kritische Divisor-Inzidenzrealisierung

Der kritische Kern benötigt keine Grenzraum-Heuristik. Verwende die klassische Identität

\[
\boxed{
\sum_{d\mid n}\varphi(d)=n.
}
\]

Auf

\[
\mathcal H_{\rm div}:=\ell^2(\mathbb N_{\ge1})
\]

definiere direkt

\[
\boxed{
\xi_n^{\rm div}
:=
\frac1{\sqrt n}
\sum_{d\mid n}\sqrt{\varphi(d)}\,e_d.
}
\]

Dann

\[
\|\xi_n^{\rm div}\|^2
=
\frac1n\sum_{d\mid n}\varphi(d)
=1.
\]

Für zwei Labels:

\[
\begin{aligned}
\langle\xi_n^{\rm div},\xi_m^{\rm div}\rangle
&=
\frac1{\sqrt{nm}}
\sum_{d\mid n,\,d\mid m}\varphi(d)\\
&=
\frac1{\sqrt{nm}}
\sum_{d\mid\gcd(n,m)}\varphi(d)\\
&=
\boxed{\frac{\gcd(n,m)}{\sqrt{nm}}.}
\end{aligned}
\]

Somit besitzt der kritische GCD-Kern eine explizite **finite-support** Gramrealisierung.

Status: `✓[K/M]`.

---

## 7. Strikte Positivität auf endlichen Mengen verschiedener Labels

Seien `n_1,\ldots,n_N` paarweise verschieden.

Die unnormierte GCD-Matrix

\[
G_{ij}:=\gcd(n_i,n_j)
\]

besitzt die Faktorisierung

\[
G=AA^*,
\]

mit

\[
A_{i,d}:=\sqrt{\varphi(d)}\,1_{d\mid n_i}.
\]

Um den Rang zu prüfen, ordne die `n_i` streng aufsteigend und betrachte nur die Spalten `d=n_j`. Dann gilt

\[
A_{i,n_j}=0
\quad\text{für }j>i,
\]

weil `n_j>n_i` nicht `n_i` teilen kann, während

\[
A_{i,n_i}=\sqrt{\varphi(n_i)}>0.
\]

Die entsprechende `N\times N`-Untermatrix ist dreieckig mit nichtverschwindender Diagonale. Also hat `A` Zeilenrang `N`.

Daher

\[
\boxed{G>0.}
\]

Da

\[
C=D^{-1/2}GD^{-1/2},
\qquad
D=\operatorname{diag}(n_1,\ldots,n_N)>0,
\]

folgt

\[
\boxed{C>0.}
\]

Damit ist der kritische Labelkern auf jeder endlichen Menge verschiedener Labels **streng positiv definit**, nicht bloß semidefinit.

---

## 8. Source-induced Cutoff-Kompatibilität

Für den C1f-Cutoff

\[
F_R=\{(p,k):p^k\le e^{2R}\}
\]

setze

\[
C_R
:=
\left(
\frac{\gcd(p^k,q^\ell)}{\sqrt{p^kq^\ell}}
\right)_{(p,k),(q,\ell)\in F_R}.
\]

Für `R<S` ist `C_R` exakt die Hauptuntermatrix von `C_S` auf `F_R`.

\[
\boxed{
C_R\text{ ist kanonisch verschachtelt und cutoff-kompatibel.}
}
\]

Die Vektoren `\xi_{p^k}^{div}` selbst hängen nicht von `R` ab.

---

## 9. Markierungserhalt ohne Labelkollaps

Da jede endliche GCD-Grammatrix strikt positiv definit ist, sind die Vektoren

\[
\{\xi_n^{div}:n\in F\}
\]

für jede endliche Menge verschiedener Labels linear unabhängig.

Damit bleibt die Labelinformation erhalten.

Gleichzeitig gilt für unterschiedliche Prime-Power-Labels aus verschiedenen Primkanälen

\[
\boxed{
\langle\xi_{p^k}^{div},\xi_{q^\ell}^{div}\rangle
=\frac1{\sqrt{p^kq^\ell}}>0.
}

Somit ist die Geometrie echt nichtorthogonal.

Dies löst exakt das abstrakte C1g-Dilemma zwischen

\[
C=I
\quad\text{und}\quad
C=\mathbf1\mathbf1^*.
\]

---

## 10. Verbindung zum Mischsektor

Die `\beta>1`-Realisierung hat eine direkte Common-Multiple-Lesart:

\[
\xi_n^{(\beta)}
\sim
\{nr:r\ge1\}.
\]

Für verschiedene Prime-Powers `p^k,q^\ell` liegen gemeinsame Koordinaten auf gemeinsamen Vielfachen und damit im gemischten Sektor.

Dieser Sektor erhält **kein** diagonales Mangoldtgewicht. Er dient ausschließlich dazu, Überlappung zu vermitteln.

Damit wird die offene Mediatoridee aus NEU-250j konkretisiert, ohne `\Lambda=0`-Zustände als zusätzliche Weilkoeffizienten zu zählen.

**Wichtig:** Dies ist eine neue P11-Konstruktion aus der multiplikativen/Dirichlet-Struktur; NEU-250j selbst hatte diesen Operator noch nicht konstruiert.

---

## 11. Verhältnis zur BC-KMS-Struktur

NEU-250g/P01 verwenden für `\beta>1` die Dirichlet-/KMS-Struktur mit dem Partitionsfaktor

\[
\zeta(\beta).
\]

C1k benutzt genau dieselbe Konvergenzskala und denselben Normalisierungsfaktor, jetzt auf dem semigruppeninduzierten Common-Multiple-Orbit.

Damit ist `c_\beta` nicht durch Rückwärtsvergleich mit der Weilform gewählt.

**Scope-Firewall:** P01 beweist keine vollständige Hilbert-Operatorrealisierung aller `p^k`-Gewichte. C1k benötigt diese starke Operatoraussage nicht; der Labelkern wird direkt auf dem arithmetischen Semigruppenraum konstruiert.

---

## 12. Kombination mit der analytischen Inzidenzgeometrie aus C1c

Für ein Prime-Power-Label

\[
\alpha=(p,k),
\qquad
n_\alpha=p^k,
\]

sei

\[
V_\alpha^{an}
:=
\sqrt{w_\alpha}\,D_{k\log p},
\qquad
w_\alpha=\frac{\log p}{p^{k/2}}.
\]

Definiere nun die markierungserhaltende Analyseabbildung

\[
\boxed{
\widetilde V_\alpha a
:=
V_\alpha^{an}a\otimes\xi_{p^k}^{div}
\in
L^2(\mathbb R)\otimes\mathcal H_{div}.
}
\]

Dann lautet der Kreuzblock

\[
\boxed{
\widetilde G_{\alpha\beta}(a,b)
=
\frac{\gcd(p^k,q^\ell)}{\sqrt{p^kq^\ell}}
\sqrt{w_\alpha w_\beta}
\langle D_{k\log p}a,D_{\ell\log q}b\rangle.
}
\]

Für jede endliche Familie `(a_\alpha)` gilt automatisch

\[
\sum_{\alpha,\beta}
\widetilde G_{\alpha\beta}(a_\alpha,a_\beta)
=
\left\|
\sum_\alpha
V_\alpha^{an}a_\alpha\otimes\xi_{n_\alpha}^{div}
\right\|^2
\ge0.
\]

Damit ist erstmals eine **vollständig explizite, liftfreie, RH-freie, markierungserhaltende und nichtorthogonale Prime-Power-Gramgeometrie** konstruiert.

Status: `✓[K/M]` als positive Vor-/Labelgeometrie.

---

## 13. Diagonalverträglichkeit

Da

\[
c(n,n)=1,
\]

ändert die Labelgeometrie die Diagonalnorm jedes analytischen Prime-Power-Kanals nicht:

\[
\boxed{
\widetilde G_{\alpha\alpha}(a,b)
=G_{\alpha\alpha}^{an}(a,b).
}
\]

Sie aktiviert ausschließlich zusätzliche geometrische Überlappungen zwischen verschiedenen Labels.

Das ist für P11 strukturell ideal: die in C1c/C1d fixierten lokalen Inzidenzenergien bleiben unverändert.

---

## 14. Entscheidende Firewall: noch keine Weil-Kompression

Aus der Positivität von `\widetilde G` folgt **nicht**

\[
B_W(a,b)
=
\langle\mathcal T_Xa,\mathcal T_Xb\rangle.
\]

Insbesondere dürfen die Off-Diagonalblöcke nicht als zusätzliche Summanden zur expliziten Weilzerlegung addiert werden.

Offen bleibt eine kanonische Source-/Kompressionsabbildung, deren positive globale Gramform die latente Geometrie `\widetilde G` nutzt und deren komprimierte Form **exakt** die bereits fixierte Weilform bzw. eine kontrollierte positive Approximation mit Restterm ergibt.

NEU-250/P10 bleiben vollständig respektiert.

---

## 15. Kanonizitätscheck K1–K10 (vorläufig)

| Test | C1k-Befund |
|---|---|
| keine frei gewählte Kopplungsmatrix | **PASS** — GCD-Kern aus Semigruppe/Dirichletstruktur |
| RH-/Nullstellendaten als Input | **PASS** — keine |
| voller Prime-Power-Index | **PASS** |
| Hermiteschkeit | **PASS** — reell symmetrisch |
| Positivität endlicher Gramblöcke | **PASS**, sogar strikt positiv |
| source-induced Cutoff-Kompatibilität | **PASS** |
| Markierungserhalt | **PASS** auf endlichen Cutoffs |
| Nichtorthogonalität | **PASS** |
| archimedische Kopplung | **OFFEN** |
| exakte Weil-Kompression / Restkontrolle | **OFFEN** |

---

## 16. Statusmatrix

| Aussage | Status |
|---|---|
| Common-Multiple-Vektor `xi_n^(beta)` für `beta>1` | `✓[K/M]` |
| Gramform `c_beta(n,m)=(gcd(n,m)/sqrt(nm))^beta` | `✓[K/M]` |
| kritischer Kernel `c(n,m)=gcd(n,m)/sqrt(nm)` | `✓[K/M]` |
| direkte Divisor-Inzidenzrealisierung via `phi(d)` | `✓[K/M]` |
| strikte Positivität auf endlichen verschiedenen Labels | `✓[K/M]` |
| Prime-Power-Crossprime-Wert `1/sqrt(p^kq^l)` | `✓[M]` |
| cutoff-kompatible Familie `C_R` | `✓[K/M]` |
| kritischer `ell^2`-Grenzvektor der Common-Multiple-Realisierung | **nicht behauptet** |
| kombinierte analytisch-arithmetische Gramgeometrie `\widetilde G` PSD | `✓[K/M]` |
| `\widetilde G` ist bereits Objekt X | `×[M]` als Schlussfolgerung |
| exakte Weil-Kompression | `?[O]` |
| archimedisch–arithmetische Labelkopplung | `?[O]` |

---

## 17. Wichtigster P11-Befund bisher

Vor C1k fehlte genau die arithmetische positive Labelgeometrie aus C1g.

Nach C1k liegt ein kanonischer Kandidat explizit vor:

\[
\boxed{
C_{(p,k),(q,\ell)}^{can}
=
\frac{\gcd(p^k,q^\ell)}{\sqrt{p^kq^\ell}}.
}
\]

Zusammen mit C1c:

\[
\boxed{
\widetilde G_{(p,k),(q,\ell)}
=
C_{(p,k),(q,\ell)}^{can}
\times
G_{(p,k),(q,\ell)}^{an}.
}
\]

Damit sind **beide Faktoren** der Prime-Power-Kreuzgeometrie nun explizit konstruiert:

1. analytische Überlappung aus dem Translationsfluss;
2. arithmetische Labelüberlappung aus GCD/Common-Multiple-Geometrie.

Der nächste Engpass ist nicht mehr `B_{pq}` selbst, sondern die **globale Source-Kompression einschließlich des archimedischen Kanals und des Defekts**.

---

## 18. Nächster Knoten

\[
\boxed{[P11\text{-}C1l]\quad\text{Archimedische Erweiterung des GCD/Common-Multiple-Labelraums und exakte Kompressionsfrage}.}
\]

Zu prüfen sind zwei Möglichkeiten ohne freie Parameter:

1. Kann der archimedische kontinuierliche Kantenmaßraum aus C1d als zusätzlicher kanonischer Labelsektor an dieselbe Divisor-/Semigruppengeometrie gekoppelt werden?
2. Falls direkte Archimedes–Prime-Labelkopplung nicht kanonisch ist: Kann die positive Prime-Power-Gramgeometrie als endlicher `G_F`-Teil in einer `G_F-R_F`-Approximation verwendet werden, wobei der Defekt aus C1e separat und kontrolliert gegen Null geführt wird?
