# NEU-103 — Entfaltungskarte aus der expliziten-Formel-Phase

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-102 (No-Go direkter \(r(u)\)-Vergleich; Entfaltungskarte \(\alpha_N(\tau)\) als offener Schritt)  
**Nächste Nummer:** NEU-104

---

## Ausgangspunkt

NEU-102 stellt fest: Die Entfaltungskarte \(\tau \mapsto \alpha_N(\tau)\) darf nicht aus Dimensionsgefühl gewählt werden. NEU-103 leitet sie aus dem Phasenvergleich der expliziten Formel her.

**Korrektur gegenüber NEU-102:** Der naive Ansatz \(\alpha_N(\tau) = \tau / \rho_M\) mit \(\rho_M = \log M / 2\pi\) ist falsch, weil \(\tau\) dual zu \(h/H\), nicht zu \(h/M\) ist.

---

## Satz NEU-103.1 — Phasenvergleich

Die geglättete Shift-Transformierte ist (in \(H\)-normierter Konvention):

$$
\mathcal{E}_{N,H}(\tau) = \sum_h \omega(h/H)\,\Delta_N(h)\,e^{-i\tau h/H}.
$$

Die Variable \(\tau\) ist dual zur **normalisierten** Shift-Variable \(h/H\).

Nullstellenbeiträge aus der expliziten Formel oszillieren für kurze Shifts \(h \ll M\) mit Phasen:

$$
e^{i\gamma h/M}.
$$

Phasenvergleich:

$$
\frac{\tau h}{H} \approx \frac{\gamma h}{M}
\quad\Longrightarrow\quad
\gamma \approx \tau \cdot \frac{M}{H} = \tau T,
\qquad T = \frac{M}{H}.
$$

$$
\boxed{\gamma \sim \tau T, \qquad T = M/H.}
$$

Die Variable \(\tau\) ist also **Nullstellenhöhe geteilt durch** \(T\), nicht die Höhe selbst.

**Status: \(\checkmark[M]\)**

---

## Satz NEU-103.2 — Relevante Nullstellendichte

Der relevante Höhenschnitt der Nullstellen ist \(T = M/H\), nicht \(M\). Die lokale Nullstellendichte bei Höhe \(T\) ist:

$$
\rho_T = \frac{\log T}{2\pi}.
$$

$$
\boxed{\rho_T = \frac{\log T}{2\pi} \text{ ist die relevante Dichte, nicht } \rho_M = \frac{\log M}{2\pi}.}
$$

Der Unterschied ist konzeptionell wichtig: \(\rho_M\) und \(\rho_T\) stimmen nur im Grobregime \(H = O(1)\) überein.

An der **selbstdualen Skala** \(H = T = \sqrt{M}\):

$$
\rho_T = \frac{\log \sqrt{M}}{2\pi} = \frac{\log M}{4\pi} = \frac{1}{2}\rho_M.
$$

Faktor \(1/2\) gegenüber der naiven Wahl.

**Status: \(\checkmark[M]\)**

---

## Definition NEU-103.3 — Zwei äquivalente Konventionen

**Konvention A** (\(H\)-normiert, Fensteranalyse-näher):

$$
\mathcal{E}_{N,H}(\tau) = \sum_h \omega(h/H)\,\Delta_N(h)\,e^{-i\tau h/H}.
$$

Entfaltete Abstandsskala:

$$
u_N(\tau) = \tau T \rho_T = \tau T \cdot \frac{\log T}{2\pi}.
$$

**Konvention B** (\(M\)-normiert, explizite-Formel-näher):

$$
\mathcal{F}_{N,H}(\sigma) = \sum_h \omega(h/H)\,\Delta_N(h)\,e^{-i\sigma h/M}.
$$

Entfaltete Abstandsskala:

$$
u_N(\sigma) = \sigma \rho_T = \sigma \cdot \frac{\log T}{2\pi}.
$$

Äquivalenz: \(\sigma = \tau T\).

| Konvention | Variable | Nullstellenhöhe | Entfaltung |
|---|---|---|---|
| A (\(H\)-normiert) | \(\tau\) | \(\gamma \sim \tau T\) | \(u = \tau T \rho_T\) |
| B (\(M\)-normiert) | \(\sigma = \tau T\) | \(\gamma \sim \sigma\) | \(u = \sigma \rho_T\) |

