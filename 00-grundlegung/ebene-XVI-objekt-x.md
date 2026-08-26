# Ebene XVI — Objekt X: Kanonisches Kontrollblatt (Revision 2, historisch reklassifiziert)

**Revision 2 · Stand: 26. Juli 2026 (NEU-221e) · ersetzt Revision 1 (Stand NEU-114, 1. Juli 2026)**

> **Reklassifikation 2026-08-26 — keine mathematische Promotion oder Rücknahme:**
> Revision 2 bleibt als umfangreiches Constraint-, No-Go- und Provenienzregister erhalten,
> ist aber seit 26. August 2026 **nicht mehr die aktuelle Identitätsdefinition von Objekt X**.
> Insbesondere das untenstehende „definitorische Fünfschicht-Profil“ ist eine historische
> Kandidatenarchitektur des Juli-Standes. Die aktuelle Single Source of Truth ist
> [`00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`](../00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md).
>
> Diese Reklassifikation entwertet **keine** separat bewiesenen route-spezifischen Sätze,
> No-Gos, Brücken- oder Realisierungsbedingungen dieses Blattes. Sie ändert nur den
> ontologischen Status der damaligen Gesamtarchitektur: Aussagen, die „X“ mit dem
> Fünfschichtprofil identifizieren, sind seit 2026-08-26 historisch zu lesen, sofern sie
> nicht separat in die aktuelle Arbeitsdefinition zurückgebunden werden.

---

## Zweck und Gebrauchsanweisung

Dieses Blatt ist **kein Forschungsblatt**, sondern die historische verbindliche Karte der
Revision-2-Katalogarbeit bis zum 26. Juli 2026. Es sammelt an einem Ort die damals gebuchten
Bedingungen, gegen die ein Kandidat für Objekt X geprüft wurde, und hält fest, welche
Bedingung auf welcher logischen Ebene und in welchem Konstruktionspfad galt.

Seit der Reklassifikation vom 26. August 2026 dient es als **Constraint-/Provenienzregister**,
nicht als aktuelle Definition der Identität von X. Für neue Objekt-X-Identitätsaussagen ist
die aktuelle Arbeitsdefinition maßgeblich; route-spezifische Resultate dieses Blattes sind
weiterhin mit ihrer ursprünglichen Provenienz zu zitieren.

**Historische Pflegeregel der Revision 2.** Jedes neue NEU-Dokument, das eine Bedingung an X, an eine seiner
Projektionen oder an einen Realisierungskandidaten begründet oder ausschließt, wurde hier
eingetragen — im selben Arbeitsgang, nicht nachträglich. Ein Eintrag ohne Gültigkeitsetikett
und ohne Pfadzuordnung war unvollständig.

### Die drei logischen Ebenen

Die Revision 1 vermischte Aussagen über $X$ mit Aussagen über seine Realisierungen. Das ist
in Revision 2 korrigiert. Innerhalb dieser historischen Architektur galten strikt getrennt:

$$
\boxed{\text{intrinsische Axiome von } X}
\qquad
\boxed{\text{Brückenaxiome für } \Pi_\gamma(X),\; W_\xi}
\qquad
\boxed{\text{Realisierungsbedingungen für } H_X}
$$

- **XVI-A** enthält die damaligen intrinsischen Identitäts-/Axiomaussagen.
- **XVI-B** die Brückenebene.
- **XVI-C** die Realisierungsebene — insbesondere gehören HP-1–HP-7 dort und **nicht** zu den damaligen Axiomen von $X$.
- **XVI-D** enthält Bedingungen, die nur innerhalb eines bestimmten Konstruktionspfades zwingend sind.
- **XVI-E** ist das Negativregister.
- **XVI-F** führt die Rückbindungstests.

### Gültigkeitsetiketten

Jede Bedingung und jedes No-Go trägt genau eines:

| Etikett | Bedeutung |
|---|---|
| `global` | betraf innerhalb der Revision-2-Architektur Objekt $X$ selbst, unabhängig vom Konstruktionsweg |
| `bridge` | betrifft die Vermittlungsarchitektur $\Pi_\gamma$, $W_\xi$, das Verhältnis von X-Kandidaten zu ihren Projektionen |
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

Diese Sperrregel bleibt auch nach der Reklassifikation uneingeschränkt gültig.

---

## XVI-A — Historische Identitätsarchitektur von Objekt X (Revision 2)

Dieser Abschnitt dokumentiert die damaligen Aussagen, die Revision 2 dem Objekt X selbst
zuschrieb. Seit 2026-08-26 sind sie als **historische Kandidatenarchitektur** zu lesen,
nicht als aktuelle X-Definition.

### A.0 — Historisches definitorisches Fünfschicht-Profil

$$
X = \bigl(A_{2D}^{r},\; [\tilde\omega_2],\; [L_3],\; \mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}},\; m \xrightarrow{\;p\;} pm \bigr)
$$

> **Status seit 2026-08-26:** Die Gesamtidentifikation dieser fünf Schichten mit Objekt X
> ist historisch. Die Statusangaben einzelner Schichten in der folgenden Tabelle sind
> Provenienzangaben der damaligen Route und werden dadurch nicht automatisch geändert.

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

Es existierten zwei Axiomatisierungen. Sie waren **nicht identisch** und wurden in
Revision 2 unterschiedlich geführt:

| System | Quelle | Rolle in Revision 2 / heutige Einordnung |
|---|---|---|
| A1–A7 | `objekt_x_minimalaxiome.md`, 17. Juni 2026, durchgehend `✗[H]` | **Historisches Leitbild.** Motivischer Fernhorizont; nie Prämisse in Beweisen. Seit 2026-08-26 ausdrücklich historischer Kandidatenrahmen. |
| X.1–X.10 / XVI-A | Ebene XVI Revision 2 | **Damals operativ verbindlich für die Katalogarbeit bis 26. Juli 2026.** Seit 2026-08-26 Constraint-/Provenienzregister, nicht aktuelle Identitätsdefinition. |

Die damalige Zuordnung: A1 → A.3, A2 → A.4, A3 → **XVI-C** (nicht XVI-A), A4 → ohne operatives
Gegenstück, A5 → A.3, A6 → A.5 plus XVI-D/P3, A7 → A.2.

Bemerkenswert: **A3 der Minimalaxiome, die spektrale Realisierungseigenschaft, war nach der
Ebenentrennung kein Axiom von $X$ mehr**, sondern eine Realisierungsbedingung. Diese
Ebenentrennung bleibt als historische Buchführungsinformation erhalten.

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

> **Verbindliche Folgerung innerhalb der Revision-2-Architektur:** $\Theta_{1/2}$ darf nicht stillschweigend in die
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

