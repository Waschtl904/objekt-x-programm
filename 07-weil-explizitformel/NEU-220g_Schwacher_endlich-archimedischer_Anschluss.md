# NEU-220g — PD-5a: Schwacher endlich-archimedischer Anschluss

**Knoten:** `[O-220-1-PD5a-weak-connection]`  
**Stand:** 25. Juli 2026  
**Vorgänger:** NEU-220f (PD-4c1–c3 ✓[K/M]/✓[M]; PD-4c4 ?[O])  
**Aufbau auf:** PD-4b ✓[K/M] (semifinite Spur), PD-4c3 ✓[M] (Spurrückgewinnung)

**Wichtige Einschränkung:** Dieser Knoten verbindet *ausschließlich den Gammaanteil*
$\Lambda_\Gamma$ mit dem endlichen Port $\Lambda_\mathrm{fin}$. Der rohe Polterm
$p_\infty^\mathrm{raw}(t) = -\frac{2it}{\frac14+t^2}$ verschwindet zwar auf reell-geradem $h$,
nicht aber allgemein auf $\mathcal{S}_\mathrm{herm}$. Der Knoten
`[O-220-1-PD3d4-pole-functional]` bleibt getrennt offen.

Atomare Unterknoten:
- **PD-5a1** — Endlicher Anschlussport $\Lambda_\mathrm{fin}$ aus Primärdateien auditieren ?[O]
- **PD-5a2** — Schwache direkte Summe $\Lambda_{\mathbb A}^\mathrm{weak} = \Lambda_\mathrm{fin} + \Lambda_\Gamma$ ?[O]$\to$✓[K/M]
- **PD-5a3** — Gemeinsamer Testfunktionsparameter ?[O]
- **PD-5a4** — Tensorprodukt-Einschränkung (Augmentationsbedarf) ?[O]

---

## 0. Strategischer Kontext

Nach NEU-220f besteht eine vollständige archimedische Kette:

$$
\Gamma_{\mathbb R} \longrightarrow S_\infty \longrightarrow Q_\infty = M_{\gamma_\infty^\mathrm{sym}} \longrightarrow \Lambda_\Gamma(h) = \tfrac1{4\pi}\tau_\infty(Q_\infty h(H_\infty)).
$$

Was fehlt, ist die Bindung an die endliche (Primzahl-)Seite. Das Ziel von NEU-220g
ist nicht die vollständige Weil-Formel, sondern die typkorrekte Vorbereitung
einer schwachen direkten Summe.

$$
\boxed{
\Lambda_{\mathbb A}^\mathrm{weak}(f_\mathrm{fin},h) = \Lambda_\mathrm{fin}(f_\mathrm{fin}) + \Lambda_\Gamma(h)
}
$$

mit klar separierten Trägerräumen und Normierungen.

---

## 1. PD-5a1 — Endlicher Anschlussport (Audit aus Primärdateien)

### 1.1 Quelle: NEU-28 (werkzeuge/neu28)

Aus dem KMS-Spurkalkül (NEU-28, §3.2) folgt unter Voraussetzung $C_L\neq 0$:

