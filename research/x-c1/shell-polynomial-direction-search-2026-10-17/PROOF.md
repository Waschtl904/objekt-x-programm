# Schalenrichtungssuche: Herleitung und ausdrücklich ungerichtete Ergebnisse

17.10.2026. Numerische Kandidaten; externe Prüfung offen. Keine Statuspromotion für N12.

## 1. Physischer Raum und Normierung

Für a=log3, b=log11/2, h=b−a, m=cosh(·/2) oder sinh(·/2), μ=∫₀ᵃm² gilt auf der neuen Schale

    ell_j(x)=sqrt((2j+1)/(2h)) P_j(2(x−a)/h−1), j=0,…,11,
    λ_j=∫ₐᵇm ell_j, G=I+2λλᵀ/μ.

Die ell_j sind unter 2dx orthonormal. Der physische Lift hat Kern −λ(s)m/μ und Normquadrat cᵀGc. Numerisch sind cond(G)=1,1128967419347988 / 1,3147908698591293; die schlechte Kondition einer Momentbasis ist hier kein Erklärungsmodell. Cholesky G=LLᵀ und c=L⁻ᵀy geben ||y||₂=1. Beide Whitening-Residuen liegen unter 10⁻¹³. Die Suche benutzt reelle Richtungen; eine globale Optimalitätsaussage über reelle oder komplexe Richtungen wird nicht gemacht.

## 2. Ganze Quellen und Residualabbildungen

Für jedes ell_j wird der ganze Lift eingesetzt. Auf 0<x<a ist die elementare C_p-Quelle modulo m

    ctilde_j(x)=A_j Mσ(x)
       −∫ₐᵇ[k(y−x)+εk(y+x)]ell_j(y)dy
       −Σ_q w_q[u_j(x+logq)+u_j(x−logq)],
    A_j=−λ_j/μ, ε=(−1)^σ,
    k(r)=exp(−r/2)/(1−exp(−2r)).

Mσ ist dieselbe gebundene J₊/J₋-Darstellung wie bei z₀. Die sieben Kanäle sind 2,3,4,5,7,8,9. Die zwölf Schnittstellen werden vollständig als Zellgrenzen behandelt. Die Fortsetzung ist im Kern A_jm, auf der positiven neuen Schale ell_j, auf der negativen εell_j(−x), sonst null.

Der Kernel wird in 1/(2r)+g(r) zerlegt; g ist bis zum ersten Pol bei ±iπ analytisch. Sein Taylorpolynom Grad 360 wird mit Arb bei 600 Bit erzeugt. Der Cauchyteil wird durch Polynomdivision exakt integriert; der reguläre Teil über analytische Polynommomente. Die Suchrechnung bezahlt den Taylorrest noch nicht gerichtet. Sechs separate 100-stellige mpmath-Integrale prüfen die beiden eingefrorenen Quellen bei x/a=1/7,1/2,6/7 mit Abweichung <10⁻³⁸. Diese Punktkontrolle ist keine uniforme Fehlergrenze.

Fhat verwendet den **physischen W-Momentmultiplikator** und den Faktor ell_j+λ_jm/μ. Polynom×Log-Momente sowie die glatten Taylorentwicklungen Grad 120 liefern die Mittelpunkte. T=X_fix Fhat. DhatT wird aus den zwölf gebundenen ganzen D-Funktionen aufgebaut; die Momentprojektion erfolgt am ganzen Residuum.

Für r_j=ctilde_j−DtildeT_j werden gespeichert:

* die zwölf I₀-Mittelpunkte, mit dem korrigierten μ₈-Kernlift;
* physische Gram-Matrizen von h=Π_ar und h₈=Π₈r|Kern;
* die endlichen Features C*Φ*h₈ und die zwölf b_F-Koordinaten;
* die kohärente ψ-k-Metrik b_F*G_p b_F;
* die stückweise Ableitungs- und Sprunggram-Matrizen des ganzen Lifts.

Der Kern verwendet 384 bzw. 512 Gaussknoten je Zelle, die alte Schale 60 dyadische Zellen mit 128 Knoten. Der ausgelassene Endpunktrest bleibt in dieser Suche ungerichtet. Alle elf zusätzlichen Richtungen sind im Auflösungsvergleich enthalten. Die gespeicherten Double-Matrizen sind identisch; die größte Differenz der hochpräzisen I₀-Mittelpunkte ist 1,92·10⁻⁴⁵ / 7,95·10⁻⁴⁶. Der gebundene z₀-Fall wird bis 5,24·10⁻¹⁶ / 2,49·10⁻¹⁶ reproduziert. Diese Differenzen sind keine Zertifikatsradien.

## 3. Richtungsabhängiges Budget und Suchziel

Verwendet wird I₀ als Mittelpunkt ohne numerische Verschiebung durch eine hohe Paarung. Das grobe Budget ist

    R(c)=H_hi ||h₈(c)|| + e_feature ||C*Φ*h₈(c)||
          +sqrt(b_F(c)*G_p b_F(c)).

