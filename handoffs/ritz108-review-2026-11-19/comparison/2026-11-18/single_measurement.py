"""ONE non-rigorous 108-bank decision measurement, fixed 3328-bit arithmetic.
Supplied quadrature adapted only for input bindings, correct current inverse,
correct residual subtraction, and fixed diagnostics. No physical error certificate.
"""
import sys,json,gzip,time,hashlib,traceback
from pathlib import Path
from fractions import Fraction as Fr
from math import factorial
HERE=Path(__file__).resolve().parent
sys.path[:0]=[str(HERE/'deps'),str(HERE/'assets')]
import flint
from flint import arb,arb_poly,arb_series,arb_mat,ctx
assert flint.__version__=='0.9.0'
ctx.prec=3328
import model_cache
from common import q,mat,ratmat,mellin,legs,columns
from residuals import Residuals
from old_fields import OldFields
def sub(a,rows,cols):return arb_mat([[a[i,j] for j in cols] for i in rows])
def midpoint(a):return arb_mat([[a[i,j].mid() for j in range(a.ncols())] for i in range(a.nrows())])
def read_json(p):
    raw=Path(p).read_bytes()
    while raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
    return json.loads(raw)
class BoundInputs:
    def json(self,alias):return read_json(HERE/'assets'/(alias+'.raw'))
def native(p):
    b=read_json(p);assert hashlib.sha256(b['payload'].encode()).hexdigest()==b['payload_sha256']
    return model_cache.unpack(json.loads(b['payload']))
def number(x,n=24):return x.mid().str(n,radius=False)
def radius(x):return x.rad().str(8,radius=False)
def deadline():
    if time.monotonic()-t0>1800:raise RuntimeError('Fixed 1800-second decision budget exhausted; no rerun')
ROOT=HERE.parent.parent
DIRECTION=ROOT/'work/abnahme_20261110/direction/Objekt-X-GPT2-Richtungsnachweis-Neue-Inversmajorante-2026-11-01'
BANKDIR=ROOT/'work/abnahme_20261110/budget_work/vorabtest/eingang'
NATIVEPATH=ROOT/'work/abnahme_20261110/review_20261110/original_20261109/budget/carrier_recombination/SHARP_FORCE_SOLUTION_NATIVE.json.gz'
OUT=HERE/'single_run';OUT.mkdir(exist_ok=True)
assert not (OUT/'START.json').exists(),'This measurement is single-use'
spec={'precision_bits':3328,'maximum_seconds':1800,'x_gauss_nodes':192,'regular_x_subpanels':4,'endpoint_dyadic_panels':120,'correlation_gauss_nodes':96,'gamma_degree':360,'bank_dimension':108,'control_max_component_difference':'1e-12','control_dual_error_norm':'1e-6','rigorous':False,'new_precision_runs_allowed':0}
(OUT/'START.json').write_text(json.dumps(spec,indent=2)+'\n')
t0=time.monotonic()
inp=BoundInputs()
print('Building frozen function representations, fixed 3328 bits',flush=True)
res=Residuals(inp,'even',degree=360)
old=OldFields(inp,res)
a8, a9, b, h, hs, mu8, mu9 = res.a8, res.a, res.b, res.h, res.hs, res.mu8, res.mu

MODES = [12, 14]
NM = 2
leg20 = legs(20)
center_ab = (a9 + b)/2
ell20 = [leg20[j](arb_poly([-1-2*a9/h, 2/h]))*(arb(2*j+1)/(2*h)).sqrt() for j in range(20)]
lam20 = [(h*(2*j+1)/2).sqrt()*mellin(j, h/2)*((center_ab/2).cosh() if j%2==0 else (center_ab/2).sinh()) for j in range(20)]
d_norm = 2*mu9 + 4*sum((lam20[j]**2 for j in range(12)), arb(0))

deg = 360
fac = [arb(factorial(j)) for j in range(deg+20)]
sh_s = arb_series([1/fac[j+1] if j%2==0 else arb(0) for j in range(deg+2)], prec=deg+2)
ex_s = arb_series([1/(2**j*fac[j]) for j in range(deg+2)], prec=deg+2)
reg_s = (ex_s/sh_s)/2
A_ker = arb_poly([reg_s[j+1]*fac[j] for j in range(deg, -1, -1)])
moments = [(b**(j+1)-a9**(j+1))/(j+1) for j in range(deg+25)]

