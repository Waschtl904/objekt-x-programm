# NEU-119 — Spektralmaß: Jacobi-Operator zu Herglotz-Funktion

**Stand:** 1. Juli 2026 | **Patch:** 8. August 2026 (Pass-A Gruppe E, E-5/6)
**Prüfart:** TARGETED-REAUDIT
**Vorgänger:** NEU-118 (Patch E-4/6)
**Nächste Nummer:** NEU-120

---

## Ausgangspunkt

NEU-119 definiert das Spektralmaß $\mu_{\Omega,N}$ und die Herglotz-Funktion $m_{\Omega,N}$ über den Jacobi-Operator $A_N^{\rm Jac,-}$. Diese Definitionen sind **konditional korrekt** — sofern $A_N^{\rm Jac,-}$ tatsächlich selbstadjungiert ist. Drei Fehler werden korrigiert.

---

## Def. NEU-119.1 — Spektralmaß und Resolventfunktion (konditional) ✓[M]

Falls $A_N = A_N^{\rm Jac,-}$ selbstadjungiert:
$$\mu_{\Omega,N}(B) := \langle\Omega_N,E_{A_N}(B)\Omega_N\rangle$$
$$\boxed{m_{\Omega,N}(z) := \langle\Omega_N,(A_N-z)^{-1}\Omega_N\rangle = \int_{\mathbb{R}}\frac{d\mu_{\Omega,N}(\lambda)}{\lambda-z}.}$$
Unter dieser Bedingung: $m_{\Omega,N}$ ist Herglotz für $\Im z>0$.

**Status: ✓[M]** (konditional auf Selbstadjungiertheit)

---

## ~~Behauptung NEU-119.2~~ — Selbstadjungiertheit von $A_N^{\rm Jac,-}$ — **×[M] / ?[O]**

> **Patch-Notiz 119.2 (Pass-A, 8. Aug. 2026):** Der aktuelle Text nennt
> $A_N^{\rm Jac,-}=H_N+\beta_NJ_N^-$, $J_N^-=\sum_{n\in\Sigma_N}\log(n)V_n^{(N)}R_N$
> und behauptet Selbstadjungiertheit. Das ist **nicht bewiesen**:
> NEU-077 rekonstruiert nur den Vorwärtsoperator $\Theta_N=\sum_n\log(n)V_n^{(N)}R_N$;
> der $J_N^-$-Strang benötigt eine Adjungierten-/Antisymmetrisierung.
> Ein Skalar $\beta_N$ macht einen einseitigen Shift nicht selbstadjungiert.

$$\boxed{A_N^{\rm Jac,-}\text{ selbstadjungiert}\quad?[O].}$$

Die Definitionen in NEU-119.1 sind konditional auf diese offene Bedingung korrekt.

**Status: ?[O]** (Selbstadjungiertheit unbewiesen)

---

## ~~Behauptung NEU-119.3~~ — Eigenvektor-Zusatzbedingung — **×[M] falsch**

> **Patch-Notiz 119.3:** Aussage „$m_{\Omega,N}$ streng Herglotz positiv, sofern $\Omega_N$ kein Eigenvektor" ist unnötig und **falsch**.
> Auch für normierten Eigenvektor $\Omega_N$ zum Eigenwert $\lambda_0$:
> $$m_{\Omega,N}(z)=\frac{1}{\lambda_0-z},\quad\Im m_{\Omega,N}(z)=\frac{\Im z}{|\lambda_0-z|^2}>0\quad(\Im z>0).$$
> Der Herglotz-Charakter ist also auch in diesem Fall gegeben.

**Status: ×[M]** (Zusatzbedingung gestrichen)

---

## ~~Behauptung NEU-119-O3~~ — „$m_{\rm arith}$ nicht einfach Stieltjes wegen Gamma-Termen" — **×[M] SUPERSEDED**

> **Patch-Notiz O3:** Das ist die alte 112.1-Verwirrung (vgl. NEU-112 Patch D-2/6, NEU-118 Patch E-4/6).
> Unter RH:
> $$m_{\rm arith}(z)=\int_{\mathbb{R}}\frac{d\mu_{\rm arith}(t)}{t-z},\quad\mu_{\rm arith}=\sum_{\gamma\in\Gamma}m_\gamma\delta_\gamma$$
> ist ein reines Stieltjes-Integral — **ohne** Gamma-Zusatzterme.
> Gamma-/Pol-/Primbeiträge gehören zur arithmetischen Zerlegung von $W_\xi^{\rm norm}$,
> nicht als zusätzliche Spektralmassen in $m_{\rm arith}$.

**Status: ×[M] SUPERSEDED**

---

## Satz NEU-119.4 — Grenzübergang (konditional) ?[O]

$$\boxed{m_{\Omega,N}(z)\xrightarrow{N\to\infty}m_{\rm arith}(z)\text{ lokal gleichmäßig in }\mathbb{C}^+\quad?[O].}$$

Kanonische Wahl von $\Omega_N$ ebenfalls offen.

**Status: ?[O]**

---

## Status-Übersicht

| Punkt | Inhalt | Status |
|-------|--------|--------|
| 119.1 | Spektralmaß/Resolvent (konditional) | ✓[M] |
| 119.2 | Selbstadjungiertheit $A_N^{\rm Jac,-}$ | ?[O] |
| 119.3 | Eigenvektor-Zusatzbedingung | ×[M] |
| 119-O3 | Gamma-Terme in $m_{\rm arith}$ | ×[M] SUPERSEDED |
| 119.4 | Grenzübergang $m_{\Omega,N}\to m_{\rm arith}$ | ?[O] |

---

## Verweise

- **NEU-077:** Vorwärtsoperator $\Theta_N$ (Adjungierten-Audit)
- NEU-111 (Patch D-1/6), NEU-112 (Patch D-2/6), NEU-118 (Patch E-4/6)
- **Akhiezer:** *The Classical Moment Problem* (1965)
- **Simon:** *Szegő's Theorem and Its Descendants* (2011)
