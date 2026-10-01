"""Independent exact controls for exclusion, partition and physical metric."""
from pathlib import Path
from fractions import Fraction as F
import tempfile
from verify_box_gate import BASE,ARCHIVE,unpack,dependencies
from box_math import exclusions,split_box,covers_point,classify,physical_projector

def main():
 with tempfile.TemporaryDirectory(prefix='odd-box-controls-') as name:
  temp=Path(name);_,_,up,_,v,_=dependencies(temp);e=up.e
  assert exclusions(v,v.pointmat([[-1,0],[0,1]]),'test',((0,1),))
  reasons=exclusions(v,v.pointmat([[1,2],[2,1]]),'test',((0,1),))
  assert any(r['kind']=='principal_minor_2' for r in reasons)
  assert not exclusions(v,[[(-F(1),F(1)),v.point(0)],[v.point(0),v.point(1)]],'wide',((0,1),))
  # Boxes containing explicitly SPD matrices must never be rejected.
  for k in range(1,20):
   r=[[F(k,7),F(2,5)],[F(-1,3),F(k+1,11)]]
   a=e.add(e.mm(e.trans(r),r),e.scale(e.eye(2),F(1,100)))
   for radius in [F(0),F(1,10000),F(1)]:
    box=[[(x-radius,x+radius) for x in row] for row in a]
    assert not exclusions(v,box,'contains SPD',((0,1),))
  root={'Y57':(F(-2),F(3)),'Y58':(F(-1),F(1)),'Y67':(F(0),F(2)),'Y68':(F(1),F(5))}
  leaves=[root]
  for key in ['Y58','Y68','Y57','Y67']:
   next_leaves=[]
   for box in leaves:
    left,right=split_box(box,key)
    assert left[key][0]==box[key][0] and right[key][1]==box[key][1] and left[key][1]==right[key][0]
    for other in root:
     if other!=key:assert left[other]==right[other]==box[other]
    next_leaves.extend([left,right])
   leaves=next_leaves
  assert any(covers_point(b,{k:(sum(x)/2,sum(x)/2) for k,x in root.items()}) for b in leaves)
  undecided={'filter_status':'NOT_EXCLUDED','direction':{'within_target_corridor':False}}
  good={'filter_status':'NOT_EXCLUDED','direction':{'within_target_corridor':True}}
  assert classify([undecided])=='UNRESOLVED' and classify([good])=='GREEN'
  assert classify([undecided,good],True)=='STRUCTURAL_OPEN'
  assert classify([{'filter_status':'EXCLUDED'}])=='EMPTY_OUTER_FAMILY'
  # Exact non-Euclidean physical angle: u=(2,1), c=(1,0), G=[[2,1],[1,3]].
  # cos^2=25/(2*15)=5/6, whereas the Euclidean value would be 4/5.
  g=v.pointmat([[2,1],[1,3]]);k=v.pointmat([[4,-2],[2,-1]]);c=[[v.point(1)],[v.point(0)]]
  projector,sin2=physical_projector(v,v.eye(2),g,g,k,c,F(3))
  assert sin2[0]<=F(1,6)<=sin2[1] and sin2[1]-sin2[0]<F('1e-120')
  expected=[[F(2,3),F(2,3)],[F(1,3),F(1,3)]]
  assert all(projector[i][j][0]<=expected[i][j]<=projector[i][j][1] for i in range(2) for j in range(2))
  # Check the two normalizations of the b-Gram exactly, including factor 17.
  gb=[[F(2),F(1)],[F(1),F(3)]];lb=[[F(1,100),F(0)],[F(0),F(1,200)]];y=[[F(1),F(2)]]
  normalized=e.mm(e.inv(e.add(gb,e.scale(lb,F(1,17)))),e.trans(y))
  unnormalized=e.scale(e.mm(e.inv(e.add(e.scale(gb,17),lb)),e.trans(y)),17)
  assert normalized==unnormalized
  try:unpack((BASE/'inputs'/ARCHIVE).read_bytes()+b' ',temp/'bad')
  except AssertionError as exc:assert 'hash mismatch' in str(exc)
  else:raise AssertionError('tampered archive accepted')
 print('PSD exclusion controls, exact four-variable partition, three-way status, physical Gram angle, factor-17 normalization and archive tamper rejection: PASS')
if __name__=='__main__':main()
