# Objekt X · Was entscheidet die feste Ritz-Route?

21. November 2026. Geprüfter GitHub-Stand `f84e357322c57e03d26daabcce03a3280d83be72`. Der Befund betrifft den festen geraden Zweiraum unter den im Projekt übernommenen physischen und analytischen Verträgen H1–H4.

**Ergebnis.** Ein rationaler Zeuge mit positiver physischer Vergleichsnorm und die erste signierte Paarung sind jetzt gerichtet eingeschlossen. Die Entscheidung über die zweite Energie und den Kreuzterm ist offen. Die gemeinsame Auswertung der zweiten Quelle auf der ganzen alten Schale fehlt. Hier gibt es einen endlichen Prüfer, die exakte Zielungleichung und einen präzisen Abbruchpunkt für weitere Arbeit.

## 1. Welcher Zeuge geprüft wurde

In der alten physischen Resttestsynthese sei die Reihenfolge Fₒ (12), ΛJ (84), äußere Richtungen im festen B-Koordinatenwechsel (12). Es gelten der ursprüngliche Momentlift, die physischen Kernanteile von Fₒ und die äußere rohe Koordinatenkonvention. Die Funktionen sind die festen gelifteten bzw. momentkorrigierten Formtests. Unter der übernommenen Identifikation der Bank liegt ihre endliche Linearkombination z in der Formdomäne. Die ergänzende 109. Koordinate des Zeugen ist null. Diese letzte Koordinate dient der Darstellung der ersten Quelle.

Für die Wahl des Zeugen wird M₀ auf die ersten 108 Koordinaten eingeschränkt. Die rechte Seite ist die gespeicherte Mittelpunktspalte t̂₂ minus λ̄₂ M₀w. Die Modellgleichung wird bei 120 Dezimalstellen gelöst. Einmaliges Runden auf das 10⁻³⁰-Gitter fixiert alle 108 Koeffizienten exakt. Die Definition ist die Liste in `witness.json` und a=1. Alle anschließenden Schranken verwenden diese rationalen Koeffizienten. Die große Skalierung einzelner Koordinaten macht es besonders wichtig, jeden Fehler im zugehörigen Funktional zu kontrahieren. Das Skript reproduziert die Auswahl aus einem gespeicherten Modell ohne neue physische Messung.

## 2. Physische Bank und endliche Einschließungen

M₀ ist die 109er-Modellmatrix. Unter der additiven ursprünglichen Fehlerbuchung gilt Mphys=M₀+Δrest+Δdir, −E ≤ Δrest ≤ E für E=Eupper−diag(old_row_majorant). Die symmetrisierten primitiven Eintragsradien r decken Δdir ab. Alle übrigen Fehlerpositionen bleiben in E. Grundlage ist die physische Bankidentifikation aus dem Erstspaltennachweis. Die 109. Spalte enthält t₁ auf den 108 Testkoordinaten. Die additive Herleitung dieser Buchung ist eine übernommene Voraussetzung. Eine positive Modellmatrix allein rechtfertigt sie nicht.

Für rationale x,y ist der bilineare Fehler höchstens

    B(x,y) = √((xᵀEx)(yᵀEy)) + |x|ᵀr|y|.

Dies folgt aus der beidseitigen Formordnung durch Cauchy–Schwarz in der E-Metrik und der Dreiecksungleichung für die Direktintervalle. Die Quadratwurzel wird mit einem ganzzahligen Wurzelverfahren nach oben gerundet. Für x=y wird der erste Term exakt verwendet. Es seien h=e₁₀₉−λ̄₁w, N=S_R[z,z] und pᵢ=η̄ᵢ[z]. Bei Verwendung der 109er-Bank werden w und z mit null ergänzt.

| Größe | Ergebnis |
|---|---|
| N = zᵀMphys z | [0,08876424931; 0,08878562299] |
| p₁ = zᵀMphys h | [−0,000011244470; +0,000011244470] |
| Betrag p₁/√N | < 0,000037742 |
| p̂₂ = t̂₂[z]−λ̄₂ zᵀM₀w | 0,0887749361506717… (Modellwert) |
| Bekannter Fehleranteil in p₂ bei festem t₂[z] | < 0,000000079542 |
| ℓ[z] im Modell | rund −4,51·10⁻³² |

Genauer gilt p₂−p̂₂=(t₂[z]−t̂₂[z])−λ̄₂ zᵀ(Mphys−M₀)w. Die Eingänge liefern für den letzten Summanden die angegebene gerichtete Schranke. Ein Preis für den ersten Summanden steht aus. Somit bleiben auch p₂²/N und p₁p₂/N physisch offen. Alle exakten Rechenresultate stehen als nach außen gerundete rationale Intervalle in `bounds.json`. Die Modellquotienten dienen nur zur Orientierung.

