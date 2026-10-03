# Gemeinsamer Y-Kernel und Odd-Eigenlinie zweiter Ordnung

**Gesamtergebnis: UNRESOLVED.** Bedingt verbessern sich `central` auf
**2,933357°** und `quarter` auf **3,070163°**. Der bisher offene Schnitt `half`
wird erstmals auf dem maximalen Eigenwertast isoliert, mit einer rigorosen
Gesamtwinkelobergrenze von **3,642693°**.

Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. Dieses Paket ist ein neuer
Forschungsbefund auf Basis `main@b8924422`, keine integrierte Statuspromotion.

## Alle 19 unveränderten Fälle

Die Zahlen sind nach oben gerundete Obergrenzen für zweimal die Abweichung
von derselben physischen Referenz. `offen` bedeutet fehlende Linienisolation;
der interne Rückfallwert 180° ist kein bestimmter tatsächlicher Winkel.
Die exakten alten und neuen rationalen Grenzen stehen in `summary.json`.

| Fall | Bisherige affine Obergrenze | Zweite Ordnung | Maximaler Ast |
| --- | ---: | ---: | --- |
| root | offen | offen | nicht isoliert |
| point/central | 1.903077° | 1.903077° | zertifiziert |
| slice/central | 3.405363° | 2.933357° | zertifiziert |
| point/half | 2.180335° | 2.180335° | zertifiziert |
| slice/half | offen | 3.642693° | zertifiziert |
| point/two_thirds | 2.360824° | 2.360824° | zertifiziert |
| slice/two_thirds | offen | offen | nicht isoliert |
| point/five_eighths | 2.316014° | 2.316014° | zertifiziert |
| slice/five_eighths | offen | offen | nicht isoliert |
| point/quarter | 1.967736° | 1.967736° | zertifiziert |
| slice/quarter | 3.765366° | 3.070163° | zertifiziert |
| terminal/rLLLLL | offen | offen | nicht isoliert |
| terminal/rLRLLLLRRLRL | offen | offen | nicht isoliert |
| terminal/rLRLLRLRRLRL | offen | offen | nicht isoliert |
| terminal/rLRRLLRRLLLL | offen | offen | nicht isoliert |
| terminal/rRRLLLLLLLR | offen | offen | nicht isoliert |
| terminal/rRRLLLRRR | offen | offen | nicht isoliert |
| terminal/rRRLLRRRR | offen | offen | nicht isoliert |
| terminal/rRRRR | offen | offen | nicht isoliert |

Alle fünf bekannten vollständigen Punkte bleiben enthalten und maximal.
Root, `two_thirds`, `five_eighths` und alle acht Diagnoseboxen bleiben
UNRESOLVED. Die Diagnoseboxen sind keine vollständige Überdeckung der Root.
Damit ist kein uniformer Gesamtwinkel unter zehn Grad bewiesen. Die im Gate
genannte Voraussetzung für einen neuen adaptiven Baum ist nicht erfüllt.

## Was die neue Rechnung erhält

Die gemeinsame Gleichung Y_L X+Y_R=0 wird um ein exakt gelöstes rationales
Zentrum entwickelt. Dieselben Y-Symbole bleiben in q−Hq, N, den drei
Momentkompressionen und der skalierten Liniengleichung erhalten. Alle
quadratischen Terme werden mitgeführt. Höhere Terme und jede Rundung erhalten
eine rigorose Restschranke. Auf der ganzen Root-Box gilt h<0,007720.

Die komponentenweise Neumann-Schranke ist hier entscheidend: Eine einzige
Restgrenze für alle Kernel-Zeilen belastet die kleinen ersten Komponenten zu
stark. Die implementierte Schranke nutzt die nichtnegative Matrix |H| und
ihre Potenzen, einschließlich eines vollständig bezahlten geometrischen Tails.
Die Herleitung steht in `PROOF.md`.

## Kontrollen und Reproduktion

- 1.530 exakte Polynom-, Rundungs- und Fehlerproduktkontrollen bei 70 und
  absichtlich nur drei Dezimalstellen; 60 exakte Kernel-Punktkontrollen.
- Positive, minimale und entartete Astkontrollen sowie negative Prüfungen
  für singuläre Zentren, fehlgeschlagene Neumann-Bedingung und ungültige Daten.
- Separater Audit: 19 exakte Zentrum-/Tailprüfungen, acht maximale
  Wurzelzertifikate, 41 Newton-Schritte und elf Arb-Winkelprüfungen bei 768 Bit.
- Die kleinen geerbten Kontrollen bestehen erneut: 40 skalierte Stifte,
  160 exakte Identitäten, Astkontrollen und affine/zentrierte Prüfungen.
- 59 Originaldateien des Direct-Line-Pakets einschließlich der 41 früheren
  Dateien bleiben bytegleich. Acht ältere Quellen stimmen mit ihren
  gebundenen Git-Blobs überein. Das Direct-Line-Originalarchiv bleibt erhalten.

Der Replay führt alle 19 Fälle vollständig aus und verlangt bytegleiche
Vergleichs-, Kontroll-, Audit- und Zusammenfassungsquittungen. Sein abschließender
Nachweis wird außerhalb des unveränderten Pakets in `REPLAY.json` abgelegt.
Manifest und Quellenprüfung sind verpflichtend; ein Teilreplay genügt nicht.

Es wurden keine Operatorintegrale, Y58-Dualdaten, L_B-Daten oder neuen
adaptiven Bäume gerechnet. PR #187 bleibt unangetastet. UNRESOLVED beweist
weder strukturelle Offenheit noch das Scheitern aller höheren Modelle.
Allgemeines Renewal, A13-Positivität, kofinale positive Familie, globales
Objekt X und RH bleiben offen.
