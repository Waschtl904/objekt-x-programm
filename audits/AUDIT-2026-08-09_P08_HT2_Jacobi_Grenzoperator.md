# P08 Pass A — H-T2 Jacobi-Grenzoperator / Renormierungsbarrieren

**Datum:** 9. August 2026  
**Paket:** H-T2  
**Prüfart:** `AUDIT-RECONCILED` + lokale `TARGETED-REAUDIT`s  
**Scope:** Live-NEU-123, NEU-123A–I inkl. beider 123F-Dateien, NEU-124, NEU-125; Abgleich gegen P06/P07 und NEU-79  

## 0. Endstatus vorweg

\[
\boxed{\text{H-T2 COMPLETE — abstraktes Jacobi-Fundament erhalten; konkreter unrenormierter nichtdegenerierter Limes scheitert bereits an }b_{1,N}\to0.}
\]

Kein direkter `D_rel`-No-Go wird Live-NEU-123 oder Live-NEU-125 zugeschrieben; beide Blätter behaupten diesen Anschluss nicht.

---

## 1. Typfirewall: zwei historisch gleich benannte, aber verschiedene Jacobi-Pfade

### 1.1 Direkt symmetrische Jacobi-Schließung

Live-NEU-123A definiert

\[
\boxed{A_N^{\rm sym}:=B_N^\Lambda=J_N^\Lambda+(J_N^\Lambda)^*.}
\]

Auf dem endlichen Raum `ell^2(I_N)` ist dies ein selbstadjungierter endlicher Operator. Die Lanczos-Matrix besitzt reelle Diagonalen und nichtnegative Offdiagonalen.

Dieser Pfad ist mathematisch sauber und von P06s antisymmetrischem Operator

\[
J_N^-:=\frac12(\Theta_N-\Theta_N^\dagger)
\]

zu unterscheiden.

**Status:** `✓[M]` für die endliche direkt symmetrisierte Jacobi-Schließung.

### 1.2 Historischer antisymmetrischer Pfad

P06 fixiert dagegen

\[
J_N^-\text{ schiefadjungiert},
\qquad
S_N:=\frac1{2i}(\Theta_N-\Theta_N^\dagger)=-iJ_N^-
\text{ selbstadjungiert}.
\]

P07 führt daneben historische Formeln vom Typ

\[
A_N^{Jac,-}=H_N+\beta_NJ_N^-
\]

und lässt deren Selbstadjungiertheit offen.

**Bindende P08-Notationsregel:** Im SYN wird die direkt symmetrische NEU-87/123A-Schließung nicht unkommentiert mit demselben Symbol wie der antisymmetrische P06/P07-Pfad bezeichnet. Vorzugsnotation:

\[
A_N^{\rm sym}=B_N^\Lambda.
\]

Damit bleibt die H-T1-Firewall vollständig erhalten, ohne die eigenständige selbstadjungierte Jacobi-Matrix aus NEU-123A fälschlich zu sperren.

---

## 2. NEU-123 Stamm — abstraktes Jacobi-Fundament

NEU-123 setzt alle endlichen Jacobi-Blöcke in einen gemeinsamen Raum `ell^2(N_0)` und formuliert:

\[
a_{j,N}\to a_j\in\mathbb R,
\qquad
b_{j,N}\to b_j>0
\quad(j\text{ fest}),
\]

sowie als hinreichendes Kriterium für wesentliche Selbstadjungiertheit des formalen Grenzoperators die Carleman-Bedingung

\[
\sum_j\frac1{b_j}=\infty.
\]

Unter Kernkonvergenz und wesentlicher Selbstadjungiertheit folgt die starke Resolventenkonvergenz der Jacobi-Trunkierungen.

### Status

- gemeinsamer Hilbertraum / endliche Jacobi-Trunkierung: `✓[M]`;
- abstraktes Core-/Carleman-zu-starker-Resolventenkonvergenz-Schema: `✓[M]` als klassisches Operatorresultat;
- Identifikation eines solchen Grenzoperators mit Zeta-/Objekt-X-Daten: daraus **nicht** folgend, `?[O]`.

