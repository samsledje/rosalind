# INI4 - http://rosalind.info/problems/ini4/

f = open('datasets/rosalind_ini4.txt')
#f = open('datasets/test.txt')

a,b = map(int, f.readline().strip().split())
sum = 0

for i in range(a, b+1):
    if i % 2 != 0:
        sum += i

print(sum)

f.close()