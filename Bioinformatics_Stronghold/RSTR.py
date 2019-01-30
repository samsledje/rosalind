# RSTR - http://rosalind.info/problems/rstr/
from math import log10

f = open('datasets/rosalind_rstr.txt')
#f = open('datasets/test.txt')

line = f.readline().strip().split()
N = int(line[0])
x = float(line[1])
s = f.readline().strip()

gc = x / 2
at = (1-x) / 2
occur_pr = 1.0

for i in s:
    if i in "GC":
        occur_pr *= gc
    elif i in "AT":
        occur_pr *= at

not_pr = 1 - occur_pr
never_pr = round(not_pr ** N, 3)


print(1 - never_pr)

f.close()