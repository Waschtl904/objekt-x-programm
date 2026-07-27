# NEU-229 — Intrinsische verbundene Form und Mischblock: Gram-Geometrie der Hebungsfaser

**Katalog-ID:** NEU-229
**Knoten:** `[O-229-1-intrinsic-connected-form-and-mixed-Gram-block]`
**Stand:** 27. Juli 2026
**Vorgänger:** NEU-228
**Ergebnis:** $B_p^{\mathrm{raw}}$ kann nicht die vollständige verbundene Form sein. Die blockdiagonale Reparatur
ist strukturell ungeeignet. Ein intrinsischer Mischblock $\beta_p$ ist die eigentliche Konstruktionsaufgabe.

---

## 0. Auditurteil

$$
\boxed{\ B_p^{\mathrm{raw}} \text{ kann nicht die vollständige verbundene Form sein.} \ }
$$

Drei Befunde:

1. **$B_p^{\mathrm{raw}}(e_p, e_p) = 0$ widerspricht $h_p(e_p,e_p)=1$** für jedes skalare Vielfache.
   `✓[M]_neg`
2. **Die blockdiagonale Reparatur $h_p^{\mathrm{dec}}$ erzeugt $\mathcal{L}_p = \emptyset$** im positiv
   definiten Kernblock. `✓[M]_neg`
3. **Der konstruktive Engpass ist der Mischblock $\beta_p$** — ohne ihn ist jede positiv definite
   Hebungsfaser leer. `❓[O]` `[O-229-1]`

---

## 1. `[O-229-1a]` — Unmittelbarer Widerspruch: $B_p^{\mathrm{raw}} \neq \alpha_p^{-1} h_p$

### 1.1 Die Nullstelle von $T_p$

Quellseitig gilt (NEU-153, Z. 179):

$$
T_p(e_0 V_p) = 0 .
$$

Damit folgt für $B_p^{\mathrm{raw}}(x,y) = \langle T_p x, T_p y \rangle$ sofort

$$
B_p^{\mathrm{raw}}(e_p, e_p) = 0, \qquad B_p^{\mathrm{raw}}(e_p, k) = 0 \quad \forall k \in K_p ,
$$

wobei $e_p = e_0 V_p$.

### 1.2 Widerspruch zur Normierung

Die in NEU-228 verwendete Normierungsbedingung verlangt

$$
h_p(e_p, e_p) = 1 .
$$

Folglich kann für kein $\alpha_p$ gelten:

$$
\boxed{\ h_p = \alpha_p B_p^{\mathrm{raw}} \quad \text{auf } \mathbb{C}e_p \oplus K_p .\ }
$$

$$
\boxed{\ [O\text{-}228\text{-}2a1\text{-primary-Wres-computation}] \quad \checkmark[M]_{\mathrm{neg,Quelle}}.\ }
$$

**Umfang.** Ausgeschlossen ist nur die Identifikation der vollständigen verbundenen Form mit einem
skalaren Vielfachen der Rohkopplungsform. $B_p^{\mathrm{raw}}$ kann weiterhin den reinen Kernblock
$A_p$ oder einen Bestandteil davon liefern. `✓[M]`

---

## 2. `[O-229-1b]` — Blockdiagonale Reparatur ist strukturell ungeeignet

### 2.1 Definition und automatische Gramwerte

Man könnte versuchen zu definieren:

$$
h_p^{\mathrm{dec}}(ce_p + k,\, de_p + \ell) = \bar{c}\,d + \alpha_p B_p^{\mathrm{raw}}(k,\ell) .
$$

Dann gilt automatisch

$$
g_{00}^{(p)} = 1, \qquad g_{0u}^{(p)} = 0 .
$$

### 2.2 Orthogonalitäts-No-Go

Ist der Kernblock $\alpha_p B_p^{\mathrm{raw}}|_{K_p \times K_p}$ positiv definit, greift unmittelbar
das Orthogonalitäts-No-Go aus NEU-228:

$$
\mathbb{C}e_p \perp K_p \quad \Longrightarrow \quad \mathcal{L}_p = \varnothing .
$$

$$
\boxed{\ \checkmark[M]_{\mathrm{neg}} \text{ für die positiv definite blockdiagonale Konstruktion.}\ }
$$

Ist der Kernblock nur positiv semidefinit, entstehen höchstens radikale Liftänderungen; nach
Quotientenbildung liefern sie keinen neuen Vektor, sofern die Kopplung korrekt durch das Radikal
faktorisiert.

---

## 3. `[O-229-1c]` — Allgemeinste hermitesche Erweiterung

### 3.1 Blockmatrixdarstellung

Die allgemeinste hermitesche Erweiterung mit $h_p(e_p, e_p) = 1$ hat die Form

$$
\boxed{\ h_p(ce_p+k,\, de_p+\ell)
= \bar{c}\,d + \bar{c}\,\beta_p(\ell) + \overline{\beta_p(k)}\,d + a_p(k,\ell), \ }
$$

