# Tatsächliches K_P für zwei festgefrorene Schalenrichtungen

17.10.2026 · **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.

**Nachtrag desselben Tages:** §8 verschärft zusätzlich das hohe Paarungsbudget.
Damit entscheidet sich der ungerade Test als Nichtausschluss; der gerade Test
bleibt unentschieden. §§1–7 dokumentieren die erste K_P-Rechnung mit den noch
unveränderten L-Intervallen, deren Resultate und Dateien erhalten bleiben.

## 1. Aussage und Abgrenzung

Für genau die beiden rational festgelegten, exakt W-normierten Richtungen aus
dem Kandidatenpaket wird die tatsächliche Budgetform eingeschlossen. Es gelten
dieselben gebundenen Operator-, Domänen- und Quellenmodellvoraussetzungen wie
bei den vorausgehenden Skalarzertifikaten. Nach außen gerundet:

| Parität | tatsächliches K_P | neue hinreichende Schwelle τ |
|---|---:|---:|
| gerade | [0,000213400114547; 0,000213400114550] | [3,314249417943; 3,314249417944] |
| ungerade | [3,911146161770442; 3,911146161770490] | [182,550050826232; 182,550050826233] |

Die unveränderten Skalarintervalle [−12,293; 15,280] und [118,635; 186,422]
entscheiden den Vergleich mit diesen neuen Schwellen nicht. Beide neuen Tests
heißen `INCONCLUSIVE_FOR_DIRECTION`. Weder Ausschluss noch Nichtausschluss wird
für diesen schärferen Test behauptet. Die frühere Nichtausschlussaussage mit
den ausdrücklich gröberen K_P-Majoranten bleibt als damaliger Test korrekt;
sie war kein Vergleich mit der tatsächlichen Budgetform.

Die Kandidaten werden weder geändert noch neu optimiert. Keine neue L-Paarung
wird berechnet. Ein ganzes gerichtetes K_P-Matrixzertifikat auf dem Schalenraum,
ein N12-Abschluss oder eine Bestätigung der Antwortregel werden nicht behauptet.

## 2. Quellen und Modellanschluss

`INPUT_BINDINGS.json` bindet die beiden Kandidaten, die vollständigen vorherigen
Skalarzertifikate, ihre Herleitung und Eingabeliste sowie das ursprüngliche
K_P-Budgetpaket. Das Antwortarchiv mit SHA-256 `b8677c0b…` wird direkt aus dem
Repository gelesen; sein vollständiger Hash, sämtliche Einträge des obersten
Manifests und die Quellbindungen von `RESPONSE_ENERGY.json` werden geprüft.
`FROZEN_RESPONSE12.json` und `FUNCTIONS12.json` müssen dieselben Hashes besitzen
wie in den Eingaben der geerbten Skalarrechnung.

Für die unveränderte Regel `A9_A11_N12_MIDPOINT_INVERSE_60_V1` gilt

    T = X_fix Fhat,
    K_P[s] = d[s] − 2Re⟨Fs,Ts⟩ + ⟨Ts,A12Ts⟩,
    Khat[s] = d[s] − (Fhat s)*S0(Fhat s),
    S0 = X_fix + X_fix* − X_fix* M_A X_fix.

X_fix und M_A sind die exakt rationalen, symmetrischen Zwölfermatrizen aus dem
Antwortarchiv. S0 wird mit `Fraction` exakt neu gebildet. Seine zwölf positiven
LDL-Pivots pro Parität werden mit Arb bestätigt. Die Subtraktionsidentität
benötigt diese Positivität nicht; sie bestätigt zusätzlich den Anschluss an
die frühere obere Budgetherleitung.

Die zwölf Intervalle für Fhat s werden vollständig aus dem separaten gerichteten
Skalarzertifikat übernommen. Ihre Modell-/Koeffizienten-/Integrationsunsicherheit
wird in der quadratischen Auswertung nicht durch Mittelpunkte ersetzt. Es gilt

    |K_P[s] − Khat[s]| ≤ E_K,
    E_K ≥ 2 δ_F ||T|| + δ_A ||T||²,

