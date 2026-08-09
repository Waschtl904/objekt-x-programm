# P08 Pass A — H-T5 Gegencheck, pfadgebunden

**Datum:** 9. August 2026  
**Scope:** externer H-T5-Entwurf gegen Live-Dateien NEU-146–150.  
**Status:** Gegencheck, nicht kanonischer Endaudit.

## Gesamturteil

Der externe Entwurf trifft mehrere Firewalls aus H-T4 richtig, stuft aber NEU-147/148/149/150 zu hoch ein. Insbesondere ist die zentrale Mellin-Identität von NEU-148 im Live-Stand falsch typisiert.

## 1. NEU-146

Erhalten:
- Schichtzerlegung
  `S_X(beta)=sum_{k>=1} sum_{p<=X} log p p^{-k beta}`.
- PNT-Hauptterm für `Re(k beta)<1`.
- Trennung R-Cutoff vs. Primcutoff und Offenheit von [ZA].

Korrekturen:
- Die Operatorausgangsformel bleibt conditional auf intrinsisches T2 und `c_p != 0`.
- Am Rand `Re(k beta)=1`, `k beta !=1` liegt ein oszillierender Nichtgrenzwert vor; NEU-147 korrigiert dies.
- Die Formulierung „für `k beta in Z` logarithmische Divergenz“ ist falsch; logarithmisch ist der Sonderfall `k beta=1`.

## 2. NEU-147

Die Randfallkorrektur in §147.1 ist richtig.

Der anschließende direkte Import der expliziten Formel ist jedoch nicht gerechtfertigt: `T_k(X,beta)` ist eine **Primzahl-Summe** über `theta(X)=sum_{p<=X} log p`, während die zitierte explizite Formel `psi(X)=sum_{p^j<=X} log p` betrifft. Der Übergang verlangt Möbius-/Primpotenzkorrekturen. Schematisch entstehen dadurch auch Beiträge `X^{rho/j-k beta}`; der Defekt ist nicht bereits exakt nur `X^{rho-k beta}`.

Weiterer lokaler Fehler: Für `Re beta>0` können triviale Nullstellen `-2n` niemals `Re(-2n-k beta)>=0` erfüllen.

Die RH-Idee für `1/2<Re beta<1` bleibt als Richtungsstruktur interessant, aber der angegebene Äquivalenzbeweis ist nicht vollständig.

## 3. NEU-148 — zentraler Fehler

Live definiert

`S_{phi,X}(beta)=sum_p phi(p/X) log p p^{-beta}/(1-p^{-beta})`.

Mellin-Inversion von `phi(p/X)` liefert den inneren Faktor

`sum_{p,k>=1} log p p^{-k beta-s}`,

nicht

`sum_{p,k>=1} log p p^{-k(beta+s)}=-zeta'/zeta(beta+s)`.

Damit ist Satz 148.A in der vorliegenden Form `×[M]`. Die korrekte Zeta-Mellin-Identität gehört zur Mangoldt-Summe

`Psi_{phi,X}(beta)=sum_{p,k>=1} log p phi(p^k/X) p^{-k beta}`.

Zusätzlich ist bei `phi=1` nahe 0 die Mellintransformierte nicht ganz; sie besitzt bei `s=0` einen einfachen Pol mit Residuum 1. NEU-149 korrigiert genau diesen Punkt.

§148.6 enthält ebenfalls eine algebraisch falsche Differenzformel. Richtig ist

`Psi-S = sum_{k>=2,p} log p [phi(p^k/X)-phi(p/X)] p^{-k beta}`.

Für `Re beta>1/2` ist eine asymptotische Übertragung wegen absolut summierbarer höheren Primpotenzen plausibel, aber separat zu beweisen.

## 4. NEU-149

Positiv: Die Korrektur `Res_{s=0} hat phi(s)=1` statt `hat phi(0)=1` ist richtig.

Aber NEU-149 kann nur die **korrigierte Mangoldt-Mellin-Kette** stützen; es repariert nicht rückwirkend Satz 148.A für `S`.

Weitere Präzisierung: Für variierendes `beta in K` ist die Menge `{omega-beta}` nicht diskret, weil `K` ein Kontinuum ist. Eine einheitliche nullstellenvermeidende Kontur und ein uniformer Abstand zu allen bewegten Polen müssen konstruktiv bewiesen oder beta-abhängig formuliert werden. Der Restabschätzungsschritt ist daher conditional.

## 5. NEU-150

Die algebraische Primlabel-Spuridentität ist nur conditional auf T2, Nichtentartung und eine saubere Definition von `N_P`.

Die angegebene Domäne

`sum p^2 |xi_p|^2 < infinity`

ist für eine nicht normierte orthogonale Familie unvollständig; natürlich erscheint `||Psi_p||^2`. Außerdem muss das orthogonale Komplement und die maximale selbstadjungierte Multiplikationsdomäne angegeben werden.

Die Hochstufungen 150.C/150.D sind nicht haltbar, weil sie die falsche NEU-148-Identität importieren. Auch [ZA] `R_p asymp p/log p` allein reicht nicht, um Finite Parts zweier unterschiedlicher Cutoff-Skalen automatisch zu identifizieren; hierfür ist eine quantitativ präzisere Cutoff-Transferkontrolle nötig.

## Endurteil des Gegenchecks

Der externe H-T5-Entwurf ist als Triage nützlich, aber die Aussagen
- „NEU-148 Mellin-Darstellung korrekt“,
- „phi-Fehler im Live-Stand nicht vorhanden“,
- „NEU-149 schließt die Restkontrolle für S“,
- „NEU-150 realisiert die regulierte Spur operatoriell“

sind im Live-Stand nicht tragfähig.

Bindender Endstatus folgt im kanonischen H-T5-Audit.