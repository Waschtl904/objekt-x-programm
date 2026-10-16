# A9-Inversspektrum: Ein-Richtungs-Verstärkung und Kalibrierung der Zertifikatsklasse

15./16. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. Art: DIAGNOSTIK
mit exakten rationalen Zertifikaten.

**Korrekturvermerk (16. Oktober).** Die erste Fassung las die hier bewiesene
obere Hülle von `H_*^-1` auf `T` in Abschnitt 4 und 5 als Aussage über die
volle Majorante `W9` auf dem rohen Vektor `Jv`, folgerte daraus die Dominanz
des Skalars `<Jv, R z>` im Residualpreis, ein voraussichtliches
`CERTIFICATE_FAIL` der eingefrorenen N12-Regel und eine zwingende Vererbung
von `C_spike` an spätere Horizonte. Diese Folgerungen sind zurückgenommen. Die
exakten Zertifikate (Sätze 1 und 2) und das Korollar über `H_*^-1` auf `T`
(Abschnitt 4) sind unverändert; Abschnitt 5 ist neu gefasst.

## 0. Zweck und Nichtanspruch

Das Reduktionspaket `renewal-reduction-and-obstructions-2026-10-15` macht
die Erneuerungsfrage an einer Hypothese `H_n` fest, deren Uniformitätsteil
(H3) verlangt, dass die physische Inverskonstante `C` entlang der Kette
beschränkt bleibt. Dieses Paket kalibriert diese Konstante am einzigen
bisher geschlossenen Schritt A8->A9 anhand der im Repository gebundenen
Originaldaten des A9-Inverspakets. Ergebnis: Die gesamte „schwierige
endliche Verstärkung" der A9-Inversen sitzt je Parität in **genau einer
Richtung**; außerhalb dieser Richtung ist die Konstante von Ordnung eins.
Die Richtung entspricht einer gerichteten Budgetlücke von Größenordnung
`10^-19` bzw. `10^-18`.

Nicht behauptet werden: eine neue A9-Eigenschaft (alle A9-Schranken
bleiben unverändert), eine A11-Aussage, ein Beweis von `H_9`, eine Deutung
der Fast-Nullrichtung als echte Kritikalität oder als Artefakt. Die
analytischen Voraussetzungen des A9-Pakets werden übernommen, nicht geprüft.

## 1. Eingaben

Archiv `research/x-c1/a9-inverse-renewal-2026-10-13/archives/Objekt-X-A9-Inverserneuerung-und-Hoher-Schurrest-2026-10-13.zip`,
SHA-256 `a1fa41958d79ab16a7c42b12375c3373f5a86a99993ae2d23c984ff6b3b2e8ae`,
Mitglieder `INVERSE_EVEN.json`, `INVERSE_ODD.json`. Daraus je Parität:

- `P_upper_rational`: symmetrische rationale 84x84-Matrix, im A9-Paket als
  `P = X_ans E^-1 X_ans*` plus Diagonalpolster `10^-40` definiert.
- `E_rational`: symmetrische rationale 203x203-Matrix, dort als
  `D203 - M_upper` (gerichtete Budgetlücke der 203 nicht gefitteten
  Funktionale) definiert; ihre Positivität ist im A9-Paket durch
  574 positive LDL-Pivots belegt.
- `beta = 20209999981781/182190000000000`.

Aus `HERLEITUNG.txt` des A9-Pakets werden ohne Nachprüfung übernommen:

```text
(1.1)  I <= J* W_X J < 1.000502 I                 (J: feste 84-Spalte auf T)
(2.4)  H_*^-1 <= (11/10) [ beta^-1 R_L + J P J* ]
(3.3)  R_L <= (5/21) I,   ||H_*^-1|| <= (11/10)[5/(21 beta) + 1.000502 tr P]
```

mit den dortigen Metrikkonventionen (`W_X` auf `T`). Alle unten
zertifizierten Aussagen betreffen ausschließlich die gespeicherten
endlichen Matrizen; Abschnitt 4 kombiniert sie mit (1.1)-(3.3) bedingt.

## 2. Satz 1: Rang-eins-Zerlegung von `P_upper` (exakt zertifiziert)

Die Datei `WITNESSES.json` enthält je Parität rationale Vektoren
`v_hat` (84), `w_orth` (84), `u_E_min` (203), `u_E_second` (203) sowie
Konstanten. `verify.py` beweist exakt rational:

