# P08 Pass-A — Eröffnung und Inventar Grenzoperator + Renormierung

**Datum:** 9. August 2026  
**SYN-Ziel:** P08 — Grenzoperator + Renormierung  
**Verfahren:** Pass A gemäß `00-uebersicht/SYN_MIGRATIONSPROTOKOLL.md`  
**Voraussetzungen:** P02 `SYN FROZEN`, P05 `SYN FROZEN ✓[K/M]`, P06 `SYN FROZEN ✓[K/M]`; P07 als Status-/RH-Äquivalenzreferenz  

**Status dieses Blatts:**

\[
\boxed{\text{P08 PASS-A-ERÖFFNUNG COMPLETE — Primärreconciliation ausständig.}}
\]

Kein P08-SYN-Transfer vor Primärreconciliation, unabhängiger Gegenprüfung und finaler Pass-A-Versiegelung.

---

## 0. Verbindliche Pass-A-Regel

P08 wird **nicht** blind als 41-Dateien-Vollaudit eröffnet. Die Regel bleibt:

\[
\text{heutige Live-Datei}
+
\text{vorhandene Audits}
+
\text{spätere Korrekturen/SYN-Firewalls}
\longrightarrow
\text{heute gültiger Endstand}.
\]

Prüfarten:

- `AUDIT-REUSED`: nur wenn Audit und heutiger Dateiinhalt tatsächlich zusammenpassen;
- `AUDIT-RECONCILED`: vorhandener Audit + spätere Korrekturen werden vereinigt;
- `TARGETED-REAUDIT`: konkrete Kollision/Lücke isoliert;
- `NEW-DIRECT-AUDIT`: kein belastbarer unabhängiger Audit vorhanden.

**Neue P08-Firewall:** Eine historische Audit-Zuordnung nach bloßer NEU-Nummer genügt nicht. Der mathematische Inhalt muss mit der heutigen Live-Datei übereinstimmen.

---

## 1. Live-Inventar Ordner 04

Kanonischer Live-Ordner:

`04-grenzoperator-renormierung/`

Der aktuelle `README.md` und der Git-Tree enthalten **41 Forschungsdokumente** plus README.

### H0 — Moment/KMS-Eingang (3 Dokumente)

1. `NEU-121_Renormierter_Moment_Hadamard_Abgleich.md`
2. `NEU-121Cfix_Normalisierung_C_xi.md`
3. `NEU-122_KMS_GNS_vs_Spektralnaehrung.md`

### H1 — Jacobi-Grenzoperator / Renormierungsbarrieren (14 Dokumente)

4. `NEU-123_Jacobi_Grenzoperator_Resolventenkonvergenz.md`
5. `NEU-123A_Jacobi_Koeffizienten_Extraktion.md`
6. `NEU-123B_Renormierungsbarriere_Jacobi.md`
7. `NEU-123C_Dreifachsumme_Diagonaldrift.md`
8. `NEU-123D_Paritaetskorrektur_Dreifachsumme.md`
9. `NEU-123E_Sparse_Shift_Barriere.md`
10. `NEU-123F_Numerische_Diagnose_Dreifachsumme.md`
11. `NEU-123F_Ergebnisse.md`
12. `NEU-123G_Zweite_Offdiagonale_Skaleninkohaerenz.md`
13. `NEU-123H_No_scalar_renormalization.md`
14. `NEU-123I_Gradierte_Renormierung_Herglotz.md`
15. `NEU-124_Spektrum_Spektralmass_Jacobi_Grenzoperator.md`
16. `NEU-125_Intrinsische_Feshbach-Skala_vor_Lanczos.md`
17. `NEU-127_Kanalseiten_Gramform_Triage.md`

### H2 — Prä-Lanczos-/Primkanal-/Selbstenergie-Schicht (14 Dokumente)

