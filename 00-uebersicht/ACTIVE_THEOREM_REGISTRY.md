# Active Theorem Registry

> **Stand:** 30. August 2026  
> **Mathematische Merge-Basis:** \`main@6ac0141b2de3a0b2af98fff6d11c403fe3b379b6\` (PR #34; C1B2A-CHIRO/TRANSFER kanonisch gebucht) · **Navigationssync:** \`main@25235a9e10ddb6d7244dd27bbc29bf03ada8cd1d\` (PR #35).  
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
| **SW1-A10 gesamt** | \`?[O]\` nur noch hinsichtlich Nichtentartung/Injektivität | der inversefreie/operatorwertige Cross-Gram-Cocycle und seine vollständige M1-Matrixdarstellung sind konstruiert und über \(3<r<4\) transferiert; offen bleibt die mathematische Kernfrage, ob dieses System einen nichttrivialen Kernel besitzt | PR #34 + Roadmap A | **aktive nächste Front:** finite-level Cross-Gram-Nichtentartung \(\ker\Gamma_I=\{0\}?\) bzw. Preimage-Form |

**Firewall:** \`AI-GREEN candidate\` allein ist ausdrücklich **kein** \`independent GREEN\` und **kein** \`✓[M]\`. A2/A3 tragen jetzt \`independent GREEN (certificate, algebraic/mechanical scope)\` zusätzlich zum separaten Hilbertraumreview. A9 bleibt als Gesamtknoten \`?[O]\`; A10-H3-INF ist unabhängig blindgeprüft ausschließlich im Existenzscope einer unendlichen augmentierten Inzidenzkomponente. Der Gesamt-Δ-DESCENT bleibt \`?[O]\`. **PR #34 promotet ausschließlich C1B2A-CHIRO und C1B2A-TRANSFER im dokumentierten Scope zu \`✓[M]\`; M1-RAW und M1-FULL(7/2) sind kanonische Certificate-Ergebnisse ohne separate Promotion. Auch PR #34 erzeugt keine Aussage über den Wert von \(\ker\Gamma_I\).**

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
| **FINITE-LEVEL CROSS-GRAM INJECTIVITY / Roadmap A** | \`?[O]\` — **aktiver nächster Knoten** | Mit der nun kanonischen tatsächlichen-\(r\)-M1-Darstellung das augmentierte System bzw. die Preimage-Form analysieren und \(\ker\Gamma_I=\{0\}\) beweisen oder einen exakten Gegenvektor konstruieren. |
| **A9-KNF Gesamtklassifikation** | \`?[O]\` | SEP-SMALL ist zertifiziert und ein partieller Bypass existiert; der komplementäre untere Bereich und der obere Chamber sind nicht vollständig klassifiziert. Für Roadmap A ist A9 derzeit nicht der primäre Engpass. |
| **SW1-Δ-DESCENT gesamt** | \`?[O]\` | Die zertifizierten Stages 1/2–12 schließen große endliche Teilgeometrien, aber nicht automatisch den gesamten blinden Summanden \(\mathcal Z_R^+\). |
| **HT-A4b global chamber exhaustivity** | \`?[O]\` | globale zehn-Flächen-/15-Chamber-Exhaustivität bleibt offen; für den SW1-Angriff derzeit nicht Priorität |
| **HT-RED** | \`?[O]\` | vollständige Tail-Gaussian-/Schur-Elimination des Restblocks offen |
| **SCHUR CROSS-GRAM INJECTIVITY** | \`?[O]\` | \(\ker\Gamma_I=\{0\}\) bzw. äquivalente Transversalitätsform auf geeigneten P12-Injektivitätsstrata |
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
- Round 29/M68 gehört zu dieser komplementären Restfront und muss nicht vorgezogen werden, solange der SW1-Angriff nicht scheitert.

Das ist eine **Priorisierungsentscheidung**, kein No-Go gegen spätere Verwendung von \(M_{68}\).

---

## 6. Aktive Beweiskette

Der aktuelle operative Pfad ist:

\[
\boxed{
\text{SW1-KNF}
\to
\text{A0}
\to
\text{A1}
\to
\text{A2}
\to
\text{A3}
\to
\text{A4}
\to
\text{A5}
\to
\text{A6}
\to
\text{A7}
\to
\text{A8}
\to
\text{A9}
\to
\text{A10-H0/H1/H2/H3}
\to
\text{A10-C1/C2-M1}
\to
\text{C1B2A-TRANSFER}
\to
\text{Roadmap A: Cross-Gram-Nichtentartung}
}
\]

A9 zeigt im kleinen unteren Subchamber endliche **freie KNF-Punktkomponenten**, aber A10-H1/H2 beweisen, dass gemeinsame Annulusvariablen diese freien Komponenten wieder verbinden können.

A10-H3-COVER realisiert auf dem freien physischen Band

\[
J=(0,L)
\]

eine kanonisch ausgewählte irrationale Rotation

\[
x\mapsto x+\Delta\pmod L.
\]

Zusammen mit dem eigenständigen Lemma

\[
\Delta/L\notin\mathbb Q
\]

und dem unabhängigen Blindreview von H3-INF steht im dokumentierten kleinen unteren Subchamber die Existenz mindestens einer **unendlichen physischen augmentierten Hub-Inzidenzkomponente**.

PR #34 hat den operatorwertigen/inversefreien Cross-Gram-Cocycle anschließend bis zur vollständigen M1-RAW/M1-FULL-Matrixdarstellung ausgebaut und den Referenzwert \(r_0=7/2\) über C1B2A-CHIRO/TRANSFER auf jedes \(3<r<4\) übertragen. Damit ist die C-seitige Matrixkonstruktion und Geometriestabilität kein offener Gate mehr. Der nächste mathematische Gegenstand ist nun die **Nichtentartung dieses bereits konstruierten Systems**, also Roadmap A.

**Firewall:** Dies ist kein Beweis für oder gegen
\[
\ker\Gamma_I=\{0\}.
\]
Eine unendliche Komponente kann einen injektiven Operator tragen. Keine Promotion, kein HT-RED, kein Objekt-X-Abschluss und keine RH-Folgerung.

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
