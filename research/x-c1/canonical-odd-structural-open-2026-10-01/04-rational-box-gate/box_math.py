"""Safe outer-box filters and a physical rank-one projector enclosure."""
from fractions import Fraction as F

VARIABLES={'Y57':(4,6),'Y58':(4,7),'Y67':(5,6),'Y68':(5,7)}

def split_box(box,key):
 lo,hi=box[key];assert lo<hi;mid=(lo+hi)/2
 left=dict(box);right=dict(box);left[key]=(lo,mid);right[key]=(mid,hi)
 return left,right

def covers_point(box,point):
 return all(box[k][0]<=point[k][0]<=point[k][1]<=box[k][1] for k in box)

def exclusions(v,matrix,label,pairs=((4,5),)):
 out=[]
 for i,row in enumerate(matrix):
  if row[i][1]<0:out.append({'matrix':label,'kind':'diagonal','indices':[i+1],'upper':row[i][1]})
 for i,j in pairs:
  minor=v.sub(v.mul(matrix[i][i],matrix[j][j]),v.square(matrix[i][j]))
  if minor[1]<0:out.append({'matrix':label,'kind':'principal_minor_2','indices':[i+1,j+1],'upper':minor[1]})
 return out

def classify(leaves,separated_witnesses=False):
 # Unexcluded interval boxes do not certify existence.
 if separated_witnesses:return 'STRUCTURAL_OPEN'
 live=[x for x in leaves if x['filter_status']!='EXCLUDED']
 if not live:return 'EMPTY_OUTER_FAMILY'
 if all(x.get('direction',{}).get('within_target_corridor',False) for x in live):return 'GREEN'
 return 'UNRESOLVED'

def physical_projector(v,n,g,gb,k,reference,gap_lower):
 """Physical G-orthogonal rank-one projection; no eigenvector-component chart."""
 u=v.mm(n,k);covariance=v.mm(k,v.tr(k));den=v.trace(v.mm(covariance,g))
 dg=v.determinant(g);assert dg[0]>0 and v.trace(g)[1]>0
 den_floor=dg[0]/v.trace(g)[1]*gap_lower**2
 den=(max(den[0],den_floor),den[1]);assert 0<den[0]<=den[1]
 c=reference;gbc=v.mm(gb,c);norm=v.mm(v.tr(c),gbc)[0][0]
 floor=min(gb[i][i][0]-sum(v.absolute(gb[i][j]) for j in range(len(gb)) if j!=i) for i in range(len(gb)))
 assert floor>0
 cnorm=sum(x[0][0]**2 for x in c)
 norm=(max(norm[0],floor*cnorm),norm[1]);assert 0<norm[0]<=norm[1]
 product=v.mm(v.tr(u),gbc);numerator=v.total(v.square(row[0]) for row in product)
 cos2=v.div(numerator,v.mul(norm,den));cos2=(max(F(0),cos2[0]),min(F(1),cos2[1]));assert cos2[0]<=cos2[1]
 sin2=(1-cos2[1],1-cos2[0])
 projector=[[v.div(x,den) for x in row] for row in v.mm(covariance,g)]
 return projector,sin2

