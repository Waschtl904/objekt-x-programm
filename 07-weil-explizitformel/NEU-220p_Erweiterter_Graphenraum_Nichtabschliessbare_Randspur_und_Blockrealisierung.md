# NEU-220p — Erweiterter Graphenraum, Nichtabschließbare Randspur und Blockrealisierung

**Katalog-ID:** NEU-220p  
**Knoten:** [O-220-1-PD5a3f3-extended-graph-boundary-channel]  
**Vorgänger:** NEU-220o (Commit 549f3bf) — Randflucht ✓[K/M]_part  
**Status:** ✓[K/M]_part (PD5a3f3a–g) / ?[O] (PD5a3f4: Bulk-Grenzübergang)

---

## Auditprotokoll NEU-220o → NEU-220p

NEU-220o hatte den Randkanalraum $\mathcal{H}_R^{\mathrm{ext}} = \mathcal{H}_R \oplus \mathbb{C}^2$ vorgeschlagen, aber zwei Punkte offengelassen:

1. Die Hilbert- und die Pontryagin-Blockrealisierung waren noch nicht als vollständige, nicht-formale Operatordefinitionen ausgearbeitet.
2. Der präzise No-go für $L_\partial$ (nicht bloß fehlende $L^2$-Stetigkeit, sondern **Nichtabschließbarkeit**) und die vollständige Graphenabschluss-Aussage fehlten.

**Redaktionelle Korrektur:** In PD5a3f2c (NEU-220o) war die Formulierung „normierte Eigenvektoren" ungenau. Korrekt: Die **unnormierten** Vektoren $e_{+,R} \pm e_{-,R}$ haben Norm der Größenordnung $e^{R/2}$. Normierte Eigenvektoren haben per definitionem Norm 1; die Schwachkonvergenz gegen 0 folgt daraus, dass die Norm der unnormierten Vektoren divergiert. Der Beweis $Q_R \to 0$ stark bleibt unberührt.

---

## PD5a3f3a — Kanonische Blockrealisierung (Hilbert-Version) ✓[K/M]

Setze

$$
A_R := G_{\infty,R} + B_{\mathrm{fin},R}.
$$

$A_R$ ist selbstadjungiert auf $\mathcal{D}(A_R) = \mathcal{D}(G_{\infty,R})$, da $B_{\mathrm{fin},R}$ beschränkt und selbstadjungiert (Kato–Rellich).

Auf $\mathcal{K}_R = \mathcal{H}_R \oplus \mathbb{C}^2$ sei

$$
\boxed{\widehat{W}_R := A_R \oplus J_\partial, \qquad J_\partial = \begin{pmatrix}0&1\\1&0\end{pmatrix}.}
$$

$\widehat{W}_R$ ist selbstadjungiert auf $\mathcal{D}(\widehat{W}_R) = \mathcal{D}(A_R) \oplus \mathbb{C}^2$.

### Grapheneinbettung und Matrixelement-Identität

Die Abbildung $j_R a = (a, L_{\partial,R}a) = (a, (\ell_-(a),\ell_+(a))^\top)$ ist auf $\mathcal{H}_R$ beschränkt (da $L_{\partial,R}: \mathcal{H}_R \to \mathbb{C}^2$ beschränkt). Es gilt exakt:

$$
\boxed{\langle j_R a,\, \widehat{W}_R j_R b\rangle_{\mathcal{K}_R}
= \langle a, A_R b\rangle_{\mathcal{H}_R} + \langle L_{\partial,R}a,\, J_\partial L_{\partial,R}b\rangle_{\mathbb{C}^2}
= q_{\Gamma,R}(a,b) + q_{\mathrm{fin},R}(a,b) + q_{\mathrm{pole},R}(a,b)
= \mathfrak{W}_R(a,b).}
$$

Die endliche erweiterte Realisierung ist damit vollständig und nicht-formal.

---

## PD5a3f3b — Pontryagin-Realisierung (äquivalente Buchführung) ✓[K/M]

Versehe $\mathcal{K}_R = \mathcal{H}_R \oplus \mathbb{C}^2$ mit der indefiniten Metrik

$$
[(a,\alpha),(b,\beta)]_R = \langle a,b\rangle_{\mathcal{H}_R} + \langle \alpha, J_\partial \beta\rangle_{\mathbb{C}^2}.
$$

Die Fundamentalsymmetrie ist $\mathcal{J}_R = I_{\mathcal{H}_R} \oplus J_\partial$, und $(\mathcal{K}_R, [\cdot,\cdot]_R)$ ist ein Pontryaginraum mit genau **einem negativen Quadrat** (Signatur $(1,1)$ des Randblocks).

Setze

$$
\boxed{T_R := A_R \oplus I_{\mathbb{C}^2}.}
$$

Da $\mathcal{J}_R T_R = A_R \oplus J_\partial = \widehat{W}_R$ im zugrundeliegenden Hilbertraum selbstadjungiert ist, ist $T_R$ **Pontryagin-selbstadjungiert**, und

