# [O-229-2a-ii] — Wres-Äquivarianz: Fixraum vs. Wres-Nullraum

**Elternknoten:** [O-229-2a — Symmetrieklassifikation des kanonischen Randvektors $b_p$]  
**Arbeitsstatus:** `✓[M]_part` (ii.1 + ii.2a geschlossen; ii.2b offen)  
**Datei:** NEU-231 (rev. 2026-07-27)  
**Quellen:** NEU-017 (OP-3.1.2), NEU-019 (OP-3.3)

---

## Typisierungspräzision

Die zentrale Typbarriere lautet:

$$
\text{NEU-017-Wirkung auf } M_1
\quad\neq\quad
\text{Wirkung auf } Y_p = \overline{\operatorname{Ran}T_p^{\mathrm{raw}}}.
$$

Das Residuenargument liefert sauber:
$$
(M_1)^{N^\times} \subseteq \ker\operatorname{Wres}_{BC}^{(2,0)}.
$$
Es liefert **nicht** typkorrekt
$Y_p^{G_{\mathrm{Wres}}} \subseteq \mathcal{N}_{\mathrm{Wres,rel}}$,
solange keine äquivariante Brüke
$$
\iota_p: Y_p \longrightarrow M_1
\qquad\text{oder}\qquad
J_p: M_1 \longrightarrow Y_p
$$
mit nachgewiesener Verträglichkeit zu Wirkung, Wres-Nullraum
und $T_p^{\mathrm{raw}}$ konstruiert ist.

---

## Teilknoten [O-229-2a-ii.1] — Quellenextraktion

**Frage:** Definieren NEU-017 und NEU-019 eine Wres-Wirkung oder eine
äquivariante Schnittfolge auf $Y_p = \overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$?

### Befund aus NEU-017

NEU-017 definiert eine $N^\times$-Wirkung ausschließlich auf dem
Hochschild-algebraischen Korrekturmodul
$$
M := \ker\bigl(\partial: C^{k-1}(F^3, F^3) \to C^k(F^3, F^3)\bigr),
$$
mit Ladungsraumzerlegung $M = M_1 \oplus \prod_{\chi \neq 1} M_\chi$.
Das Hauptresultat $H^1(N^\times, M_{\chi \neq 1}) = 0$ sichert die
ladungsneutrale Liftkorrektur.

Eine Wirkung auf einem abstrakten Hilbertraum-Abschluss
$\overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$ ist in NEU-017 **nicht definiert**.

### Befund aus NEU-019

NEU-019 definiert $\mathcal{N}_{\mathrm{Wres,rel}} \leftrightarrow
\ker\operatorname{Wres}_{BC}^{\mathrm{top}}$ als algebraisch-analytisches
Konzept auf dem Grad-3-Symbolraum $F^3 A_{BC}^{an}$.

Eine exakte Sequenz
$0 \to \mathcal{N}_{\mathrm{Wres,rel}} \to Y_p \xrightarrow{q_p} Y_p/\mathcal{N}_{\mathrm{Wres,rel}} \to 0$
mit $N^\times$-Wirkung auf beiden Ebenen ist in NEU-019 **nicht konstruiert**.

$$
\boxed{
[O\text{-}229\text{-}2a\text{-ii.1}\text{ -source-extraction}]
\quad
\checkmark[M]_{\mathrm{neg,Quelle}}
}
$$

**Befund:** Keine quellenseitig definierte Wres-Wirkung oder äquivariante
Schnittfolge auf $Y_p$.

---

## Teilknoten [O-229-2a-ii.2a] — Fixsektor im Hochschild-Modul

**Frage (typisiert auf dem tatsächlich definierten Objekt):**
Liegt $(M_1)^{N^\times}$ im Nullraum von $\operatorname{Wres}_{BC}^{(2,0)}$?

### Analyse

Sei $F \in M_1$ ($N^\times$-invariant, Ladungssektor $\chi = 1$).
Dann ist der Diagonalanteil $(R_3 F)_{M,M,0}$ strukturell konstant
(kein $\log m$-Wachstum, da die $\Lambda(n)$-Beiträge aus nicht-trivialen
Primstellen ausgeblendet sind).

Nach der Singularitätstabelle von NEU-019 (§4.1):
$$
(R_3 F)_{M,M,0} \sim \mathrm{const}
\;\Longrightarrow\;
\lambda_\beta^{\mathrm{mod}}(F) \sim \frac{c_{1,0}(F)}{\beta-1}
\quad\text{(einfacher Pol)}.
$$
Daher:
$$
\operatorname{Wres}_{BC}^{(2,0)}(F)
= \lim_{\beta\to 1^+}(\beta-1)^2\lambda_\beta^{\mathrm{mod}}(F) = 0.
$$

