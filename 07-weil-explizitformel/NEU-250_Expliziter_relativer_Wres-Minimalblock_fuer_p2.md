# NEU-250 — Expliziter relativer Wres-Minimalblock für \(p=2\)

**Kennung:** NEU-250 (ersetzt frühere Fassung desselben Dateinamens/Anspruchs)  
**Ordner:** `07-weil-explizitformel/`  
**Datum:** 2026-08-06  
**Knoten:** `[O-221-1c1a0-A]` — Primitive Wres-Grammatrix und Radikal im kleinsten Primsektor  
**Priorität:** 1 (OFFENE_PROBLEME.md)  
**Methode:** zweistufig, mit hartem Erfolgsmaßstab: entweder eine konkrete \(2\times2\)-Matrix
auf dem Papier, oder ein präziser Beweis, dass die Quellen keine solche Matrix definieren.

---

## 0 — Warnung gegen Vorwegnahme

Diese Datei behauptet **nicht**, \(\mathcal N_{\mathrm{Wres,rel}}\) vollständig zu bestimmen.
Das Radikal ist nur abstrakt definiert:

\[
\mathcal N_{\mathrm{Wres,rel}} = \{v : \langle v,w\rangle_{\mathrm{Wres,rel}} = 0\ \forall w\},
\]

während die konkrete relative Wres-Grammatrix und sogar ihre Primkantendiagonalität nach
NEU-221e und NEU-44 offen sind [`?[O]`]. Ziel ist ausschließlich die **Extraktion einer
auswertbaren Formel** und, falls möglich, ihre Anwendung auf einen konkreten \(2\times2\)-Block.

---

## Stufe A — Quellenformel extrahieren

### A.1 — Zielformel

\[
G_{2,N}(R,R') := \left\langle E^{\mathrm{rel}}_{R;\,1\to2}, E^{\mathrm{rel}}_{R';\,1\to2}\right\rangle_{\mathrm{Wres,rel}}.
\]

**Explizit ausgeschlossen** als stillschweigende Annahme: \(G_{2,N}(R,R') = \delta_{RR'}\).
NEU-221e §3.1/§9 hält fest, dass Norminvarianz nur dem Test \(f\equiv1\) entspricht und dass
der Pullback von \(Wres\) **nicht automatisch primkantendiagonal** ist [cite-intern NEU-221e].

### A.2 — Reduktion über NEU-44 (44.7)

NEU-44 definiert (nicht ableitet):

