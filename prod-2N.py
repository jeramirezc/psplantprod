import numpy as np
import sys
import tqdm

def ini():
  global Npi, l, p, M, Xa, Xb, peff
  tmp=[]
  z=np.less(np.random.random((l,l)),peff)*1
  ci=np.count_nonzero(z==1)
  while len(tmp)!= Npi:
#    x=np.random.randint(0,l)
#    y=np.random.randint(0,l)
    r=map(lambda _:np.random.randint(0,l),range(2))
    if r not in tmp:
      tmp.append(r)
      x=r[0]
      y=r[1]
      if z[x][y]==1:
        z[x][y]+=-1
  return z, tmp, ci
  
def prop(x):
  xdir=x[0]
  ydir=x[1]
  xt=x0+xdir
  yt=y0+ydir
  if 0<=xt<l and 0<=yt<l:
    if z[xt][yt]==1:
      z[xt][yt]+=-1
      tmp.append([xt,yt])

p=0.05
l=int(sys.argv[1])
rep=20000
perc=float(sys.argv[2])
Npi=int(perc*l*l/100.)
Xa=int(sys.argv[3])
Xb=int(sys.argv[4])

dirs=[[0,1],[0,-1],[1,0],[-1,0]]

f=open('prod-3N-'+str(l)+'-'+str(perc)+'.dat','w')

for j in range(19):
  M=0.05
  for i in range(19):
    print i,j
    peff=(M*Xa+(1-M)*Xb)*p
    dam=0
    for w1 in tqdm.tqdm(range(rep)):
      z,propagadores,Nps=ini()
      while len(propagadores)!=0:
        tmp=[]
        for x in propagadores:
          x0=x[0]
          y0=x[1]
          map(prop,dirs)
        propagadores=tmp
      Npv=np.count_nonzero(z==1)
      dam=(i*dam+(Nps-Npv))/float(i+1)
#    print>>f, p, M, dam
    f.write("%f %f %f \n" % (p, M, p-dam/float(l*l)))
    M+=0.05
  p+=0.05


