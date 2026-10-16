# Objekt X — Audit der Rückgaben GPT 1 (Stufe-2-Prüfung, 191 Paarungen) und GPT 2 (endlicher Stufe-3-Abschluss)

Stand 16. Oktober 2026 · PR #226 Head 0ded564 (offen), PR #227 Head 5243737 (offen, live bestätigt) · **keine Repositoryänderung, keine Mergeempfehlung**

## Was ich reproduziert habe

| Gegenstand | Ergebnis |
|---|---|
| GPT-2-Paket `ab7116f7…6b52`: `certify_stage3.py` mit Brückenarchiv b48e3895… | **PASS**; `FINITE_ACTION.json` und `RECEIPT.json` bytegleich reproduziert |
| GPT-1-Anhänge (`AUDIT.json`, `STUFE3_PAIRINGS_DIAGNOSTIC.json`) | Eingangsarchiv 62e9f6d8… = mein Stufe-1v2/2-Paket; Status laut Datei „numerische Diagnose, keine Intervalle" |
| c₀ = C·Cᵀd₀/(1−ρ) aus `d_model` und der Kongruenzmatrix (REFINED_COMMON96) unabhängig mit mpmath, 60 Stellen | ‖c₀‖ = 1,345361021394·10¹³ (gerade), 1,022028928866·10¹² (ungerade) — identisch mit dem Archivmittelpunkt, max. Abweichung 3·10⁻³² |
| GPT 1 (Quadratur, 14 080 Knoten) gegen GPT 2 (Archivmodell c_J t − c_F k₀), alle 191 Einträge je Parität | max. Abweichung 2,8·10⁻¹⁰ absolut, 1,5·10⁻¹¹ relativ (gerade); 1,7·10⁻¹⁰ / 6·10⁻¹² (ungerade). GPT-1-Werte liegen erwartungsgemäß **nicht** in den 10⁻⁶⁴-Intervallen des Archivmodells (die beschreiben nur das Modell) |
| Meine Stufe-2-Koeffizienten ⟨eₙ,Uf⟩ gegen Archiv-Φ*f | Nach Mellin-Korrektur Φ*f_n = ⟨eₙ,Uf⟩ − ⟨eₙ,m_s⟩·a_f/m_e stimmen Grade 2–8 (bzw. 3–9) auf ≤ 7·10⁻⁷. Meine ausgegebenen Koeffizienten waren **rohe** Koordinaten, nicht Φ*f; die Differenz (Grad 2: 62,7; Grad 4: 0,36; Grad 6: 8·10⁻⁴) ist genau der Momentträgeranteil. Für Grad ≥ 20 bestätigt sich GPT 1's Hinweis: mein 12-Knoten-Netz ist dort unzuverlässig (Grad 60: 250,375 statt 249,857) |

Damit sind Φ*f_v auf drei unabhängigen Wegen (meine mpmath-Quadratur, GPT 1's analytisch zerlegter Evaluator, GPT 2's Archivmodelle) konsistent. Das ist ein echter Dreiwegetest der Kette ψ → Q^np → Π8 → Φ*, nicht nur ein Replay.

## Algebraische Kontrollen der Herleitung von GPT 2

- (2.2) E*U(U8 f) = c: UΦc = MEc = Ec − e_σ⟨m_s,Ec⟩/m_e hat E-Koordinaten c; UT_h*z = Mz für z ∈ Y hat keine E-Koordinaten. **Richtig.**
- (5.1) ‖χ‖² = W_X[s] + ‖w₀ − U8f‖² ≥ ‖E*Uw₀ − c‖²: Orthogonalität von Λs und J_old(·) in H9 (Momentnullheit von w₀ − U8f) plus Koordinatenabschätzung in einer ON-Basis. **Richtig.**
- (7.1) ⟨T_h f, T_h h8⟩ = ⟨f,h8⟩ + γ_m a_f a_h − ⟨Φ*f,Φ*h8⟩: M*x = x − m_s⟨e_σ,x⟩/m_e; die gemischten Terme verschwinden, weil ⟨Uf, m_s⟩ ∝ ∫mf = 0 für f, h8 ∈ H8; E ⊕ Y zerlegt e_σ⊥. **Richtig.** (7.2) folgt mit ⟨χ,h⟩ = ⟨ψ,h⟩ − ⟨U8f, h8⟩ und U8 = T_h*T_h/δ + V*V/(1−ρ). **Richtig.**
- (4.2) ‖c − c₀‖ ≤ ‖C‖_HS(e_fix + e_k)/√(1−ρ): folgt aus c = C·Vf/(1−ρ) und der Featurefehlerabschätzung. Die Eingaben E_F, E_J, η_t sind geerbte Voraussetzungen, die ich nicht geprüft habe.
- W9-Folgerung (6): wie schon im Stufe-2-Bericht am Beweistext (A9_INVERSE_PROOF (6.4)) nachvollzogen.

## Neue Struktureinsicht (eigene Rechnung, Diagnose)

Singulärwertzerlegung der Kongruenzmatrix C (191×191, obere Dreiecksmatrix, Doppelgenauigkeit, nur Größenordnungen):

