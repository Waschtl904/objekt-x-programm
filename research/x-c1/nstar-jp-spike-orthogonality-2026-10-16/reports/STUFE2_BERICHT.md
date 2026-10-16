# Objekt X — Stufe 2: innere Quelle f_t = Π8[Q^np_{b₉} ψ_t]|(0,a₈) für t = v

Stand 16. Oktober 2026 · Diagnose am Head 0ded564 von PR #226 · **kein Zertifikat, keine Statusänderung, keine Repositoryänderung**

## Vorab: Übernahme der Gegenprüfung (Prüfpaket 940cd40e…dd49)

- Replay von `certify.py` gegen das N*Jp-Archiv b48e3895…: **PASS**, alle vier Ergebnisdateien (`DIRECTED_RESULTS.json`, `PARALLELISM.json`, `PSI_CORRECTED.json`, `RECEIPT.json`) bytegleich reproduziert. Die vier `incoming`-Dateien sind bytegleich mit meinen Stufe-1-Originalen.
- **Korrektur 1 (mein Fehler, bestätigt):** In `shell_chi.py` v1 stand λ_total = λ(r) **+** Σⱼ k_{4+j} λ(Yⱼ). Richtig ist **−**, weil (ΛYⱼ)|Kern = −(λ(Yⱼ)/μ)·m. Eigener Gegencheck: mit dem Plus ist ∫₀^{b₉} m ψ = −1,4287·10⁻⁴ (gerade) bzw. −2,6065·10⁻⁴ (ungerade), mit dem Minus 4·10⁻³⁶ bzw. −2·10⁻³⁸. Alter Wert λ_total = +7,1433·10⁻⁵ / +1,3033·10⁻⁴; korrigierter Wert **−7,14356·10⁻⁵ / −1,30329·10⁻⁴** (gerade/ungerade, t=v). Schalenteil, Normen und Aufhebungsdiagnose von Stufe 1 sind unberührt. `shell_chi.py`, `STUFE1_SHELL_RESULTS.json` und `PSI_DEFINITION.json` liegen als v2 vor. Ein erster Stufe-2-Netzlauf benutzte noch die unkorrigierte `PSI_DEFINITION.json`; er wurde verworfen und wiederholt (Auswirkung auf f_t ≈ 10⁻⁸ relativ; die Quadraturkontrolle unten hat den Fehler aufgedeckt).
- **Korrektur 2 (angenommen):** p = αv + e mit α = q/‖v‖², e ≠ 0, ‖v‖² ≠ 1. Meine Formulierungen „q = ‖p‖" und „(11q/10)|ℓ_v|²·(1+O(10⁻¹⁴))" waren als exakte Aussagen nicht gerechtfertigt; die Zahlen (1−cos² = 10⁻²⁸, ‖p−qv‖/‖p‖ = 1,3·10⁻¹⁴) bleiben richtig. Für den Test gilt ℓ_p = αℓ_v + ℓ_e; ℓ_e ist gesondert zu bezahlen oder p direkt zu verwenden.
- **12-Knoten-Gauss-Kontrolle, genauer Umfang:** Sie wurde ausschließlich auf die Produkte zₙ|Schale·ℓ_k mit n ≤ 9, k ≤ 9 (Grad ≤ 18 < 23) angewendet, also auf die vier Kernpolynom-Profile. Die Grad-95-Objekte (Jt, Yⱼ) wurden nicht mit 12 Knoten geprüft; ihre Normen sind Koeffizientensummen, ihre λ-Momente adaptive Quadraturen mit zwei Methoden (Differenz ≤ 2·10⁻⁴⁴).
- **W9-Untergrenze des Prüfpakets** (‖W9‖ > 2,52·10¹¹ gerade, > 4,98·10¹⁰ ungerade): Herleitung am Beweistext nachvollzogen. Aus (6.4) in `A9_INVERSE_PROOF.txt` folgt nach Weglassen der drei nichtnegativen Summanden ⟨f8,U8f8⟩, v12*K⁻¹v12, β⁻¹⟨ν,R_Lν⟩ und Cauchy–Schwarz in P_upper: ⟨f,W9f⟩ ≥ (11/(10q))|⟨Jp,ν⟩|² = (11/(10q))|⟨χ_p,f⟩|² für alle f ∈ H9, und damit ‖W9‖ ≥ (11/(10q))‖χ_p|Schale‖². Arithmetik: (11/(10·56619,81))·(1,1401·10⁸)² = 2,525·10¹¹. Wie im Paket gesagt: keine Untergrenze für A9⁻¹, keine Fehlerobergrenze, kein N12-Ausschluss.

## Definitionen (umgesetzt wie in FUNKTIONSANSCHLUSS §3)

