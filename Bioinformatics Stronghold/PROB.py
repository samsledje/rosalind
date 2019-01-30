# PROB - http://rosalind.info/problems/prob/
from math import log10

f = open('datasets/rosalind_prob.txt')
#f = open('datasets/test.txt')

s = list(f.readline().strip())
A = [float(i) for i in f.readline().strip().split()]
B = [0] * len(A)
pr_dict = {}

for i in range(len(A)):
    B[i] = round(s.count('A') * log10((1-A[i]) / 2) + s.count('C') * log10(A[i] / 2) + s.count('G') * log10(A[i] / 2) + s.count('T') * log10((1-A[i]) / 2), 3)

assert(len(B) == len(A))
print(' '.join(map(str, B)))

f.close()
