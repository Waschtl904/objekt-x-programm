# NEU-111 — Herglotz-Weil-Brücke und Jacobi-Realisierung

**Stand:** 1. Juli 2026 | **Patch:** 8. August 2026 (Pass-A Gruppe D, Patch D-1/2)
**Vorgänger:** NEU-110 (Symboltest \(\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}})\stackrel{?}{=}|\alpha|\); Ausgang A/B offen nach Patch)
**Nächste Nummer:** NEU-112

---

## ~~Ausgangspunkt (ursprünglich)~~ — **×[M] SUPERSEDED**

> **Patch-Notiz (Pass-A, 8. Aug. 2026):** Die ursprüngliche Fassung begann mit der Aussage,
> NEU-110 habe **Ausgang B** (\(\sigma_{\mathrm{loc}}(Q_{\mathrm{Weil}})\neq|\alpha|\)) erzwungen.
> Das ist nach dem Patch von NEU-110 (Gruppe C, Patch 5/5) nicht mehr gültig:
> Der Symboltest ist offen; weder Ausgang A noch B ist bewiesen.
> NEU-111 darf den linearen Herglotz-Weil-Kanal untersuchen,
> aber nicht mehr behaupten, NEU-110 habe ihn erzwungen.

## Ausgangspunkt (korrigiert)

$$
\boxed{\text{Unabhängig von der offenen Symbolfrage (NEU-110) untersuchen wir den linearen Herglotz-Weil-Kanal.}}
$$

Die lineare explizite Formel und die Connes-Spurformel legen nahe, dass \(m_{\rm arith}\) als Herglotz-Funktion die richtige Eingangsgröße für eine Weil-Identifikation ist. Ob der Rampenkanal (NEU-110) dieselbe oder eine andere Struktur realisiert, hängt vom offenen Symboltest ab.

---

## Satz NEU-111.1 — \(m_{\rm arith}\) Herglotz \(\Leftrightarrow\) RH (korrigierte Typisierung)

Definitionen:

$$
\Xi(z) := \xi\!\left(\tfrac{1}{2}+iz\right), \qquad
m_{\rm arith}(z) := -\frac{\Xi'(z)}{\Xi(z)} = -i\,\frac{\xi'}{\xi}\!\left(\tfrac{1}{2}+iz\right).
$$

Unter RH ist die Menge der normierten Nullstellen

$$
\Gamma := \{\gamma\in\mathbb{R} : \xi(\tfrac{1}{2}-i\gamma)=0\},
$$

und mit den zugehörigen Multiplizitäten \(m_\gamma \geq 1\) gilt die **signed-\(\Gamma\)-Darstellung** (kanonisch symmetrisch konvergent):

$$
\boxed{m_{\rm arith}(z) = \sum_{\gamma\in\Gamma} \frac{m_\gamma}{\gamma - z}.}
$$

