# NEU-120 — Bombieri-Normalisierung und Herglotz-Grenzübergang

**Stand:** 1. Juli 2026 | **Patch:** 8. August 2026 (Pass-A Gruppe E, E-6/6) | **Patch 2:** 9. August 2026
**Prüfart:** TARGETED-REAUDIT (mehrere harte Fehler aus Juli-Audit bestätigt; Patch 2: Symmetrie-Normalisierung)
**Vorgänger:** NEU-119 (Patch E-5/6)
**Nächste Nummer:** NEU-121

> **Patch-2-Übersicht:** Externer Gegencheck gegen P07. GM-Skalenbeanstandung verworfen; neuer notwendiger Konvergenztest $a_N\to0$ aus der $\Xi$-Symmetrie bewiesen. Audit: `audits/AUDIT-2026-08-09_P07_Externcheck_GM_aN_Targeted-Reaudit.md`.
>
> **Patch-Übersicht:** Vier harte Fehler gestrichen. Konditionale Grenzrelation (Firewall) bleibt als ?[O].

---

## ~~Annahme NEU-120.A~~ — $\mu_{\Omega,N}(\mathbb{R})=1$ — **×[M]**

> **Audit-Befund:** $\mu_{\rm arith}=\sum_\gamma m_\gamma\delta_\gamma$ hat **unendliche Gesamtmasse**
> (unendlich viele Nullstellen). Daher kann die unskalierte Folge von Wahrscheinlichkeitsmaßen
> **nicht im üblichen schwachen Sinn** gegen $\mu_{\rm arith}$ konvergieren.
> Insbesondere: $w_{j,N}\to 1$ für immer mehr Nullstellen bei $\sum_j w_{j,N}=1$ — unmöglich.

**Status: ×[M]** (gestrichen)

---

## ~~Satz NEU-120.B~~ — Tightness-Bedingung — **×[M]**

> **Audit-Befund:** $\int_{|\lambda|>\Lambda}d\mu_{\Omega,N}\to 0$ für jedes feste $\Lambda$
> passt nicht zu einem Grenzobjekt, dessen Masse sich über unendlich viele Nullstellen erstreckt.

**Status: ×[M]** (gestrichen)

---

## ~~Satz NEU-120.C~~ — Zusätzliche Pole bei $z=\pm i/2$ — **×[M] falsch**

> **Audit-Befund:** $\xi(s)$ ist an $s=0,1$ regulär; diese Punkte sind
> Kompensationspunkte der faktorisierten expliziten Formel, keine Pole von $-\Xi'/\Xi$.
> Unter RH hat $m_{\rm arith}$ Pole **ausschließlich** auf $\mathbb{R}$ (bei den reellen $\gamma$).

**Status: ×[M]** (gestrichen)

---

## ~~Satz NEU-120.D~~ — Momenten-Stieltjes-Entwicklung — **×[M] falsch typisiert**

> **Audit-Befund:** $m_{\rm arith}(z)\sim -1/z+c_0/z^2+\cdots$ als Wahrscheinlichkeits-Stieltjes-Entwicklung
> setzt endliche Gesamtmasse und endliche Momente voraus — beides hat $\mu_{\rm arith}$ nicht.
> Der „Moment-1-Test" $c_0\sim\sum_\gamma 1/\gamma$ ist in dieser Form kein gültiger Kalibrierungstest.

**Status: ×[M]** (gestrichen)

---

## Satz NEU-120.1 (korrigiert) — Konditionale Grenzrelation (Firewall) ?[O]

$$\boxed{m_{\Omega,N}(z)\xrightarrow{N\to\infty}m_{\rm arith}(z)\text{ lok. glm. in }\mathbb{C}^+
\;\Longrightarrow\; m_{\rm arith}\text{ Herglotz}
\;\Longrightarrow\; \text{RH.}}$$

Voraussetzungen (alle offen):
1. $A_N^{\rm Jac,-}$ tatsächlich selbstadjungiert (NEU-119: ?[O])
2. Renormierungen erhalten Herglotz-Eigenschaft (positiv-reell skaliert)
3. Kanonische Wahl von $\Omega_N$ (NEU-119: ?[O])

