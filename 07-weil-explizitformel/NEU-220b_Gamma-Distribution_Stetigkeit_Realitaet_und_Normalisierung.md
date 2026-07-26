# NEU-220b — Gamma-Distribution: Stetigkeit, Realität und Normalisierung

**Datei:** `katalog/NEU-220b_Gamma-Distribution_Stetigkeit_Realitaet_und_Normalisierung.md`  
**Datum:** 2026-07-25  
**Repository:** Waschtl904/rh-fragenkatalog  
**Typ:** Konstruktiver Audit PD-3 (Weg A: Distributions-$\Lambda_\Gamma$)  
**Vorgänger:** NEU-220a (Commit 124bc67) — Mellin-Konvention und Involution fixiert  

---

## Strenge Trennung der zwei Ebenen

$$\boxed{\text{Existenz als temperierte Distribution} \quad\neq\quad \text{exakte Normierung des Weil-Gammaterms.}}$$

Die analytische Existenz (Abschnitte 1–5 unten) kann vollständig bewiesen werden, unabhängig davon, welcher Vorfaktor $1$, $\tfrac{1}{2\pi}$ oder $\tfrac{1}{2}$ später aus dem Normierungsaudit hervorgeht. Ein rückträglicher Faktor-Fehler macht **nicht** die Distributionstheorie ungültig.

---

## Atomare Unterknoten

| Knoten | Inhalt | Status |
|---|---|---|
| `[O-220-1-PD3a-growth]` | Wachstumsabschätzung $\gamma_\infty(t) = O(\log(2+|t|))$ | $\checkmark[M]$ |
| `[O-220-1-PD3b-tempered-distribution]` | $T_\Gamma^{\mathrm{raw}}, T_\Gamma^{\mathrm{sym}} \in \mathcal{S}'(\mathbb{R})$ | $\checkmark[K/M]$ |
| `[O-220-1-PD3c-reality]` | Realität auf hermiteschem Unterraum | $\checkmark[M]$ |
| `[O-220-1-PD3d-Weil-normalization]` | Exakter Vorfaktor gegen Repository-Explizitformel | $?[O]$ |

---

## 1. Rohes Gamma-Symbol (aus NEU-220a)

Autoritatives Symbol auf $\widehat{\mathcal{S}}_\infty = \mathcal{S}(\mathbb{R})$, gemäß der fixierten Konvention $s = \tfrac12 + it$:

