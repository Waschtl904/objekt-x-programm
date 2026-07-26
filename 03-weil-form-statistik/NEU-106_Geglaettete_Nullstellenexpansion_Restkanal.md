# NEU-106 — Geglättete Nullstellenexpansion des Restkanals

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-105 (Binärer Rampen-Test; \(R \sim \varepsilon/A\) Poisson vs.\ \(R \sim \varepsilon^2/A^2\) GUE)  
**Nächste Nummer:** NEU-107

---

## Ausgangspunkt

NEU-105 zeigt: Der Entscheidungstest ist die lokale Paarstruktur von \(\mathcal{P}^{\mathrm{unf}}_{N,H}\) nahe \(\alpha = 0\). NEU-106 klärt, über welches Objekt eine Nullstellenexpansion legitimiert ist — und fügt die epistemische Trennung zwischen RH und GUE-Rampe ein.

---

## Satz NEU-106.1 — No-Go: Punktweise Nullstellenformel für \(\Delta_N(h)\)

$$
\boxed{\Delta_N(h) \text{ besitzt keine legitimierte punktweise lineare Nullstellenformel.}}
$$

Begründung: \(\Delta_N(h) = M_N^{-1}\sum_{m\sim M_N}\Lambda(m)\Lambda(m+h) - \mathfrak{S}(h)\) ist ein **quadratisches** Mangoldt-Residual. Die klassische explizite Formel gilt für \(\psi(x)\), d.h.\ lineare Mangoldt-Summen. Für quadratische Formen gibt es keine entsprechende konvergierende Nullstellenreihe im punktweisen Sinn.

Die Zeile
$$
\Delta_N(h) \rightsquigarrow \sum_\rho M_N^{\rho-1}e^{i\gamma h/M_N} + \text{Fehler}
$$
ist als **heuristisches Phasenmodell** nützlich, aber als Satz unzulässig.

**Status: \(\checkmark/\warning[M]\)** (No-Go)

---

## Satz NEU-106.2 — Legitimer Träger: Geglättete Shift-Transformierte

Der erste sinnvolle Ort für eine Nullstellenexpansion ist:

$$
\boxed{\mathcal{E}_{N,H}(\tau) = \sum_h \omega(h/H)\Delta_N(h)e^{-i\tau h/H}.}
$$

Die Glättung in \(h\) reguliert die Konvergenzprobleme der quadratischen expliziten Formel. \(\mathcal{E}_{N,H}\) ist der legitime Träger für Nullstellenbeiträge.

**Status: \(\checkmark[M]\)**

---

## Satz NEU-106.3 — Phasenmodell (heuristisch)

Unter einer geglätteten explizite-Formel-Heuristik erwarten Beiträge der Form:

$$
\mathcal{E}_{N,H}(\tau)
\approx
\sum_\rho c_{\rho,N,H}\,
\widehat{\omega}\!\left(\tau - \frac{\gamma H}{M_N}\right),
$$

äquivalent zum Phasenvergleich \(\tau h/H \sim \gamma h/M_N\), also \(\gamma \sim \tau T\) (NEU-103).

Die Amplituden \(c_{\rho,N,H}\) hängen von Fehlerterm-Kontrolle und Randtrunkierung ab.

**Status: \(\warning[H]\)** (heuristisch; nicht als Satz zitieren)

---

## Satz NEU-106.4 — Leistungsspektrum als Nullstellenpaar-Kanal

Das Leistungsspektrum wird quadratisch:

$$
|\mathcal{E}_{N,H}(\tau)|^2
\approx
\sum_{\rho,\rho'}
c_{\rho,N,H}\overline{c_{\rho',N,H}}\,
\widehat{\omega}\!\left(\tau-\frac{\gamma H}{M_N}\right)
\overline{\widehat{\omega}\!\left(\tau-\frac{\gamma' H}{M_N}\right)}.
$$

Erst in dieser geglätteten quadratischen Form werden Nullstellenpaar-Abstände \(\gamma - \gamma'\) sichtbar. Das Profil nahe \(\alpha = 0\) hängt genau davon ab, wie eng Nullstellenpaare bei kleinem normierten Abstand gehäuft sind.

**Status: \(\warning[H]\)** (heuristisch)

---

## Satz NEU-106.5 — Epistemische Trennung: RH vs.\ GUE-Rampe

$$
\boxed{\text{RH kontrolliert Fehlertermgrößen. GUE-Rampe ist eine Paarstatistik-Aussage. Sie folgt nicht aus RH allein.}}
$$

Präzise:

- RH \(\Rightarrow\) alle Nullstellen auf \(\mathrm{Re}(\rho) = 1/2\) \(\Rightarrow\) \(|M_N^{\rho-1}| = M_N^{-1/2}\) für alle \(\rho\)
- GUE-Rampe \(\Leftrightarrow\) Montgomery-Paarkorrelation \(\Leftrightarrow\) Nullstellenabstandsstatistik \(\sim 1 - (\sin\pi u/\pi u)^2\)

Daher gilt:

$$
\text{explizite Formel} \;\not\Rightarrow\; \text{Rampe}
$$
$$
\text{explizite Formel} + \text{Nullstellenpaarstatistik} \;\Rightarrow\; \text{Rampe}.
$$

Die GUE-Rampe ist **stärker** als RH (sie impliziert RH nicht umgekehrt).

**Status: \(\checkmark[M]\)**

---

## Korrekte Reihenfolge

$$
\Delta_N(h)
\;\not\rightsquigarrow\;
\sum_\rho M^{\rho-1}e^{i\gamma h/M}
\quad\text{(punktweise, No-Go)}
$$

$$
\Delta_N
\longrightarrow
\mathcal{E}_{N,H}
\longrightarrow
|\mathcal{E}_{N,H}|^2
\longrightarrow
\text{Nullstellenpaar-Kanal (nach Entfaltung)}
\longrightarrow
\text{Rampen-Test}
$$

---

## Neue Leitfrage für NEU-107

$$
\boxed{\text{Welche Nullstellenpaarannahme ist exakt äquivalent zum Rampen-Test von NEU-105?}}
$$

Konkrete Schritte:
1. Rampen-Test \(R_{N,H,A}(\varepsilon) \sim \varepsilon^2/A^2\) rückübersetzen in Paarkorrelationsbedingung
2. Vergleich mit Montgomery-Vermutung: Ist die Bedingung stärker oder schwächer?
3. Verbindung zu Goldston\u2013Montgomery: Ist die Paarannahme für den arithmetischen Kanal implizit bereits enthalten?

---

## Tabellarische Statusklassifikation

| Satz | Inhalt | Status |
|------|--------|--------|
| 106.1 | No-Go: punktweise Nullstellenformel für \(\Delta_N(h)\) | \(\checkmark/\warning[M]\) |
| 106.2 | \(\mathcal{E}_{N,H}\) legitimer Träger | \(\checkmark[M]\) |
| 106.3 | Phasenmodell \(\widehat{\omega}(\tau-\gamma H/M)\) | \(\warning[H]\) |
| 106.4 | \(|\mathcal{E}|^2\) Nullstellenpaar-Kanal | \(\warning[H]\) |
| 106.5 | Epistemisch: RH \(\not\Rightarrow\) GUE-Rampe; Paarstat. zusätzlich | \(\checkmark[M]\) |

---

## Verweise

- NEU-105: Binärer Rampen-Test \(R \sim \varepsilon^2/A^2\)
- NEU-103: Phasenvergleich \(\gamma \sim \tau T\)
- NEU-100: \(\Delta_N(h)\) als quadratisches Mangoldt-Residual
- **Montgomery:** *Pair correlation of zeros* (1973)
- **Goldston & Montgomery:** *Pair correlation, primes in short intervals* (1987)
- Goldston, Pintz & Y\u0131ld\u0131r\u0131m: *Primes in tuples* (für quadratische Mangoldt-Summen)
- Connes: *Trace formula* (1999)
