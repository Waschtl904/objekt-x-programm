# NEU-219u — Abschlussaudit der geladenen zyklischen Architektur

**Stand:** 24. Juli 2026  
**Repository:** Waschtl904/rh-fragenkatalog  
**Typ:** Abschlussaudit, Synthese und DAG-Revision  
**Vorgänger:** NEU-219l bis NEU-219t sowie METHODIK_O219_Strukturdiagnose.md

---

## 0. Zweck und Auditgrenze

Der O-219-Strang untersucht, ob der bereits konstruierte geladene Hochschild-(4)-Kozykel
$$
D_g \smile \Theta^\wedge_{p_1,p_2,p_3} \in Z^4(A_{\mathrm{alg}},M)_g
$$
über die adelische Ecke, Morita-Induktion, eine orbit-markierte Koeffizientenrealisierung und ein KMS-Modulgewicht in eine gewöhnliche skalare zyklische (4)-Klasse überführt werden kann.

Das Ergebnis ist zweigeteilt:

- Die geladene Hochschild-, Eck-, Morita-, Orbit- und Modulgewichtsarchitektur ist weitgehend typkorrekt konstruiert.
- Der kanonische Basislift besitzt keinen Orbitshift. Deshalb ist seine skalare Auswertung unabhängig von jedem Orbitgewicht $\lambda$. Unter der in NEU-219t behaupteten globalen Rotationsidentität
$$
t\Phi_0 = g^{-\beta}\Phi_0
$$
kann das verbleibende KMS-Eigengewicht nicht durch $\lambda$ kompensiert werden.

Dieses Abschlussaudit nimmt **zwei Präzisierungen** und eine **Auditgrenze** vor.

### Auditkorrektur A — Typ der Recovery-Identität

Die wörtliche Formel $\Pi_0 \circ \eta_0 = \operatorname{id}_{M_0}$ ist bei der deklarierten Zielabbildung $\Pi_0 \to N_0$ nicht streng typgleich. Die exakt typisierte Aussage lautet:
$$
\boxed{\Pi_0 \circ \eta_0 = \iota_{M_0 \hookrightarrow N_0},} \tag{0.1}
$$
wobei $\iota_{M_0 \hookrightarrow N_0}$ die kanonische Inklusion bezeichnet. Nach Eckkompression und der Identifikation $eN_0e = M_0$ gilt äquivalent:
$$
\boxed{(e\Pi_0 e) \circ \eta_0 = \operatorname{id}_{M_0}.} \tag{0.2}
$$
Die Injektivität von $\eta_0$ bleibt vollständig erhalten.

### Auditkorrektur B — Bedingung $g^{-\beta} \neq 1$

Aus $g \neq 1$ allein folgt nicht für jeden denkbaren Parameter $\beta$, dass $g^{-\beta} \neq 1$; bei $\beta = 0$ wäre der Faktor gleich $1$. Im hier verwendeten BC-KMS-Regime gilt jedoch $\beta > 1$. Daher ist die korrekte Aussage:
$$
\boxed{g \in \mathbb{Q}_+^\times,\quad g \neq 1,\quad \beta > 1 \quad\Longrightarrow\quad g^{-\beta} \neq 1.} \tag{0.3}
$$

### Auditgrenze C — vollständige NEU-219t-Buchführung

Der aktuelle Auditquellensatz enthält die Zusammenfassung und das Endresultat von NEU-219t, aber nicht die vollständige zeilenweise homogene Rechnung mit allen Faktoren $h_i^{\pm\beta}$. Daher wird streng getrennt zwischen:

- der **bewiesenen logischen Konsequenz** der Rotationsidentität;
- und der erneut unabhängig zu zertifizierenden Prämisse $(\mathcal{R})$: $t\Phi_0 = g^{-\beta}\Phi_0$ auf allen homogenen Eingaben.

