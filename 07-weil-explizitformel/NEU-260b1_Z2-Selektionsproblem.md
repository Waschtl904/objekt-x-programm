# NEU-260b.1 — $\mathbb{Z}_2$-Selektionsproblem: $(+P)$ vs. $(-P)$

**Katalog-ID:** NEU-260b.1  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-08 (Patch: 2026-08-08b)  
**Patch:** Stetigkeitsargument als reine Propagation zurückgestuft; analytische Familie-Behauptung gestrichen; KMS-Kandidat als typisierungsunvollständig markiert; Frobenius-Konventionsproblem notiert. Stattdessen: NEU-260b.2 als stärkster analytischer Kandidat freigeschaltet.

---

## 0. Was wir haben

**Gesichert (NEU-260b $\checkmark[K/M]$):**
$$
\boxed{U_a^X = \varepsilon(a)\cdot P|_{\mathcal{N}_{+,a}}, \qquad \varepsilon(a)\in\{+1,-1\}.} \qquad (0\text{-Form})
$$
In Suzuki-Trivialisierung: $\varepsilon=+1\leftrightarrow\theta=0$, $\varepsilon=-1\leftrightarrow\theta=\pi$.

---

## 1. Kandidat I: Stetigkeitsargument — nur Propagation, keine Selektion $\times[M]$

Es stimmt: Ein stetiges $\varepsilon:(0,\infty)\to\{+1,-1\}$ ist konstant. Aber sowohl $\varepsilon\equiv+1$ als auch $\varepsilon\equiv-1$ sind stetig. **Stetigkeit kann niemals zwischen den zwei Zweigen wählen**, sondern nur eine anderweitig erfolgte Auswahl bei einem Referenzpunkt $a_0$ global fortsetzen.

$$
\boxed{\text{Stetigkeitsargument: Propagation, keine Selektion.}\quad\times[M]\text{ als Selektionsmechanismus.}} \qquad (1\text{-Prop})
$$

**Gestrichene Behauptung:** "für kleine $a$, wo die Erweiterung analytisch in $a$ ist" --- Suzuki beweist Stetigkeit von $\lambda_a$, aber keine bereits konstruierte analytische Familie ausgewählter selbstadjungierter Erweiterungen. Zu streichen bis Quelle vorliegt.

$$
\text{Analytische Familie ausgewählter sa. Erweiterungen: nicht in Suzuki, keine Quelle.}\quad?[O] \qquad (1\text{-Analytic})
$$

---

## 2. Kandidat II: Parität + Suzuki-Grenzstruktur — stärkster Kandidat

Dieser Kandidat wird vollständig in **NEU-260b.2** entwickelt.

Kernaussage (Vorschau):
$$
\boxed{\text{Suzuki-Grenzrelation + Paritätsreduktion }\Longrightarrow\varepsilon(a)=+1\text{ für hinreichend großes }a.} \qquad (2\text{-Preview})
$$

Dieser Schluss ist konditional auf Suzukis Grenzrelation (die ihrerseits offen ist und RH implizieren würde). Er beweist weder die Grenzrelation noch RH. Aber er zeigt: Falls der Suzuki-Grenzmechanismus der richtige ist, ist der $\mathbb{Z}_2$-Zweig nicht frei.

$$
\text{Priorität: NEU-260b.2 bearbeiten.}\quad\to\text{NEU-260b.2} \qquad (2\text{-Prio})
$$

---

## 3. Kandidat III: BC/KMS-Zeitpfeil — Typisierungslücke $?[O]$

Ein BC-System $(\mathcal{A}_{\rm BC},\sigma_t)$ ist eine $C^*$-Algebra mit Einparametergruppe $(\sigma_t)_{t\in\mathbb{R}}$. Positive und negative Zeiten gehören beide zur Struktur. Die KMS-Bedingung beschreibt Gleichgewichtszustände; sie liefert **keinen automatischen Mechanismus**
$$
\{\text{BC/KMS-Datum}\}\longrightarrow\{+1,-1\}.
$$

Uns fehlt vollständig die typisierte Brücke:
$$
\boxed{\text{BC/KMS-Datum}\longrightarrow\operatorname{Hom}_{\rm unitary}(\mathcal{N}_{+,a},\mathcal{N}_{-,a})\quad\text{fehlt.}\quad?[O]} \qquad (3\text{-Gap})
$$

Der KMS-Kandidat bleibt interessant (der Hamiltonoperator $H$ mit $\log n$-Energien hat arithmetische Kanonizität), aber die Aussage "KMS-Vorwärtszeit $=+1$" ist Motivation, kein Satz. Erst eine explizite Wirkung auf $\mathcal{N}_{\pm,a}$ würde daraus Mathematik.

$$
\text{KMS-Kandidat: interessant, aber typisierungsunvollständig.}\quad?[O] \qquad (3\text{-Status})
$$

---

## 4. Kandidat IV: Frobenius-Orientierung — Konventionsproblem $?[O]$

"Arithmetischer" und "geometrischer" Frobenius sind inverse Standardkonventionen ($\mathrm{Frob}_p x=x^p$ arithmetisch, $x\mapsto x^{1/p}$ geometrisch). Solange keine explizite Wirkung
$$
\mathrm{Frob}_p^{(\pm)}: \mathcal{N}_{+,a}\longrightarrow\mathcal{N}_{-,a}
$$
konstruiert ist, bleibt das Vorzeichen $\varepsilon_{\rm Frob}\in\{+1,-1\}$ konventionsabhängig.

$$
\text{Frobenius-Kandidat: Konventionsproblem unaufgelöst; keine explizite Wirkung auf }\mathcal{N}_{\pm,a}.\quad?[O] \qquad (4\text{-Frob})
$$

---

## 5. Priorisierung

| Kandidat | Status | Urteil |
|---|---|---|
| Stetigkeitsargument | Nur Propagation, keine Selektion | $\times[M]$ als Selektor |
| **Parität + Suzuki-Grenzstruktur** | $\varepsilon=+1$ für gr. $a$ konditional auf Grenzrelation | **stärkster Kandidat** $\to$ NEU-260b.2 |
| KMS-Zeitpfeil | Typisierungslücke offen | $?[O]$ |
| Frobenius-Orientierung | Konventionsproblem | $?[O]$ |
| Adel./Weil-Gruppe | Hypothese | $?[O]$ |

---

## 6. Statusbuchungen

$$\varepsilon\text{ stetig }\Rightarrow\varepsilon=\text{const: stimmt, aber keine Selektion}\quad\times[M]\qquad(6\text{-a})$$
$$\text{Analytische Familie aus Suzuki: keine Quelle}\quad?[O]\qquad(6\text{-b})$$
$$\text{BC/KMS-Datum}\to\operatorname{Hom}_{\rm unitary}(\mathcal{N}_+,\mathcal{N}_-)\text{: Brücke fehlt}\quad?[O]\qquad(6\text{-c})$$
$$\text{Frobenius arith/geom: Konventionsproblem}\quad?[O]\qquad(6\text{-d})$$
$$\varepsilon=+1\text{ für gr. }a\text{ aus Suzuki-Grenzrelation (konditional)}\quad?[O]\to\text{NEU-260b.2}\qquad(6\text{-e})$$

---

*Patch 2026-08-08b. Gibt NEU-260b.2 frei.*
