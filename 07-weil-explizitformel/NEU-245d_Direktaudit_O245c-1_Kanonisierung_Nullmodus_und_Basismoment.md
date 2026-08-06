# NEU-245d — Direktaudit [O-245c/1]: Kanonisierung, Nullmodus und Basismoment

**Kennung:** NEU-245d  
**Ordner:** `07-weil-explizitformel/`  
**Datum:** 2026-08-06  
**Vorgänger:** NEU-245c \(\checkmark[M]_{\mathrm{part}}\) — M3-No-Go, M4 als neue notwendige Bedingung  
**Knoten:** \([O\text{-}245c/1]\)  
**Nachfolger (gesperrt bis Abschluss):** \([O\text{-}245c/2]\) — Identitätsaudit \(M_{X,N}(w)\to M_\Xi(w)\)

> **Korrekturblock K1–K5 eingearbeitet** (2026-08-06): vier Überbuchungen und ein Exponentenfehler aus dem Erstaudit berichtigt; Näheres in Abschnitt 10.

---

## Gegenstand

NEU-245c hat ergeben:

- M3 (Positivitätsbeweis allein) reicht nicht als Abschlussinstanz.
- M4 (Resolventen-/Momentidentifikation) ist neue notwendige Bedingung.
- Kein additiver Kreuzterm; kein Vollblock-No-Go aktiviert.

\([O\text{-}245c/1]\) prüft deshalb **ausschließlich das Basistripel**:

\[
\left(\mathcal{H}_N^{\mathrm{rel}},\; D_N^{\mathrm{rel}},\; \Psi_N\right)
\]

Noch keine höheren Momente, noch kein Vergleich mit \(M_\Xi\).

---

## 1 — Quellenexistenz

### 1.1 \(\mathcal{H}_N^{\mathrm{rel}}\)

**Frage:** Ist \(\mathcal{H}_N^{\mathrm{rel}}\) tatsächlich als Hilbertraum definiert, nicht nur formal benannt?

**Quellenlage (NEU-221, NEU-221e):**  
\(\mathcal{H}_N^{\mathrm{rel}}\) wird als Quotient

\[
\mathcal{H}_N^{\mathrm{rel}} = \mathcal{H}_{N,\mathrm{raw}} \big/ \mathcal{N}_{W_{\mathrm{res}},\mathrm{rel}}
\]

als GNS-Abschluss über die relative Wres-Paarung eingeführt (NEU-221e §2.1–2.2).

**Befund:** Die Quotientenkonstruktion ist als abstrakter Hilbertraum vollständig definiert. Die Norm stammt aus der induzierten Wres-Paarung. ✓

**Offener Punkt:** Eine explizite Orthonormalbasis oder ein konkretes Spektraldichteobjekt für \(\mathcal{H}_N^{\mathrm{rel}}\) wird in keiner Quelle bis NEU-245c angegeben. Für [O-245c/1] genügt die abstrakte Definition; für [O-245c/2] wird eine direktere Beschreibung erforderlich sein.

---

### 1.2 \(D_N^{\mathrm{rel}}\) — Domäne, Symmetrie und essentielle Selbstadjungiertheit

**Frage:** Ist \(D_N^{\mathrm{rel}}\) mit Domäne und Selbstadjungiertheit definiert?

**Quellenlage:**  
\(D_N^{\mathrm{rel}}\) wird in NEU-221c als zyklischer Feshbach-Weyl-Kandidat mit quadratischer Resolventenstruktur eingeführt. NEU-221d behauptet, die essentielle Selbstadjungiertheit sei durch NEU-53/54 abgeschlossen.

**[K1] Korrektur — Quellenseitige Präzisierung:**  
Die Buchung in NEU-221d ist zu stark:

- **NEU-53** bezeichnet die essentielle Selbstadjungiertheit als **offenen ersten Beweisengpass**.
- **NEU-54** formuliert die Nelson-Bedingungen, beweist sie aber **nicht**.
- **NEU-55** erhält essentielle Selbstadjungiertheit nur **konditional** unter den noch offenen Schur-/Nelson-Abschätzungen.

Verbindlich gilt daher:

\[
D_N^{\mathrm{rel}} \text{ symmetrisch} \quad \checkmark[M]
\]
\[
D_N^{\mathrm{rel}} \text{ wesentlich selbstadjungiert} \quad ?[O]
\]

---

