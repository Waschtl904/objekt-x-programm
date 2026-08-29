# Active Theorem Registry

> **Stand:** 29. August 2026  
> **Repo-Basis:** \`main@6ff2598d6071fc1fd9444d3f9734384c23264834\` (mathematische Merge-Basis nach PR #19–#28)  
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
| **SW1-A2** | AI-GREEN candidate — **kein independent GREEN**, keine Promotion | kanonische schiefe Annulusprojektion \(Q_{\mathscr T,K}\) und exakte Schur-Kernelreduktion | audits/P11_R32_SW1_A2_ANNULUS_PROJECTION_CANDIDATE.md; PR #22, Squash-Merge 8e2d4eb7c5d78320e8ebc218c26c4fb1ae0e004d | korrekte Operatorreduktion; keine Injektivität |
| **SW1-A3** | AI-GREEN candidate — **kein independent GREEN**, keine Promotion | positiver freier Gramoperator \(\mathfrak G_R=J_R^*(I+A)J_R\), Coercivität und Identität \(G^{-1}P_K=J_R\mathfrak G_R^{-1}J_R^*\) | audits/P11_R32_SW1_A3_FREE_COORDINATE_GRAM_CANDIDATE.md; PR #23, Squash-Merge 934c48a96ce52a4b9fd300a2d1ad7261112565dd | Ausgangspunkt der freien Gramgraph-Analyse |
| **SW1-A4** | AI-GREEN candidate + **independent GREEN (certificate)** — keine Promotion | oberer Chamber: irrationale Rotation als Strategieno-go gegen exhaustive finite physische Punktorbits; kein No-Go gegen Schur-Injektivität | audits/P11_R32_SW1_A4_IRRATIONAL_ROTATION_NOGO_CANDIDATE.md; PR #24, Squash-Merge 637e63d23540bc4d7498fd5a7df30056be035eed | obere-Chamber Struktur |
| **SW1-A5** | AI-GREEN candidate + **independent GREEN (certificate)** — keine Promotion | Zwei-Blatt-Transfer modulo \(L=a-\Delta\); keine dritte irrationale Phase | audits/P11_R32_SW1_A5_TWO_SHEET_TRANSFER_CANDIDATE.md; PR #25, Squash-Merge 99d853c211ec17e657ede78af791c6a600a875e5 | finite Blätter über irrationaler Basis |
| **SW1-A6** | AI-GREEN candidate + **independent GREEN (certificate)** — keine Promotion | unterer Chamber: A4-Rotationsmechanismus mit offenem Hole, endliche kontrahierte Segmente | audits/P11_R32_SW1_A6_ROTATION_HOLE_CANDIDATE.md; PR #26, Squash-Merge f7bad5ad9945d9815251d027d694c5f4e4d0b564 | nur Rotationssubgraph |
| **SW1-A7** | AI-GREEN candidate + **independent GREEN (certificate)** — keine Promotion | vollständiger roher A1-Punktgraph als 6-State-, Range-3-Cocycle über einer irrationalen Kreisrotation | audits/P11_R32_SW1_A7_FINITE_STATE_COCYCLE_CANDIDATE.md; PR #27, Squash-Merge b978ac426eb0c4e268237f90ada863086d030500 | finite-state Reduktion |
| **SW1-A8** | AI-GREEN candidate + **independent GREEN (certificate)** — keine Promotion | für \(0<\varepsilon<\Delta/2\) sind alle Zusammenhangskomponenten des vollständigen **rohen A1-Punktgraphen** endlich; 20 mittlere Zustände, 180 Source-Map-Fälle, exakt 10 Cross-Kandidaten, alle inaktiv | audits/P11_R32_SW1_A8_LOWER_FINITE_COMPONENTS_CANDIDATE.md; Zertifikat scripts/certify_sw1_a8_lower_finite_components.py; PR #28, Squash-Merge 6ff2598d6071fc1fd9444d3f9734384c23264834 | A8-Separator gilt **nicht automatisch** nach KNF-\(J_R\)-Rekonstruktion |

**Firewall:** `AI-GREEN candidate` allein ist ausdrücklich **kein** `independent GREEN` und **kein** `✓[M]`. SW1-2TP, SW1-AWI, A0, A1 und A4–A8 tragen `independent GREEN (certificate)` im jeweils explizit dokumentierten Scope; A2/A3 nicht. Der Gesamt-Δ-DESCENT bleibt `?[O]`, obwohl seine endlichen Teilstufen zertifiziert sind. Die Perplexity-Blindchecks erzeugen weiterhin kein `independent GREEN (cross-model)` für 2TP/AWI. **Keiner der Merges #19–#28 erzeugt eine formale Promotion.**

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
| **A9-KNF Separatorstabilität** | ?[O] — **aktiver nächster Knoten** | Bestimmen, welche zusätzlichen freien Koordinatenkanten durch \(J_R^*J_R\) und \(J_R^*AJ_R\) entstehen, identische affine Kanäle vor dem Graphurteil algebraisch zusammenfassen und entscheiden, ob die A8-Separatoren erhalten bleiben oder ein expliziter KNF-Bypass entsteht. |
| **SW1-Δ-DESCENT gesamt** | ?[O] | Die zertifizierten Stages 1/2–12 schließen große endliche Teilgeometrien, aber nicht automatisch den gesamten blinden Summanden \(\mathcal Z_R^+\). |
| **HT-A4b global chamber exhaustivity** | ?[O] | globale zehn-Flächen-/15-Chamber-Exhaustivität bleibt offen; für den SW1-Angriff derzeit nicht Priorität |
| **HT-RED** | ?[O] | vollständige Tail-Gaussian-/Schur-Elimination des Restblocks offen |
| **SCHUR CROSS-GRAM INJECTIVITY** | ?[O] | \(\ker\Gamma_I=\{0\}\) bzw. äquivalente Transversalitätsform auf geeigneten P12-Injektivitätsstrata |
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
\text{A9-KNF}
}
\]

A8 schließt im unteren Chamber den **rohen A1-Punktgraphen** zu endlichen Komponenten. Der nächste Engpass ist nicht mehr A8, sondern die Frage, ob die KNF-Rekonstruktion \(J_R\) diese Separatoren im freien Gramoperator

\[
\mathfrak G_R=J_R^*(I+A)J_R
\]

überbrückt.

Der bisherige A9-Strukturkandidat zeigt:
\[
e=L/2,\qquad d=L/2+\Delta,
\]
also eine endliche Halbperioden-Parität über derselben irrationalen \(\Delta\)-Rotation und keine neue unabhängige irrationale Phase. Das entscheidet die Separatorfrage noch nicht.

**Firewall:** A0–A8 auf main bedeutet weder HT-RED noch Schur-Injektivität noch eine Promotion. A2/A3 bleiben ausdrücklich ohne independent GREEN.

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
