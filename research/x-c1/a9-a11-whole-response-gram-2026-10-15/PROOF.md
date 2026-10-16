# Vollständiger Antwortgram und verschärfter Modellfehlertransport für A9->A11

15./16. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. Integrationstext zum
versiegelten Autorenpaket und seinem Nachtrag; der kanonische Autorenbeweis ist
`original/PROOF.txt`, die verbindlichen Klarstellungen stehen in
`original/nachtrag/NACHTRAG.txt` (beide bytegleich mit den gebundenen Archiven).

**Korrekturvermerk (16. Oktober).** Die erste Fassung dieses Textes enthielt in
Abschnitt 5 drei unbegründete Folgerungen: (i) eine Untergrenze für `||W9||` wurde
in die obere Fehlerrechnung `k * w` eingesetzt und daraus „~4e-57, Modellfehler
irrelevant" geschlossen; (ii) die Rang-eins-Obermatrix von `P_upper` wurde als
unteres Gewicht der vollen `W9` auf dem rohen Vektor `Jv` und als Dominanz eines
Skalars gelesen; (iii) daraus wurde ein voraussichtliches Scheitern der
eingefrorenen N12-Regel gefolgert. Alle drei sind zurückgenommen; der korrekte
Anschluss steht jetzt in Abschnitt 5. Der Fehler lag im Integrationstext,
nicht im Autorenpaket.

## 0. Scope

Das Autorenpaket zertifiziert unter den geerbten Operator-, Domänen- und
Integrationsvoraussetzungen des A9->A11-Arbeitsauftrags
(`research/x-c1/a9-a11-certificate-calibration-2026-10-15/WORK_ORDER.md`):

1. Vier rationale 12x12-Obermatrizen `G_T >= T T*` für die vollständigen
   zusammengesetzten Antwortfunktionen `T = X F_hat` in der physischen
   `W`-Metrik der ganzen Schale `(a, b)`, `a = log 3`, `b = log(11)/2`,
   einschließlich logarithmischem Rand und aller Approximationsfehler,
   für beide Paritäten und beide Antwortkandidaten (`X` eingefroren, `S` nur
   Nebenprüfung).
2. Direkte K-Modellfehlerpreise `2 delta_F sqrt(tr G_T) + delta_A tr G_T`.
3. Einen richtungsabhängigen Anschluss `||(R - R_hat)* W9 (R - R_hat)|| <= tr(Q_D G_T)`
   für eine später zu zertifizierende Fehlermatrix `Q_D >= (D - D_hat)* W9 (D - D_hat)`.

| | gerade | ungerade |
| --- | --- | --- |
| `||T|| <= sqrt(tr G_T)` | `< 6 838 544` | `< 784 134` |
| direkter K-Modellfehler | `< 1.661e-24` | `< 2.183e-26` |
| gewichteter Fehlerfaktor je Einheit `w >= ||W9||` | `< 5.90e-62` | `< 7.75e-64` |

Nicht zertifiziert und im Paket selbst so geführt: `||W9||`, `Q_D`, die
Modellenergie `R_hat* W9 R_hat`, der kompakte Gate einschließlich `-Pi0`,
das erneuerbare A9->A11-Zertifikat, Kofinalität, Readout, Objekt X.

## 1. Bindung

Archiv `archives/Objekt-X-Vollstaendiger-Antwortgram-und-Scharfer-Modellfehler-2026-10-15.zip`,
SHA-256 `b8677c0bb085f40052e52953ec39112894fbaa0f9f5d9997df8ae546238f41ee`,
33 Mitglieder (`SOURCE_BINDINGS.json`). Darin gebunden: das Funktionsarchiv
F12/D12 (`0a7bda3d...10d3d3`) und die eingefrorene Antwortregel
`FROZEN_RESPONSE12.json` (`132959da...1426a`, Regel `N12-MIDPOINT-INVERSE-60-v1`).
Die eingefrorene Regel trägt `rule_id A9_A11_N12_MIDPOINT_INVERSE_60_V1`
(symmetrische, eintragsweise nächste 60-stellige Inverse der frischen
A12-Mittelpunktmatrix); `fixed_X` in den Gram-Dateien ist genau diese Matrix.
`audit_S` (Mittel zweier gerichteter Invershüllen) ist ein getrennter
rationaler Kandidat und keine Inverse; seine Grame und Fehlerpreise gelten nur
für ihn.

