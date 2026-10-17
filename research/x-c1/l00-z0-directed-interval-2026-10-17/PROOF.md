# Erstes vollständiges Intervall für L₀,₀ auf z₀

17.10.2026 · AUTHOR_DERIVED · EXTERNAL_REVIEW_OPEN

## Aussage und Voraussetzungen

Unter den unveränderten Operator-, Domänen-, Quellenmodell- und Integrationsvoraussetzungen der gebundenen Stufe-1-, Stufe-3-, Hochantwort-, K_P-, Transport- und C_p-z₀-Pakete gilt für die dort festgelegte Regel X_fix und die exakt W-normierte konstante neue Schalenrichtung z₀:

| Parität | nach außen gerundetes Intervall für L₀,₀ | gebundene hinreichende Ausschlussschwelle |
|---|---:|---:|
| gerade | [−407,736; 401,497] | 980,113997 |
| ungerade | [−2,646; 11,832] | 398,766496 |

Dabei ist L₀,₀=⟨χ_p,(C_p−D̂T)z₀⟩, T=X_fix F̂. F̂ und D̂ sind die eingefrorenen physischen Funktionsmodelle. Das tatsächliche k ist berücksichtigt. Die Intervalle liegen vollständig innerhalb der genannten Schwellen. Dieser gebundene Skalartest mit z₀ schließt die Regel nicht aus. Daraus folgen weder ein vollständiger N12-Energievergleich noch eine Bestätigung der Regel, A9→A11 oder Objekt X.

Die ursprünglichen großen Quellenintegrationen werden als gebundene Voraussetzungen übernommen; dieser Prüfer ersetzt ihre externe mathematische Begutachtung nicht. Er erzeugt die hier neu benötigten ganzen Integrale mit gerichteten Resten. Die früheren numerischen hohen Paarungen und die grobe y_f-Quadratur werden nicht als Schranken benutzt.

## 1. Festes Residuum und Modellzentrum

Setze a₈=3log(2)/2, a=log(3), b=log(11)/2, σ=0 oder 1, ε=(−1)^σ und m(x)=cosh(x/2) bzw. sinh(x/2). Alle physischen inneren Produkte haben Maß 2dx. Mit μ_H=∫₀ᴴm², L=∫ₐᵇm und

    B=[2(b−a+L²/μ_a)]^(−1/2), A_c=−BL/μ_a

ist der Lift von z₀ gleich A_c m im Kern und ±B auf den beiden neuen Schalen. Die elementare Quelle c̃ ist exakt die in `gpt2-cp-z0-quelle` gebundene Darstellung mit Θ, J₊, J₋ und den sieben Primkanälen. Die zwölf inneren Schnittstellen werden als Zellgrenzen benutzt. Sie liegen alle vor a₈.

Mit r=c̃−D̃Tz₀ gilt h=Π_a r und h₈=Π₈r|Kern. Eine zusätzliche Modellunsicherheit h−h₀ wird hier nicht eingeführt: Es werden genau die ganzen eingefrorenen Funktionen integriert. Die Fehler D−D̂ der tatsächlichen Antwortregel gehören zum späteren Vergleich und sind bereits in den übernommenen Ausschlussschwellen bezahlt.

Das Modellzentrum ψ₀ stammt aus den **gerichteten** Koeffizientenboxen von `PSI_CORRECTED.json`, einschließlich des μ₈-Kernlifts. c₀ stammt aus den vollständigen Boxen `FINITE_ACTION.c_model`, nicht aus gerundeten Anzeigen. Für die Kernfunktionen Φ_j=e_j−β_j e_σ gilt ⟨Φ_j,m⟩=0. Daher werden ohne Differenz großer projizierter Funktionen berechnet:

    m_r=∫₀ᵃ r m, m_c=∫₀ᵃ⁸ r m,
    ‖h‖²=2(∫₀ᵃr²−m_r²/μ_a),
    ‖h₈‖²=2(∫₀ᵃ⁸r²−m_c²/μ₈),
    Φ*h₈=(2∫₀ᵃ⁸Φ_j r)_j,
    I₀=2(∫₀ᵃψ₀r−m_r∫₀ᵃψ₀m/μ_a)−c₀*Φ*h₈.

Die β_j und die entsprechenden vier z-Quellen werden aus der positiven sphärischen Besselreihe für die Mellinmomente bestimmt. Nach 159 Folgetermen wird der Rest durch den nächsten Term und eine geometrische Reihe eingeschlossen. Die Quotienten der folgenden Terme nehmen ab. Sämtliche Wurzeln, Logarithmen, Exponentialfunktionen, Koeffizienten und Summen werden mit Arb bei 800 Bit ausgewertet.

