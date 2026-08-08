# NEU-110 — Symboltest: Rampenkanal versus Weil-Kanal

**Stand:** 1. Juli 2026 | **Patch:** 8. August 2026 (Pass-A Gruppe C, Patch 5/5)
**Vorgänger:** NEU-109 (Hauptsymboltest \(\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}})\stackrel{?}{=}|\alpha|\); Ausgang A/B)
**Nächste Nummer:** NEU-111

---

## Ausgangspunkt

NEU-109 formuliert den Hauptsymboltest als offene Weggabelung (Ausgang A/B). Die ursprüngliche Fassung von NEU-110 entschied auf Basis einer Herkunfts-Argumentation für **Ausgang B**. Diese Entscheidung wird durch den Pass-A-Audit als logisch nicht gedeckt zurückgezogen.

---

## Satz NEU-110.1 — Herkunft der Weil-Quadratform

$$
\boxed{Q_{\mathrm{Weil}} \text{ stammt aus der linearen expliziten Formel bzw.\ der Spurformel, nicht aus der Paarstatistik.}}
$$

Bombieri formuliert \(Q_{\mathrm{Weil}}\) als RH-äquivalente Quadratform auf dem Paley–Wiener-Raum; negative Richtungen kodieren hypothetische Off-Critical-Line-Nullstellen. Connes formuliert die explizite Formel als Spurformel auf dem Adèle-Class-Space.

**Status: ✓[M]** (Quellenangabe korrekt; Herkunft unbestritten)

---

## ~~Satz NEU-110.2 (ursprünglich)~~ — ~~Symboltest: Ausgang B~~ — **×[M] SUPERSEDED**

> **Audit-Befund (Pass-A, 8. Aug. 2026):** Die ursprüngliche Behauptung
>
> $$\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}}) \neq |\alpha|$$
>
> wurde damit begründet, dass \(Q_{\mathrm{Weil}}\) aus einer Ein-Punkt-Spurformel und
> \(|\alpha|\) aus einer Zwei-Punkt-Paarstatistik stammen.
> Das ist **kein gültiger mathematischer Schluss**:
> Zwei Objekte können aus völlig verschiedenen Konstruktionen stammen und
> dennoch dasselbe lokale Hauptsymbol besitzen.
> Verschiedene Herkunft impliziert nicht \(\sigma_1 \neq \sigma_2\).

## Satz NEU-110.2 (korrigiert) — Symboltest: offen

$$
\boxed{\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}}) \stackrel{?}{=} |\alpha| \qquad ?[O]}
$$

Um die Frage zu entscheiden, ist ein expliziter Symbolvergleich nötig:
1. \(Q_{\mathrm{Weil}}\) aus Bombieri/Connes auf dem Paley–Wiener-Raum aufschreiben
2. Lokales Symbol (Hauptterm bei \(\alpha \to 0\)) extrahieren
3. Mit \(|\alpha|\) vergleichen

Ausgang A (\(\sigma_{\mathrm{loc}} = |\alpha|\)) und Ausgang B (\(\sigma_{\mathrm{loc}} \neq |\alpha|\)) sind bislang **beide offen**.

**Status: ?[O]**

---

## ~~Satz NEU-110.3 (ursprünglich)~~ — ~~No-Go additive Rekonstruktion~~ — **×[M] SUPERSEDED**

> **Audit-Befund:** Der harte No-Go
> \(Q_{\mathrm{ramp}} + Q_\Gamma + Q_{\mathrm{prime}} + Q_{\mathrm{global}} \neq Q_{\mathrm{Weil}}\)
> wurde aus der Herkunfts-Argumentation abgeleitet und fällt mit 110.2 weg.
> Aus Zwei-Punkt- vs. Ein-Punkt-Herkunft folgt nicht, dass
> keine additive oder transformierte Rekonstruktion existieren kann.

## Satz NEU-110.3 (korrigiert) — Typisierungsbedingung für Rekonstruktionsfrage

Eine additive Zerlegung

$$Q_{\mathrm{ramp}} + Q_\Gamma + Q_{\mathrm{prime}} + Q_{\mathrm{global}} \stackrel{?}{=} Q_{\mathrm{Weil}}$$

