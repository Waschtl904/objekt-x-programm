# Äußere Masse und Kopplung der kanonischen Ergänzungsräume

29. September 2026 · lokaler Forschungsblock · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

## Ergebnis

**Die äußere Massenform der echten kanonischen Ergänzungsräume ist jetzt in allen vier Fällen rigoros eingeschlossen.** Für den kleinsten äußeren L²-Massenanteil ergibt sich:

| Übergang | Parität | dim E | Einschließung von mₒᵤₜ(E) |
| --- | --- | ---: | ---: |
| A₈ → A₉ | gerade | 1 | **[0.9717 %, 2.5620 %]** |
| A₈ → A₉ | ungerade | 1 | **[5.7863 %, 12.8947 %]** |
| A₉ → A₁₁ | gerade | 2 | **[0.1284 %, 1.2872 %]** |
| A₉ → A₁₁ | ungerade | 2 | **[2.1727 %, 8.1344 %]** |

Die Angaben sind nach außen gerundet. Für Dimension zwei bezeichnet mₒᵤₜ den **kleinsten Eigenwert** der äußeren Massenform bei L²-Normierung. Die obere Grenze gilt dort nicht für jede Richtung: Es existiert eine Richtung mit höchstens diesem Außenanteil; alle Richtungen besitzen mindestens den angegebenen unteren Anteil.

Die zweite Richtung der zweidimensionalen Ergänzungen ist deutlich stärker außen vertreten:

| Ergänzung | Erster Eigenwert der äußeren Massenform | Zweiter Eigenwert |
| --- | ---: | ---: |
| E₉,₁₁ gerade | [0.1284 %, 1.2872 %] | **[30.8802 %, 40.1089 %]** |
| E₉,₁₁ ungerade | [2.1727 %, 8.1344 %] | **[38.6315 %, 57.6612 %]** |

Damit ist der qualitative Satz mₒᵤₜ>0 quantitativ bestätigt. Zugleich zeigt sich: **Eine überwiegende Außenlokalisierung des gesamten Ergänzungsraums ist nicht der gefundene Mechanismus.** Besonders die jeweils schwächste äußere Richtung liegt größtenteils im alten Intervall.

Die exakte Kopplungsidentität ist ebenfalls bestätigt:

\[
\boxed{q_B(Tx,e)=-17\langle J_{A,B}x,e\rangle_{L^2},
\qquad x\in K_A,\ e\in E_{A,B}.}
\]

Die daraus allein über mₒᵤₜ gewonnene absolute Kopplungsgrenze bleibt relativ grob. Sie ist noch kein relativer κ-Nachweis. Dieser Block berechnet wie vorgeschlagen zuerst äußere Masse und die erste geometrische Kopplungsschranke.

## 1. Definitionen und Beweisbindungen

Es bleiben unverändert

\[
b_A=q_A+17\|\cdot\|_2^2,\quad \tau=10^{-4},\quad
K_A=\operatorname{ran}\mathbf1_{(0,\tau)}(\mathcal A_A),
\]

\[
T=P_BJ_{A,B}|_{K_A},\qquad
E_{A,B}=K_B\ominus_{b_B}TK_A.
\]

Die Ränge pro Parität sind 5, 6 und 8. Der vorausgehende Transportblock beweist die Injektivität von T, die Dimensionen 1 und 2 von E und

\[
E_{A,B}=\{e\in K_B:b_B(e,Jx)=0\text{ für alle }x\in K_A\}.
\]

Mit \(\Omega_{A,B}=[-B,-A)\cup(A,B]\) definieren wir

\[
m_{\rm out}(E)=\inf_{e\in E,\ \|e\|_2=1}
\|\mathbf1_{\Omega_{A,B}}e\|_2^2.
\]

Die ursprünglichen Terminalformen, ihre Positivität, vollständigen hohen Schranken und Formnaturality werden am Commit

`d16ba43ebb20f2c61f43379fc65d7a9b9dba76de`

verwendet. Die Rechnung bleibt retrospektiv: Die schon bewiesene neue Terminalpositivität ist eine Voraussetzung.

## 2. Exakte Kopplung und ihre Normierung

Für x∈Kₐ zerlege Jx=Tx+Rx mit R=(I−Pᵦ)J. Weil e∈Kᵦ und Rx∈Kᵦ⊥ gilt qᵦ(Rx,e)=0. Außerdem ist bᵦ(Jx,e)=0. Somit

