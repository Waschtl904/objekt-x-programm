# P11 Audit — exact COMMON-JUMP / source-conditioned Tree bridge

**Datum:** 15. September 2026  
**Basis:** P11 source-first finite-window geometry, Critical-half Green/tree audit, COMMON-JUMP ledger.  
**Rolle:** typkorrekte Identifikation der raeumlichen P11-Hub-/Restfeatures mit Weil-normalisierten Jump-Kanaelen.  
**Registry:** unveraendert.  
**Nonclaim:** kein globales Object X, kein NP-GAP-/RH-Beweis, keine Publikationsneuheit.

---

## 0. Kurzurteil

Die bisher getrennt behandelten Strukturen sind auf der **Feature-Ebene bereits exakt verbunden**.

Fuer

```math
w_{p,k}=(\log p)p^{-k/2},
\qquad
t_{p,k}=k\log p,
```

definiere den quellbeschraenkten Weil-normalisierten Jump-Kanal

```math
\boxed{
X_{p,k,R}f(u)
:=\sqrt{w_{p,k}}\,D_{t_{p,k}}E_Rf(u),
\qquad u\in(-R,R).
}
```

Dann ist der originale P11-Huboperator exakt

```math
\boxed{
H_Rf
=\sum_{p^k\le e^{2R}}p^{-k/2}X_{p,k,R}f.
}
```

Der Faktor `p^{-k/2}` ist also nicht nur eine Kanalindex-Korrelation: er ist das **raeumliche Root-Funktional auf denselben Jump-Features**.

Noch staerker: Die source-dependent Martingalprojektion `Q_R(u)` interpoliert auf jedem Prime-Ast exakt zwischen

```text
voller AR(1)-/OU-Kovarianz im zweiseitigen Innenbereich
```

und

```text
reinem gemeinsamen Root-Gram am Rand.
```

Die Interpolationstiefe ist genau die Anzahl der symmetrischen Prime-Power-Shifts, deren beide Endpunkte im Quellfenster liegen.

Status:

```text
spatial P11 hub = root functional of Jump features             ✓[M]
source depth J = exact two-sided overlap depth                  ✓[M]
closed source-conditioned same-prime Gram formula               ✓[M]
full AR(1) recovered on full-overlap pairs                      ✓[M]
root-only rank-one degeneration at J=0                          ✓[M]
windowless Tree Gram has universal lower frame c0=3-2sqrt(2)    ✓[M]
that pointwise lower frame survives source conditioning          ×[M]
canonical global whitening compatible with source conditioning   ?[O]
forward Feshbach/Shorting identification with Weil form          ?[O]
```

---

# 1. Die raeumlichen P11-Features sind Weil-normalisierte Jumps

P11 verwendet

```math
D_s=U_{s/2}-U_{-s/2}.
```

Der originale Hub ist

```math
H_R
=P_R\sum_{p^k\le e^{2R}}
\sqrt{\log p}\,p^{-3k/4}D_{k\log p}E_R.
```

Da

```math
\sqrt{w_{p,k}}
=\sqrt{\log p}\,p^{-k/4},
```

folgt fuer `q_p=p^{-1/2}`

```math
\sqrt{\log p}\,p^{-3k/4}
=q_p^k\sqrt{w_{p,k}}.
```

Also exakt

```math
\boxed{
H_Rf(u)
=\sum_{p^k\le e^{2R}}
q_p^k X_{p,k,R}f(u).
}
```

Dies ist typkorrekt: beide Seiten sind Funktionen der reellen Quellvariable `u` im Fenster `(-R,R)`.

### Firewall

`X_{p,k,R}` ist hier der **auf die Quellvariable `u in (-R,R)` beschraenkte** Jump-Kanal. Die volle COMMON-JUMP-Norm auf der ganzen reellen Linie enthaelt zusaetzlich die ausserhalb des Quellfensters liegenden Shiftanteile. Diese duerfen nicht stillschweigend mit `P_R D_s E_R` identifiziert werden.

---

# 2. Der P11-Rest benutzt dieselben raeumlichen Jump-Kanaele

P11 definiert

```math
(R_Rf)(u)
=\sum_p\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_Rf(u)\otimes Q_R(u)\eta_{p,k}.
```

Damit

```math
\boxed{
(R_Rf)(u)
=\sum_{p,k}
X_{p,k,R}f(u)\otimes Q_R(u)\eta_{p,k}.
}
```

Hub und Rest verwenden somit nicht nur aehnliche Koeffizienten, sondern denselben raeumlichen Jump-Kanal; sie unterscheiden sich ausschliesslich in der finite-adischen Root-/Innovationskoordinate.

