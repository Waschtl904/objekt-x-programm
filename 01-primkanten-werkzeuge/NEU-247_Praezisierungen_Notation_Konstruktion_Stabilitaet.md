# NEU-247 — Drei Präzisierungen vor dem nächsten Leseaudit

**Knoten:** `[O-229-3B.1f-c.2b-praezisierungen]`  
**Status:** ✓[M] — festgeschriebene Konventionen, keine offenen Behauptungen  
**Vorgänger:** NEU-246 (`[O-229-3B.1f-c.2b-valuation-derivation-koszul-viability]`)

---

## 1. Kollisionsfreie Notation (ab sofort verbindlich)

Die Bezeichnung $B_3$ ist ab diesem Knoten **aufgelöst**. Ab sofort gilt:

| Symbol | Definition | Status |
|---|---|---|
| $\mathfrak{B} := A_{\mathbb{Q}}$ | die Algebra | Quellenbefund (NEU-174) |
| $C_3^{\mathrm{HH}}(\mathfrak{B}) := \mathfrak{B}^{\otimes 4}$ | Hochschild-3-Kettenraum | Standardkonstruktion |
| $\operatorname{Bd}_3^{\mathrm{HH}}(\mathfrak{B}) := \operatorname{im}(b_4 : C_4^{\mathrm{HH}}(\mathfrak{B}) \to C_3^{\mathrm{HH}}(\mathfrak{B}))$ | Hochschild-3-Randraum | Standardkonstruktion |
| $B_3^{\mathrm{adm}}$ | **ungeklärtes Symbol** — Originalnotation der Quellen | ⚠ gesperrt bis Definition gefunden |

**Sperrklausel:** $B_3^{\mathrm{adm}}$ darf **nicht** vorzeitig mit $C_3^{\mathrm{HH}}(\mathfrak{B})$ oder $\operatorname{Bd}_3^{\mathrm{HH}}(\mathfrak{B})$ identifiziert werden. Es bleibt als Originalnotation der Quellen behandelt, bis seine Definition in NEU-155 oder einem Rückverweisdokument explizit gefunden wurde.

---

## 2. Quellenbefund vs. Neukonstruktion (Schichttrennung)

### Quellengegeben (nicht konstruiert)

$$
\mathfrak{B} = A_{\mathbb{Q}} \qquad \text{(NEU-174)}
$$

$$
\delta_p : A_{\mathrm{alg}} \to A_{\mathrm{alg}} \qquad \text{(NEU-195)}
$$

### Standardmäßige Konstruktionen (nicht aus Quellen übernommen)

$$
C_3^{\mathrm{HH}}(\mathfrak{B}) = \mathfrak{B}^{\otimes 4}
$$

sofern NEU-174 diesen Kettenraum nicht selbst als solchen einführt. Dies ist vor dem Lesen von NEU-174 §§ 3–4 nicht als Primärbefund buchbar.

### Neue Konstruktion (Desiderat, noch kein Befund)

$$
L_{\delta_p}^{[3]}(a_0 \otimes \cdots \otimes a_3)
:= \sum_{j=0}^{3} a_0 \otimes \cdots \otimes \delta_p(a_j) \otimes \cdots \otimes a_3
$$

Dies ist ein **Konstruktionsdesiderat**, kein Quellenbefund. Es darf erst nach
(a) Nachweis der Stabilität $\delta_p(\mathfrak{B}) \subseteq \mathfrak{B}$ und
(b) Identifikation des Liftbereichs als Teilraum von $C_3^{\mathrm{HH}}(\mathfrak{B})$
als typkorrekte Abbildung verwendet werden.

### Noch zu beweisendes Lemma (konstruktive Schicht)

$$
b \circ L_{\delta_p}^{[n]} = L_{\delta_p}^{[n-1]} \circ b
$$

Dies folgt algebraisch aus der Leibnizregel für $\delta_p$, ist aber ein **eigenes Lemma** der konstruktiven Schicht. Es darf nicht als Primärbefund gebucht werden, bevor ein Beweistext vorliegt.

---

## 3. Stabilitätsfrage (eindeutig, noch quellenseitig offen)

Vor jeder Tensorfortsetzung muss nachgewiesen werden:

$$
\boxed{\delta_p(\mathfrak{B}) \subseteq \mathfrak{B}}
$$

**Indizpfad (noch nicht quellenfest):**

