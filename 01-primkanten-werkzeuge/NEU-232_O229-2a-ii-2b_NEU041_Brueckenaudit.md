# [O-229-2a-ii.2b] — Brückenaudit NEU-041: $C_p$ als Verbindung $M_1 \leftrightarrow Y_p$?

**Elternknoten:** [O-229-2a-ii — Wres-Äquivarianz: Fixraum vs. Wres-Nullraum]  
**Arbeitsstatus:** `✓[M]_neg,Quelle`  
**Datei:** NEU-232  
**Datum:** 2026-07-27  
**Quelle:** NEU-041 (X.3.11 Kanonischer Kopplungsoperator $C_N$)

---

## Leitfrage

Liefert NEU-041 eine typkorrekte, äquivariante Verbindung zwischen
$M_1$ und $Y_p = \overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$?

---

## [O-229-2a-ii.2b1] — Exakte Typen von $C_p$

**Frage:** Welche Definitions- und Zielbereiche hat $C_p$?
Ist die Abbildung auf primitiven Klassen oder gewählten Hebungen definiert?
Landet die unprojizierte Kopplung im Grad-3-Symbolraum?
Vernichtet $\Pi_{J,N}$ Wres-relevante Information?

### Befund

Aus NEU-041 §4, Formeln (41.6)–(41.7):

$$
C_p: \mathbb{C}\varepsilon_p \longrightarrow \mathcal{H}_{J,N},
\qquad
C_p\varepsilon_p = \Pi_{J,N}\,\widetilde{\omega}_2(\widehat{\varepsilon}_p, L_3^\circ) =: \Psi_p.
$$

Exakte Typen:

| Objekt | Typ / Raum |
|---|---|
| $\operatorname{Dom}C_p$ | $\mathbb{C}\varepsilon_p$ (eindimensionaler Hebungsraum, nicht primitiverKlassenraum) |
| $\operatorname{Codom}C_p$ | $\mathcal{H}_{J,N}$ (Jacobi-Sektor des GNS-Hilbertraums) |
| $\operatorname{Dom}\widetilde{\omega}_2$ | $B_3 \times F^3 A_{BC}^{an}$ (Hochschild-algebraisch) |
| $\operatorname{Codom}\widetilde{\omega}_2$ | $F^3 A_{BC}^{an}$ (Grad-3-Symbolraum) |
| $\Pi_{J,N}$ | Projektion $F^3 A_{BC}^{an} \to \mathcal{H}_{J,N}$ (vernichtet alle Nicht-Jacobi-Moden) |

**Kritische Einzelbefunde:**

1. **Hebungsabhängigkeit:** $C_p$ ist nur relativ zu einer gewählten Fourier-geladenen Hebung
 $\widehat{\varepsilon}_p \in B_3$ definiert. Ohne Hebungswahl ist $C_p$ nicht definiert
 (NEU-041 §3, Bedingung 1–3; Hebungsunabhängigkeit hat Status `?[O]`, vgl. (41.4)).

2. **Kein primitiver Klassenraum:** $\operatorname{Dom}C_p = \mathbb{C}\varepsilon_p$ ist der
 gewählte Lift, nicht der Quotient primitiver Klassen.

3. **Vorprojektion im Symbolraum:** $\widetilde{\omega}_2(\widehat{\varepsilon}_p, L_3^\circ)
 \in F^3 A_{BC}^{an}$ lebt im Grad-3-Symbolraum, **nicht** in einem Hilbertraum-Abschluss.

4. **$\Pi_{J,N}$ vernichtet Nicht-Jacobi-Moden:** Die Projektion auf den Jacobi-Sektor
 löscht systematisch alle Fourierorbits, die nicht in $\mathcal{H}_{J,N}$ liegen.
 Ob die Wres-$(2,0)$-Klasse im Jacobi-Sektor repräsentiert wird, ist nicht gezeigt.

5. **Zielraum $\mathcal{H}_{J,N} \neq Y_p$:** Der Zielraum ist der Jacobi-Sektor
 des GNS-Hilbertraums, nicht $\overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$.
 NEU-041 setzt nirgends $\mathcal{H}_{J,N} = Y_p$ oder $\Psi_p = T_p^{\mathrm{raw}}k$.

