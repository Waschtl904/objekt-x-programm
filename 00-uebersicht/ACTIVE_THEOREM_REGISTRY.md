# Active Theorem Registry

> **Stand:** 28. August 2026  
> **Repo-Basis:** \`main@b06f50f12973e781b87db8b06e54fd590a053b10\`  
> **Zweck:** operative, nicht exhaustive Registry der Resultate, die für die aktuelle P11/R32-SW1-/Schur-Front tatsächlich benötigt oder unmittelbar angrenzend sind.  
> **Nicht-Zweck:** Ersatz für \`STATUS.md\`, \`OFFENE_PROBLEME.md\`, die Papers oder Promotionsrecords.

Diese Datei ist eine **Navigations- und Abhängigkeitsregistry**. Eine Statuszeile hier erzeugt keine Promotion. Bei Konflikten gilt die kanonische mathematische Quelle des jeweiligen Resultats.

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

## 2. Unabhängig GREEN geprüfte Kandidaten — keine formale Promotion

| ID | Status | Inhalt | Kanonische Quelle | Verwendung |
|---|---|---|---|---|
| **HT-A1** | independently GREEN candidate | wordwise Tail-Aktion; \(44\to24\to16\)-Selektion | \`audits/P11_R32_TAIL_FG_PIVOT_CANDIDATE.md\` | Rohmaterial für die Tail-/Full-Rest-Zeilen |
| **HT-A2** | independently GREEN candidate | Tail-Kompression / skalarer Pivot, insbesondere \(P_{\mathcal T_R}(I+A)P_{\mathcal T_R}=(1+\kappa)I\) | dieselbe Datei | liefert den invertierbaren Tail-Pivot |
| **HT-A3** | independently GREEN candidate | Off-tail-Shell-Klassifikation | dieselbe Datei | kontrolliert Shell-Überlappungen / A-Walls |
| **HT-A4a** | independently GREEN candidate | FG-Klassifikation der sechs Tail-Argumente | dieselbe Datei | allgemeiner Kandidatenhintergrund; für SW1-M soll diese Blackbox nicht benötigt werden |
| **FG-1** | independently GREEN candidate — keine formale Promotion | Branch-/Gluing-Klassifikation des unsichtbaren Kerns | **Statusbuchung:** \`00-uebersicht/P11_R32_STATUS_2026-08-25.md\`, Update 2026-08-26; **Beweis-/Auditprovenienz:** \`audits/P11_R32_INVISIBLE_FIBER_GRAPH_CLASSIFICATION_AUDIT.md\` plus Exhaustivitätsabschluss | allgemeine Kernelgeometrie |
| **FG-TR1** | OVERALL GREEN candidate — keine formale Promotion | \(\Theta_R\) als beschränkter Koordinatenisomorphismus; \(L_R=\operatorname{pr}_1\Theta_R\) | **Statusbuchung:** \`00-uebersicht/P11_R32_STATUS_2026-08-25.md\`, Update 2026-08-26; **Beweis-/Auditprovenienz:** \`audits/P11_R32_TRIANGULAR_ROW_SPLITTING_AUDIT.md\` | freie Koordinaten / Rekonstruktionshintergrund |
| **\(\widehat\Phi_R\)-Normalform** | CANDIDATE GREEN als mechanische Komposition | \(E_I^*H\,\widehat\Phi_R(z,f,h)=f\) | \`00-uebersicht/P11_R32_STATUS_2026-08-25.md\`, Update 2026-08-26; Provenienz dort angegeben | Parametrisierung der augmentierten Rechnung |
| **CG-FG1** | CANDIDATE GREEN als Kompositionsreduktion | \(\Gamma_I=\operatorname{pr}_2\Gamma_R=E_I^*HBH^*E_{\mathcal A}=M_I^*M_A\) | \`00-uebersicht/P11_R32_STATUS_2026-08-25.md\`, Update 2026-08-26 | verbindet freie Koordinaten mit dem offenen Schur-Cross-Gram-Test |

**Firewall:** \`independently GREEN candidate\`, \`OVERALL GREEN candidate\` und \`CANDIDATE GREEN\` sind ausdrücklich **kein** \`✓[M]\`.

---

## 3. Aktueller SW1-Strang

| ID | Status | Scope | Quelle | Bemerkung |
|---|---|---|---|---|
| **HT-A4b-SW1** | \`?[O]\` | \(0<\sigma\le R<\varepsilon,\ R+\varepsilon<\Delta\) | \`audits/P11_R32_HT_A4B_SINGLE_CHAMBER_SUBWEDGE_CANDIDATE.md\` auf \`main\` | gemergter Rechenkandidat; keine Promotion |
| **HT-A4b-SW1-M** | \`?[O]\`, gemergter adversarial GREEN geprüfter self-contained theorem candidate — keine formale Promotion | derselbe SW1-Scope; sechs direkte Blindwerte plus direkter A-Wall-Spezialfall | \`audits/P11_R32_HT_A4B_SW1_SELF_CONTAINED_THEOREM_CANDIDATE.md\` auf \`main@b06f50f12973e781b87db8b06e54fd590a053b10\` (PR #10) | selbständiger SW1-Satz; mathematisch GREEN geprüft, aber bis zu separater Promotionsbuchung weiterhin \`?[O]\` |

**Formaler nächster Schritt nach dem gemergten PR #10:** Der dort exakt abgegrenzte selbständige SW1-Satz ist adversarial und mechanisch GREEN geprüft, bleibt aber bis zu einer separaten Promotionsbuchung \`?[O]\`. Nur dieser enge Satz kann in einem eigenen Promotions-PR zu
\[
\mathrm{HT\!-\!A4b\!-\!SW1\!-\!M}:\checkmark[M]
\]
gebucht werden.

---

## 4. Aktuell offene Zielknoten

| Knoten | Status | Exakte Rolle |
|---|---|---|
| **HT-A4b global chamber exhaustivity** | \`?[O]\` | globale zehn-Flächen-/15-Chamber-Exhaustivität bleibt offen; für den ersten SW1-Angriff derzeit nicht benötigt |
| **HT-RED** | \`?[O]\` | vollständige Tail-Gaussian-/Schur-Elimination des Restblocks offen |
| **A0 FULL FREE-COORDINATE COVERAGE** | \`?[O]\` | volle Abdeckung aller freien Koordinaten / relevanten Strata offen |
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

Der derzeit gewünschte Pfad ist:

\[
\boxed{
\text{SW1-Membership}
\;+\;
\text{Full-Rest-/Schur-Elimination}
\;+\;
\text{P12-RT }\checkmark[M]
\;\Longrightarrow\;
\ker\mathcal K_{I,A}=\{0\}\ \text{auf SW1?}
}
\]

Der einzige wirklich neue mathematische Engpass in dieser Kette ist derzeit die **Full-Rest-/Schur-Elimination auf SW1**.

---

## 7. Pflege-Regel

Diese Registry wird nur geändert, wenn sich mindestens eines der folgenden Dinge ändert:

1. ein für die aktuelle Front verwendeter Status;
2. der kanonische Quellort eines verwendeten Resultats;
3. der Scope eines verwendeten Resultats;
4. der aktive offene Zielknoten;
5. eine Abhängigkeit der aktiven Beweiskette.

Historische oder thematisch entfernte Resultate werden hier nicht vollständig katalogisiert.
