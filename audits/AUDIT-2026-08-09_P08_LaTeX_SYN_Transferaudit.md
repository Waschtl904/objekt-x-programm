# P08 LaTeX-SYN — Transferaudit

**Datum:** 9. August 2026  
**LaTeX-Ziel:** `papers/P08_Renormalized_Prime_Operators_and_Finite_Part_Structures.tex`  
**LaTeX-Commit:** `d283c34ccb5de73395e4630c2d51a9fc7052b71c`  
**Kanonische Markdown-Quelle:** `papers/P08_Renormalized_Prime_Operators_and_Finite_Part_Structures.md`, Draft-Commit `29101001e79ab5418fd8dde0af30a1d27ca2e038`  
**SYN-Primärcheck:** Commit `f3330c2f`  
**SYN-Zweitcheck:** Commit `3d3b8864`  
**Prüfart:** reiner Markdown→LaTeX-Transferaudit; kein erneuter NEU-Vollaudit  

---

## 0. Prüfauftrag

Geprüft wurden ausschließlich:

1. Abschnitts- und Rollenübertragung Markdown→LaTeX;
2. Formeltranskription;
3. Status `PROVED`, `NO-GO`, `OPEN`, `CONDITIONAL`, `DEFINITION`;
4. P05/P06/P07-Firewalls;
5. Trennung der beiden P08-Stränge;
6. Mellin-Typisierung `S` versus `Psi`;
7. offene Root-Blocker und Routing;
8. LaTeX-Struktur mit geschlossenen Umgebungen und abschließendem `\\end{document}`.

---

## 1. Typ- und Statusübertragung

Die LaTeX-Fassung hält die zentrale Jacobi-Trennung ein:

- `A_N^sym=B_N^Lambda` ist der endliche selbstadjungierte direkte Symmetriepfad;
- `J_N^-` bleibt schiefadjungiert und `S_N=-iJ_N^-` selbstadjungiert;
- die konkrete Selbstadjungiertheit des historischen `A_N^{Jac,-}` bleibt offen.

Der KMS/GNS-Block übernimmt die korrigierten Formeln

$$
C_\xi=1+\frac{\gamma_E}{2}-\frac12\log(4\pi),
\qquad
\widehat\Omega=Z^{-1/2}\Omega_\tau,
\qquad
Z_{1,N}^{-1}\sim1/\log N.
$$

Keine historische gesperrte Normierung wurde positiv reimportiert.

**Ergebnis:** `OK`.

---

## 2. Renormierungsdiagnose

LaTeX übernimmt streng

$$
b_{1,N}\asymp\gamma\sqrt{\log N/N}\to0
$$

und

$$
\langle e_0,(A_N^{sym}-z)^{-1}e_0\rangle\to-1/z.
$$

Die globale Diagonalitätsfolge ist als No-Go sichtbar. Das No-scalar-Lemma steht nur unter der offenen Quotientendivergenz; `W_N` bleibt separate offene Konstruktion.

**Ergebnis:** `OK`.

---

## 3. Self-Energy und Spurklasse

Die algebraische Zerlegung

$$
\Sigma_{rel}=\Sigma_{rel}^{\infty}+\Sigma_{rel}^{ren}(\beta)
$$

wird ohne unbewiesene Divergenzaussage übertragen.

Die feste-beta-Spurklasse setzt ausschließlich

- modellrelativ `rank C_p^rel<=1`,
- `|c_p|^2=O((log p)^2/p)`

voraus. T2 und `c_p!=0` werden ausdrücklich nicht als Voraussetzungen dieses Schritts eingesetzt.

T2/Nichtentartung beginnen erst bei der primdiagonalen Mangoldt-Observable. Die gewöhnliche Spuridentität mit `-zeta'/zeta` ist auf `Re beta>1` und den conditionalen Modellscope beschränkt.

**Ergebnis:** `OK`.

---

