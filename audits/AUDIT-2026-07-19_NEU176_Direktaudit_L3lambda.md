# AUDIT 2026-07-19 — Direktaudit NEU-176: L_{3,λ} als auswertbare Abbildung
*(Revision 2: DAG-Korrektur vom 2026-07-19, 12:01 CEST)*

## Anlass

Direktaudit gemäß atomarer Auditfrage zu [O-193-2]:

> Definiert NEU-176 tatsächlich eine Abbildung $L_{3,\lambda}: A^{\otimes 4} \to A$, deren Wert für beliebige zulässige Eingaben konkret berechnet werden kann?

Quellenbefund: $\checkmark[M]_{\mathrm{part}}$ — Produktansatz-Schablone vorhanden, aber unvollständig typisiert.

Dieses Dokument fixiert drei typologische Korrekturen, schließt einen Teilknoten algebraisch, präzisiert den [O-176-1a]-Status und korrigiert die DAG-Sperrgrafik.

---

## Bestätigter Gesamtstatus

$$\boxed{[O\text{-}193\text{-}2a] \quad \checkmark[M]_{\mathrm{part}}}$$

NEU-176 liefert eine Produktansatz-Schablone, aber noch keinen vollständig typisierten und auswertbaren $L_{3,\lambda} \in C^4_{\mathrm{fin},\lambda}(A,A)$.

---

## Korrektur 1 — Zielmodul der Produktformel

### Problem

Die in NEU-176 ([O-176-1]) angegebene Formel

$$L_{3,\lambda}(a_1,a_2,a_3,a_4) := \sum_k c_k \cdot f_k(a_1)\,f_k(a_2)\,f_k(a_3)\,f_k(a_4)$$

liegt mit der rechten Seite zunächst in $\mathbb{C}$, nicht in $A$. Für $L_{3,\lambda} \in C^4(A,A)$ muss mindestens stehen:

$$L_{3,\lambda}(a_1,a_2,a_3,a_4) = \sum_k c_k \prod_{j=1}^4 f_{k,j}(a_j)\cdot m_k, \qquad m_k \in A.$$

Im Spezialfall $m_k = 1_A$ (Bild in $\mathbb{C}\cdot 1_A \subset A$):

$$L_{3,\lambda}(a_1,a_2,a_3,a_4) = \left(\sum_k c_k \prod_{j=1}^4 f_{k,j}(a_j)\right)1_A.$$

Falls der Zielmodul $\mathbb{C}$ ist, handelt es sich nicht um einen Kozykel in $C^4(A,A)$, sondern in $C^4(A,\mathbb{C})$. Diese Koeffizientenfrage muss vor jedem Paarungstest eindeutig fixiert werden.

### Gewichtsregel mit Zielvektor

Mit vier möglicherweise verschiedenen Gewichten und Zielelement $m_k \in A_{\nu_k}$ lautet die korrekte Gewichtsadditivitätsbedingung:

$$\lambda = \nu_k + \sum_{j=1}^4 \lambda_{k,j},$$

wobei $\lambda_{k,j}$ das Gewicht von $f_{k,j}$ und $\nu_k$ das Gewicht von $m_k$ ist. Für $m_k = 1_A$ gilt $\nu_k = 0$.

Die Verwendung desselben Symbols $f_k$ in allen vier Slots in NEU-176 suggeriert dieselbe Eigenfunktion in jedem Argument. Die allgemeine Formel erfordert vier getrennte Funktionale $f_{k,1}, f_{k,2}, f_{k,3}, f_{k,4} \in A^\vee$ mit individuellen Gewichten.

**Restlücke #1:** Expliziter Zielmodul ($A$ vs. $\mathbb{C}$) und explizite Zielvektoren $m_k \in A$.

---

## Korrektur 2 — Eigenfunktionale; Präzisierter Status [O-176-1a]

### Begriffliche Korrektur

Die Frage [O-176-1a] bezog sich fälschlicherweise auf **Eigenvektoren von $A$**. Da $f_{k,j}: A \to \mathbb{C}$, liegen die Faktoren in $A^\vee$. Der korrekte Knoten fragt:

> Existieren nichttriviale **Eigenfunktionale** der dualen Zeitwirkung $\alpha_t^\vee$ auf $A^\vee$?

### Algebraischer Abschluss der Existenzfrage

**Lemma.** Sei $A = \bigoplus_{g \in \Gamma} A_g$ mit $\alpha_t(a_g) = g^{it} a_g$. Ist $A_g \neq 0$, wähle $f_g \in A_g^\vee$ nichtverschwindend, durch null auf alle anderen Komponenten fortgesetzt. Dann:

$$(\alpha_t^\vee f_g)(a) = f_g(\alpha_{-t}(a)) = g^{-it} f_g(a).$$

**Anwendung.** Für $n > 1$: $\mu_n \in A_n$, $\mu_n \neq 0$ (da $\mu_n^* \mu_n = 1$). Somit existiert $f_n \in A^\vee$ mit $f_n(\mu_n) = 1$ und $\alpha_t^\vee f_n = n^{-it} f_n$.

### Präzisierter Status [O-176-1a]

$$\boxed{\text{Existenz dualer Eigenfunktionale} \quad \checkmark[M]}$$

$$\boxed{\text{Konstruktion geeigneter expliziter } f_{k,j} \text{ für den Produktansatz} \quad ?[O]}$$

Die **Existenz** (nicht explizit berechenbar, nur existenziell gewählt) folgt algebraisch aus der $\Gamma$-Gradierung. Die **explizite Konstruktion** von $f_{k,j}$, die zusätzlich die Kozykelbedingung $bL_{3,\lambda} = 0$ erfüllt, bleibt offen.

