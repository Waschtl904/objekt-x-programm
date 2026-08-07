# NEU-250o — Konstruktionsaudit: Adelisch-archimedischer Port $r_{\infty,W}$

**Katalog-ID:** NEU-250o  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Fehlerkorrektur: 2026-08-07)  
**Auftrag:** Vier atomare Tests für $r_{\infty,W}:\mathcal{S}_{\rm adel}\to\mathcal{S}_{\infty,W}$. Kein Gram, keine Positivität, keine Polarisation — nur Existenz und Zieltyp des Ports.  
**Gesamtausgang:** Teilresultat mit Fehlerkorrektur — $P_{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}(\mathbb{R})$ korrekt; $r_\infty^{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}_\infty$ **falsch** (Gegenbeispiel); korrigierte Kette via $J_{1/2}$ an NEU-250p weitergegeben.  
**Vorgänger:** NEU-250n (N-C; $\iota_\infty^{\rm loc}:\mathcal{S}_{\infty,W}\to\mathcal{W}$ $\checkmark[K/M]$; $r_{\infty,W}\;?[O]$)

---

## 0. Ausgangsbuchung aus NEU-250n

Die Gesamtbrücke zerlegt sich kanonisch:

$$
\boxed{\mathcal{S}_{\rm adel}
\xrightarrow{\;r_{\infty,W}\;?[O]\;}
\mathcal{S}_{\infty,W}
\xrightarrow{\;\iota_\infty^{\rm loc}\;\checkmark[K/M]\;}
\mathcal{W}.} \qquad (0\text{-DAG})
$$

Dieser Knoten auditiert ausschließlich den ersten Pfeil.

---

## 1. Test 1 — Quellentyp: Was ist $\mathcal{S}_{\rm adel}$ wirklich?

### 1.1 Drei mögliche Präzisierungen

| Kandidat | Topologie | Repository-Status |
|---|---|---|
| $\mathcal{S}(\mathbb{A}_\mathbb{Q})$ (Schwartz-Bruhat) | Induktiver Limes über endliche Primmengen $S$ | NEU-245b: Architekturvorgabe; NEU-245c: $?[O]$ |
| $\bigotimes_{\rm res}' \mathcal{S}(\mathbb{Q}_p)$ (eingeschränktes Tensorprodukt) | LF-Topologie | Implizit in NEU-250k K1, nicht explizit |
| Spezieller Quellenunterraum ($\mathcal{S}_{\rm adel}^{\rm tens}$: reine Tensoren) | Unterraum-Spur | Nicht im Repository |

$$
\boxed{\mathcal{S}_{\rm adel}\text{ ist noch kein fertig konstruierter topologischer Raum im Repository.}} \qquad (1\text{-Status})
$$

Arbeitsannahme für alle weiteren Tests:

$$
\boxed{\mathcal{S}_{\rm adel}:=\mathcal{S}(\mathbb{A}_\mathbb{Q})\text{ (Arbeitsannahme, nicht bewiesen).}} \qquad (1\text{-Cond})
$$

---

## 2. Test 2 — Kandidatenklassifikation für $r_{\infty,W}$

**Kandidat A** (direkte Projektion $f\mapsto f_\infty$): Nicht kanonisch fortsetzbar auf ganz $\mathcal{S}(\mathbb{A}_\mathbb{Q})$ (NEU-250n §8).

**Kandidat B** (Paarung mit Haarvektor $\mathbf{1}_{\hat{\mathbb{Z}}}$):

$$
P_{\rm Haar}F(x_\infty) := \int_{\hat{\mathbb{Z}}} F(x_\infty, x_{\rm fin})\,dx_{\rm fin}. \qquad (2\text{-B})
$$

Linear, wohldefi­niert auf $\mathcal{S}(\mathbb{A}_\mathbb{Q})$, kanonisch. Zielraum: **siehe Test 3**.

**Kandidat C** (Fourier-Komposition): Typkorrekt formulierbar, Konvergenz offen.

| Kandidat | Linear? | Kanonisch? | Auf ganz $\mathcal{S}(\mathbb{A}_\mathbb{Q})$? |
|---|---|---|---|
| A | Ja (reine Tensoren) | Nein | Nein |
| **B** | **Ja** | **Ja ($\mathbf{1}_{\hat{\mathbb{Z}}}$ kanonisch)** | **Ja** |
| C | Ja | Potenziell ja | Offen |

