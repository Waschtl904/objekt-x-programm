# NEU-107 — Lokale Formfaktor-Annahme und Rampen-Äquivalenz

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-106 (No-Go punktweise Nullstellenformel; \(\mathcal{E}_{N,H}\) Träger; RH \(\not\Rightarrow\) GUE-Rampe)  
**Nächste Nummer:** NEU-108

---

## Ausgangspunkt

NEU-106 zeigt: Der Rampen-Test benötigt eine Paarstatistik-Annahme, die über RH allein hinausgeht. NEU-107 isoliert die minimal nötige Annahme präzise und bestimmt ihre Stärke.

**Leitprinzip:** Die Annahme wird nicht als neue Vermutung formuliert, sondern als **Äquivalenzkalibrierung** des Rampen-Tests.

---

## Definition NEU-107.1 — Lokale Formfaktor-Annahme \(\mathrm{LFF}_{N,H}(A)\)

Für festes \(0 < A \leq 1\) und jede kompakt getragene Testfunktion \(\Phi \subset (-A, A)\) gelte nach korrekter Entfaltung (NEU-103):

$$
\boxed{
\mathrm{LFF}_{N,H}(A):\quad
\int_{-A}^{A}\Phi(\alpha)\,\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)\,d\alpha
\sim c_{N,H}\int_{-A}^{A}\Phi(\alpha)\,|\alpha|\,d\alpha
}
$$

für eine von \(\Phi\) unabhängige Normierungskonstante \(c_{N,H} > 0\).

**Status: Definition** (Annahme; zu prüfen in NEU-108+)

---

## Satz NEU-107.2 — Rampen-Äquivalenz

Unter \(\mathrm{LFF}_{N,H}(A)\) gilt:

$$
R_{N,H,A}(\varepsilon)
= \frac{\int_{-\varepsilon}^{\varepsilon}\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)\,d\alpha}{\int_{-A}^{A}\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)\,d\alpha}
\sim
\frac{\int_{-\varepsilon}^{\varepsilon}|\alpha|\,d\alpha}{\int_{-A}^{A}|\alpha|\,d\alpha}
= \frac{\varepsilon^2}{A^2}.
$$

Der Rampen-Test von NEU-105 ist also zur lokalen Formfaktor-Annahme äquivalent:

$$
\mathrm{LFF}_{N,H}(A) \;\Longleftrightarrow\; R_{N,H,A}(\varepsilon) \sim \varepsilon^2/A^2.
$$

**Status: \(\checkmark[M]\)** (Kalibrierung)

---

## Satz NEU-107.3 — Stärke-Hierarchie

$$
\boxed{
\mathrm{RH}
\;<\;
\text{Varianzskala}\,(\mathrm{NEU}\text{-}101)
\;<\;
\mathrm{LFF}_{N,H}(A)
\;<\;
\text{volle Montgomery/GUE-Paarstatistik}.
}
$$

Präzise:

| Annahme | Was sie liefert | Stärke |
|---|---|---|
| RH | Nullstellenlage \(\mathrm{Re}(\rho)=1/2\) | Basis |
| Goldston\u2013Montgomery Varianzskala | skalares zweites Moment \(\mathcal{V}(M,H)\) | \(>\) RH |
| \(\mathrm{LFF}_{N,H}(A)\) | lokales Spektralprofil bei \(\alpha=0\) | \(>\) Varianzskala |
| volle Montgomery/GUE | globale Paarabstandsdichte \(1-(\mathrm{sinc}\,\pi u)^2\) | Maximum |

**Begründung für \(\mathrm{LFF} <\) volle Montgomery:** LFF testet nur lokal bei \(\alpha = 0\) und nur im spezifischen Restkanal nach Entfaltung \(\alpha = \tau T \rho_T\). Die volle Vermutung beschreibt das globale Paarprofil für alle \(u\).

**Begründung für \(\mathrm{LFF} >\) Varianzskala:** Varianzskala = Gesamtmasse des zweiten Moments. LFF fordert zusätzlich das lokale Spektralprofil (Rampe, nicht Plateau).

