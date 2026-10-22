"""Negative controls of active repair entrances; no external theorem acceptance."""
import sys
if not __debug__: raise SystemExit('Verification requires assertions enabled; Python -O/-OO is rejected.')
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
import json,shutil,subprocess,tempfile,unittest
from kernel_geometry import coefficients,evaluate,polynomial_circle_bound
HERE=Path(__file__).resolve().parent
class Controls(unittest.TestCase):
 def test_wrong_geometry_is_detected(self):
  m=[Q(1),Q(3,2)];g=[0,Q(-1,24)]
  self.assertEqual(evaluate(coefficients(g,m,inner=True),Q(1,2)),Q(-1,16))
  self.assertEqual(evaluate(coefficients(g,m,inner=False),Q(1,2)),Q(-1,48))
 def test_wrong_contour_radius_is_detected(self):
  self.assertEqual(polynomial_circle_bound([0]*8+[1],3),6561)
  self.assertLess(polynomial_circle_bound([0]*8+[1],2),6561)
 def test_optimization_rejected_at_active_entrances(self):
  for p in ['verify.py','test_controls.py','norm/independent_norm.py','norm/rational_cross_audit.py','pairing-review/verify_package.py','pairing-review/Rationale-Pruefung/rational_audit.py']:
   for flag in ['-O','-OO']:
    with self.subTest(path=p,flag=flag):
     r=subprocess.run([sys.executable,flag,'-B',str(HERE/p)],capture_output=True,text=True)
     self.assertNotEqual(r.returncode,0);self.assertIn('assertions enabled',r.stderr+r.stdout)
 def test_tampered_file_rejected(self):
  with tempfile.TemporaryDirectory()as td:
   dest=Path(td)/'package';shutil.copytree(HERE,dest)
   with (dest/'PROOF.md').open('a')as f:f.write('\nTAMPER\n')
   r=subprocess.run([sys.executable,'-B',str(dest/'verify.py'),'--bindings-only'],capture_output=True,text=True)
   self.assertNotEqual(r.returncode,0);self.assertIn('Package hash',r.stderr+r.stdout)
 def test_removed_signed_correction_rejected(self):
  with tempfile.TemporaryDirectory()as td:
   dest=Path(td)/'norm';shutil.copytree(HERE/'norm',dest)
   p=dest/'inputs/kernel-orientation-81.json';d=json.loads(p.read_bytes());d['rows'][0]['orientation_correction']=['0','0'];p.write_text(json.dumps(d))
   r=subprocess.run([sys.executable,'-B',str(dest/'rational_cross_audit.py')],capture_output=True,text=True)
   self.assertNotEqual(r.returncode,0)
 def test_scope_remains_conditional(self):
  meta=json.loads((HERE/'META.yaml').read_bytes())
  self.assertEqual(meta['review_status'],'EXTERNAL_REVIEW_OPEN');self.assertEqual(meta['closes'],[])
  self.assertIn('one unchanged fixed even witness',meta['scope'])
if __name__=='__main__':unittest.main(verbosity=2)
