# NEU-246 — Typ-, Grad- und Kerninvarianzaudit des Koszul-Kandidaten

**Katalog-ID:** NEU-246  
**Knoten:** `[O-229-3B.1f-c.2b-valuation-derivation-koszul-viability]`  
**Stand:** 28. Juli 2026  
**Vorgänger:** NEU-245  
**Leseauftrag-Quellen:** NEU-229 (01-primkanten-werkzeuge), NEU-221e (07-weil-explizitformel), NEU-195  

---

## 0. Auditurteil (vorläufig)

$$
\boxed{\ [O\text{-}229\text{-}3B.1f\text{-}c.2b\text{-valuation-derivation-koszul-viability}]
\quad ?[O]\ }
$$

**Vorlaufsperre:** Primärer Auditausgang noch nicht feststellbar. Die Typbarriere (Abschnitt 2) ist
der entscheidende Vorgänger aller weiteren Prüfpunkte. Kein Homogenitäts- oder Kerninvarianzbefund
ist vor ihrer Auflösung zulässig.

---

## 1. Zweck und Firewall

NEU-245 hat gezeigt:

$$
d_{\mathrm{lift}} = \delta_q
$$

ist kein Differential, da im Allgemeinen $\delta_q^2 \neq 0$.

Offen blieb der **Koszul-Kandidat**

$$
M_p \otimes \Lambda^n(\mathbb{C}^S), \qquad
d_{\mathrm{K}} = \sum_{q \in S} \Delta_q(m) \otimes e_q \wedge \omega,
$$

wobei die Operatoren $\Delta_q$ auf einem gemeinsamen liftseitigen Modul $M_p$ wirken und paarweise
kommutieren sollen.

**Feuerwand:** Es darf nicht vorausgesetzt werden, dass die algebraischen Bewertungsderivationen

$$
\delta_q : A_{\mathrm{alg}} \to A_{\mathrm{alg}}
$$

bereits auf $K_p^{\mathrm{alg}} \subseteq B_3$ oder $\mathcal{D}(a_p) \subseteq K_p^{\mathrm{alg}}$ wirken.
Die erste Auditfrage ist eine **Typfrage**, keine Homogenitätsfrage.

---

## 2. Quellenveranlagter Typbefund

### 2.1 Typen aus NEU-229, §§ 2.1–2.2

NEU-229 definiert (§ 2.1) den algebraischen Liftbereich:

$$
\mathcal{D}_p^{\mathrm{lift}} \subseteq \operatorname{Dom}\pi_{\mathrm{prim},p} \cap \operatorname{Dom}T_p^{\mathrm{raw}},
\qquad e_p \in \mathcal{D}_p^{\mathrm{lift}},
$$

und den minimalen algebraischen Kern:

$$
K_p^{\mathrm{alg}} := \ker\!\left(\pi_{\mathrm{prim},p}\big|_{\mathcal{D}_p^{\mathrm{lift}}}\right),
\qquad \mathcal{V}_p^{\mathrm{alg}} := \mathbb{C}e_p \oplus K_p^{\mathrm{alg}}.
$$

Die Kernform ist (§ 2.2):

$$
a_p : \mathcal{D}(a_p) \times \mathcal{D}(a_p) \to \mathbb{C}, \qquad \mathcal{D}(a_p) \subseteq K_p^{\mathrm{alg}}.
$$

### 2.2 Typ von $\delta_q$ aus dem Quellenbestand

Im auditierten Quellenbestand (insbesondere NEU-195, NEU-043, NEU-229 §§ 3–4) besitzt
$\delta_q$ ausschließlich den Typ:

$$
\delta_q : A_{\mathrm{alg}} \longrightarrow A_{\mathrm{alg}}.
$$

Eine **explizite Erweiterung** auf $B_3$, auf $\mathcal{D}_p^{\mathrm{lift}}$, auf $K_p^{\mathrm{alg}}$
oder auf $\mathcal{D}(a_p)$ ist im gegenwärtigen Quellenbestand **nicht definiert**.

### 2.3 Inklusion und Typ des ambienten Raums

Die vorhandene Inklusionskette lautet:

$$
K_p^{\mathrm{alg}} \subseteq \mathcal{D}_p^{\mathrm{lift}} \subseteq B_3.
$$

