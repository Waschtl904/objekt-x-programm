# P09 — LaTeX-SYN-Transferaudit

**Datum:** 9. August 2026  
**Markdown-Quelle:** `papers/P09_BC_Hochschild_and_Charged_Cohomology.md`  
**LaTeX-Ziel:** `papers/P09_BC_Hochschild_and_Charged_Cohomology.tex`  
**Prüfart:** reiner SYN-Transferaudit; kein erneuter Vollaudit der historischen NEU-Knoten  
**Urteil:** **OHNE KONKRETEN TRANSFERGEGENBEFUND**

---

## 1. Status- und Scopegleichheit

Beide Fassungen führen P09 als `SYN FINAL AUDITED` und verwenden als Basis:

- P09 Pass-A FINAL SEAL;
- P09 SYN-Primärcheck;
- P09 SYN-Zweitcheck.

NEU-222 wird nur als Superseding-Scan verwendet. Fehlende Live-Knoten NEU-191 und NEU-198 werden als Provenienzlücken sichtbar gehalten.

## 2. Mathematische Kernidentität

Der LaTeX-Transfer enthält dieselben belastbaren Hauptresultate wie der Markdown-Endstand:

\[
[\Omega_p]\neq0\in HH^4(A_{\mathbb Q}^{\rm alg},A_{\mathbb Q}^{\rm alg}),
\qquad \deg_\Gamma\Omega_p=1_\Gamma,
\]

\[
[D_g^{\rm corr}]\neq0\in HH^1(A_{\rm alg},A_{C^*})_g,
\]

\[
[D_g^{\rm corr}]\neq0\in HH^1(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g,
\]

und

\[
\boxed{
[D_g^{\rm corr}]\smile[\Theta^\wedge]\neq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
}
\]

## 3. Firewalls transferiert

Die LaTeX-Fassung übernimmt insbesondere korrekt:

1. `D_g(e(r))=0` ist superseded; bindend ist `D_g^corr(e(r))=mu_m C_{m,n;r} mu_n^*`;
2. nur punktweise Normkonvergenz auf jedem festen Algebraelement;
3. `MX_N->0` ist falsch; eventuelle exakte Konstanz ist korrekt;
4. keine geladene Selbstkoeffizientenklasse aus den analytischen/logarithmischen Koeffizientenklassen;
5. voller Quotient `M/[A,M]` bleibt offen;
6. NEU-205 Architecture III bleibt offen;
7. `beta=1` wird durch die I4-Gibbsrechnung nicht positiv entschieden;
8. die I4-Relation `T_sigma Phi_{beta,chi}=g^{-beta}Phi_{beta,chi}` wird nur im bewiesenen Nichtnullbereich `beta>1` zum Zyklizitäts-No-go hochgestuft;
9. I4-`Phi_{beta,chi}` und I5-`Phi_0` bleiben getrennte Objekte;
10. `s=-1` und `tPhi_0=g^{-beta}Phi_0` für den kanonischen Basislift sind superseded;
11. verbindlicher I5-Endbefund ist
    \[
    t\Phi_0\neq C\Phi_0\quad\forall C\in\mathbb C;
    \]
12. andere zyklische Repräsentanten, orbitverschiebende Lifte und Weil-/Gamma-Korrekturen bleiben offen.

## 4. Adelische Architektur

Unverändert transferiert sind:

\[
\widetilde B=C_0(\mathbb A_f),
\qquad
\widetilde A=C_0(\mathbb A_f)\rtimes_\gamma\mathbb Q_+^\times,
\]

\[
e\widetilde A_{\rm alg}e=j_A(A_{\rm alg}),
\qquad
N_k=N_0,
\]

sowie der kanonische Lift

\[
\widetilde L_0=\eta_0\circ j_M\circ L^{\rm cup}\in Z^4(A_{\rm alg},I_0),
\qquad
\kappa=\varepsilon=0.
\]

## 5. Technischer LaTeX-Check

Der Live-Quelltext wurde abschnittsweise auf offensichtliche Syntax- und Transferfehler geprüft. Dokumentklasse, Paketpräambel, Mathematikumgebungen, `enumerate`-Optionen und Dokumentabschluss sind konsistent.

Ein lokaler `pdflatex`-Lauf gegen die Live-GitHub-Datei wurde in dieser Sitzung **nicht erfolgreich ausgeführt**, weil der Container den Raw-GitHub-Endpunkt nicht per DNS auflösen konnte. Es wird daher ausdrücklich **kein erfolgreicher Compile behauptet**.

Dieser technische Infrastrukturpunkt ist kein mathematischer Gegenbefund.

---

## 6. Urteil

\[
\boxed{\text{P09 LATEX SYN-TRANSFER — OHNE KONKRETEN GEGENBEFUND.}}
\]

Die LaTeX-Fassung ist status- und inhaltsgleich zum final auditierten Markdown-SYN.