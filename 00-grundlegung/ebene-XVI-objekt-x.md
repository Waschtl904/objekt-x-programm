# Ebene XVI — Objekt X: Kanonisches Kontrollblatt

**Revision 2 · Stand: 26. Juli 2026 (NEU-221e) · ersetzt Revision 1 (Stand NEU-114, 1. Juli 2026)**

---

## Zweck und Gebrauchsanweisung

Dieses Blatt ist **kein Forschungsblatt**, sondern eine verbindliche Karte. Es sammelt an
einem Ort alle Bedingungen, gegen die ein Kandidat für Objekt X geprüft werden kann, und
hält fest, welche Bedingung auf welcher logischen Ebene und in welchem Konstruktionspfad
gilt.

**Pflegeregel.** Jedes neue NEU-Dokument, das eine Bedingung an X, an eine seiner
Projektionen oder an einen Realisierungskandidaten begründet oder ausschließt, wird hier
eingetragen — im selben Arbeitsgang, nicht nachträglich. Ein Eintrag ohne Gültigkeitsetikett
und ohne Pfadzuordnung ist unvollständig.

### Die drei logischen Ebenen

Die Revision 1 vermischte Aussagen über $X$ mit Aussagen über seine Realisierungen. Das ist
korrigiert. Es gelten strikt getrennt:

$$
\boxed{\text{intrinsische Axiome von } X}
\qquad
\boxed{\text{Brückenaxiome für } \Pi_\gamma(X),\; W_\xi}
\qquad
\boxed{\text{Realisierungsbedingungen für } H_X}
$$

- **XVI-A** enthält ausschließlich die erste Ebene.
- **XVI-B** die zweite.
- **XVI-C** die dritte — insbesondere gehören HP-1–HP-7 hierher und **nicht** zu den Axiomen von $X$.
- **XVI-D** enthält Bedingungen, die nur innerhalb eines bestimmten Konstruktionspfades zwingend sind.
- **XVI-E** ist das Negativregister.
- **XVI-F** führt die Rückbindungstests.

### Gültigkeitsetiketten

Jede Bedingung und jedes No-Go trägt genau eines:

| Etikett | Bedeutung |
|---|---|
| `global` | betrifft Objekt $X$ selbst, unabhängig vom Konstruktionsweg |
| `bridge` | betrifft die Vermittlungsarchitektur $\Pi_\gamma$, $W_\xi$, das Verhältnis von $X$ zu seinen Projektionen |
| `spectral` | betrifft die spektrale Realisierung $H_X$, Spurtyp, Determinantenebene, Schattenklasse |
| `Feshbach` | gilt nur im Primkanten-/Feshbach-/Selbstenergiepfad |
| `HH` | gilt nur, solange die kohomologische Schicht Bestandteil der Konstruktion ist |
| `route-conditional` | gilt nur unter zusätzlichen Modellannahmen eines konkreten Kandidaten |

### Konstruktionspfade

`P0` pfadunabhängig · `P1` Feshbach-/Primkantenpfad · `P2` Selbstenergie-/Mangoldtpfad ·
`P3` HH-/zyklische Kohomologie · `P4` singuläre Potentialroute · `P5` Vergleichsoperator-/Konfinementpfad

### Sperrregel

> Ein No-Go gegen einen konkreten Kandidaten wird **nicht** zu einem Axiom über $X$
> hochgestuft. Wo eine Quelle nur einen bestimmten Mechanismus ausschließt — einen
> Vergleichsoperator, eine skalare Normierung, eine Liftwahl — sagt das Feld *Umfang*
> ausdrücklich, was **nicht** ausgeschlossen ist.

---

## XVI-A — Identität von Objekt X

Hier stehen ausschließlich Aussagen, die $X$ selbst betreffen.

### A.0 — Definitorisches Fünfschicht-Profil

$$
X = \bigl(A_{2D}^{r},\; [\tilde\omega_2],\; [L_3],\; \mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}},\; m \xrightarrow{\;p\;} pm \bigr)
$$

| Schicht | Typ | Rolle | Status |
|---|---|---|---|
| $A_{2D}^r$ | nuklear-bornologische Trägeralgebra, Beurling-/log-RD-Topologie | Träger | `⚠[M]` |
| $[\tilde\omega_2]$ | primäre Hochschild-2-Klasse | Deformationsrichtung | `⚠[M]`, Nichttrivialität nur Hypothese |
| $[L_3]$ | sekundäre Hochschild-4-Klasse | Obstruktion | `❓[O]`, $[L_3]\neq 0$ unentschieden |
| $\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}$ | Spurform (Wodzicki-Residuum, kantendiagonal erweitert) | Auswertung | `✓[M]` als notwendig |
| $m\to pm$ | relative Primkanten $\mathcal H_{\mathrm{rel},N}=\bigoplus_{p\le N}\bigoplus_m \mathcal H_{m\to pm}$ | Arithmetik | `✓[M]` strukturell notwendig, NEU-44 |

### A.1 — Abgrenzungssatz (Vierschichtensatz) `global` `✓[M]`

$$
X_{\mathrm{skel}} \;\neq\; X \;\neq\; X^{\mathrm{val}} \;\neq\; W_\xi^{\mathrm{norm}}
\tag{116.0.V}
$$

mit den Übergängen $X_{\mathrm{skel}} \xrightarrow{\iota_{\mathrm{skel}}} X \xrightarrow{\iota_{\mathrm{val}}} X^{\mathrm{val}} = (X, T_{\mathrm{rel}}) \xrightarrow{\rho^{\mathrm{val}}} W_\xi^{\mathrm{norm}}$.

$X$ ist echt mehr als das nackte Divisibilitäts-/Kantenskelett und echt weniger als die
mit dem logarithmischen Cocycle angereicherte Struktur. **Quelle:** NEU-116.

### A.2 — Kategoriale Nichtidentität mit der Projektion `global` `✓[M]`

$$
X \;\neq\; m_{\mathrm{arith}}, \qquad m_{\mathrm{arith}} = \Pi_\gamma(X).
$$

Die Gleichsetzung ist **kategorial falsch**, nicht bloß ungenau. $X$ ist strukturell
höherstufig als jede einzelne seiner Projektionen. **Quelle:** NEU-114/115.

### A.3 — Kategorialer Träger `global` `⚠[M]`

$X$ über $A_{\mathrm{BC}}^{\infty}$, bornologisch-nuklear, spektralinvariant, log-RD-Topologie.
Spektralinvarianz der Einbettung $A_{2D}^r \hookrightarrow A_{\mathrm{BC}}^{C^*}$ hängt an
OP-1.6f.4b (externe Literaturroute, eingefroren). **Quelle:** NEU-10, NEU-12; A5 der Minimalaxiome.

### A.4 — Frobenius- und Zeitentwicklungskompatibilität `global` `✓[M]`

$\sigma_t$ und die Frobenius-/Skalenaktionen wirken als kommutierende Automorphismen;
$\mathbb Q_+^\times$-Wirkung mit BC-Kovarianz. **Quelle:** NEU-14; A2 der Minimalaxiome.

### A.5 — Kohomologische Vollständigkeit `global` `✓[M]`

$$HH^2(X) \supseteq E_\infty^{2,0} + E_\infty^{1,1} + E_\infty^{0,2}.$$

**Quelle:** NEU-11, NEU-13.

### A.6 — Spurform ist notwendig, nicht optional `global` `✓[M]`

$\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}$ ist Bestandteil von $X$, keine nachträgliche
Zusatzwahl. **Quelle:** NEU-19/20.

### A.7 — Relative Primkanten sind strukturell notwendig `global` `✓[M]`

Die fünfte Schicht ist nicht entbehrlich; ohne sie ist die kantendiagonale Hebung nicht
formulierbar. **Quelle:** NEU-44.

**Einschränkung (ehrlich zu führen):** Die kantendiagonale Hebung $\mathrm{Wres}_{\mathrm{rel}}$
wurde als Variante B **definiert**, nicht aus $\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}$
hergeleitet. NEU-43 Satz 43.3 zeigt, dass $T_{\mathrm{rel}}$ auf dem kollabierten Raum ohne
Kantenmarkierung nicht wohldefiniert ist, und $\kappa^*\mathrm{Wres}$ ist **nicht**
kantendiagonal. Die Intrinsizität ist offen: `❓[O]` NEU-44.X3.

### A.8 — Anti-Fitting-Bedingung `global` — methodologisch

> Jede Normierung, Gewichtung oder Skalenwahl in $X$ muss **intrinsisch aus der
> Operatorstruktur** folgen. Anpassung an Zetadaten — Nullstellenlagen, bekannte
> Konstanten, Zielasymptotiken — ist unzulässig.

Dies ist keine bewiesene Eigenschaft, sondern eine Konstruktionsdisziplin. Sie ist die
verallgemeinerte Form von HP-7 (XVI-C) und der Grund, warum der gesamte 220s–w-Strang als
`?[O], RH-stark` geführt wird. Motiviert durch NEU-78, 82, 83, 123.H, 220t.

### A.9 — Resonanzkonvergenz `global` `❓[O]` — unausgeführt

X.5 der Revision 1. In den Quellen bis heute **nicht ausgeführt**, nur benannt. Bleibt als
offene Identitätsfrage stehen.

### A.10 — Was X nicht ist

Zur Abgrenzung, unverändert aus den Minimalaxiomen:

- $X$ ist nicht die Zetafunktion.
- $X$ ist nicht der Hilbert–Pólya-Operator. $H_X$ ist eine **Realisierung** von $X$, siehe XVI-C.
- $X$ ist nicht die BC-C\*-Algebra $A_{\mathrm{BC}}^{C^*}$.
- $X$ ist kein Punkt in einem Modulraum.

### A.11 — Verhältnis der beiden Axiomensysteme

Es existieren zwei Axiomatisierungen. Sie sind **nicht identisch** und werden ab dieser
Revision unterschiedlich geführt:

| System | Quelle | Rolle ab Revision 2 |
|---|---|---|
| A1–A7 | `objekt_x_minimalaxiome.md`, 17. Juni 2026, durchgehend `✗[H]` | **Leitbild.** Motivischer Fernhorizont (Dyson-Quasikristall und Connes-Adele als zwei Projektionen desselben Objekts). Nicht operativ, keine Prämisse in Beweisen. |
| X.1–X.10 / XVI-A | Ebene XVI | **Operativ.** Verbindlich für alle Katalogarbeit. |

Die Zuordnung: A1 → A.3, A2 → A.4, A3 → **XVI-C** (nicht XVI-A), A4 → ohne operatives
Gegenstück, A5 → A.3, A6 → A.5 plus XVI-D/P3, A7 → A.2.

Bemerkenswert: **A3 der Minimalaxiome, die spektrale Realisierungseigenschaft, ist nach der
Ebenentrennung kein Axiom von $X$ mehr**, sondern eine Realisierungsbedingung. Das ist die
inhaltlich wichtigste Konsequenz dieser Revision.

---

## XVI-B — Projektions- und Brückenarchitektur

### B.0 — Die Kette

$$
X \;\xrightarrow{\;\Pi_\gamma\;}\; m_{\mathrm{arith}} \;\longrightarrow\; Q_{\mathrm{Weil}} \;\longrightarrow\; \text{RH-Kanal}
$$