Hier stehen Bedingungen an **Realisierungen** von X-Kandidaten, nicht an der aktuellen
Identitätsdefinition von X. Zwei Profile werden strikt getrennt geführt, weil die damalige
Revision an beiden gleichzeitig arbeitete und sie verschiedene Stärke haben.

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
| P1.5 | Nichtüberzählung: $\dim\ker(1-\mathcal K_\infty(\rho)) = m_\rho$ | — | `❓[O]` NEU-49 Satz 49.3, „Kern-Engpass“ |
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
| P2.3 | Quantitative Schranken im Primschalen-Abel-Lemma; Kancellation „gefährdet nahe $\beta_0\approx s$“ | `❓[O]` NEU-133 |

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
| P4.3 | $Z_g = \{0\}$ für alle $g=m/n\neq 1$ | NEU-210 `[O-210-1]`, Pontrjagin | **`✓[M]` geschlossen** |
| P4.4 | Faktoriales Ursprungspotential $X_N$ mit $\operatorname{Sing}(X)=\{0\}$ | NEU-210 `[O-210-2]` | **`✓[K]` geschlossen** |
| P4.5 | Transportband $P_j \le E_{L_j/k} \le P_{j-k}$; normkonvergente Kommutatoren | NEU-210 `[O-210-3]` | `✓[M]` |
| P4.6 | Geladene äußere Derivation $D_g : A_{\mathrm{alg}}\to A_{C^*}$, nicht $A_{C^*}$-inner | NEU-211 `[O-211-3/4]`, global NEU-217 | `✓[M]` |
| P4.7 | Technische Restknoten `[O-212-5]`, `[O-213-3/5]`, `[O-214-4b]`, `[O-217-1d]` | — | `❓[O]`, keine Existenzentscheidungen |
| P4.8 | Knoten der **verlassenen** Gitterroute: `[O-206-4]`, `[O-207-5b]`, `[O-207-5c]`, `[O-208-5]` | — | `❓[O]`, für die faktoriale Trasse gegenstandslos |

> **Statuskorrektur (NEU-222, 26. Juli 2026).** Revision 2 führte P4 als offenen
> Entscheidungsknoten und „letzten bekannten Konstruktionsweg“. Das war **falsch**:
> `[O-209-5]` und `[O-209-6]` sind seit dem 20. Juli durch NEU-210 geschlossen, und
> `[O-207-5b]` gehört zur verlassenen mehrdimensionalen Gitterroute, nicht zur faktorialen
> Trasse.
>
> **Die singuläre Route wurde beschritten und trägt bis $HH^4$**: NEU-210 (Potential,
> $Z_g=\{0\}$, Transportband) → NEU-211 ($D_g$, Nichtinnerheit) → NEU-212/216 (Zieltyp
> $\mathcal A^\infty$, $\mathcal A^{\log}$) → NEU-217 (globale Nichtinnerheit) →
> NEU-218 (Cup-Aufstieg). Sie endet **nicht** an der Konstruktion, sondern an der
> **Zyklizität** (NEU-219u).
>
> Die kohomologische Schicht von $X$ ist damit **nicht leer**, sondern gebaut und
> blockiert. Der aktive Nachfolgeknoten ist `[O-219-6]` (P3.3), nicht P4.
> Vollständiger Trassenbeleg: [`NEU-222`](../06-hochschild-bc-algebra/NEU-222_Trassenaudit_singulaere_Route_Statuskorrektur_und_offene_Restknoten.md).

### P5 — Vergleichsoperator-/Konfinementpfad

