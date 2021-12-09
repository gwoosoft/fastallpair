import numpy as np
import math
from matplotlib import pyplot as plt



mt=float(math.inf)

def init(lnew):
  n, m=lnew.shape
  for i in range(n):
    for j in range(m):
      lnew[i][j]=mt

def extends(l,w):
  n, m=l.shape
  lnew=np.zeros((6,6))

  for i in range(n):
    for j in range(n):
      lnew[i][j]=mt
      for k in range(n):
        lnew[i][j]=min(lnew[i][j], l[i][k]+w[k][j])

  return lnew


def fastp(w):
  n, x=w.shape
  l=w
  m=1
  while m<n-1:
    print(l)
    lnew=np.zeros((6,6))
    lnew=extends(l,l)
    l=lnew
    
    m=2*m
  return l


l=np.zeros((6,6))
dp=[[0,mt,mt,mt,-1, mt],
    [1, 0, mt,2,mt, mt],
    [mt, 2, 0, mt, mt,-8],
    [-4,mt,mt,0,3,mt],
    [mt, 7, mt, mt, 0, mt],
    [mt,5,10,mt,mt, 0]
    ]

for i in range(6):
  for j in range(6):
    l[i][j]=dp[i][j]



#print(l)

res=fastp(l)
print(res)