mode_data = []
for m in MODES:
    P = ell20[m] + sum(((-4*lam20[j]*lam20[m]/d_norm)*ell20[j] for j in range(12)), arb_poly([]))
    Ac = -2*lam20[m]/d_norm
    muvec = [sum((c*moments[j+k] for k, c in enumerate(P)), arb(0)) for j in range(deg+1)]
    conv = A_ker * arb_poly([v/fac[j] for j, v in enumerate(muvec)])
    gam = arb_poly([conv[deg-k]/fac[k]*((-1)**k + 1) for k in range(deg+1)])
    quot = arb_poly([sum((P[j]*moments[j-k-1] for j in range(k+1, len(P))), arb(0)) for k in range(len(P)-1)])
    P_neg = P(arb_poly([0, -1])); quot_neg = quot(arb_poly([0, -1]))
    mode_data.append((m, P, Ac, gam, quot, P_neg, quot_neg))

inv_data = read_json(DIRECTION/'final-inputs/INVERSE_DATA.json')
B_arb = ratmat(inv_data['input_basis_B'])
Y_arb = ratmat(inv_data['test_columns_Y'])
X_arb = ratmat(inv_data['outer_response_X'])

phi12 = [res.legs[n]*(arb(2*n+1)/(2*a9)).sqrt() - res.legs[0]*((arb(2*n+1)/(2*a9)).sqrt()*mellin(n,a9)/mellin(0,a9)) for n in range(2,26,2)]
TB = res.T * B_arb
P0_polys = [sum((f*TB[i,j] for i,f in enumerate(phi12)), arb_poly([])) for j in range(12)]

def w_polys(polys, B):
    return [sum((f*B[i,j] for i,f in enumerate(polys)), arb_poly([])) for j in range(12)]
hB_ell = w_polys([p.p for p in res.ell], B_arb)
hB_ner = [p(arb_poly([0, -1])) for p in hB_ell]
hB_quot = w_polys([p.p for p in res.quot], B_arb)
hB_qn = [p(arb_poly([0, -1])) for p in hB_quot]
hB_gam = w_polys([p.p for p in res.gamma], B_arb)
hB_dv = w_polys([p.p for p in res.Dv], B_arb)
hB_dm = [sum((res.Dm[i]*B_arb[i,j] for i in range(12)), arb(0)) for j in range(12)]
hB_ac = [sum((res.Ac[i]*B_arb[i,j] for i in range(12)), arb(0)) for j in range(12)]

logs5 = [arb(n).log() for n in (2,3,5,7,11)]
av=(Fr(3,2),0,0,0,0); bv=(0,1,0,0,0); cv=(0,0,0,0,Fr(1,2))
shifts=[(1,0,0,0,0),bv,(2,0,0,0,0),(0,0,1,0,0),(0,0,0,1,0),(3,0,0,0,0),(0,2,0,0,0)]
cand={av}
for edge in (av,bv,cv):
    for sh_v in shifts:
        for es in (-1,1):
            for ss in (-1,1): cand.add(tuple(es*Fr(e)+ss*Fr(t) for e,t in zip(edge,sh_v)))
out=[sum((q(t)*z for t,z in zip(v,logs5)), arb(0)) for v in cand if any(v) and v!=bv]
out=[x for x in out if float(x)>1e-30 and float(a9-x)>1e-30]
out.sort(key=float)
edges = [arb(0)] + out + [a9]
at8 = next(i for i, x in enumerate(edges) if abs(float(x - a8)) < 1e-20)

panels = []
for i in range(len(edges)-1):
    lo, hi = edges[i], edges[i+1]
    core = (i < at8)
    if i == at8 - 1 or i == len(edges) - 2:
        for k_dy in range(120):
            panels.append((hi - (hi-lo)*arb(2)**(-k_dy), hi - (hi-lo)*arb(2)**(-k_dy-1), core, i))
    else:
        panels.extend((lo+(hi-lo)*j/4, lo+(hi-lo)*(j+1)/4, core, i) for j in range(4))

N_GL = 192
gl_nodes = [arb.legendre_p_root(N_GL, k, weight=True) for k in range(N_GL)]
def powers_arb(x, n):
    res_p = [arb(1)]
    for _ in range(1, n): res_p.append(res_p[-1]*x)
    return res_p

maxdeg = max(m.nrows() for m in old.global_matrices.values())
phi_col = columns(old.phi)
z_core_col = columns([f(arb_poly([0, a8/a9])) for f in old.z])
local96_col = columns([f(arb_poly([(a8+a9)/(2*a9), hs/(2*a9)])) for f in old.z] + old.local, 96)
s2a = (2*a9).sqrt()

