# P06 SYN — Primärcheck Jacobi–Feshbach + Divisorgraph

**Datum:** 9. August 2026  
**SYN-Ziel:** `papers/P06_Jacobi_Feshbach_and_Divisor_Graph.md`  
**Geprüfter SYN-Stand:** Commit `10c06c4ea467dda3a61f724151a8a8a224ccb6e0`  
**Pass-A-Basis:** Gruppe G `P06 PASS A COMPLETE — doppelt geprüft`  
**Primärreconciliation:** `audits/AUDIT-2026-08-09_P06_PassA_Primaerreconciliation.md`, Commit `3e9b816d`  
**Pass-A-Zweitcheck:** `audits/AUDIT-2026-08-09_P06_PassA_Zweitcheck_Pfadgebunden.md`, Commit `b40af085`  
**Prüfart:** SYN-Direktaudit; kein erneuter Vollaudit der historischen NEU-Knoten  

---

## 0. Prüfauftrag

Geprüft wurde ausschließlich, ob der neue P06-SYN-Draft den versiegelten Gruppe-G-Endstand korrekt destilliert. Kontrolliert wurden:

1. Typen und Operatorrollen;
2. Formeln und Normierungen;
3. mathematische Status (`✓[M]`, `✓[K/M]`, `×[M]`, `?[O]`, `CONDITIONAL`, `SUPERSEDED`);
4. Modell-/Sektorscope;
5. P06/P11-Routing;
6. unzulässige Hochstufungen historischer Zielbehauptungen;
7. die beiden neuen Korrekturen G-T4/G-T5.

Nicht durchgeführt wurde ein neuer 33-Knoten-Audit von NEU-058–090.

---

## 1. Im SYN-Draft gefundene lokale Korrektur 1 — kollektiver Koppler

Die Erstfassung des SYN-Drafts schrieb in Def. 1.1

$$
V_N:=\bigoplus_{p\le N}V_p.
$$

Diese Schreibweise war im P06-Kontext missverständlich beziehungsweise typologisch zu stark: Gerade die spätere Reconciliation erlaubt überlappende Zielbilder der $V_p$ und verbietet eine Interpretation als orthogonale Direktsumme der Primkanalbilder.

G-T1 übernimmt aus NEU-050 die formale kollektive Schreibweise

$$
V_N=\sum_{p\le N}V_p,
$$

unter den jeweiligen Typvoraussetzungen, mit

$$
\mathcal K_N(z)=V_N^*(D_{\rm rel}-z)^{-1}V_N,
\qquad
K_{pq}(z)=V_p^*(D_{\rm rel}-z)^{-1}V_q.
$$

Der SYN-Draft wurde deshalb in Commit `10c06c4` korrigiert zu einem **kollektiven Koppler/Zeilenoperator**, ausdrücklich ohne orthogonale Direktsummenbehauptung über die Zielbilder.

**Urteil:** lokaler SYN-Transkriptions-/Typisierungsfehler; **korrigiert**, kein Fehler des versiegelten Pass-A-Endstands.

---

## 2. Im SYN-Draft gefundene lokale Korrektur 2 — Bipartitheit

Die Erstfassung formulierte zu stark, Bipartitheit sei „das Kriterium“ für das Verschwinden aller ungeraden Spuren. G-T3 beweist im relevanten endlichen symmetrischen Graphscope:

$$
\text{$r$-Gradierung allein}
\not\Rightarrow
\operatorname{Tr}(A_N^{2j+1})=0,
$$

und

$$
\text{Bipartitheit}
\Rightarrow
\text{keine ungeraden geschlossenen Wege}
\Rightarrow
\operatorname{Tr}(A_N^{2j+1})=0.
$$

Der SYN-Draft wurde in Commit `10c06c4` auf die sauberere Aussage abgeschwächt: **echte Bipartitheit ist eine robuste strukturelle Zusatzbedingung**, die ungerade geschlossene Wege ausschließt. Eine unnötige globale Notwendigkeits-/Äquivalenzbehauptung wird nicht gemacht.

