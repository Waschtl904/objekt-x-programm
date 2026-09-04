# CURRENT FRONT — Objekt X / P11 Strong Terminal

> **Operative R43 update — 4. September 2026:** PR #53 is merged at `main@b4e0293fbace457838e3fe07abbafcaf4acca19b`; active branch is `research/r43-structured-cond` (PR #54). The strict post-merge referee reconciliation preserves the kernel-witness theorem but narrows one route label: `R43-COND-UNIFORM-LOCAL-LOEWNER-TELESCOPE-ROUTE ×[M]`; `R43-COND-PARTITION-SELECTIVE-PSD ?[O]` and `R43-COND-EPSILON-RELAXED-TELESCOPE ?[O]` remain open. See `audits/P11_R43_POSTMERGE_REFEREE_RECONCILIATION_2026-09-04.md`, `00-uebersicht/P11_R43_STRUCTURED_COND_FRONT_2026-09-04.md`, and `00-uebersicht/P11_R43_COND_LEDGER_2026-09-04.md`. Strong Terminal/C6, R43, Object X, RH remain OPEN.

> **Historical operative layer below is retained verbatim; newer R43 pointers above take precedence where status wording differs.**

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 3. September 2026  
> **Aktuelle Research-Basis:** `main@2102b538c220cd809ad876c425df4f30304eb997` enthält die konsolidierte R37–R43-Linie. Aktive Härtung: Branch `research/r43-gcac-hardening`; aktueller **mathematischer R43-Head** `c4d0f03089659533fb06bf9a2822060c64e2d9e1` (kanonischer R43-Mathematikblob `983b42949d6a4a1806c0b333727cb49000b99972`). Der frühere Perplexity-Destruktivreview bleibt ausschließlich auf seinem exakten geprüften Head `c7c6f04cd601ea868cb536327504f6c90b3f0807` als **external destructive GREEN (cross-model nonblind)** gebucht; keine formale unabhängige GREEN-Promotion. **GC-AC** ist auf Kandidatenebene geschlossen. Der verbleibende Strong-Terminal-Block ist **B-FLAGTIGHT**, exakt `lim_m limsup_U ||P_{H_S^[m]}h_U||=0`; die Jet-Zahl-/Flaggenenergie ist nur ein stärkeres hinreichendes Werkzeug, nicht das Gate selbst. Der Higher-Jet-Riesz-Unterrand bleibt numerisch stark kontraindiziert, ohne theorem-level No-Go. Der partielle Kozykel `T_{U→V}=W_VW_U^*` ist algebraisch exakt, aber sein Off-Flag-Block enthält einen **statischen Range/Flag-Winkel**: bereits `T_{U→U}=P_{Ran W_U}`, daher ist `P_mT_{U→U}(I-P_m)` im Allgemeinen nicht null. Die saubere inkrementelle Front ist nun der feste Quellraum-Effekt `Q_{m,U}=W_U^*P_mW_U`, `q_m(U)=<ε_R,Q_{m,U}ε_R>`, mit echter Terminaldynamik `Q_{m,V}-Q_{m,U}` und exakter Horizon-Gauge-Formel über `C_X^{U→V}=G_{X,V}^{1/2}G_{X,U}^{-1/2}`. **B-FLAGDYN** bezeichnet die offene quantitative Kontrolle der positiven Terminalvariation von `q_m(U)`. Nach B-FLAGTIGHT bleibt **B-SIGN/B-ORIENT**; unter B-TIGHT gilt der scharfe Test `Strong Terminal ⇔ liminf_{T,U→∞}L_{R,S}^{T,U}>-1`. Kein Terminalgenerator, keine Darboux-/Clark-Identifikation und keine Object-X-/RH-Promotion wird importiert. R43 bleibt OPEN; kein Freeze, kein neues `✓[M]`.  
> **Aktiver mathematischer Stand:** **B / Strong Terminal.** R38–R42 sind jeweils **FROZEN — independently verified AI-GREEN**, ohne kanonische `✓[M]`-Promotion. Für jedes feste \(0<R<S\) konvergiert der echte Future-Transport bereits stark auf \(H_R^0=\ker\beta_R^{(0)}\). Strong Terminal / C6 ist exakt auf die eine feste Normalbahn \(W_{R,S}^{[U]}\varepsilon_R\), äquivalent auf den einen Cross-Kernel-Koeffizienten \(\operatorname{Re}\langle\varepsilon_R,K_{R,S}^{T,U}\varepsilon_R\rangle\to1\), reduziert. **R43 ist offen / exploratory** und untersucht diesen letzten Gate. R37/G4c bleibt separat offen und wird durch R38–R43 nicht rückwirkend geschlossen.  
> **Detailregistry:** [ACTIVE_THEOREM_REGISTRY](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md) · **Roadmap:** [FORSCHUNGS_ROADMAP_2026-09-03](00-uebersicht/FORSCHUNGS_ROADMAP_2026-09-03.md)