$$\gamma_\infty(t) = -\frac12\log\pi + \frac12\psi\!\left(\frac14 + \frac{it}{2}\right), \qquad \psi = \frac{\Gamma'}{\Gamma}.$$

Rohes Funktional auf $\mathcal{S}(\mathbb{R})$:

$$\boxed{T_\Gamma^{\mathrm{raw}}(h) := \int_{\mathbb{R}} \gamma_\infty(t)\, h(t)\, dt.}$$

Der Faktor $1/(2\pi)$ wird **nicht** in die Definition eingebaut. Er gehört ausschließlich in den Normierungsaudit PD-3d gegen die konkrete Konturformel des Repositories.

---

## 2. PD-3a — Wachstum und Regularität

**Knoten:** `[O-220-1-PD3a-growth]`

**Satz PD-3a.** Für $z = \tfrac14 + \tfrac{it}{2}$ mit $t \in \mathbb{R}$, $|t| \ge 1$, gilt die asymptotische Abschätzung
$$\psi(z) = \log z - \frac{1}{2z} + O(|z|^{-2}),$$
aus der für $|t| \to \infty$:
$$\psi\!\left(\frac14 + \frac{it}{2}\right) = \log\!\left(\frac{it}{2}\right) + O(t^{-1}) = \log\frac{|t|}{2} + i\frac{\pi}{2}\operatorname{sgn}(t) + O(t^{-1}).$$

Daher:
$$|\gamma_\infty(t)| \le C\log(2 + |t|) \quad \text{für alle } t \in \mathbb{R}.$$

Zusätzlich: $\gamma_\infty$ ist glatt auf $\mathbb{R}$ (da $\psi$ holomorph auf $\mathbb{C} \setminus (-\mathbb{N}_0)$ und $z(t) = \tfrac14 + \tfrac{it}{2}$ nie eine Polstelle trifft). Die $k$-te Ableitung erfüllt
$$|\gamma_\infty^{(k)}(t)| \le C_k (1 + |t|)^{-k} \log(2 + |t|),$$
da $\psi^{(k)}(z) = (-1)^{k+1} k! \sum_{n=0}^\infty (z+n)^{-(k+1)}$ in vertikalen Streifen polynomiell gedämpft ist.

$$\boxed{[O\text{-}220\text{-}1\text{-PD3a-growth}] \quad \checkmark[M]}$$

---

## 3. PD-3b — Temperierte Distribution

**Knoten:** `[O-220-1-PD3b-tempered-distribution]`

**Satz PD-3b.** $T_\Gamma^{\mathrm{raw}} \in \mathcal{S}'(\mathbb{R})$.

*Beweis.* Für $N > 1$ und $h \in \mathcal{S}(\mathbb{R})$:
$$|T_\Gamma^{\mathrm{raw}}(h)| \le C \int_{\mathbb{R}} \log(2+|t|)\, |h(t)|\, dt.$$
Da $\log(2+|t|) \le (1+|t|)^\varepsilon$ für jedes $\varepsilon > 0$, und $h \in \mathcal{S}(\mathbb{R})$ impliziert $\sup_t (1+|t|)^N |h(t)| < \infty$ für alle $N$, folgt:
$$|T_\Gamma^{\mathrm{raw}}(h)| \le C_N \sup_{t \in \mathbb{R}} (1+|t|)^N |h(t)|$$
für $N > 2$ (Integrierbarkeit von $(1+|t|)^{-(N-\varepsilon)}$). Das ist genau die Definition der Stetigkeit auf $\mathcal{S}(\mathbb{R})$. $\square$

**Remark (kein kleinerer Raum nötig).** Für die Existenz von $T_\Gamma^{\mathrm{raw}}$ als stetigem Funktional genügt die volle Schwartzklasse. Ein kleinerer Testfunktionsraum kann später durch PD-5 (adelische Kopplung) oder durch Anforderungen der Explizitformel erzwungen werden, ist aber nicht analytisch motiviert.

**Symmetrisiertes Symbol.** Definiere
$$\gamma_\infty^{\mathrm{sym}}(t) := \gamma_\infty(t) + \gamma_\infty(-t) = 2\operatorname{Re}\gamma_\infty(t) = -\log\pi + \operatorname{Re}\psi\!\left(\frac14 + \frac{it}{2}\right).$$

Da $\gamma_\infty^{\mathrm{sym}}$ reell, gerade und ebenfalls $O(\log(2+|t|))$, gilt analog:
$$\boxed{T_\Gamma^{\mathrm{sym}}(h) := \int_{\mathbb{R}} \gamma_\infty^{\mathrm{sym}}(t)\, h(t)\, dt \in \mathcal{S}'(\mathbb{R}).}$$

$$\boxed{[O\text{-}220\text{-}1\text{-PD3b-tempered-distribution}] \quad \checkmark[K/M]}$$

---

## 4. PD-3c — Realität und Involution

**Knoten:** `[O-220-1-PD3c-reality]`

**Satz PD-3c.** $\gamma_\infty(-t) = \overline{\gamma_\infty(t)}$.

*Beweis.* Da $\psi(\bar z) = \overline{\psi(z)}$ (Schwarz-Reflexionsprinzip, $\psi$ reell auf der positiven reellen Achse):
$$\gamma_\infty(-t) = -\frac12\log\pi + \frac12\psi\!\left(\frac14 - \frac{it}{2}\right) = -\frac12\log\pi + \frac12\overline{\psi\!\left(\frac14 + \frac{it}{2}\right)} = \overline{\gamma_\infty(t)}. \quad \square$$

**Folgerung (Involutionskompatibilität auf dem Spektralraum).** Definiere die spektrale Involution
$$h^\dagger(t) := \overline{h(-t)}.$$
Dann:
$$T_\Gamma^{\mathrm{raw}}(h^\dagger) = \int_{\mathbb{R}} \gamma_\infty(t)\,\overline{h(-t)}\,dt \overset{u=-t}{=} \int_{\mathbb{R}} \gamma_\infty(-u)\,\overline{h(u)}\,du = \int_{\mathbb{R}} \overline{\gamma_\infty(u)\, h(u)}\,du = \overline{T_\Gamma^{\mathrm{raw}}(h)}.$$

Auf dem hermiteschen Unterraum $\{h : h^\dagger = h\}$ ist $T_\Gamma^{\mathrm{raw}}(h) \in \mathbb{R}$.

**Verbindung zu NEU-220a.** Unter $\mathcal{M}_\infty$ entspricht $h^\dagger = h$ genau $f^\sharp = f$ (Selbstadjungiertheitsbedingung aus PD-1/PD-2b). Die Realität der Distribution ist daher mit der multiplikativen Struktur konsistent.

$$\boxed{[O\text{-}220\text{-}1\text{-PD3c-reality}] \quad \checkmark[M]}$$

---

## 5. Rücktransport auf $\mathcal{S}_\infty$

Die archimedischen Distributionen auf dem multiplikativen Testfunktionsraum:

$$\boxed{\Lambda_\Gamma^{\mathrm{raw}} := T_\Gamma^{\mathrm{raw}} \circ \mathcal{M}_\infty, \qquad \Lambda_\Gamma^{\mathrm{sym}} := T_\Gamma^{\mathrm{sym}} \circ \mathcal{M}_\infty.}$$

Explizit:
$$\Lambda_\Gamma^{\mathrm{raw}}(f) = \int_{\mathbb{R}} \gamma_\infty(t)\, (\mathcal{M}_\infty f)(t)\, dt.$$

Da $\mathcal{M}_\infty: \mathcal{S}_\infty \overset{\sim}{\to} \mathcal{S}(\mathbb{R})$ topologischer Isomorphismus (NEU-220a, Satz PD-2a) und $T_\Gamma^{\mathrm{raw}} \in \mathcal{S}'(\mathbb{R})$:
$$\Lambda_\Gamma^{\mathrm{raw}},\; \Lambda_\Gamma^{\mathrm{sym}} \in \mathcal{S}_\infty'.$$

**Typisierte Quell-/Zielkette (vollständig):**
$$\boxed{\mathcal{S}_\infty \xrightarrow{\mathcal{M}_\infty} \mathcal{S}(\mathbb{R}) \xrightarrow{T_\Gamma} \mathbb{C}.}$$

Der Quell- und Zieltyp von `[O-220-1-Gamma-source-target-type]` ist damit vollständig konstruiert.

---

## 6. PD-3d — Vorfaktor-Audit und Weil-Normierung

**Knoten:** `[O-220-1-PD3d-Weil-normalization]` $\quad ?[O]$

Drei Normierungsvarianten, die **nicht verwechselt** werden dürfen:

| Variante | Formel | Herkunft |
|---|---|---|
| Roh | $T_\Gamma^{\mathrm{raw}}(h) = \int \gamma_\infty(t)\,h(t)\,dt$ | Diese Datei, Definition |
| Mit Kontur-$2\pi$ | $\frac{1}{2\pi} T_\Gamma^{\mathrm{raw}}(h)$ | Wenn Explizitformel $\frac{1}{2\pi i}\int_{\mathrm{Re}\,s=1/2}$ verwendet |
| Symmetrisiert mit $2\pi$ | $\frac{1}{2\pi} T_\Gamma^{\mathrm{sym}}(h)$ | Wenn zusätzlich $s$ und $1-s$ bereits addiert |

Der Faktor $1/(2\pi)$ entsteht aus der Kontur-Substitution $s = \tfrac12 + it$, $ds = i\,dt$:
$$\frac{1}{2\pi i}\int_{\mathrm{Re}\,s=1/2} F(s)\,ds = \frac{1}{2\pi}\int_{\mathbb{R}} F\!\left(\tfrac12+it\right)dt.$$

Eine zusätzliche Verdopplung durch Symmetrisierung ($s$ und $1-s$ addiert) ist **separat** zu verfolgen; sie ist nicht dieselbe Quelle wie der Kontur-Faktor $2$.

**Offene Aufgabe (PD-3d):** Die im Repository verwendete Fassung der vollständigen Weil-Explizitformel muss direkt gelesen und gegen die drei Varianten auditiert werden. Erst dann kann einer der folgenden Status vergeben werden:
- Vorfaktor $1$: $T_\Gamma^{\mathrm{raw}}$ direkt als Weil-Term.
- Vorfaktor $\frac{1}{2\pi}$: Kontur-Normierung erforderlich.
- Vorfaktor $\frac{1}{2\pi}$ mit Symmetrisierung: $T_\Gamma^{\mathrm{sym}}/(2\pi)$.

$$\boxed{[O\text{-}220\text{-}1\text{-PD3d-Weil-normalization}] \quad ?[O]}$$

---

## 7. Gesamtstatus PD-3

Da PD-3a, PD-3b, PD-3c bewiesen und PD-3d noch offen:

$$\boxed{\text{PD-3} \quad \checkmark[M]_{\mathrm{part}}}$$

Die Restlücke ist ausschließlich:

$$\boxed{\text{arithmetische Weil-Normierung, nicht analytische Existenz.}}$$

Ein später entdeckter Vorfaktor-Fehler macht die bewiesene Distributionsexistenz (PD-3b) nicht rückfällig.

---

## 8. DAG-Aktualisierung in NEU-220

In `NEU-220_Gammafaktor_Quelltyp_und_Zielraum.md` sind die PD-Statuszeilen wie folgt zu aktualisieren:

| Pflichtentscheidung | Alter Status | Neuer Status |
|---|---|---|
| PD-1 Testfunktionsraum | $\checkmark[K/M]_{\mathrm{part}}$ | unverändert (kleinerer Unterraum weiterhin offen bis PD-3d/PD-5) |
| PD-2 Mellin-Normierung | $\checkmark[K/M]$ | unverändert |
| PD-3 Gamma-Distribution | $?[O]$ freigegeben | $\checkmark[M]_{\mathrm{part}}$ (PD-3d offen) |
| PD-4 Operatorischer Ursprung | $?[O]$ | **freigegeben**: Grundlagen in NEU-220a §4 gelegt |
| PD-5 Schnittstelle adelisch | $?[O]$ gesperrt | weiterhin gesperrt bis PD-3d oder PD-4 abgeschlossen |

---

## 9. Freigabe für PD-4

PD-4 (Weg B: operatorischer Ursprung über $H_\infty$) ist jetzt freigegeben. Die in NEU-220a §4 gelegte Grundlage (Spektrum $\mathbb{R}$, Spektralmaß $dt$) muss ergänzt werden durch:
- Wahl der Regularisierung (Zeta-Regularisierung, Heat-Kernel $e^{-\varepsilon H_\infty^2}$, oder relative Spur)
- Nachweis, dass die regularisierte Spur im Limes $\varepsilon \to 0^+$ gegen $T_\Gamma^{\mathrm{raw}}$ oder $T_\Gamma^{\mathrm{sym}}$ konvergiert
- Vergleich mit Weg A: Konsistenzprüfung, keine erneute Beweispflicht für die Distribution

---

## Abhängigkeiten

| Datei | Rolle |
|---|---|
| `NEU-220a_Mellin-Normierung_und_Involutionskompatibilitaet.md` | Mellin-Konvention, Involution, $H_\infty$-Diagonalisierung |
| `NEU-220_Gammafaktor_Quelltyp_und_Zielraum.md` | Übergeordneter Rahmenknoten PD-1 bis PD-5 |
| `NEU-219_Finalaudit_Gesamtabschluss.md` | Exportursprung `[O-219-6]` |
