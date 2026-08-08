# NEU-260b.1 — $\mathbb{Z}_2$-Selektionsproblem: $(+P)$ vs. $(-P)$

**Katalog-ID:** NEU-260b.1  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-08  
**Auftrag:** Selektion $\varepsilon(a)\in\{+1,-1\}$ im von-Neumann-Parameter $U_a^X=\varepsilon(a)\cdot P|_{\mathcal{N}_{+,a}}$. Suzuki + Weil-Parität liefern Reduktion $U(1)\to\mathbb{Z}_2$ (NEU-260b $\checkmark[K/M]$). Gesucht: arithmetischer Mechanismus für $\varepsilon(a)$.

---

## 0. Was wir haben und was fehlt

**Gesichert (NEU-260b $\checkmark[K/M]$):**
$$
\boxed{U_a^X = \varepsilon(a)\cdot P|_{\mathcal{N}_{+,a}}, \qquad \varepsilon(a)\in\{+1,-1\}.} \qquad (0\text{-Form})
$$

In Suzuki-Trivialisierung ($T_av_\pm=e^{\pm x}$):
- $\varepsilon(a)=+1 \leftrightarrow \theta(a)=0$
- $\varepsilon(a)=-1 \leftrightarrow \theta(a)=\pi$

**Suzuki-Grenzkonjektur:** $W(a,\theta(a);z)\to z^2\xi(1/2-iz)/\xi'(1/2-iz)$ für $a\to\infty$. Suzuki formuliert dies für einen (bisher nicht explizit fixierten) $\theta$-Zweig.

**Offene Frage:**
$$
\boxed{\text{Was wählt }\varepsilon(a)\text{? Ist }\varepsilon(a)=+1\text{ für alle }a>0, \text{ oder ist }\varepsilon(a)\text{ ein arithmetisches Datum?}} \qquad (0\text{-Q})
$$

---

## 1. Kandidat I: Globale Kompatibilität / Grenzwert-Konsistenz

### 1.1 Konstanzargument

Falls $\varepsilon:(0,\infty)\to\{+1,-1\}$ stetig wäre und für kleine $a$ (wo die Erweiterung analytisch in $a$ ist) auf einem Wert liegt, ist $\varepsilon(a)=\text{const}$ auf jeder Zusammenhangskomponente.

**Frage:** Ist $a\mapsto U_a^X$ stetig (in einem geeigneten Sinn) und $\varepsilon(a)$ deswegen konstant?

$$
\varepsilon\text{ global konstant aus Stetigkeitsargument}\quad?[O] \qquad (1\text{-Const})
$$

### 1.2 Grenzwert-Konsistenz