In Summe:
$$
F \in M_1
\;\Longrightarrow\;
\operatorname{Wres}_{BC}^{(2,0)}(F) = 0
\;\Longrightarrow\;
F \in \ker\operatorname{Wres}_{BC}^{\mathrm{top}}.
$$

$$
\boxed{
[O\text{-}229\text{-}2a\text{-ii.2a}]
\quad
\checkmark[M]
}
$$

**Befund (umfangsbegrenzt):**
$$
\boxed{
\text{Die } N^\times\text{-invariante Hochschild-Struktur aus NEU-017/019}
\text{ kann keine nichttriviale doppelte Wres-Klasse auszeichnen.}
}
$$

Der Doppelresiduenkanal verschwindet auf dem invarianten Ladungssektor.
Das ist ein starkes strukturelles No-Go **innerhalb des Hochschild-/Wres-Moduls**.
Es ist aber noch kein No-Go für jeden möglichen $b_p \in Y_p$.

---

## Teilknoten [O-229-2a-ii.2b] — Brücke $M_1 \leftrightarrow \overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$

**Frage:** Existiert im Quellenbestand eine typkorrekte, äquivariante Verbindung
zwischen $M_1$ und $\overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$?

Konkret gesucht ist eine der folgenden Strukturen:

1. Eine stetige lineare Abbildung $\iota_p: Y_p \to M_1$ (oder $J_p: M_1 \to Y_p$),
   die mit der $N^\times$-Wirkung verträglich ist;
2. ein Kompatibilitätsnachweis, dass das Bild $T_p^{\mathrm{raw}}(\mathcal{D}(a_p))$
   als Teilmenge von $M$ (oder einem Quotient davon) aufgefasst werden kann;
3. eine natürliche Einbettung $\overline{\operatorname{Ran}T_p^{\mathrm{raw}}} \hookrightarrow F^3 A_{BC}^{an}$,
   die mit der Wres-Null­ raum-Struktur verträglich ist.

**Kandidaten-Quellen für den Brükenaudit:**

| Quelle | Kandidatmechanismus | Vorprüfung |
|---|---|---|
| NEU-015 (Frobenius-Spur) | $\varepsilon_\beta$-Funktional auf $F^3$ | Algebraisch, kein Hilbertraum-Abschluss |
| NEU-016 (Modulare Spur, Monoidladung) | $P_{\mathrm{ch}}$-Graduierung | Ladungssektor-Zerlegung, Brücke unklar |
| NEU-041 (Kanonischer Kopplungsoperator $C_N$) | Expliziter Operator $C_N: H \to F^3$ | **Starkster Kandidat** — direkte Hilbertraum-zu-Symbol-Abbildung |
| NEU-056 ($\Gamma_N$-Konfinement) | Projektions-/Einbettungsstruktur | Konfinement-Obstruktion, Richtung unklar |

$$
\boxed{
[O\text{-}229\text{-}2a\text{-ii.2b}\text{ -bridge-to-raw-range}]
\quad
?[O]
}
$$

**Nächster Schritt:** Quellenaudit NEU-041 (kanonischer Kopplungsoperator $C_N$)
als stärksten Brückenkandidaten.

---

## Gesamtstatus [O-229-2a-ii]

| Teilknoten | Status |
|---|---|
| [O-229-2a-ii.1] Quellenextraktion | `✓[M]_neg,Quelle` |
| [O-229-2a-ii.2a] Fixsektor im Hochschild-Modul | `✓[M]` |
| [O-229-2a-ii.2b] Brücke $M_1 \leftrightarrow Y_p$ | `?[O]` |

$$
\boxed{
[O\text{-}229\text{-}2a\text{-ii}]
\quad
\checkmark[M]_{\mathrm{part}}
}
$$

**Umfangsbegrenztes No-Go (bereits gesichert):**
Die $N^\times$-invariante Hochschild-Struktur aus NEU-017/019 kann
keine nichttriviale doppelte Wres-Klasse auszeichnen.

**Offen:** Ob eine typkorrekte Brücke zwischen $M_1$ und
$\overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$ das No-Go auf den Rohzielraum
überträgt oder umgeht.

---

## Konsequenz für [O-229-2a] und [O-229-2]

Da [O-229-2a-ii.2b], [O-229-2a-i] und [O-229-2a-iii] offen bleiben:

$$
\boxed{[O\text{-}229\text{-}2a] \quad \checkmark[M]_{\mathrm{part}}}
$$

$$
\boxed{[O\text{-}229\text{-}2] \quad ?[O]}
$$

**Kumulierter Befund für [O-229-2]:**  
Der reine Wres-/Hochschild-Invariantenpfad trägt keine nichttriviale
doppelte Residuenklasse. Offen bleibt, ob eine modulare, ladungsgraduierte
oder durch eine Brückenabbildung erzeugte Struktur einen kanonischen
Randvektor $b_p$ im Rohzielraum $\overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$
auszeichnet.