Ob $K_p^{\mathrm{alg}} \subseteq A_{\mathrm{alg}}$ gilt — was eine natürliche Wirkung von $\delta_q$
auf $K_p^{\mathrm{alg}}$ ergäbe —, ist im Quellenbestand **nicht etabliert**. $B_3$ ist als
Hochschild-Kettenraum (Tensorraum $A^{\otimes 4}$) typisiert; $A_{\mathrm{alg}}$ ist der
algebraische Basisfaktor. Diese beiden Räume sind nicht identisch.

### 2.4 Primärbefund (Typisierung)

$$
\boxed{
[O\text{-}229\text{-}3B.1f\text{-}c.2b.1\text{-typed-lift-action}]
\quad \checkmark[M]_{\mathrm{neg,Quelle}}
}
$$

**Umfang:** Im auditierten Quellenbestand (NEU-229, NEU-195, NEU-043) ist **keine** Wirkung
von $\delta_q$ auf dem Liftbereich $\mathcal{D}_p^{\mathrm{lift}}$ oder dem Primkern $K_p^{\mathrm{alg}}$
typisiert. Eine zukünftige tensorweise oder Lie-derivierte Erweiterung wird nicht ausgeschlossen.

---

## 3. Kandidat für eine induzierte Wirkung: $L_{\delta_q}^{(3)}$

Falls $B_3 = A^{\otimes 4}$ (Hochschild-Kettenraum über $A$), wäre ein natürlicher Kandidat die
**tensorweise Lie-Ableitung**:

$$
L_{\delta_q}^{(3)}(a_0 \otimes a_1 \otimes a_2 \otimes a_3)
= \sum_{j=0}^{3} a_0 \otimes \cdots \otimes \delta_q(a_j) \otimes \cdots \otimes a_3.
$$

Dieser Operator ist **nicht identisch** mit $\delta_q$. Zu prüfen wäre:

| Prüffrage | Status |
|---|---|
| $L_{\delta_q}^{(3)} : B_3 \to B_3$? | Formal ja, falls $\delta_q : A \to A$ und $B_3 = A^{\otimes 4}$. Primärdefinition fehlt aber. |
| $L_{\delta_q}^{(3)}(\mathcal{D}_p^{\mathrm{lift}}) \subseteq \mathcal{D}_p^{\mathrm{lift}}$? | **Kein Quellenbeleg** — neues Konstruktionsdesiderat. |
| $L_{\delta_q}^{(3)}(K_p^{\mathrm{alg}}) \subseteq K_p^{\mathrm{alg}}$? | **Kein Quellenbeleg** — abhängig von Intertwining (§ 4). |

**Kennzeichnung:** Keine der tensorweisen Erweiterungen liegt als Primärdefinition vor.
Sie sind als **neues Konstruktionsdesiderat** zu führen, nicht als Quellenbefund.

---

## 4. Projektions- und Kernverträglichkeit

Sei $\Delta_q$ irgendeine Erweiterung von $\delta_q$ auf $B_3$. Dann gilt:

$$
K_p^{\mathrm{alg}} = \ker\!\left(\pi_{\mathrm{prim},p}\big|_{\mathcal{D}_p^{\mathrm{lift}}}\right).
$$

Die Homogenität des ambienten Raums allein reicht für

$$
\Delta_q(K_p^{\mathrm{alg}}) \subseteq K_p^{\mathrm{alg}}
$$

nicht aus. Hinreichend wäre eine **Intertwining-Relation**:

$$
\pi_{\mathrm{prim},p} \circ \Delta_q = \delta_{q,\mathrm{prim}} \circ \pi_{\mathrm{prim},p}
$$

mit einem geeigneten Operator $\delta_{q,\mathrm{prim}}$ auf dem primitiven Zielraum.
Für $k \in K_p^{\mathrm{alg}}$ folgte dann:

$$
\pi_{\mathrm{prim},p}(\Delta_q k) = \delta_{q,\mathrm{prim}}(\pi_{\mathrm{prim},p}(k)) = \delta_{q,\mathrm{prim}}(0) = 0,
$$

also $\Delta_q k \in K_p^{\mathrm{alg}}$. Eine solche Relation ist im Quellenbestand **nicht nachgewiesen**.

---

## 5. Homogenitätsaudit (bedingt)

**Voraussetzung:** Dieser Abschnitt ist nur relevant nach positiver Typisierung von $\Delta_q$
(Ausgang B oder besser). Bei aktuellem Ausgang A (§ 2.4) sind die folgenden Fragen **gesperrt**.

Erst nach Auflösung der Typbarriere wäre zu prüfen:

