# Objekt X — Stufe 4 (Teil 1): Die Spike-Richtung ist A9-orthogonal zu den zwölf alten Quellen

Stand 16. Oktober 2026 · PR #226 Head 0ded564, PR #227 Head 5243737 (beide offen) · Diagnose mit rigoros begründeten Teilschranken · **kein Zertifikat, keine Repositoryänderung**

## Ergebnis in einem Absatz

Für alle zwölf alten Quellen Φ_j (Grade 2–24 bzw. 3–25) und beide Paritäten gilt im Mittelpunktmodell

ℓ_v(D_j) = ⟨χ_v, A9Φ_j⟩ = [⟨ψ_v,D_j⟩ − ⟨c,Φ*h8_j⟩] − ⟨y_f − B*c, y_h⟩/δ,

wobei die eckige Klammer aus zwei Zahlen der Größenordnung 10³–10⁵ besteht, die sich **auf 10⁻¹⁰ relativ aufheben** (Differenz 10⁻⁷ … 5·10⁻⁵), und der Restterm **rigoros** durch ‖y_f − B*c‖·‖y_h‖/δ ≤ 0,04–0,15 beschränkt ist (H_B ≥ BB* aus Common96). Zugleich ist der hohe Anteil der U8-Antwort auf f_v, (y_f − B*c)/δ, auf ≲ 10⁻³ (bei exaktem ‖f_v‖²) bzw. ≲ 0,5 (konservativ) beschränkt, gegen 1,3·10¹³ im niedrigen Anteil. Die riesige L²-Norm von χ_v (> 1,34·10¹³) ist deshalb für den N12-Test **irrelevant**: Die Spike-Richtung v ist in der A9-Form nahezu orthogonal zu allem, was die Antwortregel berührt. Der untere Skalartest (11/(10q))|ℓ_p(Rz)|² kann aus dem D12-Anteil heraus praktisch nicht scheitern; was den konservativen Vergleich entscheidet, sind die übrigen Energieterme von W9, nicht der Spike.

## Schritt 1: Energie-Cauchy–Schwarz-Test der geerbten Kette (bestanden)

Prüfidee: Für die weichste Mode u₁ des Common96-Kopfes (Horizont a₈) und die #227-Funktionen D_j = A9Φ_j (Horizont a₉) muss wegen Rückzugsverträglichkeit und Positivität gelten |⟨Φu₁, D_j⟩| = |a9[JΦu₁, Φ_j]| ≤ √(a_low[u₁])·√(A12_jj). Mit a_low[u₁] ≥ u₁ᵀ(F + H_B/δ)u₁ = 1,336·10⁻²⁶ (gerade; u₁ᵀFu₁ = 1,282·10⁻²⁶, u₁ᵀH_Bu₁ = 9,8·10⁻²⁸) bzw. 8,53·10⁻²⁴ (ungerade) ist die Schranke ≈ 1,2·10⁻¹³·√A_jj bzw. 2,9·10⁻¹²·√A_jj.

Rechnung: Φu₁ = U⁻¹MEu₁ als Polynom vom Grad ≤ 382 mit Mellin-Korrektur, D_j aus `FUNCTIONS12.json` (Polynom Grad 323 in t = x/a, V-Multiplikator, Momentterm, sieben Verschiebungspolynome), 150 Stellen, Gauss–Legendre 768 Knoten je Zelle, Zellgrenzen = Verschiebungsgrenzen.

| | I_j (gerade) | I_j / Schranke | I_j (ungerade) | I_j / Schranke |
|---|---|---|---|---|
| Spannweite über j = 0…11 | −1,5·10⁻¹⁴ … +9,4·10⁻¹⁵ | 0,02 … 0,17 | −4,9·10⁻¹³ … −9,0·10⁻¹⁴ | 0,02 … 0,16 |
| naive Skala ‖Φu₁‖·‖D_j|Kern‖ | 0,43 … 2,1 | | 0,68 … 1,9 | |

Ein explizites Integral löscht sich um 13–14 Stellen genau so aus, wie die Energieschranke verlangt. Das bestätigt numerisch (i) die Rückzugsverträglichkeit zwischen Common96 (a₈) und den D12-Funktionen (a₉), (ii) dass die weiche Mode auch an die hohe Kopplung praktisch nicht ankoppelt (u₁ᵀH_Bu₁ ≈ 10⁻²⁷), (iii) dass der u₁-Anteil von ℓ_v(D_j), nämlich ‖c‖·I_j, nur −0,11 … +0,13 (gerade) bzw. −0,50 … −0,09 (ungerade) beträgt.

