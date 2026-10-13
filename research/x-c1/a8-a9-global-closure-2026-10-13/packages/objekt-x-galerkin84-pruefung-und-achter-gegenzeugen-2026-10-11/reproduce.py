"""Standard-library replay of the standalone exact obstruction certificate."""
from pathlib import Path
import hashlib,json
from check_bridge_obstruction import replay

root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_bytes())
for name,digest in manifest['files'].items():
    path=(root/name).resolve()
    assert path.is_relative_to(root)
    assert hashlib.sha256(path.read_bytes()).hexdigest()==digest,name
data=json.loads((root/'BRIDGE_OBSTRUCTION_INPUT.json').read_bytes())
result=replay(data)
assert result==json.loads((root/'BRIDGE_OBSTRUCTION.json').read_bytes())
print('PASS',len(manifest['files']),'manifest bindings; two exact bridge obstructions')
print('PROPOSED_UNIFORM_Q8_BRIDGES_REFUTED=true')
print('NEGATIVE_ACTUAL_SCHUR_WITNESS=false')
print('FULL_REMAINDER_CERTIFIED=false')