darf erst dann behauptet **oder ausgeschlossen** werden, wenn:
1. Alle Summanden auf demselben Testfunktionsraum (z.B. Paley–Wiener) definiert sind
2. Fourier- und Mellin-Normalisierungen übereinstimmen
3. Renormalisierungen konsistent gewählt sind
4. Der Symboltest (NEU-110.2) entschieden ist

$$
\boxed{\text{Rekonstruktionsfrage offen; keine Behauptung und kein Ausschluss vor gemeinsamer Typisierung.}}
$$

**Status: ?[O]**

---

## Satz NEU-110.4 — Rampenkanal: Montgomery-Konsistenztest

$$
\boxed{\text{Die Montgomery-Rampe ist ein Konsistenztest, kein nachgewiesener Nicht-Vorfahre von }Q_{\mathrm{Weil}}.}
$$

Der Rampenkanal

$$
\Delta_N \to \mathcal{E}_{N,H} \to |\mathcal{E}_{N,H}|^2 \to K(\alpha) = |\alpha|
$$

ist wertvoll als **Montgomery-Kompatibilitätstest**. Ob er auf \(Q_{\mathrm{Weil}}\) führt oder nicht, hängt vom offenen Symboltest (110.2) ab.

**Status: ✓[M]** (Konsistenztestcharakter; kein Symbol-No-Go)

---

## Satz NEU-110.5 — Konzeptionelle Pfadtrennung

$$
\text{Weil-Kanal:}\quad \text{lineare explizite Formel} \to Q_{\mathrm{Weil}} \to \text{RH-Positivität}
$$

$$
\text{Rampenkanal:}\quad \text{Restdichte} \to \text{Paarstatistik} \to K(\alpha)=|\alpha| \to \text{Montgomery-Kompatibilität}
$$

Beide Kanäle sind konzeptionell unterschiedlich aufgebaut. Ob sie konvergieren (Ausgang A) oder divergieren (Ausgang B), wird durch den offenen Symboltest entschieden.

**Status: ✓[M]** (konzeptionelle Pfadtrennung; kein bewiesenes Symbol-No-Go)

---

## Neue Leitfrage für NEU-111

$$
\boxed{\text{Welches Objekt aus NEU-63D/NEU-91 lässt sich direkt auf Bombieris Testfunktionsraum abbilden?}}
$$

Konkrete Schritte:
1. Bombieris Testfunktionsraum identifizieren (Paley–Wiener; gerade \(L^2\)-Funktionen)
2. \(m_{\mathrm{arith}}(z)\) aus NEU-63D als Herglotz-Funktion: Fourier-Transformierte extrahieren
3. Jacobi-Operator \(A_N^{\mathrm{Jac},-}\) (NEU-91): Spektralmaß und Testfunktionsraum-Anschluss
4. Verbindung zu Connes Adèle-Class-Space / Sonin-Spur

---

## Tabellarische Statusklassifikation (korrigiert)

| Satz | Inhalt | Status |
|------|--------|--------|
| 110.1 | \(Q_{\mathrm{Weil}}\) aus lin. expl. Formel/Spurformel | ✓[M] |
| 110.2 | Symboltest \(\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}}) \stackrel{?}{=} |\alpha|\) | ?[O] |
| 110.3 | Rekonstruktionsfrage offen; Typisierungsbedingung | ?[O] |
| 110.4 | Rampe = Konsistenztest (kein bewiesener Nicht-Vorfahre) | ✓[M] |
| 110.5 | Konzeptionelle Pfadtrennung (kein Symbol-No-Go) | ✓[M] |
| 110.6 | Rückkehr linearer Weil-Kanal; Verbindung NEU-63D/91 | ?[O] |

---

## Verweise

- **Bombieri:** *Remarks on Weil's quadratic functional in number theory* (2000)
- **Connes:** *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* (1999)
- **Connes & Consani:** Scaling-Action/Sonin-Spur
- **Goldston & Montgomery:** *Pair correlation of zeros and primes in short intervals* (1987)
- NEU-109: Hauptsymboltest; Ausgang A/B offen
- NEU-108 (Patch 4/5): \(Q_{\mathrm{ramp}}\) vs. \(Q_{\mathrm{Weil}}\); Typisierungswarnung
- NEU-63D: \(m_{\mathrm{arith}}(z)\) Herglotz \(\Leftrightarrow\) RH
- NEU-91: Jacobi-Operator \(A_N^{\mathrm{Jac},-}\)
