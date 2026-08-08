# NEU-115 — Weil-Distribution Interface

**Stand:** 1. Juli 2026 | **Patch:** 8. August 2026 (Pass-A Gruppe E, E-3/6)
**Prüfart:** TARGETED-REAUDIT
**Vorgänger:** NEU-114 (Patch E-2/6)
**Nächste Nummer:** NEU-116

---

## Ausgangspunkt

NEU-115 typisiert das Interface zwischen linearer Weil-Distribution und quadratischer Weilform. Die zentrale Unterscheidung ist korrekt und wichtig. Ein alter Doppelzählungsfehler (identisch NEU-113.2) wird hier korrigiert.

---

## Satz NEU-115.1 — Lineare Distribution ≠ Quadratform ✓[M]

$$\boxed{W_\xi^{\rm norm}[\Phi]\text{ ist linear in }\Phi.}$$
$$\boxed{Q_{\rm Weil}[\phi] = B_W(\phi,\phi)\text{ ist quadratisch in }\phi.}$$

Diese Unterscheidung ist der methodische Kern des Interface. Ohne den Autokorrelationslift $\Phi=\phi^**\phi$ sind beide Objekte nicht vergleichbar.

**Status: ✓[M]**

---

## ~~Def. NEU-115.2 (ursprünglich)~~ — Vierteilige $W_\xi$-Summe — **×[M] SUPERSEDED**

> **Patch-Notiz (Pass-A, 8. Aug. 2026):** Der aktuelle Text definiert
> $W_\xi = W_{\rm zeros}+W_\Gamma+W_{\rm prime}+W_{\rm pole/triv}$,
> dieselbe vierteilige Summe, die NEU-113.7 bereits als Doppelzählung
> ($= 2W_{\rm zeros}$) identifiziert hat.

## Def. NEU-115.2 (korrigiert) — Normierte Weil-Distribution

$$\boxed{W_\xi^{\rm norm} = W_{\rm zeros} = W_{\rm pole/triv}+W_\Gamma+W_{\rm prime}.}$$

Die Nullstellenseite und die arithmetische Seite sind äquivalente Darstellungen derselben Distribution — nicht zu addieren.

**Status: ✓[M]**

---

## Satz NEU-115.3 — Autokorrelationslift als Brücke ✓[M]

$$W_\xi^{\rm norm}[\phi^**\phi] = Q_{\rm zeros}[\phi] = \sum_{\gamma\in\Gamma}m_\gamma|\widehat\phi(\gamma)|^2.$$

Dies ist die einzige korrekte Brücke zwischen linearer Distribution und Quadratform.

**Status: ✓[M]** ($\to$ P02)

---

## Satz NEU-115.4 — Interface-Schutzsatz ✓[M]

$$\boxed{W_\xi^{\rm norm}[\Phi]\text{ für allg. }\Phi\text{ nicht direkt mit }Q_{\rm Weil}[\phi]\text{ vergleichbar.}}$$

Der Vergleich erfordert: (1) gemeinsamer Testfunktionsraum, (2) Fourier-Konvention, (3) Autokorrelationspaarung.

**Status: ✓[M]** (Interface-Firewall)

---

## Status-Übersicht

| Punkt | Inhalt | Status |
|-------|--------|--------|
| 115.1 | Linear $\neq$ Quadratform | ✓[M] |
| 115.2 | $W_\xi^{\rm norm}=W_{\rm zeros}$ (keine Vierfachsumme) | ✓[M] |
| 115.3 | Autokorrelationslift als Brücke | ✓[M] |
| 115.4 | Interface-Schutzsatz | ✓[M] |

---

## Verweise

- NEU-113 (Patch E-1/6): Doppelzählungswarnung NEU-113.7
- NEU-112 (Patch D-2/6): Autokorrelationslift
- **P02** (kanonische Referenz)
- **Bombieri:** *Remarks on Weil's quadratic functional* (2000)