Nachtrag `archives/Objekt-X-Antwortgram-Nachtrag-Breitenpruefung-und-W9-Klarstellung-2026-10-15.zip`,
SHA-256 `00a66e8584062b8057264b9b0dda48f89a013dc9b3756241a770bb74f2ded0a0`. Er
bettet das unveränderte Original ein, fügt in einer frischen Arbeitskopie genau
eine Zeile `need(h.high < Q(101,1000))` ein (`response_norm.py`
`98d1b655… -> 81c2e937…`), bindet eine unabhängige elementare Einschließung
`h = atanh(1/10) < 1/10 + 1/2970 < 101/1000` und baut alle vier Antwortgrame
neu auf; `RESPONSE_ENERGY.json` und `RESPONSE_CHECK.json` bleiben bytegleich.

`scripts/replay_whole_response_gram.py` prüft Katalog, beide Archive,
Mitglieder und sichtbare Kopien, entpackt außerhalb des Repositories, führt den
versiegelten `verify.py --output` des Originals und den Nachtragsprüfer aus,
vergleicht beide Quittungen mit `reports/EXPECTED_RECEIPT.json` bzw.
`reports/EXPECTED_ADDENDUM_RECEIPT.json` (576 exakte Gram-Vergleiche, 48
positive Pivots, Scope-Felder nicht promovierbar) und prüft die
paritätsabhängigen Metrikkonstanten in rationalen Einschließungen. Der
vollständige F12/D12-Eingangsreplay läuft nur mit `--full-input`.

## 2. Analytische Kette (nachgerechnet)

Die folgenden Identitäten des Autorenbeweises wurden unabhängig nachgerechnet:

```text
gerade:    m = cosh(x/2),  mu = a/2 + 2/3,       mu + nu =  b/2 + 5/(2 sqrt 11),  g = 1.11289...
ungerade:  m = sinh(x/2),  mu = 2/3 - a/2,       mu + nu = -b/2 + 5/(2 sqrt 11),  g = 1.31479...
           (aus cosh^2(x/2) = (cosh x + 1)/2, sinh^2(x/2) = (cosh x - 1)/2, sinh(log 3) = 4/3, sinh(log(11)/2) = 5/sqrt 11)
||W|| = 1 + ||m||_X^2/(2 mu) = (mu + nu)/mu =: g      (W = I + (m (x) m)/(2 mu) auf X)
v = y/a = 1 + s u,  s = h/a,  h = b - a = 0.10034 < 101/1000
log((v+1)/(v-1)) = -log u + log(2/s) + log(1 + (s/2) u),  Rest <= x^121/(121(1-x)), x <= s/2
cosh((a+hu)/2) = (2/sqrt 3) cosh(hu/2) + (1/sqrt 3) sinh(hu/2)   (e^{a/2} = sqrt 3; odd: vertauscht)
||u^k log u||_2 = sqrt 2 /(2k+1)^{3/2} < 2
||t||_X^2 = 2 int_a^b |b(u(y))|^2/(2a) dy = s int_0^1 |b|^2 du
TT*_W <= g TT*_X <= s g (G_0 + rho I),   rho = 2 sqrt(tr G_0) sqrt(sum eps_i^2) + sum eps_i^2
K_P >= K_hat - [2 delta_F sqrt(tr G_T) + delta_A tr G_T] I
tr(Q_D T T*) <= tr(Q_D G_T)  für Q_D >= 0
```

Alle Schritte sind korrekt; `rho` folgt aus Cauchy-Schwarz, die Maßumrechnung
ergibt exakt `s`, die exakte Momentprojektion `Pi_a` ist eine
Orthogonalprojektion in `L^2(0,a)` (Faktor 2 kürzt sich) und vergrößert den
Modellfehler nicht. Beide Paritätsvarianten werden im Replay getrennt als
rationale Einschließungen von `g` kontrolliert.

## 3. Numerische Plausibilisierung per Quadratur (kein zusätzlicher Beweis)

`independent_quadrature_check.py` (mpmath, nicht CI) integriert die zwölf
zusammengesetzten Antwortfunktionen direkt mit exaktem Logarithmus statt
über Reihen: gradiertes Gauss-Legendre, 40 Punkte je Panel, dyadische Panels
bis `2^-150` an den logarithmischen Rand, 55 Stellen. Ergebnis
(`reports/INDEPENDENT_QUADRATURE.json`):