```text
gerade:    P_upper <= 56620 * v v^T + (21/10) * I
ungerade:  P_upper <=  9373 * v v^T + (37/100) * I
```

jeweils durch Kongruenz-Trägheit `(0, 0, 84)` der Differenzmatrix
(84 positive Pivots). Die Konstanten sind scharf bis auf die vierte
Stelle:

```text
v^T P v / |v|^2  =  56619.81...   (gerade)      9372.43...   (ungerade)
w ⊥ v exakt,  w^T P w / |w|^2  =  2.0448...    (gerade)      0.35163...  (ungerade)
```

Folglich hat `P_upper` genau einen Eigenwert oberhalb `2.1` bzw. `0.37`;
dieser trägt `99.996 %` der Spur (`56619.8 / 56622.0` bzw.
`9372.4 / 9372.9`). Die Spurschranke des A9-Pakets ist also nicht grob,
sondern durch eine einzige Richtung ausgeschöpft.

Beobachtung (nicht zertifiziert): Die Komponenten von `v_hat` liegen in
beiden Paritäten nahezu identisch bei `0.559, 0.419, 0.331, 0.271, 0.227,
0.194, 0.168, ...` auf den Indizes `0, 2, 4, 6, 8, 10, 12, ...` der
Basis84-Ordnung. Die Richtung ist strukturell, nicht paritätsspezifisch. Die Spuraussage
betrifft die gespeicherte endliche Matrix `P_upper`, nicht die Verteilung der
physischen Inversenergie auf tatsächlich vorkommende Residuen.

## 3. Satz 2: Ursprung in einer fast verschwindenden Budgetlücke (exakt zertifiziert)

```text
gerade:    u^T E u / |u|^2  <=  4.2 * 10^-19,     zweite Richtung  <=  3.3 * 10^-12
ungerade:  u^T E u / |u|^2  <=  8.3 * 10^-18,     zweite Richtung  <=  3.3 * 10^-11
```