Diese Datei ist die **operative Navigationsschicht** des Repositories. Sie ist kein mathematischer Beweis und erzeugt keine Statuspromotion. Ihre Aufgabe ist, den gegenwärtigen Forschungsangriff, seine erlaubten Inputs und die ausdrücklich nicht benötigten Nebenfronten sichtbar zu halten.

---

## 1. Aktuelles Ziel

Die aktive Front ist **nicht** „Objekt X vollständig konstruieren“ und **nicht**
„RH beweisen“.

Operativ sind jetzt zwei Achsen getrennt:

1. **A / M1-ND-SALVAGE:** historisch/strategisch geparkt; PR #49 bleibt eingefrorener, unpromotierter Kandidat.
2. **B / Strong Terminal:** aktive Forschungsachse. R38–R42 sind frozen; **R43** ist der einzige aktuelle Arbeitsblock. Sein Hauptobservable ist
   \[
   L_{R,S}^{T,U}
   :=
   \operatorname{Re}
   \langle e_{R,0},K_{R,S}^{T,U}e_{R,0}\rangle,
   \]
   mit \(e_{R,0}=\varepsilon_R\). Strong Terminal gilt genau dann, wenn
   \[
   L_{R,S}^{T,U}\to1
   \qquad(T,U\to\infty).
   \]

Der bisherige universelle Zielknoten

\[
\ker\mathscr N_R=\{0\}
\qquad
\text{für alle SW1-Parameter}
\]

ist durch M1-ND-IMG4-SMALLR negativ entschieden.

Promotet ist der explizite Witness

\[
\boxed{
\varepsilon_0=\Delta/4,\qquad
R_0=T/100000,\qquad
\sigma_0=R_0/2,
}
\]

mit

\[
\boxed{
\ker\mathscr N_{R_0}\ne\{0\}.
}
\]

Status:

\[
\boxed{
\mathrm{M1\!-\!ND\!-\!SMALLR}:\checkmark[M]_{\rm neg}.
}
\]

Damit ist **universelle SW1-Cross-Gram-Nichtentartung in der aktuellen
finite-level Geometrie ausgeschlossen**.

Der neue eng gefasste Frontknoten lautet:

\[
\boxed{
\mathrm{M1\!-\!ND\!-\!SALVAGE}
}
\]

mit zwei möglichen Richtungen:

1. **Parameterklassifikation:** Bestimme den maximalen Restbereich, auf dem
   \(\ker\mathscr N_R=\{0\}\) noch möglich oder beweisbar ist.
2. **Architekturreparatur:** Ändere die finite-level Kopplung so, dass der
   durch FREE-Komponentensättigung erzeugte Small-\(R\)-Blindraum nicht mehr
   existiert.

Die allgemeine Aussage

\[
\forall\,0<\varepsilon<\Delta/2\ \exists R_\varepsilon^*>0:
\quad
0<R<R_\varepsilon^*,\ 0<\sigma<R
\Longrightarrow
\ker\mathscr N_R\ne0
\]

bleibt vorerst **Kandidat**, nicht mitpromotet.

**Scope-Firewall:** Die Promotion betrifft den tatsächlichen zulässigen Raum

\[
\mathscr B_K\oplus\mathscr B_W
\]

