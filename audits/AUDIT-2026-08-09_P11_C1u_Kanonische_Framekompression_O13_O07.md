# P11-C1u — Kanonische Framekompression aus BC-GCD-Inzidenz: O13-Kandidat, L2-Kollaps und O07-Firewall

**Datum:** 9. August 2026  
**Block:** P11 — Global Coupling and the Object-X Candidate Geometry  
**Status:** `✓[K/M]_part` mit modellgebundenem Negativbefund  
**Vorgänger:** `AUDIT-2026-08-09_P11_PassA_CHECKPOINT_SourceFirst_C1-C1t.md`  
**P10-Schnittstellen:** `P10-O05`, `P10-O13`, `P10-O07`

> **Scope-Firewall.** Dieser Knoten untersucht ausschließlich die direkte source-first Vorgeometrie aus C1–C1t auf dem unkomprimierten Translationsraum `L^2(R)` mit dem BC-GCD-Labelraum. Er beweist keinen globalen No-Go gegen nichttranslationinvariante, fensterabhängige, Feshbach-, Quotienten- oder andere relative Kompressionen.

---

## 0. Ausgangspunkt

Für ein Prime-Power-Label

\[
n=p^k,
\qquad
\lambda_n:=\frac{\Lambda(n)}{\sqrt n}=\frac{\log p}{p^{k/2}},
\qquad
s_n:=\log n=k\log p,
\]

liefert der C1-Checkpoint

\[
D_s:=U_{s/2}-U_{-s/2}
\]

und die normierten BC-Rangevektoren

\[
\zeta_n:=\sqrt n\,E_n,
\qquad
\langle\zeta_n,\zeta_m\rangle
=\frac{\gcd(n,m)}{\sqrt{nm}}.
\]

Für den source-induzierten Cutoff

\[
\mathcal N_R:=\{p^k:p^k\le e^{2R}\}
\]

definiere die direkte positive Synthese

\[
\boxed{
\mathcal V_R a
:=
\sum_{n\in\mathcal N_R}
\sqrt{\lambda_n}\,D_{\log n}a\otimes\zeta_n.}
\tag{C1u.1}
\]

C1o/C1t zeigen: `||V_R a||` divergiert für jedes feste nichtverschwindende kompakt getragene `a`; labeldiagonale Dämpfung mit punktweiser Rückkehr zu 1 genügt nicht.

Die Frage ist daher: Gibt es eine **source-kanonische nichtdiagonale positive Metrik**, die ausschließlich aus `V_R` selbst entsteht?

---

# 1. Kanonischer Frameoperator

Definiere

\[
\boxed{A_R:=\mathcal V_R^*\mathcal V_R\ge0.}
\tag{C1u.2}
\]

Da `N_R` endlich ist und jedes `D_s` beschränkt ist, ist `A_R` für festes `R` ein beschränkter positiver Operator auf `L^2(R)`.

Der parameterfreie bounded-transform Kandidat lautet

\[
\boxed{W_R^{\rm can}:=(I+A_R)^{-1}.}
\tag{C1u.3}
\]

Dann ist

- `0 < W_R^{can} <= I`,
- `W_R^{can}` vollständig aus der bereits konstruierten Vorgeometrie bestimmt,
- keine freie Labelmatrix und kein externer Renormierungsparameter wird eingeführt.

Die normalisierte Synthese ist

\[
\boxed{
T_R:=\mathcal V_R(I+A_R)^{-1/2}.}
\tag{C1u.4}
\]

Exakt gilt

\[
T_R^*T_R
=(I+A_R)^{-1/2}A_R(I+A_R)^{-1/2}
=A_R(I+A_R)^{-1}.
\tag{C1u.5}
\]

Daher

\[
\boxed{0\le T_R^*T_R\le I,\qquad \|T_R\|\le1.}
\tag{C1u.6}
\]

**Befund:** Die C1o-Divergenz kann durch eine kanonische **nichtskalare source-Metrik** tatsächlich kontrolliert werden.

Status: `✓[K/M]` als Konstruktion.

---

# 2. Fourier-Symbol des Frameoperators

Alle `D_s` sind Funktionen desselben Translationsflusses. Im Fourierbild gilt, bis auf die für die Norm irrelevante gemeinsame Vorzeichenkonvention,

\[
\widehat{D_sa}(\xi)
=d_s(\xi)\widehat a(\xi),
\qquad
d_s(\xi):=2i\sin\!\left(\frac{s\xi}{2}\right).
\]

Damit ist `A_R` ein Multiplikationsoperator

\[
\boxed{A_R\simeq M_{m_R}}
\tag{C1u.7}
\]

mit dem nichtnegativen Symbol

\[
\boxed{
m_R(\xi)
:=
\left\|
\sum_{n\in\mathcal N_R}
\sqrt{\lambda_n}\,
2i\sin\!\left(\frac{\xi\log n}{2}\right)
\zeta_n
\right\|_{K_{\mathcal P^*}}^2.}
\tag{C1u.8}
\]

