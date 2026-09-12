# P11 / Objekt X — Gate 2, OX-GRAM-Abschluss und OX-GEN-Neufront

> **Rolle:** Konsolidierender Gegencheck zum externen Gate-2-Bericht vom 12.09.2026.
> **Basis:** Branch `research/ox-gram-ar1-consolidation-2026-09-12`, ausgehend von `main` `77f47ec32787d5d8f2c8106c97b611650d44b9ff`.
> **Kein Registry-Eintrag, kein Merge-Anspruch, kein RH-Resultat.**

## 0. Kurzurteil

Der Gate-2-Lauf liefert starke endliche Evidenz und eine sinnvolle Frontkorrektur, ist in der übergebenen Fassung aber noch **nicht vollständig interval-zertifiziert**.

Belastbar und für die Forschungsfront wesentlich sind:

1. die berichtete 512-Bit-Arb-Cholesky-Rechnung findet in allen getesteten Unterräumen positive Pivots und keinen numerischen Gegenvektor;
2. die Existenzfrage `N_a <= G_a^+` ist als Objekt-X-Kriterium **vakuant**, sobald die lokale Weil-Positivität vorausgesetzt/anderweitig bekannt ist, weil ein Kontraktor rückwärts aus `Q=G_a^+-N_a` konstruiert werden kann;
3. die nichtzirkuläre Frage ist deshalb **Kanonizität**, nicht Existenz;
4. die exakte Rang-2-Struktur von Suzukis `r_0''` isoliert mit `e^{+x/2},e^{-x/2}` erstmals einen expliziten Generator, der zugleich mit der Prime-Normalisierung `p^{-1/2}=e^{-\log p/2}` verwandt ist;
5. daraus entsteht die neue Hauptfrage **OX-GEN**.

Vor einem Merge bleibt jedoch `CERT-HARDEN` offen; die Gründe stehen in §2.

---

## 1. Gate-2-Rechnung: was tatsächlich vorliegt

Der externe Lauf verwendet die Dirichletbasis

```math
\varphi_m(x)=\sin\!\left(\frac{m\pi(x+a)}{2a}\right),
\qquad m=1,\ldots,14,
```

mit `ctx.prec=512` und testet die geraden/ungeraden Paritätsblöcke getrennt.

Für

```math
Q=G_a^+-N_a
```

wird blockweise eine Arb-Cholesky-Zerlegung akzeptiert, wenn jede berechnete Pivot-Untergrenze strikt positiv ist.

Die übergebene Ausgabe meldet:

- `a=0.5`: 14 verschachtelte Paritätsblöcke, alle `Q>0 ZERTIFIZIERT`;
- `a=0.8`: 14 verschachtelte Paritätsblöcke, alle `Q>0 ZERTIFIZIERT`;
- `a=1.0`: 14 verschachtelte Paritätsblöcke, alle `Q>0 ZERTIFIZIERT`;
- insgesamt 42/42 positive endliche Tests;
- maximale ausgegebene Ballradien der `Q`-Einträge etwa `5.4e-26`, `2.1e-26`, `1.3e-26`.

Die kleinsten aus Mittelpunkten berechneten generalisierten Ritzwerte `nu_min` fallen bei `a=0.8,1.0` stark mit der Basisdimension; bei `a=0.5` zeigt die endliche Basis ein deutliches Abflachen.

**Firewall:** Die `mpmath`-Eigenwerte/Ritzvektoren sind Diagnostik. Der rigorose Teil ist nur die Arb-Einschließung der Matrixeinträge plus Cholesky, sofern die Matrixeinträge selbst die vollständigen mathematischen Terme einschließen.

---

## 2. Offene Zertifikationslücken im übergebenen Skript

### 2.1 Bernoulli-Tail von `r_1''`

Das Skript setzt

```text
NB = 340
```

und integriert die Partialsumme

```math
\sum_{n=1}^{340}
\frac{B_n(1/4)(-2)^n}{2n!}u^{n-1},
```

ohne den Rest `n>340` explizit als Arb-Ball zu addieren. `acb.integral` zertifiziert deshalb nur die **abgeschnittene** Reihe.

Die Lücke ist quantitativ winzig, aber formal real. Für `n>=2` gilt aus der Fourierdarstellung der Bernoulli-Polynome

```math
|B_n(1/4)|\le \frac{2n!\,\zeta(n)}{(2\pi)^n}.
```

Für `|u|<=2` folgt für den Supremumsrest nach `N`:

```math
|R_N(u)|
\le \frac{\zeta(2)}2
\frac{(2/\pi)^{N+1}}{1-2/\pi}.
```

Bei `N=340` liegt dies bei etwa `3.1e-67`. Für `a<=1` liefert die grobe Schranke
`|SHp+SHm|<=4a` und Integrationslänge `2a` einen gesamten `R1`-Formfehler von höchstens etwa `8*3.1e-67` pro normierter Basisprodukt-Hülle. Damit ist die Lücke praktisch harmlos, muss aber für ein formales Zertifikat in die Bälle eingebaut werden.

