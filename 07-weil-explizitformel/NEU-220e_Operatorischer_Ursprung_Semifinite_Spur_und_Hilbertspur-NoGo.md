# NEU-220e — PD-4: Operatorischer Ursprung von Λ_Γ; gewöhnliche Spur, semifinite Spur, intrinsischer Gamma-Ursprung

**Knoten:** `[O-220-1-PD4-operator-origin]`  
**Stand:** 25. Juli 2026  
**Vorgänger:** NEU-220d rev.2 (PD-3d ✓[K/M], PD-3 ✓[K/M])  
**Ziel:** Operatorischen Ursprung der fixierten Rohform

$$
\Lambda_\Gamma(h) = \frac1{2\pi}\int_{\mathbb R}\gamma_\infty(t)h(t)\,dt
$$

auditieren.

Atomare Unterknoten:
- **PD-4a** — Gewöhnliche Hilbertraumspur scheitert ✓[M]_neg
- **PD-4b** — Semifinite Spur realisiert $\Lambda_\Gamma$ ✓[K/M]
- **PD-4c** — Intrinsischer Gamma-Ursprung (relative/streutheoretische Konstruktion) ?[O]

---

## 0. Ausgangspunkt

NEU-220d rev.2 hat festgelegt:

$$
\Lambda_\Gamma(h) = \frac1{2\pi}\int_{\mathbb R}\gamma_\infty(t)h(t)\,dt,
\qquad h\in\mathcal{S}_\mathrm{herm}(\mathbb R),
$$

als autoritative Gamma-Rohform. PD-4 fragt: Als was für eine Spur eines Operators lässt sich $\Lambda_\Gamma$ realisieren?

Der freie Skalierungsgenerator $H_\infty=-ix\frac{d}{dx}$ wird unter $\mathcal{M}_\infty$ zu $M_t$ (Multiplikation mit $t$) auf $L^2(\mathbb R,dt)$. Er erzeugt nicht von selbst das Symbol $\gamma_\infty(t)$. Daher ist ein zusätzlicher Funktionalkalkül oder eine relative Konstruktion nötig.

---

## 1. PD-4a — Gewöhnliche Hilbertraumspur scheitert ✓[M]_neg

**Kandidat:**

$$
\Lambda_\Gamma(h) \stackrel{?}{=} \operatorname{Tr}_{B(L^2)}\bigl(\gamma_\infty(H_\infty)h(H_\infty)\bigr).
$$

**Satz PD-4a (No-Go):**

$$
\boxed{
\operatorname{Tr}_{B(L^2)}\bigl(\gamma_\infty(H_\infty)h(H_\infty)\bigr)
\text{ existiert im Allgemeinen nicht.}
}
$$

**Beweis.** Unter $\mathcal{M}_\infty: L^2(\mathbb R^\times,\frac{dx}x)\to L^2(\mathbb R,dt)$ gilt:

$$
\gamma_\infty(H_\infty)h(H_\infty) = M_{\gamma_\infty h}.
$$

Für $h\in\mathcal{S}(\mathbb R)$ gilt $\gamma_\infty h\in L^1(\mathbb R)\cap L^\infty(\mathbb R)$ wegen des logarithmischen Wachstums von $\gamma_\infty$ und der Schwartz-Abnahme von $h$. Jedoch: $M_{\gamma_\infty h}$ ist ein Multiplikationsoperator auf dem nichtatomaren Maßraum $(\mathbb R,dt)$. Ein Multiplikationsoperator $M_a$ mit $a\not\equiv 0$ auf $L^2(\mathbb R,dt)$ ist nicht kompakt — insbesondere nicht spurklassig. Die gewöhnliche Hilbert-Spur

$$
\operatorname{Tr}_{B(L^2)}(M_a) = \int_\mathbb R a(t)\,\|\delta_t\|^2\,dt
$$

ist für $L^2(\mathbb R,dt)$ nicht definiert, da es keine $L^2$-Dirac-Deltafunktionen gibt ($\delta_t\notin L^2$). $\square$

