Objekt X — Abdeckung einer berechneten Basis und gemeinsames Fehlerbudget
10. Oktober 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

Zweck: Ein konkreter Prüfauftrag für den laufenden Rechenstrang, ohne seine
Operatorintegrationen zu duplizieren. Der aktuelle Arbeitsstand von GPT 2
wurde nicht übermittelt; dieses Paket behauptet keine Prüfung seiner Daten.

Lesereihenfolge:
  1. PRUEFAUFTRAG_GPT2.txt — konkrete Eingaben, Schranken und Abnahme
  2. HERLEITUNG.txt       — vollständiger bedingter Beweis
  3. checks.json         — ausgeführte rationale Kontrollen und Gegenkontrollen

Neue Kernaussage:
Für eine exakte, möglicherweise nichtorthonormale Formbasis J genügt eine
volle Gramobergrenze für L_64* - J P. Liegt diese unter I/20, trägt der
gesamte W_X-orthogonale Tail den Boden 1/20. Exakte Rangbestimmung und
unbezahlte Nullsetzungen kleiner Funktionalwerte sind dafür nicht nötig.

Nach diesem Tailnachweis lautet ein hinreichender endlicher Schurtest
  K_lower - 20 G_residual >= eta W_J, eta>0.
Der Faktor 20 darf nur nach nachgewiesenem Tailboden 1/20 benutzt werden.
Bei schärferem nachgewiesenem Tailboden wird sein Kehrwert eingesetzt.

Reproduktion, Python-Standardbibliothek:
  python3 -B test_protocol.py
  python3 -B check_certificate.py examples/synthetic_pass.json
  python3 -B verify_package.py

Alle examples/-Daten sind SYNTHETISCH. Der Prüfer bestätigt ausschließlich
die rationalen Folgerungen aus als korrekt vorausgesetzten Operator-
einschließungen. Er erzeugt weder fehlende vollständige Grame noch einen
Nachweis ihrer Herkunft aus dem wirklichen Prim-/Gamma-Operator.
Auch eine erfolgreiche Prüfung von späteren Daten bleibt ohne deren
gesonderten analytischen/arithmetischen Nachweis bedingt.

inputs/ enthält unverändert das vorausgesetzte 64er-Paket vom 9. Oktober.
Seine Herkunft ist in SOURCE_BINDINGS.json verzeichnet. Bestehende Archive,
GitHub und laufende fremde Arbeitszweige wurden nicht verändert.

ACTUAL_A8_A9_REMAINDER_SIGN = OPEN
ACTUAL_BASIS_COVERAGE = NOT_EVALUATED
ACTUAL_TAIL_LEAKAGE_BOUND = NOT_EVALUATED
EXTERNAL_REVIEW = OPEN
