# NEU-244 — Quotient-first-Zielarchitektur und tautologischer Cone-No-Go

**Datum:** 27. Juli 2026  
**Quellenblock:** NEU-221e, NEU-226, NEU-227, NEU-229 (via NEU-242, NEU-243)  
**Entschiedener Knoten:** \([O\text{-}229\text{-}3B.1f\text{-}c.1\text{-target-complex-architecture}]\)

---

## 1. Auditbereich und Umfang

Diese Datei entscheidet den Zielarchitektur-Knoten

$$
[O\text{-}229\text{-}3B.1f\text{-}c.1\text{-target-complex-architecture}]
$$

für den Wres-relativen Rohkopplungszweig.

Die Entscheidung betrifft ausschließlich den Zweig, in dem

$$
a_p^{\mathrm{raw}}(k,\ell)
= \alpha_p\left\langle
Q_{\mathrm{Wres,rel}}T_p^{\mathrm{raw}}k,\,
Q_{\mathrm{Wres,rel}}T_p^{\mathrm{raw}}\ell
\right\rangle
$$

verwendet wird.

Es wird in dieser Datei noch **kein** nichttriviales Differential konstruiert.

---

## 2. Typkorrekter minimaler Zielraum

Definiere den ausgezeichneten Operator auf Quotientenebene:

$$
F_p^r
:= Q_{\mathrm{Wres,rel}} \circ T_p^{\mathrm{raw}}\big|_{\mathcal{D}(a_p)}
: \mathcal{D}(a_p) \longrightarrow
\mathscr{V}_{\mathrm{rel},p,N}^{\mathrm{pre}} / \mathcal{N}_{\mathrm{Wres,rel}}
$$

und den minimalen abgeschlossenen Bildraum:

$$
Y_p
:= \overline{\operatorname{Ran}F_p^r}^{\,\mathcal{H}_{\mathrm{rel},p,N}}.
$$

Dabei ist $Y_p$ der kleinste abgeschlossene Hilbertraum-Unterraum, der das vollständige quotientierte Kopplungsbild enthält.

**Typkorrekturhinweis:** Die Bezeichnung $\overline{\operatorname{Ran}T_p^{\mathrm{raw}}} \subseteq \mathcal{H}_{\mathrm{rel},p,N}$ wird vermieden, da $T_p^{\mathrm{raw}}$ zunächst in den Rohzielraum $\mathscr{V}_{\mathrm{rel},p,N}^{\mathrm{pre}}$ und nicht unmittelbar in die Hilbertraumvervollständigung abbildet. Typkorrekt ist $Y_p$ als Abschluss des Bildes von $F_p^r = Q_{\mathrm{Wres,rel}} \circ T_p^{\mathrm{raw}}|_{\mathcal{D}(a_p)}$.

---

## 3. Positivität erzwingt Quotientenfaktorisierung

Für die Rohform gilt:

$$
N_{a_p^{\mathrm{raw}}} = \ker F_p^r = \left(T_p^{\mathrm{raw}}\right)^{-1}\!\left(\mathcal{N}_{\mathrm{Wres,rel}}\right).
$$

Sei $\beta_p: \mathcal{D}(a_p) \to \mathbb{C}$ linear und erfülle

$$
|\beta_p(k)|^2 \le a_p^{\mathrm{raw}}(k,k).
$$

Für jedes $n \in N_{a_p^{\mathrm{raw}}}$ gilt dann:

$$
|\beta_p(n)|^2 \le a_p^{\mathrm{raw}}(n,n) = 0,
\qquad \text{also} \quad \beta_p(n) = 0.
$$

Daher faktorisiert $\beta_p$ eindeutig durch

$$
\mathcal{D}(a_p)/N_{a_p^{\mathrm{raw}}}.
$$

Ebenso faktorisiert jedes bezüglich der Wres-Seminorm beschränkte Funktional auf dem Rohzielraum eindeutig durch

$$
\mathscr{V}_{\mathrm{rel},p,N}^{\mathrm{pre}} / \mathcal{N}_{\mathrm{Wres,rel}}.
$$

Die Quotientenebene ist damit **keine** bloß bequeme Wahl. Sie wird für die analytisch zulässige Randdatenausgabe durch die Positivitätsbedingung erzwungen.

$$
\boxed{
[O\text{-}229\text{-}3B.1f\text{-}c.1a\text{-positivity-forces-quotient-output}]
\quad \checkmark[M].
}
$$

---

## 4. Kanonische Range-Identifikation

Die Abbildung

$$
\overline{F}_p^r:
\mathcal{D}(a_p)/N_{a_p^{\mathrm{raw}}}
\longrightarrow Y_p,
\qquad
[k] \longmapsto F_p^r(k)
$$

ist **wohldefiniert** (denn $N_{a_p^{\mathrm{raw}}} = \ker F_p^r$) und **injektiv**.

Ferner gilt:

$$
a_p^{\mathrm{raw}}(k,k) = \alpha_p \left\|\overline{F}_p^r[k]\right\|^2.
$$

Für $\alpha_p > 0$ definiert

$$
U_p[k] := \sqrt{\alpha_p}\,\overline{F}_p^r[k]
$$

eine Isometrie. Nach Vervollständigung entsteht eine unitäre Abbildung:

$$
U_p: H_{a^{\mathrm{raw}},p} \xrightarrow{\;\cong\;} Y_p.
$$

$$
\boxed{
[O\text{-}229\text{-}3B.1f\text{-}c.1b\text{-canonical-quotient-range-identification}]
\quad \checkmark[M].
}
$$

