# NEU-110 — Symboltest: Rampenkanal versus Weil-Kanal

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-109 (Hauptsymboltest \(\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}})\stackrel{?}{=}|\alpha|\); Ausgang A/B)  
**Nächste Nummer:** NEU-111

---

## Ausgangspunkt

NEU-109 formuliert den Hauptsymboltest als Weggabelung. NEU-110 entscheidet auf Basis der Quellenlage (Bombieri 2000, Connes 1999, Connes\u2013Consani) für **Ausgang B**.

---

## Satz NEU-110.1 — Herkunft der Weil-Quadratform

$$
\boxed{Q_{\mathrm{Weil}} \text{ stammt aus der linearen expliziten Formel bzw.\ der Spurformel, nicht aus der Paarstatistik.}}
$$

Bombieri formuliert \(Q_{\mathrm{Weil}}\) als RH-äquivalente Quadratform: Ihre Fourier-Transformierte liefert eine Quadratform in unendlich vielen Variablen; negative Richtungen kodieren hypothetische Off-Critical-Line-Nullstellen. Das ist ein **ein-teilchenartiger Positivitätskanal** (eine Nullstelle, nicht ein Paar).

Connes formuliert die explizite Formel als Spurformel auf dem Ad\`ele-Class-Space; Connes\u2013Consani verorten die Positivit\u00e4t archimedisch in einer Scaling-Action/Sonin-Spur-Struktur.

**Status: \(\checkmark[M]\)**

---

## Satz NEU-110.2 — Symboltest: Ausgang B

$$
\boxed{\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}}) \neq |\alpha|}
$$

sofern \(|\alpha|\) als Montgomery/GUE-Formfaktor interpretiert wird.

Begründung: Die Rampe \(K(\alpha) = |\alpha|\) entsteht auf der **Fourierseite der Nullstellen-Paarstatistik**. Sie gehört zum verbundenen Zwei-Punkt-/Varianzkanal (Goldston\u2013Montgomery/Chan), nicht zum ursprünglichen Weil-Funktional. Die Weil-Form ist ein-teilchenartig; das Rampenprofil ist eine Zwei-Punkt-Statistik.

**Status: \(\checkmark[M]\)** (Ausgang B)

---

## Satz NEU-110.3 — No-Go: Additive Rekonstruktion unzulässig

$$
\boxed{Q_{\mathrm{ramp}} + Q_{\Gamma} + Q_{\mathrm{prime}} + Q_{\mathrm{global}} \neq Q_{\mathrm{Weil}}}
$$

als additive Rekonstruktionsstrategie, solange \(Q_{\mathrm{ramp}}\) aus dem Montgomery-Formfaktor stammt. Die strukturelle Diskrepanz ist nicht durch Additivkorrektur überbrückbar, weil die Herkunftsobjekte verschieden sind (Zwei-Punkt-Statistik vs.\ Ein-Teilchen-Spurformel).

**Status: \(\checkmark[M]\)** (No-Go)

---

## Satz NEU-110.4 — Rampenkanal: Montgomery-Konsistenztest, kein Weil-Vorfahre

$$
\boxed{\text{Montgomery-Rampe ist nicht die Weil-Form, sondern eine Zwei-Punkt-Schattenform.}}
$$

Der Rampenkanal bleibt wertvoll als **Montgomery-Konsistenztest**:

$$
\Delta_N \to \mathcal{E}_{N,H} \to |\mathcal{E}_{N,H}|^2 \quad\Rightarrow\quad K(\alpha) = |\alpha| \quad\Rightarrow\quad \text{Montgomery-kompatibel.}
$$

Aber er ist kein direkter Vorfahre von \(Q_{\mathrm{Weil}}\).

**Status: \(\checkmark[M]\)**

---

## Satz NEU-110.5 — Pfadtrennung

$$
\text{Weil-Kanal:}\quad
\text{lineare explizite Formel} \to Q_{\mathrm{Weil}} \to \text{RH-Positivität}
$$

$$
\text{Rampenkanal:}\quad
\text{Restdichte} \to \text{Paarstatistik} \to K(\alpha)=|\alpha| \to \text{Montgomery-Kompatibilität}
$$

Beide Kanäle sind kompatibel, aber **nicht identisch**. Nur der Weil-Kanal führt zu RH.

**Status: \(\checkmark[M]\)**

---

## Neue Leitfrage für NEU-111

$$
\boxed{\text{Welches Objekt aus NEU-63D/NEU-91 lässt sich direkt auf Bombieris Testfunktionsraum abbilden?}}
$$

Konkrete Schritte:
1. Bombieris Testfunktionsraum identifizieren (Paley\u2013Wiener; gerade \(L^2\)-Funktionen mit Träger-Bedingung)
2. \(m_{\mathrm{arith}}(z)\) aus NEU-63D als Herglotz-Funktion: Fourier-Transformierte / Darstellungsma\ss{} extrahieren
3. Jacobi-Operator \(A_N^{\mathrm{Jac},-}\) (NEU-91): Hat sein Spektralma\ss{} einen natürlichen Testfunktionsraum-Anschluss?
4. Verbindung zu Connes Adele-Class-Space / Sonin-Spur?

---

## Tabellarische Statusklassifikation

| Satz | Inhalt | Status |
|------|--------|--------|
| 110.1 | \(Q_{\mathrm{Weil}}\) aus lin.\ expl.\ Formel/Spurformel | \(\checkmark[M]\) |
| 110.2 | \(\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}}) \neq |\alpha|\) (Ausgang B) | \(\checkmark[M]\) |
| 110.3 | No-Go additive Rekonstruktion \(Q_{\mathrm{ramp}}+\cdots\neq Q_{\mathrm{Weil}}\) | \(\checkmark[M]\) |
| 110.4 | Rampe = Zwei-Punkt-Schattenform; Konsistenztest | \(\checkmark[M]\) |
| 110.5 | Pfadtrennung Weil-Kanal vs.\ Rampenkanal | \(\checkmark[M]\) |
| 110.6 | Rückkehr linearer Weil-Kanal; Verbindung NEU-63D/91 | \(?[O]\) |

---

## Verweise

- **Bombieri:** *Remarks on Weil's quadratic functional in number theory* (2000) — \(Q_{\mathrm{Weil}}\) RH-äquivalent; ein-teilchenartig
- **Connes:** *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* (1999)
- **Connes & Consani:** Scaling-Action/Sonin-Spur; archimedische Positivität
- **Goldston & Montgomery:** *Pair correlation* (1987) — Zwei-Punkt-Kanal
- NEU-109: Hauptsymboltest; Ausgang A/B
- NEU-63D: \(m_{\mathrm{arith}}(z)\) Herglotz \(\Leftrightarrow\) RH
- NEU-91: Jacobi-Operator \(A_N^{\mathrm{Jac},-}\)
