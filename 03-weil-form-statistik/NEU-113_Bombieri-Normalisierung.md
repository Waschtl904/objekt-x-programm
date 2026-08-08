# NEU-113 — Bombieri-Normalisierung und linearer Weil-Lift

**Stand:** 1. Juli 2026 | **Patch:** 8. August 2026 (Pass-A Gruppe E, E-1/6)
**Prüfart:** AUDIT-RECONCILED
**Vorgänger:** NEU-112 (Patch D-2/6)
**Nächste Nummer:** NEU-114

> **Patch-Übersicht:** Zwei alte Fehler korrigiert. Großteil **SUPERSEDED BY P02**.

---

## Def. NEU-113.1 (korrigiert) — Mellin-Brücke mit Zentrierung

Für $f(x) = x^{-1/2}\phi(\log x)$ gilt:
$$\boxed{\widetilde f(1/2+iz) = \widehat\phi(z).}$$
Ohne den $x^{-1/2}$-Faktor entsteht ein Versatz. P02-Kanonisierung über $J_{1/2}$/$R_{\rm PW}$ ist verbindlich.

> **Patch-Notiz 113.1:** Ursprünglich fehlte der Zentrierungsfaktor → **×[M]** → korrigiert.

**Status: ✓[M]** (→ P02)

---

## ~~Satz NEU-113.2 (ursprünglich)~~ — Vierteilige $W_\xi$-Summe — **×[M] SUPERSEDED**

> **Patch-Notiz 113.2:** $W_\xi = W_{\rm zeros}+W_\Gamma+W_{\rm prime}+W_{\rm pole/triv}$ ergibt laut NEU-113.7 selbst $2W_{\rm zeros}$, nicht $W_\xi^{\rm norm}$. Doppelzählung.

## Satz NEU-113.2 (korrigiert) — Normierte Weil-Distribution
$$\boxed{W_\xi^{\rm norm} = W_{\rm zeros} = W_{\rm pole/triv}+W_\Gamma+W_{\rm prime}.}$$
Die Nullstellenseite und die arithmetische Seite sind äquivalente Darstellungen derselben Distribution — nicht zu addieren.

**Status: ✓[M]** (SUPERSEDED BY P02)

---

## Satz NEU-113.3 — Autokorrelationslift ✓[M]
$$Q_{\rm zeros}[\phi] := W_{\rm zeros}[\phi^**\phi] = \sum_{\gamma\in\Gamma}m_\gamma|\widehat\phi(\gamma)|^2 \geq 0.$$
Identisch mit NEU-112.2 (Patch D-2/2) und P02-Kanonisierung.

**Status: ✓[M]** (SUPERSEDED BY P02)

---

## Status-Übersicht

| Punkt | Inhalt | Status |
|-------|--------|--------|
| 113.1 | Mellin-Zentrierung mit $x^{-1/2}$ | ✓[M] → P02 |
| 113.2 | $W_\xi^{\rm norm}=W_{\rm zeros}$ (keine Vierfachsumme) | ✓[M] → P02 |
| 113.3 | Autokorrelationslift | ✓[M] → P02 |
| 113.7 | Doppelzählungswarnung (historisch) | ✓[M] |
| **Gesamt** | **Überwiegend SUPERSEDED BY P02** | — |

---

## Verweise

- **P02** (kanonische Referenz für alle obigen Resultate)
- NEU-112 (Patch D-2/2): Autokorrelationslift, normierte Weil-Distribution
- **Bombieri:** *Remarks on Weil's quadratic functional* (2000)
- **Connes:** *Trace formula* (1999)
