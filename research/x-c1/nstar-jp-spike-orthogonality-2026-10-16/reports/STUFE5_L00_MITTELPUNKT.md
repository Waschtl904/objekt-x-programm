# Objekt X — Stufe 5 (Teil 1): Mittelpunkt des Residualskalars L₀,₀ = ⟨χ_p, (C_p − D̂T)z₀⟩ und Fehlerinventar

17. Oktober 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN · Diagnose (Quadratur-Mittelpunkte), kein gerichtetes Intervall

## Nachtrag: Neuberechnung abgeschlossen

Die folgende Korrekturpassage und die alten Zahlen dokumentieren den Stand vor
der Neuberechnung. Aktuell ist [STUFE5_MU8_NEUBERECHNUNG.md](STUFE5_MU8_NEUBERECHNUNG.md):
beide Paritäten neu gerechnet, I₀,p = −3,11964479885967344 / +4,59312241695157234,
Normabweichung numerisch auf grobe Quadratur zurückgeführt. Dieser PR bleibt diagnostisch.

## Korrektur vom 17. Oktober 2026: Kernmasse in ψ

**ÜBERHOLT sind die bisherigen Zahlen für ⟨ψ_t,h⟩, I₀,t und die daraus
abgeleiteten L₀,₀-Mittelpunkte in diesem Bericht, für t = v und p und beide
Paritäten.** Sie wurden mit dem falschen Nenner berechnet. Die historischen
Zahlen und Logs bleiben als Fehlerbeleg erhalten; eine Neuberechnung steht aus.

In `stufe5/l00.py`, Funktion `psi_core`, stand `-lambda_total*m(x)/mu`, wobei
`mu = ∫₀ᵃ⁹ m²`. Der Kernlift Λ benötigt jedoch `mu8 = ∫₀ᵃ⁸ m²`, wie in
`stufe1/PSI_DEFINITION.json` und `stufe2/qnp_psi.py` festgelegt. Der Nenner ist
auf `mu8` korrigiert. Die Verwendungen von `mu` im z₀-Lift und in Πₐ bleiben
korrekt und unverändert.

Für unverändertes h lautet die exakte algebraische Änderung

    ΔI₀,t = -2 λ_total,t (1/μ₈ - 1/μ₉) ∫₀ᵃ⁸ m(x)h(x) dx.

Das gespeicherte `moment_r_tilde` ist ein anderes Moment und darf dafür nicht
eingesetzt werden. Der Vergleich α·I₀,v ≈ I₀,p erkennt den gemeinsamen Fehler
nicht. Die Funktionen h, h₈, ihre Koordinaten, b_F und die getrennt berechneten
hohen Reste werden durch diesen Nennerpatch nicht geändert.

`L00_lower_Pv_{even,odd}.json` kennzeichnen die betroffenen Paarungswerte nun
maschinenlesbar als `RECOMPUTATION_REQUIRED_WRONG_CORE_MASS`; Zahlen wurden
nicht nachträglich als neu gerechnet ausgegeben. Neue Läufe von `l00.py`
speichern den verwendeten Kernhorizont und μ₈ bei jeder Paarung.

Pflichtprüfung dieses Fixes: Python-Syntax, Vergleich des tatsächlichen
`psi_core` mit der Stufe-2-Definition an 24 Punkten (beide Paritäten, beide
Richtungen) sowie die Momentidentität des Einheitslifts in beiden Paritäten;
außerdem Hashbindungen und kanonischer Beweisanker. Die Regression
`python3 stufe5/test_psi_core.py` besteht und schlägt mit dem alten Nenner fehl.
Diese Prüfung ersetzt weder den vollständigen Diagnoselauf noch gerichtete
Quadraturreste. Die unveränderten Zertifikatsreplays sind kein Test von I₀.

Die folgenden Abschnitte dokumentieren den historischen Stand. Aus ihren
alten Mittelpunkten und dem unvollständigen Fehlerinventar folgt derzeit kein
gerichteter Nichtausschluss und keine Bestätigung der Regel.

## 0. Historisches Ergebnis (Mittelpunkte überholt)