Aus dem GCD-Gram folgt äquivalent

\[
m_R(\xi)
=
\sum_{n,m\in\mathcal N_R}
\sqrt{\lambda_n\lambda_m}
\frac{\gcd(n,m)}{\sqrt{nm}}
\overline{d_{\log n}(\xi)}\,d_{\log m}(\xi).
\tag{C1u.9}
\]

Positivität ist hier keine zusätzliche Annahme, sondern die Normquadratdarstellung (C1u.8).

---

# 3. Strikte Positivität für `xi != 0`

Auf jeder endlichen Menge verschiedener Labels ist die GCD-Grammatrix streng positiv definit. Daher sind die entsprechenden `zeta_n` linear unabhängig.

Sobald `R` so groß ist, dass `2,3 in N_R`, folgt aus `m_R(xi)=0`, dass insbesondere

\[
\sin\!\left(\frac{\xi\log2}{2}\right)=0,
\qquad
\sin\!\left(\frac{\xi\log3}{2}\right)=0.
\]

Für `xi != 0` würde dies `log2/log3 in Q` erzwingen, also `2^a=3^b` für geeignete positive ganze Zahlen `a,b`, unmöglich.

Damit

\[
\boxed{m_R(0)=0,\qquad m_R(\xi)>0\quad(\xi\ne0)}
\tag{C1u.10}
\]

für alle hinreichend großen `R`.

Insbesondere ist `W_R^{can}` nicht skalar.

Status: `✓[M]`.

---

# 4. Punktweises Wachstum `m_R(xi) -> infinity`

Verwende die Sternzerlegung aus C1n:

\[
\zeta_p=p^{-1/2}\zeta_1+\eta_{p,1},
\qquad
K_p^0\perp K_q^0\quad(p\ne q),
\qquad
\|\eta_{p,1}\|^2=1-p^{-1}.
\]

Für Primzahlen im Hochband

\[
e^R<p\le e^{2R}
\]

liegt im Cutoff `N_R` nur der Exponent `k=1`, denn `p^2>e^{2R}`. Deshalb kann in diesen `K_p^0`-Komponenten keine höhere `p^k`-Komponente den `k=1`-Anteil kompensieren. Aus orthogonaler Projektion auf die Summe dieser Restsektoren folgt

\[
\boxed{
m_R(\xi)
\ge
4\sum_{e^R<p\le e^{2R}}
\frac{\log p}{\sqrt p}
\left(1-\frac1p\right)
\sin^2\!\left(\frac{\xi\log p}{2}\right).}
\tag{C1u.11}
\]

Für jedes feste `xi != 0` besitzt `sin^2(xi t/2)` in jeder hinreichend langen `t`-Periode einen Teilintervallanteil, auf dem es von null weg beschränkt ist. Mit dem Primzahlsatz auf den entsprechenden festen multiplikativen Teilintervallen im Band `[e^R,e^{2R}]` wächst die rechte Seite ohne Schranke.

Folglich

\[
\boxed{m_R(\xi)\longrightarrow\infty
\qquad\text{für jedes feste }\xi\ne0.}
\tag{C1u.12}
\]

Status: `✓[M]` (PNT-basiert; derselbe asymptotische Werkzeugtyp ist im Programm bereits zugelassen).

---

# 5. Der kanonische bounded transform kollabiert im Grenzgram auf `L^2`

Aus (C1u.7) folgt

\[
W_R^{\rm can}
\simeq
M_{(1+m_R)^{-1}},
\]

und

\[
\boxed{
T_R^*T_R
\simeq
M_{k_R},
\qquad
k_R(\xi):=\frac{m_R(\xi)}{1+m_R(\xi)}.}
\tag{C1u.13}
\]

Nach (C1u.12):

\[
k_R(\xi)\to1
\quad\text{für a.e. }\xi,
\qquad
0\le k_R\le1.
\]

Dominierte Konvergenz liefert für jedes `a in L^2(R)`

\[
\boxed{
T_R^*T_R a\longrightarrow a
\quad\text{stark in }L^2(\mathbb R).}
\tag{C1u.14}
\]

Damit

\[
\boxed{
\langle T_Ra,T_Rb\rangle
\longrightarrow
\langle a,b\rangle_{L^2}.}
\tag{C1u.15}
\]

**Entscheidung:** `W_R^{can}=(I+A_R)^{-1}` ist ein echter kanonischer positiver nichtskalarer Prämetrik-Kandidat, aber **kein Objekt-X-Endpunkt**. Seine direkte Grenzgramform ist die gewöhnliche Quell-`L^2`-Geometrie. P03 sperrt gerade die Identifikation des Haar-/Quell-`L^2`-Abschlusses mit dem finalen Weilformraum.

Status:

\[
\boxed{\text{P10-O13: konstruktiver Kandidat }\checkmark[K/M]_{part},\quad
\text{Weil-Kompatibilität }?[O].}
\]

---

# 6. O07-Firewall: kein Schatten-/Fredholmobjekt in diesem direkten Modell

Für jedes hinreichend große feste `R` ist