Alternativ lässt sich die Reihe aus der Bernoulli-Erzeugenden geschlossen summieren:

```math
\boxed{
r_1''(u)=\frac{e^{u/2}}{2\sinh u}-\frac1{2u},
\qquad r_1''(0)=\frac14.}
```

Diese Form ist für die Härtung vorzuziehen, sofern die hebbare Singularität rigoros behandelt wird.

### 2.2 Prime-Power-Cutoff

Der Cutoff wird über

```python
vm_upto(float((2*a).exp()))
```

bestimmt. Für die drei getesteten Radien liegt `e^(2a)` weit von der nächsten ganzen Zahl entfernt; die konkrete Kanalliste ist daher faktisch eindeutig. Für ein Repo-Zertifikat ist die Entscheidung dennoch mit Arb-Vergleichen `n < exp(2a)` zu treffen und bei einem nicht auflösbaren Grenzfall abzubrechen.

### 2.3 Log-Randfehler in `Mterm`

Die Endpunktfehlerabschätzung enthält

```python
abs(float((2*a*e).log())) + 1
```

in einer sonst rigorosen Arb-Schranke. Eine Float-Rundung darf nicht als obere Intervallschranke dienen. Der Faktor ist vollständig in Arb zu berechnen, z.B. über eine bewiesene positive obere Schranke für `-log(2*a*e)+1`.

### 2.4 Cholesky

Die Cholesky-Logik ist konzeptionell richtig: ein Block wird nur akzeptiert, wenn jeder Pivot strikt positiv eingeschlossen ist. Für die Härtung sollte der Positivitätstest direkt als Arb-Intervallvergleich `s>0` formuliert werden, statt eine manuell aus `mid-rad` rekonstruierte Untergrenze als logische Quelle zu verwenden.

**Status:** Die Gate-2-Ausgabe ist starke Evidenz; die Bezeichnung `Arb-Cholesky-zertifiziert 42/42` wird im Repo erst nach einem gehärteten Rerun verwendet.

---

## 3. Warum die bisherige OX-GRAM-Existenzfrage geschlossen wird

Auf einem positiven Formraum sei

```math
Q=G_a^+-N_a.
```

Wenn `G_a^+>0` und `Q>=0`, dann ist

```math
0\le (G_a^+)^{-1/2}N_a(G_a^+)^{-1/2}\le I.
```

Damit existiert formal ein Kontraktor durch

```math
W_a^*W_a=(G_a^+)^{-1/2}N_a(G_a^+)^{-1/2}
       =I-(G_a^+)^{-1/2}Q(G_a^+)^{-1/2}.
```

Diese Konstruktion verwendet jedoch genau die zu erklärende Weilform `Q`; sie ist daher für Objekt X **zirkulär**.

Folglich ist

```text
"Existiert irgendein kontraktives W_a?"
```

kein sinnvoller Objekt-X-Gate, solange Positivität im betrachteten Bereich bereits bekannt ist. Ein PASS beweist keinen neuen Mechanismus; ein FAIL wäre ein Negativvektor der Weilform und damit weit mehr als ein Architekturtest.

**Buchung:** Die Front `N_a <= G_a^+ ?` wird als Objekt-X-Konstruktionsfrage geschlossen. Übrig bleibt die nichtzirkuläre Frage nach einem **kanonisch aus den Prim-/archimedischen Generatoren gebauten** Intertwiner.

---

## 4. Exakter Fund: Rang-2-Struktur von `R_0`

Suzukis Kernteil erfüllt

```math
r_0''(t)=-2\cosh(t/2).
```

Mit

```math
\cosh\frac{x-y}{2}
=\cosh\frac x2\cosh\frac y2
 -\sinh\frac x2\sinh\frac y2
```

folgt für reelles `v`

```math
\boxed{
R_0(v,v)
=-2\left(\int\cosh\frac x2\,v(x)\,dx\right)^2
+2\left(\int\sinh\frac x2\,v(x)\,dx\right)^2.}
```

Damit ist `R_0` auf dem ganzen Fenster höchstens Rang 2.

- im **geraden** Sektor verschwindet das `sinh`-Moment: `R_0<=0`, dort Rang höchstens 1 negativ;
- im **ungeraden** Sektor verschwindet das `cosh`-Moment: `R_0>=0`, dort Rang höchstens 1 positiv.

Diese Struktur ist exakt und unabhängig von numerischen Extremalvektoren.

---

## 5. Neue Hauptfrage OX-GEN

Die exponentielle Familie

```math
e^{\pm x/2}
```

erscheint gleichzeitig in zwei bisher getrennten Teilen der Architektur:

1. `R_0` wird aus `cosh(x/2),sinh(x/2)` und damit `e^{\pm x/2}` erzeugt;
2. die Prime-Normalisierung verwendet

```math
p^{-1/2}=e^{-(\log p)/2},
```

und daraus sowohl

```math
R_p(j,k)=p^{-|j-k|/2}
```

als auch die Weilgewichte

```math
w_{p,k}=\log p\,p^{-k/2}.
```