Die Konsequenz von $(\mathcal{R})$ ist vollständig geprüft. Die erneute Primärprüfung von $(\mathcal{R})$ wird als letzter atomarer Abschlussknoten vor dem Übergang zu $[O\text{-}219\text{-}6]$ isoliert.

---

## 1. Verbindliche Konventionen

$$
B_{\mathrm{alg}} = \mathbb{C}[\mathbb{Q}/\mathbb{Z}], \qquad A_{\mathrm{alg}} \subseteq A_{C^*},
$$
$$
\rho_k(f)(x) = 1_{k\widehat{\mathbb{Z}}}(x) f(x/k), \qquad \rho_k(1) = E_k, \qquad \sigma_k(f) = \mu_k^* f \mu_k,\quad (\sigma_k f)(x) = f(kx).
$$

$\rho_k$ und $\sigma_k$ sind **nicht** austauschbar. Die Ladungsgradierung ist die $\Gamma$-Gradierung:
$$
\Gamma = \mathbb{Q}_+^\times, \qquad \deg(\mu_n) = n, \qquad \deg(\mu_n^*) = n^{-1}.
$$

Die adelische Dilatationsalgebra ist $C_0(\mathbb{A}_f) \rtimes_\gamma \mathbb{Q}_+^\times$ mit
$$
(\gamma_r F)(a) = F(r^{-1}a), \qquad U_r F U_r^* = \gamma_r(F), \qquad U_r U_s = U_{rs}, \qquad \widetilde{\sigma}_\beta(U_r) = r^\beta U_r.
$$

Für $e = 1_{\widehat{\mathbb{Z}}}$ gilt die $C^*$-Eckenidentifikation $A_{C^*} \cong e\widetilde{A}e$. Auf dem algebraischen Kern:
$$
R := \widetilde{A}_{\mathrm{alg}}, \qquad B := eRe.
$$

---

## 2. Zentrales Abschlusstheorem

**Satz 219u.1 — Geladene Hochschildarchitektur und kanonische zyklische Obstruktion.**

*Seien $g \in \mathbb{Q}_+^\times$, $g \neq 1$, $\beta > 1$, und seien $p_1, p_2, p_3$ drei verschiedene Primzahlen. Es gelte:*
$$
[D_g] \in HH^1(A_{\mathrm{alg}},M)_g \setminus \{0\}, \qquad \Theta^\wedge_{p_1,p_2,p_3} \in Z^3(A_{\mathrm{alg}},A_{\mathrm{alg}})_1,
$$
$$
L^{\mathrm{cup}}_{g;\mathbf{p}} = D_g \smile \Theta^\wedge_{p_1,p_2,p_3} \in Z^4(A_{\mathrm{alg}},M)_g.
$$

*Dann gelten:*

**(A)** $L^{\mathrm{cup}}_{g;\mathbf{p}} \in Z^4(A_{\mathrm{alg}},M)_g$. ✓[M]

**(B)** Exakte adelische Ecke: $eRe = j_A(A_{\mathrm{alg}})$, Morita-Bimodule $Re$, $eR$, Einzelisomorphismen $\Pi_k: I_k \xrightarrow{\cong} N_k$. ✓[K/M]

**(C)** Orbitmarkierung notwendig: $N_k = N_0$ für alle $k$, globale unmarkierte $\Pi$-Injektivität scheitert, orbit-markierte Realisierung $\mathcal{N}_{\mathrm{tag}} = \bigoplus_k N_0 \delta_k$ mit $T(x\delta_k) = x\delta_{k+1}$. ✓[K/M]

**(D)** Vollständige Familie orbit-markierter Modulgewichte: $\varpi_{\beta,\chi}$, $\Omega_\lambda$ mit $\Omega_\lambda \circ T = \lambda \Omega_\lambda$. ✓[K/M]

