# BA10K - http://rosalind.info/problems/ba10k/
import numpy as np
import math


with open('datasets/test.txt', 'r') as f:
#with open('datasets/rosalind_ba10k.txt', 'r') as f:
    I = int(f.readline().strip())
    f.readline()
    x = f.readline().strip()
    f.readline()
    sigma = f.readline().strip().split()
    f.readline()
    Q = f.readline().strip().split()
    f.readline()
    f.readline()
    N = len(Q)
    r = len(sigma)
    n = len(x)
    A = np.zeros((N,N), dtype=float)
    E = np.zeros((N,r), dtype=float)
    qstart_pr = [1/N for i in range(N)]

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

# Forward & Backward matricies
F = np.zeros((n,N), dtype=float)
B = np.zeros((n,N), dtype=float)
Nqqp = np.zeros((N,N), dtype=float)
Nqsig = np.zeros((N,r), dtype=float)

#Forward Probabilities
for q in range(N):
    F[0,q] = qstart_pr[q] * E[q, sigma.index(x[0])]

for i in range(1,n):
    for q in range(N):
        for qpr in range(N):
            F[i, q] += F[i-1, qpr] * A[qpr, q] * E[q, sigma.index(x[i])]

#Backward Probabilities
for q in range(N):
    B[n-1, q] = 1

for i in range(n-2, -1, -1):
    for q in range(N):
        for qpr in range(N):
            B[i, q] += B[i+1, q] * A[q, qpr] * E[q, sigma.index(x[i])]

#Compute Pr(X=x)
prx = sum([F[n-1,q] for q in range(N)])
print(prx)

for _ in range(1):
    # Compute Nqqp
    for q in range(N):
        for qpr in range(N):
            print(F[i,q] * A[q,qpr] * E[qpr,sigma.index(x[i])] * B[i,q] / prx)
            s = sum([F[i,q] * A[q,qpr] * E[qpr,sigma.index(x[i])] * B[i,q] for i in range(n)])
            Nqqp[q,qpr] = s / prx

    # Compute Nqsig
    for q in range(N):
        for sig in range(r):
            s = 0
            for i in range(n):
                if sigma[sig] == x[i]:
                    s += F[i,q] * B[i,q]
    print(Nqsig, Nqqp)
    # Update A
    for q in range(N):
        qsum = sum([Nqqp[q,qdp] for qdp in range(N)])
        for qpr in range(N):
                A[q,qpr] = Nqqp[q,qpr] / qsum

    # Update E
    for q in range(N):
        sigsum = sum([Nqsig[q,spr] for spr in range(r)])
        for sig in range(r):
                E[q,sig] = Nqsig[q,sig]


