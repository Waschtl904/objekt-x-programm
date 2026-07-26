# NEU-135.D — Entscheidung: Welt 2

> Stand: Juli 2026.  
> Grundlage: NEU-44 §5 (Formel 44.8), NEU-135.  
> **Entscheidung: Kein weiterer Normwechsel.**

---

## Entscheidungssatz

$$\boxed{\|\varepsilon_p\|^2 = 1.}$$

$\varepsilon_p$ ist in NEU-44 als nackter Primkanal-Basisvektor eingeführt, ohne Mangoldt-Gewichtung. Daher gilt:

$$\|C_p^{rel}\|^2 = \|\widetilde{\Psi}_p\|^2_{W_{res,rel}}.$$

Der $(\log p)^2$-Faktor kann **nicht** in der Kanalnorm verschwinden.

---

## Konsequenz: Fixierung von $A_p^{rel}$

$$A_p^{rel} := p\|C_p^{rel}\|^2 \sim p(\log p)^2 R_p.$$

Damit gilt:

$$\boxed{R_p = O(1/p) \quad\Rightarrow\quad A_p^{rel} = O((\log p)^2).}$$

Die starke H3-rel-Version ($A_p^{rel} = O(1)$) wäre nur bei
$R_p = O(1/p(\log p)^2)$ erreichbar — zu stark als nächster natürlicher Schritt.

**Der richtige operative Satz ist:**

$$\boxed{A_p^{rel} = O((\log p)^2).}$$

---

## Der Log-Faktor ist strukturelles Signal, kein Artefakt

Der $(\log p)$-Faktor ist der **Primclock-Faktor**:

$$-\partial_s p^{-s} = (\log p)\, p^{-s}.$$

Er erscheint in zwei Messebenen:

| Ebene | Formel | Log-Potenz |
|---|---|---|
| Ableitungsseite | $-\partial_s \log(1-p^{-s})$ | $(\log p)^1$ |
| Energieseite (Norm) | $\|C_p^{rel}\|^2$ | $(\log p)^2$ |

Das Quadrat in der Normschätzung ist kein Bug — es ist die energetische Messung des Primclocks.

Aus NEU-44 §7 bestätigt:
$$-\partial_s \operatorname{Tr}_{W_{res,rel}}^{conn}\log(1-\mathcal{P}_N(s)) = \frac{\zeta_N'}{\zeta_N}(s). \quad\checkmark[M]$$

Der $\log p$-Faktor ist **strukturell verankert** in der Ableitung der relativen Selbstenergie.

---

## Kein weiterer Normwechsel

Die Normzweideutigkeit aus NEU-135 ist geschlossen. Es gibt keine sinnvolle Neudefinition von $\|\varepsilon_p\|$, die den $\log p$-Faktor absorbiert, ohne die Primclock-Struktur aus NEU-44 §7 zu zerstören.

$$\boxed{\text{Log-Faktor bleibt. Abschätzungsebene wird angepasst.}}$$

---

## Nächster Schritt: NEU-136

Benötigt wird ein **logarithmisches Abel-Lemma**, das zeigt:

$$A_p^{rel} = O((\log p)^2)$$

genügt, um die relative Selbstenergie $\Sigma_{rel,N}(\beta_0)$ kontrolliert in den $N\to\infty$-Grenzübergang zu bringen.

---

## Verweise

- **NEU-44 §5**: $C_p^{rel}\varepsilon_p = \widetilde{\Psi}_p$, $\varepsilon_p$ nackter Basisvektor
- **NEU-44 §7**: Mangoldt-Schicht strukturell erhalten
- **NEU-135**: Normkonvention-Analyse (Welt 1 vs. Welt 2)
- **NEU-133**: Primschalen-Abel-Lemma (starke Version)
- **NEU-136**: Logarithmisches Abel-Lemma (nächster Eintrag)
