# KARTE — Vollständige Verzeichnisstruktur des Repositorys `objekt-x-programm`

> **Historische Struktur-/Forschungskarte.** Die Verzeichnisauflistung und der darunter
> als „Aktueller Forschungspfad“ bezeichnete NEU-250a-Pfad stammen aus dem Stand
> 6. August 2026 und sind **nicht mehr die operative Front**.
> Aktuell maßgeblich sind [CURRENT-FRONT.md](CURRENT-FRONT.md),
> [ACTIVE_THEOREM_REGISTRY.md](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md) und
> [FORSCHUNGS_ROADMAP_2026-08-26.md](00-uebersicht/FORSCHUNGS_ROADMAP_2026-08-26.md).
> **Operativer Forschungsstand seit 2. September 2026:** B / Strong Terminal. R38--R42
> sind frozen als independently verified AI-GREEN; R43 ist der aktive offene Block. Für jedes
> feste \(0<R<S\) ist C6 auf
> \(\operatorname{Re}\langle\varepsilon_R,K_{R,S}^{T,U}\varepsilon_R\rangle\to1\ ?\)
> reduziert. R37/G4c bleibt separat offen.

> Direkt aus dem Repository verifiziert. Stand: 2026-07-28 (Bereinigungsdurchlauf).  
> Auditstand aktualisiert: 2026-07-29 (NEU-123-Komplex + NEU-124/125/127 + NEU-128A/B/130–145 + NEU-151–155).  
> Strukturupdate: 2026-08-05 (NEU-245b in 07 eingetragen; 06 vollständig aufgelistet; NEU-250 aus 06 entfernt).  
> Forschungsupdate: 2026-08-06 (NEU-245c eingetragen; M3-No-Go und M4 notiert; aktiver Pfad gesetzt).  
> **Forschungsupdate: 2026-08-06 Abend (NEU-245d, NEU-245e/f, NEU-246–NEU-250a eingetragen; aktiver Pfad auf [O-221-1c1a0-C] gesetzt).**
> **Operatives Forschungsupdate: 2026-09-02:** P11 Strong-Terminal-Auditfolge
> `audits/P11_REFEREE_E2E_R38_...` bis `R43_...` ergänzt. R38--R42 frozen; R43 offen.
> Die nachfolgende Verzeichnisauflistung bleibt eine historische Strukturaufnahme und wird
> nicht als vollständige aktuelle Dateiliste ausgegeben.

---

## Historischer Forschungspfad (Stand 6. August 2026)

```
NEU-250 ──Ausgang E──► NEU-250a ──Ausgang B──► [O-221-1c1a0-C]

Aktiver Tiefenknoten:
  j_{2,N}(E^rel_{R;1→2}) als explizites residuenfähiges BC-Element
```

**Letzter Abschluss:** NEU-250a ✓[M]_part — Ausgang B bewiesen: fehlende Repräsentation j_{p,N}: V^pre_{rel,p,N} → F³A^an_BC ist der tiefste gemeinsame Engpass.  
**Nächster Knoten:** [O-221-1c1a0-C] — BC-Repräsentation eines primitiven relativen Primkantenvektors.

---

## Wurzelverzeichnis

```
objekt-x-programm/
├── KARTE.md                          ← diese Datei
├── README.md
├── 00-grundlegung/
├── 01-primkanten-werkzeuge/
├── 02-jacobi-limes/
├── 03-weil-form-statistik/
├── 04-grenzoperator-renormierung/
├── 05-primkanal-fourierladung/
├── 06-hochschild-bc-algebra/
└── 07-weil-explizitformel/
```

---

## 00-grundlegung