weil ||s||_W=1. Die gebundenen rechten Seiten werden nochmals überprüft; E_K
stimmt außerdem mit dem K_P-Budgetpaket überein. E_K ist kleiner als
1,661·10⁻²⁴ gerade bzw. 2,183·10⁻²⁶ ungerade und wird **zweiseitig** addiert.
Die ursprünglichen großen F/A12-Integrationen bleiben übernommene Voraussetzungen;
dieses Paket führt sie nicht unabhängig neu aus.

## 3. Exakter Lift und Normierung

Seien a=log3, b=log11/2, h=b−a, ε=1 bzw. −1,
m(x)=cosh(x/2) bzw. sinh(x/2), μ=(εa+sinh a)/2. Mit der lokalen
2dx-orthonormalen Legendrebasis ell_j und den festgelegten rationalen raw_j:

    s_raw = Σ raw_j ell_j,
    λ_raw = ∫ₐᵇ s_raw m,
    n² = Σ raw_j² + 2λ_raw²/μ,
    s = s_raw/n, λ=λ_raw/n, A_c=−λ/μ.

λ_raw wird in der Variablen x=a(1+t) über die Hyperbelreihe vom Grad 120
integriert. Der Rest ist durch exp(b/2)(h/2)^121/121! beschränkt; sein Produkt
mit s_raw wird über die Summe der absoluten Polynomkoeffizienten bezahlt.
Der Lift auf R lautet

    u(x) = εs(−x) auf (−b,−a),
           A_c m(x) auf (−a,a),
           s(x) auf (a,b), sonst 0.

