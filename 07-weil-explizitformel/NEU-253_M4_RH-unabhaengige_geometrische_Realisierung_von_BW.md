# NEU-253 — M4: RH-unabhängige geometrische Realisierung von $B_W$

**Katalog-ID:** NEU-253  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch: 2026-08-07)  
**Auftrag:** M4 — Vier atomare Fragen: (A) kanonische Hilbertmajorante und Operator $A_X$; (B) Signatur-Firewall; (C) arithmetischer Constraint $\mathcal{K}_{\rm phys}/\operatorname{Rad}(B_W|_{\mathcal{K}_{\rm phys}})$; (D) Positivitätstest $B_W|_{\mathcal{K}_X}\ge0$ ohne RH.  
**Patch:** $\mathcal{N}:=\{B_W(a,a)=0\}$ $\times[M]$ $\to$ $\operatorname{Rad}(B_W|_{\mathcal{K}_{\rm phys}})$; M4-B neu als Signatur-Firewall; M4-A Beschränktheit/Abschließbarkeit getrennt.  
**Vorläufiger Status:** M4-A bis D offen $?[O]$.  
**Vorgänger:** NEU-252 M3 (Patch), NEU-250r, NEU-220l, NEU-220k, NEU-220m, NEU-220s/t

---

## 0. Ausgangslage nach M3

Nach M3 (NEU-252 Patch) besteht:
$$
\boxed{\mathcal{S}_{\rm adel}^{\rm amp}\twoheadrightarrow\mathcal{A}_{\rm PW}\xrightarrow{B_W}\mathbb{C}\quad\text{vollständig hermitesch, RH-frei.}\quad\checkmark[K/M]}
$$

M4 fragt nicht mehr: „Wie lautet die Weil-Form?“  
M4 fragt:
$$
\boxed{\text{Welches positive Hintergrund-Skalarprodukt liefert die Arithmetik selbst?}} \qquad (0\text{-Goal})
$$

$$
\boxed{\text{Nicht: „Unter RH existiert ein Hilbertraum.“}} \qquad (0\text{-No})
$$
$$
\boxed{\text{Ziel: Die Arithmetik konstruiert unabhängig von RH einen Raum, der sich als positiv erweist.}} \qquad (0\text{-Pos})
$$

---

## 1. Typen- und Raumkarte nach M3

| Raum | Definition | Status |
|---|---|---|
| $\mathcal{A}_{\rm PW}$ | $C_c^\infty(\mathbb{R};\mathbb{C})$ | $\checkmark[K/M]$ |
| $\mathcal{G}_{\rm ev}^{\mathbb{C}}$ | $C_c^\infty(\mathbb{R};\mathbb{C})_{\rm even}$ | $\checkmark[K/M]$ |
| $\mathcal{H}_{\rm PW}^{\mathbb{C}}$ | ganze PW-Fkt.; $|_{\mathbb{R}}\in\mathcal{S}(\mathbb{R})$ | $\checkmark[K/M]$ |
| $\mathcal{W}_{\mathbb{C}}$ | komplexifizierter Weil-Testkernraum | $\checkmark[K/M]$ |
| $\mathcal{S}_{\rm adel}^{\rm amp}$ | adelische Amplitudenquelle (NEU-250r) | $\checkmark[K/M]$ |
| $B_W(a,b)$ | hermitesche sesquilineare Weil-Form | $\checkmark[K/M]$ |
| $B_W\ge0$ | Äquivalent zu RH | $?[O]$ — Firewall |

$\mathcal{A}_{\rm PW}=C_c^\infty$ ist ein Testfunktionenraum, **kein** Hilbertraum. Für einen Krein- oder Hilbertraum wird eine vollständige Majoranttopologie benötigt.

---

## 2. Vorab: Radikal vs. isotroper Kegel

**Typkorrektur** (erste Fassung $\times[M]$):

$$
\boxed{\mathcal{N}:=\{a\in\mathcal{K}_{\rm phys}:B_W(a,a)=0\}\quad\times[M].} \qquad (2\text{-IsoErr})
$$

Das ist der **isotrope Kegel**. Für indefinite Formen ist dieser im Allgemeinen **nicht** linear. Gegenbeispiel mit $[x,y]:=|x|^2-|y|^2$: $(1,1)$ und $(1,-1)$ sind beide isotrop, ihre Summe $(2,0)$ aber nicht.

**Korrektur: Das Radikal ist der korrekte lineare Nullraum:**

