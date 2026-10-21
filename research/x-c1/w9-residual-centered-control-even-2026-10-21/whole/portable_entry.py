"""One explicit path-only relocation for the immutable historical builder."""
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
source=HERE/sys.argv[1]
raw=source.read_text(encoding='utf-8')
old="Path('C:/Users/sebas/Documents/Codex/2026-10-09/github-plugin-github-openai-curated-remote/work/tail-probe-2026-10-10/vendor/log_integrals.py')"
new='Path('+repr(str(HERE/'vendor/log_integrals.py'))+')'
assert raw.count(old)==1 and source.name in ('whole_function_probe.py','whole_function_probe_v2.py')
sys.argv=[str(source),*sys.argv[2:]]
ns={'__name__':'__main__','__file__':str(source)}
exec(compile(raw.replace(old,new),str(source),'exec'),ns)