### 1.3 \(\Psi_N \in \mathcal{H}_N^{\mathrm{rel}}\) — Quotientabstieg und Kanonizität

**Frage:** Ist \(\Psi_N\) als kanonischer, hebungsunabhängiger Vektor konstruiert?

**Quellenlage (NEU-221e):**  
NEU-221e beweist das Quotientabstiegskriterium:

\[
\widetilde{T}_p^{\mathrm{raw}}\bigl(\Delta_p^{\mathrm{adm}}\bigr) \subseteq \mathcal{N}_{W_{\mathrm{res}},\mathrm{rel}}
\]

genau dann, wenn die Bildklasse unabhängig von der zulässigen Hebung ist.

**[K2] Korrektur:**  
NEU-221e sagt ausdrücklich, dass diese Inklusion **weder für \(\Delta_p^{\mathrm{adm}}\) noch für den stärkeren Raum \(K_p\) bewiesen** ist. Spektralmaßinvarianz und intrinsische Sektion bleiben offen.

Damit ist **nicht** gesichert:

\[
\Psi_p[\widehat{\varepsilon}_p'] = \Psi_p[\widehat{\varepsilon}_p] \quad \text{für alle zulässigen Hebungen.}
\]

Verbindlich:

\[
\text{Quotientabstiegskriterium} \quad \checkmark[M]
\]
\[
\Psi_N \text{ als intrinsische, hebungsunabhängige Klasse} \quad ?[O]
\]

Auch das zugehörige Spektralmaß \(\mu_{\Psi_N}^{D_N^{\mathrm{rel}}}\) ist damit noch nicht intrinsisch fixiert.

---

## 2 — Kanonizität von \(\Psi_N\) — Zusammenfassung

Das Quotientabstiegskriterium ist quellenseitig formuliert \(\checkmark[M]\), aber der tatsächliche intrinsische Abstieg ist nicht durchgeführt. Das bedeutet: Die Existenz von \(\Psi_N\) als wohldefinierter Quotientenklasse steht unter der Voraussetzung, dass die noch offene Inklusion bestätigt wird.

---

## 3 — Nullmodusfreiheit

**Zu prüfende Bedingung:**

\[
\boxed{E_{D_N^{\mathrm{rel}}}(\{0\})\,\Psi_N = 0}
\]

**Präzisierung gegenüber NEU-221c:**  
Es ist nicht erforderlich, dass \(0 \in \rho(D_N^{\mathrm{rel}})\) global gilt. Ein globaler Kern \(\ker D_N^{\mathrm{rel}} \neq \{0\}\) wäre zulässig, sofern \(\Psi_N\) orthogonal dazu ist.

**[K3] Korrektur:**  
NEU-245d (Erstfassung) behauptete, NEU-221d bestätige \(E_{D_N^{\mathrm{rel}}}(\{0\})\Psi_N=0\) für den NEU-46-Sektor. Das ist falsch.

NEU-221d führt diese Bedingung als **offenen Folgeknoten \([O\text{-}221\text{-}1c1b]\)** mit Status \(?[O]\). Die Niedrigenergieabschätzung wird dort als **zu beweisende Bedingung** formuliert, nicht als Ergebnis.

Verbindlich:

\[
\boxed{E_{D_N^{\mathrm{rel}}}(\{0\})\,\Psi_N=0 \quad ?[O]}
\]

und zwar sowohl für den NEU-46-Kandidaten als auch für den allgemeinen adelischen Quotienten.

---

## 4 — Existenz des Basismoments und Niedrigenergie-Kriterium

**Zu zeigen:**

\[
\boxed{m_{0,N} = \left\langle \Psi_N,\, (D_N^{\mathrm{rel}})^{-2}\,\Psi_N \right\rangle = \int_{\mathbb{R}} |\lambda|^{-2}\,d\mu_{\Psi_N}(\lambda) < \infty}
\]

Äquivalent: \(\Psi_N \in \mathcal{D}(|D_N^{\mathrm{rel}}|^{-1})\).

Wenn diese Bedingung erfüllt ist:

\[
\Omega_{X,N} := (D_N^{\mathrm{rel}})^{-1}\,\Psi_N \quad \text{wohldefiniert}, \qquad m_{0,N} = \|\Omega_{X,N}\|^2.
\]

### [K4] Korrektur — Niedrigenergie-Schwelle ist \(\alpha > 2\), nicht \(\alpha > 1\)

Setze

\[
F_N(\varepsilon) = \mu_{\Psi_N}\bigl((-\varepsilon,\varepsilon)\setminus\{0\}\bigr).
\]

Die Konvergenz \(m_{0,N} < \infty\) ist äquivalent zu

\[
\int_0^{\varepsilon_0} \frac{F_N(r)}{r^3}\,dr < \infty.
\]

*Herleitung:* Durch Layered-cake-Umschreiben gilt

\[
\int_0^{\varepsilon_0} |\lambda|^{-2}\,d\mu(\lambda)
= \int_0^{\varepsilon_0} \frac{F_N(r)}{r^3}\,dr + \text{(konvergenter Randterm)}.
\]

Für eine Potenzschranke \(F_N(r) = O(r^\alpha)\) entsteht

\[
\int_0^{\varepsilon_0} r^{\alpha-3}\,dr,
\]

welche **genau für \(\alpha > 2\)** konvergiert. Die bisher eingetragene Schwelle \(\alpha > 1\) ist **falsch**.

Außerdem gilt notwendig:

\[
m_{0,N} < \infty \quad \Longrightarrow \quad F_N(\varepsilon) = o(\varepsilon^2).
\]

**Schwellentabelle für höhere Momente:**

| Moment | Bedingung | Hinreichende Potenzschranke |
|---|---|---|
| \(m_{0,N}\) | \(\int |\lambda|^{-2}\,d\mu < \infty\) | \(F_N(\varepsilon) = O(\varepsilon^\alpha),\; \alpha > 2\) |
| \(m_{1,N}\) | \(\int |\lambda|^{-4}\,d\mu < \infty\) | \(\alpha > 4\) |
| \(m_{2,N}\) | \(\int |\lambda|^{-6}\,d\mu < \infty\) | \(\alpha > 6\) |
| \(m_{k,N}\) | \(\int |\lambda|^{-2k-2}\,d\mu < \infty\) | \(\alpha > 2k+2\) |

**Befund:** \(\checkmark[M]_{\mathrm{neg,Quelle}}\) — keine Quelle bis NEU-245c liefert eine Abschätzung von \(F_N\) nahe 0.

---

## 5 — Normierung

**Regel:** Die Normierung von \(\Psi_N\) darf nicht nachträglich so gewählt werden, dass \(m_{0,N}=\mu_0\). Das wäre tautologisch.

Die Konstruktion in NEU-221e lässt die Skalierung von \(\Psi_N\) durch die Wres-Paarung bestimmen, nicht durch eine \(m_{0,N}\)-Forderung. Tautologieschutz ist **strukturell vorhanden** \(\checkmark[M]\).

**Unterscheidung (Protokoll):**

| Begriff | Status |
|---|---|
| Existenz von \(m_{0,N}\) | \(?[O]\) — Punkt 4 nicht belegt |
| Arithmetisch kanonischer Wert von \(m_{0,N}\) | \(?[O]\) — setzt Existenz + adelische Quellennormierung voraus |
| Tautologieschutz | \(\checkmark[M]\) |

---

## 6 — M1-Kompatibilität: Architekturtyp und globaler Kopplungsgehalt

**Typfrage:**

\[
D_N^{\mathrm{rel}} \neq \bigoplus_{p \le N} D_{p,N}^{\mathrm{rel}} \quad\text{quellenseitig belegt?}
\]

**Quellenlage (NEU-221c, NEU-221d, NEU-245b):**  
\(D_N^{\mathrm{rel}}\) wird als zyklischer Feshbach-Weyl-Kandidat mit Mischblock-Struktur eingeführt. Die zyklische Konstruktion aus NEU-46 erzwingt eine nicht-diagonale Kopplungsarchitektur.

**[K5] Korrektur:**  
NEU-221d führt den konkreten globalen Kopplungsgehalt als offenen Knoten \([O\text{-}221\text{-}1c1d]\). NEU-221e warnt, dass eine Vektordirektsumme allein **keine gekoppelte Spektralmaßstruktur** erzeugt.

Verbindlich:

\[
\text{M1-kompatibler Konstruktionstyp} \quad \checkmark[K/M]
\]
\[
\text{konkreter globaler Kopplungsgehalt} \quad ?[O]
\]

Quantitative Positivitätswirkung (M1-Stärke) wird hier nicht bewertet — das ist Teil von [O-245c/2].

---

## 7 — Revidierte Gesamtbilanz [O-245c/1]

| Aussage | Status |
|---|---|
| Relativer Ziel- und Quotiententyp | \(\checkmark[K/M]_{\mathrm{part}}\) |
| Symmetrie von \(D_N^{\mathrm{rel}}\) | \(\checkmark[M]\) |
| Essentielle Selbstadjungiertheit | \(?[O]\) |
| Quotientabstiegskriterium für \(\Psi_N\) | \(\checkmark[M]\) |
| Tatsächlicher intrinsischer Abstieg von \(\Psi_N\) | \(?[O]\) |
| Nullmodusfreiheit | \(?[O]\) |
| \(m_{0,N}<\infty\) | \(\checkmark[M]_{\mathrm{neg,Quelle}}\) |
| Tautologieschutz Normierung | \(\checkmark[M]\) |
| M1-kompatibler Architekturtyp | \(\checkmark[K/M]\) |
| Konkreter globaler Kopplungsgehalt | \(?[O]\) |

**Gesamtstatus:**

\[
\boxed{[O\text{-}245c/1] \quad \checkmark[M]_{\mathrm{part}}}
\]

Die Freigabe von \([O\text{-}245c/2]\) bleibt gesperrt.

---

## 8 — Nächster atomarer Knoten

Der nächste Schritt ist nicht unmittelbar der Vergleich \(M_{X,N}\to M_\Xi\), sondern:

\[
\boxed{[O\text{-}245d/1] \quad \text{Niedrigenergie-Spektralmassenaudit}}
\]

Sein erster Test:

1. \(\mu_{\Psi_N}(\{0\}) = 0\)
2. \(\displaystyle\int_0^{\varepsilon_0} \frac{F_N(r)}{r^3}\,dr < \infty\)
3. Idealerweise eine sichtbare Spektrallücke:
\[
\operatorname{supp}\mu_{\Psi_N} \cap (-\delta_N,\delta_N) = \varnothing
\]

Erst nach positivem Abschluss von Punkt 2 (mindestens) ist

\[
\Omega_{X,N} = (D_N^{\mathrm{rel}})^{-1}\Psi_N
\]

als belastbarer zyklischer Vektor definiert und \([O\text{-}245c/2]\) freigeschaltet.

---

## 9 — Quellenregister

| Kürzel | Dokument |
|---|---|
| NEU-221 | Adelische Momentquelle für den positiven Weil-Operator |
| NEU-221c | Zyklischer Feshbach-Weyl-Kandidat und quadratische Resolvente |
| NEU-221d | Direktextraktion NEU-46, zyklischer Sektor, Nullmodusaudit |
| NEU-221e | Affine Hebungsfaser, Wres-Quotient, Spektralmassabstieg \(\Psi_p\) |
| NEU-245b | Typaudit \([O\text{-}220\text{-}1f_0]\), Mindestarchitektur, globale Archimedes-Prim-Kopplung |
| NEU-245c | Audit Feshbach-Weyl-Kandidat gegen \([O\text{-}245b/1]\), M1–M4 |

---

## 10 — Korrekturprotokoll

Eingearbeitete Korrekturen gegenüber der Erstfassung (2026-08-06):

| Block | Korrektur | Quelle |
|---|---|---|
| K1 | Selbstadjungiertheit: NEU-221d-Buchung übernommen; jetzt quellenkritisch aufgelöst in Symmetrie \(\checkmark[M]\) vs. essentielle SA \(?[O]\) | NEU-53, NEU-54, NEU-55 |
| K2 | Kanonizität: Quotientabstiegskriterium \(\checkmark[M]\) vs. tatsächlicher intrinsischer Abstieg \(?[O]\); Spektralmaßinvarianz offen | NEU-221e |
| K3 | Nullmodusfreiheit: auch für NEU-46-Sektor nicht belegt; Knoten \([O\text{-}221\text{-}1c1b]\) mit \(?[O]\) | NEU-221d |
| K4 | Exponentenschwelle: \(\alpha>1\) ersetzt durch \(\alpha>2\); vollständige Layered-cake-Herleitung ergänzt; Schwellentabelle für \(m_{k,N}\) eingefügt | NEU-221d |
| K5 | M1-Kopplungsgehalt: Architekturtyp \(\checkmark[K/M]\) vs. konkrete globale Kopplung \(?[O]\) | NEU-221d \([O\text{-}221\text{-}1c1d]\), NEU-221e |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung des RH-Forschungsjournals*
