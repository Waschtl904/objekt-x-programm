# Abgrenzung von Suche, Nachweis und Reproduktion

Dieser Block verändert weder die äußere Antwortregel noch K_new, den
physischen geraden Zeugen oder den rationalen variationalen Testvektor.
Er untersucht einen anderen Kontrollweg für dieselbe vollständige
Inversenergie. Die Ausschlüsse und Stopplinien der Vorgänger bleiben gültig.

Nicht als Zertifikate verwendet wurden:

- Regularisierte Darstellungen in der gespeicherten Antwortmatrix und
  einzelne zusätzliche Außenkoordinaten. Sie ersetzen keinen ganzen Rest.
- Die direkte analytische Kontrolle der 64-Knoten-Kernquadratur: Ihr
  konservativer Fehlerpreis war unbrauchbar groß. Das war keine entsprechend
  große gemessene Abweichung. Stattdessen wird die 128-Knoten-Kernquadratur
  gerichtet kontrolliert und der Unterschied beider ENDLICHER Modelle durch
  gemeinsame Momente und einen geometrischen Rest auf der ganzen Schale
  eingeschlossen. Das ursprüngliche äußere Modell muss dafür nicht ersetzt werden.
- Bloße Übereinstimmung zweier äußerer Gaußnetze. Die äußere Abnahme verwendet
  analytische Taylorreste, vollständige Prim-Schnittstellen und Randintegrale.
- Ein früher Taylor-Probeabschnitt, der eine Prim-Schnittstelle überquerte.
  Die unabhängige Punktkontrolle verwarf ihn. Der angenommene vollständige
  Lauf benutzt ausschließlich die anschließend exakt geprüfte Schnittliste.

Eine endliche Paarungskontrolle verschiedener Mittelpunktdarstellungen
zeigte eine kleine verbleibende Differenz. Diese wird nicht als Gleichheit
oder als gerichteter Fehlerpreis verwendet. Das ganze Fehlerbudget bezahlt
die tatsächliche Intervallplatzierung des eingefrorenen p-Modells in K-Norm
sowie sämtliche Quellen-, Koordinaten- und physischen Modellfehler.

Der ursprüngliche äußere Lauf wurde kontrolliert unterbrochen, um seine
disjunkten restlichen Abschnittsbereiche parallel auszuführen. Fertige,
hashgebundene Abschnitte blieben erhalten. Jeder Abschnitt wird exklusiv
angelegt; die finale Summe verlangt alle 411 Belege. Vor Erstellung einer
ersten Gesamtsumme wurde der konstante Term im expliziten Randintegral von
25 auf den korrekten Wert 29 korrigiert. Kein abgenommenes Gesamtergebnis
benutzt den alten Term.

Der erste frische Gesamtreplay scheiterte technisch, weil zwei zusätzlich
gelesene Funktionsquellen im Kopierabschluss fehlten. Der endliche Replay
war bereits bytegleich. Die Zusammenstellung wurde um residuals.py und
old_fields.py erweitert und in einem neuen Verzeichnis vollständig neu
gestartet. Es wurde keine Hashprüfung abgeschaltet. Der finale Abnahmebeleg
weist den tatsächlichen Ausgang dieses vollständigen Replays aus.

Die ursprünglichen numerischen Entwicklungsquellen sind unverändert unter
whole/ erhalten. Ihre Teilstatusfelder behaupten absichtlich keinen ganzen
Vergleich. Erst der gemeinsame whole_audit.py verbindet alle erforderlichen
Nachweise. Die Zeitangaben einzelner Abschnitte sind Laufprotokolle und
gehören nicht zum kanonischen mathematischen Endergebnis.

Die extrem kleine Moment-Taylorrestzahl wird in den allgemeinen
80-Dezimalstellen-Ausgaben stark vergröbert angezeigt. Ihr analytischer
Preis <1e-200 folgt aus dem gesonderten exakten Fakultätsvergleich in der
Herleitung; die grobe Anzeige wird dafür nicht als ausreichender Endpunkt
benutzt. Die verbleibende Gesamtreserve wird mit einfachen konservativen
Caps ausgewiesen, ohne weitere Präzisions- oder Kandidatensuche.
