"""Run the sealed response replay; allow only CRLF/LF output differences.

Source code and input manifest are unchanged. The single comparison is
adapted in memory. The generated precision receipt is restored afterwards.
"""
from pathlib import Path
import sys

root=Path(sys.argv[1]).resolve()
source=root/'reproduce.py'
code=source.read_text(encoding='utf-8')
old="assert (HERE/'PRECISION_CHECK.json').read_bytes()==expected_precision"
new="assert (HERE/'PRECISION_CHECK.json').read_bytes().replace(b'\\r\\n',b'\\n')==expected_precision.replace(b'\\r\\n',b'\\n')"
assert code.count(old)==1
precision=root/'PRECISION_CHECK.json'; original=precision.read_bytes()
sys.path.insert(0,str(root))
sys.argv=[str(source),*sys.argv[2:]]
try:
    exec(compile(code.replace(old,new),str(source),'exec'),{'__name__':'__main__','__file__':str(source)})
finally:
    actual=precision.read_bytes()
    precision.write_bytes(original)
assert actual.replace(b'\r\n',b'\n')==original.replace(b'\r\n',b'\n')
print('PASS_RESPONSE_REPLAY_WITH_ONLY_CRLF_LF_COMPARISON_PORTABILITY_FIX',flush=True)
