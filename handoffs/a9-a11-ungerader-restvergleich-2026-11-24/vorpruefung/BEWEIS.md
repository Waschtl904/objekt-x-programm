# A9 → A11 · Ungerader Gegenzeuge für die skalaren Young-Gewichte

23. November 2026, projektinterne bedingte Gegenrechnung. Grundlage ist der publizierte Git-Stand `18dd92f89f889c1f506673fefee33e4544b22038` von `Waschtl904/objekt-x-programm`.

## Ergebnis und Geltungsbereich

Auf dem physisch W-normierten ungeraden Grad-11-Zeugen aus #238 überschreitet die vollständige Vergleichsenergie der Variante mit endlichem Gewicht 51/50 das tatsächliche Budget um mehr als 2,10267 · 10⁻⁷. Für die ganze dokumentierte Familie skalarer Young-Gewichte verbleibt ein Ausschlussabstand von mehr als 5,07762 · 10⁻⁸. Fest sind die äußere Antwort, U8, der ursprüngliche Zwölferblock K, die ursprüngliche Matrix P_upper, Beta und die physischen Quellabbildungen. Die Aussage über die Familie betrifft ihre Majoranten. Die tatsächliche A9-Inverse und die exakte Inverse der zugrunde liegenden Unterform können kleinere Energien haben. Für die Veränderung der äußeren Antwort bleiben die gewichteten Antwort-/Residualpaarungen gesondert auszuwerten.

## Variationale Untergrenze

Sei n = J*ν der Vektor der 84 physischen Paarungen. In der Variationsformel für D = ⟨ν,R_Lν⟩ sind die Tests Jx zulässig. Mit E = L[J,J] gilt daher für jedes x die Abschätzung D ≥ 2 Re ⟨n,x⟩ − ⟨x,Ex⟩. Die acht T-Bedingungen wurden für sämtliche 84 ungeraden Basisspalten rational geprüft. Der Prüfer bildet E mit den 96 lokalen Legendrekoeffizienten der ungeraden Basis und den Gewichten H_k + 11/10. Jede absolute Zeilensumme liegt unter 6,237. Also gilt E ≤ 8I und die Wahl x = n/8 liefert D ≥ ‖n‖²/8.

Die alte 84er-Basis, ihr Anschluss an die physische Metrik, die Variationsformel für R_L und die Gültigkeit der gebundenen #238-Quellen- und Modellfehlerschranken sind Voraussetzungen. Der Prüfer überprüft die gebundenen Dateien und Archivmitglieder. Er verwendet die gemeinsame tatsächliche Quelle mit den Fehlerpreisen des ursprünglichen K. Der vierte Teilenergiekanal des Assemblers enthält den festen Vorfaktor 11/10. Deshalb wird ausschließlich für die Hilfsrechnung die positive Matrix (10/77)I eingesetzt. Einschließlich des Vorfaktors misst sie genau die quadratische Norm ‖n‖²/8. Diese Hilfsmetrik dient zur Fehlerkontrolle der 84 Paarungen. Die tatsächliche Vergleichsenergie verwendet die gespeicherte Teilenergie mit dem Gewicht 51/50.

In der Hilfsmetrik liegt die Modellenergie bei rund 1,89523963835 · 10⁻⁸. Vom unteren Endpunkt der Modellnorm werden der vollständige Feature-Normfehler (< 4,4290 · 10⁻¹¹) sowie der ganze Residualnormfehler (< 5,289 · 10⁻¹⁵) abgezogen. Quadrieren des positiven Rests ergibt D > 1,8952384 · 10⁻⁸. Das Verfahren liefert eine Untergrenze der vollständigen Dualenergie.

## Schluss für die Gewichte

Schreibe E(a,b) = C + b B + (a/β)D mit den unveränderten nichtnegativen Anteilen C und B. Für b₀ = 51/50 liefert das frühere Zertifikat eine gerichtete Untergrenze der Teilenergie E_part(b₀) = C + b₀ B. Mit a = 1000000/644683 ergibt sich gerichtet E(a,b₀) > 5,4910443 · 10⁻⁶. Das Budget liegt unter 5,2807765 · 10⁻⁶.

Für c = 6967/1000000 ist t = 1/(1−c) ≤ b₀. Die zulässigen Gewichte erfüllen a,b ≥ t. Da C,B,D ≥ 0 sind, folgt

    E(a,b) ≥ t (E_part(b₀)/b₀ + D/β).

Der Abstand der rechten Seite zum oberen Budgetendpunkt ist größer als 5,07762 · 10⁻⁸. Selbst die schwächere Rechnung mit t = 1 ergibt noch einen Abstand über 1,36312 · 10⁻⁸. Die exakten Endpunkte stehen in der JSON-Datei. Positive Abstände bedeuten hier, dass die Vergleichsenergie zu teuer ist.

## Reproduktion

Vorausgesetzt werden eine vollständige Arbeitskopie des angegebenen Projektstands einschließlich der gebundenen Archivdateien sowie Python mit `python-flint==0.9.0`. Der folgende Aufruf arbeitet mit 1024 Bit Intervallpräzision. Das optionale letzte Argument bezeichnet die Ergebnisdatei.

    python -B odd_dual_check.py PFAD_ZUR_ARBEITSKOPIE eigene_ergebnisse.json

Die Rechnung nutzt die gespeicherten Paarungen und ihre ursprünglichen Fehlerverträge. Sie wiederholt keine physische Hauptintegration. Gezielte externe Begutachtung bleibt offen.

## Quellen

- [Ursprüngliche ungerade Teilenergie und Zeugenbindung](https://github.com/Waschtl904/objekt-x-programm/blob/18dd92f89f889c1f506673fefee33e4544b22038/research/x-c1/w9-partial-energy-2026-10-18/expected/COMPARISON_odd.json)
- [Skalare Gewichtsfamilie und Gewicht 51/50](https://github.com/Waschtl904/objekt-x-programm/blob/18dd92f89f889c1f506673fefee33e4544b22038/research/x-c1/w9-majorant-preflight-2026-10-18/PROOF.md)
- [Variationsformel im Quelleninventar](https://github.com/Waschtl904/objekt-x-programm/blob/18dd92f89f889c1f506673fefee33e4544b22038/research/x-c1/w9-energy-inventory-2026-10-17/PROOF.md)
- [Variationale Basis84-Auswertung und Transport in einer positiven Hilfsmetrik am geraden Vorgänger](https://github.com/Waschtl904/objekt-x-programm/blob/18dd92f89f889c1f506673fefee33e4544b22038/research/x-c1/w9-dual-preflight-even-2026-10-20/PROOF.md)
