# NEU-253 — M4: RH-unabhängige geometrische Realisierung von $B_W$

**Katalog-ID:** NEU-253  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** M4 — Vier atomare Fragen: (A) Hilbertmajorante $\langle\cdot,\cdot\rangle_0$ und Operator $A_X$; (B) Indefinite Signatur ohne RH; (C) Arithmetische Reduktion $\mathcal{K}_{\rm phys}/\mathcal{N}$; (D) Positivitätstest $B_W|_{\mathcal{K}_X}\ge0$ ohne RH.  
**Vorläufiger Status:** M4-A bis D offen $?[O]$.  
**Vorgänger:** NEU-252 M3 (Patch), NEU-250r, NEU-220l, NEU-220k, NEU-220m, NEU-220s/t

---

## 0. Ausgangslage nach M3

Nach M3 (NEU-252) besteht:
$$
\boxed{\mathcal{S}_{\rm adel}^{\rm amp}\longrightarrow(\mathcal{A}_{\rm PW},B_W)\text{ vollständig hermitesch, RH-frei.}\quad\checkmark[K/M]}
$$

M4 fragt nicht mehr: „Wie lautet die Weil-Form?“  
M4 fragt: **Welche kanonische globale Geometrie realisiert $B_W$, und woher kommt ihre positive Reduktion?**

$$
\boxed{\text{Nicht: „Unter RH existiert ein Hilbertraum.“}} \qquad (0\text{-No})
$$

$$
\boxed{\text{Ziel: Die Arithmetik konstruiert unabhängig von RH einen Raum, der sich als positiv erweist.}} \qquad (0\text{-Goal})
$$

Genau dort beginnt das eigentliche Objekt X.

---

## 1. Typen- und Raumkarte nach M3

| Raum | Definition | Status |
|---|---|---|
| $\mathcal{A}_{\rm PW}$ | $C_c^\infty(\mathbb{R};\mathbb{C})$ | $\checkmark[K/M]$ |
| $\mathcal{G}_{\rm ev}^{\mathbb{C}}$ | $C_c^\infty(\mathbb{R};\mathbb{C})_{\rm even}$ | $\checkmark[K/M]$ |
| $\mathcal{H}_{\rm PW}^{\mathbb{C}}$ | ganze PW-Funktionen; $|_{\mathbb{R}}\in\mathcal{S}(\mathbb{R})$ | $\checkmark[K/M]$ |
| $\mathcal{W}_{\mathbb{C}}$ | komplexifizierter Weil-Testkernraum | $\checkmark[K/M]$ |
| $\mathcal{S}_{\rm adel}^{\rm amp}$ | adelische Amplitudenquelle (NEU-250r) | $\checkmark[K/M]$ |
| $B_W(a,b)$ | hermitesche sesquilineare Weil-Form | $\checkmark[K/M]$ |
| $B_W\ge0$ | Äquivalent zu RH | $?[O]$ — Firewall |

$\mathcal{A}_{\rm PW}=C_c^\infty$ ist ein Testfunktionenraum, **kein** Hilbertraum. Für einen Krein- oder Hilbertraum wird eine vollständige Majoranttopologie benötigt.

---

## 2. M4-A — Hilbertmajorante und Realisierungsoperator

**Frage:** Existiert aus der adelischen/arithmetischen Struktur kanonisch ein positives inneres Produkt $\langle\cdot,\cdot\rangle_0$ auf (einem dichten Teilraum von) $\mathcal{A}_{\rm PW}$ und ein bzgl. $\langle\cdot,\cdot\rangle_0$ symmetrischer Operator $A_X$ mit
$$
\boxed{B_W(a,b)=\langle a,A_Xb\rangle_0\,?} \qquad (2\text{-AX})
$$

**Anforderungen an $\langle\cdot,\cdot\rangle_0$:**
- Muss aus der Struktur von Objekt X selbst kommen (adelisch, archimedisch-endlich), nicht post hoc gewählt.
- Soll $\mathcal{A}_{\rm PW}$ vollständig machen (Hilbert-Abschluss $\overline{\mathcal{A}_{\rm PW}}^0$).
- $A_X$ soll auf diesem Abschluss ein wohldefinierter selbstadjungierter Operator sein.

**Kandidaten aus dem Repo:**
- NEU-220e: Semifinite Spur $\tau$ als mögliche Prä-Geometrie
- NEU-220m/n: Rigged-Operator, Randkanäle
- NEU-220w: Hankelvollständigkeit, Moment-GNS
- NEU-221: Adelische Momentquelle

$$
\text{M4-A}\quad?[O] \qquad (2\text{-status})
$$

---

## 3. M4-B — Indefinite Signatur ohne RH

**Frage:** Wenn $A_X$ existiert (M4-A): Welche positiven, negativen und neutralen Spektralräume besitzt $A_X$?

