# NEU-221 — Adelische Momentquelle für den positiven Weil-Operator

**Katalog-ID:** NEU-221
**Knoten:** [O-221-1-adelic-positive-moment-source]
**Vorgänger:** NEU-220w (Commit f1bce0f) — vollständiger Hankel-RH-Beweis, Moment-GNS-Modell, strategischer Pivot zur Quellkonstruktion
**Status:** Neuer Hauptknoten, Rückkehr zur konstruktiven Suche nach Objekt \(X\)

---

## 0. Methodischer Schutz: die Normalisierungs-Firewall

Der wichtigste Schutzmechanismus für diesen gesamten Knoten:

$$
\boxed{\text{Die ersten beiden Momente dürfen nicht durch Skalierung angepasst werden.}}
$$

### Warum ein Fitting-Risiko besteht

Seien für irgendeinen positiven Kandidaten \(a=\tau(T)>0\), \(b=\tau(T^2)>0\). Erlaubt man gleichzeitig \(T\mapsto cT\), \(\tau\mapsto d\tau\), so kann man stets \(c,d>0\) so wählen, dass \(dc\,a=\mu_0\), \(dc^2b=\mu_1\). Zwei Momente wären dann vollständig bedeutungslos.

**Firewall-Regel:** Vor jedem Vergleich müssen unabhängig fixiert sein:

$$
\boxed{\mathcal N_X,\quad \tau_X,\quad T_X,\quad \text{sämtliche Normierungen.}}
$$

Erst danach dürfen \(\mu_0,\mu_1\) ausgewertet werden. Ein Fehlschlag ist dann ein echter Negativbefund; ein Treffer ist zumindest nicht durch zwei freie Skalierungsparameter erzeugt.

---

## 1. Arbeitsvariable: \(T_X = B_X^{-1}\) statt \(B_X\)

Statt unmittelbar einen unbeschränkten Operator \(B_X\) zu suchen, ist der primäre Kandidat:

$$
\boxed{T_X:=B_X^{-1}\ge 0, \qquad T_X\in L^1(\mathcal N_X,\tau_X).}
$$

Zielmomente: \(\tau_X(T_X^{k+1})=\mu_k\), insbesondere

$$
\boxed{\tau_X(T_X)=\mu_0, \qquad \tau_X(T_X^2)=\mu_1.}
$$

### RH-freie Prüfwerte (aus zentralen \(\Xi\)-Ableitungen, keine Konstruktionsdaten)

$$
\mu_0 = \frac12(\log\xi)''\!\left(\frac12\right) \approx 0.023104993115419,
$$
$$
\mu_1 = -\frac1{12}(\log\xi)^{(4)}\!\left(\frac12\right) \approx 3.71725992853\times10^{-5},
$$
$$
\mu_2 \approx 1.44173931401\times10^{-7}, \qquad \mu_0\mu_2-\mu_1^2 \approx 1.94933555482\times10^{-9}>0.
$$

---

## 2. Screening der vorhandenen BC-/KMS-Kandidaten

### Kandidat A — primitiver Euleroperator \(\mathcal P_N(\beta)\)

