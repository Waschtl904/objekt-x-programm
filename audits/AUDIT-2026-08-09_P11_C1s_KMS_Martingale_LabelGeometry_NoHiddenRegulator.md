# P11-C1s — KMS-Martingalgeometrie: GCD-Kern für alle `beta`, aber kein versteckter Hochprimregulator

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1s]`  
**Vorgänger:** P11-C1k, C1p, C1r  
**Primärbasis:** verbindliche BC-Relationen `mu_n^*mu_n=1`, `E_n=mu_nmu_n^*`, BC-Zeitentwicklung; `beta`-KMS-Regime aus P09/NEU-250g  

**Urteil:**

\[
\boxed{[P11-C1s]\quad\checkmark[K/M]_{\rm part}}
\]

Die gesamte in C1k/C1r gefundene GCD-/Martingalgeometrie besitzt eine direkte `beta`-KMS-Verallgemeinerung. Nach Normierung der BC-Rangeprojektionen entsteht exakt

\[
\left(\frac{\gcd(n,m)}{\sqrt{nm}}\right)^\beta.
\]

Dies stärkt die Kanonizität des Labelkerns. Zugleich zeigt die Rechnung, dass der KMS-Abfall **kein zusätzlicher kostenloser Regulator** bei festgehaltener Diagonalnorm ist: Normiert man die Labelvektoren, verschwindet der KMS-Dämpfungsfaktor aus der Diagonale; lässt man sie unnormiert, wird die Prime-Power-Synthese konvergent, aber die Weil-Halbgewichte erhalten zusätzliche Potenzen von `n^{-beta}`.

Damit wird die Konvergenz-versus-Weilgewicht-Dichotomie aus C1p strukturell erklärt.

---

## 1. KMS-Erwartung der BC-Rangeprojektionen

Sei `omega_beta` eine `beta`-KMS-Zustandsfunktion für die BC-Zeitentwicklung im Regime, in dem sie definiert ist. Die BC-Dynamik erfüllt

\[
\sigma_t(\mu_n)=n^{it}\mu_n,
\]

also analytisch

\[
\sigma_{i\beta}(\mu_n)=n^{-\beta}\mu_n.
\]

Mit der KMS-Relation

\[
\omega_\beta(ab)
=\omega_\beta\bigl(b\sigma_{i\beta}(a)\bigr)
\]

für analytische Elemente und

\[
\mu_n^*\mu_n=1
\]

folgt

\[
\begin{aligned}
\omega_\beta(E_n)
&=\omega_\beta(\mu_n\mu_n^*)\\
&=\omega_\beta\bigl(\mu_n^*\sigma_{i\beta}(\mu_n)\bigr)\\
&=n^{-\beta}\omega_\beta(1)\\
&=\boxed{n^{-\beta}}.
\end{aligned}
\]

Status: `✓[M]` im KMS-Scope.

---

## 2. Normierte KMS-Rangevektoren

Auf dem GNS-/Hilbertraum des abelschen Rangeprojektionssektors definiere

\[
\boxed{
\zeta_n^{(\beta)}
:=
n^{\beta/2}E_n.}
\]

Dann

\[
\|\zeta_n^{(\beta)}\|_\beta^2
=n^\beta\omega_\beta(E_n)=1.
\]

Für `n,m` gilt

\[
E_nE_m=E_{\operatorname{lcm}(n,m)}.
\]

Daher

\[
\begin{aligned}
\left\langle
\zeta_n^{(\beta)},
\zeta_m^{(\beta)}
\right\rangle_\beta
&=(nm)^{\beta/2}
\omega_\beta(E_{\operatorname{lcm}(n,m)})\\
&=(nm)^{\beta/2}
\operatorname{lcm}(n,m)^{-\beta}\\
&=\boxed{
\left(
\frac{\gcd(n,m)}{\sqrt{nm}}
\right)^\beta.}
\end{aligned}
\]

Dies ist exakt der C1k-Common-Multiple-Kern.

Status: `✓[K/M]`.

---

## 3. C1k besitzt damit zwei BC-interne Realisierungen

Für `\beta>1`:

\[
\boxed{
\text{KMS-Rangeprojektions-Gram}
=
\text{Common-Multiple-Dirichlet-Gram aus C1k}.}
\]

Am kritischen Kernelparameter `\beta\downarrow1` erhält man

\[
\frac{\gcd(n,m)}{\sqrt{nm}},
\]

also den C1k2-Haar-/Rangeprojektionskern.

**Firewall:** Für den vorliegenden Schluss genügt die endliche Gramkernel-Grenze. Es wird kein starker GNS-Raumgrenzwert `\beta\downarrow1` behauptet.

---

## 4. KMS-Martingaldifferenzen

Fixiere eine Primzahl `p` und definiere

\[
\boxed{
d_{p,j}^{(\beta)}
:=
E_{p^{j+1}}-p^{-\beta}E_{p^j}.}
\]

Dann

\[
\omega_\beta(d_{p,j}^{(\beta)})
=p^{-\beta(j+1)}-p^{-\beta}p^{-\beta j}=0.
\]

Für `j<k` liefert dieselbe Verschachtelungsrechnung wie in C1r

\[
\boxed{
\langle d_{p,j}^{(\beta)},d_{p,k}^{(\beta)}\rangle_\beta=0.}
\]

Die Norm ist

\[
\boxed{
\|d_{p,j}^{(\beta)}\|_\beta^2
=p^{-\beta(j+1)}(1-p^{-\beta}).}
\]

Daher bilden die normierten

\[
\boxed{
\psi_{p,j}^{(\beta)}
:=
\frac{p^{\beta(j+1)/2}}
{\sqrt{1-p^{-\beta}}}
\left(E_{p^{j+1}}-p^{-\beta}E_{p^j}\right)
}
\]

eine kanonische ON-Familie des `beta`-zentrierten p-adischen Restsektors.

Für `\beta=1` reduziert dies formal exakt auf die Haar-Martingalstruktur aus C1r.

---

## 5. Sternzerlegung für alle `beta`

Da

\[
\langle\zeta_1^{(\beta)},\zeta_n^{(\beta)}\rangle_\beta=n^{-\beta/2},
\]

definiere

\[
\eta_n^{(\beta)}
:=
\zeta_n^{(\beta)}-n^{-\beta/2}\zeta_1^{(\beta)}.
\]

Für teilerfremde `n,m` gilt

\[
\langle\eta_n^{(\beta)},\eta_m^{(\beta)}\rangle_\beta=0.
\]

Insbesondere für verschiedene Primzahlen:

\[
\boxed{K_{p,\beta}^0\perp K_{q,\beta}^0.}
\]

Für das erste Primlabel:

\[
\boxed{
\|\eta_p^{(\beta)}\|_\beta^2
=1-p^{-\beta}.}
\]

Damit bleibt die erste primspezifische Restnorm für große `p` nahe `1`.

---

## 6. Kein versteckter KMS-Abfall nach Normierung

Nehme den **exakten Weil-Lokalgewichtsfaktor** im primitiven Kanal

\[
w_p=\frac{\log p}{\sqrt p}.
\]

Kombiniert man ihn mit dem **normierten** KMS-Labelvektor `\zeta_p^{(\beta)}`, so ist der Diagonal-Labelnormfaktor weiterhin

\[
\|\zeta_p^{(\beta)}\|_\beta^2=1.
\]

Der primspezifische Rest trägt asymptotisch

\[
1-p^{-\beta}\to1.
\]

Damit bleibt der C1o-Hochprimmaßstab

\[
\boxed{\frac{\log p}{\sqrt p}}
\]

unverändert.

Folglich:

\[
\boxed{
\text{KMS-Geometrie + normierte Labels}
\not\Rightarrow
\text{zusätzliche Hochprimdämpfung}.}
\]

Status: `✓[M]`.

---

## 7. Unnormierte Rangeprojektionen liefern Dämpfung — aber ändern das Zielgewicht

Verwendet man stattdessen `E_n` selbst, gilt

\[
\|E_n\|_\beta^2=n^{-\beta}.
\]

Ein analytischer Prime-Power-Kanal mit Weilgewicht

\[
w_n=\frac{\Lambda(n)}{\sqrt n}
\]

und unnormiertem Labelvektor `E_n` erhält diagonal daher effektiv

\[
\boxed{
w_n\|E_n\|_\beta^2
=
\frac{\Lambda(n)}{n^{\beta+1/2}}.}
\]

Für `\beta>1` ist dies stark summierbar.

Aber es ist **nicht** das Weil-Halbgewicht.

Am formalen `\beta=1`-Punkt entsteht

\[
\boxed{\frac{\Lambda(n)}{n^{3/2}},}
\]

also genau die zusätzliche `n^{-1}`-Dämpfung aus C1p/C1q.

---

## 8. Normierung zurück auf Diagonale 1 stellt die Divergenz wieder her

Um aus `E_n` wieder einen Labelvektor der Norm `1` zu machen, muss man mit

\[
n^{\beta/2}
\]

multiplizieren:

\[
\zeta_n^{(\beta)}=n^{\beta/2}E_n.
\]

Genau dadurch verschwindet die KMS-Dämpfung `n^{-\beta}` aus dem quadratischen Diagonalgewicht.

Damit ist die Dichotomie algebraisch exakt:

\[
\boxed{
\text{KMS-Dämpfung behalten}
\Longleftrightarrow
\text{Diagonalgewicht ändern};
}
\]

\[
\boxed{
\text{Diagonalnorm auf 1 normalisieren}
\Longleftrightarrow
\text{KMS-Dämpfung entfernen}.}
\]

Es gibt in dieser Rangeprojektionsnormierung keinen dritten versteckten Faktor.

---

## 9. Verbindung zu C1p

C1p formulierte einen regulierten Synthesepfad mit

\[
w_n^{(\beta)}=\Lambda(n)n^{-\beta/2}
\]

und dem normierten Labelkernel `c_\beta`.

C1s zeigt jetzt, dass diese Wahl nicht aus einer zusätzlichen Normdämpfung der normierten Labelvektoren kommt. Sie ist eine **separate analytische/arithmetische Gewichtung**.

Die positive Synthese konvergiert dort für `\beta>2`, stößt aber bei `\beta=2` auf die Primzahlsingularität.

Damit bleiben C1p und C1s vollständig konsistent.

---

## 10. Cross-prime-Regulatorfrage ist nicht durch KMS-Labelnorm gelöst

Die p-adische Exponentstruktur und die `beta`-KMS-Norm sind jetzt kanonisch bestimmt.

Aber für die Hochprimrichtung gilt:

\[
\boxed{
\text{KMS-Normierung allein kontrolliert die C1o-Restenergie nicht bei festgehaltenen Weilgewichten.}
}
\]

Ein erfolgreicher Regulator muss daher außerhalb der bloßen normierten Rangeprojektions-Geometrie liegen, etwa in

- einer source-induzierten Quellamplitude;
- einer echten relativen/quotientierten Form;
- einer Operator-Finite-Part-Struktur;
- oder einer nichttrivialen Kompression einer größeren positiven Geometrie.

---

## 11. Statusmatrix

| Aussage | Status |
|---|---|
| `omega_beta(E_n)=n^{-beta}` im KMS-Scope | `✓[M]` |
| normierter KMS-Range-Gram = `(gcd/sqrt(nm))^beta` | `✓[K/M]` |
| C1k Common-Multiple-Kern = KMS-Range-Gram | `✓[K/M]` |
| kanonische `beta`-Martingaldifferenzen | `✓[K/M]` |
| normierte KMS-Labels liefern zusätzliche p-Dämpfung | `×[M]` |
| unnormierte `E_n` liefern p-Dämpfung | `✓[M]` |
| diese Dämpfung erhält Weil-Halbgewicht | `×[M]` |
| Normierung auf Labelnorm 1 entfernt Dämpfung | `✓[M]` |
| KMS-Labelnorm allein löst C1o | `×[M]` Kandidaten-No-Go |
| anderer source-induzierter cross-prime-Regulator | `?[O]` |

---

## 12. Wichtigster Befund

Die BC-GCD-Geometrie ist jetzt auf drei Ebenen vereinheitlicht:

\[
\boxed{
\text{Haar }(\beta=1)
\;\leftrightarrow\;
\text{KMS }(\beta>1)
\;\leftrightarrow\;
\text{Common-Multiple-Dirichletkern}.}
\]

Damit ist ihre Kanonizität deutlich stärker als zu Beginn von P11.

Gleichzeitig ist ausgeschlossen, dass die fehlende globale Synthesekonvergenz nur durch „die richtige KMS-Norm“ trivial verschwindet.

---

## 13. Nächster Knoten

Der verbleibende P11-C1-Strang hat nun einen klaren Engpass:

\[
\boxed{[P11\text{-}C1t]\quad\text{Triage der möglichen relativen/Finite-Part-Kompression nach C1o–C1s}.}
\]

Vor einer neuen Konstruktion soll geprüft werden, welche der bereits in P08/P10 eingefrorenen Regularisierungsfirewalls einen solchen Pfad sperren und welcher Resttyp überhaupt noch zulässig ist.