bzw. die dazu äquivalente IMG0/IMG2-Darstellung, nicht den größeren formalen
Slot-Ambientraum. Keine separate Promotion von \(\ker\Gamma_I\ne0\), kein
Objekt-X-Abschluss und keine RH-Folgerung.

---

## 2. Was bereits kostenlos zur Verfügung steht

### 2.1 Äußerer Hub — formal bewiesen

P12 liefert bereits:

\[
\boxed{
0<R<T,\qquad \sigma\le R
\Longrightarrow
\ker L_{R,S,T_0}^{\{a,b,2a\}}=\{0\}.
}
\]

Status:
\[
\boxed{\checkmark[M]}
\]

Quelle:
`papers/P12_Adelic_Hub_Injectivity_Program.tex`, Corollary `cor:p12-consolidated`.

SW1 liegt vollständig in diesem Bereich. Daher muss die äußere Hub-Injektivität für den SW1-Angriff **nicht neu bewiesen** werden.

### 2.2 Aktuelle Tail-/FG-/Kernel-Kandidaten

HT-A1, HT-A2, HT-A3 und HT-A4a sind AI-GREEN geprüfte Kandidaten, aber nicht formal promotet.

FG-1, FG-TR1, die \(\widehat\Phi_R\)-Normalform und CG-FG1 sind ebenfalls AI-GREEN Kandidaten-/Kompositionsresultate ohne formale Promotion.

