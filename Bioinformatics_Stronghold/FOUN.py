# FOUN - http://rosalind.info/problems/foun/
import numpy as np
from math import log10
from WFMD import wfmd

with open('datasets/test.txt','r') as f:
    N,m, = [int(i) for i in f.readline().strip().split()]
    A = [int(i) for i in f.readline().strip().split()]
    k = len(A)

B = np.zeros((m,k))

for i in range(m):
    for j in range(len(A)):
        x = 1-wfmd(N,2*N - A[j],i+1,1)
        B[i,j] = log10(x)

print(B)