\[
\bigl\langle E_{r;\,m\xrightarrow{p}pm}, E_{r';\,m'\xrightarrow{q}qm'}\bigr\rangle_{\mathrm{Wres,rel}}
:= \delta_{p,q}\,\delta_{m,m'}\,\langle E_{r,pm}, E_{r',pm}\rangle_{\mathrm{Wres}}.
\]

Damit reduziert sich \(G_{2,N}(R,R')\) für \(p=2\), \(m=1\) auf

\[
G_{2,N}(R,R') = \langle E_{R,2}, E_{R',2}\rangle_{\mathrm{Wres}},
\]

wobei \(E_{R,2} = \Pi_{J,N}(e_R V_2)\) das kollabierte Jacobi-Bild ist. Damit ist die Aufgabe
auf die **gewöhnliche** \(Wres\)-Paarung zweier konkreter Jacobi-Basisvektoren reduziert.
Die Intrinsizität dieser Reduktion selbst ("folgt \(Wres_{\mathrm{rel}}\) aus
\(Wres_{BC}^{\mathrm{top}}\)?") bleibt in NEU-44 als `?[O]` geführt.

### A.3 — Prüfung NEU-39 (verbundene Spur)

NEU-39 liefert eine normalisierte **verbundene Spur** \(\operatorname{Tr}_{Wres}^{\mathrm{conn}}\)
auf dem primitiven Primquotienten, mit der Kernidentität
\(P_N + \operatorname{Tr}^{\mathrm{conn}} \Rightarrow \zeta'/\zeta\). Das ist eine **Spurformel
über ganze Operatoren**, nicht eine punktweise Gramform auf zwei Basisvektoren
\(E_{R,2}, E_{R',2}\). Aus NEU-39 folgt keine Formel für \(\langle E_a,E_b\rangle_{Wres}\).

### A.4 — Prüfung NEU-41 (Selektionsregel und Kontinuanten)

NEU-41 (41.15) gibt eine **Selektionsregel**:

\[
\langle E_{r,n}, C_p\varepsilon_p\rangle_{Wres} \neq 0 \implies (r,n)\sim_{Wres}(u+ps,pm).
\]

Das ist eine Nichtverschwindungsbedingung, keine Zahl. Die konkrete Auswertung (41.16),

\[
M_p(s) = |\kappa_{p,u,s,m}|^2_{Wres}\,\frac{P_j^L(z)\,P_{M-j}^R(z)}{P_{M+1}^{(pm,a)}(z)},
\]

verwendet den Faktor \(|\kappa_{p,u,s,m}|^2_{Wres} = \langle E_{r,pm}, E_{r,pm}\rangle_{Wres}\)
als **Vorfaktor**, berechnet ihn aber selbst nicht — er wird von NEU-41 als gegebene Größe
vorausgesetzt, nicht konstruiert. Die Kontinuanten \(P_j^L, P_{M-j}^R, P_{M+1}\) aus NEU-37
betreffen den **Resolventen** von \(A_N^-\) auf Fourier-Orbits, nicht die \(Wres\)-Norm der
Basisvektoren \(E_{r,n}\) selbst — NEU-37 setzt diese Norm ebenfalls stillschweigend als
Standard-\(\ell^2\) voraus (§3–§4, Wres-Spur wird auf diagonalen Komponenten *definiert*, nicht
aus einer unabhängig konstruierten Gramform abgeleitet).

### A.5 — Prüfung NEU-31 (Wres-GNS und Determinante)

NEU-31 arbeitet ausschließlich mit \(\operatorname{Tr}_{Wres}^{\mathrm{top}}\) und
\(\det_{\mathrm{Wres}}\) auf ganzen Operatoren; es gibt dort **keine** punktweise Formel für
\(\langle E_a,E_b\rangle_{Wres}\) auf zwei konkreten Erzeugern (vgl. NEU-31 §1.1–§2.1: das
Funktional \(\tau=Wres_{BC}^{\mathrm{top}}\) wird nur über GNS-Nullraum \(N_\tau\) und die
allgemeine Beziehung \(\langle[a],[b]\rangle_\tau=\tau(a^*b)\) beschrieben, nie an zwei
konkreten Basiselementen \(e_uV_p\) ausgewertet).

### A.6 — Ergebnis Stufe A

\[
\boxed{
\textbf{Ausgang E.}\quad
\text{Die geprüften Quellen (NEU-19/24/31/37/39/41/44) definieren}\\
\text{keine auswertbare Gramform } \langle E_a,E_b\rangle_{Wres}\text{ auf zwei konkreten Basisvektoren.}
}
\]

Alle sechs Dateien verwenden \(Wres_{BC}^{\mathrm{top}}\) entweder als:

1. Spurfunktional auf ganzen Operatoren (NEU-31, NEU-39, NEU-37), oder
2. Existenzaussage auf Kohomologieklassen (NEU-19/24), oder
3. Platzhaltergröße/Vorfaktor, der selbst nicht konstruiert wird (NEU-41, \(|\kappa|^2_{Wres}\)), oder
4. Definition ohne Rückführung auf eine berechenbare Quelle (NEU-44, 44.7).

**Negativer Befund, wie in der Aufgabenstellung vorgesehen:**

\[
\boxed{
\text{Der Wres-Zielraum ist im Repository nicht rechnerisch definiert,}\\
\text{sondern nur symbolisch postuliert.}
}
\]

---

## Stufe B — entfällt in dieser Fassung

Da Stufe A keine auswertbare Paarungsformel liefert, kann der Minimalblock

\[
\mathcal V_{\min} = \operatorname{span}\{E^{\mathrm{rel}}_{R_0;1\to2}, E^{\mathrm{rel}}_{R_1;1\to2}\},
\qquad R_0\neq R_1,
\]

**nicht** numerisch ausgewertet werden. Es gibt keine Zahlen für \(G(R_0,R_0)\),
\(G(R_0,R_1)\), \(G(R_1,R_0)\), \(G(R_1,R_1)\), und folglich auch keine Determinante, keinen
Rang, kein Radikal und keine Trägheit \((n_+,n_-,n_0)\) für \(G_{\min}\) in dieser Datei.

> **Wichtig.** Dies ist kein Versagen der Rechnung, sondern das exakte Ergebnis von Stufe A:
> Ausgang E war einer der fünf zulässigen Enden und tritt hier kontrolliert ein.

### B.0 — Warum auch der Cutoff \(N\) nicht gewählt werden musste

Die Wahl des kleinsten zulässigen Cutoffs \(N\) (mit \(N=2\) als Kandidat) ist nachrangig zur
Existenz einer Paarungsformel. Ohne Stufe A ist jede \(N\)-Wahl folgenlos, da keine Zahl
produziert werden kann. Diese Frage wird an `[O-221-1c1a0-A0]` weitergegeben.

---

## Hebungsabstieg (nicht getestet)

Da keine Grammatrix vorliegt, kann auch der Hebungsabstiegstest

\[
\widetilde T_2^{\mathrm{raw}}(\Delta_2^{\mathrm{adm}}) \subseteq \mathcal N_{\mathrm{Wres,rel}}
\]

nicht gerechnet werden — unabhängig davon fehlt zusätzlich noch eine vollständige
Definition von \(\Delta_2^{\mathrm{adm}}\) selbst (NEU-221e §2, `?[O]`). NEU-228 wird hier
korrekt zitiert: ein einfacher Fouriermodus \(e_uV_2\) mit \(u\neq0\) ist **keine** zulässige
Hebungsdifferenz, sondern nur eine Kernrichtung \(k\in K_2\). Ein Test auf \(e_uV_2\) allein
würde daher, selbst bei vorhandener Grammatrix, nur den schwächeren algebraischen Test

\[
\widetilde T_2^{\mathrm{raw}}(\delta) \in \mathcal N_{\mathrm{Wres,rel}}, \qquad \delta\in K_2,
\]

liefern — nicht den vollen Hebungsabstieg. Da bereits Stufe A negativ ausfällt, wird dieser
Test hier nicht durchgeführt, um keine Scheingenauigkeit zu erzeugen.

---

## Statusbuchung

| Teilfrage | Status |
|---|---|
| Reduktion \(G_{2,N} \to \langle E_{R,2},E_{R',2}\rangle_{Wres}\) via NEU-44 (44.7) | \(\checkmark[M]\) als Reduktionsschritt |
| Intrinsizität dieser Reduktion aus \(Wres_{BC}^{\mathrm{top}}\) | \(?[O]\) (NEU-44) |
| Auswertbare Formel für \(\langle E_a,E_b\rangle_{Wres}\) in NEU-19/24/31/37/39/41/44 | **nicht vorhanden** — Ausgang E |
| \(2\times2\)-Minimalblock \(G_{\min}\) für \(p=2\) | nicht berechenbar mit aktuellem Quellenbestand |
| Rang, Determinante, Radikal, Trägheit von \(G_{\min}\) | nicht bestimmbar |
| Hebungsabstieg \(\widetilde T_2^{\mathrm{raw}}(\Delta_2^{\mathrm{adm}})\subseteq\mathcal N_{\mathrm{Wres,rel}}\) | nicht testbar (doppelt blockiert: keine Grammatrix, keine vollständige \(\Delta_2^{\mathrm{adm}}\)) |
| **Gesamtstatus `[O-221-1c1a0-A]`** | \(\checkmark[K]_{\mathrm{neg}}\) (Lokalisierung exakt, Ausgang E) |

---

## Nächster Knoten

Da keine Paarungsformel existiert:

\[
\boxed{
[O\text{-}221\text{-}1c1a0\text{-A0}]:\;\text{Konstruktion der relativen Wres-Paarung auf }\mathscr V_{\mathrm{rel},2,N}^{\mathrm{pre}}.
}
\]

Konkreter Auftrag für `[O-221-1c1a0-A0]`:

1. Gehe zurück zur ursprünglichen Konstruktion von \(Wres_{BC}^{\mathrm{top}}\) als
   Wodzicki-Residuum auf \(B_3\) (NEU-15–20) und prüfe, ob dort eine Symboldarstellung von
   \(e_uV_p\) existiert, aus der ein Residuum direkt (nicht nur als Spur über Operatoren)
   berechnet werden kann.
2. Falls ja: berechne \(\langle e_{u}V_2, e_{u'}V_2\rangle_{Wres}\) für mindestens zwei feste
   kleine Indexpaare als Zahl oder geschlossene Formel.
3. Setze das Ergebnis über NEU-44 (44.7) in \(G_{2,N}(R,R')\) ein.
4. Erst danach: Stufe B dieses Knotens (`[O-221-1c1a0-A]`) mit echten Zahlen nachholen.
5. Danach: `[O-221-1c1a0-B]` — Ausdehnung vom Minimalblock auf Erzeuger von
   \(\Delta_2^{\mathrm{adm}}\) (nur erreichbar nach A0 und Stufe B).

Falls `[O-221-1c1a0-A0]` zeigt, dass auch NEU-15–20 keine berechenbare Symboldarstellung
enthalten, ist damit bewiesen, dass der gesamte Objekt-X-Formalismus \(Wres_{BC}^{\mathrm{top}}\)
bisher nirgends auf eine konkrete Zahl heruntergerechnet hat — ein präziser, harter Befund
über den tatsächlichen Konstruktionsstand des Programms.

---

## Repository-Korrekturblock

```text
AUDIT/RECHNUNG [O-221-1c1a0-A] (NEU-250, Stand 2026-08-06)

Auftrag Stufe A: G_{2,N}(R,R') = <E_R;1->2, E_R';1->2>_Wres,rel extrahieren
Ergebnis Stufe A: Ausgang E - keine auswertbare Formel in den Quellen

Geprueft (mit Fundstellen):
  NEU-44 (44.7)  Definition kantendiagonal, keine Zahl, Intrinsizitaet ?[O]
  NEU-39         Spurformel ueber Operatoren, keine punktweise Gramform
  NEU-41 (41.15-41.16)  Selektionsregel + Kontinuanten, |kappa|^2_Wres
                        bleibt unkonstruierter Vorfaktor
  NEU-37         Kontinuanten betreffen A_N^- Resolvent, nicht die
                 Wres-Norm der Basisvektoren selbst
  NEU-31         nur Tr_Wres^top und det_Wres auf Operatoren
  NEU-24         Existenzsatz auf Kohomologieklassen, keine Zahl

Stufe B: nicht durchgefuehrt (kein numerischer Input verfuegbar)
Hebungsabstiegstest: nicht durchgefuehrt (doppelt blockiert)

Status [O-221-1c1a0-A]: checkmark[K]_neg

Negativer Befund:
  Der Wres-Zielraum ist im Repository nicht rechnerisch definiert,
  sondern nur symbolisch postuliert.

Naechster Knoten:
  [O-221-1c1a0-A0]: Konstruktion der relativen Wres-Paarung auf
  V_rel,2,N^pre - Ruecksprung zu NEU-15-20 (urspruengliche
  Symbolkalkuel-Konstruktion von B_3).

Danach erst: Stufe B dieses Knotens nachholbar, dann [O-221-1c1a0-B].
```

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung des RH-Forschungsjournals*
