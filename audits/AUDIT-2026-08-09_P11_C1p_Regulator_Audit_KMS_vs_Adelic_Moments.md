# P11-C1p — Regulatoraudit: BC/KMS-Dirichletgewicht versus adelische Momentamplituden

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1p]`  
**Vorgänger:** P11-C1m–C1o  

**Urteil:**

\[
\boxed{[P11-C1p]\quad\checkmark[M]_{\rm part}}
\]

Zwei bereits quelleninduzierte Regulatoren kontrollieren die in C1o gefundene Synthesedivergenz, aber **keiner** reproduziert zugleich ohne weitere Renormierung den exakten Weil-Halbgewichtspunkt.

1. Der BC/KMS-Dirichletpfad liefert eine kanonische konvergente positive Synthese für `\beta>2`, stößt aber bei `\beta=2` auf eine echte Primzahlsingularität; der Zielpunkt `\beta=1` liegt jenseits dieser Barriere.
2. Die P02-Standardsektion liefert am kritischen GCD-Kern eine konvergente Momentensynthese, aber mit zu starker Dämpfung `\Lambda(n)/n^{3/2}` statt `\Lambda(n)/\sqrt n`. Das Entfernen dieser Dämpfung führt exakt zur C1o-Divergenz zurück.

Damit ist der Regulatorbedarf jetzt präzise: Gesucht ist eine **nichttriviale Renormierungs-/Quotientenstruktur**, nicht bloß ein weiterer frei gewählter Skalarcutoff.

---

# Teil A — BC/KMS-Dirichletregulator

## 1. `\beta`-abhängige lokale Gewichte

Für `\beta>1` setze auf Prime-Power-Labels

\[
\boxed{
w_n^{(\beta)}
:=
\Lambda(n)n^{-\beta/2},
\qquad n\in\mathcal P^*.}
\]

Am Weil-Punkt `\beta=1` würde formal

\[
w_n^{(1)}=\frac{\Lambda(n)}{\sqrt n}
\]

gelten.

Gleichzeitig liefert C1k für `\beta>1` den normierten Common-Multiple-Gramkern

\[
\boxed{
c_\beta(n,m)
=
\left(\frac{\gcd(n,m)}{\sqrt{nm}}\right)^\beta.}
\]

Beide Strukturen verwenden damit denselben BC-/Dirichletparameter.

---

## 2. Regulierter positiver Syntheseansatz

Für `\beta>2` definiere formal

\[
\boxed{
\mathcal T_\beta^{pr}a
:=
\sum_{n\in\mathcal P^*}
\sqrt{w_n^{(\beta)}}
D_{\log n}a\otimes\xi_n^{(\beta)}.
}
\]

Hier sind die `\xi_n^{(\beta)}` die normierten C1k-Common-Multiple-Vektoren mit Gram `c_\beta`.

---

## 3. Boundedness des `\beta`-Label-Gramoperators für `\beta>2`

Fixiere `n=p^k`.

Für Labels derselben Primzahl gilt

\[
c_\beta(p^k,p^\ell)=p^{-\beta|k-\ell|/2}.
\]

Daher ist die Summe innerhalb desselben Primblocks uniform beschränkt durch eine geometrische Reihe.

Für `q\neq p`:

\[
c_\beta(p^k,q^\ell)
=p^{-k\beta/2}q^{-\ell\beta/2}.
\]

Somit ist die gesamte Kreuzprim-Zeilensumme beschränkt durch

\[
p^{-k\beta/2}
\sum_q\sum_{\ell\ge1}q^{-\ell\beta/2},
\]

und diese Reihe konvergiert für

\[
\boxed{\beta>2.}
\]

Nach dem Schur-Test definiert die unendliche Matrix `C_\beta=(c_\beta(n,m))` auf `\ell^2(\mathcal P^*)` einen beschränkten positiven Operator.

Status: `✓[M]`.

---

## 4. Konvergenz der regulierten Synthese

Für jedes `a\in L^2(\mathbb R)` gilt

\[
\|D_{\log n}a\|\le2\|a\|.
\]

Daher

\[
\sum_{n\in\mathcal P^*}
\left\|
\sqrt{w_n^{(\beta)}}D_{\log n}a
\right\|^2
\le
4\|a\|^2
\sum_{n\ge2}\Lambda(n)n^{-\beta/2}.
\]

Für `\beta/2>1`:

\[
\sum_{n\ge2}\Lambda(n)n^{-\beta/2}
=
-\frac{\zeta'}{\zeta}(\beta/2)<\infty.
\]

Zusammen mit der Beschränktheit von `C_\beta` folgt, dass die Gramquadratik der Partialsummen Cauchy ist. Damit existiert für

\[
\boxed{\beta>2}
\]

eine wohldefinierte positive globale Prime-Power-Synthese.

Status: `✓[M]`.

---

## 5. Sternzerlegung auch für `c_\beta`

Da

\[
\langle\xi_1^{(\beta)},\xi_n^{(\beta)}\rangle=n^{-\beta/2},
\]

definiere

\[
\eta_n^{(\beta)}
:=
\xi_n^{(\beta)}-n^{-\beta/2}\xi_1^{(\beta)}.
\]

Für teilerfremde `n,m` gilt

\[
\langle\eta_n^{(\beta)},\eta_m^{(\beta)}\rangle=0.
\]

Insbesondere sind die primspezifischen Restsektoren für verschiedene Primzahlen orthogonal und

\[
\boxed{
\|\eta_p^{(\beta)}\|^2=1-p^{-\beta}.}
\]

---

## 6. Echte Barriere bei `\beta=2`

Fixiere wieder

\[
0\neq a\in C_c^\infty([-R_0,R_0]).
\]

Für große Primzahlen gilt

\[
\|D_{\log p}a\|^2=2\|a\|^2.
\]

Die orthogonalen primspezifischen Restanteile liefern daher die Untergrenze

\[
\|\mathcal T_\beta^{pr}a\|^2
\ge
2\|a\|^2
\sum_{p\gg1}
\log p\,p^{-\beta/2}(1-p^{-\beta}).
\]

Die Primreihe

\[
\sum_p\log p\,p^{-s}
\]

konvergiert für `s>1` und divergiert bei `s=1`.

Somit

\[
\boxed{
\|\mathcal T_\beta^{pr}a\|
\longrightarrow\infty
\quad\text{für}\quad\beta\downarrow2.}
\]

Die positive Hilbertsynthese besitzt also keine normstetige Fortsetzung durch `\beta=2`.

Der Weil-Punkt

\[
\beta=1
\]

liegt jenseits dieser Barriere.

---

## 7. Konsequenz für den KMS-Pfad

Der BC/KMS-Parameter ist ein **echter** source-induzierter Regulator, kein frei gewählter Cutoff.

Aber:

\[
\boxed{
\text{positive Synthese bei }\beta>2
\not\xrightarrow{\rm norm}
\text{Weil-Halbgewicht bei }\beta=1.
}
\]

Ein erfolgreicher KMS-Pfad müsste daher mindestens eine nichttriviale Operation an `\beta=2` enthalten:

- Finite-Part-/Residuenrenormierung;
- Quotient eines divergenten Restsektors;
- relative Gegenform;
- oder eine andere source-induzierte Kompensation.

Keine davon ist hier bereits konstruiert.

---

# Teil B — Adelische Momentamplituden

## 8. Standardsektion liefert `n^{-1/2}`-Dämpfung

C1m zeigt für den P02-Standardlift

\[
F_a^{(0)}(x,y)=h_a(x)E_1(y)
\]

und die BC-Momente

\[
M_nF_a^{(0)}(x)=\frac{h_a(x)}{\sqrt n}.
\]

Nach logarithmischer Umparametrisierung ist die entsprechende analytische Momentamplitude

\[
\boxed{a_n(u)=\frac{a(u)}{\sqrt n}.}
\]

Diese Dämpfung ist nicht frei gewählt; sie ist der Rangeprojektionsüberlappung

\[
\langle E_1,\zeta_n\rangle=n^{-1/2}
\]

geschuldet.

---

## 9. Momentenregulierte Prime-Synthese

Setze am kritischen C1k2-Labelkern

\[
\boxed{
\mathcal T_{mom}^{pr}a
:=
\sum_{n\in\mathcal P^*}
\sqrt{w_n}
D_{\log n}\left(\frac{a}{\sqrt n}\right)
\otimes\zeta_n,
\qquad
w_n=\frac{\Lambda(n)}{\sqrt n}.
}
\]

Da `D_s` linear ist:

\[
\mathcal T_{mom}^{pr}a
=
\sum_n
\sqrt{\Lambda(n)}\,n^{-3/4}
D_{\log n}a\otimes\zeta_n.
\]

---

## 10. Konvergenz der primspezifischen Restanteile

Mit C1n:

\[
\zeta_{p^k}=p^{-k/2}\zeta_1+\eta_{p,k}.
\]

Der primspezifische Koeffizient besitzt Betrag

\[
\sqrt{\log p}\,p^{-3k/4}.
\]

Für festen `p` ist die Summe über `k` absolut konvergent.

Über verschiedene Primzahlen sind die Räume `K_p^0` orthogonal. Daher genügt

\[
\sum_p
\left(
\sum_{k\ge1}
2\sqrt{\log p}\,p^{-3k/4}
\right)^2
<\infty.
\]

Die rechte Seite wird durch ein konstantes Vielfaches von

\[
\sum_p\frac{\log p}{p^{3/2}}
<\infty
\]

beschränkt.

Somit konvergiert der gesamte primspezifische Restteil in Hilbertnorm.

Status: `✓[M]`.

---

## 11. Konvergenz des neutralen Hubanteils

Der zusätzliche neutrale Faktor aus

\[
\zeta_n=n^{-1/2}\zeta_1+\eta_n
\]

liefert den Hubkoeffizienten

\[
\sqrt{\Lambda(n)}\,n^{-5/4}.
\]

Daher

\[
\sum_{n\in\mathcal P^*}
\sqrt{\Lambda(n)}\,n^{-5/4}<\infty.
\]

Wegen

\[
\|D_{\log n}a\|\le2\|a\|
\]

konvergiert der neutrale Hubteil sogar absolut in Hilbertnorm.

Folglich:

\[
\boxed{
\mathcal T_{mom}^{pr}a
\text{ ist für jedes }a\in L^2(\mathbb R)
\text{ wohldefiniert}.}
\]

Status: `✓[M]`.

---

## 12. Aber die Diagonalgewichte sind zu stark gedämpft

Der Diagonalbeitrag der Momentensynthese lautet

\[
\left(\sqrt{w_n}n^{-1/2}\right)^2
\|D_{\log n}a\|^2
=
\boxed{
\frac{\Lambda(n)}{n^{3/2}}
\|D_{\log n}a\|^2.}
\]

Die exakte Weil-Inzidenz aus C1c benötigt dagegen

\[
\boxed{
\frac{\Lambda(n)}{\sqrt n}
\|D_{\log n}a\|^2.}
\]

Es fehlt also exakt ein Faktor `n`.

---

## 13. Rückskalierung reproduziert C1o-Divergenz

Um aus der Momentamplitude

\[
a_n=a/\sqrt n
\]

wieder dieselbe analytische Amplitude `a` zu erzeugen, müsste jeder Kanal mit `\sqrt n` verstärkt werden.

Dann wird

\[
\sqrt n\,a_n=a
\]

und die Synthese ist exakt die naive C1o-Synthese

\[
\sum_n\sqrt{w_n}D_{\log n}a\otimes\zeta_n,
\]

die divergiert.

Somit:

\[
\boxed{
\text{adelische Momentdämpfung entfernt die Divergenz, aber zugleich den benötigten Weilgewichtsfaktor}.}
\]

Status: `✓[M]`.

---

## 14. Frame-Inversion behebt dieses Problem nicht automatisch

C1m liefert die kanonische Rekonstruktion

\[
P_{K_R}f=S_RC_R^{-1}S_R^*f.
\]

Für den Standardvektor `f=E_1=\zeta_1` ist der Momentvektor gerade die `1`-te Gramspalte:

\[
m_R(E_1)=C_R e_1
\]

(wenn der neutrale Index `1` mitgeführt wird).

Daher

\[
C_R^{-1}m_R(E_1)=e_1.
\]

Die kanonische Frame-Inversion rekonstruiert also korrekt den **neutralen Ausgangsvektor**; sie erzeugt nicht plötzlich unabhängige Prime-Power-Amplituden.

Damit kann `C_R^{-1}` nicht als versteckter Verstärkungsfaktor benutzt werden, um die fehlende Weilgewichtung rückwärts einzubauen.

---

## 15. Regulator-Dichotomie

Die zwei geprüften natürlichen Regulatoren ergeben:

| Route | Konvergenz | Diagonalgewicht | Problem |
|---|---|---|---|
| BC/KMS `\beta>2` | ja | `\Lambda(n)n^{-\beta/2}` | Singularität bei `\beta=2`; Ziel `\beta=1` nicht erreicht |
| P02-Standardmomente | ja | `\Lambda(n)n^{-3/2}` | um Faktor `1/n` zu klein |
| Rückskalierung der Momente | nein | `\Lambda(n)n^{-1/2}` | exakt C1o-Divergenz |

Daher:

\[
\boxed{
\text{Kein bisheriger source-induzierter Regulator liefert zugleich globale positive Synthesekonvergenz und exakte Weil-Halbgewichte.}
}

Dies ist ein **aktueller Quellenbefund**, kein universeller mathematischer No-Go.

---

## 16. Was als nächstes gesucht werden muss

Der fehlende Mechanismus muss mehr leisten als bloße Dämpfung:

\[
\boxed{
\text{Er muss divergente positive lokale Energie kontrollieren, ohne das endliche kompensierte Weilgewicht zu verändern.}
}
\]

Dafür kommen nach P10 nur strukturelle Wege in Betracht:

1. Quotient/Radikal mit echter source-induzierter Relation;
2. Finite-Part-/Residuenmechanismus mit Operator-/Formbeweis;
3. Schur-/Feshbach-Kompression einer größeren positiven Struktur, ohne die finite Identität als globalen Grenzbeweis zu missbrauchen;
4. ein nichtskaliger labelabhängiger Regulator, der aus BC-/adelischer Geometrie erzwungen wird.

---

## 17. Statusmatrix

| Aussage | Status |
|---|---|
| `C_beta` bounded auf `ell2(P*)` für `beta>2` | `✓[M]` |
| KMS-regulierte positive Synthese für `beta>2` | `✓[M]` |
| normstetiger Grenzübergang durch `beta=2` | `×[M]` |
| direkter KMS-Syntheseweg bis `beta=1` | `×[M]` ohne neue Renormierung |
| Standardmoment-Amplitude `a_n=a/sqrt n` | `✓[M]` |
| momentregulierte globale Synthese konvergiert | `✓[M]` |
| deren Diagonalgewicht = Weil-Halbgewicht | `×[M]` |
| Rückskalierung `sqrt n` stellt Weilgewicht her | `✓[M]` algebraisch |
| rückskalierte Synthese konvergiert | `×[M]` durch C1o |
| Frame-Inversion erzeugt automatisch Prime-Power-Amplituden aus `E1` | `×[M]` |
| strukturelle Renormierung/Quotient | `?[O]` |

---

## 18. Nächster Knoten

\[
\boxed{[P11\text{-}C1q]\quad\text{Quotienten-/Finite-Part-Triage der primspezifischen Restsektoren }K_p^0.}
\]

Zu prüfen ist zuerst, ob die in C1o isolierte Divergenzkomponente

\[
\bigoplus_pK_p^0
\]

eine bereits vorhandene BC-/adelische Radikal- oder Mittelwertrelation besitzt, während der neutrale Hub erhalten bleibt. Falls nein, wird anschließend ein Finite-Part-Synthesemodell formuliert und gegen die P08/P10-Regularisierungsfirewalls geprüft.
