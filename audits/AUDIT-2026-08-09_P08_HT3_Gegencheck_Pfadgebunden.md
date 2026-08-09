# P08 Pass A — H-T3 Gegencheck

**Datum:** 9. August 2026
**Scope:** NEU-127, NEU-128A, NEU-128b, NEU-130, NEU-131

## Endurteil

Der unabhängige Gegencheck ist nützlich, aber nicht unverändert übernehmbar.

### Bestätigt

- NEU-127 ist Triage, keine fertige W_N-Konstruktion.
- Der historische Begriff „Rang-1-Projektor“ ist mit P05 zu korrigieren.
- NEU-128b trennt Self-Energy und Prä-Lanczos-Metrik sinnvoll.
- Ein festes reelles beta_0>0 ist für eine positive feste Metrik nötig.
- NEU-130 ist nur Methodenanalogie.

### Korrekturen

1. **NEU-127:** Nur b_{1,N}->0 ist streng gesichert. Die asymptotische Divergenz b_{2,N}/b_{1,N}->infinity bleibt nach H-T2 offen; es gibt finite numerische Evidenz.

2. **P05-Scope:** Rang <=1 ist nur für die induzierte relative Modellrealisierung C_p^rel eingefroren. Die Aussage darf nicht automatisch auf den historischen vollen Kanaloperator C_p übertragen werden. Damit sind NEU-128A und NEU-128b an dieser Stelle modellrelativ/konditional.

3. **NEU-128b Typfehler:** Die Formel Sigma_N(beta)x = sum_p w_p |<Psi_p,x>|^2 ist falsch getypt: links Vektor, rechts Skalar. Korrekt ist entweder die Operatorform sum_p w_p Psi_p<Psi_p,x> oder die Quadratform <x,Sigma_Nx> = sum_p w_p |<Psi_p,x>|^2.

4. **NEU-130:** „strukturell äquivalent“ wird nur als Heuristik gelesen. Die historische Identität D_rel = closure(iJ^-) ist durch P06 nicht als Operatoridentität eingefroren; D_rel wird dort separat als Transportgenerator typisiert.

5. **NEU-131 / Paper VII:** Der Live-Quelltext hat einen Skalierungsfehler: Aus B-strong P_kl <= C c^(1/2) und A_ij:=P_ij c^(1/2) folgt A_ij=O(c), nicht O(1). Außerdem folgt aus oszillatorischer Cancellation keine absolute Schur-Zeilensumme. Gegenbeispiel T_ij=e^{i alpha(i-j)}/|i-j|: signierte Blocksummen cancellieren, aber sum_j |T_ij| ~ log N. Der konkrete Schur-/Nelson-Übergang ist daher nicht bewiesen.

## Schluss

H-T3 benötigt einen kanonischen Endaudit mit diesen superseding Korrekturen. Die qualitative Suchidee einer intrinsischen positiven nichtskalaren Prä-Lanczos-Geometrie bleibt offen.