```
00-grundlegung/
├── README.md
├── ebene-XVI-objekt-x.md
├── kritischer_pfad_aktuell.md
├── objekt_x_minimalaxiome.md
├── objekt_x_p1_3a_spektraltriage.md
├── objekt_x_p1_3b01_wachstumstest.md
├── objekt_x_p1_3b02_semigroup_group_bridge.md
├── objekt_x_p1_3b03_archimedisch.md
├── objekt_x_p1_3b04_heat_gaussian.md
├── objekt_x_p1_3b05_adelisch.md
├── objekt_x_p1_3b06_poisson.md
├── objekt_x_p1_3b07_schwartz_bruhat.md
├── objekt_x_p1_3b08_vergleichsmorphismus.md
├── objekt_x_p1_3b0_beurling_charakterspur.md
├── objekt_x_p1_3b_charakterspur.md
├── objekt_x_p1_projektionsvergleich.md
├── stufen_0_VI.md
├── teil1_ebenen_I-V.md
├── teil2_ebenen_VI-XV.md
└── teil2_ebenen_VI-XV_variante_NEU-10.md
```

**Gesamt: 20 Dateien** (API-verifiziert 2026-07-28 ✓)

---

## 01-primkanten-werkzeuge

```
01-primkanten-werkzeuge/
├── README.md
├── NEU-003_Schweitzer.md
├── NEU-010_RD_skalenkorrektur.md
├── NEU-010_op16f4b_verifikation.md
├── NEU-010_op16f_beurling_groupoid.md
├── NEU-011_e2_11_berechnung.md
├── NEU-012_fx1_verifikation.md
├── NEU-013_ausschneidung.md
├── NEU-013_r1_e20_uebertragung.md
├── NEU-014_kms_zustand.md
├── NEU-015_op4_frobenius.md
├── NEU-015_r3_bv_op2.md
├── NEU-016_op3_1_monoidladung.md
├── NEU-016_op3_modular_spur.md
├── NEU-017_op3_1_2_aequivarianter_lift.md
├── NEU-018_op3_2_lambda_mod.md
├── NEU-019_op3_3_wodzicki.md
├── NEU-020_op3_4_c_rs_nicht_null.md
├── NEU-021_op4_1c_diagonaltrennung.md
├── NEU-022_op4_1c2_euler_kontraktion.md
├── NEU-023_op4_1c3_diagonal_neutralitaet.md
├── NEU-024_op4_1d_rechte_nicht_ausgeartheit.md
├── NEU-025_op4_1top_spaltbarkeit.md
├── NEU-026_x2_spektralformel_architektur.md
├── NEU-027_x2_1_bc_resolvent.md
├── NEU-028_x2_2_primseiten_identifikation.md
├── NEU-029_x2_3_cauchy_spurformel.md
├── NEU-030_x3_bc_operatorbild.md
├── NEU-031_x3_wres_gns_determinante.md
├── NEU-032_x3_connes_kompass.md
├── NEU-033_x3_bc_approximanten.md
├── NEU-034_x3_spektrum_theta_kopplung.md
├── NEU-035_x3_wres_adjungierung_theta.md
├── NEU-036_x3_determinantenkonvergenz.md
├── NEU-037_x3_jacobi_resolvent_mangoldt.md
├── NEU-038_x3_kms_jacobi_mangoldt.md
├── NEU-039_x3_verbundene_wres_spur_primoperator.md
├── NEU-040_x3_frobenius_schur_komplement.md
├── NEU-041_x3_kanonischer_kopplungsoperator_cn.md
├── NEU-042_x3_fourierhebung_laplace_p_minus_s.md
├── NEU-043_x3_reinheitslemma_rel_primclock.md
├── NEU-044R_Rueckbindung_NEU137_Schritte_S1_S2.md
├── NEU-044X_Rangstruktur_Cprel_Definition.md
├── NEU-044Xprime_Rang1_Stabilitaet_unter_Stoerungen.md
├── NEU-044_Relative_Primkanten_Normierung.md
├── NEU-044_x3_wres_kantendiagonalitaet_pq_test.md
├── NEU-045_x3_relative_feshbach_determinante_euler_mangoldt.md
├── NEU-046_x3_renormierte_relative_determinante_weyl_korrekturen.md
├── NEU-047_x3_archimedische_separation_hadamard_divisor.md
├── NEU-048_x3_residuenbilanz_divisorneutralitaet.md
├── NEU-049_x3_birman_schwinger_indexsatz.md
├── NEU-050_x3_kollektiver_birman_schwinger_operator.md
├── NEU-051_x3_resolventenmatrixelement_kpq.md
├── NEU-052_x3_spektralbasis_graphbasis_drel.md
├── NEU-053_x3_operatorstatus_drel_selbstadjungiertheit.md
├── NEU-054_x3_nelson_selbstadjungiertheit_konfinement.md
├── NEU-055_x3_nelson_matrixabschaetzung_schur.md
├── NEU-056_x3_gammaN_konfinement_obstruktion.md
├── NEU-223_Quellenaudit_alternativer_Vergleichsoperator_Schur_Konfinement_und_kompakter_Resolvent.md
├── NEU-224_Kernbestimmung_flache_Achsen_Antisymmetrisierung_und_effektiver_Raum.md
├── NEU-225_Primfaserdiagonalisierung_Transportgenerator_und_Schichtenverschiebung.md
├── NEU-226_Quellenaudit_globaler_Feshbach_Transfer_Schattenklasse_und_Primkanalueberlappung.md
├── NEU-227_Koordinatenwoerterbuch_und_Spektralmassform_des_Feshbach_Transfers.md
├── NEU-228_Der_u_Regulator_ist_die_Hebungswahl_Ruecklauf_in_die_alte_Barriere.md
├── NEU-228b_Leerfaserpruefung_Gramblock_Orthogonalitaet.md
├── NEU-229_Intrinsische_verbundene_Form_und_Mischblock_Gram_Geometrie_der_Hebungsfaser.md
├── NEU-230_O229-2a_Symmetrieklassifikation_kanonischer_Randvektor.md
├── NEU-231_O229-2a-ii_Wres_Aequivarianz_Fixraum_vs_Nullraum.md
├── NEU-232_O229-2a-ii-2b_NEU041_Brueckenaudit.md
├── NEU-233_O229-2_Hauptknoten_Update_part.md
├── NEU-234_O229-2a-iii_Ladungsgraduierung_Pch.md
├── NEU-235_O229-2a-i_GNS_Typisierung_Rohzielraum_Einbettung.md
├── NEU-236_O229-2a_und_O229-2_Formaler_Abschluss_neg_Quelle.md
├── NEU-237_O229-3_Minimales_Randdatum_Eroeffnung.md
├── NEU-238_O229-3B_Kohomologisches_Randdatum_und_3B1_Transgression.md
├── NEU-239_O229-3B1_Quellenaudit_Abschluss_und_Konstruktionsdesiderat.md
├── NEU-240_O229-3B1f-a_Minimalitaetsaudit_kohomologischer_Mechanismus.md
├── NEU-241_O229-3B1f-b_Kettenabbildungs-Audit_Rohkopplung.md
├── NEU-242_O229-3B1f-b1_Quell-und-Zielkomplex-Audit_Tpraw.md
├── NEU-246_Typ-Grad-Kerninvarianzaudit_Koszul-Kandidat.md    ← auch in 07
├── NEU-247_Tensor-Lift-Bewertungsableitungen_Typbruecke.md
├── NEU-247a_Praezisierungen_Typbruecke.md
├── NEU-247b_Domaenenpraezisierung_P5_und_Auditplan_c2b2a.md
├── NEU-248_c2b2a_Wohldefiniertheit_Tensoroperator.md
└── NEU-249_Praezisierungen_Notation_Konstruktion_Stabilitaet.md
```

