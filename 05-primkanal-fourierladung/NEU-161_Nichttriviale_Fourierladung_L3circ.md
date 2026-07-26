# NEU-161 — Nichttriviale Fourierladung von $L_3^\circ$

**Status:** offen (Quellenprüfung abgeschlossen, Engpass lokalisiert)  
**Abhängigkeiten:** NEU-159, NEU-44, NEU-160  
**Ziel:** Existenz eines expliziten geladenen Fourierkoeffizienten $\ell_{s_0,m_0} \neq 0$ mit $s_0 \neq 0$, sowie strikte Trennung der Folgerungsketten für $T_p^{\mathrm{rel}}(e_{u_0}V_p)\neq0$, $Q_p\neq0$ und $c_p\neq0$.

---

## 161.A — Quellenprüfung: Herkunft und logischer Status von $L_3^\circ$

### Quellblatt

Früheste relevante Definition und Berechnung: **NEU-42 §10** (*Fourier-geladene Primhebung und Padé-/Laplace-Realisierung von $p^{-s}$*, 28. Juni 2026, `werkzeuge/neu42_x3_fourierhebung_laplace_p_minus_s.md`).

### Prüfprotokoll — Befunde

| Prüffrage | Befund aus NEU-42 §10 |
|---|---|
| Wo erscheint $L_3^\circ$ erstmals? | NEU-42 §10; wird auch in §6 referenziert |
| Objekttyp | **Typ 2** — parametrisierte Familie $L_3^\circ = \ell_{s,m}e_sV_m$; kein konstruktiv fixierter Vektor |
| Formel für $\ell_{s,m}$? | Nicht explizit angegeben. §10 rechnet mit einem einzigen Paar $(s,m)$ und setzt $s\neq 0$ direkt voraus |
| Geladener Modus vorgeschrieben? | Nein — $s\neq 0$ ist Eingangsvoraussetzung der Rechnung, kein Ergebnis |
| Symmetrien, die $s\neq 0$ ausschließen? | Keine sichtbar |
| Relative Kantenvektoren frei oder quotientiert? | Quotientiert: $\Pi_{J,N}(e_{u+ps}V_{pm})$ durch Jacobi-Projektion |

### Zusätzlicher Befund aus §6

NEU-42 §6 stellt selbst fest: $L_3^\circ$ muss entweder auf $m=1$ projizieren *oder* relativ normalisiert werden, damit $h(pm)=\log p+\log m$ den reinen $\log p$-Beitrag isoliert. Diese Frage ist in NEU-42 unbeantwortet und gehört zur Zulässigkeitsbedingung $e_{u_0}V_p \in \mathcal{E}_p^{\mathrm{lin,ch}}$ aus 161.D.

### Ausgangsbefund

$$\boxed{?[O]: \text{Die Nichttrivialität der Fourierladung ist im Quellblatt (NEU-42) nur vorausgesetzt.}}$$

$L_3^\circ$ erscheint als formales $\sum_{s,m}\ell_{s,m}e_sV_m$ mit der Bedingung $s\neq 0$ als Rechenbedingung, nicht als bewiesene Eigenschaft. Der Engpass liegt damit in der Konstruktion von $L_3^\circ$ selbst, nicht in der Projektion oder Quotientengeometrie.

**Epistemischer Stand:** abgeschlossen. Befund: $?[O]$.

---

## 161.B — Echter Verzweigungsknoten: Fourierladung vorhanden oder nicht?

**Warnung:** Dies ist kein Vorlemma, sondern ein echter Verzweigungsknoten des Programms.

Aufgrund von 161.A gilt derzeit der dritte Ausgang:

$$\boxed{\text{Die Nichttrivialität der Fourierladung ist eine bisher unbewiesene Eingangsannahme.}}$$

Nur in den Fällen $\checkmark[M]$ und $\checkmark[M]_{\exists\text{-Wahl}}$ beginnt die Zeugenroute. Für den Übergang dorthin muss das Quellblatt ergänzt werden (siehe 161.B.Ausblick).

### Ast 1 — Nichttriviale Fourierladung ($\checkmark[M]$ oder $\checkmark[M]_{\exists\text{-Wahl}}$)

$\exists\, s_0 \neq 0,\ m_0$ mit $\ell_{s_0,m_0} \neq 0$. Zeugenroute beginnt (weiter zu 161.C–E).