### Firewall

Der Live-Stamm NEU-123 behauptet **nicht**

\[
A_N^{\rm sym}\to D_{\rm rel}.
\]

Der historische direkte Jacobi-zu-`D_rel`-Pfad bleibt durch P06 superseded, ist aber nicht als eigene Aussage des heutigen NEU-123-Stamms zu etikettieren.

---

## 3. Konkrete Stufe 1 — unrenormierter nichtdegenerierter Pfad scheitert

Live-NEU-123A liefert für den Startvektor `q_0=e_1`:

\[
a_{0,N}=0,
\]

\[
\boxed{
b_{1,N}
=\frac{\gamma}{N}
\sqrt{\sum_{n=2}^{N-1}\Lambda(n)^2}
\asymp
\gamma\sqrt{\frac{\log N}{N}}
\to0.
}
\]

NEU-123s nichtdegenerierte Eintrittsbedingung verlangt hingegen für jeden festen Index einen positiven Grenzwert `b_j>0`.

Daher ist bereits bei `j=1`:

\[
\boxed{b_{1,N}\to b_1>0\quad\text{falsch}.}
\]

### Status

- konkrete **unrenormierte** nichtdegenerierte Stufe 1 für die NEU-87/123A-Sequenz: `×[M]`;
- nicht lediglich `?[O]`.

Dies schließt nicht jeden möglichen starken Resolventenlimes aus; es schließt den in NEU-123 vorgesehenen nichtdegenerierten irreduziblen Jacobi-Limes mit positiver erster Kante aus.

---

## 4. Startvektor-Kollaps — gültiger negativer Satz, aber keine globale Diagonalität

Da

\[
A_N^{\rm sym}e_0=b_{1,N}e_1,
\qquad b_{1,N}\to0,
\]

und jeder endliche `A_N^{sym}` selbstadjungiert ist, gilt für `z` außerhalb der reellen Achse per Resolventenidentität

\[
\left|
\langle e_0,(A_N^{\rm sym}-z)^{-1}e_0\rangle+\frac1z
\right|
\le
\frac{\|A_N^{\rm sym}e_0\|}{|z|\,|\operatorname{Im}z|}
\to0.
\]

Somit

\[
\boxed{
m_{e_0,N}(z)\to-1/z.
}
\]

Die unrenormierte Startvektor-Spektralspur kann daher nicht `m_arith` liefern.

**Status:** `✓[M]_{neg}` für den Startvektor-/ersten-Kanten-Kollaps.

### Korrektur zu NEU-123A

NEU-123A formuliert weitergehend sinngemäß

\[
b_{1,N}\to0\Rightarrow A_\infty\text{ diagonal}.
\]

Das folgt nicht. Aus dem ersten Offdiagonalparameter folgt keine Aussage `b_{j,N}->0` für alle `j>=2`.

**Status der globalen Diagonalitätsbehauptung:** `×[M]`.

Bindend ist nur: `e_0` entkoppelt asymptotisch im unrenormierten Modell.

---

## 5. NEU-123B–E — Renormierungsbarriere und arithmetische Reduktion

### 5.1 Erste skalare Normalisierung

Die Wahl

\[
\kappa_N=b_{1,N}
\]

setzt die erste reskalierte Offdiagonale auf 1. Dies ist eine natürliche operatorinterne Normierungskonvention.

Nicht migriert wird eine unbegründete Einzigkeitsaussage „nur diese Normierung ist intrinsisch möglich“; die exakte Aussage ist lediglich, dass diese Wahl die erste Jacobi-Kante kanonisch normiert.

### 5.2 Exakte Diagonaldrift-Reduktion

NEU-123C reduziert exakt

\[
\boxed{
\frac{a_{1,N}}{b_{1,N}}
=
\frac{T_N}{S_N^{3/2}},
}
\]

