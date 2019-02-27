# BA10J - http://rosalind.info/problems/ba10j/
import numpy as np
np.set_printoptions(suppress=True)
import math
# forward(k_i) * backward(k_i) / forward(sink)

#with open('datasets/test2.txt', 'r') as f:
with open('datasets/rosalind_ba10j.txt', 'r') as f:
    x = f.readline().strip()
    n = len(x)
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

# Output matricies
F = np.zeros((n,N), dtype=float)
B = np.zeros((n,N), dtype=float)
SD = np.zeros((n,N), dtype=float)

#Forward Probabilities
for q in range(N):
    F[0,q] = qstart_pr[q] * E[q, sigma.index(x[0])]

for i in range(1,n):
    for q in range(N):
        for qpr in range(N):
            F[i, q] += F[i-1, qpr] * A[qpr, q] * E[q, sigma.index(x[i])]

#Total Forward
fwd = 0
for q in range(N):
    fwd += F[n-1, q]

#Backward Probabilities
for q in range(N):
    B[n-1, q] = 1

for i in range(n-2, -1, -1):
    for q in range(N):
        for qpr in range(N):
            B[i, q] += B[i+1, qpr] * A[q, qpr] * E[qpr, sigma.index(x[i+1])]

#Combining
for i in range(n):
    for q in range(N):
        SD[i, q] = F[i, q] * B[i, q] / fwd

print(SD)
np.savetxt("BA10J.tsv", SD, delimiter="\t")