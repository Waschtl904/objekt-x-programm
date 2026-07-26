# NEU-91 — Quadratischer Pivot: vom Determinantenziel zur Weil-Form

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-90 (z-Rigidität; D_N(z) → exp(−γ²/4) konstant)  
**Nächste Nummer:** NEU-92

---

## Ausgangspunkt

NEU-90 hat gezeigt: Die resolventgedämpfte Fredholm-Determinante

$$
D_N(z) = \det(I + B_N^{\Lambda} R_N(z))
$$

konvergiert im festen \(z\)-Regime gegen eine nullstellenfreie Konstante

$$
D_N(z) \to e^{-\gamma^2/4}.
$$

Damit ist der direkte \(\xi\)-Anschluss strukturell ausgeschlossen. NEU-91 zieht die logisch zwingende Konsequenz: Nicht die Determinante ist der richtige Zielträger, sondern die **quadratische Mangoldt-Masse**.

$$
\boxed{\text{Nicht die Determinante ist stabil, sondern die quadratische Mangoldt-Masse.}}
$$

---

## Satz NEU-91.1 — Determinantenrigidität (Zusammenfassung)

Aus NEU-89 und NEU-90:

$$
\operatorname{Tr}(C_N(z)^k) \to 0 \quad (k \geq 3),
\qquad
\operatorname{Tr}(C_N(z)^2) \to \frac{\gamma^2}{2}.
$$

Beide Grenzwerte sind **z-unabhängig**. Damit ist jede Fredholm-Log-Determinante im festen \(z\)-Regime asymptotisch konstant:

$$
\log D_N(z) \to -\frac{\gamma^2}{4}.
$$

**Status: ✓[M]**

---

## Korollar NEU-91.2 — Zentrierungs-No-Go (Weg A erledigt)

Die natürliche Zentrierung

$$
\widetilde{\log D}_N(z) := \log D_N(z) + \frac{\gamma^2}{4} \to 0
$$

entfernt den einzigen stabilen Hauptterm. Der verbleibende Rest ist entweder trivial oder benötigt eine nichtkanonische Nachskalierung — die dann nicht mehr den robusten Hauptterm misst, sondern einen skalenabhängigen Artefakt.

**Weg A ist kein falscher Ansatz, aber er bestätigt: Die Determinante ist nicht der richtige Zielträger.**

**Status: ✗/⚠[M]** (No-Go für direkten Informationsgewinn durch Zentrierung)

---

## Definition NEU-91.3 — Quadratischer Zielwechsel

Definiere den stabilen quadratischen Ausdruck als **Hauptobjekt**, nicht als Fehlerterm:

$$
Q_N := \operatorname{Tr}(C_N(z)^2) = \operatorname{Tr}\bigl((B_N^{\Lambda} R_N(z))^2\bigr).
$$

Allgemeiner mit Testfunktion/Gewicht \(\varphi\):

$$
Q_N(\varphi) := \gamma^2 \sum_{r,n} \Lambda(n)^2\, W_N(r,n)\, \varphi(r,n),
$$

wobei \(W_N(r,n)\) das Resolvent-Gewicht aus Satz NEU-88.1 trägt. Der konstante Fall reproduziert NEU-90:

$$
Q_N(1) \to \frac{\gamma^2}{2}.
$$

Die neuen Leitfragen sind:

$$
Q_N(\varphi) \geq 0 \quad \text{für alle zulässigen } \varphi?
\qquad
Q_N(\varphi) \to Q_{\mathrm{Weil}}(\varphi)?
$$

**Status: ❓[O]**

---

## Satz NEU-91.4 — Neue Zielarchitektur

Der direkte Eulerprodukt-/Determinantenanschluss wird zurückgestuft:

$$
\text{Determinante} \to \xi \qquad \text{No-Go im festen }z\text{-Regime.} \qquad \text{Status: } \times[M]
$$

Der neue belastbare Anschluss:

$$
\boxed{
\text{quadratische Mangoldt-Masse}
\;\longrightarrow\;
\text{Weil-Quadratform}
\;\longrightarrow\;
\text{Positivitätskriterium}.
}
$$

Das ist kein Rückschritt, sondern eine Reinigung der Zielarchitektur. NEU-90 liefert den Erkenntnisgewinn: Die Resolventdämpfung stabilisiert genau diejenige quadratische Struktur, die im Weil-Bild zentral ist.

**Status: ⚠[M]**

---

## Pfadstruktur nach NEU-91

```
Mangoldt-Korrelation (Satz NEU-88.1)
    ↓
quadratischer Grenzkern Q_N(φ) (NEU-91.3)
    ↓
Weil-Form / Positivitätsobjekt  ← NEU-92
    ↓
m_arith(z) Herglotz ⟺ RH       (NEU-63D)
```

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | Determinantenrigidität: log D_N(z) → −γ²/4 | ✓[M] |
| (B) | Weg A (Zentrierung) liefert keinen neuen Grenzinhalt | ✗/⚠[M] |
| (C) | Q_N(φ) als stabiles Hauptobjekt definiert | ✓[M] (Def.) |
| (D) | Q_N(1) → γ²/2 (aus NEU-90) | ⚠[M] |
| (E) | Q_N(φ) ≥ 0 für alle φ? | ❓[O] |
| (F) | Q_N(φ) → Q_Weil(φ)? | ❓[O] |
| (G) | Determinante → ξ: No-Go im festen z-Regime | ✗[M] |

---

## Wege B und C — nachrangige Explorationspfade

- **Weg B** (z = z_N spektral skalierend): Könnte z-Sensitivität zurückgewinnen, aber der Grenzwert hängt dann vom Skalenweg ab — kein kanonisches Objekt.
- **Weg C** (h_r nichtlinear): Erfordert neue Rechtfertigung für H_N; verlässt den durch NEU-83/84 gesicherten Dreifach-Rahmen.

Beide Wege bleiben offen, sind aber nicht der primäre NEU-92-Pfad.

---

## Verweise

- NEU-88: Satz NEU-88.1 (explizite zweite Schleifenspur)
- NEU-89: Quadratisierung; ‖C_N‖ → 0
- NEU-90: T_N(z) → γ²/2 z-unabhängig; D_N(z) → exp(−γ²/4)
- NEU-63D: m_arith(z) Herglotz ⟺ RH
- Weil: *Sur les formules explicites de la théorie des nombres* (Weil-Positivität)
- Connes: *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* (1999)
- Meyer: Duke Math. J. 127 (2005) (spektrale Interpretation der Weil-Form)
