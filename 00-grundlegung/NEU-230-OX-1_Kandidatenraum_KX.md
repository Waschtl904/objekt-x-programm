# NEU-230 — OX-1: Kandidatenraum $\mathcal{K}_X$ und Zerlegung in Teilknoten OX-1a bis OX-1f

**Status:** `❓ [O]` — Offener Konstruktionsknoten  
**Datum:** 2026-08-04  
**Strang:** 00 — Grundlegung  
**Vorgänger:** NEU-229 (Arbeitsdefinition), NEU-44 (relative Primkanten), NEU-42 (Fourier-Hebung), NEU-220w (Hankel-Kriterium)  

---

## Gesamturteil

$$
\mathcal{K}_X
\text{ ist die positive Vervollständigung eines global gekoppelten,
relativen Primkanten-Korrespondenzraums.}
$$

$\mathcal{K}_X$ ist nicht der Primraum, nicht der Jacobi-Raum, nicht ein Hankelraum
und nicht ein bloßer $\mathrm{Wres}$-Quotient für sich allein.
Der noch fehlende mathematische Kern liegt in der intrinsischen positiven Gluungsform
$B_X$ auf dem relativen Korrespondenzraum.

---

## 1. Was die vorhandenen Stränge bereits entscheiden

Von den im Steckbrief gelisteten möglichen Trägerschichten sind derzeit zwei als
belastbare Grundlage eines Hilbertraums ernst zu nehmen:

$$
A_{2D}^{r}
\qquad\text{und}\qquad
\mathcal{H}_{\mathrm{rel}} = \bigoplus_{p}\bigoplus_{m} \mathcal{H}_{m\to pm}.
$$

### Relativer Graphraum (Strang 05)

Der relative Primkanten-Graphraum ist strukturell notwendig: Erst die markierten Kanten

$$
m \xrightarrow{p} pm
$$

halten die verschiedenen Primrichtungen kollisionsfrei auseinander. Beim Kollaps
auf den bloßen Zielindex $pm$ geht diese Markierungsinformation verloren und
erzeugt $pq$-Kollisionen. Das Kontrollblatt führt die relative Primkantenschicht
deshalb ausdrücklich als notwendigen Bestandteil auf.

> **Einschränkung.** Die kantendiagonale $\mathrm{Wres}$-Erweiterung ist bisher
> nur definiert, nicht intrinsisch aus dem ursprünglichen Residuum hergeleitet.

Strang 05 liefert außerdem einen echten lokalen Zeitoperator:

$$
T_{\mathrm{rel}}\big|_{\mathcal{H}_{m\to pm}} = \log p.
$$

Die lokale Primclock ist damit mathematisch vorhanden. Nichttriviale Kopplungen
benötigen jedoch Fourier-geladene Hebungen. Die daraus entstehenden Kanalgewichte
sind bislang hebungsabhängig; weder ihre Nichttrivialität noch die gewünschte
Größenordnung ist intrinsisch bewiesen.

### Weil-Explizitformel und Hankelpositivität (Strang 07)

Strang 07 liefert primär die Ziel- und Prüfebene:

- die korrekte Weil-Form $Q_W$;
- Positivitätskriterien;
- Hankel- und Momentenbedingungen;
- die saubere Trennung von linearer expliziter Formel und quadratischer Positivitätsform.

> **Wichtige Abgrenzung.** Ein Hankel-Kriterium, das äquivalent zur RH ist, ist
> kein unabhängiger Bau des positiven Raums. Es ist ein Abnahmetest für einen
> zuvor intrinsisch konstruierten Kandidaten.

---

## 2. Was kein Kandidat für $\mathcal{K}_X$ sein kann