**(E)** Kanonischer Basislift:
$$
\widetilde{L}_0 := \eta_0 \circ j_M \circ L^{\mathrm{cup}}_{g;\mathbf{p}}: A_{\mathrm{alg}}^{\otimes 4} \longrightarrow I_0,
$$
$$
\boxed{\widetilde{L}_0 \in Z^4(A_{\mathrm{alg}}, I_0).}
$$
Recovery-Identität typkorrigiert zu $\Pi_0 \circ \eta_0 = \iota_{M_0 \hookrightarrow N_0}$, bzw. $(e\Pi_0 e) \circ \eta_0 = \operatorname{id}_{M_0}$. ✓[K/M]

**(F)** Trennung von $\Gamma$-Grad und Orbitindex:
$$
\boxed{\deg_\Gamma(\widetilde{L}_0) = g, \qquad \operatorname{supp}_{\mathrm{orb}}(\widetilde{L}_0) = \{0\},}
\qquad \kappa = 0, \qquad \varepsilon = 0. \quad \checkmark[M]
$$

**(G)** Bedingte gewöhnliche Zyklizitätsobstruktion: Unter $(\mathcal{R})$ gilt $s = -1$, $C = g^{-\beta} \neq 1$, und kein $\lambda$ kann kompensieren:
$$
\boxed{\text{kanonischer Basislift} + \text{Orbitgewicht} \not\Longrightarrow \text{gewöhnliche zyklische Klasse}.}
$$
Die Implikation $(\mathcal{R}) \Rightarrow$ Nichtzyklizität ist ✓[M]. Die Primärprüfung von $(\mathcal{R})$ ist gesperrt. $\square$

---

## 3. Detailaudit des kanonischen Lifts

### 3.1 Typen

$$
L^{\mathrm{cup}}: A_{\mathrm{alg}}^{\otimes 4} \to M, \qquad j_M: M \to M_0, \qquad \eta_0: M_0 \to I_0.
$$

Komposition $\widetilde{L}_0 = \eta_0 \circ j_M \circ L^{\mathrm{cup}}$ streng typisiert: $A_{\mathrm{alg}}^{\otimes 4} \to M \to M_0 \to I_0$. Keine nichtkonstruierte Abbildung benutzt.

### 3.2 $B$-Bilinearität von $\eta_0$

Für $b, c \in B$, $m \in M_0$:
$$
b \cdot \eta_0(m) \cdot c = be \otimes_B m \otimes_B ec = e \otimes_B bmc \otimes_B e = \eta_0(bmc).
$$

### 3.3 Recovery-Identität (typkorrigiert)

$$
\Pi_0(\eta_0(m)) = \Pi_0(e \otimes_B m \otimes_B e) = eme = m \in M_0 \subseteq N_0.
$$
Exakte Formel: $\Pi_0 \circ \eta_0 = \iota_{M_0 \hookrightarrow N_0}$. Daher $\eta_0$ injektiv.

### 3.4 Kozykelerhalt

Da $\eta_0 \circ j_M$ ein $A_{\mathrm{alg}}$-Bimodulhomomorphismus ist:
$$
b_{I_0}(\widetilde{L}_0) = (\eta_0 \circ j_M)_* \circ b_M(L^{\mathrm{cup}}) = 0.
$$

---

## 4. Zwei unabhängige Gradbegriffe

| Begriff | Bedeutung | Änderung durch |
|---|---|---|
| $\Gamma$-Grad | BC-Ladung $g \in \mathbb{Q}_+^\times$ | Algebraische Operationen |
| Orbitindex $k \in \mathbb{Z}$ | Externer Marker in $\mathcal{N}_{\mathrm{tag}}$ | Shift $T$ |

**Konsequenz:** Die Gleichsetzung „Ladung $g \Leftrightarrow$ Orbitshift um $1$" ist falsch. Für den kanonischen Lift gilt gleichzeitig $\deg_\Gamma(\widetilde{L}_0) = g$ und $\widetilde{L}_0(A_{\mathrm{alg}}^{\otimes 4}) \subseteq I_0$.

