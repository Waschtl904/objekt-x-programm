# Active Theorem Registry

> **Stand:** 1. September 2026  
> **Aktuelle mathematische Merge-Basis:** `main` mit mathematischer Basis durch PR #48 (Pre-Doku-Sync SHA `cf3d39a2e7787bc1c5b938390b6cdeec7943b0c2`). Der explizite Small-`R`-M1-ND-Gegenvektor ist `✓[M]_neg`. PR #49 (`research/sw1-m1-nd-salvage-phase-diagram`, Head `2ed1583f074574c2fdb5a48203d63d520a86b5f6`, Run `33532345053` SUCCESS) ist ein **offener, eingefrorener AI-GREEN candidate** für einen uniformen negativen Wedge und ist nicht promotet. Aktive Forschungsachse ist derzeit B / Strong Terminal, zunächst R27-F. Frühere Promotions-/Certificate-Aussagen behalten ihre eigenen Provenienzen.  
> **Zweck:** operative, nicht exhaustive Registry der Resultate, die für die aktuelle P11/R32-SW1-/Schur-Front tatsächlich benötigt oder unmittelbar angrenzend sind.  
> **Nicht-Zweck:** Ersatz für \`STATUS.md\`, \`OFFENE_PROBLEME.md\`, die Papers oder Promotionsrecords.

Diese Datei ist eine **Navigations- und Abhängigkeitsregistry**. Eine Statuszeile hier erzeugt keine Promotion. Bei Konflikten gilt die kanonische mathematische Quelle des jeweiligen Resultats.

---

## 0. Statusnomenklatur (verbindlich ab 28. August 2026, Subtypen ergänzt)

| Bezeichnung | Bedeutung |
|---|---|
| **AI-GREEN candidate** | Interne KI-Konstruktion plus kritische Zweitprüfung. **Keine** externe Begutachtung. Dies ist der Default-Status für jeden Kandidaten ohne dokumentierte externe Prüfprovenienz. |
| **independent GREEN** | Unabhängige Prüfung des **exakten** Heads/Satzes; siehe Subtypen unten. Methode, Prüfer/System, exakter Head und Scope **müssen** dokumentiert sein. |
| **\`✓[M]\`** | Formaler Objekt-X-interner Promotionsstatus. Orthogonal zu \`independent GREEN\` — unabhängig davon, ob zusätzlich externe Begutachtung existiert. |

### 0.1 Subtypen von \`independent GREEN\` (kumulativ buchbar)

| Subtyp | Bedeutung | Pflichtangaben |
|---|---|---|
| **independent GREEN (cross-model)** | Separates Modell/System prüft den exakten Satz **ohne Kenntnis** der Zielrechnung (frische Session, kein Zugriff auf den Konstruktions-Thread). Kennt die prüfende Session bereits die Zielformel/den Thread, gilt das Ergebnis nur als „cross-model nonblind“ und zählt **nicht** als \`independent GREEN\`. | Typ, Methode, Prüfer/System (inkl. Blind-/Nonblind-Vermerk), exakter geprüfter Head, exakter Satz/Scope, Verdict |
| **independent GREEN (certificate)** | Reproduzierbares maschinelles/algebraisches Zertifikat (z. B. Python/SymPy/CAS-Skript) für den endlichen algebraischen Teil. | zusätzlich: Tool/Version, Zertifikatsdatei/Skriptpfad, exakter geprüfter Git-Head, reproduzierbares Ergebnis |
| **independent GREEN (human)** | Unabhängige Prüfung durch einen externen Menschen. | zusätzlich: Reviewer/Review-Provenienz |

**Verbindliches Buchungsschema für jede \`independent GREEN\`-Zeile:**
\[
\boxed{
\text{Typ}+\text{Methode}+\text{Prüfer/System}+\text{exakter Head}+\text{exakter Satz/Scope}+\text{Verdict}
}
\]
Fehlt eine Angabe, gilt die Buchung als unvollständig und darf nicht als \`independent GREEN\` gezählt werden. Subtypen sind **kumulativ**: z. B. \`AI-GREEN + independent GREEN (cross-model) + independent GREEN (certificate)\` ist zulässig und suggeriert **keine** \`independent GREEN (human)\`-Prüfung.

**Rechtsverbindliche Klarstellung:** Alte Bezeichnungen wie \`independently GREEN candidate\`, \`OVERALL GREEN candidate\` oder \`CANDIDATE GREEN\` in früheren Versionen dieser Datei galten **nicht automatisch** als \`independent GREEN\` im obigen Sinn. Ohne dokumentierte externe Prüfprovenienz (Methode, Reviewer/System, exakter Head) werden sie ab jetzt als \`AI-GREEN candidate\` verstanden. Diese Registry wurde entsprechend normalisiert (siehe Abschnitt 2). Diese Regel gilt ex ante und darf nicht nachträglich an ein gewünschtes Ergebnis angepasst werden.

---

## 1. Formell bewiesener Input

| ID | Status | Aussage / Scope | Kanonische Quelle | Rolle an der aktuellen Front |
|---|---|---|---|---|
| **P12-RT** — A15.1 consolidated all-radius restricted-tail injectivity | \`✓[M]\` | Für \(2a<T_0<c\), \(0<R<S<T_0\), im mixed strip \(T<S<T_0\) gilt insbesondere für \(0<R<T,\ \sigma=S-T\le R\): \(\ker L_{R,S,T_0}^{\{a,b,2a\}}=\{0\}\). | \`papers/P12_Adelic_Hub_Injectivity_Program.tex\`, Corollary \`cor:p12-consolidated\`; Statusbemerkung unmittelbar danach | Liefert auf SW1 die **äußere Hub-Injektivität**. Wenn die innere Schur-/Full-Rest-Elimination \(y=0\) erzwingt, steht für den äußeren Hub bereits ein \`✓[M]\`-Input bereit. |

**SW1 liegt vollständig im P12-RT-Scope:** Aus
\[
0<\sigma\le R<\varepsilon,\qquad R+\varepsilon<\Delta
\]
folgt
\[
T<S=T+\sigma<T_0=T+\varepsilon<c,
\qquad
0<R<T,
\qquad
\sigma\le R.
\]

---

## 2. AI-GREEN geprüfte Kandidaten — keine formale Promotion

| ID | Status | Inhalt | Kanonische Quelle | Verwendung |
|---|---|---|---|---|
| **HT-A1** | AI-GREEN candidate | wordwise Tail-Aktion; \(44\to24\to16\)-Selektion | \`audits/P11_R32_TAIL_FG_PIVOT_CANDIDATE.md\` | Rohmaterial für die Tail-/Full-Rest-Zeilen |
| **HT-A2** | AI-GREEN candidate | Tail-Kompression / skalarer Pivot, insbesondere \(P_{\mathcal T_R}(I+A)P_{\mathcal T_R}=(1+\kappa)I\) | dieselbe Datei | liefert den invertierbaren Tail-Pivot |
| **HT-A3** | AI-GREEN candidate | Off-tail-Shell-Klassifikation | dieselbe Datei | kontrolliert Shell-Überlappungen / A-Walls |
| **HT-A4a** | AI-GREEN candidate | FG-Klassifikation der sechs Tail-Argumente | dieselbe Datei | allgemeiner Kandidatenhintergrund; für SW1-M soll diese Blackbox nicht benötigt werden |
| **FG-1** | AI-GREEN candidate — keine formale Promotion | Branch-/Gluing-Klassifikation des unsichtbaren Kerns | **Statusbuchung:** \`00-uebersicht/P11_R32_STATUS_2026-08-25.md\`, Update 2026-08-26; **Beweis-/Auditprovenienz:** \`audits/P11_R32_INVISIBLE_FIBER_GRAPH_CLASSIFICATION_AUDIT.md\` plus Exhaustivitätsabschluss | allgemeine Kernelgeometrie |
| **FG-TR1** | AI-GREEN candidate — keine formale Promotion | \(\Theta_R\) als beschränkter Koordinatenisomorphismus; \(L_R=\operatorname{pr}_1\Theta_R\) | **Statusbuchung:** \`00-uebersicht/P11_R32_STATUS_2026-08-25.md\`, Update 2026-08-26; **Beweis-/Auditprovenienz:** \`audits/P11_R32_TRIANGULAR_ROW_SPLITTING_AUDIT.md\` | freie Koordinaten / Rekonstruktionshintergrund |
| **\(\widehat\Phi_R\)-Normalform** | AI-GREEN candidate als mechanische Komposition | \(E_I^*H\,\widehat\Phi_R(z,f,h)=f\) | \`00-uebersicht/P11_R32_STATUS_2026-08-25.md\`, Update 2026-08-26; Provenienz dort angegeben | Parametrisierung der augmentierten Rechnung |
| **CG-FG1** | AI-GREEN candidate als Kompositionsreduktion | \(\Gamma_I=\operatorname{pr}_2\Gamma_R=E_I^*HBH^*E_{\mathcal A}=M_I^*M_A\) | \`00-uebersicht/P11_R32_STATUS_2026-08-25.md\`, Update 2026-08-26 | verbindet freie Koordinaten mit dem offenen Schur-Cross-Gram-Test |
| **SW1-KNF** | AI-GREEN candidate — keine formale Promotion | sektorale, vollständige Kernel-Normalform auf SW1: \(\mathcal K_R\cong\mathcal Z_R^+\oplus L^2(\mathcal V_R^{SW1})\) via paarweise disjunkter Samplingfenster \(I_a,I_b,I_T\); ersetzt FG-TR1/FG-1 als Blackbox ausschließlich auf SW1 | \`audits/P11_R32_SW1_KNF_CANDIDATE.md\` (PR #15, Squash-Merge \`0c98c03a332dc7c8e479edc77d8cada678eec376\`) | liefert die vollständige Koordinatenparametrisierung des inneren Kernels als Ausgangspunkt für SW1-BL7/SW1-2TP; keine Aussage über A0, HT-RED oder \(\ker\Gamma_I\) |
| **SW1-A-FOLD** | AI-GREEN candidate + **independent GREEN (certificate, algebraic/mechanical scope)** — keine formale Promotion | unitäre Odd/even-Halbachsenfaltung des augmentierten Systems; beide Odd-Extensions \(\mathcal O_{R,S}\) und \(\mathcal O_{0,R}\) explizit bijektiv mit \(O^{-1}O=I\), \(OO^{-1}=I\); innerer Hub = KNF-Row; Annulus-Hub = RB/P12-Operator; alle elf \(K^*M_\Omega K\)-Wörter unter unitärer Konjugation koeffizienten-/vorzeichentreu; \(\sigma\le R\)-Firewall bleibt literal | `audits/P11_R32_SW1_A_FOLD_RECONCILIATION_AUDIT.md`, geprüfter Audit-Blob `d89d3138421fbe2e9d2ef6bbd52019f620be545e`; Zertifikat `scripts/certify_sw1_a_fold.py`, geprüfter Blob `f6259057cc13e16799173806d5c9338decf44c9c`; Run `33331523196`, Job `99310781403`, Head `ba1cee8fd0507aebd88349daf90160f55755e357`; PR #38, Squash-Merge `b3d5b9880c649455a486e0d7b2a627de814b0932` | schließt die Vollraum↔Halbachse↔A0/A1-Brücke; **keine** Cross-Gram-Injektivität |
| **SW1-BL7** | AI-GREEN candidate — keine formale Promotion | siebter direkter Blindwert: \(s\in(R,\varepsilon)\Rightarrow 2d+s\in(a+R,b-R)\subset\mathcal Z_{R,\mathrm{SW1}}^{\rm phys}\), für jedes \(s\), Neuheit gegen die sechs promoteten Blindwerte elementar gezeigt | \`audits/P11_R32_SW1_BL7_CANDIDATE.md\` (PR #16, Squash-Merge \`5740a38ad4c24e27b7352512e57fb095b245e4d5\`) | Hilfslemma für die \(2d\pm s\)-Row im Rahmen des späteren \(\Delta\)-Descent; keine Aussage über SW1-2TP, SW1-AWI, HT-RED, A0 oder \(\ker\Gamma_I\) |
| **SW1-2TP** | AI-GREEN candidate + **independent GREEN (certificate)** — keine formale Promotion | simultaner \(T\pm s\)-2×2-Pivot: aus den elf Wörtern von \(A\) folgen die gepaarten Rows mit \(M_T=\begin{pmatrix}1+\kappa&\beta_T\\\beta_T&1+\kappa\end{pmatrix}\), \(\beta_T=-\tfrac58\log2\), beide Eigenwerte strikt positiv; im Summenkanal cancelt \(q\,w(s)\), im Differenzkanal erscheint \(2q\,w(s)\) | `audits/P11_R32_SW1_2TP_CANDIDATE.md`; Zertifikat `scripts/certify_sw1_2tp_ledger.py`; PR #17, Squash-Merge `dcbe0b005c03f6480693f79ff0d6db5f7ef34ae1`; Zertifikat: Python/SymPy 1.14.0, finaler geprüfter Head `d39b8603adb373ae31471e863c72b555b804020a`, PASS | liefert die uniforme simultane Elimination von \(y(T+s),y(T-s)\); Perplexity-Blindcheck dokumentiert FAIL, daher **kein** independent GREEN (cross-model); keine Aussage über SW1-AWI, \(\Delta\)-Descent, HT-RED, A0 oder \(\ker\Gamma_I\) |
| **SW1-AWI** | AI-GREEN candidate + **independent GREEN (certificate)** — keine formale Promotion | vollständige A-Wall-Dichotomie auf SW1: für \(\varepsilon<\Delta/2\) kein Überlapp, bei \(\varepsilon=\Delta/2\) nur L²-nulliger Berührpunkt, für \(\varepsilon>\Delta/2\) Überlapp \(J=(\Delta-\varepsilon,\varepsilon)\) mit maßtreuer Involution \(s\mapsto\Delta-s\); zugehöriger Reflexionsblock \(\beta_+I+\beta_bR_\Delta\) auf symmetrischem/antisymmetrischem Kanal strikt invertierbar | `audits/P11_R32_SW1_AWI_CANDIDATE.md`; Zertifikat `scripts/certify_sw1_awi.py`; PR #18, exakter finaler Review-Head `fe489896af592940a6d63e0395f215ab65d2540b`, Squash-Merge `9c1d2e8cfb0ea2b1b271c0d5ece95ec022cfbac9`; Python/SymPy 1.14.0, Vollzertifikat PASS | normalisiert die gesamte A-Wall-Kopplung ohne neue unkontrollierte Freiheit; Perplexity-Blindreview PARTIAL/FAIL, daher **kein** independent GREEN (cross-model); noch kein \(\Delta\)-Descent, HT-RED, A0 oder \(\ker\Gamma_I\)-Schluss |
| **SW1-Δ-DESCENT** | ?[O] als Gesamtknoten; Stages 1/2–12 im expliziten endlichen Scope AI-GREEN + **independent GREEN (certificate)** | äußere Δ-Schalen, reflektierte B-Zentrum-Geometrie und innerer KNF-Sample-Summand wurden stufenweise geschlossen; der blinde Summand \(\mathcal Z_R^+\) und damit der Gesamt-Descent bleiben offen | audits/P11_R32_SW1_DELTA_DESCENT_CANDIDATE.md und zugehörige Zertifikate; PR #19, Squash-Merge 3033a5062cfe799772b0faa564d078d5d6792337 | gemergter Kandidatenstrang; **keine Promotion**, kein HT-RED |
| **SW1-A0** | AI-GREEN candidate + **independent GREEN (certificate)** — keine Promotion | exhaustive Full Free-Coordinate Coverage von \(\mathcal Z_R^+\oplus L^2(\mathcal V_R^{SW1})\), einschließlich Horizontschwanz | audits/P11_R32_SW1_A0_COVERAGE_CANDIDATE.md; Zertifikat scripts/certify_sw1_a0_coverage.py; PR #20, Squash-Merge db6251a2e9dd3dfa0d665c725b26c4aabe2de73c | Coverage, **nicht** Injektivität |
| **SW1-A1** | AI-GREEN candidate + **independent GREEN (certificate)** — keine Promotion | vollständiges operatorwertiges finite-cell Rohsystem der ersten augmentierten Gleichung; finite cells \(\neq\) finite Dimension | audits/P11_R32_SW1_A1_FINITE_CELL_RAW_OPERATOR_CANDIDATE.md; Zertifikat scripts/certify_sw1_a1_raw_archetypes.py; PR #21, Squash-Merge 1aa6942f0b5acbcd9cc9f898cf3f8102db00f956 | Rohoperator, keine Injektivität |
| **SW1-A2** | AI-GREEN candidate + **independent GREEN (certificate, algebraic/mechanical scope)** — keine Promotion | kanonische schiefe Annulusprojektion \(Q_{\mathscr T,K}\), exakte Schur-Kernelreduktion und Cross-Gram-Reconciliation; unendlichdimensionale Hilbertraumschritte separat adversarial auditiert | audits/P11_R32_SW1_A2_ANNULUS_PROJECTION_CANDIDATE.md; Zertifikat scripts/certify_sw1_a2_annulus_projection.py; PR #29, Squash-Merge 1b2fc769b00d5b0dfe3c4bd9b4e4ec53617158c9 | korrekte Operatorreduktion; **keine Injektivität** |
| **SW1-A3** | AI-GREEN candidate + **independent GREEN (certificate, algebraic/mechanical scope)** — keine Promotion | positiver freier Gramoperator \(\mathfrak G_R=J_R^*(I+A)J_R\), Coercivität, Variationsform und Identität \(G^{-1}P_K=J_R\mathfrak G_R^{-1}J_R^*\); Hilbertraumteil separat auditiert | audits/P11_R32_SW1_A3_FREE_COORDINATE_GRAM_CANDIDATE.md; Zertifikat scripts/certify_sw1_a3_free_gram.py; PR #30, Squash-Merge e877834babf2fe551e4f13b2b6ce89bb917d743f | Ausgangspunkt der freien Gram-/Residualanalyse |
| **SW1-A4** | AI-GREEN candidate + **independent GREEN (certificate)** — keine Promotion | oberer Chamber: irrationale Rotation als Strategieno-go gegen exhaustive finite physische Punktorbits; kein No-Go gegen Schur-Injektivität | audits/P11_R32_SW1_A4_IRRATIONAL_ROTATION_NOGO_CANDIDATE.md; PR #24, Squash-Merge 637e63d23540bc4d7498fd5a7df30056be035eed | obere-Chamber Struktur |
| **SW1-A5** | AI-GREEN candidate + **independent GREEN (certificate)** — keine Promotion | Zwei-Blatt-Transfer modulo \(L=a-\Delta\); keine dritte irrationale Phase | audits/P11_R32_SW1_A5_TWO_SHEET_TRANSFER_CANDIDATE.md; PR #25, Squash-Merge 99d853c211ec17e657ede78af791c6a600a875e5 | finite Blätter über irrationaler Basis |
| **SW1-A6** | AI-GREEN candidate + **independent GREEN (certificate)** — keine Promotion | unterer Chamber: A4-Rotationsmechanismus mit offenem Hole, endliche kontrahierte Segmente | audits/P11_R32_SW1_A6_ROTATION_HOLE_CANDIDATE.md; PR #26, Squash-Merge f7bad5ad9945d9815251d027d694c5f4e4d0b564 | nur Rotationssubgraph |
| **SW1-A7** | AI-GREEN candidate + **independent GREEN (certificate)** — keine Promotion | vollständiger roher A1-Punktgraph als 6-State-, Range-3-Cocycle über einer irrationalen Kreisrotation | audits/P11_R32_SW1_A7_FINITE_STATE_COCYCLE_CANDIDATE.md; PR #27, Squash-Merge b978ac426eb0c4e268237f90ada863086d030500 | finite-state Reduktion |
| **SW1-A8** | AI-GREEN candidate + **independent GREEN (certificate)** — keine Promotion | rohe A1-Komponenten für \(0<\varepsilon<\Delta/2\) endlich; punktweiser Separator midpoint-korrigiert auf \(S_\varepsilon^{\rm reg}\); globale Sheet-Kollisionen durch den Involutionsquotienten \(J_{K,\delta}\) behandelt | audits/P11_R32_SW1_A8_LOWER_FINITE_COMPONENTS_CANDIDATE.md; supplemental certificates scripts/certify_sw1_a8_midpoint_degeneracy_fix.py und scripts/certify_sw1_sheet_collision_quotient.py; PR #31, Squash-Merge cb2d8a4c766e53f49bf2ed590be2222672c606aa | physische Endlichkeit bleibt gültig; direkter A8-Separator gilt nicht automatisch nach KNF-\(J_R\) |

| **SW1-A9** | \`?[O]\` gesamt; J0/J1/FS/DOM und **SEP-SMALL** AI-GREEN + **independent GREEN (certificate)**; BYPASS(part) zertifiziert | vollständige KNF-Gram-Kanten-/Gate-Algebra; im kleinen unteren Subchamber \(0<\varepsilon<(6\Delta-L)/4\) endliche physische KNF-Punktkomponenten; auf anderem offenem Teilgebiet existiert ein regulärer KNF-Bypass, Gesamtklassifikation bleibt offen | audits/P11_R32_SW1_A9_KNF_SEPARATOR_STABILITY_CANDIDATE.md; PR #32, Squash-Merge 70be6437332f094746962769f5ae00a3f5ac40ef | freie Gramgraph-Geometrie weitgehend reduziert; **keine** Schur-/Cross-Gram-Injektivität |
| **SW1-A10-H0/H1/H2/H3-COVER** | AI-GREEN candidate + **independent GREEN (certificate)** im jeweils dokumentierten endlichen/algebraischen Scope | Hub-Phasenalgebra; explizite Separator-Bridge; vollständiger aggregierter Hubledger \(11\) Zellen, \(53\) Kanäle, \(22\) affine Bridge-Typen; kanonisches H2-only-Rotationscover auf \(J=(0,L)\) | audits/P11_R32_SW1_A10_FINITE_CROSSGRAM_FIBER_CANDIDATE.md und zugehörige Zertifikate; PR #33, Squash-Merge eb1f56a6b7c00cbdfed6368d0ec282162e542654 | zeigt, warum freie A9-Endlichkeit nicht auf den augmentierten Hubgraphen übergeht |
| **SW1-A10-H3-INF** | AI-GREEN + **independent GREEN (cross-model blind review)** — keine Promotion | im kleinen unteren Subchamber existiert mindestens **eine unendliche physische augmentierte free-\(w\)-Hub-Inzidenzkomponente**; nichtkonstruktive Wahl von \(x_0\); basiert auf kanonischem H3-Cover und \(\Delta/L\notin\mathbb Q\) | audits/P11_R32_SW1_A10_FINITE_CROSSGRAM_FIBER_CANDIDATE.md; Reviewpaket audits/P11_R32_SW1_A10_H3_INF_REVIEW_PACKET.md; Irrationalitätslemma audits/P11_R32_SW1_DELTA_OVER_L_IRRATIONALITY_LEMMA.md; PR #33, Squash-Merge eb1f56a6b7c00cbdfed6368d0ec282162e542654 | No-Go gegen Zerlegung **nach endlichen Graphkomponenten**; weder \(\ker\Gamma_I=0\) noch \(\ker\Gamma_I\neq0\) |
| **SW1-A10-C2-M1-RAW** | **independent GREEN (certificate)** — kanonisches Certificate-Ergebnis, keine separate \`✓[M]\`-Promotion | additive Assembly der 648 Rohbeiträge zum siebenlagigen \(12\times24\)-Matrixledger ohne Overwrite; vollständige deterministische Fingerprints | \`scripts/certify_sw1_a10_c2_m1_raw_additive.py\`, geprüfter Blob \`32ed47af319c41c83c37aa2bb1ae8f37a38051e7\`; PR #34, Squash-Merge \`6ac0141b2de3a0b2af98fff6d11c403fe3b379b6\` | kanonischer Rohmatrix-Input für M1-FULL; keine Injektivität |
| **SW1-A10-C2-M1-FULL(7/2)** | **independent GREEN (certificate)** — kanonisches exhaustive Referenz-Certificate, keine separate \`✓[M]\`-Promotion | exakte physische Matrix = ausgewertetes M1-Ledger auf allen \(64\times96=6144\) offenen Referenzatomen; Zustandsfingerprint \`de2ab5b32478509feb380804a20705fa5a63e16897e46b05f8d696343cea8a4b\` | \`scripts/certify_sw1_a10_c2_m1_full_b96.py\`, geprüfter Blob \`d73993a393b9d076c72bc77cbdf3610f4695c29c\`; GitHub Actions Run \`33328052407\`, Job \`99301594041\`; PR #34 | Referenzwert \(r_0=7/2\) vollständig geschlossen |
| **SW1-A10-C1B2A-CHIRO** | \`✓[M]\` + **independent GREEN (certificate)** | gelabelter affiner Rank-4-Chirotop der 22 Hyperflächen plus \(g_\infty\) konstant auf \(3<r<4\); expliziter Rangzeuge \(\det(B_e,B_R,D_{s0},INF)=-1\), Loopfreiheit und affine Chart \(X_\infty=+\) mechanisch gehärtet | \`scripts/certify_sw1_a10_c1b2a_affine_chirotope.py\`, geprüfter Blob \`b92f7778bffe29fa11a76e2c260d1e12ae7b27c5\`; Review \`audits/P11_R32_SW1_A10_C1B2A_TRANSFER_REVIEW_PACKET.md\`; CI Run \`33328052407\` | finite/algebraische Basis des tatsächlichen-\(r\)-Transfers |
| **SW1-A10-C1B2A-TRANSFER** | \`✓[M]\` | Standard-Cryptomorphie liefert identische affine Covektor-/Topemengen; alle \(\binom{96}{2}=4560\) B96-Paare werden modulo \(L\) erfasst; nach Normierung \(\theta/L(r)\bmod1\) bleibt die zyklische 96er-Ordnung innerhalb eines festen Topes konstant | \`audits/P11_R32_SW1_A10_C1B2A_TRANSFER_REVIEW_PACKET.md\`; GATE1R-Blob \`18f992d117580260eb3865a493773d1b73833726\`; CI Run \`33328052407\`; PR #34, Squash-Merge \`6ac0141b2de3a0b2af98fff6d11c403fe3b379b6\` | schließt den Transfer ohne ambient isotopy/Folkman--Lawrence |
| **SW1-A10-C2-M1-FULL(\(r\))** | kanonische Konsequenz aus **M1-FULL(7/2) Certificate + C1B2A-TRANSFER \`✓[M]\`** | für jedes \(3<r<4\) gilt auf offenen Parameterkammern und offenen Kreisatomen dieselbe M1-FULL-Matrixidentität wie bei \(r_0=7/2\) | dieselbe PR-#34-Provenienzkette; keine neueren Script-Blobs anstelle der im CI geprüften Fassungen zitieren | C-Strang der Matrixkonstruktion/Geometriestabilität geschlossen; keine Aussage über \(\ker\Gamma_I\) |
| **SW1-A2–A10-REC** | AI-GREEN candidate + **independent GREEN (certificate, algebraic/mechanical scope)** — keine Promotion | rückwärts gerichtete Reconciliation: historischer Strategibruch `A3→A4`; C0 umgeht die explizite \(\mathfrak G_R^{-1}\)-Berechnung; explizite beidseitige Kerneltransporte \(\ker\Gamma_I\cong\ker\mathscr C_R\cong\ker\widehat{\mathscr C}_R\); C1C1-Ambient-Firewall \(WW^*=P_{\operatorname{Ran}W}\neq I_{\rm ambient}\) | `audits/P11_R32_SW1_A2_A10_RECONCILIATION_AUDIT.md`, geprüfter Audit-Blob `894362eaeed630c44d74981c279905384581f460`; `scripts/certify_sw1_a2_a10_kernel_bijections.py`, geprüfter Blob `8a7711d25ff8f9c9b790b8f4517d08f6ee9e9918`; Run `33332811231`, Job `99314333231`, Head `8e404a75a8a4f9e68bf87d3cc5556bd1da51a1d7`; PR #40, Squash-Merge `0ba1722f362ee8be0da502755933342803677330` | isoliert **M1-ND** als kleinsten aktuellen offenen Satz; keine Injektivität |
| **M1-ND-IMG0** | AI-GREEN candidate + **independent GREEN (certificate, algebraic/mechanical scope)** + **owner analytic review ACCEPTED** — keine Promotion | explizite Sheet/Parity-Bildraumcharakterisierung; Extension/Restriction (E_H,R_H,E_W,R_W) beidseitig invers; physischer Rücktransport (f\leftrightarrow y_f); Output-Range folgt aus der Faktorisierung \(\widehat{\mathscr C}_R=U_H\widetilde{\mathscr C}_RD\), **nicht** aus einer ungeprüften Ambient-\(G\)-Äquivarianz; vollständige Kernelbijektion \(\ker\mathscr N_R\cong\ker\widehat{\mathscr C}_R\) | `audits/P11_R32_SW1_M1_ND_IMAGE_SPACE_CANDIDATE.md`; PR #42 Merge `d117e4cb6e59a04ac0ae79b8176e4beaf114979e`; Certificate-Provenienz: Audit-Blob `4562cdecd76ae12198582ed8c024c6fad66f0814`, Script-Blob `7f5b11bd80e5387b1c5e8d73be4c0e4140eed8d5`, Run `33354246817`, Job `99373257498`, Head `52ae23096d1965ba3eb9c7880471b20ff0c6a5b6`; analytisches Post-Merge-Hardening im nachfolgenden Audit-Commit | legitimiert IMG1; **keine Injektivität**; owner review ist kein `independent GREEN (human)` |
| **M1-ND-IMG1** | AI-GREEN candidate + **independent GREEN (certificate, finite/algebraic reference-\(r_0\) scope)** — keine Promotion | exakte \(P_0\)-Reduktion von M1-FULL zu einem \(3\times6\)-Funktionskanal-Ledger auf allen \(64\times96=6144\) offenen B96-Atomen; direkte physische Assembly = reduzierter M1-Ledger termweise inkl. Provenienz; 117546 aktive reduzierte Terme; 12 affine Pullbacktypen; 22 reduzierte Operatorzustände; keine Kollisionen auf \((a,c,\alpha)\)-Zellen; SHA256 `1cffd33529534a15c941b67086217f8f8c47b0cc302cb2cf740b0e08c2ff4474`; Post-Review: 40 FREE + 36 HUB Speciesrelationen direkt gegen IMG0/M1 abgeglichen; ein zunächst tautologischer `lin`-Hilfstest wurde nach Review entfernt und durch Ableitung des Lifts aus unabhängig aufgebauten formalen Source-Koeffizienten plus 2508 exakte rationale Theta-Koordinatenchecks ersetzt; zweite direkte physische Implementierung reproduziert dieselben 117546/22/SHA-Werte ohne IMG1-Helper/`free_sr`/`hub_sr`/`Nwrap`; symbolic IMG1(\(r\)) für \(3<r<4\) folgt separat als analytisch/kombinatorischer Korollar aus C1B2A-TRANSFER `✓[M]` und der termweisen \(r\)-unabhängigen Reduktionsabbildung | `audits/P11_R32_SW1_M1_ND_IMG1_EFFECTIVE_LEDGER_CANDIDATE.md`; Primärscript `scripts/certify_sw1_m1_nd_img1_effective_ledger.py`; Crosschecks `scripts/certify_sw1_m1_nd_img1_species_crosscheck.py`, `scripts/certify_sw1_m1_nd_img1_direct_crosscheck.py`; Post-Review Run `33404708299`, Job `99529291967`, Head `cfda20d9d1d5e01e3d434854e589524c30753aa3`, Audit-Blob `6d123a2c3cb9fa4adf20ed37d879093c19a24e56`, Primärscript-Blob `d824bea626e5b97fbad5a75ed51097408f5b6144`, Species-Crosscheck-Blob `73fdd446e7fd02e05495ff83c5344ddb2e40e3ab`, Direct-Crosscheck-Blob `dd4aea5b694409adcdad28850eba622ed00e51cc`, M1-FULL-Blob `d73993a393b9d076c72bc77cbdf3610f4695c29c`, IMG0-Blob `7f5b11bd80e5387b1c5e8d73be4c0e4140eed8d5`, Python 3.12.14 | legitimiert die nächste Transfer-/Rekurrenzanalyse auf \(\mathscr B_K\oplus\mathscr B_W\); Certificate bleibt Referenz-\(r_0\)-Scope, all-\(r\) nur analytischer Korollar; **keine Injektivität**, keine separate actual-\(r\)-Promotion, kein `independent GREEN (human/cross-model)` |
| **M1-ND-IMG4-SMALLR** | \`✓[M]_neg\` — **kein** \`independent GREEN (external)\`; externe Unabhängigkeitsanforderung per dokumentiertem Governance-Waiver aufgehoben | expliziter zulässiger Small-\(R\)-Kernel auf \(\mathscr B_K\oplus\mathscr B_W\): bei \(\varepsilon_0=\Delta/4,\ R_0=T/100000,\ \sigma_0=R_0/2\) gilt \(\ker\mathscr N_{R_0}\neq\{0\}\); Beweis via A8-FREE-Sättigung, Mass Transport, reduzierender Horizonunterraum und Hub-Blindset | Promotionsrecord \`audits/P11_R32_SW1_M1_ND_IMG4_SMALLR_NEG_PROMOTION.md\`; Beweisquellen \`audits/P11_R32_SW1_M1_ND_IMG4_SMALLR_KERNEL_NOGO_CANDIDATE.md\`, \`audits/P11_R32_SW1_M1_ND_IMG4_ANALYTIC_GATES_CANDIDATE.md\`; mechanische Checks Gate A/B/D; Pre-Promotion-Head \`ad0a59a4c086f207ff3bdd9e31cebdafdfe646ec\`, Run \`33467557472\` SUCCESS | widerlegt universelle M1-ND-Nichtentartung auf dem gesamten SW1-Wedge; allgemeine Lower-Chamber-Small-\(R\)-Familienaussage bleibt Kandidat; keine separate Promotion von \(\ker\Gamma_I\neq0\) |
| **M1-ND-SALVAGE-A1/A2-WEDGE (PR #49)** | AI-GREEN candidate — **keine Promotion**, PR offen und eingefroren | Kandidat: \(0<\varepsilon<(T-10\Delta)/8,\ 0<R<\varepsilon,\ 0<\sigma<R \Rightarrow \ker\mathscr N_R\ne\{0\}\); 24 graph-invariante Horizon-Sperrgaps, 14 explizite Annulus-Blindintervalle, \(R\)-unabhängiges Blindmaß \(\frac72(T-10\Delta-8\varepsilon)\); adversarial zusätzlich direkte \(K_\varepsilon\)-Invarianz und \(\varepsilon\)-uniforme Rohwort-Rekonstruktion | PR #49; Head `2ed1583f074574c2fdb5a48203d63d520a86b5f6`; Run `33532345053` SUCCESS; Audit-/Review-Packet auf dem PR-Branch | **nicht auf main**, kein `✓[M]_neg`, keine Aussage für \(\varepsilon\ge\varepsilon_c\); dient als eingefrorener A-Salvage-Kandidat während B aktiv bearbeitet wird |
| **SW1-A10 gesamt / M1-ND universal** | `✓[M]_neg` für den universellen SW1-Nichtentartungsanspruch; Restparameterklassifikation `?[O]` | C1C1/M1-FULL/IMG0–IMG4 liefern einen expliziten zulässigen Small-\(R\)-Kernel; daher kann die aktuelle finite-level Cross-Gram-Geometrie nicht auf dem gesamten SW1-Wedge injektiv sein | M1-ND-IMG4-SMALLR Promotionsrecord + PR40/IMG0/IMG1 Provenienz | **neue aktive Front:** M1-ND-SALVAGE — nichtdegeneraten Restbereich klassifizieren oder Kopplung so ändern, dass der Small-\(R\)-Blindraum verschwindet |

**Firewall:** `AI-GREEN candidate` bleibt grundsätzlich **kein** `independent GREEN` und **kein** `✓[M]`. Die neue Buchung `M1-ND-IMG4-SMALLR: ✓[M]_neg` ist eine explizite Objekt-X-interne Promotion mit dokumentiertem Independence-Waiver; sie behauptet **kein** `independent GREEN (external)`. Promotiert ist ausschließlich `ker N_{R0} != {0}` am expliziten zulässigen Witness. Keine separate formale Promotion von `ker Gamma_I != {0}`, keine Aussage über alle Parameter, kein Objekt-X- oder RH-Schluss.

---

## 3. Aktueller SW1-Strang

| ID | Status | Scope | Quelle | Bemerkung |
|---|---|---|---|---|
| **HT-A4b-SW1** | \`?[O]\` | \(0<\sigma\le R<\varepsilon,\ R+\varepsilon<\Delta\) | \`audits/P11_R32_HT_A4B_SINGLE_CHAMBER_SUBWEDGE_CANDIDATE.md\` auf \`main\` | gemergter Rechenkandidat; keine Promotion |
| **HT-A4b-SW1-M** | \`✓[M]\` | derselbe SW1-Scope; sechs direkte Blindwerte, die fünf SW1-Membership-Wände \(D_-,D_0,D_+,E,A_*>\varepsilon\), plus direkter A-Wall-Spezialfall (genau der vollständige Satz aus §12 des Kandidatenaudits) | Kandidat: \`audits/P11_R32_HT_A4B_SW1_SELF_CONTAINED_THEOREM_CANDIDATE.md\` (PR #10, exakter Review-Head \`f8f9f107b9c6879611ecb492979737a5541141e9\`, Squash-Merge \`b06f50f12973e781b87db8b06e54fd590a053b10\`); Promotionsrecord: \`audits/P11_R32_HT_A4B_SW1_M_PROMOTION.md\` | promotet ausschließlich der vollständige §12-Satz (\`✓[M]\` = Objekt-X-interner Status, keine externe Begutachtung); keine Mitpromotion von HT-A4b global, HT-RED, A0 oder Schur-Cross-Gram |

Mit HT-A4b-SW1-M nun \(\checkmark[M]\) ist der SW1-Membership-Baustein der Kette formal gesichert. SW1-KNF und SW1-BL7 sind unpromotierte AI-GREEN-Bausteine; SW1-2TP und SW1-AWI sind zusätzlich jeweils als `independent GREEN (certificate)` reproduzierbar zertifiziert. Keiner dieser vier Kandidaten ist formal promotet.

---

## 4. Aktuell offene Zielknoten

| Knoten | Status | Exakte Rolle |
|---|---|---|
| **M1-ND universal auf SW1** | \`✓[M]_neg\` | durch M1-ND-IMG4-SMALLR am expliziten Witness widerlegt: \(\ker\mathscr N_{R_0}\neq\{0\}\) auf dem tatsächlichen zulässigen Raum \(\mathscr B_K\oplus\mathscr B_W\) |
| **A9-KNF Gesamtklassifikation** | \`?[O]\` | SEP-SMALL ist zertifiziert und ein partieller Bypass existiert; der komplementäre untere Bereich und der obere Chamber sind nicht vollständig klassifiziert. Für Roadmap A ist A9 derzeit nicht der primäre Engpass. |
| **SW1-Δ-DESCENT gesamt** | \`?[O]\` | Die zertifizierten Stages 1/2–12 schließen große endliche Teilgeometrien, aber nicht automatisch den gesamten blinden Summanden \(\mathcal Z_R^+\). |
| **HT-A4b global chamber exhaustivity** | \`?[O]\` | globale zehn-Flächen-/15-Chamber-Exhaustivität bleibt offen; für den SW1-Angriff derzeit nicht Priorität |
| **HT-RED** | \`?[O]\` | vollständige Tail-Gaussian-/Schur-Elimination des Restblocks offen |
| **M1-ND-SALVAGE / RESTPARAMETER-KLASSIFIKATION** | `?[O]` — derzeit **geparkt** | maximalen Parameterrest mit möglicher Nichtentartung bestimmen oder finite-level Kopplung so reparieren, dass der promotierte Small-`R`-Blindraum beseitigt wird; PR #49 bleibt eingefrorener Kandidat |
| **STRONG-TERMINAL / B** | `?[O]` — **aktive Forschungsachse** | Historische C6-Lokalfrage geschlossen; absolute Terminalmetrik ohne beschränkten Grenzoperator `✓[M]_neg`; relative Mosco-/Resolvent- und inverse-root-Grenzen vorhanden. Nächster Gate: **R27-F**, also \(D_\infty^-=T_{S,\infty}W-WT_{R,\infty}\stackrel{?}=0\) bzw. fixed Gamma-Crossblock; danach separat **R22-F** Polar-Gauge-/Angle-Defect |
| **Objekt X** | offen | noch keine konstruierte globale gemeinsame Weil-Gram-Geometrie |
| **RH** | offen | keine Folgerung aus den obigen Kandidaten |

---

## 5. Bewusst nicht benötigte Front für den ersten SW1-Angriff

Die P12-Runden 23–29 sind wichtige lokale Low-Radius-Zertifikate. Insbesondere Round 28/29 trägt den invertierbaren \(M_{68}\)-Block. Sie sind **nicht** der aktive Input für den ersten SW1-Angriff.

Grund:

- SW1 verlangt \(\sigma\le R\).
- Die äußere Hub-Injektivität ist dort bereits durch **P12-RT \(\checkmark[M]\)** global verfügbar.
- Das in P12 ausdrücklich verbleibende residual-overlap-Problem liegt im Bereich
  \[
  0<R<\rho,\qquad R<\sigma.
  \]
- Round 29/M68 gehört zur komplementären Restfront und wird nach der negativen M1-ND-Promotion nur dann vorgezogen, wenn die neue Salvage-/Architekturroute ihn benötigt.

Das ist eine **Priorisierungsentscheidung**, kein No-Go gegen spätere Verwendung von \(M_{68}\).

---

## 6. Aktive Beweiskette

Die operative Kette wird nach PR #40 **nicht mehr als lineare A4–A9-Fortsetzung gelesen**.

Historisch liefern

\[
\boxed{A2\to A3}
\]

echte Reduktions-/Koordinatisierungsschritte. Bei

\[
\boxed{A3\to A4}
\]

beginnt eine Strategie-/No-Go-Seitenfront, die keine Kerneltrivialität impliziert.

Der heutige kanonische Pfad ist:

\[
\boxed{
\text{P12-RT}
\to
\text{SW1-KNF}
\to
\text{A-FOLD}
\to
\text{A0/A1}
\to
\text{A2}
\to
\text{A10-C0}
\to
\text{C1C1}
\to
\text{C2/M1-FULL}(r)
\to
\text{PR40-Reconciliation}
\to
\text{M1-ND-IMG4-SMALLR }\checkmark[M]_{\rm neg}.
}
\]

Dabei gelten die explizit gehärteten Bijektionen

\[
\boxed{
\ker\Gamma_I
\cong
\ker\mathscr C_R
\cong
\ker\widehat{\mathscr C}_R.
}
\]

Der M1-ND-Definitionsraum ist

\[
\boxed{
\mathcal R_K\oplus\mathcal R_W
=
\operatorname{Ran}\bigl((U_H|_K)\oplus U_W\bigr),
}
\]

nicht der gesamte formale Slot-Ambientraum.

Der universelle M1-ND-Schritt ist nun durch den expliziten zulässigen
Gegenvektor negativ entschieden.

Der nächste konkrete Schritt ist daher:

1. den promotierten Small-\(R\)-Blindraum als feste No-Go-Firewall behandeln;
2. den verbleibenden Parameterbereich auf mögliche Nichtentartung klassifizieren;
3. eine quantitative Grenze zwischen degeneratem und möglichem nichtdegeneratem Bereich suchen;
4. alternativ die finite-level Kopplung so verändern, dass die FREE-Sättigung der KNF-Fenster den Annulus vollständig beobachtet.

**Firewall:** Keine Rückkehr zur universellen SW1-Injektivitätsbehauptung ohne Architekturänderung. Die Promotion betrifft nur den expliziten Witness auf dem zulässigen Raum; kein HT-RED, kein Objekt-X-Abschluss und keine RH-Folgerung.

---

## 7. Pflege-Regel

Diese Registry wird nur geändert, wenn sich mindestens eines der folgenden Dinge ändert:

1. ein für die aktuelle Front verwendeter Status;
2. der kanonische Quellort eines verwendeten Resultats;
3. der Scope eines verwendeten Resultats;
4. der aktive offene Zielknoten;
5. eine Abhängigkeit der aktiven Beweiskette;
6. eine Änderung der Statusnomenklatur selbst (Abschnitt 0).

Historische oder thematisch entfernte Resultate werden hier nicht vollständig katalogisiert.
