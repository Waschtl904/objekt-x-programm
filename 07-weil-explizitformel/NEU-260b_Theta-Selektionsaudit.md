# NEU-260b — $\theta$-Selektionsaudit: Kanonische Paarung der Defizienzlinien

**Katalog-ID:** NEU-260b  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-08  
**Auftrag:** Vier Tests: (1) Defizienzlinien exakt typisieren; (2) Gauge-Freiheit $\theta\mapsto\theta+\beta-\alpha$ beweisen; (3) BC/KMS/Frobenius-Quellenbestand für kanonisches $U_a:\mathcal{N}_{+,a}\to\mathcal{N}_{-,a}$ auditieren; (4) falls ja, explizite Koordinate $e^{i\theta(a)}$ ablesen.  
**Standardwahl:** $\lambda=\lambda_{\rm can}(a)=\lambda_a-1$ aus NEU-260a $\checkmark[K/M]$.  
**Vorgänger:** NEU-260a $\checkmark$, NEU-260 (Hauptknoten), NEU-250-Serie  

---

## 0. Leitfrage

$$
\boxed{\text{Konstruiert BC/KMS/Frobenius/Adelen kanonisch eine unitäre Identifikation }U_a:\mathcal{N}_{+,a}\longrightarrow\mathcal{N}_{-,a}?} \qquad (0\text{-Lead})
$$

Nicht: "Findet BC eine Zahl $\theta(a)$?" (Koordinate hängt von Basiswahl ab.)

Sondern: "Konstruiert BC ein geometrisches Datum $U_a$, aus dem nach Wahl einer kanonischen Basentrivialisierung die Koordinate $e^{i\theta(a)}$ abgelesen werden kann?"

---

## Test 1 — Defizienzlinien exakt typisieren

### 1.1 Minimaler Operator und Adjungierter

Auf $\mathcal{H}(T_a^{\rm can})$ (Standardwahl $\lambda=\lambda_{\rm can}(a)$) mit $\mathscr{D}_a = i\frac{d}{dx}$ auf $C_c^\infty(-a,a)$:

$$
\mathscr{D}_a^*f = i\frac{d}{dx}f\quad\text{auf}\quad\operatorname{Dom}(\mathscr{D}_a^*) = \{f\in\mathcal{H}(T_a^{\rm can}) : f\text{ abs. stetig, }f'\in\mathcal{H}(T_a^{\rm can})\}. \qquad (1\text{-Adj})
$$

### 1.2 Defizienzräume

$$
\boxed{\mathcal{N}_{+,a} := \ker(\mathscr{D}_a^* - i\cdot\mathrm{Id}) = \operatorname{span}\{e^{x}\}\cap\mathcal{H}(T_a^{\rm can}),} \qquad (1\text{-Np})
$$
$$
\boxed{\mathcal{N}_{-,a} := \ker(\mathscr{D}_a^* + i\cdot\mathrm{Id}) = \operatorname{span}\{e^{-x}\}\cap\mathcal{H}(T_a^{\rm can}).} \qquad (1\text{-Nm})
$$

**Defizienzindizes:** $(n_+,n_-)=(1,1)$ auf $(-a,a)$ für jedes $a<\infty$. $\checkmark[K/M]$ (Standard; $e^{\pm x}\in L^2(-a,a)$).

### 1.3 Kanonische (un-normierte) Vektoren

Kanonische Erzeuger (vor Normierung):
$$
\mathbf{e}_{+,a}(x) := e^x \cdot \mathbf{1}_{(-a,a)}, \qquad \mathbf{e}_{-,a}(x) := e^{-x} \cdot \mathbf{1}_{(-a,a)}. \qquad (1\text{-Gen})
$$

**Normen** in $\mathcal{H}(T_a^{\rm can})$: explizit berechenbar, abhängig von $Q_W^a$ auf $\{e^{\pm x}\}$. Diese Normen sind reell und positiv; die Phasen von $\mathbf{e}_{\pm,a}$ sind durch die reelle Funktion $e^{\pm x}$ fixiert --- aber nur bis zu einer komplexen Skalierung $\mathbf{e}_{\pm,a}\mapsto e^{i\alpha_{\pm}}\mathbf{e}_{\pm,a}$.

$$
\text{Defizienzlinien } \mathcal{N}_{\pm,a} \text{ eindimensional, kanonische Erzeuger } e^{\pm x}: \quad\checkmark[K/M] \qquad (1\text{-Done})
$$

---

## Test 2 — Gauge-Freiheit: $\theta\mapsto\theta+\beta-\alpha$ $\checkmark[K/M]$

### 2.1 von-Neumann-Parametrisierung

Suzuki wählt normierte Defizientvektoren
$$
v_{+} = \frac{\mathbf{e}_{+,a}}{\|\mathbf{e}_{+,a}\|_{T_a}}, \qquad v_{-} = \frac{\mathbf{e}_{-,a}}{\|\mathbf{e}_{-,a}\|_{T_a}}, \qquad (2\text{-Norm})
$$
und setzt $w_\theta = v_+ + e^{i\theta}v_-$. Die selbstadjungierte Erweiterung $\overline{\mathscr{D}}_{a,\theta}$ wird durch den Graphen von $w_\theta$ definiert.

### 2.2 Phasenfreiheit

Ersetzt man
$$
v_+ \mapsto e^{i\alpha}v_+, \qquad v_- \mapsto e^{i\beta}v_-, \qquad (2\text{-Phase})
$$
so transformiert der Erweiterungsvektor:
$$
w_\theta = v_+ + e^{i\theta}v_- \quad\longmapsto\quad e^{i\alpha}v_+ + e^{i(\theta+\beta)}v_- = e^{i\alpha}\left(v_+ + e^{i(\theta+\beta-\alpha)}v_-\right). \qquad (2\text{-Trans})
$$

Da der Graph von $w_\theta$ und $e^{i\alpha}w_\theta$ dieselbe selbstadjungierte Erweiterung definieren:
$$
\boxed{\theta\mapsto\theta+\beta-\alpha \quad \Rightarrow \quad \overline{\mathscr{D}}_{a,\theta}\cong\overline{\mathscr{D}}_{a,\theta+\beta-\alpha}.\quad\checkmark[K/M]} \qquad (2\text{-Gauge})
$$

**Fazit:** Die Zahl $\theta\in[0,2\pi)$ ist **keine intrinsische Größe**. Intrinsisch ist der unitäre Operator
$$
\boxed{U_a : \mathcal{N}_{+,a} \longrightarrow \mathcal{N}_{-,a}, \qquad U_a := \text{von-Neumann-Parameter (basisunabhängig definiert).}} \qquad (2\text{-Ua})
$$

Nach Wahl orthonormierter Basen $\{v_+\}$, $\{v_-\}$ erscheint $U_a$ als $e^{i\theta}$; $\theta$ selbst hängt von dieser Basiswahl ab.

---

## Test 3 — BC/KMS/Frobenius-Quellenbestand für $U_a$ $?[O]$

### 3.1 Was benötigt wird

Gesucht: eine kanonische unitäre Abbildung
$$
U_a^{\rm BC} : \mathcal{N}_{+,a} \longrightarrow \mathcal{N}_{-,a} \qquad (3\text{-Need})
$$
die aus der Struktur von BC/KMS/Frobenius/Adelen folgt, ohne Basiswahl.

### 3.2 Kandidat I: Modulare Konjugation $J_{\rm KMS}$

Im BC-/KMS-Formalismus existiert eine **modulare Konjugation** $J$ (antiunitäre Involution, $J^2=1$), die Erzeuger und Vernichter vertauscht. Auf der archimedischen Seite entspricht sie der Komplex-Konjugation kombiniert mit der Involution $x\mapsto -x$ (Spiegelung am Ursprung).

**Wirkung auf Defizienträume:** Unter der Spiegelung $\sigma: x\mapsto -x$:
$$
\mathbf{e}_{+,a}(x) = e^x \quad\xmapsto{\sigma}\quad e^{-x} = \mathbf{e}_{-,a}(x). \qquad (3\text{-Refl})
$$

Die Spiegelung $\sigma$ liefert also eine natürliche lineare Abbildung
$$
U_a^\sigma : \mathcal{N}_{+,a} \to \mathcal{N}_{-,a}, \qquad U_a^\sigma (c\cdot\mathbf{e}_{+,a}) = c\cdot\mathbf{e}_{-,a}. \qquad (3\text{-Sigma})
$$

**Status:** $U_a^\sigma$ ist wohldefiniert als lineare Abbildung zwischen eindimensionalen Räumen. Sie ist **unitär** genau dann, wenn $\|\mathbf{e}_{+,a}\|_{T_a}=\|\mathbf{e}_{-,a}\|_{T_a}$.

$$
\|\mathbf{e}_{+,a}\|_{T_a}^2 = Q_W^a(e^x,e^x) - \lambda_{\rm can}\|e^x\|_2^2, \qquad \|\mathbf{e}_{-,a}\|_{T_a}^2 = Q_W^a(e^{-x},e^{-x}) - \lambda_{\rm can}\|e^{-x}\|_2^2. \qquad (3\text{-Norms})
$$

Da $Q_W^a$ durch das Primblock-Gewicht $-2\Lambda(n)/\sqrt{n}\cdot g(\log n)$ und den $\Gamma$-Block bestimmt wird, und $\|e^x\|_{L^2(-a,a)}=\|e^{-x}\|_{L^2(-a,a)}$ (Symmetrie des Intervalls), hängt die Gleichheit der Normen davon ab, ob $Q_W^a$ selbst symmetrisch unter $x\mapsto -x$ ist.

$$
Q_W^a(f,f)=Q_W^a(\tilde f,\tilde f)\text{ mit }\tilde f(x):=\overline{f(-x)}?\quad?[O] \qquad (3\text{-Sym})
$$

**Physikalische Deutung:** $(3\text{-Sym})$ ist die Selbstdualität der Weil-Form unter der kanonischen Involution der adelischen Struktur. Diese Involution ist strukturell im BC-Strang vorhanden (Spiegelung im adelischen Multiplika-tionsfeld), muss aber explizit auf $Q_W^a$ geprüft werden.

### 3.3 Kandidat II: Frobenius-Phase

Aus der lokalen BC/Frobenius-Struktur könnte eine kanonische Phase
$$
e^{i\varphi_p} \in U(1) \qquad (3\text{-Frob})
$$
pro Primzahl $p$ entstehen (etwa aus der Frobenius-Spurformel oder dem Nakayama-Funktionalkalkül). Ein Produkt über alle $p$ wäre dann
$$
e^{i\varphi} = \prod_p e^{i\varphi_p}. \qquad (3\text{-FrobProd})
$$

**Problem:** Ein konvergentes Produkt über alle Primzahlen wäre außerordentlich unwahrscheinlich ohne zusätzliche Struktur. Dieser Kandidat ist spekulativer als Kandidat~I.

$$
\text{Frobenius-Phase als globales Produkt: spekulative Kandidatur.}\quad?[O] \qquad (3\text{-FrobStatus})
$$

### 3.4 Kandidat III: Hecke-Symmetrie

Hecke-Operatoren $T_p$ auf dem adelischen Ring haben kanonische Selbstdualität (Petersson-Pairing). Falls sie auf $\mathcal{N}_{\pm,a}$ wirken, könnten sie $U_a$ als Intertwiner auswählen.

$$
\text{Hecke-Wirkung auf }\mathcal{N}_{\pm,a}:\quad?[O] \qquad (3\text{-Hecke})
$$

### 3.5 Favorit: Modulare Konjugation / Spiegelungssymmetrie

Kandidat I hat den größten strukturellen Vorteil: er braucht kein konvergentes Produkt, sondern nur die Symmetriefrage $(3\text{-Sym})$.

$$
\boxed{\text{Primärer BC-Eintrittspunkt: Modulare Konjugation / Spiegelung }x\mapsto -x.\quad?[O]\to\text{Test 4}} \qquad (3\text{-Fav})
$$

---

## Test 4 — Explizite Koordinate $e^{i\theta(a)}$ (konditional auf Test 3) $?[O]$

Falls Test 3 ergibt $U_a^\sigma$ ist unitär (d.h. $(3\text{-Sym})$ gilt), und nach Wahl der kanonischen normierten Basen
$$
v_+ := \frac{\mathbf{e}_{+,a}}{\|\mathbf{e}_{+,a}\|_{T_a}}, \qquad v_- := \frac{\mathbf{e}_{-,a}}{\|\mathbf{e}_{-,a}\|_{T_a}}, \qquad (4\text{-Bases})
$$
transportiert $U_a^\sigma v_+ = v_-$, also $e^{i\theta(a)}=1$, d.h.
$$
\boxed{\theta_{\rm can}(a) = 0\quad\text{(falls Spiegelungssymmetrie von }Q_W^a\text{ gilt).}\quad?[O]\to\text{zu beweisen}} \qquad (4\text{-Theta0})
$$

Wenn $(3\text{-Sym})$ nicht gilt, ist $U_a^\sigma$ nicht unitär; man müsste stattdessen normieren:
$$
U_a^{\sigma,{\rm norm}} v_+ = e^{i\theta(a)} v_-, \qquad e^{i\theta(a)} = \frac{\|\mathbf{e}_{+,a}\|_{T_a}}{\|\mathbf{e}_{-,a}\|_{T_a}}\in\mathbb{R}_{>0}\cap S^1=\{1\} \qquad\text{nur falls Normen gleich.} \qquad (4\text{-Norm})
$$

Ein reellwertiges Verhältnis $\|\mathbf{e}_{+,a}\|/\|\mathbf{e}_{-,a}\|\neq 1$ wäre eine Amplitude, kein Phasenfaktor. Das wäre kein Element von $U(1)$ und könnte nicht direkt als von-Neumann-Parameter verwendet werden.

$$
\theta_{\rm can}(a)=0\Leftrightarrow\|\mathbf{e}_{+,a}\|_{T_a}=\|\mathbf{e}_{-,a}\|_{T_a}\Leftrightarrow Q_W^a\text{ ist symmetrisch unter }x\mapsto-x.\quad?[O] \qquad (4\text{-Equiv})
$$

---

## 5. Zusammenfassung und Strategische Einschätzung

$$
\boxed{\text{Kernfrage: Gilt }Q_W^a(f,f)=Q_W^a(\tilde f,\tilde f)\text{ mit }\tilde f(x)=\overline{f(-x)}?} \qquad (5\text{-Core})
$$

Falls ja: $\theta_{\rm can}(a)=0$, d.h. die Spiegelungsinvolution $x\mapsto -x$ wählt kanonisch die selbstadjungierte Erweiterung $\overline{\mathscr{D}}_{a,0}$ aus. Das wäre ein echter neuer Mechanismus: eine arithmetisch motivierte selbstadjungierte Erweiterung, nicht eine frei gewählte.

Falls nein: $Q_W^a$ bricht die Spiegelungssymmetrie; dann muss die Asymmetrie $\|\mathbf{e}_{+,a}\|\neq\|\mathbf{e}_{-,a}\|$ verstanden werden, und es braucht einen anderen Kandidaten für $U_a$.

**Struktureller Hinweis:** Die Weil-Explizitformel in M3-Form (NEU-252) enthält:
- $B_{\rm fin}$: symmetrisch unter $g\mapsto\tilde g$ (da $\Lambda(n)/\sqrt{n}$ reell und $g(\log n)$ bei reellem $g$ symmetrisierbar).
- $B_\Gamma$: durch $\operatorname{Re}\gamma_\infty(t)$ definiert, symmetrisch unter $t\mapsto -t$ (reeller Gammafaktor).
- $B_{\rm pole}$: $\hat g(i/2)+\hat g(-i/2)$, symmetrisch unter $g\mapsto\tilde g$ falls $g$ reell.

Vorläufige Einschätzung: $Q_W^a$ **könnte** symmetrisch unter $x\mapsto -x$ sein, muss aber explizit geprüft werden.

$$
Q_W^a\text{-Spiegelungssymmetrie: strukturell plausibel, noch nicht bewiesen.}\quad?[O] \qquad (5\text{-Plaus})
$$

---

## 6. Offene Punkte

$$\text{Defizienzlinien }\mathcal{N}_{\pm,a}=\operatorname{span}\{e^{\pm x}\}\cap\mathcal{H}(T_a^{\rm can})\quad\checkmark[K/M]\qquad(6\text{-a})$$
$$\theta\text{-Gauge-Freiheit: }\theta\mapsto\theta+\beta-\alpha\quad\checkmark[K/M]\qquad(6\text{-b})$$
$$U_a\text{ als intrinsisches geometrisches Datum (statt numerischem }\theta)\quad\checkmark[K/M]\qquad(6\text{-c})$$
$$Q_W^a(f,f)=Q_W^a(\tilde f,\tilde f)\text{ mit }\tilde f(x)=\overline{f(-x)}?\quad?[O]\qquad(6\text{-d})$$
$$U_a^\sigma\text{ unitär }\Leftrightarrow\|\mathbf{e}_{+,a}\|=\|\mathbf{e}_{-,a}\|\quad?[O]\qquad(6\text{-e})$$
$$\theta_{\rm can}(a)=0\text{ falls Spiegelungssymmetrie}\quad?[O]\qquad(6\text{-f})$$
$$\text{Frobenius-Phase als globales Produkt: spekulative Kandidatur}\quad?[O]\qquad(6\text{-g})$$
$$\text{Hecke-Wirkung auf }\mathcal{N}_{\pm,a}\quad?[O]\qquad(6\text{-h})$$

---

## 7. Abhängigkeiten

| Referenz | SHA/Quelle | Inhalt |
|---|---|---|
| NEU-260a (Patch) | 371412d | $\lambda_{\rm can}=\lambda_a-1$ $\checkmark$ |
| NEU-260 | Hauptknoten | Klassifikation $\theta$ als echtes Selektionsdatum |
| NEU-258 | 1fa3745 | $W_{\rm NEU-252}=W_{\rm Lit}$ $\checkmark$ |
| NEU-252 (Patch) | 4ee78ed | $B_W=B_{\rm pole}+B_\Gamma+B_{\rm fin}$ |
| NEU-250-Serie | div. | $\Lambda(p^k)/\sqrt{p^k}$ aus BC/Frobenius |
| Suzuki 2026 | \S{}2, Def. | $\overline{\mathscr{D}}_{a,\theta}$, $W(a,\theta;z)$ |
| von Neumann | \S{}III | sa. Erweiterungen, Defizienträume, Gauge-Freiheit |
| BC/KMS-Strang | div. | modulare Konjugation, Spiegelungsinvolution |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-08. Kernfrage: $Q_W^a$-Spiegelungssymmetrie $(5\text{-Core})$. Nächster Schritt: expliziter Normenvergleich $\|\mathbf{e}_{+,a}\|_{T_a}$ vs. $\|\mathbf{e}_{-,a}\|_{T_a}$.*
