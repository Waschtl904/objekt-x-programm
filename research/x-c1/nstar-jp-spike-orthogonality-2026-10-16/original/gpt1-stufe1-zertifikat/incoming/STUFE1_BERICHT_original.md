# Objekt X — Stufe 1: Schalenteil von χ_t = N*Jt und Aufhebungsdiagnose

Stand 16. Oktober 2026 · Diagnose am Head 0ded564 von PR #226 · **kein Zertifikat, keine Statusänderung**

## Prüfbasis

- Branch `research/a9-inverse-spike-calibration-2026-10-15`, Head `0ded564d5a6eff1c5b64698821a3f7d04b14e68b` (PR #226, offen).
- Archive bytegenau geprüft: Budgetpaket `7f712994…beb1f5e`, N*Jp-Paket `b48e3895…6d57b`, darin eingebettet das globale Quellarchiv `2ca3c682…53d80c`.
- Eingaben: `DIRECTIONS.json` (Jt-Koeffizientenintervalle, k-Intervalle, t exakt), `1536.json` (Q-Intervalle, S rational), Funktionsdefinitionen `FUNKTIONSANSCHLUSS.txt` §§1–3, 6.
- Rechenart: mpmath mit 60 Stellen (Mittelpunkte) plus Transport der gelieferten k-Intervallradien über die Dreiecksungleichung. Q- und Jt-Radien (≈10⁻⁶⁰) sind vernachlässigt. Das ist eine hochpräzise Diagnose, **kein rationales oder Arb-Intervallzertifikat**.

## Konventionen (so umgesetzt, so geprüft)

- a₈ = 3 log 2 / 2, b₉ = log 3, h = b₉ − a₈, c = (a₈ + b₉)/2; ℓₙ(x) = √((2n+1)/(2h)) Pₙ(2(x−c)/h), orthonormal in X = L²((a₈,b₉), 2dx).
- m = cosh(x/2) (gerade) bzw. sinh(x/2) (ungerade); μ = ∫₀^{a₈} m²; λ(r) = ∫_{a₈}^{b₉} m r (dx, nicht 2dx).
- F = (z_{σ+2}, z_{σ+4}, z_{σ+6}, z_{σ+8}, ΛY₁,…,ΛY₈), Y = QS, zₙ = eₙᵇ − e_σᵇ·(∫₀^{b₉} m eₙᵇ)/(∫₀^{b₉} m e_σᵇ).
- Schalenteil: χ_t|(a₈,b₉) = r − Σᵢ Fᵢ kᵢ mit r = Jt (96 Koeffizienten), zₙ|Schale exakt in ℓ₀…ℓ₉, Yⱼ in ℓ₀…ℓ₉₅.

## Gegenchecks (alle bestanden)

| Check | Ergebnis |
|---|---|
| W_X[Jv]/‖v‖² gegen gebundene Geometrie I ≤ J*W_X J < 1,000502 I | 1,000227989 (gerade), 1,000227934 (ungerade) — innerhalb |
| Q*W_X Q = I mit meinen λ-Integralen | Diagonale bis 2·10⁻⁴¹, Nebendiagonale (Stichprobe) bis 10⁻⁴⁵ |
| Orientierung der ℓₙ (Spiegelung s→−s als Gegenprobe) | gespiegelt bricht die Isometrie auf 10⁻¹¹…10⁻¹⁴ → Orientierung bestätigt |
| λ-Integrale tanh-sinh vs. Gauss–Legendre | Abweichung ≤ 2·10⁻⁴⁴ |
| zₙ-Schalenkoeffizienten adaptiv vs. exakte 12-Knoten-Gauss | ≤ 10⁻³⁰ |
| Momentnull aller zₙ auf (0,b₉) | ≤ 10⁻⁴⁵ |
| Richtung p = P_upper v gegen v (exakt rational) | 1 − cos² = 10⁻²⁸; ‖p − q v‖/‖p‖ = 1,3·10⁻¹⁴ (gerade), 8·10⁻¹⁵ (ungerade); q = ‖p‖ |

Die letzte Zeile ist eine eigene Beobachtung: **p ist bis auf 10⁻¹⁴ relativ ein Vielfaches von v** (q = 56619,81 gerade, 9372,44 ungerade). Damit ist χ_p = q·χ_v bis auf diese Toleranz und die unterschiedlichen k-Radien; die „obere" und die „untere" Richtung je Parität sind nicht unabhängig. Für den Test gilt entsprechend (11/(10q))|ℓ_p|² = (11q/10)|ℓ_v|²·(1 + O(10⁻¹⁴)).

## Ergebnisse Schalenteil

| Größe (X-Norm, 2dx) | gerade, t=v | gerade, t=p | ungerade, t=v | ungerade, t=p |
|---|---|---|---|---|
| ‖r‖ = ‖Jt‖ | 1,000114 | 56626,3 | 1,000114 | 9373,5 |
| ‖χ_t|Schale‖ | **2013,598** | **1,14010·10⁸** | **2199,971** | **2,06191·10⁷** |
| ‖Σ Fᵢkᵢ|Schale‖ | 2013,598 | 1,14010·10⁸ | 2199,971 | 2,06191·10⁷ |
| davon z-Anteil (i ≤ 4) | 1999,38 | 1,13204·10⁸ | 2186,63 | 2,04940·10⁷ |
| davon ΛY-Anteil (i ≥ 5) | 238,88 | 1,35252·10⁷ | 241,93 | 2,26747·10⁶ |
| Σᵢ |kᵢ|·‖Fᵢ|Schale‖ (Rohsumme) | 5,759·10⁶ | 3,261·10¹¹ | 3,157·10⁶ | 2,959·10¹⁰ |
| Aufhebungsfaktor Rohsumme/Ergebnis | 2860 | 2860 | 1435 | 1435 |
| Fehlerradius aus k-Intervallen | 0,218 | 1,234·10⁴ | 4,25·10⁻³ | 39,9 |
| relativer Fehler aus k | 1,08·10⁻⁴ | 1,08·10⁻⁴ | 1,93·10⁻⁶ | 1,93·10⁻⁶ |
| max |Koeffizient| für n ≥ 10 | 1,8·10⁻³ | 104 | 5,8·10⁻⁴ | 5,5 |

Aufhebungsdiagnose in einem Satz: Auf der Schale heben sich die z-Terme um den Faktor ≈2900 (gerade) bzw. ≈1400 (ungerade) gegeneinander auf, aber **nicht gegen r** — r (Norm 1) ist gegen das verbleibende Fk (Norm ≈2000) vernachlässigbar. Die k-Intervalle überleben die Aufhebung deutlich: relativer Fehler 10⁻⁴ (gerade) bzw. 2·10⁻⁶ (ungerade). Der Schalenteil ist damit fest und kann von Stufe 2–4 unverändert übernommen werden; u = U8(·) lebt nur auf (0,a₈) und ändert die Schale nicht.

Profil (gerade, t=v; ungerade analog): χ_v ist auf der Schale eine Randschicht an der a₈-Wand:

| x | a₈⁺ | a₈+0,05h | a₈+0,1h | a₈+0,25h | a₈+0,5h | a₈+0,75h | a₈+0,9h | b₉⁻ |
|---|---|---|---|---|---|---|---|---|
| χ_v (gerade) | −22588 | −15748 | −10853 | −3283 | −315,5 | −14,1 | −0,91 | −0,016 |
| χ_v (ungerade) | −23984 | −17077 | −12025 | −3894 | −425,9 | −22,5 | −1,65 | −0,045 |

Zum Vergleich: r = Jv selbst hat an der Wand r(a₈⁺) ≈ −115 bei ‖r‖ = 1, ist also ebenfalls wandkonzentriert, aber zwei Größenordnungen kleiner.

## Was Stufe 1 schon über den Kern (0,a₈) sagt

Auf (0,a₈) ist χ_t = −λ_total·m/μ − Σ_{i≤4} kᵢ zᵢ − u mit λ_total = λ(r) + Σⱼ k_{4+j} λ(Yⱼ). Die ersten beiden Terme sind in Stufe 1 bereits vollständig bestimmt:

| gerade, t=v | ungerade, t=v |
|---|---|
| λ_total = 7,1433·10⁻⁵ (Radius 8·10⁻¹³), Momentterm-Norm 9,5·10⁻⁵ | λ_total = 1,3033·10⁻⁴ (Radius 5·10⁻¹⁴), Momentterm-Norm 5,9·10⁻⁴ |
| ‖Σ_{i≤4} kᵢ zᵢ‖ auf (0,a₈) = **6,53·10⁶**, Wandwert −19740 | ‖Σ_{i≤4} kᵢ zᵢ‖ auf (0,a₈) = **3,59·10⁶**, Wandwert −21160 |

Das heißt: der Kernpolynomteil ist etwa 3000-mal größer als der ganze Schalenteil. Ob χ_t auf dem Kern klein wird, entscheidet allein u = U8(g r − g_F k). Das ist keine Fehlerquelle, aber eine Vorgabe für Stufe 2–3: die absoluten Fehler von u müssen gegen das **tatsächliche** χ_t|Kern gemessen werden, nicht gegen 6,5·10⁶. U8 ist nach Common96 eine Majorante, keine Inverse; eine vollständige Aufhebung darf nicht erwartet, sondern muss berechnet werden.

## Empfehlung für Stufe 2 (Umformung, keine Änderung der Definition)

Wegen Linearität gilt exakt g r − g_F k = Π8[Q^np_{b₉}(Λr − Σᵢ kᵢ Fᵢ)]|(0,a₈). Mit ψ_t := Λ(Jt) − Fk ist daher

χ_t = ψ_t − J_old·U8·Π8[Q^np_{b₉} ψ_t]|(0,a₈),

und ψ_t liegt nach Stufe 1 **vollständig als eine einzige Funktion** vor: Schale = 96 ℓₙ-Koeffizienten (Datei `PSI_DEFINITION.json`), Kern = Polynom vom Grad ≤ 9 plus −λ_total·m/μ. Die Anwendung von Q^np auf die eine Funktion ψ_t vermeidet, dass die 10⁶- bis 10¹¹-fachen Terme erst in den Kernintegralen gegeneinander ausgelöscht werden. Als Kontrolle sollte eine Stichprobe (z. B. ⟨ℓ₀, ·⟩ und ⟨ℓ₁, ·⟩ des Ergebnisses) zusätzlich über den getrennten Weg g r − Σᵢ kᵢ g_Fi berechnet werden. Zu beachten bleibt: ψ_t springt an a₈ (gerade v: −19740 + Momentterm links, −22588 rechts), daher sind die logarithmischen Randanteile von H_Γ an ±a₈ und ±b₉ mitzunehmen (FUNKTIONSANSCHLUSS §3).

## Einordnung für Stufe 4 (nicht berechnet)

Da ‖χ_v‖_{H9} ≥ ‖χ_v|Schale‖ ≈ 2014 (gerade) bzw. 2200 (ungerade) und ℓ_p = q·ℓ_v, lautet der Test (11q/10)|⟨χ_v, Rz⟩|² gegen eine Budgetobergrenze B_up. Er kann nur bestehen, wenn Rz zur normierten Richtung χ_v/‖χ_v‖ bis auf |⟨χ_v/‖χ_v‖, Rz⟩| ≤ √(B_up/(1,1q))/‖χ_v‖ orthogonal ist; für B_up von der Größenordnung ‖Rz‖² wären das ≈2·10⁻⁶ (gerade) bzw. ≈4,5·10⁻⁶ (ungerade). Das ist eine Skalenaussage aus Stufe 1, kein Ergebnis: Budgetobergrenze, Rz und die Kernpaarungen sind offen.

## Nicht gezeigt / nicht behauptet

Kein Intervallzertifikat (Gleitkomma 60 Stellen, Modellradien nur aus k), kein u, keine χ-Integrale, keine U8-Aktion, keine Paarungen mit Cz oder D12Tz, kein Richtungstest, keine Aussage zur N12-Regel, zu W9, A9→A11, Objekt X oder RH. Keine Repositoryänderung.

## Dateien

- `shell_chi.py` — Aufbau des Schalenteils, Normen, Fehlertransport (Quelle der Zahlen oben).
- `checks.py`, `profile.py` — Gegenchecks und Punktprofil.
- `STUFE1_SHELL_RESULTS.json` — alle 4×96 Schalenkoeffizienten (60 Stellen), Normen, Radien, λ-Werte.
- `PSI_DEFINITION.json` — kompakte Definition von ψ_t für Stufe 2 (Schalenkoeffizienten, Kern-k, Momentquotienten, λ_total, μ).

## Übergabeprompt für Stufe 2 (kopierbar)

```
Objekt X, Stand 16.10.2026. Offen: PR #226 (Head 0ded564; Budgetpaket 7f712994…, N*Jp-Paket
b48e3895…), PR #227 (Head 5243737); #225 gemergt. Keine Mergeempfehlung.
Stufe 1 erledigt (Diagnose, kein Zertifikat): Schalenteil chi_t|(a8,b9) = Jt - sum F_i k_i als 96
ell_n-Koeffizienten je Paritaet/Richtung; ||chi_v|Schale||_X = 2013.598 (gerade) / 2199.971 (ungerade),
Randschicht an a8 (chi_v(a8+) = -22588 / -23984), k-Intervallfehler relativ 1.1e-4 / 1.9e-6.
Beobachtung: p = P_upper v ist bis 1e-14 parallel zu v, q = ||p||; chi_p = q chi_v.
Kern ohne u: -lambda_total m/mu - sum_{i<=4} k_i z_i mit Norm 6.53e6 / 3.59e6 (t=v).
Dateien: PSI_DEFINITION.json (psi_t = Lambda Jt - Fk als eine Funktion), STUFE1_SHELL_RESULTS.json.
Aufgabe Stufe 2: Pi8[Q^np_b9 psi_t]|(0,a8) fuer die eine Funktion psi_t berechnen (Kernintegrale mit
k(r)=e^{-r/2}/(1-e^{-2r}), Primverschiebungen q=2,3,4,5,7,8, Momentkorrektur Pi8, logarithmische
Randanteile an a8 und b9 wegen Sprung von psi_t), Stichprobe gegen getrennten Weg g r - sum k_i g_Fi.
Danach Stufe 3: U8-Aktion (A) mit 191 Funktionen B8*e_i, Phi_i aus OPERATORS.json / Common96.
Fehler gegen das tatsaechliche chi_t|Kern messen, nicht gegen 6.5e6. Untergrenzen fuer ||W9|| nie in
Fehlerobertests; audit_S getrennt von fixed_X. Kein globaler Abschluss.
```