| | gerade | ungerade |
|---|---|---|
| größter Singulärwert s₁ von C | 8,83·10¹² | 3,47·10¹¹ |
| ⇒ kleinster Eigenwert des A8-Kopf-Grams ≈ 1/s₁² | **1,3·10⁻²⁶** | **8,3·10⁻²⁴** |
| Konditionszahl des Kopf-Grams | 6·10²⁶ | 9·10²³ |
| weichste Mode u₁ (Grade/Gewichte) | 6: 0,61; 8: −0,51; 4: −0,48; 10: 0,30; 2: 0,20; 12: −0,11 | 7: 0,62; 9: −0,54; 5: −0,44; 11: 0,30; 3: 0,16 |
| Anteil von c in u₁ | 99,99 % | 99,99 % |
| Verstärkung ‖c‖/‖d‖ | 5,7·10⁷ | 3,8·10⁶ |

Folgerungen:

1. **Der riesige Kern von χ_v ist eine einzige weiche Mode.** c ≈ s₁²·(u₁·d)·u₁/(1−ρ). Aus ‖c‖ = 1,35·10¹³ und s₁² = 7,8·10²⁵ folgt u₁·d ≈ 1,7·10⁻¹³ bei ‖d‖ = 2,4·10⁵ — d ist zur weichsten Mode auf 7·10⁻¹⁹ relativ orthogonal. In doppelter Genauigkeit ist das nicht auflösbar (ich erhalte 2⁻³⁷ als Rundungsartefakt, identisch in beiden Paritäten). GPT 2's Aussage, eine Doppelgenauigkeitsrechnung „wich stark ab", ist damit erklärt, und der 180-Stellen-Weg ist zwingend. Mit Cauchy–Schwarz in der Form ist die Kleinheit auch zu erwarten: |q[Φu₁, ψ]| ≤ √λ_min·√q[ψ,ψ] ≈ 10⁻¹³·√q[ψ,ψ], d. h. ψ hat trotz L²-Norm 6,5·10⁶ eine Formenergie von Größenordnung 1 — ψ lebt in den weichen Moden, wie es für einen Schur-Rest zu erwarten ist.
2. **Untere Schranke für die tatsächliche A9-Inverse (Min-Max, bedingt).** Wegen der Rückzugsverträglichkeit ist die A9-Form auf J_old w gleich der A8-Form auf w; also λ_min(A9) ≤ λ_min(A8|H8) ≤ Rayleigh-Quotient von Φu₁ ≈ 1,3·10⁻²⁶ (plus Modellfehler des Kopf-Grams). Damit **‖A9⁻¹‖ ≥ ≈7,8·10²⁵ (gerade), ≈1,2·10²³ (ungerade)** — unter denselben geerbten Gram-Voraussetzungen. GPT 2 hat dies ausdrücklich nicht behauptet; es folgt aber elementar. Die W9-Untergrenze 1,1·10³¹ liegt somit „nur" fünf Größenordnungen über dem, was jede Majorante von A9⁻¹ mindestens haben muss. Das verschiebt die Artefaktfrage: nicht W9 ist unplausibel groß, sondern **das Problem selbst ist in Richtung Φu₁ extrem schlecht konditioniert.**
3. **Konsequenz für den N12-Test.** Mit χ_p ≈ 7,6·10¹⁷ fast vollständig in Richtung J_old Φu₁ lautet die Forderung des konservativen Vergleichs |⟨J_oldΦû₁, Rz⟩| ≲ √(B_up·10q/11)/7,6·10¹⁷. Der Test ist also eine Aussage darüber, ob die eingefrorene Regel A9_A11_N12_MIDPOINT_INVERSE_60_V1 die weichste Mode des A8-Kopfes auf ~10⁻¹⁷ relativ erfasst. Ist die Regel aus denselben Gram-Daten gebaut, kann das gelingen; ist sie es nicht, ist CERTIFICATE_FAIL des **konservativen Vergleichs** praktisch sicher — und zwar als Folge der Konditionierung, nicht als Aussage über A9⁻¹ oder RH. Das ist genau die Richtung, in der GPT 2's §7 zu rechnen ist.
4. **Fehlerbudget für Stufe 4.** c ist nur auf 0,4 % (gerade: 5,2·10¹⁰ von 1,35·10¹³) bzw. 8·10⁻⁵ (ungerade) bekannt; der k-Fehler dominiert. ℓ_p(Rz) wird daher ein Intervall mit ≥ 0,4 % relativer Breite; der Test entscheidet über dist(0, ℓ_p)² gegen B_up. Rundungsfehler aller Paarungen sind gegen diesen Entscheidungsabstand zu messen, nicht gegen ‖χ‖.

## Offene Punkte an GPT 2 (Prüfbitten, keine Einwände)

- Die Rayleigh-Quotienten-Folgerung oben benötigt, dass der Kopf-Gram tatsächlich die A8-Form in der ON-Basis MEe_i darstellt (nicht eine umskalierte Variante) und dass dessen Modellfehler ≪ 10⁻²⁶ ist. Bitte gegen die Common96-Definition prüfen; falls bestätigt, als eigenständiges bedingtes Resultat registrieren.
- Die Quelle der tatsächlichen Kopplung u₁·d ≈ 1,7·10⁻¹³: Zerlegung in den A8w₀-Anteil und den Schalenkopplungsanteil g s_t (GPT-Identität f = A8w₀ + g s_t) wäre aufschlussreich, da A8w₀ nach Konstruktion kaum in u₁ koppeln dürfte.

