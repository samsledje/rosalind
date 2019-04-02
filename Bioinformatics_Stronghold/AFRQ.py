# AFRQ - http://rosalind.info/problems/afrq/
import math

with open('datasets/rosalind_afrq.txt', 'r') as f:
    A = [float(k) for k in f.readline().strip().split()]

soln = []
for k in A:
    p2 = math.sqrt(k)
    p1 = 1 - p2
    f22 = p2 ** 2
    f12 = 2 * p1 * p2
    soln.append(str(f12 + f22))

print(' '.join(soln))

# One Line Solution
#print(' '.join([(str(float(k) + (2 * (1-(float(k) ** 0.5)) * (float(k) ** 0.5)))) for k in open('datasets/test.txt', 'r').readline().strip().split()]))
