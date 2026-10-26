"""Exact rational audit after all finite midpoint radii were paid."""
from pathlib import Path
H=Path(__file__).resolve().parent
code=(H/'audit_source_gap.py').read_text(encoding='utf8')
code=code.replace('SOURCE_BLOCK_LEDGER_RESERVE.json','SOURCE_ARITHMETIC_CLOSURE.json')
code=code.replace("data['matrices']['remaining_gap']","data['remaining_gap']")
code=code.replace('SOURCE_GAP_EXACT_AUDIT.json','SOURCE_CLOSED_GAP_EXACT_AUDIT.json')
exec(compile(code,str(H/'audit_closed_source_gap.py'),'exec'))
