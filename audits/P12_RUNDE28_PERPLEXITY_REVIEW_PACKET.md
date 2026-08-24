# P12 Runde 28 — unabhängiges Review-Paket

**Status:** Review-Anforderung; **keine Promotion**.  
**Repo:** `Waschtl904/objekt-x-programm`, Branch `main`.  
**Kandidatenkette:**

- `1caebfb27f8f56894ac9773de1650f3582763444` — `audits/P12_RUNDE28_NEXT_SHELL_HORIZON_AUDIT.md`
- `a2bfb7869c4d20f576890c6073d787470d39872e` — `consolidation/round28_next_shell_horizon_verify.py`

**Zu prüfender Kandidat:** R28-A, zentrale Next-Shell-Doppelhorizont-Kammer mit 68×68-Rohblock.  
**Firewall:** P11 FROZEN; R14 unverändert; kein globaler `rho`-Descent und keine Objekt-X-/RH-Aussage.

---

## 1. Review-Auftrag

Bitte **nicht** lediglich den retained verifier ausführen und dessen `PASS` übernehmen. Die Kernassertions sollen unabhängig aus dem kanonischen Rohoperator

\[
Lh(u)=p[h(u-a)-h(u+a)]
+r[h(u-b)-h(u+b)]
+q[h(u-T)-h(u+T)]
\]

mit odd reflection sowie Support-/Horizon-Cutoffs rekonstruiert werden.

Ziel ist ein adversariales Urteil, ob R28-A als lokaler `✓[M]_part`-Mechanismus promotionsfähig ist.

---

## 2. Exakte Box B28 unabhängig prüfen

Mit

\[
\eta=e-2\delta,\quad
\chi=3\delta-e,\quad
\kappa=e-\delta,\quad
E=\varepsilon_{\max},\quad
\rho=E-\delta
\]

ist

\[
\frac{19}{2000}<R<\frac{21}{2000},
\]

\[
\left|x-\frac\delta2\right|<\frac1{5000},
\]

\[
\frac{119}{2000}<\sigma<\frac{121}{2000},
\]

\[
\frac{139}{2000}<\varepsilon<\frac{141}{2000}.
\]

Bitte mit eigenen rigorosen Schranken bestätigen:

1. `B28` liegt vollständig in `0<R<rho`, `R<sigma<epsilon<E` und `R<x`;
2. beide ersten Supportvariablen sind live:
   \[
   \sigma+x>\kappa,\qquad \sigma-x>\eta;
   \]
3. beide natürlichen Next-Shell-Quellen sind horizon-illegal:
   \[
   \varepsilon+x<2\delta,\qquad \varepsilon-x<\delta;
   \]
4. auf `B28` gilt `sigma>2 eta`;
5. daraus folgt tatsächlich die behauptete Trennung von den promovierten C42-, C44-, C26- und W43-Kammern.

Insbesondere bitte prüfen, dass hier nicht versehentlich bereits ein früherer lokaler Mechanismus greift.

---

## 3. Ausgangsdefekt 42×44 unabhängig rekonstruieren

Aus den 42 alten Round-23/C42-Quellen soll auf einem inneren Referenzpunkt und anschließend über die ganze Box rekonstruiert werden:

\[
42\text{ horizon-legale Zeilen},\qquad 44\text{ sichtbare Variablen}.
\]

Die zwei zusätzlichen sichtbaren Variablen müssen genau

\[
U_-=(-1,5,1),\qquad U_+=(1,5,0)
\]

sein.

Die Quellen

\[
V_-=(-1,4,4),\qquad V_+=(1,4,3)
\]

müssen auf `B28` tatsächlich über dem Horizont liegen und dürfen nicht als verfügbare Zusatzzeilen verwendet werden.

---

## 4. 68-Quellen-Kreis unabhängig rekonstruieren

Zu den 42 alten Quellen verwendet der Kandidat folgende 26 zusätzlichen Quellen:

```text
(-1,-1,3), (-1,0,3), (-1,0,4), (-1,1,-1), (-1,1,4),
(-1,2,-2), (-1,2,-1), (-1,2,5), (-1,3,-1), (-1,3,5),
(-1,3,6), (-1,4,-1), (-1,5,0),
( 1,-1,2), ( 1,0,2), ( 1,0,3), ( 1,1,-2), ( 1,1,3),
( 1,2,-3), ( 1,2,-2), ( 1,2,4), ( 1,3,-2), ( 1,3,4),
( 1,3,5), ( 1,4,-2), ( 1,5,-1).
```

Bitte unabhängig bestätigen:

1. genau 68 verschiedene Quellen;
2. vollständige `J`-Abgeschlossenheit unter
   \[
   J(s,m,n)=(-s,m,n+s);
   \]
3. alle 68 Quellen sind auf `B28` horizon-legal;
4. die rekonstruierten Rohzeilen erzeugen genau 68 sichtbare Variablen;
5. auch die Variablenmenge ist `J`-abgeschlossen;
6. `h(x)` und `h(delta-x)` gehören tatsächlich zu dieser Variablenmenge;
7. der resultierende Koeffizientenblock ist exakt 68×68.

