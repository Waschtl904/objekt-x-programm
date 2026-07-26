# NEU-220a — Mellin-Normierung und Involutionskompatibilität

**Datei:** `katalog/NEU-220a_Mellin-Normierung_und_Involutionskompatibilitaet.md`  
**Datum:** 2026-07-25  
**Repository:** Waschtl904/rh-fragenkatalog  
**Typ:** Pflichtaudit zu PD-1 (partiell) und PD-2 — Konventionsfixierung vor jeder Gamma-Distributionsrechnung  
**Vorgänger:** NEU-220_Gammafaktor_Quelltyp_und_Zielraum.md (Commit 4eb8653)  

---

## Atomare Knoten

$$[O\text{-}220\text{-}1\text{-PD2-Mellin-normalization}] \quad \checkmark[K/M]$$

$$[O\text{-}220\text{-}1\text{-PD1-test-space}] \quad \checkmark[K/M]_{\mathrm{part}}$$

*(PD-1 partiell: Testfunktionsraum, Haarmaß und Involution stehen fest; der für die Gamma-Distribution erforderliche kleinere Unterraum bleibt bis PD-3 offen.)*

---

## 0. Ausgangslage und Kopplungsdiagnose

PD-2 darf nicht als bloßer Vergleich zweier Mellin-Formeln behandelt werden. Die Mellin-Zentrierung ist unmittelbar mit der in PD-1 vorgeschlagenen Involution $f^\sharp(x)=\overline{f(x^{-1})}$ gekoppelt. Dieser Audit fixiert beide gleichzeitig und hält die alternative unzentrierte Variante **typisiert** fest, statt sie stillschweigend zu verwerfen.

---

## 1. Testfunktionsraum und Isomorphismus $\mathcal{S}_\infty \cong \mathcal{S}(\mathbb{R})$

**Definition (autoritativ):**
$$\mathcal{S}_\infty := \left\{ f: \mathbb{R}_+^\times \to \mathbb{C} \;\.\bigg|\; y \mapsto f(e^y) \in \mathcal{S}(\mathbb{R}) \right\}.$$

Das Haarmaß auf $\mathbb{R}_+^\times$ ist $dx/x$; unter $x = e^y$ wird $dx/x = dy$.

**Satz PD-1a.** Die Abbildung
$$\Phi: \mathcal{S}_\infty \longrightarrow \mathcal{S}(\mathbb{R}), \qquad (\Phi f)(y) := f(e^y)$$
ist ein topologischer Isomorphismus von Fréchet-Räumen.

*Beweis.* Bijektivität: $\Phi^{-1}(g)(x) = g(\log x)$. Jede Schwartz-Halbnorm auf $\mathcal{S}(\mathbb{R})$ entspricht über die Kettenenregel einer Seminorm auf $\mathcal{S}_\infty$ und umgekehrt. Das schnelle Abfallen für $y \to \pm\infty$ entspricht schnellem Abfallen für $x \to 0^+$ bzw. $x \to +\infty$. $\square$

**Involution.** Auf $\mathcal{S}_\infty$ definiere
$$f^\sharp(x) := \overline{f(x^{-1})}.$$
Unter $\Phi$: $(\Phi f^\sharp)(y) = \overline{f(e^{-y})} = \overline{(\Phi f)(-y)}$. Also entspricht $f \mapsto f^\sharp$ der Abbildung $g \mapsto \overline{g(-\cdot)}$ auf $\mathcal{S}(\mathbb{R})$. $\square$

---

## 2. Autoritative Mellin-Konvention $\mathcal{M}_\infty$

**Definition (autoritativ, PD-2):**
$$\boxed{\mathcal{M}_\infty f(t) := \int_0^\infty f(x)\, x^{it}\, \frac{dx}{x}, \qquad t \in \mathbb{R}.}$$

Unter $x = e^y$:
$$\mathcal{M}_\infty f(t) = \int_{\mathbb{R}} (\Phi f)(y)\, e^{ity}\, dy = \widehat{\Phi f}(t) \cdot 2\pi$$
*(mit der Konvention $\hat{g}(t) = \int g(y)e^{ity}\,dy$).*