| # | Anforderung | Status |
|---|---|---|
| P5.1 | Vergleichsoperator $\tilde L$ mit $\lVert J^- x\rVert \lesssim \lVert \tilde L x\rVert$ (Schur/Nelson) **und** $\lVert D_{\mathrm{rel}}x\rVert + \lVert x\rVert \ge c\lVert \tilde L x\rVert$ (Konfinement) | `❓[O]` NEU-56 (VI) |
| P5.2 | **Auf dem vollen Raum entschieden (NEU-224 §4):** $(1+D_{\mathrm{rel}}^2)^{-1/2}\notin\mathcal K(\mathcal H_{\mathrm{rel}})$, da der Operator auf dem unendlichdimensionalen $\ker D_{\mathrm{rel}}$ als Identität wirkt. $D_{\mathrm{rel}}$ hat **keinen** kompakten Resolventen auf $\mathcal H_{\mathrm{rel}}$ | **`✗[M]`** |
| P5.2′ | **Auch der reduzierte Fall entschieden (NEU-225).** Auf jeder Primfaser gilt $D_{\mathrm{rel}}\vert_{\mathcal H_{p,a}}\cong 2ic_p\,d/dt$ auf $L^2(\mathbb R)^{\oplus2}$, $c_p=\frac12\gamma_N p\log p$: rein absolutstetiges Spektrum $\mathbb R$, keine Eigenwerte, also $\mathcal H_p\subseteq(\ker D_{\mathrm{rel}})^\perp$. Graphnormbeschränkte Orthonormalfolge explizit | **`✗[M]`** |
| P5.2″ | **Diagnose:** $D_{\mathrm{rel}}$ ist ein **Transportgenerator**, kein Hilbert–Pólya-Operator. Konfinement scheiterte in NEU-56 nicht an der Wahl von $\gamma_N$ oder $L$, sondern strukturell | `✓[M]` |
| P5.3 | **Schichtenverschiebung.** Das kompakte Objekt sollte eine Ebene später entstehen: Feshbach-/Birman–Schwinger-Transfer $K_N(z)=V_N^*(D_{\mathrm{rel}}-z)^{-1}V_N$, $V_p=C_p^{\mathrm{rel}}$ (NEU-51). Dort könnten HP-2, HP-3 ($\mathcal S_2\setminus\mathcal S_1$), HP-5 ($\det_2$) und die zyklische Weyl-Funktion zusammentreffen | `❓[O]` `[O-225-2]` **Arbeitshypothese** |
| P5.3a | **`✓[M]_neg`:** $K_N(z)$ ist bei festem $N$ **nicht** endlich-rangig — jeder Primkanal trägt einen vollen $(r,n)$-Index (51.2/51.3). $\mathcal S_2\setminus\mathcal S_1$ ist bei festem $N$ nicht ausgeschlossen | `✓[M]_neg` |
| P5.3b | Off-Diagonalterme $K_{pq}\neq0$ gesichert (51.5). Mechanismus: **Überlappung der Primkanalbilder** in der BC-Algebra — verschiedene $(p,m)$ treffen dasselbe $V_{pm}$. $D_{\mathrm{rel}}$ bleibt kanalerhaltend | `✓[M]` |
| P5.3c | **`✓[M]_neg`:** (51.3)/(51.4)/(51.7) setzen eine Eigenbasis voraus, die nach NEU-225 nicht existiert (verletzt 52.D0). **Ersetzt durch NEU-227 §2:** $\langle a,K_{pq}(z)b\rangle=\int(\lambda-z)^{-1}d\mu^{a,b}_{pq}$ mit $\mu^{a,b}_{pq}(B)=\langle V_pa,E_D(B)V_qb\rangle$ | **`✓[K/M]`** `[O-226-1]` |
| P5.3f | **Koordinatenwörterbuch `✓[M]`** (NEU-227 §1): $\eta_{p;m;s,u}\leftrightarrow e_{u+ps}V_{pm}$. $r\mapsto r+n$ und $s\mapsto s+m$ sind dieselbe Bewegung. Ein Sprung $R\mapsto R\pm d$ hält die $u$-Klasse genau für $p\mid d$ — im Primsektor ist die Kettenrechnung damit **gerechtfertigt** | `✓[M]` `[O-226-2]` |
| P5.3g | Spurklassekriterium $\lvert D-z\rvert^{-1/2}V\in\mathcal S_2\Rightarrow K_N(z)\in\mathcal S_1$ (Polarzerlegung, NEU-227 §2.5) | `✓[M]` |
| P5.3h | **Abgeleitet:** $\operatorname{Tr}\operatorname{Im}K_N(z)\le\lVert V\rVert_2^2/y$, also ist der Nicht-$\mathcal S_1$-Zeuge **nur möglich, wenn $V\notin\mathcal S_2$**. Notwendig, nicht hinreichend — die Spektralmasse darf nicht zu schnell ins Unendliche entweichen | `✓[M]` |
| P5.3i | **`[O-226-3]` ist kein neuer Knoten (NEU-228).** Die $u$-Summe in (51.2) ist die Entwicklung einer **Hebung** $\widehat\varepsilon_p$: $\Psi_p(\widehat\varepsilon_p)=\Pi_{W_{\mathrm{res}}}\widetilde\omega_2(\widehat\varepsilon_p,L_3^\circ)$ (NEU-153). Also $[O\text{-}226\text{-}3]\equiv[O\text{-}153]\equiv[O\text{-}221\text{-}1c1a0]$ | `✓[M]` |
| P5.3j | **`✓[M]_neg`:** Der Primkanalprojektor $\pi_{\mathrm{prim}}$ selektiert $u=0$; der Faktor $-us\log p$ vernichtet dann die Kopplung, $V_p^{\mathrm{can}}=0$. Eindeutigkeit und Nichtnullheit sind mit ihm **nicht** gleichzeitig erfüllbar. Zulässig ist $\{u\neq0\}$, also unendlich | `✓[M]_neg` |
| P5.3k | Symmetrie-No-Go tritt **nicht** ein: $\pi_{\mathrm{prim}}U_k\neq U_k\pi_{\mathrm{prim}}$, der $p$-Kanal bricht die Fouriertranslation geometrisch | `✓[M]` |
| P5.3l | Auch `[O-226-4]` ist nicht neu: der Gramoperator $g^{(p)}_{uu}$, $g^{(p)}_{0u}$ steht in NEU-153 §D.0.5 und ist dort seit 13. Juli 2026 offen | `❓[O]` |
| P5.3m | **Rücklauf.** Ohne 153.A/B ist $V$ und damit die Schattenklasse von $K(z)$ **hebungsabhängig**. Die neue Hauptlinie läuft in dieselbe Barriere wie die alte — von der anderen Seite. Das erhöht das Gewicht des Knotens: er ist die Wohldefiniertheitsbedingung der gesamten Transferschicht | `✓[M]` |
| P5.3n | **Leerfaser-Risiko.** NEU-153 Z.207: liegt $e_0V_p$ normiert und $\perp\ker\pi_{\mathrm{prim}}$ bei positiv definiter verbundener Form, so ist $\mathcal L_p=\emptyset$ — dann existiert **keine** zulässige Kopplung $V_p$ und die Feshbach-Linie entfällt. Quellenseitig nicht ausgeschlossen | `❓[O]` `[O-228-2]` **zuerst** |
| P5.3d | NEU-77: die Feshbach-Identität ist bei endlichem $N$ **exakt**, der Limes aber nur punktweise, **nicht** normkonvergent (Punkt D); Normierungsfaktor $\lvert S_N\rvert^{-1}$ offen (Punkt E). Schattenklassen sind daher aus den Trunkierungen **nicht** erschließbar | `⚠[M]` |
| P5.3e | Freiheitsgrad: der $u$-Regulator in (51.1). Die Quelle sagt ausdrücklich, diese Wahl entscheide $\mathcal S_1$ gegen $\mathcal S_2$ | `⚠[M]` `[O-226-3]` |
| P5.2a | $\dim\ker D_{\mathrm{rel}} = \infty$ über die Faser $m=1$; $\gamma_N$- und $N$-unabhängig (NEU-224 §3.2/3.3) | `✓[M]` |
| P5.2a′ | **`✓[M]_neg`:** Die flache Achse $r=0$ (NEU-54 §5) ist flache Achse von $\Theta_N$, **nicht** von $J^-=\frac12(\Theta_N-\Theta_N^\dagger)$. Rückwärtskanten aus $r=-n$ tragen $\gamma_N n\log n\neq0$ | `✓[M]_neg` |
| P5.2a″ | **`✓[M]_neg`:** $\mathcal D_0^{\mathrm{eff}}$ nach (55.0) verlangt $r\neq0$ **und** $m>1$ und ist damit echt kleiner als $(\ker D_{\mathrm{rel}})^\perp$ sowie nicht invariant. Korrekt ist $\{m>1\}$ allein | `✓[M]_neg` |
| P5.2a‴ | Primsektoren $m=p$: **kein** Restkern (Impulsoperator hat keine Eigenwerte) | `✓[M]` |
| P5.2a⁗ | Sektoren $m$ nicht prim; Abschlusskontrolle; ist $\mathcal D_0$ ein Kern? | `❓[O]` `[O-225-1/3]` |
| P5.2b | $(\ker D_{\mathrm{rel}})^\perp$ reduziert $D_{\mathrm{rel}}$ **automatisch** (Spektralsatz, NEU-224 §5.1) | `✓[M]` |
| P5.2b′ | Offen bleibt nur: $\overline{\operatorname{Ran}(J_0^-)} = (\ker D_{\mathrm{rel}})^\perp$ (Präabschluss gegen Abschluss) | `❓[O]` |
| P5.2c | Graphnormbeschränkte Orthonormalfolge in $\operatorname{Dom}(D_{\mathrm{rel}})\cap\mathcal H^{\mathrm{eff}}_{\mathrm{rel}}$ konstruieren oder ausschließen (negativer Zeuge bzw. Weyl-Folge) | `❓[O]` `[O-223-2c]` |
| P5.3 | Schur-Test exakt statt heuristisch: $\sup_a\sum_b\lvert\Theta_{ba}\rvert/\ell(a)<\infty$ | `❓[O]` NEU-55 |
| P5.4 | Skalare Normierung $\gamma_N$ ist als Mechanismus verbraucht — P5.1 muss ohne sie auskommen | `✗[M]` NEU-56 Satz 56.2 |

P5 ist der einzige registrierte Zugang zu HP-2 (vgl. C.4), aber nicht der einzig denkbare.

