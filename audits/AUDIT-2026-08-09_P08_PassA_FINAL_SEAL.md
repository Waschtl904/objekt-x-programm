# P08 Pass-A — FINAL SEAL

**Datum:** 9. August 2026  
**SYN-Ziel:** P08 — Grenzoperator + Renormierung  
**Scope:** gesamter Live-Bestand `04-grenzoperator-renormierung/` (NEU-121 bis NEU-150 gemaess Pass-A-Inventar).  
**Verfahren:** Primaerreconciliation H-T1 bis H-T5 + unabhaengiger Gesamtgegencheck + finale Versiegelung.

## 0. Finaler Status

\[
\boxed{\text{P08 PASS-A SEALED — H-T1 bis H-T5 reconciliiert; SYN-Migration ist prozedural freigegeben.}}
\]

P08 ist damit **noch nicht SYN FROZEN**. Der naechste Schritt darf die P08-SYN-Migration sein. Alle `?[O]`, `CONDITIONAL`, `x[M]` und Scope-Firewalls dieses Seals muessen dort sichtbar erhalten bleiben.

## 1. Kanonische Pass-A-Quellen

Bindend sind in dieser Reihenfolge:

1. `AUDIT-2026-08-09_P08_HT1_Moment_KMS_Herglotz.md`
2. `AUDIT-2026-08-09_P08_HT2_Jacobi_Grenzoperator.md`
3. `AUDIT-2026-08-09_P08_HT3_Prae_Lanczos_Grammetrik.md`
4. `AUDIT-2026-08-09_P08_HT4_Selbstenergie_Spur_Mangoldt.md`
5. `AUDIT-2026-08-09_P08_HT5_Cutoff_Mellin_Rueckbindung.md`
6. `AUDIT-2026-08-09_P08_PassA_Gesamtgegencheck_Pfadgebunden.md`
7. dieses FINAL-SEAL-Blatt.

Die Eröffnung `AUDIT-2026-08-09_P08_PassA_Eroeffnung_Inventar.md` bleibt Provenienz-/Inventarreferenz; ihr damaliger Status „Primärreconciliation ausständig“ ist durch diesen Seal superseded.

Keine globale Zahl „Anzahl Fehler“ oder „Anzahl offene Punkte“ wird eingefroren. Massgeblich sind die einzelnen Statusmatrizen und die Root-Blocker unten.

## 2. H-T1 — Moment/KMS/Herglotz

Erhalten:

- korrigiert `C_xi=1+gamma_E/2-(1/2)log(4pi)`;
- GNS-Normalisierung `Omega_hat=Z^{-1/2}Omega_tau`;
- Dirichlet-Skala `Z_{1,N}^{-1}~1/log N`;
- `m_arith` Herglotz iff RH gemaess P07;
- geeignete lokal gleichmaessige Herglotz-Approximation `=> RH` als logische Implikation.

Gesperrt/superseded:

- alter C_xi-Zahlenwert;
- `Z^{+1/2}`-GNS-Normierung;
- historische Aussage `R_N~log N`;
- jede unbedingte Herglotz-/Spektralmasslesart des historischen `A_N^{Jac,-}`.

Offen bleiben insbesondere P1 KMS/GNS->Jacobi, P2 Formkompatibilitaet, konkrete selbstadjungierte Realisierung und kanonische Nevanlinna-Approximanten.

## 3. H-T2 — Jacobi-Grenzoperator / Renormierungsbarriere

Erhalten:

- endliche direkt symmetrische Jacobi-Schliessung `A_N^sym=B_N^Lambda` selbstadjungiert;
- abstraktes Jacobi/Core/Carleman-Resolventenschema;
- konkret `b_{1,N}~gamma sqrt(log N/N)->0`;
- Startvektor-Weylkanal kollabiert unrenormiert zu `-1/z`;
- skalare Lanczos-Kovarianz und abstraktes No-scalar-Lemma conditional auf `b2/b1->infinity`.

Gesperrt:

- positiver nichtdegenerierter erster Jacobi-Grenzparameter fuer die unrenormierte Folge;
- Schluss `b1->0 => gesamter Grenzoperator diagonal`;
- falsche historische Skalenprovenienzen.

