# P08 Pass-A — unabhängiger Eröffnungsgegencheck

**Datum:** 9. August 2026  
**Scope:** Gegencheck ausschließlich der Pass-A-Eröffnungsbestandsaufnahme, kein Vollaudit von P08  
**Geprüfter Anker:** `audits/AUDIT-2026-08-09_P08_PassA_Eroeffnung_Inventar.md`, Commit `b0d8113a`  

## Ergebnis

Die Prüfpunkte A–F und H wurden ohne konkreten Gegenbefund bestätigt:

- Live-Inventar: 41 Forschungsdokumente; doppelte Kennung `NEU-123F`; `NEU-126` und `NEU-129` fehlen live.
- Juli-Provenienz: DAG-Audit NEU-123–127 sowie die dokumentierten Auditblöcke bis NEU-150 sind als historische Auditbasis vorhanden.
- Audit-Reuse darf nicht nach bloßer NEU-Nummer erfolgen; die Beispiele NEU-130, NEU-136 und NEU-128A belegen die notwendige Inhaltsreconciliation.
- P05-Firewalls zu Rang, Projektorstatus, Nichtentartung, Hebungsabhängigkeit und fehlender termweiser `|c_p|^2`-Asymptotik sind korrekt übernommen.
- P06-Firewalls zur Typtrennung `J_N^-`/`S_N`, zum Transportcharakter von `D_rel`, zur endlichen Feshbachidentität und zum modellgebundenen Determinantenkollaps sind korrekt übernommen.
- Die bindende `C_\xi`-Korrektur ist korrekt: 
  \[
  C_\xi=-\frac{\xi'(0)}{\xi(0)}=1+\frac{\gamma_E}{2}-\frac12\log(4\pi)\approx0.0230957.
  \]
  Der historische Wert `-0.5493` ist `SUPERSEDED`.
- Die fünf Pakete H-T1 bis H-T5 sind als minimale Pass-A-Zerlegung sachlich gerechtfertigt; kein 41-Dateien-Vollaudit ist erforderlich.

## Einziger konkreter Gegenbefund — Präzisierung zu NEU-148 §148.2/§148.6

Die mathematische Mellin-Diagnose der Eröffnung ist richtig, aber die Beschreibung des Live-Blatts NEU-148 war zu pauschal.

Live-NEU-148 tut zweierlei gleichzeitig:

1. §148.1 definiert
   \[
   S_{\varphi,X}(\beta)=\sum_p\varphi(p/X)\frac{\log p\,p^{-\beta}}{1-p^{-\beta}}.
   \]
2. §148.2 identifiziert diese Größe fälschlich über Mellin-Inversion mit `-\zeta'/\zeta(\beta+s)` und markiert die Mellin-Darstellung positiv.
3. §148.6 erkennt jedoch selbst den Unterschied zur echten von-Mangoldt-Summe
   \[
   \Psi_{\varphi,X}(\beta)=\sum_{n\ge1}\Lambda(n)\varphi(n/X)n^{-\beta}
   \]
   und schreibt die Primpotenzenkorrektur mit `\varphi(p^k/X)` explizit aus.

Damit liegt keine vollständig unerkannte Fehlannahme vor, sondern eine **interne Inkonsistenz** zwischen §148.2 und §148.6: Der richtige Primpotenzen-Overhead wird später benannt, die falsche §148.2-Identität aber nicht zurückgezogen.

Die unabhängige Rechnung bleibt:

\[
\varphi(p/X)\quad\Longrightarrow\quad p^{-s}
\]
und daher
\[
\sum_{p,k\ge1}\log p\,p^{-k\beta-s},
\]
während
\[
-\frac{\zeta'}{\zeta}(\beta+s)=\sum_{p,k\ge1}\log p\,p^{-k\beta-ks}.
\]

Die korrekte direkte Mellin-Realisierung von `-\zeta'/\zeta(\beta+s)` gehört zur von-Mangoldt-Summe mit Cutoff `\varphi(p^k/X)`.

### Bindende Korrektur zu §4.4 des Eröffnungsankers

Die Aussage des Eröffnungsdokuments ist ab jetzt so zu lesen:

> **NEU-148 §148.6 benennt den Cutoff-Unterschied selbst; die interne Inkonsistenz mit der in §148.2 positiv markierten Mellinidentität bleibt jedoch unaufgelöst.** NEU-149 repariert den separaten Polfehler von `\widehat\varphi` bei `s=0`, nicht diese Ausgangsidentität. NEU-150s Finite-Part-Hochstufung bleibt deshalb Gegenstand von H-T5.

Dies ändert **nicht** die Prüfstrategie: H-T5 bleibt `TARGETED-REAUDIT`.

## Endurteil

\[
\boxed{\text{P08 PASS-A ERÖFFNUNG BESTÄTIGT — ein lokaler Präzisierungsbefund zu §4.4 gebunden.}}
\]

Kein weiterer Gegenbefund gegen Scope, Inventar, Provenienz oder Paketierung.