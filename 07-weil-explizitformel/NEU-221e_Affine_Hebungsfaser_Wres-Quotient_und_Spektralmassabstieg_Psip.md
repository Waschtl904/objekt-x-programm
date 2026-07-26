# NEU-221e — Affine Hebungsfaser, Wres-Quotient und Spektralmaßabstieg des relativen Kopplungsvektors

**Katalog-ID:** NEU-221e
**Knoten:** `[O-221-1c1a-lift-descent-or-spectral-measure-invariance]`
**Vorgänger:** NEU-221d (Commit dbc3506) — Direktextraktion NEU-46, Sperren [O-221-1c1a–d]
**Stand:** 26. Juli 2026
**Typ:** Typaudit mit exaktem Kriterium — *keine Entscheidung des Abstiegs*

---

## 0. Auditurteil

NEU-41 definiert nach Wahl einer Fourier-geladenen Hebung einen Kopplungsvektor. NEU-46
verwendet den daraus entstehenden relativen Vektor als **zyklischen Vektor** einer
Weyl-Funktion. Damit ist die Hebungsfrage **nicht** durch Normgleichheit entschieden:
Verschieden gewählte, gleich normierte Vektoren können verschiedene
Resolventenmatrixstellen, verschiedene Spektralmaße und verschiedene inverse Momente
besitzen.

Im positiven selbstadjungierten Hilbertraumfall bestimmt die Weyl-Funktion das zyklische
Spektralmaß eindeutig. NEU-46 weist im **indefiniten** $\mathrm{Wres}$-Fall jedoch nur ein
signiertes beziehungsweise Krein-artiges Weyl-Funktional aus. Die Eindeutigkeitsaussage ist
dort nicht ohne Weiteres verfügbar.

Der Quellenabgleich schließt den Quotientabstieg weder positiv noch negativ. Vor dem
eigentlichen Test müssen drei Ebenen getrennt werden:

1. die **algebraische affine Liftfaser**,
2. die **exakt zulässige normierte Liftmenge**,
3. die **Wres-Quotientbildung im relativen Zielraum**.

Revidierter Status:

$$
\boxed{\ [O\text{-}221\text{-}1c1a] \quad \checkmark[M]_{\mathrm{part}}.\ }
$$

Bewiesen ist das exakte Abstiegs- und Invarianzkriterium. Offen bleibt seine Verifikation
auf der noch nicht vollständig formalisierten Menge exakt zulässiger Liftänderungen.

---

## 1. Algebraische Liftfaser

Sei $B_{3,p}^{\mathrm{lift}} \subseteq B_3$ der algebraische $p$-Liftbereich und

$$
\pi_{\mathrm{prim},p} : B_{3,p}^{\mathrm{lift}} \longrightarrow \mathbb C\,\varepsilon_p
$$

die primitive Projektion. Fixiere einen algebraischen Ausgangslift
$\widehat\varepsilon_p^{\,0} \in \pi_{\mathrm{prim},p}^{-1}(\varepsilon_p)$ und setze

$$
K_p := \ker \pi_{\mathrm{prim},p}.
$$

Dann ist die vollständige algebraische Liftfaser exakt

$$
\boxed{\ \pi_{\mathrm{prim},p}^{-1}(\varepsilon_p) \;=\; \widehat\varepsilon_p^{\,0} + K_p.\ }
$$

Dies ist eine **affine** Faser über dem linearen Raum $K_p$.

> Sie ist **nicht** mit der Menge normierter zulässiger Fourier-Hebungen gleichzusetzen.

