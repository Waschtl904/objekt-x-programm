# Entscheidung: genau ein kohärenter K-Pilot, nur gerade

18. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.

U8, K und eine strukturelle Schurverschärfung wurden gemeinsam verglichen.
Ausgewählt ist die Erneuerung des alten Zwölfer-Untervergleichs:

    K_star = K + (13/100000000) G_F <= K_actual.

Die Beschränkung des gemeinsamen Fehlerpreises auf die zwölf F-Quellen
erlaubt diese konkrete Verstärkung. Zwölf positive Intervallpivots bestätigen
sie; G_F wird separat positiv geprüft. Die Wirkung auf die Energie ist offen.

Der Pilot muss K_star, E_star, P_star und nu_star gemeinsam erneuern.
Weil E_star>=E und die alten Residualfunktionen unverändert bleiben, gilt
der vollständige alte Restnachweis weiter. Keine neuen Integrationen sind
für diesen Piloten vorgesehen. Antwortmatrix, gerader #238-Zeuge und äußeres
K_P-Budget bleiben fest. Nur die Zulässigkeitsvorprüfung von K_star ist hier
berechnet; **der Pilot-Energietest ist noch nicht ausgeführt**.

`PROOF.md` enthält für alle drei Wege Ungleichung/Ersatz, quantitative Belege,
Datenlücken, kleinsten Test und die Auswahl. Das Pilotprotokoll legt Matrixgrößen,
Fehlertransport, Erfolg, Abbruch und 30-Minuten-Rechenlimit vorab fest.

```sh
python research/x-c1/w9-structural-decision-2026-10-18/verify.py --check
```

`INPUT_BINDINGS.json` und `MANIFEST.json` binden die Entscheidungsbelege;
`ACCEPTANCE.json` dokumentiert den frischen kleinen Replay und lokale Checks.
Keine parallelen U8-/Schur-Piloten, keine neue große Rechnung, kein Merge.
Meilenstein 4, N12 insgesamt und die externe Prüfung bleiben offen.