$$
\boxed{[O\text{-}220\text{-}1\text{-PD4a-ordinary-trace}]\quad\checkmark[M]_\mathrm{neg}.}
$$

**Kommentar:** Dieses No-Go ist strukturell, nicht perturbativ. Es gilt unabhängig davon, wie schnell $h$ abfällt, solange $\gamma_\infty h$ nicht identisch verschwindet.

---

## 2. PD-4b — Semifinite Spur realisiert $\Lambda_\Gamma$ ✓[K/M]

**Setup.** Sei

$$
\mathcal{N}_\infty := L^\infty(\mathbb R,dt)
$$

als kommutative Von-Neumann-Algebra von Multiplikationsoperatoren auf $L^2(\mathbb R,dt)$. Sie trägt die kanonische normale treue semifinite (n.f.s.) Spur

$$
\tau_\infty(M_a) := \int_{\mathbb R} a(t)\,dt, \qquad a\geq 0.
$$

Der $\tau_\infty$-$L^1$-Raum ist

$$
L^1(\mathcal{N}_\infty,\tau_\infty) = \{M_a : a\in L^1(\mathbb R,dt)\},
$$

und $\tau_\infty$ setzt sich linear fort auf diesen Raum.

**Satz PD-4b (Semifinite Realisierung):**

$$
\boxed{
\gamma_\infty(H_\infty)h(H_\infty) = M_{\gamma_\infty h} \in L^1(\mathcal{N}_\infty,\tau_\infty)
\quad\text{für }h\in\mathcal{S}_\mathrm{herm}(\mathbb R),
}
$$

und

$$
\boxed{
\Lambda_\Gamma(h) = \frac1{2\pi}\,\tau_\infty\bigl(\gamma_\infty(H_\infty)h(H_\infty)\bigr).
}
$$

**Beweis.** Für $h\in\mathcal{S}(\mathbb R)$ gilt $\gamma_\infty h\in L^1(\mathbb R,dt)$: Das Produkt aus logarithmischem Wachstum $\gamma_\infty(t)=O(\log|t|)$ und Schwartz-Abnahme $h(t)=O(|t|^{-N})$ für alle $N$ liegt in $L^1$. Also $M_{\gamma_\infty h}\in L^1(\mathcal{N}_\infty,\tau_\infty)$. Dann:

$$
\frac1{2\pi}\tau_\infty(M_{\gamma_\infty h})
= \frac1{2\pi}\int_{\mathbb R}(\gamma_\infty h)(t)\,dt
= \Lambda_\Gamma(h). \quad\square
$$

**Typisierung:** Die Abbildung

$$
\mathcal{S}_\mathrm{herm}(\mathbb R) \longrightarrow L^1(\mathcal{N}_\infty,\tau_\infty) \xrightarrow{\frac1{2\pi}\tau_\infty} \mathbb R
$$

ist eine typkorrekte operatoralgebraische Realisierung von $\Lambda_\Gamma$.

$$
\boxed{[O\text{-}220\text{-}1\text{-PD4b-semifinite-trace}]\quad\checkmark[K/M].}
$$

**Einschränkung:** Diese Realisierung setzt $\gamma_\infty$ mittels Funktionalkalkül ein — sie erklärt noch nicht, warum die Digammafunktion aus einer geometrischen oder streutheoretischen Konstruktion emergiert.

---

## 3. PD-4c — Intrinsischer Gamma-Ursprung ?[O]

**Offene Frage:** Gibt es eine streutheoretische oder relative Determinantenkonstruktion, die $\gamma_\infty^\mathrm{sym}$ ohne manuellen Funktionalkalkül erzeugt?

**Formales Ziel:** Finde einen Operator $T_\infty$ (relativ, streuend, Birman-Schwinger) mit

$$
\partial_t\log S_\infty(t) \sim \gamma_\infty^\mathrm{sym}(t),
$$

sodass

