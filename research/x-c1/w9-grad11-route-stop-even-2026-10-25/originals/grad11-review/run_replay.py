"""Portable entry point; uses the unchanged mathematical replay and local deps."""
from pathlib import Path
import runpy, sys
H=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path[:0]=[str(H/'deps'),str(H/'replay')]
if not __debug__:
    raise SystemExit('Use Python without -O or -OO')
runpy.run_path(str(H/'replay/directed_diagnostic.py'),run_name='__main__')
runpy.run_path(str(H/'replay/endpoint_audit.py'),run_name='__main__')
runpy.run_path(str(H/'independent_audit.py'),run_name='__main__')
