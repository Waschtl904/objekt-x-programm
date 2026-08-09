# P09 Pass-A — Eroeffnung und Inventar

**Datum:** 9. August 2026  
**SYN-Ziel:** P09 — BC + Hochschild  
**Status:** `PASS A OPEN — I1 SEALED, I2 SEALED, I3 COMPLETE / COUNTERCHECK PENDING`  
**Voraussetzung:** P01 dependency-reconciled durch `AUDIT-2026-08-09_P01_Dependency_Reaudit_vor_P09.md`  
**Hauptquellblock:** `06-hochschild-bc-algebra/`

---

## 1. Live-Inventar

Der Ordner `06-hochschild-bc-algebra/` dokumentiert den BC/Hochschild-Strang von NEU-174 bis in den NEU-219-Block; zusätzlich liegt NEU-222 als später Trassenaudit vor.

Wegen mehrfach belegter IDs — insbesondere NEU-183, NEU-193, drei NEU-217-Dateien, zwei NEU-218-Dateien sowie mehrere NEU-219-Unterdateien — arbeitet P09 **pfad- und rollenbasiert**, nicht nach bloßer Nummernsequenz.

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

`NEU-219_Finalaudit_Gesamtabschluss.md` ist der autoritative Endanker für die kanonische geladene Rotationsarchitektur. Bindend ist

\[
\widetilde L_0\longrightarrow\kappa=0\longrightarrow\varepsilon=0
\longrightarrow\text{kein globales }s\longrightarrow\text{kein }\lambda^*,
\]

sowie

\[
\boxed{t\Phi_0\neq C\Phi_0\quad\forall C\in\mathbb C.}
\]

Frühere Zwischenbehauptungen, insbesondere `s=-1`, sind zurückgerollt.

Für den I2/I3-Strang gilt zusätzlich `AUDITSTAND-2026-08-03.md` als kanonisches Kontrollblatt. `OBJEKT-X-BESTANDSAUFNAHME.md` vom 5. August bestätigt als später Gesamtanker ausdrücklich

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

**Endstand:**

- `B_3^mod:=A_Q` und `C_fin^•` liefern einen algebraischen Modell-/Gewichtraumrahmen, keine Hilbertraum- oder Operatoridentifikation;
- im separaten Vier-Prim-Modell existiert eine geladene nichttriviale HH4-Klasse, aber kein automatischer Transfer nach `A_Q`;
- auf `A_Q^alg` ist `[Omega_p] != 0 in HH^4(A,A)` mit Paarungswert `24`, jedoch neutral (`deg_Gamma Omega_p=1_Gamma`);
- `HH^4(A,A)_ch != 0?` bleibt nach I1 offen;
- NEU-184 rev2 ist der saubere Zentrum-Endanker; ältere NEU-183-Zentrumsversion `SUPERSEDED`;
- NEU-187 liefert nur partielle HH1-Daten, keine volle geladene BC-Derivation;
- NEU-190: fehlende Operatorbrücke nur negativer Quellenbefund, kein globaler No-go.

**Seal-Regel:** nur atomare Wiederöffnung bei konkretem neuem mathematischem Gegenbefund.

---

### I2 — Äußere Derivationen und singuläre Potentialroute — **PASS A COMPLETE / SEALED**

**Quellen:** NEU-192–211; Doppeldatei NEU-193; NEU-198 fehlt als Live-Datei  
**Audit:** `audits/AUDIT-2026-08-09_P09_I2_Aeussere_Derivationen_Singulaere_Potentialroute_Reconciliation.md`  
**Audit-Commit:** `6aba82cf`  
**Gegencheck:** `audits/AUDIT-2026-08-09_P09_I2_Gegencheck_Pfadgebunden.md`  
**Gegencheck-Commit:** `438aca8e` — `VALID`, kein Gegenbefund

**Endstand:**