## 3. Eine hinreichende Entscheidung für denselben Zeugen

Für ℓ=η̄₂−S_R[z,·], D=‖ℓ‖² im S_R-Formdual und δ=ℓ[z] gelten im reellen Raum exakt

    R̄₂₂ = N + 2δ + D,
    R̄₁₂ = p₁ + ⟨η̄₁,ℓ⟩ ≥ p₁ − √(uD),     u = 0,0000035227.

Die erste Gleichung entsteht durch Ausmultiplizieren, die zweite durch Cauchy–Schwarz und die bestehende ganze Schranke für die erste Restspalte. Die orthogonale Restenergie ist infₐ ‖η̄₂−a S_R[z,·]‖² und daher höchstens D. D selbst gehört zum festgelegten a=1.

Der bisherige Plan Q≤0,00924 verlangt zusätzlich p₂²/N≤0,089 und p₁p₂/N≥−0,000010. Weiterhin möglich ist folgende hinreichende Auswertung derselben festen Richtung. Sie nutzt die zwei Identitäten unmittelbar und benötigt keine separat bewiesenen Quotienten. Wähle D≤0,0109. Dann ist R̄₁₂ ≥ −0,000207197092 > −0,00020740. Für R̄₂₂≤0,1 genügt δ≤0,0001571885051. Alle Aussagen in diesem Absatz sind Implikationen.

Setze y=λ̄₂w+z und ε₂(z)=t₂[z]−t̂₂[z]. Dann ist δ=δ₀+ε₂(z)−zᵀ(Mphys−M₀)y. Der Fehler des letzten Terms ist B(z,y)<0,000010610937. Damit genügt als einfaches **einseitiges** Ziel ε₂(z)≤0,00014. Zusammen mit D≤0,0109 ergäbe dies R̄₂₂<0,099987. Beide Zielvoraussetzungen sind offen. Die arithmetischen Radien der gespeicherten zweiten Spalte decken deren physische Modell- und Integrationsfehler nicht ab.

## 4. Die vier Bilder des ganzen Funktionals

Für den Vergleich nach der alten Kernelimination schreibe S_R=D_R−H*U_s H und t₂=f_R,₂−H*U_s g₂. Im Folgenden bezeichnet D_R die direkte Restform, D die oben definierte Zahl. Für jeden zulässigen Resttest v gilt

    ℓ[v] = f_R,₂[v] − D_R[y,v] − ⟨Hv, U_s(g₂−Hy)⟩.

Dies stellt alle Terme mit derselben Quelle und demselben y vor jeder Normmajorisierung zusammen. Definiere p_F,p_J,p_B durch Auswertung dieses Ausdrucks auf den gebundenen Fₒ-, ΛJ- und rohen äußeren B-Tests. Für einen alten Schalentest Λτ definiert dieselbe Zeile den rohen Schalenkovektor, mit der ursprünglichen Momentkorrektur. Auf ihn wirkt P_T^W W⁻¹. Sein Bild heiße p_T. Damit lauten die vier Vergleichskarten

    A_Fℓ = p_F,                              Metrik K_neu⁻¹
    A_Tℓ = p_T − a_mix* K_neu⁻¹ p_F,          Metrik R_L
    A_Pℓ = p_J − a_J* K_neu⁻¹ p_F,            Metrik P
    A_Sℓ = p_B − Y_F* p_F − Y_J* p_J,         Metrik C_g⁻¹.

Dabei ist a_J=a_mix J84. Die Ganzschalenkarte setzt den rohen L²-stetigen Schalenkovektor voraus. Für f_R,₂ liefert die dokumentierte Formschnittstelle die feste geliftete Polynomquelle und den Momentterm. Für den direkten Anteil D_R[y,Λτ] darf die Form auf die festen stückweise glatten Bankfunktionen gelegt werden. Für den inversen Anteil wird nur der beschränkte Schalenadjunkt G₈* auf die Hilbertfunktion U_s(g₂−Hy) gebraucht. Die Formeln sind bedingt auf die Domänen-, Identifikations- und Schnittverträge der Projekttexte anwendbar. Weder ein Abschneiden des Kernraums bei 191 Koordinaten noch eine starke A9-Anwendung auf eine inverse Antwort kommt darin vor.

Im übernommenen Vergleich gilt D ≤ (25/21) Q, wobei

    Q = ‖A_Fℓ‖² + 10‖A_Tℓ‖² + (11/10)‖A_Pℓ‖² + ‖A_Sℓ‖²