---

## 5. Warum kein $\lambda$-Faktor auftreten kann

Auf dem $k$-ten Summanden: $\widehat{\Omega}_\lambda(\xi) = \lambda^k \widetilde{\omega}_{\beta,\chi}(U_{g^{-1}} \Pi_k(\xi))$ für $\xi \in I_k$.

Für den kanonischen Lift liegt stets $k = 0$ vor:
$$
\boxed{\widehat{\Omega}_\lambda \circ \widetilde{L}_0 = \widehat{\Omega}_1 \circ \widetilde{L}_0 \qquad \text{für alle } \lambda \in \mathbb{C}^\times.} \tag{5.1}
$$

Die gesamte skalare Cochain ist auf dem kanonischen Basislift exakt $\lambda$-unabhängig.

---

## 6. Rotationsfaktor und Implikationskette

Allgemeiner Faktor: $C = \lambda^\varepsilon g^{s\beta}$.

Für den kanonischen Basislift:
$$
\boxed{L^{\mathrm{cup}} \longrightarrow \widetilde{L}_0 \longrightarrow \kappa=0 \longrightarrow \varepsilon=0.} \tag{6.1}
$$

Unter $(\mathcal{R})$:
$$
\boxed{L^{\mathrm{cup}} \longrightarrow \widetilde{L}_0 \longrightarrow \kappa=0 \longrightarrow \varepsilon=0 \overset{(\mathcal{R})}{\longrightarrow} s=-1 \longrightarrow C = g^{-\beta} \neq 1.} \tag{6.3}
$$

Der Teil bis $\varepsilon = 0$ ist im vorliegenden Audit vollständig unabhängig geprüft. Der Pfeil zu $s = -1$ ist der Inhalt von $[O\text{-}219\text{-}5e1i]$.

---

## 7. Was exakt ausgeschlossen ist

| Aussage | Status |
|---|---|
| Eckkompressionen als Orbitseparator | ✓[M]neg |
| Globale unmarkierte $\Pi$-Injektivität | ✓[M]neg |
| Erfundene bedingte Erwartung $\Phi \to R$ | Gesperrt (kein allg. No-go) |
| $U_{g^{-1}} = T^{-1}$ auf $\mathcal{N}_{\mathrm{tag}}$ | ✓[M]neg |
| Kanonischer Basislift + Orbitgewicht $\Rightarrow$ gew. zyklische Klasse | ✓[M]neg (unter $(\mathcal{R})$) |

Ausgeschlossen ist nicht jeder denkbare Lift, sondern genau die Kombination: kanonischer Lift über $\eta_0$, Bild in $I_0$, skalare direkte KMS-Auswertung, Reparatur nur durch $\Omega_\lambda$, gewöhnliche unverdrillte Zyklizität $t\Phi = \Phi$.

---

## 8. Was nicht ausgeschlossen ist

- **Genuin orbitverschiebender Lift** mit $\varepsilon \neq 0$ (erfordert explizit $T^k$, $\tau^k$, neue Typisierung)
- **Andere Koeffizientenkategorie** (SAYD, Hopf-zyklisch, bornologisch, Gruppenoid)
- **Parazyklische/modulare Zielstruktur** mit $t_\beta \Phi_0 = \Phi_0$
- **Algebraische Neutralisierung** vor der Paarung ($M_g \otimes M_{g^{-1}} \to M_1$)
- **Weil-/Gammafaktorpfad** $[O\text{-}219\text{-}6]$ — vollständig unberührt

---

## 9. Vollständiger revidierter DAG

