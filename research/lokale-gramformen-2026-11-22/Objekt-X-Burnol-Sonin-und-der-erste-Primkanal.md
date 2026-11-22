# Objekt X · Burnols Leiteroperator und der erste semilokale Sonin-Raum

**Mathematische Vergleichsnotiz, 22. November 2026.** Bezugspunkt ist die Nichtpolform am Commit `ffc81439`. Für ihre Identifikation mit der arithmetischen Weil-Form gilt H0. Die beiden getrennten Arbeitsnotizen zum lokalen Rang und zur Jacobi-Faltung wurden für diesen Vergleich vollständig in ihrer gespeicherten Textfassung gelesen.

## 1. Herkunft und Konvention

Auf der logarithmischen Ortsachse gelte \(\tau_hu(x)=u(x-h)\). Skalarprodukte sind antilinear im ersten Argument. Zur Spektraldarstellung verwenden wir \(F_u(\xi)=\int u(x)e^{-i\xi x}\,dx=\sqrt{2\pi}\,\widehat u(\xi)\). Damit ist die Multiplikation mit \(F_u\) die integrierte Skalierungswirkung in derjenigen Mellin-Konvention, in der die Translation um \(h\) den Faktor \(e^{-ih\xi}\) trägt.

Burnols unramifizierter Leiteroperator hat in der normierten Schalenbasis die Nebendiagonalen \(-\log(p)\,p^{-|i-j|/2}\) und die Diagonale null. Sein gerader reeller Spektralmultiplikator hat den Wert \(-\log(8\pi)-\gamma-\pi/2\) bei null. Die Ableitung der lokalen Phasen in der Projektkonvention reproduziert damit bekannte lokale Wirkungen. Ihre Differenzformel wird auf Fourierbildern der glatten kompakt getragenen Tests verwendet. Die verschwindende Paarung neuer Translationen auf dem alten Fenster betrifft die komprimierte Form. Ein Übergang zwischen den Zielräumen benötigt eine eigene Abbildung. [Burnol, Spektralanalyse, S. 6–7](https://arxiv.org/pdf/math/9811040) · [Burnol, *The Explicit Formula and the conductor operator*, §§ H–I](https://arxiv.org/pdf/math/9902080) · [Projektform (1.1)–(1.3), H0](https://github.com/Waschtl904/objekt-x-programm/blob/ffc81439b73d27929777819b4374a26f6d998181/handoffs/ritz-rest-2026-11-21/belege/DOMAIN_HERLEITUNG.txt)

Für die gespeicherte Jacobi-Faltung gilt unmittelbar eine Ergänzung. Bezeichnet \(\Theta_I\) ihre lokale Hilbert-Schmidt-Fortsetzung, dann ist \(\Theta_I^* A\tau_h\Theta_I\) für jedes beschränkte positive \(A\) kompakt. Das gilt ohne Vertauschbarkeit von \(A\) und \(\tau_h\). Der Normabstand zum verlangten Kreuzblock bleibt mindestens \((\log 2)/\sqrt2\). Für diesen Schluss genügt die lokale Kompaktheit. Die in der Notiz bewiesene Injektivität bezieht sich auf die glatten Tests.

## 2. Was eine unverändert übernommene archimedische Sonin-Spur beim ersten Primkanal kosten würde

Sei \(G_\infty\) die positive Spurform aus der Kompression der Skalierungswirkung auf den archimedischen Sonin-Raum mit Abschneideparameter 1. Dieser Raum besteht aus den geraden \(L^2\)-Funktionen, die zusammen mit ihrer Fouriertransformierten auf \((-1,1)\) verschwinden. Die Projektion ist damit unabhängig von der Projektform definiert. Nach Satz 4.6 von Connes und Consani gilt auf glatten Tests in der logarithmischen Koordinate
\[
 G_\infty(u,w)=Q_\infty(u,w)+E_\epsilon(u,w).
\]
Hier ist \(Q_\infty\) der archimedische Projektterm mit dem Vorzeichen ihres \(W_\infty=-W_{\mathbb R}\). Seine Fourier-Normierung steht in (153)–(155). Der Zusatz \(E_\epsilon\) hat den Faltungskern \(\epsilon(e^{y-x})\). Diese Schreibweise ergibt sich durch Einsetzen der Korrelation \(u^**w\) in (84) und \(d^*\rho=d\log\rho\). Für die folgende Kompaktheit genügt lokale Integrierbarkeit des Fehlerkerns. Auf jedem beschränkten Ortsfenster kann man ihn auf der Differenzmenge in \(L^1\) durch glatte Kerne approximieren. Youngs Ungleichung liefert Konvergenz in Operatornorm. Die glatten komprimierten Kerne sind Hilbert-Schmidt. [Connes–Consani, *Weil positivity and Trace formula*, Satz 4.6 und Anhänge A–B](https://alainconnes.org/wp-content/uploads/Selecta.pdf)

**Folgerung für Objekt X.** Setze \(h=\log2\), \(a=h/\sqrt2\), \(|I|=h/4\) und \(H_I=\overline{V_I}^{L^2(I)}\) für die glatten Tests mit beiden verschwindenden Momenten in \(I\). Beide Intervalle \(I,I+h\) sollen im Testfenster liegen. Die Einbettung
\(\mathcal J(u,w)=u+\tau_hw\) identifiziert \(H_I\oplus H_I\) isometrisch mit dem lokalen Doppelraum. Auf glatten Tests hat die Differenz \(q_t^{\rm np}-G_\infty\) dort die beschränkte Fortsetzung
\[
 \mathcal J^*(q_t^{\rm np}-G_\infty)\mathcal J
  =
  \begin{pmatrix}0&-a\,\mathrm{Id}\\-a\,\mathrm{Id}&0\end{pmatrix}+C,
  \qquad C=C^*\ \text{kompakt}. \tag{1}
\]
Diese Kurzschreibweise meint die Differenz der zurückgezogenen Formen. Eine \(L^2\)-Beschränktheit der beiden einzelnen Diagonalformen wird nicht benötigt.

**Beweis.** Innerhalb jedes kurzen Intervalls wirkt keine Primverschiebung. Zwischen den Intervallen trifft genau eine Orientierung des ersten Zweierkanals. Die beiden Kreuzblöcke des Primanteils sind deshalb \(-a\,\mathrm{Id}\). Die gesamte archimedische Differenz ist die Kompression von \(-E_\epsilon\) und damit kompakt. Wähle eine Orthonormalfolge \(u_n\) in \(V_I\), etwa durch Gram-Schmidt aus unabhängigen glatten Zwei-Moment-Tests. Für die normierten Tests \(f_n^\pm=(u_n\pm\tau_hu_n)/\sqrt2\) folgt
\[
 (q_t^{\rm np}-G_\infty)[f_n^+]\longrightarrow -a,\qquad
 (q_t^{\rm np}-G_\infty)[f_n^-]\longrightarrow +a.
\]
Beide Folgen konvergieren schwach gegen null, weshalb die kompakten Beiträge verschwinden. ∎

Damit scheidet das Modell \(q_t^{\rm np}[f]=G_\infty[f]+\|R f\|^2\) für **alle Tests im erweiterten Fenster** aus, selbst bei beliebigem Zielraum für \(R\). Auch ein zusätzlicher kompakter selbstadjungierter Fehler auf dem lokalen Doppelraum ändert den Widerspruch nicht. Betroffen ist die unveränderte Auswertung der archimedischen Spur auf dem *gesamten neuen* Fenster. Eine Konstruktion darf alte Testwerte erhalten und neue Vektoren mit schon vorhandenen Richtungen koppeln. Die beiden Grenzwerte sind Werte der Differenz, keine negativen Diagonalwerte der Ziel-Weil-Form.

## 3. Eine aus lokalen Faktoren bestimmte Änderung des Zielraums

In der Hardy-Raum-Darstellung von Connes–Consani sei \(H_-\) der Randwertraum der linken Halbebene \(\Re s<1/2\) und \(H_+=H_-^\perp\) derjenige der rechten. Für den Multiplikator \(U\) ist \(\mathscr S(U)=\{f\in H_+:Uf\in H_-\}\) der Sonin-Raum in dieser Darstellung. Schreibe \(\mathscr S_\infty=\mathscr S(U_\infty)\) und \(\mathscr S_2=\mathscr S(U_\infty U_2)\). Für den Übergang am Ort 2 setze auf der kritischen Linie
\[
 b(s)=1-2^{-s},\quad r=2^{-1/2},\quad U_2=\overline b/b.
\]
Dann gilt \(\mathscr S_2=b\,\mathscr S_\infty\). Denn \(b,1/b\) sind beschränkte analytische Multiplikatoren rechts, und ihre konjugierten Randfunktionen haben dieselbe Eigenschaft links. Aus \(f\in H_+\), \(U_\infty f\in H_-\) folgt \(bf\in H_+\), \(U_\infty U_2bf=\bar b U_\infty f\in H_-\). Division liefert die Umkehrung. Dieser Übergang stimmt mit dem Stellenwechsel der Literatur überein. Die spätere geometrische Konstruktion gibt dieselbe Multiplikation in den Mellin-Koordinaten und einen topologischen Isomorphismus der Sonin-Räume. [Connes–Consani, *Quasi-inner functions and local factors*, §5](https://alainconnes.org/wp-content/uploads/quasi-inner.pdf) · [Connes–Consani–Moscovici, *Zeta zeros and prolate wave operators*, Satz 2 und (4.24)](https://alainconnes.org/wp-content/uploads/Zeta-zeros-and-prolateproofs-final-2024.pdf)

Sei \(\iota:\mathscr S_\infty\hookrightarrow L^2(d\xi)\) die isometrische Inklusion und \(J=M_b\iota\). Aus dem oben bestimmten Bild ergibt sich der **orthogonale** Projektor auf den Zielraum,
\[
 A=J^*J,\quad (1-r)^2 I\le A\le(1+r)^2 I,\qquad
 P_2=J A^{-1}J^*,\qquad V=JA^{-1/2}. \tag{2}
\]
Der Normausgleich in \(V\) ist durch das ursprüngliche \(L^2\)-Skalarprodukt bestimmt. In \(A\) stehen beide Translationsrichtungen, denn \(|b|^2=1+r^2-2r\cos(h\xi)\). Für den isolierten Ortsblock hat \(\langle b\widehat u,b\widehat{\tau_h w}\rangle=-r\langle u,w\rangle\) auf den Tests in \(I\). Die Projektform verlangt \(-hr\langle u,w\rangle\) aus der Primstelle. Das einfache Multiplizieren mit \(b\) und das Bilden der Sonin-Spur aus \(P_2\) sind verschiedene Rechnungen. Den Faktor \(h\) muss die normierte Spur im vollständigen Vergleich liefern.

Eine konkret definierte lineare Testabbildung in den Raum der Hilbert-Schmidt-Operatoren von \(\mathscr S_\infty\) nach \(L^2(d\xi)\) ist
\[
 R_2(u)=M_{F_u}V,\qquad G_2(u,w)=\operatorname{Tr}(R_2(u)^*R_2(w)). \tag{3}
\]
Ihre Gramform ist positiv. Für glatte kompakt getragene Tests ist \(M_{F_u}\iota\) Hilbert-Schmidt, denn das Quadrat der Hilbert-Schmidt-Norm ist die endliche archimedische Sonin-Spur auf \(u^**u\). Nun gilt \(R_2(u)=M_b(M_{F_u}\iota)A^{-1/2}\), was die Endlichkeit von (3) begründet. Alle Objekte in (2)–(3) sind vor dem Vergleich mit \(q_t^{\rm np}\) festgelegt.

**Offene Gleichung.** Auf den Tests \(u,w\in V_I\) ist zu entscheiden, ob die Spur
\[
 \operatorname{Tr}_{\mathscr S_\infty}\!\left(
 A^{-1/2}J^* M_{\overline{F_u} e^{-ih\xi} F_w}J A^{-1/2}
 \right)
 \stackrel{?}{=}
 -a\langle u,w\rangle-
 \int_{I^2}\overline{u(x)}
 \frac{e^{-(h+y-x)/2}}{1-e^{-2(h+y-x)}} w(y)\,dx\,dy. \tag{4}
\]
Die linke Seite ist das Produkt zweier Hilbert-Schmidt-Abbildungen unter der Spur. Die rechte folgt aus (1.1) der Projektquelle. Für einen ersten analytischen Test auf den nichtkompakten Anteil muss die Differenz von linker Seite und \(-a\langle u,w\rangle\) einen kompakten lokalen Kreuzoperator ergeben. Für (4) ist auch dessen genauer Gamma-Kern festgelegt. Offene Punkte sind diese Spurauswertung, die übrigen Paarungen und die Verträglichkeit der positiven Testabbildungen bei weiteren Stellenwechseln. Satz (1) betrifft die alte archimedische Spur als festen Summanden. Er entscheidet (4) für den geänderten Projektor nicht.

