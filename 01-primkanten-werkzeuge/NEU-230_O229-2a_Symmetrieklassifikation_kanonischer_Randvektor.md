# [O-229-2a] — Symmetrieklassifikation des kanonischen Randvektors $b_p$

**Elternknoten:** [O-229-2 — Intrinsische Quelle des gemischten Randvektors]  
**Arbeitsstatus:** `?[O]`  
**Datei:** NEU-230  
**Datum:** 2026-07-27

---

## Leitfrage

Erzwingen die vorhandenen Symmetrien und Funktorialitäten der Primkanalarchitektur
einen ausgezeichneten Vektor

$$
b_p \in \overline{\operatorname{Ran} T_p^{\mathrm{raw}}}, \qquad \|b_p\| \le 1,
$$

erzwingen sie $b_p = 0$, oder lassen sie eine nichtkanonische Familie von Kandidaten zu?

---

## Anti-Zirkularitätsbedingungen (geerbt von [O-229-2])

Ein Kandidat $b_p$ ist nur zulässig, wenn:

1. er vor der Wahl eines gewünschten normierten Lifts definiert ist;
2. er nicht aus dem noch undefinierten Feshbach-Transfer $K_p(z)$ rückwärts konstruiert wird;
3. seine Normierung nicht an eine gewünschte Schattenklasse oder Determinantenidentität angepasst wird;
4. sein Definitionsbereich und sein Quotientenabstieg explizit angegeben sind;
5. seine Nichttrivialität durch eine Primärformel oder vollständige Rechnung bewiesen wird.

---

## Strukturrahmen

Sei $G_p$ die Symmetriegruppe, die auf dem Primkanal $p$ tatsächlich vorhanden ist.
Konkret kommen aus der bisherigen Architektur in Frage:

| Symmetrie | Quelle | Wirkung auf $\overline{\operatorname{Ran} T_p^{\mathrm{raw}}}$ |
|---|---|---|
| Modulare Gruppe $\sigma_t^\phi$ | KMS-Zustand, NEU-014 | unitäre Wirkung, $\beta$-abhängig |
| Frobenius-Reziprozität / $\Gamma_N$-Konfinement | NEU-015, NEU-056 | Projektion auf Unterräume |
| Äquivarianter Lift (Wres-relativ) | NEU-017 | Kohärenzforderung an Schnitte |
| Monoidladung $P_{\mathrm{ch}}$ | NEU-016 | Ladungsgraduierung |
| Birman-Schwinger-Randoperator | NEU-049, NEU-050 | kompakte Störungsstruktur |

---

## Klassifikationsschema

### Fall A — eindimensionaler Fixraum

Falls $G_p$ auf $\overline{\operatorname{Ran} T_p^{\mathrm{raw}}}$ einen **eindimensionalen invarianten Unterraum** besitzt,
ist $b_p$ bis auf eine Phase $e^{i\theta}$ und eine Skalierung $\lambda \in (0,1]$ bestimmt.
Die Normierungsbedingung $\|b_p\| \le 1$ schränkt dann nur $\lambda$ ein; die Richtung ist kanonisch.

**Hinreichende Bedingung:** $G_p$ wirkt irreduzibel auf $\overline{\operatorname{Ran} T_p^{\mathrm{raw}}}$
und besitzt einen eindimensionalen Fixpunkt (z.B. zyklischen Vektor des KMS-Zustands).

### Fall B — trivialer Fixraum ($b_p = 0$ erzwungen)

Falls $G_p$ auf $\overline{\operatorname{Ran} T_p^{\mathrm{raw}}}$ **keinen nichtverschwindenden invarianten Vektor** besitzt
— insbesondere wenn die Gruppe nicht-kompakt oder irreduzibel ohne Fixvektor wirkt —
folgt aus der Invarianzforderung sofort $b_p = 0$.

Dies liefert ein **präzises No-Go**: Kein aus der vorliegenden Symmetriearchitektur
allein konstruierter $b_p$-Kandidat kann nichttrivial sein.

**Hinreichende Bedingung:** Die modulare Gruppe $\{\sigma_t^\phi\}_{t \in \mathbb{R}}$
wirkt ergodisch (ohne $L^2$-Fixvektoren außer $0$) auf $\overline{\operatorname{Ran} T_p^{\mathrm{raw}}}$.

### Fall C — mehrdimensionaler Fixraum (nichtkanonische Familie)