$$
\lambda_\mathrm{mod}(s) = \frac{C_L}{\zeta(s)},
\qquad
R_X(s) = -\partial_s\lambda_\mathrm{mod}(s) = C_L \cdot \frac{\zeta'(s)}{\zeta(s)^2}.
$$

Nach Gamma-Korrektur (NEU-28, §7.2):

$$
R_X^\xi(s) = C_L \cdot K_\xi(s),
\qquad
K_\xi(s) = -\partial_s(\xi'/\xi)(s).
$$

Die Primzahlsumme erscheint über die Von-Mangoldt-Funktion in der Dirichlet-Entwicklung von $-\zeta'/\zeta$.

### 1.2 Vier Audit-Fragen

**Frage 1: Testfunktionsraum.**

Aus NEU-28 trägt die Primzahlpotenzsumme die Dirichlet-Reihe auf $\{\Re(s)>1\}$,
als Spur $\mathrm{Tr}_{\varphi_s}(L_3\cdot\Delta_s^{-1})$ auf dem KMS-GNS-Raum.
Die zugehörige Testfunktion $f_\mathrm{fin}$ ist also ein Element des Raums:

$$
\mathcal S_\mathrm{fin} = \{f:\mathbb A_\mathrm{fin} \to \mathbb C\mid f\in C_c^\infty(\mathbb A_\mathrm{fin})\text{, adisch glatt mit kompaktem Träger}
\}
$$

in der Verwendung des Repositorys: Die Prim-Seite trägt Testfunktionen, die
als Gewichte in der $n$-Summe $\sum_n f(n)\Lambda(n)n^{-s}$ auftreten.

**Auditbefund 1:** Der genaue Raum $\mathcal S_\mathrm{fin}$ ist in den vorhandenen
Dateien (NEU-28, NEU-29) als Spurgewicht der KMS-Spur definiert, nicht als
explizit topologisierter Testraumim Weil-Sinn. Die Kompatibilität mit einer
kanonischen $dt/(2\pi)$-Normierung ist noch nicht ausgeschrieben.

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-fin-testspace}]\quad?[O].}
$$

**Frage 2: Spur, Distribution oder regulierte Grenzform.**

Aus NEU-28 §3.2:

$$
\Lambda_\mathrm{fin}(f_\mathrm{fin})
= \mathrm{Tr}_{\varphi_s}\!\bigl(L_3\cdot\Delta_s^{-1}\bigr)\big|_{s=1/2}
$$

ist zunächst eine KMS-Spur auf dem GNS-Raum $H_s$, keine gewöhnliche
Hilbertspur (die wie bei PD-4a scheitern würde). Die semifinite Struktur
auf der endlichen Seite ist aber anders als auf $L^2(\mathbb R,dt)$:
Hier wirkt $L^\infty(\mathbb N^\times)$ mit atomarer Spur $\tau_\mathrm{fin}(M_a)=\sum_n a(n)$.

**Auditbefund 2:** $\Lambda_\mathrm{fin}$ ist in Typ-III-KMS-Spurterminologie formuliert. Eine
Übersetzung in einen $\tau_\mathrm{fin}$-semifiniten Spurausdruck analog zu PD-4b
ist strukturell möglich, aber noch nicht explizit ausgeschrieben.

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-fin-trace-type}]\quad?[O].}
$$

**Frage 3: Realitätssymmetrie von $\mathcal S_\mathrm{fin}$.**

Auf der archimedischen Seite wurde $\mathcal S_{\infty,\mathrm{even}}^{\mathbb R}$
(reell-gerader Sektor) als maßgeblicher Testfunktionsraum für PD-4c3 eingesetzt.
Für $\mathcal S_\mathrm{fin}$ ist die analoge Symmetriebedingung:

$$
f_\mathrm{fin}(n) = \overline{f_\mathrm{fin}(n)}
\quad\text{(reell)},
\qquad
f_\mathrm{fin}(n) = f_\mathrm{fin}(n^{-1})
\quad\text{(inversion-symmetrisch auf }\mathbb A_\mathrm{fin}^\times\text{)}
$$

zu klären. Die Weil-Formel verlangt hermitesche Testfunktionen; die genaue
Bedingung auf $\mathcal S_\mathrm{fin}$ hängt vom gewählten Faltungsmodell ab.

**Auditbefund 3:** Aus NEU-28 ist keine explizite Involutionsbedingung auf $f_\mathrm{fin}$ entnommen. Dies ist eine offene Typfrage.

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-fin-involution}]\quad?[O].}
$$

**Frage 4: Normierungskompatibilität.**

Der archimedische Anteil trägt den Faktor $\frac{1}{4\pi}$ (aus PD-4c3).
Die endliche Weil-Summe lautet klassisch:

