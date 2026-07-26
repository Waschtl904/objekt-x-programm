# NEU-128.A — Rückleseprotokoll NEU-41: Klasse-B-Prüfung Σ_N(β)

**Stand:** 6. Juli 2026
**Typ:** Rückleseprotokoll (kein Beweisblatt, kein Konstruktionsblatt)
**Anschluss:** NEU-41 (Kanonischer Kopplungsoperator C_N), NEU-127 (Triage, Klasse A/B)
**Ziel:** Prüfung von Σ_N(β) unter den drei Fragen aus NEU-127.5

---

## Warnsatz

$$\boxed{\Sigma_N(\beta)\ \text{ist Klasse-B-bestätigt, aber noch kein}\ W_N.}$$

---

## 128.A.0 — Prüfrahmen

NEU-127.5 stellt drei konkrete Fragen für NEU-41:

1. **Kanonizität:** Ist Σ_N(β) kanonisch, oder hängt es von Hilfsentscheidungen ab?
2. **Interpretationsebene:** Schur-Komplement oder Energie-/Quadratikform?
3. **Faktorisierung (entscheidend):** Gibt es Σ_N(β) = A_N^* A_N oder W_N^{1/2} B W_N^{1/2}?

---

## 128.A.1 — Frage 1: Kanonizität

**Befund: Relativ zur Hebung kanonisch — Hebungsunabhängigkeit offen.**

NEU-41 §3 stellt ausdrücklich eine Wohlbestimmtheitsbedingung auf (41.4):

$$\widehat\varepsilon_p \sim \widehat\varepsilon_p' \;\Longrightarrow\; C_p C_p^\# = C_p' C_p'^\# \quad\text{im }Wres\text{-Quotienten.}$$

Status dieser Bedingung in NEU-41: **❓[O]** (nicht bewiesen).

Konsequenz: $C_p C_p^\#$ und damit

$$\Sigma_N(\beta) = \sum_{p \leq N}(1-p^{-\beta})^{-1} C_p C_p^\#$$

sind **relativ zur gewählten Fourier-geladenen Hebung $\widehat\varepsilon_p$** kanonisch definiert,
aber noch **nicht hebungsunabhängig** gesichert.

**Status:** ❓[O] für volle Kanonizität.

---

## 128.A.2 — Frage 2: Interpretationsebene

**Befund: Primär Weyl-Funktion / Schur-Komplement — Energieformlesart implizit, nicht ausgearbeitet.**

NEU-41 §6 definiert die Feshbach-Weyl-Funktion des Primkanals:

$$M_p(s) = \langle \Psi_p, S_N(s,s)^{-1} \Psi_p \rangle_{Wres}$$

Das ist eine resolventenartige Größe, keine Bilinearform. Σ_N(β) erscheint als gewichtete
Summe von Rang-eins-Projektoren, aber NEU-41 interpretiert diese Summe nicht explizit als
Quadratik- oder Stabilitätsform. Die Energieformlesart ist **implizit angelegt, aber nicht
ausgearbeitet**.

**Status:** ⚠[M] — Interpretationsebene offen.

---

## 128.A.3 — Frage 3: Faktorisierung

**Befund: Explizite Rang-1-Gram-Faktorisierung gesichert — das ist der entscheidende Klasse-B-Fund.**

NEU-41 §5, Gleichung (41.9):

