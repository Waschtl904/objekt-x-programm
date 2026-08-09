# P11-C1b — Lift-/Quotienteninvarianz des Prime–Prime-Gramkerns

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1b]`  
**Vorgänger:** `AUDIT-2026-08-09_P11_C1_PrimePrime_OperatorValued_GramKernel.md`  
**Primärbasis:** P05 §§1–5, §7; insbesondere Liftabhängigkeit, Nullraumfaktorisierung und die Trennung

\[
T_p\neq C_p^{[\widehat\varepsilon_p]}\neq C_p^{\rm rel}[\widehat\varepsilon_p].
\]

**Urteil:**

\[
\boxed{[P11-C1b]\quad\checkmark[M]_{\rm part}}
\]

Der Nullraumquotient kanonisiert den Gramkern für eine **fest gewählte** Kanalfamilie. Er beweist jedoch nicht die Unabhängigkeit von der Wahl der Primhebungen. Liftunabhängigkeit bleibt ein echter offener Konstruktionspunkt.

---

## 1. Ausgangspunkt nach C1

Für eine feste Familie

\[
V_p:\mathcal D_p\to\mathcal H
\]

in demselben Hilbertraum definiert

\[
G_{pq}(a,b):=\langle V_pa,V_qb\rangle
\]

einen positiven Gramkern.

P05 zeigt jedoch, dass die tatsächlich konstruierten Primkanäle historisch von einer gewählten Primhebung `\widehat\varepsilon_p` abhängen. Daher ist der relevante Typ zunächst

\[
V_p^{[\widehat\varepsilon_p]},
\]

und somit

\[
G_{pq}^{[\widehat\varepsilon_p,\widehat\varepsilon_q]}(a,b)
:=
\left\langle
V_p^{[\widehat\varepsilon_p]}a,
V_q^{[\widehat\varepsilon_q]}b
\right\rangle.
\]

Die Frage lautet, ob daraus intrinsisch ein hebungsunabhängiger Kern entsteht.

---

## 2. Was der Nullraumquotient sicher leistet

Fixiere eine Familie `V_p` und setze

\[
N_p:=\ker V_p.
\]

Dann gilt für `n\in N_p` und jedes `q,b`:

\[
G_{pq}(n,b)=\langle V_pn,V_qb\rangle=0.
\]

Daher faktorisiert jeder Kreuzblock eindeutig über

\[
\mathcal D_p/N_p.
\]

Ebenso faktorisiert der gesamte endliche Gramkern über die direkte Summe der festen Quotienten.

\[
\boxed{
\text{Für eine feste Kanalfamilie ist Nullraumfaktorisierung vollständig kompatibel mit allen Kreuzblöcken.}
}
\]

Status: `✓[M]`.

Dies ist die globale Version des abstrakten Nullraumabstiegsmechanismus aus P05 §5.

---

## 3. Warum dies keine Liftunabhängigkeit beweist

Seien zwei zulässige Hebungen gegeben und

\[
V_p'=V_p+\Delta_p.
\]

Dann ändert sich der Kreuzblock zu

\[
\begin{aligned}
G_{pq}'(a,b)-G_{pq}(a,b)
&=
\langle \Delta_pa,V_qb\rangle
+\langle V_pa,\Delta_qb\rangle
+\langle \Delta_pa,\Delta_qb\rangle.
\end{aligned}
\]

Damit verschwindet die Liftabhängigkeit **nicht** schon deshalb, weil für jede feste Realisierung ein Nullraumquotient existiert.

P05 liefert gerade keinen Satz, wonach jede zulässige Liftänderung `k` im Nullraum der relevanten Kanalabbildung liegt. Im Gegenteil bleibt die Existenz eines exakt zulässigen geladenen Lifts mit

\[
T_p(k)\neq0
\]

offen. Eine solche Richtung wäre gerade **nicht** automatisch im Rohkopplungsnullraum unsichtbar.

\[
\boxed{
\text{Nullraumquotient einer festen Realisierung}\neq\text{Kanonisierung verschiedener Realisierungen.}
}
\]

Status: `✓[M]` als Typfirewall.

---

## 4. Exaktes Kriterium für numerische Gramkern-Invarianz

Für zwei Familien `(V_p)` und `(V_p')` ist der Gramkern exakt gleich genau dann, wenn

\[
\boxed{
\langle V_p'a,V_q'b\rangle
=
\langle V_pa,V_qb\rangle
\quad
\forall p,q,a,b.
}
\]

Dies ist tautologisch als Gleichheitskriterium, aber strukturell nützlich: Es zeigt, dass **alle** Kreuz- und Diagonalblöcke gleichzeitig kontrolliert werden müssen; paarweise Normerhaltung einzelner `V_p` genügt nicht.

Ein hinreichender struktureller Mechanismus wäre ein einziger unitärer Operator `U` auf dem abgeschlossenen globalen Kanalspan mit

\[
V_p'=UV_p
\qquad\forall p.
\]

Dann

\[
\langle V_p'a,V_q'b\rangle
=
\langle UV_pa,UV_qb\rangle
=
\langle V_pa,V_qb\rangle.
\]

Damit ist die richtige Äquivalenzrelation nicht notwendigerweise „gleicher Lift“, sondern möglicherweise

\[
\boxed{\text{gemeinsame unitäre Gaugeklasse der gesamten Kanalfamilie}.}
\]

Status: `✓[M]` als abstraktes Lemma; Existenz einer solchen kanonischen Gaugeklasse im Repo: `?[O]`.

---

## 5. Kolmogorov-/Gram-Eindeutigkeit

Allgemein bestimmt ein positiver Gramkern seine minimale Hilbertraumrealisierung bis auf eindeutige unitäre Äquivalenz auf dem erzeugten Abschluss.

Für P11 bedeutet das:

- **wenn** ein intrinsischer positiver Kern `G_{pq}` unabhängig von Lifts definiert werden kann,
- dann ist die minimale gemeinsame Hilbertraumrealisierung im Wesentlichen bereits kanonisch bis auf unitäre Äquivalenz;
- die schwierigere Richtung ist daher nicht die Rekonstruktion des Hilbertraums aus `G`, sondern die intrinsische Definition von `G` selbst.

Dies verschiebt den Kanonizitätsengpass noch einmal:

\[
\boxed{
\text{intrinsischer positiver Kern}
\Longrightarrow
\text{minimale gemeinsame Geometrie bis auf unitäre Äquivalenz}.
}
\]

---

## 6. Verbindung zur P05-Liftgeometrie

P05 hält bindend fest:

1. die exakte Liftzulässigkeit ist **quadratisch**, nicht durch eine zusätzliche homogene lineare Kernfamilie beschrieben;
2. im auditierten Quellenkegel existiert keine zusätzliche nichttriviale `L_{p,a}`-Kernfamilie;
3. ein exakt zulässiger Nichtnullzeuge mit `T_p(k)\neq0` ist nicht konstruiert, aber auch nicht ausgeschlossen;
4. Nichtentartung und Hebungsunabhängigkeit der Kanalgewichte bleiben offen.

Daraus folgt für P11:

\[
\boxed{
\text{Die vorhandene lokale Quotientenarchitektur reicht nicht aus, um }G_{pq}\text{ als liftunabhängig zu erklären.}
}
\]

Dies ist **kein** No-Go gegen liftunabhängige globale Gramkerne; es ist ein Quellen-/Beweisdefizit.

---

## 7. Drei zulässige Kanonisierungswege

Nach dem Audit bleiben drei logisch verschiedene Wege offen.

### Weg A — Kanonische Hebung

Die Arithmetik selektiert für jedes `p` eine ausgezeichnete Hebung

\[
\widehat\varepsilon_p^{\rm can}.
\]

Dann wird

\[
G_{pq}:=
G_{pq}^{[\widehat\varepsilon_p^{\rm can},\widehat\varepsilon_q^{\rm can}]}.
\]

Problem: eine solche Selektion ist derzeit nicht konstruiert.

### Weg B — Liftinvarianter Kern

Obwohl die einzelnen `V_p^{[\widehat\varepsilon_p]}` variieren, bleibt ihr gesamter Gramkern invariant.

Problem: genau diese Identität ist nicht bewiesen.

### Weg C — Kanonische globale Gaugeklasse

Verschiedene Liftfamilien erzeugen Gram-äquivalente Minimalrealisierungen, verbunden durch einen **gemeinsamen** unitären Operator, nicht durch unabhängig gewählte `U_p`.

Problem: ein solcher globaler Intertwiner ist nicht konstruiert.

---

## 8. Wichtige Firewall: unabhängige lokale Unitaries reichen nicht

Nimmt man für jedes `p` unabhängig

\[
V_p'=U_pV_p,
\]

so wird

\[
G_{pq}'=V_p^*U_p^*U_qV_q.
\]

Für `p\neq q` ist dies im Allgemeinen **nicht** gleich `G_{pq}`.

Damit ist eine bloß kanalweise unitäre Äquivalenz zu schwach. Für die globale Kreuzgeometrie muss die Gauge **kohärent über alle Primrichtungen** sein.

\[
\boxed{
\text{lokale unitäre Äquivalenz}\not\Rightarrow\text{globale Gramkern-Invarianz}.
}
\]

Status: `✓[M]`.

---

## 9. Statusmatrix

| Teilfrage | Status |
|---|---|
| Kreuzblöcke faktorieren über `ker V_p` einer festen Familie | `✓[M]` |
| gesamter feste-Familie-Gramkern faktorisiert über Nullraumquotienten | `✓[M]` |
| Nullraumquotient beweist Liftunabhängigkeit | `×[M]` als Implikation |
| gemeinsame unitäre Gauge `V_p'=UV_p` erhält gesamten Gramkern | `✓[M]` |
| unabhängige lokale Gauges `V_p'=U_pV_p` erhalten Kreuzblöcke automatisch | `×[M]` |
| kanonische Hebung | `?[O]` |
| liftinvarianter numerischer Gramkern | `?[O]` |
| kanonische globale unitäre Gaugeklasse | `?[O]` |

---

## 10. P11-Kernbefund nach C1b

Nach C1 und C1b ist der konstruktive Engpass dreistufig:

\[
\boxed{
\text{Primkanalabbildungen}
\longrightarrow
\text{intrinsischer positiver Gramkern}
\longrightarrow
\text{minimale globale Hilbertraumrealisierung}.
}
\]

Der zweite Pfeil ist der aktive Engpass.

---

## 11. Nächster Arbeitsknoten

\[
\boxed{[P11\text{-}C1c]\quad\text{Suche nach einem liftfreien Gramkern direkt aus der gemeinsamen Quelle.}}
\]

Statt einzelne `V_p` zu kanonisieren, soll geprüft werden, ob P02/P05 bereits eine **direkte bilineare Formel**

\[
G_{pq}(a,b)
\]

aus adelischer Amplitude, Primkantenmarkierung, Skalierungsfluss oder Wres-Paarung liefern, deren Kolmogorov-Realisierung erst nachträglich die `V_p` erzeugt.
