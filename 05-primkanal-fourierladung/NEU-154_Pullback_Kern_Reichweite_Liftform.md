# NEU-154 — Pullback-, Kern- und Reichweitenanalyse der verbundenen Liftform

> Stand: 13. Juli 2026.
> Vorgänger: NEU-153 (Wohldefiniertheit von \(|c_p|^2\), §D.0.5).
> Nachfolger: NEU-155 (geplant: konkrete Gram-Berechnungen).
> Typ: Architekturknoten. Überführt abstrakte Liftgeometrie in konkrete Zielraumrechnung.

---

## Motivation und Einordnung

NEU-153 §D.0.5 lokalisiert die Entscheidung

\[
\mathcal{L}_p^{\mathrm{ch}} = \varnothing
\iff
v_p \perp E_p^{\mathrm{ch}}
\]

im positiv definiten Fall, benennt aber sieben offene Punkte. Alle diese Punkte
hängen an einer einzigen unerledigten Identifikation: dem Pullback der verbundenen
Paarung über \(C_p^{\mathrm{rel}}\).

**Ziel von NEU-154:** Den Pullback präzise herzustellen und danach alle verbleibenden
Entscheidungen auf konkrete Eigenschaften von \(C_p^{\mathrm{rel}}\) zu reduzieren —
**nicht** alle offenen Punkte durch den Pullback allein zu schließen.

Die Aussage ist:

> NEU-154 typisiert die verbundene Geometrie und reduziert sämtliche verbleibenden
> Entscheidungen auf Injektivitäts-, Normierungs-, Gram- und Dichtefragen für
> \(C_p^{\mathrm{rel}}\).

Der optimale Abschlusssatz lautet:

\[
\boxed{
\begin{aligned}
\langle x,y\rangle_{\mathrm{conn}}
  &= \langle C_p^{\mathrm{rel}}x,\, C_p^{\mathrm{rel}}y\rangle_{W_{\mathrm{res,rel}}},\\
N_{\mathrm{conn}}
  &= \ker C_p^{\mathrm{rel}},\\
\widehat{\mathcal{H}}_{p,\mathrm{conn}}^{\mathrm{lift}}
  &\cong \overline{\operatorname{ran}C_p^{\mathrm{rel}}},\\
\mathcal{L}_p^{\mathrm{ch}} = \varnothing
  &\iff C_p^{\mathrm{rel}}v_p \perp \overline{C_p^{\mathrm{rel}}(E_p^{\mathrm{ch}})}.
\end{aligned}
}
\tag{154.Ziel}
\]

---

## DAG-Position

```
NEU-41 §3 ──► NEU-153 §D.0.5 ──► NEU-154 ──► NEU-155 (Gram-Berechnungen)
                                      │
                                      └──► NEU-152 (Nichtentartung, bedingt)
                                      └──► NEU-150 (R-Cutoff [ZA], bedingt)
```

---

## NEU-154.A — Typkorrekte Pullbackformel

**Ziel:** Nachweis von

