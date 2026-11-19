"""Read and package one finished run; never import or execute its mathematics."""
from pathlib import Path
from decimal import Decimal
import json,hashlib,shutil,zipfile

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent.parent
OUT=ROOT/'outputs/Objekt-X-GPT2-108-Bank-Wiederholung-2026-11-19'
assert (HERE/'PROCESS_END.json').exists(),'The authorized process has not finished'
assert not OUT.exists(),'Do not silently overwrite a completed report'
def read(name):return json.loads((HERE/name).read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s):p.write_bytes(s.encode('utf-8'))
process=read('PROCESS_END.json');auth=read('REPEAT_AUTHORIZATION.json');spec=read('START.json')
assert read('single_run/START.json')==spec
assert sha(HERE/'single_measurement.py')==auth['new_script_sha256']==process['script_sha256']
assert sha(HERE/'SINGLE_RUN.log')==process['log_sha256']
bindings=read('RUN_BINDINGS.json')
for e in bindings['files']:
    p=Path(e['path']);assert p.stat().st_size==e['bytes'] and sha(p)==e['sha256'],str(p)
raw=read('single_run/RESULT.json') if (HERE/'single_run/RESULT.json').exists() else None
passed=bool(raw and process['exit_code']==0 and raw['controls_pass'])
failed_conditions=[]
if process['exit_code']!=0:failed_conditions.append('Prozess nicht erfolgreich beendet')
if raw and not passed:
    for key,limit,label in [('first_column_max_component_difference','1e-12','Erstspalte: Komponentenfehler'),('first_column_difference_dual_norm','1e-6','Erstspalte: Abstand in inverser Bankmetrik')]:
        x=Decimal(raw[key])
        if not x.is_finite() or x>=Decimal(limit):failed_conditions.append(label)
    x=Decimal(raw['energy_model_108'])
    if not x.is_finite() or x<=0:failed_conditions.append('Positive Energie nicht bestätigt')
elif not raw:
    failed_conditions.append('Lauf vor vollständiger Ergebnisausgabe abgebrochen; Ursache im Rohprotokoll')
if passed:
    assert Decimal(raw['min_LDL_pivot'])>0 and Decimal(raw['energy_model_108'])>0
    assert Decimal(raw['first_column_max_component_difference'])<Decimal('1e-12')
    assert Decimal(raw['first_column_difference_dual_norm'])<Decimal('1e-6')
    value=raw['energy_model_108']
    if Decimal(value)>Decimal('0.2573'):
        reading='Unter den übernommenen Verträgen liegt der diagnostische Unterwert über 0,2573. Das heutige Eckenverfahren schließt damit für keine erste Schranke. Keine allgemeine Unmöglichkeit und kein Routenstopp.'
    elif Decimal(value)>Decimal('0.04196'):
        reading='Unter den übernommenen Verträgen liegt der diagnostische Unterwert über 0,04196. Das Ziel 0,0417 ist mit der heutigen ersten Schranke diagnostisch nicht erreichbar. Sein Wert unter 0,2573 besagt nicht, dass die tatsächliche zweite Restenergie unter 0,2573 liegt, und bestätigt keine Machbarkeit. Kein Routenstopp.'
    else:
        reading='Der Unterwert liegt höchstens bei 0,04196. Damit ist nichts entschieden; die Pause bleibt.'
else:
    value=None
    reading='Kein freigegebener Ritz-Unterwert. Die Rechnung oder ihre unveränderten Kontrollen wurden nicht erfolgreich abgeschlossen. Keine Schwellenentscheidung, kein Nachjustieren und kein weiterer Lauf.'
summary={
    'date':'2026-11-19','status':'CONDITIONAL_NONRIGOROUS_RITZ_LOWER_VALUE' if passed else 'NO_ACCEPTED_VALUE',
    'authorized_repeat_invocations':1,'ritz_lower_value_108':value,'controls_pass':passed,
    'failed_conditions':failed_conditions,
    'first_column_max_component_difference':raw['first_column_max_component_difference'] if raw else None,
    'first_column_max_component_tolerance_strict':'1e-12',
    'first_column_difference_dual_norm':raw['first_column_difference_dual_norm'] if raw else None,
    'first_column_dual_norm_tolerance_strict':'1e-6',
    'minimum_LDL_pivot':raw['min_LDL_pivot'] if raw else None,
    'linear_equation_residual':raw['linear_solve_max_defect'] if raw else None,
    'linear_residual_is_reported_only_no_extra_acceptance_threshold':True,
    'projection_coefficient_lambda_bar2':raw['projection_coefficient_lambda_bar2'] if raw else None,
    'arithmetic_radius_is_not_total_error':raw['arithmetic_radius_only'] if passed else None,
    'process_elapsed_seconds':process['elapsed_seconds'],'process_exit_code':process['exit_code'],
    'precision_bits':spec['precision_bits'],'maximum_seconds':spec['maximum_seconds'],
    'script_sha256':sha(HERE/'single_measurement.py'),'input_bindings_sha256':sha(HERE/'RUN_BINDINGS.json'),
    'protocol_sha256':sha(HERE/'SINGLE_RUN.log'),
    'interpretation':reading,
    'scope':'Nicht-rigoroser Ritz-Unterwert, bedingt auf übernommene Verträge einschließlich der offenen nativen Herkunft der q-Lösung. Erstspaltenkontrolle ist kein q-Fehlernachweis. Keine obere Schranke der zweiten Restenergie. Kein Routenstopp, kein Zertifikat und keine Repository-Änderung.',
    'static_GPT1_q_vector_acceptance_claimed':False,
    'legacy_raw_script_status_is_not_a_route_decision':True,
    'automatic_retry':False}
