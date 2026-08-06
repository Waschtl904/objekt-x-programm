# NEU-245d — Direktaudit [O-245c/1]: Kanonisierung, Nullmodus und Basismoment

**Kennung:** NEU-245d  
**Ordner:** `07-weil-explizitformel/`  
**Datum:** 2026-08-06  
**Vorgänger:** NEU-245c \(\checkmark[M]_{\mathrm{part}}\) — M3-No-Go, M4 als neue notwendige Bedingung  
**Knoten:** \([O\text{-}245c/1]\)  
**Nachfolger (gesperrt bis Abschluss):** \([O\text{-}245c/2]\) — Identitätsaudit \(M_{X,N}(w)\to M_\Xi(w)\)

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

der GNS-Abschluss über die relative Wres-Paarung eingeführt (NEU-221e §2.1–2.2).

**Befund:** Die Quotientenkonstruktion ist als abstrakter Hilbertraum vollständig definiert. Die Norm stammt aus der induzierten Wres-Paarung. ✓

**Offener Punkt:** Die explizite Orthonormalbasis oder ein konkretes Spektraldichteobjekt für \(\mathcal{H}_N^{\mathrm{rel}}\) wird in keiner Quelle bis NEU-245c angegeben. Für [O-245c/1] genügt die abstrakte Definition; für [O-245c/2] wird eine direktere Beschreibung erforderlich sein.

---

### 1.2 \(D_N^{\mathrm{rel}}\) — Domäne und Selbstadjungiertheit

**Frage:** Ist \(D_N^{\mathrm{rel}}\) mit Domäne und Selbstadjungiertheit definiert?

**Quellenlage (NEU-221c, NEU-221d):**  
\(D_N^{\mathrm{rel}}\) wird als zyklischer Feshbach-Weyl-Kandidat auf dem Raum \(\mathcal{H}_N^{\mathrm{rel}}\) eingeführt. In NEU-221c §3 wird eine quadratische Resolventenstruktur angegeben; in NEU-221d §2 wird ein Nullmodusaudit durchgeführt.

Die Selbstadjungiertheit von \(D_N^{\mathrm{rel}}\) wird in NEU-221c als Postulat aus der zyklischen Feshbach-Weyl-Architektur übernommen, nicht aus einem konkreten Nelson-Kriterium oder Cayley-Argument für den Quotienten hergeleitet.

**Befund \(\checkmark[M]_{\mathrm{part}}\):**

- Formale Selbstadjungiertheit: **postuliert, nicht konstruktiv bewiesen** im Quotienten.
- Domäne: \(\mathcal{D}(D_N^{\mathrm{rel}})\subseteq\mathcal{H}_N^{\mathrm{rel}}\) nicht explizit charakterisiert.
- Spektralmassexistenz \(\mu_{\Psi_N}\): nur unter der Annahme zugänglich, dass \(\Psi_N\) zyklisch und \(D_N^{\mathrm{rel}}\) tatsächlich selbstadjungiert ist.

**Konsequenz für [O-245c/1]:** Die Auditpunkte 2–4 sind nur bedingt zugänglich. Sie setzen die postulierte Selbstadjungiertheit voraus. Das ist transparent zu vermerken.

---

### 1.3 \(\Psi_N \in \mathcal{H}_N^{\mathrm{rel}}\) — konkreter Vektor

**Frage:** Ist \(\Psi_N\) als konkreter Vektor konstruiert, nicht nur als formaler Lift?

**Quellenlage (NEU-221e, NEU-221d):**  
\(\Psi_N\) wird in NEU-221e als affiner Lift einer Basissektion \(\psi_p\) über die relative Hebungsfaser eingeführt. Der Lift ist **hebungsabhängig** (NEU-221e §6.1, Quellenkritik an NEU-41 §41.9).

Nach dem Rückrollpunkt in NEU-221e (Gegenlesungskorrekturen 2026-07-28):

> Der Test auf \(A_p^{\mathrm{adm}}\) ist äquivalent zum Test auf \(\Delta_p^{\mathrm{adm}}\) wegen Linearität von \(T_{\mathrm{raw}}\) und des Radikals \(\mathcal{N}_{W_{\mathrm{res}},\mathrm{rel}}\).

Das heißt: \(\Psi_N\) **als Klasse in \(\mathcal{H}_N^{\mathrm{rel}}\)** ist wohldefiniert, sobald \(\psi_p \in A_p^{\mathrm{adm}}\). Die Klassendarstellung ist hebungsunabhängig modulo \(\mathcal{N}\).

**Befund:** Als Element von \(\mathcal{H}_N^{\mathrm{rel}}\) ist \(\Psi_N\) durch die Quotientenstruktur wohldefiniert. Ein konkreter Repräsentant erfordert eine Wahl, aber die Klasse ist eindeutig. ✓ (unter den Voraussetzungen von NEU-221e)

---

## 2 — Kanonizität von \(\Psi_N\)

**Kernfrage:**

\[
\Psi_N \text{ unabhängig von der gewählten Hebung?}
\]

**Analyse:**

