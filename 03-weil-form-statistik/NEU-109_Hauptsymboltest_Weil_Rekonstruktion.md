# NEU-109 — Hauptsymboltest der Weil-Rekonstruktion

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-108 (\(Q_{\mathrm{ramp}}\) universell; No-Go \(\mathrm{LFF}\not\Rightarrow Q_{\mathrm{Weil}}\))  
**Nächste Nummer:** NEU-110

---

## Ausgangspunkt

NEU-108 zeigt: \(Q_{\mathrm{ramp}}\) ist positiv und universell, aber nicht \(Q_{\mathrm{Weil}}\). NEU-109 klärt, ob \(Q_{\mathrm{ramp}}\) zumindest das **lokale Hauptsymbol** der Weil-Quadratform ist — oder nur ein Montgomery-statistisches Nebenobjekt.

**Leitprinzip:** Nicht sofortige Addition fehlender Terme, sondern zuerst Symboltest.

---

## Satz NEU-109.1 — Schutzformulierung

$$
\boxed{Q_{\mathrm{ramp}} \text{ darf nicht direkt mit } Q_{\mathrm{Weil}} \text{ identifiziert werden, sondern höchstens mit dessen lokalem Hauptsymbol.}}
$$

Die Gleichung \(Q_{\mathrm{ramp}} + \text{Korrekturen} = Q_{\mathrm{Weil}}\) als formale Summe unabhängiger Bausteine ist erst dann legitim, wenn alle Objekte auf demselben Testfunktionsraum, in derselben Fourier-/Mellin-Normalisierung und mit derselben Renormalisierung definiert sind.

**Status: \(\checkmark[M]\)** (Schutzformulierung)

---

## Definition NEU-109.2 — Lokaler Hauptsymboltest

Der entscheidende Test lautet:

$$
\boxed{\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}}) \stackrel{?}{=} |\alpha|.}
$$

D.h.: Ist \(|\alpha|\) das lokale Hauptsymbol der Weil-Quadratform im korrekt entfalteten Spektralparameter \(\alpha\)?

**Status: \(?[O]\)** (Entscheidungstest, offen)

---

## Ausgang A — \(Q_{\mathrm{ramp}}\) ist Hauptsymbol

Falls \(\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}}) = |\alpha|\), dann ist der Rampenkanal nicht falsch, sondern unvollständig. Die Weil-Form hat dann die Zerlegung:

$$
Q_{\mathrm{Weil}} = Q_{\mathrm{ramp}} + Q_{\Gamma} + Q_{\mathrm{prime}} + Q_{\mathrm{global}} + Q_{\mathrm{ren}},
$$

wobei:

| Summand | Inhalt |
|---|---|
| \(Q_{\mathrm{ramp}}\) | lokale Nullstellenrepulsion / GUE-Mikrostruktur |
| \(Q_{\Gamma}\) | archimedische \(\Gamma\)-Faktor-Beiträge (reeller/komplexer Platz) |
| \(Q_{\mathrm{prime}}\) | Prim-/Mangoldt-Renormalisierung (\(\log p\)-Terme) |
| \(Q_{\mathrm{global}}\) | nichtlokale Paarstruktur; Rand-/Symmetriebedingungen |
| \(Q_{\mathrm{ren}}\) | Normalisierung auf gemeinsamem Testfunktionsraum |

Dann wäre **NEU-110**: Rekonstruktion der fehlenden Korrekturterme \(Q_{\Gamma}, Q_{\mathrm{prime}}, Q_{\mathrm{global}}, Q_{\mathrm{ren}}\).

**Status: \(?[O]\)**

---

## Ausgang B — \(Q_{\mathrm{ramp}}\) ist nur Paarstatistik-Nebenbild

Falls \(\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}}) \neq |\alpha|\), dann ist der Rampenkanal zwar **Montgomery-kompatibel**, aber **nicht Weil-lokalisiert**. Die Gleichung \(Q_{\mathrm{ramp}} + \cdots = Q_{\mathrm{Weil}}\) ist strukturell falsch.

Dann muss zurückgekehrt werden zum linearen explizite-Formel-Kanal:

$$
\text{explizite Formel} \to \text{Weil-Distribution} \to \text{Quadratform}
$$

statt

$$
\text{Paarstatistik} \to \text{Rampenform} \to \text{Weil-Form.}
$$

Dann wäre **NEU-110**: Rückkehr zum linearen Kanal; Verbindung zu NEU-63D (über explizite Formel und \(m_{\mathrm{arith}}\)).

**Status: \(?[O]\)**

---

## Satz NEU-109.3 — Additivitätsbedingung

$$
\boxed{\text{Die fehlenden Terme sind nicht automatisch additive Korrekturen.}}
$$

Sie werden erst dann additiv, wenn:
1. Alle Summanden auf demselben Testfunktionsraum (\(\mathcal{S}(\mathbb{R})\) oder \(C_c^\infty\)) definiert sind
2. Fourier-/Mellin-Normalisierungen übereinstimmen
3. Renormalisierungen (\(\Lambda\)-Renorm, \(N\to\infty\)-Limes) konsistent gewählt sind
4. Alle lokalen Faktoren (reell, komplex, \(p\)-adisch) einbezogen sind

**Status: \(\checkmark[M]\)**

---

## Tabellarische Statusklassifikation

| Satz | Inhalt | Status |
|------|--------|--------|
| 109.1 | Schutzformulierung: kein direktes \(Q_{\mathrm{ramp}}=Q_{\mathrm{Weil}}\) | \(\checkmark[M]\) |
| 109.2 | Hauptsymboltest \(\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}}) \stackrel{?}{=} |\alpha|\) | \(?[O]\) |
| 109.A | Ausgang A: Rampe = Hauptsymbol \(\Rightarrow\) Rekonstruktion | \(?[O]\) |
| 109.B | Ausgang B: Rampe = Nebenbild \(\Rightarrow\) Rückkehr lin. Kanal | \(?[O]\) |
| 109.3 | Additivitätsbedingung: gleicher Raum + Fourier + Renorm | \(\checkmark[M]\) |

---

## Neue Leitfrage für NEU-110

$$
\boxed{\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}}) = |\alpha|?\quad\text{Ausgang A oder B?}}
$$

Konkrete Schritte:
1. Weil-Quadratform aus Bombieri/Connes explizit aufschreiben
2. Lokales Symbol bei \(\alpha \to 0\) extrahieren
3. Vergleich mit \(|\alpha|\): Übereinstimmung oder Divergenz?
4. Falls A: nächste Korrekturen \(Q_{\Gamma}\) ausrechnen
5. Falls B: Rückkehr zu NEU-63D/explizite-Formel-Kanal

---

## Verweise

- NEU-108: \(Q_{\mathrm{ramp}}\) universell; No-Go \(\mathrm{LFF}\not\Rightarrow Q_{\mathrm{Weil}}\)
- NEU-107: Stärke-Hierarchie; \(\mathrm{LFF}\) Definition
- **Bombieri:** *Remarks on Weil's quadratic functional* (2000)
- **Connes:** *Trace formula in noncommutative geometry* (1999)
- Connes & Consani: Weil-Positivität als Trace-Formel-Phänomen
- NEU-63D: \(m_{\mathrm{arith}}(z)\) Herglotz \(\Leftrightarrow\) RH
