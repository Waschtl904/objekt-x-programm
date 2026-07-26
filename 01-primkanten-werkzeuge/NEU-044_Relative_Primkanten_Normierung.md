# NEU-44 — Relative Primkanten-Normierung

> Stand: 12. Juli 2026.
> Typ: **Kanonische Quellenrekonstruktion** (Grundlagenblatt, kein mathematisches Resultat).
> Zweck: Materialisierung der implizit verwendeten Grunddefinitionen und Normkonventionen, auf die NEU-134, NEU-135.D sowie die Rekonstruktionsblätter NEU-44.X / NEU-44.X' / NEU-44.R Bezug nehmen.

> **Epistemische Warnung:** Dieses Blatt erhebt keinen Anspruch, ein historisches Originaldokument wiederzugeben. Es dient als **kanonischer Referenzknoten** innerhalb des Repository-DAG. Alle nachgelagerten Blätter (NEU-134, NEU-135.D, NEU-44.X ff., NEU-144–152) importieren ihre Grunddefinitionen von hier.

---

## DAG-Position

```
NEU-44
  └─► NEU-134   (Kanalgewichte, Formel für |c_p|²)
        └─► NEU-135.D  (Welt-2-Entscheidung, Normkonvention)
              └─► NEU-144  (primdiagonale Observable R)
                    └─► NEU-151  (Typaudit)
                          └─► NEU-152  (Nichtentartung)
```

Parallelimporte: NEU-44.X, NEU-44.X', NEU-44.R, NEU-137.

---

## 44.1 — Grundraum und Hebungsstruktur

Der **relative Graphraum** ist

$$W_{\mathrm{res,rel}} = \bigoplus_{(m,p)}^{\perp} H_{m \xrightarrow{p} pm},$$

wobei die Summe über alle Primzahlen $p$ und Kanalindizes $m$ läuft und die Teilräume $H_{m \to pm}$ paarweise orthogonal sind (Edge-Label-Struktur, NEU-143).

Die **Primkanten-Hebung** zu einer Primzahl $p$ ist der Vektor

$$\widetilde{\Psi}_p \;\in\; W_{\mathrm{res,rel}},$$

definiert durch die Fourier-Lifting-Konstruktion aus NEU-41:

$$\widetilde{\Psi}_p = -\sum_{u \neq 0}\sum_{s,m} a_{p,u}\,\ell_{s,m}\,u\,s\,\log p\;
E^{\mathrm{rel}}_{u+ps;\,m \xrightarrow{p} pm},$$

wobei:
- $a_{p,u} \in \mathbb{C}$: Fourier-Koeffizienten der Primkanten-Hebung (NEU-41),
- $\ell_{s,m} \in \mathbb{R}$: Schleifenlängengewichte,
- $E^{\mathrm{rel}}_{u+ps;\,m \to pm}$: normierte Basisvektoren von $W_{\mathrm{res,rel}}$ (kantendiagonal).

---

## 44.2 — Normkonvention für $\varepsilon_p$ (**Welt-2-Festlegung**)

Der **Eingabevektor** $\varepsilon_p$ ist der normierte Standardbasisvektor des primspezifischen Eingangskanals:

$$\varepsilon_p \;:=\; f_3^{(p)} \;\in\; H_3^{\mathrm{rel}}, \qquad \|\varepsilon_p\|_{\mathfrak{p}_N} = 1.$$

**Welt-2-Entscheidung (NEU-135.D):** Im gesamten Katalog gilt die normierte Konvention — **Fall A** aus NEU-134 §134.0:

$$\boxed{\|\varepsilon_p\| = 1.}$$

Konsequenz: Es gilt direkt

$$|c_p|^2 = \|\widetilde{\Psi}_p\|^2_{W_{\mathrm{res,rel}}},$$

nicht $|c_p|^2 = \|\widetilde{\Psi}_p\|^2 / \|\varepsilon_p\|^2$ (Fall B aus NEU-134 §134.0 entfällt).

**Statusmarker:** ✅[Axiom/Konvention, NEU-135.D]

