# NEU-247 — Tensor-Lift von Bewertungsableitungen: Typbrücke

**Knoten:** `[O-229-3B.1f-c.2b.2-tensor-lift-of-valuation-derivations]` | Status: `?[O]` (Vorlaufsperre)  
**Vorgänger:** NEU-246 (Typ-Grad-Kerninvarianzaudit, Koszul-Kandidat)  
**Leseauftrag:** NEU-195 → Primärdefinition von $B_3$ → NEU-014 / NEU-042 → NEU-221e / NEU-229 als Verträglichkeitstest  
**Re-Audit-Präzisierung:** NEU-221e wurde im Rahmen von NEU-242 vollständig gelesen; für diesen Knoten ist kein Erstaudit mehr nötig, sondern ein gezielter Re-Audit auf Graduierung, Tensorstruktur und bereits definierte induzierte Wirkungen.

---

## 1  Problemstellung

NEU-246 hat den Typbefund abgeschlossen:

$$
\delta_q : A_{\mathrm{alg}} \to A_{\mathrm{alg}}
$$

wirkt quellengegeben **nicht** auf $B_3 = A^{\otimes 4}$, $K_p^{\mathrm{alg}}$ oder $\mathcal{D}(a_p)$.  
Solange diese Typbrücke fehlt, sind alle acht nachgelagerten Prüfpunkte (Nilpotenz, Homogenität, Radikalinvarianz, Koszul-Kandidat) gesperrt.

Der vorliegende Knoten isoliert die Typbrücke selbst.

---

## 2  Drei strikt getrennte Fragen

### 2.1  Quellenbestand

**Frage:** Definiert NEU-014, NEU-042 oder eine andere Primärdatei bereits eine Wirkung

$$
\Delta_q : B_3 \to B_3
$$

aus $\delta_q$?

- **Prüfpfad:** NEU-195 (Primärdefinition von $\delta_q$ und ihres Definitionsbereichs) → NEU-014 (KMS-Zustand, ggf. tensorweise Wirkungen) → NEU-042 (Fourierhebung, Laplace-$(p{-}s)$-Struktur).
- **Erwartetes Ergebnis:** $\checkmark[M]_{\mathrm{neg,Quelle}}$ (keine solche Wirkung quellengegeben) oder $\checkmark[M]_{\mathrm{pos,Quelle}}$ (Wirkung bereits definiert).
- **Status:** **offen** — Quellenlektüre ausstehend.

### 2.2  Kanonische Neukonstruktion

**Frage:** Falls keine Quelle eine tensorweise Wirkung liefert — ist die Lie-Ableitung

$$
L_{\delta_q}^{(3)} = \sum_{j=0}^{3} \mathbf{1}^{\otimes j} \otimes \delta_q \otimes \mathbf{1}^{\otimes(3-j)}
$$

auf dem **tatsächlich verwendeten algebraischen Tensorprodukt** $B_3 = A_{\mathrm{alg}}^{\otimes 4}$ wohldefiniert?

Voraussetzungen, die zu prüfen sind:
1. $A_{\mathrm{alg}}$ ist als $\mathbb{C}$-Algebra im Quellenbestand explizit typisiert (NEU-195 / NEU-229).
2. Das algebraische Tensorprodukt $A_{\mathrm{alg}}^{\otimes 4}$ ist als solches für $B_3$ verwendet — nicht etwa ein vervollständigtes oder projektives Tensorprodukt (Verträglichkeitstest NEU-221e / NEU-229).
3. $\delta_q$ ist eine $\mathbb{C}$-lineare Derivation auf $A_{\mathrm{alg}}$ (Leibniz-Regel); erst dann ist die Summenformel eine Derivation auf $B_3$.

- **Status:** **offen** — abhängig von 2.1 und der Tensorprodukttypverifizierung.

### 2.3  Brückenverträglichkeit

**Frage:** Falls $L_{\delta_q}^{(3)}$ wohldefiniert ist — erfüllt sie

$$
L_{\delta_q}^{(3)}\!\left(\mathcal{D}_p^{\mathrm{lift}}\right) \subseteq \mathcal{D}_p^{\mathrm{lift}}
$$

und

$$
\pi_{\mathrm{prim},p} \circ L_{\delta_q}^{(3)} = \delta_{q,\mathrm{prim}} \circ \pi_{\mathrm{prim},p}
$$

für einen typisierten Zieloperator $\delta_{q,\mathrm{prim}}$?

- **Verträglichkeitsquellen:** NEU-221e (Graduierung, Tensorstruktur, induzierte Wirkungen), NEU-229 (Primseiten-Identifikation, Liftbereich).
- **Status:** **offen** — erst nach positivem Abschluss von 2.1 und 2.2 prüfbar.

---

## 3  Nachgeordnete Prüfkette (gesperrt bis 2.3 positiv)

Erst nach vollständig positiver Antwort auf alle drei Fragen darf geprüft werden:

$$
L_{\delta_q}^{(3)}\!\left(K_p^{\mathrm{alg}}\right) \subseteq K_p^{\mathrm{alg}},
$$

danach

$$
L_{\delta_q}^{(3)}\!\left(\mathcal{D}(a_p)\right) \subseteq \mathcal{D}(a_p),
$$

und zuletzt

$$
L_{\delta_q}^{(3)}\!\left(N_{a_p}\right) \subseteq N_{a_p}.
$$

Homogenität bleibt bis dahin nachgeordnet.

---

## 4  Lesereihenfolge und erwartete Ausgänge

$$
\boxed{
\text{NEU-195}
\;\longrightarrow\;
\text{Primärdefinition von } B_3
\;\longrightarrow\;
\text{NEU-014 / NEU-042}
\;\longrightarrow\;
\text{NEU-221e / NEU-229 als Verträglichkeitstest}
}
$$

| Ausgang | Bedeutung |
|---|---|
| $\checkmark[M]_{\mathrm{neg,Quelle}}$ + Desiderat | Keine tensorweise Wirkung quellengegeben; $L_{\delta_q}^{(3)}$ als neue Konstruktion einzuführen |
| $\checkmark[K/M]$ | Vollständig definierte tensorweise Lie-Ableitung, Brückenverträglichkeit nachgewiesen |

---

## 5  Offene Konstruktionsdesiderate (noch nicht Quellenbefund)

- $L_{\delta_q}^{(3)}$ als tensorweise Lie-Ableitung ist **noch kein Quellenbefund**; er darf erst nach expliziter Definition in einer nachfolgenden NEU-Einheit verwendet werden.
- Ein typisierter Zieloperator $\delta_{q,\mathrm{prim}}$ auf $A_{\mathrm{alg}} / K_p^{\mathrm{alg}}$ (o.ä.) ist noch nicht konstruiert.

---

**Nächster Knoten nach positivem Abschluss:** `[O-229-3B.1f-c.2b.3-kernel-invariance-under-tensor-lift]`  
**Nächster Knoten bei negativem Quellenbestand (2.1):** Konstruktionsdesiderat $L_{\delta_q}^{(3)}$ als eigene NEU-Einheit formalisieren.
