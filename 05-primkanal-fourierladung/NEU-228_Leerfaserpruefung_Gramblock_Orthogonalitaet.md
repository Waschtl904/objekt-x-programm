# NEU-228 — [O-228-2] / [O-228-2a] Leerfaserprüfung: Gramblock, Orthogonalität, Radikal der Primhebungsfaser

**Datum:** 27. Juli 2026  
**Status:** ✓[M]_part  
**Nachfolger:** [O-228-2a1-primary-Wres-computation-of-g0u-and-guv]  
**Sperrvermerk:** Keine Schattenklassenrechnung vor Abschluss von [O-228-2a].

---

## 0. Kontext

NEU-228 hat gezeigt: Der naive Projektorregulator $V_p^{\mathrm{can}} = 0$ ist widerlegt (✓[M]_neg),
weil $\pi_{\mathrm{prim}}$ nur $u = 0$ selektiert und dort $-us\log p = 0$.
Daraus folgt **nicht**, dass $\mathcal{L}_p = \varnothing$ — zusätzliche Komponenten
$f_p \in \ker \pi_{\mathrm{prim}}$ können die Faser wieder befüllen.

[O-228-2] ist daher die Frage: Unter welchen Bedingungen an $\langle\cdot,\cdot\rangle_{\mathrm{conn}}$
ist die normierte Fourier-geladene Hebungsfaser $\mathcal{L}_p$ nichtleer?

---

## 1. Funktionalanalytische Normalform

Sei $e_p := e_0 V_p$, $\pi_{\mathrm{prim},p}(e_p) = \varepsilon_p$,
$$K_p := \ker \pi_{\mathrm{prim},p}.$$
Die vollständige algebraische Liftfaser ist $e_p + K_p$.

Sei $h_p(x,y) := \langle x, y \rangle_{\mathrm{conn}}$ mit $h_p(e_p, e_p) = 1$.
Jeder Lift hat die Form $\widehat{\varepsilon}_p = e_p + k$, $k \in K_p$.

Definiere
$$\ell_p(k) := h_p(e_p, k), \qquad q_p(k) := h_p(k,k).$$

Die Normierungsbedingung $h_p(e_p + k,\, e_p + k) = 1$ ist exakt äquivalent zu
$$\boxed{2\operatorname{Re}\ell_p(k) + q_p(k) = 0.} \tag{228.1}$$

Die Fourierladungsbedingung ist **keine** lineare Nebenraumbedingung, sondern eine
Nichtverschwindensbedingung eines linearen Kopplungsoperators:
$$F_p : K_p \to \mathcal{Y}_p, \qquad F_p(k) \neq 0.$$

Die zulässige Hebungsfaser ist daher:
$$\boxed{\mathcal{L}_p \neq \varnothing \iff \exists\, k \in K_p:\;
2\operatorname{Re}\ell_p(k) + q_p(k) = 0,\quad F_p(k) \neq 0,\quad
k \text{ erfüllt alle weiteren Zulässigkeitsbedingungen}.} \tag{228.4}$$

**Status:** ✓[M].

---

## 2. Gramblock

Wähle den algebraischen Fourierkern
$K_p^{\mathrm{Four}} := \operatorname{span}\{e_u V_p : u \neq 0\} \subseteq K_p.$

Definiere
$$g_{00}^{(p)} := h_p(e_0 V_p, e_0 V_p) = 1,$$
$$g_{0u}^{(p)} := h_p(e_0 V_p, e_u V_p), \quad u \neq 0,$$
$$g_{uv}^{(p)} := h_p(e_u V_p, e_v V_p), \quad u,v \neq 0.$$

Auf $\mathbb{C}e_p \oplus K_p^{\mathrm{Four}}$ hat die Form die Blockdarstellung
$$\begin{pmatrix} 1 & b_p^* \\ b_p & A_p \end{pmatrix}, \tag{228.2a.1}$$
mit $b_p = (g_{u0}^{(p)})_{u\neq 0}$, $A_p = (g_{uv}^{(p)})_{u,v \neq 0}$.

Für $k = \sum_{u \neq 0} a_u e_u V_p$ gilt:
$$\ell_p(k) = \sum_{u \neq 0} a_u\, g_{0u}^{(p)}, \qquad
q_p(k) = \sum_{u,v \neq 0} \overline{a_u} a_v\, g_{uv}^{(p)}.$$

Die Normierungsbedingung (228.1) lautet damit in Koordinaten:
$$2\operatorname{Re}\Bigl(\sum_{u \neq 0} a_u g_{0u}^{(p)}\Bigr)
+ \sum_{u,v \neq 0} \overline{a_u} a_v g_{uv}^{(p)} = 0. \tag{228.2a.2}$$

**Status:** ✓[M].

---

## 3. Orthogonalitätskriterium

$$e_p \perp K_p \iff \ell_p|_{K_p} = 0
\iff \boxed{g_{0u}^{(p)} = 0 \quad \forall\, u \neq 0.} \tag{228.2a.3}$$