Q^np_l u = H_Γu − κu − S_l u mit H_Γu(x) = ∫₀^∞ k(r)[2u(x) − u(x+r) − u(x−r)]dr, k(r) = e^{−r/2}/(1−e^{−2r}), κ = log(8π) + γ + π/2, S_l u = Σ_{q<e^{2l}} w_q[u(·+log q) + u(·−log q)], w_q = log(prime(q))/√q, q ∈ {2,3,4,5,7,8} für l = b₉. ψ_t ist paritätisch fortgesetzt (ε = (−1)^σ) und außerhalb (−b₉,b₉) null; Q wirkt auf die ganze Funktion, erst danach wird auf (0,a₈) eingeschränkt und Π8 f = f − m(∫₀^{a₈} m f dx)/μ angewendet.

Rechenart: mpmath, 22 Stellen; r-Integrale mit allen Sprungstellen von ψ als Breakpoints (a₈−x, x, a₈+x, b₉−x, b₉+x), Schwanz r > b₉+x analytisch; Primverschiebungen direkt. Kein Intervallzertifikat.

## Validierung des Operators

| Test | Ergebnis |
|---|---|
| Indikator 1_{(−A,A)} (A = a₈, b₉): H_Γ = ∫_{A−x}^∞k + ∫_{A+x}^∞k | Abweichung ≤ 10⁻²⁵ an drei Punkten |
| Gauß u = e^{−x²/2}: Ortsraumdefinition gegen Fourier-Multiplikator g(ξ) = Re ψ(¼+iξ/2) − ψ(¼) | Abweichung ≤ 5·10⁻²⁶ an drei Punkten (bestätigt die Kernnormierung) |
| ½∫_{−1}^{1}[Pₙ(x)−Pₙ(y)]/|x−y| dy = Hₙ Pₙ(x), n = 0,1,2,5,8 | ≤ 1,3·10⁻²⁶ |
| Netzquadratur: ∫₀^{a₈} m ψ gegen −λ(s_t) aus Stufe 1 | 196,27148499 vs 196,271485 (gerade), 105,69557615 vs 105,6955761 (ungerade); Differenz 10⁻⁸ = Stellenzahl des Referenzwerts |
| Netzquadratur: ∫₀^{a₈} log(a₈−x) dx exakt | 9·10⁻¹³ |
| Netzquadratur: ∫₀^{a₈} m² = μ | ≤ 2·10⁻²² |
| Momentnull nach Π8 | 3·10⁻¹⁸ / 3·10⁻¹⁹ |

## Singuläre Struktur von f_t (vollständig bestimmt)

**Logarithmischer Randterm an a₈.** Sprung j_v = ψ(a₈⁺) − ψ(a₈⁻): −2848,12987929 (gerade), −2824,08593577 (ungerade) — beide innerhalb der gerichteten Intervalle des Prüfpakets. Numerisch bestätigt: Qψ(x) − (j/2)·log(a₈−x) konvergiert für x → a₈⁻ (Werte bei a₈ − 10⁻⁶/10⁻⁸/10⁻¹⁰: −127114,06 / −127122,41 / −127122,52 gerade; 204695,03 / 204686,13 / 204686,01 ungerade). Der Koeffizient j/2 aus (5.2) des Prüfpakets ist damit auch numerisch richtig.

**Neun innere Sprungstellen** (Primverschiebungen transportieren die ψ-Wände ±a₈, ±b₉ in den Kern); Sprünge von Q_raw (rechts minus links), t = v:

| x | Herkunft | gerade | ungerade |
|---|---|---|---|
| 0,058892 = log3 − a₈ | x−log3 trifft −a₈ | −1806,52 | +1791,27 |
| 0,287682 = log4 − b₉ | x−log4 trifft −b₉ | +0,0055 | −0,0156 |
| 0,346574 = ½log2 | x+log2 trifft +a₈ und x−log4 trifft −a₈ | +408,86 | +2362,92 |
| 0,405465 = b₉ − log2 | x+log2 trifft +b₉ | −0,0078 | −0,0221 |
| 0,510826 = log5 − b₉ | x−log5 trifft −b₉ | +0,0114 | −0,0324 |
| 0,569717 = log5 − a₈ | x−log5 trifft −a₈ | −2049,98 | +2032,67 |
| 0,847298 = log7 − b₉ | x−log7 trifft −b₉ | +0,0117 | −0,0331 |
| 0,906189 = log7 − a₈ | x−log7 trifft −a₈ | −2094,76 | +2077,07 |
| 0,980829 = log8 − b₉ | x−log8 trifft −b₉ | +0,0039 | −0,0110 |

