# P07 — Weil-Form Statistics:
Correlation Channels, Form-Factor Limits and Herglotz Interfaces

**Status:** Skelett (8. August 2026) — mathematischer Endstand aus Pass-A NEU-091–120
**Basis:** PASS-A-PROTOKOLL.md (Abschlusscommit `baa3975b`)
**Nicht:** Chronologie der 30 Forschungsknoten — nur der heute gültige mathematische Stand.

---

## Abstract

Wir organisieren die quadratische Weilform-Statistik in fünf konzeptionellen Schichten:
den quadratischen Pivot (Positivität, Testkegel),
die Korrelationsstruktur (Bochner-Lift, Skalenanalyse),
den Formfaktor-/Rampenkanal (GM-Normierung, LFF, offener Symboltest),
das Herglotz-Interface (lineare Distribution $\leftrightarrow$ quadratische Form),
und die konditionale Jacobi-Realisierungsarchitektur.
Fehler aus der historischen Entwicklung (Doppelzählungen, Wahrscheinlichkeitsmaß-Annahmen,
falsche Gamma-Pol-Anteile) sind im Pass-A-Prozess identifiziert und korrigiert;
P07 enthält nur das Resultat, nicht die Geschichte.

---

## §1 — Quadratischer Pivot und Positivitätsrahmen

*Basis: NEU-091, NEU-092*

**Satz 1.1 (Quadratischer Pivot).** Der Determinantenweg liefert
$$Q_N[\phi] = \det(I + K_N[\phi]) - 1$$
als wohldefinierte quadratische Form auf dem Testkegel $\mathcal C$. [NEU-091: ✓[M]\(_\rm neg\)]

**Satz 1.2 (Testkegel-Lift).** Die Bilinearform $B_N(\phi,\psi)$ ist auf $\mathcal C$ positiv-semidefinit;
der Lift auf den vollen Schwartzraum erfordert zusätzliche Bedingungen. [NEU-092: ✓[M]]

**Offen:** Vollständige Charakterisierung des maximalen Positivitätsbereichs jenseits von $\mathcal C$.

---

## §2 — Korrelationsstruktur und Skalenanalyse

*Basis: NEU-093–100*

**Satz 2.1 (Bochner-Lift).** Die Mangoldt-Autokorrelation
$$r_N(h) = \sum_{n\leq N}\Lambda(n)\Lambda(n+h)$$
ist ein positiv-definiter Kern. Der Bochner-Lift auf den Fourier-Spektralraum ist wohltypisiert. [NEU-093/094: ✓[M]]

**Satz 2.2 (Skalendekomposition).** Die Autokorrelation zerlegt sich in drei Skalen-Regime:
- $h\ll N$: Singulärserien-dominierter Hauptterm
- $h\sim N$: Selbstduale Übergangszone
- $h\gg N$: Restdichte $\Delta_N$, Übergang zum Shift-Spektrum

[NEU-095–100: ✓[M]]

**Konditional:** Hardy–Littlewood-Hauptterm unter Siebheuristik. [NEU-098: ✓[M]\(_\rm neg\) für No-Go; Hauptterm konditional]

---

## §3 — Formfaktor-/Rampenkanal: Kalibrierung, Grenzen, offener Symboltest

*Basis: NEU-101–110*

**Def. 3.1 (GM-Normierung).** Die korrekte Goldston-Montgomery-Normierung ist
$$S_{N,H}^{\rm corr} \sim H\log(M/H) \qquad (H\leq M\leq N),$$
nicht $H\log N$. [NEU-101: ✓[M] nach Patch]

**Satz 3.2 (Lokaler Formfaktor).** Der lokale Formfaktor $F_{\rm loc}(\xi)$ ist wohldefiniert
als Größe mit lokalem $H$-Parameter; eine globale Normierung ist nicht zulässig. [NEU-107: ✓[M] nach Patch]