\[
k_R(\xi)>0\qquad\text{für a.e. }\xi.
\]

Auf dem nichtatomaren Maßraum `L^2(R,d\xi)` ist ein nichtverschwindender Multiplikationsoperator nicht kompakt. Daher ist

\[
\boxed{T_R^*T_R=M_{k_R}\notin\mathcal K(L^2(\mathbb R)).}
\tag{C1u.16}
\]

Insbesondere

\[
\boxed{T_R^*T_R\notin\mathcal S_p
\qquad\forall p<\infty.}
\tag{C1u.17}
\]

Dasselbe gilt für jede nichttriviale reine Multiplikations-Funktionalkalkülvariante `f(A_R)`, sofern `f(m_R)` auf einer Menge positiven Maßes nicht verschwindet.

**Scope:** Dies ist kein globaler No-Go gegen P10-O07. Es schließt nur die direkte unkomprimierte translationinvariante Frame-Normalisierung als Quelle einer `S_4\setminus S_2`- beziehungsweise Schatten-Fredholm-Brücke aus.

Ein erfolgreicher O07-Mechanismus muss daher mindestens eine zusätzliche Struktur einführen, welche die reine Fourier-Multiplikationsgeometrie bricht, z.B.

- echte relative/Feshbach-Kompression,
- source-window-/boundary-sensitive Geometrie,
- einen nichttranslationinvarianten Quotienten/Deszent,
- oder eine andere kompaktifizierende Schicht.

Status:

\[
\boxed{\text{P10-O07 bleibt OPEN; direkter C1u-Frameweg }\checkmark[M]_{neg,scope}.}
\]

---

# 7. O05-Reconciliation

Für die **konkrete BC-GCD-Kandidatengeometrie** ist die Primorthogonalitätsfrage inzwischen partiell entschieden:

\[
K_{\mathcal P^*}
=\mathbb C\zeta_1\oplus\bigoplus_pK_p^0,
\qquad K_p^0\perp K_q^0\;(p\ne q),
\]

während

\[
\langle\zeta_{p^k},\zeta_{q^\ell}\rangle
=\frac1{\sqrt{p^kq^\ell}}>0
\qquad(p\ne q).
\]

Damit gilt im **C1-Kandidatenmodell**:

- globale Primorthogonalität: nein;
- Kreuzblöcke: explizit vorhanden;
- gesamter Kreuzprimanteil des reinen BC-Labelgrams läuft durch den neutralen Hub `zeta_1`.

Dies schließt P10-O05 nicht global, weil O05 alle möglichen Objekt-X-Kopplungen betrifft. Aber für die aktuelle P11-Kandidatengeometrie ist die Frage konstruktiv beantwortet.

\[
\boxed{\text{P10-O05 }\to\checkmark[K/M]_{part}\text{ im BC-GCD-C1-Scope}.}
\]

---

# 8. Gesamtaussage C1u

Der C1u-Test liefert erstmals **eine kanonische positive nichtskalare source-Metrik ohne freie Parameter**:

\[
\boxed{W_R^{\rm can}=(I+\mathcal V_R^*\mathcal V_R)^{-1}.}
\]

Sie ist mathematisch sauber, kontrolliert die C1o-Divergenz und beantwortet P10-O13 partiell konstruktiv.

Aber zwei starke Firewalls treten sofort auf:

1. ihr Grenzgram kollabiert stark zur gewöhnlichen `L^2`-Quellgeometrie;
2. ihr Gramoperator ist im direkten Translationsmodell ein nichtkompakter Multiplikationsoperator und liefert daher keine Schatten-/Fredholm-Brücke.

Damit ist der nächste Engpass präziser als vor C1u:

\[
\boxed{
\text{Nicht nur eine nichtskalare Metrik fehlt, sondern eine}
\\
\textbf{relative, nichttranslationinvariante Kompression,}
\\
\text{die den BC-GCD-Hub erhält, die Hochprim-Restdivergenz kontrolliert}
\\
\text{und zugleich nicht auf }L^2\text{ kollabiert.}}
\]

---

## 9. Nächster atomarer Knoten

\[
\boxed{\text{P11-C1v: relative/Feshbach-Kompression des Frameoperators }A_R}
\]

Prüffragen:

1. Gibt es aus P05/P06 bereits eine **kanonische Projektion oder Schur-Komplementstruktur** `Q_R` mit `Q_R A_R Q_R`, die die reine Translationinvarianz bricht?
2. Bleibt der neutrale BC-Hub `zeta_1` erhalten, während nur ein wachsender Teil der `K_p^0`-Reststruktur relativiert wird?
3. Kann der resultierende Operator kompakt oder in `S_4\setminus S_2` liegen, ohne eine `Xi`-abhängige Regulatorwahl?
4. Ist die Kompression source-induced durch `R` beziehungsweise `N_R`, nicht rückwärts aus der Weilform definiert?

Bis zur Beantwortung bleibt P11 `PASS-A ACTIVE`; kein SYN, kein Seal.
