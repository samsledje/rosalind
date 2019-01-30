# IPRB - http://rosalind.info/problems/prob/
import math

f = open('datasets/rosalind_prob.txt')
#f = open('datasets/test.txt')

s = list(f.readline().strip())
A = [float(i) for i in f.readline().strip().split()]
B = [0] * len(A)
pr_dict = {}

for i in range(len(A)):
    B[i] = round(s.count('A') * math.log10((1-A[i]) / 2) + s.count('C') * math.log10(A[i] / 2) + s.count('G') * math.log10(A[i] / 2) + s.count('T') * math.log10((1-A[i]) / 2), 3)

print(', '.join([str(i) for i in B]))