\(\mathcal P_N(\beta)\varepsilon_p=p^{-\beta}\varepsilon_p\) ist positiv und BC-intrinsisch; seine verbundene Spur erzeugt korrekt die Mangoldt-Schicht \(-\partial_\beta\operatorname{Tr}^{\mathrm{conn}}\log(1-\mathcal P_N(\beta)) = \zeta_N'/\zeta_N(\beta)\). Als direkter \(T_X\)-Kandidat liefert er jedoch \(\operatorname{Tr}^{\mathrm{conn}}(\mathcal P_N(\beta)^k) = \sum_{p\le N}p^{-k\beta}\) — Primzahlzeta-Daten, nicht die zentralen \(\Xi\)-Momente. Es fehlen ihm \(\Gamma\)-Anteil, Polrenormierung, gekoppelte Spektralgeometrie.

$$
\boxed{\mathcal P_N(\beta) \text{ ist kein direkter } T_X\text{-Kandidat.}} \qquad \checkmark[M]_{\mathrm{neg}} \text{ als unmittelbarer positiver Weil-Momentoperator.}
$$

Er bleibt der richtige arithmetische Eingangsblock.

### Kandidat B — relativer modularer Clock \(e^{-sT_p^{\mathrm{rel}}}\)

NEU-42 konstruiert lokal \(T_p^{\mathrm{rel}}=\log p\) mit \(e^{-sT_p^{\mathrm{rel}}}=p^{-s}\) — eine echte BC-intrinsische Herkunft der Eulerexponentialfunktion. Die globale Realisierung auf dem vollständigen gekoppelten Quotienten war jedoch noch offen. Erzeugt zunächst lokale Größen \(p^{-s}\), nicht die positiven Spektralmomente \(\sum_\gamma\gamma^{-2k-2}\).

$$
\boxed{e^{-sT_p^{\mathrm{rel}}} \text{ ist lokaler Kanalbaustein, nicht } T_X \text{ selbst.}}
$$

### Kandidat C — KMS-Gibbsdichte \(e^{-\beta H_{\mathrm{BC}}}\)

Positiv und für geeignetes \(\beta\) spurklassig, aber ihre Momente sind Dirichlet-/Zeta-Werte bei Vielfachen von \(\beta\). Sitzt auf der unverbundenen KMS-Ebene, während Mangoldt erst durch die logarithmisch verbundene Euler-Spur entsteht (Ebenentrennung, NEU-39).

$$
\checkmark[M]_{\mathrm{neg}} \quad \text{als unmittelbares } T_X.
$$

### Kandidat D — relativer Feshbach-/Weyl-Spektralblock (stärkster Kandidat)

NEU-46 zeigt: Die Weyl-Funktionen \(M_p(z) = \langle\Psi_p,(z-D_p^{\mathrm{rel}})^{-1}\Psi_p\rangle\) verschwinden in einem nichttrivial gekoppelten Modell gerade nicht automatisch. Sie tragen die zyklischen Spektraldaten des relativen Jacobi-/Feshbach-Systems; die Determinante zerfällt in Euler-, Jacobi- und Streuanteil.

$$
\boxed{\text{Der Euleroperator liefert die arithmetische Seite;}}
$$
$$
\boxed{\text{die Weyl-/Feshbach-Komponente ist der vorhandene Kandidat für echte Spektralgeometrie.}}
$$

Es fehlen noch: ein positiver GNS-Sektor, eine globale Spur, eine gekoppelte archimedische Ergänzung, Spurklassigkeit des daraus gewonnenen \(T_X\), die Momentidentitäten.

$$
\boxed{D_{\mathrm{Spec}}^{\mathrm{rel}} = D_{\mathrm{Jac}}\cdot D_{\mathrm{scatt}}}
$$

ist noch kein \(T_X\), aber aktuell die sinnvollste Quellregion.

---

## 3. Was NEU-221 nicht tun sollte

NEU-221 sollte **nicht** einfach einen positiven Diagonaloperator definieren, dessen Eigenwerte nachträglich so gewählt werden, dass \(\tau(T_X)=\mu_0\), \(\tau(T_X^2)=\mu_1\). Ebenso wenig genügt \(T_X = c_1\mathcal P(\beta_1)\oplus c_2Q_\infty\) mit angepassten Konstanten — das wäre Momenten-Fitting, keine adelische Herleitung. Auch die ersten zwei Momente allein identifizieren den Operator nicht: unendlich viele positive Spurklasseoperatoren besitzen dieselben ersten beiden Momente.

$$
\boxed{\text{Die ersten Momente sind daher nur: frühe Falsifikationstests, keine Erfolgszertifikate.}}
$$

---

## 4. Struktur der Teilknoten

### NEU-221a — Kandidateninventar und Normierungs-Firewall

Für jeden Kandidaten wird \((\mathcal N,\tau,T)\) mit vollständig fixierter Normierung festgehalten. Prüfliste:

- Ist \(T\ge0\)?
- Ist \(T\) unabhängig von den Nullstellen definiert?
- Ist \(\tau\) positiv und kanonisch normiert?
- Ist \(T\in L^1(\mathcal N,\tau)\)?
- Sind \(\tau(T)\) und \(\tau(T^2)\) endlich?
- Sind keine freien Skalierungsparameter mehr vorhanden?

**Zentrales Ergebnis:**

$$
\boxed{\text{Der primitive Euleroperator und der relative Clock sind notwendige arithmetische Bausteine, aber kein direkter positiver Weil-Momentoperator.}}
$$

### NEU-221b — Negative Direktaudits

Direkt auszuschließen als \(T_X\): \(\mathcal P(\beta)\), \(e^{-\beta H_{\mathrm{BC}}}\), \(Q_\infty\) (als positiver \(T_X\)), sowie jede bloße direkte Summe ohne bewiesene Pol–Prim–Gamma-Kopplung.

### NEU-221c — relativer positiver Feshbach-Sektor

Erster ernsthafter Konstruktionsversuch: aus \(D_p^{\mathrm{rel}}\), \(C_p^{\mathrm{rel}}\), \(M_p(z)\) einen positiven zyklischen Operator oder ein positives Spektralmaß erzeugen. Nicht gesucht wird zunächst die gesamte \(\Xi\)-Identität, sondern ein kanonischer endlicher Kandidat \(T_{X,N}\ge0\) mit fixierter Spur \(\tau_{X,N}\).

### NEU-221d — archimedische Kopplung

Der endliche Kandidat darf nicht bloss um einen separaten Gammaoperator ergänzt werden. Es muss eine gemeinsame Konstruktion geben, deren logarithmische Determinante oder Resolventenspur gleichzeitig die bereits geschlossenen Beiträge reproduziert: Euler \(+\) \(\Gamma\) \(+\) Polrenormierung.

### NEU-221e — erster Momententest

$$
m_{0,N}:=\tau_{X,N}(T_{X,N}), \qquad m_{1,N}:=\tau_{X,N}(T_{X,N}^2).
$$

Ziel: \(m_{0,N}\longrightarrow\mu_0\), \(m_{1,N}\longrightarrow\mu_1\). Schon \(\lim m_{0,N}\neq\mu_0\) würde den Kandidaten ausschließen.

### NEU-221f — zweiter Hankeltest

Nach den ersten Momenten sollte unmittelbar \(\mu_2 \approx 1.44173931401\times10^{-7}\) einbezogen werden, sodass \(\mu_0\mu_2-\mu_1^2 \approx 1.94933555482\times10^{-9}>0\) geprüft werden kann. Damit wird erstmals nicht nur ein Einzelwert, sondern ein echter Positivitätszusammenhang getestet.

---

## 5. Kandidatenranking

| Kandidat | Rolle | Urteil |
|---|---|---|
| \(\mathcal P_N(\beta)\) | Euler-/Mangoldtquelle | kein direktes \(T_X\) |
| \(e^{-sT_p^{\mathrm{rel}}}\) | lokale Primexponentialquelle | Baustein |
| \(e^{-\beta H_{\mathrm{BC}}}\) | KMS-/Dirichletquelle | zu unverbunden |
| \(Q_\infty\) | \(\Gamma\)-Zeitverzögerung | nicht positiv allein |
| \(D_{\mathrm{Spec},N}^{\mathrm{rel}}, M_p\) | gekoppelte Spektralgeometrie | **stärkster Ausgangspunkt** |

Derzeit bester Ansatz:

$$
\boxed{\text{Euleroperator } \mathcal P_N + \text{relativer Feshbach-/Weyl-Sektor} + \text{archimedischer Streukanal}}
$$

nicht als direkte Summe, sondern als gemeinsame relative Determinanten- oder Resolventenkonstruktion.

---

## Knotenbaum

```
[O-221-1-adelic-positive-moment-source]
  -> [O-221-1a-normalization-firewall-and-candidate-screen]  ✓[K/M] (dieses Dokument)
       - Kandidat A (Euler P_N):        kein direktes T_X, notwendiger Baustein
       - Kandidat B (rel. Clock):       lokaler Kanalbaustein
       - Kandidat C (KMS-Gibbs):        zu unverbunden, negativ
       - Kandidat D (Feshbach/Weyl):    stärkster Kandidat, noch kein T_X
  -> [O-221-1b-negative-audits]                                ?[O]
  -> [O-221-1c-relative-positive-Feshbach-sector]               ?[O]
  -> [O-221-1d-archimedean-coupling]                            ?[O]
  -> [O-221-1e-first-moment-test]                               ?[O]
  -> [O-221-1f-second-Hankel-test]                              ?[O]
```

---

## Statusübersicht

| Aussage | Status |
|---|---|
| Normalisierungs-Firewall formuliert | ✓[K/M] |
| \(T_X=B_X^{-1}\) als Arbeitsvariable | ✓[K/M] |
| RH-freie Prüfwerte \(\mu_0,\mu_1,\mu_2\) berechnet | ✓[K/M] |
| \(\mathcal P_N(\beta)\) als \(T_X\) | ✓[M]_neg |
| \(e^{-\beta H_{\mathrm{BC}}}\) als \(T_X\) | ✓[M]_neg |
| \(e^{-sT_p^{\mathrm{rel}}}\) als \(T_X\) | ✓[M]_neg (Baustein) |
| Feshbach-/Weyl-Sektor als Quellregion | ✓[K/M]_part, staerkster Kandidat |
| Konkrete Konstruktion von \(T_{X,N}\ge0\) | ?[O] |
| Momententest \(m_{0,N}\to\mu_0\), \(m_{1,N}\to\mu_1\) | ?[O] |

---

## Abhängigkeiten

| Referenz | Inhalt |
|---|---|
| NEU-220w (f1bce0f) | Vollständiger Hankel-RH-Beweis, Moment-GNS-Modell, Zielwerte \(\mu_k\) |
| NEU-39 | Ebenentrennung KMS/verbundene Euler-Spur |
| NEU-42 | Relativer modularer Clock, lokale Primexponentialquelle |
| NEU-46 | Weyl-Funktionen \(M_p(z)\), relativer Feshbach-/Jacobi-Sektor |
| NEU-219 | Kanonischer geladener zyklischer Lift liefert nicht die gesuchte Verbindung |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