**Status: \(\checkmark[M]\)** (beide äquivalent)

---

## Definition NEU-103.4 — Entfaltete Profildichte

Die korrekte entfaltete spektrale Profildichte (in Konvention A) ist:

$$
\mathcal{S}^{\mathrm{unf}}_{N,H}(\alpha)
:= \mathcal{S}_{N,H}\!\left(\frac{\alpha}{T\rho_T}\right) \cdot \frac{1}{T\rho_T},
$$

wobei \(\alpha = \tau T \rho_T\) der normierte Nullstellen-Abstand ist.

$$
\boxed{\mathcal{S}^{\mathrm{unf}}_{N,H}(\alpha) \text{ wird durch } \alpha = \tau T \frac{\log T}{2\pi} \text{ definiert.}}
$$

Der No-Go-Vergleich \(\mathcal{S}_{N,H}(\rho_M \alpha) \to K(\alpha)\) (mit \(\rho_M = \log M/2\pi\)) ist falsch; der korrekte Test lautet:

$$
\mathcal{S}^{\mathrm{unf}}_{N,H}(\alpha) \;\stackrel{?}{\longrightarrow}\; K(\alpha).
$$

**Status: \(\checkmark[M]\)** (Definition; Test offen)

---

## Testwert an der selbstdualen Skala

Für \(H = T = \sqrt{M}\):

$$
u_N(\tau) = \tau \sqrt{M} \cdot \frac{\log M}{4\pi}.
$$

D.h. ein entfalteter Abstand \(\alpha = 1\) entspricht \(\tau = 4\pi / (\sqrt{M} \log M)\) in Konvention A.

---

## Neue Leitfrage für NEU-104

$$
\boxed{\mathcal{S}^{\mathrm{unf}}_{N,H}(\alpha) \stackrel{?}{\to} K(\alpha) = |\alpha| \cdot \mathbf{1}_{|\alpha|\leq 1} + \mathbf{1}_{|\alpha|>1}.}
$$

Konkrete Schritte:
1. Ist \(\mathcal{S}^{\mathrm{unf}}_{N,H}\) nach der Jacobi-/Feshbach-Kette aus NEU-77\u201387 in eine Spur-Formel einbettbar?
2. GUE-Statistik oder Poisson-Statistik in \(\mathcal{S}^{\mathrm{unf}}\)?
3. Unter welchen Bedingungen konvergiert \(\mathcal{S}^{\mathrm{unf}} \to K\)?

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | Phasenvergleich: \(\gamma \sim \tau T\) | \(\checkmark[M]\) |
| (B) | \(\rho_T = \log T / 2\pi\) relevant (nicht \(\rho_M\)) | \(\checkmark[M]\) |
| (C) | Selbstdual: \(\rho_T = \frac{1}{2}\rho_M\) | \(\checkmark[M]\) |
| (D) | Zwei Konventionen A/B; \(\sigma = \tau T\) | \(\checkmark[M]\) |
| (E) | \(\mathcal{S}^{\mathrm{unf}}_{N,H}(\alpha)\) entfaltete Profildichte | \(\checkmark[M]\) (Def.) |
| (F) | Formfaktor-Test \(\mathcal{S}^{\mathrm{unf}} \to K(\alpha)\) | \(?[O]\) |

---

## Verweise

- NEU-102: No-Go direkter \(r(u)\)-Vergleich; GUE-Formfaktor \(K(\alpha)\)
- NEU-100: \(\mathcal{E}_{N,H}(\tau)\) Definition
- NEU-97: Skalenleiter \(T = M^\theta\)
- Montgomery: *Pair correlation of zeros* (1973) (Formfaktor \(K(\alpha)\))
- Goldston & Montgomery: *Pair correlation, primes in short intervals* (1987)
- Keating & Snaith: *Random matrix theory and \(L\)-functions* (2000) (GUE-Formfaktor)
- Bogomolny & Keating: *Gutzwiller's trace formula* (Spur-Formel-Anschluss)
