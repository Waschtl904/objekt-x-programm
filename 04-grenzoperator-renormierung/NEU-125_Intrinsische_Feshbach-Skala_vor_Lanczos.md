# NEU-125 — Intrinsische Feshbach-Skala vor Lanczos

**Stand:** 6. Juli 2026  
**Anschluss:** NEU-79 (N-Flaschenhals, Feshbach-Kanalzahl), NEU-123.H–I (Jacobi-Renormierungsverbot)  
**Nächste Einheit:** NEU-126 Rücklese NEU-62 — explizite $a_N$- und Gewichtsskalen

---

## 125.0 Leitfrage

NEU-123.H–I schließen jede nachträgliche skalare oder diagonale Jacobi-Renormierung aus, sofern sie die Jacobi-Koeffizienten *nach* der Lanczos-Extraktion stabilisieren soll.  
NEU-79 enthält dagegen eine intrinsische Kanalzahl-Skala

$$J_N^- = \sqrt{N}\, U_N S_N R_N D_{BC,N} U_N^\dagger, \quad [M]$$

mit $\sqrt{N} \sim N$. Diese Skala stammt nicht aus einer willkürlichen Jacobi-Nachnormierung, sondern aus der Feshbach-Schur-Struktur, insbesondere aus der unnormalisierten Kollapsrelation $\Omega_N^\dagger \Omega_N \sim N \cdot I$.  

Die Leitfrage lautet daher:  
**Ist die NEU-79-Kanalzahl eine echte Prä-Lanczos-Skala — oder nur eine skalare Jacobi-Kovarianz?**

---

## 125.1 Skala vor oder nach Lanczos?

Sei $A_N$ ein selbstadjungierter Feshbach-Input und $\Omega_N$ der Lanczos-Startvektor.  
Für eine skalare Multiplikation $A_N^c = c_N A_N$, $c_N > 0$, gilt wegen der **Lanczos-Kovarianz**:

$$a_{j,N}^c = c_N a_{j,N}, \quad b_{j,N}^c = c_N b_{j,N}.$$

Insbesondere:

$$\frac{b_{2,N}^c}{b_{1,N}^c} = \frac{b_{2,N}}{b_{1,N}}.$$

**Befund:** Die Tatsache, dass $\sqrt{N}$ in NEU-79 *vor* Lanczos entsteht, macht sie strukturell zulässig — aber solange sie nur skalar wirkt, kann sie die Jacobi-Doppelbarriere nicht lösen. *Skalar vor Lanczos ist erlaubt, aber nicht ausreichend.*

**Status:** ✓[M]

---

## 125.2 Selbstadjungiertheit und Herglotz-Kompatibilität

Für $c_N > 0$ bleibt $A_N^c = c_N A_N$ selbstadjungiert.  
Die zugehörige Stieltjes-Herglotz-Funktion transformiert mit positivem Vorfaktor:

$$m_N^c(z) = \langle \Omega_N, (J_N^c - z)^{-1} \Omega_N \rangle \implies m_N^c(z) = c_N^{-1} m_N(z/c_N).$$

Damit bleibt die Herglotz-Eigenschaft erhalten.

**Befund:** Positive skalare Prä-Lanczos-Renormierung ist nicht wegen Selbstadjungiertheit oder Herglotz verboten. Sie scheitert nur an der Quotienteninvarianz.

**Status:** ✓[M]

---

## 125.3 Wirkung auf $b_{1,N}$

NEU-123.A–G liefern numerisch bzw. modellhaft:

$$b_{1,N} \sim \frac{\sqrt{N}}{N}, \quad \frac{b_{2,N}}{b_{1,N}} \sim N.$$

Für $A_N^c = c_N A_N$ gilt $b_{1,N}^c = c_N b_{1,N}$. Zur Stabilisierung von $b_{1,N}$ allein müsste gelten:

$$c_N \sim \frac{N}{\sqrt{N}} = \sqrt{N}.$$

Kandidatenskalen im Vergleich:

| Skala | Asymptotik $c_N \cdot b_{1,N}$ | Kommentar |
|---|---|---|
| $c_N = N$ | $\sim \sqrt{N} \to \infty$ | Überkopplung |
| $c_N = N^{-1}$ | $\sim N^{-3/2} \to 0$ | Unterkopplung |
| $c_N = \sqrt{N}$ | $\sim 1$ | kritische Skala, aber Quotient bleibt divergent |

Offene Frage: Gibt es in NEU-62/67–75/79 eine intrinsische Feshbach-Größe der Ordnung $c_N^{\mathrm{crit}} \sim \sqrt{N}$?

**Status:** ❓[O]

---

## 125.4 Wirkung auf $b_{2,N}/b_{1,N}$

Skalare Multiplikation kann den Quotienten **nicht** verändern:

$$\frac{b_{2,N}^c}{b_{1,N}^c} = \frac{c_N b_{2,N}}{c_N b_{1,N}} = \frac{b_{2,N}}{b_{1,N}} \sim N.$$