Es wird **keine Minimalität** der 68 Quellen behauptet; bitte keine solche Aussage in das Review hineinlesen.

---

## 5. Vollständiges Raw-Pattern-Zertifikat adversarial prüfen

Der retained verifier erzeugt aus den 68 Quellen insgesamt

\[
\boxed{1204}
\]

Source-/Sign-/Support-/Horizon-Ungleichungen und zertifiziert sie über der gesamten Box.

Bitte diese Zahl und die Konstruktion unabhängig reproduzieren. Besonders zu prüfen:

- Source lower / upper für jede Quelle;
- Vorzeichen sämtlicher sechs Shift-Slots;
- korrekte odd reflection;
- korrekte Unterscheidung live / dead-lower / dead-upper;
- korrekte obere Supportgrenze `T+sigma`;
- korrekte Source-Horizongrenze `T+epsilon`.

Bitte nicht nur Ecken sampeln, sondern eine rigorose affine Boxabschätzung oder eine äquivalente exakte Polyederprüfung verwenden.

Der retained Wert für die kleinste positive Rohmarge ist

\[
>0.00157927617278058.
\]

Bitte unabhängig prüfen, ob alle 1204 Bedingungen strikt bleiben und ob keine verborgene Pattern-Wand die Box schneidet.

---

## 6. J-Blockstruktur unabhängig prüfen

In natürlicher `J`-Ordnung wird behauptet

\[
M_{68}
=
\begin{pmatrix}
A_{34}&B_{34}\\
B_{34}&A_{34}
\end{pmatrix}.
\]

Bitte coefficient-for-coefficient rekonstruieren und anschließend die exakte Blockdiagonalisierung

\[
Q^{-1}M_{68}Q
=
\operatorname{diag}(A_{34}+B_{34},A_{34}-B_{34})
\]

prüfen.

---

## 7. Determinantenrechnung vollständig unabhängig wiederholen

Der Kandidat behauptet

\[
\det(A_{34}+B_{34})=-p^{12}qr^8F_+(p,q,r),
\]

\[
\det(A_{34}-B_{34})= p^{12}qr^8F_-(p,q,r),
\]

mit homogenen Grad-13-Polynomen und

\[
F_-(p,q,r)=F_+(p,-q,r).
\]

Mit

\[
\beta=q/p=2^{-3/4},
\qquad
v=(r/p)^2=\frac{\log3}{\log2}\sqrt{\frac8{27}}
\]

sollen die normierten Faktoren

\[
G_-(\beta,v)=G_+(-\beta,v)
\]

erfüllen.

Bitte die Polynome aus der Matrix **neu berechnen**, nicht aus dem Audit kopieren, und mit eigenen gerichteten rationalen Intervallen prüfen.

Retained Zielintervalle:

\[
0.3822065426030501
< G_+(\beta,v)
<0.38220654260305015,
\]

\[
0.20288790549604774
< G_-(\beta,v)
<0.20288790549604777.
\]

Daraus soll folgen

\[
\det M_{68}
=-p^{68}\beta^2v^8G_+G_-\ne0.
\]

Bitte insbesondere Vorzeichen, Exponenten und die Beziehung zwischen den beiden Paritätsfaktoren unabhängig kontrollieren.

---

## 8. Gewünschtes Verdict

Bitte am Ende getrennt ausgeben:

```text
R28-A BOX / GAP ORIENTATION: GREEN / PARTIAL / FAIL
R28-A 68x68 RAW PATTERN:    GREEN / PARTIAL / FAIL
R28-A J-BLOCK:              GREEN / PARTIAL / FAIL
R28-A NONDEGENERACY:        GREEN / PARTIAL / FAIL
R28-A OVERALL:              GREEN / PARTIAL / FAIL
```

Bei `PARTIAL` oder `FAIL` bitte die **erste konkrete mathematische Stelle** nennen, an der die Rekonstruktion vom Kandidaten abweicht.

---

## 9. Erlaubte Aussage bei vollständig unabhängigem GREEN

Bei vollständigem GREEN darf formal gesagt werden:

> Auf der exakten `J`-symmetrischen Box `B28` innerhalb der zentralen Next-Shell-Doppelhorizont-Lücke rekonstruiert der kanonische Rohoperator einen konstanten, invertierbaren 68×68-Block. Daher gilt dort lokal `h(x)=h(delta-x)=0`. Dies ist ein lokaler `✓[M]_part`-Mechanismus.

Nicht erlaubt sind daraus folgende stärkere Formulierungen:

- vollständige Schließung der gesamten Next-Shell-Horizon-Lücke;
- Schließung der einseitigen Zellen mit genau einem legalen `V`;
- globaler `rho`-Descent;
- neue globale Radius-Schwelle;
- Minimalität oder kanonische Bedeutung von 68 bzw. einer Suchgittertiefe;
- P11-/R14-Konsequenzen;
- Polar Gauge, Strong/Terminal Transport, Objekt X oder RH.

**Promotion ausschließlich nach unabhängigem GREEN.**
