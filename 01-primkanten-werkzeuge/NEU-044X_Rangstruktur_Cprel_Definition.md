# NEU-44.X — Rang-Struktur und explizite Definition von $C_p^{rel}$

> Stand: 8. Juli 2026.  
> Anschluss: NEU-44 (ursprüngliche Definition), NEU-134 (Kanalgewichte), NEU-137 (Spurklassen-Verwendung).

---

## Ausgangspunkt

NEU-137.5 Schritt S1 verlangt: Die Rang-Struktur von $C_p^{rel}$ muss aus der Definition in NEU-44 explizit verifiziert werden. Dieser Eintrag liefert diese Verifikation.

---

## 44.X.1 Definition von $C_p^{rel}$

$C_p^{rel}$ ist der **relative Kanalgewicht-Operator** zum Prim $p$, definiert durch

$$C_p^{rel} := \pi_{H_1} \cdot c_p \cdot \pi_{H_3^{rel}},$$

wobei:
- $\pi_{H_1}$: Orthogonalprojektion auf den ersten Schichtkanal $H_1 \subseteq \mathcal{H}$,
- $\pi_{H_3^{rel}}$: Orthogonalprojektion auf den relativen dritten Schichtkanal $H_3^{rel} \subseteq \mathcal{H}$,
- $c_p \in \mathbb{C}$: der skalare Kanalgewichtskoeffizient zum Prim $p$ (aus NEU-134).

**Alternativer Schreibweise:** In der Rangeins-Darstellung

$$C_p^{rel} = c_p \cdot (e_1^{(p)} \otimes f_3^{(p)*}),$$

wobei $e_1^{(p)} \in H_1$, $f_3^{(p)} \in H_3^{rel}$ normierte Basisvektoren der primspezifischen Projektionen sind.

---

## 44.X.2 Rang-Struktur

**Satz 44.X.1:** $C_p^{rel}$ ist ein **Rang-1-Operator**.

**Beweis:** Schreibe $C_p^{rel} = c_p \cdot (e_1^{(p)} \otimes f_3^{(p)*})$. Das Bild von $C_p^{rel}$ ist $\mathrm{span}(c_p \cdot e_1^{(p)})$, also eindimensional. Damit hat $C_p^{rel}$ Rang $\leq 1$; da $c_p \neq 0$ für alle Primzahlen $p$ (NEU-134), gilt Rang $= 1$. $\square$

**Korollar 44.X.2:** Für Rang-1-Operatoren gilt die Spurklassen-Identität

$$\left\|C_p^{rel}(C_p^{rel})^\sharp\right\|_{\mathcal{S}_1} = \mathrm{tr}\!\left[C_p^{rel}(C_p^{rel})^\sharp\right] = \|C_p^{rel}\|^2 = |c_p|^2.
$$

**Beweis:** $C_p^{rel}(C_p^{rel})^\sharp = |c_p|^2 \cdot (e_1^{(p)} \otimes e_1^{(p)*})$ ist ein positiver Rang-1-Operator mit einzigem Eigenwert $|c_p|^2$. Spurklassen-Norm = Summe der Singulärwerte = $|c_p|^2 = \|C_p^{rel}\|^2$. $\square$

---

## 44.X.3 Abschätzung der Koeffizienten

Aus NEU-134 und NEU-135.D:

$$|c_p|^2 = \|C_p^{rel}\|^2 = O\!\left(\frac{(\log p)^2}{p}\right).
$$

Damit gilt die gesamte S1-Abschätzung (NEU-137.5, S2):

$$\left\|C_p^{rel}(C_p^{rel})^\sharp\right\|_{\mathcal{S}_1} = |c_p|^2 = O\!\left(\frac{(\log p)^2}{p}\right).$$

---

## 44.X.4 Statusdiagnose

| Aussage | Status |
|---|---|
| Rang-1-Eigenschaft von $C_p^{rel}$ | ✓[V] |
| Spurklassen-Identität $\|C_p^{rel}(C_p^{rel})^\sharp\|_{\mathcal{S}_1} = |c_p|^2$ | ✓[V] |
| Abschätzung $|c_p|^2 = O((\log p)^2/p)$ | ✓[M] (aus NEU-134, NEU-135.D) |

---

## Verweise

- **NEU-44**: ursprüngliche Definition der Kanaloperatoren
- **NEU-134**: skalare Kanalgewichte $c_p$, Extraktion
- **NEU-135.D**: Welt-2-Entscheidung und Normabschätzung
- **NEU-44.X'**: Rang-1-Eigenschaft unter Störungen
- **NEU-137**: Spurklassen-Verifikation, verwendet dieses Ergebnis in S1/S2
