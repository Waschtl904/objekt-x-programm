# Gerichtete Residualskalare für zwei feste Grad-11-Schalenrichtungen

17.10.2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.

## 1. Aussage und festgefrorene Eingaben

Unter denselben gebundenen Operator-, Domänen- und Quellenmodellvoraussetzungen wie beim z₀-Zertifikat gilt für die beiden separat ausgewählten Richtungen:

| Parität | L(c) nach außen gerundet | τ(c) nach außen eingeschlossen |
|---|---:|---:|
| gerade | [−12,293; 15,280] | [1014,219; 1014,220] |
| ungerade | [118,635; 186,422] | [474,717; 474,718] |

Beide erfüllen sup|L(c)|<inf τ(c). Der Status lautet `DOES_NOT_EXCLUDE_FOR_DIRECTION`, bezogen auf die unten festgelegte hinreichende Schwelle aus einer gültigen K_P-Obermajorante. Dies entscheidet weder den Vergleich mit einem unbekannten schärferen K_P noch den vollen Energievergleich. N12, die Bestätigung der Regel und Objekt X bleiben offen.

Die Datei `INPUT_BINDINGS.json` bindet die beiden `FROZEN_*.json` aus dem Kandidatenpaket. Keine Matrix der Suchrechnung und keine Optimiererentscheidung wird als gerichtete Eingabe übernommen. Die Rohkoeffizienten sind exakte rationale Zahlen. Mit a=log3, b=log11/2, h=b−a und der 2dx-orthonormalen lokalen Legendrebasis ell_j sei

    s_raw=Σraw_j ell_j, λ_raw=∫ₐᵇm s_raw,
    n²=Σraw_j²+2λ_raw²/μ_a, s=s_raw/n,
    λ=λ_raw/n, A_c=−λ/μ_a.

Der Lift u ist A_c m auf (0,a), s auf (a,b), mit der festgelegten Parität auf negativen x und sonst null. Seine physische Norm ist exakt 1. λ_raw wird durch die glatte Hyperbelreihe Grad 120 mit analytischem Rest eingeschlossen. Die Division durch das gerichtete n schließt die Normierung ein. Die Rundung des Suchergebnisses definiert die feste Richtung; gegenüber einem nicht festgelegten „wahren Optimierer“ wird kein Anspruch erhoben.

## 2. Neue C_p-Kopplung für ein Polynom

Die Quelle ist auf 0<x<a dieselbe vollständige Liftformel wie im Kandidatenpaket:

    ctilde(x)=A_c Mσ(x)−Γ_s(x)−Σ_q w_q[u(x+logq)+u(x−logq)],
    Γ_s(x)=∫ₐᵇ[k(y−x)+εk(y+x)]s(y)dy.

Mσ und die sieben Primkanäle stammen aus der gebundenen elementaren Quelle. Die neue Schale wirkt im offenen alten Kern nur über diese Integralkopplungen und Verschiebungen; ihre lokalen Multiplikationsterme haben dort keinen Träger. Der Kernlift A_c m und seine lokale Gamma-Kompensation bleiben unverändert. Alle zwölf Schnittstellen der Prim-/D-Translationsstücke sind Zellgrenzen.

Schreibe k(r)=1/(2r)+g(r). Für s(y)=Σs_l y^l setze

    Q_s(x)=Σ_(l≥1) s_l Σ_(k=0)^(l−1) x^k (b^(l−k)−a^(l−k))/(l−k).

Polynomdivision ergibt exakt

    ∫ₐᵇ s(y)/(y−x)dy=s(x)[log(b−x)−log(a−x)]+Q_s(x).

Der zweite Cauchyterm entsteht durch x↦−x und Faktor ε. Für g_N(r)=Σ_(j=0)^N g_j r^j, N=360, ist die reguläre Kopplung ein explizites Polynom. Sein x^k-Koeffizient lautet

    ((−1)^k+ε) Σ_(j≥k) g_j binom(j,k) ∫ₐᵇ y^(j−k)s(y)dy.

Alle Polynommomente werden analytisch mit Arb eingeschlossen. Die Koeffizienten g_j stammen aus der Potenzreihendivision exp(r/2)/(2 sinh(r)/r); der konstante Polterm wird getrennt. Der globale Serien-Cap und die erreichte Ordnung werden ausdrücklich geprüft.

## 3. Uniformer Rest des regulären Kernels

g ist analytisch in |z|<π. Auf |z|=R=3 gilt |sinh z|≥sin R>0: für z=u+iv ist |sinh z|²=sinh²u+sin²v; bei u²+v²=R² ist die Ableitung nach u² gleich sinh(2u)/(2u)−sin(2v)/(2v)≥0. Das Minimum liegt bei u=0. Somit

    sup_|z|=R |g(z)| ≤ M_R=exp(R/2)/(2sin R)+1/(2R).

Mit r_max=a+b<R liefert die Cauchy-Abschätzung

    sup_[0,r_max]|g−g_N| ≤ e_g
      =M_R (r_max/R)^(N+1)/(1−r_max/R).

