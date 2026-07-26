# Changelog

Sitzungsprotokoll des Objekt-X-Programms, neueste Einträge zuerst.

> **Aktueller Stand: NEU-223 — 26. Juli 2026**

Die Einträge ab NEU-162 sind aus der Commit-Historie des Arbeitsjournals rekonstruiert und
zu thematischen Blöcken zusammengefasst. Für Details siehe die jeweiligen Dokumente über
den [Gesamtindex](INDEX.md).

---

## [NEU-223] — 26. Juli 2026: Vergleichsoperator, Schur, Konfinement, kompakter Resolvent

**Quellenaudit NEU-52–56. Zwei Befunde ändern die Zielnormalform.**

1. **HP-2 ist für die RH-Hinrichtung nicht erforderlich.** NEU-56 §4: Für
   $\mathrm{Spec}\subset\mathbb R$ genügt Selbstadjungiertheit; der Engpass entscheidet nur
   über den Spektraltyp. G3 betrifft ausschließlich das HP-Profil.
2. **Die $\tilde L$-Klasse ist quellenseitig auf einen Kandidaten reduziert.** (N1) verlangt
   $L$ groß, (K) verlangt $L$ klein, zusammen $L\simeq\lvert D_{\mathrm{rel}}\rvert$
   (NEU-56 §1). NEU-56 §7 nennt $\tilde L=(1+(J^-)^2)^{1/2}$: (K) wird trivial, die
   Verträglichkeitsbedingung entfällt.

Vier Aussagen strikt getrennt: Selbstadjungiertheit (N1)/(N2), Vergleichsoperatorabschätzung,
Konfinement (K), kompakte Einbettung. Die Trennungsregel (54.SEP) stand bereits in NEU-54.
Konstanten sind **nicht** uniform in $N$; (55.16) wächst wie $\gamma_N m\log m$.

Verbrauchte Freiheitsgrade: skalares $\gamma_N$ (A, A′), separables $m$-Gewicht (B1 —
partielles Konfinement nur in der $r$-Achse), $L$-Rekalibrierung (B2 — rettet Schur, ruiniert
(K)). Abgeleitet: Rekalibrierungen scheitern in **beiden** Ordnungsrichtungen.

Typkorrektur: $s_k(J^-)$ ist für unbeschränktes $J^-$ nicht definiert. Relevantes Objekt ist
$(1+(J^-)^2)^{-1/2}$; die Zielnormalform kollabiert auf dessen Kompaktheit auf
$\mathcal H^{\mathrm{eff}}_{\mathrm{rel}}$. Ein negativer Ausgang wäre eine erheblich
stärkere No-Go-Klasse als NEU-56.

Sperrvermerk: „$D_N$ diskret $\Rightarrow$ $D_\infty$ kompakt resolvent" ist unzulässig.

Nachfolgeknoten `[O-223-2]`. XVI-D/P5 entsprechend korrigiert.

---

## [NEU-222] — 26. Juli 2026: Trassenaudit der singulären Route — Statuskorrektur

**Reines Quellenaudit. Ergebnis: Die als offen geführte Entscheidungsfrage war überholt.**

`[O-209-5]` und `[O-209-6]` sind seit dem 20. Juli durch NEU-210 geschlossen
($Z_g=\{0\}$ exakt via Pontrjagin; faktoriales Ursprungspotential mit
$\operatorname{Sing}(X)=\{0\}$). `[O-207-5b]` gehört zur verlassenen mehrdimensionalen
Gitterroute; die faktoriale Kette erreicht Normkonvergenz direkt über das Transportband
$P_j \le E_{L_j/k} \le P_{j-k}$ und fällt damit in die von NEU-207 ausdrücklich
offengelassene Klasse der approximativen Ketten.

**Die singuläre Route trägt bis $HH^4$:** NEU-210 → 211 ($D_g$, Nichtinnerheit) →
212/216 (Zieltyp) → 217 (globale Nichtinnerheit) → 218 (Cup-Aufstieg). Sie endet an der
**Zyklizität** (NEU-219u), nicht an der Konstruktion.

