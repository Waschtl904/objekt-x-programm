def columns(vectors):return arb_mat([[v[i] for v in vectors] for i in range(len(vectors[0]))])
def sub(A,rows,cols):return arb_mat([[A[i,j] for j in cols] for i in rows])
def polycols(polys,n):return arb_mat([[v[k] for v in polys] for k in range(n)])
def hankel(seq,n,m):return arb_mat([[seq[i+j] for j in range(m)] for i in range(n)])
jj=list(range(84));kk=list(range(84,92))
mmall=[]
for j in range(NC):
    mm=function_moments(globalF[j],mom,'zero','one',383)
    for ci,(lo,hi) in enumerate(cells):
        add=mom.polynomial_moments(cellF[j][ci],lo,hi,383)
        mm=[x+y for x,y in zip(mm,add)]
    mmall.append(mm)
    if j%16==0:say(f'complete low projection {j}/{NC}')
legmat=arb_mat([[pol[n][k]*arb(2*n+1).sqrt() for k in range(384)] for n in range(p,384,2)])
rawlow=legmat*columns(mmall)
cp=ROOT/f'work/galerkin84-2026-10-10/GALERKIN_{args.parity.upper()}_3072.json';oldj=read(cp)
calibration=0
for i in range(191):
    for j in range(NC):
        value=rawlow[i+1,j]-cn[i]*rawlow[0,j]
        target=oldj['old_low_c_model'][i][j] if j<84 else data['frozen_K']['source_c_model'][i][j-83]
        assert value.overlaps(box(target)),('low-model calibration',i,j)
        calibration+=1
say(f'all {calibration} complete low-force calibrations passed')
tags=list(globalF[0]);sizes={tag:max(len(f[tag]) for f in globalF) for tag in tags}
features={tag:polycols([f[tag] for f in globalF],sizes[tag]) for tag in tags}
fullCross=arb_mat(84,8)
for ia,ta in enumerate(tags):
    for tb in tags:
        na,nb=sizes[ta],sizes[tb];logs=tuple(t for t in [ta,tb] if t is not None)
        seq=mom.sequence('zero','one',logs,na+nb-2)
        fullCross+=sub(features[ta],range(na),jj).transpose()*hankel(seq,na,nb)*sub(features[tb],range(nb),kk)
    say(f'complete logarithmic cross block {ia+1}/{len(tags)}')
for ci,(lo,hi) in enumerate(cells):
    degree=max(len(v[ci]) for v in cellF)
    coeff=polycols([v[ci] for v in cellF],degree)
    gm=columns([function_moments(f,mom,lo,hi,degree-1) for f in globalF])
    cj=sub(coeff,range(degree),jj);ck=sub(coeff,range(degree),kk)
    fullCross+=cj.transpose()*sub(gm,range(degree),kk)+sub(gm,range(degree),jj).transpose()*ck
    seq=mom.sequence(lo,hi,(),2*degree-2)
    fullCross+=cj.transpose()*hankel(seq,degree,degree)*ck
    say(f'complete prime-cell cross {ci+1}/{len(cells)}')
highCross=fullCross-sub(rawlow,range(192),jj).transpose()*sub(rawlow,range(192),kk)
# Independent complete function pairings, with the full high projection.
projectcoeff=polycols([pol[n]*arb(2*n+1).sqrt() for n in range(p,384,2)],384)*rawlow
high=[add_function(globalF[j],{None:arb_poly([projectcoeff[k,j] for k in range(384)])},-1) for j in range(NC)]
checks=[]
for i,j in [(0,84),(40,88),(83,91)]:
    val=function_product(high[i],high[j],mom,'zero','one')
    for ci,(lo,hi) in enumerate(cells):
        fi={None:cellF[i][ci]};fj={None:cellF[j][ci]}
        val+=function_product(high[i],fj,mom,lo,hi)+function_product(fi,high[j],mom,lo,hi)+function_product(fi,fj,mom,lo,hi)
    diff=val-highCross[i,j-84]
    assert diff.contains(0) and abs(diff)<af('1e-30')
    checks.append({'J':i,'external':j-84,'difference':diff})
