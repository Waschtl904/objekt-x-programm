# Vorab begrenzte Machbarkeitsprüfung des vollständigen Restanschlusses

Basis: 34aad090a5a05037cae3e783e07c8382fa47f4b6 (#249).
Unverändert: physischer gerader Zeuge, variationaler Vektor w, K_new,
äußere Antwortregel, Budget und alle bisher gebundenen Fehler.
AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.

Genau drei Ergebnisse:

1. Den vollständigen oberen Testendpunkt F_up mit den vorhandenen
   Basis-/Paarungs-/Formfehlern bestimmen; Budget_lo-F_up ausweisen.
   Kein Platz bedeutet Begrenzung dieses Kontrollwegs, keinen Ausschluss.
2. Mit den vorhandenen rationalen Matrizen X_ans und E_new die
   gewichtete Darstellung prüfen: P=X_ans E_new^-1 X_ans*.
   Falls P positiv definit ist, definiert
   u=E_new^-1 X_ans* P^-1 w exakt X_ans u=w und minimiert u*E_new u.
   Dies ist keine neue physische Richtung. Den gebundenen vollständigen
   Residualtransportpreis c beta u*E_new u ausdrücklich ausweisen.
3. Eine positive rationale Untergrenze epsilon mit E_new>=epsilon D_new
   bestätigen, kappa=(1-c)epsilon berechnen und daraus die für einen
   vollständigen oberen Vergleich notwendige Zielgrenze
   ||nu-HJw||²_(R_L) < kappa beta (Budget_lo-F_up) ableiten.
   Fehlende gemeinsame Funktions- und Fehlerdaten benennen.

Keine neue Integration, Kandidatensuche oder automatische Nachschärfung.
Eine zu große Oberabschätzung ist kein Gegenbeweis zur Unterform.
Bei nichtpositivem rechten Zielwert wird kein positiver Restpreis als
finanzierbar ausgegeben. Punkt 4 und externe Prüfung bleiben offen.

Pflichtabnahme: geprüfte Eingabesnapshots und Herkunftsarchive; gerichtete
Arb-Auswertung bei 1024 Bit; rationale unabhängige Positivitätsprüfungen
für Rang und Formboden; rationaler Endpunktaudit; Negativkontrollen;
bytegleicher Replay aus frischem Git-Archiv des Pakets mit seiner
vollständigen tatsächlichen Dateiabhaengigkeit; Register, generierte
Ansichten, Active Front, 60 Registry-Tests und Diffprüfung. Kein Vollarchiv
des Repositorys und kein erneuter Replay der historischen Integrationen.
Pro vollständigem Rechen-/Replayaufruf höchstens 600 Sekunden.