| | gerade | ungerade |
| --- | --- | --- |
| rel. Abweichung X-Gram numerisch vs. `s G_0` | `1.1e-38` | `3.3e-37` |
| kleinster Eigenwert von `G_T - TT*_W` (numerisch) | `+9.3e-15` | `+1.5e-16` |
| `||T||_W` numerisch | `6 483 792` | `684 744` |
| `sqrt(tr G_T)` zertifiziert | `6 838 543` | `784 133` |
| Eigenwerte von `TT*_W` | `3.2e-12 ... 4.2e13` | `1.5e-11 ... 4.7e11` |
| Konditionszahl von `TT*_W` | `1.3e25` | `3.1e22` |

Einstufung: unabhängige hochpräzise numerische Plausibilisierung. Der Lauf
führt keine zertifizierten Quadratur-, Rundungs- und Eigenwertfehler mit; ein
positiver numerischer kleinster Eigenwert beweist die Ordnung der exakten
Gram-Matrix daher nicht. Der rigorose Nachweis von `TT*_W <= G_T` bleibt die
rationale Rechnung mit vollständigen analytischen Resten im Originalpaket.
Ein Vorlauf mit 30 Stellen zeigte `-1.4e-7` als kleinsten Eigenwert; das
Verschwinden bei höherer Präzision ist mit Quadraturrauschen verträglich, ohne
Fehlereinschließung aber nicht als dessen Nachweis zu lesen. Für einen
zusätzlichen gerichteten Nachweis wären `||G_exakt - G_quad|| <= eps_quad` und
eine verifizierte Schranke `lambda_min(G_T - G_quad) > eps_quad` nötig.

## 4. Anmerkungen aus der Gegenprüfung

1. Das Original prüfte `s < 1/10`, nicht die für `e_m` benötigte Bedingung
   `h < 101/1000`; aus `s < 1/10` folgt sie nicht. Der Nachtrag ergänzt die
   Zusicherung in einer gebundenen Arbeitskopie und bestätigt sie unabhängig
   über `h = atanh(1/10)`; die Ergebnisdateien bleiben bytegleich.
2. Die numerisch gemeldete spektrale Spannweite von `TT*_W` (bis `1.3e25`)
   motiviert die richtungsabhängige Schnittstelle `tr(Q_D G_T)`. Wie viel eine
   skalare Ersetzung tatsächlich verliert, hängt von der Ausrichtung des noch
   unbekannten `Q_D` ab und ist weder zwingend noch gemessen.
3. `audit_S` ist ein rationaler Antwortkandidat (Mittel der Invershüllen), keine
   Inverse; aus `L_inv <= A^-1 <= U_inv` folgt nicht `(L_inv + U_inv)/2 = A^-1`.
   Ergebnisse eines Kandidaten dürfen nicht unter dem Namen des anderen
   weiterverwendet werden.

## 5. Korrekter Anschluss an `W9` und die Spike-Kalibrierung

**5a. Keine bezahlte gewichtete Fehlerenergie.** Die Werte `5.90e-62` und
`7.75e-64` sind Koeffizienten `k` in `Fehlerenergie <= k w` unter der
Voraussetzung `w >= ||W9||`. Eine Untergrenze für `||W9||` darf dort nicht
eingesetzt werden: Aus `||W9|| >= w_0` folgt keine obere Fehlerschranke
`k w_0`. Exaktes Gegenmodell (im Nachtragsprüfer kontrolliert): Fehleroperator
der Norm `1e-31`, `W = 1e100 I`, Energie `1e38`, obwohl `||W|| >= 62282` wahr
ist. Die gewichtete Fehlerfreigabe braucht eine obere Normschranke oder eine
nachgewiesene Matrix `Q_D >= DeltaD* W9 DeltaD`; dann gilt

```text
||(R - R_hat)* W9 (R - R_hat)|| <= ||T* Q_D T|| <= tr(Q_D T T*) <= tr(Q_D G_T),
R* W9 R <= (1 + theta) R_hat* W9 R_hat + (1 + theta^-1) T* Q_D T     (theta > 0).
```

