# N*Jp-Aufbau und Spike-Orthogonalität: Stufen 1–4 (2026-10-16)

**Status:** AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN / RESEARCH_BRANCH_UNMERGED. Art: DIAGNOSTIK mit gerichtet zertifizierten Teilstücken (Stufe 1 Schale, Stufe 3 endliche U8-Antwort) und hochpräzisen Gleitkomma-Diagnosen (Stufen 2 und 4). Kein Zertifikat des N12-Tests, keine Aussage über A9→A11, Objekt X oder RH.

Dieses Paket setzt den Nachtrag von `a9-inverse-spike-calibration-2026-10-15` fort (Budgetpaket `7f712994…beb1f5e`, N*Jp-Paket `b48e3895…6d57b`) und bindet die Antwortdaten aus `a9-a11-whole-response-gram-2026-10-15` (Archive `b8677c0b…f41ee`, `00a66e85…ed0a0`).


## Korrekturen (2026-10-17, nach Gegenprüfung durch Prüfpaket `1ccb6be1…99b0`)

Die folgenden Formulierungen der Erstfassung (PR #228) waren zu weit und gelten als **ÜBERHOLT**; die Details stehen in `reports/STUFE4_TEIL2_HOCHPAARUNGEN.md` §1:

1. „Spike-Richtung ist A9-orthogonal zu den zwölf alten Quellen" → belastbar ist nur: ⟨χ_v, A9Φ_j⟩ ist numerisch sehr klein (Mittelpunkte 10⁻⁷…2,4·10⁻⁴); keine exakte Orthogonalität.
2. Der Energie-Cauchy–Schwarz-Test in 4a verwendete die **Untergrenze** u₁ᵀ(F + H_B/δ)u₁ als Obergrenze. Auf **Modellniveau** mit A₀ (`a8_model.json.gz`) neu gerechnet: u₁ᵀA₀u₁ = 1,3355573·10⁻²⁶ / 8,5312837·10⁻²⁴ (A₀ = F + H_B/δ bis 2,5·10⁻³³); ohne Gamma-Modellfehler e_A = 1,36·10⁻²⁸ und ohne gerichtete I_j ist das kein tatsächlicher CS-Nachweis. Der tatsächliche Rayleigh-Anschluss stammt aus den beiden rationalen Zeugen des Pakets `f0bdfe69…` (Rayleigh-Quotienten in [1,321892; 1,349065]·10⁻²⁶ bzw. [8,531120; 8,531393]·10⁻²⁴); die alten Verhältnisse 0,02–0,16 bleiben Diagnose.
3. „L²-Größen 10¹³/10³¹ sind Koordinatenartefakte" → falsch: die Normen im festen physischen Raum sind isometrie-invariant und echt groß (weiche A8-Mode, bedingt ‖A9⁻¹‖ > 7,4·10²⁵ / 1,17·10²³); sie erzwingen nur keine große Paarung mit einem bestimmten Residuum.
4. „Hoher U8-Anteil ≲ 10⁻³" aus Quadraturnormen war ungerichtet; gerichtet gilt jetzt ‖u_hi,v‖ < 0,016 / 0,00245 (Prüfpaket 1ccb6be1…, Replay PASS).
5. „Der untere N12-Test kann aus dem D12-Anteil praktisch nicht scheitern" → nicht gefolgert (Antwortmatrix T mit ‖T‖ < 6,8·10⁶, C_p-Kopplung ungerechnet).

Neu (Teil 2): die zwölf hohen Paarungen r_{v,j} = (1/δ)⟨y_f − B*c, y_{h,j}⟩ sind über die ganze Funktion A8(Φc) berechnet: |r_{v,j}| ≤ 7,3·10⁻⁵ (gerade), ≤ 2,4·10⁻⁴ (ungerade), alle 24 innerhalb der diagnostischen Vergleichswerte, gebildet aus den angezeigten Hochantwortfaktoren 0,0159 bzw. 0,00245 und ungerichteten Quadraturnormen ‖y_h‖ (0,0159 ist keine nach oben gerundete Schranke). Mittelpunkte ℓ_v(D_j): 10⁻⁷…4,5·10⁻⁵ (gerade), ≤ 2,4·10⁻⁴ (ungerade). Die Zahlen r_{v,j} und ℓ_v(D_j) sind Quadratur-Mittelpunkte ohne gerichteten Rest. Die Budgetsummen 0,6 (gerade) bzw. 0,015 (ungerade) nach (7.1) sind **keine gerichteten Obergrenzen** (Kernnorm ‖h8‖ statt ‖D_j‖_{H9}, fehlende Reste und D̂-Term), sondern unvollständige Größenordnungsdiagnosen. Der Rayleigh-Test ist mit dem Modellgram A₀ nur auf Modellniveau repariert (Gamma-Fehler e_A = 1,36·10⁻²⁸ fehlt); der gerichtete Anschluss mit zwei rationalen Zeugen liegt im Paket `f0bdfe69…8880` (tatsächliche Rayleigh-Quotienten < 1,349065·10⁻²⁶ / 8,531393·10⁻²⁴; bedingt ‖A9⁻¹‖ > 7,4·10²⁵ / 1,17·10²³). ‖χ_e‖ < 25317,73 (gerade) bzw. 88,2 (ungerade). Sichere Kernaussage: unter den gebundenen Voraussetzungen ist die ganze hohe U8-Norm für v, p, e kontrolliert und der D12-Modellfehler im Rang-eins-Skalartest bezahlbar; die 24 Paarungen liefern kleine numerische Werte, deren gerichtete Intervalle und Kombination mit T offen bleiben. Details: `reports/STUFE4_TEIL2_HOCHPAARUNGEN.md` §0.

## 0. Gegenstand und Notation

Alte Schale X = L²((a₈,a₉), 2dx) mit a₈ = (3/2) log 2, a₉ = log 3; Kern (0,a₈); H9 physischer Momentnullraum auf (0,a₉); m = cosh(x/2) (gerade) bzw. sinh(x/2) (ungerade); μ = ∫₀^{a₈} m²; λ(s) = ∫_{a₈}^{a₉} m s. Quellen F = (z_{σ+2}, z_{σ+4}, z_{σ+6}, z_{σ+8}, ΛY₁…ΛY₈), U8 die Common96-Majorante, N die Quellentransformation (FUNKTIONSANSCHLUSS.txt §6 des N*Jp-Pakets). Für t ∈ {v, p = P_upper v}:

- r_t = Jt, k_t = K12⁻¹ a_fin r_t, ψ_t = Λr_t − F k_t,
- f_t = Π8[Q^np_{a₉} ψ_t]|(0,a₈), χ_t = ψ_t − J_old U8 f_t = N*Jt,
- ℓ_t(h) = ⟨χ_t, h⟩ für h ∈ H9; der untere N12-Test lautet ⟨Rz, W9 Rz⟩ ≥ (11/(10q))|ℓ_p(Rz)|² mit Rz = Cz − D12 Tz.

## 1. Stufe 1: Schalenteil (gerichtet zertifiziert durch Paket `940cd40e…dd49`)

χ_t|(a₈,a₉) = r_t − Σᵢ Fᵢ|Schale · k_{t,i} ist unabhängig von U8. Einschließungen (unter den geerbten Voraussetzungen):

| Parität | ‖χ_v|Schale‖_X | Sprung j_v = ψ_v(a₈⁺) − ψ_v(a₈⁻) |
|---|---|---|
| gerade | 2013,598122 … 2013,598426 | −2848,129905 … −2848,129854 |
| ungerade | 2199,971192 … 2199,971205 | −2824,085937 … −2824,085934 |

Die Schalenfunktion ist eine Randschicht an a₈ (gerade: −22588 bei a₈⁺, −0,016 bei a₉⁻). Zwei Korrekturen gegenüber dem ersten Diagnoselauf sind integriert: λ_total = λ(r) **−** Σⱼ k_{4+j} λ(Yⱼ) (Kernmomentkoeffizient; Gesamtmoment ∫₀^{a₉} m ψ = 0 bis 10⁻³⁶) und p = αv + e mit α = q/‖v‖², e ≠ 0 (relativer Rest 1,06·10⁻¹⁴ / 8,0·10⁻¹⁵), also ℓ_p = αℓ_v + ℓ_e. Kontrollidentität: ∫_Kern m χ_t = −λ(s_t), ‖χ_t‖² = W_X[s_t] + ‖z_t‖². Aus (6.4) des A9-Inversbeweises folgt ‖W9‖ ≥ (11/(10q))‖χ_p|Schale‖² > 2,52·10¹¹ / 4,98·10¹⁰ (Majorante; keine Fehlerobergrenze, keine Aussage über A9⁻¹).

## 2. Stufe 2: Innere Quelle f_v (Diagnose, mpmath 22 Stellen)

Q^np_{a₉} = H_Γ − κ − S (Kern k(r) = e^{−r/2}/(1−e^{−2r}), κ = log 8π + γ + π/2, Verschiebungen q = 2,3,4,5,7,8) auf die paritätisch fortgesetzte ψ_v, dann Kernrestriktion und Π8. Operator validiert gegen Indikatorfunktionen (10⁻²⁵), den Fourier-Multiplikator Re ψ(¼+iξ/2) − ψ(¼) (5·10⁻²⁶) und die Identität ½∫[Pₙ(x)−Pₙ(y)]/|x−y| dy = HₙPₙ (10⁻²⁶).

| | gerade | ungerade |
|---|---|---|
| ‖f_v‖_{H8} | 237738,801 | 268775,540 |
| Log-Randterm (j/2)·log(a₈−x), Konstante | −127122,52 | 204686,01 |
| Aufhebung ‖κψ‖/‖f_v‖ | 147 | 72 |
| Anteil Grade > 61 (Parseval, grob) | ≈617 | ≈714 |

f_v hat neun innere Sprungstellen bei x ∈ {log q − a₈, log q − a₉, a₈ − log 2, a₉ − log 2} mit Sprüngen w_q·(±j_v) (bis ±2400) und eine logarithmische Singularität an a₈. Die 191 Paarungen Φ*f_v stimmen auf drei unabhängigen Wegen überein (eigene Quadratur plus Mellin-Korrektur, GPT-1-Evaluator mit analytischer Logabspaltung, Archivmodelle c_J t − c_F k₀ aus Common96): ≤ 10⁻⁶ bzw. 2,8·10⁻¹⁰.

## 3. Stufe 3: Endliche U8-Antwort (gerichtet zertifiziert durch Paket `ab7116f7…6b52`)

Mit c = E*U(U8 f) = C·Cᵀd/(1−ρ), d = Φ*f − B·T_h f/δ, alle Eingaben aus den archivierten Ganzquellenmodellen: ‖c_v‖ = 1,345361·10¹³ (gerade) / 1,022029·10¹² (ungerade) mit zertifizierten Fehlern 5,2·10¹⁰ / 8,5·10⁷ (gemeinsamer k-Fehler als K-Ellipsoid, Quellfehler). Daraus ‖χ_v‖_{H9} > 1,34·10¹³ / 1,02·10¹² und ‖W9‖ > 1,11·10³¹ / 1,07·10²⁸ (Majorante). Unabhängige Nachrechnung von c₀ mit 60 Stellen reproduziert den Archivmittelpunkt bis 3·10⁻³².

Struktur (eigene SVD-Diagnose): C ist obere Dreiecksmatrix mit größtem Singulärwert 8,83·10¹² (gerade); der Kopf F_neu = (CCᵀ)⁻¹ hat Eigenwert ≈1,28·10⁻²⁶ zur Mode u₁ (dominante Gewichte in den Graden 2–12; vollständige 191-dimensionale Richtung), und c liegt zu 99,99 % in u₁. Die Kopplung u₁·d ≈ 1,7·10⁻¹³ ist in doppelter Genauigkeit nicht auflösbar. Min-Max (Rückzugsverträglichkeit): λ_min(A9) ≤ a_low[Φu₁] ≈ 1,34·10⁻²⁶, also ‖A9⁻¹‖ ≳ 7,5·10²⁵ (bedingt; zu prüfen).

## 4. Stufe 4 (Teil 1): Paarungen der Spike-Richtung mit den zwölf alten Quellen (Diagnose, mpmath 150 Stellen) — **Formulierungen teilweise ÜBERHOLT, siehe Korrekturen**

**4a. Energie-Cauchy–Schwarz-Test der geerbten Kette.** Für D_j = A9Φ_j (FUNCTIONS12.json, Horizont a₉) und Φu₁ (Common96, Horizont a₈) muss |⟨Φu₁, D_j⟩| = |a9[JΦu₁, Φ_j]| ≤ √(a_low[u₁])·√(A12_jj) gelten; a_low[u₁] ≥ u₁ᵀ(F + H_B/δ)u₁ = 1,336·10⁻²⁶ (gerade) / 8,53·10⁻²⁴ (ungerade) **[ÜBERHOLT als Schranke: Untergrenze; auf Modellniveau mit u₁ᵀA₀u₁ neu gerechnet (gleicher Zahlenwert, ohne Gamma-Fehler); voller Anschluss nur über `f0bdfe69…`, siehe Korrekturen Nr. 2]**. Gemessen: I_j ∈ [−1,5·10⁻¹⁴, 9,4·10⁻¹⁵] (gerade), [−4,9·10⁻¹³, −9,0·10⁻¹⁴] (ungerade); Verhältnis zur Schranke 0,02–0,17 in allen 24 Fällen; naive Skala ‖Φu₁‖‖D_j|Kern‖ ≈ 0,4–2,1. Rückzugsverträglichkeit und Positivität sind damit zwischen beiden Horizonten numerisch konsistent (Diagnose); der u₁-Anteil von ℓ_v(D_j) beträgt ‖c‖·I_j = O(0,1).

**4b. Hoher Anteil der U8-Antwort.** Aus H_B ≥ BB* (Common96) exakt: ‖B*c‖² ≤ cᵀH_Bc = 18289,12103 (gerade) / 21630,51668 (ungerade). Unabhängig: ‖y_f‖² = ‖f‖² + γ_m a_f² − ‖Φ*f‖² = 18289,12054 / 21630,55051 und ⟨B*c, y_f⟩ = ⟨c, B·T_h f⟩ = 18289,12079 / 21630,53358 (Archiv). Folglich ‖y_f − B*c‖² ≤ 3,1·10⁻⁶ / 2,6·10⁻⁵ bei exaktem ‖f‖²; wegen der Quadraturgenauigkeit von ‖f‖² (12 übereinstimmende Stellen zweier Evaluatoren, ≈ ±0,6 absolut auf ‖f‖²) konservativ ‖y_f − B*c‖ ≤ 0,8. Der hohe Anteil (y_f − B*c)/δ von U8 f_v ist also ≲ 10⁻³ (konservativ ≲ 0,5) gegen ‖Φc‖ = 1,3·10¹³: U8 f_v ≈ Φc.

**4c. ℓ_v(D_j).** Exakt gilt ℓ_v(D_j) = [⟨ψ_v, D_j⟩ − ⟨c, Φ*h8_j⟩] − ⟨y_f − B*c, y_h⟩/δ mit h8_j = Π8(D_j|Kern), y_h dessen hoher Anteil. Die Klammer besteht aus zwei Zahlen bis 1,75·10⁵, die sich in allen 24 Fällen auf 10⁻¹⁰ relativ aufheben (Differenzen 10⁻⁷ … 5·10⁻⁵); der Rest ist durch ‖y_f − B*c‖·‖y_h‖/δ ≤ 0,04–0,15 beschränkt (‖y_h‖ = 0,07–0,27). Die Paarungen ⟨χ_v, A9Φ_j⟩ sind für alle zwölf alten Quellen numerisch sehr klein **[„nahezu orthogonal" ÜBERHOLT, siehe Korrekturen Nr. 1]** — im Einklang mit den Legendrekoeffizienten ~10⁻⁹ von Jv in den niedrigen Graden der alten Schale.

**4d. Deutung [ÜBERHOLT in Teilen, siehe Korrekturen Nr. 3 und 5].** Die L²-Größen 10¹³ (χ_v) und 10³¹ (W9-Untergrenze) werden von der weichen Mode getragen (keine Koordinatenartefakte); in der A9-Energie ist χ_v ein Objekt gewöhnlicher Größe (a8[Φc] = 2,86·10¹⁰ wird von den steifen Moden getragen, die weiche Mode trägt 2,3). Ob der untere Skalartest aus dem D12-Anteil scheitern kann, ist nicht entschieden (Antwortmatrix T, C_p-Kopplung offen); **[ZURÜCKGENOMMEN: „… nicht der Spike"]** welcher Anteil den konservativen N12-Vergleich entscheidet, ist offen; der Beitrag des Spikes im vollständigen Residuum ⟨χ_p, (C_p − D̂T)z₀⟩ ist nicht bestimmt. **[ÜBERHOLT]** Ob U8-Majorante oder K12-Untermatrix aus dieser Richtung ein Hindernis erzeugen, ist nicht entschieden.

## 5. Fehler, Grenzen, nicht Behauptetes

- Stufen 2 und 4 sind Gleitkomma-Diagnosen (22 bzw. 150 Stellen) auf Mittelpunktmodellen; der kohärente k-Fehler Δχ = −(F − J_old U8 g_F)Δk ist nicht transportiert (nach dem Energieargument ≲ η_v·O(1) ≈ 10⁻⁸, aber Erwartung). Der Rest in 4c ist rigoros gegeben c und die Quadraturnormen.
- Nicht berechnet: hohe U8-Antwort als Funktion; ⟨χ_p, Cz⟩ für die neue Schale (a₉, log(11)/2); ℓ_e; K_P[z]; die zwölf N12-Skalare; W9-Energie des Residuums; A9→A11.
- Alle Aussagen setzen die geerbten Operator-, Domänen- und Integrationsvoraussetzungen der gebundenen Pakete voraus (nicht geprüft). Untergrenzen für ‖W9‖ sind keine Fehlerobergrenzen; audit_S bleibt von fixed_X getrennt; kein globaler Abschluss.

## 5b. Stufe 5 (Teil 1): Mittelpunkt des Residualskalars L₀,₀ (Diagnose)

**Korrektur 17.10.2026 — ÜBERHOLT:** Die im folgenden historischen Absatz
angezeigten I₀- und L₀,₀-Mittelpunkte verwenden im ψ-Kernlift irrtümlich μ₉
statt μ₈. `stufe5/l00.py` ist korrigiert und gegen die Stufe-2-Quelle sowie
die Momentidentität des Lifts geprüft. Die betroffenen Zahlen müssen neu
gerechnet werden; der Bericht `reports/STUFE5_L00_MITTELPUNKT.md` dokumentiert
Änderungsformel und Scope. Es liegt weiterhin kein gerichtetes L₀,₀ vor.


Für die exakt W-normierte konstante Schalenrichtung z₀ ist h = Π_a(c̃_σ − D̂Tz₀) aufgebaut (Tz₀ = X_fix·F̂z₀ mit Komponenten bis 2,6·10⁵, ‖D̂Tz₀‖ = 1,37 / 1,20, ‖h‖ = 0,3387 / 0,2948) und der Mittelpunkt I₀ = ⟨ψ_p, h⟩ − ⟨c_p, Φ*h₈⟩ = −3,1194 (gerade) / +4,5923 (ungerade) berechnet; mit dem hohen Rest α·r_v(h) (r_v(h) = 4,2·10⁻⁶ / −2,6·10⁻⁵ aus A8(Φc_v) auf einem h-angepassten Netz, innerhalb der zertifizierten Faktoren) lautet der L₀,₀-Mittelpunkt −3,36 / +4,84 gegenüber den Schwellen 980,11 / 398,77. Der kohärente F-Anteil des k-Fehlers √(b_F*G_p b_F) = 3,5·10⁻⁴ / 1,7·10⁻⁵ ersetzt die nichtkohärente Schranke e_ψ,p‖h‖ = 4751 / 13,4; verbleibendes undirektes Inventar ≈ 205 / 2,9 (ohne Quadraturreste). Alles Mittelpunkte; kein gerichtetes L₀,₀, kein Zertifikat; Details und eigene Fehler in `reports/STUFE5_L00_MITTELPUNKT.md`.

## 6. Reproduktion und Dateien

Gegenprüfungen vom 17.10.2026 gebunden: `94e2bd3b…b16f` (GPT 1, BEFUND mit kohärentem K-Transport, `check_review.py`) und `f0bdfe69…8880` (GPT 2, Rayleigh-Zeugen; Replay in `verify.py`). Nachgereicht am 17.10.: K_P-Paket `87540b07…00d3` (bedingt K_P[z₀] < 18,662828; K_P[s] < 29,603644‖s‖²_W auf dem Schalenpolynomraum Grad ≤ 11; hinreichende Schwellen dist(0, L₀,₀) > 980,113997 gerade / > 398,766496 ungerade, D12-Modellfehler enthalten), Anschlusspaket `77b806b1…` mit exakten rationalen Fehlermetriken G_t = η_t²K⁻¹ (t = v, p; beide Paritäten) und Nachprüfung `3dc06c2b…` (GPT 1). Beide Prüfer repliziert (PASS, je zwei Dateien bytegleich); `verify.py` führt sie als fünften und sechsten Replay. Kein L₀ liegt vor. Weiter nachgereicht: Prüfung von 92a274b (`5110a0eb…`, GPT 1: 24 K-Pivots, 576 Inverseinträge, vier G_t, 26 Budgetgrenzen, 24 Schwellen unabhängig bestätigt; Textpatch hier übernommen) und die elementare Darstellung der neuen Quelle C_σ z₀ = Π_a c̃_σ ohne innere Gamma-Quadratur (`993619be…`, GPT 2: drei elementare Gamma-Primitive Θ, J₊, J₋, alle sieben Primkanäle, zwölf innere Schnittstellen, Randzerlegung c̃ = g·log(a−x) + R; 32 gerichtete Punktwerte, Replay PASS, bytegleich). Für momentnulle w gilt exakt ⟨w, C_σ z₀⟩ = ⟨w, c̃_σ⟩; das ist der Baustein für die C_p-Seite von L₀,₀, noch keine Paarung.

`verify.py` prüft die Hashes aller gebundenen Archive und Dateien, führt die vier gerichteten Prüfer `certify.py` (Stufe 1), `certify_stage3.py` (Stufe 3), `certify.py` des Hochantwort-Pakets (Stufe 4, drei Vorgängerarchive) und `verify.py` des Rayleigh-Zeugen-Pakets sowie die Prüfer des K_P-, des Transportdaten- und des C_p z₀-Quellpakets gegen das im Repository gebundene N*Jp-Brückenarchiv aus und vergleicht deren Ausgaben bytegenau mit den beigefügten Sollwerten. Die mpmath-Diagnosen (`stufe1/`, `stufe2/`, `stufe4/`) werden nicht erneut gerechnet (Laufzeit 10–20 Minuten je Skript); ihre Ergebnisdateien sind hashgebunden. Berichte in `reports/` (Stufe-1-Bericht mit ÜBERHOLT-Markierungen der ersten Fassung).
