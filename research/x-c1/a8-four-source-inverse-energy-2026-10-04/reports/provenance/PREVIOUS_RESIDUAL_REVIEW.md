# Prüfung der vollständigen A8 Funktionsresiduen

4. Oktober 2026. AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.

## Ergebnis und Bedeutung

Die vier festgelegten A8 Vorschläge besitzen einen vollständig eingeschlossenen, von null verschiedenen Funktionsrest. Der Anteil außerhalb der bisherigen 191 momentkorrigierten Profile ist damit für diese Vorschläge tatsächlich nachgewiesen. Die vollständige alte inverse Residualenergie und eine positive Fortsetzungsreserve bleiben offen. Objekt X ist weiterhin das primäre Konstruktionsziel und noch nicht konstruiert.

**Vollständig nachgerechnet:** Das unveränderte Originalpaket wurde im Modus `full-recompute` ausgeführt. Alle vier Funktionsmodelle, beide vollständigen Grame und die alternative Gramrechnung wurden neu erzeugt. Sämtliche sechs Ergebnisdateien stimmen bytegenau mit den gelieferten Dateien überein. Auch die separate eigene rationale Zertifikatsprüfung besteht. Das geschlossene Originalmanifest ist nach dem Lauf unverändert gültig.

Die Prüfung übernimmt die ursprüngliche Formidentifikation, Operatoranbindung und die vorherigen Quellzertifikate. Sie ist keine externe mathematische Begutachtung und keine neue Rekonstruktion aller ursprünglichen Operatorintegrale.

## Bestätigte Zahlen

Die folgenden Intervalle sind nach außen auf 18 Dezimalstellen gerundet. Ihre Endpunkte wurden mit ganzen Zahlen und rationalen Quadratvergleichen geprüft.

| Parität | Neuer Quellgrad | Vollständige physische Residualnorm |
| --- | ---: | --- |
| Gerade | 2 | [0.067105784115152358, 0.067105784115152401] |
| Gerade | 4 | [0.091850102973068041, 0.091850102973068099] |
| Ungerade | 3 | [0.102463200931677920, 0.102463200931677923] |
| Ungerade | 5 | [0.129550543256119881, 0.129550543256119883] |

Die vollständigen Gram-Eintragsbreiten liegen unter 1.06e-17 beziehungsweise 4.85e-19. Für das L²-Komplement der alten Profile gelten die rational geprüften Matrixschranken

\[
G_{\perp,\mathrm{gerade}}\succeq4.18\cdot10^{-7}I_2,
\qquad
G_{\perp,\mathrm{ungerade}}\succeq8.27\cdot10^{-7}I_2.
\]

Die eigene Prüfung bestätigt diese Aussagen direkt durch positive Hauptminoren von `G_high_lower - floor*I`. Sie übernimmt dafür weder die Auswertungsfunktionen noch die Intervallarithmetik des gelieferten Pakets.

Diese unteren Schranken gelten für Linearkombinationen der jeweils zwei **festen** Residualfunktionen. Sie beweisen kein Hindernis für sämtliche anderen alten Näherungslösungen und kein Scheitern der Fortsetzung.

## Was an der vollständigen Rechnung geprüft wurde

Der Rechenkern behält alle 191 alten Vorschlagskoeffizienten, die ursprünglichen Mellinkorrekturen und die physischen Skalierungsfaktoren. Die alte logarithmische Randwirkung wird vollständig integriert. Die partiellen Primzahlpotenz-Translationen werden auf zehn positiven Integrationszellen behandelt; die negative Hälfte folgt durch Parität. Der neue Kanal 8 tritt nur auf der neuen Seite auf.

Der glatte neue Potentialanteil wird durch eine endliche Reihe mit vollständigem Rest eingeschlossen. Beide regulären Gamma-Kerne behalten ihre uniformen Restmajoranten. Der Operatorfehler wird mit den tatsächlichen alten und neuen Profilnormen bezahlt. Die Mellinprojektion wird vollständig durchgeführt; auch der Fehler ihrer Hilfsreihe geht in das Budget ein.

Die analytischen Momentformeln, die Kernrekursion einschließlich Endpunktkonstanten, die exakte ganzzahlige Polynomkonvolution und die Übertragung der Funktionsfehler auf die gemeinsamen Gram-Matrizen wurden am Code und an der Herleitung geprüft. Ein zweiter Gramaufbau verwendet die ursprüngliche vollständige alte Kopplungs-Grammatrix für die alte Wirkungsnorm. Er teilt weiterhin Rechenbausteine und analytische Voraussetzungen mit dem ersten Aufbau.

Die eigene Zertifikatsprüfung kontrolliert außerdem das geschlossene Manifest, die Bindung an unser vorheriges Prüfpaket, die Gram-Symmetrie, alle ausgewiesenen Loewner-Matrizen, die Normintervalle und die Quotienten der sichtbaren quadrierten Normen. Der vorherige Ganzzahlprüfbericht ist bytegleich eingebunden.

## Zusätzliche Aussage für beliebige Kombinationen der beiden Quellen

Die gelieferte Aussage über den kleinen sichtbaren Anteil betrifft jeweils einzelne Spalten. Daraus lässt sich mit den gemeinsamen Matrixzertifikaten eine Aussage für jede Kombination gewinnen.

Schreibe `B = B_E,scharf`. Für jede Parität sind nachgewiesen

\[
0\preceq G_{\mathrm{low}}\preceq B,
\qquad G_{\mathrm{full}}\succeq G_\perp\succeq\lambda_0 I_2.
\]