Die Felder `W9_norm_certified`, `Q_D_certified`,
`whole_W9_residual_energy_certified` bleiben `false`.

**5b. Der ausgezeichnete Skalar verwendet die Quellentransformation `N`.** Nach
A9-HERLEITUNG §6 hat die vollständige Majorante die Struktur

```text
f8  = J_old* f,
v12 = F* f - g_F* U8 f8,
nu  = N f = Lambda_T* f - g* U8 f8 - a_fin* K^-1 v12,
<f, W9 f> = <f8, U8 f8> + v12* K^-1 v12
          + (11/10) [ beta^-1 <nu, R_L nu> + (J* nu)* P_upper (J* nu) ].
```

Die Rang-eins-Obermatrix `P_upper <= mu v v* + eps I` aus
`research/x-c1/a9-inverse-spike-calibration-2026-10-15/` (PR #226) betrifft nur
den letzten Summanden und nur als obere Hülle. Sie liefert weder ein unteres
Gewicht der vollen `W9` auf dem rohen Vektor `Jv` noch die Dominanz eines
Skalars für die tatsächlich vorkommenden Residuen. Der passende obere
Diagnoseskalar ist `<Jv, N R_hat z>_W_X`, also die Prüfquelle `psi = N* J v`;
die Energien `<f8, U8 f8>` und `v12* K^-1 v12` bleiben zusätzlich zu bezahlen.
Das bloße Zusammenführen der Basis84-Funktionen mit `R_hat` auf `(0, a)`
reicht nicht.

**5c. Gültiger unterer Ausschlusstest.** Für `P = P_upper > 0` gilt
`P >= (Pv)(Pv)*/(v* P v)` (Cauchy-Schwarz in der `P`-Metrik). Mit
`p = P_upper v`, `q = v* P_upper v` und `chi = N* J p` folgt

```text
<f, W9 f> >= (11/10) |<J p, N f>|^2 / q,
R* W9 R   >= (11/10) (chi* R)* (chi* R) / q .
```

Übersteigt eine rigorose Untergrenze dieses Ausdrucks auf einem zulässigen `z`
eine rigorose Obergrenze von `K_P[z]`, ist der konkrete Vergleich
`K_P - R* W9 R` negativ: `CERTIFICATE_FAIL` dieses Vergleichs, nicht der
tatsächlichen A11-Form. Bei Auswertung über `R_hat` sind die Modellfehler im
Skalar mitzuführen. Eine überschrittene obere Spikehülle liefert diesen
Ausschluss nicht. Die endlichen Daten `p`, `q` liegen nach `NACHTRAG.txt` im
Paket `Objekt-X-A9-Spike-Artefaktpruefung-und-Korrekter-W9-Anschluss-2026-10-15.zip`
(SHA-256 `7f7129945b38768a5ec88994b783211db1ceb0810129ffc4ea4ba7db5beb1f5e`);
dieses ist hier nur Anschlussverweis, nicht gebunden und nicht ausgeführt.

**5d. Keine Aussage über die eingefrorene N12-Regel.** Weder aus der
Antwortnorm noch aus der Spikehülle folgt ein Scheitern von
`A9_A11_N12_MIDPOINT_INVERSE_60_V1`. Der Status dieser Regel bleibt
`UNRESOLVED`, wie in `FROZEN_RESPONSE12.json` eingetragen.

## 6. Ergebnisstatus

| Aussage | Status |
| --- | --- |
| `G_T >= TT*` (vier Obermatrizen, 48 Pivots) | Autorenresultat, versiegelter Replay und Nachtragsreplay bestanden, numerische Plausibilisierung verträglich |
| Zusicherung `h < 101/1000` | im Nachtrag ergänzt und unabhängig eingeschlossen |
| Kandidatenbindung `fixed_X` = N12-Regel, `audit_S` getrennt | geklärt (rule_id, Hashes) |
| gewichtete Modellfehlerenergie | offen (`Q_D` oder obere `W9`-Norm nötig) |
| direkte K-Modellfehler | Autorenresultat unter geerbten `delta_F`, `delta_A`, `delta_D` |
| Anschluss `tr(Q_D G_T)` | bewiesene Ungleichung, `Q_D` offen |
| `||W9||`, Modellenergie, A9->A11-Zertifikat | offen |
| externe mathematische Begutachtung | offen |
