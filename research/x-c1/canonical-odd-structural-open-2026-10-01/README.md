# Ungerade Maximierer und Grenze der Transportmomentrelaxation

**A9 nach A11: Die größte generalisierte Eigenwertgerade ist eindeutig,
aber auch die verstärkte gemeinsame Momentrelaxation lokalisiert sie nicht
eng.** Zwei zertifizierte Vervollständigungen erlauben physische inverse
Antwortrichtungen mit mindestens 89.987266 Grad Abstand.

Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. STRUCTURAL OPEN betrifft
die ausdrücklich geprüfte endliche Relaxation. Die Gegenzeugen werden
nicht als vollständige gemeinsame Realisierungen des ursprünglichen
Operatorproblems ausgegeben.

## Vier unveränderte Pakete

1. [Äußere Projektorobstruktion](01-outer-projector/PROOF.md): stark
   verschiedene Richtungen; eine notwendige gemeinsame b-Grambedingung fehlt.
2. [Gemeinsame Transportmomente](02-transport-moments/PROOF.md):
   H1>=nuB H0>=0 folgt aus Formnaturality und dem vollständigen hohen Schnitt;
   gemischte negative Zeugen schließen zwei bisherige Beispiele aus.
3. [Korrigierte Projektorobstruktion](03-corrected-projector/PROOF.md):
   eine rationale linke Korrektur erhält den Kern, erfüllt die volle
   Transportordnung und erhält die nahezu rechtwinkligen Richtungen.
4. [Rationaler Vier-Variablen-Boxtest](04-rational-box-gate/PROOF.md):
   sieben Knoten, vier Blätter; zwei getrennte Blätter enthalten zertifizierte
   zulässige Punkte. Boxüberleben allein gilt ausdrücklich nicht als Existenz.

Die vollständigen lokalen Dateien und ZIP-Archive sind bytegleich übernommen.
Historische Formulierungen wie „lokal“ in den Originalberichten bleiben als
Teil der unveränderlichen Pakete erhalten. Den aktuellen Integrationsstand
führt [CURRENT_STATE](../../../00-uebersicht/CURRENT_STATE.md).

## Nächster Forschungsblock

Direkt zu kontrollieren ist der gemeinsame projizierte Überlapp
K=(PA UA)*J*(PB UB), mit Y=K GB^-1(GB+LB/17). Zuerst sollen gemeinsame
Kreuzresiduen die für Y58 und Y68 relevanten Funktionale einschließen;
bei unzureichender Schärfe kommen verschobene rationale Projektorfilter
für die vorhandenen Trialspalten in Betracht. Ziel des nächsten Gates ist
ein rigoroser ungerader physischer Winkelkorridor unter 10 Grad Gesamtbreite.
Dies ist ein offenes Forschungsziel, kein Ergebnis dieses Pakets.

Danach folgen bandweise Momente tatsächlicher Maximierer und ein
vorwärts gerichteter Renewal-Kandidat. A13/#187 bleibt separat, bis dessen
Aussage, Konstanten und Abnahme vor dem zusätzlichen Übergang festgehalten sind.
Allgemeines Renewal, kofinale positive Familie, globales Objekt X und RH
erhalten keinen neuen Status. Der positive Gap und die gerade Lokalisierung
bleiben unverändert.

## Reproduktion

Vom Repository-Stamm, Python 3.11 oder neuer, nur Standardbibliothek:

```text
python -B research/x-c1/canonical-odd-structural-open-2026-10-01/replay.py --output PFAD_AUSSERHALB_DES_CHECKOUTS
```

Der Ausgabeordner muss neu sein. Alle vier Quittungen werden bytegleich
reproduziert; unabhängige Prüfer, frische Quellenbindungen und Kontrollen
des Replay-/CI-Pfads werden ausgeführt. Große Integrale und Operatorlösungen
bleiben gebundene Voraussetzungen. CI und Merge sind keine externe
mathematische Gesamtprüfung. SOURCE_BINDINGS.json und SHA256SUMS binden
die Originaldateien, Archive und die ergänzte Publikationshülle.
