# P07 — Weil-Form Statistics:
Correlation Channels, Form-Factor Limits and Herglotz Interfaces

**Status:** Patch 2/2 (8. August 2026) — Prä-Freigabestand für SYN-Finalaudit
**Basis:** PASS-A-PROTOKOLL.md (`baa3975b`); NEU-101 Patch 2 (`7ff336e2`)
**Patch-Commits:** Skelett (`94c25130`) → Patch 1 (`596317bb`) → Patch 2 (dieser Commit)

> *Patch-Notizen gehören ins PASS-A-PROTOKOLL und die NEU-Knoten.*
> *Das SYN-Paper enthält nur bereinigte Definitionen, Sätze und Statusangaben.*

---

## Abstract

Wir organisieren die quadratische Weilform-Statistik in fünf konzeptionellen Schichten:
den quadratischen Pivot (Positivität, Testkegel),
die Korrelationsstruktur (Bochner-Lift, Skalenanalyse),
den Formfaktor-/Rampenkanal (GM-Varianz, LFF, offener Symboltest),
das Herglotz-Interface (lineare Distribution ↔ quadratische Form),
und die konditionale Jacobi-Realisierungsarchitektur.

---

## §1 — Quadratischer Pivot und Positivitätsrahmen

*Basis: NEU-091, NEU-092*

**Satz 1.1 (Determinanten-No-Go).**
$$D_N(z) \xrightarrow{N\to\infty} e^{-\gamma^2/4}$$
im festen $z$-Regime ($z$ fest, $N\to\infty$), also $z$-unabhängig.
Daraus folgt: kein direkter $\xi$-Anschluss über den Determinantenweg im festen $z$-Regime.
[NEU-091: ✓[M]$_{\rm neg}$]

**Def. 1.2 (Quadratischer Pivot).**
$$Q_N(\varphi) := \gamma^2\sum_{r,n}\Lambda(n)^2 W_N(r,n)\varphi(r,n).$$
Separat eingeführt, unabhängig vom Determinantenansatz. [NEU-091: ✓[M]]

**Satz 1.3 (Testkegel-Positivität).** $Q_N[\phi]\geq 0$ für $\phi\in\mathcal C$ (Testkegel).
[NEU-092: ✓[M]]

**Offen.** Bilinearer Lift $B_N(f,g)$ mit Kreuzterm $\Lambda(m)\Lambda(n)$ positiv-semidefinit auf $\mathcal S$: **?[O]** [NEU-092]

---

## §2 — Korrelationsstruktur und Skalenanalyse

*Basis: NEU-093–100*

**Def. 2.1 (Abstrakte PSD-Architektur).**
Sei $\rho_N=(\rho_N(a,b))_{a,b}$ eine positiv-semidefinite Matrix mit $\rho_N(a,a)=1$.
Dann ist
$$K_N(a,b) := \sqrt{\kappa_a\kappa_b}\,\rho_N(a,b)$$
positiv-semidefinit. [NEU-093: ✓[M]]

**Def. 2.2 (Logarithmischer Bochner-Kandidat).**
Die kanonische Spezialisierung durch den logarithmischen Kandidaten:
$$\rho_N((r,m),(r,n)) := \Psi_N(\log(m/n)),$$
wobei $\Psi_N$ positiv-definit im Bochner-Sinn via
$$\Psi_N(t) = \int e^{it\xi}\,d\nu_N(\xi)$$
für ein positives Maß $\nu_N$. [NEU-094: ✓[M]]

**Offen.** Kanonische Wahl von $\rho_N$ (welcher Kandidat?): ?[O]

**Satz 2.3 (Skalentriage — drei Regime).**
Mit $M_N$ (Kurzintervallparameter) und $T = M_N^\theta$:

| Regime | Verhalten | Bedeutung |
|--------|-----------|------------|
| $T = O(1)$ | Rang-eins- / Grobmittelungs-Kollaps | Zu grob für Weil-Anschluss |
| $1 \ll T \ll M_N$ | Nichttrivialer Kandidatenbereich | ?[O] für Weil-Tauglichkeit |
| $T \gg M_N$ | Diagonal-Kollaps | Zu fein; kein Weil-Anschluss |

