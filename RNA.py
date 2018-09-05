# RNA - http://rosalind.info/problems/rna/

f = open('datasets/rosalind_rna.txt')
s = f.read().strip()

l = list(s)
for i in range(len(l)):
    if l[i] == 'T':
        l[i] = 'U'

print(''.join(l))