$$
\boxed{\text{Nicht: positiv machen. Zuerst: die tatsächliche indefinite Signatur verstehen.}} \qquad (3\text{-Scope})
$$

**Konkrete Teilfragen:**
- Wann liegt $B_W(a,a)<0$? (Gegenbeispiele ohne RH konstruieren.)
- Hat $B_W$ endliche oder unendliche negative Trägheit?
- NEU-220s/t: Kreinraum-Klassifikation, Off-Axis-Trägheit — was gilt für $B_W$?

$$
\text{M4-B}\quad?[O] \qquad (3\text{-status})
$$

---

## 4. M4-C — Arithmetische Reduktion

**Frage:** Gibt es unabhängig von RH einen kanonischen BC/adelischen Unterraum, Constraint oder Quotienten
$$
\boxed{\mathcal{K}_{\rm phys}/\mathcal{N}} \qquad (4\text{-Kphys})
$$
auf dem die negativen Richtungen von $B_W$ verschwinden?

**Präzisierung:**
- $\mathcal{K}_{\rm phys}\subset\mathcal{A}_{\rm PW}$ soll aus arithmetischer/adelischer Struktur emergieren (z.B. Adelbedingung, Periodizität, Hecke-Kompatibilität).
- $\mathcal{N}:=\{a\in\mathcal{K}_{\rm phys}:B_W(a,a)=0\}$ der Nullraum auf $\mathcal{K}_{\rm phys}$.
- $B_W|_{\mathcal{K}_{\rm phys}/\mathcal{N}}$ soll positiv-semidefinit sein.

**Strategische Bedeutung:** Dieser Schritt unterscheidet sich qualitativ von M4-D. Hier wird kein Ergebnis über $B_W$ vorausgesetzt; die Geometrie soll aus der Arithmetik **folgen**.

$$
\text{M4-C}\quad?[O] \qquad (4\text{-status})
$$

---

## 5. M4-D — Positivitätstest

**Frage:** Erst wenn $\mathcal{K}_{\rm phys}/\mathcal{N}$ in M4-C konstruiert ist: Gilt
$$
\boxed{B_W|_{\mathcal{K}_X}\ge0\quad\text{ohne RH als Voraussetzung?}} \qquad (5\text{-Test})
$$

**Firewall-Erinnerung:** M4-D **nicht** vor M4-C bearbeiten.

- GNS-Realisierung $\mathcal{H}_{\mathfrak{W}}:=\mathcal{A}_{\rm PW}/\ker B_W$ ist nur sinnvoll, wenn $B_W\ge0$ zunächst unabhängig etabliert ist.
- Positivität via RH als Voraussetzung wäre zirkulär: Wir würden die zu beweisende Eigenschaft voraussetzen.

$$
\boxed{\text{Gelingt M4-D ohne RH: zentraler Objekt-X-Mechanismus.}} \qquad (5\text{-Central})
$$

$$
\text{M4-D}\quad?[O] \qquad (5\text{-status})
$$

---

## 6. Abhängigkeiten und offene Repo-Verbindungen

| Referenz | SHA | Relevanz für M4 |
|---|---|---|
| NEU-252 M3 (Patch) | 4ee78ed | $B_W$ hermitesch, $B_W^{\rm adel}$ |
| NEU-220l | 1dc07b3 | Positivitäts-Firewall; $B_W\ge0\Leftrightarrow$ RH |
| NEU-220m | abf3c12 | Rigged-Operator; Randkanäle |
| NEU-220n | 3e9f204 | Endliche Fensteroperatoren |
| NEU-220s | 7c1a3f9 | Kreinraum-Klassifikation; Off-Axis-Trägheit |
| NEU-220t | d8b2e51 | Metrikblock; Similarity-NoGo |
| NEU-220e | 9a1f3c2 | Semifinite Spur $\tau$ |
| NEU-220w | bf4e601 | Hankelvollständigkeit; Moment-GNS |
| NEU-221 | 8c3d412 | Adelische Momentquelle |
| NEU-250r (Patch) | bd1c0ab | Surjektiver Port; $\mathcal{S}_{\rm adel}^{\rm amp}$ |

---

## 7. Atomare Nächste Schritte

Die natürliche Bearbeitungsreihenfolge:

1. **M4-A zuerst:** Kandidaten für $\langle\cdot,\cdot\rangle_0$ aus NEU-220e/m/w/221 systematisch prüfen.
2. **M4-B:** Für jeden Kandidaten: Signaturanalyse von $A_X$; Gegenbeispiele für $B_W(a,a)<0$.
3. **M4-C:** Arithmetische Reduktion; Hecke-/Adelbedingung als Constraint-Kandidat.
4. **M4-D:** Positivitätstest auf $\mathcal{K}_{\rm phys}/\mathcal{N}$, streng RH-frei.

$$
\boxed{\text{M4: RH-unabhängige geometrische Realisierung von }B_W.\quad?[O]} \qquad (7\text{-M4})
$$

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07.*
