# HAMM - http://rosalind.info/problems/hamm/

f = open('datasets/rosalind_hamm.txt')
s = f.readline().strip()
t = f.readline().strip()

assert len(s) == len(t), 'The two strings must be of equal length'

d = 0
for i in range(len(s)):
    if s[i] != t[i]:
        d += 1

print(d)

f.close()