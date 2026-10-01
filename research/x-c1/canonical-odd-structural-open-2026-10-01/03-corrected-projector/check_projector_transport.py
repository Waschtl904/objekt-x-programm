"""Independent exact algebra and inherited operator controls."""
from pathlib import Path
from fractions import Fraction as F
import os,subprocess,sys,tempfile
from verify_projector_transport import BASE,ARCHIVE,unpack,load_input

def positive2(a):assert a[0][0]>0 and a==list(map(list,zip(*a))) and a[0][0]*a[1][1]-a[0][1]**2>0
def main():
 with tempfile.TemporaryDirectory(prefix='projector-controls-') as name:
  temp=Path(name);folder,_,up=load_input(temp);e=up.e
  g=[[F(2),F(1)],[F(1),F(3)]];h=[[F(1,4),F(1,16)],[F(1,16),F(1,5)]]
  positive2(g);positive2(h);p=e.sub(g,h);positive2(p)
  assert e.mm(g,h)!=e.mm(h,g)
  a=e.mm(h,e.inv(g));c=e.add(e.eye(2),e.scale(a,F(1,4)))
  mass=e.sub(g,e.mm(e.mm(c,p),e.trans(c)))
  ah=e.mm(a,h);aah=e.mm(a,ah)
  assert mass==e.add(e.add(e.scale(h,F(1,2)),e.scale(ah,F(7,16))),e.scale(aah,F(1,16)))
  positive2(mass)
  similar_form=e.mm(c,g);positive2(similar_form)
  assert similar_form==e.add(g,e.scale(h,F(1,4)))
  y=[[F(1),F(0),F(1)],[F(0),F(1),F(-2)]];n=[[F(-1)],[F(2)],[F(1)]]
  assert e.mm(y,n)==e.mm(e.mm(c,y),n)==[[F(0)],[F(0)]]
  assert e.mm(e.inv(c),e.mm(c,y))==y
  # Mass improvement alone does not universally imply high support.
  cs=F(21,20);mass_scalar=1-cs**2*F(4,5);energy_scalar=F(1,100)-cs**2*F(9,1000)
  assert mass_scalar>0 and energy_scalar>0 and energy_scalar-mass_scalar<0
  raw=(BASE/'inputs'/ARCHIVE).read_bytes()
  try:unpack(raw+b' ',temp/'bad')
  except AssertionError as exc:assert 'hash mismatch' in str(exc)
  else:raise AssertionError('tampered input accepted')
  subprocess.run([sys.executable,'-B',str(folder/'check_transport_gate.py')],
   check=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
 print('Noncommuting mass identity, exact kernel preservation, negative support control and tamper rejection: PASS')
if __name__=='__main__':main()