### Ast 2 — Vollständige Nullladung ($\checkmark[M]_{\mathrm{deg}}$)

$\ell_{s,m} = 0$ für alle $s \neq 0$. Dann: $T_p^{\mathrm{rel}}(e_u V_p) = 0$ für alle geladenen Eingangvektoren. Strukturelle Degeneration des Kopplungsmechanismus.

### 161.B.Ausblick — Nächste Aufgabe

Das Quellblatt NEU-42 muss durch ein neues Blatt ergänzt werden, das eine der folgenden Leistungen erbringt:
- Konstruktive Festlegung eines expliziten $\ell_{s_0,m_0}\neq 0$ mit $s_0\neq 0$ (Marker $\checkmark[M]$), oder
- Nachweis einer zulässigen Wahl $L_3^\circ = e_{s_0}V_{m_0}$ mit $s_0\neq 0$ und Kompatibilitätsprüfung (Marker $\checkmark[M]_{\exists\text{-Wahl}}$).

**Epistemischer Stand:** offen — aktiver Engpass.

---

## 161.C — Expliziter Koeffizient

**Voraussetzung:** Ast 1 aus 161.B (noch nicht erreicht).

Aufgabe: Finde ein explizites Paar $(s_0, m_0)$ mit $\ell_{s_0,m_0} \neq 0$, $s_0 \neq 0$.

Ein einziger solcher Koeffizient genügt für die Zeugenroute. Er genügt nicht automatisch für $c_p\neq 0$ (siehe 161.E.3).

**Epistemischer Stand:** gesperrt bis 161.B abgeschlossen.

---

## 161.D — Minimaler relativer Zeuge

**Voraussetzung:** $(s_0, m_0)$ aus 161.C.

**Konstruktion:** Wähle $r_* \in \{1, \ldots, N_{\mathrm{Jac}}\}$ und setze $u_0 := r_* - p s_0$.

Gesondert zu prüfen (alle notwendig):
$$e_{u_0} V_p \in \mathcal{E}_p^{\mathrm{lin,ch}}$$
*(Hinweis: NEU-42 §6 zeigt, dass die $m$-Bedingung hier nicht automatisch erfüllt ist.)*

**Bedingung 1 — Skalarnichtverschwindung:**
$$-u_0 s_0 \log p \cdot \ell_{s_0, m_0} \neq 0 \qquad (u_0 \neq 0\text{ erforderlich}).$$

**Bedingung 2 — Nichtverschwindung des Zielbasisvektors:**
$$E^{\mathrm{rel}}_{r_*,\, m_0 \to pm_0} \neq 0.$$

**Bedingung 3 — Separation (Variante B bevorzugt):**

Die Separationsbedingung:
$$E^{\mathrm{rel}}_{r_*;\,m_0\to pm_0} \notin \overline{\operatorname{span}}\left\{E^{\mathrm{rel}}_{u_0+ps;\,m\to pm} : (s,m)\neq(s_0,m_0)\right\}.$$

*Variante B (duales Funktional, bevorzugt):*
$$\exists\, \varphi_{\rho_*} \in (H_p^{\mathrm{rel}})^*: \quad
\varphi_{\rho_*}\!\left(E^{\mathrm{rel}}_{r_*;\,m_0\to pm_0}\right) \neq 0, \quad
\varphi_{\rho_*}\!\left(E^{\mathrm{rel}}_{u_0+ps;\,m\to pm}\right) = 0 \text{ für }(s,m)\neq(s_0,m_0).$$

Im Hilbertraumfall: $h_* \in \left(\overline{\operatorname{span}}\{\ldots\}\right)^\perp$ mit $\langle E^{\mathrm{rel}}_{r_*;\ldots}, h_*\rangle \neq 0$.

*Idealfall (orthogonale Familie):* Koordinatenfunktional
$\varphi_{\rho_*}(x) = \langle x, E^{\mathrm{rel}}_{r_*;\,m_0\to pm_0}\rangle / \|E^{\mathrm{rel}}_{r_*;\,m_0\to pm_0}\|^2$;
Bedingungen 2 und 3 kollabieren zu $E^{\mathrm{rel}}_{r_*;\ldots}\neq 0$ und $E^{\mathrm{rel}}_{r_*;\ldots}\perp E^{\mathrm{rel}}_{u_0+ps;\ldots}$.

