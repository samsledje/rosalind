# WFMD - http://rosalind.info/problems/wfmd/
from numpy import asarray, exp, where
from scipy.misc import comb

def wfmd(N,m,g,k):
    p = m / (2*N)
    q = 1-p
    k_target = k

    # 1st generation probabilities of exactly k copies of recessive
    proba = [comb(2*N, k) * (q**k) * (p**(2*N-k)) for k in range(1, 2*N+1)]
    
   # probabilities for exactly k copies of recessive for 2nd through gth generation
    for gen in range(2,g+1):
        gen_probas = []

        for k in range(1, 2*N+1):
            cond_k_probas = [comb(2*N, k) * ((i/(2*N))**k) * (1-(i/(2*N)))**(2*N-k) for i in range(1, 2*N+1)]
            k_proba = sum([cond_k_probas[j] * proba[j] for j in range(2*N)])
            gen_probas.append(k_proba)
        proba = gen_probas
    
    # probability of at least k recessive copies
    return(sum(proba[k_target-1:]))

if __name__ == '__main__':
    with open('datasets/rosalind_wfmd.txt','r') as f:
        N,m,g,k = (int(i) for i in f.readline().strip().split())

        print(wfmd(N,m,g,k))