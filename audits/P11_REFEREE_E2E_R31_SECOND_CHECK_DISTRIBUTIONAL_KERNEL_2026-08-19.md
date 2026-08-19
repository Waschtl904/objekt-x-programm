# P11 R31 — Zweitcheck des distributionellen Gamma-Kernels

Date: 2026-08-19

## Anlass

Der Primäraudit

`audits/P11_REFEREE_E2E_R31_GAMMA_ANTILOCALITY_CANCELLATION_GATE_2026-08-19.md`

enthält beim Herleiten des off-diagonalen Gamma-Kernels die Kurzschreibweise, dass die Digamma-Reihe „modulo einer additiven Multiplikatorkonstante“ als negative Summe rationaler Terme gelesen werden könne.

Das Endresultat für den Kernel weg von der Diagonale ist korrekt, aber diese Zwischenformulierung ist als gewöhnliche Funktionsidentität zu grob: die getrennte Konstantensumme divergiert. Für einen strikten Audit muss die Herleitung distributionell über eine konvergente Differenz geführt werden.

## Korrekte Herleitung

Setze
\[
a=\frac14,
\qquad
q_\Gamma(\xi)
=-\log\pi+\operatorname{Re}\psi\!\left(a+\frac{i\xi}{2}\right).
\]
Aus der Digamma-Reihe folgt die tatsächlich konvergente Identität
\[
\boxed{
q_\Gamma(\xi)-q_\Gamma(0)
=
\sum_{n=0}^\infty
\left[
\frac1{n+a}
-
\frac{n+a}{(n+a)^2+\xi^2/4}
\right].
}
\tag{R31-Z.1}
\]
Die Summanden sind für festes \(\xi\) von Ordnung \(O(n^{-3})\).

Mit
\[
\lambda_n=2(n+a)=2n+\frac12
\]
gilt
\[
\frac{n+a}{(n+a)^2+\xi^2/4}
=
\frac{2\lambda_n}{\lambda_n^2+\xi^2}
=
\mathcal F(e^{-\lambda_n|\cdot|})(\xi)
\]
unter der bindenden P02-Fourierkonvention.

Nun sei \(\vartheta\in C_c^\infty(\mathbb R\setminus\{0\})\). Beim Paaren der inversen Fouriertransformation von (R31-Z.1) mit \(\vartheta\)

- verschwinden \(q_\Gamma(0)\) und die konstanten Terme \(1/(n+a)\), weil ihre inversen Fouriertransformationen am Punkt \(0\) getragene Delta-Terme sind;
- konvergiert die Reihe \(\sum_n e^{-\lambda_n|u|}\) auf dem Träger von \(\vartheta\) absolut und gleichmäßig.

Daher darf auf solchen Tests summiert werden und die Restriktion des distributionellen Kerns auf \(\mathbb R\setminus\{0\}\) ist exakt
\[
\boxed{
K_\Gamma(u)
=-\sum_{n=0}^\infty e^{-(2n+1/2)|u|}
=-\frac{e^{-|u|/2}}{1-e^{-2|u|}},
\qquad u\ne0.
}
\tag{R31-Z.2}
\]
Für \(c_0+c_1q_\Gamma\), \(c_1\ne0\), wird der off-diagonale Kernel mit \(c_1\) multipliziert; \(c_0\) trägt nur am Ursprung.

## Anti-Lokalität

Der anschließende Momentenbeweis des Primäraudits bleibt unverändert gültig. Für
\(\operatorname{ess\,supp}f\subset[-R,R]\) und \(x>R\) gilt
\[
(M_\Gamma f)(x)
=-c_1\sum_{n=0}^\infty e^{-\lambda_nx}
\int_{-R}^{R}f(y)e^{\lambda_ny}\,dy.
\]
Normale Konvergenz auf \(\operatorname{Re}x\ge R+\delta\), analytische Fortsetzung auf der rechten Halblinie und sukzessives Isolieren der Exponentialmomente liefern bei Vanishing auf einem offenen Intervall alle Momente gleich null. Nach \(t=e^{2y}\) erzwingt Polynomdichte \(f=0\).

Damit bleibt der Status
\[
\boxed{\text{R31-B pure exact-Gamma anti-locality}\quad\checkmark[M]}
\]
bestehen.

## Paper-Abgleich

`papers/P11_sections/P11_O3ad_Gamma_Antilocality_Cancellation_Gate.tex`

wurde in Commit

`40d693ff6017586664588fa2092b031daac0b712`

auf genau diese konvergente/distributionelle Herleitung umgestellt.

## Verdict

- Kernelresultat: ✓[M]
- Anti-Lokalität: ✓[M]
- ursprüngliche Kurzschreibweise als gewöhnliche Funktionsidentität: verworfen/ersetzt
- R30-F selbst: weiterhin ?[O]
- konkrete Annulus-Nichtkompensation des P11-Feshbachterms: weiterhin ?[O]

Keine Polar-Gauge- oder Terminal-Transport-Aussage wird aus R31 gewonnen.