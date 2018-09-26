# HAMM - http://rosalind.info/problems/GLOB
from math import inf
import numpy as np

score_matrix = {
    'A': {
        'A': 3,
        'C': -1,
        'G': -1,
        'T': -1,
        '-': -1
    },
    'C': {
        'A': -1,
        'C': 1,
        'G': -1,
        'T': -1,
        '-': -1
    },
    'G': {
        'A': -1,
        'C': -1,
        'G': 1,
        'T': -1,
        '-': -1
    },
    'T': {
        'A': -1,
        'C': -1,
        'G': -1,
        'T': 1,
        '-': -1
    },
    '-': {
        'A': 1,
        'C': -1,
        'G': -1,
        'T': -1,
        '-': inf
    }
}

f = open('test.txt')
f.readline()
x = f.readline().strip()
m = len(x)
f.readline()
y = f.readline().strip()
n = len(y)

M = np.zeros((m+1, n+1))
for i in range(1, m+1):
    M[(i, 0)] = M[(i-1, 0)] + score_matrix[x[i-1]]['-']

for j in range(1, n+1):
    M[(0, j)] = M[(0, j-1)] + score_matrix['-'][y[j-1]]

for i in range(1, m+1):
    for j in range(1, n+1):
        M[(i, j)] = max(
            M[(i-1, j)] + score_matrix[x[i-1]]['-'],
            M[(i-1, j-1)] + score_matrix[x[i-1]][y[j-1]],
            M[(i, j-1)] + score_matrix['-'][y[j-1]],
        )

print(M)

i = m
j = n
x_prime = y_prime = ""

while i > 0 or j > 0:
    if M[i-1][j-1] + score_matrix[x[i-1]][y[j-1]] == M[i][j]:
        x_prime = x[i-1] + x_prime
        y_prime = y[j-1] + y_prime
        i -= 1
        j -= 1
    elif M[i][j-1] + score_matrix['-'][y[j-1]] == M[i][j]:
        x_prime = '-' + x_prime
        y_prime = y[j-1] + y_prime
        j -= 1
    else:
        x_prime = x[i-1] + x_prime
        y_prime = '-' + y_prime
        i -= 1

print(x_prime)
print(y_prime)