## 2. F̂z₀ und Tz₀ einschließlich Integrationsrest

Die physische W-Rieszfunktion hat die gebundene Form

    [P(v)+Q(v)log((v+1)/(v−1))+c_phys m(av)]/sqrt(2a), v=y/a.

Mit u=v−1∈[0,s], s=b/a−1, ist der W-Faktor 1+(L/μ_a)m(a(1+u)). Wir zerlegen log((2+u)/u)=log2+log(1+u/2)−logu. Log(1+u/2) und die Hyperbelfunktion werden bis Grad N=120 entwickelt; gleichmäßige Reste sind

    e_log ≤ (s/2)^(N+1)/[(N+1)(1−s/2)],
    e_m ≤ exp(b/2)(as/2)^(N+1)/(N+1)!.

Für ein Polynom A sei |A|_s=Σ|A_k|s^k. Mit A=P+Q(log2+LogTaylor)+c_phys M, W_T=1+(L/μ_a)M gelten e_f=|Q|_s e_log+|c_phys|e_m und e_W=|L/μ_a|e_m. Der Fehler des Produktintegrals wird durch

    s e_f sup|W| + s e_W (|A|_s+|Q|_s(1−log s))

begrenzt (0<s<1). Das folgt aus fW−f_TW_T=(f−f_T)W+f_T(W−W_T) und ∫₀ˢ|logu|du=s(1−log s). Die verbleibenden Polynom- und Polynom×Log-Momente werden exakt symbolisch mit Arb-Koeffizienten integriert. Multiplikation mit 2Ba/sqrt(2a) und dem exakten rationalen X_fix transportiert alle Fehler nach Tz₀.

## 3. Gerichtete Quadratur auf vollständigen Zellen

Auf den 13 Kernzellen werden 512 Gauss-Legendre-Knoten benutzt. Die alte Schale (a₈,a) wird in 160 dyadische Zellen mit je 128 Knoten und ein verbleibendes Endstück zerlegt. Arb liefert Einschließungen der Legendre-Nullstellen und positiven Gewichte.

Auf einer Zelle [c−d,c+d] wird die Bernsteinellipse ρ=2 benutzt. Sie liegt im Rechteck |Re(x−c)|≤5d/4, |Im(x)|≤3d/4. Das Programm prüft, dass dieses Rechteck strikt innerhalb −a<Re x<a liegt. Damit haben a±x und b±x positive Realteile. Alle verwendeten Logarithmen sowie atanh(exp(−(a±x)/2)) und atan derselben Argumente sind dort analytisch: die Exponentialargumente liegen strikt in der Einheitskreisscheibe. Die gewählte Prim-/Translationsformel wird auf jeder Zelle analytisch fortgesetzt; Sprünge liegen ausschließlich auf Zellgrenzen.

Sei M eine komplexe Arb-Majorante des Integranden auf diesem ganzen Rechteck. Die Chebyshev-Koeffizienten erfüllen |a_k|≤2Mρ^(−k). Abschneiden nach Grad 2n−1 liefert einen gleichmäßigen Rest ≤2Mρ^(−2n)/(1−ρ^(−1)). Integral und positive Gaussregel haben jeweils Norm 2d; die Regel ist bis Grad 2n−1 exakt. Folglich gilt

    |Integral−Gauss_n| ≤ 8d M ρ^(−2n)/(1−ρ^(−1)).

Dieser Rest wird für **jeden** benötigten Integranden addiert, einschließlich aller 191 Φ-Koordinaten, Normquadrate und Quellenpaarungen b_F. Keine Netzverfeinerungsdifferenz dient als Fehlergrenze. Endpunkte und Zelllängen selbst sind Intervallgrößen; Arb schließt ihre Verwendung ein.

## 4. Vollständiger logarithmischer Endpunktrest

Für d=(a−a₈)2^(−160), t=a−x∈(0,d), wird das ganze Residuum als r=G(x)logt+H(x) zerlegt. Mit D_V als aggregiertem V-Multiplikator gilt

    G(x)=(B−A_c m(x))/2+D_V(x/a)/(2sqrt(2a)).

Die regulären Teile von J₊, J₋, Θ werden durch Herausziehen von −logt/2 eingeschlossen. Dabei werden die positiven Quotienten durch

    (1−exp(−2t))/t ∈ [2exp(−2d),2],
    (1−exp(−t))/t ∈ [exp(−d),1],
    (1−exp(−t/2))/t ∈ [exp(−d/2)/2,1/2]