mit

\[
S_N=\sum_{k\le N}\Lambda(k)^2\sim N\log N
\]

und einer positiven Mangoldt-Dreifachsumme `T_N`.

**Status:** `✓[M]` als algebraische Reduktion.

### 5.3 Heuristiken

Die naive `N^3`-Heuristik aus NEU-123C wird durch NEU-123D paritätskorrigiert. Wegen des äußeren Faktors `Lambda(h)` liegen die primären geraden Hauptterm-Shifts auf `h=2^r`.

Unter der entsprechenden Hardy-Littlewood-Heuristik ergibt sich

\[
T_N\asymp N^2\log N,
\qquad
\frac{a_{1,N}}{b_{1,N}}\asymp\sqrt{\frac N{\log N}}.
\]

**Status:** `CONDITIONAL/heuristisch`, nicht `✓[M]`.

NEU-123E identifiziert korrekt die strenge Lücke als sparse Primpaarkorrelations-Untergrenze; das Minimalziel bleibt `?[O]`.

---

## 6. NEU-123F/G — numerische Evidenz, nicht asymptotischer Satz

### 6.1 Dreifachsumme

Die numerischen Tabellen aus beiden NEU-123F-Dateien wurden unabhängig aus den angegebenen Definitionen reproduziert. Die Werte für

\[
D_N=T_N/S_N^{3/2}
\]

und

\[
\widetilde D_N=D_N\sqrt{\log N/N}
\]

stimmen für die veröffentlichten `N=100,...,5000`.

Damit ist der finite-window Befund valide:

\[
\widetilde D_N\approx1.5\text{--}1.6
\]

im getesteten Bereich.

**Status:** `heur+num`; strenge Divergenz bleibt `?[O]`.

### 6.2 Zweite Offdiagonale

Auch die veröffentlichten Lanczos-Werte aus NEU-123G für

\[
\frac{a_{1,N}}{b_{1,N}},
\qquad
\frac{b_{2,N}}{b_{1,N}}
\]

bei `N=30,...,200` wurden reproduziert.

Die Daten zeigen starkes Wachstum von `b2/b1`. Sie beweisen aber weder

\[
\frac{b_{2,N}}{b_{1,N}}\to\infty
\]

noch die stärkere asymptotische Form

\[
\frac{b_{2,N}}{b_{1,N}}\sim N.
\]

**Status:** finite numerische Evidenz `✓[M]_{num}`; asymptotische Aussage `?[O]`.

---

## 7. NEU-123H — No-scalar-renormalization

Das abstrakte Lemma ist elementar korrekt:

Falls

\[
\frac{b_{2,N}}{b_{1,N}}\to\infty,
\]

kann keine positive skalare Folge `kappa_N` beide Größen `b1,N/kappa_N` und `b2,N/kappa_N` gegen endliche positive Grenzwerte schicken.

**Status:** `✓[M]` als bedingtes abstraktes Lemma.

Die Anwendung auf die konkrete NEU-87-Sequenz bleibt wegen der offenen strengen Divergenz des Quotienten:

`CONDITIONAL / ?[O]`.

Damit wird aus den endlichen numerischen Daten kein strenger allgemeiner No-Go gemacht.

---

## 8. NEU-123I — gradierte Renormierung

Erhalten bleiben:

1. Eine nichtunitäre diagonale Similarität
   \[
   D_N^{-1}A_N^{\rm sym}D_N
   \]
   ist im ursprünglichen `ell^2` im Allgemeinen nicht selbstadjungiert.
2. Die gerichteten Kanten erfüllen exakt
   \[
   \widetilde b_{j,N}^+\widetilde b_{j,N}^-=b_{j,N}^2.
   \]
