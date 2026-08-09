# P09 — SYN-Primärcheck

**Datum:** 9. August 2026  
**SYN:** `papers/P09_BC_Hochschild_and_Charged_Cohomology.md`  
**Pass-A-Basis:** `audits/AUDIT-2026-08-09_P09_PassA_FINAL_SEAL.md`  
**Prüfart:** pfadgebundener SYN-Transfercheck; kein erneuter Vollneuaudit von NEU-174–222  
**Urteil:** **DREI LOKALE PRÄZISIERUNGEN; KEIN GEGENBEFUND GEGEN DEN P09-KERN**

---

## 1. Neutraler I1-Kern: Algebra explizit fixieren

Der Draft schreibt den neutralen Befund als

\[
[\Omega_p]\neq0\in HH^4(A_{\rm alg},A_{\rm alg})_1.
\]

Der versiegelte I1-Endstand formuliert präzise

\[
A:=A_{\mathbb Q}^{\rm alg},
\qquad
[\Omega_p]\neq0\in HH^4(A,A),
\qquad
\deg_\Gamma\Omega_p=1_\Gamma.
\]

Die Kurznotation `A_alg` ist im späteren Strang üblich, aber der SYN-Draft soll die Identifikation am Eingang ausdrücklich erklären und Satz 2.1 zunächst auf `A_Q^alg` verankern. So wird kein Modell-/Algebrawechsel stillschweigend vollzogen.

**Patch:** §1.1 Notationssatz ergänzen; Satz 2.1 auf `A_Q^alg` explizieren.

---

## 2. Provenienzlücken sichtbar machen

Im Live-Inventar fehlen:

- `NEU-191` im I1/I2-Übergang;
- `NEU-198` im I2-Strang.

Insbesondere NEU-198 wird von NEU-199 referenziert, ist aber nicht als Live-Primärquelle vorhanden. Der Pass-A-Endstand verwendet seinen behaupteten Inhalt nicht als selbständige Autorität.

**Patch:** §1 Provenienz-Firewall ergänzen:

```text
NEU-191 und NEU-198 fehlen live; aus ihnen wird keine positive SYN-Aussage allein abgeleitet.
```

Dies ist ein Provenienzvermerk, kein mathematischer Gegenbefund.

---

## 3. Reichweite des NEU-205-No-gos

Der versiegelte I2-Endstand schließt die drei konkreten dyadischen L/R/S-Platzierungen nach Korrektur der Sandwichformel negativ. Er schließt **nicht** jede relation-adaptierte singuläre Ladungsarchitektur aus.

Insbesondere bleibt die in NEU-205 als `Architecture III` geführte `N`-abhängige relation-adaptierte Variante offen.

**Patch:** §3 nach dem Potential-/Glättungs-No-go ausdrücklich ergänzen:

\[
\boxed{\text{Die relation-adaptierte Architektur III bleibt }?[O].}
\]

Damit wird ein Kandidaten-No-go nicht zu einem universellen Struktur-No-go hochgestuft.

---

## 4. Kernbefunde ohne Beanstandung

Der Primärcheck bestätigt insbesondere:

1. korrigierte geladene Derivation und nur punktweise Normkonvergenz;
2. `Z_g={0}`, faktoriale Ursprungssingularität und eventuelle Konstanz statt `MX_N->0`;
3. logarithmischen Zieltyp `B^log/A^log` und globalen Bimodul `M_glob^log`;
4. nichttrivialen Cup
   \[
   [D_g^{\rm corr}]\smile[\Theta^\wedge]\neq0
   \in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g;
   \]
5. Firewall gegen Selbstkoeffizienten-`HH^4` und gegen den vollen Quotienten `M/[A,M]`;
6. I4-Twistkonvention `sigma_beta=alpha_{-i beta}` und die Trennung der rohen `Phi_{beta,chi}` von `Phi_0`;
7. `beta=1` als offen in der Gibbs-Auswertung;
8. Laca-Dilatation, exakte algebraische Ecke, Orbitkollaps `N_k=N_0` und markierte Ersatzstruktur;
9. kanonischen Lift `L~_0 in Z^4(A_alg,I_0)` mit `kappa=epsilon=0`;
10. vollständigen Rollback von `s=-1` / `tPhi_0=g^{-beta}Phi_0`;
11. autoritativen Unit-Slot-No-go
    \[
    t\Phi_0\neq C\Phi_0\quad\forall C\in\mathbb C;
    \]
12. offene nichtkanonische zyklische Repräsentanten, orbitverschiebende Lifte und Weil-/Gamma-Route.

---

## 5. Urteil

Nach den drei lokalen Patches ist der P09-SYN-Draft für einen unabhängigen pfadgebundenen Zweitcheck freigegeben.

\[
\boxed{\text{P09 SYN PRIMÄRCHECK — KEIN KERNGEGENBEFUND; 3 LOKALE PATCHES.}}
\]