Daher gilt: **Jede skalare Prä-Lanczos-Renormierung scheitert an NEU-123.G–H.** Sie kann $b_{1,N}$ höchstens einzeln stabilisieren, aber nicht die zweite Jacobi-Stufe kontrollieren.

**Status:** ✓[M] unter NEU-123.G (numerischer Input: ⚠[M_heur+num])

---

## 125.5 Konsequenz: Nichtskalare symmetrische Feshbach-Gewichtung

Um sowohl $b_{1,N}^{\mathrm{ren}} \sim 1$ als auch $b_{2,N}^{\mathrm{ren}}/b_{1,N}^{\mathrm{ren}} = O(1)$ zu erreichen, reicht keine skalare Renormierung.  
Der einzige verbleibende zulässige Kandidat ist eine **nichtskalare, symmetrische Prä-Lanczos-Gewichtung**:

$$B_N \mapsto W_N^{1/2} B_N W_N^{1/2}, \quad W_N > 0.$$

Diese Operation ist nicht dasselbe wie eine diagonale Jacobi-Ähnlichkeit $J_N \mapsto D_N^{-1} J_N D_N$. Sie ist nur dann zulässig, wenn $W_N$:
1. *vor* Lanczos auf Feshbach-Ebene definiert ist,
2. positiv und symmetrisch wirkt,
3. aus der inneren Kanal-, Kollaps- oder Schur-Komplementstruktur stammt,
4. Selbstadjungiertheit erhält,
5. die Herglotz-Stieltjes-Theorie aus NEU-119 bewahrt.

**Status:** ❓[O]

---

## 125.6 Kandidatenskalen aus NEU-79

| Kandidat | Wirkung auf $b_{1,N}$ | Befund |
|---|---|---|
| $c_N = N$ | $b_{1,N}^c \sim \sqrt{N}$ | Überkopplung |
| $c_N = N^{-1}$ | $b_{1,N}^c \sim N^{-3/2}$ | Unterkopplung |
| $c_N = \sqrt{N}$ | $b_{1,N}^c \sim 1$ | kritische Skala, aber Quotient bleibt divergent |
| $W_N^{1/2} B_N W_N^{1/2}$ | kann mehrere Stufen unterschiedlich gewichten | einziger offener Ausweg |

Damit trennt sich die Analyse in zwei Ebenen:
- **Skalare Feshbach-Skala:** zulässig, aber unzureichend.
- **Gradierte Feshbach-Skala:** zulässig genau dann, wenn intrinsisch.

---

## 125.F Fazit

NEU-79 liefert tatsächlich eine intrinsische Prä-Lanczos-Skala $\sqrt{N}$. Das ist methodisch wichtig, weil sie nicht unter das diagonale Jacobi-Renormierungsverbot aus NEU-123.I fällt.

Aber: Solange diese Skala nur *skalar* wirkt, ist sie Lanczos-kovariant und verändert die Jacobi-Quotienten nicht. Daher kann sie die Doppelbarriere $b_{1,N} \to 0$, $b_{2,N}/b_{1,N} \to \infty$ nicht lösen.

Der eigentliche nächste Schritt ist daher nicht die Wahl eines besseren skalaren Faktors, sondern die Rücklese von NEU-62/67–75/79 nach einer **intrinsischen positiven Gewichtung $W_N > 0$ auf Feshbach-Ebene**.

**Nächste Einheit:** NEU-126 — Rücklese NEU-62: Gibt es ein intrinsisches $W_N$?

**Gesamtstatus:** ❓[O] — skalare Prä-Lanczos-Skalen ausgeschlossen als vollständige Rettung; gradierte Feshbach-Gewichtung bleibt offen.

---

## Verweise

- [NEU-79](../02-jacobi-limes/NEU-079_Kanalzahl_Skalierung_Jacobi_Limes.md) — $N$-Flaschenhals und Feshbach-Kanalzahl
- [NEU-62](../02-jacobi-limes/NEU-062_normalisierungsrigiditat_jacobi_limes.md) — Normalisierungsrigidität, $a_N$-Asymptotik, mögliche intrinsische Gewichtung
- [NEU-123A](NEU-123A_Jacobi_Koeffizienten_Extraktion.md) — $b_{1,N} \to 0$
- [NEU-123G](NEU-123G_Zweite_Offdiagonale_Skaleninkohaerenz.md) — $b_{2,N}/b_{1,N} \sim N$ numerisch
- [NEU-123H](NEU-123H_No_scalar_renormalization.md) — keine skalare $N$-Rettung bei divergentem Quotienten
- [NEU-123I](NEU-123I_Gradierte_Renormierung_Herglotz.md) — diagonale Jacobi-Ähnlichkeit verletzt Produkt-/Herglotz-Filter
- Teschl, *Jacobi Operators*, AMS 2000