**Achtung:** Aus $\pi_{\mathrm{prim},p}(e_u V_p) = 0$ ($u \neq 0$) folgt **nicht**
$h_p(e_0 V_p, e_u V_p) = 0$. Projektion und Wres-Orthogonalität sind verschiedene Strukturen.

**Status:** ✓[M] für die Äquivalenz; ❓[O] für die konkrete Berechnung aus den Primärdefinitionen.

---

## 4. Positiv-definites Orthogonalitäts-No-Go

**Satz 228.2a.1**

*Voraussetzungen:* $h_p > 0$ auf $\mathbb{C}e_p \oplus K_p$; $K_p$ abgeschlossen; $h_p(e_p, K_p) = 0$.

*Beweis:* Aus der Orthogonalität:
$$h_p(e_p + k,\, e_p + k) = h_p(e_p, e_p) + h_p(k,k) = 1 + q_p(k).$$
Normierungsbedingung $= 1$ ergibt $q_p(k) = 0$.
Wegen positiver Definitheit folgt $k = 0$.

Da $e_p = e_0 V_p$ keine Fourierladung trägt ($F_p(0) = 0$):
$$\boxed{h_p > 0 \;\text{und}\; g_{0u}^{(p)} = 0\; \forall u \neq 0
\;\Longrightarrow\; \mathcal{L}_p = \varnothing.} \tag{228.2a.4}$$

**Status:** ✓[M], bedingt auf positive Definitheit, Abgeschlossenheit, vollständige Orthogonalität.

**Umfang:** Ausgeschlossen wäre die aktuelle Fourier-Hebungs-/Feshbach-Kopplung.
Nicht ausgeschlossen: andere Kopplungsarchitekturen, Jacobi-/Stieltjeskanal,
andere spektrale Realisierungen von Objekt X.

---

## 5. Positiv-definiter nichtorthogonaler Fall

**Satz 228.2a.2**

*Voraussetzungen:* $h_p > 0$; $\exists\, v \in K_p$ mit $\ell_p(v) \neq 0$.

*Beweis:* Für $k = tv$, $t \in \mathbb{R}$:
$$h_p(e_p + tv,\, e_p + tv) = 1 + 2t\operatorname{Re}\ell_p(v) + t^2 q_p(v).$$
Neben $t = 0$ liefert
$$t^* = -\frac{2\operatorname{Re}\ell_p(v)}{q_p(v)} \neq 0$$
eine nichttriviale normierte Liftänderung. Damit:
$$\boxed{h_p > 0 \;\text{und}\; \ell_p \neq 0
\;\Longrightarrow\; \mathcal{A}_p^{\mathrm{norm}} \setminus \{0\} \neq \varnothing.} \tag{228.2a.5}$$

**Status:** ✓[M].

Daraus folgt $\mathcal{L}_p \neq \varnothing$ erst nach zusätzlichem Nachweis von
$F_p(k) \neq 0$ und allen weiteren NEU-153/157-Bedingungen.

**Status der Nichtleerheit von $\mathcal{L}_p$:** ✓[M]_part.

---

## 6. Schurkomplement (positiv definiter Fall)

Falls $A_p$ auf dem abgeschlossenen Kernraum positiv und invertierbar ist:
$$G_p > 0 \iff A_p > 0 \;\text{und}\;
\boxed{1 - b_p^* A_p^{-1} b_p > 0.} \tag{228.2a.6}$$

Der Grenzfall $1 - b_p^* A_p^{-1} b_p = 0$ zeigt eine Nullrichtung des Gramblocks an.

**Warnung:** In unendlicher Dimension darf $A_p^{-1}$ nur unter Beweis der Invertierbarkeit
und Domänenklarheit verwendet werden. Allgemein: quadratische Form oder Moore-Penrose-Inverse
auf $\overline{\operatorname{Ran} A_p}$.

**Status:** ✓[M] als Kriterium; ❓[O] konkrete Anwendbarkeit.

---

## 7. Semidefiniter Fall und Radikal

Definiere $\mathcal{N}_p := \operatorname{Rad}(h_p|_{\mathbb{C}e_p \oplus K_p})$.

Ein Vektor $x = ce_p + k$ liegt im Radikal genau dann, wenn
$$c + b_p^* k = 0, \qquad c b_p + A_p k = 0.$$

Für reine Kernrichtungen $k \in K_p$:
$$k \in \mathcal{N}_p \iff b_p^* k = 0 \;\text{und}\; A_p k = 0.$$

Solche $k$ erfüllen $\ell_p(k) = 0$, $q_p(k) = 0$ und erzeugen algebraisch normierte Lifts $e_p + k$.
Im Wres-Quotienten können sie jedoch dieselbe Klasse wie $e_p$ darstellen. Daher:
$$\boxed{\text{algebraische Nichtleerheit} \neq \text{nichttriviale Nichtleerheit im Wres-Quotienten}.}
\tag{228.2a.7}$$

