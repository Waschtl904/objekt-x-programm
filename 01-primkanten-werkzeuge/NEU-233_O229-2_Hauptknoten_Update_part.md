# [O-229-2] — Intrinsische Quelle des gemischten Randvektors $b_p$

**Status:** `✓[M]_part` (aktualisiert 2026-07-27, zuvor `?[O]`)  
**Datei:** NEU-233 (Statusupdate)  
**Eltern:** [O-229-1δ]

---

## Kumulierter Befund (Stand 2026-07-27)

### Gesichert (neg)

**1. $N^\times$-invariante Hochschild-Struktur trägt keine doppelte Wres-Klasse**

Aus [O-229-2a-ii.2a] (NEU-231):
$$
(M_1)^{N^\times} \subseteq \ker\operatorname{Wres}_{BC}^{(2,0)}.
$$
Jedes $N^\times$-invariante Element des Korrekturmoduls $M$ aus NEU-017
liefert im führenden $(\beta-1)^{-2}$-Residuum den Wert $0$.
Der invariante Hochschild-Sektor kann die für $b_p$ erforderliche
nichttriviale Wres-Quotientenklasse nicht auszeichnen.

**2. Kein quellentypkorrekter Brückenoperator in NEU-041**

Aus [O-229-2a-ii.2b] (NEU-232):
$C_p: \mathbb{C}\varepsilon_p \to \mathcal{H}_{J,N}$ ist liftabhängig
und liefert keine äquivariante, hebungsunabhängige Verbindung zwischen
$M_1$ und $Y_p = \overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$.
Hebungsunabhängigkeit im $Wres$-Quotienten hat in NEU-041 Status `?[O]`;
die Konstruktion von $C_p$ selbst setzt die Liftwahl voraus,
deren Intrinsizität sie nicht begründen kann.

**3. Ladungsgraduierung ($P_{\mathrm{ch}}$) als Hilbertraumprojektor auf $Y_p$: nicht quellendefiniert**

Aus [O-229-2a-iii] (NEU-234):
NEU-016 definiert die Monoidladung als algebraische $\chi$-Zerlegung
auf dem Hochschild-Kochankomplex, nicht als Projektor auf
$Y_p = \overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$.
Eine stetige Abbildung $P_{\mathrm{ch}}: Y_p \to Y_p$ mit
$P_{\mathrm{ch}}^2 = P_{\mathrm{ch}}$ und Wres-Nullraumverträglichkeit
ist im Quellenbestand nicht konstruiert.

### Offen

| Knoten | Inhalt | Status |
|---|---|---|
| [O-229-2a-i] | Modulare Ergodizität: Fixvektor von $\sigma_t^\varphi$ in $Y_p$? | `?[O]` |
| [O-229-2a] Eltern | Symmetrieklassifikation gesamt | `✓[M]_part` |
| [O-229-2] | Intrinsische Quelle gesamt | `✓[M]_part` |

### Nicht ausgeschlossen

- Kandidaten mit gebrochener $N^\times$-Symmetrie ($b_p \in M_\chi$, $\chi \neq 1$)
- Modulare oder ladungsgraduierte Quellen auf dem tatsächlichen Hilbertraum
- Zusätzliche, bislang nicht konstruierte Randdaten
- Andere Objekt-$X$-Architekturen jenseits der $N^\times$/Hochschild-Wirkung

---

## Statusbox

$$
\boxed{[O\text{-}229\text{-}2] \quad \checkmark[M]_{\mathrm{part}}}
$$

**Nächster Schritt:** [O-229-2a-i] — modulare Ergodizität,
formuliert auf dem nach [O-229-2a-iii] verbleibenden Sektor.