$$
\boxed{\operatorname{Rad}(B_W|_{\mathcal{K}_{\rm phys}}):=\{a\in\mathcal{K}_{\rm phys}:B_W(a,b)=0\;\forall b\in\mathcal{K}_{\rm phys}\}.} \qquad (2\text{-Rad})
$$

$\operatorname{Rad}(B_W|_{\mathcal{K}_{\rm phys}})$ ist linear und für jede hermitesche Form (auch indefinit) quotientierbar.

**Verhältnis nach Positivität:** Falls $B_W|_{\mathcal{K}_{\rm phys}}\ge0$ bewiesen wird, folgt durch Cauchy-Schwarz:
$$
B_W(a,a)=0\Longrightarrow B_W(a,b)=0\;\forall b,
$$
also $\{B_W(a,a)=0\}=\operatorname{Rad}(B_W|_{\mathcal{K}_{\rm phys}})$ nachträglich. Aber das darf nicht vorausgesetzt werden.

$$
\boxed{\text{Radikal quotientieren: erlaubt vor Positivität. Nullnormquotient: nur nach Positivität.}} \qquad (2\text{-Rule})
$$

---

## 3. M4-A — Kanonische Hilbertmajorante

**Frage:** Existiert aus der adelischen/arithmetischen Struktur kanonisch ein positives inneres Produkt $\langle\cdot,\cdot\rangle_0$ mit
$$
\boxed{B_W(a,b)=\langle a,A_Xb\rangle_0\,?} \qquad (3\text{-AX})
$$

**Anforderungen:** $\langle\cdot,\cdot\rangle_0$ muss aus der Struktur von Objekt X selbst kommen (adelisch, archimedisch-endlich), nicht post hoc gewählt.

**Zwei Fälle explizit getrennt:**

**Fall 1 — Beschränktheit (Riesz):** Falls
$$
|B_W(a,b)|\le C\|a\|_0\|b\|_0,
$$
dann liefert der Riesz-Darstellungssatz auf dem Hilbert-Abschluss $\overline{\mathcal{A}_{\rm PW}}^0$ unmittelbar einen **beschränkten** selbstadjungierten Operator $A_X$.

**Fall 2 — Abschließbarkeit (kein direkter Riesz):** Falls Beschränktheit scheitert, muss separat gezeigt werden:
$$
\boxed{\text{Dichtheit des Def.-Bereichs}\to\text{Symmetrie}\to\text{Abschließbarkeit}\to\text{selbstadjungierte Realisierung}.} \qquad (3\text{-Chain})
$$
Keine Abkürzung erlaubt; dieser Weg ist aus früheren NEU-220-Strängen bekannt.

**Kandidaten aus dem Repo:**
- NEU-220e: Semifinite Spur $\tau$ als mögliche Prä-Geometrie
- NEU-220m/n: Rigged-Operator, Randkanäle
- NEU-220w: Hankelvollständigkeit, Moment-GNS
- NEU-221: Adelische Momentquelle

$$
\text{M4-A}\quad?[O] \qquad (3\text{-status})
$$

---

## 4. M4-B — Signatur-Firewall

$$
\boxed{\text{M4-B: nicht negative Richtungen suchen, sondern Signatur-Firewall festhalten.}} \qquad (4\text{-Scope})
$$

**Signatur-Firewall** (erst präzise nach M4-A mit Realisierungsoperator $A_X$):
$$
\boxed{\mathcal{H}_-\neq0\iff\exists a:B_W(a,a)<0\iff\neg\text{RH}.} \qquad (4\text{-Fire})
$$

**Warum kein Gegenbeispiel planen:**

Ein einziges explizites $a\in\mathcal{A}_{\rm PW}$ mit $B_W(a,a)<0$ wäre nach NEU-220l (PD5a2b) kein normaler Zwischenschritt, sondern ein **Beweis, dass RH falsch ist**. Das kann nicht als geplanter M4-Schritt behandelt werden.

**Was RH-frei untersuchbar ist:**

Teilblöcke können separat Vorzeichen-unbestimmt sein (insbesondere archimedischer Rohblock, vgl. NEU-220d/e). Daraus folgt nicht, dass die vollständige Form $B_W$ negative Richtungen besitzt. Kompensationen zwischen den Blöcken sind möglich.

$$
\text{M4-B}\quad?[O]\text{ (nach M4-A)} \qquad (4\text{-status})
$$

---

## 5. M4-C — Arithmetischer Constraint