cell_cache = {}
raw_287 = arb_mat(287, NM + 2)
Phi_g = arb_mat(191, NM)
bare_z = arb_mat(4, NM)
bare_FJ = arb_mat(96, NM)
P0_g = arb_mat(12, NM)
raw_hB = arb_mat(12, NM + 2)
mc_g = [arb(0)]*NM
eg_raw_g = [arb(0)]*NM

t1 = time.monotonic()
for panel_index, (lo, hi, core, cell_i) in enumerate(panels):
    if panel_index % 16 == 0: print('x panels',panel_index,'/',len(panels),flush=True)
    deadline()
    mid = (lo + hi)/2; half = (hi - lo)/2
    terms = []
    for n, prime in res.channels:
        for sign in (-1, 1):
            sh_a = sign * res.logs[n]; y = mid + sh_a; wt = arb(prime).log()/arb(n).sqrt()
            if float(y - (-a9)) > 0 and float(a9 - y) > 0: terms.append((wt, sh_a, 'core'))
            elif float(y - a9) > 0 and float(b - y) > 0: terms.append((wt, sh_a, 'plus'))
            elif float(y - (-b)) > 0 and float(-a9 - y) > 0: terms.append((wt, sh_a, 'minus'))
    xs = []; ws = []; gs_rows = []; ms_l = []; tx9_l = []; h_rows = []
    if core and cell_i not in cell_cache:
        pp = old.prime_polys(edges[cell_i], edges[cell_i+1])
        pp_mat = columns(pp, old.global_matrices[None].nrows())
        dp_arb = [arb_poly(p) for p in res.Dpoly]
        mid_c = (edges[cell_i] + edges[cell_i+1])/2
        for ii, fj in enumerate(res.funcs):
            for term in fj['D']['shift_terms']:
                sh = res.logs[int(term['channel'])]/a9
                dl, dh = (arb(0), 1-sh) if int(term['translation_sign'])==1 else (max(arb(0), sh-1), arb(1))
                if float(mid_c/a9 - dl) > 0 and float(dh - mid_c/a9) > 0:
                    pp_t = arb_poly(list(map(q, term['polynomial'])))
                    for jj in range(12): dp_arb[jj] += res.T[ii,jj]*pp_t
        cell_cache[cell_i] = (pp_mat, w_polys(dp_arb, B_arb))
    for z_gl, w_gl in gl_nodes:
        x = mid + half*z_gl; w_dx = half*w_gl
        xs.append(x); ws.append(w_dx); mx = (x/2).cosh(); ms_l.append(mx); tx9_l.append(x/a9)
        ep = (x/2).exp()
        ms_v = (ep*(res.jp(a9-x)+res.jm(a9+x)) + (1/ep)*(res.jm(a9-x)+res.jp(a9+x)))/2
        logm = (b-x).log() - (a9-x).log(); logp = (b+x).log() - (a9+x).log()
        crow = []
        for idx_m, (m, P, Ac, gam, quot, P_neg, quot_neg) in enumerate(mode_data):
            shell = (P(x)*logm + quot(x) + P_neg(x)*logp + quot_neg(x))/2 + gam(x)
            pr = sum((wt*(Ac*((x+sh_a)/2).cosh() if kind=='core' else P(x+sh_a) if kind=='plus' else P_neg(x+sh_a)) for wt, sh_a, kind in terms), arb(0))
            gx = Ac*ms_v - shell - pr
            crow.append(gx)
            if core:
                mc_g[idx_m] += w_dx * gx * mx
                eg_raw_g[idx_m] += w_dx * gx
        gs_rows.append(crow)
        if core:
            dps_w = cell_cache[cell_i][1]
            vlog = -((a9-x).log() + (a9+x).log() - 2*a9.log())/2
            hrow = []
            for j in range(12):
                hv = hB_ac[j]*ms_v - (hB_ell[j](x)*logm + hB_quot[j](x) + hB_ner[j](x)*logp + hB_qn[j](x))/2 - hB_gam[j](x)
                hv -= (dps_w[j](x/a9) + hB_dv[j](x/a9)*vlog + hB_dm[j]*mx)/s2a
                hv -= sum((wt*(hB_ac[j]*((x+sh_a)/2).cosh() if kind=='core' else hB_ell[j](x+sh_a) if kind=='plus' else hB_ner[j](x+sh_a)) for wt, sh_a, kind in terms), arb(0))
                hrow.append(hv)
            h_rows.append(hrow)
    P0_mat = arb_mat([[f(tx) for f in P0_polys] for tx in tx9_l])
    WG = arb_mat([[ws[k]*gs_rows[k][m] for m in range(NM)] for k in range(N_GL)])
    P0_g += 2 * P0_mat.transpose() * WG
    if core:
        pp_mat = cell_cache[cell_i][0]
        V_mat = arb_mat([[ws[k]*v for v in (gs_rows[k] + [ms_l[k], arb(1)])] for k in range(N_GL)])
        H_mat = arb_mat(h_rows)
        raw_hB += H_mat.transpose() * V_mat
        ts = [x/a8 for x in xs]
        PV = arb_mat([powers_arb(t, maxdeg) for t in ts])
        for tag, co in old.global_matrices.items():
            mat_c = co + pp_mat if tag is None else co
            nr = mat_c.nrows()
            if tag is None:
                mom = sub(PV, range(N_GL), range(nr)).transpose() * V_mat
                base_g = sub(mom, range(nr), range(NM))
            else:
                lfac = [abs(t - old.roots[tag]).log() for t in ts]
                V_log = arb_mat([[lfac[k]*V_mat[k, c] for c in range(NM+2)] for k in range(N_GL)])
                mom = sub(PV, range(N_GL), range(nr)).transpose() * V_log
            raw_287 += mat_c.transpose() * mom
        Phi_g += 2 * phi_col.transpose() * sub(base_g, range(phi_col.nrows()), range(NM))
        bare_z += 2 * z_core_col.transpose() * sub(base_g, range(z_core_col.nrows()), range(NM))
    else:
        uv = [(2*x - a8 - a9)/hs for x in xs]
        PVs = arb_mat([powers_arb(u, 96) for u in uv])
        mom_s = PVs.transpose() * WG
        bare_FJ += 2 * local96_col.transpose() * mom_s
