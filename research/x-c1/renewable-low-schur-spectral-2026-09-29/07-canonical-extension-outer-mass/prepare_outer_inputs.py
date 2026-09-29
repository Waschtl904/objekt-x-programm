"""Extract only three fixed inputs from the pinned nested reference archive."""
from pathlib import Path
import argparse,hashlib,io,zipfile

def unpack(raw):
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        assert z.testzip() is None
        files={Path(n).name:z.read(n) for n in z.namelist() if not n.endswith('/')}
    for line in files['SHA256SUMS'].decode().splitlines():
        h,n=line.split('  ',1);assert hashlib.sha256(files[n]).hexdigest()==h
    return files

def main():
    p=argparse.ArgumentParser();p.add_argument('--reference',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();raw=a.reference.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='b5c8f81630711dbde81c3a2622507aa56ee835f19cae4691b3547dbb58db8cc4'
    transport=unpack(raw);ranks=unpack(transport['rank_reference.zip']);unpack(ranks['A11_reference.zip'])
    a.out.mkdir(parents=True,exist_ok=True)
    for name,blob in {'fixed_vectors.json':ranks['fixed_vectors.json'],
                      'rank_reference.zip':transport['rank_reference.zip'],
                      'transport_verification.json':transport['verification.json']}.items():
        (a.out/name).write_bytes(blob)
    print('Three pinned inputs prepared; all three reference manifests passed.')

if __name__=='__main__':main()
