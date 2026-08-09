# P09 Pass-A — Eroeffnung und Inventar

**Datum:** 9. August 2026  
**SYN-Ziel:** P09 — BC + Hochschild  
**Status:** `PASS A OPEN — I1 SEALED, I2 SEALED, I3 SEALED, I4 SEALED, I5 COMPLETE / COUNTERCHECK PENDING`  
**Voraussetzung:** P01 dependency-reconciled durch `AUDIT-2026-08-09_P01_Dependency_Reaudit_vor_P09.md`  
**Hauptquellblock:** `06-hochschild-bc-algebra/`

---

## 1. Live-Inventar und Leserichtung

Der Ordner `06-hochschild-bc-algebra/` dokumentiert den BC/Hochschild-Strang von NEU-174 bis in den NEU-219-Block; zusätzlich liegt NEU-222 als später Trassenaudit vor.

Wegen mehrfach belegter IDs — insbesondere NEU-183, NEU-193, mehrere NEU-217/218-Dateien, zwei NEU-219u-Dateien sowie zwei NEU-219y-Dateien — arbeitet P09 **pfad- und rollenbasiert**, nicht nach bloßer Nummernsequenz.

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

`NEU-219_Finalaudit_Gesamtabschluss.md` ist der autoritative Endanker für die **kanonische geladene Basislift-/Rotationsarchitektur**.

Bindend:

\[
\boxed{
\widetilde L_0\longrightarrow\kappa=0\longrightarrow\varepsilon=0
\longrightarrow\text{kein globales }s\longrightarrow\text{kein }\lambda^*.
}
\]

sowie

\[
\boxed{t\Phi_0\neq C\Phi_0\quad\forall C\in\mathbb C.}
\]

Die frühere I5-Zwischenbehauptung

\[
t\Phi_0=g^{-\beta}\Phi_0,\qquad s=-1
\]

ist **zurückgerollt** und darf nicht migriert werden.

Für den I2/I3-Strang gilt zusätzlich `AUDITSTAND-2026-08-03.md` als Kontrollblatt. `OBJEKT-X-BESTANDSAUFNAHME.md` vom 5. August bestätigt den nichtverschwindenden geladenen Hochschild-Cup und die Lesart: Blockade erst bei der zyklischen Verfeinerung, nicht bei der HH4-Nichttrivialität.

`NEU-222` ist nur lokaler Trassen-/Statusanker; Konflikte werden in I6 gegen die August-Direktaudits und den Finalaudit aufgelöst.

---

## 4. Paketstruktur Gruppe I / P09

### I1 — Algebraischer BC/Hochschild-Grundblock — **PASS A COMPLETE / SEALED**

**Quellen:** NEU-174–190  
**Audit:** `audits/AUDIT-2026-08-09_P09_I1_BC_Hochschild_Grundblock_Reconciliation.md`  
**Audit-Commit:** `bf636a2d`  
**Gegencheck:** `audits/AUDIT-2026-08-09_P09_I1_Gegencheck_Pfadgebunden.md`  
**Gegencheck-Commit:** `12e12f12` — `VALID`, kein Gegenbefund

**Endstand:** algebraischer Modellrahmen vorhanden; neutrale `[Omega_p] != 0 in HH^4(A,A)` auf `A_Q^alg`; geladene Selbstkoeffizientenklasse weiterhin offen; Zentrum-/Nullkozykel-No-gos getrennt; frühe HH1-Erweiterung nur partiell; Operatorbrücke nicht konstruiert.

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

---

### I3 — Koeffizientenmodule, Bimodul-No-go und Cup-Aufstieg — **PASS A COMPLETE / SEALED**

**Quellen:** NEU-212–218  
**Audit:** `audits/AUDIT-2026-08-09_P09_I3_Koeffizientenmodule_Bimodul_Cup_Reconciliation.md`  
**Audit-Commit:** `b513a854`  
**Gegencheck:** `audits/AUDIT-2026-08-09_P09_I3_Gegencheck_Pfadgebunden.md`  
**Gegencheck-Commit:** `88b36912` — `VALID`, kein Gegenbefund

**Endstand:** direkter logarithmischer Zieltyp `B^log/A^log`; globaler Koeffizientenbimodul `M_glob^log`; Mehrparameter-Følnerbeweis und Dualzeuge.

\[
\boxed{
[D_g^{\rm corr}]\smile[\Theta^\wedge]
\neq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
}
\]

**Firewall:** Kein Schluss auf `HH^4(A_alg,A_alg)_g`, keine automatische zyklische/KMS-/Weil-/Operatorrealisierung.

---

### I4 — KMS, getwistete Zyklizitaet und Hopf-SAYD — **PASS A COMPLETE / SEALED**