\[
\operatorname{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}(x^\# y)
= \langle C_p^{\mathrm{rel}}x,\, C_p^{\mathrm{rel}}y\rangle_{W_{\mathrm{res,rel}}}
\tag{PB}
\]

zunächst auf dem algebraischen Testraum

\[
\mathcal{D}_p := \operatorname{span}\{e_u V_p : u \in \mathbb{Z}\}.
\]

**Vorgehen:**

1. Überprüfe für Basisvektoren \(e_u V_p\), \(e_{u'} V_p\):

\[
\operatorname{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}((e_u V_p)^\# (e_{u'} V_p))
\stackrel{?}{=}
\langle C_p^{\mathrm{rel}}(e_u V_p),\, C_p^{\mathrm{rel}}(e_{u'} V_p)\rangle_{W_{\mathrm{res,rel}}}.
\tag{154.A.1}
\]

2. Prüfe Sesquilinearität und Hermitizität beider Seiten auf \(\mathcal{D}_p\).

3. Schließe durch Dichtheit von \(\mathcal{D}_p\) auf den vervollständigten Raum —
   erst nachdem (PB) auf \(\mathcal{D}_p\) gesichert ist.

**Wichtig:** (PB) darf nicht sofort auf dem gesamten Liftraum
\(\mathcal{H}_p^{\mathrm{lift}}\) behauptet werden. Die algebraische Verifikation
auf endlichen Linearkombinationen ist der notwendige erste Schritt.

**Konsequenz aus (PB):** Unmittelbar folgen
- Wohldefiniertheit von \(\langle\cdot,\cdot\rangle_{\mathrm{conn}}\) als Hermiteform
  auf \(\mathcal{D}_p\),
- positive Semidefinitheit: \(q_{\mathrm{conn}}(x) = \|C_p^{\mathrm{rel}}x\|^2 \geq 0\).

Positive **Definitheit** und Vollständigkeit folgen **nicht** automatisch;
sie werden in 154.B bzw. 154.E behandelt.

**Status:** ❓[O] — Verifikation von (154.A.1) auf Basisvektoren ausstehend.

---

## NEU-154.B — Nullraum und Definitheit

**Aus (PB) folgt unmittelbar:**

\[
N_{\mathrm{conn}} \cap \mathcal{D}_p
= \ker(C_p^{\mathrm{rel}}|_{\mathcal{D}_p}).
\tag{154.B.1}
\]

Die offene Definitheitsfrage reduziert sich auf drei getrennte Injektivitätstests,
in aufsteigender Stärke:

**Test 1** (Normierung des kanonischen Lifts):
\[
C_p^{\mathrm{rel}} v_p \neq 0.
\tag{154.B.T1}
\]

**Test 2** (Definitheit auf \(E_p^{\mathrm{ch}}\)):
\[
\ker C_p^{\mathrm{rel}} \cap E_p^{\mathrm{ch}} \stackrel{?}{=} \{0\}.
\tag{154.B.T2}
\]

**Test 3** (Definitheit auf dem für §153.D.0.5 relevanten Raum):
\[
\ker C_p^{\mathrm{rel}} \cap \bigl(\mathbb{C}v_p + E_p^{\mathrm{ch}}\bigr)
\stackrel{?}{=} \{0\}.
\tag{154.B.T3}
\]

Wenn (154.B.T3) gilt, ist \(\langle\cdot,\cdot\rangle_{\mathrm{conn}}\) positiv
definit auf \(\mathbb{C}v_p + E_p^{\mathrm{ch}}\), und die Voraussetzungen von
§153.D.0.5.B sind auf diesem Unterraum erfüllt.

**Äquivalenz:** Unter (PB) gilt die scharfe Äquivalenz

\[
\langle\cdot,\cdot\rangle_{\mathrm{conn}} \text{ positiv definit auf } M
\iff
C_p^{\mathrm{rel}}|_M \text{ injektiv},
\]

für jeden Unterraum \(M \subseteq \mathcal{D}_p\).

**Status:** T1 ❓[O], T2 ❓[O], T3 ❓[O].

---

## NEU-154.C — Normierung des kanonischen Lifts

**Ziel:** Explizite Berechnung von

\[
C_p^{\mathrm{rel}} v_p = C_p^{\mathrm{rel}}(e_0 V_p)
\in W_{\mathrm{res,rel}},
\]

und danach

\[
\|C_p^{\mathrm{rel}} v_p\|_{W_{\mathrm{res,rel}}}^2.
\tag{154.C.1}
\]

Unter (PB) gilt:

\[
\|v_p\|_{\mathrm{conn}} = 1
\iff
\|C_p^{\mathrm{rel}} v_p\|_{W_{\mathrm{res,rel}}} = 1.
\]

Dies ist der Konventionstransfer aus NEU-153 §D.0.5.B (⚠[Konventionstransfer offen]),
reduziert auf eine konkrete Norm-Berechnung im Zielraum \(W_{\mathrm{res,rel}}\).

**Drei mögliche Ausgänge:**

| Ergebnis | Konsequenz |
|---|---|
| \(\|C_p^{\mathrm{rel}}v_p\|^2 = 1\) | Normierungsannahme bestätigt; §153.D.0.5.B unverändert anwendbar |
| \(\|C_p^{\mathrm{rel}}v_p\|^2 = \alpha \neq 1\) | Neuskalierung \(v_p \mapsto v_p/\sqrt{\alpha}\) nötig; Faserbedingung anpassen |
| \(\|C_p^{\mathrm{rel}}v_p\|^2 = 0\) | \(v_p \in N_{\mathrm{conn}}\); T1 negativ; grundlegende Revision |

**Status:** ❓[O] — Berechnung ausstehend.

---

## NEU-154.D — Gemischte Gramwerte

**Ziel:** Für \(u \neq 0\), explizite Berechnung von

\[
g_{0u}^{(p)}
= \langle C_p^{\mathrm{rel}} v_p,\, C_p^{\mathrm{rel}}(e_u V_p)\rangle_{W_{\mathrm{res,rel}}}.
\tag{154.D.1}
\]

Dies ist die entscheidende konkrete Berechnung für die Existenzfrage in §153.D.0.5.

Unter (PB) entscheidet (154.D.1) die Liftgeometrie vollständig:

**Drei mögliche Ergebnisse:**

| Ergebnis | Konsequenz |
|---|---|
| \(g_{0u}^{(p)} = 0\) für alle \(u \neq 0\) | Keine geladenen Fourierlifts im algebraischen Unterraum; \(\mathcal{L}_p^{\mathrm{ch}} = \varnothing\) in \(\mathcal{D}_p\) |
| \(g_{0u}^{(p)} \neq 0\) für mindestens ein \(u\) | Unmittelbar ein geladener normierter Lift nach §153.D.0.5.B |
| Alle \(g_{0u}^{(p)} = 0\), aber Abschluss nichtorthogonal | Nur möglich wenn \(E_p^{\mathrm{ch}}\) nicht dicht in \(K_{p,\mathrm{conn}}^{\mathrm{ch}}\); bei dichter linearer Hülle erzwingt \(g_{0u}^{(p)} = 0\) für alle \(u\) bereits Orthogonalität zum gesamten Abschluss |

**Übersetzung in den Zielraum:** Sei

\[
M_p^{\mathrm{ch}} := \overline{C_p^{\mathrm{rel}}(E_p^{\mathrm{ch}})} \subseteq W_{\mathrm{res,rel}}.
\]

Dann gilt unter (PB) und bei Injektivität von \(C_p^{\mathrm{rel}}|_{\mathbb{C}v_p + E_p^{\mathrm{ch}}}\):

\[
P_{K_{p,\mathrm{conn}}^{\mathrm{ch}}}^{\mathrm{conn}} v_p = 0
\iff
P_{M_p^{\mathrm{ch}}}\bigl(C_p^{\mathrm{rel}} v_p\bigr) = 0.
\tag{154.D.2}
\]

Das verlagert die abstrakte Projektionsfrage aus NEU-153 vollständig in den
konkret zerlegten Zielraum \(W_{\mathrm{res,rel}}\).

**Status:** ❓[O] — Berechnung ausstehend; hängt von 154.A (Pullback) und 154.C (Normierung).

---

## NEU-154.E — Reichweite und Hilbertvervollständigung

**Ziel:** Nachweis der kanonischen Isometrie

\[
\mathcal{H}_p^{\mathrm{lift}} / \ker C_p^{\mathrm{rel}}
\xrightarrow{\;\sim\;}
\overline{\operatorname{ran} C_p^{\mathrm{rel}}} \subseteq W_{\mathrm{res,rel}},
\qquad
[x] \longmapsto C_p^{\mathrm{rel}} x.
\tag{154.E.1}
\]

**Wichtiger Hinweis:** Diese Isometrie folgt formal aus (PB) durch den
Isomorphiesatz für Hilberträume. Vollständigkeit des Quotienten ergibt sich
jedoch nur, wenn \(\overline{\operatorname{ran} C_p^{\mathrm{rel}}}\) als
abgeschlossener Teilraum von \(W_{\mathrm{res,rel}}\) (vollständig) vollständig ist
— was per Definition gilt.

**Konsequenz:** Die verbundene Hilbertvervollständigung ist

\[
\widehat{\mathcal{H}}_{p,\mathrm{conn}}^{\mathrm{lift}}
\cong \overline{\operatorname{ran} C_p^{\mathrm{rel}}}
\subseteq W_{\mathrm{res,rel}}.
\tag{154.E.2}
\]

**Nicht** notwendig isomorph zum ursprünglichen Liftraum \(\mathcal{H}_p^{\mathrm{lift}}\)
selbst (falls \(C_p^{\mathrm{rel}}\) nicht surjektiv oder \(\mathcal{H}_p^{\mathrm{lift}}\)
nicht vollständig bezüglich \(\|\cdot\|_{\mathrm{conn}}\)).

Nach (154.E.2) lässt sich die Orthogonalprojektion aus §153.D.0.5 intrinsisch im
Zielraum schreiben:

\[
P_{K_{p,\mathrm{conn}}^{\mathrm{ch}}}^{\mathrm{conn}} v_p = 0
\iff
P_{M_p^{\mathrm{ch}}}\bigl(C_p^{\mathrm{rel}} v_p\bigr) = 0,
\]

was (154.D.2) bestätigt und den Übergang nach NEU-155 vorbereitet.

**Status:** ❓[O] — formal klar unter (PB); Abschluss von (PB) auf \(\mathcal{D}_p\) vorausgesetzt.

---

## NEU-154.F — Separate Dichtefrage

**Ziel:**

\[
K_p \stackrel{?}{=} \overline{E_p^{\mathrm{ch}}}^{\,\|\cdot\|_{\mathrm{lift}}}.
\tag{154.F.1}
\]

**Epistemischer Status:** Diese Frage ist logisch von 154.A–E getrennt.
Sie ist eine Aussage über die primitive Projektion \(\pi_{\mathrm{prim}}\) und
den algebraischen Aufbau ihres Kerns — sie folgt **nicht** aus dem Pullback (PB).

Auch ein vollständig erfolgreicher Pullback- und Gramnachweis (154.A–D) kann die
Existenz geladener Fourierlifts entscheiden, ohne den gesamten Kern von
\(\pi_{\mathrm{prim}}\) zu klassifizieren.

**Zwei Szenarien:**

| Szenario | Konsequenz |
|---|---|
| \(K_p = \overline{E_p^{\mathrm{ch}}}^{\|\cdot\|_{\mathrm{lift}}}\) | Kern vollständig durch Fouriermoden erzeugt; \(K_p = K_{p,\mathrm{conn}}^{\mathrm{ch}}\) unter Normvergleich möglich |
| \(K_p \supsetneq \overline{E_p^{\mathrm{ch}}}^{\|\cdot\|_{\mathrm{lift}}}\) | Neutraler Anteil \(K_p \setminus E_p^{\mathrm{ch}}\) strukturell vorhanden; \(\mathcal{L}_p^{\mathrm{full}} \supsetneq \mathcal{L}_p^{\mathrm{ch}}\) nicht nur nominell |

**Hinweis:** Selbst wenn (154.F.1) positiv beantwortet wird, bleibt die
Normvergleichsfrage

\[
\overline{E_p^{\mathrm{ch}}}^{\,\|\cdot\|_{\mathrm{lift}}}
\stackrel{?}{=}
\overline{E_p^{\mathrm{ch}}}^{\,\|\cdot\|_{\mathrm{conn}}}
\tag{154.F.2}
\]

eine gesonderte Untersuchung, da \(\|\cdot\|_{\mathrm{lift}}\) und
\(\|\cdot\|_{\mathrm{conn}}\) a priori verschiedene Normen sind.

**Status:** ❓[O] — epistemisch getrennt; nicht Voraussetzung für 154.D.

---

## Statusübersicht

| Abschnitt | Aufgabe | Hängt an | Status |
|---|---|---|---|
| 154.A | Pullbackformel (PB) auf \(\mathcal{D}_p\) | NEU-41 §3 | ❓[O] |
| 154.B | Nullraum \(N_{\mathrm{conn}} = \ker C_p^{\mathrm{rel}}\), Tests T1–T3 | 154.A | ❓[O] |
| 154.C | Normierung \(\|C_p^{\mathrm{rel}}v_p\|^2\) | 154.A | ❓[O] |
| 154.D | Gramwerte \(g_{0u}^{(p)}\), Projektion in \(W_{\mathrm{res,rel}}\) | 154.A, 154.C | ❓[O] |
| 154.E | Reichweite \(\widehat{\mathcal{H}} \cong \overline{\operatorname{ran}C_p^{\mathrm{rel}}}\) | 154.A | ❓[O] formal klar |
| 154.F | Dichtefrage \(K_p = \overline{E_p^{\mathrm{ch}}}\) | unabhängig | ❓[O] separat |

---

## Verweise

- **NEU-41 §3:** Definition von \(C_p^{\mathrm{rel}}\), Wohlbestimmtheitsbedingung (41.4),
  \(\delta_{r,0}\)-Regel, verbundene Paarung — primäre Quelle für 154.A
- **NEU-44 §44.2:** Normierungsdaten \(\|e_r V_p\|\) — Quellnorm für 154.C
- **NEU-153 §D.0.5:** Abstrakte Liftgeometrie — durch 154.A–E in Zielraum übertragen
- **NEU-152 §152.6:** Abhängigkeitsverweis (Nichtentartung bedingt auf NEU-153/154)
- **NEU-150:** R-Cutoff-Zusatzannahme [ZA] bedingt auf zweiseitige Kontrolle von
  \(|c_p|^2\) — ebenfalls bedingt auf NEU-153/154