- zweiter NEU-193: geladener Dualzyklus; Paarung sieht `Alt_4`;
- symmetrische NEU-176-Schablone für diesen Zeugen blind; determinantisches Modell paart mit `24`, ist aber kein Kozykel;
- NEU-196 schließt nur den Augmentationsdetektor gegen punktierte Potentiale aus;
- NEU-197 liefert den partiellen Kommutatorquotienten als universellen Detektor;
- NEU-201-Primreihenkandidat durch NEU-202 `SUPERSEDED`;
- NEU-204: singuläre Kommutatorregularisierung positiv, aber neutral und `A_C*`-wertig;
- NEU-205: historische Sandwichformel und „Divergenz für jedes r“ `×[M]`; konkrete dyadische L/R/S-Platzierungen kandidatenspezifisch negativ; Architektur III offen;
- NEU-208: korrekt `||B_k|| = sum_{p|k} log((v_p(k)+2)/2)`, nicht Max-Norm;
- NEU-209/210: gemeinsame Ursprungslokalisierung; `M(0)=0 => MX_N` schließlich konstant, nicht notwendig `->0`;
- NEU-211 nur korrigiert lesen: `D_g^corr(e(r))=mu_m C_{m,n;r} mu_n*`, punktweise Normkonvergenz auf jedem festen `a in A_alg`;
- Hauptbefund:

\[
\boxed{[D_g^{\rm corr}]\neq0\in HH^1(A_{\rm alg},A_{C^*})_g,\qquad g\neq1.}
\]

- daraus noch kein algebraisches geladenes HH1 und noch kein HH4 mit Selbstkoeffizienten.

**Seal-Regel:** nur atomare Wiederöffnung bei konkretem neuem mathematischem Gegenbefund.

---

### I3 — Koeffizientenmodule, Bimodul-No-go und Cup-Aufstieg — **PASS A COMPLETE / COUNTERCHECK PENDING**

**Quellen:** NEU-212–218, pfadgebunden mit drei NEU-217- und zwei NEU-218-Dateien  
**Audit:** `audits/AUDIT-2026-08-09_P09_I3_Koeffizientenmodule_Bimodul_Cup_Reconciliation.md`  
**Audit-Commit:** `b513a854`  
**Prüfart:** `AUDIT-RECONCILED` / `AUDIT-REUSED` + `TARGETED-REAUDIT` des NEU-218-Følnerbeweises

**Endstand:**

1. **NEU-212:** geschriebene `A^infty`-/Schwartz-Zieltypbrücke zentral `×[M]`; verwendbar bleiben nur der neutrale Schnellabfallraum `S_0` und der endliche Schalenträger von `C_{m,n;r}`.
2. **NEU-213:** richtige Fehlerdiagnose, aber spätere Direktaudits verschärfen die Statuskorrekturen; daher teilweise `SUPERSEDED`.
3. **NEU-214/215:**
   \[
   \operatorname{Cent}_{A_{C^*}}(A_{\rm alg})=\mathbb C1,
   \]
   und jeder normstetige globale `A_alg`-Bimodulglätter in einen echten Teilraum ist null. `P09-CORE-NOGO`.
4. **NEU-216:** direkter logarithmischer Zieltyp statt nachträglicher Glättung:
   \[
   B_{\rm alg}\subsetneq B^{\log}\subsetneq C(\widehat{\mathbb Z}),
   \]
   `B^log` unitaler Banach-`*`-Koeffiziententyp; `sigma_k,rho_k,T_a` stabil; `G_{a,d} in B^log`; algebraische graduierte `A^log`; 
   \[
   [D_g^{\rm corr}]\neq0\in HH^1(A_{\rm alg},A^{\log})_g.
   \]
   Historischer gcd-Faktor `1/r` ist `×[M]`.
