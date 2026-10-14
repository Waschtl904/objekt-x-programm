# A9: erneuerte Inverse und vollständiger hoher Schurrest

Herleitung: 13. Oktober 2026; Integration: 14. Oktober 2026.
**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.

Nach zusätzlicher Elimination der Basis84 gilt für den ganzen neuen L-orthogonalen Schurrest mindestens 2/3 W_X; explizite gemeinsame A9-Inversmajorante aus dem vollständigen globalen Residualvergleich.

Für H_* auf dem bisherigen T gilt mit der vollständigen Hilfsforminversen R_L
und der festen nichtorthonormalen Basis J:

    H_*^-1 <= (11/10)[beta^-1 R_L + J P_upper J*].

Die beiden neuen rationalen 84x84-Obermatrizen werden durch je einen vollständigen
287x287-Schurblock zertifiziert. Die erneuerte gemeinsame physische Majorante W9
erfüllt A9^-1 <= W9. Für K_L={v in T: L[J,v]=0} gilt nach vollständiger
Schurminimierung über den alten A8-Raum, F12 und J mindestens (2/3)W_X.
Auf dem unveränderten bisherigen T gelten zusätzlich >W_X/65000 gerade und
>W_X/11000 ungerade. Diese drei Räume und ihre Böden bleiben getrennt.

Die [Domänenherleitung](../a9-domain-continuation-2026-10-13/PROOF.md) liefert
den ergänzenden Formrahmen. Neue Quellenintegrale und nächste Horizonte sind
noch nicht berechnet. Die bisher gebundenen großen Integrationen bleiben Inputs.

Die vollständige neue Begründung mit Definitionen, Formdomänen, Konstanten und
Schuridentitäten steht unverändert in [HERLEITUNG.txt](original/HERLEITUNG.txt).
Ihr verbindliches Originalarchiv ist `Objekt-X-A9-Inverserneuerung-und-Hoher-Schurrest-2026-10-13.zip`, SHA256 `a1fa41958d79ab16a7c42b12375c3373f5a86a99993ae2d23c984ff6b3b2e8ae`.
Der vollständige Mitgliedskatalog [SOURCE_BINDINGS.json](SOURCE_BINDINGS.json)
bindet alle Originalbytes einschließlich der ausführbaren Prüfer und Ergebnisse.

Abhängigkeit ist der [bedingte globale A8→A9-Abschluss](../a8-a9-global-closure-2026-10-13/PROOF.md).
Der Replay rekonstruiert dessen Originalarchiv mit SHA256
`65085974657257bd447d93342c5001d29e797b2fa70d876d53d36b587b16c2ba`
und führt den direkten ursprünglichen Feldabgleich aus.

Der Boden 2/3 bezieht sich auf den neuen Rest nach A8, F12 und Basis84; er beweist nicht den alten gesonderten Tailboden 1/20. Keine externe analytische Prüfung wird durch einen rationalen
Replay oder einen GitHub-Merge ersetzt. Allgemeine Horizontfortsetzung,
Objekt X, globale Weil-Positivität und RH bleiben offen.
