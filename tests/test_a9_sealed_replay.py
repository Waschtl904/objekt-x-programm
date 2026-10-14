"""Check archival boundaries, failure propagation and focused CI routing."""
from pathlib import Path
import copy, fnmatch, hashlib, importlib.util, io, json, sys, tempfile, unittest, zipfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import replay_a9_sealed as replay

class SealedReplayTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        self.p=self.root/'original.zip'
        with zipfile.ZipFile(self.p,'w') as z:z.writestr('root/original.txt',b'preserve\r\nbytes\n')
        self.spec={'bytes':self.p.stat().st_size,'sha256':replay.digest(self.p),
                   'members':{'root/original.txt':{'bytes':16,'sha256':hashlib.sha256(b'preserve\r\nbytes\n').hexdigest()}}}
        self.spec['members']['root/original.txt']['bytes']=len(b'preserve\r\nbytes\n')
    def tearDown(self):self.tmp.cleanup()
    def test_original_bytes(self):replay.archive(self.p,self.spec)
    def test_damaged_archive(self):
        self.p.write_bytes(self.p.read_bytes()+b'changed')
        with self.assertRaisesRegex(ValueError,'archive bytes'):replay.archive(self.p,self.spec)
    def test_incomplete_catalogue(self):
        self.spec['members']={}
        with self.assertRaisesRegex(ValueError,'incomplete member'):replay.archive(self.p,self.spec)
    def test_wrong_member_hash(self):
        self.spec['members']['root/original.txt']['sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'member hash'):replay.archive(self.p,self.spec)
    def test_unsafe_paths(self):
        for name in ('../escape','/absolute','x/../y','x//y','C:drive','x\\y',''):
            with self.subTest(name=name),self.assertRaises(ValueError):replay.safe(self.root,name)
    def test_failed_checker(self):
        with self.assertRaisesRegex(ValueError,'checker failed'):
            replay.execute([sys.executable,'-c','print("PASS"); raise SystemExit(3)'],self.root/'failure.log')
    def test_wrong_receipt(self):
        with self.assertRaisesRegex(ValueError,'receipt differs'):replay.match({'status':'PASS'},{'status':'FAIL'})
    def test_repository_output_rejected(self):
        with self.assertRaisesRegex(ValueError,'output must be new'):
            replay.run(ROOT/'research/x-c1',ROOT/'unsafe-output')
    def test_ci_routing(self):
        configurations=[('a9-domain-continuation.yml','a9-domain-continuation-2026-10-13')]
        inverse=ROOT/'.github/workflows/a9-inverse-renewal.yml'
        if inverse.exists():configurations.append((inverse.name,'a9-inverse-renewal-2026-10-13'))
        for workflow,folder in configurations:
            wf='.github/workflows/'+workflow;prefix='research/x-c1/'+folder
            patterns=[prefix+'/**','scripts/replay_a9_sealed.py','tests/test_a9_sealed_replay.py',wf]
            raw=(ROOT/wf).read_text(encoding='utf-8')
            got=[line.strip()[3:-1] for line in raw.splitlines() if line.strip().startswith('- "')]
            self.assertEqual(got,patterns+patterns)
            for path in (prefix+'/PROOF.md',prefix+'/archives/original.zip',patterns[1],patterns[2],wf):
                self.assertTrue(any(fnmatch.fnmatchcase(path,p) for p in patterns))
            for path in ('README.md','00-uebersicht/RESEARCH_STATE.yaml','research/unrelated/input.json'):
                self.assertFalse(any(fnmatch.fnmatchcase(path,p) for p in patterns))

if __name__=='__main__':unittest.main()
