# EVAL - http://rosalind.info/problems/eval/
from math import log10, factorial

f = open('datasets/rosalind_eval.txt')
#f = open('datasets/test.txt')

n = int(f.readline().strip())
s = f.readline().strip()
k = len(s)
A = list(map(float, f.readline().strip().split()))
B = [0] * len(A)

for i in range(len(A)):
    pr = 1.0
    gc = A[i] / 2
    at = (1 - A[i]) / 2
    for j in s:
        if j in "GC":
            pr *= gc
        else:
            pr *= at
    B[i] = str(round((n - k + 1) * pr, 4))

print(' '.join(B))

f.close()