18. `NEU-128A_Ruecklese_NEU41_KlasseB_Pruefung.md`
19. `NEU-128b_self_energy_vs_prae_lanczos_metrik.md`
20. `NEU-130_PSWF_Bruecke_Edge_Koerzivitaet_Prae_Lanczos_Metrik.md`
21. `NEU-131_Abstraktes_Edge_Schur_Nelson_Lemma.md`
22. `NEU-132_H1H2H3rel_PSWF_Abel_Primkantenraum.md`
23. `NEU-133_Primschalen_Abel_Lemma_relativer_Graphraum.md`
24. `NEU-134_Extraktion_relativer_Kanalgewichte_NEU44.md`
25. `NEU-135_Normkonvention_Primkanal_Log_Absorption.md`
26. `NEU-135D_Entscheidung_Welt2.md`
27. `NEU-136_Logarithmisches_Abel_Lemma_H3rel.md`
28. `NEU-137_Spurklassen_renormalisierte_Selbstenergie.md`
29. `NEU-138_Fredholm_Spurformeln_Zeta_Rueckbindung.md`
30. `NEU-139_Gewichtstest_Kreuzterm_Zeta_Identifikation.md`
31. `NEU-140_Normierungsbruch_Spurklasse_Mangoldt.md`

### H3 — Mangoldt-Renormierung / Edge-Label (5 Dokumente)

32. `NEU-141_Unbeschraenkte_Mangoldt_Renormierung.md`
33. `NEU-142_T2_Label_Audit.md`
34. `NEU-143_T2_Abschluss_Edge_Label.md`
35. `NEU-144_R_Primdiagonale_Observable.md`
36. `NEU-145_Regulierte_Mangoldt_Spur.md`

### H4 — Cutoff / Mellin / Finite Part (5 Dokumente)

37. `NEU-146_Cutoff_Finite_Part_Mangoldt_Spur.md`
38. `NEU-147_Explizite_Finite_Part_Struktur.md`
39. `NEU-148_Geglaettete_Mellin_Finite_Part_Spur.md`
40. `NEU-149_Restkontrolle_Nullstellenvermeidende_Kontur.md`
41. `NEU-150_Rueckbindung_Mellin_Operator_Spur.md`

### Buchhaltungsauffälligkeiten

- `NEU-123F` existiert **zweimal** mit zwei verschiedenen Dateien; im P08-Endstand muss stets der Dateiname mitgeführt werden.
- `NEU-126` fehlt live; NEU-127 selbst dokumentiert die verlorenen/geplanten 126.A/126.B und unterlässt bewusst eine Rekonstruktion.
- `NEU-129` existiert im aktuellen Live-Tree ebenfalls nicht.
- Die alte `KARTE.md` enthält für Ordner 04 teilweise historische/abweichende Dateinamen und ist für die P08-Dateibuchhaltung **nicht** kanonisch; maßgeblich sind Live-Tree und `04-grenzoperator-renormierung/README.md`.

---

## 2. Vorhandener Auditbestand und Provenienzproblem

### 2.1 Was aus Juli sicher vorhanden ist

Die Juli-/August-Zwischenbilanzen dokumentieren:

- `DAG-Audit NEU-123–127`;
- Auditblöcke NEU-128A/B/130/131;
- NEU-132–136;
- NEU-137–140;
- NEU-141–145;
- NEU-146–150 mit bereits bekanntem Mellinfehler;
- Detailarchive ab NEU-128 in `ARCHIV-AUDIT-2026-07.md` bzw. den datierten Zwischenbilanzen.

Damit ist **kein pauschaler 41-Dateien-Vollaudit** gerechtfertigt.

### 2.2 Warum Audit-Reuse nicht nach Nummer erfolgen darf

Die historische Bilanzbeschreibung stimmt bei mehreren IDs nicht zuverlässig mit dem heutigen Live-Inhalt überein. Beispiele:

- Die Juli-Bilanz charakterisiert `NEU-130` als Spurklassenabschätzung für `Sigma_rel^ren`; live ist `NEU-130_PSWF_Bruecke_Edge_Koerzivitaet_Prae_Lanczos_Metrik.md` eine PSWF-/Edge-Koerzivitätsbrücke.
- Die Juli-Bilanz charakterisiert `NEU-136` als Verbindung Jacobi-Limes → Grenzoperator; live ist NEU-136 die Zerlegung der renormalisierten Selbstenergie `Sigma_rel = Sigma_rel^infty + Sigma_rel^ren`.
- Live-`NEU-128A` ist ein Rückleseprotokoll zu NEU-41/Klasse B und behauptet insbesondere eine Rang-1-Gram-/Projektorstruktur, während die Juli-Kurzbilanz NEU-128A anders beschreibt.

