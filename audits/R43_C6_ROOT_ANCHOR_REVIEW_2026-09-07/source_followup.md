# C6-Wurzelanker: gezielter Schlussreview der Randspur-Reparatur

**7. September 2026 — Urteil: SCOPED GREEN.**
Dieser Folgecheck ersetzt nicht den vollständigen vorherigen Review
`c6_root_anchor_source_review.md`, sondern prüft gezielt die danach
ergänzten QR1–QR5, den tatsächlichen LaTeX-Diff und die angepassten
PA17–PA18. Die drei geprüften Dateistände sind:

| Datei innerhalb des Repos | Exakter Git-Dateiblob | Bytes / Zeilen |
|---|---|---:|
| `audits/P11_R43_POSITIVE_ROOT_ANCHOR_STRONG_TERMINAL_2026-09-07.md` | `53dbdbc1b540f8c750da4876823d02f157b2ffe9` | 13095 / 348 |
| `audits/P11_R43_QUADRATURE_BOUNDARY_TRACE_REPAIR_2026-09-07.md` | `300001d99259f3dbb5fd2c18155adb92cf4c551c` | 6187 / 152 |
| `papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex` | `6df7308cf269f09c6564ab162ed9b647cb3929da` | 14340 / 467 |

Die zusätzlichen SHA-256-Werte stehen in
`c6_root_anchor_followup_exact_blobs.json`. HEAD ist weiterhin
`55a3a1617513cc5d82c47d0cfd606c6b0894c984`; die neuen Dateiblobs sind
nicht Bestandteile dieses gepinnten Commits. Der beobachtete einzige
tracked Diff betrifft die hier genannte TeX-Datei. Der Reviewer hat
keine Repository-Datei geändert.

## 1. QR1–QR3: beide Sprünge sind korrekt bilanziert

Die exakte positive Zellmassenbilanz liefert für das kumulierte
Quadraturfehlermaß
\[
|F_T(r)|\le |I|\le Ce^{-4(T-r)/5}.
\]
Die beiden Sprünge des nullerweiterten reflektierten Terms haben
tatsächlich die angegebenen Vorzeichen:
\[
-2k_T^0(0+)\alpha(v)\quad(r=v/2),\qquad
+2k_T^0(T-)\alpha(v)\quad(r=(T+v)/2).
\]
Partielle Integration erfolgt für jedes feste \(v\) skalar. Die endlichen
Quadraturatome können nur für eine Nullmenge von \(v\) mit einer dieser
Sprungstellen zusammenfallen. Deshalb ist anschließendes \(L^2_v\) und
Minkowski genau wie QR3 zulässig; Hilbert-BV wird nicht behauptet.
Auch an den äußeren Integrationsgrenzen entsteht kein fehlender Term:
\(\Phi_T(0)(v)=\Phi_T((T+\varepsilon)/2)(v)=0\) für fast jedes \(v\),
weil \(\alpha\) kompakt in \((0,\varepsilon)\) liegt.
Dies ist ein eigenständiger Nachweis des korrigierten Mechanismus;
der ursprüngliche fehlerhafte Ausdruck stand in
[P11, Zeilen 279–315 am Pin](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L279-L315).

## 2. QR4: die Exponenten und beide Fehlerregime bestehen den Gegencheck

Die regularisierte Ableitung enthält im wachsenden Teil den Faktor
\[
\frac{e^{(T-2r)/2}}{\sqrt{1+T-2r}}.
\]
Multiplikation mit \(|F_T(r)|\) ergibt
\[
e^{-4T/5+4r/5}\,e^{T/2-r}
=e^{-3T/10-r/5}.
\]
Das \(r\)-Integral ist gleichmäßig beschränkt. Der konstante Anteil hat
dagegen das Integral
\[
\frac{|K_T|}{T}e^{-4T/5}
\int_0^{(T+\varepsilon)/2}e^{4r/5}dr
\le C_\alpha\frac{|K_T|}{T}e^{-2T/5}.
\]
Der linke Sprung trägt höchstens
\[
C_fe^{-3T/10}/\sqrt T
C_\alpha |K_T|T^{-1}e^{-4T/5}
\]
bei, der rechte höchstens
\(C_\alpha |K_T|T^{-1}e^{-2T/5}\).
Somit folgt einschließlich beider Spuren genau
\[
\boxed{\|Z_T^{\rm quad}\|_2
\le C_fe^{-3T/10}
+C_\alpha |K_T|T^{-1}e^{-2T/5}.}
\]
Der benötigte Trägerabstand für das Verschwinden des wachsenden Kerns
oberhalb \(T/2\) ist tatsächlich vorhanden:
[P11, Zeilen 94–153 am Pin](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L94-L153).