$$\boxed{C_p C_p^\# x = \Psi_p \langle \Psi_p, x \rangle_{Wres}}$$

$C_p C_p^\#$ ist der **Rang-eins-Projektor** auf den $Wres$-zyklischen Vektor $\Psi_p$.
Damit gilt:

$$\Sigma_N(\beta)
= \sum_{p \leq N}(1-p^{-\beta})^{-1}\,\underbrace{C_p C_p^\#}_{\text{Rang-1-Gram},\;\geq 0}
= C_N\,E_N(\beta)^{-1}\,C_N^\#$$

mit positiven Euler-Gewichten $(1-p^{-\beta})^{-1}$.

Das ist eine Gram-Faktorisierung mit arithmetischen Gewichten. Die Positivität stammt
inhaltlich aus der Feshbach-Elimination — nicht bloß aus einer Hilbertraumidentität.

**Status:** ✓[M] auf dem nichtausgearteten $Wres$-Sektor.

**Richtungshinweis:** Die Faktorisierung ist $C_p C_p^\#$, nicht $C_p^\# C_p$.
Der Unterschied bestimmt, auf welchem Raum Σ_N(β) als Metrik wirkt:
$C_p C_p^\#$ wirkt auf $\mathcal{H}_{J,N}$, $C_p^\# C_p$ auf $\mathfrak{p}_N$.
Für die $W_N$-Frage ist die Prä-Lanczos-Ebene relevant — welcher Raum das genau ist,
bleibt zu klären.

---

## 128.A.4 — Neue Obstruktion aus NEU-41 §7

NEU-41 §7 (Satz 41.3) liefert eine zusätzliche strukturelle Grenze:

$$\boxed{M_p^{raw}(s) = \langle \Psi_p, (s - D_N^-)^{-1}\Psi_p\rangle \text{ ist rational in } s.}$$

Aber $1 - p^{-s} = 1 - e^{-s \log p}$ ist keine rationale Funktion. Daher kann die
Zielbedingung $M_p(s) = 1 - p^{-s}$ für endliche Jacobi-Trunkierung **keine holomorphe
Identität** sein. Sie ist nur asymptotisch erreichbar (Padé-/Laplace-Realisierung, NEU-41 §8/9).

**Status:** ✓[M] als Negativresultat, ❓[O] als asymptotisches Beweisziel.

---

## 128.A.5 — Gesamtbefund

| Prüfpunkt | Befund | Status |
|---|---|---|
| Kanonizität von Σ_N(β) | Relativ zur Hebung kanonisch; Hebungsunabhängigkeit (41.4) offen | ❓[O] |
| Interpretationsebene | Weyl-Funktion/Schur-Komplement; Energieformlesart implizit | ⚠[M] |
| Faktorisierung | **Explizit:** $C_p C_p^\# = \Psi_p \langle \Psi_p, \cdot\rangle_{Wres}$, Rang-1-Gram mit Euler-Gewichten | ✓[M] |
| Klasse-B-Bestätigung | Positivität aus Feshbach-Elimination, nicht nur formal | ✓[M] |
| W_N-Tauglichkeit: Wirkungsebene | $C_p C_p^\#$ wirkt auf $\mathcal{H}_{J,N}$, Prä-Lanczos-Verortung unklar | ⚠[M] |
| W_N-Tauglichkeit: Kanonizität | Hebungsunabhängigkeit offen | ❓[O] |
| W_N-Tauglichkeit: Krylov-Schicht-Sensitivität | Noch nicht analysiert | ❓[O] |
| Endlich-rationale Weyl-Funktion vs. $1-p^{-s}$ | Nur asymptotisch; exakte Identität unmöglich (Satz 41.3) | ✓[M] Negativresultat |

### Kernstatus

$$\boxed{\Sigma_N(\beta):\ \checkmark[M]\ \text{als Gram-/Selbstenergieform}}$$

$$\boxed{\Sigma_N(\beta):\ {\large ?}[O]\ \text{als kanonische } W_N\text{-Metrik}}$$

Die vier offenen Punkte, die Σ_N(β) noch vom Status „fertiges $W_N$" trennen:

1. **Hebungsunabhängigkeit** (41.4): ❓[O]
2. **Wirkungsebene** $\mathcal{H}_{J,N}$ vs. echte Prä-Lanczos-Feshbach-Ebene: ❓[O]
3. **Krylov-Schicht-Sensitivität**: noch nicht analysiert — ❓[O]
4. **Endlich-rationale Weyl-Funktion vs. $1-p^{-s}$**: nur asymptotisch offen — ❓[O]

---

## 128.A.F — Fazit und Entscheidungspfad

$$\boxed{\text{NEU-41 bestätigt Klasse B, aber verschiebt die } W_N\text{-Frage nach NEU-44.}}$$

- Σ_N(β) ist als **positive Rang-1-Gram-Selbstenergie mit Euler-Gewichten** gesichert. ✓[M]
- Die Positivität stammt inhaltlich aus der Feshbach-Elimination — das ist der qualitative
  Unterschied zu Klasse A. ✓[M]
- Σ_N(β) ist jedoch **noch kein fertiges $W_N$**: Hebungsunabhängigkeit, Wirkungsebene
  und Krylov-Schicht-Sensitivität sind ungeklärt.

**Nächster Schritt:** NEU-44 unter Klasse-B-Prüfung:
relative Weil-Paarung / Primkantenstruktur als $W_N$-Kandidat.

**Gesamtstatus:** ❓[O] — Klasse-B-Kandidat bestätigt, $W_N$-Entscheidung offen.