**Gesamt: 85 Inhaltsdateien + README.md = 86 Dateien gesamt** (API-verifiziert 2026-07-28 ✓)

**Hinweis:** NEU-057 fehlt. NEU-246 auch in `07-weil-explizitformel/` vorhanden — Doppelung, Klärung ausstehend.

---

## 02-jacobi-limes

```
02-jacobi-limes/
├── README.md
├── NEU-058_skalenbilanz_obstruktion.md
├── NEU-059_jacobi_limes_spektralmass.md
├── NEU-060_core_konvergenz_resolventen_stabilitaet.md
├── NEU-061_lokale_matrixstabilisierung_core_konvergenz.md
├── NEU-062_normalisierungsrigiditat_jacobi_limes.md
├── NEU-063_arithmetische_identifikation_weyl_funktion.md
├── NEU-064_endliche_weyl_funktionen_euler_bruchstruktur.md
├── NEU-065_feshbach_jacobi_determinante_xi_funktion.md
├── NEU-066_geschlossene_divisorpfade_trace_feshbach.md
├── NEU-067_primitive_orbit_reduktion_mangoldt.md
├── NEU-068_moebius_feshbach_identitaet_mangoldt.md
├── NEU-069_primitive_zykluszerlegung_divisorgraph.md
├── NEU-070_nicht_backtracking_ihara_divisorgraph.md
├── NEU-071_quotientierung_periodisierung_divisorfluss.md
├── NEU-072_adelischer_skalierungsquotient_BC_zeitlaengen.md
├── NEU-073_theta_matrix_BC_derivation_vergleich.md
├── NEU-074_identifikation_Vn_BC_isometrie_mu_n.md
├── NEU-075_kreuzprodukt_faktorisierung_theta.md
├── NEU-076_faser_symboloperator_no_go.md
├── NEU-077_Feshbach_Kollaps.md
├── NEU-078_Normierungs_NoGo_Feshbach_Skalierung.md
├── NEU-079_Kanalzahl_Skalierung_Jacobi_Limes.md
├── NEU-080_Effektive_Jacobi_Skalierung.md
├── NEU-081_Feshbach_vs_Jacobi_Gewichtsstabilitaet.md
├── NEU-082_Kanalabhaengige_Kopplung_Dichtebedingung.md
├── NEU-083_Mangoldt_Extraktion_Dreifachkonflikt.md
├── NEU-084_Orbit_Trunkierung_Zeilennorm_Barriere.md
├── NEU-085_Starker_Null_Limes_Wandernde_Fenster.md
├── NEU-086_Nilpotenz_Barriere_Jacobi_Schliessung.md
├── NEU-087_Jacobi_Schliessung_Schleifeninvarianten.md
├── NEU-088_Relative_Resolventdeterminante_Schleifenspur.md
├── NEU-089_Hoehere_Schleifen_Asymptotische_Quadratisierung.md
└── NEU-090_Zweite_Schleifenspur_z_Rigiditaet.md
```