$$
X \;\longrightarrow\; W_\xi \quad\text{(lineares Interface)}, \qquad W_\xi \ast W_\xi \;\rightsquigarrow\; Q_{\mathrm{Weil}} \quad\text{(quadratisch)}
$$

### B.1 — Linear ist nicht quadratisch `bridge` `✓[M]`

Die Spurform $\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}$ ist **linear**, die Weil-Form
$Q_{\mathrm{Weil}}$ **quadratisch**. Eine direkte Identifikation ist kategorial ausgeschlossen.
Die Vermittlung muss über das lineare Interface $W_\xi$ auf $PW_t$ laufen, das erst durch
Paarung mit sich selbst zur Quadratform wird. **Quelle:** NEU-115.

### B.2 — Externalität des archimedischen Faktors `bridge` `✓[M]`

$$
\Theta_{1/2} \ \text{ist extern zu } X.
$$

Tests ST-3/ST-4 in NEU-116.C.15. Der Faktor entsteht als $e^{-sT_{\mathrm{rel}}}\big|_{s=1/2}$
im Übergang $X \to X^{\mathrm{val}}$, **nicht** innerhalb der Residuenstruktur von $X$.

> **Verbindliche Folgerung:** $\Theta_{1/2}$ darf nicht stillschweigend in die
> Residuenstruktur von $X$ eingebaut werden. Jede Konstruktion, die ihn dort verwendet,
> arbeitet in Wahrheit mit $X^{\mathrm{val}}$ und muss das deklarieren.

Restlücke: Intrinsizitätstest IT-2 `❓[O]`.

### B.3 — Der Spektralschatten ist nicht das Objekt `bridge` `✓[M]`

$m_{\mathrm{arith}}$ ist das Stieltjes-Nullstellenmaß $\sum_\gamma \delta_\gamma + \mu_{\Gamma,\mathrm{ren}}$
und damit der **Herglotz-Träger des Nullstellenanteils**, nicht $X$.
**Quelle:** NEU-112 Sätze 112.1–112.3, NEU-114 Satz 114.0.

### B.4 — Offene Brückenbedingungen

| Bedingung | Status | Knoten |
|---|---|---|
| $m_{\Omega,N} \to m_{\mathrm{arith}}$ (Jacobi-Realisierung) | `❓[O]` | — |
| Bombieri-Normalisierung exakt ($Q_{\mathrm{zeros}}$, $Q_\Gamma$, $Q_{\mathrm{prime}}$ auf $PW_t$) | `❓[O]` | NEU-113 |
| $m_{\mathrm{arith}}$ Herglotz $\iff$ RH | `⚠[M]` | NEU-63D |
| $Z_N^{\mathrm{completed}} \to C\cdot\xi$ | `❓[O]` | NEU-65 |
| Intrinsizitätstest IT-2 | `❓[O]` | NEU-116 |

---

## XVI-C — Spektrale Realisierungsprofile

Hier stehen Bedingungen an **Realisierungen** von $X$, nicht an $X$. Zwei Profile werden
strikt getrennt geführt, weil das Programm derzeit an beiden gleichzeitig arbeitet und sie
verschiedene Stärke haben.

### C.1 — HP-Profil (starke Realisierung) `spectral`

Ein Kandidat gilt nur dann als echter Hilbert–Pólya-Kandidat, wenn **alle** Punkte
**unabhängig von der Nullstellenliste** bewiesen sind. **Quelle:** NEU-220u.

| Kriterium | Forderung | Status |
|---|---|---|
| **HP-1** | $H_X = H_X^*$ | `⚠[M]` — NEU-53/55, unter Nelson-Bedingungen |
| **HP-2** | $H_X$ besitzt kompakten Resolventen | `❓[O]` — siehe C.3 |
| **HP-3** | $H_X^{-1} \in \mathcal S_2 \setminus \mathcal S_1$ | `❓[O]` |
| **HP-4** | $N_{H_X}(T) = \frac{T}{\pi}\log\frac{T}{2\pi} - \frac{T}{\pi} + O(\log T)$ | `❓[O]` |
| **HP-5** | $\det_2\bigl(I - zH_X^{-1}\bigr) = \Xi(z)/\Xi(0)$ | `❓[O]` |
| **HP-6** | Determinantenidentität folgt aus Spur-, Streu- oder relativer Determinantenformel | `❓[O]` |
| **HP-7** | Nullstellenlagen werden nirgendwo als Eingabedaten benutzt | **verletzt** im Strang NEU-220s–w, dort selbst als `?[O], RH-stark` geführt |

HP-7 ist die spektrale Ausprägung der Anti-Fitting-Bedingung A.8.

### C.2 — Stieltjes-Profil (schwache Realisierung) `spectral`

Zielnormalform des aktiven NEU-221-Strangs. **Quelle:** NEU-220w, NEU-221c/d.

$$
M_\Xi(w) = \bigl\langle \Omega_X,\, (I - wJ_X)^{-1}\Omega_X \bigr\rangle,
\qquad
\mu_k = \bigl\langle \Omega_X,\, J_X^{\,k}\,\Omega_X \bigr\rangle
$$

Anforderungen:

$$
\mathrm{Stieltjes\text{-}Profil} \;=\; \bigl\{\, D = D^*,\;\; \Psi,\;\; E_D(\{0\})\Psi = 0,\;\; \langle \Psi, D^{-2k-2}\Psi\rangle < \infty \ (k=0,1,2) \,\bigr\}
$$

| Anforderung | Status | Knoten |
|---|---|---|
| $D_N^{\mathrm{rel}} = (D_N^{\mathrm{rel}})^*$ | `✓[M]` über NEU-53/54 | — |
| $\Psi_p[\widehat\varepsilon_p]$ **nach Hebungswahl** typisiert; intrinsischer Vektor und intrinsische Norm $\lVert\Psi_N\rVert$ noch offen | `✓[M]_part` | `[O-221-1c1a]`, NEU-221e |
| **Hebungsunabhängigkeit des zyklischen Spektralmaßes** $\mu_{\Psi_p}^{D_N^{\mathrm{rel}}}$ | `❓[O]` | `[O-221-1c1a0]`, NEU-221e |
| $E_{D}(\{0\})\Psi_N = 0$ | `❓[O]` | `[O-221-1c1b]` |
| $\int\lvert\lambda\rvert^{-2k-2}\,d\mu_{\Psi_N} < \infty$, $k=0,1,2$ | `❓[O]` | `[O-221-1c1c]` |
| globale Kopplung in $D_{\mathrm{scatt},N}$ (parallel) | `❓[O]` | `[O-221-1c1d]` |

### C.2.1 — Normgleichheit genügt nicht `spectral` `✓[M]` — NEU-221e

Das Stieltjes-Profil verlangt einen **zyklischen** Vektor. Damit ist die Hebungsfrage nicht
durch Normierung entschieden:

> Verschieden gewählte, gleich normierte Hebungen können verschiedene
> Resolventenmatrixstellen, verschiedene Spektralmaße und verschiedene inverse Momente
> erzeugen.

Norminvarianz entspricht nur dem Test $f\equiv 1$. Erforderlich ist Invarianz von
$\langle\Psi_p[\widehat\varepsilon_p], f(D_N^{\mathrm{rel}})\Psi_p[\widehat\varepsilon_p]\rangle$
für **alle** beschränkten Borelfunktionen $f$.

Zwei Testfamilien leisten dabei **nicht** dasselbe. Die gewöhnliche Resolventenfamilie
$f_z(\lambda) = (\lambda-z)^{-1}$, $z\in\mathbb C\setminus\mathbb R$, bestimmt das
**vollständige** Spektralmaß $\mu_\Psi^{D}$. Die gerade Familie
$f_w(\lambda) = (\lambda^2-w)^{-1}$ bestimmt nur das Bildmaß unter $\lambda\mapsto\lambda^2$,
also $\mu_\Psi^{D^2}$ — das genügt für den Stieltjeskandidaten und seine **geraden**
inversen Momente, aber **nicht** für die vollständige Hebungsunabhängigkeit von
$\mu_\Psi^{D}$. NEU-46 formuliert die vollständige Weyl-Funktion mit der gewöhnlichen
Resolvente von $D_{\mathrm{rel},p}^{-}$.

### C.2.2 — Der indefinite Fall `spectral` — Typwarnung

Im positiven selbstadjungierten Hilbertraumfall bestimmt die Weyl-Funktion das zyklische
Spektralmaß eindeutig. NEU-46 weist im **indefiniten** $\mathrm{Wres}$-Fall jedoch nur ein
signiertes bzw. **Krein-artiges** Weyl-Funktional aus. Die Eindeutigkeitsaussage ist dort
nicht ohne Weiteres verfügbar.