OUT.mkdir()
write(OUT/'ERGEBNIS.json',json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
def show(k):return str(summary[k]) if summary[k] is not None else 'nicht abgeschlossen / kein freigegebener Wert'
body=f'''Objekt X – genau ein freigegebener Wiederholungslauf, 19. November 2026

Status: {summary['status']}
Nicht-rigoroser Ritz-Unterwert auf der 108er-Bank: {show('ritz_lower_value_108')}
Alle Akzeptanzbedingungen bestanden: {passed}
Verfehlte Bedingungen: {', '.join(failed_conditions) if failed_conditions else 'keine'}
Maximaler Komponentenfehler: {show('first_column_max_component_difference')} (streng < 1e-12)
Abstand in der inversen Bankmetrik: {show('first_column_difference_dual_norm')} (streng < 1e-6)
Kleinster LDL-Pivot: {show('minimum_LDL_pivot')}
Linearer Gleichungsrest: {show('linear_equation_residual')}
Laufzeit: {process['elapsed_seconds']:.3f} Sekunden
Prozess-Exitcode: {process['exit_code']}

{reading}

Aussagegrenzen
{summary['scope']}
Die statische GPT1-Abnahme der q-Vektor-Definition wird nicht behauptet.
Die im unveränderten Rohskript enthaltenen alten Statusnamen mit
"ROUTE" oder "STOP" werden ausdrücklich nicht als Routenentscheidung
übernommen. Bei gescheiterten Kontrollen sind etwaige interne Rohzahlen
kein freigegebener Messwert. Das Rohprotokoll bleibt unverändert erhalten.

Einzige Änderung gegenüber dem ersten Versuch
Laufgrenze 1800 -> 14400 Sekunden, einschließlich Fehlermeldung und
START-Metadaten. Rückersetzung stellt den alten Skripttext bytegleich her.
Präzision 3328 Bit, Panels, Knoten, Toleranzen und lambda_bar2 unverändert.
START.json wurde vor dem Prozessstart festgehalten; die vom Messskript
vor Beginn seiner Rechnung geschriebene single_run/START.json stimmt überein.

SHA256
Skript: {summary['script_sha256']}
Eingangsmanifest mit Einzelhashes: {summary['input_bindings_sha256']}
Unverändertes Rohprotokoll: {summary['protocol_sha256']}

Paketinhalt
ERGEBNIS.json und diese Datei enthalten die geltende Einordnung.
raw/ enthält unveränderte Rohdaten, soweit der Lauf sie tatsächlich erzeugt hat.
RUN_BINDINGS.json enthält die absoluten Pfade und Hashes der Originaleingaben.
Diese großen Originaleingaben werden nicht aus Berichten rekonstruiert.
Die vollständigen Eingabedateien und installierten Bibliotheken verbleiben
an den gebundenen lokalen Pfaden; das Übergabepaket enthält ihre Hashes.
'''
if not passed and raw is None:
    body+='\nProtokollende:\n'+'\n'.join((HERE/'SINGLE_RUN.log').read_text(encoding='utf-8',errors='replace').splitlines()[-22:])+'\n'
write(OUT/'ERGEBNIS.txt',body)
copies={name:name for name in ['single_measurement.py','START.json','ONLY_CHANGE.diff','REPEAT_AUTHORIZATION.json','RUN_BINDINGS.json','DEPENDENCIES_MANIFEST.json','ASSET_BINDINGS.json','INPUT_IDENTITIES.json','LAUNCH.json','PROCESS_END.json','launch_once.py','package_finished_repeat.py']}
copies['single_run/START.json']='raw/START.json'
copies['SINGLE_RUN.log']='raw/SINGLE_RUN.log'
if raw is not None:copies['single_run/RESULT.json']='raw/RESULT.json'
if (HERE/'single_run/ASSEMBLED_VECTORS.json.gz').exists():copies['single_run/ASSEMBLED_VECTORS.json.gz']='raw/ASSEMBLED_VECTORS.json.gz'
for name in ['common.py','residuals.py','old_fields.py','model_cache.py','historical_pairs.binding.json']:
    copies['assets/'+name]='assets/'+name
for source,target in copies.items():
    dest=OUT/target;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(HERE/source,dest)
manifest=[]
for p in sorted(OUT.rglob('*')):
    if p.is_file():manifest.append({'path':p.relative_to(OUT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
write(OUT/'MANIFEST.json',json.dumps({'files':manifest},indent=2)+'\n')
archive=OUT.with_suffix('.zip')
with zipfile.ZipFile(archive,'w') as z:
    for p in sorted(OUT.rglob('*')):
        if p.is_file():z.write(p,arcname=OUT.name+'/'+p.relative_to(OUT).as_posix(),compress_type=zipfile.ZIP_STORED if p.suffix=='.gz' else zipfile.ZIP_DEFLATED)
delivery={'archive':str(archive),'archive_bytes':archive.stat().st_size,'archive_sha256':sha(archive),'manifest_sha256':sha(OUT/'MANIFEST.json'),'report':str(OUT/'ERGEBNIS.txt'),'summary':summary}
write(OUT.with_suffix('.delivery.json'),json.dumps(delivery,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(delivery,indent=2,ensure_ascii=False))