begrenzt. Alle übrigen Terme sind regulär auf [a−d,a]. Mit den so berechneten G_max,H_max gelten

    ∫|r| ≤ d[H_max+G_max(1−logd)],
    ∫r² ≤ 2d[H_max²+G_max²(log²d−2logd+2)].

Multiplikation mit den jeweiligen gleichmäßigen Schranken für ψ, m, z_i und Y_j schließt sämtliche fehlenden Endpunktintegrale ein. Kernkoordinaten haben auf diesem Endstück keinen Träger. Das Endstück wird also nicht einfach weggelassen.

## 5. Ganzes Fehlerbudget für die tatsächliche Quelle

Aus dem gebundenen Hochantwortpaket, Gleichung (7.1), und der Stufe-1-Identität ψ−ψ₀=−F(k−k₀) folgt

    |L₀,₀−I₀| ≤ Eψ+Ec+R,
    Eψ=sqrt(b_F*G_p b_F), G_p=η_p²K⁻¹,
    Ec=(e_fixed+e_k)/sqrt(1−rho) · ‖C*Φ*h₈‖,
    R=H_hi,p‖h₈‖.

k₀ wird byte-/rationalgleich mit dem Zentrum der ψ-Koeffizienten geprüft. Für b_F werden die ersten vier momentfreien z_i direkt mit r gepaart. Für die acht gelifteten Schalenquellen gilt

    (b_F)_(4+j)=2[∫ₐ₈ᵃY_j r−(∫ₐ₈ᵃY_j m)m_c/μ₈].

C ist die gebundene rationale Kongruenzmatrix; der Faktor 1/sqrt(1−rho) bleibt erhalten. e_fixed umfasst die gebundenen Modell-/Quellen-/Gammafehler bei festem k₀; e_k den tatsächlichen k-Fehler in den endlichen Antwortfeatures. H_hi umfasst bereits die **ganze** hohe Antwort, alle Quellen-/Kopplungsfehler, tatsächliches k und den physischen Momentlift. Es wird keine hohe Legendre-Summe abgeschnitten.

Das frühere zusätzliche e_ψ‖h‖ wird durch Eψ ersetzt. Die konservative Dreiecksungleichung zwischen ψ-, endlichem und hohem Antwortfehler ist auch bei korrelierten Daten gültig. Sie behauptet keine unabhängigen Fehler und keine volle kohärente U₈-Transportrechnung. Derselbe k-Unsicherheitskörper wird einmal als Eingabe verwendet; seine Beiträge in den verschiedenen Summanden werden konservativ separat majorisiert.

| Fehlerquelle | gerade (aufgerundete Obergrenze) | ungerade (aufgerundete Obergrenze) |
|---|---:|---:|
| I₀: Koeffizienten, Rundung, F̂-/T-Rest, alle Quadratur- und Endpunktreste zusammen | 10⁻¹² | 10⁻¹² |
| kohärenter ψ-k-Anteil Eψ | 0,000355 | 0,000017 |
| endliche Antwort Ec | 99,538585 | 0,514378 |
| ganze hohe Antwort R | 305,076732 | 6,723795 |

Die JSON-Dateien geben zusätzlich Ec getrennt nach fixed-k- und k-change-Anteil sowie die tatsächlich berechnete I₀-Intervallbreite aus. Die erste Tabellenzeile ist eine gemeinsame Einschließung, keine Annahme unabhängiger Koeffizienten- oder Quadraturfehler. Sämtliche normabhängigen Budgetterme verwenden ebenfalls gerichtete Normintervalle.

Es folgt ein symmetrischer Radius um das **I₀-Modellzentrum**, ohne Verschiebung durch eine numerische Schätzung des hohen Restes. Die rationalen Endpunkte in `expected/` entscheiden; die Tabelle am Anfang rundet diese nach außen. Das Modellkorrekturbudget beim Übergang D̂→D ist getrennt in der übernommenen Schwelle enthalten und wird hier nicht ein zweites Mal in L₀,₀ eingerechnet.

## 6. Reproduzierbarkeit und Grenzen

`INPUT_BINDINGS.json` bindet alle direkt verwendeten Dateien und die vorbereiteten acht Eingaben. Der Vorbereiter prüft die gebundenen Originalarchive vor dem Extrahieren. `verify.py` prüft zusätzlich die eigenen Hashes, erzeugt beide Zertifikate neu und fordert bytegleiche JSON-Ausgaben. Die exakte externe Version ist python-flint 0.9.0. Ein Replay bestätigt Reproduzierbarkeit; die externe Prüfung dieser Herleitung bleibt offen.
