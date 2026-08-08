# P07 — Weil-Form Statistics:
Correlation Channels, Form-Factor Limits and Herglotz Interfaces

**Status:** Patch 1/1 (8. August 2026) — SYN-Direktaudit nach Pass-A NEU-091–120
**Basis:** PASS-A-PROTOKOLL.md (Abschlusscommit `baa3975b`)
**Patch-Commit:** siehe unten — 9 Verdichtungsfehler aus Skelett-Version korrigiert

---

## Abstract

Wir organisieren die quadratische Weilform-Statistik in fünf konzeptionellen Schichten:
den quadratischen Pivot (Positivität, Testkegel),
die Korrelationsstruktur (Bochner-Lift, Skalenanalyse),
den Formfaktor-/Rampenkanal (GM-Normierung, LFF, offener Symboltest),
das Herglotz-Interface (lineare Distribution ↔ quadratische Form),
und die konditionale Jacobi-Realisierungsarchitektur.
Fehler aus der historischen Entwicklung sind im Pass-A-Prozess korrigiert;
P07 enthält nur den heute gültigen mathematischen Stand.

---

## §1 — Quadratischer Pivot und Positivitätsrahmen

*Basis: NEU-091, NEU-092*

**Satz 1.1 (Determinanten-No-Go und quadratischer Pivot — getrennte Aussagen).**

> **Patch-Notiz §1.1:** Das Skelett hatte Determinantenweg und $Q_N$-Pivot zu einem Objekt
> $Q_N[\phi]=\det(I+K_N[\phi])-1$ verschmolzen. Das ist ein SYN-Transkriptionsfehler:
> Pass-A-Ergebnis war gerade, dass der Determinantenweg als direkte Realisierung
> **No-Go** ist; danach wird $Q_N$ als eigenständiges Mangoldt-/Quadratikobjekt eingeführt.

*(i)* **No-Go (Determinantenweg):** Der Ansatz $Q_N[\phi]\stackrel{?}{=}\det(I+K_N[\phi])-1$
scheitert als direkte Realisierung des quadratischen Pivots. [NEU-091: ✓[M]$_{\rm neg}$]

*(ii)* **Quadratischer Pivot (positiv):** $Q_N$ wird als Mangoldt-Autokorrelations-Quadratikobjekt
neu eingeführt, unabhängig vom Determinantenansatz. [NEU-091: ✓[M]]

**Satz 1.2 (Testkegel-Positivität — Lift offen).**

> **Patch-Notiz §1.2:** Das Skelett hatte den bilinearen Lift $B_N(f,g)$ bereits als
> positiv-semidefinit gebucht. Pass-A-Befund zu NEU-092: Testkegel-Positivität ✓,
> aber der echte Lift mit Kreuzterm $\Lambda(m)\Lambda(n)$ bleibt offen.

*(i)* **Testkegel:** $Q_N[\phi]\geq 0$ für $\phi\in\mathcal C$ (Testkegel). [NEU-092: ✓[M]]

*(ii)* **Bilinearer Lift:** $B_N(f,g)$ mit vollen Kreuzterme $\Lambda(m)\Lambda(n)$
positiv-semidefinit auf $\mathcal S$: **?[O]** [NEU-092]

---

## §2 — Korrelationsstruktur und Skalenanalyse

*Basis: NEU-093–100*

**Satz 2.1 (Bochner-Lift).**

> **Patch-Notiz §2.1:** Die auditierten Objekte sind $\rho_N$ (Mangoldt-Autokorrelationsdichte)
> und $\Psi_N$ (zugehörige Spektralmaß-/Bochner-Darstellung).
> Diese werden hier präzise verwendet, nicht umschrieben.

Die Mangoldt-Autokorrelationsdichte $\rho_N(h)=\frac1N\sum_{n\leq N}\Lambda(n)\Lambda(n+h)$
ist positiv-definit im Bochner-Sinn; die zugehörige spektrale Darstellung $\Psi_N$
ist wohltypisiert. [NEU-093/094: ✓[M]]

**Satz 2.2 (Skalendekomposition mit auditierten Variablen).**

> **Patch-Notiz §2.2:** Das Skelett hatte $h\ll N$, $h\sim N$, $h\gg N$ erfunden.
> Die bereinigte Gruppe B arbeitet mit $T=M_N^\theta$ als Skalenvariable und
> den drei Regimen $T=O(1)$, $1\ll T\ll M_N$, $T\gg M_N$.

Die Skalendekomposition verwendet $M_N$ (Kurzintervallparameter) und $T=M_N^\theta$:

- $T=O(1)$: Singulärserien-dominierter Hauptterm
- $1\ll T\ll M_N$: Übergangsregime; selbstduale Skala bei $T\sim M_N^{1/2}$
- $T\gg M_N$: Restdichte $\Delta_N$, Übergang zum Shift-Spektrum