Verschiedene Hebungen \(\tilde\psi_p,\, \tilde\psi_p'\) mit \(\tilde\psi_p - \tilde\psi_p' \in \mathcal{N}_{W_{\mathrm{res}},\mathrm{rel}}\) liefern **dieselbe Klasse** \(\Psi_N \in \mathcal{H}_N^{\mathrm{rel}}\). Die Klasse ist daher hebungsunabhängig.

**Einschränkung:** Die **Norm** \(\|\Psi_N\|\) und damit das Spektralmaß \(\mu_{\Psi_N}\) hängen von der induzierten Wres-Paarung ab. Diese Paarung ist intrinsisch für den Quotienten, nicht von der Hebungswahl abhängig. ✓

**Kritischer Punkt — Wres-Normierung:**  
NEU-221e §6.1 hält fest, dass \(\Psi_N\) durch die Wres-Normierung der Eingangshebung **nicht automatisch** auf \(\|\Psi_N\|=1\) normiert ist. Die Normierung ist eine separate Wahl.

Das wird für Punkt 5 (Normierung) entscheidend.

---

## 3 — Nullmodusfreiheit

**Zu prüfende Bedingung:**

\[
\boxed{E_{D_N^{\mathrm{rel}}}(\{0\})\,\Psi_N = 0}
\]

**Präzisierung gegenüber NEU-221c:**  
Es ist **nicht** erforderlich, dass \(0 \in \rho(D_N^{\mathrm{rel}})\) global gilt. Ein globaler Kern \(\ker D_N^{\mathrm{rel}} \neq \{0\}\) wäre zulässig, sofern \(\Psi_N\) orthogonal dazu ist.

**Quellenlage:**  
NEU-221d §2 enthält ein Nullmodusaudit für den zyklischen Sektor aus NEU-46. Das Ergebnis ist:

> Die Direktextraktion aus NEU-46 ergibt \(E_{D_N}(\{0\})\Psi_N = 0\) für die dort konstruierte Familie.

**Befund \(\checkmark[M]_{\mathrm{part}}\):**

- Für den **zyklischen NEU-46-Sektor**: Nullmodusfreiheit bestätigt (NEU-221d).
- Für den **allgemeinen adelischen Quotienten**: Übertragung nicht explizit durchgeführt. Die Konstruktion in NEU-221e setzt voraus, dass \(\psi_p \in A_p^{\mathrm{adm}}\) zulässig ist; ob daraus \(E_{D_N}(\{0\})\Psi_N=0\) allgemein folgt, ist nicht bewiesen.

**Konsequenz:** Nullmodusfreiheit partiell gesichert (NEU-46-Sektor), allgemein offen.

---

## 4 — Existenz des Basismoments

**Zu zeigen:**

\[
\boxed{m_{0,N} = \left\langle \Psi_N,\, (D_N^{\mathrm{rel}})^{-2}\,\Psi_N \right\rangle = \int_{\mathbb{R}} |\lambda|^{-2}\,d\mu_{\Psi_N}(\lambda) < \infty}
\]

Äquivalent: \(\Psi_N \in \mathcal{D}(|D_N^{\mathrm{rel}}|^{-1})\).

Wenn diese Bedingung erfüllt ist:

\[
\Omega_{X,N} := (D_N^{\mathrm{rel}})^{-1}\,\Psi_N \quad \text{wohldefiniert}, \qquad m_{0,N} = \|\Omega_{X,N}\|^2.
\]

**Analyse:**

Notwendige Vorbedingung: Punkt 3 (Nullmodusfreiheit) muss gelten, damit der inverse Operator \((D_N^{\mathrm{rel}})^{-1}\) auf \(\Psi_N\) definierbar ist (ggf. als reduzierter Inverse auf dem Spektralsektor).

**Quellenlage:**  
Keine Quelle bis NEU-245c gibt eine explizite Abschätzung von \(\int|\lambda|^{-2}\,d\mu_{\Psi_N}(\lambda)\) an.

**Befund \(\checkmark[M]_{\mathrm{neg,Quelle}}\) für Punkt 4:**

- Die **Existenz** von \(m_{0,N}\) als reelle Zahl ist quellenseitig **nicht belegt**.
- Aus der zyklischen Feshbach-Weyl-Architektur folgt, dass \(\mu_{\Psi_N}\) ein Spektralmaß auf \(\mathbb{R}\setminus\{0\}\) ist (unter Annahme von Punkt 3). Ob \(|\lambda|^{-2}\) dazu integrierbar ist, hängt vom Verhalten von \(\mu_{\Psi_N}\) nahe \(0\) ab.
- Für den NEU-46-Sektor: Die quadratische Resolventenstruktur aus NEU-221c gibt \((D_N^{\mathrm{rel}})^2\)-Formeln, aber keine direkte \(L^2(\mu)\)-Abschätzung mit Gewicht \(|\lambda|^{-2}\).

**Was fehlt:** Eine explizite Wachstumsabschätzung für \(\mu_{\Psi_N}((-\epsilon,\epsilon)\setminus\{0\})\) für kleines \(\epsilon>0\), die zeigt, dass diese Masse schnell genug gegen 0 geht, um \(\int|\lambda|^{-2}\,d\mu<\infty\) zu sichern.