$$
\boxed{
[O\text{-}229\text{-}2a\text{-ii.2b1}]
\quad
\checkmark[M]_{\mathrm{neg,Quelle}}
}
$$

**Befund:** $C_p$ ist eine hebungsabhängige Abbildung
$\mathbb{C}\varepsilon_p \to \mathcal{H}_{J,N}$, keine Hilbertraum-zu-Symbol-Abbildung
und keine Abbildung in $Y_p$ oder aus $M_1$.

---

## [O-229-2a-ii.2b2] — Beziehung zu $M_1$

**Frage:** Existiert in NEU-041 eine quellendefinierte Abbildung
$j_p: M_1 \to \operatorname{Dom}C_p$ oder $r_p: \operatorname{Dom}C_p \to M_1$
mit $r_p(x) \in \ker\partial$, $r_p(x) \in M_1$, und $N^\times$-Äquivarianz?

### Befund

NEU-041 konstruiert $C_p$ aus:
- $\widehat{\varepsilon}_p \in B_3$ (Fourier-geladene Hebung des Primkanals),
- $L_3^\circ \in F^3 A_{BC}^{an}$ (Grad-3-Kozykel),
- $\widetilde{\omega}_2$ (Hochschild-2-Kozykel aus NEU-015/016).

$M_1 = \ker\partial \cap (C^{k-1})_1$ (ladungsneutraler Korrektursektor aus NEU-017)
erscheint in NEU-041 **an keiner Stelle**.

Eine Abbildung $j_p$ oder $r_p$ mit den geforderten Eigenschaften ist weder
definiert noch erwähnt. Die gemeinsame Verwendung von $L_3^\circ$ in NEU-017
(als Rand $\partial\Phi_3 = L_3$) und NEU-041 (als Kopplungspartner in $\widetilde{\omega}_2$)
konstituiert keine Brücke zwischen $M_1$ und $\operatorname{Dom}C_p$:
die $L_3$-Instanzen spielen verschiedene algebraische Rollen.

$$
\boxed{
[O\text{-}229\text{-}2a\text{-ii.2b2}]
\quad
\checkmark[M]_{\mathrm{neg,Quelle}}
}
$$

**Befund:** Keine quellendefinierte Verbindung zwischen $M_1$ und $\operatorname{Dom}C_p$.

---

## [O-229-2a-ii.2b3] — Beziehung zu $Y_p$

**Frage:** Definiert NEU-041 eine kanonische Abbildung $\mathcal{H}_{J,N} \to Y_p$
oder umgekehrt? Werden $\Psi_p = T_p^{\mathrm{raw}}k$ oder
$\mathcal{H}_{J,N} = Y_p$ gesetzt?

### Befund

NEU-041 definiert ausschließlich:
$$
C_p\varepsilon_p = \Psi_p \in \mathcal{H}_{J,N}.
$$

Weder $T_p^{\mathrm{raw}}$ noch $\overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$
kommen in NEU-041 vor. Die Gleichungen $\Psi_p = T_p^{\mathrm{raw}}k$
oder $\mathcal{H}_{J,N} = Y_p$ werden an keiner Stelle behauptet oder bewiesen.

Die Feshbach-Weyl-Zielgröße (41.10) verwendet $\langle\Psi_p, S_N(s,s)^{-1}\Psi_p\rangle_{Wres}$
im Jacobi-Sektor — das ist ein Spektralausdruck in $\mathcal{H}_{J,N}$,
kein Randvektor in $Y_p$.

$$
\boxed{
[O\text{-}229\text{-}2a\text{-ii.2b3}]
\quad
\checkmark[M]_{\mathrm{neg,Quelle}}
}
$$

**Befund:** $\mathcal{H}_{J,N} \neq Y_p$ in NEU-041. Keine Abbildung zwischen beiden Räumen konstruiert.

---

## [O-229-2a-ii.2b4] — Äquivarianz und Wres-Abstieg

**Frage:** Sind die für einen Bruchennachweis erforderlichen Eigenschaften—
$N^\times$-Äquivarianz von $C_p$ und Wres-Nullraumverträglichkeit— in NEU-041 bewiesen?

### Befund

NEU-041 enthält:

