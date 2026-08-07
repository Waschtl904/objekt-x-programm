# NEU-250m — Präquotientaler archimedischer Port auf gemeinsamer adelischer Quelle

**Katalog-ID:** NEU-250m  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (M2-Patch: 2026-08-07)  
**Auftrag:** M1–M4-Meilensteine gegen NEU-245b/c auditieren.  
**Gesamtausgang:** M2 $\checkmark[M]$ (nach Patch); M1 $?[O]$ (NEU-250p); M3/M4 $?[O]$; Formdomäne-Engpass $\to$ NEU-250q.  
**Vorgänger:** NEU-250l (J-B), NEU-245c, NEU-250p

---

## M1 — Gemeinsame adelische Quelle

$$
\mathcal{S}_{\rm adel}:=\mathcal{S}(\mathbb{A}_\mathbb{Q})\quad?[O]\qquad\to\text{NEU-245c, NEU-250p} \qquad (M1)
$$

Korrekte Kette (NEU-250p, 8-a/b/c/d-korr):
$$
\boxed{\mathcal{S}(\mathbb{A}_\mathbb{Q})\xrightarrow{P_{\rm Haar}}\mathcal{S}(\mathbb{R})\xrightarrow{J_{1/2}}\mathcal{S}_\infty.} \qquad (M1\text{-Chain})
$$

---

## M2 — Hermitesche Polarisation (Patch)

### M2.1 Fehler der ersten Fassung

Die erste Fassung setzte
$$
g_{a,b}(t)=\langle a,U_tb\rangle.
$$
Die Diagonale dieser Formel wäre $\langle a,U_ta\rangle$, nicht $\operatorname{Re}\langle a,U_ta\rangle=g_a(t)$. Das ist eine Inkonsistenz.

$$
\boxed{g_{a,b}(t):=\langle a,U_tb\rangle\quad\times[M].} \qquad (M2\text{-Old, zurückgezogen})
$$

### M2.2 Korrekte hermitesche Polarisation

Sei $C_t(a,b):=\int_{\mathbb{R}}a(v)\overline{b(v-t)}\,dv$ die verschobene Kreuzkorrelation. Dann:

$$
\boxed{g_{a,b}(t):=\frac{1}{2}\bigl(C_t(a,b)+C_{-t}(a,b)\bigr)
=\frac{1}{2}\bigl(\langle a,U_tb\rangle+\langle U_ta,b\rangle\bigr).} \qquad (M2\text{-Def})
$$

**Konsistenz auf der Diagonale:**
$$
g_{a,a}(t)=\frac{1}{2}\bigl(\langle a,U_ta\rangle+\langle U_ta,a\rangle\bigr)
=\operatorname{Re}\langle a,U_ta\rangle=g_a(t).\quad\checkmark \qquad (M2\text{-Diag})
$$

**Hermitizität:**
$$
g_{b,a}(t)=\overline{g_{a,b}(t)}.\quad\checkmark \qquad (M2\text{-Herm})
$$

$$
\boxed{g_{a,b}\text{ wie in (M2-Def)}\quad\checkmark[M].} \qquad (M2\text{-Status})
$$

---

## M2.3 Korrekte polarisierte Primform $B_{\rm fin}$ (ersetzt $B_\Lambda$)

Die erste Fassung schrieb
$$
B_\Lambda(a,b)=\sum_{p,k}\frac{\log p}{p^{k/2}}\langle a,U_{k\log p}b\rangle.
$$
Diese Form ist im Allgemeinen nicht hermitesch. Ihre Diagonale reproduziert nicht die in NEU-220l bewiesene Primquadratik.

**Korrekte polarisierte Primform** (aus NEU-220l durch Polarisation mit M2-Def):
$$
\boxed{B_{\rm fin}(a,b):=-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\,g_{a,b}(\log n).} \qquad (M2\text{-Bfin})
$$

Explizit:
$$
\boxed{B_{\rm fin}(a,b)=-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\bigl[\langle a,U_{\log n}b\rangle+\langle U_{\log n}a,b\rangle\bigr].} \qquad (M2\text{-Bfin-Expl})
$$

**Diagonale:** $B_{\rm fin}(a,a)=-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}g_a(\log n)$. Das ist exakt der Primterm in NEU-220l. $\checkmark$

**Hermitizität:** $B_{\rm fin}(b,a)=\overline{B_{\rm fin}(a,b)}$. $\checkmark$

**Sprachliche Klarheit:** Der Faktor $-2$ ist ein globaler Vorfaktor der Weil-Explizitformel (NEU-220l). Der BC/von-Mangoldt-Koeffizient $\Lambda(n)/\sqrt{n}>0$ ist der lokal konstruierte Wert. Beides darf nicht identifiziert werden.

$$
\boxed{B_\Lambda\quad\times[M]\quad\to\quad B_{\rm fin}\quad\checkmark[M].} \qquad (M2\text{-Replace})
$$

---

## M2.4 Domain-Warnung: Divergenz für Gauß-Bilder

Für $F(x_\infty,x_{\rm fin})=e^{-x_\infty^2}\mathbf{1}_{\hat{\mathbb{Z}}}(x_{\rm fin})$ ergibt die Kette $J_{1/2}\circ P_{\rm Haar}$ das Element
$$
a(y)=e^{y/2}e^{-e^{2y}}\in\mathcal{S}_\infty.
$$

Die zugehörige Autokorrelation ist
$$
g_a(\log n)=\frac{\sqrt{\pi}}{2}\frac{n^{-1/2}}{\sqrt{1+n^{-2}}}.
$$

Damit:
$$
B_{\rm fin}(a,a)=-\sqrt{\pi}\sum_{n\ge2}\frac{\Lambda(n)}{n\sqrt{1+n^{-2}}}\sim-\sqrt{\pi}\sum_n\frac{\Lambda(n)}{n}\quad\text{(divergent).}
$$

$$
\boxed{J_{1/2}P_{\rm Haar}F\in\mathcal{S}_\infty\text{ liegt nicht im Definitionsbereich von }B_{\rm fin}.}
\qquad (M2\text{-DomainNoGo})$$

Formdomänen-Entscheidung (Q-A/B/C): $\to$ **NEU-250q**.

---

## M3/M4 — Status

$$
\text{M3 (Gram-Geometrie), M4 (Positiver Kern)}\quad?[O]\quad\to\text{nach NEU-250q.} \qquad (M3/M4)
$$

---

## Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-250l | 27894d5 | J-B-Entscheidung |
| NEU-250p | 56ba1f7 | $J_{1/2}$-Kette $\checkmark[K/M]$; Weil-Selbstdualität |
| NEU-220l | 1dc07b3 | Weil-Quadratik, Primterm, $-2$-Vorfaktor |
| NEU-220a | 653c8a9 | $\mathcal{M}_\infty$, $\mathcal{S}_\infty$ |
| NEU-250q | neu | Formdomäne-Audit, Q-A/B/C-Entscheidung |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. M2-Patch 2026-08-07: $g_{a,b}$ hermitesch korrigiert; $B_\Lambda\to B_{\rm fin}$; Domain-Warnung eingetragen.*