> **Reaudit NEU-56 (NEU-225 §2).** Der Widerspruch in Satz 56.1/56.2 argumentiert
> ausschließlich über **Testvektoren** $\eta_a$ mit festem $r,n$ und benutzt weder Invarianz
> noch Spektralrestriktion. **Satz 56.2 bleibt daher gültig**; korrigiert wird nur die
> Raumbezeichnung. Zurückgerollt ist allein die Aussage, $\{r\neq0, m>1\}$ spanne einen
> reduzierenden oder kernfreien Spektralraum auf. `✓[M]`
>
> **Präzisierung (NEU-223, 26. Juli 2026).** Zwei Befunde aus dem Quellenaudit:
>
> 1. **HP-2 ist für die RH-Hinrichtung nicht erforderlich.** NEU-56 §4: Für
>    $\mathrm{Spec}\subset\mathbb R$ genügt die Selbstadjungiertheit; der Engpass entscheidet
>    nur über den *Typ* des Spektrums. P5 betrifft ausschließlich das HP-Profil (XVI-C.1).
> 2. **Die $\tilde L$-Klasse ist auf einen Kandidaten reduziert.** (N1) verlangt $L$ groß,
>    (K) verlangt $L$ klein; zusammen erzwingen sie $L\simeq\lvert D_{\mathrm{rel}}\rvert$
>    (NEU-56 §1). NEU-56 §7 benennt daraufhin $\tilde L = (1+(J^-)^2)^{1/2}$, wodurch (K)
>    trivial wird und die Verträglichkeitsbedingung entfällt.
>
> **G3 ist damit keine Suchaufgabe nach einem Vergleichsoperator mehr, sondern eine
> Spektralfrage:** Ist $(1+D_{\mathrm{rel}}^2)^{-1/2}$ kompakt auf $\mathcal H^{\mathrm{eff}}_{\mathrm{rel}}$?
>
> **Zwei Präzisierungen (Rev. 2).** Erstens ist die Reduktion eine **Graphnormklasse**, keine
> Operatorgleichheit: $\lVert\tilde Lx\rVert+\lVert x\rVert \asymp \lVert\lvert D_{\mathrm{rel}}\rvert x\rVert+\lVert x\rVert$.
> Es können formal verschiedene $\tilde L$ darin liegen; für die Kompaktheit ist das
> unerheblich, da graphnormäquivalente Einbettungen gleichzeitig kompakt sind. Der Suchraum
> kollabiert auf **eine Kompaktheitsfrage**, nicht auf einen Operator. Zweitens ist der in
> NEU-56 §7 genannte Ausdruck $(1+(J^-)^2)^{1/2}$ **typwidrig**: wegen $(J^-)^*=-J^-$ (54.3)
> gilt $(J^-)^2=-D_{\mathrm{rel}}^2$, also $1+(J^-)^2=1-D_{\mathrm{rel}}^2 \not\ge 1$.
> Korrekt ist $(1+D_{\mathrm{rel}}^2)^{1/2}$. `✓[M]_neg`
>
> **Umfang eines negativen Ausgangs.** Ausgeschlossen wäre die gesamte erzwungene
> Vergleichsoperatorklasse des gegenwärtigen relativen Jacobi-/Feshbachmodells — **nicht**,
> dass eine anders konstruierte Realisierung $H_X$ HP-2 erfüllt. `[O-223-2]` ist ein binärer
> Strukturtest des HP-Profils (C.1), **keine Sperre** für den Stieltjeskanal (C.2).
> Vollständige Typisierung: [`NEU-223`](../01-primkanten-werkzeuge/NEU-223_Quellenaudit_alternativer_Vergleichsoperator_Schur_Konfinement_und_kompakter_Resolvent.md).

---

## XVI-E — Negativregister

Die folgenden 22 Einträge (X.neg.8–X.neg.29) ergänzen das bestehende Negativregister (X.neg.1–7) um die im Forschungsjournal dokumentierten No-Go-Resultate aus den Katalogabschnitten 01 bis 07. Jeder Eintrag trägt genau ein **Gültigkeitsetikett**: `global` (betraf innerhalb der Revision-2-Architektur X selbst, wegunabhängig), `bridge` (betrifft die Vermittlungsarchitektur zwischen X-Kandidaten und ihren Projektionen/Interfaces), `spectral` (betrifft die spektrale Realisierung \(H_X\), Spurtyp, Determinantenebene oder Schattenklasse), `Feshbach` (nur im Primkanten-/Feshbach-/Selbstenergiepfad gültig), `HH` (nur solange die kohomologische Schicht Bestandteil der Konstruktion ist) oder `route-conditional` (nur unter zusätzlichen Modellannahmen eines konkreten Kandidaten). Das Feld „Betroffener Konstruktionspfad“ referenziert die fünf Wege P1 (Feshbach-/Primkantenpfad), P2 (Selbstenergie-/Mangoldtpfad), P3 (HH-/zyklische Kohomologie), P4 (singuläre Potentialroute), P5 (Vergleichsoperator-/Konfinementpfad) sowie P0 für pfadunabhängige Aussagen. Die Sortierung folgt der Reichweite: zuerst wegunabhängige (`bridge`, `spectral`), dann pfadgebundene Einträge. Jeder Eintrag benennt explizit, welchen *konkreten* Kandidaten oder Mechanismus er trifft und was er ausdrücklich nicht ausschließt — pauschale Verallgemeinerungen zu Axiomen über die aktuelle Arbeitsdefinition von X sind unzulässig.

---

### X.neg.8 — Kategoriale Trennung X ≠ m_arith

**Quelle:** `NEU-114` · **Gültigkeit:** `bridge`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Die direkte Gleichsetzung von Objekt X mit der aus NEU-77–113 konstruierten arithmetischen Weyl-Herglotz-Funktion \(m_{\mathrm{arith}}\) als *identisches* Objekt (nicht nur als Bild einer Abbildung von X). |
| **Exakte Hypothesen** | Es wird lediglich die kategoriale Verschiedenheit der Konstruktionsebenen unterstellt: \(m_{\mathrm{arith}}\) ist ein eindimensionales, RH-äquivalentes Herglotz-Objekt; X ist in der damaligen Architektur fünfschichtig und kohomologisch-kategorial höherstufig. Keine weiteren Zusatzannahmen (kein Parameterbereich, kein Algebrentyp) nötig — die Aussage ist eine reine Typfeststellung innerhalb dieser Architektur. |
| **Umfang** | Schließt nur die *Identität* \(X = m_{\mathrm{arith}}\) aus. Es bleibt ausdrücklich zulässig, dass \(m_{\mathrm{arith}} = \Pi_\gamma(X)\) gilt, also dass \(m_{\mathrm{arith}}\) eine echte Projektion von X auf eine "spektrale γ-Achse" ist — sofern die Rückbindung der oberen Schichten (\([\tilde\omega_2]\), \([L_3]\), \(\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}\), Primkanten) gelingt. |
| **Positive Folgerung** | X muss über eine explizite Projektionsabbildung \(\Pi_\gamma\) vermittelt werden, die erst nachträglich (nach Rückbindungstest) mit \(m_{\mathrm{arith}}\) identifiziert werden darf. Dies erzwingt für die damalige X-Architektur eine echte Mehrschichtigkeit, die nicht auf die Spektralschatten-Spur reduzierbar ist. |
| **Betroffener Konstruktionspfad** | P0 (betrifft die Systemarchitektur der Rückbindung, unabhängig vom gewählten Konstruktionsweg). |

---

### X.neg.9 — Kategorialer Schutzsatz Wres^top ≠ Q_Weil

**Quelle:** `NEU-115` · **Gültigkeit:** `bridge`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Die direkte Gleichsetzung der Spurform-Schicht der damaligen X-Architektur, \(\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}\) (eine lineare Spur-/Distributionsform), mit der bilinearen Weil-Quadratform \(Q_{\mathrm{Weil}}\) der Explizitformel. |
| **Exakte Hypothesen** | Reine Gradbedingung: \(\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}\) ist linear, \(Q_{\mathrm{Weil}}\) ist quadratisch/bilinear. Der Ausschluss gilt unabhängig vom konkreten Inhalt beider Objekte — es handelt sich um eine typtheoretische, nicht um eine inhaltliche Aussage. Keine weitere Voraussetzung nötig. |
| **Umfang** | Schließt nur die *direkte* Gleichsetzung beider Formen aus, nicht die Existenz eines Zusammenhangs zwischen ihnen. Insbesondere nicht ausgeschlossen: ein lineares Zwischenobjekt \(W_\xi\) (Weil-Distribution auf dem Paley-Wiener-Raum), das erst durch Pairing mit sich selbst (Faltung, \(Q_{\mathrm{Weil}}[f] = \langle W_\xi, f^\ast\ast f\rangle\)) zur Quadratform wird. |
| **Positive Folgerung** | Innerhalb der damaligen Architektur musste die Spurform-Schicht über ein eigenständiges lineares Interface \(W_\xi\) vermittelt werden; \(\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}} \stackrel{?}{=} W_\xi\) blieb der präzisierte offene Anschlusstest. |
| **Betroffener Konstruktionspfad** | P0. |