---

# 3. Source depth ist exakt die geometrische Overlap-Tiefe

Die P11-Tiefe ist

```math
J_{p,R}(u)
=\max\left\{0,
\left\lfloor\frac{2(R-|u|)_+}{\log p}\right\rfloor
\right\}.
```

Fuer `k>=1` gilt

```math
\boxed{
k\le J_{p,R}(u)
\iff
|u|+\frac{k}{2}\log p\le R.
}
```

Die rechte Seite ist genau die Bedingung

```math
u\pm\frac{k}{2}\log p\in[-R,R].
```

Also:

> `Q_R(u)` behaelt den vollstaendigen `p^k`-Martingalmark genau dort, wo der zugehoerige symmetrische Jump an der Quelle `u` **beide** Shiftendpunkte innerhalb des Fensters sieht.

Die finite-adische Konditionierung ist damit ein exakter Overlap-Filter fuer die raeumlichen Jumpfeatures.

---

# 4. Geschlossene Formel fuer den source-conditioned Prime-Gram

Die normalisierten Restmarks sind

```math
\eta_{p,k}
=\sqrt{p-1}\sum_{a=0}^{k-1}p^{(a-k)/2}\psi_{p,a}.
```

Fixiere `u` und setze

```math
J=J_{p,R}(u),
\qquad
m=\min(j,k,J).
```

Dann

```math
\begin{aligned}
\langle Q_R(u)\eta_{p,j},Q_R(u)\eta_{p,k}\rangle
&=(p-1)\sum_{a=0}^{m-1}p^{a-(j+k)/2}\\
&=p^{-(j+k)/2}(p^m-1).
\end{aligned}
```

Der gemeinsame Rootanteil zweier Hub-aktiver Kanaele ist

```math
q_p^jq_p^k=p^{-(j+k)/2}.
```

Daher fuer `p^j,p^k<=e^{2R}` der **kombinierte Hub+Rest-Gram**

```math
\boxed{
G^{(p)}_{R,u}(j,k)
=p^{\min(j,k,J_{p,R}(u))-(j+k)/2}.
}
```

Fuer verschiedene Primzahlen `p!=r` sind die Restsektoren orthogonal und der Hub liefert, solange beide Kanaele im Hub-Cutoff liegen,

```math
\boxed{
G_{R,u}((p,j),(r,k))
=p^{-j/2}r^{-k/2}.
}
```

Diese Cross-prime Korrelation ist unabhaengig von `u`; die Source-Konditionierung wirkt nur auf die prime-spezifischen Innovationsraeume.

---

# 5. Interior = voller AR(1)-Gram

Falls

```math
J_{p,R}(u)\ge\min(j,k),
```

ist `m=min(j,k)` und damit

```math
\begin{aligned}
G^{(p)}_{R,u}(j,k)
&=p^{\min(j,k)-(j+k)/2}\\
&=p^{-|j-k|/2}\\
&=q_p^{|j-k|}.
\end{aligned}
```

Also wird auf jedem voll ueberlappenden Kanalpaar exakt die stationaere AR(1)-/OU-Kovarianz des fensterlosen P11-Ledgers reproduziert.

Dies ist keine asymptotische Aussage und keine Approximation.

---

# 6. Boundary = gradueller Verlust von Innovationen; bei J=0 reiner Root

Sinkt `J_{p,R}(u)` unter `min(j,k)`, so friert der Exponent bei `J` ein:

```math
G^{(p)}_{R,u}(j,k)
=p^{J-(j+k)/2}.
```

Insbesondere bei

```math
J_{p,R}(u)=0
```

verschwinden alle Restmarks dieses Primastes und

```math
\boxed{
G^{(p)}_{R,u}(j,k)
=p^{-(j+k)/2}=q_p^jq_p^k.
}
```

Der Primeblock ist dort Rang eins: nur die gemeinsame Rootkoordinate ueberlebt.

Damit ist die Source-Konditionierung geometrisch eine kontinuierliche (stueckweise konstante) Interpolation

```text
full OU/tree innovations  --->  fewer innovations  --->  root only.
```

---

# 7. Der fensterlose Tree-Gram besitzt eine universelle untere Framekonstante

Betrachte eine beliebige endliche Kanalmenge und den normalisierten fensterlosen P11-Tree-Gram `G_tree`.

Auf einem Prime-Ast gilt

```math
R_q=T_q^*T_q+uu^*,
\qquad
q=p^{-1/2},
```

mit

```math
T_q^{-1}
=\frac{I-qS}{\sqrt{1-q^2}}.
```

Wegen `||S||<=1` folgt

