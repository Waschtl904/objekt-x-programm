# NEU-220c — PD-3d: Repository-Audit Weil-Normierung und Gamma-Vorfaktor

**Knoten:** `[O-220-1-PD3d-Weil-normalization]`  
**Stand:** 25. Juli 2026  
**Vorgänger:** NEU-220b (PD-3a–c ✓[M])  
**Quellen:** NEU-26/werkzeuge, NEU-29/werkzeuge, NEU-36/werkzeuge, NEU-39/werkzeuge  
**Ziel:** Drei Normierungsebenen getrennt auditieren; PD-3d von ?[O] auf ✓[M]_part heben.

---

## 0. Aufgabe und Methodik

PD-3d fragt, welcher der drei Vorfaktoren

$$
T_\Gamma^{\mathrm{raw}}(h), \qquad \frac{1}{2\pi}T_\Gamma^{\mathrm{raw}}(h), \qquad \frac{1}{2\pi}T_\Gamma^{\mathrm{sym}}(h)
$$

der repository-kompatible Weil-Gamma-Term ist.

Die Entscheidung gliedert sich in drei logisch unabhängige Ebenen:

1. **ξ-Normalisierung** — welche Formel für ξ(s) ist autoritativ?
2. **Konturmaß** — welcher Faktor entsteht aus der Parametrisierung s = ½ + it?
3. **Testfunktionssymmetrie** — rohes hermitesches Symbol oder explizite Symmetrisierung?

Diese drei Ebenen sind strikt auseinanderzuhalten.

---

## 1. Ebene 1: ξ-Normalisierung (✓ quellenfest)

### 1.1 Autoritative Formel

Aus NEU-26 (X.2-Spektralformel) ist autoritativ festgelegt:

$$
\boxed{
\xi(s) = \frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
}
$$

NEU-36 §5.4 verwendet dieselbe Zerlegung mit explizitem Gamma-Faktor-Fehler:

