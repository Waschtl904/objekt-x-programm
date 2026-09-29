# Transport der kritischen Spektralräume

28. September 2026 · lokaler Forschungsblock · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

## Ergebnis

**Das vorgeschlagene Critical Spectral Transport Lemma folgt aus den vorhandenen Sätzen.** Die Projektion der physisch fortgesetzten alten kritischen Quellen in den neuen kritischen Raum ist injektiv. Eine numerische Berechnung einzelner Eigenvektoren ist dafür nicht erforderlich.

Zusätzlich wurden stärkere vollständige Komplement-Gaps mit neuen Ganzzahlintervall-Zertifikaten bewiesen. Sie verbessern die quantitativen Transportgrenzen:

| Übergang | Parität | Alte/neue kritische Dimension | Obergrenze für ‖(I−Pᵦ)JPₐ‖ | Untergrenze für ‖PᵦJx‖/‖x‖ |
| --- | --- | ---: | ---: | ---: |
| A₈ → A₉ | gerade | 5 → 6 | **0.019453** | **0.999810** |
| A₈ → A₉ | ungerade | 5 → 6 | **0.036057** | **0.999349** |
| A₉ → A₁₁ | gerade | 6 → 8 | **0.024468** | **0.999700** |
| A₉ → A₁₁ | ungerade | 6 → 8 | **0.045712** | **0.998954** |

Alle Normen in dieser Tabelle sind die **b-Normen mit b = q + 17‖·‖²**. Die Zahlen sind sichere, nach außen gerundete Grenzen. Es handelt sich um analytisch eingeschlossene Operatornormen; numerische Koordinaten der echten Projektoren wurden nicht erzeugt.

Die kanonischen Ergänzungsräume besitzen pro Parität Dimension **1** beziehungsweise **2**. Außerdem folgt: **Jeder von null verschiedene Ergänzungsvektor hat einen nichtverschwindenden L²-Anteil außerhalb des alten Intervalls.** Dessen Größe, räumliches Profil und Zuordnung zu einzelnen Prime-Power-Kanälen sind noch nicht numerisch bestimmt.

Die neue Aussage korrigiert eine zu enge Grenze im vorigen Bericht: Für die Injektivität und die Nichtabnahme der Ränge genügt bereits die Formnaturality. Der numerische Projektorvergleich wird für feinere Geometrie benötigt.

## 1. Voraussetzungen und Normen

Wir arbeiten im bereits positiven Bereich bis A₁₁. Die vollständigen Formräume \(\mathcal F_A\) tragen

\[
b_A(u,v)=q_A(u,v)+17\langle u,v\rangle_{L^2}.
\]

Die durch q im b-Hilbertraum dargestellten Operatoren \(\mathcal A_A\) sind positive Kontraktionen. Physische Nullfortsetzung J=J₍ₐ,ᵦ₎ erfüllt auf den vollständigen Formräumen

\[
q_B(Ju,Jv)=q_A(u,v),\qquad
\langle Ju,Jv\rangle_{L^2}=\langle u,v\rangle_{L^2},\qquad
b_B(Ju,Jv)=b_A(u,v).
\]

Dies steht im allgemeinen Wandlemma §4. Seine Gültigkeit über die q=9-Wand und die gemeinsame Wahl 17 bis A₁₁ sind dort und in `wall/Q9.md` festgehalten. Die Terminalpositivität und die vollständigen Spektralräume sind Eingaben dieses Transportblocks.

Bei \(\tau=10^{-4}\) seien

\[
P_A=\mathbf1_{(0,\tau)}(\mathcal A_A),\quad K_A=\operatorname{ran}P_A,
\quad
\alpha_A=\max\sigma(\mathcal A_A|_{K_A}),\quad
\beta_B=\inf\sigma(\mathcal A_B|_{K_B^{\perp_b}}).
\]