---

### X.neg.10 — Triviales Zentrum der C*-BC-Algebra und keine globale Bimodul-Retraktion

**Quelle:** `NEU-215` · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | (a) Jedes nichttriviale zentrale Element der \(C^*\)-vervollständigten Bost-Connes-Algebra \(A_{C^*}\); (b) jeder stetige globale \(A_{\mathrm{alg}}\)-Bimoduloperator \(R: A_{C^*}\to\mathcal A^\infty\) mit \(\mathcal A^\infty\subsetneq A_{C^*}\) als *echtem* Teilraum. |
| **Exakte Hypothesen** | Voraussetzungen der Beweiskette: \(C(\widehat{\mathbb Z})\) ist MASA in \(A_{C^*}\) (topologisch freie \(\mathbb{Q}_+^\times\)-Wirkung, Amenabilität, Eckpunktübertragung); \(\sigma_k\)-Invarianz aus \([f,\mu_k]=0\); Faktorialkonvergenz \(j!\cdot y\to0\). Zusatzkorrektur gegenüber früherer Fassung: \(A_{C^*}\) ist *nicht* einfach — der frühere Schluss „injektiv ⟹ treu“ war unzulässig und wurde zurückgenommen. |
| **Umfang** | Schließt nur nichttriviale *zentrale* Elemente und *globale, stetige, echte* Bimodul-Retraktionen aus. Schließt nicht jede Art von Unterraumkonstruktion aus — lokale, nicht-globale oder unstetige Konstruktionen sowie Konstruktionen auf der algebraischen (nicht \(C^*\)-vervollständigten) Algebra \(A_{\mathrm{alg}}\) selbst sind nicht erfasst. |
| **Positive Folgerung** | Die Hochschild-Konstruktionen, sofern sie als Kandidatenroute weiterverwendet werden, dürfen sich nicht auf zentrale Cup-Faktoren oder globale Retraktionen stützen. |
| **Betroffener Konstruktionspfad** | P3 (HH-/zyklische Kohomologie). |

---

### X.neg.11 — Hilbertraumspur-No-Go für die archimedische Gamma-Komponente

**Quelle:** `NEU-220e` · **Gültigkeit:** `spectral`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Die Realisierung der archimedischen Gamma-Rohform \(\Lambda_\Gamma(h)\) als gewöhnliche Hilbertraumspur \(\mathrm{Tr}_{B(L^2)}(\gamma_\infty(H_\infty)h(H_\infty))\) eines Operator-Funktionalkalküls. |
| **Exakte Hypothesen** | Strukturell, unabhängig vom Abklingverhalten der Testfunktion \(h\): Unter der Mellintransformation wird der Operator zum Multiplikationsoperator \(M_{\gamma_\infty h}\) auf dem nichtatomaren Maßraum \((\mathbb R, dt)\); Multiplikationsoperatoren mit \(a\not\equiv0\) sind dort nie kompakt, insbesondere nicht spurklassig. Keine Zusatzbedingung an \(h\) erforderlich. |
| **Umfang** | Schließt nur die gewöhnliche (\(\mathcal S_1\)-)Hilbertraumspur dieser konkreten archimedischen Komponente aus. Schließt nicht die Existenz einer semifiniten Spur aus — diese wird tatsächlich erfolgreich konstruiert (\(\Lambda_\Gamma(h)=\frac1{2\pi}\tau_\infty(\gamma_\infty(H_\infty)h(H_\infty))\) mit der n.f.s.-Spur \(\tau_\infty\) auf \(L^\infty(\mathbb R,dt)\)). |
| **Positive Folgerung** | Für jede Route, die diese Gamma-Rohform verwendet, muss die archimedische Komponente als semifinite statt gewöhnliche Hilbertraumspur behandelt werden; der intrinsische geometrische/streutheoretische Ursprung der Digammafunktion bleibt offen. |
| **Betroffener Konstruktionspfad** | P2. |

---

### X.neg.12 — Normierungsbruch zwischen Spurklasse und Mangoldt-Spur

**Quelle:** `NEU-140` · **Gültigkeit:** `spectral`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Die direkte Identifikation „T1“: \(|c_p|^2=\log p\), also die Hoffnung, dass die Kanalnorm \(|c_p|^2 = \mathrm{Tr}_{\mathcal S_1}(C_p^{\mathrm{rel}}(C_p^{\mathrm{rel}})^\sharp)\) selbst unmittelbar die Mangoldt-Gewichtung trägt. |
| **Exakte Hypothesen** | Beruht auf der bewiesenen oberen Schranke \(|c_p|^2=O((\log p)^2/p)\) (NEU-135.D). Daraus folgt für große \(p\): \(|c_p|^2/\log p = O(\log p/p)\to 0\) — die Schranke selbst ist unbedingt bewiesen (\(\times[F]\) für T1 direkt), keine weiteren Modellannahmen nötig. |
| **Umfang** | Schließt nur die *ungedämpfte* Identifikation \(|c_p|^2=\log p\) für große \(p\) aus. Schließt nicht aus, dass die gewöhnliche Spur \(\mathrm{Tr}(\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta))\) eine *gedämpfte* Mangoldt-Spur liefert, die durch einen zusätzlichen Renormierungsoperator wiederhergestellt werden kann. |
| **Positive Folgerung** | Die betreffende Spurklassenroute benötigt einen zusätzlichen Renormierungsoperator \(R_p=\log p/|c_p|^2\); die reine Spurklassennorm allein trägt die arithmetische Gewichtung nicht. |
| **Betroffener Konstruktionspfad** | P2. |

---

### X.neg.13 — Notwendige Unbeschränktheit der Mangoldt-Renormierung im kritischen Streifen

**Quelle:** `NEU-141` · **Gültigkeit:** `spectral`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Ein *beschränkter*, primkanaldiagonaler Renormierungsoperator \(R\) (mit \(R_p=\log p/|c_p|^2\)), der die Mangoldt-Spur exakt und im gewöhnlichen Spurklassensinn für den gesamten Bereich \(0<\Re\beta\le1\) korrekt gewichtet. |
| **Exakte Hypothesen** | Bedingt auf zwei Annahmen: (1) \(R\) ist primkanaldiagonal (setzt T2-Orthogonalität voraus, selbst offen); (2) die Wachstumsschranke \(R_p\gtrsim p/\log p\) aus NEU-140/NEU-135.D. Unter diesen Annahmen gilt zusätzlich: \(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\in\mathcal S_1\) im Mangoldt-Sinn \(\iff \Re\beta>1\). |
| **Umfang** | Schließt nur beschränkte, primkanaldiagonale Renormierungsoperatoren aus und nur die gewöhnliche Spurklassentheorie für \(0<\Re\beta\le1\). Schließt nicht aus, dass eine regulierte Spur (analytische Fortsetzung, resolventenartige Regularisierung, Hadamard-Renormierung) im kritischen Bereich funktioniert; schließt auch nicht die biorthogonale Renormierung aus, falls T2-Orthogonalität scheitert. |
| **Positive Folgerung** | Im RH-relevanten Bereich benötigt diese Route einen unbeschränkten Renormierungsoperator und eine regulierte Spur. |
| **Betroffener Konstruktionspfad** | P2. |

