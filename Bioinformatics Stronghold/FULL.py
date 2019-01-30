# FULL - http://rosalind.info/problems/full/
import numpy as np
import pprint

aa_mass_table = {   71.03711: 'A',
                    103.00919: 'C',
                    115.02694: 'D',
                    129.04259: 'E',
                    147.06841: 'F',
                    57.02146: 'G',
                    137.05891: 'H',
                    113.08406: 'I',
                    128.09496: 'K',
                    113.08406: 'L',
                    131.04049: 'M',
                    114.04293: 'N',
                    97.05276: 'P',
                    128.05858: 'Q',
                    156.10111: 'R',
                    87.03203: 'S',
                    101.04768: 'T',
                    99.06841: 'V',
                    186.07931: 'W',
                    163.06333: 'Y'
                }

def is_aa_mass(a, b, epsilon=0.001):
    diff = abs(a-b)
    for p in aa_mass_table.keys():
        if abs(p - diff) < epsilon:
            return (1, aa_mass_table[p])
    return 0, ''

f = open('datasets/rosalind_full.txt')

parent = float(f.readline().strip())
ions = []
for line in f:
    ions.append(float(line.strip()))
ions.sort()
peaks = list(ions)
path = []

print(parent)
print(ions)
m = len(ions)
n = int(m/2) - 1

# Creating Edge Graph
E = np.zeros((m, m))
AA = np.chararray((m,m), unicode=True)
for i in range(m):
    for j in range(m):
        E[i, j], AA[i, j]= is_aa_mass(ions[i], ions[j])
print(E)
print(AA)

beginning = i = 0
while len(path) < n:
    for j in range(i, m):
        if j == m:
            path = []
            peaks = list(ions)
            i = beginning + 1
            beginning += 1
            break
        p, aa = is_aa_mass(ions[i], ions[j])
        if p:
            path.append(aa)
            del peaks[m-1-i]
            i = j
            break

print(''.join(path))

f.close()