# NEU-220s rev.2 — Nullstellenpaar-Kreinraum, Off-Axis-Defekt und positive Metrik

**Katalog-ID:** NEU-220s rev.2
**Knoten:** [O-220-1-PD5a3f6-unconditional-zero-krein-model]
**Vorgänger:** NEU-220r (Commit fce7b62) — bedingtes Spektralmodell ✓[K/M]_part
**Status:** ✓[K/M]_part (PD5a3f6a–g) / ?[O] (adelische positive Metrik)
**Revision:** Multiplizitätskonvention präzisiert (Direktaudit 2026-07-26); Metrikpräzisierung aus NEU-220t

---

## Revision v1 → v2: Multiplizitätskonvention

NEU-220s v1 verwendete „Z ist die Multimenge der Nullstellen" zusammen mit einem Gewichtsfaktor m_ρ in der Norm — dies zählt Vielfachheiten doppelt. **Zwei Konventionen sind strikt zu trennen.**

### Kanonische gewichtete Konvention (Katalogstandard)

Sei Z_dist = {ρ : ξ(ρ)=0} die Menge der **verschiedenen** nichttrivialen Nullstellen und m_ρ = ord_{s=ρ} ξ(s). Dann:

$$
\boxed{\mathcal{H}_{\mathcal{Z}} = \ell^2(\mathcal{Z}_{\mathrm{dist}},m) = \left\{ c: \sum_{\rho\in\mathcal{Z}_{\mathrm{dist}}} m_\rho|c_\rho|^2<\infty \right\}.}
$$

Diese Variante ist kanonisch, vermeidet Doppelzählung und genügt für die Weil-Faktorisierung.

### Echte Multimengenkonvention (Alternative)

\(\widetilde{\mathcal{Z}} = \{(\rho,j): 1\le j\le m_\rho\}\), ungewichtetes \(\ell^2(\widetilde{\mathcal{Z}})\). Kein zusätzlicher Faktor m_ρ in der Norm. Benötigt eine Wahl der Kopien-Zuordnung unter κ.

**Im Katalog gilt durchgehend die erste (gewichtete) Konvention.**
Status v1 (Multimenge + Gewicht simultan): ✓[M]_neg (Doppelzählung).
Status rev.2 (Z_dist + Gewicht): ✓[K/M].

---

## PD5a3f6a — H_Z und κ ✓[K]

Sei Z_dist die Menge der verschiedenen nichttrivialen Nullstellen. Für ρ = β+iγ definiere die **horizontale Spiegelung**

$$
\kappa(\rho) := 1-\overline{\rho} = 1-\beta+i\gamma.
$$

Aus der Funktionalgleichung und der Konjugationssymmetrie folgt: κ erhält Z_dist einschließlich Vielfachheiten (m_{κρ} = m_ρ), und κ² = id.

$$
\boxed{\mathcal{H}_{\mathcal{Z}} = \ell^2(\mathcal{Z}_{\mathrm{dist}},m).}
$$

Dieser Raum ist **RH-frei**: kein Vorwissen über Re ρ erforderlich.

---

## PD5a3f6b — J_κ und Kreinblockzerlegung ✓[K/M]

Setze (J_κ c)(ρ) = c(κρ). Da m_{κρ} = m_ρ, ist J_κ unitär, selbstadjungiert und involutiv:

$$
\mathscr{J}_\kappa^* = \mathscr{J}_\kappa, \qquad \mathscr{J}_\kappa^2 = I.
$$

$$
\boxed{[c,d]_\kappa := \langle\mathscr{J}_\kappa c, d\rangle_{\mathcal{H}_{\mathcal{Z}}}}
$$

ist eine nichtausgeartete hermitesche **Kreinmetrik**.

| Nullstellentyp | κ-Wirkung | J_κ-Block | Vorzeichen |
|---|---|---|---|
| β = 1/2 (kritisch) | κρ = ρ | (+1) | positiv |
| Off-axis-Paar {ρ, κρ} | Vertauschung | (0 1 / 1 0) | eine neg. Richtung |

$$
\boxed{\mathrm{RH}\Longleftrightarrow\mathscr{J}_\kappa=I.}
$$

---

## PD5a3f6c — E_Z und Weil-Faktorisierung ✓[M]