**Restlücke #2:** Konstruktion geeigneter expliziter Eigenfunktionale $f_{k,j}$ für den Produktansatz.

---

## Korrektur 3 — DAG-Korrektur: [O-193-2] ist offen, nicht gesperrt

### Kernpunkt

Die fünf Datenklassen der fehlenden $L_{3,\lambda}$-Formel blockieren primär **[O-193-4]** (die gezielte Paarungsrechnung $\langle L_{3,\lambda}, z_{-\lambda}\rangle$).

Sie blockieren **nicht** [O-193-2], weil ein Kandidat

$$z_{-\lambda} \in C_4(A, A^\vee)_{-\lambda}$$

unabhängig davon gesucht werden kann, ob $L_{3,\lambda}$ bereits vollständig auswertbar ist. Ebenso hängt der Randtest $\partial z_{-\lambda} = 0$ nur vom Kandidaten und der $A$-Bimodulstruktur auf $A^\vee$ ab.

### Korrekter Knotenstatus

| Knoten | Status | Gesperrt an |
|---|---|---|
| [O-193-2] | **?[O] offen** | (nicht gesperrt — Dualzyklussuche kann beginnen) |
| [O-193-3] | ?[O] gesperrt | [O-193-2]: ohne konkreten Kettenkandidaten kein Randtest |
| [O-193-4] | ?[O] gesperrt | [O-193-2] + vollständige Formel für $L_{3,\lambda}$ |
| [O-193-5] | ?[O] gesperrt | positiver Abschluss von [O-193-3] und [O-193-4] |

### Bereinigter DAG

```
[O-193-2]  ─────────────────────────────────────────────────────────▶  [O-193-3]

( [O-193-2] + vollständige Formel für L_{3,λ} )  ───────────────────▶  [O-193-4]

[O-193-3] + [O-193-4]  ─────────────────────────────────────────▶  [O-193-5]  ───▶  [O-176-3]

[O-176-2] + [O-176-3]  ─────────────────────────────────────────▶  [L_{3,λ}] ≠ 0
```

**Konsequenz:** Genau bei [O-193-2] kann konstruktiv weitergearbeitet werden. Die Suche nach einem dualen Kettenkandidaten $z_{-\lambda} \in C_4(A, A^\vee)_{-\lambda}$ ist der nächste offene Arbeitsschritt.

---

## Bereinigte Restlückenliste (für [O-193-4])

Folgende fünf Datenklassen müssen explizit angegeben werden, bevor $L_{3,\lambda}$ in die Paarung $\langle L_{3,\lambda}, z_{-\lambda}\rangle$ eingesetzt werden kann:

| # | Fehlende Daten | Primär blockiert |
|---|---|---|
| 1 | Zielmodul und Zielvektoren $m_k \in A_{\nu_k}$ | [O-193-4] |
| 2 | Konstruktion expliziter Eigenfunktionale $f_{k,j} \in A^\vee$ mit $bL_{3,\lambda} = 0$ | [O-176-2], [O-193-4] |
| 3 | Endliche Koeffizientenfamilie $c_k \in \mathbb{C}$, $\#\{k: c_k \neq 0\} < \infty$ | [O-193-4] |
| 4 | Konkretes nichttriviales Gewicht $\lambda \neq 0$ | [O-193-4] |
| 5 | Vollständig auswertbare Generatorregel auf $e(r)$, $\mu_n$, $\mu_n^*$ | [O-193-4] |

**Diese Datenklassen blockieren nicht [O-193-2].**

---

## Aktualisierter Knotenstatus NEU-176

| Knoten | Inhalt | Status |
|---|---|---|
| [O-176-1] | $\exists\, \lambda\neq 0,\; L_{3,\lambda} \in C^4_{\mathrm{fin},\lambda}$ | $\checkmark[K]$ (unter korrigierter Typdefinition mit $m_k$) |
| [O-176-1a] Existenz | Existenz nichttrivialer dualer Eigenfunktionale | $\checkmark[M]$ (aus $\Gamma$-Gradierung) |
| [O-176-1a] Konstruktion | Explizite $f_{k,j}$ mit Kozykelbedingung | $?[O]$ |
| [O-176-2] | $bL_{3,\lambda} = 0$ | $?[O]$ |
| [O-176-3] | $L_{3,\lambda} \notin bC^3_{\mathrm{fin},\lambda}$ | $?[O]$ — zentraler offener Knoten |
| [O-176-4] | $[L_{3,\lambda}] \neq 0$ in $H^4(C_{\mathrm{fin},\lambda})$ | $?[O]$ ($\equiv [O\text{-}176\text{-}2] \wedge [O\text{-}176\text{-}3]$) |
| [O-176-5] | $[P^{\mathrm{ch}}]([L_{3,\lambda}]) \neq 0$ | $\checkmark[K]\,|\,[O\text{-}176\text{-}4]$ |

---

## Gesamtstand [O-193-x]

```
[O-193-1a]  ✓[K]
[O-193-1b]  ✓[M]
[O-193-1c]  ✓[M]
[O-193-2a]  ✓[M]_part   (Quellenbefund: Produktschablone vorhanden, nicht vollständig typisiert)
[O-193-2]   ?[O] OFFEN   ←── nächster konstruktiver Arbeitsschritt: Dualzykluskandidat z_{-λ}
[O-193-3]   ?[O] gesperrt an [O-193-2]
[O-193-4]   ?[O] gesperrt an [O-193-2] + 5 Datenklassen
[O-193-5]   ?[O] gesperrt an [O-193-3] + [O-193-4]
```

$$\boxed{\text{Nächster Schritt: Konstruktion eines Dualzykluskandidaten }z_{-\lambda} \in C_4(A,A^\vee)_{-\lambda}\text{ für [O-193-2].}}$$
