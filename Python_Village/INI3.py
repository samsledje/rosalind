# INI3 - http://rosalind.info/problems/ini3/

f = open('datasets/rosalind_ini3.txt')
#f = open('datasets/test.txt')

s = f.readline().strip()
a,b,c,d = map(int, f.readline().strip().split())

print(s[a:b+1], s[c:d+1])

f.close()