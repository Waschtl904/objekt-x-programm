# P06 LaTeX SYN — Transferaudit

**Datum:** 9. August 2026  
**SYN-Ziel:** P06 — Jacobi–Feshbach + Divisorgraph  
**Kanonische Markdown-Quelle:** `papers/P06_Jacobi_Feshbach_and_Divisor_Graph.md`  
**Markdown-Finalcommit:** `1ab1f004b03662b198d4affd245b03eb519b8154`  
**LaTeX-Ziel:** `papers/P06_Jacobi_Feshbach_and_Divisor_Graph.tex`  
**LaTeX-Erstcommit:** `d7d76c7ddd1e030718ff61ec593dd883b719675b`  
**SYN-Primärcheck:** `audits/AUDIT-2026-08-09_P06_SYN_Primaercheck.md`, Commit `b077a814`  
**SYN-Zweitcheck:** `audits/AUDIT-2026-08-09_P06_SYN_Zweitcheck_Pfadgebunden.md`, Commit `7c570498`; Urteil `OHNE KONKRETEN GEGENBEFUND`  
**Prüfart:** reiner Markdown→LaTeX-SYN-Transferaudit; kein neuer Vollaudit der historischen NEU-Knoten

---

## 1. Prüfauftrag

Geprüft wurden ausschließlich:

1. Übertragung des mathematisch versiegelten P06-Markdown-Endstands nach LaTeX;
2. Typ- und Formeltranskription;
3. Status- und Scope-Erhalt;
4. P06/P11-Routing;
5. LaTeX-Syntax und Kompilierbarkeit;
6. Vermeidung historischer `SUPERSEDED`-Aussagen als neue Sätze.

Keine neue mathematische Hochstufung war zulässig.

---

## 2. Kritische Formelkontrolle

| Punkt | Markdown-Endstand | LaTeX | Urteil |
|---|---|---|---|
| Kollektiver Koppler | $V_N=\sum_{p\le N}V_p$, keine orthogonale Direktsumme der Zielbilder | identisch typisiert | `OK` |
| Kreuzblock | $K_{pq}(z)=V_p^*(D_{\rm rel}-z)^{-1}V_q$ | identisch | `OK` |
| Spektralmaß | $\mu_{pq}^{a,b}(B)=\langle V_pa,E_D(B)V_qb\rangle$ | identisch | `OK` |
| Stieltjesform | $\langle a,K_{pq}(z)b\rangle=\int d\mu_{pq}^{a,b}(\lambda)/(\lambda-z)$ | identisch | `OK` |
| Transportnormalform | $D_{\rm rel}|_{\mathcal H_{p,a}}\cong2i\kappa_p^{\rm tr}d/dt$ | identisch | `OK` |
| Jacobi-Typtrennung | $J_N^-=\frac12(\Theta_N-\Theta_N^\dagger)$; $S_N=\frac1{2i}(\Theta_N-\Theta_N^\dagger)=-iJ_N^-$ | identisch | `OK` |
| zweite Spur | $T_N(z)=O_z(\log\log N/\log N)\to0$ | identisch | `OK` |
| HS-Norm | $\|C_N\|_{HS}^2=\operatorname{Tr}(C_N^*C_N)$ | identisch | `OK` |
| HS-Kollaps | $\|C_N(z)\|_{HS}^2=O_z(\log\log N/\log N)\to0$ | identisch | `OK` |
| Determinante | $\log D_N(z)\to0$, $D_N(z)\to1$ | identisch | `OK` |

---

## 3. Status- und Scopekontrolle

Die LaTeX-Fassung bewahrt die verbindlichen P06-Firewalls:

- `D_rel` nur im auditierten Primfaser-Scope als Transportgenerator;
- NEU-051-Diskreteigenbasis `SUPERSEDED`;
- universelles $K_{pq}\neq0$ für alle $p\neq q$ nicht behauptet;
- festes $N$ nicht als endlicher Rang gelesen;
- endliche Feshbachidentität nicht zu Schattennormkonvergenz hochgestuft;
- $u$ als Hebungswahl, nicht als freier Regulator;
- $V\in\mathcal S_4\setminus\mathcal S_2$ bleibt Arbeitshypothese / `?[O]`;
- `[O-225-3]` bleibt offen;
- $Z_N\to C\xi$ bleibt `?[O]/CONDITIONAL`;
- der Kollaps $D_N(z)\to1$ bleibt strikt auf das konkrete NEU-088–90-Modell beschränkt;
- kein allgemeiner Feshbach-No-Go wird behauptet.

**Urteil:** `STATUS/SCOPE OK`.

---

## 4. P06/P11-Routing

Die LaTeX-Fassung enthält als P06-Bausteine:

- endliche Schur-/Feshbach-Grammatik;
- Weyl-/Stieltjes-Resolventensprache;
- Birman–Schwinger-Kreuzblöcke;
- projektionswertige Kreuzspektralmaße;
- Divisorgraph-/Trace-Geometrie;
- endliche Schleifen-/Determinantenmodelle;
- konditionale Schatten-/Fredholmkriterien.

Nach P11 gesperrt bleiben:

- intrinsische Liftunabhängigkeit;
- Quellhilbertisierung;
- Gramoperator;
- Mischblock $\beta_p$;
- globale nichtorthogonale Kopplungsgeometrie;
- daraus abgeleitete globale Fredholm-/Schattenrealisierung.

**Urteil:** `ROUTING OK`.

---

## 5. LaTeX-Kompilierbarkeit

Die erzeugte Datei wurde lokal mit `pdflatex` zweimal kompiliert.

Ergebnis:

- Exit-Code: `0`;
- Ausgabe: 8 Seiten;
- keine undefinierten Referenzen;
- keine LaTeX-Fehler;
- lange Repo-Pfade über `xurl` umbrechbar;
- breite Schlussboxen in mehrzeilige `gathered`-Blöcke gesetzt;
- verbleibend lediglich eine harmlose `Overfull \\vbox`-Meldung von ca. 2.6 pt beim Seitenumbruch, ohne Inhaltsverlust.

**Urteil:** `COMPILES`.

---

## 6. Endurteil

Es wurde kein Formel-, Typ-, Status-, Scope-, Routing- oder Transkriptionskonflikt zwischen der kanonischen Markdown-Fassung und der LaTeX-Fassung gefunden.

\[
\boxed{\text{P06 LATEX SYN TRANSFERAUDIT COMPLETE.}}
\]

\[
\boxed{\text{P06 SYN FROZEN }\checkmark[K/M].}
\]

Die LaTeX-Fassung darf als eingefrorene SYN-Fassung verwendet werden.

---

## 7. Epistemische Firewall

`SYN FROZEN` bedeutet ausschließlich, dass der konsolidierte P06-Endstand korrekt übertragen und auditiert ist. Es bedeutet insbesondere nicht:

- Objekt X sei konstruiert;
- eine globale Fredholmdeterminante sei realisiert;
- die Riemannsche Vermutung sei bewiesen;
- ein allgemeiner Feshbach- oder Jacobi-No-Go sei bewiesen.