**Gesamt: 33 Inhaltsdateien + README.md = 34 Dateien gesamt** (API-verifiziert 2026-07-28 ✓)

---

## 03-weil-form-statistik

```
03-weil-form-statistik/
├── README.md
├── NEU-091_Quadratischer_Pivot_Weil_Form.md
├── NEU-092_Testkegel_Quadratischer_Weil_Lift.md
├── NEU-093_Korrelationskern_Lift_Mangoldt_Masse.md
├── NEU-094_Bochner_Tor_Logarithmische_Korrelationskerne.md
├── NEU-095_Fensterregularisierung_Autokorrelationsdiagnose.md
├── NEU-096_Skalenanalyse_Mangoldt_Autokorrelation.md
├── NEU-097_Zwischenregime_Selbstdual_Skala.md
├── NEU-098_Korrelationsdichte_Massenniveau_Stabilitaet.md
├── NEU-099_Singulaerserien_Schicht_Shift_Feinstruktur.md
├── NEU-100_Restdichte_Shift_Spektrum_Nullstellenpaar.md
├── NEU-101_Goldston_Montgomery_Transfer_Varianzkanal.md
├── NEU-102_Formfaktor_Kalibrierung_Montgomery_Spektraltest.md
├── NEU-103_Entfaltungskarte_Phasenvergleich.md
├── NEU-104_Lokaler_Formfaktor_Test.md
├── NEU-105_Lokaler_Rampen_Test_GUE_Poisson.md
├── NEU-106_Geglaettete_Nullstellenexpansion_Restkanal.md
├── NEU-107_Lokale_Formfaktor_Annahme_Rampen_Aequivalenz.md
├── NEU-108_Rampenform_versus_Weil_Quadratform.md
├── NEU-109_Hauptsymboltest_Weil_Rekonstruktion.md
├── NEU-110_Symboltest_Rampenkanal_versus_Weil_Kanal.md
├── NEU-111_Herglotz_Weil_Bruecke_Jacobi_Realisierung.md
├── NEU-112_Herglotz_Weil_Test_Nullstellenterm_Renormierung.md
├── NEU-113_Bombieri-Normalisierung.md
├── NEU-114_Rueckbindung_Spektralschatten_Objekt_X.md
├── NEU-115_Weil-Distribution_Interface.md
├── NEU-116_Rueckbindungstest_Wres_Wxi.md
├── NEU-117_X_Rigiditaet_R1.md
├── NEU-118_Bombieri_Normalisierung.md
├── NEU-118_X_Rigiditaet_R1_Nachweis.md
├── NEU-119_Spektralmass_Jacobi_zu_Herglotz.md
└── NEU-120_Bombieri_Normalisierung_Herglotz_Grenzuebergang.md
```