3. Ein gewichteter Hilbertraum ist nur mit kontrolliertem Grenzraum ein möglicher Ausweg.
4. Eine symmetrische Formrenormierung
   \[
   D_NA_N^{\rm sym}D_N
   \]
   erhält in endlicher Dimension Selbstadjungiertheit, ist aber keine Similarität und muss intrinsisch begründet werden.
5. Eine positive nichtskalare Renormierung **vor** Lanczos bleibt eine offene strukturelle Möglichkeit.

**Status:** methodische No-Go-Teile `✓[M]`; konstruktive Varianten `?[O]`.

---

## 9. NEU-124 — gesperrtes Platzhalterblatt

Live-NEU-124 ist ausdrücklich erst aktiv, wenn NEU-123 Stufe 1/2 einen kanonischen selbstadjungierten Grenzoperator liefert.

Für die konkrete unrenormierte NEU-87-Sequenz ist die verlangte positive erste Offdiagonale bereits durch

\[
b_{1,N}\to0
\]

verletzt.

Daher bleibt NEU-124 für diesen Pfad **gesperrt**.

Seine offenen Zielaussagen bleiben:

- Spektrum/Ordinaten: `?[O]`;
- reines Punktspektrum/Einfachheit: `?[O]`;
- Projektions-/Massenkontrolle: `?[O]`;
- Spektralmaßidentifikation
  \[
  \mu_{\Omega_\infty}^{A_\infty}=\mu_\xi
  \]
  : `?[O]`.

### Provenienzkorrektur

NEU-124 enthält **keine** `N/log N`-Skalenkorrektur. Ein solcher historischer Bilanzmarker wird nicht diesem Live-Blatt zugeschrieben.

---

## 10. NEU-125 — korrekter abstrakter Kern, falsche Skalenprovenienz

### 10.1 Erhaltener Satz: skalare Lanczos-Kovarianz

Für `c_N>0` gilt exakt:

\[
A_N\mapsto c_NA_N
\Longrightarrow
 a_{j,N}\mapsto c_Na_{j,N},
\qquad
 b_{j,N}\mapsto c_Nb_{j,N}.
\]

Damit ist

\[
\boxed{
\frac{b_{2,N}}{b_{1,N}}
}
\]

unter jeder positiven skalaren Prä-Lanczos-Skalierung invariant.

Die Herglotz-Transformation

\[
m_N^{c}(z)=c_N^{-1}m_N(z/c_N)
\]

ist für einen selbstadjungierten Ausgangsoperator ebenfalls korrekt.

**Status:** `✓[M]`.

### 10.2 Falscher Quellenimport aus NEU-79

NEU-125 behauptet sinngemäß, NEU-79 liefere eine intrinsische Prä-Lanczos-Skala `sqrt(N)`.

NEU-79 liefert tatsächlich

\[
J_N^-
=
\kappa_N U_N^*\mathsf S_NR_ND_{BC,N}U_N,
\qquad
\kappa_N=|\Sigma_N|,
\]

mit je nach Labelmenge

\[
\kappa_N=N
\]

oder

\[
\kappa_N\sim N/\log N.
\]

Die effektiv relevante Größe lautet

\[
\gamma_N=a_N\kappa_N
\]

und ist dort offen.

Daher:

\[
\boxed{\text{„NEU-79 liefert intrinsisch }\sqrt N\text{“}=\times[M].}
\]

Auch die Zeile `sqrt(N) ~ N` in NEU-125 §125.0 ist mathematisch falsch.

### 10.3 Präzise erste-Kanten-Skala

Aus NEU-123A folgt zur alleinigen Stabilisierung der ersten Kante

\[
c_N\asymp b_{1,N}^{-1}
\asymp
\frac1\gamma\sqrt{\frac N{\log N}}.
\]

Das ist eine aus der Jacobi-Kante abgelesene Skalierung, **keine** aus NEU-79 hergeleitete Feshbach-Kanalzahl.

### 10.4 Offener nichtskalarer Ausweg

Die Form

\[
B_N\mapsto W_N^{1/2}B_NW_N^{1/2},
\qquad W_N>0,
\]