Damit ist ||u||²=2∫ₐᵇs²+2λ²/μ=1 exakt. Die gerichtete Normierung überlappt
die unabhängig erzeugte Normierung des vorherigen Zertifikats. Die beiden
Ableitungs-/Sprunggrößen werden erneut eingeschlossen:

    A = ||u'_stückweise||²
      = 2∫ₐᵇ(s')² + 2A_c²(−εa+sinh a)/8,
    J = 2[(s(a)−A_c m(a))²+s(b)²].

Die Paritätsfortsetzung hat bei 0 keinen Sprung. Die neuen A/J-Intervalle
überlappen die vorausgehenden gerichteten Intervalle. Diese Kontrollen sind
zusätzliche Konsistenzprüfungen; die Norm- und Ableitungsidentitäten tragen
die Herleitung.

## 4. Vollständige Autokorrelation

Setze C(r)=∫_R u(x)u(x+r)dx. Da u reell und exakt normiert ist,

    ||u(·+r)−u||² = 2(1−C(r)).

Der Prüfer bildet sämtliche neun Überlappungen der drei physischen Stücke.
Für Stücke [a_i,b_i] und [a_j,b_j] lauten die Integrationsgrenzen
max(a_i,a_j−r) und min(b_i,b_j−r). Die aktiven Zweige werden mit gerichteten,
strikten Vergleichen am Zellmittelpunkt ausgewählt; ein unentscheidbarer
Vergleich bricht ab. Es gibt auf r>0 genau die möglichen Wechselstellen

    h, 2a, a+b, 2b.

Zwischen diesen Stellen bleibt jeder Zweig fest. Seine algebraische Formel
besitzt eine ganze Fortsetzung in r. Für zwei Schalenstücke wird das Produkt
der beiden verschobenen Polynome exakt integriert. Für zwei Kernstücke gilt

    ∫_l^v A_c² m(x)m(x+r)dx
      = A_c²/2 [sinh(v+r/2)−sinh(l+r/2)
                 + ε(v−l)cosh(r/2)].

Für gemischte Stücke wird m in seine zwei Exponentialterme zerlegt. Für ein
Polynom p und σ=±1 lautet die endliche Stammfunktion

    ∫p(x)exp(σx/2)dx
      = exp(σx/2) Σ_(k=0)^deg(p) (−1)^k (2σ)^(k+1) p^(k)(x).

Verschiebungsfaktoren exp(σr/2) und Paritätszeichen werden mitgeführt. Es gibt
hier keinen abgeschnittenen Exponentialreihenrest. C ist an den Wechselstellen
stetig (Translationsstetigkeit in L²); insbesondere darf C(2a) mit der rechten
Formel ausgewertet werden. Der Wert C(0) enthält als Kontrolle exakt 1.

## 5. Ganze Translationsenergie mit Resten an beiden Enden

Die gebundene direkte Nichtpolform aus `HERLEITUNG.txt`, §3, lautet

    d[s] = E[u] − κ||u||² − ⟨u,S_bu⟩,
    E[u] = ∫₀^∞ k(r)||u(·+r)−u||²dr,
    k(r) = exp(−r/2)/(1−exp(−2r)),
    κ = log(8π)+EulerGamma+π/2.

Der Bereich nahe 0 wird mit t=h·2⁻⁴⁸ abgetrennt. Für 0<r<t<h sind die vier
Sprungintervalle disjunkt, daher

    ||u(·+r)−u|| ≤ r√A+√(rJ).

Aus k(r)≤1+1/(2r) folgt die vollständige Nahbereichsgrenze

    0 ≤ E_near ≤ A(t³/3+t²/4)
        +2√(AJ)(2t^(5/2)/5+t^(3/2)/3)+J(t²/2+t/2).

Sie beträgt <1,864·10⁻¹⁵ gerade bzw. <4,723·10⁻¹⁴ ungerade. Insbesondere
ist der Lift in der hier verwendeten Formdomäne: Die Energie ist bei 0
integrierbar; die endlichen übrigen Bereiche und der folgende Fernbereich
sind ebenfalls bezahlt. Es wird kein Nahbereich nur numerisch weggelassen.

Auf [t,2b] werden 55 Zellen benutzt: 48 dyadische Zellen bis h, anschließend
Zellen mit Quotient rechter/linker Rand höchstens 2 sowie sämtliche oben
genannten Wechselstellen. Pro Zelle werden 128 Gauss-Legendre-Knoten benutzt.
Für Mittelpunkt c und Halblänge d wird das zu ρ=2 gehörende Rechteck

    |Re(z−c)|≤5d/4, |Im(z−c)|≤3d/4

gerichtet ausgewertet. Seine Realteile sind strikt positiv; damit hat der
Kernel dort keine Polstelle. Die fest ausgewählte Korrelationsformel ist dort
ganz, auch wenn ihre Fortsetzung über eine reale Wechselstelle hinausgeht.
Für f(z)=2k(z)(1−C_branch(z)) und M≥sup|f| wird je Zelle der Rest

    8d M 2^(−2n)/(1−1/2), n=128,

addiert. Er folgt durch Chebyshev-Abschneiden nach Grad 2n−1 und die positiven
Gaussgewichte: Integral und Quadratur haben auf [−1,1] jeweils Norm 2. Die
Summe dieser analytischen Reste ist <3,753·10⁻³⁸ bzw. <5,393·10⁻³⁴. Alle
Koeffizienten, Normierungen, Knoten und Funktionswerte bleiben Arb-Intervalle
bei 800 Bit; Rundungsfehler sind zusätzlich in den Intervalloperationen enthalten.

Für r≥2b verschwindet C(r). Mit

    Θ(r)=atanh(exp(−r/2))+atan(exp(−r/2)), Θ'(r)=−k(r),

ist der vollständige Rest bis unendlich exakt 2Θ(2b). Der Faktor 2 stammt
von ||u(·+r)−u||²=2 und wird nicht nochmals verdoppelt.

Die sieben aktiven Primkanäle q=2,3,4,5,7,8,9 werden vollständig ausgewertet:

    ⟨u,S_bu⟩ = 2Σ_q log(prime(q))/√q · C(log q).

Beim Kanal 9 gilt log9=2a exakt. Negative Autokorrelationsbeiträge werden mit
ihrem Vorzeichen übernommen, nicht durch eine untere oder absolute Schranke
an der falschen Stelle ersetzt.

## 6. Subtraktion und Schwellenentscheidung

Die Zwischenwerte, hier nur als ungefähre Orientierung, sind:

| Größe | gerade | ungerade |
|---|---:|---:|
| d[s] | 1,546902335417 | 3,941441397690 |
| (Fhat s)*S0(Fhat s) | 1,546688935302 | 0,030295235920 |
| alte K_P-Majorante | 19,984271332842 | 26,449113597369 |

Die starke gerade Reduktion ist eine Subtraktion zwischen gerichteten
physisch definierten Größen. Nur den positiven S0-Term von der alten groben
Majorante abzuziehen hätte noch etwa 18,438 bzw. 26,419 ergeben. Entscheidend
ist hier zusätzlich die vollständige direkte Energie statt ihrer groben
Translations-/Primnormmajorante.

Es wird das exakte rationale obere Ende K_up des neuen K_P-Intervalls gewählt.
Für die unveränderten gebundenen q und ε_D gilt die definierte hinreichende
Schwelle

    τ = sqrt(10q K_up/11)+ε_D.

Das ist weiterhin eine hinreichende Schwelle aus einer Obergrenze, kein
behaupteter exakter kritischer Wert. K_up ist in beiden Fällen positiv.
ε_D bezahlt bereits den D−Dhat-Fehler. Die unveränderten L-Intervalle werden
ohne Mittelpunktverschiebung übernommen. Die Klassifikation lautet:

* dist(0,L)>sup τ: `EXCLUDES_FOR_DIRECTION`;
* sup|L|≤inf τ: `DOES_NOT_EXCLUDE_FOR_DIRECTION`;
* sonst: `INCONCLUSIVE_FOR_DIRECTION`.

Hier trifft jeweils der dritte Fall zu. Die kleinen Integrationsreste der
neuen K_P-Rechnung beeinflussen diese Entscheidung nicht. Offen ist die
Verfeinerung des endlichen und vor allem hohen Antwortbudgets im L-Intervall.
Erst eine solche getrennte Rechnung darf den Entscheidungsstatus ändern.

## 7. Pflichtprüfungen und Reichweite des Replays

Vor dem Abnahmelauf sind verpflichtend: eigener Hashcheck, beide bytegleichen
Zertifikatsreplays aus einem frisch extrahierten Repository-Archiv, der
separate Autokorrelationskontrollweg sowie Metadaten-/Registryprüfung und
die bestehenden Registrytests. Ein CI- oder Registryerfolg ersetzt weder
diesen Paketlauf noch eine mathematische externe Begutachtung.

`audit_correlation.py` wertet den Lift unabhängig in lokalen Legendrekoordinaten
mit mpmath (100 Stellen) aus. Es integriert die reellen Überlappungen mit
64 Gaussknoten und benutzt keine Polynomprodukt-/Exponentialstammfunktion des
Certifiers. Zwölf Kontrollen pro Parität decken alle Korrelationszweige und
alle sieben Primverschiebungen ab; die größten Abweichungen betragen rund
2,86·10⁻¹⁰¹ bzw. 2,82·10⁻¹⁰⁰. Dieser ungerichtete zweite Rechenweg ist ein
Implementierungsaudit und liefert keine zusätzliche Zertifikatsschranke.

`verify.py` kontrolliert die eigene Dateibindung, erzeugt beide K_P-Zertifikate
neu, verlangt deren Bytegleichheit und führt den Kontrollweg aus. Die
übernommenen L-Zertifikate werden gebunden, hier aber nicht neu integriert.
Die neue Herleitung, die übernommenen großen Integrationen und die gesamte
Operator-/Domänenkette bleiben extern zu prüfen.

Ein erster Entwicklungsstart scheiterte vor der Rechnung an einer mehrdeutigen
Suche nach `MANIFEST.json` im verschachtelten Antwortarchiv. Der Leser verlangt
jetzt genau eine Archivwurzel und genaue relative Mitgliedsnamen. Es wurden
keine Ergebnisse dieses abgebrochenen Starts verwendet. Die Zweigauswahl wurde
vor dem Abnahmelauf von Mittelpunkt-Fließkommavergleichen auf strikt gerichtete
Vergleiche umgestellt; alle resultierenden Zertifikatsbytes blieben gleich.

## 8. Nachtrag: den hohen Koordinatenanteil des Testresiduums benutzen

Die vier neuen Ergebnisdateien trennen die Schritte: `SHARP_K_*.json` hält
die K_P-Rechnung und den damaligen Vergleich mit den alten L-Intervallen fest;
`PROJECTED_HIGH_*.json` enthält den folgenden engeren Vergleich. Die beiden
Kandidaten, I₀, sämtliche Integrationen und die K_P-Schwellen bleiben unverändert.

Aus der gebundenen Hochantwort-Herleitung, §1, gelten in isometrischen
Legendrekoordinaten exakt

    Mx=x−e⟨m_s,x⟩/m_e, x∈e⊥,
    e⊥=ran E ⊕ Y,
    Φ=U⁻¹ME, T_h=P_Y M*U,
    u_hi=U⁻¹Mr/δ, r∈Y, δ=18219/10000.

U ist isometrisch, M ist **nicht** isometrisch. Der physische hohe Antwortteil
u_hi ist deshalb nicht als orthogonal zu ran Φ anzunehmen. Stattdessen erfolgt
die folgende Subtraktion in den tatsächlich orthogonalen Koordinaten E und Y.
Der Adjunkt von M nimmt Werte in e⊥ an. Für das bereits eingeschlossene ganze
Modellresiduum h₈ und ℓ=Φ*h₈ gilt somit

    ||T_h h₈||² = ||M*U h₈||² − ||E*M*U h₈||²
                = ||M*U h₈||² − ||ℓ||²
                ≤ γ_m ||h₈||² − ||ℓ||²,
    γ_m = ||M||² = ||m_s||²/|m_e|².

Die obere Schranke γ_m ist bereits im gebundenen Hochantwortzertifikat als
`full_M_norm_squared` enthalten. Es handelt sich um die ganze Momentfunktion,
keine endliche Näherung ihres Trägers. Die 191 Komponenten von ℓ und die Norm
von h₈ liegen aus der gerichteten Skalarrechnung vor. `project_high.py` bildet
die rechte Seite vollständig mit Intervallen. Ihr oberes Ende verwendet damit
eine **untere** Einschließung der subtrahierten Quadratsumme; es wird keine
untere Normschranke als obere eingesetzt. Beide resultierenden Majoranten sind
strikt positiv, ungefähr 2,6808611·10⁻⁵ bzw. 0,44533060.

Die tatsächliche ganze Hochantwortnorm in Koordinaten ist durch R_r≥||r||
gebunden (`actual_high_difference_norm_upper`, Richtung `lower_Pv`). Es folgt

    |⟨u_hi,h₈⟩| = |⟨r,T_h h₈⟩|/δ
      ≤ (R_r/δ) sqrt(γ_m||h₈||²−||ℓ||²) = R_projected.

Die gebundenen Fehler in r, einschließlich tatsächlichem k, Modell, Quellen
und B-Kopplung, bleiben vollständig in R_r enthalten. Der Quellenmodellrest
des Testresiduums wird unverändert separat durch die ganze χ_p-Norm bezahlt.
Es wird keine neue physische Orthogonalitätsbehauptung und keine kohärente
Auswertung der zwölf zusätzlichen U₈-Antworten benutzt.

Nach oben gerundet sinkt der hohe Budgetterm auf 4,662438 gerade bzw.
15,290465 ungerade. Alle anderen Fehlerterme aus §5 des Skalarzertifikats
bleiben erhalten: kohärenter ψ-k-Fehler, vollständiger endlicher Antwortfehler
und Quellenmodellrest. Mit demselben ganzen gerichteten I₀ ergibt sich:

| Parität | engeres L, nach außen gerundet | unveränderte neue Schwelle | Entscheidung |
|---|---:|---:|---|
| gerade | [−5,961; 8,948] | [3,314249417943; 3,314249417944] | INCONCLUSIVE_FOR_DIRECTION |
| ungerade | [135,497; 169,560] | [182,550050826232; 182,550050826233] | DOES_NOT_EXCLUDE_FOR_DIRECTION |

Der neue ungerade Abstand sup|L| zur hinreichenden Schwelle ist größer als
12,990. Das ist weiterhin keine Bestätigung der Regel und kein N12-Abschluss.
Der gerade Test bleibt ein Überlappungsfall. Seine verbleibenden dominierenden
Fehler sind der endliche k-Anteil (etwa 2,791419) und die ganze hohe Antwort
(etwa 4,662438); eine weitere Verkleinerung der K_P-Quadraturreste ist unnötig.

Die Hochantwortdatei und ihre Herleitung werden zusätzlich direkt gebunden;
ihr Datenhash muss mit dem bereits im Skalarzertifikat verwendeten Hash
übereinstimmen. Der erweiterte Pflicht-Replay verlangt alle vier Ergebnisdateien
bytegleich aus einem frischen Archiv und führt die unveränderten 24 numerischen
Autokorrelationskontrollen aus. Die Registry-/Beweisankerprüfungen bleiben
verpflichtend. Externe mathematische Prüfung ist weiterhin offen.