[NEU-096: ✓[M]]

**Satz 2.4 (Singulärserien-Feinstruktur, konditional).**
Im Zwischenregime $1\ll T\ll M_N$ liefert die Feinstrukturanalyse (NEU-098–100):
- Singulärserien-Hauptterm unter Hardy–Littlewood-Siebheuristik: CONDITIONAL
- Restdichte $\Delta_N$ und Übergang zum Shift-Spektrum: ✓[M]
- Weil-Tauglichkeit des Zwischenregimes: **?[O]**

---

## §3 — Formfaktor-/Rampenkanal: Kalibrierung, Grenzen, offener Symboltest

*Basis: NEU-101–110*

**Def. 3.1 (Dyadische Kurzintervall-Varianz).**
$$\mathcal V(M,H) := \frac1M\int_M^{2M}(\psi(x+H)-\psi(x)-H)^2\,dx.$$

**Satz 3.2 (GM-Varianzasymptotik, CONDITIONAL).**
$$\text{RH + Strong Pair Correlation}\;\Longleftrightarrow\;
\mathcal V(M,H)\sim H\log(M/H)\quad(1\leq H\leq M).$$
Historischer Normierungsfehler war ein falscher Faktor $H/M$ ($\to H/M\cdot\log(M/H)$ statt $H\log(M/H)$).
[NEU-101: CONDITIONAL; GM 1987]

**Def. 3.3 (Lokales Formfaktor-Ersatzobjekt).**
$\mathcal P^{\rm unf}_{N,H}$ (unnormalisiert, lokal) ersetzt das global normierte $\mathcal S_{N,H}$ (verworfen). [NEU-104: ✓[M]$_{\rm part}$]

**Satz 3.4 (Rampenasymptotik, einseitig).** LFF $=1$ $\Rightarrow$ universelle Rampenmassenasymptotik.
Umkehrung nicht bewiesen. [NEU-107: ✓[M]$_{\rm part}$]

**Satz 3.5 (LFF-Typisierungswarnung).**
$$\text{LFF allein konstruiert oder identifiziert }Q_{\rm Weil}\text{ nicht.}$$
[NEU-108: ✓[M]$_{\rm part}$]

**Offen (Symboltest).**
$$\sigma_{\rm loc}(Q_{\rm Weil}) \stackrel{?}{=} |\alpha|. \qquad ?[O]$$
[NEU-110]

---

## §4 — Linearer Herglotz-Kanal versus quadratische Weil-Geometrie

*Basis: NEU-111–115; kanonische Ebene: P02*

**Def. 4.1 (Herglotz-Funktion — Nevanlinna-Form).**
Unter RH:
$$m_{\rm arith}(z) = A + \int_{\mathbb R}\left(\frac1{t-z}-\frac{t}{1+t^2}\right)d\mu_{\rm arith}(t),$$
wobei $\mu_{\rm arith}=\sum_{\gamma\in\Gamma}m_\gamma\delta_\gamma$ das **reine Nullstellenmaß** ist
(keine Gamma-/Pol-/Primbeiträge) und $A=\Re\,m_{\rm arith}(i)\in\mathbb R$.
Die Summe $\sum_\gamma m_\gamma/(\gamma-z)$ konvergiert im kanonisch symmetrischen Sinn.
[NEU-111, NEU-112, NEU-118: ✓[M]]

**Satz 4.2 (Herglotz $\Leftrightarrow$ RH).**
$$m_{\rm arith}\text{ ist Herglotz}\quad\Longleftrightarrow\quad\text{RH.}$$
[NEU-111.1: ✓[M]]

**Def. 4.3 (Normierte Weil-Distribution).**
$$W_\xi^{\rm norm} = W_{\rm zeros} = W_{\rm pole/triv}+W_\Gamma+W_{\rm prime}.$$
Nullstellenseite und arithmetische Seite: äquivalente Darstellungen, nicht addieren.
[NEU-113, NEU-115: ✓[M]]

