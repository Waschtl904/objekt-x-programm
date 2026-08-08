# NEU-108 — Rampenform versus Weil-Quadratform

**Stand:** 1. Juli 2026 | **Patch:** 8. August 2026 (Pass-A Gruppe C, Patch 4/5)
**Vorgänger:** NEU-107 (\(\mathrm{LFF}_{N,H}(A)\); Rampen-Äquivalenz korrigiert; Stärke-Hierarchie als Typaussage)
**Nächste Nummer:** NEU-109

---

## Ausgangspunkt

NEU-107 zeigt (nach Patch): LFF \(\Rightarrow\) Rampe, aber nicht umgekehrt. NEU-108 klärt, ob aus LFF eine Weil-Quadratform folgt oder konstruiert werden kann.

---

## Satz NEU-108.1 — Lineares Funktional, keine Quadratform

$$\Phi \mapsto c\int \Phi(\alpha)|\alpha|\,d\alpha$$

ist ein **lineares Funktional** in \(\Phi\), keine Quadratform. Positivität gilt nur auf dem positiven Testkegel (\(\Phi \geq 0\)).

**Status: ✓[M]**

---

## Definition NEU-108.2 — Quadratische Rampenform

$$Q_{\mathrm{ramp}}[g] := c\int_{\mathbb{R}} |\alpha|\,|g(\alpha)|^2\,d\alpha.$$

Positiv (\(Q_{\mathrm{ramp}}[g] \geq 0\)); gewichtete \(L^2\)-Halbnorm mit Gewicht \(|\alpha|\).

**Status: ✓[M]** (Definition)

---

## Satz NEU-108.3 — \(Q_{\mathrm{ramp}}\) universell, nicht zeta-spezifisch

$$
\boxed{Q_{\mathrm{ramp}}[g] = c\int|\alpha||g(\alpha)|^2\,d\alpha \text{ ist immer nicht-negativ, unabhängig von }\zeta.}
$$

Die Nicht-Negativität folgt aus dem Multiplikator \(|\alpha| \geq 0\) allein, ohne Information über Zeta-Nullstellen.

**Status: ✓[M]**

---

## Satz NEU-108.4 — LFF allein identifiziert \(Q_{\mathrm{Weil}}\) nicht

> **Patch-Notiz (Pass-A, 8. Aug. 2026):** Die ursprüngliche Fassung formulierte einen harten logischen No-Go
> \(\mathrm{LFF} \not\Rightarrow Q_{\mathrm{Weil}}\).
> Eine mathematische Nichtimplikation \(A \not\Rightarrow B\) erfordert
> einen Gegenbeweis oder ein Gegenmodell; die bloße Tatsache, dass LFF weniger
> offensichtliche Information enthält, reicht nicht aus.
> Der harte No-Go wird daher zurückgezogen.

$$
\boxed{\text{LFF allein konstruiert bzw.\ identifiziert }Q_{\mathrm{Weil}}\text{ nicht.}}
$$

Das ist eine **Typisierungswarnung**: LFF beschreibt ein lokales/universelles Verhalten; \(Q_{\mathrm{Weil}}\) kodiert globale arithmetische Positivität über die Spurformel. Ob LFF unter Zusatzbedingungen \(Q_{\mathrm{Weil}}\) impliziert oder nicht, ist mathematisch offen.

**Status: ✓[M]_part** (Typisierungswarnung gültig; harter logischer No-Go zurückgezogen)

---

## Satz NEU-108.5 — Fehlende Terme zur Weil-Rekonstruktion

Für eine vollständige Weil-Identifikation wären zusätzlich nötig:

$$
Q_{\mathrm{ramp}}
\;+\;
\underbrace{\text{archimedische Terme}}_{\text{reeller/komplexer Platz}}
\;+\;
\underbrace{\text{Prim-/Singulärserie-Renormalisierung}}_{\text{lokale Faktoren}}
\;+\;
\underbrace{\text{globale Paarstruktur}}_{\text{volle Paarabstandsdichte}}
\;\stackrel{?}{=}\;
Q_{\mathrm{Weil}}.
$$

Ob diese Terme ausreichen und konsistent kombiniert werden können, ist nicht bewiesen.

**Status: ?[O]**

---

## Tabellarische Statusklassifikation (korrigiert)

| Satz | Inhalt | Status |
|------|--------|--------|
| 108.1 | \(\int\Phi|\alpha|\) lineares Funktional | ✓[M] |
| 108.2 | \(Q_{\mathrm{ramp}}[g] = c\int|\alpha||g|^2\) | ✓[M] |
| 108.3 | \(Q_{\mathrm{ramp}}\) universell, nicht zeta-spezifisch | ✓[M] |
| 108.4 | LFF identifiziert \(Q_{\mathrm{Weil}}\) nicht allein — Typisierungswarnung | ✓[M]_part |
| 108.5 | Fehlende Terme; Rekonstruktionsfrage offen | ?[O] |

---

## Verweise

- NEU-107 (Patch 3/5): LFF (korrigiert); Rampenform
- NEU-106: Epistemisch RH \(\not\Rightarrow\) GUE
- **Bombieri:** *Remarks on Weil's quadratic functional in number theory* (2000)
- **Connes:** *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* (1999)
- Goldston & Montgomery: *Pair correlation* (1987)
- Montgomery: *Pair correlation of zeros* (1973)