Für die exakt W-normierte konstante Schalenrichtung z₀ auf (log 3, log 11/2) ist der Mittelpunkt des Residualskalars
L₀,₀ = ⟨χ_p(k₀), h⟩, h = Π_a(c̃_σ − D̂Tz₀), gleich **−3,36 (gerade)** bzw. **+4,84 (ungerade)**, bei natürlicher Skala ‖χ_p‖·‖h‖ ≈ 2,6·10¹⁷ bzw. 2,8·10¹⁵; die hinreichenden Ausschlussschwellen des K_P-Pakets lauten dist(0, L₀,₀) > 980,113997 bzw. > 398,766496. Die geerbten, nichtkohärenten Fehlerkonstanten ergeben ein undirektes Budget von ≈ 4,96·10³ (gerade; dominiert vom k-Fehler durch F) bzw. ≈ 16,2 (ungerade); mit kohärentem F-Anteil (§4) schrumpft es auf ≈ 205 bzw. ≈ 2,9. **Ein Ausschluss der festen Regel A9_A11_N12_MIDPOINT_INVERSE_60_V1 durch z₀ ist damit nicht in Sicht; ungerade liegt selbst das undirekte Budget um den Faktor ≈ 19 unter der Schwelle.** Ein Ergebnis unter der Schwelle bestätigt die Regel nicht; es ist ein Nichtausschluss für diese eine Richtung.

## 1. Aufbau