**Frage:** Gibt es unabhängig von RH einen kanonischen BC/Hecke/adelischen Unterraum
$$
\mathcal{K}_{\rm phys}\subseteq H_0
$$
aus arithmetischer Struktur, auf dem die negativen Richtungen von $B_W$ verschwinden?

**Korrekter Quotient:**
$$
\boxed{\mathcal{K}_{\rm phys}/\operatorname{Rad}(B_W|_{\mathcal{K}_{\rm phys}}).} \qquad (5\text{-Quot})
$$

$\mathcal{K}_{\rm phys}$ soll aus arithmetischer/adelischer Struktur emergieren (z.B. Adelbedingung, Hecke-Kompatibilität, Periodizität), nicht post hoc gewählt werden. Noch keine Positivität voraussetzen.

$$
\text{M4-C}\quad?[O] \qquad (5\text{-status})
$$

---

## 6. M4-D — Positivitätstest

$$
\boxed{B_W|_{\mathcal{K}_X}\ge0\quad\text{ohne RH als Voraussetzung?}} \qquad (6\text{-Test})
$$

**Firewall:** M4-D nicht vor M4-C. GNS-Abschluss $\mathcal{H}_{\mathfrak{W}}$ zur Hilbert-Vervollständigung erst nach $B_W\ge0$; Radikal-Quotient $\mathcal{K}_{\rm phys}/\operatorname{Rad}(B_W|_{\mathcal{K}_{\rm phys}})$ ist RH-frei erlaubt. Positivität via RH als Prämisse wäre zirkulär.

$$
\boxed{\text{Gelingt M4-D ohne RH: zentraler Objekt-X-Mechanismus.}} \qquad (6\text{-Central})
$$

$$
\text{M4-D}\quad?[O] \qquad (6\text{-status})
$$

---

## 7. Bearbeitungsreihenfolge

$$
\boxed{\text{M4-A}\to\text{M4-B}\to\text{M4-C}\to\text{M4-D.}} \qquad (7\text{-Order})
$$

---

## 8. Statusbuchungen

$$\mathcal{N}:=\{B_W(a,a)=0\}\text{ als Quotient}\quad\times[M]\;(\text{isotroper Kegel, nicht linear}) \qquad (8\text{-a})$$

$$\operatorname{Rad}(B_W|_{\mathcal{K}_{\rm phys}})=\{a:B_W(a,b)=0\;\forall b\}\text{ korrekt, linear, quotientierbar}\quad\checkmark[K/M] \qquad (8\text{-b})$$

$$\text{Gegenbeispiel }B_W(a,a)<0\text{ als M4-Schritt}\quad\times[M]\;(\text{wäre Widerlegung RH}) \qquad (8\text{-c})$$

$$\mathcal{H}_-\neq0\iff\neg\text{RH}\;(\text{Signatur-Firewall})\quad\checkmark[K/M] \qquad (8\text{-d})$$

$$\text{M4-A: Beschränktheit (Riesz) vs. Abschließbarkeit explizit getrennt}\quad\checkmark[K/M] \qquad (8\text{-e})$$

$$\text{M4 gesamt}\quad?[O] \qquad (8\text{-M4})$$

---

## 9. Abhängigkeiten

| Referenz | SHA | Relevanz für M4 |
|---|---|---|
| NEU-252 M3 (Patch) | 4ee78ed | $B_W$ hermitesch, $B_W^{\rm adel}$ |
| NEU-220l | 1dc07b3 | $B_W\ge0\Leftrightarrow$ RH; Positivitäts-Firewall |
| NEU-220m | abf3c12 | Rigged-Operator; Randkanäle |
| NEU-220s | 7c1a3f9 | Kreinraum-Klassifikation; Off-Axis-Trägheit |
| NEU-220t | d8b2e51 | Metrikblock; Similarity-NoGo |
| NEU-220e | 9a1f3c2 | Semifinite Spur $\tau$ |
| NEU-220w | bf4e601 | Hankelvollständigkeit; Moment-GNS |
| NEU-221 | 8c3d412 | Adelische Momentquelle |
| NEU-250r (Patch) | bd1c0ab | Surjektiver Port; $\mathcal{S}_{\rm adel}^{\rm amp}$ |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch 2026-08-07: $\mathcal{N}=\{B_W(a,a)=0\}$ $\times[M]$ $\to$ $\operatorname{Rad}$; Signatur-Firewall; M4-A Beschränktheit/Abschließbarkeit getrennt.*
