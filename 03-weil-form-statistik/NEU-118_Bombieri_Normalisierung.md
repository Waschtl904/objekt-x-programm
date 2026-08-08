# NEU-118 — Bombieri-Normalisierung: Herglotz-Funktion und Spektralmaß

**Stand:** 1. Juli 2026 | **Patch:** 8. August 2026 (Pass-A Gruppe E, E-4/6)
**Prüfart:** TARGETED-REAUDIT + teilweise SUPERSEDED durch NEU-119/P02
**Vorgänger:** NEU-117 (Rigidität R1)
**Nächste Nummer:** NEU-119

> **Patch-Übersicht:** Verwechslung $\mu_{\rm arith}$ (Maß) $\leftrightarrow$ $m_{\rm arith}(z)$ (Funktion) und falsche Gamma-/Pol-Spektralanteile korrigiert.

---

## Def. NEU-118.1 (korrigiert) — Zwei getrennte Objekte

Es gibt **zwei verschiedene** Objekte:

**Das Herglotz-Spektralmaß** (ein Radon-Maß auf $\mathbb{R}$):
$$\boxed{\mu_{\rm arith} = \sum_{\gamma\in\Gamma}m_\gamma\,\delta_\gamma.}$$
Unter RH: rein atomares Maß auf $\Gamma$. **Keine** Gamma-/Pol-/Primbeiträge.

**Die Herglotz-Funktion** (holomorph auf $\mathbb{C}^+$):
$$\boxed{m_{\rm arith}(z) = \int_{\mathbb{R}}\frac{d\mu_{\rm arith}(t)}{t-z} = \sum_{\gamma\in\Gamma}\frac{m_\gamma}{\gamma-z}.}$$

> **Patch-Notiz 118.1:** Ursprünglicher Text wechselt zwischen „$m_{\rm arith}$ ist ein Radon-Maß" und „$m_{\rm arith}(z)$ ist eine Herglotz-Funktion" — das sind zwei verschiedene Objekte; der Wechsel ist ein Typfehler.

**Status: ✓[M]**

---

## ~~Behauptung NEU-118.2~~ — Gamma-/Pol-Spektralanteile in $m_{\rm arith}$ — **×[M] SUPERSEDED**

> **Patch-Notiz 118.2:** Gamma-/Pol-/Primbeiträge gehören zur arithmetischen Zerlegung von
> $W_\xi^{\rm norm}$, nicht als zusätzliche Spektralmassen in $\mu_{\rm arith}$.
> Unter RH ist $\mu_{\rm arith}$ ein reines Nullstellenmaß.

**Status: ×[M] SUPERSEDED** (vgl. NEU-112 Patch D-2/6, NEU-119 Patch E-5/6, P02)

---

## Satz NEU-118.3 — Herglotz $\Leftrightarrow$ RH ✓[M]

$$\boxed{m_{\rm arith}\text{ ist Herglotz}\quad\Longleftrightarrow\quad\text{RH.}}$$

- Unter RH: alle Pole von $m_{\rm arith}$ auf $\mathbb{R}$ $\Rightarrow$ Herglotz ✓
- Ohne RH: Off-line-Nullstellen erzeugen Pole in $\mathbb{C}^+$ $\Rightarrow$ Herglotz zerstört

**Status: ✓[M]** (vgl. NEU-111.1, Patch D-1/6)

---

## Status-Übersicht

| Punkt | Inhalt | Status |
|-------|--------|--------|
| 118.1 | $\mu_{\rm arith}$ (Maß) vs $m_{\rm arith}(z)$ (Funktion) | ✓[M] |
| 118.2 | Gamma-/Pol-Anteile in $m_{\rm arith}$ | ×[M] SUPERSEDED |
| 118.3 | Herglotz $\Leftrightarrow$ RH | ✓[M] |

---

## Verweise

- NEU-119 (Patch E-5/6): Spektralmaß-Definition; Selbstadjungiertheit konditional
- NEU-111 (Patch D-1/6): $m_{\rm arith}$ Herglotz $\Leftrightarrow$ RH
- NEU-112 (Patch D-2/6): $\mu_{\rm arith}=\sum m_\gamma\delta_\gamma$
- **Bombieri:** *Remarks on Weil's quadratic functional* (2000)
- **Connes:** *Trace formula* (1999)