**Satz PD-2a** (Isomorphismus).
$$\mathcal{M}_\infty: \mathcal{S}_\infty \overset{\sim}{\longrightarrow} \mathcal{S}(\mathbb{R}).$$

*Beweis.* $\mathcal{M}_\infty = \mathcal{F} \circ \Phi$ (Fouriertransformation auf $\mathcal{S}(\mathbb{R})$ nach $\Phi$). Da $\mathcal{F}: \mathcal{S}(\mathbb{R}) \to \mathcal{S}(\mathbb{R})$ und $\Phi: \mathcal{S}_\infty \to \mathcal{S}(\mathbb{R})$ beide Isomorphismen sind, ist die Komposition ein Isomorphismus. $\square$

---

## 3. Involutionskompatibilität

**Satz PD-2b.**
$$\boxed{\mathcal{M}_\infty(f^\sharp)(t) = \overline{\mathcal{M}_\infty f(t)}.}$$

*Beweis.*
$$\mathcal{M}_\infty(f^\sharp)(t) = \int_0^\infty \overline{f(x^{-1})}\, x^{it}\, \frac{dx}{x}.$$
Substitution $u = x^{-1}$, $du/u = dx/x$:
$$= \int_0^\infty \overline{f(u)}\, u^{-it}\, \frac{du}{u} = \overline{\int_0^\infty f(u)\, u^{it}\, \frac{du}{u}} = \overline{\mathcal{M}_\infty f(t)}. \quad \square$$

**Folgerung.** Auf dem reellen Unterraum $\mathcal{S}_\infty^\sharp := \{f \in \mathcal{S}_\infty : f^\sharp = f\}$ ist $\mathcal{M}_\infty f$ reellwertig. Dieser Unterraum wird für die Weil-Distribution relevant sein.

---

## 4. Diagonalisierung des Skalierungsgenerators

**Definition.** Der Skalierungsgenerator auf $\mathcal{S}_\infty \subset L^2(\mathbb{R}_+^\times, dx/x)$:
$$H_\infty := -i\, x\frac{d}{dx}.$$

**Satz PD-2c.**
$$\boxed{\mathcal{M}_\infty \circ H_\infty = M_t \circ \mathcal{M}_\infty,}$$
wobei $M_t$ die Multiplikation mit der reellen Variablen $t$ bezeichnet.