$$
\Lambda_\Gamma(h) = \frac1{2\pi}\int_{\mathbb R}(\partial_t\log S_\infty)(t)\cdot h(t)\,dt
$$

als Spektralverschiebungs- oder Kreimer-Streuphase-Form entsteht.

**Motivation aus dem Repository:** NEU-47 platziert $D_\infty$ als archimedische Komponente eines vollständigen Feshbach-Schur-Operators. Die BC-Geometrie trennt $D_\mathrm{Arch}$ (Gamma/Pol) von $D_\mathrm{scatt}$ (Nullstellen). Analog sollte auf archimedischer Seite ein relativer Operator existieren, dessen Streuphase $\gamma_\infty^\mathrm{sym}$ reproduziert.

**Kandidaten für spätere Untersuchung:**

| Ansatz | Idee | Vorläufiger Status |
|---|---|---|
| $\gamma_\infty^\mathrm{sym}(H_\infty)$ via Funktionalkalkül | $\tau_\infty(\gamma_\infty^\mathrm{sym}(H_\infty)h(H_\infty))$ | ✓ als Tautologie; kein intrinsischer Ursprung |
| Relativer Resolventen-/Birman-Schwinger-Operator $K_\infty$ | $\partial_t\log\det(1+K_\infty(t))=\gamma_\infty^\mathrm{sym}(t)$ | ?[O] |
| Streuphase $S_\infty$ eines archimedischen freien/gestörten Paars | $-i\partial_t\log S_\infty(t)=\gamma_\infty^\mathrm{sym}(t)$ | ?[O] |
| Relative Spurformel aus $D_\mathrm{Arch}/D_\mathrm{free}$ | Direkter Quotient zweier Zeta-/Determinantenfunktionen | ?[O] |

$$
\boxed{[O\text{-}220\text{-}1\text{-PD4c-intrinsic-relative-origin}]\quad?[O].}
$$

---

## 4. Statusmatrix PD-4

| Knoten | Aussage | Status |
|---|---|---|
| PD-4a | $\operatorname{Tr}_{B(L^2)}(\gamma_\infty(H_\infty)h(H_\infty))$ existiert nicht | ✓[M]_neg |
| PD-4b | $\Lambda_\Gamma(h)=\frac1{2\pi}\tau_\infty(M_{\gamma_\infty h})$, $\tau_\infty$ n.f.s. auf $L^\infty$ | ✓[K/M] |
| PD-4c | Intrinsischer $\gamma_\infty$-Ursprung via relative/Streu-Konstruktion | ?[O] |
| Pol-Funktional | $\Lambda_\mathrm{pole}^\mathrm{raw}$ in vollständiger Weil-Form | ?[O] (aus PD-3d4) |

$$
\boxed{\text{PD-4}\quad\checkmark[K/M]_{\mathrm{part}}.}
$$

PD-4 ist durch PD-4b mit einem typkorrekten operatoralgebraischen Befund teilweise geschlossen. PD-4c bleibt der konzeptionell tiefere offene Knoten.

---

## 5. Übergabe an PD-5

PD-5 kann beginnen, sobald PD-4c einen ersten positiven Kandidaten hat. Bis dahin ist PD-5 gesperrt.

Die vollständige archimedische Zielfunktion:

$$
\Lambda_\mathrm{Arch}(h)
= \underbrace{\frac1{2\pi}\int_{\mathbb R}p_\infty^\mathrm{raw}(t)h(t)\,dt}_{\Lambda_\mathrm{pole}^\mathrm{raw}}
+ \underbrace{\frac1{2\pi}\tau_\infty(M_{\gamma_\infty h})}_{\Lambda_\Gamma}.
$$

---

*Datei: `katalog/NEU-220e_Operatorischer_Ursprung_Semifinite_Spur_und_Hilbertspur-NoGo.md` | 25. Juli 2026*  
*Kernresultat: PD-4a ✓[M]_neg, PD-4b ✓[K/M], PD-4c ?[O]*  
*Quellen: NEU-220d rev.2, NEU-47*