**Konvergenzbedingung** (bei unendlicher Summe und stetigem $\varphi_{\rho_*}$):
$$\sum_{s,m}|c_{s,m}|^2\|E_{s,m}^{\mathrm{rel}}\|^2 < \infty, \qquad T_p^{\mathrm{rel}}(e_{u_0}V_p) = \sum_{s,m}c_{s,m}E_{s,m}^{\mathrm{rel}} \in H_p^{\mathrm{rel}}.$$
Bei endlicher Summe oder bereits definiertem Hilbertraumvektor entfällt dieser Punkt.

**Zentrale Rechnung:**
$$\varphi_{\rho_*}\!\left(T_p^{\mathrm{rel}}(e_{u_0}V_p)\right)
= -u_0 s_0 \log p \cdot \ell_{s_0,m_0} \cdot \varphi_{\rho_*}\!\left(E^{\mathrm{rel}}_{r_*;\,m_0\to pm_0}\right) \neq 0
\quad\Longrightarrow\quad T_p^{\mathrm{rel}}(e_{u_0}V_p)\neq 0.$$

**Epistemischer Stand:** gesperrt bis 161.C abgeschlossen.

---

## 161.E — Getrennte Folgerungen: $Q_p^{\mathrm{rel}}$, $Q_p$, $c_p$

### 161.E.1 — $Q_p^{\mathrm{rel}} \neq 0$

$$T_p^{\mathrm{rel}} : \mathcal{E}_p^{\mathrm{lin,ch}} \to H_p^{\mathrm{rel}}, \quad N_p^{\mathrm{rel}} := \ker T_p^{\mathrm{rel}} \cap \mathcal{E}_p^{\mathrm{lin,ch}}, \quad Q_p^{\mathrm{rel,raw}} := \mathcal{E}_p^{\mathrm{lin,ch}}/N_p^{\mathrm{rel}}.$$
$$Q_p^{\mathrm{rel}} \neq 0 \iff T_p^{\mathrm{rel}}(\mathcal{E}_p^{\mathrm{lin,ch}}) \neq \{0\}.$$
Zeuge aus 161.D liefert das direkt. **Status:** gesperrt bis 161.D.

### 161.E.2 — $Q_p \neq 0$

Eigene Projektionsfrage: $\pi_{\mathrm{Jac}}(T_p^{\mathrm{rel}}(e_{u_0}V_p)) \neq 0$. **Status:** offen, nicht durch 161.D abgedeckt.

### 161.E.3 — $c_p \neq 0$ (NEU-44-Route)

$$\ell_{s_0,m_0}\neq0 \;+\; a_{p,u_0}\neq0 \;+\; \text{Kollisionskontrolle} \;\Longrightarrow\; c_p\neq0.$$
**Status:** offen, erfordert Rückbindung an NEU-44.

---

## Vollständige Implikationskette

**Zeugenpfad:**
```
161.A: NEU-42 §10  →  Befund ?[O]: Nichttrivialität nur vorausgesetzt
  │
  └─► 161.B.Ausblick: Quellblatt ergänzen
        ├─ checkmark[M]_deg: strukturelle Nullladung  →  Degeneration
        └─ checkmark[M] oder checkmark[M]_{exists-Wahl}
              └─► 161.C: explizites Paar (s0, m0)
                    └─► 161.D: u0=r*-ps0; Bed. 1-3; Konvergenz; Zulässigkeit
                          └─► phi(T_p^rel(e_{u0}Vp)) ≠ 0
                                ├─► 161.E.1: Q_p^rel ≠ 0  [direkt]
                                ├─► 161.E.2: Q_p ≠ 0      [Projektionsüberleben]
                                └─► Symmetrietripel pi_p → Irreduzibilität
```

**NEU-44-Route (separat):**
```
ell_{s0,m0}≠0  +  a_{p,u0}≠0  +  Kollisionskontrolle  ⟹  c_p ≠ 0
```

**Epistemische DAG-Regel:** Hilbert–Pólya-orientierte Aussagen werden erst dann als Befunde gezählt, wenn die jeweiligen NEU-Knoten die vollständigen Hypothesen schließen. Das Programm ist so architektoniert, dass diese Eigenschaften geprüft werden können — nicht, dass es sie bereits besitzt.
