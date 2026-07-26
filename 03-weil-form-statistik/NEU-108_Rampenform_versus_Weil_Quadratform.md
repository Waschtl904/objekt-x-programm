# NEU-108 — Rampenform versus Weil-Quadratform

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-107 (\(\mathrm{LFF}_{N,H}(A)\); Rampen-Äquivalenz; Stärke-Hierarchie)  
**Nächste Nummer:** NEU-109

---

## Ausgangspunkt

NEU-107 zeigt: \(\mathrm{LFF}_{N,H}(A) \Leftrightarrow R_{N,H,A}(\varepsilon) \sim \varepsilon^2/A^2\). NEU-108 klärt, ob daraus bereits eine Weil-Quadratform folgt.

**Schutzsatz vorweg:** Das entfaltete Leistungsspektrum liefert höchstens einen lokalen universellen Rampenanteil. Die Weil-Quadratform ist ein arithmetisches Objekt; ihre Positivität ist RH-relevant.

---

## Satz NEU-108.1 — Linearer Funktional, keine Quadratform

Der Ausdruck

$$
\Phi \mapsto c\int \Phi(\alpha)|\alpha|\,d\alpha
$$

ist ein **lineares Funktional** in \(\Phi\), keine Quadratform. Er ist positiv nur auf dem positiven Testkegel:

$$
\Phi \geq 0 \;\Rightarrow\; c\int\Phi(\alpha)|\alpha|\,d\alpha \geq 0.
$$

Für allgemeines \(\Phi \in C_c(\mathbb{R})\) gibt es kein Positivitätsargument.

**Status: \(\checkmark[M]\)**

---

## Definition NEU-108.2 — Quadratische Rampenform

Eine echte positive Quadratform entsteht durch:

$$
Q_{\mathrm{ramp}}[g] := c\int_{\mathbb{R}} |\alpha|\,|g(\alpha)|^2\,d\alpha.
$$

Diese Form ist positiv (\(Q_{\mathrm{ramp}}[g] \geq 0\) für alle \(g\)) und entspricht einer gewichteten \(L^2\)-Norm mit Gewicht \(|\alpha|\).

**Status: \(\checkmark[M]\)** (Definition)

---

## Satz NEU-108.3 — \(Q_{\mathrm{ramp}}\) ist universell, nicht zeta-spezifisch

$$
\boxed{Q_{\mathrm{ramp}}[g] = c\int|\alpha||g(\alpha)|^2\,d\alpha \text{ ist immer positiv, unabhängig von }\zeta.}
$$

Begründung: Die Positivität folgt aus dem positiven Multiplikator \(|\alpha|\). Sie enthält keine Information über die Lage der Zeta-Nullstellen. Daher ist \(Q_{\mathrm{ramp}}\) kein RH-relevantes Positivitätsobjekt.

Die Weil-Quadratform dagegen:
- ist an die arithmetische explizite Formel gebunden
- ist positiv semidefinit genau dann, wenn RH gilt (Bombieri-Formulierung)
- trägt globale Paar- und archimedische Struktur

**Status: \(\checkmark[M]\)**

---

## Satz NEU-108.4 — No-Go: \(\mathrm{LFF} \not\Rightarrow Q_{\mathrm{Weil}}\)

$$
\boxed{\mathrm{LFF}_{N,H}(A) \;\not\Rightarrow\; Q_{\mathrm{Weil}}.}
$$

Korrekt ist nur:

$$
\mathrm{LFF}_{N,H}(A) \;\Rightarrow\; Q_{\mathrm{ramp}} \quad\text{(lokal, universell).}
$$

\(\mathrm{LFF}\) ist **notwendig** als Montgomery-kompatibles Signal, aber **nicht hinreichend** für die volle Weil-Quadratform.

**Status: \(\checkmark/\warning[M]\)** (No-Go)

---

## Satz NEU-108.5 — Fehlende Terme zur Weil-Rekonstruktion

Für eine Weil-Identifikation benötigt man zusätzlich:

$$
Q_{\mathrm{ramp}}
\;+\;
\underbrace{\text{archimedische Terme}}_{\text{reeller/komplexer Platz}}
\;+\;
\underbrace{\text{Prim-/Singulärserien-Renormalisierung}}_{\text{lokale Faktoren}}
\;+\;
\underbrace{\text{globale Paarstruktur}}_{\text{volle Paarabstandsdichte}}
\;\stackrel{?}{=}\;
Q_{\mathrm{Weil}}.
$$

Diese Rekonstruktion ist die Leitfrage für NEU-109.

**Status: \(?[O]\)** (offene Rekonstruktionsfrage)

---

## Tabellarische Statusklassifikation

| Satz | Inhalt | Status |
|------|--------|--------|
| 108.1 | \(\int\Phi|\alpha|\) nur lineares Funktional | \(\checkmark[M]\) |
| 108.2 | \(Q_{\mathrm{ramp}}[g] = c\int|\alpha||g|^2\) | \(\checkmark[M]\) (Def.) |
| 108.3 | \(Q_{\mathrm{ramp}}\) universell, nicht zeta-spezifisch | \(\checkmark[M]\) |
| 108.4 | No-Go: \(\mathrm{LFF} \not\Rightarrow Q_{\mathrm{Weil}}\) | \(\checkmark/\warning[M]\) |
| 108.5 | Fehlende Terme: archimedisch + Renorm + global | \(?[O]\) |

---

## Neue Leitfrage für NEU-109

$$
\boxed{\text{Welche Zusatzterme fehlen, um aus }Q_{\mathrm{ramp}}\text{ die volle }Q_{\mathrm{Weil}}\text{ zu rekonstruieren?}}
$$

Konkrete Schritte:
1. **Archimedische Terme:** Beitrag des reellen/komplexen Platzes in der Weil-Formel (\(\Gamma\)-Faktoren, Residuum von \(\xi'/\xi\))
2. **Primterm-Renormierung:** Lokale Faktoren \(\log p\) vs.\ \(\log|\alpha|\)-Struktur
3. **Globale Paarstruktur:** Vollständige Paarabstandsdichte vs.\ lokales Rampenprofil
4. **Connes\u2013Consani:** Weil-Positivität als Trace-Formel-Phänomen; Verbindung zu \(\mathcal{H}_N\)

---

## Verweise

- NEU-107: \(\mathrm{LFF}_{N,H}(A)\); Rampen-Äquivalenz
- NEU-106: Epistemisch RH \(\not\Rightarrow\) GUE
- **Bombieri:** *Remarks on Weil's quadratic functional* (2000)
- **Connes:** *Trace formula in noncommutative geometry* (1999)
- Connes & Consani: *On the notion of geometry over \(\mathbb{F}_1\)* (2010)
- Goldston & Montgomery: *Pair correlation* (1987)
- Montgomery: *Pair correlation of zeros* (1973)