print(f"[2] x-integration done in {time.monotonic()-t1:.2f}s", flush=True)

t2 = time.monotonic()
ps_B = [sum((ell20[i]*B_arb[i,j] for i in range(12)), arb_poly([])) for j in range(12)]
ac_B = [-sum((lam20[i]*B_arb[i,j] for i in range(12)), arb(0))/mu9 for j in range(12)]
ends = [(-b, -a9), (-a9, a9), (a9, b)]
all_P = ps_B + [md[1] for md in mode_data]
all_ac = ac_B + [md[2] for md in mode_data]
px_all = [[p(arb_poly([0,-1])), None, p] for p in all_P]

def ep_primitive(p, sign):
    ans = p*(2*sign); d_p = p
    for k_i in range(1, len(p)):
        d_p = d_p.derivative(); ans += d_p*((-1)**k_i*(2*sign)**(k_i+1))
    return ans

def eval_corr_at_r(r):
    out_m = [[arb(0), arb(0)] for _ in range(14)]
    for i, (ai, bi) in enumerate(ends):
        for j, (aj, bj) in enumerate(ends):
            lo_x = max(ai, aj - r); hi_x = min(bi, bj - r)
            if float(hi_x - lo_x) <= 0: continue
            if i == 1 and j == 1:
                v = ((hi_x+r/2).sinh() - (lo_x+r/2).sinh() + (hi_x-lo_x)*(r/2).cosh())/2
                for c_m in range(2):
                    ac_y = all_ac[12+c_m]
                    for r_k in range(14):
                        out_m[r_k][c_m] += all_ac[r_k]*ac_y*v
            elif i != 1 and j != 1:
                for c_m in range(2):
                    shift_y = px_all[12+c_m][j](arb_poly([r, 1]))
                    for r_k in range(14):
                        Q_int = (px_all[r_k][i] * shift_y).integral()
                        out_m[r_k][c_m] += Q_int(hi_x) - Q_int(lo_x)
            else:
                for c_m in range(2):
                    for r_k in range(14):
                        pol = px_all[12+c_m][j](arb_poly([r, 1])) if i == 1 else px_all[r_k][i]
                        sh_e = arb(0) if i == 1 else r
                        coef = all_ac[r_k] if i == 1 else all_ac[12+c_m]
                        for sign in (1, -1):
                            Q_int = ep_primitive(pol, sign)
                            vv = (hi_x*sign/2).exp()*Q_int(hi_x) - (lo_x*sign/2).exp()*Q_int(lo_x)
                            out_m[r_k][c_m] += coef/2 * (sh_e*sign/2).exp() * vv
    return out_m

