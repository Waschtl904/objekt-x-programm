> [!WARNING]
> **HISTORICAL SNAPSHOT — nur die operative Navigation ist ersetzt.**
>
> As of: 2026-09-19
> Nicht zur Bestimmung der aktuellen Forschungsfront verwenden.
> Kanonischer Status: [RESEARCH_STATE.yaml](RESEARCH_STATE.yaml).
> Lesbarer Einstieg: [CURRENT_STATE.md](CURRENT_STATE.md).
> Der folgende Originalinhalt bleibt als Provenienz unverändert erhalten.
> Mathematische Inhalte werden durch diesen Hinweis nicht pauschal verworfen.

# Objekt-X-Programm — Repository-Karte

> **Operativer Hinweis (19. September 2026):** Für die aktuelle Shell-Schur-Fortsetzung und ihre genaue Stellung auf dem Weg zu Objekt X zuerst die
> [Transportleiter zu Objekt X](TRANSPORT_ZU_OBJEKT_X_LEITER_2026-09-19.md) lesen.
> Der aktuelle Forschungs-Head schließt den unendlichen geraden A-Gauge-High-Tail auf `0<h<=10^-20`, aber noch nicht den endlichen Low-Block, die Mischblöcke oder den Odd-Sektor.
>
> Für die ältere kanonische Gesamtorganisation außerdem
> [CURRENT-FRONT](../CURRENT-FRONT.md),
> [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md),
> [AKTUELLER_STAND](AKTUELLER_STAND.md),
> [DAG](DAG.md) und die
> [Forschungsroadmap 2026-09-03](FORSCHUNGS_ROADMAP_2026-09-03.md) konsultieren.
>
> Die darunterstehende Repository-/Syntheseorganisation ist teilweise historisch
> (Grundstruktur vom 8. August 2026). Historische Navigationsfassungen werden unter
> [archiv/](archiv/) erhalten.

---

## Aktuelle Forschungsleiter

| Stufe | Stand |
|---|---|
| Endpunkt `B=log(5)/2` | positiv geschlossen auf `main` |
| lokaler Even-All-Source-Transport | geschlossen für `h<=2^(-10^16)` |
| Even-WIDTH-AMPLIFICATION | unendlicher High-Tail geschlossen für `h<=10^-20`; Low- und Mischblöcke offen |
| Odd-Fortsetzung | offen |
| Strong Terminal | offen und von der lokalen Shell-Schur-Fortsetzung zu unterscheiden |
| full C1-GEOM / Objekt X / RH | offen |

Die vollständige Status- und Abhängigkeitsleiter steht in
[TRANSPORT_ZU_OBJEKT_X_LEITER_2026-09-19.md](TRANSPORT_ZU_OBJEKT_X_LEITER_2026-09-19.md).

---

## Drei Reifestufen

| Stufe | Ort | Charakter |
|---|---|---|
| **NEU-Knoten** (atomare Forschung) | `active/` und `archive-nodes/` | Darf Fehler, No-Gos, Patches, Statuswechsel enthalten. Laborbuch. |
| **SYN-/P-Manuskripte** (konsolidiert) | `papers/` | Nur aktuell gültiger mathematischer Stand. Alle Definitionen konsolidiert. LaTeX. |
| **Publikationspaper** | `papers/` (markiert `PUB`) | Nur wenn Aussage stark genug für Einreichung. |

---

## Repo-Struktur

```
objekt-x-programm/
├── 00-uebersicht/
│   ├── README.md          ← diese Datei
│   ├── TRANSPORT_ZU_OBJEKT_X_LEITER_2026-09-19.md
│   ├── AKTUELLER_STAND.md ← ältere Gesamtübersicht
│   └── DAG.md             ← Abhängigkeitsgraph
├── papers/
│   ├── README_papers.md   ← Manuskript-Index
│   ├── P01_BC_Prime_Power_Weights.tex
│   ├── P02_Adelic_Weil_Amplitude_Port.tex
│   ├── P03_Haar_L2_Firewall.tex
│   └── P04_Finite_Weil_Geometry.tex
├── active/
│   ├── NEU-260b_Theta-Selektionsaudit.md
│   ├── NEU-260c_Grenznormalisierung.md   (offen)
│   └── NEU-260d_Jab-Geometrie.md         (offen)
└── archive-nodes/
    ├── 00-grundlegung/
    ├── 01-primkanten-werkzeuge/
    ├── ...
    └── 07-weil-explizitformel/   ← NEU-250 bis NEU-260a
```

---

## Tages-Workflow

1. **Neue Mathematik:** `active/NEU-XXX` oder ein klar abgegrenztes reproduzierbares Forschungspaket anlegen.
2. **Abgeschlossener Block:** Block in `papers/PXX` verdichten; Knoten nach `archive-nodes/` verschieben.
3. **Audit:** Immer gegen die kanonischen Beweisartefakte auditieren; für Provenienz die gebundenen Pakete konsultieren.
4. **Statuspromotion:** Checker-PASS, CI, Merge und Prüfsummen allein erzeugen keine mathematische Statuspromotion.

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm.*