Korrigiert: Ebene XVI XVI-D/P4 (führte geschlossene Knoten als offen und P4 als
Entscheidungsknoten), Bestandsaufnahme §4.1 („kohomologische Schicht steuert auf Leere
zu" — zurückgenommen) und die G4-Priorisierung (entfällt; G3 rückt auf Rang eins).

Verbleibend offen auf der Trasse: `[O-212-5]`, `[O-213-3/5]`, `[O-214-4b]`, `[O-217-1d]` —
technische Restknoten, keine Existenzentscheidungen.

---

## [NEU-221e] — 26. Juli 2026: Hebungsfaser, Wres-Quotient, Spektralmaßabstieg

**Typaudit des Kopplungsvektors. Das exakte Abstiegskriterium ist bewiesen, seine
Verifikation gesperrt. `[O-221-1c1a]` steigt von `?[O]` auf `✓[M]_part`.**

Die Kernkorrektur: Weil NEU-46 den relativen Vektor als **zyklischen** Vektor einer
Weyl-Funktion verwendet, ist die Hebungsfrage **nicht** durch Normgleichheit entschieden.
Verschieden gewählte, gleich normierte Hebungen können verschiedene Resolventenmatrixstellen,
Spektralmaße und inverse Momente erzeugen.

Drei Ebenen werden getrennt: algebraische affine Liftfaser $\widehat\varepsilon_p^{\,0}+K_p$ ·
exakt zulässige normierte Liftmenge $\widehat{\mathcal E}_p^{\mathrm{adm}}$ ·
Wres-Quotientbildung im **relativen** Zielraum.

| Ergebnis | Status |
|---|---|
| Exaktes Abstiegskriterium $\widetilde T_p^{\mathrm{raw}}(\Delta_p^{\mathrm{adm}}) \subseteq \mathcal N_{\mathrm{Wres,rel}}$ | `✓[M]` |
| Roh- und quotientierte Kopplung typologisch getrennt: $T_p^{\mathrm{rel}} = Q_{\mathrm{Wres,rel}}\circ\widetilde T_p^{\mathrm{raw}}$ | `✓[K]_part` |
| $\Delta_p^{\mathrm{adm}} = \mathcal A_p^{\mathrm{adm}} - \mathcal A_p^{\mathrm{adm}}$ ist die **Differenzmenge**, im Allgemeinen echt größer als $\mathcal A_p^{\mathrm{adm}}$ (157.2) | `✓[M]` |
| Ungeladener Rohkandidat $e_0V_p$ ausgeschlossen — $\widetilde T_p^{\mathrm{raw}}(e_0V_p)=0$ | `✓[M]_neg` |
| Rang-eins-Bildstabilisator ist $U(1)$ — nur im **positiven** Hilbertraumfall | `✓[M]` konditional |
| Verifikation des Abstiegs auf $\Delta_p^{\mathrm{adm}}$ | **gesperrt** |
| Beschränktheit/Rang von $T_p^{\mathrm{rel}}$ auf ganz $B_{3,p}^{\mathrm{lift}}$ | `?[O]` |
| Spektralmaßinvarianz, Liftstabilisator, intrinsische Sektion | `?[O]` |

Vier Typkorrekturen gegenüber dem Vorentwurf: das Wres-Radikal muss **vor** dem Quotienten
formuliert werden; $K_p$ ist nicht die Menge zulässiger Hebungsänderungen; der Zielraum muss
der **kantenmarkierte** relative Raum sein; Rang eins und Beschränktheit von
$C_p[\widehat\varepsilon_p]$ folgen aus dem eindimensionalen Definitionsraum und sagen nichts
über die Rohabbildung.

Typwarnungen: Bei indefiniter Form ist das Radikal **nicht** die Menge isotroper Vektoren.
Der Schluss $C_pC_p^{\#}=C_p'C_p'^{\#} \Rightarrow \Psi_p'=e^{i\theta}\Psi_p$ setzt die positive
Hilbertrealisierung voraus.

Nächster atomarer Knoten: `[O-221-1c1a0-admissible-difference-locus-and-raw-relative-coupling]`.

Parallel: **Ebene XVI Revision 2** — das Axiomenregister wurde von Stand NEU-114 auf NEU-221e
nachgezogen und in ein Kontrollblatt mit drei logischen Ebenen umgebaut.
Siehe [`00-grundlegung/ebene-XVI-objekt-x.md`](00-grundlegung/ebene-XVI-objekt-x.md).

---

## [NEU-221 – NEU-221d] — 26. Juli 2026: Adelische Momentquelle

**Ziel: eine adelische Quelle für die positive Momentfolge des Hankel-Kriteriums.
Zwischenstand — die Quelle ist noch nicht konstruiert, aber die fehlenden Bestandteile sind
exakt benannt.**

| Eintrag | Ergebnis | Status |
|---|---|---|
| NEU-221 | Sichtung vorhandener BC-/KMS-Quellen; erster normalisierter positiver Weil-Momentkandidat | `✓ [K]` |
| NEU-221c | Zyklischer Feshbach-Weyl-Kandidat, quadratische Resolvente, Normierungs-Firewall für den Quellvektor | `✓ [K]` |
| NEU-221d | Direktextraktion aus NEU-46: $D_N^{\mathrm{rel}}$ ist selbstadjungiert, aber $(\mathcal H_N^{\mathrm{rel}}, D_N^{\mathrm{rel}}, \Psi_N)$ ist **noch kein vollständig typisiertes zyklisches Tripel** | `✓ [M]_part` |

Offen nach NEU-221d: Typisierung von $\varepsilon_p, \Psi_p$ als konkrete Hilbertvektoren,
quellseitige Fixierung von $\lVert\Psi_N\rVert$, Nullmodusfreiheit $E_{D_N^{\mathrm{rel}}}(\{0\})\Psi_N = 0$,
Endlichkeit der inversen Momente $\int\lvert\lambda\rvert^{-2k-2}d\mu_{\Psi_N}$ für $k=0,1,2$
sowie die vollständig gekoppelte endlich-archimedische Geometrie.

---

## [NEU-220 – NEU-220w] — 25.–26. Juli 2026: Weil-Explizitformel bis Hankelpositivität

**Der bislang stärkste Strang. Endet mit einer unkonditionalen RH-Äquivalenz.**

### Archimedischer Faktor (NEU-220 – 220g)

| Eintrag | Ergebnis |
|---|---|
| NEU-220 / 220a | Quelltyp und Zielraum des Gammafaktors; zentrierte Mellin-Koordinate, Involutionskompatibilität |
| NEU-220b | Gamma-Symbol als temperierte Distribution konstruiert |
| NEU-220c / 220d | Repository-Audit der Weil-Normierung; Trennung von Pol- und Gammaanteil, Korrektur des rohen Polterms auf der kritischen Linie |
| NEU-220e | **No-Go:** gewöhnliche Hilbertspur unzureichend — $\Lambda_\Gamma$ verlangt eine semifinite Spur |
| NEU-220f / 220g | Gamma-Symbol als archimedische Streuphasenableitung; typkorrekte Zusammenführung endlicher und archimedischer Spurformen |

### Konturtransport und Weil-Form (NEU-220h – 220m)

| Eintrag | Ergebnis |
|---|---|
| NEU-220h / 220i | Endlicher Weil-Port aus NEU-28; Zeta-Quotient als endlicher Streufaktor ausgeschlossen |
| NEU-220j / 220k | Holomorpher Weil-Testkern, Konvergenz der Nullstellensumme, Horizontalabschätzung; Xi-Masterkontur mit exakten Vorzeichen, Faktor 2 und Polbuchhaltung ohne Doppelzählung trivialer Nullstellen |
| NEU-220l | Weil-Quadratform über zentrierte Autokorrelation typisiert; RH-Positivität von der Spektralrealisierung getrennt |
| NEU-220m rev.2 | Gesamt-Weilform auf der Testfunktions-Rigging; Korrektur von Pol- und Primpolarisierung, Gammadomänen, indefiniter Abschließbarkeit |

### Grenztyp und Krein-Raum (NEU-220n – 220t)

| Eintrag | Ergebnis |
|---|---|
| NEU-220n – 220p | Endliche Fensteroperatoren selbstadjungiert; Randflucht bewiesen; globale Spur nicht abschließbar; erweiterter Graphenraum konstruiert |
| NEU-220q | Prim-Pol-Renormierung; RH-äquivalentes Temperiertheitskriterium |
| NEU-220r | Fourier-Nullstellenmaß identifiziert; Lebesgue-$L^2$-Multiplikator ausgeschlossen; bedingtes Spektralmodell |
| NEU-220s rev.2 | Unkonditionales Nullstellenpaar-Kreinmodell; RH als Kollaps zur positiven Metrik; Korrektur der Multiplizitäts-Doppelzählung |
| NEU-220t | Vollständige Klassifikation der Metrikblöcke; **Off-Axis-Trägheit, Positivitäts-No-Go, Similarity-No-Go**; beschränkte Similarity zu positiver Metrik ist RH-äquivalent |

### Hankel-Kriterium (NEU-220u – 220w)

| Eintrag | Ergebnis |
|---|---|
| NEU-220u | Spektraldeterminantenklasse von $\Xi$ fixiert; **gewöhnliche Spurklassen-Determinante ausgeschlossen**; Resolventenspur als Ziel |
| NEU-220v rev.2 | Xi-Determinante als Stieltjes-Resolventenspur; Hankel-Positivitätshierarchie; Korrektur der Quadratnullstellen-Implikation |
| **NEU-220w** | **Vollständige Hankel-Hierarchie ist RH-äquivalent** — beide Richtungen bewiesen; Moment-GNS-Weyl-Modell; Quantisierung des semifiniten Spektralmaßes |

$$\mathrm{RH} \iff H_N^{(0)}\succeq 0 \ \text{ und }\ H_N^{(1)}\succeq 0 \quad \forall N\ge 0, \qquad \mu_k = -\frac{k+1}{(2k+2)!}(\log\Xi)^{(2k+2)}(0).$$

---

## [NEU-219 – NEU-219z] — 22.–25. Juli 2026: O-219-Strang und No-Go-Theorem

**Der längste geschlossene Strang des Programms. Ergebnis: ein starkes negatives
Strukturresultat, das die Zyklizitätsobstruktion exakt lokalisiert.**

| Block | Ergebnis |
|---|---|
| NEU-219 – 219d | KMS-Typaudit: $\omega_\beta(\eta_{q,P})=0$ negativ; getwisteter Quotient; expliziter Neutralisierer; $\omega_{\beta,\chi}(\sigma_P(G_q))>0$ für $\beta>1$; Ladungseigenkochain $T_\sigma\Phi = g^{-\beta}\Phi$ |
| NEU-219e – 219g | Externe Eigenlinie; unitales Bimodul negativ; parazyklisches Koeffizientenobjekt offen; Hopf-Typbruch Komodul vs. Modul; SAYD-Stabilität vs. Ladung negativ — Dilatationspfad wird primär |
| NEU-219h – 219l | Automorphe Dilatation der $\rho_n$; Laca-Dilatation mit $\tau = \gamma_g\circ\sigma_\beta$; adelischer Lift des Koeffizientenmoduls; Multiplikator-, Paarungs- und Morita-Audit; exakter algebraischer Eckkern |
| NEU-219m – 219q | Orbit-Direktheit negativ; orbit-markierte Ersatzrealisierung und KMS-Modulgewicht; Multiplikator-Shift ausgeschlossen; dreiparametriger Auditrahmen $C(g,\beta,\lambda) = \lambda^\varepsilon g^{s\beta}$; Orbitindexfunktion $\kappa$ |
| NEU-219r – 219t | Kanonischer Basislift $\tilde L_0$: Erstdefinition, Kozykelerhalt, $\kappa = 0$, $\varepsilon = 0$; vollständige $U_{g^{-1}}$-Buchführung; **$s = -1$ global bewiesen** |
| **NEU-219u** | **No-Go-Theorem O-219:** $\tilde L_0 \in Z^4(A_{\mathrm{alg}}, I_0)$ typkorrekt, aber $t\Phi_0 = g^{-\beta}\Phi_0$ mit $g^{-\beta}\neq 1$ — keine gewöhnliche zyklische Klasse in $HC^4$ |
| NEU-219v – 219z | Nachaudits: typwidrige $U$-Eingaberotation ausgeschlossen; (R1)–(R3) als unzureichend erkannt (Fall D); $D_g$-Primärformel und Zieltypbrücke über NEU-211/216/217; Unit-Slot-Zeuge $\mu_P^*$; Finalaudit mit DAG-Export und Rollback-Vermerk |

Konsequenz: Der Pfad `[O-219-6]` — Weil-/Gammafaktorpaarung — wird zum neuen Hauptpfad
und eröffnet den Strang NEU-220.

---

## [NEU-216 – NEU-218] — 21.–22. Juli 2026: Koeffiziententyp und Cup-Aufstieg

| Eintrag | Ergebnis | Status |
|---|---|---|
| NEU-216 rev.1–6 | Logarithmischer Koeffiziententyp $\mathcal B^{\log}$ vollständig auditiert: kanonisches Schalenmittel $m_j$, radiale Seminorm, Faktorialband $C_\sigma(k)$, Supportschwelle $J(k)$, Band-Mittelwertlemma mit scharfen Konstanten, submultiplikative Norm **ohne Renormierung**, $T_a := \sigma_a$ kanonisch, $\mathcal A^{\log}$ konstruiert, $D_g(A_{\mathrm{alg}})\subseteq\mathcal A^{\log}$ | `✓ [M]` |
| NEU-217 rev.1–3 | Lokaler $p$-Block: Typisierung $N/S/H_p$, Gradkonflikt $\delta_p$ vs. $D_g$ fixiert, Faithfulness-Negativresultat, koordinatenfreie $\delta_p^{(0)}$ via Gaugewirkung | `✓ [K/M]` |
| NEU-217 `[O-217-2b/2c]` | gcd-Fallzerlegung, lokale Defekträume, Bimodulstabilität, lokale Nichtinnerheit via Normdivergenzbeweis (Gradpaarargument gestrichen) | `✓ [M]` |
| NEU-217 `[O-217-2c-6]` | Lokal-globaler Klebeknoten: Zwei-Punkt-Trennungszeuge für $\sigma_q$ und $\rho_q$, intrinsische Konstruktion, **globale Nichtinnerheit** — Grad-1-Pfad geschlossen | `✓ [K/M]` |
| NEU-218 | Grad-3-Partner und geladener Cup-Aufstieg; Eingabealternierung widerlegt; Korrekturaudit rollt die Baker-Gewichtstrennung zurück, schließt die Nica-Formel positiv; `[SO-Q_sigma]` via Følner-Wachstumsargument geschlossen — **Cup-Aufstieg $HH^4$ vollständig** | `✓ [M]` |

Zusätzlich: `KONVENTIONEN.md` angelegt und die $\rho_k$-Fourierform verbindlich fixiert.

---

## [NEU-195 – NEU-215] — 19.–21. Juli 2026: Derivationen, Potentiale, Bimodul-No-go

| Eintrag | Ergebnis | Status |
|---|---|---|
| NEU-195 | Bewertungsderivationen; Reduktion auf eine atomare $HH^1$-Frage; Routen A/B | `✓ [M]` / `✓ [M]_neg` |
| NEU-196 / 200 | Augmentationsblindheit: reguläre Potentiale sind im Kommutatorquotienten unsichtbar | `✓ [M]_neg` |
| NEU-197 / 199 | Universeller Dualdetektor, Kommutatorquotient $Q_{h,p}$; Generatorformel $D_g^H(\mu_k)$, Obstruktionspfeil-Quotiententest | `✓ [M]` |
| NEU-201 – 203 | Singuläres Potential $H_{\mathrm{sing}}$ als Testkandidat; **Revisionsaudit: alle drei Beweisschritte negativ** — $H_{\mathrm{sing}}$ nicht wohldefiniert, KMS-Test unzulässig; korrigiertes Singularitätskriterium über Projektionsdifferenzen | `✗ [M]` |
| NEU-204 / 205 | Dyadische Schalen: neutrale unbeschränkte äußere Derivation $A_{\mathrm{alg}}\to A_{C^*}$; geladener/algebraischer Zieltyp negativ; geladener dyadischer Twist, naive Linksverschiebung ausgeschlossen | `✓ [M]` / `✓ [M]_neg` |
| NEU-206 – 210 | Biorthogonale geladene Partialisometrieschalen; Bewertungsgitter und **Ketten-No-go**; separierbare Primpotentiale und Refinementstabilität; **Charakterkern-No-go**; faktoriale Ursprungssingularität und Charakterabsorption | `✓ [K/M]` / `✗ [M]` |
| NEU-211 – 213 | Nichtteilerfremder Faktorialaudit und geladene äußere Derivation; Zieltypbrücke über das intermediäre Koeffizientenmodul $\mathcal A^\infty$; Revisionsaudit korrigiert Rechen- und Leibniz-Typfehler | `✓ [M]` |
| NEU-214 rev.2 / 215 rev.4 | Bimodul-Rigiditätslemma und glattes Potential $X_N^\infty$; Zentralisatorbeweis, MASA via topologisch freier $\mathbb Q_+^\times$-Wirkung, $Z(A_{C^*}) = \mathbb C 1$ — **globaler Bimodul-No-go, verschärft zu $R=0$** | `✗ [M]` |

---

## [NEU-174 – NEU-194] — 18.–19. Juli 2026: Hochschild-Komplex und geladene HH⁴-Klasse

| Eintrag | Ergebnis |
|---|---|
| NEU-174 / 175 | Minimaler Hochschild-Komplex mit induzierter BC-Zeitwirkung; Gewichtraumkomplex und geladener Kettenprojektor; Korrekturen: Modellwahl $B_3^{\mathrm{mod}}$, reguläres Bimodul, $\alpha_t\circ\sigma = \sigma\circ\alpha_t$ |
| NEU-176 / 177 | Konstruktion einer nichttrivialen geladenen 4-Kohomologieklasse; direkter Kozykeltest und gewichteter Dualzyklus für $L_{3,\lambda}$; Statuskorrektur zu NEU-176 |
| NEU-178 | **Vier-Prim-Polynommodell:** explizite geladene $HH^4$-Klasse und Dualzyklus; schließt `[O-177-1..7]` im lokalen Modell, eröffnet den Transferknoten zu $A_{\mathbb Q}$ |
| NEU-179 – 181 | Transfertriage; $\mathbb Q_+^\times$-Gradierung und Primvaluationsderivationen; Homogenitätsaudit und algebraischer Modular-Twist $\sigma_\beta$; typisierte Cup-Route mit Leibnizregel |
| NEU-182 / 183 | **Nullkozykel-No-go:** $Z(A_{\mathbb Q})_g = 0$ für $g\neq 1_\Gamma$ (regulär) und $Z^0(A,{}_{\mathrm{id}}A_{\sigma_\beta}) = 0$ für $\Re\beta>0$ (verdreht); Zentrumstest, Strukturbruch, $\Omega_{\mathbf p}$-Auswertung |
| NEU-184 – 187 | Koeffizientenaudit für $Z(A_{\mathbb Q})_g$; Augmentationscharakter und Dualzyklus; geladener Sektor von $HH^4$; **Restriktionssatz** für geladene äußere Derivationen mit Gruppenalgebra-Reduktion, $H^1(G,B_\rho)\neq 0$ |
| NEU-188 | Erweiterungsobstruktion punktierter Gruppenkozykel; vollständiges Relationssystem (E3)/(E7); `[O-188-4]` **konditional** aufgelöst |
| AUDIT 2026-07-19 | Fortschrittsbilanz-Korrektur: Trennung von regulärer und verdrehter Nullkozykelroute, Äußerlichkeit nur konditional, Operatorbrücke als nächste Pflichtdisziplin |
| NEU-189 / 190 | Typaudit der Operatorrealisierung von $[\Omega_{\mathbf p}]$; vollständiger Audit NEU-1–188 nach typisierter Operatorbrücke — negativer Quellenbefund bestätigt |
| NEU-192 – 194 | Zeugenarchitektur, Separationssatz und Warnlemma für invariante Spuren; geladener Dualzyklus $z_{-\lambda}$ konstruiert, Randtest geschlossen; Paarung $\neq 0$; determinantisches Modell als Kozykel ausgeschlossen |

---

## [NEU-162 – NEU-173] — 15.–18. Juli 2026: Zeugenroute L₃° und Typfundament

**Ergebnis des Stranges: Die Zeugenroute über $L_3^\circ$ ließ sich nicht schließen. Die
Quellenkegel-Audits legten offen, dass die Fourierladung nie konstruktiv fixiert wurde —
ein negativer, aber präziser Befund, der den Übergang zur kohomologischen Route auslöste.**

| Eintrag | Ergebnis |
|---|---|
| NEU-162 – 164 | Quantoren- und Zulässigkeitstest für $L_3^\circ = e_1V_1$; Einmodenzeuge, Liftmitgliedschaft, Nichtnullkante; $R_{p,j}$-Test mit drei Ausgängen A/B/C und $U_p^{\mathrm{adm}}$ |
| NEU-165 / 165a / 165b | Import der $R_{p,j}$-Wirkung, Matrixstruktur, Basisnullmengen, gemeinsamer Kern; Quellenregister; **Konsistenzaudit: $R_{p,j}$ in NEU-157 nur postuliert (Klasse 4)** — führt zu NEU-157 rev.3 |
| NEU-166 / 166a / 166b | Ein- und Zweimoden-Test; Typ-, Domänen- und Deszentaudit von $\tilde T_p$; Rollen- und Provenienzentscheidung mit Stop-Regel $u = 1-p$, vier Endbefunden und Sperrmarken |
| NEU-167 / 167b | Lineare Kernbedingungen vs. offene Fourierladungsbedingung; `[O-167-2]` **negativ geschlossen** — $A_p = \emptyset$ im auditierten Quellenkegel |
| NEU-168 / 169 | Nichtverschwindensgeometrie der exakt zulässigen Liftmenge; Kollisionssystem und Einzelmoden-Nichtverschwindung von $B_p$ |
| NEU-170 / 170a – 170c | Gewichteter Träger von $L_3^\circ$; Klassen- und Repräsentantenaudit — **negativer Quellenbefund**; NEU-28 ist Spur-/Normierungsquelle, **kein Fourierimport** |
| NEU-170d | Vollständiger bereinigter DAG-Stand nach Direktaudit NEU-20/26/28/29/161/162/170a–c |
| NEU-171 – 173 | Typfundament der $L_3$-Klasse und ihres Fouriergrades; Direktaudit NEU-72/170b; Delta-Audit NEU-20/28 und Abschluss des Typfundament-Quellenkegels |

---

## Frühere Einträge (bis NEU-161 rev.5)

Das ursprüngliche Sitzungsprotokoll bis zum 15. Juli 2026 ist unverändert erhalten:
[CHANGELOG_alt.md](CHANGELOG_alt.md).
