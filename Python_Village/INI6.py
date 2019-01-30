# INI6 - http://rosalind.info/problems/ini6/

f = open('datasets/rosalind_ini6.txt')
#f = open('datasets/test.txt')

l = f.readline().strip().split()
d = {}

for i in l:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

for i in d.keys():
    print(i, d[i])

f.close()