r_panels = [(h*arb(2)**(-k_d), h*arb(2)**(-k_d+1)) for k_d in range(120, 0, -1)]
for left, right in ((h, 2*a9), (2*a9, a9+b), (a9+b, 2*b)):
    lo_r = left
    while float(2*lo_r - right) < 0:
        r_panels.append((lo_r, 2*lo_r)); lo_r = 2*lo_r
    r_panels.append((lo_r, right))

N_GL_R = 96
gl_r = [arb.legendre_p_root(N_GL_R, k, weight=True) for k in range(N_GL_R)]
C0 = [[arb(0), arb(0)] for _ in range(14)]
for im, m1 in enumerate(MODES):
    for jn, m2 in enumerate(MODES):
        C0[12+im][jn] = (arb(1) if im==jn else arb(0)) - 4*lam20[m1]*lam20[m2]/d_norm

Q_arb = [[arb(0), arb(0)] for _ in range(14)]
for panel_index, (lo_r, hi_r) in enumerate(r_panels):
    if panel_index % 16 == 0: print('correlation panels',panel_index,'/',len(r_panels),flush=True)
    deadline()
    mr = (lo_r+hi_r)/2; hr = (hi_r-lo_r)/2
    for zr, wr in gl_r:
        rv = mr + hr*zr
        ker = 2 * (-rv/2).exp() / (1 - (-2*rv).exp()) * hr * wr
        Cr = eval_corr_at_r(rv)
        for rk in range(14):
            for cm in range(2):
                Q_arb[rk][cm] += ker * (C0[rk][cm] - Cr[rk][cm])

tail_2b = ((1 + (-b).exp())/(1 - (-b).exp())).log() + 2*((-b).exp()).atan()
const_c = (8*arb.pi()).log() + arb.const_euler() + arb.pi()/2
for rk in range(14):
    for cm in range(2):
        Q_arb[rk][cm] += C0[rk][cm] * (tail_2b - const_c)
for n, prime in res.channels:
    rv = arb(n).log(); wt = 2*arb(prime).log()/arb(n).sqrt()
    Cr = eval_corr_at_r(rv)
    for rk in range(14):
        for cm in range(2):
            Q_arb[rk][cm] -= wt * Cr[rk][cm]

dB_arb = arb_mat([Q_arb[rk] for rk in range(12)])
D2_arb = arb_mat([Q_arb[12+rk] for rk in range(2)])
print(f"[3] Exact arb dB & D2 done in {time.monotonic()-t2:.2f}s", flush=True)

# Validate dB[:,0] against DIRECT12_RESULT.json!

