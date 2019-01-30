# IPRB - http://rosalind.info/problems/prob/
import math

f = open('datasets/rosalind_prob.txt')
#f = open('datasets/test.txt')

s = f.readline().strip()
A = [float(i) for i in f.readline().strip().split()]
B = [0] * len(A)
pr_dict = {}

for i in range(len(A)):
    gc_con = A[i]
    pr_dict['C'] = pr_dict['G'] = gc_con / 2
    pr_dict['A'] = pr_dict['T'] = (1 - gc_con) / 2
    pr_s = 0
    for j in s:
        pr_s += math.log10(pr_dict[j])
    B[i] = round(pr_s, 3)

print(', '.join([str(i) for i in B]))