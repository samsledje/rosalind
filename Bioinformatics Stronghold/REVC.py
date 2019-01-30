# REVC - http://rosalind.info/problems/revc/

f = open('datasets/rosalind_revc.txt')
s = f.read().strip()

mapping = { 'A': 'T',
            'C': 'G',
            'G': 'C',
            'T': 'A'}

rev_comp = []

for l in s:
    rev_comp.append(mapping[l])

rev_comp.reverse()
print(''.join(rev_comp))

f.close()