1. Besitzt $B_3$ eine quellengegebene $\mathbb{Q}_+^\times$-Graduierung?
2. Ist $\mathcal{D}_p^{\mathrm{lift}} = \bigoplus_g \mathcal{D}_{p,g}^{\mathrm{lift}}$ graduiert?
3. Ist $K_p^{\mathrm{alg}} = \bigoplus_g (K_p^{\mathrm{alg}} \cap \mathcal{D}_{p,g}^{\mathrm{lift}})$?
4. Ist $\pi_{\mathrm{prim},p}$ gradverträglich?
5. Wirkt $\Delta_q$ graderhaltend: $\Delta_q(\mathcal{D}_{p,g}^{\mathrm{lift}}) \subseteq \mathcal{D}_{p,g}^{\mathrm{lift}}$?

Nur wenn alle fünf Punkte erfüllt sind, kann Gradstabilität zur Kerninvarianz beitragen.

---

## 6. Formbereichsinvarianz (bedingt)

Selbst aus $\Delta_q(K_p^{\mathrm{alg}}) \subseteq K_p^{\mathrm{alg}}$ (falls bewiesen) folgt **nicht**:

$$
\Delta_q(\mathcal{D}(a_p)) \subseteq \mathcal{D}(a_p).
$$

Da $\mathcal{D}(a_p) \subsetneq K_p^{\mathrm{alg}}$ durch zusätzliche Form-Zulässigkeits- und
Regularitätsbedingungen definiert ist (NEU-229, § 2.2), muss **jede dieser Bedingungen** einzeln
unter $\Delta_q$ erhalten bleiben. Ein algebraischer Erhaltungssatz für $K_p^{\mathrm{alg}}$
allein genügt nicht.

---

## 7. Kommutatorprüfung auf dem tatsächlichen Modul

NEU-245 hat die Kommutation auf algebraischen Erzeugern festgestellt:

$$
[\delta_q, \delta_\ell] = 0 \quad \text{auf } A_{\mathrm{alg}}.
$$

Für den Koszul-Komplex wird benötigt:

$$
[\Delta_q, \Delta_\ell] = 0 \quad \text{auf } M_p.
$$

Falls $\Delta_q = L_{\delta_q}^{(3)}$ tensorweise definiert ist, folgt diese Kommutation formal
aus $[\delta_q, \delta_\ell] = 0$, **sofern** alle Summanden auf einem gemeinsamen invarianten
Definitionsbereich definiert sind — was nach § 3 noch nicht etabliert ist.
Erst dann gilt $d_{\mathrm{K}}^2 = 0$.

---

## 8. Radikal- und Quotientenabstieg (bedingt)

Für einen Komplex auf dem Formquotienten $H_{a,p} = \overline{\mathcal{D}(a_p)/N_{a_p}}^{a_p}$
(NEU-229, § 2.2) ist zusätzlich erforderlich:

$$
\Delta_q(N_{a_p}) \subseteq N_{a_p}.
$$

Aus der Rohkopplungsstruktur (NEU-229, § 6.3) kann dies durch eine Intertwining-Relation

$$
\Delta_q \circ T_p^{\mathrm{raw}} = \Gamma_q \circ T_p^{\mathrm{raw}}
$$

gesichert werden. Ohne eine solche Relation oder einen direkten Beweis ist der Abstieg auf
$H_{a,p}$ nicht gesichert.

---

## 9. Abschlussmatrix

| Prüfpunkt | Erforderlicher Befund | Aktueller Status |
|---|---|---|
| **Typisierung** | $\Delta_q$ wirkt auf liftseitigem Vektorraum | `✓[M]_neg,Quelle` |
| Liftbereich | $\Delta_q(\mathcal{D}_p^{\mathrm{lift}}) \subseteq \mathcal{D}_p^{\mathrm{lift}}$ | **gesperrt** |
| Primkern | $\Delta_q(K_p^{\mathrm{alg}}) \subseteq K_p^{\mathrm{alg}}$ | **gesperrt** |
| Formbereich | $\Delta_q(\mathcal{D}(a_p)) \subseteq \mathcal{D}(a_p)$ | **gesperrt** |
| Kommutation | $[\Delta_q, \Delta_\ell] = 0$ auf gemeinsamem Bereich | **gesperrt** |
| Radikal | $\Delta_q(N_{a_p}) \subseteq N_{a_p}$ | **gesperrt** |
| Quotient | induzierte Operatoren auf $H_{a,p}$ | **gesperrt** |
| Koszul | $d_{\mathrm{K}}^2 = 0$ auf tatsächlichem Modul | **gesperrt** |
| Nichttrivialität | relevante Kohomologie nicht tautologisch | **gesperrt** |

