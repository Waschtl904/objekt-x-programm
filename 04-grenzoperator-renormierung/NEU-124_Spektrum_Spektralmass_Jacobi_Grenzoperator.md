# NEU-124 — Spektrum und Spektralmaß des Jacobi-Grenzoperators

**Datum:** 4. Juli 2026
**Anschluss:** NEU-123
**Status:** 🔒 GESPERRTES PLATZHALTERBLATT

> Dieses Blatt wird erst aktiv, wenn NEU-123 Stufe 1 und Stufe 2 bestanden sind.
> Alle Aussagen in NEU-124 sind bis dahin formal offen und dürfen nicht
> zur Begründung von NEU-123 verwendet werden.

---

## 124.0 — Eintrittsbedingung

Dieses Blatt wird erst aktiv, wenn NEU-123 folgende Punkte liefert:

$$a_{j,N} \to a_j, \qquad b_{j,N} \to b_j > 0 \quad\text{für jedes feste }j,$$

sowie einen kanonischen selbstadjungierten Grenzoperator $A_\infty$.

Idealerweise zusätzlich:

$$A_N^{\mathrm{Jac},-} \;\xrightarrow{\mathrm{s.r.}}\; A_\infty.$$

Solange diese Bedingungen nicht erfüllt sind, sind alle Aussagen in NEU-124 bedeutungslos. ?[O]

---

## 124.1 — Erste Zielaussage: Spektrum

Zu prüfen (erst nach Aktivierung):

$$\sigma(A_\infty) \;\stackrel{?}{=}\; \{\operatorname{Im}\rho : \xi(\rho) = 0\}.$$

Diese Aussage betrifft nur die **Ordinatenmenge** der Zeta-Nullstellen.
Sie impliziert für sich allein **nicht** RH (vgl. NEU-122.S.1 und NEU-123.6).

Status: ?[O]

---

## 124.2 — Zweite Zielaussage: Punktspektrum und Einfachheit

Zu prüfen, ob $A_\infty$ reines Punktspektrum besitzt und ob die Eigenwerte einfach sind:

$$\sigma(A_\infty) = \sigma_p(A_\infty) = \{\lambda_1, \lambda_2, \ldots\}, \qquad \lambda_k \;\stackrel{?}{=}\; \gamma_k,$$

wobei $\gamma_k = \operatorname{Im}\rho_k$ unter RH die Ordinaten der nichttrivialen Nullstellen $\rho_k = \tfrac{1}{2} + i\gamma_k$ sind.

**Ohne RH** darf $\lambda_k \stackrel{?}{=} \gamma_k$ nur als Ordinatenvergleich gelesen werden, nicht als Aussage über Realteile.

Zusatzbedingungen (vgl. NEU-123.6):
- Kein kontinuierliches Spektrum.
- Keine Spektralmasse geht im Limes $N \to \infty$ verloren.
- Eigenprojektionen von $A_N^{\mathrm{Jac},-}$ approximieren die von $A_\infty$.

Status: ?[O]

---

## 124.3 — Dritte Zielaussage: Spektralmaß

Die RH-relevante und logisch stärkste Frage:

$$\mu_{\Omega_\infty}^{A_\infty} \;\stackrel{?}{=}\; \mu_\xi.$$

Die Weyl-Funktion ist durch das Spektralmaß vollständig bestimmt:

$$m_{\Omega_\infty}(z) = \int_{\mathbb{R}} \frac{d\mu_{\Omega_\infty}^{A_\infty}(t)}{t - z}.$$

Zwei Maße können denselben Träger $\{\gamma_k\}$ haben und dennoch verschiedene Weyl-Funktionen erzeugen.
Daher reicht 124.1 allein nicht. Erst die Maßidentifikation liefert:

$$m_{\Omega_\infty}(z) = m_{\mathrm{arith}}(z).$$

Status: ?[O]

---

## 124.4 — Anschluss an NEU-120.W (Zielkette)

Falls 124.3 bestanden ist, schließt sich die vollständige Argumentationskette:

$$\boxed{A_N^{\mathrm{Jac},-} \xrightarrow{\mathrm{s.r.}} A_\infty}
\;\Longrightarrow\;
\mu_{\Omega_\infty}^{A_\infty} = \mu_\xi
\;\Longrightarrow\;
m_{\Omega_\infty} = m_{\mathrm{arith}}
\;\Longrightarrow\;
m_{\mathrm{arith}}\text{ ist Herglotz}
\;\Longleftrightarrow\;
\mathrm{RH}.$$

Der letzte Schritt ist NEU-120.W (WARNSATZ) kombiniert mit NEU-63D. ⚠[M]

Die Kette ist **logisch klar**, aber jeder Pfeil ist ein offenes Problem:

| Pfeil | Status |
|-------|--------|
| $A_N \xrightarrow{\mathrm{s.r.}} A_\infty$ | ?[O] (NEU-123) |
| $\mu_{\Omega_\infty}^{A_\infty} = \mu_\xi$ | ?[O] (NEU-124.3) |
| $m_{\Omega_\infty} = m_{\mathrm{arith}}$ | ?[O] (NEU-124.3) |
| $m_{\mathrm{arith}}$ Herglotz $\Leftrightarrow$ RH | ✓[M] (NEU-63D, NEU-120.W) |

---

## 124.S — Sperrvermerk (methodisch bindend)

**NEU-124 darf nicht zur Begründung von NEU-123 verwendet werden.**

Die logische Richtung ist ausschließlich:

$$\mathrm{NEU\text{-}123} \;\Longrightarrow\; \mathrm{NEU\text{-}124}.$$

Insbesondere dürfen:
- Zeta-Ordinaten $\gamma_k$,
- Hadamard-Gewichte,
- Bombieri-Gewichte,
- die Konstante $C_\xi$,

**nicht rückwirkend** zur Wahl der Jacobi-Koeffizienten $a_j, b_j$ oder des Vektors $\Omega_\infty$ verwendet werden.

Verletzung dieses Sperrvermerks fällt unter das Anti-Fitting-Axiom (NEU-122.0) und entleert den Beweis.

✓[M] als methodische Sperre

---

## 124.N — Nächste Aufgabe

Vor inhaltlicher Bearbeitung von NEU-124 ist **NEU-123 Stufe 1** auszuführen:

$$\boxed{\text{Extrahiere }a_{j,N},\,b_{j,N}\text{ aus NEU-77–87 und prüfe Stabilisierung für feste }j.}$$

Erst wenn Stufe 1 und Stufe 2 (Carleman) von NEU-123 bestanden sind, wird dieses Blatt von einem Platzhalter zu einem aktiven Prüfblatt.

---

## Querverweise

- NEU-63D: RH $\Leftrightarrow$ $m_{\mathrm{arith}}$ Herglotz ✓[M]
- NEU-77–87: Feshbach-Kollaps $\to$ $A_N^{\mathrm{Jac},-}$ ✓[M]
- NEU-120: WARNSATZ ⚠[M]
- NEU-122: Anti-Fitting-Axiom, Eintrittsbedingungen P1/P2/P3 ?[O]
- NEU-123: Jacobi-Grenzoperator, starke Resolventenkonvergenz ?[O]

---

*Katalog: rh-fragenkatalog | Einheit: NEU-124 | Status: Platzhalter gesperrt | Erstellt: 2026-07-04*
