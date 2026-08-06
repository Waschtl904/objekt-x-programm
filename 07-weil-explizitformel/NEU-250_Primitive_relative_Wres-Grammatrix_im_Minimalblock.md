# NEU-250 — Primitive relative Wres-Grammatrix im Minimalblock

**Kennung:** NEU-250  
**Ordner:** `07-weil-explizitformel/`  
**Datum:** 2026-08-06  
**Knoten:** `[O-221-1c1a0-A]`  
**Vorgänger:** NEU-221e §11 (kleinster nächster atomarer Knoten), NEU-249 §9 (Rücklauf)  
**Priorität:** 1 (laut OFFENE_PROBLEME.md)  
**Typ:** Direktrechnung mit fünf zugelassenen Ausgängen — **Ausgang E eingetreten**

---

## 0 — Arbeitsauftrag

Gesucht war nicht ein einzelner Diagonalwert, sondern ein **Minimalblock mit Kreuztermen**:
Für festes \(p\) und den kleinsten zulässigen Cutoff, für mindestens zwei verschiedene
Zielindizes \(R, R'\):

\[
G_p(R,R) := h_{\mathrm{Wres,rel}}\bigl(E^{\mathrm{rel}}_{R;1\to p}, E^{\mathrm{rel}}_{R;1\to p}\bigr),
\qquad
G_p(R,R') := h_{\mathrm{Wres,rel}}\bigl(E^{\mathrm{rel}}_{R;1\to p}, E^{\mathrm{rel}}_{R';1\to p}\bigr),
\]

