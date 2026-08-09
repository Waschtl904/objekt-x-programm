# P10 — Targeted-Reaudit: P07/NEU-091 versus P06 G-T4/G-T5

**Datum:** 9. August 2026  
**SYN-Ziel:** P10 — kondensierte No-Go-Sammlung  
**Prüfart:** `TARGETED-REAUDIT`  
**Konflikt:** P07 §1 / Statusmatrix gegen den späteren P06-Endstand G-T4/G-T5  
**Status:** **RECONCILED — P07-Determinantenwert `e^{-\gamma^2/4}` ist `SUPERSEDED`; autoritativ ist im NEU-088–90-Modell `D_N(z)\to1`.**

---

## 1. Konfliktbild

Das eingefrorene P07-SYN übernimmt aus NEU-091 die historische Aussage

\[
D_N(z)\longrightarrow e^{-\gamma^2/4}
\]

im festen-\(z\)-Regime und bezeichnet sie als gesicherten Determinanten-No-Go.

NEU-091 selbst macht ausdrücklich klar, dass dieser Wert aus NEU-089/090 stammt und auf

\[
\operatorname{Tr}(C_N(z)^2)\to\gamma^2/2
\]

beruht.

Der spätere P06-Targeted-Reaudit G-T4 prüft genau diesen NEU-090-Schritt im selben Modellscope

\[
h_r=r,\qquad M_N=N/\log N,\qquad z\text{ fest und zulässig},
\]

und widerlegt die benötigte uniforme Asymptotik. Stattdessen gilt

\[
\boxed{
T_N(z)=O_z\!\left(\frac{\log\log N}{\log N}\right)\to0.
}
\]

G-T5 korrigiert zusätzlich die historische Hilbert–Schmidt-/Selbstadjungiertheitsargumentation und erhält

\[
\|C_N(z)\|_{HS}\to0,
\qquad
\|C_N(z)\|\to0,
\qquad
\operatorname{Tr}(C_N(z)^k)\to0\quad(k\ge2).
\]

Da der lineare Term im konkreten endlichen Modell verschwindet, folgt

\[
\boxed{
\log D_N(z)\to0,
\qquad
D_N(z)\to1.
}
\]

---

## 2. Präzedenzentscheidung

Es handelt sich **nicht** um zwei verschiedene zulässige Grenzregimes, sondern um eine spätere Korrektur derselben historischen NEU-089/090-Rechnung, auf die NEU-091 und P07 §1 verweisen.

Daher gilt für die SYN-Reconciliation:

| Aussage | Endstatus |
|---|---|
| `Tr(C_N(z)^2) -> gamma^2/2` im NEU-088–90-Scaling | `×[M] / SUPERSEDED` |
| `D_N(z) -> exp(-gamma^2/4)` im selben Scaling | `×[M] / SUPERSEDED` |
| `T_N(z) -> 0` | `✓[M]` im Modellscope |
| `||C_N(z)||_HS -> 0` | `✓[M]` im Modellscope |
| `D_N(z) -> 1` | `✓[M]_{neg}` im Modellscope |
| nichttrivialer `C xi(z)`-Grenzwert aus genau dieser Skalierung | ausgeschlossen im Modellscope |
| allgemeiner Feshbach-/Fredholm-/Determinanten-No-Go | **nicht bewiesen** |

---

## 3. P10-Klassifikation

Für P10 darf nur folgende konservative Aussage als Kandidaten-No-Go übernommen werden:

> **Konkreter NEU-088–90-Determinantenpfad.** Für `h_r=r`, `M_N=N/log N` und festes zulässiges `z` kollabieren die relativen Schleifenterme; insbesondere `D_N(z)->1`. Diese konkrete Mangoldt-/Orbit-/Resolvent-Skalierung kann daher keinen nichttrivialen `C xi(z)`-Grenzwert erzeugen.

Ausdrücklich **nicht** ausgeschlossen sind:

- andere Skalierungen oder Renormierungen relativer Determinanten;
- ein globaler Transfer `V^*(D_rel-z)^{-1}V` nach intrinsischer Quellkonstruktion;
- `det_2`-/Weil-Realisierungen in anderer Hilbertisierung;
- andere Feshbach-/Fredholm-Architekturen.

Zielklassifikation: `P10-NOGO` als **Kandidaten-No-Go / modell- und skalenspezifisch**.

Die historische Konstante `e^{-gamma^2/4}` gehört dagegen ausschließlich nach `SUPERSEDED-only`.

---

## 4. Konsequenz für den eingefrorenen P07-Stand

P07 §1 und die zugehörige Statusmatrix enthalten damit einen konkreten, später auditierten Gegenbefund. Die Freeze-Regel erlaubt in diesem Fall eine eng begrenzte Wiederöffnung.

Erforderliche lokale Reparatur:

1. P07 Markdown: `D_N(z)->e^{-gamma^2/4}` durch den reconciliierten Nullschleifen-/`D_N(z)->1`-Befund ersetzen;
2. P07 LaTeX synchron korrigieren;
3. keine historischen NEU-Dateien umschreiben;
4. keine Aussage zu einem universellen Feshbach-No-Go hochstufen.

Bis diese lokale Synchronisation ausgeführt ist, ist dieser Audit die autoritative Präzedenz für P10.

---

## 5. Endurteil

\[
\boxed{
\text{P07/NEU-091-Konstante `e^{-\gamma^2/4}` SUPERSEDED;}
\quad
D_N(z)\to1\text{ ist der korrigierte konkrete No-Go-Befund.}
}
\]

**Kein universeller Determinanten- oder Feshbach-No-Go.**