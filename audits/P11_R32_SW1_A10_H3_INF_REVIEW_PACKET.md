# P11/R32 — SW1-A10 H3-INF Independent Review Packet

> **Stand:** 30. August 2026  
> **Ziel:** unabhängiger mathematischer Review des analytischen H3-INF-Schlusses.  
> **Noch kein independent GREEN für H3-INF.**

## A. Bereits zertifizierte finite Inputs

1. **H2 aggregierter Hubledger**
   - 11 \(t\)-Zellen;
   - 53 aggregierte nichtverschwindende Kanäle;
   - 115 Paarvorkommen;
   - 22 affine Bridge-Typen;
   - maximale Indexreichweite \(4\).

2. **H3-COVER**
   - freies physisches Band
     \[
     J=(0,L)\subset(0,a-R);
     \]
   - kanonische disjunkte Zonenauswahl
     \[
     Z_1=(0,e-R),
     \quad
     Z_2=(e-R,e),
     \quad
     Z_3=(e,L-\Delta),
     \quad
     Z_4=(L-\Delta,L);
     \]
   - auf \(Z_1,Z_2,Z_3\) existieren H2-only-Wörter mit Endpunkt \(x+\Delta\);
   - auf \(Z_4\) existiert ein H2-only-Wort mit Endpunkt \(x+\Delta-L\);
   - sämtliche neun verwendeten Bridge-Segmente liegen in expliziten H2-Zellen.

3. **Irrationalitätslemma**
   \[
   \Delta/L\notin\mathbb Q.
   \]

## B. Kanonische Transferabbildung

Definiere ausschließlich durch die oben disjunkten Zonen

\[
F(x)=
\begin{cases}
x+\Delta,&x\in Z_1\cup Z_2\cup Z_3,\\
x+\Delta-L,&x\in Z_4.
\end{cases}
\]

Dann

\[
F(x)=x+\Delta\pmod L.
\]

Wichtig: Der zugrunde liegende Graph kann außerhalb dieser kanonischen Auswahl mehrere legale Wörter besitzen. Insbesondere können P3 und das Wrap-Wort auf einem Teilbereich beide legal sein und verschiedene physische Endpunkte besitzen. Für H3-INF wird **keine Eindeutigkeit der Graphrelation** behauptet; benötigt wird nur die Existenz der oben fest gewählten kanonischen Pfade.

## C. Vollständige Randmenge

Auf dem Kreis ist die kanonische Ausnahme-Menge

\[
E=
\{0,\ e-R,\ e,\ L-\Delta\}
\pmod L.
\]

Dabei ist \(0\equiv L\) die Kreisgrenze; im offenen physikalischen Band \(J=(0,L)\) selbst liegt sie nicht.

Es gibt keinen zusätzlichen inneren Umschaltpunkt: \(L-R\) ist nur eine obere Legalitätsgrenze des längeren P3-Wortes, wird aber durch die kanonische Kürzung von P3 auf \((e,L-\Delta)\) nicht als Selector-Grenze benutzt.

## D. Analytischer Existenzschluss

Setze

\[
\mathcal E_\infty
=
\bigcup_{n\ge0}(E-n\Delta)
\pmod L.
\]

Da \(E\) endlich ist, ist \(\mathcal E_\infty\) abzählbar.

Da der Kreis \(\mathbb T_L\) überabzählbar ist, existiert

\[
x_0\in J\setminus\mathcal E_\infty.
\]

Dann gilt für

\[
x_n=x_0+n\Delta\pmod L
\]

für alle \(n\):

\[
x_n\notin E.
\]

Daher liefert der kanonische H3-Cover bei jedem Schritt einen endlichen tatsächlichen Hubpfad

\[
x_n\leadsto x_{n+1}.
\]

Durch Konkatenation liegen alle \(x_n\) in derselben physischen augmentierten Zusammenhangskomponente.

Wegen \(\Delta/L\notin\mathbb Q\) sind die Orbitpunkte paarweise verschieden.

Folgerungskandidat:

\[
\boxed{
\text{Der augmentierte free-\(w\)-Hub-Inzidenzgraph besitzt mindestens eine unendliche physische Zusammenhangskomponente.}
}
\]

## E. Bitte adversarial prüfen

1. Ist die kanonische Zoneneinteilung wirklich disjunkt und vollständig auf \(J\setminus E\)?
2. Sind die Randpunkte in \(E\) vollständig?
3. Reicht die Existenz eines fest gewählten legalen Wortes je Zone aus, obwohl die Graphrelation selbst mehrwertig sein kann?
4. Folgt aus \(x_0\notin\mathcal E_\infty\) korrekt, dass **alle** Vorwärtsorbitpunkte die Wortgrenzen vermeiden?
5. Sind die \(x_n\) tatsächlich physisch verschiedene Punkte und nicht nur verschiedene Liftlabels?
6. Ist die Konkatenation der endlichen Hubpfade ausreichend, um alle \(x_n\) derselben Zusammenhangskomponente zuzuordnen?
7. Gibt es irgendeinen stillen Gebrauch einer stärkeren Aussage als \(\Delta/L\notin\mathbb Q\)?
8. Folgt wirklich nur Existenz **einer** unendlichen Komponente, nicht Universalität?
9. Bestätigt der Schluss ausschließlich ein No-Go gegen finite **Graphkomponenten**-Fasern und keinerlei Cross-Gram-Nichtinjektivität?

## F. Reproduzierbare Dateien

- scripts/certify_sw1_a10_h2_compact_ledger.py
- scripts/certify_sw1_a10_h3_rotation_cover.py
- scripts/certify_sw1_a10_h3_independent_review.py
- scripts/certify_sw1_delta_over_L_irrationality.py
- audits/P11_R32_SW1_A10_FINITE_CROSSGRAM_FIBER_CANDIDATE.md
- audits/P11_R32_SW1_DELTA_OVER_L_IRRATIONALITY_LEMMA.md
