# P09 Pass-A — Eroeffnung und Inventar

**Datum:** 9. August 2026  
**SYN-Ziel:** P09 — BC + Hochschild  
**Status:** `PASS A OPEN — I1 SEALED, I2 SEALED, I3 SEALED, I4 COMPLETE / COUNTERCHECK PENDING`  
**Voraussetzung:** P01 dependency-reconciled durch `AUDIT-2026-08-09_P01_Dependency_Reaudit_vor_P09.md`  
**Hauptquellblock:** `06-hochschild-bc-algebra/`

---

## 1. Live-Inventar und Leserichtung

Der Ordner `06-hochschild-bc-algebra/` dokumentiert den BC/Hochschild-Strang von NEU-174 bis in den NEU-219-Block; zusätzlich liegt NEU-222 als später Trassenaudit vor.

Wegen mehrfach belegter IDs — insbesondere NEU-183, NEU-193, drei NEU-217-Dateien, zwei NEU-218-Dateien sowie mehrere NEU-219-Unterdateien — arbeitet P09 **pfad- und rollenbasiert**, nicht nach bloßer Nummernsequenz.

Verbindliche Präzedenz:

```text
August-Finalaudit / spätere Bestandsaufnahme / kanonischer Auditstand
    > node-spezifischer Direktaudit / Blockaudit
    > Abschluss-/Revisionsdatei des Knotens
    > frühere Zwischenfassung.
```

Ein späterer Rollback darf nur auf dasselbe mathematische Objekt übertragen werden. Insbesondere ist die rohe I4-KMS-Kochain `Phi_{beta,chi}` nicht mit dem späteren kanonischen Basislift `Phi_0` aus I5 zu identifizieren.

---

## 2. Verbindliche Vor-Firewall aus P01

P09 darf aus P01 nur folgende lokale BC-Aussagen importieren:

1. primitiver `p`-Kanal: algebraischer Faktor `log p/sqrt(p)` (`INCORPORATED_part`);
2. arithmetische Identität `Lambda(p^m)/sqrt(p^m)=log p/p^(m/2)` (`✓[M]`, RH-frei);
3. all-`n`-Operatorrealisierung `h_n^bal=n^-1/2 I` bleibt `?[O]/CONDITIONAL`;
4. Mangoldt-Trägertrennung gegen direkte Kreuzprimkollision ist kein Orthogonalitätssatz.

Die alte P01-Draftaussage `all results unconditional` ist `SUPERSEDED`.

---

## 3. Autoritative Spätanker

`NEU-219_Finalaudit_Gesamtabschluss.md` ist der autoritative Endanker für die **kanonische geladene Basislift-/Rotationsarchitektur**. Bindend ist dort

\[
\widetilde L_0\longrightarrow\kappa=0\longrightarrow\varepsilon=0
\longrightarrow\text{kein globales }s\longrightarrow\text{kein }\lambda^*,
\]

sowie

\[
\boxed{t\Phi_0\neq C\Phi_0\quad\forall C\in\mathbb C.}
\]

Frühere I5-Zwischenbehauptungen, insbesondere `s=-1`, sind zurückgerollt.

Für den I2/I3-Strang gilt zusätzlich `AUDITSTAND-2026-08-03.md` als Kontrollblatt. `OBJEKT-X-BESTANDSAUFNAHME.md` vom 5. August bestätigt ausdrücklich

\[
[D_g^{\rm corr}]\smile[\Theta^\wedge]\neq0
\]

und die Lesart: singuläre Route trägt bis `HH^4`, Blockade erst bei der Zyklizität.

`NEU-222` ist nur lokaler Trassen-/Statusanker; seine älteren überstarken Detailstatus werden durch spätere Direktaudits und den Finalaudit begrenzt.

---

## 4. Paketstruktur Gruppe I / P09

### I1 — Algebraischer BC/Hochschild-Grundblock — **PASS A COMPLETE / SEALED**

**Quellen:** NEU-174–190  
**Audit:** `audits/AUDIT-2026-08-09_P09_I1_BC_Hochschild_Grundblock_Reconciliation.md`  
**Audit-Commit:** `bf636a2d`  
**Gegencheck:** `audits/AUDIT-2026-08-09_P09_I1_Gegencheck_Pfadgebunden.md`  
**Gegencheck-Commit:** `12e12f12` — `VALID`, kein Gegenbefund

**Endstand:** algebraischer Modellrahmen vorhanden; neutrale `[Omega_p] != 0 in HH^4(A,A)` auf `A_Q^alg`; geladene Selbstkoeffizientenklasse weiterhin offen; Zentrum-/Nullkozykel-No-gos getrennt; frühe HH1-Erweiterung nur partiell; Operatorbrücke nicht konstruiert.

**Seal-Regel:** nur atomare Wiederöffnung bei konkretem neuem mathematischem Gegenbefund.

---