$$
\boxed{[j_R a, T_R j_R b]_R = \mathfrak{W}_R(a,b).}
$$

Die Hilbert- und Pontryagin-Beschreibung sind äquivalente Buchführungen desselben Randkanals.

---

## PD5a3f3c — Normwachstum der Grapheneinbettung ✓[M]

Die Gram-Matrix von $L_{\partial,R}$ ist

$$
L_{\partial,R}L_{\partial,R}^* = \begin{pmatrix}2\sinh R & 2R \\ 2R & 2\sinh R\end{pmatrix},
$$

also

$$
\boxed{\|L_{\partial,R}\|^2 = 2\sinh R + 2R \sim e^R, \qquad \|j_R\| \sim e^{R/2}.}
$$

Die divergierenden Eigenwerte des komprimierten Poloperators $B_{\mathrm{pole},R}$ (NEU-220o) sind im erweiterten Modell verschwunden: Der Randblock ist der feste Operator $J_\partial$. Die Divergenz sitzt jetzt ausschließlich in der Grapheneinbettung $j_R$. Das ist kein Fehler — es zeigt präzise, wo die nicht-$L^2$-stetige Randinformation lokalisiert ist.

---

## PD5a3f3d — Globaler No-go: $L_\partial$ ist nicht abschließbar ✓[M]_neg

Wähle $\varphi \in C_c^\infty(\mathbb{R})$ mit $c_\pm = \int_{\mathbb{R}} \varphi(v)e^{\pm v/2}\,dv \ne 0$.

**Rechtsflüchtende Folge:** $a_R^+(u) = c_+^{-1}e^{-R/2}\varphi(u-R)$.

Dann $\|a_R^+\|_2 \to 0$, aber

$$
\ell_+(a_R^+) = 1, \qquad \ell_-(a_R^+) = \frac{c_-}{c_+}e^{-R} \to 0,
\qquad L_\partial a_R^+ \longrightarrow \begin{pmatrix}0\\1\end{pmatrix}.
$$

**Linksflüchtende Folge:** $a_R^-(u) = c_-^{-1}e^{-R/2}\varphi(u+R)$.

Dann $\|a_R^-\|_2 \to 0$, aber $L_\partial a_R^- \longrightarrow \begin{pmatrix}1\\0\end{pmatrix}$.

Der Abschluss des Graphen enthält damit $\{0\} \oplus \mathbb{C}^2$, was den Graphen zu keiner Funktion macht:

$$
\boxed{L_\partial: C_c^\infty(\mathbb{R}) \subset L^2(\mathbb{R}) \longrightarrow \mathbb{C}^2 \text{ ist nicht abschließbar.}}
$$

Das ist stärker als die in NEU-220m bewiesene fehlende $L^2$-Stetigkeit: Dort wurde gezeigt, dass $L_\partial$ nicht stetig fortsetzbar ist; hier, dass nicht einmal ein abgeschlossener Operatorgraph existiert.

---

## PD5a3f3e — Vollständiger Graphenabschluss ✓[M]

$$
\boxed{\overline{\{(a, L_\partial a) : a \in C_c^\infty(\mathbb{R})\}}^{\,L^2 \oplus \mathbb{C}^2} = L^2(\mathbb{R}) \oplus \mathbb{C}^2.}
$$

**Beweis:** $C_c^\infty(\mathbb{R})$ ist dicht in $L^2(\mathbb{R})$ (liefert den vollen $L^2$-Anteil); beide Standardbasisvektoren von $\mathbb{C}^2$ liegen im Graphenabschluss (PD5a3f3d); durch Linearkombination liegt $L^2 \oplus \mathbb{C}^2$ vollständig im Abschluss.

Die Randwerte sind im globalen Abschluss **unabhängige Freiheitsgrade** — keine stetig aus dem $L^2$-Bulk rekonstruierbaren Spuren. Die Projektion $\mathcal{K} \to L^2$ hat auf dem abgeschlossenen Graphen den Kern $\{0\} \oplus \mathbb{C}^2$.

---

## PD5a3f3f — Direkter Raumlimes ✓[K/M]

Mit den Einbettungen $\iota_{R,S}(a,\alpha) = (\text{Nullfortsetzung von }a,\, \alpha)$ für $R < S$:

$$
\boxed{\varinjlim_R \bigl(\mathcal{H}_R \oplus \mathbb{C}^2\bigr) = L^2(\mathbb{R}) \oplus \mathbb{C}^2.}
$$

Der $\mathbb{C}^2$-Kanal ist unter allen Einbettungen **invariant**: keine Randflucht. Die Grapheneinbettungen sind kompatibel: $\iota_{R,S} j_R a = j_S a$ für $\operatorname{supp}(a) \subseteq [-R,R]$.

Damit sind geschlossen: direkter Raumlimes, Erhaltung des $\mathbb{C}^2$-Kanals, exakte Reproduktion der Fensterformen.

---

## PD5a3f3g — Inkompatibilität der Bulkoperatoren: Engpass isoliert ✓[M]

