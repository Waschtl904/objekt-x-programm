# Allgemeines Ein-Wand-Lemma — q=9 als zweite Instanz

27. September 2026 · **Lokal hergeleitet / EXTERNAL_REVIEW_OPEN**

Der rohe O10-Mechanismus ist jetzt für jede einzelne Prime-Power-Wand der
festen C1a-Familie formuliert und bewiesen. Seine direkten Verhältnisse
liefern eine konsistente Rohtransportfamilie auf **jedem endlichen Horizont**.
q=9 ist die zweite konkrete Anwendung desselben Satzes.

## Allgemeiner Kern

Für eine neue Wand mit `v=Λ(q*)/sqrt(q*)` und `ℓ=log(q*)` gilt

$$
1-\cos(\ell\xi)\le C_\ell g(\xi),\qquad
C_\ell=\max(1,\ell^2/16).
$$

Dadurch sind beide Wandverhältnisse auf allen Frequenzen kontrolliert:

$$
\sqrt{\frac{s_-}{s_-+2v}}\le a_T\le1+vC_\ell,
\qquad
\sqrt{\frac{s_-}{s_-+2v}}\le a_D\le1+\frac{2v}{\kappa}.
$$

Der [vollständige Beweis](PROOF.md) umfasst die ursprünglichen Mellinbedingungen,
vollständigen Formdomänen, beide Carrier, Quellenidentitäten, Formnaturality,
Cocycles, Defektintertwining und Gramkompression. Die positive Korrektur folgt,
sobald die beiden vollständigen Endpunktdefekte strikt positive Böden besitzen.

## Konkretes Ergebnis für q=9

Die neue Kammer ist `(A9,A11]` mit `A9=log3` und `A11=log11/2`.
Der Kanal 9 hat Gewicht `log3/3`; 10 ist keine Primzahlpotenz und 11 bleibt
am rechten Endpunkt inaktiv.

| Größe | Bewiesene Grenze |
| --- | --- |
| Gemeinsame untere Wandgrenze | `sqrt(150/161)` |
| Obere T-Wandgrenze | `41/30` |
| Obere D-Wandgrenze | `86/75` |
| Voller T-Boden bis A11, ohne Formpositivität vorauszusetzen | `36/355` |
| Positiver Defektboden auf dem transportierten alten A9-Bild | `1/(13·10^35+1)` |

Die [q=9-Instanz](Q9.md) enthält auch die gemeinsame Familie über q=8 und q=9
für alle `1≤A≤B≤C≤A11`. Die dritte volle Terminalpositivität bleibt offen.

## Bedeutung für die Fortsetzung

Die rohe Fortsetzung kann über jede endliche Folge von Wänden wiederholt
werden. Die Schranken dürfen dabei vom maximalen Horizont abhängen.
Insbesondere wird die alte Quellnormzahl 17 nicht ohne neue Kontrolle
für beliebig große Horizonte verwendet.

Für die positive Fortsetzung ist weiterhin pro neuer Kammer ein
vollständiger positiver Terminalnachweis nötig. Eine jeweils eigene Reserve
genügt für einen endlichen Schritt. Eine kofinale positive Folge ist nicht
bewiesen; globale Objekt-X- und RH-Aussagen bleiben offen.

Das nächste Gate ist **THIRD-CHAMBER TERMINAL POSITIVITY AT A11**.
Dabei muss auch die q=3-Norm neu bezahlt werden: Rechts von A9 entstehen
Dreierketten mit Norm `sqrt(2)`. Die bisherigen 296 Koordinaten und der
hohe A9-Boden 2/3 werden für diese Kammer nicht übernommen.

## Ausgeführte Prüfung und Reproduktion

**109 exakte Prüfungen bestanden**, einschließlich sieben commitgebundener
Repository-Quellenprüfungen. Die Prüfung benötigt ausschließlich die
Python-Standardbibliothek. Ohne Repositorypfad entfallen die sieben
Git-Prüfungen; es verbleiben 102 Kontrollen.

```text
python verify_wall.py --output replay.json
python verify_wall.py --repository PFAD_ZUM_REPOSITORY --output replay_with_sources.json
```

Der Prüfer kontrolliert Algebra, skalare Majoranten, beide Aktivierungsgrenzen,
die Zuordnung der Wände bei 56 geordneten Endpunkt-/Innen-Tripeln, exakte
Mellin-nullende Quellproben und Dateibindungen. Die unendlichdimensionalen
Abschluss- und Operatorargumente stehen im Beweistext und bleiben extern zu prüfen.

Die ursprünglichen O10- und A9-Dateien wurden vollständig gegen ihre
jeweiligen Manifeste geprüft. Das große A9-Matrixpaket wurde in diesem Block
nicht neu berechnet. Ausgewählte Beweise und Quittungen sind bytegleich
unter `inputs/` beigefügt; das vollständige frühere A9-ZIP ist in
`SOURCE_BINDINGS.json` über seinen Hash gebunden.

## Repository und Audit

Das neue Paket ist lokal; Main und Registry wurden hier nicht geändert.
Der beobachtete Main-Stand ist `7f154559fef92d16b890d24e1ae86faa8f4f6d87`.
Der [Main-Abgleich](MAIN_CHECK.md) berücksichtigt neben dem kumulativen
Audittext auch den während dieser Arbeit hinzugekommenen PR #177.

[Prüfumfang und Grenzen](AUDIT.md) · [Maschinenlesbare Ergebnisse](CHECK_RESULTS.json)

Die früheren Aussagen „q=9 offen“ in kopierten A9-Quittungen gehören zu deren
damaligem Textstand. Der aktuelle Stand dieses Pakets steht hier und in
`CHECK_RESULTS.json`. Die volle dritte Kammer bleibt offen.