### I2 — Aeussere Derivationen und singulaere Potentialroute — **PASS A COMPLETE / SEALED**

**Quellen:** NEU-192–211; Doppeldatei NEU-193; NEU-198 fehlt als Live-Datei  
**Audit:** `audits/AUDIT-2026-08-09_P09_I2_Aeussere_Derivationen_Singulaere_Potentialroute_Reconciliation.md`  
**Audit-Commit:** `6aba82cf`  
**Gegencheck:** `audits/AUDIT-2026-08-09_P09_I2_Gegencheck_Pfadgebunden.md`  
**Gegencheck-Commit:** `438aca8e` — `VALID`, kein Gegenbefund

**Hauptbefund:**

\[
\boxed{[D_g^{\rm corr}]\neq0\in HH^1(A_{\rm alg},A_{C^*})_g,\qquad g\neq1.}
\]

Keine automatische algebraische Selbstkoeffizientenklasse und kein HH4-Sprung aus I2.

**Seal-Regel:** nur atomare Wiederöffnung bei konkretem neuem mathematischem Gegenbefund.

---

### I3 — Koeffizientenmodule, Bimodul-No-go und Cup-Aufstieg — **PASS A COMPLETE / SEALED**

**Quellen:** NEU-212–218, pfadgebunden mit drei NEU-217- und zwei NEU-218-Dateien  
**Audit:** `audits/AUDIT-2026-08-09_P09_I3_Koeffizientenmodule_Bimodul_Cup_Reconciliation.md`  
**Audit-Commit:** `b513a854`  
**Gegencheck:** `audits/AUDIT-2026-08-09_P09_I3_Gegencheck_Pfadgebunden.md`  
**Gegencheck-Commit:** `88b36912` — `VALID`, kein Gegenbefund

**Endstand:**

- NEU-212-Schwartz-Zieltypbrücke zentral `×[M]`;
- NEU-214/215: globaler normstetiger Bimodul-Glätter in echten Teilraum `P09-CORE-NOGO`;
- NEU-216: direkter logarithmischer Zieltyp `B^log/A^log`;
- NEU-217: globaler Koeffizientenbimodul `M_glob^log` trägt `D_g^corr`;
- NEU-218-Abschluss: Mehrparameter-Følnerbeweis, partieller Modulquotient, Dualzyklus und nichtverschwindende Paarung.

Verbindlicher Hauptbefund:

\[
\boxed{
[D_g^{\rm corr}]\smile[\Theta^\wedge]
\neq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
}
\]

**Firewall:** Kein Schluss auf `HH^4(A_alg,A_alg)_g`, keine automatische zyklische/KMS-/Weil-/Operatorrealisierung.

**Seal-Regel:** nur atomare Wiederöffnung bei konkretem neuem mathematischem Gegenbefund.

---

### I4 — KMS, getwistete Zyklizitaet und Hopf-SAYD — **PASS A COMPLETE / COUNTERCHECK PENDING**

**Quellen:** `NEU-219_Zyklischer...`, `NEU-219a`–`NEU-219g`  
**Blockanker:** `NEU-219_BLOCKAUDIT_I_KMS_Twist_Triage.md`  
**Audit:** `audits/AUDIT-2026-08-09_P09_I4_KMS_Zyklisch_Hopf_Reconciliation.md`  
**Audit-Commit:** `d3579ff9`  
**Prüfart:** `AUDIT-RECONCILED` / `AUDIT-REUSED` + `TARGETED-REAUDIT` der Twist-, Zyklisierungs- und SAYD-Schritte

**Endstand:**

1. Der direkte KMS-Detektor des nichtneutralen Zielelements verschwindet für `beta>0`:
   \[
   \omega_\beta(\eta_{q,P})=0.
   \]
2. Nach expliziter Gradneutralisierung durch `a0^neu` gilt für alle extremalen KMS-Zustände im bewiesenen Gibbs-Bereich `beta>1`:
   \[
   \omega_{\beta,\chi}(\sigma_P(G_q))>0.
   \]
   `beta=1` bleibt durch I4 **unbehandelt/offen**.
3. Standard-Twistorientierung:
   \[
   \sigma_\beta=\alpha_{-i\beta}=\theta_\beta^{-1}.
   \]
   Damit
   \[
   0\neq\Phi_{\beta,\chi}\in Z^4_{\sigma_\beta,\mathrm{Hoch}}(A_{\rm alg}),
   \qquad b^{\sigma_\beta}\Phi_{\beta,\chi}=0.
   \]
4. Für diese rohe I4-Kochain:
   \[
   T_{\sigma_\beta}\Phi_{\beta,\chi}=g^{-\beta}\Phi_{\beta,\chi}\neq\Phi_{\beta,\chi},
   \]
   daher keine standardmäßige getwistete zyklische Klasse **dieses Repräsentanten**.