---

## 3. Test 3 — Bildbedingung: Fehlerkorrektur

### 3.1 Behauptung (erste Fassung, jetzt zurückgezogen)

Die erste Fassung dieses Knotens buchte:
$$
r_\infty^{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}_\infty\quad\checkmark[M]_{\rm cond}.
$$

**Diese Buchung ist falsch.** Gegenbeispiel:

### 3.2 Gegenbeispiel

Nehme
$$
F(x_\infty, x_{\rm fin}) = e^{-x_\infty^2}\cdot\mathbf{1}_{\hat{\mathbb{Z}}}(x_{\rm fin}),
\qquad\operatorname{vol}(\hat{\mathbb{Z}})=1.
$$

Dann:
$$
P_{\rm Haar}F(x) = e^{-x^2}.
$$

Wäre $P_{\rm Haar}F\in\mathcal{S}_\infty$, müsste nach NEU-220a Definition
$$
g(y) := (\Phi P_{\rm Haar}F)(y) = e^{-e^{2y}}
$$
eine Schwartz-Funktion auf $\mathbb{R}$ sein. Aber:
$$
\boxed{g(y) = e^{-e^{2y}}\longrightarrow 1 \qquad (y\to-\infty).}
$$

$g$ ist nicht Schwartz (kein Abfall für $y\to-\infty$). Also:

$$
\boxed{P_{\rm Haar}F\notin\mathcal{S}_\infty.} \qquad (3\text{-NoGo})
$$

### 3.3 Was $P_{\rm Haar}$ tatsächlich liefert

Die Haar-Paarung liefert eine gewöhnliche additive Schwartz-Funktion:

$$
\boxed{P_{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\longrightarrow\mathcal{S}(\mathbb{R}).} \qquad (3\text{-Correct})
$$

Das ist die übliche Tate-Schwartz-Bruhat-Struktur am reellen Ort. $\mathcal{S}_\infty$ verlangt dagegen schnellen Abfall auch für $x\to 0^+$ (d.h. $y\to-\infty$), was die additive Schwartz-Bedingung nicht sicherstellt.

### 3.4 Zusätzlicher Fehler: der Dichtheits-Pfeil

Die erste Fassung schrieb:
$$
\mathcal{S}_\infty\xrightarrow{\text{Restriktion/Dichtheitsargument}}\mathcal{S}_{\infty,W}.
$$

Dieser Pfeil ist **kein definierter Operator**. Dichte läuft in die andere Richtung: ein kleiner Testkern kann in einem größeren Raum dicht liegen, erzeugt aber keine kanonische Projektion vom großen zurück auf den kleinen Raum. Dieser Pfeil wird ersatzlos gestrichen.

---

## 4. Test 4 — Kanonizität von $\phi_{\rm fin}^0$ (bleibt gültig)

$\phi_{\rm fin}^0 = \mathbf{1}_{\hat{\mathbb{Z}}}$ ist der kanonischste Kandidat (Haarmaß, Eulerprodukt $\bigotimes_p \mathbf{1}_{\mathbb{Z}_p}$). Der KMS-Grundzustand bei $\beta=1$ ist strukturell ähnlich, aber $\beta$-abhängig.

$$
\boxed{\phi_{\rm fin}^0 = \mathbf{1}_{\hat{\mathbb{Z}}}\text{ ist kanonisch. Der Paarungsschritt }P_{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}(\mathbb{R})\text{ ist korrekt.}} \qquad (4\text{-OK})
$$

---

## 5. Korrigierte Statusbuchungen

$$
P_{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}(\mathbb{R})\quad\checkmark[M]_{\rm cond} \qquad (5\text{-a})
$$

$$
r_\infty^{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}_\infty\quad\times[M]\qquad(\text{Gegenbeispiel \S3.2}) \qquad (5\text{-b})
$$

$$
\text{Zielraumrevision nach }\mathcal{S}_\infty\quad\times[M]\qquad(\text{Zielraum war falsch}) \qquad (5\text{-c})
$$

$$
\text{Dichtheits-Pfeil }\mathcal{S}_\infty\to\mathcal{S}_{\infty,W}\quad\times[M]\qquad(\text{kein definierter Operator}) \qquad (5\text{-d})
$$

$$
r_{\infty,W}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}_{\infty,W}\quad?[O]\quad\to\text{NEU-250p} \qquad (5\text{-e})
$$