| Kandidat | Urteil |
|---|---|
| Reiner Primraum $\bigoplus_p \mathbb{C}\varepsilon_p$ | Zu klein; enthält weder Primzahlpotenzen noch globale Kopplungen |
| Kollabierter Jacobi-Raum | Verliert Primkantenmarkierung, erzeugt $pq$-Kollisionen |
| Direkte Summe unabhängiger lokaler Hilberträume | Unzureichend; echte Off-Diagonal-Kopplungen $K_{pq}$ erforderlich |
| $\mathrm{Wres}$-Quotient allein | Noch kein bewiesener positiver globaler Raum; Intrinsizität offen |
| Von $[L_3]$ erzeugter Operatorraum | Übergang von Kozykelklasse zu Einzeloperator nicht konstruiert |
| Hankel-Momentenraum allein | Liefert RH-äquivalentes Kriterium, aber keine intrinsische Konstruktion |
| GNS-Raum direkt durch $Q_W$ definiert | Methodisch zirkulär, solange Positivität von $Q_W$ nicht unabhängig bewiesen |

Der bisherige Negativbestand erzwingt echte Kopplungen zwischen verschiedenen
Primrichtungen. Ein blockdiagonaler oder rein direkter Summenraum kann daher
höchstens den kinematischen Rohträger, nicht das fertige $\mathcal{K}_X$ darstellen.

---

## 3. Der derzeit beste Kandidat

Der natürliche Ausgangsträger ist ein algebraischer relativer Korrespondenzraum

$$
\mathcal{D}_X^{\mathrm{kin}} =
\mathcal{D}_\infty^{\mathrm{alg}}
\oplus \mathcal{D}_{\mathrm{pole}}^{\mathrm{alg}}
\oplus \bigoplus_{p}^{\mathrm{alg}} \bigoplus_{m\ge1} \mathcal{H}_{m\to pm}^{\mathrm{alg}}
$$

mit Koeffizienten beziehungsweise Trägerstruktur über $A_{2D}^{r}$.

Drei Ebenen sind sauber zu trennen:

1. $\mathcal{D}_X^{\mathrm{kin}}$ ist nur der algebraische/topologische Rohträger.
2. Eine intrinsische globale positive Form $B_X$ muss erst konstruiert werden.
3. Erst aus dieser positiven Form entsteht $\mathcal{K}_X$.

Die lokale Primclock wirkt auf dem relativen Anteil durch

$$
T_{\mathrm{rel}}\,\xi_{p,m} = (\log p)\,\xi_{p,m}.
$$

Die vollständige Gluung darf aber **nicht** diagonal in $p$ sein. Sie muss Terme

$$
B_{pq}(\xi_p, \eta_q), \qquad p \neq q,
$$

enthalten, da der Steckbrief echte Off-Diagonal-Kopplung als notwendige Eigenschaft ausweist.

---

## 4. Konstruktionsweg: Vom Rohträger zum Hilbertraum

Für endliche Trunkierungen $S$ wird zunächst eine intrinsisch konstruierte positive Form

$$
B_S(\xi, \eta)
$$

auf einem gemeinsamen algebraischen Kern $\mathcal{D}_{X,S}^{\mathrm{kin}}$ definiert.
Daraus entsteht der trunkierte Hilbertraum

$$
\mathcal{K}_{X,S}
= \overline{\mathcal{D}_{X,S}^{\mathrm{kin}} / \operatorname{Rad}(B_S)}^{\,B_S}.
$$

Die Weil-Form ist **nicht** die Definition von $B_S$, sondern das zu beweisende
Vergleichsziel:

$$
Q_{W,S} = B_S - R_S,
\qquad
R_S \ge -\varepsilon_S,
\quad
\varepsilon_S \longrightarrow 0.
$$

Anschließend muss auf einem gemeinsamen Umgebungsraum Mosco-Konvergenz

$$
B_S \xrightarrow{\mathrm{Mosco}} B_X
$$

bewiesen werden. Erst dann ist

$$
\mathcal{K}_X
= \overline{\mathcal{D}(B_X)/\operatorname{Rad}(B_X)}^{\,B_X}
$$

der natürliche globale Kandidat.