Kontrolle: Sprung = w_q·(±j) exakt, z. B. w₅·j = 0,71971·(−2848,13) = −2049,98 (gerade), mit Paritätsvorzeichen bei negativen Argumenten (ungerade: +2032,67 = −w₅·j_ungerade). Die b₉-Sprünge sind klein, weil ψ_v(b₉⁻) nur −0,0159/−0,0451 ist; für p skalieren alle Werte mit α ≈ 56620 bzw. 9372.

Konsequenz: f_t ist stückweise glatt mit log-Singularität an a₈ und neun Sprüngen; jede Weiterverarbeitung (Normen, Pairings, Legendrekoeffizienten) muss diese Punkte als Zellgrenzen führen. Eine rein glatte Behandlung wäre, wie das Prüfpaket sagt, unzulässig.

## Ergebnisse auf dem Netz (468 Knoten: 10 Sprungzellen + 28 geometrisch verfeinerte Zellen zu a₈, je 12 Gauss-Knoten)

| Größe (H8-Norm, 2dx) | gerade, t=v | ungerade, t=v |
|---|---|---|
| ∫₀^{a₈} m·Q_rawψ dx (Moment vor Π8) | 17314,6257 | 7703,0467 |
| Norm des abgezogenen Momentträgers | 22948,1 | 34647,5 |
| ‖Q_rawψ‖ | 238843,78 | 270999,52 |
| **‖f_t‖ = ‖Π8 Q^np ψ_t‖** | **237738,801** | **268775,540** |
| ‖H_Γψ‖ | 3,2513·10⁷ | 1,8787·10⁷ |
| ‖κψ‖ | 3,5067·10⁷ | 1,9263·10⁷ |
| ‖Sψ‖ | 3,4138·10⁶ | 1,0580·10⁶ |
| Aufhebung ‖κψ‖/‖f_t‖ | 147 | 72 |
| Anteil Grade ≤ 61 an ‖f_t‖² | 1 − 6,7·10⁻⁶ | 1 − 7,1·10⁻⁶ |
| Norm des Anteils Grade > 61 | 617 | 714 |

Deutung: Q^np hebt ψ auf dem Kern um zwei Größenordnungen auf (H_Γψ ≈ κψ + Sψ), aber die Quelle f_t bleibt mit ≈2,4·10⁵ bzw. 2,7·10⁵ etwa 120-mal größer als der Schalenteil (2014/2200). f_t ist stark niedriggradig: die skalierten Koeffizienten ⟨eₙ, Uf⟩ sind bis n ≈ 15 von der Ordnung 10⁵ (gerade: n=0: −1597; 2: 40503; 4: 27376; 6: −33525; 8: −103716; 10: −30721; 12: 154147; 14: −122046 …) und fallen danach ab. Die Koeffizienten für n ≳ 20 sind mit diesem Netz nicht verlässlich (12 Knoten pro Zelle gegen bis zu 10 Oszillationen von P₆₁); verlässlich sind Normen, Momente, Sprünge und die niedrigen Grade.

Hinweis zur Momentkorrektur: Der Π8-Abzug (Norm 2,3·10⁴/3,5·10⁴) ist ≈10 % von f_t, keine Kleinigkeit; U8 f_t liegt nach Konstruktion im alten Momentnullraum, wie vom Prüfpaket als Kontrolle gefordert (∫ m f_t = 3·10⁻¹⁸).

## Was für Stufe 3 folgt

- U8 f nach Formel (A) braucht: Φ*f (191 Pairings mit Polynomen bis Grad σ+382), y = T_h f = P_Y M* U f (hoher Anteil; die Grade > 61 tragen hier nur ‖·‖ ≈ 600–700, der Anteil > 383 ist entsprechend kleiner), B8 y und B8*c. Da f_t vorwiegend niedriggradig ist, wird U8 f_t voraussichtlich vom Φc-Term dominiert; das ist eine Erwartung, keine Rechnung.
- Für die 191 Pairings reichen 12 Knoten pro Zelle nicht; nötig sind ≈ 2000–3000 Auswertungen von f_t. Mit dem jetzigen mpmath-Evaluator (≈1,2 s pro Punkt) sind das 40–60 Minuten pro Parität — machbar, aber ein schneller Doppelgenauigkeits-Evaluator (gleiche Breakpoint-Logik, feste Gauss-Regeln in r, Ziel 10⁻¹² relativ) wäre für die Diagnosestufe angemessener; das Zertifikat kommt ohnehin nicht aus diesem Code.
- Fehler: Der gemeinsame k-Fehler geht nach Prüfpaket §2 als Δχ = −(F − J_old U8 g_F)Δk mit dem K-Ellipsoid ein, nicht als unabhängige Radien; der L²-Fehler von ψ darf nicht durch Q geschoben werden. Für ψ_e (‖ψ_e|Schale‖ ≈ 1,4·10⁻⁶ gerade, 9,3·10⁻⁸ ungerade laut Prüfpaket) ist f_e grob von der Ordnung 10⁻¹ — klein, aber zu bezahlen, nicht wegzulassen.