Wegen `B >= 0` gilt `B <= tr(B) I`. Also folgt

\[
G_{\mathrm{low}}\preceq
\frac{\operatorname{tr}B}{\lambda_0}G_{\mathrm{full}}.
\]

Die eigene rationale Rechnung bestätigt die konservativen strikten Schranken

\[
\frac{\|P_{\mathrm{low}}\mathcal R u\|_2^2}
     {\|\mathcal R u\|_2^2}
<\begin{cases}
1.1\cdot10^{-26}&\text{gerade},\\
5.7\cdot10^{-30}&\text{ungerade}
\end{cases}
\qquad(u\ne0).
\]

Es handelt sich weiterhin um L²-Anteile. Die Aussage liefert keinen entsprechenden Energiequotienten und erfasst nur die beiden festgehaltenen Quellen je Parität.

## Der nächste gezielte Rechenschritt

Jetzt müssen zwei gemeinsame 2×2-Matrizen auf denselben festgelegten Quellen zusammengebracht werden:

\[
K_{ij}=q_b(z_i-Jp_i,z_j-Jp_j),\qquad
W=\mathcal R^*Q_a^{-1}\mathcal R.
\]

Für die ausgewählten Quellenklassen gilt unter den bisherigen Formannahmen exakt

\[
S=K-W.
\]

Die Inversion benutzt die bereits zertifizierte alte Positivität. Die Positivität der neuen Gesamtform wird dabei nicht vorausgesetzt.

**Arbeitsvorschlag, noch kein neues Zertifikat:** Zuerst `K` mit gemeinsamen Fehlern einschließen und daran das benötigte Budget für `W` ablesen. Danach `W` unter voller Berücksichtigung der alten niedrigen und hohen Kopplung einschließen. Falls die gegenwärtigen Vorschläge dafür unbrauchbar sind, gezielte hohe Korrekturen konstruieren und ihren vollständigen Rest erneut bezahlen. Die bisherigen Vorschläge bleiben als Referenz erhalten.

Für eine gültige untere Matrix `K_minus` und obere Matrix `W_plus` wäre

\[
K_{\mathrm{minus}}-W_{\mathrm{plus}}\succeq\eta I_2,
\qquad\eta>0,
\]

ein klarer Erfolg für diesen ausgewählten Quellenblock. Ein positiver Block allein beweist noch keinen vollständigen Fortsetzungssatz. Die gesamte neue hohe Antwort und die vollständige Quotientenanbindung bleiben eigene Aufgaben.

Wenn die Reserve mit diesen Einschließungen nicht positiv wird, ist das zunächst ein offenes Rechenergebnis. Eine echte negative Richtung benötigt eine passende obere Einschließung des Schurwerts; breite Intervalle allein genügen dafür nicht.

## Weshalb der hohe Rest nicht einfach durch einen hohen Gap geteilt werden darf

Das L²-Komplement der 191 Profile muss kein invarianter Teilraum des alten Operators sein. Ein dort liegender Rest kann über die alte Kopplung empfindliche niedrige Richtungen anregen. Ein hoher Blockgap allein kontrolliert diese Rückwirkung nicht.

Ein kleines allgemeines Beispiel zeigt das Problem. Für

\[
Q=\begin{pmatrix}0.010001&0.1\\0.1&1\end{pmatrix},
\qquad r=\binom01
\]

ist `Q` positiv definit, der hohe Block gleich 1 und der niedrige Anteil von `r` gleich null. Trotzdem ist

\[
r^*Q^{-1}r=10001.
\]

Dieses Beispiel beschreibt keine gemessenen A8 Daten. Es erklärt ausschließlich, weshalb eine solche Division ohne Kopplungsnachweis mathematisch falsch wäre.

Mit dem übernommenen globalen A8 Boden `c_a = 1.2e-29` ist zwar `W <= G_full/c_a` gültig. Die Spuren unserer daraus gebildeten Obermatrizen liegen aber bei ungefähr 1.0783e27 und 2.2735e27. Das sind große **Obergrenzen**, keine Nachweise großer tatsächlicher inverser Energie. Sie zeigen, welche Information bei einer bloßen Verwendung des globalen Bodens verloren geht.

## Quellenbindung und Wiederholung

Originalpaket: `ObjektX_A8_Vollstaendige_Residuen_2026-10-04.zip`, 40 005 494 Bytes.

SHA-256: `2287538ae928d08dd459baa1d43586c0f47bd17a21ba05bdea98a7291a857754`.

Das Originalmanifest bindet 21 Dateien. Die Archive und der gelieferte Quellcode bleiben unverändert. Das kompakte Prüfpaket enthält die kleinen Ergebnisdateien, Prüfquittungen und den eigenen Zertifikatsprüfer. Die 114 MB große Funktionsdatei wird durch den Originalpaket-Hash und ihren Hash in der Rücklaufquittung gebunden und nicht erneut verpackt.

Der eigene Prüfer lässt sich mit dem unveränderten Original-ZIP wiederholen:

```text
python -B check_full_residual_certificates.py --package ORIGINAL.zip --out NEUE_PRUEFUNG.json
```

Der vollständige Paketrücklauf erfolgt im entpackten Originalverzeichnis:

```text
python -B reproduce.py --out ../NEUER_RUECKLAUF
```

Die Ausgabeziele müssen jeweils neu sein. `--audit-only` ersetzt keine vollständige Neuerzeugung.

GitHub und Registry wurden in dieser Prüfung nicht verändert.
