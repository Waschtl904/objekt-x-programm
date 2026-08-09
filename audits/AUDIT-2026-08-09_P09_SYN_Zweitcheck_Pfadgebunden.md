# P09 — SYN-Zweitcheck pfadgebunden

**Datum:** 9. August 2026  
**SYN:** `papers/P09_BC_Hochschild_and_Charged_Cohomology.md`  
**Basis:** P09 Pass-A FINAL SEAL + SYN-Primärcheck + Primärcheck-Patch  
**Prüfart:** unabhängiger pfadgebundener Status-/Typ-/Präzedenzcheck  
**Urteil:** **EINE LOKALE REICHWEITENKORREKTUR; DANACH OHNE KONKRETEN GEGENBEFUND**

---

## 1. I1 — neutrale Klasse

Bestätigt:

\[
A=A_{\mathbb Q}^{\rm alg},\qquad
[\Omega_p]\neq0\in HH^4(A,A),\qquad
\deg_\Gamma\Omega_p=1_\Gamma.
\]

Der Draft trennt nun korrekt Modellklasse, neutrale BC-Klasse und offenen geladenen Selbstkoeffizientensektor.

## 2. I2 — korrigierte Derivation

Bestätigt:

- `D_g^corr(e(r))=mu_m C_{m,n;r} mu_n^*`;
- nur punktweise Normkonvergenz auf jedem festen Algebraelement;
- geladene analytische Nichtinnerheit in `HH^1(A_alg,A_C*)_g`;
- kein algebraischer Selbstkoeffizientenschluss;
- NEU-205 Architecture III bleibt offen;
- fehlende NEU-198-Primärquelle wird nicht als Autorität verwendet.

## 3. I3 — logarithmischer Zieltyp und Cup

Bestätigt:

\[
[D_g^{\rm corr}]\neq0\in HH^1(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g
\]

und

\[
[D_g^{\rm corr}]\smile[\Theta^\wedge]\neq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
\]

Der Draft enthält die beiden entscheidenden Firewalls:

1. kein Schluss auf `HH^4(A_alg,A_alg)_g`;
2. der volle Quotient `M/[A,M]` bleibt offen.

## 4. I4 — lokale Reichweitenkorrektur

Bestätigt ist die strukturelle Eigenrelation der rohen I4-KMS-Kochain

\[
T_{\sigma_\beta}\Phi_{\beta,\chi}=g^{-\beta}\Phi_{\beta,\chi}.
\]

Die für die zyklische Negativentscheidung benötigte **Nichtverschwindung** von `Phi_{beta,chi}` ist im auditieren Gibbs-Kanal jedoch nur für

\[
\boxed{\beta>1}
\]

bewiesen. Der Draft formulierte den anschließenden Nichttrivialitäts-/Zyklizitätssatz einmal mit `beta>0`. Das ist zu weit.

**Patch:** In Satz 5.4 den eigentlichen No-go auf den bewiesenen Nichtnullbereich `beta>1` begrenzen. Die rein algebraische Eigenrelation darf stehenbleiben; `beta=1` und der nicht per Gibbs-Auswertung kontrollierte Bereich werden nicht positiv hochgestuft.

## 5. I5 — Präzedenz und End-No-go

Bestätigt:

- Laca-Dilatation und exakte algebraische Ecke;
- `N_k=N_0`, daher externe Orbitmarkierung;
- `U_{g^{-1}} != T^{-1}`;
- kanonischer Basislift `L~_0 in Z^4(A_alg,I_0)`, `kappa=epsilon=0`;
- `s=-1` und `tPhi_0=g^{-beta}Phi_0` vollständig `SUPERSEDED`;
- Unit-Slot-Endbefund
  \[
  t\Phi_0\neq C\Phi_0\quad\forall C\in\mathbb C
  \]
  im bewiesenen `beta>1`-KMS-Bereich;
- andere zyklische Repräsentanten und nichtkanonische orbitverschiebende Lifte bleiben offen.

## 6. I6 — NEU-222

Bestätigt: Der Draft übernimmt nur die Makrotrasse „singuläre Route trägt bis HH4, Blockade bei zyklischer Verfeinerung“ und nicht die supersedierten Detailstatus aus NEU-222.

Insbesondere werden nicht migriert:

- `[O-209-6] vollständig geschlossen`;
- `MX_N->0`;
- NEU-212-Schwartz-Zieltyp;
- historische `D_g(e(r))=0`-Formel;
- alte Terminierung über `s=-1`.

---

## 7. Schlussurteil

Nach der lokalen `beta>1`-Präzisierung besteht kein verbleibender Status-, Typ-, Formel-, Präzedenz- oder Routingkonflikt im P09-Markdown-SYN.

\[
\boxed{\text{P09 SYN-ZWEITCHECK — OHNE KONKRETEN GEGENBEFUND NACH LOKALEM PATCH.}}
\]