**Gesamt: 30 Inhaltsdateien + README.md = 31 Dateien gesamt** (API-verifiziert 2026-07-28 ✓)

---

## 04-grenzoperator-renormierung

```
04-grenzoperator-renormierung/
├── README.md
├── NEU-121Cfix_Normalisierung_C_xi.md
├── NEU-121_Renormierter_Moment_Hilbertraum.md
├── NEU-122_Duale_Spurform_Renormierter_Grenzoperator.md
├── NEU-123_Spurform_Grenzoperator.md
├── NEU-123A_Spurform_Grenzoperator_Variante_A.md
├── NEU-123B_Grenzoperator_Normalform.md
├── NEU-123C_Grenzoperator_Eigenwertzuordnung.md
├── NEU-123D_Grenzoperator_Schleife.md
├── NEU-124_Gewicht_Kanaloperator.md
├── NEU-125_Skalierung_Prim_Kanal.md
├── NEU-126_Operatornorm_Grenzoperator.md
├── NEU-127_Primkanal_Fourier_Ladung.md
├── NEU-128A_Primkanal_Operator.md
├── NEU-128B_Primkanal_Operator_Ueberarbeitung.md
├── NEU-129_Primkanal_Operator_Komplement.md
├── NEU-130_Spurklasse_Sigma_rel_ren.md
├── NEU-131_Spurformel_Sigma_rel_ren.md
├── NEU-132_Primkanal_Abel_Raum.md
├── NEU-133_Primschalen_Graphraum.md
├── NEU-134_Nichtentartung_Primkanal.md
├── NEU-135D_Obere_Schranke_Primkanal.md
├── NEU-136_Jacobi_Grenzoperator_Verbindung.md
├── NEU-137_Absolutkonvergenz_Sigma_rel_ren.md
├── NEU-138_Spurformel_Vorbereitung.md
├── NEU-139_Konvergenzabgrenzung.md
├── NEU-140_Aggregation_Diagonaloperator.md
├── NEU-141_Diagonaloperator_R.md
├── NEU-142_Edge_Label_T2.md
├── NEU-143_T2_Abschluss.md
├── NEU-144_Operator_R_Selbstadjungiertheit.md
├── NEU-145_Regulierte_Spur.md
├── NEU-146_Cutoff_Finite_Part.md
├── NEU-147_Finite_Part_Struktur.md
├── NEU-148_Mellin_Finite_Part_Spur.md
├── NEU-149_Restkontrolle_Kontur.md
└── NEU-150_Rueckbindung_Mellin_Operatorspur.md
```

**Gesamt: 41 Inhaltsdateien + README.md = 42 Dateien gesamt** (API-verifiziert 2026-07-28 ✓)

---

## 05-primkanal-fourierladung

```
05-primkanal-fourierladung/
├── README.md
├── NEU-151_Normalisierungs_Typaudit_Primkanaloperatoren.md
├── NEU-152_Nichtentartung_Primkanalgewichte.md
├── NEU-153_Hebungsunabhaengigkeit_Primkanalgewichte.md
├── NEU-154_Pullback_Kern_Reichweite_Liftform.md
├── NEU-155_Rohkopplung_Primkanalkompression_Rang1Erweiterung.md
├── NEU-156_Verbundene_Restspurform_Rekonstruktion_Eindeutigkeit.md
├── NEU-157_Zulaessigkeitsraum_Rohkopplung_Nichttrivialitaet.md
├── NEU-158_Invariante_Formen_Rohkopplungsquotient_Symmetrieeindeutigkeit.md
├── NEU-159_Dualzeuge_Projektionsnichtvernichtung_Liftzulassigkeit.md
├── NEU-160_Rohkopplungsquotient_Symmetrieabstieg.md
├── [NEU-161 bis NEU-173 + Varianten — Dateinamen noch nicht API-verifiziert]
```