bei maximalem Diagonaleintrag von `E` nahe `1`. Da `E > 0` (A9-Paket),
ist `lambda_min(E)` positiv, aber höchstens von dieser Größe. Konditionszahl
(Korrektur 16. Oktober: die erste Fassung schrieb pauschal „übersteigt
`10^18`"): gerade über `2 * 10^18`; ungerade nach der vollständigen
Einschließung des Budgetpakets `1.206 * 10^17 < cond_2(E_odd) < 1.2625 * 10^17`. Numerisch (nicht zertifiziert,
Kontext in `WITNESSES.json`) liefert die Richtung `u` den Anteil
`|X_ans u|^2 / lambda_min = 56573` an der Spur `56622` von `P` (gerade)
bzw. `9364` von `9373` (ungerade); die zweite Richtung liefert `48` bzw.
`8.7`, alle weiteren zusammen unter `1`.

Die Verstärkung der A9-Inversen ist also kein diffuser Effekt vieler
Antwortrichtungen, sondern die Spiegelung genau einer Richtung, in der die
gerichtete Budgetlücke `D203 - M_upper` praktisch null ist.

## 4. Korollar: Kalibrierung der Inverskonstante (bedingt auf (1.1)-(3.3))

Für `f` in `T` gilt mit Satz 1 und `J* f` in Basis84-Koordinaten

```text
<f, J P J* f> = (J* f)^T P (J* f)
             <= mu |<J v, f>_W_X|^2 + eps |J* f|^2
             <= mu |<J v, f>_W_X|^2 + 1.000502 eps ||f||_W_X^2 .
```

Eingesetzt in (2.4) mit `R_L <= (5/21) I`:

```text
<f, H_*^-1 f> <= K_off * ||f||_W_X^2 + (11/10) mu |<J v, f>_W_X|^2,

K_off = (11/10) [ 5/(21 beta) + 1.000502 eps ]
      = 4.672...  (gerade)      2.768...  (ungerade),

(11/10) mu = 62282  (gerade)   10310.3  (ungerade).
```

Zum Vergleich reproduziert dieselbe Rechnung mit `tr P` statt `eps` die
globale Schranke (3.3): `62317.8 < 65000` bzw. `10317.7 < 11000`.

Damit gilt auf dem `W_X`-orthogonalen Komplement **eines einzigen
Vektors** `J v` je Parität

```text
H_*  >=  W_X / 4.68   (gerade),        H_*  >=  W_X / 2.77   (ungerade),
```

gegenüber `W_X / 65000` bzw. `W_X / 11000` auf ganz `T`. Das Verhältnis
beträgt `13338` bzw. `3727`.

In der Sprache des Reduktionspakets: Der Anteil `H_*^-1` der A9-Majorante hat
auf `T`, relativ zur Metrik `W_X`, eine obere Hülle der Gestalt

```text
H_*^-1  <=  C_off * W_X^-1  +  C_spike * (J v)(J v)^*,
C_off ~ 4.7 / 2.8,   C_spike ~ 6.2 * 10^4 / 1.0 * 10^4 .
```

Das ist eine obere Hülle eines Summanden; weder ein unteres Gewicht noch eine
Aussage über die volle `W9`, die zusätzlich die A8-Energie `<f8, U8 f8>`, die
Zwölferenergie `v12* K^-1 v12` und die gemeinsame Quellentransformation `N`
enthält (Abschnitt 5). Für die Uniformitätsforderung (H3) heißt das nur: In
diesem Summanden ist die Hülle außerhalb einer Richtung von Ordnung eins.

## 5. Korrekter Anschluss an `W9` und Folgerungen

**5a. Vollständige Majorante.** Nach A9-HERLEITUNG §6 gilt für `f` im
physischen Raum

```text
f8  = J_old* f,
v12 = F* f - g_F* U8 f8,
nu  = N f = Lambda_T* f - g* U8 f8 - a_fin* K^-1 v12,
<f, W9 f> = <f8, U8 f8> + v12* K^-1 v12
          + (11/10) [ beta^-1 <nu, R_L nu> + (J* nu)* P_upper (J* nu) ].
```

Satz 1 betrifft nur den letzten Summanden und nur als obere Hülle. Die
Quellentransformation `N` und die ersten beiden Energien verschwinden durch die
Rang-eins-Kalibrierung nicht.

**5b. Oberer Diagnoseskalar.** Mit `psi = N* J v` ist
`<psi, R z>_H9 = <J v, N R z>_W_X` der zum Spike gehörende obere
Diagnoseskalar. Er ist ein Beitrag zu einer zusätzlichen hinreichenden Hülle;
ein zu großer Wert zeigt nur, dass diese Hülle nicht zum Abschluss reicht, und
ist kein `CERTIFICATE_FAIL` der ursprünglichen festen Antwortregel.

**5c. Unterer Ausschlusstest.** Für `P = P_upper > 0` gilt
`P >= (P v)(P v)* / (v* P v)` (Cauchy-Schwarz in der `P`-Metrik). Mit
`p = P_upper v`, `q = v* P_upper v`, `chi = N* J p` folgt

```text
<f, W9 f> >= (11/10) |<J p, N f>|^2 / q,        R* W9 R >= (11/10) (chi* R)* (chi* R) / q .
```

Übersteigt eine rigorose Untergrenze hiervon auf einem zulässigen `z` eine
rigorose Obergrenze von `K_P[z]`, ist der konkrete Vergleich `K_P - R* W9 R`
negativ: `CERTIFICATE_FAIL` dieses Vergleichs, nicht der tatsächlichen
A11-Form. Bei Auswertung über `R_hat` sind die Modellfehler im Skalar
mitzuführen. Die endlichen Daten `p`, `q` sind aus `P_upper` und `v_hat`
dieses Pakets exakt berechenbar; die skalaren Restfunktionen (`N`, `J` in
Funktionsdarstellung) liegen hier nicht vor.

**5d. Antwortregel.** Eine erneuerbare Regel kann `J v` in die endliche
Antwortbasis aufnehmen oder die gerichtete Budgetlücke in Richtung `u`
schärfer einschließen; beides ohne Rückgriff auf die Zielpositivität. Ob die
eingefrorene Regel `A9_A11_N12_MIDPOINT_INVERSE_60_V1` scheitert, folgt weder
aus Satz 1 noch aus einer Antwortnorm; ihr Status bleibt `UNRESOLVED`.

**5e. Ursprung: kein Rundungs- oder Einschließungsartefakt (Nachtrag,
Abschnitt 7).** Die getrennte Auswertung aus dem gebundenen Budgetpaket
ergibt für die Richtung `u` (je `/||u||^2`)

```text
                       gerade              ungerade
u* D203 u              1.446574323191e-13  4.802798196429e-13
u* M_upper u           1.446570179788e-13  4.802715290430e-13
u* E u                 4.143403183543e-19  8.290599939281e-18
E relativ zu D203      2.864 ppm           17.26 ppm
analytischer M-Fehler  0.877 % von u*Eu    0.00559 % von u*Eu
reine Rundung          < 2.5e-37           < 1.2e-38
```

Bei unverändertem `D203`, unverändertem `X` und der geerbten zweiseitigen
Fehlerhülle von `M` kann das tatsächliche `M` die Lücke höchstens um
`1.7549 %` (gerade) bzw. `0.01119 %` (ungerade) vergrößern; die endliche
Verstärkung bleibt über `55590` bzw. `9362`. Genauere `M`-Daten beseitigen
den Spike also nicht. Das ist eine Aussage über den festgelegten
Untervergleich, nicht über die tatsächliche A9-Inverse; Verluste im
konservativen `D`- oder `U8`-Vergleich bleiben davon getrennt.

**5f. Kofinalität.** Lemma 2 des Reduktionspakets betrifft die tatsächlichen
eingeschränkten Inversen, nicht eine Majorantenkonstruktion, und nichtfallend
heißt nicht unbeschränkt: `Q_n = diag(1/C, 1, ..., 1)` ist eine beliebig lange
genestete Kette mit konstanter Inversnorm `C` (Budgetpaket, HERLEITUNG §6).
Eine zwingende Kofinalitätssperre oder die zwingende Aufnahme genau von `Jv`
in die Antwortbasis folgt aus dem Befund nicht.

## 7. Nachtrag 16. Oktober: gebundene Anschlusspakete

**Rekonsiliation.** Der Nachtrag zu #227 verweist auf
`Objekt-X-A9-Spike-Artefaktpruefung-und-Korrekter-W9-Anschluss-2026-10-15.zip`
mit SHA-256 `7f7129945b38768a5ec88994b783211db1ceb0810129ffc4ea4ba7db5beb1f5e`.
Eine Gegenprüfung konnte zunächst keine Bytes zu diesem Hash finden und bot
ein anders benanntes Paket (`c6a3bfbf…`) an. Das am 16. Oktober übergebene
Archiv hat exakt den referenzierten Hash; nur dieses ist hier gebunden
(`archives/`, `SOURCE_BINDINGS.json`, Abschnitt `identity_reconciliation`).

**Budgetpaket (15. Oktober, `7f712994…`).** Enthält unverändert das
A9-Inversarchiv (`a1fa4195…`) und das Antwortarchiv
(`Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11.zip`), die
getrennte `D203`/`M`-Auswertung aus 5e, die `N*`-Formel und `p = P_upper v`,
`q = v* P_upper v` exakt rational. Zusätzlich beweist es bedingt eine echte
untere Verstärkung der reduzierten Vergleichsinversen auf der Testrichtung
`J X u`: `<JXu, H_*^-1 JXu>/||JXu||^2 > 55000` (gerade) bzw. `> 9300`
(ungerade); ausdrücklich keine Untergrenze für die volle wahre A9-Inverse.
Frischer Replay: 17 Manifestbindungen, 4 Git-Blob-Bindungen an den
#226-Head `ed31c343`, 524 exakte Gleichheiten, 8 Cauchy-Kontrollmodelle.

**N*Jp-Paket (16. Oktober, `b48e3895d57cc5cc2c11ca170e32d6af5fbdfcde9948b4db7c370d3376b6d57b`).**
Liefert die vollständigen Funktionsdefinitionen von `J`, `Lambda_T`, `g`,
`g_F`, `U8`, `a_fin`, `K` und das globale Quellarchiv (`2ca3c682…`). Die
Basis84 liegt auf der alten Schale `(a8, b9) = (3 log 2 / 2, log 3)`; erst
`Lambda` hebt sie in den A9-Raum. `U8` ist als ganze Funktionsaktion
ausgeschrieben (`y = T_h f`, `d = Phi* f - B8 y/delta`,
`c = C_inv C_inv* d/(1-rho)`, `U8 f = Phi c + T_h*(y - B8* c)/delta`), ohne
hohen Abschneidegrad. Für `t = v` und `t = P_upper v` je Parität liegen `Jt`
in 96 lokalen Legendre-Koeffizientenintervallen und die zwölf
`k = K^-1 a_fin Jt` als Einschließungen des tatsächlichen `k` vor
(Modell `k0` plus analytischer Fehler in `K`-Norm: `1.965e-8` / `1.113e-3`
gerade, `7.924e-10` / `7.427e-6` ungerade). Die gesuchte Funktion ist

```text
chi_t = N* J t = Lambda r - F k - J_old U8 (g r - g_F k),     r = J t,
chi_t(x) = -lambda(r) m(x)/mu - sum_i F_i(x) k_i - u(x)      (0 < x < a8),
chi_t(x) = r(x) - sum_i F_i(x) k_i                            (a8 < x < b9),
ell_t(R z) = <chi_t, C z>_H9 - <chi_t, D12 T z>_H9,
<R z, W9 R z> >= (11/(10 q)) |ell_p(R z)|^2 .
```

Die `k`-Koeffizienten sind groß (bis `2.8e11` gerade, `2.5e10` ungerade,
Intervallbreiten bis `2.1e4` bzw. `68`); Aufhebungen und Fehler müssen
gemeinsam behandelt werden. Frischer Replay: 24 positive `K`-Pivots, 168
`p`-Komponenten, 2 `q`-Identitäten, 288 Inverseinträge, 48 `K k0`-Gleichungen,
32 Nullrelationen, 384 Koeffizientenintervalle; `DIRECTIONS.json` bytegleich.

**Nicht berechnet:** `chi`-Integrale, der untere Ausschlusstest auf den zwölf
zulässigen `z`, die vollständige `W9`-Energie, A9->A11. Keine Aussage über
Erfolg oder Scheitern der N12-Regel.

`scripts/replay_spike_budget_nstar.py` bindet beide Archive, die sichtbaren
Kopien und die eingebetteten Quellarchive, führt beide Prüfer außerhalb des
Repositories aus und vergleicht die Quittungen mit
`reports/EXPECTED_BUDGET_RECEIPT.json` und `reports/EXPECTED_NSTAR_RECEIPT.json`.

## 6. Ergebnisstatus

| Aussage | Status |
| --- | --- |
| Satz 1 (Rang-eins-Zerlegung, Schärfezeugen) | exakt rational zertifiziert |
| Satz 2 (Fast-Nullrichtung von `E`) | exakt rational zertifiziert (obere Schranke) |
| Spurzerlegung `56573 / 48 / < 1` | numerisch, Kontext |
| Korollar Abschnitt 4 | bewiesen, bedingt auf (1.1), (2.4), (3.3) des A9-Pakets |
| Abschnitt 5a-5f | Konsequenzen und Arbeitsanweisungen, keine neuen Sätze; 5c ist eine elementare Ungleichung |
| Ursprung 5e | kein Artefakt; Untervergleich echt eng (Budgetpaket, bedingt) |
| untere Verstärkung von `H_*^-1` auf `JXu` > 55000 / 9300 | Budgetpaket, bedingt, nur reduzierter Vergleich |
| `chi`-Integrale, Ausschlusstest | offen |

## 7. Exakte Kontrollen

`verify.py` (Standardbibliothek, exakte Bruchrechnung) prüft die Archiv-SHA,
Symmetrie und Spur von `P`, die Trägheit `(0,0,84)` für Satz 1, die
Rayleighquotienten von `v` und des exakt orthogonalen `w`, die
Rayleighquotienten von `u` und der zweiten Richtung für Satz 2 sowie die
Konstanten des Korollars einschließlich der Reproduktion von (3.3).
Laufzeit etwa 2,5 Minuten, dominiert von den beiden exakten LDL.

## 8. Quellen

- A9-Inverspaket: `research/x-c1/a9-inverse-renewal-2026-10-13/` (PROOF.md,
  original/HERLEITUNG.txt, original/BERICHT.txt, gebundenes Archiv).
- Reduktionspaket: `research/x-c1/renewal-reduction-and-obstructions-2026-10-15/PROOF.md`.
- Arbeitsauftrag: `research/x-c1/a9-a11-certificate-calibration-2026-10-15/WORK_ORDER.md`.
- Basis84-Prüfung: `research/x-c1/a9-inverse-renewal-2026-10-13/original/sources/BASIS84_ENERGY_REVIEW.txt`.
