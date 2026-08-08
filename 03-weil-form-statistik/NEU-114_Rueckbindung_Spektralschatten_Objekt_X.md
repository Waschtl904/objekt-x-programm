# NEU-114 — Rückbindung: Spektralschatten und Objekt X

**Stand:** 1. Juli 2026 | **Patch:** 8. August 2026 (Pass-A Gruppe E, E-2/6)
**Prüfart:** TARGETED-REAUDIT
**Vorgänger:** NEU-113 (Patch E-1/6)
**Nächste Nummer:** NEU-115

---

## Ausgangspunkt

NEU-113 etabliert $W_\xi^{\rm norm}$ und den Autokorrelationslift. NEU-114 fragt: Gibt es ein Objekt $X$, dessen Spektralschatten $\Pi_\gamma(X)$ genau $m_{\rm arith}$ ergibt?

**Schutzsatz:** $m_{\rm arith}$ ist nicht dasselbe wie $X$ selbst — eine Typisierungswarnung, keine Identifikation.

---

## Satz NEU-114.1 — Typisierungswarnung: $m_{\rm arith} \neq X$ ✓[M]

$$\boxed{m_{\rm arith} \neq X \text{ als Objekte.}}$$

$m_{\rm arith}(z)$ ist eine skalare Herglotz-Funktion (unter RH). $X$ ist ein hypothetischer Operator/Spektralobjekt. Selbst wenn $X$ existiert, ist $m_{\rm arith}$ nur ein skalarer Schatten davon.

**Status: ✓[M]** (Typisierungswarnung)

---

## ~~Satz NEU-114.2 (ursprünglich)~~ — $m_{\rm arith}=\Pi_\gamma(X)$ als ✓[M] — **KORRIGIERT**

> **Patch-Notiz (Pass-A, 8. Aug. 2026):** Der aktuelle Text bucht
> $m_{\rm arith}=\Pi_\gamma(X)$ als ✓[M],
> obwohl die Datei selbst sagt, dies gelte nur, falls die Rückbindung gelingt.
> Die Tests 114.3–114.5 stehen weiterhin offen.
> Eine bedingte Aussage als unbedingte zu buchen ist ein Statusfehler.

## Satz NEU-114.2 (korrigiert) — Spektralschatten-Kandidat

$$\boxed{m_{\rm arith} = \Pi_\gamma(X) \quad ?[O].}$$

Falls eine Spektralprojektion $\Pi_\gamma$ von $X$ konstruiert wird und korrekt zurückbindet, ist $m_{\rm arith}$ ein Kandidat für deren Spektralschatten — nicht $X$ selbst. Der Rückbindungstest ist offen.

**Status: ?[O]** (konditional; Rückbindung unbewiesen)

---

## Tests NEU-114.3–5 — Rückbindungstests

**Test A:** Nullstellen-Spektrum: $\sigma(\Pi_\gamma(X)) \stackrel{?}{=} \Gamma$ ?[O]

**Test B:** Herglotz-Charakter: $\Pi_\gamma(X)$ erzeugt Herglotz-Funktion $\Leftrightarrow$ Selbstadjungiertheit von $X$ auf kritischer Linie ?[O]

**Test C:** Rückbindungsgleichung: $\langle\Omega,(\Pi_\gamma(X)-z)^{-1}\Omega\rangle \stackrel{?}{=} m_{\rm arith}(z)$ ?[O]

**Status: ?[O]** (alle drei Tests offen)

---

## Status-Übersicht

| Punkt | Inhalt | Status |
|-------|--------|--------|
| 114.1 | $m_{\rm arith}\neq X$ Typisierungswarnung | ✓[M] |
| 114.2 | $m_{\rm arith}=\Pi_\gamma(X)$ | ?[O] |
| 114.3–5 | Rückbindungstests A/B/C | ?[O] |

---

## Verweise

- NEU-113 (Patch E-1/6): $W_\xi^{\rm norm}$, Autokorrelationslift
- NEU-111 (Patch D-1/6): $m_{\rm arith}$ Herglotz $\Leftrightarrow$ RH
- **Connes:** *Trace formula* (1999) — Ad-Class-Space als Kandidat für $X$