---

## 5 — Normierung

**Regel:** Die Normierung von \(\Psi_N\) darf **nicht nachträglich** so gewählt werden, dass \(m_{0,N}=\mu_0\). Das wäre tautologisch.

**Audit:**

Die Konstruktion in NEU-221e lässt die Skalierung von \(\Psi_N\) durch die Wres-Paarung bestimmen, nicht durch eine \(m_{0,N}\)-Forderung. Insofern ist der Tautologieschutz **strukturell vorhanden**.

**Unterscheidung (für das Protokoll):**

| Begriff | Status |
|---|---|
| Existenz von \(m_{0,N}\) | offen — Punkt 4 nicht belegt |
| Arithmetisch kanonischer Wert von \(m_{0,N}\) | offen — setzt Existenz + adelische Quellennormierung voraus |
| Tautologieschutz | ✓ — Normierung kommt aus Wres-Struktur |

---

## 6 — M1-Kompatibilität: Typ von \(D_N^{\mathrm{rel}}\)

**Typfrage:**

\[
D_N^{\mathrm{rel}} \neq \bigoplus_{p \le N} D_{p,N}^{\mathrm{rel}} \quad\text{quellenseitig belegt?}
\]

**Analyse:**

In NEU-221c wird \(D_N^{\mathrm{rel}}\) als **zyklischer** Feshbach-Weyl-Kandidat eingeführt — explizit mit Mischblock-Struktur. NEU-221d §2 verweist auf den zyklischen Sektor aus NEU-46, der eine nicht-diagonale Kopplungsstruktur erzwingt.

In NEU-245b wurde M1 als Mindestarchitektur (globale Archimedes-Prim-Kopplung, kein direktes Summen-Zerfallen) positiv bewertet.

**Befund \(\checkmark[M]\) für M1-Typfrage:**  
Die Quellen NEU-221c + NEU-221d + NEU-245b belegen gemeinsam, dass \(D_N^{\mathrm{rel}}\) im zyklischen Sektor einen echten globalen Feshbach-Anteil besitzt. Die direkte Summe lokaler Blöcke wäre unverträglich mit der zyklischen Konstruktion.

Quantitative Positivitätswirkung (M1-Stärke) wird hier nicht bewertet — das ist Teil von [O-245c/2].

---

## 7 — Gesamtbilanz [O-245c/1]

| Prüfpunkt | Befund |
|---|---|
| \(\mathcal{H}_N^{\mathrm{rel}}\) definiert | ✓ (Quotient, abstrakt) |
| \(D_N^{\mathrm{rel}}\) mit Domäne + Selbstadjungiertheit | \(\checkmark[M]_{\mathrm{part}}\) (postuliert, nicht konstruktiv) |
| \(\Psi_N \in \mathcal{H}_N^{\mathrm{rel}}\) als Klasse | ✓ (hebungsunabhängig mod \(\mathcal{N}\)) |
| Kanonizität \(\Psi_N\) | ✓ (Klassendarstellung eindeutig) |
| Nullmodusfreiheit \(E_{D_N}(\{0\})\Psi_N=0\) | \(\checkmark[M]_{\mathrm{part}}\) (NEU-46-Sektor ✓; allgemein offen) |
| Existenz \(m_{0,N} < \infty\) | \(\checkmark[M]_{\mathrm{neg,Quelle}}\) (keine Abschätzung vorhanden) |
| Tautologieschutz Normierung | ✓ |
| M1-Typfrage | ✓ |

**Gesamtstatus:** \(\checkmark[M]_{\mathrm{part}}\)

---

## 8 — Offene Fragen und Folgeknoten

### Für [O-245c/1]-Vervollständigung nötig

1. **Selbstadjungiertheit konstruktiv:** Nelson-Kriterium oder Cayley-Argument für \(D_N^{\mathrm{rel}}\) im Quotienten. Oder expliziter Verweis auf eine Quelle, die das leistet.

2. **Nullmodusfreiheit allgemein:** Abstieg der NEU-221d-Aussage vom NEU-46-Sektor auf den allgemeinen adelischen Quotienten. Kandidatenquelle: NEU-221e §2.2 (Linearitätsargument) — ausreichen könnte, dass \(\psi_p \in A_p^{\mathrm{adm}}\) bereits die Nullmodusfreiheit erzwingt.

3. **Existenz \(m_{0,N}\):** Explizite Abschätzung
   \[
   \mu_{\Psi_N}((-\epsilon,\epsilon)\setminus\{0\}) = O(\epsilon^\alpha), \quad \alpha > 1
   \]
   aus der zyklischen Feshbach-Weyl-Resolventenstruktur (NEU-221c §3). Das ist der eigentliche mathematische Kern von [O-245c/1].

### Freigeschaltet nach positivem Abschluss

\[
[O\text{-}245c/2]: \quad M_{X,N}(w) \longrightarrow M_\Xi(w)
\]

Identitätsaudit der Momentfolge. Erst nach Punkt 3 oben.

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

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung des RH-Forschungsjournals*