Für `NEU-130` zeigt die Git-Historie nur den initialen öffentlichen Import vom 26. Juli 2026. Die Diskrepanz lässt sich daher jedenfalls in diesem Beispiel nicht durch eine spätere P08-Dateiänderung nach dem Juli-Audit erklären.

**Konsequenz:** Historische Kurzbilanztexte werden als Navigationshilfe benutzt, aber ein `AUDIT-REUSED` wird erst nach Inhaltsabgleich vergeben.

---

## 3. Bereits eingefrorene superseding Firewalls

### 3.1 P05 — Primkanal-/Liftgeometrie

Für P08 verbindlich:

- `rank C_p^rel <= 1` nur auf der induzierten modellrelativen Ebene;
- der gewichtete Rang-1-Operator ist im Allgemeinen **kein orthogonaler Projektor**;
- `c_p != 0` ist nicht unbedingter Satz;
- Hebungsunabhängigkeit von `|c_p|^2` ist offen;
- eine termweise Asymptotik
  `|c_p|^2 ~ (log p)^2/p`
  ist nicht bewiesen;
- intrinsische Edge-/Lift-/Gramgeometrie darf nicht aus historischen Modellannahmen importiert werden.

Daher müssen alle P08-Aussagen über `P_p`, `c_p`, T2-Orthogonalität, `R_p = log p/|c_p|^2` und primweise Direktsummen gegen P05 reconciliert werden.

### 3.2 P06 — Jacobi/Feshbach/Spektralstatus

Für P08 verbindlich:

- `J_N^- = 1/2(Theta_N-Theta_N^dagger)` ist schiefadjungiert;
- `S_N = (1/2i)(Theta_N-Theta_N^dagger) = -i J_N^-` ist die selbstadjungierte Version;
- der direkte historische Jacobi-Limes ist **nicht** der Hilbert–Pólya-Endoperator;
- `D_rel` ist in auditierten Primfasern Transportgenerator mit rein absolutstetigem Spektrum;
- endliche Feshbachidentität impliziert keine Schattennormkonvergenz;
- festes Primcutoff `N` impliziert keinen endlichen Rang des globalen Feshbachtransfers;
- im konkreten NEU-088–90-Modell kollabiert die historische Schleifendeterminante auf `D_N(z) -> 1`, ohne allgemeinen Feshbach-No-Go.

Damit müssen P08-Jacobi-Grenzoperator-, Herglotz-, Schatten- und Fredholmaussagen strikt als abstrakte/konditionale Modellresultate von einer Objekt-X-Endoperatorbehauptung getrennt werden.

---

## 4. Bereits identifizierte konkrete Konflikte

### 4.1 NEU-121 / 121Cfix

NEU-121 enthält den falschen Zahlenwert `C_xi ~ -0.5493` für

`C_xi = -xi'(0)/xi(0)`.

`NEU-121Cfix` korrigiert bindend zu

\[
C_\xi
=1+\frac{\gamma_E}{2}-\frac12\log(4\pi)
\approx 0.0230957.
\]

Der alte Zahlenwert ist `SUPERSEDED`.

### 4.2 NEU-123-Familie gegen P06-Typisierung

Mehrere frühe Blätter sprechen von `A_N^{Jac,-}` als selbstadjungiertem Jacobi-Operator. Vor Übernahme nach P08 muss geklärt werden, ob dies die selbstadjungierte `S_N`-Schließung bezeichnet oder den historischen antisymmetrischen `J_N^-`-Typ vermischt. Zusätzlich darf ein abstraktes Jacobi-Trunkierungslemma nicht wieder als konkreter Objekt-X-/HP-Grenzoperator gelesen werden.

### 4.3 NEU-128A gegen P05

