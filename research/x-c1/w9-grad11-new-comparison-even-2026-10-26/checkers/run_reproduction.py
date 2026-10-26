"""Relocate one immutable archive lookup without altering research sources."""
from pathlib import Path
import builtins,hashlib,json,os,runpy,sys
H=Path(__file__).resolve().parent;package=H.parents[2]
assert len(sys.argv)>=2,'Usage: run_reproduction.py local_script.py [arguments]'
name=sys.argv[1];assert Path(name).name==name and name.endswith('.py')
target=H/name;assert target.is_file()
record=json.loads((H/'LOW_INPUT_RECEIPT.json').read_bytes())[0]
archive=package/'evidence/Objekt-X-Endlicher-Schuranschluss-2026-10-09.zip'
raw=archive.read_bytes()
assert len(raw)==record['bytes']and hashlib.sha256(raw).hexdigest()==record['sha256']
del raw
repository=package/'repository';assert repository.is_dir()
os.environ['OBJX_REPOSITORY']=str(repository.resolve())
old_open=builtins.open
def relocated_open(file,mode='r',*args,**kwargs):
    if isinstance(file,(str,os.PathLike))and os.fspath(file)==record['local_cache']:
        assert mode=='rb','Historical archive is read-only'
        return old_open(archive,mode,*args,**kwargs)
    return old_open(file,mode,*args,**kwargs)
builtins.open=relocated_open
sys.path.insert(0,str(H));sys.argv=[str(target)]+sys.argv[2:]
try:runpy.run_path(str(target),run_name='__main__')
finally:builtins.open=old_open