**Gesamt: 33 Inhaltsdateien + README.md = 34 Dateien gesamt** (API-verifiziert 2026-07-28 ✓)

---

## 06-hochschild-bc-algebra

```
06-hochschild-bc-algebra/
[Inhalt unverändert — zuletzt API-verifiziert 2026-08-05]
Gesamt: 84 Inhaltsdateien + README.md = 85 Dateien
```

---

## 07-weil-explizitformel

```
07-weil-explizitformel/
├── README.md
├── NEU-220_Gammafaktor_Quelltyp_und_Zielraum.md
├── NEU-220a bis NEU-220w  [27 Dateien]
├── NEU-221_Adelische_Momentquelle_fuer_den_positiven_Weil-Operator.md
├── NEU-221c_Zyklischer_Feshbach-Weyl_Kandidat_und_quadratische_Resolvente.md
├── NEU-221d_Direktextraktion_NEU46_Zyklischer_Sektor_und_Nullmodusaudit.md
├── NEU-221e_Affine_Hebungsfaser_Wres-Quotient_und_Spektralmassabstieg_Psip.md
├── NEU-242_Abschlussaudit_O229-3B1f-b1_Kettenabbildungs-Negativbefund.md
├── NEU-243_Kompatibilitaetsfirewall_Quell-Zielkomplex_Nichttrivialitaet.md
├── NEU-244_Quotient-first-Zielarchitektur_und_tautologischer_Cone-No-Go.md
├── NEU-245_c2a_Operatortypaudit_NEU195_NEU216.md
├── NEU-245b_Typaudit_O220-1f0_Mindestarchitektur_globale_Archimedes-Prim-Kopplung.md
├── NEU-245c_Audit_Feshbach-Weyl-Kandidat_gegen_O245b1_M1-M4.md
├── NEU-245d_Direktaudit_O245c-1_Kanonisierung_Nullmodus_und_Basismoment.md
├── NEU-245e  [Wres-Direktaudit I]
├── NEU-245f  [Wres-Direktaudit II]
├── NEU-246_Typ-Grad-Kerninvarianzaudit_Koszul-Kandidat.md
├── NEU-247_Tensor-Lift-Bewertungsableitungen_Typbruecke.md
├── NEU-247a_Praezisierungen_Typbruecke.md
├── NEU-247b_Domaenenpraezisierung_P5_und_Auditplan_c2b2a.md
├── NEU-248_c2b2a_Wohldefiniertheit_Tensoroperator.md
├── NEU-249_Praezisierungen_Notation_Konstruktion_Stabilitaet.md
├── NEU-250_[Wres-Minimalblock Kleinfallprüfung]   → Ausgang E
└── NEU-250a_O221-1c1a0-B_Typisierung_Dirichletresiduumsform_relativer_Primkantenraum.md  ← NEU 2026-08-06 → Ausgang B
```

**Gesamt: ~42 Inhaltsdateien + README.md** (Stand 2026-08-06 Abend; exakte Zählung beim nächsten API-Audit)

**Forschungsstatus 07:**
- NEU-250: ✓[M] → **Ausgang E** — keine auswertbare relative Gramform im Minimalblock
- NEU-250a: ✓[M]_part → **Ausgang B** — fehlende Repräsentation j_{p,N}: V^pre_{rel,p,N} → F³A^an_BC als tiefste Lücke identifiziert
- **Aktiver Pfad:** NEU-250 →E→ NEU-250a →B→ [O-221-1c1a0-C]
- **Aktiver Tiefenknoten:** j_{2,N}(E^rel_{R;1→2}) als explizites residuenfähiges BC-Element konstruieren
- NEU-246 auch in `01-primkanten-werkzeuge/` vorhanden — Doppelung, Klärung ausstehend.