Weil 2∫ₐᵇs²≤||u||²=1, gilt ∫|s|≤sqrt(h/2). Für beide Kernelintegrale zusammen folgt daher

    ||ctilde−ctilde_N||_∞ ≤ 2sqrt(h/2)e_g,
    ||Π_a(ctilde−ctilde_N)|| ≤ sqrt(2a)·2sqrt(h/2)e_g.

Die orthogonale Momentprojektion vergrößert die physische L²-Norm nicht. Mit der **gebundenen ganzen χ_p-Normobergrenze** wird dieser zusätzliche Modellfehler direkt bezahlt:

    E_source ≤ ||χ_p||_upper sqrt(2a)·2sqrt(h/2)e_g.

Er beträgt <5,230·10⁻²³ gerade / <6,547·10⁻²⁵ ungerade. Damit wird der reguläre Kernelrest nicht mit einer kleinen Kernnorm oder einem unbekannten Integrationsrest verwechselt. Die analytische Quadratur integriert ausschließlich das explizite Modell ctilde_N; E_source schließt den Übergang zur tatsächlichen Quelle.

## 4. Gerichtete Integration des ganzen Residualmodells

Für r_N=ctilde_N−Dtilde X_fix Fhat s werden sämtliche Schritte aus [dem z₀-Prüfer](../l00-z0-directed-interval-2026-10-17/PROOF.md), §§1–5, übernommen und erneut ausgeführt, mit folgenden ausdrücklich angepassten Größen:

* Im Fhat-Integral ist W_T=s(a(1+u))+λM(u)/μ_a. Sein Rest ist |λ/μ_a|e_m; eine uniforme Majorante ist |s(a(1+u))|_s+|λ/μ_a|m(b). Die Produktrestformel aus §2 des z₀-Pakets bleibt damit unverändert gültig.
* Die Primverschiebungen verwenden s(x+shift) oder εs(−x−shift) statt einer konstanten Schalenhöhe.
* Die Gamma-Kopplung ist das in §§2–3 definierte Polynom-plus-Cauchylog-Modell. Auf den komplexen Quadraturrechtecken werden **Differenzen einzelner Logarithmen** benutzt. a±x und b±x liegen dort in der rechten Halbebene; die Fortsetzungen sind analytisch.
* Am ausgelassenen Endstück t=a−x∈(0,d), d=(a−a₈)2⁻¹⁶⁰, lautet der logarithmische Koeffizient

      G(x)=(s(x)−A_c m(x))/2+D_V(x/a)/(2sqrt(2a)).

  Der reguläre Gammaanteil ist [s(x)log(b−x)+Q_s(x)+ε(s(−x)(log(b+x)−log(a+x))+Q_s(−x))]/2+Γ_regular,N(x). Dadurch wird die ganze Darstellung r_N=G logt+H eingeschlossen. Die gleichen analytischen L¹-/L²-Endpunktmajoranten gelten.

Es werden 512 Gaussknoten auf jeder der 13 Kernzellen und 128 Knoten auf jeder der 160 dyadischen alten Schalen verwendet. Für jeden Integranden wird der analytische Chebyshev-/Gaussrest 8d M 2⁻²ⁿ/(1−1/2) auf dem vollständigen ρ=2-Rechteck addiert. Alle Modellkoeffizienten, Mellinmomente, Normen, 191 Φ-Koordinaten und zwölf b_F-Koordinaten bleiben Intervallgrößen. Keine Suchmatrix, Netzverfeinerungsdifferenz oder numerische hohe Paarung ersetzt diesen Rest.

Der ursprüngliche komplexe Ausdruck log((b−x)/(a−x)) erzeugte auf einer breiten Rechteckbox eine nichtendliche Intervallauswertung. Der Pflichtcheck stoppte diesen Entwicklungsversuch. Die analytisch äquivalente Differenz log(b−x)−log(a−x) beseitigt diese Intervallüberbreite; keine Zell- oder Fehlerprüfung wurde entfernt.

## 5. Vollständiges Skalarbudget

Mit dem gebundenen k₀, unverändertem X_fix und den ganzen Quellen-/Antwortschranken gilt

    L(c) ∈ I₀(c)+[−E,E],
    E=Eψ+Efinite+Ehigh+Esource,
    Eψ=sqrt(b_F*G_p b_F),
    Efinite=(e_fixed+e_k)||C*Φ*h₈,N||/sqrt(1−rho),
    Ehigh=H_hi,p ||h₈,N||.

Das Modellzentrum I₀ verwendet die vollständigen gerichteten ψ₀- und c₀-Koeffizientenboxen. Der μ₈-Nenner und die exakte k₀-Zuordnung werden beibehalten. Die gemeinsamen k-Fehlerbeiträge werden konservativ durch Dreiecksungleichung transportiert; kein zusätzliches e_ψ||h|| wird nochmals addiert. E_source bezahlt den gesamten Unterschied zwischen Modellresiduum und tatsächlichem Residuum direkt über χ_p.