Die kritischen Räume sind endlichdimensional; für die untersuchten Terminals liegt der Schnitt in einer Lücke. Allgemein genügt für das folgende Lemma bereits \(0\le\alpha_A<\beta_B\). Die Spektralprojektoren sind sowohl b-orthogonal als auch q-orthogonal; als physische Quellenräume entsprechen sie dem Q-Schnitt \(17/9999\).

## 2. Critical Spectral Transport Lemma

**Satz.** Unter diesen Voraussetzungen gilt

\[
\boxed{\|(I-P_B)JP_A\|_{b_A\to b_B}
\le\sqrt{\alpha_A/\beta_B}<1.}
\]

Für \(T=P_BJ|_{K_A}:K_A\to K_B\) folgt

\[
\boxed{\sqrt{1-\alpha_A/\beta_B}\,\|x\|_{b_A}
\le\|Tx\|_{b_B}\le\|x\|_{b_A}.}
\]

Insbesondere ist T injektiv und \(\dim K_B\ge\dim K_A\).

**Beweis.** Für x∈Kₐ setze z=(I−Pᵦ)Jx. Spektrale Orthogonalität und Positivität ergeben

\[
\beta_B\|z\|_{b_B}^2\le q_B[z]
\le q_B[P_BJx]+q_B[z]
=q_B[Jx]=q_A[x]\le\alpha_A\|x\|_{b_A}^2.
\]

Pythagoras und die b-Isometrie von J liefern

\[
\|Tx\|_{b_B}^2=\|x\|_{b_A}^2-\|z\|_{b_B}^2
\ge(1-\alpha_A/\beta_B)\|x\|_{b_A}^2.
\]

Beide Aussagen sind damit bewiesen. Der Operatornormbound auf dem ganzen alten Formraum folgt zusätzlich aus ‖Pₐ‖≤1.

**Nichtabnahme.** Auf dem bereits positiven gemeinsamen Horizont folgt die Nichtabnahme der kritischen Spektralzahl auch unmittelbar aus Minimax: J erhält Norm und Rayleighquotienten jedes alten Testraums. Deshalb sind die geordneten Eigenwerte \(\mu_j(Q_B)\le\mu_j(Q_A)\). Bei einer gemeinsamen b-Norm gilt dasselbe für die b-Spektralwerte. Eine Gleichheit des Schnitts mit einem neuen Eigenwert stört die Injektivitätsaussage nicht, solange αₐ<τ≤βᵦ.

Die Monotonie setzt vergleichbare Normen und den hier angenommenen positiven Bereich voraus. Eine unveränderte globale Wahl 17 und neue Terminalpositivität werden außerhalb des bereits geprüften Horizonts nicht aus diesem Satz abgeleitet.

## 3. Woher die α-Grenzen kommen

Die alten physischen Testräume werden nicht mit den echten kritischen Räumen identifiziert. Die bereits bewiesene Rangzahl r und das Minimax-Prinzip rechtfertigen den Schluss

\[
\mu_r(Q_A)\le U_r
\quad\Longrightarrow\quad
\alpha_A\le\frac{U_r}{U_r+17}.
\]

Hier ist Uᵣ die zertifizierte obere Rayleighgrenze des r-dimensionalen echten physischen Testraums einschließlich seiner Mellin-Massenmatrix. Somit liefern die vorhandenen Daten tatsächlich Obergrenzen für den höchsten echten kritischen Spektralwert:

| Alter Terminal | Parität | Sichere Obergrenze für αₐ |
| --- | --- | ---: |
| A₈ | gerade | 8.369359·10⁻⁸ |
| A₈ | ungerade | 5.015758·10⁻⁶ |
| A₉ | gerade | 1.321999·10⁻⁷ |
| A₉ | ungerade | 8.662505·10⁻⁶ |

Die exakten rationalen Werte werden im Prüfer übernommen. Schon βᵦ≥10⁻⁴ beweist die Injektivität; die stärkeren nachfolgenden β-Grenzen verbessern ihre Konditionierung.

## 4. Neue vollständige Komplement-Gaps