5. **NEU-217:** lokale Koeffizienten-HH1-Aussage mit `M_{g,p}^log` nicht vollständig typisiert; globale Konstruktion funktioniert:
   \[
   [D_g^{\rm corr}]\neq0\in HH^1(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
   \]
   Formel `(G1)` mit erstem Index `nk`, nicht `nk/delta`.
6. **NEU-218:** neutraler Grad-3-Partner `Theta^wedge` ist nichttrivial; der geladene Cup ist Kozykel. Alte Augmentations-/Baker-Wege sind nicht final. Der Abschluss beweist per Mehrparameter-Følnerargument einen nichtverschwindenden partiellen Modulquotienten, konstruiert einen Dualzyklus und erhält:

\[
\boxed{
[D_g^{\rm corr}]\smile[\Theta^\wedge]
\neq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
}
\]

Der volle Quotient gegen `[A,M]` bleibt offen und ist für diesen Beweis nicht erforderlich.

**Reichweiten-Firewall:** Kein Schluss auf `HH^4(A_alg,A_alg)_g`, keine automatische zyklische/KMS-/Weil-/Operatorrealisierung. NEU-219 blockiert erst die kanonische zyklische/Rotationsverfeinerung und rollt den Hochschild-Cup nicht zurück.

**Seal-Regel:** nach externem Gegencheck ohne Befund versiegeln; bei Gegenbefund nur atomare Wiederöffnung.

---

### I4 — KMS, zyklische und Hopf-zyklische Kandidaten

**Quellen:** NEU-219, NEU-219a–g  
**Status:** `WAITING FOR I3 SEAL`  
**Prüfziel:** positive KMS-/Auswertungsformeln von der Existenz eines gewöhnlichen, getwisteten oder Hopf-zyklischen Repräsentanten trennen; spätere Rotations-No-gos berücksichtigen.

---

### I5 — Dilatation, Orbitmarkierung und kanonischer Rotationsabschluss

**Quellen:** NEU-219h–z + `NEU-219_Finalaudit_Gesamtabschluss.md`  
**Prüfziel:** Finalaudit als autoritativen Endstand migrieren; `s=-1` und andere Rollback-Zwischenbehauptungen als `SUPERSEDED` markieren.

---

### I6 — Später Trassenaudit / Superseding-Scan

**Quelle:** NEU-222  
**Prüfziel:** nur als lokaler Trassen-/Statusabgleich; bei Konflikten haben August-Direktaudits und Finalaudit Vorrang.

---

## 5. Routing-Firewalls

- **P09:** BC/Hochschild-/KMS-/Koeffizientenstruktur, belastbare Cup-/Derivationsresultate und die strukturentscheidenden No-gos.
- **P10:** kondensierte Sammlung isolierter ausgeschlossener Kandidaten; P09-CORE-NOGOs dürfen gespiegelt, aber nicht aus P09 entfernt werden.
- **P11:** globale nichtorthogonale Gramkopplung, intrinsische Quellhilbertisierung, Mediator und Objekt-X-Gesamtgeometrie.
- **P12:** finite-to-infinite Weil-Grenzfragen.

P09 darf weder die P11-Quell-/Gramstruktur vorwegnehmen noch aus einer Hochschildklasse unmittelbar einen Hilbert–Pólya-Operator ableiten.

### P09-CORE-NOGOs nach I3

- zu starke Schwartz-Regularisierung (NEU-212),
- globaler normstetiger Bimodul-Glätter (NEU-215),
- untypisierte lokale NEU-217-Koeffizientenklasse,
- Baker-/komplexe `log q`-Koeffiziententrennung im ersten NEU-218.

Diese bleiben in P09, weil sie die positive Architektur `B^log -> M_glob^log -> HH4` typisieren.

---

## 6. Nächster Arbeitsschritt

Aktueller Stand:

\[
\boxed{
\text{P09 PASS A OPEN — I1 SEALED; I2 SEALED; I3 COMPLETE / COUNTERCHECK PENDING.}
}
\]

Die fünf atomaren Gegencheckfragen stehen in §14 des I3-Auditblatts. Nach Gegencheck ohne konkreten Befund wird I3 versiegelt und I4 (NEU-219, NEU-219a–g) aktiviert.