class BoxModel:
 def __init__(self,v,source,outer,projected,inherited):
  self.v=v;self.source=source;self.outer=outer;self.key='A9->A11-odd'
  self.r=source['results'][self.key]
  self.nr=projected['runs']['primary.json']['results'][self.key]
  second=projected['runs']['crosscheck.json']['results'][self.key]
  self.y=v.intersectmat(v.matrix(self.nr['Y']),v.matrix(second['Y']))
  self.full={}
  for chamber,prefix in [('A9-odd','A'),('A11-odd','B')]:
   first=projected['runs']['primary.json']['trials'][chamber]
   other=projected['runs']['crosscheck.json']['trials'][chamber]
   for short,field in [('G','projected_Gram'),('L','projected_energy'),('Z','projected_inverse')]:
    self.full[short+prefix]=v.symmetric(v.intersectmat(v.matrix(first[field]),v.matrix(other[field])))
  self.nu=F(outer['trials']['A11-odd']['physical_complement_gap_lower_exact'])
  self.s=v.symmetric(v.matrix(outer['trials']['A11-odd']['physical_Ritz_matrix']))
  self.global_bounds=inherited['results']['primary.json'][self.key]
  self.reference=[[v.point(sum(map(F,row[1]))/2)] for row in self.r['central_N']]
  self.target=F(1,100)
  self.prepare()

 def prepare(self):
  v=self.v
  self.bb=v.addmat(self.full['GB'],v.scale(self.full['LB'],F(1,17)))
  self.bbi=v.inverse(self.bb,True)
  self.ylinv=v.inverse([row[:6] for row in self.y])

 def root_box(self):return {name:self.y[i][j] for name,(i,j) in VARIABLES.items()}

 def matrix_y(self,box):
  y=[row[:] for row in self.y]
  for key,(i,j) in VARIABLES.items():y[i][j]=box[key]
  return y

 def transport(self,y):
  v=self.v;f=self.full;x=v.mm(self.bbi,v.tr(y))
  mass=v.symmetric(v.submat(f['GA'],v.mm(v.mm(v.tr(x),f['GB']),x)))
  energy=v.symmetric(v.submat(f['LA'],v.mm(v.mm(v.tr(x),f['LB']),x)))
  first=v.submat(energy,v.scale(mass,self.nu))
  second=v.addmat(v.submat(f['LA'],v.scale(f['GA'],self.nu)),
   v.mm(v.mm(v.tr(x),v.submat(v.scale(f['GB'],self.nu),f['LB'])),x))
  support=v.symmetric(v.intersectmat(first,second))
  return {'H0':mass,'H1':energy,'Hnu':support}

 def inverse2(self,a,det_bounds):
  v=self.v;d=v.intersect(v.determinant(a),det_bounds);assert d[0]>0,'unresolved determinant floor'
  adj=[[a[1][1],v.neg(a[0][1])],[v.neg(a[1][0]),a[0][0]]]
  return [[v.div(x,d) for x in row] for row in adj]

 def direction(self,y):
  v=self.v;r=self.r;f=self.full;nr=self.nr
  n=v.scale(v.mm(self.ylinv,[row[6:] for row in y]),-1)+v.eye(2)
  n=v.intersectmat(n,v.matrix(nr['N']))
  def compress(a):return v.symmetric(v.mm(v.mm(v.tr(n),a),n))
  g=v.symmetric(v.intersectmat(compress(f['GB']),v.matrix(nr['compressed_moment_entries']['G0'])))
  lower=v.symmetric(v.matrix(r['energy_Loewner_lower_in_raw_basis']));upper=v.symmetric(v.matrix(r['energy_Loewner_upper_in_raw_basis']))
  l=v.symmetric(v.intersectmat(v.intersectmat(compress(f['LB']),v.matrix(nr['compressed_moment_entries']['L0'])),v.hull_from_order(lower,upper)))
  z=v.symmetric(v.intersectmat(compress(f['ZB']),v.matrix(nr['compressed_moment_entries']['Z0'])))
  # Same Y and N are used in both inverse-energy functionals.
  flo,_=v.functional_enclosure(v.matrix(r['trial_resolvent_lower_factor']),y,v.matrix(r['central_left']),n)
  fhi,_=v.functional_enclosure(v.matrix(r['trial_resolvent_upper_factor']),y,v.matrix(r['central_left']),n)
  en=compress(self.s)
  zlo=v.submat(v.mm(v.tr(flo),flo),v.scale(en,1/self.nu**2));zhi=v.mm(v.tr(fhi),fhi)
  z=v.symmetric(v.intersectmat(z,v.hull_from_order(zlo,zhi)))
  li=self.inverse2(l,(v.determinant(lower)[0],v.determinant(upper)[1]))
  m=v.symmetric(v.addmat(v.addmat(l,v.scale(g,34)),v.scale(v.mm(v.mm(g,li),g),289)))
  rr=v.symmetric(v.addmat(v.addmat(l,v.scale(g,34)),v.scale(z,289)))
  mi=self.inverse2(m,v.interval(self.global_bounds['a_interval']))
  t=v.mm(mi,rr);beta=v.interval(self.global_bounds['beta_minus_interval'])
  tr=v.trace(t);det=v.determinant(t);delta=v.sub(v.square(tr),v.mul(v.point(4),det))
  if delta[0]>0 and det[0]>0 and tr[0]>0:
   gap=(v.sqrt_lower(delta[0]),v.sqrt_upper(delta[1]))
   plus=v.div(v.add(tr,gap),v.point(2))
   beta=v.intersect(beta,v.div(det,plus))
  k=[row[:] for row in t]
  for i in range(2):k[i][i]=v.sub(k[i][i],beta)
  projector,sin2=physical_projector(v,n,g,f['GB'],k,self.reference,F(self.global_bounds['gap_lower']))
  return {'same_N_for_all_moments':True,'N':n,'G0':g,'L0':l,'Z0':z,
   'beta_minus':beta,'physical_Gram_projector_in_kernel_coordinates':projector,
   'sine_squared_to_common_reference':sin2,'within_target_corridor':sin2[1]<=self.target}

 def evaluate(self,box):
  y=self.matrix_y(box);moments=self.transport(y)
  reasons=exclusions(self.v,moments['H0'],'H0')+exclusions(self.v,moments['Hnu'],'Hnu')
  result={'filter_status':'EXCLUDED' if reasons else 'NOT_EXCLUDED','exclusion_reasons':reasons,
   'transport_diagonals':{name:[row[i] for i,row in enumerate(a)] for name,a in moments.items()},
   'existence_from_box_survival':False}
  if not reasons:
   try:result['direction']=self.direction(y)
   except AssertionError as exc:result['direction']={'within_target_corridor':False,'enclosure_unresolved':str(exc)}
  return result