**Quelle:** NEU-157 rev.3 §157.B (`$K_p := \ker(\pi_{\mathrm{prim}})$`, „Die vollständige
Liftfaser lautet somit $\widehat\varepsilon_p^{\,0} + K_p$"). `✓[M]`

---

## 2. Exakt zulässige normierte Hebungen

Sei

$$
h_p(x,y) := \operatorname{Tr}_{\mathrm{Wres}}^{\mathrm{conn}}\bigl(x^{\#}y\bigr),
\qquad q_p(x) := h_p(x,x).
$$

Die Normierungsbedingung von NEU-41 §3 lautet

$$
h_p(\widehat\varepsilon_p, \widehat\varepsilon_p) = 1.
$$

Für $\widehat\varepsilon_p = \widehat\varepsilon_p^{\,0} + k$ mit $k \in K_p$ ist sie
äquivalent zu

$$
\boxed{\ 2\operatorname{Re} h_p\bigl(\widehat\varepsilon_p^{\,0}, k\bigr) + h_p(k,k) = 0.\ }
\tag{157.1}
$$

Diese Bedingung ist **quadratisch**. Ihre Lösungsmenge
$\mathcal Q_p(\widehat\varepsilon_p^{\,0})$ ist im Allgemeinen **kein komplexer
Vektorraum** — NEU-157 rev.3 §157.D bezeichnet sie ausdrücklich als Quadrik, nicht als
Einheitssphäre. `✓[M]`

Unter Einbeziehung aller explizit konstruierten linearen, affinen und nichtlinearen
Nebenbedingungen sei

$$
\widehat{\mathcal E}_p^{\mathrm{adm}} \;\subseteq\; \pi_{\mathrm{prim},p}^{-1}(\varepsilon_p)
$$

die Menge exakt zulässiger normierter Fourier-geladener Hebungen.

> Der vollständige Quellenbestand definiert diese Menge derzeit **nicht abschließend**.
> Insbesondere dürfen postulierte, aber nicht konstruierte Operatoren — etwa die
> $R_{p,j}$, deren Nichtkonstruiertheit NEU-165b festgestellt hat — nicht zur Definition
> verwendet werden. `?[O]`

### 2.1 Die zulässige Differenzmenge

$$
\boxed{\
\Delta_p^{\mathrm{adm}} := \bigl\{\, \widehat\varepsilon_p' - \widehat\varepsilon_p \;:\;
\widehat\varepsilon_p, \widehat\varepsilon_p' \in \widehat{\mathcal E}_p^{\mathrm{adm}} \,\bigr\}
\;\subseteq\; K_p.
\ }
$$

Es gilt $\Delta_p^{\mathrm{adm}} \subseteq K_p$, aber im Allgemeinen **weder**
$\Delta_p^{\mathrm{adm}} = K_p$ **noch** Linearität von $\Delta_p^{\mathrm{adm}}$.

### 2.2 Abgrenzung gegen $\mathcal A_p^{\mathrm{adm}}$ aus NEU-157

> **Querabgleich (editorisch, nicht Quellenaussage).** NEU-157 rev.3 führt in (157.2)
> bereits eine Menge exakt zulässiger **Liftänderungen relativ zu einem festen
> Ausgangslift**:
> $$\mathcal A_p^{\mathrm{adm}}(\widehat\varepsilon_p^{\,0}) = \bigl\{k \in K_p^{\mathrm{hom}} : k \in \mathcal Q_p(\widehat\varepsilon_p^{\,0}),\; F_{p,\alpha}(\widehat\varepsilon_p^{\,0}+k)=0\ \forall\alpha\bigr\}$$
> mit $\widehat{\mathcal E}_p^{\mathrm{adm}} = \widehat\varepsilon_p^{\,0} + \mathcal A_p^{\mathrm{adm}}(\widehat\varepsilon_p^{\,0})$.
>
> Daraus folgt
> $$\Delta_p^{\mathrm{adm}} = \mathcal A_p^{\mathrm{adm}} - \mathcal A_p^{\mathrm{adm}},$$
> also die **Differenzmenge**, nicht $\mathcal A_p^{\mathrm{adm}}$ selbst. Da
> $\mathcal A_p^{\mathrm{adm}}$ als Teilmenge einer Quadrik im Allgemeinen kein
> Vektorraum ist, ist die Differenzmenge im Allgemeinen **echt größer**:
> $$\mathcal A_p^{\mathrm{adm}} \subseteq \Delta_p^{\mathrm{adm}}, \qquad \text{Gleichheit nur bei } 0 \in \mathcal A_p^{\mathrm{adm}} \text{ und Abgeschlossenheit unter Differenzen.}$$
> Ein Abstiegstest auf $\mathcal A_p^{\mathrm{adm}}$ allein ist daher **nicht hinreichend**;
> der Test muss auf $\Delta_p^{\mathrm{adm}}$ laufen. Ebenso genügt der Tangentialraum
> $\mathrm{Tan}_{\widehat\varepsilon_p^{\,0}}\mathfrak L_p^{\mathrm{adm}}$ (157.4) nicht —
> NEU-157 §157.F hält selbst fest, dass ein Tangentialvektor „noch kein exakt zulässiger
> Liftwechsel" ist.

---

## 3. Relativer Rohzielraum und Wres-Quotient

### 3.1 Warum der Zielraum relativ sein muss

NEU-41 arbeitet mit dem kollabierten Jacobi-Zielraum: dort steht
$\Psi_p := \Pi_{J,N}\psi_p \in \mathcal H_{J,N}$ (NEU-41 §164). NEU-43/44 korrigieren diese
Architektur — verschiedene Primkanten können nach dem Kollaps im selben Sektor $V_{pq}$
landen. Der sichere Feshbach-Operator und damit der in NEU-46 verwendete Weyl-Sektor leben
deshalb im **kantenmarkierten** Raum

$$
\mathcal H_{\mathrm{rel},N} = \bigoplus_{p\le N}\bigoplus_m \mathcal H_{m\xrightarrow{\;p\;}pm}.
$$

Der Pullback der ursprünglichen $\mathrm{Wres}$-Paarung ist **nicht automatisch
primkantendiagonal**; die relative kantendiagonale Paarung ist eine zusätzliche
Konstruktion, deren Intrinsizität offen bleibt (NEU-44.X3, `❓[O]`).

Für den Audit gegen NEU-46 ist daher **nicht** $T_p : B_{3,p}^{\mathrm{lift}} \to \mathcal H_{J,N}$
primär, sondern

$$
\boxed{\ T_p^{\mathrm{rel}} : B_{3,p}^{\mathrm{lift}} \longrightarrow \mathcal H_{\mathrm{rel},p,N}.\ }
$$

Erst danach darf gegebenenfalls eine Kollapsabbildung
$\kappa : \mathcal H_{\mathrm{rel},N} \to \mathcal H_{J,N}$ untersucht werden.

### 3.2 Rohzielraum, Radikal, Quotient

Sei

$$
\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}} := \operatorname{span}\Bigl\{\, E^{\mathrm{rel}}_{r;\,m\xrightarrow{p}pm} \,\Bigr\}
$$

der algebraische relative Rohzielraum **vor** Wres-Quotient und Vervollständigung, und sei
$\langle\cdot,\cdot\rangle_{\mathrm{Wres,rel}}$ die verwendete relative sesquilineare Form.
Ihr **Radikal** ist

$$
\boxed{\
\mathcal N_{\mathrm{Wres,rel}} := \bigl\{\, v \in \mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}} \;:\;
\langle v, w\rangle_{\mathrm{Wres,rel}} = 0 \ \ \forall\, w \in \mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}} \,\bigr\}.
\ }
$$