[NEU-095–100: ✓[M]]

**Konditional:** Hardy–Littlewood-Hauptterm unter Siebheuristik. [NEU-098: ✓[M]$_{\rm neg}$ für No-Go; Hauptterm konditional]

---

## §3 — Formfaktor-/Rampenkanal: Kalibrierung, Grenzen, offener Symboltest

*Basis: NEU-101–110*

**Def. 3.1 (GM-Kurzintervallvarianz).**

> **Patch-Notiz §3.1:** Das Skelett hatte den historischen Fehler als „$H\log N$ statt
> $H\log(M/H)$" beschrieben. Korrekt: Der Fehler war ein falsch eingesetzter Faktor
> $H/M$ (also $\frac{H}{M}\log(M/H)$ statt $H\log(M/H)$).
> Außerdem: Standardgröße ist die Kurzintervallvarianz $V(M,H)$, nicht ein neu
> eingeführtes $S_{N,H}^{\rm corr}$.

Die Kurzintervallvarianz
$$V(M,H) := \frac1M\sum_{m\leq M}\left(\sum_{m<n\leq m+H}\Lambda(n)-H\right)^2$$
hat den Hauptterm
$$\boxed{V(M,H)\sim H\log(M/H)\qquad(H\leq M).}$$
Historischer Fehler: Faktor $H/M$ in der Normierung erzeugte $\frac HM\log(M/H)$.
[NEU-101: ✓[M] nach Patch]

**Def. 3.2 (Lokales Formfaktor-Ersatzobjekt).**

> **Patch-Notiz §3.2:** Das Skelett führte ein undefiniertes $F_{\rm loc}(\xi)$ ein.
> Pass-A-Ergebnis: Das globale $\mathcal S_{N,H}$ ist verworfen; das geprüfte Objekt
> ist $\mathcal P^{\rm unf}_{N,H}$ (unnormalisiertes lokales Ersatzobjekt) bzw.
> lokale Fenstertests.

Das lokale Formfaktor-Ersatzobjekt $\mathcal P^{\rm unf}_{N,H}$ (unnormalisiert, lokal) ersetzt
das global normierte $\mathcal S_{N,H}$ (verworfen). Lokale Fenstertests sind wohltypisiert. [NEU-104: ✓[M]$_{\rm part}$]

**Satz 3.3 (Rampenasymptotik, einseitig).**
Aus LFF $= 1$ folgt universelle Rampenmassenasymptotik;
die Umkehrung ist nicht bewiesen. [NEU-107: ✓[M]$_{\rm part}$]

**Satz 3.4 (LFF-Typisierungswarnung).**

> **Patch-Notiz §3.4:** Das Skelett schrieb „Rampenform ist kein Selbstadjungiertheitsbeweis".
> Der NEU-108-Befund betrifft nicht Selbstadjungiertheit, sondern:

$$\boxed{\text{LFF allein konstruiert oder identifiziert }Q_{\rm Weil}\text{ nicht.}}$$

[NEU-108: ✓[M]$_{\rm part}$ nach Patch]

**Offen (Symboltest).**
$$\sigma_{\rm loc}(Q_{\rm Weil}) \stackrel{?}{=} |\alpha|. \qquad ?[O]$$
Weder Ausgang A noch Ausgang B bewiesen. [NEU-110]

---

## §4 — Linearer Herglotz-Kanal versus quadratische Weil-Geometrie

*Basis: NEU-111–115; kanonische Ebene: P02*

**Def. 4.1 (Herglotz-Funktion — Konvergenzform).**

> **Patch-Notiz §4.1:** Das Skelett schrieb
> $m_{\rm arith}(z)=\sum_\gamma m_\gamma/(\gamma-z)=\int d\mu_{\rm arith}/(t-z)$
> ohne Konvergenzangabe. Da $\mu_{\rm arith}$ unendliche Gesamtmasse hat,
> ist dies kein absolut konvergentes Stieltjes-Integral.
> Die mathematisch korrekte Form ist die symmetrische Herglotz-Nevanlinna-Darstellung.
> (Kein Rückfall in den Gamma-Fehler: $\mu_{\rm arith}$ bleibt rein atomar.)

Unter RH:
$$\boxed{m_{\rm arith}(z) = A + \int_{\mathbb R}\left(\frac1{t-z}-\frac{t}{1+t^2}\right)d\mu_{\rm arith}(t),}$$
wobei $\mu_{\rm arith}=\sum_{\gamma\in\Gamma}m_\gamma\delta_\gamma$ das **reine Nullstellenmaß** ist
(keine Gamma-/Pol-/Primbeiträge) und $A=\Re\, m_{\rm arith}(i)$ eine reelle Konstante.
Die Summe $\sum_\gamma m_\gamma/(\gamma-z)$ konvergiert im kanonisch symmetrischen Sinn. [NEU-111, NEU-112, NEU-118: ✓[M] nach Patches]