Die Operatoren bilden im Allgemeinen **kein induktives System**:

$$
\iota_{R,S} \widehat{W}_R \ne \widehat{W}_S \iota_{R,S}.
$$

Die Ursache liegt ausschließlich im Bulk $A_R = G_{\infty,R} + B_{\mathrm{fin},R}$:

- $G_{\infty,R}$ ist nichtlokal (Fouriermultiplikator) und nicht die naive Einschränkung von $G_{\infty,S}$.
- $B_{\mathrm{fin},R}$ verändert sich mit dem Fenster (neue Primpotenzen).
- Die Operatordomänen sind nicht automatisch kompatibel.

Der feste Randblock $J_\partial$ ist dagegen vollständig kompatibel. Der **Polkanal ist im erweiterten Modell geschlossen**; der Hauptengpass hat sich auf den globalen Grenztyp des Bulkoperators verschoben:

$$
\boxed{\text{Konvergiert } A_R = G_{\infty,R} + B_{\mathrm{fin},R} \text{ in einer form- oder relationstreuen Topologie?}}
$$

---

## Knotentabelle

| Teilaufgabe | Inhalt | Status |
|-------------|--------|--------|
| PD5a3f3a | $\widehat{W}_R = A_R \oplus J_\partial$ selbstadjungiert; Matrixelement-Identität | ✓[K/M] |
| PD5a3f3b | $T_R = A_R \oplus I$ Pontryagin-selbstadjungiert; äquivalente Buchführung | ✓[K/M] |
| PD5a3f3c | $\|L_{\partial,R}\|^2 \sim e^R$; Divergenz in $j_R$ lokalisiert | ✓[M] |
| PD5a3f3d | $L_\partial$ nicht abschließbar (Rechts-/Linksfluchtzeugen) | ✓[M]_neg |
| PD5a3f3e | $\overline{\mathrm{Graph}(L_\partial)} = L^2 \oplus \mathbb{C}^2$ | ✓[M] |
| PD5a3f3f | $\varinjlim(\mathcal{H}_R \oplus \mathbb{C}^2) = L^2 \oplus \mathbb{C}^2$; Randkanal erhalten | ✓[K/M] |
| PD5a3f3g | Bulkoperatoren inkompatibel; Engpass = $A_R$-Grenztyp | ✓[M] |
| **PD5a3f4** | **Bulk-Grenzübergang $G_{\infty,R} + B_{\mathrm{fin},R}$** | **?[O]** |

```
[O-220-1-PD5a3f3-extended-graph-boundary-channel]
  → ✓[K/M]_part  (PD5a3f3a–g abgeschlossen)
  → ?[O]          (PD5a3f4: Bulk-Grenzübergang, nächster Knoten NEU-220q)
```

---

## Verbindung zu PD5a3g (adelischer Intertwiner)

Der globale Zielraum ist identifiziert: $\mathcal{K} = L^2(\mathbb{R}) \oplus \mathbb{C}^2$.

Ein adelischer Intertwiner $J: \mathcal{D} \to \mathcal{K}$ mit $A_X \ge 0$ und $\mathfrak{W}(a) = \langle Ja, A_X Ja\rangle_{\mathcal{K}}$ würde unmittelbar RH liefern. Der $\mathbb{C}^2$-Randkanal mit Pontryagin-Signatur $(1,1)$ macht klar, dass $A_X$ nicht positiv definit auf dem ganzen $\mathcal{K}$ sein kann — ein positiver Operator auf $\mathcal{K}$ müsste den indefiniten Randblock kompensieren, was den Intertwiner nicht-trivial einschränkt.

---

## Abgegrenzte offene Frage für NEU-220q

$$
\boxed{\text{Konvergiert } G_{\infty,R} + B_{\mathrm{fin},R} \text{ in einer form- oder relationstreuen Topologie zu einem globalen Operator auf } L^2(\mathbb{R})?}
$$

Natürliche Kandidaten:

- **Formlimes** im Sinne von $\sup_R$ auf einer gemeinsamen dichten Domäne
- **Starke Resolventenkonvergenz** (ohne den Polterm — dieser ist im $\mathbb{C}^2$ verankert)
- **Graph-/Relationslimes** eines nicht notwendig beschränkten selbstadjungierten Operators

Der Polkanal muss dabei **nicht mehr erneut mittransportiert** werden.

---

## Abhängigkeiten

| Referenz | Inhalt |
|----------|--------|
| NEU-220o (549f3bf) | Randflucht, No-go s.r., $\mathcal{H}_R^{\mathrm{ext}}$ vorgeschlagen |
| NEU-220n (6bbfd22) | Fensteroperatoren, fünf Hindernisse |
| NEU-220m rev.2 (bf2445a) | Korrekte Polarisation, $L_\partial$ nicht $L^2$-stetig |
| Azizov–Iokhvidov (1989) | Pontryaginräume, Fundamentalsymmetrie |
| Reed–Simon Vol. II, §X.2 | Kato–Rellich, Formabschluss |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