> **Typwarnung.** Bei einer **indefiniten** Form ist das Radikal **nicht** dasselbe wie die
> Menge der isotropen Vektoren $\{v : \langle v,v\rangle_{\mathrm{Wres,rel}} = 0\}$. Die
> beiden dürfen nicht identifiziert werden.

Setze

$$
Q_{\mathrm{Wres,rel}} : \mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}} \longrightarrow
\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}} \big/ \mathcal N_{\mathrm{Wres,rel}},
$$

und nach positiver Hilbertrealisierung beziehungsweise geeigneter Vervollständigung
$\mathcal H_{\mathrm{rel},p,N}$.

---

## 4. Rohkopplung und quotientierte Kopplung

Bei festem $L_3^\circ$ ist die Rohkopplung in der ersten Variablen **linear**:

$$
\boxed{\ \widetilde T_p^{\mathrm{raw}}(x) := \widetilde\omega_2^{\mathrm{rel}}\bigl(x, L_3^\circ\bigr)
\in \mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}.\ }
$$

Mit der Fourierregel $\widetilde\omega_2(e_uV_p, e_sV_m) = -u\,s\,\log(p)\, e_{u+ps}V_{pm}$
gilt auf Basiselementen

$$
\widetilde T_p^{\mathrm{raw}}(e_uV_p) = -\sum_{s,m} \ell_{s,m}\, u\, s\, \log p \;
E^{\mathrm{rel}}_{u+ps;\,m\xrightarrow{p}pm},
$$

