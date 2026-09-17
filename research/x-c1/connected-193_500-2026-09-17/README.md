# Connected waxing a=193/500 — 17. September 2026

Append-only Forschungsablage für PR #137.

**Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`. Kein Merge, keine Registry-Promotion.

Enthalten:
- `X_C1_CONNECTED_WAXING_193_500.md` — analytischer Nachweis auf der gesamten verbundenen NULLPOL-Klasse `H1_0(-193/500,193/500) ∩ ker E_+ ∩ ker E_-`;
- `check_x_c1_connected_193_500.py` — Standardbibliothek, exakte Bruchrechnung;
- `connected_193_500_checks.log` — ausgeführter lokaler Output, 27 PASS;
- `connected_193_500_results.json` — ausgewählte exakte rationale Resultate;
- `SHA256SUMS` — Bytesicherung.

Hauptsatz des Autortextes:
`Q_W[u] >= 1193/5002000 ||u||_2^2 > 1/5000 ||u||_2^2`.

Der Punkt liegt unter der diagnostischen Nullstelle der skalarisierten Mode 2. Dies ist keine Aussage über den Schwellenübertritt, Prime 3, das volle Einheitsfenster, all-window NP-GAP, Objekt X oder RH.

Elternstände:
- Connected `a=3/8`: Commit `35e36915114122373806366bb8631673bd9f7d5a` enthält das ursprüngliche Paket;
- Connected `a=19/50`: Commit `c2a4f1ffddc285d393d50c87183c2ce25a2bb860`;
- der neue Schritt verwendet kein A1.
