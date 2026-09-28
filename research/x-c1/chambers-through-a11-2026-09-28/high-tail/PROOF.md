# Ein erneuerbarer hoher Tail — und die verbleibende niedrige Positivität

Lokale Herleitung · EXTERNAL_REVIEW_OPEN

## Aussage

Für jeden festen endlichen Horizont L≥1 und jeden gewünschten hohen Boden
δ>0 existiert ein endlicher gerader Schnitt N=N(L,δ), so dass die
ursprünglichen Zwei-Mellin-Quellen mit verschwindenden niedrigen
Legendrekoordinaten in **allen** Fenstern 1≤A≤L die Schranke

\[
q_A[u]\ge\delta\|u\|^2
\]

erfüllen. Die Kodimension je Parität ist N/2−1. N darf mit L wachsen.
Die Aussage enthält keine Positivität der verbleibenden niedrigen Richtungen.

## 1. Allgemeiner Kernelbound

Mit z=t/2 gilt k_reg(2z)=(sech z+csch z−1/z)/4≤1/4.
Für 0<z≤1 benutzt man (2j+1)!≥6^j und erhält
sinh(z)/z≤1/(1−z²/6). Also csch(z)≥1/z−z/6 und
k_reg(2z)≥−1/24. Für z≥1 gilt unmittelbar
k_reg(2z)≥−1/(4z)≥−1/4. Der Grenzwert bei Null ist 1/4.
Daher gilt global |k_reg(t)|≤1/4 und ||K_A||≤A/2≤L/2.

## 2. Endlicher Verlust auf jedem endlichen Horizont

Vor der Momentkorrektur wird dieselbe poltermfreie Erweiterung auf der
Referenzformdomäne wie in PROOF.md benutzt; auf den zulässigen Quellen
stimmt sie mit der physischen Weil-Form des Modells überein.

Die aktiven Primzahlpotenzen q<exp(2L) bilden eine endliche Menge Q_L.
Setze Ω_L=Σ_(q∈Q_L) w_q. Jeder zweiseitige partielle Shift hat Norm ≤2;
somit ||S_A||≤2Ω_L. Mit q0(A)=−log(2πA)−γ und V≥0 gilt

\[
q_A[y]\ge\bigl(H_N-C_L\bigr)\|y\|^2,\quad
C_L=\log(2\pi L)+\gamma+L/2+2\Omega_L.
\tag{1}
\]

Die konkrete gemeinsame Abschätzung aus PROOF.md verbessert 2Ω_L zu

\[
B_L=\operatorname*{ess\,sup}_{|x|<1}(r_L(x)-V(x)),\quad0\le B_L\le2\Omega_L.
\]

Das Supremum ist durch endlich viele Shiftgrenzen bestimmbar: Auf der
positiven Hälfte ist r_L stückweise konstant, V zunehmend. Es genügt der
jeweilige linke Zellrand. Kontakte und zusammenfallende Grenzen werden
einmal geführt; einzelne Randpunkte sind für die Form ohne Bedeutung.
Für A≤L gilt r_A≤r_L. Damit darf in (1) auch der schärfere gemeinsame
Verlust log(2πL)+γ+L/2+B_L verwendet werden.

## 3. Vollständige Mellinkorrektur

Setze z_L=L/2 und wähle N groß genug für
z_L²<(N+1)(N+2). Die in PROOF.md hergeleiteten Momentreste gelten mit
z0=z_L. Insbesondere gehen

\[
\epsilon_{p,N}(L)=
\frac{z_L^{N+p}}{(N+p)!\,[1-z_L^2/((N+p+1)(N+p+2))]}
\begin{cases}1&p=0,\\4&p=1\end{cases}
\]

für festes L gegen Null. Der ungerade Nennerbound bleibt für A≥1 gültig.
Mit den normierten Trägern e0,e1 gelten auf dem gesamten Horizont die
endlichen Konstanten

\[
D_L=2+L/2+2\Omega_L,\qquad
E_L=3+\log(2\pi L)+\gamma+L/2+2\Omega_L,
\]

so dass |q_A(y,e_p)|≤D_L||y|| und ||Q_Ae_p||≤E_L.
Folglich ist der hohe physische Boden mindestens

\[
\frac{H_N-C_L-2D_L\epsilon_N-E_L\epsilon_N^2}{1+\epsilon_N^2},
\quad\epsilon_N=\max_p\epsilon_{p,N}(L).
\tag{2}
\]

Da H_N→∞ und ε_N→0, übersteigt (2) jeden vorgegebenen endlichen δ für
hinreichend großes gerades N. Für einen effektiv vorgegebenen Horizont
genügt eine rationale obere Einschließung von L: Man darf damit auch die
endliche Kanalfamilie nach oben vergrößern und alle Konstanten rational
einschließen. Eine Suche mit diesen gerichteten Schranken terminiert.
Mit dem schärferen B_L kann N kleiner werden.

Die vollständige Formdomäne, die Momentrekonstruktion und die exakte
Kodimension folgen aus dem allgemeinen endlichen Horizontmodell und
derselben stetigen Koordinatenabbildung wie in PROOF.md §4. Der Satz ist
deshalb keine Aussage nur über eine Modentrunkierung.

## 4. Bedeutung und Grenze

Damit kann der **hohe Teil** auf jedem endlichen Horizont erneut positiv
gemacht werden, beispielsweise immer mit δ=1. Der dazu erforderliche
Schnitt darf sich ändern. Dies entspricht der endlichen Reduktion eines
nach oben wachsenden harmonischen Diagonalanteils unter beschränkten
Störungen und positiver Randkomponente.

Es bleibt der niedrige vollständige Schurrest. Er kann durch die ganze
hohe Antwort beeinflusst werden; sein Vorzeichen wird durch (2) nicht
festgelegt. Eine negative Richtung der Gesamtform könnte in diesem
endlichen Rest liegen. Weder eine gemeinsame endliche Kodimension für
alle Horizonte noch eine positive volle Terminalreserve für alle L
folgt aus diesem Satz.

Für A11 wird die stärkere gemeinsame Shift-/Potentialrechnung mit einem
zusätzlich verbesserten mittelwertfreien Gamma-Bound benutzt. Der
resultierende Schnitt 572/573 ist daher wesentlich günstiger als die
allgemeine grobe Existenzabschätzung (1).

Der nächste strukturelle Forschungsgegenstand ist somit eine erneuerbare
**Positivität des niedrigen Schurrests**. Ein immer verfügbarer positiver
hoher Tail allein schließt Objekt X nicht.