Die neue Rechnung umgeht den konservativen globalen Spurbound \(H^{up}\preceq\gamma F\). Stattdessen wird die gesamte gespeicherte hohe Kopplungsmatrix in der parameterabhängigen Vergleichsform belassen.

In den Mellin-korrigierten Referenzkoordinaten gelten weiterhin

\[
G=M^*M\preceq\rho I,\quad \rho<1003/1000,\quad
H\succeq\delta I,\quad BB^*\preceq H^{up},\quad
F=L_0-e_LI-\delta^{-1}H^{up}.
\]

Für \(t=(1003/1000)\mu<\delta\) folgt aus \(\widehat Q-\mu G\succeq\widehat Q-tI\) und vollständiger hoher Schur-Elimination

\[
\mathscr C(t)
=F-tI-\frac{t}{\delta(\delta-t)}H^{up}.
\]

Diese untere Vergleichsmatrix bezahlt den **ganzen unendlichen hohen Raum**. Verwendet werden δ=2/3 bei A₉ und δ=1 bei A₁₁. Die Massenmatrix wird nicht durch eine unzulässige orthonormale Annahme ersetzt.

Für r=6 beziehungsweise r=8 und die bereits festgehaltenen rationalen Testspalten V beweist der neue Ganzzahlprüfer

\[
\mathscr C(t)+VV^*>0,\qquad -V^*\mathscr C(t)V>0.
\]

Damit hat die Vergleichsmatrix genau r negative Richtungen und keinen Nullraum. Die vollständige physische Form hat bei μ höchstens r nichtpositive Richtungen. Aus dem früheren Rangzertifikat sind bereits r echte Eigenwerte unter 17/9999<μ bekannt. Daher liegt der gesamte physische Spektralrest strikt oberhalb des hier geprüften μ.

| Neuer Terminal | Parität | Geprüfter physischer Schnitt μ | Untergrenze βᵦ=μ/(μ+17), abgerundet |
| --- | --- | ---: | ---: |
| A₉ | gerade | 0.003761 | 2.21186·10⁻⁴ |
| A₉ | ungerade | 0.065841 | 3.85805·10⁻³ |
| A₁₁ | gerade | 0.003755 | 2.20833·10⁻⁴ |
| A₁₁ | ungerade | 0.070769 | 4.14562·10⁻³ |

Die vier Dezimalwerte für μ sind exakte rationale Prüfparameter. Es werden keine optimierten Eigenwerte behauptet. Die Obergrenzen für die Transportnormen in der Ergebnistabelle folgen durch exakte rationale Quotienten und nach außen eingeschlossene Quadratwurzeln.

**Rechenmethode.** Gleitkomma-Cholesky schlägt nur rationale Faktoren R,T vor. Der unabhängige Prüfer rekonstruiert \(\mathscr C(t)+VV^*\) aus den ursprünglichen Modell-/F-Intervallen. Mit 200 Dezimalstellen in Ganzzahlintervallen prüft er

\[
\epsilon\ge\|\mathscr C(t)+VV^*-R^*R\|,\quad
\eta\ge\|I-RT\|,\quad \nu=\|T\|_F^2,
\quad \frac{(1-\eta)^2}{\nu}-\epsilon>0.
\]

Zusätzlich prüft er die sechs beziehungsweise acht positiven Pivots der negativen Kompression und den Einschluss der Formel für F. Keine numerischen Eigenvektoren und kein endlicher Ersatz für die hohe Antwort gehen in den neuen Nachweis ein.

## 5. Kanonischer transportierter Teil und Ergänzungsraum

Setze \(\widetilde K_{A\to B}=TK_A\). Alle folgenden Adjungierten beziehen sich auf b. Insbesondere bedeutet \(J^\dagger\) den b-Adjungierten; er ist nicht allgemein mit der physischen Einschränkung einer Quelle gleichzusetzen.

Mit \(D=T^\dagger T\) gilt

\[
(1-\varepsilon^2)I\preceq D\preceq I,
\qquad\varepsilon^2=\overline\alpha_A/\underline\beta_B<1.
\]

