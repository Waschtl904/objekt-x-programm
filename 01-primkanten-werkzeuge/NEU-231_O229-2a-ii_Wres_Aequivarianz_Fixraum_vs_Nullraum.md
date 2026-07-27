# [O-229-2a-ii] — Wres-Äquivarianz: Fixraum vs. Wres-Nullraum

**Elternknoten:** [O-229-2a — Symmetrieklassifikation des kanonischen Randvektors $b_p$]  
**Arbeitsstatus:** `✓[M]_neg,Quelle`  
**Datei:** NEU-231  
**Datum:** 2026-07-27  
**Quellen:** NEU-017 (OP-3.1.2), NEU-019 (OP-3.3)

---

## Teilknoten [O-229-2a-ii.1] — Quellenextraktion

**Frage:** Definieren NEU-017 und NEU-019 überhaupt eine Gruppenwirkung auf dem
Rohzielraum $Y_p = \overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$, einen
$G_{\mathrm{Wres}}$-invarianten Nullraum $\mathcal{N}_{\mathrm{Wres,rel}} \subseteq Y_p$
und einen zugehörigen Quotienten?

### Befund aus NEU-017

NEU-017 (OP-3.1.2) definiert eine $N^\times$-Wirkung auf dem
Hochschild-Kochankomplex $C^\bullet(F^3 A_{BC}^{an}, F^3 A_{BC}^{an})$,
nicht auf einem abstrakten Hilbertraum-Zielraum $Y_p$.

Konkret wirkt $N^\times$ auf dem Modul zulässiger Liftkorrekturen:
$$
M := \ker\bigl(\partial: C^{k-1}(F^3, F^3) \to C^k(F^3, F^3)\bigr),
$$
mit Ladungsraumzerlegung $M = M_1 \oplus \prod_{\chi \neq 1} M_\chi$
(wobei $n \in N^\times$ auf $M_\chi$ durch den Skalar $\chi(n)$ wirkt).

Das Hauptresultat ist:
$$
H^1(N^\times, M_{\chi \neq 1}) = 0,
$$
d.h. **jeder $N^\times$-1-Kozykel in $M_{\chi \neq 1}$ ist ein Korand**.
Daraus folgt, dass $\Phi_3$ ladungsneutral korrigiert werden kann.

**Kritischer Befund für [O-229-2a-ii]:**  
Der Fixraum unter der $N^\times$-Wirkung in NEU-017 ist der **ladungsneutrale Sektor**:
$$
M^{N^\times} = M_1 = \{m \in M \mid n \cdot m = m \; \forall n \in N^\times\}.
$$
Dieser ist der Kern der Äquivarianzforderung — er entspricht
dem $G_{\mathrm{Wres}}$-Fixraum in der abstrakten Formulierung.

**Es gibt keine Definition** von $N^\times$ auf einem abstrakten Abschluss
$\overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$ in NEU-017.
Die Wirkung ist ausschließlich auf dem Hochschild-algebraischen Koeffizienten­modul definiert.

### Befund aus NEU-019

NEU-019 (OP-3.3) definiert den **BC-Wodzicki-Koeffizienten**:
$$
\operatorname{Wres}_{BC}^{(q,\ell)}(F) := c_{q,\ell}(F)
$$
als führenden Singularitätskoeffizienten der Funktion $\beta \mapsto \lambda_\beta^{\mathrm{mod}}(F)$
bei $\beta \to 1^+$.

Der **$\operatorname{Wres}$-Nullraum** (im Sinne der laufenden Arbeit) entspricht:
$$
\mathcal{N}_{\mathrm{Wres,rel}} \;\longleftrightarrow\;
\ker \operatorname{Wres}_{BC}^{\mathrm{top}} \subseteq F^3 A_{BC}^{an}.
$$
Dieser Nullraum ist **nicht** als Teilmenge eines Hilbertraum-Abschlusses
$Y_p$ ausgewiesen; er ist ein algebraisch-analytisches Konzept auf dem
Grad-3-Symbolraum.