Offen:

- `b2/b1->infinity` streng;
- eine intrinsische positive nichtskalare Prae-Lanczos-Renormierung;
- NEU-124-Spektrum/Spektralmass/Grenzoperatoridentifikation.

**Firewall:** Die Doppelbarriere diagnostiziert einen Bedarf; sie konstruiert kein `W_N`.

## 4. H-T3 — Prae-Lanczos-/Grammetrik

Erhalten:

- NEU-127 als Triage;
- Jacobi-seitige Self-Energy ist noch keine Prae-Lanczos-Metrik;
- feste positive beta-Gewichte als Modellvoraussetzung;
- PSWF nur als Methodenheuristik.

Gesperrt:

- historischer gewichteter Rang-1-Operator als „Projektor“;
- Operator/Skalar-Formel in NEU-128b;
- Paper-VII-Skalierung `A=P c^(1/2)` als H3-Nachweis;
- Phasencancellation `=>` absolute Schur-Zeilensumme.

**P05-Firewall:** Rang `<=1` gilt nur in der induzierten relativen Modellrealisierung. Globaler Rang-eins-, Liftunabhaengigkeits- oder Nichtentartungssatz wird nicht importiert.

## 5. H-T4 — Selbstenergie / Spurklasse / Mangoldt

Erhalten:

\[
\Sigma_{rel}=\Sigma_{rel}^{\infty}+\Sigma_{rel}^{ren}(\beta)
\]

als algebraische beta-Zerlegung.

Unter

- modellrelativ `rank C_p^rel<=1`, und
- quantitativ `|c_p|^2=O((log p)^2/p)`

folgt fuer festes `beta>0`

\[
\Sigma_{rel}^{ren}(\beta)\in S_1
\]

`CONDITIONAL check[M]_{model}`.

Wichtig: T2 und `c_p!=0` sind **nicht** Voraussetzungen dieses reinen S1-Schritts.

Gesperrt:

- Primeclock-H1/Abel-Schranke aus NEU-132/133;
- `sum_{p<=N}(log p)^2/p ~(log N)^3/3` (korrekt ist `(log N)^2/2`);
- Rohdivergenz allein aus Upper Bound;
- allgemeine Gleichsetzung der S1-Norm mit Operatornormquadrat ausserhalb Rang 1;
- primeweise Eigenwert-/Eulerproduktlesart ohne T2;
- falsche zweite-Spur-Formel in NEU-139.

Offen/conditional:

- quantitative `c_p`-Kontrolle intrinsisch;
- intrinsisches T2;
- `c_p!=0` fuer alle relevanten Primkanaele;
- primdiagonales Mangoldt-`R`;
- operatorielle Finite-Part-Realisierung.

**Rohanteil-Firewall:** Ueber `Sigma_rel^infty` wird weder Divergenz noch Nicht-Regularisierbarkeit aus den vorhandenen Bounds behauptet.

## 6. H-T5 — Cutoff / Mellin / Rueckbindung

### 6.1 Exakter analytischer Kern

Das korrekte Mellin-Objekt ist

\[
\Psi_{\varphi,X}(\beta)=\sum_n\Lambda(n)\varphi(n/X)n^{-\beta},
\]

mit

