# P11/R32 — unabhängiges Reviewpaket für FG-TR1 Triangular Row Splitting

**Status:** Review-Anforderung; keine Promotion.  
**Zu prüfen:**

- `audits/P11_R32_TRIANGULAR_ROW_SPLITTING_AUDIT.md`
- `audits/P11_R32_FG_EXHAUSTIVITY_CLOSURE.md`
- `consolidation/p11_r32_triangular_row_splitting_verify.py` nur als Algebra-/Arithmetik-Cross-check.

**P11 FROZEN; P12 unverändert; R14 unverändert.**

Das Review soll ausdrücklich adversarial sein. Ein einziges echtes Gegenbeispiel gegen den behaupteten beschränkten Split reicht für `FAIL`.

---

## A. Geometrische Links-/Rechtszerlegung

Prüfen Sie für

\[
a=\tfrac12\log2,
\quad b=\tfrac12\log3,
\quad T=2a,
\quad d=b-a,
\quad e=T-b,
\quad0<R<a
\]

die a.e.-Zerlegung

\[
\mathcal U_R=(a-R,a)\,\dot\cup\,\mathcal V_R,
\qquad
\mathcal V_R=\mathcal U_R\cap(a,T_0).
\]

Insbesondere: Gibt es irgendeinen Branch außer `A_-`/`B_-`, der einen positiven physischen Punkt `<a` treffen kann?

```text
TR-A LEFT/RIGHT SAMPLE SPLIT: GREEN / PARTIAL / FAIL
```

---

## B. Einzige Rückkopplung und Rekursionstiefe

Prüfen Sie exakt

\[
a=d+e,
\qquad d-e=\tfrac12\log(9/8)>0,
\qquad a<2d.
\]

Für `u>d` gilt

\[
b-u=a-(u-d),
\]

also `B_-(u)=A_-(u-d)`. Prüfen Sie dann adversarial die entscheidende Schranke

\[
0<u-d<R-d<a-d=e<d.
\]

Damit soll jede Rückkopplung nach **einem** Schritt in der ersten Schicht landen. Suchen Sie insbesondere nach einem Parameterregime `0<R<a`, in dem eine zweite linke Rekursion dennoch nötig wäre.

```text
TR-B ONE-STEP FEEDBACK: GREEN / PARTIAL / FAIL
```

---

## C. Koeffizienten-Firewall

Der Split löst die Row-Gleichung nach `A_-` auf und benötigt daher `p!=0`.

Prüfen Sie, dass der in der R32-Drei-Shift-Gleichung mit `p` bezeichnete Koeffizient des ersten `2`-Kanals tatsächlich aus dem kanonischen neutralen P11-Hub stammt und nicht verschwindet. Der P11-Hub hat aktive Prime-Power-Gewichte

\[
\sqrt{\log \ell}\,\ell^{-3k/4}>0.
\]

Falls die lokale Notation `p` nicht eindeutig mit diesem nichtverschwindenden Koeffizienten verknüpft ist, markieren Sie diesen Punkt `PARTIAL`, statt die Identifikation stillschweigend anzunehmen.

```text
TR-C NONZERO PIVOT COEFFICIENT: GREEN / PARTIAL / FAIL
```

---

## D. Erste und zweite Rekonstruktionsschicht

Sei

\[
L_R=\Lambda_RJ_R.
\]

Für beliebige

\[
f\in L^2(0,R),
\qquad h\in L^2(\mathcal V_R)
\]

prüfen Sie die Formeln des Audits für `x_0` auf `u<d` und `x_1` auf `u>d` durch direktes Einsetzen in

\[
(L_Rg)(u)
=p[g(a-u)-g(a+u)]
+r[g(b-u)-g(b+u)]
+q[g(T-u)-g(T+u)].
\]

Horizon-Cuts von `B_+` und `C_+` müssen durch die Nullfortsetzung von `h` exakt behandelt werden.

```text
TR-D TWO-LAYER RECONSTRUCTION: GREEN / PARTIAL / FAIL
```

---

## E. Beschränktheit und Bijektivität von Theta_R

Prüfen Sie