SW1-KNF (`audits/P11_R32_SW1_KNF_CANDIDATE.md`, PR #15) ist ein AI-GREEN Kandidat, der auf SW1 eine vollständige sektorale Kernel-Normalform liefert und dort die globale FG-TR1-Blackbox ersetzt.

SW1-BL7 (`audits/P11_R32_SW1_BL7_CANDIDATE.md`, PR #16) ist ein AI-GREEN Kandidat: für \(s\in(R,\varepsilon)\) gilt \(2d+s\in(a+R,b-R)\subset\mathcal Z_{R,\mathrm{SW1}}^{\rm phys}\), für jedes \(s\), als siebter direkter Blindwert neben den sechs promoteten.

SW1-2TP (`audits/P11_R32_SW1_2TP_CANDIDATE.md`, PR #17) ist AI-GREEN + `independent GREEN (certificate)`: die beiden \(T\pm s\)-Rows wurden direkt aus den elf Wörtern von \(A\) hergeleitet; \(M_T\) ist uniform positiv invertierbar; das reproduzierbare Zertifikat `scripts/certify_sw1_2tp_ledger.py` (Python/SymPy 1.14.0) prüft 88 Echo-Fälle, Hub-Support, Pivot und Eigenkanäle mit PASS. Der Perplexity-Blindcheck ist dokumentiert FAIL und erzeugt kein cross-model GREEN.

SW1-AWI (`audits/P11_R32_SW1_AWI_CANDIDATE.md`, PR #18) ist AI-GREEN + `independent GREEN (certificate)`: die A-Wall-Dichotomie ist vollständig fallweise normalisiert; in der oberen Kammer wirkt die Kollision über die maßtreue Reflexion \(s\mapsto\Delta-s\), und der zugehörige Zwei-Kanal-Block ist strikt invertierbar. Das Vollzertifikat `scripts/certify_sw1_awi.py` (Python/SymPy 1.14.0) prüft Geometrie, Fixpunkt, Koeffizientenordnung, Eigenkanäle und Invertierbarkeit mit PASS. Perplexity ist PARTIAL/FAIL und erzeugt kein cross-model GREEN.

Keine dieser Kandidatenzeilen trägt eine Promotion; keine Aussage über A0, HT-RED oder \(\ker\Gamma_I\).

Exakte Status- und Quellenliste:
[ACTIVE_THEOREM_REGISTRY](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).

---

## 3. Gemergter Zwischenmeilenstein: PR #10

PR #10 theorematisiert nur den einfachen SW1-Membership-Satz und ist inzwischen in `main` gemergt.

Ziel/Kern (§12, vollständig):
\[
\boxed{
\begin{array}{l}
s,\ a-s,\ a+s,\ T-s,\ 2d-s,\ T+s\ \text{sind auf SW1 direkte Blindwerte, }(Z,Z,Z,Z,Z,Z),\\
D_-,\ D_0,\ D_+,\ E,\ A_*>\varepsilon,\\
I_b\cap I_-=\emptyset,\qquad I_b\cap I_+\neq\emptyset\iff\varepsilon>\Delta/2,\\
\text{inkl. korrektem Berührungsfall bei }\varepsilon=\Delta/2.
\end{array}
}
\]

Der Beweis in PR #10 ist absichtlich selbständig und verwendet HT.17/18, HT.23–27, FG-TR1 und HT-A4a **nicht als Beweisblackboxen**.

Aktueller Status:

\[
\boxed{
\mathrm{HT\!-\!A4b\!-\!SW1\!-\!M}:\checkmark[M]
}
\]

Promotet mit kanonischem Promotionsrecord `audits/P11_R32_HT_A4B_SW1_M_PROMOTION.md`. Exakter adversarial und mechanisch geprüfter Review-Head: `f8f9f107b9c6879611ecb492979737a5541141e9`; Squash-Merge in main: `b06f50f12973e781b87db8b06e54fd590a053b10`. Keine Mitpromotion von HT-A4b global, HT-RED, A0 oder Schur-Cross-Gram.

---

## 4. Nächster mathematischer Schritt

PR #40 hat den bestehenden A2–A10-Stack rückwärts reconciliert.

Der historische erste Bruch der alten linearen Strategie liegt bei

\[
\boxed{
\mathrm{A3}\to\mathrm{A4},
}

weil A4–A9 Struktur-/No-Go-/Separatoraussagen liefern, aber keine weitere Implikation
\[
\ker\Gamma_I=\{0\}.
\]

Operativ ist dieser alte Bruch jedoch durch A10-C0 umgangen: Statt \(\mathfrak G_R^{-1}\) explizit auszurechnen, wird der inversefreie Operator

\[
\boxed{
\mathscr C_R(\xi,w)
=
(I+A)J_R\xi+HE_{\mathcal A}w
}
\]

verwendet. PR #40 härtet die beidseitige Korrespondenz mit

\[
\Theta=J_R\oplus I_{\mathscr W},
\qquad
\Theta^{-1}(y,w)=(\Psi_Ry,w),
\]

und damit

\[
\boxed{
\ker\mathscr C_R
\xrightarrow{\sim}
\ker\mathcal K_{I,A}
\xrightarrow{\sim}
\ker\Gamma_I.
}
\]

C1C1 transportiert weiter mittels

\[
W=(U_H|_K)\oplus U_W
\]

auf den echten Bildraum

\[
\mathcal R_K\oplus\mathcal R_W,
\]

mit explizitem

\[
W^{-1}(F,G)
=
\bigl((U_H|_K)^{-1}F,U_W^{-1}G\bigr).
\]

Somit

\[
\boxed{
\ker\widehat{\mathscr C}_R
\cong
\ker\mathscr C_R
\cong
\ker\Gamma_I.
\]

Der Ambientraum ist ausdrücklich größer:
\[
WW^*=P_{\operatorname{Ran}W}\ne I_{\rm ambient}
\]
im Allgemeinen. Das PR-#40-Zertifikat konstruiert sogar einen nichttrivialen künstlichen Ambient-Kernelvektor; daher ist diese Scope-Grenze zwingend.

M1-FULL liefert im tatsächlichen \(r\)-Scope die exakte finite-range Darstellung

\[
\boxed{
(\widehat{\mathscr C}_R F)(\theta)
=
\sum_{j=-3}^{3}
M_j(\theta)F(\theta+jr_0),
\qquad r_0=\frac72,
}
\]

wobei jede \(M_j(\theta)\) eine explizite \(2\times2\)-Matrix ist.

Die aktuelle R43-Front liegt jedoch auf **B / Strong Terminal**; die historische M1-ND-Linie bleibt geparkt. Für den aktuellen Stand siehe die operative R43-Kopfschicht am Dateianfang sowie die dort verlinkten COND-Frontdateien.
