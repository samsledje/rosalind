# BA2G - http://rosalind.info/problems/ba2g/
import math
import numpy as np
from random import randint

nucleotide_map = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

def get_kmers(T, k):
    return [T[i:i+k] for i in range(len(T)-k+1)]

def get_random_kmer(T, k):
    i = randint(0,len(T)-k)
    return T[i:i+k]

def profile_random_kmer(T, P, k):
    all_kmers = list(get_kmers(T, k))
    probas = [calc_kmer_pr(i, P) for i in all_kmers]
    probas = np.asarray(probas)
    pr_dist = probas / probas.sum()
    return np.random.choice(all_kmers, p=pr_dist)

def calc_kmer_pr(kmer, P):
    basepr = 1
    for i in range(len(kmer)):
        multpr = P[nucleotide_map[kmer[i]], i]
        basepr *= multpr
    return basepr

def calc_profile_matrix(motifs, k):
    pfm = np.ones((4, k))
    for i in range(k):
        for m in motifs:
            pfm[nucleotide_map[m[i]],i] += 1
    return pfm / pfm.sum(axis=0)

def score_motifs(motifs):
    score = 0
    k = len(motifs[0])
    pfm = np.ones((4, k))
    for i in range(k):
        for m in motifs:
            pfm[nucleotide_map[m[i]],i] += 1
    for c in range(k):
        score += pfm[:,c].sum() - pfm[:,c].max()
    return score

def GibbsSampler(Dna, k, t, N):
    # Randomly select kmers
    motifs = [get_random_kmer(T,k) for T in Dna]
    best_motifs = motifs.copy()
    best_score = score_motifs(best_motifs)
    for _ in range(N):
        #print('{}/{}'.format(l,N))
        # Randomly pick which motif to replace
        i = randint(0, t-1)
        # Calculate profile matrix with all but Motifs[i]
        profile_motifs = [motifs[j] for j in range(len(motifs)) if j != i]
        P = calc_profile_matrix(profile_motifs, k)
        # Resign Motifs[i] as a profile random kmer
        motifs[i] = profile_random_kmer(Dna[i], P, k)
        # If score is lower replace best motifs
        score = score_motifs(motifs)
        if score < best_score:
            best_motifs = motifs.copy()
            best_score = score
    return best_motifs, best_score

def multipleGibbsSampler(Dna,k,t,N,R):
    best_motifs = [get_random_kmer(T,k) for T in Dna]
    best_score = score_motifs(best_motifs)
    for i in range(R):
        print('{}/{}'.format(i+1,R))
        motifs, score = GibbsSampler(Dna,k,t,N)
        if score < best_score:
            best_motifs = motifs
            best_score = score
    return best_motifs

with open('datasets/rosalind_ba2g.txt', 'r') as f:
#with open('datasets/test.txt', 'r') as f:
    k, t, N = (int(i) for i in f.readline().strip().split())
    Dna = []
    for _ in range(t):
        Dna.append(f.readline().strip())

m = multipleGibbsSampler(Dna,k,t,N,20)
for motif in m:
    print(motif)