| Knoten / Aussage | Repo-Status | Revidierter Auditstatus | Bemerkung |
|---|---|---|---|
| $[D_g] \neq 0$, $\Theta^\wedge$, $L^{\mathrm{cup}} \in Z^4$ | ✓[M] | ✓[M] | Voraussetzung vor O-219 |
| $eRe = j_A(A_{\mathrm{alg}})$, Normalform | ✓[K/M] | ✓[K/M] | Exakte $\rho/\sigma$-Trennung |
| Einzelne $\Pi_k \to N_k$ | ✓[K/M] | ✓[K/M] | Bimodulisomorphismen |
| $N_k = N_0$, globale $\Pi$-Injektivität neg. | ✓[M]neg | ✓[M]neg | Differenzkern |
| Orbit-markierte Realisierung $\mathcal{N}_{\mathrm{tag}}$ | ✓[K/M] | ✓[K/M] | Index extern erhalten |
| $\varpi_{\beta,\chi}$, $\Omega_\lambda$ | ✓[K/M] | ✓[K/M] | KMS-Relation geprüft |
| $c_k = g^{-k\beta}$ aus bloßer Bimodulidentität | — | ✓[M]neg | Erst Shiftrelation erzwingt Rekursion |
| $U_{g^{-1}} = T^{-1}$ | ✓[M]neg | ✓[M]neg | Multiplikation erhält $k$ |
| $C = \lambda^\varepsilon g^{s\beta}$ (NEU-219o/p) | ✓[K] | ✓[K/M] | Exponenten sauber getrennt |
| Fehlende Definition $\widetilde{L}$ (NEU-219q) | ✓[M]neg,Quelle | ✓[M]neg,Quelle | In NEU-219r repariert |
| $\eta_0$ $B$-bilinear, injektiv (NEU-219r) | ✓[K] | ✓[K/M] | — |
| $\Pi_0 \eta_0 = \operatorname{id}_{M_0}$ (wörtlich) | ✓[M] | **revidiert** | Typkorrekt: Inklusion $M_0 \hookrightarrow N_0$ |
| $(e\Pi_0 e)\eta_0 = \operatorname{id}_{M_0}$ | — | ✓[M] | Eckkomprimierte Form |
| Typ $\widetilde{L}_0$, Kozykelbedingung | ✓[M] | ✓[M] | — |
| $\kappa = 0$, $\varepsilon = 0$ | ✓[M] | ✓[M] | $\Gamma$-Grad $\neq$ Orbitindex |
| $\widehat{\Omega}_\lambda \circ \widetilde{L}_0 = \widehat{\Omega}_1 \circ \widetilde{L}_0$ | — | ✓[M] | $\lambda^0 = 1$ |
| $\Phi_0$, $t\Phi_0$ (NEU-219s) | ✓[K/M] | ✓[K/M] | $(-1)^4 = 1$ |
| $t\Phi_0 = g^{-\beta}\Phi_0$ global (NEU-219t) | ✓[M] | **gesperrt** | Vollständige Primärrechnung fehlt |
| $s = -1$ (Folgerung aus $(\mathcal{R})$) | ✓[M] | ✓[M] bedingt | — |
| $g^{-\beta} \neq 1$ | ✓[M] | ✓[M] für $g\neq1$, $\beta>1$ | Parameterbedingung präzisiert |
| $[O\text{-}219\text{-}r3]$: Basislift nicht zyklifizierbar | ✓[M]neg | ✓[M] als Implikation aus $(\mathcal{R})$ | Prämisse gesperrt |
| $[O\text{-}219\text{-}6]$: Weil-/Gammafaktorpaarung | ?[O] | ?[O], zurückgestellt | Nach $[O\text{-}219\text{-}5e1i]$ |

---

## 10. Letzter notwendiger Abschlussknoten

$$
\boxed{[O\text{-}219\text{-}5e1i\text{-typed-global-rotation-audit}] \quad ?[O]}
$$

**Auftrag:** Erstelle eine quellenunabhängig lesbare Rechnung für alle homogenen Eingaben $a_i \in (A_{\mathrm{alg}})_{h_i}$, $h_i \in \Gamma$, und beweise oder widerlege global $t\Phi_0 = g^{-\beta}\Phi_0$.