---

## 10. Mögliche Statusausgänge

### Ausgang A — Keine liftseitige Wirkung definiert (aktueller Stand)

Der Quellenbestand liefert ausschließlich $\delta_q : A_{\mathrm{alg}} \to A_{\mathrm{alg}}$
und keine Erweiterung auf $B_3$. Daher gilt:

$$
\boxed{
[O\text{-}229\text{-}3B.1f\text{-}c.2b.1\text{-typed-lift-action}]
\quad \checkmark[M]_{\mathrm{neg,Quelle}}
}
$$

Der Koszul-Kandidat ist **konstruktiv offen, quellenmäßig blockiert**.

### Ausgang B — Wirkung vorhanden, Kerninvarianz fehlt

Dann gilt $[c.2b.1]\ \checkmark[K/M]$, aber $[c.2b.2\text{-primitive-kernel-invariance}]\ ?[O]$.

### Ausgang C — Wirkung und Kerninvarianz vorhanden, Formbereich offen

Dann gilt $[c.2b.2]\ \checkmark[M]$ und $[c.2b.3\text{-form-domain-invariance}]\ ?[O]$.

### Ausgang D — Alle Invarianzen und Kommutation bewiesen

Erst dann darf der Koszul-Komplex

$$
M_p \otimes \Lambda^n(\mathbb{C}^S), \qquad
d_{\mathrm{K}} = \sum_{q \in S} \Delta_q \otimes (e_q \wedge \cdot)
$$

mit $d_{\mathrm{K}}^2 = 0$ gesetzt werden, und der Knoten

$$
[O\text{-}229\text{-}3B.1f\text{-}c.2b] \quad \checkmark[K/M]
$$

wäre geschlossen.

---

## 11. Unmittelbarer Leseauftrag (nächste Schritte)

In dieser Reihenfolge zu lesen:

1. **NEU-221e** — genauer Typ von $B_3$, Liftbereich, Primprojektion und Kern;
2. **NEU-229** ✓ (gelesen) — Typen von $\mathcal{D}_p^{\mathrm{lift}}$, $K_p^{\mathrm{alg}}$,
   $\mathcal{D}(a_p)$, $N_{a_p}$ etabliert (§§ 2.1–2.2, 3.3, 6.3);
3. **NEU-195** — genauer Definitionsbereich und Graduierungswirkung von $\delta_q$;
4. **Primärdatei für $B_3$ als Hochschild- oder Tensorraum** — Kandidaten: NEU-014 (KMS-Zustand),
   NEU-042 (Fourier-Laplace-Hebung), laut Abhängigkeitstabelle NEU-229 § 10.

**Sperrvermerk:** Keine tensorweise Erweiterung von $\delta_q$ darf ohne explizite Definition oder
vollständige neue Konstruktion verwendet werden.

---

## 12. Strategische Schlussaussage

$$
\boxed{
\delta_q : A_{\mathrm{alg}} \to A_{\mathrm{alg}} \text{ besitzt bislang möglicherweise gar keinen Typ auf }
K_p^{\mathrm{alg}} \subseteq B_3.
}
$$

Erst wenn diese **Typbarriere** überwunden ist, werden Homogenität und Kerninvarianz entscheidend.

---

## Abhängigkeiten

| Referenz | Verwendet für |
|---|---|
| **NEU-229** (§§ 2.1–2.2, 3, 6) | Primärtypen $\mathcal{D}_p^{\mathrm{lift}}$, $K_p^{\mathrm{alg}}$, $\mathcal{D}(a_p)$, $N_{a_p}$, Radikal $\ker T_p^{\mathrm{raw}}$ |
| NEU-245 | $d_{\mathrm{lift}} = \delta_q$ kein Differential; $[\delta_q, \delta_\ell] = 0$ auf algebraischen Erzeugern |
| NEU-043 | Fourierregel $\widetilde{\omega}_2(e_u V_p, e_s V_m) = -us\log(p)\,e_{u+ps}V_{pm}$ |
| NEU-195 | Definitionsbereich und Graduierungswirkung von $\delta_q$ — noch zu lesen |
| NEU-221e | Genauer Typ von $B_3$, Liftbereich — noch zu lesen |
| NEU-014 | KMS-Zustand auf $B_3$ — Kandidat für Tensorerweiterung |
| NEU-042 | Fourier-Laplace-Hebung — Kandidat für Tensorerweiterung |