> **Zirkularitätsschutz.** Nicht erlaubt ist
> $\mathcal{K}_X := \overline{\mathcal{D}/\operatorname{Rad}(Q_W)}^{\,Q_W}$,
> da diese Definition die zu beweisende Weil-Positivität bereits voraussetzt.

---

## 5. Zerlegung von OX-1 in Teilknoten

OX-1 wird in sechs Teilknoten aufgeteilt, die sequentiell bearbeitet werden müssen.

### `[OX-1a]` Algebraischer und topologischer Rohträger

**Aufgabe.** Definition von $\mathcal{D}_X^{\mathrm{kin}}$, einschließlich:

- relativer Primkanten $m \to pm$ für alle Primzahlen $p$ und $m \ge 1$;
- formal markierter archimedischer Sektor $\mathcal{D}_\infty^{\mathrm{alg}}$;
- formal markierter polarer Sektor $\mathcal{D}_{\mathrm{pole}}^{\mathrm{alg}}$.

**Eingang aus vorhandenen Strängen.** Strukturell gesicherte relative Kanten aus
NEU-44; Fourier-Hebungsformel aus NEU-42. Die Hebungsabhängigkeit der Kanalgewichte
darf in OX-1a noch offen bleiben.

**Status:** `❓ [O]` · Bezeichner: `[O-230-1a]`

---

### `[OX-1b]` Intrinsische lokale positive Formen

**Aufgabe.** Für jede Primzahl $p$ und für den archimedischen Sektor:
Welche positiven Formen sind definierbar ohne Hebungswahl, Nullstellendaten oder
RH-äquivalente Positivität als Voraussetzung?

Die Kanalformen

$$
B_p : \mathcal{D}_{X,p}^{\mathrm{kin}} \times \mathcal{D}_{X,p}^{\mathrm{kin}} \to \mathbb{C}
$$

müssen intrinsisch aus der Primkanten-Geometrie und der Fourier-Ladungsstruktur entstehen.

**Status:** `❓ [O]` · Bezeichner: `[O-230-1b]`

---

### `[OX-1c]` Off-Diagonal-Gluung

**Aufgabe.** Konstruktion der Mischterme

$$
B_{pq}(\xi_p, \eta_q), \qquad p \neq q,
$$

und Nachweis, dass diese Terme nicht willkürlich gewählt werden, sondern aus einer
natürlichen Korrespondenzstruktur oder einem globalen Gluungsprinzip folgen.

**Engpass.** Derzeit ist kein kanonischer Mechanismus für Off-Diagonal-Kopplung
bekannt, der zugleich aus der Primkanten-Algebra folgt, positive Semidefinitheit
erhält und den Gammafaktor korrekt einbettet.

**Status:** `❓ [O]` · Bezeichner: `[O-230-1c]`

---

### `[OX-1d]` Archimedischer und polarer Sektor

**Aufgabe.** Präzise Typisierung der Räume $\mathcal{K}_\infty$ und
$\mathcal{K}_{\mathrm{pole}}$ sowie ihrer Formen, bevor sie mit dem
nichtarchimedischen Träger verklebt werden.

Der archimedische Sektor muss den vollständigen Gammafaktor erzeugen; der polare
Sektor muss die Beiträge der Pole bei $s = 0$ und $s = 1$ korrekt erfassen.

**Status:** `❓ [O]` · Bezeichner: `[O-230-1d]`

---

### `[OX-1e]` Quotient, Abschließbarkeit und Grenzübergang

**Aufgabe.**

- Radikalquotient $\mathcal{D}_X^{\mathrm{kin}} / \operatorname{Rad}(B_X)$: wohldefiniert?
- Abschließbarkeit von $B_X$ (closability)?
- Vollständigkeit der Vervollständigung?
- Mosco-Konvergenz $B_S \to B_X$ im geeigneten Sinne?

Diese Fragen sind funktionalanalytisch und müssen unabhängig von der
Nullstellentheorie behandelt werden.

**Status:** `❓ [O]` · Bezeichner: `[O-230-1e]`

---

