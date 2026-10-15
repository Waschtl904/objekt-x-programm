# Vollständiger Antwortgram und verschärfter Modellfehlertransport für A9->A11

15. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. Integrationstext zum
versiegelten Autorenpaket; der kanonische Autorenbeweis ist `original/PROOF.txt`
(bytegleich mit dem gebundenen Archiv).

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
`scripts/replay_whole_response_gram.py` prüft Katalog, Archiv, Mitglieder und
sichtbare Kopien, entpackt außerhalb des Repositories, führt den versiegelten
`verify.py --output` aus und vergleicht die Quittung mit
`reports/EXPECTED_RECEIPT.json` (576 exakte Gram-Vergleiche, 48 positive
Pivots, alle Scope-Felder unverändert). Der vollständige F12/D12-Eingangsreplay
läuft nur mit `--full-input`.

## 2. Analytische Kette (nachgerechnet)

Die folgenden Identitäten des Autorenbeweises wurden unabhängig nachgerechnet:

```text
mu_even = a/2 + 2/3,  mu_odd = 2/3 - a/2            (sinh(log 3) = 4/3)
mu + nu = +-b/2 + 5/(2 sqrt 11)                      (sinh(log(11)/2) = 5/sqrt 11)
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
Modellfehler nicht.

## 3. Unabhängiger Gegencheck per Quadratur

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

Die Matrixordnung `TT*_W <= G_T` hält damit auch gegen eine andere
Rechenmethode in jeder Richtung. Ein Vorlauf mit nur 30 Stellen zeigte
`-1.4e-7` als kleinsten Eigenwert; das war Quadraturrauschen bei Einträgen
der Größe `1e13` und verschwindet bei höherer Präzision. Die Metrikschranke
`W <= g I` ist in einer Richtung bis auf `1e-15` ausgeschöpft.

## 4. Anmerkungen aus der Gegenprüfung

1. `response_norm.py` prüft `s < 1/10`, nicht die für `e_m` benötigte
   Bedingung `h < 101/1000`. Sie ist wahr (`h = 0.100335...`), sollte aber als
   Zusicherung im Code stehen.
2. Die Antwortmenge ist extrem schlecht konditioniert (Konditionszahl von
   `TT*_W` bis `1.3e25`). Die richtungsabhängige Form `tr(Q_D G_T)` ist
   deshalb nötig; jede skalare Ersetzung von `T` durch `||T||` verschenkt bis
   zu 25 Größenordnungen.
3. Kandidat `S` verwendet Mittelpunkte der Löwner-Schranken und ist keine
   zertifizierte Inverse; das steht im Autorentext und ist bei jeder
   Weiterverwendung mitzuführen.

## 5. Anschluss an die Spike-Kalibrierung

Nach `research/x-c1/a9-inverse-spike-calibration-2026-10-15/` (PR #226, zum Zeitpunkt dieses Pakets nicht integriert) trägt `W9`
auf der Basis84-Richtung `Jv` mindestens das Gewicht `(11/10) * 56620 ~ 6.2e4`
(gerade) bzw. `~ 1.0e4` (ungerade). Als Untergrenze für `w` eingesetzt, wird
der gewichtete Modellfehlerfaktor `5.9e-62 * 6.2e4 ~ 4e-57`. Die Modellfehler
sind damit für jede plausible `W9`-Norm irrelevant. Der gesamte offene
Betrag des Schritts liegt in der tatsächlichen Energie `R_hat* W9 R_hat` und
dort dominant im Skalar `<Jv, R_hat z>` je Parität. Dieses Paket enthält `Jv`
nicht; der Vortest ist eine eigene Aufgabe.

## 6. Ergebnisstatus

| Aussage | Status |
| --- | --- |
| `G_T >= TT*` (vier Obermatrizen, 48 Pivots) | Autorenresultat, versiegelter Replay bestanden, Quadratur-Gegencheck bestanden |
| direkte K-Modellfehler | Autorenresultat unter geerbten `delta_F`, `delta_A`, `delta_D` |
| Anschluss `tr(Q_D G_T)` | bewiesene Ungleichung, `Q_D` offen |
| `||W9||`, Modellenergie, A9->A11-Zertifikat | offen |
| externe mathematische Begutachtung | offen |
