from pathlib import Path
import shutil,json
B=Path(__file__).resolve().parent;R=B/'received';W=B/'work';A=B.parent
for p in [W/'pairing-check',W/'pairing-refinement',W/'research-review']:p.mkdir(exist_ok=True)
for dst,src in [(W/'repo',A/'repo'),(W/'pairing-check/snapshot',A/'repo'),(W/'pairing-check/deps',A/'python09'),(W/'research-review/data',A/'repo/research/x-c1/w9-residual-centered-control-even-2026-10-21/whole')]:
 if not dst.exists():dst.symlink_to(src.resolve(),target_is_directory=True)
bootstrap=(R/'Neuberechnung/pairing-check/run_pairs.py').read_text().replace("ROOT=BASE/'snapshot'","ROOT=(BASE/'snapshot').resolve()")
(W/'pairing-check/run_pairs.py').write_text(bootstrap)
for name in ['kernel_orientation.py','add_panels.py','validate_orientation.py']:
 shutil.copyfile(R/'Neuberechnung/pairing-refinement'/name,W/'pairing-refinement'/name)
for name in ['localized-81.json','kernel-orientation-81.json']:
 shutil.copyfile(R/'Pruefdaten'/name,W/'pairing-refinement'/name)
code=(R/'Neuberechnung/pairing-refinement/core_tail.py').read_text()
needle="hh=tm.hjet(ns,xx);h0=hh.s[0]"
replacement='''# Independent audit amendment: polynomial bounds must use the same Cauchy
# radius as the tail estimate. Original peval is hard-coded to radius 2.
original_hh=tm.hjet(ns,xx)
original_remainder=abs(original_hh.b).upper()*R**(-8)/(1-1/R)
def peval_radius(p,x):
 x=tm.jet(x);assert x.s.length()<=2
 co=p(arb_poly([x.s[0],x.s[1]]))
 bound=arb_poly([abs(v).upper() for v in co])(R).upper()
 return tm.Jet(arb_series(list(co)[:tm.Jet.N],prec=tm.Jet.N),acb(arb(0,bound),arb(0,bound)))
tm.peval=peval_radius
hh=tm.hjet(ns,xx);h0=hh.s[0]
contour_review={'normalized_radius':enc(R),'original_contour_bound':enc(abs(original_hh.b).upper()),'corrected_contour_bound':enc(abs(hh.b).upper()),'original_cauchy_remainder':enc(original_remainder),'corrected_cauchy_remainder':enc(abs(hh.b).upper()*R**(-8)/(1-1/R))}
(TASK/'contour-review.json').write_text(json.dumps(contour_review,indent=2)+'\\n')
print('CONTOUR_REVIEW', {k:float(box(v).upper()) for k,v in contour_review.items()},flush=True)'''
assert code.count(needle)==1
(W/'pairing-refinement/core_tail_review.py').write_text(code.replace(needle,replacement))
(B/'PLAN.txt').write_text('''Gezielte unabhängige Prüfung des GPT-2-Reparaturarchivs, 2026-10-22.
1. Interne Hashes, Quellenbindungen, bestehende 65 und neue 16 Abschnitte prüfen.
2. Rationale Abnahme aus unveränderten Eingangsdaten wiederholen.
3. Alle 84 Kernkorrekturen gegen unseren vorherigen unabhängigen Rechenweg prüfen.
4. Alle 16 neuen Taylor-Abschnitte erneut aus dem gebundenen Modell berechnen.
5. Neue h-Randkorrektur nach Anpassung der Polynom-Konturhülle an ihren tatsächlichen Radius erneut berechnen. Originalarchiv unverändert lassen.
6. Alle 84 endgültigen Differenzen samt Fehlerhülle erneut prüfen; keine geerbten analytischen Voraussetzungen als neu bewiesen ausgeben.
Kein Push, Merge, Branchwechsel oder Eingriff in eingefrorene Repositorydateien.
''')
print('Review scripts prepared',W)