und analog \(G_p(R',R'), G_p(R',R)\), gefolgt von

\[
\det\begin{pmatrix}G_p(R,R)&G_p(R,R')\\G_p(R',R)&G_p(R',R')\end{pmatrix}
\]

und der Kernbestimmung dieses \(2\times2\)-Blocks. Grund: Ein nichtverschwindender
Diagonalwert allein entscheidet weder Diagonalität der Form noch Trivialität des Radikals
(Fehlermuster aus NEU-246 — vgl. NEU-249 §0).

---

## 1 — Was zur Berechnung benötigt wird

Die kantendiagonale Wres-Paarung ist in NEU-44 (44.7) **definiert**, nicht abgeleitet:

\[
\bigl\langle E_{r;\,m\xrightarrow{p}pm}, E_{r';\,m'\xrightarrow{q}qm'}\bigr\rangle_{\mathrm{Wres,rel}}
:= \delta_{p,q}\,\delta_{m,m'}\,\langle E_{r,pm}, E_{r',pm}\rangle_{\mathrm{Wres}}.
\]

Damit reduziert sich die gesuchte Grammatrix \(G_p(R,R')\) auf die **kollabierte** Paarung
\(\langle E_{R,pm}, E_{R',pm}\rangle_{\mathrm{Wres}}\) im Jacobi-Zielraum \(\mathcal H_{J,N}\).
Um diese zu berechnen, braucht man eine explizite Formel für

\[
\langle E_a, E_b\rangle_{\mathrm{Wres}} = Wres_{BC}^{\mathrm{top}}(E_a^\# E_b)
\]

auf zwei konkreten Basiselementen \(E_a, E_b\) von \(B_3\) bzw. dessen Jacobi-Bild.

---

## 2 — Quellenprüfung: existiert eine berechenbare Formel?

Drei Kandidatendateien wurden direkt geprüft.

### 2.1 — NEU-44 (kantendiagonale Definition)

NEU-44 (44.7) **definiert** \(Wres_{\mathrm{rel}}\) durch Rückgriff auf die gewöhnliche
\(Wres\)-Paarung, liefert aber selbst **keine Zahlenformel** für \(\langle E_a,E_b\rangle_{Wres}\).
Die Intrinsizität aus \(Wres_{BC}^{\mathrm{top}}\) ist dort ausdrücklich als \(\text{?[O]}\)
geführt (Statusmatrix, letzte Zeilen).

### 2.2 — NEU-24 (Frobenius-Nichtausgeartetheit)

NEU-24 beweist **Existenzaussagen** ("\([c]\neq 0 \Rightarrow \exists[\Psi]: B([\Psi],[c])\neq 0\)")
über Euler-Homotopie und Koszul-Azyklizität. Das ist ein reiner Nichtverschwindenssatz auf
Kohomologieklassen — **keine explizite Zahl** für \(B([\Psi],[c])\) auf zwei gegebenen
Basiserzeugern. Der Auswertungskoeffizient \(\varepsilon(c,a_1,\dots,a_4)\) in §3.1 wird
selbst nicht berechnet, sondern nur als existent postuliert ("universelle
Koeffizientenformel", §3.1–3.2).

### 2.3 — NEU-31 (Wres-GNS und Determinante)

NEU-31 arbeitet ausschließlich auf der Ebene von Spurformeln
(\(\operatorname{Tr}_{Wres}^{\mathrm{top}}\), \(\det_{Wres}\)) und formalen Identitäten mit
\(\xi(s)\). Es gibt dort **keine** punktweise Formel für \(\langle E_a,E_b\rangle_{Wres}\)
auf zwei konkreten Erzeugern \(E_a,E_b\); \(Wres_{BC}^{\mathrm{top}}\) wird nur als Spur auf
ganzen Operatoren ausgewertet, nicht als punktweise sesquilineare Form auf Basiselementen.

### 2.4 — Ergebnis der Quellenprüfung

\[
\boxed{
\text{Keine der geprüften Quellen liefert eine direkt auswertbare Zahlenformel für}\;
\langle E_a,E_b\rangle_{Wres}\;\text{auf zwei expliziten Basiserzeugern.}
}
\]

\(Wres_{BC}^{\mathrm{top}}\) ist im gesamten geprüften Quellenbestand **symbolisch**
definiert (als Wodzicki-Residuum eines Operatorkalküls bzw. als Frobenius-Funktional auf
Hochschild-Klassen), aber an keiner Stelle auf zwei konkrete Erzeuger \(E_R, E_{R'}\)
heruntergerechnet.

---

## 3 — Gewählter Ausgang: E

Von den fünf zugelassenen Ausgängen tritt:

\[
\boxed{
\textbf{Ausgang E: Keine berechenbare Quellenformel.}
}
\]

Nicht eingetreten sind (da sie eine Zahl voraussetzen, die nicht existiert):

- A (explizite positive Gramform) — nicht prüfbar
- B (explizite indefinite Gramform) — nicht prüfbar
- C (nichttriviales Radikal explizit gefunden) — nicht prüfbar
- D (Hebungsabhängigkeit direkt gezeigt) — nicht prüfbar

**Wichtige Präzisierung.** Ausgang E bedeutet nicht "das Problem ist unlösbar", sondern:
Die Lokalisierung der symbolischen Lücke ist jetzt exakt — wir wissen, **welche** Datei
konstruktiv werden muss, bevor der Minimalblock überhaupt eine Zahl liefern kann.

---

## 4 — Präzise Lokalisierung der Lücke

Der Wodzicki-Residuumsformalismus \(Wres_{BC}^{\mathrm{top}}\) geht auf die ursprüngliche
Konstruktion der Objekt-X-Algebra \(B_3\) als Operatoralgebra mit Symbolkalkül zurück
(vgl. NEU-15–20). Die Paarung ist dort definiert als Residuum eines
pseudodifferentiellen Symbols. Um \(\langle E_a,E_b\rangle_{Wres}\) numerisch zu erhalten,
fehlt genau ein Baustein:

\[
\boxed{
\text{Explizite Symbolrepräsentation der Basiselemente } e_uV_p \text{ als}
\text{ pseudodifferentielle Operatoren, deren Wodzicki-Residuum direkt}
\text{ (nicht nur formal) berechenbar ist.}
}
\]

Diese Symboldarstellung ist in keiner der geprüften Dateien (NEU-15–20, NEU-24, NEU-31,
NEU-44) explizit ausgeführt. Alle Resultate arbeiten auf der Ebene von
Kohomologieklassen, Spurformeln oder Kollapsargumenten — nie auf der Ebene einer
konkreten Zwei-Erzeuger-Auswertung.

---

## 5 — Konsequenz für `[O-221-1c1a0]` und `[O-246/0corr-2]`

Damit ist präzisiert, warum sowohl `[O-221-1c1a0]` als auch der Wres-Gramabstieg von
`[O-246/0corr-2]` an derselben Stelle blockiert sind: **Es gibt noch keine einzige
berechnete Zahl** \(\langle E_a,E_b\rangle_{Wres}\) im gesamten Programm. Jede
nachgelagerte Frage — Radikal, Diagonalität, Hebungsunabhängigkeit, Kanonizität der
Gewichte \(b_{s,u}\) — erbt diese Lücke.

\[
\boxed{
[O\text{-}221\text{-}1c1a0\text{-A}]:\;\checkmark[K]_{\mathrm{neg}}
\quad\text{(Quellenlage geprüft, Lokalisierung exakt, keine Zahl verfügbar)}
}
\]

---

## 6 — Nächster atomarer Knoten

\[
\boxed{
[O\text{-}221\text{-}1c1a0\text{-B}]\quad
\text{Explizite Symboldarstellung von } e_uV_p \text{ und direkte Wodzicki-Residuumsrechnung}
}
\]

Konkreter Auftrag:

1. Wähle die kleinste konkrete Realisierung von \(B_3\) als Symbolalgebra (z. B. über die
   in NEU-15–17 verwendete Konstruktion) und schreibe \(e_uV_p\) explizit als Symbol
   \(\sigma_{u,p}(\xi)\) einer festen Ordnung.
2. Berechne das Wodzicki-Residuum \(Wres(\sigma_{u,p}^\# \sigma_{u',p'})\) für zwei feste
   kleine Indexpaare \((u,p), (u',p')\) als **Zahl oder geschlossene Formel**.
3. Setze das Ergebnis in NEU-44 (44.7) ein und berechne \(G_p(R,R), G_p(R,R'),
   G_p(R',R), G_p(R',R')\) für den kleinsten Cutoff.
4. Erst danach: Determinante, Kern, Radikaltest gegen \(\Delta_p^{\mathrm{adm}}\)
   (Rücklauf zu NEU-221e §11).

Erst wenn dieser Knoten eine Zahl liefert, ist der ursprünglich beabsichtigte
Minimalblock-Test aus §0 überhaupt ausführbar.

---

## 7 — Repository-Korrekturblock

```text
AUDIT [O-221-1c1a0-A] (NEU-250, Stand 2026-08-06)

Auftrag:  Minimalblock G_p(R,R'), Kreuzterme, Determinante, Kern
Ergebnis: Ausgang E - keine berechenbare Quellenformel

Geprueft:
  NEU-44 (44.7)  - Definition kantendiagonal, keine Zahl        ?[O]
  NEU-24 §3       - Existenzsatz, kein expliziter Koeffizient    ?[O]
  NEU-31          - nur Spurformeln, keine Zwei-Erzeuger-Zahl    ?[O]

Lokalisierte Luecke:
  Explizite Symboldarstellung von e_uV_p als pseudodifferentielles
  Symbol mit direkt berechenbarem Wodzicki-Residuum FEHLT im gesamten
  Quellenbestand (NEU-15-20, NEU-24, NEU-31, NEU-44).

Status [O-221-1c1a0-A]: checkmark[K]_neg (Lokalisierung exakt)

Naechster Knoten:
  [O-221-1c1a0-B]: Explizite Symboldarstellung + direkte
  Residuumsrechnung fuer mindestens zwei Indexpaare.

Ruecklauf:
  Erst nach [O-221-1c1a0-B] ist der Minimalblock-Test (dieser Knoten,
  Teil A) tatsaechlich ausfuehrbar. [O-246/0corr-2] (Wres-Gramabstieg)
  erbt dieselbe Blockade.
```

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung des RH-Forschungsjournals*