Ebenso: NEU-41 formuliert die Kanalgleichheit mit dem Wres-Adjungierten,
$C_pC_p^{\#} = C_p'C_p'^{\#}$. Der Schluss auf Phasenäquivalenz
$\Psi_p' = e^{i\theta}\Psi_p$ — und damit auf volle Spektralmaßinvarianz — setzt die
**positive** Hilbertrealisierung voraus ($\#\to *$). Im indefiniten Fall ist er nicht
verfügbar.

> Verwandte Typwarnung: Bei indefiniter Form ist das **Radikal**
> $\mathcal N_{\mathrm{Wres,rel}} = \{v : \langle v,w\rangle = 0\ \forall w\}$ **nicht**
> die Menge der isotropen Vektoren $\{v : \langle v,v\rangle = 0\}$.

### C.3 — Nichtimplikation `spectral` — verbindlich

$$
\boxed{\ \text{Stieltjes-Profil} \;\not\Rightarrow\; \text{HP-Profil}.\ }
$$

**Begründung.** Endliche inverse Momente eines **zyklischen Vektors**,
$\langle\Psi, D^{-2k-2}\Psi\rangle<\infty$, sind eine Aussage über das Spektralmaß
$\mu_\Psi$ **relativ zu diesem Vektor**. Sie implizieren weder
$H_X^{-1}\in\mathcal S_2\setminus\mathcal S_1$ auf dem gesamten Hilbertraum (HP-3) noch
einen kompakten Resolventen (HP-2). Ein Erfolg von NEU-221 liefert ein
Stieltjes-Momentmodell — **keinen** Hilbert–Pólya-Operator.

Auch die Umkehrung ist nicht ohne Zusatz gültig: Aus dem HP-Profil folgt das
Stieltjes-Profil erst nach Wahl eines zyklischen Vektors mit den geforderten
Integrabilitätseigenschaften; deren Existenz ist eine eigene Frage.

**Konsequenz für die Buchführung:** Fortschritt an `[O-221-1c1a–d]` darf **nicht** als
Fortschritt an HP-2/HP-3 verbucht werden. Es sind zwei Konten.

### C.4 — Status von HP-2, präzise

Die in der Bestandsaufnahme formulierte Kollision war zu scharf gefasst und wird hier
korrigiert.

**Was NEU-56 beweist:** Über den dort gewählten Vergleichsoperator $L$ und eine **skalare**
Normierung $\gamma_N$ sind globaler Schur-Test und Konfinement unvereinbar. (N1) verlangt
$J^-\lesssim L$, (K) verlangt $L\lesssim |D_{\mathrm{rel}}|$; beide zusammen erzwingen
$L\simeq|D_{\mathrm{rel}}|$, was der erzwungenen Rate $\gamma_N = K/(N\log N)$ widerspricht.
Damit ist **Weg A über $L$** verschlossen: `✗[M]`, Satz 56.2, Punkt (V). Zwei getestete
Alternativen (separables Gewicht B1, $L$-Rekalibrierung B2) scheitern ebenfalls.

**Was NEU-56 nicht beweist:**

$$
H_X \text{ kann grundsätzlich keinen kompakten Resolventen besitzen.}
$$

Das ist **nicht** gezeigt. NEU-56 Punkt (VI) hält ausdrücklich offen: *Weg A bleibt offen
über einen anderen Vergleichsoperator*, `❓[O]`.

**Korrekte Formulierung des Knotenstatus:**

> NEU-56 (VI) ist der derzeit **einzige explizit registrierte** offene
> Vergleichsoperatorpfad zu HP-2. Ein anders konstruierter Operator könnte HP-2 erfüllen,
> ohne den NEU-56-Mechanismus überhaupt zu verwenden.

Die essentielle Selbstadjungiertheit bleibt von der Obstruktion unberührt (Satz 56.3,
`✓[M]`) — betroffen ist allein der Spektraltyp, nicht HP-1.

### C.5 — Weitere Realisierungsbedingungen `spectral`

| Bedingung | Inhalt | Quelle |
|---|---|---|
| Spurtyp | semifinite Spur erforderlich; gewöhnliche Hilbertraumspur unzureichend für $\Lambda_\Gamma$ | NEU-220e |
| Determinantentyp | Carleman-Determinante $\det_2$; gewöhnliche Fredholm-Determinante typologisch falsch | NEU-220u |
| Schattenklasse | $\mathcal S_2\setminus\mathcal S_1$ | NEU-220u |
| Metrik | positive invertierbare Metrik im Nullstellenpaar-Kreinraum existiert **genau dann, wenn RH** — jede Reparatur in diesem Modell ist tautologisch | NEU-220t |
| Hankel-Kriterium | $\mathrm{RH}\iff H_N^{(0)}\succeq 0 \wedge H_N^{(1)}\succeq 0\ \forall N$, mit $\mu_k = -\frac{k+1}{(2k+2)!}(\log\Xi)^{(2k+2)}(0)$ | NEU-220w `✓[M]` |

---

## XVI-D — Pfadspezifische Anforderungen

Eine Bedingung wird hier **nur dort** als zwingend geführt, wo das zugehörige No-Go sie
tatsächlich erzwingt.

### P1 — Feshbach-/Primkantenpfad

| # | Anforderung | Erzwungen durch | Status |
|---|---|---|---|
| P1.1 | Nichtverschwindender Off-Diagonal-Anteil $K^{\mathrm{off}} \neq 0$; falls vollständige Nichtzerlegbarkeit benötigt wird: der Primkopplungsgraph besitzt keinen nichttrivialen entkoppelten Block. **Nicht** gefordert ist $K_{pq}\neq 0$ für *jedes* Paar $p\neq q$ — das ginge über die No-Gos hinaus. Eine orthogonale primweise Direktzerlegung **sowohl** des zyklischen Vektors **als auch** des Operators erzeugt die nötige globale Kopplung nicht | NEU-50, 51, 207, 209 | Anforderung |
| P1.2 | Gradierte Normierung (Diagonalmatrix $D_N$) statt eines Skalars $\kappa_N$ | NEU-78, 82, 83, 123.H | Anforderung |
| P1.3 | Dichte Trägerstruktur $\kappa_N\asymp N$, nicht rein primzahlindiziert | NEU-82, 83 | Anforderung |
| P1.4 | **Primkantendiagonalität der quellseitig induzierten $\mathrm{Wres}$-Paarung.** In einer ausdrücklich orthogonalen Direktsumme ist $\langle\Psi_p,\Psi_q\rangle=0$ definitorisch und kein Satz; offen ist, ob die aus $\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}$ **induzierte** Paarung diese Diagonalität liefert. Der Pullback $\kappa^*\mathrm{Wres}$ tut es nicht (NEU-44.X3). Genau deshalb trennt NEU-43 den graph-erweiterten vom kollabierten Raum | — | `❓[O]` `[O-144-1]` |
| P1.5 | Nichtüberzählung: $\dim\ker(1-\mathcal K_\infty(\rho)) = m_\rho$ | — | `❓[O]` NEU-49 Satz 49.3, „Kern-Engpass" |
| P1.6 | Spurklassenkriterium für die volle gekoppelte Matrix, formuliert über die echte Spektralbasis von $D_{\mathrm{rel}}$ | — | `❓[O]` NEU-51/52; Eigenbasis existiert nicht explizit |
| P1.7 | Intrinsizität von $\mathrm{Wres}_{\mathrm{rel}}$ aus $\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}$ | — | `❓[O]` NEU-44.X3 (vgl. A.7) |
| P1.8 | **Hebungsabstieg:** $\widetilde T_p^{\mathrm{raw}}(\Delta_p^{\mathrm{adm}}) \subseteq \mathcal N_{\mathrm{Wres,rel}}$ mit $\Delta_p^{\mathrm{adm}} = \mathcal A_p^{\mathrm{adm}} - \mathcal A_p^{\mathrm{adm}}$. Bei $0\in\mathcal A_p^{\mathrm{adm}}$ ist dies wegen der Linearität von $\widetilde T_p^{\mathrm{raw}}$ **äquivalent** zum Test auf ganz $\mathcal A_p^{\mathrm{adm}}$. Ein Test nur auf dem Tangentialraum (157.4) ist **nicht** ausreichend | — | **gesperrt** NEU-221e, `[O-221-1c1a0]` |
| P1.9 | Beschränktheit und Rang von $T_p^{\mathrm{rel}}$ auf **ganz** $B_{3,p}^{\mathrm{lift}}$ — folgt **nicht** aus der Rang-eins-Eigenschaft von $C_p[\widehat\varepsilon_p]$ (eindimensionaler Definitionsraum) | — | `❓[O]` NEU-221e |
| P1.10 | Exakt zulässige Liftmenge $\widehat{\mathcal E}_p^{\mathrm{adm}}$ vollständig formalisieren; postulierte, nicht konstruierte Operatoren ($R_{p,j}$, NEU-165b) sind unzulässig | — | `❓[O]` NEU-157 rev.3 |
| P1.11 | Liftstabilisator bestimmen; Normierung allein erzwingt **keine** Phasenäquivalenz zweier zulässiger Hebungen | — | `❓[O]` NEU-221e §6 |

### P2 — Selbstenergie-/Mangoldtpfad

| # | Anforderung | Status |
|---|---|---|
| P2.1 | Unbeschränkte Operatoren und regulierte Spuren im Bereich $0<\Re\beta\le 1$; $R_p \gtrsim p/\log p$ ist unbeschränkt (die Quelle beweist keine untere Schranke mit Konstante exakt $1$) | `✓[M]` NEU-140/141/144 |
| P2.2 | Regularisierungsschema für $\operatorname{Tr}_{\mathrm{reg}}(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}})$ im kritischen Streifen | `❓[O]` `[O-144-3]` |
| P2.3 | Quantitative Schranken im Primschalen-Abel-Lemma; Kancellation „gefährdet nahe $\beta_0\approx s$" | `❓[O]` NEU-133 |

Die Kette trägt gesichert bis $\Re\beta>1$ und bricht exakt am kritischen Streifen.

### P3 — HH-/zyklische Kohomologie

Gilt nur, solange die kohomologische Schicht Bestandteil der Konstruktion bleiben soll.

| # | Anforderung | Erzwungen durch | Status |
|---|---|---|---|
| P3.1 | Keine Erzeugung über zentrale Cup-Faktoren — das Zentrum ist trivial | NEU-182, 183 | `✓[M]` |
| P3.2 | Keine globale Bimodul-Retraktion; $Z(A_{C^*}) = \mathbb C\cdot 1$ | NEU-215 | `✓[M]` |
| P3.3 | Getwistete, parazyklische oder $\sigma$-zyklische Koeffizientenkategorie — oder Orbitshift $\kappa\neq 0$ | NEU-219u | Anforderung |
| P3.4 | Konstruktion über direkte Kozykelkonstruktion (Barauflösung, Deformation) oder Quotientenmodell | NEU-182/183/215 | Anforderung |
| P3.5 | Erweiterbarkeit punktierter Gruppenkozykel auf $A_{\mathbb Q}^{\mathrm{alg}}$ | — | `❓[O]` `[O-188-0..3]` |

### P4 — Singuläre Potentialroute

| # | Anforderung | Erzwungen durch | Status |
|---|---|---|---|
| P4.1 | Echte Singularität bei 0: $H \in \mathrm{LC}(\hat{\mathbb Z}\setminus\{0\})\setminus\mathrm{LC}(\hat{\mathbb Z})$ — reguläre Potentiale sind im Kommutatorquotienten unsichtbar | NEU-196, 200 | `✓[M]` |
| P4.2 | Gemeinsame, punktkonzentrierte Singularität $\operatorname{Sing}\subseteq Z_g$ statt separierbarer Struktur auf Koordinatenhyperflächen | NEU-207, 209 | Anforderung |
| P4.3 | Randtermkontrolle | — | `❓[O]` `[O-207-5b]` |
| P4.4 | Charakterkernmenge $Z_g$ | — | `❓[O]` `[O-209-5/6]` |

> **Entscheidungsknoten — höchste Priorität bei serieller Bearbeitung.** P4 ist nach
> P3.1/P3.2/P3.4 der **letzte bekannte** Konstruktionsweg für die geladene Klasse.
> Scheitert P4.3/P4.4, hat die kohomologische Schicht von $X$ nach heutigem Wissensstand
> keinen bekannten Konstruktionsweg mehr. Dieser Knoten ist vor weiterer Investition in P3
> zu entscheiden.
>
> P4 ist der **schärfere** Entscheidungstest: Beide Ausgänge sind informativ — ein
> positiver hält die HH-Schicht am Leben, ein negativer schließt sie nach heutigem Wissen
> ab. P5 (→ HP-2) bleibt parallel der wichtigste **spektrale** Knoten, hat aber nicht
> denselben Ja/Nein-Charakter.

### P5 — Vergleichsoperator-/Konfinementpfad

| # | Anforderung | Status |
|---|---|---|
| P5.1 | Vergleichsoperator $\tilde L$ mit $\lVert J^- x\rVert \lesssim \lVert \tilde L x\rVert$ (Schur/Nelson) **und** $\lVert D_{\mathrm{rel}}x\rVert + \lVert x\rVert \ge c\lVert \tilde L x\rVert$ (Konfinement) | `❓[O]` NEU-56 (VI) |
| P5.2 | Singulärwertasymptotik $s_k(J^-\vert_{H^{\mathrm{eff}}_{\mathrm{rel}}})$: divergent oder akkumulierend? | `❓[O]` — Blatt NEU-57 existiert nicht |
| P5.3 | Schur-Test exakt statt heuristisch: $\sup_a\sum_b\lvert\Theta_{ba}\rvert/\ell(a)<\infty$ | `❓[O]` NEU-55 |
| P5.4 | Skalare Normierung $\gamma_N$ ist als Mechanismus verbraucht — P5.1 muss ohne sie auskommen | `✗[M]` NEU-56 Satz 56.2 |