---

### X.neg.14 — Nilpotenz-Barriere des isolierten Mangoldt-Jacobi-Operators

**Quelle:** `NEU-86` · **Gültigkeit:** `spectral`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Der isolierte, rein vorwärtsgerichtete (strikt oberdreieckige) Mangoldt-gewichtete Jacobi-Operator \(J_N^\Lambda\) auf endlichem \(\ell^2(I_N)\) als Träger einer nichttrivialen Spur-/Determinantenstruktur. |
| **Exakte Hypothesen** | Gilt für \(J_N^\Lambda\) in seiner isolierten Form auf endlichem \(N\); \((J_N^\Lambda)^N=0\) ist unbedingt. |
| **Umfang** | Schließt nur die isolierte Vorwärts-Shift-Klasse aus; nicht den Jacobi-Abschluss, relative Determinanten oder echte Feshbach-Schur-Komplemente. |
| **Positive Folgerung** | Spur und Fredholm-Determinante des isolierten Vorwärtsoperators tragen keine arithmetische Information; eine entsprechende Realisierungsroute muss symmetrisieren oder Schur-komplementieren. |
| **Betroffener Konstruktionspfad** | P2. |

---

### X.neg.15 — Direkt-Summen-Obstruktion des kollektiven Birman-Schwinger-Operators

**Quelle:** `NEU-50` · **Gültigkeit:** `Feshbach`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Der kollektive Birman-Schwinger-Operator \(K_N\), konstruiert als reine Blockdiagonale \(\bigoplus_p K_p\) über Primkanäle, als Lösung des Nichtüberzählungsproblems. |
| **Exakte Hypothesen** | Reine algebraische Identität: \(\det(1-\mathcal K_N^{\mathrm{diag}})=\prod_{p\le N}\det(1-K_p)\) und \(\ker(1-\mathcal K_N^{\mathrm{diag}}(\rho))=\bigoplus_{p\le N}\ker(1-K_p(\rho))\). |
| **Umfang** | Schließt nur die blockdiagonale Konstruktion aus, nicht kollektiv gekoppelte Feshbach-Formen mit echten Off-Diagonaltermen. |
| **Positive Folgerung** | Der primkanten-basierte Birman-Schwinger-Baustein muss in dieser Route echte Kreuzterme zwischen Primkanälen tragen. |
| **Betroffener Konstruktionspfad** | P1. |

---

### X.neg.16 — Normierungs-No-Go für isometrische Feshbach-Kollaps-Einbettungen

**Quelle:** `NEU-78` · **Gültigkeit:** `Feshbach`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Eine isometrische Einbettung \(U_N:\ell^2(I_N)\to\mathcal H_N\), die den ungewichteten exakten Kollapsoperator reproduziert. |
| **Exakte Hypothesen** | Endliches \(N\) mit \(|S_N|>1\); Einbettungsbedingung und benötigte Kanalgewichte widersprechen einander. |
| **Umfang** | Schließt nur isometrische Kollaps-Einbettungen aus; gewichtete oder explizit renormierte Varianten bleiben offen. |
| **Positive Folgerung** | Die Kollaps-Komponente kann in dieser Route nicht demokratisch-isometrisch sein. |
| **Betroffener Konstruktionspfad** | P1. |

---

### X.neg.17 — Dichtebedingung für simultane Feshbach- und Jacobi-Stabilität

**Quelle:** `NEU-82` · **Gültigkeit:** `Feshbach`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Eine dünne Labelmenge \(\Sigma_N\) als Trägerstruktur, die gleichzeitig Feshbach-Gesamtstabilität und Jacobi-Gewichts-Beschränktheit liefert. |
| **Exakte Hypothesen** | Simultane Forderung von Feshbach-Stabilität und Jacobi-Gewichts-Stabilität erzwingt \(\kappa_N\asymp N\). |
| **Umfang** | Schließt nur dünne Labelmengen aus; die volle Labelmenge bleibt. |
| **Positive Folgerung** | Die Jacobi-Limes-Komponente dieser Route muss auf einer dichten Labelmenge aufbauen. |
| **Betroffener Konstruktionspfad** | P1. |

---

### X.neg.18 — Dreifach-Konflikt Feshbach/Jacobi/Mangoldt auf vollem Orbitbereich

**Quelle:** `NEU-83` · **Gültigkeit:** `Feshbach`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Eine Gewichtsfolge, die auf vollem Orbitbereich gleichzeitig Mangoldt-proportional, Jacobi-beschränkt und Feshbach-stabil ist. |
| **Exakte Hypothesen** | Voller Orbitbereich \(r\le N\); die drei Forderungen erzeugen den dokumentierten Widerspruch. |
| **Umfang** | Orbit-Trunkierung oder andere Normen bleiben offen. |
| **Positive Folgerung** | Die konkrete Route benötigt eine zusätzliche Orbit-/Normstruktur. |
| **Betroffener Konstruktionspfad** | P1. |

---

### X.neg.19 — Trivialität des starken Operatorlimes auf festen Basisvektoren

**Quelle:** `NEU-85` · **Gültigkeit:** `Feshbach`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Der naive starke Operatorlimes des Mangoldt-gewichteten Jacobi-Vorwärtsoperators auf fest getragenen Vektoren. |
| **Exakte Hypothesen** | Für jeden fest getragenen Vektor verschwindet die entsprechende Norm asymptotisch. |
| **Umfang** | Wandernde Fenster, Funktionale, Determinanten und renormierte Testtopologien bleiben unberührt. |
| **Positive Folgerung** | Die Grenzstruktur dieser Route ist nicht im naiven starken \(\ell^2\)-Limes sichtbar. |
| **Betroffener Konstruktionspfad** | P1. |

---

### X.neg.20 — Kein einzelner Skalar stabilisiert zwei divergierende Offdiagonalfolgen

**Quelle:** `NEU-123H` · **Gültigkeit:** `route-conditional`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Ein einzelner skalarer Renormierungsfaktor \(\kappa_N\), der zwei divergierende Offdiagonalfolgen gleichzeitig auf endliche positive Grenzwerte bringt. |
| **Exakte Hypothesen** | Das abstrakte Lemma ist unbedingt; die konkrete Jacobi-Anwendung ist an die dokumentierte Divergenzannahme gebunden. |
| **Umfang** | Gradierte Renormierungen bleiben offen. |
| **Positive Folgerung** | Die konkrete Grenzoperatorroute benötigt eine gradierte statt skalare Renormierung, sofern ihre Hypothesen greifen. |
| **Betroffener Konstruktionspfad** | P2. |

---

### X.neg.21 — Norm-No-Go für verdrehte Nullkozykel bei Re β > 0

**Quelle:** `NEU-182` · `NEU-183` (Quellenaudit) · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Ein nichttrivialer verdrehter Nullkozykel \(u\in Z^0(A_{\mathbb Q}^{\mathrm{alg}}, M_{\sigma_\beta})\), der über den Cup-Weg einen geladenen Vier-Kozykel faktorisieren könnte. |
| **Exakte Hypothesen** | Für \(n>1\), \(\operatorname{Re}\beta>0\), BC-Isometriebeziehungen und treue C*-Einbettung folgt \(u=0\). |
| **Umfang** | Gilt nur für \(\operatorname{Re}\beta>0\) und schließt nur diese Faktorisierungsroute aus. |
| **Positive Folgerung** | Die entsprechende HH-Route kann nicht über einen verdrehten zentralen Nullkozykel-Cup-Faktor laufen. |
| **Betroffener Konstruktionspfad** | P3. |

