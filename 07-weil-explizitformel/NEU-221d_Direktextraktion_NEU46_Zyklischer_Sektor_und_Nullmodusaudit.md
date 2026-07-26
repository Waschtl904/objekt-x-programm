# NEU-221d — Direktextraktion NEU-46: Zyklischer Sektor und Nullmodusaudit

**Stand:** 26. Juli 2026  
**Programm:** Objekt X / X.3.16 → NEU-221-Zweig  
**Vorgänger:** NEU-221c  
**Typ:** Quellenaudit mit partieller Extraktion — *keine Konstruktion des Feshbach-Momentoperators*

---

## Ziel

Dieser Knoten extrahiert quellgetreu, was NEU-46 über das Feshbach-Tripel
\(({\mathcal H}_N^{\mathrm{rel}},\, D_N^{\mathrm{rel}},\, \Psi_N)\)
tatsächlich belegt, und stellt fest, welche Bestandteile noch fehlen, bevor
\(\Omega_{X,N} = (D_N^{\mathrm{rel}})^{-1}\Psi_N\) und
\(J_{X,N} = (D_N^{\mathrm{rel}})^{-2}\) als verfügbar markiert werden dürfen.

---

## 1. Zentraler Befund

> \(D_N^{\mathrm{rel}}\) ist selbstadjungiert,  
> aber \(({\mathcal H}_N^{\mathrm{rel}},\, D_N^{\mathrm{rel}},\, \Psi_N)\)  
> ist noch **kein vollständig typisiertes zyklisches Tripel**.

---

## 2. Autoritativer Statusbericht

| Teilfrage | Status |
|-----------|--------|
| \(D_N^{\mathrm{rel}}\) selbstadjungiert | ✓\[M\] über NEU-53/54 (Nelson-Matrixabschätzung + Konfinement) |
| \(\Psi_p = C_p^{\mathrm{rel}}\varepsilon_p\) formal definiert | ✓\[K\]\_part (NEU-46, §1, Gl. 46.5–6) |
| \(\varepsilon_p,\, \Psi_p\) als konkrete Hilbertvektoren typisiert | ?\[O\] |
| \(\|\Psi_N\|\) quellseitig fixiert | ?\[O\] |
| \(E_{D_N^{\mathrm{rel}}}(\{0\})\Psi_N = 0\) | ?\[O\] |
| \(\int\|\lambda\|^{-2k-2}\,d\mu_{\Psi_N} < \infty\), \(k=0,1,2\) | ?\[O\] |
| vollständig gekoppelte endliche/archimedische Geometrie | ?\[O\] |

**Knotenstatus:**
```
[O-221-1c1-NEU46-source-triple-and-zero-spectral-test]   ✓[M]_part
```

---

## 3. Was NEU-46 tatsächlich belegt

### 3.1 Weyl-Funktion als zyklisches Spektralintegral (✓\[M\])

NEU-46, §1, Gl. (46.5–6) setzt
$$
M_p(z) = \langle \Psi_p,\,(z - D_{rel,p}^-)^{-1}\Psi_p\rangle_{W_{\mathrm{res,rel}}}
= \int \frac{d\mu_p(\lambda)}{z - \lambda}
$$
mit \(\Psi_p := C_p^{\mathrm{rel}}\varepsilon_p\). Die Spektralmaßdarstellung ist formal korrekt aufgeschrieben.

### 3.2 Nichtverschwindungssatz (✓\[M\])

NEU-46, Satz 46.1 beweist:
$$
M_p \equiv 0 \iff C_p^{\mathrm{rel}} = 0.
$$
Das fixiert die logische Äquivalenz, liefert aber keine Norm für \(\Psi_p\).

### 3.3 Drei-Faktoren-Zerlegung (✓\[M\])

NEU-46, Satz 46.3, Gl. (46.21–23):
$$
D_{\mathrm{Fesh},N}^{\mathrm{rel}} = D_{\mathrm{Euler},N}^{\mathrm{conn}} \cdot D_{\mathrm{Spec},N}^{\mathrm{rel}},
$$
$$
D_{\mathrm{Spec},N}^{\mathrm{rel}} = D_{\mathrm{Jac},N} \cdot D_{\mathrm{scatt},N},
$$
wobei \(D_{\mathrm{scatt},N}\) Birman-Schwinger-Struktur trägt. Die Zerlegung ist mathematisch dokumentiert.

### 3.4 Selbstadjungiertheit (✓\[M\] via NEU-53/54)

- [NEU-53](../01-primkanten-werkzeuge/NEU-053_x3_operatorstatus_drel_selbstadjungiertheit.md): Operator-Typaudit von \(D_N^{\mathrm{rel}}\).  
- [NEU-54](../01-primkanten-werkzeuge/NEU-054_x3_nelson_selbstadjungiertheit_konfinement.md): Nelson-Kriterium + Konfinement-Argument.  
- Ergebnis: \(D_N^{\mathrm{rel}}\) ist (wesentlich) selbstadjungiert auf seiner natürlichen Definitionsmenge.

---

## 4. Wichtigste Sperre

Die Ausdrücke
$$
\Omega_{X,N} = (D_N^{\mathrm{rel}})^{-1}\Psi_N, \qquad J_{X,N} = (D_N^{\mathrm{rel}})^{-2}
$$
dürfen im zyklischen Kandidaten **noch nicht als verfügbar markiert werden**.

