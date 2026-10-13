"""Standalone manifest and rational replay; no numerical libraries needed."""
from pathlib import Path
import hashlib,json
from audit_directional import audit
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_bytes())
for name,digest in manifest['files'].items():
 p=(root/name).resolve();assert p.is_relative_to(root)
 assert hashlib.sha256(p.read_bytes()).hexdigest()==digest,name
result=audit();assert result==json.loads((root/'AUDIT.json').read_bytes())
print('PASS',len(manifest['files']),'manifest bindings; rational directional bridges and comparison obstruction')
print('NEGATIVE_ACTUAL_SCHUR_WITNESS=false; FULL_REMAINDER_CERTIFIED=false')