Die erste und zweite Konstante stammen aus dem gebundenen Hochantwortpaket; e_feature enthält 1/sqrt(1−rho). Es werden keine zwölf zusätzlichen U₈-Antworten vorausgesetzt.

Für einen W-normierten Lift u seien A=||u'_stückweise||² und J die Summe der vier Sprungquadrate. Auf 0<t≤0,1<h gilt gemäß dem gebundenen K_P-Paket

    B(A,J,t)=A(t³/3+t²/4)
      +2sqrt(AJ)(2t^(5/2)/5+t^(3/2)/3)+J(t²/2+t/2)
      +4[1−t+log(1/t)/2+35/24]+3.

Hier werden A und J aus der tatsächlichen Richtung gerechnet, einschließlich der glatten Kernableitung und des inneren Sprungs ell(a)−A_c m(a). Die Majorante ist

    K_up(c)=min(29,603644, B(A(c),J(c),t)+E_K),
    τ(c)=sqrt(10q K_up(c)/11)+ε_D.

ε_D ist die gebundene Operatornormabschätzung auf dem W-Einheitsraum, kein nur für z₀ gültiger Fehler. Die Suchroutine minimiert B numerisch über t∈[10⁻⁹,0,1]. Jede Wahl in diesem Bereich ist für die analytische Majorante zulässig. Im Zertifikatslauf wird der gewählte rationale t-Wert festgefroren.

Optimiert wird I₀(c)−R(c)−τ(c), nach Orientierung I₀(c)≥0. SLSQP auf der euklidischen Einheitskugel verwendet z₀, die duale I₀-Richtung, zwölf H₈-Eigenrichtungen, zwölf Koordinatenrichtungen und 32 Zufallsstarts mit festem Seed. Die Daten enthalten alle 58 Läufe, Konvergenzmeldungen und Tangentialgradienten. Kleine negative Eigenwerte auf Double-Rundungsniveau werden ausschließlich für die Suchmajorante gekappt; ein materiell negativer Eigenwert bricht ab. Dies ist keine gerichtete PSD-Prüfung.

| Parität | I₀ | R | τ | beste gefundene Marge | z₀ mit derselben Budgetform |
|---|---:|---:|---:|---:|---:|
| gerade | 1,493637 | 13,785992 | 1014,219657 | −1026,512012 | −1367,910481 |
| ungerade | 152,528516 | 33,893399 | 474,717778 | −356,082661 | -396,925177 |

Die duale W-Norm der I₀-Zeile ist 408,753888 / 156,685934. Bereits nach Weglassen sämtlicher Radiusbeiträge und der positiven A,J-Terme bleibt die numerische obere Marge −527,737071 / −224,332212. Dafür wird B≥4[0,9+log10/2+35/24]+3 benutzt. Diese Diagnose begrenzt nur das hier gewählte Mittelpunkt-/Majorantenmodell; sie ist weder ein gerichteter Satz über alle Richtungen noch eine Schranke mit dem unbekannten tatsächlichen K_P anstelle seiner groben Majorante.

## 4. Einfrieren, Reproduktion und Grenzen

`FROZEN_even.json` und `FROZEN_odd.json` binden die Auswahl per SHA-256. Die auf 25 signifikante Dezimalstellen gerundeten Double-Koeffizienten werden als **exakte rationale Rohkoeffizienten** aufgefasst. Die exakte Richtung lautet Σraw_j ell_j / sqrt(rawᵀG raw). Damit wird nicht behauptet, die gerundete Richtung sei das exakte Optimierergebnis. Der separate Certifier rechnet genau diese feste Richtung; seine Normierung und Koeffizientenunsicherheiten werden mit Arb eingeschlossen.

Der Replay erwartet die vier Matrixdateien bytegleich und die Suche mit Marge-Toleranz 10⁻⁷ und Koeffiziententoleranz 10⁻⁵, weil BLAS-/Optimizerdetails nicht plattformübergreifend bitidentisch sein müssen. Die publizierten rationalen Kandidaten bleiben unverändert, auch wenn ein Replay minimal andere Optimiererkoeffizienten liefert.

Verworfener Entwicklungsversuch: `arb_series` hatte trotz gewünschtem Grad 360 den globalen Standard-Cap 10 verwendet. Der z₀-Pflichttest stoppte den Lauf; keine damaligen Ergebnisse sind übernommen. Jetzt sind `ctx.cap=362` und eine Präzisionsassertion gesetzt. Die vorhandenen Zertifikate #230/#231 waren davon nicht betroffen.

Nächste fachliche Frage: tatsächliches richtungsabhängiges K_P, insbesondere die bisher verworfene positive Korrektur Fhat*S₀Fhat, und ein gegebenenfalls schärferes Residualzentrum. Mehr Starts oder bloß engere Integrationsreste bei unveränderter grober Schwelle lösen die beobachtete Barriere nicht.
