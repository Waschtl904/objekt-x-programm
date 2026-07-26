# NEU-220t — Metrikblock-Klassifikation, Off-Axis-Trägheit und Similarity-No-Go

**Katalog-ID:** NEU-220t
**Knoten:** [O-220-1-PD5a3f7-metric-block-classification]
**Vorgänger:** NEU-220s rev.2 (Commit 11aa74c) — RH-freies Krein-Modell ✓[K/M]_part
**Status:** ✓[K/M]_part (PD5a3f7a–g) / ?[O] (nichttautologisches adelisches Spektralmodell)

---

## Strategischer Befund

$$
\boxed{\text{Die negative Richtung eines off-axis-Paares ist kein Artefakt der Wahl von }\mathscr{J}_\kappa\text{; sie ist für jede zulässige invertierbare Metrik invariant.}}
$$

Damit ist der Forschungsweg
$$
\mathscr{J}_\kappa \longrightarrow \text{nichtlokale Korrektur} \longrightarrow \eta>0
$$
**gesperrt**, solange die Metrikgleichung \(Z_{\mathcal{Z}}^*\eta = \eta Z_{\mathcal{Z}}\) erhalten bleibt.

---

## PD5a3f7a — Multiplizitätskonvention ✓[K/M]

Katalogstandard (seit NEU-220s rev.2):

$$
\mathcal{H}_{\mathcal{Z}} = \ell^2(\mathcal{Z}_{\mathrm{dist}},m), \qquad \|c\|^2 = \sum_{\rho\in\mathcal{Z}_{\mathrm{dist}}} m_\rho|c_\rho|^2.
$$

In der gewichteten Konvention erzeugt jedes verschiedene off-axis-κ-Paar **eine** negative Richtung; m_ρ erscheint als Gewicht, nicht als Faserdimension.

In der alternativen Multimengenrealisierung \(\ell^2(\widetilde{\mathcal{Z}})\) erzeugt ein off-axis-Paar m_ρ negative Richtungen — inhaltlich äquivalent, konventionell verschieden.

---

## PD5a3f7b — (\(\overline{\lambda_\rho}-\lambda_\sigma)\eta_{\rho\sigma}=0\) ✓[M]

In der normierten atomaren Basis: η_{ρσ} = ⟨e_ρ, η e_σ⟩. Aus \(Z_{\mathcal{Z}}^*\eta = \eta Z_{\mathcal{Z}}\):

$$
\boxed{\bigl(\overline{\lambda_\rho}-\lambda_\sigma\bigr)\eta_{\rho\sigma}=0.}
$$

**Herleitung:** \(Z_{\mathcal{Z}}e_\rho = \lambda_\rho e_\rho\) und \(Z_{\mathcal{Z}}^*e_\rho = \overline{\lambda_\rho}e_\rho\) liefern

$$
\langle e_\rho, Z_{\mathcal{Z}}^*\eta e_\sigma\rangle = \overline{\lambda_\rho}\,\eta_{\rho\sigma}, \qquad
\langle e_\rho, \eta Z_{\mathcal{Z}}e_\sigma\rangle = \lambda_\sigma\,\eta_{\rho\sigma}.
$$

Gleichsetzen gibt die Behauptung.

---

## PD5a3f7c — Vollständige κ-Orbitzerlegung ✓[M]

Da \(\lambda_{\kappa\rho} = \overline{\lambda_\rho}\), darf \(\eta_{\rho\sigma} \ne 0\) nur gelten, wenn \(\lambda_\sigma = \overline{\lambda_\rho}\):

- **Diagonal:** σ = ρ nur wenn λ_ρ ∈ ℝ, d.h. β_ρ = 1/2
- **Off-diagonal:** σ = κρ im off-axis-Fall
- **Entartung:** σ = ρ' nur bei echter Entartung λ_{ρ'} = λ̄_ρ

$$
\boxed{\text{Die Metrikgleichung zerfällt vollständig in die }\kappa\text{-Orbits.}}
$$

Nichtlokale Kopplungen zwischen verschiedenen, nichtenttarteten Nullstellenpaaren können die off-axis-Indefinitheit **nicht** beseitigen.

---

## PD5a3f7d — Trägheit jedes off-axis-Blocks ✓[M]

