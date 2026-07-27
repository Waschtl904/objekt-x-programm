# [O-229-2a-iii] — Ladungsgraduierung: $P_{\mathrm{ch}}$ als Quelle für $b_p$?

**Elternknoten:** [O-229-2a — Symmetrieklassifikation des kanonischen Randvektors $b_p$]  
**Arbeitsstatus:** `✓[M]_neg,Quelle`  
**Datei:** NEU-234  
**Datum:** 2026-07-27  
**Quelle:** NEU-016 (OP-3.1 Monoidladungs-Kriterium)

---

## Leitfrage

Liefert der Ladungsoperator $P_{\mathrm{ch}}$ (NEU-016) eine $G_p$-invariante
Komponente in $\overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$,
die als kanonischer Randvektor $b_p$ dienen kann?

---

## [O-229-2a-iii.1] — Exakte Typen von $P_{\mathrm{ch}}$

**Frage:** Welche Definitions- und Zielbereiche hat $P_{\mathrm{ch}}$?
Ist $P_{\mathrm{ch}}^2 = P_{\mathrm{ch}}$? Ist $P_{\mathrm{ch}}$ auf $Y_p$ definiert und stetig?

### Befund aus NEU-016

NEU-016 definiert die **Monoidladung** $\chi(\Psi)$ als algebraische Invariante
eines homogenen Hochschild-Kochains $\Psi \in C^k(F^3 A_{BC}^{an}, F^3 A_{BC}^{an})$:
$$
\chi(\Psi) = \frac{N_{\mathrm{out}}}{n_1 \cdots n_k} \in \mathbb{Q}_+^\times.
$$
Die $\sigma_z$-Wirkung auf einem homogenen $\Psi_\chi$ ergibt
$\sigma_{i\beta} \cdot \Psi_\chi = \chi^{-\beta} \Psi_\chi$ (NEU-016, §2.1).
Daraus folgt die Zerlegung des Kochankomplexes in Ladungssektoren:
$$
C^k(F^3, F^3) = \bigoplus_{\chi \in \mathbb{Q}_+^\times} C^k_{\chi}.
$$

**Kritischer Befund:** Ein Projektor $P_{\mathrm{ch}}$ auf einen bestimmten
Ladungssektor $\chi_0$ ist in NEU-016 **nicht als eigenständiges Objekt definiert**.
Die Zerlegung ist algebraisch-graduiert; ein stetig-linearer Projektor
$$
P_{\mathrm{ch}}: Y_p \longrightarrow Y_p, \qquad P_{\mathrm{ch}}^2 = P_{\mathrm{ch}}
$$
auf dem Hilbertraum-Abschluss $Y_p = \overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$
ist in NEU-016 **nicht konstruiert**.

NEU-016 definiert ferner keinen Zusammenhang zwischen der
$\chi$-Zerlegung des Kochankomplexes und dem Abschluss $Y_p$.

$$
\boxed{[O\text{-}229\text{-}2a\text{-iii.1}] \quad \checkmark[M]_{\mathrm{neg,Quelle}}}
$$

---

## [O-229-2a-iii.2] — Verträglichkeit mit $Y_p$ und $\mathcal{N}_{\mathrm{Wres,rel}}$

**Frage:** Gilt $P_{\mathrm{ch}} Y_p \subseteq Y_p$ und
$P_{\mathrm{ch}} \mathcal{N}_{\mathrm{Wres,rel}} \subseteq \mathcal{N}_{\mathrm{Wres,rel}}$?

### Befund

Da [O-229-2a-iii.1] zeigt, dass $P_{\mathrm{ch}}$ als Hilbertraumprojektor
auf $Y_p$ in NEU-016 nicht definiert ist, sind beide Verträglichkeitsfragen
nicht stellbar: es gibt kein Objekt, dessen Verträglichkeit geprüft werden könnte.

Die Ladungszerlegung im Kochankomplex hat keine quellenbelegte Fortsetzung
auf $Y_p$ oder auf $\mathcal{N}_{\mathrm{Wres,rel}}$.

$$
\boxed{[O\text{-}229\text{-}2a\text{-iii.2}] \quad \checkmark[M]_{\mathrm{neg,Quelle}}}
$$

---

## [O-229-2a-iii.3] — Sektormultiplizität

**Frage:** $\dim\bigl(P_{\mathrm{ch}}Y_p / (P_{\mathrm{ch}}Y_p \cap
\mathcal{N}_{\mathrm{Wres,rel}})\bigr) = ?$

### Befund

