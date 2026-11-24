# A9 → A11 am festen ungeraden Zeugen

24. November 2026 · Projektinterne Herleitung · Externe Prüfung offen

Der gekoppelte Untervergleich besteht die endliche Vorprüfung. Seine vollständige Inversenergie am Zeugen liegt unter dem Budget, **falls** die tatsächliche ungerade Restquelle auf dem ganzen alten Raum die Schranke `d ≤ 8,1·10⁻⁹` erfüllt. Diese letzte Voraussetzung bleibt offen.

## Ergebnis

| Größe | Gerichteter Befund |
| --- | ---: |
| Neuer rationaler Zwölferblock | Alle zwölf führenden Hauptminoren von Kₒ − K_alt strikt positiv |
| Variationswert einschließlich Basisenergie | 5,205068139790·10⁻⁶ < F < 5,206736691454·10⁻⁶ |
| Unteres Zeugenbudget | K_P[eₒ] > 5,280776435141·10⁻⁶ |
| Budgetuntergrenze abzüglich oberem F-Endpunkt | > 7,40397·10⁻⁸ |
| Endliche gewichtete Restnorm z | < 8,558·10⁻⁸ |
| Voller Inverspreis unter der Voraussetzung d ≤ 8,1·10⁻⁹ | < 5,280273126·10⁻⁶ |
| Abstand zur Budgetuntergrenze unter derselben Voraussetzung | > 5,03309·10⁻¹⁰ |

## Unterform und Zeuge

Alle Eingaben stammen aus den ungeraden Falldaten. Aus den gebundenen Matrizen des gemeinsamen 96-Spalten-Nachweises seien U_F der Modellgram, E_F die ganze Fehlermatrix der zwölf F-Quellen, G_F die Koordinatenmetrik und D_F,− die direkte Untergrenze. Für jedes rationale ε > 0 gilt durch Quadratergänzung

    K_ceiling = D_F,− − (1+ε) U_F − (1+1/ε) E_F ≤ K_tatsächlich.

Der Prüfer wählt ε als auf das 10⁻⁴⁰-Raster gerundete Quadratwurzel des Quotienten tr(G_F⁻¹ E_F)/tr(G_F⁻¹ U_F). Er schließt die symmetrischen Einträge von K_ceiling ein und zieht vom rationalen Mittelpunkt die jeweilige Zeilensumme der Radien sowie 10⁻⁶⁰ auf der Diagonalen ab. Die zwölf exakt rationalen Determinanten zeigen K_alt < Kₒ. Die Zeilensummenabschätzung gibt Kₒ ≤ K_ceiling. In der unergänzten alten Form wird allein der Zwölferblock erhöht. Für die zugehörigen vollständigen unteren Formen folgt Q_alt ≤ Qₒ ≤ A₉. Die Positivität, die Domänen und die Ordnung Q_alt⁻¹ ≤ W₉ stammen aus der alten Zertifikatskette. Damit gilt für diese konkrete neue Inversmajorante

    A₉⁻¹ ≤ Qₒ⁻¹ ≤ Q_alt⁻¹ ≤ W₉.

Der äußere W-normierte Zeuge, die äußere Antwort und das Budget stammen aus derselben gebundenen Falldatei wie beim früheren Ausschluss. Der frühere Hochraumboden überträgt sich, wenn der projektinterne Nachweis des Bodens und seine Voraussetzungen gelten. Der hier berechnete Inversvergleich verwendet keine Information über die A11-Zielpositivität.

## Variationswert und ganze Restquelle