\[
q_B(Tx,e)=q_B(Jx,e)=-17\langle Jx,e\rangle_2.
\]

Da Jx im alten Intervall getragen ist,

\[
|q_B(Tx,e)|\le17\sqrt{1-m_{\rm out}(E)}\,
\|x\|_2\|e\|_2.
\tag{1}
\]

Wegen q≥0 und b=q+17‖·‖² folgt für die auf Kₐ zurückgezogene Kopplung \(\widehat C(x,e)=q_B(Tx,e)\)

\[
\boxed{\|\widehat C\|_{b_A,b_B}
\le\sqrt{1-m_{\rm out}(E)}.}
\tag{2}
\]

Für die Kopplung auf dem Bild TKₐ selbst ist die rechte Seite zusätzlich durch die zertifizierte minimale Singularwertgrenze von T zu teilen. Diese Unterscheidung verhindert, dass T versehentlich als b-Isometrie behandelt wird.

## 3. Echte Spektralräume aus Hilfsräumen einschließen

Die gespeicherten rationalen Diagnosevektoren sind keine echten Eigenvektoren. Wir verwenden ihre Mellin-korrigierten physischen Quellen ausschließlich zur Konstruktion von Hilfsräumen Wₐ und Wᵦ mit den richtigen Dimensionen rₐ und rᵦ.

Die physische L²-Grammatrix enthält die vollständige niedrige Momentkorrektur. Eine gerichtete Cholesky-Normierung definiert L²-orthonormale Basismatrizen Uₐ und Uᵦ. Für die tatsächlichen Rayleighquotienten auf Wₐ gilt eine neue gerichtete Obergrenze Θₐ.

Ist νₐ eine bewiesene Untergrenze des vollständigen physischen Komplementspektrums, dann

\[
\|(I-P_A)U_A\|_2^2\le\Theta_A/\nu_A.
\]

Aus der gleichen endlichen Dimension und einer Grenze unter 1 folgt

\[
\|P_A-P_{W_A}^{(2)}\|_2\le\eta_A,
\qquad \eta_A=\sqrt{\Theta_A/\nu_A}.
\tag{3}
\]

Dieser Schluss verwendet das ganze physische Spektrum. Die Ergänzung wird nicht mit einem Nullraum einer bloßen Trunkierung gleichgesetzt.

Für A₈ wurden zwei zusätzliche vollständige Gap-Zertifikate erstellt. Wie beim vorausgehenden Transportblock bleiben die ganze hohe Kopplungsmatrix und die nichttriviale Mellin-Masse in der parameterabhängigen Schurabschätzung erhalten. Die geprüften neuen physischen Grenzen sind

\[
\nu_{8,\rm even}=0.00418,\qquad
\nu_{8,\rm odd}=0.069995.
\]

Je fünf positive Pivots der negativen Kompression und eine positive rationale Reparatur beweisen die passende Zählung. Für A₉ und A₁₁ werden die vier Gap-Zertifikate des Transportpakets verwendet.

Die resultierenden sicheren Projektorfehler sind, nach oben gerundet:

| Terminal | Gerade | Ungerade |
| --- | ---: | ---: |
| A₈ | 0.018443 | 0.034902 |
| A₉ | 0.024429 | 0.047291 |
| A₁₁ | 0.030020 | 0.049331 |

Ein zusätzlich berechneter Residuentest war in diesen Fällen konservativer. Der endgültige rationale Nachweis benutzt ausschließlich (3), die Energieabschätzung mit vollständigem Gap.

## 4. Der kleine Hilfsraum und sein Abstand zum kanonischen E

Setze

\[
M=(JU_A)^*U_B,\qquad
F_{A,B}=W_B\cap(JW_A)^{\perp_{L^2}}.
\]

Die physische Überlappungsmatrix M wird durch gerichtete polynomielle Integration bestimmt. Aus \(MM^*\succeq s^2I>0\) folgt dim F=rᵦ−rₐ. Eine festgelegte Kernbasis von M wird L²-orthonormalisiert; ihre physische Basismatrix sei Uꜰ. Sie ist eine exakt definierte Hilfsbasis und wird nicht als Basis des kanonischen E ausgegeben.

Für e∈E mit ‖e‖₂=1 und x∈Kₐ liefert die Kopplungsidentität zusammen mit Cauchy–Schwarz für die bereits positive Form

\[
|\langle Jx,e\rangle_2|
\le\frac{\sqrt{\Theta_A\Theta_B}}{17}\|x\|_2
=:\zeta\|x\|_2.
\tag{4}
\]