P5 ist der einzige registrierte Zugang zu HP-2 (vgl. C.4), aber nicht der einzig denkbare.

---

## XVI-E — Negativregister

Die folgenden 22 Einträge (X.neg.8–X.neg.29) ergänzen das bestehende Negativregister (X.neg.1–7) um die im Forschungsjournal dokumentierten No-Go-Resultate aus den Katalogabschnitten 01 bis 07. Jeder Eintrag trägt genau ein **Gültigkeitsetikett**: `global` (betrifft X selbst, wegunabhängig), `bridge` (betrifft die Vermittlungsarchitektur zwischen X und seinen Projektionen/Interfaces), `spectral` (betrifft die spektrale Realisierung \(H_X\), Spurtyp, Determinantenebene oder Schattenklasse), `Feshbach` (nur im Primkanten-/Feshbach-/Selbstenergiepfad gültig), `HH` (nur solange die kohomologische Schicht Bestandteil der Konstruktion ist) oder `route-conditional` (nur unter zusätzlichen Modellannahmen eines konkreten Kandidaten). Das Feld „Betroffener Konstruktionspfad" referenziert die fünf Wege P1 (Feshbach-/Primkantenpfad), P2 (Selbstenergie-/Mangoldtpfad), P3 (HH-/zyklische Kohomologie), P4 (singuläre Potentialroute), P5 (Vergleichsoperator-/Konfinementpfad) sowie P0 für pfadunabhängige Aussagen. Die Sortierung folgt der Reichweite: zuerst wegunabhängige (`bridge`, `spectral`), dann pfadgebundene Einträge. Jeder Eintrag benennt explizit, welchen *konkreten* Kandidaten oder Mechanismus er trifft und was er ausdrücklich nicht ausschließt — pauschale Verallgemeinerungen zu Axiomen über X sind vermieden.

---

### X.neg.8 — Kategoriale Trennung X ≠ m_arith

**Quelle:** `NEU-114` · **Gültigkeit:** `bridge`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Die direkte Gleichsetzung von Objekt X mit der aus NEU-77–113 konstruierten arithmetischen Weyl-Herglotz-Funktion \(m_{\mathrm{arith}}\) als *identisches* Objekt (nicht nur als Bild einer Abbildung von X). |
| **Exakte Hypothesen** | Es wird lediglich die kategoriale Verschiedenheit der Konstruktionsebenen unterstellt: \(m_{\mathrm{arith}}\) ist ein eindimensionales, RH-äquivalentes Herglotz-Objekt; X ist fünfschichtig und kohomologisch-kategorial höherstufig. Keine weiteren Zusatzannahmen (kein Parameterbereich, kein Algebrentyp) nötig — die Aussage ist eine reine Typfeststellung. |
| **Umfang** | Schließt nur die *Identität* \(X = m_{\mathrm{arith}}\) aus. Es bleibt ausdrücklich zulässig, dass \(m_{\mathrm{arith}} = \Pi_\gamma(X)\) gilt, also dass \(m_{\mathrm{arith}}\) eine echte Projektion von X auf eine "spektrale γ-Achse" ist — sofern die Rückbindung der oberen Schichten (\([\tilde\omega_2]\), \([L_3]\), \(\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}\), Primkanten) gelingt. |
| **Positive Folgerung** | X muss über eine explizite Projektionsabbildung \(\Pi_\gamma\) vermittelt werden, die erst nachträglich (nach Rückbindungstest) mit \(m_{\mathrm{arith}}\) identifiziert werden darf. Dies erzwingt für X selbst eine echte Mehrschichtigkeit, die nicht auf die Spektralschatten-Spur reduzierbar ist. |
| **Betroffener Konstruktionspfad** | P0 (betrifft die Systemarchitektur der Rückbindung, unabhängig vom gewählten Konstruktionsweg). |

---

### X.neg.9 — Kategorialer Schutzsatz Wres^top ≠ Q_Weil

**Quelle:** `NEU-115` · **Gültigkeit:** `bridge`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Die direkte Gleichsetzung der Spurform-Schicht von X, \(\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}\) (eine lineare Spur-/Distributionsform), mit der bilinearen Weil-Quadratform \(Q_{\mathrm{Weil}}\) der Explizitformel. |
| **Exakte Hypothesen** | Reine Gradbedingung: \(\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}\) ist linear, \(Q_{\mathrm{Weil}}\) ist quadratisch/bilinear. Der Ausschluss gilt unabhängig vom konkreten Inhalt beider Objekte — es handelt sich um eine typtheoretische, nicht um eine inhaltliche Aussage. Keine weitere Voraussetzung nötig. |
| **Umfang** | Schließt nur die *direkte* Gleichsetzung beider Formen aus, nicht die Existenz eines Zusammenhangs zwischen ihnen. Insbesondere nicht ausgeschlossen: ein lineares Zwischenobjekt \(W_\xi\) (Weil-Distribution auf dem Paley-Wiener-Raum), das erst durch Pairing mit sich selbst (Faltung, \(Q_{\mathrm{Weil}}[f] = \langle W_\xi, f^\ast\ast f\rangle\)) zur Quadratform wird. |
| **Positive Folgerung** | Die Spurform-Schicht von X muss über ein eigenständiges lineares Interface \(W_\xi\) vermittelt werden, bevor sie an die (quadratische) Weil-Explizitformel andocken kann; \(\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}} \stackrel{?}{=} W_\xi\) bleibt der präzisierte, noch offene Anschlusstest. |
| **Betroffener Konstruktionspfad** | P0 (betrifft die Vermittlungsschicht zwischen der \(\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}\)-Komponente von X und der Weil-Formel, unabhängig vom Konstruktionsweg der Spurform selbst). |

---

### X.neg.10 — Triviales Zentrum der C*-BC-Algebra und keine globale Bimodul-Retraktion

**Quelle:** `NEU-215` · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | (a) Jedes nichttriviale zentrale Element der \(C^*\)-vervollständigten Bost-Connes-Algebra \(A_{C^*}\); (b) jeder stetige globale \(A_{\mathrm{alg}}\)-Bimoduloperator \(R: A_{C^*}\to\mathcal A^\infty\) mit \(\mathcal A^\infty\subsetneq A_{C^*}\) als *echtem* Teilraum. |
| **Exakte Hypothesen** | Voraussetzungen der Beweiskette: \(C(\widehat{\mathbb Z})\) ist MASA in \(A_{C^*}\) (topologisch freie \(\mathbb{Q}_+^\times\)-Wirkung, Amenabilität, Eckpunktübertragung); \(\sigma_k\)-Invarianz aus \([f,\mu_k]=0\); Faktorialkonvergenz \(j!\cdot y\to0\). Zusatzkorrektur gegenüber früherer Fassung: \(A_{C^*}\) ist *nicht* einfach — der frühere Schluss „injektiv ⟹ treu" war unzulässig und wurde zurückgenommen. |
| **Umfang** | Schließt nur nichttriviale *zentrale* Elemente und *globale, stetige, echte* Bimodul-Retraktionen aus. Schließt nicht jede Art von Unterraumkonstruktion aus — lokale, nicht-globale oder unstetige Konstruktionen sowie Konstruktionen auf der algebraischen (nicht \(C^*\)-vervollständigten) Algebra \(A_{\mathrm{alg}}\) selbst sind nicht erfasst. |
| **Positive Folgerung** | Die Hochschild-Konstruktionen von \([\tilde\omega_2]\), \([L_3]\) und letztlich \(\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}\), die auf \(A_{C^*}\) aufbauen, dürfen sich nicht auf zentrale Cup-Faktoren oder globale Retraktionen stützen — jede Zerlegung dieser HH-Schichten von X muss ohne solche Mechanismen auskommen. |
| **Betroffener Konstruktionspfad** | P3 (HH-/zyklische Kohomologie). |

---

### X.neg.11 — Hilbertraumspur-No-Go für die archimedische Gamma-Komponente

**Quelle:** `NEU-220e` · **Gültigkeit:** `spectral`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Die Realisierung der archimedischen Gamma-Rohform \(\Lambda_\Gamma(h)\) als gewöhnliche Hilbertraumspur \(\mathrm{Tr}_{B(L^2)}(\gamma_\infty(H_\infty)h(H_\infty))\) eines Operator-Funktionalkalküls. |
| **Exakte Hypothesen** | Strukturell, unabhängig vom Abklingverhalten der Testfunktion \(h\): Unter der Mellintransformation wird der Operator zum Multiplikationsoperator \(M_{\gamma_\infty h}\) auf dem nichtatomaren Maßraum \((\mathbb R, dt)\); Multiplikationsoperatoren mit \(a\not\equiv0\) sind dort nie kompakt, insbesondere nicht spurklassig. Keine Zusatzbedingung an \(h\) erforderlich. |
| **Umfang** | Schließt nur die gewöhnliche (\(\mathcal S_1\)-)Hilbertraumspur dieser konkreten archimedischen Komponente aus. Schließt nicht die Existenz einer semifiniten Spur aus — diese wird tatsächlich erfolgreich konstruiert (\(\Lambda_\Gamma(h)=\frac1{2\pi}\tau_\infty(\gamma_\infty(H_\infty)h(H_\infty))\) mit der n.f.s.-Spur \(\tau_\infty\) auf \(L^\infty(\mathbb R,dt)\)). |
| **Positive Folgerung** | Die archimedische Komponente der Spurform \(\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}\) von X muss als semifinite (statt gewöhnliche Hilbertraum-)Spur realisiert werden; der intrinsische geometrische/streutheoretische Ursprung der auftretenden Digammafunktion bleibt offen. |
| **Betroffener Konstruktionspfad** | P2 (Selbstenergie-/Mangoldtpfad — die Gamma-Rohform entsteht als archimedischer Gegenpart zu den endlichen Primkanal-Selbstenergie-Termen der Weil-Explizitformel-Realisierung). |

---

### X.neg.12 — Normierungsbruch zwischen Spurklasse und Mangoldt-Spur

**Quelle:** `NEU-140` · **Gültigkeit:** `spectral`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Die direkte Identifikation „T1": \(|c_p|^2=\log p\), also die Hoffnung, dass die Kanalnorm \(|c_p|^2 = \mathrm{Tr}_{\mathcal S_1}(C_p^{\mathrm{rel}}(C_p^{\mathrm{rel}})^\sharp)\) selbst unmittelbar die Mangoldt-Gewichtung trägt. |
| **Exakte Hypothesen** | Beruht auf der bewiesenen oberen Schranke \(|c_p|^2=O((\log p)^2/p)\) (NEU-135.D). Daraus folgt für große \(p\): \(|c_p|^2/\log p = O(\log p/p)\to 0\) — die Schranke selbst ist unbedingt bewiesen (\(\times[F]\) für T1 direkt), keine weiteren Modellannahmen nötig. |
| **Umfang** | Schließt nur die *ungedämpfte* Identifikation \(|c_p|^2=\log p\) für große \(p\) aus. Schließt nicht aus, dass die gewöhnliche Spur \(\mathrm{Tr}(\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta))\) eine *gedämpfte* Mangoldt-Spur liefert, die durch einen zusätzlichen Renormierungsoperator wiederhergestellt werden kann. |
| **Positive Folgerung** | Die Spurklassen-Komponente, die in \(\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}\) und die Zeta-Identifikation von X eingeht, benötigt zwingend einen zusätzlichen Renormierungsoperator \(R_p=\log p/|c_p|^2\) — die reine Spurklassennorm allein trägt die arithmetische Gewichtung nicht. |
| **Betroffener Konstruktionspfad** | P2 (Selbstenergie-/Mangoldtpfad). |