$$
\frac{\xi'}{\xi}(s)
= \frac{1}{2}\log\pi^{-1}
+ \frac{1}{2}\frac{\Gamma'}{\Gamma}\!\left(\frac{s}{2}\right)
+ \frac{1}{s}
+ \frac{1}{s-1}
+ \frac{\zeta'}{\zeta}(s).
$$

NEU-39 §10 hält explizit fest: Die Gamma-/Polterme sind von der nichtarchimedischen Euler-Schicht ζ′/ζ strikt getrennt und als eigener offener Punkt markiert (`❓ [O]`).

### 1.2 Gammaanteil auf s = ½ + it

Auf der kritischen Linie s = ½ + it, also mit s/2 = ¼ + it/2, lautet der reine Gammaanteil:

$$
\boxed{
\gamma_\infty(t)
= -\frac{1}{2}\log\pi + \frac{1}{2}\psi\!\left(\frac{1}{4}+\frac{it}{2}\right),
}
$$

exakt konsistent mit NEU-220a/b. Der Pol-Term 1/s + 1/(s−1) gehört in den separaten Pol-/Randterm; er ist kein Teil von γ∞.

**Status Ebene 1:** ✓ quellenfest — keine Normierungsambiguität.

---

## 2. Ebene 2: Konturmaß (✓ quellenfest)

### 2.1 Repository-Kontur in NEU-29

NEU-29 §2.1 definiert den Doppelresolvent-Funktionalkalkül autoritativ als:

$$
f(D_X^{BC}) := \frac{1}{2\pi i}\int_\Gamma F(s)\cdot(s-D_X^{BC})^{-2}\,ds.
$$

NEU-29 §3 schreibt die Cauchy-Spurformel:

$$
\operatorname{Tr}_{Wres}^{top}(f(D_X^{BC})\cdot L_3^\circ)
= \frac{1}{2\pi i}\int_\Gamma F(s)\cdot K_\xi(s)\,ds.
$$

Dies ist der kanonische Repository-Konturkalkül.

### 2.2 Parametrisierung s = ½ + it

Mit der Parametrisierung

$$
s = \frac{1}{2}+it, \qquad ds = i\,dt
$$

wird der Konturintegrand:

$$
\frac{1}{2\pi i}\int_\Gamma (\cdots)\,ds
\;\longrightarrow\;
\frac{1}{2\pi i}\int_{\mathbb R}(\cdots)\cdot i\,dt
= \frac{1}{2\pi}\int_{\mathbb R}(\cdots)\,dt.
$$

Der Faktor 1/(2π) ist daher nicht eine zusätzliche Konvention, sondern eine direkte algebraische Konsequenz des in NEU-29 festgelegten Konturmaßes ds/(2πi) und der Parametrisierung der kritischen Linie.

**Status Ebene 2:** ✓ quellenfest — Vorfaktor 1/(2π) ist durch NEU-29 und s = ½ + it zwingend.

---

## 3. Ebene 3: Testfunktionssymmetrie (?[O] → Restlücke)

### 3.1 Was NEU-29 nicht festlegt

NEU-29 behandelt den Cauchy-Funktionalkalkül mit allgemeinen holomorphen Testfunktionen F auf Konturen Γ. Es enthält keine explizit ausgeschriebene Weil-Testfunktionsformel in der t-Schwartz-/Mellin-Normierung. Insbesondere entscheidet NEU-29 nicht zwischen:

**(A)** Rohes Symbol auf dem hermiteschen Unterraum:

$$
\frac{1}{2\pi}\int_{\mathbb R}\gamma_\infty(t)\,h(t)\,dt,
\qquad h(-t) = \overline{h(t)},
$$

**(B)** Symmetrisiertes Symbol auf geradem reellen Testfunktionsraum:

$$
\frac{1}{2\pi}\int_{\mathbb R}\gamma_\infty^{\mathrm{sym}}(t)\,h(t)\,dt,
\qquad h(-t)=h(t)\in\mathbb R,
$$

mit eventuell angepasstem Integrationsbereich (nur t ≥ 0, mit Halbierungsfaktor) oder weiterhin über ganz ℝ.

### 3.2 Was NEU-36 und NEU-39 festlegen

NEU-36 §5.4 markiert die intrinsische Gamma-Faktor-Realisierung als `❓ [O]`:

> „Der BC-Operator muss entweder den archimedischen Faktor als Zusatzsektor tragen, oder E_N^Γ extern additiv korrigieren."

NEU-39 §10 hält fest:

> „NEU-39 erzeugt nur die endliche nichtarchimedische Euler-Schicht ζ′_N/ζ_N. Die vollständige ξ-Schicht benötigt zusätzlich die archimedischen Gamma-/Polterme. Daher bleibt die intrinsische Gamma-Faktor-Realisierung weiterhin ein eigener offener Punkt."

Damit ist bestätigt: Kein Repository-Text legt bisher fest, ob die Gamma-Distribution in Form (A) oder Form (B) in die vollständige Explizitformel eingeht.

### 3.3 Die Faktor-2-Quelle

Es gibt zwei logisch unabhängige Quellen eines Faktors 2:

| Quelle | Entstehung | Entscheidung |
|---|---|---|
| Konturmaß ds/(2πi) → dt/(2π) | NEU-29 Parametrisierung | ✓ festgelegt |
| Symmetrisierung γ∞ → γ∞^sym = 2 Re γ∞ | Summation t und −t | ?[O] offen |

Diese beiden Faktoren 2 sind strikt auseinanderzuhalten. Der erste ist algebraisch zwingend, der zweite hängt von der Wahl des Testfunktionsraums ab.

### 3.4 Doppelzählungsrisiko

Verwendet man das symmetrisierte Symbol γ∞^sym und integriert weiterhin über ganz ℝ (statt nur über t ≥ 0 mit Faktor ½), wird der Gammaanteil doppelt gezählt. Kein Repository-Text hat diese Konvention bisher explizit fixiert.

**Status Ebene 3:** ?[O] — Restlücke ist ausschließlich die Wahl zwischen (A) und (B), nicht die analytische Existenz der Distribution.

---

## 4. Zusammenfassung des Audit-Ergebnisses

| Ebene | Befund | Status |
|---|---|---|
| ξ-Normalisierung: ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s) | NEU-26, NEU-36 §5.4 | ✓ quellenfest |
| Konturmaß: ds/(2πi) ↦ dt/(2π) via s = ½ + it | NEU-29 §2.1, §3 | ✓ quellenfest |
| Roh (A) vs. Symmetrisiert (B), Integrationsbereich | Kein Repository-Text | ?[O] offen |

### Vorläufiger Auditstatus PD-3d:

$$
\boxed{
\text{PD-3d} \quad \checkmark[M]_{\mathrm{part}}
}
$$

Der Vorfaktor 1/(2π) ist durch NEU-29 zwingend. Die mögliche zusätzliche Symmetrisierung sowie die Halbierungsfrage bleiben zu auditieren, bis eine autoritative Repository-Fassung der vollständigen Weil-Testfunktionsformel in t-Schwartz-/Mellin-Normierung vorliegt.

Die Restlücke ist präzise:

$$
\boxed{
\text{rohes hermitesches Symbol (A) versus explizite Symmetrisierung (B) mit Integrationsbereichsfrage.}
}
$$

---

## 5. Aktualisierter PD-3-Gesamtstatus

$$
\boxed{
\text{PD-3} \quad \checkmark[M]_{\mathrm{part}}
}
$$

| Unterknoten | Aussage | Status |
|---|---|---|
| PD-3a | γ∞(t) = O(log(2+\|t\|)) | ✓[M] |
| PD-3b | T_Γ^raw, T_Γ^sym ∈ S′(ℝ) | ✓[K/M] |
| PD-3c | γ∞(−t) = γ∞(t)̄, Realität auf hermit. Unterraum | ✓[M] |
| PD-3d | Vorfaktor 1/(2π): quellenfest; Roh vs. Sym: offen | ✓[M]_part |

Die verbleibende Restlücke ist ausschließlich arithmetische Weil-Normierung (Testfunktionssymmetrie), nicht analytische Existenz.

---

## 6. Empfohlener nächster Schritt

Um PD-3d vollständig zu schließen (→ ✓[K/M]), muss eine Quelle im Repository — oder ein neuer Knoten NEU-220d — explizit festlegen:

- Ob die vollständige Weil-Explizitformel auf dem hermiteschen Unterraum {h : h(−t) = h(t)̄} oder auf dem geraden reellen Raum {h : h(−t) = h(t)} formuliert ist,
- und ob bei Verwendung von γ∞^sym der Integrationsbereich auf ℝ_{≥0} eingeschränkt (mit Faktor ½) oder auf ganz ℝ beibehalten wird.

Diese Entscheidung hat keine Rückwirkung auf PD-3a–c (analytische Existenz und Stetigkeit sind davon unabhängig).

---

*Datei: `katalog/NEU-220c_Repositoryaudit_Weil-Normierung_und_Gamma-Vorfaktor.md` | 25. Juli 2026*  
*Kernresultat: Vorfaktor 1/(2π) ✓ quellenfest; Roh-vs.-Sym-Entscheidung ?[O]*  
*Quellen: NEU-26, NEU-29, NEU-36, NEU-39 (werkzeuge)*