## Nicht gezeigt / nicht behauptet

Kein Intervallzertifikat; keine Rechnung für t = p oder e (nur t = v; p über α und e zu führen); keine U8-Aktion, kein χ_t|Kern, keine Pairings mit Cz oder D12Tz, kein N12-Test, keine Aussage zu W9-Dominanz, A9→A11, Objekt X oder RH. Keine Repositoryänderung.

## Dateien

- `qnp_psi.py` — Evaluator (ψ_t, H_Γ, S, Q^np, Breakpoints, Netz); `validate.py`, `t4.py` — Operatorvalidierung und Log-Randterm; `jumps.py` — innere Sprünge; `run_mesh.py`, `post.py` — Netzlauf und Nachbearbeitung.
- `MESH_even_upper_v.json`, `MESH_odd_upper_v.json` — 468 Knoten je Parität mit x, w, ψ, H_Γψ, Sψ, Q_raw (korrigiertes ψ).
- `STUFE2_RESULTS.json` — Momente, Normen, Koeffizienten, Profil; `STUFE2_JUMPS.json` — Sprünge, j, Log-Konstante.
- `v1_wrong_sign/` — verworfener erster Lauf mit falschem λ_total (zur Nachvollziehbarkeit).
- Stufe 1 v2: `../stufe1/shell_chi.py`, `STUFE1_SHELL_RESULTS.json`, `PSI_DEFINITION.json` (Vorzeichen korrigiert).

## Übergabeprompt für Stufe 3 (kopierbar)

```
Objekt X, Stand 16.10.2026. Offen: PR #226 (Head 0ded564; Budgetpaket 7f712994…, N*Jp-Paket
b48e3895…), PR #227 (Head 5243737); #225 gemergt. Keine Mergeempfehlung.
Stufe 1 (Schale) gerichtet zertifiziert durch Pruefpaket 940cd40e… (certify.py PASS, bytegleich);
zwei Korrekturen uebernommen: lambda_total = lambda(r) - sum k_{4+j} lambda(Y_j) (Minus), und
p = alpha v + e mit e != 0 (alpha = q/||v||^2); ell_p = alpha ell_v + ell_e.
Stufe 2 (Diagnose, kein Zertifikat, t=v): f_t = Pi8[Q^np_b9 psi_t]|(0,a8) auf 468-Knoten-Netz;
||f_v||_H8 = 237738.80 (gerade) / 268775.54 (ungerade); Moment vor Pi8 17314.63 / 7703.05;
Log-Randterm (j/2) log(a8-x) mit j = -2848.12988 / -2824.08594, Konstante -127122.52 / 204686.01;
neun innere Spruenge bei x = log q - a8, log q - b9, a8 - log2, b9 - log2 (Werte in STUFE2_JUMPS.json);
f_v ist niedriggradig (Grade > 61 tragen nur ~650 der Norm). Dateien: qnp_psi.py, MESH_*.json,
STUFE2_RESULTS.json, STUFE2_JUMPS.json, PSI_DEFINITION.json v2.
Aufgabe Stufe 3: U8 f_v nach Formel (A): y = T_h f, d = Phi* f - B8 y/delta, c = C_inv C_inv* d/(1-rho),
U8 f = Phi c + T_h*(y - B8* c)/delta; C_inv, rho, delta aus OPERATORS.json (Common96); B8* e_i als
ganze Funktionen (Q^np_a8 auf M E e_i, Randlogarithmen, Primverschiebungen q=2,3,4,5,7); P_Y als
Identitaet minus endliche niedrige Projektion. Dafuer zuerst schnellen Evaluator fuer f_t (Breakpoints
wie oben, Ziel 1e-12) und Pairings mit den 191 Phi_i. Kontrollen: int m U8 f = 0; ||chi_t||^2 =
W_X[s_t] + ||z_t||^2 mit z_t = (I - U8 A8) w_t - U8 g s_t; int_core m chi_t = -lambda(s_t).
Danach Stufe 4: ell_p(Rz) = <chi_p, Cz> - <chi_p, D12 Tz> fuer die 12 z (FUNCTIONS12.json,
FROZEN_RESPONSE12.json im #227-Archiv), gemeinsamer k-Fehler als K-Ellipsoid, p direkt oder e bezahlen,
11/(10q) dist(0, ell_p)^2 gegen Budgetobergrenze. Untergrenzen fuer ||W9|| nie in Fehlerobertests;
audit_S getrennt von fixed_X. Kein globaler Abschluss.
```
