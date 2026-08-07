# NEU-260 — Kanonizitätsaudit der Suzuki-Grenzdaten und adelischen Übergangsstruktur

**Katalog-ID:** NEU-260  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** Vier atomare Teilknoten zur Kanonisierung der Suzuki-Grenzdaten durch BC/KMS/Hecke/Adelen. Erste Stelle, wo das Programm über Suzuki 2026 hinausgeht.  
**Vorgänger:** NEU-259 (final $\checkmark$), NEU-258 $\checkmark$, NEU-250-Serie  

---

## 0. Klassifikation der Grenzdaten

| Datum | Charakter | Teilknoten |
|---|---|---|
| $\lambda(a)<\lambda_a$ | Formtopologie weitgehend **Gauge**; Spektralinvarianz offen | **NEU-260a** |
| $\theta(a)\in[0,2\pi)$ | **Echtes Selektionsdatum** ($S^1$-Familie, Defizit $(1,1)$) | **NEU-260b** |
| $\phi(a,z)$ | **Echtes Grenznormierungsproblem** | **NEU-260c** |
| $J_{a,b}$ | **Eigene Objekt-X-Geometrie** (nicht in Suzukis Vermutung) | **NEU-260d** |

**Wo das Programm über Suzuki hinausgeht:**

$$
\boxed{\text{Suzuki stellt RH-frei endliche Operatoren bereit und vermutet den richtigen Grenzwert.}}
$$
$$
\boxed{\text{Objekt X erklärt, warum genau eine Familie }\theta(a)\text{ gewählt wird und warum die endlichen Geometrien global kompatibel sind.}} \qquad (0\text{-ObjX})
$$

**Strategische Kette:**
$$
\boxed{\underbrace{\text{BC/KMS/Hecke}}_{\text{arithm. Struktur}}\xrightarrow{\theta(a),\,\phi(a,z),\,J_{a,b}}\underbrace{\{\mathcal{H}(T_a),\overline{\mathscr{D}}_{a,\theta(a)},J_{a,b}\}_{a<b}}_{\text{Objekt X}}\xrightarrow{\text{RH}}\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma).} \qquad (0\text{-Chain})
$$

---

## Teilknoten

- **NEU-260a** — $\lambda$-Gauge-Audit: `NEU-260a_Lambda-Gauge-Audit.md`
- **NEU-260b** — $\theta$-Selektionsaudit: `NEU-260b_Theta-Selektion.md` $\;?[O]$
- **NEU-260c** — Grenznormalisierung $\phi(a,z)$: `NEU-260c_Grenznormalisierung.md` $\;?[O]$
- **NEU-260d** — $J_{a,b}$-Audit: `NEU-260d_Jab-Geometrie.md` $\;?[O]$

---

## Statusbuchungen

$$\lambda\text{-Gauge: }\mathcal{H}(T_{a,\lambda_1})\cong\mathcal{H}(T_{a,\lambda_2})\quad\checkmark[K/M]\to\text{NEU-260a}\qquad(S\text{-a})$$
$$\sigma(\overline{\mathscr{D}}_{a,\theta}^{(\lambda_1)})\stackrel{?}{=}\sigma(\overline{\mathscr{D}}_{a,\theta'}^{(\lambda_2)})\quad?[O]\to\text{NEU-260a}\qquad(S\text{-b})$$
$$\theta(a)\text{-Selektion aus BC/KMS/Frobenius}\quad?[O]\to\text{NEU-260b}\qquad(S\text{-c})$$
$$\phi(a,z)\text{-Normalisierung}\quad?[O]\to\text{NEU-260c}\qquad(S\text{-d})$$
$$J_{a,b}\text{ kanonisch + Intertwining}\quad?[O]\to\text{NEU-260d}\qquad(S\text{-e})$$

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Gibt NEU-260a–d frei.*
