# NEU-98 — Korrelationsdichte und Massenniveau-Stabilität der Skalenleiter

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-97 (Skalenleiter \(T=M_N^\theta\); \(T_c=\sqrt{M_N}\) selbstdual; \(T_0=\log^2 M_N\) Kontrollskala)  
**Nächste Nummer:** NEU-99

---

## Ausgangspunkt

NEU-97 stellt die Frage, ob \(B_{N,T}^{\mathrm{arith}}\) entlang der Skalenleiter stabil bleibt und ob ein kritisches \(\theta^*\) existiert. NEU-98 untersucht diese Frage auf **Massenniveau**.

**Korrekturnotiz:** In NEU-97 gilt am selbstdualen Punkt \(T_c = \sqrt{M_N}\) (nicht \(M_N\)); dort treffen sich \(T_c = H_N = \sqrt{M_N}\). Dies wurde dort konsistent so gesetzt.

---

## Definition NEU-98.1 — Rohe Mangoldt-Korrelationsmasse

Setze \(T = M_N^\theta\), \(0 < \theta < 1\), und

$$
H_N := \frac{M_N}{T} = M_N^{1-\theta}.
$$

Auf einem dyadischen Block \(m,n \sim M_N\) definiere die **rohe Korrelationsmasse**

$$
\mathcal{C}_N(\theta)
:=
\sum_{\substack{m,n \sim M_N \\ |m-n| \leq H_N}}
\frac{\Lambda(m)\Lambda(n)}{mn}.
$$

Die PNT-Heuristik liefert:

$$
\mathcal{C}_N(\theta) \sim \frac{H_N}{M_N} = M_N^{-\theta}.
$$

*(Begründung: \(\sim M_N H_N\) Paare, Gewicht \(\sim M_N^{-2}\) pro Paar, \(\Lambda\)-Mittel \(\sim 1\).)* 

**Status: \(\warning[M]\)** (PNT-Heuristik; auf breiten Fenstern \(H_N \gg \log^2 M_N\) kontrollierbar)

---

## Definition NEU-98.2 — Renormierte Korrelationsdichte

Da \(\mathcal{C}_N(\theta) \to 0\) für jedes feste \(\theta > 0\), ist die natürliche **renormierte Dichte**

$$
\widetilde{\mathcal{C}}_N(\theta)
:=
T \cdot \mathcal{C}_N(\theta)
= M_N^\theta \cdot \mathcal{C}_N(\theta).
$$

Heuristisch gilt dann:

$$
\widetilde{\mathcal{C}}_N(\theta) \sim 1.
$$

Die renormierte Dichte ist daher der richtige Prüfgegenstand für Stabilität entlang der Leiter.

**Status: \(\checkmark[M]\)** (Definition)

---

## Satz NEU-98.3 — Diagonalanteil

Der Diagonalanteil (nur \(m = n\)) auf dem Block \(n \sim M_N\):

$$
\mathcal{D}_N
:= \sum_{n \sim M_N} \frac{\Lambda(n)^2}{n^2}
\sim \frac{\log M_N}{M_N}.
$$

**Status: \(\checkmark / \warning[M]\)** (PNT-Standard)

---

## Satz NEU-98.4 — Kreuz/Diagonal-Verhältnis

Mit den Heuristiken aus 98.1 und 98.3:

$$
\frac{\mathcal{C}_N(\theta)}{\mathcal{D}_N}
\sim
\frac{M_N^{-\theta}}{\log M_N / M_N}
=
\frac{M_N^{1-\theta}}{\log M_N}.
$$

Für jedes feste \(0 < \theta < 1\):

$$
\frac{\mathcal{C}_N(\theta)}{\mathcal{D}_N} \to \infty.
$$

Die Kreuzmasse **dominiert** die Diagonale entlang der gesamten Skalenleiter.

Der diagonale Kollaps tritt erst im Randbereich

$$
H_N = O(\log M_N), \qquad T \approx \frac{M_N}{\log M_N}, \qquad \theta \to 1
$$

auf.

**Status: \(\warning[M]\)** (PNT-/Paar-Heuristik, kontrollierbar auf breiten Fenstern)