Die Formel $\delta_p(a_q) = v_p(q)\, a_q$ legt Stabilität nahe, falls $A_{\mathbb{Q}}$ als rationaler direkter Summenkern derselben homogenen Komponenten definiert ist wie $A_{\mathrm{alg}}$. Das Verhältnis $A_{\mathbb{Q}}$ zu $A_{\mathrm{alg}}$ ist erst nach Abgleich der exakten Definitionen in den Quellen zu klären.

**Sperrkonsequenz:** Erst nach Beweis der Stabilität ist

$$
L_{\delta_p}^{[3]} : C_3^{\mathrm{HH}}(\mathfrak{B}) \to C_3^{\mathrm{HH}}(\mathfrak{B})
$$

typkorrekt konstruierbar.

---

## Nächste Lesereihenfolge (engst möglich)

| Schritt | Dokument | Ziel |
|---|---|---|
| 1 | **NEU-155** | Unmittelbarer Definitionskontext von $B_3^{\mathrm{adm}}$; Rückverweise und importierte Notation; früheste bestätigte Verwendung $T_p : B_3^{\mathrm{adm}} \longrightarrow H_{J,N}$ |
| 2 | **NEU-157** | Verhältnis $B_3^{\mathrm{adm}}$ — Normierungsquadrik — Zulässigkeitsraum |
| 3 | Rückverweisdokumente aus NEU-155 | Definition von $B_3^{\mathrm{adm}}$ rückwärts verfolgen |
| 4 | **NEU-221e** | Provenienz von $B_{3,p}^{\mathrm{lift}}$; Verhältnis zu $B_3^{\mathrm{adm}}$ |
| 5 | **NEU-229** | Erstauftreten / Import von $\mathcal{D}_p^{\mathrm{lift}}$ |

**Suchbegriffe (exakt):**
$$
B_3^{\mathrm{adm}},\quad B_{3,p}^{\mathrm{lift}},\quad \mathcal{D}_p^{\mathrm{lift}},\quad \pi_{\mathrm{prim},p},\quad K_p^{\mathrm{alg}}
$$

---

## Provenienzmatrix

| Objekt | Zu entscheidende Frage |
|---|---|
| $B_3^{\mathrm{adm}}$ | Teilraum welcher Algebra, Kette oder Kokette? |
| $B_{3,p}^{\mathrm{lift}}$ | Affine Faser innerhalb welches ambienten Raumes? |
| $\mathcal{D}_p^{\mathrm{lift}}$ | Linearer Teilraum von $B_3^{\mathrm{adm}}$, $B_{3,p}^{\mathrm{lift}}$ oder einem neuen Raum? |
| $K_p^{\mathrm{alg}}$ | Kern innerhalb welches exakt typisierten Definitionsbereichs? |
| $T_p^{\mathrm{raw}}$ | Auf Algebraelementen, Ketten oder Koketten ausgewertet? |

---

## Mögliche Abschlussfälle

### Kettenfall
Falls $\mathcal{D}_p^{\mathrm{lift}} \subseteq C_3^{\mathrm{HH}}(\mathfrak{B})$: Vier-Slot-Lie-Ableitung ist der richtige Kandidat.

### Ränderfall
Falls $\mathcal{D}_p^{\mathrm{lift}} \subseteq \operatorname{Bd}_3^{\mathrm{HH}}(\mathfrak{B})$: Nach Beweis von $b \circ L_{\delta_p} = L_{\delta_p} \circ b$ kann Invarianz des ambienten Randraums geschlossen werden. Zulässigkeitsbedingungen bleiben separat offen.

### Kokettenfall
Falls der Liftbereich in einem Raum $C^n(\mathfrak{B}, M)$ liegt: Vier-Slot-Tensorformel ist falsch typisiert. Eine kontravariante Lie-Ableitung auf Koketten — einschließlich Wirkung auf $M$ — wäre zu konstruieren.

### Separater Liftmodul
Falls $B_3^{\mathrm{adm}}$ ein eigenständiger Modul ohne identifizierte Ketten- oder Koketteneinbettung ist: Koszul-Zweig bleibt an einer neuen Brückenabbildung blockiert.

---

## Gesperrte Folgeknoten

Alle acht Prüfpunkte des Koszul-Kandidaten $M_p \otimes \Lambda^n(\mathbb{C}^S)$ bleiben gesperrt bis:
1. Provenienz von $B_3^{\mathrm{adm}}$ aus NEU-155 geklärt,
2. Stabilitätsnachweis $\delta_p(\mathfrak{B}) \subseteq \mathfrak{B}$ quellenfest,
3. Schichttrennung Quellenbefund / Konstruktion formalisiert.
