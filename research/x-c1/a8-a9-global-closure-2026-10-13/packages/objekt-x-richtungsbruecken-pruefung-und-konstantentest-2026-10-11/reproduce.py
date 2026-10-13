"""Replay the sealed input and the independent rational extension."""
from pathlib import Path
import hashlib,json,subprocess,sys,tempfile,zipfile
from independent_control import control

root=Path(__file__).resolve().parent
files=json.loads((root/'MANIFEST.json').read_bytes())['files']
for rel,digest in files.items():
    p=(root/rel).resolve();assert p.is_relative_to(root)
    assert hashlib.sha256(p.read_bytes()).hexdigest()==digest,rel
archive=root/'inputs/Objekt-X-Richtungsbruecke-und-Vergleichsgrenze-2026-10-11.zip'
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='4faa7004a0622b7434ad0baa35c15f53a165db8d758091bd1f1aa682bb20275d'
with tempfile.TemporaryDirectory(prefix='objekt-x-direction-review-') as name:
    tmp=Path(name)
    with zipfile.ZipFile(archive) as z:
        for entry in z.infolist():
            assert (tmp/entry.filename).resolve().is_relative_to(tmp.resolve())
            assert (entry.external_attr>>16)&0o170000!=0o120000
        z.extractall(tmp)
    inp=tmp/'Objekt-X-Richtungsbruecke-und-Vergleichsgrenze-2026-10-11'
    subprocess.run([sys.executable,'-B','reproduce.py'],cwd=inp,check=True)
    result=control(inp)
    assert result==json.loads((root/'INDEPENDENT_CONTROL.json').read_bytes())
print('PASS: input replay and independent rational control, including full constant bonus')
print('NEGATIVE_ACTUAL_SCHUR_WITNESS=false; FULL_REMAINDER_CERTIFIED=false')