Falls $\dim \operatorname{Fix}_{G_p}(\overline{\operatorname{Ran} T_p^{\mathrm{raw}}}) \ge 2$,
gibt es eine ganze Familie von $G_p$-invarianten Kandidaten.
Dann reicht die Symmetrie allein nicht aus, um $b_p$ zu fixieren;
es wird ein zusätzliches Auswahlprinzip benötigt (z.B. Extremalvektor einer Variationsaufgabe).

---

## Zu prüfende Primärfragen

### [O-229-2a-i] — Modulare Ergodizität

Hat die modulare Gruppe $\sigma_t^\phi$ einen nichttrivialen Fixvektor in
$\overline{\operatorname{Ran} T_p^{\mathrm{raw}}}$?

- Relevante Quellen: NEU-014 (KMS), NEU-018 ($\lambda$-modulare Spektralform), NEU-016 (modulare Spur).
- Erwartung aus bisherigen Audits: Die Moduläroperatoren wirken auf dem vollen GNS-Raum
  und besitzen generisch keinen $L^2$-Fixvektor außer dem zyklischen Vektor $\Omega$.
  Ob $\Omega \in \overline{\operatorname{Ran} T_p^{\mathrm{raw}}}$ liegt, ist ungeklärt.
- **Status:** `?[O]`

### [O-229-2a-ii] — Wres-Äquivarianzbedingung

Schränkt die Wres-relative Äquivarianz (NEU-017, NEU-019) den Fixraum
von $G_p$ auf $\overline{\operatorname{Ran} T_p^{\mathrm{raw}}}$ weiter ein?

- Konkret: Verlangt die Schnittbedingung aus NEU-017, dass ein äquivarianter
  Schnitt $b_p$ im Wres-Nullraum $\mathcal{N}_{\mathrm{Wres,rel}}$ landet?
  Falls ja, wäre $b_p \in \mathcal{N}_{\mathrm{Wres,rel}} \cap \overline{\operatorname{Ran} T_p^{\mathrm{raw}}}$,
  was zusammen mit $T_p^{\mathrm{raw}} k \notin \mathcal{N}_{\mathrm{Wres,rel}}$
  (Nichttrivialitätsbedingung) unmittelbar einen Widerspruch liefern würde.
- **Status:** `?[O]`

### [O-229-2a-iii] — Ladungsgraduierung und $P_{\mathrm{ch}}$

Besitzt der Ladungsoperator $P_{\mathrm{ch}}$ (NEU-016) eine Eigenkomponente
in $\overline{\operatorname{Ran} T_p^{\mathrm{raw}}}$, die als $G_p$-invarianter Vektor dient?

- Relevante Quellen: NEU-016 (Monoidladung), NEU-020 ($c_{rs} \neq 0$).
- **Status:** `?[O]`

---

## Vorläufige Einschätzung (ohne abgeschlossenen Primärquellenabgleich)

Aus den bisher geprüften Quellen ergibt sich kein Hinweis auf einen
eindimensionalen $G_p$-Fixraum in $\overline{\operatorname{Ran} T_p^{\mathrm{raw}}}$.

Die modulare Gruppe wirkt typischerweise ohne $L^2$-Fixvektoren außer $\Omega$,
und ob $\Omega$ im Bildraum von $T_p^{\mathrm{raw}}$ liegt, ist nicht belegt.
Die Wres-Äquivarianz könnte sogar einen No-Go-Mechanismus aktivieren (→ [O-229-2a-ii]).

**Dieser Befund ist noch nicht als Negativergebnis abgeschlossen**,
da die drei Teilfragen [O-229-2a-i], [O-229-2a-ii], [O-229-2a-iii]
noch nicht einzeln gegen Primärquellen geprüft wurden.

---

## Statusbox

$$
\boxed{
[O\text{-}229\text{-}2a\text{-canonical-vector-from-existing-symmetries}]
\quad ?[O]
}
$$

**Offene Teilknoten:**

$$
\boxed{[O\text{-}229\text{-}2a\text{-i}] \quad ?[O]}
\qquad
\boxed{[O\text{-}229\text{-}2a\text{-ii}] \quad ?[O]}
\qquad
\boxed{[O\text{-}229\text{-}2a\text{-iii}] \quad ?[O]}
$$

**Nächster Schritt:** Primärquellenabgleich für [O-229-2a-i] (modulare Ergodizität)
gegen NEU-014, NEU-018. Falls dort Ergodizität bestätigt wird und
$\Omega \notin \overline{\operatorname{Ran} T_p^{\mathrm{raw}}}$, liefert dies
ein partielles No-Go für Fall A und verstärkt die Hypothese $b_p = 0$ aus Fall B.