---

### X.neg.13 — Notwendige Unbeschränktheit der Mangoldt-Renormierung im kritischen Streifen

**Quelle:** `NEU-141` · **Gültigkeit:** `spectral`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Ein *beschränkter*, primkanaldiagonaler Renormierungsoperator \(R\) (mit \(R_p=\log p/|c_p|^2\)), der die Mangoldt-Spur exakt und im gewöhnlichen Spurklassensinn für den gesamten Bereich \(0<\Re\beta\le1\) korrekt gewichtet. |
| **Exakte Hypothesen** | Bedingt auf zwei Annahmen: (1) \(R\) ist primkanaldiagonal (setzt T2-Orthogonalität voraus, selbst offen); (2) die Wachstumsschranke \(R_p\gtrsim p/\log p\) aus NEU-140/NEU-135.D. Unter diesen Annahmen gilt zusätzlich: \(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\in\mathcal S_1\) im Mangoldt-Sinn \(\iff \Re\beta>1\). |
| **Umfang** | Schließt nur beschränkte, primkanaldiagonale Renormierungsoperatoren aus und nur die gewöhnliche Spurklassentheorie für \(0<\Re\beta\le1\). Schließt nicht aus, dass eine regulierte Spur (analytische Fortsetzung, resolventenartige Regularisierung, Hadamard-Renormierung) im kritischen Bereich funktioniert; schließt auch nicht die (aufwendigere, „deutlich instabilere") biorthogonale Renormierung aus, falls T2-Orthogonalität scheitert. |
| **Positive Folgerung** | Im RH-relevanten Bereich \(0<\Re\beta\le1\) muss X mit einem notwendig unbeschränkten Renormierungsoperator und einer regulierten (nicht gewöhnlichen) Spur arbeiten — die gewöhnliche Spurklassentheorie ist dort strukturell unzureichend. |
| **Betroffener Konstruktionspfad** | P2 (Selbstenergie-/Mangoldtpfad). |

---

### X.neg.14 — Nilpotenz-Barriere des isolierten Mangoldt-Jacobi-Operators

**Quelle:** `NEU-86` · **Gültigkeit:** `spectral`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Der isolierte, rein vorwärtsgerichtete (strikt oberdreieckige) Mangoldt-gewichtete Jacobi-Operator \(J_N^\Lambda\) auf endlichem \(\ell^2(I_N)\) als Träger einer nichttrivialen Spur-/Determinantenstruktur für X. |
| **Exakte Hypothesen** | Gilt für \(J_N^\Lambda\) in seiner isolierten (nicht mit ihrem Adjungierten symmetrisierten) Form auf endlichem \(N\); die algebraische Identität \((J_N^\Lambda)^N=0\) ist unbedingt (reine Struktureigenschaft strikt oberdreieckiger Matrizen). |
| **Umfang** | Schließt nur die *isolierte* Vorwärts-Shift-Klasse aus. Schließt nicht den Jacobi-Abschluss \(A_N^\Lambda=H_N+J_N^\Lambda+(J_N^\Lambda)^*\) aus (selbstadjungiert, nichttriviales Spektrum), nicht die relative Determinante \(\det(I+(J_N^\Lambda+(J_N^\Lambda)^*)(H_N-z)^{-1})\), und nicht einen echten Feshbach-Schur-Komplement-Operator. |
| **Positive Folgerung** | Für X gilt: Spur (\(=0\) für \(k\ge1\)) und Fredholm-Determinante (\(\equiv1\)) des isolierten Vorwärtsoperators tragen keine arithmetische Information — die zentrale Operator-Komponente \(A_{2D}^r\) muss auf einer symmetrisierten oder Schur-komplementierten Konstruktion beruhen, nicht auf einem reinen Shift. |
| **Betroffener Konstruktionspfad** | P2 (Selbstenergie-/Mangoldtpfad). |

---

### X.neg.15 — Direkt-Summen-Obstruktion des kollektiven Birman-Schwinger-Operators

**Quelle:** `NEU-50` · **Gültigkeit:** `Feshbach`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Der kollektive Birman-Schwinger-Operator \(K_N\), konstruiert als reine Blockdiagonale \(\bigoplus_p K_p\) über Primkanäle, als Lösung des Nichtüberzählungsproblems (korrekte Multiplizität \(m_\rho\) der Nullstellen). |
| **Exakte Hypothesen** | Reine algebraische Identität, ohne Zusatzannahmen: \(\det(1-\mathcal K_N^{\mathrm{diag}})=\prod_{p\le N}\det(1-K_p)\) und \(\ker(1-\mathcal K_N^{\mathrm{diag}}(\rho))=\bigoplus_{p\le N}\ker(1-K_p(\rho))\). |
| **Umfang** | Schließt nur die *blockdiagonale* Konstruktion aus, die die Einzelkanalbeiträge rein additiv reproduziert. Schließt nicht jede Konstruktion eines kollektiven Operators aus \(K_p\)-Bausteinen aus — insbesondere nicht die Feshbach-Form \(\mathcal K_N(s)=V_N^*(D_{\mathrm{rel}}-s)^{-1}V_N\) mit Off-Diagonal-Kopplung \(K_{pq}(s)=V_p^*(D_{\mathrm{rel}}-s)^{-1}V_q\neq0\) für \(p\neq q\). |
| **Positive Folgerung** | Der primkanten-basierte Birman-Schwinger-Baustein von \(A_{2D}^r\) muss echte Kreuzterme (Off-Diagonal-Kopplung) zwischen Primkanälen tragen; diese sollen über \([\tilde\omega_2]\), \([L_3]^\circ\), \(\mathrm{Wres}\) motiviert werden, die explizite Formel bleibt offen. |
| **Betroffener Konstruktionspfad** | P1 (Feshbach-/Primkantenpfad). |

---

### X.neg.16 — Normierungs-No-Go für isometrische Feshbach-Kollaps-Einbettungen

**Quelle:** `NEU-78` · **Gültigkeit:** `Feshbach`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Eine isometrische (normerhaltende) Einbettung \(U_N:\ell^2(I_N)\to\mathcal H_N\), die den ungewichteten, exakten Kollapsoperator \(J_N^-\) über \(U_N^* S_N R_N D_{BC,N} U_N = J_N^-\) reproduziert. |
| **Exakte Hypothesen** | Gilt für endliches \(N\) mit \(|S_N|>1\) (mehr als ein Kanal). Beweis über Widerspruch: Einbettungsbedingung \(\sum_n|a_{n,N}|^2=1\) erzwingt \(|a_{n,N}|^2<1\) für alle \(n\), unvereinbar mit der für \(J_N^-\) nötigen Bedingung \(|a_{n,N}|^2=1\) für alle \(n\) gleichzeitig. |
| **Umfang** | Schließt nur *isometrische* Kollaps-Einbettungen aus. Schließt nicht aus: (1) \(J_N^-\) als unnormalisierte Wechselwirkungsmatrix mit extern absorbiertem Faktor \(|S_N|\); (2) kanalabhängige Renormierung \(\widetilde J_N^-=|S_N|^{-1}J_N^-\); (3) einen expliziten Kopplungsfaktor \(\Pi_N=|S_N|^{1/2}U_N\). Der Jacobi-kompatible Anschluss (Skalierung im Limes) bleibt offen. |
| **Positive Folgerung** | Die Kollaps-Komponente des Feshbach-Bausteins von \(A_{2D}^r\) kann nicht demokratisch-isometrisch sein; sie muss eine gewichtete Mittelung oder einen expliziten Kopplungsfaktor tragen, der den \(|S_N|\)-Faktor durch den Limes verfolgt. |
| **Betroffener Konstruktionspfad** | P1 (Feshbach-/Primkantenpfad). |

---

### X.neg.17 — Dichtebedingung für simultane Feshbach- und Jacobi-Stabilität

**Quelle:** `NEU-82` · **Gültigkeit:** `Feshbach`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Eine dünne Labelmenge \(\Sigma_N\) (z.B. nur Primzahlen \(\{p\le N\}\), \(\kappa_N\sim N/\log N\)) als Trägerstruktur, die gleichzeitig Feshbach-Gesamtstabilität und Jacobi-Gewichts-Beschränktheit liefert. |
| **Exakte Hypothesen** | Simultane Forderung von Feshbach-Stabilität (\(\sum_{n\in\Sigma_N}\lambda_{n,N}\to\gamma>0\)) und Jacobi-Gewichts-Stabilität (\(N\cdot\sup_n\lambda_{n,N}=O(1)\)); daraus folgt formal \(\sum_n\lambda_{n,N}\lesssim\kappa_N/N\), also \(\kappa_N\asymp N\). Unbedingte algebraische Herleitung. |
| **Umfang** | Schließt nur *dünne* Labelmengen als Trägerstruktur für die Jacobi-Limes-Komponente aus. Schließt nicht die volle Labelmenge \(\Sigma_N=\{2,\ldots,N\}\) aus — im Gegenteil, diese ist nach dem Ergebnis die *einzige* verbleibende Wahl. |
| **Positive Folgerung** | Die Jacobi-Limes-Komponente von \(A_{2D}^r\) muss auf der vollen (dichten) Labelmenge aufbauen, mit nachträglicher Mangoldt-Extraktion über Möbius-/Primsektor-Projektion — nicht auf einer primzahlindizierten dünnen Trägermenge. |
| **Betroffener Konstruktionspfad** | P1 (Feshbach-/Primkantenpfad). |

---

### X.neg.18 — Dreifach-Konflikt Feshbach/Jacobi/Mangoldt auf vollem Orbitbereich

**Quelle:** `NEU-83` · **Gültigkeit:** `Feshbach`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Eine Gewichtsfolge \(\lambda_{n,N}\), die auf dem *vollen* Orbitbereich \(r\le N\) gleichzeitig proportional zur von-Mangoldt-Funktion \(\Lambda(n)\) ist, Jacobi-Zeilennormen beschränkt hält und Feshbach-Gesamtmasse stabilisiert. |
| **Exakte Hypothesen** | Ausdrücklich beschränkt auf den vollen Orbitbereich \(r\le N\). Beweis: Mangoldt-Gewichtung \(\lambda_{n,N}=c_N\Lambda(n)\) und Jacobi-Stabilität \(c_N\Lambda(n)\lesssim1/N\) erzwingen \(c_N\lesssim1/(N\log N)\), womit \(\sum_n\lambda_{n,N}\lesssim1/\log N\to0\) — Widerspruch zur Feshbach-Stabilität \(\to\gamma>0\). |
| **Umfang** | Schließt nur die Kompatibilität aller drei Forderungen *auf dem vollen Orbitbereich* \(r\le N\) aus. Schließt nicht die Orbit-Trunkierung \(r\lesssim N/\log N\) aus, unter der alle drei Forderungen gleichzeitig erfüllbar werden; auch nicht ein logarithmisches Jacobi-Wachstum unter Carleman-Kontrolle oder eine gewichtete, große \(r\) dämpfende Hilbertraumnorm. |
| **Positive Folgerung** | Die arithmetische (Mangoldt-)Aufladung der Jacobi-Komponente von X erfordert eine Orbit-Trunkierung \(r\lesssim N/\log N\) (favorisierter Reparaturweg) — der volle Orbitbereich ist für diese Aufladung nicht tragfähig. |
| **Betroffener Konstruktionspfad** | P1 (Feshbach-/Primkantenpfad). |

---

### X.neg.19 — Trivialität des starken Operatorlimes auf festen Basisvektoren

**Quelle:** `NEU-85` · **Gültigkeit:** `Feshbach`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Der naive starke Operatorlimes des Mangoldt-gewichteten Jacobi-Vorwärtsoperators \(J_N^\Lambda\) auf dem Raum fest getragener (nicht mit \(N\) mitwachsender) \(\ell^2\)-Vektoren als Trägerkonstruktion für die arithmetische Information von X. |
| **Exakte Hypothesen** | Für jeden endlich getragenen, mit \(N\) fest bleibenden Vektor \(f\) (bzw. \(\delta_r\) mit festem \(r\)) gilt \(\|J_N^\Lambda\delta_r\|_2\asymp\gamma r\sqrt{\log N/N}\to0\) — reine asymptotische Rechnung, keine weiteren Modellannahmen. |
| **Umfang** | Schließt nur den starken Limes *auf festen Vektoren* aus, obwohl die Feshbach-Gesamtmasse \(\sum_n\lambda_{n,N}\sim\gamma\) stabil bleibt. Schließt nicht aus: wandernde Fenster \(r=r_N=\alpha\sqrt{N/\log N}\) mit endlicher, nichttrivialer Zeilennorm; Feshbach-/Kollapsfunktionale \(\Pi_N J_N^\Lambda\Pi_N^*\); Spur- und Determinantenobjekte; \(N\)-abhängige (renormierte) Testtopologie. |
| **Positive Folgerung** | Die Existenzform des Grenzoperators \(A_{2D}^r\) kann nicht im naiven starken \(\ell^2\)-Konvergenzbegriff auf festen Basisvektoren verortet werden — X wird erst durch eine geeignete Zusatzstruktur (wandernde Skalierung, Funktional, renormierte Testtopologie) als Grenzobjekt sichtbar. |
| **Betroffener Konstruktionspfad** | P1 (Feshbach-/Primkantenpfad). |

---

### X.neg.20 — Kein einzelner Skalar stabilisiert zwei divergierende Offdiagonalfolgen

**Quelle:** `NEU-123H` · **Gültigkeit:** `route-conditional`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Ein einzelner skalarer Renormierungsfaktor \(\kappa_N\), der die Jacobi-Offdiagonalfolgen \(b_{1,N}\) und \(b_{2,N}\) aus der NEU-87-Jacobi-Schließung gleichzeitig zu endlichen, positiven Grenzwerten stabilisiert. |
| **Exakte Hypothesen** | Das Lemma selbst ist unbedingt (reine Analysis: Für positive Folgen mit \(b_{2,N}/b_{1,N}\to\infty\) existiert keine Folge \(\kappa_N>0\) mit \(b_{1,N}/\kappa_N\to c_1\in(0,\infty)\) und \(b_{2,N}/\kappa_N\to c_2\in(0,\infty)\) gleichzeitig). Die Anwendung auf den konkreten Jacobi-Operator ist dagegen **bedingt** auf den numerischen Befund \(b_{2,N}/b_{1,N}\sim N\to\infty\) (NEU-123.G); ein strenger Beweis hängt an der offenen Sieve-Parity-Barriere. |
| **Umfang** | Schließt nur *einen einzelnen skalaren* Renormierungsfaktor aus, und die Anwendung auf den Jacobi-Operator nur unter der (numerisch, nicht streng bewiesenen) Divergenzannahme. Schließt nicht die gradierte (indexabhängige) Renormierung \(\widetilde A_N=D_N^{-1}A_N^{\mathrm{Jac},-}D_N\) mit Diagonalmatrix \(D_N\) aus — sofern diese intrinsisch aus der Feshbach-Struktur folgt und nicht extern an Zeta-Zieldaten gefittet wird (Anti-Fitting-Axiom). |
| **Positive Folgerung** | Die Grenzoperator-Konstruktion von \(A_{2D}^r\) benötigt eine gradierte statt skalare Renormierung — deren intrinsische (nicht gefittete) Existenz ist der noch offene Kernpunkt. |
| **Betroffener Konstruktionspfad** | P2 (Selbstenergie-/Mangoldtpfad — Grenzoperator-Renormierung als Fortsetzung der Jacobi-Konstruktion). |

---

### X.neg.21 — Norm-No-Go für verdrehte Nullkozykel bei Re β > 0

**Quelle:** `NEU-182` · `NEU-183` (Quellenaudit) · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Ein nichttrivialer verdrehter Nullkozykel \(u\in Z^0(A_{\mathbb Q}^{\mathrm{alg}}, M_{\sigma_\beta})\), der über den Cup-Weg \(u_\beta\smile\Omega_{\mathbf p}\) einen geladenen Vier-Kozykel faktorisieren könnte. |
| **Exakte Hypothesen** | Für \(n>1\), \(\mu_n u = n^{-\beta}u\mu_n\), \(\operatorname{Re}\beta>0\): unter der Isometriebedingung \(\mu_n^*\mu_n=1\) (Relation (R2) der Bost-Connes-Standardpräsentation) und treuer \(C^*\)-Einbettung \(A_{\mathbb Q}^{\mathrm{alg}}\hookrightarrow A_{\mathbb Q}^{C^*}\) folgt \(u=0\) über das Isometrie-Lemma \(\|u\|=\|vu\|=|c|\,\|uv\|\le|c|\,\|u\|\). Beide Zusatzhypothesen sind durch das Quellenaudit als Standardresultat (Bost–Connes 1995, Relationen (R1)–(R7)) bestätigt, wodurch das Ergebnis unbedingt wird. |
| **Umfang** | Gilt nur für \(\operatorname{Re}\beta>0\), nicht für \(\operatorname{Re}\beta=0\). Schließt ausdrücklich nur die *verdrehte* Faktorisierungsroute aus — nicht \(HH^4(A_{\mathbb Q}^{\mathrm{alg}}, {}_{\mathrm{id}}A_{\mathbb Q,\sigma_\beta})_{\mathrm{ch}}=0\) insgesamt. Der reguläre Faktorisierungsweg (mit \(u_g\in Z(A)\cap A_g\), \(g\neq1\)) ist ein separater Fall (siehe X.neg.22). |
| **Positive Folgerung** | Die geladene HH⁴/HH²-Klassenkonstruktion (\([\tilde\omega_2]\)/\([L_3]\)-Schicht von X bzw. deren Vorstufen) kann für \(\operatorname{Re}\beta>0\) nicht über einen verdrehten zentralen Nullkozykel-Cup-Faktor laufen. |
| **Betroffener Konstruktionspfad** | P3 (HH-/zyklische Kohomologie). |

---

### X.neg.22 — Trivialität des regulären Zentrums der Bost-Connes-Algebra

**Quelle:** `NEU-183` (Zentrumstest) · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Ein homogenes Element \(u_g\neq0\) vom Grad \(g\neq1\) in der Bost-Connes-Algebra \(A_{\mathbb Q}^{\mathrm{alg}}\), das mit allen Erzeugern (\(e(r)\), \(\mu_n\), \(\mu_n^*\)) kommutiert — d.h. die *reguläre* Zentrumsroute \(u_g\smile\Omega_{\mathbf p}\) für die geladene HH⁴-Klasse. |
| **Exakte Hypothesen** | \(Z(A_{\mathbb Q}^{\mathrm{alg}})_g=0\) für alle \(g\neq1\), bestätigt über die Standardpräsentation von Bost–Connes (Normalform \(w_{m,r,n}=\mu_m e(r)\mu_n^*\) als Linearbasis von \(A_g\)). Gilt für alle \(\beta\), nicht nur \(\beta>0\) — im Unterschied zum verdrehten Fall (X.neg.21). |
| **Umfang** | Schließt die reguläre *und* (zusammen mit X.neg.21) die verdrehte Cup-Produkt-Faktorisierungsroute über zentrale Elemente vollständig aus. Schließt nicht aus, dass das Polynommodell \(\mathbb C[x_1,\ldots,x_4]\) (NEU-178) geladene Zentralelemente besitzt — dieses Modell ist aber nachweislich nicht direkt auf die volle BC-Algebra \(A_{\mathbb Q}\) übertragbar (Isometriehindernis \(\mu_n\mu_n^*\neq1\) plus Zentrumsmangel). Direkte HH⁴-Klassen ohne Produktstruktur (Barauflösung, Deformationstheorie) bleiben unberührt. |
| **Positive Folgerung** | Die geladene Vierkozykelklasse für \([L_3]\) muss über direkte Kozykelkonstruktionen oder über eine Projektion auf ein einfacheres Modell (Polynommodell als „Quotientenschatten") erzeugt werden — nicht über zentrale Cup-Faktoren in \(A_{\mathbb Q}^{\mathrm{alg}}\) selbst. |
| **Betroffener Konstruktionspfad** | P3 (HH-/zyklische Kohomologie). |

---

### X.neg.23 — Augmentationsblindheit der punktierten Potentialroute

**Quelle:** `NEU-196` · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Jeder aus der punktierten Potentialroute (NEU-186–188) erzeugte Derivationskandidat \(D_g\), bezüglich der für NEU-195 nötigen Augmentationsbedingung \(\varepsilon(D_g(\mu_p))\neq0\). |
| **Exakte Hypothesen** | \(F_k(0)=0\) für jede lokal konstante Fortsetzung \(F_k\) eines regularisierten Differenzdefekts \(\Delta_k H = H(kx)-H(x)\) eines auf \(\widehat{\mathbb Z}\setminus\{0\}\) lokal konstanten \(H\) — elementarer Kompaktheits-/Teleskopbeweis, unbedingt. Konsequenz: \(\langle\Omega_{D_g,\mathbf p}, z_{-\lambda}^{g,\mathbf p}\rangle=0\). |
| **Umfang** | Schließt nur die *gesamte punktierte-Potentialarchitektur* aus NEU-186–188 als Quelle für die Augmentationskopplung aus — ausdrücklich nicht \(D_g=0\) und nicht \([D_g]=0\in HH^1(A,A)_g\) insgesamt. |
| **Positive Folgerung** | Die geladene Derivation, die \([\tilde\omega_2]\) bzw. \([L_3]\) trägt, muss entweder außerhalb der punktierten-Potentialarchitektur konstruiert werden, oder der Dualzyklus muss so modifiziert werden, dass er die singuläre Randklasse bei \(\partial\widehat{\mathbb Z}\) statt der Augmentation \(\varepsilon\) bei 0 detektiert (z.B. über einen Residuenoperator oder Grenzwert entlang \(x_j\to0\)). |
| **Betroffener Konstruktionspfad** | P4 (singuläre Potentialroute). |

---

### X.neg.24 — Unsichtbarkeit regulärer Potentiale im Kommutatorquotienten

**Quelle:** `NEU-200` · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Jedes global reguläre (auf ganz \(\widehat{\mathbb Z}\) lokal konstante) Potential \(H\in\operatorname{LC}(\widehat{\mathbb Z})=B\) als Quelle einer nichtverschwindenden Klasse im relevanten Kommutatorquotienten. |
| **Exakte Hypothesen** | \([G_i^H]=0\) in \(B/\sum_{j=1}^4(1-\alpha_{p_j})B\) für *jedes* global reguläre \(H\), mit explizitem Kommutatorzeugen \(Y_{g,H,\mathbf p,i}=[\mu_{p_i},a_{i,H}]\) — unbedingt für den regulären Sektor, unabhängig vom konkreten \(H\). |
| **Umfang** | Schließt nur den *regulären* Sektor aus, nicht die punktierte (bei 0 singuläre) Potentialroute insgesamt, sondern nur deren regulären Untersektor. \([G_i^H]\) ist dabei eine Rand-Singularitätsobstruktion, keine gewöhnliche Nichtverschwindungsobstruktion. |
| **Positive Folgerung** | Ein positiver Befund (nichtverschwindende Klasse) kann nur von einem echt singulären Potential \(H\in\operatorname{LC}(\widehat{\mathbb Z}\setminus\{0\})\setminus\operatorname{LC}(\widehat{\mathbb Z})\) mit \(F_{p_j}=\alpha_{p_j}(H)-H\in B\) für die relevanten \(p_j\) kommen — Regularität bei 0 ist der Feind der Nichttrivialität in dieser Konstruktion. |
| **Betroffener Konstruktionspfad** | P4 (singuläre Potentialroute). |

---

### X.neg.25 — Ketten-No-Go für die eindimensionale Kettenarchitektur des Bewertungsgitters

**Quelle:** `NEU-207` · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Eine exakte, eindimensionale totale Teilbarkeitskette \((L_j)\), die Vielfache zweier verschiedener Primzahlen enthält, als unter allen Primtransporten \(T_p(L)=L/(L,p)\) geschlossene Nachbarschalen-Geometrie. |
| **Exakte Hypothesen** | Für \(p\neq q\) mit \(pq\mid L\): \(L/p\) und \(L/q\) sind in der Teilbarkeitsordnung unvergleichbar, da \(p\)-Bewertung und \(q\)-Bewertung gegenläufig laufen. Gilt sobald mehr als eine Primrichtung im Spiel ist — keine weiteren Modellannahmen. |
| **Umfang** | Schließt ausschließlich die *exakte totale Kettenarchitektur* aus. Ausdrücklich **nicht** ausgeschlossen: approximative Ketten, verzweigte Indexmengen, mehrdimensionale Gitter, endliche gesättigte Kastenmodelle. |
| **Positive Folgerung** | Der eindimensionale Nachfolger der dyadischen Konstruktion (NEU-204) ist beendet; die Konstruktion muss zum mehrdimensionalen Bewertungsgitter \(\Lambda=\mathbb N_0^{(\mathcal P)}\) mit exakten Gittertranslationen übergehen — dieser Übergang wird in derselben Quelle tatsächlich erfolgreich durchgeführt, mit verbleibendem Flaschenhals bei der Randtermkontrolle wachsender Gitterpartitionen. |
| **Betroffener Konstruktionspfad** | P4 (singuläre Potentialroute). |

---

### X.neg.26 — Ausschluss des naiven Sandwichansatzes für geladene Primkanal-Kopplung

**Quelle:** `NEU-209` · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Der naive geladene Kopplungsansatz \(Z_{F,\mathbf N}=\mu_m(\sum_{p\in F}\widetilde X_{p,N_p})\mu_n^*\), der eine Summe unabhängiger, separierbarer Prim-Singularitäten \(X=\sum_p X_p\) mit den geladenen Erzeugern \(\mu_m,\mu_n^*\) sandwichartig koppelt. |
| **Exakte Hypothesen** | Gilt für jeden nichtverschwindenden Charakterfehlermultiplikator \(M_{g,r}\neq0\). Mechanismus: Separierbare Primkanäle \(X_{p,N}\) tragen ihre Singularität auf ganzen Koordinatenhyperflächen \(K_p=\{x_p=0\}\) (nicht nur im Punkt 0); für \(p\nmid L\) „sieht" der Multiplikator \(K_p\) vollständig (\(\|M|_{K_p}\|=\|M\|\)), sodass \(\|M\widetilde X_{p,N}\|\to\infty\) — die \(e(r)\)-Kommutatornormen divergieren. |
| **Umfang** | Schließt nur die *geladene Kopplung* über diesen naiven Sandwichmechanismus aus. Der neutrale Erfolg von NEU-208 (Refinementstabilität des separierbaren Kanals selbst, ohne geladene Kopplung) bleibt ausdrücklich bestehen. |
| **Positive Folgerung** | Gesucht ist keine Summe unabhängiger Prim-Singularitäten, sondern eine gemeinsame, global bei 0 lokalisierte Singularität mit separierbaren Transportdifferenzen, die notwendig \(\operatorname{Sing}(X)\subseteq Z_g\) (gemeinsame Charakterkernmenge) erfüllt — Kandidat: \(X_N=f(N)\cdot E_{\mathrm{lcm}(1,\ldots,N)}\). |
| **Betroffener Konstruktionspfad** | P4 (singuläre Potentialroute). |

---

### X.neg.27 — Nichtzyklizität des kanonischen Basislifts des geladenen Vierkozykels

**Quelle:** `NEU-219u` · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Der kanonische Basislift \(\widetilde L_0=\eta_0\circ j_M\circ L^{\mathrm{cup}}_{g;\mathbf p}\) (mit \(\kappa=0\), \(\varepsilon=0\)) des geladenen Vierkozykels, als Erzeuger einer Klasse in der zyklischen Kohomologie \(HC^4(A_{\mathrm{alg}})\). |
| **Exakte Hypothesen** | Gilt für \(g\neq1\). \(\widetilde L_0\in Z^4(A_{\mathrm{alg}}, I_0)\) ist zwar ein typkorrekter Hochschildkozykel, aber \(t\Phi_0=g^{-\beta}\Phi_0\) mit \(g^{-\beta}\neq1\) macht \(\Phi_0\) nicht zyklisch. Kein Orbitgewicht \(\lambda\) kann diese Abweichung kompensieren, da \(\widetilde L_0(A_{\mathrm{alg}}^{\otimes4})\subseteq I_0\) stets den Faktor \(\lambda^0=1\) trägt. Ursache ist eine globale, eingabeunabhängige Rotation um \(g^{-\beta}\), die aus der Spektraleigenschaft von \(U_{g^{-1}}\) im KMS-Zustand stammt. |
| **Umfang** | Schließt nur den *kanonischen* Basislift (mit \(\kappa=0,\varepsilon=0\)) aus. Schließt nicht aus: einen Orbitshift-Lift (\(\kappa\neq0\), mit \(T^k\) oder \(\tau^k\)); eine Ladungsneutralisation vor zyklischer Auswertung; eine andere Koeffizientenkategorie (parazyklisch, \(\sigma\)-zyklisch, getwistet-zyklisch); eine modulare/parazyklische Struktur statt gewöhnlicher Zyklizität. |
| **Positive Folgerung** | Die \([L_3]\)-Schicht von X kann nicht in der naivsten (Cup-Produkt-mit-KMS-Zustand-)Form realisiert sein — sie benötigt zwingend eine der genannten Zusatzkonstruktionen (Orbitshift, Ladungsneutralisation, getwistete/parazyklische Kohomologietheorie), um überhaupt eine zyklische Klasse zu liefern. |
| **Betroffener Konstruktionspfad** | P3 (HH-/zyklische Kohomologie). |

---

### X.neg.28 — Positive invertierbare Kreinraum-Metrik existiert nur unter RH selbst

**Quelle:** `NEU-220t` · **Gültigkeit:** `route-conditional`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Der naive Konstruktionsweg „Kreinraum-Metrik \(\mathscr J_\kappa\) → nichtlokale Korrektur → positive, invertierbare Metrik \(\eta>0\)" für den konkreten Kreinraum-Modell-Kandidaten von \(A_{2D}^r\), solange an der Metrikgleichung \(Z^*\eta=\eta Z\) festgehalten wird. |
| **Exakte Hypothesen** | Modellspezifisch für das Kreinraum-Modell mit hypothetischem off-axis-Nullstellenpaar \(\{\rho,\kappa\rho\}\) (\(\rho\neq\kappa\rho\)). Für jede invertierbare hermitesche Metriklösung \(\eta\) erzwingt jedes solche Paar eine indefinite Signatur (Blockform \(\begin{pmatrix}0&\alpha\\\bar\alpha&0\end{pmatrix}\)) — unabhängig von der Wahl von \(\mathscr J_\kappa\). Äquivalenzaussage: \(\mathrm{RH}\iff\exists\,\eta\ge cI>0: Z_{\mathcal Z}^*\eta=\eta Z_{\mathcal Z}\), ebenso \(\mathrm{RH}\iff Z_{\mathcal Z}\) ist durch beschränkte Ähnlichkeit zu einem selbstadjungierten Operator transformierbar. |
| **Umfang** | Gilt nur innerhalb dieses konkreten, expliziten Kreinraum-Modells, das die Nullstellenlage bereits als Eingabedatum verwendet (also selbst „tautologisch" RH-abhängig aufgebaut ist). Schließt nicht jeden denkbaren selbstadjungierten Kandidaten für \(A_{2D}^r\) aus — nur diesen einen Konstruktionsmechanismus über die Metrikgleichung. |
| **Positive Folgerung** | Für einen nicht-tautologischen Weg zu \(A_{2D}^r\) muss zunächst aus der adelischen Architektur ein positiver Spektralraum \((\mathcal H_X, A_X=A_X^*)\) *ohne* Verwendung der Nullstellenlage konstruiert werden, und erst danach über eine Spur-, Determinanten- oder Streuidentität gezeigt werden, dass seine spektrale Determinante \(\xi\) ist. |
| **Betroffener Konstruktionspfad** | P5 (Vergleichsoperator-/Konfinementpfad). |

---

### X.neg.29 — Schattenklassenzwang gegen die gewöhnliche Fredholm-Determinante des Hilbert-Pólya-Kandidaten

**Quelle:** `NEU-220u` · **Gültigkeit:** `spectral`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Der Kandidat \(\Xi(z)/\Xi(0)=\det(I-zH^{-1})\) mit **gewöhnlichem** Fredholm-Determinanten eines hypothetischen Hilbert-Pólya-Operators \(H\) mit Eigenwerten \(\gamma\) (den Nichttrivialnullstellen-Ordinaten). |
| **Exakte Hypothesen** | Unter RH als Zählhypothese, aber die Herleitung des Schattenklassenzwangs selbst benutzt nur die unbedingt gültige Riemann-von-Mangoldt-Zählformel: \(\sum_{\gamma>0}\gamma^{-p}<\infty\iff p>1\), also \(A_+^{-1}\in\mathcal S_2\setminus\mathcal S_1\) für einen hypothetischen positiven Operator \(A_+\) mit diesen Eigenwerten — \(H^{-1}\) liegt somit nicht in der Spurklasse \(\mathcal S_1\), in der die gewöhnliche Fredholm-Determinante definiert wäre. |
| **Umfang** | Schließt nur die Realisierung über die **gewöhnliche** (\(\mathcal S_1\)-)Fredholm-Determinante aus. Schließt nicht aus: den quadrierten Determinanten \(\det(I-z^2A_+^{-2})\) (da \(A_+^{-2}\in\mathcal S_1\)), konditional erfolgreich hergeleitet; ebenso nicht die äquivalente Carleman-Fredholm-Determinante zweiter Ordnung \(\det_2(I-zH_Z^{-1})\). |
| **Positive Folgerung** | Die zulässige Operatorklasse für den Hilbert-Pólya-Kandidaten \(A_{2D}^r\) muss zwingend in der Schattenklasse \(\mathcal S_2\setminus\mathcal S_1\) liegen und über eine quadrierte bzw. Carleman-regularisierte Determinante zweiter Ordnung realisiert werden — die Endkriterien HP-1 bis HP-7 (insbesondere HP-7: Nullstellenlagen dürfen nirgendwo als Eingabedaten dienen) benennen exakt, was ein nichttautologischer Kandidat \(H_X\) zusätzlich leisten müsste. |
| **Betroffener Konstruktionspfad** | P5 (Vergleichsoperator-/Konfinementpfad). |

---

## XVI-F — Register der Rückbindungstests 114.1–114.4

NEU-114 (1. Juli 2026) erkannte, dass der Pfad NEU-77–113 nicht $X$ bearbeitet, sondern die
Projektion $\Pi_\gamma(X)$, und richtete vier Tests ein, um den Spektralschatten wieder an
$X$ zu binden. Die Tests wurden geöffnet und danach in keinem der 105 Dokumente ab NEU-117
mehr erwähnt.

Dieses Register schließt die Lücke: Es verbucht, was inzwischen implizit beantwortet ist,
und führt für jeden Test einen Nachfolgeknoten.

$$
\Pi_\gamma\bigl(\mathrm{Wres}^{\mathrm{top}}, [\tilde\omega_2], [L_3], \mathrm{KMS}\bigr)
\;\overset{?}{=}\; m_{\mathrm{arith}} \,/\, Q_{\mathrm{Weil}}
$$

### F.1 — Test 114.1: $HH^2$ $[\tilde\omega_2] \to$ Herglotz-Kanal

| | |
|---|---|
| **Status** | `❓[O]` — unverändert offen |
| **Frage** | Erzeugt die primäre Hochschild-2-Klasse einen Beitrag zum Herglotz-Kanal von $m_{\mathrm{arith}}$? |
| **Was seit NEU-114 dazukam** | Nichts Direktes. Der 06-Strang arbeitete an $HH^4$, nicht an $HH^2$. |
| **Blockade** | Die Nichttrivialität von $[\tilde\omega_2]$ ist selbst nur Hypothese (vgl. XVI-A, A.0). |
| **Nachfolgeknoten** | `[O-114-1]` — offen, kein Bearbeiter |

### F.2 — Test 114.2: $HH^4$ $[L_3] \to$ Obstruktionsterm

| | |
|---|---|
| **Status** | $\checkmark[M]_{\mathrm{neg}}$ — **für den kanonischen O-219-Weg** |
| **Was seit NEU-114 dazukam** | Der gesamte Strang NEU-174 – NEU-219z. Der Cup-Aufstieg $L^{\mathrm{cup}}_{g;\mathbf p}\in Z^4(A_{\mathrm{alg}},M)_g$ gelang (NEU-218), der kanonische Basislift ist typkorrekt — aber nicht zyklisch: $t\Phi_0 = g^{-\beta}\Phi_0$ mit $g^{-\beta}\neq 1$ (NEU-219u). |

> **Reichweite — verbindlich.** Der negative Befund gilt für den **kanonischen Basislift**
> $\tilde L_0 = \eta_0\circ j_M\circ L^{\mathrm{cup}}_{g;\mathbf p}$, **nicht** für jede
> denkbare $HH^4$-Realisierung. Ausdrücklich **nicht** ausgeschlossen sind: Lifts mit
> Orbitshift $\kappa\neq 0$, algebraische Ladungsneutralisation vor der zyklischen
> Auswertung, sowie parazyklische, $\sigma$-zyklische oder getwistet-zyklische
> Koeffizientenkategorien.

| | |
|---|---|
| **Nachfolgeknoten** | `[O-219-6]` — Weil-/Gammafaktorpaarung, **aktiv beschritten** ab NEU-220; ferner XVI-D/P3.3 und P4 |

### F.3 — Test 114.3: $\mathrm{Wres}^{\mathrm{top}} \to Q_{\mathrm{Weil}}$

| | |
|---|---|
| **Status** | $\checkmark[M]_{\mathrm{part}}$ |
| **Was seit NEU-114 dazukam** | NEU-116 führte den Test teilweise aus und lieferte den **Vierschichtensatz** (116.0.V): $X_{\mathrm{skel}} \neq X \neq X^{\mathrm{val}} \neq W_\xi^{\mathrm{norm}}$. Tests ST-3/ST-4 (116.C.15) zeigen: $\Theta_{1/2}$ ist **extern** zu $X$, `✓[M]`. Intrinsizitätstest IT-1/3/4 `✓[M]` gegen $B_{\mathrm{ref}}$. Ferner: NEU-115 trennt linear von quadratisch kategorial. |
| **Gesichertes Teilergebnis** | Eine direkte Identifikation ist ausgeschlossen; die Vermittlung läuft über drei funktorielle Schritte $\iota_{\mathrm{skel}}, \iota_{\mathrm{val}}, \rho^{\mathrm{val}}$ und über das lineare Interface $W_\xi$. Siehe XVI-B, B.1 und B.2. |
| **Restlücke** | Intrinsizitätstest IT-2 `❓[O]`; die Teiltests 116.A ($E_{0,1}$), 116.B ($G$) und 116.C ($-P$) sind einzeln nicht abgeschlossen. |
| **Nachfolgeknoten** | `[O-116-IT2]`; inhaltlich fortgesetzt im gesamten Strang NEU-220 (Gammafaktor, Konturtransport, Weil-Quadratik) |

### F.4 — Test 114.4: $m \to p^k m \;\Rightarrow\; \Lambda(p^k)$

| | |
|---|---|
| **Status** | **gesperrt durch** `[O-144-1]` |
| **Was seit NEU-114 dazukam** | NEU-141 etabliert $\operatorname{Tr}(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)) = -\zeta'/\zeta(\beta)$ für $\Re\beta>1$, `✓[M]`. Die Kette Primkanten → Mangoldt-Gewicht trägt damit im Konvergenzbereich. |
| **Blockade** | Die T2-Orthogonalität $\langle\Psi_p,\Psi_q\rangle = 0$ für $p\neq q$ wird in NEU-141 **zur Voraussetzung erklärt, nicht bewiesen**. NEU-144 vermerkt wörtlich: „strukturell plausibel und durch Aufbau motiviert, aber noch kein formaler Beweis". Sie trägt die gesamte primdiagonale Struktur von $R$. |
| **Zweite Blockade** | Der kritische Streifen $0<\Re\beta\le 1$ ist unbehandelt, `[O-144-3]`. |
| **Nachfolgeknoten** | `[O-144-1]` (Edge-Label-Beweis der T2-Orthogonalität) und `[O-144-3]` (Regularisierung im kritischen Streifen); vgl. XVI-D/P1.4 und P2.2 |

### F.5 — Bilanz des Registers

| Test | Stand NEU-114 | Stand NEU-221e | Verschiebung |
|---|---|---|---|
| 114.1 | `❓[O]` | `❓[O]` | keine |
| 114.2 | `❓[O]` | $\checkmark[M]_{\mathrm{neg}}$ (kanonischer Weg) | **negativ entschieden, Reparaturpfade benannt** |
| 114.3 | `❓[O]` | $\checkmark[M]_{\mathrm{part}}$ | **Teilergebnis: Vierschichtensatz, $\Theta_{1/2}$ extern** |
| 114.4 | `⚠[M]` | gesperrt | **Blockade lokalisiert: `[O-144-1]`** |

Drei der vier Tests haben sich bewegt, ohne dass es verbucht wurde. Test 114.1 ist der
einzige, der seit dem 1. Juli tatsächlich unberührt geblieben ist.

---

## XVI-G — Pflege dieses Blattes

### Verbindliche Regel

> Jedes neue NEU-Dokument, das eine Bedingung an $X$, an eine seiner Projektionen oder an
> einen Realisierungskandidaten begründet oder ausschließt, wird **im selben Arbeitsgang**
> hier eingetragen. Ein Eintrag ohne Gültigkeitsetikett und ohne Pfadzuordnung ist
> unvollständig.

### Prüffragen vor jedem Eintrag

1. **Welche Ebene?** Betrifft die Aussage $X$ selbst (XVI-A), die Brücke (XVI-B), eine
   Realisierung (XVI-C) oder nur einen Pfad (XVI-D)?
2. **Welches Etikett?** `global`, `bridge`, `spectral`, `Feshbach`, `HH`, `route-conditional`.
3. **Welcher Umfang?** Was schließt das Resultat **nicht** aus? Dieses Feld ist Pflicht.
4. **Wird ein Kandidat mit einer Klasse verwechselt?** Ein No-Go gegen einen konkreten
   Mechanismus wird nicht zu einem Axiom über $X$ hochgestuft (Sperrregel).
5. **Berührt es einen Rückbindungstest?** Dann XVI-F mitführen.

### Änderungsprotokoll

| Revision | Stand | Wesentliche Änderung |
|---|---|---|
| 1 | NEU-114, 1. Juli 2026 | X.1–X.10, X.neg.1–7, Fünfschicht-Profil, vier Rückbindungstests |
| **2** | **NEU-221e, 26. Juli 2026** | Trennung in drei logische Ebenen; HP-1–HP-7 als Realisierungsbedingungen statt Axiome; Gültigkeitsetiketten und Pfadcodes eingeführt; Sperrregel; XVI-E mit X.neg.8–X.neg.29; XVI-F verbucht die Rückbindungstests; Statuskorrektur zu HP-2 und NEU-56 (VI); Stieltjes-Profil um Spektralmaßinvarianz erweitert (NEU-221e) |

### Offene Baustellen dieses Blattes

- **Test 114.1** ist der einzige nie bearbeitete Rückbindungstest.
- **A.9 (Resonanzkonvergenz)** ist seit Revision 1 unausgeführt.
- **A.11**: Die Zuordnung der Minimalaxiome A1–A7 zur operativen Ebene ist vorgenommen, aber
  A4 (Quasikristall-/Aperiodizitätsprinzip) hat bis heute **kein operatives Gegenstück**.
- Die Entscheidung zwischen den beiden Axiomensystemen ist getroffen (X.1–X.10 führt), aber
  A1–A7 sind nicht formell zurückgezogen.