## Schritt 2: Der hohe Anteil der U8-Antwort ist winzig

Aus Common96: ρ = ‖A_c*F_neu A_c − I‖ < 10⁻⁴⁰ ist der Kongruenzfehler; C·Cᵀ = F_neu⁻¹ mit F_neu ≤ A_low − H_B/δ, und H_B ≥ BB* (p = 10⁻¹⁰, also fast scharf). Damit ist ‖B*c‖² ≤ cᵀH_Bc exakt auswertbar:

| | gerade | ungerade |
|---|---|---|
| cᵀH_Bc (⇒ ‖B*c‖ ≤) | 18289,12103 (135,23728) | 21630,51668 (147,07317) |
| ‖y_f‖² = ‖f‖² + γ_m a_f² − ‖Φ*f‖² (7.1) | 18289,12054 (135,23728) | 21630,55051 (147,07328) |
| ⟨B*c, y_f⟩ = ⟨c, B·T_h f⟩ (Archiv) | 18289,12079 | 21630,53358 |
| ‖y_f − B*c‖² ≤ ‖y_f‖² − 2⟨B*c,y_f⟩ + cᵀH_Bc | 3,1·10⁻⁶ | 2,6·10⁻⁵ |
| ⇒ ‖(y_f − B*c)/δ‖ (hoher Anteil von U8 f_v) | ≤ 9,6·10⁻⁴ | ≤ 2,8·10⁻³ |
| zum Vergleich ‖Φc‖ | 1,345·10¹³ | 1,022·10¹² |