jeweils in der rechts angegebenen Metrik zu lesen ist. Für D≤0,0109 genügt Q≤0,009156. Daraus folgt als notwendige Teilbedingung für diesen konkreten Preis ‖A_Tℓ‖²_(R_L)≤0,0009156. Eine kleine T-Schranke allein würde den Vergleich nicht schließen.

## 5. Was in der Fehlerrechnung offen bleibt

| Teil | Zu kontrollierende Größe |
|---|---|
| Endliche zweite Quelle | Gemeinsame gerichtete Fehler in den direkten F/J-Paarungen, im Rohblock B*(d−P₀*g), im hohen Kernterm und in Vᵀzq. Vor Summation zuerst mit demselben z kontrahieren. Dies liefert ε₂(z) und die endlichen q-Anteile der vier Bilder. |
| Ganze alte Schale | Auf 3 log(2)/2 < x < log(3) den gemeinsamen Modellvertreter von f_R,₂−D_R[y,·]−H*U_s(g₂−Hy) bilden. Die nativen 17 Kernstücke enden am linken Rand. Auf dieser Schale braucht man die richtigen Prim-/Logzweige, Endstreifen, Momentkorrektur, die Kern-zu-Schale-Wirkung und den F-Abzug der T-Karte. |
| Übergang Modell → physisch | N-Projektion, Momentlift, Gamma- und Basisabweichungen, hohe und niedrige Kernantwort, direkte Paarungen, Integrations- und Speicherradien unter den tatsächlichen Koeffizienten. Vorhandene Kosten dürfen bei identischem Geltungsbereich einmal übernommen werden. Die Fehler des q-Modells gehören zusätzlich zur 109er-Bank. |
| Vergleichsmetriken | K_neu, P, C_g und R_L in ihren gebundenen Normen einschließlich a_mix-, a_J-, gegebenenfalls κ- und P₀-Transport. Für angenäherte Inversen/Karten werden gerichtete Unsicherheiten benötigt. Die exakten rationalen B- und Y-Karten benötigen keinen pauschalen Zusatzpreis. |

Ein zulässiger Abschluss wäre beispielsweise eine Einschließung der vier gemeinsamen Modellbilder mit Normen b_j und sämtlichen Transport-, Modell- und Integrationsfehlern e_j in derselben physischen Metrik. Dann gilt Q ≤ Σ_j Gewicht_j (b_j+e_j)². Schärfere gemeinsame Gramabschätzungen sind möglich. Für das ganze T-Bild fehlt aus den gesichteten Daten schon b_T als gerichtete Zahl. Die 84 J-Paarungen bestimmen eine Funktion auf dem ganzen T nicht. Ein zusätzlicher Anteil, der auf diesen Tests verschwindet, bleibt durch diese Paarungen allein unbeschränkt. Das ist eine Aussage über die Reichweite des Tests und kein Gegenbeispiel zur konkreten arithmetischen Quelle.

**Entscheidung.** Aus dem vorhandenen Material ergibt sich kein physischer Zweiraumnachweis. Ein großer neuer Lauf ist derzeit nicht begründet. Zuerst braucht es die hergeleitete Darstellung mit quantitativer Kontrolle des ganzen T-Rests, einschließlich des Modells selbst, sowie die signierte zweite Quellenpaarung. Ein bereits zu grober oberer Preis entscheidet nur über die Eignung dieser Abschätzung. Für einen Ausschluss wären eine tatsächliche untere Schranke oder ein anderer Unmöglichkeitsbeweis nötig.

## 6. Reproduktion und Quellen

Nach dem Entpacken `python replay.py` ausführen (Python 3.11 oder neuer, Standardbibliothek). Der Prüfer kontrolliert sechs Eingangshashes, reproduziert den Zeugen, sämtliche ausgegebenen rationalen Intervalle und die beiden bedingten skalaren Schurböden des Übergangs A8→A9. Er erzeugt keine neuen Integrale. `belege/` enthält die Herleitungen zum Nachlesen und die Resultate der gesonderten Wiederholung der q-Hashprüfung gegen das kombinierte Original sowie der 256×2 Budgetprüfung.

[GitHub-Stand](https://github.com/Waschtl904/objekt-x-programm/tree/f84e357322c57e03d26daabcce03a3280d83be72) · [Ritz-Original](https://github.com/Waschtl904/objekt-x-programm/tree/f84e357322c57e03d26daabcce03a3280d83be72/handoffs/ritz108-review-2026-11-19) · [Vergleichs- und Budgetgrundlagen](https://github.com/Waschtl904/objekt-x-programm/tree/f84e357322c57e03d26daabcce03a3280d83be72/research/x-c1/november-integration-2026-11-11)