Der b-orthogonale Projektor auf das transportierte Bild und der auf die Ergänzung sind exakt

\[
\Pi_{\widetilde K}=TD^{-1}T^\dagger,\qquad
\boxed{\Pi_E=P_B-TD^{-1}T^\dagger.}
\]

Damit

\[
E_{A,B}=K_B\ominus_b\widetilde K_{A\to B}
=\{e\in K_B:\ b_B(e,Jx)=0\ \forall x\in K_A\}.
\]

Diese Definition benötigt keine Wahl einzelner Eigenvektoren. Ihre Dimension beträgt rᵦ−rₐ: **1 je Parität für A₈→A₉**, **2 je Parität für A₉→A₁₁**, insgesamt 2 beziehungsweise 4.

Die Dimensionendifferenz lokalisiert keinen Rangwechsel an einer Prime-Power-Wand. Die feste Spektralschwelle kann auch innerhalb einer Kammer unterschritten werden.

Die Polarform \(U=TD^{-1/2}\) liefert zudem eine kanonische **b-isometrische** Einbettung von Kₐ in Kᵦ. Daraus wird keine q-Isometrie behauptet.

## 6. Eine bereits beweisbare räumliche Aussage

**Satz.** Unter denselben Voraussetzungen und \(\alpha_B<\beta_A\) gilt

\[
\boxed{E_{A,B}\cap J\mathcal F_A=\{0\}.}
\]

**Beweis.** Sei e=Jy∈E. Wegen der Charakterisierung von E gilt y⊥ᵦKₐ. Daher

\[
q_B[e]=q_A[y]\ge\beta_A\|y\|_{b_A}^2
=\beta_A\|e\|_{b_B}^2.
\]

Andererseits liegt e in Kᵦ, also \(q_B[e]\le\alpha_B\|e\|_{b_B}^2\). Wegen αᵦ<βₐ folgt e=0.

Für unsere feste Schwelle ist αᵦ<τ≤βₐ in beiden Übergängen erfüllt. Die bereits bewiesene vollständige Formraumcharakterisierung sagt außerdem: Jede neue Quelle mit Träger innerhalb [-A,A] gehört zum alten Formraum. Deshalb ist die Einschränkung

\[
R_{\rm außen}:E_{A,B}\longrightarrow
L^2([-B,-A)\cup(A,B])
\]

injektiv. In jeder der endlichen Ergänzungen existiert folglich ein positiver minimaler äußerer Massenanteil bei L²-Normierung. **Ein Zahlenwert für diesen Anteil wurde hier nicht berechnet.** Die Aussage beweist weder überwiegende Randlokalisierung noch Konzentration an einem bestimmten Shift.

Für eine spätere numerische Charakterisierung bietet sich der L²-orthogonale Projektor \(P_E^{(2)}\) auf E an. Er ist von \(\Pi_E\), dem b-Projektor, zu unterscheiden. Basisfreie Ortsdaten sind beispielsweise

\[
\operatorname{tr}\bigl(P_E^{(2)}\mathbf1_\Omega P_E^{(2)}|_E\bigr)
\]

und die Eigenwertgrenzen der äußeren Massen-Grammatrix. Der Beitrag eines Prime-Power-Kanals ist die entsprechende **vorzeichenbehaftete** Korrelationsform

\[
-2w_q\operatorname{Re}\langle e,T_{\log q}e\rangle_{L^2}.
\]

Solche Kanalbeiträge dürfen nicht als nichtnegative Wahrscheinlichkeitsanteile gelesen werden. Ihre Berechnung benötigt eine genauere Einschließung von \(\Pi_E\) beziehungsweise seiner Quellenbilder, die dieser Block nicht ausgibt.

## 7. Konsequenz für die nächste Schur-Zerlegung

Die Zerlegung

\[
\mathcal F_B=\widetilde K_{A\to B}\oplus_b E_{A,B}\oplus_b K_B^{\perp_b}
\]

