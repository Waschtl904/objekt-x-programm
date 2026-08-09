# P08 Pass-A — Gesamtgegencheck, pfadgebunden

**Datum:** 9. August 2026  
**Rolle:** unabhängiger Querschnittsentwurf gegen die kanonischen Live-Audits H-T1 bis H-T5.  
**Status:** `AUDIT-RECONCILED`; dieses Blatt ist nicht selbst der Seal.

## 1. Gesamturteil zum eingereichten Gegencheck

Der Gegencheck ist als Querschnitt nützlich und bestätigt die Hauptfirewalls aus H-T3 bis H-T5. Er ist jedoch nicht unverändert sealing-faehig. Mehrere globale Bilanz- und Implikationsaussagen werden korrigiert.

## 2. Korrektur: keine globale Fehler-/Offenpunktzahl einfrieren

Die im Gegencheck genannte Bilanz `16 x[M]` / `11 ?[O]` ist nicht kanonisch.

Grund: Die dortige x[M]-Uebersicht beginnt praktisch erst bei H-T3. H-T1 enthaelt bereits eigene Sperren (historischer C_xi-Zahlenwert, falsche GNS-Normierung, verkehrte R_N~log N-Aussage). H-T2 enthaelt weitere Sperren (u.a. konkrete unrenormierte positive erste Jacobi-Kante, globale Diagonalitaetsfolgerung, falsche Skalenprovenienz). Ebenso ist die offene Liste nicht vollstaendig, weil H-T1/H-T2 weitere eigenstaendige ?[O]-Punkte tragen.

**Bindende Regel:** P08-SYN uebernimmt Statusmatrizen und benannte Root-Blocker, keine globale Zaehlstatistik.

## 3. Korrektur der Renormierungslogik

Aus

`b_{1,N}->0` und `b_{2,N}/b_{1,N}->infinity`

folgt nicht die Existenz eines positiven nichtskalaren Prae-Lanczos-Operators `W_N`. Der zweite Grenzwert ist zudem streng offen.

Bindend ist nur:

- `b_{1,N}->0`: `check[M]`;
- `b2/b1->infinity`: `?[O]` mit starker finiter Numerik;
- falls `b2/b1->infinity`, scheitert eine einzige positive skalare Renormierung an beiden Kanten: abstraktes Lemma `check[M]`, konkrete Anwendung conditional;
- `W_N`: offener Kandidat `?[O]`, keine Folgerung aus der Doppelbarriere.

## 4. Korrektur der Spurklassen-Voraussetzungen

Die feste-beta-Aussage

`Sigma_rel^ren(beta) in S_1`

benoetigt im H-T4-Modell:

1. `rank C_p^rel <= 1` im induzierten P05-Modell;
2. die quantitative Schranke `|c_p|^2=O((log p)^2/p)`.

Dann folgt fuer festes `beta>0` die absolute S1-Konvergenz conditional/model-relative.

**Nicht erforderlich fuer diesen reinen S1-Schritt:** T2 und `c_p!=0`.

T2 und Nichtentartung werden erst fuer die primdiagonale Mangoldt-Observable

`R_p=log p/|c_p|^2`

und die entsprechende primweise Operatorrechnung benoetigt.

## 5. Korrektur der Sigma-infinity-Firewall

Die Aussage `Sigma_rel^infty ist kein regulierbarer Summand` ist nicht bewiesen und wird nicht eingefroren.

Bindend ist nur:

- die algebraische Zerlegung `Sigma_rel=Sigma_rel^infty+Sigma_rel^ren(beta)` ist korrekt;
- aus der vorhandenen Upper-Bound-Kontrolle folgt keine Divergenz von `Sigma_rel^infty`;
- daher duerfen weder Divergenzgrad noch Finite-Part-/Nichtregularisierbarkeitsaussagen fuer den Rohanteil importiert werden.

## 6. Korrektur: analytischer und operatorieller Strang getrennt

### Analytischer Strang

Exaktes Mellin-Objekt ist

`Psi_{phi,X}(beta)=sum_n Lambda(n) phi(n/X)n^{-beta}`,

nicht die Prime-only-Summe mit `phi(p/X)` im Eulerfaktor.

Bindend:

- Psi-Mellin-Identitaet: `check[M]`;
- `Res_{s=0} hat phi(s)=1`: `check[M]`;
- fixed-contour Restlemma fuer Psi: `CONDITIONAL check[M]`;
- uniforme nullstellenvermeidende Kontur + vollstaendige Residuenzahlung: `?[O]`;
- korrekter Transfer `Psi-S ->0` fuer `Re beta>1/2`: `?[O]` quantitativ.

### Operatorstrang

Separat erforderlich:

- intrinsisches T2/direct-sum typing: `?[O]`;
- `c_p!=0` fuer relevante Primkanaele: `?[O]`;
- maximale Domaenen von `R` und `N_P` mit Normfaktoren: offen/conditional;
- Primlabel-Spurformel: `CONDITIONAL check[M]_{model}`;
- Identifikation des Primlabel-Finite-Parts mit `-zeta'/zeta`: `?[O]`;
- Transfer zum R-Cutoff: `?[O]`, benoetigt mehr als bloss `R_p asymp p/log p`.

## 7. Root-Blocker statt unvollstaendiger Gesamtzaehlung

Fuer das Seal werden mindestens folgende Root-Klassen getrennt gefuehrt:

- H-T1: konkrete selbstadjungierte KMS/GNS-Jacobi-Bruecke P1; Formkompatibilitaet P2; kanonische Herglotz/Nevanlinna-Approximanten;
- H-T2: strenge Divergenz `b2/b1`; nichtskalare Prae-Lanczos-Renormierung; gesperrter Spektralmass-/Grenzoperatorpfad NEU-124;
- H-T3/P05: intrinsische Lift-/Gramgeometrie und `W_N`;
- H-T4: quantitative c_p-Kontrolle, intrinsisches T2, Nichtentartung, primdiagonales Mangoldt-R;
- H-T5: uniforme Kontur/Residuen, Psi/S-Transfer, operatorielle Primlabel-Bruecke, R-Cutoff-Transfer.

## 8. SYN-Migrationsregel

Die offenen Punkte `c_p!=0` und T2 sind mathematisch zentrale Root-Blocker, muessen aber **nicht vor der SYN-Migration geloest** werden. Nach einem finalen Pass-A-Seal darf P08-SYN migriert werden, sofern diese Punkte sichtbar als `?[O]`/`CONDITIONAL` getragen und keine historischen Hochstufungen importiert werden.

## 9. Endurteil

`P08 GESAMTGEGENCHECK RECONCILED — sealing-faehig nach den obigen Korrekturen.`