Daraus entsteht eine nichtzirkuläre, beidseitig falsifizierbare Forschungsfrage:

> **OX-GEN.** Ist der Rang-2-Defekt `R_0` als Rand-/Defektterm derselben Exponentialstruktur darstellbar, die die Prime-Power-Kanäle normiert? Gibt es eine explizit aus `{e^{+x/2},e^{-x/2},K_n, logarithmischer Douglas-Geometrie}` gebaute Abbildung, die insbesondere
>
> ```math
> \left(\int\cosh\frac x2\,v\right)^2
> ```
>
> im geraden Sektor als intrinsischen Defekt der Prime-/archimedischen Featuregeometrie erzeugt, ohne `Q_{B_a}`, ohne `B_a^{1/2}`, ohne `lambda_a` und ohne RH zu verwenden?

Eine positive Antwort konstruiert einen expliziten Teil einer gemeinsamen Geometrie. Eine negative Antwort, sofern sie eine natürlich definierte Generator-Klasse ausschließt, verkleinert die Gussform.

**Scope:** `R_1` und der Skalar `c_aI` bleiben dabei offen; OX-GEN ist ein Teilproblem, kein vollständiger Objekt-X-Ansatz.

---

## 6. Rolle der Extremalrichtungen

Der externe Lauf zerlegt numerisch die Ritz-Extremalrichtung termweise. Bei `a=1`, gerader Sektor, ergibt sich ungefähr

```text
Douglas/4         +1.059612079304
Prime-Gram        +5.758791640483
Log-Multiplikator +0.013855959762
G_a^+             +6.832259679549
c_a ||v||^2       +8.267561095664
R_0                -1.629811797805
R_1                +0.194510381690
N_a               +6.832259679549
Q                  +4.5e-17
```

Diese nahezu vollständige Kürzung entsteht erst aus allen Blöcken; `Prime-Gram - A_a||v||^2` allein erklärt sie nicht.

**Firewall:** Bei `a>=0.8` fallen die Ritzwerte bis zur maximalen getesteten Dimension weiter stark; der Ritzvektor ist dort trunkierungsabhängig. Strukturelle Experimente sollen deshalb zunächst bei `a=0.5` erfolgen, wo die endliche Basis eine deutlich stabilere Richtung zeigt.

Eine beobachtete Koeffizientenratio nahe `0.603` wird ausdrücklich **nicht** gedeutet; sie ist radius-/sektorabhängig und fällt unter die Anti-Fitting-Regel.

---

## 7. Spurtrennung

### Spur A — Objekt X

Nur OX-GEN plus die dafür tatsächlich nötige Zertifikationshärtung.

Nächste Reihenfolge:

1. `CERT-HARDEN`: Gate 1/2 mit Bernoulli-Rest oder geschlossener `r_1''`-Form, Arb-sicherem Prime-Power-Cutoff und reinem Arb-Randfehler rerunnen;
2. `OX-GEN-A`: bei `a=0.5` die exakten `cosh/sinh`-Momentfunktionale in der Prime-/Douglas-Featureabbildung isolieren;
3. vorab eine natürliche Generator-Klasse definieren, damit ein negatives Ergebnis tatsächlich eine Architekturklasse ausschließt;
4. erst danach nach einem expliziten Intertwiner suchen.

Keine weiteren `mu_max`-Dimensionssweeps als Hauptfront: sie messen ohne neuen Mechanismus nur lokale Weil-Positivität.

### Spur B — eigenständige Mathematik

Prime-Power-AR(1)/Martingal-Faktorisierung separat theorem-ready verschriftlichen:

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}\,p^{-|j-k|/2},
\qquad
T_q^*T_q+uu^*=R_q.
```

Fensterfrei, exakt, RH-unabhängig und ausdrücklich **nicht** als Objekt X vermarkten. Der bisherige Literaturbefund ist nur Neuheitsindikator, kein Prioritätsbeweis.

---

## 8. Methodische Regel für künftige Gates

Ein Falsifikationsgate zählt nur dann als echte Verengung der Gussform, wenn **beide Ausgänge vorab logisch möglich** sind.

Ein Test, dessen negativer Ausgang bereits durch einen bekannten Positivitätssatz ausgeschlossen ist, kann zwar Implementierungsfehler oder Normalisierungsprobleme finden, aber keine Architekturklasse eliminieren.

---

## 9. Status

```text
Gate 1 Normalisierung               stark GREEN; vollständige Härtung OPEN
Gate 2 endliche Positivität         starke 512-Bit-Arb-Evidenz; formaler Repo-Freeze OPEN
OX-GRAM Existenzfrage               geschlossen/vakuant als Objekt-X-Gate
R_0 Rang-2-Paritätszerlegung        ✓[M] exakt
OX-GEN                              ?[O] neue Spur-A-Hauptfrage
AR(1)/Martingal-Faktorisierung      ✓[M] Spur B / theorem-ready
Objekt X                            ?[O]
RH                                  ?[O]
```

Kein Registry-Update und kein Merge aus diesem Dokument allein.