Prüfung erforderlich:
$$\widetilde{T}_p^{\mathrm{raw}}(\mathcal{N}_p \cap K_p) \subseteq \mathcal{N}_{\mathrm{Wres,rel}}\;?
\tag{228.2a.8}$$
(Verbindung zum Quotientabstieg aus NEU-221e.)

**Status:** ✓[M] für das Kriterium; ❓[O] konkrete Radikalbestimmung.

---

## 8. Indefiniter Fall

Ist $h_p$ indefinit, entscheidet weder $g_{0u}^{(p)} = 0$ noch $g_{0u}^{(p)} \neq 0$
allein über Nichtleerheit. Selbst bei $\ell_p = 0$ kann eine isotrope Richtung
$k \neq 0$, $q_p(k) = 0$ die Normierung erfüllen.

**Hinreichende Kriterien:**

**8.1 Nichtisotrope Richtung mit Kreuzterm:**
Sei $v \in K_p$ mit $q_p(v) \neq 0$, $\ell_p(v) \neq 0$. Dann ist
$$k^* = -\frac{2\overline{\ell_p(v)}}{q_p(v)}\, v$$
eine nichttriviale Lösung von (228.1). Besitzt $v$ Fourierladung, ist $\mathcal{L}_p$ nichtleer.
**Status:** ✓[M].

**8.2 Isotrope Richtung:**
Sei $v \neq 0$ mit $q_p(v) = 0$. Durch Phasenwahl von $cv$ kann
$\operatorname{Re}\ell_p(cv) = 0$ erreicht werden, dann erfüllt $k = cv \neq 0$ die Normierungsgleichung.
Zusätzlich muss $F_p(k) \neq 0$ gelten.
**Status:** ✓[M].

Der vollständige Test bleibt (228.4). **Status:** ✓[M] für die Normalform; ❓[O] konkrete Entscheidung.

---

## 9. Exakte Ladungsbedingung

Vor endgültiger Entscheidung muss aus NEU-153/157 extrahiert werden, welche Bedingung
„hat Fourierladung" exakt bezeichnet. Mögliche, nicht automatisch äquivalente Formulierungen:

- $k \neq 0$
- $\exists\, u \neq 0: a_u \neq 0$
- $f_p(k) \neq 0$
- $\widetilde{T}_p^{\mathrm{raw}}(k) \neq 0$

Die Feshbach-Kopplung benötigt mindestens $\widetilde{T}_p^{\mathrm{raw}}(k) \neq 0$.
Ein formal Fourier-geladener Lift, der im Kern der Rohkopplung liegt, genügt nicht.

**Status:** ❓[O].

---

## 10. Revidierter Status

$$\boxed{[O\text{-}228\text{-}2a] \quad \checkmark[M]_{\mathrm{part}}}$$

**Bewiesen / exakt typisiert:**
- Gramblockdarstellung
- Orthogonalitätsbedingung $g_{0u}^{(p)} = 0\;\forall u \neq 0$
- Positiv-definites Orthogonalitäts-No-Go (Satz 228.2a.1)
- Existenz nichttrivialer normierter Liftänderungen bei Nichtorthogonalität (Satz 228.2a.2)
- Radikalgleichungen und Trennung algebraisch/quotientiert
- Trennung Normierungsbedingung / Fourierladungsbedingung

**Offen:**
- Primärberechnung von $g_{0u}^{(p)}$ und $g_{uv}^{(p)}$ aus NEU-41/153
- Formtyp von $h_p$ (positiv definit / semidefinit / indefinit)
- Radikal $\mathcal{N}_p$
- Exakte Ladungsdefinition (NEU-153/157)
- Weitere Nebenbedingungen $\mathcal{A}_p^{\mathrm{adm}}$ aus NEU-153/157/221e

---

## 11. Nächster atomarer Knoten

$$\boxed{[O\text{-}228\text{-}2a1\text{-primary-Wres-computation-of-}g_{0u}^{(p)}\text{-and-}g_{uv}^{(p)}]}$$

**Auftrag:**
1. Definition von $\langle\cdot,\cdot\rangle_{\mathrm{conn}}$ aus NEU-41/153 vollständig extrahieren.
2. Für Fourierbasiselemente berechnen: $h_p(e_u V_p, e_v V_p)$.
3. Entscheiden: $g_{0u}^{(p)} = 0\;?$
4. Danach: Positivität, Semidefinitheit oder Indefinitheit des Gramblocks bestimmen.

**Der entscheidende Ja/Nein-Test lautet:**
$$\boxed{g_{0u}^{(p)} = 0 \text{ für alle } u \neq 0 \quad\text{oder nicht?}}$$

Im positiv definiten Fall entscheidet genau dieser Kreuzblock, ob die Feshbach-Eingangsfaser leer ist.