**Urteil:** lokale SYN-Überformulierung; **korrigiert**, kein Fehler des versiegelten Pass-A-Endstands.

---

## 3. Typ- und Spektralprüfung

### 3.1 Kollektive Birman–Schwinger-Architektur

Der korrigierte SYN-Draft übernimmt richtig:

$$
\mathcal K_N(z)=V_N^*(D_{\rm rel}-z)^{-1}V_N,
\qquad
K_{pq}(z)=V_p^*(D_{\rm rel}-z)^{-1}V_q,
$$

nur unter Typ-/Domainvoraussetzungen.

Richtig getrennt werden:

- formale Operatorarchitektur;
- mögliche/generische Kanalbildüberlappung;
- nicht bewiesenes universelles $K_{pq}(z)\neq0$ für jedes $p\neq q$;
- intrinsische globale Quell-/Gramkonstruktion, die nach P11 geroutet bleibt.

**Ergebnis:** `OK`.

### 3.2 Transportgenerator statt HP-Endoperator

Der SYN-Draft beschränkt die Transportnormalform

$$
D_{\rm rel}|_{\mathcal H_{p,a}}
\cong
2i\kappa_p^{\rm tr}\frac d{dt}
$$

korrekt auf die auditierten Primfasern und übernimmt dort rein absolutstetiges Spektrum, Kernfreiheit und fehlenden kompakten reduzierten Resolventen. Er schließt ausdrücklich keinen anderen späteren Objekt-X-/HP-Endoperator aus.

**Ergebnis:** `OK`.

### 3.3 Spektralmaß statt diskreter Eigenbasis

Die historische NEU-051-Darstellung wird korrekt als `SUPERSEDED` markiert. Verbindlich übernommen wird

$$
\mu_{pq}^{a,b}(B)=\langle V_pa,E_D(B)V_qb\rangle,
$$

$$
\langle a,K_{pq}(z)b\rangle
=
\int_{\mathbb R}\frac{d\mu_{pq}^{a,b}(\lambda)}{\lambda-z}.
$$

Der Spektralsatz selbst wird nicht verworfen.

**Ergebnis:** `OK`.

---

## 4. Normalisierungs- und Divisorgraphprüfung

Der SYN-Draft übernimmt korrekt

$$
J_N^-:=\frac12(\Theta_N-\Theta_N^\dagger),
\qquad
S_N:=\frac1{2i}(\Theta_N-\Theta_N^\dagger)=-iJ_N^-.
$$

Er behauptet keine intrinsische $\gamma_N=1$-Rigidität.

Für die endliche Graph-/Trace-Schicht werden korrekt migriert:

$$
\operatorname{Tr}(A_N)=0
$$

bei off-diagonalem endlichem $A_N$ sowie

$$
\operatorname{Tr}(A_N^2)=\|A_N\|_{HS}^2
$$

im endlichen selbstadjungierten Fall.

Ebenso korrekt:

$$
\log(p^k)=k\log p\neq\Lambda(p^k)=\log p
\qquad(k>1).
$$

Die historische konkrete $\sum r^2\log^2n$-Normalisierung wird nicht als kanonische P06-Form hochgestuft.

**Ergebnis:** `OK` nach Korrektur aus §2 dieses Audits.

---

## 5. Feshbach-/Schattenprüfung

Der SYN-Draft hält die zentrale Firewall ein:

$$
\boxed{
\text{endliche Feshbachidentität}
\neq
\text{Schattennorm-kontrollierter globaler Limes}.
}
$$

Er unterscheidet die pathwise Skala

$$
M_N^{\rm path}\lesssim\frac{N}{\log N}
$$

von der strengeren Operatorstabilitätsskala

$$
M_N^{\rm op}\lesssim\sqrt{\frac{N}{\log N}}.
$$

Festes $N$ wird nicht mit endlichem Rang von $\mathcal K_N$ verwechselt. Schatten-/Fredholmrealisierung bleibt bis zur intrinsischen Quelle/Gramgeometrie offen beziehungsweise konditional.

**Ergebnis:** `OK`.

---

## 6. G-T4 — zweite Schleifenspur

