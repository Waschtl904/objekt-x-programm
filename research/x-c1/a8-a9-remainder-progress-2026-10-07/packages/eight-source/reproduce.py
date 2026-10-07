"""Reproduce the fixed eight-source experiment from its preserved source archive."""
from pathlib import Path, PurePosixPath
import argparse,hashlib,json,subprocess,sys,zipfile,os

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def verify(root):
    manifest=root/'SHA256SUMS';seen=set()
    for line in manifest.read_text(encoding='utf-8').splitlines():
        digest,name=line.split('  ',1);p=PurePosixPath(name)
        assert not p.is_absolute() and '..' not in p.parts and '\\' not in name and ':' not in name
        assert name not in seen;seen.add(name)
        assert sha(root.joinpath(*p.parts))==digest,name
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='SHA256SUMS' and '__pycache__' not in p.parts}
    assert actual==seen,(actual-seen,seen-actual)
    return len(seen)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--check-only',action='store_true')
    args=ap.parse_args();assert __debug__
    root=Path(__file__).resolve().parent;out=args.out.resolve()
    assert not out.exists() and not out.is_relative_to(root)
    count=verify(root);out.mkdir(parents=True)
    archive=root/'inputs/ObjektX_A8_Inverse_Energie_2026-10-04.zip'
    assert sha(archive)=='068d2cbf63732d318836dadb5bd86a61e81f74358398d9f4cdba3095f5353536'
    src=out/'original';src.mkdir()
    with zipfile.ZipFile(archive) as z:
        names=z.namelist();assert len(names)==len(set(names))
        for info in z.infolist():
            p=PurePosixPath(info.filename)
            assert not p.is_absolute() and '..' not in p.parts and '\\' not in info.filename and ':' not in info.filename
            assert (info.external_attr>>16)&0o170000 != 0o120000
            dest=src.joinpath(*p.parts)
            if info.is_dir():dest.mkdir(parents=True,exist_ok=True)
            else:dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(info))
    src=src/'Objekt-X-A8-Inverse-Energie-2026-10-04'
    oldcount=verify(src)
    receipt={'status':'PASS_SOURCE_AND_PACKAGE_CHECKS','package_files':count,'source_files':oldcount,
             'archive_preserved':True,'full_replay_performed':False}
    if not args.check_only:
        for bits in [3072,4096]:
            cmd=[sys.executable,'-B',str(root/'code/worker.py'),'--root',str(root),'--source',str(src),'--bits',str(bits),'--out',str(out/str(bits))]
            with (out/(str(bits)+'.log')).open('w',encoding='utf-8') as log:subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT,check=True)
        subprocess.run([sys.executable,'-B',str(root/'code/audit_eight.py'),'--primary',str(out/'3072/RESULT.json'),'--higher',str(out/'4096/RESULT.json'),'--out',str(out/'EXACT_CHECK.json')],check=True)
        sys.path.insert(0,str(root/'code'))
        from audit_eight import compare
        for bits in [3072,4096]:compare(json.loads((root/'expected'/str(bits)/'RESULT.json').read_bytes()),json.loads((out/str(bits)/'RESULT.json').read_bytes()))
        receipt.update(status='PASS_FULL_REPLAY',full_replay_performed=True,bits=[3072,4096],numerical_enclosures_match=True)
    assert sha(archive)=='068d2cbf63732d318836dadb5bd86a61e81f74358398d9f4cdba3095f5353536'
    verify(root);verify(src)
    (out/'REPLAY.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt))
if __name__=='__main__':main()