| Beitrag (nach oben gerundet) | gerade | ungerade |
|---|---:|---:|
| I₀: sämtliche Koeffizienten-/Quadratur-/Endpunktreste | 10⁻¹⁰ | 10⁻¹⁰ |
| Eψ | 0,000351 | 0,000144 |
| Efinite | 2,791420 | 1,740643 |
| Ehigh | 10,994223 | 32,152614 |
| Esource | 5,230·10⁻²³ | 6,547·10⁻²⁵ |

Die JSON-Dateien geben die maßgeblichen exakten rationalen Intervalle aus. Die Tabellen runden nach außen. Die Mittelpunkte sind etwa 1,493637131069 und 152,528515770934. Der hohe Rest verschiebt diese Mittelpunkte nicht.

## 6. Richtungsabhängige hinreichende Schwellen

Der Translationsschnitt t wurde im Kandidatenpaket als rationaler Wert festgefroren. Der Certifier optimiert ihn nicht. Es gilt 0<t≤0,1<h. Die tatsächlichen Ableitungs- und Sprunggrößen werden erneut gerichtet integriert:

    A=2∫ₐᵇ(s')²+2A_c²∫₀ᵃ(m')²,
    J=2[(s(a)−A_c m(a))²+s(b)²].

Die vier Sprungindikatoren sind für Translationen <t disjunkt; die Paritätsfortsetzung hat bei 0 keinen Sprung. Damit gilt ||u(·+r)−u||≤r sqrt(A)+sqrt(rJ). Einschließlich des Kreuzterms und aller Translationen bis unendlich folgt die B(A,J,t)-Formel aus [dem gebundenen K_P-Paket](../nstar-jp-spike-orthogonality-2026-10-16/original/gpt2-kp-budgets/HERLEITUNG.txt), §§3–5. Dort ist auch die Positivität von S₀ und der zweiseitige Modellfehler E_K gebunden, sodass K_P[s]≤B+E_K.

Der Certifier wählt zwischen dieser Majorante und der gebundenen ganzen Grad-11-Majorante 29,603644. Die Wahl erfolgt nur bei getrennten Intervallgrenzen; andernfalls wird die sicher gültige ganze Majorante genommen. Hier gilt in beiden Fällen die richtungsabhängige Variante:

    K_up ≈19,9842713328424 / 26,4491135973689,
    τ=sqrt(10q K_up/11)+ε_D.

q und ε_D stammen aus den unveränderten Operatornormschranken für W-normierte Schalenrichtungen. D−Dhat wird damit bereits in der Schwelle bezahlt. Eine zusätzliche Wiederholung dieses Fehlers im L-Intervall wäre unnötig.

Die Auswertung unterscheidet strikt:

* dist(0,L)>sup τ: `EXCLUDES_FOR_DIRECTION`;
* sup|L|<inf τ: `DOES_NOT_EXCLUDE_FOR_DIRECTION`;
* sonst: `INCONCLUSIVE_FOR_DIRECTION`.

τ ist eine definierte hinreichende Schwelle aus einer Obermajorante, kein exakter kritischer Wert der tatsächlichen K_P-Form. Der Nichtausschluss verbietet deshalb keinen späteren stärkeren Test.

## 7. Reproduzierbarkeit und offene Prüfung

`verify.py` kontrolliert eigene Dateien, gebundene Repository-Eingaben und Originalarchive, extrahiert die acht Recheneingaben frisch und verlangt beide Ergebnisdateien bytegleich. Die Auswahl bleibt von diesem Lauf getrennt. Die unabhängigen numerischen Punktkontrollen der Kandidatenstufe werden für die Zertifikatsgültigkeit nicht vorausgesetzt.

Offen bleiben externe mathematische Prüfung dieser Verallgemeinerung, der übernommenen Quellen-/Domänenvoraussetzungen und der ganzen hohen Antwortschranke. Der Replay bestätigt Determinismus und Eingabebindung, nicht diese externe Begutachtung. Es wird keine gerichtete globale Optimalität der Kandidaten und kein vollständiger N12-Ausgang behauptet.

## Provenienzkorrektur vor Integration

Der isolierte Archivtest der ersten Veröffentlichung fand eine fehlende direkte Bindung von `BUDGET_BOUNDS.json`. Die gelesene Datei war bereits Teil des unveränderten Repository-Bestands, fehlte aber in der eigenen Eingabeliste. Nun sind Budget, zugehörige Herleitung/Prüfer/Quittung sowie der Eingabevorbereiter direkt gebunden; im Kandidatenpaket zusätzlich beide z₀-Kontrollzertifikate. Jeder JSON-Ladevorgang der Rechenprogramme prüft die Bindungsliste. Die Rechendaten und Resultatdateien bleiben bytegleich. Diese Korrektur schließt die Provenienzlücke, ohne die mathematischen Voraussetzungen oder Zahlen zu ändern.
