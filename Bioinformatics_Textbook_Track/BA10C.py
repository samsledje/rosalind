# BA10C - http://rosalind.info/problems/ba10c/
import numpy as np
import math

with open('datasets/rosalind_ba10c2.txt', 'r') as f:
    s = f.readline().strip()
    n = len(s)
    f.readline()
    sigma = f.readline().strip().split()
    r = len(sigma)
    f.readline()
    Q = f.readline().strip().split()
    N = len(Q)
    f.readline()
    f.readline()
    A = np.zeros((N,N), dtype=float)
    E = np.zeros((N,r), dtype=float)
    #qstart_pr = [1/N for i in range(N)]
    qstart_pr = [0.2, 0.4, 0.4]

    for i in range(N):
        trans_pr = [float(k) for k in f.readline().strip().split()[1:]]
        for j in range(N):
            A[i,j] = trans_pr[j]
    f.readline()
    f.readline()

    for i in range(N):
        emiss_pr = [float(k) for k in f.readline().strip().split()[1:]]
        for j in range(r):
            E[i,j] = emiss_pr[j]

    print(A)
    print(E)
    print(qstart_pr)

V = np.zeros((N,n), dtype=np.float)
prev = np.zeros((N,n))

for j in range(N):
    c = sigma.index(s[0])
    V[j,0] = math.log(qstart_pr[j] * E[j,c])

for i in range(1,n):
    c = sigma.index(s[i])
    for j in range(N):
        V[j, i] = max([V[p,i-1] + math.log(A[p,j] * E[j,c]) for p in range(N)])
        prev[j,i] = np.argmax([V[p,i-1] + math.log(A[p,j] * E[j,c]) for p in range(N)])

y = [-1] * n
y[n-1] = np.argmax(V[:,n-1])
for i in range(n-1, 0, -1):
    y[i-1] = int(prev[y[i], i])
print(V)
import pandas as pd
pd.DataFrame(V).to_csv('test.csv', sep='&')
print(''.join([Q[i] for i in y]))