bleibt als abstrakte Prä-Lanczos-Idee offen. Ihre Intrinsizität, Typisierung und arithmetische Herkunft werden nicht in H-T2 gelöst; das gehört in die nachfolgende Gram-/Prä-Lanczos-Reconciliation H-T3 und, für die globale intrinsische Geometrie, gegebenenfalls P11.

---

## 11. H-T2 Statusmatrix

| Punkt | Endstatus |
|---|---|
| Endlicher direkt symmetrischer Jacobi-Block `B_N^Lambda` | `✓[M]` selbstadjungiert |
| P06 `J_N^-` vs. `S_N` Typtrennung | bindende Firewall `✓[M]` |
| Abstraktes NEU-123 Core/Carleman/s.r.-Schema | `✓[M]` |
| Konkrete unrenormierte Bedingung `b1,N -> b1>0` | `×[M]` |
| Unrenormierter Startvektor-Weyl-Limes | `m_{e0,N}->-1/z`, `✓[M]_{neg}` |
| NEU-123A globale Diagonalität aus `b1,N->0` | `×[M]` |
| Exakte Reduktion `a1/b1=T_N/S_N^{3/2}` | `✓[M]` |
| Paritätskorrigierte Driftordnung | `CONDITIONAL/heur+num`; streng `?[O]` |
| 123F finite numerische Tabellen | unabhängig reproduziert `✓[M]_{num}` |
| 123G finite Lanczos-Tabellen | unabhängig reproduziert `✓[M]_{num}` |
| `b2/b1 -> infinity` bzw. `~N` | `?[O]` streng |
| 123H No-scalar-Lemma | `✓[M]` abstrakt; Anwendung `CONDITIONAL` |
| 123I Nichtunitäre Similarität als Jacobi-Rettung | `✓[M]_{neg}` |
| 123I gewichtete/Form-/Prä-Lanczos-Varianten | `?[O]` |
| NEU-124 | gesperrt, Zielaussagen `?[O]` |
| behauptete NEU-124 `N/log N`-Skala | nicht im Live-Blatt; nicht migrieren |
| NEU-125 skalare Lanczos-Kovarianz | `✓[M]` |
| NEU-125 „NEU-79 liefert sqrt(N)“ | `×[M]` |
| präzise erste-Kanten-Skala `1/b1` | `~sqrt(N/log N)`, `✓[M]` aus NEU-123A |
| intrinsisches nichtskalares `W_N` | `?[O]` -> H-T3/P11 |
| direkter Jacobi->`D_rel`-Anschluss in Live-123/125 | nicht vorhanden |

---

## 12. Endurteil H-T2

\[
\boxed{\text{H-T2 COMPLETE — keine ausstehenden H-T2-Reaudits.}}
\]

Der belastbare P08-Endkern aus diesem Paket lautet:

1. **Abstraktes Jacobi-Grenzoperatorfundament:** tragfähig.
2. **Konkreter unrenormierter NEU-87-Jacobi-Limes:** nichtdegenerierter Pfad scheitert bereits an `b1,N->0`; der Startvektor-Weyl-Limes kollabiert auf `-1/z`.
3. **Skalare Rettung:** erste Kante kann normalisiert werden, aber die zweite-Kanten-Barriere ist streng noch offen; keine numerische Asymptotik wird zum Satz hochgestuft.
4. **Gradierte/nichtskalare Rettung:** nur als intrinsisch herzuleitende Prä-Lanczos-Form sinnvoll; offen.
5. **NEU-124:** bleibt gesperrt.
6. **NEU-125:** abstrakte Skalarkovarianz bleibt; die behauptete `sqrt(N)`-Feshbach-Provenienz aus NEU-79 wird verworfen.

Nächster Pass-A-Knoten:

\[
\boxed{\text{H-T3 — NEU-127/128A/b/130/131: Prä-Lanczos-Grammetrik und Typreconciliation.}}
\]