$$
\Lambda_\mathrm{fin}(f_\mathrm{fin}) = \sum_{p^k} \Lambda(p^k)\,\hat f_\mathrm{fin}(p^k)
$$

mit von-Mangoldt-Gewichten. Die Normierung $dt/(2\pi)$ im archimedischen Teil
erfordert eine explizite Prüfung, ob die endliche Summe in derselben
Maßnormierung definiert ist.

**Auditbefund 4:** Die Normierung der Weil-Testfunktionen ist in den Primärdateien nicht
explizit auf $dt/(2\pi)$ abgestimmt. Dieser Abgleich ist ein notweniges Vorab-Audit.

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-normalization}]\quad?[O].}
$$

### 1.3 Zusammenfassung PD-5a1

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-finite-port}]\quad?[O].}
$$

Vier Audit-Unterfragen sind offen. Sobald alle vier geklärt sind (oder
ein Unterfragenblock als ✓[M] abgelegt werden kann), wird PD-5a1 geschlossen.

---

## 2. PD-5a2 — Schwache direkte Summe

**Voraussetzung:** PD-5a1 $\geq$ ✓[M] (zumindest partiell).

**Definition.** Sei $\mathcal S_\mathrm{fin}$ der (noch zu präzisierende) endliche
Testfunktionsraum und $\mathcal S_{\infty,\mathrm{even}}^{\mathbb R}$ der reell-gerade
archimedische Testsektor. Setze:

$$
\boxed{
\mathcal S_{\mathbb A}^\mathrm{weak} := \mathcal S_\mathrm{fin} \oplus \mathcal S_{\infty,\mathrm{even}}^{\mathbb R}
}
$$

als direkte Summe mit dem Funktional:

$$
\boxed{
\Lambda_{\mathbb A}^\mathrm{weak}(f_\mathrm{fin},h)
:= \Lambda_\mathrm{fin}(f_\mathrm{fin}) + \Lambda_\Gamma(h),
\quad
\Lambda_\Gamma(h) = \frac1{4\pi}\tau_\infty\bigl(Q_\infty\,h(H_\infty)\bigr).
}
$$

**Typkorrektheit.** $\Lambda_\mathrm{fin}$ und $\Lambda_\Gamma$ sind typkorrekt getrennt:
- $\Lambda_\mathrm{fin}$ wirkt auf $\mathcal S_\mathrm{fin}$ (diskrete/endliche Primzahlseite)
- $\Lambda_\Gamma$ wirkt auf $\mathcal S_{\infty,\mathrm{even}}^{\mathbb R}$ (archimedischer Gammaterm)
- Keine Kreuzterme; keine Kopplungsannahme.

**Was diese Konstruktion leistet:** Sie stellt fest, dass beide Anteile dieselbe
komplexe Zahl $\mathbb C$ als Zielraum haben und additiv zusammengeführt werden können,
ohne das eine die Struktur des anderen voraussetzt.

**Was sie nicht leistet:**
- Keine adelische Wechselwirkung
- Kein gemeinsamer Testfunktionsparameter
- Keine vollständige Weil-Formel
- Kein Objekt XXX

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a2-weak-direct-sum}]\quad?[O]\to\checkmark[K/M]\text{ (bedingt durch PD-5a1)}.}
$$

---

## 3. PD-5a3 — Gemeinsamer Testfunktionsparameter

**Frage:** Gibt es eine globale Testfunktion $F\in\mathcal S_{\mathbb A}$ mit einer
kanonischen Projektion

$$
F \longmapsto (F_\mathrm{fin}, F_\infty),
$$

sodass $\Lambda_{\mathbb A}(F) = \Lambda_\mathrm{fin}(F_\mathrm{fin}) + \Lambda_\Gamma(F_\infty)$ gilt?

**Kandidat.** Die Standardwahl wäre der Bruhat-Schwartz-Raum $\mathcal S(\mathbb A)$
auf den Adelen, mit der kanonischen Tensorprodukttopologie:

$$
\mathcal S(\mathbb A) \cong \mathcal S(\mathbb A_\mathrm{fin}) \widehat\otimes \mathcal S(\mathbb R).
$$

Die Projektion $(F_\mathrm{fin}, F_\infty) = (F|_{\mathbb A_\mathrm{fin}\times\{0\}}, F|_{\{0\}\times\mathbb R})$
ist jedoch nur für Rang-1-Tensoren $F = f_\mathrm{fin}\otimes h$ kanonisch definiert.

**Einschränkung (PD-5a4-Vorgriff):** Für allgemeine $F\in\mathcal S(\mathbb A)$ ist
die Abbildung $F\mapsto(F_\mathrm{fin},F_\infty)$ eine Diagonaleinschränkung,
keine freie Projektion. Die Definitheit eines skalaren Funktionals auf
$\mathcal S(\mathbb A)$ erfordert dann kanonische Augmentationen (siehe PD-5a4).

**Auditfrage aus dem Repository:** Die Dateien neu26–neu30 arbeiten mit einer globalen
Mellinvariable $s$ und einer festen Spurform $\lambda_\mathrm{mod}(s)$, aber
nicht mit einer explizit adelischen Testfunktion $F\in\mathcal S(\mathbb A)$.
Eine globale Diagonalabbildung $\mathcal S_{\mathbb A}\to\mathcal S_\mathrm{fin}\oplus\mathcal S_{\infty,\mathrm{even}}^{\mathbb R}$
ist in den Primärdateien nicht konstruiert.

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a3-global-test-function}]\quad?[O].}
$$

---

## 4. PD-5a4 — Tensorprodukt-Einschränkung

**Warnung:** Ein Tensorproduktansatz

$$
\mathcal S_\mathrm{fin}\,\widehat\otimes\,\mathcal S_\infty
$$

würde für ein skalares Funktional zusätzliche kanonische Augmentationen
$\varepsilon_\mathrm{fin}:\mathcal S_\mathrm{fin}\to\mathbb C$ und $\varepsilon_\infty:\mathcal S_\infty\to\mathbb C$ benötigen:

$$
\Lambda_\mathrm{fin}\otimes\varepsilon_\infty + \varepsilon_\mathrm{fin}\otimes\Lambda_\Gamma.
$$

**Natürliche Kandidaten für Augmentationen:**

| Seite | Kandidat für $\varepsilon$ | Natürlichkeit |
|---|---|---|
| $\varepsilon_\infty(h)$ | $h(0)$ (Dirac-Auswertung) | Nicht stetig auf $\mathcal S$ ohne Zusatzbedingung |
| $\varepsilon_\infty(h)$ | $\int_\mathbb R h\,dt/(2\pi)$ | Stetig, aber Normierung ungeklärt |
| $\varepsilon_\mathrm{fin}(f)$ | $f(1)$ (Einheitswert) | Stetig auf $C_c^\infty(\mathbb A_\mathrm{fin})$ |
| $\varepsilon_\mathrm{fin}(f)$ | $\hat f(1)$ (Fourier bei 1) | Nur sinnvoll nach Maßwahl |

Ohne einen natürlichen Augmentationsmechanismus ist das Tensorprodukt
kein ehrlicherer Typ als die direkte Summe. Der direkten-Summen-Anschluss
(PD-5a2) ist daher der methodisch korrekte erste Schritt.

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a4-tensor-augmentation}]\quad?[O].}
$$

---

## 5. Polwarnung: Strikte Trennung von $\Lambda_\mathrm{pole}$

Aus NEU-220d rev.2 gilt die folgende strikte Einschränkung:

> $p_\infty^\mathrm{raw}(t) = -\frac{2it}{\frac14+t^2}$ verschwindet auf reell-geradem $h$, **nicht** aber allgemein auf $\mathcal S_\mathrm{herm}$.