Sperrgrund: Es fehlen gleichzeitig

1. \(E_{D_N^{\mathrm{rel}}}(\{0\})\Psi_N = 0\) — sonst ist \((D_N^{\mathrm{rel}})^{-1}\Psi_N\) nicht im Hilbertraum;
2. \(\displaystyle\int_{\lambda\ne 0} |\lambda|^{-2}\,d\mu_{\Psi_N}(\lambda) < \infty\) — Integrierbarkeit der inversen Momente.

Für die ersten drei Momente \(m_{k,N} = \int|\lambda|^{-2k-2}\,d\mu_{\Psi_N}\), \(k=0,1,2\),
werden entsprechend die Potenzen 2, 4, 6 benötigt.

---

## 5. Vier kleinste Folgeknoten

### PD5-NEU-221d → [O-221-1c1a]

**Vektorkongretisierung und Normierung**

```
[O-221-1c1a-source-vector-concretization-and-normalization]
```

Zu extrahieren bzw. zu beweisen:
$$
\varepsilon_p \in \mathcal H_p, \qquad C_p^{\mathrm{rel}}\varepsilon_p \in \mathcal H_p^{\mathrm{rel}},
$$
die genaue Bildung von \(\Psi_N\) aus den lokalen Vektoren und deren unveränderliche Normierung \(\|\Psi_N\|^2 = \sum_{p \le N}\|\Psi_p\|^2\).

---

### PD5-NEU-221d → [O-221-1c1b]

**Zyklischer Nullmodustest**

```
[O-221-1c1b-cyclic-zero-spectrum-test]
```

Zu prüfen:
$$
E_{D_N^{\mathrm{rel}}}(\{0\})\Psi_N = 0,
$$
und präziser: Verhalten von \(d\mu_{\Psi_N}\) in einer Umgebung von 0, insbesondere ob
\(\mu_{\Psi_N}(\{0\}) = 0\) und ob eine lokale Schranke der Form
\(\mu_{\Psi_N}([-\epsilon,\epsilon]) = O(\epsilon^\alpha)\), \(\alpha > 2\), vorliegt.

---

### PD5-NEU-221d → [O-221-1c1c]

**Inverse Momentintegrabilität**

```
[O-221-1c1c-inverse-moment-integrability]
```

Zu beweisen:
$$
\int |\lambda|^{-2}\,d\mu_{\Psi_N} < \infty, \qquad
\int |\lambda|^{-4}\,d\mu_{\Psi_N} < \infty, \qquad
\int |\lambda|^{-6}\,d\mu_{\Psi_N} < \infty.
$$

Erst danach sind die Momente
$$
m_{k,N} = \int |\lambda|^{-2k-2}\,d\mu_{\Psi_N}(\lambda), \quad k = 0,1,2
$$
wohldefiniert und die Stieltjes-Funktion
$$
M_{X,N}(w) = \int_{[0,\infty)} \frac{d\nu_N(x)}{x - w}
$$
trägt echte analytische Information.

---

### PD5-NEU-221d → [O-221-1c1d]

**Globaler Kopplungsgehalt von \(D_{\mathrm{scatt},N}\)**

```
[O-221-1c1d-global-coupling-content-of-DscattN]
```

Zu klären: Erzeugt \(D_{\mathrm{scatt},N}\) tatsächlich globale Kopplung zwischen den Primblöcken, oder liegen lediglich unabhängige lokale Primblöcke vor?

Begründung der Trennung: Auch ein vollständig typisiertes *lokales* Tripel \((\mathcal H_p^{\mathrm{rel}}, D_{rel,p}^-, \Psi_p)\) wäre kein Objekt-X-Kandidat, wenn keine kohärente Kopplung über \(p\) existiert. Die Frage nach globaler Kopplung darf nicht mit der Vektornormierung vermischt werden.

---

## 6. Abhängigkeitsgraph der Sperren

```
NEU-46 (vorhanden)
  ├── Selbstadjungiertheit: ✓[M]  (NEU-53/54)
  ├── Formale Vektordefinition: ✓[K]_part
  │
  ├── [O-221-1c1a]  Vektorkongretisierung/Normierung
  │       ↓ (Voraussetzung für)
  ├── [O-221-1c1b]  Nullmodustest E_D({0})Ψ_N = 0
  │       ↓ (Voraussetzung für)
  ├── [O-221-1c1c]  Inverse Momente k=0,1,2
  │       ↓ (Freischaltet)
  │   Ω_{X,N} und J_{X,N}  ← GESPERRT bis hier
  │
  └── [O-221-1c1d]  Globale Kopplung in D_scatt,N  (parallel, unabhängig)
```

---

## 7. Strategische Einordnung

Der kritische Pfad zu Objekt X ist durch diesen Audit auf **konkrete Vektor- und Spektralbedingungen** reduziert. Die Selbstadjungiertheitsfrage ist erledigt; abstrakte Positivitätsargumente fügen nichts hinzu. Der nächste echte Fortschritt hängt ausschließlich an der quellgetreuen Extraktion und, falls nötig, Schließung der unter [O-221-1c1a–d] identifizierten Lücken.