Der Herglotz-Charakter folgt aus der Hadamard-Darstellung von \(\xi'/\xi\); off-line Nullstellen würden Pole von \(m_{\rm arith}\) in \(\mathbb{C}^+\) erzeugen und den Herglotz-Charakter zerstören.

> **Typisierungsnotiz:** Die vage Schreibweise \(\sum_\gamma \frac{1}{\gamma-z} + \text{Renormierung}\)
> ohne signed-\(\Gamma\), Multiplizitäten und Typ der Renormierung ist **durch diese Fassung ersetzt**.
> Gamma-, Pol- und Primbeiträge sind keine zusätzlichen Atome des Herglotz-Spektralmaßes;
> sie erscheinen bei der faktoriellen Zerlegung der expliziten Formel über
> \(s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\), aber nicht im Herglotz-Spektralmaß von \(m_{\rm arith}\).

**Status: \(\checkmark[M]\)** (unter RH; signed-\(\Gamma\)+Multiplizitäten)

---

## Satz NEU-111.2 — Pfadordnung (Architektur)

Die angestrebte Kette lautet:

$$
A_N^{\rm Jac,-} \;\longrightarrow\; m_{\Omega,N} \;\longrightarrow\; m_{\rm arith}.
$$

> **Patch-Notiz:** Zum Zeitpunkt von NEU-111 war \(m_{\Omega,N}\) noch nicht sauber definiert.
> NEU-119 stellt ausdrücklich fest, dass weder \(\Omega_N\) noch \(m_{\Omega,N}\) in dieser Phase
> sauber typisiert waren, und lässt die kanonische Wahl von \(\Omega_N\) weiterhin offen.
> Der Pfeil \(A_N^{\rm Jac,-}\to m_{\Omega,N}\to m_{\rm arith}\) ist daher in NEU-111
> **Programmarchitektur**, kein konstruierter mathematischer Pfeil.

Der rettbare Kern:

$$
\boxed{m_{\Omega,N} \to m_{\rm arith} \text{ muss bewiesen werden,
 bevor die Jacobi-Struktur mit der Weil-Geometrie identifiziert wird.}}
$$

Das ist der richtige methodische Schutz: keine Identifikation vor Typisierung.

**Status: \(\checkmark[M]_{\rm part}\)** (Architektur korrekt; \(m_{\Omega,N}\) erst in NEU-119 definiert)

---

## Satz NEU-111.3 — Jacobi-Positivität: Typisierungs-Firewall

> **Patch-Notiz:** Die ursprüngliche Fassung formulierte einen harten No-Go:
> ein beliebiges Jacobi-Spektralmaß sei kein Connes-Weil-Objekt.
> Als allgemeiner mathematischer Ausschlusssatz ist das nicht bewiesen:
> ein speziell konstruiertes Jacobi-Maß könnte prinzipiell gerade das gewünschte
> Spektralmaß realisieren. Der No-Go wird zur **Typisierungs-Firewall** abgeschwächt.

$$
\boxed{\text{Jacobi-Positivität allein identifiziert kein Weil-/Connes-Objekt.}}
$$

Ohne zusätzliche arithmetische Information (Nullstellenstruktur, explizite Formel, Adele-Class-Space) führt ein positives Jacobi-Spektralmaß nicht automatisch auf \(Q_{\rm Weil}\).

**Status: \(\checkmark[M]_{\rm part}\)** (Typisierungswarnung gültig; harter No-Go zurückgezogen)

---

## Satz NEU-111.4 — Die beiden Flaschenhälse

**Test 1 — Herglotz-Weil-Test:**

$$
m_{\rm arith}(z) \stackrel{?}{\longrightarrow} W_\xi^{\rm norm}[\Phi]
$$

Das Herglotz-Objekt \(m_{\rm arith}\) muss über einen Autokorrelations-/Amplitudenlift in die lineare Weil-Distribution überführt werden. Der Lift ist durch den Positivierungsschritt \(\Phi = \phi^* * \phi\) in NEU-113 später expliziert.

**Status: ?[O]**

**Test 2 — Jacobi-Limes:**

$$
m_{\Omega,N}(z) \stackrel{?}{\longrightarrow} m_{\rm arith}(z) \quad (N\to\infty)
$$

Dieser Grenzübergang erfordert die kanonische Wahl von \(\Omega_N\), die in **NEU-119** erst definiert (und deren Existenz dort noch als offen bezeichnet) wird.

**Status: ?[O]** (offener Schritt; \(m_{\Omega,N}\)-Struktur: NEU-119)

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| 111.0 | Ausgangspunkt: unabhängig von Symbolfrage | ✓[M] (korrigiert) |
| 111.1 | \(m_{\rm arith}\) Herglotz \(\Leftrightarrow\) RH; signed-\(\Gamma\)+Multiplizitäten | ✓[M] |
| 111.2 | Pfadordnung \(A_N^{\rm Jac,-}\to m_{\Omega,N}\to m_{\rm arith}\); Architektur | ✓[M]_part |
| 111.3 | Jacobi-Positivität identifiziert kein Weil-Objekt | ✓[M]_part |
| 111.4a | Herglotz-Weil-Test | ?[O] |
| 111.4b | Jacobi-Limes \(m_{\Omega,N}\to m_{\rm arith}\) | ?[O] |

---

## Verweise

- **Bombieri:** *Remarks on Weil's quadratic functional in number theory* (2000)
- **Connes:** *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* (1999)
- **Hadamard:** Produktdarstellung von \(\xi\)
- NEU-110 (Patch 5/5): Symboltest offen; Ausgang A/B beide offen
- **NEU-113:** Autokorrelationslift \(\Phi=\phi^**\phi\); \(W_{\rm zeros}[\Phi]\to Q_{\rm zeros}[\phi]\)
- **NEU-119:** Definition \(m_{\Omega,N}\); kanonische \(\Omega_N\)-Wahl offen
- NEU-91: Jacobi-Operator \(A_N^{\rm Jac,-}\)
- NEU-63D: \(m_{\rm arith}(z)\) Herglotz \(\Leftrightarrow\) RH (frühere Herleitung)