Betrachte ein einfaches off-axis-Paar \(\{\rho,\kappa\rho\}\), \(\rho\ne\kappa\rho\). In der Basis \((e_\rho, e_{\kappa\rho})\) hat jede selbstadjungierte Lösung der Metrikgleichung die Form

$$
\boxed{\eta_{\{\rho,\kappa\rho\}} = \begin{pmatrix}0&\alpha\\ \overline{\alpha}&0\end{pmatrix}.}
$$

Die Diagonaleinträge verschwinden, weil \(\lambda_\rho \notin \mathbb{R}\). Eigenwerte: \(|\alpha|\) und \(-|\alpha|\).

- \(\alpha \ne 0\): Block invertierbar, aber **indefinit** (Sylvester-Trägheit: eine positive, eine negative Richtung)
- \(\alpha = 0\): positiv semidefinit, aber vollständig **degeneriert**

**Ein positiver, invertierbarer Block existiert nicht.**

**Höhere Multiplizität** (Faserrealisierung \(\mathbb{C}^m \oplus \mathbb{C}^m\)):

$$
\eta_{\mathrm{pair}} = \begin{pmatrix}0&A\\A^*&0\end{pmatrix}.
$$

Ist A invertierbar: genau m positive und m negative Eigenwerte. Interne Mischung entfernt die Indefinitheit nicht.

$$
\boxed{\text{Jedes off-axis-Paar erzwingt eine negative Metrikrichtung.}}
$$

Der kanonische Block \(J_\kappa = \bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)\) ist nicht bloß eine bequeme Wahl. Seine Signatur ist für jede invertierbare hermitesche Metrikantwort unvermeidbar.

---

## PD5a3f7e — Positivitäts- und Nichtausgeartetheits-No-go ✓[M]

**Stärkeres No-go:** Sei \(\eta \ge 0\) (ohne Invertierbarkeit). Für eine off-axis-Nullstelle ρ folgt aus der Metrikgleichung \(\langle e_\rho, \eta e_\rho\rangle = 0\). Da \(\eta \ge 0\): \(\eta^{1/2}e_\rho = 0\), also \(\eta e_\rho = 0\).

$$
\boxed{\eta\ge0,\quad Z^*\eta=\eta Z\quad\Longrightarrow\quad \eta\text{ verschwindet auf allen off-axis-Eigenräumen.}}
$$

Eine positive nichtausgeartete Metrik existiert **genau dann**, wenn es keine off-axis-Nullstellen gibt.

Die RH-Äquivalenz wird damit **blockweise lokal** bewiesen:

$$
\boxed{\mathrm{RH}\iff\exists\,\eta\ge cI>0: Z_{\mathcal{Z}}^*\eta=\eta Z_{\mathcal{Z}}.}
$$

---

## PD5a3f7f — Bounded-similarity-Äquivalenz zu RH ✓[M]

Angenommen, es gibt \(\mathcal{H}_X\), \(A_X = A_X^*\) und beschränkt invertierbares \(U:\mathcal{H}_X\to\mathcal{H}_{\mathcal{Z}}\) mit \(Z_{\mathcal{Z}}U = UA_X\). Dann ist \(\eta = (U^{-1})^*U^{-1}\) positiv, beschränkt invertierbar, und \(Z_{\mathcal{Z}}^*\eta = \eta Z_{\mathcal{Z}}\). Unter RH: \(A_X = Z_{\mathcal{Z}}\), \(U = I\).

$$
\boxed{\mathrm{RH}\iff Z_{\mathcal{Z}}\text{ ist durch eine beschränkte Ähnlichkeit zu einem selbstadjungierten Operator transformierbar.}}
$$

Das entspricht dem **quasi-hermiteschen Rahmen** (Scholtz–Geyer–Hahne 1992; Mostafazadeh 2002): Ein beschränkter quasi-hermitescher Operator mit beschränkt invertierbarer positiver Metrik ist genau dann zu einem selbstadjungierten Operator ähnlich.

---

## PD5a3f7g — Export: Anforderungen an das nichttautologische adelische Spektralmodell ✓[M] / ?[O]

Die Klassifikation sperrt den naiven Weg \(\mathscr{J}_\kappa \to\) nichtlokale Korrektur \(\to\,\eta>0\), solange die Metrikgleichung erhalten bleibt.

$$
\boxed{\text{Eine positive adelische Metrik konstruiert nicht nur RH; ihre lokale Existenz schließt jedes off-axis-Paar unmittelbar aus.}}
$$

