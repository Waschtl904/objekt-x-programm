"""Input rejection and scope controls for the new method pilot only."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('method_verify',HERE/'verify.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)

class Controls(unittest.TestCase):
    def test_wrong_hash_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'input').write_bytes(b'modified')
            binding={'source_commit':v.BASE,'files':{'first':{'path':'input','sha256':'0'*64}}}
            with self.assertRaisesRegex(ValueError,'Hash mismatch'):
                v.snapshot(root,json.dumps(binding).encode())

    def test_escape_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            binding={'source_commit':v.BASE,'files':{'first':{'path':'../outside','sha256':'0'*64}}}
            with self.assertRaisesRegex(ValueError,'Escaping input'):
                v.snapshot(root,json.dumps(binding).encode())

    def test_negative_norm_rejected(self):
        with self.assertRaisesRegex(ValueError,'Invalid norm square'):
            v.upnorm(v.arb(-1))

    def test_negative_root_rejected(self):
        with self.assertRaisesRegex(ValueError,'Negative square'):
            v.sqrt_upper(-1)

    def test_optimized_python_rejected(self):
        run=subprocess.run([sys.executable,'-O',str(HERE/'verify.py')],capture_output=True,text=True,timeout=10)
        self.assertNotEqual(run.returncode,0)
        self.assertIn('python -O is not allowed',run.stderr)

    def test_target_not_a_measured_value(self):
        result=json.loads((HERE/'RESULT.json').read_bytes())
        self.assertFalse(result['full_residual_computed'])
        self.assertFalse(result['full_inverse_upper_certified'])
        self.assertIn('NOT been computed',result['condition'])

if __name__=='__main__': unittest.main()
