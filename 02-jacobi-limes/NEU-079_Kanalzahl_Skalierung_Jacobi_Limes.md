# NEU-79 — Kanalzahl-Skalierung und Jacobi-kompatibler Feshbach-Limes

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-78 (Normierungs-No-Go; isometrischer Kollaps liefert \(\kappa_N^{-1}J_N^-\))  
**Nächste Nummer:** NEU-80

---

## Notationskorrektur (ab NEU-79 verbindlich)

Ab diesem Eintrag wird die Doppelbelegung von \(S_N\) aufgelöst:

$$
\Sigma_N := \text{endliche Labelmenge (Indexmenge der }n\text{-Kanäle)}
$$

$$
\kappa_N := |\Sigma_N| \quad \text{(Kanalzahl, skalare Kardinalität)}
$$

$$
\mathsf{S}_N := \text{getrunkter Shift-Operator auf }\mathcal{H}_N
\quad (\|\mathsf{S}_N\| = 1)
$$

**Korrekte Schreibweise der NEU-78-Identität:**

$$
U_N^* \mathsf{S}_N R_N D_{BC,N} U_N = \kappa_N^{-1} J_N^-
$$

(nicht \(\|\mathsf{S}_N\|^{-1} J_N^-\), denn \(\|\mathsf{S}_N\| = 1\); der Faktor kommt ausschließlich von \(\kappa_N = |\Sigma_N|\)).

---

## Ausgangspunkt

Aus NEU-77/78 liegt die exakte endliche Identität vor:

$$
\Pi_N \mathsf{S}_N R_N D_{BC,N} \Pi_N^* = J_N^-
\qquad \checkmark[M]
$$

mit dem unnormalisierten Kollapsoperator \(\Pi_N\), der erfüllt:

$$
\Pi_N \Pi_N^* = \kappa_N \cdot I, \qquad \|\Pi_N\|^2 = \kappa_N.
$$

Die normierte isometrische Einbettung ist

$$
U_N := \kappa_N^{-1/2} \Pi_N^*, \qquad U_N^* U_N = I_{\ell^2(I_N)},
$$

und es gilt exakt:

$$
U_N^* \mathsf{S}_N R_N D_{BC,N} U_N = \kappa_N^{-1} J_N^-.
$$

Damit:

$$
\boxed{J_N^- = \kappa_N \cdot U_N^* \mathsf{S}_N R_N D_{BC,N} U_N.}
$$

Der Unterschied zwischen unnormalisiertem und normiertem Kollaps ist **rein skalar**: der Faktor \(\kappa_N\).

---

## Kernproblem: Asymptotik von \(\gamma_N\)

Wenn die Jacobi-Normierung aus NEU-62 durch eine Skalenfolge \((a_N)\) gegeben ist, lautet die effektiv im Jacobi-Limes relevante Größe:

$$
\gamma_N := a_N \kappa_N.
$$

Denn der normierte Feshbach-Beitrag auf der Jacobi-Skala ist:

$$
a_N J_N^- = \gamma_N \cdot U_N^* \mathsf{S}_N R_N D_{BC,N} U_N.
$$

Der analytische Flaschenhals reduziert sich damit auf die **skalare Asymptotik**:

$$
\boxed{\gamma_N = a_N \kappa_N \quad \overset{?}{\longrightarrow} \quad \gamma \in (0, \infty).}
$$

---

## Drei Fälle

### Fall 1: \(\gamma_N \to \gamma \in (0, \infty)\)

Dann hat der normierte Feshbach-Kollaps eine nichttriviale endliche Kopplungsstärke:

$$
a_N J_N^- \sim \gamma \cdot U_N^* \mathsf{S}_N R_N D_{BC,N} U_N.
$$

Dies ist der **Jacobi-kompatible Fall** — der Limes existiert mit endlicher Gewichtung.  
**Status: Zielfall ⚠[M]**

### Fall 2: \(\gamma_N \to 0\)

Der Feshbach-Beitrag verschwindet im Limes. Der arithmetische Operator ist auf der Jacobi-Skala zu schwach normiert.  
**Status: degenerierter Limes ✗[M] (falls tatsächlich eintretend)**

### Fall 3: \(\gamma_N \to \infty\)

Die effektive Kopplung divergiert. Entweder muss \(a_N\) angepasst oder der Operator mit \(\kappa_N^{-1}\) zusätzlich renormiert werden.  
**Status: Überkopplung / Renormierungsbedarf ⚠[M]**

---

## Asymptotik von \(\kappa_N\) je nach Labelmenge

| Labelmenge \(\Sigma_N\) | \(\kappa_N\) | Asymptotik |
|---|---|---|
| \(\{1, \ldots, N\}\) | \(N\) | \(\kappa_N = N\) |
| \(\{p \leq N \text{ prim}\}\) | \(\pi(N)\) | \(\kappa_N \sim N/\log N\) (Primzahlsatz) |
| Primpotenzen \(\{p^k \leq N\}\) | \(\sum_{p} \lfloor \log_p N \rfloor\) | \(\sim N/\log N\) (dominiert von Primzahlen) |

Die Wahl von \(\Sigma_N\) muss mit der späteren Mangoldt-/Primsektor-Extraktion (NEU-67/75) abgestimmt werden.  
Für die Mangoldt-Funktion \(\Lambda(n)\) sind Primpotenzen natürlich; für \(\log(n)\) ist die volle Labelmenge \(\{1,\ldots,N\}\) natürlich.

---

## Statusbewertung

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(J_N^- = \kappa_N \cdot U_N^* \mathsf{S}_N R_N D_{BC,N} U_N\) (skalar-exakt) | ✓[M] |
| (B) | \(\kappa_N\)-Asymptotik je nach \(\Sigma_N\) bestimmbar | ✓[M] |
| (C) | Wahl von \(\Sigma_N\) muss mit Mangoldt-/Primsektor-Extraktion abgestimmt sein | ⚠[M] |
| (D) | \(a_N\) aus NEU-62 exakt einsetzen und \(\gamma_N = a_N \kappa_N\) bestimmen | ❓[O] |
| (E) | Asymptotischer Fall (1, 2 oder 3) entscheidet über Jacobi-Kompatibilität | ❓[O] |

---

## Erste konkrete Prüfgleichung

Sobald \(a_N\) aus NEU-62 explizit vorliegt:

$$
\boxed{a_N \kappa_N \overset{?}{\to} \gamma}
$$

entscheidet sich, ob der unnormalisierte Kollaps (Option 3 aus NEU-78) direkt  
Jacobi-kompatibel ist oder ob eine zusätzliche Renormierung nötig wird.

---

## Konsequenz für den kritischen Pfad

NEU-79 reduziert den metrischen Flaschenhals auf eine **skalare Asymptotik**.  
Es müssen keine neuen Operatoren gebaut werden. Die offene Frage ist:

> Ist die Jacobi-Normierung \(a_N\) kompatibel mit der Kanalzahl \(\kappa_N\)?

---

## Verweise

- NEU-62: Normalisierungsrigidität, Jacobi-Limes (liefert \(a_N\))
- NEU-77: Unnormalisierter Kollaps, exakte Identität
- NEU-78: Normierungs-No-Go, isometrischer Kollaps
- NEU-67/75: Mangoldt-Extraktion, Primsektor-Projektion (bestimmt optimales \(\Sigma_N\))
- NEU-59: Jacobi-Limes, Spektralmass (Zielrahmen)