Schreibe u = Jw. Der Prüfer löst das symmetrisierte ungerade Mittelpunktproblem in den 84 Koordinaten einmal und friert w mit rationalen Einträgen auf dem 10⁻⁵⁰-Raster ein. Alle folgenden Zahlen bewerten diesen festen Vektor. Mit h als Kernquelle, v als ergänzter Zwölferquelle, g als Kernkopplung, a als tatsächlichem Zwölfer-Kreuzblock, q als direkter Form und η = 10⁻¹⁰ gilt in der alten Formdomäne

    νₒ = Λ_T* f − g* U₈ h − a* Kₒ⁻¹ v,
    Hₒ = (1−η)q − g* U₈ g − a* Kₒ⁻¹ a,
    F = ⟨h,U₈h⟩ + ⟨v,Kₒ⁻¹v⟩ + 2 Re νₒ[u] − Hₒ[u],
    rₒ = νₒ − Hₒ u,
    ⟨f,Qₒ⁻¹ f⟩ = F + ⟨rₒ,Hₒ⁻¹ rₒ⟩.

Insbesondere lässt sich die auszuwertende **ganze** Quelle für jeden alten Resttest t so schreiben, mit antilinearer erster Stelle,

    rₒ[t] = ⟨Λ_T t,f⟩ − (1−η)q[t,u]
            − ⟨g t,U₈(h−g u)⟩ − ⟨a t,Kₒ⁻¹(v−a u)⟩.

Die Ergebnisdatei enthält auch zwölf rationale Mittelpunkte für die gemeinsam gebildete Kraft v−a u. Ihr Fehler in der Kₒ⁻¹-Norm enthält den v-Featurefehler, den physischen Quellenfehler, den Fehler der Kreuzwirkung auf u und die Rundung. Die koordinatenweise gespeicherte Kraft ist vor der Anwendung von Kₒ⁻¹ zu lesen.

Für F wird die Basisenergie als gemeinsame Gramnorm eingeschlossen. Die Paarung νₒ[u] benutzt den positiven Ausgabegram ww*. Für die direkte quadratische Form wird (D_plus−D_minus)/2 in Richtung w ausgewertet. Der U-Preis in dieser Richtung ist 2√(u_w e_w)+e_w aus Modellenergie und Fehlerenergie. Die F–J-Kreuzkorrektur enthält die ganze Fehlergrammatrix einschließlich des historischen Hochquellenfehlers. Der Term ηq[u] wird einmal eingeschlossen, die Untergrenze q[u] ≥ 0 zusätzlich aus der gerichteten direkten Matrix geprüft.

## Endliche Restnorm und offene Ganzraumbedingung

Für den endlichen Preis wird die vorhandene ungerade Obermatrix P_upper benutzt. Bei festem inneren Antwortoperator X wächst die innere Energiematrix um diag(0,Kₒ−K_alt). Daher gilt X E_neu⁻¹ X* ≤ X E_alt⁻¹ X* ≤ P_upper. Aus demselben Grund bleibt die ursprüngliche ungerade Kontraktionsschranke mit c = 6967/10⁶ gültig. Die neue Quelle und ihr Kreuzblock enthalten jeweils Kₒ⁻¹.

Der Prüfer schließt z = ‖P_upper^(1/2) J* rₒ‖ mit den ungeraden gemeinsamen Daten ein. Auf den Modellvektor J*νₒ,0 − H₀ w + η D_J,0 w werden die Fehler der Quelle, der direkten Wirkung, der U-Wirkung und der vollen quadratischen Kreuzblockwirkung addiert. Die drei Produkte der beiden Kreuzblockfehler werden wie in § 3 der unten verlinkten Herleitung eingeschlossen. Im JSON steht jeder Fehlerbeitrag separat.

Mit β = 20209999981781/182190000000000 und d = ⟨rₒ,R_L rₒ⟩ auf dem ganzen T liefert die alte Inversabschätzung für die neue Quelle

    ⟨f,Qₒ⁻¹ f⟩ ≤ F_oben + (d/β + z_oben² + 2 z_oben √(c d/β))/(1−c).