**Quellen:** `NEU-219_Zyklischer...`, `NEU-219a`–`NEU-219g`  
**Blockanker:** `NEU-219_BLOCKAUDIT_I_KMS_Twist_Triage.md`  
**Audit:** `audits/AUDIT-2026-08-09_P09_I4_KMS_Zyklisch_Hopf_Reconciliation.md`  
**Audit-Commit:** `d3579ff9`  
**Gegencheck:** `audits/AUDIT-2026-08-09_P09_I4_Gegencheck_Pfadgebunden.md`  
**Gegencheck-Commit:** `362ddd68` — `VALID`, kein Gegenbefund

**Endstand:**

1. Direkter KMS-Detektor des nichtneutralen Zielelements verschwindet für `beta>0`.
2. Nach Gradneutralisierung gilt im bewiesenen Gibbs-Bereich `beta>1`:
   \[
   \omega_{\beta,\chi}(\sigma_P(G_q))>0.
   \]
3. Korrekte Standard-Twistorientierung:
   \[
   \sigma_\beta=\alpha_{-i\beta}=\theta_\beta^{-1}.
   \]
4. Für die rohe I4-Kochain:
   \[
   0\neq\Phi_{\beta,\chi}\in Z^4_{\sigma_\beta,\mathrm{Hoch}}(A_{\rm alg}),
   \qquad
   T_{\sigma_\beta}\Phi_{\beta,\chi}=g^{-\beta}\Phi_{\beta,\chi}\neq\Phi_{\beta,\chi}.
   \]
5. Gewöhnliche Zyklisierung des `w!=1`-Sektors annihiliert den geladenen Sektor.
6. Standard-`H_beta=C[Z]`-SAYD kann exakten KMS-Twist und nichttriviale Ladung nicht gleichzeitig tragen.
7. Nichtstandardmäßiger `A`-relativer Hopf-Koeffizient bleibt offen.
8. `beta=1` bleibt durch die I4-Gibbs-Rechnung offen.

**Präzedenz-Firewall:** Diese I4-Eigenrelation betrifft `Phi_{beta,chi}` und wird nicht durch den I5-Rollback für `Phi_0` aufgehoben.

---

### I5 — Dilatation, Orbitmarkierung und kanonischer Rotationsabschluss — **PASS A COMPLETE / COUNTERCHECK PENDING**

**Quellen:** NEU-219h–z + `NEU-219_Finalaudit_Gesamtabschluss.md`  
**Audit:** `audits/AUDIT-2026-08-09_P09_I5_Dilatation_Orbitmarkierung_Kanonischer_Rotationsabschluss_Reconciliation.md`  
**Audit-Commit:** `4111eb13`  
**Prüfart:** `AUDIT-RECONCILED` / `AUDIT-REUSED` + `TARGETED-REAUDIT` der Rollback- und Unit-Slot-Kette

**Positiver Strukturkern:**

- adelische Dilatation `C_0(A_f)`, Gruppenwirkung `gamma`, Full-Corner-Struktur;
- exakte algebraische Ecke
  \[
  e\widetilde A_{alg}e=j_A(A_{alg});
  \]
- algebraischer Morita-Kontext;
- Orbitkollaps der unmarkierten Realisierung, daher notwendige externe Markierung
  \[
  \mathcal N_{tag}=\bigoplus_kN_0\delta_k;
  \]
- typisiertes markiertes KMS-Modulgewicht `varpi_{beta,chi}` und Eigenfamilie `Omega_lambda`;
- kanonischer Basislift
  \[
  \boxed{\widetilde L_0=\eta_0\circ j_M\circ L^{cup}\in Z^4(A_{alg},I_0)},
  \]
  mit
  \[
  \boxed{\kappa=0,\qquad\varepsilon=0.}
  \]

**Orbit-No-gos:**

\[
\boxed{N_k=N_0\quad\forall k,}
\]

globale unmarkierte `Pi` daher nicht injektiv; Eckkompressionen separieren die Orbits nicht; `U_{g^{-1}}` erhält den Orbitindex und ist nicht `T^{-1}`.

**Autoritativer Rollback:**

`NEU-219s/t` und das erste `NEU-219u_Abschluss_O219_NoGo_Theorem.md` sind für die Behauptung

\[
t\Phi_0=g^{-\beta}\Phi_0,\qquad s=-1
\]

`SUPERSEDED`. NEU-219v/w zeigen, dass die verwendeten Beweiswege typwidrig bzw. unzureichend waren.

**Stärkerer Endbeweis:**

NEU-219z/y2 verwenden den Unit-Slot-Test mit

\[
a_0^\star=\mu_P^*,
\]

und erhalten für `beta>1`

\[
W(\mu_P^*)=-n^{-\beta}\omega_{\beta,\chi}(G_P)<0.
\]

Für

\[
(\mu_P^*,\mu_{p_1},\mu_{p_2},\mu_{p_3},1)
\]

gilt

\[
\Phi_0=0,\qquad t\Phi_0\neq0.
\]