**Revidierter adelischer Auftrag ?[O]:**

$$
\boxed{\begin{gathered}
\text{Konstruiere zunächst aus der adelischen Architektur einen}\\
\text{positiven Spektralraum }(\mathcal{H}_X, A_X=A_X^*)\\
\text{ohne Verwendung der Nullstellenlage,}
\end{gathered}}
$$

und beweise anschließend über eine Spur-, Determinanten- oder Streuidentität, dass seine spektrale Determinante \(\xi\) ist. Erst danach Identifikation mit \((\mathcal{H}_{\mathcal{Z}}, Z_{\mathcal{Z}})\).

Das stimmt mit der bekannten Situation überein, dass de-Branges-artige Modelle unter RH konstruierbar sind, ihre Positivität aber die entscheidende Voraussetzung bleibt.

---

## Knotentabelle

| Teilaufgabe | Inhalt | Status |
|---|---|---|
| PD5a3f7a | Multiplizitätskonvention Z_dist vs. Multimenge; Doppelzählung ausgeschlossen | ✓[K/M] |
| PD5a3f7b | (λ̄_ρ − λ_σ)η_{ρσ}=0; Kopplung nur bei konjugierten λ-Werten | ✓[M] |
| PD5a3f7c | Vollständige κ-Orbitzerlegung; keine nichtlokale Mischung möglich | ✓[M] |
| PD5a3f7d | Trägheit des off-axis-Blocks; höhere Multiplizität m_ρ erzeugt m_ρ neg. Richtungen | ✓[M] |
| PD5a3f7e | Positivitäts-No-go; positive Metrik annihiliert off-axis-Kanäle; RH ⟺ ∃η≥cI | ✓[M] |
| PD5a3f7f | Bounded-similarity-Äquivalenz; quasi-hermitischer Rahmen (Scholtz–Mostafazadeh) | ✓[M] |
| PD5a3f7g | Nichtlokales Mischen gesperrt; adelischer Auftrag: (H_X, A_X) ohne Nullstellenvorannahme | ✓[M] / ?[O] |

```
[O-220-1-PD5a3f7-metric-block-classification]
  -> ✓[K/M]_part  (PD5a3f7a-g abgeschlossen)
  -> ?[O]          (PD5a3f7g: adelisches positives Spektralmodell ohne Nullstellentautologie)
```

---

## Gesamtbilanz NEU-220m bis NEU-220t

| Schicht | Inhalt | Status |
|---|---|---|
| Testfunktionsform | W hermitesch, Typklassifikation | ✓[K/M] |
| Pol–Prim-Renormierung | K_pf = ν₊ + ν̌₊ + e^{−|x|/2}dx | ✓[M] |
| Temperiertes Kriterium | K_W ∈ S' ⟺ RH | ✓[K/M] |
| Bedingtes Spektralmodell | H_Z = L²(μ_Z) unter RH | ✓[K/M], konditional |
| RH-freier Kreinraum | H_Z, J_κ, W = [E_Z·, E_Z·]_κ | ✓[K/M] |
| RH-Reformulierungen | B_Z=0; Hilbert-s.a.; ∃η≥cI | ✓[M] |
| Metrikblock-Klassifikation | κ-Orbitzerlegung; off-axis-Trägheit; No-go | ✓[M] |
| Bounded-similarity | RH ⟺ beschränkte Ähnlichkeit; quasi-hermitisch | ✓[M] |
| Adelisches positives Spektralmodell | (H_X, A_X) ohne Nullstellenvorannahme | ?[O], RH-stark |

---

## Abhängigkeiten

| Referenz | Inhalt |
|---|---|
| NEU-220s rev.2 (11aa74c) | Kreinraum, J_κ, E_Z, Z_Z |
| NEU-220r (fce7b62) | Bedingtes Spektralmodell L²(μ_Z) |
| NEU-220q (ed81836) | Pol–Prim-Renormierung |
| Scholtz–Geyer–Hahne (1992) | Quasi-hermitische QM, beschränkte Metrik |
| Mostafazadeh (2002) | Pseudo-hermitische Operatoren, bounded similarity |
| Bognar (1974) | Kreinräume, Fundamentalsymmetrie |
| Connes (1999) | BC-Kern, adelischer Rahmen |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
