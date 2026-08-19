# P11 R31 — Zweitcheck der Operator-Domain-Typisierung des Annulusdefekts

Date: 2026-08-19

## Prüfpunkt

R31 definiert für \(0<R<S<T_0\)
\[
j_{R,S}=E_{R,S}\rho_{R,T_0}
\]
und
\[
\Delta_{R,S}^{[T_0]}
=\phi_S-(C_{\Gamma,S}+\Sigma_S^{[T_0]})j_{R,S}.
\]
Damit \(\Delta_{R,S}^{[T_0]}\) als echter \(L^2(-S,S)\)-Vektor und nicht nur als Formfunktional definiert ist, muss
\[
j_{R,S}\in\mathcal D(C_{\Gamma,S})
\]
explizit geprüft werden.

## Domain-Check

R30, Proposition `prop:o3ac-riesz-equation`, gilt an jedem festen Source-Level. Insbesondere existiert für \(X=R\) ein \(s_R>0\) mit
\[
E_R\rho_{R,T_0}\in H^{s_R}(\mathbb R).
\]
P11 hat
\[
m_\Gamma(\xi)\asymp\log(2+|\xi|).
\]
Für jedes \(s_R>0\) gilt daher
\[
[\log(2+|\xi|)]^2\lesssim_{s_R}\langle\xi\rangle^{2s_R}.
\]
Folglich
\[
m_\Gamma\widehat{E_R\rho_{R,T_0}}\in L^2(\mathbb R).
\]
Da
\[
E_Sj_{R,S}=E_R\rho_{R,T_0},
\]
liegt \(j_{R,S}\) in der Operator-Domain der finite-window Gamma-Realisierung:
\[
\boxed{
j_{R,S}\in\mathcal D(C_{\Gamma,S}).
}
\]
Der Schurterm \(\Sigma_S^{[T_0]}\) ist beschränkt, also
\[
\mathcal D(C_{\Gamma,S}+\Sigma_S^{[T_0]})
=
\mathcal D(C_{\Gamma,S}).
\]
Somit ist
\[
\boxed{
\Delta_{R,S}^{[T_0]}\in L^2(-S,S)
}
\]
sauber typisiert.

## Pullback und Support

Auf diesen typisierten Vektoren kann die fixed-terminal Form-Pullback-Identität schwach angewendet werden. Zusammen mit
\[
E_{R,S}^*\phi_S=\phi_R
\]
und
\[
(C_{\Gamma,R}+\Sigma_R^{[T_0]})\rho_{R,T_0}=\phi_R
\]
folgt
\[
E_{R,S}^*\Delta_{R,S}^{[T_0]}=0.
\]
Da \(E_{R,S}^*\) die Restriktion auf \((-R,R)\) ist, verschwindet der \(L^2\)-Defekt dort fast überall und ist im Randannulus
\[
(-S,-R)\cup(R,S)
\]
getragen.

Damit bleibt die Äquivalenz
\[
\Delta_{R,S}^{[T_0]}=0
\iff
\rho_{S,T_0}=E_{R,S}\rho_{R,T_0}
\iff
s_{R,S,T_0}=0
\]
vollständig typisiert.

## Verdict

\[
\boxed{\text{R31-C exact annular cancellation gate}\quad\checkmark[M].}
\]

Kein Statuswechsel für R30-F:
\[
\boxed{R_*(S,T_0)=S\quad ?[O].}
\]

Paper-Abgleich: `papers/P11_sections/P11_O3ad_Gamma_Antilocality_Cancellation_Gate.tex` enthält die explizite Domain-Zeile seit Commit

`ac40da948dc94a38adc5b25e33f402e471f77844`.

Keine Polar-Gauge-, Terminal-Transport-, Objekt-X- oder RH-Aussage folgt aus diesem Domain-Check.