**Die Datei muss zwingend enthalten:**
- Genaue homogene Kovarianzformel für $L^{\mathrm{cup}}(a_0,\ldots,a_3)$
- Genaue Relation zwischen Ausgangsgrad und $g, h_0,\ldots,h_4$
- Jede Anwendung der inversen KMS-Identität
- Jede Verschiebung von $U_{g^{-1}}$
- Alle entstehenden Faktoren $h_i^{\pm\beta}$ und ihre paarweise Aufhebung
- Verbleibende Potenz von $g^\beta$
- Explizite Feststellung: kein $T^{\pm 1}$ kommt vor
- Daraus folgende $\lambda$-Unabhängigkeit
- Typkorrektur $\Pi_0 \eta_0 = \iota_{M_0 \hookrightarrow N_0}$

**Entscheidungsgabel:**

| Ergebnis | Konsequenz |
|---|---|
| $t\Phi_0 = g^{-\beta}\Phi_0$ bestätigt | $[O\text{-}219\text{-}r3]$ ✓[M]neg endgültig |
| Anderer konstanter Faktor | $s$ revidieren |
| Eingabeabhängiger Faktor übrig | Globale Eigenrelation falsch; NEU-219t zurückrollen |
| Echter Shift $T^\varepsilon$ | $\varepsilon = 0$ revidieren |

---

## 11. Übergang zu $[O\text{-}219\text{-}6]$

Nach Abschluss von $[O\text{-}219\text{-}5e1i]$:

$$
\boxed{[O\text{-}219\text{-}6]: \quad \text{Weil-/Gammafaktorpaarung aus der adelischen/KMS-Architektur.}}
$$

Zu trennen: nichtarchimedische Primzahlpotenzbeiträge, archimedische Gamma- und Polterme, Positivitätsraum, Skalierungsgenerator, modulare/parazyklische Kohomologiestruktur.

Optionaler Nebenpfad: $[O\text{-}219\text{-}5e2\text{-genuine-orbit-shifting-lift}]$ — nicht Voraussetzung für den Weil-/Gammafaktorpfad.

---

## 12. Gesamturteil

$$
\boxed{\text{geladener Hochschild-Kozykel} \neq \text{gewöhnliche skalare zyklische Klasse}.}
$$

**Positiv konstruiert:**
$$
L^{\mathrm{cup}}, \quad eRe, \quad Re/eR, \quad I_k, \quad \mathcal{N}_{\mathrm{tag}}, \quad \varpi_{\beta,\chi}, \quad \Omega_\lambda, \quad \widetilde{L}_0.
$$

**Negativ entschieden:**
$$
\text{Eckseparator}, \quad \text{globale unmarkierte } \Pi\text{-Injektivität}, \quad \text{erfundene Erwartung}, \quad U_{g^{-1}} = T^{-1}.
$$

**Unabhängig geprüft (ohne $(\mathcal{R})$):**
$$
\kappa = 0, \qquad \varepsilon = 0, \qquad \widehat{\Omega}_\lambda \circ \widetilde{L}_0 \text{ ist unabhängig von } \lambda.
$$

**Unter $(\mathcal{R})$:**
$$
s = -1, \qquad C = g^{-\beta} \neq 1, \qquad \text{gewöhnliche Zyklizitätsobstruktion.}
$$

Die einzig verbleibende methodische Pflicht vor $[O\text{-}219\text{-}6]$: vollständige Primärzertifizierung der globalen Rotationsidentität in $[O\text{-}219\text{-}5e1i]$.

---

**Commit-Referenz:** Nachfolger von NEU-219t (759d515) und NEU-219u erste Version (465141f).  
**Letzter offener Knoten:** $[O\text{-}219\text{-}5e1i\text{-typed-global-rotation-audit}]$ — ?[O].