Da weder $P_{\mathrm{ch}}$ auf $Y_p$ definiert ist ([iii.1]) noch
$\mathcal{N}_{\mathrm{Wres,rel}}$ als Teilmenge von $Y_p$ konstruiert ist
(vgl. NEU-231, [O-229-2a-ii.1]), ist der Quotientenausdruck
typisierungsmäßig nicht wohlgestellt.

Eine Multiplizitätsaussage setzt voraus, dass beide Terme im gleichen
Raum leben und $P_{\mathrm{ch}}$ stetig auf diesem Raum wirkt —
bei des in den Quellen nicht belegt.

$$
\boxed{[O\text{-}229\text{-}2a\text{-iii.3}] \quad \checkmark[M]_{\mathrm{neg,Quelle}}}
$$

---

## [O-229-2a-iii.4] — Kanonische Normierung

**Frage:** Falls ein eindimensionaler Sektor existiert — ist Phase und Norm
intrinsisch festgelegt?

### Befund

Da [iii.1]–[iii.3] zeigen, dass der ladungsgraduierte Projektor auf $Y_p$
nicht quellendefiniert ist, wird [iii.4] nicht erreicht.
Die Frage nach kanonischer Normierung stellt sich nicht,
solange kein Objekt mit dem richtigen Typ existiert.

$$
\boxed{[O\text{-}229\text{-}2a\text{-iii.4}] \quad \checkmark[M]_{\mathrm{neg,Quelle}}}
$$

---

## [O-229-2a-iii.5] — Modulare Verträglichkeit

**Frage:** $\sigma_t^\varphi P_{\mathrm{ch}} = P_{\mathrm{ch}} \sigma_t^\varphi$?

### Befund

Da $P_{\mathrm{ch}}$ auf $Y_p$ nicht existiert, ist diese Kommutationsrelation
nicht formulierbar. Die Frage ist auf den tatsächlich verbleibenden
Hilbertraum-Sektor zu verschieben, der nach [O-229-2a-i]
(modulare Ergodizität) identifiziert werden muss.

Aus NEU-016 ergibt sich immerhin: $\sigma_{i\beta}$ und die Ladungszerlegung
kommutieren auf dem Kochankomplex, da $\sigma_{i\beta} \cdot \Psi_\chi = \chi^{-\beta}\Psi_\chi$
den Ladungssektor erhält. Diese algebraische Kommutation ist aber keine
Hilbertraum-Aussage über $Y_p$.

$$
\boxed{[O\text{-}229\text{-}2a\text{-iii.5}] \quad \checkmark[M]_{\mathrm{neg,Quelle}}}
$$

**Konsequenz für [O-229-2a-i]:** Die modulare Ergodizitätsfrage
darf nicht auf dem Kochankomplex-Sektor gestellt werden,
sondern muss direkt auf dem GNS/Hilbertraum-Abschluss formuliert werden,
ohne die unzulässige Brücke $M_\chi \leftrightarrow Y_p$.

---

## Gesamtstatus [O-229-2a-iii]

| Teilknoten | Status |
|---|---|
| [iii.1] Exakte Typen von $P_{\mathrm{ch}}$ | `✓[M]_neg,Quelle` |
| [iii.2] Verträglichkeit mit $Y_p$ und $\mathcal{N}_{\mathrm{Wres,rel}}$ | `✓[M]_neg,Quelle` |
| [iii.3] Sektormultiplizität | `✓[M]_neg,Quelle` |
| [iii.4] Kanonische Normierung | `✓[M]_neg,Quelle` |
| [iii.5] Modulare Verträglichkeit | `✓[M]_neg,Quelle` |

$$
\boxed{[O\text{-}229\text{-}2a\text{-iii}] \quad \checkmark[M]_{\mathrm{neg,Quelle}}}
$$

**Befund:** NEU-016 definiert $P_{\mathrm{ch}}$ ausschließlich als algebraische
Ladungsgraduierung auf dem Hochschild-Kochankomplex, nicht als
Hilbertraumprojektor auf $Y_p$. Alle fünf Teilknoten schließen negativ,
weil die erforderliche Typen-Grundlage im Quellenbestand fehlt.

---

## Konsequenz für [O-229-2a]

Mit [O-229-2a-ii] `✓[M]_neg,Quelle` und [O-229-2a-iii] `✓[M]_neg,Quelle`
verbleibt nur noch:

$$
\boxed{[O\text{-}229\text{-}2a\text{-i}] \quad ?[O]}
\qquad\text{(modulare Ergodizität, direkt auf GNS-Hilbertraum, ohne Kochankomplex-Brücke)}
$$

$$
\boxed{[O\text{-}229\text{-}2a] \quad \checkmark[M]_{\mathrm{part}}}
$$