Mit (3) folgt \(\|(JU_A)^*e\|\le\eta_A+\zeta\). Für z=(I−P_{W_B}^{(2)})e gilt ‖z‖≤ηᵦ und

\[
\|(JU_A)^*(I-P_{W_B}^{(2)})\|\le\sqrt{1-s^2}.
\]

Damit ist die Komponente von \(P_{W_B}^{(2)}e\) senkrecht zu F höchstens

\[
\frac{\eta_A+\zeta+\sqrt{1-s^2}\eta_B}{s}.
\]

Die beiden Fehleranteile sind orthogonal. Folglich

\[
\boxed{\|P_E^{(2)}-P_F^{(2)}\|_2^2
\le\varepsilon_E^2
:=\eta_B^2+
\frac{(\eta_A+\zeta+\sqrt{1-s^2}\eta_B)^2}{s^2}<1.}
\tag{5}
\]

Der letzte Schritt nutzt dim E=dim F. Hier ist \(P_E^{(2)}\) ausdrücklich der L²-Projektor auf E, nicht dessen b-Projektor.

Eine konkrete, basisfreie Übertragung der Hilfsbasis auf E ist ihre Polarprojektion

\[
U_E=P_E^{(2)}U_F\bigl(U_F^*P_E^{(2)}U_F\bigr)^{-1/2}.
\]

Sie ist L²-orthonormal und erfüllt

\[
\|U_E-U_F\|_2\le d_E
:=\sqrt{\frac{2\varepsilon_E^2}{1+\sqrt{1-\varepsilon_E^2}}}.
\tag{6}
\]

Die vier Grenzen für dₑ sind nach oben gerundet 0.030742, 0.059272, 0.038808 und 0.068904, in der Reihenfolge der Ergebnistabelle.

## 5. Rigorose Einschließung der kleinen Außenmassenmatrix

Definiere

\[
M_F=U_F^*\mathbf1_\Omega U_F,\qquad
M_E=U_E^*\mathbf1_\Omega U_E.
\]

Die tatsächlich integrierten Hilfsmatrizen sind ungefähr

\[
M_{F,8\to9}^{\rm even}=[0.0167232801],\qquad
M_{F,8\to9}^{\rm odd}=[0.0898917659],
\]

\[
M_{F,9\to11}^{\rm even}\approx
\begin{pmatrix}0.0400056408&0.1038878331\\0.1038878331&0.3190058306\end{pmatrix},
\]

\[
M_{F,9\to11}^{\rm odd}\approx
\begin{pmatrix}0.1292166237&0.1692452780\\0.1692452780&0.3942864898\end{pmatrix}.
\]

Diese Anzeigen sind **nicht** die ungestörten wahren E-Matrizen. Die exakten Intervallmatrizen und die folgende Übertragung bilden gemeinsam das Zertifikat.

Aus \(\|\mathbf1_\Omega(U_E-U_F)\|\le d_E\) folgt für alle geordneten Eigenwerte

\[
\bigl(\sqrt{\underline\lambda_j(M_F)}-d_E\bigr)^2
\le\lambda_j(M_E)
\le\min\{1,\bigl(\sqrt{\overline\lambda_j(M_F)}+d_E\bigr)^2\},
\tag{7}
\]

wobei alle unteren Wurzeln in diesem Paket größer als dₑ sind. Dies ist die Singularwert-Störungsabschätzung für die beiden eingeschränkten Basismatrizen; sie liefert insbesondere die positiven Zahlen in der Ergebnistabelle.

Zusätzlich werden vollständige Matrixeinschließungen ausgegeben:

\[
\|M_E-M_F\|\le2\sqrt{\overline\lambda_{\max}(M_F)}\,d_E+d_E^2,
\tag{8}
\]

und mit \(c=d_E/\sqrt{\underline\lambda_{\min}(M_F)}<1\)

\[
\boxed{(1-c)^2M_F\preceq M_E\preceq(1+c)^2M_F.}
\tag{9}
\]

Die rationalen Faktoren und alle Eintragsintervalle stehen in `verification.json`. Einzelne breite Eintragsintervalle können negative Diagonaluntergrenzen enthalten; die gemeinsame Matrix ist trotzdem durch (7) und (9) strikt positiv zertifiziert. Eintragsweise Intervalluntergrenzen sind keine untere Loewner-Matrix.