**Umfang:** Die Identifikation gilt für den Rohkopplungszweig mit der angegebenen Pullback-Form und $\alpha_p > 0$.

---

## 5. Architekturentscheidung

Die für das spätere Mischfunktional und Randdatum relevante Endarchitektur ist **quotient-first (Typ A)**:

$$
C_{p,\mathrm{tar}}^{r+s}
\subseteq
\mathscr{V}_{\mathrm{rel},p,N}^{\mathrm{pre}} / \mathcal{N}_{\mathrm{Wres,rel}}
$$

bzw. nach Vervollständigung

$$
C_{p,\mathrm{tar}}^{r+s} \subseteq \mathcal{H}_{\mathrm{rel},p,N}.
$$

Als minimaler Bildraum wird $Y_p$ ausgezeichnet.

**Typ B (prequotient-first) ist nicht widerlegt.** Er ist jedoch nur als **vorgelagerte Konstruktion** zulässig: Falls ein intrinsisches Rohdifferential $d_{\mathrm{pre}}$ gefunden wird, muss bewiesen werden:

$$
d_{\mathrm{pre}}\,\mathcal{N}_{\mathrm{Wres,rel}}^n \subseteq \mathcal{N}_{\mathrm{Wres,rel}}^{n+1}.
$$

Der dadurch induzierte Quotientenkomplex muss anschließend die Quotient-first-Endarchitektur reproduzieren. Typ A und Typ B sind daher **keine gleichrangigen Alternativen**: Typ A ist die notwendige Endarchitektur; Typ B kann höchstens eine vorgelagerte Kettenrealisierung liefern.

$$
\boxed{
[O\text{-}229\text{-}3B.1f\text{-}c.1\text{-target-complex-architecture}]
\quad \checkmark[K/M].
}
$$

**Umfang:** Typ A wird als minimale Endarchitektur des Wres-relativen Rohkopplungszweigs festgelegt. Typ B bleibt als optionaler vorgelagerter Kettenlift offen.

---

## 6. Tautologischer Cone-No-Go

Betrachte die auf je einen Grad konzentrierten Komplexe:

$$
C_{p,\mathrm{lift}}^r = H_{a^{\mathrm{raw}},p},
\qquad
C_{p,\mathrm{tar}}^r = Y_p,
$$

mit

$$
d_{\mathrm{lift}} = 0, \qquad d_{\mathrm{tar}} = 0,
$$

und der Kettenabbildung $F^r = U_p$.

Da $U_p$ unitär ist, ist $F^\bullet$ ein **Kettenisomorphismus**. Sein Mapping Cone

$$
\operatorname{Cone}(F^\bullet)
$$

ist daher **azyklisch** und sogar kontrahierbar.

Diese Konstruktion erzeugt:
- **keine** neue Kohomologieklasse (NT2 aus NEU-243 verletzt),
- **keine** nichttriviale Transgression $\tau_p$ (NT3 verletzt),
- **keine** Randdatenausgabe $b_p, \beta_p, \Lambda_p$.

$$
\boxed{
[O\text{-}229\text{-}3B.1f\text{-}c.1c\text{-tautological-quotient-range-cone}]
\quad \checkmark[M]_{\mathrm{neg}}.
}
$$

**Umfang:** Ausgeschlossen ist nur der auf einen Grad konzentrierte Nulldifferential-Kandidat mit der kanonischen quotient-range-Isometrie $U_p$. Nicht ausgeschlossen sind Komplexe mit zusätzlichen Graden, intrinsischen nichtverschwindenden Differentialen oder weiteren nichttautologischen Komponenten.

---

## 7. Konsequenz für [c.2]

Der Quellkomplex darf **nicht** lediglich aus $H_{a^{\mathrm{raw}},p}$ in einem einzigen Grad mit Nulldifferential bestehen.

Für
$$
[O\text{-}229\text{-}3B.1f\text{-}c.2\text{-intrinsic-lift-complex}]
$$
müssen daher **zusätzliche Gradstücke** und ein **intrinsisches nichtverschwindendes Differential** konstruiert werden.

Die neue Struktur muss mindestens eine Information tragen, die **nicht** bereits in der tautologischen Identifikation

$$
H_{a^{\mathrm{raw}},p} \cong Y_p
$$

enthalten ist. Ein bloßer Komplex auf dem Formquotienten genügt nicht, weil die kanonische Abbildung zum Bildraum dort bereits eine skalierte unitäre Identifikation ist.

Der eigentliche Forschungsengpass ist damit:

$$
\boxed{
[c.2]:
\text{Woher kommt ein zusätzlicher Grad und ein intrinsisches,
nichtverschwindendes } d_{\mathrm{lift}}?
}
$$

---

## 8. Gesamtstatus

| Teilknoten | Status |
|------------|--------|
| c.1a (Positivität erzwingt Quotient) | \(\checkmark[M]\) |
| c.1b (kanonische Range-Identifikation) | \(\checkmark[M]\) |
| c.1c (tautologischer Cone) | \(\checkmark[M]_{\mathrm{neg}}\) |
| **c.1 gesamt** | \(\checkmark[K/M]\) |
| c.2 (intrinsischer Quellkomplex) | \(?[O]_{\mathrm{offen}}\) |
| c.3 (Kettenabbildungserweiterung) | \(?[O]_{\mathrm{offen}}\) |
| c.4 (Randdatenausgabe) | \(?[O]_{\mathrm{offen}}\) |
| b.2 (Mapping Cone) | \(?[O]_{\mathrm{blockiert}}\) |
| b.3 | \(?[O]_{\mathrm{blockiert}}\) |