Daher:

\[
\boxed{t\Phi_0\neq C\Phi_0\quad\forall C\in\mathbb C.}
\]

Kein globaler Rotationsexponent `s` existiert; `lambda` ist wegen `epsilon=0` wirkungslos.

**Quellfehler-Firewall:** Nicht migrieren aus x/y:

- `D_g(e(r))=0`;
- `D_g(B_alg)=0`;
- „gleichmäßiger Grenzwert“ von `ad(Y_N)`;
- falscher erster Index `nk/delta` in der y1-Transportformel.

Korrekt zu verwenden:

\[
D_g^{corr}(e(r))=\mu_m C_{m,n;r}\mu_n^*,
\]

punktweise Normkonvergenz auf jedem festen `a in A_alg`, und

\[
\sigma_n(G_{k,d})=G_{nk,d/\delta}-\rho_{d/\delta}G_{n/\delta,1}.
\]

Der y2-Unit-Slot-Hauptbeweis bleibt trotz seiner historisch überholten Einleitung gültig.

**Reichweiten-Firewall:** Offen bleiben ausdrücklich

- `[O-219-cyclic-representative]` — anderer zyklischer/getwistet-zyklischer Repräsentant derselben Hochschildklasse;
- genuin orbitverschiebender nichtkanonischer Lift;
- voller gewöhnlicher Quotient `M/[A,M]`;
- Weil-/Gammafaktorpfad `[O-219-6]`, exportiert nach NEU-220.

**Gegencheck:** fünf atomare Fragen stehen in §14 des I5-Auditblatts.

---

### I6 — Spaeter Trassenaudit / Superseding- und Routing-Scan

**Quelle:** `NEU-222_Trassenaudit_singulaere_Route_Statuskorrektur_und_offene_Restknoten.md`  
**Status:** `WAITING FOR I5 SEAL`  
**Prüfziel:** NEU-222 nur als lokalen Trassen-/Statusanker reconciliieren. Bei Konflikten haben August-Direktaudits und der NEU-219-Finalaudit Vorrang. Für jeden späteren No-go ist explizit zu entscheiden: `P09-CORE-NOGO`, `P10-NOGO` oder `SUPERSEDED`.

---

## 5. Routing-Firewalls

- **P09:** BC/Hochschild-/KMS-/Koeffizientenstruktur, belastbare Cup-/Derivationsresultate und strukturentscheidende No-gos.
- **P10:** kondensierte Sammlung isolierter ausgeschlossener Kandidaten; P09-CORE-NOGOs dürfen gespiegelt, aber nicht aus P09 entfernt werden.
- **P11:** globale nichtorthogonale Gramkopplung, intrinsische Quellhilbertisierung, Mediator und Objekt-X-Gesamtgeometrie.
- **P12:** finite-to-infinite Weil-Grenzfragen.

P09 darf weder die P11-Quell-/Gramstruktur vorwegnehmen noch aus einer Hochschild-, KMS- oder zyklischen Klasse unmittelbar einen Hilbert–Polya-Operator ableiten.

### P09-CORE-NOGOs nach I5

- zu starke Schwartz-Regularisierung (NEU-212),
- globaler normstetiger Bimodul-Glätter (NEU-215),
- untypisierte lokale NEU-217-Koeffizientenklasse,
- Baker-/komplexe `log q`-Koeffiziententrennung im ersten NEU-218,
- direkter gewöhnlicher KMS-Detektor des geladenen Zielelements,
- falsche Twist-Orientierung im Standard-Letztrand,
- standardmäßige getwistete Zyklizität der rohen geladenen I4-KMS-Kochain,
- 1-dim. unitales `sigma_beta`-äquivariantes `A_alg`-Bimodul,
- gewöhnliche Zyklisierung des `w!=1`-Gewichtssektors,
- kanonische `H_Gamma`-Aktion allein aus der Gradierung,
- Standard-`H_beta`-SAYD mit gleichzeitig exaktem KMS-Twist und Ladung,
- formales `u_g` ohne echte Dilatation,
- unmarkierte Orbitdirektheit / globale `Pi`-Injektivität,
- Eckkompression als Orbitseparator,
- `U_{g^{-1}}=T^{-1}` auf `N_tag`,
- typwidrige U-Eingaberotation,
- R1–R3 als Beweis einer globalen Basisliftrotation,
- globale konstante Rotationseigenrelation des kanonischen Basislifts `Phi_0`.

---

## 6. Naechster Arbeitsschritt

Aktueller Stand:

\[
\boxed{
\text{P09 PASS A OPEN — I1–I4 SEALED; I5 COMPLETE / COUNTERCHECK PENDING.}
}
\]

Nach Gegencheck der fünf atomaren I5-Fragen ohne konkreten Befund wird I5 versiegelt und I6 (`NEU-222`) als letzter Superseding-/Routing-Scan aktiviert.