---

## Satz NEU-98.5 — Kein inneres kritisches \(\theta^*\) auf Massenniveau

$$
\boxed{\text{Kein inneres kritisches }\theta^* \in (0,1)\text{ auf Massenniveau.}}
$$

Begründung: Das Verhältnis \(\mathcal{C}_N/\mathcal{D}_N \sim M_N^{1-\theta}/\log M_N\) ist eine streng monoton fallende Funktion von \(\theta\) ohne innere Singularität. Es gibt keinen Wert \(\theta^* \in (0,1)\), bei dem die Kreuzterme auf Massenniveau kollabieren oder die Diagonale übernehmen.

**Konsequenz:** Ein eventuelles kritisches \(\theta^*\) kann nur in der **arithmetischen Feinstruktur** der normierten Mangoldt-Korrelationen liegen, nicht in der rohen Massenbilanz.

**Status: \(\checkmark / \warning[M]\)**

---

## Verschiebung des Flaschenhalses

| Vorher (NEU-97) | Nachher (NEU-98) |
|---|---|
| Gibt es ein \(\theta^*\)? | Nein, nicht auf Massenniveau |
| Sind Kreuzterme vorhanden? | Ja, dominieren für alle \(\theta < 1\) |
| Was ist stabil? | \(\widetilde{\mathcal{C}}_N(\theta) \sim 1\) |
| Wo liegt der echte Bruchpunkt? | In der arithmetischen Feinstruktur von \(\widetilde{\mathcal{C}}_N\) |

$$
\boxed{\text{Flaschenhals} = \text{Feinstruktur von }\widetilde{\mathcal{C}}_N(\theta)\text{, nicht Massenbilanz.}}
$$

---

## Neue Leitfrage für NEU-99

$$
\boxed{\text{Tr\u00e4gt die Feinstruktur von }\widetilde{\mathcal{C}}_N(\theta)\text{ eine Weil-kompatible Grenzform?}}
$$

Konkrete Teilfragen:
1. Welche Singularserienkorrekturen tragen \(\widetilde{\mathcal{C}}_N(\theta)\) bei festen Primpaaren \((p,q)\) bei?
2. Wie verhält sich die renormierte Dichte an der Selbstdual-Skala \(\theta = 1/2\)?
3. Kann die explizite Formel die Feinstruktur von \(\widetilde{\mathcal{C}}_N\) in Nullstellenterme übersetzen?

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(\mathcal{C}_N(\theta) \sim M_N^{-\theta}\) (PNT-Heuristik) | \(\warning[M]\) |
| (B) | \(\widetilde{\mathcal{C}}_N = T \cdot \mathcal{C}_N \sim 1\) (Renormierung) | \(\checkmark[M]\) (Def.) |
| (C) | \(\mathcal{D}_N \sim \log M_N / M_N\) | \(\checkmark/\warning[M]\) |
| (D) | \(\mathcal{C}_N/\mathcal{D}_N \sim M_N^{1-\theta}/\log M_N \to \infty\) | \(\warning[M]\) |
| (E) | Kein inneres \(\theta^*\) auf Massenniveau | \(\checkmark/\warning[M]\) |
| (F) | Feinstruktur \(\widetilde{\mathcal{C}}_N\) und Weil-Grenzform | \(?[O]\) |

---

## Verweise

- NEU-97: Skalenleiter \(T = M_N^\theta\); \(T_c = \sqrt{M_N}\); \(T_0 = \log^2 M_N\)
- NEU-95: Fensterpflicht; Autokorrelationsexpansion
- NEU-92: Diagonalmasse \(\mu_N\) (Vergleich mit \(\mathcal{D}_N\))
- Goldston & Y\u0131ld\u0131r\u0131m: *Higher correlations of divisor sums* (Paarstatistik in kurzen Intervallen)
- Selberg: *Lectures on sieves* (logarithmische Mittelwerts\u00e4tze)
- Hardy & Littlewood: *Some problems of Partitio Numerorum* (Singul\u00e4rserien)
- Iwaniec & Kowalski: *Analytic Number Theory*, Kap. 5 (Mittelwerts\u00e4tze)
