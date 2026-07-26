# NEU-111 — Herglotz-Weil-Brücke und Jacobi-Realisierung

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-110 (Ausgang B; Pfadtrennung Weil- vs. Rampenkanal)  
**Nächste Nummer:** NEU-112

---

## Ausgangspunkt

NEU-110 erzwingt Ausgang B: Der Weil-Kanal läuft über die lineare explizite Formel, nicht über den Rampenkanal. NEU-111 ordnet die Objekte des Weil-Kanals in ihrer logischen Abhängigkeit.

**Leitprinzip:**

$$
\boxed{m_{\mathrm{arith}} \text{ ist der primäre Weil-Kandidat; }
A_N^{\mathrm{Jac},-} \text{ ist nur ein Realisierungs-/Approximationskandidat.}}
$$

---

## Satz NEU-111.1 — Primärer Weil-Kandidat: \(m_{\mathrm{arith}}(z)\)

Aus NEU-63D ist

$$
m_{\mathrm{arith}}(z)
:= -i\frac{\xi'}{\xi}\!\left(\tfrac{1}{2}+iz\right)
$$

eine Herglotz-Funktion genau dann, wenn RH gilt. Unter RH hat sie die Stieltjes-Darstellung:

$$
m_{\mathrm{arith}}(z)
\sim
\sum_{\gamma}
\frac{1}{\gamma - z}
+ \text{Renormierung},
$$

wobei \(\rho = \tfrac{1}{2}+i\gamma\) über die kritischen Nullstellen läuft. Das ist ein **ein-teilchenartiges** Spektralobjekt auf derselben Achse wie Bombieris Weil-Funktional.

**Status: ✓[M]** (aus NEU-63D)

---

## Satz NEU-111.2 — Pfadordnung

Die korrekte Abhängigkeitsordnung lautet:

$$
m_{\mathrm{arith}}
\longrightarrow
\text{Bombieri/Weil-Testfunktionsraum}
\longrightarrow
Q_{\mathrm{Weil}},
$$

und erst sekundär:

$$
A_N^{\mathrm{Jac},-}
\longrightarrow
m_{\Omega,N}(z) := \langle \Omega,(A_N^{\mathrm{Jac},-}-z)^{-1}\Omega\rangle
\longrightarrow
m_{\mathrm{arith}}.
$$

Der direkte Sprung \(A_N^{\mathrm{Jac},-} \to\) Connes-Adèle-Class-Spurformel ist **unzulässig**, solange nicht gezeigt ist:
1. \(m_{\Omega,N} \to m_{\mathrm{arith}}\) lokal gleichmäßig auf \(\mathbb{C}^+\)
2. Die entstehende Spur hat auf Bombieris/Connes' Testfunktionsraum dieselbe Renormalisierung wie \(Q_{\mathrm{Weil}}\)

**Status: ✓[M]**

---

## Satz NEU-111.3 — No-Go: Beliebiges Jacobi-Spektralmaß ist kein Connes-Weil-Objekt

$$
\boxed{\text{Ein beliebiges positives Jacobi-Spektralmaß ist noch kein Connes-Weil-Objekt.}}
$$

Begründung: Connes' Spurformel ist nicht „Spektralmaß allgemein", sondern eine spezifische Scaling-Action-/Adèle-Class-Spurstruktur mit archimedischen PSWF-Korrekturen (Connes–Consani). Der Jacobi-Operator muss diese Struktur erst über \(m_{\Omega,N} \to m_{\mathrm{arith}}\) und den korrekten Testfunktionsraum nachweisen.

**Status: ✓[M]** (No-Go)

---

## Definition NEU-111.4 — Zwei präzise Flaschenhals-Tests

**Test 1 — Herglotz-Weil-Test:**

$$
m_{\mathrm{arith}}
\stackrel{?}{\longmapsto}
Q_{\mathrm{Weil}}
$$

auf dem Paley–Wiener-/kompakt getragenen Testfunktionsraum von Bombieri. Konkret: Gibt es einen natürlichen Auswertungsoperator

$$
T:\; f \mapsto \int m_{\mathrm{arith}}(t)\hat{f}(t)\,dt
$$

der mit Bombieris Weil-Quadratform zusammenfällt?

**Status: ❓[O]**

**Test 2 — Jacobi-Realisierungstest:**

$$
m_{\Omega,N}(z) \stackrel{?}{\longrightarrow} m_{\mathrm{arith}}(z)
$$

lokal gleichmäßig auf \(\mathbb{C}^+\) (bzw. im Sinne schwacher Konvergenz der Spektralmaße). Erst wenn dieser Test besteht, ist \(A_N^{\mathrm{Jac},-}\) eine legitime endliche Jacobi-Realisierung des Weil-Kanals.

**Status: ❓[O]**

---

## Tabellarische Statusklassifikation

| Satz | Inhalt | Status |
|------|--------|--------|
| 111.1 | \(m_{\mathrm{arith}}\) primärer Weil-Kandidat (Stieltjes/Herglotz) | ✓[M] |
| 111.2 | Pfadordnung: \(m_{\mathrm{arith}} \to Q_{\mathrm{Weil}}\) vor \(A_N^{\mathrm{Jac},-}\) | ✓[M] |
| 111.3 | No-Go: Jacobi-Spektralmaß ≠ Connes-Weil | ✓[M] |
| 111.4a | Herglotz-Weil-Test: \(m_{\mathrm{arith}} \stackrel{?}{\to} Q_{\mathrm{Weil}}\) | ❓[O] |
| 111.4b | Jacobi-Realisierungstest: \(m_{\Omega,N} \stackrel{?}{\to} m_{\mathrm{arith}}\) | ❓[O] |

---

## Neue Leitfrage für NEU-112

$$
\boxed{m_{\mathrm{arith}}(z) \stackrel{?}{\longmapsto} Q_{\mathrm{Weil}}\quad\text{(Herglotz-Weil-Test auf Bombieri-Testfunktionsraum)}}
$$

Konkrete Schritte:
1. Bombieris Testfunktionsraum präzise aufschreiben (Paley–Wiener \(PW_t\); gerade \(L^2\)-Funktionen, Träger \([-t,t]\))
2. Weil-Quadratform \(Q_{\mathrm{Weil}}[f]\) nach Bombieri explizit ausschreiben (archimedischer Term + Primterm + Nullstellenterm)
3. \(m_{\mathrm{arith}}(z)\) Stieltjes-Darstellung in Bombieri-Normalisierung einsetzen
4. Vergleich: stimmen Nullstellenterm und \(\sum_\gamma 1/(\gamma-z)\)-Beitrag überein?
5. Archimedischer Rest: \(\Gamma\)-Terme in Bombieri = archimedische PSWF-Terme in Connes–Consani?

---

## Verweise

- NEU-63D: \(m_{\mathrm{arith}}(z)\) Herglotz \(\Leftrightarrow\) RH
- NEU-91: \(A_N^{\mathrm{Jac},-}\) Jacobi-Operator
- NEU-110: Ausgang B; Pfadtrennung
- **Bombieri:** *Remarks on Weil's quadratic functional* (2000) — Paley–Wiener-Raum; \(Q_{\mathrm{Weil}}\) explizit
- **Connes:** *Trace formula in noncommutative geometry* (1999)
- **Connes & Consani:** Scaling-Action / archimedische PSWF-Terme
