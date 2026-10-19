"""Bound-input, full map and deterministic-seed search replay (not a proof)."""
import hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
from fractions import Fraction
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PACKAGE=HERE.parent/'nstar-jp-spike-orthogonality-2026-10-16'
def main():
 for rel,digest in json.loads((HERE/'MANIFEST.json').read_text()).items():
  assert hashlib.sha256((HERE/rel).read_bytes()).hexdigest()==digest,rel
 bind=json.loads((HERE/'INPUT_BINDINGS.json').read_text())
 for rel,digest in bind['archive_sha256'].items():
  assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==digest,rel
 with tempfile.TemporaryDirectory(prefix='objekt-x-shell-search-') as td:
  td=Path(td);inputs=td/'inputs';out=td/'out'
  subprocess.run([sys.executable,'-B',str(PACKAGE/'stufe5/prepare_inputs.py'),str(inputs)],check=True)
  env=dict(os.environ,OBJEKT_X_STAGE5_INPUTS=str(inputs),OBJEKT_X_SEARCH_OUTPUT=str(out))
  for resolution in (384,512):
   jobs=[subprocess.Popen([sys.executable,'-B',str(HERE/'build_data.py'),p,str(resolution)],env=env) for p in ('even','odd')]
   assert all(p.wait()==0 for p in jobs)
   for par in ('even','odd'):
    name=f'MAPS_{par}_{resolution}.json'
    assert (out/name).read_bytes()==(HERE/'data'/name).read_bytes(),name
  jobs=[subprocess.Popen([sys.executable,'-B',str(HERE/'search.py'),p],env=env)for p in ('even','odd')]
  assert all(p.wait()==0 for p in jobs)
  for par in ('even','odd'):
   got=json.loads((out/f'SEARCH_{par}.json').read_text());ref=json.loads((HERE/'data'/f'SEARCH_{par}.json').read_text())
   assert abs(got['best']['margin_diagnostic']-ref['best']['margin_diagnostic'])<1e-7
   assert np.linalg.norm(np.array(got['best']['coefficients'])-ref['best']['coefficients'])<1e-5
   frozen=json.loads((HERE/'data'/f'FROZEN_{par}.json').read_text())
   assert frozen['selection_file_sha256']==hashlib.sha256((HERE/'data'/f'SEARCH_{par}.json').read_bytes()).hexdigest()
   expected=[str(Fraction(format(x,'.25g')))for x in ref['best']['coefficients']]
   assert frozen['raw_exact_rational_coefficients']==expected
   # Audits use the originally frozen direction, never a slightly changed optimizer result.
   (out/f'FROZEN_{par}.json').write_bytes((HERE/'data'/f'FROZEN_{par}.json').read_bytes())
  subprocess.run([sys.executable,'-B',str(HERE/'audit_source.py')],env=env,check=True)
  assert (out/'SOURCE_AUDIT.json').read_bytes()==(HERE/'data'/'SOURCE_AUDIT.json').read_bytes()
 print('PASS: four maps byte-identical; seeded search reproduced within declared optimizer tolerances; source audit byte-identical. Exploratory only.')
if __name__=='__main__':main()