Live-NEU-128A bezeichnet `C_p C_p^#` als Rang-1-Projektor und stuft eine Gram-/Selbstenergieform relativ stark hoch. P05 friert dagegen die Typtrennung und die Nicht-Projektor-Firewall ein; Nichtentartung und Hebungsunabhängigkeit bleiben offen.

Dieser Konflikt ist vor P08-SYN lokal zu reconciliieren.

### 4.4 Mellin-Grundfehler NEU-148 → NEU-149/150

NEU-148 definiert

\[
S_{\varphi,X}(\beta)
=\sum_p \varphi(p/X)\frac{\log p\,p^{-\beta}}{1-p^{-\beta}}.
\]

Nach Mellin-Inversion entsteht jedoch

\[
\sum_{p,k\ge1}\log p\,p^{-k\beta-s},
\]

während

\[
-\frac{\zeta'}{\zeta}(\beta+s)
=\sum_{p,k\ge1}\log p\,p^{-k\beta-ks}.
\]

Die in NEU-148.2 behauptete Identität mit `-zeta'/zeta(beta+s)` ist daher für den Cutoff `varphi(p/X)` falsch. Der korrekte von-Mangoldt/Mellin-Cutoff benutzt `varphi(p^k/X)`.

NEU-149 korrigiert zwar einen separaten Fehler aus NEU-148 — `hat varphi` hat bei `s=0` einen Pol mit Residuum 1, wenn `varphi=1` nahe 0 — übernimmt aber die falsche Mellin-Grundidentität und kann deshalb die Schlussformel für das definierte `S_{varphi,X}` nicht retten.

NEU-150s Aussage „Primlabel-Finite-Part = -zeta'/zeta“ hängt ausdrücklich an NEU-148/149 und ist daher ebenfalls nicht als `✓[M]` übernehmbar. Die rein algebraische Identität zwischen einem **definierten** Primlabel-Cutoff und der entsprechenden endlichen Primsumme ist davon getrennt zu prüfen.

Dieser Konflikt entspricht dem bereits in der Juli-Bilanz notierten Mellinfehler (`varphi(p/X)` vs. `varphi(p^k/X)`), wird jetzt aber für Pass A präzise lokalisiert.

---

## 5. Vorläufige Prüfartmatrix

| Paket | Dateien | Vorläufige Prüfart | Grund |
|---|---|---|---|
| **H0** | NEU-121, 121Cfix, 122 | `NEW-DIRECT-AUDIT` / `AUDIT-RECONCILED` | kein belastbarer separater Juli-Direktaudit für 121/122 identifiziert; Cfix ist bindende Korrektur |
| **H1** | NEU-123-Familie, 124, 125, 127 | `AUDIT-RECONCILED` + gezielt `TARGETED-REAUDIT` | DAG-Audit vorhanden; P06-Typ-/Spektralstatus superseding |
| **H2** | NEU-128A/b, 130–140 | `AUDIT-RECONCILED` + `TARGETED-REAUDIT` | Juli-Auditmaterial vorhanden, aber Kurzbilanz↔Live-Inhalt nicht zuverlässig; P05/P06-Firewalls greifen |
| **H3** | NEU-141–145 | `AUDIT-RECONCILED` + `TARGETED-REAUDIT` | Juli-Audit vorhanden; T2/c_p/R/Schatten-/zeta-Trace-Aussagen durch P05/P06 zu begrenzen |
| **H4** | NEU-146–150 | `TARGETED-REAUDIT` | bereits bekannter und live bestätigter Mellinfehler; Downstream-Vererbung bis NEU-150 |

**`NEW-DIRECT-AUDIT` wird damit vorläufig nur für die kleine H0-Eingangsschicht zugelassen.** Für H1–H4 wird der vorhandene Auditbestand maximal wiederverwendet und nur an konkreten Kollisionsstellen neu gerechnet.

---

## 6. Geplanter minimaler Reaudit-Satz

Vorläufig fünf gezielte Prüfaufträge:

### H-T1 — NEU-121/121Cfix/122: Moment/KMS/Herglotz

Prüfen:
- C_xi-Normalisierung;
- KMS-GNS-Normalisierung;
- Typ von `A_N^{Jac,-}` gegen P06 `J_N^- / S_N`;
- welche Herglotz-/RH-Implikationen nur konditional bleiben.

### H-T2 — NEU-123-Familie/124/125: Jacobi-Grenzoperator

Prüfen:
- abstraktes Jacobi-Trunkierungs-/Carleman-Lemma;
- konkrete Koeffizientenstabilisierung;
- selbstadjungierter Typ;
- Spektralmaß statt bloßes Spektrum;
- vollständige Trennung vom historischen direkten HP-Limes.

### H-T3 — NEU-127/128A/b/130/131: Prä-Lanczos-Grammetrik

Prüfen:
- `C_p C_p^#`/`P_p`-Typen;
- „Projektor“ vs. gewichteter Rang-1-Operator;
- Kanonizität/Hebungsabhängigkeit;
- zulässige positive Prä-Lanczos-Form ohne P11-Import.

### H-T4 — NEU-132–145: Selbstenergie/Schatten/Mangoldt-Renormierung

Prüfen:
- alle `c_p`-Schranken nur im heute zulässigen Status;
- T2-/Edge-Orthogonalität;
- Spurklasse nur unter klaren Hypothesen;
- `R`-Observable und Domain;
- gewöhnliche Spur vs. definierte analytische Fortsetzung;
- keine zirkuläre Zeta-/RH-„Herleitung“.

### H-T5 — NEU-146–150: Cutoff/Mellin/Finite Part

Prüfen:
- Cutoffvariable `p` vs. `p^k`;
- Mellintransformierte bei `s=0`;
- korrekte `-zeta'/zeta`-Mellinidentität;
- Residuen-/Restkontrolle erst nach korrekter Ausgangssumme;
- welche Teile von NEU-150 rein operatoralgebraisch erhalten bleiben;
- keine Hochstufung des Primlabel-Finite-Parts vor Reparatur der Mellinroute.

---

## 7. Vorläufiges Routing für P08

### In P08 gehören

- abstrakte Grenzoperator-/Resolventenkonvergenzkriterien;
- Renormierungsbarrieren vor/nach Lanczos;
- konditionale Prä-Lanczos-Form-/Selbstenergiearchitektur;
- Spurklassen-/Fredholmkriterien mit expliziten Voraussetzungen;
- saubere Trennung gewöhnliche Spur / Regularisierung / Finite Part;
- Mellin-/Cutoff-No-Gos und korrigierbare analytische Schnittstelle.

### Nicht als gelöste P08-Grundlage importieren

- intrinsische globale Primkanal-/Lift-/Gramgeometrie → P11;
- direkter Jacobi-/Transportoperator als HP-Endoperator → durch P06 gesperrt;
- unbedingte `c_p`-Nichtentartung oder `|c_p|^2 ~ (log p)^2/p` → offen nach P05;
- zeta-/xi-Identifikation, die durch Definition der Zielspur bereits eingebaut wurde → höchstens Regularisierungsdefinition/No-Go, kein arithmetischer Herleitungssatz;
- historische Mellin-Finite-Part-Schlussformel aus NEU-148–150 vor Reparatur → gesperrt.

---

## 8. Endurteil der Eröffnung

P08 ist **nicht** auditfrei, aber auch **kein 41-Dateien-Neuaudit**.

Der vorhandene Juli-Auditbestand ist substanziell und wird weiterverwendet. Wegen der nachträglich eingefrorenen P05/P06-Endstände, der unzuverlässigen Kurzbilanz↔Live-ID-Zuordnung und des konkreten Mellinfehlers sind jedoch fünf lokale Reconciliation-/Reaudit-Pakete erforderlich.

\[
\boxed{\text{P08 PASS-A-SCOPE: 41 Live-Dokumente, 5 Prüfpakete, nur H0 mit möglichem NEW-DIRECT-AUDIT.}}
\]

Nächster Schritt:

\[
\boxed{\text{H-T1 bis H-T5 abarbeiten }\longrightarrow\text{ P08 Primärreconciliation}.}
\]

Danach unabhängiger pfadgebundener Gegencheck; erst dann `P08 PASS A COMPLETE` und P08-SYN-Freigabe.