**Satz 4.4 (Kanonische Positivierungsbrücke).**
$$\Phi=\phi^**\phi\quad\Longrightarrow\quad
W_\xi^{\rm norm}[\Phi] = Q_{\rm zeros}[\phi] = \sum_{\gamma\in\Gamma}m_\gamma|\widehat\phi(\gamma)|^2.$$
Dies ist die **kanonische** Positivierungsbrücke (Einzigkeit nicht bewiesen).
[NEU-112/113/115: ✓[M]; kanonisiert in P02]

**Satz 4.5 (Interface-Schutzsatz).**
$$m_{\rm arith}\rightsquigarrow W_\xi^{\rm norm}
\quad\text{und getrennt}\quad
a\to g_{a,b}\to h_{a,b}\to B_W(a,b).$$
Ohne Autokorrelationspaarung kein direkter Vergleich; P02 als kanonische Definitionsebene.

**Offen.** $m_{\rm arith}=\Pi_\gamma(X)$: ?[O] [NEU-114]

---

## §5 — Jacobi-/Herglotz-Realisierung: konditionale Architektur

*Basis: NEU-118–120*

**Def. 5.1 (Spektralmaß, konditional).** Falls $A_N^{\rm Jac,-}$ selbstadjungiert:
$$m_{\Omega,N}(z) = \langle\Omega_N,(A_N^{\rm Jac,-}-z)^{-1}\Omega_N\rangle
= \int_{\mathbb R}\frac{d\mu_{\Omega,N}(\lambda)}{\lambda-z},\quad
\mu_{\Omega,N}(\mathbb R)=1.$$
[NEU-119.1: ✓[M] konditional]

**Offen.** $A_N^{\rm Jac,-}=H_N+\beta_N J_N^-$ selbstadjungiert: ?[O] [NEU-119.2]

**Def. 5.2 (Nevanlinna-normalisierte Approximanten).**
Da $\mu_{\Omega,N}(\mathbb R)=1$ und $\mu_{\rm arith}$ unendliche Gesamtmasse hat,
ist eine Renormierungsfolge $c_N>0$ erforderlich:
$$\widetilde\mu_N := c_N\,\mu_{\Omega,N}.$$
Die zugehörigen Nevanlinna-normalisierten Approximanten:
$$\widetilde m_N^{\rm ren}(z) := a_N + \int_{\mathbb R}\left(\frac1{t-z}-\frac{t}{1+t^2}\right)d\widetilde\mu_N(t),
\quad c_N>0,\; a_N\in\mathbb R.$$
$a_N$ kann von Null verschieden sein; nur bei zusätzlicher Symmetrie reduziert sich
das auf eine blosse Skalierung $c_N m_{\Omega,N}$.

**Satz 5.3 (Konditionale Firewall).**
$$\boxed{\widetilde m_N^{\rm ren}(z)\xrightarrow{N\to\infty}m_{\rm arith}(z)
\text{ lok. glm. in }\mathbb C^+
\;\Longrightarrow\; m_{\rm arith}\text{ Herglotz}
\;\Longrightarrow\; \text{RH.}}$$

Offene Voraussetzungen:
1. $A_N^{\rm Jac,-}$ selbstadjungiert [NEU-119: ?[O]]
2. Renormierungsfolge $c_N>0$, Gewichtsfolge $a_N\in\mathbb R$ passend gewählt
3. Kontrolle der Nevanlinna-Gewichte: $\int d\widetilde\mu_N(t)/(1+t^2)$ kontrolliert
4. Vague Konvergenz $\widetilde\mu_N\to\mu_{\rm arith}$ allein impliziert **nicht** automatisch
   lokale gleichmäßige Konvergenz von $\widetilde m_N^{\rm ren}$ — Tail-Kontrolle nötig
5. Kanonische Wahl von $\Omega_N$ [NEU-119: ?[O]]

**Konditionale Architektur.**
$$A_N^{\rm Jac,-} \stackrel{?[O]}{\longrightarrow} m_{\Omega,N}
\stackrel{c_N,\,a_N}{\longrightarrow} \widetilde m_N^{\rm ren}
\stackrel{?[O]}{\longrightarrow} m_{\rm arith}.$$

---

