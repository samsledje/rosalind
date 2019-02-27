# BA10H - http://rosalind.info/problems/ba10h/
import numpy as np
import math


#with open('datasets/test2.txt', 'r') as f:
with open('datasets/rosalind_ba10h.txt', 'r') as f:
    x = f.readline().strip()
    f.readline()
    sigma = f.readline().strip().split()
    f.readline()
    pi = f.readline().strip()
    f.readline()
    Q = f.readline().strip().split()
    N = len(Q)
    n = len(x)
    r = len(sigma)

def n_in(small, large):
    #computes the number of times small appears in large
    c = 0
    s = len(small)
    L = len(large)
    for i in range(L-s+1):
        if large[i:i+s] == small:
            c += 1
    return c

def sig_in(q, sigma, x, pi):
    #computes the number of times q emitted sigma in sequence x, pi
    n = len(x)
    assert n == len(pi)
    c = 0
    for i in range(n):
        if pi[i] == q and x[i] == sigma:
            c += 1
    return c

A = np.zeros((N,N))
E = np.zeros((N,r))

# Compute A
for q in range(N):
    qsum = 0
    for qdp in range(N):
        qsum += n_in('{}{}'.format(Q[q],Q[qdp]), pi)
    for qpr in range(N):
        if qsum == 0:
            A[q,qpr] = 1/N
        else:
            A[q,qpr] = n_in('{}{}'.format(Q[q],Q[qpr]), pi) / qsum
print(A)

# Compute E
for q in range(N):
    sigsum = 0
    for spr in range(r):
        sigsum += sig_in(Q[q], sigma[spr], x, pi)
    for sig in range(r):
        if sigsum == 0:
            E[q, sig] = 1/r
        else:
            E[q,sig] = sig_in(Q[q], sigma[sig], x, pi) / sigsum
print(E)

with open("BA10H.tsv", "w+") as f:
    for q in range(N):
        f.write('\t'+Q[q]+'\t')
    for q in range(N):
        f.write('\n'+Q[q]+'\t')
        for qpr in range(N):
            f.write(str(A[q,qpr])+'\t')
    f.write("\n--------\n")
    for sig in range(r):
        f.write('\t'+sigma[sig]+'\t')
    for q in range(N):
        f.write('\n'+Q[q]+'\t')
        for sig in range(r):
            f.write(str(E[q,sig])+'\t')