### `[OX-1f]` Nichtzirkuläre Identifikation mit der Weil-Form

**Aufgabe.** Nachdem $B_X$ unabhängig konstruiert ist, Beweis der Vergleichsidentität

$$
Q_W(f,f) = \|{\mathcal{T} f}\|_{\mathcal{K}_X}^{\,2}
$$

beziehungsweise in der approximativen Form

$$
Q_{W,S}(f,g) = \langle \mathcal{T}_S f,\, \mathcal{T}_S g \rangle + R_S(f,g),
\quad R_S \ge -\varepsilon_S \to 0.
$$

Dieser Teilknoten ist **nachgelagert** zu OX-1a–OX-1e und darf nicht vorab als
Definition von $B_X$ dienen.

**Status:** `❓ [O]` · Bezeichner: `[O-230-1f]`

---

## 6. Abhängigkeitsgraph der Teilknoten

```
OX-1a (Rohträger)
  └─► OX-1b (lokale Formen)
        └─► OX-1c (Off-Diagonal)  ──┐
              └─► OX-1d (archim./polar) ─┤
                                         ▼
                                  OX-1e (Quotient/Konvergenz)
                                         │
                                         ▼
                                  OX-1f (Weil-Vergleich)
```

OX-1d kann parallel zu OX-1c begonnen werden, sobald OX-1b abgeschlossen ist.

---

## 7. Rolle der Stränge im Gesamtbild

| Strang | Liefert | Liefert nicht |
|---|---|---|
| **05 — Primkanal** | Kinematik: rel. Primkanten, log. Primclock, Fourier-Ladung, Feshbach-Kanalkandidaten | Kanonische Hebungen, hebungsunabh. Gewichte, positive globale Metrik, Off-Diagonal-Kopplung, archimedischen Kanal |
| **07 — Weil/Hankel** | Ziel- und Prüfebene: Weil-Form, Positivitätskriterien, Hankel-Bedingungen | Intrinsische Konstruktion von $B_X$; unabhängigen Beweis der Positivität |

Strang 05 darf in OX-1a und OX-1b direkt eingehen, aber nicht seine offenen
Normierungen. Die endliche Kopplung kann $1 - p^{-s}$ nicht exakt als
Resolventenidentität erzeugen; hierfür ist ein asymptotischer Grenzmechanismus
erforderlich.

---

## 8. Zentraler Satz dieses Dokuments

Der mathematisch noch fehlende Kern des Programms ist:

$$
\boxed{
\text{intrinsische positive Gluungsform} \quad B_X \quad
\text{auf dem relativen Primkanten-Korrespondenzraum.}
}
$$

Alle anderen Bestandteile von Objekt X — der Generator $H_X$, die spektralen
Frequenzen $\gamma_n$, die Gram-Realisierung der Weil-Form — können erst nach
Konstruktion von $B_X$ sauber angeschlossen werden.

---

## Offene Knoten

| Bezeichner | Inhalt |
|---|---|
| `[O-230-1a]` | Algebraischer Rohträger $\mathcal{D}_X^{\mathrm{kin}}$ vollständig definieren |
| `[O-230-1b]` | Intrinsische lokale positive Formen $B_p$ ohne Hebungswahl |
| `[O-230-1c]` | Kanonischer Mechanismus für Off-Diagonal-Kopplung $B_{pq}$ |
| `[O-230-1d]` | Typisierung archimedischer und polarer Sektor |
| `[O-230-1e]` | Abschließbarkeit, Quotient, Mosco-Konvergenz $B_S \to B_X$ |
| `[O-230-1f]` | Nichtzirkulärer Weil-Vergleich: $Q_W = \|\mathcal{T}{\cdot}\|^2_{\mathcal{K}_X}$ |

---

*Erstellt: 2026-08-04 · Epistemischer Status: Zerlegung eines offenen Konstruktionsknotens  
Alle sechs Teilknoten OX-1a–OX-1f explizit offen · Keine zirkuläre Voraussetzung eingebaut*