```math
\|T_q^{-1}\|
\le\frac{1+q}{\sqrt{1-q^2}}.
```

Daher

```math
T_q^*T_q
\succeq
\frac{1-q}{1+q}I.
```

Da `q<=2^{-1/2}` fuer alle Primzahlen,

```math
\frac{1-q}{1+q}
\ge
\frac{1-2^{-1/2}}{1+2^{-1/2}}
=3-2\sqrt2.
```

Die Restinnovationen verschiedener Primzahlen sind orthogonal und der gemeinsame Root ist ein zusaetzlicher positiver Rang-eins-Term. Somit

```math
\boxed{
G_{tree}\succeq(3-2\sqrt2)I.
}
```

Tensorisiert mit einem beliebigen Hilbertraum `H` folgt fuer beliebige Kanalvektoren `y_i in H`

```math
\boxed{
\sum_{i,j}(G_{tree})_{ij}\langle y_i,y_j\rangle
\ge
(3-2\sqrt2)\sum_i\|y_i\|^2.
}
```

Das ist ein radiusunabhaengiger Lower-Frame-Satz fuer die **ungekuerzte** P11-Tree-Geometrie.

---

# 8. Source conditioning zerstoert diesen pointwise Framebound am Rand

Der Satz aus §7 darf nicht auf die source-conditioned Gramfelder `G_{R,u}` uebertragen werden.

Bei `J=0` und mindestens zwei Hub-aktiven Kanaelen ist der Gram auf dem betreffenden Kanalspan nur

```math
G_{R,u}=qq^*,
```

also Rang eins. Damit besitzt er Nullrichtungen und es existiert kein `c>0` mit

```math
G_{R,u}\succeq cI
```

uniform in `u`.

Somit

```text
windowless Tree Lower Frame              ✓[M]
pointwise source-conditioned Lower Frame ×[M]
```

Die verlorene Koerzivitaet ist exakt ein Boundary-/Overlap-Phaenomen und muss durch die raeumliche Struktur, die Gamma-Seite, Feshbach-Shorting oder die Radius-Transportgeometrie repariert werden; sie kann nicht aus dem fensterlosen Kanal-Gram allein importiert werden.

---

# 9. Tiefe Restkanaele und Firewall

Der Hub summiert nur ueber

```math
p^k\le e^{2R}.
```

Der Restoperator kann wegen einseitiger Shiftueberlappung noch tiefere Kanaele enthalten; aus der P11-Supportrechnung folgt effektiv nur

```math
p^k\le e^{4R}.
```

Fuer solche tieferen Kanaele existiert keine gemeinsame Hubkoordinate in `H_R`. Ihre source-conditioned Marks duerfen daher nicht in die Formel aus §4 mit einem kuenstlich hinzugefuegten Rootterm eingesetzt werden.

Das ist strukturell passend zur COMMON-JUMP-Gauge:

- `k log p<=2R`: potentiell echte zweiseitige Interaktionskanaele und Hubkopplung;
- `2R<k log p<=4R`: nur einseitige source-boundary Sichtbarkeit im P11-Rest, ohne Hubterm.

Ob diese tieferen Restkanaele exakt die notwendige Exterior-/Gauge-Absorption einer Forward-Dilation liefern, ist **noch offen**. Die vorhandenen Formeln machen diese Frage jetzt aber typkorrekt und lokal explizit.

---

# 10. Konsequenz fuer Whitening und den naechsten Gate

Auf dem ungekuerzten Kanalindexraum kann man aus dem Tree-Syntheseoperator `S`, `S^*S=G_tree`, die kanonische Isometrie

```math
U=S G_{tree}^{-1/2}
```

bilden. Dies transportiert orthogonale Kanalfeatures energieerhaltend in den Tree-Span.

Der source-conditioned P11 ist jedoch **kein** festes `G_tree`: sein Innovationsgram haengt ueber `J_{p,R}(u)` von der Raumvariable ab und wird am Rand singulaer.

Daher liefert das konstante fensterlose Whitening nicht automatisch einen radius- und source-kompatiblen Intertwiner fuer den realen P11-Operator.

Der naechste echte Gate lautet:

```math
\boxed{
\text{Existiert eine kanonische source-dependent Dilation/Whitening-Struktur,}
}
```

```math
\boxed{
\text{die die exakten Gramfelder }G_{R,u}\text{ samt tiefen Randkanaelen}
\text{ und den COMMON-JUMP-Cutoff verbindet?}
}
```

Jede positive Antwort muss insbesondere die Rangdegeneration bei `J=0`, die tieferen Restkanaele und die connecting maps `R<S` gleichzeitig behandeln.