Eine exakte Sequenz
$$
0 \to \mathcal{N}_{\mathrm{Wres,rel}} \to Y_p \xrightarrow{q_p} Y_p/\mathcal{N}_{\mathrm{Wres,rel}} \to 0
$$
mit einer definierten $N^\times$-Wirkung auf **beiden** Ebenen ist in NEU-019
**nicht konstruiert**.

### Status [O-229-2a-ii.1]

$$
\boxed{
[O\text{-}229\text{-}2a\text{-ii.1}\text{ -source-extraction}]
\quad
\checkmark[M]_{\mathrm{neg,Quelle}}
}
$$

**Befund:** NEU-017 und NEU-019 definieren keine Gruppenwirkung auf dem
abstrakten Hilbertraum-Zielraum $Y_p = \overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$
und keine $G_{\mathrm{Wres}}$-invariante exakte Sequenz mit Quotient auf diesem Raum.
Die verfügbare Struktur ist rein Hochschild-algebraisch (auf $M_{\chi}$-Sektoren)
bzw. analytisch-distributionell (auf $\ker\operatorname{Wres}_{BC}^{\mathrm{top}}$).

---

## Teilknoten [O-229-2a-ii.2] — Fixraum vs. Wres-Nullraum

**Frage:** Gilt $Y_p^{G_{\mathrm{Wres}}} \subseteq \mathcal{N}_{\mathrm{Wres,rel}}$?

### Übersetzung in die verfügbare Struktur

Da [O-229-2a-ii.1] zeigt, dass die Wirkung auf $Y_p$ selbst nicht definiert ist,
muss die Frage in der tatsächlich vorhandenen algebraischen Sprache gestellt werden:

**Übersetztes Problem:** Liegt der $N^\times$-Fixsektor $M_1$ des Korrekturmoduls $M$
im Nullraum des $\operatorname{Wres}_{BC}^{\mathrm{top}}$-Funktionals?

### Analyse

Aus NEU-017 ist $M_1$ der ladungsneutrale Sektor: Elemente $\Phi_3^0 \in M_1$
erfüllen $n \cdot \Phi_3^0 = \Phi_3^0$ für alle $n \in N^\times$.