## 4. Mellin- und Finite-Part-Transfer

LaTeX überträgt als exaktes Mellin-Objekt

$$
\Psi_{\varphi,X}(\beta)=\sum_n\Lambda(n)\varphi(n/X)n^{-\beta},
$$

mit

$$
\Psi_{\varphi,X}(\beta)
=\frac1{2\pi i}\int_{(c)}\widehat\varphi(s)X^s
\left(-\frac{\zeta'}{\zeta}(\beta+s)\right)ds.
$$

Die falsche Prime-only-Identität für `S_{varphi,X}` bleibt gesperrt. Ebenso korrekt übertragen:

$$
\operatorname{Res}_{s=0}\widehat\varphi(s)=1,
$$

und

$$
\Psi-S
=\sum_{k\ge2}\sum_p\log p
[\varphi(p^k/X)-\varphi(p/X)]p^{-k\beta}.
$$

Der quantitative/uniforme Transfer, die uniforme Kontur/Residuenzählung sowie Primlabel-Finite-Part und R-Cutoff bleiben offen.

**Ergebnis:** `OK`.

---

## 5. Finite-Part-Tautologie und Operatorbrücke

Die LaTeX-Definition

$$
\Tr_{reg}(R\Sigma)(\beta):=\AC[-\zeta'/\zeta](\beta)
$$

wird ausdrücklich nur als Definition geführt. Sie ersetzt keinen operatoriellen Grenzwert.

Die Primlabel-Observable `N_P` bleibt conditional und trägt die korrekte Domänengewichtung

$$
\sum_pp^2|\xi_p|^2\|\Psi_p\|^2<\infty.
$$

**Ergebnis:** `OK`.

---

## 6. Statusmatrix und Routing

Die LaTeX-Statusmatrix bewahrt die zentralen Statusunterschiede. Die Root-Blocker sind vollständig sichtbar. Das Routing bleibt:

- negative Befunde → P10;
- intrinsische Lift-/Gram-/T2-/Nichtentartungs- und globale Schattenfragen → P11;
- Finite-to-Infinite-Weil-Grenzen → P12.

Kein No-Go wird zu einem allgemeinen Ausschluss der Methode überdehnt.

**Ergebnis:** `OK`.

---

## 7. Technische LaTeX-Prüfung

Die live gespeicherte Datei wurde strukturell geprüft:

- vollständige `amsart`-Präambel;
- benötigte Pakete für Theoreme, Tabellen und Mathematik eingebunden;
- Theorem-/Definition-/Open-Problem-Umgebungen geschlossen;
- `longtable` geschlossen;
- Labels/Referenzen im übertragenen Text konsistent verwendet;
- Datei endet ordnungsgemäß mit `\\end{document}`.

Eine lokale `pdflatex`-Kompilierung wurde in dieser Sitzung **nicht ausgeführt**, weil die GitHub-Connector-Datei nicht als lokale Containerdatei materialisiert werden konnte und der Container keinen DNS-Zugriff auf den Raw-GitHub-Endpunkt hatte. Dies ist kein mathematischer Gegenbefund; es wird ausdrücklich **kein erfolgreicher Compile behauptet**.

---

## 8. Transferurteil

Zwischen der doppelt geprüften Markdown-Inhaltsstufe und der LaTeX-Fassung wurde kein Status-, Typ-, Formel-, Scope- oder Routingkonflikt gefunden.

$$
\boxed{
\text{P08 LaTeX-SYN-TRANSFERAUDIT: OHNE KONKRETEN GEGENBEFUND.}
}
$$

Die mathematische SYN-Migration kann als `SYN FROZEN ✓[K/M]` gebucht werden. Eine spätere technische Kompilierungsprüfung darf rein redaktionell nachgetragen werden, ohne den mathematischen Pass-A-/SYN-Status neu zu öffnen, sofern sie keinen inhaltlichen Transkriptionsfehler findet.
