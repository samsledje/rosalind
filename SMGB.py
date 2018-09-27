# SMGB - http://rosalind.info/problems/SMGB
from math import inf
import numpy as np

score_matrix = np.asarray([ [1, -1, -1, -1, -1],
                            [-1, 1, -1, -1, -1],
                            [-1, -1, 1, -1, -1],
                            [-1, -1, -1, 1, -1],
                            [-1, -1, -1, -1, inf]
])

char_dict = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

f = open('datasets/rosalind_smgb.txt')
seq = []
for line in f:
    if line.startswith('>'):
        if len(seq) != 0:
            x = ''.join(seq)
            seq = []
    else:
        seq.append(line.strip())
y = ''.join(seq)

m = len(x)
n = len(y)

M = np.zeros((m+1, n+1))

for i in range(1, m+1):
    for j in range(1, n+1):
        x_ind = char_dict[x[i-1]]
        y_ind = char_dict[y[j-1]]
        M[(i, j)] = max(
            M[(i-1, j)] + score_matrix[(x_ind, 4)],
            M[(i-1, j-1)] + score_matrix[(x_ind, y_ind)],
            M[(i, j-1)] + score_matrix[(4, y_ind)],
            )

print('single loops')
for i in range(1, m+1):
    x_ind = char_dict[x[i-1]]
    y_ind = char_dict[y[n-1]]
    M[(i, n)] = max(
        M[(i, n-1)] + score_matrix[(x_ind, 4)],
        M[(i-1, n)],
        M[(i-1, n-1)] + score_matrix[(x_ind, y_ind)]
        )

for j in range(1, n+1):
    x_ind = char_dict[x[m-1]]
    y_ind = char_dict[y[j-1]]
    M[(m, j)] = max(
        M[(m-1, j)] + score_matrix[(4, y_ind)],
        M[(m, j-1)],
        M[(m-1, j-1)] + score_matrix[(x_ind, y_ind)]
        )

M[(m,n)] = max(M[(m-1, n)], M[(m-1,n-1)], M[(m,n-1)])

i = m
j = n
x_prime = y_prime = ""

print('backtracking')
while i > 0 or j > 0:
    x_ind = char_dict[x[i-1]]
    y_ind = char_dict[y[j-1]]
    if (i == m or i == 0) and M[(i, j-1)] == M[(i, j)]:
        x_prime = '-' + x_prime
        y_prime = y[j-1] + y_prime
        j -= 1
    elif (j == n or j == 0) and M[(i-1, j)] == M[(i, j)]:
        x_prime = x[i-1] + x_prime
        y_prime = '-' + y_prime
        i -= 1
    elif M[(i-1, j-1)] + score_matrix[(x_ind, y_ind)] == M[(i, j)]:
        x_prime = x[i-1] + x_prime
        y_prime = y[j-1] + y_prime
        i -= 1
        j -= 1
    elif M[(i, j-1)] + score_matrix[(4, y_ind)] == M[(i, j)]:
        x_prime = '-' + x_prime
        y_prime = y[j-1] + y_prime
        j -= 1
    else:
        x_prime = x[i-1] + x_prime
        y_prime = '-' + y_prime
        i -= 1

outfile = open('smgb_result.txt', 'w+')
outfile.write(str(int(M[(m, n)])))
outfile.write('\n')
outfile.write(x_prime)
outfile.write('\n')
outfile.write(y_prime)
outfile.close()
# print(int(M[(m, n)]))
# print(x_prime)
# print(y_prime)

