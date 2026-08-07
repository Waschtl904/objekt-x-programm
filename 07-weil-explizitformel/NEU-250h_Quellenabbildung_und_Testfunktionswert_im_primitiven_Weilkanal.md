# NEU-250h — Quellenabbildung und Testfunktionswert im primitiven Weilkanal

**Katalog-ID:** NEU-250h
**Vorgänger:** NEU-250g (Modulare Halbgewichtung und primitiver Weilfaktor) ✓[K/M]
**Status:** ✓[M] für H1–H2, ?[O] für H3

---

## 0. Ausgangslage

NEU-250g liefert den lokalen arithmetischen Gewichtsfaktor
$$
h_p^{\mathrm{bal}}\bigl(\mathsf H_{\rm BC}^{1/2}E_R,\mathsf H_{\rm BC}^{1/2}E_{R'}\bigr) = \frac{\log p}{\sqrt p}\,\delta_{RR'}. \qquad (1)
$$

Gesucht ist die Brücke zum primitiven Term der Weil-Explizitformel, in dem $\frac{\log p}{\sqrt p}$ nicht isoliert steht, sondern mit einem Testfunktionswert $g(\log p)$ multipliziert wird. Die Aufgabe ist **nicht**, $g(\log p)$ neu zu erfinden, sondern die bereits verbindliche Quellenabbildung aus NEU-220l zu zitieren und typkorrekt anzuschließen.

---

## H1 — Arithmetisches Gewicht (bereits erledigt)

Durch NEU-250g fixiert:
$$
w_p := \frac{\log p}{\sqrt p}. \qquad (2)
$$

Status: ✓[M], keine offene Frage.

---

## H2 — Testfunktions-Matrixkoeffizient

### Verbindliche Quelle: NEU-220l, PD5a2a/c

Für $a \in \mathcal A_{\mathrm{PW}} = C_c^\infty(\mathbb R;\mathbb C)$ mit Involution $a^\sharp(u):=\overline{a(-u)}$ ist die Autokorrelation
$$
c_a(x) := (a*a^\sharp)(x) = \int_{\mathbb R} a(v)\,\overline{a(v-x)}\,dv, \qquad (3)
$$
und die verbindliche **reelle Evenisierung**
$$
g_a(x) := \tfrac12\bigl(c_a(x)+c_a(-x)\bigr) = \operatorname{Re}\, c_a(x). \qquad (4)
$$

Setzt man den Translationsoperator $(U_x a)(v) := a(v-x)$ ein (unitär auf $L^2(\mathbb R)$, da reine Verschiebung), so ist (3) exakt ein Matrixkoeffizient:
$$
\boxed{g_a(\log p) = \operatorname{Re}\,\langle a, U_{\log p}\,a\rangle_{L^2(\mathbb R)}.} \qquad (5)
$$

### Korrektur gegenüber der Ausgangsvermutung

Die in der Anfrage vorgeschlagene Form $g(\log p) = \langle U_{\log p}f,f\rangle$ ist **strukturell richtig**, aber in zwei Punkten unvollständig gegenüber der Projektkonvention:

- **Realteil ist zwingend**: Ohne $\operatorname{Re}(\cdot)$ ist $c_a(x)$ im Allgemeinen komplex, weil $a$ komplexwertig ist. Nur $g_a = \operatorname{Re}\,c_a$ ist die Größe, die tatsächlich in der Masterform auftritt (NEU-220l, PD5a2c). Die Weglassung des Realteils wäre ein Typfehler analog zu den in NEU-250g bereits identifizierten Vorzeichen-/Typfehlern.
- **Reihenfolge/Konjugation fest**: In (3) steht $\overline{a(v-x)}$, nicht $\overline{a(v+x)}$ oder $a(v-x)$ ohne Konjugation. Diese Konvention ist durch das Lemma $\mathcal M_{a^\sharp}(s)=\overline{\mathcal M_a(1-\bar s)}$ in NEU-220l erzwungen, nicht frei wählbar.

### Einbettung in die volle arithmetische Summe

Die verbindliche Masterform (NEU-220l, PD5a2d) ist
$$
\mathfrak W(a) = h_a(i/2)+h_a(-i/2)+2\Lambda_\Gamma(h_a) - 2\sum_{n\geq 2}\frac{\Lambda(n)}{\sqrt n}\,g_a(\log n). \qquad (6)
$$

Für $n=p$ prim ($m=1$) gilt $\Lambda(p)=\log p$, sodass der einzelne Summand exakt
$$
\frac{\log p}{\sqrt p}\,g_a(\log p) = w_p \cdot \operatorname{Re}\,\langle a, U_{\log p}a\rangle \qquad (7)
$$
lautet — dein primitiver Term als $m=1$-Spezialfall von (6), jetzt mit korrektem Realteil.

Status H2: ✓[M], direkt aus vorhandener Quelle zitiert, keine Neuherleitung nötig.

---

## Firewall — explizit gefordert, hiermit gesetzt

$$
\boxed{\text{NEU-250h behauptet NICHT: } \frac{\log p}{\sqrt p}g_a(\log p) = \|\mathcal C_p f\|^2 \text{ für irgendein } \mathcal C_p.}
$$

Grund: $\langle a, U_{\log p}a\rangle$ ist ein Matrixkoeffizient eines unitären Operators, kein Normquadrat. Er kann für beliebiges $a$ negativ oder null sein (nur $\operatorname{Re}$, kein Betragsquadrat). Insbesondere ist
$$
\mathcal C_p := \sqrt{g_a(\log p)}\,E_R
$$
**nicht wohldefiniert** (keine kanonische Wurzel, kein garantiertes Vorzeichen). Diese Konstruktion wird hier explizit als Nicht-Weg protokolliert, wie in der Anfrage gefordert.

Ebenso bleibt aus NEU-250g bestehen: $\mathsf H_{\rm BC}^{1/2}$ ist algebraischer Multiplikator auf dem balancierten $p$-Kanal; Selbstadjungiertheit/Abschluss/Definitionsbereich ist weiterhin R2, hier nicht mitbehauptet.

---

## H3 — Globale Faktorisierung (offen)

Offene Frage, unverändert wie in der Anfrage benannt: Wie geht
$$
\sum_p \frac{\log p}{\sqrt p}\operatorname{Re}\langle a, U_{\log p}a\rangle
$$
zusammen mit dem archimedischen Kanal ($h_a(i/2)+h_a(-i/2)+2\Lambda_\Gamma(h_a)$) und den Primzahlpotenz-Termen ($n=p^m$, $m>1$) in die globale, unter RH positive Form (6) ein? Die Positivität von $\mathfrak W(a)$ selbst ist laut NEU-220l/PD5a2f äquivalent zu RH — sie darf hier weder vorausgesetzt noch beiläufig erzwungen werden.

Status H3: ?[O], nächster Knoten.

---

## Nächster Test (wie in der Anfrage angekündigt)

Primzahlpotenzterm $m>1$: Für $n=p^m$ ist $\Lambda(p^m)=\log p$ und der Summand in (6) wird
$$
\frac{\log p}{p^{m/2}}\,g_a(m\log p) = \frac{\log p}{p^{m/2}}\operatorname{Re}\langle a, U_{m\log p}a\rangle.
$$
Zu prüfen: Passt dieser Term zu einer $m$-fachen Iteration des balancierten $p$-Kanals aus NEU-250g (also $\mathsf H_{\rm BC}^{1/2}$ auf dem $p^m$-Sektor), oder erfordert er einen eigenständigen Knoten NEU-250i?

---

## Abhängigkeiten

| Referenz | Inhalt |
|---|---|
| NEU-250g | $w_p=\log p/\sqrt p$ aus balancierter Frobeniusform |
| NEU-220l (PD5a2a–f) | $a^\sharp$, $c_a$, $g_a=\operatorname{Re} c_a$, Masterform $\mathfrak W(a)$ |
| NEU-220k | Xi-Masterkontur, Grundlage für $h_a$-Seite |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/objekt-x-programm.*