---

### X.neg.22 — Trivialität des regulären Zentrums der Bost-Connes-Algebra

**Quelle:** `NEU-183` (Zentrumstest) · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Ein nichttriviales homogenes Zentralelement vom Grad \(g\neq1\) als regulärer Cup-Faktor. |
| **Exakte Hypothesen** | Standardpräsentation der BC-Algebra; dokumentierter Zentrumstest. |
| **Umfang** | Schließt die reguläre Zentrumsroute aus, nicht direkte HH-Klassenkonstruktionen. |
| **Positive Folgerung** | Eine HH-Route muss direkte Kozykel-/Quotientenmechanismen statt zentraler Cup-Faktoren verwenden. |
| **Betroffener Konstruktionspfad** | P3. |

---

### X.neg.23 — Augmentationsblindheit der punktierten Potentialroute

**Quelle:** `NEU-196` · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Die dokumentierte punktierte Potentialarchitektur als Quelle der benötigten Augmentationskopplung. |
| **Exakte Hypothesen** | Die dokumentierte Kompaktheits-/Teleskopidentität erzwingt die entsprechende Nullpaarung. |
| **Umfang** | Schließt nicht jede geladene Derivation oder HH-Klasse aus. |
| **Positive Folgerung** | Eine positive Route muss außerhalb dieses Augmentationsmechanismus liegen oder einen anderen Dualzeugen verwenden. |
| **Betroffener Konstruktionspfad** | P4. |

---

### X.neg.24 — Unsichtbarkeit regulärer Potentiale im Kommutatorquotienten

**Quelle:** `NEU-200` · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Global reguläre Potentiale als Quelle einer nichtverschwindenden Klasse im relevanten Kommutatorquotienten. |
| **Exakte Hypothesen** | Dokumentierter expliziter Kommutatorzeuge. |
| **Umfang** | Singuläre Potentiale bleiben offen. |
| **Positive Folgerung** | Ein positiver Befund kann in dieser Route nur aus echtem singulärem Verhalten bei 0 kommen. |
| **Betroffener Konstruktionspfad** | P4. |

---

### X.neg.25 — Ketten-No-Go für die eindimensionale Kettenarchitektur des Bewertungsgitters

**Quelle:** `NEU-207` · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Eine exakte eindimensionale totale Teilbarkeitskette, die mehrere Primrichtungen transportstabil aufnimmt. |
| **Exakte Hypothesen** | Unvergleichbarkeit von \(L/p\) und \(L/q\) für verschiedene Primrichtungen. |
| **Umfang** | Mehrdimensionale oder verzweigte Indexmengen bleiben möglich. |
| **Positive Folgerung** | Die konkrete Route muss in ein mehrdimensionales Bewertungsgitter wechseln. |
| **Betroffener Konstruktionspfad** | P4. |

---

### X.neg.26 — Ausschluss des naiven Sandwichansatzes für geladene Primkanal-Kopplung

**Quelle:** `NEU-209` · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Der naive geladene Kopplungsansatz \(Z_{F,\mathbf N}=\mu_m(\sum_{p\in F}\widetilde X_{p,N_p})\mu_n^*\) mit separierbaren Prim-Singularitäten. |
| **Exakte Hypothesen** | Für jeden nichtverschwindenden Charakterfehlermultiplikator trifft der dokumentierte Hyperflächen-Singularitätsmechanismus. |
| **Umfang** | Der neutrale separierbare Erfolg bleibt bestehen; ausgeschlossen ist die geladene Sandwichkopplung. |
| **Positive Folgerung** | Gesucht ist in dieser Route eine gemeinsame, punktlokalisierte Singularität. |
| **Betroffener Konstruktionspfad** | P4. |

---

### X.neg.27 — Nichtzyklizität des kanonischen Basislifts des geladenen Vierkozykels

**Quelle:** `NEU-219u` · **Gültigkeit:** `HH`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Der kanonische Basislift \(\widetilde L_0\) mit \(\kappa=0,\varepsilon=0\) als Erzeuger einer Klasse in \(HC^4\). |
| **Exakte Hypothesen** | Für \(g\neq1\): \(t\Phi_0=g^{-\beta}\Phi_0\neq\Phi_0\). |
| **Umfang** | Orbitshift, Neutralisation und andere Koeffizientenkategorien bleiben offen. |
| **Positive Folgerung** | Die kanonische Basislift-Route ist geschlossen; alternative zyklische Strukturen wären nötig. |
| **Betroffener Konstruktionspfad** | P3. |

---

### X.neg.28 — Positive invertierbare Kreinraum-Metrik existiert nur unter RH selbst

**Quelle:** `NEU-220t` · **Gültigkeit:** `route-conditional`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | Der naive Kreinraum-Metrik-Reparaturweg im konkreten Nullstellenpaar-Modell. |
| **Exakte Hypothesen** | Modellspezifische Metrikgleichung; off-axis-Paare erzwingen indefinite Signatur. |
| **Umfang** | Schließt nicht jeden denkbaren selbstadjungierten Kandidaten aus. |
| **Positive Folgerung** | Eine nichttautologische positive Realisierung müsste ohne Nullstellenlagen als Eingabedaten konstruiert werden. |
| **Betroffener Konstruktionspfad** | P5. |

---

### X.neg.29 — Schattenklassenzwang gegen die gewöhnliche Fredholm-Determinante des Hilbert-Pólya-Kandidaten

**Quelle:** `NEU-220u` · **Gültigkeit:** `spectral`

| Feld | Inhalt |
|---|---|
| **Ausgeschlossener Kandidat** | \(\Xi(z)/\Xi(0)=\det(I-zH^{-1})\) mit gewöhnlicher Fredholm-Determinante eines hypothetischen HP-Operators mit den Nullstellenordinaten als Eigenwerten. |
| **Exakte Hypothesen** | Riemann-von-Mangoldt-Zählung erzwingt \(H^{-1}\in\mathcal S_2\setminus\mathcal S_1\) in diesem Modell. |
| **Umfang** | Schließt die gewöhnliche \(\mathcal S_1\)-Fredholm-Determinante aus, nicht \(\det_2\) oder quadrierte Determinanten. |
| **Positive Folgerung** | Eine entsprechende HP-Realisierung müsste Carleman-/Quadratdeterminanten verwenden und HP-7 respektieren. |
| **Betroffener Konstruktionspfad** | P5. |

---

## XVI-F — Register der Rückbindungstests 114.1–114.4

NEU-114 (1. Juli 2026) erkannte, dass der Pfad NEU-77–113 nicht $X$ bearbeitet, sondern die
Projektion $\Pi_\gamma(X)$, und richtete vier Tests ein, um den Spektralschatten wieder an
die damalige X-Architektur zu binden. Die Tests wurden geöffnet und danach in keinem der 105 Dokumente ab NEU-117
mehr erwähnt.

Dieses Register schließt die damalige Lücke: Es verbucht, was inzwischen implizit beantwortet ist,
und führt für jeden Test einen Nachfolgeknoten.

$$
\Pi_\gamma\bigl(\mathrm{Wres}^{\mathrm{top}}, [\tilde\omega_2], [L_3], \mathrm{KMS}\bigr)
\;\overset{?}{=}\; m_{\mathrm{arith}} \,/\, Q_{\mathrm{Weil}}
$$