## §6 — Statusmatrix

| Aussage | Status | Quelle |
|---------|--------|--------|
| $D_N(z)\to e^{-\gamma^2/4}$ (Determinanten-No-Go) | PROVED | NEU-091 |
| Quadratischer Pivot $Q_N$ (Mangoldt-Objekt) | PROVED (Definition) | NEU-091 |
| Testkegel-Positivität $Q_N[\phi]\geq 0$ auf $\mathcal C$ | PROVED | NEU-092 |
| Bilinearer Lift $B_N(f,g)$ pos.-semidef. auf $\mathcal S$ | OPEN | NEU-092 |
| Abstrakte PSD-Architektur $K_N$ aus $\rho_N$ | PROVED | NEU-093 |
| Logarithmischer Bochner-Kandidat $\Psi_N$ | PROVED | NEU-094 |
| Kanonische Wahl von $\rho_N$ | OPEN | NEU-093 |
| Skalentriage: $T\gg M_N$ Diagonal-Kollaps | PROVED | NEU-096 |
| Skalentriage: $T=O(1)$ Rang-eins-Kollaps | PROVED | NEU-096 |
| Zwischenregime $1\ll T\ll M_N$ Weil-tauglich | OPEN | NEU-096/097 |
| Hardy–Littlewood Singulärserien-Hauptterm | CONDITIONAL (Siebheuristik) | NEU-098 |
| $\mathcal V(M,H)\sim H\log(M/H)$ | CONDITIONAL (RH + SPC, GM 1987) | NEU-101 |
| $\mathcal P^{\rm unf}_{N,H}$ lokales Formfaktor-Ersatzobjekt | PROVED$_{\rm part}$ | NEU-104 |
| LFF $\Rightarrow$ Rampenasymptotik (einseitig) | PROVED$_{\rm part}$ | NEU-107 |
| LFF $\Leftrightarrow$ Rampenform (Biimplikation) | NO-GO (nur $\Rightarrow$) | NEU-107 |
| LFF allein identifiziert $Q_{\rm Weil}$ nicht | PROVED (Typisierungswarnung) | NEU-108 |
| Symboltest $\sigma_{\rm loc}(Q_{\rm Weil})\stackrel?=|\alpha|$ | OPEN | NEU-110 |
| $m_{\rm arith}$ Herglotz $\Leftrightarrow$ RH | PROVED | NEU-111 |
| $\mu_{\rm arith}=\sum m_\gamma\delta_\gamma$ (reines Nullstellenmaß) | PROVED | NEU-112/118 |
| $m_{\rm arith}$ in Nevanlinna-Form (symmetrische Konvergenz) | PROVED (Typisierung) | NEU-111/118 |
| $W_\xi^{\rm norm}=W_{\rm zeros}$ (keine Doppelzählung) | PROVED | NEU-113/115 |
| Kanonische Positivierungsbrücke $Q_{\rm zeros}=\sum m_\gamma|\widehat\phi|^2$ | PROVED | NEU-112/113 |
| Einzigkeit der Positivierungsbrücke | NOT PROVED | — |
| $m_{\rm arith}=\Pi_\gamma(X)$ | OPEN | NEU-114 |
| $A_N^{\rm Jac,-}$ selbstadjungiert | OPEN | NEU-119 |
| Nevanlinna-Renormierung $(c_N,a_N)$, Tail-Kontrolle | OPEN | NEU-120 |
| Vague Konvergenz $\widetilde\mu_N\to\mu_{\rm arith}$ | OPEN | NEU-120 |
| Konditionale Firewall $\widetilde m_N^{\rm ren}\to m_{\rm arith}\Rightarrow$ RH | CONDITIONAL | NEU-120 |
| $\mu_{\Omega,N}(\mathbb R)=1$ ohne $c_N$ genügt | NO-GO (Massendiskrepanz) | NEU-120 |
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

*Fehlerhistorie, Patch-Notizen, Provenienz: PASS-A-PROTOKOLL.md + `03-weil-form-statistik/NEU-091–120`.*
*Nächster Schritt nach Finalaudit: `papers/P07_Weil_Form_Statistics.tex`*