wobei
- $\beta_p : K_p \to \mathbb{C}$ ein lineares Mischfunktional,
- $a_p : K_p \times K_p \to \mathbb{C}$ eine hermitesche Form.

### 3.2 Gramwerte

$$
g_{0u}^{(p)} = \beta_p(e_u V_p), \qquad g_{uv}^{(p)} = a_p(e_u V_p,\, e_v V_p) .
$$

### 3.3 Warum $B_p^{\mathrm{raw}}$ den Mischblock nicht liefert

Die Rohkopplungsform kann höchstens den Ansatz

$$
a_p(k,\ell) = \alpha_p \langle T_p k, T_p \ell \rangle
$$

motivieren. Sie erzeugt aber gerade **nicht** den entscheidenden Mischblock $\beta_p$, weil

$$
T_p e_p = 0 \quad \Longrightarrow \quad \langle T_p e_p, T_p k \rangle = 0 \quad \forall k \in K_p .
$$

$$
\boxed{\ \text{Konstruktiver Engpass: Woher stammt intrinsisch ein nichtverschwindender Mischblock } \beta_p?\ }
$$

Ohne einen solchen Mischblock ist die positiv definite Hebungsfaser leer. `❓[O]`

---

## 4. `[O-229-1d]` — Positivitätsbedingung und Schurkomplementkriterium

Falls $a_p \geq 0$ mit $a_p(k,\ell) = \langle k, A_p \ell \rangle$, muss $\beta_p$ bezüglich $A_p$
beschränkt sein. Im invertierbaren Fall lautet das Schurkomplementkriterium:

$$
\boxed{\ 1 - \langle b_p, A_p^{-1} b_p \rangle \geq 0 .\ }
$$

Für positive Definitheit des vollen Gramblocks wird die strikte Ungleichung benötigt.

### 4.1 Anforderungsliste an einen brauchbaren Mischblock

Ein zulässiger $\beta_p$ muss gleichzeitig:

- **intrinsisch** aus $W_{\mathrm{res}}$-, Fourier-, KMS- oder Randgeometrie entstehen — kein freies Datum
- **nicht verschwinden**: $\beta_p \not\equiv 0$
- **beschränkt** gegenüber $A_p^{1/2}$ sein
- **Positivität** des gesamten Gramblocks erhalten (Schurkriterium)
- mit $\sharp$, Quotient und relevanten Symmetrien **kompatibel** sein
- einen **geladenen normierten Lift** $e_p + k$ mit $\widetilde{T}_p^{\mathrm{raw}}(k) \neq 0$ liefern

Das ist eine echte Konstruktionsaufgabe, keine verbleibende Matrixrechnung.

---

## 5. `[O-229-1e]` — Kandidatenanalyse für $\beta_p$

### 5.1 Ausgeschlossene Kandidaten

| Kandidat | Grund des Ausschlusses |
|---|---|
| $\beta_p(k) = \langle e_p, k \rangle_{L^2}$ | Nicht intrinsisch; $L^2$-Skalarprodukt nicht kanonisch auf $B_3$ |
| $\beta_p(k) = B_p^{\mathrm{raw}}(e_p, k)$ | Verschwindet identisch wegen $T_p e_p = 0$ |
| Freie Wahl $\beta_p \in K_p^*$ | Anti-Fitting-Firewall (X.neg, A.8) |

### 5.2 Offene Kandidaten

| Kandidat | Herkunft | Status |
|---|---|---|
| KMS-Zweipunktfunktion $\omega_{\beta}(e_p, \cdot)|_{K_p}$ | KMS-Zustand auf $B_3$ (NEU-014) | `❓[O]` |
| Randoperator aus Fourier-Laplace-Struktur | NEU-042, Randgeometrie | `❓[O]` |
| Modularer Operator $\Delta^{1/2}$-Matrixelement | Tomita-Takesaki auf $W_{\mathrm{res}}$ | `❓[O]` |
| Spektralprojektion eines kanonischen Ladungsoperators $Q$ | NEU-051, intrinsische Schwelle | `❓[O]` |

---

## 6. Revidierter Status von `[O-228-2a]`

| Knoten | Aussage | Status |
|---|---|---|
| `[O-228-2a1-primary-Wres-computation]` | $\mathrm{Tr}_{W_{\mathrm{res}}}^{\mathrm{conn}}$ auf Fourier-Liftbasis nicht konstruktiv definiert; $\sharp$-Operation ohne bewiesene hermitesche Realisierung dort | `✓[M]_neg,Quelle` |
| `[O-228-2a1]` (Ersatz $h_p = \alpha_p B_p^{\mathrm{raw}}$) | Widerspricht Normierung $h_p(e_p,e_p)=1$ | `✓[M]_neg` |
| `[O-228-2a]` | Teilweise beantwortet — negativer Teil geschlossen, konstruktiver Teil offen | `✓[M]_part` |

---

## 7. Statusbilanz