**Satz 4.2 (Herglotz $\Leftrightarrow$ RH).**
$$m_{\rm arith}\text{ ist Herglotz} \quad\Longleftrightarrow\quad \text{RH.}$$
[NEU-111.1: ✓[M]]

**Def. 4.3 (Normierte Weil-Distribution).**
$$W_\xi^{\rm norm} = W_{\rm zeros} = W_{\rm pole/triv}+W_\Gamma+W_{\rm prime}.$$
Nullstellenseite und arithmetische Seite: äquivalente Darstellungen, nicht addieren. [NEU-113, NEU-115: ✓[M]]

**Satz 4.4 (Kanonische Positivierungsbrücke).**

> **Patch-Notiz §4.4:** Das Skelett schrieb „dies ist die *einzige* korrekte Brücke".
> Bewiesen ist nur, dass $\Phi=\phi^**\phi$ eine kanonische Positivierungsbrücke liefert.
> Dass keine andere Realisierung existieren kann, ist nicht bewiesen.

$$\Phi=\phi^**\phi\quad\Longrightarrow\quad
W_\xi^{\rm norm}[\Phi] = Q_{\rm zeros}[\phi] = \sum_{\gamma\in\Gamma}m_\gamma|\widehat\phi(\gamma)|^2.$$
Dies ist die **kanonische** Positivierungsbrücke (nicht nachgewiesen: Einzigkeit). [NEU-112/113/115: ✓[M]; kanonisiert in P02]

**Satz 4.5 (Interface-Schutzsatz).**
$$m_{\rm arith}\rightsquigarrow W_\xi^{\rm norm}
\quad\text{und getrennt}\quad
a\to g_{a,b}\to h_{a,b}\to B_W(a,b).$$
P02 liefert die kanonische Definitionsebene.

**Offen.** $m_{\rm arith}=\Pi_\gamma(X)$: ?[O] — Rückbindungstests A/B/C offen. [NEU-114]

---

## §5 — Jacobi-/Herglotz-Realisierung: konditionale Architektur

*Basis: NEU-118–120*

**Def. 5.1 (Spektralmaß, konditional).** Falls $A_N^{\rm Jac,-}$ selbstadjungiert:
$$m_{\Omega,N}(z) = \langle\Omega_N,(A_N^{\rm Jac,-}-z)^{-1}\Omega_N\rangle
= \int_{\mathbb R}\frac{d\mu_{\Omega,N}(\lambda)}{\lambda-z}.$$
[NEU-119.1: ✓[M] konditional]; $\mu_{\Omega,N}(\mathbb R)=1$ (normiertes Maß).

**Offen (Selbstadjungiertheit).** Der konkrete Kandidat
$A_N^{\rm Jac,-}=H_N+\beta_N J_N^-$, $J_N^-=\sum_{n\in\Sigma_N}\log(n)V_n^{(N)}R_N$:
einseitiger Shift wird durch Wahl von $\beta_N$ nicht selbstadjungiert. [NEU-119.2: ?[O]]

**Konditionale Architektur.**
$$A_N^{\rm Jac,-} \stackrel{?[O]}{\longrightarrow} m_{\Omega,N} \stackrel{?[O]}{\longrightarrow} \widetilde m_N \stackrel{?[O]}{\longrightarrow} m_{\rm arith}.$$

**Satz 5.2 (Konditionale Firewall).**
$$\boxed{\widetilde m_N(z)\xrightarrow{N\to\infty}m_{\rm arith}(z)
\text{ lok. glm. in }\mathbb C^+
\;\Longrightarrow\; m_{\rm arith}\text{ Herglotz}
\;\Longrightarrow\; \text{RH.}}$$

**Offene Renormierung (Patch-Notiz §5).**

> Das Skelett hatte vague Konvergenz ohne Renormierung genannt.
> Da $\mu_{\Omega,N}(\mathbb R)=1$ (normiertes Wahrscheinlichkeitsmaß) und
> $\mu_{\rm arith}$ unendliche Gesamtmasse hat, ist eine explizite
> Renormierungsfolge $c_N\to\infty$ erforderlich:
> $$\widetilde\mu_N := c_N\,\mu_{\Omega,N},\qquad \widetilde m_N := c_N\,m_{\Omega,N}.$$
> Erst dann ist vague Konvergenz $\widetilde\mu_N\to\mu_{\rm arith}$ auf $C_c(\mathbb R)$ denkbar.
> Die Wahl von $c_N$ und der Nachweis der Konvergenz sind **offen**.