insbesondere

$$
\boxed{\ \widetilde T_p^{\mathrm{raw}}(e_0 V_p) = 0. \ }
$$

Die quotientierte relative Kopplung ist

$$
\boxed{\ T_p^{\mathrm{rel}} := Q_{\mathrm{Wres,rel}} \circ \widetilde T_p^{\mathrm{raw}}. \ }
$$

Für eine fest gewählte Hebung definiert sie
$\Psi_p[\widehat\varepsilon_p] := T_p^{\mathrm{rel}}(\widehat\varepsilon_p) \in \mathcal H_{\mathrm{rel},p,N}$
und daraus den Kopplungsoperator

$$
C_p[\widehat\varepsilon_p] : \mathbb C\,\varepsilon_p \longrightarrow \mathcal H_{\mathrm{rel},p,N},
\qquad C_p[\widehat\varepsilon_p](\lambda\varepsilon_p) = \lambda\,\Psi_p[\widehat\varepsilon_p].
$$

> **Typwarnung.** $C_p[\widehat\varepsilon_p]$ hat einen **eindimensionalen**
> Definitionsraum und ist deshalb trivialerweise vom Rang höchstens eins und beschränkt.
> Daraus folgt **nichts** über Rang oder Beschränktheit der Rohabbildung
> $\widetilde T_p^{\mathrm{raw}}$ beziehungsweise $T_p^{\mathrm{rel}}$ auf dem gesamten
> Liftbereich $B_{3,p}^{\mathrm{lift}}$. Dieser kann viele Fouriermoden enthalten, deren
> Bilder in verschiedene Zielmoden $E^{\mathrm{rel}}_{u+ps;\,m\to pm}$ laufen. Beschränktheit
> von $T_p^{\mathrm{rel}}$ ist nur bei expliziter endlicher Trunkierung automatisch;
> global ist sie quellseitig **nicht bewiesen**. `❓[O]`

---

## 5. Exaktes Quotientabstiegskriterium

Der relative Kopplungsvektor steigt genau dann von der Hebungsfaser auf den primitiven
Kanal ab, wenn