- **Hebungsunabhängigkeit:** Bedingung (41.4) fordert
 $\widehat{\varepsilon}_p \sim \widehat{\varepsilon}_p' \Rightarrow C_pC_p^\# = C_p'C_p'^\#$
 im $Wres$-Quotienten. Status: `?[O]` (NEU-041 §3, Bedingung 4).

- **$N^\times$-Äquivarianz von $C_p$:** Eine Bedingung
 $C_p(n \cdot x) = n \cdot C_p(x)$ wird in NEU-041 **nicht formuliert und nicht bewiesen**.

- **Wres-Nullraum-Verträglichkeit:** Die Feshbach-Struktur arbeitet mit
 $\langle\Psi_p, \cdot\rangle_{Wres}$, aber eine Aussage
 $B_p^{-1}(\mathcal{N}_{\mathrm{Wres,rel}}) = ?$ ist nicht konstruiert.

**Zirkularitätspunkt (bestätigt):** $C_p$ ist liftabhängig über $\widehat{\varepsilon}_p$.
Eine aus $C_p$ abgeleitete Brücke zu $Y_p$ würde die Liftwahl voraussetzen,
deren Unabhängigkeit sie begründen soll. Dieser Zirkularitätspunkt ist
in NEU-041 offen (Hebungsunabhängigkeit `?[O]`) und durch die vorhandene
Architektur nicht aufgelöst.

$$
\boxed{
[O\text{-}229\text{-}2a\text{-ii.2b4}]
\quad
\checkmark[M]_{\mathrm{neg,Quelle}}
}
$$

**Befund:** Weder $N^\times$-Äquivarianz noch Wres-Nullraumverträglichkeit von $C_p$
sind in NEU-041 formuliert oder bewiesen.

---

## Gesamtstatus [O-229-2a-ii.2b]

| Teilknoten | Status |
|---|---|
| [ii.2b1] Exakte Typen von $C_p$ | `✓[M]_neg,Quelle` |
| [ii.2b2] Beziehung zu $M_1$ | `✓[M]_neg,Quelle` |
| [ii.2b3] Beziehung zu $Y_p$ | `✓[M]_neg,Quelle` |
| [ii.2b4] Äquivarianz und Wres-Abstieg | `✓[M]_neg,Quelle` |

$$
\boxed{
[O\text{-}229\text{-}2a\text{-ii.2b}\text{ -NEU41-bridge}]
\quad
\checkmark[M]_{\mathrm{neg,Quelle}}
}
$$

**Befund:** NEU-041 definiert $C_p$ als liftabhängige Abbildung
$\mathbb{C}\varepsilon_p \to \mathcal{H}_{J,N}$. Es existiert keine typkorrekte,
äquivariante Verbindung zu $M_1$ oder $Y_p = \overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$.
Die Hebungsunabhängigkeit ist offen und die Konstruktion von $C_p$ selbst setzt die
Liftwahl voraus, deren Intrinsizität sie nicht begründen kann.

**Umfangsbegrenzung:** Dieses Ergebnis widerlegt $C_N$ nicht als Kopplungsoperator
für die Feshbach-Weyl-Zielgröße. Es zeigt nur, dass NEU-041 die benötigte
Brücke zwischen Hochschild-Fixsektor, Wres-Quotient und Rohzielraum
gegenwrtig nicht liefert.

---

## Konsequenz für [O-229-2a-ii] und [O-229-2a]

$$
\boxed{[O\text{-}229\text{-}2a\text{-ii.2b}] \quad \checkmark[M]_{\mathrm{neg,Quelle}}}
\qquad\Longrightarrow\qquad
\boxed{[O\text{-}229\text{-}2a\text{-ii}] \quad \checkmark[M]_{\mathrm{neg,Quelle}}}
$$

Da [O-229-2a-ii.2b] als einziger offener Unterknoten von [O-229-2a-ii] mit
`neg,Quelle` geschlossen wird und [ii.1] sowie [ii.2a] bereits geschlossen sind,
ist [O-229-2a-ii] vollständig abgeschlossen.

Für [O-229-2a] verbleiben [O-229-2a-i] und [O-229-2a-iii] offen.
Solange diese offen sind, bleibt:

$$
\boxed{[O\text{-}229\text{-}2a] \quad \checkmark[M]_{\mathrm{part}}}
$$