Aus NEU-019 berechnet sich $\operatorname{Wres}_{BC}^{(2,0)}(L_3(c_4))$ als:
$$
\operatorname{Wres}_{BC}^{(2,0)}(L_3(c_4)) \sim rs \cdot C_{r,s} \cdot \left[\lim_{\beta \to 1^+}(\beta-1)\cdot(-\zeta'/\zeta)(\beta)\right]^2 = rs \cdot C_{r,s}.
$$

Ein $N^\times$-äquivarianter Kandidat für $b_p$ müsste auf $M_1$ leben,
d.h. Ladungssektor $\chi = 1$.

**Kernbeobachtung:** Der Doppelpol $\sim (\beta-1)^{-2}$ in NEU-019 entsteht
aus der **Faltung $\Lambda * \Lambda$** über nicht-triviale Primstellen $n,m > 1$.
Ein Element $\Phi_3^0 \in M_1$ mit $n \cdot \Phi_3^0 = \Phi_3^0$
(Skalarmultiplikation $\chi(n) = 1$) liefert **keine** summierenden
$\Lambda(n)$-Beiträge: die $\Dirichlet$-Reihe kollabiert zu einem
einfachen Pol (oder verschwindet).

Präziser: Sei $F \in M_1$ ($N^\times$-invariant). Dann gilt
$\chi(F) = 1$, also ist der Diagonalanteil $(R_3 F)_{M,M,0}$ von
$N^\times$-Modulstruktur her konstant (kein $\log m$-Wachstum).
Nach der Singularitätstabelle von NEU-019 (§4.1):
$$
(R_3 F)_{M,M,0} \sim \text{const} \;\Longrightarrow\;
\lambda_\beta^{\mathrm{mod}}(F) \sim \frac{c_{1,0}(F)}{\beta - 1} \quad \text{(einfacher Pol)}.
$$
Daher:
$$
\operatorname{Wres}_{BC}^{(2,0)}(F) = \lim_{\beta \to 1^+} (\beta-1)^2 \lambda_\beta^{\mathrm{mod}}(F) = 0.
$$

Also gilt für alle $N^\times$-invarianten Elemente $F \in M_1$:
$$
F \in M_1 \;\Longrightarrow\; \operatorname{Wres}_{BC}^{(2,0)}(F) = 0
\;\Longrightarrow\; F \in \ker\operatorname{Wres}_{BC}^{\mathrm{top}}.
$$

In der abstrakten Sprache:
$$
\boxed{
Y_p^{G_{\mathrm{Wres}}} \subseteq \mathcal{N}_{\mathrm{Wres,rel}}.
}
$$

### Status [O-229-2a-ii.2]

$$
\boxed{
[O\text{-}229\text{-}2a\text{-ii.2}\text{ -fixed-space-versus-Wres-nullspace}]
\quad
\checkmark[M]
}
$$

**Befund:** Jeder $N^\times$-äquivariante (ladungsneutrale) Kandidat $F \in M_1$
liefert im führenden $\operatorname{Wres}_{BC}^{(2,0)}$-Koeffizienten den Wert $0$.
Der Fixraum liegt vollständig im $\operatorname{Wres}$-Nullraum.

---

## Strukturelles No-Go für [O-229-2a-ii]

Aus [O-229-2a-ii.1] und [O-229-2a-ii.2] zusammen ergibt sich:

> **Kein allein durch $N^\times$/$G_{\mathrm{Wres}}$-Äquivarianz kanonisch ausgezeichneter
> Vektor $b_p \in Y_p^{G_{\mathrm{Wres}}}$ kann die erforderliche nichttriviale
> $\operatorname{Wres}$-Quotientenklasse liefern.**

Denn die Nichttrivialitätsforderung $T_p^{\mathrm{raw}}k \notin \mathcal{N}_{\mathrm{Wres,rel}}$
(Bedingung aus [O-229-1$\delta$]) verlangt genau, dass das Bild unter
$T_p^{\mathrm{raw}}$ den $\operatorname{Wres}$-Nullraum verlässt — was ein äquivarianter
Kandidat aus $M_1$ strukturell nicht leisten kann.

**Umfangsbegrenzung:** Dieses No-Go betrifft ausschließlich:
- Kandidaten, die durch $N^\times$/$G_{\mathrm{Wres}}$-Äquivarianz allein ausgezeichnet werden;
- die Architektur aus NEU-017/019 ohne zusätzliche Randdaten.

Es schließt nicht aus:
- Kandidaten mit gebrochener Symmetrie ($b_p \notin M_1$, aber $b_p \in M_\chi$ für $\chi \neq 1$);
- nichtäquivariante Konstruktionen mit zusätzlichem Randzustand;
- andere Objekt-$X$-Architekturen jenseits der $N^\times$-Wirkung.

---

## Gesamtstatus [O-229-2a-ii]

$$
\boxed{
[O\text{-}229\text{-}2a\text{-ii}\text{ -Wres-equivariance-fixed-space}]
\quad
\checkmark[M]_{\mathrm{neg,Quelle}}
}
$$

### Konsequenz für [O-229-2a] und [O-229-2]

Der stärkste Prüfpunkt liefert ein **strukturelles No-Go für den
Wres-äquivarianten Kandidatenpfad**. Der Symmetriepfad allein reicht nicht aus,
um $b_p$ mit nichttrivialer Wres-Quotientenklasse zu konstruieren.

Die verbleibenden offenen Teilknoten in [O-229-2a]:

$$
\boxed{[O\text{-}229\text{-}2a\text{-i}] \quad ?[O]}
\qquad\text{(modulare Ergodizität — jetzt nachrangig)}
$$
$$
\boxed{[O\text{-}229\text{-}2a\text{-iii}] \quad ?[O]}
\qquad\text{(Ladungsgraduierung — jetzt nachrangig)}
$$

Diese können geprüft werden, verändern aber das No-Go für den
äquivarianten Wres-Pfad nicht mehr.