Für feste glatte \(m=0\)-Quellen ist dies weiterhin
\(o(\sqrt{M_T^{\rm cost}})\). Für die R16-Familie mit
\(K_T=O(\sqrt T)\) und uniformen glatten Kernschranken folgt nun zudem
**absolut** \(Z_T^{\rm quad}=o(1)\). Diese beiden Voraussetzungen der
R16-Anwendung wurden im Rohtext nachgeprüft:
[R16, Zeilen 57–106 und 123–158](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R16_TC1_NEARNULL_REMAINDER_2026-08-14.md#L57-L158).

## 3. QR5: Kosten unabhängig von der fehlerhaften Lipschitzbehauptung

Die lokale Kostenhülle und die positive Massenkostenidentität liefern,
bis auf harmlose feste Zellvergleichskonstanten, das Integral
\[
\int_0^{T/2}\frac{e^{-r}}{1+T-2r}\,dr
+C e^{-T/2}
+C\frac{|K_T|^2}{T^2}e^{-T/2}.
\]
Auf \([0,T/4]\) ist der erste Anteil \(O(T^{-1})\); auf
\([T/4,T/2]\) genügt bereits \(O(e^{-T/4})\).
Die ausgewiesene etwas gröbere QR5-Schranke
\[
\|Y_T^{\rm prim,-}\|^2
\le C_f\left(T^{-1}+Te^{-T/4}
+|K_T|^2T^{-2}e^{-T/2}\right)
\]
ist deshalb richtig. Für die R16-Familie folgt sogar
\(\|Y_T^{\rm prim,-}\|^2=O(T^{-1})\).
Die echte vollständige \(a=0\)-Hebung bleibt unverändert; mit ihrer
Tailoperatornorm \(O(\sqrt{T+1}e^{-T/2})\) ist der zusätzliche
R16-Sourcefehler ebenfalls absolut \(o(1)\).
Hier wurde keine primitive Formdominanz eingeschoben:
[P11, Massenkosten Zeilen 248–270](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L248-L270),
[P11, vollständige Hebung Zeilen 317–359 am Pin](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L317-L359).

## 4. Korrigierter gegenüber früherem Prüfstand

**Früher:** Meine globale Hölder-\(1/2\)-Reparatur bewies die relative
Kleinheit für den scharfen festen \(m=0\)-Eingang des neuen Normalenbeweises.
Sie bewies nicht die absolute R16-Quadraturkleinheit.

**Jetzt:** QR1–QR5 und ihr tatsächlicher TeX-Diff schließen genau diesen
zusätzlichen absoluten Fehlerkanal. Deshalb muss das vollständige
C6-Beweispaket die neue gewichtete skalare Randspur-Reparatur importieren,
nicht bloß auf meine gröbere Hölder-Schranke verweisen.

Die kanonische PA-Datei verlinkt diese Reparatur nun ausdrücklich;
PA17–PA18 quantifizieren korrekt nur über \(m\ge1\). Der vorherige
Indexhinweis ist damit erledigt. Die Normalenalgebra PA1–PA19 und ihre
Scopes bleiben GREEN. Normalkonvergenz selbst benötigt kein GC-AC;
der ganze fixed-pair-C6-Limes importiert weiterhin ausdrücklich den
vorhandenen tangentialen R42.51-Satz im so korrigierten Eingangsrahmen:
[R42.51–R42.60](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md#L1322-L1480).

**Endurteil:** Kein neuer Blocker im gezielt geprüften Dreidateienpaket.
Dies ist keine pauschale Neuzertifizierung jeder früheren Auditdatei,
keine uniforme \(R,S\)- oder Operatornormaussage und keine Objekt-X-/RH-Promotion.

## 5. Zweiter Folgecheck: O3o/O3p ausdrücklich mitgezogen

**Erweiterter Schlussstand: ebenfalls SCOPED GREEN.**
Nach dem ersten Dreidateiencheck wurden zwei weitere kanonische
TeX-Module und der erläuternde QR-Audit ergänzt. Die aktuellen fünf
Prüfblobs stehen vollständig in
`c6_root_anchor_followup_final_exact_blobs.json`:

| Datei / Modul | Aktueller geprüfter Git-Dateiblob |
|---|---|
| PA1–PA19 | `53dbdbc1b540f8c750da4876823d02f157b2ffe9` |
| QR1–QR5, jetzt einschließlich R17-Anwendungsbullet | `08936b6ed315510a606986f96802b1e914b385be` |
| `P11_Odd_Asymptotic_FullProof.tex` | `6df7308cf269f09c6564ab162ed9b647cb3929da` |
| `P11_O3o_TC1_NearNull_Remainder_Collapse.tex` | `741124dd8dbab29452b24ca9af5d4be5dd7a8f67` |
| `P11_O3p_Vanishing_NearNull_Core.tex` | `1fb4217407e68ac3e2be3d2259ccd97ef450a40d` |

Der tatsächliche aktuelle tracked Diff umfasst jetzt **genau diese drei
TeX-Dateien**, nicht mehr nur die eine TeX-Datei des ersten Folgechecks.
Der Reviewer hat weiterhin keine Repository-Datei geändert.

**O3o:** Die neue direkte Verwendung der trace-aware Schranke mit
\(K_U=O(\sqrt U)\) liefert
\[
\|Z_U^{\rm quad}\|_2
\le Ce^{-3U/10}+CU^{-1/2}e^{-2U/5}=o(1).
\]
Zusammen mit der bereits geprüften diskreten \(O(U^{-1})\)-Kostenschranke
und dem unveränderten vollständigen Tail-Lift ist die konkret betroffene
R16-Absoluteingangsstelle geschlossen.

**O3p:** Für das feste glatte gerade mittelwertfreie Profil \(g\) gilt
\[
k_g^{(U)}(t)=2g(U-t),\qquad
k_g^{(U)}(0+)=0\quad(U\ \text{groß}),\qquad
k_g^{(U)}(U-)=2g(0).
\]
Der reguläre Source-Representer-Ableitungsteil liegt bei
\(r=U/2+O_g(1)\), ist \(O_g(1)\) beschränkt und hat einen
\(r\)-Träger von \(O_g(1)\) Länge. Auf diesem Träger ist
\(|F_U(r)|\le C_ge^{-2U/5}\), also beträgt sein Fehler
\(O_g(e^{-2U/5})\). Die obere Spur trägt ausdrücklich zusätzlich
\[
4|g(0)|\,\|\alpha(v)F_U((U+v)/2)\|_2
=O_g(e^{-2U/5})
\]
bei; die untere Spur ist null. Die diskreten Kosten bleiben
\(O_g(e^{-U/2})\), weil das Zertifikatsfeld ebenfalls in einem
Streifen fester Breite um \(U/2\) liegt und dort die inverse
primitive Massendichte \(O_g(e^{-U/2})\) ist. Die vollständige
Hebung und der Tailoperator sind unverändert.
Damit ist auch die feste R17-Profilabsorption bezüglich des gefundenen
Randspurfehlers wirklich repariert, nicht bloß behauptet:
[ursprünglicher O3p-Eingang, Zeilen 96–145 am Pin](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_O3p_Vanishing_NearNull_Core.tex#L96-L145).

**Endgültiger Scope dieses Folgechecks:** Die scharfe relative
Quellenergie, die betroffene absolute O3o/R16-Near-null-Quadratur
und die betroffene absolute O3p/R17-Profilabsorption haben jetzt
eine konsistente gemeinsame Randspurbehandlung. PA1–PA19 bleiben
mit den früher genannten Grenzen GREEN. Kein neuer Blocker im
geprüften Fünfdateienpaket.