# Current November-1 Schur inverse; never substitute the old October inverse.
prepared=native(HERE/'assets/PREPARED_CORE.json.gz')
savedq=native(NATIVEPATH)
C=midpoint(prepared['C']);d=q('19/10')
z1=midpoint(prepared['solution12_preconditioned']);zq=midpoint(savedq['solutionq_preconditioned'])
src=inp.json('old_sources')['cases'][0]
cf=midpoint(mat(src['old_certificate']['source_c_model']))
cj=midpoint(mat(src['galerkin']['old_low_c_model']))
bf=midpoint(mat(src['old_certificate']['source_Bh_model']))
bj=midpoint(mat(src['galerkin']['old_low_Bh_model']))
VF=C.transpose()*(cf-bf/d);VJ=C.transpose()*(cj-bj/d)
hist=read_json(HERE/'assets/historical_pairs.raw')
ch=midpoint(mat(hist['Phi_star_h']))*B_arb
bh=midpoint(sub(mat(hist['high_cross_models']),range(191),range(12)))*B_arb
VH=C.transpose()*(ch-bh/d)
V=arb_mat([[VF[i,j] if j<12 else VJ[i,j-12] if j<96 else VH[i,j-96] for j in range(108)] for i in range(191)])
scale8=(arb(2)/a8).sqrt();me8=(2*a8).sqrt()*mellin(0,a8);gamma_a=2*mu8/(me8*me8)
eh=[eg_raw_g[m]*scale8-mc_g[m]*me8/mu8 for m in range(NM)]
rawF=sub(raw_287,range(191,287),range(NM+2))
lowF=midpoint(sub(old.low,range(191),range(191,287)))
HF=arb_mat([[2*(rawF[i,m]-rawF[i,NM]*mc_g[m]/mu8)+gamma_a*eh[m]*(rawF[i,NM+1]*scale8-rawF[i,NM]*me8/mu8) for m in range(NM)]for i in range(96)])-lowF.transpose()*Phi_g
HH=arb_mat([[2*(raw_hB[i,m]-raw_hB[i,NM]*mc_g[m]/mu8)+gamma_a*eh[m]*(raw_hB[i,NM+1]*scale8-raw_hB[i,NM]*me8/mu8) for m in range(NM)]for i in range(12)])-ch.transpose()*Phi_g
bare=arb_mat([[bare_FJ[i,m]+(bare_z[i,m] if i<4 else -2*old.lam[i-4]*mc_g[m]/mu8) for m in range(NM)]for i in range(96)])
direct=arb_mat([[bare[i,m] if i<96 else dB_arb[i-96,m]-P0_g[i-96,m] for m in range(NM)]for i in range(108)])
high=arb_mat([[HF[i,m] if i<96 else HH[i-96,m] for m in range(NM)]for i in range(108)])
first=sub(direct-high/d,range(108),[0])-V.transpose()*z1
k=q('13619/125000')
second=sub(direct-high/d,range(108),[1])-sub(direct-high/d,range(108),[0])*k-V.transpose()*zq
# Preserve evaluated balls; their radii cover arithmetic only, NOT quadrature/model errors.
model_cache.save(OUT/'ASSEMBLED_VECTORS.json.gz',{'first':first,'second':second,'Phi_g':Phi_g,'mc_g':mc_g,'V':V},hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),spec)
cb=read_json(BANKDIR/'COMMON_BANK_109.json.gz');den=q(cb['denominator'])
M109=arb_mat([[q(x)/den for x in row]for row in cb['M_model_integer']])
M=sub(M109,range(108),range(108));bank_first=sub(M109,range(108),[108])
fc=read_json(BANKDIR/'FIRST_COLUMN_COORDINATES.json')
w1=arb_mat([[q(row[0])]for row in fc['shell96']+fc['outer12_B_coordinates_z']])
scalar=read_json(ROOT/'work/zweite_restspalte_20261111/SECOND_SCALAR_RESULT.json')
lam=q(scalar['lambda_bar2']['rational'])
eta=midpoint(second)-M*w1*lam
diff=midpoint(first)-bank_first
# Positive LDL and a single solve in the complete 108-dimensional bank.
L=[[arb(int(i==j)) for j in range(108)]for i in range(108)];pivots=[]
for i in range(108):
    pivot=M[i,i]-sum((L[i][j]**2*pivots[j] for j in range(i)),arb(0))
    assert pivot>0,('NONPOSITIVE_MODEL_PIVOT',i,str(pivot));pivots.append(pivot)
    for r in range(i+1,108):L[r][i]=(M[r,i]-sum((L[r][j]*L[i][j]*pivots[j] for j in range(i)),arb(0)))/pivot
rhs=arb_mat([[eta[i,0],diff[i,0]]for i in range(108)]);sol=M.solve(rhs)
energy=(eta.transpose()*sub(sol,range(108),[0]))[0,0]
control2=(diff.transpose()*sub(sol,range(108),[1]))[0,0]
control=control2.sqrt();component=max(abs(diff[i,0])for i in range(108))
solve_defect=max(abs((M*sol-rhs)[i,j])for i in range(108)for j in range(2))
valid=component<q('1e-12') and control<q('1e-6') and energy>0
status='INCONCLUSIVE_CONTROL_FAILED'
if valid:
    status='DIAGNOSTIC_SINGLE_WITNESS_STOP' if energy>q('0.2573') else 'DIAGNOSTIC_ROUTE_OPEN' if energy>=q('0.05') else 'DIAGNOSTIC_BELOW_EXPECTED_RANGE'
result={**spec,'status':status,'elapsed_seconds':time.monotonic()-t0,'energy_model_108':number(energy),'arithmetic_radius_only':radius(energy),'first_column_max_component_difference':number(component),'first_column_difference_dual_norm':number(control),'linear_solve_max_defect':number(solve_defect),'min_LDL_pivot':number(min(pivots)),'controls_pass':bool(valid),'projection_coefficient_lambda_bar2':number(lam),'interpretation':'Finite frozen model diagnostic only. Physical rest-form identification and full model/quadrature/error transport are not certified. No result for infinite complement. No automatic follow-up.'}
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