**Status: ?[O]** (konditionale Firewall)

---

## Satz NEU-120.2 — Korrekter Konvergenzrahmen ?[O]

Für $\mu_{\Omega,N}\to\mu_{\rm arith}$ (unendliche Gesamtmasse) ist der korrekte Rahmen **vague Konvergenz** auf $\mathbb{R}$:
$$\int\phi\,d\mu_{\Omega,N}\to\int\phi\,d\mu_{\rm arith}\quad\text{für alle }\phi\in C_c(\mathbb{R}).$$
Ohne Skalierung kann keine Folge von Wahrscheinlichkeitsmaßen vague gegen $\mu_{\rm arith}$ konvergieren.

**Status: ?[O]** (korrekter Rahmen; Konvergenz offen)

---

## Satz NEU-120.3 — Symmetrie-Normalisierung und notwendiger $a_N$-Test ✓[M]

Mit der kanonischen Definition

$$
\Xi(z)=\xi\!\left(\tfrac12+iz\right),
\qquad
m_{\rm arith}(z)=-\frac{\Xi'(z)}{\Xi(z)}
$$

folgt aus der Funktionalgleichung $\xi(s)=\xi(1-s)$:

$$
\Xi(-z)=\Xi(z),
\qquad
m_{\rm arith}(-z)=-m_{\rm arith}(z).
$$

Zusammen mit der reellen Symmetrie

$$
 m_{\rm arith}(\bar z)=\overline{m_{\rm arith}(z)}
$$

ergibt sich bei $z=i$:

$$
\overline{m_{\rm arith}(i)}
=m_{\rm arith}(-i)
=-m_{\rm arith}(i).
$$

Also ist $m_{\rm arith}(i)$ rein imaginär und damit

$$
\boxed{A=\Re m_{\rm arith}(i)=0.}
$$

Für Nevanlinna-normalisierte Approximanten

$$
\widetilde m_N^{\rm ren}(z)
=a_N+\int_{\mathbb R}
\left(\frac1{t-z}-\frac{t}{1+t^2}\right)d\widetilde\mu_N(t)
$$

gilt bei $z=i$

$$
\frac1{t-i}-\frac{t}{1+t^2}=\frac{i}{1+t^2},
$$

also

$$
\Re\widetilde m_N^{\rm ren}(i)=a_N.
$$

Daher ist

$$
\boxed{
\widetilde m_N^{\rm ren}\xrightarrow{\rm loc.glm.}m_{\rm arith}
\quad\Longrightarrow\quad
a_N\to0.
}
$$

Dies ist keine zusätzliche RH-Annahme, sondern eine notwendige Konsequenz der bereits offenen lokalen gleichmäßigen Konvergenz.

**Status: ✓[M]** (notwendiger Symmetrie-/Normalisierungstest innerhalb der konditionalen Grenzarchitektur)

---

## Status-Übersicht

| Punkt | Inhalt | Status |
|-------|--------|--------|
| 120.A | $\mu_{\Omega,N}(\mathbb{R})=1$ Wahrscheinlichkeitsmaß | ×[M] |
| 120.B | Tightness-Bedingung | ×[M] |
| 120.C | Pole bei $\pm i/2$ | ×[M] |
| 120.D | Momenten-Stieltjes-Entwicklung | ×[M] |
| 120.1 | Konditionale Firewall | ?[O] |
| 120.2 | Vague-Konvergenz Rahmen | ?[O] |
| 120.3 | $A=0$ und lokale gleichmäßige Konvergenz $\Rightarrow a_N\to0$ | ✓[M] |

---

## Verweise

- NEU-119 (Patch E-5/6): Selbstadjungiertheit ?[O]; Spektralmaß-Definition
- NEU-111 (Patch D-1/6), NEU-112 (Patch D-2/6)
- `audits/AUDIT-2026-08-09_P07_Externcheck_GM_aN_Targeted-Reaudit.md`
- **Akhiezer:** *The Classical Moment Problem* (1965)
- **Simon:** *Szegő's Theorem and Its Descendants* (2011)
- **Bombieri:** *Remarks on Weil's quadratic functional* (2000)