**Status: \(\checkmark[M]\)**

---

## Satz NEU-107.4 — Implikation

$$
\text{explizite Formel} + \mathrm{LFF}_{N,H}(A)
\;\Longrightarrow\;
\text{NEU-105-Rampe}.
$$

Ohne \(\mathrm{LFF}_{N,H}(A)\) kann die korrekte Varianzskala durch ein Poisson-artiges Plateau entstehen und wäre dann kein Weil-Signal.

**Status: \(\checkmark[M]\)**

---

## Satz NEU-107.5 — Goldston\u2013Montgomery-Kanal

Die blosse Goldston\u2013Montgomery-Varianzskala enthält \(\mathrm{LFF}_{N,H}(A)\) **nicht automatisch**. LFF ist im Transfer enthalten nur, wenn man die **starke Paarkorrelationsvermutung** (nicht nur die Varianzformel) mitnimmt.

Goldston\u2013Montgomery zeigen unter RH:
$$
\text{starke Paarkorrelationsvermutung}
\;\Longleftrightarrow\;
\mathcal{V}(M,H) \sim \frac{H}{M}\log\frac{M}{H}.
$$

Diese Äquivalenz deutet an, dass der Goldston\u2013Montgomery-Kanal für das lokale Profil relevant ist, sobald man die volle Paarkorrelationsstruktur mitnimmt — aber die Varianzformel allein reicht nicht.

**Status: \(\warning[M]\)**

---

## Neue Leitfrage für NEU-108

$$
\boxed{\text{Genügt }\mathrm{LFF}_{N,H}(A)\text{, um eine positive Weil-artige Testform zu erzeugen?}}
$$

Konkrete Schritte:
1. Aus \(\int \Phi(\alpha)\,\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)\,d\alpha \sim c \int \Phi(\alpha)|\alpha|\,d\alpha\): Ist die Abbildung \(\Phi \mapsto c\int\Phi(\alpha)|\alpha|\,d\alpha\) eine positive Weil-Form?
2. Vergleich: \(\int|\alpha|\,d\alpha\) hat die Gestalt \(Q(f,f)\) mit \(f\) Fourier-Transformätes von \(\Phi\)?
3. Anschluss an Connes\u2013Weil: \(Q_{\mathrm{Weil}}(f,f) = \sum_\rho \hat{f}(\rho) + \ldots\) für geeignetes \(f\)?

Ausblick:
$$
\Delta_N \to \mathcal{P}^{\mathrm{unf}}_{N,H} \to K_{\mathrm{GUE}} \to \text{Weil-kompatible positive Spektralform}.
$$

---

## Tabellarische Statusklassifikation

| Satz | Inhalt | Status |
|------|--------|--------|
| 107.1 | \(\mathrm{LFF}_{N,H}(A)\) Definition | Def. |
| 107.2 | Rampen-Äquivalenz \(\mathrm{LFF} \Leftrightarrow R \sim \varepsilon^2/A^2\) | \(\checkmark[M]\) |
| 107.3 | Stärke-Hierarchie RH \(<\) Var \(<\) LFF \(<\) Montgomery | \(\checkmark[M]\) |
| 107.4 | expl.\(+\)LFF \(\Rightarrow\) Rampe | \(\checkmark[M]\) |
| 107.5 | G.-M. Varianzskala enthält LFF nicht automatisch | \(\warning[M]\) |

---

## Verweise

- NEU-106: No-Go punktweise; epistemisch RH \(\not\Rightarrow\) GUE
- NEU-105: Binärer Rampen-Test \(R \sim \varepsilon^2/A^2\)
- NEU-104: \(\mathcal{P}^{\mathrm{unf}}_{N,H}\) und No-Go global
- **Goldston & Montgomery:** *Pair correlation, primes in short intervals* (1987)
- **Chan:** *Short intervals* (2003) (starke Paarkorrelation fast äquivalent)
- Connes: *Trace formula* (1999) (spätere Weil-Schnittstelle)
- Keating & Snaith: *Random matrix theory and \(L\)-functions* (2000)
