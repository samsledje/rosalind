# WFMD - http://rosalind.info/problems/wfmd/
from numpy import asarray, exp, where
from scipy.misc import comb

def wfmd(N,m,g,k):
    p = m / (2*N)
    q = 1-p

    proba = [comb(2*N, i) * ((q) ** i) * (p) ** (2*N - i) for i in range(1, 2 * N + 1)]
    
    # Determine the probabiliy of a given of recessive allels in the 2nd to k-th generations.
    # Use the total law of probability, along with the probabilities from the previous generation.
    # i.e., P(1 Rec) = P(1 Rec | 0 Rec in previous gen) +  P(1 Rec | 1 Rec in previous gen) + ... + P(1 Rec | 2N Rec in previous gen)
    # Notice that the conditional probabilities are binomial terms, similar to the first generation calculations.
    for gen in range(2, g + 1):
        temp_p = []
        
        for j in range(1, 2 * N + 1):
            temp_term = [comb(2 * N, j) * ((x / (2.0 * N)) ** j) * \
                         (1.0 - (x / (2.0 * N))) ** (2 * N - j) for x in range(1, 2 * N + 1)]
            temp_p.append(sum([temp_term[i] * proba[i] for i in range(len(temp_term))]))
        proba = temp_p
    
    # Sum to get the desired probability. Note: We have k-1 due to omitting the 0th term.
    return(sum(proba[k-1:]))

if __name__ == '__main__':
    with open('datasets/test.txt','r') as f:
        N,m,g,k = (int(i) for i in f.readline().strip().split())

        print(wfmd(N,m,g,k))