"""Verify an already safely extracted incoming archive without running its programs."""
from pathlib import Path
import hashlib,json
B=Path(__file__).resolve().parent;R=B/'received'
seen=set()
for line in (R/'SHA256SUMS.txt').read_text().splitlines():
 want,rel=line.split('  ',1);p=R/rel
 assert not Path(rel).is_absolute() and p.resolve().is_relative_to(R.resolve())
 assert rel not in seen and p.is_file() and not p.is_symlink()
 assert hashlib.sha256(p.read_bytes()).hexdigest()==want,rel
 seen.add(rel)
actual={str(p.relative_to(R))for p in R.rglob('*') if p.is_file()}
assert seen==actual-{'SHA256SUMS.txt'}
out={'internal_hashes_verified':len(seen),'exact_coverage_except_manifest':True}
(B/'archive-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