Alle Eingaben stammen aus gebundenen Paketen: z₀, c̃_σ (993619be…), D̂ und F̂ (FUNCTIONS12, #227), X_fix (FROZEN_RESPONSE12), ψ_p (Stufe-1-Zertifikat 940cd40e…), c_p = U8-Modellantwort (Stufe-3-Paket ab7116f7…, Richtung lower_Pv direkt), hohe Normschranken (1ccb6be1…), K⁻¹ und G_t (77b806b1…), K_P[z₀] und Schwellen (87540b07…).

1. **z₀ und Lift.** B = 1/√(2(h + L²/μ)), A_c = −BL/μ (Anzeigen gerade 2,11607876508 / −0,204232725671; ungerade 1,94701904125 / −1,00966650682); Normquadrat 1 und Halbintervallmoment 0 auf 10⁻¹⁴⁰ geprüft.
2. **Elementare Quelle c̃_σ** nach (2.1)–(4.1) des Pakets 993619be… (Primitive Θ, J₊, J₋; sieben Primkanäle). Kontrolle: an allen 13 zertifizierten Zellmittelpunkten und am Randkoeffizienten g_σ(a) Abweichung ≤ 3·10⁻¹¹⁶ (gerade) / 2·10⁻¹¹⁶ (ungerade).
3. **Tz₀ = X_fix·F̂z₀** mit (F̂z₀)_j = ⟨f_j, z₀⟩_X = 2B∫_a^b f_j dy über die rohen Riesz-Darstellungen (Polynom + log((v+1)/(v−1))-Multiplikator + Momentterm), 31 geometrisch verfeinerte Zellen zu y = a, 384 Gauss-Knoten. Tz₀ hat Komponenten bis 2,6·10⁵ (gerade; |Tz₀| = 427 937) bzw. 4,4·10⁴ (ungerade; |Tz₀| = 69 257).
4. **D̂Tz₀ = Σ_i (Tz₀)_i D̂_i** mit den gebundenen Modellfunktionen (150 Stellen). Trotz der großen Koeffizienten ist ‖D̂Tz₀‖ = 1,3653 (gerade) / 1,1985 (ungerade): massive Auslöschung, konsistent mit K_P[z₀] < 18,66.
5. **h = Π_a(c̃ − D̂Tz₀)** mit explizitem Moment (∫m·r̃ = −1,49216 / −0,70453). Normen: ‖c̃‖ = 2,3847 / 3,1508; ‖h‖ = 0,338715 / 0,294795; h₈ = Π₈(h|(0,a₈)) mit ‖h₈‖ = 0,338531 / 0,293431; ‖Φ*h₈‖ (191 Koordinaten, 384-Knoten-Zellen) = 0,317655 / 0,274806; ‖y_h‖ = √(‖h₈‖² + γ_m a_h² − ‖Φ*h₈‖²) = 0,117040 / 0,102876.
   Netze: Kern (0,a₈) mit allen zwölf Prim-Schnittstellen von c̃ und den Schnitten von D̂ (13 Zellen × 384 Knoten); Schale (a₈,a) geometrisch mit 39 Stufen zu a (log-Singularität), 40 Zellen × 384 Knoten.

## 2. Zerlegung und Mittelpunkt (Formel (7.1) des Hochantwort-Pakets, D_j → h, v → p)

⟨χ_p, h⟩ = I₀ − r_p,  I₀ = ⟨ψ_p, h⟩ − ⟨c_p, Φ*h₈⟩,  r_p = (1/δ)⟨y_f − B*c_p, y_h⟩ (hoher Rest), |r_p| ≤ H_hi,p‖y_h‖.

| | gerade | ungerade |
|---|---|---|
| ⟨ψ_p, h⟩ | 32 521,953115 | −33 067,135524 |
| davon Schalenanteil | −897 201,09 | 267 027,49 |
| ⟨c_p, Φ*h₈⟩ | 32 525,072496 | −33 071,727861 |
| **I₀** | **−3,119380** | **+4,592337** |
| Kontrolle α·I₀,v (v direkt) | −3,119380 (Differenz 6·10⁻¹¹) | 4,592337 (Differenz 3·10⁻¹¹) |
| r_v(h) über ganze Funktion A8(Φc_v) auf h-Netz | 4,2·10⁻⁶ (Vergleich H_hi,v‖y_h‖ = 1,9·10⁻³) | −2,6·10⁻⁵ (Vergleich 2,5·10⁻⁴) |
| r_p ≈ α·r_v(h) (+ r_e, |r_e| ≤ H_hi,e‖y_h‖ ≤ 5,2·10⁻¹¹) | 0,2385 | −0,2439 |
| **L₀,₀-Mittelpunkt I₀ − r_p** | **−3,358** | **+4,836** |

Konsistenztests: (i) ⟨y_f, y_h⟩/δ aus f_v auf dem h-angepassten Netz = 0,277061 gegen ⟨B*c_v, y_h⟩/δ aus der Funktion A8(Φc_v) = 0,277057 (gerade) bzw. −0,0132005 gegen −0,0131744 (ungerade) — Aufhebung auf 4·10⁻⁶ bzw. 3·10⁻⁵ bei Einzelgrößen von Ordnung 10²; (ii) ‖y_f‖ aus dem Netz 135,2385 / 147,0742 gegen die zertifizierten Werte 135,237 / 147,073; (iii) ‖h₈‖, a_h und die Φ*h₈-Koordinaten k ≤ 30 stimmen zwischen drei verschiedenen Netzen (384-Knoten-Kernnetz, 24-Knoten-Operatornetz, 12-Knoten-f-Netz) auf 10⁻¹⁶ bis 10⁻¹⁸ überein.

## 3. Fehlerinventar (geerbte Konstanten; undirekt, keine Quadraturreste)

| Term in (7.1) | Bedeutung | gerade | ungerade |
|---|---|---|---|
| e_ψ,p·‖h‖ | ψ-Modellfehler = −F(k_actual − k_model), **nichtkohärent** | 14 026 · 0,3387 = **4 751** | 45,36 · 0,2948 = 13,37 |
| e_Ψ,p/√(1−ρ)·‖C*Φ*h₈‖ | Merkmalsfehler von c_p (k-Änderung dominiert); ‖C*Φ*h₈‖ = 0,2964 / 0,2232 | 99,5 | 0,514 |
| H_hi,p·‖y_h‖ | hoher Rest (Schranke; tatsächlicher Wert 0,24) | 105,5 | 2,357 |
| χ_upper,p·ε_R·‖z₀‖_W | D − D̂ (bereits in den Schwellen bezahlt) | < 1,9·10⁻¹³ | < 2,7·10⁻¹⁶ |
| Summe (ohne Quadratur) | | ≈ 4 956 | ≈ 16,2 |
| Schwelle dist(0, L₀,₀) > | | 980,114 | 398,766 |

Ungerade: selbst mit den nichtkohärenten Konstanten läge L₀,₀ in [−11,4; 21,0] — die Schwelle 398,77 ist um den Faktor ≈ 19 entfernt. Gerade: das Budget 4 963 übersteigt die Schwelle; entscheidend ist der Term e_ψ,p‖h‖, also der k-Fehler durch die zwölf Quellen F. Genau dieser Term ist kohärent transportierbar (§4).

## 4. Kohärenter k-Fehler: F-Anteil

Δχ_p = −HΔk mit H = F − J_old U8 g_F. Der F-Anteil ist mit b_F = F*h ∈ ℝ¹² und G_p = η_p²K⁻¹ (77b806b1…) exakt beschränkt durch |⟨FΔk, h⟩| ≤ √(b_F*G_p b_F). F = (z_{σ+2}, z_{σ+4}, z_{σ+6}, z_{σ+8}, ΛY₁, …, ΛY₈) nach FUNKTIONSANSCHLUSS §3; die Y_j = Q·S wurden aus den gebundenen lokalen Q-Koeffizienten (half-inverse/expected/1536.json, Block über |Q·Zt − Jt| ≤ 6·10⁻⁴² identifiziert) und der rationalen Matrix S rekonstruiert, ΛY_j = Y_j auf der Schale und −(λ(Y_j)/μ₈)m im Kern.

| | gerade | ungerade |
|---|---|---|
| b_F,1…4 = ⟨z_{σ+2k}, h⟩ | je ≈ −1,2…−2,3·10⁻¹⁵ | je ≈ −1,4…−2,3·10⁻¹⁵ |
| b_F,5…12 = ⟨ΛY_j, h⟩ | −5,2·10⁻⁴, 1,2·10⁻⁴, 4,1·10⁻⁴, 4,4·10⁻⁴, 4,2·10⁻⁴, 3,8·10⁻⁴, 3,5·10⁻⁴, 3,1·10⁻⁴ | 3,5·10⁻³, 2,2·10⁻³, 1,1·10⁻³, 7,1·10⁻⁴, 5,4·10⁻⁴, 4,5·10⁻⁴, 3,8·10⁻⁴, 3,4·10⁻⁴ |
| √(b_F*G_p b_F) (kohärent, p) | **3,55·10⁻⁴** | **1,70·10⁻⁵** |
| zum Vergleich e_ψ,p·‖h‖ (nichtkohärent) | 4 751 | 13,37 |
| Kontrolle v: √(b_F*G_v b_F) gegen e_ψ,v‖h‖ | 6,3·10⁻⁹ gegen 0,084 | 1,8·10⁻⁹ gegen 1,4·10⁻³ |
| k₀ (77b806b1…) gegen core_k_mid (Stufe 1), erste vier Komponenten | Abweichung 4·10⁻⁴⁹ | 5·10⁻⁵⁰ |

Die ersten vier Komponenten verschwinden auf 10⁻¹⁵: h ist (bis auf die 60-stellige Rundung von X_fix ≈ A12⁻¹) orthogonal zu den Testpolynomen Φ_i der Regel, und die z_{σ+2k} liegen in deren Spann — das ist die Galerkin-Struktur der festen Antwortregel, hier numerisch sichtbar. Der kohärente F-Anteil des k-Fehlers ist damit um sieben Größenordnungen kleiner als die geerbte nichtkohärente Schranke.

**Fehlerinventar mit kohärentem F-Anteil** (undirekt in den übrigen Termen, ohne Quadraturreste): gerade 3,5·10⁻⁴ + 99,5 (Merkmalsfehler mit ‖C*Φ*h₈‖ = 0,2964) + 105,5 (hoher Rest, Schranke) ≈ **205** gegenüber Schwelle 980,11; ungerade 1,7·10⁻⁵ + 0,514 (‖C*Φ*h₈‖ = 0,2232) + 2,357 ≈ **2,9** gegenüber 398,77. In beiden Paritäten läge L₀,₀ dann in einem Intervall um −3,36 bzw. +4,84 mit Radius ≈ 205 bzw. ≈ 2,9 — weit unter den Schwellen, also **kein Ausschluss der Regel durch z₀**, sobald die Quadraturreste gerichtet nachgeliefert sind.

Der zweite Anteil (−J_old U8 g_F Δk) bleibt hier mit dem geerbten Merkmalsfehler 106,7 / 0,633 bezahlt (Dreiecksungleichung; Kohärenz zwischen beiden Anteilen wird dabei nicht ausgenutzt). Für seinen kohärenten Transport wären die zwölf U8-Antworten auf g_F e_i nötig (Stufe-2/3-Pipeline für zwölf k-Einheitsrichtungen).

## 5. Eigene Fehler in dieser Stufe (alt → neu)

1. Erstfassung von `l00.py` zog ⟨y_f, y_h⟩/δ allein vom Mittelpunkt ab („L00_midpoint_ohne_hohen_Rest" = −1,27·10⁸ / −8,9·10⁶). Falsch: der hohe Rest ist die Differenz (1/δ)⟨y_f − B*c, y_h⟩, die durch H_hi‖y_h‖ beschränkt ist; der Mittelpunkt ist I₀ = ⟨ψ_p, h⟩ − ⟨c_p, Φ*h₈⟩ (§2). Korrigiert.
2. Erster Konsistenztest mit der gespeicherten Funktion A8(Φc_v) aus Stufe 4 ergab r_v(h) = 1920 — Verletzung der zertifizierten Schranke. Ursache: das Stufe-4-Netz enthält die zwölf Prim-Schnittstellen von c̃ nicht (sichtbar an ‖h₈‖ = 0,33665 statt 0,33853). Behoben durch Neuauswertung von A8(Φc_v) auf einem h-angepassten Netz (41 Zellen, 24 Knoten; κ_c reproduziert auf 10⁻⁹).
3. Danach r_v(h) = 2244 — Ursache: ⟨f, h₈⟩ auf dem Stufe-2-Netz von f, das die h-Schnittstellen ebenfalls nicht enthält (in Stufe 4 fielen die D_j-Schnittstellen mit denen von f zusammen). Behoben durch Neuberechnung von f_v = Π₈[Q^np ψ_v] auf dem vereinigten Netz (45 Zellen); ‖y_f‖ stimmt danach mit dem Zertifikat überein.
4. Beim Einzelstart mit `odd` wurde die Parität aus der Listenposition abgeleitet (c̃-Kontrolle schlug mit 2,89 fehl); behoben.
5. Zwei parallele Läufe überschrieben dieselbe Ausgabedatei; jetzt paritätsgetrennte Dateien.

## 6. Was fehlt für ein gerichtetes L₀,₀

- Gerichtete Quadraturreste für ⟨ψ_p, h⟩, Φ*h₈, F̂z₀, die Momente und Normen (Produkte stückweise analytischer Funktionen mit log-Randtermen und Sprüngen; Randzerlegung c̃ = g·log(a−x) + R aus 993619be… nutzbar).
- Kohärenter Transport des Antwortanteils (zwölf U8-Antworten auf g_F e_i) oder Nachweis, dass der geerbte Merkmalsfehler ausreicht (gerade: 99,5 < 980 — reicht, da der F-Anteil kohärent klein ist).
- Einbeziehung aller übrigen Modellfehler (D̂-Rundung, F̂-Darstellung, Tz₀-Verstärkung |Tz₀| ≈ 4·10⁵ auf die D̂-Einschließungen).
- Das Ergebnis betrifft nur z₀ (Grad 0). Für den ganzen Schalenpolynomraum Grad ≤ 11 (K_P[s] < 29,6‖s‖²_W) wären die entsprechenden Richtungen z_n zu rechnen; die Pipeline ist dafür linear in z.

## 7. Dateien

`l00.py` (Hauptrechner inkl. b_F und kohärentem F-Anteil), `high_rest2.py` (A8(Φc_v) auf h-Netz, r_v(h)), `check_yf.py` (f_v auf h-Netz, ⟨y_f, y_h⟩), `run_mesh_h.py` (Stufe-2-Pipeline auf vereinigtem Netz), Ergebnisse `L00_lower_Pv_{even,odd}.json`, `HIGH_REST_{even,odd}.json`, `A8PHIC_hmesh_{even,odd}.json`, Netze `MESHH_{even,odd}_upper_v.json`, `MESH_{even,odd}_lower_Pv.json`, Logs.
