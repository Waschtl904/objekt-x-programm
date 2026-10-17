# Objekt X — Stufe 4 (Teil 2): Korrekturen, hohe Paarungen r_{v,j} und Fehlerbudget der D12-Skalare

Stand 17. Oktober 2026 · Grundlage: Prüfpaket `1ccb6be1…99b0` (vollständige hohe U8-Antwort, Spike-Skalarfehler), repliziert mit PASS (drei Ergebnisdateien bytegleich) · Diagnose; kein Zertifikat; keine Repositoryänderung in diesem Schritt.


## 0. Korrekturen zur Fassung vom 17.10. (Gegenprüfungen `94e2bd3b…b16f` und `f0bdfe69…8880`)

1. **Budget 0,6 / 0,015 ist keine gerichtete Obergrenze.** Alter Stand: „gerichtetes Budget ≲ 0,6 / 0,015". Korrigiert: Im Term e_ψ‖D_j‖_{H9} wurde die kleinere Kernnorm ‖h8‖ ≤ ‖D_j‖_{H9} eingesetzt (Untergrenze an der Stelle einer Obergrenze); außerdem fehlen gerichtete Reste für I₀, ‖C*Φ*h8‖ und ‖y_h‖, der D̂-Modellfehlerterm fehlt, und H_hi war nach unten gerundet. Die Zahlen in §3 gelten nur als **unvollständige Größenordnungsdiagnose**.
2. **Cauchy–Schwarz-Test nur auf Modellniveau repariert.** Alter Stand: „Obergrenze aus dem tatsächlichen Gram A". Korrigiert: u₁ᵀA₀u₁ ist der Modellwert ohne den zweiseitigen Gamma-Modellfehler e_A = (42/5)ε_Γ = 1,3587·10⁻²⁸ (≈1,02 % der geraden Modellenergie). Gerichtet geschlossen ist der Rayleigh-Teil jetzt durch das Paket `f0bdfe69…` mit zwei exakt rationalen Zeugen (Replay PASS, bytegleich): tatsächliche Rayleigh-Quotienten in [1,321892; 1,349065]·10⁻²⁶ (gerade) bzw. [8,531120; 8,531393]·10⁻²⁴ (ungerade) (nach außen gerundet; eine frühere Anzeige dieser Fassung hatte die oberen Endpunkte nach innen gerundet), daraus bedingt ‖A9⁻¹‖ > 7,4·10²⁵ / 1,17·10²³. Meine I_j und die Quotienten |I_j|/Schranke bleiben Diagnose (keine Einschließung von I_j, A12_jj).
3. **‖χ_e‖:** Alter Stand: „‖χ_e‖ < 88,2". Korrigiert: 88,2 gilt nur ungerade; gerade ist die gebundene Grenze 25317,73 (COMPLETE_HIGH_RESPONSE.json). Für ℓ_p = αℓ_v + ℓ_e ist der gerade Rest entsprechend groß zu bezahlen oder p direkt zu rechnen.
4. **r_{v,j} und ℓ_v(D_j) sind Quadratur-Mittelpunkte**, keine gerichteten Intervalle; die Vergleichsschranke (zertifizierter Faktor < 0,016 bzw. < 0,00245, hier als 0,0159 bzw. 0,00245 angezeigt) mal ‖y_h‖ verwendet selbst die ungerichtete Quadraturnorm ‖y_h‖, das Einhalten ist eine Konsistenzdiagnose. Die globalen Quadraturkontrollen weichen um +7,56 / −37,5 (gerade) bzw. +100,8 / −115,8 (ungerade) vom Archiv ab; sie widerlegen die Einzelpaarungen nicht, belegen aber auch keine Genauigkeit 10⁻⁵. `high_pairings.py` steigt jetzt bei nichtpositivem Normquadrat aus (vorher `sqrt(abs(·))`). (7.1) ist um I₀ zentriert; ein Abzug von r_diag bräuchte eine Schranke für r − r_diag.
5. **A8PHIC_*.json** sind Funktionswerte auf zwei Netzen, keine gerichtete Funktionsdarstellung; neue C_p-Paarungen brauchen vollständige Integration mit Rest.
6. **K_P-Budgets** liegen laut Gegenprüfung im Paket `87540b07…00d3` vor (fixed_X: K_P[s] < 29,603644·‖s‖²_W auf dem neuen Schalenpolynomraum Grad ≤ 11; Schwellen dist(0, L₀,₀) > 980,113997 gerade / > 398,766496 ungerade für den ersten Test, mit zwei Nachkommastellen sicher > 980,12 / > 398,77; eine frühere Anzeige „980,11" war nach unten gerundet). Das Paket ist seit der Nachreichung vom 17.10. gebunden und repliziert (PASS, bytegleich), ebenso das Anschlusspaket mit den exakten Fehlermetriken G_t = η_t²K⁻¹ (§8). Der entscheidende Schritt bleibt das gesamte gerichtete L₀ für ⟨χ_p, (C_p − D̂T)z₀⟩ inkl. C_p-Kopplung, e und kohärentem k-Fehler; die zwölf D12-Skalare sollen nicht getrennt mit ‖T‖ abgeschätzt werden.
7. **Kohärenter k-Transport** (aus `94e2bd3b…`, BEFUND §5): mit H = F − J_old·U8·g_F und B_D = H*D gilt |⟨χ(k) − χ(k₀), h⟩| ≤ η·√((H*h)*K⁻¹(H*h)) und e_D*e_D ≤ η²·B_D*K⁻¹B_D; Doppelzählung mit dem bereits k-haltigen Hochantwortfehler ist zu vermeiden. Noch nicht numerisch ausgeführt.

## 1. Korrekturen meiner Stufe-4-Teil-1-Aussagen (ausdrücklich)

| Frühere Formulierung (Teil 1 / PR #228) | Korrektur |
|---|---|
| „Die Spike-Richtung ist A9-orthogonal zu den zwölf alten Quellen" | Zu weit. Belastbar ist: **⟨χ_v, A9Φ_j⟩ ist für alle 24 Fälle numerisch sehr klein** (Mittelpunkte 10⁻⁷…2,4·10⁻⁴ bei natürlicher Skala 10³–10⁵); eine exakte Orthogonalität ist nicht bewiesen und wird nicht behauptet. |
| Energie-Cauchy–Schwarz-Test mit a_low[u₁] ≥ u₁ᵀ(F + H_B/δ)u₁ | Eine **Untergrenze** darf nicht als Obergrenze in |a(u,w)| ≤ √(a(u,u)a(w,w)) eingesetzt werden. Auf Modellniveau repariert mit dem Modellgram A₀ aus `a8_model.json.gz`: u₁ᵀA₀u₁ = 1,3355573·10⁻²⁶ (gerade) / 8,5312837·10⁻²⁴ (ungerade) (A₀ stimmt mit F + H_B/δ bis 2,5·10⁻³³ überein); die Verhältnisse |I_j|/Schranke bleiben 0,02–0,16 (`SOFTMODE_CS_CORRECTED.json`) — **Diagnose, da der Gamma-Modellfehler e_A = 1,36·10⁻²⁸ fehlt und I_j, A12_jj nicht eingeschlossen sind**; der gerichtete Rayleigh-Anschluss steht im Paket `f0bdfe69…` (§0 Nr. 2). |
| „L²-Normen 10¹³/10³¹ sind Koordinatenartefakte" | Falsch formuliert. Die Normen im festen physischen Raum sind unter isometrischen Koordinatenwechseln invariant und damit echte große Größen, getragen von einer extrem weichen A8-Mode (λ ≈ 1,3·10⁻²⁶); bedingt folgt ‖A9⁻¹‖ > 7,4·10²⁵ (gerade) / 1,17·10²³ (ungerade). Große Norm erzwingt aber keine große Paarung mit einem bestimmten Residuum. |
| „U8 f_v ≈ Φc, hoher Anteil ≲ 10⁻³" aus Quadraturnormen | Nicht gerichtet, weil ‖f_v‖² aus Quadratur stammte. Gerichtet geschlossen ist jetzt durch das Prüfpaket: ‖u_hi,v‖ < 0,016 (gerade) / 0,00245 (ungerade), mit tatsächlichem k, allen Quellen-/Kopplungsfehlern und Momentlift. |
| v und u₁ | Zwei verschiedene Objekte: v ist die 84-dimensionale Spike-Richtung aus P_upper, u₁ die 191-dimensionale weiche Mode des Common96-Kopfes; der Koeffizientenvektor c von U8 f_v liegt numerisch fast ganz in Richtung u₁. χ_v = N*Jv ist ein dritter, physischer Vektor. |
| „Der untere N12-Test kann aus dem D12-Anteil praktisch nicht scheitern" | Nicht gefolgert: die D12-Paarungen werden im Residuum mit der großen Antwortmatrix T (‖T‖ < 6,8·10⁶) kombiniert, und die neue C_p-Kopplung ist ungerechnet. |

## 2. Die zwölf hohen Paarungen r_{v,j} = (1/δ)⟨y_f − B*c, y_{h,j}⟩

**Weg.** ⟨B*c, y_h⟩ = ⟨T_h A8(Φc), T_h h8⟩ = ⟨A8(Φc), h8⟩ + γ_m a_{A8Φc} a_h − (A·c)·(Φ*h8) nach (7.1), mit A8(Φc) = [Q^np_{a₈} P_c(x/a₈) − κ_c m]/√(2a₈) als **einer** ganzen Funktion am Horizont a₈, P_c = Σᵢ cᵢ(e_{nᵢ} − βᵢe_σ). Operator in analytischer Zerlegung Q P = D_H P + q₀P + V P − Γ_{a₈}P − S_{a₈}P (D_H Pₙ = HₙPₙ, q₀ = −log(2πa₈) − γ, V = −½log(1−t²), Γ mit exaktem k_reg = k − 1/(2r) per Gauss–Legendre 2×192 Knoten beidseits der Knickstelle, Verschiebungen q = 2,3,4,5,7); gegen meinen direkten H_Γ-Integrator auf 10⁻²⁹ validiert (`validate_a8.py`). Niedrige Koordinaten (A·c) aus dem Modellgram A (nicht aus Quadratur); Φ*h8_j, a_h aus den 384-Knoten-Werten von Teil 1 (150 Stellen). Nur ⟨A8(Φc), h8_j⟩ per Quadratur (24 Knoten je Zelle, alle a₈- und a₉-Sprungstellen als Zellgrenzen, 24 geometrische Zellen zur Log-Singularität an a₈), mpmath 50 Stellen.

**Kontrollen (Diagnose, keine gerichteten Reste).** (A·c)_k gegen Quadratur für k ≤ 30: 2,7·10⁻⁸ / 3,9·10⁻⁸ relativ; a_{A8Φc} = −1596,97428 (gerade) = a_f; ‖A8Φc‖ = 237738,80113 = ‖f_v‖ auf 10⁻¹⁰ (erwartet, da A_low c ≈ d/(1−ρ)); h8-Normen gegen Teil 1 auf 10⁻¹⁰. Ein erster Lauf, der auch Φ*h8 mit 24 Knoten je Zelle extrahierte, lieferte r-Werte bis 2,3 und **verletzte die zertifizierte Schranke** |r_{v,j}| ≤ ‖r‖‖y_h‖/δ ≤ 0,0159·‖y_h‖ — Koordinaten bis Grad 383 brauchen ≥ 192 Knoten je Zelle; der Lauf wurde verworfen. Die Kontrollen auf 10⁻¹⁴ relativ (‖B*c‖² gegen cᵀG₀c, ⟨B*c,y_f⟩ gegen Archiv) sind mit Quadratur nicht erreichbar und bleiben dem Prüfpaket überlassen.

| gerade: Grad | ⟨y_f,y_h⟩/δ | ⟨B*c,y_h⟩/δ | **r_{v,j}** | diagn. Vergleichswert | Klammer (Teil 1) | **ℓ_v(D_j) Mittelpunkt** |
|---|---|---|---|---|---|---|
| 2 | −0,0409784 | −0,0409752 | −3,2·10⁻⁶ | 1,0·10⁻³ | −3,5·10⁻⁶ | −3,2·10⁻⁷ |
| 4 | −0,0565979 | −0,0565969 | −1,0·10⁻⁶ | 1,4·10⁻³ | −4,1·10⁻⁶ | −3,1·10⁻⁶ |
| 6 | −0,0690132 | −0,0690177 | +4,4·10⁻⁶ | 1,7·10⁻³ | −3,7·10⁻⁶ | −8,1·10⁻⁶ |
| 8 | −0,0804067 | −0,0804159 | +9,2·10⁻⁶ | 1,9·10⁻³ | −2,4·10⁻⁶ | −1,2·10⁻⁵ |
| 10 | −0,0913721 | −0,0913780 | +5,9·10⁻⁶ | 2,2·10⁻³ | +1,0·10⁻⁷ | −5,8·10⁻⁶ |
| 12 | −0,1022016 | −0,1021987 | −2,9·10⁻⁶ | 2,4·10⁻³ | +4,0·10⁻⁶ | +6,9·10⁻⁶ |
| 14 | −0,1130345 | −0,1130319 | −2,6·10⁻⁶ | 2,6·10⁻³ | +8,0·10⁻⁶ | +1,1·10⁻⁵ |
| 16 | −0,1239082 | −0,1238887 | −1,9·10⁻⁵ | 2,7·10⁻³ | +1,4·10⁻⁵ | +3,4·10⁻⁵ |
| 18 | −0,1347952 | −0,1348092 | +1,4·10⁻⁵ | 2,9·10⁻³ | +2,1·10⁻⁵ | +7,3·10⁻⁶ |
| 20 | −0,1456075 | −0,1456761 | +6,9·10⁻⁵ | 3,1·10⁻³ | +2,9·10⁻⁵ | −3,9·10⁻⁵ |
| 22 | −0,1562119 | −0,1562845 | +7,3·10⁻⁵ | 3,3·10⁻³ | +3,9·10⁻⁵ | −3,4·10⁻⁵ |
| 24 | −0,1664295 | −0,1664333 | +3,8·10⁻⁶ | 3,5·10⁻³ | +4,9·10⁻⁵ | +4,5·10⁻⁵ |

Ungerade (Grade 3–25): r_{v,j} zwischen −2,4·10⁻⁴ und +2,2·10⁻⁴, alle unter dem diagnostischen Vergleichswert 2,5·10⁻⁴…6,5·10⁻⁴ (zertifizierter Faktor < 0,00245 mal ungerichtete Quadraturnorm ‖y_h‖) (am engsten bei Grad 13: 2,40·10⁻⁴ gegen 4,9·10⁻⁴); ℓ_v(D_j)-Mittelpunkte zwischen −2,2·10⁻⁴ und +2,4·10⁻⁴. Vollständige Zahlen in `HIGH_PAIRINGS_even.json`, `HIGH_PAIRINGS_odd.json`.

Befund (Konsistenzdiagnose): Alle 24 Mittelpunkte r_{v,j} liegen innerhalb der Vergleichsschranke (zertifizierter Faktor × ungerichtete Quadraturnorm ‖y_h‖) (gerade um Faktor 30–300 darunter, ungerade um Faktor 2–20). Die Fast-Entkopplung ⟨χ_v, A9Φ_j⟩ ≈ 0 wird damit durch den vollständigen hohen Anteil nicht aufgehoben: ℓ_v(D_j) ≈ 10⁻⁵ (gerade) bzw. 10⁻⁴ (ungerade) als Mittelpunktwert, gegen eine natürliche Skala von 10³–10⁵.

## 3. Unvollständige Budgetdiagnose zu (7.1) des Prüfpakets (keine gerichtete Obergrenze, siehe §0 Nr. 1)

|⟨χ_v,D_j⟩ − I₀| ≤ e_ψ‖D_j‖ + e_Ψ‖C*Φ*h8‖/√(1−ρ) + H_hi‖h8‖ + χ_upper‖D_j − D̂_j‖, mit e_Ψ = 5,93·10⁻³ / 2,46·10⁻⁴, H_hi = 0,0159 / 0,00245, e_ψ = 0,2477 / 0,00484 (gerade/ungerade; Zahlen aus `FINITE_ACTION.json` und `COMPLETE_HIGH_RESPONSE.json`). Mit ‖C*Φ*h8_j‖ = 0,39–1,42 und ‖h8_j‖ statt ‖D_j‖_{H9} (Untergrenze, daher Größenordnung):

| | gerade | ungerade |
|---|---|---|
| Term e_Ψ‖C*Φ*h8‖/√(1−ρ) | 0,0023–0,0084 | 1,2·10⁻⁴–3,3·10⁻⁴ |
| Term H_hi‖h8‖ | 0,0066–0,034 | 0,0016–0,0047 |
| Term e_ψ‖h8‖ (dominant) | 0,10–0,53 | 0,0032–0,0094 |
| Summe (ohne D̂-Term, ‖D_j‖ durch ‖h8‖ ersetzt) | 0,11–0,57 | 0,005–0,014 |

**[ÜBERHOLT, siehe §0 Nr. 1]** Die Summen 0,6 (gerade) bzw. 0,015 (ungerade) sind keine gerichteten Obergrenzen, sondern unvollständige Größenordnungsdiagnosen (Kernnorm statt ganzer Norm, fehlende Reste, kein D̂-Term); die Mittelpunkte liegen bei 10⁻⁵ bzw. 10⁻⁴. Der Abstand kommt fast ganz aus e_ψ, dem nichtkohärenten k-Intervalltransport der Stufe 1 (‖Δk‖·‖Fᵢ‖); ein kohärenter Transport über das K-Ellipsoid (Δχ = −(F − J_old U8 g_F)Δk) kann dieses Budget vermutlich um Größenordnungen verkleinern und ist der nächste lohnende Schritt für die D12-Skalare. Für t = p ist ℓ_p(D_j) = αℓ_v(D_j) + ℓ_e(D_j) mit α ≈ 56620 / 9372; ℓ_e ist noch nicht gerechnet; ‖χ_e‖ < 25317,73 (gerade) bzw. < 88,2 (ungerade) **[Fassung 1 nannte 88,2 für beide Paritäten — korrigiert]**.

## 4. Was offen bleibt

⟨χ_p, C z⟩ für die neue Schale (a₉, log(11)/2) — dieselbe Zerlegung ⟨ψ,Cz⟩ − ⟨c,Φ*(Cz)_8⟩ − ⟨r, y_{Cz}⟩/δ kann die gespeicherten Netzwerte von A8(Φc) (`A8PHIC_*.json`) an diesen Knoten wiederverwenden; eine neue gerichtete Paarung braucht aber einen vollständigen Integrationsrest und gegebenenfalls zusätzliche Funktionswerte; ℓ_e; kohärenter k-Fehler; K_P[z]; der Vergleich (6.3) des Prüfpakets. Keine Aussage zu N12-Erfolg oder -Ausschluss, A9→A11, Objekt X, RH.

## 5. Dateien

`a8_operator.py`, `validate_a8.py`, `high_pairings.py`; `A8PHIC_even.json`, `A8PHIC_odd.json` (Funktionswerte von A8(Φc) auf Paarungs- und f-Netz, 40 Stellen); `HIGH_PAIRINGS_*.json`; `SOFTMODE_CS_CORRECTED.json`; `D12_ERROR_BUDGET.json`; Replay des Prüfpakets 1ccb6be1… (PASS, bytegleich).

## 8. Nachreichung 17.10.: K_P-Paket und exakte Eingaben für den kohärenten k-Transport

Gebunden und repliziert (PASS, je zwei Ergebnisdateien bytegleich): das K_P-Paket `87540b07…00d3` (Prüfer mit den vier Übergabearchiven 1ccb6be1, b48e3895, ab7116f7, b8677c0b: 24 gerichtete positive Pivots, ganze analytische Energieobergrenze, 24 Einzelbudgets, zwei Raumgrenzen) und das Anschlusspaket `77b806b1…` (exakte rationale Inverse K⁻¹ der festen Untermatrix K12_new_rational, K·K⁻¹ = I in 576 Einträgen, vier Matrizen G_t = η_t²K⁻¹ für t = v, p und beide Paritäten; η_v ≈ 1,96·10⁻⁸ / 7,92·10⁻¹⁰, η_p ≈ 1,112·10⁻³ / 7,43·10⁻⁶).

Für die unveränderte Regel A9_A11_N12_MIDPOINT_INVERSE_60_V1 und die exakt W-normierte konstante Schalenrichtung z₀ = ℓ₀/√(1 + 2λ₀²/μ) auf (log 3, log 11/2) gilt bedingt K_P[z₀] < 18,662828; aus einem gültigen gerichteten Intervall L₀,₀ für ⟨χ_p, (C_p − D̂T)z₀⟩ genügt dist(0, L₀,₀) > 980,113997 (gerade) bzw. > 398,766496 (ungerade), D12-Modellfehler enthalten. Für den ganzen Schalenpolynomraum Grad ≤ 11: K_P[s] < 29,603644·‖s‖²_W.

Kohärenter k-Fehler, fertige Formel: mit H = F − J_old·U8·g_F, b = H*h, h = (C_p − D̂T)z₀ gilt |⟨Δχ_p, h⟩| ≤ η_p·√(b*K⁻¹b) = √(b*G_p b); für eine gerichtete Box |b_i − b₀,i| ≤ r_i gilt E_k ≤ √(b₀*G_p b₀) + √(rᵀ|G_p|r) (3.1 des Anschlusspakets). Noch nicht vorhanden: gerichtete Einschließungen von H*C_p z₀ und H*D̂Tz₀ sowie das gesamte L₀,₀. Der alte Hochantwortfehler enthält bereits k-Anteile; beim Aufbau von L₀ wird k₀ eingefroren, Mittelpunkt und übrige Reste der festen Funktion bestimmt und Δk genau einmal über G_p bezahlt. Kein N12-Erfolg oder -Ausschluss wird behauptet.