say('three independent full high-source pairings passed')
dp=ROOT/f'work/direct-rest84-2026-10-11/DIRECT_REST_{args.parity.upper()}_3072.json';directold=read(dp)
Msource=[box(x) for x in directold['M_source_model'][:84]]
for j in kk:
    val=function_product(globalF[j],{None:mcore},mom,'zero','one')
    for ci,(lo,hi) in enumerate(cells):val+=mom.integral(cellF[j][ci]*mcore,lo,hi)
    Msource.append((2*a).sqrt()*val)
Qmm=box(directold['Q_mm_model'])
shellpath=INHERITED/'work/gamma-low-2026-10-09/SHELL_GAMMA_4096.json';shell_data=read(shellpath)
localmom=Moments({'left':arb(-1),'right':arb(1)},500)
c_direct=-(arb.pi()*h).log()-arb.const_euler();harm=[arb(0)]
for n in range(1,NLOC):harm.append(harm[-1]+arb(1)/n)
Jcoeff=sub(Ymid,range(NLOC),jj);Kcoeff=sub(Ymid,range(NLOC),kk)
diagonal=Jcoeff.transpose()*arb_mat([[(harm[n]+c_direct)*Kcoeff[n,k] for k in range(8)] for n in range(NLOC)])
JL=polycols(Ylocal[:84],NLOC);KL=polycols(Ylocal[84:],NLOC)
seq1=localmom.sequence('left','right',('left',),2*NLOC-2);seq2=localmom.sequence('left','right',('right',),2*NLOC-2)
potential=JL.transpose()*hankel([-(x+y)*h/2 for x,y in zip(seq1,seq2)],NLOC,NLOC)*KL
cs32=list(map(F,shell_data['self_coefficients']));kernels=[]
for j in kk:
    ks=arb_poly([])
    for parity_local in [0,1]:
        ls=[Ymid[n,j]*((2*n+1)/(2*h)).sqrt() if n%2==parity_local else arb(0) for n in range(NLOC)]
        rp=sum((pol[n]*ls[n] for n in range(NLOC)),arb_poly([]))
        ks+=kernel(rp,ls,h/2,cs32,parity_local)
    kernels.append(ks)
kd=max(map(len,kernels));seq=localmom.sequence('left','right',(),kd+NLOC-2)
selfpair=JL.transpose()*hankel(seq,NLOC,kd)*polycols(kernels,kd)*h
vm=[]
for j in range(32):
    rate=af(F(4*j+1,2))
    vm.append([h*((2*n+1)/(2*h)).sqrt()*(-rate*c).exp()*((-1)**n)*mellin(n,rate*h) for n in range(NLOC)])
Mmirror=arb_mat(vm)*Ymid
mirrorpair=2*sub(Mmirror,range(32),jj).transpose()*sub(Mmirror,range(32),kk)
correction=arb_mat([[-(lam[i]*Msource[j]+Msource[i]*lam[j])/mu-lam[i]*lam[j]*Qmm/mu**2 for j in kk] for i in jj])
directCross=diagonal+potential-selfpair-((-1)**p)*mirrorpair+correction
LKK=Kcoeff.transpose()*arb_mat([[(harm[n]+af('1.1'))*Kcoeff[n,k] for k in range(8)] for n in range(NLOC)])
LJK=Jcoeff.transpose()*arb_mat([[(harm[n]+af('1.1'))*Kcoeff[n,k] for k in range(8)] for n in range(NLOC)])
assert rounding<af('1e-60') and epsGamma<af('1e-34')
bindings.update({path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in [cp,dp,shellpath]})
out={'status':'FULL_HIGH_AND_DIRECT_J84_EXTERNAL8_CROSSES','parity':args.parity,'bits':args.bits,
 'full_high_cross_model':highCross,'direct_cross_model':directCross,'L_external_model':LKK,'L_J_external_model':LJK,
 'source_model_J_and_K_frozen':True,'complete_low_force_calibrations':calibration,'full_high_function_checks':checks,
 'rounding':rounding,'gamma_error':epsGamma,'direct_cross_entry_error':'1e-20','bindings':bindings,
 'seconds':time.monotonic()-start,'full_remainder_certified':False}
args.out.write_text(json.dumps(serial(out,80),indent=2)+'\n')
say('DONE complete J84/exterior8 crosses for the composed residual')
