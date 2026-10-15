# A9-Inversspektrum: Ein-Richtungs-Verstärkung und Kalibrierung der Zertifikatsklasse

15. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. Art: DIAGNOSTIK
mit exakten rationalen Zertifikaten.

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
Basis84-Ordnung. Die Richtung ist strukturell, nicht paritätsspezifisch.

## 3. Satz 2: Ursprung in einer fast verschwindenden Budgetlücke (exakt zertifiziert)

```text
gerade:    u^T E u / |u|^2  <=  4.2 * 10^-19,     zweite Richtung  <=  3.3 * 10^-12
ungerade:  u^T E u / |u|^2  <=  8.3 * 10^-18,     zweite Richtung  <=  3.3 * 10^-11
```

bei maximalem Diagonaleintrag von `E` nahe `1`. Da `E > 0` (A9-Paket),
ist `lambda_min(E)` positiv, aber höchstens von dieser Größe; die
Konditionszahl von `E` übersteigt `10^18`. Numerisch (nicht zertifiziert,
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

In der Sprache des Reduktionspakets: Das A9-Zertifikat hat, relativ zur
physischen Metrik `W_X`, die Gestalt

```text
U_9  <=  C_off * W_X^-1  +  C_spike * (J v)(J v)^*,
C_off ~ 4.7 / 2.8,   C_spike ~ 6.2 * 10^4 / 1.0 * 10^4 .
```

Die Uniformitätsforderung (H3) ist deshalb an A9 keine Aussage über
84 Richtungen, sondern über eine.

## 5. Folgerungen für `H_9` und den A9->A11-Auftrag

**5a. Residualpreis.** Für jede Antwortabbildung `P_9` und jedes `z` im
neuen A11-Raum gilt nach Abschnitt 4

```text
<R z, U_9 R z>  <=  C_off ||R z||_W_X^2  +  C_spike |<J v, R z>_W_X|^2 .
```

Der erste Term ist mit Konstante unter `5` harmlos. Der gesamte Schwierigkeitsgrad
von (H1) konzentriert sich im Skalar `<J v, R z>` je Parität. Ein billiger
Vortest, der vor den vollständigen gemeinsamen Energien des Arbeitsauftrags
`a9-a11-certificate-calibration-2026-10-15` ausgeführt werden kann, ist die
Berechnung genau dieser Kopplung der neuen Kanalquellen an `J v`. Liegt sie
nicht unter `(reserve / C_spike)^(1/2)`, versagt die Regel
`N12-MIDPOINT-INVERSE-60-v1` als `CERTIFICATE_FAIL`, ohne dass dies etwas
über die tatsächliche A11-Form aussagt.

**5b. Antwortregel.** Eine erneuerbare Regel hat zwei zulässige Auswege,
beide ohne Rückgriff auf die Zielpositivität: Entweder wird `J v` in die
endliche Antwortbasis aufgenommen (die Richtung wandert aus dem
unendlichen Rest in den exakt invertierbaren endlichen Block), oder die
gerichtete Budgetlücke in Richtung `u` wird mit schärferer Einschließung
neu bewertet. Die wachsende Zahl kritischer Richtungen ist im Programm
ausdrücklich zugelassen.

**5c. Zwei Hypothesen zum Ursprung (offen).** `lambda_min(E) ~ 10^-19`
kann (i) eine echte Fast-Kritikalität des A8->A9-Schurbudgets in dieser
Richtung oder (ii) ein Artefakt der gerichteten Einschließung sein, bei der
`D203` und `M_upper` in Richtung `u` bis auf Rundungsreste übereinstimmen.
Entscheidbar ist das durch getrennte Auswertung von `u^T D203 u` und
`u^T M_upper u` aus dem Antwortarchiv; dieses liegt nicht im hier gebundenen
Zip. Im Fall (ii) ist die Verstärkung mit besserer Einschließung
reduzierbar; im Fall (i) ist die Richtung ein echter Kandidat für eine
akkumulierende kritische Familie im Sinn der Kofinalitätsobligation.

**5d. Kofinalität.** Nach Lemma 2 des Reduktionspakets kann die
Inversmajorante entlang der Kette nicht fallen. Bleibt die Richtung `J v`
im unendlichen Rest, erbt jeder spätere Horizont `C_spike >= 6 * 10^4`.
Eine Erneuerungsregel, die sie nicht in den endlichen Block überführt,
ist daher strukturell nicht kofinal fortsetzbar, unabhängig von den
A11-Daten.

## 6. Ergebnisstatus

| Aussage | Status |
| --- | --- |
| Satz 1 (Rang-eins-Zerlegung, Schärfezeugen) | exakt rational zertifiziert |
| Satz 2 (Fast-Nullrichtung von `E`) | exakt rational zertifiziert (obere Schranke) |
| Spurzerlegung `56573 / 48 / < 1` | numerisch, Kontext |
| Korollar Abschnitt 4 | bewiesen, bedingt auf (1.1), (2.4), (3.3) des A9-Pakets |
| Folgerungen 5a-5d | Konsequenzen und Arbeitsanweisungen, keine neuen Sätze |
| Ursprungshypothesen 5c | offen |

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