### F.1 — Test 114.1: $HH^2$ $[\tilde\omega_2] \to$ Herglotz-Kanal

| | |
|---|---|
| **Status** | `❓[O]` — unverändert offen innerhalb dieser Route |
| **Frage** | Erzeugt die primäre Hochschild-2-Klasse einen Beitrag zum Herglotz-Kanal von $m_{\mathrm{arith}}$? |
| **Was seit NEU-114 dazukam** | Nichts Direktes. Der 06-Strang arbeitete an $HH^4$, nicht an $HH^2$. |
| **Blockade** | Die Nichttrivialität von $[\tilde\omega_2]$ ist selbst nur Hypothese. |
| **Nachfolgeknoten** | `[O-114-1]` — offen, kein Bearbeiter |

### F.2 — Test 114.2: $HH^4$ $[L_3] \to$ Obstruktionsterm

| | |
|---|---|
| **Status** | $\checkmark[M]_{\mathrm{neg}}$ — **für den kanonischen O-219-Weg** |
| **Was seit NEU-114 dazukam** | Der gesamte Strang NEU-174 – NEU-219z. Der Cup-Aufstieg gelang, der kanonische Basislift ist typkorrekt, aber nicht zyklisch: $t\Phi_0 = g^{-\beta}\Phi_0$. |

> **Reichweite — verbindlich.** Der negative Befund gilt für den **kanonischen Basislift**,
> nicht für jede denkbare $HH^4$-Realisierung. Ausdrücklich nicht ausgeschlossen sind
> Orbitshift-Lifts, Ladungsneutralisation sowie parazyklische, $\sigma$-zyklische oder
> getwistet-zyklische Koeffizientenkategorien.

| | |
|---|---|
| **Nachfolgeknoten** | `[O-219-6]` — Weil-/Gammafaktorpaarung; ferner XVI-D/P3.3 und P4 |

### F.3 — Test 114.3: $\mathrm{Wres}^{\mathrm{top}} \to Q_{\mathrm{Weil}}$

| | |
|---|---|
| **Status** | $\checkmark[M]_{\mathrm{part}}$ |
| **Was seit NEU-114 dazukam** | NEU-116 lieferte den Vierschichtensatz und die Externalität von $\Theta_{1/2}$. NEU-115 trennt linear von quadratisch. |
| **Gesichertes Teilergebnis** | Eine direkte Identifikation ist ausgeschlossen; die damalige Vermittlungsroute lief über mehrere funktorielle Schritte und das lineare Interface $W_\xi$. |
| **Restlücke** | Intrinsizitätstest IT-2 `❓[O]`; weitere Teiltests nicht abgeschlossen. |
| **Nachfolgeknoten** | `[O-116-IT2]`; inhaltlich im NEU-220-Strang fortgesetzt |

### F.4 — Test 114.4: $m \to p^k m \;\Rightarrow\; \Lambda(p^k)$

| | |
|---|---|
| **Status** | **gesperrt durch** `[O-144-1]` |
| **Was seit NEU-114 dazukam** | NEU-141 etabliert $\operatorname{Tr}(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)) = -\zeta'/\zeta(\beta)$ für $\Re\beta>1$, `✓[M]`. |
| **Blockade** | Die T2-Orthogonalität wird zur Voraussetzung erklärt, nicht bewiesen. |
| **Zweite Blockade** | Der kritische Streifen $0<\Re\beta\le 1$ ist unbehandelt, `[O-144-3]`. |
| **Nachfolgeknoten** | `[O-144-1]` und `[O-144-3]`; vgl. XVI-D/P1.4 und P2.2 |

### F.5 — Bilanz des Registers

| Test | Stand NEU-114 | Stand NEU-221e | Verschiebung |
|---|---|---|---|
| 114.1 | `❓[O]` | `❓[O]` | keine |
| 114.2 | `❓[O]` | $\checkmark[M]_{\mathrm{neg}}$ (kanonischer Weg) | **negativ entschieden, Reparaturpfade benannt** |
| 114.3 | `❓[O]` | $\checkmark[M]_{\mathrm{part}}$ | **Teilergebnis: Vierschichtensatz, $\Theta_{1/2}$ extern** |
| 114.4 | `⚠[M]` | gesperrt | **Blockade lokalisiert: `[O-144-1]`** |

Drei der vier Tests bewegten sich innerhalb der damaligen Architektur. Test 114.1 blieb
unberührt. Seit 2026-08-26 sind diese Tests als Provenienz der historischen
Fünfschicht-/Brückenarchitektur zu lesen, nicht als aktuelle Definitionstests von X.

---

## XVI-G — Pflege dieses Blattes

### Historische Regel der Revision 2

> Jedes neue NEU-Dokument, das eine Bedingung an $X$, an eine seiner Projektionen oder an
> einen Realisierungskandidaten begründete oder ausschloss, wurde **im selben Arbeitsgang**
> hier eingetragen.

Seit 2026-08-26 werden **neue Identitätsaussagen zu Objekt X** nicht mehr hier als bindende
Definition gebucht, sondern zuerst gegen die aktuelle Arbeitsdefinition geprüft. Dieses
Blatt bleibt für seine route-spezifischen Constraints und No-Gos zitierfähig.

### Prüffragen vor jeder Weiterverwendung

1. **Historisch oder aktuell?** Ist die Aussage Teil der Revision-2-Architektur oder in die
   aktuelle Objekt-X-Arbeitsdefinition zurückgebunden?
2. **Welche Ebene?** Betrifft sie eine Kandidatenidentität, Brücke, Realisierung oder nur
   einen Pfad?
3. **Welches Etikett?** `global`, `bridge`, `spectral`, `Feshbach`, `HH`, `route-conditional`.
4. **Welcher Umfang?** Was schließt das Resultat **nicht** aus?
5. **Wird ein Kandidat mit einer Klasse verwechselt?** Ein No-Go gegen einen konkreten
   Mechanismus wird nicht zu einem Axiom über X hochgestuft.

### Änderungsprotokoll

| Revision | Stand | Wesentliche Änderung |
|---|---|---|
| 1 | NEU-114, 1. Juli 2026 | X.1–X.10, X.neg.1–7, Fünfschicht-Profil, vier Rückbindungstests |
| **2** | **NEU-221e, 26. Juli 2026** | Trennung in drei logische Ebenen; HP-1–HP-7 als Realisierungsbedingungen statt Axiome; Gültigkeitsetiketten und Pfadcodes; Sperrregel; erweitertes Negativregister und Rückbindungstests |
| **2R** | **26. August 2026** | **Reklassifikation ohne mathematische Promotion/Rücknahme:** Fünfschicht-Identität und Revision-2-Axiomensystem historisiert; Blatt bleibt Constraint-/No-Go-/Provenienzregister. Aktuelle X-Definition nach `00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`. |

### Offene historische Baustellen dieses Blattes

- **Test 114.1** wurde innerhalb der Revision-2-Route nie bearbeitet.
- **A.9 (Resonanzkonvergenz)** blieb unausgeführt.
- **A.11**: A4 des alten Leitbilds hatte kein operatives Gegenstück.
- Diese Punkte sind seit der Reklassifikation **keine automatisch aktuellen Objekt-X-
  Identitätsknoten**; sie werden nur dann wieder aktiv, wenn eine heutige Konstruktion die
  entsprechende historische Route ausdrücklich reaktiviert.