Voraussetzungen der Firewall (alle offen):
1. $A_N^{\rm Jac,-}$ selbstadjungiert [NEU-119: ?[O]]
2. Renormierungsfolge $c_N$ Herglotz-erhaltend (positiv-reell)
3. Kanonische Wahl von $\Omega_N$ [NEU-119: ?[O]]
4. Vague Konvergenz $\widetilde\mu_N\to\mu_{\rm arith}$ [NEU-120.2: ?[O]]

---

## §6 — Statusmatrix

| Aussage | Status | Quelle |
|---------|--------|--------|
| Determinantenweg als direkte Realisierung von $Q_N$ | NO-GO | NEU-091 |
| Quadratischer Pivot $Q_N$ (Mangoldt-Objekt) | PROVED | NEU-091 |
| Testkegel-Positivität $Q_N[\phi]\geq 0$ auf $\mathcal C$ | PROVED | NEU-092 |
| Bilinearer Lift $B_N(f,g)$ positiv-semidefinit auf $\mathcal S$ | OPEN | NEU-092 |
| Bochner-Lift $\rho_N/\Psi_N$, Skalendekomposition ($T/M_N$-Regime) | PROVED | NEU-093–100 |
| Hardy–Littlewood Hauptterm | CONDITIONAL (Siebheuristik) | NEU-098 |
| $V(M,H)\sim H\log(M/H)$ (GM-Normierung, korrigiert) | PROVED | NEU-101 |
| $\mathcal P^{\rm unf}_{N,H}$ lokales Formfaktor-Ersatzobjekt | PROVED$_{\rm part}$ | NEU-104 |
| LFF $\Rightarrow$ Rampenasymptotik (einseitig) | PROVED$_{\rm part}$ | NEU-107 |
| LFF $\Leftrightarrow$ Rampenform (Biimplikation) | NO-GO (nur $\Rightarrow$) | NEU-107 |
| LFF allein identifiziert $Q_{\rm Weil}$ nicht | PROVED (Typisierungswarnung) | NEU-108 |
| Symboltest $\sigma_{\rm loc}(Q_{\rm Weil})\stackrel?=|\alpha|$ | OPEN | NEU-110 |
| $m_{\rm arith}$ Herglotz $\Leftrightarrow$ RH | PROVED | NEU-111 |
| $\mu_{\rm arith}=\sum m_\gamma\delta_\gamma$ (reines Nullstellenmaß) | PROVED | NEU-112/118 |
| $m_{\rm arith}$: Herglotz-Nevanlinna-Form (symmetrische Konvergenz) | PROVED (Typisierung) | NEU-111/118 |
| $W_\xi^{\rm norm}=W_{\rm zeros}$ (keine Doppelzählung) | PROVED | NEU-113/115 |
| Kanonische Positivierungsbrücke $Q_{\rm zeros}[\phi]=\sum m_\gamma|\widehat\phi|^2$ | PROVED | NEU-112/113 |
| Einzigkeit der Positivierungsbrücke | NOT PROVED | — |
| $m_{\rm arith}=\Pi_\gamma(X)$ | OPEN | NEU-114 |
| $A_N^{\rm Jac,-}$ selbstadjungiert | OPEN | NEU-119 |
| Renormierungsfolge $c_N$, vague Konvergenz $\widetilde\mu_N\to\mu_{\rm arith}$ | OPEN | NEU-120 |
| Konditionale Firewall $\widetilde m_N\to m_{\rm arith}\Rightarrow$ RH | CONDITIONAL | NEU-120 |
| Wahrscheinlichkeitsmaß-Normierung $\mu_{\Omega,N}(\mathbb R)=1$ ohne $c_N$ | NO-GO (Massendiskrepanz) | NEU-120 |
| Pole $\pm i/2$ in $m_{\rm arith}$ | NO-GO | NEU-120 |

---

## Referenzen

- **P02** — Kanonische Weil-Form-Definitionen ($J_{1/2}$, $R_{\rm PW}$, $g_{a,b}$, $h_{a,b}$, $B_W$)
- Bombieri, E.: *Remarks on Weil's quadratic functional in the theory of prime numbers* (2000)
- Connes, A.: *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* (1999)
- Goldston, D.A., Montgomery, H.L.: *Pair correlation of zeros and primes in short intervals* (1987)
- Akhiezer, N.I.: *The Classical Moment Problem* (1965)
- Simon, B.: *Szegő's Theorem and Its Descendants* (2011)
- Hardy, G.H., Littlewood, J.E.: *Some problems of Partitio Numerorum III* (1923)

---

*Detaillierte Fehlerhistorie, Patch-Notizen, Provenienz: PASS-A-PROTOKOLL.md + `03-weil-form-statistik/NEU-091–120`.*
*Nächster Schritt: P07.tex (LaTeX-SYN) nach Freigabe dieses Stands.*