Der rechte Ausdruck wächst mit d. Beim abgesicherten z-Endpunkt und der Budgetuntergrenze liegt seine Gleichheitsgrenze bei ungefähr 8,1554408033·10⁻⁹. Der einfach gerundete Zielwert 8,1·10⁻⁹ lässt einen strikt positiven Abstand. Einen Weg zum genügenden Nachweis bietet auch ein tatsächlicher W_X-Hilbertvertreter r mit Norm höchstens 0,0001844. Aus L ≥ (21/5)W_X auf T folgt dann d ≤ (5/21)‖r‖² < 8,1·10⁻⁹. Bei direkter Arbeit im Formdualraum ist dieser Umweg über die Hilbertnorm entbehrlich.

Die alte Untergrenze 1,8952384·10⁻⁸ galt der ursprünglichen Quelle ν bei ursprünglichem K. Hier wird eine andere Quelle nach der Subtraktion Hₒu und dem Wechsel auf Kₒ geprüft. Die 84 Paarungen liefern keine Ganzraumobergrenze für d. Für die physische Rechnung fehlen in diesem Paket die gerichtete ungerade Einschließung des ganzen gemeinsamen Felds und der Anschluss seiner Modellfehler. Der gerade Feldaufbau verwendet gerade Fortsetzung und cosh als Momentprofil. Der ungerade Anschluss benötigt die Spiegelvorzeichen, sinh als Momentprofil und die passenden Quellen- und Randfehler. Auch nach einem positiven Einzelzeugentest bleibt der volle Quotienten-Schurvergleich für Punkt 4 offen.

## Reproduktion

`python endpunkte.py` prüft die Schlussungleichung mit exakten Brüchen ohne Zusatzpakete, einschließlich der Richtung beim Quadrieren. Der vollständige numerische Replay benötigt Python mit python-flint 0.9.0 und eine lokale Kopie des Projekts mit den gebundenen Quelldateien im Original-Byteformat. Der Referenzcommit lautet `18dd92f89f889c1f506673fefee33e4544b22038`. Bei Windows-Checkouts ist eine automatische LF-zu-CRLF-Umwandlung der Eingabedateien zu vermeiden. Aufruf im entpackten Prüfpaket:

    python odd_coupled_24.py PFAD_ZUM_REPOSITORY replay.json

Der Prüfer arbeitet mit 1024 Bit Arb-Präzision, verifiziert die gebundenen Eingabebytes und berechnet Kₒ, den Zeugenwert, die endliche Restnorm und die bedingte Schwelle neu. Die ursprünglichen physikalischen Integrale, die alte Ordnung und die Domänenbeweise gehen als Projektvoraussetzungen ein. Die historische Vorprüfung vom 23. November ist mit Prüfer, Beweis und Endpunkten als unverändertes ZIP beigefügt. Beide Rechnungen lassen sich getrennt reproduzieren.

### Commitgebundene Grundlagen

- [Ursprüngliche ungerade Zeugendaten und gemeinsame Energierechnung](https://github.com/Waschtl904/objekt-x-programm/tree/18dd92f89f889c1f506673fefee33e4544b22038/research/x-c1/w9-partial-energy-2026-10-18)
- [Matrixunterform und Ordnung nach Erhöhung des Zwölferblocks](https://github.com/Waschtl904/objekt-x-programm/blob/18dd92f89f889c1f506673fefee33e4544b22038/research/x-c1/w9-matrix-error-selection-2026-10-20/PROOF.md)
- [Gekoppelte Restabschätzung und gerichtete Fehler der Formwirkung](https://github.com/Waschtl904/objekt-x-programm/blob/18dd92f89f889c1f506673fefee33e4544b22038/research/x-c1/w9-residual-centered-control-even-2026-10-21/PROOF.md)
- [Alte Inversmajorante und Metrik auf T](https://github.com/Waschtl904/objekt-x-programm/blob/18dd92f89f889c1f506673fefee33e4544b22038/research/x-c1/a9-inverse-renewal-2026-10-13/original/HERLEITUNG.txt)