M_a(s) = ∫ a(u) e^{(s−1/2)u} du. Definiere (E_Z a)(ρ) = M_a(ρ).

Paley–Wiener-Abfall + Nullstellendichte: E_Z : C_c^∞ → H_Z RH-frei wohldefiniert.

$$
\boxed{\mathfrak{W}(a,b) = [\mathcal{E}_{\mathcal{Z}}a,\mathcal{E}_{\mathcal{Z}}b]_\kappa.}
$$

Unter RH: J_κ = I, Krein kollabiert zu Hilbert (NEU-220r).

---

## PD5a3f6d — Z_Z Krein-selbstadjungiert ✓[K/M]

λ_ρ = (ρ−1/2)/i, (Z_Z c)(ρ) = λ_ρ c(ρ). Wegen λ_{κρ} = λ̄_ρ:

$$
\boxed{Z_{\mathcal{Z}}^*\mathscr{J}_\kappa = \mathscr{J}_\kappa Z_{\mathcal{Z}},}
\qquad
\boxed{\mathrm{RH}\iff Z_{\mathcal{Z}}\text{ Hilbert-selbstadjungiert.}}
$$

---

## PD5a3f6e — Z_Z = Γ_Z − iB_Z ✓[K/M]

(Γ_Z c)(ρ) = γ_ρ c(ρ), (B_Z c)(ρ) = (β_ρ − 1/2)c(ρ), ‖B_Z‖ ≤ 1/2.

J_κ Γ_Z = Γ_Z J_κ, J_κ B_Z = −B_Z J_κ.

$$
\boxed{\mathrm{RH}\iff B_{\mathcal{Z}}=0.}
$$

---

## PD5a3f6f — Z_Z E_Z = E_Z D ✓[M]

Partielle Integration: M_{Da}(s) = λ_s M_a(s).

$$
\boxed{Z_{\mathcal{Z}}\mathcal{E}_{\mathcal{Z}}=\mathcal{E}_{\mathcal{Z}}D.}
$$

Exakte RH-freie Intertwiningrelation. Lokalisiert den Typfehler des naiven Hilbert–Pólya-Ansatzes.

---

## PD5a3f6g — Positive Metrik η und RH-Äquivalenz ✓[M] / ?[O]

**Vollständige Anforderung (präzisiert durch NEU-220t-Audit):**
η ∈ B(H_Z), η = η*, η ≥ cI (c>0), η⁻¹ beschränkt,
η D(Z_Z) = D(Z_Z*), und Z_Z* η c = η Z_Z c auf D(Z_Z).

Bei unbeschränkten Metriken sind zusätzliche Domänenbedingungen unverzichtbar; die bloße symbolische Gleichung Z*η = ηZ genügt nicht.

$$
\boxed{\mathrm{RH}\iff\exists\,\eta\ge cI>0: Z_{\mathcal{Z}}^*\eta=\eta Z_{\mathcal{Z}}.}
$$

**Adelischer Auftrag ?[O]:** Konstruiere η aus der BC-/adelischen Architektur ohne Vorannahme über die Nullstellenlage. Präzisierung und vollständige Metrikblock-Klassifikation in NEU-220t (PD5a3f7).

---

## Knotentabelle

| Teilaufgabe | Inhalt | Status |
|---|---|---|
| PD5a3f6a | H_Z = ℓ²(Z_dist, m); κ-Symmetrie RH-frei | ✓[K] |
| PD5a3f6b | J_κ Fundamentalsymmetrie; Blockzerlegung; RH ⟺ J_κ=I | ✓[K/M] |
| PD5a3f6c | E_Z RH-frei; W = [E_Z·, E_Z·]_κ | ✓[M] |
| PD5a3f6d | Z_Z Krein-s.a.; RH ⟺ Hilbert-s.a. | ✓[K/M] |
| PD5a3f6e | Z_Z = Γ_Z − iB_Z; RH ⟺ B_Z = 0 | ✓[K/M] |
| PD5a3f6f | Z_Z E_Z = E_Z D; Typfehler lokalisiert | ✓[M] |
| PD5a3f6g | RH ⟺ ∃η≥cI; vollständige Domänenbedingung; adelische Konstruktion offen | ✓[M] / ?[O] |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