*Beweis.* Für $f \in \mathcal{S}_\infty$:
$$\mathcal{M}_\infty(H_\infty f)(t) = \int_0^\infty (-i)\left(x\frac{d}{dx}f(x)\right) x^{it}\, \frac{dx}{x}.$$
Partielle Integration bezüglich $dx/x$ (Randterme verschwinden wegen $f \in \mathcal{S}_\infty$):
$$= \int_0^\infty f(x)\, (-i)\cdot(-it)\, x^{it}\, \frac{dx}{x} \cdot (-1) + \text{(Randterm = 0)}$$
Direkte Rechnung: $x\frac{d}{dx}(x^{it}) = it\cdot x^{it}$, daher
$$\mathcal{M}_\infty(-ix\tfrac{d}{dx}f)(t) = -i \int_0^\infty (x\tfrac{d}{dx}f)\, x^{it}\tfrac{dx}{x}.$$
Integration durch Teile ($u = x^{it}$, $dv = x\frac{d}{dx}f\cdot\frac{dx}{x} = f'(x)dx$):
$$= -i\left[-\int_0^\infty f(x)\cdot it\cdot x^{it}\tfrac{dx}{x}\right] = t\cdot \mathcal{M}_\infty f(t). \quad \square$$

**Folgerung.** $H_\infty$ ist auf $L^2(\mathbb{R}_+^\times, dx/x)$ wesentlich selbstadjungiert; sein Spektrum ist $\mathbb{R}$; die Spektralmaß ist das Lebesgue-Maß $dt$ auf $\mathbb{R}$. Für PD-4 (Skalierungsgenerator und regulierte Spur) ist damit die Grundlage gelegt.

---

## 5. Koordinatenübersetzung: Weil-Symmetrie

**Zwei Koordinatenebenen (autoritativ):**

| Ebene | Variable | Bedeutung |
|---|---|---|
| Interne Hilbertraumkoordinate | $t \in \mathbb{R}$ | Spektrum von $H_\infty$, Argument von $\mathcal{M}_\infty f$ |
| Arithmetische Spektralkoordinate | $s = \tfrac{1}{2} + it$ | Argument der Riemannschen $\zeta(s)$ und $\Gamma_{\mathbb{R}}(s)$ |

**Satz PD-2d** (Weil-Symmetrie als einfache Spiegelung).
$$\boxed{s \longleftrightarrow 1-s \qquad\Longleftrightarrow\qquad t \longleftrightarrow -t.}$$

*Beweis.* $1 - s = 1 - (\tfrac12 + it) = \tfrac12 - it = \tfrac12 + i(-t)$. $\square$

**Folgerung.** Die Funktionalgleichung $\xi(s) = \xi(1-s)$ wird in der $t$-Koordinate zur geraden Bedingung $\xi(\tfrac12 + it) = \xi(\tfrac12 - it)$, d.h. $\xi(\tfrac12 + it) \in \mathbb{R}$ für $t \in \mathbb{R}$. Die Symmetrie ist damit eine Realitätsbedingung, keine eigentliche Transformation.

---

## 6. Gammafaktor in der $t$-Koordinate

Der archimedische Faktor der vollständigen Riemannschen Zeta-Funktion:
$$\Gamma_{\mathbb{R}}(s) = \pi^{-s/2}\Gamma\!\left(\frac{s}{2}\right).$$

Logarithmische Ableitung in $s$:
$$\frac{\Gamma_{\mathbb{R}}'}{\Gamma_{\mathbb{R}}}(s) = -\frac{1}{2}\log\pi + \frac{1}{2}\psi\!\left(\frac{s}{2}\right), \qquad \psi = \frac{\Gamma'}{\Gamma}.$$

Übersetzung auf $s = \tfrac{1}{2} + it$:
$$\boxed{\gamma_\infty(t) := -\frac{1}{2}\log\pi + \frac{1}{2}\psi\!\left(\frac{1}{4} + \frac{it}{2}\right).}$$

Symmetrisierter Realteil (relevant für reelle Weil-Form auf $\mathcal{S}_\infty^\sharp$):
$$\boxed{\gamma_\infty^{\mathrm{sym}}(t) = -\log\pi + \operatorname{Re}\psi\!\left(\frac{1}{4} + \frac{it}{2}\right).}$$

**Vorbehalt (für PD-3):** Der genaue Vorfaktor $1$ oder $1/2$ vor $\gamma_\infty^{\mathrm{sym}}$ muss gegen die im Repository verwendete Normierung der vollständigen expliziten Formel auditiert werden. Er wird **nicht** in diesem Knoten festgeschrieben.

---

## 7. Typisierte Zurückweisung der unzentrierten Variante

Die unzentrierte Mellin-Transformation
$$(\mathcal{M}_s f)(s) = \int_0^\infty f(x)\, x^s\, \frac{dx}{x}$$
ist mit der Involution $f^\sharp(x) = \overline{f(x^{-1})}$ **nicht** Weil-symmetriekompatibel:

$$\mathcal{M}_s(f^\sharp)(s) = \overline{\mathcal{M}_s f(-\overline{s})},$$

d.h. die zugehörige Spiegelung ist $s \mapsto -\overline{s}$, nicht $s \mapsto 1 - \overline{s}$.

Die unzentrierte Variante **ist** kompatibel mit einer anderen Involution:
$$f^\#(x) := x^{-1}\overline{f(x^{-1})},$$
denn dann gilt $\mathcal{M}_s(f^\#)(s) = \overline{\mathcal{M}_s f(1 - \overline{s})}$. Das wäre eine legitime alternative Konvention, kollidiert aber mit der in PD-1 bereits fixierten Involution $f^\sharp$.

**Feststellung (typisiert, nicht nur verworfen):**

| Mellin | Passende Involution | Weil-Symmetrie in $s$ | Kompatibel mit PD-1 |
|---|---|---|---|
| $\mathcal{M}_\infty$ (zentriert, $x^{it}$) | $f^\sharp(x) = \overline{f(x^{-1})}$ | $s \mapsto 1-s \Leftrightarrow t\mapsto -t$ | **Ja** |
| $\mathcal{M}_s$ (unzentriert, $x^s$) | $f^\#(x) = x^{-1}\overline{f(x^{-1})}$ | $s \mapsto 1-\overline{s}$ direkt | Nein (andere Involution) |

Diese Tabelle ist dauerhafter Bestandteil des DAG; spätere Knoten dürfen nicht stillschweigend zur unzentrierten Variante wechseln.

---

## 8. Vollständige Aussagenliste (Beweiszusammenfassung)

| Aussage | Satz | Status |
|---|---|---|
| $\mathcal{S}_\infty \cong \mathcal{S}(\mathbb{R})$ über $f \mapsto [y \mapsto f(e^y)]$ | PD-1a | $\checkmark$ |
| $\mathcal{M}_\infty: \mathcal{S}_\infty \overset{\sim}{\to} \mathcal{S}(\mathbb{R})$ | PD-2a | $\checkmark$ |
| $\mathcal{M}_\infty(f^\sharp) = \overline{\mathcal{M}_\infty f}$ | PD-2b | $\checkmark$ |
| $\mathcal{M}_\infty H_\infty \mathcal{M}_\infty^{-1} = M_t$ | PD-2c | $\checkmark$ |
| $s \leftrightarrow 1-s \Leftrightarrow t \leftrightarrow -t$ | PD-2d | $\checkmark$ |
| $\gamma_\infty(t) = -\tfrac12\log\pi + \tfrac12\psi(\tfrac14 + \tfrac{it}{2})$ | §6 | $\checkmark$ (Vorfaktor für PD-3 reserviert) |
| $\mathcal{M}_s$ mit $f^\#$ kompatibel, aber PD-1-Kollision | §7 | typisiert festgehalten |

---

## 9. DAG-Statusaktualisierung

$$[O\text{-}220\text{-}1\text{-PD2-Mellin-normalization}] \quad \checkmark[K/M]$$

$$[O\text{-}220\text{-}1\text{-PD1-test-space}] \quad \checkmark[K/M]_{\mathrm{part}}$$

In `NEU-220_Gammafaktor_Quelltyp_und_Zielraum.md` sind PD-1 und PD-2 damit wie folgt zu aktualisieren:

| Pflichtentscheidung | Alter Status | Neuer Status |
|---|---|---|
| PD-1 Testfunktionsraum | ?[O] | $\checkmark[K/M]_{\mathrm{part}}$ (kleinerer Unterraum für PD-3 offen) |
| PD-2 Mellin-Normierung | ?[O] | $\checkmark[K/M]$ |
| PD-3 Gamma-Distribution | ?[O] | **freigegeben**: beginnt mit $t \mapsto -\tfrac12\log\pi + \tfrac12\psi(\tfrac14+\tfrac{it}{2})$ |

---

## 10. Freigabe für PD-3

PD-3 (Gamma-Distribution, Weg A) kann jetzt ohne weitere Konventionsunsicherheit mit dem konkreten Symbol
$$t \longmapsto -\frac{1}{2}\log\pi + \frac{1}{2}\psi\!\left(\frac{1}{4} + \frac{it}{2}\right)$$
beginnen. Zu beweisen ist dort:

- Stetigkeit von $f \mapsto \int_{\mathbb{R}} \gamma_\infty(t)\, (\mathcal{M}_\infty f)(t)\, dt$ auf $\mathcal{S}_\infty$
- Konvergenz des Integrals (Wachstum von $\psi$ auf der kritischen Linie)
- Exakte Übereinstimmung mit dem $\Gamma_{\mathbb{R}}'/\Gamma_{\mathbb{R}}$-Term der vollständigen Weil-Explizitformel
- Vorfaktor-Audit gegen die Repository-Normierung

---

## Abhängigkeiten

| Datei | Rolle |
|---|---|
| `NEU-220_Gammafaktor_Quelltyp_und_Zielraum.md` | Übergeordneter Rahmenknoten |
| `NEU-219_Finalaudit_Gesamtabschluss.md` | Exportursprung `[O-219-6]` |
