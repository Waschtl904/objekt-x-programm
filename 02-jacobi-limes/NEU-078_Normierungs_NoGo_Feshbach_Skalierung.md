# NEU-78 — Normierungs-No-Go und Jacobi-kompatible Feshbach-Skalierung

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-77 (Feshbach-Kollapsidentität exakt; unnormalisierter Kollaps)  
**Nächste Nummer:** NEU-79

---

## Ausgangspunkt

Aus NEU-77 ist gesichert:

$$
\Pi_N S_N R_N D_{BC,N} \Pi_N^* = J_N^-  \qquad \checkmark[M]
$$

mit dem **unnormalisierten** Kollapsoperator \( \Pi_N \eta_{r,n} = \delta_r \),  
der die Eigenschaft \( \Pi_N \Pi_N^* = |S_N| \cdot I \) (nicht \( I \)) hat.

Der neue Engpass: Welche Skalierung macht diesen unnormalisierten Kollaps  
kompatibel mit dem späteren **Jacobi-/Feshbach-Limes** (NEU-59–62)?

---

## (A) Unnormalisierter Kollaps — Wiederholung

$$
\Pi_N S_N R_N D_{BC,N} \Pi_N^* = J_N^- \qquad \checkmark[M]
$$

Exakt für endliches \( N \), kein Fehlerterm (NEU-77/B–C).

---

## (B) Isometrischer (demokratisch normierter) Kollaps

Ersetzt man \( \Pi_N \) durch die isometrische Einbettung

$$
U_N \delta_r = |S_N|^{-1/2} \sum_{n \in S_N} \eta_{r,n},
\qquad U_N^* U_N = I_{\ell^2(I_N)},
$$

so gilt:

$$
U_N^* S_N R_N D_{BC,N} U_N\, \delta_r
= |S_N|^{-1} \sum_{n \in S_N} r\log(n)\,\delta_{r+n}
= |S_N|^{-1} J_N^- \delta_r.
$$

Also:

$$
U_N^* S_N R_N D_{BC,N} U_N = |S_N|^{-1} J_N^- \qquad \checkmark[M]
$$

Der fehlende Faktor \( |S_N| \) ist der direkte Preis der Normierung.

---

## (C) Allgemein gewichteter Kollaps

Für eine beliebige isometrische Einbettung

$$
U_N \delta_r = \sum_{n \in S_N} a_{n,N}\, \eta_{r,n},
\qquad \sum_{n \in S_N} |a_{n,N}|^2 = 1,
$$

ergibt sich:

$$
U_N^* S_N R_N D_{BC,N} U_N\, \delta_r
= \sum_{n \in S_N} |a_{n,N}|^2\, r\log(n)\,\delta_{r+n}.
$$

Das ist eine **gewichtete Mittelung** der \( n \)-Kanäle mit Gewichten \( |a_{n,N}|^2 \),
nicht die ungewichtete Summe \( J_N^- \).

---

## (D) No-Go: Isometrische Einbettung erzeugt nie \( J_N^- \)

**Lemma (Normierungs-No-Go):**  
Für \( |S_N| > 1 \) gibt es keine isometrische Einbettung  
\( U_N : \ell^2(I_N) \to \mathcal{H}_N \) mit

$$
U_N^* S_N R_N D_{BC,N} U_N = J_N^-.
$$

**Beweis:**  
Die Einbettungsbedingung \( \sum_{n} |a_{n,N}|^2 = 1 \) erzwingt \( |a_{n,N}|^2 < 1 \)  
für alle \( n \) (da \( |S_N| > 1 \)).  
Um die ungewichtete Summe \( J_N^- \) zu erhalten, bräuchte man \( |a_{n,N}|^2 = 1 \)  
für alle \( n \in S_N \) gleichzeitig — Widerspruch zur Normierungsbedingung. \( \square \)

**Status: ✓[M]**

---

## (E) Offener Engpass: Jacobi-kompatible Skalierung

Drei mögliche Auflösungen, alle noch offen:

### Option 1: \( J_N^- \) als unnormalisierte Wechselwirkungsmatrix

\( J_N^- \) wird **nicht** als normierter Operator, sondern als rohe  
Wechselwirkungsmatrix im Jacobi-Limes verstanden. Die Normierung  
wird extern durch die Jacobi-Skalenfolge aus NEU-62 übernommen.  
Kompatibilitätsbedingung: Der \( |S_N| \)-Faktor muss in der  
Jacobi-Normierungssequenz absorbiert werden können.

### Option 2: Kanalabhängige Renormierung

Ersetzt man \( J_N^- \) durch den **renormierten Operator**

$$
\widetilde{J}_N^- = |S_N|^{-1} J_N^-,
$$

so entsteht \( \widetilde{J}_N^- \) exakt aus isometrischem Kollaps (B).  
Frage: Ist der Jacobi-Limes von \( \widetilde{J}_N^- \) äquivalent zu dem von \( J_N^- \),  
oder ändert sich das Spektrum?

### Option 3: Direkter Kopplungsfaktor \( |S_N| \)

Man arbeitet mit

$$
\Pi_N = |S_N|^{1/2} U_N
$$

explizit, und verfolgt den \( |S_N| \)-Faktor durch den gesamten  
Jacobi-/Feshbach-Limes. Die Frage ist dann, ob \( |S_N| \to \infty \)  
(für \( N \to \infty \), \( S_N = \{n \leq N\} \)) den Limes kontrollierbar lässt.

**Status aller drei Optionen: ❓[O]**

---

## Statusbewertung

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | Unnormalisierter Kollaps \( \Pi_N \) liefert \( J_N^- \) exakt | ✓[M] |
| (B) | Demokratisch normierter Kollaps \( U_N \) liefert \( |S_N|^{-1} J_N^- \) | ✓[M] |
| (C) | Allg. isometrischer Kollaps liefert gewichtete Mittelung von \( J_N^- \) | ✓[M] |
| (D) | **No-Go:** Kein isometrischer Kollaps erzeugt die volle Summe \( J_N^- \) | ✓[M] |
| (E) | Jacobi-kompatible Skalierung (Optionen 1–3) | ❓[O] |

---

## Sprachliche Präzisierung (aus NEU-77-Diskussion)

In kritischer_pfad_aktuell.md steht korrekt \( |S_N| \)-Faktor  
(Kardinalität der Labelmenge), nicht \( \|S_N\| \) (Operatornorm).  
Die korrekte Relation ist:

$$
\|\Pi_N\|^2 = |S_N|, \qquad \Pi_N \Pi_N^* = |S_N| \cdot I.
$$

---

## Konsequenz für den kritischen Pfad

NEU-78 zeigt:
- Das **algebraische Erzeugungsproblem** ist gelöst (NEU-77).
- Das **metrische Kompatibilitätsproblem** ist der neue Flaschenhals:
  Wie geht \( J_N^- \) als unnormalisierte Matrix in den Jacobi-Limes ein?
- Die Antwort entscheidet, ob \( J_N^- \) direkt oder nach Renormierung  
  \( \widetilde{J}_N^- = |S_N|^{-1} J_N^- \) die relevante Jacobi-Tridiagonalmatrix ist.

---

## Verweise

- NEU-62: Normalisierungsrigidität, Jacobi-Limes (externer Normierungsrahmen)
- NEU-77: Exakte Kollapsidentität, unnormalisierter \( \Pi_N \)
- NEU-59: Jacobi-Limes, Spektralmass (Zielrahmen für Skalierung)
- Reed & Simon II: Isometrische Einbettungen, partielle Isometrien
