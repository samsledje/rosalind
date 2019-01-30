# DNA - http://rosalind.info/problems/dna/

f = open('datasets/rosalind_dna_1_dataset.txt')
s = f.read().strip()

a = c = g = t = 0

for i in s:
    if i == 'A':
        a += 1
    elif i == 'C':
        c += 1
    elif i == 'G':
        g += 1
    elif i == 'T':
        t += 1

print(a,c,g,t)

f.close()