Daraus darf **nicht** geschlossen werden, dass die Faktoren $s(s-1)$ in der vollständigen
expliziten Formel irrelevant sind. Ihre Beiträge können als Konturresiduen oder
Randterme erscheinen, selbst wenn das kritische-Linien-Integral des rohen Symbols
für reell-gerades $h$ verschwindet.

Daher gilt:

$$
\Lambda_{\mathbb A}^\mathrm{weak}(f_\mathrm{fin},h)
= \Lambda_\mathrm{fin}(f_\mathrm{fin}) + \Lambda_\Gamma(h)
\quad\text{(Gammaterm only)}
$$

und separat offen:

$$
\boxed{[O\text{-}220\text{-}1\text{-PD3d4-pole-functional}]\quad?[O].}
\quad\text{(kein Anschluss in NEU-220g)}
$$

---

## 6. Objekt XXX — Fortschritt nach NEU-220g

NEU-220g zeigt zum ersten Mal, dass die archimedische Kette aus NEU-220f
$\Gamma_\mathbb{R}\to S_\infty\to Q_\infty\to\Lambda_\Gamma$ mit einem endlichen
Port $\Lambda_\mathrm{fin}$ typkorrekt addiert werden kann, ohne vorzeitig
eine Kopplung zu behaupten.

Der Kandidat für Objekt XXX nimmt jetzt die folgende Gestalt an:

$$
\boxed{
\text{Objekt XXX} = \Bigl(\mathcal S_{\mathbb A}^\mathrm{weak},\,
\Lambda_{\mathbb A}^\mathrm{weak} = \Lambda_\mathrm{fin}+\Lambda_\Gamma,\,
\mathscr S_\infty = M_{S_\infty}\Bigr)
}
$$

**Noch fehlende Bestandteile:**
1. Typisierung von $\mathcal S_\mathrm{fin}$ (PD-5a1)
2. Gemeinsame Testfunktion aus $\mathcal S(\mathbb A)$ (PD-5a3)
3. Vollständige Weil-Formel mit Polterm (PD-3d4, PD-5b)
4. Intrinsisches Streusystem $S_\infty$ aus $(H_0,H_1)$ (PD-4c4)

---

## 7. Aktualisierter DAG-Stand NEU-220 (nach NEU-220g)

```
PD-1   checkmark[K/M]_part
PD-2   checkmark[K/M]
PD-3   checkmark[K/M]   (Gamma-Distribution vollständig)
  └── [PD3d4-pole-functional]  ?[O]   <- Polterm auf S_herm
PD-4   checkmark[K/M]_part
  ├── PD-4a  checkmark[M]_neg   Hilbertspur No-Go
  ├── PD-4b  checkmark[K/M]    semifinite Spur tau_infty
  ├── PD-4c1 checkmark[K/M]    S_infty unitar
  ├── PD-4c2 checkmark[K/M]    Q_infty = M_gamma_sym
  ├── PD-4c3 checkmark[M]      Spurrueckgewinnung (reell-gerade)
  └── PD-4c4 ?[O]              echtes Streusystem (H_0,H_1)
PD-5a  (freigegeben ab PD-4b/c3)
  ├── PD-5a1 ?[O]   endlicher Port Lambda_fin (4 Audit-Unterfragen)
  ├── PD-5a2 ?[O]   schwache direkte Summe (bedingt durch PD-5a1)
  ├── PD-5a3 ?[O]   gemeinsamer Testfunktionsparameter
  └── PD-5a4 ?[O]   Tensorprodukt-Augmentation
PD-5b  GESPERRT bis PD-4c4 >= checkmark[M]
```

---

*Datei: `katalog/NEU-220g_Schwacher_endlich-archimedischer_Anschluss.md` | 25. Juli 2026*  
*Kernresultat: PD-5a-Struktur entworfen; PD-5a1 mit 4 Audit-Unterfragen; PD-5a2 typkorrekt formuliert; Polterm strikt getrennt*  
*Quellen: NEU-28 (endliche Seite), NEU-220d–f (archimedische Seite)*