## Stufe 4: Datenlage und Plan

PR #227 (Head 5243737, live bestätigt) enthält die zwei Archive `Objekt-X-Vollstaendiger-Antwortgram-und-Scharfer-Modellfehler-2026-10-15.zip` und `…-Nachtrag-Breitenpruefung-und-W9-Klarstellung-2026-10-15.zip`; FUNCTIONS12.json / FROZEN_RESPONSE12.json müssen darin liegen (nicht geöffnet). Für (7.2) je z und Parität nötig: ⟨ψ_t,h⟩ auf (0,b₉) inkl. Schale; ⟨f_t,h8⟩ als ganze L²-Paarung (f_t mit Log-Randterm und neun Sprüngen, GPT-1-Evaluator geeignet); a_h; Φ*h8 (191 Paarungen); Vh8 = C*(Φ*h8 − B·T_h h8/δ) — der Term B·T_h h8 braucht die hohen Kopplungsdaten für h; falls h = C_p z, D12Tz nicht aus archivierten Quellen linear zusammensetzbar sind, ist das der eigentliche Rechenblock (191 ganze Funktionen B8*e_i). Fehler: gemeinsames K-Ellipsoid für Δk, p direkt oder e bezahlen, alles gegen den Entscheidungsabstand.

## Redaktionelles

`STUFE1_BERICHT.md` v2: die überholten Passagen (Plus-Formel, „q = ‖p‖", alter Übergabeprompt) sind jetzt im Text als ÜBERHOLT markiert, der Korrekturkopf verweist darauf. Das Stufe-1-Paket bleibt Diagnose, nicht Zertifikat.

## Übergabeprompt für Stufe 4 (kopierbar, ersetzt alle älteren)

```
Objekt X, Stand 16.10.2026. PR #226 Head 0ded564, PR #227 Head 5243737, beide offen; #225 gemergt.
Keine Mergeempfehlung. Bindungen: Budget 7f712994…, N*Jp b48e3895…, global 2ca3c682…,
Stufe-1-Zertifikat 940cd40e…, Stufe-1v2/2-Diagnose 62e9f6d8…, Stufe-3-Paket ab7116f7… (PASS, bytegleich).
Regeln: lambda_total = lambda(r) - sum k_{4+j} lambda(Y_j) (Minus). p = alpha v + e, e != 0;
ell_p = alpha ell_v + ell_e. U8 = Common96-Majorante, U8 A8 != I. C, C* nicht vertauschen.
Stand: Phi*f_v dreifach konsistent (Quadratur GPT1, Archivmodell GPT2, eigene mpmath+Mellin, <=1e-6).
c = E*U(U8 f) fuer v,p,e je Paritaet gerichtet eingeschlossen: ||c_v|| = 1.3454e13 / 1.0220e12,
Fehler 5.2e10 / 8.5e7. ||chi_v|| > 1.34e13 / 1.0219e12; ||W9|| > 1.11e31 / 1.07e28 (Majorante).
Struktur: c liegt zu 99.99% in der weichsten Mode u1 des A8-Kopf-Grams (Eigenwert ~1.3e-26 gerade,
8.3e-24 ungerade; Polynom Grade 2-12 bzw. 3-13); Kopplung u1.d ~ 1.7e-13 nur mit >=60 Stellen
aufloesbar. Min-Max: ||A9^-1|| >= ~7.8e25 / 1.2e23 (bedingt, zu pruefen).
Aufgabe Stufe 4: fuer die 12 zulaessigen z der Regel A9_A11_N12_MIDPOINT_INVERSE_60_V1 (#227-Archive)
h = C_p z bzw. D12 T z, h8 = Pi8 h|core; Skalar nach HERLEITUNG §7 (7.2):
<chi_t,h> = <psi_t,h> - [<f_t,h8> + gamma_m a_f a_h - <Phi*f_t,Phi*h8>]/delta - <Vf_t,Vh8>/(1-rho),
mit ganzer L2-Paarung <f_t,h8> (Log-Randterm, neun Spruenge), Phi*h8 (191), Vh8 inkl. B T_h h8.
Fehler: gemeinsames K-Ellipsoid fuer Delta k, Quellfehler E_F/E_J, p direkt oder e bezahlen,
alles gegen den Entscheidungsabstand; dann 11/(10q) dist(0, ell_p)^2 gegen B_up.
Erwartung (Heuristik, nicht Ergebnis): Test entscheidet, ob die Regel die Mode u1 auf ~1e-17 erfasst.
CERTIFICATE_FAIL waere Aussage ueber den konservativen Vergleich, nicht ueber A9^-1 oder RH.
Untergrenzen fuer ||W9|| nie als Fehlerobergrenzen; audit_S getrennt von fixed_X; kein globaler Abschluss.
```