Falls der Grenzwert
$$
\lim_{a\to\infty} W(a,\theta(a);z) = \frac{z^2\xi(1/2-iz)}{\xi'(1/2-iz)}
$$
nur für $\theta=0$ (und nicht $\theta=\pi$) Nullstellen genau auf der kritischen Geraden hat, wäre $\varepsilon(a)=+1$ aus der Grenzfunktion erzwungen.

$$
\varepsilon(a)=+1\text{ aus Grenzwert-Konsistenz (nur }\theta=0\text{ korrekte Nullstellenlage)}\quad?[O] \qquad (1\text{-Limit})
$$

**Wichtig:** $(1\text{-Limit})$ wäre RH-konditional, wenn die Nullstellen-auf-kritischer-Geraden-Eigenschaft nur unter RH gilt. Muss sorgfältig separiert werden.

---

## 2. Kandidat II: BC/Adelen-Orientierung

### 2.1 Fragestellung

Die BC/adelische Struktur trägt eine natürliche Orientierung (z.B. aus dem Vorzeichen der KMS-Zeitentwicklung, der modularen Involution, oder der Frobenius-Orientierung $\mathrm{Frob}_p$ vs. $\mathrm{Frob}_p^{-1}$).

Frage: Induziert diese Orientierung ein kanonisches $\varepsilon_{\rm BC}\in\{+1,-1\}$?

$$
\boxed{\varepsilon_{\rm BC}\in\{+1,-1\}\text{ aus BC/adelischer Orientierung}\quad?[O]} \qquad (2\text{-BC})
$$

### 2.2 Konkrete Quelle: KMS-Zeitpfeil

Die KMS-Bedingung bei inverser Temperatur $\beta$ definiert einen Zeitpfeil: $\sigma_t(a)=e^{itH}ae^{-itH}$ für $t>0$ (Vorwärtsentwicklung). Dieser Zeitpfeil ist mit einem $\mathbb{Z}_2$-Vorzeichen assoziiert (Vorwärts vs. Rückwärts).

Falls $\varepsilon_{\rm BC}=+1$ der Vorwärtsentwicklung entspricht, wäre $\theta_{\rm can}(a)=0$ KMS-kanonisch.

$$
\varepsilon_{\rm BC}=+1\leftrightarrow\text{KMS-Vorwärtszeitpfeil}\quad?[O] \qquad (2\text{-KMS})
$$

### 2.3 Konkrete Quelle: Frobenius-Orientierung

Für jede Primzahl $p$ hat $\mathrm{Frob}_p$ eine kanonische Richtung (arithmetische Normierung: $\mathrm{Frob}_p x = x^p$ auf dem Residuenkörper). Das Vorzeichen $\varepsilon_p\in\{+1,-1\}$ könnte global ein $\varepsilon(a)$ induzieren.

$$
\varepsilon(a)\text{ aus Frobenius-Orientierung}\quad?[O] \qquad (2\text{-Frob})
$$

---

## 3. Kandidat III: Adelische Orientierung / Weil-Gruppe

### 3.1 Éléments d'analyse

Die Weil-Gruppe $W_\mathbb{Q}$ hat eine kanonische Orientierung (Artin-Reziprozitätsabbildung). Ob diese auf den Defizienzraum $\mathcal{N}_{+,a}$ wirkt und ein Vorzeichen induziert:

$$
\varepsilon(a)\text{ aus Weil-Gruppenorientierung}\quad?[O] \qquad (3\text{-Weil})
$$

---

## 4. Strategische Einschätzung

**Stärkster Kandidat (kurzfristig):** $(1\text{-Const})$ --- Stetigkeitsargument liefert $\varepsilon=\text{const}$ ohne Arithmetik. Falls $\varepsilon(a_0)=+1$ für ein explizit berechenbares $a_0$, folgt $\varepsilon\equiv+1$ global.

**Stärkster Kandidat (langfristig/Objekt X):** $(2\text{-BC})$ --- BC/KMS-Zeitpfeil oder Frobenius-Orientierung wählt $\varepsilon$ kanonisch. Das wäre echter neuer Mechanismus, der über Suzuki hinausgeht.

**Schönstes Ergebnis:** Falls beide übereinstimmen ($\varepsilon_{\rm Suzuki}=\varepsilon_{\rm BC}=+1$), ist $\theta_{\rm can}(a)=0$ sowohl analytisch als auch arithmetisch ausgezeichnet.

$$
\boxed{\text{Nächster Schritt: Stetigkeitsargument für }\varepsilon\text{ prüfen; dann BC/KMS-Zeitpfeil-Kandidat.}} \qquad (4\text{-Next})
$$

---

## 5. Statusbuchungen

$$U_a^X=\varepsilon(a)P|_{\mathcal{N}_{+,a}},\;\varepsilon\in\{+1,-1\}\quad\checkmark[K/M]\text{ (von NEU-260b)}\qquad(5\text{-a})$$
$$\varepsilon(a)=+1\leftrightarrow\theta=0,\quad\varepsilon(a)=-1\leftrightarrow\theta=\pi\quad\checkmark[K/M]\qquad(5\text{-b})$$
$$\varepsilon\text{ global konstant aus Stetigkeitsargument}\quad?[O]\qquad(5\text{-c})$$
$$\varepsilon=+1\text{ aus Grenzwert-Konsistenz}\quad?[O]\qquad(5\text{-d})$$
$$\varepsilon_{\rm BC}\in\{+1,-1\}\text{ aus BC/KMS-Zeitpfeil}\quad?[O]\qquad(5\text{-e})$$
$$\varepsilon\text{ aus Frobenius-Orientierung}\quad?[O]\qquad(5\text{-f})$$
$$\varepsilon\text{ aus adelischer/Weil-Gruppenorientierung}\quad?[O]\qquad(5\text{-g})$$

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm.*  
*Erstellt 2026-08-08. Von NEU-260b freigegeben. Kernfrage: $\varepsilon(a)\in\{+1,-1\}$.*
