# Bedingtes Hilfslemma für Inversmajoranten

Das [Lemma](PROOF.md) gibt die vollständige neue Inversmajorante aus,
wenn eine positive Restvergleichsform bereits auf dem ganzen neuen Raum
bewiesen ist. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**;
keine arithmetische Statuspromotion.

Die Voraussetzungen betreffen insbesondere die vollständige Formdomäne,
graphbeschränkte Antworten und echte Hilbertresiduen. Die Konstruktion
der benötigten arithmetischen Restreserve bleibt eine eigene Aufgabe.

Reproduktion ab Repositorywurzel:

```text
python -B research/x-c1/conditional-inverse-propagation-2026-10-15/verify.py
```

Die zwölf neu ausgeführten rationalen Kontrollmodelle prüfen Algebra und
Fehlerfälle. Sie sind kein Test der tatsächlichen A9→A11-Operatoren.
Der Prüfer bindet zusätzlich den analytisch gelesenen Beweistext per SHA-256.
Eine Textänderung erfordert eine neue Prüfung und Aktualisierung dieses
Ankers; der Hash selbst beweist keine Mathematik.

Verbindlicher Prüfumfang dieser Änderung: Domänen- und Kongruenzprüfung
des Lemmas, alle zwölf Kontrollmodelle, META-Proofbindung, kanonischer
Registervalidator und dessen vorhandene Tests sowie anwendbare CI am
finalen PR-Head und Integrationscommit. Historische Großintegrationen
sind für dieses abstrakte Lemma keine Eingaben und werden nicht wiederholt.