\[
\Theta_Rg=(L_Rg,g|_{\mathcal V_R})
\]

als Abbildung

\[
L^2(\mathcal U_R)
\to
L^2(0,R)\oplus L^2(\mathcal V_R).
\]

Zu zeigen:

1. `Theta_R` ist beschränkt.
2. Die Zwei-Schicht-Formeln definieren für jedes `(f,h)` genau ein `g`.
3. `Theta_R^{-1}` ist beschränkt; keine versteckte punktweise Auswertung außerhalb der `L2`-Klasse wird verwendet.
4. Endpunkte/`u=d` sind reine Nullmengen.

```text
TR-E BOUNDED COORDINATE ISOMORPHISM: GREEN / PARTIAL / FAIL
```

---

## F. Rechtsinverse und Split-Surjektivität

Setzen Sie `h=0` und prüfen Sie

\[
(Q_Rf)(a-u)
=
\begin{cases}
f(u)/p,&0<u<\min\{R,d\},\\
f(u)/p-rf(u-d)/p^2,&d<u<R,
\end{cases}
\]

mit `Q_Rf=0` auf `V_R`.

Prüfen Sie exakt

\[
L_RQ_R=I.
\]

```text
TR-F EXPLICIT RIGHT INVERSE: GREEN / PARTIAL / FAIL
```

---

## G. Kernelklassifikation

Aus dem Koordinatenisomorphismus soll folgen

\[
\ker L_R\cong L^2(\mathcal V_R)
\]

und über `J_R`

\[
\mathfrak G_R\cap\ker\Lambda_R
\cong L^2(\mathcal V_R).
\]

Zusammen mit dem separat geschlossenen FGR-F-Schritt:

\[
\mathcal N_I
\cong
\mathcal Z_R^+\oplus L^2(\mathcal V_R).
\]

Suchen Sie ausdrücklich nach einer geglueten Kernel-Familie, die nicht durch eine freie rechte physische Funktion `h` erzeugt wird, oder nach zwei verschiedenen `h`, die dieselbe Kernel-Lösung erzeugen.

```text
TR-G COMPLETE SAMPLED-KERNEL PARAMETRIZATION: GREEN / PARTIAL / FAIL
```

---

## H. Scope-Firewall

Bitte bestätigen oder verwerfen:

- `FG-TR1` ist eine Klassifikation der **lokalen inneren Row-Gleichung**, nicht des vollen augmentierten Blocks.
- Das Resultat macht `N_I` nicht trivial; es zeigt vielmehr explizite freie `L2`-Daten.
- Kein voller Schur-Crossblock, kein Closed-Range-Satz, kein Strong Terminal, kein Objekt X und keine RH-Folge.
- Der strategische Nutzen ist ein Koordinatenwechsel: die zusätzliche Full-Rest-/Schur-Bedingung kann anschließend auf `Z_R^+ \oplus L2(V_R)` gezogen werden.

```text
TR-H SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

---

## Gesamtverdict

```text
TR-A LEFT/RIGHT SAMPLE SPLIT:                  GREEN / PARTIAL / FAIL
TR-B ONE-STEP FEEDBACK:                       GREEN / PARTIAL / FAIL
TR-C NONZERO PIVOT COEFFICIENT:               GREEN / PARTIAL / FAIL
TR-D TWO-LAYER RECONSTRUCTION:                GREEN / PARTIAL / FAIL
TR-E BOUNDED COORDINATE ISOMORPHISM:          GREEN / PARTIAL / FAIL
TR-F EXPLICIT RIGHT INVERSE:                  GREEN / PARTIAL / FAIL
TR-G COMPLETE SAMPLED-KERNEL PARAMETRIZATION: GREEN / PARTIAL / FAIL
TR-H SCOPE FIREWALL:                          GREEN / PARTIAL / FAIL
FG-TR1 OVERALL:                               GREEN / PARTIAL / FAIL
```

Nur bei vollständigem GREEN wäre formal als nächster Schritt eine Promotion von

```text
FG-TR1: ✓[M]
```

überhaupt zulässig. Dieses Reviewpaket selbst promotet nichts.