Der SYN-Draft übernimmt den korrigierten Modellbefund vollständig:

$$
T_N(z)
=O_z\!\left(\frac{\log\log N}{\log N}\right)
\to0
$$

auf der pathwise Skala $M_N=N/\log N$ für festes zulässiges $z$.

Der historische Grenzwert

$$
T_N(z)\to\gamma^2/2
$$

wird korrekt als `×[M]` geführt.

Keine unzulässige Hochstufung über den NEU-088–90-Modellscope hinaus gefunden.

**Ergebnis:** `OK`.

---

## 7. G-T5 — höhere Schleifen und relative Determinante

Der SYN-Draft übernimmt korrekt, dass für komplexes $z$

$$
C_N(z)=R_N(z)^{1/2}B_N^\Lambda R_N(z)^{1/2}
$$

im Allgemeinen nicht selbstadjungiert ist. Die historische Gleichsetzung

$$
\|C_N\|_{HS}^2=\operatorname{Tr}(C_N^2)
$$

wird verworfen und ersetzt durch

$$
\|C_N\|_{HS}^2=\operatorname{Tr}(C_N^*C_N).
$$

Weiter korrekt übernommen:

$$
\|C_N(z)\|_{HS}^2
=O_z\!\left(\frac{\log\log N}{\log N}\right)
\to0,
$$

$$
\|C_N(z)\|\to0,
$$

und für jedes feste $k\ge3$

$$
|\operatorname{Tr}(C_N^k)|
\le
\|C_N\|^{k-2}\|C_N\|_{HS}^2
\to0.
$$

Im konkreten endlichen NEU-088–90-Modell wird korrekt gefolgert:

$$
\boxed{
\log D_N(z)\to0,
\qquad
D_N(z)\to1.
}
$$

Der SYN-Draft markiert ausdrücklich, dass dies **kein allgemeiner Feshbach-No-Go** ist.

**Ergebnis:** `OK`.

---

## 8. Offene Aussagen und Routing

Keine der folgenden Aussagen wird unzulässig hochgestuft:

- zusammengesetzte Sektoren `[O-225-3]`: `?[O]`;
- $Z_N\to C\xi$: `?[O] / CONDITIONAL`;
- $V\in\mathcal S_4\setminus\mathcal S_2$: strukturelle Arbeitshypothese / offen;
- globale Schatten-/Fredholmklasse: offen/konditional;
- intrinsische Liftunabhängigkeit: P11;
- Quellhilbertisierung: P11;
- Gramoperator und Mischblock $\beta_p$: P11;
- globale nichtorthogonale Kopplungsgeometrie: P11.

Der $u$-Parameter wird korrekt als Hebungswahl und nicht als frei justierbarer Regulator geführt.

**Ergebnis:** `OK`.

---

## 9. Primärcheck-Endurteil

Nach Anwendung der beiden lokalen SYN-Draft-Korrekturen aus Commit `10c06c4` wurde **kein verbleibender mathematischer, typologischer, Status- oder Routingkonflikt** gegenüber dem versiegelten P06-Pass-A-Endstand gefunden.

\[
\boxed{\text{P06 SYN PRIMARY CHECK COMPLETE.}}
\]

\[
\boxed{\text{kein verbleibender konkreter Gegenbefund.}}
\]

Der Markdown-SYN-Stand kann daher auf

`SYN PRIMARY AUDITED — unabhängiger SYN-Zweitcheck ausständig`

gesetzt werden.

**Noch nicht zulässig:**

- `SYN FINAL AUDITED`;
- LaTeX-Transfer;
- `SYN FROZEN`;
- Eintrag als eingefrorenes P06 in `SYN_PROVENIENZ.md`.

Diese Schritte folgen erst nach einem unabhängigen pfadgebundenen P06-SYN-Zweitcheck ohne konkreten Gegenbefund.

---

## 10. Epistemische Firewall

Der SYN-Primärcheck bestätigt die korrekte **Migration des bereits auditierten Endstands**. Er beweist keine neue Objekt-X-Konstruktion, keine globale Schattenrealisierung und keine Aussage der Riemannschen Vermutung.