\[
\Psi_{\varphi,X}(\beta)=\frac1{2\pi i}\int_{(c)}\widehat\varphi(s)X^s\left(-\frac{\zeta'}{\zeta}(\beta+s)\right)ds.
\]

Bei `varphi=1` nahe 0 gilt

\[
Res_{s=0}\widehat\varphi(s)=1,
\]

nicht `hat varphi(0)=1`.

### 6.2 Gesperrte Prime-only-Schritte

Nicht migrieren:

- direkte Mellin-Identitaet fuer `S_{varphi,X}` mit Cutoff `varphi(p/X)`;
- Identifikation `theta=psi` in der Prime-only-Explizitformel;
- Live-Differenzformel `Psi-S` aus NEU-148.6;
- daraus abgeleitete unbedingte Primlabel-Finite-Part-/Operatorrealisierung.

Korrekt ist

\[
\Psi_{\varphi,X}-S_{\varphi,X}
=\sum_{k\ge2}\sum_p\log p\,[\varphi(p^k/X)-\varphi(p/X)]p^{-k\beta}.
\]

### 6.3 Offene analytische/operatorielle Schritte

- uniforme nullstellenvermeidende Kontur + vollstaendige Residuenzahlung fuer `Psi`: `?[O]`;
- fixed-contour Restlemma fuer `Psi`: `CONDITIONAL check[M]`;
- `Psi-S->0` fuer `Re beta>1/2`: `?[O]` quantitativ;
- Primlabel-Observable `N_P`: `CONDITIONAL`, mit maximaler Domaene und Normfaktoren zu typisieren;
- Primlabel-Spurformel: `CONDITIONAL check[M]_{model}`;
- Primlabel-Finite-Part `=-zeta'/zeta`: `?[O]`;
- operatorielle Realisierung von `Tr_reg`: `?[O]`;
- R-Cutoff-Transfer: `?[O]`, benoetigt mehr als `[ZA] R_p asymp p/log p`.

`Tr_reg := AC[-zeta'/zeta]` bleibt ausschliesslich `check[def]`.

## 7. Zwei getrennte P08-Stränge

### Strang A — Renormierungsdiagnose

\[
b_{1,N}->0\quad check[M]
\]

plus starke finite Evidenz fuer `b2/b1`, aber strenger Grenzwert `?[O]`.

Falls `b2/b1->infinity`, greift das abstrakte skalare No-go-Lemma. Eine positive nichtskalare Prae-Lanczos-Geometrie `W_N` bleibt Kandidat `?[O]`; ihre Existenz folgt nicht aus der Barriere.

### Strang B — Mangoldt/Mellin-Operatorbruecke

1. modellrelative Rangstruktur + quantitative c_p-Obergrenze -> feste-beta S1 conditional;
2. T2 + Nichtentartung -> primdiagonales `R` conditional;
3. exakte `Psi`-Mellin-Analyse -> analytischer Finite-Part-Pfad;
4. `Psi/S`-Transfer -> Prime-only-Pfad;
5. Operator-/Primlabel-Bruecke -> operatorielle Regularisierung;
6. separater, staerkerer Vergleich -> R-Cutoff.

Keine Stufe darf durch die Definitionsgleichung `Tr_reg:=AC[-zeta'/zeta]` ersetzt werden.

## 8. Root-Blocker fuer P08-SYN

P08-SYN muss mindestens sichtbar tragen:

- H-T1: P1/P2 und selbstadjungierte konkrete GNS/Jacobi-Realisierung;
- H-T2: `b2/b1->infinity` streng und `W_N`;
- P05/H-T3: intrinsische Lift-/Gramgeometrie;
- H-T4: quantitative `c_p`-Kontrolle, T2, Nichtentartung, Mangoldt-`R`;
- H-T5: uniforme Kontur/Residuen, `Psi/S`-Transfer, operatorielle Primlabel-Bruecke, R-Cutoff-Transfer.

Diese Punkte duerfen in SYN offen bleiben; ihre Loesung ist **keine Voraussetzung fuer die Migration**, sofern der Status korrekt markiert wird.

## 9. SYN-Migrationsfreigabe

Die drei im Eröffnungsblatt verlangten Bedingungen sind nun erfuellt:

1. Primaerreconciliation: H-T1 bis H-T5 `COMPLETE`;
2. unabhaengiger Gesamtgegencheck: `RECONCILED`;
3. finaler Pass-A-Seal: dieses Blatt.

Damit gilt:

\[
\boxed{\text{P08 SYN-MIGRATION FREIGEGEBEN — noch nicht ausgefuehrt.}}
\]

Bei der Migration gilt strikt:

- nur heutiger korrigierter Endstand;
- keine historischen `x[M]`-Behauptungen als positive Ergebnisse;
- `CONDITIONAL` und `?[O]` explizit;
- keine Identifikation des historischen direkten Jacobi-Limes mit einem Hilbert-Pólya-Endoperator;
- keine Behauptung eines RH-Beweises oder eines konstruierten Objekt X.
