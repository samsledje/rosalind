# BA2C - http://rosalind.info/problems/ba2c/
import numpy as np
import math

nucleotide_map = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

def get_kmers(T, k):
    for i in range(len(T)-k):
        yield T[i:i+k]

def calc_kmer_pr(kmer,P):
    basepr = 1
    for i in range(len(kmer)):
        multpr = P[nucleotide_map[kmer[i]], i]
        basepr *= multpr
    return basepr

with open('datasets/rosalind_ba2c.txt', 'r') as f:
    T = f.readline().strip()
    k = int(f.readline().strip())
    P = [0,0,0,0]
    for i in range(4):
        P[i] = [float(j) for j in f.readline().strip().split()]

P = np.asarray(P)
kmer_probs = {}
for km in get_kmers(T,k):
    kmer_probs[km] = calc_kmer_pr(km, P)
print(max(kmer_probs.keys(), key=lambda k: kmer_probs[k]))