| Aussage | Status |
|---|---|
| $T_p(e_0 V_p) = 0$ quellseitig (NEU-153 Z.179) | `✓[M]` |
| $B_p^{\mathrm{raw}}(e_p,e_p) = 0$, $B_p^{\mathrm{raw}}(e_p,k) = 0\ \forall k \in K_p$ | `✓[M]` |
| $h_p = \alpha_p B_p^{\mathrm{raw}}$ unmöglich auf $\mathbb{C}e_p \oplus K_p$ | `✓[M]_neg` |
| Blockdiagonale Reparatur $h_p^{\mathrm{dec}}$ mit pos. def. Kernblock $\Rightarrow \mathcal{L}_p = \emptyset$ | `✓[M]_neg` |
| Allgemeinste Form mit $h_p(e_p,e_p)=1$ erfordert Mischblock $\beta_p$ | `✓[M]` |
| $B_p^{\mathrm{raw}}$ erzeugt $\beta_p = 0$ — strukturell ungeeignet | `✓[M]_neg` |
| Intrinsischer nichtverschwindender Mischblock $\beta_p$ | `❓[O]` |
| Schurkomplementkriterium $1 - \langle b_p, A_p^{-1} b_p \rangle \geq 0$ | `❓[O]` — auswertbar erst nach Konstruktion von $\beta_p$ |
| Kernblock $a_p(k,\ell) = \alpha_p \langle T_p k, T_p \ell \rangle$ als Ansatz | `❓[O]` — Positivität und Rang offen |
| Feshbach-Transfer und Hebungsabstieg | **gesperrt** bis `[O-229-1]` geschlossen |

---

## 8. Strategische Aussage

$$
\boxed{\ \text{Die Transferschicht benötigt nicht bloß eine normierte Fourierhebung,}\ }
$$

$$
\boxed{\ \text{sondern eine neue intrinsische verbundene Form mit nichttrivialem Mischblock.}\ }
$$

Ohne Wiederauffinden der fehlenden NEU-41/143-Primärdefinitionen wäre jede solche Form eine neue
Konstruktion `✓[K]`, keine Rekonstruktion eines bereits bewiesenen $W_{\mathrm{res}}$-Objekts. Der
aktuelle Audit lokalisiert das Leerfaser-Risiko eine Ebene tiefer als bisher: nicht erst in der
Hebungsunabhängigkeit (153.A/B), sondern bereits in der **undefinierten verbundenen Gramgeometrie**.

> **Anti-Fitting.** Der Mischblock $\beta_p$ darf **nicht** so gewählt werden, dass $\mathcal{S}_2
> \setminus \mathcal{S}_1$ oder die $\Xi$-Identität herauskommt. Nur ein aus der intrinsischen
> $W_{\mathrm{res}}$-Geometrie kanonisch bestimmter Wert ist zulässig.

> **Sperrvermerk.** Kein Hebungsabstieg, keine Schattenklassenrechnung vor `[O-229-1]`.

---

## 9. Nächste Knoten

| Knoten | Aufgabe | Priorität |
|---|---|---|
| `[O-229-1-α]` | Kernblock untersuchen: $a_p(k,\ell) \stackrel{?}{=} \alpha_p \langle T_p k, T_p \ell \rangle$ — Positivität, Rang, Radikal | **1** |
| `[O-229-1-β]` | Intrinsischen Mischblock konstruieren: $\beta_p(k) = h_p(e_p, k)$ — Herkunft aus KMS / Fourier-Laplace / Modularem Operator | **1** |
| `[O-229-1-γ]` | Hermitizität, Positivität, Schurkomplementkriterium des vollen Gramblocks beweisen | **2** |
| `[O-229-1-δ]` | Nichttrivialität prüfen: $\beta_p \neq 0$ und normierter Lift $e_p + k$ mit $\widetilde{T}_p^{\mathrm{raw}}(k) \neq 0$ | **2** |
| `[O-153-A/B]` | Hebungsunabhängigkeit — gesperrt bis `[O-229-1-δ]` | danach |
| `[O-226-4]` | Gramoperator $g_{0u}^{(p)}$, $g_{uu}^{(p)}$ — gesperrt bis `[O-229-1-γ]` | danach |

---

## Abhängigkeiten

| Referenz | Verwendet für |
|---|---|
| NEU-041 | Kopplungsoperator $T_p$, Wohlbestimmtheitsbedingung (41.4) |
| NEU-043 | (43.1) Fourierregel $\widetilde\omega_2(e_uV_p, e_sV_m) = -us\log(p)\,e_{u+ps}V_{pm}$ |
| NEU-051 | Regulatoroptionen, Kopplungsform (51.2) |
| **NEU-153** | $T_p(e_0V_p)=0$ (Z.179), Faser $\mathcal{L}_p$, Gram $g^{(p)}$, Stufen 153.A/B/D.0 |
| NEU-014 | KMS-Zustand auf $B_3$ — Kandidat für $\beta_p$ |
| NEU-042 | Fourier-Laplace-Hebung — Kandidat für $\beta_p$ |
| NEU-143 | Primärdefinition verbundene Form (Quelle fehlt teilweise) |
| NEU-225/226/227/228 | Transportgenerator, Feshbach-Transfer, Spektralmaßform, Hebungswahl |