Die niedrige Dimension der abschließenden Massenform ersetzt somit nicht die Kontrolle der Spektralräume. Sie macht aber die abschließende Integration und Eigenwertauswertung klein, sobald die vollständigen Gap-Bindungen vorliegen.

## 6. Erste geometrische Kopplungsgrenzen und ihre Bedeutung

Aus den neuen unteren Massengrenzen folgt durch (2):

| Übergang / Parität | Obergrenze für ‖Ĉ‖ in den alten/neuen b-Normen |
| --- | ---: |
| A₈ → A₉ gerade | 0.995130 |
| A₈ → A₉ ungerade | 0.970638 |
| A₉ → A₁₁ gerade | 0.999358 |
| A₉ → A₁₁ ungerade | 0.989077 |

Diese Größen sind absolute Kopplungsgrenzen, **keine κ-Werte**. Sie liegen nahe eins, weil der kleinste äußere Massenanteil klein bleibt.

Zur Einordnung: Aus der bereits bekannten neuen Positivität und Cauchy–Schwarz folgt sogar die viel kleinere absolute Grenze

\[
\|\widehat C\|\le\sqrt{\overline\alpha_A\,\overline\alpha_B},
\qquad\overline\alpha=\Theta/(\Theta+17).
\]

Ihre sicheren Anzeigen sind 1.051·10⁻⁷, 6.591·10⁻⁶, 1.622·10⁻⁷ und 9.368·10⁻⁶. Diese Abschätzung benutzt die bereits zertifizierten positiven Terminals und ist kein neuer vorwärts gerichteter Positivitätsbeweis.

Der Vergleich zeigt konkret die Grenze einer reinen Außenmassenargumentation: **Die Menge der inneren Masse sagt noch wenig über ihre Ausrichtung zum alten kritischen Raum.** Eine Ergänzungsrichtung kann große innere Masse besitzen und trotzdem nahezu L²-orthogonal zu allen alten kritischen Richtungen sein.

Für

\[
\kappa_{\rm new}=\|S^{-1/2}CD_E^{-1}C^*S^{-1/2}\|
\]

sind außerdem relative Grenzen bezüglich der kleinen Eigenwerte von S und Dₑ erforderlich. Die hier berechneten absoluten Normschranken erfüllen diese Aufgabe nicht. Der nächste κ-Block muss deshalb die energiegewichtete Überlappung kontrollieren; die positive äußere Mindestmasse allein genügt nicht. Ein neuer κ-Lauf wurde hier nicht ausgeführt.

## Prüfung und Reproduzierbarkeit

- Zwei neue A₈-Komplement-Gaps mit der Standardbibliothek und Ganzzahlintervallen vollständig zertifiziert.
- Physische Testräume, ihre Massen-/Form-Grammatrizen und Überlappungen mit python-flint 0.9.0 bei **1024 und 1280 Bit** berechnet.
- Außen- und Überlappungsintegrale durch Gauss-Legendre-Quadratur mit **594 beziehungsweise 602 Knoten**. Die Integranden sind Polynome; die Grade liegen innerhalb der exakten Quadraturordnung. Die Intervallarithmetik bezahlt die Koeffizienten-, Knoten- und Parameterunsicherheit.
- Alle relevanten Matrizen beider Läufe besitzen überlappende Einschließungen. Ein separater Standardbibliothek-Prüfer berechnet aus ihren rationalen Endpunkten erneut die Projektorfehler, kleinen Eigenwertintervalle, Polarabstände, E-Massen und Kopplungsgrenzen.
- 18 Repository-Quellen sowie die vollständigen Manifeste der verschachtelten Referenzpakete überprüft. Keine ursprünglichen Terminalintegrale neu aufgebaut; ihre analytischen Beweise und Zertifikate bleiben Eingaben.
- Die analytische Übertragung (3)–(9) steht ausdrücklich im Bericht. Der rationale Replay ist kein formales Beweisassistenzsystem und ersetzt keine externe mathematische Begutachtung.

`verification.json` ist die maßgebliche Ergebnisdatei. `primary.json` und `crosscheck.json` enthalten die gerichteten Eingangsmatrizen. Die ausgeführten Prüfprotokolle und Reproduktionsanweisungen liegen bei.

**Keine Änderungen an Main, Registry, historischen Quellen oder globalen Verifikationsständen.** Keine neue Eigenbasis, keine Prime-/Shift-Zuordnung und kein allgemeiner Renewal-Satz werden behauptet.
