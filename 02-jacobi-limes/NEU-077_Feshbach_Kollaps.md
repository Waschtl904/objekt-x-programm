# NEU-77 — Feshbach-Kollaps und exakte Trunkierungsidentität

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-76 (erweiterter Hilbertraum, No-Go BC-*-Darstellung)  
**Nächste Nummer:** NEU-78

---

## Ausgangspunkt

Aus NEU-76 liegt der erweiterte Hilbertraum

$$
\mathcal{H}_N = \ell^2(I_N) \otimes \ell^2(S_N)
$$

mit Orthonormalbasis $(\eta_{r,n})_{r \in I_N,\, n \in S_N}$ vor, wobei $S_N \subset \mathbb{N}^\times$ eine **endliche** Labelmenge ist.

Die Operatoren auf $\mathcal{H}_N$ sind definiert durch:

$$
R_N \, \eta_{r,n} = r \, \eta_{r,n}
$$

$$
D_{BC,N} \, \eta_{r,n} = \log(n) \, \eta_{r,n}
$$

$$
S_N \, \eta_{r,n} =
\begin{cases}
\eta_{r+n,\, n}, & r+n \in I_N, \\
0, & r+n \notin I_N.
\end{cases}
$$

Dann gilt unmittelbar (bereits aus NEU-76):

$$
S_N R_N D_{BC,N} \, \eta_{r,n} = r \log(n) \, \eta_{r+n,\,n}
\quad \text{(mit Randbeschnitt } r+n \in I_N\text{).}
$$

---

## Kollapsoperator (unnormalisiert)

Definiere den **unnormalisierten Kollapsoperator**

$$
\Pi_N : \mathcal{H}_N \to \ell^2(I_N)
$$

durch

$$
\Pi_N \, \eta_{r,n} = \delta_r.
$$

Sein adjungierter Operator ist:

$$
\Pi_N^* \, \delta_r = \sum_{n \in S_N} \eta_{r,n}.
$$

### Wichtige Bemerkung: $\Pi_N$ ist keine orthogonale Projektion

Es gilt:

$$
\Pi_N \Pi_N^* = |S_N| \cdot I_{\ell^2(I_N)}.
$$

Der Ausdruck $\Pi_N S_N R_N D_{BC,N} \Pi_N^*$ ist daher eine
**unnormalisierte Feshbach-Kollapskompression**, nicht eine orthogonale
Projektion. Dies ist der entscheidende Präzisionspunkt gegenüber einer
orthogonalen Feshbach-Projektion.

---

## Exakte Kollaps-Identität

Für $\delta_r \in \ell^2(I_N)$ rechnet man:

$$
\Pi_N^* \, \delta_r = \sum_{n \in S_N} \eta_{r,n},
$$

$$
S_N R_N D_{BC,N} \, \Pi_N^* \, \delta_r
= \sum_{n \in S_N} r \log(n) \, \eta_{r+n,\,n}
\quad (\text{mit Randbeschnitt}),
$$

$$
\Pi_N S_N R_N D_{BC,N} \Pi_N^* \, \delta_r
= \sum_{\substack{n \in S_N \\ r+n \in I_N}} r \log(n) \, \delta_{r+n}.
$$

Definiert man den **getrunkierten Shift**

$$
V_n^{(N)} \delta_r =
\begin{cases}
\delta_{r+n}, & r+n \in I_N, \\
0, & r+n \notin I_N,
\end{cases}
$$

und

$$
J_N^- := \sum_{n \in S_N} \log(n) \, V_n^{(N)} R_N,
$$

so folgt **exakt** (für endliches $N$, **ohne Fehlerterm**):

$$
\boxed{\Pi_N S_N R_N D_{BC,N} \Pi_N^* = J_N^-}
$$

---

## Statusbewertung

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | $S_N$ ist partielle Isometrie (beschränkt) auf $\mathcal{H}_N$ | ✓[M] |
| (B) | $\Pi_N^*$ als unnormalisierte Inklusion liefert exakt $J_N^-$-Matrixelemente | ✓[M] |
| (C) | Gleichheit für endliches $N$ **exakt**, sofern $J_N^-$ mit gleichem Randbeschnitt $V_n^{(N)}$ definiert | ✓[M] |
| (D) | Ohne Trunkierung (ungetrunkter Shift auf größerem/unendlichem Raum): Randterme entstehen; deren Verschwinden ist **keine Operatornormaussage**, nur stark/punktweise für endlich-getragene Vektoren | ⚠[M] |
| (E) | Normierte orthogonale Feshbach-Projektion $\tilde{\Pi}_N = |S_N|^{-1/2} \Pi_N$ liefert nur $|S_N|^{-1} J_N^-$; fehlender Faktor muss mit Jacobi-/Feshbach-Normierung (NEU-62) abgestimmt werden | ⚠[M] |

---

## Was explizit **nicht** behauptet wird

- **Keine** "starke Operatornormkonvergenz" $\Pi S R D_{BC} \Pi^* \to J_N^-$:  
  Der Ausdruck "starke Operatornorm" ist kategorial inkonsistent.  
  Randterme können im Operatornormsinn normgroß bleiben.  
  Zulässig ist nur: für feste endlich-getragene Vektoren und wachsende
  Fenster $I_N$ verschwinden Randterme **punktweise/stark**,  
  sofern die Labelmenge $S_N$ kontrolliert wächst.

---

## Konsequenz für den kritischen Pfad

NEU-77 löst den **algebraischen Operator-Matching-Schritt**

$$
S R D_{BC} \leadsto J_N^-
$$

auf dem erweiterten Hilbertraum mit unnormalisiertem Kollaps **exakt** für
endliches $N$.

Der verbleibende Engpass ist **nicht mehr** die Erzeugung des
$r \log(n)$-Shiftterms, sondern:

1. **Normierung**: Abstimmung des $|S_N|$-Faktors mit der Jacobi-Limes-Normierung (NEU-62)
2. **Limeskontrolle**: Kontrolle der Feshbach-Kompression für $N \to \infty$  
   (stark/punktweise, nicht Operatornorm)
3. **Mangoldt-Extraktion**: $\log n \to \Lambda(n)$ via Primsektor-Projektion (NEU-67/75)  
   — separater arithmetischer Schritt, unverändert ⚠[M]

---

## Verweise

- NEU-73: $J_N^- = \sum_{n} \log(n) V_n R$ (Operatorstruktur)
- NEU-74: $V_n \sim M_{e_n}$, nicht $\mu_n$
- NEU-75: $\Theta = M_{e_n} \partial_\theta \delta_{BC}$ auf Monomen
- NEU-76: Erweiterter Hilbertraum $\mathcal{H}_N$; No-Go BC-$*$-Darstellung
- NEU-62: Normalisierungsrigidität, Jacobi-Limes (Normierungsabstimmung nötig)
- Reed & Simon II/IV: Partielle Isometrien, Feshbach-Projektion
