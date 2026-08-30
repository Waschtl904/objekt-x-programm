# P11-R32 / SW1-A10-C1B2A-TRANSFER — Independent Review Packet

## Zweck

Dieser Review-Knoten ist **getrennt** vom bereits mechanisch zertifizierten Rank-4-Chirotop-Ledger.

Zu prüfen ist ausschließlich der mathematische Transferschritt

[
r_0=7/2
quadlongrightarrowquad
rin(3,4)
]

für die konkrete affine Hyperflächenfamilie aus 18 Kollisionsflächen plus 4 Simplexfacetten.

Keine Aussage über Cross-Gram-Injektivität.

---

## Zertifizierter finite/algebraischer Input

### 0. Affine Verstärkung mit ausgezeichnetem Unendlichkeitselement

Zusätzlich zum 22er-Chirotop liegt nun der stärkere affine Prüfer

`scripts/certify_sw1_a10_c1b2a_affine_chirotope.py`

vor.

Committed Blob:

`1c2f7a3e6123697846e4f6d5e931d3c962b1fb20`

Er fügt das feste ausgezeichnete Unendlichkeitselement

[
g_\infty=(0,0,0,1)
]

hinzu und prüft alle

[
\binom{23}{4}=8855
]

Rank-4-Minoren.

Die 1540 neuen INF-Minoren sind

[
622\text{ identisch Null}+918\text{ konstant nonzero}+0\text{ r-abhängig}.
]

Damit ist die affine, nicht nur projektive, Chirotop-Konstanz auf (3<r<4) mechanisch zertifiziert.

### 1. Ursprünglicher 22er-Minorenledger

Die Datei

`scripts/certify_sw1_a10_c1b2a_chirotope.py`

prüft exakt alle

[
inom{22}{4}=7315
]

orientierten Rank-4-Minoren der augmentierten Zeilen

[
(a_{i,1},a_{i,2},a_{i,3},-b_i(r)).
]

Committed Blob:

`c4acf11c1564a67bd10b92c76bcf74adc6d26ebb`

Ergebnis:

`SW1-A10-C1B2A CHIROTOPE CONSTANCY CERTIFICATE: PASS`

Klassifikation:

[
1652	ext{ identisch Null},qquad
2012	ext{ konstant nonzero},qquad
3651	ext{ affin-linear}.
]

Die einzige Nullstellenmenge der linearen Minoren ist

[
{-3,-2,-1,-1/2,0,1/3,1/2,2/3,1,4/3,3/2,2,5/2,3,4,5,6}.
]

Daher verschwindet kein nichtidentischer Rank-4-Minor für (3<r<4), und der vollständige Chirotop ist dort konstant.

Die vier Simplexfacetten sind Teil derselben 22er-Konfiguration.

---

## Zu prüfender mathematischer Schluss

Die benötigte Aussage ist bewusst enger als ein globaler topologischer Satz.

### TRANSFER-A

Für die stetige Einparameterfamilie der 22 orientierten affinen Hyperflächen folgt aus dem konstanten Chirotop auf (3<r<4), dass die Menge der Covektoren/Topes des realisierbaren orientierten Matroids konstant ist.

Insbesondere sind die 64 offenen Parameterkammer-Signvektoren bei (r_0=7/2) dieselben Signvektoren wie bei jedem tatsächlichen (rin(3,4)).

### TRANSFER-B

Weil die vier Simplexfacetten in der Konfiguration enthalten und orientiert mitgeführt werden, bleibt auch die innerhalb

[
0<sigma<R<arepsilon<(r+1)/2
]

relevante geklippte Kammerstruktur konstant.

### TRANSFER-C

Die (B_{96})-Kreiswanddifferenzen werden durch dieselben 18 Kollisionshyperflächen kontrolliert, und GATE1R hat bereits

[
S_{96}=S_{92},
qquad
C_{96}=C_{92}
]

als Mengengleichheiten zertifiziert.

Daher soll innerhalb korrespondierender Parameterkammern auch die zyklische Ordnung der 96 Kreiswände konstant bleiben.

### TRANSFER-D

Wenn A–C gelten, darf die exhaustive M1-FULL-Prüfung der 64 Kammern × 96 offenen Kreisatome am Referenzwert (r_0=7/2) auf jedes tatsächliche (rin(3,4)) übertragen werden, **sofern** M1-FULL selbst provenance-sauber PASS ist.

---

## Adversarielle Fragen

1. Reicht die Konstanz des **affinen 23er-Chirotops einschließlich des ausgezeichneten Unendlichkeitselements** tatsächlich aus, um den vollständigen realisierbaren affinen orientierten Matroid/Covektor-Datensatz konstant zu halten?

2. Können identisch verschwindende Minoren eine versteckte Änderung des Covektor-Datensatzes erlauben, obwohl sämtliche nichtidentischen Minoren auf ((3,4)) ihr Vorzeichen behalten?

3. Sind die vier Simplexfacetten korrekt Teil der orientierten Konfiguration, so dass auch Rand-/Clipping-Inzidenzen abgedeckt sind?

4. Reicht die konstante Tope-Struktur für die Aussage „dieselben 64 offenen Kammer-Signvektoren“, oder wird zusätzlich eine echte ambient isotopy benötigt?

5. Ist für M1-FULL überhaupt eine ambient isotopy nötig, oder genügt die Konstanz der Kammer-Signvektoren plus der (B_{96})-Kreisordnung?

6. Folgt die konstante zyklische (B_{96})-Ordnung in jeder Kammer tatsächlich aus den bereits zertifizierten Kollisionshyperflächen, oder fehlt eine zusätzliche Wrap-/Kreisorientierungsbedingung?

7. Gibt es bei (r=3) oder (r=4) relevante Degenerationen, die den offenen Intervalltransfer (3<r<4) trotzdem beeinflussen könnten?

8. Ist der Schluss TRANSFER-D korrekt auf **offene** Parameterkammern und **offene** Kreisatome beschränkt, wobei Randmengen später nur a.e. ignoriert werden?

9. Welche minimale mathematische Aussage sollte nach erfolgreichem Review gebucht werden:
   - konstante Covektor-/Tope-Struktur,
   - kombinatorische Arrangement-Isotopie,
   - oder volle ambient isotopy?

10. Folgt aus keinem dieser Punkte bereits irgendeine Aussage über
[
kerGamma_I?
]
Die erwartete Antwort ist ausdrücklich **nein**.

---

## Gewünschtes Verdict

Bitte getrennt urteilen:

- **C1B2A-CHIRO**: bereits mechanisch zertifizierter finite/algebraischer Input.
- **C1B2A-TRANSFER**: GREEN / PARTIAL / FAIL mit genauer Begründung.

Keine Promotion und keine Cross-Gram-Injektivitätsaussage.
