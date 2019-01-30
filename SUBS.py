# SUBS - http://rosalind.info/problems/subs/

f = open('datasets/rosalind_subs.txt')
s = f.readline().strip()
t = f.readline().strip()

n = len(s)
m = len(t)
l = []

for i in range(n-m):
    if t == s[i:i+m]:
        l.append(str(i+1))

print(' '.join(l))