$$
\Psi_p[\widehat\varepsilon_p'] = \Psi_p[\widehat\varepsilon_p]
\qquad\text{für alle } \widehat\varepsilon_p, \widehat\varepsilon_p' \in \widehat{\mathcal E}_p^{\mathrm{adm}}.
$$

Wegen der Linearität der Rohkopplung ist dies äquivalent zu

$$
\boxed{\ \widetilde T_p^{\mathrm{raw}}\bigl(\Delta_p^{\mathrm{adm}}\bigr) \subseteq \mathcal N_{\mathrm{Wres,rel}}. \ }
\tag{221e.1}
$$

Die stärkere Bedingung

$$
\widetilde T_p^{\mathrm{raw}}(K_p) \subseteq \mathcal N_{\mathrm{Wres,rel}}
\tag{221e.2}
$$

ist **hinreichend**. Sie ist nur dann notwendig, wenn jede algebraische Kernrichtung als
Differenz exakt zulässiger Hebungen realisiert wird — das ist derzeit gerade **nicht**
bewiesen.

Falls der Abstieg gilt, existiert eine kanonische Abbildung

$$
\overline T_p : \mathbb C\,\varepsilon_p \longrightarrow \mathcal H_{\mathrm{rel},p,N},
\qquad \overline T_p(\varepsilon_p) = \Psi_p,
$$

unabhängig von der Hebungswahl.

> Der Quellenbestand beweist die Inklusion (221e.1) derzeit **weder** für
> $\Delta_p^{\mathrm{adm}}$ **noch** für $K_p$.

---

## 6. Normierung und Stabilisator

Die Gleichung $h_p(\widehat\varepsilon_p,\widehat\varepsilon_p) = 1$ definiert nur eine
**normierte Niveaumenge** innerhalb der affinen Liftfaser. Sie beweist **nicht**, dass zwei
normierte Hebungen nur durch eine Phase zusammenhängen.

Der Stabilisator der Liftmenge kann enthalten:

- Phasen, soweit mit der primitiven Projektion vereinbar;
- additive Wres-radikale Richtungen;
- nichttriviale Fourier-Rotationen;
- Symmetrien der Nebenbedingungen;
- Änderungen, die zwar die Eingangsform, nicht aber die Rohkopplung erhalten.

Ohne explizite Wres-Grammatrix und ohne vollständige Definition der zulässigen Liftmenge
ist der Liftstabilisator **offen**. `❓[O]`

Dagegen gilt im **positiven Hilbertraumfall** für nichtverschwindende Bildvektoren:

$$
C_p C_p^{*} = C_p' C_p'^{*} \quad\Longrightarrow\quad \Psi_p' = e^{i\theta}\,\Psi_p .
$$

Der Stabilisator des nichtverschwindenden Rang-eins-Bildkanals ist dann genau die
Phasengruppe $U(1)$. `✓[M]`, bedingt durch Nichtnullheit und Kanalgleichheit.

> **Notationshinweis.** NEU-41 §7 formuliert die Bedingung mit dem Wres-Adjungierten:
> $C_pC_p^{\#} = C_p'C_p'^{\#}$. Das ist eine **stärkere** Forderung als bloße
> Normgleichheit, und NEU-41 lässt sie ausdrücklich **offen**. Der Übergang von $\#$ zu
> $*$ setzt die positive Hilbertrealisierung voraus; im indefiniten Fall ist die
> Phasenschlussfolgerung nicht verfügbar.

---

## 7. Spektralmaßinvarianz

Sei $D_N^{\mathrm{rel}} = (D_N^{\mathrm{rel}})^{*}$ auf dem positiven relativen
Hilbertraum, und sei $\mu_{\widehat\varepsilon_p}^{D_N^{\mathrm{rel}}}$ das zyklische
Spektralmaß von $\Psi_p[\widehat\varepsilon_p]$.

Hebungsunabhängigkeit des Spektralmaßes ist äquivalent dazu, dass

$$
\bigl\langle \Psi_p[\widehat\varepsilon_p],\, f\bigl(D_N^{\mathrm{rel}}\bigr)\, \Psi_p[\widehat\varepsilon_p] \bigr\rangle
$$

für **alle** beschränkten Borelfunktionen $f$ unabhängig von $\widehat\varepsilon_p$ ist.

Als erster vollständiger Test genügt die Resolventenfamilie

$$
f_w(\lambda) = (\lambda - w)^{-1}, \quad w \notin \mathbb R,
\qquad\text{bzw. für den Stieltjeskandidaten}\qquad
f_w(\lambda) = (\lambda^2 - w)^{-1}.
$$

> **Kernpunkt.** Die bloße Norminvarianz entspricht nur dem Test $f \equiv 1$ und ist
> **nicht ausreichend**. Genau hier liegt der Unterschied zwischen NEU-41 (Normierung) und
> NEU-46 (zyklische Spektraldaten).

Die stärkere offene Bedingung

$$
C_p[\widehat\varepsilon_p]\,C_p[\widehat\varepsilon_p]^{*} = C_p[\widehat\varepsilon_p']\,C_p[\widehat\varepsilon_p']^{*}
$$

würde im positiven Hilbertraum die Phasenäquivalenz der Vektoren und damit die
**vollständige** Spektralmaßinvarianz implizieren. NEU-41 fordert eine solche
Rang-eins-Kanalinvarianz, beweist sie aber nicht. NEU-46 zeigt, warum ihr Fehlen die Weyl-
und Feshbach-Daten ambig macht. `❓[O]`

---

## 8. Nullkandidat

Für den ungeladenen algebraischen Ausgangslift gilt
$\widetilde T_p^{\mathrm{raw}}(e_0V_p) = 0$. Damit ist dieser **konkrete** Kandidat
ausgeschlossen:

$$
\boxed{\ e_0 V_p \quad \checkmark[M]_{\mathrm{neg}} \ }
$$

als nichttriviale Feshbach-Kopplungsquelle.

> **Umfang.** Daraus folgt **nicht**, dass der einzige kanonische Quotientabstieg null ist.
> Zu unterscheiden sind:
> 1. der algebraische Ausgangslift $e_0V_p$;
> 2. exakt zulässige Fourier-geladene normierte Hebungen;
> 3. mögliche kanonische Sektionen der affinen Liftfaser;
> 4. ein Abstieg des Rang-eins-Kanals oder nur des Spektralmaßes.

Ein negativer Abschluss des gesamten Feshbach-Momentkandidaten ist erst gerechtfertigt,
wenn bewiesen ist, dass $T_p^{\mathrm{rel}}(\widehat\varepsilon_p) = 0$ für **jede**
intrinsisch zulässige Hebung beziehungsweise jede intrinsische Sektion gilt — oder wenn
gezeigt ist, dass relevante freie Hebungswahl **verschiedene** Spektralmaße erzeugt.

---

## 9. Globaler Vektor

Im kantenmarkierten relativen Raum lautet die formale Bildung

$$
\mathcal H_{\mathrm{rel},N} = \bigoplus_{p\le N} \mathcal H_{\mathrm{rel},p,N},
\qquad
\Psi_N = \bigoplus_{p\le N} \Psi_p .
$$

Falls diese Summe als **orthogonale** Hilbertdirektsumme mit primkantendiagonaler relativer
Paarung konstruiert ist, gilt

$$
\boxed{\ \lVert \Psi_N \rVert^2 = \sum_{p\le N} \lVert \Psi_p \rVert^2. \ }
$$

Nach Kollaps in den gewöhnlichen Jacobi-Raum ist diese Orthogonalität **nicht automatisch**
erhalten — verschiedene Primkanten können im selben Zielsektor kollidieren (NEU-43/44).

> **Trennung zweier Fragen.** Die Vektordirektsumme entscheidet **nicht** über die globale
> Kopplung des Spektralmaßes. Besitzt $D_N^{\mathrm{rel}}$ Off-Diagonalblöcke zwischen
> Primsektoren, kann $\mu_{\Psi_N}^{D_N^{\mathrm{rel}}}$ global gekoppelt sein. Nur wenn
> **sowohl** der Raum **als auch** der Operator orthogonal direkt zerfallen, folgt
> $$M_N(w) = \sum_{p\le N} M_{p,N}(w).$$

Dies ist genau die Frage von `[O-221-1c1d]` und darf nicht mit der Vektornormierung
`[O-221-1c1a]` vermischt werden.

---

## 10. Revidierter Status

| Aussage | Status |
|---|---|
| algebraische Liftfaser $\widehat\varepsilon_p^{\,0} + K_p$ | `✓[M]` |
| $K_p = \ker\pi_{\mathrm{prim},p}$ | `✓[M]` |
| Wres-Normierung ist quadratisch, $\mathcal Q_p$ kein Vektorraum | `✓[M]` |
| exakt zulässige Liftmenge $\widehat{\mathcal E}_p^{\mathrm{adm}}$ vollständig formalisiert | `?[O]` — NEU-157-R1–R3 unvollständig |
| relative Roh-/Quotientkopplung exakt getrennt typisiert | `✓[K]_part` als notwendige Typisierung |
| $\Delta_p^{\mathrm{adm}} = \mathcal A_p^{\mathrm{adm}} - \mathcal A_p^{\mathrm{adm}}$, im Allgemeinen echt größer als $\mathcal A_p^{\mathrm{adm}}$ | `✓[M]` (editorischer Querabgleich §2.2) |
| Quotientabstieg auf $\Delta_p^{\mathrm{adm}}$ | **gesperrt**, solange $\Delta_p^{\mathrm{adm}}$ nicht bestimmt ist |
| stärkere Inklusion auf ganz $K_p$ | `?[O]`, hinreichend, nicht notwendigerweise äquivalent |
| Liftstabilisator | `?[O]` |
| Rang-eins-Bildstabilisator $U(1)$ | `✓[M]`, bedingt durch $\Psi_p\neq 0$ und $C_pC_p^{*} = C_p'C_p'^{*}$ |
| Beschränktheit/Rang von $T_p^{\mathrm{rel}}$ auf ganz $B_{3,p}^{\mathrm{lift}}$ | `?[O]` |
| Spektralmaßinvarianz | `?[O]` |
| intrinsische Sektion | `?[O]` |
| ungeladener Rohkandidat $e_0V_p$ | `✓[M]_neg`, da Rohkopplung null |
| Schluss „einziger kanonischer Abstieg ist null" | **nicht bewiesen** |
| globaler Vektor im relativen Graphraum | `✓[M]_part` nur im kantenmarkierten relativen Hilbertraum |
| **Gesamtstatus `[O-221-1c1a]`** | **`✓[M]_part`** |

---

## 11. Kleinster nächster atomarer Knoten

$$
\boxed{\ [O\text{-}221\text{-}1c1a0\text{-admissible-difference-locus-and-raw-relative-coupling}] \ }
$$

Genau drei Aufgaben:

1. **Bedingungen klassifizieren.** Alle Bedingungen an eine Hebung als homogen-linear,
   affin, quadratisch oder nichtlinear einordnen und $\widehat{\mathcal E}_p^{\mathrm{adm}}$
   vollständig definieren. Postulierte, nicht konstruierte Operatoren sind unzulässig.
2. **Zielraum fixieren.** Den algebraischen relativen Rohzielraum
   $\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}$, sein Wres-Radikal
   $\mathcal N_{\mathrm{Wres,rel}}$ und die Quotientenabbildung $Q_{\mathrm{Wres,rel}}$
   explizit hinschreiben.
3. **Test rechnen.** Für Erzeuger beziehungsweise explizite Kurven in
   $\Delta_p^{\mathrm{adm}}$ prüfen, ob
   $\widetilde T_p^{\mathrm{raw}}(\Delta_p^{\mathrm{adm}}) \subseteq \mathcal N_{\mathrm{Wres,rel}}$.

Erst danach ist eine Entscheidung zwischen den Fällen A–E möglich.

---

## Abhängigkeiten

| Referenz | Inhalt |
|---|---|
| NEU-221d | Sperren `[O-221-1c1a–d]`, Nullmodusaudit |
| NEU-221c | Zielnormalform $M_\Xi(w) = \langle\Omega_X,(I-wJ_X)^{-1}\Omega_X\rangle$ |
| NEU-46 | Relative Weyl-Funktionen $M_p(z)$, zyklischer Vektor, Feshbach-Sektor |
| NEU-41 | Kopplungsoperator $C_p$, Wres-Normierung, $C_pC_p^{\#}=C_p'C_p'^{\#}$ (offen) |
| NEU-43/44 | Kantenmarkierung, Kollapsproblem, relative kantendiagonale Paarung |
| NEU-157 rev.3 | Affine Liftfaser, quadratische Normierungsbedingung, $\mathcal A_p^{\mathrm{adm}}$ (157.2) |
| NEU-165b | $R_{p,j}$ nirgends explizit konstruiert |
| NEU-42 §10 | Fourierregel $\widetilde\omega_2(e_uV_p, e_sV_m)$ |