---

## 6. Weitergabe an NEU-250p

Das Gegenbeispiel zeigt direkt auf die Korrektur. Nach der Haar-Paarung liegt man in $\mathcal{S}(\mathbb{R})$. Der fehlende Schritt nach $\mathcal{S}_\infty$ ist der **Halbgewichtstransfer**:

$$
\boxed{J_{1/2}h(x) := x^{1/2}h(x),\qquad x>0.} \qquad (6\text{-J})
$$

Die korrigierte Kette:

$$
\boxed{\mathcal{S}(\mathbb{A}_\mathbb{Q})\xrightarrow{\;P_{\rm Haar}\;}\mathcal{S}(\mathbb{R})\xrightarrow{\;J_{1/2}\;}\mathcal{S}_\infty.} \qquad (6\text{-Chain})
$$

Die Komposition mit $\mathcal{M}_\infty$ ergibt auf der kritischen Geraden:
$$
(\mathcal{M}_\infty J_{1/2}P_{\rm Haar}F)(t) = \int_0^\infty (P_{\rm Haar}F)(x)\,x^{1/2+it}\,d^\times x.
$$

Das ist die archimedische Tate-Mellinform bei $s=\frac{1}{2}+it$ — die kritische Zentrierung entsteht aus dem Typwechsel, nicht durch Annahme.

Beweis aller vier Punkte: **NEU-250p**.

---

## 7. Auditmatrix (korrigiert)

| Test | Frage | Befund |
|---|---|---|
| 1 — Quelle | $\mathcal{S}_{\rm adel}$ definiert? | Architekturplatzhalter; Arbeitsannahme $\mathcal{S}(\mathbb{A}_\mathbb{Q})$ |
| 2 — Kandidaten | Bester Kandidat? | Kandidat B ($P_{\rm Haar}$ mit $\mathbf{1}_{\hat{\mathbb{Z}}}$), Ziel $\mathcal{S}(\mathbb{R})$ |
| 3 — Bild | Landet $P_{\rm Haar}(F)\in\mathcal{S}_\infty$? | **Nein** — Gegenbeispiel $e^{-x^2}$ |
| 3b — Bild korrekt | Wo landet $P_{\rm Haar}$? | $\mathcal{S}(\mathbb{R})$ |
| 4 — Kanonizität | $\mathbf{1}_{\hat{\mathbb{Z}}}$ kanonisch? | Ja |
| 5 — Zielraum | Korrekte Fortsetzung? | Via $J_{1/2}$: $\mathcal{S}(\mathbb{R})\to\mathcal{S}_\infty$ — NEU-250p |

---

## Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-250n | e0f2f70 | Vorgänger; $\iota_\infty^{\rm loc}$ $\checkmark[K/M]$; $r_{\infty,W}$ $?[O]$ |
| NEU-220a | 653c8a9 | $\mathcal{S}_\infty$-Definition; $\mathcal{M}_\infty$ |
| NEU-220j | 41e28cf | $\mathcal{W}$, LF-Topologie |
| NEU-245b | 79ecf25 | $\mathcal{S}_{\rm adel}$ Architekturvorgabe |
| NEU-245c | 1ef32ab | $\mathcal{S}_{\rm adel}$ Konstruktion $?[O]$ |
| NEU-250m | ce1a7af | M1--M4 |
| **NEU-250p** | **neu** | **$J_{1/2}$-Direktaudit: $\mathcal{S}(\mathbb{R})\to\mathcal{S}_\infty$, Tate-Zentrierung** |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Fehlerkorrektur 2026-08-07: $r_\infty^{\rm Haar}\to\mathcal{S}_\infty$ zurückgezogen; Zielraumrevision zurückgezogen; Dichtheits-Pfeil gestrichen. Korrekte Kette an NEU-250p.*