**Satz 3.3 (Rampenasymptotik, einseitig).** Aus LFF $= 1$ folgt universelle Rampenmassenasymptotik;
die Umkehrung ist nicht bewiesen. [NEU-107: ✓[M]\(_\rm part\)]

**Satz 3.4 (Rampenform vs. Weil-Quadratform).** Die Rampenform ist eine Typisierungswarnung,
kein Selbstadjungiertheitsbeweis. [NEU-108: ✓[M]\(_\rm part\) nach Patch]

**Offen (Symboltest).**
$$\sigma_{\rm loc}(Q_{\rm Weil}) \stackrel{?}{=} |\alpha|. \qquad ?[O]$$
Weder Ausgang A ($\sigma_{\rm loc}=|\alpha|$) noch Ausgang B ($\sigma_{\rm loc}\neq|\alpha|$) ist bewiesen. [NEU-110: nach Patch]

---

## §4 — Linearer Herglotz-Kanal versus quadratische Weil-Geometrie

*Basis: NEU-111–115; kanonische Ebene: P02*

**Def. 4.1 (Herglotz-Funktion).** Unter RH:
$$m_{\rm arith}(z) = -\frac{\Xi'(z)}{\Xi(z)}
= \sum_{\gamma\in\Gamma}\frac{m_\gamma}{\gamma-z}
= \int_{\mathbb R}\frac{d\mu_{\rm arith}(t)}{t-z},$$
wobei $\mu_{\rm arith}=\sum_{\gamma\in\Gamma}m_\gamma\delta_\gamma$ das **reine Nullstellenmaß** ist.
Keine Gamma-/Pol-/Primbeiträge in $\mu_{\rm arith}$. [NEU-111, NEU-112, NEU-118: ✓[M] nach Patches]

**Satz 4.2 (Herglotz $\Leftrightarrow$ RH).**
$$m_{\rm arith}\text{ ist Herglotz} \quad\Longleftrightarrow\quad \text{RH.}$$
[NEU-111.1: ✓[M]]

**Def. 4.3 (Normierte Weil-Distribution).**
$$W_\xi^{\rm norm} = W_{\rm zeros} = W_{\rm pole/triv}+W_\Gamma+W_{\rm prime}.$$
Die Nullstellenseite und die arithmetische Seite sind äquivalente Darstellungen— nicht zu addieren. [NEU-113, NEU-115: ✓[M] nach Patches]

**Satz 4.4 (Autokorrelationslift — Brücke linear/quadratisch).**
$$\Phi=\phi^**\phi\quad\Longrightarrow\quad
W_\xi^{\rm norm}[\Phi] = Q_{\rm zeros}[\phi] = \sum_{\gamma\in\Gamma}m_\gamma|\widehat\phi(\gamma)|^2.$$
Dies ist die **einzige** korrekte Brücke. [NEU-112, NEU-113, NEU-115: ✓[M]; kanonisiert in P02]

**Satz 4.5 (Interface-Schutzsatz).**
$$m_{\rm arith}\rightsquigarrow W_\xi^{\rm norm}
\quad\text{und getrennt}\quad
a\to g_{a,b}\to h_{a,b}\to B_W(a,b).$$
Ohne Autokorrelationspaarung kein direkter Vergleich. P02 liefert die kanonische Definitionsebene.

**Offen.** $m_{\rm arith}=\Pi_\gamma(X)$: ?[O] — Rückbindungstests A/B/C offen. [NEU-114]

---

## §5 — Jacobi-/Herglotz-Realisierung: konditionale Architektur

*Basis: NEU-118–120*

**Def. 5.1 (Spektralmaß, konditional).** Falls $A_N^{\rm Jac,-}$ selbstadjungiert:
$$m_{\Omega,N}(z) = \langle\Omega_N,(A_N^{\rm Jac,-}-z)^{-1}\Omega_N\rangle
= \int_{\mathbb R}\frac{d\mu_{\Omega,N}(\lambda)}{\lambda-z}.$$
[NEU-119.1: ✓[M] konditional]

**Offen (Selbstadjungiertheit).** Der konkrete Jacobi-Kandidat
$$A_N^{\rm Jac,-} = H_N+\beta_N J_N^-, \quad
J_N^-=\sum_{n\in\Sigma_N}\log(n)V_n^{(N)}R_N$$
is not proved to be self-adjoint. Ein einseitiger Shift wird durch Wahl von $\beta_N$ nicht selbstadjungiert.
[NEU-119.2: ?[O]]

**Konditionale Architektur.**
$$A_N^{\rm Jac,-} \stackrel{?[O]}{\longrightarrow} m_{\Omega,N} \stackrel{?[O]}{\longrightarrow} m_{\rm arith}.$$

**Satz 5.2 (Konditionale Firewall).**
$$\boxed{m_{\Omega,N}(z)\xrightarrow{N\to\infty}m_{\rm arith}(z)
\text{ lok. glm. in }\mathbb C^+
\;\Longrightarrow\; m_{\rm arith}\text{ Herglotz}
\;\Longrightarrow\; \text{RH.}}$$
Voraussetzungen: Selbstadjungiertheit, Herglotz-erhaltende Renormierung, kanonische $\Omega_N$-Wahl.
[NEU-120.1: ?[O] konditionale Firewall]

**Bemerkung (korrekter Konvergenzrahmen).** Da $\mu_{\rm arith}$ unendliche Gesamtmasse hat,
ist der korrekte Rahmen vague Konvergenz:
$$\int\phi\,d\mu_{\Omega,N}\to\int\phi\,d\mu_{\rm arith}\quad(\phi\in C_c(\mathbb R)).$$
Wahrscheinlichkeitsmaß-Normierungen scheitern prinzipiell. [NEU-120.2: ?[O] Rahmen]

---

## §6 — Statusmatrix: was überlebt und was nicht

| Aussage | Status | Quelle |
|---------|--------|--------|
| Quadratischer Pivot $Q_N$, Testkegel | PROVED | NEU-091/092 |
| Bochner-Lift, Skalendekomposition | PROVED | NEU-093–100 |
| Hardy–Littlewood Hauptterm | CONDITIONAL (Siebheuristik) | NEU-098 |
| GM-Normierung $H\log(M/H)$ | PROVED (korrigiert) | NEU-101 |
| Lokaler Formfaktor, Rampenasymptotik (einseitig) | PROVED | NEU-107 |
| LFF $\Leftrightarrow$ Rampenform (Biimplikation) | NO-GO (nur $\Rightarrow$) | NEU-107 |
| Symboltest $\sigma_{\rm loc}(Q_{\rm Weil})=?|\alpha|$ | OPEN | NEU-110 |
| $m_{\rm arith}$ Herglotz $\Leftrightarrow$ RH | PROVED | NEU-111 |
| $\mu_{\rm arith}=\sum m_\gamma\delta_\gamma$ (reines Nullstellenmaß) | PROVED | NEU-112/118 |
| $W_\xi^{\rm norm}=W_{\rm zeros}$ (keine Doppelzählung) | PROVED | NEU-113/115 |
| Autokorrelationslift $Q_{\rm zeros}[\phi]=\sum m_\gamma|\widehat\phi|^2$ | PROVED | NEU-112/113 |
| $m_{\rm arith}=\Pi_\gamma(X)$ | OPEN | NEU-114 |
| $A_N^{\rm Jac,-}$ selbstadjungiert | OPEN | NEU-119 |
| Grenzübergang $m_{\Omega,N}\to m_{\rm arith}$ | OPEN | NEU-119/120 |
| Konditionale Firewall $\to$ RH | CONDITIONAL | NEU-120 |
| Wahrscheinlichkeitsmaß-Normierung $\mu_{\Omega,N}(\mathbb R)=1$ | NO-GO | NEU-120 |
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

*Detaillierte Fehlerhistorie, Patch-Notizen und Provenanzdaten: PASS-A-PROTOKOLL.md + `03-weil-form-statistik/NEU-091–120`.*