hat für die q-Form die Struktur

\[
\begin{pmatrix}
S&C&0\\
C^*&D_E&0\\
0&0&D_\perp
\end{pmatrix},\qquad D_\perp\succeq\beta_BI.
\]

Die Nullen folgen aus der echten Spektralzerlegung Kᵦ⊕Kᵦ⊥. Zwischen transportiertem Teil und E besteht dagegen im Allgemeinen eine q-Kopplung: Beide Teilräume sind b-orthogonal, aber nicht notwendig q-orthogonal. Ein späterer κ-Test dieser Zerlegung betrifft somit nur die Kopplung des rₐ-dimensionalen alten Bildes an die **1 beziehungsweise 2 zusätzlichen Dimensionen** je Parität. Der robuste Spektralrest koppelt in dieser exakten Zerlegung nicht an.

Der tatsächliche κ-Test wird hier noch nicht ausgeführt. Auch diese endliche Blockdarstellung beweist keine neue Terminalpositivität, denn Kᵦ und seine Positivität stammen aus dem bereits zertifizierten neuen Terminal.

## 8. Was zur Erneuerbarkeit noch fehlt

Mit \(R=(I-P_B)J|_{K_A}\) folgt exakt

\[
T^\dagger\mathcal A_BT
=\mathcal A_A|_{K_A}-R^\dagger\mathcal A_BR.
\]

Die Projektion verliert also Formenergie. Eine kleine absolute b-Norm von R sichert keine entsprechend kleine **relative** Energieänderung auf den allerschwächsten alten Richtungen. Für einen vorwärts gerichteten Renewal-Satz bleiben deshalb quantitative Energie- und Kopplungskontrollen nötig, die neue Positivität nicht bereits voraussetzen.

Auch erfüllen die projizierten kritischen Transporte nicht automatisch ein Cocycle. Für A<B<C gilt

\[
T_{B,C}T_{A,B}-T_{A,C}
=-P_CJ_{B,C}(I-P_B)J_{A,B}|_{K_A}.
\]

Der Fehler ist durch die alte Leckage begrenzt, aber nicht notwendig null. Die physische Nullfortsetzung selbst erfüllt weiterhin ihr exaktes Cocycle.

Somit stehen jetzt ein analytischer Injektivitätssatz, quantitative stabile Einbettungen, kanonische kleine Ergänzungen und eine qualitative Ortsaussage bereit. Offen bleiben die numerische Massen-/Kanalanalyse dieser Ergänzungen sowie der neue relative κ-Nachweis. Ein allgemeiner Fortsetzungs- oder RH-Satz wird daraus nicht abgeleitet.

## Prüfstand und Dateien

- Alle vier neuen parameterabhängigen Komplement-Gap-Zertifikate wurden vollständig mit Ganzzahlintervallen reproduziert.
- Die vier Normobergrenzen und die vier minimalen Singularwert-Untergrenzen wurden als rationale Quadratwurzelgrenzen geprüft.
- Das frühere Rangpaket und sein eingebettetes A₁₁-Paket wurden anhand ihrer vollständigen Manifeste geprüft. Die verwendeten Repository-Blobs wurden gegen Commit `d16ba43ebb20f2c61f43379fc65d7a9b9dba76de` abgeglichen.
- Die vorhandenen Massennormgrenzen stammen aus den gebundenen 512-/768-Bit-Rechnungen. Die ursprünglichen Terminalintegrale und Rangläufe wurden hier nicht neu erzeugt.
- `verification.json` enthält die exakten Grenzen, `integer_replay.log` das vollständige neue Prüfprotokoll. `REPRODUKTION.md` beschreibt den Replay. `rank_reference.zip` enthält die unveränderten Eingangszertifikate.

**Main, Registry, historische Quellen und vorhandene globale Verifikationsstände wurden nicht verändert.** Das Ergebnis ist ein lokaler mathematischer Forschungsblock mit offenem externem Review.