Vorbehalt: ‖f_v‖² stammt aus Quadratur (meine 22-stellige Netzrechnung und GPT 1's Evaluator stimmen auf 12 Stellen überein, also ‖f‖² auf ≈ ±0,6 absolut); konservativ ist daher ‖y_f − B*c‖ ≤ 0,8 zu setzen. Die Übereinstimmung der drei Zahlen 18289,1205/…1208/…1210 auf 7 Stellen ist selbst ein Dreiwegetest (Quadratur von f, Archivmodell B·T_h f, Common96-Matrix H_B) und bedeutet: U8 f_v ≈ Φc, die Antwort ist bis auf ≲ 10⁻³ (konservativ ≲ 0,5) rein niedriggradig. Damit ist GPT 2's offene „ganze hohe Antwortfunktion" für t = v auf eine kleine Zahl reduziert.

## Schritt 3: ℓ_v(D_j) über (7.2), alle Terme außer der B-Kopplung berechnet, B-Kopplung beschränkt

Zerlegung: ⟨χ_v,D_j⟩ = ⟨ψ_v,D_j⟩ − ⟨y_f,y_h⟩/δ − ⟨c,Φ*h8_j⟩ + ⟨B*c,y_h⟩/δ = [⟨ψ_v,D_j⟩ − ⟨c,Φ*h8_j⟩] − ⟨y_f − B*c, y_h⟩/δ, mit h8_j = Π8(D_j|Kern), y_h dessen hoher Anteil (‖y_h‖² = ‖h8‖² + γ_m a_h² − ‖Φ*h8‖²).

| j | Grad | ⟨ψ_v,D_j⟩ (gerade) | ⟨c,Φ*h8_j⟩ | Differenz | ‖y_h‖ | Rest ≤ (mit ‖y_f−B*c‖ ≤ 0,8) |
|---|---|---|---|---|---|---|
| 0 | 2 | −1696,602708 | −1696,602704 | −3,5·10⁻⁶ | 0,065 | 0,029 |
| 1 | 4 | −33563,740667 | −33563,740663 | −4,1·10⁻⁶ | 0,089 | 0,039 |
| 2 | 6 | −83998,443521 | −83998,443517 | −3,7·10⁻⁶ | 0,107 | 0,047 |
| 3 | 8 | −89174,275663 | −89174,275660 | −2,4·10⁻⁶ | 0,122 | 0,054 |
| 4 | 10 | 36612,285752 | 36612,285751 | +1,0·10⁻⁷ | 0,136 | 0,060 |
| 5 | 12 | 128287,347535 | 128287,347531 | +4,0·10⁻⁶ | 0,149 | 0,065 |
| 6 | 14 | −146491,937775 | −146491,937783 | +8,0·10⁻⁶ | 0,160 | 0,070 |
| 7 | 16 | 79377,421520 | 79377,421506 | +1,4·10⁻⁵ | 0,172 | 0,075 |
| 8 | 18 | −18644,744132 | −18644,744153 | +2,1·10⁻⁵ | 0,183 | 0,080 |
| 9 | 20 | 8917,211668 | 8917,211639 | +2,9·10⁻⁵ | 0,194 | 0,085 |
| 10 | 22 | −11358,350610 | −11358,350649 | +3,9·10⁻⁵ | 0,206 | 0,090 |
| 11 | 24 | 11050,067290 | 11050,067241 | +4,9·10⁻⁵ | 0,218 | 0,096 |

Ungerade analog: Werte bis 1,75·10⁵, Differenzen −1,9·10⁻⁵ … +9,4·10⁻⁶, ‖y_h‖ 0,10–0,27, Rest ≤ 0,045–0,117. Vollständige Zahlen in `D12_TERMS.json`.

Auch ⟨f_v,h8_j⟩ und ⟨Φ*f_v,Φ*h8_j⟩ stimmen auf 10⁻⁴ relativ überein (f_v niedriggradig), die Klammer ⟨y_f,y_h⟩/δ liegt bei −0,04 … −0,17 und wird vom B-Term bis auf den kleinen Rest kompensiert.

Deutung: ⟨χ_v, A9Φ_j⟩ ≈ 0 auf 10⁻¹⁰ relativ zur natürlichen Skala. Das ist die erwartete Spike-Eigenschaft — Jv hat Legendrekoeffizienten ~10⁻⁹ in den niedrigen Graden der alten Schale, ist also gegen glatte Schalenfunktionen (die Φ_j|Schale) orthogonal in genau dieser Größenordnung; über N A9Φ_j (Schur-Bild des Schalenanteils von Φ_j) überträgt sich das auf ℓ_v.

## Konsequenzen

1. **Für den unteren N12-Test.** ℓ_p(Rz) = ⟨χ_p, Cz⟩ − Σ_j (Tz)_j ℓ_p(D_j) mit ℓ_p = αℓ_v + ℓ_e, α ≈ 56620. Der D12-Anteil ist pro Quelle |ℓ_p(D_j)| ≲ 56620·(10⁻⁵ + 0,1) ≲ 6·10³ (konservativ) bzw. ≲ 1 (bei exaktem ‖f‖²); mit ‖T‖ < 6,8·10⁶ ist das als Obergrenze noch nicht klein genug, um die D12-Summe für beliebige z zu vernachlässigen — die Schranke muss durch den tatsächlichen Wert von ⟨y_f − B*c, y_h⟩ ersetzt werden (siehe nächste Schritte), der nach Schritt 2 um Größenordnungen kleiner sein dürfte. Für ⟨χ_p, Cz⟩ gilt dieselbe Struktur ⟨ψ_p,Cz⟩ − ⟨c_p,Φ*(Cz)_8⟩ − ⟨y_f−B*c, y_{Cz}⟩·α/δ; da Cz auf der alten Schale glatt bis auf die Log-Singularität bei a₉ ist (weit weg von der a₈-Wand, an der Jv sitzt), ist dieselbe Auslöschung zu erwarten — zu rechnen, nicht anzunehmen.
2. **Zur Artefaktfrage.** Die L²-Größen 10¹³ (χ_v) und 10³¹ (W9-Untergrenze) sind Koordinatenartefakte der weichen Mode (Eigenwert 10⁻²⁶); in der A9-Energie ist χ_v ein Objekt der Ordnung 1–10⁵, und die Spike-Richtung koppelt an die N12-Objekte nur über Energiepaarungen, die hier auf 10⁻¹⁰ verschwinden. Weder die U8-Majorante noch die K12-Untermatrix erzeugen für den N12-Test ein Hindernis aus dieser Richtung.
3. **Zur Normalisierung von Stufe 2.** Meine Stufe-2-Koeffizienten waren rohe ⟨eₙ,Uf⟩; Φ*f = ⟨eₙ,Uf⟩ − ⟨eₙ,m_s⟩a_f/m_e (Mellin-Korrektur) — damit stimmen drei unabhängige Wege auf 10⁻⁷ überein.

## Was gezeigt ist und was nicht

Gezeigt (Diagnose, Mittelpunktmodelle, Energie-Argumente am geerbten Datenbestand): I_j-Test, Schranke ‖B*c‖² ≤ cᵀH_Bc (rigoros gegeben c), Kleinheit des hohen U8-Anteils (bis auf ‖f‖²-Genauigkeit), alle (7.2)-Terme für h = D_j außer dem B-Term, dessen Betrag rigoros beschränkt ist. Nicht gezeigt: Intervallzertifikat; der kohärente k-Fehler (Δχ = −HΔk) ist nicht transportiert — nach dem Energieargument ist er ≲ η_v·O(1) ≈ 10⁻⁸·O(1), aber das ist Erwartung; ⟨χ_p, Cz⟩ für die neue Schale; ℓ_e; die zwölf vollständigen N12-Skalare; K_P[z]; W9-Energie; A9→A11; Objekt X; RH.

## Dateien

`softmode_pairings.py`, `SOFTMODE_PAIRINGS.json` (I_j, Schranken, u₁, Rayleigh-Quotient); `d12_terms.py`, `D12_TERMS.json` (alle Terme, Φ*h8_j je 191 Einträge, Normen); Bericht. Eingaben: #227-Archive b8677c0b… / 00a66e85… (D12-Funktionen aus dem eingebetteten Archiv 0a7bda3d…), Stufe-3-Paket ab7116f7… (c, Φ*f, B·T_h f, H_B, F, C), Stufe-2-Netz (f_v), PSI_DEFINITION v2 (ψ_v).

## Übergabeprompt (kopierbar, ersetzt alle älteren)

```
Objekt X, Stand 16.10.2026. PR #226 Head 0ded564, PR #227 Head 5243737, beide offen; keine Mergeempfehlung.
Regeln: lambda_total mit Minus; p = alpha v + e (e != 0); U8 = Common96-Majorante; C C^T = F_neu^-1,
F_neu <= A_low - H_B/delta, H_B >= B B*; rho = Kongruenzfehler < 1e-40.
Neu (Stufe 4 Teil 1, Diagnose): (a) Energie-CS-Test bestanden: |<Phi u1, D_j>| = 1e-14 (gerade) / 1e-13
(ungerade) <= sqrt(a_low[u1]) sqrt(A12_jj), Verhaeltnis 0.02-0.17, alle 24 Faelle. (b) Hoher Anteil von
U8 f_v: ||y_f - B*c||^2 <= ||y_f||^2 - 2<c,B T_h f> + c^T H_B c = 3e-6 / 2.6e-5 (bei exaktem ||f||^2;
konservativ ||y_f - B*c|| <= 0.8). (c) ell_v(D_j) = [<psi_v,D_j> - <c,Phi*h8_j>] - <y_f - B*c, y_h>/delta
mit Klammer = 1e-7..5e-5 (Aufhebung 1e-10 relativ) und |Rest| <= 0.04-0.15; Dateien D12_TERMS.json,
SOFTMODE_PAIRINGS.json. Deutung: Spike-Richtung v ist A9-orthogonal zu den 12 alten Quellen; die
L2-Groessen 1e13/1e31 sind Koordinatenartefakte der weichen Mode (Eigenwert 1e-26).
Naechste Schritte: (1) hohe U8-Antwort h_f = (y_f - B*c)/delta als Funktion oder zumindest
<h_f, y_h_j> exakt: B*c = sum_i c_i B8*e_i braucht die 191 ganzen Funktionen A8 Phi_i (Q^np_a8 auf
M E e_i: D_H, V-Log, q0, Gamma_a8 regulaer, Shifts q=2,3,4,5,7, Momentprojektion); weiche Mode und
Moden 2-3 in >=60 Stellen, Rest in double. (2) <chi_v, C z> fuer die neue Schale (a9,b=log(11)/2):
C z = Pi_a Q^np_b z|(0,a9), z = neue Schalenbasis bzw. die im N12-Gate benutzten Testfunktionen
(Definition in #227 klaeren: K_P = d - F*T - T*F + T*A12 T, d = volle neue Form), gleiche Zerlegung
<psi,Cz> - <c,Phi*(Cz)_8> - <h_f, y_Cz>. (3) ell_e (Richtungsrest) mitfuehren. (4) kohaerenter k-Fehler
Delta ell = -sum_i Delta k_i <F_i - J U8 g_Fi, D_j> ueber archivierte c_F, b_F; Energieargument liefert
~eta_v O(1) = 1e-8. (5) Erst dann 11/(10q) dist(0, ell_p(Rz))^2 gegen K_P[z]_upper.
Untergrenzen fuer ||W9|| nie als Fehlerobergrenzen; audit_S getrennt von fixed_X; kein globaler Abschluss.
```