5. Externe Eigenlinie kompensiert nur formal `T`; kein 1-dim. unitales `sigma_beta`-äquivariantes `A_alg`-Bimodul.
6. Der `w=g^{-beta}`-Gewichtssektor ist ein `b^sigma`-Unterkomplex, wird aber bei gewöhnlicher Invarianten-/Koinvarianten-Zyklisierung für `w!=1` annihiliert.
7. Die `Q_+^x`-Gradierung liefert kanonisch eine Hopf-**Koaktion**, nicht eine kanonische Aktion. Der reparierte Hopf-Typ `H_beta=C[Z]` wirkt durch `sigma_beta`.
8. Im standardmäßigen `H_beta`-SAYD-Setup kollidieren exakter KMS-Twist und nichttriviale Ladung mit der SAYD-Stabilität. Nichtstandardmäßiger `A`-relativer Hopf-Koeffizient bleibt offen.
9. Der volle gewöhnliche Quotient `eta notin [A,M]` bleibt offen.
10. Die Dilatations-/Crossed-Product-Route wird an I5 weitergereicht.

**Wichtige Reichweiten-Firewall:** I4 rollt I3 nicht zurück und schließt nicht alle möglichen nichtkanonischen zyklischen/getwistet-zyklischen Repräsentanten aus. Der spätere Finalaudit hält `[O-219-cyclic-representative] ?[O]` ausdrücklich offen/exportiert.

**Gegencheck:** fünf atomare Fragen stehen in §14 des I4-Auditblatts.

---

### I5 — Dilatation, Orbitmarkierung und kanonischer Rotationsabschluss

**Quellen:** NEU-219h–z + `NEU-219_Finalaudit_Gesamtabschluss.md`  
**Status:** `WAITING FOR I4 SEAL`  
**Prüfziel:** Dilatations-/adelische/Morita-/Basisliftarchitektur gegen den August-Finalaudit reconciliieren; `s=-1` und andere Rollback-Zwischenbehauptungen als `SUPERSEDED` markieren; kanonischen Unit-Slot-No-go vom offenen nichtkanonischen Ersatzrepräsentanten trennen.

---

### I6 — Spaeter Trassenaudit / Superseding-Scan

**Quelle:** NEU-222  
**Prüfziel:** nur als lokaler Trassen-/Statusabgleich; bei Konflikten haben August-Direktaudits und Finalaudit Vorrang.

---

## 5. Routing-Firewalls

- **P09:** BC/Hochschild-/KMS-/Koeffizientenstruktur, belastbare Cup-/Derivationsresultate und strukturentscheidende No-gos.
- **P10:** kondensierte Sammlung isolierter ausgeschlossener Kandidaten; P09-CORE-NOGOs dürfen gespiegelt, aber nicht aus P09 entfernt werden.
- **P11:** globale nichtorthogonale Gramkopplung, intrinsische Quellhilbertisierung, Mediator und Objekt-X-Gesamtgeometrie.
- **P12:** finite-to-infinite Weil-Grenzfragen.

P09 darf weder die P11-Quell-/Gramstruktur vorwegnehmen noch aus einer Hochschild- oder KMS-Klasse unmittelbar einen Hilbert–Polya-Operator ableiten.

### P09-CORE-NOGOs nach I4

- zu starke Schwartz-Regularisierung (NEU-212),
- globaler normstetiger Bimodul-Glätter (NEU-215),
- untypisierte lokale NEU-217-Koeffizientenklasse,
- Baker-/komplexe `log q`-Koeffiziententrennung im ersten NEU-218,
- direkter gewöhnlicher KMS-Detektor des geladenen Zielelements,
- falsche Twist-Orientierung im Standard-Letztrand,
- standardmäßige getwistete Zyklizität der rohen geladenen KMS-Kochain,
- 1-dim. unitales `sigma_beta`-äquivariantes `A_alg`-Bimodul,
- gewöhnliche Zyklisierung des `w!=1`-Gewichtssektors,
- kanonische `H_Gamma`-Aktion allein aus der Gradierung,
- Standard-`H_beta`-SAYD-Koeffizient mit gleichzeitig exaktem KMS-Twist und Ladung.

Diese bleiben in P09, weil sie den positiven Pfad

```text
HH4-Cup -> gradneutralisierte KMS-Auswertung -> getwisteter Hochschildkozykel
       -> Ladungsobstruktion -> Dilatations-/nichtkanonischer Reparaturraum
```

präzise typisieren.

---

## 6. Naechster Arbeitsschritt

Aktueller Stand:

\[
\boxed{
\text{P09 PASS A OPEN — I1 SEALED; I2 SEALED; I3 SEALED; I4 COMPLETE / COUNTERCHECK PENDING.}
}
\]

Nach Gegencheck der fünf atomaren I4-Fragen ohne konkreten Befund wird I4 versiegelt und I5 (`NEU-219h–z` + Finalaudit) aktiviert.