---

## 44.3 — Definition von $C_p^{\mathrm{rel}}$

Der **relative Primkanaloperator** ist

$$C_p^{\mathrm{rel}} \;:=\; \pi_{H_1} \cdot c_p \cdot \pi_{H_3^{\mathrm{rel}}},$$

wobei $\pi_{H_1}$, $\pi_{H_3^{\mathrm{rel}}}$ die Orthogonalprojektionen auf die jeweiligen Schichtkanäle sind.

In der Rang-1-Darstellung (normierte Basisvektoren $e_1^{(p)} \in H_1$, $f_3^{(p)} \in H_3^{\mathrm{rel}}$):

$$C_p^{\mathrm{rel}} \;=\; c_p \cdot \bigl(e_1^{(p)} \otimes f_3^{(p)*}\bigr), \qquad
\|e_1^{(p)}\| = \|f_3^{(p)}\| = 1.$$

Damit gilt:
$$\widetilde{\Psi}_p \;=\; C_p^{\mathrm{rel}}\,\varepsilon_p \;=\; C_p^{\mathrm{rel}}\,f_3^{(p)} \;=\; c_p \cdot e_1^{(p)}.$$

**Statusmarker:** ✅[Definition]

---

## 44.4 — Definition von $c_p$

Der **skalare Kanalgewichtskoeffizient** $c_p \in \mathbb{C}$ ist durch die Projektionsstruktur eindeutig bestimmt:

$$c_p \;=\; \langle e_1^{(p)},\, C_p^{\mathrm{rel}}\, f_3^{(p)} \rangle
\;=\; \langle e_1^{(p)},\, \widetilde{\Psi}_p \rangle.$$

Wegen $\widetilde{\Psi}_p = c_p \cdot e_1^{(p)}$ und $\|e_1^{(p)}\| = 1$ gilt:

$$|c_p|^2 \;=\; \|\widetilde{\Psi}_p\|^2_{W_{\mathrm{res,rel}}}
\;=\; (\log p)^2 \sum_m \|F_{p,m}\|^2_{W_{\mathrm{res}}},$$

mit $F_{p,m} := \sum_{u,s} a_{p,u}\,\ell_{s,m}\,u\,s\, E^{\mathrm{rel}}_{u+ps;\,m \to pm}$ (aus NEU-134 §134.1).

Für alle Primzahlen $p$ gilt $c_p \neq 0$ (NEU-134, Voraussetzung für Rang-1).

**Statusmarker:** ✅[Definition]

---

## 44.5 — Definition von $\widetilde{\Psi}_p$ und $\|\widetilde{\Psi}_p\|^2$

$$\widetilde{\Psi}_p \;=\; c_p \cdot e_1^{(p)}, \qquad
\|\widetilde{\Psi}_p\|^2 \;=\; |c_p|^2.$$

Die Faktorisierung:

$$|c_p|^2 \;=\; (\log p)^2 \cdot B_p, \qquad
B_p \;:=\; \sum_m \|F_{p,m}\|^2_{W_{\mathrm{res}}} \;\geq\; 0.$$

Die Prüffrage von NEU-152 — ob $B_p \geq A/p$ gleichmäßig gilt — ist von dieser Definition streng getrennt und wird dort behandelt.

**Statusmarker:** ✅[Definition]; Abschätzung von $B_p$: ❓[O] → NEU-152

---

## 44.6 — Definition von $P_p$ und $\pi_p$

Der **gewichtete Primkanaloperator** ist

$$P_p \;:=\; C_p^{\mathrm{rel}}(C_p^{\mathrm{rel}})^*
\;=\; |c_p|^2 \cdot |e_1^{(p)}\rangle\langle e_1^{(p)}|.$$

Die **orthogonale Rang-1-Projektion** wird separat bezeichnet:

$$\pi_p \;:=\; |e_1^{(p)}\rangle\langle e_1^{(p)}|, \qquad \pi_p^2 = \pi_p, \qquad \mathrm{Tr}(\pi_p) = 1.$$

Damit gilt:

$$P_p = |c_p|^2 \cdot \pi_p, \qquad P_p^2 = |c_p|^2\, P_p, \qquad \mathrm{Tr}(P_p) = |c_p|^2.$$

$P_p$ ist **kein Projektor** (außer für $|c_p|^2 \in \{0,1\}$). Die Notation $\pi_p$ für die orthogonale Projektion ist ab NEU-151 verbindlich.

**Statusmarker:** ✅[Definition]

---

## 44.7 — Rang-1-Modell (Zusammenfassung)

Unter der Welt-2-Normkonvention ($\|\varepsilon_p\| = 1$) gilt das vollständige Rang-1-Modell:

| Objekt | Exakte Formel | Norm |
|---|---|---|
| $\varepsilon_p$ | $f_3^{(p)} \in H_3^{\mathrm{rel}}$ | $\|\varepsilon_p\| = 1$ |
| $C_p^{\mathrm{rel}}$ | $c_p \cdot (e_1^{(p)} \otimes f_3^{(p)*})$ | $\|C_p^{\mathrm{rel}}\|_{\mathrm{op}} = \|C_p^{\mathrm{rel}}\|_{\mathcal{S}_1} = |c_p|$ |
| $\widetilde{\Psi}_p$ | $c_p \cdot e_1^{(p)}$ | $\|\widetilde{\Psi}_p\| = |c_p|$ |
| $P_p$ | $|c_p|^2 \cdot \pi_p$ | $\|P_p\|_{\mathrm{op}} = \|P_p\|_{\mathcal{S}_1} = \mathrm{Tr}(P_p) = |c_p|^2$ |
| $\pi_p$ | $|e_1^{(p)}\rangle\langle e_1^{(p)}|$ | $\|\pi_p\|_{\mathrm{op}} = 1$, $\mathrm{Tr}(\pi_p) = 1$ |
| $c_p$ | $\langle e_1^{(p)}, \widetilde{\Psi}_p \rangle$ | $|c_p|^2 = (\log p)^2 B_p$ |

**Zentrale Identität (Import in NEU-151):**

$$\boxed{\|\widetilde{\Psi}_p\|^2 = \|C_p^{\mathrm{rel}}\|_{\mathrm{op}}^2 = \|C_p^{\mathrm{rel}}\|_{\mathcal{S}_2}^2 = \mathrm{Tr}(P_p) = |c_p|^2}$$

**Statusmarker:** ✅[Axiom/Konvention + Definition]

---

## Offene Fragen (ausdrücklich ausgelagert)

Dieses Blatt enthält keine Abschätzungen. Alle quantitativen Fragen sind ausgelagert:

| Frage | Ort |
|---|---|
| $|c_p|^2 = O((\log p)^2/p)$? (obere Schranke) | NEU-135.D, NEU-134 §134.5 |
| $B_p = O(1/p)$? (harter Prüfstein) | NEU-134 §134.6 |
| $B_p \geq A/p$? (Nichtentartung) | NEU-152 |
| Normkonvention für $a_{p,u}$, $\ell_{s,m}$ | NEU-41 |

---

## Verweise

- **NEU-41**: Fourier-Hebung, Koeffizienten $a_{p,u}$, Schleifenlängengewichte $\ell_{s,m}$
- **NEU-134**: Kanalgewichte, Formel für $|c_p|^2$, drei Szenarien für $B_p$
- **NEU-135.D**: Welt-2-Entscheidung, Normabschätzung, obere Schranke
- **NEU-44.X**: Rang-1-Beweis (Verifikationseintrag, baut auf diesem Blatt auf)
- **NEU-44.X'**: Rang-1-Stabilität unter Störungen
- **NEU-44.R**: Rückbindung an NEU-137 (Spurklassen-Verifikation)
- **NEU-143**: Edge-Label, Orthogonalität der Teilräume $H_{m \to pm}$
- **NEU-151**: Typaudit (importiert dieses Blatt als Quelle)
- **NEU-152**: Nichtentartung (Prüffrage $B_p \geq A/p$)
